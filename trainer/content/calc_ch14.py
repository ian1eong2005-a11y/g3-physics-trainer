"""Chapter 14 Practical Electricity: P = V I, E = V I t, cost in kWh, fuse ratings."""
from .. import sketches2 as sk
from .base import fmt, md_table, nice, numeric_options, template

MAINS = 230


# ---------------------------------------------------------------- L1
@template("c14_power_from_vi", chapter=14, level=1, lo="14b")
def power_from_vi(rng):
    V = nice(rng, 12, 230)
    I = nice(rng, 0.5, 2, 2.5, 4, 5, 8, 10) if V == 230 else nice(rng, 0.5, 1.5, 2, 3, 5)
    P = V * I
    opts, key, mis = numeric_options(rng, P, [
        (V / I, "You divided. Power = p.d. × current."),
        (I / V, "You divided the wrong way round. P = V I."),
        (V + I, "You added. P = V × I."),
    ], unit="W")
    return dict(
        stem=f"Fig. 1 shows the rating plate of an appliance that works on **{V} V** and draws a current of **{fmt(I)} A**. What is its power?",
        figure=sk.rating_plate([f"{V} V", f"{fmt(I)} A"]),
        options=opts, key=key, misconceptions=mis,
        formula="power = p.d. × current (P = V I)",
        working=["P = V I", f"= {V} × {fmt(I)}", f"= **{fmt(P)} W**"],
        hints=["Which equation links power, p.d. and current?",
               f"The p.d. is {V} V and the current is {fmt(I)} A. Multiply.",
               f"P = {V} × {fmt(I)}."],
    )


@template("c14_energy_from_power_time", chapter=14, level=1, lo="14b")
def energy_from_power_time(rng):
    P = nice(rng, 20, 60, 100, 500, 800, 1500, 2000)
    t = nice(rng, 5, 10, 20, 30, 60, 120)
    E = P * t
    opts, key, mis = numeric_options(rng, E, [
        (P / t, "You divided. Energy = power × time."),
        (t / P, "You divided the wrong way round. E = P t."),
        (P * t / 60, "You divided by 60; the time is already in seconds."),
    ], unit="J")
    return dict(
        stem=f"Fig. 1 shows an appliance rated at **{fmt(P)} W**. How much energy does it transfer in **{t} s**?",
        figure=sk.rating_plate([f"{fmt(P)} W"]),
        options=opts, key=key, misconceptions=mis,
        formula="energy = power × time (E = P t = V I t)",
        working=["E = P t", f"= {fmt(P)} × {t}", f"= **{fmt(E)} J**"],
        hints=["Power is energy transferred per second. How much in several seconds?",
               f"{fmt(P)} joules every second, for {t} seconds.",
               f"E = {fmt(P)} × {t}."],
    )


# ---------------------------------------------------------------- L2
@template("c14_current_from_power", chapter=14, level=2, lo="14b")
def current_from_power(rng):
    P = nice(rng, 460, 920, 1150, 1380, 2300, 2760, 3000)
    I = P / MAINS
    opts, key, mis = numeric_options(rng, I, [
        (P * MAINS, "You multiplied. Rearrange P = V I to give I = P ÷ V."),
        (MAINS / P, "You divided the wrong way round: I = P ÷ V."),
        (P / MAINS / 2, "Check the division: I = P ÷ 230."),
    ], unit="A", dp=1)
    return dict(
        stem=f"Fig. 1 shows the rating plate of a heater: **{fmt(P)} W, 230 V**. What current does it draw?",
        figure=sk.rating_plate([f"{fmt(P)} W", "230 V"], title="heater"),
        options=opts, key=key, misconceptions=mis,
        formula="P = V I, rearranged: I = P ÷ V",
        working=["I = P ÷ V", f"= {fmt(P)} ÷ 230", f"= **{fmt(I, dp=1)} A**"],
        hints=["You know the power and the p.d. Rearrange P = V I for the current.",
               f"Divide {fmt(P)} W by 230 V.",
               f"I = {fmt(P)} ÷ 230."],
    )


