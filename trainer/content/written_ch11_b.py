"""Chapter 11 Light: 50 more written-answer questions (10 per level), marked by keywords/phrases."""
from .. import figs
from .. import sketches2 as sk
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall
CH = 11


def Q(id, lv, lo, stem, points, model, hints, keywords, passes, fails, pitfalls=(), min_points=None, figure=None):
    written(id, CH, lv, lo, stem=stem, points=points, model_answer=model, hints=hints, keywords=keywords,
            pitfalls=pitfalls, min_points=min_points, figure=figure, sample_pass=passes, sample_fail=fails)


FROM_SURFACE = PF(["measured from the surface", "angle to the surface", "angle with the surface", "from the mirror surface"],
                  "Angles of incidence, reflection and refraction are measured from the NORMAL, not from the surface.")
SPEEDS_UP_IN_GLASS = PF(["speeds up in glass", "faster in glass", "speeds up when it enters glass"], "Light SLOWS DOWN when it enters glass from air.")

# ---------------------------------------------------------------- L1
Q("w11b_define_angle_reflection", 1, "11a", "Fig. 1 shows a ray reflected by a plane mirror. Define the angle of reflection.",
  [P("the angle between the reflected ray and the normal", ["between the reflected ray and the normal", "reflected ray and the normal", "angle between the reflected ray"], ordered=False, window=9)],
  "The angle of reflection is the angle between the reflected ray and the normal at the point of incidence.",
  ["Which ray leaves the mirror?", "Angles are measured from which line?", "Define it."],
  "angle between reflected ray and normal",
  ["The angle between the reflected ray and the normal", "it is measured between the reflected ray and the normal"],
  ["The angle between the reflected ray and the mirror", "The angle between the incident ray and the normal"],
  pitfalls=[FROM_SURFACE, PF(["reflected ray and the mirror", "incident ray and the normal"], "The angle of reflection is between the REFLECTED ray and the NORMAL.")],
  figure=lambda: sk.reflection_diagram(40, show_r=True, label_i="i", label_r="r"))

Q("w11b_define_refraction", 1, "11c", "State what is meant by refraction of light.",
  [P("the change in direction (bending) of light", ["bending", "change in direction", "bends", "changes direction"]),
   P("when it passes from one medium into another (because its speed changes)", ["one medium into another", "from one material to another", "different medium", "speed changes", "enters glass", "boundary"])],
  "Refraction is the bending (change in direction) of light as it passes from one medium into another, caused by the change in its speed.",
  ["What happens to a ray at an air–glass boundary?", "Why does it happen?", "Define it."],
  "change in direction when passing between media",
  ["The bending of light when it passes from one medium into another", "light changes direction at a boundary because its speed changes"],
  ["Light bouncing off a mirror", "Light splitting into colours"], min_points=2,
  pitfalls=[PF(["bouncing off", "bounces off a mirror"], "Bouncing off a surface is REFLECTION.")])

Q("w11b_define_angle_refraction", 1, "11c", "Fig. 1 shows a ray passing from air into glass. Define the angle of refraction.",
  [P("the angle between the refracted ray and the normal", ["refracted ray and the normal", "between the refracted ray and the normal", "angle between the refracted ray"])],
  "The angle of refraction is the angle between the refracted ray and the normal.",
  ["Which ray is in the glass?", "Angles are measured from which line?", "Define it."],
  "angle between refracted ray and normal",
  ["The angle between the refracted ray and the normal", "it is the angle the refracted ray makes with the normal"],
  ["The angle between the refracted ray and the glass surface", "The angle of incidence"],
  pitfalls=[FROM_SURFACE, PF(["refracted ray and the glass surface", "refracted ray and the surface"], "Measure from the NORMAL.")],
  figure=lambda: sk.refraction_diagram(50, 31, label_i="i", label_r="r"))

Q("w11b_principal_focus_def", 1, "11g", "Fig. 1 shows a parallel beam passing through a converging lens. State what is meant by the principal focus F.",
  [P("the point where rays parallel to the principal axis converge (meet) after passing through the lens", ["parallel to the principal axis", "rays meet", "rays converge", "converge to a point", "meet at a point", "brought to a focus"])],
  "The principal focus F is the point on the principal axis where rays parallel to the principal axis converge (meet) after passing through the lens.",
  ["What happens to parallel rays after the lens?", "Where do they meet?", "Define it."],
  "point where parallel rays converge after the lens",
  ["The point where rays parallel to the principal axis meet after passing through the lens", "where parallel rays converge after the lens"],
  ["The centre of the lens", "The point where the object is placed"],
  figure=lambda: sk.lens_parallel_beam(2.0))

Q("w11b_principal_axis", 1, "11f", "State what is meant by the principal axis of a lens.",
  [P("the line passing through the optical centre of the lens, at right angles (perpendicular) to the lens", ["through the optical centre", "through the centre", "at right angles to the lens", "perpendicular to the lens", "through the middle"])],
  "The principal axis is the straight line passing through the optical centre of the lens, at right angles to the lens.",
  ["It is a line, not a point.", "Where does it pass through the lens?", "At what angle to the lens?"],
  "line through optical centre, perpendicular to lens",
  ["The line through the optical centre at right angles to the lens", "a line through the centre of the lens, perpendicular to it"],
  ["The edge of the lens", "The focal point"])

Q("w11b_snell_state", 1, "11d", "State the relationship between the angle of incidence i and the angle of refraction r for light passing from air into a given glass block.",
  [P("sin i ÷ sin r is a constant (the refractive index)", ["sin i / sin r", "sin i ÷ sin r", "sin i over sin r", "ratio of the sines", "snell"])],
  "For a given pair of media, sin i ÷ sin r is a constant; for light entering the glass from air, this constant is the refractive index of the glass.",
  ["This is Snell's law.", "It involves the sines of the angles.", "State it."],
  "sin i ÷ sin r = constant",
  ["sin i ÷ sin r is constant", "sin i / sin r equals the refractive index"],
  ["i ÷ r is constant", "i + r = 90°"])

Q("w11b_converging_shape", 1, "11f", "Describe the shape of a thin converging lens and what it does to parallel rays of light.",
  [P("it is thicker in the middle than at the edges (convex)", ["thicker in the middle", "thicker at the centre", "convex", "bulges", "fatter in the middle"]),
   P("it brings parallel rays together to a focus (converges them)", ["brings them together", "converges", "meet at a point", "focus"])],
  "A thin converging lens is thicker in the middle than at its edges (convex). It refracts parallel rays of light so that they come together at a point, the principal focus.",
  ["Is it thicker in the middle or at the edges?", "What does it do to parallel rays?", "Describe both."],
  "thicker in middle; converges parallel rays",
  ["It is thicker in the middle and brings parallel rays together to a focus", "a convex lens that converges parallel light to a point"],
  ["It is thinner in the middle and spreads rays out", "It reflects the light"], min_points=2)

