---
id: 001
question: plane-seat-98
title: Four decisive seats, symmetric first hit
strategy: new: decisive-seats-symmetry
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 1
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is sound and it uses no simulation. It identifies the four decisive seats (1, 98, 99, 100) and argues by symmetry that each is equally likely to be taken first, so the answer is 3/4. All three landmarks are new because the frontier was empty.
typed_1: structure | chaos | seat 1 taken | reduces-to | - | Chaos ends as soon as seat 1 is taken, or when a taken seat's owner boards after passenger 98.
typed_2: symmetry | seat 1 and seats 98, 99 and 100 | decisive seats | invariant | first one taken | Among seat 1 and seats 98, 99 and 100, each is equally likely to be the first one taken, by symmetry.
typed_3: share | passenger 98 displaced | decisive seats | reduces-to | one case in four | Passenger 98 is displaced only if seat 98 is the first of those four seats taken, which is one case in four.
---

CHAIN by duelist A
1. ✈️ (root) — One hundred passengers board a full plane in order, one seat each.
2. 🎲 (root) — The first passenger sits in a random seat. Each later passenger takes their own seat if it is free, and otherwise a random free seat.
3. ❓ (← 1, 2) — What is the probability that passenger 98, the third-to-last, ends up in their own seat?
4. 🪑 (← 2) — Passenger 98 loses their seat only if someone takes it before they board, and only a random chooser can do that.
5. 🔗 (← 2, 4) — Chaos is carried by a chain of displaced people. Each random chooser takes a seat, and that seat's owner is displaced when they board, so the chain continues.
6. 1️⃣ (← 5) — The chain ends the moment someone takes seat 1, because passenger 1 has already boarded and nobody is displaced.
7. 🎯 (← 4, 5, 6) — Four seats matter before passenger 98 boards: seat 1, seat 98, seat 99 and seat 100. Seat 1 ends the chaos, and the other three are the seats we care about.
8. ⚖️ (← 2, 7) — Every random chooser picks uniformly among free seats. Seats 98, 99 and 100 and seat 1 are treated alike by a chooser, so each of the four is equally likely to be the first of them taken.
9. 🧯 (← 5, 7, 8) — If seat 99 or seat 100 is taken first, its owner boards after passenger 98, so no one before 98 is displaced and the chaos stops. Seat 98 stays free.
10. ✅ (← 6, 8) — If seat 1 is taken first, the chaos also stops and seat 98 stays free.
11. 💥 (← 8, 9, 10) — Only "seat 98 is taken first" ruins passenger 98. That is one of four equally likely outcomes, and the other three leave them safe.
12. 🧮 (← 11) — Three of the four equally likely outcomes are good for passenger 98, so they sit in their own seat three times out of four.
13. 👀 (← 12) — Self-check: the same argument for the last passenger has two relevant seats, seat 1 and seat 100. That gives one half, which is the known answer for the last passenger, so the method is consistent.

LANDMARKS:
- Chaos ends as soon as seat 1 is taken, or when a taken seat's owner boards after passenger 98.
- Among seat 1 and seats 98, 99 and 100, each is equally likely to be the first one taken, by symmetry.
- Passenger 98 is displaced only if seat 98 is the first of those four seats taken, which is one case in four.
ANSWER: 3/4
