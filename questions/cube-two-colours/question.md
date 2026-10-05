---
id: cube-two-colours
title: Two-colour cubes up to rotation
status: answered
added: 2026-10-05
family: counting under symmetry
attractor: none
guess_target: 10
guess_recall: likely   # 5/5 identical exact bare guesses on 2026-10-05: a known result, not an estimate
guess_scale: linear
guess_unit: number of distinct cubes
---

# Question

Each face of a cube is painted either black or white. Two painted cubes count as the same if one can be
rotated to look exactly like the other. **How many different painted cubes are there?**

# Reference answer (referee only)

**10.** By number of black faces: 0 → 1; 1 → 1; 2 → 2 (adjacent or opposite); 3 → 2 (three meeting at a
corner, or a band of three around the cube); 4 → 2 (the complements of the two-black cases); 5 → 1;
6 → 1. Total 10. Burnside's lemma gives the same (1/24)(64 + 6·8 + 3·16 + 8·4 + 6·8) = 10.
Tolerance: exact.

# Why it is in the atlas

Counting-under-symmetry family. The calculation route is Burnside bookkeeping over 24 rotations; the
holistic route is seeing the orbits directly (case by number of black faces, with the adjacent/opposite
and corner/band distinctions, and the complement symmetry that mirrors the count). Routes differ by
which symmetry they lean on.

# Breadth

No routes yet.
