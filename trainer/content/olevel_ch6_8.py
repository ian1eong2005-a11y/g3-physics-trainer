"""O level 2026 MCQ practice, Ch 6-8 (Energy; Kinetic Particle Model; Thermal Processes): adapted SEAB O-Level MCQs on
learning outcomes the 2026 Paper 2 (Q1-7) did not test. Chapter 5 has none: its outcomes were tested in Q5."""
import math

from .. import sketches, sketches3 as k3
from ..config import G
from .base import calc_q, explain_mcqs, fmt, md_table, nice, template

CAT = "olevel"


def src(text):
    return f"_Adapted from {text}._"


# ================================================================== Ch 6 Energy
explain_mcqs([
    dict(id="o26_bounce_chain", chapter=6, level=2, lo="6a", source="SEAB O-Level 2014 MCQ 5",
         stem="A tennis ball is dropped from a window. It falls, hits the ground, squashes and bounces back up. Which sequence of energy stores is correct, from the moment it is dropped until it leaves the ground?",
         correct="gravitational potential → kinetic → elastic potential → kinetic",
         wrongs={"kinetic → gravitational potential → elastic potential → kinetic": "At the start the ball is at rest at a height: its energy is gravitational potential.",
                 "gravitational potential → elastic potential → kinetic → gravitational potential": "The ball gains kinetic energy as it falls BEFORE it squashes.",
                 "gravitational potential → kinetic → chemical potential → kinetic": "Squashing the ball stores elastic, not chemical, potential energy."},
         hints=["What store does a raised, stationary ball have?", "What happens to its speed as it falls?", "When it squashes, energy is stored in its shape."]),
    dict(id="o26_not_potential", chapter=6, level=1, lo="6a", source="SEAB O-Level 2016 MCQ 7",
         stem="Which is **not** a potential energy store?",
         correct="kinetic", wrongs={"chemical": "Chemical energy is a potential store (in fuel, food, batteries).",
                                    "elastic": "Elastic energy is a potential store (stretched or squashed objects).",
                                    "gravitational": "Gravitational energy is a potential store (raised objects)."},
         hints=["Potential stores are energy held because of position, shape or arrangement.", "The syllabus lists gravitational, chemical and elastic potential stores.",
                "Which store depends on motion instead?"]),
    dict(id="o26_wind_turbine", chapter=6, level=1, lo="6a", source="SEAB O-Level 2018 MCQ 8",
         stem="Which device is designed to transfer energy from a kinetic store into energy transferred electrically?",
         correct="a wind turbine", wrongs={"an electric fan": "A fan does the opposite: electrical energy to kinetic energy.",
                                           "an electric kettle": "A kettle transfers electrical energy to the internal store of water.",
                                           "a battery-powered torch": "A torch transfers chemical energy to electrical and then light."},
         hints=["Where does the moving (kinetic) energy come from?", "The device must OUTPUT electrical energy.", "Moving air turns its blades."]),
    dict(id="o26_closed_system", chapter=6, level=1, lo="6c", source="SEAB O-Level 2020 MCQ 7",
         stem="Energy is transferred between stores inside a closed system. Which statement about the total energy of the system is correct?",
         correct="It stays the same.", wrongs={"It decreases.": "Energy cannot be destroyed (principle of conservation of energy).",
                                               "It increases.": "Energy cannot be created.", "It becomes zero.": "The energy is still there, in other stores."},
         hints=["Recall the principle of conservation of energy.", "Energy is neither created nor destroyed.", "A closed system exchanges no energy with the outside."]),
    dict(id="o26_bungee", chapter=6, level=1, lo="6a", source="SEAB specimen 2024 MCQ 6",
         stem="A bungee jumper falls from a bridge with increasing speed before the cord starts to stretch. What is the main energy transfer during this time?",
         correct="gravitational potential store to kinetic store",
         wrongs={"kinetic store to gravitational potential store": "The jumper is going DOWN and speeding up.",
                 "kinetic store to internal store": "The jumper's speed is increasing, so the kinetic store is filling, not emptying.",
                 "gravitational potential store to elastic potential store": "The cord has not started to stretch yet."},
         hints=["Height is decreasing.", "Speed is increasing.", "Which store empties and which fills?"]),
], category=CAT)


