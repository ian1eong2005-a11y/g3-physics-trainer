"""O level 2026 MCQ practice, Ch 1-5: the remaining SEAB Ten-Year-Series MCQs in the 5086 syllabus (added 31 Oct 2026).
Same context, skill and answer logic as the SEAB question; figures redrawn; numbers changed slightly and varied on every serve."""
from .. import figs, sketches, sketches4 as k4
from .base import calc_q, explain_mcqs, fmt, md_table, nice, template, text_options

CAT = "olevel"


def src(text):
    return f"_Adapted from {text}._"


# ================================================================== Ch 1 Measurement
explain_mcqs([
    dict(id="o26t_earth_order", chapter=1, level=1, lo="1d", source="SEAB O-Level 2015 MCQ 1",
         stem="What is the order of magnitude of the diameter of the Earth?",
         correct="1 × 10⁷ m",
         wrongs={"1 × 10³ m": "10³ m is 1 km: about the size of a small town.",
                 "1 × 10⁵ m": "10⁵ m is 100 km: about the width of a small country.",
                 "1 × 10⁹ m": "10⁹ m is about the diameter of the Sun, a hundred times the Earth's."},
         hints=["The Earth's diameter is about 12 700 km.", "Change km into m: 12 700 km = 12 700 000 m.",
                "Round 1.27 × 10⁷ m to the nearest power of ten."]),
    dict(id="o26t_base_quantity", chapter=1, level=1, lo="1b", source="SEAB O-Level 2021 MCQ 1",
         stem="Which quantity is a base quantity?",
         correct="temperature",
         wrongs={"area": "Area is derived from length × length (m²).",
                 "speed": "Speed is derived from length ÷ time (m/s).",
                 "weight": "Weight is a force, derived from mass, length and time (N = kg m/s²)."},
         hints=["The base quantities are mass, length, time, current, temperature and amount of substance.",
                "A derived quantity is made by combining base quantities.", "Which option is on the list of base quantities?"]),
    dict(id="o26t_pendulum_later", chapter=1, level=3, lo="1e", source="SEAB O-Level 2015 MCQ 2",
         stem="A pendulum has a period of **0.80 s**. Fig. 1 shows the moment a stopwatch is started: the pendulum is vertical "
              "and moving to the right. Where is the pendulum, and which way is it moving, **2.0 s** later?",
         correct="vertical, moving to the left",
         wrongs={"vertical, moving to the right": "That would be after a whole number of periods. 2.0 s is 2.5 periods.",
                 "at the right-hand end of its swing": "That is a quarter of a period after the start, plus whole periods; 2.5 periods is a half more.",
                 "at the left-hand end of its swing": "That is three-quarters of a period after the start, plus whole periods."},
         hints=["How many periods is 2.0 s? Divide by 0.80 s.", "After 2 whole periods it is back where it started.",
                "Half a period more: it passes through the middle again, but going the other way."],
         figure=lambda: k4.pendulum_start()),
], category=CAT)


@template("o26t_stopwatch_lap", chapter=1, level=1, lo="1e", category=CAT)
def stopwatch_lap(rng):
    m1, s1, m2, s2 = nice(rng, (1, 48, 2, 35), (1, 52, 2, 40), (1, 15, 2, 5), (1, 38, 2, 21))   # seconds borrow, as in the SEAB item
    lap2 = (m2 * 60 + s2) - (m1 * 60 + s1)
    t2 = m2 * 60 + s2

    def ms(t):
        return f"{t // 60} min {t % 60:02d} s"
    correct = ms(lap2)
    wrongs = {ms(m1 * 60 + s1): "That is the time for the FIRST lap (start to first reading).",
              ms(t2): "That is the total time for both laps.",
              ms((m2 - m1) * 60 + abs(s2 - s1)): "Subtract minutes and seconds together: change both readings into seconds first."}
    wrongs = {k: v for k, v in wrongs.items() if k != correct}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem="A student times a runner who runs two laps of a track. Fig. 1 shows the stopwatch at the start, at the end of the "
                     "first lap and at the end of the second lap. What is the time taken for the **second** lap?",
                figure=k4.side_by_side([figs.stopwatch("00:00"), figs.stopwatch(f"{m1:02d}:{s1:02d}"), figs.stopwatch(f"{m2:02d}:{s2:02d}")],
                                       ["start", "end of lap 1", "end of lap 2"], width=6.6),
                options=opts, key=key, misconceptions=mis, formula="time for lap 2 = reading at end of lap 2 − reading at end of lap 1",
                working=[f"end of lap 2 = {t2} s, end of lap 1 = {m1 * 60 + s1} s", f"lap 2 = {t2} − {m1 * 60 + s1} = {lap2} s = **{correct}**",
                         src("SEAB 5086 specimen paper 2024 MCQ 1")],
                hints=["The second lap starts when the first lap ends.", "Change both readings into seconds.", "Subtract."])


