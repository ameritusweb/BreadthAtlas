# Frontier — landmarks used so far (cube-three-colours)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | Cubes sort into disjoint classes by how many colours they use: three use one colour and eight per pair use exactly two. | route 001 | VALID |
| 2 | Cubes using all three colours split into the face-count patterns 4-1-1, 3-2-1 and 2-2-2, giving six, eighteen and six cubes. | route 001 | VALID |
| 3 | Cubes using all three colours total thirty. | route 001 | VALID |
| 4 | The rotation group has twenty-four elements, in five axis types of sizes 1, 6, 3, 8 and 6. | attempt 001 | ILL-FORMED |
| 5 | A painting is fixed by a rotation exactly when it is constant on each face-cycle, giving cycle counts 6, 3, 4, 2 and 3. | attempt 001 | ILL-FORMED |
| 6 | Burnside's lemma: the number of cubes equals the average number of fixed paintings, and the total over all rotations is 1368. | attempt 001 | ILL-FORMED |
| 7 | Each opposite pair of faces has one of six types: single-coloured in one of three colours, or mixed in one of three colour pairs. | route 002 | VALID |
| 8 | A cube is determined by the unordered collection of its three pair-types, giving fifty-six collections. | route 002 | VALID |
| 9 | Only the ab, bc, ca collection splits into two mirror-image cubes, which adds one. | route 002 | VALID |
| 10 | Cubes using only the colours of one chosen pair number ten, and two such families overlap only in one plain cube. | attempt 002 | DUPLICATE |
| 11 | Overlap correction: cubes using at most two of the three colours total twenty-seven. | attempt 002 | DUPLICATE |
| 12 | The at-most-two-colour cubes and the all-three-colour cubes are complementary, so the total is twenty-seven plus thirty. | attempt 002 | DUPLICATE |
