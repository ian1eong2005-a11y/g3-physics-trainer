"""O level 2026 MCQ practice, Ch 1-4: SEAB O-Level MCQs (2014-2021 papers, 2024 specimen) on learning outcomes that the
2026 Paper 2 (Q1-7) did not test, ADAPTED (same context and skill, numbers changed slightly; numbers vary on every serve)."""
import numpy as np

from .. import figs, sketches, sketches3 as k3
from ..config import G
from .base import calc_q, explain_mcqs, fmt, md_table, nice, template, text_options

CAT = "olevel"


def src(text):
    return f"_Adapted from {text}._"


# ================================================================== Ch 1 Measurement
explain_mcqs([
    dict(id="o26_scalar", chapter=1, level=1, lo="1f", source="SEAB O-Level 2016 MCQ 1",
         stem="Which quantity is a scalar quantity?",
         correct="distance",
         wrongs={"acceleration": "Acceleration has a direction, so it is a vector.",
                 "weight": "Weight is a force; it acts in a direction (downwards), so it is a vector.",
                 "velocity": "Velocity is speed in a stated direction, so it is a vector."},
         hints=["A scalar has magnitude only; a vector has magnitude AND direction.",
                "Which of these could you state without giving a direction?",
                "Distance is how far; displacement is how far in a direction."]),
    dict(id="o26_two_vectors", chapter=1, level=2, lo="1f", source="SEAB O-Level 2019 MCQ 1",
         stem="Which pair consists of **two** vector quantities?",
         correct="force and velocity",
         wrongs={"mass and velocity": "Mass is a scalar: it has no direction.",
                 "speed and acceleration": "Speed is a scalar; velocity is the vector version.",
                 "energy and weight": "Energy is a scalar."},
         hints=["Check each quantity in the pair: does it need a direction?",
                "Mass, speed, energy, density, pressure and work are scalars.",
                "Find the pair where BOTH need a direction."]),
    dict(id="o26_prefix_convert", chapter=1, level=2, lo="1c", source="SEAB O-Level 2018 MCQ 1",
         stem="A potential difference of **5 millivolts** across a resistor causes a current of **3 microamperes**.\n\n"
              + md_table(["quantity", "with prefix"], [["p.d.", "5 mV"], ["current", "3 μA"]])
              + "\n\nWhich gives the p.d. in volts and the current in amperes?",
         correct="0.005 V and 0.000 003 A",
         wrongs={"0.000 005 V and 0.000 003 A": "milli = 10⁻³, not 10⁻⁶. 5 mV = 0.005 V.",
                 "0.005 V and 0.003 A": "micro = 10⁻⁶, not 10⁻³. 3 μA = 0.000 003 A.",
                 "0.000 005 V and 0.003 A": "Both prefixes are swapped: milli = 10⁻³ and micro = 10⁻⁶."},
         hints=["milli (m) means × 10⁻³.", "micro (μ) means × 10⁻⁶.", "5 × 10⁻³ V and 3 × 10⁻⁶ A."]),
    dict(id="o26_energy_units_order", chapter=1, level=2, lo="1c", source="SEAB O-Level 2020 MCQ 1",
         stem="Which list shows units of energy in order of **increasing** size?\n\n"
              + md_table(["prefix", "μ", "m", "k", "M"], [["value", "10⁻⁶", "10⁻³", "10³", "10⁶"]]),
         correct="μJ → mJ → kJ → MJ",
         wrongs={"mJ → μJ → kJ → MJ": "μ (10⁻⁶) is smaller than m (10⁻³), so μJ comes first.",
                 "MJ → kJ → mJ → μJ": "This is decreasing size.",
                 "kJ → MJ → μJ → mJ": "Order the powers of ten from the most negative to the most positive."},
         hints=["Write each prefix as a power of ten.", "μ = 10⁻⁶, m = 10⁻³, k = 10³, M = 10⁶.",
                "Increasing means smallest first."]),
], category=CAT)


# ================================================================== Ch 2 Kinematics
def _curve_then_line():
    ts = np.linspace(0, 8, 81)
    vs = np.where(ts < 4, 0.28 * ts ** 2, 4.48 + 2.24 * (ts - 4))
    return list(zip(ts, vs))


