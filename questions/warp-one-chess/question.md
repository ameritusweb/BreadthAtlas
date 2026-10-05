---
id: warp-one-chess
title: Winning mechanisms in Warp 1 chess
status: answered
added: 2026-10-05
family: game strategy, empirical referee
attractor: the plain chess finish (back-rank mate, queen-and-king) applied without using the flip
referee_script: scripts/warp_referee.py
attach: positions/index.md
source: the Warp 1 chess project, external (engine, self-play checkpoint iter_294, mini_games archive); path via external.local.json key warp_root
---

# Question

Warp 1 is chess on two 8×7 boards back to back. Every square has a mirror square on the other board;
a piece may flip to its mirror either before or after it moves, and flips create threats across the
boards. There is one extra piece, the crab. The positions in `positions/` are Warp 1 positions with
White to move and a forced win available.

**Name a winning mechanism, show it as a chain, and prove it: cite one position by id and give a line
from that position to checkmate in which your mechanism is the finishing tactic.** Each route must
rest on a mechanism different from every accepted route's, not on a different position.

Answer format (parsed by the engine referee — exact): `ANSWER: mechanism <name>; position <Pnn>;
line <m1> <m2> … <mN>` with moves in the archive's notation (`La2La4`; pre-flip `La2>Ra2Rb4`;
post-flip `Lc2Rg6=Lg6`; promotion suffix `q`), White's move first, ending in checkmate. The engine
replays the line, checks every move is legal, checks the end is mate, and searches every Black
alternative; an illegal or escapable line is WRONG however good the chain.

# Glossary

See SCOPE.md (draft glossary: 🌀 cross-board flip · 👑 king as weapon · 🪞 mirror-square threat ·
🫁 smother · 🎯 kill zone · 🦀 crab tactic · ♟️ pawn net · 🔱 fork · 📐 diagonal battery · 🚪 open-file
break).

# Reference answer (referee only)

Each position file in `positions/` carries the archive's own line and the kind of its final move.
The empirical referee (`scripts/warp_referee.py`) is final on soundness: the cited line must be legal,
end in checkmate, and be forced against every Black reply within the line's length (or be flagged
`unverified` if the search budget runs out). The model referee rules on whether the chain's mechanism
is the one the line actually executes, and on novelty of mechanism via typed landmarks.

# Breadth

Playable since 2026-10-05 night: 12 positions in positions/, each a proved forced mate in two (36 of 2,271 archive tails were forced; the rest ended in blunders). First game (3 Opus, blind): 3 attempts, all WRONG by the engine — an illegal move, an unforced line
with a quiet tempo, a line blind to Black's flip escape. All three chose the flip mechanic. No routes
yet; the proof lines in the position files remain unmatched by any player.
