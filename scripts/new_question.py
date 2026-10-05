"""Scaffold a question folder.

  python scripts/new_question.py <question-id> --title "…" --family "…" --attractor "…" \
      --question "…" --answer "…" [--why "…"] [--status answered|open] [--image file.png]

Creates questions/<id>/question.md, an empty landmarks.md, and routes/ attempts/ games/ with .gitkeep.
Refuses to overwrite. The reference answer is referee-only during play but public in the repo; write it
as a verifiable statement with a tolerance, not as a hint.
"""
import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id")
    ap.add_argument("--title", required=True)
    ap.add_argument("--family", required=True, help="comma-separated families, e.g. 'counting under symmetry, parity'")
    ap.add_argument("--attractor", default="none", help="the wrong-but-tempting approach the question pulls toward")
    ap.add_argument("--question", required=True)
    ap.add_argument("--answer", required=True, help="reference answer with tolerance; 'open' questions may say 'unknown'")
    ap.add_argument("--why", default="", help="why it is in the atlas (what strategies it should surface)")
    ap.add_argument("--status", default="answered", choices=["answered", "open"])
    ap.add_argument("--image", default="", help="image file name, already placed in the folder")
    args = ap.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", args.id):
        sys.exit("id must be lowercase words joined by hyphens")
    d = ROOT / "questions" / args.id
    if d.exists():
        sys.exit(f"{d} already exists")
    for sub in ("routes", "attempts", "games"):
        (d / sub).mkdir(parents=True)
        (d / sub / ".gitkeep").touch()
    fm = [f"id: {args.id}", f"title: {args.title}", f"status: {args.status}", f"added: {dt.date.today().isoformat()}",
          f"family: {args.family}", f"attractor: {args.attractor}"]
    if args.image:
        fm.insert(4, f"image: {args.image}")
    body = ["---", *fm, "---", "", "# Question", "", args.question.strip(), "", "# Reference answer (referee only)", "",
            args.answer.strip(), ""]
    if args.why:
        body += ["# Why it is in the atlas", "", args.why.strip(), ""]
    body += ["# Breadth", "", "No played or accepted routes yet.", ""]
    (d / "question.md").write_text("\n".join(body), encoding="utf-8")
    (d / "landmarks.md").write_text(f"# Frontier — landmarks used so far ({args.id})\n\nNo played chains yet. Only VALID chains bind the frontier.\n", encoding="utf-8")
    print(f"created questions/{args.id}/")


if __name__ == "__main__":
    main()
