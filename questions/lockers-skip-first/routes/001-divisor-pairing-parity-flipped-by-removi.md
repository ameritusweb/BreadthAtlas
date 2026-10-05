---
id: 001
question: lockers-skip-first
title: Divisor-pairing parity, flipped by removing divisor one
strategy: new: parity-by-pairing
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 1
referee: opus/v1
criterion: v1
verdict: VALID
reason: Every step follows from its parents and the answer of 90 is exact. The frontier was empty, so all four landmarks are new: toggle count equals divisor count minus one, divisor pairing gives squares an odd count, dropping student 1 flips the parity so the non-squares end open, and there are ten squares up to 100.
typed_1: reduction | toggle count | divisor count of n | reduces-to | divisor count minus one | Locker n is toggled once per divisor other than 1, so the toggle count is one less than the divisor count.
typed_2: symmetry | divisors of n | perfect squares | = | pairing d with n/d | Divisors pair up as d with n/d, so only perfect squares have an odd number of divisors.
typed_3: state | open lockers | non-squares | = | parity of toggle count | Dropping student 1 flips the parity, so the open lockers are the non-squares and the squares stay closed.
typed_4: size | perfect squares | - | = | squares of 1 through 10 | There are ten perfect squares up to 100, so the rest are open.
---

CHAIN by duelist A
1. 🔒 (root) — Given: there are one hundred lockers in a row, all closed at the start.
2. 🚶 (root) — Given: students numbered 2 to 100 walk past in turn, and student k toggles every locker whose number is a multiple of k.
3. 🙅 (root) — Given: student 1 is absent, so no one toggles every locker. This differs from the familiar version.
4. ❓ (← 1, 2, 3) — Asked: how many lockers are open at the end, when student 1 never toggles?
5. 🔁 (← 2, 3) — Locker n is toggled once for each divisor of n other than 1, because student 1 is missing.
6. ⚖️ (← 1, 5) — A locker starts closed, so it ends open exactly when it is toggled an odd number of times.
7. 🤝 (← 5) — Divisors of n pair up as d with n/d, so the full divisor count is even unless some divisor pairs with itself.
8. 🟦 (← 7) — Only perfect squares have a self-paired divisor, so squares have an odd number of divisors and non-squares an even number.
9. ➖ (← 5, 8) — The toggle count is the divisor count with the divisor 1 removed, which flips the parity: non-squares get an odd number of toggles and squares an even number.
10. 🔓 (← 6, 9) — So the lockers that end open are exactly the non-squares, and the squares stay closed.
11. 🔟 (← 10) — The perfect squares from 1 up to 100 are the squares of 1 through 10, so there are ten of them.
12. 👀 (← 9, 10) — Self-check: locker 1 is never toggled, so it stays closed, and it is a square, which agrees with the rule.
13. 🎯 (← 10, 11) — Of the hundred lockers, the ten squares stay closed and all the rest are open, which gives ninety.

LANDMARKS:
- Locker n is toggled once per divisor other than 1, so the toggle count is one less than the divisor count.
- Divisors pair up as d with n/d, so only perfect squares have an odd number of divisors.
- Dropping student 1 flips the parity, so the open lockers are the non-squares and the squares stay closed.
- There are ten perfect squares up to 100, so the rest are open.

ANSWER: 90
