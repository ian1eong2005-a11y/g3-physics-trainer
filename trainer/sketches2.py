"""Diagrams for Chapters 11-16: ray diagrams, lenses, circuits, mains plug, magnetic fields, atoms and decay curves."""
import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Ellipse, FancyArrowPatch, Polygon, Rectangle

from .figs import DPI, _fig, _png, graph


def _arrow(ax, p0, p1, lw=1.8, ms=14, color="black", ls="-"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=ms, lw=lw, color=color, linestyle=ls))


def _mid_arrow(ax, p0, p1, lw=1.8, color="black"):
    """Line from p0 to p1 with an arrowhead at its midpoint (ray convention)."""
    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=color, lw=lw)
    mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    n = math.hypot(dx, dy) or 1
    ax.add_patch(FancyArrowPatch((mx - dx / n * 0.01, my - dy / n * 0.01), (mx + dx / n * 0.02, my + dy / n * 0.02),
                                 arrowstyle="-|>", mutation_scale=14, lw=lw, color=color))


# ================================================================== Ch 11 Light
def reflection_diagram(angle_i, show_r=True, label_i="i", label_r="r"):
    """Plane mirror along the x-axis; incident ray from upper left at angle_i to the normal; reflected ray to upper right."""
    fig, ax = _fig(4.6, 3.2)
    ax.plot([-3, 3], [0, 0], color="black", lw=2.2)
    for x in np.arange(-3, 3, 0.3):
        ax.plot([x, x - 0.2], [0, -0.25], color="black", lw=0.9)
    ax.plot([0, 0], [0, 3.0], color="black", lw=1.0, ls="--")
    ax.text(0.1, 2.85, "normal", fontsize=9, ha="left", va="top")
    a = math.radians(angle_i)
    L = 2.6
    _mid_arrow(ax, (-L * math.sin(a), L * math.cos(a)), (0, 0))
    ax.add_patch(Arc((0, 0), 1.4, 1.4, angle=90, theta1=0, theta2=angle_i, lw=1.0))
    ax.text(-0.95 * math.sin(a / 2) - 0.1, 0.95 * math.cos(a / 2), label_i, fontsize=11, ha="right", va="center")
    if show_r:
        _mid_arrow(ax, (0, 0), (L * math.sin(a), L * math.cos(a)))
        ax.add_patch(Arc((0, 0), 1.4, 1.4, angle=90 - angle_i, theta1=0, theta2=angle_i, lw=1.0))
        ax.text(0.95 * math.sin(a / 2) + 0.1, 0.95 * math.cos(a / 2), label_r, fontsize=11, ha="left", va="center")
    ax.text(2.9, -0.55, "mirror", fontsize=9, ha="right", va="top")
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-0.8, 3.2)
    return _png(fig)


