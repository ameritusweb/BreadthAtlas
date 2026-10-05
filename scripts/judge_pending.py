"""Referee the offline queue: every chain under questions/*/attempts/pending/.

  python scripts/judge_pending.py [question-id | all] [--referee opus] [--dry-run]

Each queued chain is judged exactly as a played one: the empirical referee runs first where the
question has one, the model referee rules on soundness and novelty against the live frontier, verdicts
are recorded under routes/ or attempts/ with depth fixed at acceptance, landmarks are appended, and the
session is archived under games/ as a queue log. The queue entry is removed once recorded (its text and
provenance live on in the record). Queue order is submission order, so a later chain is judged against
any earlier one that was accepted.
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from play import (Question, Chain, ask, frontmatter, read, referee_prompt, parse_verdict, record_chain,  # noqa: E402
                  ROOT)


def judge_one(q, path, referee_model, game_log):
    text = read(path)
    meta = frontmatter(text)
    chain = Chain(text.split("---", 2)[-1].strip())
    chain.check_form()   # re-run under the current checker; notes go to the referee, errors are decisive
    if chain.errors:
        verdict = {"verdict": "ILL-FORMED", "reason": "; ".join(chain.errors), "route": meta.get("title", ""), "strategy": meta.get("strategy", "")}
    else:
        empirical = None
        if q.meta.get("referee_script"):
            script = (ROOT / q.meta["referee_script"]).resolve()
            if script.exists():
                r = subprocess.run([sys.executable, str(script), "--question", q.id], input=chain.text, capture_output=True, text=True, encoding="utf-8", timeout=900)
                empirical = (r.stdout.strip().splitlines() or [""])[-1]
                chain.notes.append(f"EMPIRICAL REFEREE RESULT (final on soundness of the cited line/scorer): {empirical}")
                game_log.append(f"\n<!-- empirical referee -->\n{empirical}\n")
        raw = ask(referee_model, referee_prompt(q, chain.text, f"queued chain {meta.get('id')}", chain.notes), tools=q.tools, allowed=q.allowed)
        if empirical and re.search(r"EMPIRICAL:\s*(not forced|illegal|weak)", empirical, re.I):
            raw = re.sub(r"VERDICT([^:]*):\s*[\w\-]+", r"VERDICT\1: WRONG", raw, count=1) + f"\n(overridden to WRONG: {empirical})"
        elif empirical and re.search(r"EMPIRICAL:\s*duplicate-of", empirical, re.I):
            raw = re.sub(r"VERDICT([^:]*):\s*[\w\-]+", r"VERDICT\1: DUPLICATE", raw, count=1) + f"\n(overridden to DUPLICATE: {empirical})"
        game_log.append(f"\n<!-- raw referee output -->\n{raw.strip()}\n")
        verdict = parse_verdict(raw)
        if empirical:
            verdict["reason"] = f"[{empirical}] " + verdict["reason"]
    contributor = meta.get("contributor", "?")
    model, _, label = contributor.partition(" (")
    label = label.rstrip(")") or "offline"
    ref, name = record_chain(q, chain, model.strip(), label, verdict, {"referee": referee_model}, game_log)
    # the record carries the submission date, not the judging date
    rec = q.dir / ("routes" if verdict["verdict"] == "VALID" else "attempts") / name
    rec.write_text(re.sub(r"(?m)^date:.*$", f"date: {meta.get('date', dt.date.today().isoformat())}\njudged: {dt.date.today().isoformat()}", read(rec), count=1), encoding="utf-8")
    path.unlink()
    print(f"  queued {meta.get('id')} -> {ref}: {verdict['verdict']} - {verdict['reason'][:140]}")
    return verdict["verdict"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question", nargs="?", default="all")
    ap.add_argument("--referee", default="opus")
    ap.add_argument("--dry-run", action="store_true", help="list the queue and exit")
    args = ap.parse_args()
    qids = [p.name for p in sorted((ROOT / "questions").iterdir()) if p.is_dir()] if args.question == "all" else [args.question]
    total = {}
    for qid in qids:
        pend = ROOT / "questions" / qid / "attempts" / "pending"
        queue = sorted(pend.glob("*.md")) if pend.exists() else []
        if not queue:
            continue
        print(f"{qid}: {len(queue)} queued")
        if args.dry_run:
            for p in queue:
                print(f"  {p.name}")
            continue
        q = Question(qid)
        stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        game_log = [f"# queue - {qid} - {stamp} - referee {args.referee}\n"]
        for p in queue:
            v = judge_one(q, p, args.referee, game_log)
            total[v] = total.get(v, 0) + 1
        (q.dir / "games" / f"{stamp}-queue.md").write_text("\n".join(game_log), encoding="utf-8")
    if total:
        print("judged:", ", ".join(f"{k} {v}" for k, v in sorted(total.items())))
        print("now run: python scripts/build_leaderboard.py && python scripts/strategy_map.py && python scripts/export_dataset.py && python scripts/build_site.py")
    elif not args.dry_run:
        print("queue empty")


if __name__ == "__main__":
    main()
