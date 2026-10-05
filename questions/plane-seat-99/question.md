---
id: plane-seat-99
title: The second-to-last passenger
status: answered
added: 2026-10-05
family: altered famous puzzle
attractor: the lost-boarding-pass problem, last passenger, answer 1/2
discriminator: the passenger of interest is the second-to-last, so there are THREE decisive seats (1, 99, 100), not two
guess_target: 0.6667
guess_scale: linear
guess_unit: a probability between 0 and 1
---

# Question

One hundred passengers board a full plane in order. The first has lost their boarding pass and sits in
a random seat. Each later passenger takes their own seat if it is free, otherwise a random free seat.
**What is the probability that passenger 99 — the second-to-last — ends up in their own seat?**

# Reference answer (referee only)

**2/3.** For passenger k the decisive seats are seat 1, seat k, and the seats of everyone after k; a
random chooser's pick settles k's fate only when it lands on one of these, and they are symmetric. For
k = 99 there are three (seats 1, 99, 100), one of which is bad. Tolerance: the exact fraction, or a
decimal within 0.02. The famous answer ½ (for passenger 100) is WRONG.

# Vocabulary

Canonical subjects and objects for typed landmarks:

- passenger of interest
- decisive seats
- first passenger's seat
- last passenger's seat
- displacement chain
- random chooser
- own-seat probability
- smaller plane
- last passenger's known half

# Why it is in the atlas

Altered-famous family. The famous version is strongly primed; the chain must depict the alteration
(second-to-last, three decisive seats) or a reader snaps to ½. The calculation route is a 100-step
recursion; the holistic route is one symmetry picture.

# Breadth

No routes yet.
