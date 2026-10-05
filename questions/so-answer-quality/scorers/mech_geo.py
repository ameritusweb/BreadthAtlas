"""Mechanism route: 📊 latent geometry only (belief n_effective, anisotropy, eccentricity, drift, …), read linearly."""
from mech_family_linear import family_margin

def score_pair(question: str, high: str, low: str) -> float:
    return family_margin("geo_", high, low)
