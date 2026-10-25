"""Schematic diagrams for questions that would otherwise be text only, plus Ch 5-10 diagrams
(beams, slopes, lifts, waves, echo, wavefronts, EM spectrum, particles, heating curves, convection)."""
import io

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

from .figs import DPI, _fig, _png, graph


def _boxlabel(ax, x, y, text, size=10, ha="center", va="center"):
    ax.text(x, y, text, ha=ha, va=va, fontsize=size, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))


def _car(ax, x, y, w=1.4, h=0.55, label=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12", fc="white", ec="black", lw=1.6))
    ax.add_patch(Polygon([(x + 0.3, y + h), (x + 0.5, y + h + 0.35), (x + w - 0.35, y + h + 0.35), (x + w - 0.15, y + h)], fc="white", ec="black", lw=1.4))
    for cx in (x + 0.33, x + w - 0.33):
        ax.add_patch(Circle((cx, y), 0.16, fc="white", ec="black", lw=1.4))
    if label:
        ax.text(x + w / 2, y + h / 2 + 0.02, label, ha="center", va="center", fontsize=9)


# ------------------------------------------------------------------ motion
def motion_sketch(start_label, end_label, mid_label, body_label=None, body="car"):
    """Object at two positions with an arrow between: labels above each position and along the arrow."""
    fig, ax = _fig(6.0, 2.3)
    ax.plot([-0.3, 7.3], [0, 0], color="black", lw=1.4)
    if body == "car":
        _car(ax, 0.0, 0.16, label=body_label)
        _car(ax, 5.4, 0.16, label=body_label)
    else:
        for x in (0.0, 5.4):
            ax.add_patch(Rectangle((x, 0.02), 1.4, 0.9, fc="white", ec="black", lw=1.6))
            if body_label:
                ax.text(x + 0.7, 0.47, body_label, ha="center", va="center", fontsize=9)
    ax.add_patch(FancyArrowPatch((1.7, 1.55), (5.2, 1.55), arrowstyle="-|>", mutation_scale=16, lw=1.8, color="black"))
    ax.text(3.45, 1.78, mid_label, ha="center", va="bottom", fontsize=10)
    ax.text(0.7, 1.45, start_label, ha="center", va="bottom", fontsize=10)
    ax.text(6.1, 1.45, end_label, ha="center", va="bottom", fontsize=10)
    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(-0.4, 2.4)
    return _png(fig)


def journey_sketch(segments):
    """segments: list of (distance_label, speed_label) drawn as consecutive sections."""
    fig, ax = _fig(6.4, 1.9)
    x = 0.0
    seg_w = 6.0 / len(segments)
    for dist, speed in segments:
        ax.plot([x, x + seg_w], [0, 0], color="black", lw=2.0)
        ax.plot([x], [0], "o", color="black", markersize=6)
        ax.text(x + seg_w / 2, 0.22, dist, ha="center", va="bottom", fontsize=10)
        ax.text(x + seg_w / 2, -0.25, speed, ha="center", va="top", fontsize=10)
        x += seg_w
    ax.plot([x], [0], "o", color="black", markersize=6)
    ax.text(0, -0.75, "start", ha="center", va="top", fontsize=9)
    ax.text(x, -0.75, "end", ha="center", va="top", fontsize=9)
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-1.2, 0.9)
    return _png(fig)


def pendulum_sketch(note=None):
    fig, ax = _fig(3.0, 3.2)
    ax.plot([-1.2, 1.2], [3.0, 3.0], color="black", lw=2.0)
    for xh in np.arange(-1.2, 1.2, 0.2):
        ax.plot([xh, xh + 0.15], [3.0, 3.2], color="black", lw=0.8)
    for ang, ls in ((0.0, "-"), (0.45, "--"), (-0.45, "--")):
        x, y = 2.6 * np.sin(ang), 3.0 - 2.6 * np.cos(ang)
        ax.plot([0, x], [3.0, y], color="black", lw=1.4, ls=ls)
        ax.add_patch(Circle((x, y), 0.22, fc="white" if ls == "--" else "#999999", ec="black", lw=1.4))
    ax.add_patch(FancyArrowPatch((-0.9, 0.05), (0.9, 0.05), arrowstyle="<|-|>", mutation_scale=12, lw=1.2, color="black", connectionstyle="arc3,rad=-0.3"))
    if note:
        ax.text(0, -0.55, note, ha="center", va="top", fontsize=10)
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.0, 3.4)
    return _png(fig)


