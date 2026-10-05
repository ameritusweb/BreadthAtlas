# Landmark schema — v2 (implemented 2026-10-05 evening; reports, does not yet decide)

Status: the referee now emits typed landmarks for every judged chain (`play.py` referee prompt), they
are stored as `typed_N:` frontmatter lines on route files, `scripts/type_landmarks.py` back-fills older
routes, and `LEADERBOARD.md` shows breadth at R0 and R2 beside the referee's own count. Route identity
is still *decided* by the referee's DUPLICATE verdict; the typed columns exist to be compared against
it. When they agree over enough routes, the decision moves to code. R1 is defined below but not yet
reported.

Criterion v1 decides route identity by whether landmark *sets coincide in substance*, as judged by the
referee. Two cases from the first games show why that is not enough:

- `olympic-pool`: bathtubs, tankers, body-fulls and tap-time were ruled one route (yardstick change);
  the ruling is right but rests on the referee abstracting "yardstick" by itself.
- `plane-seat-99`: routes 001 and 002 are the same symmetry argument framed as *state when passenger 99
  boards* versus *the relay process*; the referee accepted both, noting the closeness. Under a stricter
  reading they are one route. Breadth is 2 or 3 depending on a judgment nobody wrote down.

The fix is to make the referee emit landmarks in a typed form, so identity is decided by a rule, and
the rule can be applied at more than one resolution.

## Typed landmark

```
landmark := { kind, subject, object?, relation?, yardstick?, text }
kind      ∈ { size, rate, limit, share, structure, symmetry, state, construction, obstruction }
subject   the thing the claim is about (pool, lifetime-drinking, seat-99, top-ring, …)
object    what it is compared to or placed in (lifetime-drinking, household-use, …)
relation  ∈ { ≈, ≫, ≪, =, ∈, bijects, alternates, invariant, forbids, exists }
yardstick the unit or lens the claim is expressed in (tanker, bathtub, tap-day, body-full, …)
text      the plain-words landmark as written
```

Examples:

| text | kind | subject | object | relation | yardstick |
|---|---|---|---|---|---|
| The pool is about a hundred tanker loads. | size | pool | — | ≈ | tanker |
| A lifetime of drinking is one or two tanker loads. | size | lifetime-drinking | — | ≈ | tanker |
| Drinking the pool would take a hundred litres a day. | rate | required-intake | — | ≈ | litres/day |
| The kidney caps intake at a few tens of litres a day. | limit | body | required-intake | forbids | litres/day |
| Drinking is a hundredth of household use. | share | drinking | household-use | ≈ | — |
| Seats 1, 99, 100 are symmetric until one is hit. | symmetry | decisive-seats | — | invariant | — |
| Top points pair vertically with bottom points. | structure | point-set | — | bijects | — |

## Identity at three resolutions

- **R0 (coarse, = criterion v1):** drop `yardstick` and `text`; two landmarks are the same if
  (kind, subject, object, relation) match. Bathtubs and tankers collapse; so do "state at boarding" and
  "relay process" if both reduce to (symmetry, decisive-seats, —, invariant).
- **R1 (medium):** also distinguish `kind` ∈ {state, construction} framings — the plane's two routes
  separate, the pool's yardstick costumes still collapse.
- **R2 (fine):** keep `yardstick` — every costume is its own route. Not a breadth measure of
  intuition; useful only to count how many costumes an attractor route attracts.

Breadth is reported per resolution. The atlas's headline number is R0; the snap/attractor analysis
uses R2 counts.

## How it enters the pipeline

1. ☑ Referee output carries a `TYPED LANDMARKS:` block (one line per landmark), with the question's
   already-typed vocabulary shown so subject/object phrases are reused.
2. ☑ `play.py` stores plain landmarks in the body and typed ones as `typed_N` frontmatter.
3. ◐ `build_leaderboard.py` reports breadth at R0 and R2 from typed landmarks next to the referee's
   count. `ceiling.py` and the DUPLICATE decision still use the referee's verdict.
4. ☑ `scripts/type_landmarks.py` back-fills existing routes in depth order.

Validation (2026-10-05, 63 judged chains incl. duplicates): R0 83 %, R2 81 % agreement with the
referee; zero over-merges (no VALID route typed as a duplicate); all misses are synonym drift in
subject/object phrases. The yardstick rule works when phrases are reused (tap-time collapses at R0,
separates at R2).

Next step — **controlled subject vocabulary**: each question lists its canonical subjects/objects
(e.g. olympic-pool: `olympic pool volume`, `lifetime drinking total`, `daily water intake`,
`required daily intake`, `household water use`, `extreme drinker`); the typer must choose from the
list or propose an addition the referee approves. Until then typed identity is used as a filter
(typed-DUP ⇒ DUP) and the referee keeps the decision.
