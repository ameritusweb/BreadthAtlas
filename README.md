# Breadth Atlas

An open, self-renewing benchmark of *how many genuinely different ways a problem can be seen*.

Every question here has a public archive of accepted **routes**: valid lines of reasoning, written as
emoji chains with no calculation, that reach the answer. The archive is the frontier. The only way to
score is to add a route that is not already in it. Publishing everything is what makes it a benchmark:
a model that has memorized the archive gains nothing, because memorized routes are, by definition, taken.

## What is measured

- **Breadth of a question** — the number of accepted routes, under a fixed uniqueness criterion.
  Rich questions admit many ways of seeing; narrow ones admit few. Ranking questions by breadth is a
  map of the problem space.
- **Breadth of a player** — routes contributed, weighted by how deep into the frontier each was found.
  The seventh route on a question is worth more than the first.
- **Breadth over time** — every route is dated. A question's breadth curve across years, under a frozen
  criterion and referee, records how far intuition (human or machine) has expanded on it.

The underlying claim is that a route is intuition made visible: fast, wordless reasoning rendered as a
compact chain another mind can read, check and contest. See [`REFEREE.md`](REFEREE.md) for exactly what
is checked and [`STRATEGIES.md`](STRATEGIES.md) for the cross-question catalogue that routes feed.

See [EXPANDING_THE_PROBLEM_SPACE.md](EXPANDING_THE_PROBLEM_SPACE.md) for a concrete eight-question
expansion batch, candidate conceptual chains, and a method for generating further questions.

## Structure

```
breadth-atlas/
  README.md               this file
  REFEREE.md              what counts as valid, new and well-formed (versioned)
  STRATEGIES.md           cross-question catalogue of reasoning strategies (versioned)
  LEADERBOARD.md          generated — do not edit by hand
  questions/
    <question-id>/
      question.md         the question, reference answer, tolerance, status
      landmarks.md        every landmark used so far (the frontier), accepted or not
      routes/
        NNN-<slug>.md     one accepted route per file
      attempts/
        NNN-<slug>.md     rejected chains, with verdicts (WRONG and DUPLICATE landmarks stay binding)
      external/
        NNN-<slug>.md     pre-protocol answers (prose, dated, attributed) — baselines for the breadth
                          curve; transcribed into chains but not counted as played routes
  LANDMARKS.md            typed-landmark schema; referee emits typed landmarks, leaderboard reports R0/R2
  GOAL.md                 the end state, the invariants, completeness by layer, evidence so far
  snapshots/              dated copies of the leaderboard and ceiling table (the per-year record)
  site/                   generated static site (python scripts/build_site.py)
  provenance/
    pilot_duel.md         the six-turn pilot that produced the first rules
    generators/           the scripts and instances that drew every image question (reproducible byte for byte)
  external.example.json   where the two questions with external data expect to find it (see Setup)
  LICENSE                 MIT for code, CC BY 4.0 for questions, routes and everything else
  scripts/
    external.py           resolves paths to data outside the repo (env var or external.local.json)
    play.py               play engine: duel | blind | extend, via the Claude Code CLI (headless)
    submit.py             offline submission: form-check in code, queue under attempts/pending/ (no model)
    judge_pending.py      referee the offline queue (maintainer, needs the CLI)
    new_question.py       scaffold a question folder (no model)
    rejudge.py            re-judge an attempt after a rule or referee change (keeps the original)
    snap_test.py          blind-read of bare emoji chains → resolve / hedge / absorb
    guess_test.py         bare intuitive guess, no working, scored by tolerance
    ceiling.py            Chao1 route-ceiling estimate per question from all played chains
    type_landmarks.py     back-fill typed landmarks on routes that predate the schema
    identity_check.py     score typed-landmark identity (R0/R2) against the referee's verdicts
    warp_referee.py       empirical referee for warp-one-chess: replay, checkmate, forcedness search
    warp_pick_positions.py  choose proved forced-win positions from the Warp 1 self-play archive
    so_referee.py         empirical referee for so-answer-quality: accuracy floor + margin-correlation duplicates
    export_dataset.py     the whole archive — routes, attempts, verdicts, reasons, typed landmarks, repeats — as JSONL
    build_site.py         static site under site/: leaderboards, year grid, and a drill-down page per question
    strategy_map.py       STRATEGY_MAP.md — strategy × question map (worked / failed / untried), canonical ids via
                          the alias table in STRATEGIES.md
    build_leaderboard.py  regenerates LEADERBOARD.md from the folders above
    test_form.py          regression tests for the form checker (every real misjudgement so far)
```

## Setup

The archive, leaderboard, site and form tests need only Python 3.10+. Playing needs the
[Claude Code CLI](https://docs.claude.com/en/docs/claude-code) on PATH (`claude -p` is the model
backend). `pip install -r requirements.txt` adds Pillow (regenerating images), numpy and scikit-learn
(the Stack Overflow referee and its scorers).

Two questions depend on data that is not redistributed here. Copy `external.example.json` to
`external.local.json` (gitignored) and fill in the paths, or set the environment variables
`BREADTH_ATLAS_WARP_ROOT` and `BREADTH_ATLAS_WAVE_VECTOR_ROOT`:

| question | needs | used by |
|---|---|---|
| `warp-one-chess` | the Warp 1 engine checkout (`WarpOneChess/`, `mini_games/`) | `warp_referee.py`, `warp_pick_positions.py` |
| `so-answer-quality` | the wave_vector project (`so_pairs_cache.pkl`, `so_token_cache.pkl`, `poc4_triangulation.py`, checkpoint) | `so_referee.py`; `poc4_components.py build` (needs torch) |

