"""Mechanism route: 🌲 gradient-boosted trees over all extracted families (geo + eigen + triangulation + curvature),
fitted on the train split only — the project's own reader, measured under the referee's protocol."""
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier

from poc4_components import load_cache, val_row

_gbm = None

def gbm():
    global _gbm
    if _gbm is None:
        c = load_cache()
        d = c["train_h"] - c["train_l"]
        X = np.vstack([d, -d]); y = np.array([1] * len(d) + [0] * len(d))
        _gbm = GradientBoostingClassifier(n_estimators=200, max_depth=3, learning_rate=0.05, subsample=0.8, random_state=42).fit(X, y)
    return _gbm

def score_pair(question: str, high: str, low: str) -> float:
    c = load_cache()
    rh, sh = val_row(high); rl, sl = val_row(low)
    fh = (c["val_h"] if sh == "h" else c["val_l"])[rh]
    fl = (c["val_h"] if sl == "h" else c["val_l"])[rl]
    return float(gbm().decision_function((fh - fl)[None, :])[0])