Q("w11b_optical_centre", 1, "11f", "State what happens to a ray of light passing through the optical centre of a thin lens.",
  [P("it passes straight through without changing direction (undeviated)", ["straight through", "without changing direction", "undeviated", "not bent", "does not bend", "continues straight"])],
  "A ray passing through the optical centre of a thin lens goes straight through without changing direction.",
  ["The centre of a thin lens is like a thin flat sheet of glass.", "Does the ray bend?", "State it."],
  "passes straight through (undeviated)",
  ["It passes straight through without bending", "it goes straight on, undeviated"],
  ["It bends towards the principal focus", "It is reflected back"])

Q("w11b_mirror_image_size_distance", 1, "11b", "State how the size and position of the image in a plane mirror compare with the object.",
  [P("the image is the same size as the object", ["same size"]),
   P("it is the same distance behind the mirror as the object is in front", ["same distance behind", "as far behind", "same distance", "equal distance"])],
  "The image in a plane mirror is the same size as the object and is the same distance behind the mirror as the object is in front of it.",
  ["Is the image magnified?", "Where is the image compared with the mirror?", "State both."],
  "same size; same distance behind",
  ["It is the same size and the same distance behind the mirror", "same size as the object, as far behind as the object is in front"],
  ["It is larger and closer to the mirror", "It is half the size"], min_points=2)

Q("w11b_light_slower_glass", 1, "11e", "State how the speed of light in glass compares with its speed in air.",
  [P("light travels more slowly in glass", ["slower in glass", "more slowly", "slower", "slows down", "less in glass"])],
  "Light travels more slowly in glass than in air (in glass of refractive index 1.5 it travels at about 2 × 10⁸ m/s).",
  ["Light bends towards the normal entering glass.", "What change in speed causes that?", "State it."],
  "slower in glass",
  ["Light travels more slowly in glass", "it slows down in glass"],
  ["Light travels faster in glass", "The same speed"], pitfalls=[SPEEDS_UP_IN_GLASS])

# ---------------------------------------------------------------- L2
Q("w11b_reflect_40", 2, "11b", "Fig. 1 shows a ray hitting a plane mirror with an angle of incidence of 40°. State the angle of reflection and explain how you know.",
  [P("the angle of reflection is 40°", ["40°", "40 degrees", "40"]),
   P("because the angle of incidence equals the angle of reflection (law of reflection)", ["equals the angle of incidence", "angle of incidence equals", "law of reflection", "i = r", "same as the angle of incidence", "equal"])],
  "The angle of reflection is 40°, because by the law of reflection the angle of reflection equals the angle of incidence.",
  ["What does the law of reflection say?", "What is the angle of incidence?", "State the answer."],
  "40°; i = r",
  ["40°, because the angle of reflection equals the angle of incidence", "it is 40° by the law of reflection"],
  ["50°", "80°"], min_points=2,
  figure=lambda: sk.reflection_diagram(40, show_r=True, label_i="40°", label_r="r"))

Q("w11b_glass_to_air", 2, "11c", "A ray passes at an angle from glass into air. Describe what happens to its speed and direction.",
  [P("it speeds up", ["speeds up", "faster", "increases speed", "speed increases"]),
   P("it bends away from the normal", ["away from the normal", "bends away"])],
  "As the ray passes from glass into air it speeds up, so it bends away from the normal.",
  ["Is light faster in glass or in air?", "Speeding up bends a ray which way?", "Describe both."],
  "speeds up; bends away from normal",
  ["It speeds up and bends away from the normal", "faster in air, so it bends away from the normal"],
  ["It slows down and bends towards the normal", "It goes straight on"], min_points=2,
  pitfalls=[PF(["bends towards the normal", "slows down"], "Going from glass INTO AIR, light speeds up and bends AWAY from the normal.")])

Q("w11b_standard_rays", 2, "11h", "Name two standard rays used to draw a ray diagram for a converging lens, and describe how each travels after the lens.",
  [P("a ray parallel to the principal axis passes through F on the other side", ["parallel to the principal axis", "parallel ray", "through f", "through the focus", "principal focus"]),
   P("a ray through the optical centre goes straight on (undeviated)", ["optical centre", "through the centre", "straight on", "undeviated", "straight through"])],
  "One ray, parallel to the principal axis, is refracted through the principal focus F on the other side. A second ray, through the optical centre, passes straight on without changing direction. (A ray through F on the near side emerges parallel to the axis.)",
  ["Think of a ray parallel to the axis.", "Think of a ray through the middle of the lens.", "Describe what each does."],
  "parallel ray → through F; ray through centre → straight",
  ["A ray parallel to the principal axis passes through F, and a ray through the optical centre goes straight through", "parallel ray goes through the focus; centre ray is undeviated"],
  ["All rays pass through the centre", "Rays bounce off the lens"], min_points=2)

Q("w11b_lateral_inversion", 2, "11b", "Ambulances often have the word AMBULANCE written back to front on the front. Explain why.",
  [P("a plane mirror image is laterally inverted (left and right swapped)", ["laterally inverted", "lateral inversion", "left and right", "back to front", "reversed"]),
   P("so drivers in front see the word the right way round in their rear-view mirror", ["rear-view mirror", "mirror", "right way round", "reads correctly", "correct way"])],
  "The image in a plane mirror is laterally inverted, with left and right swapped. Writing AMBULANCE back to front means that drivers ahead see it the right way round in their rear-view mirrors and can read it at once.",
  ["How does a plane mirror change writing?", "Who will see the word in a mirror?", "Explain."],
  "mirror image laterally inverted → reads correctly in mirror",
  ["Mirror images are laterally inverted, so drivers see AMBULANCE the right way round in their rear-view mirror", "the mirror reverses left and right, so the reversed word reads correctly"],
  ["It looks more urgent", "Mirrors turn writing upside down"], min_points=2,
  pitfalls=[PF(["upside down", "turn writing upside down"], "A plane mirror image is upright but LATERALLY inverted.")])

Q("w11b_n_meaning", 2, "11e", "Glass has a refractive index of 1.5. Explain what this tells you.",
  [P("light travels 1.5 times faster in a vacuum (air) than in the glass", ["1.5 times", "1.5 times faster", "1.5 times slower", "speed in vacuum ÷ speed in glass", "divided by the speed in glass", "c ÷ v"]),
   P("so light travels at about 2 × 10^8 m/s in the glass", ["2 × 10", "2 x 10", "2.0 × 10", "200 000 000"])],
  "A refractive index of 1.5 means that light travels 1.5 times faster in a vacuum than in the glass (n = c ÷ v). So in the glass light travels at 3 × 10⁸ ÷ 1.5 = 2 × 10⁸ m/s.",
  ["How is refractive index defined?", "What does 1.5 compare?", "Work out the speed in glass."],
  "c ÷ v = 1.5; v = 2 × 10⁸ m/s",
  ["Light is 1.5 times faster in a vacuum than in glass, so it travels at 2 × 10⁸ m/s in the glass", "the speed in vacuum divided by the speed in glass is 1.5"],
  ["Light is 1.5 times faster in glass", "The glass is 1.5 cm thick"], min_points=1, pitfalls=[SPEEDS_UP_IN_GLASS])

