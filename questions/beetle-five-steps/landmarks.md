# Frontier — landmarks used so far (beetle-five-steps)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | The cube's corners can be two-coloured so that every edge switches colour, so any closed walk on the cube has even length. | route 001 | VALID |
| 2 | An odd number of steps cannot return to the starting colour, so five steps on the cube fail. | route 001 | VALID |
| 3 | The octahedron has an explicit five-corner loop, going via the top, a middle corner, the bottom, and two adjacent middle corners. | route 001 | VALID |
| 4 | Each cube edge changes exactly one of the three position choices, and a return needs each choice changed an even number of times, so closed cube walks have even length. | route 002 | VALID |
| 5 | On the octahedron, the top corner touches all four corners of the middle square ring. | route 002 | VALID |
| 6 | Two spokes from the top plus three ring edges make a five-edge closed walk on the octahedron. | route 002 | VALID |
| 7 | On the cube, the distance from the start (the number of position choices that differ) changes by exactly one on every edge, so its parity flips each step and five steps leave an odd, nonzero distance. | attempt 001 | DUPLICATE |
| 8 | On the octahedron, any two corners that are not opposite touch, so a walk can hop freely between the three opposite pairs. | attempt 001 | DUPLICATE |
| 9 | The route A, B, C, A′, B′, back to A is a five-edge closed walk on the octahedron. | attempt 001 | DUPLICATE |
| 10 | Every cube face has an even number of edges, and closed walks on the cube's surface are built from face outlines, so every closed walk on the cube has even length. | route 003 | VALID |
| 11 | Three triangular faces in a row around one octahedron corner have an outline of exactly five edges. | route 003 | VALID |
| 12 | That fan outline is a closed five-edge walk on the octahedron. | route 003 | VALID |
