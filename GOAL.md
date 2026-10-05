# GOAL — where the end state resides

This file is the fixed point. Everything else in the repo is measured against it. When a piece below
is done, mark it; when the vision changes, change this file first.

## The end state in one paragraph

A public, self-renewing archive in which every question has a growing list of genuinely different,
valid, non-calculating ways of reaching its answer — each written as an emoji chain another mind can
read, check and contest. Models and people extend the frontier by play; a versioned referee keeps the
archive honest; the archive ranks questions by richness, players by depth-weighted contribution, and
years by how far intuition has expanded. Routes abstract into strategies, and the strategy catalogue
becomes a library of ways to think that can be aimed at problems nobody has solved.

## What it is for

1. **Measure what nobody measures:** not whether a mind reaches the answer, but how many distinct ways
   it can see the problem — the breadth of its understanding — and where that breadth breaks.
2. **Never wear out:** no answer key to memorize; publishing the archive *is* the benchmark, because
   the only way to score is to add what is not already there.
3. **Map problems as well as minds:** which questions are rich, which are narrow, and how each one's
   breadth grows year over year.
4. **Keep machine progress legible and shared:** emoji chains stay human-readable; humans can play,
   challenge, and find routes machines missed. If machines ever find routes no human can follow, this
   is where it shows first.
5. **Become an approach database:** strategies that recur across unrelated questions are the ones to
   try on open problems; gaps in coverage are where to look next.

## The invariants (true at every stage, or the measurements are void)

- **No calculation in a route.** Breadth of *intuition* is the quantity; a computed route is a different
  quantity. The runner enforces form; the referee enforces the rest.
- **Published frontier.** Every played chain, accepted or not, is public; the landmarks of accepted
  chains are used up, and rejected chains stand as a record of what was tried and how it failed.
- **Frozen ruler per version.** Uniqueness criterion and referee are versioned; breadth is comparable
  only within a version; upgrades re-judge the archive before accepting new routes.
- **Depth fixed at acceptance.** A route's value reflects how much of the frontier was already taken.
- **Nothing deleted.** Failed chains mark the edge of reliable intuition and are kept as data. The
  full constraint list is all four verdict types: VALID (what works), WRONG (where reasoning breaks),
  DUPLICATE (where it collapses onto something found), ILL-FORMED (where it cannot express itself).
  A chain that re-walks a charted dead end is marked `repeats:` — the dead-end analogue of the snap
  rate. `scripts/export_dataset.py` emits the whole landscape as one JSONL for training; a model
  trained on routes alone learns the interior and never the edge.
- **Self-contained chains.** A chain depicts its givens and its question before its argument; the
  blind-read test (reconstruct the question from the emoji alone) is the check.

## Completeness, by layer

Each layer lists its done-condition. Status: ☐ not started · ◐ partial · ☑ done.

### L0 — Format and rules  ◐
- ☑ Route / attempt file format with versioned criterion and referee fields
- ☑ Referee spec v1 written from actual rulings (REFEREE.md)
- ☑ Strategy catalogue v1 (STRATEGIES.md)
- ☑ Chain grammar formalized and checked by code (`play.py: Chain.check_form`): emoji count, root
  marking, parent-tag validity, ❓ present and before the argument, idle steps (👀/❓ exempt),
  landmarks 2–4, answer last, arithmetic-with-result; pinned by `scripts/test_form.py`
- ◐ Landmark schema (LANDMARKS.md): referee emits typed landmarks (kind | subject | object | relation |
  yardstick | text) with the question's vocabulary for phrase reuse; stored as `typed_N` frontmatter;
  leaderboard reports breadth at R0 and R2 beside the referee's count; `scripts/type_landmarks.py`
  back-fills. Not yet used to *decide* DUPLICATE — the referee still rules; the schema reports.

### L1 — Play engine  ◐
- ☑ Runner: `scripts/play.py <question>` drives duelists + referee through the Claude Code CLI
  (`claude -p`, headless, no tools except Read for image questions), enforces form in code, routes
  judgment calls to the referee, writes routes/attempts/landmarks, regenerates the board
- ◐ Challenge mechanic implemented (duel mode; not yet exercised in a recorded game)
- ☑ Modes: duel, blind, extend
- ☑ Run log per game archived under `questions/<q>/games/`
- ☐ Backend abstraction (API key / other providers) so any lab can point its model at the repo
- ☑ Backend robustness: `ask()` retries with backoff; typer skips a failed call instead of aborting;
  a player that reports it could not read the image is re-asked once
