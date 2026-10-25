"""Chapter 16 Radioactivity: extra calculation templates (nuclide numbers, decay changes, half-life)."""
from .. import sketches2 as sk
from .base import calc_q, fmt, md_table, nice, template
from .calc_ch16 import ALPHA, BETA, HALF_LIVES, N0S, NUCLIDES, nuc


# ---------------------------------------------------------------- L1
@template("c16_electrons_neutral", chapter=16, level=1, lo="16a")
def electrons_neutral(rng):
    sym, name, Z, A = rng.choice(NUCLIDES)
    return calc_q(rng, f"The table gives the nuclide of a neutral {name} atom. How many electrons does the atom have?\n\n" + md_table(["nuclide"], [[nuc(A, Z, sym)]]), Z, [
        (A, "That is the nucleon number. In a neutral atom, electrons = protons."),
        (A - Z, "That is the number of neutrons."),
        (A + Z, "Electrons = proton number in a neutral atom."),
    ], "", "neutral atom: number of electrons = proton number Z", [f"Z = {Z}", f"electrons = **{Z}**"],
        ["A neutral atom has no overall charge.", "Each proton (+) is balanced by one electron (−).", "Read the proton number (bottom number)."], sf=None)


@template("c16_read_nucleon_number", chapter=16, level=1, lo="16c")
def read_nucleon_number(rng):
    sym, name, Z, A = rng.choice(NUCLIDES)
    return calc_q(rng, f"The table shows the nuclide notation for an isotope of {name}. What is its nucleon number?\n\n" + md_table(["nuclide"], [[nuc(A, Z, sym)]]), A, [
        (Z, "That is the proton number (the bottom number)."),
        (A - Z, "That is the neutron number."),
        (A + Z, "The nucleon number is the top number itself."),
    ], "", "nuclide notation: top = nucleon number A, bottom = proton number Z", [f"top number = **{A}**"],
        ["In nuclide notation the nucleon number is written at the top.", "The proton number is at the bottom.", "Read the top number."], sf=None)


@template("c16_read_proton_number", chapter=16, level=1, lo="16c")
def read_proton_number(rng):
    sym, name, Z, A = rng.choice(NUCLIDES)
    return calc_q(rng, f"The table shows the nuclide notation for an isotope of {name}. How many protons are in its nucleus?\n\n" + md_table(["nuclide"], [[nuc(A, Z, sym)]]), Z, [
        (A, "That is the nucleon number (protons + neutrons)."),
        (A - Z, "That is the number of neutrons."),
        (A + Z, "The proton number is the bottom number."),
    ], "", "nuclide notation: bottom number = proton number Z", [f"proton number = **{Z}**"],
        ["Which number in the notation counts protons?", "It is the smaller, bottom number.", "Read it off."], sf=None)


@template("c16_half_activity", chapter=16, level=1, lo="16g")
def half_activity(rng):
    T, unit = rng.choice(HALF_LIVES)
    n0 = rng.choice(N0S)
    return calc_q(rng, f"A source has an activity of **{n0} counts per minute** and a half-life of **{T} {unit}**. The table summarises this. What is its activity after **{T} {unit}**?\n\n" + md_table(["initial activity / counts per min", "half-life"], [[n0, f"{T} {unit}"]]), n0 / 2, [
        (n0, "After one half-life the activity has HALVED."),
        (n0 / 4, "That is after TWO half-lives."),
        (n0 - T, "Halve the activity; do not subtract the time."),
    ], "counts per min", "after one half-life, activity halves", [f"{n0} ÷ 2 = **{n0 // 2} counts per min**"],
        ["What happens to the activity in one half-life?", "It halves.", f"{n0} ÷ 2."], sf=None)


