---
route: 003
reader: sonnet
judge: opus
date: 2026-10-05
class: ABSORB
---

## Bare chain

1.🧑‍🤝‍🧑(root) 2.📅(root) 3.❓(← 1, 2) 4.🗄️(← 2) 5.🍰(← 1, 4) 6.🔝(← 5) 7.🪜(← 6) 8.🤝(← 7) 9.🔒(← 6, 8) 10.🎯(← 8, 9) 11.👀(← 3, 10)

## Reader

SETUP: A group of people and calendar days, probably the birthday problem. Days act as pigeonholes (🗄️), and each person is assigned a birthday (🍰).
QUESTION: Probably how many people are needed before two of them share a birthday with probability of at least 1/2, or with certainty.
SHAPE: Pigeonhole setup, then an upper bound (🔝) built by a step-by-step product or ladder (🪜). A match or collision (🤝) is then locked in as a bound (🔒) and hits the target threshold (🎯). The argument ends with a self-check against the question (👀).
ANSWER: 23 (a guess, from the birthday-problem reading; the pigeonhole certainty answer would be 366).
CONFIDENCE: low

## Judge

CLASS: ABSORB
SETUP_RECOVERED: partly
QUESTION_RECOVERED: no
REASON: The reader framed it as the classic birthday problem (days, 23, ≥1/2 threshold) and answered 23, missing the calendar-month twist and the pigeonhole certainty answer of 1.