def _vwxyz():
    pts = [(t, 0.5 * t * t) for t in np.linspace(0, 2, 21)]
    pts += [(t, 2 + 2 * (t - 2) - 0.5 * (t - 2) ** 2) for t in np.linspace(2, 4, 21)]
    pts += [(8, 4), (10, 0)]
    return pts


def _parachute():
    ts = np.linspace(0, 16, 81)
    pts = [(t, 50 * (1 - np.exp(-t / 4))) for t in ts]
    v_top = pts[-1][1]
    pts += [(18, v_top)]
    pts += [(18 + d, 6 + (v_top - 6) * np.exp(-d * 1.6)) for d in np.linspace(0, 3, 31)]
    pts += [(30, 6), (30.3, 0)]
    return pts, v_top


explain_mcqs([
    dict(id="o26_curve_then_line", chapter=2, level=2, lo="2g", source="SEAB O-Level 2014 MCQ 2",
         stem="Fig. 1 is the speed-time graph of a car that starts from rest. Which describes the motion of the car?",
         correct="non-uniform acceleration, then uniform acceleration",
         wrongs={"uniform acceleration, then non-uniform acceleration": "The curved part comes first: a curve means the gradient (acceleration) is changing.",
                 "uniform speed, then non-uniform acceleration": "Uniform speed would be a horizontal line. The speed is rising all the time.",
                 "uniform speed, then uniform acceleration": "The speed is never constant here; the graph never goes flat."},
         hints=["On a speed-time graph the gradient is the acceleration.", "A curve = changing gradient; a straight sloping line = constant gradient.",
                "Look at the order: curve first, straight line second."],
         figure=lambda: figs.graph(_curve_then_line(), 8, 16, 2, 4)),
    dict(id="o26_decreasing_accel", chapter=2, level=3, lo="2d", source="SEAB O-Level 2015 MCQ 3",
         stem="Fig. 1 is a speed-time graph. In which part of the motion is the acceleration **decreasing**?",
         correct="Q to R",
         wrongs={"P to Q": "From P to Q the graph gets steeper: the acceleration is increasing.",
                 "R to S": "R to S is flat: zero acceleration, not decreasing acceleration.",
                 "S to T": "S to T is a straight line: constant deceleration."},
         hints=["Acceleration = gradient of the speed-time graph.", "Decreasing acceleration: the speed still rises, but the curve gets flatter.",
                "Which part curves over towards the horizontal?"],
         figure=lambda: figs.graph(_vwxyz(), 10, 5, 2, 1, labels=[(0, 0, "P", 8, 10), (2, 2, "Q", -10, 8), (4, 4, "R", -4, 12), (8, 4, "S", 6, 12), (10, 0, "T", -10, 10)])),
    dict(id="o26_parachute_opens", chapter=2, level=3, lo="2g", source="SEAB O-Level 2016 MCQ 2",
         stem="Fig. 1 is the speed-time graph of a skydiver who jumps from a plane and later opens a parachute. At which point does the parachute open?",
         correct="Q",
         wrongs={"P": "At P the speed is still increasing quickly: the skydiver is still in free fall.",
                 "R": "At R the skydiver has already slowed down to the new, lower terminal speed.",
                 "S": "S is where the skydiver lands and stops."},
         hints=["Opening the parachute suddenly increases the air resistance.", "That causes a sudden, large deceleration.",
                "Find where the speed starts to drop steeply."],
         figure=lambda: figs.graph(_parachute()[0], 32, 60, 4, 10, labels=[(4, 50 * (1 - np.exp(-1)), "P", -10, 8), (18, _parachute()[1], "Q", 4, 12),
                                                                           (21, 6, "R", 4, 12), (30, 6, "S", 2, 12)])),
    dict(id="o26_accel_how", chapter=2, level=1, lo="2c", source="SEAB O-Level 2019 MCQ 2",
         stem="How is the value of a uniform acceleration calculated?\n\n" + md_table(["quantity", "symbol"], [["initial velocity", "u"], ["final velocity", "v"], ["time taken", "t"]]),
         correct="change in velocity ÷ time taken",
         wrongs={"distance travelled ÷ time taken": "That is average speed.",
                 "area under a speed-time graph": "The area gives the distance travelled.",
                 "gradient of a distance-time graph": "That gradient is the speed."},
         hints=["Acceleration is the rate of change of velocity.", "Rate of change = change ÷ time.", "a = (v − u) ÷ t."]),
    dict(id="o26_accel_from_graph", chapter=2, level=1, lo="2e", source="SEAB O-Level 2021 MCQ 2",
         stem="How can the acceleration of an object be found from a graph?\n\n" + md_table(["graph", "gradient gives", "area gives"], [["distance-time", "?", "–"], ["speed-time", "?", "?"]]),
         correct="from the gradient of a speed-time graph",
         wrongs={"from the area under a speed-time graph": "The area under a speed-time graph is the distance travelled.",
                 "from the gradient of a distance-time graph": "The gradient of a distance-time graph is the speed.",
                 "from the area under a distance-time graph": "This area has no meaning in the syllabus."},
         hints=["Acceleration = change in speed ÷ time.", "On which graph is (change in speed ÷ time) the slope?", "Gradient of speed-time = acceleration."]),
], category=CAT)


