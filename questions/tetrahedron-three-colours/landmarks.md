# Frontier — landmarks used so far (tetrahedron-three-colours)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | The rotation group is the even permutations of the four faces, so rotation preserves each colour's face count. | route 001 | VALID |
| 2 | Sorting paintings by colour-count pattern gives 3 (all one colour), 6 (three and one), 3 (two and two) and 3 (two, one, one), with no all-different pattern. | route 001 | VALID |
| 3 | In the two, one, one pattern, a rotation can swap the two single faces while swapping the doubled pair, so there is only one picture per doubled colour. | route 001 | VALID |
| 4 | The rotation group is 2-transitive on the faces, so any set of faces of a given size can be moved to any other such set. | route 002 | VALID |
| 5 | With two colours, a painting is determined by how many faces get each colour. | route 002 | VALID |
| 6 | Sorting by the set of colours used gives one colour, exactly two colours, and all three colours, each counted separately. | route 002 | VALID |
| 7 | Because four faces and three colours force a repeated colour, swapping two equal faces absorbs any odd rearrangement, so rotations are as good as all rearrangements. | route 003 | VALID |
| 8 | Hence a painting up to rotation is exactly a multiset of four colours from three. | route 003 | VALID |
| 9 | Multisets are counted by placing two dividers among six slots in a row of faces. | route 003 | VALID |
| 10 | Removing one face of a chosen colour is a reversible correspondence between multisets of four with that colour present and multisets of three, so the count follows a recursion on size. | route 004 | VALID |
| 11 | Multisets of two colours from three split into three doubled and three mixed, giving six. | route 004 | VALID |
| 12 | Size-three multisets split into four without C and six with C, and size-four multisets into five without C and ten with C. | route 004 | VALID |