Q("w11b_mirror_upright", 2, "11b", "State whether the image in a plane mirror is real or virtual and whether it is upright or inverted, and explain the first answer.",
  [P("virtual", ["virtual"]),
   P("upright", ["upright", "the right way up", "not inverted"]),
   P("virtual because the rays only appear to come from behind the mirror and it cannot be formed on a screen", ["appear to come from", "cannot be formed on a screen", "not on a screen", "rays do not meet", "only appear"])],
  "The image is virtual and upright. It is virtual because the reflected rays only appear to come from a point behind the mirror; no light actually reaches there, so the image cannot be formed on a screen.",
  ["Do light rays actually pass through the image behind the mirror?", "Is the image the right way up?", "Answer and explain."],
  "virtual, upright; rays only appear to come from it",
  ["It is virtual and upright, because the rays only appear to come from behind the mirror", "virtual since it cannot be formed on a screen, and upright"],
  ["Real and inverted", "Real because you can see it"], min_points=2)

Q("w11b_parallel_converge", 2, "11f", "Fig. 1 shows a beam of light parallel to the principal axis entering a converging lens. Describe what happens to the beam.",
  [P("the rays are refracted (bent) by the lens", ["refracted", "bent", "bends", "change direction"]),
   P("they converge and meet at the principal focus F", ["converge", "meet at", "principal focus", "come together", "focus"]),
   P("and then spread out again beyond F", ["spread out", "diverge", "beyond f", "after f"])],
  "The rays are refracted by the lens so that they converge and meet at the principal focus F on the other side. Beyond F they spread out again.",
  ["Does the lens bend the rays?", "Where do they meet?", "What happens after that point?"],
  "refracted, converge at F, then spread out",
  ["The rays are refracted and converge at the principal focus, then spread out again", "the lens bends the parallel rays so they meet at F"],
  ["The rays are reflected back", "The rays spread out from the lens"], min_points=2,
  figure=lambda: sk.lens_parallel_beam(2.0))

Q("w11b_measure_angles", 2, "11a", "When investigating reflection with a ray box and protractor, a student draws a normal at the point where the ray hits the mirror. Explain why and how the angles should be measured.",
  [P("the normal is a line at 90° to the mirror at the point of incidence", ["90", "right angles", "perpendicular"]),
   P("angles of incidence and reflection are measured from the normal (not the mirror)", ["from the normal", "between the ray and the normal", "measured from the normal"]),
   P("use a protractor centred on the point where the ray hits the mirror", ["protractor", "centred", "point of incidence", "where the ray hits"])],
  "The normal is a line drawn at 90° to the mirror at the point of incidence. Angles of incidence and reflection are measured between each ray and the normal, not the mirror, using a protractor centred on the point where the ray meets the mirror.",
  ["What angle does the normal make with the mirror?", "From which line are the angles measured?", "How is the protractor placed?"],
  "normal at 90°; measure angles from the normal; protractor at point of incidence",
  ["The normal is at right angles to the mirror and both angles are measured from it with a protractor at the point where the ray hits", "angles are measured between each ray and the normal, which is perpendicular to the mirror"],
  ["Measure the angles from the mirror surface", "Normals are not needed"], min_points=2, pitfalls=[FROM_SURFACE])

Q("w11b_ray_through_f", 2, "11h", "A ray passes through the principal focus F on its way to a converging lens. Describe the ray after it passes through the lens.",
  [P("it emerges parallel to the principal axis", ["parallel to the principal axis", "parallel to the axis", "emerges parallel", "comes out parallel"])],
  "A ray that passes through the principal focus on its way to the lens emerges from the lens parallel to the principal axis.",
  ["This is the reverse of a parallel ray passing through F.", "Light paths are reversible.", "Describe the ray."],
  "emerges parallel to the axis",
  ["It emerges parallel to the principal axis", "it comes out parallel to the axis"],
  ["It goes straight through the centre", "It bends towards F again"])

Q("w11b_real_on_screen", 2, "11h", "In a projector, a converging lens forms an image of a slide on a screen. State two features of this image and explain why it can appear on the screen.",
  [P("real", ["real"]),
   P("inverted (and magnified)", ["inverted", "upside down", "magnified"]),
   P("light rays actually meet at the screen, which is why it is real", ["rays actually meet", "light actually reaches", "rays converge", "actually meet"])],
  "The image is real, inverted and magnified. It can appear on the screen because light rays from the slide actually meet at the screen after passing through the lens, which is what makes it a real image.",
  ["Can a virtual image be formed on a screen?", "Is the image upright or inverted?", "Why does it appear on the screen?"],
  "real, inverted, magnified; rays actually meet",
  ["It is real and inverted, because the light rays actually meet at the screen", "a real, magnified, upside-down image where the rays converge"],
  ["Virtual and upright", "The screen makes its own image"], min_points=2)

# ---------------------------------------------------------------- L3
Q("w11b_pool_shallower", 3, "11c", "A swimming pool looks shallower than it really is. Explain why.",
  [P("light from the bottom refracts (bends away from the normal) as it leaves the water into air", ["bends away from the normal", "refracts", "refraction", "bends as it leaves"]),
   P("the eye traces the rays back in straight lines", ["straight lines", "traces back", "eye assumes", "brain assumes", "appear to come from"]),
   P("so they appear to come from a point higher up (the bottom looks shallower)", ["higher", "shallower", "nearer the surface", "above the real"])],
  "Light from the bottom of the pool is refracted away from the normal as it passes from water into air. The eye assumes light travels in straight lines, so it traces the rays back to a point higher than the real bottom; the pool therefore looks shallower than it is.",
  ["What happens to light leaving the water?", "How does the eye interpret where the light came from?", "Explain."],
  "refraction away from normal at surface; eye traces straight back → appears higher",
  ["Light bends away from the normal as it leaves the water, and the eye traces it back in straight lines so the bottom appears higher", "refraction at the surface makes the light seem to come from a shallower point"],
  ["The water magnifies the pool", "Light reflects off the bottom"], min_points=2)

Q("w11b_periscope", 3, "11b", "A simple periscope contains two plane mirrors at 45°. Explain how it lets you see over a wall.",
  [P("light from the object hits the top mirror and is reflected down (angle of incidence 45° = angle of reflection)", ["reflected down", "top mirror", "45°", "at 45", "angle of incidence equals"]),
   P("it then hits the bottom mirror and is reflected into the eye", ["bottom mirror", "reflected into the eye", "second mirror", "reflects again"]),
   P("so light travels down the tube and you see the object", ["down the tube", "you see", "reaches the eye", "turned through 90"])],
  "Light from the object over the wall strikes the top mirror at 45° and is reflected straight down the tube (angle of reflection = angle of incidence). It then strikes the bottom mirror, also at 45°, and is reflected horizontally into the eye, so the viewer sees the object.",
  ["What does the top mirror do to the light?", "And the bottom mirror?", "Explain the path."],
  "two reflections at 45° send light down then into the eye",
  ["Light is reflected down by the top mirror and then into the eye by the bottom mirror", "the two mirrors at 45° each turn the light through 90°, so it reaches the eye"],
  ["The periscope uses lenses to bend light round corners", "Light passes through the mirrors"], min_points=2)