@template("c14_energy_vit_minutes", chapter=14, level=2, lo="14b")
def energy_vit_minutes(rng):
    V = nice(rng, 12, 230)
    I = nice(rng, 0.5, 1, 2, 4, 5) if V == 230 else nice(rng, 2, 3, 5)
    t_min = nice(rng, 2, 5, 10, 15, 20)
    E = V * I * t_min * 60
    opts, key, mis = numeric_options(rng, E, [
        (V * I * t_min, "You left the time in minutes. E = V I t needs the time in seconds."),
        (V * I, "That is the power in watts. Multiply by the time in seconds."),
        (V * I * t_min * 60 / 60 / 60, "You divided by 60 instead of multiplying: minutes × 60 = seconds."),
    ], unit="J")
    return dict(
        stem=f"Fig. 1 shows an appliance on a **{V} V** supply drawing **{fmt(I)} A** for **{t_min} minutes**. How much energy does it transfer?",
        figure=sk.rating_plate([f"{V} V", f"{fmt(I)} A"]),
        options=opts, key=key, misconceptions=mis,
        formula="E = V I t, with t in seconds",
        working=[f"t = {t_min} min = {t_min * 60} s", f"E = {V} × {fmt(I)} × {t_min * 60}", f"= **{fmt(E)} J**"],
        hints=["E = V I t. Which quantity is not yet in SI units?",
               f"{t_min} minutes = {t_min * 60} seconds.",
               f"E = {V} × {fmt(I)} × {t_min * 60}."],
    )


@template("c14_cost_single_appliance", chapter=14, level=2, lo="14c")
def cost_single_appliance(rng):
    P_kW = nice(rng, 0.5, 1, 1.5, 2, 2.5, 3)
    h = nice(rng, 2, 3, 4, 5, 8, 10)
    price = nice(rng, 20, 25, 30, 32)
    cost = P_kW * h * price
    opts, key, mis = numeric_options(rng, cost, [
        (P_kW * 1000 * h * price, "You used watts instead of kilowatts. A kWh uses power in kW."),
        (P_kW * price, "You forgot the time. Energy in kWh = power (kW) × time (h)."),
        (P_kW * h, "That is the energy in kWh. Multiply by the price per kWh for the cost."),
    ], unit="cents")
    return dict(
        stem=f"Fig. 1 shows the rating of a **{fmt(P_kW)} kW** appliance. It is used for **{h} hours**. Electricity costs **{price} cents per kWh**. What is the cost?",
        figure=sk.rating_plate([f"{fmt(P_kW)} kW", f"used {h} h"]),
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × time (h); cost = energy × price per kWh",
        working=[f"energy = {fmt(P_kW)} × {h} = {fmt(P_kW * h)} kWh", f"cost = {fmt(P_kW * h)} × {price} = **{fmt(cost)} cents**"],
        hints=["A kilowatt-hour is the energy used by 1 kW running for 1 hour. How many kWh here?",
               f"{fmt(P_kW)} kW × {h} h = {fmt(P_kW * h)} kWh.",
               f"Multiply {fmt(P_kW * h)} kWh by {price} cents."],
    )


