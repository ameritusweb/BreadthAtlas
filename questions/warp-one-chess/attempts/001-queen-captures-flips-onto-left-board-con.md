---
id: 001
question: warp-one-chess
title: Queen captures, flips onto Left board, contact mate
strategy: new: mirror-landing-contact-mate
contributor: opus (blind player 1)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: WRONG
reason: Step 7 fails. The empirical referee rejects ply 1 `Rg3Rf4=Lf4` as an illegal move from P01, so the capture-then-flip landing on Lf4 never happens and the mate claimed in steps 10–12 does not exist. The chain's own caveat says it did not check Black's cross-board replies.
discriminator_depicted: yes
typed_1: obstruction | Ld4 | kill zone around the Black king | ∈ | - | Ld4 is the only square around the king that the other White pieces leave uncovered.
typed_2: construction | post-flip queen landing on Lf4 | Ld4 | forbids | - | A post-flip landing on Lf4 gives check from a square defended by the Lg3 pawn and covers Ld4 along rank 4.
typed_3: obstruction | Black pieces on the Left board | contact check | forbids | - | With no Black piece on the Left board, the contact check cannot be answered on that board.
---

CHAIN by blind player 1
1. ♟️ (root): In P01 the Black king stands on Le3, and every square around it on the Left board is empty or White-occupied, with no other Black piece on the Left board.
2. 🌀 (root): By the Warp 1 rule a piece may flip to its mirror square after moving, so a Right-board piece can land on the Left board.
3. ❓ (← 1, 2): Find a mechanism and a line from P01, White to move, that ends in checkmate, with the mechanism as the finishing tactic.
4. 🎯 (← 1): The kill zone is the ring Ld2, Ld3, Ld4, Le2, Le4, Lf2, Lf3, Lf4 around the king on Le3.
5. 👑 (← 4): The White king on Le1 already covers Ld2, Le2 and Lf2 in that ring.
6. 🔱 (← 4): White's own pieces cover more of the ring: the Lc3 knight covers Le2 and Le4, the Lg1 knight covers Le2 and Lf3, and the Lf1 bishop covers Ld3 through the empty Le2.
7. 🪞 (← 2): The White queen on Rg3 can capture the pawn on Rf4 and then flip to its mirror Lf4, arriving diagonally next to the king and giving check.
8. 📐 (← 7): From Lf4 the queen sweeps rank 4 through the empty Le4 to Ld4, and it sweeps the f-file down through Lf3, which closes the last gaps in the ring.
9. 🛡️ (← 7, 1): The Lg3 pawn defends Lf4, so the king cannot capture the queen, and Black has no piece on the Left board that could take it.
10. 🫁 (← 5, 6, 8, 9): Every square in the ring is now covered, and the check is a contact check that cannot be blocked.
11. 👀 (← 10): Self-check: Ld4 was the only square nothing else covered, and the queen's rank-4 line covers it, so no plain flight square is left.
12. 🏁 (← 10): Therefore the capture on Rf4 followed by the flip to Lf4 is mate in one, and the flip landing is the finishing tactic.

LANDMARKS:
- Ld4 is the only square around the king that the other White pieces leave uncovered.
- A post-flip landing on Lf4 gives check from a square defended by the Lg3 pawn and covers Ld4 along rank 4.
- With no Black piece on the Left board, the contact check cannot be answered on that board.

Caveat: I checked only the Left board by hand. I have not ruled out Black answers that use flips, such as the Black king flipping to an open Right-board square, or the Re3 queen recapturing across the boards. If the rules allow those, this line is not mate.

ANSWER: mechanism mirror-landing queen check; position P01; line Rg3Rf4=Lf4
