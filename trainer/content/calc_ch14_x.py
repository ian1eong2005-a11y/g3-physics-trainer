"""Chapter 14 Practical Electricity: extra calculation templates (P = V I, E = P t, kWh, cost, fuses)."""
from .. import sketches2 as sk
from .base import calc_q, fmt, md_table, nice, template

MAINS = 230


# ---------------------------------------------------------------- L1
@template("c14_power_from_e_t", chapter=14, level=1, lo="14b")
def power_from_e_t(rng):
    P = nice(rng, 40, 60, 100, 500, 1200)
    t = nice(rng, 10, 20, 50, 60)
    E = P * t
    return calc_q(rng, f"Fig. 1 shows an appliance that transfers **{E} J** of energy in **{t} s**. What is its power?", P, [
        (E * t, "P = E ÷ t."),
        (t / E, "P = E ÷ t, not t ÷ E."),
        (E, "That is the energy; divide by the time."),
    ], "W", "P = E ÷ t", [f"P = {E} ÷ {t}", f"= **{fmt(P)} W**"],
        ["Power is energy transferred per second.", "P = E ÷ t.", f"{E} ÷ {t}."],
        figure=sk.rating_plate(["power = ?", f"{E} J in {t} s"]))


@template("c14_kwh_simple", chapter=14, level=1, lo="14c")
def kwh_simple(rng):
    P = nice(rng, 1, 1.5, 2, 3)
    h = nice(rng, 2, 3, 4, 5)
    return calc_q(rng, f"Fig. 1 shows the rating of a **{fmt(P)} kW** heater. It is used for **{h} hours**. How much energy does it use, in kWh?", P * h, [
        (P / h, "Energy = power × time."),
        (P * h * 1000, "With power in kW and time in h, the answer is already in kWh."),
        (P * h * 3600, "kW × h gives kWh directly; no conversion to seconds."),
    ], "kWh", "energy (kWh) = power (kW) × time (h)", [f"E = {fmt(P)} × {h}", f"= **{fmt(P * h)} kWh**"],
        ["Power in kW, time in hours.", "E = P × t.", f"{fmt(P)} × {h}."],
        figure=sk.rating_plate([f"{fmt(P)} kW", "230 V"]))


@template("c14_current_simple", chapter=14, level=1, lo="14b")
def current_simple(rng):
    P = nice(rng, 460, 690, 1150, 2300)
    I = P / MAINS
    return calc_q(rng, f"Fig. 1 shows the rating plate of an appliance: **{P} W, 230 V**. What current does it draw?", I, [
        (P * MAINS, "I = P ÷ V."),
        (MAINS / P, "I = P ÷ V, not V ÷ P."),
        (P / MAINS * 10, "Check the division: P ÷ V."),
    ], "A", "P = V I, so I = P ÷ V", [f"I = {P} ÷ 230", f"= **{fmt(I)} A**"],
        ["P = V I.", "Rearrange for I.", f"{P} ÷ 230."],
        figure=sk.rating_plate([f"{P} W", "230 V"]))


@template("c14_cost_from_units", chapter=14, level=1, lo="14c")
def cost_from_units(rng):
    units = nice(rng, 5, 10, 12, 20, 40)
    price = nice(rng, 20, 25, 30)
    cost = units * price
    table = md_table(["energy used / kWh", "price per kWh / cents"], [[units, price]])
    return calc_q(rng, f"The table shows the energy used by a family's oven in a month.\n\n{table}\n\nWhat does this cost, in cents?", cost, [
        (units / price, "Cost = number of kWh × price per kWh."),
        (price, "That is the price of ONE kWh."),
        (units + price, "Multiply, do not add."),
    ], "cents", "cost = kWh × price per kWh", [f"cost = {units} × {price}", f"= **{cost} cents**"],
        ["Each kWh costs the given price.", "Multiply the number of kWh by the price.", f"{units} × {price}."], sf=None)


# ---------------------------------------------------------------- L2
@template("c14_w_to_kw", chapter=14, level=2, lo="14c")
def w_to_kw(rng):
    P = nice(rng, 60, 100, 800, 1500, 2400)
    h = nice(rng, 5, 10, 20)
    E = P / 1000 * h
    return calc_q(rng, f"Fig. 1 shows a **{P} W** appliance. It is used for **{h} hours**. How many kWh does it use?", E, [
        (P * h, "Convert W to kW (÷ 1000) first."),
        (P * h / 100, "1 kW = 1000 W, not 100 W."),
        (P / 1000 / h, "E = P × t."),
    ], "kWh", "kWh = (W ÷ 1000) × hours", [f"P = {P} W = {fmt(P / 1000)} kW", f"E = {fmt(P / 1000)} × {h}", f"= **{fmt(E)} kWh**"],
        ["The kWh needs power in kW.", "Divide W by 1000.", "Multiply by the hours."],
        figure=sk.rating_plate([f"{P} W", "230 V"]))


