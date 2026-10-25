"""Question content registry. Importing the chapter modules registers their templates."""
import importlib
import pkgutil

# every module in this package except base registers questions on import (calc_ch*, explain_ch*, recall*, written_ch*)
for _name in sorted(m.name for m in pkgutil.iter_modules(__path__)):
    if _name != "base":
        importlib.import_module(f"{__name__}.{_name}")
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