- ◐ Form checker: idle steps demoted to a referee note (semantic call); challenge-text parsing and a
  `(root)` abuse check still ☐

### L2 — Question corpus  ◐ (31 of a target ≥ 50: 21 played, 2 empirical-referee questions
built, 8 curated 2026-10-05 night via `scripts/seed_expansion_batch.py` — see
EXPANDING_THE_PROBLEM_SPACE.md for the batch, the generative method and the curation workflow)
- ◐ Families represented: Fermi estimation ☑ · multi-view reconstruction ☑ (turntable, three-view) ·
  long state tracking ☑ (swap ladder, beetle) · altered-famous puzzles ☑ (plane seat 99, chessboard
  adjacent corners) · spatial ☑ (wire cube) · counting under symmetry ☐ · open problems ☑
  (balance-five-objects, with the first per-question glossary)
- ☑ Each question carries: definite answer + tolerance, `attractor`, `family`, image + key + generator
  for image questions, and `discriminator` (what a chain must depict to be distinguishable from its
  attractor) on every altered-famous and parametrized question
- ☐ Parametrized families (same question, new instance) so routes must be re-derived, not recalled
- ☐ Held-out questions for contamination checks

### L3b — Empirical referees  ◐ (scoped 2026-10-05)
- ☑ Design: `questions/warp-one-chess/SCOPE.md` — a referee that *plays*: replays a route's cited line
  on the project's own engine, checks legality and checkmate, searches Black's replies for forcedness;
  the engine is final on soundness, the model referee on mechanism and novelty
- ☑ `play.py` hook: questions with `referee_script:` run it before the model referee; `not forced` or
  `illegal` overrides the verdict to WRONG
- ☐ `scripts/warp_referee.py` (replay + mate + bounded forcedness), `warp_pick_positions.py`, board
  renderer, position set, first game

### L3c — Computable novelty  ◐ (scoped 2026-10-05)
- ☑ Design: `questions/so-answer-quality/SCOPE.md` — routes ship executable scorers over shared
  held-out answer pairs; accuracy floor 0.60 (baselines: transformer 0.679, poc4 0.661); DUPLICATE
  when per-pair margins correlate (Spearman ρ ≥ 0.80), ambiguous band 0.50–0.80 referred to the model
  referee. Domain concepts and the model's own mechanisms are one vocabulary.
- ☑ `scripts/so_referee.py` + three seed scorers; margins of valid routes stored for comparison
- ◐ Mechanism scorers over the trained poc4 components written (quality head, geo, eigen,
  triangulation, GBM-all; train-split fitting only); feature extraction running; verdicts pending
- ☑ `play.py` hook: `weak` → WRONG, `duplicate-of` → DUPLICATE, `ambiguous`/`unverified` → model referee
- ◐ First game on so-answer-quality: runner supports `tools: Read,Write` per question and tells
  players where to write scorers; held pending a decision to execute model-written scorers locally

### L3 — Referee governance  ◐
- ☑ Verdict format, order of checks, conduct rules
- ☑ Referee as a reproducible artifact: the prompt is built from REFEREE.md + question files by
  `play.py`; model and criterion recorded per route
- ☐ Audit: sample of acceptances re-judged by a stronger model or humans; disagreement rate reported
- ☑ Re-judging pipeline (`scripts/rejudge.py`, keeps originals under `attempts/superseded/`,
  honours the form version a chain was played under); used nine times on day one
- ☐ Open-problem mode: soundness + novelty only; divergence between accepted routes flagged

### L4 — Measurement  ◐
- ◐ Breadth per question (one resolution, v1); per-resolution scoring ☐
- ☐ Ceiling estimate per question (species-richness estimator over many games) with error bars;
  player breadth reported as streak ÷ ceiling
- ☑ Snap test script (`scripts/snap_test.py`): blind-read of bare chains, judged resolve / hedge /
  absorb. First result: olympic-pool routes 001–003 all ABSORB → the ❓ self-containment rule was added
- ☑ Intuition test script (`scripts/guess_test.py`): bare guess, no working, tolerance curve;
  `guess_target` set on 4 questions
- ☐ Covert-calculation detector: identity-type questions where exact answers imply computation
- ☐ Per-player profile = breadth × snap resistance × intuition curve

