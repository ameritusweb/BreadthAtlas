# Referee specification — v2

Changes from v1 (2026-10-05, evening): **simulation in words counts as calculation** (§1); routes
judged under v1 keep their `criterion: v1` stamp and are re-judged under v2 where the change bites.

Every submitted chain receives exactly one verdict: **VALID**, **WRONG**, **DUPLICATE** or
**ILL-FORMED**. Checks are applied in the order below; the first failure is the verdict.

## 1. Form (ILL-FORMED if any fails)

- At least ten emoji.
- Every emoji that is not a **root** carries a parent tag `(← k, …)` naming one or more earlier emoji.
  A parent need not be the immediately preceding emoji; branches may split and merge.
- An emoji may be a root only if it states a **given**: a premise of the problem or a factual premise
  from general knowledge that the chain relies on (pool size, daily intake, lifespan, a physiological
  rate). Roots are marked `(root)`. Any other unparented emoji is a form failure.
- Every emoji has a one-sentence explanation of what it contributes. An emoji that does no work in the
  argument is a form failure — but whether a step does work is semantic, so the code checker only
  *reports* steps that no later step cites, and the referee rules. A stated partial conclusion ("rail 9
  holds L"), a self-check written in the explanation, 👀 and ❓ all do work; a decorative step does not.
  (Changed after the v2 ladder games, where every structurally sound chain was auto-failed for an
  uncited conclusion step.)
- **Self-contained.** The chain opens with its givens as roots, then exactly one ❓ step, parented to
  the givens, stating what is asked — including anything that departs from a familiar version of the
  problem — and only then the argument. (Added after the blind-read test showed that chains encoding
  only the argument are read as the nearest famous problem; routes 001–003 of `olympic-pool` predate
  this rule and are kept as form-v1.)
- After the chain: two to four **landmarks**, the intermediate claims the route passes through, in
  plain words. The answer comes last.
- **No calculation.** No equations, arithmetic, code, or multiplying stated numbers. Rough magnitudes
  may be stated in words by comparison ("a bathtub a week", "a lifetime is a few thousand weeks") and
  two magnitudes may be set against each other ("tens of thousands against a few hundred"). What the
  code checker flags is *numerals combined by an operator with a stated numeric result* ("10 times 100
  is 1000", "= 64", "80 years x 365 days gives 29200"); dimensions ("8×8 board"), fractions ("2/3")
  and prose uses of "equals" are values, not calculation. Worded arithmetic without numerals ("ten
  times a hundred is a thousand") passes the code check and is left to the referee's judgement.
- Precedent (cube-three-colours, 2026-10-05): a Burnside chain that raises the colour count to each
  cycle count, weights by rotation class, totals to 1368 and divides by 24 is calculation in words,
  ILL-FORMED. Perceptual counting of orbits by class (colour multiset, pair types, period) is not.
- **No simulation (v2).** Writing out the intermediate state of a system step by step — the row of
  tokens after rung 30, the board after move 12, the seat map after passenger 40 — is calculation in
  words and is ILL-FORMED. A landmark on a state-tracking question must be *structural*: a symmetry,
  an invariant, a decomposition into independent parts, a cancellation, a bound. "After rung 30 the row
  is D A C E H B F G" is a snapshot, not a landmark; "the lower half mirrors the upper half, so they
  cancel except for the middle rung" is a landmark. Tracing *two* objects through a structure to find
  which ones meet is allowed once the structure has been established; tracing all of them is simulation.
- Conventions: a side branch ending in 👀 is a self-check; a merge into 💥 is a contradiction.

## 2. Soundness (WRONG if any fails)

- Each step follows from the parents it names.
- Each factual claim is true to the precision the chain uses it at. A loose magnitude is fine; a claim
  that is off by a category is not (the pilot's "a small town" for forty people was WRONG).
- The final answer is correct within the question's stated tolerance.
- The chain answers the question asked, not a neighbouring one (counting all household water use
  instead of drinking is WRONG unless the chain returns to drinking alone).

## 3. Novelty (DUPLICATE if fails) — uniqueness criterion v1

- Two chains are the same route if their landmark sets coincide in substance. Wording, emoji choice
  and step order are ignored.
- A chain is new only if at least one of its landmarks is a claim no earlier **accepted** chain passed
  through. Only VALID chains bind the frontier. Rejected chains' landmarks are recorded in
  `landmarks.md` as data but do not bar a later chain on the same route. (v2.1, after two incidents on
  the ladders: first a correct route barred because its first player failed a form technicality, then
  a correct, well-formed chain ruled DUPLICATE of a chain the referee had just ruled WRONG. The archive
  measures breadth of *valid* routes; a route is not spent until someone has actually established it.)
- **Changing the yardstick is not a new route.** Measuring both quantities in a different container,
  vehicle, body, or unit of running time, then comparing, is the same route as any earlier chain that
  measured both quantities in a common unit and compared. (Pilot rulings: bathtubs, tanker loads,
  body-fulls and tap-time were one route.)
- A landmark that only asserts novelty ("this comparison is different from the others") makes no claim
  about the problem and carries no weight.
- A landmark that restates the final factor in other words ("it would take dozens of lifetimes") is
  not new if the factor was already reached.

Resolution note: v1 is deliberately coarse. A finer criterion that distinguished volume-yardsticks
from time-yardsticks would have accepted the pilot's tap-time chain. Breadth figures are only
comparable under the same criterion version.

### Empirical duplicates that outperform (so-answer-quality, v2.1)

When novelty is decided by margin correlation, a chain can duplicate an accepted route *and* reach
the verdict better (the GBM over all families: ρ 0.86 with the quality head, accuracy 0.766 vs
0.653). It is still the same mechanism — but a better execution of it. Rule: a duplicate that beats
the route it duplicates by ≥ 0.05 accuracy **supersedes** it as the route's best instance: the route's
stored margins and recorded accuracy update, the superseding chain is filed under `attempts/` with
`verdict: DUPLICATE` and `supersedes: route NNN`, and breadth is unchanged. The same principle
applies by analogy on game questions: a cleaner line for an established mechanism is the mechanism's
best instance, not a new route.

## 4. Challenges

A player may, instead of submitting a chain, challenge the most recent accepted route by naming a
specific step and the flaw. The referee rules **SUCCEEDS** (the flaw is real: the route moves to
`attempts/`, its landmarks' novelty re-opens, the challenger is credited) or **FAILS** (the challenger
is recorded as having lost the round). A challenge must name a step; "this seems loose" is not a
challenge.

## 5. Output

```
VERDICT on <route or challenge>: VALID | WRONG | DUPLICATE | ILL-FORMED | SUCCEEDS | FAILS
REASON: one or two sentences; name the step for WRONG/ILL-FORMED, the earlier route and shared
        landmarks for DUPLICATE, the new landmark(s) for VALID
ROUTE: a 5–10 word label for the line of reasoning
STRATEGY: the catalogue entry it instantiates, or "new" with a proposed name
```

## 6. Referee conduct

- Keep and publish the running landmark list (`landmarks.md`); every played chain's landmarks are
  appended, with the chain's verdict.
- Rulings are consistent across a question's history. If the referee discovers it has applied two
  readings of a rule (the pilot did, on whether rejected chains' landmarks count), the player who
  relied on the earlier reading keeps the benefit, and the rule is clarified for all later chains.
- A referee upgrade is a new version; the archive is re-judged under it before new routes are accepted.
