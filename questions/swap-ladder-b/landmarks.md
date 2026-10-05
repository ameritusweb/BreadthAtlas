# Frontier — landmarks used so far (swap-ladder-b)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | After rung 30 the row is D A C E H B F G L J K M. | attempt 001 | ILL-FORMED |
| 2 | Rungs 31–38 restore everything on the right to home order and bring B to rail 3. | attempt 001 | ILL-FORMED |
| 3 | The final row is A B D C E F G H J K L M, with only C and D swapped. | attempt 001 | ILL-FORMED |
| 4 | Rail 12 is never touched, so M never moves. | attempt 002 | ILL-FORMED |
| 5 | After rung 12 the row is C A D E H B F L G J K M. | attempt 002 | ILL-FORMED |
| 6 | Rung 41 swaps rails 5 and 6, turning F E into E F as the last step. | attempt 002 | ILL-FORMED |
| 7 | Rung 40 puts D on rail 3 and B on rail 2. | attempt 002 | ILL-FORMED |
| 8 | Rail 12 is never touched, so M is fixed. | attempt 003 | WRONG |
| 9 | An odd number of rungs means the overall rearrangement is odd, so it cannot be the identity. | attempt 003 | WRONG |
| 10 | The right block (E–M) nets out to the identity, and A and B return home. | attempt 003 | WRONG |
| 11 | The whole ladder amounts to a single swap of C and D. | attempt 003 | WRONG |
| 12 | Rail 12 is never touched by a rung, so M is fixed. | attempt 004 | WRONG |
| 13 | Forty-one rungs is an odd number of exchanges, so the net permutation is odd. | attempt 004 | WRONG |
| 14 | The net permutation is a single swap of C and D (rails 3 and 4), with every other token home. | attempt 004 | WRONG |
| 15 | The number of rungs is odd, so the overall permutation is odd and cannot be the identity. | attempt 005 | WRONG |
| 16 | Rail 12 is never touched, so M is fixed. | attempt 005 | WRONG |
| 17 | Repeated swaps on the same rail pairs cancel, so the whole ladder reduces to a single exchange of C and D. | attempt 005 | WRONG |
| 18 | Rail 12 is never touched, so M is fixed. | attempt 006 | WRONG |
| 19 | The odd rung count forces an odd net permutation, with at least one pair displaced. | attempt 006 | WRONG |
| 20 | The net effect is a single exchange of C and D, so D is on rail 3 and C is on rail 4. | attempt 006 | WRONG |
| 21 | Ten tokens, including M, are home. | attempt 006 | WRONG |
