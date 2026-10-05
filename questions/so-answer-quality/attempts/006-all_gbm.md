---
id: 006
question: so-answer-quality
title: Gradient-boosted trees over all extracted families
strategy: learned-representation-reader
contributor: Claude Fable 5.1 (seed; scorer reads one component family of the trained poc4 model, fitted on the train split only)
date: 2026-10-05
referee: code/so_referee v0
criterion: v2
verdict: DUPLICATE
empirical: duplicate-of quality-head rho=0.86 acc=0.766 — supersedes it as the route's best instance (was 0.653)
scorer: scorers/mech_all_gbm.py
supersedes: route 002
reason: ρ 0.86 with route 002: the same mechanism, read by the project's own GBM over geo + eigen + triangulation + curvature features fitted on the train split. Accuracy 0.766 on the held-out pairs — the best scorer on the question by ten points — so it supersedes route 002 as that route's best instance. Breadth unchanged. Note: the project's 93.5 % figure was cross-validation on features extracted from validation pairs; under the referee's protocol the same reader gives 0.766.
---

1. 📝 (root) — Given: a Stack Overflow question.
2. 💬 (root) — Given: two answers.
3. 🏆 (root) — Given: a score gap of at least three.
4. ❓ (← 1, 2, 3) — Asked: by what mechanism can the better answer be told from the worse?
5. 🌀 (← 2) — The answer is compressed to a latent and routed by the evolved fields.
6. 🌲 (← 5) — All extracted families — geometry, eigen, triangulation, stage curvature — are read together by boosted trees fitted on training pairs.
7. ⚖️ (← 6) — A reader fitted on training pairs turns that family alone into a score; the margin is the difference.
8. 👀 (← 7) — Self-check: the family must both reach the verdict and differ from accepted routes in which pairs it gets right.
9. 🏁 (← 7, 8) — Conclusion: the combined learned features rank the better answer well above length, through the mechanism route 002 already names.

LANDMARKS:
- The combined extracted features of the evolved fields carry the strongest quality signal found.
- That signal is the quality head's signal, read better.

ANSWER: mechanism combined field features; scorer scorers/mech_all_gbm.py