---
id: 001
question: so-answer-quality
title: The longer answer is the better one
strategy: new: dominant-surface-proxy
contributor: Claude Fable 5.1 (seed, hand-written)
date: 2026-10-05
depth: 1
referee: code/so_referee v0 (acc floor 0.60, dup ρ 0.80)
criterion: v2
verdict: VALID
empirical: valid acc=0.664 rho_max=0.00 (n=4000)
scorer: scorers/length_chars.py
note: The attractor route, seeded so the correlation test has a reference. Its accuracy is level with the NODE-flowtron variant (poc4_large, 0.661) and 1.5 points under the transformer baseline (0.679); the triangulation+GBM pipeline is measured separately by the mechanism routes.
typed_1: share | answer length | answer quality | ≈ | characters | Effort and coverage both grow with length, so length tracks quality.
typed_2: bound | sheer length | - | exists | pairwise accuracy | Length alone ranks the better answer about two times in three.
---

1. 📝 (root) — Given: a Stack Overflow question.
2. 💬 (root) — Given: two answers to it.
3. 🏆 (root) — Given: one answer's score is at least three above the other's.
4. ❓ (← 1, 2, 3) — Asked: by what mechanism can the higher-scored answer be told from the lower?
5. ✍️ (← 2) — An answer that explains more, shows more code and covers more cases is, other things equal, longer.
6. 👍 (← 3, 5) — Voters reward explanation, code and coverage, so the rewarded answer tends to be the longer one.
7. 📏 (← 5, 6) — Therefore sheer length is a proxy for the things voters reward.
8. ⚖️ (← 7) — Mechanism: score each answer by its length; the margin is the difference.
9. 👀 (← 8) — Self-check: the proxy must fail on padded or rambling answers, so it cannot be perfect — a real but weak signal.
10. 🏁 (← 8, 9) — Conclusion: length ranks the better answer well above chance, and the scorer proves it.

LANDMARKS:
- Effort and coverage both grow with length, so length tracks quality.
- Length alone ranks the better answer about two times in three.

ANSWER: mechanism sheer length; scorer scorers/length_chars.py
