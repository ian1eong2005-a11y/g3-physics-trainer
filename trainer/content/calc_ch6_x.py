"""Chapter 6 Energy: extra calculation templates (Ek, Ep, work, power, conservation)."""
import math

from .. import sketches
from .base import calc_q, fmt, md_table, nice, template

G = 10


# ---------------------------------------------------------------- L1
@template("c6_ke_ball_grams", chapter=6, level=1, lo="6b")
def ke_ball_grams(rng):
    m_g = nice(rng, 200, 400, 500, 600)
    v = nice(rng, 5, 10, 12, 20)
    E = 0.5 * m_g / 1000 * v * v
    return calc_q(rng, f"Fig. 1 shows a ball of mass **{m_g} g** moving at **{v} m/s**. What is its kinetic energy?", E, [
        (0.5 * m_g * v * v, "Convert the mass to kg (÷ 1000) first."),
        (m_g / 1000 * v * v, "Ek = ½ m v²: remember the ½."),
        (0.5 * m_g / 1000 * v, "Square the speed: Ek = ½ m v²."),
    ], "J", "Ek = ½ m v² (m in kg)", [f"m = {m_g} g = {fmt(m_g / 1000)} kg", f"Ek = ½ × {fmt(m_g / 1000)} × {v}²", f"= **{fmt(E)} J**"],
        ["Mass must be in kg.", "Ek = ½ m v².", f"½ × {fmt(m_g / 1000)} × {v * v}."],
        figure=sketches.motion_sketch("", "", f"{v} m/s", body="box", body_label=f"{m_g} g"))


@template("c6_gpe_stairs", chapter=6, level=1, lo="6b")
def gpe_stairs(rng):
    m = nice(rng, 40, 50, 60, 70)
    h = nice(rng, 3, 4, 5, 6)
    E = m * G * h
    table = md_table(["mass of student / kg", "height climbed / m"], [[m, h]])
    return calc_q(rng, "A student climbs the stairs to the next floor (g = 10 N/kg)." + chr(10) + chr(10) + table + chr(10) + chr(10) + "What is her gain in gravitational potential energy?", E, [
        (m * h, "Ep = m g h: include g."),
        (m * G / h, "Multiply by the height."),
        (0.5 * m * G * h, "There is no ½ in Ep = m g h."),
    ], "J", "Ep = m g h", ["Ep = m g h", f"= {m} × 10 × {h}", f"= **{fmt(E)} J**"],
        ["Which formula gives gravitational potential energy?", "Ep = m g h.", f"{m} × 10 × {h}."])


@template("c6_work_lifting", chapter=6, level=1, lo="6d")
def work_lifting(rng):
    F = nice(rng, 50, 80, 120, 200)
    h = nice(rng, 1.5, 2, 3, 4)
    W = F * h
    return calc_q(rng, f"Fig. 1 shows a box lifted vertically through **{fmt(h)} m** by a steady upward force of **{F} N**. How much work is done by the force?", W, [
        (F / h, "Work = force × distance moved, not ÷."),
        (F * h * G, "The force is already given in newtons; do not multiply by g."),
        (F + h, "Multiply force by distance."),
    ], "J", "work done = force × distance moved in the direction of the force", ["W = F × d", f"= {F} × {fmt(h)}", f"= **{fmt(W)} J**"],
        ["Work = force × distance in the direction of the force.", "The force is upward and the box moves upward.", f"{F} × {fmt(h)}."],
        figure=sketches.lift_sketch(f"{fmt(h)} m", body_label=f"{F} N"))


