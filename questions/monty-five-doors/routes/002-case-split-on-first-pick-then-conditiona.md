---
id: 002
question: monty-five-doors
title: Case split on first pick, then conditional hit
strategy: new: case-split-on-first-pick
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 2
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is well-formed and contains no simulation. Its case split is structural, not a step-by-step state trace, and it reaches the correct 4/15. Its first landmark is new: switching can win only after a wrong first pick, and a right first pick makes every switch lose. Route 001 never passed through this. It moved probability onto the remaining doors instead of conditioning on whether the first pick was right.
typed_1: structure | switching winning | a wrong first pick | reduces-to | - | Switching can only win if my first pick was wrong, and a right first pick makes every switch lose.
typed_2: state | the car | the three closed doors | ∈ | - | Given a wrong first pick, the car is certainly among the three closed doors, because the host never reveals it.
typed_3: share | a single switch target's chance | the wrong-pick case's chance | = | one in three | Within that case a random closed door hits the car one time in three, so the answer is that fraction of the wrong-pick case's chance.
---

CHAIN by duelist B
1. 🚪 (root) — Given: there are five doors, one hiding a car and four hiding goats.
2. 🎯 (root) — Given: I first pick one door.
3. 🧑‍🎤 (root) — Given: the host knows where the car is and opens one of the other four doors, always showing a goat and never the car.
4. 🔀 (root) — Given: I switch to one of the three remaining closed doors, picking among them at random.
5. ❓ (← 1, 2, 3, 4) — Asked: the probability I win the car if I switch. This differs from the familiar version in that there are five doors and three closed doors to choose among, not one.
6. 🎲 (← 1, 2, 5) — Split into two cases by whether my first pick was right. It was wrong four times out of five and right one time in five, so wrong is the far more common case.
7. ❌ (← 6) — Case "first pick right": the car is behind my door, so every door I could switch to hides a goat and switching surely loses.
8. ✅ (← 3, 6) — Case "first pick wrong": the car is among the other four doors, and the host opened a goat, so the car must be behind one of the three closed doors.
9. 🎰 (← 4, 8) — In the wrong-pick case, exactly one of the three closed doors holds the car, and I choose among them at random, so I hit it one time in three.
10. 🧩 (← 7, 9) — Switching can win only in the wrong-pick case, and even there it wins only one time in three. So my win chance is one third of the wrong-pick case's chance.
11. 🏁 (← 6, 10) — The wrong-pick case has chance four fifths, so one third of it gives four fifteenths.
12. 👀 (← 11) — Self-check: four fifteenths is a bit more than staying (one fifth) and well below the wrong-pick case's four fifths. It is also under one third, as it must be, since I win only part of the time within one case.

LANDMARKS:
- Switching can only win if my first pick was wrong, and a right first pick makes every switch lose.
- Given a wrong first pick, the car is certainly among the three closed doors, because the host never reveals it.
- Within that case a random closed door hits the car one time in three, so the answer is that fraction of the wrong-pick case's chance.

ANSWER: 4/15