### L5 — Strategy layer  ◐
- ☑ Catalogue curated: 50 entries with shape, worked and failed columns (STRATEGIES.md v2 + the
  open-problem principles + the expansion batch's ten new principles); referee cites catalogue ids
- ☑ Alias table (`alias: <proposal> => <id>` lines in STRATEGIES.md) folds referee-proposed names
  into entries; `scripts/strategy_map.py` and the leaderboard canonicalize through it
- ☑ Strategy × question map (STRATEGY_MAP.md): worked / failed / untried per cell; nine strategies
  have accepted routes on more than one question (orbit-by-invariant-count on 9, explicit-construction
  on 7, part-of-whole and symmetric-absorbing-set on 4)
- ☐ Clustering on chain structure (DAG shape, 💥/👀 placement) + landmark types, not emoji glyphs
- ☐ Each strategy tagged with questions where it worked and where it was tried and failed
- ☐ Gap finder: strategies that worked on structurally similar questions but were never tried here

### L6 — Public face  ◐
- ☑ Leaderboards generated from the folders (markdown)
- ☑ Static site (`scripts/build_site.py` → `site/`): ranked questions, question-by-year grid, models
  by routes, where intuition overreached, and a page per question with every route and attempt
  (chain, verdict, reason, typed landmarks). Local files; no hosting yet
- ☐ Human submission + challenge flow with attribution
- ☐ Leaderboards: top-breadth questions · players by depth-weighted score · humans who found routes
  machines missed

### L7 — Time  ◐
- ◐ First dated snapshot taken (`snapshots/2026-10-05-*`); formal freeze of criterion v1 + referee v1
  not yet declared — the rules changed four times today, so freezing now would be premature
- ☐ Yearly re-run of the corpus with the current model generation under the frozen ruler
- ☐ Breadth curves per question; aggregate curve per year

### L8 — Approach database  ☐
- ☐ Open problems added with `status: open`
- ☐ Strategy transfer suggestions for a new or open question, ranked by cross-domain recurrence
- ☐ Map of tried / untried angles per open problem

## Order of work

1. **L1 runner** — nothing grows until play is automated.
2. **L2 corpus** — seed ≥ 20 questions across families; regenerate the untilted turntable image.
3. **Play** — populate; archive raw games.
4. **L0 landmark schema + L5 clustering** — built on real routes, not guesses.
5. **L4 ceilings and profiles** — once there are many games per question.
6. **L3 audit + L7 freeze** — declare v1 and stamp it.
7. **L6 site, L8 open problems.**

## Evidence so far

Pilot (2026-10-05, Sonnet × 2 vs Opus referee, Olympic-pool question): six turns, three genuine routes,
four costumes of the first route, one false claim introduced while reaching for novelty, one duplicate,
one form failure, zero challenges. Blind-read tests: argument shape transmits from bare emoji;
setup transmits only when depicted up front; a chain that omits the alteration is read as the famous
version. These are the first data points for L4 and the reason L0's self-contained-chain invariant
exists.

First automated games (2026-10-05, runner v1): plane-seat-99 duel produced three VALID routes in four
turns, two of which are one symmetry argument in two framings (state-at-boarding vs relay process) —
accepted under v1 and the clearest case yet that uniqueness needs a computable landmark schema.
Turntable blind: both players perceived the vertical pairing and a ten-faced prism, both read the ring
order off a single view and got a self-intersecting outline; the referee, viewing the image, named the
true order and ruled WRONG. Snap test on pool routes 001–003: 3/3 ABSORB → ❓ rule added. Guess test on
plane-seat-99 (Sonnet, 5 samples): 2/3 twice, ½ three times — a 60 % intuitive snap. Four form-checker
defects found and fixed by play, each pinned in `scripts/test_form.py`: terminal 👀 flagged as idle;
❓ flagged as idle; "equals" in prose and "8×8 board" flagged as arithmetic; units between number and
operator missed. Headless image questions: players refused to guess when the Read tool was denied
("a false claim loses the round") rather than fabricate — the right behaviour; fixed by pre-approving
Read. First valid image route: three-view-solid (player saw the drawing, counted base U-prism faces
plus step-cut additions). Referee caught a genuine symmetry gap on wire-cube attempt 001 (three-fold
rotation alone does not space six corners evenly). Chessboard: four accepted routes, several of them
distinct explicit tilings — the clearest case that "exhibit a construction" may be one strategy with
many instances, to be settled by the landmark schema (LANDMARKS.md).

First open problem (balance-five-objects, blind, 2 players, before the glossary reached the prompt):
player 1 took the attractor stack and justified it with a rigid-body fallacy the referee named exactly
(a free-standing bottle tips about its own base, whatever the combined centre of mass); player 2 found
triangulation (A-frame tents) but lost on form, with a dubious "nail ties the tents" step left unjudged.
Neither found containment (🫙). Swap-ladder: both players solved it by block decomposition and rung-by-
rung tracing — simulation in words — and neither saw the mirror structure; the no-calculation rule is
hardest to enforce on discrete state tracking. Rule change from that game: ILL-FORMED chains' landmarks
are no longer binding.

Pre-protocol baseline filed (`balance-five-objects/external/001`): Claude Fable 5.1, months earlier,
asked for "the best way" — one principle found, the second (containment) present as an aside and not
recognised as a route. Same model as the one that built this repo. The gap between "best way" and
"how many ways" is the quantity the atlas measures.

Glossary effect (balance-five-objects, blind, 3 Sonnet players, glossary live): every player left the
attractor stack — containment, triangulation, counterbalance — and every chain was WRONG: a false
physical claim in each, and two of three dropped objects to make the problem easier. The shared
vocabulary raised the breadth of *attempts* and exposed that the accuracy constraint, not the ideas,
is the binding one on physical problems. Question text tightened to forbid setting objects aside.

Opus vs Sonnet, first data point (olympic-pool, extend, 2 attempts): Opus's first attempt was a
yardstick costume (depth layer in the pool → DUPLICATE); its second was a route Sonnet never found in
seven chains — aggregate to humanity, then take one person's share (`aggregate-and-share`). Breadth
rose by one genuine route, not only by costumes.

**Turntable solved without calculation (2026-10-05, Opus, blind):** both Opus players recovered the
exact four-pointed-star prism — tips vs inner slots, inner points tracking between neighbouring tips,
the hidden corner explained by an arm, unknown angles described qualitatively from the tips — and the
referee verified every reading against the image. Two routes, both Opus; Sonnet 0 for 4 (both Sonnet
chains read the ring order off a single view). Both Opus chains were first killed by the arithmetic
detector matching "θ = 30°" in the restated givens; fixed and pinned.

Snap test after the ❓ rule (beetle, 3 routes): still 3/3 ABSORB. ❓ marks that a question is asked;
its content sits in the explanation, invisible to a bare-emoji reader. Open issue: require the asked
quantity itself to be depicted (e.g. ❓ plus the emoji of what is asked), or accept that bare-chain
readability needs the question's glossary. Not changed today.

**Resolved as criterion v2 (2026-10-05 evening):** simulation in words is ILL-FORMED; the swap-ladder
route was demoted on re-judging and both ladder instances now stand at zero routes.

**Was open issue #1 — simulation in words.** Both ladder instances were solved by writing out the token
row rung by rung (one chain was WRONG only because an intermediate row was mis-tracked); no player on
either instance saw the mirror structure. Step-by-step state bookkeeping is the calculation route for
state-tracking questions and the current rule does not exclude it. Proposed amendment for criterion v2:
*writing out intermediate states of the system counts as calculation; landmarks on state-tracking
questions must be structural (symmetry, invariant, decomposition), not positional snapshots.*

Snap resistance in chains vs guesses: on the three altered-famous questions played under the protocol
(lockers, Monty-4, birthday-months) every chain — 12 of 12 — reached the altered answer; the bare-guess
test on plane-seat-99 snapped 60 % of the time. Chains resist the attractor where intuition alone does
not. Question richness: cube-two-colours produced four valid, distinct routes in four turns with no
stumble — the widest question relative to turns played.

Open problems, second data point (barometer-building, blind, 3 Sonnet players, glossary live): two
VALID routes — pressure gradient (the attractor; 2 of 3 took it) and timed free fall — one lost on
form. First accepted routes on any open problem. Contrast with balance-five-objects (0 for 5): the
open-problem format works; what fails on the balancing question is the physics of the proposals.

Counting under symmetry is the widest family so far: cube-two-colours 4/4, necklace-six-beads 4/4 and
tetrahedron-three-colours 4/4 (including the 2-transitivity → multisets route), cube-three-colours 2
routes with a Burnside chain correctly ruled ILL-FORMED as calculation in words,
every chain correct, every route a different classification scheme (by invariant count, by run count,
by period, by rotation-then-flip). Typing weakness confirmed on the first back-filled rows: the typer
put the yardstick into the object field, so R0 will not collapse costumes until rows are re-typed under
the corrected rule (`type_landmarks.py --force`).

**Ladders under v2 (8 chains, 2 instances, after the idle rule moved to the referee):** no simulation
survived, and the chains went structural — block decomposition, rung-count parity, and (attempt 004)
the mirror cancellation itself, found on the left block. None established the answer: the parity
argument proves an odd permutation, not the single swap the chains asserted, and the mirror was never
applied to the block holding the unpaired rung. Both ladders: 0 routes, honestly. Two rule repairs
came from these games: idle steps are a referee note, not a code failure; and only VALID chains bind
the frontier (v2.1) — a WRONG chain had been barring a correct one.

**Typed-landmark identity validated against the referee (63 judged chains, 2026-10-05 evening):**
R0 83 %, R2 81 % agreement, and every disagreement is one-directional — the typer never merged two
routes the referee kept apart; it only failed to merge duplicates whose landmarks used different noun
phrases for the same thing. With phrases reused, the yardstick rule behaved as designed (the tap-time
costume collapses at R0, separates at R2). Decision: typed identity is safe as a *filter* (typed-DUP ⇒
DUP) but not yet as the decision; the residual is vocabulary drift, fixed by a controlled per-question
subject vocabulary (the glossary mechanism extended to subjects). Decision still rests with the
referee.

**Empirical referee, first act (warp-one-chess):** the self-play archive's "White wins by checkmate"
lines are games Black lost, not proofs — the referee showed P01's line is not forced (Black has a
second-ply escape). The question's premise moves from "positions from winning games" to "positions
where the win is proved by search"; the picker now keeps only proved wins. A referee that plays
corrected its own source before any player touched the question. Full search over 160 archive lines:
77 provably not forced, 83 beyond a 30 s budget, 0 proved — the self-play archive contains no provable
wins at its game-start positions, and a plain Python search cannot prove 7-ply mates in time. Position
source changed to the point three plies before each game's mate (`--tail 3`): of 2,271 such tails,
**36 were forced (1.6 %)** — in almost every self-play game Black's last move was a blunder, not a lost
position. Twelve proved mate-in-two positions admitted, each with its proof in the file; the question
is playable. **First engine-refereed game (3 Opus players, blind): 3/3 WRONG, every one caught by
the engine** — an illegal capture-then-flip at ply 1; a quiet tempo that let Black escape at ply 2; a
line that ignored Black's own flip escape. All three reached for the flip mechanic and all three
misread the position; the model referee tied each engine verdict to the exact step that broke. Zero
routes: a frontier question, and the first where the gap between "sounds right" and "is right" is
measured by a machine rather than a reading.