@template("o26t_micrometer_vernier", chapter=1, level=3, lo="1e", category=CAT)
def micrometer_vernier(rng):
    m, v = nice(rng, (5.68, 2.4), (7.42, 1.6), (6.27, 3.5), (4.83, 2.8))
    c = f"micrometer {fmt(m, dp=2)} mm, vernier caliper {fmt(v, dp=1)} mm"
    wrongs = {f"micrometer {fmt(m + 0.5, dp=2)} mm, vernier caliper {fmt(v, dp=1)} mm": "Check the half-millimetre marks on the micrometer sleeve: read the last mark showing, not the next one.",
              f"micrometer {fmt(m, dp=2)} mm, vernier caliper {fmt(v + 1, dp=1)} mm": "On the vernier, read the main scale at the ZERO of the vernier scale, not at the end of it.",
              f"micrometer {fmt(m + 0.5, dp=2)} mm, vernier caliper {fmt(v + 1, dp=1)} mm": "Both main-scale readings are 1 step too high."}
    opts, key, mis = text_options(rng, c, wrongs)
    return dict(stem="Fig. 1 shows the scales of a micrometer screw gauge and of a vernier caliper. What are the two readings?",
                figure=k4.stacked([figs.micrometer(m), figs.vernier(v)], ["micrometer screw gauge", "vernier caliper"]),
                options=opts, key=key, misconceptions=mis, formula="reading = main scale + thimble (or vernier) scale",
                working=[f"micrometer: sleeve {fmt(int(m * 2) / 2, dp=1)} mm + thimble {fmt(round((m - int(m * 2) / 2) * 100))} × 0.01 mm = **{fmt(m, dp=2)} mm**",
                         f"vernier: main scale {int(v)} mm + vernier line {round((v - int(v)) * 10)} × 0.1 mm = **{fmt(v, dp=1)} mm**",
                         src("SEAB O-Level 2020 MCQ 2")],
                hints=["Micrometer: the sleeve gives whole and half millimetres; the thimble gives hundredths.",
                       "Vernier: read the main scale at the vernier's zero, then find the vernier line that lines up exactly.",
                       "Add the two parts for each instrument."])


@template("o26t_vernier_extension", chapter=1, level=4, lo="1e", category=CAT)
def vernier_extension(rng):
    before, after_mm = nice(rng, (0.71, 12.4), (0.86, 14.1), (0.62, 9.5), (0.94, 15.2))
    after = after_mm / 10
    ext = after - before
    return calc_q(rng, f"A vernier scale measures the stretch of a wire. Before a mass is hung on the wire the reading is **{fmt(before, dp=2)} cm**. "
                       "Fig. 1 shows the reading after the mass is hung on the wire (scale in mm). What is the extension caused by the mass?",
                  ext, [(after, "That is the reading after the mass is added. Subtract the reading before."),
                        (after + before, "Extension is the DIFFERENCE between the readings, not the sum."),
                        (int(after_mm) / 10 - before, "Add the vernier part: the reading is main scale + vernier.")],
                  "cm", "extension = reading after − reading before",
                  [f"reading after = {fmt(after_mm, dp=1)} mm = {fmt(after, dp=2)} cm", f"extension = {fmt(after, dp=2)} − {fmt(before, dp=2)} = **{fmt(ext, dp=2)} cm**",
                   src("SEAB O-Level 2014 MCQ 1")],
                  ["Read the vernier: main scale at the zero, plus the vernier line that lines up.", "Change mm into cm.", "Subtract the first reading."],
                  figure=figs.vernier(after_mm), dp=2)


