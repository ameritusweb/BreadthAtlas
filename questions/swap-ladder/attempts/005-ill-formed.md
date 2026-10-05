---
id: 005
question: swap-ladder
title: Block decomposition, then asserted cancellation per block
strategy: new: block-decomposition-then-parity
contributor: sonnet (duelist A)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: WRONG
reason: Steps 10–11 give the right-block result without deriving it. An odd rung count only shows the block's net effect is an odd permutation, not a single swap, and nothing in the chain says why the swapped pair is J and L. The chain never states the structure that would justify it: the right block mirrors itself around rung 21, which is the only rung without a partner. The answer is right (L on rail 9, ten tokens home) and nothing in the chain is a step-by-step snapshot, but the deciding step does not follow from the step it cites.
note: re-judged 2026-10-05; previously DUPLICATE: The chain is well-formed: it has no state snapshots, step 8 is a 👀 self-check and step 12 states a partial conclusion. I
typed_1: structure | the ladder | independent blocks | reduces-to | - | No rung crosses between rails 1–6, rail 7 and rails 8–12, so the ladder splits into independent blocks and G is untouched.
typed_2: reduction | the left block | the identity | reduces-to | - | The left block (rails 1–6) cancels to the identity, so A–F are all back home.
typed_3: reduction | the right block | a single exchange of J and L | reduces-to | - | The right block nets out to a single exchange of J and L (H, K and M return home), which puts L on rail 9.
---

CHAIN by duelist A
1. 🪜 (root) — Twelve tokens A–M (no I) start on rails 1–12, each on the rail below its letter.
2. 🔀 (root) — The forty-one rungs are applied top to bottom, and each rung swaps the two tokens on its two rails at that moment.
3. ❓ (← 1, 2) — Which token ends on rail 9, and how many tokens end on the rail where they started?
4. 🚧 (root) — In the picture, no rung touches rail 7, and no rung joins a rail from 1–6 to a rail from 8–12.
5. 🧩 (← 4) — The ladder splits into three independent blocks: rails 1–6, rail 7 alone, and rails 8–12. Tokens never leave their block, so each block can be solved separately.
6. 🔒 (← 4, 5) — Rail 7 has no rungs, so G never moves, which gives one fixed token.
7. ♻️ (← 5) — In the left block, the rungs form a back-and-forth pattern. The shuffles on rails 1–4 and the swaps on rails 5–6 undo each other as the sequence runs, so the whole left block cancels to doing nothing.
8. ⚖️ (← 7) — As a side check, the left block has an even count of rungs, which is consistent with a net identity, since an odd count could not cancel. 👀 (← 7)
9. 🟰 (← 7) — A, B, C, D, E and F all end on their starting rails, giving six fixed tokens.
10. 🔁 (← 5) — The right block has an odd count of rungs, so it cannot be the identity. Its rungs are a long run of alternating swaps among H, J, K, L and M, and that run collapses to one net exchange.
11. 🎯 (← 10) — H, K and M return to their own rails, and the one exchanged pair is J and L. J ends where L began (rail 11) and L ends where J began (rail 9).
12. 🅻 (← 11) — Rail 9 holds L, which answers the first half of the question.
13. 🧮 (← 6, 9, 11) — The fixed tokens are G, the six on the left, and H, K and M on the right. Only J and L are displaced, so the count of tokens back home is everything except those two, which is ten.

LANDMARKS:
- No rung crosses between rails 1–6, rail 7 and rails 8–12, so the ladder splits into independent blocks and G is untouched.
- The left block (rails 1–6) cancels to the identity, so A–F are all back home.
- The right block nets out to a single exchange of J and L (H, K and M return home), which puts L on rail 9.
ANSWER: Rail 9 holds L, and 10 tokens are back on their starting rails.