@template("o26_graph_accel_mass", chapter=2, level=3, lo="2c", category=CAT)
def graph_accel_mass(rng):
    v, t = nice(rng, (8, 2), (9, 3), (12, 4), (12, 3), (10, 5))
    a = v / t
    m = nice(rng, 0.20, 0.25, 0.40, 0.50)
    F = m * a
    q = calc_q(rng, f"Fig. 1 is the speed-time graph of a trolley pulled by a constant resultant force of **{fmt(F)} N**. What is the mass of the trolley?",
               m, [(F * a, "You multiplied F by a. Rearrange F = ma: m = F ÷ a."), (F / v, "You divided by the speed, not the acceleration."),
                   (a / F, "You divided the wrong way round: m = F ÷ a.")], "kg", "F = ma, a = gradient of the speed-time graph",
               [f"a = gradient = {fmt(v)} ÷ {fmt(t)} = {fmt(a)} m/s²", f"m = F ÷ a = {fmt(F)} ÷ {fmt(a)} = **{fmt(m)} kg**", src("SEAB O-Level 2015 MCQ 4")],
               ["First find the acceleration from the graph.", "Acceleration = gradient = change in speed ÷ time.", "Then use F = ma, so m = F ÷ a."],
               figure=figs.graph([(0, 0), (t, v)], t + 1, v + 2 if v % 2 == 0 else v + 1, 1, 2 if v > 9 else 1))
    return q


@template("o26_avg_speed_two_legs", chapter=2, level=2, lo="2b", category=CAT)
def avg_speed_two_legs(rng):
    d1, t1, d2, t2 = nice(rng, (90, 60, 30, 30), (75, 45, 25, 15), (60, 40, 30, 20), (120, 90, 20, 30), (100, 50, 20, 40))
    T = (t1 + t2) / 60
    v = (d1 + d2) / T
    mean = (d1 / (t1 / 60) + d2 / (t2 / 60)) / 2
    return calc_q(rng, "A car travels along a main road and then a side road (table). What is its average speed for the whole journey?\n\n"
                  + md_table(["part", "distance / km", "time / min"], [["main road", d1, t1], ["side road", d2, t2]]),
                  v, [(mean, "You averaged the two speeds. Use total distance ÷ total time."), ((d1 + d2) / (t1 / 60), "You used the time for the main road only."),
                      (d1 / (t1 / 60), "That is the speed on the main road only.")], "km/h", "average speed = total distance ÷ total time",
                  [f"total distance = {d1} + {d2} = {d1 + d2} km", f"total time = {t1} + {t2} = {t1 + t2} min = {fmt(T)} h",
                   f"average speed = {d1 + d2} ÷ {fmt(T)} = **{fmt(v)} km/h**", src("SEAB O-Level 2017 MCQ 1")],
                  ["Average speed is NOT the average of the two speeds.", "Add the distances, add the times.", "Change the total time to hours."])


