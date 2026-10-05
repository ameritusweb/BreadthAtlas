---
id: cube-three-colours
title: Three-colour cubes up to rotation
status: answered
added: 2026-10-05
family: counting under symmetry (parametrized sibling of cube-two-colours)
attractor: the two-colour case (10)
discriminator: THREE colours, not two; the two-colour count appears only as a sub-case
guess_target: 57
guess_recall: likely   # 5/5 identical exact bare guesses on 2026-10-05: a known result, not an estimate
guess_scale: log
guess_unit: number of distinct cubes
---

# Question

Each face of a cube is painted one of three colours. Two painted cubes count as the same if one can be
rotated to look exactly like the other. **How many different painted cubes are there?**

# Reference answer (referee only)

**57.** Burnside over the 24 rotations: (3⁶ + 6·3³ + 3·3⁴ + 8·3² + 6·3³)/24 = (729 + 162 + 243 + 72 +
162)/24 = 1368/24 = 57. A perceptual route must organize the count by colour multiset or by face-pair
structure; the two-colour answer 10 appears as a sub-case (any two of the three colours) and chains
that stop at 3·10 − 3 = 27 or similar have missed the three-colour configurations. Tolerance: exact.

# Why it is in the atlas

Parametrized sibling of `cube-two-colours`: the same strategies apply but every count must be
re-derived, and the case list is long enough that the "see the orbits" route is genuinely harder than
the two-colour case.

# Breadth

No routes yet.
