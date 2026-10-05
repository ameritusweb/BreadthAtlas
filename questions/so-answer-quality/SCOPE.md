# Scope — Stack Overflow answer quality as an atlas question whose novelty test is code

## Why this question is different

Warp 1 gave the atlas a referee that *plays*. This question gives it a **duplicate test that
computes**. The verdict is a pairwise one — given two answers to the same question, which is better
(the one with the higher score, gap ≥ 3) — and every route must ship an executable scorer over the
same cached pairs. Two routes are costumes if their per-pair margins correlate. That is the first
novelty decision in the atlas made by a number rather than by a referee's reading of landmarks, and it
is the measurement-time twin of the orthogonality constraint `poc4_triangulation` enforces at training
time.

Source: the wave_vector project (external; `wave_vector_root` in `external.local.json`) — `poc4_triangulation.py` (TF-IDF tokens →
VAE latent → three orthogonal wave-vector fields evolved over stages → interference residuals, NODE
routing statistics, geometry and eigen features → quality head, contrastive margin 0.15; GBM over
extracted features), cached pairs (`so_pairs_cache.pkl`), a transformer baseline and its results.

## The concept vocabulary — domain and mechanism on equal footing

The architecture's mechanisms are concepts in the chain, not the space the chain lives in. A route may
be 📐 → 🎯 → ⚖️ or 🌀 → 🌊 → 💥 → ⚖️; both are routes to the verdict.

