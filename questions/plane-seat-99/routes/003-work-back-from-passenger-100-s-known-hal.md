---
id: 003
question: plane-seat-99
title: Work back from passenger 100's known half
strategy: new: bootstrap-from-known-answer
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 3
referee: opus/v1
criterion: v1
verdict: VALID
reason: The new landmark is the second one: passenger 100's losing half splits into the whole seat-100 case plus half of the seat-99 case, using the famous ½ answer for the last passenger. No earlier chain passed through this claim. The other two landmarks repeat route 001's landmarks 2–3, and every step is sound, giving the correct 2/3.
typed_1: symmetry | seat 99 | seat 100 | bijects | equally likely occupied | Seats 99 and 100 are interchangeable before passenger 99 boards, so "seat 99 is the occupied one" and "seat 100 is the occupied one" are equally likely.
typed_2: share | passenger 100 losing seat | seat-100 case plus half of seat-99 case | = | 1/2 | Passenger 100 loses their seat half the time, and that half is the whole seat-100 case plus half of the seat-99 case, because a displaced passenger 99 picks between seats 1 and 100 by a fair coin.
typed_3: share | passenger 99 displacement | occupied seat among 1, 99, 100 | = | 1/3 | Matching those two facts shows the seat-99 case is exactly one third of the possibilities.
---

CHAIN by duelist A
1. 🪑 (root) — Given: 100 seats and 100 passengers, and passenger 1 sits at random, possibly in their own seat 1.
2. 🔁 (root) — Given: each later passenger takes their own seat if it is free, otherwise a uniformly random free seat.
3. 🧍 (← 1, 2) — When passenger 99 boards, 98 people are seated, so exactly two seats are free.
4. 🧱 (← 2, 3) — Passengers 2 to 98 all sit in their own seats or are displaced into some other seat, so seats 2–98 are all full, which leaves exactly one of seats 1, 99 and 100 occupied.
5. 🅰️ (← 4) — That gives three exclusive cases, "seat 1 is the occupied one", "seat 99 is the occupied one" and "seat 100 is the occupied one", and passenger 99 is displaced only in the seat-99 case.
6. 👯 (← 2, 4) — Before passenger 99 boards, seats 99 and 100 are only ever taken by random picks, because their owners board later, so the two seats are interchangeable and the seat-99 case is as likely as the seat-100 case.
7. 📚 (root) — Given from general knowledge: the last passenger in this puzzle gets their own seat exactly half the time, and loses it the other half.
8. 🛎️ (← 4, 5) — Passenger 100 loses their seat only if seat 100 was already occupied when 99 boarded, or if 99 was displaced and then picked seat 100.
9. 🪙 (← 2, 5) — A displaced passenger 99 faces exactly two free seats, 1 and 100, and picks between them by a fair coin, so half of the seat-99 case reaches seat 100.
10. ⚖️ (← 6, 7, 8, 9) — Passenger 100's losing half is made of the whole seat-100 case plus half of the seat-99 case, and since those two cases are equal in size, one and a half such cases fill exactly half of everything.
11. ⅓ (← 5, 10) — So the seat-99 case, the only one that displaces passenger 99, is one third of the possibilities.
12. 👀 (← 5, 11) — Self-check: the seat-99 case and the seat-100 case are each one third, which leaves one third for the seat-1 case, and that matches the earlier equal-picks reasoning.
13. ✅ (← 11, 12) — Passenger 99 keeps their own seat in the remaining two thirds.
LANDMARKS:
- Seats 99 and 100 are interchangeable before passenger 99 boards, so "seat 99 is the occupied one" and "seat 100 is the occupied one" are equally likely.
- Passenger 100 loses their seat half the time, and that half is the whole seat-100 case plus half of the seat-99 case, because a displaced passenger 99 picks between seats 1 and 100 by a fair coin.
- Matching those two facts shows the seat-99 case is exactly one third of the possibilities.
ANSWER: 2/3