@template("c14_time_from_e_p", chapter=14, level=2, lo="14b")
def time_from_e_p(rng):
    P = nice(rng, 500, 1000, 2000, 2500)
    t = nice(rng, 60, 90, 120, 300)
    E = P * t
    table = md_table(["power of kettle / W", "energy needed / J"], [[P, E]])
    return calc_q(rng, f"A kettle must supply a fixed amount of energy to boil some water.\n\n{table}\n\nHow long does this take?", t, [
        (E * P, "t = E ÷ P."),
        (P / E, "t = E ÷ P, not P ÷ E."),
        (t / 60, "That is in minutes; the answer is in seconds."),
    ], "s", "t = E ÷ P", [f"t = {E} ÷ {P}", f"= **{fmt(t)} s**"],
        ["P = E ÷ t.", "Rearrange for t.", f"{E} ÷ {P}."])


@template("c14_energy_kw_minutes", chapter=14, level=2, lo="14b")
def energy_kw_minutes(rng):
    P = nice(rng, 1.2, 1.5, 2, 3)
    m = nice(rng, 2, 3, 5, 10)
    E_kj = P * m * 60
    return calc_q(rng, f"Fig. 1 shows a **{fmt(P)} kW** hair dryer used for **{m} minutes**. How much energy does it transfer, in kJ?", E_kj, [
        (P * m, "Convert minutes to seconds (× 60)."),
        (P * m * 60 * 1000, "That is in J; the question asks for kJ (kW × s gives kJ)."),
        (P * m / 60, "Multiply by 60 to change minutes to seconds."),
    ], "kJ", "E = P × t; kW × s = kJ", [f"t = {m} × 60 = {m * 60} s", f"E = {fmt(P)} × {m * 60}", f"= **{fmt(E_kj)} kJ**"],
        ["E = P × t.", "Change minutes to seconds.", "kW × s gives kJ."],
        figure=sk.rating_plate([f"{fmt(P)} kW", "230 V"]))


@template("c14_voltage_from_p_i", chapter=14, level=2, lo="14b")
def voltage_from_p_i(rng):
    V = nice(rng, 6, 12, 24)
    I = nice(rng, 0.5, 2, 3, 4)
    P = V * I
    return calc_q(rng, f"Fig. 1 shows the label on a car accessory: **{fmt(P)} W**, drawing **{fmt(I)} A**. What p.d. does it work on?", V, [
        (P * I, "V = P ÷ I."),
        (I / P, "V = P ÷ I."),
        (P, "That is the power."),
    ], "V", "P = V I, so V = P ÷ I", [f"V = {fmt(P)} ÷ {fmt(I)}", f"= **{fmt(V)} V**"],
        ["P = V I.", "Rearrange for V.", f"{fmt(P)} ÷ {fmt(I)}."],
        figure=sk.rating_plate([f"{fmt(P)} W", f"{fmt(I)} A"]))


@template("c14_cost_dollars", chapter=14, level=2, lo="14c")
def cost_dollars(rng):
    P = nice(rng, 2, 2.5, 3)
    h = nice(rng, 4, 6, 8, 10)
    price = nice(rng, 25, 30, 32)
    cost = P * h * price / 100
    return calc_q(rng, f"Fig. 1 shows a **{fmt(P)} kW** air-conditioner. It runs for **{h} hours** and electricity costs **{price} cents per kWh**. What is the cost in dollars?", cost, [
        (P * h * price, "That is in cents; divide by 100 for dollars."),
        (P * h / price, "Cost = kWh × price."),
        (P * h, "That is the energy in kWh; multiply by the price."),
    ], "$", "kWh = kW × h; cost = kWh × price", [f"E = {fmt(P)} × {h} = {fmt(P * h)} kWh", f"cost = {fmt(P * h)} × {price} = {fmt(P * h * price)} cents", f"= **${cost:.2f}**"],
        ["Find the energy in kWh.", "Multiply by the price.", "100 cents = $1."],
        figure=sk.rating_plate([f"{fmt(P)} kW", "230 V"]), dp=2)


