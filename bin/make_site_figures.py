#!/usr/bin/env python3
"""Generate the abstract illustrations used on the site.

These are deliberately schematic: they illustrate the kind of object the group works
with (state time courses, network graphs, null distributions) rather than showing
results from any particular paper. Re-run with:

    python3 bin/make_site_figures.py

Outputs land in assets/img/.
"""

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
os.makedirs(OUT, exist_ok=True)

INK = "#1f2933"
MUTED = "#8b97a6"
PALETTE = ["#3d5a80", "#ee6c4d", "#98c1d9", "#5c8001", "#a15ea8"]
rng = np.random.default_rng(11)


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", path)


def state_sequence(n=520, k=4, dwell=34):
    """A piecewise-constant state sequence with roughly geometric dwell times."""
    seq, t, s = [], 0, 0
    while t < n:
        length = max(6, int(rng.exponential(dwell)))
        seq.extend([s] * length)
        t += length
        s = rng.choice([j for j in range(k) if j != s])
    return np.array(seq[:n])


def smooth_noise(n, width):
    x = rng.normal(size=n + 4 * width)
    kernel = np.hanning(width)
    kernel /= kernel.sum()
    return np.convolve(x, kernel, "same")[2 * width : 2 * width + n]


def hero():
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    seq = state_sequence(560, 4, dwell=26)
    t = np.arange(len(seq))

    # state ribbon along the top
    for k in range(4):
        ax.fill_between(t, 3.30, 3.62, where=seq == k, color=PALETTE[k], lw=0)

    # three well-separated channels whose amplitude follows the active state
    for i, offset in enumerate([2.55, 1.70, 0.85]):
        base = smooth_noise(len(t), 26)
        base /= np.abs(base).max()
        gain = np.array([0.30 + 0.22 * ((k + i) % 4) for k in seq])
        gain = np.convolve(gain, np.ones(9) / 9, "same")
        ax.plot(t, offset + gain * base * 0.52, color=INK, lw=1.05, alpha=0.9, solid_capstyle="round")

    # mark a few state transitions
    for c in np.where(np.diff(seq) != 0)[0][::2]:
        ax.plot([c, c], [0.15, 3.24], color=MUTED, lw=0.5, ls=(0, (2, 4)), alpha=0.45)

    ax.set_xlim(-4, len(t) + 4)
    ax.set_ylim(0, 4.05)
    ax.axis("off")
    ax.text(0, 3.78, "recurring network states", color=MUTED, fontsize=9)
    ax.text(0, 0.0, "time", color=MUTED, fontsize=9)
    save(fig, "lab_hero.png")


def dynamics():
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.0), gridspec_kw={"width_ratios": [1.5, 1]})
    ax = axes[0]
    seq = state_sequence(400, 4)
    for k in range(4):
        ax.fill_between(np.arange(len(seq)), 0, 1, where=seq == k, color=PALETTE[k], lw=0)
    ax.set_xlim(0, len(seq))
    ax.set_ylim(-0.55, 1.1)
    ax.axis("off")
    ax.text(0, -0.42, "state time course", color=MUTED, fontsize=8)

    ax = axes[1]
    ax.axis("off")
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.25, 1.25)
    ang = np.linspace(0, 2 * np.pi, 5)[:4] + np.pi / 4
    xy = np.c_[np.cos(ang), np.sin(ang)]
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            ax.annotate(
                "",
                xy=xy[j] * 0.72,
                xytext=xy[i] * 0.72,
                arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=0.8, alpha=0.55, connectionstyle="arc3,rad=0.22"),
            )
    for i in range(4):
        ax.scatter(*xy[i], s=520, color=PALETTE[i], zorder=3, edgecolors="white", linewidths=1.5)
    ax.text(0, -1.18, "transition probabilities", color=MUTED, fontsize=8, ha="center")
    save(fig, "research_dynamics.png")


def statistics():
    fig, ax = plt.subplots(figsize=(6.6, 3.0))
    null = rng.normal(0, 1, 40000)
    ax.hist(null, bins=70, color="#c9d4e0", edgecolor="white", linewidth=0.4)
    obs = 2.9
    ax.axvline(obs, color=PALETTE[1], lw=2)
    ax.axvline(np.percentile(null, 95), color=MUTED, lw=1, ls="--")
    ax.text(obs + 0.12, ax.get_ylim()[1] * 0.78, "observed", color=PALETTE[1], fontsize=9)
    ax.text(np.percentile(null, 95) - 0.12, ax.get_ylim()[1] * 0.52, "95th pct\nof the null", color=MUTED, fontsize=8, ha="right")
    ax.text(-3.9, ax.get_ylim()[1] * 0.86, "permutation null", color=MUTED, fontsize=9)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_yticks([])
    ax.set_xticks([])
    save(fig, "research_statistics.png")


def perception():
    fig, ax = plt.subplots(figsize=(6.6, 3.0))
    t = np.linspace(-0.4, 1.0, 400)
    ongoing = 0.55 * np.sin(2 * np.pi * 7 * t + 0.6) * np.exp(-0.25 * np.abs(t))
    evoked = np.exp(-((t - 0.19) ** 2) / (2 * 0.045**2)) * 1.35 - np.exp(-((t - 0.34) ** 2) / (2 * 0.07**2)) * 0.8
    ax.plot(t, ongoing, color=MUTED, lw=1.3, label="ongoing activity")
    ax.plot(t, ongoing + evoked, color=PALETTE[0], lw=1.8, label="ongoing + stimulus")
    ax.axvline(0, color=PALETTE[1], lw=1.2)
    ax.text(0.012, -1.15, "stimulus", color=PALETTE[1], fontsize=9)
    ax.legend(frameon=False, fontsize=8, loc="upper right", labelcolor=MUTED)
    ax.set_ylim(-1.3, 1.9)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_yticks([])
    ax.set_xticks([])
    save(fig, "research_perception.png")


def clinical():
    fig, ax = plt.subplots(figsize=(6.6, 3.0))
    n, k = 16, 6
    grid = rng.random((k, n))
    grid[:, 9:] += np.linspace(0, 0.55, n - 9)
    grid = np.clip(grid, 0, 1.4)
    ax.imshow(grid, aspect="auto", cmap="BuPu", vmin=0, vmax=1.4)
    ax.add_patch(Rectangle((8.5, -0.5), n - 8.5, k, fill=False, edgecolor=PALETTE[1], lw=1.8))
    ax.text(n - 0.3, -0.95, "deviation from the normative range", color=PALETTE[1], fontsize=8.5, ha="right")
    ax.text(-0.4, k - 0.15, "individuals", color=MUTED, fontsize=8, rotation=90, va="bottom", ha="right")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    save(fig, "research_clinical.png")


if __name__ == "__main__":
    hero()
    dynamics()
    statistics()
    perception()
    clinical()
