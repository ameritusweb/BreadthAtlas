"""Shared: a linear reader over ONE feature family, fitted on the train split only.
Used by mech_geo.py, mech_eigen.py, mech_tri.py via FAMILY."""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from poc4_components import load_cache, val_row, family_columns

_models = {}

def reader(family):
    if family not in _models:
        c = load_cache()
        cols = family_columns(c["names"].tolist(), family)
        if not cols:
            raise RuntimeError(f"no features for family {family}")
        d = c["train_h"][:, cols] - c["train_l"][:, cols]
        X = np.vstack([d, -d]); y = np.array([1] * len(d) + [0] * len(d))
        sc = StandardScaler().fit(X)
        clf = LogisticRegression(max_iter=2000, C=0.5).fit(sc.transform(X), y)
        _models[family] = (cols, sc, clf)
    return _models[family]

def family_margin(family, high, low):
    cols, sc, clf = reader(family)
    c = load_cache()
    rh, sh = val_row(high); rl, sl = val_row(low)
    fh = (c["val_h"] if sh == "h" else c["val_l"])[rh, cols]
    fl = (c["val_h"] if sl == "h" else c["val_l"])[rl, cols]
    return float(clf.decision_function(sc.transform((fh - fl)[None, :]))[0])