@template("o26_distance_kmh_min", chapter=2, level=4, lo="2h", category=CAT)
def distance_kmh_min(rng):
    u, v, t = nice(rng, (36, 72, 5), (40, 80, 6), (30, 90, 2), (54, 90, 5), (50, 70, 3))
    d = (u + v) / 2 * t / 60
    return calc_q(rng, f"Fig. 1 shows a car speeding up with constant acceleration from **{u} km/h to {v} km/h in {t} minutes**. What distance does it travel in this time?",
                  d, [(v * t / 60, "You used the final speed for the whole time. The car was slower at the start."),
                      ((u + v) * t / 60, "You forgot to halve: average speed = (u + v) ÷ 2."),
                      ((v - u) / 2 * t / 60, "That is only the triangle part of the area; add the rectangle under it.")],
                  "km", "distance = area under the speed-time graph = average speed × time",
                  [f"average speed = ({u} + {v}) ÷ 2 = {fmt((u + v) / 2)} km/h", f"time = {t} min = {fmt(t / 60)} h",
                   f"distance = {fmt((u + v) / 2)} × {fmt(t / 60)} = **{fmt(d)} km**", src("SEAB O-Level 2017 MCQ 2")],
                  ["The distance is the area under the speed-time graph.", "For uniform acceleration that area = average speed × time.", "Change minutes into hours."],
                  figure=figs.graph([(0, u), (t, v)], t + 1, 100, 1, 20, xlabel="time / min", ylabel="speed / km/h"))


@template("o26_runners_same_distance", chapter=2, level=5, lo="2h", category=CAT)
def runners_same_distance(rng):
    # runner X: 0 -> vx in tx, then constant; runner Y: 0 -> vy in ty, then constant. Find when distances are equal (Y ahead at first).
    vx, tx, vy, ty = nice(rng, (12, 4, 8, 2), (12, 6, 8, 2), (10, 4, 6, 1), (15, 6, 9, 2))

    def dist(v, tt, t):
        return 0.5 * v / tt * t * t if t <= tt else 0.5 * v * tt + v * (t - tt)
    ts = np.linspace(0.01, 12, 120001)
    diff = np.array([dist(vx, tx, t) - dist(vy, ty, t) for t in ts])
    t_eq = round(float(ts[np.argmax(diff >= 0)]), 1)
    t_end = 8.0
    lead = dist(vx, tx, t_end) - dist(vy, ty, t_end)
    t_same_speed = round(vy / (vx / tx), 1)
    correct = f"The runners have run the same distance after {fmt(t_eq, dp=1)} s."
    wrongs = {f"The runners have run the same distance after {fmt(t_same_speed, dp=1)} s.": f"At {fmt(t_same_speed, dp=1)} s their SPEEDS are equal (the lines cross); distance is the AREA under each line.",
              f"After {fmt(t_end, dp=1)} s, runner Y has run {fmt(abs(lead))} m further than runner X.": "Work out both areas at 8.0 s: X is ahead, not Y.",
              f"After {fmt(t_end, dp=1)} s, runner X has run {fmt(2 * abs(lead))} m further than runner Y.": f"Check the areas: X is ahead by {fmt(abs(lead))} m, not {fmt(2 * abs(lead))} m."}
    assert lead > 0 and t_eq != t_same_speed
    opts, key, mis = text_options(rng, correct, wrongs)
    xp = [(0, 0), (tx, vx), (10, vx)]
    yp = [(0, 0), (ty, vy), (10, vy)]
    return dict(stem="Fig. 1 is the speed-time graph for two runners, X and Y, who start a race together. Which statement is correct?",
                figure=k3.two_runner_graph(xp, yp, 10, max(vx, vy) + 4, 2, 2 if vx <= 12 else 3),
                options=opts, key=key, misconceptions=mis, formula="distance = area under the speed-time graph",
                working=[f"Y: area = ½ × {ty} × {vy} + {vy}(t − {ty});  X: area = ½ × {tx} × {vx} for the first {tx} s, then + {vx}(t − {tx})",
                         f"The areas are equal at t = **{fmt(t_eq, dp=1)} s**", f"At 8.0 s X is ahead by {fmt(lead)} m.", src("SEAB O-Level 2019 MCQ 3")],
                hints=["Distance travelled = area under each line.", "Write each runner's area as a function of time, or test the times in the options.",
                       "Where the lines cross the SPEEDS are equal, not the distances."])


