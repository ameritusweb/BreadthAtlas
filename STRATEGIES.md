# Strategy catalogue — v2 (curated 2026-10-05 from 33 accepted routes on 14 questions)

A route belongs to one question. A **strategy** is what a route looks like once the question is
removed: the shape of the argument and the kind of landmarks it passes through. Entries are keyed on
chain structure (where the parent-tag graph branches, merges into 💥, hangs a 👀) and landmark type —
not on emoji glyphs. Each entry lists the questions where it produced an accepted route (**worked**)
and, where known, where it was tried and rejected (**failed**), so the catalogue doubles as a map of
tried and untried angles.

When the referee proposes `STRATEGY: new: <name>`, the name goes to the *pending* table at the bottom
until curated into an entry here or merged into one.

## Entries

| id | strategy | shape | worked | failed |
|---|---|---|---|---|
| `common-unit` | Express both quantities in one yardstick and compare. Changing the yardstick is the same strategy. | two parallel branches from the givens merging at a comparison; often a heavy-case 👀 | olympic-pool | olympic-pool ×4 costumes (bathtub, body-full, tap-time, depth layer → DUPLICATE) |
| `rate-vs-limit` | Convert the demand into a required rate and confront it with a physical or physiological ceiling. | demand branch + limit branch merging into 💥 | olympic-pool | olympic-pool (stomach-fills costume → DUPLICATE) |
| `part-of-whole` | Place the quantity inside a larger whole it is a known fraction of; size the whole against the target. | whole-branch and share-branch meeting; conclusion by exclusion of the remainder | olympic-pool, monty-four-doors | — |
| `aggregate-and-share` | Scale up to a population where the quantities are familiar, then divide back to one member. | aggregate branch → per-member share | olympic-pool (Opus) | — |
| `symmetric-absorbing-set` | The outcome is fixed by which of a few symmetric states is reached first; the states are interchangeable, so each is equally likely. | identify the decisive set → symmetry → equal slices 🍰 | plane-seat-99 (as "decisive-set symmetry" and, framed as the process, "displacement-relay-first-hit") | plane-seat-99 (restatements → DUPLICATE) |
| `self-similar-reduction` | A first move reduces the problem to a smaller instance of itself with the same question. | reduction step → same shape at smaller size | plane-seat-99 | — |
| `bootstrap-from-known-case` | Start from a solved neighbouring case and adjust for the difference. | known-case root → delta → answer; often a 👀 against the known case | plane-seat-99 | — |
| `likelihood-weighting` | Weight the equally likely prior worlds by how likely the observed action was in each. | priors → observation → reweight → normalize | monty-four-doors | — |
| `two-colouring-invariant` | Colour the states so every step switches colour; parity of step count then forbids or forces return. Includes coordinate-sum parity and explicit checkerboards. | colouring root → each step flips → parity conclusion; plus a witness for the positive case | beetle-five-steps (×2 framings), chessboard-adjacent-corners (as the necessary condition) | — |
| `face-parity` | Closed walks decompose into face boundaries; if every face is even, every closed walk is even. | faces root → decomposition → parity | beetle-five-steps | — |
| `cut-parity` | Split along a seam; parity of what lies on each side forces how many pieces cross it. | seam → counts each side → forced crossings → construction | chessboard-adjacent-corners | — |
| `explicit-construction` | Exhibit the object directly (a tiling, a path, an arrangement). Counts as a distinct route only when its organizing idea differs from other constructions. | build → verify ✅ | chessboard-adjacent-corners (×3 tilings with different organizing ideas), beetle (octahedron witness) | balance-five-objects (every construction so far physically unsound → WRONG) |
| `divisor-pairing-parity` | Pair each divisor d with n/d; only squares have an unpaired divisor; adjust for which divisors act. | pairing → odd/even → flip for the alteration | lockers-skip-first | lockers (restatements → DUPLICATE) |
| `prime-exponent-parity` | The divisor count is the product of (exponent + 1); odd iff all exponents even. | factorization root → product → parity | lockers-skip-first | — |
| `pigeonhole` | More objects than classes forces a shared class; certainty, not probability. | counts → 💥 with "all distinct" | birthday-months | birthday-months (restatement → DUPLICATE) |
| `complement-to-zero` | The complement event's probability is a product with a zero factor. | sequential avoidance → factor reaches zero | birthday-months | — |
| `max-at-least-mean` | The fullest class holds at least the average; the average exceeds one. | average → bound → conclusion | birthday-months | — |
| `orbit-by-invariant-count` | Partition configurations by a quantity rotations preserve (black-face count, mixed-pair count) and count orbits within each class, using the colour-swap complement as a mirror. | partition → per-class orbits → complement 👀 | cube-two-colours (×2: by black count, by mixed opposite pairs) | — |
| `pin-and-reduce-symmetry` | Fix one feature (an axis, a pair) to kill most of the symmetry, then count what remains (a belt). | pin → residual symmetry → count belt → add the uniform cases | cube-two-colours (×2) | — |
| `base-solid-plus-cuts` | Start from a bounding solid and subtract the features the views show; track faces added and removed. | block root → feature branches → tally | three-view-solid | — |
| `orientation-tally` | Classify faces by which way they face and count each class from the view that sees it face-on. | per-direction branches → sum | three-view-solid | — |
| `direction-counting` | The number of edge directions bounds the number of sides a projected convex outline can have. | directions root → bound → identify | wire-cube-diagonal | — |
| `invariant-substructure` | Find the substructure the viewing symmetry preserves (the zigzag ring), then project it. | symmetry root → preserved cycle → outline | wire-cube-diagonal | wire-cube (three-fold alone claimed to space six corners → WRONG) |
| `ring-separation` | Separate points into rings by reach (tips vs inner corners); place inner points by interpolation between neighbouring tips. | reach partition → neighbour tracking → cyclic order | turntable-solid (Opus) | turntable-solid (Sonnet: ring order read off one view → WRONG ×2) |
| `calibrate-then-place` | Use the extreme points (tips) to fix the unknown parameters (view angles), then place the rest. | tips → angles → remaining points | turntable-solid (Opus) | — |
| `independent-blocks` | Decompose the system into non-interacting parts and solve each. | block partition → per-block result → combine | — (swap-ladder route demoted under v2: the per-block solving was simulation) | swap-ladder ×2, swap-ladder-b ×2 |
| `mirror-cancellation` | A sequence that is its own reverse cancels from the inside out; only the unpaired middle survives. | symmetry root → cancellation → residue | — (expected on the ladders; noticed on one block by a player, not yet used to derive the answer) | swap-ladder (partial, chain failed elsewhere) |
| `dominant-surface-proxy` | Rank by the cheapest surface quantity that voters' rewards correlate with (length). The attractor on prediction questions; its costumes are unit changes. | effort → proxy → margin; 👀 on where the proxy fails | so-answer-quality | so-answer-quality (word count → DUPLICATE ρ 0.96 by code) |
| `learned-representation-reader` | Read a trained model's internal representation (latent, routing, its geometry) into a verdict; different readers of the same representation are one route, the best reader its best instance. | encode → evolve → read → ⚖️ | so-answer-quality (quality head; GBM supersedes as best instance) | so-answer-quality (triangulation-only reader → DUPLICATE ρ 0.93) |
| `single-family-reader` | Read one feature family of a representation alone to test whether it carries the verdict by itself. | one family → linear reader → ⚖️ | — | so-answer-quality (geometry 0.577, eigen 0.565 — below floor) |

