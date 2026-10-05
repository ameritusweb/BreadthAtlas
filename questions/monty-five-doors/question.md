---
id: monty-five-doors
title: Monty Hall with five doors
status: answered
added: 2026-10-05
family: altered famous puzzle (parametrized sibling of monty-four-doors)
attractor: three-door Monty Hall (2/3); the four-door sibling (3/8)
discriminator: FIVE doors and ONE opened; three closed doors remain to switch to
guess_target: 0.2667
guess_scale: linear
guess_unit: a probability between 0 and 1
---

# Question

Five doors hide one car and four goats. You pick a door. The host, who knows where the car is, opens
one of the other four doors to reveal a goat, and offers you the chance to switch to one of the three
remaining closed doors. **If you switch, what is the probability that you win the car?**

# Reference answer (referee only)

**4/15.** Your pick holds the car with probability 1/5; the other four doors share 4/5; the host
removes one goat, leaving three closed doors that still share 4/5, so each has 4/15 ≈ 0.267. Switching
wins with 4/15 against 1/5 for staying. Tolerance: the exact fraction or a decimal within 0.02.
2/3 and 3/8 are WRONG.

# Why it is in the atlas

Second parametrized sibling in the Monty family. The share-splitting and likelihood-weighting routes
from `monty-four-doors` transfer; the numbers do not.

# Breadth

No routes yet.
