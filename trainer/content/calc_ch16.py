"""Chapter 16 Radioactivity: nuclide numbers, decay equations, half-life from tables, graphs and readings."""
from .. import sketches2 as sk
from .base import fmt, md_table, nice, numeric_options, template, text_options

SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def nuc(A, Z, sym):
    return f"{str(A).translate(SUP)}{str(Z).translate(SUB)}{sym}"


# (symbol, name, Z, A)
NUCLIDES = [("C", "carbon", 6, 14), ("N", "nitrogen", 7, 14), ("O", "oxygen", 8, 18), ("Na", "sodium", 11, 24), ("Al", "aluminium", 13, 27),
            ("Cl", "chlorine", 17, 37), ("K", "potassium", 19, 40), ("Fe", "iron", 26, 56), ("Co", "cobalt", 27, 60), ("Sr", "strontium", 38, 90),
            ("I", "iodine", 53, 131), ("Cs", "caesium", 55, 137), ("Rn", "radon", 86, 222), ("Ra", "radium", 88, 226), ("U", "uranium", 92, 238),
            ("Po", "polonium", 84, 210), ("Th", "thorium", 90, 234), ("Am", "americium", 95, 241), ("Tc", "technetium", 43, 99)]
SMALL = [("He", "helium", 2, 4), ("Li", "lithium", 3, 7), ("Be", "beryllium", 4, 9)]

# parent -> daughter for alpha decay: (sym, name, Z, A, daughter sym, daughter name)
ALPHA = [("U", "uranium", 92, 238, "Th", "thorium"), ("Ra", "radium", 88, 226, "Rn", "radon"), ("Po", "polonium", 84, 210, "Pb", "lead"),
         ("Am", "americium", 95, 241, "Np", "neptunium"), ("Rn", "radon", 86, 222, "Po", "polonium"), ("Th", "thorium", 90, 232, "Ra", "radium")]
BETA = [("C", "carbon", 6, 14, "N", "nitrogen"), ("Sr", "strontium", 38, 90, "Y", "yttrium"), ("Co", "cobalt", 27, 60, "Ni", "nickel"),
        ("I", "iodine", 53, 131, "Xe", "xenon"), ("Cs", "caesium", 55, 137, "Ba", "barium"), ("Th", "thorium", 90, 234, "Pa", "protactinium"),
        ("K", "potassium", 19, 40, "Ca", "calcium"), ("Na", "sodium", 11, 24, "Mg", "magnesium")]
HALF_LIVES = [(2, "min"), (3, "min"), (4, "min"), (5, "min"), (6, "min"), (8, "min"), (10, "min"), (12, "min"), (15, "min"), (20, "min"),
              (2, "hours"), (3, "hours"), (6, "hours"), (8, "hours"), (2, "days"), (4, "days"), (5, "days"), (8, "days"), (3, "years"), (5, "years")]
N0S = [800, 1600, 2400, 3200, 4000, 4800, 6400, 8000]


# ---------------------------------------------------------------- L1
@template("c16_neutron_number_small", chapter=16, level=1, lo="16a")
def neutron_number_small(rng):
    sym, name, Z, A = rng.choice(SMALL)
    N = A - Z
    opts, key, mis = numeric_options(rng, N, [
        (A, "That is the nucleon number (total protons + neutrons)."),
        (Z, "That is the proton number, not the number of neutrons."),
        (A + Z, "You added the two numbers. Neutrons = nucleon number − proton number."),
    ], sf=None)
    return dict(
        stem=f"Fig. 1 shows an atom of {name}, {nuc(A, Z, sym)}. How many neutrons are in its nucleus?",
        figure=sk.atom_diagram(Z, N, symbol=nuc(A, Z, sym)),
        options=opts, key=key, misconceptions=mis,
        formula="neutron number = nucleon number − proton number (N = A − Z)",
        working=[f"nucleon number A = {A}, proton number Z = {Z}", f"N = A − Z = {A} − {Z}", f"= **{N}**"],
        hints=["The top number is the nucleon number (protons + neutrons); the bottom number is the proton number.",
               f"Neutrons = {A} − {Z}.",
               "Count the light-coloured particles in the diagram to check."],
    )