**Computable novelty, first run (so-answer-quality, 4,000 held-out pairs):** sheer answer length
ranks the better answer at 0.664 — 1.5 points under the transformer baseline (0.679) and level with
the NODE-flowtron variant (`poc4_large`, 0.661). Word count was ruled its costume by code (ρ = 0.96);
code share fell below the floor (0.577). Three verdicts without a referee's reading. The triangulation
pipeline's own headline (GBM over 44 geo/eigen/triangulation features, 93.5 % CV) was measured under
a different protocol; the mechanism routes will re-measure it under the referee's — GBM fitted on the
train split, margins scored on the held-out pairs — so it and length become comparable, and each
component route must also show low correlation with length to count as a mechanism of its own.

**Mechanism routes on so-answer-quality (five scorers over the trained poc4 model, train-split fitting
only, 4,000 held-out pairs):** the quality head is a second mechanism (0.653, ρ 0.42 vs length);
geometry alone (0.577) and eigen alone (0.565) are below the floor; triangulation-only is the head's
signal (ρ 0.93); the GBM over all families is the head's signal read best — **0.766**, ten points over
length — and supersedes route 002 as its best instance. Breadth 2. The protocol difference explains
the gap to the published 93.5 %: that figure cross-validated on features extracted from validation
pairs; fit on train and scored held-out, the same reader gives 0.766. New rule: an empirical
duplicate that outperforms by ≥ 0.05 supersedes the route's best instance (REFEREE.md §3).

