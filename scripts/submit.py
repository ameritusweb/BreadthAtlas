"""Submit a chain offline - no model, no API. For contributors (human or model) who cannot run a referee.

  python scripts/submit.py <question-id> <chain-file> --contributor "<name>"

The form checker (REFEREE.md section 1) runs in code. A chain that fails form is recorded at once under
attempts/ as ILL-FORMED, exactly as in play; the code referee is final on form. A chain that passes
form is queued under attempts/pending/ with verdict PENDING and does not touch the frontier until
someone with a referee runs scripts/judge_pending.py. Queued chains are not counted by the leaderboard.

The chain file is the chain text (numbered emoji steps, LANDMARKS, ANSWER last). It may start with a
frontmatter block giving `title:` and `strategy:`; those are carried into the queue entry.
"""
import argparse
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from play import Question, Chain, frontmatter, read, slug, CRITERION  # noqa: E402

TODAY = dt.date.today().isoformat()


def split_frontmatter(text):
    if text.lstrip().startswith("---"):
        parts = text.lstrip().split("---", 2)
        if len(parts) == 3:
            return frontmatter(text), parts[2].strip()
    return {}, text.strip()


def next_pending_id(q):
    pend = q.dir / "attempts" / "pending"
    pend.mkdir(parents=True, exist_ok=True)
    return pend, f"{len(list(pend.glob('*.md'))) + 1:03d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question")
    ap.add_argument("chain_file")
    ap.add_argument("--contributor", required=True, help='e.g. "claude-sonnet-4.5 (offline)" or "Jane Doe"')
    args = ap.parse_args()
    q = Question(args.question)
    meta, body = split_frontmatter(read(Path(args.chain_file)))
    chain = Chain(body)
    if not chain.check_form():
        cid = q.next_id("attempts")
        fm = [f"id: {cid}", f"question: {q.id}", f"title: {meta.get('title', '(form failure)')}",
              f"strategy: {meta.get('strategy', 'unclassified')}", f"contributor: {args.contributor}", f"date: {TODAY}",
              f"referee: code/{CRITERION}", f"criterion: {CRITERION}", "verdict: ILL-FORMED", f"reason: {'; '.join(chain.errors)}"]
        path = q.dir / "attempts" / f"{cid}-ill-formed.md"
        path.write_text("---\n" + "\n".join(fm) + "\n---\n\n" + body + "\n", encoding="utf-8")
        if chain.landmarks:
            q.append_landmarks(chain.landmarks, f"attempt {cid}", "ILL-FORMED")
        print(f"ILL-FORMED -> {path.relative_to(q.dir.parent.parent)}")
        for e in chain.errors:
            print(f"  - {e}")
        sys.exit(1)
    pend, pid = next_pending_id(q)
    fm = [f"id: {pid}", f"question: {q.id}", f"title: {meta.get('title', 'untitled')}",
          f"strategy: {meta.get('strategy', 'unclassified')}", f"contributor: {args.contributor}", f"date: {TODAY}",
          f"criterion: {CRITERION}", "verdict: PENDING", "reason: form passed in code; awaiting referee"]
    for n in chain.notes:
        fm.append(f"form_note: {n}")
    path = pend / f"{pid}-{slug(meta.get('title') or 'chain')}.md"
    path.write_text("---\n" + "\n".join(fm) + "\n---\n\n" + body + "\n", encoding="utf-8")
    print(f"PENDING -> {path.relative_to(q.dir.parent.parent)}  ({len(chain.steps)} steps, {len(chain.landmarks)} landmarks)")
    for n in chain.notes:
        print(f"  note: {n}")


if __name__ == "__main__":
    main()
