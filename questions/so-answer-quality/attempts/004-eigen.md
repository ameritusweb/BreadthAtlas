---
id: 004
question: so-answer-quality
title: Eigen structure of the routing alone
strategy: new: single-family-reader
contributor: Claude Fable 5.1 (seed; scorer reads one component family of the trained poc4 model, fitted on the train split only)
date: 2026-10-05
referee: code/so_referee v0
criterion: v2
verdict: WRONG
empirical: weak acc=0.565 (floor 0.60)
scorer: scorers/mech_eigen.py
reason: The five eigen features of the routing distribution read linearly reach 0.565, below the floor.
---

1. 📝 (root) — Given: a Stack Overflow question.
2. 💬 (root) — Given: two answers.
3. 🏆 (root) — Given: a score gap of at least three.
4. ❓ (← 1, 2, 3) — Asked: by what mechanism can the better answer be told from the worse?
5. 🌀 (← 2) — The answer is compressed to a latent and routed by the evolved fields.
6. 🔍 (← 5) — Only the eigen decomposition of the routing distribution is read.
7. ⚖️ (← 6) — A reader fitted on training pairs turns that family alone into a score; the margin is the difference.
8. 👀 (← 7) — Self-check: the family must both reach the verdict and differ from accepted routes in which pairs it gets right.
9. 🏁 (← 7, 8) — Conclusion: eigen structure alone tracks quality weakly.

LANDMARKS:
- The routing's eigen spectrum carries some quality signal.
- Eigen features alone do not reach the verdict.

ANSWER: mechanism eigen structure; scorer scorers/mech_eigen.py