# Frontier — landmarks used so far (warp-one-chess)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | Ld4 is the only square around the king that the other White pieces leave uncovered. | attempt 001 | WRONG |
| 2 | A post-flip landing on Lf4 gives check from a square defended by the Lg3 pawn and covers Ld4 along rank 4. | attempt 001 | WRONG |
| 3 | With no Black piece on the Left board, the contact check cannot be answered on that board. | attempt 001 | WRONG |
| 4 | The rook on Lh1 and the pawn pair g3/h2 already shut Lf2's back rank and Lg3. | attempt 002 | WRONG |
| 5 | A knight moved to Ld2 guards Lf3, so a queen flipped there cannot be captured by the king. | attempt 002 | WRONG |
| 6 | A queen flipped to Lf3 from the Right board covers Le2, Le3 and Lg2 at the same moment. | attempt 002 | WRONG |
| 7 | A post-flip queen landing on Lg5, guarded by the Le4 knight, leaves the Black king only Lh3 on the Left board. | attempt 003 | WRONG |
| 8 | Queen Lg5–Lh5 checks down the h-file. The x-ray makes Kxh2 illegal, and the White king on Lf2 seals g2 and guards g3. | attempt 003 | WRONG |
| 9 | The White king acts as the decisive co-attacker in a corner net on the h-file. | attempt 003 | WRONG |