# ================================================================== Ch 3 Force and pressure, Ch 4 Dynamics
explain_mcqs([
    dict(id="o26t_cement_board", chapter=3, level=1, lo="3i", source="SEAB 5086 specimen paper 2024 MCQ 5",
         stem="To stop a heavy concrete mixer sinking into soft ground, it is stood on a large flat board. Why does this work?",
         correct="The large area decreases the pressure on the ground.",
         wrongs={"The large area increases the pressure on the ground.": "Pressure = force ÷ area: a larger area gives a SMALLER pressure.",
                 "The large area decreases the weight on the ground.": "The board does not change the mixer's weight (it adds a little).",
                 "The large area increases the weight on the ground.": "Sinking depends on the pressure, not just the weight."},
         hints=["Write the formula for pressure.", "The force (weight) stays about the same.", "What happens to F ÷ A when A gets bigger?"]),
    dict(id="o26t_bed_of_nails", chapter=3, level=2, lo="3i", source="SEAB O-Level 2017 MCQ 7",
         stem="A performer lies on a board with hundreds of sharp nails pointing upwards, and is not hurt. Which statement explains this?",
         correct="The weight is spread over a large total area, which decreases the pressure.",
         wrongs={"The weight is spread over a small area, which decreases the pressure.": "Hundreds of nail points together make a LARGE total area.",
                 "The weight is spread over a large total area, which increases the pressure.": "A larger area means a smaller pressure (p = F ÷ A).",
                 "The weight is spread over a small area, which increases the pressure.": "A large pressure would pierce the skin. Here the pressure is small."},
         hints=["One nail would hurt: all the weight on one tiny point.", "With hundreds of nails, what happens to the total area?",
                "p = F ÷ A."]),
    dict(id="o26t_forces_constant_up", chapter=4, level=2, lo="4a", source="SEAB O-Level 2016 MCQ 3",
         stem="Fig. 1 shows four forces P, Q, R and S acting on an object. The object moves vertically **upwards at a constant speed**. "
              "Which statement **must** be correct?",
         correct="Q and S are equal in size, and P and R are equal in size.",
         wrongs={"All four forces are the same size.": "Only opposite pairs must balance. P and R need not equal Q and S.",
                 "P and R are equal in size, but both are larger than Q and S.": "Nothing says how the vertical forces compare with the horizontal ones.",
                 "Q and S are equal in size, but P is larger than R.": "Constant speed means NO resultant force, so P must equal R, even though it moves up."},
         hints=["Constant speed in a straight line: is there a resultant force?", "Newton's first law: balanced forces → no change in motion.",
                "Each pair of opposite forces must cancel."],
         figure=lambda: figs.force_diagram([("P", "up", 1.0), ("Q", "right", 1.0), ("R", "down", 1.0), ("S", "left", 1.0)], ground=False)),
    dict(id="o26t_rocket_fbd", chapter=4, level=2, lo="4b", source="SEAB O-Level 2017 MCQ 3",
         stem="A rocket is travelling vertically **upwards** through the air. Which describes the directions of the forces on it?",
         correct="thrust upwards; weight and air resistance downwards",
         wrongs={"thrust and air resistance upwards; weight downwards": "Air resistance opposes the motion. The rocket moves up, so air resistance acts DOWN.",
                 "weight and air resistance upwards; thrust downwards": "Weight always acts towards the Earth (down), and the thrust drives the rocket up.",
                 "air resistance upwards; thrust and weight downwards": "The thrust pushes the rocket the way it is going: up."},
         hints=["Weight always acts towards the centre of the Earth.", "Air resistance acts opposite to the direction of motion.",
                "Thrust pushes the rocket forwards."]),
    dict(id="o26t_car_f_equals_r", chapter=4, level=1, lo="4a", source="SEAB O-Level 2018 MCQ 3",
         stem="A car is moving forwards. The forward force F on it is equal to the resistive force R. Which statement is correct?",
         correct="The car moves with uniform (constant) velocity.",
         wrongs={"The car moves with uniform acceleration.": "Acceleration needs a resultant force. Here F − R = 0.",
                 "The car moves with non-uniform acceleration.": "With no resultant force there is no acceleration at all.",
                 "The car is slowing down to a stop.": "Slowing down needs R to be larger than F."},
         hints=["Find the resultant force: F − R.", "What does a resultant force of zero do to a moving object?",
                "Newton's first law."]),
], category=CAT)