@template("c16_subtract_background", chapter=16, level=1, lo="16f")
def subtract_background(rng):
    bg = nice(rng, 15, 20, 25, 30)
    true = nice(rng, 120, 180, 250, 400)
    return calc_q(rng, f"A GM tube near a source reads **{true + bg} counts per minute**. The background count rate is **{bg} counts per minute**. The table summarises this. What is the count rate due to the source alone?\n\n" + md_table(["measured / counts per min", "background / counts per min"], [[true + bg, bg]]), true, [
        (true + 2 * bg, "Subtract the background; do not add it."),
        (true + bg, "That still includes the background."),
        ((true + bg) / bg, "Subtract the background count rate."),
    ], "counts per min", "corrected count rate = measured − background", [f"{true + bg} − {bg}", f"= **{true} counts per min**"],
        ["The detector records background radiation as well.", "Remove it from the reading.", "Subtract."], sf=None)


@template("c16_neutrons_heavy", chapter=16, level=1, lo="16b")
def neutrons_heavy(rng):
    sym, name, Z, A = rng.choice([s for s in NUCLIDES if s[2] > 50])
    N = A - Z
    return calc_q(rng, f"Fig. 1 shows the decay curve of a {name} source. Its nuclide is shown in the table. How many neutrons are in each nucleus?\n\n" + md_table(["nuclide"], [[nuc(A, Z, sym)]]), N, [
        (A, "That is the nucleon number."),
        (Z, "That is the proton number."),
        (A + Z, "Neutrons = nucleon number − proton number."),
    ], "", "N = A − Z", [f"N = {A} − {Z}", f"= **{N}**"],
        ["Nucleon number = protons + neutrons.", "Subtract the proton number.", f"{A} − {Z}."],
        figure=sk.decay_curve(800, 4), sf=None)


# ---------------------------------------------------------------- L2
@template("c16_count_halflives", chapter=16, level=2, lo="16g")
def count_halflives(rng):
    T, unit = rng.choice(HALF_LIVES)
    n = nice(rng, 2, 3, 4, 5)
    t = n * T
    table = md_table(["half-life", "time elapsed"], [[f"{T} {unit}", f"{t} {unit}"]])
    return calc_q(rng, f"A radioactive sample is left for some time.\n\n{table}\n\nHow many half-lives have passed?", n, [
        (t * T, "Number of half-lives = time ÷ half-life."),
        (n * 2, "Divide the time by the half-life."),
        (T / t, "Time ÷ half-life, not half-life ÷ time."),
    ], "", "number of half-lives = time ÷ half-life", [f"{t} ÷ {T}", f"= **{n}**"],
        ["How many half-lives fit into the time?", "Divide.", f"{t} ÷ {T}."], sf=None)


@template("c16_time_to_quarter", chapter=16, level=2, lo="16g")
def time_to_quarter(rng):
    T, unit = rng.choice(HALF_LIVES)
    return calc_q(rng, f"Fig. 1 shows the decay curve of a source with a half-life of **{T} {unit}**. How long does it take for the activity to fall to a QUARTER of its starting value?", 2 * T, [
        (T, "One half-life leaves a HALF. A quarter needs two halvings."),
        (4 * T, "A quarter is (½)², so two half-lives, not four."),
        (T / 4, "Each halving takes a full half-life."),
    ], unit, "1 → ½ → ¼: two half-lives", [f"¼ = ½ × ½: 2 half-lives", f"time = 2 × {T} = **{2 * T} {unit}**"],
        ["After one half-life, what fraction remains?", "Halve again.", "Count the halvings."],
        figure=sk.decay_curve(800, T, unit=unit), sf=None)


@template("c16_isotope_neutron_difference", chapter=16, level=2, lo="16b")
def isotope_neutron_difference(rng):
    sym, name, Z, A1, A2 = rng.choice([("C", "carbon", 6, 12, 14), ("U", "uranium", 92, 235, 238), ("Cl", "chlorine", 17, 35, 37),
                                       ("H", "hydrogen", 1, 1, 3), ("O", "oxygen", 8, 16, 18), ("I", "iodine", 53, 127, 131)])
    table = md_table(["isotope", "nuclide"], [["first", nuc(A1, Z, sym)], ["second", nuc(A2, Z, sym)]])
    return calc_q(rng, f"The table shows two isotopes of {name}.\n\n{table}\n\nHow many more neutrons does the second isotope have than the first?", A2 - A1, [
        (A2 - Z, "That is the number of neutrons in the second isotope, not the difference."),
        (0, "Isotopes have the same number of PROTONS but different numbers of neutrons."),
        (A2 + A1 - 2 * Z, "Subtract the two neutron numbers."),
    ], "", "isotopes: same Z, so the difference in A is the difference in neutrons", [f"neutrons: {A1 - Z} and {A2 - Z}", f"difference = **{A2 - A1}**"],
        ["Isotopes have the same proton number.", "Any difference in nucleon number is due to neutrons.", f"{A2} − {A1}."], sf=None)


