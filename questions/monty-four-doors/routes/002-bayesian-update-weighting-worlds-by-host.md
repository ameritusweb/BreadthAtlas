---
id: 002
question: monty-four-doors
title: Bayesian update weighting worlds by host-opening likelihood
strategy: new: likelihood-weighting
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 2
referee: opus/v1
criterion: v1
verdict: VALID
reason: The chain is sound: weighting the equal priors by the host's opening likelihoods (1/3, 1/2, 1/2, 0) gives 2:3:3, so each closed door holds 3/8. Its first two landmarks are new: the host's particular opening is likelier when the car is behind a closed door than behind your door, and the worlds stand as three parts per closed door against two for yours. No earlier binding chain passed through either claim.
typed_1: rate | closed door world | original pick world | ≫ | one in two vs one in three | The host's particular opening is likelier when the car sits behind a closed door, where he had two goats to choose from, than behind your door, where he had three.
typed_2: share | closed door world | original pick world | ≫ | three parts vs two parts | Weighing equal starting chances by those likelihoods makes the worlds stand as three parts for each closed door and two parts for your door.
typed_3: share | two closed doors | - | = | three in eight | The surviving worlds total eight parts, so a given closed door holds three eighths.
---

CHAIN by duelist A
1. 🚪 (root) — Given: there are four doors with one car and three goats behind them, and you pick one door at the start.
2. 🎩 (root) — Given: the host knows where the car is, opens one of your other three doors to show a goat, then offers a switch to one of the two remaining closed doors.
3. ❓ (← 1, 2) — Asked: the chance of winning the car if you switch to one of the two remaining closed doors, which differs from the familiar version where only one door is left to switch to.
4. 🎲 (← 1) — Before anything is opened, the car is equally likely to be behind any of the four doors, so each possible world starts with the same weight.
5. 🔭 (← 2, 3) — Focus on what you actually saw, which is the host opening one particular door, and ask how likely that sighting is in each possible world.
6. 🎯 (← 2, 5) — If the car is behind your own door, the host had three goat doors to choose from, so opening this particular one is only a one-in-three event.
7. 🔀 (← 2, 5) — If the car is behind one of the two closed doors, the host had only two goat doors available, so opening this particular one is a one-in-two event, which is more likely than in the world where your door holds the car.
8. 🚫 (← 2, 5) — If the car were behind the opened door the host could not have opened it, so that world is ruled out entirely.
9. ⚖️ (← 4, 6, 7, 8) — With equal starting weights, each closed door's world is boosted over your door's world in the ratio of a half to a third, which is three parts for each closed door against two parts for your door.
10. 🧮 (← 9) — The surviving worlds together make eight parts, and a given closed door's world holds three of those eight parts.
11. 👀 (← 8, 9) — Self-check: the ruled-out world has no weight and the remaining three parts, three parts and two parts cover everything, so no world is lost or counted twice.
12. 🏆 (← 3, 10) — Switching to a given closed door therefore wins with chance three in eight.

LANDMARKS:
- The host's particular opening is likelier when the car sits behind a closed door, where he had two goats to choose from, than behind your door, where he had three.
- Weighing equal starting chances by those likelihoods makes the worlds stand as three parts for each closed door and two parts for your door.
- The surviving worlds total eight parts, so a given closed door holds three eighths.

ANSWER: 3/8