@template("o26t_nail_cork", chapter=3, level=3, lo="3i", category=CAT)
def nail_cork(rng):
    p1, a1, a2 = nice(rng, (0.25, 120, 15), (0.40, 90, 12), (0.20, 150, 25), (0.30, 100, 12))
    F = p1 * a1
    p2 = F / a2
    return calc_q(rng, "A student pushes a nail into a cork with a hand (table). What pressure does the point of the nail exert on the cork?\n\n"
                  + md_table(["quantity", "value"], [["pressure of the hand on the nail head", f"{fmt(p1)} N/mm²"],
                                                     ["area of the nail head", f"{a1} mm²"], ["area of the nail point", f"{a2} mm²"]]),
                  p2, [(p1, "The FORCE is passed on by the nail, not the pressure. The pressure changes with area."),
                       (p1 * a2 / a1, "You divided the wrong way: the point has the SMALLER area, so the pressure is larger."),
                       (F, "That is the force on the nail. Divide it by the area of the point.")],
                  "N/mm²", "F = p × A at the head; p = F ÷ A at the point",
                  [f"force = {fmt(p1)} × {a1} = {fmt(F)} N", f"pressure on the cork = {fmt(F)} ÷ {a2} = **{fmt(p2)} N/mm²**", src("SEAB O-Level 2016 MCQ 6")],
                  ["The nail passes the same FORCE from the head to the point.", "Find the force: F = p × A for the head.", "Then p = F ÷ A for the point."])


@template("o26t_toy_car_weight", chapter=3, level=2, lo="3i", category=CAT)
def toy_car_weight(rng):
    p, a = nice(rng, (2.5, 8), (4.0, 6), (3.0, 12), (4.5, 5))
    W = p * a * 4
    return calc_q(rng, "Each tyre of a four-wheeled toy car exerts a pressure on the ground (table). What is the weight of the toy car?\n\n"
                  + md_table(["quantity", "value"], [["pressure under each tyre", f"{fmt(p)} N/cm²"], ["contact area of each tyre", f"{a} cm²"]]),
                  W, [(p * a, "That is the force on ONE tyre. The car has four."), (p / a * 4, "Force = pressure × area, not pressure ÷ area."),
                      (p * a * 2, "Four tyres, not two.")],
                  "N", "F = p × A",
                  [f"force on one tyre = {fmt(p)} × {a} = {fmt(p * a)} N", f"weight = 4 × {fmt(p * a)} = **{fmt(W)} N**", src("SEAB O-Level 2018 MCQ 7")],
                  ["Rearrange p = F ÷ A.", "Find the force on one tyre.", "The weight is shared by four tyres."])


@template("o26t_plane_window", chapter=3, level=3, lo="3i", category=CAT)
def plane_window(rng):
    pin, pout, a = nice(rng, (90, 60, 0.15), (85, 55, 0.12), (75, 40, 0.20), (95, 50, 0.10))
    F = (pin - pout) * 1000 * a
    return calc_q(rng, "A window in an aeroplane has the area shown in the table. What is the resultant force on the window due to the "
                       "pressures inside and outside?\n\n"
                  + md_table(["quantity", "value"], [["area of window", f"{fmt(a)} m²"], ["pressure inside", f"{pin} kPa"], ["pressure outside", f"{pout} kPa"]]),
                  F, [(pin * 1000 * a, "That is the force from the inside air only. The outside air pushes the other way."),
                      ((pin + pout) * 1000 * a, "The two pressures push in OPPOSITE directions: subtract them."),
                      (pout * 1000 * a, "That is the force from the outside air only.")],
                  "N", "F = (p inside − p outside) × A",
                  [f"pressure difference = {pin} − {pout} = {pin - pout} kPa = {(pin - pout) * 1000} Pa",
                   f"F = {(pin - pout) * 1000} × {fmt(a)} = **{fmt(F)} N**", src("SEAB O-Level 2020 MCQ 6")],
                  ["The inside air pushes out; the outside air pushes in.", "Find the pressure difference and change kPa to Pa.", "F = p × A."])


