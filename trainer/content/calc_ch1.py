"""Chapter 1 Measurement: calculation templates (period, instrument readings, displacement, unit conversion)."""
from .. import figs, sketches
from .base import fmt, nice, numeric_options, template


# ---------------------------------------------------------------- L1
@template("c1_period_from_oscillations", chapter=1, level=1, lo="1e")
def period_from_oscillations(rng):
    n = nice(rng, 10, 20, 25, 40, 50)
    T = nice(rng, 0.8, 1.2, 1.5, 1.6, 2.0, 2.4, 2.5)
    total = round(n * T, 2)
    opts, key, mis = numeric_options(rng, T, [
        (n / total, "You divided the number of oscillations by the time. Period = time ÷ number of oscillations."),
        (total * n, "You multiplied. The period is the time for ONE oscillation, so it must be smaller than the total time."),
        (total, "That is the total time for all the oscillations, not the time for one."),
    ], unit="s")
    return dict(
        stem=f"A student times the pendulum shown in Fig. 1 and finds that it completes **{n} oscillations in {fmt(total)} s**. What is the period of the pendulum?",
        figure=sketches.pendulum_sketch(f"{n} complete oscillations in {fmt(total)} s"),
        options=opts, key=key, misconceptions=mis,
        formula="period = total time ÷ number of oscillations",
        working=[f"period = total time ÷ number of oscillations", f"= {fmt(total)} s ÷ {n}", f"= **{fmt(T)} s**"],
        hints=[
            "The period is the time for ONE complete oscillation. Which formula links the total time, the number of oscillations and the period?",
            f"The {fmt(total)} s is the time for {n} oscillations. You want the time for just one of them, so the answer must be smaller than {fmt(total)} s.",
            f"T = {fmt(total)} ÷ {n}. Work out the division and keep the unit s.",
        ],
    )


# ---------------------------------------------------------------- L2
@template("c1_micrometer_reading", chapter=1, level=2, lo="1e")
def micrometer_reading(rng):
    main = nice(rng, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5)
    div = rng.randint(3, 47)
    reading = round(main + div / 100, 2)
    half = abs(main - int(main)) > 1e-9
    wrong_half = reading - 0.5 if half else reading + 0.5
    opts, key, mis = numeric_options(rng, reading, [
        (wrong_half, "Check the half-millimetre marks below the datum line: " + ("one is visible, so add 0.5 mm to the whole millimetres." if half else "none is visible after the last whole millimetre, so do not add 0.5 mm.")),
        (round(main + div / 10, 2), "Each thimble division is 0.01 mm, not 0.1 mm. 50 divisions make one turn of 0.5 mm."),
        (round(reading + (0.01 if div < 47 else -0.01), 2), "You misread the thimble by one division. Find the division that lines up exactly with the datum line."),
    ], unit="mm", dp=2)
    return dict(
        stem="Fig. 1 shows the scale of a micrometer screw gauge being used to measure the diameter of a wire. There is no zero error. What is the diameter of the wire?",
        figure=figs.micrometer(reading),
        options=opts, key=key, misconceptions=mis,
        formula="reading = main scale (to the nearest 0.5 mm) + thimble division × 0.01 mm",
        working=[f"main scale reading = {fmt(main, dp=2)} mm", f"thimble reading = {div} × 0.01 mm = {fmt(div / 100, dp=2)} mm",
                 f"diameter = {fmt(main, dp=2)} + {fmt(div / 100, dp=2)} = **{fmt(reading, dp=2)} mm**"],
        hints=[
            "A micrometer reading has two parts. Which two scales do you add together, and what is the value of one thimble division?",
            f"Main scale: read the last mark visible before the thimble edge, remembering the half-mm marks below the line. Thimble: find the division level with the datum line (it is {div}).",
            f"Reading = {fmt(main, dp=2)} mm + {div} × 0.01 mm. Add them.",
        ],
    )


