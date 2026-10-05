# Frontier — landmarks used so far (monty-four-doors)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | Your original pick holds the car one time in four, so the other three doors together hold it three times in four. | route 001 | VALID |
| 2 | The host's goat reveal does not change the group's chance; it concentrates it on the two closed doors. | route 001 | VALID |
| 3 | The two remaining closed doors are symmetric and split the group's chance equally, so each gets three in eight. | route 001 | VALID |
| 4 | If your first pick is right, which happens one time in four, every switch loses. | attempt 001 | DUPLICATE |
| 5 | If your first pick is wrong, the car must be behind one of the two closed doors, because the host never opens it. | attempt 001 | DUPLICATE |
| 6 | In the wrong-pick case a blind switch to one of the two closed doors finds the car half the time, so the win share is half of three quarters. | attempt 001 | DUPLICATE |
| 7 | The host's particular opening is likelier when the car sits behind a closed door, where he had two goats to choose from, than behind your door, where he had three. | route 002 | VALID |
| 8 | Weighing equal starting chances by those likelihoods makes the worlds stand as three parts for each closed door and two parts for your door. | route 002 | VALID |
| 9 | The surviving worlds total eight parts, so a given closed door holds three eighths. | route 002 | VALID |
| 10 | Your door keeps its one-in-four chance because the host's reveal was guaranteed whatever it hides, so the reveal says nothing about your door. | attempt 002 | DUPLICATE |
| 11 | The opened door's lost quarter is handed over to the two closed doors, which split it equally. | attempt 002 | DUPLICATE |
| 12 | Each closed door ends with its own quarter plus half of the opened door's former quarter, which is three eighths. | attempt 002 | DUPLICATE |