**Snap test, ❓-era routes on the altered-famous family (lockers, Monty-4, birthday): 7/7 ABSORB.**
Readers answered the famous versions (10 lockers; "classic birthday, 23, ½"). Conclusion: the ❓
marker carries *that* a question is asked, not what distinguishes it. Rule v2.2: a chain must depict
the question's discriminator in emoji at or before ❓; the referee records `discriminator_depicted`
as a measurement so the next snap test can compare depicted against not.

**SO route 003 (player 2's recovered scorer, re-judged with the empirical step):** a field-evolution
sign vote over the `tri_evo_` components — acc 0.641, ρ 0.64 vs length (ambiguous band), accepted
by the model referee as a reader of a different component than the quality head. Breadth 3.

**First SO game (2 Opus players):** both chains sound; both failed at the tool layer — the scoped
Write rule was not honoured, so no scorer file existed and the referee could not run. Fixed by
inline submission (players embed the scorer source; the runner writes it to a controlled path).
Player 2's scorer was recovered from the log for re-judging. **Second SO game (inline submission):**
both scorers saved correctly; both chains then failed to parse because the players wrote
`1. 🧑‍💻❓ (root): …` with a colon where the grammar expected a dash — the eighth form-checker
leniency gap found by play, fixed and pinned; both chains re-judged with their scorers: the "visible effort" cue sum (log length + code blocks + lists
+ term overlap) was DUPLICATE of length at ρ 0.93 despite 0.668 accuracy — effort cues are length in a
costume, decided by code; the "completeness as a capped count of distinct content kinds" scorer was
VALID at 0.669, ρ 0.67 (ambiguous band, accepted by the model referee) — SO route 004. SO breadth 4:
length, the learned routing-geometry reader, a field-evolution component vote, content-kind coverage.

**Intuition sweep (12 questions × 5 bare guesses, Sonnet):** three behaviours. *Recall*: every
closed-form counting/symmetry question (cube 10 and 57, necklace 13, tetrahedron 15, wire cube 6,
lockers 90, Monty-4 3/8, birthday 1) — five identical exact hits, zero variance: not a guess but a
known result, the covert-calculation signature. Such questions cannot measure intuition in a model
that knows them; parametrized novel instances can. *Snap*: plane-98 → ½ five of five (never ¾);
Monty-5 three correct, two wrong. *Estimation*: three-view faces 9–14 around 12 — but blind, since
the harness had not shown the image; and the pool question answered in mixed units. Harness fixed
(image shown; answer form pinned to the unit) and re-run: three-view with the image → 12 five of five
(with the picture the model solves it, so it is not a guess either); the pool with the unit pinned →
3, 3, 35, 30, 30 around 40 — a real estimate distribution, the first honest intuition curve. The guess
test's informative region is novel instances without a visible solving path; eight recall-contaminated
questions are flagged `guess_recall: likely`.

**Expansion batch, blind play (8 curated questions × 2 Sonnet players, 2026-10-05 night): 16/16
VALID**, two distinct routes per question (lamps: lit-count parity vs handshake double counting;
cyclic tasks: extremal earliest starter vs a task preceding itself; sealed boxes: conservation vs
last-move destination; mirrored involutions: inside-out cancellation vs whole-trip inverse). Transfer
evidence: `mirror-cancellation`, never derived on either ladder, was found at once on its curated
transfer instance — the structural opportunity was recognizable there and not on the ladders.
Totals: 31 questions, 72 routes, 47 attempts, 119 archived chains; typed identity R0 86 %.
**Extension play on the same eight (one Sonnet attempt each against the visible two-route frontier):
4 VALID, 4 DUPLICATE — extension yield 50 % at depth 3.** New routes: spanning-tree case split
(bridges), contraction of robust clusters to a tree skeleton (two bridges per island), a one-way-line
counterexample (central hub), and reversibility isolating the dead-end state (sealed boxes — the
second spine the curator notes had proposed, found by a player). Duplicates were restatements the
referee tied to their originals (orientation-blind distances = mirror twin; even-set closure = parity
invariant; transitive precedence = cyclic strict order; retracing = inverse of composition).

## Definition of done

The atlas is complete when a model from any lab can be pointed at the repo, asked to widen any
question's breadth, and the result — accepted or rejected — lands in the archive under a frozen ruler,
with the question's breadth, its ceiling estimate, the player's depth-weighted score, and the
strategy catalogue all updated without a human relaying a single message.
