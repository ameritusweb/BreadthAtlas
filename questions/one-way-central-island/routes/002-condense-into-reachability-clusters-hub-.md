---
id: 002
question: one-way-central-island
title: Condense into reachability clusters; hub's cluster is sink
strategy: new: condensation-sink-component
contributor: sonnet (blind player 2)
date: 2026-10-05
depth: 2
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain has no simulation and every step is sound. Step 12 is the chain's stated conclusion, so it does work. Its new landmarks are not among route 001's three. First, the islands split into mutual-reachability clusters whose condensation has no loops. Second, H's cluster is forced to be the dead end of that picture. Third, the guarantee holds exactly when H's cluster is the whole network.
discriminator_depicted: yes
typed_1: structure | mutual-reachability clusters | bridges between clusters | forbids | - | Islands split into clusters of mutual reachability, and the bridges between clusters never form a loop.
typed_2: structure | H's cluster | leaving the hub | forbids | - | If everyone reaches H, H's cluster is the dead end of the cluster picture, with no bridge leaving it.
typed_3: reduction | the guarantee | H's cluster is the whole network | reduces-to | - | The guarantee holds exactly when H's cluster is the whole network. A three-island inward star (A→H, B→H) fails this and also leaves A and B unable to reach each other.
---

CHAIN by blind player 2
1. 🏝️ (root) — Given: a finite set of islands joined by one-way bridges.
2. 🎯 (root) — Given: every island can reach the central island H by following bridge directions.
3. ❓ (← 1, 2) — Asked: does "all reach H" force "every island reaches every other" (🔁↔️ for every pair, not just 🎯 toward H)? If not, give a counterexample.
4. 🔄 (← 1, 3) — "Everyone reaches everyone" means mutual reachability, so islands that can reach each other form natural clusters.
5. 🧩 (← 4) — Every island belongs to exactly one cluster of mutual reachability, so the islands split cleanly into clusters.
6. ⬇️ (← 5) — Collapse each cluster to a single point. The bridges left between clusters can never form a loop, because a loop would merge those clusters into one.
7. 🕳️ (← 2, 6) — Every cluster must lead into H's cluster. If H's cluster had a bridge out to another cluster, that cluster would also be reachable from H, so the two would merge. So H's cluster is the dead end of the collapsed picture.
8. 🚪 (← 7) — The guarantee therefore holds only if H's cluster contains all the islands. Any island outside it is an entrant that can get in but never back out.
9. 🌟 (← 1, 8) — Build a concrete case: islands A, B and H, with bridges A→H and B→H only. A and B are outsiders to H's cluster.
10. ✅ (← 2, 9) — Check the given: A reaches H directly, B reaches H directly, and H trivially reaches itself, so everyone reaches H.
11. 🚫 (← 9) — No bridge leaves H, so H cannot reach A or B. A also cannot reach B, because A's only bridge ends at H, which is a dead end.
12. ⚖️ (← 3, 8, 10, 11) — The givens hold but mutual reachability fails, so the guarantee is false.
13. 👀 (← 10) — Self-check: the network is finite, the bridges are one-way, and every island reaches H, so the counterexample respects all the givens.

LANDMARKS:
- Islands split into clusters of mutual reachability, and the bridges between clusters never form a loop.
- If everyone reaches H, H's cluster is the dead end of the cluster picture, with no bridge leaving it.
- The guarantee holds exactly when H's cluster is the whole network. A three-island inward star (A→H, B→H) fails this and also leaves A and B unable to reach each other.

ANSWER: No. All islands reaching H does not make every island reach every other. Counterexample: islands A, B and H with bridges A→H and B→H only. Everyone reaches H, but H cannot reach A or B, and A cannot reach B.
