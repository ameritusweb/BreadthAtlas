---
id: 002
question: tetrahedron-mirror-information
title: Rebuild from distances: fourth vertex has two mirror positions
strategy: new: reconstruct-and-count-solutions
contributor: sonnet (blind player 2)
date: 2026-10-05
depth: 2
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is sound and contains no simulation or calculation. Its first landmark is new: it rebuilds the tetrahedron from the distances, with the triangle fixing a plane and the fourth vertex left with exactly two possible positions. Route 001 instead applied a global mirror to an existing configuration and never reconstructed one. Its other two landmarks (the mirror pair, and the clockwise/counterclockwise orientation) match route 001's landmarks 1–2 in substance.
discriminator_depicted: no
typed_1: construction | fourth vertex | pairwise distances | exists | - | Three vertices fix a planar triangle, and the fourth vertex's three distances leave exactly two positions.
typed_2: symmetry | two positions of the fourth vertex | mirror twin | bijects | - | Those two positions are mirror images across the triangle's plane.
typed_3: obstruction | non-flat labelled tetrahedron | mirror twin | forbids | - | Seen from the fourth vertex, the three base corners run clockwise for one position and counterclockwise for the other.
---

CHAIN by blind player 2
1. 🔺 (root) — Four labelled vertices form a non-flat tetrahedron.
2. 📏 (root) — All six pairwise distances are given, with no positions or orientation-sensitive data.
3. ❓ (← 1, 2) — Asked: can the distances alone uniquely fix the handedness relative to a fixed external orientation? Yes or no.
4. 🧱 (← 2) — The three distances among the first three vertices fix a triangle's shape, which lies in a single plane.
5. 🪞 (← 4) — That plane divides space into two sides, an "above" and a "below".
6. 🎯 (← 2, 4) — The fourth vertex has a given distance to each of the three corners, so it can sit at only two points.
7. ⚖️ (← 5, 6) — The two points are reflections of each other across the triangle's plane, so they are equally far from every corner.
8. 🔁 (← 6, 7) — Choosing either point gives a tetrahedron that matches all six given distances.
9. 🤚 (← 1, 8) — Because the shape is non-flat, the fourth vertex is off the plane. Viewed from the fourth vertex, the three corners then run clockwise for one choice and counterclockwise for the other, so the two have opposite handedness.
10. 🧭 (← 3, 9) — A fixed external orientation cannot favour either choice, because the distance data are identical for both.
11. 👀 (← 1, 7) — Self-check: if the vertex were on the plane, the two points would merge and handedness would vanish. Non-flatness excludes this, so the two choices really are different.
12. 💥 (← 3, 8, 10) — A unique verdict would contradict the fact that both opposite-handed solutions fit the data.

LANDMARKS:
- Three vertices fix a planar triangle, and the fourth vertex's three distances leave exactly two positions.
- Those two positions are mirror images across the triangle's plane.
- Seen from the fourth vertex, the three base corners run clockwise for one position and counterclockwise for the other.

ANSWER: No. The distances do not uniquely determine the handedness, because both mirror-image tetrahedra fit them.
