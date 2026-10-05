---
id: 002
question: pair-toggle-lamps
title: Graph degree view with handshake double counting
strategy: new: handshake-double-counting
contributor: sonnet (blind player 2)
date: 2026-10-05
depth: 2
referee: opus/v2
criterion: v2
verdict: VALID
reason: The argument is sound and does no step-by-step simulation. It reads the whole move sequence as one graph and counts all the line-ends at once, never tracking state move by move. Two of its landmarks are not in route 001's set: the reduction "lamp on ⇔ its dot has odd degree" and the double count "total line-ends is even". Route 001 instead used an invariant that holds after every move.
discriminator_depicted: no
typed_1: reduction | a lamp's lit state | parity of its dot's degree | reduces-to | - | Moves are lines between lamp-dots, and a lamp is on exactly when its dot has an odd number of lines (a graph degree view).
typed_2: structure | the total of line-ends | twice the number of moves | = | - | Double counting: every line has two ends, so the total of line-ends is even.
typed_3: obstruction | the even number of odd-degree dots | the one-lamp target | forbids | - | Handshake principle: the number of odd-degree dots must be even, so exactly one odd dot is impossible.
---

CHAIN by blind player 2
1. 💡 (root) — There are six lamps, all initially off.
2. 🔀 (root) — Each move picks two distinct lamps and toggles both.
3. ❓ (← 1, 2) — 6️⃣💡 all off, then paired toggles: can exactly 1️⃣ lamp end up on?
4. 🕸️ (← 2) — Draw each lamp as a dot and each move as a line joining the two chosen dots. A whole sequence of moves is then a bundle of lines, and repeated pairs are separate lines.
5. 👆 (← 2, 4) — Each line touches exactly two dots, so every move adds exactly two line-ends in all.
6. 🧮 (← 5) — The total number of line-ends over all dots is therefore even, because it is built from pairs.
7. 🔁 (← 1, 4) — A lamp starts off and flips on each touch. It is on exactly when its dot has an odd number of line-ends.
8. 🔆 (← 3, 7) — Exactly one lamp on would mean exactly one dot has an odd number of line-ends, and the other five have even numbers.
9. ➕ (← 8) — Five even counts plus one odd count give an odd total number of line-ends.
10. 👀 (← 4, 7) — Self-check: a repeated pair gives two lines on the same dots, so it adds an even count to each dot and the argument still holds.
11. 💥 (← 6, 9) — The total must be both even and odd, which is a contradiction.

LANDMARKS:
- Moves are lines between lamp-dots, and a lamp is on exactly when its dot has an odd number of lines (a graph degree view).
- Double counting: every line has two ends, so the total of line-ends is even.
- Handshake principle: the number of odd-degree dots must be even, so exactly one odd dot is impossible.
ANSWER: No
