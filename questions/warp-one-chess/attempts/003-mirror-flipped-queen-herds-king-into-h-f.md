---
id: 003
question: warp-one-chess
title: Mirror-flipped queen herds king into h-file corner
strategy: new: mirror-flip-corner-sweep
contributor: opus (blind player 3)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: WRONG
reason: Steps 7–8 say the post-flip queen on Lg5 leaves the king only Lh3, but they only consider the Left board and ignore Black's own flip escapes. The engine shows Black can answer with Lg4>Rg4Rg5 instead of Lg4Lh3, so the line is not forced. Step 14 admits this was never checked.
discriminator_depicted: yes
typed_1: obstruction | post-flip queen on Lg5 | Black king flight squares | reduces-to | - | A post-flip queen landing on Lg5, guarded by the Le4 knight, leaves the Black king only Lh3 on the Left board.
typed_2: construction | queen check on the h-file | White king on Lf2 | forbids | - | Queen Lg5–Lh5 checks down the h-file. The x-ray makes Kxh2 illegal, and the White king on Lf2 seals g2 and guards g3.
typed_3: structure | White king | corner net on the h-file | ∈ | - | The White king acts as the decisive co-attacker in a corner net on the h-file.
---

CHAIN by blind player 3
1. 🗺️ (root): In P07 the Black king stands on Lg4 with no other Black piece on the Left board. White has Ke4 and Nd3 knights, pawns g3 and h2, and the king on Lf2 there.
2. 🌀 (root): A piece may flip to its mirror square, which has the same coordinates on the other board, before or after it moves. So the White queen on Rh6 can reach Left-board squares in one move.
3. ❓ (← 1, 2): Name a mechanism and give a forced line from P07 to mate in which it is the finishing tactic. 🪞♛➡️🧭: the queen arrives on the king's board through a mirror flip, which is not possible in ordinary chess.
4. 🎯 (← 1): Around Lg4, the White king covers f3. The g3 pawn, guarded by Kf2 and h2, cannot be taken. Pawn g3 and Nd3 cover f4 and h4, and Ne4 covers g5, so only f5, h3 and h5 are open.
5. 🌀 (← 2, 4): The queen slides Rh6–Rg5 on the Right board and post-flips to Lg5, giving contact check on the king's own board.
6. 🛡️ (← 1, 5): Lg5 is guarded by the knight on Le4, so the king cannot capture the queen.
7. 🧱 (← 4, 5): From Lg5 the queen covers f5 along the rank and h5 and h4 by contact. Together with step 4, that leaves only Lh3 on the Left board.
8. 🚶 (← 7): Black's king is herded into the corner pocket on Lh3.
9. 🎯 (← 1, 8): Around Lh3, g2 is covered by Kf2, and g3 is a guarded pawn. h2 is a White pawn that only the h-file can guard.
10. 🔫 (← 8, 9): The queen steps sideways from Lg5 to Lh5, giving check down the empty h-file.
11. 📐 (← 10): The queen on h5 x-rays through the king along the h-file, so Kxh2 stays in check. It also covers g4 along the diagonal and h4 on the file.
12. 👑 (← 1, 9): The White king on Lf2 is a weapon here, because it alone denies g2 and guards the g3 pawn.
13. 🫁 (← 9, 11, 12): Every Left-board square around Lh3 is covered or self-blocked, so the king is netted in the corner.
14. 👀 (← 13): Self-check: this ruling depends on the referee engine also finding no Black flip-escape or flip-capture of Lh5 from the Right board. I have not verified that by search.
15. 🏁 (← 5, 10, 13): The finishing tactic is a mirror-flipped queen that sweeps the king into the corner and mates along a file, with its own king as co-attacker.
LANDMARKS:
- A post-flip queen landing on Lg5, guarded by the Le4 knight, leaves the Black king only Lh3 on the Left board.
- Queen Lg5–Lh5 checks down the h-file. The x-ray makes Kxh2 illegal, and the White king on Lf2 seals g2 and guards g3.
- The White king acts as the decisive co-attacker in a corner net on the h-file.
ANSWER: mechanism mirror-flip corner sweep; position P07; line Rh6Rg5=Lg5 Lg4Lh3 Lg5Lh5