| `burnside-averaging` | Average fixed colourings over the symmetry group. The calculation attractor on counting questions; ILL-FORMED under the no-calculation rule. | group root → per-class counts → average | — | cube-three-colours (ILL-FORMED: arithmetic in words) |
| `period-decomposition` | Split arrangements by their shortest repeating block; count aperiodic and periodic classes separately. | period root → aperiodic/periodic split → sum | necklace-six-beads | — |
| `parity-bound` | An odd number of transpositions gives an odd permutation, which bounds what can be fixed — a bound, not the answer. | count → parity → bound | — | swap-ladder ×2 (asserted a single swap from an odd count → WRONG) |
| `simulation` | Trace the system's state step by step. Calculation in words; ILL-FORMED since v2. | — | — | swap-ladder, swap-ladder-b (ILL-FORMED) |
| `surface-structure` | Rank text by a visible structural feature (code share, headings). | feature → margin | — | so-answer-quality (code share 0.577, below floor) |
| `low-centre-of-mass` | Lay things flat and low over a wide base. The default stack on balancing problems. | ⚓🏔️ | — | balance-five-objects (rigid-body fallacy → WRONG) |
| `triangulation` | Brace with rigid triangles (tents, A-frames). | 🔺 | — | balance-five-objects (book tent splays → WRONG; nail "tie bar" unjudged) |
| `counterbalance` | Balance a load across a fulcrum. | ⚖️ | — | balance-five-objects (counterweighted a lid that stands alone → WRONG) |
| `containment` | Neutralize an unbalanceable object by enclosing it in another. | 🪨 → 🫙 | — | balance-five-objects (sound idea, chain dropped the eggs → WRONG) |
| `buoyancy` | Lift by flotation. | 🌊 | ball-in-pipe | — |
| `adhesion` | Lift by a sticky contact stronger than the weight. | 🧲 | ball-in-pipe | — |
| `pressure-gradient` | Infer height from the fall of pressure with altitude. | 🌬️ | barometer-building | — |
| `free-fall` | Infer height from fall time under gravity. | 🪂 | barometer-building | — |

