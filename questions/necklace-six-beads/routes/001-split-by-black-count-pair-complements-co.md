---
id: 001
question: necklace-six-beads
title: Split by black count, pair complements, count gaps
strategy: new: invariant-partition-with-complement-pairing
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 1
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is sound and reaches 13. The final tally adds up already-counted cases, which is counting and not simulation or arithmetic, and no step snapshots any state. With the frontier empty, all three landmarks are new: the black-count invariant split, the colour-swap pairing of complementary groups, and the gap-pattern counts for two and three black beads (three each, with flipping merging the two-one-none orders).
typed_1: structure | black-bead count | turning and flipping | invariant | - | The number of black beads is unchanged by turning and flipping, so it splits the necklaces into separate groups.
typed_2: symmetry | k-black necklaces | (6−k)-black necklaces | bijects | - | Swapping colours pairs the groups: four black with two, five with one, six with none.
typed_3: reduction | two- and three-black necklaces | gap between blacks and white placement in gaps | reduces-to | - | Two black beads give three necklaces, by the gap between them. Three black beads give three, by how the whites fall in the gaps.
---

CHAIN by duelist A
1. 🔴 (root) — A necklace is a ring of six beads, each black or white.
2. 🔄 (root) — Necklaces count as the same if turning the ring or flipping it over makes one look like the other.
3. ❓ (← 1, 2) — How many different necklaces are there, with turning and flipping counted as the same?
4. ⚫ (← 1) — Sort the necklaces by how many beads are black. Turning and flipping never change that number, so necklaces with different counts can never be the same.
5. 🪞 (← 3, 4) — Swapping black and white maps the necklaces with k black beads one-to-one onto those with k white beads. So the group with four black mirrors the group with two black, five mirrors one, and six mirrors none.
6. 0️⃣ (← 4) — With no black bead, or with exactly one, there is just one necklace each. All positions of a lone bead look alike after turning.
7. ✌️ (← 4) — With two black beads, the only thing that matters is how far apart they sit: touching, one bead between, or opposite. That gives three necklaces.
8. 🔱 (← 4) — With three black beads, the three white beads fall into the three gaps between them. They can all be in one gap, split as two, one and none (flipping makes the two orders the same), or spread one in each gap. That gives three necklaces.
9. 🔗 (← 5, 6, 7) — By the colour-swap mirror, four black beads gives as many necklaces as two black (three). Five black gives as many as one black (one), and six black gives as many as none (one).
10. 🧩 (← 6, 7, 8, 9) — Put the groups together. Zero and six black give one each, one and five black give one each, two and four black give three each, and three black gives three. The total is thirteen.
11. 👀 (← 10) — Self-check: these are the binary bracelets of length six, a known family whose sequence runs 2, 3, 4, 6, 8, 13 and so gives thirteen at length six.

LANDMARKS:
- The number of black beads is unchanged by turning and flipping, so it splits the necklaces into separate groups.
- Swapping colours pairs the groups: four black with two, five with one, six with none.
- Two black beads give three necklaces, by the gap between them. Three black beads give three, by how the whites fall in the gaps.
ANSWER: 13
