---
id: 003
question: two-bridges-per-island
title: Squeeze robust clusters to a point; the skeleton is a tree
strategy: new: contract-to-cluster-tree
contributor: sonnet (extender)
date: 2026-10-05
depth: 3
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is sound: three triangles joined in a row are a simple, connected network with at least two bridges per island, and either linking bridge disconnects it. Nothing in it is a step-by-step simulation, and step 12 states the conclusion, so it does work. It introduces new landmarks 1 and 2. Landmark 1 squeezes each robust cluster to a point and notes that the at-least-two condition puts no limit on the skeleton, which can be a tree. Landmark 2 says every link of a tree skeleton is a cut bridge. Neither route 001 nor route 002 went through a cluster skeleton or a tree argument.
discriminator_depicted: no
typed_1: reduction | network | skeleton of clusters | reduces-to | - | Squeezing each internally robust cluster to a single point turns the network into a skeleton of clusters. The at-least-two condition says nothing about that skeleton, which can be a tree.
typed_2: obstruction | tree skeleton link | network connectivity after one closure | forbids | - | A tree skeleton with at least two clusters has every link as a sole connection, so each such link is a bridge whose closure disconnects the network.
typed_3: construction | three triangles joined in a row | minimum degree two at every island | exists | - | The counterexample is a chain of three triangles joined in a row by two linking bridges. Both linking bridges are cut bridges.
---

CHAIN by extender
1. 🏝️ (root) — Given: the network is finite, connected and undirected, with no self-bridges and no parallel bridges.
2. 🌉🌉 (root) — Given: every island has at least two bridges touching it.
3. ❓ (← 1, 2) — Asked: must the network stay connected after any single bridge closes, and if not, what is a concrete counterexample?
4. 🔺 (← 1, 2) — A triangle is a small cluster that is robust inside. Every island in it has two bridges, and there are no loops or parallels.
5. 🔺🔺🔺 (← 4) — Take three separate triangles, called left, middle and right. Each cluster is robust inside itself.
6. 🗜️ (← 5) — Imagine squeezing each triangle into a single dot. The network becomes three dots, and only the bridges between triangles are left.
7. 🔗🔗 (← 6) — Link left to middle with one bridge and middle to right with one bridge. The squeezed picture is a path of three dots, which is a tree with no cycle.
8. ✅ (← 2, 5, 7) — The real network is connected and simple. Every island has two bridges, and the three linked corners have three. All the givens hold.
9. 🌳 (← 7) — In a tree, every link is the only route between its two sides. So each of the two linking bridges is the sole connection between the clusters it joins.
10. ✂️ (← 8, 9) — Close the bridge between the left and middle triangles.
11. 💔 (← 9, 10) — Nothing else connects the left triangle to the others, so the network falls apart into two pieces.
12. 🚫 (← 3, 8, 11) — A network meeting every given became disconnected after one closure, so the answer is no.
13. 👀 (← 11) — Self-check: closing a bridge inside a triangle leaves the other two sides, so only the two linking bridges are weak points. That matches the tree picture.

LANDMARKS:
- Squeezing each internally robust cluster to a single point turns the network into a skeleton of clusters. The at-least-two condition says nothing about that skeleton, which can be a tree.
- A tree skeleton with at least two clusters has every link as a sole connection, so each such link is a bridge whose closure disconnects the network.
- The counterexample is a chain of three triangles joined in a row by two linking bridges. Both linking bridges are cut bridges.

ANSWER: No. Take three disjoint triangles in a row, with one bridge from the left triangle to the middle one and one from the middle triangle to the right one. Every island has at least two bridges, but closing either linking bridge disconnects the network.
