---
id: 002
question: chessboard-adjacent-corners
title: Vertical six-row block plus a hand-tiled notched two-row strip
strategy: new: explicit-construction
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 2
referee: opus/v1
criterion: v1
verdict: VALID
reason: The tiling is sound: 24 vertical dominoes cover rows 3–8, and 7 dominoes cover the strip (a2b2, g2h2, b1c1, d1e1, f1g1, c2d2, e2f2), giving 31 in all. Two landmarks are new: the two-row strip missing its two bottom corners, and closing that strip's ends with horizontal a2b2 and g2h2. Attempt 002 instead covered columns b–g of rows 1–2 with vertical dominoes and closed the ends vertically into row 3, and attempt 001 split the board as rows 2–8 plus b1–g1.
typed_1: construction | rows 3 to 8 | vertical domino tiling | exists | parity | Rows 3 to 8 form an even-height full rectangle that vertical dominoes cover column by column.
typed_2: structure | two-row strip | - | = | - | What is left is a two-row strip of fourteen squares, missing its two bottom corners.
typed_3: construction | two-row strip | horizontal domino tiling | exists | - | The strip's ends are closed off by horizontal dominoes in row 2 (a2b2 and g2h2), and the middle is filled by horizontal pairs.
---

CHAIN by duelist B
1. ♟️ (root) — A standard chessboard is 8 columns wide and 8 rows tall, and a domino covers two squares that share an edge.
2. ✂️ (root) — The squares a1 and h1, the two ends of the bottom row, are removed, leaving 62 squares.
3. ❓ (← 1, 2) — Can the remaining squares be exactly covered by dominoes? This is not the opposite-corners version, because both removed squares sit on the same edge row.
4. 🔝 (← 1, 2) — Rows 3 to 8 are untouched by the removal, so they form a full rectangle six rows tall and eight columns wide.
5. 🧱 (← 4) — Each column of that rectangle is six squares tall, an even height, so stacked vertical dominoes cover it, three per column.
6. 🪟 (← 2, 5) — What remains is only a thin strip of rows 1 and 2, which is row 2 whole plus b1 to g1 in row 1.
7. ◀️ (← 6) — At the left end of the strip, a2 has no square below it, so it pairs sideways with b2 in a horizontal domino.
8. ▶️ (← 6) — At the right end, h2 is likewise paired sideways with g2 in a horizontal domino.
9. 🟰 (← 6, 7, 8) — The middle of the strip is then b1 to g1 beneath c2 to f2, which is a notched block of ten squares.
10. 🔲 (← 9) — Row 1 splits into three horizontal dominoes b1c1, d1e1 and f1g1, and the gaps above are c2d2 and e2f2, which are also horizontal pairs.
11. 🔗 (← 5, 7, 8, 10) — The vertical block, the two end dominoes and the five middle dominoes together cover every remaining square once.
12. 👀 (← 11) — Self-check: the strip's 14 squares are used by seven dominoes with no overlap, and a1 and h1 are never touched.
13. ✅ (← 3, 11) — An exact covering exists, so the answer to the question is yes.

LANDMARKS:
- Rows 3 to 8 form an even-height full rectangle that vertical dominoes cover column by column.
- What is left is a two-row strip of fourteen squares, missing its two bottom corners.
- The strip's ends are closed off by horizontal dominoes in row 2 (a2b2 and g2h2), and the middle is filled by horizontal pairs.

ANSWER: Yes
