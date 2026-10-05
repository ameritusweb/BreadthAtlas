---
id: turntable-solid
title: The solid behind four turntable views
status: answered
added: 2026-10-05
image: puzzle.png
key: answer_key.json
source: derivation benchmark star4 instance (provenance/generators/star4.instance.json), views 30/60/150/240, labels shuffled (seed 7); render with provenance/generators/render_puzzle.py
---

# Question

The image shows four orthographic views (A, B, C and D) of a single solid sitting on a turntable that
rotates about a vertical axis. Sixteen labelled points are plotted in every view, drawn as filled dots
when visible and hollow dots when hidden. Only View A's angle is given (θ = 30°); the angles of Views
B, C and D are unknown. **What is the 3-D solid?**

State the answer as the solid's faces, each as the list of point labels around it.

# Reference answer (referee only)

See `answer_key.json` for the label mapping, face list and per-view visibility. The solid is a
four-pointed star slab: eight side quadrilaterals and two eight-sided caps; a correct answer lists
those ten faces by label. The image is the untilted variant (vertical pairings and four-fold symmetry
intact), chosen deliberately: those are the perceptual handles a non-calculating solver needs.
A tilted, offset variant that removes them exists in the parent folder for calculation-allowed play.

# Why it is in the atlas

An image-based question with a definite answer and an overwhelming pull toward calculation (the grid
invites solving for coordinates). With calculation forbidden, the solid has to be recognised from how
its points slide and occlude between views — the holistic-visual-spatial reasoning the source benchmark
was written to probe. Expected routes include: vertical pairing → slab; occlusion order → outline;
hollow dots → which side the viewer is on (rules out the mirror image); silhouette symmetry → the
star's four-fold structure.

# Breadth

No routes accepted yet. `landmarks.md` is empty.