def refraction_diagram(angle_i, angle_r, medium="glass", label_i="i", label_r="r", show_r=True):
    """Air above, medium below the boundary; ray refracts towards the normal."""
    fig, ax = _fig(4.6, 4.0)
    ax.add_patch(Rectangle((-3, -3), 6, 3, fc="#e4edf6", ec="black", lw=1.4))
    ax.plot([-3, 3], [0, 0], color="black", lw=1.6)
    ax.plot([0, 0], [-3, 3], color="black", lw=1.0, ls="--")
    ax.text(0.1, 2.85, "normal", fontsize=9, ha="left", va="top")
    ax.text(-2.9, 2.7, "air", fontsize=10, ha="left", va="top")
    ax.text(-2.9, -2.7, medium, fontsize=10, ha="left", va="bottom")
    a = math.radians(angle_i)
    L = 2.6
    _mid_arrow(ax, (-L * math.sin(a), L * math.cos(a)), (0, 0))
    ax.add_patch(Arc((0, 0), 1.2, 1.2, angle=90, theta1=0, theta2=angle_i, lw=1.0))
    ax.text(-0.5 * math.sin(a / 2) - 0.3, 0.5 * math.cos(a / 2) + 0.35, label_i, fontsize=11, ha="right", va="center",
            bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none"))
    if show_r:
        b = math.radians(angle_r)
        _mid_arrow(ax, (0, 0), (L * math.sin(b), -L * math.cos(b)))
        ax.add_patch(Arc((0, 0), 1.2, 1.2, angle=270, theta1=0, theta2=angle_r, lw=1.0))
        ax.text(0.5 * math.sin(b / 2) + 0.35, -0.5 * math.cos(b / 2) - 0.35, label_r, fontsize=11, ha="left", va="center",
                bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none"))
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.2, 3.2)
    return _png(fig)


def lens_diagram(u, f, h=1.0, show_image=True, labels=True):
    """Converging lens at x = 0, focal length f, object (arrow) of height h at x = -u. Draws the two standard rays.
    Real image if u > f (inverted, at v = uf/(u-f)); virtual, upright image if u < f (drawn with dashed rays)."""
    real = u > f
    v = u * f / (u - f) if real else u * f / (f - u)        # image distance (positive = right of lens for real)
    hi = h * v / u
    xmax = max(u, v if real else v) * 1.15 + 0.5
    fig, ax = plt.subplots(figsize=(6.4, 3.2), dpi=DPI)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.plot([-xmax, xmax], [0, 0], color="black", lw=1.0)
    ax.add_patch(Ellipse((0, 0), 0.5, 2 * max(h, hi, 1.4) * 1.3, fc="#dfe8f3", ec="black", lw=1.4))
    for s in (-1, 1):
        ax.plot([s * f], [0], "|", color="black", markersize=10, mew=1.6)
        ax.plot([2 * s * f], [0], "|", color="black", markersize=8, mew=1.2)
        if labels:
            ax.text(s * f, -0.35, "F", ha="center", va="top", fontsize=10)
            ax.text(2 * s * f, -0.35, "2F", ha="center", va="top", fontsize=9)
    _arrow(ax, (-u, 0), (-u, h), lw=2.0, ms=14)
    if labels:
        ax.text(-u, h + 0.15, "object", ha="center", va="bottom", fontsize=9)
    # ray 1: parallel to axis, then through F on the far side
    _mid_arrow(ax, (-u, h), (0, h))
    if real:
        _mid_arrow(ax, (0, h), (v, -hi))
        # ray 2: through the optical centre, straight on
        _mid_arrow(ax, (-u, h), (v, -hi))
        if show_image:
            _arrow(ax, (v, 0), (v, -hi), lw=2.0, ms=14)
            if labels:
                ax.text(v, -hi - 0.15, "image", ha="center", va="top", fontsize=9)
    else:
        # refracted ray through far F, extended backwards (dashed) to the virtual image
        end = (f * 2.2, h - (h / f) * f * 2.2)
        _mid_arrow(ax, (0, h), end)
        ax.plot([0, -v], [h, hi], color="black", lw=1.0, ls="--")
        # ray 2 through centre, extended backwards
        k = (xmax) / u
        _mid_arrow(ax, (-u, h), (xmax * 0.9, -h * (xmax * 0.9) / u))
        ax.plot([-u, -v], [h, hi], color="black", lw=1.0, ls="--")
        if show_image:
            ax.add_patch(FancyArrowPatch((-v, 0), (-v, hi), arrowstyle="-|>", mutation_scale=14, lw=2.0, color="black", linestyle="--"))
            if labels:
                ax.text(-v, hi + 0.15, "image", ha="center", va="bottom", fontsize=9)
    ax.set_xlim(-xmax, xmax)
    ax.set_ylim(-max(h, hi, 1.4) * 1.6, max(h, hi, 1.4) * 1.6)
    fig.tight_layout()
    return _png(fig, pad=0.05)


def lens_parallel_beam(f=2.0):
    fig, ax = plt.subplots(figsize=(5.2, 2.6), dpi=DPI)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.plot([-4, 4], [0, 0], color="black", lw=1.0)
    ax.add_patch(Ellipse((0, 0), 0.5, 3.2, fc="#dfe8f3", ec="black", lw=1.4))
    for y in (-1.2, -0.6, 0.6, 1.2):
        _mid_arrow(ax, (-3.8, y), (0, y))
        _mid_arrow(ax, (0, y), (f, 0))
        ax.plot([f, f + 1.6], [0, -y * 0.8], color="black", lw=1.4)
    ax.plot([f], [0], "o", color="black", markersize=5)
    ax.text(f, -0.4, "F", ha="center", va="top", fontsize=11)
    ax.add_patch(FancyArrowPatch((0, -1.75), (f, -1.75), arrowstyle="<|-|>", mutation_scale=10, lw=1.0, color="black"))
    ax.text(f / 2, -1.9, "focal length f", ha="center", va="top", fontsize=9)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-2.4, 1.9)
    fig.tight_layout()
    return _png(fig, pad=0.05)


