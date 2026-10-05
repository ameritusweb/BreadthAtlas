---
id: 004
question: cube-two-colours
title: Pin a mixed pair, count the belt, add uniform-pair cubes
strategy: new: pin-a-pair-and-count-the-belt
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 4
referee: opus/v1
criterion: v1
verdict: VALID
reason: The route is sound and gives 10. Its new landmark is the first one: pinning a *mixed* opposite pair black-up and white-down leaves only spins about the vertical axis, so the cubes with a mixed pair reduce to the six belt patterns. Route 003 pinned a both-black pair, which splits the cubes differently, and no earlier chain passed through this claim. The other landmarks overlap route 003's landmark 8 (six belt patterns) and route 002's landmark 6 (the zero-mixed class has four cubes), but one new landmark is enough.
typed_1: reduction | cubes with a mixed opposite pair | four-face belt up to spinning | reduces-to | - | Cubes with a mixed opposite pair can be turned so that the black face is on top and the white face is on the bottom, leaving a four-face belt to colour up to spinning.
typed_2: size | four-face belt patterns | cube count | = | six cubes | That belt has six patterns up to spinning, and they give six different cubes, because their black counts and band-or-corner shapes differ.
typed_3: size | cubes with no mixed opposite pair | both-black pair count | = | four cubes | Cubes with no mixed opposite pair number four, set by how many opposite pairs are both black.
---

CHAIN by duelist B
1. 🧊 (root) — A cube has six square faces, and each face is painted black or white.
2. 🔄 (root) — Two painted cubes count as the same if some rotation of one makes it look exactly like the other.
3. ❓ (← 1, 2) — How many different painted cubes are there, counting rotated copies as the same?
4. ↔️ (← 1) — The six faces form three pairs of opposite faces, one pair for each axis.
5. 🎭 (← 4) — Each opposite pair is both black, both white, or mixed (one black, one white). Rotation carries opposite pairs to opposite pairs and keeps their kind.
6. 🪢 (← 2, 5) — Split all cubes into those with at least one mixed pair and those with none. Rotation cannot move a cube from one set to the other, so the two sets are separate.
7. ⬆️ (← 2, 6) — In the first set, rotate a mixed pair so that its black face is on top and its white face is on the bottom. What remains is the belt of four side faces, coloured up to spinning about the vertical axis.
8. 📿 (← 7) — A belt of four faces, up to spinning, has none, one, two side by side, two opposite, three, or four black faces. That is six patterns.
9. 🧮 (← 5, 7, 8) — The six patterns give cubes with 1, 2, 3, 3, 4 and 5 black faces. The two 3-black cubes differ because one has an opposite black pair (the band) and the other does not (the corner). So all six cubes are different, and every cube with a mixed pair is one of them, so this set has six cubes.
10. ⚪ (← 5, 6) — In the second set every pair is both black or both white. Rotations can swap the three axes freely, so only the number of both-black pairs matters.
11. 4️⃣ (← 10) — That number can be 0, 1, 2 or 3, and each value is a different cube. So the second set has four cubes.
12. 👀 (← 9, 11) — Self-check: the all-black and all-white cubes land in the second set, and the cube with opposite white faces and four black faces also lands there. None of them has a mixed pair, so none is counted in the first set.
13. 🔟 (← 9, 11, 12) — The first set has six cubes and the second has four, so there are ten in total.

LANDMARKS:
- Cubes with a mixed opposite pair can be turned so that the black face is on top and the white face is on the bottom, leaving a four-face belt to colour up to spinning.
- That belt has six patterns up to spinning, and they give six different cubes, because their black counts and band-or-corner shapes differ.
- Cubes with no mixed opposite pair number four, set by how many opposite pairs are both black.
ANSWER: 10
