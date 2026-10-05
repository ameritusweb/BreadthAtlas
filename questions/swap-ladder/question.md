---
id: swap-ladder
title: The swap ladder
status: answered
added: 2026-10-05
image: ladder.png
key: answer_key.json
family: long state tracking
attractor: none (novel instance; generator provenance/generators/ex2_ladder.py)
---

# Question

Twelve tokens A–M (no I) start on rails 1–12. The forty-one rungs are applied from top to bottom; each
rung swaps whichever two tokens are on its two rails at that moment. After the last rung, **which token
is on rail 9, and how many tokens are back on the rail where they started?**

# Reference answer (referee only)

**Rail 9 holds L; ten tokens are home.** The rung pattern is mirror-symmetric about the middle row
(rungs 1–20 repeated in reverse as 22–41) with a single unpaired rung at row 21 on rails 10–11. The
mirrored halves cancel; the only lasting effect is that the two tokens reaching rails 10–11 at row 21
(L on rail 10, J on rail 11) exchange starting rails. Final order A B C D E F G H L K J M.
Tolerance: exact on both parts.

# Why it is in the atlas

State-tracking family. The calculation route is a 41-step simulation; the holistic route is seeing
the mirror and the lone rung. Trap: "it is symmetric, so everything returns."

# Breadth

No routes yet.
