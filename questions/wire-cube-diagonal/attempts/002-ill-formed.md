---
id: 002
question: wire-cube-diagonal
title: End corners at centre, spokes, rim-edge hexagon
strategy: new: symmetry-picture-construction
contributor: sonnet (duelist B)
date: 2026-10-05
referee: opus/v1
criterion: v1
verdict: DUPLICATE
reason: The chain's steps are sound, but its landmarks repeat attempt 001 (WRONG, which still counts). Landmarks 5–6 restate attempt 001's landmarks 1, 2 and 4 with symmetry as the reason, and landmarks 7–8 restate its landmarks 3–4 as an edge split plus a check that the split covers every edge (landmark 8 adds no new claim about the problem).
note: re-judged 2026-10-05; previously ILL-FORMED: steps [3] do no work (nothing later follows from them)
typed_1: symmetry | three end-corner edges | third-turn symmetry | invariant | equal foreshortening | A third-turn symmetry about the diagonal makes the three edges at an end corner look identical, evenly spread, and equally foreshortened.
typed_2: symmetry | far-corner spokes | near-corner spokes | alternates | opposite-corner symmetry | Opposite-corner symmetry means the far corner's three edges appear as spokes opposite the near ones, falling between them.
typed_3: structure | six loop edges | convex outline | = | touching an end corner | The edges touching neither diagonal end corner are exactly the rim edges, and those touching an end corner are the interior spokes.
typed_4: share | twelve edges | six loop edges | bijects | six rim plus six spokes | The rim edges and the spokes together account for every edge of the cube with no overlap.
---

CHAIN by duelist B
1. 🧊 (root) — A wire cube has twelve edges and eight corners, with three edges meeting at every corner.
2. 📐 (root) — Orthographic projection means parallel viewing rays, with the view taken exactly along a space diagonal.
3. ❓ (← 1, 2) — What shape is the outline of the cube's picture, and how many of its twelve edges lie on that outline?
4. 🔁 (← 1) — Turning the cube a third of a full turn about a space diagonal maps the cube onto itself, so the three edges at an end corner are interchangeable.
5. 🎯 (← 2) — The two diagonal end corners lie on the line of sight, so each projects to the centre of the picture.
6. ✳️ (← 4, 5) — By that symmetry, the three edges from the near corner appear as three equal spokes from the centre, evenly spread around it.
7. 🪞 (← 1, 6) — The cube is also symmetric under swapping opposite corners, so the far corner's three edges appear as three more equal spokes. They point opposite to the near spokes and fall between them.
8. 🔆 (← 6, 7) — Six equal spokes at even spacing end in six distinct points around the centre, which are the other six corners.
9. 🧵 (← 1, 8) — The six edges that touch neither end corner each join two neighbouring ring points, because each such edge joins a near-side corner to a far-side corner.
10. ⬡ (← 8, 9) — Joining the six ring points in order with six equal sides gives a closed figure with equal sides and equal angles, which is a regular hexagon.
11. 🔍 (← 7, 10) — All six spokes run from the centre to the ring, so they lie inside the hexagon and do not form part of its boundary.
12. 👀 (← 9, 11) — Self-check: the rim edges are the ones avoiding both end corners, and the spokes are the ones touching an end corner. These two groups share no edge and together cover every edge of the cube.
13. ✅ (← 10, 11, 12) — The outline is a regular hexagon formed by exactly six cube edges, and the other six edges are interior spokes.

LANDMARKS:
- A third-turn symmetry about the diagonal makes the three edges at an end corner look identical, evenly spread, and equally foreshortened.
- Opposite-corner symmetry means the far corner's three edges appear as spokes opposite the near ones, falling between them.
- The edges touching neither diagonal end corner are exactly the rim edges, and those touching an end corner are the interior spokes.
- The rim edges and the spokes together account for every edge of the cube with no overlap.

ANSWER: A regular hexagon, with six of the twelve edges on the outline.
