"""Shared helper for mechanism routes: extracts per-answer features from the trained poc4 triangulation
model and caches them, so each scorer can read ONE component family and nothing else.

  python poc4_components.py build [--ckpt NAME.pt] [--n-train 3000] [--n-val 4000]

Cache: components_cache.npz next to this file — feature matrices for train (h/l) and val (h/l),
quality-head scores, feature names, and the val answer texts' order (aligned with so_pairs_cache
val_pairs, which is what so_referee iterates). Scorers map answer text -> row via that order.
Fitting (signs, linear readers, GBM) is always done on the TRAIN rows only.
"""
import argparse
import os
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ATLAS = HERE.parent.parent.parent
CACHE = HERE / "components_cache.npz"
DEFAULT_CKPT = "poc3_s2_t4_f3_ortho_product_project_tree_ep10.pt"

_cache = None


def load_cache():
    global _cache
    if _cache is None:
        if not CACHE.exists():
            raise RuntimeError(f"{CACHE} missing — run: python poc4_components.py build")
        _cache = dict(np.load(CACHE, allow_pickle=True))
        _cache["index"] = {t: i for i, t in enumerate(_cache["val_high_text"].tolist())}
        _cache["index_low"] = {t: i for i, t in enumerate(_cache["val_low_text"].tolist())}
    return _cache


def val_row(text):
    """Row index of a val answer by its text; (row, 'h'|'l')."""
    c = load_cache()
    if text in c["index"]:
        return c["index"][text], "h"
    if text in c["index_low"]:
        return c["index_low"][text], "l"
    raise KeyError("answer text not found among the cached val pairs")


def family_columns(names, family):
    return [i for i, n in enumerate(names) if n.startswith(family)]


# ---------------------------------------------------------------- build

def build(ckpt, n_train, n_val):
    import pickle
    import torch
    sys.path.insert(0, str(ATLAS / "scripts"))
    from external import external
    WV = external("wave_vector_root")
    sys.path.insert(0, str(WV))
    os.chdir(WV)
    import poc4_triangulation as P

    cache = pickle.load(open(WV / "so_token_cache.pkl", "rb"))
    pairs = pickle.load(open(WV / "so_pairs_cache.pkl", "rb"))["val_pairs"]
    vs = cache["vocab_size"]
    h_train, l_train = cache["h_train"][:n_train], cache["l_train"][:n_train]
    h_val, l_val = cache["h_val"][:n_val], cache["l_val"][:n_val]
    pairs = pairs[:n_val]

    tag = ckpt.replace("poc3_", "").split("_ep")[0]
    parts = tag.split("_")  # s2 t4 f3 ortho product project tree
    cfg = dict(n_stages=int(parts[0][1:]), n_steps=int(parts[1][1:]), n_fields=int(parts[2][1:]),
               angle=parts[3], interference=parts[4], conditioning=parts[5], stage_mode=parts[6] if len(parts) > 6 else "chain")
    print("model config from tag:", cfg)
    model = P.TriangulationModel(vs, P.DEVICE, dropout=0.0, skip_group=False, skip_prim=False, skip_stage=False,
                                 n_meta=0, field_shape=(32, 32), field_dim=64, **cfg)
    sd = torch.load(WV / ckpt, map_location=P.DEVICE, weights_only=True)
    missing, unexpected = model.load_state_dict(sd, strict=False)
    print(f"loaded {ckpt}: {len(sd)} tensors, missing {len(missing)}, unexpected {len(unexpected)}")
    if missing:
        print("  missing (first 8):", missing[:8])
    model.eval()

    def extract(h_tok, l_tok):
        feats_h, feats_l, q_h, q_l, names = [], [], [], [], None
        curv_flat = model.triangulation.curvature_field.view(-1)
        with torch.no_grad():
            for start in range(0, len(h_tok), 128):
                h_ids = torch.tensor(h_tok[start:start + 128], dtype=torch.long, device=P.DEVICE)
                l_ids = torch.tensor(l_tok[start:start + 128], dtype=torch.long, device=P.DEVICE)
                (h_sc, l_sc, h_routing, l_routing, h_af, l_af, h_lat, l_lat, _, _) = model.forward_batch(h_ids, l_ids)
                q_h += h_sc.float().cpu().tolist(); q_l += l_sc.float().cpu().tolist()
                h_eig = model.eigen_coder(h_routing).float().cpu().numpy()
                l_eig = model.eigen_coder(l_routing).float().cpu().numpy()
                tf = lambda vals: [v.item() if isinstance(v, torch.Tensor) else float(v) for v in vals]
                for i in range(len(h_ids)):
                    rows = []
                    for routing, lat, af, eig in ((h_routing, h_lat, h_af, h_eig), (l_routing, l_lat, l_af, l_eig)):
                        geo = [float(v.item() if isinstance(v, torch.Tensor) else v) for v in P.extract_geo_vec(model.geo_analyzer, routing[i], lat[i], curv_flat)]
                        res = tf(model.triangulation.triangulation_residual(af, sample_idx=i))
                        pw = tf(model.triangulation.pairwise_residuals(af, sample_idx=i))
                        evo = tf(model.triangulation.evolution_magnitudes(af, sample_idx=i))
                        curv = tf(model.triangulation.stage_curvature_features(af, sample_idx=i))
                        if names is None:
                            names = ([f"geo_{a}" for a in P.GEO_ATTRS] + [f"eigen_{k}" for k in range(len(eig[i]))]
                                     + [f"tri_res_{k}" for k in range(len(res))] + [f"tri_pw_{k}" for k in range(len(pw))]
                                     + [f"tri_evo_{k}" for k in range(len(evo))] + [f"curv_{k}" for k in range(len(curv))])
                        rows.append(geo + eig[i].tolist() + res + pw + evo + curv)
                    feats_h.append(rows[0]); feats_l.append(rows[1])
                print(f"\r  extracted {min(start + 128, len(h_tok))}/{len(h_tok)}", end="")
        print()
        return np.array(feats_h, dtype=float), np.array(feats_l, dtype=float), np.array(q_h), np.array(q_l), names

    print("train:")
    tr_h, tr_l, tr_qh, tr_ql, names = extract(h_train, l_train)
    print("val:")
    va_h, va_l, va_qh, va_ql, _ = extract(h_val, l_val)
    np.savez(CACHE, train_h=tr_h, train_l=tr_l, train_qh=tr_qh, train_ql=tr_ql,
             val_h=va_h, val_l=va_l, val_qh=va_qh, val_ql=va_ql, names=np.array(names),
             val_high_text=np.array([p["high_text"] for p in pairs], dtype=object),
             val_low_text=np.array([p["low_text"] for p in pairs], dtype=object), ckpt=ckpt)
    print(f"cached {len(names)} features for {len(tr_h)} train and {len(va_h)} val pairs → {CACHE}")
    print(f"quality head alone on val: acc={(va_qh > va_ql).mean():.3f}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build"])
    ap.add_argument("--ckpt", default=DEFAULT_CKPT)
    ap.add_argument("--n-train", type=int, default=3000)
    ap.add_argument("--n-val", type=int, default=4000)
    a = ap.parse_args()
    build(a.ckpt, a.n_train, a.n_val)