@template("o26_car_sand", chapter=6, level=3, lo="6d", category=CAT)
def car_sand(rng):
    m, v, F = nice(rng, (800, 10, 2000), (1200, 10, 2500), (1000, 12, 3600), (900, 10, 1800), (1200, 15, 4500))
    KE = 0.5 * m * v * v
    d = KE / F
    return calc_q(rng, f"A car of mass **{m} kg** moving at **{v} m/s** runs into a bed of sand, which exerts a constant stopping force of **{F} N**. How far does the car travel into the sand?\n\n"
                  + md_table(["mass / kg", "speed / m/s", "stopping force / N"], [[m, v, F]]),
                  d, [(m * v / F, "Use the kinetic energy ½mv², not mv."), (m * v * v / F, "You forgot the ½ in ½mv²."), (0.5 * m * v / F, "Square the speed in ½mv².")],
                  "m", "work done by the force = kinetic energy lost;  F d = ½ m v²",
                  [f"KE = ½ × {m} × {v}² = {fmt(KE)} J", f"F d = KE → d = {fmt(KE)} ÷ {F} = **{fmt(d)} m**", src("SEAB O-Level 2014 MCQ 6")],
                  ["All the kinetic energy is removed by the sand.", "Work done by the stopping force = force × distance.", "Set F d = ½ m v²."])


@template("o26_push_power", chapter=6, level=2, lo="6e", category=CAT)
def push_power(rng):
    F = nice(rng, 200, 250, 400)
    W = nice(rng, 500, 800)
    d = nice(rng, 2.0, 4.0, 5.0)
    t = nice(rng, 10, 20, 25)
    P = F * d / t
    return calc_q(rng, f"A force of **{F} N** pushes a box of weight {W} N a distance of **{fmt(d)} m** along a level floor in **{t} s** (Fig. 1). What is the average power used to move the box?",
                  P, [(W * d / t, "The box moves sideways: use the push, not the weight."), (F * d, "That is the work done; divide by the time."),
                      (F * t / d, "Power = work ÷ time = F d ÷ t.")], "W", "power = work done ÷ time = F d ÷ t",
                  [f"work = {F} × {fmt(d)} = {fmt(F * d)} J", f"power = {fmt(F * d)} ÷ {t} = **{fmt(P)} W**", src("SEAB O-Level 2015 MCQ 7 and 2019 MCQ 7")],
                  ["Work done = force × distance moved in the direction of the force.", "Which force acts along the motion?", "Power = work ÷ time."],
                  figure=sketches.push_sketch(f"{F} N", f"{fmt(d)} m", body_label=f"{W} N"))


@template("o26_bullet_ke_lost", chapter=6, level=3, lo="6b", category=CAT)
def bullet_ke_lost(rng):
    m = nice(rng, 0.020, 0.040, 0.050)
    v1 = nice(rng, 400, 450, 600)
    v2 = nice(rng, 100, 150, 200, 300)
    lost = 0.5 * m * (v1 ** 2 - v2 ** 2)
    return calc_q(rng, f"A bullet of mass **{fmt(m)} kg** passes through a block of wood and slows from **{v1} m/s** to **{v2} m/s**. How much kinetic energy does it lose?\n\n"
                  + md_table(["", "speed / m/s"], [["before", v1], ["after", v2]]),
                  lost, [(0.5 * m * (v1 - v2) ** 2, "You squared the change in speed. Find each KE and subtract."), (m * (v1 ** 2 - v2 ** 2), "You forgot the ½."),
                         (0.5 * m * v1 ** 2, "That is the KE at the start; subtract the KE left at the end.")], "J", "Ek = ½ m v²",
                  [f"KE before = ½ × {fmt(m)} × {v1}² = {fmt(0.5 * m * v1 ** 2)} J", f"KE after = ½ × {fmt(m)} × {v2}² = {fmt(0.5 * m * v2 ** 2)} J",
                   f"lost = **{fmt(lost)} J**", src("SEAB O-Level 2016 MCQ 8")],
                  ["Work out the kinetic energy before and after.", "KE depends on v², so you cannot just use the change in speed.", "Subtract."])


