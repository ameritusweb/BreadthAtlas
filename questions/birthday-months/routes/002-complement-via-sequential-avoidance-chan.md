---
id: 002
question: birthday-months
title: Complement via sequential avoidance chances reaching zero
strategy: new: complement-product
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 2
referee: opus/v1
criterion: v1
verdict: VALID
reason: Every step is sound and the answer of 1 is exact. Landmarks 2 and 3 repeat route 001's pigeonhole and certainty claims, but landmark 1 is new: no earlier binding chain finds the complement by multiplying each arrival's chance of avoiding the earlier months, a chance that shrinks to zero at the thirteenth person.
typed_1: rate | newcomer's avoidance chance | free months | reduces-to | - | For everyone to have different months, each new arrival must avoid all earlier months, and that chance shrinks as the free months get used up.
typed_2: obstruction | distinct birth months assignment | thirteenth person | forbids | twelve | After twelve people, no free month remains, so the chance the thirteenth avoids a match is nothing.
typed_3: state | shared birth month | every arrangement | invariant | certainty | The probability that all twenty-three months differ is zero, so its complement, a shared month, has probability one.
---

CHAIN by duelist B
1. 🧑‍🤝‍🧑 (root) — Given: twenty-three people are in a room.
2. 📅 (root) — Given from general knowledge: a year has exactly twelve calendar months, and each person is born in exactly one of them.
3. ❓ (← 1, 2) — Asked: what is the probability that at least two of the twenty-three share a birth month? This is the month version, not the familiar day-of-year birthday problem.
4. 🔄 (← 3) — Use the complement. "At least two share a month" is the opposite of "everyone has a different month", so the two probabilities fill the whole certainty between them.
5. 🚶 (← 1, 4) — Bring the people in one at a time. For "all different" to hold, each newcomer must land in a month that nobody before them has.
6. 🟢 (← 2, 5) — Count the free months as people arrive. The first person has all twelve free, and each later arrival leaves one fewer free month than before.
7. 📉 (← 6) — The chance that a newcomer avoids all earlier months shrinks with every arrival, because the free months dwindle. It starts near certain and ends up small.
8. 🈳 (← 2, 6) — After twelve people with all different months, no month is left free. The count of free months has dropped to nothing.
9. 🚫 (← 7, 8) — So for the thirteenth person, the chance of landing in a free month is nothing. A newcomer cannot avoid a month that has no free option.
10. ⛓️ (← 5, 9) — "All different" needs every newcomer's step to succeed in turn. One step with no chance of success makes the whole chain's chance nothing.
11. ➕ (← 1, 10) — The room has twenty-three people, so it reaches the thirteenth person and beyond. The impossible step is therefore part of this room.
12. 🅾️ (← 4, 11) — The chance that all twenty-three have different months is zero.
13. 🎯 (← 4, 12) — The complement of a zero chance is full certainty, so a shared month has probability one.
14. 👀 (← 3, 13) — Self-check: this is about months, not days. The famous roughly even-odds result at twenty-three belongs to days, so it does not apply here.

LANDMARKS:
- For everyone to have different months, each new arrival must avoid all earlier months, and that chance shrinks as the free months get used up.
- After twelve people, no free month remains, so the chance the thirteenth avoids a match is nothing.
- The probability that all twenty-three months differ is zero, so its complement, a shared month, has probability one.

ANSWER: 1 (100%, certain)
