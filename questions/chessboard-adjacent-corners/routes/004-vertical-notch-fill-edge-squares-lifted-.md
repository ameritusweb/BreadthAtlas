---
id: 004
question: chessboard-adjacent-corners
title: Vertical notch-fill, edge squares lifted into row three
strategy: new: explicit-construction
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 4
referee: opus/v1
criterion: v1
verdict: VALID
reason: The tiling checks out: 6 vertical dominoes in b–g across rows 1–2, 2 vertical dominoes at a2–a3 and h2–h3, 3 horizontal on b3–g3, and 20 horizontal on rows 4–8 make 31 with no overlaps or gaps. Its landmarks (vertical b–g pairs leaving a2 and h2; a2 and h2 rescued into row 3, leaving b3–g3; the three-row-plus-five-row split) were reached by no other played chain; their only prior appearance is this attempt's own earlier ILL-FORMED play, which cannot count against its re-judging.
note: re-judged 2026-10-05 from attempt 002 (ILL-FORMED: step 1 performs arithmetic: 'The board is a standard 8×8 grid of squares, with columns a–…')
typed_1: construction | notched bottom strip | vertical domino tiling | exists | - | Vertical dominoes in columns b–g across rows 1–2 fill the notched bottom strip, leaving only a2 and h2.
typed_2: construction | leftover squares a2 and h2 | row 3 run b3–g3 | reduces-to | parity | The leftover squares a2 and h2 are rescued by vertical dominoes reaching up into row 3, which leaves b3–g3 as a clean even run.
typed_3: structure | remaining board | bottom three-row region | = | - | The board is split into a bottom three-row region built from vertical and edge dominoes and an untouched five-row remainder.
---

CHAIN by duelist B
1. ♟️ (root) — The board is a standard 8×8 grid of squares, with columns a–h and rows 1–8.
2. ✂️ (root) — The two corners a1 and h1 at the same end of row 1 are removed.
3. 🁣 (root) — A domino covers exactly two edge-adjacent squares, either horizontally or vertically.
4. ❓ (← 1, 2, 3) — Can the 62 remaining squares be covered exactly by dominoes, with no overlaps and no gaps? Here two corners of the same edge are removed, not the opposite corners of the familiar puzzle.
5. 🧱 (← 4) — Split the board into the bottom two rows (rows 1–2) and the rest, and start with the bottom strip. In that strip row 2 is whole, and row 1 has only b1 through g1.
6. ↕️ (← 5, 3) — Place a vertical domino on each column from b to g, covering b1–b2 through g1–g2, so the six notches of row 1 are filled.
7. 🧩 (← 5, 6) — Only a2 and h2 are left uncovered in the strip, each one stranded at an end of row 2.
8. 🔗 (← 7, 3) — Cover a2 with a vertical domino reaching up to a3, and h2 with one reaching up to h3.
9. ➖ (← 8) — Row 3 now has only b3 through g3 left, a plain unbroken run of squares.
10. ➡️ (← 9, 3) — That run is covered by horizontal dominoes laid end to end across row 3.
11. 🏢 (← 8, 3) — Rows 4 through 8 are untouched, so horizontal dominoes cover each of them.
12. ✅ (← 6, 8, 10, 11) — Every one of the 62 squares is covered exactly once, so the tiling exists.
13. 👀 (← 12) — Self-check: the vertical pairs in rows 1–3 stay inside the board and avoid the removed corners, and no domino overlaps another or hangs off the edge.

LANDMARKS:
- Vertical dominoes in columns b–g across rows 1–2 fill the notched bottom strip, leaving only a2 and h2.
- The leftover squares a2 and h2 are rescued by vertical dominoes reaching up into row 3, which leaves b3–g3 as a clean even run.
- The board is split into a bottom three-row region built from vertical and edge dominoes and an untouched five-row remainder.

ANSWER: Yes, the remaining 62 squares can be exactly covered by 31 dominoes.