@template("c16_neutron_number", chapter=16, level=1, lo="16a")
def neutron_number(rng):
    sym, name, Z, A = rng.choice(NUCLIDES)
    N = A - Z
    opts, key, mis = numeric_options(rng, N, [
        (A, "That is the nucleon number (total protons + neutrons)."),
        (Z, "That is the proton number, not the number of neutrons."),
        (A + Z, "You added the two numbers. Neutrons = nucleon number − proton number."),
    ], sf=None)
    table = md_table(["nuclide", "proton number", "nucleon number"], [[nuc(A, Z, sym), Z, A]])
    return dict(
        stem=f"The table gives the numbers for a nuclide of {name}.\n\n{table}\n\nHow many neutrons are in one nucleus?",
        options=opts, key=key, misconceptions=mis,
        formula="neutron number = nucleon number − proton number (N = A − Z)",
        working=[f"N = A − Z = {A} − {Z}", f"= **{N}**"],
        hints=["Nucleon number = protons + neutrons.",
               "Subtract the proton number from the nucleon number.",
               f"{A} − {Z}."],
    )


@template("c16_nucleon_number_from_counts", chapter=16, level=1, lo="16a")
def nucleon_number_from_counts(rng):
    sym, name, Z, A = rng.choice(NUCLIDES)
    N = A - Z
    opts, key, mis = numeric_options(rng, A, [
        (N, "That is the number of neutrons only."),
        (Z, "That is the proton number only."),
        (abs(N - Z) or N + 1, "You subtracted. Nucleon number = protons + neutrons."),
    ], sf=None)
    table = md_table(["particle", "number in the nucleus"], [["protons", Z], ["neutrons", N]])
    return dict(
        stem=f"The table shows the particles in the nucleus of a {name} atom.\n\n{table}\n\nWhat is its nucleon number?",
        options=opts, key=key, misconceptions=mis,
        formula="nucleon number = number of protons + number of neutrons",
        working=[f"A = Z + N = {Z} + {N}", f"= **{A}**"],
        hints=["Nucleons are the particles in the nucleus: protons AND neutrons.",
               "Add the two numbers.",
               f"{Z} + {N}."],
    )


