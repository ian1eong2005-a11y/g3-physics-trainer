"""Constants for the G3 Science (Physics) adaptive trainer. Change class lists and rules here only."""

APP_TITLE = "G3 Physics Trainer"
SCHOOL = "Queenstown Secondary School"

# Login dropdown, grouped by level. Add Sec 4 classes here when known.
CLASSES = {
    "Sec 3": ["3SG2", "3SG3", "3SG4", "3SG8"],
    "Sec 4": ["4SG1", "4SG2", "4SG3", "4SG4"],
    "Sec 5": ["5AS"],
}
CLASS_LIST = [c for group in CLASSES.values() for c in group]

CHAPTERS = {
    1: "Measurement",
    2: "Kinematics",
    3: "Force and Pressure",
    4: "Dynamics",
    5: "Turning Effects of Forces",
    6: "Energy",
    7: "Kinetic Particle Model of Matter",
    8: "Thermal Processes",
    9: "General Wave Properties",
    10: "Electromagnetic Spectrum",
    11: "Light",
    12: "Electric Charge and Current",
    13: "D.C. Circuits",
    14: "Practical Electricity",
    15: "Magnetism and Electromagnetism",
    16: "Radioactivity",
}

CATEGORIES = {
    "calc": "Calculation",
    "explain": "Explanation",
    "written": "Written answer",
    "olevel": "O level 2026 MCQ practice",
}

WRITTEN_LEVEL_NAMES = {
    1: "L1 - state or define in a phrase",
    2: "L2 - state two facts or describe simply",
    3: "L3 - explain with a reason",
    4: "L4 - explain with a chain of reasoning",
    5: "L5 - apply or evaluate in a new situation",
}

LEVEL_NAMES = {
    1: "L1 - one formula, direct substitution",
    2: "L2 - one formula with a conversion, reading or rearrangement",
    3: "L3 - two steps, usually with a figure",
    4: "L4 - graphs and linked formulas",
    5: "L5 - multi-step with a trap",
}
EXPLAIN_LEVEL_NAMES = {
    1: "L1 - recall and definitions",
    2: "L2 - identify and classify",
    3: "L3 - apply a concept",
    4: "L4 - explain with reasoning",
    5: "L5 - evaluate",
}

# 2026 O-Level 5086 Paper 2: learning outcomes it did NOT test (from "Output documents/2026 O-Level 5086 P2 Table of
# Specifications.xlsx", sheet "LOs not tested"). 14c counts as tested (kW h unit in Q1).
P2_2026_NOT_TESTED = {
    "1a", "1c", "1d", "1f", "2a", "2d", "2e", "2f", "2g", "2h", "2i", "3b", "3c", "3d", "3e", "3f", "3g", "3h", "4d", "5a", "5c",
    "6d", "6e", "7a", "7d", "8a", "9b", "9g", "9h", "9i", "11a", "11b", "11f", "11g", "11h", "12a", "12b", "12e", "12f", "12h",
    "13e", "14a", "14d", "14g", "14h", "14i", "15a", "15c", "15e", "15g", "15h", "15i", "16f", "16h",
}
P2_2026_Q10_ONLY = {"6c", "7b", "7c", "7e", "8b", "8c", "8d", "8e"}             # tested only in the either/or Q10
P2_2026_Q11_ONLY = {"9e", "9f", "10a", "10b", "10c", "10d", "11c", "11d", "11e"}  # tested only in the either/or Q11


def p2_2026_note(lo: str):
    """Note shown on an O-level practice question, worked out from its learning outcome; None if Paper 2 tested it."""
    if lo in P2_2026_NOT_TESTED:
        return "NOT in P2 2026"
    if lo in P2_2026_Q10_ONLY:
        return "NOT in P2 2026 Section A (only in either/or Q10)"
    if lo in P2_2026_Q11_ONLY:
        return "NOT in P2 2026 Section A (only in either/or Q11)"
    return None


OLEVEL_LEVEL_NAMES = {
    1: "L1 - recall a definition or fact (SEAB style)",
    2: "L2 - one step: a formula or a rule",
    3: "L3 - read a diagram or graph, or two steps",
    4: "L4 - several steps or unfamiliar context",
    5: "L5 - hardest past-year MCQs",
}

# Adaptive rules (confirmed by the teacher, 24 Oct 2026)
UP_STREAK = 5          # correct in a row at a level -> level + 1
DOWN_STREAK = 3        # wrong in a row at a level -> level - 1
MIN_LEVEL, MAX_LEVEL = 1, 5
START_LEVEL = 1
HISTORY_LEN = 1000     # served template ids remembered per category; a question comes back only after its whole pool has been seen

ONLINE_SECONDS = 120   # "online" on the dashboard if active within this many seconds
DASHBOARD_REFRESH_S = 5

DEFAULT_TEACHER_PASSWORD = "physics"   # used only when no TEACHER_PASSWORD secret / env var is set

G = 10.0               # N/kg, as used in school papers
