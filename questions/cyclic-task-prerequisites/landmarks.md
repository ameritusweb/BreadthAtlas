# Frontier — landmarks used so far (cyclic-task-prerequisites)

No played chains yet. Only VALID chains bind the frontier.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | Any schedule has a first task to start, and it would need an earlier-finished task. | route 001 | VALID |
| 2 | Finishing requires starting first, so a finished prerequisite must have started even earlier, contradicting the first start. | route 001 | VALID |
| 3 | A cycle of strict prerequisites has no entry point, so nothing can begin. | route 001 | VALID |
| 4 | Each task's finish is strictly later than its prerequisite's finish, because the prerequisite ends before the task starts and the task has positive duration. | route 002 | VALID |
| 5 | Among the three finish moments, the earliest finisher would need a prerequisite that finished even earlier. | route 002 | VALID |
| 6 | Going around the loop, the strictly-earlier finishes would circle back to a finish earlier than itself. | route 002 | VALID |
| 7 | Composing the prerequisites around the loop collapses them into one task that must finish before it can start. | attempt 001 | DUPLICATE |
| 8 | A task's start would have to come after its own finish, while positive duration puts its finish after its start. | attempt 001 | DUPLICATE |
