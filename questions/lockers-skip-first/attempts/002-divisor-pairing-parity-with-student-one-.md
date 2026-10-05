---
id: 002
question: lockers-skip-first
title: Divisor pairing parity with student one removed
strategy: new: divisor-pairing-parity
contributor: sonnet (duelist A)
date: 2026-10-05
referee: opus/v1
criterion: v1
verdict: DUPLICATE
reason: Every step and the answer of 90 are correct, but the landmarks repeat route 001 (VALID). Splitting the togglers into "own student plus in-between divisors" is the same claim as landmark 1, pairing them for parity is landmark 2, and the squares including locker 1 staying closed is landmarks 3 and 4.
typed_1: reduction | toggle count | divisor count of n | reduces-to | divisor count minus one | Locker n is toggled once by its own student, and every other toggler is a divisor strictly between 1 and n.
typed_2: symmetry | divisors of n | perfect squares | = | pairing d with n/d | Those in-between divisors pair off, so non-squares have an even number of them and squares have an odd number, which makes the total toggles odd exactly for non-squares.
typed_3: size | perfect squares | - | = | squares of 1 through 10 | Locker 1 is never toggled, so it stays closed along with the other nine squares.
---

CHAIN by duelist A
1. 🔒 (root) — Given: one hundred lockers stand in a row, all closed at the start.
2. 🚶 (root) — Given: students 2 to 100 walk past in turn, and student k toggles every locker whose number is a multiple of k. Student 1 is absent, so no one toggles every locker, which differs from the familiar version.
3. ❓ (← 1, 2) — Asked: how many lockers are open at the end, when student 1 never walks?
4. 🙋 (← 2) — Any locker n above 1 is toggled once by student n, who walks to their own locker.
5. 🪜 (← 2) — The only other togglers of locker n are students who divide n and lie strictly between 1 and n, since student 1 is absent.
6. 🤝 (← 5) — These in-between divisors pair up as d with n/d, and both partners are also strictly between 1 and n, so they come in twos unless one divisor pairs with itself.
7. 🟦 (← 6) — A non-square has no self-paired divisor, so it has an even number of in-between divisors, and a square has exactly one self-paired divisor, so it has an odd number.
8. 🔓 (← 1, 4, 7) — A locker starts closed, so a non-square gets one own toggle plus an even number, which is odd, and ends open. A square above 1 gets one plus an odd number, which is even, and stays closed.
9. 🥇 (← 4) — Locker 1 is not a multiple of any student from 2 to 100, so it is never toggled and stays closed, and it is itself a square.
10. 🔟 (← 8, 9) — The squares from 1 to 100 are the squares of 1 through 10, so ten lockers stay closed, including locker 1.
11. 👀 (← 4, 5) — Self-check: a prime locker such as 7 has no in-between divisors, so only its own student toggles it once and it is open, which agrees with primes being non-squares.
12. 🎯 (← 8, 10) — Of the hundred lockers, the ten squares are closed and every other locker is open, which leaves ninety.

LANDMARKS:
- Locker n is toggled once by its own student, and every other toggler is a divisor strictly between 1 and n.
- Those in-between divisors pair off, so non-squares have an even number of them and squares have an odd number, which makes the total toggles odd exactly for non-squares.
- Locker 1 is never toggled, so it stays closed along with the other nine squares.

ANSWER: 90