@template("c16_after_two_halflives", chapter=16, level=2, lo="16g")
def after_two_halflives(rng):
    T, unit = rng.choice(HALF_LIVES)
    n0 = rng.choice(N0S)
    return calc_q(rng, f"Fig. 1 shows the decay curve of a source with a half-life of **{T} {unit}** and an initial activity of **{n0} counts per minute**. What is its activity after **{2 * T} {unit}**?", n0 / 4, [
        (n0 / 2, "That is after ONE half-life; {2T} is two half-lives.".replace("{2T}", f"{2 * T} {unit}")),
        (0, "Two half-lives leave a quarter, not zero."),
        (n0 / 8, "That is after THREE half-lives."),
    ], "counts per min", "two half-lives: activity ÷ 4", [f"{2 * T} ÷ {T} = 2 half-lives", f"{n0} → {n0 // 2} → **{n0 // 4} counts per min**"],
        ["How many half-lives is the time?", "Halve once for each half-life.", f"{n0} ÷ 2 ÷ 2."],
        figure=sk.decay_curve(n0, T, unit=unit), sf=None)


@template("c16_corrected_from_table", chapter=16, level=2, lo="16f")
def corrected_from_table(rng):
    bg = nice(rng, 20, 30, 40)
    vals = [nice(rng, 300, 400), nice(rng, 150, 200)]
    row = rng.randint(0, 1)
    table = md_table(["time / min", "measured count rate / counts per min"], [[0, vals[0] + bg], [10, vals[1] + bg]])
    return calc_q(rng, f"The background count rate is **{bg} counts per minute**. The table shows measured count rates near a source.\n\n{table}\n\nWhat is the corrected count rate at **t = {10 * row} min**?", vals[row], [
        (vals[row] + 2 * bg, "Subtract the background."),
        (vals[row] + bg, "That is the measured value; subtract the background."),
        (vals[1 - row], "Use the reading at the time asked for."),
    ], "counts per min", "corrected = measured − background", [f"{vals[row] + bg} − {bg}", f"= **{vals[row]} counts per min**"],
        ["Find the measured value at that time.", "Background must be removed.", "Subtract."], sf=None)


@template("c16_read_halflife_graph_b", chapter=16, level=2, lo="16g")
def read_halflife_graph_b(rng):
    T, unit = rng.choice(HALF_LIVES[:12])
    n0 = rng.choice([1600, 3200, 4000, 6400])
    return calc_q(rng, f"Fig. 1 shows the number of undecayed nuclei in a sample against time. How long does it take for the number to fall from **{n0 // 2}** to **{n0 // 4}**?", T, [
        (2 * T, "From ½ to ¼ is ONE halving, so one half-life."),
        (T / 2, "Each halving takes a full half-life."),
        (3 * T, "Read the times at ½ and ¼ of the starting value."),
    ], unit, "each halving takes one half-life, wherever you start", [f"{n0 // 2} → {n0 // 4} is one halving", f"time = one half-life = **{T} {unit}**"],
        ["How many halvings is it from the first number to the second?", "Every halving takes the same time.", "Read the half-life from the curve."],
        figure=sk.decay_curve(n0, T, unit=unit), sf=None)


