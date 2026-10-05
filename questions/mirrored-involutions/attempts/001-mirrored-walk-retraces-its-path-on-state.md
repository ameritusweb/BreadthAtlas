---
id: 001
question: mirrored-involutions
title: Mirrored walk retraces its path on state graph
strategy: new: path-retracing-on-state-graph
contributor: sonnet (extender)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: DUPLICATE
reason: The chain restates routes 001 and 002 in state-graph language. Steps 8–10 cancel the pairs one by one from the inside out, which is route 001's landmarks 1–2 (the innermost C,C pair cancels on the state between them, then the next pair is exposed). "Retraces the same path in reverse" is route 002's landmark 4 (C,B,A undoes A,B,C). "Two-way link" is route 002's landmark 5 (each action is its own undo). Swapping the picture from sequence cancellation to dots and arrows changes how the argument is presented, not the route. The steps are sound. The walk uses abstract placeholder states rather than concrete device snapshots, so it is not simulation.
discriminator_depicted: no
typed_1: structure | each action | a two-way link between states | = | - | Each action is a two-way link between states, because the self-undo given makes every arrow reversible.
typed_2: symmetry | the second half C,B,A | the inverse of the forward trip A,B,C | = | - | The full sequence is a walk that goes out along a path and then retraces the same path in reverse.
typed_3: reduction | the mirrored sequence | the empty sequence | reduces-to | - | Determinism forces each return hop to land on the state just left, so the walk cannot branch away from the retraced path.
---

CHAIN by extender
1. 🔁 (root) — Given: applying the same action twice in a row restores the state it acted on.
2. 🎲 (root) — Given: each action is always legal and deterministic, so from any state it leads to exactly one result.
3. 🔤 (root) — Given: the sequence performed is A, B, C, C, B, A, and the actions need not commute.
4. ❓ (← 1, 2, 3) — Asked: after A, B, C and then the mirrored C, B, A, must the final state equal the starting state, with the actions unfamiliar and not assumed to commute?
5. 🕸️ (← 2) — Picture states as dots, and each action as an arrow from every dot to its single result dot.
6. ↔️ (← 1, 5) — If action X sends dot s to dot t, then X applied to t gives s by the self-undo given, so every arrow also works backward and each action is a two-way link.
7. 🚶 (← 3, 5) — The sequence is a walk on these dots: start at s, hop by A to s1, by B to s2, by C to s3, then hop by C, then B, then A.
8. 🔙 (← 2, 6, 7) — At s3 the next hop is C, which is the same two-way link just used to arrive, and determinism means it has only one result, so it lands back on s2.
9. ⏪ (← 6, 8) — At s2 the hop is B, the link used to reach s2 from s1, so it returns to s1.
10. 🏠 (← 6, 9) — At s1 the hop is A, the link used to leave s, so it returns to s.
11. 🚫🔀 (← 3, 8) — Non-commutation never matters, because each return hop reuses the exact link just walked and nothing is swapped or reordered.
12. ✅ (← 4, 10, 11) — The walk retraces its own path back to the start, so the final state equals the starting state, for any start.
13. 👀 (← 12) — Self-check: a non-mirrored order like A, B, A, B would not retrace the path, so the mirror order is what makes the walk return.

LANDMARKS:
- Each action is a two-way link between states, because the self-undo given makes every arrow reversible.
- The full sequence is a walk that goes out along a path and then retraces the same path in reverse.
- Determinism forces each return hop to land on the state just left, so the walk cannot branch away from the retraced path.

ANSWER: Yes
