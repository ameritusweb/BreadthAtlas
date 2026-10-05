---
id: 001
question: three-view-solid
title: Base U-prism faces plus step-cut additions, counted
strategy: new: base-solid-plus-cuts
contributor: sonnet (blind player 1)
date: 2026-10-05
depth: 1
referee: opus/v1
criterion: v1
verdict: VALID
reason: Every step follows from its parents and matches the drawing, and the answer of twelve is exact. All three landmarks are new because no chain has been played yet: the U-profile slot running the full depth, the full-width step at the back bottom, and the ten-face U-prism plus a riser and tread with no face split.
typed_1: structure | front view | U-shaped through-slot | = | top view | The front view shows a U-shaped profile, and the top view shows the slot runs the full depth.
typed_2: structure | right-side view | full-width step cut | = | dashed lines | The right-side view and the dashed lines show a full-width step cut at the back bottom.
typed_3: size | face count | twelve | = | U-prism ten faces | The U-prism has ten faces, and the step adds a riser and a tread without splitting any other face.
---

CHAIN by blind player 1
1. 📐 (root) — Given: the drawing shows the top, front and right-side views of one solid in third-angle projection, and every face is flat with every edge parallel to an axis.
2. 🔍 (root) — Given: solid lines are visible edges and dashed lines are hidden edges.
3. ❓ (← 1, 2) — Asked: how many flat faces does the solid have, counting each flat region once whatever its outline?
4. 🟦 (← 1, 3) — The front view is a square with a rectangular notch cut down from the top in the middle, so the solid's profile along the viewing direction is a U shape.
5. 🔳 (← 2, 4) — The top view has two solid vertical lines that line up with the notch walls and run from front to back, so the notch is a slot running the full depth of the solid.
6. 🪜 (← 2, 5) — The right-side view shows the lower back corner stepped inward. The dashed lines across the full width in the top and front views show this step cut spans the whole width.
7. 🧱 (← 4, 5) — The U-shaped prism before the step cut has these faces: front end, back end, bottom, left side, right side, left top strip, right top strip, slot floor, and two slot walls.
8. ✂️ (← 6) — The step cut removes a low strip from the back bottom edge. It adds one new vertical riser face and one new horizontal tread face.
9. 🔁 (← 7, 8) — The cut neither splits nor merges any existing face. The back end stays one U-shaped piece, the bottom stays one piece, and each outer side becomes one L-shaped piece.
10. 🧮 (← 7, 8, 9) — Counting every face one by one gives all the prism faces plus the riser and the tread, which is twelve in total.
11. 👀 (← 5, 10) — Self-check: the top view shows three strips, which are the two top strips and the slot floor, matching the faces listed. The dashed line at the step matches the riser and tread.
12. 🎯 (← 10) — The solid has twelve faces.

LANDMARKS:
- The front view shows a U-shaped profile, and the top view shows the slot runs the full depth.
- The right-side view and the dashed lines show a full-width step cut at the back bottom.
- The U-prism has ten faces, and the step adds a riser and a tread without splitting any other face.

ANSWER: 12
