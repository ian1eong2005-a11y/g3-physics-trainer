"""Chapter 1 Measurement: more calculation templates (prefixes, cylinder readings, zero errors, stacks, resultants, unit volume)."""
import math

from .. import figs
from .base import fmt, md_table, nice, numeric_options, template

PREFIXES = [(2.5, "km", "m", 1000), (450, "mm", "m", 0.001), (35, "cm", "m", 0.01), (750, "mg", "g", 0.001),
            (1.2, "kg", "g", 1000), (250, "ms", "s", 0.001), (3.6, "km", "m", 1000), (820, "mm", "m", 0.001),
            (64, "cm", "m", 0.01), (0.75, "kg", "g", 1000), (125, "ms", "s", 0.001), (5.4, "kN", "N", 1000)]


# ---------------------------------------------------------------- L1
@template("c1_prefix_convert", chapter=1, level=1, lo="1c")
def prefix_convert(rng):
    v, pu, base, k = rng.choice(PREFIXES)
    ans = v * k
    opts, key, mis = numeric_options(rng, ans, [
        (v / k, f"You divided by the wrong factor. 1 {pu} = {fmt(k, sf=None)} {base}, so multiply."),
        (ans * 10, "Check the size of the prefix: you are out by a factor of 10."),
        (ans / 10, "Check the size of the prefix: you are out by a factor of 10."),
    ], unit=base, sf=None)
    table = md_table(["quantity", "measured value"], [["reading", f"{fmt(v, sf=None)} {pu}"]])
    return dict(
        stem=f"The table shows a measurement.\n\n{table}\n\nWhat is this value in **{base}**?",
        options=opts, key=key, misconceptions=mis,
        formula=f"1 {pu} = {fmt(k, sf=None)} {base}",
        working=[f"1 {pu} = {fmt(k, sf=None)} {base}", f"{fmt(v, sf=None)} {pu} = {fmt(v, sf=None)} × {fmt(k, sf=None)} {base}", f"= **{fmt(ans, sf=None)} {base}**"],
        hints=[f"What does the prefix in '{pu}' stand for?",
               f"1 {pu} = {fmt(k, sf=None)} {base}.",
               f"Multiply {fmt(v, sf=None)} by {fmt(k, sf=None)}."],
    )


