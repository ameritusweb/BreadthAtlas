---
id: 003
question: plane-seat-98
title: Middle pick restarts problem; induct down to four seats
strategy: new: restart-recursion-induction
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 3
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is correct. Step 9 states the result for any number of middle passengers without spelling out the weighted average, but the claim is true: each restart is a uniform pick among the same four decisive seats or another restart, so the bad chance stays one in four. No earlier binding chain uses the restart recursion (landmark 1) or the claim that the answer does not depend on the number of middle passengers (landmark 2), although landmark 3 repeats attempt 001's four-seat collapse.
typed_1: reduction | first passenger's pick | restarted problem | reduces-to | - | Splitting on the first passenger's pick, a pick in the middle just restarts the same problem with a displaced passenger as the new chooser.
typed_2: symmetry | passenger 98 displaced | middle passengers | invariant | - | The chance that passenger 98 is displaced does not depend on how many passengers sit between the chooser and passenger 98.
typed_3: share | passenger 98 displaced | decisive seats | reduces-to | one case in four | With no middle passengers the plane has four seats, and the bad pick is one of four.
---

CHAIN by duelist B
1. ✈️ (root) — One hundred passengers board a full plane in order, one seat each.
2. 🎲 (root) — The first passenger sits in a random seat, and each later passenger takes their own seat if it is free, otherwise a random free seat.
3. ❓ (← 1, 2) — What is the probability that passenger 98, the third-to-last, ends up in their own seat?
4. 🎬 (← 2) — Split on the first passenger's seat. Everything that follows depends on where that single random pick lands.
5. 🏠 (← 4) — If the first passenger picks their own seat 1, nobody is ever displaced, so passenger 98 is fine.
6. 🔚 (← 4) — If the first passenger picks seat 99 or seat 100, those owners board after passenger 98. Seat 98 is untouched and passenger 98 is fine.
7. 💺 (← 4) — If the first passenger picks seat 98, passenger 98 is displaced. This case is bad.
8. 🔁 (← 2, 4) — If the first passenger picks a seat from 2 to 97, that owner is displaced and chooses at random among the free seats. This is the same situation as the start, with the displaced passenger as the new "lost-pass" passenger, and seat 1 now counts as a free seat that ends the chaos.
9. 🪞 (← 8) — The restarted problem has the same four relevant seats and the same three outcomes (good, good, bad) as before, but fewer passengers in the middle. So the chance of a bad ending does not depend on how many passengers sit between the chooser and passenger 98.
10. 0️⃣ (← 7, 9) — Because the bad chance does not depend on the middle passengers, we may take the case with none. Then the plane has only the four seats 1, 98, 99 and 100, and the first passenger picks uniformly among them, so the bad pick is one of four.
11. 🧮 (← 5, 6, 10) — Three of those four equally likely outcomes leave passenger 98 in their own seat, so the answer is three quarters.
12. 👀 (← 11) — Self-check: for the last passenger the same argument leaves a two-seat plane, giving one half, the known answer.

LANDMARKS:
- Splitting on the first passenger's pick, a pick in the middle just restarts the same problem with a displaced passenger as the new chooser.
- The chance that passenger 98 is displaced does not depend on how many passengers sit between the chooser and passenger 98.
- With no middle passengers the plane has four seats, and the bad pick is one of four.
ANSWER: 3/4
