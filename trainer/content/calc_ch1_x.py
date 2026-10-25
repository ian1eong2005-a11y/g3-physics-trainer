"""Chapter 1 Measurement: extra L2 calculation templates."""
from .. import figs
from .base import calc_q, fmt, md_table, nice, template


@template("c1_stopwatch_minutes", chapter=1, level=2, lo="1e")
def stopwatch_minutes(rng):
    m = nice(rng, 1, 2)
    s = nice(rng, 5.4, 12.8, 24.6, 38.2, 47.5)
    total = m * 60 + s
    return calc_q(rng, "Fig. 1 shows the display of a stopwatch after timing a race. What is the time in seconds?", total, [
        (m * 100 + s, "The display shows minutes:seconds. One minute is 60 s, not 100 s."),
        (m + s / 60, "That converts the time into minutes; the question asks for seconds."),
        (s, "You left out the whole minutes."),
    ], "s", "time in s = minutes × 60 + seconds",
        [f"{m} min = {m * 60} s", f"time = {m * 60} + {fmt(s)}", f"= **{fmt(total, sf=4)} s**"],
        ["The display is in minutes : seconds.", "Convert the minutes to seconds first.", f"{m} × 60 + {fmt(s)}."],
        figure=figs.stopwatch(f"{m}:{s:05.2f}"), sf=4)


@template("c1_mm_to_um", chapter=1, level=2, lo="1c")
def mm_to_um(rng):
    v = nice(rng, 0.45, 0.08, 0.25, 0.012, 0.6, 0.035)
    ans = v * 1000
    table = md_table(["object", "thickness / mm"], [["human hair" if v < 0.1 else "sheet of card", fmt(v)]])
    return calc_q(rng, f"The table gives the thickness of an object.\n\n{table}\n\nWhat is this thickness in **micrometres (μm)**?", ans, [
        (v / 1000, "1 mm = 1000 μm, so multiply by 1000."),
        (v * 1e6, "1 mm = 10³ μm (1 m = 10⁶ μm, but 1 mm = 10³ μm)."),
        (v * 100, "1 mm = 1000 μm, not 100 μm."),
    ], "μm", "1 mm = 10⁻³ m and 1 μm = 10⁻⁶ m, so 1 mm = 1000 μm",
        [f"{fmt(v)} mm × 1000", f"= **{fmt(ans)} μm**"],
        ["Write both prefixes as powers of ten.", "milli = 10⁻³, micro = 10⁻⁶.", "So 1 mm = 1000 μm."])


@template("c1_rule_length", chapter=1, level=2, lo="1e")
def rule_length(rng):
    a = nice(rng, 1.0, 1.5, 2.3, 3.0, 4.2)
    L = nice(rng, 5.6, 6.8, 7.4, 8.5, 9.2)
    b = round(a + L, 1)
    table = md_table(["", "rule reading / cm"], [["left end of pencil", fmt(a)], ["right end of pencil", fmt(b)]])
    return calc_q(rng, f"A pencil lies along a rule, but its left end is not at the zero mark. The table shows the readings at its two ends.\n\n{table}\n\nWhat is the length of the pencil?", L, [
        (b, "That is the reading at the right end. Subtract the reading at the left end."),
        (a + b, "You added the readings. Length = right reading − left reading."),
        (L * 10, "That is the length in mm; the readings are in cm."),
    ], "cm", "length = reading at one end − reading at the other end",
        [f"length = {fmt(b)} − {fmt(a)}", f"= **{fmt(L)} cm**"],
        ["The pencil does not start at 0.", "Subtract the starting reading from the end reading.", f"{fmt(b)} − {fmt(a)}."])


@template("c1_mean_period_table", chapter=1, level=2, lo="1e")
def mean_period_table(rng):
    n = 20
    T = nice(rng, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0)
    base = n * T
    t1, t2, t3 = round(base + 0.2, 1), round(base - 0.1, 1), round(base - 0.1, 1)
    mean = (t1 + t2 + t3) / 3
    table = md_table(["attempt", "time for 20 oscillations / s"], [[1, fmt(t1, sf=4)], [2, fmt(t2, sf=4)], [3, fmt(t3, sf=4)]])
    return calc_q(rng, f"A student times 20 oscillations of a pendulum three times.\n\n{table}\n\nWhat is the period of the pendulum?", mean / n, [
        (mean, "That is the mean time for 20 oscillations. Divide by 20."),
        (t1 / n, "Use the MEAN of all three readings, not just the first."),
        ((t1 + t2 + t3) / n, "You added the readings but did not divide by 3 first."),
    ], "s", "period = mean time for 20 oscillations ÷ 20",
        [f"mean = ({fmt(t1, sf=4)} + {fmt(t2, sf=4)} + {fmt(t3, sf=4)}) ÷ 3 = {fmt(mean, sf=4)} s", f"period = {fmt(mean, sf=4)} ÷ 20", f"= **{fmt(mean / n)} s**"],
        ["First find the mean time for 20 oscillations.", "The period is the time for ONE oscillation.", "Divide the mean by 20."])


@template("c1_cylinder_250", chapter=1, level=2, lo="1e")
def cylinder_250(rng):
    level = nice(rng, 120, 140, 160, 180, 210, 230)
    return calc_q(rng, "Fig. 1 shows a 250 cm³ measuring cylinder containing water. What is the volume of the water?", level, [
        (level + 10, "Count the small divisions again: each one is 10 cm³."),
        (level // 50 * 50 + (level % 50) // 10, "Each small division is 10 cm³, not 1 cm³."),
        (level - 10, "Count the small divisions again: each one is 10 cm³."),
    ], "cm³", "volume = last numbered mark + number of small divisions × 10 cm³",
        ["numbered marks every 50 cm³, 5 small divisions between them, so 1 division = 10 cm³", f"volume = **{level} cm³**"],
        ["Work out the value of one small division.", "There are 5 divisions between marks 50 cm³ apart.", "Count up from the last numbered mark below the meniscus."],
        figure=figs.measuring_cylinder(level, max_ml=250, step_ml=50, minor_ml=10), sf=None)


@template("c1_time_convert", chapter=1, level=2, lo="1a")
def time_convert(rng):
    v, unit, k = rng.choice([(2.5, "min", 60), (1.5, "h", 3600), (0.25, "h", 3600), (4.5, "min", 60), (0.75, "min", 60), (2.2, "h", 3600)])
    ans = v * k
    table = md_table(["activity", "time taken"], [["experiment", f"{fmt(v)} {unit}"]])
    return calc_q(rng, f"The table shows how long an experiment took.\n\n{table}\n\nWhat is this time in **seconds**?", ans, [
        (v * 100, "There are 60 s in a minute and 3600 s in an hour, not 100."),
        (v / k, "You divided. A time in seconds is a LARGER number than the same time in minutes or hours."),
        (v * 60 if k == 3600 else v * 3600, "Check the conversion factor: 1 min = 60 s; 1 h = 3600 s."),
    ], "s", "1 min = 60 s; 1 h = 60 × 60 = 3600 s",
        [f"{fmt(v)} {unit} × {k}", f"= **{fmt(ans)} s**"],
        ["How many seconds are in one minute? In one hour?", f"1 {unit} = {k} s.", f"Multiply {fmt(v)} by {k}."])
