"""Diagrams for the 'O level 2026 MCQ practice' category (adapted SEAB MCQs): echoes, hill track, windlass, piston, water tank,
mirror and boundary rays, field between magnet ends, compasses around two magnets (field computed numerically), wires in fields.
Magnetic directions are computed (cross products / pole model), never drawn by hand, so a figure cannot contradict its key."""
import math

import matplotlib

matplotlib.use("Agg")
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Polygon, Rectangle

from .figs import _cylinder, _fig, _png


def _arrow(ax, p0, p1, lw=1.6, ms=13, color="black", ls="-"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=ms, lw=lw, color=color, linestyle=ls))


def _dim(ax, p0, p1, text, off=(0, -0.3), fs=10):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="<|-|>", mutation_scale=10, lw=1.0, color="black"))
    ax.text((p0[0] + p1[0]) / 2 + off[0], (p0[1] + p1[1]) / 2 + off[1], text, ha="center", va="center", fontsize=fs,
            bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none"))


def _person(ax, x, label):
    ax.add_patch(Circle((x, 1.45), 0.18, fc="white", ec="black", lw=1.3))
    ax.plot([x, x], [1.27, 0.6], color="black", lw=1.3)
    ax.plot([x, x - 0.25], [0.6, 0], color="black", lw=1.3)
    ax.plot([x, x + 0.25], [0.6, 0], color="black", lw=1.3)
    ax.plot([x - 0.3, x + 0.3], [1.05, 1.05], color="black", lw=1.3)
    ax.text(x, 1.75, label, ha="center", va="bottom", fontsize=9.5)


# ------------------------------------------------------------------ Ch 9 echoes
def building_echo(d_wall, d_listener):
    """Building on the left, girl (pistol) d_wall in front of it, boy d_listener further away."""
    fig, ax = _fig(6.8, 2.6)
    ax.plot([-0.2, 7.2], [0, 0], color="black", lw=1.4)
    ax.add_patch(Rectangle((0, 0), 1.2, 2.4, fc="#dddddd", ec="black", lw=1.5))
    for y in (0.5, 1.1, 1.7):
        for x in (0.2, 0.7):
            ax.add_patch(Rectangle((x, y), 0.3, 0.35, fc="white", ec="black", lw=0.8))
    ax.text(0.6, 2.5, "building", ha="center", va="bottom", fontsize=9.5)
    _person(ax, 3.0, "girl (pistol)")
    _person(ax, 6.6, "boy")
    _dim(ax, (1.2, -0.45), (3.0, -0.45), d_wall, off=(0, -0.3))
    _dim(ax, (3.0, -0.45), (6.6, -0.45), d_listener, off=(0, -0.3))
    ax.set_xlim(-0.3, 7.3)
    ax.set_ylim(-1.2, 3.0)
    return _png(fig)


def between_cliffs(d_left, d_right):
    """A person standing between two cliffs."""
    fig, ax = _fig(6.6, 2.6)
    ax.plot([0, 7.0], [0, 0], color="black", lw=1.4)
    ax.add_patch(Polygon([(0, 0), (0, 2.4), (0.7, 2.4), (0.9, 0)], fc="#cccccc", ec="black", lw=1.5))
    ax.add_patch(Polygon([(7.0, 0), (7.0, 2.4), (6.3, 2.4), (6.1, 0)], fc="#cccccc", ec="black", lw=1.5))
    ax.text(0.4, 2.5, "cliff", ha="center", va="bottom", fontsize=9.5)
    ax.text(6.6, 2.5, "cliff", ha="center", va="bottom", fontsize=9.5)
    _person(ax, 4.0, "man")
    _dim(ax, (0.9, -0.45), (4.0, -0.45), d_left)
    _dim(ax, (4.0, -0.45), (6.1, -0.45), d_right)
    ax.set_xlim(-0.2, 7.2)
    ax.set_ylim(-1.2, 3.0)
    return _png(fig)


# ------------------------------------------------------------------ Ch 6 energy
def hill_track(peak_label, end_label, start="X", end="Y"):
    """Ball at X on the ground; the track rises over a hump of height peak, then levels off at a lower height at Y."""
    fig, ax = _fig(6.4, 2.8)
    xs = np.linspace(0, 6, 300)
    ys = np.where(xs < 1.5, 0, 0)
    hump = 2.0 * np.exp(-((xs - 3.0) / 0.7) ** 2)
    plateau = 1.4 / (1 + np.exp(-(xs - 3.3) * 6))
    ys = np.maximum(hump, plateau)
    ax.plot(xs, ys, color="black", lw=1.6)
    ax.add_patch(Circle((0.6, 0.2), 0.2, fc="white", ec="black", lw=1.4))
    _arrow(ax, (0.9, 0.2), (1.5, 0.2), lw=1.4, ms=12)
    ax.text(0.6, -0.15, start, ha="center", va="top", fontsize=11, fontweight="bold")
    ax.plot([5.4], [1.4], "o", color="black", markersize=4)
    ax.text(5.4, 1.55, end, ha="center", va="bottom", fontsize=11, fontweight="bold")
    ax.plot([0, 6.3], [0, 0], color="black", lw=0.8, ls="--")
    ax.plot([3.0, 6.3], [2.0, 2.0], color="black", lw=0.8, ls="--")
    ax.plot([5.4, 6.3], [1.4, 1.4], color="black", lw=0.8, ls="--")
    _dim(ax, (6.2, 0), (6.2, 2.0), "", off=(0, 0))
    ax.text(6.35, 1.0, peak_label, ha="left", va="center", fontsize=10)
    ax.text(5.25, 0.7, end_label, ha="right", va="center", fontsize=10)
    ax.add_patch(FancyArrowPatch((5.4, 0), (5.4, 1.4), arrowstyle="<|-|>", mutation_scale=10, lw=1.0, color="black"))
    ax.set_xlim(-0.2, 8.2)
    ax.set_ylim(-0.6, 2.5)
    return _png(fig)


def windlass(diam_label, handle_label, load_label):
    """Bucket lifted by a rope wound round a cylinder turned by a handle."""
    fig, ax = _fig(4.2, 3.8)
    ax.add_patch(Circle((0, 2.6), 0.9, fc="#eeeeee", ec="black", lw=1.6))
    ax.add_patch(Circle((0, 2.6), 0.12, fc="white", ec="black", lw=1.2))
    ax.plot([0, -0.8], [2.6, 3.3], color="black", lw=3.0)
    ax.add_patch(Circle((-0.8, 3.3), 0.1, fc="black", ec="black"))
    ax.text(-0.9, 3.45, "handle", ha="right", va="bottom", fontsize=9)
    ax.plot([0.9, 0.9], [2.6, 0.9], color="black", lw=1.4)
    ax.add_patch(Polygon([(0.45, 0.9), (1.35, 0.9), (1.2, 0.0), (0.6, 0.0)], fc="white", ec="black", lw=1.5))
    ax.text(1.5, 0.45, load_label, ha="left", va="center", fontsize=10)
    _dim(ax, (-0.9, 1.45), (0.9, 1.45), diam_label, off=(0, -0.25), fs=9.5)
    ax.text(-1.2, 2.2, handle_label, ha="right", va="center", fontsize=9.5)
    ax.text(0.0, 3.65, "cylinder", ha="center", va="bottom", fontsize=9)
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-0.3, 4.1)
    return _png(fig)


