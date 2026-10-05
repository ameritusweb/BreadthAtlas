---
id: 003
question: necklace-six-beads
title: Split by shortest repeating block, then subtract periodic cases
strategy: new: primitive-period-decomposition
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 3
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is sound and correct: there are 5 periodic necklaces (two single-colour, one alternating, BBW-repeat and BWW-repeat) and 8 aperiodic ones (1+2+2+2+1), with no step-by-step state snapshots. Steps 10 and 11 refer to steps 7 and 6 without tagging them, but that is acceptable because the periodicity of those cases follows from the step 4 definition they inherit. The new landmarks are the split by shortest repeating block, which no earlier binding chain used (route 001 used black count, route 002 used runs), and the count of five periodic necklaces that comes from it.
typed_1: structure | periodicity | turning and flipping | invariant | - | Rings are split by whether they are periodic, meaning a shorter block of one, two or three beads repeats, rather than by black count or runs.
typed_2: reduction | periodic necklaces | single-colour, alternating and three-bead-block rings | reduces-to | - | The periodic rings are the two single-colour rings, the alternating ring, and two three-bead-block rings, giving five.
typed_3: reduction | aperiodic necklaces | black-bead count | reduces-to | - | The aperiodic rings number eight, found by excluding the periodic cases from each count of black beads.
---

CHAIN by duelist A
1. 🔴 (root) — A necklace is a ring of six beads, each black or white.
2. 🔄 (root) — Two necklaces are the same if turning the ring or flipping it over makes one look like the other.
3. ❓ (← 1, 2) — How many different necklaces are there, with turning and flipping counted as the same?
4. 🔁 (← 1, 2) — Call a ring periodic if it is just a shorter block repeated around the ring. The block length must divide six, so it is one, two or three beads. Turning and flipping keep this property, so periodic and aperiodic rings never get confused.
5. ⚪ (← 4) — A block of one bead means a single-colour ring, either all black or all white. That gives two necklaces.
6. ➰ (← 4) — A shortest block of two beads must be one black and one white, which gives strict alternation. That gives one necklace.
7. 🔺 (← 4) — A shortest block of three beads must use both colours, and a block that is not purely alternating can only be two of one colour and one of the other, so it is two black then one white, or one black then two white. Repeating either gives a ring, and the two rings are different. That gives two necklaces.
8. 🧮 (← 5, 6, 7) — Together the periodic rings make up five necklaces.
9. 🌀 (← 1, 4) — Now take the aperiodic rings, where no shorter block repeats, and sort them by number of black beads. A lone black bead gives one ring, and a lone white bead gives one ring.
10. ✌️ (← 9) — With two black beads, the pair is touching, one bead apart, or opposite. Opposite is the three-bead repeat from step 7, so it is already counted, which leaves two aperiodic rings. Swapping colours gives two more rings with four black beads.
11. 🔱 (← 9) — With three black beads, either all three touch, or two touch and one stands apart. The alternating ring is already counted as periodic, so two aperiodic rings remain.
12. 🧩 (← 9, 10, 11) — Adding the aperiodic rings gives one with a lone black bead, two with two black, two with three black, two with four black and one with five black. That makes eight aperiodic necklaces.
13. 🏁 (← 3, 8, 12) — Every ring is either periodic or aperiodic, and never both. The five periodic and eight aperiodic necklaces together make thirteen.
14. 👀 (← 13) — Self-check: thirteen matches the known count of two-colour bracelets of length six.

LANDMARKS:
- Rings are split by whether they are periodic, meaning a shorter block of one, two or three beads repeats, rather than by black count or runs.
- The periodic rings are the two single-colour rings, the alternating ring, and two three-bead-block rings, giving five.
- The aperiodic rings number eight, found by excluding the periodic cases from each count of black beads.
ANSWER: 13