# ================================================================== Ch 12-14 Circuits
def _resistor(ax, x, y, label, w=1.0, h=0.36):
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, fc="white", ec="black", lw=1.5))
    if label:
        ax.text(x, y + h / 2 + 0.12, label, ha="center", va="bottom", fontsize=9.5)


def _lamp(ax, x, y, label=None):
    ax.add_patch(Circle((x, y), 0.26, fc="white", ec="black", lw=1.5))
    d = 0.26 * 0.707
    ax.plot([x - d, x + d], [y - d, y + d], color="black", lw=1.2)
    ax.plot([x - d, x + d], [y + d, y - d], color="black", lw=1.2)
    if label:
        ax.text(x, y + 0.4, label, ha="center", va="bottom", fontsize=9.5)


def _meter(ax, x, y, letter, label=None):
    ax.add_patch(Circle((x, y), 0.28, fc="white", ec="black", lw=1.5))
    ax.text(x, y, letter, ha="center", va="center", fontsize=10, fontweight="bold")
    if label:
        ax.text(x, y + 0.42, label, ha="center", va="bottom", fontsize=9)


def _cell(ax, x, y, label=None, vertical=True):
    """Battery symbol centred at (x, y) on a vertical wire."""
    ax.plot([x - 0.35, x + 0.35], [y + 0.12, y + 0.12], color="black", lw=2.2)
    ax.plot([x - 0.18, x + 0.18], [y - 0.12, y - 0.12], color="black", lw=1.2)
    if label:
        ax.text(x - 0.5, y, label, ha="right", va="center", fontsize=9.5)


def _switch(ax, x, y, closed=True):
    ax.plot([x - 0.4], [y], "o", color="black", markersize=4)
    ax.plot([x + 0.4], [y], "o", color="black", markersize=4)
    if closed:
        ax.plot([x - 0.4, x + 0.4], [y, y], color="black", lw=1.5)
    else:
        ax.plot([x - 0.4, x + 0.25], [y, y + 0.35], color="black", lw=1.5)


