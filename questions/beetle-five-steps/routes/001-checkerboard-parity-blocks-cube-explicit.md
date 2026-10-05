---
id: 001
question: beetle-five-steps
title: Checkerboard parity blocks cube; explicit octahedron five-loop
strategy: new: parity-colouring-plus-witness
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 1
referee: opus/v1
criterion: v1
verdict: VALID
reason: Every landmark is new because the frontier is empty: the two-colouring of the cube's corners forces even-length closed walks, and the explicit five-edge loop top → middle → bottom → adjacent middle → adjacent middle → top closes on the octahedron. Both the cube obstruction and the octahedron construction are sound, and the answer matches exactly.
typed_1: invariant | cube corners | closed walk length | invariant | parity | The cube's corners can be two-coloured so that every edge switches colour, so any closed walk on the cube has even length.
typed_2: obstruction | five-step walk | cube closed walk | forbids | parity | An odd number of steps cannot return to the starting colour, so five steps on the cube fail.
typed_3: construction | octahedron five-cycle | octahedron closed walk | exists | - | The octahedron has an explicit five-corner loop, going via the top, a middle corner, the bottom, and two adjacent middle corners.
---

CHAIN by duelist A
1. 🧊 (root) — Given: a cube has corners joined by edges, and each edge joins two corners.
2. 🪲 (root) — Given: a beetle starts at a corner and walks exactly five edges, moving to a new corner with each edge.
3. ❓ (← 1, 2) — Asked: can the beetle end at its starting corner on the cube, and likewise on an octahedron?
4. 🎨 (← 1) — The cube's corners can be painted in two colours, like a checkerboard, so that every edge joins two differently coloured corners.
5. 🔀 (← 2, 4) — Every step along an edge therefore switches the beetle's corner colour.
6. 5️⃣ (← 5) — Five steps is an odd number of switches, so the beetle ends on the colour opposite to where it began.
7. 🚫 (← 6) — A corner of the opposite colour cannot be the starting corner, so the cube walk cannot close.
8. 🔷 (root) — Given: an octahedron has six corners, a top, a bottom, and four forming a square around the middle.
9. 🔗 (← 8) — Each middle corner touches both the top and the bottom and its two square neighbours, while the top and bottom do not touch each other.
10. 🛤️ (← 3, 9) — Try the route top, middle one, bottom, middle two, middle three, back to top.
11. 👀 (← 9, 10) — Self-check: every hop in this route joins touching corners, and the five corners visited are all different.
12. ✅ (← 10, 11) — The route is a valid five-edge walk that returns to its start, so the octahedron allows it.
13. 🏁 (← 7, 12) — Combining the two cases: the cube says no and the octahedron says yes.

LANDMARKS:
- The cube's corners can be two-coloured so that every edge switches colour, so any closed walk on the cube has even length.
- An odd number of steps cannot return to the starting colour, so five steps on the cube fail.
- The octahedron has an explicit five-corner loop, going via the top, a middle corner, the bottom, and two adjacent middle corners.
ANSWER: Cube: no. Octahedron: yes.
