"""O level 2026 MCQ practice, Ch 9-15: the remaining SEAB Ten-Year-Series MCQs in the 5086 syllabus (added 31 Oct 2026).
Same context, skill and answer logic as the SEAB question; figures redrawn; numbers changed slightly and varied on every serve."""
from .. import figs, sketches, sketches2 as sk, sketches4 as k4
from .base import calc_q, explain_mcqs, fmt, md_table, nice, template, text_options

CAT = "olevel"
SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def src(text):
    return f"_Adapted from {text}._"


def sci(x, unit=""):
    """2.0 × 10⁵ Hz style."""
    e = 0
    while abs(x) >= 10:
        x /= 10
        e += 1
    while abs(x) < 1:
        x *= 10
        e -= 1
    return f"{x:.1f} × 10{str(e).translate(SUP)} {unit}".strip()


# ================================================================== Ch 9 Waves
explain_mcqs([
    dict(id="o26t_wavefront", chapter=9, level=1, lo="9a", source="SEAB O-Level 2014 MCQ 9 and 2019 MCQ 10",
         stem="What is meant by the term **wavefront**?",
         correct="a line joining points along the crest (peak) of a wave",
         wrongs={"the distance between two neighbouring crests of a wave": "That is the wavelength.",
                 "the distance between a trough and a crest of a wave": "That is twice the amplitude, and it is a distance, not a line.",
                 "a line joining a trough to the next crest of a wave": "A wavefront joins points that are in step, e.g. all on the same crest."},
         hints=["In a ripple tank you see wavefronts as bright lines.", "Each line joins points that are all at the same stage of the wave.",
                "Which option describes a line along one crest?"]),
    dict(id="o26t_metres_terms", chapter=9, level=1, lo="9c", source="SEAB O-Level 2015 MCQ 9",
         stem="Which two of these wave quantities are measured in metres: amplitude, frequency, speed, wavelength?",
         correct="amplitude and wavelength",
         wrongs={"amplitude and frequency": "Frequency is measured in hertz (Hz).",
                 "frequency and speed": "Frequency is in Hz and speed is in m/s.",
                 "speed and wavelength": "Speed is in m/s, not m."},
         hints=["Which quantities are distances?", "Frequency is per second; speed is distance per second.", "Pick the two lengths."]),
    dict(id="o26t_period_def", chapter=9, level=1, lo="9c", source="SEAB O-Level 2017 MCQ 11",
         stem="A wave travels along a spring. Which statement about the **period** of the wave is correct?",
         correct="It is the time taken for one complete oscillation.",
         wrongs={"It is measured in hertz.": "Hertz is the unit of frequency. Period is a time, in seconds.",
                 "It is the number of oscillations each second.": "That is the frequency.",
                 "It is the speed of the wave divided by its wavelength.": "v ÷ λ gives the frequency; the period is 1 ÷ f."},
         hints=["Period is a time.", "Frequency and period are reciprocals: T = 1 ÷ f.", "Which option is a time for one oscillation?"]),
    dict(id="o26t_sound_speed_order", chapter=9, level=1, lo="9f", source="SEAB O-Level 2014 MCQ 13 and 2017 MCQ 14",
         stem="Which list gives the speed of sound in air, steel and water from **slowest to fastest**?",
         correct="air → water → steel",
         wrongs={"air → steel → water": "Sound travels fastest in solids, so steel is last.",
                 "steel → air → water": "Steel is the fastest, not the slowest.",
                 "steel → water → air": "This is fastest to slowest; the question asks slowest first."},
         hints=["Sound needs particles to pass the vibration on.", "Gases are slowest, solids are fastest.", "Liquids are in between."]),
], category=CAT)


@template("o26t_amp_lambda_graph", chapter=9, level=2, lo="9c", category=CAT)
def amp_lambda_graph(rng):
    A, L = nice(rng, (1.5, 40), (1.0, 60), (2.0, 20), (1.5, 30))
    c = f"amplitude {fmt(A)} cm, wavelength {L} cm"
    wrongs = {f"amplitude {fmt(2 * A)} cm, wavelength {L} cm": "Amplitude is from the centre line to a crest, not from trough to crest.",
              f"amplitude {fmt(A)} cm, wavelength {fmt(L / 2)} cm": "A wavelength is one complete wave: crest to the next crest.",
              f"amplitude {fmt(2 * A)} cm, wavelength {fmt(L / 2)} cm": "Both are half a wave out: amplitude is centre-to-crest, wavelength is crest-to-crest."}
    opts, key, mis = text_options(rng, c, wrongs)
    return dict(stem="Fig. 1 shows how the displacement of particles varies with distance along a wave. What are the amplitude and the wavelength?",
                figure=sketches.wave_graph(A, L, kind="distance"), options=opts, key=key, misconceptions=mis, formula=None,
                working=[f"amplitude = height of a crest above the centre line = **{fmt(A)} cm**",
                         f"wavelength = distance from one crest to the next = **{L} cm**", src("SEAB O-Level 2016 MCQ 11")],
                hints=["Amplitude: centre line to crest.", "Wavelength: one whole wave, crest to crest.", "Read both off the axes."])