@template("c6_power_kj", chapter=6, level=1, lo="6e")
def power_kj(rng):
    E_kj = nice(rng, 12, 18, 30, 60, 90)
    t = nice(rng, 10, 20, 30, 60)
    P = E_kj * 1000 / t
    table = md_table(["energy transferred / kJ", "time / s"], [[E_kj, t]])
    return calc_q(rng, f"The table gives the energy transferred by an electric motor.\n\n{table}\n\nWhat is its power in watts?", P, [
        (E_kj / t, "Convert kJ to J (× 1000) to get the power in W."),
        (E_kj * 1000 * t, "Power = energy ÷ time."),
        (t / (E_kj * 1000), "P = E ÷ t."),
    ], "W", "P = E ÷ t (E in J, t in s)", [f"E = {E_kj} kJ = {E_kj * 1000} J", f"P = {E_kj * 1000} ÷ {t}", f"= **{fmt(P)} W**"],
        ["Power is energy per unit time.", "Change kJ to J.", "Divide by the time."])


# ---------------------------------------------------------------- L2
@template("c6_energy_from_power", chapter=6, level=2, lo="6e")
def energy_from_power(rng):
    P = nice(rng, 60, 100, 500, 1200, 2000)
    t_min = nice(rng, 2, 5, 10)
    E = P * t_min * 60
    return calc_q(rng, f"Fig. 1 shows a motor of power **{P} W** running for **{t_min} minutes**. How much energy does it transfer?", E, [
        (P * t_min, "Convert minutes to seconds (× 60)."),
        (P / (t_min * 60), "E = P × t."),
        (P * t_min * 3600, "1 minute = 60 s, not 3600 s."),
    ], "J", "E = P × t (t in s)", [f"t = {t_min} × 60 = {t_min * 60} s", f"E = {P} × {t_min * 60}", f"= **{fmt(E)} J**"],
        ["Rearrange P = E ÷ t.", "Convert the time to seconds.", "Multiply."],
        figure=sketches.lift_sketch("h", body_label="load", extra=f"P = {P} W"))


@template("c6_time_from_power", chapter=6, level=2, lo="6e")
def time_from_power(rng):
    P = nice(rng, 500, 800, 1000, 2000)
    t = nice(rng, 30, 60, 90, 120)
    E = P * t
    table = md_table(["power of heater / W", "energy needed / J"], [[P, E]])
    return calc_q(rng, f"A heater must supply a fixed amount of energy.\n\n{table}\n\nHow long does this take?", t, [
        (E * P, "t = E ÷ P."),
        (P / E, "t = E ÷ P, not P ÷ E."),
        (t / 60, "That is in minutes; the answer is in seconds."),
    ], "s", "t = E ÷ P", ["t = E ÷ P", f"= {E} ÷ {P}", f"= **{fmt(t)} s**"],
        ["P = E ÷ t.", "Rearrange for t.", f"{E} ÷ {P}."])


@template("c6_mass_from_gpe", chapter=6, level=2, lo="6b")
def mass_from_gpe(rng):
    m = nice(rng, 2, 5, 8, 12, 20)
    h = nice(rng, 2, 3, 5, 10)
    E = m * G * h
    return calc_q(rng, f"Fig. 1 shows a crate lifted through **{h} m**. It gains **{E} J** of gravitational potential energy (g = 10 N/kg). What is its mass?", m, [
        (E / h, "Divide by g as well: m = Ep ÷ (g h)."),
        (E * G * h, "m = Ep ÷ (g h)."),
        (E / G, "Divide by the height as well."),
    ], "kg", "m = Ep ÷ (g h)", ["m = Ep ÷ (g h)", f"= {E} ÷ (10 × {h})", f"= **{fmt(m)} kg**"],
        ["Ep = m g h.", "Rearrange for m.", f"{E} ÷ {10 * h}."],
        figure=sketches.lift_sketch(f"{h} m", body_label="m = ?"))


