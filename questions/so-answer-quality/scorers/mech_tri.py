"""Mechanism route: 💥 triangulation only — per-stage residuals, pairwise disagreement, evolution magnitudes — read linearly."""
from mech_family_linear import family_margin

def score_pair(question: str, high: str, low: str) -> float:
    return family_margin("tri_", high, low)