@template("o26_ball_over_hump", chapter=6, level=4, lo="6c", category=CAT)
def ball_over_hump(rng):
    h, v = nice(rng, (45, 3.0), (20, 2.0), (80, 4.0), (125, 5.0))
    hy = nice(rng, *(x for x in (10, 15, 20, 30) if x < h))
    return calc_q(rng, f"A ball rolls from X along the track in Fig. 1. It must get over the hump, **{h} cm** high, to reach Y, which is {hy} cm above X. "
                  "Assume no energy is lost and g = 10 N/kg. What is the minimum speed the ball must have at X?",
                  v, [(math.sqrt(2 * G * hy / 100), "Y is not the highest point: the ball must first get over the hump."),
                      (math.sqrt(2 * G * (h - hy) / 100), "Use the full height of the hump above X."),
                      (math.sqrt(G * h / 100), "Use ½ v² = g h, so v = √(2 g h).")], "m/s", "½ m v² = m g h  →  v = √(2 g h)",
                  [f"h = {h} cm = {fmt(h / 100)} m (the hump, the highest point)", f"v = √(2 × 10 × {fmt(h / 100)}) = **{fmt(v)} m/s**", src("SEAB O-Level 2017 MCQ 8")],
                  ["The kinetic energy at X must be enough to reach the highest point.", "½ m v² = m g h: the mass cancels.", "Change cm to m."],
                  figure=k3.hill_track(f"{h} cm", f"{hy} cm"), sf=2)


@template("o26_walk_uphill_power", chapter=6, level=2, lo="6e", category=CAT)
def walk_uphill_power(rng):
    W = nice(rng, 500, 600, 720)
    h = nice(rng, 6, 9, 12, 15)
    P = W * h / 60
    return calc_q(rng, f"A hiker of weight **{W} N** walks uphill and rises **{h} m** vertically every minute (Fig. 1). What useful power does the hiker produce?",
                  P, [(W * h, "That is the work done each minute; divide by 60 s."), (W * h / 3600, "One minute is 60 s, not 3600 s."),
                      (W / h, "Power = work ÷ time = W h ÷ t.")], "W", "power = gain in GPE ÷ time = W h ÷ t",
                  [f"work against gravity each minute = {W} × {h} = {W * h} J", f"P = {W * h} ÷ 60 = **{fmt(P)} W**", src("SEAB O-Level 2018 MCQ 9")],
                  ["Useful work = weight × height gained.", "Use the height gained in one minute.", "Divide by 60 s."],
                  figure=sketches.slope_sketch(f"{h} m every minute", top_label="hiker"))


@template("o26_spring_energy", chapter=6, level=4, lo="6c", category=CAT)
def spring_energy(rng):
    a = nice(rng, 8.0, 9.0, 10.0)
    b = nice(rng, 1.0, 1.5, 2.0)
    d = nice(rng, 4.0, 5.0, 6.0)
    c = nice(rng, 1.2, 1.8, 2.4)
    e = a + b - c - d
    return calc_q(rng, "A mass on a spring oscillates up and down (Fig. 1). No energy is lost.\n\n"
                  + md_table(["position", "kinetic / J", "gravitational potential / J", "elastic potential / J"],
                             [["top of the motion", "0", fmt(a), fmt(b)], ["another position", fmt(c), fmt(d), "?"]])
                  + "\n\nWhat is the elastic potential energy at the other position?",
                  e, [(a - c - d, "You left out the elastic energy at the top: the total is ALL three stores."), (a + b - c, "Subtract the gravitational potential energy as well."),
                      (b + c, "The total energy stays constant: find it first.")], "J", "total energy is constant",
                  [f"total = 0 + {fmt(a)} + {fmt(b)} = {fmt(a + b)} J", f"elastic = {fmt(a + b)} − {fmt(c)} − {fmt(d)} = **{fmt(e)} J**", src("SEAB O-Level 2020 MCQ 8")],
                  ["Find the total energy at the top.", "The total is the same at every position.", "Subtract the stores you know."],
                  figure=k3.mass_on_spring(), sf=2)


