"""Mechanism route: the trained network's own quality head (🌀 latent → 🌊 fields → routing+latent+eigen → ⚖️).
No fitting here: the score is the model's output for the answer."""
from poc4_components import load_cache, val_row

def score(question: str, answer: str) -> float:
    c = load_cache()
    row, side = val_row(answer)
    return float(c["val_qh"][row] if side == "h" else c["val_ql"][row])