Q("w11b_rear_view", 3, "11b", "Describe the image a driver sees in a flat (plane) rear-view mirror and explain why it is useful.",
  [P("virtual, upright, same size, laterally inverted", ["virtual", "upright", "same size", "laterally inverted"]),
   P("useful because it shows the road behind the right way up and at the true size (judging distances)", ["right way up", "true size", "judge", "distance", "see behind", "road behind"])],
  "The image is virtual, upright, the same size as the object and laterally inverted. It is useful because it shows the traffic behind the right way up and at its true size, so the driver can judge its distance.",
  ["List the features of a plane mirror image.", "Why is 'upright' and 'same size' helpful to a driver?", "Explain."],
  "virtual, upright, same size, laterally inverted; helps judge traffic",
  ["It is upright and the same size, so the driver can see the traffic behind and judge distances", "a virtual, upright, laterally inverted image of the road behind"],
  ["Real and inverted", "Magnified"], min_points=2)

Q("w11b_diamond_speed", 3, "11e", "Diamond has a refractive index of 2.4. Explain what this means for the speed of light in diamond compared with glass (n = 1.5).",
  [P("n = c ÷ v, so v = c ÷ n", ["c ÷ n", "c / n", "n = c ÷ v", "v = c ÷ n", "speed in vacuum ÷"]),
   P("light is slower in diamond than in glass (larger n means smaller v)", ["slower in diamond", "slower", "more slowly", "larger n", "higher refractive index", "larger refractive index", "smaller speed"]),
   P("about 1.25 × 10^8 m/s in diamond compared with 2 × 10^8 m/s in glass", ["1.25", "2 × 10", "1.3 × 10"])],
  "Since n = c ÷ v, the speed in a material is v = c ÷ n. Diamond has a larger refractive index than glass, so light travels more slowly in it: about 3 × 10⁸ ÷ 2.4 = 1.25 × 10⁸ m/s, compared with 2 × 10⁸ m/s in glass.",
  ["How is refractive index defined?", "Larger n means larger or smaller speed?", "Work out both speeds."],
  "v = c/n; diamond slower (1.25 × 10⁸ vs 2 × 10⁸ m/s)",
  ["v = c ÷ n, so light is slower in diamond, about 1.25 × 10⁸ m/s compared with 2 × 10⁸ m/s in glass", "the larger refractive index means light travels more slowly in diamond"],
  ["Light is faster in diamond", "The speeds are the same"], min_points=1)

Q("w11b_block_parallel", 3, "11c", "A ray passes through a rectangular glass block, entering and leaving through parallel faces. Explain why the emerging ray is parallel to the incident ray.",
  [P("at the first face the ray bends towards the normal (slows down)", ["towards the normal", "slows down", "first face", "entering"]),
   P("at the second face it bends away from the normal by the same amount (speeds up)", ["away from the normal", "same amount", "speeds up", "second face", "leaving"]),
   P("because the faces are parallel, the two changes cancel, so it emerges parallel (but shifted sideways)", ["cancel", "parallel faces", "emerges parallel", "shifted sideways", "same angle"])],
  "On entering the block the ray slows down and bends towards the normal. On leaving through the parallel opposite face it speeds up and bends away from the normal by the same amount. Because the faces are parallel, the two deviations cancel, so the emerging ray is parallel to the incident ray, though shifted sideways.",
  ["What happens at the first face?", "What happens at the second face?", "Why do the two effects cancel?"],
  "bend towards then away equally; parallel faces → emerges parallel",
  ["It bends towards the normal entering and away from the normal leaving by the same amount, so because the faces are parallel it emerges parallel", "it bends towards the normal going in and away from it coming out, so the two refractions cancel and the ray comes out parallel but shifted sideways"],
  ["It is reflected inside the block", "It comes out at 90°"], min_points=2)

Q("w11b_camera_lens", 3, "11h", "A camera lens forms an image of a distant tree on the sensor. Describe the image and explain why it must be real.",
  [P("real, inverted and diminished (smaller than the tree)", ["real", "inverted", "diminished", "smaller", "upside down"]),
   P("it must be real so that light actually falls on the sensor and can be recorded", ["light actually falls", "rays actually meet", "on the sensor", "recorded", "formed on"])],
  "The image is real, inverted and diminished (much smaller than the tree). It must be real because the light rays must actually meet on the sensor so that the sensor can detect and record the image.",
  ["Is the image bigger or smaller than the tree?", "Is it upright or inverted?", "Why must it be real?"],
  "real, inverted, diminished; rays meet on sensor",
  ["It is real, inverted and smaller, because the rays must actually meet on the sensor to be recorded", "a diminished upside-down real image formed on the sensor"],
  ["Virtual and magnified", "Upright and the same size"], min_points=2)

Q("w11b_walk_to_mirror", 3, "11b", "A boy walks towards a plane mirror. Explain what happens to the position and the size of his image.",
  [P("the image moves closer to the mirror (always the same distance behind as he is in front)", ["moves closer", "same distance behind", "closer to the mirror", "gets nearer"]),
   P("the image stays the same size", ["same size", "does not change size", "size stays the same"])],
  "His image is always the same distance behind the mirror as he is in front, so as he walks towards the mirror his image also moves closer to it. The image stays the same size as him.",
  ["Where is a plane mirror image?", "Does the image size change?", "Explain."],
  "image moves closer (same distance behind); same size",
  ["The image moves closer because it is always the same distance behind the mirror, and it stays the same size", "it gets nearer the mirror but does not change size"],
  ["The image gets bigger", "The image moves further away"], min_points=2,
  pitfalls=[PF(["image gets bigger", "image becomes larger"], "A plane mirror image is always the same size as the object.")])

Q("w11b_more_bending_higher_n", 3, "11d", "Light enters water (n = 1.33) and glass (n = 1.5) at the same angle of incidence. Explain which bends more.",
  [P("the glass bends the light more", ["glass bends more", "glass", "more in glass"]),
   P("because it has the higher refractive index (light slows down more)", ["higher refractive index", "larger refractive index", "slows down more", "higher n"]),
   P("so sin r = sin i ÷ n is smaller: smaller angle of refraction", ["smaller angle of refraction", "sin r", "smaller r", "closer to the normal"])],
  "The glass bends the light more. It has the higher refractive index, so light slows down more on entering it. Since sin r = sin i ÷ n, the larger n gives a smaller angle of refraction, so the ray bends closer to the normal.",
  ["Which material has the higher refractive index?", "What does a higher n mean for the angle of refraction?", "Explain."],
  "glass: higher n → smaller r → more bending",
  ["Glass bends it more because it has a higher refractive index, so the angle of refraction is smaller", "the higher n of glass means light slows down more and bends closer to the normal"],
  ["Water bends it more because it is a liquid", "They bend it equally"], min_points=2)