def mass_on_spring():
    fig, ax = _fig(2.6, 3.6)
    ax.plot([-0.9, 0.9], [3.2, 3.2], color="black", lw=2.0)
    for x in np.arange(-0.9, 0.9, 0.2):
        ax.plot([x, x + 0.15], [3.2, 3.4], color="black", lw=0.8)
    t = np.linspace(0, 1, 400)
    ax.plot(0.18 * np.sin(2 * np.pi * 12 * t), 3.2 - 1.9 * t, color="black", lw=1.2)
    ax.add_patch(Rectangle((-0.4, 0.9), 0.8, 0.4, fc="#dddddd", ec="black", lw=1.4))
    ax.text(0.55, 1.1, "mass", ha="left", va="center", fontsize=9.5)
    ax.add_patch(FancyArrowPatch((0.75, 2.0), (0.75, 2.9), arrowstyle="<|-|>", mutation_scale=10, lw=1.0, color="black"))
    ax.text(0.85, 2.45, "oscillates", ha="left", va="center", fontsize=8.5)
    ax.set_xlim(-1.1, 1.9)
    ax.set_ylim(0.7, 3.5)
    return _png(fig)


# ------------------------------------------------------------------ Ch 7-8
def piston_gas():
    fig, ax = _fig(4.4, 1.9)
    ax.plot([0, 3.4], [0, 0], color="black", lw=1.6)
    ax.plot([0, 3.4], [1.2, 1.2], color="black", lw=1.6)
    ax.plot([0, 0], [0, 1.2], color="black", lw=1.6)
    rng = np.random.default_rng(2)
    for _ in range(14):
        ax.add_patch(Circle((rng.uniform(0.15, 2.3), rng.uniform(0.15, 1.05)), 0.06, fc="#888888", ec="none"))
    ax.add_patch(Rectangle((2.45, 0.02), 0.25, 1.16, fc="#bbbbbb", ec="black", lw=1.3, hatch="///"))
    ax.add_patch(Rectangle((2.7, 0.5), 1.0, 0.2, fc="#bbbbbb", ec="black", lw=1.2))
    ax.text(1.2, -0.15, "gas", ha="center", va="top", fontsize=9.5)
    ax.text(2.6, 1.3, "frictionless piston", ha="center", va="bottom", fontsize=9)
    ax.set_xlim(-0.2, 3.9)
    ax.set_ylim(-0.5, 1.7)
    return _png(fig)


