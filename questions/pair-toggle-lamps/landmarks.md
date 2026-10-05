# Frontier — landmarks used so far (pair-toggle-lamps)

No played chains yet. Only VALID chains bind the frontier.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | Each move changes the number of lit lamps by plus two, minus two, or zero. | route 001 | VALID |
| 2 | The parity of the lit count is an invariant of every move. | route 001 | VALID |
| 3 | The start has an even lit count (zero), but one lit lamp is odd, a contradiction. | route 001 | VALID |
| 4 | Moves are lines between lamp-dots, and a lamp is on exactly when its dot has an odd number of lines (a graph degree view). | route 002 | VALID |
| 5 | Double counting: every line has two ends, so the total of line-ends is even. | route 002 | VALID |
| 6 | Handshake principle: the number of odd-degree dots must be even, so exactly one odd dot is impossible. | route 002 | VALID |
| 7 | A move undoes itself and moves commute, so the final lit set is the combination of the chosen pairs with overlaps cancelling. | attempt 001 | DUPLICATE |
| 8 | The family of pairable (splittable into twosomes) lamp sets is closed under combining, and contains the start and every move. | attempt 001 | DUPLICATE |
| 9 | A single lit lamp is not pairable, so it lies outside everything reachable. | attempt 001 | DUPLICATE |
