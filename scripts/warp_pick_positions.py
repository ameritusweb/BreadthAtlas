"""Pick a diverse set of forced-win positions from the Warp 1 self-play archive.

  python scripts/warp_pick_positions.py [--count 12] [--max-plies 9]

Scans <warp_root>/mini_games/*/*/game_*_White_wins_checkmate.txt (see scripts/external.py), parses the start FEN
and the line, replays it on the engine to confirm legality and checkmate, classifies the finishing
move (piece type, flip, capture), and writes:
  questions/warp-one-chess/positions/<id>.md   (fen, board, archive line, finish kind — referee only)
  questions/warp-one-chess/positions/index.md  (fen + board only — what players see)
Diversity: prefer the shortest lines, at most `count // 4` positions per finish kind.
"""
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from external import external  # noqa: E402

WARP_ROOT = external("warp_root")
sys.path.insert(0, str(WARP_ROOT))
from WarpOneChess.board import WarpBoard  # noqa: E402
from WarpOneChess.move import PIECE_NAMES, NO_FLIP  # noqa: E402

ATLAS = Path(__file__).resolve().parent.parent
OUT = ATLAS / "questions" / "warp-one-chess" / "positions"


def legal(board):
    lm = board.legal_moves
    return lm() if callable(lm) else lm


def parse_game(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    start = re.search(r"^Start:\s*(.+)$", text, re.M)
    moves = re.findall(r"^\s*\d+\.\s*[WB]\s+(\S+)", text, re.M)
    if not start or not moves:
        return None
    return start.group(1).strip(), moves


def classify_final(board, move):
    pt, color = board.piece_at(move.from_square)
    name = {v: k for k, v in PIECE_NAMES.items()}  # not needed; use PIECE_NAMES directly
    piece = PIECE_NAMES.get(pt, "?")
    cap = board.is_capture(move) if callable(board.is_capture) else False
    flip = "flip" if move.flip_type != NO_FLIP else "noflip"
    return f"{piece}-{flip}-{'capture' if cap else 'quiet'}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=12)
    ap.add_argument("--max-plies", type=int, default=9)
    ap.add_argument("--verify", type=float, default=0, help="seconds per candidate for the forcedness search; keep only proved wins")
    ap.add_argument("--tail", type=int, default=0, help="use the position this many plies before the final mate as the start (odd: 3, 5, 7); 0 = the archive's start position")
    args = ap.parse_args()
    if args.verify:
        from warp_referee import verify as verify_line
    OUT.mkdir(parents=True, exist_ok=True)

    candidates = []
    files = sorted((WARP_ROOT / "mini_games").glob("*/*/game_*_White_wins_checkmate.txt"))
    for f in files:
        parsed = parse_game(f)
        if not parsed:
            continue
        fen, moves = parsed
        if len(moves) % 2 == 0:
            continue
        if args.tail:
            if len(moves) < args.tail:
                continue
            # replay the prefix to reach the position `tail` plies before mate; the tail becomes the line
            try:
                b0 = WarpBoard.from_fen(fen)
                for tok in moves[:len(moves) - args.tail]:
                    mv = next((x for x in legal(b0) if x.uci() == tok), None)
                    if mv is None:
                        raise ValueError(tok)
                    b0.push(mv)
                fen, moves = b0.to_fen(), moves[len(moves) - args.tail:]
            except Exception:  # noqa: BLE001
                continue
        elif len(moves) > args.max_plies:
            continue
        try:
            board = WarpBoard.from_fen(fen)
            if not board.turn:  # must be White to move
                continue
            ok = True
            final_kind = None
            for i, tok in enumerate(moves):
                m = next((x for x in legal(board) if x.uci() == tok), None)
                if m is None:
                    ok = False
                    break
                if i == len(moves) - 1:
                    final_kind = classify_final(board, m)
                board.push(m)
            if not ok or not (board.is_checkmate() if callable(board.is_checkmate) else board.is_checkmate):
                continue
        except Exception as err:  # noqa: BLE001
            continue
        candidates.append({"file": f, "fen": fen, "moves": moves, "kind": final_kind, "plies": len(moves)})

    candidates.sort(key=lambda c: (c["plies"], str(c["file"])))
    if args.verify:
        proved = []
        tally = defaultdict(int)
        for c in candidates:
            res = verify_line(c["fen"], c["moves"], args.verify)
            status = res.split("—")[0].replace("EMPIRICAL:", "").strip()
            tally[status] += 1
            if status == "forced":
                c["proof"] = res
                proved.append(c)
            if len(proved) >= args.count * 3:
                break
        print(f"forcedness over {sum(tally.values())} candidates: {dict(tally)}")
        candidates = proved
    per_kind = defaultdict(int)
    cap = max(1, args.count // 4)
    chosen = []
    for c in candidates:
        if per_kind[c["kind"]] >= cap:
            continue
        per_kind[c["kind"]] += 1
        chosen.append(c)
        if len(chosen) >= args.count:
            break

    index = ["# Positions — Warp 1, White to move, a forced win exists", "",
             "Cite a position by its id. Boards: Left side then Right side, rank 7 at top; uppercase = White.", ""]
    for n, c in enumerate(chosen, 1):
        pid = f"P{n:02d}"
        board = WarpBoard.from_fen(c["fen"])
        ascii_board = repr(board)
        (OUT / f"{pid}.md").write_text(
            f"---\nid: {pid}\nfen: {c['fen']}\nplies: {c['plies']}\nfinish: {c['kind']}\nsource: {c['file'].relative_to(WARP_ROOT)}\ntail: {args.tail}\narchive_line: {' '.join(c['moves'])}\nproof: {c.get('proof', 'not verified')}\n---\n\n```\n{ascii_board}\n```\n", encoding="utf-8")
        index += [f"## {pid}", "", f"FEN: `{c['fen']}`", "", "```", ascii_board, "```", ""]
    (OUT / "index.md").write_text("\n".join(index), encoding="utf-8")
    print(f"scanned {len(files)} games, {len(candidates)} verified candidates, chose {len(chosen)}:")
    for n, c in enumerate(chosen, 1):
        print(f"  P{n:02d}  {c['plies']} plies  {c['kind']}  {c['file'].parent.parent.name}/{c['file'].parent.name}/{c['file'].name}")


if __name__ == "__main__":
    main()
