"""Chapter 5 Turning Effects of Forces: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 5


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


FORCES_EQUAL = PF(["forces must be equal", "weights must be equal", "equal weights balance", "the forces are equal on each side"],
                  "Balance needs equal MOMENTS (force × distance), not equal forces.")

# ---------------------------------------------------------------- L1
Q("w5b_pivot_def", 1, "5a", "State what is meant by the pivot of a lever, giving an example.",
  [P("the fixed point about which the lever turns (the fulcrum)", ["point about which", "turns about", "point it turns", "fixed point", "fulcrum", "point of rotation", "rotates about"]),
   P("example: the hinge of a door, the middle of a see-saw, the nut for a spanner", ["hinge", "see-saw", "seesaw", "nut", "middle of", "axle", "wheel"])],
  "The pivot is the fixed point about which a lever turns (also called the fulcrum). For example, the hinge is the pivot of a door, and the support at the middle is the pivot of a see-saw.",
  ["What does a lever rotate about?", "Think of a door or a see-saw.", "Define it and give an example."],
  "point about which a lever turns; e.g. door hinge",
  ["The point about which the lever turns, such as the hinge of a door", "the fulcrum, the fixed point it rotates about, like the middle of a see-saw"],
  ["The end of the lever where you push", "The heaviest part of the lever"], min_points=2)

Q("w5b_turning_examples", 1, "5a", "Give two everyday examples of the turning effect of a force.",
  [P("first example (door, spanner, see-saw, tap, steering wheel, scissors, bottle opener, wheelbarrow)", ["door", "spanner", "see-saw", "seesaw", "tap", "steering wheel", "scissors", "bottle opener", "wheelbarrow", "crowbar", "screwdriver", "handle"]),
   P("a force applied at a distance from a pivot makes the object turn", ["turn", "rotate", "pivot", "about a hinge", "turning"])],
  "Pushing a door open about its hinges and turning a nut with a spanner are both examples of the turning effect (moment) of a force: a force applied at a distance from a pivot makes the object rotate.",
  ["Think of things that rotate when you push or pull them.", "Each has a pivot.", "Name two."],
  "e.g. door, spanner, see-saw, tap",
  ["Opening a door and turning a nut with a spanner", "a see-saw tipping and a tap being turned"],
  ["A ball rolling down a hill", "A car moving in a straight line"], min_points=1)

Q("w5b_clockwise_meaning", 1, "5c", "Fig. 1 shows forces on a beam. State what is meant by a clockwise moment and an anticlockwise moment.",
  [P("a clockwise moment tends to turn the body the same way as the hands of a clock", ["same way as the hands", "same direction as a clock", "like a clock", "clockwise turns"]),
   P("an anticlockwise moment tends to turn it the opposite way", ["opposite way", "opposite direction", "other way", "against the clock"])],
  "A clockwise moment is the turning effect of a force that tends to rotate a body in the same direction as the hands of a clock. An anticlockwise moment tends to rotate it in the opposite direction.",
  ["Moments have a direction of turning.", "Compare with the hands of a clock.", "Define both."],
  "clockwise = same way as clock hands; anticlockwise = opposite",
  ["A clockwise moment turns it the same way as the hands of a clock; anticlockwise turns it the opposite way", "clockwise is like a clock, anticlockwise is the other way"],
  ["Clockwise means the force is larger", "Anticlockwise means the force is upwards"], min_points=2,
  figure=lambda: sketches.beam(4, 2, [("F₁", 1, "down"), ("F₂", 3.4, "down")]))

Q("w5b_moment_formula", 1, "5b", "Write down the formula for the moment of a force, stating the meaning and unit of each quantity.",
  [P("moment = force × perpendicular distance from the pivot", ["force × perpendicular distance", "force × distance", "force times distance", "f × d", "force multiplied by"]),
   P("units: moment in N m, force in N, distance in m", ["n m", "newton metre", "nm"])],
  "Moment = force × perpendicular distance from the pivot. The force is in newtons (N), the distance in metres (m), and the moment in newton metres (N m).",
  ["Two quantities determine the turning effect.", "Which operation combines them?", "Give the units."],
  "moment = F × d; N m",
  ["Moment = force × perpendicular distance from the pivot, in N m", "F × d, with force in newtons and distance in metres, giving newton metres"],
  ["Moment = force ÷ distance", "Moment = mass × distance"], min_points=1,
  pitfalls=[PF(["force ÷ distance", "force / distance", "force divided by distance"], "Moment = force × distance.")])

Q("w5b_equilibrium_conditions", 1, "5c", "State the two conditions for a body to be in equilibrium.",
  [P("the resultant force on it is zero", ["resultant force is zero", "no resultant force", "zero resultant force", "forces balance", "balanced forces"]),
   P("the resultant moment about any point is zero (clockwise = anticlockwise)", ["resultant moment is zero", "no resultant moment", "moments balance", "clockwise moments equal", "sum of clockwise", "clockwise = anticlockwise"])],
  "For a body to be in equilibrium, the resultant force on it must be zero, and the resultant moment about any point must be zero, i.e. the sum of clockwise moments equals the sum of anticlockwise moments.",
  ["Equilibrium means no change in motion and no turning.", "One condition is about forces, the other about moments.", "State both."],
  "zero resultant force; zero resultant moment",
  ["The resultant force is zero and the resultant moment is zero", "the forces balance and the clockwise moments equal the anticlockwise moments"],
  ["It must be at rest and touching the ground", "All the forces must be zero"], min_points=2)

Q("w5b_cg_uniform_rod", 1, "5e", "State where the centre of gravity of a uniform rod is, and explain why.",
  [P("at its centre (midpoint)", ["centre", "middle", "midpoint", "halfway"]),
   P("because its mass is spread evenly along its length", ["spread evenly", "evenly distributed", "uniform", "same mass on each side", "symmetrical"])],
  "The centre of gravity of a uniform rod is at its midpoint, because its mass is spread evenly along its length, so its weight acts at the centre.",
  ["What does 'uniform' mean?", "Where would the weight act for a symmetrical mass distribution?", "State and explain."],
  "midpoint; mass evenly spread",
  ["At the middle, because the mass is spread evenly", "its midpoint, since the rod is uniform"],
  ["At one end", "Wherever it is held"], min_points=2)

Q("w5b_stability_factors", 1, "5e", "State two features that make an object stable.",
  [P("a low centre of gravity", ["low centre of gravity", "centre of gravity is low", "lower centre of gravity", "low cg", "heavy base", "weight low down"]),
   P("a wide base", ["wide base", "broad base", "large base", "wider base"])],
  "An object is more stable if it has a low centre of gravity and a wide base.",
  ["Think of a racing car or a traffic cone.", "Where is their weight concentrated?", "What is their base like?"],
  "low centre of gravity; wide base",
  ["A low centre of gravity and a wide base", "having its weight low down and a broad base"],
  ["A high centre of gravity and a narrow base", "Being tall"], min_points=2,
  pitfalls=[PF(["high centre of gravity", "narrow base"], "A high centre of gravity or a narrow base makes an object LESS stable.")])

Q("w5b_force_through_pivot", 1, "5b", "State the moment of a force whose line of action passes through the pivot, and explain.",
  [P("the moment is zero", ["zero", "no moment", "no turning effect", "nothing"]),
   P("because the perpendicular distance from the pivot is zero", ["distance is zero", "zero distance", "perpendicular distance is zero", "passes through the pivot"])],
  "Its moment is zero, because the perpendicular distance from the pivot to the line of action of the force is zero, and moment = force × distance.",
  ["Moment = force × perpendicular distance.", "How far is the line of action from the pivot?", "Multiply."],
  "zero moment; zero distance",
  ["Zero, because the perpendicular distance is zero", "there is no turning effect since the distance from the pivot is zero"],
  ["It is very large", "It equals the force"], min_points=2)

Q("w5b_increase_moment", 1, "5b", "State two ways of increasing the moment of a force about a pivot.",
  [P("increase the size of the force", ["larger force", "bigger force", "increase the force", "more force", "push harder"]),
   P("increase the perpendicular distance from the pivot", ["increase the distance", "further from the pivot", "longer distance", "larger distance", "greater distance", "greater perpendicular distance", "longer handle", "longer lever"])],
  "The moment can be increased by applying a larger force, or by applying the force at a greater perpendicular distance from the pivot.",
  ["Moment = force × distance.", "Which factors can you increase?", "State both."],
  "larger force; larger distance",
  ["Use a larger force, or apply it further from the pivot", "push harder or use a longer handle"],
  ["Make the object lighter", "Move the force closer to the pivot"], min_points=2,
  pitfalls=[PF(["closer to the pivot", "nearer the pivot"], "Moving the force closer to the pivot DECREASES the moment.")])

Q("w5b_cg_outside", 1, "5e", "Explain how the centre of gravity of a ring can be at a point where there is no material.",
  [P("the centre of gravity is the point where the whole weight can be taken to act", ["whole weight", "weight acts", "where the weight", "point where the weight"]),
   P("for a ring it is at the centre of the hole, by symmetry, outside the material", ["centre of the ring", "middle of the hole", "in the hole", "outside the material", "symmetry", "empty space"])],
  "The centre of gravity is the point where the whole weight of a body can be taken to act. For a ring, by symmetry, this point is at the centre of the ring, which is in the empty hole, so it is not within the material.",
  ["Define centre of gravity.", "Where is the 'average position' of a ring's mass?", "Is there material there?"],
  "point where weight acts; at the centre of the hole",
  ["The centre of gravity is where the whole weight acts; for a ring it is at the centre of the hole by symmetry", "it is at the middle of the ring, in the empty space"],
  ["The centre of gravity is always inside the object", "A ring has no centre of gravity"], min_points=1,
  pitfalls=[PF(["always inside the object", "no centre of gravity"], "The centre of gravity can lie outside the material, as for a ring.")])

# ---------------------------------------------------------------- L2
Q("w5b_scissors_near_pivot", 2, "5a", "Explain why thick card is easier to cut near the pivot of a pair of scissors than near the tips.",
  [P("near the pivot the card is closer to the pivot than your hand is", ["closer to the pivot", "near the pivot", "small distance", "short distance"]),
   P("so the same moment from your hand produces a larger force on the card", ["larger force", "bigger force", "greater force", "more force on the card"])],
  "Your hand applies a moment about the pivot. Near the pivot, the card is a small distance from the pivot, so the same moment produces a much larger force on the card (moment = force × distance), which cuts it more easily.",
  ["Your hands provide a moment about the pivot.", "The blades exert a force on the card at some distance from the pivot.", "For a fixed moment, what happens to the force when the distance is smaller?"],
  "same moment, smaller distance → larger cutting force",
  ["Near the pivot the distance is small, so the same moment gives a larger force on the card", "the card is closer to the pivot, so a bigger force acts on it"],
  ["The blades are sharper near the pivot", "There is more friction at the tips"], min_points=2)

Q("w5b_lever_tap", 2, "5a", "Taps in homes for the elderly often have long lever handles. Explain why.",
  [P("a long handle means the force is applied far from the pivot (axis of the tap)", ["long handle", "far from the pivot", "large distance", "greater distance", "further from the axis"]),
   P("so a small force gives a large enough moment to turn the tap", ["small force", "less force", "large moment", "bigger moment", "easier to turn"])],
  "A long lever handle lets the force be applied a large distance from the tap's axis (pivot). Since moment = force × distance, a small force from a weak hand gives a large enough moment to turn the tap.",
  ["Where is the pivot of a tap?", "What does a long handle change?", "Use moment = F × d."],
  "large distance → small force gives large moment",
  ["The long handle gives a large distance from the pivot, so a small force produces a big enough moment", "a greater distance means less force is needed to turn it"],
  ["Long handles are prettier", "Long handles reduce friction"], min_points=2)

Q("w5b_equal_children", 2, "5d", "Fig. 1 shows a see-saw pivoted at its centre. Two children of equal weight want to balance it. Where should they sit, and why?",
  [P("at equal distances from the pivot, on opposite sides", ["equal distances", "same distance", "same distance from the pivot", "equal distance"]),
   P("so their moments are equal and opposite (W × d the same)", ["moments are equal", "equal moments", "clockwise equals anticlockwise", "moments balance", "same moment"])],
  "They should sit on opposite sides at equal distances from the pivot. With equal weights and equal distances, their moments are equal and opposite, so the see-saw balances.",
  ["Their weights are equal.", "What else must be equal for their moments to be equal?", "Explain."],
  "equal distances; equal moments",
  ["At equal distances on opposite sides, so their moments are equal", "the same distance from the pivot, giving equal clockwise and anticlockwise moments"],
  ["Both on the same side", "One at the pivot"], min_points=2,
  figure=lambda: sketches.beam(4, 2, [("W", 0.6, "down"), ("W", 3.4, "down")]))

Q("w5b_push_near_hinge", 2, "5a", "Explain why it is hard to open a door by pushing near its hinge.",
  [P("near the hinge the perpendicular distance from the pivot is small", ["small distance", "close to the hinge", "close to the pivot", "short distance", "near the pivot", "distance is small", "small moment"]),
   P("so a much larger force is needed to produce the same moment", ["larger force", "more force", "bigger force", "same moment needs", "push harder", "push much harder"])],
  "Near the hinge, the perpendicular distance from the pivot is small. Since moment = force × distance, a much larger force is needed to produce the moment required to open the door.",
  ["Where is the pivot of a door?", "How far from it are you pushing?", "Use moment = F × d."],
  "small distance → larger force for same moment",
  ["The distance from the hinge is small so a larger force is needed for the same moment", "pushing close to the pivot gives a small moment unless you push much harder"],
  ["The door is heavier near the hinge", "There is more friction near the hinge"], min_points=2)

Q("w5b_bottle_opener", 2, "5a", "Explain how a bottle opener makes it easy to remove a tight bottle cap.",
  [P("the bottle opener is a lever: the effort is applied at the end of a long handle, far from the pivot", ["lever", "long handle", "far from the pivot", "large distance"]),
   P("the cap is a short distance from the pivot, so a small effort produces a large force on the cap", ["short distance", "small effort", "large force", "bigger force", "close to the pivot"])],
  "The bottle opener is a lever. The effort is applied at the end of a long handle, far from the pivot, while the cap is a short distance from the pivot. The moments balance, so a small effort produces a large force on the cap.",
  ["Where is the pivot?", "Compare the distances of the effort and the cap from the pivot.", "Use the principle of moments."],
  "lever; effort far, load near → small effort, large force",
  ["It is a lever: a small effort far from the pivot produces a large force on the cap close to the pivot", "the long handle gives a large distance, so a small push makes a big force on the cap"],
  ["The opener is magnetic", "It heats the cap"], min_points=2)

Q("w5b_bend_forward_hips", 2, "5e", "When you bend forward to touch your toes, your hips move backwards. Explain why this keeps you from falling over.",
  [P("bending forward moves your centre of gravity forward", ["centre of gravity moves forward", "cg moves forward", "shifts your centre of gravity"]),
   P("moving the hips back keeps the centre of gravity above your feet (your base)", ["above your feet", "over your feet", "above the feet", "over the feet", "within your base", "above the base", "over the base"]),
   P("if the line of action of your weight fell outside your feet, you would topple", ["outside", "topple", "fall over", "tip over"])],
  "Bending forward moves your centre of gravity forward. By moving your hips backwards, your body keeps its centre of gravity above your feet, which form your base. If the line of action of your weight fell outside your feet, its moment would make you topple.",
  ["What happens to your centre of gravity when you lean forward?", "Where must it be for you to stay balanced?", "How do your hips help?"],
  "keep centre of gravity above the feet",
  ["Moving the hips back keeps the centre of gravity above the feet; otherwise you would topple", "bending moves the cg forward, so the hips go back to keep it over the base"],
  ["Your hips make you lighter", "It stretches your muscles"], min_points=2)

Q("w5b_balance_finger", 2, "5e", "A metre rule balances on your finger at one particular point. Explain what this point is and why the rule balances there.",
  [P("it is the centre of gravity of the rule", ["centre of gravity"]),
   P("the weight acts through the finger (pivot), so it has no moment / moments on each side balance", ["through the finger", "through the pivot", "no moment", "moments balance", "equal moments", "balanced"])],
  "The balance point is the rule's centre of gravity. The weight of the rule acts through this point, which is directly above the finger, so the weight has no moment about the finger and the rule balances.",
  ["Where does the weight of the rule act?", "What is its moment about the finger if it acts through it?", "Explain."],
  "balance point = centre of gravity; weight through pivot, no moment",
  ["It is the centre of gravity; the weight acts through the finger so there is no turning moment", "the centre of gravity, where the moments on each side balance"],
  ["It is the heaviest end", "It is always the 0 cm mark"], min_points=2)

Q("w5b_steering_wheel", 2, "5a", "Explain why lorries have large steering wheels.",
  [P("the driver's hands are a large distance from the centre (pivot) of the wheel", ["large distance", "far from the centre", "large radius", "further from the pivot", "bigger wheel"]),
   P("so a smaller force produces the large moment needed to steer", ["smaller force", "less force", "large moment", "bigger moment", "easier to turn"])],
  "On a large steering wheel the driver's hands are a large distance from the centre, which is the pivot. Since moment = force × distance, a smaller force is needed to produce the large moment required to steer the heavy lorry.",
  ["Where is the pivot of a steering wheel?", "What does a large wheel change?", "Use moment = F × d."],
  "large radius → smaller force for same moment",
  ["The hands are further from the pivot, so a smaller force gives the large moment needed", "a bigger wheel means a larger distance, so less force is needed to steer"],
  ["Big wheels look better", "They reduce the lorry's weight"], min_points=2)

Q("w5b_crowbar", 2, "5d", "Fig. 1 shows a crowbar used to lift a heavy rock. Explain how a person can lift the rock with a much smaller force than its weight.",
  [P("the crowbar is a lever with the pivot close to the rock", ["lever", "pivot close to the rock", "pivot near the rock", "short distance"]),
   P("the effort is applied far from the pivot (long arm)", ["far from the pivot", "long arm", "large distance", "end of the bar"]),
   P("the moments balance: small effort × large distance = large load × small distance", ["moments balance", "principle of moments", "small effort", "large distance", "small force"])],
  "The crowbar is a lever with its pivot very close to the rock. The person pushes at the far end, a large distance from the pivot. By the principle of moments, a small effort × large distance can balance the large load × small distance, so the rock can be lifted with a much smaller force.",
  ["Where is the pivot compared with the rock?", "Where is the effort applied?", "Use the principle of moments."],
  "lever; pivot near load; effort far → small effort",
  ["The pivot is close to the rock and the effort is far away, so by the principle of moments a small force lifts it", "a small force at a large distance balances the large load at a small distance"],
  ["The crowbar makes the rock lighter", "The rock is pushed by friction"], min_points=2,
  figure=lambda: sketches.beam(2.2, 0.3, [("load", 0.1, "down"), ("effort", 2.1, "down")]))


Q("w5b_wrench_pipe", 2, "5a", "A plumber slides a metal pipe over the handle of a wrench to undo a very tight nut. Explain why this helps.",
  [P("the pipe makes the handle longer, so the force is applied further from the pivot (the nut)", ["longer", "further from the pivot", "further from the nut", "larger distance", "greater distance", "extends the handle"]),
   P("so the same force gives a larger moment on the nut", ["larger moment", "bigger moment", "greater moment", "more turning effect", "same force"])],
  "The pipe extends the handle, so the plumber's force is applied further from the nut, which is the pivot. Since moment = force × distance, the same force now gives a larger moment on the nut, enough to loosen it.",
  ["What does the pipe change about the wrench?", "Where is the pivot?", "Use moment = force × distance."],
  "longer handle → larger distance → larger moment",
  ["The pipe makes the handle longer, so the same force at a larger distance gives a bigger moment", "it extends the handle so the force is further from the nut, giving more turning effect"],
  ["The pipe makes the wrench heavier", "The pipe reduces friction on the nut"], min_points=2)

# ---------------------------------------------------------------- L3
Q("w5b_forearm", 3, "5d", "When you hold a heavy book in your hand with your forearm horizontal, your biceps muscle pulls up on the forearm close to the elbow. Explain why the biceps force must be much larger than the weight of the book.",
  [P("the elbow is the pivot", ["elbow is the pivot", "pivot is the elbow", "about the elbow"]),
   P("the biceps acts much closer to the elbow than the book does", ["closer to the elbow", "short distance", "small distance", "near the elbow", "much closer"]),
   P("for the moments to balance, a small distance needs a large force", ["moments balance", "principle of moments", "large force", "larger force", "bigger force"])],
  "The elbow acts as the pivot. The biceps pulls up very close to the elbow, while the book's weight acts much further away, in the hand. For the moments about the elbow to balance, the biceps force × its small distance must equal the weight × its large distance, so the biceps force must be much larger than the weight.",
  ["Where is the pivot of the forearm?", "Compare the distances of the muscle and the book from it.", "Use the principle of moments."],
  "pivot at elbow; muscle close → much larger force",
  ["The elbow is the pivot and the biceps acts much closer to it than the book, so it needs a larger force for the moments to balance", "the muscle's distance is small, so its force must be big to balance the book's moment"],
  ["The muscle is weaker than the book", "The book has no moment"], min_points=2)

Q("w5b_paint_lid", 3, "5d", "Explain why a screwdriver can be used to prise off the tight lid of a paint tin.",
  [P("the screwdriver acts as a lever with the tin's rim as the pivot", ["lever", "rim", "pivot", "edge of the tin"]),
   P("the hand pushes far from the pivot, the lid is very close to it", ["far from the pivot", "long handle", "close to the pivot", "short distance", "large distance"]),
   P("so a small force on the handle produces a large force on the lid", ["small force", "large force", "bigger force", "moments balance"])],
  "The screwdriver acts as a lever, with the rim of the tin as the pivot. The hand pushes on the handle a long way from the pivot, while the tip pushes on the lid very close to it. By the principle of moments, a small force on the handle produces a large force on the lid, enough to lift it.",
  ["What acts as the pivot?", "Compare the distances of the hand and the lid from the pivot.", "Apply the principle of moments."],
  "lever; pivot at rim; small effort far → large force on lid",
  ["It is a lever with the rim as the pivot; a small force far away gives a large force on the lid close to the pivot", "the long handle means a small push makes a big force on the lid"],
  ["The screwdriver is sharp", "It heats the paint"], min_points=2)

Q("w5b_bridge_supports", 3, "5d", "A person stands on a plank resting on two supports, one at each end, closer to the left support. Explain which support pushes up with the larger force.",
  [P("the left support (the one nearer the person)", ["left support", "nearer support", "closer support", "the left"]),
   P("taking moments about the right support, the person's weight has a larger moment arm about it, so the left support must provide more upward force", ["moments about", "take moments", "principle of moments", "larger moment", "further from"]),
   P("the supports share the total weight, the nearer one taking more", ["share", "more of the weight", "takes more", "total weight"])],
  "The left support, nearer the person, pushes up harder. Taking moments about the right support, the person's weight is a long distance from it, so the left support must give a larger upward force to balance that moment. The two supports share the total weight, with the nearer one taking more.",
  ["Take moments about one of the supports.", "How far is the person from each support?", "Which support must take more of the weight?"],
  "nearer (left) support pushes harder",
  ["The left support, because the person is closer to it; taking moments about the right support shows it must push harder", "the nearer support takes more of the weight"],
  ["Both push equally", "The right support pushes harder"], min_points=2)

Q("w5b_bus_tilt", 3, "5e", "A double-decker bus is tilted on a test ramp. Explain the condition for it to topple over.",
  [P("it topples when the vertical line through its centre of gravity falls outside its base (wheels)", ["outside the base", "outside its base", "beyond the wheels", "outside the wheels", "falls outside"]),
   P("then the weight gives a moment about the lower wheels that turns it over, instead of back", ["moment", "turns it over", "tips it over", "about the wheels", "turning effect"])],
  "The bus topples when the vertical line through its centre of gravity falls outside its base, beyond the lower wheels. The weight then has a moment about the lower wheels that turns the bus over, instead of a moment that turns it back onto all its wheels.",
  ["Where does the bus's weight act?", "What happens when the line of action of the weight passes the edge of the base?", "Explain the toppling."],
  "line of action of weight outside base → toppling moment",
  ["It topples when the line through its centre of gravity falls outside its base, so the weight's moment turns it over", "when the centre of gravity is beyond the wheels, the weight tips it over"],
  ["It topples as soon as it tilts", "It topples when it gets too heavy"], min_points=1)

Q("w5b_wine_glass", 3, "5e", "Explain why a wine glass has a wide, heavy base.",
  [P("a heavy base lowers the centre of gravity", ["lowers the centre of gravity", "low centre of gravity", "centre of gravity low", "lower centre of gravity"]),
   P("a wide base means it can tilt further before the centre of gravity passes outside the base", ["wide base", "tilt further", "outside the base", "harder to topple", "more stable"])],
  "The heavy base lowers the glass's centre of gravity, and the wide base means the glass can be tilted further before the line of action of its weight falls outside the base. Both make the glass more stable and less likely to topple.",
  ["What does a heavy base do to the centre of gravity?", "What does a wide base do?", "Link both to stability."],
  "heavy base → low CG; wide base → more stable",
  ["The heavy base lowers the centre of gravity and the wide base means it can tilt further before toppling", "it gives a low centre of gravity and a wide base, so it is more stable"],
  ["The base makes it hold more wine", "It looks more expensive"], min_points=2)

Q("w5b_child_moves_in", 3, "5d", "A see-saw is balanced with a child on each side. One child moves closer to the pivot. Explain what happens.",
  [P("that child's moment decreases (same weight, smaller distance)", ["moment decreases", "smaller moment", "less moment", "smaller distance"]),
   P("the moments no longer balance; the other child's moment is larger", ["no longer balance", "not balanced", "larger moment", "unbalanced"]),
   P("so the see-saw tips down on the other child's side", ["tips", "goes down", "other side goes down", "other child goes down", "turns"])],
  "Moving closer to the pivot reduces that child's moment, since the weight is unchanged but the distance is smaller. The moments no longer balance: the other child's moment is now larger, so the see-saw turns, with the other child's side going down.",
  ["What happens to the moving child's moment?", "Are the moments still equal?", "Which way does the see-saw turn?"],
  "moment decreases → unbalanced → other side goes down",
  ["The child's moment decreases, so the other child's moment is larger and that side goes down", "the moments are no longer balanced, so the see-saw tips towards the other child"],
  ["Nothing changes", "The child who moved goes down"], min_points=2)

Q("w5b_mobile", 3, "5d", "A hanging mobile has a light rod with a large toy near the centre and a small toy near the end. Explain how it can balance.",
  [P("the rod balances when the moments about the suspension point are equal", ["moments are equal", "equal moments", "moments balance", "principle of moments", "clockwise equals anticlockwise", "same on each side"]),
   P("the large (heavy) toy is close to the pivot and the small (light) toy far from it, so weight × distance is the same", ["heavy toy close", "light toy far", "weight × distance", "larger weight smaller distance", "small toy further"])],
  "The rod balances when the moments about the point where it hangs are equal. The heavy toy is close to the pivot and the light toy is far from it, so weight × distance can be the same for both, giving equal and opposite moments.",
  ["What is the condition for balance?", "Compare the weights and distances of the toys.", "Use moment = weight × distance."],
  "equal moments: heavy × short = light × long",
  ["The moments about the pivot are equal, because the heavy toy is close and the light toy is far away", "weight × distance is the same on each side"],
  ["The toys must be the same weight", "The string holds it level"], min_points=2, pitfalls=[FORCES_EQUAL])

Q("w5b_plasticine_rule_cg", 3, "5e", "A lump of plasticine is stuck near one end of a metre rule. Describe how to find the new centre of gravity of the rule-and-plasticine, and where you expect it to be.",
  [P("balance the rule on a knife edge (or finger), moving it until it balances", ["knife edge", "balance", "finger", "move until it balances", "pivot"]),
   P("the balance point is the new centre of gravity", ["balance point", "centre of gravity"]),
   P("it is closer to the end with the plasticine (no longer at 50 cm)", ["closer to the plasticine", "towards the plasticine", "nearer the end with", "not at 50 cm", "moved towards"])],
  "Place the rule on a knife edge and slide it until it balances. The balance point is the new centre of gravity. It will be closer to the end with the plasticine, not at the 50 cm mark, because the extra mass is on that side.",
  ["How can you find a centre of gravity by balancing?", "Where was it before the plasticine was added?", "Which way does it move?"],
  "balance on knife edge; CG moves towards the plasticine",
  ["Balance it on a knife edge; the balance point is the centre of gravity, which moves towards the plasticine end", "slide it on a finger until it balances; it will be closer to the end with the plasticine"],
  ["It stays at 50 cm", "Hang it from one end"], min_points=2)

Q("w5b_door_stop", 3, "5a", "A door stop wedged far from the hinge holds a door open more firmly than one placed near the hinge. Explain why.",
  [P("far from the hinge, the door stop's force acts at a large distance from the pivot", ["large distance", "far from the hinge", "further from the pivot", "long distance", "bigger distance", "greater distance"]),
   P("so it can give a large moment to balance the moment trying to close the door", ["large moment", "bigger moment", "balance the moment", "resist the moment", "larger moment"])],
  "Placed far from the hinge, the door stop pushes on the door at a large distance from the pivot, so its force gives a large moment that can balance the moment trying to close the door (e.g. from a draught). Near the hinge, the same force gives only a small moment.",
  ["Where is the pivot?", "How does distance affect the moment of the door stop's force?", "Explain."],
  "large distance → large resisting moment",
  ["Far from the hinge the distance is large, so the door stop gives a larger moment to resist the door closing", "a bigger distance from the pivot means a larger moment holding the door"],
  ["The door is lighter far from the hinge", "There is less air far from the hinge"], min_points=2)


Q("w5b_gate_sag", 3, "5e", "A long, heavy garden gate is held by hinges at one end. Over time its far end sags downwards. Explain this using moments, and suggest one fix.",
  [P("the gate's weight acts at its centre of gravity, far from the hinges", ["centre of gravity", "far from the hinges", "weight acts at the centre", "middle of the gate"]),
   P("so the weight has a large moment about the hinges, pulling the far end down", ["large moment", "big moment", "moment about the hinges", "turning effect", "pulls the far end down"]),
   P("fix: a diagonal brace, a wheel or support under the far end, or a lighter / shorter gate", ["brace", "diagonal", "wheel", "support", "lighter gate", "shorter gate", "post"])],
  "The gate's weight acts at its centre of gravity, a long way from the hinges, so it has a large moment about the hinges that tends to turn the far end downwards; over time this bends the hinges and frame. A diagonal brace, or a wheel or post supporting the far end, provides an opposing force and reduces the sag.",
  ["Where does the gate's weight act?", "How large is its moment about the hinges?", "How could that moment be resisted?"],
  "weight far from hinges → large moment → sagging; brace or support",
  ["The weight acts at the centre of gravity far from the hinges, so it has a large moment that pulls the far end down; a wheel under the end would help", "a large moment about the hinges makes it sag, so add a diagonal brace"],
  ["The hinges get rusty and shrink", "The gate grows longer"], min_points=2)

# ---------------------------------------------------------------- L4
Q("w5b_find_unknown_mass", 4, "5d", "Describe how to find the mass of a small stone using a metre rule pivoted at its centre and a known 50 g mass.",
  [P("hang the stone on one side and move the 50 g mass on the other side until the rule balances", ["move the 50 g", "until it balances", "until the rule balances", "adjust", "slide"]),
   P("measure each distance from the pivot", ["measure the distances", "distance from the pivot", "measure each distance", "d1", "both distances"]),
   P("use the principle of moments: m × d₁ = 50 × d₂, so m = 50 × d₂ ÷ d₁", ["principle of moments", "m × d", "50 × d", "moments", "m = 50"])],
  "Balance the metre rule at its centre, so its own weight has no moment. Hang the stone at a fixed distance on one side and slide the 50 g mass along the other side until the rule balances. Measure both distances from the pivot. By the principle of moments, m × d₁ = 50 g × d₂, so m = 50 × d₂ ÷ d₁. Repeat for different positions and average.",
  ["Why pivot the rule at its centre?", "What do you adjust to get balance?", "How do you calculate the mass?"],
  "balance with known mass; measure distances; m d₁ = 50 d₂",
  ["Hang the stone on one side and move the 50 g mass until it balances, measure both distances and use the principle of moments: m × d₁ = 50 × d₂", "balance the rule, measure the distances from the pivot and use moments to find m"],
  ["Weigh the rule", "Put the stone at the pivot"], min_points=2)

Q("w5b_crane_load_limit", 4, "5d", "A crane's maximum safe load gets smaller the further the load is from the tower. Explain why, using moments.",
  [P("the moment of the load = load × distance from the tower", ["load × distance", "weight × distance", "moment of the load", "moment = force × distance"]),
   P("further out, the same load gives a larger moment", ["larger moment", "bigger moment", "moment increases", "further out"]),
   P("the counterweight/crane can only balance a certain moment, so the load must be smaller to keep the moment safe (avoid toppling)", ["counterweight", "topple", "smaller load", "maximum moment", "balance", "tip over"])],
  "The moment of the load about the tower is load × distance. Further out, the same load produces a larger moment. The counterweight and crane structure can only balance a certain maximum moment without toppling, so the load must be smaller when it is further out to keep the moment within that limit.",
  ["What is the moment of the load?", "What happens to it as the distance increases?", "What limits the moment the crane can handle?"],
  "moment = load × distance; limited balancing moment",
  ["The moment is load × distance, so further out the same load has a bigger moment; the counterweight can only balance a certain moment, so the load must be smaller to stop it toppling", "a larger distance gives a larger moment, so the safe load decreases"],
  ["The cable is weaker further out", "The load gets heavier further out"], min_points=2)

Q("w5b_wheelchair_ramp", 4, "5e", "A wheelchair can tip backwards when going up a steep ramp. Explain why, and how 'anti-tip' wheels at the back help.",
  [P("on a slope the centre of gravity moves back relative to the wheels", ["centre of gravity moves back", "moves backwards", "cg shifts back", "behind the wheels"]),
   P("if the line of action of the weight falls behind the rear wheels, it topples backwards", ["behind the rear wheels", "outside the base", "falls behind", "topple backwards", "tips backwards"]),
   P("anti-tip wheels extend the base backwards, keeping the weight's line of action within the base", ["extend the base", "wider base", "bigger base", "within the base", "longer base"])],
  "On a steep ramp the wheelchair tilts back, so its centre of gravity moves back relative to the wheels. If the line of action of its weight falls behind the rear wheels, the weight's moment tips it over backwards. Anti-tip wheels extend the base further back, so the line of action of the weight stays within the base and the chair does not topple.",
  ["What happens to the centre of gravity's position on a slope?", "When does an object topple?", "How do extra wheels change the base?"],
  "CG moves back; line of action outside base; anti-tip wheels extend base",
  ["On the ramp the centre of gravity moves back, and if the weight acts behind the rear wheels it tips; anti-tip wheels extend the base", "the cg shifts back outside the base; extra wheels make the base longer so it stays inside"],
  ["The wheels are too small", "The wheelchair gets heavier on a slope"], min_points=2)

Q("w5b_carry_plank_cg", 4, "5e", "Explain why it is easiest to carry a long plank with one hand when you hold it at its centre of gravity.",
  [P("holding it at its centre of gravity, the weight acts through your hand (pivot)", ["through your hand", "through the pivot", "at the centre of gravity", "weight acts through"]),
   P("so the weight has no moment about your hand, and the plank does not tend to turn", ["no moment", "does not turn", "no turning", "balanced", "zero moment"]),
   P("elsewhere, the weight's moment would tend to rotate it, which your hand must resist", ["would rotate", "tend to turn", "must resist", "twist", "turning effect"])],
  "If you hold the plank at its centre of gravity, its weight acts through your hand, so the weight has no moment about your hand and the plank does not tend to turn. Held anywhere else, the weight would have a moment about your hand, and you would have to resist it to stop the plank rotating.",
  ["Where does the weight of the plank act?", "What is its moment about your hand if you hold it there?", "What happens if you hold it elsewhere?"],
  "hold at CG → weight through hand → no moment",
  ["At the centre of gravity the weight acts through your hand, so there is no moment and it does not turn", "holding it elsewhere gives the weight a moment that tends to rotate it"],
  ["The plank is lighter at its centre", "It is easier to see where you are going"], min_points=1)

Q("w5b_stand_from_chair", 4, "5e", "Explain why you have to lean forward before you can stand up from a chair.",
  [P("standing on your feet, your feet are your new base", ["feet are the base", "new base", "base is your feet", "standing on your feet"]),
   P("your centre of gravity must be above your feet, or your weight's moment pulls you back down", ["above your feet", "over your feet", "centre of gravity over", "pulls you back", "fall back"]),
   P("leaning forward moves your centre of gravity forward over your feet", ["moves the centre of gravity forward", "move your centre of gravity", "shifts the centre of gravity", "lean forward"])],
  "When you stand up, your feet become your base. Sitting, your centre of gravity is behind your feet, so if you tried to stand straight up your weight's moment would pull you back into the chair. Leaning forward moves your centre of gravity forward until it is above your feet, so you can rise without toppling backwards.",
  ["What is your base when standing?", "Where is your centre of gravity when you are seated?", "What does leaning forward achieve?"],
  "lean to bring CG over the feet (base)",
  ["Leaning forward moves your centre of gravity over your feet, which are your base, otherwise you fall back", "your cg must be above your feet to stand, so you lean forward"],
  ["Leaning makes you lighter", "Chairs push you forward"], min_points=2)

Q("w5b_balance_two_kids_one_adult", 4, "5d", "Two children, each of weight 300 N, sit together 2 m from the pivot of a see-saw. Explain how an adult of weight 600 N could balance them.",
  [P("the children's total moment = 600 N × 2 m = 1200 N m", ["1200", "600 × 2", "2 × 300", "total moment"]),
   P("the adult must give an equal moment on the other side", ["equal moment", "same moment", "moments balance", "principle of moments"]),
   P("so sit 2 m from the pivot on the other side (1200 ÷ 600)", ["2 m", "1200 ÷ 600", "same distance", "2 metres"])],
  "The children's combined moment is 2 × 300 N × 2 m = 1200 N m. The adult must provide an equal moment on the other side, so the adult should sit 1200 ÷ 600 = 2 m from the pivot on the opposite side.",
  ["Find the children's total moment.", "What moment must the adult provide?", "Solve for the distance."],
  "1200 N m; adult at 2 m on other side",
  ["The children give a moment of 1200 N m, so the adult must sit 2 m from the pivot on the other side", "600 × 2 = 1200 N m, so 1200 ÷ 600 = 2 m"],
  ["The adult sits at the pivot", "The adult sits 4 m away"], min_points=2)

Q("w5b_tall_vs_short_topple", 4, "5e", "Two blocks have the same square base, but one is twice as tall. Explain which can be tilted further before it topples.",
  [P("the shorter block can be tilted further", ["shorter block", "short block", "shorter one", "short one"]),
   P("its centre of gravity is lower", ["lower centre of gravity", "centre of gravity is lower", "low centre of gravity"]),
   P("so it must be tilted through a larger angle before the line of action of its weight falls outside the base", ["larger angle", "further", "outside the base", "line of action", "beyond the edge"])],
  "The shorter block can be tilted further. Its centre of gravity is lower, so it must be tilted through a larger angle before the vertical line through its centre of gravity passes outside the edge of its base and it topples.",
  ["Where is each block's centre of gravity?", "When does a block topple?", "Which needs the larger tilt?"],
  "shorter → lower CG → larger tilt before toppling",
  ["The shorter block, because its centre of gravity is lower, so it needs a larger angle before the weight acts outside the base", "the short one has a low cg, so it can be tilted further"],
  ["The taller block, because it is heavier", "Both topple at the same angle"], min_points=2)

Q("w5b_balancing_toy", 4, "5e", "A balancing toy rests on a point with heavy weights hanging below the point on curved arms. Explain why it is so stable.",
  [P("the heavy weights put the centre of gravity below the pivot point", ["below the pivot", "below the point", "centre of gravity is below", "underneath the pivot"]),
   P("when tilted, the weight produces a moment that turns it back to its original position", ["turns it back", "restoring", "back to its original", "returns", "moment brings it back"])],
  "The heavy weights on the curved arms put the toy's centre of gravity below its pivot point. When the toy is tilted, its weight acts to one side of the pivot and produces a moment that turns it back towards its original position, so it is very stable.",
  ["Where is the toy's centre of gravity?", "What happens to the weight's moment when it tilts?", "Explain the stability."],
  "CG below pivot → restoring moment",
  ["Its centre of gravity is below the pivot, so when tilted the weight's moment turns it back", "the weights put the cg below the point, giving a moment that returns it"],
  ["It is glued to the point", "It is very light"], min_points=2)

Q("w5b_verify_principle", 4, "5c", "Describe an experiment to check the principle of moments using a metre rule, a pivot and some slotted masses.",
  [P("balance the metre rule on the pivot at its centre", ["balance the rule", "pivot at the centre", "at its centre", "50 cm"]),
   P("hang different masses at different distances on each side and adjust until it balances", ["hang masses", "different masses", "adjust", "until it balances", "both sides"]),
   P("measure the distances and check that sum of clockwise moments = sum of anticlockwise moments", ["clockwise moments", "anticlockwise moments", "sum of", "check", "equal moments", "force × distance"])],
  "Balance the metre rule on the pivot at its centre so its weight has no moment. Hang masses at various distances on both sides and adjust their positions until the rule balances again. Measure each distance from the pivot and calculate the moments: the sum of the clockwise moments should equal the sum of the anticlockwise moments. Repeat with different arrangements.",
  ["Why pivot the rule at its centre?", "What do you vary?", "What do you calculate and compare?"],
  "balance; hang masses; compare sums of moments",
  ["Balance the rule at its centre, hang masses on both sides until it balances, then check that clockwise moments equal anticlockwise moments", "measure the distances, work out force × distance on each side and compare"],
  ["Measure how fast the rule falls", "Weigh the rule only"], min_points=1)

Q("w5b_carry_bag_lean", 4, "5e", "When carrying a heavy bag in your right hand, you lean to the left. Explain why.",
  [P("the bag moves the combined centre of gravity to the right", ["moves the centre of gravity", "centre of gravity to the right", "shifts the centre of gravity", "cg moves right"]),
   P("leaning left brings the centre of gravity back above your feet (base)", ["above your feet", "over your feet", "over the base", "within the base", "back over"]),
   P("otherwise the weight's moment would tip you over to the right", ["topple", "tip over", "fall", "moment"])],
  "The heavy bag moves the combined centre of gravity of you and the bag towards the right. By leaning left, you bring the centre of gravity back above your feet, your base; otherwise the weight would have a moment that tips you over to the right.",
  ["What does the bag do to the combined centre of gravity?", "Where must the centre of gravity be?", "How does leaning help?"],
  "bag shifts CG right; lean left to keep CG over feet",
  ["The bag shifts the centre of gravity to the right, so you lean left to keep it above your feet", "leaning brings the cg back over the base so you do not topple"],
  ["Leaning makes the bag lighter", "Your left side is stronger"], min_points=1)

# ---------------------------------------------------------------- L5
Q("w5b_spanner_force_claim", 5, "5b", "A student says: 'A longer spanner works better because it lets you push with a bigger force.' Evaluate this claim.",
  [P("the claim is misleading: your push need not be bigger", ["misleading", "wrong", "not a bigger force", "same force", "not correct", "not the force", "it is the moment"]),
   P("the longer spanner increases the distance from the pivot, so the same push gives a larger moment", ["larger moment", "bigger moment", "greater distance", "longer distance", "moment = force × distance"]),
   P("so a smaller push can produce the moment needed to undo the nut", ["smaller push", "less force", "smaller force", "easier"])],
  "The claim is misleading. A longer spanner does not let you push with a bigger force; it increases the distance from the pivot to where you push. Since moment = force × distance, the same push gives a larger moment, so a smaller push can produce the moment needed to loosen the nut.",
  ["What does a longer spanner change: your force or the distance?", "Which quantity turns the nut?", "Evaluate the claim."],
  "same force, larger distance → larger moment",
  ["Misleading: the force is the same but the distance is larger, so the moment is larger; you can use a smaller force", "it is the moment, not the force, that increases, because moment = force × distance"],
  ["Correct, longer spanners increase your strength", "Correct, the force is doubled"], min_points=2)

Q("w5b_design_stable_lamp", 5, "5e", "Design a desk lamp that is hard to knock over. Explain each design feature using ideas about centre of gravity.",
  [P("a heavy base (to lower the centre of gravity)", ["heavy base", "lower the centre of gravity", "low centre of gravity", "weight at the bottom"]),
   P("a wide base", ["wide base", "broad base", "large base"]),
   P("so it can be tilted further before the line of action of its weight falls outside the base", ["outside the base", "tilt further", "line of action", "harder to topple"]),
   P("keep the lampshade/arm light", ["light lampshade", "light arm", "light top", "lightweight top"])],
  "Give the lamp a heavy, wide base and a light arm and lampshade. The heavy base and light top keep the centre of gravity low, and the wide base means the lamp can be tilted a long way before the vertical line through its centre of gravity falls outside the base, so it is hard to knock over.",
  ["What makes an object stable?", "How can you lower the centre of gravity?", "How does the base width help?"],
  "heavy wide base; light top; CG stays within base",
  ["A heavy, wide base and a light shade keep the centre of gravity low, so it can tilt further before the weight acts outside the base", "make the base heavy and broad so the cg is low and stays inside the base"],
  ["A tall thin stand with a heavy shade", "Make it out of glass"], min_points=2)

Q("w5b_cg_inside_claim", 5, "5e", "A student says: 'The centre of gravity of an object is always somewhere inside the material of the object.' Evaluate this claim with examples.",
  [P("the claim is wrong", ["wrong", "not always", "incorrect", "false"]),
   P("examples: a ring, horseshoe, boomerang, mug or chair, where the centre of gravity is in empty space", ["ring", "horseshoe", "boomerang", "mug", "chair", "hoop", "empty space", "hole"]),
   P("it is the point where the whole weight acts, which can be outside the material", ["whole weight", "weight acts", "point where", "outside the material"])],
  "The claim is wrong. The centre of gravity is the point where the whole weight can be taken to act, and it need not be in the material. For a ring or a horseshoe, it lies in the empty space at the centre; for a boomerang it lies between the arms.",
  ["Define centre of gravity.", "Think of a ring or a horseshoe.", "Where is its centre of gravity?"],
  "wrong; ring/horseshoe CG in empty space",
  ["Wrong: for a ring or horseshoe the centre of gravity is in the empty space, because it is just where the whole weight acts", "not always; a boomerang has its centre of gravity outside the material"],
  ["Correct, it must be inside", "Correct, it is always at the heaviest part"], min_points=2)

Q("w5b_unequal_arms", 5, "5d", "A shopkeeper's beam balance has one arm slightly longer than the other. Evaluate how this affects the masses measured.",
  [P("the balance relies on equal moments: m₁ × d₁ = m₂ × d₂", ["equal moments", "moments", "m × d", "principle of moments"]),
   P("with unequal arms, balance occurs with unequal masses", ["unequal masses", "different masses", "not equal masses", "masses are not equal"]),
   P("so the measured mass is wrong (too large or too small depending on which pan is used)", ["wrong", "incorrect", "too large", "too small", "inaccurate", "error"])],
  "A beam balance works by the principle of moments: m₁ × d₁ = m₂ × d₂. If the arms are equal, balance means equal masses. With one arm longer, the beam balances when the masses are unequal, so the mass read from the standard weights is wrong: too small if the goods are on the longer arm, too large if they are on the shorter arm.",
  ["What principle does a beam balance use?", "What happens to the balance condition if d₁ ≠ d₂?", "How does that affect the reading?"],
  "moments: unequal arms → unequal masses balance → wrong reading",
  ["It uses moments, so with unequal arms the masses that balance are unequal and the measured mass is wrong", "the moments m × d must be equal, so if the arms differ, unequal masses balance and the reading is too large or too small"],
  ["It makes no difference", "It changes the weight of the goods"], min_points=2)

Q("w5b_counterweight_adjust", 5, "5d", "Some cranes can move their counterweight along the short arm. Evaluate why this is useful.",
  [P("the load's moment changes with the load and its distance", ["load's moment", "moment of the load", "changes", "load × distance"]),
   P("moving the counterweight changes its moment so it can balance the load's moment", ["balance", "change its moment", "equal moment", "match the moment", "moments balance"]),
   P("keeping the resultant moment small stops the crane toppling", ["topple", "tip over", "stable", "resultant moment"])],
  "The moment of the load about the tower depends on the size of the load and how far out it is. By moving the counterweight along the short arm, its moment can be adjusted to balance the load's moment. Keeping the resultant moment small stops the crane from toppling over in either direction.",
  ["Is the load's moment always the same?", "How does moving the counterweight change its moment?", "What is the danger if the moments are unbalanced?"],
  "adjust counterweight moment to balance varying load moment; avoid toppling",
  ["The load's moment changes, so moving the counterweight lets its moment balance it and stops the crane toppling", "it keeps the moments balanced for different loads so the crane does not tip over"],
  ["It makes the crane taller", "It lifts the load faster"], min_points=2)

Q("w5b_child_adult_balance", 5, "5d", "A 400 N child wants to balance a 600 N adult on a see-saw 4 m long, pivoted at its centre. Evaluate whether this is possible and where they should sit.",
  [P("possible, if the adult sits closer to the pivot than the child", ["possible", "adult closer", "adult sits closer", "closer to the pivot"]),
   P("moments must be equal: 400 × d₁ = 600 × d₂", ["400 ×", "600 ×", "equal moments", "moments balance", "principle of moments"]),
   P("e.g. child at the end, 2 m, and adult at 400 × 2 ÷ 600 ≈ 1.33 m", ["1.33", "1.3 m", "2 m", "800 ÷ 600"])],
  "It is possible if the adult sits closer to the pivot than the child. The moments must be equal: 400 × d(child) = 600 × d(adult). For example, with the child at the end, 2 m from the pivot, the adult must sit 400 × 2 ÷ 600 ≈ 1.33 m from the pivot on the other side.",
  ["Can unequal weights balance?", "Write the condition for balance.", "Choose a position for the child and find the adult's."],
  "possible; adult closer; 400 d₁ = 600 d₂ (e.g. 2 m and 1.33 m)",
  ["Yes, if the adult sits closer to the pivot: with the child at 2 m, the adult sits at 1.33 m so the moments are equal", "possible because 400 × 2 = 600 × 1.33, so equal moments"],
  ["Impossible because the weights are different", "The adult must sit further away"], min_points=2, pitfalls=[FORCES_EQUAL])

Q("w5b_ignore_beam_weight_claim", 5, "5d", "A student balances a uniform rule on a pivot at the 30 cm mark using a weight at the 10 cm mark, and ignores the weight of the rule. Evaluate this.",
  [P("the rule's weight cannot be ignored here, because it acts at the 50 cm mark, not at the pivot", ["50 cm", "not at the pivot", "cannot be ignored", "acts at the centre", "rule's weight"]),
   P("it has a moment about the pivot (weight × 20 cm)", ["has a moment", "20 cm", "moment about the pivot", "its own moment"]),
   P("its moment must be included: weight × 20 cm = hanging weight × 20 cm", ["include", "must be included", "taken into account", "clockwise"])],
  "This is wrong. The rule is uniform, so its weight acts at the 50 cm mark, 20 cm from the pivot at 30 cm. Its weight therefore has a moment about the pivot and must be included: the rule's weight × 20 cm (clockwise) balances the hanging weight × 20 cm (anticlockwise). The rule's weight can only be ignored when it is pivoted at its centre.",
  ["Where does the weight of a uniform rule act?", "Is that at the pivot?", "Does the rule's weight have a moment?"],
  "rule's weight at 50 cm has a moment about a 30 cm pivot",
  ["It cannot be ignored because the rule's weight acts at 50 cm, 20 cm from the pivot, so it has a moment that must be included", "the weight of the rule is not at the pivot, so its moment must be taken into account"],
  ["It is fine because rules are light", "The weight of the rule acts at the pivot"], min_points=2)

Q("w5b_bus_design_low", 5, "5e", "Bus designers place heavy parts such as the engine and fuel tank as low as possible. Evaluate why, referring to tilt tests.",
  [P("heavy parts low keeps the centre of gravity low", ["centre of gravity low", "low centre of gravity", "lowers the centre of gravity"]),
   P("so the bus can tilt through a larger angle before the line of action of its weight falls outside its base", ["larger angle", "bigger angle", "tilt further", "outside the base", "line of action", "outside the wheels"]),
   P("making it less likely to topple on bends or slopes (passing tilt tests)", ["less likely to topple", "more stable", "not topple", "bends", "pass the test"])],
  "Putting the heavy parts low keeps the bus's centre of gravity low. The bus can then be tilted through a larger angle before the vertical line through its centre of gravity falls outside its wheelbase, so it is more stable and less likely to topple on sharp bends or slopes. This is what tilt tests check.",
  ["Where is the centre of gravity if heavy parts are low?", "How does that affect the toppling angle?", "Why does it matter on the road?"],
  "low CG → larger toppling angle → stable",
  ["It keeps the centre of gravity low, so the bus can tilt further before the weight acts outside the base, making it less likely to topple", "a low cg means a bigger angle is needed to tip it over, so it is more stable"],
  ["Heavy parts low make the bus faster", "It makes the bus lighter"], min_points=2)

Q("w5b_arm_muscle_design", 5, "5d", "The biceps muscle is attached very close to the elbow. Evaluate this arrangement: what is the disadvantage, and what is the advantage?",
  [P("disadvantage: the muscle must exert a much larger force than the load (small distance from the pivot)", ["larger force", "much bigger force", "small distance", "large force", "disadvantage"]),
   P("advantage: a small contraction of the muscle moves the hand a large distance (quickly)", ["large distance", "moves the hand far", "quickly", "fast", "large movement", "small contraction"])],
  "Because the biceps is attached close to the elbow (the pivot), its moment arm is small, so it must exert a force much larger than the load to balance the load's moment, a disadvantage. The advantage is that a small shortening of the muscle moves the hand through a large distance quickly, giving speed and range of movement.",
  ["How far is the muscle from the pivot compared with the hand?", "What does that mean for the force needed?", "What is gained in return?"],
  "close attachment: large force needed, but large, fast movement of the hand",
  ["The muscle needs a much larger force because it is close to the elbow, but a small contraction moves the hand a large distance quickly", "disadvantage: large force needed; advantage: fast, large movement"],
  ["The muscle is attached far from the elbow", "There is no disadvantage"], min_points=2)

Q("w5b_bottle_quarter_full", 5, "5e", "A plastic bottle a quarter full of water is harder to knock over than the same bottle completely full. Evaluate why.",
  [P("a quarter-full bottle has its centre of gravity low (the water sits at the bottom)", ["centre of gravity low", "low centre of gravity", "water at the bottom", "lower centre of gravity"]),
   P("the full bottle's centre of gravity is higher (near the middle of its height)", ["higher centre of gravity", "middle of the bottle", "centre of gravity is higher"]),
   P("a lower centre of gravity means a larger tilt is needed before the line of action falls outside the base", ["larger tilt", "tilt further", "outside the base", "line of action", "more stable"])],
  "With only a quarter of the water, the water sits at the bottom, so the bottle's centre of gravity is low. When full, the centre of gravity is higher, near the middle of its height. A lower centre of gravity means the bottle must be tilted further before the vertical line through its centre of gravity falls outside its base, so the quarter-full bottle is more stable.",
  ["Where is the centre of gravity in each bottle?", "How does its height affect stability?", "Evaluate."],
  "quarter full → low CG → more stable",
  ["The quarter-full bottle has a low centre of gravity because the water is at the bottom, so it must tilt further before the weight acts outside the base", "the full bottle has a higher cg so it topples more easily"],
  ["The full bottle is more stable because it is heavier", "They are equally stable"], min_points=1,
  pitfalls=[PF(["full bottle is more stable", "heavier so more stable", "equally stable"], "Stability depends on the HEIGHT of the centre of gravity, not just the weight.")])
