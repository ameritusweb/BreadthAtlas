---
id: 003
question: monty-five-doors
title: Weigh locations by how well each explains the reveal
strategy: new: likelihood-weighting (Bayes by explanatory power)
contributor: sonnet (duelist B)
date: 2026-10-05
depth: 3
referee: opus/v2
criterion: v2
verdict: VALID
reason: The chain is correct. It weighs each possible car location by how likely the host was to make this particular opening (one in four if the car is behind my door, one in three if it is behind a given closed door), which gives weights of 3:4:4:4:0 and the answer 4/15. Its first two landmarks are new: the host-likelihood comparison and the four-to-three weighting. No earlier chain uses how likely the host's opening was. The "fifteen parts" sum is no more calculation than route 001's "a third of four fifths", so it passes the no-calculation rule.
typed_1: rate | the host's particular opening given the car behind my door | the host's particular opening given the car behind a closed door | ≪ | - | The host's particular opening is less likely when the car is behind my door, since he had four options, than when it is behind a given closed door, where he had three.
typed_2: share | each closed door's weight | my door's weight | = | four to three | Each closed door therefore outweighs my door in the ratio four to three, and the opened door has no weight.
typed_3: share | a single switch target's chance | all the weight | = | fifteen equal parts | The weights split into equal parts, three for my door and four for each closed door, so one switch target holds four of the fifteen parts.
---

CHAIN by duelist B
1. 🚪 (root) — Given: there are five doors, one hiding a car and four hiding goats.
2. 🎯 (root) — Given: I first pick one door, and before anything happens every door is equally likely to hide the car.
3. 🧑‍🎤 (root) — Given: the host knows where the car is and opens one of the other four doors, always showing a goat, never my door and never the car.
4. 🔀 (root) — Given: I then switch to one of the three remaining closed doors, picking among them with no preference.
5. ❓ (← 1, 2, 3, 4) — Asked: the probability I win the car if I switch. This differs from the familiar version in that there are five doors and three closed doors to choose among, not one.
6. 👁️ (← 3, 5) — I have seen the host open one particular goat door, so I ask, for each place the car could be, how likely the host was to make exactly this opening.
7. 🏠 (← 2, 6) — If the car is behind my door, the host could have opened any of four other doors. Opening this particular one was only one choice among four, so it was fairly unlikely.
8. 🚫 (← 3, 6) — The car cannot be behind the opened door, because the host never reveals the car. That location is ruled out entirely.
9. 🔍 (← 3, 6) — If the car is behind one particular closed door, the host could not open my door or that door. His choice was then among only three doors, so this particular opening was more likely than in the case where my door holds the car.
10. ⚖️ (← 1, 7, 9) — All locations started equally likely, so after the sighting the weights differ only by how well each explains it. Each closed door beats my door in the ratio four to three.
11. 🧱 (← 8, 10) — In equal-sized parts, my door holds three, each of the three closed doors holds four, and the opened door holds none.
12. 🏁 (← 4, 11) — All parts together make fifteen, and switching to one closed door gets four of them, so my chance is four fifteenths.
13. 👀 (← 12) — Self-check: a closed door is a bit better than my door, which is about one fifth, and far below all three closed doors together. Four fifteenths is just above one fifth, as expected.

LANDMARKS:
- The host's particular opening is less likely when the car is behind my door, since he had four options, than when it is behind a given closed door, where he had three.
- Each closed door therefore outweighs my door in the ratio four to three, and the opened door has no weight.
- The weights split into equal parts, three for my door and four for each closed door, so one switch target holds four of the fifteen parts.

ANSWER: 4/15
