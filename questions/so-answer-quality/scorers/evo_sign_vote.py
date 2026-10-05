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
