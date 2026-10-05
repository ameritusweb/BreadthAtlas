# Scope — Warp 1 Chess as an atlas question with an empirical referee

## Why this question is different

Every question so far has a referee that *judges*. This one has a referee that *plays*. A route's
central claim — "from this position White wins by mechanism M along line L" — is executable: the
project's own `WarpBoard` can replay the line, confirm every move is legal, confirm the final
position is checkmate, and search Black's alternatives to confirm the win is forced. That verdict
cannot be argued with, which makes this the strongest soundness check in the atlas and the model for
every future game-domain question (Pokemon leads, Go joseki, any engine-checkable claim).

Source: the Warp 1 chess project (external; `warp_root` in `external.local.json`) — an engine (`WarpOneChess/board.py`, model-free legal-move
generation, FEN in/out), a self-play checkpoint (`checkpoints/warp1_selfplay_iter_294.pt`), and
`mini_games/iter_*/line_*/game_NNN_<result>.txt`: hundreds of engine-discovered forced wins, each a
start FEN plus a ~9-ply line to checkmate.

## The rules, as the glossary will state them

- Two 8×7 boards, Left and Right, back to back; every square has a mirror square on the other board.
- Standard pieces plus the **crab** (value 3, its own attack pattern).
- A move may **flip**: the piece crosses to its mirror square either before moving (pre-flip) or after
  (post-flip). Notation: `Lc2Rg6=Lg6` — from Lc2 to Rg6, then flipped to Lg6.
- Flips create threats on the *other* board; a king can be captured by a piece arriving from the
  mirror square. Check, mate and stalemate are as in chess but over both boards.

## The question (breadth framing)

Not "what is the best move here" — that has one answer and no breadth. Instead:

> **What distinct winning mechanisms exist in Warp 1?** A route names a mechanism, depicts it as an
> emoji chain, and proves it with one position from the archive and a line from that position to
> checkmate in which the mechanism is the finishing tactic.

Breadth = number of mechanisms with a verified proof. The self-play author's own list (Decapitation,
Rf2 kill zone, cross-board flip finish, pawn nets, crab finishers, bishop diagonals, knight forks)
is the hypothesis; the atlas's DUPLICATE test decides whether those are seven mechanisms or fewer
(Decapitation and flip-finish both end in a flip-capture — same R0 key?).

Players receive a curated set of ~12 positions (FEN + ASCII board + an image rendered from the
board) in the question folder, chosen from the mini-games so that several mechanisms are present.
A route must cite one position by id and give its line in the archive's notation.

## The referee — two halves

1. **Empirical (code, `scripts/warp_referee.py`)** — for the cited position and line:
   - replay with `WarpBoard.from_fen` + `push`; every move must be legal (ILL-FORMED otherwise);
   - the final position must be checkmate for the side to move (WRONG otherwise);
   - **forcedness**: at each Black move in the line, enumerate every legal Black reply and confirm
     White still mates within the remaining plies by a depth-bounded search (alpha-beta over
     `legal_moves`, mate-only evaluation, time-boxed). Three outcomes: `forced`, `not forced` (a
     Black reply escapes — WRONG), or `unverified` (budget exceeded — recorded, route accepted as
     "line verified, forcedness unverified" and flagged for a longer run).
2. **Model referee (as elsewhere)** — judges that the chain's mechanism is what actually happens in
   the verified line (the typed landmark `construction | king | - | flip-capture | mirror square` must
   match the final move's kind), and novelty against accepted mechanisms via typed landmarks. Form is
   the standard chain grammar; the ❓ step is "which mechanism wins here?"; no calculation means no
   engine search in the chain — the player must *see* the mechanism; the referee does the searching.

Precedent to write into REFEREE.md: "a route whose line fails the engine is WRONG however elegant
its chain; a route whose chain describes a different mechanism from the one its line executes is
WRONG; the engine verdict is final on soundness, the model referee on mechanism and novelty."

## Glossary (draft)

| emoji | mechanism |
|---|---|
| 🌀 | cross-board flip: a piece arrives from the mirror square |
| 👑 | king as weapon (the "Decapitation") |
| 🪞 | mirror-square threat: attack a square via its twin |
| 🫁 | smother: escape squares covered, then strike |
| 🎯 | kill zone: a square the defender cannot cover (f2) |
| 🦀 | crab-specific tactic |
| ♟️ | pawn net / promotion threat |
| 🔱 | fork |
| 📐 | diagonal battery |
| 🚪 | back-rank / open-file break |

## What to build (in order)

1. `scripts/warp_pick_positions.py` — scan `mini_games`, select ~12 start FENs with short forced
   mates (≤ 9 plies) and varied final-move kinds (flip capture, pawn, crab, knight, bishop, rook,
   king), write `questions/warp-one-chess/positions/NN.md` (FEN, ASCII board, the archive's line as
   the reference, kind of finish) and a `positions/index.md` for players (FEN + board only; no lines).
2. `scripts/warp_referee.py` — replay + mate check + bounded forcedness; CLI: `warp_referee.py <fen>
   "<line>"` → `forced | not forced | unverified`, with the escaping reply if any.
3. `play.py` hook: for questions with `referee_script:` in frontmatter, run the script on the route's
   cited position and line *before* the model referee; its result is injected as a FORM NOTE / verdict
   override (WRONG on `not forced` or illegal; ILL-FORMED on unparseable line).
4. Question entry `question.md` with the glossary above, the rules, the answer format (mechanism +
   position id + line), and `status: answered` (each route's answer is definite: a verified line).
5. First game: blind, 3 players, Opus (the Sonnet runs read ring orders off single views; this needs
   the same kind of seeing).

Effort: 1–2 are a few hours (the board API is clean; move parsing from the archive notation is the
one piece to confirm); 3 is small; 4 is writing. Rendering board images needs either the project's
`gui.py` (tkinter) or a small PIL renderer over `piece_map()` — PIL, ~60 lines.

## What this adds to the atlas

- A third referee type (empirical) with an explicit precedence rule over the model referee.
- The first question whose breadth is *mechanisms with proofs*, the shape every game domain shares.
- A direct bridge to the strategy catalogue: `smother-then-strike` would get its first instance here
  and a cross-domain twin in `balance-five-objects` (🫙 containment: neutralize, then arrange).
- A legibility layer over self-play: the engine found these mechanisms as weights; the archive names
  them as chains and proves each with one line.
