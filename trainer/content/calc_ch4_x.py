"""Chapter 4 Dynamics: extra calculation templates (F = m a with resultant forces, lifts, rockets, braking)."""
from .. import figs, sketches
from .base import calc_q, fmt, md_table, nice, template

G = 10


def _vt(pts, ymax):
    xmax = max(p[0] for p in pts)
    xstep = next(s for s in (1, 2, 5, 10) if xmax / s <= 8)
    ystep = next(s for s in (1, 2, 5, 10, 20) if ymax / s <= 6)
    return figs.graph(pts, -(-xmax // xstep) * xstep, -(-ymax // ystep) * ystep, xstep, ystep)


# ---------------------------------------------------------------- L3
@template("c4_two_forces_same_way", chapter=4, level=3, lo="4c")
def two_forces_same_way(rng):
    F1, F2 = nice(rng, 20, 30, 40), nice(rng, 10, 15, 20)
    m = nice(rng, 5, 10, 25)
    a = (F1 + F2) / m
    table = md_table(["force on the cart", "size / N", "direction"], [["push from person A", F1, "east"], ["push from person B", F2, "east"]])
    return calc_q(rng, f"Two people push a cart of mass **{m} kg**. Friction is negligible.\n\n{table}\n\nWhat is the acceleration of the cart?", a, [
        ((F1 - F2) / m, "Both forces act in the SAME direction, so add them."),
        (F1 / m, "Include both forces in the resultant."),
        ((F1 + F2) * m, "a = F ÷ m, not F × m."),
    ], "m/s²", "resultant force = F₁ + F₂; a = F ÷ m", [f"F = {F1} + {F2} = {F1 + F2} N", f"a = {F1 + F2} ÷ {m}", f"= **{fmt(a)} m/s²**"],
        ["Find the resultant force first.", "Forces in the same direction add.", "Then a = F ÷ m."])


@template("c4_force_kmh_change", chapter=4, level=3, lo="4c")
def force_kmh_change(rng):
    m = nice(rng, 800, 1000, 1200)
    vk = nice(rng, 36, 54, 72)
    t = nice(rng, 5, 6, 10)
    F = m * vk / 3.6 / t
    return calc_q(rng, f"Fig. 1 shows a car of mass **{m} kg** that speeds up uniformly from rest to **{vk} km/h** in **{t} s**. What is the resultant force on it?", F, [
        (m * vk / t, "Convert km/h to m/s (÷ 3.6) before finding the acceleration."),
        (m * vk * 3.6 / t, "To convert km/h to m/s, divide by 3.6."),
        (vk / 3.6 / t, "That is the acceleration; multiply by the mass."),
    ], "N", "a = Δv ÷ t (in m/s); F = m a", [f"{vk} km/h = {fmt(vk / 3.6)} m/s", f"a = {fmt(vk / 3.6)} ÷ {t} = {fmt(vk / 3.6 / t)} m/s²", f"F = {m} × {fmt(vk / 3.6 / t)} = **{fmt(F)} N**"],
        ["Convert the speed to m/s.", "Find the acceleration.", "F = m a."],
        figure=sketches.motion_sketch("0", f"{vk} km/h", f"t = {t} s", body="car"))


@template("c4_mass_from_graph_force", chapter=4, level=3, lo="4c")
def mass_from_graph_force(rng):
    a = nice(rng, 1, 2, 2.5, 4)
    T = nice(rng, 4, 5, 8)
    F = nice(rng, 50, 100, 200, 400)
    m = F / a
    return calc_q(rng, f"A resultant force of **{F} N** acts on a trolley. Fig. 1 shows its speed–time graph. What is the mass of the trolley?", m, [
        (F * a, "m = F ÷ a, not F × a."),
        (F / (a * T), "The acceleration is the gradient: Δv ÷ Δt."),
        (a / F, "m = F ÷ a."),
    ], "kg", "a = gradient of v–t graph; m = F ÷ a", [f"a = {fmt(a * T)} ÷ {T} = {fmt(a)} m/s²", f"m = {F} ÷ {fmt(a)}", f"= **{fmt(m)} kg**"],
        ["Find the acceleration from the gradient of the graph.", "F = m a.", "Rearrange for m."],
        figure=_vt([(0, 0), (T, a * T)], a * T * 1.2))


@template("c4_accel_with_friction", chapter=4, level=3, lo="4c")
def accel_with_friction(rng):
    m = nice(rng, 4, 5, 10, 20)
    f = nice(rng, 5, 8, 10, 20)
    a = nice(rng, 0.5, 1, 1.5, 2)
    P = m * a + f
    return calc_q(rng, f"Fig. 1 shows a box of mass **{m} kg** pulled by a rope with a force of **{fmt(P)} N** against friction of **{f} N**. What is the acceleration of the box?", a, [
        (P / m, "Subtract the friction to get the resultant force first."),
        ((P + f) / m, "Friction acts AGAINST the pull, so subtract it."),
        ((P - f) * m, "a = F ÷ m."),
    ], "m/s²", "resultant = pull − friction; a = F ÷ m", [f"F = {fmt(P)} − {f} = {fmt(P - f)} N", f"a = {fmt(P - f)} ÷ {m}", f"= **{fmt(a)} m/s²**"],
        ["What is the resultant force on the box?", "Pull and friction act in opposite directions.", "a = resultant ÷ mass."],
        figure=figs.force_diagram([(f"{fmt(P)} N", "right", 1.8), (f"{f} N", "left", 1.0)], label_body=f"{m} kg"))


# ---------------------------------------------------------------- L4
@template("c4_find_applied_force", chapter=4, level=4, lo="4c")
def find_applied_force(rng):
    m = nice(rng, 20, 40, 50, 60)
    a = nice(rng, 0.5, 1, 1.5, 2)
    f = nice(rng, 30, 40, 60, 80)
    P = m * a + f
    return calc_q(rng, f"Fig. 1 shows a crate of mass **{m} kg** that accelerates at **{fmt(a)} m/s²** when pushed. The friction on it is **{f} N**. What is the size of the push?", P, [
        (m * a, "That is the RESULTANT force. The push must also overcome friction."),
        (m * a - f, "Push − friction = m a, so push = m a + friction."),
        (f, "That is only the friction."),
    ], "N", "push − friction = m a", [f"m a = {m} × {fmt(a)} = {fmt(m * a)} N", f"push = {fmt(m * a)} + {f}", f"= **{fmt(P)} N**"],
        ["Resultant force = push − friction.", "Resultant force = m a.", "So push = m a + friction."],
        figure=figs.force_diagram([("push = ?", "right", 1.8), (f"{f} N", "left", 1.0)], label_body=f"{m} kg"))


@template("c4_rocket_launch", chapter=4, level=4, lo="4c")
def rocket_launch(rng):
    m = nice(rng, 2000, 5000, 10000)
    a = nice(rng, 2, 5, 10, 15)
    T = m * (a + G)
    return calc_q(rng, f"Fig. 1 shows a rocket of mass **{m} kg** that accelerates upwards at **{a} m/s²** just after launch (g = 10 N/kg). What is the thrust from its engines?", T, [
        (m * a, "That is the resultant force. The thrust must also support the weight."),
        (m * G, "That is the weight; the thrust must be larger for the rocket to accelerate up."),
        (m * (a - G) if a != G else m * 5, "Thrust − weight = m a, so thrust = m a + m g."),
    ], "N", "thrust − weight = m a", [f"weight = {m} × 10 = {m * G} N", f"thrust = m a + W = {m * a} + {m * G}", f"= **{fmt(T)} N**"],
        ["Draw the two forces: thrust up, weight down.", "Resultant = thrust − weight = m a.", "Rearrange for thrust."],
        figure=figs.force_diagram([("thrust", "up", 1.8), (f"W = {m * G} N", "down", 1.2)], label_body="rocket", ground=False))


@template("c4_stop_time_from_force", chapter=4, level=4, lo="4c")
def stop_time_from_force(rng):
    m = nice(rng, 800, 1000, 1200, 1500)
    F = nice(rng, 3000, 4000, 6000)
    u = nice(rng, 15, 20, 24, 30)
    a = F / m
    t = u / a
    return calc_q(rng, f"Fig. 1 shows a car of mass **{m} kg** moving at **{u} m/s**. Its brakes give a constant braking force of **{F} N**. How long does it take to stop?", t, [
        (u * a, "t = Δv ÷ a, not Δv × a."),
        (u / F, "Find the deceleration first: a = F ÷ m."),
        (m * u / F / 2, "No ½ here: t = u ÷ a."),
    ], "s", "a = F ÷ m; t = u ÷ a", [f"a = {F} ÷ {m} = {fmt(a)} m/s²", f"t = {u} ÷ {fmt(a)}", f"= **{fmt(t)} s**"],
        ["Find the deceleration from F = m a.", "The car loses all its speed.", "time = change in speed ÷ deceleration."],
        figure=figs.force_diagram([(f"{F} N", "left", 1.6)], label_body=f"{m} kg"))


@template("c4_lift_tension_up", chapter=4, level=4, lo="4c")
def lift_tension_up(rng):
    m = nice(rng, 500, 600, 800, 1000)
    a = nice(rng, 0.5, 1, 1.5, 2)
    T = m * (G + a)
    return calc_q(rng, f"Fig. 1 shows a lift of mass **{m} kg** accelerating upwards at **{fmt(a)} m/s²** (g = 10 N/kg). What is the tension in the cable?", T, [
        (m * G, "That would be the tension at constant speed. The lift is accelerating upwards."),
        (m * (G - a), "When accelerating UP, the tension is GREATER than the weight."),
        (m * a, "That is the resultant force only."),
    ], "N", "T − W = m a", [f"W = {m} × 10 = {m * G} N", f"T = {m * G} + {m} × {fmt(a)}", f"= **{fmt(T)} N**"],
        ["Two forces act: tension up and weight down.", "Resultant = T − W = m a.", "T = W + m a."],
        figure=figs.force_diagram([("T = ?", "up", 1.8), (f"W = {m * G} N", "down", 1.4)], label_body="lift", ground=False))


# ---------------------------------------------------------------- L5
@template("c4_parachute_deceleration", chapter=4, level=5, lo="4c")
def parachute_deceleration(rng):
    m = nice(rng, 60, 70, 80, 90)
    R = nice(rng, 1200, 1500, 1800, 2000)
    a = (R - m * G) / m
    return calc_q(rng, f"Fig. 1 shows a parachutist of mass **{m} kg** just after the parachute opens. The air resistance is **{R} N** (g = 10 N/kg). What is the size of her deceleration?", a, [
        (R / m, "Subtract the weight to find the resultant force first."),
        ((R + m * G) / m, "Weight and air resistance act in OPPOSITE directions."),
        (R - m * G, "That is the resultant force; divide by the mass."),
    ], "m/s²", "resultant = R − W (upwards); a = F ÷ m", [f"W = {m} × 10 = {m * G} N", f"resultant = {R} − {m * G} = {R - m * G} N upwards", f"a = {R - m * G} ÷ {m} = **{fmt(a)} m/s²**"],
        ["Compare the air resistance with the weight.", "The resultant force acts upwards, so she slows down.", "a = resultant ÷ mass."],
        figure=figs.force_diagram([(f"{R} N", "up", 1.8), (f"W = {m * G} N", "down", 1.0)], label_body=f"{m} kg", ground=False))


@template("c4_braking_distance_from_force", chapter=4, level=5, lo="4c")
def braking_distance_from_force(rng):
    m = nice(rng, 1000, 1200, 1500)
    u = nice(rng, 20, 24, 30)
    a = nice(rng, 4, 5, 6)
    F = m * a
    t = u / a
    d = 0.5 * u * t
    table = md_table(["mass / kg", "initial speed / m/s", "braking force / N"], [[m, u, F]])
    return calc_q(rng, f"The table gives data for a car braking to rest with a constant force.\n\n{table}\n\nWhat is its braking distance?", d, [
        (u * t, "Braking is uniform deceleration: distance = ½ × u × t (area of a triangle)."),
        (u * u / a, "Distance = ½ × u × t, where t = u ÷ a."),
        (t, "That is the braking time, not the distance."),
    ], "m", "a = F ÷ m; t = u ÷ a; distance = ½ u t", [f"a = {F} ÷ {m} = {fmt(a)} m/s²", f"t = {u} ÷ {fmt(a)} = {fmt(t)} s", f"d = ½ × {u} × {fmt(t)} = **{fmt(d)} m**"],
        ["Find the deceleration from F = m a.", "Find the stopping time.", "The distance is the area of the triangle under the v–t graph."])


@template("c4_terminal_drag", chapter=4, level=5, lo="4a")
def terminal_drag(rng):
    m = nice(rng, 0.05, 0.2, 60, 75, 90)
    D = m * G
    return calc_q(rng, f"Fig. 1 shows an object of mass **{fmt(m)} kg** falling through air at its terminal velocity (g = 10 N/kg). What is the air resistance on it?", D, [
        (0, "At terminal velocity the object is still moving, and air resistance acts on it."),
        (m, "That is the mass; air resistance is a force in newtons."),
        (D * 2, "At terminal velocity air resistance EQUALS the weight."),
    ], "N", "terminal velocity: resultant force = 0, so air resistance = weight", ["resultant force = 0 (constant velocity)", f"air resistance = W = {fmt(m)} × 10", f"= **{fmt(D)} N**"],
        ["What is the acceleration at terminal velocity?", "Zero acceleration means zero resultant force.", "So air resistance balances the weight."],
        figure=figs.force_diagram([("air resistance", "up", 1.6), ("weight", "down", 1.6)], label_body=f"{fmt(m)} kg", ground=False))


@template("c4_friction_from_graph", chapter=4, level=5, lo="4d")
def friction_from_graph(rng):
    m = nice(rng, 10, 20, 25, 40)
    a = nice(rng, 0.5, 1, 1.5, 2)
    T = nice(rng, 4, 5, 6)
    f = nice(rng, 10, 20, 30)
    P = m * a + f
    return calc_q(rng, f"A box of mass **{m} kg** is pulled across a floor by a constant force of **{fmt(P)} N**. Fig. 1 shows its speed–time graph. What is the friction acting on the box?", f, [
        (m * a, "That is the resultant force (m a). Friction = pull − m a."),
        (P, "That is the pull; some of it is used to overcome friction."),
        (P - m * a * T, "The acceleration is the gradient, a = Δv ÷ Δt."),
    ], "N", "a = gradient; pull − friction = m a", [f"a = {fmt(a * T)} ÷ {T} = {fmt(a)} m/s²", f"m a = {m} × {fmt(a)} = {fmt(m * a)} N", f"friction = {fmt(P)} − {fmt(m * a)} = **{fmt(f)} N**"],
        ["Find the acceleration from the gradient.", "Resultant force = m a.", "Friction = pull − resultant."],
        figure=_vt([(0, 0), (T, a * T)], a * T * 1.2))
