---
id: 002
question: necklace-six-beads
title: Classify necklaces by number of one-colour runs
strategy: new: invariant-partition-by-run-count
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 2
referee: opus/v2
criterion: v2
verdict: VALID
reason: The new landmark is landmark 1: the chain sorts necklaces by the number of black runs, which turning and flipping preserve, instead of by black-bead count (route 001). The family counts (two, five, five and one) are each correct, the one-of-each case in step 10 correctly treats the two mirror-image forms as one necklace, and the total of 13 matches the reference, with no step-by-step state snapshots.
typed_1: structure | black-run count | turning and flipping | invariant | - | Necklaces are sorted by the number of one-colour runs around the ring, which turning and flipping preserve, rather than by the number of black beads.
typed_2: reduction | one- and two-black-run necklaces | run length and spare-bead placement among alternating runs | reduces-to | - | One black run gives five necklaces, set by the run length. Two black runs give five, by where two spare beads go among four alternating runs.
typed_3: reduction | three-black-run and single-colour necklaces | single-colour, alternating and three-bead-block rings | reduces-to | - | Three black runs force perfect alternation, giving one necklace, and the single-colour rings give two.
---

CHAIN by duelist B
1. 🔴 (root) — A necklace is a ring of six beads, each black or white.
2. 🔄 (root) — Two necklaces are the same if turning the ring or flipping it over makes one look like the other.
3. ❓ (← 1, 2) — How many different necklaces are there, with turning and flipping counted as the same?
4. 🧱 (← 1) — Read around the ring and group beads into runs of one colour. Unless the ring is a single colour, black runs and white runs alternate, so there are equally many of each.
5. 🔒 (← 2, 4) — Turning and flipping never change how many black runs there are, so the necklaces split into separate families by that count. A single-colour ring has no runs of the other colour and forms its own family.
6. ⬛ (← 5) — The single-colour family is all black or all white, which gives two necklaces.
7. 1️⃣ (← 5) — With one black run and one white run, the necklace is fixed by the length of the black run, from one to five. Flipping changes nothing here, so this family has five necklaces.
8. 3️⃣ (← 5) — With three black runs and three white runs, all six runs are one bead long, so beads simply alternate. That gives one necklace.
9. 2️⃣ (← 5) — With two black runs and two white runs, the four runs alternate around the ring. The two spare beads beyond one per run must be placed.
10. 🎯 (← 9) — If both spare beads go in one run, it is either a black run or a white run, which gives two necklaces. If they go in two different runs, the pair is both black, both white, or one of each, which gives three necklaces. In the one-of-each case every black run touches every white run, so the position is forced. The family has five necklaces.
11. 🧩 (← 6, 7, 8, 10) — Add the families: two single-colour, five with one black run, five with two, one with three. The total is thirteen.
12. 👀 (← 11) — Self-check: six runs is the most that fit in six beads, so no family with four or more black runs exists and nothing is missed.

LANDMARKS:
- Necklaces are sorted by the number of one-colour runs around the ring, which turning and flipping preserve, rather than by the number of black beads.
- One black run gives five necklaces, set by the run length. Two black runs give five, by where two spare beads go among four alternating runs.
- Three black runs force perfect alternation, giving one necklace, and the single-colour rings give two.
ANSWER: 13
