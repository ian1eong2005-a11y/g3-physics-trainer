"""Chapter 4 Dynamics: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import figs
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 4


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


FORCE_OF_MOTION = PF(["force of motion", "forward force keeps it moving", "needs a force to keep moving", "needs a force to keep it moving"],
                     "No force is needed to keep an object moving at constant velocity (Newton's first law).")
SAME_BODY_PAIR = PF(["weight and normal force are an action", "weight and the normal force are an action", "weight and normal reaction are a pair"],
                    "Weight and the normal force both act on the same body, so they are not an action–reaction pair.")

# ---------------------------------------------------------------- L1
Q("w4b_first_law", 1, "4a", "State Newton's first law of motion.",
  [P("an object stays at rest or keeps moving at constant velocity (steady speed in a straight line)", ["stays at rest", "remains at rest", "constant velocity", "constant speed in a straight line", "uniform motion", "keeps moving"]),
   P("unless a resultant (unbalanced) force acts on it", ["unless a resultant force", "unless an unbalanced force", "no resultant force", "unless a force acts", "unless acted on"])],
  "An object stays at rest, or continues to move at constant velocity in a straight line, unless a resultant force acts on it.",
  ["The first law is about what happens when there is NO resultant force.", "What does a stationary object do? A moving one?", "State the law in one sentence."],
  "stays at rest / constant velocity unless a resultant force acts",
  ["An object stays at rest or moves at constant velocity unless a resultant force acts on it", "a body keeps moving in a straight line at constant speed unless an unbalanced force acts"],
  ["Force equals mass times acceleration", "Every action has an equal and opposite reaction"], min_points=2)

Q("w4b_third_law", 1, "4a", "State Newton's third law of motion.",
  [P("if body A exerts a force on body B, B exerts a force on A", ["exerts a force on", "a on b", "b on a", "every action has", "action and reaction", "force on each other"]),
   P("the forces are equal in size and opposite in direction (and of the same type)", ["equal and opposite", "equal in size", "opposite in direction", "same size"])],
  "If body A exerts a force on body B, then body B exerts a force on body A that is equal in size, opposite in direction and of the same type.",
  ["This law is about pairs of forces between two bodies.", "How do the sizes and directions of the pair compare?", "State it."],
  "A on B ⇒ B on A, equal and opposite",
  ["If A exerts a force on B, B exerts an equal and opposite force on A", "every action has an equal and opposite reaction acting on the other body"],
  ["An object stays at rest unless a force acts", "Force equals mass times acceleration"], min_points=2)

Q("w4b_define_newton", 1, "4c", "Define the newton, the unit of force.",
  [P("the force that gives a mass of 1 kg an acceleration of 1 m/s²", ["1 kg", "1 m/s2", "one kilogram", "acceleration of 1"])],
  "One newton is the resultant force that gives a mass of 1 kg an acceleration of 1 m/s².",
  ["Use F = m a.", "Put m = 1 kg and a = 1 m/s².", "State the definition."],
  "force giving 1 kg an acceleration of 1 m/s²",
  ["The force that gives 1 kg an acceleration of 1 m/s²", "one newton accelerates a one kilogram mass at 1 m/s²"],
  ["The weight of 1 kg", "The force needed to move 1 m"],
  pitfalls=[PF(["weight of 1 kg", "weight of one kilogram"], "1 kg weighs about 10 N on Earth; the newton is defined by F = m a.")])

Q("w4b_mass_and_accel", 1, "4c", "State how the acceleration produced by a given resultant force depends on the mass of the object.",
  [P("larger mass gives smaller acceleration (a = F ÷ m; inversely proportional)", ["smaller acceleration", "less acceleration", "inversely proportional", "a = f / m", "a = f ÷ m", "the bigger the mass the smaller", "more mass less acceleration"])],
  "For a given resultant force, the larger the mass, the smaller the acceleration: a = F ÷ m, so the acceleration is inversely proportional to the mass.",
  ["Use F = m a with F fixed.", "If m is bigger, what happens to a?", "State the relationship."],
  "larger mass → smaller acceleration (a = F ÷ m)",
  ["A larger mass gives a smaller acceleration", "the acceleration is inversely proportional to the mass, a = F ÷ m"],
  ["A larger mass gives a larger acceleration", "Mass does not affect acceleration"],
  pitfalls=[PF(["larger mass gives a larger acceleration", "more mass more acceleration", "bigger mass bigger acceleration"], "With the same force, a bigger mass accelerates LESS.")])

Q("w4b_friction_direction_def", 1, "4d", "A box slides to the left across a floor. State the direction of the friction on it and explain.",
  [P("to the right", ["to the right", "right", "opposite direction"]),
   P("because friction opposes the relative motion (sliding) of the surfaces", ["opposes", "against the motion", "opposite to the motion", "resists the motion", "opposite direction to the sliding", "opposite to the sliding"])],
  "Friction acts to the right, because friction always opposes the relative motion of the two surfaces sliding over each other.",
  ["Which way is the box moving?", "Does friction act with or against the motion?", "State the direction and reason."],
  "to the right; opposes motion",
  ["To the right, because friction opposes the motion", "it acts in the opposite direction to the sliding, to the right"],
  ["To the left, the same way as it moves", "Upwards"], min_points=2,
  pitfalls=[PF(["to the left", "same way as it moves", "same direction as the motion"], "Friction acts OPPOSITE to the direction of motion.")])

Q("w4b_air_resistance_def", 1, "4d", "State what air resistance is and how it changes with speed.",
  [P("a frictional (drag) force from the air opposing motion through it", ["opposes the motion", "friction from the air", "drag", "force from the air", "resists motion through air"]),
   P("it increases as the speed increases", ["increases with speed", "increases as speed increases", "larger at higher speed", "faster means more", "greater speed greater", "gets larger as", "larger as the object moves faster"])],
  "Air resistance is a frictional (drag) force exerted by the air on an object moving through it, opposing its motion. It increases as the object's speed increases.",
  ["What does the air do to a moving object?", "Is it bigger when you move faster or slower?", "State both."],
  "drag opposing motion; increases with speed",
  ["Air resistance is a drag force opposing motion through the air, and it increases with speed", "friction from the air that gets larger as the object moves faster"],
  ["Air resistance pushes objects forward", "It is the weight of the air"], min_points=2)

Q("w4b_resultant_def", 1, "4a", "State what is meant by the resultant force on a body.",
  [P("the single force that has the same effect as all the forces acting on the body together (their vector sum)", ["single force", "same effect as all", "overall force", "net force", "sum of all the forces", "combined effect"])],
  "The resultant force is the single force that has the same effect as all the forces acting on a body together; it is their vector sum.",
  ["Several forces can act on one body.", "Can they be replaced by one force?", "Define that force."],
  "single force equivalent to all forces (vector sum)",
  ["The single force that has the same effect as all the forces acting together", "the net force, the vector sum of all the forces on the body"],
  ["The largest force acting on the body", "The force the body exerts on the ground"])

Q("w4b_rest_stays_rest", 1, "4a", "A book lies on a table with balanced forces acting on it. State what happens to the book and explain.",
  [P("it stays at rest", ["stays at rest", "remains at rest", "does not move", "stays still"]),
   P("because the resultant force is zero, so there is no acceleration", ["resultant force is zero", "no resultant force", "zero resultant", "no acceleration", "balanced"])],
  "The book stays at rest. The forces are balanced, so the resultant force is zero and there is no acceleration (Newton's first law).",
  ["Balanced forces give what resultant?", "What happens with no resultant force?", "State and explain."],
  "stays at rest; zero resultant",
  ["It stays at rest because the resultant force is zero", "nothing changes; balanced forces give no acceleration so it remains at rest"],
  ["It slowly slides off", "It accelerates upwards"], min_points=2)

Q("w4b_force_shape", 1, "4a", "Besides changing an object's speed or direction, state one other effect a force can have on an object, with an example.",
  [P("change its shape or size (deform it)", ["shape", "size", "deform", "squash", "stretch", "bend", "compress"]),
   P("example: squeezing a ball, stretching a spring, bending a ruler", ["ball", "spring", "ruler", "clay", "sponge", "rubber band"])],
  "A force can change an object's shape or size: for example, stretching a spring, squashing a sponge or bending a ruler.",
  ["Think of what happens when you squeeze a sponge.", "Is that a change in motion?", "Name the effect and an example."],
  "change shape/size; example",
  ["It can change the shape of an object, like squashing a sponge", "stretching a spring changes its size"],
  ["It can change the object's mass", "It can change its colour"], min_points=2,
  pitfalls=[PF(["change its mass", "changes the mass"], "A force cannot change an object's mass.")])

Q("w4b_cup_forces", 1, "4b", "Fig. 1 shows a cup at rest on a table. Name the two forces acting on the cup and state how they compare.",
  [P("weight (downwards) and normal force/reaction from the table (upwards)", ["weight", "normal", "reaction", "gravity"]),
   P("they are equal in size and opposite in direction", ["equal", "same size", "balanced", "equal and opposite"])],
  "The two forces are the cup's weight, acting downwards, and the normal force from the table, acting upwards. Because the cup is at rest, they are equal in size and opposite in direction.",
  ["One force is caused by gravity.", "The other comes from the table.", "How must they compare if the cup stays still?"],
  "weight and normal force; equal and opposite",
  ["Its weight downwards and the normal force from the table upwards; they are equal and opposite", "gravity pulls it down and the table pushes it up with an equal force"],
  ["Friction and tension", "Air resistance and thrust"], min_points=2,
  figure=lambda: figs.force_diagram([("?", "up", 1.3), ("?", "down", 1.3)], label_body="cup"))

# ---------------------------------------------------------------- L2
Q("w4b_seat_belt", 2, "4a", "Explain how a seat belt protects a passenger when a car stops suddenly.",
  [P("the passenger tends to keep moving forward at the car's original speed (no force on them otherwise)", ["keep moving forward", "continue moving", "tends to keep moving", "first law", "inertia", "same speed"]),
   P("the belt exerts a backward force on the passenger, slowing them down with the car", ["backward force", "force backwards", "holds them back", "pulls them back", "slows them down", "stops them"]),
   P("so they do not hit the windscreen or dashboard", ["windscreen", "dashboard", "hit the", "thrown forward"])],
  "When the car stops suddenly, the passenger tends to continue moving forward at the original speed, because no force acts on them to slow them down (Newton's first law). The seat belt exerts a backward force on the passenger, slowing them down with the car so they are not thrown into the windscreen or dashboard.",
  ["What does the passenger's body tend to do when the car stops?", "What force does the belt provide?", "What does this prevent?"],
  "passenger keeps moving; belt gives backward force",
  ["The passenger keeps moving forward, so the belt provides a backward force to slow them down and stop them hitting the windscreen", "by the first law they continue moving; the seat belt holds them back"],
  ["The seat belt pushes the car forward", "The passenger is thrown forward by a forward force"], min_points=2,
  pitfalls=[PF(["thrown forward by a force", "forward force on the passenger", "pushed forward by a force"], "No forward force acts on the passenger; they simply keep moving.")])

Q("w4b_tablecloth", 2, "4a", "A magician pulls a tablecloth very quickly from under some plates, and the plates stay on the table. Explain why.",
  [P("the plates tend to stay at rest (Newton's first law / inertia)", ["stay at rest", "remain at rest", "inertia", "first law", "keep still"]),
   P("the cloth is pulled so quickly that the friction on the plates acts for only a very short time", ["very short time", "quickly", "little time", "brief", "short"]),
   P("so the plates gain hardly any speed and stay where they are", ["hardly any speed", "barely move", "do not move much", "very little", "small change"])],
  "The plates tend to stay at rest (Newton's first law). The cloth is pulled so quickly that the friction from it acts on the plates for only a very short time, so the plates gain hardly any speed and remain on the table.",
  ["What do objects at rest tend to do?", "How long does the friction from the cloth act?", "What is the effect on the plates?"],
  "plates tend to stay at rest; friction acts briefly",
  ["The plates tend to stay at rest, and the cloth moves so quickly that friction acts for a very short time, so they barely move", "inertia keeps them still because the force acts only briefly"],
  ["The plates are glued down", "The cloth pushes the plates down"], min_points=2)

Q("w4b_full_trolley", 2, "4c", "Explain why a full supermarket trolley is harder to start moving than an empty one.",
  [P("the full trolley has a larger mass", ["larger mass", "more mass", "greater mass", "heavier"]),
   P("a larger mass needs a larger force for the same acceleration (F = m a)", ["larger force", "more force", "f = ma", "f = m a", "harder to accelerate", "smaller acceleration"])],
  "The full trolley has a larger mass. By F = m a, a larger mass needs a larger resultant force to give it the same acceleration, so it is harder to start moving.",
  ["What is different about the full trolley?", "Use F = m a.", "Explain."],
  "larger mass needs larger force (F = m a)",
  ["It has more mass, so by F = ma it needs a larger force for the same acceleration", "greater mass means a smaller acceleration for the same push"],
  ["Its wheels are stuck", "It has less friction"], min_points=2)

Q("w4b_bicycle_brakes", 2, "4d", "Explain how the brakes on a bicycle make it slow down.",
  [P("the brake pads press on the wheel rims (or discs)", ["brake pads", "press on the wheel", "pads", "rim", "disc"]),
   P("friction between pads and wheel opposes the motion, giving a backward resultant force", ["friction", "opposes the motion", "backward force", "resultant force backwards", "against the motion"]),
   P("so the bicycle decelerates", ["decelerates", "slows down", "deceleration", "loses speed"])],
  "When the brakes are applied, the brake pads press on the wheel rims. Friction between the pads and the rims opposes the wheels' motion, giving a backward resultant force on the bicycle, so it decelerates.",
  ["What touches the wheel when you brake?", "Which force acts between them?", "What effect does that force have?"],
  "pads press on wheel; friction opposes motion; decelerates",
  ["The brake pads press on the wheel and friction opposes the motion, so the bicycle slows down", "friction between the pads and the rim gives a backward force and the bike decelerates"],
  ["The brakes make the bicycle lighter", "The brakes push the road"], min_points=2)

Q("w4b_walking_on_ice", 2, "4d", "Explain why it is difficult to walk on ice.",
  [P("there is very little friction between shoes and ice", ["little friction", "low friction", "less friction", "very little friction", "smooth"]),
   P("walking needs friction: your foot pushes back on the ground and friction pushes you forward", ["push back", "pushes backwards", "friction pushes you forward", "grip", "foot slips"])],
  "To walk, your foot pushes backwards on the ground and friction from the ground pushes you forwards. On ice there is very little friction, so your foot slips backwards instead and you cannot push yourself forward.",
  ["What force from the ground lets you walk?", "How much of that force is there on ice?", "What happens to your foot?"],
  "walking needs friction; ice gives little friction",
  ["There is very little friction on ice, and walking needs friction to push you forward, so your foot slips", "your foot pushes back on the ground but with low friction it just slides"],
  ["Ice is too cold", "Ice has too much friction"], min_points=2,
  pitfalls=[PF(["too much friction", "more friction"], "Ice has very LITTLE friction.")])

Q("w4b_swimmer", 2, "4a", "Explain, using Newton's third law, how a swimmer moves forward through the water.",
  [P("the swimmer pushes the water backwards", ["pushes the water backwards", "pushes water back", "push the water backward", "force on the water backwards"]),
   P("the water pushes the swimmer forwards with an equal and opposite force", ["water pushes the swimmer forward", "water pushes forward", "equal and opposite", "pushes them forward", "reaction pushes"])],
  "The swimmer's arms and legs push the water backwards. By Newton's third law, the water pushes the swimmer forwards with a force of equal size, so the swimmer moves forward.",
  ["Which way do the swimmer's hands push the water?", "What does the third law say about the water's force on the swimmer?", "Explain the motion."],
  "pushes water back; water pushes swimmer forward",
  ["The swimmer pushes the water backwards and the water pushes the swimmer forwards with an equal and opposite force", "by the third law, pushing water back gives a forward push on the swimmer"],
  ["The water pulls the swimmer by friction", "The swimmer floats forward"], min_points=2)

Q("w4b_balloon_rocket", 2, "4a", "A blown-up balloon is released and shoots across the room. Explain its motion using Newton's third law.",
  [P("the balloon pushes the air out backwards", ["pushes the air out", "pushes air backwards", "air is pushed out", "forces the air out", "force on the air backwards", "air backwards"]),
   P("the air pushes the balloon forwards with an equal and opposite force", ["air pushes the balloon", "equal and opposite", "pushes it forward", "forward force on the balloon", "reaction"])],
  "The stretched balloon pushes the air out of its neck backwards. By Newton's third law, the air pushes the balloon forwards with an equal and opposite force, so the balloon shoots forward.",
  ["What does the balloon do to the air inside it?", "What does the air do back to the balloon?", "Which way does the balloon move?"],
  "balloon pushes air back; air pushes balloon forward",
  ["The balloon pushes air out backwards, and the air pushes the balloon forwards equally", "third law: force on the air backwards, equal and opposite force on the balloon forwards"],
  ["The air outside pushes the balloon", "The balloon is lighter than air"], min_points=2)

Q("w4b_hanging_lamp", 2, "4b", "Fig. 1 shows a lamp hanging at rest from a cord. Describe the forces on the lamp.",
  [P("tension in the cord acting upwards", ["tension", "upwards", "cord pulls up", "pull of the cord"]),
   P("weight acting downwards", ["weight", "downwards", "gravity"]),
   P("they are equal and opposite because the lamp is at rest (zero resultant)", ["equal", "balanced", "zero resultant", "equal and opposite", "same size"])],
  "Two forces act on the lamp: the tension in the cord pulling it upwards and its weight pulling it downwards. Because the lamp is at rest, the resultant force is zero, so the tension equals the weight.",
  ["What pulls the lamp up?", "What pulls it down?", "How must they compare if it is at rest?"],
  "tension up = weight down",
  ["Tension acts upwards and weight acts downwards, and they are equal because the lamp is at rest", "the cord pulls up with a tension equal to the weight pulling down"],
  ["Only its weight acts", "Friction holds it up"], min_points=2,
  figure=lambda: figs.force_diagram([("T", "up", 1.4), ("W", "down", 1.4)], label_body="lamp", ground=False))

Q("w4b_plane_cruising", 2, "4a", "An aircraft flies horizontally at a constant velocity. State how the forces on it compare and explain.",
  [P("thrust equals drag (air resistance)", ["thrust equals drag", "thrust equals air resistance", "thrust = drag", "forward and backward forces are equal"]),
   P("lift equals weight", ["lift equals weight", "lift = weight", "upward and downward forces are equal"]),
   P("because constant velocity means zero resultant force", ["zero resultant", "no resultant", "constant velocity", "balanced", "no acceleration"])],
  "At constant velocity there is no acceleration, so the resultant force is zero: the forward thrust equals the drag, and the upward lift equals the weight.",
  ["What does constant velocity tell you about acceleration?", "So what is the resultant force?", "Compare the pairs of opposite forces."],
  "thrust = drag; lift = weight; zero resultant",
  ["Thrust equals drag and lift equals weight because the resultant force is zero at constant velocity", "the forces are balanced: thrust = air resistance and lift = weight"],
  ["Thrust is greater than drag to keep it moving", "Lift is greater than weight"], min_points=2, pitfalls=[FORCE_OF_MOTION])

Q("w4b_oil_engine", 2, "4d", "Explain why oil is used between the moving parts of an engine.",
  [P("oil reduces friction between the moving surfaces", ["reduces friction", "less friction", "lower friction", "lubricant", "lubricate"]),
   P("so less energy is wasted as heat and the parts wear out less", ["less heat", "less wear", "wear", "overheating", "less energy wasted", "efficient"])],
  "Oil acts as a lubricant, reducing friction between the moving parts. This means less energy is wasted as heat and the parts wear out less quickly.",
  ["What does friction between moving parts cause?", "How does oil change the friction?", "What are the benefits?"],
  "reduces friction; less heating and wear",
  ["Oil reduces friction between moving parts, so there is less heat and less wear", "it lubricates the engine so less energy is wasted and parts last longer"],
  ["Oil increases friction for grip", "Oil makes the engine heavier"], min_points=2,
  pitfalls=[PF(["increases friction", "more friction"], "Oil REDUCES friction.")])

# ---------------------------------------------------------------- L3
Q("w4b_loaded_car", 3, "4c", "A car accelerates more slowly when it is fully loaded with passengers and luggage, even though the engine provides the same force. Explain.",
  [P("the loaded car has a larger mass", ["larger mass", "more mass", "greater mass", "heavier"]),
   P("a = F ÷ m, so for the same resultant force the acceleration is smaller", ["a = f / m", "a = f ÷ m", "f = ma", "f = m a", "smaller acceleration", "less acceleration"])],
  "The loaded car has a larger mass. Since a = F ÷ m, the same resultant force produces a smaller acceleration on a larger mass, so the car speeds up more slowly.",
  ["What changes when the car is loaded?", "Use F = m a with the same F.", "Explain."],
  "larger mass; same F → smaller a",
  ["The loaded car has more mass, so with the same force a = F ÷ m is smaller", "greater mass gives less acceleration for the same force"],
  ["The engine gets tired", "The car has less friction"], min_points=2)

Q("w4b_double_force", 3, "4c", "The resultant force on a trolley is doubled while its mass stays the same. Explain what happens to its acceleration.",
  [P("the acceleration doubles", ["doubles", "twice", "two times", "double"]),
   P("because acceleration is proportional to resultant force (a = F ÷ m, m fixed)", ["proportional", "a = f / m", "a = f ÷ m", "f = ma", "f = m a", "mass is the same"])],
  "The acceleration doubles. With the mass fixed, a = F ÷ m, so the acceleration is directly proportional to the resultant force.",
  ["Use F = m a.", "Which quantity is fixed?", "If F doubles, what happens to a?"],
  "acceleration doubles (a ∝ F)",
  ["The acceleration doubles because a = F ÷ m and the mass is the same", "it is proportional to the force, so twice the force gives twice the acceleration"],
  ["The acceleration halves", "The acceleration stays the same"], min_points=2)

Q("w4b_rocket_space", 3, "4a", "A student says a rocket cannot work in space because there is no air to push against. Explain how a rocket accelerates in space.",
  [P("the rocket pushes its exhaust gases backwards (out of the nozzle)", ["pushes the exhaust", "pushes gases backwards", "exhaust gases", "pushes the gas out", "ejects gas"]),
   P("the gases push the rocket forwards with an equal and opposite force (third law)", ["gases push the rocket", "equal and opposite", "third law", "pushes the rocket forward", "reaction"]),
   P("it does not need air: it pushes on its own exhaust", ["does not need air", "no air needed", "not push on the air", "own exhaust", "not the air"])],
  "A rocket pushes its exhaust gases backwards out of its nozzle. By Newton's third law, the gases push the rocket forwards with an equal and opposite force. It is pushing on its own exhaust, not on air, so it works in space.",
  ["What does a rocket push on?", "What pushes back on the rocket?", "Is air needed for this?"],
  "pushes exhaust back; exhaust pushes rocket forward; no air needed",
  ["The rocket pushes exhaust gases backwards and the gases push it forwards equally, so it does not need air", "by the third law the exhaust pushes the rocket forward; it pushes on its own gases, not on the air"],
  ["Rockets cannot work in space", "The rocket pushes against the stars"], min_points=2)

Q("w4b_hovercraft", 3, "4d", "Explain why a hovercraft glides easily over land and water.",
  [P("it rides on a cushion of air, so it does not touch the surface", ["cushion of air", "layer of air", "air cushion", "does not touch", "floats on air"]),
   P("so there is very little friction", ["little friction", "less friction", "reduces friction", "almost no friction", "low friction"])],
  "A hovercraft rides on a cushion of air, so its body does not touch the surface. This greatly reduces friction, so a small force can keep it moving easily.",
  ["What is underneath a hovercraft?", "Does it touch the ground?", "What does that do to friction?"],
  "air cushion → very little friction",
  ["It floats on a cushion of air so there is very little friction", "the air layer means it does not touch the ground, reducing friction"],
  ["Its engines are very heavy", "It has large tyres"], min_points=2)

Q("w4b_magnets_pair", 3, "4a", "A large magnet and a small magnet attract each other. A student says the large magnet pulls harder. Explain why this is wrong.",
  [P("by Newton's third law the forces are equal in size (and opposite)", ["equal", "same size", "third law", "equal and opposite"]),
   P("each magnet exerts a force on the other; the pair acts on different bodies", ["each exerts", "on the other", "different bodies", "on each other", "both"])],
  "By Newton's third law, the force the large magnet exerts on the small one is equal in size and opposite in direction to the force the small magnet exerts on the large one. The two forces act on different bodies, but they are always equal.",
  ["Which law is about pairs of forces between two bodies?", "What does it say about their sizes?", "Explain."],
  "third law: equal and opposite forces",
  ["By the third law the forces on each magnet are equal and opposite, so the big magnet does not pull harder", "each magnet pulls the other with the same size of force"],
  ["The large magnet pulls harder because it is stronger", "The small magnet does not pull at all"], min_points=1,
  pitfalls=[PF(["large magnet pulls harder", "bigger magnet pulls harder", "small magnet does not pull"], "The forces in a third-law pair are always equal in size.")])

Q("w4b_book_slows", 3, "4d", "A book is pushed across a table and released. It slows down and stops. Explain why.",
  [P("after release, the only horizontal force is friction", ["only friction", "friction acts", "friction is the only", "no push"]),
   P("friction opposes the motion, giving a resultant force backwards", ["opposes the motion", "backward", "resultant force", "against the motion"]),
   P("so the book decelerates until it stops", ["decelerates", "slows down", "deceleration", "until it stops"])],
  "Once the book is released, the only horizontal force on it is friction from the table. Friction opposes the motion, so there is a resultant force backwards, which makes the book decelerate until it stops.",
  ["What horizontal forces act after the push stops?", "Which way does friction act?", "What does a backward resultant force do?"],
  "only friction → backward resultant → decelerates",
  ["Only friction acts, opposing the motion, so the resultant force is backwards and the book decelerates", "friction gives a backward resultant force so it slows down and stops"],
  ["Its force of motion runs out", "It gets tired"], min_points=2, pitfalls=[FORCE_OF_MOTION, PF(["force runs out", "push runs out", "force of motion runs out"], "Nothing 'runs out'; friction causes the deceleration.")])

Q("w4b_lift_constant_up", 3, "4a", "A lift moves upwards at a constant speed. Explain how the tension in its cable compares with its weight.",
  [P("the tension equals the weight", ["equals the weight", "tension = weight", "same as the weight", "equal"]),
   P("constant speed in a straight line means zero acceleration, so zero resultant force", ["zero acceleration", "no acceleration", "zero resultant", "no resultant", "constant speed", "balanced"])],
  "The tension equals the weight. Moving at constant speed in a straight line means there is no acceleration, so the resultant force is zero and the upward and downward forces balance.",
  ["Is the lift accelerating?", "What resultant force is needed for zero acceleration?", "Compare tension and weight."],
  "tension = weight; zero resultant",
  ["The tension equals the weight because at constant speed there is no acceleration and no resultant force", "they are balanced, so tension = weight"],
  ["The tension is greater because it is moving up", "The tension is zero"], min_points=2,
  pitfalls=[PF(["greater because it is moving up", "tension is greater"], "At CONSTANT speed the forces balance; tension is greater only while accelerating upwards.")])

Q("w4b_cyclist_top_speed", 3, "4d", "A cyclist pedals with a constant driving force but eventually reaches a steady top speed. Explain why.",
  [P("air resistance (and friction) increase as her speed increases", ["air resistance increases", "increases with speed", "drag increases", "resistive forces increase", "more air resistance"]),
   P("eventually they equal the driving force", ["equal the driving force", "balance the driving force", "equals the forward force", "balanced"]),
   P("then the resultant force is zero, so there is no acceleration and the speed is constant", ["resultant force is zero", "no resultant", "no acceleration", "constant speed", "steady speed"])],
  "As the cyclist speeds up, air resistance and friction increase. Eventually they become equal to her driving force, so the resultant force is zero; there is then no acceleration and she moves at a steady top speed.",
  ["What happens to air resistance as she speeds up?", "What happens when it equals her driving force?", "Explain the steady speed."],
  "air resistance grows until it equals driving force; zero resultant",
  ["Air resistance increases with speed until it equals her driving force, so the resultant force is zero and her speed stays constant", "the drag grows until the forces balance, giving no acceleration"],
  ["She gets tired and pedals less", "Her mass increases"], min_points=2)

Q("w4b_trolley_force_meter", 3, "4c", "A force meter pulls a trolley on a smooth bench. Explain why the trolley accelerates even though the pulling force is constant.",
  [P("there is a constant resultant (unbalanced) force on the trolley", ["resultant force", "unbalanced force", "constant force", "net force"]),
   P("a resultant force produces an acceleration (F = m a), so the velocity keeps increasing", ["f = ma", "f = m a", "produces an acceleration", "acceleration", "velocity increases", "speeds up"])],
  "With a smooth bench there is (almost) no friction, so the constant pull is an unbalanced resultant force on the trolley. A resultant force produces an acceleration, F = m a, so the trolley's velocity keeps increasing at a constant rate.",
  ["Is anything balancing the pull?", "What does a resultant force do?", "Explain."],
  "constant resultant force → constant acceleration",
  ["The pull is an unbalanced resultant force, and F = ma means it produces a constant acceleration", "there is a net force, so the trolley keeps speeding up"],
  ["Because the force meter is moving", "Because the trolley is light"], min_points=2)

Q("w4b_falling_apple_pair", 3, "4a", "An apple falls from a tree. Identify the action–reaction pair involving the apple's weight.",
  [P("the Earth pulls the apple downwards (the apple's weight)", ["earth pulls the apple", "earth on the apple", "weight of the apple", "gravitational pull of the earth"]),
   P("the apple pulls the Earth upwards with an equal force", ["apple pulls the earth", "apple on the earth", "pulls the earth up", "equal force on the earth"])],
  "The Earth pulls the apple downwards with a gravitational force (the apple's weight). The reaction is the apple pulling the Earth upwards with a gravitational force of equal size.",
  ["The weight is the pull of which body on which?", "The reaction acts on the other body.", "State both forces."],
  "Earth pulls apple down; apple pulls Earth up",
  ["The Earth pulls the apple down and the apple pulls the Earth up with an equal force", "weight of the apple is the Earth's pull; the apple pulls the Earth upwards equally"],
  ["The weight and the air resistance", "The weight and the normal force"], min_points=2, pitfalls=[SAME_BODY_PAIR])

# ---------------------------------------------------------------- L4
Q("w4b_lift_slowing_down", 4, "4c", "A person stands on bathroom scales in a lift that is moving DOWN but slowing to a stop. Explain whether the scales read more or less than the person's weight.",
  [P("slowing down while moving downwards means the acceleration is upwards", ["acceleration is upwards", "accelerating upwards", "upward acceleration", "acceleration upwards"]),
   P("so the upward normal force from the scales must be greater than the weight", ["greater than the weight", "more than the weight", "larger than the weight", "normal force is greater"]),
   P("so the scales read more than the person's weight", ["read more", "reads more", "higher reading", "greater reading", "heavier"])],
  "The lift is moving down but slowing, so its acceleration is upwards. For the person to accelerate upwards, the upward normal force from the scales must be greater than their weight, so the scales read more than the person's weight.",
  ["Moving down and slowing: which way is the acceleration?", "Which force must be bigger for that acceleration?", "So what do the scales show?"],
  "acceleration up → normal force > weight → reading more",
  ["The acceleration is upwards, so the normal force is greater than the weight and the scales read more", "slowing while going down means an upward acceleration, so the reading is higher than the weight"],
  ["The scales read less because the lift is going down", "The scales read zero"], min_points=2,
  pitfalls=[PF(["read less because", "reads less because it is going down"], "It is the direction of the ACCELERATION (upwards here) that matters, not the direction of motion.")])

Q("w4b_wet_brakes", 4, "4d", "Explain why a car takes longer to stop on a wet road than on a dry one, braking as hard as possible.",
  [P("water reduces the friction between the tyres and the road", ["less friction", "reduces friction", "lower friction", "smaller friction", "slippery"]),
   P("so the maximum braking (resultant) force is smaller", ["smaller force", "smaller braking force", "less braking force", "smaller resultant force"]),
   P("so the deceleration is smaller (a = F ÷ m) and it takes longer and further to stop", ["smaller deceleration", "less deceleration", "longer to stop", "further to stop", "a = f / m", "a = f ÷ m"])],
  "Water reduces the friction between the tyres and the road, so the maximum braking force is smaller. By a = F ÷ m, the deceleration is smaller, so the car takes longer, and a longer distance, to stop.",
  ["What does water do to tyre–road friction?", "How does that affect the force that can slow the car?", "Use a = F ÷ m."],
  "less friction → smaller force → smaller deceleration",
  ["Water reduces the friction, so the braking force is smaller and the deceleration is less, so it takes longer to stop", "less friction gives a smaller resultant force and a smaller deceleration"],
  ["The car is heavier when wet", "The brakes get hotter"], min_points=2)

Q("w4b_box_on_slope_fbd", 4, "4b", "A box rests without moving on a rough slope. Describe the three forces acting on it.",
  [P("its weight, acting vertically downwards", ["weight", "vertically downwards", "gravity"]),
   P("the normal force, acting at right angles to the slope", ["normal force", "right angles to the slope", "perpendicular to the slope", "normal reaction"]),
   P("friction, acting up the slope (stopping it sliding down)", ["friction", "up the slope", "stops it sliding", "along the slope"])],
  "Three forces act on the box: its weight, acting vertically downwards; the normal force from the slope, acting at right angles to the slope's surface; and friction, acting up the slope to stop the box sliding down. Because the box is at rest, these three forces balance.",
  ["Which force always acts vertically downwards?", "Which force acts at right angles to the surface?", "Which force stops it sliding?"],
  "weight (down), normal (perpendicular to slope), friction (up the slope)",
  ["Weight acts vertically down, the normal force acts at right angles to the slope, and friction acts up the slope", "gravity downwards, a perpendicular normal force and friction along the slope upwards"],
  ["Weight and thrust", "Only its weight"], min_points=3)

Q("w4b_crouch_cyclist", 4, "4d", "Racing cyclists crouch low over their handlebars. Explain how this lets them reach a higher top speed.",
  [P("crouching reduces their air resistance (smaller area facing the air)", ["reduces air resistance", "less air resistance", "smaller area", "streamlined", "less drag"]),
   P("at top speed, air resistance balances the driving force", ["balances the driving force", "equals the driving force", "balanced", "top speed when"]),
   P("so with less air resistance at a given speed they can go faster before the forces balance", ["go faster", "higher speed", "faster before", "higher top speed"])],
  "Crouching makes the cyclist more streamlined, reducing air resistance at any given speed. Top speed is reached when air resistance becomes equal to the driving force, so with less air resistance at each speed, the cyclist can go faster before the forces balance.",
  ["What does crouching change?", "What decides the top speed?", "Link the two."],
  "crouch → less drag; top speed when drag = driving force",
  ["Crouching reduces air resistance, so they can go faster before air resistance equals the driving force", "being streamlined gives less drag, so the top speed is higher"],
  ["Crouching makes them lighter", "Crouching increases their driving force"], min_points=2)

Q("w4b_plan_mass_accel", 4, "4c", "Plan an experiment to show how the acceleration of a trolley depends on its mass when the resultant force is kept constant.",
  [P("keep the pulling force constant (e.g. same hanging mass or force meter reading)", ["constant force", "same force", "same pulling force", "keep the force", "same hanging mass"]),
   P("change the mass by adding masses to the trolley", ["add masses", "change the mass", "adding masses", "different masses", "load the trolley"]),
   P("measure the acceleration each time (light gates or ticker tape) and compare / plot", ["measure the acceleration", "light gates", "ticker tape", "plot", "graph", "compare"])],
  "Pull the trolley with a constant force, for example by the same hanging mass over a pulley. Change the trolley's mass by adding masses to it. For each mass, measure the acceleration with light gates or a ticker-timer. The results should show that a larger mass gives a smaller acceleration (a ∝ 1/m).",
  ["What must you keep the same?", "What do you change?", "What do you measure, and how?"],
  "constant force; vary mass; measure acceleration",
  ["Keep the pulling force the same, add masses to the trolley and measure the acceleration with light gates each time", "use the same force, change the mass and compare the accelerations"],
  ["Change both the force and the mass", "Measure the trolley's colour"], min_points=2)

Q("w4b_earth_doesnt_move", 4, "4c", "An apple pulls the Earth upwards with the same size of force as the Earth pulls the apple down. Explain why the Earth does not noticeably accelerate towards the apple.",
  [P("the forces are equal in size (third law)", ["equal", "same size", "third law", "same force"]),
   P("the Earth's mass is enormous compared with the apple's", ["enormous mass", "huge mass", "much larger mass", "very large mass", "mass of the earth is huge"]),
   P("a = F ÷ m, so the Earth's acceleration is tiny", ["a = f / m", "a = f ÷ m", "tiny acceleration", "very small acceleration", "negligible"])],
  "By the third law the two forces are equal in size. But the Earth's mass is enormous compared with the apple's, so by a = F ÷ m, the Earth's acceleration is far too tiny to notice, while the apple's is about 10 m/s².",
  ["Are the forces equal?", "How do the masses compare?", "Use a = F ÷ m."],
  "equal forces; huge mass → tiny acceleration",
  ["The forces are equal but the Earth has an enormous mass, so a = F ÷ m gives a tiny acceleration", "same force, but the Earth's huge mass means its acceleration is negligible"],
  ["The Earth does not feel any force", "The apple's force is too small"], min_points=2,
  pitfalls=[PF(["does not feel any force", "no force on the earth", "apple's force is smaller"], "The Earth feels a force equal to the apple's weight; its acceleration is tiny because of its huge mass.")])

Q("w4b_fbd_values", 4, "4b", "Fig. 1 shows a box with a 30 N push to the right, 10 N friction to the left, and its 50 N weight balanced by a 50 N normal force. Explain the resultant force and how the box moves.",
  [P("vertical forces balance (50 N up, 50 N down)", ["vertical forces balance", "50 n up and 50 n down", "weight and normal force balance", "vertical resultant is zero", "cancel"]),
   P("horizontal resultant = 30 − 10 = 20 N to the right", ["20 n", "30 − 10", "30 - 10", "to the right"]),
   P("so the box accelerates to the right", ["accelerates to the right", "accelerates", "speeds up", "acceleration to the right"])],
  "The vertical forces balance, 50 N up and 50 N down, so there is no vertical resultant. Horizontally, the resultant is 30 − 10 = 20 N to the right, so the box accelerates to the right.",
  ["Deal with vertical and horizontal forces separately.", "Do the vertical forces cancel?", "What is the horizontal resultant, and what does it do?"],
  "vertical balanced; 20 N right → accelerates right",
  ["The vertical forces balance, and the horizontal resultant is 30 − 10 = 20 N to the right, so it accelerates to the right", "a 20 N resultant to the right makes the box speed up; weight and normal force cancel"],
  ["It stays still because the forces balance", "The resultant is 90 N"], min_points=2,
  figure=lambda: figs.force_diagram([("30 N", "right", 1.6), ("10 N", "left", 1.0), ("50 N", "up", 1.1), ("50 N", "down", 1.1)], label_body="box"))

Q("w4b_heavier_skydiver", 4, "4d", "Two skydivers of different mass jump with the same body position. Explain why the heavier one reaches a higher terminal velocity.",
  [P("at terminal velocity, air resistance equals weight", ["air resistance equals weight", "air resistance = weight", "drag equals weight", "balances the weight"]),
   P("the heavier skydiver has a larger weight, so needs a larger air resistance to balance it", ["larger weight", "more weight", "needs more air resistance", "larger air resistance"]),
   P("air resistance increases with speed, so a higher speed is needed", ["increases with speed", "higher speed", "faster", "must fall faster"])],
  "At terminal velocity, air resistance equals weight. The heavier skydiver has a larger weight, so a larger air resistance is needed to balance it. Since air resistance increases with speed, the heavier skydiver must fall faster before the forces balance, giving a higher terminal velocity.",
  ["What is the condition for terminal velocity?", "Which skydiver needs more air resistance?", "How is air resistance related to speed?"],
  "terminal: drag = weight; bigger weight → more drag needed → higher speed",
  ["At terminal velocity air resistance equals weight; the heavier one has more weight so it needs more air resistance, which happens at a higher speed", "a larger weight needs a larger drag to balance, and drag increases with speed"],
  ["Heavier objects fall faster because gravity is stronger on them", "They have the same terminal velocity"], min_points=2)

Q("w4b_jump_off_boat", 4, "4a", "A girl jumps forward from a small boat onto a jetty, and the boat moves backwards. Explain why.",
  [P("she pushes backwards on the boat", ["pushes backwards on the boat", "pushes the boat back", "pushes on the boat", "force on the boat backwards"]),
   P("the boat pushes her forwards with an equal and opposite force (third law)", ["equal and opposite", "boat pushes her forward", "third law", "reaction"]),
   P("so the boat accelerates backwards (little friction from the water)", ["boat moves backwards", "accelerates backwards", "boat goes back", "little friction"])],
  "To jump forward, the girl pushes backwards on the boat. By Newton's third law the boat pushes her forwards with an equal and opposite force. The backward push on the boat, with little resistance from the water, makes the boat move backwards.",
  ["Which way does she push on the boat to jump forward?", "What does the third law say?", "What happens to the boat?"],
  "she pushes boat back; boat pushes her forward; boat moves back",
  ["She pushes back on the boat and the boat pushes her forward with an equal and opposite force, so the boat moves backwards", "by the third law her push on the boat sends it backwards"],
  ["The water pulls the boat back", "The boat is lighter after she leaves"], min_points=2)

Q("w4b_tyre_tread", 4, "4d", "Explain why car tyres have deep treads, and why this matters on wet roads.",
  [P("treads give grip (friction) between tyre and road", ["grip", "friction", "increase friction", "maintain friction"]),
   P("on wet roads, the grooves channel water away so the tyre stays in contact with the road", ["channel water", "push water away", "remove water", "water away", "stay in contact", "touches the road"]),
   P("so braking and steering forces can still act (preventing skidding)", ["braking", "steering", "skid", "skidding", "slipping"])],
  "Tyre treads help provide grip: the friction between the tyre and the road. On wet roads the grooves channel water out from under the tyre so that the rubber stays in contact with the road, keeping the friction high enough for braking and steering and preventing skidding.",
  ["What force do tyres rely on?", "What does water do between tyre and road?", "How do grooves help?"],
  "treads keep friction; grooves channel water away",
  ["The treads channel water away so the tyre stays in contact with the road and keeps the friction for braking", "deep grooves remove water, maintaining grip and preventing skidding"],
  ["Treads make the car lighter", "Treads reduce friction to go faster"], min_points=2)

# ---------------------------------------------------------------- L5
Q("w4b_horse_cart", 5, "4a", "A student says: 'A horse pulling a cart can never move it, because the cart pulls back on the horse with an equal force.' Evaluate this argument.",
  [P("the two forces in the pair act on different bodies, so they do not cancel", ["different bodies", "different objects", "do not cancel", "act on different", "not on the same"]),
   P("to decide each body's motion, consider all the forces on that body only", ["forces on the cart", "forces on the horse", "on that body", "consider each", "all the forces on"]),
   P("the cart accelerates if the horse's pull is greater than the friction on the cart (the horse pushes on the ground)", ["greater than the friction", "more than the friction", "ground pushes the horse", "pushes on the ground", "friction from the ground"])],
  "The argument is wrong. The horse's pull on the cart and the cart's pull on the horse are an action–reaction pair acting on different bodies, so they do not cancel. To find whether the cart moves, consider only the forces on the cart: if the horse's pull is greater than the friction on the cart, the cart accelerates. The horse moves forward because the ground pushes it forward when it pushes back on the ground.",
  ["Which bodies do the two forces act on?", "Can forces on different bodies cancel?", "Which forces decide whether the cart moves?"],
  "third-law pair on different bodies; consider forces on the cart only",
  ["The forces act on different bodies so they do not cancel; the cart moves if the horse's pull is greater than the friction on the cart", "wrong, the pair acts on different objects, so you must look at the forces on the cart alone"],
  ["Correct, equal forces always cancel", "Correct, the cart cannot move"], min_points=2,
  pitfalls=[PF(["equal forces always cancel", "the forces cancel", "cart cannot move"], "Third-law forces act on DIFFERENT bodies, so they never cancel each other.")])

Q("w4b_friction_surfaces_design", 5, "4d", "Design an experiment to compare the friction between a wooden block and three different surfaces.",
  [P("pull the block along each surface with a force meter (newton meter) at a slow, steady speed", ["force meter", "newton meter", "spring balance", "steady speed", "constant speed", "pull the block"]),
   P("at constant speed, the force meter reading equals the friction", ["reading equals the friction", "equal to the friction", "friction equals the pull", "balanced"]),
   P("keep the same block (same weight) and repeat for each surface, averaging", ["same block", "same weight", "same mass", "repeat", "average", "fair test"])],
  "Attach a force meter to the block and pull it along each surface at a slow, steady speed. At constant speed the forces balance, so the force-meter reading equals the friction. Use the same block (same weight) on each surface, repeat each measurement several times and average, then compare the friction for the three surfaces.",
  ["What instrument measures a pulling force?", "When does the pull equal the friction?", "What must be kept the same?"],
  "force meter at steady speed; reading = friction; same block; repeats",
  ["Pull the block with a force meter at constant speed so the reading equals the friction, using the same block on each surface and repeating", "use a newton meter, pull steadily, and compare the readings for the three surfaces with the same weight"],
  ["Drop the block on each surface", "Measure the temperature of each surface"], min_points=2)

Q("w4b_astronaut_throw", 5, "4a", "An astronaut drifting outside a space station has a heavy tool but no rope. Evaluate how she could use the tool to get back to the station.",
  [P("throw the tool directly away from the station", ["throw the tool away", "throw it away from the station", "away from the station", "push the tool away"]),
   P("the tool pushes back on her with an equal and opposite force (third law)", ["equal and opposite", "third law", "pushes back on her", "reaction"]),
   P("so she accelerates towards the station and then drifts there at constant velocity (no friction in space)", ["towards the station", "drifts", "constant velocity", "keeps moving", "no friction"])],
  "She should throw the tool directly away from the station. As she pushes the tool away, the tool pushes her in the opposite direction with an equal force (Newton's third law), so she moves towards the station. With no friction in space, she then keeps drifting towards it at constant velocity.",
  ["Which way must she push the tool?", "What force acts on her as she does so?", "What happens to her afterwards?"],
  "throw tool away from station; reaction pushes her towards it; drifts",
  ["Throw the tool away from the station; by the third law it pushes her back towards the station and she keeps drifting", "pushing the tool away gives an equal and opposite force that moves her towards the station"],
  ["Swim through space", "Throw the tool towards the station"], min_points=2,
  pitfalls=[PF(["throw the tool towards the station", "throw it towards the station"], "Throwing the tool towards the station would push her AWAY from it.")])

Q("w4b_constant_speed_claim", 5, "4a", "A student says: 'A car cruising at a constant 100 km/h has a bigger resultant force on it than a car cruising at a constant 50 km/h.' Evaluate this claim.",
  [P("wrong: both have zero resultant force", ["zero resultant", "no resultant", "both zero", "wrong", "resultant is zero"]),
   P("constant velocity means zero acceleration, so F = m a = 0", ["zero acceleration", "no acceleration", "constant velocity", "f = ma"]),
   P("the faster car needs a bigger driving force only because its air resistance is bigger; the forces still balance", ["bigger driving force", "larger driving force", "more air resistance", "balance", "drag is bigger"])],
  "The claim is wrong. Both cars move at constant velocity, so their accelerations are zero and the resultant force on each is zero (F = m a). The faster car does need a bigger driving force, but only because its air resistance is bigger; the forces on it are still balanced.",
  ["What is the acceleration of each car?", "What does that make the resultant force?", "Why does the faster car need more engine force?"],
  "both zero resultant; bigger drag needs bigger driving force",
  ["Wrong: both have zero resultant force because they are at constant velocity; the faster car only needs more driving force to balance more air resistance", "the resultant force is zero for both since there is no acceleration"],
  ["Correct, faster cars need a bigger resultant force", "Correct, 100 km/h needs twice the resultant force"], min_points=2, pitfalls=[FORCE_OF_MOTION])

Q("w4b_lift_three_stages", 5, "4c", "A lift starts from rest, accelerates upwards, moves up at constant speed, then slows to a stop. Compare the cable tension with the lift's weight in each stage.",
  [P("accelerating upwards: tension greater than weight", ["greater than the weight", "more than the weight", "tension is greater", "larger than the weight", "bigger than the weight"]),
   P("constant speed: tension equals weight", ["equals the weight", "tension = weight", "same as the weight", "equal to the weight"]),
   P("slowing down (while going up): tension less than weight", ["less than the weight", "smaller than the weight", "tension is less", "lower than the weight"])],
  "While accelerating upwards, the resultant force is upwards, so the tension is greater than the weight. At constant speed there is no acceleration, so the tension equals the weight. While slowing down on the way up, the acceleration is downwards, so the tension is less than the weight.",
  ["Find the direction of the acceleration in each stage.", "The resultant force is in the direction of the acceleration.", "Compare tension and weight for each."],
  "accelerating up: T > W; constant: T = W; slowing: T < W",
  ["Accelerating up the tension is greater than the weight, at constant speed it equals the weight, and slowing down it is less than the weight", "the tension is bigger than the weight when accelerating up, equal to the weight at constant speed, and smaller than the weight when slowing down"],
  ["The tension is always equal to the weight", "The tension is always greater because it goes up"], min_points=3)

Q("w4b_puck_ice_floor", 5, "4d", "A puck is given the same push on ice and on a wooden floor. Explain, using forces, why it slides much further on ice.",
  [P("friction on ice is much smaller", ["less friction", "smaller friction", "little friction", "low friction"]),
   P("so the backward resultant force is smaller and the deceleration is smaller (a = F ÷ m)", ["smaller deceleration", "less deceleration", "smaller resultant", "a = f / m", "a = f ÷ m", "slows down more slowly"]),
   P("so it takes longer to stop and travels further from the same starting speed", ["further", "longer to stop", "travels further", "slides further"])],
  "The friction on ice is much smaller than on wood. After the push, friction is the only horizontal force, so the backward resultant force on the ice is smaller and, by a = F ÷ m, the puck decelerates more slowly. From the same starting speed it therefore takes longer to stop and slides further.",
  ["Which force slows the puck after the push?", "How does it compare on ice and wood?", "Link this to deceleration and distance."],
  "less friction → smaller deceleration → further",
  ["There is less friction on ice, so the deceleration is smaller and it slides further before stopping", "smaller friction gives a smaller resultant force, so it slows down more slowly"],
  ["The ice pushes the puck forward", "The puck is lighter on ice"], min_points=2)

Q("w4b_weight_normal_pair_claim", 5, "4a", "A student says: 'The weight of a book on a table and the normal force from the table are an action–reaction pair.' Evaluate this claim.",
  [P("wrong: both forces act on the same body (the book)", ["same body", "both act on the book", "same object", "wrong", "act on the book"]),
   P("they are equal because the book is in equilibrium (first/second law), not because of the third law", ["equilibrium", "balanced", "at rest", "zero resultant", "first law"]),
   P("the true pairs are: Earth pulls book / book pulls Earth; table pushes book / book pushes table", ["book pulls the earth", "book pushes the table", "earth pulls the book", "table pushes the book"])],
  "The claim is wrong. The weight and the normal force both act on the same body, the book, so they cannot be an action–reaction pair. They are equal because the book is in equilibrium. The real pairs are: the Earth pulls the book and the book pulls the Earth; the table pushes up on the book and the book pushes down on the table.",
  ["Which body does each force act on?", "Why are they equal, then?", "Name the true third-law partners."],
  "same body → not a pair; equal because balanced; true pairs",
  ["Wrong: both act on the book, so they are not an action-reaction pair; they are equal because the book is at rest. The pair of the weight is the book pulling the Earth", "they act on the same object; the real partner of the normal force is the book pushing the table"],
  ["Correct, they are equal and opposite so they are a pair", "Correct, every pair of balanced forces is an action-reaction pair"], min_points=2,
  pitfalls=[PF(["equal and opposite so they are a pair", "balanced forces are an action", "every pair of balanced forces"], "Balanced forces act on the SAME body; third-law pairs act on DIFFERENT bodies.")])

Q("w4b_a_vs_f_graph", 5, "4c", "A graph of acceleration against resultant force for a trolley is a straight line through the origin. Explain what this shows and how the trolley's mass could be found from it.",
  [P("acceleration is directly proportional to resultant force", ["directly proportional", "proportional", "a ∝ f", "doubles when"]),
   P("the gradient = a ÷ F = 1 ÷ m", ["gradient", "1 / m", "1 ÷ m", "one over the mass", "a ÷ f"]),
   P("so mass = 1 ÷ gradient (or F ÷ a for any point)", ["1 ÷ gradient", "1 / gradient", "f ÷ a", "f / a", "inverse of the gradient", "mass = f"])],
  "A straight line through the origin shows that the acceleration is directly proportional to the resultant force. Since a = F ÷ m, the gradient of the graph (a ÷ F) equals 1 ÷ m, so the mass is 1 ÷ gradient, or F ÷ a for any point on the line.",
  ["What does a straight line through the origin mean?", "Rearrange F = m a as a = (1/m) F.", "How do you get m from the gradient?"],
  "a ∝ F; gradient = 1/m; m = 1/gradient",
  ["It shows acceleration is proportional to force; the gradient is 1/m, so the mass is 1 ÷ gradient", "a is directly proportional to F, and m = F ÷ a from any point on the line"],
  ["It shows mass increases with force", "The mass is equal to the gradient"], min_points=2,
  pitfalls=[PF(["mass is equal to the gradient", "mass = gradient"], "The gradient of a against F is 1/m, so m = 1 ÷ gradient.")])

Q("w4b_tow_truck", 5, "4c", "A truck tows a broken-down car with a rope, and both speed up together. Explain the forces on the car and why it accelerates.",
  [P("the rope pulls the car forward with a tension force", ["tension", "rope pulls", "pull of the rope", "forward pull"]),
   P("friction / air resistance act backwards on the car", ["friction", "air resistance", "backwards", "resistive"]),
   P("tension is greater than the resistive forces, so there is a forward resultant force and the car accelerates (F = m a)", ["greater than", "forward resultant", "resultant force forward", "f = ma", "f = m a", "accelerates"])],
  "The rope pulls the car forward with a tension force, while friction and air resistance act backwards on it. The tension is greater than these resistive forces, so there is a forward resultant force on the car, and by F = m a the car accelerates.",
  ["What forward force acts on the car?", "What backward forces act on it?", "Compare them to explain the acceleration."],
  "tension forward > resistive forces → forward resultant → accelerates",
  ["The rope's tension pulls it forward and is greater than the friction and air resistance, so the resultant force is forward and it accelerates", "tension forwards beats the backward resistive forces, giving F = ma"],
  ["The car's engine pushes it", "The car is pushed by the air"], min_points=2)

Q("w4b_rocket_fuel_burns", 5, "4c", "A rocket's engines give a constant thrust. Explain why the rocket's acceleration increases as it burns its fuel.",
  [P("burning fuel reduces the rocket's mass", ["mass decreases", "loses mass", "smaller mass", "less mass", "lighter"]),
   P("with the same (or larger) resultant force, a smaller mass gives a larger acceleration (a = F ÷ m)", ["a = f / m", "a = f ÷ m", "larger acceleration", "greater acceleration", "f = ma"]),
   P("its weight also decreases, so the upward resultant force increases", ["weight decreases", "less weight", "resultant force increases", "larger resultant"])],
  "As the fuel burns and is expelled, the rocket's mass decreases. Its weight also decreases, so with constant thrust the upward resultant force increases. By a = F ÷ m, a larger resultant force on a smaller mass gives a larger acceleration.",
  ["What happens to the rocket's mass as fuel is used?", "What happens to its weight and the resultant force?", "Use a = F ÷ m."],
  "mass falls; weight falls → resultant rises; a = F ÷ m increases",
  ["Burning fuel reduces the mass and the weight, so the resultant force increases and a = F ÷ m gets larger", "the rocket gets lighter, so the same thrust gives a greater acceleration"],
  ["The thrust increases", "The rocket gains mass"], min_points=2)
