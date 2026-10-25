"""Chapter 6 Energy: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 6


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


DESTROYED = PF(["energy is destroyed", "energy is lost forever", "energy disappears", "energy is used up", "destroys energy", "energy gets destroyed"],
               "Energy is never destroyed; it is transferred to other stores (often the internal store of the surroundings).")

# ---------------------------------------------------------------- L1
Q("w6b_joule", 1, "6d", "State the SI unit of energy and define it in terms of work done.",
  [P("the joule (J)", ["joule", "j"]),
   P("1 J is the work done when a force of 1 N moves its point of application 1 m in the direction of the force", ["1 n", "1 m", "one newton", "one metre", "newton metre", "force of 1 n"])],
  "The SI unit of energy is the joule (J). One joule is the work done when a force of 1 N moves its point of application through 1 m in the direction of the force.",
  ["Energy and work share a unit.", "Work = force × distance.", "Use 1 N and 1 m."],
  "joule; 1 J = 1 N × 1 m",
  ["The joule; 1 J is the work done when 1 N moves something 1 m", "joules, where one joule is a force of one newton moving one metre"],
  ["The watt", "The newton"], min_points=2)

Q("w6b_four_stores", 1, "6a", "Name four different energy stores.",
  [P("kinetic", ["kinetic"]), P("gravitational potential", ["gravitational"]), P("chemical potential", ["chemical"]),
   P("elastic potential", ["elastic"]), P("internal (thermal)", ["internal", "thermal"]), P("nuclear", ["nuclear"])],
  "Four energy stores are kinetic, gravitational potential, chemical potential and elastic potential (internal and nuclear are others).",
  ["One store is linked to motion and another to height.", "Food and batteries have one; a stretched spring has another.", "Name four."],
  "kinetic, gravitational, chemical, elastic, internal, nuclear",
  ["kinetic, gravitational potential, chemical and elastic", "chemical, nuclear, internal and kinetic"],
  ["light, sound, electricity and heat", "force, power, work and speed"], min_points=4)

Q("w6b_ke_formula", 1, "6b", "Write down the formula for kinetic energy and state the meaning and unit of each symbol.",
  [P("Ek = ½ m v²", ["½ m v2", "1/2 m v2", "half m v squared", "½mv2", "0.5 m v2", "half × mass × speed squared", "½ × m × v2", "half mass speed squared"]),
   P("m = mass in kg, v = speed in m/s, Ek in J", ["kg", "m/s", "joules", "mass", "speed"])],
  "Kinetic energy Ek = ½ m v², where m is the mass in kg, v is the speed in m/s, and Ek is in joules.",
  ["Kinetic energy depends on mass and speed.", "One of them is squared.", "Give the units."],
  "Ek = ½ m v²; kg, m/s, J",
  ["Ek = ½ m v², with mass in kg, speed in m/s and energy in J", "kinetic energy = half × mass × speed squared, in joules"],
  ["Ek = m g h", "Ek = m v"], min_points=1,
  pitfalls=[PF(["ek = mgh", "ek = m g h", "ek = mv", "ek = m v"], "Kinetic energy = ½ m v²; m g h is gravitational potential energy.")])

Q("w6b_gpe_formula", 1, "6b", "Write down the formula for the gravitational potential energy gained by an object near the Earth, with the meaning and unit of each symbol.",
  [P("Ep = m g h", ["m g h", "mgh", "mass × g × height", "mass times g times height"]),
   P("m in kg, g in N/kg, h in m, Ep in J", ["kg", "n/kg", "height", "joules", "metres"])],
  "Ep = m g h, where m is the mass in kg, g is the gravitational field strength in N/kg, h is the height gained in m, and Ep is in joules.",
  ["Ep depends on mass, field strength and height.", "Multiply them.", "Give the units."],
  "Ep = m g h; kg, N/kg, m, J",
  ["Ep = mgh, with mass in kg, g in N/kg and height in m, giving joules", "mass × g × height, in joules"],
  ["Ep = ½ m v²", "Ep = m ÷ h"], min_points=1)

Q("w6b_work_formula", 1, "6d", "Write down the formula for work done and state what each quantity means.",
  [P("work done = force × distance moved in the direction of the force", ["force × distance", "force times distance", "f × d", "force multiplied by distance", "w = fd", "w = f d"]),
   P("force in N, distance in m (in the direction of the force), work in J", ["in the direction of the force", "joules", "newtons", "metres", "direction of the force"])],
  "Work done = force × distance moved in the direction of the force. The force is in newtons, the distance in metres, and the work done in joules.",
  ["Work needs a force and a movement.", "The movement must be in a particular direction.", "Give the formula and units."],
  "W = F × d (in direction of F); J",
  ["Work = force × distance moved in the direction of the force, in joules", "W = F × d, with force in N and distance in m"],
  ["Work = force ÷ time", "Work = mass × speed"], min_points=1)

Q("w6b_power_formula", 1, "6e", "Write down the formula for power and state the unit of each quantity.",
  [P("power = energy transferred (work done) ÷ time taken", ["energy ÷ time", "energy / time", "energy divided by time", "work done ÷ time", "work ÷ time", "p = e / t", "e ÷ t"]),
   P("power in W, energy in J, time in s", ["watts", "w", "joules", "seconds"])],
  "Power = energy transferred ÷ time taken (or work done ÷ time). Power is in watts, energy in joules and time in seconds.",
  ["Power is a rate.", "Rate means 'per unit time'.", "Give the formula and units."],
  "P = E ÷ t; W, J, s",
  ["Power = energy transferred ÷ time taken, in watts", "P = E/t, with energy in joules and time in seconds"],
  ["Power = energy × time", "Power = force × distance"], min_points=1,
  pitfalls=[PF(["energy × time", "energy times time"], "Power = energy ÷ time.")])

Q("w6b_elastic_example", 1, "6a", "Give an example of an object with energy in its elastic potential store, and explain why.",
  [P("a stretched or squashed object, e.g. stretched rubber band, compressed spring, drawn bow, bungee cord", ["stretched", "compressed", "squashed", "spring", "rubber band", "bow", "bungee", "catapult", "trampoline"]),
   P("energy is stored because the object is deformed (changed shape)", ["deformed", "changed shape", "stretched", "squashed", "out of shape"])],
  "A stretched rubber band (or a compressed spring) has energy in its elastic potential store, because it has been deformed; it can release the energy when it returns to its original shape.",
  ["Which objects spring back when released?", "What has been done to them?", "Give one and explain."],
  "stretched/compressed objects; deformed",
  ["A stretched rubber band, because it has been deformed", "a compressed spring stores elastic energy because it is squashed"],
  ["A moving car", "A cup of hot tea"], min_points=1)

Q("w6b_chemical_example", 1, "6a", "Give two examples of objects that have energy in a chemical potential store.",
  [P("first example: food, fuel (petrol, coal, wood), battery", ["food", "fuel", "petrol", "coal", "wood", "battery", "gas", "oil", "candle"]),
   P("they release energy through chemical reactions", ["chemical reaction", "reactions", "burning", "react", "combustion", "digestion"])],
  "Food and batteries (also fuels such as petrol, coal and wood) have energy in a chemical potential store; the energy is released by chemical reactions such as burning or respiration.",
  ["Think of things that release energy when they react.", "What do people and cars 'run on'?", "Name two."],
  "food, fuel, batteries",
  ["Food and petrol, which release energy in chemical reactions", "a battery and coal store chemical energy"],
  ["A spring and a magnet", "A moving ball"], min_points=1)

Q("w6b_pathways", 1, "6a", "Name three pathways by which energy can be transferred from one store to another.",
  [P("mechanically (by a force doing work)", ["mechanically", "mechanical", "force doing work", "by forces"]),
   P("electrically (by an electric current)", ["electrically", "electric current", "electrical"]),
   P("by heating, or by radiation (light, sound waves)", ["heating", "radiation", "light", "sound", "waves"])],
  "Energy can be transferred mechanically (by a force doing work), electrically (by an electric current), by heating, and by radiation such as light or sound waves.",
  ["How does a moving object transfer energy?", "How does a battery transfer energy to a lamp?", "How does a hot object transfer energy?"],
  "mechanically, electrically, heating, radiation",
  ["Mechanically, electrically and by heating", "by a force doing work, by an electric current, and by light"],
  ["kinetic, chemical and nuclear", "push, pull and twist"], min_points=3)

Q("w6b_book_shelf_store", 1, "6a", "A book is lifted onto a high shelf. Name the energy store that increases and explain.",
  [P("the gravitational potential store", ["gravitational"]),
   P("because the book is higher (raised in the Earth's gravitational field)", ["higher", "raised", "height", "lifted", "above the ground"])],
  "The book's gravitational potential store increases, because it has been raised to a greater height in the Earth's gravitational field.",
  ["What changes about the book?", "Which store depends on height?", "Name and explain."],
  "gravitational potential store; height increased",
  ["Its gravitational potential store, because it is higher", "gravitational potential energy increases as it is raised"],
  ["Its kinetic store", "Its chemical store"], min_points=2)

# ---------------------------------------------------------------- L2
Q("w6b_torch_transfers", 2, "6a", "Describe the energy transfers when a battery-powered torch is switched on.",
  [P("energy from the chemical store of the battery", ["chemical"]),
   P("is transferred electrically to the lamp", ["electrically", "electric current", "electrical"]),
   P("and then by light (radiation) and heating to the surroundings' internal store", ["light", "radiation", "heating", "internal", "surroundings", "thermal"])],
  "Energy in the chemical store of the battery is transferred electrically to the lamp. The lamp then transfers energy by light (radiation) and by heating, ending up in the internal store of the surroundings.",
  ["Where is the energy stored at the start?", "How does it get to the lamp?", "How does the lamp transfer it?"],
  "chemical → electrically → light and heating → surroundings",
  ["Chemical energy in the battery is transferred electrically to the lamp, which gives out light and heats the surroundings", "from the battery's chemical store, electrically, then as light and heat"],
  ["The torch makes energy from nothing", "Light is stored in the battery"], min_points=2,
  pitfalls=[PF(["light is stored", "makes energy from nothing", "creates energy"], "Energy is stored in the battery's chemical store; light is how it leaves the lamp.")])

Q("w6b_bow_arrow", 2, "6a", "Describe the energy transfer when an archer releases a drawn bow and the arrow flies off.",
  [P("energy in the elastic potential store of the bent bow (and string)", ["elastic"]),
   P("is transferred mechanically to the kinetic store of the arrow", ["kinetic", "arrow moves", "mechanically"])],
  "Energy in the elastic potential store of the bent bow is transferred mechanically, by the string pushing on the arrow, to the kinetic store of the arrow.",
  ["Which store does the drawn bow have?", "Which store does the moving arrow have?", "Describe the transfer."],
  "elastic → kinetic",
  ["Elastic energy in the bow is transferred to the kinetic store of the arrow", "the bow's elastic potential store goes into the arrow's kinetic store"],
  ["Chemical energy in the arrow", "The bow creates energy"], min_points=2)

Q("w6b_solar_panel", 2, "6a", "Describe the energy transfer in a solar panel that powers a calculator.",
  [P("energy arrives from the Sun by radiation (light)", ["radiation", "light", "sunlight", "sun"]),
   P("and is transferred electrically to the calculator", ["electrically", "electric current", "electrical", "electricity"])],
  "Energy reaches the solar panel from the Sun by radiation (light). The panel transfers the energy electrically, by an electric current, to the calculator.",
  ["How does energy arrive from the Sun?", "How does the panel pass it on?", "Describe both."],
  "light (radiation) → electrically",
  ["Light from the Sun is transferred electrically to the calculator", "energy arrives by radiation and leaves electrically"],
  ["The calculator stores sunlight", "Kinetic energy from the Sun"], min_points=2)

Q("w6b_car_engine", 2, "6a", "Describe the energy transfers when a car's engine burns petrol to move the car.",
  [P("energy in the chemical store of the petrol (and oxygen)", ["chemical"]),
   P("is transferred mechanically to the kinetic store of the car", ["kinetic", "mechanically", "moving car", "movement"]),
   P("and much is transferred by heating to the internal store of the engine and surroundings (wasted)", ["internal", "heating", "wasted", "surroundings", "thermal", "heat"])],
  "Energy in the chemical store of the petrol is released as it burns. Some is transferred mechanically to the kinetic store of the car, while much is transferred by heating to the internal store of the engine and the surroundings, which is wasted.",
  ["Where is the energy stored at the start?", "Which store increases as the car speeds up?", "Where does the rest go?"],
  "chemical → kinetic (useful) + internal (wasted)",
  ["Chemical energy in the petrol goes to the kinetic store of the car, and a lot is wasted heating the engine and surroundings", "from the chemical store to kinetic energy, with much transferred to the internal store of the surroundings"],
  ["The engine creates energy", "Kinetic energy turns into petrol"], min_points=2, pitfalls=[DESTROYED])

Q("w6b_wasted_meaning", 2, "6c", "Explain what is meant by 'wasted energy' when a machine is used.",
  [P("energy transferred to stores that are not useful for the purpose", ["not useful", "not wanted", "unwanted", "not the useful", "does not do the job"]),
   P("usually the internal store of the surroundings, by heating (or sound)", ["internal", "heating", "surroundings", "thermal", "sound", "heat"]),
   P("it is not destroyed, but spread out and hard to use", ["not destroyed", "still exists", "spread out", "dissipated", "hard to use"])],
  "Wasted energy is energy transferred to stores that are not useful for the machine's purpose, usually the internal store of the surroundings by heating (and sound). It is not destroyed, but it is spread out and hard to use again.",
  ["Does a machine transfer all its energy usefully?", "Where does the rest usually go?", "Is it destroyed?"],
  "energy to unwanted stores (internal of surroundings); not destroyed",
  ["Energy that goes to unwanted stores, usually heating the surroundings; it is not destroyed but spread out", "energy transferred to the internal store of the surroundings, which is not useful"],
  ["Energy that is destroyed", "Energy that the machine stores for later"], min_points=2, pitfalls=[DESTROYED])

Q("w6b_holding_bag", 2, "6d", "A student holds a heavy bag still at waist height for a minute and her arms get tired. Explain why no work is done on the bag.",
  [P("work = force × distance moved in the direction of the force", ["force × distance", "force times distance", "distance moved", "w = fd"]),
   P("the bag does not move, so the distance is zero and the work done on it is zero", ["does not move", "no distance", "distance is zero", "zero distance", "not moving"]),
   P("her muscles transfer energy internally (heating), which is why she gets tired", ["muscles", "internally", "heating", "tired"])],
  "Work done = force × distance moved in the direction of the force. The bag does not move, so the distance is zero and no work is done on the bag. Her muscles still use energy internally, transferring it by heating, which is why she gets tired.",
  ["What is the formula for work?", "How far does the bag move?", "Why does she still get tired?"],
  "W = F × d; d = 0; muscles transfer energy internally",
  ["Work is force × distance and the bag does not move, so no work is done on it; her muscles still use energy", "the distance moved is zero, so the work done on the bag is zero"],
  ["A lot of work is done because the bag is heavy", "Work is force × time"], min_points=2)

Q("w6b_60w_meaning", 2, "6e", "A lamp is rated at 60 W. Explain what this means.",
  [P("it transfers 60 J of energy every second", ["60 j every second", "60 j each second", "60 joules per second", "60 j per second", "60 j/s"])],
  "A power of 60 W means the lamp transfers 60 J of energy every second.",
  ["1 W = 1 J/s.", "So 60 W = …", "Put it into words."],
  "60 J per second",
  ["It transfers 60 J of energy every second", "60 joules per second"],
  ["It uses 60 J in total", "It has a voltage of 60 V"])

Q("w6b_double_mass_ke", 2, "6b", "Explain what happens to the kinetic energy of a moving object if its mass doubles but its speed stays the same.",
  [P("the kinetic energy doubles", ["doubles", "twice", "double", "two times"]),
   P("because Ek = ½ m v², which is directly proportional to mass", ["½ m v2", "proportional to mass", "ek = ½", "directly proportional", "half m v squared"])],
  "The kinetic energy doubles, because Ek = ½ m v² is directly proportional to the mass when the speed is unchanged.",
  ["Write down the formula for Ek.", "Which quantity changes?", "How does Ek depend on it?"],
  "Ek ∝ m → doubles",
  ["It doubles, because Ek = ½ m v² is proportional to mass", "the kinetic energy is twice as much"],
  ["It quadruples", "It stays the same"], min_points=1,
  pitfalls=[PF(["quadruples", "four times"], "Only the SPEED is squared in ½ m v²; doubling the mass doubles Ek.")])

Q("w6b_lift_constant_speed", 2, "6d", "A crane lifts a crate at a steady speed. Explain why the work done by the crane on the crate equals the crate's gain in gravitational potential energy.",
  [P("at steady speed the kinetic energy does not change", ["kinetic energy does not change", "no change in kinetic", "steady speed", "same speed", "constant speed"]),
   P("so all the work done goes into the gravitational potential store (W = m g h)", ["gravitational potential", "mgh", "m g h", "all the work", "gain in ep", "gain in gravitational"]),
   P("the lifting force equals the weight, and work = weight × height", ["force equals the weight", "weight × height", "force × height", "equals the weight"])],
  "At a steady speed the crate's kinetic energy does not change, so all the work done on it goes into its gravitational potential store. The lifting force equals the weight, so work = weight × height = m g h, the gain in Ep.",
  ["Does the crate's kinetic energy change?", "Where does the work go, then?", "How big is the lifting force?"],
  "constant speed → no ΔEk → work = ΔEp = m g h",
  ["At steady speed the kinetic energy is unchanged, so all the work goes into the gravitational potential store, m g h", "the force equals the weight, so the work done is weight × height = gain in Ep"],
  ["The crane creates energy", "Work is lost as speed"], min_points=2)

Q("w6b_friction_heats", 2, "6c", "When you slide a box across a rough floor, the box and floor get slightly warmer. Explain this in terms of work and energy.",
  [P("work is done against friction", ["work done against friction", "against friction", "friction does work", "overcome friction"]),
   P("this transfers energy to the internal (thermal) store of the box and floor", ["internal", "thermal", "heating", "warmer", "heat"]),
   P("the energy is not destroyed", ["not destroyed", "conserved", "still there", "transferred"])],
  "Work is done against friction as the box slides. This transfers energy to the internal (thermal) store of the box and the floor, so they warm up slightly. The energy is not destroyed, only transferred.",
  ["Which force acts between the box and the floor?", "What happens to the energy used to overcome it?", "Explain the warming."],
  "work against friction → internal store",
  ["Work is done against friction, which transfers energy to the internal store of the box and floor", "overcoming friction heats them up; the energy is transferred, not destroyed"],
  ["The floor is heated by the room", "Friction creates energy"], min_points=2, pitfalls=[DESTROYED])

# ---------------------------------------------------------------- L3
Q("w6b_double_speed_ke", 3, "6b", "Explain why doubling a car's speed makes its kinetic energy four times as large, and why this matters for braking.",
  [P("Ek = ½ m v², so Ek depends on the square of the speed", ["v2", "speed squared", "square of the speed", "½ m v2", "squared"]),
   P("doubling v multiplies v² by 4", ["2 squared", "4 times", "four times", "multiplies by 4", "× 4"]),
   P("the brakes must do four times as much work to stop it (larger stopping distance)", ["four times as much work", "more work", "longer braking distance", "four times the distance", "harder to stop", "braking distance"])],
  "Kinetic energy is ½ m v², so it depends on the square of the speed: doubling v makes v² four times as large, so Ek is four times as large. The brakes must do four times as much work to stop the car, so with the same braking force the braking distance is four times as long.",
  ["Which quantity is squared in the formula?", "What is 2²?", "What must the brakes do to stop the car?"],
  "Ek ∝ v²; 4× Ek; 4× work to stop",
  ["Ek = ½ m v², so doubling the speed gives four times the kinetic energy, and the brakes must do four times as much work", "speed is squared, so 2² = 4; the braking distance is longer"],
  ["Doubling speed doubles the kinetic energy", "Speed does not affect braking"], min_points=2,
  pitfalls=[PF(["doubles the kinetic energy", "kinetic energy doubles"], "Ek depends on v², so doubling v QUADRUPLES Ek.")])

Q("w6b_same_work_less_time", 3, "6e", "Two machines lift identical loads to the same height. Machine A takes 10 s and machine B takes 20 s. Compare the work done and the power of each.",
  [P("they do the same work (same load and height)", ["same work", "equal work", "same energy", "same amount of work"]),
   P("A has twice the power of B", ["twice the power", "double the power", "a has more power", "a is more powerful", "greater power"]),
   P("because power = work ÷ time, and A takes half the time", ["work ÷ time", "energy ÷ time", "half the time", "less time", "p = w / t"])],
  "Both machines do the same work, because they lift the same load through the same height. Power = work ÷ time, and A takes half as long, so A has twice the power of B.",
  ["Does the work depend on how long it takes?", "How is power calculated?", "Compare the times."],
  "same work; A twice the power",
  ["They do the same work, but A has twice the power because it takes half the time", "same energy transferred, and power = work ÷ time, so A is more powerful"],
  ["A does twice as much work", "B has more power because it takes longer"], min_points=2)

Q("w6b_skate_ramp", 3, "6c", "A skateboarder starts from rest at the top of one side of a U-shaped ramp. Explain why she does not quite reach the same height on the other side.",
  [P("Ep at the top is transferred to Ek at the bottom and back to Ep", ["gravitational", "kinetic", "transferred"]),
   P("some energy is transferred to the internal store of the surroundings by friction and air resistance (and sound)", ["friction", "air resistance", "internal", "heating", "sound", "surroundings"]),
   P("so less energy is left for the gravitational store on the other side, so she reaches a lower height", ["less energy", "lower height", "not as high", "less gravitational", "cannot reach"])],
  "Her gravitational potential energy is transferred to kinetic energy on the way down and back to gravitational potential energy on the way up. But friction and air resistance transfer some energy to the internal store of the surroundings (and some as sound), so less energy is left to store gravitationally, and she cannot reach the same height.",
  ["Describe the energy transfers as she goes down and up.", "What forces act against her motion?", "What happens to the energy they transfer?"],
  "Ep → Ek → Ep, minus losses to friction/air resistance",
  ["Some energy is transferred to the surroundings by friction and air resistance, so there is less gravitational potential energy on the other side and she reaches a lower height", "friction heats the surroundings, so less energy is left to climb as high"],
  ["Gravity is weaker on the other side", "Energy is destroyed at the bottom"], min_points=2, pitfalls=[DESTROYED])

Q("w6b_spring_toy", 3, "6a", "A toy is launched upwards by a compressed spring. Describe the energy transfers from release until the toy reaches its highest point.",
  [P("elastic potential store of the compressed spring", ["elastic"]),
   P("to the kinetic store of the toy as it is launched", ["kinetic"]),
   P("then to the gravitational potential store as it rises and slows", ["gravitational"])],
  "Energy in the elastic potential store of the compressed spring is transferred to the kinetic store of the toy as it is launched. As the toy rises and slows down, its kinetic energy is transferred to its gravitational potential store, which is greatest at the highest point (some is also transferred to the surroundings by air resistance).",
  ["Which store does the compressed spring have?", "What happens as the toy shoots up?", "And as it rises and slows?"],
  "elastic → kinetic → gravitational",
  ["Elastic energy in the spring becomes kinetic energy of the toy, which then becomes gravitational potential energy as it rises", "elastic → kinetic → gravitational potential"],
  ["Chemical energy becomes light", "The toy gains mass as it rises"], min_points=3)

Q("w6b_hydro", 3, "6a", "Describe the energy transfers in a hydroelectric power station, from water stored behind a dam to electricity.",
  [P("water stored high up has energy in its gravitational potential store", ["gravitational"]),
   P("as it falls, this is transferred to the kinetic store of the water, which turns the turbines", ["kinetic", "turbine", "falls"]),
   P("the generator transfers energy electrically", ["electrically", "electrical", "generator", "electricity"])],
  "Water held high behind the dam has energy in its gravitational potential store. As it flows down, this is transferred to the kinetic store of the water, which turns the turbines. The generators then transfer the energy electrically to the grid.",
  ["Where is the energy stored before the water falls?", "What happens to the water as it falls?", "How is the energy passed on to homes?"],
  "gravitational → kinetic → turbine → electrically",
  ["The water's gravitational potential energy becomes kinetic energy, which turns the turbine, and the generator transfers it electrically", "gravitational → kinetic → electrical energy"],
  ["The dam stores electricity", "Chemical energy in the water"], min_points=2)

Q("w6b_brakes_hot", 3, "6c", "After a long downhill run, a cyclist notices her brakes are hot. Explain why.",
  [P("the brakes do work against friction to keep her speed down", ["work against friction", "friction", "brakes do work"]),
   P("this transfers energy from her gravitational (and kinetic) store", ["gravitational", "kinetic"]),
   P("to the internal (thermal) store of the brakes, which become hot", ["internal", "thermal", "heating", "hot"])],
  "As she descends, her gravitational potential energy would otherwise become kinetic energy. The brakes do work against friction to keep her speed down, transferring this energy to the internal store of the brake pads and wheel rims, so they become hot.",
  ["Where does her energy come from as she goes downhill?", "What do the brakes do?", "Where does that energy end up?"],
  "gravitational/kinetic → work against friction → internal store of brakes",
  ["Her gravitational potential energy is transferred by friction in the brakes to their internal store, so they get hot", "the brakes do work against friction, heating them up"],
  ["The sun heats the brakes", "The brakes create heat from nothing"], min_points=2)

Q("w6b_dissipated", 3, "6c", "A ball bounces lower each time until it stops. Explain where its energy has gone, and why that energy is no longer useful.",
  [P("each bounce transfers some energy to the internal store of the ball, floor and air (and sound)", ["internal", "heating", "sound", "surroundings", "thermal"]),
   P("the total energy is conserved (not destroyed)", ["not destroyed", "conserved", "still exists", "total energy"]),
   P("but it is spread out (dissipated) in the surroundings, so it is hard to use", ["spread out", "dissipated", "hard to use", "not useful", "cannot be used"])],
  "With each bounce, some energy is transferred to the internal store of the ball, the floor and the air, and some as sound. The total energy is conserved, but it has been spread out (dissipated) as a tiny warming of the surroundings, so it is no longer in a useful form.",
  ["Where does energy go in each bounce?", "Is it destroyed?", "Why can it not be used again?"],
  "transferred to internal store of surroundings and sound; conserved but dissipated",
  ["Energy is transferred to the internal store of the floor and air and as sound; it is not destroyed but spread out, so it is not useful", "the energy is dissipated to the surroundings, so it still exists but cannot be used"],
  ["The energy is destroyed", "It goes back into the ball's chemical store"], min_points=2, pitfalls=[DESTROYED])

Q("w6b_ramp_vs_lift", 3, "6d", "A box can be lifted straight up onto a platform, or pushed up a smooth ramp to the same height. Compare the force needed and the work done.",
  [P("the ramp needs a smaller force", ["smaller force", "less force", "less effort", "easier"]),
   P("but the force must act over a longer distance", ["longer distance", "further", "greater distance", "longer path"]),
   P("the work done is the same (equal to m g h) if the ramp is smooth", ["same work", "equal work", "mgh", "m g h", "same energy"])],
  "Pushing up the ramp needs a smaller force, but the force has to act over a longer distance. If the ramp is smooth, the work done is the same either way, because it equals the gain in gravitational potential energy, m g h.",
  ["Which way needs a smaller force?", "Which way needs a longer distance?", "Compare the work done, which equals the gain in Ep."],
  "ramp: smaller force, longer distance, same work (m g h)",
  ["The ramp needs a smaller force over a longer distance, but the work done is the same, mgh", "less force on the ramp, more distance, same work"],
  ["The ramp needs less work", "Lifting needs a smaller force"], min_points=2,
  pitfalls=[PF(["ramp needs less work", "less work on the ramp"], "On a smooth ramp the WORK is the same; only the force is smaller.")])

Q("w6b_hairdryer_power", 3, "6e", "Two hairdryers are rated at 2000 W and 1000 W. Explain the difference in what they do.",
  [P("the 2000 W dryer transfers twice as much energy per second", ["twice as much energy per second", "2000 j per second", "more energy per second", "twice as much energy each second", "transfers energy faster"]),
   P("so it heats/dries hair faster (in a given time it transfers more energy)", ["faster", "quicker", "more energy in the same time", "dries faster"])],
  "The 2000 W hairdryer transfers 2000 J of energy every second, twice as much as the 1000 W one. In a given time it transfers twice as much energy, so it heats the air and dries hair faster.",
  ["What does the power rating tell you?", "Compare the energy per second.", "What is the practical difference?"],
  "2000 J/s vs 1000 J/s; faster",
  ["The 2000 W dryer transfers twice as much energy per second, so it dries hair faster", "it gives 2000 J each second instead of 1000 J, so it works quicker"],
  ["The 2000 W dryer lasts twice as long", "They transfer the same energy per second"], min_points=1)

Q("w6b_speed_independent_mass", 3, "6c", "A heavy ball and a light ball are dropped from the same height (no air resistance). Use energy to explain why they reach the same speed at the ground.",
  [P("Ep lost = Ek gained: m g h = ½ m v²", ["m g h = ½ m v2", "mgh = ½mv2", "potential energy becomes kinetic", "ep = ek", "gravitational to kinetic"]),
   P("the mass cancels, so v = √(2 g h), the same for both", ["mass cancels", "mass cancels out", "does not depend on mass", "same for both", "independent of mass", "v = √"])],
  "With no air resistance, the gravitational potential energy lost equals the kinetic energy gained: m g h = ½ m v². The mass cancels, giving v = √(2 g h), so both balls reach the same speed at the ground.",
  ["Write down the energy conversion as each ball falls.", "What happens to the mass in the equation?", "What is the final speed?"],
  "m g h = ½ m v²; mass cancels",
  ["mgh = ½mv², so the mass cancels and v = √(2gh) is the same for both", "potential energy becomes kinetic energy, and the speed does not depend on mass"],
  ["The heavier ball is faster because it has more energy", "The lighter ball is faster"], min_points=2)

# ---------------------------------------------------------------- L4
Q("w6b_wind_turbine", 4, "6c", "Describe the energy transfers in a wind turbine and explain why not all the wind's energy becomes electrical energy.",
  [P("kinetic store of the moving air", ["kinetic"]),
   P("turns the blades and generator, transferring energy electrically", ["electrically", "electrical", "generator", "electricity"]),
   P("some energy is wasted: friction in moving parts heats them, and some as sound; much air passes without slowing", ["friction", "heating", "sound", "wasted", "internal", "surroundings", "passes through"])],
  "The kinetic store of the moving air turns the blades, which drive a generator that transfers energy electrically. Not all the wind's energy becomes electrical energy: some is transferred by heating in the gearbox and bearings due to friction, some as sound, and much of the air passes through without giving up all its kinetic energy.",
  ["Which store does the wind have?", "What does the generator do?", "Where is energy wasted?"],
  "kinetic → electrically; friction, sound, air not fully slowed",
  ["The wind's kinetic energy turns the turbine and generator, transferring energy electrically; some is wasted as heating by friction and as sound", "kinetic → electrical, with losses from friction in moving parts and sound"],
  ["The turbine creates energy from nothing", "All the wind energy becomes electricity"], min_points=2, pitfalls=[DESTROYED])

Q("w6b_trampoline", 4, "6a", "Describe the energy transfers as a child bounces on a trampoline, from the top of one bounce, down to the lowest point, and back up.",
  [P("at the top: gravitational potential store (maximum)", ["gravitational"]),
   P("falling: gravitational → kinetic", ["kinetic"]),
   P("at the lowest point the trampoline is stretched: kinetic → elastic potential, then back to kinetic and gravitational", ["elastic"])],
  "At the top of a bounce, the child's energy is mainly in the gravitational potential store. As she falls, it is transferred to her kinetic store. On landing, the trampoline stretches and the kinetic energy is transferred to its elastic potential store, which is greatest at the lowest point. The trampoline then springs back, transferring the energy back to kinetic and then gravitational potential energy as she rises (with some lost to the surroundings).",
  ["What store is largest at the top?", "And while falling?", "What stores energy at the lowest point?"],
  "gravitational → kinetic → elastic → kinetic → gravitational",
  ["Gravitational potential energy becomes kinetic energy as she falls, then elastic energy in the stretched trampoline, then back to kinetic and gravitational", "gravitational → kinetic → elastic and back again"],
  ["Chemical energy in the trampoline", "Energy is destroyed at the bottom"], min_points=3, pitfalls=[DESTROYED])

Q("w6b_measure_power_stairs", 4, "6e", "Describe how to measure a student's useful power when running up a flight of stairs.",
  [P("measure the student's mass with a balance/scales (weight = m g)", ["mass", "weigh", "balance", "scales", "weight"]),
   P("measure the vertical height of the stairs with a metre rule / tape", ["vertical height", "height of the stairs", "measure the height", "tape measure", "metre rule"]),
   P("time the run with a stopwatch; power = m g h ÷ t", ["stopwatch", "time", "mgh ÷ t", "m g h ÷ t", "energy ÷ time", "work ÷ time", "divide by the time"])],
  "Measure the student's mass on bathroom scales, and the vertical height of the flight of stairs with a tape measure. Time the student running up with a stopwatch. The useful work done is m g h, so the power = m g h ÷ t.",
  ["What energy does the student gain?", "Which three measurements do you need?", "How do you combine them?"],
  "measure m, h (vertical), t; P = m g h ÷ t",
  ["Measure the mass, the vertical height of the stairs and the time with a stopwatch, then power = mgh ÷ t", "weigh the student, measure the height and time the run; divide m g h by the time"],
  ["Measure the length of the staircase and the student's height", "Count the steps only"], min_points=2)

Q("w6b_car_uphill", 4, "6c", "A car uses more fuel driving up a hill than along a flat road at the same speed. Explain why in terms of energy.",
  [P("going uphill, the car gains gravitational potential energy", ["gravitational", "height", "gains potential"]),
   P("this extra energy comes from the chemical store of the fuel", ["chemical", "fuel", "petrol"]),
   P("as well as the energy needed to overcome friction and air resistance (same as on the flat)", ["friction", "air resistance", "as well as", "in addition"])],
  "On both roads the engine must do work against friction and air resistance. Going uphill, the car also gains gravitational potential energy as it rises. This extra energy must come from the chemical store of the fuel, so more fuel is used.",
  ["Which store increases when the car goes uphill?", "Where must that energy come from?", "What other work is done on both roads?"],
  "extra gravitational PE from fuel's chemical store",
  ["Going uphill the car gains gravitational potential energy, which must come from the chemical store of the fuel as well as overcoming friction", "the extra height means extra Ep, so more fuel is burned"],
  ["The engine is less efficient on hills", "The car gets heavier"], min_points=2)

Q("w6b_pendulum_stops", 4, "6c", "A pendulum is left swinging and eventually stops. Explain what happens to its energy.",
  [P("on each swing, air resistance and friction at the pivot do work", ["air resistance", "friction", "pivot"]),
   P("transferring energy to the internal store of the air and pivot (surroundings)", ["internal", "heating", "surroundings", "thermal", "warms"]),
   P("so the pendulum's total (Ep + Ek) gradually decreases until it stops; energy is conserved overall", ["decreases", "gradually", "conserved", "not destroyed", "swings get smaller"])],
  "On each swing, air resistance and friction at the pivot transfer some of the pendulum's energy to the internal store of the air and the pivot. The pendulum's total energy gradually decreases, so the swings get smaller until it stops. The energy is not destroyed; it is dissipated into the surroundings.",
  ["What forces oppose the pendulum's motion?", "Where does the energy they transfer go?", "Is energy destroyed?"],
  "air resistance and pivot friction → internal store of surroundings",
  ["Air resistance and friction at the pivot transfer energy to the surroundings, so the swings get smaller; the energy is not destroyed", "the energy is gradually transferred to the internal store of the air, so it stops"],
  ["The energy is destroyed", "Gravity runs out"], min_points=2, pitfalls=[DESTROYED, PF(["gravity runs out", "runs out of gravity"], "Gravity does not run out; energy is transferred to the surroundings.")])

Q("w6b_freewheel_downhill", 4, "6c", "A cyclist freewheels (without pedalling) down a long hill and speeds up. Describe the energy transfers, and explain why her final speed is less than if there were no friction.",
  [P("gravitational potential store decreases as she descends", ["gravitational potential store decreases", "gravitational potential energy decreases", "gravitational decreases", "loses gravitational", "ep decreases", "potential energy decreases", "gravitational potential energy becomes kinetic", "gravitational to kinetic"]),
   P("kinetic store increases as she speeds up", ["kinetic store increases", "kinetic energy increases", "gains kinetic", "ek increases", "becomes kinetic"]),
   P("some energy is transferred to the surroundings by air resistance and friction, so less becomes kinetic", ["air resistance", "friction", "surroundings", "less becomes kinetic", "wasted", "internal"])],
  "As she descends, her gravitational potential store decreases and her kinetic store increases, so she speeds up. Some of the energy is transferred to the internal store of the surroundings by air resistance and friction, so not all the lost gravitational energy becomes kinetic energy; her final speed is less than it would be without friction.",
  ["Which store decreases as she goes down?", "Which store increases?", "Where else does some energy go?"],
  "gravitational → kinetic, minus losses",
  ["Her gravitational potential energy becomes kinetic energy, but some is transferred to the surroundings by air resistance and friction, so her speed is lower", "Ep decreases and Ek increases; air resistance wastes some energy"],
  ["She gains chemical energy", "Kinetic energy becomes gravitational"], min_points=2,
  pitfalls=[PF(["kinetic energy becomes gravitational", "kinetic becomes gravitational"], "Going DOWNHILL, gravitational potential energy becomes kinetic energy, not the other way round.")])

Q("w6b_work_to_ke", 4, "6d", "A student pushes a trolley from rest along a smooth bench with a constant force. Explain how the work done is related to the trolley's kinetic energy.",
  [P("work done on the trolley = force × distance", ["force × distance", "force times distance", "w = fd", "work done"]),
   P("on a smooth bench no energy is wasted, so all the work done becomes kinetic energy", ["all the work", "becomes kinetic", "kinetic energy", "no friction", "smooth"]),
   P("so ½ m v² = F × d", ["½ m v2 = f", "½mv2", "work done = kinetic", "equals the kinetic energy", "equal to the gain in kinetic"])],
  "The work done on the trolley is force × distance. On a smooth bench no energy is transferred by friction, so all the work done goes into the trolley's kinetic store: the work done equals the gain in kinetic energy, F × d = ½ m v².",
  ["How is work done calculated?", "Is any energy wasted on a smooth bench?", "Where does the work done go?"],
  "W = F d = gain in Ek (no friction)",
  ["The work done, force × distance, all becomes kinetic energy because there is no friction, so F × d = ½ m v²", "on a smooth bench, the work done equals the gain in kinetic energy"],
  ["The work done becomes gravitational energy", "The trolley creates its own energy"], min_points=2)

Q("w6b_weightlifter_power", 4, "6e", "Two weightlifters lift identical barbells to the same height. One lifts quickly, the other slowly. Compare the work they do and their power.",
  [P("they do the same work (same weight, same height: m g h)", ["same work", "equal work", "same energy", "mgh", "m g h"]),
   P("the quicker lifter has the greater power", ["quicker", "faster", "greater power", "more power", "more powerful"]),
   P("because power = work ÷ time and the time is shorter", ["work ÷ time", "energy ÷ time", "shorter time", "less time", "p = w / t"])],
  "Both do the same work, m g h, because the barbells and heights are identical. Power = work ÷ time, so the weightlifter who lifts quickly, taking less time, develops the greater power.",
  ["Does the work depend on how fast you lift?", "How is power related to time?", "Compare."],
  "same work; faster lifter more power",
  ["They do the same work, mgh, but the quicker lifter has more power because power = work ÷ time", "same energy transferred; less time means greater power"],
  ["The slower lifter does more work", "The quicker lifter does more work"], min_points=2)

Q("w6b_speed_limits_energy", 4, "6b", "Use ideas about kinetic energy and work to explain why a small increase in speed near a school greatly increases the danger.",
  [P("kinetic energy = ½ m v², so it increases with the square of the speed", ["v2", "speed squared", "square of the speed", "½ m v2"]),
   P("the brakes must do more work (F × d) to remove this energy", ["work", "brakes", "f × d", "braking force × distance"]),
   P("so the braking distance increases a lot (and a collision transfers more energy)", ["braking distance", "longer to stop", "further to stop", "more energy in a collision", "more damage"])],
  "Kinetic energy = ½ m v², so it increases with the square of the speed: a small rise in speed gives a much larger kinetic energy. To stop, the brakes must do work (braking force × distance) equal to this energy, so the braking distance increases a lot, and any collision transfers far more energy, causing more harm.",
  ["How does Ek depend on speed?", "How do the brakes remove kinetic energy?", "What does that mean for stopping distance?"],
  "Ek ∝ v²; brakes do work F × d; much longer braking distance",
  ["Kinetic energy depends on speed squared, so the brakes must do much more work and the braking distance becomes much longer", "½ m v² rises quickly with speed, so the car needs a longer distance to stop"],
  ["Faster cars are lighter", "Speed does not affect stopping"], min_points=2)

Q("w6b_heavier_more_ke", 4, "6b", "A heavy ball and a light ball are dropped from the same height and land at the same speed. Explain which has more kinetic energy on landing.",
  [P("the heavy ball has more kinetic energy", ["heavy ball", "heavier ball", "heavier one"]),
   P("Ek = ½ m v²: same v but larger m", ["½ m v2", "larger mass", "more mass", "same speed", "proportional to mass"]),
   P("it also had more gravitational potential energy (m g h) at the start", ["more gravitational", "mgh", "m g h", "more potential energy"])],
  "The heavy ball has more kinetic energy. Both land at the same speed, but Ek = ½ m v² is larger for the larger mass. This is because the heavy ball also started with more gravitational potential energy (m g h is larger for larger m).",
  ["Do they land at the same speed?", "How does Ek depend on mass?", "Where did the extra Ek come from?"],
  "heavy ball: same v, larger m → more Ek (more m g h at start)",
  ["The heavy ball, because Ek = ½ m v² and it has more mass at the same speed; it also had more gravitational potential energy at the start", "the heavier one has more kinetic energy since its mass is larger"],
  ["The light ball, because it is faster", "They have the same kinetic energy"], min_points=2)

# ---------------------------------------------------------------- L5
Q("w6b_running_out_claim", 5, "6c", "People often say 'we are running out of energy', yet energy is always conserved. Evaluate this statement.",
  [P("energy is conserved: it cannot be destroyed (or created)", ["conserved", "cannot be destroyed", "not destroyed", "cannot be created"]),
   P("what is running out is useful energy stores such as fossil fuels (chemical stores)", ["fossil fuels", "fuel", "useful", "chemical store", "coal", "oil"]),
   P("used energy ends up dissipated in the surroundings, where it is hard to use", ["dissipated", "spread out", "surroundings", "hard to use", "not useful", "internal"])],
  "The total amount of energy is conserved, so energy itself is not running out. What is running out is useful energy stores, such as the chemical stores of fossil fuels. When we use them, the energy ends up dissipated as a small warming of the surroundings, where it is spread out and very hard to use again.",
  ["Can energy be destroyed?", "What do people really mean is running out?", "Where does used energy end up?"],
  "energy conserved; useful stores (fuels) running out; energy dissipated",
  ["Energy is conserved, but useful stores like fossil fuels are running out; used energy is dissipated to the surroundings where it is hard to use", "energy is not destroyed, it spreads out; it is the fuels that run out"],
  ["Correct, energy is being destroyed", "Correct, the Sun is using up all the energy"], min_points=2, pitfalls=[DESTROYED])

Q("w6b_measure_ke_trolley", 5, "6b", "Design an experiment to find the kinetic energy of a trolley rolling along a bench.",
  [P("measure the trolley's mass with a balance", ["balance", "mass", "weigh"]),
   P("measure its speed, e.g. with a light gate and a card of known length (speed = length ÷ time)", ["light gate", "card", "speed = length", "length ÷ time", "ticker tape", "measure the speed"]),
   P("calculate Ek = ½ m v² (repeat and average)", ["½ m v2", "half m v squared", "ek = ½", "½mv2", "repeat"])],
  "Measure the trolley's mass on a balance. Fix a card of known length to it and let it pass through a light gate; the timer gives the time for the card to pass, so speed = card length ÷ time. Calculate Ek = ½ m v², and repeat several times to find an average.",
  ["Which two quantities does Ek depend on?", "How can you measure each?", "Combine them."],
  "mass by balance; speed by light gate; Ek = ½ m v²",
  ["Weigh the trolley, find its speed with a light gate and card, and calculate ½ m v²", "measure the mass and the speed, then kinetic energy = half m v squared"],
  ["Measure its height and use mgh", "Measure the length of the bench"], min_points=2)

Q("w6b_ramp_less_work_claim", 5, "6d", "A student says: 'Using a ramp to load a heavy box onto a truck means less work is done.' Evaluate this claim.",
  [P("wrong (for a smooth ramp): the work done equals the gain in gravitational potential energy, m g h, either way", ["wrong", "same work", "mgh", "m g h", "equal work", "not less work"]),
   P("the ramp reduces the FORCE needed, but the distance moved is longer", ["smaller force", "less force", "longer distance", "further", "reduces the force"]),
   P("on a real ramp, friction means slightly more work is done", ["friction", "more work", "slightly more"])],
  "The claim is wrong. Whether the box is lifted directly or pushed up a smooth ramp, the work done equals its gain in gravitational potential energy, m g h. The ramp reduces the force needed, but that force acts over a longer distance. On a real ramp, friction means slightly more work is done, not less.",
  ["What does the work done on the box become?", "What does the ramp change: force or work?", "What effect does friction have?"],
  "same work (m g h); smaller force × longer distance; friction adds work",
  ["Wrong: the work is the same, mgh; the ramp only reduces the force while increasing the distance, and friction makes the work slightly more", "a ramp needs less force over a longer distance, but the same work"],
  ["Correct, ramps reduce the work", "Correct, ramps create energy"], min_points=2,
  pitfalls=[PF(["ramps reduce the work", "less work with a ramp", "ramp reduces the work"], "A ramp reduces the FORCE, not the work done.")])

Q("w6b_pole_vault", 5, "6a", "Describe the energy transfers during a pole vault, from the run-up to the highest point of the jump.",
  [P("run-up: chemical store (muscles) → kinetic store of the athlete", ["chemical", "kinetic"]),
   P("the pole bends: kinetic → elastic potential store of the pole", ["elastic"]),
   P("the pole straightens: elastic → gravitational potential store as the athlete rises", ["gravitational"])],
  "During the run-up, energy from the athlete's chemical store (muscles) is transferred to her kinetic store. When the pole is planted and bends, kinetic energy is transferred to the elastic potential store of the pole. As the pole straightens, it lifts the athlete, transferring energy to her gravitational potential store, greatest at the highest point (some is lost to the surroundings).",
  ["Where does the energy for the run-up come from?", "What happens when the pole bends?", "And when it straightens?"],
  "chemical → kinetic → elastic → gravitational",
  ["Chemical energy gives kinetic energy in the run-up, the bent pole stores elastic energy, which becomes gravitational potential energy as she rises", "chemical → kinetic → elastic → gravitational potential"],
  ["Only gravitational energy is involved", "The pole creates energy"], min_points=3)

Q("w6b_dam_height_flow", 5, "6e", "Explain why a hydroelectric station with a higher dam, and with more water flowing each second, can produce more electrical power.",
  [P("Ep = m g h, so water from a greater height has more energy per kilogram", ["mgh", "m g h", "greater height", "higher", "more energy per kilogram"]),
   P("more water per second means more mass, so more energy transferred per second", ["more water per second", "more mass", "flow rate", "each second", "per second"]),
   P("power = energy ÷ time, so more energy per second means more power", ["energy ÷ time", "energy per second", "power =", "more power"])],
  "The energy the water can supply is its gravitational potential energy, m g h. A higher dam gives each kilogram of water more energy, and more water flowing each second means more mass per second. Since power = energy ÷ time, both increase the energy transferred per second, so more electrical power can be produced.",
  ["What energy does the water have behind the dam?", "How does height affect it?", "How does the flow rate affect energy per second?"],
  "Ep = m g h per kg; more mass per second; P = E ÷ t",
  ["Water from a higher dam has more energy, mgh, and more water per second means more energy each second, so more power", "power is energy per second, and a greater height and flow rate both increase it"],
  ["A higher dam has colder water", "More water makes the generator lighter"], min_points=2)

Q("w6b_power_vs_energy_claim", 5, "6e", "A student says: 'A more powerful car always has more energy than a less powerful one.' Evaluate this claim.",
  [P("the claim confuses power and energy; it is wrong (or not necessarily true)", ["wrong", "confuses", "not necessarily", "incorrect", "not the same"]),
   P("power is the rate of energy transfer (energy per second)", ["rate", "energy per second", "energy ÷ time", "how quickly", "how fast"]),
   P("a powerful car transfers energy faster; the energy it has depends on its speed, fuel etc.", ["faster", "more quickly", "depends on", "speed", "fuel"])],
  "The claim confuses power with energy and is wrong. Power is the rate of energy transfer, the energy transferred per second. A more powerful car can transfer energy more quickly, for example to accelerate faster, but how much energy it has depends on things such as its speed (kinetic energy) and the fuel in its tank.",
  ["What is the definition of power?", "Is power an amount of energy?", "Evaluate the claim."],
  "power = rate of transfer, not amount of energy",
  ["Wrong: power is the rate of energy transfer, so a powerful car transfers energy faster but does not necessarily have more energy", "it confuses power and energy; power is energy per second"],
  ["Correct, power and energy are the same thing", "Correct, powerful cars store more energy"], min_points=2)

Q("w6b_bounce_heights_trend", 5, "6c", "A ball is dropped from 2.0 m and bounces to 1.6 m, then 1.28 m, then about 1.0 m. Describe the pattern and explain it using energy.",
  [P("each bounce reaches about 80% (the same fraction) of the previous height", ["80", "same fraction", "same percentage", "four fifths", "0.8", "each bounce is lower"]),
   P("so the same fraction of the energy is lost each bounce (Ep ∝ h)", ["same fraction of the energy", "20", "fraction of its energy", "lost each bounce", "mgh"]),
   P("lost energy goes to the internal store of the ball and floor, and to sound", ["internal", "heating", "sound", "surroundings", "thermal"])],
  "Each bounce reaches about 80 % of the previous height (1.6 ÷ 2.0 = 0.8, 1.28 ÷ 1.6 = 0.8). Since Ep = m g h, the ball keeps the same fraction, 80 %, of its energy at each bounce and loses 20 %. The lost energy is transferred to the internal store of the ball and floor, and as sound.",
  ["Divide each height by the one before.", "What does that say about energy, since Ep = m g h?", "Where does the lost energy go?"],
  "constant 80% per bounce; 20% of energy lost each time to heating and sound",
  ["Each bounce is 80 % of the one before, so the same fraction of energy is lost each time, to the internal store of the ball and floor and as sound", "the height falls by the same fraction, 0.8, so 20 % of the energy is lost each bounce to heating and sound"],
  ["The ball loses the same height each time", "Energy is destroyed at each bounce"], min_points=2, pitfalls=[DESTROYED])

Q("w6b_carry_flat_claim", 5, "6d", "A student carries a box along a level corridor at constant height and speed. She says she is doing work on the box against gravity. Evaluate this.",
  [P("no work is done against gravity: the box does not move vertically", ["no work against gravity", "does not move vertically", "no vertical", "height does not change", "same height"]),
   P("the upward force (supporting the weight) is at right angles to the motion, so it does no work", ["right angles", "perpendicular", "upward force", "not in the direction"]),
   P("her muscles still use energy (heating), so she feels tired, but the box's energy is unchanged", ["muscles", "tired", "box's energy", "heating", "unchanged", "no change"])],
  "No work is done on the box against gravity, because the box does not move vertically: the upward force she exerts to support its weight is at right angles to its horizontal motion, so it does no work. The box's energy is unchanged at constant height and speed. Her muscles do use energy (transferred by heating), which is why she feels tired.",
  ["Does the box gain height?", "In which direction is the supporting force, and in which direction does the box move?", "Why does she still feel tired?"],
  "no vertical movement → no work against gravity; force ⊥ motion",
  ["No work is done against gravity because the box does not move vertically; the upward force is at right angles to the motion, though her muscles still use energy", "the height does not change so no work against gravity is done on the box"],
  ["Correct, carrying anything always does work against gravity", "Correct, the box gains potential energy"], min_points=1)

Q("w6b_two_slopes", 5, "6c", "Two smooth slopes have the same height, one steep and one gentle. Identical balls are released from the top of each. Compare their speeds at the bottom, and say what changes if the slopes are rough.",
  [P("smooth: same speed at the bottom, because both lose the same Ep (m g h) and gain the same Ek", ["same speed", "same height", "same mgh", "same kinetic energy", "equal speed"]),
   P("rough: the ball on the gentle (longer) slope is slower", ["gentle slope is slower", "longer slope", "slower on the gentle", "longer distance"]),
   P("because more work is done against friction over the longer distance", ["more work against friction", "friction over a longer distance", "more energy lost", "friction"])],
  "On smooth slopes, both balls lose the same gravitational potential energy, m g h, because the height is the same, so they gain the same kinetic energy and reach the same speed. If the slopes are rough, the ball on the gentle slope travels further, so more work is done against friction; it loses more energy and is slower at the bottom.",
  ["What decides the energy each ball gains?", "Does the slope's steepness matter without friction?", "With friction, which ball travels further?"],
  "smooth: same speed (same h); rough: gentle slope slower (longer path, more friction work)",
  ["On smooth slopes they have the same speed because the height is the same; on rough slopes the gentle one is slower because friction does more work over the longer distance", "same mgh gives the same speed, but with friction the longer slope loses more energy"],
  ["The steep slope always gives the higher speed", "The gentle slope gives the higher speed"], min_points=2)

Q("w6b_body_energy_use", 5, "6c", "A student calculates the useful work she does climbing stairs as m g h. Explain why the energy released from her food store is much greater than this.",
  [P("the body is not efficient: much of the energy is transferred by heating (body warms up, sweating)", ["heating", "warms up", "heat", "not efficient", "wasted", "sweat"]),
   P("energy is also used to keep the body working (heart, breathing) and moving limbs, not only lifting", ["heart", "breathing", "moving limbs", "other processes", "keep the body"]),
   P("energy is conserved: the extra goes to the internal store of the body and surroundings", ["conserved", "internal", "surroundings", "not destroyed"])],
  "The body is far from efficient. Only part of the energy released from the chemical store of food goes into lifting her (m g h). Much more is transferred by heating, warming her body and the surroundings, and energy is also used to keep her heart, lungs and other organs working and to swing her limbs. Energy is conserved, but most of it ends up in the internal store of her body and surroundings.",
  ["Does all the food energy go into lifting her?", "What else does the body do while climbing?", "Where does the extra energy end up?"],
  "body inefficient; heating, organs; energy ends up in internal stores",
  ["The body is not efficient, so much of the food energy heats her body and the surroundings and keeps her heart and lungs working; only part becomes mgh", "most of the energy is transferred by heating, so it is wasted rather than lifting her"],
  ["Food energy is destroyed in the body", "mgh is always equal to the food energy used"], min_points=1, pitfalls=[DESTROYED])
