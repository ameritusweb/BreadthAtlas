---
id: 001
question: lockers-skip-first
title: Familiar game plus student 1, then take complement
strategy: new: complement-of-known-variant
contributor: sonnet (duelist B)
date: 2026-10-05
referee: opus/v1
criterion: v1
verdict: DUPLICATE
reason: Every landmark repeats route 001 in substance. "Student 1's absence flips each locker, so our result is the complement of the familiar result" is route 001's landmark 3, "dropping student 1 flips the parity". "The familiar game leaves only the ten perfect squares open" combines route 001's landmarks 2 and 4, which cover divisor pairing (only squares get an odd count) and the ten squares up to 100. Framing the argument as the familiar game plus one extra student is a change of presentation, not a new claim about the problem.
typed_1: reduction | our game | familiar game | reduces-to | one extra toggle per locker | Student 1 would toggle every locker exactly once, so our final state is the exact opposite of the familiar game's final state.
typed_2: symmetry | open lockers | closed lockers of familiar game | = | complement | A locker is open in our game exactly when it is closed in the familiar game, so the open set is the complement of the familiar open set.
typed_3: state | open lockers | non-squares | = | squares of 1 through 10 | The familiar game leaves only the ten perfect squares open, so the complement is all the other lockers.
---

CHAIN by duelist B
1. 🔒 (root) — Given: one hundred lockers stand in a row, all closed at the start.
2. 🚶 (root) — Given: students 2 to 100 walk past in turn, and student k toggles every locker whose number is a multiple of k.
3. 🙅 (root) — Given: student 1 is absent, so no one toggles every locker. This differs from the familiar version.
4. ❓ (← 1, 2, 3) — Asked: how many lockers are open at the end when student 1 never walks?
5. 🧩 (← 2, 3) — Picture the familiar game as our game plus one extra student 1, who toggles every locker exactly once.
6. 🔀 (← 5) — Only the parity of toggles matters, so one extra toggle on every locker flips every locker's final state; our result is the exact opposite of the familiar result.
7. 🪞 (← 1, 6) — Since all lockers start closed in both games, a locker is open in ours exactly when it is closed in the familiar game.
8. 🤝 (← 5) — In the familiar game, locker n is toggled once per divisor, and divisors pair up as d with n/d.
9. 🟦 (← 8) — Pairing leaves an odd count only when a divisor pairs with itself, so only perfect squares are open in the familiar game.
10. 🔟 (← 9) — The perfect squares from 1 to 100 are the squares of 1 through 10, so there are ten of them.
11. 🚪 (← 9, 10) — In the familiar game exactly ten lockers are open, and every other locker is closed.
12. 🔓 (← 7, 11) — So in our game the open lockers are exactly the ones closed in the familiar game, which is every locker except those ten.
13. 👀 (← 12) — Self-check: locker 1 is never toggled in our game, so it is closed, and it is a square, which agrees.
14. 🎯 (← 4, 10, 12) — Out of a hundred lockers, all but ten are open, which answers the question.
LANDMARKS:
- Student 1 would toggle every locker exactly once, so our final state is the exact opposite of the familiar game's final state.
- A locker is open in our game exactly when it is closed in the familiar game, so the open set is the complement of the familiar open set.
- The familiar game leaves only the ten perfect squares open, so the complement is all the other lockers.
ANSWER: 90
