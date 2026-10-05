---
id: 004
question: necklace-six-beads
title: Rotation classes first, then flips merge chiral pairs
strategy: new: refine-then-quotient (count under subgroup, merge by mirror pairs)
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 4
referee: opus/v2
criterion: v2
verdict: VALID
reason: Two landmarks are new. One counts turning alone first, giving fourteen classes, and then lets flipping merge them. The other says every ring except one handed pair is its own mirror image, and that pair is the two three-black rings with a touching pair and a separate bead. No earlier route went through either claim, and the chain contains no state snapshots.
typed_1: reduction | necklaces | turning-only classes | reduces-to | - | Count rings up to turning alone first, giving fourteen classes, then let flipping merge classes afterwards.
typed_2: symmetry | turning-only classes | mirror image | invariant | - | Every ring except one pair is its own mirror image, so flipping merges only a single pair of turning classes.
typed_3: structure | three-black rings with a touching pair and a separate bead | mirror image | bijects | - | That one handed pair is the two three-black rings with a touching pair and a separate bead, which are mirror images but not turnings of each other.
---

CHAIN by duelist B
1. 🔴 (root) — A necklace is a ring of six beads, each black or white.
2. 🔄 (root) — Two necklaces are the same if turning the ring or flipping it over makes one look like the other.
3. ❓ (← 1, 2) — How many different necklaces are there, with turning and flipping counted as the same?
4. 🔃 (← 1, 2) — Handle the two moves in stages: first count rings up to turning alone, then see how flipping merges some of those classes.
5. ⚫ (← 4) — Turning never changes the number of black beads, so sort the turning-only classes by that number. With none, one, five or six black beads there is a single class each, since a lone odd bead can only sit in one place up to turning.
6. ✌️ (← 5) — With two black beads, the turning classes are set by the gap between them: touching, one between, or opposite. That gives three classes, and by colour swap four black beads also give three.
7. 🔱 (← 5) — With three black beads, the turning classes are: all three together, alternating, and two patterns where a pair touches and one bead stands apart. The two apart-patterns differ in which way round the lone bead sits. That gives four classes.
8. 🧮 (← 5, 6, 7) — Gathering the groups gives fourteen classes under turning alone.
9. 🪞 (← 2, 4) — Flipping can only merge a class with another class if the ring looks different from its own mirror image. A ring that matches its mirror image stays alone.
10. 🙂 (← 5, 6, 9) — Every class with zero, one, two, four, five or six black beads is its own mirror image. The two-black gap patterns are left-right symmetric, and colour swap carries this to four black.
11. 🤝 (← 7, 9) — With three black beads, the all-together ring and the alternating ring are their own mirror images. The two apart-patterns are mirror images of each other but are different by turning, so flipping merges them into one.
12. 🧩 (← 8, 10, 11) — Exactly one pair of classes merges. The fourteen turning classes therefore drop by one, to thirteen.
13. 👀 (← 12) — Self-check: thirteen is one below the fourteen turning-only classes, and the single handed pair is the only difference.

LANDMARKS:
- Count rings up to turning alone first, giving fourteen classes, then let flipping merge classes afterwards.
- Every ring except one pair is its own mirror image, so flipping merges only a single pair of turning classes.
- That one handed pair is the two three-black rings with a touching pair and a separate bead, which are mirror images but not turnings of each other.
ANSWER: 13
