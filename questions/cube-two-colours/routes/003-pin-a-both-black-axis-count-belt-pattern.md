---
id: 003
question: cube-two-colours
title: Pin a both-black axis, count belt patterns
strategy: new: pin-a-feature-and-reduce-symmetry
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 3
referee: opus/v1
criterion: v1
verdict: VALID
reason: All steps are sound. The six belt patterns give six distinct cubes with a both-black pair, the four cubes without one are fixed by their count of mixed pairs, and together they make 10. The landmarks "a both-black pair can be turned to the top and bottom, leaving a four-face belt to colour up to spinning" and "a belt has six patterns up to spinning, each a different cube" are new. No earlier chain split the cubes on whether they have a both-black pair.
typed_1: reduction | cubes with a both-black opposite pair | four-face belt up to spinning | reduces-to | - | Cubes with a both-black opposite pair can be turned so that pair is on top and bottom, leaving only the four-face belt to colour up to spinning.
typed_2: size | four-face belt patterns | cube count | = | six cubes | A belt of four faces has six patterns up to spinning, and each gives a different cube.
typed_3: size | cubes with no both-black opposite pair | mixed-pair count | = | four cubes | Cubes with no both-black opposite pair number four, set by whether zero, one, two or three opposite pairs are mixed.
---

CHAIN by duelist A
1. 🧊 (root) — A cube has six square faces, and each face is painted black or white.
2. 🔄 (root) — Two painted cubes count as the same if some rotation of one makes it look exactly like the other.
3. ❓ (← 1, 2) — How many different painted cubes are there, counting rotated copies as the same?
4. ↔️ (← 1) — The six faces split into three pairs of opposite faces, one pair for each axis.
5. 🎭 (← 4) — Each opposite pair is both black, both white, or mixed. Rotation carries opposite pairs to opposite pairs and keeps their kind.
6. ⬛ (← 5) — Split all cubes into two sets: those with at least one both-black opposite pair, and those with none. Rotation cannot move a cube from one set to the other.
7. 🔝 (← 2, 6) — In the first set, rotate a both-black pair to the top and bottom. The only rotations that keep it there are spins about the vertical axis, so what remains is the belt of four side faces, coloured up to spinning.
8. 📿 (← 7) — A belt of four faces, up to spinning, has black count none, one, two side by side, two opposite, three, or four. That is six patterns.
9. 🧩 (← 5, 7, 8) — These six patterns give six different cubes. Black totals separate all of them except the two-black belts, and those differ in whether the belt itself holds a both-black pair. Choosing another both-black pair as the axis gives the same pattern type, so nothing is counted twice.
10. ⚪ (← 5, 6) — In the second set every pair is white or mixed, so the number of mixed pairs (0, 1, 2 or 3) is the only thing that can vary. Zero mixed pairs is all white. One gives a single black face. Two give two adjacent black faces. Three give one black face per axis, meeting at a corner. Each case is one cube, so this set has four cubes.
11. 👀 (← 9, 10) — Self-check: the two sets are disjoint, because having a both-black pair is unchanged by rotation. Nothing is counted in both.
12. 🔟 (← 9, 10, 11) — Six cubes from the first set and four from the second make ten in total.

LANDMARKS:
- Cubes with a both-black opposite pair can be turned so that pair is on top and bottom, leaving only the four-face belt to colour up to spinning.
- A belt of four faces has six patterns up to spinning, and each gives a different cube.
- Cubes with no both-black opposite pair number four, set by whether zero, one, two or three opposite pairs are mixed.
ANSWER: 10
