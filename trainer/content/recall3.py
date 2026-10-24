"""Explanation category for Chapters 11-16: recall (L1), identify / classify (L2) and apply (L3) MCQs, with diagrams."""
from .. import sketches2 as sk
from .base import template, text_options

RECALL3 = [
    # ------------------------------------------------------------ Chapter 11 Light
    dict(id="r11_law_of_reflection", chapter=11, level=1, lo="11b",
         stem="Fig. 1 shows a ray reflected by a plane mirror. Which statement is the law of reflection?",
         correct="The angle of incidence is equal to the angle of reflection.",
         wrongs={"The angle of incidence is twice the angle of reflection.": "The two angles are always EQUAL.",
                 "The reflected ray is always at right angles to the mirror.": "The reflected ray leaves at the same angle to the normal as the incident ray arrived.",
                 "The angle of incidence plus the angle of reflection is 90°.": "They add to 2i, not to 90°; each is measured from the normal."},
         hints=["Both angles are measured between a ray and the normal. How do they compare?",
                "Think of a ball bouncing off a wall symmetrically.",
                "Rule out the options that contradict what you know, then choose the one that matches the law exactly."],
         figure=lambda: sk.reflection_diagram(40)),
    dict(id="r11_normal_definition", chapter=11, level=1, lo="11a",
         stem="In the study of reflection and refraction, the normal is",
         correct="a line at right angles to the surface at the point where the ray meets it",
         wrongs={"the incident ray": "The incident ray is the ray arriving at the surface.",
                 "a line along the surface of the mirror": "The normal is perpendicular to the surface, not along it.",
                 "the ray that passes straight through without bending": "That is a ray travelling along the normal, not the normal itself."},
         hints=["Angles of incidence and reflection are measured from this line.",
                "It is a construction line, not a ray, drawn perpendicular to the surface.",
                "Rule out the options that describe rays rather than a construction line."]),
    dict(id="r11_refraction_cause", chapter=11, level=2, lo="11c",
         stem="Fig. 1 shows a ray of light passing from air into glass. Why does the ray bend towards the normal?",
         correct="Light travels more slowly in glass than in air.",
         wrongs={"Light travels faster in glass than in air.": "Light is SLOWER in glass; that is why it bends towards the normal.",
                 "The glass absorbs part of the light.": "Absorption affects brightness, not the direction of the ray.",
                 "The glass surface reflects the light.": "Some reflection does occur, but refraction is the change of direction of the light that enters."},
         hints=["Refraction happens when the speed of light changes between two media.",
                "Glass is optically denser than air: what does that do to the speed?",
                "Rule out the options about absorption and reflection, which do not change the direction of the transmitted ray."],
         figure=lambda: sk.refraction_diagram(45, 28)),
    dict(id="r11_refractive_index_def", chapter=11, level=1, lo="11e",
         stem="The refractive index of a medium is defined as",
         correct="the speed of light in a vacuum divided by the speed of light in the medium",
         wrongs={"the speed of light in the medium divided by the speed of light in a vacuum": "That ratio is less than 1; refractive index is defined the other way round and is greater than 1.",
                 "the angle of incidence divided by the angle of refraction": "It is the ratio of the SINES of the angles, not of the angles themselves.",
                 "the thickness of the medium divided by the wavelength": "Refractive index does not depend on thickness."},
         hints=["It is a ratio of two speeds, and it is always greater than 1 for glass or water.",
                "Which speed is larger: in a vacuum or in glass? Put the larger one on top.",
                "Rule out the options involving angles or thickness."]),
    dict(id="r11_plane_mirror_image", chapter=11, level=2, lo="11b",
         stem="Which set of characteristics describes the image of an object formed by a plane mirror?",
         correct="virtual, upright, same size, laterally inverted, same distance behind the mirror as the object is in front",
         wrongs={"real, inverted, same size, on the surface of the mirror": "A plane-mirror image is virtual and upright, and it appears BEHIND the mirror.",
                 "virtual, upright, magnified, in front of the mirror": "The image is the same size as the object and appears behind the mirror.",
                 "real, upright, diminished, behind the mirror": "The image cannot be formed on a screen, so it is virtual, and it is the same size as the object."},
         hints=["Look in a mirror: are you upside down? Bigger? Can the image be caught on a screen?",
                "Your left hand appears as a right hand: that is lateral inversion.",
                "Rule out any option that says real, inverted, magnified or diminished."]),
    dict(id="r11_converging_lens_action", chapter=11, level=1, lo="11f",
         stem="Fig. 1 shows a parallel beam of light passing through a thin converging lens. What does the lens do to the beam?",
         correct="It brings the rays together to a point called the principal focus.",
         wrongs={"It spreads the rays out so they never meet.": "That is a diverging lens. A converging lens brings rays together.",
                 "It reflects the rays back towards the source.": "A lens refracts light through itself; it does not reflect it back.",
                 "It leaves the rays parallel but slows them down.": "The rays are bent towards the axis so that they converge."},
         hints=["The name of the lens tells you what happens to the rays.",
                "Parallel rays meet at one point after the lens. What is that point called?",
                "Rule out the options describing diverging or reflecting."],
         figure=lambda: sk.lens_parallel_beam(2.0)),
    dict(id="r11_focal_length_def", chapter=11, level=1, lo="11g",
         stem="The focal length of a converging lens is",
         correct="the distance between the optical centre of the lens and the principal focus",
         wrongs={"the distance between the object and the lens": "That is the object distance, which can be anything.",
                 "the distance between the two principal foci": "That is twice the focal length.",
                 "the thickness of the lens": "Focal length depends on the curvature, not on the thickness measured across the lens."},
         hints=["It is measured from the centre of the lens to one particular point.",
                "That point is where parallel rays are brought together.",
                "Rule out the options about the object, the two foci or the thickness."]),
    dict(id="r11_real_vs_virtual", chapter=11, level=3, lo="11h",
         stem="Fig. 1 shows an object placed between a converging lens and its principal focus F. Which row describes the image?",
         correct="virtual, upright, magnified, on the same side of the lens as the object",
         wrongs={"real, inverted, magnified, on the opposite side of the lens": "An object inside F gives a VIRTUAL, upright image: the rays only appear to come from it.",
                 "real, inverted, diminished, on the opposite side of the lens": "That is the image of an object beyond 2F.",
                 "virtual, inverted, same size, behind the lens": "The image is upright and magnified, as in a magnifying glass."},
         hints=["This is how a magnifying glass is used. What does a magnifying glass show you?",
                "The refracted rays diverge, so they must be traced back to find the image.",
                "Rule out any option with 'real' or 'inverted'."],
         figure=lambda: sk.lens_diagram(1.4, 2, h=0.8)),
]


def _register(item):
    @template(item["id"], chapter=item["chapter"], level=item["level"], lo=item["lo"], category="explain")
    def make(rng, item=item):
        opts, key, mis = text_options(rng, item["correct"], item["wrongs"])
        fig = item.get("figure")
        hints = [h if "___" not in h else "Rule out the options that contradict what you know, then choose the one that matches the definition exactly." for h in item["hints"]]
        return dict(stem=item["stem"], options=opts, key=key, misconceptions=mis, hints=hints,
                    working=[f"Correct statement: **{item['correct']}**"], formula=None, figure=fig() if fig else None)


for _item in RECALL3:
    _register(_item)
