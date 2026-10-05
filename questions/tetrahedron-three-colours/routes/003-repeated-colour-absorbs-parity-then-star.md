---
id: 003
question: tetrahedron-three-colours
title: Repeated colour absorbs parity, then stars and bars
strategy: new: parity-absorption-reduction-to-multisets
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 3
referee: opus/v2
criterion: v2
verdict: VALID
reason: The argument is sound, with no calculation and no simulation. Every painting has a repeated colour, so its stabiliser in the full group of face rearrangements contains a transposition; that makes orbits under the even permutations the same as orbits under all rearrangements, the classes are exactly the multisets, and two dividers in six slots give 15. The new landmarks are the parity-absorption step (rotations are as good as all rearrangements because a repeated colour supplies an odd symmetry) and the stars-and-bars count of multisets; neither appears in routes 001 or 002.
typed_1: symmetry | rotation group | all rearrangements of faces | = | - | Because four faces and three colours force a repeated colour, swapping two equal faces absorbs any odd rearrangement, so rotations are as good as all rearrangements.
typed_2: reduction | painted tetrahedra | multisets of four colours from three | bijects | - | Hence a painting up to rotation is exactly a multiset of four colours from three.
typed_3: construction | multisets of four colours from three | placements of two dividers among six slots | bijects | - | Multisets are counted by placing two dividers among six slots in a row of faces.
---

CHAIN by duelist A
1. 🔺 (root) — A regular tetrahedron has four faces.
2. 🎨 (root) — Each face gets one of three colours, and two paintings are the same if a rotation, with no reflection, turns one into the other.
3. ❓ (← 1, 2) — How many different painted tetrahedra are there up to rotation?
4. 🔄 (← 1) — Rotations realise exactly the even permutations of the four faces, which is half of all the ways to rearrange the faces.
5. 🕊️ (← 1, 2) — Four faces and only three colours means by pigeonhole that some colour is used on at least two faces.
6. 🔁 (← 5) — Swapping two equally coloured faces is an odd rearrangement, yet it leaves the painting looking exactly the same.
7. 🧲 (← 4, 6) — Any odd rearrangement equals an even one followed by that swap. So rearranging faces in any way gives nothing beyond what rotations give, and two paintings with the same colours are rotation-equivalent.
8. 🧺 (← 3, 7) — A painted tetrahedron up to rotation is therefore determined by its multiset of colours, meaning how many faces get each colour.
9. 🧱 (← 4, 8) — Conversely, rotations only move faces around, so paintings with different multisets can never be equivalent. Pictures correspond exactly to multisets of four colours drawn from three.
10. 📏 (← 2, 9) — Count these multisets by lining up the four faces in a row and inserting two dividers to cut the row into a first-colour block, a second-colour block and a third-colour block (blocks may be empty).
11. 🎲 (← 10) — Each multiset corresponds to exactly one placement of the dividers among the six slots in the row of faces and dividers. The count is the number of ways to choose which two of the six slots hold dividers.
12. ➕ (← 11) — That choice of two slots among six gives the total number of pictures.
13. 👀 (← 12) — Self-check: sorting the multisets by pattern (all four equal, three and one, two and two, two one one) reproduces the same total, so the two ways of counting agree.

LANDMARKS:
- Because four faces and three colours force a repeated colour, swapping two equal faces absorbs any odd rearrangement, so rotations are as good as all rearrangements.
- Hence a painting up to rotation is exactly a multiset of four colours from three.
- Multisets are counted by placing two dividers among six slots in a row of faces.
ANSWER: 15
