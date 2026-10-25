"""Chapter 13 D.C. Circuits: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import sketches2 as sk
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 13


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


CURRENT_USED_UP = PF(["current is used up", "current gets used up", "uses up the current", "current is lost"],
                     "Current is NOT used up: the same current flows all the way round a series loop.")
PARALLEL_ADDS = PF(["resistances add in parallel", "add the resistances in parallel", "parallel resistance is the sum"],
                   "In PARALLEL, 1/R = 1/R₁ + 1/R₂: the effective resistance is LESS than the smallest resistor.")

# ---------------------------------------------------------------- L1
Q("w13b_parallel_formula", 1, "13f", "State the formula for the effective resistance R of two resistors R₁ and R₂ connected in parallel.",
  [P("1/R = 1/R₁ + 1/R₂", ["1/r = 1/r1 + 1/r2", "1 / r = 1 / r1 + 1 / r2", "1/r1 + 1/r2", "1 / r1 + 1 / r2", "product over sum", "r1r2 / r1 + r2", "reciprocal"])],
  "1/R = 1/R₁ + 1/R₂ (equivalently, R = R₁R₂ ÷ (R₁ + R₂)).",
  ["It uses reciprocals.", "1 over R equals ...", "Write it."],
  "1/R = 1/R₁ + 1/R₂",
  ["1/R = 1/R1 + 1/R2", "one over R equals the sum of the reciprocals, 1/R1 + 1/R2"],
  ["R = R1 + R2", "R = R1 × R2"],
  pitfalls=[PF(["r = r1 + r2"], "R = R₁ + R₂ is for SERIES. In parallel, 1/R = 1/R₁ + 1/R₂.")])

Q("w13b_variable_resistor_use", 1, "13a", "State what a variable resistor is used for in a circuit.",
  [P("to change (vary) the resistance, and so control the current", ["change the resistance", "vary the resistance", "control the current", "change the current", "adjust the current", "vary the current"])],
  "A variable resistor is used to change the resistance in a circuit and so control the current, for example to dim a lamp.",
  ["What can you change on a variable resistor?", "What does that do to the current?", "State it."],
  "varies R to control current",
  ["To change the resistance and so control the current", "it lets you vary the current, e.g. to dim a lamp"],
  ["To store charge", "To measure the voltage"])

Q("w13b_series_meaning", 1, "13b", "State what is meant by components connected in series.",
  [P("connected one after another in a single loop (one path for the current)", ["one after another", "single loop", "one path", "single path", "one loop", "end to end"])],
  "Components in series are connected one after another in a single loop, so there is only one path for the current.",
  ["How many paths does the current have?", "How are the components arranged?", "State it."],
  "one after another, single path",
  ["Connected one after another so there is only one path for the current", "in a single loop, end to end"],
  ["Connected side by side across the same two points", "Connected in separate branches"])

Q("w13b_parallel_meaning", 1, "13d", "State what is meant by components connected in parallel.",
  [P("connected in separate branches across the same two points (more than one path for the current)", ["separate branches", "same two points", "more than one path", "side by side", "different branches", "branches"])],
  "Components in parallel are connected in separate branches between the same two points, so the current has more than one path.",
  ["How many paths does the current have?", "Where is each component connected?", "State it."],
  "separate branches across the same two points",
  ["Connected in separate branches between the same two points", "side by side, so the current has more than one path"],
  ["One after another in a single loop", "All in one line"])

Q("w13b_two_identical_parallel", 1, "13f", "State the effective resistance of two identical 10 Ω resistors connected in parallel.",
  [P("5 Ω (half of one resistor)", ["5 ω", "5 ohm", "5 ohms", "half", "5.0 ω"])],
  "The effective resistance is 5 Ω: two identical resistors in parallel give half the resistance of one.",
  ["Use 1/R = 1/10 + 1/10.", "Two identical resistors in parallel give half.", "State it."],
  "5 Ω",
  ["5 Ω", "half of 10, so 5 ohms"],
  ["20 Ω", "10 Ω"],
  pitfalls=[PF(["20 ω", "20 ohms", "20 ohm"], "20 Ω is the SERIES value. In parallel, two 10 Ω give 5 Ω.")])

Q("w13b_series_battery_pd", 1, "13c", "Fig. 1 shows two lamps in series. The p.d.s across them are 2 V and 4 V. State the p.d. across the battery.",
  [P("6 V (the p.d.s add up)", ["6 v", "6 volts", "6.0 v"])],
  "The battery p.d. is 6 V, because in series the p.d.s across the components add up to the p.d. across the whole circuit.",
  ["What is the rule for p.d.s in series?", "Add them.", "State it."],
  "2 + 4 = 6 V",
  ["6 V", "2 V + 4 V = 6 V"],
  ["4 V", "2 V"],
  figure=lambda: sk.circuit(series=[("lamp", "2 V"), ("lamp", "4 V")], emf=""))

Q("w13b_parallel_each_pd", 1, "13e", "Fig. 1 shows two lamps in parallel connected to a 6 V battery. State the p.d. across each lamp.",
  [P("6 V each (same p.d. across parallel branches)", ["6 v", "6 volts", "6.0 v"])],
  "Each lamp has a p.d. of 6 V across it, because the p.d. across each branch of a parallel circuit is the same as the supply.",
  ["What is the rule for p.d. in parallel?", "Each branch is connected directly across the battery.", "State it."],
  "6 V each",
  ["6 V across each lamp", "each lamp gets the full 6 volts"],
  ["3 V each", "12 V"],
  pitfalls=[PF(["3 v each", "3 volts each", "shared equally"], "In PARALLEL each branch gets the FULL supply p.d.")],
  figure=lambda: sk.circuit(parallel=[[("lamp", "L1")], [("lamp", "L2")]], emf="6 V"))

Q("w13b_junction_missing", 1, "13d", "A main current of 3.0 A splits into two parallel branches. One branch carries 1.0 A. State the current in the other branch.",
  [P("2.0 A (branch currents add up to the main current)", ["2.0 a", "2 a", "2 amps", "2.0 amps", "2 amperes"])],
  "The other branch carries 3.0 − 1.0 = 2.0 A, because the branch currents add up to the main current.",
  ["What do the branch currents add up to?", "Subtract.", "State it."],
  "3.0 − 1.0 = 2.0 A",
  ["2.0 A", "3 − 1 = 2 A"],
  ["3.0 A", "1.0 A"])

Q("w13b_series_switch_open", 1, "13b", "State what happens to all the lamps in a series circuit when the switch is opened.",
  [P("they all go out", ["all go out", "all go off", "all switch off", "none light", "all turn off", "all off"]),
   P("because the circuit is broken, so no current flows anywhere", ["circuit is broken", "no current", "broken", "incomplete", "open circuit"])],
  "All the lamps go out, because opening the switch breaks the single loop, so no current flows anywhere in the circuit.",
  ["How many paths are there in series?", "What happens if that path is broken?", "State it."],
  "all go out; no current",
  ["They all go out because the circuit is broken and no current flows", "all the lamps turn off since there is no complete path"],
  ["Only the lamp next to the switch goes out", "They get brighter"], min_points=1,
  pitfalls=[PF(["only the lamp next to", "only one lamp goes out"], "In SERIES there is one path, so ALL the lamps go out.")])

Q("w13b_switch_purpose", 1, "13a", "State what a switch does in a circuit.",
  [P("it opens (breaks) or closes (completes) the circuit, turning the current off or on", ["opens", "closes", "breaks the circuit", "completes the circuit", "turns the current on and off", "on and off", "off and on"])],
  "A switch opens or closes the circuit: when open it breaks the circuit so no current flows, and when closed it completes the circuit so current can flow.",
  ["What does an open switch do to the path?", "And a closed switch?", "State it."],
  "opens/closes circuit → current off/on",
  ["It opens or closes the circuit to turn the current off or on", "it breaks the circuit when open and completes it when closed"],
  ["It measures the current", "It stores charge"])

# ---------------------------------------------------------------- L2
Q("w13b_series_4_6", 2, "13f", "A 4 Ω resistor and a 6 Ω resistor are connected in series. State their effective resistance and explain how you got it.",
  [P("10 Ω", ["10 ω", "10 ohms", "10 ohm"]),
   P("in series the resistances add (R = R₁ + R₂)", ["add", "r = r1 + r2", "sum", "4 + 6", "added together"])],
  "The effective resistance is 10 Ω, because resistances in series add: R = 4 + 6 = 10 Ω.",
  ["What is the rule for resistors in series?", "Add them.", "State it with the reason."],
  "R = 4 + 6 = 10 Ω",
  ["10 Ω, because in series the resistances add", "R = R1 + R2 = 4 + 6 = 10 ohms"],
  ["2.4 Ω", "24 Ω"], min_points=2)

Q("w13b_add_series_less_current", 2, "13f", "A second resistor is added in series with a resistor connected to a battery. Explain what happens to the current.",
  [P("the total (effective) resistance increases", ["resistance increases", "total resistance increases", "more resistance", "higher resistance", "greater resistance", "resistances add"]),
   P("so the current decreases (I = V / R with the same battery)", ["current decreases", "current falls", "less current", "smaller current", "current goes down", "decreases"])],
  "Resistances in series add, so the total resistance increases. With the same battery p.d., I = V / R, so the current decreases.",
  ["What happens to the total resistance in series?", "Use I = V / R.", "Explain."],
  "R total up → I down",
  ["The total resistance increases, so the current decreases", "adding resistance in series means less current flows from the same battery"],
  ["The current increases", "The current stays the same"], min_points=2,
  pitfalls=[PF(["current increases", "current stays the same"], "More resistance in series means LESS current.")])

Q("w13b_parallel_full_pd", 2, "13e", "Explain why each branch of a parallel circuit has the same p.d. as the battery.",
  [P("each branch is connected directly across the battery terminals (between the same two points)", ["connected directly across", "across the battery", "same two points", "connected to both terminals", "directly to the battery"]),
   P("so each charge passing through any branch has the same energy transferred per coulomb", ["same energy", "energy per coulomb", "same p.d.", "same voltage"])],
  "Each branch is connected directly between the same two points, the battery terminals. So each coulomb passing through any branch has the same energy transferred, and every branch has the same p.d. as the battery.",
  ["What are the ends of each branch connected to?", "What does p.d. measure?", "Explain."],
  "each branch across the same two points (battery terminals)",
  ["Each branch is connected directly across the battery terminals, so each has the same p.d.", "all the branches are between the same two points, so they get the same voltage"],
  ["Because the current is the same in each branch", "Because the p.d. is shared out"], min_points=1,
  pitfalls=[PF(["current is the same in each branch", "p.d. is shared"], "In parallel the p.d. is the SAME because each branch is across the same two points; the currents can differ.")])

Q("w13b_voltmeter_parallel_reading", 2, "13e", "Fig. 1 shows two resistors in parallel. A voltmeter across R₁ reads 4.5 V. State the p.d. across R₂ and explain.",
  [P("4.5 V", ["4.5 v", "4.5 volts"]),
   P("the p.d. across parallel branches is the same", ["same", "equal", "parallel branches", "same p.d."])],
  "The p.d. across R₂ is also 4.5 V, because the p.d. across each branch of a parallel circuit is the same.",
  ["What is the rule for p.d. in parallel?", "R₁ and R₂ are across the same two points.", "State it."],
  "4.5 V (same p.d.)",
  ["4.5 V, because the p.d. across parallel branches is the same", "the same 4.5 volts, since they are in parallel"],
  ["9 V", "2.25 V"], min_points=2,
  figure=lambda: sk.circuit(parallel=[[("R", "R₁")], [("R", "R₂")]], emf="", voltmeter=("parallel", 0)))

Q("w13b_ammeter_anywhere_series", 2, "13b", "Explain why it does not matter where an ammeter is placed in a series circuit.",
  [P("the current is the same at every point in a series circuit", ["same at every point", "current is the same", "same current everywhere", "same everywhere", "same at all points"]),
   P("because there is only one path, and charge is not used up", ["one path", "only one path", "not used up", "single loop", "charge is not lost"])],
  "The current is the same at every point in a series circuit, because there is only one path and charge is not used up, so the ammeter gives the same reading wherever it is placed.",
  ["What is the rule for current in series?", "Why is it true?", "Explain."],
  "same current everywhere (one path, charge not used up)",
  ["The current is the same at every point because there is only one path", "charge is not used up, so the same current flows everywhere in the loop"],
  ["Because ammeters measure voltage", "Because the current is largest near the battery"], min_points=1,
  pitfalls=[CURRENT_USED_UP, PF(["largest near the battery", "current is bigger near"], "In series the current is the SAME everywhere.")])

Q("w13b_fairy_lights", 2, "13b", "In an old set of fairy lights, all the bulbs went out when one bulb failed. State how the bulbs were connected and explain.",
  [P("in series", ["series"]),
   P("a broken bulb breaks the single path, so no current flows through any of them", ["breaks the circuit", "single path", "one path", "no current", "circuit is broken", "breaks the path", "circuit incomplete", "incomplete"])],
  "The bulbs were connected in series. There is only one path for the current, so when one bulb failed it broke the circuit and no current could flow through any of the bulbs.",
  ["Which connection has only one path?", "What happens when that path is broken?", "Explain."],
  "series; one path broken → no current",
  ["In series, because one broken bulb breaks the only path so no current flows", "series: the failed bulb makes the circuit incomplete"],
  ["In parallel", "The bulbs were all broken"], min_points=2,
  pitfalls=[PF(["in parallel", "parallel"], "In PARALLEL the other bulbs would stay lit; these were in SERIES.")])

Q("w13b_own_switch", 2, "13e", "Explain why lamps connected in parallel can each be switched on and off independently.",
  [P("each lamp is in its own branch with its own switch", ["own branch", "separate branch", "own switch", "its own path", "each branch"]),
   P("opening one branch does not break the path through the other branches", ["other branches", "still complete", "others stay on", "not affect the others", "does not break"])],
  "Each lamp is in its own branch, so a switch in that branch controls only that lamp. Opening it breaks only that branch; the paths through the other branches are still complete, so the other lamps stay on.",
  ["Where does each lamp sit in a parallel circuit?", "What happens to the other branches when one switch opens?", "Explain."],
  "own branch; other branches still complete",
  ["Each lamp has its own branch and switch, so opening one does not break the path through the others", "the other branches are still complete, so the others stay on"],
  ["Because the current is shared equally", "Because they are in series"], min_points=1)

Q("w13b_identical_parallel_split", 2, "13d", "Two identical lamps are connected in parallel. The main current is 0.80 A. State the current in each lamp and explain.",
  [P("0.40 A each", ["0.40 a", "0.4 a", "0.4 amps", "0.40 amps"]),
   P("identical lamps take equal currents, which add to the main current", ["identical", "equal", "add up", "split equally", "shared equally", "same resistance"])],
  "Each lamp carries 0.40 A. The lamps are identical with the same p.d., so they take equal currents, and the two branch currents add up to the main current of 0.80 A.",
  ["Do identical lamps in parallel take equal currents?", "What do the branch currents add up to?", "Calculate."],
  "0.40 A each (equal, add to 0.80 A)",
  ["0.40 A each, because identical lamps share the current equally", "0.4 A each since they are identical and the branch currents add to 0.8 A"],
  ["0.80 A each", "1.6 A each"], min_points=2)

Q("w13b_cells_in_series", 2, "13c", "Two 1.5 V cells are connected in series, positive to negative. State the total p.d. supplied and explain.",
  [P("3.0 V", ["3.0 v", "3 v", "3 volts"]),
   P("the e.m.f.s (p.d.s) of cells in series add up", ["add", "add up", "1.5 + 1.5", "sum", "combine"])],
  "The total p.d. is 3.0 V, because the e.m.f.s of cells connected in series (positive to negative) add up: 1.5 + 1.5 = 3.0 V.",
  ["What happens to the voltages of cells in series?", "Add them.", "State it."],
  "1.5 + 1.5 = 3.0 V",
  ["3.0 V because the cells' voltages add in series", "1.5 + 1.5 = 3 V"],
  ["1.5 V", "0.75 V"], min_points=2)

Q("w13b_draw_voltmeter", 2, "13a", "Describe how a voltmeter is drawn in a circuit diagram to measure the p.d. across a lamp.",
  [P("a circle with the letter V", ["circle with v", "circle with the letter v", "v in a circle", "circle containing v"]),
   P("connected in parallel across (to each side of) the lamp", ["in parallel", "across the lamp", "each side of the lamp", "parallel"])],
  "A voltmeter is drawn as a circle with the letter V inside it, connected in parallel across the lamp, with one lead on each side of the lamp.",
  ["What is the voltmeter symbol?", "How is it connected?", "Describe."],
  "circle with V, in parallel across lamp",
  ["A circle with V inside, connected in parallel across the lamp", "draw V in a circle with wires to each side of the lamp"],
  ["A circle with A in series", "A rectangle in series"], min_points=2,
  pitfalls=[PF(["in series with the lamp", "circle with a"], "A voltmeter (V in a circle) goes in PARALLEL across the lamp.")])

# ---------------------------------------------------------------- L3
Q("w13b_series_current_calc", 3, "13g", "Fig. 1 shows a 2.0 Ω and a 4.0 Ω resistor in series with a 12 V battery. Explain how to find the current, and give its value.",
  [P("total resistance = 2.0 + 4.0 = 6.0 Ω", ["6.0 ω", "6 ω", "6 ohms", "6.0 ohms", "2 + 4"]),
   P("I = V / R = 12 ÷ 6.0", ["i = v / r", "v / r", "12 / 6", "12 ÷ 6"]),
   P("= 2.0 A", ["2.0 a", "2 a", "2 amps"])],
  "The resistors are in series, so the total resistance is 2.0 + 4.0 = 6.0 Ω. Then I = V / R = 12 ÷ 6.0 = 2.0 A.",
  ["Find the total resistance first.", "Then use I = V / R.", "Calculate."],
  "R = 6.0 Ω; I = 12/6 = 2.0 A",
  ["Total resistance is 6 Ω, so I = V / R = 12 ÷ 6 = 2 A", "add to get 6 ohms, then 12 / 6 = 2.0 A"],
  ["I = 12 ÷ 2 = 6 A", "I = 12 ÷ 4 = 3 A"], min_points=2,
  pitfalls=[PF(["= 6 a", "= 3 a"], "Use the TOTAL resistance, 6.0 Ω: I = 12 ÷ 6.0 = 2.0 A.")],
  figure=lambda: sk.circuit(series=[("R", "2.0 Ω"), ("R", "4.0 Ω")], emf="12 V"))

Q("w13b_parallel_6_3", 3, "13f", "Explain how to find the effective resistance of a 6 Ω and a 3 Ω resistor in parallel, and give the value.",
  [P("use 1/R = 1/6 + 1/3", ["1/r = 1/6 + 1/3", "1/6 + 1/3", "1 / 6 + 1 / 3", "product over sum", "18 / 9", "6 × 3"]),
   P("1/R = 1/2, so R = 2 Ω", ["2 ω", "2 ohms", "2.0 ω", "2 ohm"]),
   P("which is less than the smallest resistor", ["less than the smallest", "less than the smaller", "smaller than 3", "less than 3"])],
  "Use 1/R = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2, so R = 2 Ω (or product over sum: 18 ÷ 9 = 2 Ω). This is less than the smaller resistor, as expected for parallel.",
  ["Write the parallel formula.", "Add the fractions.", "Turn 1/R into R."],
  "1/R = 1/6 + 1/3 = 1/2 → R = 2 Ω",
  ["1/R = 1/6 + 1/3 = 1/2, so R = 2 Ω", "product over sum: 18 ÷ 9 = 2 ohms, less than the smallest resistor"],
  ["R = 6 + 3 = 9 Ω", "R = 4.5 Ω"], min_points=2, pitfalls=[PARALLEL_ADDS, PF(["r = 6 + 3", "6 + 3 = 9"], "6 + 3 = 9 Ω is the SERIES value.")])

Q("w13b_remove_parallel_lamp", 3, "13d", "Fig. 1 shows two identical lamps in parallel. Lamp L2 is unscrewed. Explain what happens to the brightness of L1 and to the main current.",
  [P("L1 stays the same brightness", ["same brightness", "stays the same", "no change", "unchanged", "does not change"]),
   P("because it still has the full battery p.d. across it, so its current is unchanged", ["full battery p.d.", "same p.d.", "same voltage", "still has 6", "its current is unchanged", "same current"]),
   P("the main current decreases (halves), because one branch no longer carries current", ["main current decreases", "main current halves", "main current falls", "halves", "less current from the battery"])],
  "L1 stays the same brightness, because it still has the full battery p.d. across it, so its current is unchanged. The main current falls to half, because the L2 branch no longer carries any current.",
  ["Does removing L2 change the p.d. across L1?", "What happens to L1's current?", "What do the branch currents add up to now?"],
  "L1 unchanged (same p.d.); main current halves",
  ["L1 stays the same because it still has the same p.d., but the main current halves", "L1 is unchanged and the battery current decreases because only one branch carries current"],
  ["L1 gets brighter because it gets all the current", "Both lamps go out"], min_points=2,
  pitfalls=[PF(["gets brighter", "gets all the current", "both go out", "both lamps go out"], "In parallel L1 keeps the SAME p.d., so it stays the SAME brightness.")],
  figure=lambda: sk.circuit(series=[("A", "A")], parallel=[[("lamp", "L1")], [("lamp", "L2")]], emf=""))

Q("w13b_series_bigger_r_bigger_pd", 3, "13c", "Two resistors of 10 Ω and 20 Ω are in series. Explain which one has the larger p.d. across it.",
  [P("the 20 Ω resistor", ["20 ω", "20 ohm", "larger resistor", "bigger resistor", "20 ohms"]),
   P("the current is the same through both in series", ["same current", "current is the same"]),
   P("V = I R, so the larger resistance has the larger p.d. (twice as much)", ["v = i r", "v = ir", "twice", "proportional to resistance", "larger resistance"])],
  "The 20 Ω resistor has the larger p.d. In series the same current flows through both, and since V = I R, the resistor with the larger resistance has the larger p.d.: twice as much as the 10 Ω resistor.",
  ["What is the same for both resistors in series?", "Use V = IR.", "Which has the larger p.d.?"],
  "20 Ω: same I, V = IR",
  ["The 20 Ω resistor, because the current is the same and V = IR", "the bigger resistor gets twice the p.d. since the same current flows through both"],
  ["The 10 Ω resistor, because more current goes through it", "They have the same p.d."], min_points=2,
  pitfalls=[PF(["more current goes through", "same p.d."], "In SERIES the current is the same, so the LARGER resistor has the larger p.d.")])

Q("w13b_parallel_smaller_r_more_current", 3, "13d", "A 10 Ω and a 20 Ω resistor are connected in parallel. Explain which one carries the larger current.",
  [P("the 10 Ω resistor", ["10 ω", "10 ohm", "smaller resistor", "10 ohms", "smaller resistance"]),
   P("the p.d. across both is the same in parallel", ["same p.d.", "same voltage", "p.d. is the same", "same pd"]),
   P("I = V / R, so the smaller resistance carries the larger current (twice as much)", ["i = v / r", "v / r", "twice", "inversely proportional", "smaller resistance"])],
  "The 10 Ω resistor carries the larger current. In parallel both resistors have the same p.d., and since I = V / R, the smaller resistance carries the larger current: twice as much as the 20 Ω resistor.",
  ["What is the same for both resistors in parallel?", "Use I = V / R.", "Which has the larger current?"],
  "10 Ω: same V, I = V/R",
  ["The 10 Ω resistor, because the p.d. is the same and I = V / R", "the smaller resistor takes twice the current since both have the same voltage"],
  ["The 20 Ω resistor", "They carry the same current"], min_points=2)

Q("w13b_series_vs_parallel_brightness", 3, "13e", "Two identical lamps are connected to the same battery, first in series and then in parallel. Explain which arrangement makes the lamps brighter.",
  [P("parallel is brighter", ["parallel is brighter", "brighter in parallel", "parallel", "in parallel"]),
   P("in parallel each lamp gets the full battery p.d.", ["full battery p.d.", "full p.d.", "full voltage", "whole p.d.", "same p.d. as the battery"]),
   P("in series the p.d. is shared, so each gets only half", ["shared", "half", "split", "each gets half"])],
  "The lamps are brighter in parallel. In parallel each lamp has the full battery p.d. across it, so more current flows through each. In series the battery p.d. is shared, so each lamp gets only half of it and less current.",
  ["What p.d. does each lamp get in series?", "And in parallel?", "Which gives more current per lamp?"],
  "parallel: full p.d. each; series: half each",
  ["Parallel, because each lamp gets the full battery p.d. while in series they share it", "in parallel each lamp has the whole voltage, but in series each has only half"],
  ["Series, because the current is the same", "They are equally bright"], min_points=2)

Q("w13b_three_parallel_lamps", 3, "13d", "Three identical lamps are in parallel and the main current is 0.90 A. One lamp is removed. Explain the new main current.",
  [P("each lamp originally carried 0.30 A", ["0.30 a", "0.3 a", "0.3 amps"]),
   P("the remaining lamps still carry 0.30 A each (same p.d.)", ["same p.d.", "still 0.3", "unchanged", "same current", "still carry"]),
   P("so the main current is 0.60 A", ["0.60 a", "0.6 a", "0.6 amps"])],
  "Each identical lamp carried 0.90 ÷ 3 = 0.30 A. Removing one does not change the p.d. across the others, so each still carries 0.30 A. The new main current is 2 × 0.30 = 0.60 A.",
  ["What did each lamp carry?", "Does removing one change the others?", "Add the remaining branch currents."],
  "0.30 A each; new main current 0.60 A",
  ["Each lamp took 0.3 A, the other two are unchanged, so the main current is 0.6 A", "0.30 A each; with one removed the main current is 0.60 A"],
  ["0.90 A, it stays the same", "0.45 A each, so 0.90 A"], min_points=2)

Q("w13b_led_resistor", 3, "13g", "An LED is always connected in series with a resistor. Explain why.",
  [P("the resistor limits (reduces) the current", ["limits the current", "reduces the current", "limit the current", "less current", "controls the current"]),
   P("so that the LED is not damaged by too large a current", ["damaged", "burn out", "protect", "too large a current", "too much current"]),
   P("the resistor takes part of the supply p.d. (series p.d.s add)", ["share", "part of the p.d.", "p.d. across the resistor", "takes some of the voltage"])],
  "The resistor limits the current in the circuit. Without it, too large a current would flow and damage the LED. In series, the resistor takes part of the supply p.d., leaving only a small p.d. across the LED.",
  ["What would happen to an LED with too much current?", "What does a series resistor do to the current?", "Explain."],
  "resistor limits current → protects LED",
  ["The resistor limits the current so the LED is not damaged", "it reduces the current to protect the LED from burning out"],
  ["To make the LED brighter", "To store energy"], min_points=1)

Q("w13b_series_pd_missing", 3, "13c", "A 9.0 V battery is connected to a lamp and a resistor in series. The p.d. across the lamp is 3.5 V. Explain how to find the p.d. across the resistor, and give the value.",
  [P("the p.d.s across series components add up to the battery p.d.", ["add up", "sum", "add to", "total p.d.", "adds up"]),
   P("9.0 − 3.5 = 5.5 V", ["5.5 v", "5.5 volts", "9.0 − 3.5", "9 - 3.5"])],
  "In series, the p.d.s across the components add up to the battery p.d. So the p.d. across the resistor is 9.0 − 3.5 = 5.5 V.",
  ["What is the rule for p.d.s in series?", "Subtract the lamp's p.d.", "Calculate."],
  "9.0 − 3.5 = 5.5 V",
  ["The p.d.s add up to 9 V, so the resistor has 9.0 − 3.5 = 5.5 V", "5.5 V, because the series p.d.s sum to the battery voltage"],
  ["3.5 V", "12.5 V"], min_points=2)

Q("w13b_new_branch_no_change", 3, "13e", "Fig. 1 shows a lamp L1 connected to a battery. A second lamp L2 is connected in parallel with it. Explain what happens to the current through L1.",
  [P("the current through L1 stays the same", ["stays the same", "unchanged", "no change", "does not change", "same current"]),
   P("because the p.d. across L1 is still the battery p.d. and its resistance is unchanged", ["same p.d.", "still the battery p.d.", "full battery p.d.", "same voltage", "resistance is unchanged"]),
   P("the battery supplies extra current for the new branch", ["extra current", "main current increases", "more current from the battery", "battery current increases"])],
  "The current through L1 stays the same, because it still has the full battery p.d. across it and its resistance has not changed (I = V / R). The battery simply supplies extra current for the new branch, so the main current increases.",
  ["Does adding a branch change the p.d. across L1?", "Use I = V / R for L1.", "Where does L2's current come from?"],
  "L1 current unchanged; main current increases",
  ["L1's current stays the same because it still has the full battery p.d., and the main current increases", "unchanged, since the voltage across L1 is the same; the battery supplies extra current"],
  ["L1's current halves because it is shared", "L1 goes out"], min_points=2,
  pitfalls=[PF(["halves because it is shared", "current is shared", "l1 gets dimmer"], "Adding a PARALLEL branch does not change the current in L1 (ideal battery).")],
  figure=lambda: sk.circuit(parallel=[[("lamp", "L1")], [("lamp", "L2 (added)")]], emf=""))

# ---------------------------------------------------------------- L4
Q("w13b_combination_4_8_8", 4, "13g", "Fig. 1 shows a 4 Ω resistor in series with two 8 Ω resistors in parallel, connected to a 12 V battery. Explain how to find the current from the battery and the p.d. across the parallel pair.",
  [P("the two 8 Ω in parallel give 4 Ω", ["4 ω", "4 ohms", "parallel pair is 4", "8 ÷ 2", "half of 8"]),
   P("total resistance 4 + 4 = 8 Ω, so I = 12 ÷ 8 = 1.5 A", ["1.5 a", "1.5 amps", "8 ω", "12 ÷ 8", "12 / 8"]),
   P("p.d. across the pair = 1.5 × 4 = 6 V", ["6 v", "6 volts", "6.0 v"])],
  "The two 8 Ω resistors in parallel have an effective resistance of 4 Ω. The total resistance is 4 + 4 = 8 Ω, so the battery current is I = 12 ÷ 8 = 1.5 A. The p.d. across the parallel pair is V = I R = 1.5 × 4 = 6 V.",
  ["Combine the parallel pair first.", "Add the series resistor and use I = V / R.", "Use V = IR for the pair."],
  "pair 4 Ω; total 8 Ω; I = 1.5 A; V = 6 V",
  ["The parallel pair is 4 Ω, so the total is 8 Ω and I = 1.5 A; the p.d. across the pair is 1.5 × 4 = 6 V", "8 Ω total, 1.5 A from the battery, 6 V across the parallel resistors"],
  ["Total is 20 Ω so I = 0.6 A", "I = 12 ÷ 4 = 3 A"], min_points=2,
  figure=lambda: sk.circuit(series=[("R", "4 Ω")], parallel=[[("R", "8 Ω")], [("R", "8 Ω")]], emf="12 V"))

Q("w13b_close_branch_switch", 4, "13d", "Fig. 1 shows two lamps in parallel with a switch in the branch of L2, which is open. Explain what happens to the reading of the main ammeter when the switch is closed.",
  [P("the main current increases", ["increases", "goes up", "rises", "larger", "bigger"]),
   P("L2's branch now also carries current", ["l2 now carries", "second branch", "extra branch", "another path", "current through l2"]),
   P("the main current is the sum of the branch currents (effective resistance falls)", ["sum of the branch currents", "add", "effective resistance decreases", "effective resistance falls", "total resistance falls", "lower total resistance"])],
  "The main ammeter reading increases. Closing the switch lets L2's branch carry current as well, and the main current is the sum of the branch currents; equivalently the effective resistance of the circuit falls.",
  ["What happens in L2's branch when the switch closes?", "How is the main current related to the branch currents?", "Explain."],
  "main current increases (extra branch current)",
  ["It increases, because L2's branch now carries current too and the main current is the sum of the branch currents", "the main current goes up as the effective resistance falls"],
  ["It decreases", "It stays the same"], min_points=2,
  figure=lambda: sk.circuit(series=[("A", "A")], parallel=[[("lamp", "L1")], [("lamp", "L2")]], emf="", switch=False))

Q("w13b_short_one_series_lamp", 4, "13c", "Two identical lamps are in series with a battery. A thick wire is connected across lamp L1 only. Explain what happens to each lamp.",
  [P("L1 goes out because the current takes the zero-resistance wire instead", ["l1 goes out", "goes out", "bypasses", "wire instead", "short circuit", "no current through l1"]),
   P("L2 gets brighter", ["l2 gets brighter", "brighter"]),
   P("because L2 now has the whole battery p.d. (total resistance halves, current increases)", ["whole battery p.d.", "full p.d.", "all the p.d.", "current increases", "resistance halves", "full voltage"])],
  "L1 goes out, because the current takes the path through the thick wire, which has almost no resistance, instead of through L1. L2 gets brighter: the total resistance is halved, so the current increases, and L2 now has the whole battery p.d. across it.",
  ["Which path does the current take: the lamp or the wire?", "What is the total resistance now?", "What p.d. does L2 get?"],
  "L1 off (bypassed); L2 brighter (full p.d.)",
  ["L1 goes out because the wire short-circuits it, and L2 gets brighter because it has the full battery p.d.", "the current bypasses L1 through the wire, so L1 goes out and L2 is brighter"],
  ["Both lamps go out", "Both stay the same"], min_points=2)

Q("w13b_make_3_and_9", 4, "13f", "A student has several 6 Ω resistors. Explain how to connect them to make an effective resistance of (a) 3 Ω and (b) 9 Ω.",
  [P("3 Ω: two 6 Ω resistors in parallel", ["two in parallel", "two 6 ω in parallel", "parallel gives 3", "2 in parallel", "parallel pair for 3", "pair for 3"]),
   P("9 Ω: two in parallel (3 Ω) in series with a third 6 Ω", ["in series with a third", "3 + 6", "3 ω in series with 6", "plus a third", "series with another 6"])],
  "(a) Two 6 Ω resistors in parallel give 6 ÷ 2 = 3 Ω. (b) Put that parallel pair (3 Ω) in series with a third 6 Ω resistor: 3 + 6 = 9 Ω.",
  ["Two identical resistors in parallel give what?", "Series resistances add.", "Combine."],
  "3 Ω: 2 in parallel; 9 Ω: parallel pair + 6 Ω in series",
  ["Two in parallel give 3 Ω; that pair in series with a third 6 Ω gives 9 Ω", "parallel pair for 3 ohms, then 3 + 6 = 9 ohms with another in series"],
  ["Two in series for 3 Ω", "Three in parallel for 9 Ω"], min_points=2)

Q("w13b_three_series_lamps_pd", 4, "13c", "Three identical lamps are connected in series to a 12 V battery. Explain the p.d. across each lamp.",
  [P("the p.d.s add up to 12 V", ["add up", "sum", "add to 12", "total of 12"]),
   P("identical lamps with the same current have equal p.d.s", ["identical", "equal", "same current", "shared equally", "same resistance"]),
   P("so each has 4 V", ["4 v", "4 volts", "4.0 v", "12 ÷ 3"])],
  "In series the p.d.s add up to the battery p.d. of 12 V. The lamps are identical and carry the same current, so they have equal p.d.s: 12 ÷ 3 = 4 V each.",
  ["What do the p.d.s add up to?", "Why are they equal?", "Divide."],
  "12 V shared equally → 4 V each",
  ["The p.d.s add to 12 V and the lamps are identical, so each has 4 V", "12 ÷ 3 = 4 V across each identical lamp"],
  ["12 V each", "36 V in total"], min_points=2,
  pitfalls=[PF(["12 v each", "12 volts each"], "12 V across each would be PARALLEL. In series they share it: 4 V each.")])

Q("w13b_series_parallel_compare", 4, "13f", "Two 10 Ω resistors are connected to a 10 V supply, first in series and then in parallel. Compare the current from the supply in each case.",
  [P("series: 20 Ω, current 0.5 A", ["0.5 a", "0.50 a", "20 ω", "20 ohms"]),
   P("parallel: 5 Ω, current 2 A", ["2 a", "2.0 a", "5 ω", "5 ohms"]),
   P("the parallel current is four times the series current", ["four times", "4 times", "×4", "larger in parallel"])],
  "In series the effective resistance is 20 Ω, so I = 10 ÷ 20 = 0.5 A. In parallel it is 5 Ω, so I = 10 ÷ 5 = 2 A. The parallel arrangement draws four times as much current.",
  ["Find the effective resistance in each case.", "Use I = V / R.", "Compare."],
  "series 20 Ω → 0.5 A; parallel 5 Ω → 2 A; ×4",
  ["Series gives 20 Ω and 0.5 A, parallel gives 5 Ω and 2 A, four times as much", "0.5 A in series and 2 A in parallel"],
  ["Both give 1 A", "Series gives more current"], min_points=2)

Q("w13b_fault_voltmeter", 4, "13c", "In a series circuit of a battery, a switch and a lamp, the switch is closed but the lamp does not light. A voltmeter across the lamp reads the full battery p.d. Explain what the fault is.",
  [P("the lamp is broken / its filament is broken (open circuit at the lamp)", ["filament is broken", "lamp is broken", "broken filament", "open circuit", "lamp has blown", "blown"]),
   P("no current flows, so there is no p.d. across the rest of the circuit", ["no current", "no p.d. across the rest", "rest of the circuit"]),
   P("so the whole battery p.d. appears across the gap in the lamp", ["whole battery p.d.", "full p.d. across", "across the gap", "across the break", "full battery p.d."])],
  "The lamp's filament is broken, making an open circuit at the lamp. With no current flowing, there is no p.d. across the rest of the circuit, so the whole battery p.d. appears across the break in the lamp, which is what the voltmeter reads.",
  ["Is current flowing?", "Where does the battery p.d. appear if there is a break?", "Identify the fault."],
  "broken lamp (open circuit); full p.d. across the break",
  ["The lamp's filament is broken, so no current flows and the whole battery p.d. is across the lamp", "an open circuit at the lamp; the voltmeter reads the full battery p.d. across the break"],
  ["The battery is flat", "The voltmeter is broken"], min_points=2,
  pitfalls=[PF(["battery is flat"], "A flat battery would give NO voltmeter reading; the full p.d. across the lamp shows the break is at the lamp.")])

Q("w13b_branch_currents_4_6", 4, "13g", "A 4 Ω and a 6 Ω resistor are connected in parallel across a 12 V battery. Explain how to find the current in each branch and from the battery.",
  [P("each branch has 12 V across it", ["12 v across", "same p.d.", "12 v each", "full 12 v"]),
   P("I₁ = 12 ÷ 4 = 3 A and I₂ = 12 ÷ 6 = 2 A", ["3 a", "2 a", "12 ÷ 4", "12 / 4"]),
   P("battery current = 3 + 2 = 5 A", ["5 a", "5 amps", "3 + 2", "5.0 a"])],
  "Each branch has the full 12 V across it. The branch currents are I = V / R: 12 ÷ 4 = 3 A and 12 ÷ 6 = 2 A. The battery current is their sum, 3 + 2 = 5 A.",
  ["What is the p.d. across each branch?", "Use I = V / R for each.", "Add."],
  "12 V each; 3 A and 2 A; total 5 A",
  ["Each has 12 V, so the currents are 3 A and 2 A and the battery supplies 5 A", "12 / 4 = 3 A, 12 / 6 = 2 A, total 5 A"],
  ["1.2 A each", "Total 1.2 A because R = 10 Ω"], min_points=2)

Q("w13b_add_parallel_voltmeter", 4, "13g", "A 2 Ω resistor is in series with a 4 Ω resistor across a 6 V supply. A second 4 Ω resistor is then connected in parallel with the first 4 Ω. Explain what happens to the p.d. across the 4 Ω part.",
  [P("before: 6 V shared 2 : 4, so 4 V across the 4 Ω", ["4 v", "4 volts", "before"]),
   P("after: the parallel pair is 2 Ω, equal to the series resistor", ["2 ω", "2 ohms", "parallel pair is 2", "pair is 2"]),
   P("so the p.d. falls to 3 V (shared equally)", ["3 v", "3 volts", "falls", "decreases", "shared equally"])],
  "Before, the 6 V is shared in the ratio 2 : 4, so the 4 Ω has 4 V across it. After, the two 4 Ω in parallel give 2 Ω, the same as the series resistor, so the 6 V is shared equally and the p.d. across the parallel part falls to 3 V.",
  ["Work out the p.d. share before.", "What is the parallel pair's resistance?", "Work out the new share."],
  "4 V → 3 V",
  ["It falls from 4 V to 3 V, because the parallel pair is only 2 Ω and the 6 V is then shared equally", "the parallel pair is 2 ohms, so the p.d. drops from 4 V to 3 V"],
  ["It stays at 4 V", "It rises to 6 V"], min_points=2)

Q("w13b_mixed_brightness", 4, "13d", "Fig. 1 shows lamp L1 in series with two identical lamps L2 and L3 connected in parallel. All three lamps are identical. Explain which lamp is brightest.",
  [P("L1 is the brightest", ["l1 is the brightest", "l1 is brightest", "l1 brightest", "l1"]),
   P("all the current passes through L1", ["all the current", "whole current", "main current", "full current", "total current"]),
   P("the current then splits equally between L2 and L3, so each gets half", ["splits", "half", "shared", "divides"])],
  "L1 is the brightest. All of the main current passes through L1, and then it splits equally between the identical lamps L2 and L3, so each of them carries only half of it. (L1 also has the larger share of the p.d.)",
  ["Which lamp carries the whole current?", "What happens to the current at the junction?", "Compare."],
  "L1: whole current; L2, L3: half each",
  ["L1 is brightest because all the current goes through it, while L2 and L3 each get half", "the main current flows through L1 and then splits between L2 and L3"],
  ["L2 and L3 are brightest because they are in parallel", "All are equally bright"], min_points=2,
  pitfalls=[PF(["equally bright", "l2 and l3 are brightest"], "L1 carries the WHOLE current; L2 and L3 each carry half, so L1 is brightest.")],
  figure=lambda: sk.circuit(series=[("lamp", "L1")], parallel=[[("lamp", "L2")], [("lamp", "L3")]], emf=""))

# ---------------------------------------------------------------- L5
Q("w13b_claim_more_resistors", 5, "13f", "A student says: 'Adding another resistor to a circuit always increases the total resistance.' Evaluate this claim.",
  [P("true only if the resistor is added in series", ["in series", "series"]),
   P("adding a resistor in parallel decreases the total resistance", ["in parallel decreases", "parallel decreases", "parallel reduces", "less resistance in parallel", "decreases in parallel", "lower"]),
   P("because a parallel branch gives the current an extra path (effective resistance less than the smallest)", ["extra path", "another path", "less than the smallest", "more paths"])],
  "The claim is only true for a resistor added in series, where resistances add. Adding a resistor in parallel decreases the total resistance, because it gives the current an extra path; the effective resistance is less than the smallest resistor.",
  ["What happens to total R when you add in series?", "What about in parallel?", "Evaluate."],
  "series: up; parallel: down (extra path)",
  ["Only in series; adding a resistor in parallel decreases the total resistance because there is an extra path", "true for series, false for parallel where the resistance decreases"],
  ["Correct, resistance always increases", "Correct, more resistors always mean less current"], min_points=2, pitfalls=[PARALLEL_ADDS])

Q("w13b_claim_parallel_battery_lasts", 5, "13d", "A student says: 'Connecting lamps in parallel makes a battery last longer than connecting them in series.' Evaluate this claim.",
  [P("wrong: lamps in parallel draw a larger current from the battery", ["wrong", "larger current", "more current", "draw more current", "higher current"]),
   P("because the effective resistance is lower and each lamp has the full p.d.", ["lower resistance", "effective resistance is lower", "full p.d.", "less resistance"]),
   P("so the battery's energy is used faster and it goes flat sooner", ["flat sooner", "runs out faster", "used faster", "shorter time", "faster"])],
  "The claim is wrong. In parallel the effective resistance is lower and each lamp has the full p.d., so a larger current is drawn from the battery. The lamps are brighter, but the battery's energy is used faster and it goes flat sooner.",
  ["Which arrangement has the lower total resistance?", "Which draws more current?", "What happens to the battery?"],
  "wrong; parallel → more current → battery runs down faster",
  ["Wrong: parallel lamps draw more current because the resistance is lower, so the battery goes flat sooner", "wrong, because the parallel circuit draws more current and uses energy faster, so the battery runs out faster"],
  ["Correct, parallel saves energy", "Correct, parallel circuits use no current"], min_points=2)

Q("w13b_design_current_rule", 5, "13d", "Design an experiment to check that the branch currents in a parallel circuit add up to the main current.",
  [P("set up two (or more) resistors/lamps in parallel with a battery", ["in parallel", "parallel circuit", "two resistors", "two lamps"]),
   P("place ammeters in the main circuit and in each branch (in series)", ["ammeter in each branch", "ammeters", "main circuit", "in each branch"]),
   P("compare the main reading with the sum of the branch readings; repeat with different resistors", ["sum", "add the branch readings", "compare", "repeat", "different resistors"])],
  "Connect two resistors in parallel to a battery. Place an ammeter in series in the main circuit and one in each branch. Close the switch and compare the main reading with the sum of the branch readings. Repeat with different resistors (or more branches) to check the rule holds each time.",
  ["What circuit do you need?", "Where do the ammeters go?", "What do you compare, and how do you make it reliable?"],
  "parallel circuit; ammeters in main + each branch; compare sum; repeat",
  ["Set up resistors in parallel with ammeters in the main circuit and each branch, and check that the branch readings add up to the main reading; repeat with different resistors", "put an ammeter in each branch and in the main wire, then compare the sum"],
  ["Use a voltmeter across the battery only", "Measure the resistance with a ruler"], min_points=2)

Q("w13b_claim_bigger_r_more_pd_parallel", 5, "13e", "A student says: 'In a parallel circuit, the resistor with the larger resistance has the larger p.d. across it.' Evaluate this.",
  [P("wrong: in parallel both resistors have the same p.d.", ["wrong", "same p.d.", "same voltage", "equal p.d."]),
   P("this is true in series, not parallel", ["series", "in series"]),
   P("in parallel the larger resistance carries the smaller current (I = V / R)", ["smaller current", "less current", "i = v / r", "carries less"])],
  "The statement is wrong. In parallel each branch is across the same two points, so both resistors have the same p.d. The larger resistor carries the smaller current, because I = V / R. The statement would be true for resistors in series, where the current is the same.",
  ["What is the same for parallel branches?", "What differs between them?", "Where would the statement be true?"],
  "wrong; same p.d. in parallel; larger R → smaller I; true in series",
  ["Wrong: in parallel the p.d. is the same, and the larger resistor just carries less current; it is true in series", "both have the same voltage in parallel; the larger resistance takes a smaller current"],
  ["Correct, larger resistance always means larger p.d.", "Correct, the smaller resistor gets less p.d."], min_points=2)

Q("w13b_design_series_pd_rule", 5, "13c", "Design an experiment to check that the p.d.s across components in series add up to the p.d. across the battery.",
  [P("connect two (or three) resistors/lamps in series with a battery", ["in series", "series circuit", "two resistors", "two lamps"]),
   P("use a voltmeter in parallel across each component and across the battery", ["voltmeter across each", "voltmeter", "across each component", "across the battery", "in parallel"]),
   P("check the component readings add to the battery reading; repeat with different components", ["add up", "sum", "compare", "repeat", "different"])],
  "Connect two or three resistors in series with a battery and switch. Connect a voltmeter in parallel across each resistor in turn, and then across the battery. Check that the readings across the resistors add up to the reading across the battery. Repeat with different resistors to show the rule holds generally.",
  ["What circuit do you need?", "How is the voltmeter connected?", "What do you compare?"],
  "series circuit; voltmeter across each and battery; compare sum; repeat",
  ["Set up resistors in series and measure the p.d. across each and across the battery with a voltmeter, then check they add up; repeat with different resistors", "use a voltmeter across each component and check that the sum equals the battery p.d."],
  ["Use an ammeter across each resistor", "Measure the current only"], min_points=2)

Q("w13b_fault_one_parallel_lamp", 5, "13e", "Two lamps are in parallel. L1 lights but L2 does not. Evaluate two possible causes and how a voltmeter could tell them apart.",
  [P("cause 1: L2's filament is broken", ["filament is broken", "lamp is broken", "broken filament", "blown", "l2 is broken"]),
   P("cause 2: a loose connection / broken wire in L2's branch", ["loose connection", "broken wire", "loose wire", "bad connection"]),
   P("voltmeter across L2: full p.d. means the lamp is broken; zero means the break is elsewhere in the branch (the wire)", ["full p.d.", "zero", "reads the battery voltage", "no reading", "across l2"])],
  "L2 may have a broken filament, or there may be a loose connection or broken wire in its branch. The battery and the rest of the circuit work, since L1 lights. A voltmeter across L2 tells them apart: if it reads the full battery p.d., the break is in the lamp itself; if it reads zero, the lamp is not receiving the p.d., so the break is in the wiring of that branch.",
  ["Why can't the battery be the problem?", "What could break the L2 branch?", "What would a voltmeter across L2 show in each case?"],
  "broken filament or loose connection; voltmeter: full p.d. → lamp; zero → wiring",
  ["L2's filament could be broken or its wire loose; a voltmeter across L2 reads the full p.d. if the lamp is broken but zero if the wire is broken", "either a blown lamp or a bad connection in L2's branch; check with a voltmeter across L2"],
  ["The battery is flat", "L1 is taking all the current"], min_points=2,
  pitfalls=[PF(["battery is flat", "taking all the current"], "L1 lights, so the battery works; the fault is in L2's branch.")])

Q("w13b_claim_half_parallel", 5, "13f", "A student says: 'The effective resistance of any two resistors in parallel is half the larger one.' Evaluate this, using a 6 Ω and a 3 Ω resistor.",
  [P("wrong in general: only true for two identical resistors (half of either)", ["wrong", "only for identical", "identical", "only true if they are equal", "equal resistors"]),
   P("for 6 Ω and 3 Ω: 1/R = 1/6 + 1/3, so R = 2 Ω, not 3 Ω", ["2 ω", "2 ohms", "not 3", "1/6 + 1/3"]),
   P("the effective resistance is always less than the smaller resistor", ["less than the smaller", "less than the smallest", "smaller than 3"])],
  "The statement is wrong in general. For two identical resistors the effective resistance is half of either one, but for 6 Ω and 3 Ω, 1/R = 1/6 + 1/3 = 1/2, so R = 2 Ω, not 3 Ω. In parallel the effective resistance is always less than the smaller resistor.",
  ["When is 'half' correct?", "Work out 6 Ω and 3 Ω in parallel.", "Compare with the student's rule."],
  "wrong; only for identical; 6∥3 = 2 Ω; always < smaller",
  ["Wrong: it only works for identical resistors; 6 and 3 in parallel give 2 Ω, which is less than the smaller one", "it only works for identical resistors: 1/6 + 1/3 = 1/2 gives 2 Ω, not half of 6"],
  ["Correct, 6 and 3 give 3 Ω", "Correct, always half"], min_points=2)

Q("w13b_network_three_12", 5, "13f", "Using three 12 Ω resistors, explain how to make an effective resistance of 18 Ω and of 4 Ω.",
  [P("18 Ω: two in parallel (6 Ω) in series with the third (12 Ω)", ["6 + 12", "two in parallel in series", "in series with the third", "parallel pair in series"]),
   P("4 Ω: all three in parallel", ["all three in parallel", "three in parallel", "12 ÷ 3"])],
  "For 18 Ω, connect two resistors in parallel (12 ÷ 2 = 6 Ω) and put this pair in series with the third: 6 + 12 = 18 Ω. For 4 Ω, connect all three in parallel: 12 ÷ 3 = 4 Ω.",
  ["Two identical in parallel give half.", "Three identical in parallel give a third.", "Combine with series."],
  "18 Ω: (12∥12) + 12; 4 Ω: all three in parallel",
  ["Two in parallel give 6 Ω, plus the third in series gives 18 Ω; all three in parallel give 4 Ω", "parallel pair in series with the third for 18 ohms, all three in parallel for 4 ohms"],
  ["All three in series for 18 Ω", "Two in series for 4 Ω"], min_points=2)

Q("w13b_claim_short_harmless", 5, "13g", "A student says: 'Connecting a thick copper wire straight across a battery is harmless, because there is no lamp to burn out.' Evaluate this claim.",
  [P("wrong: the wire has almost no resistance, so a very large current flows (short circuit)", ["wrong", "very large current", "huge current", "short circuit", "almost no resistance", "very low resistance"]),
   P("the wire and battery get very hot (could cause burns or fire)", ["very hot", "overheat", "fire", "burn", "heats up"]),
   P("the battery quickly runs flat / may be damaged", ["runs flat", "damaged", "drains", "goes flat quickly"])],
  "The claim is wrong. The thick wire has almost no resistance, so by I = V / R a very large current flows: a short circuit. The wire and the battery become very hot, which could cause burns or a fire, and the battery is quickly drained or damaged.",
  ["What is the resistance of a thick copper wire?", "What current does I = V / R give?", "What happens to the wire and battery?"],
  "wrong; R ≈ 0 → huge current; overheating; battery drained",
  ["Wrong: the wire has almost no resistance, so a huge current flows, the wire and battery overheat and the battery goes flat", "it is a short circuit; the very large current can cause a fire"],
  ["Correct, no current flows without a lamp", "Correct, copper stops the current"], min_points=2)

Q("w13b_claim_ammeters_branch_equal", 5, "13d", "A student finds ammeter readings of 0.5 A and 0.3 A in two parallel branches, and 0.6 A in the main circuit. Evaluate these results.",
  [P("the branch currents should add up to the main current", ["add up", "sum", "should equal", "add to the main", "do not add up"]),
   P("0.5 + 0.3 = 0.8 A, not 0.6 A, so a reading is wrong", ["0.8 a", "0.8", "not 0.6", "do not add up", "does not match"]),
   P("possible causes: zero error, misread scale, faulty meter; repeat / check the meters", ["zero error", "misread", "faulty", "repeat", "check", "parallax"])],
  "The results cannot all be right, because the branch currents in a parallel circuit should add up to the main current: 0.5 + 0.3 = 0.8 A, not 0.6 A. One of the meters may have a zero error, been misread or be faulty; the meters should be checked for zero error and the readings repeated.",
  ["What rule links the three readings?", "Do they obey it?", "What could cause the difference?"],
  "branch sum 0.8 A ≠ 0.6 A → error (zero error, misreading); repeat",
  ["The branch currents should add to the main current, but 0.5 + 0.3 = 0.8 A, not 0.6 A, so a meter has an error; check for zero error and repeat", "they do not add up: 0.5 + 0.3 is 0.8 A, so one reading is wrong"],
  ["They are correct because current is used up", "The main current should be smaller than each branch"], min_points=2,
  pitfalls=[CURRENT_USED_UP])