# ---------------------------------------------------------------- L2
@template("c16_half_life_from_table", chapter=16, level=2, lo="16f")
def half_life_from_table(rng):
    T, unit = rng.choice(HALF_LIVES[:10])
    n0 = rng.choice(N0S)
    rows = [[k * T, n0 // 2 ** k] for k in range(4)]
    table = md_table([f"time / {unit}", "count rate / counts per min"], rows)
    opts, key, mis = numeric_options(rng, T, [
        (2 * T, "That is the time for the count rate to fall to a QUARTER (two half-lives)."),
        (3 * T, "That is the time for three halvings, not one."),
        (T / 2, "Half-life is the time for the count rate to halve, not half of the time interval."),
    ], unit=unit, sf=None)
    return dict(
        stem=f"The table shows how the count rate from a radioactive source changes with time (background already subtracted).\n\n{table}\n\nWhat is the half-life of the source?",
        options=opts, key=key, misconceptions=mis,
        formula="half-life = time for the activity (count rate) to fall to half its value",
        working=[f"count rate falls from {n0} to {n0 // 2} between t = 0 and t = {T} {unit}", f"half-life = **{T} {unit}**"],
        hints=["Find the time at which the count rate is half of its starting value.",
               f"The count rate starts at {n0}. When is it {n0 // 2}?",
               "Check: it halves again over the next equal interval."],
    )


@template("c16_half_life_from_graph", chapter=16, level=2, lo="16f")
def half_life_from_graph(rng):
    T, unit = rng.choice(HALF_LIVES[:10])
    n0 = rng.choice(N0S)
    opts, key, mis = numeric_options(rng, T, [
        (2 * T, "That is the time for the activity to fall to a quarter: two half-lives."),
        (T / 2, "Half-life is the time to fall to HALF the activity, read on the time axis."),
        (4 * T, "That is four half-lives, the full width of the graph."),
    ], unit=unit, sf=None)
    return dict(
        stem=f"Fig. 1 shows how the activity of a radioactive source changes with time. What is the half-life of the source?",
        figure=sk.decay_curve(n0, T, unit=unit),
        options=opts, key=key, misconceptions=mis,
        formula="half-life = time for the activity to fall to half its value (read from the graph)",
        working=[f"initial activity = {n0}; half of this is {n0 // 2}", f"from the graph, activity = {n0 // 2} at t = {T} {unit}", f"half-life = **{T} {unit}**"],
        hints=["Read the activity at t = 0 and halve it.",
               f"Find where the curve reaches {n0 // 2} and read the time underneath.",
               "You can check by halving again: the next halving takes the same time."],
    )


@template("c16_remaining_after_halflives", chapter=16, level=2, lo="16f")
def remaining_after_halflives(rng):
    T, unit = rng.choice(HALF_LIVES)
    n = nice(rng, 2, 3, 4)
    n0 = rng.choice(N0S)
    t = n * T
    left = n0 / 2 ** n
    opts, key, mis = numeric_options(rng, left, [
        (n0 / n, f"You divided by {n}. Each half-life HALVES the amount, so after {n} half-lives it is divided by 2^{n} = {2 ** n}."),
        (n0 / 2, "That is after ONE half-life only."),
        (n0 / 2 ** (n - 1), f"That is after {n - 1} half-lives. Count the halvings again: {t} ÷ {T} = {n}."),
    ], sf=None)
    return dict(
        stem=f"Fig. 1 shows the decay curve of a source with a half-life of **{T} {unit}**. Its activity is **{n0} counts per minute** at the start. What is the activity after **{t} {unit}**?",
        figure=sk.decay_curve(n0, T, t_max=max(4 * T, t), unit=unit),
        options=opts, key=key, misconceptions=mis,
        formula="number of half-lives = time ÷ half-life; activity halves each half-life",
        working=[f"number of half-lives = {t} ÷ {T} = {n}", f"activity = {n0} → " + " → ".join(fmt(n0 / 2 ** k, sf=None) for k in range(1, n + 1)),
                 f"= **{fmt(left, sf=None)} counts per minute**"],
        hints=["How many half-lives fit into the time given?",
               f"{t} ÷ {T} = {n} half-lives. Halve the activity that many times.",
               f"{n0} halved {n} times."],
    )


# ---------------------------------------------------------------- L3
@template("c16_alpha_decay_product", chapter=16, level=3, lo="16d")
def alpha_decay_product(rng):
    sym, name, Z, A, dsym, dname = rng.choice(ALPHA)
    correct = nuc(A - 4, Z - 2, dsym)
    wrongs = {nuc(A - 2, Z - 4, dsym): "You swapped the changes: an alpha particle carries away 4 nucleons and 2 protons.",
              nuc(A - 4, Z, sym): "The proton number also falls by 2, so the element changes.",
              nuc(A - 2, Z - 1, dsym): "An alpha particle is ⁴₂He: nucleon number down by 4, proton number down by 2."}
    opts, key, mis = text_options(rng, correct, wrongs)
    table = md_table(["", "nucleon number", "proton number"], [[f"{name}, {nuc(A, Z, sym)}", A, Z], ["alpha particle", 4, 2]])
    return dict(
        stem=f"A nucleus of {name} emits an alpha particle.\n\n{table}\n\nWhich nuclide is formed?",
        options=opts, key=key, misconceptions=mis,
        formula="alpha decay: nucleon number −4, proton number −2 (the alpha particle is ⁴₂He)",
        working=[f"{nuc(A, Z, sym)} → {correct} + ⁴₂He", f"nucleon number: {A} − 4 = {A - 4}; proton number: {Z} − 2 = {Z - 2}", f"new nuclide = **{correct}** ({dname})"],
        hints=["An alpha particle is a helium nucleus: 2 protons and 2 neutrons.",
               "Subtract 4 from the nucleon number and 2 from the proton number.",
               f"{A} − 4 and {Z} − 2; the proton number changes, so it is a different element."],
    )


@template("c16_beta_decay_product", chapter=16, level=3, lo="16d")
def beta_decay_product(rng):
    sym, name, Z, A, dsym, dname = rng.choice(BETA)
    correct = nuc(A, Z + 1, dsym)
    wrongs = {nuc(A, Z - 1, dsym): "In beta decay a neutron becomes a proton, so the proton number goes UP by 1.",
              nuc(A - 1, Z + 1, dsym): "The nucleon number is unchanged: a neutron is replaced by a proton, so the total stays the same.",
              nuc(A - 4, Z - 2, dsym): "That is the result of ALPHA decay."}
    opts, key, mis = text_options(rng, correct, wrongs)
    table = md_table(["", "nucleon number", "proton number"], [[f"{name}, {nuc(A, Z, sym)}", A, Z], ["beta particle", 0, -1]])
    return dict(
        stem=f"A nucleus of {name} emits a beta particle.\n\n{table}\n\nWhich nuclide is formed?",
        options=opts, key=key, misconceptions=mis,
        formula="beta decay: a neutron becomes a proton + electron; nucleon number unchanged, proton number +1",
        working=[f"{nuc(A, Z, sym)} → {correct} + ⁰₋₁e", f"nucleon number stays {A}; proton number {Z} + 1 = {Z + 1}", f"new nuclide = **{correct}** ({dname})"],
        hints=["A beta particle is an electron from the nucleus, formed when a neutron turns into a proton.",
               "The nucleon number does not change; the proton number rises by 1.",
               f"Nucleon number {A}, proton number {Z + 1}."],
    )


@template("c16_half_life_with_background", chapter=16, level=3, lo="16f")
def half_life_with_background(rng):
    T, unit = rng.choice(HALF_LIVES[:10])
    bg = nice(rng, 20, 30, 40, 50, 60)
    n0 = rng.choice(N0S)
    rows = [[k * T, n0 // 2 ** k + bg] for k in range(4)]
    table = md_table([f"time / {unit}", "measured count rate / counts per min"], rows)
    opts, key, mis = numeric_options(rng, T, [
        (2 * T, "After subtracting the background the count rate halves in less time than this."),
        (T / 2, "Half-life is the time for the corrected count rate to halve."),
        (3 * T, "Subtract the background first; the corrected count halves each interval."),
    ], unit=unit, sf=None)
    return dict(
        stem=f"The background count rate in a laboratory is **{bg} counts per minute**. The table shows the measured count rate near a radioactive source.\n\n{table}\n\nWhat is the half-life of the source?",
        options=opts, key=key, misconceptions=mis,
        formula="corrected count rate = measured − background; half-life = time for the corrected rate to halve",
        working=[f"corrected count rates: {n0}, {n0 // 2}, {n0 // 4}, {n0 // 8} (subtracting {bg})", f"{n0} → {n0 // 2} takes {T} {unit}", f"half-life = **{T} {unit}**"],
        hints=["The measured count includes background radiation. Subtract it from every reading first.",
               f"Corrected readings: {n0}, {n0 // 2}, {n0 // 4}, ...",
               "How long does the corrected count take to halve?"],
    )


# ---------------------------------------------------------------- L4
@template("c16_time_to_fraction", chapter=16, level=4, lo="16f")
def time_to_fraction(rng):
    T, unit = rng.choice(HALF_LIVES)
    n = nice(rng, 2, 3, 4)
    frac = 2 ** n
    t = n * T
    opts, key, mis = numeric_options(rng, t, [
        (frac * T, f"You multiplied by {frac}. Falling to 1/{frac} takes {n} half-lives, not {frac}."),
        (T, "That is one half-life, which leaves half, not 1/" + str(frac) + "."),
        ((n - 1) * T, f"That is one half-life too few: 1/{frac} needs {n} halvings."),
    ], unit=unit, sf=None)
    return dict(
        stem=f"Fig. 1 shows the decay curve of a source whose half-life is **{T} {unit}**. How long does it take for the activity to fall to **1/{frac}** of its initial value?",
        figure=sk.decay_curve(1600, T, t_max=max(4, n) * T, unit=unit),
        options=opts, key=key, misconceptions=mis,
        formula="1 → 1/2 → 1/4 → 1/8 ...: each halving takes one half-life",
        working=[f"1/{frac} = (1/2)^{n}, so {n} half-lives are needed", f"time = {n} × {T}", f"= **{t} {unit}**"],
        hints=["Write 1/" + str(frac) + " as a power of a half.",
               f"1/{frac} = (1/2)^{n}, so {n} halvings.",
               f"Each halving takes {T} {unit}."],
    )


@template("c16_half_life_from_two_readings", chapter=16, level=4, lo="16f")
def half_life_from_two_readings(rng):
    T, unit = rng.choice(HALF_LIVES)
    n = nice(rng, 2, 3, 4)
    n0 = rng.choice(N0S)
    t = n * T
    left = n0 // 2 ** n
    table = md_table([f"time / {unit}", "activity / counts per min"], [[0, n0], [t, left]])
    opts, key, mis = numeric_options(rng, T, [
        (t / 2, "You halved the time. The activity fell by a factor of " + str(2 ** n) + f", which is {n} halvings."),
        (t, f"The whole time covers {n} half-lives, not one."),
        (t / 2 ** n, f"You divided by {2 ** n}. Divide the time by the NUMBER of half-lives ({n})."),
    ], unit=unit, sf=None)
    return dict(
        stem=f"The table shows the corrected activity of a radioactive source at two times.\n\n{table}\n\nWhat is the half-life of the source?",
        options=opts, key=key, misconceptions=mis,
        formula="count the halvings from N₀ to N; half-life = time ÷ number of halvings",
        working=[f"{n0} → " + " → ".join(str(n0 // 2 ** k) for k in range(1, n + 1)) + f": {n} halvings", f"half-life = {t} ÷ {n}", f"= **{T} {unit}**"],
        hints=["How many times must the activity halve to get from the first reading to the second?",
               f"{n0} halves {n} times to reach {left}.",
               f"Those {n} halvings took {t} {unit} altogether."],
    )


# ---------------------------------------------------------------- L5
@template("c16_initial_activity", chapter=16, level=5, lo="16f")
def initial_activity(rng):
    T, unit = rng.choice(HALF_LIVES)
    n = nice(rng, 2, 3, 4)
    left = nice(rng, 50, 100, 150, 200, 250, 300)
    t = n * T
    n0 = left * 2 ** n
    table = md_table(["half-life", "time since the sample was made", "activity now / counts per min"], [[f"{T} {unit}", f"{t} {unit}", left]])
    opts, key, mis = numeric_options(rng, n0, [
        (left * n, f"You multiplied by {n}. Each half-life DOUBLES the amount when you work backwards: ×2^{n}."),
        (left * 2, "That is one half-life back only."),
        (left * 2 ** (n - 1), f"One doubling too few: {t} ÷ {T} = {n} half-lives."),
    ], sf=None)
    return dict(
        stem=f"The table gives data for a radioactive sample.\n\n{table}\n\nWhat was the activity of the sample when it was made?",
        options=opts, key=key, misconceptions=mis,
        formula="going back one half-life doubles the activity",
        working=[f"number of half-lives = {t} ÷ {T} = {n}", f"initial activity = {left} × 2^{n} = {left} × {2 ** n}", f"= **{n0} counts per minute**"],
        hints=["Work backwards in time: the activity was double its present value one half-life ago.",
               f"{t} ÷ {T} = {n} half-lives ago.",
               f"Double {left} that many times."],
    )


@template("c16_sample_age", chapter=16, level=5, lo="16f")
def sample_age(rng):
    T = nice(rng, 5700, 30, 1600, 8, 12)
    unit = {5700: "years", 30: "years", 1600: "years", 8: "days", 12: "hours"}[T]
    n = nice(rng, 2, 3, 4)
    frac = 2 ** n
    age = n * T
    table = md_table(["activity of fresh sample", "activity of old sample", "half-life"], [[f"{frac * 25} counts per min", "25 counts per min", f"{T} {unit}"]])
    opts, key, mis = numeric_options(rng, age, [
        (frac * T, f"You multiplied by {frac}. The activity fell to 1/{frac}, which is {n} halvings, not {frac}."),
        (T, "That is one half-life, which would halve the activity only."),
        ((n - 1) * T, f"One halving too few: {frac * 25} → 25 takes {n} halvings."),
    ], unit=unit, sf=None)
    return dict(
        stem=f"The table compares the activity of a fresh sample of a material with that of an old sample of the same material and mass.\n\n{table}\n\nEstimate the age of the old sample.",
        options=opts, key=key, misconceptions=mis,
        formula="number of halvings from fresh to old activity; age = halvings × half-life",
        working=[f"{frac * 25} → 25 is a fall to 1/{frac} = (1/2)^{n}: {n} half-lives", f"age = {n} × {T}", f"= **{age} {unit}**"],
        hints=["How many times must the fresh activity halve to reach the old activity?",
               f"{frac * 25} ÷ 25 = {frac} = 2^{n}.",
               f"Age = {n} half-lives."],
    )
