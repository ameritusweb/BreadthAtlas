---
id: 003
question: one-way-central-island
title: One-way line: source unreachable, sink hub cannot exit
strategy: new: source-and-sink-obstruction
contributor: sonnet (extender)
date: 2026-10-05
depth: 3
referee: opus/v2
criterion: v2
verdict: VALID
reason: The one-way line A→B→H is a correct counterexample. Its step-by-step reasoning is structural, so it does not count as simulation. It adds a new landmark: a source island with no incoming bridge can never be reached by anyone, which is an obstruction separate from the sink hub of route 001 and the cluster dead end of route 002.
discriminator_depicted: yes
typed_1: construction | one-way line A→B→H | the givens | ∈ | - | Reachability is transitive, so a one-way line A→B→H lets everyone reach H while the order of the line can never be reversed.
typed_2: obstruction | source island with no incoming bridge | being reached by other islands | forbids | - | The start of the line is a source with no incoming bridge, so no other island can reach it. This is a second obstruction besides H having no exit.
typed_3: structure | reaching the hub | incoming bridges to other islands | - | - | The hub condition constrains only the routes into H. It places no demand on incoming bridges for the other islands.
---

CHAIN by extender
1. 🏝️🌉☝️ (root) — Given: a finite set of islands joined only by one-way bridges.
2. 🏠👈🏝️ (root) — Given: every island can reach the central island H by following bridge directions.
3. ❓ (← 1, 2) — Asked: does "everyone reaches H" (🏝️➡️🏠) force "everyone reaches everyone" (🔁🏝️🏝️ for every pair)? If not, give a counterexample.
4. 🧱 (← 1) — Reachability chains together: if X reaches Y and Y reaches Z, then X reaches Z by following the two routes in turn.
5. 🚂 (← 1, 4) — Build a one-way line of three islands: bridge A→B and bridge B→H, and nothing else.
6. ✅ (← 2, 4, 5) — The givens hold: B reaches H directly, A reaches H through B, and H reaches itself.
7. 🌱 (← 5) — A is a pure starting point: no bridge points into A.
8. 🚫 (← 7) — Since no bridge enters A, no other island can ever reach A, so B and H cannot get back to A.
9. 🏁 (← 5) — H is a pure end point: no bridge leaves H, so H cannot reach A or B.
10. 🔒 (← 4, 8, 9) — Travel on the line only goes forward, so every backward pair (B to A, H to B, H to A) is unreachable.
11. 👀 (← 6) — Self-check: the network is finite, the bridges are one-way, and all three islands reach H, so the example respects the givens.
12. 🎯 (← 3, 6, 8, 10) — The givens hold but mutual reachability fails, so the guarantee is false.

LANDMARKS:
- Reachability is transitive, so a one-way line A→B→H lets everyone reach H while the order of the line can never be reversed.
- The start of the line is a source with no incoming bridge, so no other island can reach it. This is a second obstruction besides H having no exit.
- The hub condition constrains only the routes into H. It places no demand on incoming bridges for the other islands.

ANSWER: No. Counterexample: three islands A, B, H with bridges A→B and B→H only. Everyone reaches H, but H cannot reach B or A, and B cannot reach A.
