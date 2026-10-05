---
id: 001
question: plane-seat-99
title: First-occupied of three decisive seats is uniform
strategy: new: decisive-set symmetry
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 1
referee: opus/v1
criterion: v1
verdict: VALID
reason: The chain is sound: seats 2–98 must be filled before passenger 99 boards, which leaves exactly one of seats 1, 99 and 100 occupied, and by symmetry each is equally likely to be that seat, so the answer is 2/3. The frontier was empty, so all three landmarks are new: the filled block of seats 2–98, the single occupied seat among the three being equally likely to be any of them, and the one-in-three chance that it is seat 99.
typed_1: state | seats 2–98 | passenger 99 boarding | = | two free seats | When passenger 99 boards, exactly two seats are free, and seats 2–98 are all already filled.
typed_2: symmetry | occupied seat among 1, 99, 100 | seats 1, 99, 100 | bijects | 1/3 each | Exactly one of seats 1, 99 and 100 is occupied at that moment, and each of the three is equally likely to be that one.
typed_3: share | passenger 99 displacement | occupied seat among 1, 99, 100 | = | 1/3 | Passenger 99 is displaced only if that occupied seat is seat 99, which is a one-in-three chance.
---

CHAIN by duelist A
1. 🪑 (root) — Given: 100 seats and 100 passengers, and passenger 1 sits randomly, which may be their own seat 1.
2. 🔁 (root) — Given: each later passenger takes their own seat if it is free, otherwise a uniformly random free seat.
3. 🧍 (← 1, 2) — When passenger 99 boards, 98 people are seated, so exactly two seats are free.
4. 🧱 (← 2, 3) — Every passenger from 2 to 98 ends up seated, and none of them can be left without a seat. This means seats 2 through 98 are all occupied by the time 99 boards.
5. 🎯 (← 3, 4) — Of the three seats 1, 99 and 100, exactly one is occupied by then, because 98 are seated and seats 2–98 account for 97.
6. 🧩 (← 5) — Passenger 99 sits in their own seat unless the one occupied seat among the three is seat 99.
7. 🎲 (← 1, 2) — Whenever someone picks a random seat while seats 1, 99 and 100 are all still free, those three seats are equally likely picks.
8. 🔗 (← 2, 7) — Nobody ever takes seat 99 or seat 100 except by a random pick, since their owners board later. Seat 1 is taken only by passenger 1's own random pick or by a later random pick.
9. 🥇 (← 5, 7, 8) — The first of the three seats to be occupied is therefore equally likely to be seat 1, 99 or 100.
10. ☝️ (← 5, 9) — Only one of the three is occupied when 99 boards, so that first-occupied seat is the only one.
11. ⅓ (← 6, 10) — Passenger 99 is displaced only if that single seat is 99, which is one case out of three equally likely cases.
12. 👀 (← 11) — Self-check: by the same reasoning, passenger 100 gets their seat in one of two equally likely cases when only seats 1 and 100 are in play, which matches the known one-half. So the method is consistent.
13. ✅ (← 11, 12) — The chance of the own seat is the remainder, two cases out of three.

LANDMARKS:
- When passenger 99 boards, exactly two seats are free, and seats 2–98 are all already filled.
- Exactly one of seats 1, 99 and 100 is occupied at that moment, and each of the three is equally likely to be that one.
- Passenger 99 is displaced only if that occupied seat is seat 99, which is a one-in-three chance.

ANSWER: 2/3
