# Frontier — landmarks used so far (barometer-building)

Rows marked VALID bind the frontier; the rest record what was tried and how it failed.

| # | landmark | chain | verdict |
|---|---|---|---|
| 1 | Air pressure decreases with height, so the barometer reads lower on the roof than at the ground. | attempt 001 | ILL-FORMED |
| 2 | The difference between the ground and roof pressure readings, converted by the known rate of pressure fall with altitude, gives the height. | attempt 001 | ILL-FORMED |
| 3 | Both readings are taken with the same barometer in quick succession, so weather changes and instrument error do not distort the difference. | attempt 001 | ILL-FORMED |
| 4 | Air pressure is lower at the roof than at the ground, so the barometer reads less there. | route 001 | VALID |
| 5 | Over a building-sized climb, the pressure drop is roughly proportional to the height climbed. | route 001 | VALID |
| 6 | A known pressure-per-height rate converts the measured drop into a height. | route 001 | VALID |
| 7 | A heavy barometer dropped from the roof falls almost freely, because air drag is small for a dense compact object over a building's height. | route 002 | VALID |
| 8 | The fall time from rest fixes the height, which grows as the square of the time, so a longer drop means a taller building. | route 002 | VALID |
| 9 | Timing the drop from release to impact, together with the known strength of gravity, gives the roof height. | route 002 | VALID |