# ---------------------------------------------------------------- L3
@template("c16_two_alphas_nucleon", chapter=16, level=3, lo="16e")
def two_alphas_A(rng):
    sym, name, Z, A, dsym, dname = rng.choice(ALPHA)
    return calc_q(rng, f"A nucleus of {name}, {nuc(A, Z, sym)}, emits two alpha particles one after the other. The table summarises this. What is the nucleon number of the final nucleus?\n\n" + md_table(["starting nuclide", "decays"], [[nuc(A, Z, sym), "2 alpha"]]), A - 8, [
        (A - 4, "That is after ONE alpha decay."),
        (A - 2, "Each alpha particle carries away 4 nucleons, not 1."),
        (A - 4 * 1 - 2, "Each alpha decay reduces A by 4: 2 × 4 = 8."),
    ], "", "each alpha: A − 4, Z − 2", [f"A = {A} − 2 × 4", f"= **{A - 8}**"],
        ["What is an alpha particle made of?", "Each one removes 4 nucleons.", f"{A} − 8."], sf=None)


@template("c16_two_betas_proton", chapter=16, level=3, lo="16e")
def two_betas_Z(rng):
    sym, name, Z, A, dsym, dname = rng.choice(BETA)
    return calc_q(rng, f"A nucleus of {name}, {nuc(A, Z, sym)}, undergoes two beta decays one after the other. The table summarises this. What is the proton number of the final nucleus?\n\n" + md_table(["starting nuclide", "decays"], [[nuc(A, Z, sym), "2 beta"]]), Z + 2, [
        (Z - 2, "In beta decay a neutron becomes a proton: Z goes UP by 1 each time."),
        (Z + 1, "That is after ONE beta decay."),
        (Z, "Beta decay changes the proton number."),
    ], "", "each beta: Z + 1, A unchanged", [f"Z = {Z} + 2", f"= **{Z + 2}**"],
        ["In beta decay, a neutron turns into a proton and an electron.", "So Z increases by 1 for each decay.", f"{Z} + 2."], sf=None)


@template("c16_alpha_then_beta_proton", chapter=16, level=3, lo="16e")
def alpha_then_beta_A_Z(rng):
    sym, name, Z, A, dsym, dname = rng.choice(ALPHA)
    Zf = Z - 2 + 1
    return calc_q(rng, f"A nucleus of {name}, {nuc(A, Z, sym)}, emits an alpha particle and then a beta particle. The table summarises this. What is the proton number of the final nucleus?\n\n" + md_table(["starting nuclide", "decays"], [[nuc(A, Z, sym), "alpha, then beta"]]), Zf, [
        (Z - 2, "That is after the alpha decay only; the beta decay then adds 1."),
        (Z - 3, "Beta decay INCREASES Z by 1."),
        (A - 4, "That is the nucleon number, not the proton number."),
    ], "", "alpha: Z − 2; beta: Z + 1", [f"after alpha: Z = {Z - 2}", f"after beta: Z = {Z - 2} + 1 = **{Zf}**"],
        ["Deal with one decay at a time.", "Alpha: Z − 2. Beta: Z + 1.", "Combine the changes."], sf=None)


@template("c16_percent_remaining", chapter=16, level=3, lo="16g")
def percent_remaining(rng):
    n = nice(rng, 1, 2, 3, 4)
    T, unit = rng.choice(HALF_LIVES)
    pct = 100 / 2 ** n
    return calc_q(rng, f"A sample is left for **{n * T} {unit}**. The half-life is **{T} {unit}**. The table summarises this. What percentage of the original radioactive nuclei remains?\n\n" + md_table(["half-life", "time"], [[f"{T} {unit}", f"{n * T} {unit}"]]), pct, [
        (100 - 100 / 2 ** n, "That is the percentage that has DECAYED."),
        (100 / (2 * n), f"Halve {n} times: (½)^{n}, not ½ × 1/{n}."),
        (50, "That is after one half-life only." if n > 1 else "Check the number of half-lives."),
    ], "%", "remaining = 100 % × (½)^n", [f"n = {n * T} ÷ {T} = {n}", f"remaining = 100 ÷ 2^{n}", f"= **{fmt(pct)} %**"],
        ["How many half-lives have passed?", "Halve 100 % that many times.", "100 → 50 → 25 → …"])