# ================================================================== Ch 5 Turning effects
explain_mcqs([
    dict(id="o26t_equilibrium_conditions", chapter=5, level=1, lo="5c", source="SEAB 5086 specimen paper 2024 MCQ 4",
         stem="Which are the conditions for an object to be in equilibrium?",
         correct="no resultant force and no resultant turning effect",
         wrongs={"no resultant force, but a resultant turning effect": "A resultant turning effect would make the object start to rotate.",
                 "a resultant force, but no resultant turning effect": "A resultant force would make the object accelerate.",
                 "a resultant force and a resultant turning effect": "Equilibrium means BOTH the forces and the moments balance."},
         hints=["Equilibrium: no change in motion and no change in rotation.", "What would a resultant force do?",
                "What would a resultant moment do?"]),
    dict(id="o26t_topple_easily", chapter=5, level=1, lo="5e", source="SEAB O-Level 2017 MCQ 5",
         stem="A toy is designed to fall over easily when it is hit. What should it have?",
         correct="a narrow base and a high centre of gravity",
         wrongs={"a narrow base and a low centre of gravity": "A low centre of gravity makes it MORE stable.",
                 "a wide base and a high centre of gravity": "A wide base makes it MORE stable.",
                 "a wide base and a low centre of gravity": "That is the most STABLE design, the opposite of what is wanted."},
         hints=["An object topples when its weight acts outside its base.", "Which makes that happen after only a small tilt: narrow or wide base?",
                "High or low centre of gravity?"]),
    dict(id="o26t_letters_stable", chapter=5, level=2, lo="5e", source="SEAB O-Level 2019 MCQ 5",
         stem="Wooden 3-D capital letters of the same height and thickness stand upright on a table. Which letter is the most stable?",
         correct="H",
         wrongs={"I": "I has the narrowest base: a small tilt moves its centre of gravity outside the base.",
                 "Y": "Y stands on a single narrow stem with most of its mass high up.",
                 "T": "T stands on a narrow stem with a heavy bar at the top: high centre of gravity."},
         hints=["Stability: wide base, low centre of gravity.", "Look at how wide each letter is where it touches the table.",
                "Which has two feet far apart?"]),
], category=CAT)


@template("o26t_window_moment", chapter=5, level=3, lo="5b", category=CAT)
def window_moment(rng):
    W, dw, F, df = nice(rng, (120, 0.25, 40, 0.80), (80, 0.30, 30, 0.90), (150, 0.20, 35, 0.90), (90, 0.25, 30, 0.80))
    cw, acw = F * df, W * dw
    res = abs(cw - acw)
    return calc_q(rng, f"Fig. 1 shows a window pivoted along one edge. Its weight is **{W} N**, acting {fmt(dw)} m from the pivot, and it is "
                       f"pushed up with a force of **{F} N**, {fmt(df)} m from the pivot. What is the size of the resultant moment about the pivot?",
                  res, [(cw + acw, "The two moments act in OPPOSITE directions: subtract them."), (cw, "That is the moment of the push only."),
                        (acw, "That is the moment of the weight only.")],
                  "N m", "moment = force × perpendicular distance; resultant = difference of the opposing moments",
                  [f"moment of push = {F} × {fmt(df)} = {fmt(cw)} N m", f"moment of weight = {W} × {fmt(dw)} = {fmt(acw)} N m",
                   f"resultant = {fmt(max(cw, acw))} − {fmt(min(cw, acw))} = **{fmt(res)} N m**", src("SEAB O-Level 2016 MCQ 5")],
                  ["Find each moment: force × distance from the pivot.", "One turns the window up, the other down.", "Subtract."],
                  figure=sketches.beam(1.0, 0.0, [(f"{W} N", dw, "down"), (f"{F} N", df, "up")],
                                       dist_labels=[(0, dw, f"{fmt(dw)} m"), (0, df, f"{fmt(df)} m")]))


@template("o26t_plank_x", chapter=5, level=3, lo="5d", category=CAT)
def plank_x(rng):
    U, D = nice(rng, (3, 4), (2, 6), (1, 5), (3, 5))
    X = (U * 4 + D * 4) / 2
    return calc_q(rng, f"Fig. 1 shows a uniform plank pivoted at its mid-point. An upward force of **{U} N** acts at the left end, weight X hangs "
                       f"2.0 m left of the pivot and a weight of **{D} N** hangs at the right end. The plank balances. What is weight X?",
                  X, [(D * 4 / 2, "You left out the upward force. It turns the plank the same way as the right-hand weight."),
                      ((D * 4 - U * 4) / 2, "The upward force on the LEFT turns the plank clockwise, the same way as the right-hand weight."),
                      (U + D, "Balance the MOMENTS, not the forces.")],
                  "N", "principle of moments: sum of clockwise moments = sum of anticlockwise moments",
                  [f"clockwise: {U} × 4.0 + {D} × 4.0 = {U * 4 + D * 4} N m", f"anticlockwise: X × 2.0",
                   f"X = {U * 4 + D * 4} ÷ 2.0 = **{fmt(X)} N**", src("SEAB O-Level 2017 MCQ 6")],
                  ["Take moments about the pivot. The plank's own weight acts at the pivot.", "Which way does the upward force on the left turn the plank?",
                   "Clockwise moments = anticlockwise moments."],
                  figure=sketches.beam(8, 4, [(f"{U} N", 0, "up"), ("X", 2, "down"), (f"{D} N", 8, "down")],
                                       dist_labels=[(0, 2, "2.0 m"), (2, 4, "2.0 m"), (4, 8, "4.0 m")]))