@template("o26_trolley_accel", chapter=2, level=1, lo="2c", category=CAT)
def trolley_accel(rng):
    u = nice(rng, 0.5, 1.0, 2.0)
    a = nice(rng, 1.5, 2.0, 2.5)
    t = nice(rng, 2.0, 4.0)
    v = u + a * t
    return calc_q(rng, "A student measures the velocity of a trolley moving in a straight line (table). What is its acceleration?\n\n"
                  + md_table(["time / s", "velocity / m/s"], [["0", fmt(u)], [fmt(t), fmt(v)]]),
                  a, [(v / t, "You used the final velocity, not the CHANGE in velocity."), ((v + u) / t, "You added the velocities; use v − u."),
                      ((v - u) * t, "You multiplied by the time; divide instead.")], "m/s²", "a = (v − u) ÷ t",
                  [f"a = ({fmt(v)} − {fmt(u)}) ÷ {fmt(t)} = **{fmt(a)} m/s²**", src("SEAB specimen 2024 MCQ 2")],
                  ["Acceleration = change in velocity ÷ time.", f"Change in velocity = {fmt(v)} − {fmt(u)}.", f"Divide by {fmt(t)} s."])


# ================================================================== Ch 3 Force and Pressure
@template("o26_moon_mass_weight", chapter=3, level=2, lo="3e", category=CAT)
def moon_mass_weight(rng):
    m = nice(rng, 12, 20, 25, 30)
    gm = 1.6
    correct = f"mass {m} kg, weight {fmt(m * gm)} N"
    wrongs = {f"mass {m} kg, weight {fmt(m * G)} N": "That is its weight on Earth. On the Moon use g = 1.6 N/kg.",
              f"mass {fmt(m * gm / G)} kg, weight {fmt(m * gm)} N": "Mass does NOT change when an object is moved; only its weight changes.",
              f"mass {fmt(m * gm)} kg, weight {fmt(m * gm * G)} N": "Mass stays the same, and weight = mass × g with the Moon's g."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"An object of mass **{m} kg** on Earth is taken to the Moon (Fig. 1). What are its mass and weight on the Moon?",
                figure=sketches.two_bodies_sketch(["g = 10 N/kg"], ["g = 1.6 N/kg"]),
                options=opts, key=key, misconceptions=mis, formula="weight = mass × g",
                working=["Mass is the amount of matter: it does not change.", f"weight on the Moon = {m} × 1.6 = **{fmt(m * gm)} N**", src("SEAB O-Level 2014 MCQ 4")],
                hints=["Does the amount of matter change when you move the object?", "W = m g.", "Use the Moon's value of g."])