# ---------------------------------------------------------------- L3
@template("c14_choose_fuse", chapter=14, level=3, lo="14e")
def choose_fuse(rng):
    P = nice(rng, 400, 500, 600, 800, 1000, 1800, 2000, 2500, 2800)
    I = P / MAINS
    fuse = next(f for f in (3, 5, 13) if f > I)
    others = [f for f in (1, 3, 5, 13) if f != fuse]
    opts, key, mis = numeric_options(rng, fuse, [
        (next((f for f in (1, 3, 5) if f < I), 1), f"That fuse is rated BELOW the normal current of {fmt(I, dp=2)} A, so it would blow in normal use."),
        (next((f for f in (13, 5) if f > fuse), 13) if fuse != 13 else 30, "That rating is much higher than needed; a fault current might not blow it. Choose the smallest rating above the normal current."),
        (round(I, 1), f"That is the normal current. The fuse must be rated just ABOVE it: the next standard value."),
    ], unit="A")
    return dict(
        stem=f"Fig. 1 shows the rating of an appliance: **{fmt(P)} W, 230 V**. Fuses are available rated 3 A, 5 A and 13 A. Which fuse should be fitted?",
        figure=sk.rating_plate([f"{fmt(P)} W", "230 V"]),
        options=opts, key=key, misconceptions=mis,
        formula="I = P ÷ V; choose the smallest standard fuse rating just above the normal current",
        working=[f"I = {fmt(P)} ÷ 230 = {fmt(I, dp=2)} A", f"smallest fuse rated above {fmt(I, dp=2)} A: **{fuse} A**"],
        hints=["First find the current the appliance normally draws, using P = V I.",
               f"I = {fmt(P)} ÷ 230 = {fmt(I, dp=2)} A. The fuse must not blow at this current, but should blow soon above it.",
               f"Pick the smallest of 3 A, 5 A, 13 A that is above {fmt(I, dp=2)} A."],
    )


@template("c14_kwh_from_watts_hours", chapter=14, level=3, lo="14c")
def kwh_from_watts_hours(rng):
    P = nice(rng, 40, 60, 100, 150, 250, 400, 800)
    h = nice(rng, 3, 5, 6, 8, 10, 12, 25)
    kwh = P / 1000 * h
    opts, key, mis = numeric_options(rng, kwh, [
        (P * h, "You left the power in watts. kWh needs kilowatts (÷ 1000)."),
        (P / 1000 / h, "You divided by the time. Energy = power × time."),
        (P * h / 100, "You divided by 100 instead of 1000."),
    ], unit="kWh")
    return dict(
        stem=f"Fig. 1 shows a **{fmt(P)} W** appliance. It runs for **{h} hours**. How much energy does it use, in kWh?",
        figure=sk.rating_plate([f"{fmt(P)} W", f"used {h} h"]),
        options=opts, key=key, misconceptions=mis,
        formula="energy (kWh) = power (kW) × time (h)",
        working=[f"P = {fmt(P)} W = {fmt(P / 1000)} kW", f"energy = {fmt(P / 1000)} × {h} = **{fmt(kwh)} kWh**"],
        hints=["kWh means kilowatts × hours. Convert the power first.",
               f"{fmt(P)} W = {fmt(P / 1000)} kW.",
               f"energy = {fmt(P / 1000)} × {h}."],
    )


@template("c14_element_resistance", chapter=14, level=3, lo="14b")
def element_resistance(rng):
    P = nice(rng, 460, 920, 1150, 2300, 2760)
    I = P / MAINS
    R = MAINS / I
    opts, key, mis = numeric_options(rng, R, [
        (MAINS / P, "You divided V by P. Find the current first (I = P ÷ V), then R = V ÷ I."),
        (P / MAINS, "That is the current in amperes, not the resistance."),
        (MAINS * I, "You multiplied V by I: that gives the power again. R = V ÷ I."),
    ], unit="Ω")
    return dict(
        stem=f"Fig. 1 shows the rating of an electric kettle: **{fmt(P)} W, 230 V**. What is the resistance of its heating element when working normally?",
        figure=sk.rating_plate([f"{fmt(P)} W", "230 V"], title="kettle"),
        options=opts, key=key, misconceptions=mis,
        formula="I = P ÷ V, then R = V ÷ I",
        working=[f"I = {fmt(P)} ÷ 230 = {fmt(I)} A", f"R = 230 ÷ {fmt(I)} = **{fmt(R)} Ω**"],
        hints=["Two steps: the current from the power, then the resistance from the current.",
               f"I = {fmt(P)} ÷ 230 = {fmt(I)} A.",
               f"R = 230 ÷ {fmt(I)}."],
    )


