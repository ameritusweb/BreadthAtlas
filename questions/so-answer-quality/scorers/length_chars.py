"""Seed route (attractor): the longer answer is the better one. Mechanism: 📏 sheer length."""

def score(question: str, answer: str) -> float:
    return float(len(answer))
