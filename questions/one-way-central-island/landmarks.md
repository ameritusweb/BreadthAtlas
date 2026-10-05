# Frontier — landmarks used so far (one-way-central-island)

No played chains yet. Only VALID chains bind the frontier.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | Reaching the hub is one-directional information: it says nothing about leaving the hub. | route 001 | VALID |
| 2 | A hub with no outgoing bridges (a sink) satisfies the givens while being unable to reach anyone else. | route 001 | VALID |
| 3 | The two-island network with a single bridge A→H is a minimal counterexample. | route 001 | VALID |
| 4 | Islands split into clusters of mutual reachability, and the bridges between clusters never form a loop. | route 002 | VALID |
| 5 | If everyone reaches H, H's cluster is the dead end of the cluster picture, with no bridge leaving it. | route 002 | VALID |
| 6 | The guarantee holds exactly when H's cluster is the whole network. A three-island inward star (A→H, B→H) fails this and also leaves A and B unable to reach each other. | route 002 | VALID |
| 7 | Reachability is transitive, so a one-way line A→B→H lets everyone reach H while the order of the line can never be reversed. | route 003 | VALID |
| 8 | The start of the line is a source with no incoming bridge, so no other island can reach it. This is a second obstruction besides H having no exit. | route 003 | VALID |
| 9 | The hub condition constrains only the routes into H. It places no demand on incoming bridges for the other islands. | route 003 | VALID |
