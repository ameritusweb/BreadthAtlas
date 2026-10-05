import math
import re

# Mechanism: coverage of distinct content kinds. Each kind counts once, however
# much of it the answer contains. A bounded vocabulary term only breaks ties.

_CODE_BLOCK = re.compile(r"<pre\b|```|^(?: {4}|\t)\S", re.I | re.M)
_INLINE_CODE = re.compile(r"<code\b|`[^`\n]+`", re.I)
_LINK = re.compile(r"<a\s[^>]*href|https?://", re.I)
_LIST = re.compile(r"<(?:ul|ol)\b|^\s*(?:[-*+]|\d+[.)])\s+\S", re.I | re.M)
_EMPHASIS = re.compile(r"<h\d\b|<strong\b|<b>|<em\b|\*\*|^#{1,6}\s", re.I | re.M)
_CAVEAT = re.compile(
    r"\b(?:however|note|caveat|warning|beware|careful|unless|except|avoid|deprecated)\b",
    re.I,
)
_REASON = re.compile(
    r"\b(?:because|since|the reason|so that|this means|which means|therefore)\b", re.I
)
_EXAMPLE = re.compile(
    r"\b(?:for example|e\.g\.|for instance|example|output|prints|returns)\b", re.I
)

_STRIP_BLOCKS = re.compile(r"<pre\b.*?</pre>|```.*?```", re.I | re.S)
_STRIP_TAGS = re.compile(r"<[^>]+>")
_WORD = re.compile(r"[A-Za-z_]\w*")


def _prose_words(text: str) -> int:
    prose = _STRIP_BLOCKS.sub(" ", text)
    prose = _STRIP_TAGS.sub(" ", prose)
    return len(_WORD.findall(prose))


def score(question: str, answer: str) -> float:
    text = answer or ""
    kinds = 0
    kinds += 1 if _prose_words(text) >= 20 else 0
    for pat in (_CODE_BLOCK, _INLINE_CODE, _LINK, _LIST, _EMPHASIS,
                _CAVEAT, _REASON, _EXAMPLE):
        kinds += 1 if pat.search(text) else 0

    vocab = len(set(w.lower() for w in _WORD.findall(_STRIP_TAGS.sub(" ", text))))
    tie_break = 0.9 * min(1.0, math.log1p(vocab) / math.log(2001.0))
    return float(kinds) + tie_break
