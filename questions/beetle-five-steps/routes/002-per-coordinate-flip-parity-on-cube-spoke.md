---
id: 002
question: beetle-five-steps
title: Per-coordinate flip parity on cube; spoke-ring pentagon on octahedron
strategy: new: coordinate-parity-invariant
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 2
referee: opus/v1
criterion: v1
verdict: VALID
reason: The chain is sound. Its first landmark is new: each cube edge flips exactly one of three position choices, and a return needs every choice flipped an even number of times. That tracks three separate parities, a different intermediate claim from route 001's single two-colouring. Its octahedron loop is also different: it uses the top and four ring corners and never passes through the bottom.
typed_1: invariant | cube corners | closed walk length | invariant | parity | Each cube edge changes exactly one of the three position choices, and a return needs each choice changed an even number of times, so closed cube walks have even length.
typed_2: structure | top corner | middle square ring | = | - | On the octahedron, the top corner touches all four corners of the middle square ring.
typed_3: construction | octahedron five-cycle | octahedron closed walk | exists | - | Two spokes from the top plus three ring edges make a five-edge closed walk on the octahedron.
---

CHAIN by duelist B
1. 🧊 (root) — Given: each cube corner is fixed by three binary choices (left or right, front or back, up or down), and each edge joins two corners.
2. 🪲 (root) — Given: a beetle starts at a corner and walks exactly five edges, moving to a new corner with each edge.
3. ❓ (← 1, 2) — Asked: can the beetle finish at its starting corner on the cube, and also on an octahedron?
4. 🧭 (← 1) — Walking along one cube edge changes exactly one of the three binary choices and leaves the other two alone.
5. 🔁 (← 4) — To end at the starting corner, each of the three choices must be changed an even number of times, so that each returns to its original value.
6. ➕ (← 5) — Three even tallies of changes add up to an even total, so any closed walk on the cube has an even number of edges.
7. 5️⃣ (← 2, 6) — Five edges is odd, so the beetle cannot be back at its start on the cube.
8. 🔷 (root) — Given: an octahedron has six corners, and each corner touches every other corner except its single opposite corner.
9. 🎡 (← 8) — Take the top corner and the four middle corners. The top touches all four, and the four middle corners form a square ring.
10. 🛤️ (← 3, 9) — Walk from the top to a middle corner, then around three sides of the ring to the middle corner next to where you began, then up to the top. That is two spokes and three ring edges, five edges in all.
11. 👀 (← 9, 10) — Self-check: every hop joins touching corners, and the five corners visited before returning are all different.
12. ✅ (← 10, 11) — This is a legitimate five-edge walk that returns to its start, so the octahedron allows it.
13. 🏁 (← 7, 12) — Combining the two cases: the cube cannot, the octahedron can.

LANDMARKS:
- Each cube edge changes exactly one of the three position choices, and a return needs each choice changed an even number of times, so closed cube walks have even length.
- On the octahedron, the top corner touches all four corners of the middle square ring.
- Two spokes from the top plus three ring edges make a five-edge closed walk on the octahedron.
ANSWER: Cube: no. Octahedron: yes.
