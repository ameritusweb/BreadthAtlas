---
id: 008
question: so-answer-quality
title: hand-weighted surface cues dominated by answer length
strategy: new: hand-set-surface-cue-sum
contributor: opus (blind player 1)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: DUPLICATE
reason: [EMPIRICAL: duplicate-of length-chars rho=0.93 acc=0.668] The chain's form is fine and its accuracy (0.668) clears 0.60, but its margins correlate at ρ 0.93 with route 001 (length-chars). Its main landmark, "visible effort, meaning log-scaled length plus runnable code blocks", is in substance route 001's "effort and coverage both grow with length". At 0.668 against roughly two in three, it is not ≥ 0.05 more accurate, so it does not supersede route 001. The claim in step 11 that it is a separate route only asserts novelty and carries no weight.
note: re-judged 2026-10-05; previously ILL-FORMED: only 0 emoji steps; at least 10 required; no ❓ step stating what is asked
---

CHAIN by blind player 1
1. 🧑‍💻❓ (root): Each Stack Overflow question comes with two of its own answers, and the referee scores only the text of the question and of each answer.
2. 🥇➕3️⃣🆚🥉 (root): In each pair, one answer has at least three more votes than the other, and the referee holds out 4,000 such pairs.
3. 🗳️👀📄 (root): People vote after looking at the page, so whatever they reward has to show on the surface of the answer.
4. ❓ (← 1, 2, 3): Using only the raw text and no trained model, which mechanism picks the higher-voted answer of a pair more than six times in ten?
5. 📏 (← 3, 4): Voters tend to reward visible effort, so the answer that explains more usually has more words.
6. 🔤🧮 (← 5): Counting words on a log scale captures that effort and keeps one very long answer from swamping everything else.
7. 🪞💻 (← 3, 4): A block of runnable code is something a reader can copy and use, so an answer with one is more likely to earn votes.
8. 📐📋 (← 3, 7): Lists and links show the answer has been organised and points to references, which adds a smaller signal.
9. 🎯🔤 (← 1, 4): If an answer reuses the question's distinctive terms, it is more likely addressing the question than drifting off topic.
10. 🧹 (← 1, 6, 9): Removing HTML markup and common filler words first means the counts measure what the answer says, not its formatting or "the" and "and".
11. ➕🧩 (← 6, 7, 8, 9, 10): A fixed sum of these hand-set cues needs no fitting and uses no latent or component features, so it is a separate route from the field-evolution voters.
12. 👀 (← 11): Check: none of the cues reads the model's components, percentile ranks or train win-rates, so the route does not depend on the accepted landmarks.
13. ⚖️ (← 11, 2): The margin is how far the two answers' cue sums differ, and its sign picks the winner of each held-out pair.

LANDMARKS:
- Visible effort, meaning log-scaled length plus runnable code blocks, is what voters see and reward.
- Reusing the question's distinctive (rarer, non-filler) terms is a sign the answer is relevant.
- A fixed, hand-set sum of surface cues, with no training and no model components, ranks the pair.



ANSWER: mechanism surface-effort-relevance; scorer scorers/surface_effort_relevance.py
