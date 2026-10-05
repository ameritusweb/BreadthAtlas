---
id: 004
question: swap-ladder
title: Split at idle rail 7, mirror-cancel, trace right block
strategy: new: decompose-then-simulate
contributor: sonnet (duelist B)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: ILL-FORMED
reason: Step 7 (🔁) gets its result by "carrying the five right-block tokens through their rungs." That traces every token in the block, which is simulation under the v2 rule. The matching landmark only gives the net result (a J–L swap) and names no structural reason for it, such as the mirror symmetry around the unpaired row-21 rung on rails 10–11. The parity self-check in step 10 is consistent with that result but does not establish it.
note: re-judged 2026-10-05; previously ILL-FORMED: steps [10] do no work (nothing later follows from them)
---

CHAIN by duelist B
1. 🪜 (root) — Twelve tokens A–M (no I) start on rails 1–12, one token per rail.
2. 🔀 (root) — Forty-one rungs are applied top to bottom, and each swaps whichever two tokens sit on its two rails at that moment.
3. ❓ (← 1, 2) — Which token ends on rail 9, and how many tokens end on the rail where they started?
4. 🚧 (← 2, 3) — No rung touches rail 7, and none joins rail 6 to rail 8, so the token on rail 7 (G) never moves and the ladder splits into two separate blocks.
5. 🧩 (← 4) — The left block (rails 1–6) and the right block (rails 8–12) can be handled independently, because no token crosses between them.
6. 🪞 (← 5) — The left block's rungs read the same from top to bottom as from bottom to top, so each rung is cancelled by its mirror partner, working from the middle outward, and every left token ends where it began.
7. 🔁 (← 5) — Carrying the five right-block tokens through their rungs, H, K and M end on their home rails and only J and L trade places.
8. 🎯 (← 7) — Rail 9 is J's start rail, and after the trade it holds L.
9. 🧾 (← 4, 6, 7) — The tokens back home are the six on the left, G, and H, K and M on the right. J and L are the only ones displaced.
10. ⚖️ (← 7) — 👀 Self-check: the right block has an odd number of rungs, so its net effect must be an odd permutation, and a single swap of J and L is odd. The left block has an even number, which fits it being the identity.
11. 🏁 (← 8, 9) — The token on rail 9 is L, and ten tokens are back on their starting rails.

LANDMARKS:
- Rail 7 is untouched and no rung crosses between rails 6 and 8, so G is fixed and the ladder splits into two independent blocks.
- The left block's rungs form a mirror-symmetric (palindromic) sequence that cancels pair by pair, leaving rails 1–6 unchanged.
- The right block nets out to a single swap of J and L, which agrees with the parity of its rung count.
ANSWER: Token L is on rail 9, and 10 tokens are back on their starting rails.