@template("c14_meter_difference", chapter=14, level=2, lo="14c")
def meter_difference(rng):
    start = nice(rng, 1234.5, 2051.2, 3478.6, 5602.3)
    used = nice(rng, 12.5, 18.4, 25.0, 31.6)
    end = round(start + used, 1)
    table = md_table(["", "meter reading / kWh"], [["start of week", fmt(start, dp=1)], ["end of week", fmt(end, dp=1)]])
    return calc_q(rng, f"The table shows a household electricity meter at the start and end of a week.\n\n{table}\n\nHow much energy was used during the week?", used, [
        (end, "That is the meter reading, not the energy used in the week."),
        (start + end, "Subtract the readings."),
        (used * 10, "Check the subtraction."),
    ], "kWh", "energy used = end reading − start reading", [f"{fmt(end, dp=1)} − {fmt(start, dp=1)}", f"= **{fmt(used, dp=1)} kWh**"],
        ["The meter counts the total kWh ever used.", "Subtract the earlier reading from the later one.", "The answer is in kWh."], dp=1)


# ---------------------------------------------------------------- L3
@template("c14_fuse_choice_b", chapter=14, level=3, lo="14e")
def fuse_choice_b(rng):
    P = nice(rng, 100, 500, 690, 920, 1840, 2760)
    I = P / MAINS
    fuse = next(f for f in (3, 5, 13) if f > I)
    return calc_q(rng, f"Fig. 1 shows the rating of an appliance: **{P} W, 230 V**. Fuses of 3 A, 5 A and 13 A are available. Which fuse should be fitted?", fuse, [
        (13 if fuse != 13 else 5, "Choose the SMALLEST rating that is above the normal current."),
        (3 if fuse != 3 else 13, "The fuse must be above the normal current, " + fmt(I) + " A."),
        (5 if fuse != 5 else 3, "Work out I = P ÷ V and choose the next rating up."),
    ], "A", "I = P ÷ V; fuse = smallest rating above I", [f"I = {P} ÷ 230 = {fmt(I)} A", f"fuse = **{fuse} A**"],
        ["Find the normal current.", "The fuse must not blow in normal use.", "But it should be as small as possible."],
        figure=sk.rating_plate([f"{P} W", "230 V"]), sf=None)


@template("c14_daily_cost_days", chapter=14, level=3, lo="14c")
def daily_cost_days(rng):
    P = nice(rng, 0.1, 0.15, 0.5, 1.2)
    h = nice(rng, 4, 6, 8)
    days = nice(rng, 7, 30)
    price = nice(rng, 20, 25, 30)
    cost = P * h * days * price
    table = md_table(["power / kW", "hours per day", "days", "price / cents per kWh"], [[fmt(P), h, days, price]])
    return calc_q(rng, f"The table gives the use of an appliance.\n\n{table}\n\nWhat is the total cost, in cents?", cost, [
        (P * h * price, "That is the cost for ONE day."),
        (P * h * days, "That is the energy in kWh; multiply by the price."),
        (P * 1000 * h * days * price, "Keep the power in kW."),
    ], "cents", "kWh = kW × hours per day × days; cost = kWh × price", [f"E = {fmt(P)} × {h} × {days} = {fmt(P * h * days)} kWh", f"cost = {fmt(P * h * days)} × {price}", f"= **{fmt(cost)} cents**"],
        ["Find the total hours of use.", "Find the energy in kWh.", "Multiply by the price."])


@template("c14_power_from_v_r", chapter=14, level=3, lo="14b")
def power_from_v_r(rng):
    V = nice(rng, 12, 24, 230)
    R = nice(rng, 4, 8, 12) if V < 100 else nice(rng, 23, 46, 115)
    I = V / R
    P = V * I
    return calc_q(rng, f"Fig. 1 shows a heating element of resistance **{R} Ω** connected to a **{V} V** supply. What is its power?", P, [
        (V * R, "First find the current I = V ÷ R, then P = V I."),
        (V / R, "That is the current; multiply by V to get the power."),
        (I * R, "That is the p.d. again; P = V × I."),
    ], "W", "I = V ÷ R; P = V I", [f"I = {V} ÷ {R} = {fmt(I)} A", f"P = {V} × {fmt(I)}", f"= **{fmt(P)} W**"],
        ["Find the current first.", "I = V ÷ R.", "Then P = V I."],
        figure=sk.circuit(series=[("R", f"{R} Ω")], emf=f"{V} V"))


