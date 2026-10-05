---
id: necklace-six-beads
title: Six-bead necklaces in two colours
status: answered
added: 2026-10-05
family: counting under symmetry
attractor: none
guess_target: 13
guess_recall: likely   # 5/5 identical exact bare guesses on 2026-10-05: a known result, not an estimate
guess_scale: linear
guess_unit: number of distinct necklaces
---

# Question

A necklace has six beads, each black or white. Two necklaces count as the same if one can be turned
around the ring, or flipped over, to look like the other. **How many different necklaces are there?**

# Reference answer (referee only)

**13.** By number of black beads: 0 → 1; 1 → 1; 2 → 3 (adjacent, one apart, opposite); 3 → 3 (three
together, two-and-one, alternating); 4 → 3 (complements of the two-black cases); 5 → 1; 6 → 1.
Total 13. (Bracelets, n = 6, two colours.) Tolerance: exact. Note: without flips (rotation only) the
answer is 14 — the two three-black "two-and-one" chiral forms become distinct; a chain answering 14 has
dropped the flip and is WRONG.

# Why it is in the atlas

Counting-under-symmetry family; the flip is the trap (13 vs 14). Routes differ by which symmetry
organizes the count: by black count with complement mirroring; by gap pattern; by orbit of a chosen
bead; by Burnside-style averaging done perceptually.

# Breadth

No routes yet.
