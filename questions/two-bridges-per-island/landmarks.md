# Frontier — landmarks used so far (two-bridges-per-island)

No played chains yet. Only VALID chains bind the frontier.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | Having at least two bridges at every island is a local condition, and it can be met by cycles that are joined only by a single link. | route 001 | VALID |
| 2 | Two triangles joined by one bridge give a connected simple network with every island having at least two bridges. | route 001 | VALID |
| 3 | That single linking bridge is a cut bridge, and closing it splits the network into two triangles. | route 001 | VALID |
| 4 | A connector island with exactly two bridges, one into each of two separate squares, satisfies the at-least-two condition while each of its bridges is the sole link to one side. | route 002 | VALID |
| 5 | Closing either bridge at the connector island leaves a whole square cut off. | route 002 | VALID |
| 6 | Each square is internally robust, but nothing makes the connector's bridges lie on a cycle. | route 002 | VALID |
| 7 | Squeezing each internally robust cluster to a single point turns the network into a skeleton of clusters. The at-least-two condition says nothing about that skeleton, which can be a tree. | route 003 | VALID |
| 8 | A tree skeleton with at least two clusters has every link as a sole connection, so each such link is a bridge whose closure disconnects the network. | route 003 | VALID |
| 9 | The counterexample is a chain of three triangles joined in a row by two linking bridges. Both linking bridges are cut bridges. | route 003 | VALID |
