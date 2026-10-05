---
id: 001
question: wire-cube-diagonal
title: Corners collapse to centre, ring of six forms hexagon
strategy: new: projected-vertex-ring
contributor: sonnet (duelist A)
date: 2026-10-05
referee: opus/v1
criterion: v1
verdict: WRONG
reason: Step 8 (🔄) says all six ring corners are the same distance from the centre and evenly spaced, and credits only the three-fold turn symmetry from step 5. That symmetry spaces each group of three evenly but does not give the two groups the same distance or put one group exactly between the other; that also needs the near-far (central) symmetry, which the chain never states, so step 8 and step 9's alternation do not follow from their named parents.
note: re-judged 2026-10-05; previously ILL-FORMED: steps [4] do no work (nothing later follows from them)
typed_1: state | near and far corners | centre of the picture | = | - | The near and far corners project onto the same point at the centre of the picture.
typed_2: symmetry | six ring corners | centre of the picture | invariant | third-turn symmetry | The other six corners form a ring of equal distance and equal spacing around the centre.
typed_3: structure | convex outline | six loop edges | bijects | one cube edge per hexagon side | The outline joins the ring corners in order, and each hexagon side is one cube edge.
typed_4: structure | six spoke edges | regular hexagon | alternates | - | The six remaining edges are spokes from the centre to alternate hexagon corners, inside the outline.
---

CHAIN by duelist A
1. 🧊 (root) — Given: a wire-frame cube has twelve edges and eight corners, with only the edges drawn.
2. 🔭 (root) — Given: it is viewed in orthographic projection, so parallel lines stay parallel and there is no perspective shrinking.
3. 🧭 (root) — Given: the line of sight runs exactly along a space diagonal, from one corner through the centre to the opposite corner.
4. ❓ (← 1, 2, 3) — Asked: what shape is the outline of the figure, and how many of the twelve edges lie on that outline?
5. 🎯 (← 3) — By symmetry the line of sight is equally tilted to the three edges meeting at the near corner, so those three edges look equally long and are spread evenly around the centre.
6. 🔻 (← 5) — The near corner and the far corner both land at the centre of the picture, hidden one behind the other.
7. 🔗 (← 1, 6) — Each of the other six corners is joined to the near corner or the far corner by an edge, so these six corners are the ones that remain around the centre.
8. 🔄 (← 5, 7) — Those six corners sit at equal distances from the centre and are evenly spaced around it by the three-fold turn symmetry about the line of sight, so they form a ring.
9. 🛑 (← 8) — Three of the six ring corners are neighbours of the near corner and three are neighbours of the far corner, and they alternate around the ring.
10. 📐 (← 8, 9) — Ring corners that are adjacent in the picture are one from each group, and each such pair is joined by a real cube edge, the ones that run along the sides of the cube between the two groups.
11. ⬡ (← 8, 10) — Joining six evenly spaced corners in order gives a regular hexagon, and the outline is this hexagon.
12. 🧮 (← 10, 11) — The hexagon has six sides, each made by one cube edge, so six edges lie on the outline.
13. ✳️ (← 1, 6, 12) — The other six edges are the three from the near corner and the three from the far corner, which run from the centre out to alternate hexagon corners and lie inside the outline.
14. 👀 (← 12, 13) — Self-check: six edges on the outline plus six spokes inside make all twelve edges, so nothing is missing or counted twice.

LANDMARKS:
- The near and far corners project onto the same point at the centre of the picture.
- The other six corners form a ring of equal distance and equal spacing around the centre.
- The outline joins the ring corners in order, and each hexagon side is one cube edge.
- The six remaining edges are spokes from the centre to alternate hexagon corners, inside the outline.

ANSWER: A regular hexagon, with 6 of the 12 edges on the outline.