@template("o26_windlass_work", chapter=6, level=5, lo="6d", category=CAT)
def windlass_work(rng):
    D = nice(rng, 160, 200, 250)
    n = nice(rng, 8, 10, 12)
    Wt = nice(rng, 50, 60, 80)
    L = nice(rng, 100, 120, 150)
    h = n * math.pi * D / 1000
    work = Wt * h
    return calc_q(rng, f"A bucket of weight **{Wt} N** is lifted by a rope wound round a cylinder of diameter **{D} mm**. The cylinder is turned by a handle {L} mm long (Fig. 1). "
                  f"The handle is turned through **{n} complete turns**. How much work is done on the bucket?",
                  work, [(Wt * n * math.pi * L / 1000, "The rope winds round the CYLINDER, not the handle."), (Wt * n * math.pi * D / 2000, "Use the circumference π × diameter, not π × radius."),
                         (Wt * n * D / 1000, "Each turn winds one circumference (π d) of rope.")], "J", "work = force × distance;  rope wound per turn = π d",
                  [f"rope wound = {n} × π × {fmt(D / 1000)} m = {fmt(h)} m", f"work = {Wt} × {fmt(h)} = **{fmt(work)} J**", src("SEAB O-Level 2021 MCQ 3")],
                  ["How far does the bucket rise in one turn?", "One turn winds one circumference of the cylinder.", "Work = weight × height lifted."],
                  figure=k3.windlass(f"{D} mm", f"handle {L} mm", f"{Wt} N"))


@template("o26_cyclist_slope", chapter=6, level=5, lo="6e", category=CAT)
def cyclist_slope(rng):
    W = nice(rng, 700, 750, 800)
    s = nice(rng, 60, 80, 100)
    t = nice(rng, 4.0, 5.0, 8.0)
    kk = nice(rng, 20, 25, 40)
    h = s / kk
    P = W * h / t
    return calc_q(rng, f"A cyclist of weight **{W} N** rides **{s} m** along a road at constant speed in **{fmt(t)} s**. The road (Fig. 1) rises **1.0 m for every {kk} m** along it. "
                  "Ignore friction. What average power does the cyclist produce?",
                  P, [(W * s / t, "Use the height gained, not the distance along the road."), (W * h, "That is the work; divide by the time."),
                      (W * kk / t, "Height gained = distance ÷ " + str(kk) + ".")], "W", "power = W h ÷ t",
                  [f"height gained = {s} ÷ {kk} = {fmt(h)} m", f"work = {W} × {fmt(h)} = {fmt(W * h)} J", f"P = {fmt(W * h)} ÷ {fmt(t)} = **{fmt(P)} W**",
                   src("SEAB O-Level 2021 MCQ 7")],
                  ["At constant speed the only work is against gravity.", "Find the vertical height gained.", "Power = work ÷ time."],
                  figure=sketches.slope_sketch(f"1.0 m rise per {kk} m", top_label="cyclist"))


@template("o26_stairs_power", chapter=6, level=2, lo="6e", category=CAT)
def stairs_power(rng):
    W = nice(rng, 500, 550, 650)
    h = nice(rng, 3.0, 4.5, 6.0)
    t = nice(rng, 2.5, 3.0, 5.0)
    P = W * h / t
    return calc_q(rng, f"A student of weight **{W} N** runs up a staircase of total height **{fmt(h)} m** in **{fmt(t)} s**. What power is needed?\n\n"
                  + md_table(["weight / N", "height / m", "time / s"], [[W, fmt(h), fmt(t)]]),
                  P, [(W * h, "That is the work; divide by the time."), (W * t / h, "Power = W h ÷ t."), (W * h * t, "Divide by the time; do not multiply.")],
                  "W", "power = work ÷ time = W h ÷ t",
                  [f"work = {W} × {fmt(h)} = {fmt(W * h)} J", f"P = {fmt(W * h)} ÷ {fmt(t)} = **{fmt(P)} W**", src("SEAB specimen 2024 MCQ 7")],
                  ["Work against gravity = weight × height.", "Power = work ÷ time.", f"Divide by {fmt(t)} s."])