explain_mcqs([
    dict(id="o26_g_definition", chapter=3, level=1, lo="3d", source="SEAB O-Level 2015 MCQ 5 and 2021 MCQ 5",
         stem="How is the gravitational field strength at a place calculated?",
         correct="weight ÷ mass",
         wrongs={"mass ÷ weight": "Upside down: g = W ÷ m, in N/kg.", "mass × weight": "The unit N/kg shows a division.",
                 "weight × 10": "10 N/kg is the value of g near the Earth, not how it is defined."},
         hints=["g is the gravitational force per unit mass.", "Look at its unit: N/kg.", "Newtons divided by kilograms."]),
    dict(id="o26_mass_not_correct", chapter=3, level=2, lo="3b", source="SEAB O-Level 2016 MCQ 4",
         stem="Which statement about the mass of a body is **not** correct?",
         correct="Its mass becomes smaller when it is taken to the Moon.",
         wrongs={"Its mass is a measure of the amount of matter in it.": "This statement is TRUE, so it is not the answer.",
                 "Its mass resists a change in its state of rest or motion.": "This is TRUE (inertia), so it is not the answer.",
                 "Its mass is attracted by a gravitational field.": "This is TRUE: a mass in a gravitational field feels a force."},
         hints=["Three of these statements are true.", "What changes on the Moon: mass or weight?", "Mass does not depend on g."]),
    dict(id="o26_grav_force", chapter=3, level=2, lo="3c", source="SEAB O-Level 2018 MCQ 5",
         stem="A gravitational field is a region in which a mass feels a force. Which statement about this force is correct?",
         correct="It keeps the Moon in orbit around the Earth.",
         wrongs={"It can be attractive or repulsive.": "Gravitational force is always attractive.",
                 "It depends on the charge on the body.": "That is the electric force. Gravity acts on mass.",
                 "It depends only on the volume of the body.": "It depends on the mass, not the volume."},
         hints=["Gravity acts between masses.", "Is gravity ever repulsive?", "What holds a moon or planet in its orbit?"]),
    dict(id="o26_inertia_same", chapter=3, level=2, lo="3b", source="SEAB O-Level 2020 MCQ 4",
         stem="A 2 kg block is placed in turn on the surface of the Earth, inside a space station in orbit and on the surface of the Moon (Fig. 1). Where is its inertia the largest?",
         correct="It is the same in all three places.",
         wrongs={"on the surface of the Earth": "Inertia depends on mass, which does not change with g.",
                 "inside the space station": "'Weightless' does not mean massless; inertia is unchanged.",
                 "on the surface of the Moon": "The weight is smaller on the Moon, but the mass (and inertia) is the same."},
         hints=["Inertia is the resistance to a change in motion.", "Which quantity measures inertia: mass or weight?", "Does the mass change from place to place?"],
         figure=lambda: sketches.two_bodies_sketch(["2 kg block"], ["2 kg block"])),
    dict(id="o26_smallest_mass", chapter=3, level=3, lo="3e", source="SEAB O-Level 2020 MCQ 5",
         stem="Four objects are on four different planets.\n\n"
              + md_table(["object", "field strength / N per kg", "weight / N"], [["P", "8", "112"], ["Q", "10", "100"], ["R", "12", "216"], ["S", "24", "144"]])
              + "\n\nWhich object has the smallest mass?",
         correct="S", wrongs={"Q": "Q has the smallest WEIGHT. Mass = weight ÷ g = 10 kg.",
                              "P": "P: 112 ÷ 8 = 14 kg.", "R": "R: 216 ÷ 12 = 18 kg."},
         hints=["Mass = weight ÷ field strength.", "Work it out for every object.", "The smallest weight is not always the smallest mass."]),
    dict(id="o26_plane_climbs", chapter=3, level=2, lo="3f", source="SEAB specimen 2024 MCQ 3",
         stem="A passenger sits in an aeroplane that takes off and climbs to 12 000 m. During this time, what happens to the mass and the weight of the passenger?\n\n"
              + md_table(["height / m", "g / N per kg"], [["0", "9.81"], ["12 000", "9.77"]]),
         correct="mass unchanged, weight decreases",
         wrongs={"mass decreases, weight decreases": "Mass does not depend on height.",
                 "mass unchanged, weight increases": "g gets slightly SMALLER higher up, so W = mg gets smaller.",
                 "mass increases, weight increases": "Neither increases."},
         hints=["Mass is the amount of matter.", "Weight = mass × g.", "Look at how g changes in the table."]),
], category=CAT)


@template("o26_hollow_block_density", chapter=3, level=4, lo="3g", category=CAT)
def hollow_block_density(rng):
    L, w, h = nice(rng, (10, 6, 5), (12, 5, 4), (10, 5, 4))
    p, q = nice(rng, (4, 2), (3, 2), (2, 2))
    V = L * w * h - L * p * q
    rho = nice(rng, 2.7, 7.9, 8.9)
    m = rho * V
    return calc_q(rng, "A metal block has a rectangular hole cut right through its length (table). What is the density of the metal?\n\n"
                  + md_table(["measurement", "value"], [["outside of block", f"{L} cm × {w} cm × {h} cm"], ["hole (through the {L} cm length)", f"{p} cm × {q} cm"],
                                                       ["mass of block", f"{fmt(m)} g"]]),
                  rho, [(m / (L * w * h), "You used the outside volume and forgot to subtract the hole."), (m / (L * p * q), "You used the volume of the hole."),
                        (V / m, "You divided volume by mass; density = mass ÷ volume.")], "g/cm³", "density = mass ÷ volume",
                  [f"volume of metal = {L}×{w}×{h} − {L}×{p}×{q} = {L * w * h} − {L * p * q} = {V} cm³", f"density = {fmt(m)} ÷ {V} = **{fmt(rho)} g/cm³**",
                   src("SEAB O-Level 2015 MCQ 6")],
                  ["Find the volume of metal only.", "Volume of metal = outside volume − volume of the hole.", "Then density = mass ÷ volume."])