Q("w11b_shorter_f_stronger", 3, "11g", "Lens A has a focal length of 5 cm and lens B has a focal length of 20 cm. Explain which lens bends light more strongly.",
  [P("lens A (shorter focal length)", ["lens a", "shorter focal length", "5 cm"]),
   P("it brings parallel rays to a focus closer to the lens, so it bends them more", ["closer to the lens", "bends them more", "more strongly", "more powerful", "converges more"])],
  "Lens A, with the shorter focal length, bends light more strongly: it brings parallel rays to a focus only 5 cm from the lens, so it must deviate them more than lens B, which focuses them 20 cm away.",
  ["What does the focal length measure?", "Which lens brings parallel rays together sooner?", "Explain."],
  "shorter f → more bending",
  ["Lens A, because its shorter focal length means it brings parallel rays to a focus closer to the lens, bending them more", "the 5 cm lens converges the light more strongly"],
  ["Lens B, because it is longer", "They bend light equally"], min_points=2)

Q("w11b_ray_box_block", 3, "11d", "Describe how to trace the path of a ray through a glass block using a ray box, so that the angles of incidence and refraction can be measured.",
  [P("draw round the block on paper and shine a ray from the ray box at an angle onto one face", ["draw round the block", "outline", "shine a ray", "ray box", "at an angle"]),
   P("mark the incident and emerging rays with crosses/dots, remove the block and join the points through the block", ["mark", "crosses", "dots", "join", "remove the block", "join the points"]),
   P("draw normals at the entry point and measure i and r with a protractor", ["normal", "protractor", "measure i and r", "angle of incidence and refraction"])],
  "Place the block on paper and draw round it. Shine a narrow ray from the ray box onto one face at an angle. Mark the incident and emerging rays with small crosses, remove the block, and join the points to show the path through the block. Draw a normal where the ray enters and measure i and r with a protractor.",
  ["How do you record where the block was?", "How do you record the rays?", "How do you get the path inside the block and the angles?"],
  "draw round block; mark rays; join through block; normal; protractor",
  ["Draw round the block, mark the incident and emerging rays with crosses, remove the block and join them, then draw the normal and measure the angles with a protractor", "trace the rays with dots, join them through the outline and measure i and r from the normal"],
  ["Look through the block and estimate the angles", "Measure the thickness of the block"], min_points=2)

# ---------------------------------------------------------------- L4
Q("w11b_snell_graph", 4, "11d", "Describe how to use a graph to find the refractive index of a glass block from several pairs of angles i and r.",
  [P("measure r for several different values of i", ["several", "different angles", "range of angles", "repeat for different"]),
   P("plot sin i (y-axis) against sin r (x-axis)", ["plot sin i against sin r", "sin i against sin r", "graph of sin i", "plot sin i"]),
   P("draw a best-fit straight line through the origin; the gradient is the refractive index", ["gradient", "best-fit", "straight line", "through the origin", "gradient is the refractive index"])],
  "Measure the angle of refraction r for several different angles of incidence i. Plot sin i on the y-axis against sin r on the x-axis. The points lie on a straight line through the origin; the gradient of the best-fit line is the refractive index, since sin i ÷ sin r = n.",
  ["How many readings do you need?", "What do you plot?", "Which feature of the graph gives n?"],
  "several i and r; plot sin i vs sin r; gradient = n",
  ["Measure r for several values of i, plot sin i against sin r, and the gradient of the straight line is the refractive index", "the gradient of a graph of sin i against sin r gives n"],
  ["Plot i against r and read the intercept", "Measure one angle only"], min_points=2)

Q("w11b_dentist_mirror", 4, "11b", "A dentist uses a small plane mirror to see the back of a patient's teeth. Explain how the dentist sees the teeth and describe the image.",
  [P("light from the back of the teeth reflects off the mirror into the dentist's eye", ["reflects off the mirror", "reflected into the eye", "light from the teeth", "reflects"]),
   P("the image appears behind the mirror (virtual)", ["virtual", "behind the mirror", "appears to be behind"]),
   P("upright, same size, laterally inverted", ["upright", "same size", "laterally inverted"])],
  "Light from the back of the teeth reflects off the mirror, obeying the law of reflection, and travels into the dentist's eye. The dentist sees a virtual image that appears to be behind the mirror; it is upright, the same size as the teeth and laterally inverted.",
  ["How does light get from the teeth to the dentist's eye?", "Where does the image appear?", "Describe it."],
  "light reflects into eye; virtual image behind mirror, upright, same size, laterally inverted",
  ["Light from the teeth reflects off the mirror into the dentist's eye; the image is virtual, upright and laterally inverted", "the mirror reflects light from the teeth so the dentist sees a virtual image behind it"],
  ["The mirror makes the teeth glow", "The image is real and inverted"], min_points=2)

Q("w11b_object_at_2f", 4, "11h", "Fig. 1 shows a ray diagram for an object at 2F in front of a converging lens. Describe the image formed, using the diagram.",
  [P("real (the rays actually meet)", ["real", "rays meet", "rays actually cross"]),
   P("inverted", ["inverted", "upside down"]),
   P("the same size as the object, at 2F on the other side", ["same size", "at 2f", "equal size"])],
  "The rays actually cross on the other side of the lens, so the image is real. It is inverted, and it is the same size as the object, formed at 2F on the other side of the lens.",
  ["Do the rays actually meet after the lens?", "Is the image above or below the axis?", "Compare its size with the object."],
  "real, inverted, same size (at 2F)",
  ["It is real, inverted and the same size, formed at 2F on the other side", "a real upside-down image the same size as the object"],
  ["Virtual, upright and magnified", "Real and diminished"], min_points=2,
  figure=lambda: sk.lens_diagram(4, 2))

Q("w11b_projector_slide_upside_down", 4, "11h", "Slides in a lens projector are put in upside down. Explain why.",
  [P("the projector lens forms a real image that is inverted", ["inverted", "upside down", "real image"]),
   P("so putting the slide in upside down makes the image on the screen the right way up", ["right way up", "upright on the screen", "correct way up", "appears upright", "slide is inverted", "correct it"])],
  "A converging lens in a projector forms a real image that is inverted. Putting the slide in upside down means that the inverted image on the screen is the right way up.",
  ["What kind of image does the projector lens form?", "Is it upright or inverted?", "How does an upside-down slide help?"],
  "real image is inverted, so slide inserted upside down",
  ["The lens forms an inverted real image, so an upside-down slide gives an upright picture on the screen", "the image is upside down, so the slide is inverted to correct it"],
  ["So that the light can pass through", "Because screens are upside down"], min_points=2)

