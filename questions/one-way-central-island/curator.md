# Curator notes — unjudged candidate

This file contains solution hypotheses. It is not a played route, is not scored, and must not be supplied as player input.

## Candidate chain

1. ➡️ (root) — Bridges may be traversed only in their marked direction.
2. 🎯 (root) — Every island can reach the central island H.
3. ❓ (← 1, 2) — Does this ensure that every island can reach every other island?
4. 🏝️ (← 1, 3) — Consider distinct islands A, B, and H.
5. ↘️ (← 1, 4) — Give A a bridge to H and B a bridge to H, with no other bridges.
6. ✅ (← 2, 5) — Every island can reach H in this network, with H already at the destination.
7. 🛑 (← 5) — H has no outgoing bridge.
8. 🚶 (← 5, 7) — A traveller leaving A can only reach H and then stop.
9. 🚫 (← 4, 8) — That traveller cannot reach B.
10. ⚠️ (← 3, 6, 9) — A common reachable destination does not establish mutual reachability.
LANDMARKS:
- A directed hub can be reachable from every island while having no outgoing bridge.
- Arrival at a common destination supplies no path out to another island.
ANSWER: No.

## Other conceptual spines to investigate

directed counterexample; obstruction by a sink

## Boundary variant

Also require H to reach every island; a path into H followed by a path out reaches any destination.
