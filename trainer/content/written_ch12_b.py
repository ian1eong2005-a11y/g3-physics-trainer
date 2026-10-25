"""Chapter 12 Electric Charge and Current: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import sketches2 as sk
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 12


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


AMPS_FOR_CHARGE = PF(["charge is measured in amperes", "charge in amps", "coulomb is the unit of current"],
                     "Charge is measured in COULOMBS; the ampere is the unit of CURRENT.")
CREATES_CHARGE = PF(["creates charge", "makes new charge", "charge is created", "produces charge from nothing"],
                    "Charge is never created: rubbing only TRANSFERS electrons from one object to the other.")

# ---------------------------------------------------------------- L1
Q("w12b_coulomb_def", 1, "12e", "State what is meant by one coulomb of charge, in terms of current and time.",
  [P("the charge that passes a point when a current of 1 A flows for 1 s", ["1 a for 1 s", "one ampere for one second", "1 ampere for 1 second", "current of 1 a", "one amp for one second", "1 amp for 1 second"])],
  "One coulomb is the charge that passes a point in a circuit when a current of one ampere flows for one second (Q = I t).",
  ["Use Q = I × t.", "What current and time give Q = 1?", "State it."],
  "1 C = 1 A × 1 s",
  ["The charge passing a point when 1 A flows for 1 s", "it is the charge carried by a current of one ampere in one second"],
  ["The charge on one electron", "One volt per ampere"], pitfalls=[AMPS_FOR_CHARGE])

Q("w12b_ammeter_unit", 1, "12c", "State the name of the instrument that measures current, the unit of current, and how the instrument is connected.",
  [P("ammeter", ["ammeter"]),
   P("ampere (A)", ["ampere", "amp", "amps", "amperes"]),
   P("connected in series", ["in series", "series"])],
  "Current is measured with an ammeter, in amperes (A). The ammeter is connected in series with the component.",
  ["Which meter has the letter A in its symbol?", "What is the unit?", "Series or parallel?"],
  "ammeter; ampere; in series",
  ["An ammeter, measuring in amperes, connected in series", "ammeter in series; unit amps"],
  ["A voltmeter in volts", "An ammeter connected in parallel, in coulombs"], min_points=2,
  pitfalls=[PF(["ammeter connected in parallel", "ammeter in parallel"], "An ammeter is connected in SERIES."), AMPS_FOR_CHARGE])

Q("w12b_voltmeter_unit", 1, "12g", "State the name of the instrument that measures potential difference, its unit, and how it is connected.",
  [P("voltmeter", ["voltmeter"]),
   P("volt (V)", ["volt", "volts"]),
   P("connected in parallel across the component", ["in parallel", "parallel", "across the component", "across"])],
  "Potential difference is measured with a voltmeter, in volts (V). The voltmeter is connected in parallel, across the component.",
  ["Which meter has the letter V in its symbol?", "What is the unit?", "Is it connected across or in line with the component?"],
  "voltmeter; volt; in parallel",
  ["A voltmeter, in volts, connected in parallel across the component", "voltmeter across the component, unit volts"],
  ["An ammeter in amperes", "A voltmeter connected in series, in joules"], min_points=2,
  pitfalls=[PF(["voltmeter connected in series", "voltmeter in series"], "A voltmeter is connected in PARALLEL, across the component.")])

Q("w12b_resistance_formula", 1, "12h", "State the relationship between resistance, potential difference and current.",
  [P("resistance = p.d. ÷ current (R = V / I)", ["r = v / i", "p.d. ÷ current", "pd ÷ current", "potential difference ÷ current", "potential difference divided by current", "voltage divided by current", "v / i", "pd divided by current"])],
  "Resistance = potential difference ÷ current, or R = V / I.",
  ["Resistance links V and I.", "Which one is divided by which?", "Write it."],
  "R = V / I",
  ["R = V / I", "resistance equals potential difference divided by current"],
  ["R = V × I", "R = I / V"],
  pitfalls=[PF(["r = v × i", "r = i / v", "v × i", "current divided by"], "Resistance = p.d. ÷ current: R = V / I.")])

Q("w12b_ohm_meaning", 1, "12h", "State what is meant by a resistance of 1 ohm.",
  [P("a p.d. of 1 V drives a current of 1 A through it (1 V per ampere)", ["1 v per", "1 volt per", "1 v drives 1 a", "one volt per ampere", "1 v across", "one volt drives a current of one ampere", "1 volt drives 1 amp"])],
  "A component has a resistance of 1 ohm if a potential difference of 1 V across it drives a current of 1 A through it (1 Ω = 1 V/A).",
  ["Use R = V / I.", "What V and I give R = 1?", "State it."],
  "1 Ω = 1 V per A",
  ["A p.d. of 1 V drives a current of 1 A through it", "one volt per ampere"],
  ["1 A per volt", "1 C per second"],
  pitfalls=[PF(["a per volt", "amp per volt", "ampere per volt"], "Resistance is VOLTS per AMPERE (R = V / I), not amperes per volt.")])

Q("w12b_conventional_direction", 1, "12d", "State the direction of conventional current in a circuit connected to a cell.",
  [P("from the positive terminal round the circuit to the negative terminal", ["positive to negative", "positive terminal to the negative", "from positive to negative", "+ to −", "out of the positive", "from the positive terminal"])],
  "Conventional current flows from the positive terminal of the cell, round the external circuit, to the negative terminal.",
  ["Conventional current was defined before electrons were discovered.", "Which terminal does it leave?", "State it."],
  "positive → negative",
  ["From the positive terminal to the negative terminal", "it flows from positive to negative around the circuit"],
  ["From negative to positive", "Both ways at once"],
  pitfalls=[PF(["negative to positive", "from the negative terminal"], "That is ELECTRON flow. Conventional current is from + to −.")])

Q("w12b_charge_carriers_metal", 1, "12c", "State which particles carry the current in a metal wire.",
  [P("free electrons (delocalised electrons)", ["free electrons", "electrons", "delocalised electrons", "mobile electrons"])],
  "In a metal wire the current is carried by free (delocalised) electrons.",
  ["They are negatively charged.", "They are free to move through the metal.", "Name them."],
  "free electrons",
  ["Free electrons", "the electrons that are free to move"],
  ["Protons", "Positive ions moving along the wire"],
  pitfalls=[PF(["protons", "positive ions moving", "neutrons"], "In metals only free ELECTRONS move; the positive ions stay in place.")])

Q("w12b_area_resistance", 1, "12j", "State how the resistance of a wire depends on its cross-sectional area, for a fixed material and length.",
  [P("resistance is inversely proportional to the cross-sectional area (larger area, smaller resistance)", ["inversely proportional", "larger area smaller resistance", "thicker wire less resistance", "bigger area lower resistance", "smaller resistance"])],
  "The resistance is inversely proportional to the cross-sectional area: doubling the area halves the resistance.",
  ["Is a thick wire easier or harder for current to flow through?", "What kind of proportionality?", "State it."],
  "R ∝ 1/A",
  ["Resistance is inversely proportional to the cross-sectional area", "a larger area gives a smaller resistance"],
  ["Resistance is directly proportional to the area", "Area makes no difference"],
  pitfalls=[PF(["directly proportional to the area", "larger area larger resistance", "thicker wire more resistance"], "A THICKER wire has LESS resistance: R is inversely proportional to area.")])

Q("w12b_length_resistance", 1, "12j", "State how the resistance of a wire depends on its length, for a fixed material and cross-sectional area.",
  [P("resistance is directly proportional to length (double length, double resistance)", ["directly proportional", "proportional to the length", "double the length double", "longer more resistance", "longer wire greater resistance"])],
  "The resistance is directly proportional to the length: doubling the length doubles the resistance.",
  ["Is a longer wire harder for current to pass through?", "What kind of proportionality?", "State it."],
  "R ∝ L",
  ["Resistance is directly proportional to the length", "doubling the length doubles the resistance"],
  ["Resistance is inversely proportional to the length", "Length does not matter"],
  pitfalls=[PF(["inversely proportional to the length", "longer less resistance"], "A LONGER wire has MORE resistance.")])

Q("w12b_electron_charge", 1, "12a", "State the type of charge carried by an electron and by a proton.",
  [P("electron: negative", ["electron is negative", "electrons are negative", "electron negative", "negative electron", "electron has a negative"]),
   P("proton: positive", ["proton is positive", "protons are positive", "proton positive", "positive proton", "proton has a positive"])],
  "An electron carries a negative charge and a proton carries a positive charge.",
  ["Which particle orbits the nucleus?", "Which is in the nucleus?", "State both charges."],
  "electron −; proton +",
  ["An electron is negative and a proton is positive", "electrons are negative, protons are positive"],
  ["Electrons are positive and protons negative", "Both are neutral"], min_points=2,
  pitfalls=[PF(["electrons are positive", "electron is positive", "protons are negative", "proton is negative"], "Electrons are NEGATIVE; protons are POSITIVE.")])

# ---------------------------------------------------------------- L2
Q("w12b_meaning_2A", 2, "12e", "A current of 2 A flows through a lamp. Explain what this means in terms of charge.",
  [P("2 coulombs of charge pass through the lamp every second", ["2 c every second", "2 coulombs per second", "2 c per second", "2 coulombs every second", "2 c each second", "two coulombs per second", "2 c of charge flows each second"])],
  "A current of 2 A means that 2 coulombs of charge pass through the lamp every second (I = Q ÷ t).",
  ["Current is the rate of flow of charge.", "1 A = 1 C per second.", "Explain 2 A."],
  "2 C per second",
  ["2 coulombs of charge pass through the lamp every second", "2 C of charge flows each second"],
  ["2 electrons pass every second", "The lamp uses 2 J"],
  pitfalls=[PF(["2 electrons", "two electrons"], "2 A is 2 COULOMBS per second, which is a huge number of electrons.")])

Q("w12b_rubbing_polythene", 2, "12a", "A polythene rod is rubbed with a cloth and becomes negatively charged. Explain how this happens.",
  [P("electrons are transferred (rubbed off) from the cloth onto the rod", ["electrons are transferred", "electrons move from the cloth", "gains electrons", "electrons from the cloth", "rod gains electrons", "transfer of electrons"]),
   P("the cloth loses electrons and becomes positively charged", ["cloth loses electrons", "cloth becomes positive", "cloth is positive", "cloth positively charged", "cloth is left positive"])],
  "Friction transfers electrons from the cloth onto the polythene rod. The rod gains electrons and becomes negatively charged, while the cloth loses electrons and is left positively charged.",
  ["Which particles move when objects are rubbed?", "Which way do they move here?", "What happens to the cloth?"],
  "electrons move cloth → rod; cloth becomes positive",
  ["Electrons are transferred from the cloth to the rod, so the rod gains electrons and the cloth becomes positive", "the rod gains electrons from the cloth; the cloth is left positive"],
  ["Positive charges move from the rod to the cloth", "Rubbing creates negative charge"], min_points=1,
  pitfalls=[CREATES_CHARGE, PF(["positive charges move", "protons move", "protons are transferred"], "Only ELECTRONS move when objects are rubbed.")])

Q("w12b_meaning_6V", 2, "12g", "The p.d. across a lamp is 6 V. Explain what this means.",
  [P("6 J of work is done (energy transferred) for each coulomb of charge passing through the lamp", ["6 j per coulomb", "6 joules per coulomb", "6 j for each coulomb", "6 j of energy for every coulomb", "6 joules for each coulomb", "6 j per c", "6 j of energy is transferred for each coulomb", "6 joules of work are done per coulomb", "6 j of electrical energy is converted", "for every coulomb", "for each coulomb"])],
  "A p.d. of 6 V means that 6 J of electrical energy is converted (work done) for every coulomb of charge passing through the lamp.",
  ["p.d. is work done per unit charge.", "1 V = 1 J per C.", "Explain 6 V."],
  "6 J per coulomb",
  ["6 J of energy is transferred for each coulomb of charge through the lamp", "6 joules of work are done per coulomb"],
  ["6 C pass per second", "6 A flows through the lamp"],
  pitfalls=[PF(["6 c pass per second", "6 a flows", "6 coulombs per second"], "Volts measure energy per coulomb, not charge per second.")])

Q("w12b_meaning_5ohm", 2, "12h", "A resistor has a resistance of 5 Ω. Explain what this means.",
  [P("a p.d. of 5 V is needed to drive a current of 1 A through it (5 V per ampere)", ["5 v per", "5 volts per", "5 v to drive 1 a", "5 v for each ampere", "5 v for every ampere", "5 volts for each amp", "5 v for 1 a", "5 volts to drive 1 amp", "5 v is needed to drive 1 a"])],
  "A resistance of 5 Ω means that a potential difference of 5 V is needed across the resistor for each ampere of current through it (R = V / I).",
  ["Use R = V / I.", "What p.d. would 1 A need?", "Explain."],
  "5 V per ampere",
  ["A p.d. of 5 V is needed to drive 1 A through it", "5 volts for each amp of current"],
  ["5 A flows through it", "It uses 5 J of energy"])

Q("w12b_copper_wires", 2, "12j", "Explain why connecting wires in a circuit are made of thick copper.",
  [P("copper has a low resistance (good conductor)", ["low resistance", "good conductor", "conducts well", "very low resistance"]),
   P("thick wire has a large cross-sectional area, so even lower resistance", ["thick", "large cross-sectional area", "larger area", "bigger area"]),
   P("so little energy is wasted in the wires (most p.d. is across the components)", ["little energy", "less energy wasted", "not wasted", "do not heat up", "less heating", "energy goes to the components"])],
  "Copper is a very good conductor with low resistance, and a thick wire has a large cross-sectional area, which lowers the resistance further. So very little energy is wasted in the connecting wires.",
  ["Is copper a good conductor?", "How does thickness affect resistance?", "Why do we want low resistance wires?"],
  "copper low resistance; thick → larger area → lower R; little energy wasted",
  ["Copper has low resistance and thick wire has a large cross-sectional area, so little energy is wasted in the wires", "a thick copper wire is a good conductor with very low resistance"],
  ["Copper is magnetic", "Thick wires are stronger only"], min_points=2)

Q("w12b_electron_direction", 2, "12d", "Fig. 1 shows a lamp connected to a cell. Describe the direction in which electrons flow in the wires, and compare it with conventional current.",
  [P("electrons flow from the negative terminal round the circuit to the positive terminal", ["negative to positive", "from the negative terminal", "negative terminal to the positive", "out of the negative"]),
   P("this is opposite to the conventional current (positive to negative)", ["opposite", "other way", "reverse", "opposite direction"])],
  "Electrons flow out of the negative terminal, round the circuit and into the positive terminal. This is opposite to the direction of conventional current, which flows from positive to negative.",
  ["Electrons are negative; which terminal repels them?", "Which terminal attracts them?", "Compare with conventional current."],
  "electrons − → +; opposite to conventional current",
  ["Electrons flow from the negative terminal to the positive terminal, opposite to conventional current", "from negative to positive, which is the opposite direction to conventional current"],
  ["Electrons flow from positive to negative, the same as conventional current", "Electrons do not move"], min_points=2,
  pitfalls=[PF(["electrons flow from positive to negative", "same as conventional current", "same direction as conventional"], "Electrons flow from − to +, OPPOSITE to conventional current.")],
  figure=lambda: sk.circuit(series=[("lamp", None)], emf="+  −"))

Q("w12b_double_r_same_v", 2, "12i", "A resistor is replaced by one with twice the resistance, with the same p.d. across it. State and explain what happens to the current.",
  [P("the current halves", ["halves", "half", "halved"]),
   P("because I = V / R and V is unchanged", ["i = v / r", "v / r", "same p.d.", "same pd", "inversely proportional", "v is unchanged", "same voltage"])],
  "The current halves, because I = V / R: with V unchanged, doubling R halves I.",
  ["Rearrange R = V / I for I.", "What happens to I if R doubles and V is fixed?", "State and explain."],
  "current halves (I = V/R)",
  ["The current halves because I = V / R and the p.d. is the same", "it is halved since current is inversely proportional to resistance at the same voltage"],
  ["The current doubles", "The current stays the same"], min_points=2,
  pitfalls=[PF(["current doubles", "current stays the same"], "With the same p.d., doubling R HALVES the current.")])

Q("w12b_insulator_conductor", 2, "12c", "Explain why a copper wire conducts electricity but a plastic rod does not.",
  [P("copper has free electrons that can move through it", ["free electrons", "electrons free to move", "electrons can move", "mobile electrons", "delocalised electrons", "electrons that can move"]),
   P("plastic has no free electrons (they are held tightly), so no charge can flow", ["no free electrons", "held tightly", "cannot move", "bound", "not free", "cannot flow"])],
  "Copper contains free electrons that can move through the metal, so charge can flow. In plastic the electrons are held tightly in the atoms, so there are no free electrons and no charge can flow.",
  ["What carries current in a metal?", "Are there such carriers in plastic?", "Explain."],
  "copper: free electrons; plastic: no free electrons",
  ["Copper has free electrons that can move, but plastic has no free electrons", "in plastic the electrons are held tightly so charge cannot flow, while copper has mobile electrons"],
  ["Copper is heavier", "Plastic has no atoms"], min_points=2)

Q("w12b_ammeter_terminals", 2, "12c", "Describe how an ammeter should be connected to measure the current through a lamp correctly.",
  [P("in series with the lamp", ["in series", "series"]),
   P("its positive (red) terminal connected towards the positive terminal of the cell", ["positive terminal", "red terminal", "+ terminal", "positive to positive", "positive side"]),
   P("choose a suitable range / check for zero error", ["range", "zero error", "check it reads zero", "reads zero"])],
  "Connect the ammeter in series with the lamp, with its positive (red) terminal on the side connected to the positive terminal of the cell. Choose a suitable range and check that it reads zero before the switch is closed.",
  ["Series or parallel?", "Which way round are the terminals connected?", "What should you check first?"],
  "series; + to +; suitable range / zero",
  ["In series with the lamp, with its positive terminal towards the positive of the cell", "connect it in series, red terminal to the positive side, and check it reads zero"],
  ["In parallel across the lamp", "Either way round in parallel"], min_points=2,
  pitfalls=[PF(["in parallel across the lamp", "connected in parallel", "way round in parallel"], "An ammeter is connected in SERIES.")])

Q("w12b_charge_time", 2, "12e", "The same current flows through a resistor for 2 minutes instead of 1 minute. State and explain what happens to the charge that passes.",
  [P("the charge doubles", ["doubles", "twice", "double"]),
   P("because Q = I t and I is the same", ["q = i t", "q = it", "charge = current × time", "current × time", "proportional to time", "same current", "current is the same"])],
  "The charge that passes doubles, because Q = I t: with the same current, doubling the time doubles the charge.",
  ["Write the equation linking charge, current and time.", "Which quantity changes?", "State and explain."],
  "charge doubles (Q = It)",
  ["The charge doubles because Q = It and the current is the same", "twice as much charge passes since charge = current × time"],
  ["The charge halves", "The charge stays the same"], min_points=2)

# ---------------------------------------------------------------- L3
Q("w12b_charge_half_minute", 3, "12e", "A cell drives a current of 0.5 A through a lamp for 1 minute. Explain how you find the charge that passes, and give the value.",
  [P("use Q = I t", ["q = i t", "q = it", "charge = current × time", "current × time"]),
   P("convert the time to seconds: 60 s", ["60 s", "60 seconds", "in seconds", "0.5 × 60"]),
   P("Q = 0.5 × 60 = 30 C", ["30 c", "30 coulombs"])],
  "Use Q = I t with the time in seconds: Q = 0.5 A × 60 s = 30 C.",
  ["Which equation links Q, I and t?", "What unit must time be in?", "Calculate."],
  "Q = It = 0.5 × 60 = 30 C",
  ["Q = It = 0.5 × 60 = 30 C", "charge = current × time in seconds, so 30 coulombs"],
  ["Q = 0.5 × 1 = 0.5 C", "Q = 60 ÷ 0.5 = 120 C"], min_points=2,
  pitfalls=[PF(["0.5 c", "120 c"], "Use Q = I × t with t = 60 s: Q = 30 C.")])

Q("w12b_electrons_attracted", 3, "12d", "Explain, in terms of charges, why electrons in a wire move towards the positive terminal of a cell.",
  [P("electrons are negatively charged", ["electrons are negative", "negatively charged", "negative charge", "negative electrons"]),
   P("they are attracted by the positive terminal (unlike charges attract)", ["attracted", "unlike charges attract", "opposite charges attract", "pulled towards"]),
   P("and repelled by the negative terminal (like charges repel)", ["repelled", "like charges repel", "pushed away"])],
  "Electrons are negatively charged. They are repelled by the negative terminal (like charges repel) and attracted by the positive terminal (unlike charges attract), so they drift towards the positive terminal.",
  ["What is the charge on an electron?", "Which terminal attracts it?", "Which terminal repels it?"],
  "electrons negative: attracted to +, repelled by −",
  ["Electrons are negative, so they are attracted to the positive terminal and repelled by the negative terminal", "unlike charges attract, so the negative electrons move towards the positive terminal"],
  ["Electrons are positive so they move to the positive terminal", "Gravity pulls them"], min_points=2,
  pitfalls=[PF(["electrons are positive"], "Electrons are NEGATIVE.")])

Q("w12b_r_unchanged_LA", 3, "12j", "Wire Q is made of the same metal as wire P but is twice as long and has twice the cross-sectional area. Explain how their resistances compare.",
  [P("doubling the length doubles the resistance", ["doubling the length doubles", "twice as long doubles", "length doubles the resistance", "proportional to length", "double length double"]),
   P("doubling the area halves the resistance", ["doubling the area halves", "area halves", "inversely proportional to area", "twice the area halves", "double area half"]),
   P("so the resistances are equal", ["the same", "equal", "same resistance", "no change"])],
  "Resistance is proportional to length, so doubling the length doubles the resistance; it is inversely proportional to area, so doubling the area halves it. The two effects cancel, so the resistances are equal.",
  ["What does doubling the length do?", "What does doubling the area do?", "Combine the two."],
  "×2 for length, ÷2 for area → same resistance",
  ["Doubling the length doubles R but doubling the area halves it, so they have the same resistance", "R is proportional to length and inversely proportional to area, so the resistance is the same"],
  ["Q has four times the resistance", "Q has half the resistance"], min_points=2)

Q("w12b_ammeter_low_r", 3, "12c", "Explain why an ammeter is designed to have a very small resistance.",
  [P("it is connected in series, so all the current passes through it", ["in series", "series", "all the current"]),
   P("a small resistance does not reduce (change) the current it is measuring", ["does not reduce the current", "does not change the current", "does not affect the current", "current stays the same", "not reduce the current"])],
  "An ammeter is connected in series, so the whole current flows through it. It is made with a very small resistance so that it does not reduce the current it is measuring.",
  ["How is an ammeter connected?", "What would a large resistance in series do to the current?", "Explain."],
  "in series; low R so it does not change the current",
  ["It is in series, so a small resistance does not reduce the current it measures", "a low resistance means connecting the ammeter in series does not change the current"],
  ["So that it measures volts", "So that it gets hot"], min_points=2)

Q("w12b_voltmeter_high_r", 3, "12g", "Explain why a voltmeter is designed to have a very large resistance.",
  [P("it is connected in parallel across the component", ["in parallel", "parallel", "across the component"]),
   P("a large resistance means very little current flows through the voltmeter, so it does not disturb the circuit", ["very little current", "almost no current", "does not take current", "does not disturb", "does not affect the circuit", "takes very little current"])],
  "A voltmeter is connected in parallel across a component. Its very large resistance means that almost no current flows through it, so it does not change the current or p.d. it is measuring.",
  ["How is a voltmeter connected?", "What would a low-resistance voltmeter in parallel do?", "Explain."],
  "in parallel; high R so almost no current through it",
  ["It is connected in parallel, and a large resistance means almost no current flows through it so it does not disturb the circuit", "being in parallel, its high resistance means it takes very little current from the component"],
  ["So it can measure large currents", "So that it heats up"], min_points=2)

Q("w12b_pd_rises_with_current", 3, "12i", "The current through a fixed resistor increases from 0.2 A to 0.4 A. Explain what happens to the p.d. across it.",
  [P("the p.d. doubles", ["doubles", "twice", "double"]),
   P("because V = I R and R is constant", ["v = i r", "v = ir", "r is constant", "same resistance", "proportional to the current", "fixed resistance", "fixed resistor", "resistance stays the same"])],
  "The p.d. doubles. For a fixed resistor V = I R with R constant, so the p.d. is proportional to the current: doubling the current doubles the p.d.",
  ["Write V in terms of I and R.", "Which stays constant?", "What happens to V?"],
  "V doubles (V = IR, R fixed)",
  ["The p.d. doubles because V = IR and R stays the same", "the voltage is proportional to the current for a fixed resistor, so it doubles"],
  ["The p.d. halves", "The p.d. stays the same"], min_points=2)

Q("w12b_metal_conductor_why", 3, "12c", "Explain how a current flows in a metal wire when it is connected to a cell.",
  [P("the metal contains free electrons", ["free electrons", "electrons free to move", "delocalised electrons"]),
   P("the cell's p.d. makes the free electrons drift in one direction (towards the positive terminal)", ["drift", "move in one direction", "towards the positive", "flow towards", "pushed round", "pushes the free electrons round"]),
   P("this flow of charge is the current", ["flow of charge", "rate of flow of charge", "movement of charge"])],
  "A metal contains free electrons. When the wire is connected to a cell, the p.d. makes these electrons drift through the wire towards the positive terminal. This flow of charge is the electric current.",
  ["What particles in the metal can move?", "What does the cell make them do?", "What do we call this?"],
  "free electrons drift (to +) → flow of charge = current",
  ["The free electrons in the metal drift towards the positive terminal, and this flow of charge is the current", "the cell pushes the free electrons round the circuit, giving a flow of charge"],
  ["The cell fills the wire with new electrons", "Protons flow along the wire"], min_points=2,
  pitfalls=[PF(["protons flow", "protons move"], "Only free ELECTRONS move in a metal.")])

Q("w12b_halve_both", 3, "12j", "A wire is cut in half (half the length). Explain what happens to the resistance of each piece, and the resistance if the two halves are then twisted together side by side to act as one thick wire.",
  [P("each half has half the resistance (resistance proportional to length)", ["half the resistance", "halves", "proportional to length", "half each"]),
   P("side by side the area doubles, so the resistance halves again: one quarter of the original", ["quarter", "one quarter", "1/4", "a quarter", "four times smaller"])],
  "Resistance is proportional to length, so each half has half the original resistance. Twisted side by side they act as a wire of the same half length but twice the cross-sectional area, which halves the resistance again, giving a quarter of the original resistance.",
  ["Resistance and length?", "What happens to the area when the halves are side by side?", "Combine."],
  "each half: ½R; side by side: ¼R",
  ["Each half has half the resistance; side by side the area doubles so the resistance is a quarter of the original", "half each, then a quarter when combined"],
  ["Each half has double the resistance", "The resistance stays the same"], min_points=2)

Q("w12b_two_rods_charged", 3, "12b", "Two acetate strips are both rubbed with the same cloth and hung near each other. Predict and explain what happens.",
  [P("they repel (move apart)", ["repel", "move apart", "push apart"]),
   P("both get the same type of charge (both positive)", ["same charge", "same type of charge", "both positive", "like charges", "same sign"]),
   P("like charges repel", ["like charges repel", "same charges repel"])],
  "They repel and move apart. Rubbing both with the same cloth gives them the same type of charge (acetate becomes positive by losing electrons), and like charges repel.",
  ["Will they have the same or opposite charges?", "What do like charges do?", "Predict."],
  "same charge → repel",
  ["They repel because both have the same type of charge and like charges repel", "both are positive, so they push apart"],
  ["They attract because they are both charged", "Nothing happens"], min_points=2,
  pitfalls=[PF(["they attract", "attract each other"], "Two strips with the SAME charge repel.")])

Q("w12b_resistance_reading", 3, "12i", "Fig. 1 shows the circuit used. A student reads 3.0 V on the voltmeter and 0.15 A on the ammeter. Explain how to find the resistance of R and give the value.",
  [P("use R = V / I", ["r = v / i", "v / i", "p.d. ÷ current", "divide the voltage by the current", "voltage divided by current"]),
   P("R = 3.0 ÷ 0.15 = 20 Ω", ["20"])],
  "Use R = V / I: R = 3.0 V ÷ 0.15 A = 20 Ω.",
  ["Which equation links R, V and I?", "Which reading goes on top?", "Calculate."],
  "R = V/I = 3.0 ÷ 0.15 = 20 Ω",
  ["R = V / I = 3.0 ÷ 0.15 = 20 Ω", "divide the voltage by the current: 20 ohms"],
  ["R = 3.0 × 0.15 = 0.45 Ω", "R = 0.15 ÷ 3.0 = 0.05 Ω"], min_points=2,
  pitfalls=[PF(["0.45", "0.05"], "R = V ÷ I = 3.0 ÷ 0.15 = 20 Ω.")],
  figure=lambda: sk.circuit(series=[("R", "R")], emf="", ammeter="main", voltmeter=("series", 0)))

# ---------------------------------------------------------------- L4
Q("w12b_chain_charges", 4, "12b", "Three charged spheres X, Y and Z hang from threads. X repels Y, and Y attracts Z. Z is positively charged. Deduce the charges on X and Y, explaining each step.",
  [P("Y attracts positive Z, so Y is negative (unlike charges attract)", ["y is negative", "y must be negative", "y negative"]),
   P("X repels Y, so X has the same charge: X is negative (like charges repel)", ["x is negative", "x must be negative", "x negative", "x is negative too", "both negative"])],
  "Y attracts Z, which is positive; unlike charges attract, so Y is negative. X repels Y; like charges repel, so X has the same charge as Y and is also negative.",
  ["Start with Z, whose charge you know.", "Attract means unlike; repel means like.", "Work out Y, then X."],
  "Y negative (attracts +Z); X negative (repels Y)",
  ["Y is negative because it attracts positive Z, and X is negative because it repels Y", "unlike charges attract so Y is negative; like charges repel so X is negative too"],
  ["X and Y are both positive", "Y is positive and X is negative"], min_points=2,
  pitfalls=[PF(["y is positive", "x is positive", "both positive"], "Y attracts POSITIVE Z, so Y is NEGATIVE; X repels Y, so X is negative too.")])

Q("w12b_energy_from_pd", 4, "12g", "The p.d. across a lamp is 6.0 V. Explain how much energy is transferred in the lamp when 3.0 C of charge passes through it.",
  [P("p.d. is the work done (energy transferred) per unit charge", ["per unit charge", "per coulomb", "work done per", "energy per coulomb", "w = q v", "w = qv", "e = q v"]),
   P("so 6.0 J per coulomb × 3.0 C = 18 J", ["18 j", "18 joules"])],
  "The p.d. is the energy transferred per unit charge, so 6.0 V means 6.0 J for each coulomb. For 3.0 C the energy is 6.0 × 3.0 = 18 J.",
  ["What does 6.0 V mean per coulomb?", "How many coulombs pass?", "Multiply."],
  "W = QV = 3.0 × 6.0 = 18 J",
  ["p.d. is energy per coulomb, so 6.0 J per coulomb × 3.0 C = 18 J", "W = QV, so the energy is 18 J"],
  ["2 J because 6 ÷ 3", "6 J"], min_points=2,
  pitfalls=[PF(["2 j", "2 joules"], "Energy = charge × p.d. = 3.0 × 6.0 = 18 J.")])

Q("w12b_stretched_wire", 4, "12j", "A wire is stretched until it is twice as long; its volume stays the same, so its cross-sectional area halves. Explain what happens to its resistance.",
  [P("doubling the length doubles the resistance", ["doubling the length doubles", "twice as long", "length doubles", "proportional to length", "×2 for length", "both changes double"]),
   P("halving the area doubles the resistance again", ["halving the area doubles", "area halves", "inversely proportional to area", "half the area doubles", "doubles it again"]),
   P("so the resistance becomes four times as large", ["four times", "4 times", "quadruples", "×4", "4r"])],
  "Resistance is proportional to length, so doubling the length doubles it. It is inversely proportional to area, so halving the area doubles it again. Overall the resistance becomes four times as large.",
  ["What does doubling the length do?", "What does halving the area do?", "Combine the two factors."],
  "×2 × ×2 = ×4",
  ["Doubling the length doubles R and halving the area doubles it again, so the resistance is four times as large", "it quadruples because both changes double the resistance"],
  ["It doubles", "It stays the same because the volume is the same"], min_points=2,
  pitfalls=[PF(["stays the same because the volume", "volume is the same so"], "Same volume does NOT mean same resistance: longer AND thinner → 4× the resistance.")])

Q("w12b_ratio_constant", 4, "12i", "A student records the readings below for a component. Explain whether the component has a constant resistance.\n\n| V / V | 1.0 | 2.0 | 3.0 |\n|---|---|---|---|\n| I / A | 0.10 | 0.20 | 0.30 |",
  [P("work out R = V / I for each pair", ["v / i", "r = v / i", "divide v by i", "each pair", "for each reading", "every pair", "each reading"]),
   P("each gives 10 Ω", ["10"]),
   P("so the resistance is constant (V is proportional to I)", ["constant", "the same", "proportional", "does not change"])],
  "Working out R = V / I for each pair gives 1.0 ÷ 0.10 = 10 Ω, 2.0 ÷ 0.20 = 10 Ω and 3.0 ÷ 0.30 = 10 Ω. The ratio is the same each time, so the resistance is constant: the current is proportional to the p.d.",
  ["Calculate V ÷ I for each column.", "Are the answers the same?", "Conclude."],
  "V/I = 10 Ω each time → constant",
  ["V / I is 10 Ω for every pair, so the resistance is constant", "each reading gives R = 10 Ω, so V is proportional to I and the resistance does not change"],
  ["The resistance increases because V increases", "The resistance decreases because I increases"], min_points=2,
  pitfalls=[PF(["resistance increases", "resistance decreases"], "V ÷ I is 10 Ω for every pair, so R is CONSTANT.")])

Q("w12b_cell_gives_energy", 4, "12f", "A student says that a cell 'supplies the electrons' for a circuit. Explain what a cell actually supplies.",
  [P("the electrons are already in the wires (free electrons in the metal)", ["already in the wires", "already in the wire", "already there", "electrons are in the metal", "free electrons in the wire", "already in the metal"]),
   P("the cell supplies energy to the charges (its e.m.f. pushes them round)", ["supplies energy", "gives energy", "energy to the charges", "pushes them round", "e.m.f.", "emf"]),
   P("the energy is transferred in the components (e.g. lamp)", ["transferred in the lamp", "in the components", "converted in", "light and heat", "lamp"])],
  "The electrons are already in the wires: they are the free electrons of the metal. The cell supplies energy to the charges, its e.m.f. pushing them round the circuit, and this energy is transferred in the components such as the lamp.",
  ["Where are the moving electrons before the cell is connected?", "What does the cell give them?", "Where does that go?"],
  "electrons already in wires; cell gives energy; energy transferred in components",
  ["The electrons are already in the wires; the cell supplies energy that pushes them round, and the energy is transferred in the lamp", "the cell gives energy to the charges, which are already in the metal"],
  ["The cell is full of spare electrons", "The cell supplies protons"], min_points=2)

Q("w12b_earthing_sphere", 4, "12d", "A negatively charged metal sphere is connected to earth by a wire. Explain what flows in the wire and in which direction, and the direction of the conventional current.",
  [P("electrons flow from the sphere to earth", ["electrons flow from the sphere to earth", "electrons flow to earth", "electrons move to the earth", "electrons go to earth", "electrons flow into the earth", "extra electrons go to earth"]),
   P("until the sphere is uncharged (neutral)", ["uncharged", "neutral", "no charge"]),
   P("conventional current is from earth to the sphere (opposite to electron flow)", ["earth to the sphere", "opposite", "from earth to", "into the sphere", "the opposite way"])],
  "Excess electrons flow from the sphere through the wire to earth until the sphere is neutral. Conventional current is in the opposite direction, from earth to the sphere.",
  ["The sphere has extra electrons. Where do they go?", "When does the flow stop?", "Conventional current is opposite to electron flow."],
  "electrons sphere → earth; conventional current earth → sphere",
  ["Electrons flow from the sphere to earth until it is neutral, so conventional current is from earth to the sphere", "the extra electrons go to earth; conventional current flows the opposite way"],
  ["Protons flow from earth to the sphere", "Nothing flows"], min_points=2,
  pitfalls=[PF(["protons flow", "positive charges flow from earth"], "Only ELECTRONS move; conventional current is just the opposite DIRECTION.")])

Q("w12b_thick_cable_cooker", 4, "12j", "An electric cooker draws a large current, so it is connected with a much thicker cable than a lamp. Explain why.",
  [P("a thicker cable has a larger cross-sectional area, so lower resistance", ["larger cross-sectional area", "lower resistance", "less resistance", "larger area"]),
   P("so less energy is wasted as heat in the cable with the large current", ["less heat", "does not overheat", "less heating", "not get too hot", "less energy wasted", "does not get hot"])],
  "A thicker cable has a larger cross-sectional area and so a lower resistance. With the large current a cooker draws, a low resistance means less energy is converted to heat in the cable, so it does not overheat.",
  ["How does thickness affect resistance?", "What happens in a thin cable carrying a large current?", "Explain."],
  "thick → low R → less heating with large current",
  ["A thicker cable has a lower resistance, so it does not overheat with the large current", "the larger area gives less resistance and less heat in the cable"],
  ["Thick cables look better", "Thick cables carry more voltage"], min_points=2)

Q("w12b_same_charge_more_time", 4, "12e", "Cell P drives 0.2 A for 50 s; cell Q drives 0.5 A for 20 s. Compare the charge that each moves round its circuit, showing your reasoning.",
  [P("use Q = I t for each", ["q = i t", "q = it", "current × time", "charge = current × time"]),
   P("P: 0.2 × 50 = 10 C and Q: 0.5 × 20 = 10 C", ["10 c", "10 coulombs"]),
   P("the charges are equal", ["equal", "the same", "same charge"])],
  "Using Q = I t: cell P moves 0.2 × 50 = 10 C and cell Q moves 0.5 × 20 = 10 C. The two charges are equal, even though the currents differ.",
  ["Which equation do you need?", "Work out each charge.", "Compare."],
  "Q = It: both 10 C, equal",
  ["Q = It gives 10 C for both, so the charges are the same", "P moves 0.2 × 50 = 10 C and Q moves 0.5 × 20 = 10 C, equal"],
  ["Q moves more charge because its current is bigger", "P moves more because it runs longer"], min_points=2)

Q("w12b_reduce_heater_r", 4, "12j", "An engineer wants a heating wire of the same metal with a smaller resistance. Suggest two changes to the wire and explain each.",
  [P("make it shorter: resistance is proportional to length", ["shorter", "reduce the length", "less length"]),
   P("make it thicker: larger cross-sectional area gives smaller resistance", ["thicker", "larger cross-sectional area", "increase the area", "larger area", "wider"])],
  "Make the wire shorter, because resistance is proportional to length. Make it thicker, because a larger cross-sectional area gives a smaller resistance (R is inversely proportional to area).",
  ["How does length affect R?", "How does thickness affect R?", "Suggest both."],
  "shorter; thicker",
  ["Make it shorter because R is proportional to length, and thicker because a larger area reduces R", "use a shorter and thicker wire"],
  ["Make it longer and thinner", "Paint it black"], min_points=2,
  pitfalls=[PF(["longer and thinner", "make it longer", "make it thinner"], "LONGER or THINNER wire INCREASES resistance.")])

Q("w12b_two_meters_mixed", 4, "12g", "A student accidentally connects the voltmeter in series and the ammeter in parallel across a lamp. Explain what happens.",
  [P("the voltmeter in series has a very high resistance, so almost no current flows", ["almost no current", "very little current", "high resistance", "no current flows"]),
   P("so the lamp does not light", ["does not light", "lamp is off", "no light", "lamp will not light", "lamp stays off"]),
   P("the ammeter shows (nearly) zero / the readings are wrong", ["reads zero", "zero", "wrong readings", "no reading", "ammeter reads nothing"])],
  "The voltmeter's very high resistance in series means almost no current flows round the circuit, so the lamp does not light and the ammeter reads (nearly) zero. The readings are useless; the meters must be swapped.",
  ["What is the resistance of a voltmeter?", "What happens to the current when it is in series?", "What do the lamp and ammeter show?"],
  "voltmeter in series → almost no current → lamp off, ammeter ≈ 0",
  ["The voltmeter has a very high resistance, so almost no current flows; the lamp does not light and the ammeter reads zero", "almost no current flows, so the lamp stays off"],
  ["The lamp becomes brighter", "Everything works normally"], min_points=2)

# ---------------------------------------------------------------- L5
Q("w12b_battery_stores_charge", 5, "12f", "A student says: 'A battery goes flat because it runs out of charge.' Evaluate this statement.",
  [P("wrong: the charges (electrons) are not used up; they flow round the circuit", ["wrong", "not used up", "charge is not used up", "flow round", "charges are not used"]),
   P("the battery supplies energy to the charges", ["supplies energy", "gives energy", "energy to the charges", "chemical energy", "gives to the charges"]),
   P("it goes flat when its (chemical) energy store is used up", ["energy is used up", "runs out of energy", "chemical energy runs out", "energy store", "out of energy", "energy that runs out", "runs out of chemical energy"])],
  "The statement is wrong. The charges are not used up: the same electrons flow round and round the circuit. The battery supplies energy to the charges from its chemical energy store, and it goes flat when that energy is used up.",
  ["Is charge used up in a circuit?", "What does the battery give the charges?", "What actually runs out?"],
  "wrong; charge not used up; chemical energy runs out",
  ["Wrong: charge is not used up; the battery runs out of chemical energy, which it gives to the charges", "it is the energy, not the charge, that runs out, because the charges flow round the circuit"],
  ["Correct, batteries are full of electrons", "Correct, charge is used up in the lamp"], min_points=2)

Q("w12b_current_neg_to_pos", 5, "12d", "A student writes: 'Current flows from the negative terminal to the positive terminal, so circuit diagrams draw it the wrong way.' Evaluate this.",
  [P("electrons do flow from negative to positive", ["electrons flow from negative to positive", "electron flow is negative to positive", "electrons move from negative", "electrons do flow"]),
   P("but by convention current is shown from positive to negative (conventional current, chosen before electrons were known)", ["conventional current", "convention", "positive to negative", "before electrons were discovered", "agreed"]),
   P("so diagrams are not wrong: they show conventional current, opposite to electron flow", ["not wrong", "opposite", "both are correct", "just a convention"])],
  "The student is partly right: electrons do flow from the negative terminal to the positive terminal. But circuit diagrams show conventional current, which by convention (chosen before electrons were discovered) flows from positive to negative. The diagrams are not wrong; conventional current is simply opposite in direction to electron flow.",
  ["Which way do electrons flow?", "What is conventional current?", "Is the diagram wrong?"],
  "electrons − → +; diagrams show conventional current + → −; not wrong",
  ["Electrons flow from negative to positive, but diagrams show conventional current from positive to negative, so they are not wrong", "it is just a convention: conventional current is opposite to electron flow"],
  ["Correct, all textbooks are wrong", "Current flows both ways"], min_points=2)

Q("w12b_more_volts_more_current", 5, "12i", "A student claims: 'A 3 V battery always gives twice the current of a 1.5 V battery.' Evaluate this claim.",
  [P("only true for the same resistance (I = V / R)", ["same resistance", "i = v / r", "depends on the resistance", "v / r", "if the resistance is the same"]),
   P("a different (larger) resistance in the 3 V circuit could give the same or less current", ["larger resistance", "different resistance", "less current", "same current", "smaller current"]),
   P("volts measure energy per coulomb, not current", ["energy per coulomb", "energy per unit charge", "not current", "work done per"])],
  "The claim is only true if both batteries drive current through the same resistance, since I = V / R. If the 3 V circuit has a larger resistance, the current could be the same or even smaller. The volt measures energy per coulomb, not current.",
  ["Write I in terms of V and R.", "What if the resistances differ?", "What does a volt measure?"],
  "only if R same (I = V/R); different R changes it",
  ["Only true if the resistance is the same, because I = V / R; a larger resistance could give less current", "it depends on the resistance of each circuit, and a larger resistance gives a smaller current"],
  ["Correct, always", "Wrong, the 1.5 V battery gives more current"], min_points=2)

Q("w12b_insulators_no_charge", 5, "12c", "A student says: 'Insulators do not conduct because they contain no charged particles.' Evaluate this.",
  [P("wrong: insulators contain charged particles (electrons and protons)", ["wrong", "contain electrons", "have electrons", "contain charged particles", "electrons and protons", "have charged particles"]),
   P("but their electrons are held tightly, so there are no free electrons to move", ["held tightly", "no free electrons", "cannot move", "not free", "bound", "none are free"]),
   P("insulators can still become charged by rubbing", ["become charged", "charged by rubbing", "rubbing", "static"])],
  "The statement is wrong. Insulators contain charged particles, electrons and protons, like all matter. They do not conduct because their electrons are held tightly in the atoms, so there are no free electrons to move. Indeed, insulators can be charged by rubbing, which shows they contain charges.",
  ["Are insulators made of atoms?", "Why can't their electrons carry a current?", "What evidence shows insulators contain charges?"],
  "wrong; have electrons but held tightly (no free electrons); can be charged by rubbing",
  ["Wrong: insulators contain electrons, but they are held tightly so there are no free electrons to move", "they have charged particles but none are free to move; they can still be charged by rubbing"],
  ["Correct, insulators have no electrons", "Correct, plastic is made of nothing"], min_points=2)

Q("w12b_design_thickness", 5, "12j", "Design an experiment to show how the resistance of a wire depends on its cross-sectional area.",
  [P("use wires of the same material and same length but different diameters (cross-sectional areas)", ["same material", "same length", "different diameters", "different thickness", "different cross-sectional area"]),
   P("measure V and I for each with a voltmeter and ammeter and calculate R = V / I", ["r = v / i", "v / i", "voltmeter", "ammeter", "measure v and i"]),
   P("measure the diameter with a micrometer, work out the area, and plot R against 1/area (straight line through origin)", ["micrometer", "1 / a", "1/area", "plot r against", "straight line", "graph"])],
  "Use several wires of the same material and the same length but different diameters. Measure each diameter with a micrometer screw gauge and work out the cross-sectional area. For each wire, measure the p.d. and current with a voltmeter and ammeter and calculate R = V / I, keeping the current small so the wire does not heat up. Plot R against 1/area: a straight line through the origin shows R is inversely proportional to area.",
  ["What must be kept the same?", "How do you measure R?", "How do you show the relationship?"],
  "same material and length; R = V/I; micrometer; plot R vs 1/A",
  ["Use wires of the same material and length but different thickness, measure V and I to get R = V / I, and plot R against 1/area", "measure the diameter with a micrometer and find R for each wire with an ammeter and voltmeter"],
  ["Use wires of different lengths", "Weigh each wire"], min_points=2)

Q("w12b_rubbing_creates_charge", 5, "12a", "A student says: 'Rubbing a balloon on hair creates negative charge.' Evaluate this.",
  [P("wrong: charge is not created, only transferred", ["not created", "transferred", "wrong", "only moved", "conserved"]),
   P("electrons move from the hair to the balloon", ["electrons move from the hair", "electrons from the hair", "balloon gains electrons", "hair loses electrons", "electrons are transferred"]),
   P("so the hair becomes equally positive", ["hair becomes positive", "hair is positive", "equal positive", "equally positive", "hair positive"])],
  "The statement is wrong. Charge is not created; it is transferred. Rubbing moves electrons from the hair to the balloon, so the balloon becomes negative and the hair becomes equally positively charged.",
  ["Is charge created or moved?", "Which particles move, and which way?", "What happens to the hair?"],
  "wrong; electrons transferred hair → balloon; hair positive",
  ["Wrong: no charge is created; electrons are transferred from the hair to the balloon, leaving the hair positive", "charge is only moved: the balloon gains electrons and the hair becomes positive"],
  ["Correct, rubbing makes electrons", "Correct, friction creates charge"], min_points=2,
  pitfalls=[CREATES_CHARGE])

Q("w12b_heating_data", 5, "12i", "A student finds V ÷ I for a long thin wire increases as she takes readings at larger and larger currents. Evaluate a possible reason and suggest an improvement.",
  [P("the wire heats up at larger currents", ["heats up", "gets hot", "temperature rises", "warms up", "heating"]),
   P("a hotter metal wire has a larger resistance", ["higher resistance", "larger resistance", "resistance increases", "more resistance", "raises the resistance"]),
   P("improvement: keep the current small / switch off between readings so the temperature stays constant", ["small current", "switch off between", "constant temperature", "let it cool", "keep the current low", "between readings", "keep the current small"])],
  "A likely reason is that the wire heats up at larger currents, and a hotter metal has a larger resistance, so V ÷ I rises. To improve, keep the currents small and switch off between readings so that the wire stays at a constant temperature.",
  ["What happens to a wire carrying a large current?", "How does temperature affect a metal's resistance?", "How can you keep the temperature constant?"],
  "wire heats → R rises; use small current, switch off between readings",
  ["The wire heats up so its resistance increases; keep the current small and switch off between readings", "heating raises the resistance, so let it cool between readings to keep the temperature constant"],
  ["The ammeter is broken", "The wire gets longer as current increases"], min_points=2)

Q("w12b_ammeter_parallel_claim", 5, "12c", "A student says: 'An ammeter should be connected in parallel with the lamp because it measures the current through the lamp.' Evaluate this.",
  [P("wrong: an ammeter must be in series", ["wrong", "in series", "must be in series", "goes in series"]),
   P("so that the current through the lamp also passes through the ammeter", ["same current", "current passes through", "all the current", "goes through the ammeter", "flows through it"]),
   P("in parallel its very low resistance would take most of the current (short circuit), giving a wrong reading and possible damage", ["low resistance", "short circuit", "short-circuit", "most of the current", "damage", "wrong reading"])],
  "The statement is wrong. An ammeter must be in series so that the current through the lamp also passes through the ammeter. In parallel, its very low resistance would take almost all the current and short-circuit the lamp, giving a wrong reading and possibly damaging the meter.",
  ["How must an ammeter be connected?", "Why does that measure the lamp's current?", "What would happen in parallel?"],
  "wrong; series so same current; parallel → short circuit",
  ["Wrong: it must be in series so the same current flows through it; in parallel its low resistance would short-circuit the lamp", "an ammeter goes in series; in parallel it would take most of the current"],
  ["Correct, ammeters go in parallel", "Either way works"], min_points=2)

Q("w12b_one_amp_electrons", 5, "12e", "A student says: 'A current of 1 A means one electron passes each second.' Evaluate this, given that one electron carries a charge of 1.6 × 10^-19 C.",
  [P("wrong: 1 A means 1 coulomb per second", ["wrong", "1 coulomb per second", "1 c per second", "one coulomb per second", "1 c each second"]),
   P("1 C is the charge of a huge number of electrons: 1 ÷ 1.6 × 10^-19 ≈ 6.25 × 10^18", ["6.25 × 10", "6.3 × 10", "6.25 x 10", "huge number", "very large number"]),
   P("so about 6 × 10^18 electrons pass each second", ["electrons pass each second", "electrons per second", "per second"])],
  "The statement is wrong. 1 A means 1 coulomb of charge passes each second. Since each electron carries only 1.6 × 10⁻¹⁹ C, 1 C is the charge of 1 ÷ 1.6 × 10⁻¹⁹ ≈ 6.25 × 10¹⁸ electrons, so about 6 × 10¹⁸ electrons pass each second.",
  ["What does 1 A mean in coulombs?", "How many electrons make 1 C?", "Evaluate."],
  "wrong; 1 C/s ≈ 6.25 × 10¹⁸ electrons per second",
  ["Wrong: 1 A is 1 C per second, which is about 6.25 × 10^18 electrons per second", "1 A means one coulomb per second, a huge number of electrons"],
  ["Correct, one electron per second", "1 A means one proton per second"], min_points=2)

Q("w12b_thick_more_metal_claim", 5, "12j", "A student says: 'A thicker wire has more resistance, because it contains more metal for the electrons to bump into.' Evaluate this.",
  [P("wrong: a thicker wire has less resistance", ["wrong", "less resistance", "lower resistance", "smaller resistance"]),
   P("its larger cross-sectional area gives more paths: more free electrons can flow side by side", ["larger cross-sectional area", "more paths", "side by side", "more free electrons", "larger area", "more room"]),
   P("resistance is inversely proportional to area, so doubling the area halves R", ["inversely proportional", "halves", "doubling the area halves"])],
  "The statement is wrong. A thicker wire has a larger cross-sectional area, so more free electrons can flow side by side through it at the same time; the wire has less resistance. Resistance is inversely proportional to cross-sectional area, so doubling the area halves the resistance.",
  ["Does a thicker wire let more or less current through for the same p.d.?", "Think of more lanes on a road.", "How does R depend on area?"],
  "wrong; larger area → more paths → less R (R ∝ 1/A)",
  ["Wrong: a thicker wire has a larger area so more electrons can flow side by side, giving less resistance", "it has a lower resistance, because resistance is inversely proportional to the cross-sectional area"],
  ["Correct, more metal means more resistance", "Correct, thick wires block electrons"], min_points=2,
  pitfalls=[PF(["thicker wire has more resistance", "more metal means more resistance", "thick wires block"], "A THICKER wire has LESS resistance.")])
