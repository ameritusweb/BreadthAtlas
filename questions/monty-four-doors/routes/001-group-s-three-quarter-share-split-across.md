---
id: 001
question: monty-four-doors
title: Group's three-quarter share split across two closed doors
strategy: part-of-whole
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 1
referee: opus/v1
criterion: v1
verdict: VALID
reason: The frontier is empty, so all three landmarks are new: the unpicked group holds three in four, the host's reveal concentrates that chance on the two closed doors, and those two doors split it equally at three in eight each. Every step follows from its named parents, and the answer 3/8 matches the reference.
typed_1: share | original pick | other three doors | ≪ | one in four vs three in four | Your original pick holds the car one time in four, so the other three doors together hold it three times in four.
typed_2: reduction | other three doors | two closed doors | reduces-to | three in four | The host's goat reveal does not change the group's chance; it concentrates it on the two closed doors.
typed_3: symmetry | two closed doors | - | = | three in eight | The two remaining closed doors are symmetric and split the group's chance equally, so each gets three in eight.
---

CHAIN by duelist A
1. 🚪 (root) — Given: there are four doors, with one car and three goats behind them.
2. 🙋 (root) — Given: you pick one door at the start.
3. 🎩 (root) — Given: the host knows where the car is and always opens one of your other three doors to show a goat, then offers a switch to one of the two remaining closed doors.
4. ❓ (← 1, 2, 3) — Asked: the chance of winning the car if you switch to one of the two remaining closed doors, which differs from the familiar version where only one door is left to switch to.
5. 🎲 (← 1, 2) — Before any reveal the car is equally likely to be behind any door, so your first pick hides it only one time in four.
6. 👥 (← 5) — The other three doors together must hold the car whenever your pick does not, so as a group they hold it three times in four.
7. 🔒 (← 3, 6) — The group has at most one car, so the host can always show a goat from it, and the reveal gives no reason to change the group's chance.
8. 🧲 (← 6, 7) — The group's three-in-four chance therefore now sits entirely on its two still-closed doors, because the opened door is known to be a goat.
9. ⚖️ (← 3, 8) — Nothing distinguishes the two closed doors from your viewpoint, so they share the group's chance equally.
10. 🍰 (← 8, 9) — Each closed door gets half of the group's three-in-four chance, which is three in eight.
11. 👀 (← 5, 10) — Self-check: your own door's one in four plus the two switch doors' three in eight each fills the whole certainty, so nothing is lost or double counted.
12. 🏆 (← 4, 10) — Switching to one of the two closed doors therefore wins with chance three in eight.

LANDMARKS:
- Your original pick holds the car one time in four, so the other three doors together hold it three times in four.
- The host's goat reveal does not change the group's chance; it concentrates it on the two closed doors.
- The two remaining closed doors are symmetric and split the group's chance equally, so each gets three in eight.

ANSWER: 3/8
