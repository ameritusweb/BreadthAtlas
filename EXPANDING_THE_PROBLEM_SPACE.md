# Expanding the Breadth Atlas problem space

## Concrete expansion added on 2026-10-05

Eight new questions have been added to `questions/`, increasing the corpus from 23 to 31. Each has a reference answer, an empty played-landmark frontier, and a ten-step conceptual chain in `curator.md`. These drafts are unjudged and contribute no accepted-route score. The existing player loader does not include curator notes in its question input.

| New question | Answer | Conceptual chain spine |
|---|---|---|
| [Bridges on loops](questions/bridges-on-loops/question.md) | A single closure cannot disconnect the network. | Loop → alternate path → substitute crossing. |
| [Two bridges per island](questions/two-bridges-per-island/question.md) | Local redundancy does not guarantee global redundancy. | Two triangles → sole joining bridge → separating cut. |
| [One-way central island](questions/one-way-central-island/question.md) | A common reachable hub does not imply mutual reachability. | Directed arrival → sink → no onward path. |
| [Tetrahedron mirror information](questions/tetrahedron-mirror-information/question.md) | Distances do not determine handedness. | Reflection → unchanged evidence → opposite answers. |
| [Pair-toggle lamps](questions/pair-toggle-lamps/question.md) | Exactly one lit lamp is unreachable. | Paired changes → parity preserved → target excluded. |
| [Cyclic task prerequisites](questions/cyclic-task-prerequisites/question.md) | No successful schedule exists. | Earliest start → required earlier start → contradiction. |
| [Sealed-box transfers](questions/sealed-box-transfers/question.md) | Transfers cannot empty the whole collection. | Local loss and gain → global conservation → impossible target. |
| [Mirrored involutions](questions/mirrored-involutions/question.md) | The mirrored action sequence restores its starting state. | Centre pair → cancellation → nested restoration. |

All eight drafts pass the existing mechanical chain checker and all eight questions load through the existing play engine. Computational checks additionally covered the graph counterexample, all 253 connected loop-protected simple networks on five vertices, every reachable lamp state, every triple of self-inverse permutations on four device states, and a reflected tetrahedron's distance record. These checks support the reference examples; they are not model-referee judgments of soundness or novelty. General arguments are recorded in each reference answer.

The leaderboard has been regenerated. Next, play these questions through the existing blind and extension modes to establish accepted routes. Candidate second spines and boundary variants are already recorded in each question's curator notes.

## How this batch was generated

To invent a new atlas problem, start with a relationship that could make its answer visible: a bottleneck, an indistinguishable pair, a preserved total, a reversible operation, a constraint that changes what is reachable. Give that relationship concrete objects, then ask a question it can settle without calculation.

To invent a conceptual emoji chain, draw how that relationship changes what follows from the givens. Each emoji should carry a concept or operation whose meaning the explanation establishes. The chain's novelty lives in its intermediate claims, not in new glyphs.

The examples below are proposed questions and candidate chains, not referee-accepted additions to the archive. Their principles are familiar ideas; their potential contribution is to extend the atlas's present coverage. The existing [referee rules](REFEREE.md) still govern acceptance.

## The generative move: relationship → question → chain

Take **containment** as an example. “Put the nail inside the bottle” is a move. The conceptual claim is that enclosure can remove an otherwise troublesome degree of freedom. That opens several directions:

- In physical design: can an enclosure prevent an object from escaping without immobilizing it?
- In a network: can a region trap movement because every exit is blocked?
- In information: can an observation restrict the possible answer to one equivalence class without identifying a member?

These are candidate analogies. For each one, establish what is being contained, what can still change, and what cannot cross the boundary. The analogy becomes a reasoning route only when those relationships support the answer.

Use this invention sequence:

1. **Choose a conceptual verb:** preserve, separate, hide, reveal, reverse, trap, pair, constrain, amplify, cancel.
2. **Choose objects it can act on:** paths, arrangements, observations, forces, choices, signals, transformations.
3. **Write the load-bearing claim:** “every path crosses this edge”; “these observations cannot distinguish a reflection”; “every allowed move preserves the total.”
4. **Ask what that claim settles:** reachability, identification, possibility, stability, or a forced outcome.
5. **Build the chain backward from the claim:** what establishes it, and what follows from it?
6. **Try a second conceptual spine on the same question.** A different proof obligation or intermediate claim can produce another route; a new metaphor alone cannot.
7. **Break one premise.** The resulting question tests whether the player understands why the original chain worked.