@template("c6_height_from_gpe", chapter=6, level=2, lo="6b")
def height_from_gpe(rng):
    m = nice(rng, 0.5, 2, 4, 50)
    h = nice(rng, 2, 4, 6, 8, 12)
    E = m * G * h
    return calc_q(rng, f"Fig. 1 shows an object of mass **{fmt(m)} kg** lifted until it has gained **{fmt(E)} J** of gravitational potential energy (g = 10 N/kg). Through what height was it lifted?", h, [
        (E / m, "Divide by g as well: h = Ep ÷ (m g)."),
        (E * m * G, "h = Ep ÷ (m g)."),
        (E / G, "Divide by the mass as well."),
    ], "m", "h = Ep ÷ (m g)", ["h = Ep ÷ (m g)", f"= {fmt(E)} ÷ ({fmt(m)} × 10)", f"= **{fmt(h)} m**"],
        ["Ep = m g h.", "Rearrange for h.", f"{fmt(E)} ÷ {fmt(m * G)}."],
        figure=sketches.lift_sketch("h = ?", body_label=f"{fmt(m)} kg"))


# ---------------------------------------------------------------- L3
@template("c6_speed_from_ke", chapter=6, level=3, lo="6b")
def speed_from_ke(rng):
    m = nice(rng, 2, 4, 5, 8, 10)
    v = nice(rng, 3, 4, 5, 6, 10)
    E = 0.5 * m * v * v
    return calc_q(rng, f"Fig. 1 shows a trolley of mass **{m} kg** with **{fmt(E)} J** of kinetic energy. What is its speed?", v, [
        (2 * E / m, "That is v²; take the square root."),
        (E / m, "v² = 2 Ek ÷ m, then square-root."),
        (math.sqrt(E / m), "Remember the factor 2: v = √(2 Ek ÷ m)."),
    ], "m/s", "v = √(2 Ek ÷ m)", [f"v² = 2 × {fmt(E)} ÷ {m} = {fmt(v * v)}", f"v = √{fmt(v * v)}", f"= **{fmt(v)} m/s**"],
        ["Ek = ½ m v².", "Rearrange for v²: v² = 2 Ek ÷ m.", "Then take the square root."],
        figure=sketches.motion_sketch("", "", "v = ?", body="box", body_label=f"{m} kg"))


@template("c6_work_against_friction", chapter=6, level=3, lo="6d")
def work_against_friction(rng):
    f = nice(rng, 20, 30, 40, 50)
    d = nice(rng, 5, 8, 10, 15)
    W = f * d
    return calc_q(rng, f"Fig. 1 shows a box pushed at constant speed for **{d} m** across a floor. The friction on the box is **{f} N**. How much work is done against friction?", W, [
        (f / d, "Work = force × distance."),
        (f * d / 2, "No ½: W = F × d."),
        (f + d, "Multiply force by distance."),
    ], "J", "work done against friction = friction × distance", ["W = f × d", f"= {f} × {d}", f"= **{fmt(W)} J**"],
        ["At constant speed, the push equals the friction.", "Work = force × distance.", f"{f} × {d}."],
        figure=sketches.push_sketch(f"{f} N", f"{d} m", friction_label=f"friction {f} N"))


@template("c6_ke_change", chapter=6, level=3, lo="6b")
def ke_change(rng):
    m = nice(rng, 800, 1000, 1200)
    u, v = rng.choice([(10, 20), (5, 15), (20, 30), (12, 18)])
    dE = 0.5 * m * (v * v - u * u)
    return calc_q(rng, f"Fig. 1 shows a car of mass **{m} kg** that speeds up from **{u} m/s** to **{v} m/s**. By how much does its kinetic energy increase?", dE, [
        (0.5 * m * (v - u) ** 2, "Work out each kinetic energy separately; (v − u)² is not v² − u²."),
        (0.5 * m * v * v, "That is the final Ek; subtract the initial Ek."),
        (m * (v * v - u * u), "Remember the ½ in Ek = ½ m v²."),
    ], "J", "ΔEk = ½ m v² − ½ m u²", [f"final Ek = ½ × {m} × {v}² = {fmt(0.5 * m * v * v)} J", f"initial Ek = ½ × {m} × {u}² = {fmt(0.5 * m * u * u)} J", f"increase = **{fmt(dE)} J**"],
        ["Find the kinetic energy at each speed.", "Ek = ½ m v².", "Subtract."],
        figure=sketches.motion_sketch(f"{u} m/s", f"{v} m/s", f"{m} kg", body="car"))


