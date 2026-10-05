---
id: so-answer-quality
title: Mechanisms that rank the better Stack Overflow answer
status: answered
added: 2026-10-05
family: prediction, empirical referee, computable novelty
attractor: answer length (and its costumes: token count, code lines, number of paragraphs)
referee_script: scripts/so_referee.py
tools: Read
scorer_inline: true
source: the wave_vector project, external (poc4_triangulation.py, so_pairs_cache.pkl); path via external.local.json key wave_vector_root
---

# Question

Pairs of answers to the same Stack Overflow question are given, one scored at least three points
above the other. **Name a mechanism by which the better answer can be told from the worse, show it
as a chain, and prove it with a scorer** — a function from (question, answer) to a number — run on
the shared held-out pairs. Each route must rest on a mechanism whose margins do not merely track an
accepted route's.

Answer format (parsed by the code referee — exact): `ANSWER: mechanism <name>; scorer
scorers/<file>.py`. The scorer file defines `score(question: str, answer: str) -> float` (the margin
is the difference of the two answers' scores) or, for pair-trained readers, `score_pair(question,
high, low) -> float`. It may read `scorers/poc4_components.py` for the trained model's component
features (fitted on the train split only). The referee runs it on 4,000 held-out pairs: accuracy
below 0.60 is WRONG; margins correlating ≥ 0.80 with an accepted route's are DUPLICATE (and supersede
it if ≥ 0.05 more accurate); 0.50–0.80 is referred to the model referee with the number.

# Glossary

See SCOPE.md — domain concepts (📐 structure, 🎯 relevance, ✅ correctness, 🔗 coherence,
📏 completeness, 🪞 examples, ⚠️ caveats, ⏳ timing) and mechanism concepts (🔤 lexical, 🌀 latent,
🌊 field evolution, ⊥ orthogonality, 💥 residual, 🌳 NODE routing, 📊 geometry, 🔍 eigen, 🌲 GBM,
⚖️ margin) on equal footing.

# Reference answer (referee only)

There is no single answer; each route's claim is settled by code: pairwise accuracy ≥ 0.60 on the
held-out pairs (else WRONG), Spearman ρ < 0.80 against every accepted route's margins (else
DUPLICATE; 0.50–0.80 referred to the model referee with the number). The model referee rules on
whether the chain describes what the scorer does.

# Breadth

Seeded 2026-10-05 with the attractor and its first costume, all judged by code: route 001 sheer
length — VALID, acc 0.664 (level with the NODE-flowtron variant's 0.661; the triangulation+GBM
pipeline's 93.5 % CV is under its own protocol and is re-measured by the mechanism routes); attempt 001 word count —
DUPLICATE of route 001 at ρ 0.96; attempt 002 code share — WRONG, acc 0.577 below the floor.
Mechanism routes (2026-10-05, late): route 002 the network's quality head — VALID, acc 0.653, ρ 0.42
vs length (a second mechanism); attempts 003 geometry-only 0.577 and 004 eigen-only 0.565 — WRONG
(below floor); attempt 005 triangulation-only — DUPLICATE of 002 at ρ 0.93; attempt 006 GBM over all
families — DUPLICATE of 002 at ρ 0.86 with acc **0.766**, superseding it as the route's best instance.
Breadth after the first two played games: 4 mechanisms — route 003 a field-evolution component sign
vote (Opus, acc 0.641, ρ 0.64 vs length), route 004 completeness as a capped count of distinct content
kinds (Opus, acc 0.669, ρ 0.67); a hand-set "visible effort" cue sum was DUPLICATE of length at ρ 0.93.
Under the referee's protocol the project's reader scores 0.766, ten points over length; its published
93.5 % was cross-validated on validation-extracted features.
