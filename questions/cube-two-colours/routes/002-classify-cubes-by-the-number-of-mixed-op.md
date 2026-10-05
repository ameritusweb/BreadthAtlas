---
id: 002
question: cube-two-colours
title: Classify cubes by the number of mixed opposite-face pairs
strategy: new: opposite-pair-decomposition
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 2
referee: opus/v1
criterion: v1
verdict: VALID
reason: All the steps are sound and give 10. Route 001 sorted cubes by black-face count. This chain sorts them by a different rotation-invariant, so its two later landmarks are new: "the number of mixed opposite pairs (0 to 3) splits the cubes into four classes" and "the classes contain four, three, two and one cubes."
typed_1: structure | opposite pair | both-black, both-white or mixed | ∈ | - | A cube has three pairs of opposite faces, and each pair is both black, both white, or mixed.
typed_2: symmetry | mixed-pair count | rotation | invariant | - | The number of mixed opposite pairs (0 to 3) is unchanged by rotation, so it splits the cubes into four classes.
typed_3: size | mixed-pair classes | cube count | = | four, three, two and one cubes | The classes contain four, three, two and one cubes respectively.
---

CHAIN by duelist B
1. 🧊 (root) — A cube has six square faces, and each face is painted black or white.
2. 🔄 (root) — Two painted cubes count as the same if some rotation of one makes it look exactly like the other.
3. ❓ (← 1, 2) — How many different painted cubes are there, counting rotated copies as the same?
4. ↔️ (← 1) — The six faces split into three pairs of opposite faces, one pair for each axis through the cube.
5. 🎭 (← 4) — Each opposite pair is of one of three kinds: both black, both white, or mixed (one black, one white).
6. 🔢 (← 2, 5) — A rotation carries opposite pairs to opposite pairs and keeps their kinds. So the number of mixed pairs (0, 1, 2 or 3) is unchanged, and cubes with different counts are different.
7. 0️⃣ (← 5, 6) — With no mixed pair, every pair is both black or both white. Rotations can swap the axes freely, so only the number of both-black pairs matters. That number can be 0, 1, 2 or 3, which gives four cubes.
8. 1️⃣ (← 5, 6) — With one mixed pair, the other two pairs can be both white, both black, or one of each. A half-turn about a perpendicular axis swaps the two faces of the mixed pair and keeps the other pairs in place. So the mixed pair's orientation does not matter, and this gives three cubes.
9. 2️⃣ (← 5, 6) — With two mixed pairs, the two black faces from them are adjacent, and any such adjacent arrangement can be rotated onto any other. The third pair is then both black or both white, which gives two cubes.
10. 3️⃣ (← 5, 6) — With three mixed pairs, there is one black face on each axis, so no two black faces are opposite and all three meet at a corner. Rotations carry any corner to any other, so this gives one cube.
11. 🔟 (← 7, 8, 9, 10) — The four cases are exhaustive and mutually different. They contribute four, three, two and one cubes, which total ten.

LANDMARKS:
- A cube has three pairs of opposite faces, and each pair is both black, both white, or mixed.
- The number of mixed opposite pairs (0 to 3) is unchanged by rotation, so it splits the cubes into four classes.
- The classes contain four, three, two and one cubes respectively.
ANSWER: 10