def water_tank(heater="top"):
    """Insulated metal tank of water with an electric heater near the top (or bottom)."""
    fig, ax = _fig(3.0, 3.8)
    ax.add_patch(Rectangle((0, 0), 2.0, 3.4, fc="#bbbbbb", ec="black", lw=1.4))
    ax.add_patch(Rectangle((0.15, 0.15), 1.7, 3.1, fc="#e4edf6", ec="black", lw=1.0))
    y = 2.8 if heater == "top" else 0.6
    xs = np.linspace(0.15, 1.1, 200)
    ax.plot(xs, y + 0.08 * np.sin(xs * 40), color="#c00000", lw=1.6)
    ax.plot([-0.5, 0.15], [y, y], color="black", lw=1.2)
    ax.text(2.15, y, "heater", ha="left", va="center", fontsize=9)
    ax.text(2.15, 1.6, "water", ha="left", va="center", fontsize=9)
    ax.text(2.15, 0.07, "insulation", ha="left", va="center", fontsize=9)
    ax.set_xlim(-0.6, 3.3)
    ax.set_ylim(-0.2, 3.6)
    return _png(fig)


def cylinder_stone(level_ml, max_ml=10, step_ml=1, minor_ml=0.2):
    """One measuring cylinder holding water with a stone in it."""
    fig, ax = _fig(2.0, 4.2)
    _cylinder(ax, 0, level_ml, max_ml, step_ml, minor_ml, stone=True)
    ax.set_xlim(-0.7, 2.9)
    ax.set_ylim(-0.6, 11.0)
    return _png(fig)


# ------------------------------------------------------------------ Ch 11 rays
def mirror_angles(i):
    """Vertical plane mirror; X = angle between incident and reflected rays, Y = angle between reflected ray and mirror."""
    fig, ax = _fig(4.0, 3.2)
    ax.plot([0, 0], [-1.6, 1.6], color="black", lw=2.2)
    for y in np.arange(-1.6, 1.6, 0.2):
        ax.plot([0, 0.15], [y, y + 0.12], color="black", lw=0.8)
    a = math.radians(i)
    L = 2.4
    p_in = (-L * math.cos(a), L * math.sin(a))
    p_out = (-L * math.cos(a), -L * math.sin(a))
    ax.plot([p_in[0], 0], [p_in[1], 0], color="black", lw=1.6)
    ax.plot([0, p_out[0]], [0, p_out[1]], color="black", lw=1.6)
    _arrow(ax, (p_in[0] * 0.55, p_in[1] * 0.55), (p_in[0] * 0.5, p_in[1] * 0.5), ms=13)
    _arrow(ax, (p_out[0] * 0.5, p_out[1] * 0.5), (p_out[0] * 0.55, p_out[1] * 0.55), ms=13)
    ax.add_patch(Arc((0, 0), 1.2, 1.2, angle=180 - i, theta1=0, theta2=2 * i, lw=1.0))
    ax.text(-0.85, 0.0, "X", ha="center", va="center", fontsize=11, fontstyle="italic")
    ax.add_patch(Arc((0, 0), 0.8, 0.8, angle=180 + i, theta1=0, theta2=90 - i, lw=1.0))
    m = math.radians(225 + i / 2)
    ax.text(0.62 * math.cos(m), 0.62 * math.sin(m), "Y", ha="center", va="center", fontsize=11, fontstyle="italic")
    ax.text(-L * math.cos(a) - 0.1, L * math.sin(a) + 0.1, "incident ray", ha="center", va="bottom", fontsize=9)
    ax.set_xlim(-3.0, 0.6)
    ax.set_ylim(-1.9, 2.1)
    return _png(fig)


