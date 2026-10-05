# Frontier — landmarks used so far (plane-seat-98)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | Chaos ends as soon as seat 1 is taken, or when a taken seat's owner boards after passenger 98. | route 001 | VALID |
| 2 | Among seat 1 and seats 98, 99 and 100, each is equally likely to be the first one taken, by symmetry. | route 001 | VALID |
| 3 | Passenger 98 is displaced only if seat 98 is the first of those four seats taken, which is one case in four. | route 001 | VALID |
| 4 | Passengers who sit in their own seat can be deleted, so the hundred-seat plane collapses to a four-seat plane of the first passenger and passengers 98, 99 and 100. | attempt 001 | DUPLICATE |
| 5 | In the collapsed plane, the first passenger's single uniform choice among four seats decides everything. | attempt 001 | DUPLICATE |
| 6 | Only the pick of seat 98 displaces passenger 98, and the other three picks leave them in their seat. | attempt 001 | DUPLICATE |
| 7 | When passenger 98 boards, every seat from 2 to 97 is already occupied, so exactly three seats are free. | route 002 | VALID |
| 8 | Those three free seats are three of the four seats 1, 98, 99 and 100, so exactly one of those four is occupied. | route 002 | VALID |
| 9 | Passenger 98 is displaced only if the one occupied seat of the four is seat 98, which is one case in four. | route 002 | VALID |
| 10 | Splitting on the first passenger's pick, a pick in the middle just restarts the same problem with a displaced passenger as the new chooser. | route 003 | VALID |
| 11 | The chance that passenger 98 is displaced does not depend on how many passengers sit between the chooser and passenger 98. | route 003 | VALID |
| 12 | With no middle passengers the plane has four seats, and the bad pick is one of four. | route 003 | VALID |
