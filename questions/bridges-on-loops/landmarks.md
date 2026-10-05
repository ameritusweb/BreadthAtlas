# Frontier — landmarks used so far (bridges-on-loops)

No played chains yet. Only VALID chains bind the frontier.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | Each loop through the closed bridge gives a detour path between its two endpoints. | route 001 | VALID |
| 2 | Any route using the closed bridge can be rerouted along that detour. | route 001 | VALID |
| 3 | A bridge that lies on a loop is never a cut bridge, so connectivity survives its removal. | route 001 | VALID |
| 4 | Removing one bridge can leave at most two pieces, with the bridge's two ends in different pieces. | route 002 | VALID |
| 5 | If the network split, the closed bridge would be the only link between the two pieces. | route 002 | VALID |
| 6 | A closed loop must cross between two pieces an even number of times, but this loop would cross exactly once, which is a parity contradiction. | route 002 | VALID |
| 7 | The network has a spanning tree, so if the closed bridge is outside it, everything stays connected through the tree. | route 003 | VALID |
| 8 | If the closed bridge is in the tree, its removal splits the tree into two parts, and the loop through the bridge must cross between them again by a different open bridge. | route 003 | VALID |
| 9 | That second crossing bridge reconnects the two tree parts, so connectivity survives either way. | route 003 | VALID |
