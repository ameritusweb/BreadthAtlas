---
id: 002
question: wire-cube-diagonal
title: Zigzag crown of edges forms the hull outline
strategy: new: invariant-substructure (find the edge cycle the symmetry preserves, then take its hull)
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 2
referee: opus/v1
criterion: v1
verdict: VALID
reason: The steps hold up: the six edges that avoid both diagonal ends do form a closed zigzag. Two cube symmetries make that loop appear as a regular hexagon, and its edges are the outline. The new landmarks are the closed loop alternating near and far around the line of sight (9) and the outline as the convex hull fixed by that loop alone (10); neither appears in attempts 001–002, which came before it.
note: re-judged 2026-10-05 from attempt 003 (ILL-FORMED: steps [3] do no work (nothing later follows from them))
typed_1: structure | six loop edges | line of sight | alternates | - | The six edges avoiding both diagonal ends form one closed zigzag loop, a crown of corners alternating near and far, that circles the line of sight.
typed_2: reduction | convex outline | six loop edges | reduces-to | convex hull of projected corners | The outline is the convex hull of the projected corners, and the end corners, which project to the centre, add nothing to it, so the loop alone makes the outline.
typed_3: symmetry | convex outline | regular hexagon | = | third-turn and flip symmetry | Rotation and flip symmetry make the loop's six corners appear regular, so the hull is a regular hexagon whose sides are the loop edges.
---

CHAIN by duelist A
1. 🧊 (root) — Given: a cube has 8 corners and 12 equal edges, and each edge joins two corners.
2. 👁️ (root) — Given: the view is orthographic, looking exactly along a space diagonal, from one corner through the centre to the opposite corner.
3. ❓ (← 1, 2) — Asked: what shape is the outline of the wire cube seen this way, and how many of its twelve edges lie on that outline? Only edges are drawn, with no faces.
4. 🔄 (← 1) — The six corners that are not diagonal ends are three neighbours of the near end and three neighbours of the far end. Each near neighbour is joined by an edge to two far neighbours. So six edges form one closed zigzag loop through those six corners and avoid both end corners.
5. ↕️ (← 4) — Going round the loop, the corners alternate between the near side and the far side of the cube. The loop is a crown wrapped around the waist of the cube, circling the line of sight.
6. 🔺 (root) — Given: the outline of a see-through solid in orthographic view is the convex hull of its projected corners.
7. 🔁 (← 4, 5) — A third-turn about the diagonal carries the loop onto itself, and so does the half-turn flip that swaps near and far. So the six loop corners appear equally spaced and equally distant around the picture's centre.
8. 🎯 (← 4, 6) — The two end corners lie on the line of sight, so they project to the centre, inside the ring of the six loop corners. The hull is therefore fixed by the six loop corners alone.
9. ⬡ (← 6, 7, 8) — The convex hull of six equally spaced, equidistant points is a regular hexagon. So the outline is a regular hexagon.
10. 🔢 (← 4, 9) — Neighbouring hexagon corners are neighbours in the loop, so each hexagon side is a loop edge. Six edges lie on the outline.
11. 🧮 (← 4, 10) — The other six edges each touch an end corner, which projects to the centre. They run from the centre to the rim and lie inside the outline.
12. 👀 (← 10, 11) — Self-check: six edges on the rim plus six edges inside make twelve, so every edge is counted once.

LANDMARKS:
- The six edges avoiding both diagonal ends form one closed zigzag loop, a crown of corners alternating near and far, that circles the line of sight.
- The outline is the convex hull of the projected corners, and the end corners, which project to the centre, add nothing to it, so the loop alone makes the outline.
- Rotation and flip symmetry make the loop's six corners appear regular, so the hull is a regular hexagon whose sides are the loop edges.
ANSWER: A regular hexagon, with 6 of the 12 edges on the outline (the other 6 lie inside it).