def boundary_deviation(i, label="θ"):
    """Ray hits a horizontal boundary at angle i to the normal; reflected ray drawn; dashed line = path with no boundary."""
    fig, ax = _fig(4.6, 3.2)
    ax.plot([-2.8, 2.8], [0, 0], color="black", lw=2.0)
    ax.text(2.7, 0.1, "boundary", ha="right", va="bottom", fontsize=9)
    ax.plot([0, 0], [0, 2.4], color="black", lw=0.9, ls="--")
    ax.text(0.08, 2.35, "normal", ha="left", va="top", fontsize=8.5)
    a = math.radians(i)
    L = 2.3
    ax.plot([-L * math.sin(a), 0], [L * math.cos(a), 0], color="black", lw=1.6)
    _arrow(ax, (-L * math.sin(a) * 0.55, L * math.cos(a) * 0.55), (-L * math.sin(a) * 0.5, L * math.cos(a) * 0.5))
    ax.plot([0, L * math.sin(a)], [0, L * math.cos(a)], color="black", lw=1.6)
    _arrow(ax, (L * math.sin(a) * 0.5, L * math.cos(a) * 0.5), (L * math.sin(a) * 0.55, L * math.cos(a) * 0.55))
    ax.plot([0, L * math.sin(a) * 0.8], [0, -L * math.cos(a) * 0.8], color="black", lw=1.0, ls=":")
    ax.add_patch(Arc((0, 0), 1.2, 1.2, angle=90, theta1=0, theta2=i, lw=1.0))
    m = math.radians(i / 2)
    ax.text(-1.35 * math.sin(m), 1.35 * math.cos(m), f"{i}°", ha="center", va="center", fontsize=9.5)
    ax.add_patch(Arc((0, 0), 0.8, 0.8, angle=-(90 - i), theta1=0, theta2=180 - 2 * i, lw=1.0))
    ax.text(0.62, 0.08, label, ha="left", va="bottom", fontsize=11)
    ax.text(L * math.sin(a) * 0.8, -L * math.cos(a) * 0.8 - 0.1, "path with no boundary", ha="center", va="top", fontsize=8)
    ax.set_xlim(-2.9, 2.9)
    ax.set_ylim(-2.3, 2.6)
    return _png(fig)