@template("o26t_plank_block", chapter=5, level=2, lo="5d", category=CAT)
def plank_block(rng):
    L, dq, Q = nice(rng, (2.0, 0.80, 300), (2.5, 1.0, 450), (3.0, 1.2, 360), (2.0, 0.50, 600))
    dp = L - dq
    P = Q * dq / dp
    return calc_q(rng, f"Fig. 1 shows a light plank {fmt(L)} m long on a pivot. Block Q ({Q} N) is at one end, {fmt(dq)} m from the pivot, and "
                       "block P is at the other end. What weight must P have to keep the plank horizontal?",
                  P, [(Q * dq / L, "Measure P's distance from the PIVOT, not the full length of the plank."),
                      (Q * dp / dq, "The distances are the wrong way round: P × (its distance) = Q × (Q's distance)."), (Q, "Equal weights balance only at equal distances.")],
                  "N", "principle of moments",
                  [f"P's distance = {fmt(L)} − {fmt(dq)} = {fmt(dp)} m", f"P × {fmt(dp)} = {Q} × {fmt(dq)}", f"P = **{fmt(P)} N**",
                   src("SEAB O-Level 2019 MCQ 6")],
                  ["Find how far P is from the pivot.", "Moment = force × distance from the pivot.", "Set P's moment equal to Q's moment."],
                  figure=sketches.beam(L, dp, [("P", 0, "down"), (f"Q = {Q} N", L, "down")],
                                       dist_labels=[(0, L, f"{fmt(L)} m"), (dp, L, f"{fmt(dq)} m")]))


@template("o26t_force_at_x", chapter=5, level=4, lo="5d", category=CAT)
def force_at_x(rng):
    wl, wr = nice(rng, (16, 10), (12, 9), (20, 8), (18, 6))
    net = wr * 4 - wl * 2          # clockwise minus anticlockwise, N m
    F = abs(net) / 4
    up_or_down = "downward" if net > 0 else "upward"
    other = "upward" if net > 0 else "downward"
    correct = f"{fmt(F)} N {up_or_down}"
    wrongs = {f"{fmt(F)} N {other}": f"The extra moment must turn the plank the OTHER way to the resultant. Check which side is heavier in moments.",
              f"{fmt(2 * F)} N {up_or_down}": "X is 4 m from the pivot, not 2 m.",
              f"{fmt(abs(net))} N {up_or_down}": "That is the resultant MOMENT (N m). Divide by the distance to X."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"Fig. 1 shows a uniform plank pivoted at its mid-point, with a {wl} N weight 2 m left of the pivot and a {wr} N weight "
                     "4 m right of the pivot. A force is applied at point X, 4 m left of the pivot, to balance the plank. "
                     "What are the size and direction of this force?",
                figure=k4.plank_point_x(wl, wr),
                options=opts, key=key, misconceptions=mis, formula="principle of moments",
                working=[f"clockwise: {wr} × 4 = {wr * 4} N m; anticlockwise: {wl} × 2 = {wl * 2} N m",
                         f"unbalanced moment = {abs(net)} N m {'clockwise' if net > 0 else 'anticlockwise'}",
                         f"force at X = {abs(net)} ÷ 4 = **{fmt(F)} N**, {up_or_down} (it must turn the plank {'anticlockwise' if net > 0 else 'clockwise'})",
                         src("SEAB O-Level 2021 MCQ 6")],
                hints=["Work out the clockwise and anticlockwise moments of the two weights.", "Which way is the plank trying to turn?",
                       "The force at X must give the missing moment: size = moment ÷ 4 m."])