## Worked invention 1: a bridge becomes a question about separation

**Conceptual seed:** every crossing depends on one shared link.

**Proposed question:** Two internally connected groups of islands, West and East, are joined by exactly one bridge. A traveller starts in West and wants to reach East using bridges only. If the joining bridge closes, can any detour still reach East?

**Conceptual spine:** 🗺️ → ✂️ → 🧱 → 🚫. The key move is to see a cut between regions rather than search individual paths.

```text
1. 🏝️ (root) — West is a connected group of islands with bridges inside it.
2. 🏖️ (root) — East is another connected group of islands with bridges inside it.
3. 🌉 (root) — Exactly one bridge joins any island in West to any island in East, and it is closed.
4. 🚶 (root) — The traveller starts in West and can move only along open bridges.
5. ❓ (← 1, 2, 3, 4) — Can a detour along open bridges take the traveller into East?
6. ✂️ (← 1, 2, 3) — Separating the islands into West and East exposes the closed bridge as the only link across the separation.
7. 🚪 (← 4, 6) — Any journey into East would have to include a first crossing from West to East.
8. 🔒 (← 3, 6, 7) — That first crossing would have to use the closed bridge.
9. 🔁 (← 1, 6) — Detours within West change the route inside the region but create no additional crossing.
10. 🚫 (← 4, 8, 9) — No permitted journey can reach East.
LANDMARKS:
- Every journey from West to East must cross the same single bridge.
- Detours within a region cannot replace a missing connection across the separation.
ANSWER: No.
```

**A second route to investigate:** reachable-set closure. Instead of locating the edge every successful path would need, show that the set of West islands is closed under every permitted move. The proposed landmark is “every next step from a reachable island remains in West.” The referee must decide whether this is substantively distinct from the cut argument.

**Expansion:** transfer to a dependency system where every way of producing an output needs one unavailable input. Verify the dependency rules; the bridge analogy does not establish them.

**Boundary:** add another crossing. The first route's “only link” claim fails, and the question must be solved under the new connectivity.

## Worked invention 2: a mirror becomes a question about information

**Conceptual seed:** a transformation changes the answer while preserving every supplied observation.

**Proposed question:** A labelled, non-flat tetrahedron is described only by all its pairwise vertex distances. Can those distances determine which of its two mirror handednesses it has, relative to a fixed external orientation?

**Conceptual spine:** 🪞 → 📏 → 🎭 → ❔. The insight is an indistinguishable pair, not a difficult reconstruction.

```text
1. 🔺 (root) — The object is a labelled tetrahedron whose vertices do not all lie in one plane.
2. 📏 (root) — The supplied observations are only the distances between every pair of labelled vertices.
3. 🧭 (root) — The requested handedness is defined relative to a fixed external orientation.
4. ❓ (← 1, 2, 3) — Do the supplied distances determine the tetrahedron's handedness?
5. 🪞 (← 1, 3) — Reflecting the tetrahedron produces a labelled configuration with opposite handedness.
6. ↔️ (← 2, 5) — Reflection preserves the distance between every corresponding pair of vertices.
7. 📋 (← 2, 6) — The original and reflected configurations therefore supply exactly the same observations.
8. 🎭 (← 5, 7) — One observation record is compatible with opposite handednesses.
9. 🔍 (← 7, 8) — A decision using only that record has no evidence for choosing between them.
10. ❔ (← 4, 8, 9) — The handedness cannot be uniquely determined from the supplied distances.
LANDMARKS:
- Reflection reverses handedness while preserving every supplied pairwise distance.
- The same observation record is compatible with opposite answers.
ANSWER: No; the distances leave a mirror ambiguity.
```

**Expansion:** seek other observation-preserving transformations: relabelling, time shifts, rotations, or hidden-variable changes. Each creates a candidate identification problem if it changes the requested answer. A transformation that preserves both observations and answer supplies no such ambiguity.

**Boundary:** supply an orientation-sensitive observation. Ask whether it distinguishes the pair. This tests what information is missing, rather than merely asking for another rendering of the tetrahedron.

## Worked invention 3: a preserved total becomes an impossibility question

**Conceptual seed:** allowed moves change appearances while leaving one quantity fixed.

**Proposed question:** A sealed collection of boxes contains counters. A move transfers a counter from one box to another; counters cannot enter or leave the collection. Initially, at least one counter is present. Can a sequence of moves make every box empty?

