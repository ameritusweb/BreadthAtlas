"""Snap test: can the question be recovered from a route's bare emoji chain?

  python scripts/snap_test.py <question-id> [--reader MODEL] [--judge MODEL] [--routes 001,002]

For each accepted route, the explanations are stripped (emoji, (root) marks and parent tags only), a
blind reader infers the setup, the question and the answer, and a judge classifies the reading:
  RESOLVE  the reader recovered the actual question (including any alteration from a famous version)
  HEDGE    the reader saw the discriminator but would not commit (gave both the real and the famous reading)
  ABSORB   the reader snapped to the famous attractor, or to an unrelated problem, ignoring the discriminator
Results go to questions/<q>/snap/<route>-<reader>.md and a summary line is printed.
"""
import argparse
import datetime as dt
import re
from pathlib import Path

from play import Question, Chain, ask, frontmatter, read

READER_PROMPT = """You are taking part in an experiment about whether a chain of emoji can carry the meaning of a mathematical argument on its own. Do not use tools. Answer from the emoji alone.

The chain below was written by someone solving a math/logic puzzle. Each emoji after the givens follows from the earlier emoji named in its parent tag (← …); (root) marks a given; ❓ marks where the question is stated; 👀 marks a self-check; 💥 marks a contradiction; 🏁 marks the conclusion. You are NOT given the puzzle or the explanations.

{chain}

Infer, as precisely as you can:
SETUP: <the domain and physical/mathematical setup>
QUESTION: <the specific question being asked>
SHAPE: <the shape of the argument>
ANSWER: <your best guess at the answer, or "cannot determine">
CONFIDENCE: <low | medium | high>
Be honest about guesswork. Reply in exactly those five labelled lines.
"""

JUDGE_PROMPT = """You are judging a blind-reading experiment. Do not use tools.

A reader was shown only the emoji of a reasoning chain and asked to infer the problem. Classify the reading.

THE ACTUAL QUESTION ({title}):
{question}

THE ACTUAL ANSWER (reference):
{reference}

FAMOUS ATTRACTOR (a well-known problem this one resembles or departs from, if any): {attractor}

THE READER'S INFERENCE:
{reading}

Classify as exactly one of:
RESOLVE — the reader recovered the actual question, including whatever distinguishes it from the attractor, and its answer (if given) is the actual answer or compatible with it.
HEDGE — the reader noticed the distinguishing feature but did not commit: it offered both the actual reading and the attractor (or another) reading, or answered with both.
ABSORB — the reader landed on the attractor or on an unrelated problem, missing or explaining away what distinguishes the actual question.

Reply in exactly this format:
CLASS: RESOLVE | HEDGE | ABSORB
SETUP_RECOVERED: yes | partly | no
QUESTION_RECOVERED: yes | partly | no
REASON: <one sentence>
"""

def bare(chain):
    parts = []
    for st in chain.steps:
        tag = "(root)" if st["root"] else ("(← " + ", ".join(str(p) for p in st["parents"]) + ")" if st["parents"] else "")
        parts.append(f"{st['n']}.{st['emoji']}{tag}")
    return " ".join(parts)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question")
    ap.add_argument("--reader", default="sonnet")
    ap.add_argument("--judge", default="opus")
    ap.add_argument("--routes", default="")
    args = ap.parse_args()
    q = Question(args.question)
    out_dir = q.dir / "snap"
    out_dir.mkdir(exist_ok=True)
    wanted = set(args.routes.split(",")) if args.routes else None
    attractor = q.meta.get("attractor", "none")
    counts = {"RESOLVE": 0, "HEDGE": 0, "ABSORB": 0}
    for f in q.routes():
        meta = frontmatter(read(f))
        if wanted and meta.get("id") not in wanted:
            continue
        chain = Chain(read(f).split("---", 2)[-1])
        stripped = bare(chain)
        reading = ask(args.reader, READER_PROMPT.format(chain=stripped))
        judgement = ask(args.judge, JUDGE_PROMPT.format(title=q.title, question=q.question, reference=q.reference, attractor=attractor, reading=reading))
        cls = re.search(r"CLASS:\s*([A-Z]+)", judgement)
        cls = cls.group(1) if cls else "UNPARSED"
        counts[cls] = counts.get(cls, 0) + 1
        stamp = dt.date.today().isoformat()
        (out_dir / f"{meta.get('id', f.stem)}-{args.reader}.md").write_text(
            f"---\nroute: {meta.get('id')}\nreader: {args.reader}\njudge: {args.judge}\ndate: {stamp}\nclass: {cls}\n---\n\n"
            f"## Bare chain\n\n{stripped}\n\n## Reader\n\n{reading}\n\n## Judge\n\n{judgement}\n", encoding="utf-8")
        print(f"route {meta.get('id')}: {cls} — {judgement.splitlines()[-1][:120]}")
    print("summary:", counts)

if __name__ == "__main__":
    main()
