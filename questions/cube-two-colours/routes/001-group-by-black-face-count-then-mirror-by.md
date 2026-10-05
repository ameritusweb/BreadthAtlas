---
id: 001
question: cube-two-colours
title: Group by black-face count, then mirror by colour swap
strategy: new: invariant-partition
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 1
referee: opus/v1
criterion: v1
verdict: VALID
reason: Every step is correct and the total of 10 is exact. Since no route has been played yet, all three landmarks are new: rotation preserves the black-face count; two black faces are adjacent or opposite and three are a corner or a band; and swapping the colours mirrors the counts of 4, 5 and 6 black faces onto 2, 1 and 0.
typed_1: symmetry | black-face count | rotation | invariant | - | Rotation never changes the number of black faces, so cubes can be sorted into groups by black-face count.
typed_2: structure | two-black and three-black cubes | adjacent/opposite and corner/band | ∈ | two cubes each | Two black faces form either an adjacent pair or an opposite pair, and three black faces form either a corner or a band, giving two cubes each.
typed_3: symmetry | four-, five- and six-black groups | two-, one- and zero-black groups | bijects | colour swap | Swapping the two colours mirrors the groups with four, five and six black faces onto those with two, one and zero.
---

CHAIN by duelist A
1. 🧊 (root) — A cube has six square faces, and each face is painted black or white.
2. 🔄 (root) — Two painted cubes count as the same if some rotation of one makes it look exactly like the other.
3. ❓ (← 1, 2) — How many different painted cubes are there, counting rotated copies as the same?
4. ⚫ (← 1, 3) — Sort cubes by how many faces are black. A rotation never changes that count, so cubes in different groups are always different.
5. ⚪ (← 4) — With no black faces, the cube is all white, so there is one cube.
6. 1️⃣ (← 4) — With exactly one black face, any face can be rotated to the top, so there is one cube.
7. 2️⃣ (← 4) — With two black faces, they either share an edge or sit opposite each other. Rotation preserves which case holds and can turn any pair of the same kind into any other, so there are two cubes.
8. 3️⃣ (← 4) — With three black faces, either two of them are opposite, forming a band of three in a row, or none are opposite, so all three meet at one corner. Each case is a single cube up to rotation, so there are two cubes.
9. 🔁 (← 4) — Swapping black and white on every face respects rotation. It pairs the four-black group with the two-black group, the five-black group with the one-black group, and the six-black group with the zero-black group.
10. 👀 (← 8, 9) — Self-check: the three-black group maps to itself under the swap. A corner cube turns into a corner cube, and a band cube into a band cube, so that group is not double counted.
11. 🔟 (← 5, 6, 7, 8, 9) — Add up the groups: zero, one, two and three black faces give one, one, two and two cubes. The mirrored groups with four, five and six black faces give two, one and one. Altogether there are ten.

LANDMARKS:
- Rotation never changes the number of black faces, so cubes can be sorted into groups by black-face count.
- Two black faces form either an adjacent pair or an opposite pair, and three black faces form either a corner or a band, giving two cubes each.
- Swapping the two colours mirrors the groups with four, five and six black faces onto those with two, one and zero.
ANSWER: 10
