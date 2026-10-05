---
id: 006
question: swap-ladder
title: Parity of forty-one transpositions bounds the home count
strategy: new: parity-bound
contributor: sonnet (duelist B)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: WRONG
reason: The final answer is wrong on both parts: rail 9 holds L, not H, and ten tokens are home, not four. Step 10 admits the argument cannot settle the question, so the answer is an unsupported guess. Steps 4–9 are sound and contain no simulation, so form does not fail.
note: re-judged 2026-10-05; previously ILL-FORMED: steps [10] do no work (nothing later follows from them)
typed_1: reduction | the ladder | a product of forty-one transpositions | reduces-to | - | Each rung is one transposition, so the whole ladder is a product of forty-one transpositions.
typed_2: obstruction | the odd rung count | the identity | forbids | permutation parity | The odd rung count makes the final arrangement an odd permutation, which is never the identity.
typed_3: bound | tokens back on their starting rails | twelve tokens | ≪ | ten tokens | At most ten of the twelve tokens can be back on their starting rails.
---

CHAIN by duelist B
1. 🪜 (root) — Given: there are forty-one rungs, applied top to bottom, and each rung swaps the two tokens on its two rails.
2. 🔤 (root) — Given: twelve tokens A–M (no I) start on rails 1–12, one token per rail.
3. ❓ (← 1, 2) — Asked: after the last rung, which token is on rail 9, and how many tokens are on the rail where they started?
4. 🔁 (← 1) — Each rung exchanges exactly two tokens and leaves the rest alone, so each rung is a single transposition.
5. 🧮 (← 1, 4) — The ladder is a chain of forty-one transpositions, and the final arrangement is their composition.
6. 🎲 (← 5) — The number of rungs is odd, and every transposition flips the parity of the arrangement, so the final arrangement is an odd permutation.
7. 🚫 (← 6) — An odd permutation cannot be the identity, so at least two tokens must have left their starting rails.
8. 📏 (← 2, 7) — Tokens back home are the fixed points, so with twelve tokens at most ten can be home.
9. 🧩 (← 6, 8) — The fixed points sit inside the leftover cycles, and those cycles together make an odd permutation. This confines the home count to the range zero to ten.
10. 🔎 (← 3, 9) — Pinning down rail 9 and the exact home count needs the rung positions in the picture, which this structural argument does not supply.
11. 👀 (← 7) — Self-check: a single swap is odd and moves two tokens, which agrees with step 7's lower bound of two.

LANDMARKS:
- Each rung is one transposition, so the whole ladder is a product of forty-one transpositions.
- The odd rung count makes the final arrangement an odd permutation, which is never the identity.
- At most ten of the twelve tokens can be back on their starting rails.

ANSWER: I could not read the image, so this is a guess: rail 9 holds token H, and 4 tokens are back on their starting rails.