**Conceptual spine:** 🔄 → 🧮 → 🔒 → 💥. This is deliberately a simple anchor; harder variants should obscure the conserved quantity while retaining a verified invariant.

```text
1. 📦 (root) — All counters are inside a sealed collection of boxes.
2. ⚫ (root) — At least one counter is present initially.
3. 🔄 (root) — Each allowed move transfers a counter from one box to another without adding or removing counters.
4. ❓ (← 1, 2, 3) — Can allowed moves make every box empty?
5. ➖ (← 3) — A transfer removes a counter from its source box.
6. ➕ (← 3) — The same transfer places that counter in its destination box.
7. ⚖️ (← 5, 6) — The loss at the source and gain at the destination preserve the collection's total.
8. 🔒 (← 3, 7) — Every permitted move preserves that total, so any sequence preserves it too.
9. 🕳️ (← 4) — An arrangement in which every box is empty would contain no counters.
10. 💥 (← 2, 8, 9) — An empty collection contradicts the preserved presence of counters.
LANDMARKS:
- Every local transfer preserves the global total.
- The proposed final arrangement has a different total from the initial arrangement.
ANSWER: No.
```

**A second route to investigate:** follow one initially present counter conceptually. Every allowed move either leaves it in its box or puts it in another box, so it always has a location within the collection. This uses persistence of a witness rather than a total. It does not require tracing an actual sequence of states. Whether the two landmarks count as separate routes remains a referee decision.

**Expansion:** replace literal counters with a conserved property that is less visually obvious. Potential settings include flow through a network or exchanges among accounts; define the permitted moves precisely before asserting conservation.

**Boundary:** allow a counter to leave the collection. Conservation of the collection's total no longer holds. The revised question needs an answer supported by the new rules.

## Invent chains by composing concepts

Composition can expose problems that a single strategy does not settle. Make the interaction explicit.

| Composition | Candidate problem to develop | Claim the chain must establish |
|---|---|---|
| Conservation + bottleneck | Resources move between regions through a restricted connection. Can the target distribution be reached? | What must cross the boundary, and whether the connection permits it. |
| Symmetry + missing information | Several objects fit a partial observation. What extra observation separates them? | Which transformation preserves the existing evidence and which new evidence breaks it. |
| Containment + reversibility | Moves can be undone inside a region, but an exit is one-way. Can the starting state be recovered? | Where reversibility stops and whether another return route exists. |
| Pairing + boundary defect | Local contributions cancel except near an edge or unmatched element. What survives? | Why interior cancellation holds and what the boundary leaves unpaired. |
| Decomposition + coupling | Two subsystems are independently solvable until one shared constraint is imposed. Is their combined solution still possible? | Whether the local solutions agree on the shared constraint. |

These are question generators, not established theorems. Write the actual givens, settle the answer, and construct the intermediate claims before adding a question to play.

## A prompt for generating candidate questions and chains

```text
Using the Breadth Atlas rules and the accepted-route frontier supplied below:

Choose one conceptual relationship underrepresented in the corpus.
State it as a claim about objects, transformations, or observations.
Create a precise question whose answer follows from that relationship
without arithmetic or step-by-step simulation.

Return:
1. The question with complete givens and a precise ask.
2. Its reference answer and an independently checkable justification.
3. A candidate chain with at least ten emoji steps, roots, parent tags,
   exactly one question step, two to four landmarks, and the answer last.
4. A proposed second route with different substantive intermediate claims,
   or an explicit statement that no second route has been found.
5. One changed premise that breaks the first argument, with the revised
   answer or an explicit statement that it remains unresolved.
6. The nearest existing strategy and what coverage this candidate adds.

Do not claim novelty from different emoji, names, units, or wording.
Do not claim referee acceptance. Separate verified claims from proposals.
```

Use the sections below to curate and test the candidates produced by this method.

---

# Curation and evaluation workflow

## 1. Separate the kinds of expansion

| Kind | What changes | What it reveals |
|---|---|---|
| Route | A new set of substantive landmarks reaches an existing question's answer. | Another way to see the same problem. |
| Instance | Parameters, layout, or givens change within a family. | Whether a strategy survives beyond the example where it was found. |
| Boundary | One assumption changes so an earlier strategy fails or needs repair. | Where that strategy applies and where it breaks. |
| Family | A new underlying structure or combination of structures enters the corpus. | A region of reasoning the atlas has not covered. |
| Domain | An existing structure appears in another setting. | Whether a strategy transfers across subject matter. |
| Verification | A claim becomes testable through a new referee or evidence source. | A region that can now be admitted and judged reliably. |

