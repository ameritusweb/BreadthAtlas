# Curator notes — unjudged candidate

This file contains solution hypotheses. It is not a played route, is not scored, and must not be supplied as player input.

## Candidate chain

1. 🗺️ (root) — The finite undirected island network is connected.
2. 🔁 (root) — Every bridge belongs to a loop with no repeated bridge or intermediate island.
3. 🔒 (root) — Exactly one bridge closes.
4. ❓ (← 1, 2, 3) — Can this closure disconnect the network?
5. 🌉 (← 2, 3) — The closed bridge belongs to a loop through its two endpoints.
6. ↪️ (← 3, 5) — The remainder of that loop still joins those endpoints using open bridges.
7. 🚶 (← 1) — Any chosen pair of islands had a connecting path before the closure.
8. 🔀 (← 6, 7) — If that path used the closed bridge, its crossing can be replaced by the open detour.
9. ✅ (← 3, 7) — If the path avoided the closed bridge, it remains available.
10. 🤝 (← 8, 9) — Every pair of islands remains connected after the closure.
LANDMARKS:
- The rest of a loop connects the closed bridge's endpoints.
- Any affected path can substitute that detour for the closed crossing.
ANSWER: No.

## Other conceptual spines to investigate

alternate-path substitution; contradiction through a supposed separating edge

## Boundary variant

Allow one bridge to belong to no loop; two otherwise connected groups joined only by it give a separating closure.
