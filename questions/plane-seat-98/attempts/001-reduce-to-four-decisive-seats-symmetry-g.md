---
id: 001
question: plane-seat-98
title: Reduce to four decisive seats, symmetry gives three-quarters
strategy: new: decisive-seat-reduction
contributor: sonnet (duelist B)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: DUPLICATE
reason: Chain 2 is the same route as route 001. Its "collapse to a four-seat plane" is route 001's reduction to the decisive seats (landmark 1). Its "single uniform choice among four seats" is route 001's symmetry over which decisive seat is taken first (landmark 2, which step 8 states almost word for word). Its "only seat 98 is bad" is route 001's one case in four (landmark 3). Deleting passengers who sit in their own seat is only how the reduction is reached, not a new claim about the problem.
typed_1: reduction | hundred-seat plane | four-seat plane | reduces-to | - | Passengers who sit in their own seat can be deleted, so the hundred-seat plane collapses to a four-seat plane of the first passenger and passengers 98, 99 and 100.
typed_2: symmetry | first passenger's pick | decisive seats | invariant | - | In the collapsed plane, the first passenger's single uniform choice among four seats decides everything.
typed_3: share | passenger 98 displaced | decisive seats | reduces-to | one case in four | Only the pick of seat 98 displaces passenger 98, and the other three picks leave them in their seat.
---

CHAIN by duelist B
1. ✈️ (root) — One hundred passengers board a full plane in order, one seat each.
2. 🎲 (root) — The first passenger sits in a random seat, and each later passenger takes their own seat if it is free, otherwise a random free seat.
3. ❓ (← 1, 2) — What is the probability that passenger 98, the third-to-last, ends up in their own seat?
4. 🙂 (← 2) — A passenger whose own seat is free simply sits there, so they change nothing for anyone else.
5. 🧩 (← 4) — Passengers who sit in their own seat can be deleted from the story. Only the displaced passengers and their random choices shape what happens.
6. 🔍 (← 2, 5) — Whenever a random chooser picks among the free seats, the only picks that matter to passenger 98 are seat 1, seat 98, seat 99 and seat 100. Any other pick just displaces someone who then chooses again in the same way.
7. 🗜️ (← 5, 6) — So the hundred-seat plane collapses to a four-seat plane with only the first passenger, passenger 98, passenger 99 and passenger 100. The first passenger's one random choice stands in for the whole chain of displacements.
8. 🪑 (← 7) — In the small plane the first passenger picks uniformly among the four seats. The first of the four relevant seats to be hit in the big plane is hit with the same fairness.
9. 🏠 (← 8) — If the pick is the first passenger's own seat, nobody is displaced, so passenger 98 is seated correctly.
10. ⏭️ (← 8) — If the pick is seat 99 or seat 100, that owner boards after passenger 98, so seat 98 is still free when passenger 98 boards.
11. 💺 (← 8) — If the pick is seat 98, passenger 98 is displaced. This is the only bad case.
12. ⚖️ (← 9, 10, 11) — Three of the four equally likely picks are good for passenger 98 and only one is bad, so passenger 98 is seated correctly three times out of four.
13. 👀 (← 12) — Self-check: collapsing the same way for the last passenger gives a two-seat plane, so one half, which matches the known answer.

LANDMARKS:
- Passengers who sit in their own seat can be deleted, so the hundred-seat plane collapses to a four-seat plane of the first passenger and passengers 98, 99 and 100.
- In the collapsed plane, the first passenger's single uniform choice among four seats decides everything.
- Only the pick of seat 98 displaces passenger 98, and the other three picks leave them in their seat.
ANSWER: 3/4
