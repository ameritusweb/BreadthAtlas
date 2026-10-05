---
id: 001
question: pair-toggle-lamps
title: Parity of lit count invariant under pair toggles
strategy: new: parity-invariant-obstruction
contributor: sonnet (blind player 1)
date: 2026-10-05
depth: 1
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is sound and contains no simulation: it reasons from a structural invariant (lit-count parity) and never tracks the board state. It is the first accepted chain on an empty frontier, so all three of its landmarks are new: changes in steps of plus two, minus two or zero; parity is invariant; and an even start cannot reach an odd target.
discriminator_depicted: yes
typed_1: structure | a pair-toggle move | the lit count | ∈ | - | Each move changes the number of lit lamps by plus two, minus two, or zero.
typed_2: symmetry | parity of the lit count | a pair-toggle move | invariant | - | The parity of the lit count is an invariant of every move.
typed_3: obstruction | the even starting lit count | the one-lamp target | forbids | - | The start has an even lit count (zero), but one lit lamp is odd, a contradiction.
---

CHAIN by blind player 1
1. 6️⃣💡 (root) — There are six lamps, all initially off.
2. 🔀2️⃣ (root) — Each move toggles exactly two distinct lamps, flipping each one's state.
3. ❓ (← 1, 2) — Can some sequence of moves leave exactly one lamp on (1️⃣💡 on, the other five off)?
4. 🔢 (← 2) — Each move changes the count of lit lamps by two, up or down, or leaves it the same: both lamps off go on (+2), both on go off (−2), and one of each swaps (0).
5. 🧬 (← 4) — So the parity of the lit count (even or odd) never changes, which makes it an invariant of every move.
6. 0️⃣ (← 1) — At the start no lamp is lit, so the lit count is zero, which is even.
7. 🟰 (← 5, 6) — Because parity is preserved and starts even, the lit count is even after any sequence of moves.
8. 1️⃣ (← 3) — Exactly one lamp on means a lit count of one, which is odd.
9. 💥 (← 7, 8) — The required odd count contradicts the always-even count, so the target is unreachable.
10. 👀 (← 9) — Self-check: the argument never used the number six, so it holds for any lamp count. It also never assumed the order of moves, so it covers every sequence.

LANDMARKS:
- Each move changes the number of lit lamps by plus two, minus two, or zero.
- The parity of the lit count is an invariant of every move.
- The start has an even lit count (zero), but one lit lamp is odd, a contradiction.

ANSWER: No