def circuit(series=(), parallel=(), emf="", ammeter=None, voltmeter=None, switch=None, title=None):
    """Battery on the left; `series` components along the top wire; `parallel` = list of branches (each a list of components)
    placed on the right between two nodes. A component is (kind, label) with kind in 'R', 'lamp', 'A', 'V', 'wire'.
    ammeter='main' puts an ammeter in the bottom wire. voltmeter=('series', i) or ('parallel', j) draws a voltmeter across it."""
    series, parallel = list(series), [list(b) for b in parallel]
    n_s = len(series)
    n_b = len(parallel)
    top_len = 1.8 + 1.6 * n_s
    px = top_len + (1.6 if n_b else 0.2)          # x of the parallel block start
    width = px + (2.6 if n_b else 0.0)
    H = 2.4
    branch_gap = 1.1
    fig, ax = _fig(max(4.8, width * 0.95), max(3.0, (H + (n_b - 1) * branch_gap) * 0.9 + 1.2))
    # outer loop
    ax.plot([0, 0], [0, H], color="black", lw=1.5)
    ax.plot([0, width], [H, H], color="black", lw=1.5)
    ax.plot([width, width], [0, H], color="black", lw=1.5)
    ax.plot([0, width], [0, 0], color="black", lw=1.5)
    _cell(ax, 0, H / 2, label=emf)
    # series components on the top wire
    xs = []
    for i, (kind, label) in enumerate(series):
        x = 1.6 + 1.6 * i
        xs.append(x)
        if kind == "R":
            _resistor(ax, x, H, label)
        elif kind == "lamp":
            _lamp(ax, x, H, label)
        elif kind == "A":
            _meter(ax, x, H, "A", label)
        elif kind == "V":
            _meter(ax, x, H, "V", label)
    # parallel block
    if n_b:
        x0, x1 = px, px + 2.0
        ys = [H - 0.0 - k * branch_gap for k in range(n_b)]
        yc = (ys[0] + ys[-1]) / 2
        ax.plot([x0, x0], [ys[-1], H], color="black", lw=1.5)
        ax.plot([x1, x1], [ys[-1], H], color="black", lw=1.5)
        ax.plot([x1, width], [H, H], color="black", lw=1.5)
        for k, (y, branch) in enumerate(zip(ys, parallel)):
            ax.plot([x0, x1], [y, y], color="black", lw=1.5)
            m = len(branch)
            for j, (kind, label) in enumerate(branch):
                x = x0 + (x1 - x0) * (j + 1) / (m + 1)
                if kind == "R":
                    _resistor(ax, x, y, label, w=0.8)
                elif kind == "lamp":
                    _lamp(ax, x, y, label)
                elif kind == "A":
                    _meter(ax, x, y, "A", label)
            if k > 0:
                ax.plot([x0], [y], "o", color="black", markersize=4)
                ax.plot([x1], [y], "o", color="black", markersize=4)
    if ammeter == "main":
        _meter(ax, width / 2, 0, "A")
    if switch is not None:
        _switch(ax, width * 0.75 if ammeter != "main" else width * 0.25, 0, closed=switch)
    if voltmeter is not None:
        where, idx = voltmeter
        if where == "series":
            x = xs[idx]
            ax.plot([x - 0.6, x - 0.6, x + 0.6, x + 0.6], [H, H + 1.0, H + 1.0, H], color="black", lw=1.3)
            _meter(ax, x, H + 1.0, "V")
        else:
            y = H - idx * branch_gap
            ax.plot([px - 0.3, px - 0.3, px + 2.3, px + 2.3], [y, y - 0.9 * (n_b) - 0.3, y - 0.9 * (n_b) - 0.3, y], color="black", lw=1.3)
            _meter(ax, px + 1.0, y - 0.9 * n_b - 0.3, "V")
    if title:
        ax.text(width / 2, -0.75, title, ha="center", va="top", fontsize=9.5)
    ax.set_xlim(-1.4, width + 0.6)
    ax.set_ylim(-1.3 - (branch_gap * max(n_b - 1, 0)), H + 1.6)
    return _png(fig)


def vi_graph(resistance, vmax=12, label=None):
    pts = [(0, 0), (vmax, vmax / resistance)]
    imax = vmax / resistance
    istep = next(s for s in (0.1, 0.2, 0.5, 1, 2, 5, 10) if imax / s <= 6)
    vstep = next(s for s in (1, 2, 5, 10) if vmax / s <= 6)
    return graph(pts, vmax, (int(imax / istep) + 1) * istep, vstep, istep, xlabel="p.d. / V", ylabel="current / A")


def wire_pair(len1, area1, len2, area2):
    """Two wires of the same material drawn to compare length and thickness."""
    fig, ax = _fig(5.4, 2.4)
    k = 4.0 / max(len1, len2)
    for i, (L, A, name) in enumerate(((len1, area1, "wire X"), (len2, area2, "wire Y"))):
        y = 1.6 - i * 1.3
        h = 0.18 + 0.22 * (A / max(area1, area2))
        ax.add_patch(Rectangle((0, y - h / 2), L * k, h, fc="#cccccc", ec="black", lw=1.3))
        ax.text(L * k + 0.2, y, f"{name}: length {L}, area {A}", ha="left", va="center", fontsize=9.5)
    ax.set_xlim(-0.2, 8.2)
    ax.set_ylim(-0.4, 2.3)
    return _png(fig)


