"""Estimate each question's route ceiling from the archive (species-richness estimator).

  python scripts/ceiling.py [question-id]

Every played chain is an observation of a route: an accepted route observes itself; a DUPLICATE
observes the earlier route named in its referee reason ("route 002", "chain 1", "attempt 003" → the
route that chain belongs to); WRONG and ILL-FORMED chains are observations of their strategy's route
when the referee named one, otherwise ignored. With observed routes S_obs, singletons f1 (routes seen
once) and doubletons f2 (seen twice), the bias-corrected Chao1 estimate is

    S_hat = S_obs + f1 (f1 - 1) / (2 (f2 + 1))

and breadth-so-far = S_obs / S_hat. Few games → wide uncertainty; the estimate is reported with the
raw counts so it can be read sceptically.
"""
import re
import sys
from collections import Counter
from pathlib import Path

from play import frontmatter, read

ROOT = Path(__file__).resolve().parent.parent

def observations(qdir):
    routes = {}
    for f in sorted((qdir / "routes").glob("*.md")) if (qdir / "routes").exists() else []:
        m = frontmatter(read(f))
        routes[m.get("id")] = m
    obs = Counter()
    for rid in routes:
        obs[rid] += 1
    unresolved = 0
    for f in sorted((qdir / "attempts").glob("*.md")) if (qdir / "attempts").exists() else []:
        m = frontmatter(read(f))
        reason = m.get("reason", "")
        hit = re.search(r"route\s+(\d{3})", reason)
        if hit and hit.group(1) in routes:
            obs[hit.group(1)] += 1
            continue
        # fall back to strategy match when exactly one accepted route has that strategy
        strat = m.get("strategy", "")
        same = [rid for rid, rm in routes.items() if rm.get("strategy") == strat and strat not in ("", "unclassified")]
        if m.get("verdict") == "DUPLICATE" and len(same) == 1:
            obs[same[0]] += 1
        else:
            unresolved += 1
    return routes, obs, unresolved

def chao1(obs):
    counts = list(obs.values())
    s_obs = len(counts)
    f1 = sum(1 for c in counts if c == 1)
    f2 = sum(1 for c in counts if c == 2)
    s_hat = s_obs + f1 * (f1 - 1) / (2 * (f2 + 1))
    return s_obs, f1, f2, s_hat

def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    print("| question | routes seen | singletons | doubletons | Chao1 ceiling | breadth so far | unresolved attempts |")
    print("|---|---|---|---|---|---|---|")
    for qdir in sorted(p for p in (ROOT / "questions").iterdir() if p.is_dir()):
        if only and qdir.name != only:
            continue
        routes, obs, unresolved = observations(qdir)
        if not routes:
            print(f"| `{qdir.name}` | 0 | – | – | – | – | {unresolved} |")
            continue
        s_obs, f1, f2, s_hat = chao1(obs)
        print(f"| `{qdir.name}` | {s_obs} | {f1} | {f2} | {s_hat:.1f} | {s_obs / s_hat:.0%} | {unresolved} |")

if __name__ == "__main__":
    main()
