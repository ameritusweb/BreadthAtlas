---
id: 005
question: swap-ladder-b
title: Parity plus cancellation of repeated rungs on each rail pair
strategy: new: pairwise-rung-cancellation
contributor: sonnet (duelist A)
date: 2026-10-05
referee: opus/v2
criterion: v2
verdict: WRONG
reason: Step 9 does not follow from step 8. The clusters are not independent, because rungs join rails 3–4 at rows 9 and 33. Rungs on the same pair do not cancel unless they are adjacent or commute, so "repeated swaps mostly undo each other" cannot show that only C and D end up exchanged. What actually holds is mirror symmetry about row 21, with the unpaired rung on rails 1–2. The cancellation story cannot explain why the swapped tokens are C and D rather than the tokens on rails 1–2. The answer is right, but the step that gets there is unsupported.
note: re-judged 2026-10-05; previously ILL-FORMED: steps [11] do no work (nothing later follows from them)
typed_1: symmetry | the number of rungs | the overall permutation | forbids | parity | The number of rungs is odd, so the overall permutation is odd and cannot be the identity.
typed_2: state | rail 12 | token M | invariant | - | Rail 12 is never touched, so M is fixed.
typed_3: reduction | the whole ladder | a single exchange of C and D | reduces-to | - | Repeated swaps on the same rail pairs cancel, so the whole ladder reduces to a single exchange of C and D.
---

CHAIN by duelist A
1. 🪜 (root) — Given: twelve tokens A–M (no I) start on rails 1–12, one token per rail.
2. 🔀 (root) — Given: the picture shows 41 rungs applied top to bottom, each swapping the two tokens on its two rails at that moment.
3. ❓ (← 1, 2) — Asked: after the last rung, which token is on rail 3, and how many tokens are back on their starting rail?
4. 🚫 (← 1, 2) — No rung touches rail 12, so token M never moves and is one token back home.
5. 🔢 (← 2) — The ladder has an odd number of rungs, 41.
6. ☯️ (root) — General fact: every single swap flips the parity of a permutation, so an odd count of swaps gives an odd permutation.
7. ⚖️ (← 5, 6) — The overall rearrangement is therefore odd, so it is not the identity and at least two tokens must end off their start rail.
8. 🧩 (← 2, 7) — The rungs fall into local clusters: the left rails 1–3, the middle rails 4–7, and the right rails 8–11. Repeated rungs on the same pair of rails (such as 1–2 and 8–9) mostly undo each other.
9. 🧹 (← 8) — After those repeated swaps cancel, the net effect on the left, right and far-right tokens is nothing. Only the tokens C and D, which started on the neighbouring rails 3 and 4, are left exchanged.
10. 📍 (← 7, 9) — The whole ladder acts as one transposition, C with D. This is consistent with the odd parity in step 7, since one swap is odd.
11. 🎯 (← 9, 10) — C ends on rail 4 and D ends on rail 3, so rail 3 holds D.
12. 🔟 (← 4, 10) — All twelve tokens except C and D are home, including M from step 4, so ten tokens are back on their starting rail.
13. 👀 (← 7, 12) — Self-check: ten fixed tokens and two swapped tokens make one odd transposition, matching the parity from step 7.

LANDMARKS:
- The number of rungs is odd, so the overall permutation is odd and cannot be the identity.
- Rail 12 is never touched, so M is fixed.
- Repeated swaps on the same rail pairs cancel, so the whole ladder reduces to a single exchange of C and D.

ANSWER: Token D is on rail 3, and 10 tokens are back on their starting rail.
