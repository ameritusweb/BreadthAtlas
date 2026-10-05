# Frontier — landmarks used so far (birthday-months)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | There are only twelve possible birth months, and twenty-three people exceed that. | route 001 | VALID |
| 2 | Assuming all months are different would use up the twelve months by the twelfth person (pigeonhole), leaving the thirteenth with no new month. | route 001 | VALID |
| 3 | A shared month occurs in every possible arrangement, so the event is certain, with no need to weigh likelihoods. | route 001 | VALID |
| 4 | For everyone to have different months, each new arrival must avoid all earlier months, and that chance shrinks as the free months get used up. | route 002 | VALID |
| 5 | After twelve people, no free month remains, so the chance the thirteenth avoids a match is nothing. | route 002 | VALID |
| 6 | The probability that all twenty-three months differ is zero, so its complement, a shared month, has probability one. | route 002 | VALID |
| 7 | Spread evenly over twelve months, twenty-three people average nearly two per month, which is more than one. | route 003 | VALID |
| 8 | The fullest month holds at least the average, and since headcounts are whole numbers, at least two people. | route 003 | VALID |
| 9 | This holds for every possible set of birth months, so a shared month is certain. | route 003 | VALID |
| 10 | Choosing one representative for each month that appears gives at most twelve representatives, so with twenty-three people some are not representatives. | attempt 001 | DUPLICATE |
| 11 | Every non-representative was born in a month that already has a representative, a different person, so the two of them share a month. | attempt 001 | DUPLICATE |
| 12 | This works for any set of birth months, so a shared month is certain. | attempt 001 | DUPLICATE |