| `conservation-invariant` | A quantity every allowed move preserves rules out any target with a different value. | moves root → local loss = local gain → global total fixed → 💥 with target | sealed-box-transfers | — |
| `parity-invariant` | A parity every allowed move preserves rules out targets of the other parity. (General form; `two-colouring-invariant` is its graph special case.) | moves root → parity preserved → target excluded | pair-toggle-lamps | — |
| `last-step-witness` | Whatever the final move does, it leaves a witness that contradicts the target (the last destination is non-empty). | final move → witness → 💥 | sealed-box-transfers | — |
| `extremal-element-contradiction` | Pick the extreme element (earliest, largest); the constraint on it contradicts its extremality. | order root → extreme element → its prerequisite is earlier → 💥 | cyclic-task-prerequisites | — |
| `cyclic-strict-order` | Following a strict order around a cycle makes an element precede itself. | cycle root → chain of strict precedences → self-precedence 💥 | cyclic-task-prerequisites | — |
| `condensation-sink` | Collapse mutually reachable nodes into clusters; a sink cluster has no way out, so a common hub there proves nothing about mutual reach. | reachability clusters → sink → no onward path | one-way-central-island | — |
| `invariance-witness` | Exhibit a transformation that preserves every supplied observation while changing the answer; the observations cannot decide. | transformation → observations unchanged → answer changed → ambiguity | tetrahedron-mirror-information | — |
| `reconstruct-and-count` | Rebuild the object from the data and count how many objects fit; more than one means the data does not decide. | construction → branch point → two solutions | tetrahedron-mirror-information | — |
| `handshake-double-counting` | Count the same incidences two ways (per node, per link); the parity or total that falls out constrains the state. | double count → forced parity/total | pair-toggle-lamps | — |
| `inverse-of-composition` | The reverse of a sequence of self-inverse actions is its inverse (socks-and-shoes), so a mirrored sequence restores the start. | composition → reversal = inverse → identity | mirrored-involutions | — |

| `spanning-tree-argument` | Fix a spanning tree; split cases by whether the removed link is a tree edge; a loop edge re-crosses any tree cut. | tree root → case split → recrossing | bridges-on-loops | — |
| `contract-to-quotient` | Collapse robust (2-edge-connected) clusters to points; the skeleton that remains is a tree whose edges are exactly the critical links. (Directed special case: `condensation-sink`.) | contraction → tree skeleton → read off critical links | two-bridges-per-island | — |
| `reversibility-partition` | Where every move is reversible, reachability is an equivalence; a state with no move out (or in) sits in its own class, so it cannot be reached from a live state. | reversible moves → classes → terminal state isolated | sealed-box-transfers | — |