# ---------------------------------------------------------------- L4
@template("c14_weekly_cost_table", chapter=14, level=4, lo="14c")
def weekly_cost_table(rng):
    items = [("fridge", nice(rng, 0.1, 0.15, 0.2), 24 * 7), ("television", nice(rng, 0.1, 0.15, 0.2), nice(rng, 14, 21, 28)), ("kettle", nice(rng, 2, 2.5, 3), nice(rng, 1, 2, 3))]
    price = nice(rng, 25, 30)
    total_kwh = sum(p * h for _, p, h in items)
    cost = total_kwh * price / 100
    opts, key, mis = numeric_options(rng, cost, [
        (sum(p for _, p, _ in items) * price / 100, "You forgot the hours. Each appliance's energy is power × time."),
        (total_kwh, "That is the total energy in kWh, not the cost. Multiply by the price."),
        (total_kwh * price, "That is the cost in cents. The question asks for dollars (÷ 100)."),
    ], unit="$", dp=2)
    table = md_table(["appliance", "power / kW", "hours used per week"], [[n, fmt(p), fmt(h)] for n, p, h in items])
    return dict(
        stem=f"The table shows three appliances in a home.\n\n{table}\n\nElectricity costs **{price} cents per kWh**. What is the total cost of running the three appliances for one week, in dollars?",
        options=opts, key=key, misconceptions=mis,
        formula="for each appliance energy (kWh) = power (kW) × hours; add; cost = total kWh × price",
        working=[" + ".join(f"{fmt(p)} × {fmt(h)}" for _, p, h in items) + f" = {fmt(total_kwh)} kWh",
                 f"cost = {fmt(total_kwh)} × {price} cents = {fmt(total_kwh * price)} cents = **${fmt(cost, dp=2)}**"],
        hints=["Work out the kWh for each row (kW × hours), then add them.",
               f"Total = {fmt(total_kwh)} kWh.",
               f"Cost = {fmt(total_kwh)} × {price} cents, then convert to dollars."],
    )


@template("c14_power_from_meter", chapter=14, level=4, lo="14c")
def power_from_meter(rng):
    start = nice(rng, 1234.5, 2045.0, 5120.2, 8760.4)
    kwh = nice(rng, 3, 4.5, 6, 7.5, 9, 12)
    hours = nice(rng, 2, 3, 5, 6)
    end = start + kwh
    P = kwh / hours
    opts, key, mis = numeric_options(rng, P, [
        (kwh * hours, "You multiplied. Power = energy ÷ time."),
        (kwh, "That is the energy used in kWh. Divide by the time for the average power."),
        (end / hours, "You used the final meter reading. Use the DIFFERENCE between the readings."),
    ], unit="kW")
    table = md_table(["", "reading / kWh"], [["start", fmt(start, dp=1)], ["after " + str(hours) + " hours", fmt(end, dp=1)]])
    return dict(
        stem=f"The table shows the readings on a household electricity meter while only a heater was switched on.\n\n{table}\n\nWhat is the average power of the heater?",
        options=opts, key=key, misconceptions=mis,
        formula="energy used = difference in meter readings; power = energy ÷ time",
        working=[f"energy = {fmt(end, dp=1)} − {fmt(start, dp=1)} = {fmt(kwh)} kWh", f"power = {fmt(kwh)} ÷ {hours} = **{fmt(P)} kW**"],
        hints=["The meter counts kWh. How much energy was used between the two readings?",
               f"{fmt(end, dp=1)} − {fmt(start, dp=1)} = {fmt(kwh)} kWh over {hours} hours.",
               f"power = {fmt(kwh)} ÷ {hours}."],
    )


