"""Extra drawers for the TYS questions added to the 'O level 2026 MCQ practice' set (31 Oct 2026)."""
import io

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle  # noqa: E402

DPI = 150


def _fig(w, h):
    fig, ax = plt.subplots(figsize=(w, h), dpi=DPI)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def _png(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, bbox_inches="tight", pad_inches=0.05, facecolor="white")
    plt.close(fig)
    return buf.getvalue()


def _arrow(ax, p0, p1, lw=1.6, ms=13, style="-|>"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms, lw=lw, color="black"))


def side_by_side(pngs, titles=None, width=7.6):
    """Join several PNG images left to right into one figure, with optional titles under each."""
    imgs = [plt.imread(io.BytesIO(p), format="png") for p in pngs]
    fig, axes = plt.subplots(1, len(imgs), figsize=(width, width / len(imgs) * 0.75), dpi=DPI)
    for i, (ax, im) in enumerate(zip(np.atleast_1d(axes), imgs)):
        ax.imshow(im)
        ax.axis("off")
        if titles:
            ax.set_title(titles[i], fontsize=10, y=-0.16)
    fig.tight_layout()
    return _png(fig)


def two_wave_graphs(lam_cm, period_s, amp=1.0):
    """Displacement-distance (cm) and displacement-time (s) graphs of the same water wave, 1.5 cycles each."""
    fig, axes = plt.subplots(1, 2, figsize=(7.6, 2.6), dpi=DPI)
    for ax, L, lab in ((axes[0], lam_cm, "distance / cm"), (axes[1], period_s, "time / s")):
        xx = np.linspace(0, 1.5 * L, 300)
        ax.plot(xx, amp * np.sin(2 * np.pi * xx / L), color="black", lw=2.0)
        ax.axhline(0, color="black", lw=1.0)
        ax.set_xlim(0, 1.5 * L * 1.05)
        ax.set_ylim(-1.6 * amp, 1.6 * amp)
        ax.set_xticks(np.round(np.arange(0, 1.5 * L + 1e-9, L / 2), 4))
        ax.set_yticks([])
        ax.set_xlabel(lab, fontsize=10)
        ax.set_ylabel("displacement", fontsize=10)
        ax.tick_params(labelsize=9)
        ax.grid(axis="x", color="#BBBBBB", lw=0.6)
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    return buf.getvalue()


def parallel_wires():
    """Two vertical wires P and Q, both carrying a downward current."""
    fig, ax = _fig(4.2, 4.0)
    for x, name in ((0.0, "P"), (2.4, "Q")):
        ax.plot([x, x], [0, 4], color="black", lw=1.8)
        _arrow(ax, (x, 3.3), (x, 2.9), lw=1.6)
        _arrow(ax, (x, 0.6), (x, 0.2), lw=1.6)
        ax.text(x, 4.15, name, ha="center", va="bottom", fontsize=12, fontweight="bold")
    for x in (0.0, 2.4):
        ax.text(x + 0.15, 1.6, "current", rotation=90, fontsize=8.5, va="center")
    ax.text(1.2, -0.15, "both wires lie in the plane of the page", ha="center", fontsize=8.5)
    ax.set_xlim(-0.6, 4.0)
    ax.set_ylim(-0.2, 4.5)
    return _png(fig)


def ripple_crests(n, gap_label="6.0 cm"):
    """Circular crests around a dipper P, the gap between the two outermost crests marked."""
    fig, ax = _fig(3.8, 3.8)
    for i in range(1, n + 1):
        ax.add_patch(Circle((0, 0), 0.55 * i, fc="none", ec="black", lw=1.4))
    ax.plot([0], [0], "o", color="black", markersize=4)
    ax.text(0.1, 0.1, "P", fontsize=11)
    a = np.deg2rad(40)
    r0, r1 = 0.55 * (n - 1), 0.55 * n
    _arrow(ax, (r0 * np.cos(a), r0 * np.sin(a)), (r1 * np.cos(a), r1 * np.sin(a)), lw=1.2, ms=10, style="<|-|>")
    ax.text(r1 * np.cos(a) + 0.1, r1 * np.sin(a) + 0.15, gap_label, fontsize=10)
    ax.set_xlim(-0.6 * n - 0.3, 0.6 * n + 1.4)
    ax.set_ylim(-0.6 * n - 0.3, 0.6 * n + 0.6)
    return _png(fig)