@template("c6_pendulum_speed", chapter=6, level=3, lo="6c")
def pendulum_speed(rng):
    h = nice(rng, 0.05, 0.2, 0.45, 0.8)
    v = math.sqrt(2 * G * h)
    return calc_q(rng, f"Fig. 1 shows a pendulum bob released from rest at a point **{fmt(h * 100)} cm** higher than its lowest point. Ignoring air resistance (g = 10 N/kg), what is its speed at the lowest point?", v, [
        (2 * G * h, "That is v²; take the square root."),
        (math.sqrt(G * h), "m g h = ½ m v², so v = √(2 g h)."),
        (math.sqrt(2 * G * h * 100), "Convert the height to metres first."),
    ], "m/s", "m g h = ½ m v², so v = √(2 g h)", [f"h = {fmt(h)} m", f"v = √(2 × 10 × {fmt(h)}) = √{fmt(2 * G * h)}", f"= **{fmt(v)} m/s**"],
        ["Energy is conserved: Ep lost = Ek gained.", "The mass cancels.", "v = √(2 g h), with h in metres."],
        figure=sketches.pendulum_sketch(f"released {fmt(h * 100)} cm above lowest point"))


# ---------------------------------------------------------------- L4
@template("c6_bounce_energy_lost", chapter=6, level=4, lo="6c")
def bounce_energy_lost(rng):
    m = nice(rng, 0.1, 0.2, 0.5)
    h1 = nice(rng, 2.0, 2.5, 3.0)
    h2 = nice(rng, 1.2, 1.5, 1.8)
    lost = m * G * (h1 - h2)
    return calc_q(rng, f"A ball of mass **{fmt(m)} kg** is dropped from **{fmt(h1)} m** and bounces back up to **{fmt(h2)} m** (g = 10 N/kg). The table summarises this. How much energy is transferred to other stores during the bounce?\n\n" + md_table(["drop height / m", "bounce height / m"], [[fmt(h1), fmt(h2)]]), lost, [
        (m * G * h2, "That is the Ep at the top of the bounce; find the DIFFERENCE."),
        (m * G * h1, "That is the starting Ep."),
        (m * (h1 - h2), "Include g: Ep = m g h."),
    ], "J", "energy lost = m g (h₁ − h₂)", [f"Ep at start = {fmt(m)} × 10 × {fmt(h1)} = {fmt(m * G * h1)} J", f"Ep after bounce = {fmt(m * G * h2)} J", f"lost = **{fmt(lost)} J**"],
        ["Compare the gravitational potential energy at the two heights.", "The difference went to other stores (internal, sound).", "m g (h₁ − h₂)."])


@template("c6_average_air_resistance", chapter=6, level=4, lo="6c")
def average_air_resistance(rng):
    m = nice(rng, 0.5, 1, 2)
    h = nice(rng, 20, 40, 45)
    v = nice(rng, 15, 20, 25)
    if 0.5 * v * v >= G * h:
        v = 15
    lost = m * G * h - 0.5 * m * v * v
    R = lost / h
    return calc_q(rng, f"An object of mass **{fmt(m)} kg** falls from rest through **{h} m** and reaches **{v} m/s** (g = 10 N/kg). The table summarises the data. What is the average air resistance?\n\n" + md_table(["mass / kg", "height fallen / m", "final speed / m/s"], [[fmt(m), h, v]]), R, [
        (lost, "That is the energy lost; divide by the distance to get the average force."),
        (m * G - R * 2 if m * G - R * 2 > 0 else m * G * 2, "Work done against air resistance = energy lost = R × distance."),
        (m * G, "That is the weight, not the air resistance."),
    ], "N", "energy lost = Ep − Ek = R × distance", [f"Ep lost = {fmt(m * G * h)} J; Ek gained = {fmt(0.5 * m * v * v)} J", f"energy to air resistance = {fmt(lost)} J", f"R = {fmt(lost)} ÷ {h} = **{fmt(R)} N**"],
        ["Without air resistance, all the Ep would become Ek.", "The missing energy is work done against air resistance.", "Work = force × distance, so R = energy ÷ distance."])


