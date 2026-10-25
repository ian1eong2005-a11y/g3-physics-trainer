"""Chapter 15 Magnetism and Electromagnetism: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import sketches2 as sk
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 15


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


ATTRACT_PROVES = PF(["attraction proves", "attracts so it is a magnet", "attraction shows it is a magnet"],
                    "Attraction does not prove a magnet: a magnet also attracts unmagnetised iron. Only REPULSION proves it.")
ALUMINIUM_MAGNETIC = PF(["aluminium is magnetic", "copper is magnetic", "all metals are magnetic"],
                        "Only iron, steel, nickel and cobalt (and their alloys) are magnetic; aluminium and copper are not.")

# ---------------------------------------------------------------- L1
Q("w15b_like_unlike_poles", 1, "15a", "State what happens when two like poles, and when two unlike poles, of magnets are brought together.",
  [P("like poles repel", ["like poles repel", "same poles repel", "like repel", "north and north repel", "n and n repel", "same poles push apart", "push apart"]),
   P("unlike poles attract", ["unlike poles attract", "opposite poles attract", "unlike attract", "north and south attract", "n and s attract"])],
  "Like poles (N and N, or S and S) repel each other; unlike poles (N and S) attract each other.",
  ["Two north poles: push or pull?", "A north and a south pole?", "State both."],
  "like repel; unlike attract",
  ["Like poles repel and unlike poles attract", "the same poles push apart and opposite poles attract"],
  ["Like poles attract", "All poles attract"], min_points=2,
  pitfalls=[PF(["like poles attract", "same poles attract"], "LIKE poles REPEL; UNLIKE poles attract.")])

Q("w15b_field_def", 1, "15d", "State what is meant by a magnetic field.",
  [P("a region in which a magnetic material (or magnetic pole) experiences a force", ["region", "area around", "space around"]),
   P("where a magnetic material or pole feels a force", ["experiences a force", "feels a force", "force on a magnetic", "magnetic force"])],
  "A magnetic field is a region in which a magnetic pole or magnetic material experiences a force.",
  ["It is a region around a magnet.", "What happens to iron in it?", "State it."],
  "region where magnetic material feels a force",
  ["A region where a magnetic material experiences a force", "the space around a magnet where a magnetic pole feels a force"],
  ["The lines drawn on paper", "The north pole of a magnet"], min_points=2)

Q("w15b_suspended_magnet", 1, "15a", "A bar magnet is hung by a thread so that it can turn freely. State which way it comes to rest.",
  [P("along the north–south direction, with its north pole pointing north", ["north-south", "north south", "points north", "north pole points north", "n pole points north", "pointing north"])],
  "It comes to rest along the north–south direction, with its north-seeking pole pointing (geographic) north.",
  ["This is how a compass works.", "Which end points north?", "State it."],
  "N–S, north pole to north",
  ["It points north–south with its north pole pointing north", "the north pole points north"],
  ["It points east–west", "It keeps spinning"],
  pitfalls=[PF(["east-west", "east west", "keeps spinning"], "A freely suspended magnet settles NORTH–SOUTH.")])

Q("w15b_field_strongest", 1, "15e", "Fig. 1 shows the field around a bar magnet. State where the field is strongest and how the diagram shows this.",
  [P("at the poles", ["poles", "at the ends", "near the poles"]),
   P("where the field lines are closest together", ["closest together", "closer together", "lines are close", "most lines", "densest", "close together"])],
  "The field is strongest at the poles, where the field lines are closest together.",
  ["Where do the lines bunch up?", "Closer lines mean what?", "State both."],
  "at the poles; lines closest",
  ["At the poles, where the field lines are closest together", "near the ends, because the lines are closer together"],
  ["In the middle of the magnet", "Far from the magnet"], min_points=2,
  figure=lambda: sk.bar_magnet_field())

Q("w15b_field_line_rules", 1, "15e", "State two rules followed by magnetic field lines drawn around a magnet.",
  [P("they go from north to south outside the magnet", ["north to south", "n to s", "from north"]),
   P("they never cross", ["never cross", "do not cross", "don't cross"]),
   P("they are closer together where the field is stronger", ["closer together", "closer where stronger", "closer lines", "stronger field"])],
  "Field lines go from the north pole to the south pole outside the magnet, they never cross, and they are drawn closer together where the field is stronger.",
  ["Which direction do the arrows point?", "Can two lines cross?", "What does spacing show?"],
  "N → S; never cross; closer = stronger",
  ["They go from north to south and they never cross", "lines never cross and are closer together where the field is stronger"],
  ["They go from south to north and cross at the poles", "They are always straight"], min_points=2,
  pitfalls=[PF(["south to north", "cross at the poles", "lines cross"], "Field lines go N → S outside the magnet and NEVER cross.")])

Q("w15b_electromagnet_def", 1, "15b", "State what an electromagnet is.",
  [P("a coil of wire (solenoid) wound on a soft iron core", ["coil", "solenoid", "iron core", "soft iron"]),
   P("which is magnetic only while a current flows", ["only when a current", "while a current flows", "when the current is on", "switched on and off", "current flows"])],
  "An electromagnet is a coil of wire (solenoid) wound on a soft iron core, which is magnetic only while a current flows through the coil.",
  ["What is it made of?", "When is it magnetic?", "State it."],
  "coil on soft iron core, magnetic when current flows",
  ["A coil of wire on a soft iron core that is magnetic only when a current flows", "a solenoid with an iron core that becomes magnetic when the current is on"],
  ["A permanent steel magnet", "A magnet made of copper"], min_points=2)

Q("w15b_wire_field_shape", 1, "15f", "Fig. 1 shows a straight wire carrying a current into the page. State the shape of the magnetic field lines around it.",
  [P("concentric circles around the wire", ["concentric circles", "circles", "circular", "rings"])],
  "The field lines are concentric circles centred on the wire.",
  ["Do the lines go along the wire or around it?", "What shape?", "State it."],
  "concentric circles",
  ["Concentric circles around the wire", "circles centred on the wire"],
  ["Straight lines parallel to the wire", "Lines from north to south"],
  pitfalls=[PF(["straight lines parallel", "parallel to the wire"], "The field lines are CIRCLES around the wire.")],
  figure=lambda: sk.straight_wire_field(True))

Q("w15b_wire_more_current", 1, "15f", "State the effect on the magnetic field around a straight wire of increasing the current.",
  [P("the field becomes stronger (lines drawn closer together)", ["stronger", "stronger field", "closer together", "increases"])],
  "Increasing the current makes the magnetic field stronger; the circles are drawn closer together.",
  ["More current gives more or less field?", "How would the diagram change?", "State it."],
  "stronger field",
  ["The field becomes stronger", "the field lines get closer together because the field is stronger"],
  ["The field becomes weaker", "The field reverses"])

Q("w15b_wire_reverse", 1, "15f", "State the effect on the magnetic field around a straight wire of reversing the current.",
  [P("the direction of the field reverses (clockwise becomes anticlockwise)", ["reverses", "opposite direction", "changes direction", "anticlockwise", "reversed", "opposite way", "other way round"])],
  "Reversing the current reverses the direction of the magnetic field: clockwise circles become anticlockwise.",
  ["Does the shape change?", "What about the arrows on the circles?", "State it."],
  "field direction reverses",
  ["The field direction reverses", "the field goes the opposite way round"],
  ["The field disappears", "The field gets stronger"])

Q("w15b_lhr_fingers", 1, "15h", "State what the thumb, first finger and second finger represent in Fleming's left-hand rule.",
  [P("first finger: field", ["first finger field", "first finger is the field", "first finger: field", "forefinger field", "first finger magnetic field"]),
   P("second finger: current", ["second finger current", "second finger is the current", "second finger: current", "middle finger current"]),
   P("thumb: force (motion)", ["thumb force", "thumb is the force", "thumb: force", "thumb motion", "thumb is the motion", "thumb thrust"])],
  "First finger = magnetic field, second finger = current, thumb = force (motion).",
  ["Field, Current, Motion — which finger is which?", "The first finger points along the field.", "State all three."],
  "first finger field; second finger current; thumb force",
  ["First finger is the field, second finger is the current, thumb is the force", "thumb = motion, first finger = field, second finger = current"],
  ["Thumb is the current, first finger the force", "First finger is the current"], min_points=3)

# ---------------------------------------------------------------- L2
Q("w15b_repulsion_test", 2, "15a", "Explain why repulsion, not attraction, is the only sure test that an object is a magnet.",
  [P("a magnet attracts both magnets and unmagnetised magnetic materials (e.g. iron)", ["attracts iron", "unmagnetised", "magnetic material", "attracts both", "also attracts", "could be iron"]),
   P("only two magnets can repel each other (like poles)", ["only two magnets", "only magnets repel", "like poles repel", "repel only", "repulsion needs", "needs like poles"])],
  "A magnet attracts both other magnets and unmagnetised magnetic materials such as iron, so attraction does not prove an object is a magnet. Only two magnets can repel (like poles), so repulsion is the sure test.",
  ["What else, apart from a magnet, does a magnet attract?", "What can only happen between two magnets?", "Explain."],
  "attraction also with iron; repulsion only between magnets",
  ["A magnet attracts unmagnetised iron as well, but only two magnets repel", "attraction could be iron; repulsion needs like poles of two magnets"],
  ["Because attraction is weaker", "Because magnets never attract"], min_points=2, pitfalls=[ATTRACT_PROVES])

Q("w15b_induced_nail", 2, "15b", "An iron nail is placed near the north pole of a magnet. Describe and explain what happens.",
  [P("the nail becomes an induced magnet", ["induced magnet", "becomes magnetised", "induced magnetism", "becomes a magnet"]),
   P("the end nearest the north pole becomes a south pole", ["nearest end becomes south", "near end becomes south", "end near the north pole becomes a south", "south pole", "becomes s"]),
   P("so the nail is attracted (unlike poles attract)", ["attracted", "unlike poles attract", "attract"])],
  "The nail becomes an induced magnet: the end nearest the magnet's north pole becomes a south pole, and the far end a north pole. Unlike poles attract, so the nail is attracted to the magnet.",
  ["What does the magnet do to the nail?", "Which pole is induced at the near end?", "What happens then?"],
  "induced magnet; near end S; attracted",
  ["The nail becomes an induced magnet with a south pole at the end near the north pole, so it is attracted", "magnetism is induced, the near end becomes S, and unlike poles attract"],
  ["The nail is repelled", "Nothing happens to iron"], min_points=2,
  pitfalls=[PF(["nail is repelled", "repels the nail"], "Induced magnetism always gives ATTRACTION: the near end becomes the opposite pole.")])

Q("w15b_solenoid_vs_bar", 2, "15f", "Compare the magnetic field of a current-carrying solenoid with that of a bar magnet.",
  [P("outside, the field pattern is the same shape as a bar magnet's", ["same shape", "like a bar magnet", "similar", "same as a bar magnet"]),
   P("the ends of the solenoid act as north and south poles", ["ends act as poles", "north and south poles", "poles at the ends", "one end north"]),
   P("inside the solenoid the field is strong and uniform (parallel lines)", ["inside", "uniform", "parallel lines", "strong inside"])],
  "Outside, a solenoid's field has the same shape as a bar magnet's, and its ends act as north and south poles. Inside the solenoid the field is strong and uniform, shown by parallel, evenly spaced lines.",
  ["What does the outside field look like?", "What do the ends behave as?", "What is the field like inside?"],
  "like bar magnet outside; ends are poles; uniform inside",
  ["It has the same shape as a bar magnet's field, the ends act as poles, and inside the field is uniform", "like a bar magnet with poles at its ends, with parallel lines inside"],
  ["It is circles like a straight wire only", "It has no poles"], min_points=2,
  figure=lambda: sk.solenoid_field())

Q("w15b_plot_wire_field", 2, "15f", "Describe how to show the shape of the magnetic field around a straight vertical current-carrying wire.",
  [P("pass the wire vertically through a horizontal card", ["through a card", "horizontal card", "card", "cardboard"]),
   P("sprinkle iron filings on the card (or place plotting compasses) and switch on a large current", ["iron filings", "plotting compass", "compasses"]),
   P("tap the card; the filings form circles around the wire", ["tap", "circles", "concentric", "rings"])],
  "Pass the wire vertically through a horizontal card. Sprinkle iron filings on the card (or place small plotting compasses around the wire) and switch on a large current. Tap the card gently: the filings line up in concentric circles around the wire.",
  ["How is the card arranged?", "What shows the field?", "What pattern appears?"],
  "wire through card; iron filings/compasses; circles",
  ["Pass the wire through a card, sprinkle iron filings, switch on and tap; the filings form circles", "put plotting compasses on a card around the wire to show the circular field"],
  ["Hold a bar magnet near the wire", "Measure the current"], min_points=2)

Q("w15b_two_ways_bigger_force", 2, "15g", "State and explain two ways of increasing the force on a current-carrying wire in a magnetic field.",
  [P("increase the current", ["increase the current", "larger current", "more current", "bigger current"]),
   P("use a stronger magnet (stronger field)", ["stronger magnet", "stronger field", "stronger magnetic field", "more powerful magnet"]),
   P("the force depends on both the current and the field strength", ["depends on", "stronger interaction", "both", "field strength"])],
  "Increase the current in the wire, or use a stronger magnet to give a stronger field. The force depends on both the size of the current and the strength of the field.",
  ["What two things interact to make the force?", "Make each larger.", "State both."],
  "more current; stronger magnet",
  ["Increase the current and use a stronger magnet", "a larger current or a stronger magnetic field"],
  ["Use a longer magnet only", "Reverse the current"], min_points=2)

Q("w15b_lhr_down", 2, "15h", "Fig. 1 shows a wire carrying a current into the page in a magnetic field directed to the right. Use Fleming's left-hand rule to find the direction of the force.",
  [P("the force is downwards", ["downwards", "down", "downward"]),
   P("first finger to the right (field), second finger into the page (current), thumb points down", ["first finger", "second finger", "thumb", "left-hand rule", "left hand rule"])],
  "Point the first finger to the right (field) and the second finger into the page (current). The thumb then points downwards, so the force on the wire is downwards.",
  ["Point your first finger along the field.", "Point your second finger along the current.", "Where does your thumb point?"],
  "force downwards",
  ["The force is downwards: first finger right, second finger into the page, thumb down", "using the left-hand rule the thumb points down"],
  ["Upwards", "To the left"], min_points=1,
  pitfalls=[PF(["force is upwards", "force is up", "force is to the left", "force is to the right", "upward force"], "Field right, current into the page: the force is DOWN.")],
  figure=lambda: sk.flemings_lhr(field="right", current="into"))

Q("w15b_parallel_no_force", 2, "15h", "A current-carrying wire is placed parallel to the magnetic field lines. State the force on it and explain.",
  [P("there is no force", ["no force", "zero force", "force is zero", "no magnetic force"]),
   P("a force only acts when the current has a component at right angles (perpendicular) to the field", ["right angles", "perpendicular", "at an angle", "across the field", "cut across"])],
  "There is no force on the wire. A force acts on a current-carrying wire only when the current is at an angle to (ideally at right angles to) the field; parallel to the field there is no force.",
  ["When does the left-hand rule give a force?", "What angle is the current to the field here?", "Explain."],
  "no force (current parallel to field)",
  ["There is no force because the current is parallel to the field, not at right angles to it", "zero force; there must be an angle between the current and the field"],
  ["A maximum force", "A force along the wire"], min_points=1,
  pitfalls=[PF(["maximum force", "force along the wire"], "Parallel to the field there is NO force.")])

Q("w15b_demagnetise", 2, "15c", "Describe two ways of demagnetising a steel magnet.",
  [P("heat it strongly", ["heat", "heating", "heat it"]),
   P("hammer it (or drop it repeatedly)", ["hammer", "hammering", "drop it", "dropping"])],
  "A steel magnet can be demagnetised by heating it strongly or by hammering it (or dropping it repeatedly), which jumbles its magnetic alignment.",
  ["What does violent treatment do to a magnet?", "What does strong heat do?", "Give two ways."],
  "heat; hammer",
  ["Heat it strongly or hammer it", "hammer it hard or heat it until red hot"],
  ["Cool it in a fridge", "Paint it"], min_points=2)

Q("w15b_magnetise_steel", 2, "15b", "Describe how a steel bar can be made into a permanent magnet using a solenoid.",
  [P("place the steel bar inside a solenoid", ["inside a solenoid", "in a solenoid", "inside the coil", "in the coil"]),
   P("pass a (large) direct current through the solenoid for a short time", ["direct current", "d.c.", "dc", "switch on", "pass a current", "large current"]),
   P("switch off and remove it: the steel stays magnetised", ["stays magnetised", "remains magnetised", "keeps its magnetism", "remove", "switch off"])],
  "Place the steel bar inside a solenoid and pass a large direct current through the solenoid briefly. Switch off and remove the bar: because steel is a hard magnetic material, it stays magnetised.",
  ["Where does the bar go?", "What current is used?", "What happens when you switch off?"],
  "steel in solenoid; d.c. on; stays magnetised",
  ["Put the steel bar inside a solenoid, switch on a direct current, then switch off; the steel stays magnetised", "place it in the coil and pass a large d.c. current through it"],
  ["Rub it with copper", "Heat it in a flame"], min_points=2)

Q("w15b_test_coin", 2, "15a", "Describe how to test whether a coin contains a magnetic material, and what each result shows.",
  [P("bring a magnet close to the coin", ["bring a magnet", "hold a magnet", "magnet near", "use a magnet"]),
   P("if it is attracted, it contains a magnetic material (iron, steel, nickel or cobalt)", ["attracted", "nickel", "iron", "steel", "magnetic material"]),
   P("if it is not attracted, it is made of non-magnetic metals (e.g. copper, aluminium)", ["not attracted", "non-magnetic", "copper", "aluminium", "no effect"])],
  "Bring a magnet close to the coin. If the coin is attracted, it contains a magnetic material such as iron, steel or nickel. If it is not attracted, it is made only of non-magnetic metals such as copper or aluminium.",
  ["What tool do you need?", "What does attraction tell you?", "What does no attraction tell you?"],
  "magnet near coin: attracted → magnetic; not → non-magnetic",
  ["Bring a magnet near; if the coin is attracted it contains a magnetic material like nickel or steel, if not it is non-magnetic", "use a magnet: attraction means iron, steel or nickel; no attraction means copper or aluminium"],
  ["Weigh the coin", "Heat the coin and see if it glows"], min_points=2, pitfalls=[ALUMINIUM_MAGNETIC])

# ---------------------------------------------------------------- L3
Q("w15b_steel_keeps", 3, "15c", "An iron bar and a steel bar are both magnetised inside a solenoid and then removed. Explain the difference in what happens to them.",
  [P("the steel bar stays magnetised (permanent magnet)", ["steel stays magnetised", "steel keeps", "steel remains", "steel is permanent", "steel stays"]),
   P("the iron bar loses most of its magnetism (temporary magnet)", ["iron loses", "iron is temporary", "iron does not stay", "iron loses its magnetism", "iron loses most"]),
   P("steel is hard magnetic, hard to magnetise and demagnetise; iron is soft magnetic, easy to magnetise and demagnetise", ["hard magnetic", "soft magnetic", "easy to demagnetise", "hard to demagnetise", "easily"])],
  "The steel bar stays magnetised, becoming a permanent magnet, while the iron bar loses most of its magnetism, so it is only a temporary magnet. Steel is a hard magnetic material: hard to magnetise and hard to demagnetise. Iron is soft: easily magnetised and easily demagnetised.",
  ["Which material keeps its magnetism?", "Which loses it?", "Why?"],
  "steel permanent; iron temporary",
  ["Steel stays magnetised but iron loses its magnetism, because iron is easily demagnetised", "the steel is a permanent magnet and the iron is temporary"],
  ["Both stay magnetised", "Iron stays magnetised and steel does not"], min_points=2,
  pitfalls=[PF(["iron stays magnetised", "both stay magnetised", "steel loses"], "STEEL keeps its magnetism; IRON loses it.")])

Q("w15b_like_poles_field", 3, "15e", "Fig. 1 shows the field between two like poles facing each other. Describe the pattern and explain the point midway between them.",
  [P("the field lines curve away from each other / do not join across the gap", ["curve away", "do not join", "bend away", "repel", "turn away", "spread away"]),
   P("there is a neutral point midway where the fields cancel", ["neutral point", "cancel", "no field", "zero field", "fields cancel"]),
   P("a compass there would not point in any particular direction", ["compass", "not point", "no direction", "any direction"])],
  "The lines from the two like poles curve away from each other and do not join across the gap. Midway between the poles there is a neutral point where the two fields are equal and opposite, so they cancel; a compass placed there would not point in any particular direction.",
  ["Do the lines join across the gap?", "What happens to the fields midway?", "What would a compass do there?"],
  "lines curve away; neutral point where fields cancel",
  ["The lines curve away from each other and there is a neutral point midway where the fields cancel", "a neutral point with no field forms between the like poles, because the lines curve away from each other"],
  ["Straight lines join the two poles", "The field is strongest midway"], min_points=2,
  figure=lambda: sk.two_poles(like=True))

Q("w15b_more_turns", 3, "15b", "Explain why an electromagnet with more turns of wire is stronger, with the same current.",
  [P("each turn produces its own magnetic field", ["each turn", "every turn", "each loop", "all the loops"]),
   P("the fields of the turns add together, giving a stronger field", ["add", "add together", "combine", "add up", "reinforce"])],
  "Each turn of wire carrying the current produces its own magnetic field. With more turns, more of these fields add together, so the overall field of the electromagnet is stronger.",
  ["What does each turn of wire produce?", "What happens when there are more of them?", "Explain."],
  "each turn's field adds → stronger",
  ["Each turn makes its own field, and the fields add together, so more turns give a stronger field", "the fields of all the loops combine"],
  ["More turns reduce the current", "More turns make the wire longer only"], min_points=2)

Q("w15b_lhr_field_left", 3, "15h", "Fig. 1 shows a wire carrying a current out of the page in a magnetic field directed to the left. Use Fleming's left-hand rule to find the direction of the force, and explain.",
  [P("the force is downwards", ["downwards", "down", "downward"]),
   P("first finger left (field), second finger out of the page (current), thumb down", ["first finger", "second finger", "thumb", "left-hand rule", "left hand rule"])],
  "Point the first finger to the left (field) and the second finger out of the page (current). The thumb points downwards, so the force is downwards.",
  ["Point the first finger along the field (to the left).", "Point the second finger out of the page.", "Where does the thumb point?"],
  "force downwards",
  ["The force is downwards: first finger left, second finger out of the page, thumb down", "by the left-hand rule the force is down"],
  ["Upwards", "Out of the page"], min_points=1,
  pitfalls=[PF(["force is upwards", "force is up", "force is out of the page", "upward force"], "Field left, current out of the page: the force is DOWN.")],
  figure=lambda: sk.flemings_lhr(field="left", current="out"))

Q("w15b_wire_jumps", 3, "15g", "A loose wire lies between the poles of a magnet. When a current is switched on, the wire jumps. Explain why.",
  [P("the current produces a magnetic field around the wire", ["field around the wire", "magnetic field around", "current produces a field", "own magnetic field"]),
   P("this field interacts with the magnet's field", ["interacts", "combines", "interaction", "two fields"]),
   P("producing a force on the wire (direction given by Fleming's left-hand rule)", ["force", "left-hand rule", "left hand rule", "pushes the wire"])],
  "The current produces its own magnetic field around the wire. This field interacts with the field of the magnet, producing a force on the wire that makes it jump. Its direction is given by Fleming's left-hand rule.",
  ["What does a current produce around a wire?", "What happens when two fields meet?", "Explain."],
  "wire's field interacts with magnet's field → force",
  ["The current produces a magnetic field that interacts with the magnet's field, giving a force on the wire", "the two fields interact, so there is a force on the wire"],
  ["The wire is attracted because copper is magnetic", "The current makes the wire hot"], min_points=2,
  pitfalls=[PF(["copper is magnetic"], "Copper is NOT magnetic: the force comes from the CURRENT's field.")])

Q("w15b_filings_line_up", 3, "15b", "Explain why iron filings sprinkled around a bar magnet line up along the field lines.",
  [P("each filing becomes an induced (tiny) magnet", ["induced magnet", "tiny magnet", "becomes magnetised", "induced magnetism", "little magnet", "magnetised by induction", "by induction"]),
   P("it turns to line up with the field, like a compass", ["line up with the field", "turns", "like a compass", "aligns", "points along"])],
  "Each iron filing becomes a tiny induced magnet in the field of the bar magnet. Like a small compass needle, it turns to line up along the direction of the field, so the filings trace out the field lines.",
  ["What happens to iron in a magnetic field?", "What does a small magnet do in a field?", "Explain."],
  "each filing becomes induced magnet and aligns with field",
  ["Each filing becomes a tiny induced magnet and lines up with the field like a compass", "the filings are magnetised by induction and turn to point along the field"],
  ["The filings are attracted to the middle", "The filings are charged"], min_points=2)

Q("w15b_solenoid_reverse", 3, "15f", "The current in a solenoid is reversed. Explain what happens to its poles, and how a compass near one end would show this.",
  [P("the poles swap (north becomes south)", ["poles swap", "poles reverse", "north becomes south", "swap", "reversed"]),
   P("because the field direction reverses", ["field reverses", "field direction reverses", "field changes direction"]),
   P("the compass near the end turns round to point the opposite way", ["turns round", "opposite way", "points the other way", "reverses", "swings round"])],
  "Reversing the current reverses the direction of the field, so the poles swap: the north end becomes a south end and vice versa. A compass near one end turns round to point the opposite way.",
  ["What happens to the field direction?", "What does that do to the poles?", "What does the compass do?"],
  "field reverses → poles swap → compass turns round",
  ["The poles swap because the field reverses, so a compass at the end turns round", "north becomes south; the compass needle points the other way"],
  ["The solenoid loses its poles", "The poles stay the same"], min_points=2)

Q("w15b_inside_solenoid", 3, "15f", "Fig. 1 shows the field of a solenoid. Describe the field inside the solenoid and explain how the diagram shows it.",
  [P("strong and uniform", ["uniform", "strong", "same strength"]),
   P("shown by straight, parallel, equally spaced lines", ["parallel", "straight", "equally spaced", "evenly spaced"])],
  "Inside the solenoid the field is strong and uniform, shown by straight, parallel, equally spaced field lines.",
  ["What do the lines inside look like?", "What does equal spacing mean?", "Describe."],
  "strong, uniform: parallel equally spaced lines",
  ["The field inside is strong and uniform, shown by parallel equally spaced lines", "parallel straight lines show a uniform field inside"],
  ["There is no field inside", "Circles around each turn only"], min_points=2,
  figure=lambda: sk.solenoid_field())

Q("w15b_both_ends_attract", 3, "15b", "An iron bar is attracted by both the north pole and the south pole of a magnet. Explain why this shows the bar is not itself a magnet.",
  [P("the iron is magnetised by induction, with the opposite pole induced at the near end", ["induction", "induced", "opposite pole", "unlike pole"]),
   P("so it is always attracted, whichever pole is near", ["always attracted", "whichever pole", "both poles", "either pole"]),
   P("a magnet would be repelled by one of the poles", ["repelled by one", "would repel", "repulsion", "one end would repel"])],
  "The unmagnetised iron bar has magnetism induced in it: whichever pole is brought near, the opposite pole is induced at the near end, so it is always attracted. If the bar were a magnet, one of the poles would repel one of its ends.",
  ["What is induced at the near end of the bar?", "Does that depend on which pole is used?", "What would a real magnet do?"],
  "induced opposite pole → always attracted; magnet would show repulsion",
  ["Magnetism is induced so the near end always becomes the opposite pole and is attracted; a magnet would be repelled by one pole", "it is attracted by both because of induced magnetism, while a magnet would show repulsion"],
  ["It must be a strong magnet", "Iron attracts all poles because it is charged"], min_points=2, pitfalls=[ATTRACT_PROVES])

Q("w15b_compass_points_north", 3, "15d", "Explain why a compass needle points north when no magnet is nearby.",
  [P("the compass needle is a small magnet", ["small magnet", "tiny magnet", "needle is a magnet", "magnetised needle"]),
   P("the Earth has a magnetic field", ["earth's magnetic field", "earth has a magnetic field", "earth's field", "earth is like a magnet"]),
   P("the needle lines up with the Earth's field, its north pole pointing north", ["lines up", "aligns", "points along", "line up"])],
  "The compass needle is a small, freely pivoted magnet. The Earth has its own magnetic field, and the needle turns to line up with it, so that its north-seeking pole points north.",
  ["What is the compass needle?", "What field is always present?", "What does a magnet do in a field?"],
  "needle is a magnet; aligns with Earth's field",
  ["The needle is a small magnet that lines up with the Earth's magnetic field", "the Earth's field makes the magnetised needle align north–south"],
  ["The needle is attracted to the North Pole's ice", "Because north is up"], min_points=2)

# ---------------------------------------------------------------- L4
Q("w15b_identify_three", 4, "15a", "Three identical-looking bars are made of a magnet, unmagnetised iron and aluminium. Describe how to identify each using only another magnet.",
  [P("bring a pole of the magnet to each end of each bar", ["each end", "both ends", "bring a pole", "each bar"]),
   P("the bar that is repelled at one end is the magnet", ["repelled", "repulsion", "repels"]),
   P("the bar attracted at both ends is iron; the one that is not attracted is aluminium", ["attracted at both ends", "both ends attracted", "not attracted", "no effect", "nothing happens"])],
  "Bring one pole of the magnet up to each end of each bar. The bar that is repelled by one of its ends is the magnet. The bar attracted at both ends is the unmagnetised iron. The bar that is not attracted at all is the aluminium.",
  ["What effect proves a bar is a magnet?", "What does iron show?", "What does aluminium show?"],
  "repelled → magnet; attracted both ends → iron; no effect → aluminium",
  ["Test each end: the one repelled is the magnet, the one attracted at both ends is iron, and the one not attracted is aluminium", "repulsion shows the magnet, attraction only shows iron, nothing happens with aluminium"],
  ["The heaviest bar is the magnet", "All three are attracted"], min_points=2, pitfalls=[ALUMINIUM_MAGNETIC])

Q("w15b_cut_magnet", 4, "15a", "A student predicts that cutting a bar magnet in half gives a separate north pole and south pole. Explain what actually happens.",
  [P("each half becomes a complete magnet", ["complete magnet", "two magnets", "each half is a magnet", "two smaller magnets", "new magnets"]),
   P("with its own north and south pole", ["north and south", "both poles", "own north", "two poles", "n and s"]),
   P("so a single isolated pole cannot be made", ["cannot", "never", "isolated pole", "not possible", "always two poles"])],
  "Each half becomes a complete, smaller magnet with its own north pole and south pole. However many times a magnet is cut, each piece has two poles; a single isolated pole cannot be produced.",
  ["Does a piece of magnet ever have only one pole?", "What does each half become?", "Explain."],
  "each half is a magnet with N and S",
  ["Each half becomes a complete magnet with its own north and south pole", "you get two smaller magnets, each with both poles; you cannot get a single pole"],
  ["You get a north half and a south half", "The halves are no longer magnetic"], min_points=2,
  pitfalls=[PF(["north half and a south half", "separate north pole", "single north pole"], "Every piece of magnet has BOTH a north and a south pole.")])

Q("w15b_electromagnet_uses", 4, "15b", "Explain why an electromagnet, rather than a permanent magnet, is used in an electric door lock.",
  [P("an electromagnet can be switched on and off", ["switched on and off", "switched off", "turned off", "on and off"]),
   P("so the lock can be released (opened) by switching off the current", ["released", "unlock", "opened", "release"]),
   P("its strength can be controlled by changing the current", ["strength can be controlled", "change the current", "adjust", "vary the strength", "controlled"])],
  "An electromagnet can be switched on and off. With the current on it holds the lock closed; switching off the current releases the lock. Its strength can also be controlled by changing the current. A permanent magnet cannot be switched off.",
  ["Can a permanent magnet be switched off?", "How is the lock opened?", "What else can you control?"],
  "switch on/off; release by switching off; adjustable strength",
  ["An electromagnet can be switched on and off, so the lock can be released by switching off the current", "it can be turned off to open the lock and its strength can be controlled"],
  ["Electromagnets are permanent", "Permanent magnets are too weak"], min_points=2)

Q("w15b_reverse_both", 4, "15g", "A wire carrying a current out of the page in a field to the right feels a force upwards (Fig. 1). Explain what happens to the force if both the current and the field are reversed.",
  [P("the force is still upwards (unchanged)", ["still upwards", "still up", "unchanged", "stays the same", "same direction"]),
   P("reversing one reverses the force, reversing the other reverses it back", ["reverses it back", "two reversals cancel", "cancel", "reversed twice", "each reversal"]),
   P("check: field left, current into the page gives force up (left-hand rule)", ["left-hand rule", "left hand rule", "field left", "into the page"])],
  "The force is still upwards. Reversing the current alone would reverse the force; reversing the field as well reverses it back, so the two reversals cancel. Check with the left-hand rule: field to the left and current into the page gives a force upwards.",
  ["What does reversing only the current do?", "What does reversing the field do then?", "Check with the left-hand rule."],
  "two reversals cancel → still upwards",
  ["It is still upwards, because reversing both cancels out", "the force stays up: each reversal flips it, so two reversals bring it back"],
  ["It becomes downwards", "It becomes zero"], min_points=1,
  pitfalls=[PF(["becomes downwards", "force is now downwards", "becomes zero"], "Reversing BOTH current and field leaves the force UNCHANGED.")],
  figure=lambda: sk.flemings_lhr(field="right", current="out", force="up"))

Q("w15b_motor_more_turns", 4, "15i", "Fig. 1 shows a coil in a magnetic field. Explain why adding more turns to the coil increases its turning effect.",
  [P("each turn has sides carrying current at right angles to the field, so each experiences forces", ["each turn", "every turn", "each side", "each wire"]),
   P("the forces on the two sides are in opposite directions, producing a turning effect", ["opposite directions", "turning effect", "moment", "couple", "rotate"]),
   P("more turns give more forces, so a larger total turning effect", ["more forces", "larger turning effect", "add up", "larger total", "bigger turning effect"])],
  "Each turn of the coil has two sides carrying current in opposite directions across the field, so they feel forces in opposite directions, producing a turning effect. With more turns, more of these forces act and add up, giving a larger total turning effect.",
  ["What force acts on each side of one turn?", "Why do the forces cause turning?", "What do more turns do?"],
  "each turn adds opposite forces → larger turning effect",
  ["Each turn has forces in opposite directions on its sides, so more turns give more forces and a larger turning effect", "the forces on every turn add up, increasing the turning effect"],
  ["More turns make the coil heavier so it turns slower", "More turns reduce the field"], min_points=2,
  figure=lambda: sk.coil_in_field())

Q("w15b_compass_both_ends", 4, "15f", "Compasses are placed at the two ends of a current-carrying solenoid. Explain why their north poles point in opposite directions relative to the solenoid.",
  [P("one end of the solenoid is a north pole and the other a south pole", ["one end north", "north and south", "one end is a north pole", "poles"]),
   P("a compass's north end is repelled by the solenoid's north pole and attracted to its south pole", ["repelled", "attracted", "like poles repel", "unlike poles attract"]),
   P("so at one end it points away from the solenoid, at the other end towards it", ["away", "towards", "opposite"])],
  "The two ends of the solenoid act as a north pole and a south pole. The north end of a compass is repelled by the solenoid's north pole and attracted to its south pole. So at the north end the compass needle points away from the solenoid, and at the south end it points towards it.",
  ["What are the ends of a solenoid like?", "How does the compass's N end respond to each pole?", "Explain."],
  "ends are N and S; compass N repelled by N, attracted by S",
  ["One end is north and the other south, so the compass points away at the north end and towards the solenoid at the south end", "the compass north pole is repelled by one end and attracted by the other"],
  ["The compasses are faulty", "The current flows only at one end"], min_points=2)

Q("w15b_wire_field_distance", 4, "15f", "Fig. 1 shows the field around a straight wire. Explain how the strength of the field changes with distance from the wire, and how the diagram shows it.",
  [P("the field is weaker further from the wire", ["weaker further", "weaker", "decreases with distance", "gets weaker"]),
   P("shown by the circles being further apart", ["further apart", "spacing increases", "spread out", "wider apart"]),
   P("strongest close to the wire where circles are closest", ["strongest close", "closest", "near the wire", "stronger near"])],
  "The field is strongest close to the wire and gets weaker further away. The diagram shows this because the circles are closest together near the wire and further apart as the distance increases.",
  ["Where are the circles closest?", "What does wider spacing mean?", "Explain."],
  "weaker with distance: circles further apart",
  ["The field gets weaker further from the wire, shown by the circles getting further apart", "strongest near the wire, where the lines are closest, and weaker further away"],
  ["The field is the same everywhere", "The field gets stronger further away"], min_points=2,
  figure=lambda: sk.straight_wire_field(False))

Q("w15b_force_vs_current_expt", 4, "15g", "Describe an experiment to show that the force on a current-carrying wire in a magnetic field increases with the current.",
  [P("place a magnet (pair of magnets on a yoke) on a top-pan balance with a fixed wire passing between the poles", ["balance", "top-pan balance", "between the poles", "magnet on a balance"]),
   P("vary the current with a variable resistor and measure it with an ammeter", ["variable resistor", "ammeter", "vary the current", "change the current"]),
   P("the change in balance reading shows the force; it increases as the current increases", ["change in reading", "balance reading", "increases", "reading changes"])],
  "Put a magnet (two magnets on a steel yoke) on a top-pan balance, with a fixed horizontal wire clamped between the poles. Pass a current through the wire, varied with a variable resistor and measured with an ammeter. The change in the balance reading measures the force on the wire; it increases as the current increases.",
  ["How can you measure a small force?", "How do you vary and measure the current?", "What shows the result?"],
  "magnet on balance, wire between poles; vary I; balance change increases",
  ["Put the magnet on a balance with a wire between the poles, vary the current with a variable resistor and see the balance reading change more with larger current", "measure the change in balance reading for different ammeter readings"],
  ["Weigh the wire before and after", "Use a compass to measure the force"], min_points=2)

Q("w15b_fridge_door", 4, "15b", "A fridge door seal contains a flexible magnetic strip, and the fridge frame is made of steel. Explain how the door is held shut.",
  [P("the magnet induces magnetism in the steel frame", ["induces", "induced", "magnetises the steel", "induced magnetism"]),
   P("the induced pole nearest the magnet is opposite, so the strip is attracted to the frame", ["opposite pole", "attracted", "unlike poles", "attraction"]),
   P("steel is a magnetic material (unlike aluminium or plastic)", ["steel is magnetic", "magnetic material", "steel"])],
  "Steel is a magnetic material. The magnetic strip induces magnetism in the steel frame, with an opposite pole on the part nearest the strip, so the strip is attracted to the frame and holds the door shut.",
  ["Is steel a magnetic material?", "What happens to steel near a magnet?", "Why is there attraction?"],
  "induced magnetism in steel → attraction",
  ["The magnetic strip induces magnetism in the steel frame, so they attract and hold the door shut", "steel is magnetic, so induced opposite poles attract the strip"],
  ["The door is held by static charge", "Air pressure only"], min_points=2)

Q("w15b_lhr_find_current", 4, "15h", "A wire lies in a magnetic field directed to the right, and the force on it is downwards. Use Fleming's left-hand rule to deduce the direction of the current.",
  [P("the current is into the page", ["into the page", "into page"]),
   P("first finger right (field), thumb down (force): the second finger points into the page", ["first finger", "thumb", "second finger", "left-hand rule", "left hand rule"])],
  "Point the first finger to the right (field) and turn the hand so that the thumb points down (force). The second finger then points into the page, so the current is into the page.",
  ["Set the first finger along the field.", "Set the thumb along the force.", "Which way does the second finger point?"],
  "current into the page",
  ["Into the page: first finger right, thumb down, second finger into the page", "the current flows into the page"],
  ["Out of the page", "To the right"], min_points=1,
  pitfalls=[PF(["out of the page", "current is to the right", "current is to the left"], "Field right, force down: the current is INTO the page.")])

# ---------------------------------------------------------------- L5
Q("w15b_claim_iron_compass", 5, "15c", "A student says: 'Iron is the best material for a compass needle because it is very easy to magnetise.' Evaluate this.",
  [P("wrong: iron is easy to magnetise but also easily loses its magnetism (temporary)", ["wrong", "loses its magnetism", "easily demagnetised", "temporary", "does not keep"]),
   P("a compass needle must stay magnetised permanently", ["stay magnetised", "permanent", "keep its magnetism", "permanently"]),
   P("so steel, a hard magnetic material, is used", ["steel", "hard magnetic"])],
  "The statement is wrong. Iron is easy to magnetise, but it is also easily demagnetised, so it only makes a temporary magnet. A compass needle must stay magnetised permanently, so steel, a hard magnetic material that keeps its magnetism, is used.",
  ["Does iron keep its magnetism?", "What must a compass needle do?", "Which material is used?"],
  "wrong; iron temporary; needle must be permanent → steel",
  ["Wrong: iron loses its magnetism easily, so a compass needle is made of steel, which stays magnetised", "the needle must be a permanent magnet, so steel is used, not iron"],
  ["Correct, iron is used for compasses", "Correct, copper is even better"], min_points=2)

Q("w15b_claim_bigger_stronger", 5, "15a", "A student says: 'A bigger magnet is always stronger than a smaller one.' Evaluate this claim and suggest a fair test.",
  [P("not necessarily: strength depends on the material and how strongly it is magnetised, not just size", ["not necessarily", "depends on the material", "material", "not just size", "wrong"]),
   P("fair test: count how many paper clips (or how far away a compass is deflected) each magnet holds", ["paper clips", "count", "compass", "how far", "number of clips"]),
   P("keep other factors the same (same clips, same pole, same distance)", ["same clips", "same pole", "same distance", "fair test", "keep the same"])],
  "The claim is not necessarily true: a magnet's strength depends on its material and how strongly it is magnetised, not just its size; a small neodymium magnet can be far stronger than a large ferrite one. A fair test is to count how many identical paper clips each magnet can hold in a chain from the same pole (or how far away each deflects a compass), keeping everything else the same.",
  ["Does size alone decide strength?", "How could you measure strength?", "How do you keep the test fair?"],
  "not necessarily; test with paper clips/compass, keep other factors same",
  ["Not necessarily: it depends on the material; count how many identical paper clips each holds from the same pole", "size alone does not decide strength; compare with a fair paper-clip test"],
  ["Correct, size decides strength", "Correct, heavier magnets are stronger"], min_points=2)

Q("w15b_claim_attraction_magnet", 5, "15a", "A student says: 'Rod X attracted the north pole of my magnet, so rod X must be a magnet.' Evaluate this conclusion.",
  [P("not valid: an unmagnetised magnetic material (e.g. iron) is also attracted", ["not valid", "wrong", "iron is also attracted", "unmagnetised", "magnetic material", "could be iron"]),
   P("because magnetism is induced in it", ["induced", "induction"]),
   P("test for repulsion with both ends: repulsion proves it is a magnet", ["repulsion", "repel", "test both ends", "other end"])],
  "The conclusion is not valid. An unmagnetised magnetic material such as iron would also be attracted, because magnetism is induced in it. To prove rod X is a magnet, test both its ends with the same pole: if one end is repelled, X is a magnet.",
  ["Would iron also be attracted?", "Why?", "What test would prove it?"],
  "not valid; iron also attracted (induction); test for repulsion",
  ["Not valid: iron would also be attracted by induction, so test for repulsion", "it could be unmagnetised iron; only repulsion proves a magnet"],
  ["Correct, attraction proves it is a magnet", "Correct, only magnets are attracted"], min_points=2, pitfalls=[ATTRACT_PROVES])

Q("w15b_design_turns", 5, "15b", "Design an investigation to find how the number of turns on an electromagnet affects its strength.",
  [P("independent variable: the number of turns (e.g. 10, 20, 30...)", ["number of turns", "different numbers of turns", "vary the turns", "change the turns"]),
   P("keep the current (ammeter + variable resistor) and the core the same", ["same current", "constant current", "keep the current", "same core", "variable resistor", "ammeter"]),
   P("measure strength by the number of paper clips picked up; repeat and average", ["paper clips", "number of clips", "repeat", "average"])],
  "Wind an electromagnet with 10 turns on an iron nail and connect it to a power supply with an ammeter and variable resistor. Count how many identical paper clips it picks up. Repeat for 20, 30, 40 turns, adjusting the variable resistor to keep the current the same and using the same nail. Repeat each reading and average, then plot the number of clips against the number of turns.",
  ["What do you change?", "What must stay the same, and how?", "What do you measure?"],
  "vary turns; constant current and core; count clips; repeat",
  ["Change the number of turns, keep the current and the core the same, and count how many paper clips it picks up; repeat and average", "vary the turns and measure strength with paper clips at constant current"],
  ["Change the current and the turns together", "Use different nails each time"], min_points=2)

Q("w15b_claim_always_force", 5, "15g", "A student says: 'Any wire in a magnetic field always feels a force.' Evaluate this claim.",
  [P("wrong: there must be a current in the wire", ["wrong", "must be a current", "needs a current", "no current no force", "current must flow"]),
   P("and the current must not be parallel to the field (largest at right angles)", ["parallel", "right angles", "perpendicular", "angle"]),
   P("a force arises from the interaction of the current's field with the magnet's field", ["interaction", "current's field", "field of the current", "interacts"])],
  "The claim is wrong. A force only acts if a current flows in the wire, because the force comes from the interaction of the current's own magnetic field with the magnet's field. Even then, there is no force if the current is parallel to the field; the force is largest when the current is at right angles to it.",
  ["Is there a force with no current?", "What if the current is parallel to the field?", "Evaluate."],
  "wrong; needs current; none if parallel to field",
  ["Wrong: it needs a current, and there is no force if the current is parallel to the field", "only a current-carrying wire at an angle to the field feels a force"],
  ["Correct, all wires feel a force", "Correct, copper is magnetic"], min_points=2)

Q("w15b_claim_reverse_both_reverses", 5, "15g", "A student says: 'To reverse a motor, reverse both the current and the magnetic field, to make sure.' Evaluate this advice.",
  [P("wrong: reversing both leaves the force (rotation) unchanged", ["wrong", "unchanged", "same direction", "cancel", "no change"]),
   P("reversing either the current or the field alone reverses the force", ["either", "only one", "one of them", "alone", "just the current", "only the current", "only the field"]),
   P("so reverse just one of them", ["just one", "only one", "one of them", "reverse only"])],
  "The advice is wrong. Reversing the current reverses the force, and reversing the field reverses it again, so reversing both leaves the motor turning the same way. To reverse the motor, reverse only one of them: either the current or the field.",
  ["What does reversing the current alone do?", "What does reversing the field as well do?", "What should be done?"],
  "wrong; both → unchanged; reverse only one",
  ["Wrong: reversing both cancels out, so reverse only the current or only the field", "the motor would turn the same way; reverse just one of them"],
  ["Correct, it reverses twice as well", "Correct, it stops the motor"], min_points=2)

Q("w15b_weak_compass_deflection", 5, "15f", "A compass placed near a wire carrying a small current hardly moves. Evaluate two improvements to make the effect clearer.",
  [P("increase the current, to make the field stronger", ["increase the current", "larger current", "more current"]),
   P("place the compass closer to the wire, where the field is stronger", ["closer", "nearer", "move the compass closer"]),
   P("align the wire north–south so the wire's field is at right angles to Earth's field (or switch on/off to see the change)", ["north-south", "north south", "at right angles to the earth", "switch on and off", "earth's field"])],
  "Increase the current, which makes the wire's field stronger, and place the compass closer to the wire, where the field is stronger. It also helps to lay the wire north–south, so that the wire's field is at right angles to the Earth's field and turns the needle more, and to switch the current on and off to see the change clearly.",
  ["How can you make the wire's field stronger?", "Where is the field strongest?", "How does the Earth's field affect the compass?"],
  "larger current; compass closer; wire N–S",
  ["Increase the current and move the compass closer to the wire", "use a larger current, put the compass nearer and align the wire north–south"],
  ["Use a smaller current", "Move the compass further away"], min_points=2)

Q("w15b_claim_lines_real", 5, "15e", "A student says: 'Iron filings prove that magnetic field lines are real lines in space.' Evaluate this.",
  [P("wrong: field lines are a model used to show the direction and strength of the field", ["wrong", "model", "imaginary", "not real", "way of representing"]),
   P("the filings form a pattern because each becomes an induced magnet and lines up with the field", ["induced magnet", "line up", "aligns", "pattern"]),
   P("the field exists everywhere around the magnet, not only along separate lines", ["everywhere", "continuous", "between the lines", "all around"])],
  "The statement is wrong. Field lines are a model used to show the direction and strength of a magnetic field. The filings form a pattern because each becomes an induced magnet and lines up with the field; the gaps between them do not mean there is no field. The field exists everywhere around the magnet, not only along separate lines.",
  ["Are field lines real objects?", "Why do the filings line up?", "Is there field between the lines?"],
  "wrong; lines are a model; filings align by induction; field everywhere",
  ["Wrong: field lines are only a model; the filings line up because each becomes an induced magnet, and the field exists everywhere", "field lines are imaginary; the filings just align with the field"],
  ["Correct, the lines are made of iron", "Correct, the field is only along the lines"], min_points=2)

Q("w15b_motor_wont_start", 5, "15i", "A student's simple motor does not turn at all when switched on. Evaluate three possible causes.",
  [P("no current: a loose connection or flat battery", ["no current", "loose connection", "flat battery", "broken wire", "circuit incomplete", "check the connections", "connections"]),
   P("the magnetic field or current is too weak to overcome friction", ["too weak", "friction", "weak magnet", "small current", "stronger magnet"]),
   P("the coil started in a position with no turning effect (forces in line, e.g. coil plane perpendicular to the field); give it a push", ["no turning effect", "perpendicular to the field", "give it a push", "forces in line", "dead spot", "push"])],
  "Possible causes: there is no current because of a loose connection or flat battery; the field or current is too weak to overcome friction in the bearings; or the coil started in the position where the forces on its sides act along the same line, giving no turning effect, so it needs a small push to start.",
  ["Is current flowing?", "Is the turning effect enough to overcome friction?", "Could the coil's starting position matter?"],
  "no current; too weak vs friction; starting position with no turning effect",
  ["There may be no current from a loose connection, the magnet may be too weak to overcome friction, or the coil may be in a position with no turning effect", "check the connections, use a stronger magnet, and give the coil a push"],
  ["The coil is made of copper", "The motor is too light"], min_points=2)

Q("w15b_claim_cans", 5, "15c", "A student says: 'A magnet can separate aluminium cans from steel cans at a recycling centre because it picks up the aluminium ones.' Evaluate this.",
  [P("wrong: aluminium is not magnetic", ["wrong", "aluminium is not magnetic", "aluminium is non-magnetic", "not attracted"]),
   P("the magnet attracts the steel cans (steel is magnetic)", ["steel cans", "attracts the steel", "steel is magnetic", "picks up the steel"]),
   P("so the steel is removed and the aluminium is left behind; an electromagnet can then release the steel", ["left behind", "separated", "electromagnet", "release", "switch off"])],
  "The idea of separating them with a magnet is right, but the reasoning is wrong. Aluminium is not magnetic, so the magnet picks up the steel cans instead, leaving the aluminium behind. An electromagnet is used so that the steel cans can be released by switching off the current.",
  ["Is aluminium magnetic?", "Which cans does the magnet pick up?", "How can the steel be released?"],
  "wrong; steel picked up, aluminium left; electromagnet releases",
  ["Wrong: aluminium is not magnetic, so the magnet picks up the steel cans and leaves the aluminium", "the magnet attracts steel, not aluminium, which is left behind"],
  ["Correct, magnets attract aluminium", "Correct, all metal cans are magnetic"], min_points=2, pitfalls=[ALUMINIUM_MAGNETIC])
