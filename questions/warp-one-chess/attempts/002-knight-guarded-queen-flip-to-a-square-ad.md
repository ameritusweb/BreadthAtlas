---
id: 002
question: warp-one-chess
title: Knight-guarded queen flip to a square adjacent to the king
strategy: new: guarded-adjacent-flip-queen-mate
contributor: opus (blind player 2)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: WRONG
reason: Step 7 (and step 12, which builds on it) spends a quiet tempo on Lb1Ld2 to guard Lf3, so Black is not forced into Ra1Rb1. The empirical referee shows that at ply 2 Black plays Rc3Re2 instead, and White has no mate on the next move. The cited line is escapable, and the engine's ruling is final on soundness.
discriminator_depicted: yes
typed_1: obstruction | Black king's back rank and Lg3 | rook Lh1 and pawn pair g3/h2 | forbids | - | The rook on Lh1 and the pawn pair g3/h2 already shut Lf2's back rank and Lg3.
typed_2: construction | knight guard on Ld2 | king capture on Lf3 | forbids | - | A knight moved to Ld2 guards Lf3, so a queen flipped there cannot be captured by the king.
typed_3: construction | queen post-flip landing on Lf3 | Black king's ring | forbids | - | A queen flipped to Lf3 from the Right board covers Le2, Le3 and Lg2 at the same moment.
---

CHAIN by blind player 2
1. 🌀 (root) — In Warp 1 a piece may flip to its mirror square on the other board either before or after it moves, so a piece on one board can land on the other.
2. 🪞 (root) — In P09 the White queen stands on Rf2, the mirror of the Black king's square Lf2.
3. 🗺️ (root) — In P09 the Left board holds White's Rh1, the h2 and g3 pawns, a knight on Lb1, and a king on Lc2 that is too far away to touch the Black king's ring.
4. ❓ (← 1, 2, 3) — Name a winning mechanism in Warp 1, and prove it with a line from a cited position that ends in checkmate with that mechanism as the finishing blow.
5. 📏 (← 3) — The rook on Lh1 sweeps the whole first rank, which shuts the Black king out of Le1, Lf1 and Lg1.
6. ♟️ (← 3) — The h2 pawn defends the g3 pawn, so the king can never capture on Lg3.
7. 🐴 (← 3) — A knight brought from Lb1 to Ld2 guards Lf3, the square right in front of the king.
8. 🦀 (← 1, 2) — Because it stands on the king's mirror file, the queen can step up one square on the Right board and then flip onto Lf3, landing next to the king.
9. 👑 (← 8) — From Lf3 the queen covers Le2 and Lg2 on its diagonals and Le3 along its rank, which closes the king's remaining exits.
10. 🎯 (← 5, 6, 9) — Rank 1 is covered by the rook, Lg3 by the pawn, and the rest of the ring by the queen, so no square next to the king is free.
11. 🫁 (← 7, 8) — The checking queen is guarded by the Ld2 knight, so the king cannot take it.
12. 🔱 (← 7, 10, 11) — With the knight guard set up first, the post-flip queen check works as a guarded, adjacent kill that leaves nothing in the king's ring free.
13. 👀 (← 12) — Self-check: this rests on the guarded landing square Lf3, not on the Lf4 or Ld4 ideas from the earlier failed attempt.

LANDMARKS:
- The rook on Lh1 and the pawn pair g3/h2 already shut Lf2's back rank and Lg3.
- A knight moved to Ld2 guards Lf3, so a queen flipped there cannot be captured by the king.
- A queen flipped to Lf3 from the Right board covers Le2, Le3 and Lg2 at the same moment.

ANSWER: mechanism guarded mirror-flip queen kill; position P09; line Lb1Ld2 Ra1Rb1 Rf2Rf3=Lf3
