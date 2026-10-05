"""Costume candidate: word count. Expected to be a duplicate of length_chars by the correlation test."""

def score(question: str, answer: str) -> float:
    return float(len(answer.split()))
