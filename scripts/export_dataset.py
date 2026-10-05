"""Export the whole archive — routes and attempts, verdicts, reasons, typed landmarks, repeats — as JSONL.

  python scripts/export_dataset.py [out.jsonl]

One record per judged chain. Nothing is filtered: the accepted routes are the interior of the space,
the rejected attempts are its boundary, and a model trained on only the first never learns the edge.
Fields: question, kind (route|attempt), id, title, strategy, contributor, date, depth, criterion,
referee, verdict, reason, repeats, empirical, typed (list), landmarks (list), answer, chain (text),
question_text, attractor, discriminator, family, status.
"""
import json
import sys
from pathlib import Path

from play import frontmatter, read, section, ROOT

def chain_parts(body):
    landmarks, answer = [], ""
    in_lm = False
    for line in body.splitlines():
        s = line.strip()
        if s.upper().startswith("LANDMARKS"):
            in_lm = True
            continue
        if s.upper().startswith("ANSWER"):
            answer = s.split(":", 1)[1].strip() if ":" in s else s
            in_lm = False
            continue
        if in_lm and s.startswith(("-", "•", "*")):
            landmarks.append(s.lstrip("-•* ").strip())
    return landmarks, answer

def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "snapshots" / "archive.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with out.open("w", encoding="utf-8") as fh:
        for qdir in sorted(p for p in (ROOT / "questions").iterdir() if p.is_dir()):
            qtext = read(qdir / "question.md") if (qdir / "question.md").exists() else ""
            qmeta = frontmatter(qtext)
            qbody = section(qtext, "Question")
            for kind in ("routes", "attempts"):
                for f in sorted((qdir / kind).glob("*.md")) if (qdir / kind).exists() else []:
                    text = read(f)
                    meta = frontmatter(text)
                    body = text.split("---", 2)[-1].strip()
                    landmarks, answer = chain_parts(body)
                    rec = {
                        "question": qdir.name, "kind": kind[:-1], "id": meta.get("id"), "title": meta.get("title"),
                        "strategy": meta.get("strategy"), "contributor": meta.get("contributor"), "date": meta.get("date"),
                        "depth": meta.get("depth"), "criterion": meta.get("criterion"), "referee": meta.get("referee"),
                        "verdict": meta.get("verdict"), "reason": meta.get("reason"), "repeats": meta.get("repeats"),
                        "empirical": meta.get("empirical"),
                        "typed": [meta[k] for k in sorted(k for k in meta if k.startswith("typed_"))],
                        "landmarks": landmarks, "answer": answer, "chain": body,
                        "question_text": qbody, "attractor": qmeta.get("attractor"), "discriminator": qmeta.get("discriminator"),
                        "family": qmeta.get("family"), "status": qmeta.get("status"),
                    }
                    fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    n += 1
    print(f"{n} records → {out}")

if __name__ == "__main__":
    main()
