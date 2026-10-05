---
id: 002
question: lockers-skip-first
title: Divisor-count parity via prime-exponent factorization
strategy: new: prime-exponent-parity
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 2
referee: opus/v1
criterion: v1
verdict: VALID
reason: The new landmark is "the divisor count is the product of one more than each prime exponent, so it is odd exactly when every exponent is even." No earlier binding chain passed through it, because route 001 and attempt 002 reached the square/non-square split by pairing d with n/d. The other two landmarks repeat route 001's landmarks 1–3, and all steps follow from their parents, giving the correct answer of 90.
typed_1: structure | divisor count of n | prime exponents of n | = | product of one-more-than-each-exponent | A number's divisor count is the product of one-more-than-each-prime-exponent, so it is odd exactly when every exponent is even.
typed_2: structure | divisors of n | perfect squares | = | all prime exponents even | Every exponent being even means the number is a perfect square, so only squares have an odd divisor count.
typed_3: reduction | toggle count | divisor count of n | reduces-to | divisor count minus one | With student 1 absent the toggle count is the divisor count minus one, so the open lockers are exactly the non-squares.
---

CHAIN by duelist B
1. 🔒 (root) — Given: one hundred lockers stand in a row, all closed at the start.
2. 🚶 (root) — Given: students 2 to 100 walk past in turn, and student k toggles every locker whose number is a multiple of k; student 1 is absent, so no one toggles every locker, which differs from the familiar version.
3. ❓ (← 1, 2) — Asked: how many lockers are open at the end, when student 1 never walks?
4. 🧬 (root) — Given from general knowledge: every number splits uniquely into primes with exponents, and each divisor is made by choosing, for every prime, how many copies of it to keep, from none up to all of them.
5. 🧮 (← 4) — So the number of divisors of a locker is the product of the per-prime choice counts, where a prime with exponent e offers one more choice than e.
6. 🔢 (← 5) — A product of whole numbers is odd only when every factor is odd, so the divisor count is odd exactly when every prime's exponent is even.
7. 🟦 (← 6) — All exponents even means the number is a perfect square, built from half of each exponent, and every perfect square has this form, so the divisor count is odd exactly for squares.
8. ➖ (← 2) — Locker n is toggled by exactly its divisors other than 1, because student 1 is absent, so the toggle count is the divisor count with one removed.
9. 🔁 (← 1, 7, 8) — A locker starts closed and ends open exactly when toggled an odd number of times, which happens when the divisor count is even, so open lockers are exactly the non-squares.
10. 🔟 (← 9) — Ten is the largest whole number whose square fits within a hundred, since the square of ten is exactly the last locker number, so ten lockers are squares.
11. 👀 (← 8, 9) — Self-check: a prime locker has only itself and 1 as divisors, so it is toggled by one student only and ends open, which agrees with primes being non-squares.
12. 🎯 (← 3, 9, 10) — Of the hundred lockers, the ten squares stay closed and all the others are open, which answers the question.
LANDMARKS:
- A number's divisor count is the product of one-more-than-each-prime-exponent, so it is odd exactly when every exponent is even.
- Every exponent being even means the number is a perfect square, so only squares have an odd divisor count.
- With student 1 absent the toggle count is the divisor count minus one, so the open lockers are exactly the non-squares.
ANSWER: 90
