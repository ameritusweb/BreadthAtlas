---
id: 001
question: tetrahedron-three-colours
title: Split by colour-count pattern, count orbits per pattern
strategy: new: case-split-by-invariant-pattern
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 1
referee: opus/v2
criterion: v2
verdict: VALID
reason: Every step holds, and the count of 15 matches the reference. Step 10 is right: the twelve rotations act freely on the twelve labelled two-one-one placements, and the half-turn through the doubled pair's shared edge swaps both pairs. The frontier is empty, so all three landmarks are new: rotation group = even face permutations preserving colour counts; split by colour pattern into 3/6/3/3; and the half-turn merging the two-one-one singletons.
typed_1: symmetry | rotation group | count of faces per colour | invariant | - | The rotation group is the even permutations of the four faces, so rotation preserves each colour's face count.
typed_2: reduction | painted tetrahedra | colour-count patterns | reduces-to | - | Sorting paintings by colour-count pattern gives 3 (all one colour), 6 (three and one), 3 (two and two) and 3 (two, one, one), with no all-different pattern.
typed_3: symmetry | rotation group | two, one, one paintings | exists | - | In the two, one, one pattern, a rotation can swap the two single faces while swapping the doubled pair, so there is only one picture per doubled colour.
---

CHAIN by duelist A
1. 🔺 (root) — A regular tetrahedron has four faces.
2. 🎨 (root) — Each face gets one of three colours, and two paintings are the same if a rotation, with no reflection, turns one into the other.
3. ❓ (← 1, 2) — How many different painted tetrahedra are there up to rotation?
4. 🔄 (← 1) — Any rotation of the tetrahedron permutes the faces, and every even permutation of the four faces is realised by a rotation. The rotation group is therefore the even permutations, which has twelve elements.
5. 🧮 (← 3, 4) — Instead of averaging, sort the paintings by how many faces each colour gets. Rotations never change those counts, so each pattern can be counted on its own.
6. 🟦 (← 2, 5) — Pattern "all four faces one colour": there is one painting per colour, so three in total.
7. 🧩 (← 4, 5) — Pattern "three faces one colour, one face another": the lone face can be rotated to any position, so one picture per ordered pair of colours. That gives six.
8. ⚖️ (← 4, 5) — Pattern "two faces and two faces": the two colours form a pair, and the two faces of one colour sit on an edge. All such placements are equivalent under rotation, so there is one picture per pair of colours, three in total.
9. 🔀 (← 4, 5) — Pattern "two, one, one": the doubled colour can be chosen in three ways, and the other two colours are then forced.
10. 🧷 (← 4, 9) — The labelled placements of this pattern fall into a single orbit, because the twelve rotations act without fixed points on them. Swapping the two single faces can be done by a rotation that also swaps the doubled pair, so there is one picture per doubled colour, three in total.
11. 🚫 (← 2, 5) — The pattern "all four different" cannot occur, because only three colours exist, so nothing is added for it.
12. ➕ (← 6, 7, 8, 10, 11) — Adding the pattern totals gives all the distinct paintings.
13. 👀 (← 12) — Self-check: the pattern sizes of 1, 4, 6 and 12 labelled paintings per pattern are consistent with orbits of at most twelve, and the total is a plausible fraction of the eighty-one labelled paintings.

LANDMARKS:
- The rotation group is the even permutations of the four faces, so rotation preserves each colour's face count.
- Sorting paintings by colour-count pattern gives 3 (all one colour), 6 (three and one), 3 (two and two) and 3 (two, one, one), with no all-different pattern.
- In the two, one, one pattern, a rotation can swap the two single faces while swapping the doubled pair, so there is only one picture per doubled colour.
ANSWER: 15
