---
id: swap-ladder-b
title: The swap ladder, second instance
status: answered
added: 2026-10-05
image: ladder.png
key: answer_key.json
family: long state tracking (parametrized sibling of swap-ladder, seed 23)
attractor: none
---

# Question

Twelve tokens A–M (no I) start on rails 1–12. The forty-one rungs are applied from top to bottom; each
rung swaps whichever two tokens are on its two rails at that moment. After the last rung, **which token
is on rail 3, and how many tokens are back on the rail where they started?**

# Reference answer (referee only)

**Rail 3 holds D; ten tokens are home.** Same structure as `swap-ladder`: rungs 1–20 mirrored as 22–41
with a single unpaired rung at row 21, here on rails 1–2. The two tokens reaching rails 1–2 at row 21
(C and D) exchange starting rails. Final order A B D C E F G H J K L M. Tolerance: exact on both parts.

# Why it is in the atlas

The first parametrized sibling. A route found on `swap-ladder` (mirror cancellation, or block
decomposition with tracing) must be re-derived here, not recalled; a player that recites the first
instance's answer gets this one wrong.

# Breadth

No routes yet.
