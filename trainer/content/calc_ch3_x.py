"""Chapter 3 Force and Pressure: extra calculation templates (weight, density, pressure)."""
from .. import figs, sketches
from .base import calc_q, fmt, md_table, nice, template

G = 10


# ---------------------------------------------------------------- L1
@template("c3_weight_on_moon_simple", chapter=3, level=1, lo="3e")
def weight_on_moon_simple(rng):
    m = nice(rng, 5, 10, 20, 25, 50, 60)
    W = m * 1.6
    return calc_q(rng, f"Fig. 1 shows an astronaut's tool kit of mass **{m} kg** on the Moon, where g = 1.6 N/kg. What is its weight on the Moon?", W, [
        (m * 10, "That is its weight on Earth. Use g = 1.6 N/kg on the Moon."),
        (m / 1.6, "W = m × g, not m ÷ g."),
        (m, "That is the mass in kg; weight is a force in newtons."),
    ], "N", "weight = mass × gravitational field strength", ["W = m g", f"= {m} × 1.6", f"= **{fmt(W)} N**"],
        ["Weight = mass × g.", "Use the Moon's value of g.", f"{m} × 1.6."],
        figure=sketches.two_bodies_sketch(["g = 10 N/kg"], ["g = 1.6 N/kg", f"mass {m} kg"]))


@template("c3_density_lump", chapter=3, level=1, lo="3g")
def density_lump(rng):
    rho = nice(rng, 2.5, 2.7, 7.9, 8.9, 11.3, 19.3)
    V = nice(rng, 10, 20, 40, 50)
    m = rho * V
    return calc_q(rng, "Fig. 1 shows a lump of metal with its mass and volume. What is the density of the metal?", rho, [
        (V / m, "Density = mass ÷ volume, not volume ÷ mass."),
        (m * V, "You multiplied. Density = mass ÷ volume."),
        (m - V, "Divide, do not subtract."),
    ], "g/cm³", "density = mass ÷ volume", ["ρ = m ÷ V", f"= {fmt(m)} ÷ {V}", f"= **{fmt(rho)} g/cm³**"],
        ["Which formula defines density?", "Mass in g, volume in cm³ gives g/cm³.", f"{fmt(m)} ÷ {V}."],
        figure=sketches.lump_sketch([f"mass = {fmt(m)} g", f"volume = {V} cm³"]))


@template("c3_mass_from_density", chapter=3, level=1, lo="3g")
def mass_from_density(rng):
    rho = nice(rng, 0.8, 1.0, 1.2, 2.7, 7.8)
    V = nice(rng, 50, 100, 200, 250)
    m = rho * V
    return calc_q(rng, f"Fig. 1 shows a block of volume **{V} cm³** made of a material of density **{fmt(rho)} g/cm³**. What is its mass?", m, [
        (V / rho, "m = ρ × V, not V ÷ ρ."),
        (rho / V, "m = ρ × V."),
        (rho + V, "Multiply density by volume."),
    ], "g", "mass = density × volume", ["m = ρ V", f"= {fmt(rho)} × {V}", f"= **{fmt(m)} g**"],
        ["Rearrange density = mass ÷ volume.", "mass = density × volume.", f"{fmt(rho)} × {V}."],
        figure=sketches.lump_sketch([f"density = {fmt(rho)} g/cm³", f"volume = {V} cm³"]))


@template("c3_force_from_pressure", chapter=3, level=1, lo="3i")
def force_from_pressure(rng):
    p = nice(rng, 200, 500, 800, 1200, 2500)
    A = nice(rng, 0.2, 0.5, 1.5, 2.0)
    F = p * A
    return calc_q(rng, f"Fig. 1 shows a crate exerting a pressure of **{p} Pa** on the ground over an area of **{fmt(A)} m²**. What force does it exert on the ground?", F, [
        (p / A, "F = p × A, not p ÷ A."),
        (A / p, "F = p × A."),
        (p, "That is the pressure; multiply by the area to get the force."),
    ], "N", "force = pressure × area", ["F = p A", f"= {p} × {fmt(A)}", f"= **{fmt(F)} N**"],
        ["Rearrange pressure = force ÷ area.", "force = pressure × area.", f"{p} × {fmt(A)}."],
        figure=sketches.pressure_block("F = ?", f"area = {fmt(A)} m²"))


