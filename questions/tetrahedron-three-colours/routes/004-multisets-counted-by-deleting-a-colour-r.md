---
id: 004
question: tetrahedron-three-colours
title: Multisets counted by deleting a colour, recursing on size
strategy: new: deletion-recursion-on-multiset-size
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 4
referee: opus/v2
criterion: v2
verdict: VALID
reason: Steps 4–7 re-reach route 003's reduction to multisets of four colours from three, but the counting is new. Deleting one C-face gives a reversible recursion on multiset size, which differs from route 003's dividers among six slots and is not a change of yardstick. The other new landmarks are the doubled/mixed split of pairs and the with-C/without-C splits at sizes three and four. Every step is sound and the answer 15 is exact.
typed_1: reduction | multisets of four colours from three | multisets of three colours from three | reduces-to | - | Removing one face of a chosen colour is a reversible correspondence between multisets of four with that colour present and multisets of three, so the count follows a recursion on size.
typed_2: size | multisets of two colours from three | - | = | - | Multisets of two colours from three split into three doubled and three mixed, giving six.
typed_3: size | multisets of four colours from three | multisets of three colours from three | = | - | Size-three multisets split into four without C and six with C, and size-four multisets into five without C and ten with C.
---

CHAIN by duelist B
1. 🔺 (root) — A regular tetrahedron has four faces.
2. 🎨 (root) — Each face is painted one of three colours, A, B or C, and two paintings are the same if a rotation (no reflection) turns one into the other.
3. ❓ (← 1, 2) — How many different painted tetrahedra are there up to rotation?
4. 🔄 (← 1) — Rotations realise exactly the even permutations of the four faces, which is half of all rearrangements.
5. 🕊️ (← 1, 2) — Four faces and three colours force some colour onto at least two faces, by pigeonhole.
6. 🧲 (← 4, 5) — Swapping two equally coloured faces is an odd rearrangement that changes nothing. So any rearrangement can be replaced by a rotation, and paintings with the same colour counts are equivalent.
7. 🧺 (← 3, 6) — A painting up to rotation is exactly a multiset of four colours drawn from three, and different multisets are never equivalent.
8. ✂️ (← 2, 7) — Split the multisets by whether colour C appears at all, giving two disjoint families that together cover everything.
9. 🅰️ (← 7, 8) — With C absent, a multiset of four from A and B is fixed by how many faces are A, which can be none through four, so there are five.
10. 🔻 (← 7, 8) — With C present, delete one C-face. This is a reversible correspondence with multisets of three colours from the three colours, since adding a C back undoes it.
11. 🔁 (← 10) — Split those size-three multisets the same way. With C absent, they are multisets of three from A and B, fixed by the A count from none to three, so there are four.
12. 🪓 (← 10, 11) — With C present among the three, delete another C. This leaves multisets of two colours from the three colours.
13. 👯 (← 12) — A pair either repeats a colour, which can be done in three ways, or uses two different colours, which can also be done in three ways. So there are six pairs.
14. 🧮 (← 11, 13) — The size-three multisets are the four without C plus the six with C, which gives ten.
15. ➕ (← 9, 10, 14) — The size-four multisets are the five without C plus the ten with C, which gives the total number of pictures.
16. 👀 (← 15) — Self-check: the total agrees with the counts by pattern (three single-colour, six three-and-one, three two-and-two, three two-one-one).

LANDMARKS:
- Removing one face of a chosen colour is a reversible correspondence between multisets of four with that colour present and multisets of three, so the count follows a recursion on size.
- Multisets of two colours from three split into three doubled and three mixed, giving six.
- Size-three multisets split into four without C and six with C, and size-four multisets into five without C and ten with C.
ANSWER: 15
