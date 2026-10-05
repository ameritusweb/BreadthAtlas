---
id: 002
question: monty-four-doors
title: Your door stays fixed; closed doors split the rest
strategy: part-of-whole
contributor: sonnet (duelist B)
date: 2026-10-05
referee: opus/v1
criterion: v1
verdict: DUPLICATE
reason: The chain's landmarks match route 001 in substance: "your door keeps one-in-four because the reveal was guaranteed" is route 001's landmarks 1–2 (your pick holds one in four, and the reveal leaves the group's chance unchanged); "the opened door's quarter is handed over to the two closed doors, which split it equally" is route 001's landmarks 2–3 (the group's chance concentrates on the two closed doors and is split equally, as the chain's own step 10 states). Its third landmark ("own quarter plus half the opened door's quarter, which is three eighths") restates the three-eighths already reached by route 001 in other words, so it carries no novelty.
typed_1: invariant | original pick | host's reveal | invariant | one in four | Your door keeps its one-in-four chance because the host's reveal was guaranteed whatever it hides, so the reveal says nothing about your door.
typed_2: reduction | opened door | two closed doors | reduces-to | one quarter | The opened door's lost quarter is handed over to the two closed doors, which split it equally.
typed_3: share | two closed doors | - | = | three in eight | Each closed door ends with its own quarter plus half of the opened door's former quarter, which is three eighths.
---

CHAIN by duelist B
1. 🚪 (root) — Given: there are four doors, with one car and three goats behind them.
2. 🙋 (root) — Given: you pick one door at the start.
3. 🎩 (root) — Given: the host knows where the car is, opens one of your other three doors to show a goat, and then offers a switch to one of the two remaining closed doors.
4. ❓ (← 1, 2, 3) — Asked: the chance of winning the car if you switch to one of the two remaining closed doors, which differs from the familiar version where only one door is left to switch to.
5. 🎲 (← 1, 2) — Before any reveal the car is equally likely to be behind any door, so each door, including yours, holds it one time in four.
6. 🛡️ (← 3) — The host never touches your door and can always find a goat among the other three, so the reveal would have happened whatever your door hides.
7. 🧱 (← 5, 6) — Because the reveal was guaranteed either way, it tells you nothing about your own door, which therefore keeps its one-in-four chance.
8. 🪦 (← 3) — The opened door is shown to be a goat, so the quarter it started with is now empty.
9. 🎁 (← 5, 7, 8) — Your door keeps one quarter and the opened door holds none, so the rest of the certainty, three quarters, lies on the two closed doors, which have taken over the opened door's lost quarter.
10. 🪞 (← 3, 9) — Nothing separates the two closed doors from your viewpoint, so they share that three-quarter total equally.
11. 🍰 (← 9, 10) — Each closed door ends up with its own starting quarter plus half of the opened door's former quarter, which makes it three eighths.
12. 👀 (← 7, 11) — Self-check: your door's quarter plus two closed doors holding three eighths each fills the whole certainty, with nothing lost or double counted.
13. 🏆 (← 4, 11) — Switching to one of the two closed doors therefore wins with chance three in eight.

LANDMARKS:
- Your door keeps its one-in-four chance because the host's reveal was guaranteed whatever it hides, so the reveal says nothing about your door.
- The opened door's lost quarter is handed over to the two closed doors, which split it equally.
- Each closed door ends with its own quarter plus half of the opened door's former quarter, which is three eighths.
ANSWER: 3/8