@template("o26t_freq_time_graph", chapter=9, level=2, lo="9c", category=CAT)
def freq_time_graph(rng):
    T = nice(rng, 4.0, 0.5, 2.5, 1.6)
    f = 1 / T
    return calc_q(rng, "Fig. 1 shows how the displacement of a point on a wave varies with time. What is the frequency of the wave?",
                  f, [(T, "That is the period (time for one wave). Frequency = 1 ÷ period."), (2 / T, "One whole wave is crest to crest, not half a wave."),
                      (1 / (2 * T), "Read the period as the time for ONE complete wave, not two.")],
                  "Hz", "f = 1 ÷ T",
                  [f"period T = time for one complete wave = {fmt(T)} s", f"f = 1 ÷ {fmt(T)} = **{fmt(f)} Hz**", src("SEAB O-Level 2014 MCQ 10")],
                  ["Find the time for one complete wave on the graph.", "That is the period T.", "f = 1 ÷ T."],
                  figure=sketches.wave_graph(1.0, T, kind="time"))


@template("o26t_rings_frequency", chapter=9, level=2, lo="9c", category=CAT)
def rings_frequency(rng):
    n, t = nice(rng, (4, 8), (6, 12), (8, 16), (6, 4))
    f = n / t
    return calc_q(rng, f"Fig. 1 shows the circular wave crests in a ripple tank **{t} s** after the dipper started. What is the frequency of the wave?",
                  f, [(t / n, "That is the period (time per wave). Frequency = waves per second."), ((n - 1) / t, "Count the crests, not the gaps between them."),
                      (n * t / 10, "Frequency = number of waves ÷ time.")],
                  "Hz", "f = number of waves ÷ time",
                  [f"number of crests = {n}", f"f = {n} ÷ {t} = **{fmt(f)} Hz**", src("SEAB O-Level 2020 MCQ 12")],
                  ["Count the crests: each one is one wave made by the dipper.", "Frequency = waves made per second.", "Divide by the time."],
                  figure=k4.ripple_rings(n))


@template("o26t_two_graphs_speed", chapter=9, level=3, lo="9d", category=CAT)
def two_graphs_speed(rng):
    L, T = nice(rng, (3.0, 0.05), (4.0, 0.10), (1.5, 0.03), (2.4, 0.04))
    v = L / T
    return calc_q(rng, "Fig. 1 shows the displacement-distance graph and the displacement-time graph of the same water wave. What is the speed of the wave?",
                  v, [(L * T, "v = f × λ = λ ÷ T, not λ × T."), (L / 2 / T, "One wavelength is crest to crest: read a whole wave."),
                      (L / (T / 2), "One period is a whole wave on the time graph, not half a wave.")],
                  "cm/s", "v = f λ = λ ÷ T",
                  [f"wavelength λ = {fmt(L)} cm (distance graph)", f"period T = {fmt(T)} s, so f = {fmt(1 / T)} Hz (time graph)",
                   f"v = {fmt(1 / T)} × {fmt(L)} = **{fmt(v)} cm/s**", src("SEAB O-Level 2015 MCQ 10 and 2018 MCQ 11")],
                  ["The distance graph gives the wavelength.", "The time graph gives the period, and f = 1 ÷ T.", "v = f λ."],
                  figure=k4.two_wave_graphs(L, T))


@template("o26t_ripple_plane_speed", chapter=9, level=2, lo="9d", category=CAT)
def ripple_plane_speed(rng):
    n, span, f = nice(rng, (5, 16, 5.0), (6, 25, 3.0), (7, 18, 4.0), (5, 12, 6.0))
    lam = span / (n - 1)
    v = f * lam
    return calc_q(rng, f"A dipper vibrates at **{fmt(f)} Hz**. Fig. 1 shows the straight wavefronts in the ripple tank, with the distance across "
                       "them marked. What is the speed of the waves?",
                  v, [(f * span / n, "Count the GAPS between the crests, not the crests."), (f * span, "The marked distance covers several wavelengths."),
                      (span / (n - 1) / f, "v = f × λ, not λ ÷ f.")],
                  "cm/s", "v = f λ",
                  [f"{n} crests → {n - 1} wavelengths in {span} cm, so λ = {fmt(lam)} cm", f"v = {fmt(f)} × {fmt(lam)} = **{fmt(v)} cm/s**",
                   src("SEAB 5086 specimen paper 2024 MCQ 9")],
                  ["Between the first and last crest there are (number of crests − 1) wavelengths.", "Find λ.", "v = f λ."],
                  figure=sketches.wavefronts_sketch(n, f"{span} cm"))


