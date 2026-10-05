"""Locations of data that lives outside this repository.

Two questions depend on external projects that are not redistributed here:
  warp-one-chess     the Warp 1 engine and its self-play archive   (key: warp_root)
  so-answer-quality  the wave_vector project: poc4_triangulation.py, so_pairs_cache.pkl,
                     so_token_cache.pkl and the trained checkpoint  (key: wave_vector_root)

Configure either by environment variable or by a gitignored external.local.json at the repo root
(copy external.example.json). Every other question and script works from the repo alone.
"""
import json
import os
from pathlib import Path

ATLAS = Path(__file__).resolve().parent.parent
LOCAL = ATLAS / "external.local.json"

KEYS = {
    "warp_root": ("BREADTH_ATLAS_WARP_ROOT",
                  "checkout of the Warp 1 chess project (contains WarpOneChess/ and mini_games/)"),
    "wave_vector_root": ("BREADTH_ATLAS_WAVE_VECTOR_ROOT",
                         "the wave_vector project (poc4_triangulation.py, so_pairs_cache.pkl, so_token_cache.pkl, *.pt)"),
}


def external(key):
    """Path for an external dependency, or a SystemExit with setup instructions."""
    env, what = KEYS[key]
    val = os.environ.get(env)
    if not val and LOCAL.exists():
        val = json.loads(LOCAL.read_text(encoding="utf-8")).get(key)
    if not val:
        raise SystemExit(f"external data not configured: {key} = {what}.\n"
                         f"Set {env}, or copy external.example.json to external.local.json and fill in \"{key}\".")
    path = Path(val).expanduser()
    if not path.exists():
        raise SystemExit(f"external data for {key} not found at {path} ({what}).")
    return path
