---
id: 002
question: so-answer-quality
title: The network's own verdict: latent routing, geometry and eigen structure read by the quality head
strategy: new: learned-representation-reader
contributor: Claude Fable 5.1 (seed; scorer reads the trained poc4 model, no fitting)
date: 2026-10-05
depth: 2
referee: code/so_referee v0
criterion: v2
verdict: VALID
empirical: valid acc=0.653 rho_max=0.42 vs length-chars (n=4000); best instance: gbm-all-families acc=0.766 (attempt 005 supersedes)
scorer: scorers/mech_quality_head.py
note: Second mechanism on the question. ρ 0.42 against length — a different signal, not a costume. The triangulation-features reader (attempt 004, ρ 0.93) and the all-families GBM (attempt 005, ρ 0.86, acc 0.766) are the same mechanism read differently; the GBM is its best instance.
typed_1: structure | answer text | latent representation | reduces-to | VAE | The answer is compressed to a latent that fields then evolve.
typed_2: share | routing distribution | answer quality | ≈ | - | Where the evolved fields route mass, and its geometry, tracks quality.
typed_3: bound | learned reader | sheer length | ≈ | pairwise accuracy | The learned reader ranks the better answer about as often as length does, but on different pairs.
---

1. 📝 (root) — Given: a Stack Overflow question.
2. 💬 (root) — Given: two answers.
3. 🏆 (root) — Given: a score gap of at least three.
4. ❓ (← 1, 2, 3) — Asked: by what mechanism can the better answer be told from the worse?
5. 🔤 (← 2) — Each answer is tokenized by its distinctive words.
6. 🌀 (← 5) — A VAE compresses the token sequence into a latent representation.
7. 🌊 (← 6) — Three orthogonal fields evolve from the latent and route its mass across a grid.
8. 📊 (← 7) — The routing has a geometry — how concentrated, how anisotropic, how it drifts — and an eigen structure.
9. ⚖️ (← 7, 8) — A trained head reads routing, latent and eigen features together into a single score; the margin is the difference of the two answers' scores.
10. 👀 (← 9) — Self-check: this signal must differ from length in which pairs it gets right, or it is length in a costume; the correlation test decides.
11. 🏁 (← 9, 10) — Conclusion: the learned representation ranks the better answer above chance through a mechanism distinct from length.

LANDMARKS:
- The answer is compressed to a latent that fields then evolve.
- Where the evolved fields route mass, and its geometry, tracks quality.
- The learned reader ranks the better answer about as often as length does, but on different pairs.

ANSWER: mechanism learned routing geometry; scorer scorers/mech_quality_head.py