A new story about comparing two quantities may be a useful transfer test while still using `common-unit`. A new ladder layout may test the same cancellation mechanism. Both belong in the map, but neither automatically establishes a new strategy or route.

Count accepted routes locally under the question's criterion. Record transfer separately: the same strategy working on two questions is evidence of generality, not a reason to reject its first valid use on the second question.

## 2. Map structures before collecting topics

Use topics to find examples, and structures to decide what those examples add. “More physics” is a search direction. “A conservation argument where local observations disagree with the global balance” describes a gap to fill.

Give each candidate a short profile along these axes:

| Axis | Choices to consider |
|---|---|
| Underlying structure | Symmetry, conservation, connectivity, ordering, recursion, constraint, uncertainty, feedback, geometry. |
| Task | Identify, compare, predict, construct, rule out, explain an observation, distinguish hypotheses. |
| Access to the problem | Prose, diagram, multiple views, qualitative observations, bounded interaction. |
| Route opportunities | Invariant, pairing, decomposition, bound, construction, contradiction, analogy, causal intervention. |
| Obstacle | Famous-answer attractor, misleading local view, irrelevant detail, hidden dependency, missing assumption. |
| Answer type | Exact answer, approximate answer with tolerance, impossibility, witness, conditional conclusion. |
| Verification | Known proof, generated key, executable checker, measured outcome, unresolved soundness review. |

These are curation notes, not new mandatory runner fields. A candidate should say which combination is missing or weakly represented. Filling every possible combination would produce many artificial questions; choose combinations with a clear reasoning opportunity.

## 3. Generate candidates from four sources

### A. Transfer an existing strategy

Start with a strategy in [STRATEGIES.md](STRATEGIES.md), strip away its original objects, and look for another system with the same relationships.

Examples to develop:

- **Mirror cancellation:** move from swap ladders to a sequence of reversible mechanical operations. Ask what survives a reversed sequence with one unmatched operation.
- **Rate versus limit:** move from lifetime drinking to a reservoir supplied and drained at bounded rates. Ask whether a target can be reached using qualitative bounds.
- **Two-colouring invariant:** move from board walks to a network whose links always cross a partition. Ask which returns or destinations are impossible.
- **Aggregate and share:** move from pool volume to a shared resource whose total is familiar but whose per-person demand is not.
- **Pin and reduce symmetry:** move from coloured solids to circular arrangements or equivalent network layouts. Ask what becomes distinguishable once one feature is fixed.

For each transfer, write down the correspondence between the original and new objects. Then identify what might invalidate it. A resemblance without preserved relationships is a source of candidates, not a sound route.

Do not put the intended strategy in the player's prompt. Keep it in the curator's reference notes so play can reveal whether the player finds it independently.

### B. Change one load-bearing assumption

Create a paired question by changing exactly one condition that matters to a known argument.

| Original structure | Controlled change | What the pair tests |
|---|---|---|
| A mirrored sequence of self-inverse swaps | Replace one swap with an operation whose inverse differs from itself. | Whether the player checks the condition behind cancellation. |
| Interchangeable decisive states | Make one state behave differently. | Whether symmetry is established rather than assumed. |
| An even-cycle network | Introduce an odd cycle. | Whether the parity obstruction is applied within its domain. |
| A rigid arrangement | Allow a contact to slide or an object to rotate freely. | Whether stability depends on an unstated constraint. |
| A recognizable projected outline | Remove a view or introduce a second compatible object. | Whether the evidence determines the answer uniquely. |

Verify both members of the pair. A changed condition does not guarantee a changed answer, and it may introduce ambiguity. The reference notes should identify the exact step that survives, fails, or needs replacement.

### C. Investigate repeated failures

Use attempts to choose new questions as well as to search for new routes.

- Repeated simulation suggests a smaller instance where a structural shortcut is visible, followed by larger variants that retain it.
- Repeated famous-answer absorption suggests a paired instance with an explicit alteration and a different verified answer.
- Repeated physically false constructions suggest a question that isolates the disputed contact, support, or constraint.
- Repeated yardstick costumes suggest testing whether the question admits another principle at all.
- Repeated disagreement about novelty suggests an instance where the competing mechanisms produce distinguishable intermediate claims.

Treat these as hypotheses about the failure. An easier instance, a glossary, or a diagram changes the assistance available; record that change instead of pooling the results.

