# Frontier — landmarks used so far (plane-seat-99)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | When passenger 99 boards, exactly two seats are free, and seats 2–98 are all already filled. | route 001 | VALID |
| 2 | Exactly one of seats 1, 99 and 100 is occupied at that moment, and each of the three is equally likely to be that one. | route 001 | VALID |
| 3 | Passenger 99 is displaced only if that occupied seat is seat 99, which is a one-in-three chance. | route 001 | VALID |
| 4 | Displaced passengers form a forward-moving relay of random picks, and the relay stops the moment someone picks seat 1. | route 002 | VALID |
| 5 | Picking seat 100 only affects passenger 100, who boards after passenger 99, so it never harms passenger 99. | route 002 | VALID |
| 6 | The first relay pick to touch seat 1, seat 99 or seat 100 is equally likely to be any of the three. | route 002 | VALID |
| 7 | Seats 99 and 100 are interchangeable before passenger 99 boards, so "seat 99 is the occupied one" and "seat 100 is the occupied one" are equally likely. | route 003 | VALID |
| 8 | Passenger 100 loses their seat half the time, and that half is the whole seat-100 case plus half of the seat-99 case, because a displaced passenger 99 picks between seats 1 and 100 by a fair coin. | route 003 | VALID |
| 9 | Matching those two facts shows the seat-99 case is exactly one third of the possibilities. | route 003 | VALID |
| 10 | After passenger 1 takes a seat strictly between seat 1 and seat 99, the rest of the boarding is the same puzzle on a smaller plane with the same second-to-last passenger. | route 004 | VALID |
| 11 | The chance for the second-to-last passenger is the same on every plane size, matching the three-seat plane where only the middle seat pick harms them. | route 004 | VALID |
| 12 | First picks of seats 1, 99 and 100 are two-thirds safe in ratio, and the reduced cases are also two-thirds safe, so the blend stays two-thirds. | route 004 | VALID |
