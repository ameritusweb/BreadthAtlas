---
id: 001
question: turntable-solid
title: Outer and inner rings, notches, order from midpoint tracking
strategy: new: ring-separation-and-midpoint-interpolation
contributor: opus (blind player 1)
date: 2026-10-05
depth: 1
referee: opus/v1
criterion: v1
verdict: VALID
reason: All the readings hold in the image (step 4's vertical pairings, step 6's swapping and mirroring of the outer slots, step 8's leaning toward a midpoint in all four views, step 11's hidden HW in View A), and the ten faces are the correct star-slab answer. New landmarks are: two rings with very different reach; the inner ring sitting inside the tips' square, which makes the solid a non-convex four-pointed star; and the order fixed by each inner point following the midpoint of its neighbouring tips. No earlier chain passed through any of these.
note: re-judged 2026-10-05 from attempt 003 (ILL-FORMED: step 1 performs arithmetic: 'Four orthographic turntable views (A at θ = 30°; B, C and D …')
typed_1: share | outer labels | outer slots | invariant | inner slots | The outer labels (NZ, EV, KA, GD) always take the outer slots and the inner labels (QA, QN, HW, XS) always take the inner slots, so there are two rings with very different reach.
typed_2: structure | inner ring | outer tip square | ≪ | edge distance | The inner ring lies well inside the square formed by the outer tips, so the cross-section is non-convex: a four-pointed star.
typed_3: structure | inner ring | outer labels | alternates | cyclic order | Each inner point follows the midpoint of two neighbouring tips across the views (QA follows NZ and EV, QN follows GD and NZ), which fixes the order NZ, QA, EV, XS, KA, HW, GD, QN.
typed_4: obstruction | HW | convex prism | forbids | - | HW is hidden between two visible tips in View A, which confirms that it is a notch.
---

CHAIN by blind player 1
1. 🖼️ (root) — Four orthographic turntable views (A at θ = 30°; B, C and D at unknown angles) show sixteen labelled points of one solid, with filled dots for visible points and hollow dots for hidden ones.
2. 📏 (root) — In every view, eight labels sit on an upper line and eight on a lower line, and their horizontal positions always come from the same eight slots: a far pair, a second pair, an inner pair and a near-centre pair, mirrored about the axis.
3. ❓ (← 1, 2) — What is the solid, given as each face's list of point labels? The angles of three views are unknown, and the solid need not be a convex prism.
4. 🔗 (← 2) — In every view, each upper label shares its horizontal slot with one fixed lower label (NZ–UF, EV–CY, QA–HE, QN–EL, XS–WA, HW–CZ, GD–AZ, KA–KL), so these pairs are vertical edges and the solid is a straight extrusion.
5. 🪐 (← 2) — In all four views, NZ, EV, KA and GD only ever take the far and second slots, and QA, QN, HW and XS only ever take the inner and near-centre slots, so they form an outer ring and an inner ring that reaches less than half as far.
6. ✚ (← 5) — Within the outer ring, NZ and EV swap between the far and second slots from view to view, and KA and GD always mirror them; this is how two equal arms at right angles behave, so the outer four are the tips of a square cross.
7. 🎯 (← 5, 6) — A square's edges pass the centre at about seven-tenths of its tip distance, but the inner ring sits at less than half that distance, so the inner points lie well inside the outer square and must be notches.
8. 🧭 (← 5, 6) — In every view, QA leans the same way as the midpoint of NZ and EV: strongly when both lean the same way, and weakly when they disagree. QN does the same with NZ and GD, so QA sits between NZ and EV, and QN between GD and NZ.
9. 🔄 (← 6, 8) — Because the cross mirrors through the centre, XS sits between EV and KA, and HW between KA and GD, which gives the cyclic order NZ, QA, EV, XS, KA, HW, GD, QN.
10. ⭐ (← 7, 9) — The cross-section alternates outer tips with inner notches, so it is a non-convex four-pointed star, not a convex octagon.
11. 👀 (← 9, 10) — Check: in View A, HW is hidden while its flanking tips GD and KA are both visible. That is impossible for a convex prism, but it is exactly what a notch tucked between two tips produces.
12. 🏗️ (← 4, 9, 10) — Joining the star outline on top to its partner outline below gives two star-shaped caps and eight rectangular side walls, one for each star edge.
LANDMARKS:
- The outer labels (NZ, EV, KA, GD) always take the outer slots and the inner labels (QA, QN, HW, XS) always take the inner slots, so there are two rings with very different reach.
- The inner ring lies well inside the square formed by the outer tips, so the cross-section is non-convex: a four-pointed star.
- Each inner point follows the midpoint of two neighbouring tips across the views (QA follows NZ and EV, QN follows GD and NZ), which fixes the order NZ, QA, EV, XS, KA, HW, GD, QN.
- HW is hidden between two visible tips in View A, which confirms that it is a notch.
ANSWER: A four-pointed-star prism. Faces: top [NZ, QA, EV, XS, KA, HW, GD, QN]; bottom [UF, HE, CY, WA, KL, CZ, AZ, EL]; sides [NZ, QA, HE, UF], [QA, EV, CY, HE], [EV, XS, WA, CY], [XS, KA, KL, WA], [KA, HW, CZ, KL], [HW, GD, AZ, CZ], [GD, QN, EL, AZ], [QN, NZ, UF, EL].
