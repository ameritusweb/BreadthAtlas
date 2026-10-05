---
id: 003
question: birthday-months
title: Average exceeds one, so the fullest month holds two
strategy: new: max-at-least-mean
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 3
referee: opus/v1
criterion: v1
verdict: VALID
reason: The chain is sound and reaches the exact answer, 1. Its new landmarks are that twenty-three people spread over twelve months average nearly two per month, and that the fullest month must hold at least the average and so, in whole people, at least two. No earlier chain used this averaging argument: route 001 filled the months one by one, and route 002 multiplied shrinking chances.
typed_1: share | twenty-three people | birth months | ≫ | twelve | Spread evenly over twelve months, twenty-three people average nearly two per month, which is more than one.
typed_2: bound | fullest month | twenty-three people | exists | twelve | The fullest month holds at least the average, and since headcounts are whole numbers, at least two people.
typed_3: state | shared birth month | every arrangement | invariant | certainty | This holds for every possible set of birth months, so a shared month is certain.
---

CHAIN by duelist A
1. 🧑‍🤝‍🧑 (root) — Given: twenty-three people are in a room.
2. 📅 (root) — Given from general knowledge: a year has exactly twelve calendar months, and each person is born in exactly one of them.
3. ❓ (← 1, 2) — Asked: what is the probability that at least two of the twenty-three share a birth month? This is the month version, not the familiar day-of-year birthday problem.
4. 🗄️ (← 2) — Treat each month as a bucket, so there are twelve buckets. Each person's birth month drops them into exactly one bucket.
5. 🍰 (← 1, 4) — Share the crowd out evenly across the buckets. The average bucket then holds nearly two people, which is more than one.
6. 🔝 (← 5) — The fullest bucket can never hold fewer than the average bucket. If every bucket were below average, the whole crowd would not fit.
7. 🪜 (← 6) — People come in whole numbers, and the average is above one. So the fullest month must hold at least two people.
8. 🤝 (← 7) — Two people in the same month bucket means a shared birth month exists.
9. 🔒 (← 6, 8) — The averaging argument never used any particular birth dates. It holds for every possible set of births, so no arrangement escapes a shared month.
10. 🎯 (← 8, 9) — An event that holds in every possible arrangement is certain, so its probability is one.
11. 👀 (← 3, 10) — Self-check: this is about months, not days. The roughly even-odds result at twenty-three people belongs to days, and does not apply here.

LANDMARKS:
- Spread evenly over twelve months, twenty-three people average nearly two per month, which is more than one.
- The fullest month holds at least the average, and since headcounts are whole numbers, at least two people.
- This holds for every possible set of birth months, so a shared month is certain.

ANSWER: 1 (100%, certain)