@template("c3_volume_from_density", chapter=3, level=1, lo="3g")
def volume_from_density(rng):
    rho = nice(rng, 2, 4, 5, 8, 10)
    V = nice(rng, 15, 20, 30, 40, 60)
    m = rho * V
    return calc_q(rng, f"Fig. 1 shows a piece of metal of mass **{m} g** and density **{rho} g/cm³**. What is its volume?", V, [
        (m * rho, "V = m ÷ ρ, not m × ρ."),
        (rho / m, "V = m ÷ ρ."),
        (m - rho, "Divide, do not subtract."),
    ], "cm³", "volume = mass ÷ density", ["V = m ÷ ρ", f"= {m} ÷ {rho}", f"= **{fmt(V)} cm³**"],
        ["Rearrange density = mass ÷ volume for V.", "V = m ÷ ρ.", f"{m} ÷ {rho}."],
        figure=sketches.lump_sketch([f"mass = {m} g", f"density = {rho} g/cm³"]))


@template("c3_weight_bag_earth", chapter=3, level=1, lo="3e")
def weight_bag_earth(rng):
    m = nice(rng, 0.5, 1.2, 2.5, 3.6, 8, 15)
    W = m * G
    return calc_q(rng, f"Fig. 1 shows a bag of sugar of mass **{fmt(m)} kg** hanging from a spring balance on Earth (g = 10 N/kg). What does the balance read?", W, [
        (m / G, "W = m × g, not m ÷ g."),
        (m, "That is the mass; the balance reads weight in newtons."),
        (m * 9.8 * 10, "Use g = 10 N/kg once only."),
    ], "N", "weight = mass × g", ["W = m g", f"= {fmt(m)} × 10", f"= **{fmt(W)} N**"],
        ["A spring balance measures weight.", "W = m × g.", f"{fmt(m)} × 10."],
        figure=sketches.spring_balance("W = ?", f"{fmt(m)} kg"))


# ---------------------------------------------------------------- L2
@template("c3_g_from_weight", chapter=3, level=2, lo="3d")
def g_from_weight(rng):
    m = nice(rng, 2, 4, 5, 8, 10)
    g = nice(rng, 3.7, 8.9, 11, 24, 1.6)
    W = round(m * g, 2)
    return calc_q(rng, f"Fig. 1 shows a spring balance on another planet. A mass of **{m} kg** hung on it reads **{fmt(W)} N**. What is the gravitational field strength on that planet?", g, [
        (W * m, "g = W ÷ m, not W × m."),
        (m / W, "g = W ÷ m."),
        (W, "That is the weight; divide by the mass."),
    ], "N/kg", "g = weight ÷ mass", ["g = W ÷ m", f"= {fmt(W)} ÷ {m}", f"= **{fmt(g)} N/kg**"],
        ["g is the gravitational force per unit mass.", "Divide the weight by the mass.", f"{fmt(W)} ÷ {m}."],
        figure=sketches.spring_balance(f"{fmt(W)} N", f"{m} kg"))