@template("o26t_radio_frequency", chapter=9, level=2, lo="9d", category=CAT)
def radio_frequency(rng):
    lam = nice(rng, 2000, 1200, 3000, 600)
    f = 3.0e8 / lam
    c = sci(f, "Hz")
    wrongs = {sci(f * 10, "Hz"): f"Check the powers of ten: 3.0 × 10⁸ ÷ {lam}.",
              sci(f / 10, "Hz"): f"Check the powers of ten: 3.0 × 10⁸ ÷ {lam}.",
              sci(lam / 3.0e8, "Hz"): "f = v ÷ λ, not λ ÷ v."}
    wrongs = {k: v for k, v in wrongs.items() if k != c}
    opts, key, mis = text_options(rng, c, wrongs)
    return dict(stem="A radio wave travels at 3.0 × 10⁸ m/s (table). What is its frequency?\n\n"
                     + md_table(["quantity", "value"], [["speed", "3.0 × 10⁸ m/s"], ["wavelength", f"{lam} m"]]),
                options=opts, key=key, misconceptions=mis, formula="v = f λ, so f = v ÷ λ",
                working=[f"f = 3.0 × 10⁸ ÷ {lam} = **{c}**", src("SEAB 5086 specimen paper 2024 MCQ 11")],
                hints=["Use v = f λ.", "Rearrange: f = v ÷ λ.", "Keep track of the powers of ten."], figure=None)


@template("o26t_rings_speed_freq", chapter=9, level=3, lo="9d", category=CAT)
def rings_speed_freq(rng):
    n, t, gap = nice(rng, (4, 2.0, 5.0), (3, 1.5, 4.0), (5, 2.0, 3.0), (6, 3.0, 4.0))
    f = n / t
    v = f * gap
    fw = t / n
    c = f"speed {fmt(v)} cm/s, frequency {fmt(f)} Hz"
    wrongs = {f"speed {fmt(fw * gap)} cm/s, frequency {fmt(fw)} Hz": "Frequency = crests per second = number ÷ time, not time ÷ number.",
              f"speed {fmt(fw * gap)} cm/s, frequency {fmt(f)} Hz": "The speed must use the same frequency: v = f λ.",
              f"speed {fmt(v)} cm/s, frequency {fmt(fw)} Hz": "That frequency is the period. f = number of waves ÷ time."}
    opts, key, mis = text_options(rng, c, wrongs)
    return dict(stem=f"A dipper at P makes **{n} wave crests in {fmt(t)} s**. Fig. 1 shows the crests, which are **{fmt(gap)} cm** apart. "
                     "What are the speed and the frequency of the waves?",
                figure=k4.ripple_crests(3, f"{fmt(gap)} cm"), options=opts, key=key, misconceptions=mis, formula="f = waves ÷ time; v = f λ",
                working=[f"f = {n} ÷ {fmt(t)} = {fmt(f)} Hz", f"λ = {fmt(gap)} cm, so v = {fmt(f)} × {fmt(gap)} = **{fmt(v)} cm/s**",
                         src("SEAB O-Level 2019 MCQ 11")],
                hints=["Frequency = number of waves made per second.", "The distance between crests is the wavelength.", "v = f λ."])


@template("o26t_double_frequency", chapter=9, level=2, lo="9d", category=CAT)
def double_frequency(rng):
    f, v = nice(rng, (500, 340), (425, 340), (300, 330), (550, 330))
    lam2 = v / (2 * f)
    c = f"speed {v} m/s, wavelength {fmt(lam2)} m"
    wrongs = {f"speed {v} m/s, wavelength {fmt(2 * lam2)} m": "That is the wavelength at the ORIGINAL frequency. Doubling f halves λ.",
              f"speed {2 * v} m/s, wavelength {fmt(2 * lam2)} m": "The speed of sound in air does not depend on the frequency.",
              f"speed {2 * v} m/s, wavelength {fmt(lam2)} m": "The speed stays the same; only λ changes."}
    opts, key, mis = text_options(rng, c, wrongs)
    return dict(stem=f"A sound wave of frequency **{f} Hz** travels through air at **{v} m/s**. The frequency is doubled to {2 * f} Hz. "
                     "What are the speed and wavelength of the new wave in air?\n\n" + md_table(["", "frequency / Hz", "speed / m/s"], [["before", f, v], ["after", 2 * f, "?"]]),
                options=opts, key=key, misconceptions=mis, formula="v = f λ",
                working=[f"the speed in air stays {v} m/s", f"λ = {v} ÷ {2 * f} = **{fmt(lam2)} m**", src("SEAB O-Level 2016 MCQ 14 and 2021 MCQ 14")],
                hints=["What decides the speed of sound: the source or the medium?", "The medium (air) is the same.", "λ = v ÷ f with the new f."],
                figure=None)


