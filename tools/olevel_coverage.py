"""Write OLEVEL_MCQ_COVERAGE.md: every 5086 learning outcome -> its O-level practice questions and P2 2026 note, and every SEAB
Ten-Year-Series MCQ -> the item that adapts it (or why it is out of the 5086 syllabus). Run: python tools/olevel_coverage.py"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

from test_olevel import ALL_LOS, OLEVEL, OUT_OF_SCOPE, TYS  # noqa: E402

from trainer.config import CHAPTERS, p2_2026_note  # noqa: E402

src_of, cites = {}, defaultdict(list)
for t in OLEVEL:
    text = " ".join(t.make(0).working)
    m = re.search(r"_Adapted from (.+?)\._", text)
    src_of[t.id] = m.group(1) if m else "?"
    for mm in re.finditer(r"SEAB (?:O-Level (\d{4})|5086 specimen paper 2024|specimen 2024) MCQ (\d+)((?: and (?:\d{4} )?MCQ \d+)*)", text):
        y = mm.group(1) or "specimen"
        cites[(y, int(mm.group(2)))].append(t.id)
        for m2 in re.finditer(r"and (?:(\d{4}) )?MCQ (\d+)", mm.group(3)):
            cites[(m2.group(1) or y, int(m2.group(2)))].append(t.id)

by_lo = defaultdict(list)
for t in OLEVEL:
    by_lo[t.lo].append(t)
n_tys = sum(1 for t in OLEVEL if src_of[t.id].startswith("SEAB"))
n_school = len(OLEVEL) - n_tys
out = ["# O level 2026 MCQ practice: coverage", "",
       f"{len(OLEVEL)} questions: {n_tys} adapted from SEAB papers (Ten-Year Series 2014-2021 and the 5086 specimen paper), "
       f"{n_school} adapted from schools' 2024 prelim papers for outcomes with no SEAB MCQ. Every one of the {len(ALL_LOS)} learning outcomes has at least one question.",
       "", "The note comes from the 'LOs not tested' sheet of `2026 O-Level 5086 P2 Table of Specifications.xlsx`.", "",
       "## By learning outcome", "", "| LO | note | questions | sources |", "|---|---|---|---|"]
for lo in ALL_LOS:
    ts = by_lo[lo]
    out.append(f"| {lo} | {p2_2026_note(lo) or 'tested in P2 2026'} | {len(ts)} | " + "; ".join(sorted({src_of[t.id] for t in ts})) + " |")
out += ["", "## Every SEAB Ten-Year-Series MCQ", "", "| paper | MCQ | trainer item(s) |", "|---|---|---|"]
for y, qs in TYS.items():
    for q in qs:
        if (y, q) in OUT_OF_SCOPE:
            cell = f"left out: {OUT_OF_SCOPE[(y, q)]} is not in the 5086 syllabus"
        else:
            cell = ", ".join(sorted(set(cites.get((y, q), [])))) or "MISSING"
        out.append(f"| {'5086 specimen 2024' if y == 'specimen' else 'O-Level ' + y} | {q} | {cell} |")
(ROOT / "OLEVEL_MCQ_COVERAGE.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("written", len(OLEVEL), "items;", sum(1 for l in out if "MISSING" in l), "missing")
