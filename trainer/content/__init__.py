"""Question content registry. Importing the chapter modules registers their templates."""
from . import calc_ch1, calc_ch2, calc_ch3, calc_ch4, recall  # noqa: F401  (registration side effects)
from .base import TEMPLATES, Question, Template

__all__ = ["TEMPLATES", "Question", "Template"]