# ================================================================== Ch 12 Electric charge and current
explain_mcqs([
    dict(id="o26t_one_volt", chapter=12, level=1, lo="12g", source="SEAB O-Level 2016 MCQ 15",
         stem="The potential difference across a component is **1 V**. Which statement is correct?",
         correct="1 J of work is done in driving one coulomb of charge through the component.",
         wrongs={"1 C of charge is driven through the component in one second.": "1 C per second is a current of 1 A, not a p.d.",
                 "1 J of work is done in driving one ampere of current through the component.": "p.d. is work per unit CHARGE (coulomb), not per ampere.",
                 "1 W of power is produced in driving one coulomb through the component.": "Volts are joules per coulomb, not watts per coulomb."},
         hints=["p.d. = work done ÷ charge.", "1 V = 1 J/C.", "Which option has joules and coulombs?"]),
    dict(id="o26t_emf_unit", chapter=12, level=1, lo="12f", source="SEAB O-Level 2021 MCQ 17",
         stem="The e.m.f. of a cell is measured in volts. How else can this unit be written?",
         correct="joule per coulomb",
         wrongs={"coulomb per volt": "That is the unit of capacitance, not e.m.f.",
                 "joule coulomb": "e.m.f. is energy DIVIDED by charge.",
                 "watt per coulomb": "Energy is in joules, not watts."},
         hints=["e.m.f. is the energy given to each unit of charge.", "Energy in J, charge in C.", "Energy ÷ charge."]),
    dict(id="o26t_three_wires", chapter=12, level=3, lo="12j", source="SEAB O-Level 2018 MCQ 16",
         stem="Fig. 1 shows the voltage-current graphs for three wires X, Y and Z of the same material and the same length. "
              "How do the resistance and the cross-sectional area change in going from X to Z?",
         correct="resistance increases; cross-sectional area decreases",
         wrongs={"resistance decreases; cross-sectional area decreases": "On a V-I graph a steeper line means a LARGER resistance (R = V ÷ I).",
                 "resistance decreases; cross-sectional area increases": "Z is steepest, so it has the largest resistance.",
                 "resistance increases; cross-sectional area increases": "A thicker wire has a SMALLER resistance; Z must be the thinnest."},
         hints=["R = V ÷ I = gradient of a V-I graph.", "Which line is steepest?", "For the same length, R is inversely proportional to the area."],
         figure=lambda: k4.vi_three_wires()),
], category=CAT)