def plug_sketch(labels=True):
    """UK-style three-pin plug viewed from inside, with earth (top), live (right, fused) and neutral (left)."""
    fig, ax = _fig(4.4, 4.0)
    ax.add_patch(Polygon([(-1.8, -1.6), (1.8, -1.6), (2.0, 0.8), (0, 2.0), (-2.0, 0.8)], fc="#f4f4f4", ec="black", lw=1.6))
    ax.add_patch(Rectangle((-0.18, 1.0), 0.36, 0.7, fc="#888888", ec="black", lw=1.2))      # earth pin
    ax.add_patch(Rectangle((-1.5, -0.6), 0.36, 0.55, fc="#888888", ec="black", lw=1.2))     # neutral pin
    ax.add_patch(Rectangle((1.14, -0.6), 0.36, 0.55, fc="#888888", ec="black", lw=1.2))     # live pin
    ax.add_patch(Rectangle((0.75, -0.2), 0.9, 0.3, fc="white", ec="black", lw=1.2))         # fuse
    ax.text(1.2, -0.05, "fuse", ha="center", va="center", fontsize=7.5)
    # wires from cable at the bottom
    ax.add_patch(Rectangle((-0.35, -2.2), 0.7, 0.6, fc="#dddddd", ec="black", lw=1.2))
    ax.plot([0, 0, 0], [-1.6, -0.9, 1.0], color="#3a7d44", lw=2.2)           # earth: green/yellow
    ax.plot([0, 0], [-1.6, 1.0], color="#e3c531", lw=1.0, ls=(0, (3, 3)))
    ax.plot([-0.1, -1.32, -1.32], [-1.6, -0.9, -0.6], color="#2c5fb3", lw=2.2)   # neutral: blue
    ax.plot([0.1, 1.2, 1.2], [-1.6, -0.9, -0.2], color="#8b5a2b", lw=2.2)        # live: brown, to fuse
    if labels:
        ax.text(0.3, 1.55, "E (green/yellow)", ha="left", va="center", fontsize=8.5)
        ax.text(-1.32, -0.95, "N (blue)", ha="center", va="top", fontsize=8.5)
        ax.text(1.55, -0.95, "L (brown)", ha="center", va="top", fontsize=8.5)
        ax.text(0, -2.35, "cable", ha="center", va="top", fontsize=8.5)
    ax.set_xlim(-2.4, 2.6)
    ax.set_ylim(-2.7, 2.3)
    return _png(fig)


# ================================================================== Ch 15 Magnetism
def bar_magnet(ax, x, y, w=2.0, h=0.7, nleft=True):
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w / 2, h, fc="#d9d9d9", ec="black", lw=1.4, zorder=5))
    ax.add_patch(Rectangle((x, y - h / 2), w / 2, h, fc="white", ec="black", lw=1.4, zorder=5))
    ax.text(x - w / 4, y, "N" if nleft else "S", ha="center", va="center", fontsize=12, fontweight="bold", zorder=6)
    ax.text(x + w / 4, y, "S" if nleft else "N", ha="center", va="center", fontsize=12, fontweight="bold", zorder=6)


def bar_magnet_field(show_lines=True, compass_at=None):
    """Field lines around a single bar magnet (N on the right), arrows N -> S outside."""
    fig, ax = _fig(5.4, 3.4)
    bar_magnet(ax, 0, 0, w=2.4, h=0.8, nleft=False)
    if show_lines:
        for a in (0.75, 1.35, 2.0):
            w, h = 2.6 + 2.2 * a, 2 * a
            ax.add_patch(Ellipse((0, 0), w, h, fc="none", ec="black", lw=1.1))
            # outside the magnet the field runs from N (right) round to S (left): arrows point left on top, right underneath
            _arrow(ax, (0.12, h / 2), (-0.12, h / 2), lw=1.0, ms=11)
            _arrow(ax, (-0.12, -h / 2), (0.12, -h / 2), lw=1.0, ms=11)
        _arrow(ax, (1.25, 0), (3.3, 0), lw=1.1, ms=11)
        _arrow(ax, (-3.3, 0), (-1.25, 0), lw=1.1, ms=11)
    if compass_at:
        cx, cy = compass_at
        ax.add_patch(Circle((cx, cy), 0.3, fc="white", ec="black", lw=1.2))
        ax.text(cx, cy, "?", ha="center", va="center", fontsize=10)
    ax.set_xlim(-3.6, 3.6)
    ax.set_ylim(-2.3, 2.3)
    return _png(fig)


