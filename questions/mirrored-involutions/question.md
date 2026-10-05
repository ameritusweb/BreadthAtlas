---
id: mirrored-involutions
title: Do unfamiliar reversible actions cancel in a mirror?
status: answered
added: 2026-10-05
family: reversibility, composition
attractor: actions must commute for a sequence to cancel
---

# Question

A device has actions A, B, and C. Each is always legal, deterministic, and applying the same action twice consecutively restores the state it acted on. They need not commute. Starting from any state, perform A, then B, then C, then C, then B, then A. Must the final state equal the starting state?

# Reference answer (referee only)

Yes. The adjacent C actions cancel. The now adjacent B actions cancel, then the A actions cancel. No commutation is used; each pair acts on the same intervening state and restores it. Tolerance: exact yes with a general structural argument, not a simulated device state.

# Why it is in the atlas

Transfers mirror cancellation beyond a token ladder and isolates self-inverse actions from merely reversible actions.

# Breadth

No played or accepted routes yet. The unjudged draft in curator.md is not part of the frontier.