@template("c14_joules_to_kwh", chapter=14, level=3, lo="14c")
def joules_to_kwh(rng):
    kwh = nice(rng, 0.5, 1, 2, 2.5, 5)
    E = kwh * 3.6e6
    table = md_table(["energy transferred / J"], [[f"{fmt(E / 1e6)} × 10⁶"]])
    return calc_q(rng, f"An appliance transfers this amount of energy.\n\n{table}\n\nWhat is this in kWh? (1 kWh = 3.6 × 10⁶ J)", kwh, [
        (E / 1e6, "1 kWh = 3.6 × 10⁶ J, not 10⁶ J."),
        (E / 3600, "Divide by 3.6 × 10⁶ (1000 W × 3600 s)."),
        (E / 3.6e6 * 1000, "Check the conversion: 1 kWh = 1000 W × 3600 s."),
    ], "kWh", "kWh = J ÷ (3.6 × 10⁶)", [f"{fmt(E / 1e6)} × 10⁶ ÷ 3.6 × 10⁶", f"= **{fmt(kwh)} kWh**"],
        ["1 kWh = 1 kW for 1 h.", "= 1000 W × 3600 s.", "Divide the joules by 3.6 × 10⁶."])


@template("c14_charge_through_heater", chapter=14, level=3, lo="14b")
def charge_through_heater(rng):
    P = nice(rng, 1150, 2300)
    t = nice(rng, 60, 120, 300)
    I = P / MAINS
    Q = I * t
    return calc_q(rng, f"Fig. 1 shows the rating of a heater: **{P} W, 230 V**. How much charge flows through it in **{t} s**?", Q, [
        (P * t, "That is the energy in J. Find the current first, then Q = I t."),
        (I, "That is the current; multiply by the time."),
        (P * t / MAINS / 60, "The time is already in seconds."),
    ], "C", "I = P ÷ V; Q = I t", [f"I = {P} ÷ 230 = {fmt(I)} A", f"Q = {fmt(I)} × {t}", f"= **{fmt(Q)} C**"],
        ["Find the current from the rating.", "I = P ÷ V.", "Then Q = I t."],
        figure=sk.rating_plate([f"{P} W", "230 V"]))


@template("c14_hours_per_kwh", chapter=14, level=3, lo="14c")
def hours_per_kwh(rng):
    P = nice(rng, 20, 40, 50, 100, 200, 250)
    h = 1000 / P
    return calc_q(rng, f"Fig. 1 shows a **{P} W** lamp. For how many hours can it run on **1 kWh** of energy?", h, [
        (P / 1000, "t = E ÷ P with E = 1 kWh and P in kW."),
        (1000 * P, "t = E ÷ P."),
        (h * 60, "That is in minutes; the answer is in hours."),
    ], "h", "t = E ÷ P = 1 kWh ÷ (P in kW)", [f"P = {P} W = {fmt(P / 1000)} kW", f"t = 1 ÷ {fmt(P / 1000)}", f"= **{fmt(h)} h**"],
        ["Convert the power to kW.", "t = E ÷ P.", "1 ÷ the power in kW."],
        figure=sk.rating_plate([f"{P} W", "230 V"]))


# ---------------------------------------------------------------- L4
@template("c14_compare_cost_difference", chapter=14, level=4, lo="14c")
def compare_cost_difference(rng):
    (a, Pa, ha), (b, Pb, hb) = rng.choice([(("heater", 2, 3), ("fan", 0.05, 8)), (("oven", 2.5, 1.5), ("microwave", 0.8, 0.5)),
                                           (("dryer", 2.4, 1), ("kettle", 2.2, 0.25))])
    price = nice(rng, 20, 25, 30)
    diff = (Pa * ha - Pb * hb) * price
    table = md_table(["appliance", "power / kW", "hours used per day"], [[a, fmt(Pa), fmt(ha)], [b, fmt(Pb), fmt(hb)]])
    return calc_q(rng, f"The table compares two appliances. Electricity costs **{price} cents per kWh**.\n\n{table}\n\nHow much more does the {a} cost per day than the {b}, in cents?", diff, [
        ((Pa - Pb) * price, "Include the hours each is used: kWh = kW × h."),
        (Pa * ha * price, "That is the cost of the first appliance only."),
        (Pa * ha - Pb * hb, "That is the difference in kWh; multiply by the price."),
    ], "cents", "cost = kW × h × price for each; subtract", [f"{a}: {fmt(Pa)} × {fmt(ha)} = {fmt(Pa * ha)} kWh", f"{b}: {fmt(Pb)} × {fmt(hb)} = {fmt(Pb * hb)} kWh", f"difference = {fmt(Pa * ha - Pb * hb)} × {price} = **{fmt(diff)} cents**"],
        ["Find the kWh for each appliance.", "Subtract.", "Multiply by the price."])