def two_poles(like=False):
    """Field between two facing poles: unlike (N facing S) gives straight lines across; like (N facing N) lines repel."""
    fig, ax = _fig(5.6, 3.0)
    bar_magnet(ax, -2.0, 0, w=2.0, h=0.8, nleft=True if like else True)
    # left magnet: S on right end if unlike? Set: left magnet N (left) S (right) for like=False -> facing poles S and N. Simpler:
    ax.clear()
    ax.set_aspect("equal")
    ax.axis("off")
    if like:
        bar_magnet(ax, -2.0, 0, w=2.0, h=0.8, nleft=False)   # S N  |  N S
        bar_magnet(ax, 2.0, 0, w=2.0, h=0.8, nleft=True)
        for y in (0.15, 0.45, 0.75, -0.15, -0.45, -0.75):
            s = np.sign(y) or 1
            xs = np.linspace(-0.95, -0.2, 50)
            ax.plot(xs, y + s * (xs + 0.95) ** 2 * 0.9, color="black", lw=1.0)
            xs2 = np.linspace(0.2, 0.95, 50)
            ax.plot(xs2, y + s * (0.95 - xs2) ** 2 * 0.9, color="black", lw=1.0)
        ax.text(0, 0, "", fontsize=8)
    else:
        bar_magnet(ax, -2.0, 0, w=2.0, h=0.8, nleft=False)   # S N  |  S N  -> facing N and S
        bar_magnet(ax, 2.0, 0, w=2.0, h=0.8, nleft=False)
        for y in (0.3, 0.1, -0.1, -0.3):
            _arrow(ax, (-0.95, y), (0.95, y), lw=1.1, ms=10)
        for y, c in ((0.55, 0.25), (-0.55, -0.25)):
            xs = np.linspace(-0.95, 0.95, 60)
            ax.plot(xs, y + c * np.cos(xs * np.pi / 1.9) * 0.6, color="black", lw=1.0)
    ax.set_xlim(-3.3, 3.3)
    ax.set_ylim(-1.6, 1.6)
    return _png(fig)


def straight_wire_field(current_into_page=True):
    """Concentric field lines around a straight wire seen end-on (dot = out of page, cross = into page)."""
    fig, ax = _fig(3.6, 3.6)
    for r in (0.6, 1.1, 1.6, 2.1):
        ax.add_patch(Circle((0, 0), r, fc="none", ec="black", lw=1.1))
        a = math.radians(60)
        s = 1 if current_into_page else -1
        p0 = (r * math.cos(a), r * math.sin(a))
        p1 = (r * math.cos(a - s * 0.08), r * math.sin(a - s * 0.08))
        ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=11, lw=1.0, color="black"))
    ax.add_patch(Circle((0, 0), 0.22, fc="white", ec="black", lw=1.4))
    if current_into_page:
        ax.plot([-0.12, 0.12], [-0.12, 0.12], color="black", lw=1.4)
        ax.plot([-0.12, 0.12], [0.12, -0.12], color="black", lw=1.4)
    else:
        ax.plot([0], [0], "o", color="black", markersize=4)
    ax.text(0, -2.45, "current " + ("into the page" if current_into_page else "out of the page"), ha="center", va="top", fontsize=9)
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-3.0, 2.5)
    return _png(fig)


def solenoid_field(label_ends=False):
    fig, ax = _fig(5.6, 3.0)
    n = 8
    for i in range(n):
        x = -2.1 + i * 0.6
        ax.add_patch(Ellipse((x, 0), 0.3, 1.2, fc="none", ec="black", lw=1.4))
    ax.plot([-2.6, -2.25], [-0.6, -0.6], color="black", lw=1.4)
    ax.plot([2.1, 2.6], [0.6, 0.6], color="black", lw=1.4)
    ax.text(-2.75, -0.6, "+", ha="right", va="center", fontsize=11)
    ax.text(2.75, 0.6, "−", ha="left", va="center", fontsize=11)
    _arrow(ax, (-1.8, 0), (1.8, 0), lw=1.3, ms=12)
    for yy in (1.0, -1.0):
        xs = np.linspace(-2.4, 2.4, 80)
        ax.plot(xs, yy * (1 + 0.25 * np.cos(xs * np.pi / 2.4)), color="black", lw=1.0)
    ax.add_patch(FancyArrowPatch((2.4, 0.8), (2.4, 1.1), arrowstyle="-|>", mutation_scale=10, lw=1.0, color="black"))
    ax.add_patch(FancyArrowPatch((-2.4, 1.1), (-2.4, 0.8), arrowstyle="-|>", mutation_scale=10, lw=1.0, color="black"))
    if label_ends:
        ax.text(-2.5, 0.0, "?", ha="right", va="center", fontsize=13, fontweight="bold")
        ax.text(2.5, 0.0, "?", ha="left", va="center", fontsize=13, fontweight="bold")
    ax.set_xlim(-3.4, 3.4)
    ax.set_ylim(-1.8, 1.8)
    return _png(fig)