@template("c1_vernier_reading", chapter=1, level=2, lo="1e")
def vernier_reading(rng):
    main_mm = rng.randint(12, 88)
    tenth = rng.randint(1, 9)
    reading_mm = main_mm + tenth / 10
    reading_cm = reading_mm / 10
    opts, key, mis = numeric_options(rng, reading_cm, [
        (main_mm / 10 + tenth / 10, "Each vernier division is worth 0.01 cm (0.1 mm), not 0.1 cm."),
        ((main_mm + 1) / 10 + tenth / 100, "Read the main-scale mark just to the LEFT of the vernier zero, not the one to the right."),
        (main_mm / 10, "You ignored the vernier scale. Find the vernier division that lines up with a main-scale mark."),
    ], unit="cm", dp=2)
    return dict(
        stem="Fig. 1 shows part of a pair of vernier calipers being used to measure the length of a bolt. What is the reading, in cm?",
        figure=figs.vernier(reading_mm),
        options=opts, key=key, misconceptions=mis,
        formula="reading = main scale reading (left of the vernier zero) + coinciding vernier division × 0.01 cm",
        working=[f"main scale reading (mark just before the vernier zero) = {fmt(main_mm / 10, dp=1)} cm",
                 f"vernier division that coincides = {tenth} → {tenth} × 0.01 cm = {fmt(tenth / 100, dp=2)} cm",
                 f"reading = {fmt(main_mm / 10, dp=1)} + {fmt(tenth / 100, dp=2)} = **{fmt(reading_cm, dp=2)} cm**"],
        hints=[
            "Two steps: the main-scale reading just before the vernier zero, then the vernier division that lines up exactly with a main-scale mark. What is one vernier division worth?",
            f"The vernier zero sits just past the {main_mm} mm mark, so the main-scale part is {fmt(main_mm / 10, dp=1)} cm. Now look for the coinciding division (it is {tenth}).",
            f"Reading = {fmt(main_mm / 10, dp=1)} cm + {tenth} × 0.01 cm.",
        ],
    )


