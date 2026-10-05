---
id: 001
question: olympic-pool
title: Pool and lifetime measured in tanker loads
strategy: common-unit
contributor: claude-sonnet-4.5 (duelist B)
date: 2026-10-05
depth: 1
referee: opus/v1
criterion: v1
verdict: VALID
note: Accepted under the ruling B had been given that a chain rejected on form did not use up its landmarks; the rule was then changed (see REFEREE.md §3). Structurally the same route as attempt 001.
typed_1: size | olympic pool volume | - | ≈ | tanker load | The pool holds close to a hundred road tanker loads.
typed_2: size | lifetime drinking total | - | ≈ | tanker load | A normal person's whole lifetime of drinking is only about one or two tanker loads.
typed_3: size | olympic pool volume | lifetime drinking total | ≫ | lifetime drinking total | Matching the pool would take dozens of lifetimes of drinking.
typed_4: bound | extreme lifetime drinking total | olympic pool volume | ≪ | tanker load | Even an extreme drinker reaches only a handful of tankers.
---

1. 🏊 (root) — Given: an Olympic pool is a huge tank, about fifty metres long and two metres deep. It holds a few million litres.
2. 🥤 (root) — Given: a person drinks roughly a couple of litres of water a day.
3. 🧓 (root) — Given: a long lifetime is around eighty years.
4. 🚛 (← 1) — A road tanker truck holds tens of thousands of litres. The pool therefore fills close to a hundred such tankers, which is a long convoy.
5. 🗓️ (← 2, 3) — Daily sips repeated across eighty years add up to tens of thousands of litres in total, a number that is large but finite.
6. 🚚 (← 5, 4) — That lifetime total is about one or two tanker loads. Seen this way, one person's whole life of drinking fits in a single tanker or two.
7. 🚛🚛 (← 1, 4, 6) — Set against a convoy of nearly a hundred tankers, one or two loads is a tiny share of the pool.
8. 🤪 (← 2) — A hugely thirsty person might drink three or four times the usual amount, but that is the most a body can plausibly sustain.
9. 🚚🚚 (← 6, 8) — Even the thirsty person's lifetime total is only a handful of tankers, still a small slice of the convoy.
10. 👀 (← 7, 9) — Self-check: even the extreme drinker falls far short, so the verdict does not depend on an ordinary lifestyle.
11. ⏳ (← 7, 10) — Matching the pool would take dozens of whole lifetimes lined up one after another.
12. 🚫 (← 10, 11) — So no single person could drink a pool's worth of water in one lifetime.
13. 🔢 (← 7, 11, 12) — The pool is bigger by a factor in the tens, about forty.

LANDMARKS:
- The pool holds close to a hundred road tanker loads.
- A normal person's whole lifetime of drinking is only about one or two tanker loads.
- Matching the pool would take dozens of lifetimes of drinking.
- Even an extreme drinker reaches only a handful of tankers.

ANSWER: No; the pool is bigger by roughly 40 times.
