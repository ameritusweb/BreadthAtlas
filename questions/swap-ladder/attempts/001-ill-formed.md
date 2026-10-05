---
id: 001
question: swap-ladder
title: (form failure)
strategy: unclassified
contributor: sonnet (blind player 1)
date: 2026-10-05
referee: code/v1
criterion: v1
verdict: ILL-FORMED
reason: steps [11] do no work (nothing later follows from them)
---

CHAIN by blind player 1
1. 🪜 (root) — Twelve tokens A–M (no I) start on rails 1–12, one token per rail.
2. ↕️ (root) — Forty-one rungs are applied from top to bottom, and each rung swaps the two tokens on its two rails at that moment.
3. ❓ (← 1, 2) — Which token ends on rail 9, and how many tokens end on the rail where they started?
4. 🧩 (← 2) — No rung touches rails 1–6 and also rails 8–12, and none touches rail 7. So the ladder splits into a left group (rails 1–6), a right group (rails 8–12), and rail 7 alone.
5. 🟰 (← 1, 4) — G sits alone on rail 7 and never moves, so it counts as one token back home.
6. 🔀 (← 4) — I follow the left group (A–F) rung by rung. It uses only the rungs between rails 1–2, 2–3, 3–4, 4–5 and 5–6, and it shuffles tokens among those six rails.
7. 🏠 (← 6) — After the last left rung, A, B, C, D, E and F are all back on their starting rails. The middle shuffles cancel out, and the final rung between rails 4 and 5 restores D and E. That gives six tokens home.
8. 🔁 (← 4) — I follow the right group (H, J, K, L, M) on rails 8–12 through its 25 rungs, and I track its order after every rung.
9. 📍 (← 8) — Partway through, the order on rails 8–12 is K, J, H, L, M. Rungs 38, 39 and 40 then turn it into L, H, K, J, M.
10. 🏁 (← 9) — The last rung, between rails 8 and 9, swaps L and H. The right group ends as H, L, K, J, M on rails 8–12.
11. 🎯 (← 10) — Rail 9 holds L at the end, which answers the first half of the question.
12. 🔢 (← 10) — On the right, H is on rail 8, K on rail 10 and M on rail 12, all where they started. L and J have swapped places, so three tokens are home.
13. ➕ (← 5, 7, 12) — Adding G (one), the left group (six) and the right group (three) gives ten tokens on their starting rails.
14. 👀 (← 13) — Self-check: the two non-home tokens, J and L, sit on each other's start rails (J on 11, L on 9). That leaves exactly two tokens off their start rails, and the total is consistent.
LANDMARKS:
- The ladder splits into independent blocks: rails 1–6, rail 7 alone, and rails 8–12.
- The left block (A–F) returns completely to its starting order.
- The right block ends as H, L, K, J, M, so L is on rail 9 and only J and L are displaced.
ANSWER: L is on rail 9, and 10 tokens are back on their starting rails.
