---
id: 001
question: so-answer-quality
title: Word count as the measure of effort
strategy: dominant-surface-proxy
contributor: Claude Fable 5.1 (seed, hand-written)
date: 2026-10-05
referee: code/so_referee v0
criterion: v2
verdict: DUPLICATE
empirical: duplicate-of length-chars rho=0.96 acc=0.641
scorer: scorers/token_count.py
reason: Per-pair margins correlate with route 001 at ρ = 0.96 — the same mechanism in a different unit. Decided by code, no referee reading required.
---

1. 📝 (root) — Given: a Stack Overflow question.
2. 💬 (root) — Given: two answers.
3. 🏆 (root) — Given: a score gap of at least three.
4. ❓ (← 1, 2, 3) — Asked: what mechanism separates them?
5. 🗣️ (← 2) — An answer is made of words; more words means more said.
6. 👍 (← 3, 5) — Voters reward answers that say more.
7. 🔢 (← 5, 6) — Count the words of each answer.
8. ⚖️ (← 7) — The margin is the word-count difference.
9. 👀 (← 8) — Self-check: words and characters move together, so this may be length in another coat.
10. 🏁 (← 8) — Conclusion: word count ranks the better answer.

LANDMARKS:
- Saying more wins votes.
- Word count measures how much is said.

ANSWER: mechanism word count; scorer scorers/token_count.py