def ripple_rings(n):
    """n concentric crests around a wave source (no measurement marked)."""
    fig, ax = _fig(3.4, 3.4)
    for i in range(1, n + 1):
        ax.add_patch(Circle((0, 0), 0.5 * i, fc="none", ec="black", lw=1.4))
    ax.plot([0], [0], "o", color="black", markersize=4)
    ax.annotate("wave source", (0, 0), xytext=(-0.5 * n - 1.6, 0.5 * n * 0.7), fontsize=9.5,
                arrowprops=dict(arrowstyle="-", lw=0.8))
    ax.annotate("wave crests", (0.5 * n * 0.72, 0.5 * n * 0.69), xytext=(0.5 * n + 0.2, 0.5 * n + 0.2), fontsize=9.5,
                arrowprops=dict(arrowstyle="-", lw=0.8))
    ax.set_xlim(-0.5 * n - 1.8, 0.5 * n + 1.8)
    ax.set_ylim(-0.5 * n - 0.3, 0.5 * n + 0.6)
    return _png(fig)


def _coil(ax, x0, x1, y0, y1, turns=8):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc="#e8e8e8", ec="black", lw=1.4))
    for xx in np.linspace(x0 + 0.15, x1 - 0.15, turns):
        ax.plot([xx, xx + 0.12], [y1 + 0.12, y0 - 0.12], color="black", lw=1.2)


def electromagnet_attracts(n_right=True):
    """Electromagnet (coil on a battery) attracting a permanent bar magnet placed to its right."""
    fig, ax = _fig(5.4, 2.6)
    _coil(ax, 0, 2.4, 0.9, 1.6)
    ax.plot([0.1, 0.1, 1.05], [0.9, 0.1, 0.1], color="black", lw=1.4)
    ax.plot([1.35, 2.3, 2.3], [0.1, 0.1, 0.9], color="black", lw=1.4)
    ax.plot([1.05, 1.05], [-0.15, 0.35], color="black", lw=2.2)
    ax.plot([1.35, 1.35], [-0.02, 0.22], color="black", lw=2.2)
    ax.add_patch(Rectangle((2.8, 0.85), 2.2, 0.8, fc="white", ec="black", lw=1.6))
    ax.text(3.05, 1.25, "N" if n_right else "S", fontsize=12, va="center")
    ax.text(4.75, 1.25, "S" if n_right else "N", fontsize=12, va="center", ha="right")
    ax.text(1.2, 1.95, "electromagnet", ha="center", fontsize=9.5)
    ax.text(3.9, 1.95, "permanent magnet", ha="center", fontsize=9.5)
    ax.set_xlim(-0.3, 5.3)
    ax.set_ylim(-0.4, 2.3)
    return _png(fig)


def vi_three_wires(slopes=(0.5, 0.75, 1.0), names=("X", "Y", "Z")):
    """Voltage-current graphs (straight lines through the origin) for three wires; no scale numbers."""
    fig, ax = plt.subplots(figsize=(4.4, 3.2), dpi=DPI)
    for k, nm in zip(slopes, names):
        ax.plot([0, 1], [0, k], color="black", lw=1.8)
        ax.text(1.02, k, nm, fontsize=11, va="center")
    ax.set_xlim(0, 1.15)
    ax.set_ylim(0, max(slopes) * 1.15)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("current / A", fontsize=10)
    ax.set_ylabel("voltage / V", fontsize=10)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    return buf.getvalue()


def pendulum_start():
    """Pendulum hanging vertically, moving to the right, at the moment the stopwatch starts."""
    fig, ax = _fig(3.0, 3.2)
    ax.plot([-1.0, 1.0], [3.0, 3.0], color="black", lw=2.0)
    ax.plot([0, 0], [3.0, 0.6], color="black", lw=1.4)
    ax.add_patch(Circle((0, 0.4), 0.2, fc="#bbbbbb", ec="black", lw=1.4))
    _arrow(ax, (0.3, 0.4), (1.1, 0.4))
    ax.text(1.2, 0.4, "direction", va="center", fontsize=10)
    ax.set_xlim(-1.3, 2.4)
    ax.set_ylim(0, 3.2)
    return _png(fig)


