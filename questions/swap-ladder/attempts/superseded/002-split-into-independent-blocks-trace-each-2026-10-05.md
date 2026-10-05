---
id: 002
question: swap-ladder
title: Split into independent blocks, trace each rung-by-rung
strategy: new: block-decomposition-trace
contributor: sonnet (blind player 2)
date: 2026-10-05
referee: opus/v1
criterion: v1
verdict: DUPLICATE
reason: Every landmark repeats attempt 001, which counts even though it was rejected. "Rail 7 has no rung, so G is fixed" is the same as 001's "rail 7 alone" block. "H, K, M home; J and L swapped" is the same as 001's right-block result. "Ten home" only restates the final count that follows from 001's landmarks 2 and 3.
---

CHAIN by blind player 2
1. 🔤 (root) — Twelve tokens A–M (no I) start on rails 1–12, one token per rail.
2. 🪜 (root) — Forty-one rungs are applied top to bottom, and each rung swaps the two tokens on its two rails at that moment.
3. 🖼️ (root) — The picture shows which pair of neighbouring rails each rung joins, and in what order.
4. ❓ (← 1, 2, 3) — Which token ends on rail 9, and how many tokens end on the rail where they began?
5. 7️⃣ (← 3) — No rung touches rail 7, so G never moves and stays home.
6. ⬅️ (← 2, 3) — Every rung on the left lies within rails 1–6, so those six tokens only mix among themselves. I follow them rung by rung.
7. ✅ (← 6) — After the last left rung, A to F are back in their starting order, so all six are home.
8. ➡️ (← 2, 3) — Every rung on the right lies within rails 8–12, so those five tokens form a separate group. I follow them rung by rung.
9. 🧩 (← 8) — After the last right rung the order on rails 8–12 is H, L, K, J, M.
10. 🎯 (← 9) — Rail 9 is the second place in that order, so it holds L.
11. 🏠 (← 9) — H, K and M are on their own rails, and only J and L have traded places.
12. 👀 (← 10) — Self-check: just before the final rung (a swap of rails 8 and 9), rail 9 holds H. That swap brings L onto rail 9, which agrees with step 10.
13. 🧮 (← 5, 7, 11) — Counting the home tokens: the whole left group, G, and H, K, M. Everything is home except J and L.
14. 🏁 (← 10, 13) — Rail 9 holds L, and ten tokens are home.

LANDMARKS:
- Rail 7 has no rung, so G is a fixed point that never moves.
- On the right, H, K and M end on their own rails while J and L have swapped places.
- Everything except J and L ends at home, so ten of the twelve tokens are back where they started.

ANSWER: Token L is on rail 9, and 10 tokens are back on their starting rails.