# ------------------------------------------------------------------ matter / forces
def lump_sketch(lines):
    """An irregular solid with text lines beside it (e.g. mass and volume)."""
    fig, ax = _fig(4.2, 2.4)
    pts = [(0.0, 0.3), (0.6, -0.2), (1.6, -0.35), (2.4, 0.1), (2.6, 0.9), (2.0, 1.5), (1.0, 1.6), (0.2, 1.1)]
    ax.add_patch(Polygon(pts, fc="#bbbbbb", ec="black", lw=1.6))
    for i, t in enumerate(lines):
        ax.text(3.1, 1.2 - 0.55 * i, t, ha="left", va="center", fontsize=11)
    ax.set_xlim(-0.3, 6.5)
    ax.set_ylim(-0.7, 2.0)
    return _png(fig)


def pressure_block(force_label, area_label, face_label=None):
    """Block on the ground with a downward force arrow and the contact-area label."""
    fig, ax = _fig(4.2, 3.2)
    ax.plot([-2.6, 2.6], [0, 0], color="black", lw=1.6)
    for x in np.arange(-2.6, 2.6, 0.25):
        ax.plot([x, x - 0.18], [0, -0.2], color="black", lw=0.8)
    ax.add_patch(Rectangle((-1.0, 0), 2.0, 1.2, fc="white", ec="black", lw=1.8))
    ax.add_patch(FancyArrowPatch((0, 2.9), (0, 1.3), arrowstyle="-|>", mutation_scale=16, lw=2.0, color="black"))
    _boxlabel(ax, 0.3, 2.3, force_label, size=11, ha="left")
    if face_label:
        ax.text(0, 0.6, face_label, ha="center", va="center", fontsize=10)
    ax.text(0, -0.5, area_label, ha="center", va="top", fontsize=10)
    ax.set_xlim(-2.8, 3.6)
    ax.set_ylim(-1.1, 3.2)
    return _png(fig)


def spring_balance(reading_label, body_label=None):
    """Object hanging from a spring balance whose scale shows reading_label."""
    fig, ax = _fig(2.6, 4.2)
    ax.plot([-0.8, 0.8], [5.0, 5.0], color="black", lw=2.0)
    ax.plot([0, 0], [5.0, 4.4], color="black", lw=1.4)
    ax.add_patch(FancyBboxPatch((-0.45, 2.3), 0.9, 2.1, boxstyle="round,pad=0.02", fc="white", ec="black", lw=1.6))
    for i in range(6):
        y = 2.6 + i * 0.3
        ax.plot([0.2, 0.45], [y, y], color="black", lw=0.9)
    ax.add_patch(Rectangle((-0.42, 3.05), 0.6, 0.35, fc="#eeeeee", ec="black", lw=0.8))
    ax.text(-0.12, 3.22, reading_label, ha="center", va="center", fontsize=8)
    ax.plot([0, 0], [2.3, 1.6], color="black", lw=1.4)
    ax.add_patch(Rectangle((-0.6, 0.5), 1.2, 1.1, fc="white", ec="black", lw=1.6))
    if body_label:
        ax.text(0, 1.05, body_label, ha="center", va="center", fontsize=10)
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(0.2, 5.3)
    return _png(fig)


def beakers_sketch(items):
    """items: list of (name, line1, line2): beakers side by side with the text under each."""
    fig, ax = _fig(5.4, 3.0)
    for i, (name, l1, l2) in enumerate(items):
        x = i * 2.8
        ax.add_patch(Rectangle((x, 0), 1.8, 2.0, fc="white", ec="black", lw=1.6))
        ax.add_patch(Rectangle((x + 0.03, 0.03), 1.74, 1.1 + 0.3 * i, fc="#d9d9d9", ec="none"))
        ax.plot([x + 0.03, x + 1.77], [1.13 + 0.3 * i] * 2, color="black", lw=1.2)
        ax.text(x + 0.9, 2.15, name, ha="center", va="bottom", fontsize=11)
        ax.text(x + 0.9, -0.3, l1, ha="center", va="top", fontsize=9.5)
        ax.text(x + 0.9, -0.7, l2, ha="center", va="top", fontsize=9.5)
    ax.set_xlim(-0.4, 2.8 * len(items) - 0.6)
    ax.set_ylim(-1.3, 2.7)
    return _png(fig)


