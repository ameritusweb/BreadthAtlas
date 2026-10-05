---
id: 002
question: olympic-pool
title: Required daily rate against the body's limit
strategy: rate-vs-limit
contributor: claude-sonnet-4.5 (duelist A)
date: 2026-10-05
depth: 2
referee: opus/v1
criterion: v1
verdict: VALID
typed_1: rate | daily quota to drink pool | - | ≈ | litres per day | Spreading the pool over a lifetime requires a daily quota of about a hundred litres.
typed_2: limit | kidney excretion ceiling | - | ≈ | litres per day | The kidney excretion ceiling caps sustained intake at a few tens of litres a day.
typed_3: obstruction | daily quota to drink pool | kidney excretion ceiling | forbids | litres per day | The required daily rate would cause fatal water intoxication, which contradicts the plan.
---

1. 🏊 (root) — Given: an Olympic pool holds a few million litres.
2. 🥤 (root) — Given: a person normally drinks roughly a couple of litres of water a day.
3. 🧓 (root) — Given: a long lifetime is around eighty years, which is tens of thousands of days.
4. 🗓️ (← 3) — Spreading the pool evenly over those days gives a daily quota to drink.
5. 🌊 (← 1, 4) — A few million litres shared among tens of thousands of days means the daily quota is on the order of a hundred litres, which is enormous.
6. 🧍 (← 2, 5) — That daily quota is dozens of times the normal daily intake, and the same factor describes how much bigger the pool is than a lifetime of normal drinking.
7. 🫘 (root) — Given: kidneys can excrete only about a litre an hour at best, so the body has a hard ceiling on how much water it can process.
8. ⏱️ (← 7) — Even if someone drank nonstop for every waking hour, the kidney ceiling would cap them at a few tens of litres a day.
9. 🧂 (← 8) — Drinking beyond that ceiling dilutes the blood sodium (water intoxication), which causes seizures, coma and death within days.
10. 💥 (← 5, 8) — The required hundred litres a day contradicts the physiological ceiling of a few tens of litres a day, so the plan is impossible even for an extreme drinker.
11. 👀 (← 9, 10) — Self-check: drinking the quota at a sustained rate would be fatal, not merely uncomfortable, so the conclusion is not a close call.
12. 🚫 (← 10, 11) — So no one could drink a pool's worth of water in one lifetime.
13. 🔢 (← 6, 12) — The pool exceeds a normal lifetime's drinking by a factor in the tens, about forty.

LANDMARKS:
- Spreading the pool over a lifetime requires a daily quota of about a hundred litres.
- The kidney excretion ceiling caps sustained intake at a few tens of litres a day.
- The required daily rate would cause fatal water intoxication, which contradicts the plan.

ANSWER: No; the pool is bigger by roughly 40 times.