def flemings_lhr(field="right", current="into", force=None):
    """Horizontal field (arrows), wire seen end-on with current into/out of the page, optional force arrow."""
    fig, ax = _fig(4.2, 3.4)
    for y in (-1.0, -0.5, 0.5, 1.0):
        if field == "right":
            _arrow(ax, (-2.2, y), (2.2, y), lw=1.0, ms=10)
        else:
            _arrow(ax, (2.2, y), (-2.2, y), lw=1.0, ms=10)
    ax.text(0, 1.45, "magnetic field", ha="center", va="bottom", fontsize=9)
    ax.add_patch(Circle((0, 0), 0.3, fc="white", ec="black", lw=1.6))
    if current == "into":
        ax.plot([-0.17, 0.17], [-0.17, 0.17], color="black", lw=1.6)
        ax.plot([-0.17, 0.17], [0.17, -0.17], color="black", lw=1.6)
    else:
        ax.plot([0], [0], "o", color="black", markersize=5)
    ax.text(0.45, -0.1, "current " + ("into page" if current == "into" else "out of page"), ha="left", va="center", fontsize=8.5)
    if force:
        # F = I L x B with x to the right, y up, z out of the page: field right + current out of page -> force up
        expected = "up" if (field == "right") == (current == "out") else "down"
        if force != expected:
            raise ValueError(f"flemings_lhr: field {field}, current {current} gives a force {expected}, not {force}")
        d = {"up": (0, 1), "down": (0, -1)}[force]
        _arrow(ax, (0, 0.35 * d[1]), (0, 1.3 * d[1]), lw=2.0, ms=14)
        ax.text(0.3, 0.72 * d[1], "force", ha="left", va="center", fontsize=9.5, bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none"))
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-1.8, 1.9)
    return _png(fig)


