---
id: 001
question: cyclic-task-prerequisites
title: Transitive precedence around the loop forces self-precedence
strategy: new: cycle-transitivity-self-precedence
contributor: sonnet (extender)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: DUPLICATE
reason: Chain 3 follows the precedences around the loop until a task has to come before itself. Route 002 already reached that through landmarks 4 and 6: each finish is strictly later than its prerequisite's finish, so going round the loop gives a finish earlier than itself. Using A's start and finish as the reference points, instead of finish against finish, measures the same loop differently but is the same route.
discriminator_depicted: no
typed_1: reduction | the cycle of strict prerequisites | a task needing its own completion first | reduces-to | - | Composing the prerequisites around the loop collapses them into one task that must finish before it can start.
typed_2: obstruction | a task's start | a task's finish | forbids | - | A task's start would have to come after its own finish, while positive duration puts its finish after its start.
---

CHAIN by extender
1. 🅰️ (root) — Task A can start only after B has finished.
2. 🅱️ (root) — Task B can start only after C has finished.
3. 🅒 (root) — Task C can start only after A has finished.
4. ⏳ (root) — Every task takes a positive duration between its start and its finish, and no prerequisite can be waived.
5. ❓ (← 1, 2, 3, 4) — Asked: can any schedule finish all three tasks of this three-task loop?
6. 🔗 (← 1, 2, 4, 5) — Suppose all three finish. Chaining the first two rules, A's start comes after B's finish, which comes after B's start, which comes after C's finish. So A cannot start until C has finished, and the middle task drops out.
7. 🔁 (← 3, 4, 6) — Chaining once more, C's finish comes after C's start, which comes after A's finish. So A cannot start until after A itself has finished, and the loop collapses into a single task needing its own completion first.
8. 🕰️ (← 4) — Independently, A's finish comes strictly after A's start, because finishing takes positive time.
9. 💥 (← 7, 8) — A's start would be after A's finish, while A's finish is after A's start. Both cannot hold.
10. 🚫 (← 9) — So the supposition that all three finish fails, and no schedule finishes all three.
11. 👀 (← 10) — Self-check: rotating the names A, B, C gives the same collapse for B and C, so nothing depended on the choice of A.

LANDMARKS:
- Composing the prerequisites around the loop collapses them into one task that must finish before it can start.
- A task's start would have to come after its own finish, while positive duration puts its finish after its start.

ANSWER: No, no schedule can finish all three tasks.