@template("c14_max_lamps_on_fuse", chapter=14, level=4, lo="14e")
def max_lamps_on_fuse(rng):
    P = nice(rng, 100, 150, 200, 500)
    fuse = nice(rng, 5, 13)
    n = int(fuse * MAINS / P)
    table = md_table(["power of each lamp / W", "mains p.d. / V", "fuse rating / A"], [[P, MAINS, fuse]])
    return calc_q(rng, f"Identical lamps are connected in parallel to a circuit protected by a fuse.\n\n{table}\n\nWhat is the greatest number of lamps that can be switched on without blowing the fuse?", n, [
        (n + 1, "Round DOWN: one more lamp would take the current above the fuse rating."),
        (fuse * P / MAINS, "Find the current per lamp (P ÷ V) and divide the fuse rating by it."),
        (int(fuse * MAINS / P / 2), "Check the arithmetic: fuse rating ÷ current per lamp."),
    ], "lamps", "current per lamp = P ÷ V; number = fuse ÷ current per lamp (round down)",
        [f"I per lamp = {P} ÷ 230 = {fmt(P / MAINS)} A", f"{fuse} ÷ {fmt(P / MAINS)} = {fmt(fuse * MAINS / P)}", f"greatest number = **{n}**"],
        ["Find the current each lamp draws.", "Currents in parallel add.", "How many fit under the fuse rating?"], sf=None)


@template("c14_monthly_bill_table", chapter=14, level=4, lo="14c")
def monthly_bill_table(rng):
    rows = [("lights", 0.3, 5), ("fridge", 0.2, 24), ("TV", 0.15, 4)]
    days = 30
    price = nice(rng, 20, 25, 30)
    kwh = sum(p * h for _, p, h in rows) * days
    cost = kwh * price / 100
    table = md_table(["appliance", "power / kW", "hours per day"], [[n, fmt(p), h] for n, p, h in rows])
    return calc_q(rng, f"The table shows daily use in a flat. Electricity costs **{price} cents per kWh**.\n\n{table}\n\nWhat is the cost for **{days} days**, in dollars?", cost, [
        (kwh * price, "That is in cents; divide by 100."),
        (kwh / days * price / 100, "That is the cost for ONE day."),
        (kwh, "That is the energy in kWh."),
    ], "$", "daily kWh = Σ kW × h; × days × price", [f"daily energy = {fmt(kwh / days)} kWh", f"{days} days: {fmt(kwh)} kWh", f"cost = {fmt(kwh)} × {price} ÷ 100 = **${cost:.2f}**"],
        ["Find each appliance's daily kWh.", "Add them and multiply by the days.", "Multiply by the price and convert to dollars."], dp=2)


@template("c14_power_from_kwh_hours", chapter=14, level=4, lo="14c")
def power_from_kwh_hours(rng):
    E = nice(rng, 3, 4.5, 6, 9)
    h = nice(rng, 2, 3, 4)
    P = E / h * 1000
    table = md_table(["energy used / kWh", "time / h"], [[fmt(E), h]])
    return calc_q(rng, f"A water heater uses this much energy.\n\n{table}\n\nWhat is its power in watts?", P, [
        (E / h, "That is the power in kW; convert to W (× 1000)."),
        (E * h * 1000, "P = E ÷ t."),
        (E / h * 100, "1 kW = 1000 W."),
    ], "W", "P (kW) = E (kWh) ÷ t (h); × 1000 for W", [f"P = {fmt(E)} ÷ {h} = {fmt(E / h)} kW", f"= **{fmt(P)} W**"],
        ["P = E ÷ t.", "kWh ÷ h gives kW.", "Convert kW to W."])


