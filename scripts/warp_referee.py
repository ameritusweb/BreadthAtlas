"""Empirical referee for warp-one-chess: replays a route's cited line on the Warp 1 engine.

  python scripts/warp_referee.py --question warp-one-chess < chain.txt
  python scripts/warp_referee.py --fen "<fen>" --line "La2La4 Rb7Rb5 ..." [--budget 60]

Reads the chain text from stdin and looks for its ANSWER line:
  ANSWER: mechanism <name>; position <id>; line <m1> <m2> ... <mN>
Loads the position's FEN from questions/<q>/positions/<id>.md (frontmatter `fen:`), replays the
line (White to move first), and prints one final line:
  EMPIRICAL: forced | not forced | unverified | illegal | unparseable — <detail>
"forced" means: every move legal, final position checkmate, and at every Black move in the line every
legal Black reply still loses to a White mate within the remaining plies (depth-bounded search,
time-boxed; budget exhaustion → "unverified").
"""
import argparse
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from external import external  # noqa: E402

WARP_ROOT = external("warp_root")
sys.path.insert(0, str(WARP_ROOT))
from WarpOneChess.board import WarpBoard  # noqa: E402

ATLAS = Path(__file__).resolve().parent.parent


def legal(board):
    lm = board.legal_moves
    return lm() if callable(lm) else lm


def find_move(board, token):
    for m in legal(board):
        if m.uci() == token:
            return m
    return None


def is_mate(board):
    return board.is_checkmate() if callable(board.is_checkmate) else board.is_checkmate


def white_mates_within(board, plies, deadline):
    """White to move. True if White can force mate within `plies` plies (odd). None if out of time."""
    if time.time() > deadline:
        return None
    moves = legal(board)
    # try mating moves first
    for m in moves:
        board.push(m)
        mate = is_mate(board)
        board.pop()
        if mate:
            return True
    if plies <= 1:
        return False
    for m in moves:
        board.push(m)
        ok = black_cannot_escape(board, plies - 1, deadline)
        board.pop()
        if ok is None:
            return None
        if ok:
            return True
    return False


def black_cannot_escape(board, plies, deadline):
    """Black to move. True if every Black reply allows a White mate within `plies - 1`... (plies even)."""
    if time.time() > deadline:
        return None
    replies = legal(board)
    if not replies:
        return is_mate(board)  # already mate (Black has no moves and is in check)
    for r in replies:
        board.push(r)
        res = white_mates_within(board, plies - 1, deadline)
        board.pop()
        if res is None:
            return None
        if not res:
            return False
    return True


def verify(fen, tokens, budget):
    board = WarpBoard.from_fen(fen)
    deadline = time.time() + budget
    plies = len(tokens)
    for i, tok in enumerate(tokens):
        m = find_move(board, tok)
        if m is None:
            return f"EMPIRICAL: illegal — ply {i + 1} '{tok}' is not a legal move in {board.to_fen()[:60]}…"
        if i % 2 == 1:  # Black's move in the line: check all alternatives
            remaining = plies - i  # plies left including this one
            for alt in legal(board):
                if alt.uci() == tok:
                    continue
                board.push(alt)
                res = white_mates_within(board, remaining - 1, deadline)
                board.pop()
                if res is None:
                    return f"EMPIRICAL: unverified — forcedness search exceeded {budget}s at ply {i + 1}"
                if not res:
                    return f"EMPIRICAL: not forced — at ply {i + 1} Black can play {alt.uci()} instead of {tok} and White has no mate within {remaining - 1} plies"
        board.push(m)
    if not is_mate(board):
        return "EMPIRICAL: not forced — the line ends but the final position is not checkmate"
    return f"EMPIRICAL: forced — {plies}-ply line verified: legal throughout, ends in checkmate, every Black alternative loses"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--question", default="warp-one-chess")
    ap.add_argument("--fen")
    ap.add_argument("--line")
    ap.add_argument("--budget", type=float, default=120)
    args = ap.parse_args()

    if args.fen and args.line:
        print(verify(args.fen, args.line.split(), args.budget))
        return

    text = sys.stdin.read()
    m = re.search(r"ANSWER:\s*mechanism\s*(.+?);\s*position\s*([\w\-]+);\s*line\s*(.+)$", text, re.I | re.M)
    if not m:
        print("EMPIRICAL: unparseable — ANSWER line must read: mechanism <name>; position <id>; line <moves>")
        return
    pos_id, line = m.group(2).strip(), m.group(3).strip().rstrip(".")
    pos_file = ATLAS / "questions" / args.question / "positions" / f"{pos_id}.md"
    if not pos_file.exists():
        print(f"EMPIRICAL: unparseable — no position '{pos_id}' in positions/")
        return
    fm = re.search(r"^fen:\s*(.+)$", pos_file.read_text(encoding="utf-8"), re.M)
    if not fm:
        print(f"EMPIRICAL: unparseable — position {pos_id} has no fen")
        return
    tokens = [t for t in re.split(r"[\s,]+", line) if t and not re.match(r"^\d+\.$", t)]
    print(verify(fm.group(1).strip(), tokens, args.budget))


if __name__ == "__main__":
    main()
