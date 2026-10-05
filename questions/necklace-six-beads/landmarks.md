# Frontier — landmarks used so far (necklace-six-beads)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | The number of black beads is unchanged by turning and flipping, so it splits the necklaces into separate groups. | route 001 | VALID |
| 2 | Swapping colours pairs the groups: four black with two, five with one, six with none. | route 001 | VALID |
| 3 | Two black beads give three necklaces, by the gap between them. Three black beads give three, by how the whites fall in the gaps. | route 001 | VALID |
| 4 | Necklaces are sorted by the number of one-colour runs around the ring, which turning and flipping preserve, rather than by the number of black beads. | route 002 | VALID |
| 5 | One black run gives five necklaces, set by the run length. Two black runs give five, by where two spare beads go among four alternating runs. | route 002 | VALID |
| 6 | Three black runs force perfect alternation, giving one necklace, and the single-colour rings give two. | route 002 | VALID |
| 7 | Rings are split by whether they are periodic, meaning a shorter block of one, two or three beads repeats, rather than by black count or runs. | route 003 | VALID |
| 8 | The periodic rings are the two single-colour rings, the alternating ring, and two three-bead-block rings, giving five. | route 003 | VALID |
| 9 | The aperiodic rings number eight, found by excluding the periodic cases from each count of black beads. | route 003 | VALID |
| 10 | Count rings up to turning alone first, giving fourteen classes, then let flipping merge classes afterwards. | route 004 | VALID |
| 11 | Every ring except one pair is its own mirror image, so flipping merges only a single pair of turning classes. | route 004 | VALID |
| 12 | That one handed pair is the two three-black rings with a touching pair and a separate bead, which are mirror images but not turnings of each other. | route 004 | VALID |