Rejected landmarks remain useful search history. Under the current rules, only accepted routes bind novelty.

### D. Open a domain through a trustworthy referee

Some regions become practical only when claims can be checked beyond a model's reading. The atlas's Warp 1 and answer-quality work provide two patterns: checking a proposed outcome with an engine, and comparing executable mechanisms on shared evidence.

Candidate extensions include:

- Network designs checked for connectivity and failure tolerance.
- Packing or tiling constructions checked for coverage and overlap.
- Qualitative physical predictions tested in a specified simulation or experiment.
- Diagnostic mechanisms evaluated on a fixed set of cases with known outcomes.
- Planning mechanisms checked against explicit resource and dependency constraints.

Keep the mechanism visible in the chain. A checker can verify that a construction works without proving that the claimed principle explains it. Likewise, a successful game line does not establish a forced win, and predictive accuracy alone does not establish a new mechanism.

Executable witnesses and empirical evidence need an explicit question-specific protocol, as in the existing empirical scopes. They do not silently authorize calculation inside ordinary routes. If admitting a new task requires a rule change, document and version it before comparing scores.

## 4. Prioritize regions with different reasoning demands

The following are proposed directions, not claims that each already has a valid question or several independent routes.

| Region | Candidate question shape | Route opportunities to investigate | Main verification issue |
|---|---|---|---|
| Conservation and balance | Can a rearrangement or flow achieve a target while preserving a total? | Global balance, local pairing, bounds, contradiction. | Define the system boundary and permitted exchanges. |
| Connectivity and bottlenecks | Which link failure separates a network, or can a route avoid a chokepoint? | Cuts, alternate paths, decomposition, redundancy. | Check the actual graph and all relevant cases. |
| Causal structure | Which change would distinguish two explanations of an observation? | Intervention, conditional independence, counterexample. | State causal assumptions and whether the evidence identifies an answer. |
| Information and identification | Can these observations distinguish every allowed object? | Indistinguishability, symmetry, witness pairs, partitioning. | Exhaust the allowed objects or prove the ambiguity structurally. |
| Ordering and dependencies | Which outcome is forced by precedence constraints without tracing every schedule? | Partial order, critical dependency, exchange argument. | Avoid relying on an unstated scheduling rule. |
| Robust physical design | Which arrangement retains support after a specified perturbation? | Containment, triangulation, constraint, counterbalance. | Specify dimensions, contacts, friction assumptions, and the perturbation. |
| Feedback and equilibrium | What happens qualitatively after a disturbance in a coupled system? | Restoring response, reinforcing loop, limiting case, conservation. | Specify the model and the range in which the qualitative claim holds. |
| Representation and ambiguity | Which features survive a projection, encoding, or change of viewpoint? | Invariant substructure, multiple-view agreement, reconstruction, counterexample. | Ensure the supplied representation supports the claimed inference. |

Choose initial candidates with modest scope and strong verification. Broad domain labels such as “causality” or “design” are not sufficient question specifications.

## 5. Use a candidate card before adding a question

Keep a short Markdown card for each proposal. This is a proposed working format, not a change to `question.md` parsing.

```markdown
# Candidate: <working title>

- Expansion kind: family / transfer / instance / boundary / verification
- Gap filled: <missing structure, task, or relationship>
- Nearest existing question: <id, or none>
- Player-facing question: <complete givens and precise ask>
- Answer and tolerance: <or the admissible claim for an open question>
- Verification: <proof, key, checker, evidence; unresolved issues>
- Possible route principles: <curator hypotheses, not player hints>
- Likely attractor: <and what distinguishes this question>
- Load-bearing assumptions: <conditions a route must respect>
- Variant plan: <one transfer or boundary instance>
- Novelty criterion: <what distinguishes mechanisms from costumes>
- Assistance condition: <image, glossary, tools, or none>
- Admission decision: ready / revise / scoped
```

Look for plausible room for multiple principles, but do not require a curator to find them all before admission. A narrow question can be an informative control. A zero-route question can expose a limitation. Label the purpose so a hard frontier question is distinguishable from an underspecified one.

## 6. Admit questions through a short evidence cycle

