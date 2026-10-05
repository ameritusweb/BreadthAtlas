# Frontier — landmarks used so far (monty-five-doors)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | The host's reveal leaves my door's chance unchanged, while the group of the other four doors keeps four times its chance. | route 001 | VALID |
| 2 | The opened goat door's chance moves entirely onto the three remaining closed doors. | route 001 | VALID |
| 3 | By symmetry the three closed doors split the other-group's chance equally. | route 001 | VALID |
| 4 | A single switch target gets a third of four fifths, which sits between staying and taking all the other doors. | route 001 | VALID |
| 5 | Switching can only win if my first pick was wrong, and a right first pick makes every switch lose. | route 002 | VALID |
| 6 | Given a wrong first pick, the car is certainly among the three closed doors, because the host never reveals it. | route 002 | VALID |
| 7 | Within that case a random closed door hits the car one time in three, so the answer is that fraction of the wrong-pick case's chance. | route 002 | VALID |
| 8 | All door chances must add up to certainty: my door keeps one fifth and the opened door has none, so the three closed doors hold the remaining four fifths. | attempt 001 | DUPLICATE |
| 9 | That leftover is divided equally among the three closed doors by symmetry, so one switch target gets a third of it. | attempt 001 | DUPLICATE |
| 10 | The host's particular opening is less likely when the car is behind my door, since he had four options, than when it is behind a given closed door, where he had three. | route 003 | VALID |
| 11 | Each closed door therefore outweighs my door in the ratio four to three, and the opened door has no weight. | route 003 | VALID |
| 12 | The weights split into equal parts, three for my door and four for each closed door, so one switch target holds four of the fifteen parts. | route 003 | VALID |
