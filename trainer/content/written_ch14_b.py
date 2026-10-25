"""Chapter 14 Practical Electricity: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import sketches2 as sk
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 14


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


KWH_POWER = PF(["kwh is a unit of power", "kilowatt-hour is a unit of power", "kwh measures power"],
               "The kilowatt-hour is a unit of ENERGY (power × time), not power.")
FUSE_SHOCK = PF(["fuse stops you getting a shock", "fuse protects the user from shock", "fuse prevents electric shock"],
                "A fuse protects the WIRING from overheating; it is the EARTH wire (with the fuse) that protects the user.")

# ---------------------------------------------------------------- L1
Q("w14b_power_formula", 1, "14b", "State the equation linking electrical power, p.d. and current, and the unit of power.",
  [P("P = V I (power = p.d. × current)", ["p = v i", "p = vi", "p = iv", "power = voltage × current", "p.d. × current", "voltage times current", "v × i", "current × voltage"]),
   P("measured in watts (W)", ["watt", "watts", "in w"])],
  "Power = p.d. × current, P = V I, measured in watts (W).",
  ["Power links V and I.", "Multiply or divide?", "State the unit too."],
  "P = VI; watt",
  ["P = VI, measured in watts", "power = voltage × current, in W"],
  ["P = V / I in joules", "P = I / V in volts"], min_points=2,
  pitfalls=[PF(["p = v / i", "v / i"], "P = V × I; V / I is RESISTANCE.")])

Q("w14b_energy_formula", 1, "14b", "State the equation for the electrical energy E transferred by an appliance in terms of p.d., current and time, and its unit.",
  [P("E = V I t", ["e = v i t", "e = vit", "e = ivt", "v × i × t", "voltage × current × time", "e = pt", "power × time"]),
   P("measured in joules (J)", ["joule", "joules", "in j"])],
  "E = V I t (or E = P t), measured in joules (J).",
  ["Energy = power × time.", "Power = V I.", "Combine them and give the unit."],
  "E = VIt; joule",
  ["E = VIt, in joules", "energy = voltage × current × time, measured in J"],
  ["E = V / I in watts", "E = VI in volts"], min_points=2)

Q("w14b_wire_colours", 1, "14h", "Fig. 1 shows a three-pin plug. State the colour of the insulation on the live, neutral and earth wires.",
  [P("live: brown", ["brown"]),
   P("neutral: blue", ["blue"]),
   P("earth: green and yellow (stripes)", ["green and yellow", "green/yellow", "yellow and green", "green-yellow", "green yellow"])],
  "Live is brown, neutral is blue and earth is green and yellow striped.",
  ["One is brown.", "One is blue.", "The earth wire is striped."],
  "live brown; neutral blue; earth green/yellow",
  ["Live brown, neutral blue, earth green and yellow", "brown for live, blue for neutral and green/yellow for earth"],
  ["Live red, neutral black, earth green", "All are black"], min_points=3,
  figure=lambda: sk.plug_sketch(labels=False))

Q("w14b_element_property", 1, "14a", "State two properties that the heating element of an electric heater should have.",
  [P("high resistance", ["high resistance", "large resistance"]),
   P("high melting point (does not melt or oxidise when red hot)", ["high melting point", "does not melt", "withstand high temperature", "does not oxidise", "not melt"])],
  "A heating element should have a high resistance and a high melting point, so that it gets very hot without melting (e.g. nichrome).",
  ["What makes a wire heat up a lot?", "It gets red hot. What must it not do?", "State two properties."],
  "high resistance; high melting point",
  ["High resistance and a high melting point", "a large resistance so it heats up, and it must not melt"],
  ["Low resistance and low melting point", "It must be magnetic"], min_points=2,
  pitfalls=[PF(["low resistance", "low melting point"], "A heating element needs a HIGH resistance and a HIGH melting point.")])

Q("w14b_breaker_def", 1, "14e", "State what a circuit breaker does.",
  [P("it automatically switches off (breaks) the circuit when the current is too large (exceeds its rating)", ["switches off", "breaks the circuit", "cuts off", "trips", "opens the circuit", "turns off"]),
   P("when the current is too large", ["too large", "too high", "exceeds", "too much current", "above its rating", "more than its rating", "larger than its rated"])],
  "A circuit breaker automatically switches off (breaks) the circuit when the current becomes larger than its rated value.",
  ["What happens when too much current flows?", "Does it need replacing afterwards?", "State it."],
  "breaks circuit when current exceeds rating",
  ["It automatically breaks the circuit when the current is too large", "it trips and switches off when the current exceeds its rating"],
  ["It stores extra current", "It increases the voltage"], min_points=2)

Q("w14b_fuse_which_wire", 1, "14i", "Fig. 1 shows a three-pin plug. State which wire the fuse is connected to.",
  [P("the live wire (brown)", ["live", "brown"])],
  "The fuse is connected to the live (brown) wire.",
  ["Which wire is at the high p.d.?", "Its colour is brown.", "Name it."],
  "live",
  ["The live wire", "the brown live wire"],
  ["The neutral wire", "The earth wire"],
  pitfalls=[PF(["neutral", "earth wire", "blue"], "The fuse is fitted in the LIVE (brown) wire.")],
  figure=lambda: sk.plug_sketch())

Q("w14b_watt_meaning", 1, "14b", "State what is meant by a power of 1 watt.",
  [P("1 joule of energy transferred per second", ["1 joule per second", "1 j per second", "one joule per second", "1 j/s", "1 j each second", "1 joule every second", "joule of energy is transferred every second", "one joule transferred each second", "joule transferred each second"])],
  "A power of 1 watt means that 1 joule of energy is transferred every second.",
  ["Power is the rate of energy transfer.", "In joules and seconds?", "State it."],
  "1 W = 1 J/s",
  ["1 joule of energy per second", "one joule transferred each second"],
  ["1 volt per ampere", "1 coulomb per second"])

Q("w14b_earth_connections", 1, "14g", "State what the two ends of the earth wire of a metal-cased appliance are connected to.",
  [P("the metal casing of the appliance", ["metal casing", "casing", "metal case", "metal body"]),
   P("the ground (earth), through the earth pin of the plug", ["ground", "earth pin", "the earth", "into the ground"])],
  "One end of the earth wire is connected to the metal casing of the appliance; the other goes through the earth pin of the plug to the ground.",
  ["What part of the appliance must not become live?", "Where does the earth wire lead?", "State both."],
  "casing and ground",
  ["The metal casing and the ground", "it joins the metal case to the earth through the earth pin"],
  ["The live wire and the fuse", "The switch and the neutral"], min_points=2)

Q("w14b_kwh_joules", 1, "14c", "State how many joules are equal to 1 kWh.",
  [P("3.6 × 10^6 J (3 600 000 J)", ["3.6 × 10⁶", "3.6 × 10^6", "3.6 x 10^6", "3 600 000", "3600000", "3.6 million", "3.6 mj"])],
  "1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J.",
  ["1 kW = 1000 W.", "1 h = 3600 s.", "Multiply."],
  "1000 × 3600 = 3.6 × 10⁶ J",
  ["3.6 × 10^6 J", "3 600 000 joules"],
  ["1000 J", "3600 J"])

Q("w14b_mains_voltage", 1, "14d", "State the p.d. of the mains supply in Singapore homes and why touching a live wire is very dangerous.",
  [P("230 V", ["230"]),
   P("it can drive a large (possibly fatal) current through the body (electric shock)", ["electric shock", "current through the body", "fatal", "kill", "electrocuted", "electrocution", "shock"])],
  "The mains supply is 230 V. Touching a live wire can drive a large current through the body to earth, giving a severe, possibly fatal, electric shock.",
  ["What is the mains p.d.?", "What would it drive through your body?", "State both."],
  "230 V; fatal shock",
  ["230 V, and touching the live wire can give a fatal electric shock", "230 volts, which drives a dangerous current through the body"],
  ["12 V, which is harmless", "1.5 V"], min_points=2)

# ---------------------------------------------------------------- L2
Q("w14b_kettle_heating", 2, "14a", "Describe how an electric kettle heats the water inside it.",
  [P("current flows through a high-resistance heating element", ["heating element", "element", "high resistance", "current flows through"]),
   P("electrical energy is converted to thermal energy (element gets hot)", ["thermal energy", "heat", "gets hot", "heats up", "internal energy"]),
   P("the heat is transferred to the water (conduction and convection)", ["to the water", "convection", "conduction", "water is heated", "heats the water"])],
  "A current flows through the high-resistance heating element, which converts electrical energy into thermal energy and becomes hot. Heat is conducted from the element to the water, and convection currents spread it through the water.",
  ["What part of the kettle carries the current?", "What does the current do to it?", "How does the water get hot?"],
  "current in element → thermal energy → transferred to water",
  ["A current through the heating element makes it hot, and the heat is transferred to the water by conduction and convection", "the element converts electrical energy to heat which heats the water"],
  ["The kettle uses magnetism", "Light from the element heats the water"], min_points=2,
  pitfalls=[PF(["light from the element", "light heats"], "The element heats the water by CONDUCTION and CONVECTION, not by light.")])

Q("w14b_meaning_2kW", 2, "14b", "Fig. 1 shows the rating plate of a heater. Explain what the power rating of 2 kW means.",
  [P("2000 J of electrical energy is converted every second", ["2000 j per second", "2000 joules per second", "2000 j each second", "2000 j every second", "2 kj per second"]),
   P("when it is used at its rated voltage (230 V)", ["230", "rated voltage", "rated p.d.", "normal voltage"])],
  "A power of 2 kW means that the heater converts 2000 J of electrical energy into thermal energy every second, when it is connected to its rated voltage of 230 V.",
  ["1 kW = 1000 W.", "1 W = 1 J per second.", "Explain 2 kW."],
  "2000 J per second at 230 V",
  ["It converts 2000 J of energy every second at 230 V", "2000 joules per second when used at the rated voltage"],
  ["It uses 2 kWh every second", "It needs 2 kV"], min_points=1, pitfalls=[KWH_POWER],
  figure=lambda: sk.rating_plate(["230 V", "2 kW"], title="heater"))

Q("w14b_kwh_simple", 2, "14c", "A 1.5 kW heater is used for 2 hours. Explain how much energy, in kWh, it uses.",
  [P("energy (kWh) = power (kW) × time (h)", ["power × time", "e = pt", "kw × h", "multiply the power by the time", "p × t"]),
   P("1.5 × 2 = 3 kWh", ["3 kwh", "3.0 kwh", "3 kw h"])],
  "Energy in kWh = power in kW × time in hours = 1.5 × 2 = 3 kWh.",
  ["Use E = P × t.", "Keep power in kW and time in hours.", "Calculate."],
  "1.5 kW × 2 h = 3 kWh",
  ["E = Pt = 1.5 × 2 = 3 kWh", "power × time = 3 kWh"],
  ["0.75 kWh", "3000 kWh"], min_points=2)

Q("w14b_damaged_insulation", 2, "14d", "Explain why using an appliance with a cable whose insulation is damaged is dangerous.",
  [P("the live wire may be exposed", ["live wire exposed", "exposed", "bare wire", "live wire can be touched", "wires are exposed"]),
   P("touching it lets current flow through the body (electric shock)", ["electric shock", "through the body", "shock", "electrocuted"]),
   P("bare wires could touch each other, causing a short circuit, sparks or fire", ["short circuit", "fire", "sparks", "touch each other"])],
  "Damaged insulation may expose the live wire. Anyone touching it could get an electric shock as current flows through their body. Bare wires might also touch each other, causing a short circuit, sparks and a fire.",
  ["What does insulation cover?", "What happens if someone touches the bare live wire?", "What if two bare wires touch?"],
  "exposed live wire → shock; short circuit → fire",
  ["The live wire may be exposed, so touching it gives an electric shock, and bare wires could short circuit and cause a fire", "bare wires can give a shock or touch and cause a fire"],
  ["The appliance uses more electricity", "It makes the appliance slower"], min_points=2)

Q("w14b_fuse_melts", 2, "14e", "Describe what happens inside a 5 A fuse when a current of 10 A flows through it.",
  [P("the fuse wire heats up", ["heats up", "gets hot", "becomes hot", "heating effect"]),
   P("it melts (blows)", ["melts", "blows", "burns out"]),
   P("which breaks the circuit so the current stops", ["breaks the circuit", "current stops", "no current", "cuts off", "stops the current", "circuit is broken"])],
  "The current is larger than the fuse rating, so the thin fuse wire heats up until it melts (the fuse blows). This breaks the circuit and the current stops.",
  ["Is 10 A above the rating?", "What does a large current do to a thin wire?", "What happens to the circuit?"],
  "heats, melts, breaks circuit",
  ["The fuse wire heats up and melts, breaking the circuit", "it blows: the wire gets hot, melts and stops the current"],
  ["The fuse lets 10 A through safely", "The fuse increases the current"], min_points=2)

Q("w14b_two_vs_three_core", 2, "14f", "A metal toaster has a three-core cable, but a plastic-cased hair dryer has a two-core cable. Explain why.",
  [P("the toaster's metal casing could become live, so it needs an earth wire", ["metal casing", "could become live", "earth wire", "needs earthing", "earthed"]),
   P("the hair dryer is double insulated: its plastic casing does not conduct, so it cannot become live", ["double insulated", "plastic", "does not conduct", "cannot become live", "insulator", "no earth wire needed"])],
  "The toaster has a metal casing, which could become live if a fault occurs, so it needs a third (earth) wire. The hair dryer is double insulated: its plastic casing is an insulator and cannot become live, so it needs no earth wire.",
  ["Can a metal case become live? A plastic one?", "Which needs an earth wire?", "Explain."],
  "metal → earth wire; plastic (double insulated) → none",
  ["The metal toaster needs an earth wire because its casing could become live, but the plastic hair dryer is double insulated", "metal conducts so the toaster must be earthed; the plastic case cannot become live"],
  ["Hair dryers use less current", "Toasters are heavier"], min_points=2)

Q("w14b_current_from_power", 2, "14b", "An appliance is rated 1150 W, 230 V. Explain how to find the current it draws, and give the value.",
  [P("use I = P / V", ["i = p / v", "p / v", "power ÷ voltage", "power divided by voltage", "p = vi"]),
   P("1150 ÷ 230 = 5 A", ["5 a", "5.0 a", "5 amps", "5 amperes"])],
  "Use P = V I, so I = P / V = 1150 ÷ 230 = 5.0 A.",
  ["Rearrange P = VI.", "Divide power by voltage.", "Calculate."],
  "I = P/V = 1150/230 = 5 A",
  ["I = P / V = 1150 ÷ 230 = 5 A", "power divided by voltage gives 5 amps"],
  ["I = 1150 × 230", "I = 230 ÷ 1150 = 0.2 A"], min_points=2,
  figure=lambda: sk.rating_plate(["1150 W", "230 V"]))

Q("w14b_switch_off_bulb", 2, "14i", "Explain why you should switch off the supply before changing a light bulb.",
  [P("the lamp holder is connected to the live wire (at 230 V)", ["live", "230", "connected to the live", "holder is live"]),
   P("touching it could give an electric shock", ["electric shock", "shock", "electrocuted", "current through the body"])],
  "The lamp holder is connected to the live wire at 230 V. Switching off (with the switch in the live wire) disconnects it, so you cannot get an electric shock when touching the holder.",
  ["What wire is the lamp holder connected to?", "What could happen if you touch it while it is live?", "Explain."],
  "holder live → shock risk",
  ["The holder is connected to the live wire, so you could get an electric shock", "it is at 230 V and touching it could electrocute you"],
  ["To save electricity", "So that the bulb cools down only"], min_points=2)

Q("w14b_heater_more_current", 2, "14b", "Two heaters are connected to the 230 V mains. Heater X draws 8 A and heater Y draws 4 A. Explain which heater has the greater power.",
  [P("heater X", ["heater x", "x has the greater", "x"]),
   P("P = V I: same p.d., so the larger current gives the larger power (twice)", ["p = v i", "p = vi", "same voltage", "same p.d.", "larger current", "twice", "more current"])],
  "Heater X has the greater power. Since P = V I and both have the same p.d. of 230 V, the heater drawing the larger current has the larger power: X has twice the power of Y.",
  ["Write the power equation.", "Which quantity is the same for both?", "Compare."],
  "X: P = VI, same V, larger I",
  ["Heater X, because P = VI and the voltage is the same, so the larger current gives more power", "X has twice the power since it draws twice the current at 230 V"],
  ["Heater Y because it uses less current", "They have the same power"], min_points=2)

Q("w14b_bathroom_switch", 2, "14d", "Explain why light switches in bathrooms are usually pull-cord switches or are placed outside the bathroom.",
  [P("bathrooms are damp / people have wet hands", ["damp", "wet hands", "water", "wet"]),
   P("water conducts electricity, so touching a switch with wet hands could cause an electric shock", ["water conducts", "conducts", "electric shock", "shock", "current through the body"]),
   P("a pull cord (insulating) keeps hands away from the live parts", ["pull cord", "insulating cord", "away from", "not touch", "keeps hands away"])],
  "Bathrooms are damp and people often have wet hands. Water conducts electricity, so touching a switch with wet hands could let current pass through the body and cause an electric shock. An insulating pull cord, or a switch outside, keeps wet hands away from the live parts.",
  ["What is different about bathrooms?", "Why is water dangerous with electricity?", "How does a pull cord help?"],
  "damp conditions; water conducts → shock; pull cord keeps hands away",
  ["Bathrooms are damp and water conducts, so wet hands on a switch could cause a shock; a pull cord keeps hands away", "water conducts electricity, so a pull-cord switch avoids touching the switch with wet hands"],
  ["Pull cords are cheaper", "Bathrooms need brighter lights"], min_points=2)

# ---------------------------------------------------------------- L3
Q("w14b_evit_calc", 3, "14b", "A lamp on a 230 V supply draws a current of 0.25 A. Explain how to find the energy it uses in 2 minutes, and give the value.",
  [P("use E = V I t", ["e = v i t", "e = vit", "v × i × t", "voltage × current × time"]),
   P("t = 120 s", ["120 s", "120 seconds", "in seconds"]),
   P("E = 230 × 0.25 × 120 = 6900 J", ["6900 j", "6900 joules", "6 900", "6.9 kj"])],
  "Use E = V I t with the time in seconds: E = 230 × 0.25 × 120 = 6900 J.",
  ["Which equation includes V, I and t?", "Convert minutes to seconds.", "Calculate."],
  "E = 230 × 0.25 × 120 = 6900 J",
  ["E = VIt = 230 × 0.25 × 120 = 6900 J", "convert to 120 s, then 230 × 0.25 × 120 = 6900 joules"],
  ["E = 230 × 0.25 × 2 = 115 J", "E = 230 × 0.25 = 57.5 J"], min_points=2,
  pitfalls=[PF(["115 j", "57.5 j"], "Time must be in SECONDS: t = 120 s, so E = 6900 J.")])

Q("w14b_fuse_choice_kettle", 3, "14e", "A kettle is rated 2300 W, 230 V. Fuses of 3 A, 5 A and 13 A are available. Explain which fuse should be used.",
  [P("normal current = 2300 ÷ 230 = 10 A", ["10 a", "10 amps", "2300 ÷ 230", "2300 / 230"]),
   P("choose the 13 A fuse", ["13 a", "13 amp"]),
   P("the rating must be just above the normal current (3 A and 5 A would blow in normal use)", ["just above", "slightly higher", "higher than 10", "would blow", "above the normal current", "smallest rating above"])],
  "The normal current is I = P / V = 2300 ÷ 230 = 10 A. The fuse rating must be just above the normal current, so use the 13 A fuse; the 3 A and 5 A fuses would blow every time the kettle is used.",
  ["Find the normal current.", "The fuse must be just above it.", "Choose."],
  "I = 10 A → 13 A fuse",
  ["The current is 10 A, so the 13 A fuse, which is just above the normal current", "2300 ÷ 230 = 10 A; the 3 A and 5 A fuses would blow, so use 13 A"],
  ["3 A, because a smaller fuse is safer", "5 A"], min_points=2,
  pitfalls=[PF(["smaller fuse is safer", "use the 3 a", "use the 5 a"], "A fuse below the normal current (10 A) would blow in normal use.")],
  figure=lambda: sk.rating_plate(["2300 W", "230 V"], title="kettle"))

Q("w14b_tv_cost", 3, "14c", "A 150 W television is used for 4 hours a day for 30 days. Electricity costs 25 cents per kWh. Explain how to find the cost.",
  [P("energy = 0.15 kW × 4 h × 30 = 18 kWh", ["18 kwh", "0.15 kw", "0.15 × 4 × 30", "18 kw h"]),
   P("cost = 18 × 25 cents = 450 cents ($4.50)", ["450 cents", "4.50", "4.5", "450"])],
  "Convert the power to kW: 0.15 kW. Energy = 0.15 × 4 × 30 = 18 kWh. Cost = 18 × 25 cents = 450 cents = $4.50.",
  ["Convert 150 W to kW.", "Multiply by the total hours.", "Multiply by the cost per kWh."],
  "0.15 × 120 = 18 kWh → $4.50",
  ["0.15 kW × 120 h = 18 kWh, and 18 × 25 cents = $4.50", "the energy is 18 kWh so the cost is 450 cents"],
  ["150 × 4 × 30 × 25 = 450 000 cents", "$0.45"], min_points=2)

Q("w14b_earth_fault_path", 3, "14f", "A live wire inside a metal kettle comes loose and touches the earthed metal casing. Explain what happens to the current.",
  [P("current flows from the live wire through the casing and down the earth wire to the ground", ["earth wire", "to the ground", "to earth", "through the casing"]),
   P("the earth path has very low resistance, so a very large current flows", ["low resistance", "large current", "very large current", "surge"]),
   P("this large current blows the fuse (or trips the breaker), cutting off the live supply", ["blows the fuse", "fuse blows", "fuse melts", "trips", "cuts off"])],
  "Current flows from the live wire through the metal casing and down the earth wire to the ground. Because this path has a very low resistance, a very large current flows, which blows the fuse (or trips the circuit breaker) and cuts off the live supply to the kettle.",
  ["Where can current go from the casing?", "What is the resistance of that path?", "What happens to the fuse?"],
  "live → casing → earth wire; low R → large I → fuse blows",
  ["The current flows down the low-resistance earth wire, so a large current blows the fuse", "a very large current flows to earth through the casing, melting the fuse and cutting off the supply"],
  ["The kettle boils faster", "Nothing happens because the casing is metal"], min_points=2)

Q("w14b_fuse_in_neutral", 3, "14i", "An electrician wrongly fits the fuse of an appliance in the neutral wire. Explain why this is dangerous even when the fuse has blown.",
  [P("after the fuse blows, the appliance is still connected to the live wire", ["still connected to the live", "still live", "remains live", "live wire is still connected"]),
   P("so parts of it are still at 230 V and touching them could cause a shock", ["electric shock", "shock", "230", "dangerous to touch"]),
   P("the fuse must be in the live wire to disconnect the high voltage", ["in the live wire", "disconnect the live", "fuse in live"])],
  "If the fuse is in the neutral wire, when it blows the current stops but the appliance is still connected to the live wire. Parts of it remain at 230 V, so someone touching them, thinking it is safe, could get an electric shock. The fuse must be in the live wire so that blowing it disconnects the high p.d.",
  ["Which wire is at 230 V?", "If the neutral is broken, is the appliance still connected to the live?", "Explain."],
  "fuse in neutral → appliance still live after blowing → shock",
  ["Even after the fuse blows the appliance is still connected to the live wire, so it is still at 230 V and could give a shock", "the appliance remains live, so the fuse must be in the live wire"],
  ["It is not dangerous because no current flows", "The fuse will not blow"], min_points=2,
  pitfalls=[PF(["not dangerous because no current", "safe because no current flows"], "No current, but the appliance is still at 230 V: touching it can give a shock.")])

Q("w14b_breaker_reset", 3, "14e", "Explain two advantages of using circuit breakers instead of fuses in a home.",
  [P("a circuit breaker can be reset (switched back on) and need not be replaced", ["reset", "switched back on", "no need to replace", "not need replacing", "reused", "reusable"]),
   P("it acts faster than a fuse", ["faster", "quicker", "more quickly"]),
   P("it is easy to see which circuit has tripped", ["easy to see", "which circuit", "easy to find", "see which"])],
  "A circuit breaker can simply be reset once the fault is fixed, so nothing needs to be replaced. It also switches off faster than a fuse melts, and it is easy to see which circuit has tripped.",
  ["What do you do after a fuse blows? After a breaker trips?", "Which acts faster?", "Give two."],
  "reset (no replacement); faster; easy to see",
  ["It can be reset instead of replaced, and it acts faster than a fuse", "breakers are reusable and switch off more quickly"],
  ["Breakers are cheaper to replace each time", "Fuses are faster"], min_points=2)

Q("w14b_element_vs_cable", 3, "14a", "The heating element of a heater and the cable supplying it carry the same current. Explain why the element gets very hot but the cable does not.",
  [P("the element has a much higher resistance than the cable", ["higher resistance", "high resistance", "larger resistance", "more resistance"]),
   P("so most of the p.d. is across the element and its power (P = VI) is much larger", ["most of the p.d.", "larger p.d.", "p = vi", "more power", "larger power", "more energy"]),
   P("the cable has a low resistance (thick copper), so little energy is converted in it", ["low resistance", "thick copper", "little energy", "little heat", "copper"])],
  "The element has a much higher resistance than the cable. With the same current, most of the p.d. is across the element, so its power P = V I is much larger and it gets very hot. The thick copper cable has a low resistance, so very little energy is converted to heat in it.",
  ["Compare the resistances.", "Same current: where is most of the p.d.?", "Use P = VI."],
  "element high R → most p.d. → most power; cable low R",
  ["The element has a much higher resistance, so most of the p.d. and power is in the element while the low-resistance cable stays cool", "the copper cable has a low resistance, so little heat is produced in it, but the high-resistance element gets hot"],
  ["The cable is insulated so it cannot get hot", "The element carries more current"], min_points=2,
  pitfalls=[PF(["element carries more current", "more current in the element"], "They are in series, so the current is the SAME; the difference is the RESISTANCE.")])

Q("w14b_coiled_cable", 3, "14d", "The instructions for an extension cable on a drum say it must be fully unwound before a heater is plugged into it. Explain why.",
  [P("a heater draws a large current, so the cable heats up", ["large current", "cable heats up", "heats", "gets hot", "warms up"]),
   P("when coiled, the heat cannot escape (the coils heat each other)", ["cannot escape", "trapped", "coils heat each other", "cannot be lost", "no air", "cannot get out"]),
   P("so the cable overheats, melting the insulation and causing a fire", ["overheat", "melt the insulation", "fire", "insulation melts"])],
  "A heater draws a large current, which heats the cable. When the cable is coiled on the drum, the heat cannot escape because the coils heat each other, so the cable can overheat, melt its insulation and start a fire. Unwinding it lets the heat escape.",
  ["What does a large current do to the cable?", "What is different when it is coiled?", "What could happen?"],
  "large I heats cable; coiled → heat trapped → overheating, fire",
  ["The large current heats the cable, and when it is coiled the heat cannot escape, so it overheats and could cause a fire", "coiled cable traps the heat, melting the insulation"],
  ["Coiled cables carry less voltage", "So that it reaches the socket"], min_points=2)

Q("w14b_kwh_unit_why", 3, "14c", "Explain why electricity bills use the kilowatt-hour instead of the joule.",
  [P("the joule is a very small unit of energy", ["very small", "too small", "small unit"]),
   P("1 kWh = 3.6 × 10^6 J, so household energy in joules would be huge numbers", ["3.6 × 10", "huge numbers", "very large numbers", "3 600 000", "millions"]),
   P("the kWh gives convenient numbers (power in kW × time in hours)", ["convenient", "easier", "kw × h", "manageable", "simpler"])],
  "The joule is a very small unit: 1 kWh = 3.6 × 10⁶ J, so a household's energy use in joules would be a huge number. The kWh, found from power in kW × time in hours, gives convenient numbers.",
  ["How many joules are in 1 kWh?", "What would a monthly bill look like in joules?", "Explain."],
  "J too small; 1 kWh = 3.6 MJ; convenient numbers",
  ["The joule is too small; 1 kWh is 3.6 × 10^6 J, so the kWh gives more convenient numbers", "bills in joules would have huge numbers, so the larger kWh is easier"],
  ["Because the kWh is a unit of power", "Joules cannot measure electricity"], min_points=2, pitfalls=[KWH_POWER])

Q("w14b_extension_overload", 3, "14e", "A kettle (10 A) and a toaster (4 A) are plugged into an extension lead whose plug has a 13 A fuse. Explain what happens and why it is a safety feature.",
  [P("the total current is 14 A (the currents add, as they are in parallel)", ["14 a", "14 amps", "10 + 4", "add"]),
   P("this exceeds 13 A, so the fuse blows", ["fuse blows", "exceeds 13", "more than 13", "fuse melts", "above 13"]),
   P("this stops the extension cable carrying too much current and overheating", ["overheating", "overheat", "fire", "too much current", "protects the cable"])],
  "The appliances are in parallel, so their currents add: 10 + 4 = 14 A. This exceeds the 13 A rating, so the fuse blows. This is a safety feature: it stops the extension cable carrying more current than it is designed for, which could make it overheat and start a fire.",
  ["How do the currents of parallel appliances combine?", "Compare with the fuse rating.", "Why is blowing useful?"],
  "10 + 4 = 14 A > 13 A → fuse blows; protects cable from overheating",
  ["The total is 14 A, more than 13 A, so the fuse blows and stops the cable overheating", "10 + 4 = 14 A exceeds the rating, so the fuse melts to protect the lead from fire"],
  ["Nothing happens because each is below 13 A", "The fuse protects the user from shock"], min_points=2, pitfalls=[FUSE_SHOCK])

# ---------------------------------------------------------------- L4
Q("w14b_fuse_borderline", 4, "14e", "A heater draws exactly 3.0 A in normal use. Fuses of 3 A, 5 A and 13 A are available. Explain which fuse to choose.",
  [P("choose the 5 A fuse", ["5 a", "5 amp"]),
   P("a 3 A fuse is too close: it could blow in normal use (e.g. at switch-on surges)", ["too close", "could blow", "would blow", "blow in normal use", "surge", "no margin"]),
   P("13 A is too large: it would not blow until the current was dangerously high", ["13 a is too large", "too large", "too high", "would not blow", "dangerously high", "too big"])],
  "Choose the 5 A fuse. A 3 A fuse is the same as the normal current, so it could blow during normal use, especially with the surge at switch-on. A 13 A fuse is too large: it would allow a dangerously high current before blowing. The 5 A fuse is the smallest rating just above the normal current.",
  ["What is the normal current?", "Why not exactly the same rating?", "Why not the largest?"],
  "5 A: 3 A blows in normal use; 13 A too large",
  ["The 5 A fuse, because 3 A could blow in normal use and 13 A would let too large a current flow", "5 A is just above the normal current; 3 A is too close and 13 A too high"],
  ["3 A because it matches the current", "13 A because it never blows"], min_points=2,
  pitfalls=[PF(["never blows", "13 a because"], "A 13 A fuse would let a dangerously large current flow before blowing.")])

Q("w14b_same_energy_heaters", 4, "14c", "Heater A (1 kW) is used for 3 hours and heater B (3 kW) for 1 hour. Explain which costs more to run.",
  [P("A: 1 × 3 = 3 kWh", ["3 kwh", "1 × 3", "1 x 3"]),
   P("B: 3 × 1 = 3 kWh", ["3 × 1", "3 x 1", "both 3", "same energy", "also 3 kwh"]),
   P("same energy, so the same cost", ["same cost", "cost the same", "equal cost", "same"])],
  "Energy = power × time. A uses 1 kW × 3 h = 3 kWh and B uses 3 kW × 1 h = 3 kWh. They use the same energy, so they cost the same to run.",
  ["Work out the kWh for each.", "Cost depends on kWh.", "Compare."],
  "both 3 kWh → same cost",
  ["Both use 3 kWh, so they cost the same", "1 × 3 = 3 × 1 = 3 kWh, so the cost is equal"],
  ["B costs more because it is more powerful", "A costs more because it runs longer"], min_points=2,
  pitfalls=[PF(["costs more because it is more powerful", "costs more because it runs longer"], "Cost depends on ENERGY = power × time; both use 3 kWh.")])

Q("w14b_broken_earth", 4, "14f", "The earth wire of a metal-cased iron is broken, and then a live wire touches the casing. Explain what happens.",
  [P("the casing becomes live (at 230 V)", ["casing becomes live", "becomes live", "230", "casing is live"]),
   P("no large current flows to earth, so the fuse does not blow", ["fuse does not blow", "not blow", "no large current", "fuse will not", "fuse stays intact", "no current flows to earth"]),
   P("a person touching the casing becomes the path to earth and gets an electric shock", ["electric shock", "shock", "through the person", "through the body", "path to earth", "electrocuted"])],
  "With the earth wire broken, the casing becomes live at 230 V. No low-resistance path to earth exists, so no large current flows and the fuse does not blow. Anyone touching the casing becomes the path to earth, and current flows through their body, giving an electric shock.",
  ["What p.d. is the casing at?", "Is there a low-resistance path for a large current?", "What happens to someone who touches it?"],
  "casing live; fuse does not blow; person gets shock",
  ["The casing becomes live but the fuse does not blow, so a person touching it gets a shock", "no current flows to earth so the fuse stays intact and the user is electrocuted when touching the casing"],
  ["The fuse blows straight away", "Nothing, because the iron is switched on"], min_points=2,
  pitfalls=[PF(["fuse blows straight away", "fuse blows immediately"], "Without an earth path NO large current flows, so the fuse does NOT blow.")])

Q("w14b_power_from_energy", 4, "14b", "A kettle transfers 690 000 J of energy in 5 minutes from the 230 V mains. Explain how to find its power and the current it draws.",
  [P("P = E / t = 690 000 ÷ 300", ["e / t", "690 000 ÷ 300", "300 s", "energy ÷ time", "energy divided by time"]),
   P("= 2300 W", ["2300 w", "2300 watts", "2.3 kw"]),
   P("I = P / V = 2300 ÷ 230 = 10 A", ["10 a", "10 amps", "2300 ÷ 230"])],
  "Power = energy ÷ time = 690 000 ÷ 300 = 2300 W (time in seconds: 5 × 60 = 300 s). Current I = P / V = 2300 ÷ 230 = 10 A.",
  ["Convert 5 minutes to seconds.", "P = E / t.", "Then I = P / V."],
  "P = 2300 W; I = 10 A",
  ["P = 690 000 ÷ 300 = 2300 W, and I = 2300 ÷ 230 = 10 A", "the power is 2.3 kW, so the current is 10 A"],
  ["P = 690 000 ÷ 5 = 138 000 W", "I = 230 ÷ 2300 = 0.1 A"], min_points=2)

Q("w14b_heater_two_elements", 4, "14b", "A heater has two identical 1 kW elements, connected in parallel across the 230 V mains, each with its own switch. Explain the power when one and when both are on.",
  [P("each element has the full 230 V across it (parallel)", ["full 230", "230 v across each", "same p.d.", "parallel", "each has 230"]),
   P("one on: 1 kW", ["1 kw", "1000 w"]),
   P("both on: 2 kW (powers add; the mains supplies twice the current)", ["2 kw", "2000 w", "twice", "double"])],
  "In parallel each element has the full 230 V across it, so each always gives 1 kW. With one on, the power is 1 kW. With both on, the powers add to 2 kW, because the mains supplies twice the current.",
  ["What p.d. does each parallel element get?", "Does switching on the second change the first?", "Add the powers."],
  "1 kW; 2 kW",
  ["Each element has 230 V in parallel, so one gives 1 kW and both give 2 kW", "1 kW with one, 2 kW with both because the current doubles"],
  ["Both on gives 0.5 kW each", "Both on gives 1 kW"], min_points=2)

Q("w14b_reduce_bill", 4, "14c", "A family wants to reduce its electricity bill. Using E = P t, suggest two changes and explain each.",
  [P("use appliances of lower power (e.g. LED lamps instead of filament lamps)", ["lower power", "less power", "led", "energy-efficient", "smaller power"]),
   P("use appliances for less time (switch off when not needed)", ["less time", "shorter time", "switch off", "turn off", "fewer hours"]),
   P("both reduce the energy in kWh, and cost = kWh × price", ["fewer kwh", "less energy", "reduce the energy", "kwh"])],
  "Since E = P t, use appliances with a lower power, such as LED lamps instead of filament lamps, and use them for less time, switching them off when they are not needed. Both reduce the energy used in kWh, and the bill is the number of kWh × the price per kWh.",
  ["What two factors does E depend on?", "How can each be reduced?", "How does energy relate to cost?"],
  "lower P; shorter t → fewer kWh → lower cost",
  ["Use lower-power appliances such as LED lamps and use them for less time, because both reduce the energy in kWh", "switch things off sooner and choose energy-efficient appliances to use less energy"],
  ["Use a bigger fuse", "Use thicker cables"], min_points=2)

Q("w14b_wet_floor_shock", 4, "14d", "Explain why touching a live wire while standing barefoot on a wet floor is more dangerous than when wearing dry rubber shoes.",
  [P("current flows through the body to earth (ground)", ["to earth", "to the ground", "through the body", "through your body"]),
   P("a wet floor and bare feet give a low-resistance path, so a large current flows", ["low resistance", "large current", "water conducts", "wet floor conducts"]),
   P("dry rubber is an insulator with high resistance, so very little current flows", ["rubber is an insulator", "insulator", "high resistance", "little current", "rubber insulates"])],
  "Touching a live wire lets current flow through the body to the ground. With bare feet on a wet floor, the path has a low resistance because water conducts, so a large and possibly fatal current flows. Dry rubber soles are an insulator with a very high resistance, so very little current can flow.",
  ["Where does the current go after passing through the body?", "Does water lower or raise the resistance?", "What does rubber do?"],
  "current to earth; wet → low R → large I; rubber → high R",
  ["Current flows through the body to earth, and the wet floor gives a low resistance so a large current flows, while dry rubber insulates", "water conducts so a large current flows; rubber has a high resistance"],
  ["Rubber shoes attract electricity", "Water stops the current"], min_points=2)

Q("w14b_thin_fuse_wire", 4, "14e", "Explain why the wire in a 3 A fuse is thinner than the wire in a 13 A fuse.",
  [P("a thinner wire has a higher resistance", ["higher resistance", "more resistance", "larger resistance"]),
   P("so it heats up more for a given current", ["heats up more", "hotter", "more heat"]),
   P("and melts at a smaller current (3 A)", ["melts at a smaller current", "melts at a lower current", "smaller current", "lower current", "melts at 3"])],
  "A thinner wire has a smaller cross-sectional area and so a higher resistance. For a given current it heats up more, so it reaches its melting point at a smaller current: just above 3 A rather than 13 A.",
  ["How does thickness affect resistance?", "How does that affect heating?", "At what current does it melt?"],
  "thinner → higher R → heats more → melts at lower current",
  ["The thinner wire has a higher resistance, so it heats up more and melts at a smaller current", "it melts at a lower current because its higher resistance makes it hotter"],
  ["Thinner wire is cheaper", "Thick wire melts first"], min_points=2)

Q("w14b_kettle_cost_minutes", 4, "14c", "A 2.4 kW kettle is used for 3 minutes. Electricity costs 30 cents per kWh. Explain how to find the cost.",
  [P("time = 3 ÷ 60 = 0.05 h", ["0.05 h", "0.05", "3 ÷ 60", "3 / 60"]),
   P("energy = 2.4 × 0.05 = 0.12 kWh", ["0.12 kwh", "0.12"]),
   P("cost = 0.12 × 30 = 3.6 cents", ["3.6 cents", "3.6"])],
  "Convert the time to hours: 3 ÷ 60 = 0.05 h. Energy = 2.4 kW × 0.05 h = 0.12 kWh. Cost = 0.12 × 30 cents = 3.6 cents.",
  ["Convert minutes to hours.", "kWh = kW × h.", "Multiply by the price."],
  "0.05 h → 0.12 kWh → 3.6 cents",
  ["3 min = 0.05 h, so 2.4 × 0.05 = 0.12 kWh, costing 0.12 × 30 = 3.6 cents", "0.12 kWh at 30 cents gives 3.6 cents"],
  ["2.4 × 3 × 30 = 216 cents", "7.2 kWh"], min_points=2,
  pitfalls=[PF(["216 cents", "7.2 kwh"], "Time must be in HOURS: 3 min = 0.05 h.")])

Q("w14b_charge_and_energy", 4, "14b", "A heater draws 5.0 A from the 230 V mains for 10 minutes. Explain how to find the charge that passes and the energy transferred.",
  [P("Q = I t = 5.0 × 600 = 3000 C", ["3000 c", "3000 coulombs", "5 × 600", "q = it"]),
   P("E = Q V (or V I t) = 3000 × 230 = 690 000 J", ["690 000", "690000", "6.9 × 10", "e = qv", "q v"]),
   P("time in seconds: 600 s", ["600 s", "600 seconds"])],
  "Using t = 600 s: Q = I t = 5.0 × 600 = 3000 C. The energy E = Q V = 3000 × 230 = 690 000 J, which is the same as V I t = 230 × 5.0 × 600.",
  ["Convert 10 minutes to seconds.", "Q = I t.", "E = Q V."],
  "Q = 3000 C; E = 690 000 J",
  ["Q = 5 × 600 = 3000 C and E = QV = 3000 × 230 = 690 000 J", "3000 coulombs pass, transferring 690 000 joules"],
  ["Q = 50 C and E = 11 500 J", "E = 230 × 5 = 1150 J"], min_points=2)

# ---------------------------------------------------------------- L5
Q("w14b_claim_230_more_energy", 5, "14b", "A student says: 'A 230 V appliance always uses more energy than a 12 V appliance.' Evaluate this claim.",
  [P("wrong (not always): energy depends on current and time as well as p.d. (E = V I t)", ["wrong", "e = v i t", "e = vit", "current and time", "depends on the current", "depends on time"]),
   P("a 12 V appliance drawing a large current, or used for longer, can use more energy", ["large current", "used for longer", "longer time", "more current", "for longer"]),
   P("example: 12 V × 10 A = 120 W vs 230 V × 0.1 A = 23 W", ["120 w", "23 w", "example", "for example"])],
  "The claim is wrong. Energy depends on current and time as well as p.d.: E = V I t. A 12 V appliance drawing a large current, or used for longer, can use more energy; for example 12 V × 10 A = 120 W is more powerful than 230 V × 0.1 A = 23 W.",
  ["What equation gives the energy?", "Which other quantities matter?", "Give a counter-example."],
  "wrong; E = VIt depends on I and t too",
  ["Wrong: E = VIt, so a 12 V appliance with a large current or used for longer can use more energy", "not always; it depends on the current and the time too"],
  ["Correct, higher voltage always means more energy", "Correct, voltage is energy"], min_points=1)

Q("w14b_claim_kwh_power", 5, "14c", "A student writes: 'My heater has a power of 3 kWh.' Evaluate this statement and correct it.",
  [P("wrong: kWh is a unit of energy, not power", ["unit of energy", "energy not power", "kwh is energy", "measures energy", "not power"]),
   P("the power should be in kW (3 kW)", ["3 kw", "kilowatt", "should be kw", "in kw"]),
   P("kWh = kW × hours; e.g. 3 kW for 1 h uses 3 kWh", ["kw × h", "power × time", "3 kw for 1 hour", "kw times hours", "for 1 hour"])],
  "The statement is wrong: the kWh is a unit of energy, not power. The heater's power should be given in kW, e.g. 3 kW. A kWh is power in kW × time in hours: a 3 kW heater used for 1 hour uses 3 kWh of energy.",
  ["Is the kWh a unit of power or energy?", "What is the unit of power?", "Correct the statement."],
  "wrong; kWh = energy; power in kW",
  ["Wrong: kWh is a unit of energy, so the power is 3 kW; used for 1 hour it would use 3 kWh", "the power should be 3 kW, because kWh measures energy"],
  ["Correct, kWh is a unit of power", "Correct, it should be 3 kV"], min_points=2, pitfalls=[KWH_POWER])

Q("w14b_claim_plastic_no_safety", 5, "14f", "A student says: 'A plastic-cased (double-insulated) kettle needs no safety features at all.' Evaluate this.",
  [P("it does not need an earth wire, because its casing cannot become live", ["no earth wire", "does not need an earth", "cannot become live", "casing cannot be live", "plastic does not conduct"]),
   P("but it still needs a fuse to protect the cable from overheating if too much current flows", ["still needs a fuse", "needs a fuse", "fuse", "cable from overheating", "overheating"]),
   P("so the claim is wrong; other hazards (damaged insulation, water) still apply", ["wrong", "still", "damaged insulation", "water", "damp"])],
  "The claim is wrong. Being double insulated means it does not need an earth wire, because its plastic casing cannot become live. But it still needs a fuse in the live wire to protect the cable from overheating if a fault makes too much current flow, and hazards such as damaged insulation or water still apply.",
  ["Which safety feature does double insulation replace?", "What does the fuse protect?", "Evaluate."],
  "wrong; no earth needed but fuse still needed",
  ["Wrong: it does not need an earth wire, but it still needs a fuse to stop the cable overheating", "double insulation replaces the earth wire only; a fuse is still needed"],
  ["Correct, plastic kettles are completely safe", "Correct, plastic stops all currents"], min_points=2)

Q("w14b_claim_lowest_fuse", 5, "14e", "A student says: 'The lowest-rated fuse is always the safest choice.' Evaluate this claim.",
  [P("wrong: a fuse rated below the normal current would blow in normal use", ["wrong", "blow in normal use", "would blow", "below the normal current", "keep blowing"]),
   P("the appliance would not work", ["not work", "would not work", "cannot be used", "stop working"]),
   P("the correct fuse is the smallest rating just above the normal working current", ["just above", "slightly above", "smallest rating above", "slightly higher than", "above the normal current"])],
  "The claim is wrong. A fuse rated below the normal working current would blow every time the appliance is used, so the appliance would not work. The safest correct choice is the fuse with the smallest rating just above the normal working current.",
  ["What happens if the fuse rating is below the working current?", "Can the appliance be used?", "What is the right rule?"],
  "wrong; too low → blows in normal use; choose just above normal current",
  ["Wrong: a fuse below the normal current would blow in normal use; choose the one just above the working current", "the lowest fuse might keep blowing, so pick the smallest rating slightly above the normal current"],
  ["Correct, lower is always safer", "Use the highest fuse instead"], min_points=2)

Q("w14b_design_power", 5, "14b", "Design an experiment to measure the power of a low-voltage (12 V) immersion heater.",
  [P("connect the heater to a 12 V supply with an ammeter in series and a voltmeter in parallel", ["ammeter in series", "voltmeter in parallel", "ammeter", "voltmeter"]),
   P("calculate P = V I from the readings", ["p = v i", "p = vi", "v × i", "multiply"]),
   P("take several readings / repeat and average (or measure energy with a joulemeter and divide by time)", ["repeat", "average", "several readings", "joulemeter", "divide by time"])],
  "Connect the immersion heater to a 12 V supply with an ammeter in series and a voltmeter in parallel across the heater. Read V and I and calculate P = V I. Repeat the readings and take an average (or measure the energy with a joulemeter over a timed period and divide by the time).",
  ["Which meters do you need and how are they connected?", "How do you get power from the readings?", "How do you make it reliable?"],
  "ammeter series, voltmeter parallel; P = VI; repeat",
  ["Use an ammeter in series and a voltmeter in parallel, then P = VI; repeat and average", "measure V and I and multiply, taking several readings"],
  ["Measure the length of the heater", "Weigh the heater"], min_points=2)

Q("w14b_claim_standby_free", 5, "14c", "A student says: 'Leaving a 2 W television on standby all day costs nothing.' Evaluate this, for 20 h a day for 365 days at 30 cents per kWh.",
  [P("wrong: standby still uses energy", ["wrong", "still uses energy", "uses energy", "not nothing", "costs something"]),
   P("energy = 0.002 kW × 20 h × 365 = 14.6 kWh per year", ["14.6 kwh", "14.6", "0.002"]),
   P("cost = 14.6 × 30 = 438 cents ≈ $4.38 per year (small but not zero)", ["438", "4.38", "small", "not zero"])],
  "The claim is wrong. Standby still uses energy: 0.002 kW × 20 h × 365 = 14.6 kWh per year, which costs 14.6 × 30 = 438 cents, about $4.38 a year. The cost is small for one television but not zero, and it adds up over many appliances.",
  ["Does a 2 W appliance use energy?", "Work out kWh per year.", "Work out the cost."],
  "wrong; 14.6 kWh/year ≈ $4.38",
  ["Wrong: it uses 14.6 kWh a year, costing about $4.38, which is small but not zero", "standby uses 0.002 × 20 × 365 = 14.6 kWh, so it costs 438 cents"],
  ["Correct, standby uses no electricity", "Correct, 2 W is zero power"], min_points=2)

Q("w14b_claim_earth_current_shock", 5, "14f", "A student says: 'When the earth wire carries current, you will get a shock if you touch the appliance.' Evaluate this.",
  [P("wrong: when the earth wire carries a fault current, the casing is held near 0 V", ["wrong", "near 0 v", "0 v", "earth potential", "zero volts", "held at earth"]),
   P("the current flows through the low-resistance earth wire rather than through a person", ["low resistance", "rather than through", "instead of through", "not through the person", "through the earth wire"]),
   P("the large current quickly blows the fuse, disconnecting the live supply", ["blows the fuse", "fuse blows", "fuse melts", "trips", "disconnect"])],
  "The statement is wrong. When the earth wire carries a fault current, it keeps the casing near 0 V, because the current takes the low-resistance earth wire rather than passing through a person. The large current also quickly blows the fuse, disconnecting the live supply, so the appliance is made safe.",
  ["What p.d. is the casing at when it is earthed?", "Which path does the current prefer?", "What happens to the fuse?"],
  "wrong; casing held near 0 V; current takes earth wire; fuse blows",
  ["Wrong: the earth wire keeps the casing near 0 V and the large current blows the fuse, so the current does not flow through you", "the current flows through the low-resistance earth wire instead of through a person, and the fuse melts"],
  ["Correct, an earthed appliance always gives a shock", "Correct, earth wires carry the shock to you"], min_points=2)

Q("w14b_adapter_chain", 5, "14e", "A student plugs several adapters into one another and connects a heater, a kettle and an iron to the same socket. Evaluate the risks.",
  [P("the currents of the appliances add (in parallel), giving a very large total current", ["currents add", "large total current", "total current", "add up", "very large current"]),
   P("the socket and wiring may overheat, melting insulation and causing a fire", ["overheat", "fire", "melt", "too hot", "insulation"]),
   P("use separate sockets / do not exceed the rating of the socket or fuse", ["separate sockets", "do not exceed", "rating", "spread", "different sockets"])],
  "The appliances are in parallel, so their currents add, giving a very large total current through the socket and adapters. The socket and wiring can overheat, melting the insulation and starting a fire. The student should use separate sockets so the rating of each socket and fuse is not exceeded.",
  ["How do the currents of the appliances combine?", "What does a large current do to wiring?", "What should be done instead?"],
  "currents add → overload → overheating/fire; use separate sockets",
  ["Their currents add to a very large current, so the socket can overheat and cause a fire; use separate sockets", "overloading the socket makes it overheat; do not exceed its rating"],
  ["It is safe because each appliance has its own plug", "It saves electricity"], min_points=2)

Q("w14b_claim_breaker_no_earth", 5, "14f", "A student says: 'A house with circuit breakers does not need appliances to be earthed.' Evaluate this.",
  [P("wrong: a breaker only trips when a large current flows", ["wrong", "only trips", "large current", "trips when"]),
   P("without an earth wire, a live casing gives no low-resistance path, so no large current flows and the breaker does not trip", ["no low-resistance path", "does not trip", "no large current", "not trip", "no path"]),
   P("a person touching the casing would get a shock; earthing and breakers work together", ["shock", "work together", "both", "together", "touching the casing"])],
  "The claim is wrong. A circuit breaker only trips when a large current flows. If a metal casing becomes live with no earth wire, there is no low-resistance path, so no large current flows and the breaker does not trip; a person touching the casing would get a shock. Earthing provides the path for the large current, so earthing and breakers work together.",
  ["What makes a breaker trip?", "Is there a large current without an earth wire?", "What happens to the user?"],
  "wrong; breaker needs large current; earthing provides path; work together",
  ["Wrong: without earthing no large current flows, so the breaker does not trip and a person touching the casing gets a shock", "breakers only trip for large currents, so earthing is still needed; they work together"],
  ["Correct, breakers replace earthing", "Correct, breakers stop all shocks"], min_points=2)

Q("w14b_heater_choice_cost", 5, "14c", "A shop says: 'Our 1.5 kW heater is cheaper to run than a 2 kW heater.' A family would run the 1.5 kW heater for 4 h or the 2 kW heater for 3 h to warm the same room. Evaluate the claim.",
  [P("1.5 kW × 4 h = 6 kWh", ["6 kwh", "1.5 × 4"]),
   P("2 kW × 3 h = 6 kWh", ["2 × 3", "also 6", "both 6", "same energy"]),
   P("so the running cost is the same: cost depends on energy (kWh), not power alone", ["same cost", "the same", "depends on energy", "not power alone", "equal"])],
  "The claim is not true here. The 1.5 kW heater uses 1.5 × 4 = 6 kWh and the 2 kW heater uses 2 × 3 = 6 kWh. They use the same energy, so the running cost is the same: cost depends on energy (power × time), not on power alone.",
  ["Work out the kWh for each heater.", "Cost depends on kWh.", "Evaluate."],
  "both 6 kWh → same cost",
  ["Both use 6 kWh, so the cost is the same; cost depends on energy, not power alone", "1.5 × 4 = 2 × 3 = 6 kWh, so neither is cheaper"],
  ["Correct, lower power is always cheaper", "The 2 kW heater is cheaper"], min_points=2)
