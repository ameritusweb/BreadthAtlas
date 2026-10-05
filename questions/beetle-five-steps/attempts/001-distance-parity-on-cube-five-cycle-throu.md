---
id: 001
question: beetle-five-steps
title: Distance-parity on cube, five-cycle through octahedron pairs
strategy: new: parity-obstruction-plus-construction
contributor: sonnet (duelist A)
date: 2026-10-05
referee: opus/v1
criterion: v1
verdict: DUPLICATE
reason: The cube landmark is route 001's two-colouring in other words: colouring each corner by whether its distance from the start is even or odd gives that colouring, and the edge argument repeats route 002's landmark 4. The octahedron landmarks repeat route 002's landmark 5 (by symmetry, each corner touches every corner except its opposite) and routes 001 and 002's explicit five-edge loop (landmarks 3 and 6), since A, B, C, A′, B′ is the same five-cycle up to symmetry.
typed_1: invariant | cube corners | closed walk length | invariant | parity | On the cube, the distance from the start (the number of position choices that differ) changes by exactly one on every edge, so its parity flips each step and five steps leave an odd, nonzero distance.
typed_2: structure | octahedron corners | opposite pairs | = | - | On the octahedron, any two corners that are not opposite touch, so a walk can hop freely between the three opposite pairs.
typed_3: construction | octahedron five-cycle | octahedron closed walk | exists | - | The route A, B, C, A′, B′, back to A is a five-edge closed walk on the octahedron.
---

CHAIN by duelist A
1. 🧊 (root) — Given: a cube has corners and edges, each edge joins two corners, and each corner is fixed by three binary choices (left or right, front or back, up or down).
2. 🪲 (root) — Given: a beetle starts at a corner and walks exactly five edges, moving to a new corner with each edge.
3. ❓ (← 1, 2) — Asked: can the beetle finish at its starting corner on the cube, and likewise on an octahedron?
4. 📏 (← 1) — Measure how far a corner is from the start by counting how many of the three choices differ from the start's. Walking one edge flips exactly one choice, so this distance changes by exactly one, up or down.
5. 🔀 (← 2, 4) — Every step therefore flips the parity of the beetle's distance, from even to odd or from odd to even.
6. 5️⃣ (← 5) — After five steps, an odd number of flips, the distance is odd.
7. 🚫 (← 6) — The start has distance zero, which is even, so the beetle cannot be back at its start after five steps on the cube.
8. 🔷 (root) — Given: an octahedron has six corners in three opposite pairs, and each corner touches every other corner except its own opposite.
9. 🔗 (← 8) — Call the pairs A and A′, B and B′, C and C′. Any two corners from different pairs touch.
10. 🛤️ (← 3, 9) — Try the route A, B, C, A′, B′, and back to A.
11. 👀 (← 9, 10) — Self-check: the hops A–B, B–C, C–A′, A′–B′ and B′–A each join corners from different pairs, so each is an edge, and the five corners visited are all different.
12. ✅ (← 10, 11) — This is a valid five-edge walk that returns to its start, so the octahedron allows it.
13. 🏁 (← 7, 12) — Combining the two cases: the cube cannot, the octahedron can.

LANDMARKS:
- On the cube, the distance from the start (the number of position choices that differ) changes by exactly one on every edge, so its parity flips each step and five steps leave an odd, nonzero distance.
- On the octahedron, any two corners that are not opposite touch, so a walk can hop freely between the three opposite pairs.
- The route A, B, C, A′, B′, back to A is a five-edge closed walk on the octahedron.

ANSWER: Cube: no. Octahedron: yes.
