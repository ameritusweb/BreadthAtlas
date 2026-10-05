---
id: 003
question: swap-ladder-b
title: Parity plus block separation asserting cancellation
strategy: new: parity-and-block-decomposition
contributor: sonnet (duelist A)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: WRONG
reason: Step 6 does not follow from its parents (← 2, 4): having only four rungs between rails 4 and 5 says nothing about which tokens end up in which block. Steps 7 and 10 are also unsupported. "The many small rungs cancel" and "the shuffling undoes itself" are stated without any structural reason, and an odd rearrangement of four tokens (step 9) does not force a single C–D swap with A and B home. The final answer is correct, but the chain asserts the cancellation instead of deriving it; it never uses the mirror of rungs 1–20 in 22–41 around the unpaired rung at row 21.
note: re-judged 2026-10-05; previously ILL-FORMED: steps [11, 12] do no work (nothing later follows from them)
---

CHAIN by duelist A
1. 🪢 (root) — Twelve tokens A–M (no I) start on rails 1–12, one token per rail.
2. 🪜 (root) — Forty-one rungs are applied top to bottom, and each rung swaps the two tokens on its two rails at that moment.
3. ❓ (← 1, 2) — Asked: which token is on rail 3 after the last rung, and how many tokens are back on their starting rail? The ladder is a fresh instance with a different drawing than the familiar one.
4. 🚫 (root) — In the picture, rail 12 has no rung touching it, so token M never moves.
5. 🔀 (← 2) — Every rung is a single swap, so the whole ladder is one rearrangement of the tokens. An odd number of rungs makes that rearrangement odd, meaning it cannot be the do-nothing rearrangement.
6. 🚪 (← 2, 4) — Only four rungs link rails 4 and 5, so rails 1–4 and rails 5–12 trade tokens at only a few doorways. Tracking the tokens through those doorways, the left block ends holding exactly its own four tokens A–D, and the right block holds E–M.
7. 🎯 (← 4, 6) — In the right block, the many small rungs among rails 5–11 cancel out in net effect. Each of E, F, G, H, J, K, L ends on its own rail, and M is already fixed.
8. 🔁 (← 6) — In the left block, only A, B, C and D are shuffled, by many rungs between rails 1–2 and 2–3 and by just two rungs between rails 3–4. Their net effect is some rearrangement of those four tokens.
9. 🧮 (← 5, 7, 8) — The whole ladder is odd and the right block contributes no net change, so the left four tokens must be rearranged in an odd way.
10. ✂️ (← 8, 9) — The shuffling on rails 1–2 and 2–3 undoes itself, so A and B return home. The odd leftover is then a single swap of the two tokens C and D.
11. 🥇 (← 10) — C and D have traded places, so rail 3 holds D.
12. 🔟 (← 7, 10) — Every token except the swapped pair C and D is home, which leaves ten tokens on their starting rails.
13. 👀 (← 5, 10) — Self-check: one swap is an odd rearrangement, which agrees with an odd number of rungs. The answer is consistent.

LANDMARKS:
- Rail 12 is never touched, so M is fixed.
- An odd number of rungs means the overall rearrangement is odd, so it cannot be the identity.
- The right block (E–M) nets out to the identity, and A and B return home.
- The whole ladder amounts to a single swap of C and D.

ANSWER: Rail 3 holds token D, and 10 tokens are back on their starting rails.
