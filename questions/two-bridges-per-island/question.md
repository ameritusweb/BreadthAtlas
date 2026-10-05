---
id: two-bridges-per-island
title: Does local redundancy guarantee global redundancy?
status: answered
added: 2026-10-05
family: connectivity, counterexample
attractor: at least two bridges per island means no single point of failure
---

# Question

A finite connected undirected network has at least two distinct bridges incident to every island. No bridge joins an island to itself, and there are no parallel bridges. Must the network remain connected after any single bridge closes? Give a concrete counterexample if the answer is no.

# Reference answer (referee only)

No. Use two disjoint triangles, joined by one additional bridge between a vertex of each triangle. Each island has at least two incident bridges; the joining vertices have three. Closing the joining bridge separates the triangles. Tolerance: exact no with a counterexample satisfying every condition.

# Why it is in the atlas

Tests the difference between local degree and a global cut; pairs with bridges-on-loops.

# Breadth

No played or accepted routes yet. The unjudged draft in curator.md is not part of the frontier.
