"""Validate typed-landmark identity against the referee's novelty verdicts.

  python scripts/identity_check.py [question-id | all] [--resolution R0|R2]

Replays every judged chain of a question in play order (routes by depth, then attempts by id; the
true interleaving is approximated) and asks: does the typed identity say NEW (introduces a key no
earlier chain had) or DUP? Compares with the referee: VALID should be NEW, DUPLICATE should be DUP.
WRONG chains are shown but not scored (they are rejected on soundness, not novelty). Reports agreement
per question and the disagreements, which are where either the typer or the referee is wrong.
"""
import argparse
from pathlib import Path

from play import frontmatter, read, ROOT

def keys_of(meta, resolution):
    out = set()
    for k in sorted(k for k in meta if k.startswith("typed_")):
        parts = [p.strip().lower() for p in meta[k].split("|")]
        if len(parts) < 5:
            continue
        out.add(tuple(parts[:4]) + ((parts[4],) if resolution == "R2" else ()))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question", nargs="?", default="all")
    ap.add_argument("--resolution", default="R0", choices=["R0", "R2"])
    args = ap.parse_args()
    qdirs = [p for p in sorted((ROOT / "questions").iterdir()) if p.is_dir()] if args.question == "all" else [ROOT / "questions" / args.question]
    total_agree = total_scored = 0
    print(f"| question | scored | agree | VALID→DUP (typer too coarse) | DUPLICATE→NEW (typer too fine) | untyped |")
    print("|---|---|---|---|---|---|")
    disagreements = []
    for qdir in qdirs:
        chains = []
        for f in sorted((qdir / "routes").glob("*.md")) if (qdir / "routes").exists() else []:
            m = frontmatter(read(f)); chains.append((int(m.get("depth", 0)), "route", m))
        for f in sorted((qdir / "attempts").glob("*.md")) if (qdir / "attempts").exists() else []:
            m = frontmatter(read(f)); chains.append((1000 + int(m.get("id", "0") or 0), "attempt", m))
        chains.sort(key=lambda c: c[0])
        seen = set()
        agree = scored = vd = dn = untyped = 0
        for _, kind, m in chains:
            ks = keys_of(m, args.resolution)
            verdict = m.get("verdict", "")
            if not ks:
                untyped += 1
                continue
            new = bool(ks - seen)
            seen |= ks
            if verdict == "VALID":
                scored += 1
                if new: agree += 1
                else: vd += 1; disagreements.append((qdir.name, kind, m.get("id"), "VALID but typed-identity says DUP", m.get("title", "")))
            elif verdict == "DUPLICATE":
                scored += 1
                if not new: agree += 1
                else: dn += 1; disagreements.append((qdir.name, kind, m.get("id"), "DUPLICATE but typed-identity says NEW", m.get("title", "")))
        total_agree += agree; total_scored += scored
        if scored or untyped:
            print(f"| `{qdir.name}` | {scored} | {agree} | {vd} | {dn} | {untyped} |")
    print(f"\n{args.resolution}: {total_agree}/{total_scored} agree ({(total_agree / total_scored):.0%})" if total_scored else "nothing scored")
    for d in disagreements:
        print(f"- {d[0]} {d[1]} {d[2]}: {d[3]} — {d[4]}")

if __name__ == "__main__":
    main()
