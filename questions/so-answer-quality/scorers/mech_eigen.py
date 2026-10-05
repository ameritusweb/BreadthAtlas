"""Mechanism route: 🔍 eigen decomposition of the routing distribution only, read linearly."""
from mech_family_linear import family_margin

def score_pair(question: str, high: str, low: str) -> float:
    return family_margin("eigen_", high, low)
