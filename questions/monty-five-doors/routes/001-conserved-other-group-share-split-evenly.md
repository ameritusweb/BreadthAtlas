---
id: 001
question: monty-five-doors
title: Conserved other-group share split evenly by symmetry
strategy: new: conserved-share-symmetric-split
contributor: sonnet (duelist A)
date: 2026-10-05
depth: 1
referee: opus/v2
criterion: v2
verdict: VALID
reason: Every step follows from the parents it names, there is no step-by-step state tracing, and the answer 4/15 matches the reference. Because the frontier is empty, all four landmarks are new: the host's reveal leaves my door's chance unchanged, the opened door's chance moves to the three closed doors, those doors are symmetric so they split it equally, and a single switch target gets a third of four fifths.
---

CHAIN by duelist A
1. 🚪 (root) — Given: there are five doors, one hiding a car and four hiding goats.
2. 🎯 (root) — Given: I first pick one door.
3. 🧑‍🎤 (root) — Given: the host knows where the car is, and always opens one of the other four doors to show a goat, never my door and never the car.
4. 🔀 (root) — Given: I then switch to one of the three other closed doors, with no reason to prefer any of them.
5. ❓ (← 1, 2, 3, 4) — Asked: the probability I win the car if I switch. This differs from the familiar version in that there are five doors and I must choose among three remaining closed doors, not one.
6. 🎲 (← 1, 2) — Before the host acts, all doors are equally likely to hide the car. My door holds one share of the chance and the other four doors together hold four shares, so the group of other doors is four times as likely to hold the car as my door.
7. 🛡️ (← 3, 6) — The host's reveal never touches my door and is always a goat, so it tells me nothing new about my door, and my door's chance stays at its small original share.
8. 🪣 (← 3, 7) — The opened door is now known to be a goat, so it holds no chance. The big chance held by the other-door group, which is not changed by the reveal, now sits entirely on the three closed doors.
9. ⚖️ (← 3, 8) — Nothing in the host's rule favors any of those three closed doors over another, so they are symmetric and must share that chance equally.
10. 🍰 (← 8, 9) — So each of the three closed doors holds an equal third of the big other-group chance.
11. 🏁 (← 6, 7, 10) — The other-group's chance is four fifths, so one door among the three has a third of four fifths. That is four fifteenths.
12. 👀 (← 7, 11) — Self-check: this is better than staying, which stays at one fifth, and less than four fifths, which is the chance if I could take all the other closed doors at once. A single door out of three should land in between, and four fifteenths does.

LANDMARKS:
- The host's reveal leaves my door's chance unchanged, while the group of the other four doors keeps four times its chance.
- The opened goat door's chance moves entirely onto the three remaining closed doors.
- By symmetry the three closed doors split the other-group's chance equally.
- A single switch target gets a third of four fifths, which sits between staying and taking all the other doors.

ANSWER: 4/15
