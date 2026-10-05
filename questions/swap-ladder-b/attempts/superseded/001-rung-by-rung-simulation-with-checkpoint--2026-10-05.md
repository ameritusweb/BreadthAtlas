---
id: 001
question: swap-ladder-b
title: Rung-by-rung simulation with checkpoint rows at rungs 30 and 38
strategy: new: direct-simulation
contributor: sonnet (blind player 1)
date: 2026-10-05
referee: opus/v1
criterion: v1
verdict: WRONG
reason: Step 5 says that after rungs 7–11 "E and F come back to rails 5 and 6, and H and G are swapped," but by rung 11 the picture puts H on rail 5 and B on rail 6, with E on rail 4 and F on rail 7, as the chain's own row "C A D E H B F G" shows. The false claim is never used again, and every later row and the final answer A B D C E F G H J K L M are correct, but a false claim fails soundness on its own.
---

CHAIN by blind player 1
1. 🪜 (root) — Given: twelve tokens A–M (no I) start on rails 1–12, in alphabetical order.
2. 🔀 (root) — Given: forty-one rungs are applied top to bottom, and each rung swaps the two tokens on its two rails at that moment.
3. ❓ (← 1, 2) — Asked: which token ends on rail 3, and how many tokens end on the rail where they started? This version has 41 rungs, and the tokens skip the letter I.
4. 👆 (← 2, 3) — The top rungs are read first: 5↔6, 2↔3, 1↔2, then 10↔11, 5↔6, 7↔8. The first 5↔6 is undone by the second, and the left side becomes C A B D.
5. 🧩 (← 4) — Rungs 7–11 are 9↔10, 6↔7, 3↔4, 4↔5, 5↔6. The tokens E and F come back to rails 5 and 6, and H and G are swapped. By rung 11 the left side reads C A D E, then H B F G.
6. 🔁 (← 5) — The 1↔2 and 2↔3 rungs recur through the middle: rungs 13, 17, 18, 21, 24, 25, 29. Together they leave rail 1 holding D and rails 2–3 holding A and C after rung 29.
7. 🌀 (← 5) — The right-hand 8↔9 and 7↔8 rungs (12, 16, 19, 20, 22, 23, 26, 30) and the 10↔11 rungs (4, 15, 27, 38) mostly cancel out. By rung 30 the right side reads F G L J K M.
8. 🧮 (← 6, 7) — After rung 30 the full row is D A C E H B F G L J K M. Every token is displaced, so the bottom rungs still decide the result.
9. 🔧 (← 8) — Rungs 31–34 (5↔6, 4↔5, 3↔4, 6↔7) pull B into rail 3 and C into rail 4. They also put E, F and H in their home order. The row becomes D A B C E F H G L J K M.
10. 🧹 (← 9) — Rungs 35–38 (9↔10, 7↔8, 5↔6, 10↔11) restore G, H, J, K, L to their home rails. They also swap E and F, leaving D A B C F E G H J K L M.
11. 🏁 (← 10) — The last three groups are 1↔2 (rung 39), 2↔3 (rung 40) and 5↔6 (rung 41). Rungs 39 and 40 carry D rightward from rail 1 to rail 3, and rung 41 restores E and F. The final row is A B D C E F G H J K L M.
12. 👀 (← 11) — Self-check: 41 rungs were counted from the picture, and the final row is a valid permutation of all twelve letters. Only D and C are out of place, and they sit on each other's rails.
13. ✅ (← 11, 12) — Rail 3 holds D. Ten of the twelve tokens are on their starting rails, because only C and D are swapped.

LANDMARKS:
- After rung 30 the row is D A C E H B F G L J K M.
- Rungs 31–38 restore everything on the right to home order and bring B to rail 3.
- The final row is A B D C E F G H J K L M, with only C and D swapped.
ANSWER: Token D is on rail 3, and 10 tokens are back on their starting rails.
