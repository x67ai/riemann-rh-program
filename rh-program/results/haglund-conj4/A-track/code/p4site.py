# p4site.py -- A-track P4: the site of the Conjecture-1 violation (Xi_27 zero 3143.2207 + 0.3153i) in pencils 26 and 27.
import os, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from p4 import style, COL, SURF, INK, INK2, D, F

def panel(ax, R, xlim, ylim, title, hi=None, real_k=True, real_k1=True):
    style(ax)
    for r in R["branches"]:
        P = r["path"]
        xs = [p[1] for p in P]; ys = [p[2] for p in P]
        if max(xs) < xlim[0] - 1 or min(xs) > xlim[1] + 1:
            continue
        e = r["end"] if r["end"] in COL else "u0"
        lw = 2.0 if (hi and any(abs(r["start"][0] - h) < 1e-3 for h in hi)) else 1.0
        ax.plot(xs, ys, color=COL[e], linewidth=lw, zorder=2)
        ax.plot([xs[0]], [ys[0]], "o", ms=4.5, mfc="white", mec=INK, mew=0.9, zorder=3)
        if r["end"] == "landed":
            ax.plot([r.get("x_land", xs[-1])], [0], "v", ms=6.5, color=COL["landed"], mec=INK, mew=0.5, zorder=4)
        elif r["end"] == "u0":
            ax.plot([xs[-1]], [ys[-1]], "s", ms=5, color=COL["u0"], mec=INK, mew=0.5, zorder=4)
    k = R["k"]
    if real_k:
        rz = [x for x in R["axis"]["zeros_Xik"] if xlim[0] <= x <= xlim[1]]
        ax.plot(rz, [0] * len(rz), "|", ms=12, mew=1.6, color=INK, label="real zeros of Xi_%d (u = 1)" % k, zorder=5)
    if real_k1:
        rz = [x for x in R["axis"]["zeros_Xik1"] if xlim[0] <= x <= xlim[1]]
        ax.plot(rz, [0] * len(rz), "|", ms=7, mew=1.0, color=INK2, label="real zeros of Xi_%d (u = 0)" % (k + 1), zorder=5)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_xlabel("Re z", color=INK, fontsize=9); ax.set_ylabel("Im z", color=INK, fontsize=9)
    ax.set_title(title, color=INK, fontsize=10, loc="left")

if __name__ == "__main__":
    R26 = json.load(open(os.path.join(D, "frontier_k26.json")))
    R27 = json.load(open(os.path.join(D, "frontier_k27.json")))
    fig, axs = plt.subplots(1, 3, figsize=(15, 5.2), dpi=150, gridspec_kw={"width_ratios": [1.4, 1, 1]})
    fig.patch.set_facecolor(SURF)
    hi26 = [3130.2619, 3132.1660]
    panel(axs[0], R26, (3112, 3160), (-1, 58), "(a) pencil 26: branches from zeros of Xi_26 near the site", hi26, True, False)
    panel(axs[1], R26, (3139, 3148), (-0.05, 1.6), "(b) pencil 26 near the axis", hi26)
    axs[1].annotate("u = 0 end: 3143.2207 + 0.3153i\n(zero of Xi_27)", (3143.2207, 0.3153), (3139.4, 1.05), fontsize=8,
                    color=INK, arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
    axs[1].annotate("lands at 3145.2290\nu* = 3.3e-76", (3145.229, 0.0), (3145.6, 0.75), fontsize=8, color=INK,
                    arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
    panel(axs[2], R27, (3140, 3151), (-0.05, 1.9), "(c) pencil 27 near the axis", [3143.2207])
    axs[2].annotate("from 3143.2207 + 0.3153i:\nlands at 3143.2466, u* = 0.41", (3143.2466, 0.0), (3140.3, 1.2), fontsize=8,
                    color=INK, arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
    h = [plt.Line2D([], [], color=COL["landed"], lw=1.5, label="branch that lands"),
         plt.Line2D([], [], color=COL["u0"], lw=1.5, label="branch that ends at a non-real zero of Xi_{k+1}"),
         plt.Line2D([], [], color=COL["exit-right"], lw=1.5, label="branch that leaves the window"),
         plt.Line2D([], [], marker="o", ms=4.5, mfc="white", mec=INK, ls="none", label="start: zero of Xi_k"),
         plt.Line2D([], [], marker="s", ms=5, color=COL["u0"], mec=INK, ls="none", label="end: zero of Xi_{k+1}"),
         plt.Line2D([], [], marker="v", ms=6.5, color=COL["landed"], mec=INK, ls="none", label="landing point")]
    fig.legend(handles=h, loc="lower center", ncol=6, fontsize=8, frameon=False, labelcolor=INK)
    for ax in axs[1:]:
        ax.legend(loc="upper right", fontsize=7.5, frameon=False, labelcolor=INK)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    out = os.path.join(F, "site_k26_k27.png")
    fig.savefig(out, facecolor=SURF)
    print("wrote", out)
