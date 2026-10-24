"""Question content registry. Importing the chapter modules registers their templates."""
from . import calc_ch1, calc_ch2, calc_ch3, calc_ch4, calc_ch5, calc_ch6, calc_ch9, calc_ch10, recall, recall2, written_ch1, written_ch2, written_ch3, written_ch4, written_ch5, written_ch6, written_ch7, written_ch8, written_ch9, written_ch10  # noqa: F401
from .base import TEMPLATES, Question, Template


def chapters_with_content(category: str):
    return sorted({t.chapter for t in TEMPLATES if t.category == category})


def inventory():
    """{(category, chapter): {level: count}}"""
    out = {}
    for t in TEMPLATES:
        out.setdefault((t.category, t.chapter), {}).setdefault(t.level, 0)
        out[(t.category, t.chapter)][t.level] += 1
    return out


__all__ = ["TEMPLATES", "Question", "Template", "chapters_with_content", "inventory"]