@template("c6_pump_power", chapter=6, level=4, lo="6e")
def pump_power(rng):
    m = nice(rng, 20, 50, 60, 100)
    h = nice(rng, 5, 8, 10, 12)
    t = nice(rng, 10, 20, 30)
    P = m * G * h / t
    return calc_q(rng, f"Fig. 1 shows a pump that raises **{m} kg** of water through a height of **{h} m** in **{t} s** (g = 10 N/kg). What useful power does it deliver?", P, [
        (m * G * h, "That is the energy; divide by the time."),
        (m * h / t, "Use the weight m g, not the mass."),
        (m * G * h * t, "P = E ÷ t."),
    ], "W", "P = m g h ÷ t", [f"Ep gained = {m} × 10 × {h} = {m * G * h} J", f"P = {m * G * h} ÷ {t}", f"= **{fmt(P)} W**"],
        ["Find the energy given to the water.", "Ep = m g h.", "Power = energy ÷ time."],
        figure=sketches.lift_sketch(f"{h} m", body_label=f"{m} kg water"))


@template("c6_speed_from_work", chapter=6, level=4, lo="6d")
def speed_from_work(rng):
    m = nice(rng, 2, 4, 5, 8)
    F = nice(rng, 10, 20, 25, 40)
    d = nice(rng, 2, 4, 5, 10)
    W = F * d
    v = math.sqrt(2 * W / m)
    return calc_q(rng, f"Fig. 1 shows a trolley of mass **{m} kg** at rest on a smooth track. A constant force of **{F} N** pushes it for **{d} m**. What is its final speed?", v, [
        (2 * W / m, "That is v²; take the square root."),
        (W / m, "Ek = W gives ½ m v² = F d, so v = √(2 F d ÷ m)."),
        (math.sqrt(W / m), "Do not forget the factor 2."),
    ], "m/s", "work done = gain in Ek: F d = ½ m v²", [f"W = {F} × {d} = {W} J", f"½ × {m} × v² = {W}", f"v = **{fmt(v)} m/s**"],
        ["The work done on the trolley becomes kinetic energy.", "W = F × d.", "Set F d = ½ m v² and solve for v."],
        figure=sketches.push_sketch(f"{F} N", f"{d} m", body_label=f"{m} kg"))


# ---------------------------------------------------------------- L5
@template("c6_crane_time", chapter=6, level=5, lo="6e")
def crane_time(rng):
    m = nice(rng, 200, 500, 800, 1000)
    h = nice(rng, 10, 15, 20, 30)
    P = nice(rng, 5000, 10000, 20000)
    t = m * G * h / P
    return calc_q(rng, f"Fig. 1 shows a crane with a useful power output of **{P} W** lifting a load of mass **{m} kg** through **{h} m** at constant speed (g = 10 N/kg). How long does the lift take?", t, [
        (P / (m * G * h), "t = E ÷ P."),
        (m * h / P, "Use the weight (m g) in the energy."),
        (m * G * h / P / 60, "The answer is already in seconds."),
    ], "s", "t = m g h ÷ P", [f"E = {m} × 10 × {h} = {m * G * h} J", f"t = {m * G * h} ÷ {P}", f"= **{fmt(t)} s**"],
        ["Find the energy needed.", "Power = energy ÷ time.", "Rearrange for time."],
        figure=sketches.lift_sketch(f"{h} m", body_label=f"{m} kg", extra=f"P = {P} W"))