@template("c1_cylinder_reading", chapter=1, level=1, lo="1e")
def cylinder_reading(rng):
    level = nice(rng, 42, 46, 54, 58, 62, 66, 74, 78, 84, 88)
    opts, key, mis = numeric_options(rng, level, [
        (level + 2, "You counted one small division too many. Each small division is 2 cm³."),
        (level - 2, "You counted one small division too few. Each small division is 2 cm³."),
        (level // 10 * 10 + (level % 10) / 2, "You took each small division as 1 cm³. There are 5 small divisions per 10 cm³, so each is 2 cm³."),
    ], unit="cm³", sf=None)
    return dict(
        stem="Fig. 1 shows water in a measuring cylinder. The eye is level with the bottom of the meniscus. What is the volume of the water?",
        figure=figs.measuring_cylinder(level),
        options=opts, key=key, misconceptions=mis,
        formula="volume = last numbered mark + (number of small divisions × value of one division)",
        working=["each 10 cm³ is split into 5 small divisions, so one division = 2 cm³",
                 f"the meniscus is at {level // 10 * 10} + {(level % 10) // 2} × 2", f"= **{level} cm³**"],
        hints=["Find the value of one small division first.",
               "There are 5 small divisions between numbered marks 10 cm³ apart.",
               "Count the divisions above the last numbered mark below the meniscus."],
    )


# ---------------------------------------------------------------- L3
@template("c1_volume_by_displacement", chapter=1, level=3, lo="1e")
def volume_by_displacement(rng):
    before = nice(rng, 30, 40, 44, 50, 52, 60)
    stone = nice(rng, 12, 14, 16, 18, 22, 24, 26)
    after = before + stone
    opts, key, mis = numeric_options(rng, stone, [
        (after, "That is the reading after the stone is added, not the stone's volume."),
        (before + after, "You added the readings. The stone's volume is the RISE in level."),
        (stone + 2, "Read both levels carefully: each small division is 2 cm³."),
    ], unit="cm³", sf=None)
    return dict(
        stem="Fig. 1 shows a measuring cylinder before and after a small stone is lowered into it. What is the volume of the stone?",
        figure=figs.two_cylinders(before, after),
        options=opts, key=key, misconceptions=mis,
        formula="volume of stone = reading after − reading before",
        working=[f"before = {before} cm³, after = {after} cm³", f"volume = {after} − {before}", f"= **{stone} cm³**"],
        hints=["The stone pushes water up by its own volume.",
               "Read both cylinders (one small division = 2 cm³).",
               "Subtract the first reading from the second."],
    )


@template("c1_micrometer_zero_error", chapter=1, level=3, lo="1e")
def micrometer_zero_error(rng):
    main = nice(rng, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0)
    div = rng.randint(8, 45)
    reading = round(main + div / 100, 2)
    ze = nice(rng, 0.02, 0.03, 0.04, -0.01, -0.02, -0.03)
    corr = round(reading - ze, 2)
    sign = f"+{ze:.2f}" if ze > 0 else f"−{abs(ze):.2f}"
    opts, key, mis = numeric_options(rng, corr, [
        (round(reading + ze, 2), "You added the zero error. Corrected reading = reading − zero error (taking its sign into account)."),
        (reading, "You ignored the zero error."),
        (round(corr - 0.01, 2), "You misread the thimble by one division."),
    ], unit="mm", dp=2)
    table = md_table(["zero error of the micrometer"], [[f"{sign} mm"]])
    return dict(
        stem=f"Fig. 1 shows a micrometer screw gauge measuring the diameter of a rod. The table gives the zero error of the gauge.\n\n{table}\n\nWhat is the corrected diameter of the rod?",
        figure=figs.micrometer(reading),
        options=opts, key=key, misconceptions=mis,
        formula="corrected reading = observed reading − zero error",
        working=[f"observed reading = {main:.2f} + {div} × 0.01 = {reading:.2f} mm", f"corrected = {reading:.2f} − ({sign})", f"= **{corr:.2f} mm**"],
        hints=["Read the micrometer first: main scale + thimble.",
               "A positive zero error means every reading is too large; a negative one, too small.",
               f"Corrected = {reading:.2f} − ({sign})."],
    )


# ---------------------------------------------------------------- L4
@template("c1_vernier_zero_error", chapter=1, level=4, lo="1e")
def vernier_zero_error(rng):
    main = rng.randint(18, 44)
    tenth = rng.randint(1, 9)
    reading_mm = main + tenth / 10
    ze_cm = nice(rng, 0.02, 0.03, 0.04, -0.02, -0.03)
    corr = round(reading_mm / 10 - ze_cm, 2)
    sign = f"+{ze_cm:.2f}" if ze_cm > 0 else f"−{abs(ze_cm):.2f}"
    opts, key, mis = numeric_options(rng, corr, [
        (round(reading_mm / 10 + ze_cm, 2), "You added the zero error. Corrected reading = reading − zero error."),
        (round(reading_mm / 10, 2), "You ignored the zero error."),
        (round(reading_mm - ze_cm, 2), "Your reading is in mm but the zero error and the answer are in cm. Convert first."),
    ], unit="cm", dp=2)
    table = md_table(["zero error of the calipers"], [[f"{sign} cm"]])
    return dict(
        stem=f"Fig. 1 shows the scales of a pair of vernier calipers measuring a block. The table gives the zero error of the calipers.\n\n{table}\n\nWhat is the corrected length of the block, in cm?",
        figure=figs.vernier(reading_mm),
        options=opts, key=key, misconceptions=mis,
        formula="corrected reading = observed reading − zero error (same units)",
        working=[f"observed reading = {reading_mm:.1f} mm = {reading_mm / 10:.2f} cm", f"corrected = {reading_mm / 10:.2f} − ({sign})", f"= **{corr:.2f} cm**"],
        hints=["Read the main scale just before the vernier zero, then find the vernier line that lines up.",
               "Convert the reading to cm before using the zero error.",
               f"Corrected = {reading_mm / 10:.2f} − ({sign})."],
    )


@template("c1_stack_thickness", chapter=1, level=4, lo="1e")
def stack_thickness(rng):
    n = nice(rng, 50, 40, 25, 20)
    each = nice(rng, 0.08, 0.09, 0.10, 0.11, 0.12, 0.14, 0.16, 0.18)
    reading = round(n * each, 2)
    if reading > 7.5:
        n, reading = 25, round(25 * each, 2)
    opts, key, mis = numeric_options(rng, reading / n, [
        (reading, "That is the thickness of the whole stack, not of one sheet."),
        (reading * n, "You multiplied. One sheet is thinner than the stack, so divide."),
        (reading / n * 10, "Check the division: you are out by a factor of 10."),
    ], unit="mm", sf=2)
    return dict(
        stem=f"Fig. 1 shows a micrometer screw gauge measuring the thickness of a stack of **{n} identical sheets** of card. What is the thickness of one sheet?",
        figure=figs.micrometer(reading),
        options=opts, key=key, misconceptions=mis,
        formula="thickness of one sheet = thickness of stack ÷ number of sheets",
        working=[f"stack = {reading:.2f} mm", f"one sheet = {reading:.2f} ÷ {n}", f"= **{fmt(reading / n, sf=2)} mm**"],
        hints=["Measuring many sheets together and dividing makes the result more precise.",
               "Read the micrometer to get the thickness of the whole stack.",
               f"Divide that reading by {n}."],
    )


@template("c1_resultant_velocity", chapter=1, level=4, lo="1f")
def resultant_velocity(rng):
    a, b, c = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (1.5, 2, 2.5), (0.9, 1.2, 1.5), (2.4, 3.2, 4)])
    opts, key, mis = numeric_options(rng, c, [
        (a + b, "You added the speeds. Vectors at right angles combine by Pythagoras' theorem."),
        (abs(b - a), "You subtracted. The two velocities are at right angles, so use Pythagoras."),
        (a * b, "You multiplied. Use resultant² = a² + b²."),
    ], unit="m/s", sf=3)
    return dict(
        stem=f"Fig. 1 shows a boat that moves at **{fmt(a)} m/s** across a river (northwards) while the current carries it at **{fmt(b)} m/s** eastwards. What is the magnitude of the boat's resultant velocity?",
        figure=figs.force_diagram([(f"{fmt(a)} m/s", "up", 1.6), (f"{fmt(b)} m/s", "right", 2.0)], label_body="boat", ground=False),
        options=opts, key=key, misconceptions=mis,
        formula="for two vectors at right angles: resultant = √(a² + b²)",
        working=[f"resultant² = {fmt(a)}² + {fmt(b)}² = {fmt(a * a)} + {fmt(b * b)} = {fmt(c * c)}", f"resultant = √{fmt(c * c)}", f"= **{fmt(c)} m/s**"],
        hints=["Velocity is a vector: direction matters, so you cannot simply add the speeds.",
               "The two velocities are at right angles. Which theorem gives the third side of a right-angled triangle?",
               f"√({fmt(a)}² + {fmt(b)}²)."],
    )


