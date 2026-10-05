---
id: 001
question: bridges-on-loops
title: Loop remainder detours around the closed bridge
strategy: new: splice-detour-reroute
contributor: sonnet (blind player 1)
date: 2026-10-05
depth: 1
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is sound and well-formed. Dropping the closed bridge from its loop leaves a detour between the bridge's endpoints (step 6). Splicing that detour into any route that used the bridge keeps every pair of islands connected (steps 8–9). The frontier was empty, so all three landmarks are new: the loop gives a detour, routes can be rerouted along it, and a bridge on a loop is not a cut bridge.
typed_1: construction | the loop through the closed bridge | a detour path between the closed bridge's endpoints | exists | - | Each loop through the closed bridge gives a detour path between its two endpoints.
typed_2: reduction | any route using the closed bridge | a route avoiding the closed bridge | reduces-to | - | Any route using the closed bridge can be rerouted along that detour.
typed_3: obstruction | a bridge on a loop | being a cut bridge | forbids | - | A bridge that lies on a loop is never a cut bridge, so connectivity survives its removal.
---

CHAIN by blind player 1
1. 🏝️ (root) — The network is finite and connected: every island can be reached from every other.
2. 🔁 (root) — Every bridge lies on a loop that returns to its start without repeating a bridge or an intermediate island.
3. ❓ (← 1, 2) — Exactly one bridge closes; can the remaining network become disconnected?
4. 🌉 (← 3) — Pick any bridge and call its endpoints A and B; this is the bridge that closes.
5. 🔄 (← 2, 4) — The picked bridge lies on a loop, so that loop leaves A over the bridge and comes back to A through B.
6. 🛤️ (← 5) — Dropping the closed bridge from the loop leaves a path from A to B that never uses the closed bridge.
7. 🧭 (← 1) — Any route between two islands in the original network is a sequence of bridges, and it may or may not use the closed bridge.
8. 🩹 (← 6, 7) — If a route uses the closed bridge, replace that one bridge with the A-to-B path; the route now avoids the closed bridge and still joins the same two islands.
9. 🔗 (← 8) — So every pair of islands is still joined by a route after the closure.
10. 🟢 (← 9) — The remaining network is still connected.
11. 👀 (← 10) — Self-check: a bridge with no alternate A-to-B path would not lie on any loop, which contradicts the given, so the closing bridge cannot be indispensable.
12. 🚫 (← 3, 10) — The answer to the question is no: the network cannot become disconnected.

LANDMARKS:
- Each loop through the closed bridge gives a detour path between its two endpoints.
- Any route using the closed bridge can be rerouted along that detour.
- A bridge that lies on a loop is never a cut bridge, so connectivity survives its removal.

ANSWER: No, the remaining network cannot become disconnected.
