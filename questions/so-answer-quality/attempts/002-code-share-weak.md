---
id: 002
question: so-answer-quality
title: Share of the answer that is code
strategy: new: structural-signal
contributor: Claude Fable 5.1 (seed, hand-written)
date: 2026-10-05
referee: code/so_referee v0
criterion: v2
verdict: WRONG
empirical: weak acc=0.577 (floor 0.60)
scorer: scorers/code_blocks.py
reason: The mechanism is real but does not reach the verdict: 0.577 pairwise accuracy is below the 0.60 floor. Recorded as evidence that code share is a weaker signal than length on this split.
---

1. 📝 (root) — Given: a Stack Overflow question.
2. 💬 (root) — Given: two answers.
3. 🏆 (root) — Given: a score gap of at least three.
4. ❓ (← 1, 2, 3) — Asked: what mechanism separates them?
5. 📐 (← 2) — Answers are structured: prose, code blocks, lists.
6. 🧑‍💻 (← 1, 5) — Programming questions want code; an answer that shows code shows a solution.
7. 📊 (← 5, 6) — Measure the share of each answer that is code.
8. ⚖️ (← 7) — The margin is the difference in code share.
9. 👀 (← 8) — Self-check: a one-line correct snippet and a wall of wrong code both score high, so the share may mislead.
10. 🏁 (← 8) — Conclusion: code share ranks the better answer.

LANDMARKS:
- Programming answers are judged by whether they show a solution.
- The share of an answer that is code measures that.

ANSWER: mechanism code share; scorer scorers/code_blocks.py