| `mirror-square-threat` | Attack a square through its twin on the other board: flip a piece so it lands next to, or captures toward, the king. The defining Warp 1 mechanic; every first-game attempt reached for it and misread the position. | flip → mirror landing → threat | — | warp-one-chess ×3 (illegal flip; unforced quiet tempo; Black's own flip escape ignored — all WRONG by the engine) |

## Aliases

Referee-proposed names folded into catalogue ids. Parsed by `scripts/strategy_map.py` (format:
`alias: <proposed-name> => <catalogue-id>`); add a line whenever the referee proposes a name that is an
existing entry in different words.

alias: adhesive-probe => adhesion
alias: axis-pair-decomposition => orbit-by-invariant-count
alias: opposite-pair-decomposition => orbit-by-invariant-count
alias: block-decomposition-then-parity => independent-blocks
alias: block-decomposition-with-parity => independent-blocks
alias: parity-and-block-decomposition => independent-blocks
alias: decompose-then-simulate => independent-blocks
alias: bootstrap-from-known-answer => bootstrap-from-known-case
alias: complement-of-known-variant => bootstrap-from-known-case
alias: buoyancy-flotation => buoyancy
alias: burnside-orbit-averaging => burnside-averaging
alias: case-split-by-colour-multiset => orbit-by-invariant-count
alias: case-split-by-colours-used => orbit-by-invariant-count
alias: case-split-by-invariant-pattern => orbit-by-invariant-count
alias: invariant-partition => orbit-by-invariant-count
alias: invariant-partition-by-run-count => orbit-by-invariant-count
alias: invariant-partition-with-complement-pairing => orbit-by-invariant-count
alias: transitivity-collapse-by-colours-used => orbit-by-invariant-count
alias: parity-absorption-reduction-to-multisets => orbit-by-invariant-count
alias: case-split-on-first-pick => part-of-whole
alias: conserve-and-split => part-of-whole
alias: conserved-share-symmetric-split => part-of-whole
alias: containment-ballast => containment
alias: coordinate-parity-invariant => two-colouring-invariant
alias: parity-colouring-plus-witness => two-colouring-invariant
alias: parity-obstruction-plus-construction => two-colouring-invariant
alias: counterbalance-across-hinge => counterbalance
alias: cut-parity-contradiction => cut-parity
alias: decisive-seat-reduction => symmetric-absorbing-set
alias: decisive-seats-symmetry => symmetric-absorbing-set
alias: decisive-set-symmetry => symmetric-absorbing-set
alias: displacement-relay-first-hit => symmetric-absorbing-set
alias: pigeonhole-at-boarding => symmetric-absorbing-set
alias: deletion-recursion-on-multiset-size => self-similar-reduction
alias: restart-recursion-induction => self-similar-reduction
alias: direct-simulation => simulation
alias: mirror-cancellation-to-single-transposition => mirror-cancellation
alias: pairwise-rung-cancellation => mirror-cancellation
alias: parity-then-assert => parity-bound
alias: parity-by-pairing => divisor-pairing-parity
alias: explicit-minimal-counterexample => explicit-construction
alias: free-fall-timing => free-fall
alias: low-wide-base => low-centre-of-mass
alias: per-component-weighted-sign-vote => single-family-reader
alias: pigeonhole-certainty => pigeonhole
alias: pigeonhole-witness => pigeonhole
alias: pin-a-feature-and-reduce-symmetry => pin-and-reduce-symmetry
alias: pin-a-pair-and-count-the-belt => pin-and-reduce-symmetry
alias: refine-then-quotient => pin-and-reduce-symmetry
alias: pressure-altimetry => pressure-gradient
alias: primitive-period-decomposition => period-decomposition
alias: projected-vertex-ring => invariant-substructure
alias: symmetry-picture-construction => invariant-substructure
alias: symmetry-then-silhouette-ordering => ring-separation
alias: single-view-angular-ordering => ring-separation
alias: ring-separation-and-midpoint-interpolation => ring-separation
alias: structural-signal => surface-structure
alias: triangulation-tent => triangulation
alias: splice-detour-reroute => explicit-construction
alias: explicit-minimal-counterexample => explicit-construction
alias: degree-two-cut-vertex-counterexample => explicit-construction
alias: minimal-sink-counterexample => explicit-construction
alias: condensation-sink-component => condensation-sink
alias: invariance-witness-reflection => invariance-witness
alias: reconstruct-and-count-solutions => reconstruct-and-count
alias: parity-invariant-obstruction => parity-invariant
alias: extremal-first-element-contradiction => extremal-element-contradiction
alias: cyclic-strict-order-self-precedence => cyclic-strict-order
alias: conservation-invariant-obstruction => conservation-invariant
alias: nested-peeling-cancellation => mirror-cancellation
alias: inverse-of-composition-reversal => inverse-of-composition
alias: spanning-tree-cut-repair => spanning-tree-argument
alias: contract-to-cluster-tree => contract-to-quotient
alias: source-and-sink-obstruction => condensation-sink
alias: reversibility-isolates-terminal-state => reversibility-partition
alias: mirror-landing-queen-check => mirror-square-threat
alias: guarded-mirror-flip-queen-kill => mirror-square-threat
alias: mirror-flip-corner-sweep => mirror-square-threat

## Observations the catalogue already supports

- Strategies that recur across unrelated questions: `two-colouring-invariant` (beetle, chessboard),
  `part-of-whole` (pool, Monty), `pigeonhole`/`max-at-least-mean` (birthday) are the general-purpose
  ones so far; `pin-and-reduce-symmetry` and `orbit-by-invariant-count` are the counting family's.
- The costume problem lives inside `common-unit`: five costumes on one question. Under the landmark
  schema (LANDMARKS.md) this is the R0/R2 distinction.
- `explicit-construction` is the entry most at risk of inflating breadth; it needs the schema's
  "organizing idea" field to stay honest.
- Gaps worth probing: no route yet uses `mirror-cancellation` on the ladders; no `aggregate-and-share`
  outside the pool; no `likelihood-weighting` outside Monty; no `self-similar-reduction` on the
  Monty or lockers families where it plainly applies.

## Pending referee proposals

None uncurated as of this revision. New `STRATEGY: new:` names from future games are appended here.