# ================================================================== Ch 7 Kinetic particle model
explain_mcqs([
    dict(id="o26_temperature_ke", chapter=7, level=1, lo="7c", source="SEAB O-Level 2014 MCQ 7",
         stem="The temperature of a substance is linked to which energy of its particles?",
         correct="their average kinetic energy",
         wrongs={"their potential energy": "Potential energy of particles changes during melting and boiling, at constant temperature.",
                 "their chemical energy": "Chemical energy is stored in bonds within molecules, not linked to temperature.",
                 "their nuclear energy": "Nuclear energy is stored in the nucleus."},
         hints=["When a body warms up, its particles move faster.", "Faster motion means more kinetic energy.", "Temperature measures the AVERAGE of this."]),
    dict(id="o26_liquid_heated_not", chapter=7, level=2, lo="7b", source="SEAB O-Level 2015 MCQ 8 and 2020 MCQ 9",
         stem="A liquid is heated. Which statement about its molecules is **not** correct?",
         correct="The molecules themselves get bigger.",
         wrongs={"The molecules move faster.": "This is TRUE, so it is not the answer.",
                 "The molecules gain energy.": "This is TRUE, so it is not the answer.",
                 "On average, the molecules move further apart.": "This is TRUE (the liquid expands), so it is not the answer."},
         hints=["Three of the statements are true.", "A liquid expands when heated. Why?", "The spaces between molecules grow; the molecules do not."]),
    dict(id="o26_liquid_ke", chapter=7, level=2, lo="7c", source="SEAB O-Level 2017 MCQ 9",
         stem="Which statement is correct?",
         correct="In a liquid, the average kinetic energy of the molecules increases as the temperature rises.",
         wrongs={"The molecules in a gas are closer together than in a liquid.": "Gas molecules are much FURTHER apart.",
                 "The molecules in a solid are much further apart than in a liquid.": "Solid and liquid molecules are both closely packed.",
                 "In a solid, the molecules move freely around each other.": "Solid molecules only vibrate about fixed positions."},
         hints=["Picture the arrangement in a solid, a liquid and a gas.", "What does a rise in temperature do to the particles?", "Rule out the arrangement statements first."]),
    dict(id="o26_solidify", chapter=7, level=2, lo="7e", source="SEAB O-Level 2017 MCQ 10 and 2020 MCQ 11",
         stem="Molten lead is poured into a mould. It cools to its melting point and starts to solidify. While it solidifies, which statement is correct?",
         correct="Its temperature stays the same and energy is transferred from the lead to the surroundings.",
         wrongs={"Its temperature falls and energy is transferred from the lead to the surroundings.": "During a change of state the temperature stays constant.",
                 "Its temperature stays the same and no energy is transferred to the surroundings.": "Energy IS released as the particles bond into a solid.",
                 "Its temperature falls and no energy is transferred to the surroundings.": "Both parts are wrong: constant temperature, and energy is given out."},
         hints=["What happens to the temperature during a change of state?", "Solidifying: particles come together into fixed positions.", "That releases energy."]),
    dict(id="o26_solid_vibrate", chapter=7, level=1, lo="7b", source="SEAB O-Level 2019 MCQ 8",
         stem="Which statement about solids, liquids and gases is correct?",
         correct="In a solid, the particles vibrate about fixed positions.",
         wrongs={"In a gas, the particles move slowly downwards because of gravity.": "Gas particles move quickly and randomly in all directions.",
                 "In a liquid, the particles move in only a few directions.": "Liquid particles move randomly in all directions, sliding past each other.",
                 "Liquids and gases can both be compressed easily.": "Liquids are hard to compress: their particles are close together."},
         hints=["Recall how particles move in each state.", "Which state can be squashed easily?", "Which state has particles in fixed positions?"]),
    dict(id="o26_piston_gas", chapter=7, level=3, lo="7b", source="SEAB specimen 2024 MCQ 8",
         stem="Some gas is trapped in a cylinder by a frictionless piston (Fig. 1). The temperature of the gas is raised. Which statement is correct?",
         correct="The gas expands and pushes the piston outwards.",
         wrongs={"The molecules get larger.": "Molecules do not change size; they move faster and hit the piston harder.",
                 "The piston stays where it is.": "The faster molecules push harder on the piston, and it is free to move.",
                 "The molecules move more slowly.": "Higher temperature means faster molecules."},
         hints=["What happens to molecular speed when the temperature rises?", "Faster molecules hit the piston more often and harder.", "The piston is free to move."],
         figure=k3.piston_gas),
], category=CAT)


