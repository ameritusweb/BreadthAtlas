---
id: 003
question: chessboard-adjacent-corners
title: Horizontal row-by-row tiling after the shortened first row
strategy: new: explicit-construction
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 3
referee: opus/v1
criterion: v1
verdict: VALID
reason: The tiling is correct: rows 2–8 take 28 horizontal dominoes and b1–g1 takes three, which makes 31. No chain was played before attempt 001, so its own earlier landmarks (1–3: opposite-coloured corners keep the counts balanced, full rows tiled horizontally, b1–g1 an even run of three dominoes) cannot make it a duplicate, and they are new.
note: re-judged 2026-10-05 from attempt 001 (ILL-FORMED: step 1 performs arithmetic: 'The board is a standard 8×8 chessboard whose squares alterna…')
typed_1: symmetry | removed squares a1 and h1 | color counts | invariant | parity | The two removed squares a1 and h1 have opposite colors, so the color counts stay balanced.
typed_2: construction | rows 2 to 8 | horizontal domino tiling | exists | - | Rows 2 through 8 are untouched full rows, each tiled by horizontal dominoes.
typed_3: construction | row 1 run b1–g1 | horizontal domino tiling | exists | parity | The leftover first row b1–g1 is an even-length unbroken run, tiled by three horizontal dominoes.
typed_4: construction | remaining board | exact domino covering | exists | - | The answer comes from an explicit tiling, not from a color-balance argument alone.
---

CHAIN by duelist A
1. ♟️ (root) — The board is a standard 8×8 chessboard whose squares alternate light and dark.
2. ✂️ (root) — The two squares a1 and h1, the ends of one edge row, are removed, leaving 62 squares.
3. ❓ (← 1, 2) — Asked: can the 62 remaining squares be exactly covered by 31 dominoes, each covering two adjacent squares? Note that the removed corners are both on the same edge, unlike the familiar version with opposite corners.
4. 🔀 (← 1, 2) — A row of eight alternating squares starts and ends on opposite colors, so a1 and h1 have different colors.
5. ⚖️ (← 4) — Removing one light and one dark square leaves equal numbers of each, so the usual color-count obstruction does not apply.
6. 🧱 (← 1) — Rows 2 through 8 are untouched, so they are seven complete rows of eight squares.
7. ↔️ (← 6) — Each complete row of eight splits into side-by-side horizontal dominoes with nothing left over, so all seven rows are covered.
8. 🪟 (← 2) — The damaged first row is now just b1 through g1, a single unbroken run of squares.
9. 🔢 (← 8) — That run has an even length, so it pairs off from the left as b1-c1, d1-e1, f1-g1 with nothing left over.
10. 🧩 (← 7, 9) — The seven full rows and the repaired first row are covered by separate dominoes that never overlap, so the whole remaining board is covered.
11. 👀 (← 5, 10) — Self-check: every horizontal domino covers one light and one dark square, which matches the balanced colors, so there is no conflict.
12. ✅ (← 3, 10) — The explicit tiling answers the question: yes, the board can be covered.
LANDMARKS:
- The two removed squares a1 and h1 have opposite colors, so the color counts stay balanced.
- Rows 2 through 8 are untouched full rows, each tiled by horizontal dominoes.
- The leftover first row b1–g1 is an even-length unbroken run, tiled by three horizontal dominoes.
- The answer comes from an explicit tiling, not from a color-balance argument alone.
ANSWER: Yes, the remaining 62 squares can be exactly covered by 31 dominoes.
