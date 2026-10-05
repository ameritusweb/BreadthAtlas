---
id: 003
question: so-answer-quality
title: train-weighted sign vote over field-evolution components
strategy: new: per-component-weighted-sign-vote
contributor: opus (blind player 2)
date: 2026-10-05
depth: 3
referee: opus/v2
criterion: v2
verdict: VALID
reason: [EMPIRICAL: ambiguous acc=0.641 rho=0.64 vs length-chars — model referee decides] The chain matches the scorer step by step: it uses only the tri_evo_ components, takes each component's direction and |win−0.5| weight from train pairs, and sums sign-weighted percentiles from pooled train answers. It scores 0.641 accuracy. Its margins correlate 0.64 with length-chars, which is below the duplicate threshold and leaves enough independent signal to count as a distinct mechanism. No accepted chain binds yet, so its landmarks (field-evolution magnitudes alone carry the signal; a per-component weighted vote from train win-rates; percentile scaling with no fitted direction) are new.
note: re-judged 2026-10-05 from attempt 008 (WRONG: Step 12 and the ANSWER line point to `scorers/evo_sign_vote.py`, but that file does not exist. The empirical referee the)
---

Note: I wasn't allowed to write `scorers/evo_sign_vote.py`, so the file does not exist yet and the referee can't run this route until it's saved. This is the intended content:

```python
"""Field-evolution sign vote: each tri_evo_* component casts a train-fitted, weighted vote."""
import numpy as np
from poc4_components import load_cache, val_row, family_columns

FAMILY = "tri_evo_"
_model = None

def _fit():
    global _model
    if _model is None:
        c = load_cache()
        cols = family_columns(c["names"].tolist(), FAMILY)
        th, tl = c["train_h"][:, cols], c["train_l"][:, cols]
        win = (th > tl).mean(axis=0)
        _model = dict(cols=cols, sign=np.where(win >= 0.5, 1.0, -1.0), weight=np.abs(win - 0.5),
                      pooled=np.sort(np.vstack([th, tl]), axis=0))
    return _model

def score(question: str, answer: str) -> float:
    m = _fit(); c = load_cache()
    try:
        row, side = val_row(answer)
    except KeyError:
        return 0.0
    x = (c["val_h"] if side == "h" else c["val_l"])[row, m["cols"]]
    n = m["pooled"].shape[0]
    pct = np.array([np.searchsorted(m["pooled"][:, j], x[j]) / n for j in range(len(x))])
    return float(np.sum(m["weight"] * m["sign"] * pct))
```

CHAIN by blind player 2
1. 📚 (root) — Each pair has two answers to one Stack Overflow question, and one answer scored at least three points higher than the other.
2. 🧠 (root) — A trained triangulation model exposes per-answer component features, fitted on the train split only. One family of these features, 🌊 field evolution, records how far the answer's latent fields move from stage to stage.
3. ❓ (← 1, 2) — Which mechanism separates the better answer from the worse one? It must be shown by a scorer that gets at least 0.60 accuracy on 4,000 held-out pairs, and its margins must not merely track another route's.
4. 🌊 (← 2) — Use only the field-evolution magnitudes, meaning how much the answer's representation is reworked as it passes through the stages.
5. 🔗 (← 4) — A coherent answer that builds an argument should push its fields through steadier, more purposeful movement than a scattered or off-target one, so evolution size should carry a quality signal.
6. 🗳️ (← 1, 5) — On the train pairs, check each evolution component on its own: how often does the better answer have the larger value? That fraction gives the component's preferred direction.
7. ⚖️ (← 6) — A component's vote weight is how far its train win-rate sits from a coin flip, so components that barely tell the answers apart count for almost nothing.
8. 📶 (← 4) — Replace each raw value with its percentile among the pooled train answers. All components then share one ordinal scale without dividing by any spread.
9. ➕ (← 6, 7, 8) — An answer's score is the weighted sum of its percentiles, each multiplied by the sign of its component's vote. This is a committee of independent votes, not one fitted direction.
10. 🎯 (← 1, 9) — Because both answers share the same question, the pair margin is just the difference of the two vote totals. The better answer should win whenever most of the confident components side with it.
11. 👀 (← 7, 9) — Self-check: if every component were a coin flip, all weights would be near zero and the margins would collapse toward zero instead of inventing a signal.
12. 🏁 (← 10) — The mechanism is a train-weighted sign vote over field-evolution components, ranked by percentile. It is run as the scorer evo_sign_vote.
LANDMARKS:
- Field-evolution magnitudes alone, meaning how much an answer's latent fields are reworked across stages, carry a quality signal.
- Each component votes on its own, with a direction and a confidence weight taken from its train win-rate against a coin flip.
- Percentile ranks among pooled train answers put the components on a common scale without any spread-based rescaling or fitted direction.
ANSWER: mechanism field-evolution sign vote; scorer scorers/evo_sign_vote.py
