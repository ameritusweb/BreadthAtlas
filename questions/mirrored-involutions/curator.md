# Curator notes — unjudged candidate

This file contains solution hypotheses. It is not a played route, is not scored, and must not be supplied as player input.

## Candidate chain

1. 🎛️ (root) — Actions A, B, and C are always legal and deterministic.
2. ↩️ (root) — Applying any one of these actions twice consecutively restores the state it acted on.
3. 📜 (root) — The sequence is A, B, C, C, B, A, and the actions need not commute.
4. ❓ (← 1, 2, 3) — Must the sequence restore every starting state?
5. 🪞 (← 3) — The action sequence mirrors itself around the adjacent C pair.
6. ✂️ (← 1, 2, 5) — The adjacent C pair can be removed without changing the sequence's effect.
7. 🔗 (← 3, 6) — Removing that pair exposes the B pair as adjacent operations.
8. ✂️ (← 1, 2, 7) — The exposed B pair can also be removed without changing the effect.
9. ✅ (← 2, 3, 8) — Only the A pair remains, and it restores its input state.
10. 🔒 (← 6, 8, 9) — Cancellation from the middle outward restores the starting state without reordering actions.
LANDMARKS:
- Adjacent self-inverse actions cancel regardless of the surrounding state.
- The mirrored sequence exposes cancelling pairs from the centre outward without commutation.
ANSWER: Yes.

## Other conceptual spines to investigate

mirror cancellation; nested restoration

## Boundary variant

Make C reversible but not self-inverse; the repeated C pair need not cancel. A and B as identity actions and C as a quarter-turn give a counterexample.