def two_mirrors(i):
    """Two plane mirrors at right angles (corner at the origin, mirrors along the axes); ray hits the vertical one at angle i."""
    fig, ax = _fig(3.8, 3.4)
    ax.plot([0, 0], [0, 3.0], color="black", lw=2.2)
    ax.plot([0, 3.0], [0, 0], color="black", lw=2.2)
    for y in np.arange(0.1, 3.0, 0.2):
        ax.plot([0, -0.15], [y, y - 0.12], color="black", lw=0.8)
    for x in np.arange(0.1, 3.0, 0.2):
        ax.plot([x, x - 0.12], [0, -0.15], color="black", lw=0.8)
    a = math.radians(i)
    y1 = 1.9
    # incident ray travels left and down, at angle i to the normal of the vertical mirror (the normal is horizontal)
    d_in = (-math.cos(a), -math.sin(a))
    start = (0 - d_in[0] * 3.0, y1 - d_in[1] * 3.0)
    ax.plot([start[0], 0], [start[1], y1], color="black", lw=1.6)
    _arrow(ax, ((start[0]) * 0.5, (start[1] + y1) / 2), ((start[0]) * 0.45, (start[1] * 0.45 + y1 * 0.55)))
    d1 = (math.cos(a), -math.sin(a))
    t = y1 / math.sin(a)
    p2 = (d1[0] * t, 0)
    ax.plot([0, p2[0]], [y1, 0], color="black", lw=1.6)
    d2 = (math.cos(a), math.sin(a))
    end = (p2[0] + d2[0] * 1.6, d2[1] * 1.6)
    ax.plot([p2[0], end[0]], [0, end[1]], color="black", lw=1.6)
    _arrow(ax, (p2[0] + d2[0] * 0.8, d2[1] * 0.8), (p2[0] + d2[0] * 0.9, d2[1] * 0.9))
    ax.add_patch(Arc((0, y1), 0.9, 0.9, angle=0, theta1=0, theta2=i, lw=1.0))
    ax.plot([0, 0.9], [y1, y1], color="black", lw=0.8, ls="--")
    ax.text(0.55, y1 + 0.28, f"{i}°", ha="left", va="center", fontsize=9.5)
    ax.set_xlim(-0.4, max(3.2, end[0] + 0.2))
    ax.set_ylim(-0.4, max(3.2, start[1] + 0.2))
    return _png(fig)


def boundary_ray_up(i, r, lower="medium S", upper="medium T"):
    """Ray travels upwards from the lower medium into the upper one; angles to the normal i (lower) and r (upper)."""
    fig, ax = _fig(3.8, 3.6)
    ax.add_patch(Rectangle((-2, -2), 4, 2, fc="#d9d9d9", ec="none"))
    ax.plot([-2, 2], [0, 0], color="black", lw=1.4)
    ax.plot([0, 0], [-2, 2], color="black", lw=0.9, ls="--")
    ax.text(1.95, -0.15, lower, ha="right", va="top", fontsize=9.5)
    ax.text(1.95, 0.15, upper, ha="right", va="bottom", fontsize=9.5)
    a, b = math.radians(i), math.radians(r)
    p0 = (-1.9 * math.tan(a), -1.9)
    p1 = (1.9 * math.tan(b), 1.9)
    ax.plot([p0[0], 0], [p0[1], 0], color="black", lw=1.6)
    ax.plot([0, p1[0]], [0, p1[1]], color="black", lw=1.6)
    _arrow(ax, (p0[0] * 0.55, p0[1] * 0.55), (p0[0] * 0.45, p0[1] * 0.45))
    _arrow(ax, (p1[0] * 0.45, p1[1] * 0.45), (p1[0] * 0.55, p1[1] * 0.55))
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-2.1, 2.1)
    return _png(fig)


# ------------------------------------------------------------------ Ch 15 magnetism
def _magnet(ax, x, y, w, h, left, right, vertical=False, shade_left=True):
    """Bar magnet; left/right are the end labels ('' for unlabelled)."""
    if vertical:
        ax.add_patch(Rectangle((x - h / 2, y - w / 2), h, w, fc="#eeeeee", ec="black", lw=1.4, zorder=5))
        ax.text(x, y + w / 2 - 0.25, left, ha="center", va="center", fontsize=11, fontweight="bold", zorder=6)
        ax.text(x, y - w / 2 + 0.25, right, ha="center", va="center", fontsize=11, fontweight="bold", zorder=6)
    else:
        ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, fc="#eeeeee", ec="black", lw=1.4, zorder=5))
        ax.text(x - w / 2 + 0.25, y, left, ha="center", va="center", fontsize=11, fontweight="bold", zorder=6)
        ax.text(x + w / 2 - 0.25, y, right, ha="center", va="center", fontsize=11, fontweight="bold", zorder=6)