@template("c3_density_kg_m3", chapter=3, level=2, lo="3g")
def density_kg_m3(rng):
    rho = nice(rng, 800, 1000, 2500, 2700, 7800)
    V = nice(rng, 0.02, 0.05, 0.1, 0.2)
    m = rho * V
    return calc_q(rng, f"Fig. 1 shows a block of mass **{fmt(m)} kg** and volume **{fmt(V)} m³**. What is its density?", rho, [
        (V / m, "Density = mass ÷ volume."),
        (m * V, "You multiplied. Density = mass ÷ volume."),
        (rho / 1000, "That would be in g/cm³; the data are in kg and m³."),
    ], "kg/m³", "density = mass ÷ volume", ["ρ = m ÷ V", f"= {fmt(m)} ÷ {fmt(V)}", f"= **{fmt(rho)} kg/m³**"],
        ["Density = mass ÷ volume.", "kg ÷ m³ gives kg/m³.", f"{fmt(m)} ÷ {fmt(V)}."],
        figure=sketches.lump_sketch([f"mass = {fmt(m)} kg", f"volume = {fmt(V)} m³"]))


@template("c3_area_from_pressure", chapter=3, level=2, lo="3i")
def area_from_pressure(rng):
    F = nice(rng, 600, 800, 1200, 2000)
    p = nice(rng, 2000, 4000, 5000, 8000, 10000)
    A = F / p
    return calc_q(rng, f"Fig. 1 shows a load of weight **{F} N** resting on the ground. The pressure under it is **{p} Pa**. What is the area of contact?", A, [
        (p / F, "A = F ÷ p, not p ÷ F."),
        (F * p, "A = F ÷ p."),
        (A * 10000, "That is in cm²; the answer in m² is F ÷ p."),
    ], "m²", "area = force ÷ pressure", ["A = F ÷ p", f"= {F} ÷ {p}", f"= **{fmt(A)} m²**"],
        ["Rearrange p = F ÷ A.", "A = F ÷ p.", f"{F} ÷ {p}."],
        figure=sketches.pressure_block(f"{F} N", "area = ?"))


@template("c3_weight_table_planets", chapter=3, level=2, lo="3e")
def weight_table_planets(rng):
    planet, g = rng.choice([("Mars", 3.7), ("Jupiter", 25), ("Venus", 8.9), ("Mercury", 3.7), ("the Moon", 1.6)])
    m = nice(rng, 2, 5, 10, 20, 40)
    W = m * g
    table = md_table(["body", "g / N/kg"], [["Earth", 10], [planet, fmt(g)]])
    return calc_q(rng, f"The table gives the gravitational field strength on two bodies.\n\n{table}\n\nWhat is the weight of a **{m} kg** rover on {planet}?", W, [
        (m * 10, "That is its weight on Earth."),
        (m / g, "W = m × g."),
        (m * 10 / g, "Multiply the mass by g for that body directly."),
    ], "N", "weight = mass × g", ["W = m g", f"= {m} × {fmt(g)}", f"= **{fmt(W)} N**"],
        ["The mass is the same everywhere.", f"Use g for {planet}.", f"{m} × {fmt(g)}."])


@template("c3_identify_material", chapter=3, level=2, lo="3g")
def identify_material(rng):
    mats = [("aluminium", 2.7), ("iron", 7.9), ("copper", 8.9), ("lead", 11.3)]
    name, rho = rng.choice(mats)
    V = nice(rng, 10, 20, 30)
    m = rho * V
    table = md_table(["metal", "density / g/cm³"], [[n, fmt(r)] for n, r in mats])
    return calc_q(rng, f"A metal cube has a mass of **{fmt(m)} g** and a volume of **{V} cm³**. The table lists some densities.\n\n{table}\n\nWhat is the density of the cube (and so which metal is it)?", rho, [
        (V / m, "Density = mass ÷ volume."),
        (m / V / 10, "Check the division."),
        (m * V / 100, "Density = mass ÷ volume."),
    ], "g/cm³", "density = mass ÷ volume; match it to the table",
        [f"ρ = {fmt(m)} ÷ {V} = **{fmt(rho)} g/cm³**", f"so the metal is {name}"],
        ["Work out mass ÷ volume.", "Compare your answer with the table.", f"{fmt(m)} ÷ {V}."])


