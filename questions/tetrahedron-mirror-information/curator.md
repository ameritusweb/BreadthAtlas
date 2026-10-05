# Curator notes — unjudged candidate

This file contains solution hypotheses. It is not a played route, is not scored, and must not be supplied as player input.

## Candidate chain

1. 🔺 (root) — The labelled tetrahedron is non-flat.
2. 📏 (root) — Only its pairwise vertex distances are supplied.
3. 🧭 (root) — Handedness is defined relative to a fixed external orientation.
4. ❓ (← 1, 2, 3) — Can these distances uniquely determine handedness?
5. 🪞 (← 1, 3) — Reflect a configuration to produce one of opposite handedness.
6. ↔️ (← 2, 5) — Reflection preserves every corresponding pairwise distance.
7. 📋 (← 2, 6) — The original and reflected configurations give the same observation record.
8. 🎭 (← 5, 7) — This record is compatible with opposite handednesses.
9. 🔍 (← 7, 8) — Evidence confined to the record cannot select between them.
10. ❔ (← 4, 8, 9) — The supplied data leave handedness unresolved.
LANDMARKS:
- Reflection changes handedness while preserving every supplied distance.
- A single observation record admits opposite answers.
ANSWER: No; a mirror ambiguity remains.

## Other conceptual spines to investigate

indistinguishable pair; observation-preserving transformation

## Boundary variant

Add a measurement that states on which oriented side of the labelled face ABC vertex D lies; this resolves handedness.
