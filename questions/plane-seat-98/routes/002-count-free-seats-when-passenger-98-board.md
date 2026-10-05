---
id: 002
question: plane-seat-98
title: Count free seats when passenger 98 boards
strategy: new: pigeonhole-at-boarding
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 2
referee: opus/v2
criterion: v2
verdict: VALID
reason: Every step holds and 3/4 is correct. Step 5 states a simple count in words ("three free"), which is not simulation. The first two landmarks are new to this question: when passenger 98 boards, seats 2 to 97 are all occupied, so exactly one of seats 1, 98, 99 and 100 is taken. Route 001 instead tracked the first of those seats to be taken. The third landmark matches route 001's landmark 3 in substance and adds nothing new.
typed_1: state | seats 2 to 97 | free seats | = | three free seats | When passenger 98 boards, every seat from 2 to 97 is already occupied, so exactly three seats are free.
typed_2: structure | seat 1 and seats 98, 99 and 100 | free seats | ∈ | one occupied seat | Those three free seats are three of the four seats 1, 98, 99 and 100, so exactly one of those four is occupied.
typed_3: share | passenger 98 displaced | decisive seats | reduces-to | one case in four | Passenger 98 is displaced only if the one occupied seat of the four is seat 98, which is one case in four.
---

CHAIN by duelist A
1. ✈️ (root) — One hundred passengers board a full plane in order, one seat each.
2. 🎲 (root) — The first passenger sits in a random seat. Each later passenger takes their own seat if it is free, and otherwise a random free seat.
3. ❓ (← 1, 2) — What is the probability that passenger 98, the third-to-last, ends up in their own seat?
4. 🧱 (← 2) — Before passenger 98 boards, each of passengers 2 to 97 has either sat in their own seat or been displaced. A displaced passenger's seat was already taken, so every seat from 2 to 97 is occupied.
5. 🔢 (← 1, 4) — Ninety-seven passengers are seated and the plane has one hundred seats, so exactly three seats are free when passenger 98 boards.
6. 🧺 (← 4, 5) — Seats 2 to 97 are all full, so the three free seats must come from the four seats 1, 98, 99 and 100. Exactly one of those four is occupied.
7. 🕳️ (← 6) — Passenger 98 is displaced exactly when the one occupied seat among the four is seat 98. If it is seat 1, 99 or 100, seat 98 is free.
8. 🙋 (← 2, 6) — Passengers 99 and 100 have not boarded yet, so no one has sat in seats 99 or 100 by choosing their own seat. Only a random chooser could have taken the single occupied seat among the four.
9. ⚖️ (← 2, 8) — A random chooser treats seats 1, 98, 99 and 100 identically, since all are free and nobody has a reason to prefer one. So each of the four is equally likely to be the one occupied seat.
10. 🧮 (← 7, 9) — The one occupied seat is seat 98 in one case out of four. In the other three cases seat 98 is free and passenger 98 sits in their own seat.
11. 👀 (← 10) — Self-check: for the last passenger, one seat is free and it is either seat 1 or seat 100, equally likely. That gives one half, the known answer, so the counting method is consistent.

LANDMARKS:
- When passenger 98 boards, every seat from 2 to 97 is already occupied, so exactly three seats are free.
- Those three free seats are three of the four seats 1, 98, 99 and 100, so exactly one of those four is occupied.
- Passenger 98 is displaced only if the one occupied seat of the four is seat 98, which is one case in four.
ANSWER: 3/4
