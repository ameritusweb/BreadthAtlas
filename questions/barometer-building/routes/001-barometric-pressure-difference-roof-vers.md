---
id: 001
question: barometer-building
title: Barometric pressure difference, roof versus ground, converted to height
strategy: new: pressure-altimetry
contributor: sonnet (blind player 2)
date: 2026-10-05
depth: 1
referee: opus/v2
criterion: v2
verdict: VALID
reason: No binding chains exist yet, so all three landmarks are new: the roof reading is lower than the ground reading; over a building-sized climb the pressure drop is roughly proportional to height; and a known rate of pressure fall per unit height turns the drop into a height. Every step follows from the parents it names, the physics is correct (near the ground the fall is roughly 1 hPa per 8 m and close to linear), and nothing is simulated.
typed_1: state | roof pressure | ground pressure | ≪ | - | Air pressure is lower at the roof than at the ground, so the barometer reads less there.
typed_2: rate | pressure drop | building height | ≈ | - | Over a building-sized climb, the pressure drop is roughly proportional to the height climbed.
typed_3: reduction | building height | pressure drop | reduces-to | pressure per height | A known pressure-per-height rate converts the measured drop into a height.
---

CHAIN by blind player 2
1. 🌡️ (root) — The barometer is a pressure gauge that reads the local air pressure.
2. 🏢 (root) — The building is tall, and both its ground level and its roof can be reached.
3. ❓ (← 1, 2) — Asked: describe a method, and the principle it relies on, that uses the barometer to find the building's height. The barometer must play a role in the method.
4. 🌬️ (root) — Air pressure falls with height, because less air lies above you the higher you go.
5. ⬇️ (← 1, 2, 3) — Read the barometer at ground level.
6. ⬆️ (← 1, 2, 3) — Carry the barometer up to the roof and read it again.
7. 📉 (← 4, 5, 6) — The roof reading comes out lower than the ground reading, as the principle predicts.
8. ⚖️ (← 7) — The difference between the two readings is the pressure drop over the building. Compared with the whole atmospheric pressure, this drop is small.
9. 🪜 (← 4, 8) — Over so small a climb, equal steps of height give nearly equal pressure drops. So the drop is proportional to the height climbed.
10. 🧭 (← 9) — Standard-atmosphere tables give the known rate of pressure fall per unit of height near the ground.
11. 🏁 (← 8, 9, 10) — The measured drop, converted at that known rate, gives the building's height.

LANDMARKS:
- Air pressure is lower at the roof than at the ground, so the barometer reads less there.
- Over a building-sized climb, the pressure drop is roughly proportional to the height climbed.
- A known pressure-per-height rate converts the measured drop into a height.

ANSWER: Read the barometer at the ground and again at the roof. The pressure drop, converted at the known rate at which pressure falls with height, gives the building's height. The principle is that pressure falls with height.