@template("c3_pressure_person", chapter=3, level=2, lo="3i")
def pressure_person(rng):
    m = nice(rng, 50, 60, 70, 80)
    A = nice(rng, 0.02, 0.04, 0.05)
    p = m * G / A
    return calc_q(rng, f"Fig. 1 shows a person of mass **{m} kg** standing on both feet, with a total contact area of **{fmt(A)} m²** (g = 10 N/kg). What pressure does the person exert on the floor?", p, [
        (m / A, "Use the WEIGHT (m × g) as the force, not the mass."),
        (m * G * A, "p = F ÷ A, not F × A."),
        (m * G / A / 2, "The area given is already for both feet."),
    ], "Pa", "pressure = weight ÷ area, weight = m g", [f"W = {m} × 10 = {m * G} N", f"p = {m * G} ÷ {fmt(A)}", f"= **{fmt(p)} Pa**"],
        ["The force on the floor is the person's weight.", "W = m g.", "p = W ÷ A."],
        figure=sketches.pressure_block(f"W = {m * G} N", f"area = {fmt(A)} m²"))


# ---------------------------------------------------------------- L3
@template("c3_density_convert", chapter=3, level=3, lo="3g")
def density_convert(rng):
    rho = nice(rng, 0.8, 1.2, 2.7, 7.9, 13.6)
    table = md_table(["liquid or solid", "density / g/cm³"], [["sample", fmt(rho)]])
    return calc_q(rng, f"The table gives the density of a substance.\n\n{table}\n\nWhat is its density in **kg/m³**?", rho * 1000, [
        (rho / 1000, "1 g/cm³ = 1000 kg/m³, so multiply."),
        (rho * 100, "1 m³ = 10⁶ cm³ and 1 kg = 1000 g: the factor is 1000, not 100."),
        (rho * 1e6, "Include the change from g to kg (÷ 1000) as well as cm³ to m³ (× 10⁶)."),
    ], "kg/m³", "1 g/cm³ = 1000 kg/m³", [f"{fmt(rho)} g/cm³ × 1000", f"= **{fmt(rho * 1000)} kg/m³**"],
        ["Convert g to kg and cm³ to m³ together.", "1 g/cm³ = (10⁻³ kg) ÷ (10⁻⁶ m³) = 1000 kg/m³.", f"{fmt(rho)} × 1000."])


@template("c3_tank_liquid_mass", chapter=3, level=3, lo="3g")
def tank_liquid_mass(rng):
    rho = nice(rng, 800, 1000, 1200)
    a, b, c = nice(rng, 0.5, 1.0, 2.0), nice(rng, 0.4, 0.5, 1.0), nice(rng, 0.2, 0.5, 0.8)
    V = a * b * c
    m = rho * V
    return calc_q(rng, f"Fig. 1 shows a tank filled with a liquid of density **{rho} kg/m³**. What is the mass of the liquid?", m, [
        (V, "That is the volume in m³; multiply by the density."),
        (rho / V, "m = ρ × V."),
        (rho * (a + b + c), "Volume = length × breadth × height, not their sum."),
    ], "kg", "mass = density × volume (V = l × b × h)", [f"V = {fmt(a)} × {fmt(b)} × {fmt(c)} = {fmt(V)} m³", f"m = {rho} × {fmt(V)}", f"= **{fmt(m)} kg**"],
        ["Find the volume of the tank first.", "Then use m = ρ V.", "Keep everything in kg and m."],
        figure=figs.labelled_block(a, b, c, "m"))


