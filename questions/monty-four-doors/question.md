---
id: monty-four-doors
title: Monty Hall with four doors
status: answered
added: 2026-10-05
family: altered famous puzzle
attractor: three-door Monty Hall (switching wins 2/3)
discriminator: FOUR doors and ONE opened; two closed doors remain to switch to, sharing the unpicked group's probability
guess_target: 0.375
guess_recall: likely   # 5/5 identical exact bare guesses on 2026-10-05: a known result, not an estimate
guess_scale: linear
guess_unit: a probability between 0 and 1
---

# Question

Four doors hide one car and three goats. You pick a door. The host, who knows where the car is, opens
one of the other three doors to reveal a goat, and offers you the chance to switch to one of the two
remaining closed doors. **If you switch, what is the probability that you win the car?**

# Reference answer (referee only)

**3/8.** Your first pick holds the car with probability 1/4; the other three doors share 3/4. The host
removes one goat from those three, leaving two closed doors that still share the 3/4 between them, so
each has probability 3/8. Switching (to either one) wins with probability 3/8, against 1/4 for staying.
Tolerance: the exact fraction or a decimal within 0.02. The famous 2/3 is WRONG.

# Why it is in the atlas

Altered-famous family. The structure of the classic argument survives (the host's action concentrates
probability on unopened doors) but the number does not; a chain must depict four doors and one opened,
not three and one, or the reader snaps to 2/3.

# Breadth

No routes yet.