@template("c6_skier_friction_speed", chapter=6, level=5, lo="6c")
def skier_friction_speed(rng):
    m = nice(rng, 50, 60, 80)
    h = nice(rng, 20, 30, 45)
    lost = nice(rng, 2000, 3000, 4000)
    Ek = m * G * h - lost
    if Ek <= 0:
        lost = m * G * h // 4
        Ek = m * G * h - lost
    v = math.sqrt(2 * Ek / m)
    return calc_q(rng, f"Fig. 1 shows a skier of mass **{m} kg** who starts from rest at the top of a slope of vertical height **{h} m**. **{lost} J** of energy is transferred by friction on the way down (g = 10 N/kg). What is her speed at the bottom?", v, [
        (math.sqrt(2 * G * h), "Subtract the energy transferred by friction first."),
        (math.sqrt(2 * (m * G * h + lost) / m), "Friction REMOVES energy from the skier."),
        (2 * Ek / m, "That is v²; take the square root."),
    ], "m/s", "Ek at bottom = m g h − energy lost; v = √(2 Ek ÷ m)", [f"Ep = {m} × 10 × {h} = {m * G * h} J", f"Ek = {m * G * h} − {lost} = {Ek} J", f"v = √(2 × {Ek} ÷ {m}) = **{fmt(v)} m/s**"],
        ["Start with the Ep at the top.", "Subtract the energy lost to friction to find the Ek at the bottom.", "Then find v from Ek = ½ m v²."],
        figure=sketches.slope_sketch(f"{h} m", top_label="start", bottom_label="v = ?"))


@template("c6_stairs_steps_power", chapter=6, level=5, lo="6e")
def stairs_steps_power(rng):
    m = nice(rng, 50, 60, 70)
    n = nice(rng, 20, 25, 30, 40)
    step_cm = nice(rng, 15, 18, 20)
    t = nice(rng, 6, 8, 10, 12)
    h = n * step_cm / 100
    P = m * G * h / t
    table = md_table(["mass / kg", "number of steps", "height of each step / cm", "time / s"], [[m, n, step_cm, t]])
    return calc_q(rng, f"A student runs up a staircase.\n\n{table}\n\nTaking g = 10 N/kg, what is her average useful power?", P, [
        (m * G * n * step_cm / t, "Convert the step height to metres (÷ 100)."),
        (m * G * h, "That is the energy; divide by the time."),
        (m * h / t, "Use the weight (m g)."),
    ], "W", "h = number of steps × step height; P = m g h ÷ t", [f"h = {n} × {fmt(step_cm / 100)} = {fmt(h)} m", f"E = {m} × 10 × {fmt(h)} = {fmt(m * G * h)} J", f"P = {fmt(m * G * h)} ÷ {t} = **{fmt(P)} W**"],
        ["Find the total height climbed in metres.", "Find the gain in Ep.", "Divide by the time."])


@template("c6_bounce_percentage", chapter=6, level=5, lo="6c")
def bounce_percentage(rng):
    h1 = nice(rng, 2.0, 2.5, 4.0, 5.0)
    frac = nice(rng, 0.6, 0.7, 0.75, 0.8)
    h2 = h1 * frac
    pct = (1 - frac) * 100
    table = md_table(["drop height / m", "bounce height / m"], [[fmt(h1), fmt(h2)]])
    return calc_q(rng, f"A ball is dropped and its bounce is measured.\n\n{table}\n\nWhat percentage of its gravitational potential energy is transferred to other stores during the bounce?", pct, [
        (frac * 100, "That is the percentage KEPT; the question asks for the percentage transferred away."),
        ((h1 - h2), "That is the loss in height, not a percentage."),
        ((h1 - h2) / h2 * 100, "Divide by the STARTING height (energy at the start)."),
    ], "%", "Ep ∝ h, so % lost = (h₁ − h₂) ÷ h₁ × 100", [f"loss in height = {fmt(h1)} − {fmt(h2)} = {fmt(h1 - h2)} m", f"% lost = {fmt(h1 - h2)} ÷ {fmt(h1)} × 100", f"= **{fmt(pct)} %**"],
        ["Ep = m g h, so Ep is proportional to height (m and g are fixed).", "Compare the heights.", "Express the loss as a percentage of the starting value."])