def field_between_ends(kind):
    """Two bar magnets end to end; facing ends labelled X (left magnet) and Y (right magnet).
    kind: 'unlike_lr' (lines straight across, arrows left to right: X = N, Y = S), 'unlike_rl' (X = S, Y = N),
    'like_in' (lines bend away, arrows INTO both ends: both S), 'like_out' (arrows OUT of both ends: both N)."""
    fig, ax = _fig(5.6, 2.6)
    _magnet(ax, -2.0, 0, 2.2, 0.7, "", "X")
    _magnet(ax, 2.0, 0, 2.2, 0.7, "Y", "")
    gx0, gx1 = -0.9, 0.9
    if kind.startswith("unlike"):
        for yv in (-0.25, 0.0, 0.25):
            p0, p1 = ((gx0, yv), (gx1, yv)) if kind == "unlike_lr" else ((gx1, yv), (gx0, yv))
            _arrow(ax, p0, p1, lw=1.1, ms=10)
        for s in (1, -1):
            xs = np.linspace(gx0, gx1, 60)
            ax.plot(xs, s * (0.45 + 0.35 * np.sin((xs - gx0) / (gx1 - gx0) * np.pi)), color="black", lw=1.0)
    else:
        inward = kind == "like_in"
        t = np.linspace(0, 1, 40)
        for x0, side in ((gx0, 1), (gx1, -1)):            # X end lines run right, Y end lines run left
            for sgn in (1, -1):
                for spread in (0.12, 0.28):
                    xs = x0 + side * 0.75 * (1 - (1 - t) ** 2)
                    ys = sgn * (spread + 1.0 * t ** 2)
                    ax.plot(xs, ys, color="black", lw=1.0)
                    near, far = (xs[14], ys[14]), (xs[22], ys[22])
                    _arrow(ax, far, near, lw=1.0, ms=9) if inward else _arrow(ax, near, far, lw=1.0, ms=9)
    ax.set_xlim(-3.3, 3.3)
    ax.set_ylim(-1.5, 1.5)
    return _png(fig)


def _field(px, py, poles):
    """Field of point poles (strength +1 = N, -1 = S) at (px, py)."""
    bx = by = 0.0
    for (x, y, q) in poles:
        dx, dy = px - x, py - y
        r3 = (dx * dx + dy * dy) ** 1.5 + 1e-9
        bx += q * dx / r3
        by += q * dy / r3
    return bx, by


def compasses_two_magnets(wrong="R"):
    """Two identical bar magnets in a line (S N  N S); compasses P-S; the needle of `wrong` is drawn reversed.
    Every other needle points along the field computed from a point-pole model."""
    fig, ax = _fig(6.6, 2.8)
    poles = [(-3.3, 0, -1), (-0.9, 0, 1), (0.9, 0, 1), (3.3, 0, -1)]
    _magnet(ax, -2.1, 0, 2.6, 0.6, "S", "N")
    _magnet(ax, 2.1, 0, 2.6, 0.6, "N", "S")
    spots = {"P": (-4.1, 0), "Q": (-2.1, 0.95), "R": (2.1, -0.95), "S": (4.1, 0)}
    truth = {}
    for name, (x, y) in spots.items():
        bx, by = _field(x, y, poles)
        n = math.hypot(bx, by)
        ux, uy = bx / n, by / n
        truth[name] = (ux, uy)
        if name == wrong:
            ux, uy = -ux, -uy
        ax.add_patch(Circle((x, y), 0.36, fc="white", ec="black", lw=1.3))
        _arrow(ax, (x - 0.26 * ux, y - 0.26 * uy), (x + 0.26 * ux, y + 0.26 * uy), lw=1.4, ms=11)
        if y < 0:
            ax.text(x, y - 0.5, name, ha="center", va="top", fontsize=11, fontweight="bold")
        else:
            ax.text(x, y + 0.5, name, ha="center", va="bottom", fontsize=11, fontweight="bold")
    ax.set_xlim(-4.7, 4.7)
    ax.set_ylim(-1.9, 1.6)
    return _png(fig)


