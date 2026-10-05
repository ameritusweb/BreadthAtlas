---
id: 001
question: monty-four-doors
title: Case split on first pick, halve wrong-pick share
strategy: part-of-whole
contributor: sonnet (duelist B)
date: 2026-10-05
referee: opus/v1
criterion: v1
verdict: DUPLICATE
reason: The chain is sound, but each of its landmarks matches one from route 001 in substance. "Pick is right one time in four" matches landmark 1; "in the wrong-pick case the car must be behind one of the two closed doors" matches landmark 2 (the host concentrates the group's three-in-four chance on the two closed doors); "a blind switch finds it half the time, half of three quarters" matches landmark 3 (the two doors split the chance equally, three in eight each).
typed_1: share | original pick | - | = | one in four | If your first pick is right, which happens one time in four, every switch loses.
typed_2: reduction | other three doors | two closed doors | reduces-to | - | If your first pick is wrong, the car must be behind one of the two closed doors, because the host never opens it.
typed_3: share | two closed doors | - | = | half of three quarters | In the wrong-pick case a blind switch to one of the two closed doors finds the car half the time, so the win share is half of three quarters.
---

CHAIN by duelist B
1. 🚪 (root) — Given: there are four doors, with one car and three goats behind them.
2. 🙋 (root) — Given: you pick one door at the start.
3. 🎩 (root) — Given: the host knows where the car is, opens one of your other three doors to show a goat, and then offers a switch to one of the two remaining closed doors.
4. ❓ (← 1, 2, 3) — Asked: the chance of winning the car if you switch to one of the two remaining closed doors, which differs from the familiar version where only one door is left to switch to.
5. 🎲 (← 1, 2) — Before any reveal the car is equally likely to be behind any door, so your pick is right one time in four and wrong three times in four.
6. ✅ (← 5) — In the case where your pick is right, the car is behind it, so both remaining closed doors hide goats and any switch loses.
7. ❌ (← 5) — In the case where your pick is wrong, the car is behind one of the three other doors.
8. 🔦 (← 3, 7) — In that wrong-pick case the host must avoid the car, so the car is never the opened door and must sit behind one of the two closed doors.
9. 🪙 (← 8) — Of those two closed doors one hides the car and one a goat, and nothing tells you which, so your switch is a blind choice that hits the car half the time.
10. 🧩 (← 5, 6) — The right-pick case adds nothing to the switching wins, so every win comes from the wrong-pick case.
11. 🥧 (← 7, 9, 10) — The wrong-pick case happens three times in four, and within it the switch wins half the time, so the win share is half of three quarters.
12. 👀 (← 6, 9) — Self-check: the right-pick case has two goat doors and the wrong-pick case has one car door and one goat door, so no case is double counted or missing.
13. 🏆 (← 4, 10, 11) — Switching to one of the two closed doors therefore wins with chance three in eight.

LANDMARKS:
- If your first pick is right, which happens one time in four, every switch loses.
- If your first pick is wrong, the car must be behind one of the two closed doors, because the host never opens it.
- In the wrong-pick case a blind switch to one of the two closed doors finds the car half the time, so the win share is half of three quarters.
ANSWER: 3/8
