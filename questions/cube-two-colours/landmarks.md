# Frontier — landmarks used so far (cube-two-colours)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | Rotation never changes the number of black faces, so cubes can be sorted into groups by black-face count. | route 001 | VALID |
| 2 | Two black faces form either an adjacent pair or an opposite pair, and three black faces form either a corner or a band, giving two cubes each. | route 001 | VALID |
| 3 | Swapping the two colours mirrors the groups with four, five and six black faces onto those with two, one and zero. | route 001 | VALID |
| 4 | A cube has three pairs of opposite faces, and each pair is both black, both white, or mixed. | route 002 | VALID |
| 5 | The number of mixed opposite pairs (0 to 3) is unchanged by rotation, so it splits the cubes into four classes. | route 002 | VALID |
| 6 | The classes contain four, three, two and one cubes respectively. | route 002 | VALID |
| 7 | Cubes with a both-black opposite pair can be turned so that pair is on top and bottom, leaving only the four-face belt to colour up to spinning. | route 003 | VALID |
| 8 | A belt of four faces has six patterns up to spinning, and each gives a different cube. | route 003 | VALID |
| 9 | Cubes with no both-black opposite pair number four, set by whether zero, one, two or three opposite pairs are mixed. | route 003 | VALID |
| 10 | Cubes with a mixed opposite pair can be turned so that the black face is on top and the white face is on the bottom, leaving a four-face belt to colour up to spinning. | route 004 | VALID |
| 11 | That belt has six patterns up to spinning, and they give six different cubes, because their black counts and band-or-corner shapes differ. | route 004 | VALID |
| 12 | Cubes with no mixed opposite pair number four, set by how many opposite pairs are both black. | route 004 | VALID |