Q("w11b_glass_vs_water_bending", 4, "11d", "Explain why a ray entering glass at 50° bends more than a ray entering water at 50°, and how you could show this experimentally.",
  [P("glass has a higher refractive index, so light slows more and the angle of refraction is smaller", ["higher refractive index", "slows down more", "slows more", "slows more in glass", "glass bends it more", "smaller angle of refraction", "higher n"]),
   P("experiment: shine rays at 50° into a glass block and a water tank (or plastic box of water)", ["glass block", "box of water", "into water", "water tank", "ray box", "same angle", "50°"]),
   P("measure the angles of refraction with a protractor and compare: glass gives the smaller r", ["measure the angle of refraction", "protractor", "compare", "smaller r", "glass gives"])],
  "Glass has a higher refractive index than water, so light slows down more on entering it and, by sin r = sin i ÷ n, the angle of refraction is smaller: the ray bends more. To show this, shine rays from a ray box at 50° into a glass block and into a clear box of water, trace the rays, and measure the angles of refraction with a protractor; the angle in glass is smaller.",
  ["Which material has the higher n?", "How does that affect r?", "How would you test it?"],
  "glass higher n → smaller r; trace rays at 50° in both and compare",
  ["Glass has a higher refractive index so the angle of refraction is smaller; shine rays at 50° into glass and water and measure r with a protractor", "light slows more in glass, so it bends more; compare the measured angles of refraction"],
  ["Water bends light more because it is wet", "Both bend the same"], min_points=2,
  pitfalls=[PF(["water bends light more", "water bends it more"], "Glass has the higher refractive index, so GLASS bends the light more.")])

Q("w11b_frequency_unchanged_glass", 4, "11e", "When light enters glass from air, its speed decreases. Explain what happens to its frequency and wavelength.",
  [P("the frequency stays the same (set by the source)", ["frequency stays the same", "same frequency", "frequency does not change", "frequency is unchanged"]),
   P("the wavelength decreases (v = f λ)", ["wavelength decreases", "shorter wavelength", "wavelength gets shorter", "smaller wavelength"])],
  "The frequency stays the same, because it is set by the source. Since v = f λ and the speed decreases, the wavelength must decrease in the glass.",
  ["What sets the frequency?", "Use v = f λ.", "What must change?"],
  "f unchanged; λ decreases",
  ["The frequency stays the same and the wavelength decreases, because v = fλ", "same frequency, shorter wavelength in the glass"],
  ["The frequency decreases", "The wavelength increases"], min_points=2,
  pitfalls=[PF(["frequency decreases", "frequency changes", "wavelength increases"], "Frequency is fixed by the source; slower light has a SHORTER wavelength.")])

Q("w11b_see_image_behind_mirror", 4, "11b", "Explain, using rays, how your eye sees an image of an object that seems to be behind a plane mirror.",
  [P("rays from the object reflect off the mirror (obeying the law of reflection) into the eye", ["reflect off the mirror", "reflected into the eye", "law of reflection", "reflect"]),
   P("the eye/brain assumes light travels in straight lines and traces the rays back", ["straight lines", "traces back", "assumes", "extend the rays back"]),
   P("the traced-back rays meet behind the mirror, where the (virtual) image appears", ["meet behind the mirror", "behind the mirror", "virtual image", "appear to come from"])],
  "Rays from the object strike the mirror and are reflected into the eye, obeying the law of reflection. The eye and brain assume light travels in straight lines, so they trace the reflected rays back. These lines meet at a point behind the mirror, where the virtual image appears to be.",
  ["What happens to rays from the object at the mirror?", "How does the brain judge where light came from?", "Where do the traced-back rays meet?"],
  "reflected rays traced back in straight lines meet behind the mirror",
  ["Rays reflect off the mirror into the eye, and the brain traces them back in straight lines to a point behind the mirror, where the virtual image appears", "the reflected rays seem to come from behind the mirror because the eye extends them back"],
  ["Light passes through the mirror to the image", "The image is painted on the mirror"], min_points=2)

Q("w11b_fish_spear", 4, "11c", "A fisherman sees a fish in clear water. Explain why he must aim his spear below where the fish appears to be.",
  [P("light from the fish refracts away from the normal as it leaves the water", ["refracts", "away from the normal", "bends", "refraction"]),
   P("the eye traces the rays back in straight lines, so the fish appears higher (shallower) than it is", ["appears higher", "shallower", "straight lines", "appears nearer the surface", "higher than"]),
   P("so the real fish is deeper, below the image", ["deeper", "below", "real position", "lower"])],
  "Light from the fish is refracted away from the normal as it leaves the water. The fisherman's eye traces the rays back in straight lines, so the fish appears higher, nearer the surface, than it really is. The real fish is deeper, so he must aim below the image.",
  ["What happens to light leaving the water?", "Where does the fish appear to be?", "Where is it really?"],
  "refraction makes fish appear higher; real fish deeper",
  ["Refraction at the surface makes the fish appear higher than it is, so the real fish is deeper and he must aim below it", "light bends away from the normal leaving the water, so the fish looks shallower"],
  ["Because the fish swims away", "The water magnifies the fish so aim above"], min_points=2)

Q("w11b_thick_thin_lens", 4, "11g", "Two converging lenses are made of the same glass. One is much more curved (fatter) than the other. Predict and explain which has the shorter focal length.",
  [P("the more curved (fatter) lens has the shorter focal length", ["more curved", "fatter", "shorter focal length", "fatter lens"]),
   P("its surfaces are more steeply angled, so rays meet them at larger angles and are bent more", ["bent more", "bends more", "larger angles", "more strongly", "steeper"]),
   P("so parallel rays converge closer to the lens", ["closer to the lens", "converge closer", "focus nearer", "nearer"])],
  "The more curved lens has the shorter focal length. Its surfaces are more steeply angled, so rays meet them at larger angles of incidence and are refracted more. Parallel rays are therefore brought to a focus closer to the lens.",
  ["How does the curvature affect the angles at which rays meet the surfaces?", "More bending means what for the focus?", "Predict."],
  "more curved → more bending → shorter focal length",
  ["The fatter lens has the shorter focal length because it bends the rays more, so they meet closer to the lens", "more curved surfaces refract light more strongly, focusing nearer the lens"],
  ["The thinner lens has the shorter focal length", "Both have the same focal length"], min_points=2)