def coil_in_field():
    """Rectangular coil between magnet poles, viewed from above, with the two sides carrying current in opposite directions."""
    fig, ax = _fig(5.0, 3.0)
    ax.add_patch(Rectangle((-3.0, -0.6), 0.8, 1.2, fc="#d9d9d9", ec="black", lw=1.4))
    ax.add_patch(Rectangle((2.2, -0.6), 0.8, 1.2, fc="white", ec="black", lw=1.4))
    ax.text(-2.6, 0, "N", ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(2.6, 0, "S", ha="center", va="center", fontsize=12, fontweight="bold")
    for y in (-0.3, 0.3):
        _arrow(ax, (-2.1, y), (2.1, y), lw=0.9, ms=9)
    for x, into in ((-1.0, True), (1.0, False)):
        ax.add_patch(Circle((x, 0), 0.28, fc="white", ec="black", lw=1.5))
        if into:
            ax.plot([x - 0.15, x + 0.15], [-0.15, 0.15], color="black", lw=1.4)
            ax.plot([x - 0.15, x + 0.15], [0.15, -0.15], color="black", lw=1.4)
        else:
            ax.plot([x], [0], "o", color="black", markersize=4)
    ax.text(-1.0, -0.55, "side P", ha="center", va="top", fontsize=9)
    ax.text(1.0, -0.55, "side Q", ha="center", va="top", fontsize=9)
    ax.plot([-1.0, -1.0, 1.0, 1.0], [0.28, 1.0, 1.0, 0.28], color="black", lw=1.0, ls=":")
    ax.set_xlim(-3.3, 3.3)
    ax.set_ylim(-1.2, 1.5)
    return _png(fig)


# ================================================================== Ch 16 Radioactivity
def atom_diagram(protons, neutrons, electrons=None, symbol=None):
    electrons = protons if electrons is None else electrons
    fig, ax = _fig(3.4, 3.4)
    ax.add_patch(Circle((0, 0), 0.75, fc="#eeeeee", ec="black", lw=1.4))
    rng = np.random.default_rng(1)
    pts = []
    for i in range(protons + neutrons):
        for _ in range(100):
            p = rng.uniform(-0.45, 0.45, 2)
            if np.hypot(*p) <= 0.5 and all(np.hypot(*(p - q)) > 0.22 for q in pts):
                pts.append(p)
                break
    for i, p in enumerate(pts):
        ax.add_patch(Circle(p, 0.12, fc="#555555" if i < protons else "white", ec="black", lw=0.9))
    ax.add_patch(Circle((0, 0), 1.45, fc="none", ec="black", lw=0.9, ls="--"))
    for k in range(electrons):
        a = 2 * np.pi * k / max(electrons, 1) + 0.4
        ax.add_patch(Circle((1.45 * np.cos(a), 1.45 * np.sin(a)), 0.09, fc="black", ec="black"))
    ax.text(0, -1.8, f"{protons} protons (dark), {neutrons} neutrons (light), {electrons} electrons", ha="center", va="top", fontsize=8)
    if symbol:
        ax.text(1.7, 1.5, symbol, ha="left", va="center", fontsize=12)
    ax.set_xlim(-2.0, 2.4)
    ax.set_ylim(-2.3, 2.0)
    return _png(fig)


def decay_curve(n0, half_life, t_max=None, unit="min", marks=None):
    t_max = t_max or 4 * half_life
    ts = np.linspace(0, t_max, 200)
    ns = n0 * 0.5 ** (ts / half_life)
    pts = list(zip(ts, ns))
    steps = [m * 10 ** k for k in range(0, 7) for m in (1, 2, 5)]
    xstep = next(s for s in steps if t_max / s <= 8)
    ystep = next(s for s in steps if s >= 10 and n0 / s <= 8)
    xmax = (int(t_max / xstep) + (1 if t_max % xstep else 0)) * xstep
    ymax = (int(n0 / ystep) + (1 if n0 % ystep else 0)) * ystep
    return graph(pts, xmax, ymax, xstep, ystep, xlabel=f"time / {unit}", ylabel="count rate / counts per min" if n0 < 2000 else "number of undecayed nuclei", labels=marks)


def penetration_diagram():
    """Alpha stopped by paper, beta by aluminium, gamma reduced by lead."""
    fig, ax = _fig(6.0, 2.8)
    mats = [("paper", 1.6, 0.08), ("aluminium\n(few mm)", 3.4, 0.2), ("lead\n(cm)", 5.2, 0.45)]
    for name, x, w in mats:
        ax.add_patch(Rectangle((x, 0.2), w, 2.4, fc="#bbbbbb", ec="black", lw=1.2))
        ax.text(x + w / 2, -0.05, name, ha="center", va="top", fontsize=8.5)
    for y, name, stop in ((2.2, "alpha (α)", 1.6), (1.4, "beta (β)", 3.4), (0.6, "gamma (γ)", 6.0)):
        _arrow(ax, (0.2, y), (stop - 0.02, y), lw=1.6, ms=12)
        ax.text(0.1, y + 0.14, name, ha="left", va="bottom", fontsize=9)
    ax.text(6.15, 0.6, "(reduced)", ha="left", va="center", fontsize=8)
    ax.set_xlim(0, 7.6)
    ax.set_ylim(-0.9, 2.9)
    return _png(fig)


def rating_plate(lines, title="appliance"):
    """A rating label as found on an appliance, e.g. ['230 V', '2000 W', '50 Hz']."""
    fig, ax = _fig(3.6, 2.2)
    ax.add_patch(Rectangle((0, 0), 4.0, 2.4, fc="#f7f7f7", ec="black", lw=1.6))
    ax.text(2.0, 2.05, title, ha="center", va="center", fontsize=10, fontweight="bold")
    ax.plot([0.2, 3.8], [1.8, 1.8], color="black", lw=0.8)
    for i, t in enumerate(lines):
        ax.text(2.0, 1.45 - i * 0.45, t, ha="center", va="center", fontsize=10.5)
    ax.set_xlim(-0.2, 4.2)
    ax.set_ylim(-0.2, 2.6)
    return _png(fig)
