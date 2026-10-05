---
id: 002
question: cube-three-colours
title: Classify cubes by opposite-pair types, correct for chirality
strategy: new: axis-pair-decomposition
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 2
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is sound: the three opposite pairs are permuted freely and flipped two at a time, so the 56 multisets of pair-types each give one cube except {ab, bc, ca}, which splits into a mirror pair, for 57. All three landmarks are new: six opposite-pair types, the cube determined by its unordered pair-type collection (56), and the single chiral split adding one. None of them coincides with route 001's colour-count or face-pattern landmarks.
typed_1: structure | opposite pair of faces | six pair-types | ∈ | - | Each opposite pair of faces has one of six types: single-coloured in one of three colours, or mixed in one of three colour pairs.
typed_2: reduction | painted cubes | unordered collection of three pair-types | reduces-to | - | A cube is determined by the unordered collection of its three pair-types, giving fifty-six collections.
typed_3: symmetry | ab, bc, ca collection | two mirror-image cubes | bijects | - | Only the ab, bc, ca collection splits into two mirror-image cubes, which adds one.
---

CHAIN by duelist A
1. 🧊 (root) — A cube has six faces, and rotations are the only moves allowed for matching two cubes.
2. 🎨 (root) — Each face gets one of three colours, and colours may repeat or go unused.
3. ❓ (← 1, 2) — How many painted cubes are there if cubes that differ only by a rotation count as the same?
4. ↔️ (← 1) — The six faces form three opposite pairs, and every rotation carries opposite pairs to opposite pairs.
5. 🏷️ (← 2, 4) — Each opposite pair, read without regard to which face is which, has one of six types: both faces one of the three colours (three types), or the two faces two different colours (three types, one per pair of colours).
6. 🔀 (← 4) — Rotations can shuffle the three opposite pairs in any order, so which axis carries which type is irrelevant. The unordered collection of three types is what is left.
7. 📦 (← 5, 6) — Drawing three types with repetition from six gives fifty-six collections, and every collection can be painted, so there are at least fifty-six cubes.
8. 🎯 (← 7) — A collection gives more than one cube only if the way the mixed pairs' faces are oriented against each other cannot be undone by a rotation. A rotation flips two pairs at once, never one alone.
9. 🪞 (← 8) — That obstruction is a handedness, so it shows up only when a cube differs from its mirror image. It needs all three pairs mixed with all three colour-pairs different (ab, bc, ca), and the two arrangements are mirror images.
10. ➕ (← 9) — Every other collection gives exactly one cube, since its mixed pairs share a colour or a pair is single-coloured, and that lets a lone flip be traded for a rotation. The ab, bc, ca collection gives two cubes, so it adds exactly one extra cube.
11. 🧩 (← 7, 10) — Fifty-six collections plus one extra mirror-image cube gives fifty-seven cubes.
12. 👀 (← 11) — Self-check: with two colours the types are three (two single-coloured, one mixed), the collections of three number ten, and no handed case arises. This matches the known ten.

LANDMARKS:
- Each opposite pair of faces has one of six types: single-coloured in one of three colours, or mixed in one of three colour pairs.
- A cube is determined by the unordered collection of its three pair-types, giving fifty-six collections.
- Only the ab, bc, ca collection splits into two mirror-image cubes, which adds one.
ANSWER: 57
