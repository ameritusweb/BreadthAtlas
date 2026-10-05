---
id: 003
question: beetle-five-steps
title: Even face outlines force even closed walks
strategy: new: face-parity (closed walks built from even face boundaries)
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 3
referee: opus/v1
criterion: v1
verdict: VALID
reason: The first landmark is new: every cube face has an even outline, and closed walks on the cube's surface are built from face outlines, so every closed walk has even length. No earlier chain used this argument. The octahedron fan outline (spoke, three ring edges, spoke) matches route 002's landmark 6 in substance, but one new landmark is enough to make the chain VALID.
typed_1: invariant | cube corners | closed walk length | invariant | parity | Every cube face has an even number of edges, and closed walks on the cube's surface are built from face outlines, so every closed walk on the cube has even length.
typed_2: structure | three-triangle fan | fan outline | = | edges | Three triangular faces in a row around one octahedron corner have an outline of exactly five edges.
typed_3: construction | octahedron five-cycle | octahedron closed walk | exists | - | That fan outline is a closed five-edge walk on the octahedron.
---

CHAIN by duelist B
1. 🧊 (root) — Given: a cube has six square faces, each edge joins two corners, and each edge borders exactly two faces.
2. 🪲 (root) — Given: a beetle starts at a corner and walks exactly five edges, moving to a new corner with each edge.
3. ❓ (← 1, 2) — Asked: can the beetle finish at its starting corner on the cube, and also on an octahedron?
4. ⬜ (← 1) — Every cube face is bounded by exactly four edges, an even number.
5. 🧩 (← 1, 4) — The cube's surface has no holes, so the edges that a closed walk uses an odd number of times can be built by combining face outlines, where shared edges cancel in pairs.
6. 🔢 (← 4, 5) — Combining even-sized outlines with cancelling pairs always leaves an even number of edges, so the odd-use edges are even in number, and so is the total walk length.
7. 5️⃣ (← 2, 6) — Five edges is odd, so the beetle cannot be back at its start on the cube.
8. 🔷 (root) — Given: an octahedron has six corners and eight triangular faces, and four triangles meet at each corner.
9. 🔺 (← 8) — Around the top corner, take three triangles in a row, each sharing a spoke with the next.
10. 🧵 (← 3, 9) — The outer edge of this three-triangle fan is a spoke, three ring edges, and a second spoke, which is a closed route of five edges.
11. 👀 (← 9, 10) — Self-check: each hop lies on a triangle, so it is a real edge, and the five corners visited are all different.
12. ✅ (← 10, 11) — This is a legitimate five-edge walk that returns to its start, so the octahedron allows it.
13. 🏁 (← 7, 12) — Combining the two cases: the cube cannot, the octahedron can.

LANDMARKS:
- Every cube face has an even number of edges, and closed walks on the cube's surface are built from face outlines, so every closed walk on the cube has even length.
- Three triangular faces in a row around one octahedron corner have an outline of exactly five edges.
- That fan outline is a closed five-edge walk on the octahedron.
ANSWER: Cube: no. Octahedron: yes.