@template("c3_pressure_from_mass", chapter=3, level=3, lo="3i")
def pressure_from_mass(rng):
    m = nice(rng, 20, 40, 50, 80)
    A_cm2 = nice(rng, 200, 400, 500, 1000)
    p = m * G / (A_cm2 / 1e4)
    return calc_q(rng, f"Fig. 1 shows a box of mass **{m} kg** resting on a floor. The area of its base is **{A_cm2} cm²** (g = 10 N/kg). What pressure does it exert?", p, [
        (m * G / A_cm2, "Convert the area to m² first (÷ 10 000)."),
        (m / (A_cm2 / 1e4), "Use the weight (m × g), not the mass."),
        (m * G / (A_cm2 / 100), "1 m² = 10 000 cm², so divide by 10 000, not 100."),
    ], "Pa", "p = m g ÷ A with A in m²", [f"W = {m} × 10 = {m * G} N", f"A = {A_cm2} ÷ 10 000 = {fmt(A_cm2 / 1e4)} m²", f"p = **{fmt(p)} Pa**"],
        ["Find the weight.", "Convert cm² to m².", "p = W ÷ A."],
        figure=sketches.pressure_block(f"{m} kg", f"base = {A_cm2} cm²"))


@template("c3_weight_difference_moon", chapter=3, level=3, lo="3f")
def weight_difference_moon(rng):
    m = nice(rng, 10, 20, 50, 75, 90)
    diff = m * (10 - 1.6)
    return calc_q(rng, f"Fig. 1 compares the Earth (g = 10 N/kg) and the Moon (g = 1.6 N/kg). By how much does the weight of a **{m} kg** astronaut decrease when she goes from the Earth to the Moon?", diff, [
        (m * 1.6, "That is her weight on the Moon, not the decrease."),
        (m * 10, "That is her weight on Earth."),
        (0, "Her mass is unchanged, but her weight changes."),
    ], "N", "decrease = m × (g_Earth − g_Moon)", [f"Earth: {m} × 10 = {m * 10} N; Moon: {m} × 1.6 = {fmt(m * 1.6)} N", f"decrease = **{fmt(diff)} N**"],
        ["Work out her weight in each place.", "W = m g with the right g.", "Subtract."],
        figure=sketches.two_bodies_sketch(["g = 10 N/kg"], ["g = 1.6 N/kg"]))


# ---------------------------------------------------------------- L4
@template("c3_least_pressure_face", chapter=3, level=4, lo="3i")
def least_pressure_face(rng):
    a, b, c = nice(rng, 20, 25), nice(rng, 10, 12), nice(rng, 5, 6)
    W = nice(rng, 30, 40, 60)
    A = a * b / 1e4
    p = W / A
    return calc_q(rng, f"Fig. 1 shows a block of weight **{W} N** with its dimensions in cm. What is the **least** pressure it can exert when resting on a flat floor?", p, [
        (W / (b * c / 1e4), "That is the GREATEST pressure (smallest face). Least pressure uses the LARGEST face."),
        (W / (a * b), "Convert the area from cm² to m²."),
        (W / (a * c / 1e4), "Use the largest face, which is a × b."),
    ], "Pa", "least pressure = weight ÷ largest area", [f"largest face = {a} cm × {b} cm = {a * b} cm² = {fmt(A)} m²", f"p = {W} ÷ {fmt(A)}", f"= **{fmt(p)} Pa**"],
        ["For the same weight, a bigger area gives a smaller pressure.", "Find the largest face.", "Convert cm² to m², then divide."],
        figure=figs.labelled_block(a, b, c, "cm"))


@template("c3_block_weight_from_dims", chapter=3, level=4, lo="3g")
def block_weight_from_dims(rng):
    rho = nice(rng, 2.7, 7.8, 8.9)
    a, b, c = nice(rng, 5, 10), nice(rng, 4, 5), nice(rng, 2, 4)
    m_kg = rho * a * b * c / 1000
    W = m_kg * G
    return calc_q(rng, f"Fig. 1 shows a metal block of density **{fmt(rho)} g/cm³**. Taking g = 10 N/kg, what is its weight?", W, [
        (m_kg, "That is the mass in kg. Weight = m × g."),
        (rho * a * b * c * G, "Convert the mass from g to kg before multiplying by g."),
        (W / 10, "Weight = m × g, with g = 10 N/kg."),
    ], "N", "V = l b h; m = ρ V; W = m g", [f"V = {a} × {b} × {c} = {a * b * c} cm³", f"m = {fmt(rho)} × {a * b * c} = {fmt(rho * a * b * c)} g = {fmt(m_kg)} kg", f"W = {fmt(m_kg)} × 10 = **{fmt(W)} N**"],
        ["Volume first, then mass.", "Convert g to kg.", "Weight = m g."],
        figure=figs.labelled_block(a, b, c, "cm"))


