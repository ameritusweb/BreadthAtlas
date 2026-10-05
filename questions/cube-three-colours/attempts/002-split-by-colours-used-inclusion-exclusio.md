---
id: 002
question: cube-three-colours
title: Split by colours used, inclusion–exclusion on pairs
strategy: new: case-split-by-colours-used
contributor: sonnet (duelist B)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: DUPLICATE
reason: This is the same route as route 001. The figure of 27 is just route 001's landmark 1 (three plain cubes plus eight two-colour cubes per pair) counted by inclusion–exclusion instead of disjoint classes. The thirty three-colour cubes in step 10 come straight from route 001's landmarks 2 and 3 (the 4-1-1 / 3-2-1 / 2-2-2 split), so the chain adds no claim about the problem that route 001 had not already passed through.
typed_1: structure | single-pair families | plain cube | ∈ | - | Cubes using only the colours of one chosen pair number ten, and two such families overlap only in one plain cube.
typed_2: size | at-most-two-colour cubes | - | = | cubes | Overlap correction: cubes using at most two of the three colours total twenty-seven.
typed_3: reduction | painted cubes | at-most-two-colour cubes and three-colour cubes | reduces-to | - | The at-most-two-colour cubes and the all-three-colour cubes are complementary, so the total is twenty-seven plus thirty.
---

CHAIN by duelist B
1. 🧊 (root) — A cube has six faces, and only rotations may be used to match two cubes.
2. 🎨 (root) — Each face gets one of three colours, and colours may repeat or go unused.
3. ❓ (← 1, 2) — How many painted cubes are there if cubes that differ only by a rotation count as the same?
4. 2️⃣ (root) — From general knowledge, with two available colours there are exactly ten distinct painted cubes, and this count includes the two plain cubes.
5. 🗂️ (← 3) — Sort each cube by the set of colours it uses. Rotation never changes that set, so each cube belongs to exactly one set-class: a single colour, a pair, or all three.
6. 🔍 (← 4, 5) — For a chosen pair of colours, the cubes that use only colours from that pair number ten. They are the cubes whose colour set is that pair or one of its two single colours.
7. 🔗 (← 6) — Two different pairs share only one colour. The only cube that uses colours from both pairs is the plain cube of that shared colour. No cube avoids all three colours.
8. 🫧 (← 6, 7) — Cubes using at most two colours form the union of three overlapping families of ten. Each plain cube lies in two families, so it was counted twice. Removing the double counts leaves a total of twenty-seven.
9. 🎯 (← 5, 8) — The cubes that remain are exactly those using all three colours, so the total is the twenty-seven cubes using at most two colours plus the all-three-colour cubes.
10. 🧩 (← 9) — Splitting the all-three-colour cubes by face-count pattern (4-1-1, 3-2-1, 2-2-2) and counting each pattern's shapes gives thirty cubes.
11. ➕ (← 8, 9, 10) — Adding the thirty all-three-colour cubes to the twenty-seven at-most-two-colour cubes gives fifty-seven.
12. 👀 (← 11) — Self-check: for two colours the same union logic gives the two plain cubes plus eight mixed ones, which is ten. This matches the premise.

LANDMARKS:
- Cubes using only the colours of one chosen pair number ten, and two such families overlap only in one plain cube.
- Overlap correction: cubes using at most two of the three colours total twenty-seven.
- The at-most-two-colour cubes and the all-three-colour cubes are complementary, so the total is twenty-seven plus thirty.
ANSWER: 57