def wire_in_vertical_field(electron_flow="right"):
    """Horizontal wire across vertical field lines (field up the page); arrow shows the direction of ELECTRON flow."""
    fig, ax = _fig(4.4, 2.8)
    for x in (-1.2, -0.6, 0.0, 0.6, 1.2):
        _arrow(ax, (x, -1.1), (x, 1.1), lw=1.0, ms=10)
    ax.text(0, 1.25, "magnetic field", ha="center", va="bottom", fontsize=9)
    ax.add_patch(Rectangle((-1.7, -0.12), 3.4, 0.24, fc="#dddddd", ec="black", lw=1.2, zorder=4))
    ax.text(-1.8, 0, "wire", ha="right", va="center", fontsize=9)
    s = 1 if electron_flow == "right" else -1
    _arrow(ax, (1.9 * -s if s < 0 else 1.9, -0.55), (1.9 + 0.9 * s if s > 0 else -1.9 - 0.9, -0.55), lw=1.4, ms=12)
    ax.text(2.35 if s > 0 else -2.35, -0.25, "electron flow", ha="center", va="bottom", fontsize=8.5)
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-1.4, 1.6)
    return _png(fig)


def force_on_wire(field, current):
    """Unit force vector F = I x B. field and current are 3-vectors (x right, y up the page, z out of the page)."""
    return tuple(int(v) for v in np.cross(np.array(current), np.array(field)))


WIRE_DIRS = {"P": (0, 1), "Q": (1, 0), "R": (0, -1), "S": (-1, 0)}


def vertical_wire_top_view(current_down=True, n_left="N"):
    """Vertical wire seen from above between two poles; directions P (up the page), Q (right), R (down the page), S (left). current_down=True: current flows downwards (into the page seen from above)."""
    fig, ax = _fig(5.4, 2.8)
    s_left = n_left
    s_right = "S" if n_left == "N" else "N"
    ax.add_patch(Rectangle((-2.7, -0.6), 0.9, 1.2, fc="#dddddd", ec="black", lw=1.4))
    ax.add_patch(Rectangle((1.8, -0.6), 0.9, 1.2, fc="#dddddd", ec="black", lw=1.4))
    ax.text(-2.25, 0, s_left, ha="center", va="center", fontsize=14, fontweight="bold")
    ax.text(2.25, 0, s_right, ha="center", va="center", fontsize=14, fontweight="bold")
    ax.add_patch(Circle((0, 0), 0.16, fc="white", ec="black", lw=1.3, zorder=5))
    if current_down:
        ax.plot([-0.09, 0.09], [-0.09, 0.09], color="black", lw=1.2, zorder=6)
        ax.plot([-0.09, 0.09], [0.09, -0.09], color="black", lw=1.2, zorder=6)
    else:
        ax.plot([0], [0], "o", color="black", markersize=3, zorder=6)
    for name, (dx, dy) in WIRE_DIRS.items():
        _arrow(ax, (dx * 0.25, dy * 0.25), (dx * 1.05, dy * 1.05), lw=1.3, ms=11)
        ax.text(dx * 1.3, dy * 1.3, name, ha="center", va="center", fontsize=11, fontweight="bold")
    ax.text(0, -1.75, "wire seen from above (" + ("current flows down, into the page" if current_down else "current flows up, out of the page") + ")",
            ha="center", va="top", fontsize=8.5)
    ax.set_xlim(-3.0, 3.0)
    ax.set_ylim(-2.2, 1.7)
    return _png(fig)