@template("c3_overflow_can_density", chapter=3, level=4, lo="3g")
def overflow_can_density(rng):
    V = nice(rng, 20, 25, 40, 50)
    rho = nice(rng, 2.4, 2.8, 3.0, 5.6)
    m = rho * V
    table = md_table(["measurement", "value"], [["mass of stone", f"{fmt(m)} g"], ["water collected from the overflow can", f"{V} cm³"]])
    return calc_q(rng, f"A stone is lowered into a full overflow can and the displaced water is collected.\n\n{table}\n\nWhat is the density of the stone?", rho, [
        (V / m, "Density = mass ÷ volume."),
        (m / V * 1000, "The answer is in g/cm³; no conversion is needed."),
        (m - V, "Divide mass by volume."),
    ], "g/cm³", "volume of stone = volume of water displaced; density = mass ÷ volume", [f"V = {V} cm³", f"ρ = {fmt(m)} ÷ {V}", f"= **{fmt(rho)} g/cm³**"],
        ["The water that overflows has the same volume as the stone.", "density = mass ÷ volume.", f"{fmt(m)} ÷ {V}."])


@template("c3_min_area_for_pressure", chapter=3, level=4, lo="3i")
def min_area_for_pressure(rng):
    m = nice(rng, 2000, 5000, 8000, 12000)
    pmax = nice(rng, 50000, 100000, 200000)
    A = m * G / pmax
    return calc_q(rng, f"Fig. 1 shows a machine of mass **{m} kg** to be placed on soft ground that can withstand a pressure of at most **{pmax} Pa** (g = 10 N/kg). What is the smallest total area of the supports?", A, [
        (m / pmax, "Use the weight (m × g) as the force."),
        (pmax / (m * G), "A = F ÷ p."),
        (m * G * pmax, "A = F ÷ p, not F × p."),
    ], "m²", "A = W ÷ p_max", [f"W = {m} × 10 = {m * G} N", f"A = {m * G} ÷ {pmax}", f"= **{fmt(A)} m²**"],
        ["The pressure must not exceed the limit.", "A smaller area gives a larger pressure, so find the area at which p equals the limit.", "A = W ÷ p."],
        figure=sketches.pressure_block(f"{m} kg", "area = ?"))


# ---------------------------------------------------------------- L5
@template("c3_alloy_density", chapter=3, level=5, lo="3g")
def alloy_density(rng):
    (n1, r1), (n2, r2) = rng.choice([(("copper", 8.9), ("zinc", 7.1)), (("gold", 19.3), ("silver", 10.5)), (("lead", 11.3), ("tin", 7.3))])
    V1, V2 = nice(rng, 10, 20, 30), nice(rng, 10, 20)
    m = r1 * V1 + r2 * V2
    rho = m / (V1 + V2)
    table = md_table(["metal", "volume / cm³", "density / g/cm³"], [[n1, V1, fmt(r1)], [n2, V2, fmt(r2)]])
    return calc_q(rng, f"Two metals are melted together to make an alloy, with no change in total volume.\n\n{table}\n\nWhat is the density of the alloy?", rho, [
        ((r1 + r2) / 2, "Do not average the densities; use total mass ÷ total volume."),
        (m, "That is the total mass in g; divide by the total volume."),
        (m / V1, "Divide by the TOTAL volume."),
    ], "g/cm³", "density = total mass ÷ total volume",
        [f"m = {fmt(r1)} × {V1} + {fmt(r2)} × {V2} = {fmt(m)} g", f"V = {V1 + V2} cm³", f"ρ = **{fmt(rho)} g/cm³**"],
        ["Find the mass of each metal (ρ × V).", "Add the masses and add the volumes.", "Divide total mass by total volume."])