def plank_point_x(wl, wr):
    """Uniform plank (8 m) pivoted at its middle; wl N hangs 2 m left of the pivot, wr N at the right end; point X marked at
    the left end with no force drawn (the question asks for its direction)."""
    fig, ax = _fig(6.6, 3.0)
    ax.add_patch(Rectangle((0, 0), 8.0, 0.3, fc="#eeeeee", ec="black", lw=1.8))
    ax.add_patch(plt.Polygon([(4, 0), (3.6, -0.75), (4.4, -0.75)], fc="white", ec="black", lw=1.6))
    ax.text(4.55, -0.55, "pivot", fontsize=9.5)
    for x, lab in ((2, f"{wl} N"), (8, f"{wr} N")):
        _arrow(ax, (x, 1.9), (x, 0.34), lw=1.9, ms=15)
        ax.text(x, 2.0, lab, ha="center", va="bottom", fontsize=10.5)
    ax.plot([0], [0.15], "o", color="black", markersize=6)
    ax.text(0, 0.55, "X", ha="center", fontsize=12, fontweight="bold")
    for i, (x0, x1, t) in enumerate(((0, 2, "2 m"), (2, 4, "2 m"), (4, 8, "4 m"))):
        _arrow(ax, (x0, -1.3), (x1, -1.3), lw=1.0, ms=10, style="<|-|>")
        ax.text((x0 + x1) / 2, -1.2, t, ha="center", va="bottom", fontsize=9.5)
    ax.set_xlim(-0.6, 8.6)
    ax.set_ylim(-1.7, 2.6)
    return _png(fig)


def stacked(pngs, titles=None, width=6.4):
    """Stack PNG images top to bottom (each at full width), with an optional caption under each."""
    imgs = [plt.imread(io.BytesIO(p), format="png") for p in pngs]
    hs = [im.shape[0] / im.shape[1] * width for im in imgs]
    fig, axes = plt.subplots(len(imgs), 1, figsize=(width, sum(hs) + 0.45 * len(imgs)), dpi=DPI,
                             gridspec_kw={"height_ratios": hs})
    for i, (ax, im) in enumerate(zip(np.atleast_1d(axes), imgs)):
        ax.imshow(im)
        ax.axis("off")
        if titles:
            ax.set_title(titles[i], fontsize=10, y=-0.22)
    fig.tight_layout()
    return _png(fig)


def sound_particles(mark="compression", seed=4):
    """Air particles in a sound wave (bands of crowded and spread-out dots) with a line X at a compression or rarefaction."""
    rng = np.random.default_rng(seed)
    fig, ax = plt.subplots(figsize=(7.0, 1.9), dpi=DPI)
    lam = 2.0
    xs = []
    while len(xs) < 1400:
        x = rng.uniform(0, 8)
        dens = 0.5 + 0.5 * np.cos(2 * np.pi * x / lam)       # crowded where cos = 1 (x = 0, 2, 4, 6, 8)
        if rng.uniform() < 0.12 + 0.88 * dens:
            xs.append(x)
    ys = rng.uniform(0, 1, len(xs))
    ax.scatter(xs, ys, s=2.5, color="black")
    xm = 4.0 if mark == "compression" else 5.0
    ax.plot([xm, xm], [-0.12, 1.12], color="black", lw=2.2)
    ax.text(xm, -0.32, "X", ha="center", va="center", fontsize=12, fontweight="bold")
    ax.annotate("", (6.8, 1.3), (5.3, 1.3), arrowprops=dict(arrowstyle="-|>", lw=1.5))
    ax.text(5.2, 1.3, "sound wave ", ha="right", va="center", fontsize=10)
    ax.set_xlim(0, 8)
    ax.set_ylim(-0.5, 1.5)
    ax.axis("off")
    return _png(fig)


def parallel_with_cell(plus_right=True):
    """Resistor P (top), a cell (middle) and resistor Q (bottom), all connected between the same two side wires.
    The cell's + terminal (long plate) is on the right if plus_right."""
    fig, ax = _fig(4.6, 3.4)
    for y in (2.4, 1.2, 0.0):
        ax.plot([0, 4], [y, y], color="black", lw=1.5)
    ax.plot([0, 0], [0, 2.4], color="black", lw=1.5)
    ax.plot([4, 4], [0, 2.4], color="black", lw=1.5)
    for y, nm in ((2.4, "P"), (0.0, "Q")):
        ax.add_patch(Rectangle((1.5, y - 0.18), 1.0, 0.36, fc="white", ec="black", lw=1.5))
        ax.text(2.0, y + 0.35, nm, ha="center", fontsize=12, fontweight="bold")
    ax.add_patch(Rectangle((1.86, 1.1), 0.28, 0.2, fc="white", ec="white", zorder=3))
    xl, xs = (2.15, 1.85) if plus_right else (1.85, 2.15)       # long plate x, short plate x
    ax.plot([xl, xl], [0.8, 1.6], color="black", lw=1.6, zorder=4)
    ax.plot([xs, xs], [1.0, 1.4], color="black", lw=3.0, zorder=4)
    ax.text(xl + (0.15 if plus_right else -0.15), 1.75, "+", ha="center", fontsize=12)
    ax.text(xs + (-0.15 if plus_right else 0.15), 1.7, "−", ha="center", fontsize=12)
    ax.set_xlim(-0.3, 4.3)
    ax.set_ylim(-0.5, 3.0)
    return _png(fig)
