---
id: lockers-skip-first
title: The lockers, with the first student absent
status: answered
added: 2026-10-05
family: altered famous puzzle
attractor: the hundred lockers (students 1–100; answer 10, the perfect squares)
discriminator: student 1 is absent, so each locker's toggle count is its divisor count MINUS ONE; the parity is inverted relative to the famous game
guess_target: 90
guess_recall: likely   # 5/5 identical exact bare guesses on 2026-10-05: a known result, not an estimate
guess_scale: linear
guess_unit: number of lockers left open
---

# Question

One hundred lockers stand closed in a row. Students numbered 2 to 100 walk past in turn; student k
toggles (opens if closed, closes if open) every locker whose number is a multiple of k. Student 1 is
absent, so no one toggles every locker. **How many lockers are open at the end?**

# Reference answer (referee only)

**90.** Locker n is toggled once per divisor of n other than 1, i.e. d(n) − 1 times. It ends open when
that count is odd, i.e. when d(n) is even, i.e. when n is *not* a perfect square. There are 10 perfect
squares in 1–100, so 90 lockers are open. Locker 1 is toggled by nobody and stays closed, consistent
with 1 being a square. Tolerance: exact. The famous answer 10 is WRONG — the alteration inverts it.

# Why it is in the atlas

Altered-famous family. The attractor is strong ("lockers → perfect squares → 10") and the alteration
exactly flips the parity, so a snapped answer is maximally wrong. The holistic route is the divisor-
pairing picture with one divisor removed.

# Breadth

No routes yet.
