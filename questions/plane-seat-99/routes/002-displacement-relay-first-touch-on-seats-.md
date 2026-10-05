---
id: 002
question: plane-seat-99
title: Displacement relay; first touch on seats 1, 99, 100
strategy: new: displacement-relay-first-hit
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 2
referee: opus/v1
criterion: v1
verdict: VALID
reason: Every step follows from its parents and the answer 2/3 is correct. Chain 2 brings two new landmarks: displaced passengers form a forward-moving relay that stops at seat 1, and a pick of seat 100 never harms passenger 99. Its third landmark, about which seat the relay touches first, is close to route 001's landmark 2 but is a separate claim about the process rather than about the seats when passenger 99 boards.
typed_1: structure | displaced passengers | seat 1 | forbids | - | Displaced passengers form a forward-moving relay of random picks, and the relay stops the moment someone picks seat 1.
typed_2: state | seat 100 pick | passenger 99 | forbids | - | Picking seat 100 only affects passenger 100, who boards after passenger 99, so it never harms passenger 99.
typed_3: symmetry | occupied seat among 1, 99, 100 | seats 1, 99, 100 | bijects | 1/3 each | The first relay pick to touch seat 1, seat 99 or seat 100 is equally likely to be any of the three.
---

CHAIN by duelist B
1. 🪑 (root) — Given: 100 seats and 100 passengers, and passenger 1 picks a seat at random, possibly their own.
2. 🔁 (root) — Given: each later passenger takes their own seat if it is free, otherwise a uniformly random free seat.
3. 🪢 (← 1, 2) — Only a displaced passenger ever makes a random pick, so the trouble travels as a relay: passenger 1 picks a seat, its owner is bumped and picks, and so on.
4. ➡️ (← 2, 3) — Each bump goes to a later passenger than the one before, because a seat that is still free belongs to someone who has not yet boarded.
5. 🛑 (← 2, 3) — If anyone in the relay picks seat 1, the relay ends, because every remaining passenger finds their own seat free.
6. 🚪 (← 4, 5) — If the relay picks seat 100, passenger 100 is bumped, but that comes after passenger 99 has already sat, so passenger 99 is unaffected.
7. 🔔 (← 4) — Passenger 99 is bumped only if some relay member picks seat 99, since nobody else takes it.
8. ⚖️ (← 2, 3) — Until the relay touches one of them, seats 1, 99 and 100 are all free at every pick, so each pick is equally likely to land on any of the three.
9. 🥊 (← 5, 6, 8) — The first of those three seats that the relay touches is equally likely to be seat 1, 99 or 100, and only seat 99 bumps passenger 99.
10. ⅓ (← 7, 9) — Passenger 99 is therefore bumped in exactly one of three equally likely cases.
11. 👀 (← 10) — Self-check: on a three-seat plane the middle passenger is bumped only if passenger 1 picks the middle seat, which is one of three equal picks, matching this result.
12. ✅ (← 10, 11) — Passenger 99 keeps their own seat in the remaining two of the three cases.
LANDMARKS:
- Displaced passengers form a forward-moving relay of random picks, and the relay stops the moment someone picks seat 1.
- Picking seat 100 only affects passenger 100, who boards after passenger 99, so it never harms passenger 99.
- The first relay pick to touch seat 1, seat 99 or seat 100 is equally likely to be any of the three.
ANSWER: 2/3
