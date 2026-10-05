---
id: tetrahedron-three-colours
title: Three-colour tetrahedra up to rotation
status: answered
added: 2026-10-05
family: counting under symmetry
attractor: none
guess_target: 15
guess_recall: likely   # 5/5 identical exact bare guesses on 2026-10-05: a known result, not an estimate
guess_scale: linear
guess_unit: number of distinct tetrahedra
---

# Question

Each of the four faces of a regular tetrahedron is painted one of three colours. Two painted
tetrahedra count as the same if one can be rotated to look like the other (no reflections).
**How many different painted tetrahedra are there?**

# Reference answer (referee only)

**15.** By colour multiset: all four one colour — 3; three of one colour and one of another — 6;
two and two — 3; two of one colour and one each of the other two — 3 (the two singletons are
interchangeable by a rotation about the axis through the doubled pair's shared edge midpoint, so each
choice of the doubled colour gives one tetrahedron). Total 3 + 6 + 3 + 3 = 15. Burnside: (81 + 8·9 +
3·9)/12 = 15. Tolerance: exact. A chain that counts the two-one-one case as 6 has missed the rotation
and gets 18 — WRONG.

# Why it is in the atlas

Counting-under-symmetry family. The subtle case (two-one-one) is where routes differ: by the axis
through an edge, by fixing the doubled pair, by complement to the four-distinct-colour case that
cannot occur with three colours.

# Breadth

No routes yet.
