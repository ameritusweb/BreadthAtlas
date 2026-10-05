---
id: pair-toggle-lamps
title: Can paired switches leave one lamp on?
status: answered
added: 2026-10-05
family: invariants, reachability
attractor: enough switch operations can produce any lighting pattern
---

# Question

A panel has six lamps, all initially off. Each move chooses any two distinct lamps and toggles both: off becomes on and on becomes off. Can any sequence of moves leave exactly one lamp on?

# Reference answer (referee only)

No. Pair toggles preserve the parity of the number of lit lamps: two off lamps add a pair, two on lamps remove a pair, and a mixed pair merely transfers the lit state. Initially the lit count is even; a single lit lamp is odd. Tolerance: exact no with a sequence-independent obstruction.

# Why it is in the atlas

Transfers parity from walks to configuration reachability; no actual switching sequence needs tracing.

# Breadth

No played or accepted routes yet. The unjudged draft in curator.md is not part of the frontier.