Q("w11b_move_mirror", 4, "11b", "A girl stands still 2 m in front of a plane mirror. The mirror is moved 0.5 m further away from her. Explain how far her image moves and find the new distance between her and her image.",
  [P("the image is always as far behind the mirror as she is in front", ["as far behind", "same distance behind", "equal distance"]),
   P("the mirror is now 2.5 m from her, so the image is 2.5 m behind the mirror: 5 m from her", ["5 m", "5.0 m", "2.5 m behind"]),
   P("so the image moves 1 m (twice the mirror's movement)", ["1 m", "twice", "double", "1.0 m"])],
  "The image is always as far behind the mirror as she is in front of it. After the move the mirror is 2.5 m from her, so the image is 2.5 m behind the mirror, 5 m from her. Before, it was 4 m from her, so the image has moved 1 m, twice as far as the mirror moved.",
  ["Where is a plane mirror image?", "How far is the mirror from her now?", "Compare the old and new image distances."],
  "image 2.5 m behind mirror → 5 m from her; moved 1 m (twice the mirror)",
  ["The image is as far behind the mirror as she is in front, so it is 2.5 m behind the mirror and 5 m from her; it moved 1 m", "it is now 5 m from her, so the image moved twice as far as the mirror, 1 m"],
  ["The image moves 0.5 m and is 2.5 m from her", "The image does not move"], min_points=2)

# ---------------------------------------------------------------- L5
Q("w11b_see_more_claim", 5, "11b", "A student says: 'If I step back from a small plane mirror, my image gets smaller.' Evaluate this claim.",
  [P("wrong: the image is always the same size as the object", ["wrong", "same size", "does not get smaller", "always the same size"]),
   P("it moves further behind the mirror (same distance behind as she is in front)", ["further behind", "same distance behind", "moves back", "further away"]),
   P("it only looks smaller because it is further from the eye (smaller angle)", ["looks smaller", "further away", "appears smaller", "smaller angle", "further from the eye"])],
  "The claim is wrong. The image in a plane mirror is always the same size as the object. When she steps back, the image moves further behind the mirror, so it is further from her eye and only looks smaller, in the same way that any object looks smaller from further away.",
  ["Does a plane mirror image change size?", "Where does the image move?", "Why might it look smaller?"],
  "wrong; same size; further away so appears smaller",
  ["Wrong: the image stays the same size but moves further behind the mirror, so it only looks smaller because it is further away", "the image is always the same size; it appears smaller because it is further from the eye"],
  ["Correct, the image shrinks", "Correct, mirrors make distant things smaller"], min_points=2)

Q("w11b_normal_incidence_claim", 5, "11c", "A student says: 'Light only slows down in glass if it hits the glass at an angle.' Evaluate this claim.",
  [P("wrong: light slows down in glass whatever the angle", ["wrong", "always slows", "slows down whatever", "any angle", "still slows down"]),
   P("at normal incidence (along the normal) it slows down but does not change direction", ["along the normal", "normal incidence", "does not change direction", "does not bend", "0°"]),
   P("bending only happens when it meets the boundary at an angle", ["at an angle", "bending only", "only bends", "changes direction only"])],
  "The claim is wrong. Light always slows down when it enters glass. When it travels along the normal (angle of incidence 0°), it slows down but does not change direction; it only bends when it meets the boundary at an angle.",
  ["Does the speed of light in glass depend on the angle?", "What happens to a ray along the normal?", "When does bending happen?"],
  "wrong; always slows; along normal: slows, no bending",
  ["Wrong: light always slows down in glass; along the normal it slows but does not bend, and it bends only at an angle", "it slows down at any angle, but only changes direction when it is not along the normal"],
  ["Correct, light at 90° does not slow down", "Correct, only angled light enters the glass"], min_points=2)

Q("w11b_compare_n_design", 5, "11d", "Design an experiment to compare the refractive indices of a glass block and a perspex block of the same shape.",
  [P("for each block, trace rays at several angles of incidence and measure the angles of refraction", ["several angles", "trace rays", "measure the angles", "ray box", "angles of refraction"]),
   P("calculate sin i ÷ sin r for each pair (or plot sin i against sin r and find the gradient)", ["sin i ÷ sin r", "sin i / sin r", "gradient", "plot sin i"]),
   P("compare the average values: the larger value is the higher refractive index", ["compare", "average", "larger value", "higher refractive index", "mean"])],
  "For each block, shine rays from a ray box at several different angles of incidence, trace them and measure the angles of refraction with a protractor. Calculate sin i ÷ sin r for each pair and average them (or plot sin i against sin r and find the gradient). Compare the two values: the block with the larger value has the higher refractive index.",
  ["What measurements do you need for each block?", "How do you turn them into a refractive index?", "How do you compare?"],
  "trace rays at several i; sin i ÷ sin r (or gradient); compare averages",
  ["For each block measure r at several angles of incidence, work out sin i ÷ sin r and average, then compare the two values", "plot sin i against sin r for each block and compare the gradients"],
  ["Weigh the blocks", "Compare how clear the blocks look"], min_points=2)

Q("w11b_real_image_claim", 5, "11h", "A student says: 'A real image is one that you can actually see, and a virtual image cannot be seen.' Evaluate this.",
  [P("wrong: virtual images can be seen too (e.g. in a plane mirror or magnifying glass)", ["wrong", "virtual images can be seen", "can see a virtual", "mirror", "magnifying glass"]),
   P("a real image is where rays actually meet, so it can be formed on a screen", ["rays actually meet", "formed on a screen", "on a screen", "actually converge"]),
   P("a virtual image is where rays only appear to come from; it cannot be formed on a screen", ["appear to come from", "cannot be formed on a screen", "only appear", "rays do not meet"])],
  "The statement is wrong. Virtual images can be seen: you see one every time you look in a plane mirror. The difference is that a real image is where light rays actually meet, so it can be formed on a screen; a virtual image is where rays only appear to come from, so it cannot be formed on a screen.",
  ["Can you see your image in a mirror? Is it real or virtual?", "What is the real definition of a real image?", "And of a virtual image?"],
  "wrong; both can be seen; real = rays meet (screen); virtual = rays only appear to come from",
  ["Wrong: you can see virtual images in a mirror; a real image is where rays actually meet and can be put on a screen, while a virtual image cannot", "a virtual image can be seen too, but it cannot be formed on a screen because the rays only appear to come from it"],
  ["Correct, virtual images are invisible", "Correct, only real images exist"], min_points=2)

Q("w11b_projector_vs_camera", 5, "11h", "A projector forms a large image of a small slide; a camera forms a small image of a large scene. Evaluate how the object distance compared with the focal length differs in each case, using ray diagram ideas.",
  [P("projector: object (slide) between F and 2F, giving a real, inverted, magnified image far from the lens", ["between f and 2f", "magnified", "close to f", "just beyond f"]),
   P("camera: object far beyond 2F, giving a real, inverted, diminished image near F", ["beyond 2f", "far away", "diminished", "near f", "close to the focal point"]),
   P("both images are real and inverted", ["real", "inverted", "both"])],
  "In both cases the images are real and inverted. In a projector the slide is placed just beyond F (between F and 2F), so the image is magnified and formed far from the lens, on the screen. In a camera the scene is far beyond 2F, so the image is diminished and formed close to F, on the sensor.",
  ["Where is the slide compared with F in a projector?", "Where is the scene compared with 2F in a camera?", "What do the images have in common?"],
  "projector: F<u<2F (magnified); camera: u>2F (diminished); both real, inverted",
  ["In a projector the slide is between F and 2F so the image is magnified, while in a camera the object is beyond 2F so the image is diminished; both are real and inverted", "projector object just beyond F, camera object far beyond 2F; both give real inverted images"],
  ["Both objects are inside F", "The projector image is virtual"], min_points=2)