# ================================================================== Ch 8 Thermal processes
explain_mcqs([
    dict(id="o26_tank_top_heater", chapter=8, level=3, lo="8e", source="SEAB O-Level 2016 MCQ 9",
         stem="The water at the top of an insulated tank is heated by a heater near the top (Fig. 1). No water enters or leaves. Why does the water at the bottom stay cold for a long time?",
         correct="Water is a poor conductor of heat.",
         wrongs={"Cold water at the top sinks to the bottom.": "The water at the top is HOT and less dense: it stays at the top, so there is no convection downwards.",
                 "Hot water at the bottom rises to the top.": "The heater is at the top: the water at the bottom is cold, not hot.",
                 "The insulation is a poor conductor of heat.": "The insulation stops energy leaving the tank; it does not explain why the bottom stays cold."},
         hints=["Hot water is less dense and stays at the top.", "So convection cannot carry energy downwards.", "The only way down is conduction through the water."],
         figure=lambda: k3.water_tank("top")),
    dict(id="o26_radiation_not", chapter=8, level=2, lo="8d", source="SEAB O-Level 2018 MCQ 10",
         stem="The rate at which a hot object loses energy by radiation depends on several factors. Which does **not** affect it?",
         correct="the pressure of the surrounding air",
         wrongs={"the colour of its surface": "Dull black surfaces radiate faster than shiny white ones.",
                 "its surface area": "A larger surface area radiates energy faster.",
                 "its surface temperature": "A hotter surface radiates energy faster."},
         hints=["Radiation needs no medium.", "The syllabus factors are colour and texture, temperature and surface area.", "Which option is about the surroundings, not the surface?"]),
    dict(id="o26_radiation_per_m2", chapter=8, level=3, lo="8d", source="SEAB O-Level 2020 MCQ 10",
         stem="A heated surface loses energy by radiation. Which of these does **not** affect the energy lost **per square metre** of the surface?",
         correct="the area of the surface",
         wrongs={"the colour of the surface": "Colour affects radiation from every square metre.",
                 "the texture of the surface": "Shiny smooth surfaces radiate less than dull rough ones.",
                 "the temperature of the surface": "Hotter surfaces radiate more from every square metre."},
         hints=["Read the question carefully: PER square metre.", "A bigger area loses more in total, but the same amount per square metre.", "The other three change every square metre."]),
    dict(id="o26_trapped_air", chapter=8, level=2, lo="8e", source="SEAB O-Level 2021 MCQ 8",
         stem="Why does a jacket filled with fibres that trap air keep you warm?",
         correct="Air is a poor conductor, and trapping it reduces energy transfer by convection.",
         wrongs={"Air is a good conductor, and trapping it reduces energy transfer by convection.": "Air is a POOR conductor.",
                 "Air is a poor conductor, and trapping it increases energy transfer by convection.": "Trapped air cannot circulate, so convection is reduced.",
                 "Air is a good conductor, and trapping it increases energy transfer by convection.": "Both parts are wrong."},
         hints=["Is air a good or a poor conductor?", "Convection needs the fluid to move.", "What happens when the air cannot move?"]),
], category=CAT)
