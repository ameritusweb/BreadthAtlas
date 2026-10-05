# Frontier — landmarks used so far (swap-ladder)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | The ladder splits into independent blocks: rails 1–6, rail 7 alone, and rails 8–12. | attempt 001 | ILL-FORMED |
| 2 | The left block (A–F) returns completely to its starting order. | attempt 001 | ILL-FORMED |
| 3 | The right block ends as H, L, K, J, M, so L is on rail 9 and only J and L are displaced. | attempt 001 | ILL-FORMED |
| 4 | Rail 7 has no rung, so G is a fixed point that never moves. | attempt 002 | ILL-FORMED |
| 5 | On the right, H, K and M end on their own rails while J and L have swapped places. | attempt 002 | ILL-FORMED |
| 6 | Everything except J and L ends at home, so ten of the twelve tokens are back where they started. | attempt 002 | ILL-FORMED |
| 7 | Rail 7 is never touched, so the ladder splits into independent left (rails 1–6) and right (rails 8–12) blocks. | attempt 003 | WRONG |
| 8 | The left block's net effect is the identity. | attempt 003 | WRONG |
| 9 | The right block's net effect is a single swap of rails 9 and 11, which the odd rung count supports. | attempt 003 | WRONG |
| 10 | Rail 7 is untouched and no rung crosses between rails 6 and 8, so G is fixed and the ladder splits into two independent blocks. | attempt 004 | ILL-FORMED |
| 11 | The left block's rungs form a mirror-symmetric (palindromic) sequence that cancels pair by pair, leaving rails 1–6 unchanged. | attempt 004 | ILL-FORMED |
| 12 | The right block nets out to a single swap of J and L, which agrees with the parity of its rung count. | attempt 004 | ILL-FORMED |
| 13 | No rung crosses between rails 1–6, rail 7 and rails 8–12, so the ladder splits into independent blocks and G is untouched. | attempt 005 | WRONG |
| 14 | The left block (rails 1–6) cancels to the identity, so A–F are all back home. | attempt 005 | WRONG |
| 15 | The right block nets out to a single exchange of J and L (H, K and M return home), which puts L on rail 9. | attempt 005 | WRONG |
| 16 | Each rung is one transposition, so the whole ladder is a product of forty-one transpositions. | attempt 006 | WRONG |
| 17 | The odd rung count makes the final arrangement an odd permutation, which is never the identity. | attempt 006 | WRONG |
| 18 | At most ten of the twelve tokens can be back on their starting rails. | attempt 006 | WRONG |
