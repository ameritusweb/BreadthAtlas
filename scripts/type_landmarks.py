"""Back-fill typed landmarks on accepted routes that lack them (LANDMARKS.md schema).

  python scripts/type_landmarks.py [question-id | all] [--model MODEL]

Routes are processed in depth order; each call sees the vocabulary already typed on the question so
subject/object phrases are reused and identity can be matched. Writes typed_N lines into the route's
frontmatter. Idempotent: routes that already have typed_1 are skipped.
"""
import argparse
import re
from pathlib import Path

from play import Question, Chain, ask, frontmatter, read, parse_typed, ROOT

PROMPT = """You are typing the landmarks of an accepted reasoning route for the Breadth Atlas so that route identity can be computed. Do not use tools.

QUESTION ({title}):
{question}

THE ROUTE'S CHAIN:
{chain}

THE ROUTE'S PLAIN LANDMARKS:
{landmarks}

Type each landmark, in order, as one line:
kind | subject | object | relation | yardstick | text
kind ∈ size, rate, limit, share, structure, symmetry, state, construction, obstruction, reduction, bound
relation ∈ ≈, ≫, ≪, =, ∈, bijects, alternates, invariant, forbids, exists, reduces-to
Use "-" for an empty field. subject and object are the two things the claim relates (the pool, a lifetime of drinking, the decisive seats). A UNIT or YARDSTICK (tanker load, bathtub, litres per day, body-full) goes ONLY in the yardstick field, never in subject or object; a claim that sizes one thing in a unit has object "-". REUSE the exact phrase already used for the same thing in the vocabulary below so that matching works. "text" is the landmark as written.

Vocabulary already typed on this question:
{vocab}

Reply with the heading TYPED LANDMARKS: followed by exactly one line per landmark and nothing else.
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question", nargs="?", default="all")
    ap.add_argument("--model", default="opus")
    ap.add_argument("--force", action="store_true", help="re-type routes that already have typed_N lines (strips the old ones)")
    ap.add_argument("--attempts", action="store_true", help="also type chains in attempts/ (needed to validate identity against DUPLICATE verdicts)")
    args = ap.parse_args()
    qids = [p.name for p in sorted((ROOT / "questions").iterdir()) if p.is_dir()] if args.question == "all" else [args.question]
    for qid in qids:
        q = Question(qid)
        routes = sorted(q.routes(), key=lambda f: int(frontmatter(read(f)).get("depth", 0)))
        if args.attempts:
            routes += [f for f in q.attempts() if frontmatter(read(f)).get("verdict") in ("DUPLICATE", "WRONG")]
        for f in routes:
            text = read(f)
            meta = frontmatter(text)
            if "typed_1" in meta and not args.force:
                continue
            if args.force:
                text = re.sub(r"(?m)^typed_\d+:.*\n", "", text)
                f.write_text(text, encoding="utf-8")
            body = text.split("---", 2)[-1].strip()
            chain = Chain(body)
            try:
                raw = ask(args.model, PROMPT.format(title=q.title, question=q.question, chain=chain.text,
                                                    landmarks="\n".join("- " + l for l in chain.landmarks), vocab=q.typed_vocabulary()))
            except RuntimeError as err:
                print(f"{qid} {f.parent.name[:-1]} {meta.get('id')}: skipped ({err})")
                continue
            typed = parse_typed(raw)
            if not typed:
                print(f"{qid} route {meta.get('id')}: no typed lines parsed")
                continue
            fm_end = text.index("---", 3)
            insert = "".join(f"typed_{i}: {t}\n" for i, t in enumerate(typed, 1))
            new_text = text[:fm_end] + insert + text[fm_end:]
            f.write_text(new_text, encoding="utf-8")
            print(f"{qid} {f.parent.name[:-1]} {meta.get('id')}: {len(typed)} typed")

if __name__ == "__main__":
    main()
