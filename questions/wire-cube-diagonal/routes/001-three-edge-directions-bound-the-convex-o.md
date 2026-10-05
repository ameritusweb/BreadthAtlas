---
id: 001
question: wire-cube-diagonal
title: Three edge directions bound the convex outline's side count
strategy: new: direction-counting
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 1
referee: opus/v1
criterion: v1
verdict: VALID
reason: The chain is sound: it counts the edge directions and uses the shape's symmetry to bound and then fix the number of outline sides, giving the correct answer of a regular hexagon with 6 edges. Two landmarks are new: "a convex outline using only three directions has at most six sides, at most two per direction" and "each direction's four edges split two on the outline and two inside." No earlier chain passed through either claim.
typed_1: size | twelve edges | - | = | equal foreshortening | The diagonal is tilted equally to all three edge directions, so all twelve edges appear the same length, in three line-directions 60° apart.
typed_2: bound | convex outline | three line-directions | forbids | two sides per direction | A convex outline using only three directions has at most six sides, with at most two sides per direction.
typed_3: symmetry | convex outline | regular hexagon | = | central and third-turn symmetry | Central symmetry and third-turn symmetry together force exactly six sides, so the outline is a regular hexagon.
typed_4: share | twelve edges | convex outline | = | two of four per direction | Each direction's four edges split two on the outline and two inside, giving six on the outline.
---

CHAIN by duelist B
1. 🧊 (root) — Given: a cube has twelve edges, four parallel to each of three mutually perpendicular directions.
2. 👁️ (root) — Given: the view is orthographic, along a space diagonal from one corner through the centre to the opposite corner, and all edges are drawn as a wire frame.
3. ❓ (← 1, 2) — Asked: what shape is the outline of this picture, and how many of the twelve edges lie on the outline? This is not the familiar face-on square view.
4. 📐 (← 1, 2) — The diagonal is tilted equally to all three edge directions, so each direction is foreshortened by the same amount.
5. 🔱 (← 4) — With equal tilt, the three directions show up as lines evenly spread around the picture, 60° apart as lines.
6. 📏 (← 4) — Parallel edges are equal, and every direction is foreshortened equally, so all twelve edges appear the same length.
7. 🧩 (← 1, 5) — The whole picture is therefore built from segments in only three line-directions, four segments in each.
8. 🧱 (← 6, 7) — The outline is a closed convex shape made of equal-length segments drawn from those three directions.
9. 🔒 (← 5, 8) — A convex outline can use each direction for at most two sides, one on each opposite side, so it has at most six sides.
10. 🔄 (← 5, 9) — The cube is centrally symmetric, so the outline is too, and a triangle is ruled out. The outline also has a third-turn symmetry about the diagonal, which rules out a parallelogram. That leaves six sides, two per direction.
11. ⬡ (← 6, 9, 10) — Six equal sides with that symmetry make the outline a regular hexagon.
12. 🧮 (← 1, 7, 11) — Each direction has four edges, and two of them are hexagon sides. That gives six outline edges, and the other two per direction lie inside, as the six spokes.
13. 👀 (← 12) — Self-check: six outline edges plus six inner spokes make twelve, so none is missing or counted twice.
14. 🏁 (← 3, 11, 12) — The outline is a regular hexagon, and six edges lie on it.

LANDMARKS:
- The diagonal is tilted equally to all three edge directions, so all twelve edges appear the same length, in three line-directions 60° apart.
- A convex outline using only three directions has at most six sides, with at most two sides per direction.
- Central symmetry and third-turn symmetry together force exactly six sides, so the outline is a regular hexagon.
- Each direction's four edges split two on the outline and two inside, giving six on the outline.

ANSWER: A regular hexagon, with 6 of the 12 edges on the outline (the other 6 appear as spokes inside it).
