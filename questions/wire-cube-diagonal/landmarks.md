# Frontier — landmarks used so far (wire-cube-diagonal)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | The near and far corners project onto the same point at the centre of the picture. | attempt 001 | WRONG |
| 2 | The other six corners form a ring of equal distance and equal spacing around the centre. | attempt 001 | WRONG |
| 3 | The outline joins the ring corners in order, and each hexagon side is one cube edge. | attempt 001 | WRONG |
| 4 | The six remaining edges are spokes from the centre to alternate hexagon corners, inside the outline. | attempt 001 | WRONG |
| 5 | A third-turn symmetry about the diagonal makes the three edges at an end corner look identical, evenly spread, and equally foreshortened. | attempt 002 | DUPLICATE |
| 6 | Opposite-corner symmetry means the far corner's three edges appear as spokes opposite the near ones, falling between them. | attempt 002 | DUPLICATE |
| 7 | The edges touching neither diagonal end corner are exactly the rim edges, and those touching an end corner are the interior spokes. | attempt 002 | DUPLICATE |
| 8 | The rim edges and the spokes together account for every edge of the cube with no overlap. | attempt 002 | DUPLICATE |
| 9 | The six edges avoiding both diagonal ends form one closed zigzag loop, a crown of corners alternating near and far, that circles the line of sight. | route 002 | VALID |
| 10 | The outline is the convex hull of the projected corners, and the end corners, which project to the centre, add nothing to it, so the loop alone makes the outline. | route 002 | VALID |
| 11 | Rotation and flip symmetry make the loop's six corners appear regular, so the hull is a regular hexagon whose sides are the loop edges. | route 002 | VALID |
| 12 | The diagonal is tilted equally to all three edge directions, so all twelve edges appear the same length, in three line-directions 60° apart. | route 001 | VALID |
| 13 | A convex outline using only three directions has at most six sides, with at most two sides per direction. | route 001 | VALID |
| 14 | Central symmetry and third-turn symmetry together force exactly six sides, so the outline is a regular hexagon. | route 001 | VALID |
| 15 | Each direction's four edges split two on the outline and two inside, giving six on the outline. | route 001 | VALID |