1. **Specify the problem.** Write complete givens, the exact ask, permitted resources, and answer tolerance. For an altered familiar puzzle, make the alteration explicit.
2. **Establish judgeability.** Verify the reference answer or define what evidence makes an open claim admissible. Author-side calculation, generators, and checkers can establish keys; the player's route remains subject to its protocol.
3. **Check structural opportunity.** Write at least one plausible non-calculating route in private curator notes, or state why a frontier question is admitted without one. Do not count those notes as played routes.
4. **Run blind play.** Use independent players without the accepted-route frontier to observe natural routes and attractors. Keep reference answers and curator hypotheses out of player inputs.
5. **Run extension play.** Show the accepted frontier and ask for another route. This tests expansion after familiar routes are consumed.
6. **Inspect failures for curation.** Decide whether they indicate a reasoning limit, ambiguous wording, missing evidence, or a verification gap. Correct defective questions with a recorded revision.
7. **Test a transfer or boundary.** Determine whether the proposed strategy survives a new instance or whether the changed assumption is noticed.
8. **Archive and classify.** Preserve chains and verdicts, update the strategy catalogue when warranted, and regenerate the leaderboard using the existing workflow.

Give comparison groups the same play budget and assistance condition. Record model, referee, criterion, and question revision. Treat measurements across different conditions as separate results.

## 7. Build families that reveal conditions of use

A useful family can have three members:

- **Anchor:** a verified instance where the structural opportunity can be recognized.
- **Transfer:** a different presentation or domain preserving that opportunity.
- **Boundary:** a changed assumption that limits or defeats the earlier argument.

For cancellation, the anchor could be a mirrored ladder; the transfer could use reversible operations on an object; the boundary could substitute a non-self-inverse operation while repeating the same operation in the mirrored position. Each needs its own verified answer.

Generators should vary features with known relevance: topology, symmetry, the location of an unmatched operation, permitted contacts, or information available. Record the generator version and seed. Verify every generated instance; preserving a visual pattern does not necessarily preserve a unique answer or the intended route.

Keep a reserved set of instances outside the public frontier during evaluation, then publish them with their results. This complements the public archive: memorized routes cannot extend an existing frontier, but new instances also test whether a strategy can be re-derived.

## 8. Expand the strategy map alongside the corpus

Maintain a question-by-strategy map with these states:

| State | Meaning |
|---|---|
| Worked | An accepted route uses the strategy. |
| Attempted and failed | A submitted chain tried it and received a rejection; link the reason. |
| Proposed | A curator predicts applicability, without accepted evidence. |
| Untried | No recorded attempt; applicability is unknown. |
| Ruled out under stated assumptions | A specific argument establishes why it cannot apply. |

An absent route is not evidence that a strategy is impossible. A rejected execution is not proof that the whole strategy fails. Preserve the distinction between the principle and the chain that attempted it.

Use this map to select the next question or game: try a recurring strategy in an unrelated family, investigate a rejection near an accepted application, or create a boundary around a principle that currently looks universal.

If glossaries are used, distinguish vocabulary for the givens from vocabulary that names possible solution principles. Compare assisted and unassisted play separately. A glossary can improve communication while also supplying ideas the player otherwise would have needed to find.

## 9. Measure the expansion that occurred

Alongside existing breadth scores, report:

- **Structural coverage:** which combinations of structure and task have admitted questions.
- **Strategy transfer:** which strategies have accepted applications across distinct families or domains.
- **Boundary behavior:** whether players detect when a known argument's assumptions no longer hold.
- **Extension yield:** accepted new routes per submitted extension attempt under a stated budget.
- **Failure distribution:** WRONG, DUPLICATE, and ILL-FORMED attempts, with recurring reasons.
- **Verification coverage:** which questions have settled keys or working empirical checks, and which remain scoped.

Question count, accepted breadth, and structural coverage answer different questions. Publish all three with their conditions. Keep scoped proposals outside played-question results, and keep route counts separated by criterion and referee versions.

## 10. Start with one small expansion batch

An initial batch could contain twelve candidates:

- Four transfers of established strategies into different settings.
- Four boundary variants that change one assumption in an existing family.
- Four questions from the proposed regions above, selected for clear givens and strong verification.

Write the candidate cards first, verify the answers, then admit the ready subset. Give each admitted question a comparable blind and extension budget. For every candidate, record what it actually added: an instance, a transfer, a boundary, a new strategy, or a newly judgeable domain. Revise candidates that expose specification defects and retain honestly difficult questions whose evidence is sound.

The next batch should follow the resulting gaps. If one strategy transfers widely, test its boundary. If several domains collapse onto one strategy, seek a different structure. If a new structure produces promising but unsound attempts, improve its verification and isolate the disputed claims. This makes corpus growth follow evidence about how problems can be seen.
