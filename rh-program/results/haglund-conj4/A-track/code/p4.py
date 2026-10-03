# p4.py -- A-track P4: pictures of the branches (Im z against Re z) from the census files.
# Colors: first three slots of the dataviz reference palette (validated all-pairs, light surface); end types are also
# distinguished by marker shape (secondary encoding), and a legend names them.
import sys, os, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
COL = {"landed": "#2a78d6", "u0": "#eb6834", "exit-right": "#1baf7a"}
LAB = {"landed": "lands on the real axis", "u0": "ends at a non-real zero of Xi_{k+1}", "exit-right": "leaves through Re z = X_k"}

def style(ax):
    ax.set_facecolor(SURF)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK2)
    ax.tick_params(colors=INK2, labelsize=9)
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)

def branches_plot(fn, out, title, xlim=None, ylim=None, show_real=True):
    R = json.load(open(fn))
    k = R["k"]
    fig, ax = plt.subplots(figsize=(11, 5.2), dpi=150)
    fig.patch.set_facecolor(SURF)
    style(ax)
    seen = set()
    for r in R["branches"]:
        P = r["path"]
        xs = [p[1] for p in P]; ys = [p[2] for p in P]
        e = r["end"] if r["end"] in COL else "u0"
        lab = LAB[e].replace("{k+1}", str(k + 1)).replace("X_k", "X_%d" % k) if e not in seen else None
        seen.add(e)
        ax.plot(xs, ys, color=COL[e], linewidth=1.3, label=lab, zorder=2)
        ax.plot([xs[0]], [ys[0]], "o", ms=4.5, mfc="white", mec=INK, mew=0.9, zorder=3)
        if r["end"] == "landed":
            ax.plot([r.get("x_land", xs[-1])], [0], "v", ms=6, color=COL["landed"], mec=INK, mew=0.5, zorder=4)
        elif r["end"] == "u0":
            ax.plot([xs[-1]], [ys[-1]], "s", ms=4.5, color=COL["u0"], mec=INK, mew=0.5, zorder=4)
        else:
            ax.plot([xs[-1]], [ys[-1]], "x", ms=6, color=INK, mew=1.2, zorder=4)
    ax.plot([], [], "o", ms=4.5, mfc="white", mec=INK, mew=0.9, linestyle="none", label="start: zero of Xi_%d (u = 1)" % k)
    ax.plot([], [], "s", ms=4.5, color=COL["u0"], mec=INK, mew=0.5, linestyle="none", label="end: zero of Xi_%d (u = 0)" % (k + 1))
    ax.plot([], [], "v", ms=6, color=COL["landed"], mec=INK, mew=0.5, linestyle="none", label="landing point (local max of S_%d)" % k)
    if show_real:
        rz = R["axis"]["zeros_Xik1"]
        ax.plot(rz, [0] * len(rz), "|", ms=7, color=INK2, label="real zeros of Xi_%d" % (k + 1), zorder=1)
    if R["tag"] == "P1":
        ax.axvline(R["window"][1], color=INK2, linewidth=0.8, linestyle="--", zorder=1)
    ax.set_xlabel("Re z", color=INK, fontsize=10); ax.set_ylabel("Im z", color=INK, fontsize=10)
    if xlim: ax.set_xlim(*xlim)
    if ylim: ax.set_ylim(*ylim)
    else: ax.set_ylim(bottom=-0.5)
    ax.set_title(title, color=INK, fontsize=11, loc="left")
    ax.legend(loc="upper left", fontsize=8, frameon=False, labelcolor=INK)
    fig.tight_layout()
    fig.savefig(out, facecolor=SURF)
    plt.close(fig)
    print("wrote", out)

if __name__ == "__main__":
    os.makedirs(F, exist_ok=True)
    for k in [int(a) for a in sys.argv[1:]]:
        fn = os.path.join(D, "census_k%d.json" % k)
        R = json.load(open(fn))
        branches_plot(fn, os.path.join(F, "branches_k%d.png" % k),
                      "Pencil Xi_%d + t Phi_%d: every branch from a non-real zero of Xi_%d in W_%d = [0, %.2f] x [0, %.0f]"
                      % (k, k + 1, k, k, R["window"][1], R["Y"]))
