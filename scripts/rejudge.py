"""Re-judge an attempt under the current form checker and referee.

  python scripts/rejudge.py <question-id> <attempt-id> [--referee MODEL]

Used when a form rule or referee version changes. If the chain now passes form and the referee rules
VALID, the file moves to routes/ with a fresh id and depth; its landmark rows are updated. Otherwise the
attempt file's verdict and reason are rewritten in place. The original file is kept under
attempts/superseded/ either way, so the history survives.
"""
import argparse
import datetime as dt
import re
import shutil

import subprocess
import sys as _sys
from play import Question, Chain, ask, frontmatter, read, referee_prompt, parse_verdict, slug, CRITERION, ROOT

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question")
    ap.add_argument("attempt")
    ap.add_argument("--referee", default="opus")
    ap.add_argument("--form", default="v2", choices=["v1", "v2"], help="v1 = before the ❓ self-containment rule (chains played before it are judged under v1)")
    args = ap.parse_args()
    q = Question(args.question)
    # accepts "003" (an attempt) or "route:002" (an accepted route, which may be demoted)
    target = args.attempt
    pool = q.routes() if target.startswith("route:") else q.attempts()
    key = target.split(":", 1)[-1]
    matches = [f for f in pool if f.name.startswith(key)]
    if len(matches) != 1:
        raise SystemExit(f"{target}: {len(matches)} matches")
    src = matches[0]
    was_route = target.startswith("route:")
    text = read(src)
    meta = frontmatter(text)
    body = text.split("---", 2)[-1].strip()
    chain = Chain(body)
    today = dt.date.today().isoformat()
    superseded = q.dir / "attempts" / "superseded"
    superseded.mkdir(exist_ok=True)
    shutil.copy(src, superseded / f"{'route-' if was_route else ''}{src.stem}-{today}.md")

    if not chain.check_form(require_question=(args.form != "v1")):
        verdict = {"verdict": "ILL-FORMED", "reason": "; ".join(chain.errors), "route": meta.get("title", ""), "strategy": meta.get("strategy", "")}
    else:
        empirical = None
        if q.meta.get("referee_script"):
            script = (ROOT / q.meta["referee_script"]).resolve()
            if script.exists():
                r = subprocess.run([_sys.executable, str(script), "--question", q.id], input=chain.text, capture_output=True, text=True, encoding="utf-8", timeout=900)
                empirical = (r.stdout.strip().splitlines() or [""])[-1]
                chain.notes.append(f"EMPIRICAL REFEREE RESULT (final on soundness of the cited line/scorer): {empirical}")
                print(f"  {empirical}")
        raw = ask(args.referee, referee_prompt(q, chain.text, f"attempt {meta.get('id')} (re-judged)", chain.notes), tools=q.tools, allowed=q.allowed)
        if empirical and re.search(r"EMPIRICAL:\s*(not forced|illegal|weak)", empirical, re.I):
            raw = re.sub(r"VERDICT([^:]*):\s*[\w\-]+", r"VERDICT\1: WRONG", raw, count=1) + f"\n(overridden to WRONG: {empirical})"
        elif empirical and re.search(r"EMPIRICAL:\s*duplicate-of", empirical, re.I):
            raw = re.sub(r"VERDICT([^:]*):\s*[\w\-]+", r"VERDICT\1: DUPLICATE", raw, count=1) + f"\n(overridden to DUPLICATE: {empirical})"
        verdict = parse_verdict(raw)
        if empirical:
            verdict["reason"] = f"[{empirical}] " + verdict["reason"]
    print(f"re-judged attempt {meta.get('id')}: {verdict['verdict']} — {verdict['reason'][:160]}")

    old_ref = f"{'route' if was_route else 'attempt'} {meta.get('id')}"
    if verdict["verdict"] == "VALID" and was_route:
        # still valid: restamp in place
        text2 = re.sub(r"(?m)^criterion:.*$", f"criterion: {CRITERION}", text)
        text2 = re.sub(r"(?m)^referee:.*$", f"referee: {args.referee}/{CRITERION}", text2)
        src.write_text(text2.rstrip("\n") + f"\nnote: re-judged {today} under {CRITERION}: still VALID — {verdict['reason'][:160]}\n" if "note:" not in text2 else text2, encoding="utf-8")
        return
    if verdict["verdict"] != "VALID" and was_route:
        # demote to attempts
        aid = q.next_id("attempts")
        fm = [f"id: {aid}", f"question: {q.id}", f"title: {meta.get('title', '')}", f"strategy: {meta.get('strategy', 'unclassified')}",
              f"contributor: {meta.get('contributor', '?')}", f"date: {meta.get('date', today)}", f"referee: {args.referee}/{CRITERION}",
              f"criterion: {CRITERION}", f"verdict: {verdict['verdict']}", f"reason: {verdict['reason']}",
              f"note: demoted {today} from {old_ref} (was VALID under {meta.get('criterion', 'v1')})"]
        (q.dir / "attempts" / f"{aid}-{slug(meta.get('title') or 'demoted')}.md").write_text("---\n" + "\n".join(fm) + "\n---\n\n" + chain.text + "\n", encoding="utf-8")
        src.unlink()
        new_ref, new_verdict = f"attempt {aid}", verdict["verdict"]
    elif verdict["verdict"] == "VALID":
        rid = q.next_id("routes")
        depth = len(q.routes()) + 1
        fm = [f"id: {rid}", f"question: {q.id}", f"title: {verdict.get('route') or meta.get('title', '')}",
              f"strategy: {verdict.get('strategy') or 'unclassified'}", f"contributor: {meta.get('contributor', '?')}",
              f"date: {meta.get('date', today)}", f"depth: {depth}", f"referee: {args.referee}/{CRITERION}",
              f"criterion: {CRITERION}", "verdict: VALID", f"reason: {verdict['reason']}",
              f"note: re-judged {today} from {old_ref} ({meta.get('verdict')}: {meta.get('reason', '')[:120]})"]
        (q.dir / "routes" / f"{rid}-{slug(verdict.get('route') or 'route')}.md").write_text("---\n" + "\n".join(fm) + "\n---\n\n" + chain.text + "\n", encoding="utf-8")
        src.unlink()
        new_ref, new_verdict = f"route {rid}", "VALID"
    else:
        fm = [f"id: {meta.get('id')}", f"question: {q.id}", f"title: {verdict.get('route') or meta.get('title', '')}",
              f"strategy: {verdict.get('strategy') or meta.get('strategy', 'unclassified')}", f"contributor: {meta.get('contributor', '?')}",
              f"date: {meta.get('date', today)}", f"referee: {args.referee}/{CRITERION}", f"criterion: {CRITERION}",
              f"verdict: {verdict['verdict']}", f"reason: {verdict['reason']}",
              f"note: re-judged {today}; previously {meta.get('verdict')}: {meta.get('reason', '')[:120]}"]
        src.write_text("---\n" + "\n".join(fm) + "\n---\n\n" + chain.text + "\n", encoding="utf-8")
        new_ref, new_verdict = old_ref, verdict["verdict"]

    lm = q.dir / "landmarks.md"
    if lm.exists():
        lines = []
        for line in read(lm).splitlines():
            if f"| {old_ref} |" in line:
                line = re.sub(r"\|\s*" + re.escape(old_ref) + r"\s*\|\s*[A-Z\-]+\s*\|$", f"| {new_ref} | {new_verdict} |", line)
            lines.append(line)
        lm.write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
