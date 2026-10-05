# Frontier — landmarks used so far (chessboard-adjacent-corners)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | The two removed squares a1 and h1 have opposite colors, so the color counts stay balanced. | route 003 | VALID |
| 2 | Rows 2 through 8 are untouched full rows, each tiled by horizontal dominoes. | route 003 | VALID |
| 3 | The leftover first row b1–g1 is an even-length unbroken run, tiled by three horizontal dominoes. | route 003 | VALID |
| 4 | The answer comes from an explicit tiling, not from a color-balance argument alone. | route 003 | VALID |
| 5 | Vertical dominoes in columns b–g across rows 1–2 fill the notched bottom strip, leaving only a2 and h2. | route 004 | VALID |
| 6 | The leftover squares a2 and h2 are rescued by vertical dominoes reaching up into row 3, which leaves b3–g3 as a clean even run. | route 004 | VALID |
| 7 | The board is split into a bottom three-row region built from vertical and edge dominoes and an untouched five-row remainder. | route 004 | VALID |
| 8 | Each half-board (left and right of the central seam) has an odd number of squares once a corner is removed. | route 001 | VALID |
| 9 | Dominoes inside a half cover an even number of its squares, so an odd number of dominoes must straddle the seam. | route 001 | VALID |
| 10 | One domino straddling the seam on the bottom row (d1–e1) fixes the parity, and each half then splits into even pieces. | route 001 | VALID |
| 11 | Rows 3 to 8 form an even-height full rectangle that vertical dominoes cover column by column. | route 002 | VALID |
| 12 | What is left is a two-row strip of fourteen squares, missing its two bottom corners. | route 002 | VALID |
| 13 | The strip's ends are closed off by horizontal dominoes in row 2 (a2b2 and g2h2), and the middle is filled by horizontal pairs. | route 002 | VALID |