| emoji | concept | kind |
|---|---|---|
| 📝 | the question text (root) | given |
| 💬 | the two answer texts (root) | given |
| 🏆 | score gap ≥ 3 between them (root) | given |
| 📐 | structure: headings, code blocks, lists | domain |
| 🎯 | relevance: addresses the question asked | domain |
| ✅ | correctness: code runs, facts hold | domain |
| 🔗 | coherence: each part follows from the last | domain |
| 📏 | completeness: edge cases, the *why* | domain |
| 🪞 | example quality: shows rather than tells | domain |
| ⚠️ | caveats: limitations, versions | domain |
| ⏳ | timing: posted before/after the accepted answer; era | domain |
| 🔤 | lexical surface: TF-IDF token statistics | mechanism |
| 🌀 | latent encoding: VAE compression of the answer | mechanism |
| 🌊 | field evolution: velocity-ODE flow over stages | mechanism |
| ⊥ | orthogonal separation of fields | mechanism |
| 💥 | interference residual: where fields disagree | mechanism |
| 🌳 | NODE routing: soft-tree splits on routing statistics (entropy, n_eff, max-prob, centroid, anisotropy, spread) | mechanism |
| 📊 | latent geometry: curvature, eccentricity | mechanism |
| 🔍 | eigen decomposition of the routing distribution | mechanism |
| 🌲 | gradient-boosted trees over extracted features | mechanism |
| ⚖️ | contrastive margin: high score minus low score | mechanism (the verdict's form) |

## The question (breadth framing)

> **What genuinely different mechanisms rank the better answer above the worse one?** A route names a
> mechanism, depicts it as a chain, and proves it with a scorer: a function from an answer pair to a
> margin, run on the shared validation pairs.

Breadth = number of accepted mechanisms. Two scorers are the same mechanism if their margins correlate.

## The referee — three parts, two of them code

1. **Accuracy (code).** The scorer's pairwise accuracy on the held-out pairs must exceed a floor:
   above chance by a margin that rules out noise (≥ 0.60 on ≥ 2,000 pairs) — the floor is deliberately
   below the trained models, because a *mechanism* can be real and weak (answer length alone is a real,
   weak signal). Below the floor → WRONG ("the mechanism does not reach the verdict").
2. **Novelty (code).** Spearman correlation of the scorer's per-pair margins with every accepted
   route's saved margins. ρ ≥ 0.80 with any → DUPLICATE, naming the route. Between 0.50 and 0.80 →
   referred to the model referee with the number. Below 0.50 → new. Thresholds are criterion
   parameters, versioned like everything else.
3. **Mechanism match (model).** The chain must describe what the scorer does; a chain about 🎯
   relevance proved by a scorer that counts code blocks is WRONG. Typed landmarks as elsewhere.

Precedence: code verdicts are final on accuracy and on ρ ≥ 0.80 duplicates; the model referee rules
on mechanism match and on the ambiguous band.

## Two kinds of route, one referee

- **Domain routes** — scorers written from the text: length, code-block count, link count, heading
  count, overlap with the question's tokens, presence of caveat phrases, timing from metadata. Cheap,
  many will be costumes of each other (length ≈ token count ≈ code lines), which is the point.
- **Mechanism routes** — scorers that read one part of the trained `poc4` model in isolation: the
  quality head alone; the triangulation residuals alone; NODE routing stats alone; latent geometry
  alone; eigen features alone; the GBM over one feature family. Each is a route through the
  architecture; the correlation test decides whether the architecture's "three different fields" are
  three mechanisms or one with three wrappers — the question `TRIANGULATION_ANALYSIS.md` asks by
  feature importance, answered here by the atlas's own test.

Expected costume collapses worth seeing: 🔤 lexical vs 📐 structure (both track length); 🌳 NODE
stats vs 💥 residual (both read routing); 📊 geometry vs 🔍 eigen (both read the same distribution).

## Status (2026-10-05, late)

Built: `so_referee.py` (accuracy floor, margin-correlation duplicates, `score`/`score_pair`
contracts, margins stored per accepted route); three domain scorers (length — VALID 0.664; word
count — DUPLICATE ρ 0.96; code share — WRONG 0.577); `poc4_components.py` (extracts the project's
own feature families from `poc3_s2_t4_f3_ortho_product_project_tree_ep10.pt` for 3,000 train and the
same 4,000 held-out pairs) and five mechanism scorers — quality head (no fitting), geo-only,
eigen-only, triangulation-only (linear readers fitted on train), and the GBM over all families
(the project's reader under the referee's protocol). Pending: the extraction run, then the five
referee verdicts.

## What to build (in order)

1. `scripts/so_referee.py` — loads the cached pairs (fixed validation split by seed), runs a scorer
   module given in the ANSWER line (`ANSWER: mechanism <name>; scorer <path.py>`), computes accuracy
   and ρ against `questions/so-answer-quality/margins/<route-id>.npy`, prints
   `EMPIRICAL: valid acc=… | weak acc=… | duplicate-of <route> rho=… | ambiguous rho=… | error`.
   On VALID the margins are saved under `margins/`.
2. A scorer contract: `def score(question: str, answer: str) -> float`; the referee calls it on both
   answers and takes the difference. Mechanism scorers get a helper that loads the `poc4` checkpoint
   once and exposes per-component features.
3. `play.py`: the existing `referee_script:` hook already handles this; add the "ambiguous → model
   referee" path (inject ρ as a FORM NOTE; the model rules).
4. Seed routes by hand — one domain (length) and one mechanism (quality head) — so the correlation
   test has something to compare against, then run blind games; players write scorers.
5. Gap report: concepts in the glossary with no accepted route; this is the "direct the model to look
   there" step.

Effort: 1–2 are a few hours (pairs are cached; the model components are already factored in
`extract_and_eval`); 3 is small; 4 is the first real test.

## What this adds to the atlas

- A **computable novelty criterion** (margin correlation) with explicit thresholds — the thing the
  typed-landmark schema approximates, done exactly for prediction tasks.
- Architecture as a route domain: the atlas's gap finder applied to model design ("no accepted route
  uses ⏳ timing; no route reaches the verdict through 🌳 alone").
- A training loop: accepted mechanism routes are the diverse signal the triangulation fields were
  being forced toward by orthogonality; routes rejected as duplicates are the collapses it was
  forbidding. The atlas measures what `poc4` engineers, on the same task, with the same pairs.
