---
id: 001
question: monty-five-doors
title: Conserve total chance, then split leftover symmetrically
strategy: new: conserve-and-split
contributor: sonnet (duelist A)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: DUPLICATE
reason: This is the same route as route 001. The first landmark here (my door keeps a fifth, the opened door has none, so the three closed doors hold four fifths) matches route 001 landmarks 1–2 in substance. The second (an equal symmetric split, so one target gets a third) matches route 001 landmarks 3–4; calling it "adding up to certainty" instead of "chance moving over" is only a change of wording.
typed_1: share | the three closed doors | all the weight | = | four fifths | All door chances must add up to certainty: my door keeps one fifth and the opened door has none, so the three closed doors hold the remaining four fifths.
typed_2: symmetry | a single switch target's chance | the three closed doors | = | one in three | That leftover is divided equally among the three closed doors by symmetry, so one switch target gets a third of it.
---

CHAIN by duelist A
1. 🚪 (root) — Given: there are five doors, one hiding a car and four hiding goats.
2. 🎯 (root) — Given: I first pick one door.
3. 🧑‍🎤 (root) — Given: the host knows where the car is and opens one of the other four doors, always a goat, never my door and never the car.
4. 🔀 (root) — Given: I switch to one of the three other closed doors, with no reason to prefer any of them.
5. ❓ (← 1, 2, 3, 4) — Asked: the probability I win the car if I switch. This differs from the familiar version in that there are five doors and I must choose one of three closed doors, not one.
6. 🎲 (← 1, 2) — At the start every door is equally likely to hide the car, so my door holds a small fifth of the certainty.
7. 🛡️ (← 3, 6) — The host never opens my door and never shows the car, so his reveal cannot tell me anything about my door. My door stays at its fifth.
8. 🕳️ (← 3) — The opened door is known to be a goat, so it holds no chance of the car at all.
9. 🧮 (← 1, 8) — Exactly one car exists, so the chances across all five doors must together make up certainty, with nothing lost and nothing extra.
10. 🥧 (← 7, 8, 9) — My door holds a fifth and the opened door holds nothing. Whatever certainty remains must sit on the three closed doors, which is four fifths of it.
11. ⚖️ (← 3, 4) — The host's rule gives no door among the three closed ones any special status, so by symmetry they hold equal shares.
12. 🍰 (← 10, 11) — Splitting the remaining four fifths into three equal shares gives each closed door the same slice, a third of four fifths.
13. 🏁 (← 5, 12) — Switching to one closed door wins with the chance of that one slice, which is four fifteenths.
14. 👀 (← 7, 13) — Self-check: this beats staying at one fifth, and it is below all three closed doors together at four fifths, so it lands in the right range.

LANDMARKS:
- All door chances must add up to certainty: my door keeps one fifth and the opened door has none, so the three closed doors hold the remaining four fifths.
- That leftover is divided equally among the three closed doors by symmetry, so one switch target gets a third of it.

ANSWER: 4/15