@template("o26_stone_water_volume", chapter=3, level=3, lo="3g", category=CAT)
def stone_water_volume(rng):
    R = nice(rng, 4.4, 4.8, 5.2, 5.6, 6.2)
    M, rho = nice(rng, (3.0, 2.5), (5.4, 2.7), (4.8, 3.0))
    Vs = M / rho
    Vw = R - Vs
    return calc_q(rng, f"Fig. 1 shows a measuring cylinder containing some water and a stone. The stone has a mass of **{fmt(M)} g** and a density of **{fmt(rho)} g/cm³**. What is the volume of the water?",
                  Vw, [(R, "That is the water AND the stone together."), (R - M, "You subtracted the mass of the stone; subtract its volume."),
                       (R + Vs, "Subtract the stone's volume; do not add it.")], "cm³", "volume = mass ÷ density",
                  [f"reading = {fmt(R)} cm³", f"volume of stone = {fmt(M)} ÷ {fmt(rho)} = {fmt(Vs)} cm³", f"volume of water = {fmt(R)} − {fmt(Vs)} = **{fmt(Vw)} cm³**",
                   src("SEAB O-Level 2017 MCQ 4")],
                  ["The reading includes the stone.", "Find the stone's volume from its mass and density.", "Subtract it from the reading."],
                  figure=k3.cylinder_stone(R), sf=2)


@template("o26_g_on_planet", chapter=3, level=2, lo="3e", category=CAT)
def g_on_planet(rng):
    WE = nice(rng, 1200, 1500, 2000)
    name, gp = nice(rng, ("Mars", 3.7), ("Mercury", 3.8), ("the Moon", 1.6))
    Wp = WE * gp / G
    return calc_q(rng, f"A space probe weighs **{WE} N** on Earth (g = 10 N/kg) and **{fmt(Wp)} N** on {name} (Fig. 1). What is the gravitational field strength on {name}?",
                  gp, [(Wp / WE, "You found the ratio of the weights; multiply it by 10 N/kg."), (G * WE / Wp, "Upside down: g = W ÷ m."),
                       (WE / Wp, "Find the mass first: m = W ÷ g on Earth.")], "N/kg", "W = m g",
                  [f"mass = {WE} ÷ 10 = {fmt(WE / G)} kg", f"g = {fmt(Wp)} ÷ {fmt(WE / G)} = **{fmt(gp)} N/kg**", src("SEAB O-Level 2018 MCQ 6")],
                  ["The mass is the same in both places.", "Find the mass from the Earth weight.", "g on the planet = weight there ÷ mass."],
                  figure=sketches.two_bodies_sketch([f"weight {WE} N"], [f"weight {fmt(Wp)} N"], right_name=name))


@template("o26_paper_clips", chapter=3, level=4, lo="3g", category=CAT)
def paper_clips(rng):
    m = nice(rng, 0.40, 0.50, 0.80)
    before = nice(rng, 20, 30)
    dV = nice(rng, 15, 20, 25)
    rho = 8.0
    n = dV * rho / m
    return calc_q(rng, f"A student finds the number of steel paper clips in a box. One clip has a mass of **{fmt(m)} g**; steel has a density of **8.0 g/cm³**. "
                  "Fig. 1 shows the water level before and after all the clips are added. How many clips are in the box?",
                  n, [(dV / m, "You divided the volume by the mass of one clip. Find the total MASS first (volume × density)."),
                      ((before + dV) * rho / m, "Use the RISE in the water level, not the final reading."),
                      (dV * rho, "That is the total mass in grams; divide by the mass of one clip.")], "", "mass = density × volume",
                  [f"volume of clips = {before + dV} − {before} = {dV} cm³", f"mass of clips = {dV} × 8.0 = {fmt(dV * rho)} g",
                   f"number = {fmt(dV * rho)} ÷ {fmt(m)} = **{fmt(n)}**", src("SEAB O-Level 2019 MCQ 4")],
                  ["Volume of clips = rise in water level.", "Total mass = density × volume.", "Number = total mass ÷ mass of one clip."],
                  figure=figs.two_cylinders(before, before + dV, max_ml=60, step_ml=10, minor_ml=2))


# ================================================================== Ch 4 Dynamics
explain_mcqs([
    dict(id="o26_tyre_friction", chapter=4, level=3, lo="4d", source="SEAB O-Level 2014 MCQ 3",
         stem="A car is driven forwards along a level road and is speeding up. In which direction does the friction force from the road act on the tyres of its driving wheels?",
         correct="forwards, in the direction the car is moving",
         wrongs={"backwards, opposite to the direction the car is moving": "The driving wheels push BACK on the road; the road pushes the tyres FORWARDS. That is what drives the car.",
                 "upwards, away from the road": "Upwards is the normal force, not friction.",
                 "there is no friction on the driving wheels": "Without friction the wheels would just spin (like on ice)."},
         hints=["The wheel turns and its tyre pushes backwards on the road.", "By Newton's third law the road pushes the tyre the other way.",
                "What force actually makes the car speed up?"]),
], category=CAT)


