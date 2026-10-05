"""Empirical referee for so-answer-quality: runs a route's scorer on the cached held-out pairs.

  python scripts/so_referee.py --question so-answer-quality < chain.txt
  python scripts/so_referee.py --scorer path/to/scorer.py [--name label] [--save]

The chain's ANSWER line must read:  ANSWER: mechanism <name>; scorer <path.py>
A scorer module defines  score(question: str, answer: str) -> float ; the margin for a pair is
score(q, high) - score(q, low). Verdict line (last line of output):
  EMPIRICAL: valid acc=0.xx rho_max=0.xx vs <route>      accuracy >= FLOOR and rho < AMBIG
  EMPIRICAL: ambiguous acc=0.xx rho=0.xx vs <route>      AMBIG <= rho < DUP  (model referee decides)
  EMPIRICAL: duplicate-of <route> rho=0.xx acc=0.xx      rho >= DUP
  EMPIRICAL: weak acc=0.xx                               accuracy below FLOOR  (WRONG: mechanism does not reach the verdict)
  EMPIRICAL: error — <detail>
Margins of valid routes are saved to questions/<q>/margins/<name>.npy for future comparisons.
"""
import argparse
import importlib.util
import pickle
import re
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from external import external  # noqa: E402

ATLAS = Path(__file__).resolve().parent.parent
CACHE = external("wave_vector_root") / "so_pairs_cache.pkl"
FLOOR, AMBIG, DUP = 0.60, 0.50, 0.80
SUPERSEDE = 0.05   # a duplicate this much more accurate than the route it duplicates becomes that route's best instance
MAX_PAIRS = 4000


def load_pairs():
    data = pickle.load(open(CACHE, "rb"))
    pairs = data["val_pairs"] if isinstance(data, dict) and "val_pairs" in data else data
    out = []
    for p in pairs[:MAX_PAIRS]:
        q = p.get("question_text") or p.get("question") or p.get("title") or ""
        out.append((q, p["high_text"], p["low_text"]))
    return out


def load_scorer(path):
    """Returns a function (question, high, low) -> margin. A scorer module may define either
    score(question, answer) -> float (margin = score(high) - score(low)) or, for pair-trained
    mechanisms, score_pair(question, high, low) -> float."""
    spec = importlib.util.spec_from_file_location("scorer_mod", path)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(Path(path).parent))
    spec.loader.exec_module(mod)
    if hasattr(mod, "score_pair"):
        return mod.score_pair
    if hasattr(mod, "score"):
        return lambda q, h, l: mod.score(q, h) - mod.score(q, l)
    raise RuntimeError("scorer module defines neither score(question, answer) nor score_pair(question, high, low)")


def spearman(a, b):
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    if ra.std() == 0 or rb.std() == 0:
        return 0.0
    return float(np.corrcoef(ra, rb)[0, 1])


def evaluate(scorer_path, question_id, name, save):
    pairs = load_pairs()
    margin_of = load_scorer(scorer_path)
    margins = np.array([margin_of(q, h, l) for q, h, l in pairs], dtype=float)
    acc = float((margins > 0).mean() + 0.5 * (margins == 0).mean())
    mdir = ATLAS / "questions" / question_id / "margins"
    mdir.mkdir(parents=True, exist_ok=True)
    rhos = []
    for f in sorted(mdir.glob("*.npy")):
        other = np.load(f)
        if len(other) == len(margins):
            rhos.append((abs(spearman(margins, other)), f.stem))
    rho_max, who = max(rhos) if rhos else (0.0, "-")
    if acc < FLOOR:
        return f"EMPIRICAL: weak acc={acc:.3f} (floor {FLOOR}) — the mechanism does not reach the verdict", margins
    if rho_max >= DUP:
        other = np.load(mdir / f"{who}.npy")
        other_acc = float((other > 0).mean() + 0.5 * (other == 0).mean())
        if acc >= other_acc + SUPERSEDE:
            np.save(mdir / f"{who}.npy", margins)   # the route's best instance now defines its margins
            return f"EMPIRICAL: duplicate-of {who} rho={rho_max:.2f} acc={acc:.3f} — supersedes it as the route's best instance (was {other_acc:.3f})", margins
        return f"EMPIRICAL: duplicate-of {who} rho={rho_max:.2f} acc={acc:.3f}", margins
    if rho_max >= AMBIG:
        return f"EMPIRICAL: ambiguous acc={acc:.3f} rho={rho_max:.2f} vs {who} — model referee decides", margins
    if save and name:
        np.save(mdir / f"{name}.npy", margins)
    return f"EMPIRICAL: valid acc={acc:.3f} rho_max={rho_max:.2f} vs {who} (n={len(margins)})", margins


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--question", default="so-answer-quality")
    ap.add_argument("--scorer")
    ap.add_argument("--name")
    ap.add_argument("--save", action="store_true")
    args = ap.parse_args()
    if args.scorer:
        verdict, _ = evaluate(args.scorer, args.question, args.name or Path(args.scorer).stem, args.save)
        print(verdict)
        return
    text = sys.stdin.read()
    m = re.search(r"ANSWER:\s*mechanism\s*(.+?);\s*scorer\s*(\S+)", text, re.I)
    if not m:
        print("EMPIRICAL: error — ANSWER line must read: mechanism <name>; scorer <path.py>")
        return
    name = re.sub(r"[^a-z0-9]+", "-", m.group(1).strip().lower()).strip("-")
    path = Path(m.group(2).strip().rstrip("."))
    if not path.is_absolute():
        path = ATLAS / "questions" / args.question / path
    if not path.exists():
        print(f"EMPIRICAL: error — scorer file not found: {path}")
        return
    try:
        verdict, _ = evaluate(str(path), args.question, name, save=True)
    except Exception as err:  # noqa: BLE001
        verdict = f"EMPIRICAL: error — {err}"
    print(verdict)


if __name__ == "__main__":
    main()
