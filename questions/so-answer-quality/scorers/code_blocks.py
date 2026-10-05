"""Candidate mechanism: 📐 structure — the share of the answer that is code (fenced or indented)."""
import re

def score(question: str, answer: str) -> float:
    fenced = sum(len(b) for b in re.findall(r"```.*?```", answer, re.S))
    indented = sum(len(line) for line in answer.splitlines() if line.startswith("    "))
    code = fenced + indented
    return code / (len(answer) + 1.0)
