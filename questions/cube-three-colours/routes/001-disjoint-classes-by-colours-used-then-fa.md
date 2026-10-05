---
id: 001
question: cube-three-colours
title: Disjoint classes by colours used, then face-count patterns
strategy: new: case-split-by-colour-multiset
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 1
referee: opus/v2
criterion: v2
verdict: VALID
reason: The steps are correct and give the exact answer 57: 3 one-colour cubes, 8 per pair for two colours, and 30 for three colours from patterns 4-1-1, 3-2-1 and 2-2-2 giving 6, 18 and 6. The case additions are counting by cases, not simulation, and with an empty frontier all three landmarks are new: the disjoint split by colours used, the face-count pattern split, and the three-colour total of thirty.
typed_1: reduction | painted cubes | colours used | reduces-to | - | Cubes sort into disjoint classes by how many colours they use: three use one colour and eight per pair use exactly two.
typed_2: structure | three-colour cubes | face-count patterns 4-1-1, 3-2-1 and 2-2-2 | ∈ | - | Cubes using all three colours split into the face-count patterns 4-1-1, 3-2-1 and 2-2-2, giving six, eighteen and six cubes.
typed_3: size | three-colour cubes | - | = | cubes | Cubes using all three colours total thirty.
---

CHAIN by duelist A
1. 🧊 (root) — A cube has six faces, and rotations of the cube are the only moves allowed for matching two cubes.
2. 🎨 (root) — Each face gets one of three colours, and every colour may be used on any number of faces, including none.
3. ❓ (← 1, 2) — How many painted cubes are there if cubes that differ only by a rotation count as the same?
4. 🗂️ (← 3) — Sort every cube by how many of the three colours it actually uses (one, two or three). Rotation never changes that, so the classes don't overlap and the class counts can be added.
5. 1️⃣ (← 4) — Using one colour gives a plain cube, so there are exactly three such cubes, one per colour.
6. 🔢 (← 1, 4) — For a fixed pair of colours, split by how many faces have the first colour. One face or five faces gives one shape each, and two, three or four faces give two shapes each, the pair of faces being adjacent or opposite and the three faces being a corner or a strip. This gives eight cubes that use both colours.
7. 2️⃣ (← 4, 6) — There are three possible pairs of colours, and each pair gives its own eight cubes. Together these are the exactly-two-colour cubes.
8. 3️⃣ (← 4) — For cubes using all three colours, split by how the six faces divide among the colours. The only possible patterns are 4-1-1, 3-2-1 and 2-2-2.
9. 🅰️ (← 1, 8) — For 4-1-1, choose which colour has four faces, then place the two single faces. They are either adjacent or opposite, so there are six cubes.
10. 🅱️ (← 1, 8) — For 3-2-1, the three-face set is a corner or a strip. After that the two-face and one-face split of the other three faces has one option for a corner and two for a strip. That is three shapes per assignment of colours to sizes, and six assignments, so eighteen cubes.
11. 🆎 (← 1, 8) — For 2-2-2, the pairs are all opposite (one cube), one opposite and two adjacent (three cubes, one per colour that is opposite), or all adjacent (two cubes, mirror images). That makes six cubes.
12. 🧮 (← 9, 10, 11) — Adding the three patterns, thirty cubes use all three colours.
13. 🧩 (← 5, 7, 12) — Adding the one-colour, two-colour and three-colour classes gives fifty-seven cubes.
14. 👀 (← 13) — Self-check: with two colours the same method gives ten cubes, which matches the known count, so the method is sound.

LANDMARKS:
- Cubes sort into disjoint classes by how many colours they use: three use one colour and eight per pair use exactly two.
- Cubes using all three colours split into the face-count patterns 4-1-1, 3-2-1 and 2-2-2, giving six, eighteen and six cubes.
- Cubes using all three colours total thirty.
ANSWER: 57
