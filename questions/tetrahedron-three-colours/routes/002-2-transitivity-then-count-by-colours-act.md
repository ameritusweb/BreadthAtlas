---
id: 002
question: tetrahedron-three-colours
title: 2-transitivity, then count by colours actually used
strategy: new: transitivity-collapse-by-colours-used
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 2
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is sound. The even permutations of four faces form a 2-transitive group, so it gives 3 + 9 + 3 = 15 with no snapshots or arithmetic. Two of its landmarks are new against route 001: the rotations are 2-transitive on faces, and a two-colour painting is fixed by its colour counts. Its decomposition by the set of colours used, rather than by colour-count pattern, is also new.
typed_1: symmetry | rotation group | sets of faces of a given size | invariant | - | The rotation group is 2-transitive on the faces, so any set of faces of a given size can be moved to any other such set.
typed_2: reduction | two-colour paintings | count of faces per colour | bijects | - | With two colours, a painting is determined by how many faces get each colour.
typed_3: reduction | painted tetrahedra | set of colours used | reduces-to | - | Sorting by the set of colours used gives one colour, exactly two colours, and all three colours, each counted separately.
---

CHAIN by duelist B
1. 🔺 (root) — A regular tetrahedron has four faces.
2. 🎨 (root) — Each face is painted one of three colours, and two paintings are the same if a rotation (no reflection) turns one into the other.
3. ❓ (← 1, 2) — How many different painted tetrahedra are there up to rotation?
4. 🔄 (← 1) — Rotations permute the four faces, and the rotations realise exactly the even permutations of the faces.
5. 🤝 (← 4) — The even permutations can carry any pair of faces to any other pair, and any trio to any other trio, so the rotations are 2-transitive on faces.
6. 🧱 (← 5) — With two colours, choose which faces get the first colour. Any chosen set of a given size is equivalent to any other of that size, so a two-colour painting is fixed by how many faces get each colour.
7. 🎯 (← 2, 6) — For one chosen pair of colours, this gives one picture for each count of the first colour from none to all four, including the two single-colour paintings.
8. 🗂️ (← 2, 7) — Sort every painting by the set of colours it actually uses. This gives three kinds: one colour, exactly two colours, all three colours.
9. 1️⃣ (← 7, 8) — Using one colour gives one painting per colour, which is three.
10. 2️⃣ (← 7, 8, 9) — For each pair of colours, remove the two single-colour cases from step 7. The remaining counts (one–three, two–two, three–one) give three pictures per pair, and there are three pairs of colours.
11. 3️⃣ (← 2, 5, 8) — Using all three colours forces one colour on two faces and the others on one face each. The doubled pair sits on an edge, and by 2-transitivity every such placement is equivalent, so each choice of doubled colour gives one picture.
12. ➕ (← 9, 10, 11) — The three kinds (one colour, exactly two colours, all three colours) do not overlap and together cover everything, so we add their sizes.
13. 👀 (← 12) — Self-check: the two-colour counts of five per pair, with the shared single-colour paintings counted once, agree with this total.

LANDMARKS:
- The rotation group is 2-transitive on the faces, so any set of faces of a given size can be moved to any other such set.
- With two colours, a painting is determined by how many faces get each colour.
- Sorting by the set of colours used gives one colour, exactly two colours, and all three colours, each counted separately.
ANSWER: 15
