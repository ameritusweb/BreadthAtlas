---
id: 001
question: birthday-months
title: Pigeonhole contradiction: twelve months cannot hold twenty-three distinctly
strategy: new: pigeonhole-certainty
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 1
referee: opus/v1
criterion: v1
verdict: VALID
reason: Each step follows from its parents, and the answer of exactly 1 is correct by pigeonhole. Because the frontier is empty, all three landmarks are new: twenty-three people exceed twelve months, distinct months run out by the twelfth person, and a shared month occurs in every arrangement so the event is certain.
typed_1: size | twenty-three people | birth months | ≫ | twelve | There are only twelve possible birth months, and twenty-three people exceed that.
typed_2: obstruction | distinct birth months assignment | thirteenth person | forbids | twelve | Assuming all months are different would use up the twelve months by the twelfth person (pigeonhole), leaving the thirteenth with no new month.
typed_3: state | shared birth month | every arrangement | invariant | certainty | A shared month occurs in every possible arrangement, so the event is certain, with no need to weigh likelihoods.
---

CHAIN by duelist A
1. 🧑‍🤝‍🧑 (root) — Given: twenty-three people are in a room.
2. 📅 (root) — Given from general knowledge: a calendar year has exactly twelve months, and everyone is born in exactly one of them.
3. ❓ (← 1, 2) — Asked: what is the probability that at least two of the twenty-three share a birth month? This is the month, not the day-of-year, as in the familiar birthday problem.
4. 🗄️ (← 2) — Picture twelve labelled boxes, one per month. Each person's birth month puts them in exactly one box.
5. 🚶 (← 1, 4) — Place the people into the boxes one at a time, each into the box for their own month.
6. 🧪 (← 2, 5) — Suppose, for contradiction, that nobody shares a month. Then every person occupies a different box, so the twelve boxes are used up after twelve people.
7. ⚖️ (← 1, 6) — Set the crowd against the boxes: twenty-three people is far more than twelve boxes, nearly double.
8. 🚪 (← 6, 7) — After the boxes are all taken, any further person must go into a box that is already occupied.
9. 💥 (← 6, 8) — This contradicts the supposition that everyone has a different month, so the supposition cannot hold.
10. 🔒 (← 9) — Therefore every possible set of birth months for this room contains a shared month. No arrangement avoids it, however unlikely it looks.
11. 🎯 (← 10) — An event that happens in every possible arrangement is certain, so its probability is the maximum, one hundred percent.
12. 👀 (← 3, 11) — Self-check: the question is about months, not days. The famous twenty-three, about even odds, applies to days, and does not apply here, where certainty holds.

LANDMARKS:
- There are only twelve possible birth months, and twenty-three people exceed that.
- Assuming all months are different would use up the twelve months by the twelfth person (pigeonhole), leaving the thirteenth with no new month.
- A shared month occurs in every possible arrangement, so the event is certain, with no need to weigh likelihoods.

ANSWER: 1 (100%, certain)
