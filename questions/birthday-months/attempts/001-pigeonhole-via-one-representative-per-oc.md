---
id: 001
question: birthday-months
title: Pigeonhole via one representative per occupied month
strategy: new: pigeonhole-witness
contributor: sonnet (duelist B)
date: 2026-10-05
referee: opus/v1
criterion: v1
verdict: DUPLICATE
reason: The chain is sound, but it takes the same route as route 001. "At most twelve representatives, so with twenty-three some are not representatives" is route 001's landmark 1: only twelve months, and twenty-three people exceed that. "A non-representative's month already has a different person in it" is route 001's landmark 2 in other words: once the twelve months are used up, the extra person has no new month. "Certain for any set of birth months" repeats route 001's landmark 3 and route 003's landmark 9.
typed_1: bound | representatives | twenty-three people | ≪ | twelve | Choosing one representative for each month that appears gives at most twelve representatives, so with twenty-three people some are not representatives.
typed_2: construction | non-representative | representative | exists | - | Every non-representative was born in a month that already has a representative, a different person, so the two of them share a month.
typed_3: state | shared birth month | every arrangement | invariant | certainty | This works for any set of birth months, so a shared month is certain.
---

CHAIN by duelist B
1. 🧑‍🤝‍🧑 (root) — Given: twenty-three people are in a room.
2. 📅 (root) — Given from general knowledge: a year has exactly twelve calendar months, and each person is born in exactly one of them.
3. ❓ (← 1, 2) — Asked: what is the probability that at least two of the twenty-three share a birth month? This is the month version, not the familiar day-of-year birthday problem.
4. 🎖️ (← 2, 3) — For every month that appears among the birth months in the room, appoint one representative: a person born in that month. Each appearing month gets exactly one representative.
5. 🔢 (← 2, 4) — There is at most one representative per month, so there are at most twelve representatives in total.
6. 🧮 (← 1, 5) — Set the crowd against the representatives: twenty-three people is far more than twelve. So many people, at least nearly half the room, are not representatives.
7. 🙋 (← 6) — Pick any one person who is not a representative.
8. 🔗 (← 4, 7) — That person's birth month appears in the room, so it has a representative. That representative is a different person, because the one picked is not a representative.
9. 🤝 (← 7, 8) — The picked person and their month's representative are two different people born in the same month. So a shared month exists.
10. 🔒 (← 9) — This worked for any room of this size and any birth months, with no particular dates assumed. So every possible arrangement contains a shared month.
11. 🎯 (← 10) — An event that holds in every possible arrangement is certain, so its probability is one.
12. 👀 (← 3, 11) — Self-check: this is about months, not days. The famous roughly even-odds result at twenty-three belongs to days, and does not apply here.

LANDMARKS:
- Choosing one representative for each month that appears gives at most twelve representatives, so with twenty-three people some are not representatives.
- Every non-representative was born in a month that already has a representative, a different person, so the two of them share a month.
- This works for any set of birth months, so a shared month is certain.

ANSWER: 1 (100%, certain)