@template("c1_stopwatch_period", chapter=1, level=2, lo="1e")
def stopwatch_period(rng):
    n = nice(rng, 10, 20, 25, 30, 40, 50)
    T = nice(rng, 1.2, 1.5, 1.6, 1.8, 2.0, 2.4, 2.5, 3.0)
    total = round(n * T, 2)
    minutes, secs = int(total // 60), total - 60 * int(total // 60)
    display = f"{minutes}:{secs:05.2f}"
    misread = minutes * 100 + secs if minutes else total * 10
    opts, key, mis = numeric_options(rng, T, [
        (n / total, "You divided the number of oscillations by the time: it should be time ÷ number."),
        (misread / n, "The display shows minutes : seconds. Convert the minutes to seconds first (1 min = 60 s)." if minutes else "Check how you read the display: the digits after the colon are seconds."),
        (total / (n + 1), "You divided by one oscillation too many. Count the oscillations given in the question."),
    ], unit="s", dp=2)
    return dict(
        stem=f"A student starts a stopwatch as a pendulum bob passes its rest position and stops it after **{n} complete oscillations**. Fig. 1 shows the stopwatch. What is the period of the pendulum?",
        figure=figs.stopwatch(display),
        options=opts, key=key, misconceptions=mis,
        formula="period = total time ÷ number of oscillations",
        working=[f"stopwatch reading = {display} = {fmt(total)} s", f"period = {fmt(total)} ÷ {n} = **{fmt(T, dp=2)} s**"],
        hints=[
            "First read the stopwatch in seconds, then ask: how many oscillations did that time cover?",
            f"The display {display} means {minutes} min {fmt(secs)} s = {fmt(total)} s in total. That is for {n} oscillations.",
            f"Period = {fmt(total)} ÷ {n}.",
        ],
    )


# ---------------------------------------------------------------- L3
@template("c1_displacement_two_legs", chapter=1, level=3, lo="1f")
def displacement_two_legs(rng):
    a, b, c = rng.choice([(3, 4, 5), (6, 8, 10), (9, 12, 15), (5, 12, 13), (8, 15, 17), (30, 40, 50), (60, 80, 100), (50, 120, 130)])
    opts, key, mis = numeric_options(rng, c, [
        (a + b, "That is the total DISTANCE walked. Displacement is the straight-line distance from start to finish."),
        (abs(a - b), "You subtracted the two legs. They are at right angles, so use Pythagoras' theorem."),
        (max(a, b), "That is just the longer leg. The straight line from start to finish is longer than either leg."),
    ], unit="m")
    return dict(
        stem=f"A student walks **{a} m due north** and then **{b} m due east**, as shown in Fig. 1. What is the magnitude of the student's displacement from the starting point?",
        figure=figs.path_figure(a, b),
        options=opts, key=key, misconceptions=mis,
        formula="displacement² = north² + east² (Pythagoras, legs at right angles)",
        working=[f"displacement = √({a}² + {b}²)", f"= √({a * a} + {b * b}) = √{a * a + b * b}", f"= **{c} m**"],
        hints=[
            "Displacement is a vector: the straight-line distance from start to finish, with a direction. What shape do the two legs and the straight line make?",
            f"The two legs are at right angles, so the straight line is the hypotenuse of a right-angled triangle with sides {a} m and {b} m.",
            f"displacement = √({a}² + {b}²) = √{a * a + b * b}.",
        ],
    )


# ---------------------------------------------------------------- L5
@template("c1_density_mixed_units", chapter=1, level=5, lo="1c")
def density_mixed_units(rng):
    rho = nice(rng, 0.8, 1.2, 2.5, 2.7, 4.0, 7.9, 8.9)        # g/cm³
    V = nice(rng, 200, 250, 400, 500, 800, 1000)              # cm³
    mass_kg = round(rho * V / 1000, 4)
    ans = rho * 1000                                          # kg/m³
    opts, key, mis = numeric_options(rng, ans, [
        (rho, "That is the density in g/cm³. The question asks for kg/m³, and 1 g/cm³ = 1000 kg/m³."),
        (rho / 10, "You used 1 m³ = 100 cm³. In fact 1 m³ = 100 × 100 × 100 = 1 000 000 cm³."),
        (rho * 1e6, "You left the mass in grams. 1 kg = 1000 g."),
    ], unit="kg/m³")
    return dict(
        stem=f"Fig. 1 shows a metal block of mass **{fmt(mass_kg, sf=4)} kg** and volume **{V} cm³**. What is the density of the metal in **kg/m³**?",
        figure=sketches.lump_sketch([f"mass = {fmt(mass_kg, sf=4)} kg", f"volume = {V} cm³"]),
        options=opts, key=key, misconceptions=mis,
        formula="density = mass ÷ volume, with mass in kg and volume in m³ (1 m³ = 1 000 000 cm³)",
        working=[f"volume = {V} cm³ = {V} ÷ 1 000 000 m³ = {fmt(V / 1e6, sf=4)} m³",
                 f"density = {fmt(mass_kg, sf=4)} ÷ {fmt(V / 1e6, sf=4)}", f"= **{fmt(ans)} kg/m³**"],
        hints=[
            "Density = mass ÷ volume, but the answer must be in kg/m³. Which of the two given quantities is NOT in an SI unit?",
            f"The volume is in cm³. How many cm³ make 1 m³? (Think 100 cm × 100 cm × 100 cm.)",
            f"density = {fmt(mass_kg, sf=4)} kg ÷ ({V} ÷ 1 000 000) m³. Alternatively: {fmt(rho * V)} g ÷ {V} cm³ = {fmt(rho)} g/cm³, then × 1000.",
        ],
    )
