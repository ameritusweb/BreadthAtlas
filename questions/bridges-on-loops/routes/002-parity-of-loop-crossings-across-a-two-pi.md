---
id: 002
question: bridges-on-loops
title: Parity of loop crossings across a two-piece cut
strategy: new: cut-parity-contradiction
contributor: sonnet (blind player 2)
date: 2026-10-05
depth: 2
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is sound and uses no calculation or step-by-step simulation. Steps 5–10 prove the result by contradiction: the remainder has at most two pieces, the closed bridge is the only link between them, and the loop through it would have to cross between the pieces an even number of times but crosses only once. The "at most two pieces" split and the parity-crossing contradiction are new landmarks that do not appear in route 001's detour-and-reroute set.
typed_1: structure | the network after closing the bridge | at most two pieces, separating the closed bridge's endpoints | reduces-to | - | Removing one bridge can leave at most two pieces, with the bridge's two ends in different pieces.
typed_2: structure | the closed bridge | the only link between the two pieces | = | - | If the network split, the closed bridge would be the only link between the two pieces.
typed_3: obstruction | the loop through the closed bridge | crossing between two pieces an odd number of times | forbids | - | A closed loop must cross between two pieces an even number of times, but this loop would cross exactly once, which is a parity contradiction.
---

CHAIN by blind player 2
1. 🏝️🌉 (root) — The network is finite and connected, with undirected bridges between islands.
2. 🔁 (root) — Every bridge lies on a loop that returns to its start without repeating a bridge or an intermediate island.
3. ❓ (← 1, 2) — The question: if exactly one bridge is closed, can the rest become disconnected?
4. 1️⃣🚧 (root) — Exactly one bridge, b, closes, and its two ends are the islands u and v.
5. 🧩 (← 1, 4) — Suppose the rest is disconnected. Every island was connected to u or v through the original network, so what remains has exactly two pieces, one holding u and the other holding v.
6. ⚔️ (← 5) — Since the pieces were joined originally, b is the only bridge between the two pieces.
7. 🔄 (← 2, 4) — b lies on a loop, and that loop starts and ends on one island, so it begins and ends in the same piece.
8. 🚪 (← 6, 7) — A closed loop that starts and ends in the same piece crosses between the pieces an even number of times.
9. ☝️ (← 4, 6, 7) — The loop uses b, the only crossing, and never repeats a bridge, so it crosses exactly once, which is an odd number of times.
10. 💥 (← 8, 9) — Even and odd crossings contradict each other, so the supposed split is impossible.
11. 🛡️ (← 5, 10) — The remaining network therefore cannot split into two pieces, so it stays connected.
12. ✅ (← 3, 11) — The answer to the question is no.

LANDMARKS:
- Removing one bridge can leave at most two pieces, with the bridge's two ends in different pieces.
- If the network split, the closed bridge would be the only link between the two pieces.
- A closed loop must cross between two pieces an even number of times, but this loop would cross exactly once, which is a parity contradiction.

ANSWER: No. The remaining network always stays connected.
