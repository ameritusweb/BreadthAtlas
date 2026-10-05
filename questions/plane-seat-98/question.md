---
id: plane-seat-98
title: The third-to-last passenger
status: answered
added: 2026-10-05
family: altered famous puzzle (parametrized sibling of plane-seat-99)
attractor: the lost-boarding-pass problem, last passenger, answer 1/2; and the sibling's 2/3
discriminator: the passenger of interest is the third-to-last, so there are FOUR decisive seats (1, 98, 99, 100)
guess_target: 0.75
guess_scale: linear
guess_unit: a probability between 0 and 1
---

# Question

One hundred passengers board a full plane in order. The first has lost their boarding pass and sits in
a random seat. Each later passenger takes their own seat if it is free, otherwise a random free seat.
**What is the probability that passenger 98 — the third-to-last — ends up in their own seat?**

# Reference answer (referee only)

**3/4.** For passenger k the decisive seats are seat 1, seat k, and the seats of everyone after k —
here seats 1, 98, 99, 100 — and a random chooser's pick settles k's fate only when it lands on one of
them; by symmetry each is equally likely to be hit first, and only seat 98 is bad. Tolerance: the exact
fraction or a decimal within 0.02. Both ½ and 2/3 are WRONG.

# Why it is in the atlas

Parametrized sibling of `plane-seat-99`. Every route found there (decisive-set symmetry, relay,
self-similar reduction, bootstrap from the last passenger's ½) applies, but the count of decisive
seats changes, so a recalled "three equal slices" is wrong here. Tests re-derivation versus recall.

# Breadth

No routes yet.