@template("c3_spring_balance_moon", chapter=3, level=5, lo="3f")
def spring_balance_moon(rng):
    W_earth = nice(rng, 30, 50, 80, 120, 200)
    m = W_earth / 10
    W_moon = m * 1.6
    return calc_q(rng, f"Fig. 1 shows a spring balance reading **{W_earth} N** for a rock on Earth (g = 10 N/kg). What would it read for the same rock on the Moon, where g = 1.6 N/kg?", W_moon, [
        (W_earth, "The MASS is unchanged, but a spring balance reads weight, which changes."),
        (m, "That is the mass in kg; the balance reads newtons."),
        (W_earth / 1.6, "Find the mass first (W ÷ 10), then multiply by 1.6."),
    ], "N", "m = W_Earth ÷ g_Earth; W_Moon = m × g_Moon", [f"m = {W_earth} ÷ 10 = {fmt(m)} kg", f"W on Moon = {fmt(m)} × 1.6", f"= **{fmt(W_moon)} N**"],
        ["A spring balance measures weight.", "Find the mass, which does not change.", "Multiply by the Moon's g."],
        figure=sketches.spring_balance(f"{W_earth} N (Earth)", "rock"))


@template("c3_table_legs_pressure", chapter=3, level=5, lo="3i")
def table_legs_pressure(rng):
    m = nice(rng, 20, 30, 40, 60)
    a_cm2 = nice(rng, 4, 5, 8, 10)
    p = m * G / (4 * a_cm2 / 1e4)
    return calc_q(rng, f"Fig. 1 shows a table of mass **{m} kg** standing on **4 legs**, each with an end area of **{a_cm2} cm²** (g = 10 N/kg). What pressure does each leg exert on the floor?", p, [
        (m * G / (a_cm2 / 1e4), "The weight is shared by FOUR legs: use the total area of all four."),
        (m * G / (4 * a_cm2), "Convert cm² to m² (÷ 10 000)."),
        (m / (4 * a_cm2 / 1e4), "Use the weight (m × g) as the force."),
    ], "Pa", "p = W ÷ total area of the legs", [f"W = {m} × 10 = {m * G} N", f"total area = 4 × {a_cm2} = {4 * a_cm2} cm² = {fmt(4 * a_cm2 / 1e4)} m²", f"p = **{fmt(p)} Pa**"],
        ["Find the weight of the table.", "The weight is spread over four legs.", "Convert the total area to m²."],
        figure=sketches.pressure_block(f"{m * G} N", f"4 legs × {a_cm2} cm²"))


@template("c3_tank_water_weight", chapter=3, level=5, lo="3g")
def tank_water_weight(rng):
    a, b, c = nice(rng, 50, 80, 100), nice(rng, 40, 50), nice(rng, 30, 40)
    V_m3 = a * b * c / 1e6
    W = V_m3 * 1000 * G
    return calc_q(rng, f"Fig. 1 shows an aquarium with internal dimensions in cm, filled with water of density **1000 kg/m³** (g = 10 N/kg). What is the weight of the water?", W, [
        (a * b * c * 1000 * G, "Convert cm³ to m³ (÷ 10⁶) before using 1000 kg/m³."),
        (V_m3 * 1000, "That is the mass in kg; weight = m × g."),
        (a * b * c / 1000 * G, "1 m³ = 10⁶ cm³, not 1000 cm³."),
    ], "N", "V in m³; m = ρ V; W = m g", [f"V = {a} × {b} × {c} = {a * b * c} cm³ = {fmt(V_m3)} m³", f"m = 1000 × {fmt(V_m3)} = {fmt(V_m3 * 1000)} kg", f"W = **{fmt(W)} N**"],
        ["Find the volume and convert it to m³.", "Mass = density × volume.", "Weight = mass × g."],
        figure=figs.labelled_block(a, b, c, "cm"))