def coil_between_poles(p_into=True, n_left=True):
    """Rectangular coil seen from above between two poles; side P (left) and side Q (right) carry opposite currents."""
    fig, ax = _fig(5.0, 3.0)
    ax.add_patch(Rectangle((-3.0, -0.6), 0.8, 1.2, fc="#d9d9d9", ec="black", lw=1.4))
    ax.add_patch(Rectangle((2.2, -0.6), 0.8, 1.2, fc="#d9d9d9", ec="black", lw=1.4))
    ax.text(-2.6, 0, "N" if n_left else "S", ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(2.6, 0, "S" if n_left else "N", ha="center", va="center", fontsize=12, fontweight="bold")
    for x, into in ((-1.0, p_into), (1.0, not p_into)):
        ax.add_patch(Circle((x, 0), 0.28, fc="white", ec="black", lw=1.5))
        if into:
            ax.plot([x - 0.15, x + 0.15], [-0.15, 0.15], color="black", lw=1.4)
            ax.plot([x - 0.15, x + 0.15], [0.15, -0.15], color="black", lw=1.4)
        else:
            ax.plot([x], [0], "o", color="black", markersize=4)
    ax.text(-1.0, -0.55, "side P", ha="center", va="top", fontsize=9)
    ax.text(1.0, -0.55, "side Q", ha="center", va="top", fontsize=9)
    ax.plot([-1.0, -1.0, 1.0, 1.0], [0.28, 1.0, 1.0, 0.28], color="black", lw=1.0, ls=":")
    ax.text(0, 1.05, "coil (seen from above)", ha="center", va="bottom", fontsize=8.5)
    ax.set_xlim(-3.3, 3.3)
    ax.set_ylim(-1.2, 1.6)
    return _png(fig)


def coil_rotation(p_into=True, n_left=True):
    """'clockwise' or 'anticlockwise' as seen from above, from F = I x B on the two sides."""
    field = (1, 0, 0) if n_left else (-1, 0, 0)
    torque = 0
    for x, into in ((-1, p_into), (1, not p_into)):
        current = (0, 0, -1) if into else (0, 0, 1)
        fx, fy, _ = force_on_wire(field, current)
        torque += x * fy - 0 * fx
    return "anticlockwise" if torque > 0 else "clockwise"


# ------------------------------------------------------------------ graphs and lenses
def two_runner_graph(x_pts, y_pts, xmax, ymax, xstep, ystep):
    """Speed-time graph of two runners: X dashed, Y solid, each labelled at its right-hand end."""
    import matplotlib.pyplot as plt
    from .figs import DPI
    fig, ax = plt.subplots(figsize=(4.8, 3.0), dpi=DPI)
    for pts, ls, name in ((x_pts, "--", "runner X"), (y_pts, "-", "runner Y")):
        xs, ys = zip(*pts)
        ax.plot(xs, ys, color="black", lw=2.0, ls=ls)
        ax.text(xs[-1] + 0.15, ys[-1], name, ha="left", va="center", fontsize=9.5)
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax)
    ax.set_xticks(np.arange(0, xmax + 1e-9, xstep))
    ax.set_yticks(np.arange(0, ymax + 1e-9, ystep))
    ax.grid(color="#999999", lw=0.6)
    ax.set_xlabel("time / s", fontsize=10)
    ax.set_ylabel("speed / m/s", fontsize=10)
    ax.tick_params(labelsize=9)
    fig.tight_layout()
    fig.subplots_adjust(right=0.8)
    return _png(fig)


def rays_after_lens(u_label):
    """Object on the axis-left of a lens; two rays from its top leave the lens still diverging. F is not marked."""
    fig, ax = _fig(5.6, 2.8)
    ax.plot([-3.4, 3.4], [0, 0], color="black", lw=0.9, ls="--")
    ax.plot([0, 0], [-1.3, 1.5], color="black", lw=1.6)
    ax.text(0, 1.6, "lens", ha="center", va="bottom", fontsize=9)
    _arrow(ax, (-1.6, 0), (-1.6, 0.6), lw=1.8, ms=12)
    ax.text(-1.6, -0.15, "object", ha="center", va="top", fontsize=9)
    top = (-1.6, 0.6)
    # ray 1 parallel to the axis, bends towards the axis but less than it would for a short focal length
    ax.plot([top[0], 0], [0.6, 0.6], color="black", lw=1.4)
    _arrow(ax, (-0.9, 0.6), (-0.8, 0.6), lw=1.4, ms=10)
    ax.plot([0, 3.2], [0.6, 0.6 - 3.2 * 0.6 / 2.6], color="black", lw=1.4)
    _arrow(ax, (1.6, 0.6 - 1.6 * 0.6 / 2.6), (1.7, 0.6 - 1.7 * 0.6 / 2.6), lw=1.4, ms=10)
    # ray 2 through the optical centre, straight on
    ax.plot([top[0], 3.2], [0.6, 0.6 - 4.8 * 0.6 / 1.6], color="black", lw=1.4)
    _arrow(ax, (1.6, 0.6 - 3.2 * 0.6 / 1.6), (1.7, 0.6 - 3.3 * 0.6 / 1.6), lw=1.4, ms=10)
    _dim(ax, (-1.6, -0.75), (0, -0.75), u_label, off=(0, -0.28))
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1.6, 1.9)
    return _png(fig)
