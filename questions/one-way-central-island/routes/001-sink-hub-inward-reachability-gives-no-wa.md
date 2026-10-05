---
id: 001
question: one-way-central-island
title: Sink hub: inward reachability gives no way out
strategy: new: minimal-sink-counterexample
contributor: sonnet (blind player 1)
date: 2026-10-05
depth: 1
referee: opus/v2
criterion: v2
verdict: VALID
reason: The two-island network with one bridge from A to H meets the givens, since A reaches H and H reaches itself trivially. In that network H cannot reach A, so the answer "no" is correct, and the chain has no calculation or simulation. Its new landmarks are that reaching the hub says nothing about leaving it, that a sink hub satisfies the givens, and that the one-bridge A→H network is a minimal counterexample.
discriminator_depicted: yes
typed_1: structure | reaching the hub | leaving the hub | - | - | Reaching the hub is one-directional information: it says nothing about leaving the hub.
typed_2: construction | sink hub | the givens | ∈ | - | A hub with no outgoing bridges (a sink) satisfies the givens while being unable to reach anyone else.
typed_3: construction | two-island network with single bridge A→H | minimal counterexample | exists | - | The two-island network with a single bridge A→H is a minimal counterexample.
---

CHAIN by blind player 1
1. 🏝️➡️🏠 (root) — Given: every island can reach the hub H by following bridge directions.
2. 🌉☝️ (root) — Given: all bridges are one-way.
3. ❓ (← 1, 2) — Asked: must every island also be able to reach every other island? 🔁🏝️🏝️ is the "reach each other" property, and a counterexample is wanted if not.
4. 🧪 (← 3) — To answer "no," it is enough to build one small network satisfying the givens where some island cannot reach another.
5. 🏠🏝️ (← 4) — Take the smallest example: hub H plus one other island A, two islands in total.
6. 🌉A➡️H (← 2, 5) — Build a single one-way bridge from A to H and no other bridge.
7. ✅1 (← 1, 6) — The givens hold: A reaches H by the bridge, and H reaches itself by staying put.
8. 🚫H➡️A (← 6) — No bridge leaves H, so from H there is no move at all and H cannot get to A.
9. 💥? (← 7, 8) — Not a contradiction: this shows the "every island reaches every other" claim fails here, with the givens still true.
10. 👀 (← 6, 8) — Self-check: the only bridge points into H, so nothing can leave H; this confirms A is unreachable from H.
11. 🔄 (← 3, 9) — The guarantee would need a way back out of H, and the givens only say that roads lead in. Nothing about them forces a road out.
12. 🎯 (← 7, 8, 11) — Conclusion: the hub-reachability property does not guarantee mutual reachability, and the two-island network with one bridge A to H is a counterexample.

LANDMARKS:
- Reaching the hub is one-directional information: it says nothing about leaving the hub.
- A hub with no outgoing bridges (a sink) satisfies the givens while being unable to reach anyone else.
- The two-island network with a single bridge A→H is a minimal counterexample.

ANSWER: No. For example, with islands A and H and one one-way bridge from A to H, every island reaches H, but H cannot reach A.
