# Curator notes — unjudged candidate

This file contains solution hypotheses. It is not a played route, is not scored, and must not be supplied as player input.

## Candidate chain

1. 🗺️ (root) — The network is finite, connected, undirected, and has no loops or parallel bridges.
2. 🌉 (root) — Every island has at least two incident bridges.
3. ❓ (← 1, 2) — Must every single-bridge closure preserve connectivity?
4. 🔺 (← 1, 3) — Build a triangle of distinct islands connected around its perimeter.
5. 🔻 (← 1, 3) — Build a second triangle using different islands.
6. 🔗 (← 4, 5) — Join one vertex of the first triangle to one vertex of the second with a single bridge.
7. ✅ (← 4, 5, 6) — This network is connected and satisfies the required bridge count at every island.
8. ✂️ (← 6) — The joining bridge is the only crossing between the two triangles.
9. 🔒 (← 7, 8) — Closing it leaves the triangles disconnected despite every island's initial local redundancy.
10. 🚫 (← 3, 7, 9) — The stated local condition does not guarantee survival of every closure.
LANDMARKS:
- Two triangles joined by one bridge satisfy the local degree condition.
- Their sole inter-triangle crossing is nevertheless a separating bridge.
ANSWER: No; two triangles joined by a single bridge are a counterexample.

## Other conceptual spines to investigate

explicit counterexample; local versus global constraint

## Boundary variant

Strengthen the premise to every bridge lying on a loop; the answer becomes yes, as in bridges-on-loops.