@template("c16_mass_remaining", chapter=16, level=3, lo="16g")
def mass_remaining(rng):
    m0 = nice(rng, 16, 32, 40, 64, 80)
    n = nice(rng, 2, 3, 4)
    T, unit = rng.choice(HALF_LIVES)
    return calc_q(rng, f"A sample contains **{m0} g** of a radioactive isotope with a half-life of **{T} {unit}**. The table summarises this. What mass of the isotope remains undecayed after **{n * T} {unit}**?\n\n" + md_table(["starting mass / g", "half-life", "time"], [[m0, f"{T} {unit}", f"{n * T} {unit}"]]), m0 / 2 ** n, [
        (m0 / n, f"Each half-life HALVES the mass: divide by 2^{n}, not {n}."),
        (m0 - m0 / 2 ** n, "That is the mass that has DECAYED."),
        (m0 / 2, "That is after one half-life only."),
    ], "g", "mass remaining = m₀ × (½)^n", [f"n = {n}", f"{m0} ÷ 2^{n} = {m0} ÷ {2 ** n}", f"= **{fmt(m0 / 2 ** n)} g**"],
        ["Find the number of half-lives.", "Halve the mass for each half-life.", f"{m0} ÷ {2 ** n}."])


@template("c16_halflife_from_percent", chapter=16, level=3, lo="16g")
def halflife_from_percent(rng):
    n = nice(rng, 2, 3)
    T = nice(rng, 2, 3, 5, 6, 8)
    unit = nice(rng, "days", "hours", "min")
    pct = 100 / 2 ** n
    t = n * T
    table = md_table(["time / " + unit, "activity remaining / %"], [[0, 100], [t, fmt(pct)]])
    return calc_q(rng, f"The activity of a sample is measured at two times.\n\n{table}\n\nWhat is the half-life?", T, [
        (t, f"{fmt(pct)} % remaining means {n} half-lives have passed, not one."),
        (t / 2 if n == 3 else t / 3, f"{fmt(pct)} % = (½)^{n}: divide the time by {n}."),
        (t * n, "Half-life = time ÷ number of halvings."),
    ], unit, "count halvings from 100 % to the final %; T = t ÷ n", [f"100 % → " + " → ".join(fmt(100 / 2 ** k) + " %" for k in range(1, n + 1)), f"{n} half-lives in {t} {unit}", f"T = **{T} {unit}**"],
        ["How many halvings take 100 % down to that value?", "Those halvings took the whole time.", "Divide the time by the number of halvings."], sf=None)


# ---------------------------------------------------------------- L4
@template("c16_time_to_percent", chapter=16, level=4, lo="16g")
def time_to_percent(rng):
    n = nice(rng, 3, 4)
    T, unit = rng.choice(HALF_LIVES)
    pct = 100 / 2 ** n
    return calc_q(rng, f"Fig. 1 shows the decay curve of a source whose half-life is **{T} {unit}**. How long does it take for its activity to fall to **{fmt(pct)} %** of the starting value?", n * T, [
        (T * 100 / pct, "That treats the fall as proportional. Count the halvings instead."),
        ((n - 1) * T, "Count the halvings again: 100 → 50 → 25 → …"),
        (T * (100 - pct) / 50, "Each halving takes one half-life."),
    ], unit, "number of halvings × half-life", [f"100 % → " + " → ".join(fmt(100 / 2 ** k) + " %" for k in range(1, n + 1)) + f": {n} halvings", f"time = {n} × {T} = **{n * T} {unit}**"],
        ["Write the percentage as (½)^n.", "Find n.", "Multiply by the half-life."],
        figure=sk.decay_curve(800, T, t_max=max(4, n) * T, unit=unit), sf=None)


@template("c16_mass_decayed", chapter=16, level=4, lo="16g")
def mass_decayed(rng):
    m0 = nice(rng, 20, 40, 64, 80, 120)
    n = nice(rng, 2, 3)
    T, unit = rng.choice(HALF_LIVES)
    dec = m0 - m0 / 2 ** n
    table = md_table(["starting mass / g", "half-life", "time"], [[m0, f"{T} {unit}", f"{n * T} {unit}"]])
    return calc_q(rng, f"A radioactive isotope decays into a stable product.\n\n{table}\n\nWhat mass of the isotope has DECAYED by the end of this time?", dec, [
        (m0 / 2 ** n, "That is the mass that REMAINS. Subtract it from the starting mass."),
        (m0 / 2, "That is after one half-life only."),
        (m0, "Some of the isotope is still undecayed."),
    ], "g", "decayed = m₀ − m₀ (½)^n", [f"remaining = {m0} ÷ {2 ** n} = {fmt(m0 / 2 ** n)} g", f"decayed = {m0} − {fmt(m0 / 2 ** n)}", f"= **{fmt(dec)} g**"],
        ["Find the mass remaining first.", "Halve once per half-life.", "Subtract from the starting mass."])


