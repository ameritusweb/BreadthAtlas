---
id: 001
question: ball-in-pipe
title: Fill pipe with water, ball floats up
strategy: new: buoyancy-flotation
contributor: sonnet (blind player 1)
date: 2026-10-05
depth: 1
referee: opus/v2
criterion: v2
verdict: VALID
reason: First chain on this question, so the frontier is empty. Its new landmarks are that the closed rigid pipe holds water, that the ball's density is far below water's, that water reaches under the ball through the gap, and that filling to the rim brings the ball within reach. The steps follow from their parents, there is no calculation or step-by-step state tracking, and the answer is sound: a ping-pong ball floats mostly above the waterline, so it can be grasped at the rim.
typed_1: structure | pipe | water | invariant | cup | The pipe is closed at the bottom and rigid, so it holds water like a cup.
typed_2: size | ball weight | buoyant force | ≪ | - | The ball is far less dense than water, so the water's upward push on it exceeds its weight.
typed_3: structure | water | ball | exists | - | Water can get under the ball through the small gap, so the ball is lifted rather than pinned.
typed_4: construction | water level | ball | reduces-to | - | Raising the water level to the rim floats the ball to where it can be picked out by hand.
---

CHAIN by blind player 1
1. 🏓 (root) — Given: the ball is light, hollow, and floats, and it sits at the bottom of the pipe.
2. 🧪 (root) — Given: the pipe is narrow, rigid, open at the top, closed at the floor, and just wider than the ball.
3. 🏢 (root) — Given: an ordinary office has water, cups, a sink or water bottles, tape, paper, and straws.
4. ❓ (← 1, 2, 3) — Asked: how to get the ball out without damaging the pipe or ball, and which principle it relies on, with each route resting on a different principle.
5. 🌊 (← 1, 3) — Water is available in the office, in bottles, cups, or from a sink, so the pipe can be filled from the top.
6. 🧪 (← 2, 5) — Because the pipe is rigid and closed at the floor, it acts as a watertight container, so poured water stays in and its level rises.
7. 🏓 (← 1, 6) — The ball is hollow and much less dense than water, so the water around it pushes up harder than gravity pulls it down.
8. 🌊 (← 7) — The upward push of the displaced water is greater than the ball's weight, so the ball rises with the water level, and the ball cannot be stuck as it is smooth and not sealed against the wall.
9. 🧪 (← 2, 8) — The gap between ball and wall is small but nonzero, so water can reach under the ball and lift it rather than only pressing from above.
10. 🏢 (← 6, 9) — Keep pouring until the water reaches the rim, and the ball floats at the top where a hand can lift it out.
11. 👀 (← 10) — Self-check: the ball is not damaged by water, and the pipe is not damaged by water, so both constraints hold.

LANDMARKS:
- The pipe is closed at the bottom and rigid, so it holds water like a cup.
- The ball is far less dense than water, so the water's upward push on it exceeds its weight.
- Water can get under the ball through the small gap, so the ball is lifted rather than pinned.
- Raising the water level to the rim floats the ball to where it can be picked out by hand.

ANSWER: Fill the pipe with water from the top; by buoyancy the ball floats up to the rim, where you lift it out by hand.