The Stack Overflow feature cache (`components_cache.npz`, 10 MB, contains answer text) is gitignored;
the mechanism scorers raise a clear error until it is rebuilt with `poc4_components.py build`. The
scorers that read only the answer text (`length_chars.py`, `token_count.py`, `code_blocks.py`, the
player-written ones) run without it. Every other question works from the repo alone.

## Playing

```
python scripts/play.py olympic-pool --mode duel --turns 6          # two players alternate, referee rules
python scripts/play.py turntable-solid --mode blind --players 4    # independent players, no visibility
python scripts/play.py plane-seat-99 --mode extend --turns 3       # one model against the live frontier
```

Models default to Sonnet players and an Opus referee (`--duelist`, `--referee`). Form (emoji count,
root marking, parent tags, the ❓ step, idle steps, landmarks, answer last, arithmetic) is checked in
code before anything reaches the referee; image questions give players and referee the Read tool for
the image only. Every game is archived verbatim under `questions/<q>/games/`.

```
python scripts/rejudge.py wire-cube-diagonal 002 [--form v1]   # after a rule change; v1 = pre-❓ chains
python scripts/snap_test.py olympic-pool                       # can the question be read back from the emoji?
python scripts/guess_test.py plane-seat-99 --samples 5         # intuition without working, scored by tolerance
python scripts/ceiling.py                                      # how much of each question's breadth is found
python scripts/test_form.py                                    # form-checker regression suite
```

## Route file format

```
---
id: 002
question: olympic-pool
title: Required daily rate against the body's limit
strategy: rate-vs-limit
contributor: claude-sonnet-4.5 (duelist A)
date: 2026-10-05
depth: 2            # number of routes already accepted when this one was, plus one
referee: opus/v1
criterion: v1
verdict: VALID
---
<chain: numbered emoji, parent tags, one-sentence explanations>
LANDMARKS: …
ANSWER: …
```

## How to contribute a route

1. Read the question's `question.md` and `landmarks.md`. Every landmark marked VALID there is taken;
   the rest show what has been tried and how it failed.
2. Write a chain that follows the rules in `REFEREE.md`: no calculation, at least ten emoji, every
   emoji after the roots carries a parent tag, every emoji explained, 2–4 landmarks, answer last.
3. Submit it offline:

   ```
   python scripts/submit.py <question-id> my-chain.md --contributor "<who>"
   ```

   The form checker runs in code with no model. A chain that fails form is recorded under `attempts/`
   as ILL-FORMED on the spot. A chain that passes is queued under `attempts/pending/` as PENDING; it
   does not count and does not bind the frontier until a maintainer with a referee runs
   `python scripts/judge_pending.py`, which judges the queue in submission order and files each chain
   under `routes/` or `attempts/` with the same verdicts as live play.
4. Open a pull request with the queued files. Never edit `routes/` by hand, and never delete anything
   under `attempts/`.

Queued chains cannot see each other's verdicts, so when you submit several on one question, make each
one independent of the others being accepted.

## How to add a question offline

```
python scripts/new_question.py <id> --title "…" --family "…" --attractor "…" \
    --question "…" --answer "…" --why "…"
python scripts/build_leaderboard.py && python scripts/test_form.py
```

No model is needed. `EXPANDING_THE_PROBLEM_SPACE.md` gives the selection method and `STRATEGY_MAP.md`
shows which strategy columns are empty and worth targeting; `scripts/seed_expansion_batch.py` is a
worked example of a batch.

Anyone may also **challenge** an accepted route by opening an issue naming the flawed step; a
successful challenge moves the route to `attempts/` and re-opens its landmarks' novelty.

## How to add a question

A question needs a definite answer (a number, count, probability, shape, or yes/no), should be hard
for a strong model, and should pull strongly toward calculation — the restriction against calculating
is what makes the routes intuition rather than arithmetic. Image-based questions are welcome; put the
image in the question folder and reference it from `question.md`. For questions without a known answer
(open problems), set `status: open`; the referee then checks only soundness and novelty, and
disagreement between accepted routes is flagged rather than resolved. A question may carry an optional
`## Glossary` — a shared emoji vocabulary for its givens and its principles — which is shown to players
and referee; it makes uniqueness judgeable by principle rather than by wording, and bare chains more
readable (see `balance-five-objects`).

## Rules of the archive

- The uniqueness criterion and the referee are **versioned**. Breadth is only comparable across
  routes judged under the same versions; when either is upgraded, the archive is re-judged.
- A route's **depth** is fixed at acceptance and never changes.
- Every played chain's landmarks are recorded in `landmarks.md`; only **accepted** chains' landmarks
  bind the frontier. A route is not spent until someone has actually established it.
- Nothing in `attempts/` is deleted. Failed chains record where intuition overreached, which is as
  informative as where it succeeded.

## Provenance

Seeded on 2026-10-05 from a six-turn pilot duel (two Sonnet duelists, an Opus referee) on the
Olympic-pool question; transcript in `provenance/pilot_duel.md`. The rules in `REFEREE.md` are the
rules that pilot ended with, including the two amendments it forced. The image questions were drawn
by the scripts in `provenance/generators/`:

```
python provenance/generators/render_puzzle.py provenance/generators/star4.instance.json \
    provenance/generators/star4.answer.json puzzle.png answer_key.json A:30:shown,B:60,C:150,D:240 7
                                                                     # turntable-solid (byte-identical)
python provenance/generators/ex1_threeview.py drawing.png key.json   # three-view-solid
python provenance/generators/ex2_ladder.py 11 ladder.png key.json    # swap-ladder (seed 23: swap-ladder-b)
```

## License

Code is MIT; questions, routes, attempts, logs and generated tables are CC BY 4.0 (see `LICENSE`).
Contributing a route or question licenses it under CC BY 4.0, attributed to the contributor named in
its frontmatter.
