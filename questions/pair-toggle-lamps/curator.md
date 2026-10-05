# Curator notes — unjudged candidate

This file contains solution hypotheses. It is not a played route, is not scored, and must not be supplied as player input.

## Candidate chain

1. 💡 (root) — Six lamps are initially off.
2. 🔄 (root) — A move toggles any two distinct lamps.
3. ❓ (← 1, 2) — Can a sequence leave exactly one lamp on?
4. ➕ (← 2) — Toggling two off lamps adds a pair of lit lamps.
5. ➖ (← 2) — Toggling two on lamps removes a pair of lit lamps.
6. ↔️ (← 2) — Toggling a mixed pair moves the lit state without changing how many lamps are on.
7. ⚖️ (← 4, 5, 6) — Every move preserves whether the lit lamps can be paired without a leftover.
8. 🔒 (← 1, 7) — Starting from none, every reachable configuration has an even number of lit lamps.
9. ⚫ (← 3) — Exactly one lit lamp would be an unpaired leftover.
10. 💥 (← 8, 9) — The proposed target violates the preserved parity.
LANDMARKS:
- Every allowed toggle preserves lit-count parity.
- The initial configuration and the single-lamp target have different parity.
ANSWER: No.

## Other conceptual spines to investigate

parity invariant; reachability obstruction

## Boundary variant

Allow a move toggling one lamp; the target becomes reachable immediately.
