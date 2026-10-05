---
id: 001
question: cube-three-colours
title: Burnside average of fixed colourings over rotation classes
strategy: new: burnside-orbit-averaging
contributor: sonnet (duelist B)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: ILL-FORMED
reason: Step 9 does arithmetic in words. It raises three to each cycle count, weights each result by the number of rotations of that type, and adds them to an exact total of 1368; step 10 then divides by twenty-four. That is multiplying stated numbers to a numeric result, which §1 "No calculation" forbids, and the third landmark ("the total over all rotations is 1368") is the output of that sum rather than a structural claim. The chain is otherwise sound and would be new, so its landmarks are recorded but do not bar a later well-formed chain on this route.
typed_1: structure | cube rotations | five axis types | reduces-to | - | The rotation group has twenty-four elements, in five axis types of sizes 1, 6, 3, 8 and 6.
typed_2: symmetry | fixed paintings | face-cycles | invariant | - | A painting is fixed by a rotation exactly when it is constant on each face-cycle, giving cycle counts 6, 3, 4, 2 and 3.
typed_3: reduction | painted cubes | average number of fixed paintings | reduces-to | - | Burnside's lemma: the number of cubes equals the average number of fixed paintings, and the total over all rotations is 1368.
---

CHAIN by duelist B
1. 🧊 (root) — A cube has six faces, and only rotations of the cube may be used to match two cubes.
2. 🎨 (root) — Each face gets one of three colours, and colours may repeat or go unused.
3. ❓ (← 1, 2) — How many painted cubes are there if cubes that differ only by a rotation count as the same?
4. 🔄 (← 1) — The rotations of the cube number twenty-four: any of six faces can go on the bottom, and then there are four spins about the vertical axis.
5. 🧭 (← 4) — Sort the twenty-four rotations by axis type: the identity (1), quarter-turns about face axes (6), half-turns about face axes (3), third-turns about vertex axes (8), and half-turns about edge axes (6).
6. 🔗 (← 2, 3) — A painted cube is unchanged by a rotation exactly when every cycle of faces under that rotation is one colour. So the fixed paintings number three choices for each cycle.
7. 🧱 (← 5, 6) — The cycle counts are six for the identity, three for a quarter-turn (top, bottom, side ring), four for a face half-turn, two for a vertex third-turn and three for an edge half-turn.
8. ⚖️ (← 3, 4) — By Burnside's lemma, the number of distinct painted cubes equals the average number of paintings fixed per rotation, taken over all twenty-four rotations.
9. 🧮 (← 5, 6, 7) — Weighting each type's fixed-painting count by how many rotations it has and adding them all gives thirteen hundred sixty-eight.
10. 🎯 (← 8, 9) — Averaging that total over the twenty-four rotations gives fifty-seven.
11. 👀 (← 10) — Self-check: with two colours the same method gives a total of two hundred forty, so ten cubes, which matches the known count.

LANDMARKS:
- The rotation group has twenty-four elements, in five axis types of sizes 1, 6, 3, 8 and 6.
- A painting is fixed by a rotation exactly when it is constant on each face-cycle, giving cycle counts 6, 3, 4, 2 and 3.
- Burnside's lemma: the number of cubes equals the average number of fixed paintings, and the total over all rotations is 1368.
ANSWER: 57