@template("o26_box_accel", chapter=4, level=2, lo="4c", category=CAT)
def box_accel(rng):
    m = nice(rng, 40, 60, 80)
    a = nice(rng, 0.25, 0.50, 0.75)
    f = nice(rng, 180, 240, 300)
    F = f + m * a
    return calc_q(rng, f"A box of mass **{m} kg** is pushed across a floor with a force of **{fmt(F)} N**. The total friction on the box is **{f} N** (Fig. 1). What is the acceleration of the box?",
                  a, [(F / m, "You ignored friction. Use the RESULTANT force."), ((F + f) / m, "Friction acts against the push: subtract it."),
                      (f / m, "You used the friction force alone.")], "m/s²", "resultant force = m a",
                  [f"resultant force = {fmt(F)} − {f} = {fmt(F - f)} N", f"a = {fmt(F - f)} ÷ {m} = **{fmt(a)} m/s²**", src("SEAB O-Level 2018 MCQ 4")],
                  ["Find the resultant force first.", "Resultant = push − friction.", "a = F ÷ m."],
                  figure=figs.force_diagram([(f"{fmt(F)} N", "right", 1.4), (f"friction {f} N", "left", 1.0)], label_body=f"{m} kg"))


@template("o26_friction_from_accel", chapter=4, level=3, lo="4d", category=CAT)
def friction_from_accel(rng):
    m = nice(rng, 120, 150, 200)
    a = nice(rng, 0.40, 0.50)
    f = nice(rng, 90, 120, 150)
    F = f + m * a
    return calc_q(rng, f"A crate of mass **{m} kg** is pushed across a rough floor with a force of **{fmt(F)} N**. Its acceleration is **{fmt(a)} m/s²**. What is the friction force on the crate?\n\n"
                  + md_table(["mass / kg", "push / N", "acceleration / m/s²"], [[m, fmt(F), fmt(a)]]),
                  f, [(m * a, "That is the RESULTANT force, not the friction."), (F + m * a, "Friction = push − resultant, not push + resultant."),
                      (F, "That is the push. Friction is smaller because the crate accelerates.")], "N", "resultant force = m a",
                  [f"resultant = {m} × {fmt(a)} = {fmt(m * a)} N", f"friction = {fmt(F)} − {fmt(m * a)} = **{fmt(f)} N**", src("SEAB O-Level 2020 MCQ 3")],
                  ["Find the resultant force from F = ma.", "Resultant = push − friction.", "So friction = push − resultant."])


@template("o26_braking_force", chapter=4, level=4, lo="4c", category=CAT)
def braking_force(rng):
    m = nice(rng, 1200, 1500, 1800)
    v, tmin = nice(rng, (24, 0.40), (30, 0.50), (36, 0.50), (18, 0.25))
    cruise = nice(rng, 6, 8, 10)
    a = v / (tmin * 60)
    F = m * a
    return calc_q(rng, f"A car of mass **{m} kg** travels at a constant **{v} m/s** for {cruise} minutes. The brakes are then applied and the car slows down uniformly, stopping in **{fmt(tmin)} minutes**. What is the braking force?\n\n"
                  + md_table(["mass / kg", "speed / m/s", "braking time / min"], [[m, v, fmt(tmin)]]),
                  F, [(m * v / tmin, "Change minutes into seconds before working out the deceleration."), (m * v / (cruise * 60), "The cruising time does not matter; use the braking time."),
                      (m * v, "That is not a force: divide by the time to get the deceleration first.")], "N", "a = (v − u) ÷ t,  F = m a",
                  [f"braking time = {fmt(tmin)} × 60 = {fmt(tmin * 60)} s", f"deceleration = {v} ÷ {fmt(tmin * 60)} = {fmt(a)} m/s²",
                   f"F = {m} × {fmt(a)} = **{fmt(F)} N**", src("SEAB O-Level 2021 MCQ 4")],
                  ["Only the braking part matters.", "Deceleration = change in speed ÷ time, with time in seconds.", "Then F = m a."])
