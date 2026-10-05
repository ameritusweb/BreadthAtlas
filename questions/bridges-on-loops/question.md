---
id: bridges-on-loops
title: Can a bridge on a loop be indispensable?
status: answered
added: 2026-10-05
family: connectivity, failure tolerance
attractor: removing a bridge always breaks a connection
---

# Question

A finite connected network of islands has undirected bridges. Every bridge lies on at least one loop that returns to its starting island without repeating a bridge or an intermediate island. Exactly one bridge closes. Can the remaining network become disconnected?

# Reference answer (referee only)

No. For the closed bridge's endpoints, the rest of its loop supplies an alternative path. Replace any use of the closed bridge in an original path with that alternative. All originally connected islands remain connected. Tolerance: exact yes/no with a general argument, not one example.

# Why it is in the atlas

Introduces alternate-path substitution and contrasts local edge loss with global reachability.

# Breadth

No played or accepted routes yet. The unjudged draft in curator.md is not part of the frontier.
