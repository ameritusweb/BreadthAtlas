---
id: 001
question: barometer-building
title: (form failure)
strategy: unclassified
contributor: sonnet (blind player 1)
date: 2026-10-05
referee: code/v2
criterion: v2
verdict: ILL-FORMED
reason: steps [10] do no work (nothing later follows from them)
---

CHAIN by blind player 1
1. 🌡️ (root) — Given: the barometer is a pressure gauge, a heavy object, a thing of known length, and a thing of value.
2. 🏢 (root) — Given: the building is tall, with a reachable roof, a shadow, stairs, and a superintendent.
3. ❓ (← 1, 2) — Asked: describe a method, and the principle it relies on, for finding the building's height, with the barometer playing a role in the method.
4. 🌬️ (root) — General knowledge: air pressure falls steadily as one goes higher, because less air lies above.
5. 🌡️ (← 1) — Take the barometer to the foot of the building and read the pressure there, using it as the pressure gauge it is.
6. 🛗 (← 2) — Go up to the roof by the stairs, carrying the barometer, so the same instrument can be read at the top.
7. 🌡️ (← 5, 6) — Read the pressure again on the roof with the same barometer, so any instrument error is the same at both readings.
8. ⚖️ (← 5, 7) — Compare the two readings: the roof reading is lower than the ground reading, and the gap between them reflects the height climbed.
9. 🌬️ (← 4, 8) — Because pressure falls steadily with height near the ground, a bigger gap means a taller building, and the gap converts to height using the known rate of fall of pressure with altitude.
10. 🏢 (← 9) — The converted gap gives the building's height; a tall building gives a clearly measurable gap, while a short one would give a gap too small to read well.
11. 👀 (← 4, 8) — Self-check: the method needs the pressure to be steady between the two readings and the instrument to be sensitive enough, so read both quickly, one soon after the other, on a calm day.

LANDMARKS:
- Air pressure decreases with height, so the barometer reads lower on the roof than at the ground.
- The difference between the ground and roof pressure readings, converted by the known rate of pressure fall with altitude, gives the height.
- Both readings are taken with the same barometer in quick succession, so weather changes and instrument error do not distort the difference.

ANSWER: Read the barometer at the foot of the building and again on the roof; the pressure difference, converted using the known rate at which air pressure falls with height, gives the building's height.
