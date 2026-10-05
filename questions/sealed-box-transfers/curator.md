# Curator notes — unjudged candidate

This file contains solution hypotheses. It is not a played route, is not scored, and must not be supplied as player input.

## Candidate chain

1. 📦 (root) — Counters occupy boxes in a sealed collection.
2. ⚫ (root) — At least one counter is initially present.
3. 🔄 (root) — Each allowed move transfers a counter between distinct boxes without destruction or escape.
4. ❓ (← 1, 2, 3) — Can a sequence make every box empty?
5. ➖ (← 3) — A transfer removes a counter from its source box.
6. ➕ (← 3) — That same counter is added to the destination box.
7. ⚖️ (← 5, 6) — Every transfer preserves the collection's total.
8. 🔒 (← 3, 7) — Any sequence of allowed transfers preserves the initial total.
9. 🕳️ (← 4) — Emptying every box would leave no counters in the collection.
10. 💥 (← 2, 8, 9) — That target contradicts the preserved presence of counters.
LANDMARKS:
- Every local transfer preserves the global total.
- The all-empty target has a different total from the initial state.
ANSWER: No.

## Other conceptual spines to investigate

conservation; persistence of an initial witness

## Boundary variant

Allow transfers outside the collection; the conserved system boundary changes and emptying becomes possible.
