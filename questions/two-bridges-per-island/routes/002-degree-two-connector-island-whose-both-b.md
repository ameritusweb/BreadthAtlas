---
id: 002
question: two-bridges-per-island
title: Degree-two connector island whose both bridges are cut bridges
strategy: new: degree-two-cut-vertex-counterexample
contributor: sonnet (blind player 2)
date: 2026-10-05
depth: 2
referee: opus/v2
criterion: v2
verdict: VALID
reason: The counterexample is correct and simple, and no step is a state snapshot. It adds two landmarks that route 001 lacks: an island with exactly two bridges can have both of them be cut bridges (each is the sole link to one side), and the degree condition cannot force a bridge to lie on a cycle. Route 001 used a single direct link between two cycles instead.
typed_1: construction | connector island with exactly two bridges | minimum degree two at every island | exists | - | A connector island with exactly two bridges, one into each of two separate squares, satisfies the at-least-two condition while each of its bridges is the sole link to one side.
typed_2: obstruction | connector island's bridges | network connectivity after one closure | forbids | - | Closing either bridge at the connector island leaves a whole square cut off.
typed_3: structure | minimum degree two at every island | connector island's bridges lying on a cycle | forbids | - | Each square is internally robust, but nothing makes the connector's bridges lie on a cycle.
---

CHAIN by blind player 2
1. 🏝️ (root) — Given: the network is finite, connected, undirected, with no self-bridges and no parallel bridges.
2. 🌉 (root) — Given: every island has at least two bridges touching it.
3. ❓ (← 1, 2) — Asked: must the network stay connected after any single bridge closes, and if not, what is a concrete counterexample?
4. 🔲 (← 1, 2) — Build a left square of four islands joined in a ring; each island has two bridges, with no loops or parallels.
5. 🔳 (← 4) — Build a second, separate right square in the same way.
6. 🧍 (← 2) — Add one middle island M with exactly two bridges: one to a corner of the left square and one to a corner of the right square.
7. 🔗 (← 4, 5, 6) — The combined network is connected and simple, and every island has at least two bridges (M and the plain square islands have two, the two joined corners have three).
8. ✂️ (← 6, 7) — Close the bridge between M and the left square's corner.
9. 🧱 (← 4, 8) — That bridge was the only link between the left square and everything else, so the left square is now cut off from M and the right square.
10. ⛔ (← 3, 7, 9) — A network meeting the premises became disconnected after one closure, so the answer is no.
11. 👀 (← 10) — Self-check: the squares and the two M bridges contain no loops or parallel bridges, and the closed bridge really was the only crossing, so the counterexample holds.

LANDMARKS:
- A connector island with exactly two bridges, one into each of two separate squares, satisfies the at-least-two condition while each of its bridges is the sole link to one side.
- Closing either bridge at the connector island leaves a whole square cut off.
- Each square is internally robust, but nothing makes the connector's bridges lie on a cycle.

ANSWER: No. Take two disjoint four-island squares and a middle island joined by one bridge to a corner of each square. Every island has at least two bridges, but closing the bridge between the middle island and the left square disconnects the network.