@template("c16_neutrons_after_alpha", chapter=16, level=4, lo="16e")
def neutrons_after_alpha(rng):
    sym, name, Z, A, dsym, dname = rng.choice(ALPHA)
    Nf = (A - 4) - (Z - 2)
    return calc_q(rng, f"A nucleus of {name}, {nuc(A, Z, sym)}, emits an alpha particle. The table summarises this. How many neutrons does the new nucleus contain?\n\n" + md_table(["parent nuclide", "decay"], [[nuc(A, Z, sym), "alpha"]]), Nf, [
        (A - Z, "That is the number of neutrons BEFORE the decay."),
        (A - Z - 4, "An alpha particle contains 2 neutrons (and 2 protons), not 4 neutrons."),
        (A - 4, "That is the new nucleon number; subtract the new proton number."),
    ], "", "new A = A − 4, new Z = Z − 2; N = A − Z", [f"new A = {A - 4}, new Z = {Z - 2}", f"N = {A - 4} − {Z - 2}", f"= **{Nf}**"],
        ["Find the new nucleon and proton numbers.", "An alpha particle has 2 protons and 2 neutrons.", "Neutrons = A − Z."], sf=None)


@template("c16_activity_at_fraction_time", chapter=16, level=4, lo="16g")
def activity_at_fraction_time(rng):
    T, unit = rng.choice(HALF_LIVES)
    n0 = rng.choice([1600, 3200, 6400])
    n = nice(rng, 3, 4)
    table = md_table(["time", "activity / counts per min"], [[f"0 {unit}", n0], [f"{T} {unit}", n0 // 2]])
    return calc_q(rng, f"The table shows the activity of a source at two times.\n\n{table}\n\nWhat will its activity be at **{n * T} {unit}**?", n0 / 2 ** n, [
        (n0 / 2 ** (n - 1), "Count the half-lives from t = 0, not from the second reading."),
        (n0 / n, "Halve repeatedly; do not divide by the number of half-lives."),
        (n0 / 2 - n * 100, "Each half-life halves the activity."),
    ], "counts per min", "half-life from the table; activity = n₀ × (½)^n", [f"half-life = {T} {unit}", f"{n * T} {unit} = {n} half-lives", f"activity = {n0} ÷ {2 ** n} = **{fmt(n0 / 2 ** n)} counts per min**"],
        ["Use the table to find the half-life.", "How many half-lives is the new time?", "Halve that many times."], sf=None)


# ---------------------------------------------------------------- L5
@template("c16_initial_mass", chapter=16, level=5, lo="16g")
def initial_mass(rng):
    m = nice(rng, 1.5, 2, 2.5, 5)
    n = nice(rng, 2, 3, 4)
    T, unit = rng.choice(HALF_LIVES)
    table = md_table(["mass remaining now / g", "half-life", "time since it was made"], [[fmt(m), f"{T} {unit}", f"{n * T} {unit}"]])
    return calc_q(rng, f"A radioactive sample was made some time ago.\n\n{table}\n\nWhat mass of the isotope was there when it was made?", m * 2 ** n, [
        (m * n, f"Going back each half-life DOUBLES the mass: × 2^{n}."),
        (m * 2, "That is only one half-life back."),
        (m / 2 ** n, "Going back in time the mass was LARGER."),
    ], "g", "m₀ = m × 2^n", [f"n = {n * T} ÷ {T} = {n}", f"m₀ = {fmt(m)} × {2 ** n}", f"= **{fmt(m * 2 ** n)} g**"],
        ["Work backwards in time.", "One half-life earlier there was twice as much.", f"Double {n} times."])


@template("c16_decay_chain", chapter=16, level=5, lo="16e")
def decay_chain(rng):
    sym, name, Z, A = rng.choice([("U", "uranium", 92, 238), ("Th", "thorium", 90, 232), ("Ra", "radium", 88, 226), ("Rn", "radon", 86, 222)])
    na, nb = rng.choice([(1, 2), (2, 1), (2, 2), (3, 2)])
    Af = A - 4 * na
    Zf = Z - 2 * na + nb
    table = md_table(["starting nuclide", "alpha decays", "beta decays"], [[nuc(A, Z, sym), na, nb]])
    return calc_q(rng, f"A nucleus goes through a short decay chain.\n\n{table}\n\nWhat is the proton number of the final nucleus?", Zf, [
        (Z - 2 * na - nb, "Beta decay INCREASES Z by 1."),
        (Z - 2 * na, "Include the beta decays: each adds 1 to Z."),
        (Af, "That is the final nucleon number, not the proton number."),
    ], "", f"each alpha: Z − 2; each beta: Z + 1", [f"Z = {Z} − 2 × {na} + {nb}", f"= **{Zf}**", f"(final nucleon number = {A} − 4 × {na} = {Af})"],
        ["Treat alpha and beta decays separately.", "Alpha: Z − 2. Beta: Z + 1.", "Add up all the changes."], sf=None)


@template("c16_halflife_with_background_two", chapter=16, level=5, lo="16g")
def halflife_with_background_two(rng):
    bg = nice(rng, 20, 30, 40, 50)
    n0 = rng.choice([800, 1600, 2400])
    n = nice(rng, 2, 3)
    T = nice(rng, 2, 3, 5, 10)
    unit = nice(rng, "min", "hours")
    t = n * T
    table = md_table([f"time / {unit}", "measured count rate / counts per min"], [[0, n0 + bg], [t, n0 // 2 ** n + bg]])
    return calc_q(rng, f"The background count rate is **{bg} counts per minute**. The table shows two measured readings near a source.\n\n{table}\n\nWhat is the half-life of the source?", T, [
        (t / (n - 1) if n > 1 else t, "Subtract the background from BOTH readings before counting halvings."),
        (t, f"The corrected count rate halves {n} times, not once."),
        (t * n, "Half-life = time ÷ number of halvings."),
    ], unit, "correct both readings, count halvings, T = t ÷ n", [f"corrected: {n0} and {n0 // 2 ** n}", f"{n0} → {n0 // 2 ** n} is {n} halvings", f"T = {t} ÷ {n} = **{T} {unit}**"],
        ["Remove the background from each reading.", "How many halvings take the first corrected value to the second?", "Divide the time by that number."], sf=None)


@template("c16_two_sources_ratio", chapter=16, level=5, lo="16g")
def two_sources_ratio(rng):
    TA, TB = rng.choice([(2, 4), (3, 6), (5, 10), (1, 3)])
    t = TA * TB * nice(rng, 1, 2) if TB % TA else TB * nice(rng, 1, 2)
    nA, nB = t // TA, t // TB
    ratio = 2 ** (nA - nB)
    table = md_table(["source", "half-life / days", "activity at t = 0 / counts per min"], [["A", TA, 1600], ["B", TB, 1600]])
    return calc_q(rng, f"Two sources start with the same activity.\n\n{table}\n\nAfter **{t} days**, how many times greater is the activity of B than that of A?", ratio, [
        (TB / TA, "Work out how many halvings EACH source has had."),
        (nA - nB, "The ratio is 2 raised to the difference in the number of half-lives."),
        (1, "A has the shorter half-life, so it has decayed more."),
    ], "", "A has t/T_A halvings, B has t/T_B; ratio = 2^(n_A − n_B)", [f"A: {t} ÷ {TA} = {nA} half-lives → 1600 ÷ {2 ** nA} = {fmt(1600 / 2 ** nA)}", f"B: {t} ÷ {TB} = {nB} half-lives → 1600 ÷ {2 ** nB} = {fmt(1600 / 2 ** nB)}", f"ratio = **{fmt(ratio)}**"],
        ["Find the number of half-lives for each source.", "Work out each activity.", "Divide B's activity by A's."], sf=None)