Q("w11b_angle_from_surface_error", 5, "11a", "A student measures the 'angle of incidence' as 30° between the ray and the mirror surface, and gets an 'angle of reflection' of 60° from the normal. She concludes the law of reflection is wrong. Evaluate her conclusion.",
  [P("her conclusion is wrong: she measured the incident angle from the surface, not the normal", ["measured from the surface", "not the normal", "wrong", "mistake", "error"]),
   P("the true angle of incidence is 90° − 30° = 60°", ["90 − 30", "90 - 30", "60", "true angle"]),
   P("which equals the angle of reflection (60°), so the law holds", ["equals", "law holds", "agrees", "same as the angle of reflection", "law is correct"])],
  "Her conclusion is wrong because she made a measurement error: she measured the angle of incidence from the mirror surface instead of from the normal. The true angle of incidence is 90° − 30° = 60°, which equals the angle of reflection of 60°, so her results actually agree with the law of reflection.",
  ["From which line should the angle of incidence be measured?", "What is the true angle of incidence?", "Does it now agree?"],
  "measured from surface; true i = 60° = r; law holds",
  ["Wrong: she measured the angle from the surface, so the real angle of incidence is 60°, which equals the angle of reflection, so the law holds", "it is a measurement error; 90 − 30 = 60, the same as the reflection angle"],
  ["She is right, the law is wrong", "Angles should be measured from the surface"], min_points=2)

Q("w11b_corner_reflector", 5, "11b", "Bicycle reflectors contain many pairs of tiny mirrors (or surfaces) at 90° to each other. Evaluate why this sends light back towards a car's headlights.",
  [P("light reflects off one surface and then the other", ["reflects twice", "two reflections", "one surface and then the other", "reflects off both"]),
   P("with surfaces at 90°, the two reflections turn the ray through 180°", ["180", "turned back", "opposite direction", "reverses"]),
   P("so the light returns parallel to its original path, back to the driver, whatever the angle", ["back to the driver", "back towards the car", "parallel to its original path", "whatever the angle", "returns"])],
  "Light entering a corner made of two surfaces at 90° is reflected off one surface and then the other. With the surfaces at right angles, the two reflections together turn the ray through 180°, so it returns parallel to its original path, back towards the car's headlights and the driver, for a wide range of angles.",
  ["How many times is the light reflected?", "What is the total change in direction?", "Where does the light go?"],
  "two reflections at 90° → turned through 180° → back to driver",
  ["The light reflects off both surfaces, and because they are at 90° it is turned through 180° and goes back towards the car", "two reflections at right angles send the light back parallel to its path, to the driver"],
  ["The reflector glows by itself", "The light passes through the reflector"], min_points=2)

Q("w11b_magnifier_screen_claim", 5, "11h", "A student says: 'I can catch the image from my magnifying glass on a sheet of paper.' Evaluate this claim.",
  [P("wrong (when used as a magnifier, object inside F)", ["wrong", "cannot", "not possible"]),
   P("the image is virtual: the rays only appear to come from it, so it cannot be formed on paper", ["virtual", "cannot be formed on", "only appear to come from", "rays do not meet"]),
   P("a real image could be formed only if the object is further than F from the lens (e.g. a distant window)", ["further than f", "beyond f", "distant object", "real image", "window"])],
  "As a magnifier, with the object closer than F, the claim is wrong: the image is virtual, because the rays only appear to come from it, so it cannot be caught on paper. The same lens can form a real image on paper only if the object is further than F from the lens, such as a distant window.",
  ["Is a magnifying-glass image real or virtual?", "Can a virtual image be put on paper?", "When could this lens make a real image?"],
  "magnifier image virtual → not on paper; real only if object beyond F",
  ["Wrong: as a magnifier the image is virtual, so it cannot be formed on paper; only an object beyond F gives a real image", "the magnified image is virtual since the rays do not meet, so it cannot be caught on a screen"],
  ["Correct, all lens images can be put on paper", "Correct, magnified images are always real"], min_points=2)

Q("w11b_n_depends_material", 5, "11d", "A student says: 'Every transparent material bends light by the same amount, because light always slows to the same speed in solids.' Evaluate this.",
  [P("wrong: different materials have different refractive indices", ["wrong", "different refractive indices", "different materials", "differs"]),
   P("light slows by different amounts in different materials (n = c ÷ v)", ["different amounts", "different speeds", "n = c ÷ v", "c / v"]),
   P("so for the same angle of incidence, a higher n gives more bending (e.g. diamond 2.4 vs glass 1.5)", ["higher n", "more bending", "diamond", "glass 1.5", "2.4"])],
  "The statement is wrong. Different materials have different refractive indices, because light slows down by different amounts in them (n = c ÷ v). For the same angle of incidence, a material with a higher refractive index, such as diamond (2.4) compared with glass (1.5), bends the light more.",
  ["Is the refractive index the same for all materials?", "What does n tell you about the speed?", "Give an example."],
  "wrong; different n, different speeds; higher n bends more",
  ["Wrong: different materials have different refractive indices because light slows by different amounts, so diamond bends light more than glass", "light travels at different speeds in different materials, so the bending differs"],
  ["Correct, all solids have n = 1.5", "Correct, light has one speed in all solids"], min_points=2)

Q("w11b_half_covered_lens", 5, "11h", "A student covers the top half of a converging lens that is forming a real image of a lamp on a screen. She predicts that the top half of the image will disappear. Evaluate this prediction.",
  [P("wrong: the whole image is still formed", ["wrong", "whole image", "complete image", "still formed", "all of the image"]),
   P("light from every point of the lamp passes through the uncovered half and still reaches every image point", ["every point", "uncovered half", "bottom half", "still reaches", "rays from each point"]),
   P("but the image is dimmer, because less light passes through the lens", ["dimmer", "less bright", "less light", "fainter"])],
  "The prediction is wrong. Light from every point on the lamp spreads out and reaches all parts of the lens, so rays from each point still pass through the uncovered half and meet at the corresponding image point. The whole image is still formed, but it is dimmer because only half as much light passes through the lens.",
  ["Does light from one point of the lamp go through only one part of the lens?", "What happens to the image points?", "What changes?"],
  "wrong; whole image formed; dimmer",
  ["Wrong: light from every point still passes through the uncovered half, so the whole image forms, but it is dimmer", "the complete image is still there but fainter because less light gets through"],
  ["Correct, half the image disappears", "The image disappears completely"], min_points=2)
