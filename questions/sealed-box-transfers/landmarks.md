# Frontier — landmarks used so far (sealed-box-transfers)

No played chains yet. Only VALID chains bind the frontier.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | A move only relocates a counter, so the set of counters in the collection never changes (a conservation invariant). | route 001 | VALID |
| 2 | Since at least one counter exists at the start, one still exists after any moves, and it must sit in some box. | route 001 | VALID |
| 3 | "All boxes empty" would need no counter to exist anywhere in the collection, which contradicts the previous point. | route 001 | VALID |
| 4 | Every move leaves its destination box nonempty, so it cannot end in an empty state. | route 002 | VALID |
| 5 | Case split: no moves (the start is nonempty) versus at least one move (the last move's destination is nonempty). | route 002 | VALID |
| 6 | Every move is reversible, so states connected by moves form mutually reachable clusters. | route 003 | VALID |
| 7 | The all-empty state is a dead end with no possible move out of it, so by reversibility it is isolated from every other state. | route 003 | VALID |
| 8 | The start has a counter, so it lies outside that isolated all-empty state and cannot reach it. | route 003 | VALID |
