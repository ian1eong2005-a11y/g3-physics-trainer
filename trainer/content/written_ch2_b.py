"""Chapter 2 Kinematics: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import figs, sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 2


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


def vt(pts, xmax, ymax, xs, ys, ylabel="speed / m/s"):
    return lambda: figs.graph(pts, xmax, ymax, xs, ys, ylabel=ylabel)


# ---------------------------------------------------------------- L1
Q("w2b_speed_units", 1, "2b", "State the SI unit of speed and give two other units that are often used for speed.",
  [P("SI unit: metre per second (m/s)", ["m/s", "metres per second", "metre per second"]),
   P("other units: km/h, cm/s, mph", ["km/h", "kilometres per hour", "cm/s", "centimetres per second", "mph", "miles per hour"])],
  "The SI unit of speed is the metre per second (m/s). Other common units are kilometres per hour (km/h) and centimetres per second (cm/s).",
  ["Speed = distance ÷ time.", "SI units of distance and time are m and s.", "Think of car speedometers for another unit."],
  "m/s; km/h, cm/s",
  ["The SI unit is m/s; km/h and cm/s are also used", "metres per second, and also kilometres per hour"],
  ["Newtons and joules", "m/s² and N"], min_points=2)

Q("w2b_define_velocity", 1, "2a", "Define velocity.",
  [P("velocity is the speed in a stated direction (rate of change of displacement)", ["speed in a given direction", "speed in a stated direction", "speed in a particular direction", "rate of change of displacement", "displacement per unit time", "displacement divided by time", "speed and direction", "speed with direction"])],
  "Velocity is the speed of an object in a stated direction; it is the rate of change of displacement, so it is a vector.",
  ["Velocity is related to speed.", "What extra information does velocity include?", "Give a one-line definition."],
  "speed in a given direction / rate of change of displacement",
  ["Velocity is speed in a given direction", "the rate of change of displacement"],
  ["Velocity is how fast something accelerates", "Velocity is the distance travelled"])

Q("w2b_uniform_accel_meaning", 1, "2c", "State what is meant by uniform acceleration.",
  [P("the velocity changes by equal amounts in equal intervals of time (constant acceleration)", ["equal amounts in equal times", "equal amounts every second", "same amount every second", "constant rate", "constant acceleration", "changes steadily", "equal changes in equal times", "same change in velocity each second"])],
  "Uniform acceleration means the velocity changes by equal amounts in equal intervals of time, so the acceleration is constant.",
  ["'Uniform' means unchanging.", "How does the velocity change from second to second?", "Describe that pattern."],
  "velocity changes by equal amounts in equal times",
  ["The velocity increases by the same amount every second", "acceleration that is constant, with equal changes in velocity in equal times"],
  ["The velocity stays the same", "The object moves in a straight line"])

Q("w2b_gradient_vt", 1, "2g", "Fig. 1 shows a speed–time graph. State what the gradient of a speed–time graph represents.",
  [P("the acceleration (rate of change of speed)", ["acceleration", "rate of change of speed", "rate of change of velocity", "change in speed per second"])],
  "The gradient of a speed–time graph represents the acceleration, the rate of change of speed.",
  ["Gradient = change in y ÷ change in x.", "Here that is change in speed ÷ time.", "What quantity is that?"],
  "gradient = acceleration",
  ["It represents the acceleration", "the rate of change of speed"],
  ["The distance travelled", "The speed"],
  pitfalls=[PF(["gradient is the distance", "gradient represents the distance", "it is the distance", "represents the distance"], "The AREA under a speed–time graph is the distance; the gradient is the acceleration.")],
  figure=vt([(0, 0), (6, 18)], 8, 20, 2, 5))

Q("w2b_rest_on_dt", 1, "2f", "Describe how a body at rest is shown on a distance–time graph, and explain why.",
  [P("a horizontal (flat) line", ["horizontal line", "flat line", "horizontal", "zero gradient", "parallel to the time axis"]),
   P("because the distance does not change as time passes", ["distance does not change", "distance stays the same", "distance is constant", "not moving", "no change in distance", "same distance"])],
  "A body at rest is shown by a horizontal line on a distance–time graph, because its distance does not change as time passes, so the gradient (speed) is zero.",
  ["If the body is at rest, does its distance change?", "What line keeps the same value as time goes on?", "Give the shape and the reason."],
  "horizontal line; distance unchanged",
  ["A horizontal line, because the distance stays the same", "a flat line since the distance does not change with time"],
  ["A straight line sloping upwards", "A vertical line"], min_points=2)

Q("w2b_rest_on_vt", 1, "2g", "Describe how a body at rest is shown on a speed–time graph.",
  [P("a horizontal line along the time axis (speed = 0)", ["along the time axis", "on the time axis", "speed is zero", "speed of zero", "zero speed", "at 0", "line at zero"])],
  "A body at rest is shown by a horizontal line along the time axis, because its speed is zero throughout.",
  ["What is the speed of a body at rest?", "Where on the speed axis is that value?", "Describe the line."],
  "horizontal line along the time axis (speed 0)",
  ["A line along the time axis, where speed is zero", "a horizontal line at zero speed"],
  ["A horizontal line above the time axis", "A line sloping upwards"],
  pitfalls=[PF(["above the time axis", "above the axis"], "A horizontal line ABOVE the axis means constant speed; at rest is speed = 0, on the axis.")])

Q("w2b_constant_speed_dt", 1, "2f", "Describe how motion at constant speed is shown on a distance–time graph.",
  [P("a straight line sloping upwards (constant gradient)", ["straight line", "constant gradient", "straight sloping", "sloping straight", "straight diagonal"])],
  "Constant speed is shown by a straight, sloping line on a distance–time graph: the distance increases by equal amounts each second, so the gradient is constant.",
  ["The gradient of a distance–time graph is the speed.", "If the speed is constant, is the gradient constant?", "What shape has a constant gradient?"],
  "straight sloping line (constant gradient)",
  ["A straight line sloping upwards", "a straight line with a constant gradient"],
  ["A curve getting steeper", "A horizontal line"])

Q("w2b_deceleration_meaning", 1, "2c", "State what is meant by deceleration.",
  [P("a decrease in velocity/speed with time (negative acceleration, slowing down)", ["slowing down", "decrease in speed", "decrease in velocity", "negative acceleration", "speed decreases", "loses speed", "reducing speed"])],
  "Deceleration is a decrease in speed (velocity) with time; it is a negative acceleration, meaning the object is slowing down.",
  ["Think of a car braking.", "What happens to its speed?", "Deceleration is the opposite of speeding up."],
  "slowing down; negative acceleration",
  ["Deceleration means slowing down, a negative acceleration", "the speed decreases with time"],
  ["Moving backwards", "Moving at a constant speed"],
  pitfalls=[PF(["moving backwards", "going backwards"], "Deceleration means slowing down, not reversing.")])

Q("w2b_displacement_def", 1, "2a", "State the difference between distance and displacement.",
  [P("distance is the total length of path travelled (scalar)", ["total length", "total path", "length of the path", "how far it has travelled", "distance is a scalar", "total distance"]),
   P("displacement is the straight-line distance from start to finish in a stated direction (vector)", ["straight line", "from start to finish", "in a direction", "displacement is a vector", "change in position", "start to end"])],
  "Distance is the total length of the path travelled; it is a scalar. Displacement is the straight-line distance from the start point to the finish point in a stated direction; it is a vector.",
  ["Does distance depend on the route taken?", "Does displacement?", "Which one has a direction?"],
  "distance = path length (scalar); displacement = straight line start to finish with direction (vector)",
  ["Distance is the total length of the path; displacement is the straight-line distance from start to finish in a direction", "distance is a scalar, displacement is a vector measured in a straight line from start to end"],
  ["They are the same", "Displacement is always larger than distance"])

Q("w2b_free_fall_meaning", 1, "2i", "State what is meant by an object in free fall near the Earth.",
  [P("it falls with only its weight (gravity) acting on it, with negligible air resistance", ["only gravity", "only its weight", "no air resistance", "negligible air resistance", "only force is gravity", "only force is its weight"]),
   P("its acceleration is constant, about 10 m/s²", ["10 m/s2", "constant acceleration", "same acceleration", "accelerates at 10"])],
  "An object is in free fall when the only force acting on it is its weight, with air resistance negligible. It then falls with a constant acceleration of about 10 m/s².",
  ["What force acts on a freely falling object?", "What about air resistance?", "What is its acceleration?"],
  "only weight acts; no air resistance; a ≈ 10 m/s²",
  ["Only gravity acts on it with no air resistance, so it accelerates at 10 m/s²", "falling with only its weight acting and a constant acceleration of 10 m/s²"],
  ["Falling at a constant speed", "Floating in space"], min_points=1,
  pitfalls=[PF(["constant speed", "steady speed"], "A freely falling object ACCELERATES; its speed is not constant.")])

# ---------------------------------------------------------------- L2
Q("w2b_steeper_faster", 2, "2f", "Fig. 1 shows a distance–time graph with two straight sections. Explain how you can tell from the graph which section is faster.",
  [P("the steeper section shows the greater speed", ["steeper", "steeper line", "larger gradient", "greater gradient", "steepest"]),
   P("because the gradient of a distance–time graph is the speed (more distance per second)", ["gradient is the speed", "gradient represents speed", "more distance per second", "more distance in the same time", "distance ÷ time"])],
  "The steeper section is faster. The gradient of a distance–time graph equals the speed, so a steeper line means more distance covered each second.",
  ["What does the gradient of a distance–time graph represent?", "Compare the steepness of the two sections.", "Link the two ideas."],
  "steeper = faster; gradient = speed",
  ["The steeper section is faster because the gradient is the speed", "steeper line, larger gradient, more distance per second, so faster"],
  ["The longer section is faster", "The section higher up the graph is faster"], min_points=2,
  figure=vt([(0, 0), (20, 40), (30, 100)], 30, 120, 5, 20, ylabel="distance / m"))

Q("w2b_vt_uniform_shape", 2, "2g", "Describe the speed–time graph of an object that accelerates uniformly from rest, and explain its shape.",
  [P("a straight line starting at the origin (zero speed at t = 0)", ["straight line", "through the origin", "starts at zero", "from the origin", "starts at 0"]),
   P("sloping upwards with a constant gradient because the acceleration is constant", ["constant gradient", "sloping upwards", "constant acceleration", "uniform acceleration", "same gradient"])],
  "The graph is a straight line starting at the origin, because the object starts from rest. It slopes upwards with a constant gradient, because the acceleration (the gradient) is constant.",
  ["Where does the line start if the object begins at rest?", "What does uniform acceleration mean for the gradient?", "Describe and explain."],
  "straight line from origin; constant gradient",
  ["A straight line through the origin sloping upwards, because the acceleration is constant", "it starts at zero and has a constant gradient since the acceleration is uniform"],
  ["A horizontal line", "A curve that gets flatter"], min_points=2)

Q("w2b_dt_curve_steeper", 2, "2f", "Fig. 1 shows a distance–time graph that curves upwards, getting steeper. Describe the motion and explain.",
  [P("the object is speeding up (accelerating)", ["speeding up", "accelerating", "speed increases", "getting faster", "increasing speed"]),
   P("because the gradient (speed) is increasing", ["gradient increases", "gradient is increasing", "getting steeper", "gets steeper", "steeper", "steeper means faster", "gradient is the speed"])],
  "The object is speeding up. The gradient of a distance–time graph is the speed, and the curve gets steeper, so the speed is increasing.",
  ["What does the gradient show?", "Is the gradient getting larger or smaller?", "What does that mean for the speed?"],
  "speeding up; gradient increasing",
  ["It is speeding up because the gradient, which is the speed, increases", "accelerating, as the line gets steeper"],
  ["It is slowing down", "It is moving at constant speed"], min_points=2,
  figure=vt([(t, 0.6 * t * t) for t in range(0, 11)], 10, 60, 2, 10, ylabel="distance / m"))

Q("w2b_vt_down_slope", 2, "2g", "Fig. 1 shows a speed–time graph. Describe the motion shown by the straight line sloping downwards to the time axis.",
  [P("the object is slowing down (decelerating) uniformly", ["decelerating", "slowing down", "uniform deceleration", "speed decreases", "losing speed"]),
   P("until it comes to rest (speed zero) where the line meets the axis", ["comes to rest", "stops", "speed becomes zero", "reaches zero", "at rest"])],
  "The object is slowing down with a uniform deceleration (constant negative gradient) until it comes to rest where the line meets the time axis.",
  ["What happens to the speed along that section?", "Is the gradient constant?", "What happens where the line meets the time axis?"],
  "uniform deceleration to rest",
  ["It is decelerating uniformly until it stops", "the speed decreases steadily and it comes to rest"],
  ["It is moving backwards", "It is speeding up"], min_points=2,
  pitfalls=[PF(["moving backwards", "going backwards", "reversing"], "A downward slope on a speed–time graph means slowing down, not reversing.")],
  figure=vt([(0, 0), (4, 12), (10, 12), (14, 0)], 14, 15, 2, 5))

Q("w2b_light_gate_speed", 2, "2b", "Describe how a light gate and a card can be used to measure the speed of a trolley.",
  [P("fix a card of known length to the trolley; it interrupts the light beam as it passes", ["card", "known length", "interrupts the beam", "blocks the beam", "breaks the beam", "length of the card"]),
   P("the timer records how long the beam is blocked", ["time the beam is blocked", "timer records", "time taken", "measures the time"]),
   P("speed = length of card ÷ time", ["length ÷ time", "length divided by time", "distance ÷ time", "length of card divided by", "speed = length"])],
  "Attach a card of known length to the trolley so that it passes through the light gate. The timer records the time for which the card blocks the light beam. The speed is the length of the card divided by this time.",
  ["What does the card do as it passes the gate?", "What does the timer measure?", "How do you get speed from these?"],
  "card of known length blocks beam; time recorded; speed = length ÷ time",
  ["A card of known length blocks the beam; the timer measures the time, and speed = length of card ÷ time", "the card interrupts the light beam and speed is the card length divided by the time it was blocked"],
  ["Put the light gate on the trolley and weigh it", "Measure the speed with a ruler only"], min_points=2)

Q("w2b_kmh_to_ms_explain", 2, "2b", "Explain how to convert a speed of 72 km/h into m/s.",
  [P("1 km = 1000 m and 1 h = 3600 s", ["1000 m", "3600 s", "1 km = 1000", "1 h = 3600", "1000 and 3600"]),
   P("so multiply by 1000 and divide by 3600 (divide by 3.6)", ["÷ 3.6", "divide by 3.6", "× 1000 ÷ 3600", "1000 / 3600", "divided by 3.6", "multiply by 1000", "divide by 3600"]),
   P("72 km/h = 20 m/s", ["20 m/s"])],
  "1 km = 1000 m and 1 h = 3600 s, so 72 km/h = 72 × 1000 m ÷ 3600 s, which is the same as dividing by 3.6: 72 km/h = 20 m/s.",
  ["Convert the km to m and the hours to s.", "That is × 1000 and ÷ 3600.", "Combine them into one factor."],
  "× 1000 ÷ 3600 = ÷ 3.6; 20 m/s",
  ["1 km is 1000 m and 1 h is 3600 s, so divide by 3.6 to get 20 m/s", "multiply by 1000, divide by 3600: 72 km/h is 20 m/s"],
  ["Multiply by 3.6 to get 259 m/s", "Divide by 60 to get 1.2 m/s"], min_points=2,
  pitfalls=[PF(["multiply by 3.6", "× 3.6", "259"], "Going from km/h to m/s, you DIVIDE by 3.6.")])

Q("w2b_bus_average_lower", 2, "2b", "A bus reaches 60 km/h on a route, but its average speed for the whole journey is only 25 km/h. Explain why.",
  [P("average speed = total distance ÷ total time", ["total distance ÷ total time", "total distance divided by total time", "total time", "whole journey"]),
   P("the bus stops at bus stops and traffic lights and travels slower at times, which adds time without much distance", ["stops", "bus stops", "traffic", "waiting", "slows down", "time stopped", "standing still"])],
  "Average speed is the total distance divided by the total time. The bus spends time stopped at bus stops and traffic lights and moving slowly in traffic, which adds to the total time without adding much distance, so its average speed is much lower than its top speed.",
  ["How is average speed calculated?", "What does a bus spend a lot of time doing?", "How does that affect the average?"],
  "average = total distance ÷ total time; stops add time",
  ["Average speed uses the total time, which includes stopping at bus stops and traffic lights", "the bus stops often, so the total distance divided by total time is lower than its top speed"],
  ["The speedometer is broken", "Average speed is always half the top speed"], min_points=2)

Q("w2b_feather_coin", 2, "2i", "A coin and a feather are dropped together in air and then in a vacuum tube. Explain what happens in each case.",
  [P("in air the feather falls more slowly because air resistance on it is large compared with its weight", ["air resistance", "feather falls slower", "feather is slower", "coin lands first", "coin hits first"]),
   P("in a vacuum they fall together with the same acceleration (about 10 m/s²)", ["same time", "together", "same acceleration", "same rate", "land together", "10 m/s2"]),
   P("because there is no air resistance in a vacuum", ["no air resistance", "no air", "vacuum has no air", "without air"])],
  "In air, the coin lands first because the air resistance on the feather is large compared with its weight, so it falls slowly. In a vacuum there is no air resistance, so both fall with the same acceleration, about 10 m/s², and land together.",
  ["What slows the feather down in air?", "What is missing in the vacuum tube?", "Describe both cases."],
  "air: feather slower (air resistance); vacuum: together, same acceleration",
  ["In air the coin lands first because of air resistance on the feather; in a vacuum there is no air so they fall together", "with air the feather falls slower; without air they have the same acceleration and land at the same time"],
  ["The coin always falls faster because it is heavier", "The feather floats in the vacuum"], min_points=2,
  pitfalls=[PF(["feather floats", "heavier objects fall faster"], "In a vacuum all objects fall with the same acceleration.")])

Q("w2b_meaning_2ms2", 2, "2c", "A car accelerates uniformly at 2 m/s². Explain what this means.",
  [P("its velocity increases by 2 m/s every second", ["2 m/s every second", "2 m/s each second", "increases by 2 m/s", "gains 2 m/s", "2 m/s per second", "2 m/s faster every second"])],
  "An acceleration of 2 m/s² means the car's velocity increases by 2 m/s every second.",
  ["Acceleration = change in velocity ÷ time.", "m/s² = (m/s) per second.", "Put that into words."],
  "velocity increases by 2 m/s every second",
  ["Its velocity increases by 2 m/s every second", "it gets 2 m/s faster each second"],
  ["It moves 2 metres every second", "Its speed is 2 m/s"],
  pitfalls=[PF(["moves 2 metres", "travels 2 m every", "2 metres every second", "speed is 2 m/s"], "2 m/s² is a change in velocity of 2 m/s every second, not a distance or a speed.")])

Q("w2b_dt_curve_flatter", 2, "2f", "Fig. 1 shows a distance–time graph that curves and becomes flatter. Describe the motion and explain.",
  [P("the object is slowing down (decelerating)", ["slowing down", "decelerating", "speed decreases", "getting slower", "losing speed"]),
   P("because the gradient (speed) is decreasing", ["gradient decreases", "getting less steep", "flatter", "gradient is decreasing", "less steep"])],
  "The object is slowing down: the gradient of a distance–time graph is the speed, and the curve becomes less steep, so the speed decreases.",
  ["What does the gradient of a distance–time graph show?", "Is the curve getting steeper or flatter?", "What does that mean?"],
  "slowing down; gradient decreasing",
  ["It is slowing down because the gradient decreases", "decelerating, as the line gets flatter and less steep"],
  ["It is speeding up", "It is moving backwards"], min_points=2,
  figure=vt([(t, 60 - 0.6 * (10 - t) ** 2) for t in range(0, 11)], 10, 60, 2, 10, ylabel="distance / m"))

# ---------------------------------------------------------------- L3
Q("w2b_distance_two_shapes", 3, "2h", "Fig. 1 shows a speed–time graph: uniform acceleration from rest, then constant speed. Explain how to find the total distance travelled.",
  [P("distance is the area under the speed–time graph", ["area under", "area beneath"]),
   P("split it into a triangle (½ × base × height) for the acceleration", ["triangle", "½ × base × height", "half base times height", "half × base × height"]),
   P("and a rectangle (speed × time) for the constant speed, then add", ["rectangle", "speed × time", "add the areas", "add them", "total area"])],
  "The distance travelled is the area under the speed–time graph. Split it into a triangle for the accelerating part (½ × base × height) and a rectangle for the constant-speed part (speed × time), then add the two areas.",
  ["What does the area under a speed–time graph give?", "What shapes make up this area?", "How do you combine them?"],
  "area under graph = triangle + rectangle",
  ["Find the area under the graph: the triangle ½ × base × height plus the rectangle speed × time", "distance is the area; add the triangle and the rectangle"],
  ["Find the gradient of the graph", "Multiply the highest speed by the total time"], min_points=2,
  figure=vt([(0, 0), (4, 12), (12, 12)], 12, 15, 2, 5))

Q("w2b_car_pulling_away", 3, "2d", "A car pulls away from traffic lights. Its acceleration is large at first and becomes smaller as it speeds up. Describe the shape of its speed–time graph and explain.",
  [P("a curve with speed increasing", ["curve", "curved", "speed increases", "rising curve"]),
   P("the gradient starts steep and becomes less steep (flatter)", ["gets less steep", "becomes flatter", "gradient decreases", "less steep", "steep at first"]),
   P("because the gradient is the acceleration, which is decreasing (non-uniform acceleration)", ["gradient is the acceleration", "acceleration decreases", "non-uniform", "acceleration gets smaller"])],
  "The graph is a curve that rises, starting steeply and becoming less steep. The gradient of a speed–time graph is the acceleration; the acceleration is large at first and decreases, so the gradient decreases, showing non-uniform acceleration.",
  ["Is the speed increasing?", "What does the gradient represent, and how does it change here?", "Describe the shape."],
  "rising curve, gradient decreasing (acceleration decreasing)",
  ["A rising curve that starts steep and gets less steep because the acceleration decreases", "the speed increases but the gradient gets flatter, as the gradient is the acceleration"],
  ["A straight line through the origin", "A horizontal line"], min_points=2)

Q("w2b_gradient_deceleration", 3, "2e", "Fig. 1 shows a speed–time graph of a car braking. Explain how to find its deceleration from the graph.",
  [P("deceleration = gradient of the line (change in speed ÷ time taken)", ["gradient", "change in speed ÷ time", "change in speed divided by time", "rise over run", "decrease in speed ÷ time"]),
   P("read the starting speed and the time taken to stop, and divide", ["starting speed", "initial speed", "time taken to stop", "read the speed", "divide the speed by the time"])],
  "The deceleration is the size of the gradient of the line. Read the initial speed and the time taken for the speed to fall to zero from the graph; deceleration = decrease in speed ÷ time taken.",
  ["What does the gradient of a speed–time graph represent?", "Which two values do you read off?", "How do you combine them?"],
  "gradient = Δspeed ÷ time",
  ["Find the gradient: the decrease in speed divided by the time taken to stop", "read the initial speed and the time to stop, then divide the speed by the time"],
  ["Find the area under the graph", "Read the highest point"], min_points=1,
  pitfalls=[PF(["area under the graph", "find the area"], "The area gives the distance; the gradient gives the (de)acceleration.")],
  figure=vt([(0, 20), (5, 0)], 6, 25, 1, 5))

Q("w2b_stopping_distance_parts", 3, "2h", "The stopping distance of a car is made up of the thinking distance and the braking distance. Explain what each part is.",
  [P("thinking distance: distance travelled during the driver's reaction time, at constant speed", ["reaction time", "before braking", "before the brakes", "while reacting", "constant speed", "driver reacts"]),
   P("braking distance: distance travelled while the brakes slow the car to rest", ["while braking", "brakes are applied", "decelerating", "slows to a stop", "after the brakes", "to stop"])],
  "The thinking distance is the distance the car travels at constant speed during the driver's reaction time, before the brakes are applied. The braking distance is the distance it travels while the brakes decelerate it to rest. Stopping distance = thinking distance + braking distance.",
  ["What happens in the moment after the driver sees a hazard?", "What happens after the brakes are pressed?", "Explain both parts."],
  "thinking: during reaction time; braking: while decelerating",
  ["Thinking distance is travelled during the reaction time before braking; braking distance is travelled while the brakes slow the car to a stop", "first the car moves at constant speed while the driver reacts, then it decelerates while braking"],
  ["Thinking distance is how far the driver can see", "Both are the same thing"], min_points=2)

Q("w2b_compare_two_vt_lines", 3, "2g", "Two cars start from rest. On a speed–time graph, car A's line is steeper than car B's. Both are straight. What can you conclude?",
  [P("both accelerate uniformly (straight lines)", ["uniform", "uniformly", "constant acceleration", "straight lines"]),
   P("car A has the greater acceleration (steeper gradient)", ["a has the greater acceleration", "a accelerates more", "a has a larger acceleration", "steeper means greater acceleration", "a has the bigger acceleration", "a accelerates faster"])],
  "Both cars accelerate uniformly, because their lines are straight. Car A's line is steeper, so it has the greater acceleration: its speed increases by more each second.",
  ["What does a straight line on a speed–time graph tell you?", "What does the steepness tell you?", "Compare A and B."],
  "both uniform; A greater acceleration",
  ["Both have uniform acceleration, and A has the greater acceleration because its line is steeper", "A accelerates more since its gradient is steeper; both are constant accelerations"],
  ["Car A travels at a constant speed", "Car B is faster"], min_points=1)

Q("w2b_trolley_ramp", 3, "2c", "A trolley is released at the top of a ramp. Describe how you could show, using measurements, that it accelerates as it rolls down.",
  [P("measure its speed at two points (e.g. with light gates, or time over equal distances)", ["light gates", "two light gates", "speed at two points", "measure the speed", "time for equal distances", "ticker tape"]),
   P("the speed further down is greater (or it takes less time for each equal section)", ["speed increases", "faster further down", "greater speed", "less time", "higher speed at the bottom", "speed is bigger"])],
  "Measure the trolley's speed at two points down the ramp, for example with two light gates. The speed at the lower gate is greater than at the upper gate, which shows that the trolley is accelerating. (Equally, it takes less time to cover each equal section further down.)",
  ["What would you need to measure to show acceleration?", "Where would you measure it?", "What result would you expect?"],
  "measure speed at two points; speed larger further down",
  ["Use two light gates to measure the speed at two points; the speed is greater further down, so it accelerates", "time it over equal distances; it takes less time further down because its speed increases"],
  ["Weigh the trolley at the top and the bottom", "Measure the length of the ramp only"], min_points=2)

Q("w2b_dt_bus_stop", 3, "2f", "Fig. 1 shows the distance–time graph of a bus. Explain what the flat section shows and how it affects the average speed.",
  [P("the flat section shows the bus is stationary (at rest), e.g. at a bus stop", ["at rest", "stationary", "stopped", "not moving", "bus stop"]),
   P("the time stopped still counts in the total time, so the average speed is lower", ["total time", "lowers the average", "average speed is lower", "reduces the average", "still counts", "included in the time"])],
  "The flat section shows the distance is not changing, so the bus is stationary, for example at a bus stop. The time spent stopped is included in the total time, so it lowers the bus's average speed for the whole journey.",
  ["What does a horizontal section on a distance–time graph show?", "Does the stopping time count towards the average?", "Explain the effect."],
  "flat = at rest; adds time, lowers average speed",
  ["The bus is stopped there, and that time counts in the total time so the average speed is lower", "it is stationary at a bus stop, which reduces the average speed because the total time is longer"],
  ["The bus is moving at constant speed", "The bus is going backwards"], min_points=2,
  figure=vt([(0, 0), (60, 600), (120, 600), (180, 1200)], 180, 1200, 30, 200, ylabel="distance / m"))

Q("w2b_dt_never_down", 3, "2f", "For an object moving in one direction, explain why its distance–time graph can never slope downwards.",
  [P("distance travelled can only increase (or stay the same) with time", ["can only increase", "only increases", "never decreases", "cannot decrease", "stays the same or increases", "keeps adding"]),
   P("a downward slope would mean the distance travelled was getting smaller, which is impossible", ["getting smaller", "would decrease", "impossible", "cannot get less", "going down would mean"])],
  "Distance travelled is the total length covered, so as time passes it can only increase or stay the same. A downward slope would mean the distance travelled was getting smaller, which is impossible; the most it can do is level off when the object stops.",
  ["Can the total distance you have walked ever go down?", "What would a downward slope mean?", "Explain."],
  "distance can only increase or stay constant",
  ["Distance travelled can only increase or stay the same, so it cannot go down", "a downward slope would mean the distance gets smaller, which is impossible"],
  ["Because objects cannot slow down", "Because the speed is always constant"], min_points=1)

Q("w2b_thinking_distance_double", 3, "2h", "Explain why doubling a car's speed doubles its thinking distance, assuming the driver's reaction time stays the same.",
  [P("thinking distance = speed × reaction time", ["speed × reaction time", "speed times reaction time", "speed multiplied by reaction time", "distance = speed × time"]),
   P("the reaction time is the same, so twice the speed gives twice the distance", ["same reaction time", "reaction time is the same", "twice the distance", "doubles", "proportional"])],
  "During the reaction time the car moves at constant speed, so thinking distance = speed × reaction time. If the reaction time is unchanged, doubling the speed doubles the thinking distance.",
  ["How does the car move during the reaction time?", "Which formula gives the thinking distance?", "What happens if one factor doubles?"],
  "thinking distance = speed × reaction time",
  ["Thinking distance is speed times reaction time, and the reaction time is the same, so it doubles", "distance = speed × time; same reaction time, twice the speed, twice the distance"],
  ["Because the brakes work less well", "Because the car is heavier"], min_points=2)

Q("w2b_g_same_all_masses", 3, "2i", "Explain why, if air resistance is negligible, a 1 kg ball and a 5 kg ball dropped together hit the ground at the same time.",
  [P("all objects near the Earth fall with the same acceleration (about 10 m/s²) when air resistance is negligible", ["same acceleration", "10 m/s2", "acceleration of free fall", "constant acceleration", "same rate"]),
   P("the acceleration does not depend on mass", ["does not depend on mass", "independent of mass", "mass does not matter", "regardless of mass", "whatever the mass"])],
  "With air resistance negligible, every object near the Earth falls with the same acceleration of free fall, about 10 m/s², whatever its mass. So the two balls gain speed at the same rate and hit the ground together.",
  ["What is the acceleration of a freely falling object?", "Does it depend on mass?", "So how do their speeds compare at each moment?"],
  "same acceleration 10 m/s²; independent of mass",
  ["They have the same acceleration of 10 m/s² because it does not depend on mass", "all objects fall at the same rate without air resistance, regardless of mass"],
  ["The heavier ball falls faster", "The lighter ball falls faster"],
  pitfalls=[PF(["heavier ball falls faster", "heavier one falls faster", "heavier objects fall faster"], "Without air resistance, all objects fall with the same acceleration.")])

# ---------------------------------------------------------------- L4
Q("w2b_vt_from_story", 4, "2g", "A train starts from rest, accelerates uniformly for 30 s, travels at constant speed for 2 minutes, then decelerates uniformly to rest in 20 s. Describe the shape of its speed–time graph.",
  [P("a straight line sloping up from the origin for the first 30 s", ["straight line up", "sloping up", "from the origin", "rises", "increasing straight line"]),
   P("a horizontal line for 2 minutes (constant speed)", ["horizontal", "flat", "constant speed", "level"]),
   P("a straight line sloping down to zero over the last 20 s, steeper than the first section", ["sloping down", "down to zero", "back to zero", "steeper", "decreases to zero"])],
  "The graph starts at the origin with a straight line sloping upwards for 30 s (uniform acceleration), then a horizontal line for 2 minutes (constant speed), then a straight line sloping down to zero speed over 20 s. The last section is steeper than the first, because the train loses the same speed in less time.",
  ["Describe each stage in turn.", "Uniform acceleration → straight sloping line; constant speed → horizontal.", "Compare the slopes of the first and last sections."],
  "straight up from origin; horizontal; straight down to zero (steeper)",
  ["A straight line up from the origin, then a horizontal line, then a steeper straight line down to zero", "rises in a straight line, stays flat at constant speed, then slopes down to zero"],
  ["A single curve", "A horizontal line all the way"], min_points=2)

Q("w2b_dt_from_vt_constant", 4, "2e", "Fig. 1 shows a speed–time graph of a cyclist moving at constant speed. Describe the distance–time graph for the same motion and explain.",
  [P("a straight line sloping upwards from the origin", ["straight line", "sloping upwards", "through the origin", "straight sloping"]),
   P("because the distance increases by the same amount every second (constant gradient = constant speed)", ["same amount every second", "same amount each second", "same distance each second", "constant gradient", "equal distances", "gradient is the speed", "constant rate"])],
  "The distance–time graph is a straight line sloping upwards from the origin. At constant speed the distance increases by the same amount every second, so the gradient, which equals the speed, is constant.",
  ["What does constant speed mean for the distance each second?", "What shape has a constant gradient?", "Describe the distance–time graph."],
  "straight sloping line; constant gradient",
  ["A straight line sloping upwards because the distance increases by the same amount each second", "a straight line with a constant gradient equal to the speed"],
  ["A horizontal line", "A curve getting steeper"], min_points=2,
  figure=vt([(0, 6), (10, 6)], 10, 10, 2, 2))

Q("w2b_vt_from_dt_curve", 4, "2e", "Fig. 1 shows a distance–time graph that gets steadily steeper (a smooth curve). Describe the speed–time graph for the same motion.",
  [P("the speed is increasing (the d–t gradient increases)", ["speed increases", "increasing speed", "speeding up", "gradient increases"]),
   P("so the speed–time graph is a line that rises (e.g. a straight line upwards if the acceleration is uniform)", ["rises", "sloping upwards", "line going up", "straight line up", "increasing line"])],
  "The distance–time graph gets steeper, so the speed is increasing. The speed–time graph is therefore a line that rises; if the curve is a steady (parabolic) curve, the speed increases uniformly and the speed–time graph is a straight line sloping upwards.",
  ["What does the gradient of the distance–time graph tell you?", "How does it change?", "How would speed against time look?"],
  "speed increasing → rising speed–time line",
  ["The speed is increasing, so the speed–time graph is a line sloping upwards", "the gradient gets steeper so the speed rises; the speed–time graph goes up"],
  ["A horizontal line", "A line sloping downwards"], min_points=2,
  figure=vt([(t, 0.5 * t * t) for t in range(0, 11)], 10, 50, 2, 10, ylabel="distance / m"))

Q("w2b_average_of_speeds", 4, "2b", "A cyclist rides 6 km at 12 km/h and then 6 km at 6 km/h. A student says the average speed is (12 + 6) ÷ 2 = 9 km/h. Explain why this is wrong and find the correct value.",
  [P("average speed = total distance ÷ total time, not the mean of the speeds", ["total distance ÷ total time", "total distance divided by total time", "not the mean", "not the average of the speeds", "total time"]),
   P("more time is spent at the slower speed (0.5 h and 1 h)", ["0.5 h", "1 h", "longer at the slower", "more time", "half an hour", "one hour"]),
   P("correct value: 12 km ÷ 1.5 h = 8 km/h", ["8 km/h", "12 ÷ 1.5", "1.5 h"])],
  "Average speed is total distance ÷ total time, not the mean of the speeds. The first 6 km takes 0.5 h and the second 6 km takes 1 h, so more time is spent at the slower speed. Average speed = 12 km ÷ 1.5 h = 8 km/h.",
  ["How long does each half of the journey take?", "Which speed does the cyclist spend longer at?", "Use total distance ÷ total time."],
  "total distance ÷ total time; 8 km/h",
  ["Average speed is total distance over total time: 12 km in 1.5 h is 8 km/h, because more time is spent at the slower speed", "you cannot average the speeds; the times are 0.5 h and 1 h, so it is 8 km/h"],
  ["The student is right, it is 9 km/h", "It is 18 km/h"], min_points=2)

Q("w2b_wet_road", 4, "2h", "On a wet road a car's brakes give a smaller deceleration. Use the idea of a speed–time graph to explain why the braking distance is longer.",
  [P("smaller deceleration means a less steep line, so it takes longer to stop", ["less steep", "takes longer to stop", "longer time", "smaller gradient", "more time to stop"]),
   P("braking distance = area under the graph (triangle), which is larger", ["area", "larger area", "bigger triangle", "area under the graph", "½ × speed × time"])],
  "With a smaller deceleration the braking section of the speed–time graph is less steep, so the car takes longer to stop from the same speed. The braking distance is the area of the triangle under this section, ½ × speed × time, which is larger because the time is longer.",
  ["What does a smaller deceleration do to the gradient?", "How does that change the stopping time?", "What represents the braking distance on the graph?"],
  "less steep, longer time, larger area",
  ["The line is less steep so it takes longer to stop, and the area under the graph, the braking distance, is larger", "smaller deceleration means more time to stop, giving a bigger triangle area"],
  ["The car is heavier when the road is wet", "The braking distance is shorter on a wet road"], min_points=2)

Q("w2b_two_light_gates_accel", 4, "2c", "Describe how to measure the acceleration of a trolley using two light gates, a card on the trolley and a timer.",
  [P("measure the speed at each gate (card length ÷ time the beam is blocked)", ["speed at each gate", "card length ÷ time", "length of the card divided by", "speed at the first gate", "speed at the second gate"]),
   P("measure the time taken to travel between the two gates", ["time between the gates", "time taken between", "time to travel from one gate", "time between"]),
   P("acceleration = (final speed − initial speed) ÷ time between gates", ["change in speed ÷ time", "change in speed divided by time", "(v − u) ÷ t", "difference in speed divided by", "final speed minus initial speed"])],
  "Find the speed at each light gate from the length of the card divided by the time for which it blocks the beam. Also measure the time taken for the trolley to travel from the first gate to the second. Acceleration = (speed at second gate − speed at first gate) ÷ time between the gates.",
  ["What can each light gate measure?", "What other time is needed?", "How do you calculate the acceleration?"],
  "speed at each gate; time between; a = Δv ÷ t",
  ["Find the speed at each gate using card length divided by time, measure the time between the gates, then acceleration = change in speed ÷ time", "measure the speed at the first gate and the second gate and the time between them; a = (v − u) ÷ t"],
  ["Weigh the trolley and divide by the time", "Measure the length of the track only"], min_points=2)

Q("w2b_ticker_constant", 4, "2b", "A ticker-timer makes 50 dots per second on a tape pulled by a trolley. The dots are equally spaced, 2 cm apart. Explain what this shows and how to find the speed.",
  [P("equal spacing means constant speed", ["constant speed", "equal spacing", "evenly spaced", "same speed", "steady speed", "not accelerating"]),
   P("the time between dots is 1/50 s = 0.02 s", ["0.02 s", "1/50", "fiftieth of a second", "1 / 50"]),
   P("speed = 2 cm ÷ 0.02 s = 100 cm/s (1 m/s)", ["100 cm/s", "1 m/s", "2 ÷ 0.02", "distance ÷ time"])],
  "Equally spaced dots show the trolley moved equal distances in equal times, so its speed was constant. The time between dots is 1/50 s = 0.02 s, so the speed = 2 cm ÷ 0.02 s = 100 cm/s = 1 m/s.",
  ["What does equal spacing tell you?", "How long is the gap between dots?", "speed = distance ÷ time."],
  "equal spacing = constant speed; 0.02 s; 100 cm/s",
  ["Equal spacing means constant speed; each gap is 0.02 s so the speed is 2 cm ÷ 0.02 s = 100 cm/s", "the trolley moves at a steady speed of 1 m/s because 2 cm takes 1/50 s"],
  ["The trolley is accelerating", "The speed is 2 cm/s"], min_points=2)

Q("w2b_average_speed_camera", 4, "2b", "Average-speed cameras record when a car passes two points 5 km apart. Explain how the average speed is found and why a driver cannot simply slow down just at the cameras.",
  [P("average speed = distance between cameras ÷ time taken between them", ["distance ÷ time", "5 km ÷ time", "5 km by the time", "distance between the cameras divided by", "divided by the time", "time between the cameras", "total distance ÷ total time"]),
   P("speeding anywhere between the cameras shortens the time, raising the average speed", ["shorter time", "less time", "time is short", "raises the average", "higher average", "anywhere between", "whole distance", "does not help"])],
  "The system records the time taken to travel the 5 km between the cameras; average speed = 5 km ÷ that time. If the driver speeds anywhere between the cameras, the time taken is shorter, so the average speed is higher, even if the car slows down when passing each camera.",
  ["What two pieces of information does the system have?", "How is average speed calculated?", "What happens to the time if you speed between cameras?"],
  "average speed = 5 km ÷ time between cameras",
  ["Average speed is the distance between cameras divided by the time; speeding in between makes the time shorter so the average is higher", "it divides 5 km by the time taken, so slowing at the cameras does not help if the total time is short"],
  ["The camera measures the instantaneous speed only", "It uses the car's weight"], min_points=2)

Q("w2b_ball_slope_then_floor", 4, "2g", "A ball rolls down a slope, speeding up uniformly, then rolls along a rough floor, slowing down uniformly until it stops. Describe its speed–time graph.",
  [P("a straight line sloping upwards while on the slope", ["sloping upwards", "straight line up", "rises", "increases uniformly"]),
   P("then a straight line sloping down to zero while on the floor", ["sloping down", "down to zero", "decreases to zero", "back to zero", "falls to zero"]),
   P("the peak is where it reaches the bottom of the slope (maximum speed)", ["peak", "maximum speed", "highest point", "bottom of the slope", "top speed"])],
  "The graph is a straight line rising from the origin while the ball speeds up uniformly on the slope, reaching a peak (maximum speed) at the bottom of the slope, then a straight line sloping down to zero while it slows down uniformly on the floor.",
  ["What happens to its speed on the slope?", "What happens on the rough floor?", "Where is the highest speed?"],
  "straight up, peak, straight down to zero",
  ["A straight line up while on the slope, a peak at the bottom, then a straight line down to zero on the floor", "it rises uniformly, reaches maximum speed, then falls back to zero"],
  ["A horizontal line", "A curve that keeps rising"], min_points=2)

Q("w2b_lift_slowing_up", 4, "2c", "A lift is moving upwards but slowing down as it approaches the top floor. State the directions of its velocity and its acceleration, and explain.",
  [P("velocity is upwards (it is moving up)", ["velocity is upwards", "velocity upwards", "moving up", "velocity is up"]),
   P("acceleration is downwards, because its upward velocity is decreasing", ["acceleration is downwards", "acceleration downwards", "acceleration is down", "opposite to the velocity", "velocity is decreasing"])],
  "The lift's velocity is upwards because it is moving up. Its acceleration is downwards, opposite to its velocity, because its upward velocity is decreasing (it is decelerating).",
  ["Which way is the lift moving?", "Is its speed increasing or decreasing?", "If speed decreases, how does the acceleration direction compare with the velocity?"],
  "velocity up; acceleration down (opposite)",
  ["The velocity is upwards but the acceleration is downwards because it is slowing down", "moving up, so velocity up; decelerating, so the acceleration is down, opposite to the velocity"],
  ["Both are upwards", "Both are downwards"], min_points=2)

# ---------------------------------------------------------------- L5
Q("w2b_horizontal_vt_claim", 5, "2g", "A student says: 'A horizontal line on a speed–time graph means the object is not moving.' Evaluate this claim.",
  [P("the claim is wrong in general: a horizontal line means constant speed (zero acceleration)", ["wrong", "constant speed", "zero acceleration", "not accelerating", "steady speed"]),
   P("the object is at rest only if the line lies along the time axis (speed = 0)", ["only if", "along the time axis", "speed is zero", "on the axis", "at zero"]),
   P("the student may be confusing it with a distance–time graph, where horizontal means at rest", ["distance–time", "distance-time", "confusing", "on a distance time graph"])],
  "The claim is wrong in general. A horizontal line on a speed–time graph means the speed is constant (zero acceleration); the object is at rest only if the line lies along the time axis at zero speed. The student is confusing it with a distance–time graph, where a horizontal line does mean the object is at rest.",
  ["What does a horizontal line on a speed–time graph tell you about the speed?", "When would it show rest?", "Which graph is the student thinking of?"],
  "horizontal on v–t = constant speed; rest only on the axis; confusion with d–t",
  ["Wrong: it means constant speed; it is only at rest if the line is along the time axis, which is the case for a distance–time graph", "not true, a horizontal line shows a steady speed with zero acceleration unless the speed is zero"],
  ["Correct, horizontal always means stopped", "Correct, the object is not moving"], min_points=2)

Q("w2b_ruler_drop_reaction", 5, "2i", "To measure reaction time, a partner drops a ruler and a student catches it as quickly as possible. Explain why the distance the ruler falls can be used to compare reaction times, and how to make the test fair.",
  [P("the ruler falls freely with constant acceleration, so a longer reaction time lets it fall further", ["falls further", "longer reaction time", "further it falls", "more distance", "greater distance means slower", "constant acceleration"]),
   P("so the distance fallen is a measure of the reaction time (bigger distance = slower reaction)", ["measure of", "slower reaction", "compare", "bigger distance"]),
   P("fair test: same start position (zero at fingers), same hand, no warning, repeat and average", ["same start", "zero at the fingers", "same hand", "no warning", "repeat", "average", "same height"])],
  "The ruler falls freely with a constant acceleration, so the longer the student takes to react, the further it falls before being caught. The distance fallen is therefore a measure of reaction time: a larger distance means a slower reaction. For a fair test, start with the zero mark level with the fingers, use the same hand, give no warning of the drop, and repeat several times and average.",
  ["How does the ruler move once released?", "How is reaction time linked to the distance fallen?", "What must be kept the same?"],
  "longer reaction → falls further; same start, repeat, average",
  ["The ruler accelerates uniformly so the longer the reaction time, the further it falls; keep the zero at the fingers, repeat and average", "bigger distance means a slower reaction; make it fair with the same starting position and repeats"],
  ["A heavier ruler would fall more slowly", "The distance does not depend on reaction time"], min_points=2)

Q("w2b_lines_cross_claim", 5, "2g", "On a speed–time graph, the lines for two cars starting side by side cross at t = 10 s. A student says car B catches up with car A at 10 s. Evaluate this.",
  [P("wrong: where speed–time lines cross, the cars have the same SPEED, not the same position", ["same speed", "not the same position", "equal speeds", "speed is the same", "wrong"]),
   P("to compare positions, compare the AREAS under the graphs (distances travelled)", ["area", "areas under", "distance travelled", "compare the areas", "distances"]),
   P("B catches A only when the areas become equal, which is later", ["later", "when the areas are equal", "after 10 s", "equal areas", "equal distances"])],
  "The claim is wrong. Where the speed–time lines cross, the two cars have the same speed, not the same position. Their positions are found from the areas under the graphs; car B catches car A only when the areas, the distances travelled, become equal, which happens later than 10 s.",
  ["What does the point where speed–time lines cross tell you?", "What represents distance travelled?", "When would B actually catch A?"],
  "crossing = same speed; positions from areas; catch-up later",
  ["Wrong: crossing lines means the same speed, not the same position; B catches A when the areas under the graphs are equal, which is later", "at 10 s they only have equal speeds; compare the distances (areas) to see when B catches up"],
  ["Correct, the crossing point is where they meet", "Correct, B overtakes A at 10 s"], min_points=2)

Q("w2b_average_speed_claim", 5, "2b", "A driver says: 'My average speed was 50 km/h, so I never drove faster than 50 km/h.' Evaluate this claim.",
  [P("the claim is wrong / not necessarily true", ["wrong", "not necessarily", "not true", "does not mean", "incorrect"]),
   P("average speed = total distance ÷ total time, so the speed may have varied", ["total distance ÷ total time", "total distance divided by", "varied", "changed", "faster at times", "slower at times"]),
   P("periods of slow driving or stopping must be balanced by driving faster than 50 km/h", ["balanced", "stopping", "slower parts", "must have gone faster", "above 50", "faster than 50"])],
  "The claim is not necessarily true. Average speed is total distance ÷ total time, so the speed can vary during the journey. If the driver stopped at lights or drove slowly at times, they must have driven faster than 50 km/h at other times to achieve an average of 50 km/h.",
  ["How is average speed defined?", "Could the speed have changed during the journey?", "What must happen if part of the journey was slow?"],
  "average ≠ maximum; slow parts balanced by faster parts",
  ["Wrong: average speed is total distance over total time, so if the driver stopped at lights they must have gone faster than 50 km/h at times", "not necessarily, because the speed varied; slower parts must be balanced by faster parts"],
  ["Correct, the average is the highest speed", "Correct, average speed is the speed all the time"], min_points=2)

Q("w2b_air_vs_vacuum_graph", 5, "2d", "Describe and explain the difference between the speed–time graphs of a ball falling in a vacuum and the same ball falling through air for a long way.",
  [P("vacuum: a straight line through the origin (constant acceleration 10 m/s²)", ["straight line", "constant acceleration", "10 m/s2", "uniform acceleration"]),
   P("air: a curve that gets less steep and levels off (decreasing acceleration)", ["curve", "less steep", "levels off", "flattens", "decreasing acceleration"]),
   P("because air resistance increases with speed until it balances the weight, giving a terminal (constant) speed", ["air resistance increases", "terminal", "balances the weight", "equals the weight", "constant speed"])],
  "In a vacuum the graph is a straight line through the origin, because the ball has a constant acceleration of about 10 m/s². In air the graph is a curve that becomes less steep and levels off, because air resistance increases with speed, reducing the acceleration until it balances the weight and the ball falls at a constant, terminal speed.",
  ["What is the acceleration in a vacuum?", "What force grows as the ball speeds up in air?", "What happens when that force equals the weight?"],
  "vacuum: straight line; air: curve levelling off; air resistance → terminal speed",
  ["In a vacuum it is a straight line with constant acceleration; in air it is a curve that levels off because air resistance increases until it equals the weight", "straight line for the vacuum, and for air a curve that flattens to a terminal speed"],
  ["Both are straight lines", "The ball in air falls faster"], min_points=2)

Q("w2b_start_on_sound", 5, "2b", "A timekeeper at the finish of a 200 m race starts the stopwatch when she HEARS the starting gun. Evaluate this method (speed of sound ≈ 340 m/s).",
  [P("sound takes about 0.6 s to travel 200 m (200 ÷ 340)", ["0.6 s", "0.59", "200 ÷ 340", "takes time to travel", "sound is slow"]),
   P("so she starts the stopwatch late and the recorded times are too short", ["starts late", "too short", "less than the real time", "times are too small", "runners seem faster"]),
   P("better: start when she SEES the smoke/flash, since light arrives almost instantly", ["see the smoke", "see the flash", "light", "almost instantly", "visual signal"])],
  "Sound travels at about 340 m/s, so it takes about 200 ÷ 340 ≈ 0.6 s to reach the finish. The timekeeper starts the stopwatch about 0.6 s late, so every recorded time is too short. She should start when she sees the smoke or flash from the gun, because light reaches her almost instantly.",
  ["How long does the sound take to cover 200 m?", "Is the stopwatch started early or late?", "What signal arrives faster?"],
  "sound delay ≈ 0.6 s; times too short; use the flash",
  ["Sound takes about 0.6 s to travel 200 m, so she starts late and the times are too short; she should start when she sees the smoke", "the recorded times are too small because sound is slow; use the flash, as light arrives almost instantly"],
  ["It is accurate because sound is instant", "The times would be too long"], min_points=2,
  pitfalls=[PF(["sound is instant", "sound travels instantly", "times would be too long", "times are too long"], "Sound takes about 0.6 s over 200 m, so the stopwatch starts late and the times are too SHORT.")])

Q("w2b_two_brakers", 5, "2h", "Two identical cars brake from the same speed. Car X decelerates at 6 m/s² and car Y at 3 m/s². Use speed–time graphs to compare their braking times and braking distances.",
  [P("Y takes twice as long to stop (smaller deceleration, less steep line)", ["twice as long", "twice the time", "longer to stop", "less steep", "double the time"]),
   P("braking distance = area of triangle (½ × speed × time), so Y's is twice X's", ["twice the distance", "twice as far", "double the distance", "area", "½ × speed × time"])],
  "On the speed–time graph Y's braking line is half as steep, so Y takes twice as long to stop. The braking distance is the area of the triangle, ½ × speed × time; with the same starting speed and twice the time, Y's braking distance is twice X's.",
  ["How does the deceleration affect the stopping time?", "What area gives the braking distance?", "Compare the two triangles."],
  "Y twice the time; triangle area → twice the distance",
  ["Y takes twice as long to stop, and since the distance is the area ½ × speed × time, Y's braking distance is twice as far", "Y's line is less steep so it takes double the time and travels twice the distance"],
  ["X takes longer to stop", "They stop in the same distance"], min_points=2)

Q("w2b_slowing_backwards_claim", 5, "2c", "A student says: 'A car with a negative acceleration must be moving backwards.' Evaluate this claim.",
  [P("wrong: negative acceleration means the acceleration is opposite to the chosen positive direction", ["wrong", "not true", "opposite direction", "opposite to the velocity", "not backwards", "incorrect", "just means decelerating"]),
   P("a car moving forwards but slowing down has a negative acceleration (deceleration)", ["slowing down", "decelerating", "moving forwards", "still moving forward", "deceleration"])],
  "The claim is wrong. A negative acceleration means the acceleration acts in the opposite direction to the one taken as positive. A car moving forwards but slowing down has a negative acceleration (a deceleration) while still moving forwards.",
  ["What does the sign of an acceleration tell you?", "Can a car moving forwards have a negative acceleration?", "Give an example."],
  "negative acceleration = slowing down (opposite to motion), not reversing",
  ["Wrong: a car moving forwards but slowing down has a negative acceleration; it means the acceleration is opposite to the motion", "not true, negative acceleration just means decelerating, the car can still be moving forward"],
  ["Correct, negative means backwards", "Correct, it is reversing"], min_points=2)

Q("w2b_which_graph_for_what", 5, "2e", "Explain which graph (distance–time or speed–time) and which feature of it you would use to find (a) the speed of a car moving steadily, (b) its acceleration, and (c) the distance it travels.",
  [P("(a) speed: gradient of the distance–time graph", ["gradient of the distance", "gradient of a distance-time", "distance–time gradient", "distance time graph gradient", "gradient of the d"]),
   P("(b) acceleration: gradient of the speed–time graph", ["gradient of the speed", "gradient of a speed-time", "speed–time gradient", "speed time graph gradient"]),
   P("(c) distance: area under the speed–time graph (or read from the distance–time graph)", ["area under the speed", "area under", "read the distance", "area"])],
  "(a) The speed is the gradient of the distance–time graph. (b) The acceleration is the gradient of the speed–time graph. (c) The distance travelled is the area under the speed–time graph (or it can be read directly from the distance–time graph).",
  ["What does the gradient of each graph give?", "What does the area under a speed–time graph give?", "Match each quantity to a graph and feature."],
  "speed: d–t gradient; acceleration: v–t gradient; distance: area under v–t",
  ["Speed is the gradient of the distance-time graph, acceleration is the gradient of the speed-time graph, and distance is the area under the speed-time graph", "use the distance time graph gradient for speed, the speed time graph gradient for acceleration and the area under it for distance"],
  ["Use the area under the distance-time graph for speed", "All three come from the highest point of the graph"], min_points=2)

Q("w2b_sprinter_profile", 5, "2h", "A sprinter accelerates for the first 4 s, runs at a steady top speed for the next 6 s, then slows slightly near the end. Describe the speed–time graph and explain how to find the total distance from it.",
  [P("rising line (acceleration) for 4 s, then horizontal (constant speed), then sloping slightly down", ["rises", "sloping up", "then horizontal", "flat", "constant speed", "slopes down", "slightly down"]),
   P("total distance = total area under the graph", ["area under", "total area", "area"]),
   P("found by splitting into shapes (triangle, rectangle, trapezium) and adding", ["triangle", "rectangle", "trapezium", "add the areas", "split into shapes"])],
  "The graph rises for the first 4 s while the sprinter accelerates, is horizontal for the next 6 s at top speed, then slopes slightly down as she slows near the end. The total distance is the total area under the graph, found by splitting it into a triangle, a rectangle and a trapezium and adding their areas.",
  ["Describe each stage of the motion on the graph.", "Which feature of a speed–time graph gives distance?", "How do you find an area with several shapes?"],
  "up, flat, slightly down; distance = total area (add shapes)",
  ["It rises for 4 s, is flat at constant speed, then slopes slightly down; the distance is the total area under the graph, adding the triangle, rectangle and trapezium", "the line goes up then is horizontal then slopes down a little; add the areas of the shapes to find the distance"],
  ["A single horizontal line; distance is the gradient", "It goes straight up and down"], min_points=2)
