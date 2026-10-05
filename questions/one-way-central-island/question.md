---
id: one-way-central-island
title: All roads lead to the hub, but can anyone leave?
status: answered
added: 2026-10-05
family: directed connectivity
attractor: a common reachable hub connects everyone to everyone
---

# Question

A finite network of islands uses one-way bridges. There is a central island H that every island can reach by following the bridge directions. Does this guarantee that every island can reach every other island? Give a counterexample if not.

# Reference answer (referee only)

No. Take islands A, B, H with only the directed bridges A to H and B to H. Both outer islands reach H, and H reaches itself by staying put, but neither outer island can reach the other. Tolerance: exact no with a directed counterexample. A stronger condition that H also reaches every island would guarantee the result by concatenating paths through H.

# Why it is in the atlas

Adds direction-sensitive composition and distinguishes a common destination from mutual accessibility.

# Breadth

No played or accepted routes yet. The unjudged draft in curator.md is not part of the frontier.