# ---------------------------------------------------------------- L5
@template("c14_led_payback", chapter=14, level=5, lo="14c")
def led_payback(rng):
    Pold, Pnew = rng.choice([(60, 10), (100, 15), (75, 12)])
    h = nice(rng, 4, 5, 6)
    price = nice(rng, 25, 30)
    lamp_cost = nice(rng, 300, 450, 600)
    saving_per_day = (Pold - Pnew) / 1000 * h * price
    days = lamp_cost / saving_per_day
    table = md_table(["", "power / W"], [["old lamp", Pold], ["LED lamp", Pnew]])
    return calc_q(rng, f"An old lamp is replaced by an LED lamp that costs **{lamp_cost} cents**. The lamp is on **{h} hours** a day and electricity costs **{price} cents per kWh**.\n\n{table}\n\nAfter how many days has the saving paid for the LED lamp?", days, [
        (lamp_cost / (Pnew / 1000 * h * price), "Use the SAVING per day, which comes from the difference in power."),
        (lamp_cost / ((Pold - Pnew) * h * price), "Convert W to kW before finding kWh."),
        (lamp_cost / ((Pold - Pnew) / 1000 * price), "Include the hours of use per day."),
    ], "days", "saving per day = (ΔP in kW) × h × price; days = lamp cost ÷ daily saving",
        [f"ΔP = {Pold - Pnew} W = {fmt((Pold - Pnew) / 1000)} kW", f"saving per day = {fmt((Pold - Pnew) / 1000)} × {h} × {price} = {fmt(saving_per_day)} cents", f"days = {lamp_cost} ÷ {fmt(saving_per_day)} = **{fmt(days)}**"],
        ["Find how much less power the LED uses.", "Work out the daily saving in cents.", "Divide the lamp's cost by the daily saving."])


@template("c14_element_for_power", chapter=14, level=5, lo="14b")
def element_for_power(rng):
    P = nice(rng, 1150, 2300, 460, 920)
    I = P / MAINS
    R = MAINS / I
    return calc_q(rng, f"A heater must have a power of **{P} W** on the 230 V mains. The table summarises this. What resistance must its element have?\n\n" + md_table(["required power / W", "mains p.d. / V"], [[P, MAINS]]), R, [
        (P / MAINS, "That is the current. R = V ÷ I."),
        (MAINS * I, "That is the power again. R = V ÷ I."),
        (P / I, "R = V ÷ I, not P ÷ I."),
    ], "Ω", "I = P ÷ V; R = V ÷ I", [f"I = {P} ÷ 230 = {fmt(I)} A", f"R = 230 ÷ {fmt(I)}", f"= **{fmt(R)} Ω**"],
        ["Find the current the heater must draw.", "I = P ÷ V.", "Then R = V ÷ I."])


@template("c14_adapter_fuse", chapter=14, level=5, lo="14e")
def adapter_fuse(rng):
    a, b = rng.choice([(460, 690), (920, 460), (1150, 230), (690, 690)])
    I = (a + b) / MAINS
    fuse = next(f for f in (3, 5, 13) if f > I)
    table = md_table(["appliance", "power / W"], [["A", a], ["B", b]])
    return calc_q(rng, f"Two appliances run together from one 230 V adapter. Fuses of 3 A, 5 A and 13 A are available for the adapter's plug.\n\n{table}\n\nWhich fuse should be fitted?", fuse, [
        (next(f for f in (3, 5, 13) if f > a / MAINS), "Add the two powers: the plug carries BOTH currents."),
        (13 if fuse != 13 else 5, "Choose the smallest rating above the total current."),
        (3 if fuse != 3 else 13, "Find the total current first: (P_A + P_B) ÷ V."),
    ], "A", "I_total = (P_A + P_B) ÷ V; smallest fuse above it", [f"I = ({a} + {b}) ÷ 230 = {fmt(I)} A", f"fuse = **{fuse} A**"],
        ["Both appliances draw current through the same plug.", "Add their powers.", "Find the total current and choose the fuse."], sf=None)


@template("c14_time_for_cost", chapter=14, level=5, lo="14c")
def time_for_cost(rng):
    P = nice(rng, 2, 2.5, 3)
    price = nice(rng, 20, 25)
    budget = nice(rng, 100, 150, 200)
    h = budget / price / P
    table = md_table(["heater power / kW", "price / cents per kWh", "budget / cents"], [[fmt(P), price, budget]])
    return calc_q(rng, f"A student wants to know how long a heater can run for a fixed budget.\n\n{table}\n\nFor how many hours can it run?", h, [
        (budget / price, "That is the number of kWh; divide by the power to get hours."),
        (budget * P / price, "t = kWh ÷ kW."),
        (budget / (price * P) * 60, "That is in minutes."),
    ], "h", "kWh affordable = budget ÷ price; t = kWh ÷ P", [f"kWh = {budget} ÷ {price} = {fmt(budget / price)} kWh", f"t = {fmt(budget / price)} ÷ {fmt(P)}", f"= **{fmt(h)} h**"],
        ["How many kWh can the budget buy?", "Energy = power × time.", "Divide the kWh by the power in kW."])