# ---------------------------------------------------------------- L5
@template("c1_block_volume_m3", chapter=1, level=5, lo="1c")
def block_volume_m3(rng):
    a, b, c = nice(rng, 10, 20, 25, 40, 50), nice(rng, 10, 20, 30), nice(rng, 5, 10, 20)
    v_cm3 = a * b * c
    v_m3 = v_cm3 / 1e6
    opts, key, mis = numeric_options(rng, v_m3, [
        (v_cm3 / 100, "1 m = 100 cm, but 1 m³ = 100 × 100 × 100 = 1 000 000 cm³."),
        (v_cm3 / 1000, "1 m³ = 1 000 000 cm³, not 1000 cm³ (1000 cm³ is one litre)."),
        (v_cm3 / 1e5, "Check the conversion: divide cm³ by 1 000 000 to get m³."),
    ], unit="m³", sf=3)
    return dict(
        stem="Fig. 1 shows a rectangular block with its dimensions. What is the volume of the block in **m³**?",
        figure=figs.labelled_block(a, b, c, "cm"),
        options=opts, key=key, misconceptions=mis,
        formula="volume = length × breadth × height; 1 m³ = 10⁶ cm³",
        working=[f"volume = {a} × {b} × {c} = {v_cm3} cm³", f"= {v_cm3} ÷ 1 000 000 m³", f"= **{fmt(v_m3)} m³**"],
        hints=["Work out the volume in cm³ first.",
               "1 m = 100 cm, so 1 m³ = 100 × 100 × 100 cm³.",
               f"Divide {v_cm3} by 1 000 000."],
    )


@template("c1_volume_one_marble", chapter=1, level=5, lo="1e")
def volume_one_marble(rng):
    n = nice(rng, 5, 8, 10, 12, 20)
    each = nice(rng, 1.2, 1.5, 2.0, 2.4, 2.5, 3.0)
    before = nice(rng, 30, 40, 50)
    rise = round(n * each, 1)
    if rise % 2:
        each, rise = 2.0, n * 2.0
    before = min(before, (96 - int(rise)) // 2 * 2)
    after = before + int(rise)
    opts, key, mis = numeric_options(rng, (after - before) / n, [
        (after - before, "That is the volume of all the marbles together."),
        (after / n, "You divided the final reading, not the rise in level."),
        ((after - before) * n, "You multiplied. One marble has a smaller volume than all of them."),
    ], unit="cm³", sf=3)
    return dict(
        stem=f"Fig. 1 shows a measuring cylinder before and after **{n} identical marbles** are added. What is the volume of one marble?",
        figure=figs.two_cylinders(before, after),
        options=opts, key=key, misconceptions=mis,
        formula="volume of one marble = (reading after − reading before) ÷ number of marbles",
        working=[f"rise = {after} − {before} = {after - before} cm³", f"one marble = {after - before} ÷ {n}", f"= **{fmt((after - before) / n)} cm³**"],
        hints=["The rise in water level equals the total volume of the marbles.",
               "Read both cylinders, then subtract.",
               f"Divide the total by {n}."],
    )
