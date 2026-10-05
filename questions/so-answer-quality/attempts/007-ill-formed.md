---
id: 007
question: so-answer-quality
title: (form failure)
strategy: unclassified
contributor: opus (blind player 1)
date: 2026-10-05
referee: code/v2
criterion: v2
verdict: ILL-FORMED
reason: the answer is not the last line
---

I wasn't allowed to write `scorers/p1_linear_margin_reader.py`, so the scorer file that the ANSWER line below points to doesn't exist. If the referee runs now, this route fails. To fix it, grant write access and re-run, or save the code at the bottom of this message to that path yourself. I haven't run it, so the 0.60 accuracy threshold is not checked.

CHAIN by blind player 1
1. 📐 (root) — Each held-out item is a pair of answers to the same Stack Overflow question, and one of them scored at least three points above the other.
2. 🌳 (root) — A trained model already reads every answer and gives several groups of component features: geometry, eigen codes, triangulation leftovers, how the field changes over steps, curvature, and a quality-head score. All of it was fitted on the train split only.
3. ❓ (← 1, 2) — Name a mechanism that tells the better answer from the worse one, and back it with a scorer from (question, answer) to a number that gets at least 0.60 accuracy on the 4,000 held-out pairs.
4. ⚖️ (← 1) — Both answers respond to the same question, so whatever the question itself contributes affects both equally and drops out of the comparison; only how the two answers differ carries signal.
5. 📊 (← 2) — Each feature group catches a different trace of quality (structure, coherence, how the field settles), so no single group is likely to be the strongest signal by itself.
6. 🔍 (← 5) — The groups are measured on very different scales, so each feature is first rescaled by how much it varies across train answers, so that no group wins just because its numbers are bigger.
7. 🎯 (← 4, 6) — On the train pairs, take the high-minus-low difference of the rescaled features and fit one direction along which the better answer tends to sit further out.
8. 🔗 (← 7) — The direction is fitted to work both ways round (each pair also appears with high and low swapped and the opposite label), so the margin flips sign when the answers are swapped and needs no offset.
9. ⚠️ (← 7) — The fit includes a penalty that pulls weights toward zero, so features that are noisy or that repeat each other share weight instead of overfitting the train pairs.
10. ✅ (← 8, 9) — An answer's score is how far its rescaled features sit along that direction, and the margin is the better answer's score minus the worse answer's.
11. 👀 (← 2, 10) — Check: the fit uses only train rows and the held-out answers are only looked up, so no held-out label leaks into the scorer.
12. 🏁 (← 3, 10) — The mechanism is a linear margin reader across all the component groups, and its accuracy on the held-out pairs is the evidence for the route.

LANDMARKS:
- The question's contribution is the same for both answers, so only the difference between the answers matters (comparison within the pair).
- Rescale each component feature by how much it varies so that all groups count on equal terms.
- One direction, fitted on train pair differences with a penalty and both orderings, ranks answers by how far they sit along it.

ANSWER: mechanism linear-margin-reader; scorer scorers/p1_linear_margin_reader.py

```python
"""Blind player 1 route: a linear margin reader over the trained model's component features."""
import numpy as np
import poc4_components as C

_w = _mu = _sd = None

def _stack(feats, q):
    return np.nan_to_num(np.column_stack([feats, q]), nan=0.0, posinf=0.0, neginf=0.0)

def _fit():
    global _w, _mu, _sd
    c = C.load_cache()
    th = _stack(c["train_h"], c["train_qh"]); tl = _stack(c["train_l"], c["train_ql"])
    both = np.vstack([th, tl]); _mu = both.mean(0); _sd = both.std(0); _sd[_sd < 1e-9] = 1.0
    d = (th - tl) / _sd
    X = np.vstack([d, -d]); y = np.concatenate([np.ones(len(d)), np.zeros(len(d))])
    w = np.zeros(X.shape[1]); lam = 1.0
    for _ in range(50):  # Newton steps on L2-regularised logistic loss
        p = 1.0 / (1.0 + np.exp(-np.clip(X @ w, -30, 30)))
        g = X.T @ (p - y) + lam * w
        H = (X * (p * (1 - p))[:, None]).T @ X + lam * np.eye(X.shape[1])
        step = np.linalg.solve(H, g); w -= step
        if np.abs(step).max() < 1e-8:
            break
    _w = w

def score(question: str, answer: str) -> float:
    if _w is None:
        _fit()
    c = C.load_cache()
    try:
        row, side = C.val_row(answer)
    except KeyError:
        return 0.0
    feats = c["val_h"][row] if side == "h" else c["val_l"][row]
    q = c["val_qh"][row] if side == "h" else c["val_ql"][row]
    x = _stack(feats[None, :], np.array([q]))[0]
    return float(((x - _mu) / _sd) @ _w)
```