def two_bodies_sketch(left_lines, right_lines, left_name="Earth", right_name="Moon"):
    fig, ax = _fig(5.6, 2.6)
    ax.add_patch(Circle((1.0, 1.0), 1.0, fc="#dddddd", ec="black", lw=1.6))
    ax.add_patch(Circle((5.2, 1.0), 0.55, fc="#f2f2f2", ec="black", lw=1.6))
    ax.text(1.0, 2.2, left_name, ha="center", va="bottom", fontsize=11)
    ax.text(5.2, 2.2, right_name, ha="center", va="bottom", fontsize=11)
    for i, t in enumerate(left_lines):
        ax.text(1.0, -0.3 - 0.4 * i, t, ha="center", va="top", fontsize=9.5)
    for i, t in enumerate(right_lines):
        ax.text(5.2, -0.3 - 0.4 * i, t, ha="center", va="top", fontsize=9.5)
    ax.set_xlim(-0.3, 6.5)
    ax.set_ylim(-1.3, 2.7)
    return _png(fig)


# ------------------------------------------------------------------ Ch 5 moments
def beam(length, pivot, forces, dist_labels=None, uniform=False, weight_label=None):
    """Beam of `length` on a pivot at x = pivot. forces: list of (label, x, 'up'|'down').
    dist_labels: list of (x0, x1, text) dimension lines under the beam. uniform=True draws the weight at the centre."""
    fig, ax = _fig(6.6, 3.4)
    k = 6.0 / length

    def X(x):
        return x * k

    ax.add_patch(Rectangle((0, 0), 6.0, 0.28, fc="#eeeeee", ec="black", lw=1.8))
    if pivot is not None:
        ax.add_patch(Polygon([(X(pivot), 0), (X(pivot) - 0.35, -0.7), (X(pivot) + 0.35, -0.7)], fc="white", ec="black", lw=1.6))
    ax.plot([-0.3, 6.3], [-0.7, -0.7], color="black", lw=1.2)
    for label, x, d in forces:
        if d == "down":
            ax.add_patch(FancyArrowPatch((X(x), 1.9), (X(x), 0.32), arrowstyle="-|>", mutation_scale=15, lw=1.9, color="black"))
            ax.text(X(x), 2.05, label, ha="center", va="bottom", fontsize=10.5)
        else:
            ax.add_patch(FancyArrowPatch((X(x), -1.5), (X(x), -0.04), arrowstyle="-|>", mutation_scale=15, lw=1.9, color="black"))
            ax.text(X(x) + 0.2, -1.1, label, ha="left", va="center", fontsize=10.5, bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none"))
    if uniform:
        xc = X(length / 2)
        ax.plot([xc], [0.14], "o", color="black", markersize=5)
        ax.add_patch(FancyArrowPatch((xc, 0.14), (xc, -0.55), arrowstyle="-|>", mutation_scale=15, lw=1.9, color="black"))
        ax.text(xc + 0.18, -0.4, weight_label or "W", ha="left", va="center", fontsize=10.5, bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none"))
    for i, (x0, x1, text) in enumerate(dist_labels or []):
        y = -2.2 - 0.45 * i
        ax.add_patch(FancyArrowPatch((X(x0), y), (X(x1), y), arrowstyle="<|-|>", mutation_scale=11, lw=1.1, color="black"))
        ax.plot([X(x0), X(x0)], [y - 0.12, -0.75], color="#777777", lw=0.6, ls=":")
        ax.plot([X(x1), X(x1)], [y - 0.12, -0.75], color="#777777", lw=0.6, ls=":")
        ax.text((X(x0) + X(x1)) / 2, y + 0.08, text, ha="center", va="bottom", fontsize=9.5, bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none"))
    ax.set_xlim(-0.6, 6.6)
    ax.set_ylim(-3.4, 2.9)
    return _png(fig)


# ------------------------------------------------------------------ Ch 6 energy
def slope_sketch(h_label, top_label=None, bottom_label=None):
    """Block at the top of a smooth slope of height h."""
    fig, ax = _fig(5.4, 3.0)
    ax.add_patch(Polygon([(0, 0), (5.5, 0), (5.5, 2.6)], fc="#f0f0f0", ec="black", lw=1.6))
    ax.plot([-0.4, 5.8], [0, 0], color="black", lw=1.4)
    ang = np.arctan2(2.6, 5.5)
    bx, by = 4.6, 4.6 * 2.6 / 5.5
    tr = matplotlib.transforms.Affine2D().rotate_around(bx, by, ang) + ax.transData
    ax.add_patch(Rectangle((bx - 0.45, by), 0.9, 0.6, fc="white", ec="black", lw=1.6, transform=tr))
    ax.add_patch(FancyArrowPatch((5.9, 0), (5.9, 2.6), arrowstyle="<|-|>", mutation_scale=11, lw=1.1, color="black"))
    ax.text(6.05, 1.3, h_label, ha="left", va="center", fontsize=10.5)
    if top_label:
        ax.text(4.3, 3.1, top_label, ha="center", va="bottom", fontsize=10)
    if bottom_label:
        ax.text(0.3, -0.35, bottom_label, ha="left", va="top", fontsize=10)
    ax.set_xlim(-0.6, 7.8)
    ax.set_ylim(-1.0, 3.7)
    return _png(fig)


def lift_sketch(h_label, body_label=None, extra=None):
    """Motor lifting a box through height h."""
    fig, ax = _fig(4.2, 3.6)
    ax.plot([-1.0, 3.6], [0, 0], color="black", lw=1.4)
    ax.add_patch(Rectangle((2.6, 0), 0.4, 4.2, fc="#dddddd", ec="black", lw=1.4))
    ax.add_patch(Rectangle((0.0, 4.0), 3.0, 0.3, fc="#dddddd", ec="black", lw=1.4))
    ax.add_patch(Rectangle((2.4, 4.3), 0.8, 0.5, fc="white", ec="black", lw=1.4))
    ax.text(2.8, 4.55, "motor", ha="center", va="center", fontsize=8)
    ax.plot([0.8, 0.8], [4.0, 2.6], color="black", lw=1.2)
    ax.add_patch(Rectangle((0.3, 1.8), 1.0, 0.8, fc="white", ec="black", lw=1.6))
    if body_label:
        ax.text(0.8, 2.2, body_label, ha="center", va="center", fontsize=9.5)
    ax.add_patch(Rectangle((0.3, 0), 1.0, 0.8, fc="white", ec="black", lw=1.0, ls="--"))
    ax.add_patch(FancyArrowPatch((-0.4, 0.0), (-0.4, 1.8), arrowstyle="<|-|>", mutation_scale=11, lw=1.1, color="black"))
    ax.text(-0.55, 0.9, h_label, ha="right", va="center", fontsize=10.5)
    if extra:
        ax.text(1.3, -0.5, extra, ha="center", va="top", fontsize=10)
    ax.set_xlim(-2.6, 3.9)
    ax.set_ylim(-1.1, 5.1)
    return _png(fig)


def push_sketch(force_label, dist_label, body_label=None, friction_label=None):
    """Box pushed along the ground through a distance."""
    fig, ax = _fig(6.0, 2.4)
    ax.plot([-0.4, 7.4], [0, 0], color="black", lw=1.4)
    ax.add_patch(Rectangle((0.6, 0), 1.3, 1.0, fc="white", ec="black", lw=1.6, ls="--"))
    ax.add_patch(Rectangle((5.0, 0), 1.3, 1.0, fc="white", ec="black", lw=1.6))
    if body_label:
        ax.text(5.65, 0.5, body_label, ha="center", va="center", fontsize=9.5)
        ax.text(1.25, 0.5, body_label, ha="center", va="center", fontsize=9.5, color="#666666")
    ax.add_patch(FancyArrowPatch((6.35, 0.5), (7.5, 0.5), arrowstyle="-|>", mutation_scale=14, lw=1.8, color="black"))
    ax.text(7.0, 0.8, force_label, ha="center", va="bottom", fontsize=10)
    if friction_label:
        ax.add_patch(FancyArrowPatch((4.95, 0.3), (4.0, 0.3), arrowstyle="-|>", mutation_scale=14, lw=1.8, color="black"))
        ax.text(4.5, -0.3, friction_label, ha="center", va="top", fontsize=10)
    ax.add_patch(FancyArrowPatch((1.25, 1.45), (5.65, 1.45), arrowstyle="<|-|>", mutation_scale=11, lw=1.1, color="black"))
    ax.text(3.45, 1.6, dist_label, ha="center", va="bottom", fontsize=10.5)
    ax.set_xlim(-0.6, 8.4)
    ax.set_ylim(-0.9, 2.3)
    return _png(fig)


# ------------------------------------------------------------------ Ch 9 waves
def wave_graph(amplitude, period_or_lambda, kind="distance", cycles=2.0, mark=None):
    """Displacement against distance (kind='distance': cm; 'distance_m': m) or time (kind='time': s; 'time_ms': ms)."""
    L = period_or_lambda
    xmax = cycles * L
    xx = np.linspace(0, xmax, 400)
    yy = amplitude * np.sin(2 * np.pi * xx / L)
    ymax = amplitude * 1.5
    xlabel = {"distance": "distance / cm", "time": "time / s", "distance_m": "distance / m", "time_ms": "time / ms"}[kind]
    fig, ax = plt.subplots(figsize=(5.0, 2.8), dpi=DPI)
    ax.plot(xx, yy, color="black", lw=2.0)
    ax.axhline(0, color="black", lw=1.0)
    ax.set_xlim(0, xmax)
    ax.set_ylim(-ymax, ymax)
    ax.set_xticks(np.arange(0, xmax + 1e-9, L / 2))
    ax.set_yticks(np.arange(-ymax, ymax + 1e-9, amplitude / 2))
    ax.set_xticks(np.arange(0, xmax + 1e-9, L / 10), minor=True)
    ax.grid(which="major", color="#666666", linewidth=0.7)
    ax.grid(which="minor", color="#BBBBBB", linewidth=0.4)
    ax.tick_params(labelsize=8.5)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel("displacement / cm", fontsize=10)
    for (x, y, text, dx, dy) in (mark or []):
        ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points", fontsize=10, fontweight="bold", ha="center",
                    bbox=dict(boxstyle="circle,pad=0.12", fc="white", ec="none"))
        ax.plot([x], [y], "o", color="black", markersize=4)
    for s in ax.spines.values():
        s.set_linewidth(1.3)
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    return buf.getvalue()


def echo_sketch(d_label, t_label, left="student", right="wall", wave="sound", back="echo", person=True):
    """Source on the left, reflector/target on the right. person=False draws a transmitter box; back=None: one-way signal."""
    fig, ax = _fig(6.0, 2.6)
    ax.plot([-0.3, 6.6], [0, 0], color="black", lw=1.4)
    if person:
        ax.add_patch(Circle((0.3, 1.55), 0.22, fc="white", ec="black", lw=1.4))
        ax.plot([0.3, 0.3], [1.33, 0.6], color="black", lw=1.4)
        ax.plot([0.3, 0.0], [0.6, 0.0], color="black", lw=1.4)
        ax.plot([0.3, 0.6], [0.6, 0.0], color="black", lw=1.4)
        ax.plot([0.3, 0.65], [1.15, 0.85], color="black", lw=1.4)
    else:
        ax.add_patch(Rectangle((0.0, 0.0), 0.7, 1.1, fc="white", ec="black", lw=1.6))
        ax.add_patch(Polygon([(0.7, 0.75), (1.0, 1.05), (1.0, 0.45)], fc="#cccccc", ec="black", lw=1.2))
    ax.text(0.3, -0.25, left, ha="center", va="top", fontsize=9.5)
    ax.add_patch(Rectangle((6.0, 0), 0.5, 2.2, fc="#cccccc", ec="black", lw=1.6))
    ax.text(6.25, 2.3, right, ha="center", va="bottom", fontsize=9.5)
    ax.add_patch(FancyArrowPatch((1.1, 1.5), (5.8, 1.5), arrowstyle="-|>", mutation_scale=13, lw=1.4, color="black", connectionstyle="arc3,rad=-0.15"))
    if back:
        ax.add_patch(FancyArrowPatch((5.8, 1.0), (1.1, 1.0), arrowstyle="-|>", mutation_scale=13, lw=1.4, color="black", connectionstyle="arc3,rad=-0.15"))
        ax.text(3.45, 0.55, back, ha="center", va="top", fontsize=9.5)
    ax.text(3.45, 2.05, wave, ha="center", va="bottom", fontsize=9.5)
    ax.add_patch(FancyArrowPatch((0.3, -0.8), (6.0, -0.8), arrowstyle="<|-|>", mutation_scale=11, lw=1.1, color="black"))
    ax.text(3.15, -0.95, d_label, ha="center", va="top", fontsize=10.5)
    ax.text(3.15, 2.95, t_label, ha="center", va="top", fontsize=10.5)
    ax.set_xlim(-0.6, 7.0)
    ax.set_ylim(-1.7, 3.1)
    return _png(fig)


def wavefronts_sketch(n, span_label):
    """n straight wavefronts (ripple tank) with a dimension line across them."""
    fig, ax = _fig(5.6, 2.6)
    ax.add_patch(Rectangle((0, 0), 6.0, 2.4, fc="#f7f7f7", ec="black", lw=1.4))
    xs = np.linspace(0.6, 5.4, n)
    for x in xs:
        ax.plot([x, x], [0.25, 2.15], color="black", lw=1.8)
    ax.add_patch(FancyArrowPatch((xs[0], -0.4), (xs[-1], -0.4), arrowstyle="<|-|>", mutation_scale=11, lw=1.1, color="black"))
    ax.text((xs[0] + xs[-1]) / 2, -0.55, span_label, ha="center", va="top", fontsize=10.5)
    ax.add_patch(FancyArrowPatch((2.6, 2.7), (3.6, 2.7), arrowstyle="-|>", mutation_scale=12, lw=1.3, color="black"))
    ax.text(3.1, 2.8, "direction of travel", ha="center", va="bottom", fontsize=9)
    ax.set_xlim(-0.3, 6.3)
    ax.set_ylim(-1.3, 3.4)
    return _png(fig)


# ------------------------------------------------------------------ Ch 10 EM spectrum
EM_REGIONS = ["radio waves", "microwaves", "infrared", "visible light", "ultraviolet", "X-rays", "gamma rays"]


def em_spectrum(hidden=None, highlight=None):
    """The seven regions in order of decreasing wavelength. hidden: region names replaced by letters P, Q, R, S."""
    fig, ax = _fig(7.2, 2.0)
    hidden = hidden or []
    letters = iter("PQRS")
    for i, name in enumerate(EM_REGIONS):
        fc = "#dddddd" if name == highlight else "white"
        ax.add_patch(Rectangle((i, 0), 1, 0.9, fc=fc, ec="black", lw=1.4))
        if name in hidden:
            ax.text(i + 0.5, 0.45, next(letters), ha="center", va="center", fontsize=12, fontweight="bold")
        else:
            ax.text(i + 0.5, 0.45, name.replace(" ", "\n"), ha="center", va="center", fontsize=8.5)
    ax.add_patch(FancyArrowPatch((0.0, -0.35), (7.0, -0.35), arrowstyle="-|>", mutation_scale=12, lw=1.3, color="black"))
    ax.text(3.5, -0.5, "increasing frequency, decreasing wavelength", ha="center", va="top", fontsize=9)
    ax.set_xlim(-0.2, 7.2)
    ax.set_ylim(-1.1, 1.2)
    return _png(fig)


# ------------------------------------------------------------------ Ch 7-8 particles and thermal
def _draw_particles(ax, state, rng):
    ax.add_patch(Rectangle((0, 0), 3, 3, fc="white", ec="black", lw=1.6))
    if state == "solid":
        for i in range(5):
            for j in range(5):
                ax.add_patch(Circle((0.4 + i * 0.55, 0.4 + j * 0.55), 0.22, fc="#999999", ec="black", lw=0.9))
        return
    n, gap = (20, 0.5) if state == "liquid" else (7, 0.8)
    pts = []
    tries = 0
    while len(pts) < n and tries < 5000:
        tries += 1
        p = rng.uniform(0.3, 2.7, 2)
        if all(np.hypot(*(p - q)) > gap for q in pts):
            pts.append(p)
    for p in pts:
        ax.add_patch(Circle(p, 0.22, fc="#999999", ec="black", lw=0.9))
        if state == "gas":
            d = rng.uniform(-1, 1, 2)
            d = d / np.hypot(*d) * 0.5
            ax.add_patch(FancyArrowPatch(p, p + d, arrowstyle="-|>", mutation_scale=9, lw=1.0, color="black"))


def particles(state, label=None):
    fig, ax = _fig(2.6, 2.6)
    _draw_particles(ax, state, np.random.default_rng(3))
    if label:
        ax.text(1.5, -0.25, label, ha="center", va="top", fontsize=10)
    ax.set_xlim(-0.2, 3.2)
    ax.set_ylim(-0.7, 3.2)
    return _png(fig)


def three_states(order=("solid", "liquid", "gas"), names=("X", "Y", "Z")):
    """Three particle boxes side by side, labelled with letters."""
    fig, axs = plt.subplots(1, 3, figsize=(7.0, 2.6), dpi=DPI)
    rng = np.random.default_rng(5)
    for ax, state, name in zip(axs, order, names):
        ax.set_aspect("equal")
        ax.axis("off")
        _draw_particles(ax, state, rng)
        ax.text(1.5, -0.3, name, ha="center", va="top", fontsize=13, fontweight="bold")
        ax.set_xlim(-0.2, 3.2)
        ax.set_ylim(-0.9, 3.2)
    fig.tight_layout()
    return _png(fig, pad=0.08)


def heating_curve(pts, labels=None):
    """Temperature-time graph; pts are (time / min, temperature / °C) corners."""
    xs, ys = zip(*pts)
    xstep = next(s for s in (1, 2, 5, 10, 20, 50) if max(xs) / s <= 8)
    xmax = (int(max(xs) / xstep) + (1 if max(xs) % xstep else 0)) * xstep
    ymax = (int(max(ys) / 20) + 1) * 20
    return graph(pts, xmax, ymax, xstep, 20, xlabel="time / min", ylabel="temperature / °C", labels=labels)


def convection_sketch():
    """Beaker of water heated at one side with the circulation marked A (rising) and B (sinking)."""
    fig, ax = _fig(3.6, 3.2)
    ax.add_patch(Rectangle((0, 0), 3.0, 3.0, fc="#eef3f8", ec="black", lw=1.6))
    ax.plot([0, 3.0], [3.0, 3.0], color="white", lw=2.5)
    ax.add_patch(Polygon([(0.45, -0.1), (0.65, -0.7), (0.85, -0.1)], fc="#999999", ec="black", lw=1.0))
    ax.text(0.65, -0.85, "heat", ha="center", va="top", fontsize=9.5)
    ax.add_patch(FancyArrowPatch((0.6, 0.4), (0.6, 2.5), arrowstyle="-|>", mutation_scale=13, lw=1.6, color="black"))
    ax.add_patch(FancyArrowPatch((0.8, 2.6), (2.3, 2.6), arrowstyle="-|>", mutation_scale=13, lw=1.6, color="black"))
    ax.add_patch(FancyArrowPatch((2.4, 2.5), (2.4, 0.4), arrowstyle="-|>", mutation_scale=13, lw=1.6, color="black"))
    ax.add_patch(FancyArrowPatch((2.2, 0.3), (0.8, 0.3), arrowstyle="-|>", mutation_scale=13, lw=1.6, color="black"))
    ax.text(0.6, 1.45, "A", ha="center", va="center", fontsize=12, fontweight="bold", bbox=dict(boxstyle="circle,pad=0.15", fc="white", ec="none"))
    ax.text(2.4, 1.45, "B", ha="center", va="center", fontsize=12, fontweight="bold", bbox=dict(boxstyle="circle,pad=0.15", fc="white", ec="none"))
    ax.set_xlim(-0.3, 3.3)
    ax.set_ylim(-1.2, 3.3)
    return _png(fig)


def rod_sketch(materials):
    """Rods of different materials heated at one end, with wax-held pins (conduction comparison)."""
    fig, ax = _fig(5.6, 2.6)
    for i, m in enumerate(materials):
        y = 2.2 - i * 0.8
        ax.add_patch(Rectangle((0.8, y - 0.12), 4.4, 0.24, fc="#dddddd", ec="black", lw=1.3))
        ax.text(5.35, y, m, ha="left", va="center", fontsize=9.5)
        for x in (2.0, 3.2, 4.4):
            ax.plot([x, x], [y - 0.12, y - 0.5], color="black", lw=1.0)
            ax.add_patch(Circle((x, y - 0.12), 0.07, fc="#666666", ec="none"))
    ax.add_patch(Polygon([(0.2, 0.0), (0.45, -0.6), (0.7, 0.0)], fc="#999999", ec="black", lw=1.0))
    ax.add_patch(Rectangle((0.2, 0.0), 0.5, 2.5, fc="#f2f2f2", ec="black", lw=1.2))
    ax.text(0.45, 2.65, "heat", ha="center", va="bottom", fontsize=9)
    ax.set_xlim(-0.2, 7.2)
    ax.set_ylim(-0.9, 3.0)
    return _png(fig)


def flask_sketch():
    """Cross-section of a vacuum flask: double glass wall, vacuum gap, silvered surfaces, stopper."""
    fig, ax = _fig(3.4, 4.0)
    ax.add_patch(Rectangle((0, 0), 3.0, 4.0, fc="#f4f4f4", ec="black", lw=1.6))
    ax.add_patch(Rectangle((0.35, 0.3), 2.3, 3.4, fc="white", ec="black", lw=1.4))
    ax.add_patch(Rectangle((0.65, 0.6), 1.7, 3.1, fc="#dfe8f3", ec="black", lw=1.4))
    ax.add_patch(Rectangle((0.5, 3.7), 2.0, 0.5, fc="#bbbbbb", ec="black", lw=1.4))
    ax.text(1.5, 3.95, "stopper", ha="center", va="center", fontsize=8)
    ax.text(1.5, 2.1, "hot\nliquid", ha="center", va="center", fontsize=9)
    ax.annotate("vacuum", (0.5, 1.6), xytext=(-1.6, 1.6), fontsize=9, ha="center", arrowprops=dict(arrowstyle="-|>", lw=1.0))
    ax.annotate("silvered\nsurfaces", (0.65, 0.9), xytext=(-1.6, 0.6), fontsize=9, ha="center", arrowprops=dict(arrowstyle="-|>", lw=1.0))
    ax.annotate("outer\ncase", (0.1, 3.0), xytext=(-1.6, 3.1), fontsize=9, ha="center", arrowprops=dict(arrowstyle="-|>", lw=1.0))
    ax.set_xlim(-2.6, 3.4)
    ax.set_ylim(-0.3, 4.5)
    return _png(fig)


def two_cups_sketch(left="dull black", right="shiny silver", note=None):
    fig, ax = _fig(5.0, 2.6)
    for x, fc, name in ((0.0, "#333333", left), (3.0, "#e6e6e6", right)):
        ax.add_patch(Polygon([(x, 0), (x + 1.8, 0), (x + 1.6, 2.0), (x + 0.2, 2.0)], fc=fc, ec="black", lw=1.6))
        for dx in (0.6, 0.9, 1.2):
            ax.plot([x + dx, x + dx + 0.15], [2.15, 2.7], color="#777777", lw=1.0, ls="--")
        ax.text(x + 0.9, -0.3, name, ha="center", va="top", fontsize=10)
    if note:
        ax.text(2.4, 3.0, note, ha="center", va="bottom", fontsize=9.5)
    ax.set_xlim(-0.4, 5.2)
    ax.set_ylim(-0.9, 3.5)
    return _png(fig)
