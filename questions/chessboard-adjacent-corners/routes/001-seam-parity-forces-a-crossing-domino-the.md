---
id: 001
question: chessboard-adjacent-corners
title: Seam parity forces a crossing domino, then halves tile
strategy: new: cut-parity (split along a line, use parity to force crossings)
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 1
referee: opus/v1
criterion: v1
verdict: VALID
reason: Every step holds. Each half has 31 squares, so an odd number of dominoes must cross the seam, and with d1–e1 placed the tiling covers all 62 squares exactly. The final tiling is the same as attempt 001's, but the first two landmarks are new: each half-board has an odd number of squares, so an odd number of dominoes must straddle the central seam.
typed_1: structure | half-board with one corner removed | - | = | parity | Each half-board (left and right of the central seam) has an odd number of squares once a corner is removed.
typed_2: obstruction | dominoes inside a half | dominoes straddling the seam | forbids | parity | Dominoes inside a half cover an even number of its squares, so an odd number of dominoes must straddle the seam.
typed_3: construction | seam domino d1–e1 | exact domino covering | exists | parity | One domino straddling the seam on the bottom row (d1–e1) fixes the parity, and each half then splits into even pieces.
---

CHAIN by duelist A
1. ♟️ (root) — A standard chessboard has columns a–h and rows 1–8, with a central seam between columns d and e.
2. ✂️ (root) — The corners a1 and h1, at the two ends of the same edge row, are removed.
3. ❓ (← 1, 2) — Can the remaining squares be exactly covered by dominoes? This is not the opposite-corners version, because both removed squares are on the same edge.
4. ⬅️ (← 1, 2) — The left half (columns a–d) is a full half-board with a1 removed, so it holds an odd number of squares.
5. ➡️ (← 1, 2) — The right half (columns e–h) likewise lost h1, so it also holds an odd number of squares.
6. 🧩 (← 4, 5) — Dominoes lying wholly inside one half cover an even number of its squares, so an odd half needs an odd number of dominoes straddling the seam.
7. 🎯 (← 6) — The simplest choice is exactly one straddling domino, placed on the bottom row as d1–e1.
8. 🟦 (← 4, 7) — With d1 taken, the left half is b1–c1 as one horizontal domino, plus rows 2–8 of columns a–d as horizontal pairs a–b and c–d.
9. 🟥 (← 5, 7) — By mirror image, the right half is f1–g1 as one horizontal domino, plus rows 2–8 of columns e–h as horizontal pairs e–f and g–h.
10. 🔗 (← 7, 8, 9) — The seam domino, the left-half dominoes and the right-half dominoes together make a complete covering.
11. 👀 (← 10) — Self-check: row 1 is b1c1, d1e1, f1g1, which skips a1 and h1, and no square is used twice.
12. ✅ (← 3, 10) — A full exact covering exists, so the answer to the question is yes.

LANDMARKS:
- Each half-board (left and right of the central seam) has an odd number of squares once a corner is removed.
- Dominoes inside a half cover an even number of its squares, so an odd number of dominoes must straddle the seam.
- One domino straddling the seam on the bottom row (d1–e1) fixes the parity, and each half then splits into even pieces.

ANSWER: Yes