# ---------------------------------------------------------------- L5
@template("c14_annual_cost_comparison", chapter=14, level=5, lo="14c")
def annual_cost_comparison(rng):
    P_old = nice(rng, 60, 75, 100)
    P_new = nice(rng, 8, 10, 12, 15)
    h = nice(rng, 4, 5, 6, 8)
    price = nice(rng, 25, 30)
    saving = (P_old - P_new) / 1000 * h * 365 * price / 100
    opts, key, mis = numeric_options(rng, saving, [
        ((P_old - P_new) / 1000 * h * price / 100, "That is the saving per DAY. Multiply by 365 for a year."),
        ((P_old - P_new) * h * 365 * price / 100, "You left the power in watts; kWh needs kW."),
        (P_old / 1000 * h * 365 * price / 100, "That is the full cost of the old lamp, not the saving. Subtract the new lamp's cost."),
    ], unit="$", dp=2)
    return dict(
        stem=f"Fig. 1 shows the ratings of two lamps. A **{fmt(P_old)} W** filament lamp is replaced by a **{fmt(P_new)} W** LED lamp giving the same light. The lamp is used **{h} hours a day** and electricity costs **{price} cents per kWh**. How much money is saved in a year (365 days)?",
        figure=sk.rating_plate([f"old: {fmt(P_old)} W", f"new: {fmt(P_new)} W"], title="lamps"),
        options=opts, key=key, misconceptions=mis,
        formula="saving = (P_old − P_new in kW) × hours per year × price",
        working=[f"power saved = {fmt(P_old)} − {fmt(P_new)} = {fmt(P_old - P_new)} W = {fmt((P_old - P_new) / 1000)} kW",
                 f"hours per year = {h} × 365 = {h * 365}", f"energy saved = {fmt((P_old - P_new) / 1000)} × {h * 365} = {fmt((P_old - P_new) / 1000 * h * 365)} kWh",
                 f"saving = {fmt((P_old - P_new) / 1000 * h * 365)} × {price} cents = **${fmt(saving, dp=2)}**"],
        hints=["Find the difference in power, convert to kW, and multiply by the total hours in a year.",
               f"Power saved = {fmt(P_old - P_new)} W; hours per year = {h * 365}.",
               f"Energy saved in kWh × {price} cents, then convert to dollars."],
    )


@template("c14_total_current_socket", chapter=14, level=5, lo="14e")
def total_current_socket(rng):
    apps = rng.sample([("kettle", 2300), ("heater", 2000), ("toaster", 920), ("iron", 1150), ("hair dryer", 1380), ("microwave", 920)], 3)
    total_P = sum(p for _, p in apps)
    I = total_P / MAINS
    opts, key, mis = numeric_options(rng, I, [
        (max(p for _, p in apps) / MAINS, "That is the current of the largest appliance only. All three currents add."),
        (total_P / MAINS / 3, "You averaged. The currents ADD because the appliances are in parallel."),
        (total_P * MAINS / 1000, "You multiplied by the p.d. I = P ÷ V."),
    ], unit="A", dp=1)
    table = md_table(["appliance", "power / W"], [[n, fmt(p)] for n, p in apps])
    return dict(
        stem=f"Three appliances are plugged into one 230 V extension socket fitted with a 13 A fuse.\n\n{table}\n\nWhat total current is drawn when all three are used together? (Decide whether the fuse will blow.)",
        options=opts, key=key, misconceptions=mis,
        formula="appliances in parallel: total current = sum of P ÷ V for each (or total power ÷ V)",
        working=[f"total power = {' + '.join(fmt(p) for _, p in apps)} = {fmt(total_P)} W", f"I = {fmt(total_P)} ÷ 230 = **{fmt(I, dp=1)} A**",
                 ("this exceeds 13 A, so the fuse blows" if I > 13 else "this is below 13 A, so the fuse does not blow")],
        hints=["Each appliance draws its own current, and they are in parallel. How do the currents combine?",
               f"Total power = {fmt(total_P)} W. Then I = P ÷ V.",
               f"I = {fmt(total_P)} ÷ 230; compare with 13 A."],
    )