@template("o26t_vi_graph_resistance", chapter=12, level=2, lo="12i", category=CAT)
def vi_graph_resistance(rng):
    imax, vmax = nice(rng, (5, 20), (4, 24), (2, 5), (3, 12))
    R = vmax / imax
    return calc_q(rng, "Fig. 1 shows the results of an experiment to find the resistance of a wire. What is the resistance of the wire?",
                  R, [(imax / vmax, "R = V ÷ I, not I ÷ V."), (vmax * imax, "Divide V by I; do not multiply."), (vmax, "That is just one voltage reading.")],
                  "Ω", "R = V ÷ I = gradient of the V-I graph",
                  [f"at I = {imax} A, V = {vmax} V", f"R = {vmax} ÷ {imax} = **{fmt(R)} Ω**", src("SEAB O-Level 2014 MCQ 15")],
                  ["Pick a point on the line.", "Read V and I there.", "R = V ÷ I."],
                  figure=figs.graph([(0, 0), (imax, vmax)], imax, vmax, 1 if imax <= 5 else 2, max(1, vmax // 4), xlabel="current / A", ylabel="voltage / V"))


@template("o26t_wire_scaling", chapter=12, level=3, lo="12j", category=CAT)
def wire_scaling(rng):
    L1, A1, R1, L2, A2 = nice(rng, (0.40, 1.0, 0.60, 1.6, 0.50), (2.0, 0.40, 1.6, 0.50, 0.80), (0.50, 0.80, 0.90, 1.5, 0.40), (3.0, 0.60, 2.4, 0.75, 1.2))
    R2 = R1 * (L2 / L1) * (A1 / A2)
    word = "longer" if L2 > L1 else "shorter"
    return calc_q(rng, f"A wire has the length, cross-sectional area and resistance in the table. Another wire of the same material has the second "
                       f"set of dimensions. What is the resistance of the {word} wire?\n\n"
                  + md_table(["wire", "length / m", "area / 10⁻⁶ m²", "resistance / Ω"], [["first", fmt(L1), fmt(A1), fmt(R1)], ["second", fmt(L2), fmt(A2), "?"]]),
                  R2, [(R1 * L2 / L1, "You allowed for the length but not the area."), (R1 * A1 / A2, "You allowed for the area but not the length."),
                       (R1 * (L2 / L1) * (A2 / A1), "R is INVERSELY proportional to area: a thinner wire has MORE resistance.")],
                  "Ω", "R ∝ length ÷ area",
                  [f"length × {fmt(L2 / L1)}, area × {fmt(A2 / A1)}", f"R = {fmt(R1)} × {fmt(L2 / L1)} × {fmt(A1 / A2)} = **{fmt(R2)} Ω**",
                   src("SEAB O-Level 2014 MCQ 16 and 2020 MCQ 18")],
                  ["R is proportional to length.", "R is inversely proportional to cross-sectional area.", "Apply both factors."])


# ================================================================== Ch 13 D.C. circuits
explain_mcqs([
    dict(id="o26t_currents_pqr", chapter=13, level=2, lo="13d", source="SEAB 5086 specimen paper 2024 MCQ 14",
         stem="Fig. 1 shows a 2 Ω and a 4 Ω resistor in parallel with a battery. Ammeters P and Q are in the two branches and ammeter R is in the "
              "main circuit. Which statement about the currents is correct?",
         correct="The current at R is the greatest.",
         wrongs={"The current at P is the greatest.": "P carries more than Q (smaller resistance), but R carries P + Q.",
                 "The current at Q is the greatest.": "The 4 Ω branch carries the SMALLEST current.",
                 "The current is the same at P, Q and R.": "That is true in series. In parallel the current splits."},
         hints=["In parallel, the main current splits between the branches.", "Main current = sum of the branch currents.",
                "Which ammeter measures the total?"],
         figure=lambda: sk.circuit(series=[("A", "R")], parallel=[[("A", "P"), ("R", "2 Ω")], [("A", "Q"), ("R", "4 Ω")]], emf="")),
    dict(id="o26t_x_then_yz", chapter=13, level=2, lo="13d", source="SEAB O-Level 2015 MCQ 17",
         stem="Fig. 1 shows resistor X in series with two resistors Y and Z in parallel. All three resistances are equal. Which statement is correct?",
         correct="The current in Y is smaller than in X and equal to that in Z.",
         wrongs={"The current in Y is larger than in X and equal to that in Z.": "All of X's current splits between Y and Z, so each gets less.",
                 "The current in Y is larger than in X and larger than in Z.": "Y and Z are equal resistors in parallel, so they share equally.",
                 "The current in Y is smaller than in X and larger than in Z.": "Equal resistors in parallel take EQUAL currents."},
         hints=["All the current passes through X.", "At the junction it splits between Y and Z.", "Equal resistances: equal shares."],
         figure=lambda: sk.circuit(series=[("R", "X")], parallel=[[("R", "Y")], [("R", "Z")]], emf="")),
    dict(id="o26t_parallel_statement", chapter=13, level=1, lo="13d", source="SEAB O-Level 2016 MCQ 17",
         stem="A 2 Ω resistor and a 5 Ω resistor are connected in parallel with a power source. Which statement is correct?",
         correct="The current from the power source is the sum of the currents in the two branches.",
         wrongs={"The current in a branch is found by resistance ÷ p.d.": "I = V ÷ R, not R ÷ V.",
                 "The current is equal in both branches.": "The 2 Ω branch takes more current than the 5 Ω branch.",
                 "The p.d.s across the two resistors add up to the p.d. of the source.": "That is true for SERIES. In parallel each branch has the full p.d."},
         hints=["Recall the current rule for parallel circuits.", "And the p.d. rule for parallel circuits.", "I = V ÷ R."]),
    dict(id="o26t_brighter_lamp", chapter=13, level=2, lo="13c", source="SEAB O-Level 2019 MCQ 16",
         stem="Fig. 1 shows a lamp in series with a variable resistor and a battery. The variable resistor is adjusted and the lamp becomes "
              "**brighter**. What happens to the p.d. across the variable resistor and to the current in the lamp?",
         correct="p.d. across the variable resistor decreases; current in the lamp increases",
         wrongs={"p.d. across the variable resistor decreases; current in the lamp decreases": "A brighter lamp needs a LARGER current.",
                 "p.d. across the variable resistor increases; current in the lamp decreases": "Both are the wrong way round.",
                 "p.d. across the variable resistor increases; current in the lamp increases": "The battery p.d. is shared. If the lamp gets more, the resistor gets less."},
         hints=["A brighter lamp has a bigger current and a bigger p.d.", "In series, the p.d.s add up to the battery p.d.",
                "If the lamp's share goes up, what happens to the resistor's share?"],
         figure=lambda: sk.circuit(series=[("R", "variable"), ("lamp", None)], emf="")),
    dict(id="o26t_not_obtainable", chapter=13, level=3, lo="13f", source="SEAB O-Level 2018 MCQ 15",
         stem="Three 6 Ω resistors are **all** connected together, in series, in parallel or in a mixture. Which total resistance **cannot** be obtained?",
         correct="12 Ω",
         wrongs={"2 Ω": "All three in parallel: 6 ÷ 3 = 2 Ω.",
                 "4 Ω": "Two in series (12 Ω) in parallel with the third: 12 × 6 ÷ 18 = 4 Ω.",
                 "9 Ω": "Two in parallel (3 Ω) in series with the third: 3 + 6 = 9 Ω."},
         hints=["List the four ways: all series, all parallel, and the two mixtures.", "Work out each total.",
                "12 Ω would need only two resistors in series."]),
], category=CAT)


@template("o26t_find_r_series", chapter=13, level=3, lo="13g", category=CAT)
def find_r_series(rng):
    E, I, r = nice(rng, (6, 0.75, 2), (4.5, 0.5, 3), (9, 1.5, 2), (12, 0.8, 5))
    R = E / I - r
    return calc_q(rng, f"Fig. 1 shows a {fmt(E)} V battery, a {fmt(r)} Ω resistor and resistor R in series. The ammeter reads **{fmt(I)} A**. "
                       "What is the resistance of R?",
                  R, [(E / I, "That is the TOTAL resistance. Subtract the other resistor."), (E / I + r, "Subtract the known resistor, do not add it."),
                      (I * r, "That is the p.d. across the known resistor, not a resistance.")],
                  "Ω", "R total = V ÷ I; R = R total − r",
                  [f"total resistance = {fmt(E)} ÷ {fmt(I)} = {fmt(E / I)} Ω", f"R = {fmt(E / I)} − {fmt(r)} = **{fmt(R)} Ω**",
                   src("SEAB 5086 specimen paper 2024 MCQ 15")],
                  ["Find the total resistance from the battery p.d. and the current.", "In series, resistances add.", "Subtract the known resistor."],
                  figure=sk.circuit(series=[("A", "A"), ("R", "R"), ("R", f"{fmt(r)} Ω")], emf=f"{fmt(E)} V"))


@template("o26t_three_parallel", chapter=13, level=2, lo="13f", category=CAT)
def three_parallel(rng):
    a, b, c = nice(rng, (6, 3, 2), (4, 4, 2), (12, 6, 4), (3, 6, 6))
    R = 1 / (1 / a + 1 / b + 1 / c)
    return calc_q(rng, f"Fig. 1 shows three resistors, {a} Ω, {b} Ω and {c} Ω, in parallel. What is their effective resistance?",
                  R, [(a + b + c, "Resistances ADD only in series."), (1 / a + 1 / b + 1 / c, "That is 1 ÷ R. Take the reciprocal."),
                      ((a + b + c) / 3, "The effective resistance is not the average; it is less than the smallest resistor.")],
                  "Ω", "1/R = 1/R₁ + 1/R₂ + 1/R₃",
                  [f"1/R = 1/{a} + 1/{b} + 1/{c} = {fmt(1 / R)}", f"R = **{fmt(R)} Ω**", src("SEAB O-Level 2015 MCQ 16")],
                  ["Use the parallel formula.", "Add the reciprocals.", "Turn 1/R back into R; it must be less than the smallest resistor."],
                  figure=sk.circuit(parallel=[[("R", f"{a} Ω")], [("R", f"{b} Ω")], [("R", f"{c} Ω")]], emf=""))


@template("o26t_lamp_pd", chapter=13, level=3, lo="13c", category=CAT)
def lamp_pd(rng):
    E, I, R = nice(rng, (3.0, 0.40, 5.0), (4.5, 0.30, 10), (6.0, 0.50, 8.0), (3.0, 0.25, 6.0))
    VL = E - I * R
    return calc_q(rng, f"Fig. 1 shows a {fmt(R)} Ω resistor in series with a lamp. A voltmeter across the battery reads **{fmt(E)} V** and the "
                       f"ammeter reads **{fmt(I * 1000)} mA**. What is the p.d. across the lamp?",
                  VL, [(I * R, "That is the p.d. across the RESISTOR."), (E, "That is the p.d. across the whole circuit."),
                       (E + I * R, "In series the p.d.s add up to the battery p.d.: subtract, do not add.")],
                  "V", "V = IR; series p.d.s add up",
                  [f"p.d. across resistor = {fmt(I)} × {fmt(R)} = {fmt(I * R)} V", f"p.d. across lamp = {fmt(E)} − {fmt(I * R)} = **{fmt(VL)} V**",
                   src("SEAB O-Level 2016 MCQ 16")],
                  ["Change mA to A.", "Find the p.d. across the resistor with V = IR.", "The two p.d.s add up to the battery p.d."],
                  figure=sk.circuit(series=[("A", "A"), ("R", f"{fmt(R)} Ω"), ("lamp", None)], emf=f"{fmt(E)} V"))


@template("o26t_r_from_meters", chapter=13, level=4, lo="13g", category=CAT)
def r_from_meters(rng):
    E, V1, I, I1 = nice(rng, (12, 8, 3, 1), (18, 6, 4, 1), (10, 4, 5, 2), (9, 3, 4, 1))
    R = (E - V1) / (I - I1)
    return calc_q(rng, f"In Fig. 1 the battery e.m.f. is {E} V. The voltmeter across the first resistor reads **{V1} V**, the main ammeter reads "
                       f"**{I} A** and the ammeter in one parallel branch reads **{I1} A**. What is the resistance of R?",
                  R, [(V1 / (I - I1), "Use the p.d. across the PARALLEL part: e.m.f. − voltmeter reading."), ((E - V1) / I, "Use the current in R's branch, not the main current."),
                      ((E - V1) / I1, "That is the other branch's current.")],
                  "Ω", "series p.d.s add; branch currents add; R = V ÷ I",
                  [f"p.d. across the parallel part = {E} − {V1} = {E - V1} V", f"current in R = {I} − {I1} = {I - I1} A",
                   f"R = {E - V1} ÷ {I - I1} = **{fmt(R)} Ω**", src("SEAB O-Level 2018 MCQ 18")],
                  ["The p.d.s across the series resistor and the parallel part add up to the e.m.f.", "The branch currents add up to the main current.",
                   "R = V ÷ I for R's branch."],
                  figure=sk.circuit(series=[("R", ""), ("A", f"{I} A")], parallel=[[("R", ""), ("A", f"{I1} A")], [("R", "R")]], emf=f"{E} V",
                                    voltmeter=("series", 0)))


@template("o26t_emf_parallel", chapter=13, level=3, lo="13g", category=CAT)
def emf_parallel(rng):
    a, b, I = nice(rng, (4, 12, 1.5), (2, 8, 2.5), (10, 15, 1.0), (6, 12, 1.5))
    Rp = a * b / (a + b)
    E = I * Rp
    return calc_q(rng, f"Fig. 1 shows a {a} Ω and a {b} Ω resistor in parallel with a battery. The ammeter reads **{fmt(I)} A**. What is the e.m.f. of the battery?",
                  E, [(I * (a + b), "The resistors are in PARALLEL, not series."), (I * a, f"The whole {fmt(I)} A does not flow through the {a} Ω resistor."),
                      (I * b, f"The whole {fmt(I)} A does not flow through the {b} Ω resistor.")],
                  "V", "1/R = 1/R₁ + 1/R₂; E = I R",
                  [f"R = {a} × {b} ÷ ({a} + {b}) = {fmt(Rp)} Ω", f"E = {fmt(I)} × {fmt(Rp)} = **{fmt(E)} V**", src("SEAB O-Level 2019 MCQ 15")],
                  ["Find the effective resistance of the parallel pair.", "The ammeter reads the total current.", "E = I × R."],
                  figure=sk.circuit(series=[("A", "A")], parallel=[[("R", f"{a} Ω")], [("R", f"{b} Ω")]], emf=""))


@template("o26t_identical_parallel", chapter=13, level=2, lo="13f", category=CAT)
def identical_parallel(rng):
    n, Re = nice(rng, (3, 0.40), (5, 0.60), (4, 0.75), (6, 0.50))
    R = n * Re
    return calc_q(rng, f"When **{n}** identical resistors are connected in parallel, their effective resistance is **{fmt(Re)} Ω**. "
                       "What is the resistance of one resistor?\n\n" + md_table(["number in parallel", "effective resistance / Ω"], [[n, fmt(Re)]]),
                  R, [(Re / n, "Parallel makes the total SMALLER than one resistor, so one resistor is larger."), (Re, "One resistor alone has more resistance than the group."),
                      (Re * n / 2, f"n identical resistors in parallel give R ÷ n; here n = {n}.")],
                  "Ω", "n identical resistors in parallel: R_eff = R ÷ n",
                  [f"R = {n} × {fmt(Re)} = **{fmt(R)} Ω**", src("SEAB O-Level 2021 MCQ 16")],
                  ["n identical resistors in parallel: R_eff = R ÷ n.", "Rearrange for R.", "Check: one resistor > effective resistance."], figure=None)


# ================================================================== Ch 14 Practical electricity
explain_mcqs([
    dict(id="o26t_both_formulae", chapter=14, level=1, lo="14b", source="SEAB O-Level 2021 MCQ 18",
         stem="In which pair are **both** formulae correct?",
         correct="E = VIt and P = VI",
         wrongs={"E = VIt and P = V ÷ I": "V ÷ I is the resistance, not the power.",
                 "E = VI ÷ t and P = V ÷ I": "Energy = power × time, so multiply by t; and P = VI.",
                 "E = VI ÷ t and P = VI": "Energy = power × time = VI × t, not VI ÷ t."},
         hints=["Power = p.d. × current.", "Energy = power × time.", "So E = VIt."]),
    dict(id="o26t_fuse_rating", chapter=14, level=1, lo="14e", source="SEAB O-Level 2017 MCQ 19",
         stem="A plug for a lamp contains a fuse rated at **3 A**. Which statement is correct?",
         correct="The fuse melts and breaks the circuit if the current is larger than 3 A.",
         wrongs={"The fuse contains an electromagnet.": "A fuse is a thin wire that melts. A circuit breaker uses an electromagnet.",
                 "The fuse is connected to the earth pin of the plug.": "The fuse is in the LIVE wire.",
                 "The fuse keeps the current at 3 A.": "The fuse does not control the current; it only breaks the circuit when the current is too large."},
         hints=["What is inside a fuse?", "What happens to a thin wire carrying too large a current?", "Which wire is the fuse in?"]),
    dict(id="o26t_earth_wire_shock", chapter=14, level=2, lo="14f", source="SEAB 5086 specimen paper 2024 MCQ 17",
         stem="The earth wire of a cable is attached to the metal case of an appliance. How does it prevent an electric shock if the live wire touches the case?",
         correct="It lets a large current flow to earth, which blows the fuse.",
         wrongs={"It lets a current flow to earth so that the appliance keeps working.": "The large current blows the fuse, so the appliance stops working.",
                 "It stops the fuse from blowing.": "Blowing the fuse is exactly how the appliance is made safe.",
                 "It reduces the current to a safe level.": "The earth path has very LOW resistance, so the current becomes very large."},
         hints=["The earth wire has a very low resistance.", "What does a very large current do to the fuse?", "Once the fuse blows, the case is no longer live."]),
], category=CAT)


@template("o26t_resistor_heat", chapter=14, level=2, lo="14b", category=CAT)
def resistor_heat(rng):
    R, I, t = nice(rng, (4, 3, 5), (10, 2, 6), (6, 0.5, 20), (8, 1.5, 4))
    V = I * R
    E = V * I * t
    return calc_q(rng, "A current passes through a resistor (table). How much energy is changed into heat?\n\n"
                  + md_table(["quantity", "value"], [["resistance", f"{R} Ω"], ["current", f"{fmt(I)} A"], ["time", f"{t} s"]]),
                  E, [(R * I * t, "That is V × t. Multiply by the current as well: E = VIt."), (V * t, "E = V × I × t: you left out I."),
                      (I * I * R, "That is the power. Multiply by the time.")],
                  "J", "V = IR; E = VIt",
                  [f"V = {fmt(I)} × {R} = {fmt(V)} V", f"E = {fmt(V)} × {fmt(I)} × {t} = **{fmt(E)} J**", src("SEAB O-Level 2015 MCQ 19")],
                  ["Find the p.d. with V = IR.", "Energy = VIt.", "Check the units: V × A × s = J."])


@template("o26t_heater_time", chapter=14, level=2, lo="14b", category=CAT)
def heater_time(rng):
    I, V, E = nice(rng, (5, 240, 360000), (8, 230, 552000), (6, 230, 690000), (4, 240, 288000))
    t = E / (V * I)
    return calc_q(rng, f"An electric heater takes a current of **{I} A** from a **{V} V** supply. How long does it take to convert **{E:,} J** of electrical energy?"
                  .replace(",", " "),
                  t, [(E / V, "Divide by the power (V × I), not by V alone."), (E / I, "Divide by the power (V × I), not by I alone."),
                      (t / 60, "That is the time in minutes; the options are in seconds.")],
                  "s", "E = VIt, so t = E ÷ (VI)",
                  [f"power = {V} × {I} = {V * I} W", f"t = {E} ÷ {V * I} = **{fmt(t)} s**", src("SEAB O-Level 2014 MCQ 18 and 2018 MCQ 19")],
                  ["Find the power: P = VI.", "Energy = power × time.", "t = E ÷ P."], figure=None)


# ================================================================== Ch 15 Magnetism and electromagnetism
@template("o26t_parallel_wires", chapter=15, level=5, lo="15h", category=CAT)
def parallel_wires(rng):
    correct = "towards P"
    wrongs = {"away from P": "That is the force when the currents are in OPPOSITE directions. Currents in the same direction attract.",
              "into the page": "P's field at Q is into or out of the page, but the FORCE is at right angles to both the field and the current.",
              "out of the page": "Use the left-hand rule with P's field at Q: the force lies in the plane of the page."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem="Fig. 1 shows two long parallel vertical wires P and Q, both carrying a **downward** current. The magnetic field of P exerts a "
                     "force on Q, at right angles to Q. What is the direction of the force on Q?",
                figure=k4.parallel_wires(), options=opts, key=key, misconceptions=mis,
                formula="field of a wire: right-hand grip rule; force: Fleming's left-hand rule",
                working=["Right-hand grip: P's downward current makes a field at Q (to its right) that points OUT of the page.",
                         "Left-hand rule at Q: first finger out of the page (field), second finger down (current) → thumb points to the LEFT.",
                         "So the force on Q is **towards P**: currents in the same direction attract.", src("SEAB 5086 specimen paper 2024 MCQ 19")],
                hints=["First find the direction of P's magnetic field at Q (right-hand grip rule).",
                       "Then use Fleming's left-hand rule for Q: field, current, force.", "Parallel currents in the same direction attract."])


@template("o26t_electromagnet_compasses", chapter=15, level=4, lo="15f", category=CAT)
def electromagnet_compasses(rng):
    n_right = rng.random() < 0.5            # True: the magnet's N faces the coil
    # The coil end facing the magnet is the opposite pole (it attracts). Outside a magnet the field runs N -> S.
    if n_right:   # coil: left N, right S. left of left end: field away from N -> points left; right of S end: into S -> left; above: N->S -> right
        c = "left compass ←, compass above →, right compass ←"
        ends = "left end N, right end S"
    else:         # coil: left S, right N
        c = "left compass →, compass above ←, right compass →"
        ends = "left end S, right end N"
    flip = {"←": "→", "→": "←"}
    allr = "left compass →, compass above →, right compass →"
    alll = "left compass ←, compass above ←, right compass ←"
    rev = "".join(flip.get(ch, ch) for ch in c)
    wrongs = {rev: "Every needle is reversed: the coil end next to the magnet's pole is the OPPOSITE pole, because they attract.",
              allr: "Outside the coil the field curves round from its N end to its S end, so the end compasses do not point the same way as the one above.",
              alll: "Outside the coil the field curves round from its N end to its S end, so the end compasses do not point the same way as the one above."}
    wrongs = {k: v for k, v in wrongs.items() if k != c}
    opts, key, mis = text_options(rng, c, wrongs)
    return dict(stem="Fig. 1 shows an electromagnet that **attracts** a permanent bar magnet. The bar magnet is removed and three plotting compasses "
                     "are placed: one beyond each end of the coil and one above its middle. Which way do the compass needles (N ends) point?",
                figure=k4.electromagnet_attracts(n_right), options=opts, key=key, misconceptions=mis,
                formula="unlike poles attract; outside a magnet the field goes from N to S",
                working=[f"The coil end facing the magnet is the opposite pole, so the coil has {ends}.",
                         "A compass needle points along the field: away from an N pole, towards an S pole, and from N to S above the coil.",
                         f"**{c}**", src("SEAB O-Level 2020 MCQ 37")],
                hints=["The electromagnet attracts the magnet: which pole must the facing end of the coil be?",
                       "Then the other end of the coil is the other pole.", "Compass N ends point along the field lines: from N round to S."])
