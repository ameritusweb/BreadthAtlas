# Curator notes — unjudged candidate

This file contains solution hypotheses. It is not a played route, is not scored, and must not be supplied as player input.

## Candidate chain

1. 📋 (root) — None of tasks A, B, and C has started.
2. 🔗 (root) — A requires B finished, B requires C finished, and C requires A finished before starting.
3. ⏳ (root) — Each completion requires a positive duration after its task starts, and prerequisites cannot be waived.
4. ❓ (← 1, 2, 3) — Can a schedule finish all three tasks?
5. 🧪 (← 4) — Suppose such a successful schedule exists.
6. 🥇 (← 1, 3, 5) — Among the required starts there must be an earliest starting time.
7. 🔒 (← 2, 6) — Any task starting then requires a different task already finished.
8. 🕰️ (← 3, 7) — That finished task must have started strictly earlier.
9. 💥 (← 6, 8) — This contradicts the earliest starting time, even if some starts are simultaneous.
10. 🚫 (← 5, 9) — No successful schedule exists.
LANDMARKS:
- Any successful schedule has an earliest task start.
- Every possible first start requires a strictly earlier start.
ANSWER: No.

## Other conceptual spines to investigate

earliest-event contradiction; strict-order cycle

## Boundary variant

Remove C's prerequisite; complete C, then B, then A.
