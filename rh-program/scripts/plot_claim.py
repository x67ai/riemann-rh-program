#!/usr/bin/env python3
"""Two-panel picture of a numerical claim over a range (KICKSTART 10(v)).

usage: plot_claim.py DATA.csv OUT.png --title "..." [--law "LABEL=EXPR" ...] [--ylabel "..."]

DATA.csv   two columns x,y (a header line is skipped); the raw points of the claim.
--law      a candidate law as LABEL=EXPR, EXPR a Python expression in x using
           log, sqrt, exp, pi (for example  "0.2 log^2 x=0.2*log(x)**2"  or
           "x^0.25 (scaled)=0.74*x**0.25"). Any number of laws.

Left panel: the points on log-log axes with every law drawn through the range.
Right panel: the LOCAL SLOPE d log y / d log x between consecutive points, with
the slope each law has at the same places. A power law is a horizontal line on
the right; anything that keeps falling is not one. The picture proves nothing
(BRIEF-WARNINGS W2): it is what the reader of a claim looks at before the
sentence about the claim is written.
"""
import csv, math, sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ENV = {"log": math.log, "sqrt": math.sqrt, "exp": math.exp, "pi": math.pi}

def main():
    a = sys.argv[1:]
    if len(a) < 2:
        sys.exit(__doc__)
    data, out = a[0], a[1]
    title, ylabel, laws = "", "y", []
    i = 2
    while i < len(a):
        if a[i] == "--title":
            title = a[i + 1]
        elif a[i] == "--ylabel":
            ylabel = a[i + 1]
        elif a[i] == "--law":
            label, expr = a[i + 1].split("=", 1)
            laws.append((label, expr))
        else:
            sys.exit("unknown argument %r\n%s" % (a[i], __doc__))
        i += 2
    pts = []
    for row in csv.reader(open(data, encoding="utf-8")):
        try:
            pts.append((float(row[0]), float(row[1])))
        except (ValueError, IndexError):
            continue
    pts.sort()
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    f = lambda expr, x: eval(expr, {"__builtins__": {}}, dict(ENV, x=x))

    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.2))
    ax.loglog(xs, ys, "o", color="black", label="data (%d points)" % len(pts))
    grid = [xs[0] * (xs[-1] / xs[0]) ** (k / 200) for k in range(201)]
    for label, expr in laws:
        ax.loglog(grid, [f(expr, x) for x in grid], "-", linewidth=1.2, label=label)
    ax.set_xlabel("x")
    ax.set_ylabel(ylabel)
    ax.set_title("points and candidate laws")
    ax.legend(fontsize=8)
    ax.grid(True, which="both", linewidth=0.3)

    mids = [math.sqrt(xs[k] * xs[k + 1]) for k in range(len(xs) - 1)]
    slope = lambda u, v, x0, x1: (math.log(v) - math.log(u)) / (math.log(x1) - math.log(x0))
    bx.semilogx(mids, [slope(ys[k], ys[k + 1], xs[k], xs[k + 1]) for k in range(len(xs) - 1)],
                "o-", color="black", label="data")
    for label, expr in laws:
        bx.semilogx(mids, [slope(f(expr, xs[k]), f(expr, xs[k + 1]), xs[k], xs[k + 1])
                           for k in range(len(xs) - 1)], "--", linewidth=1.2, label=label)
    bx.axhline(0, color="gray", linewidth=0.5)
    bx.set_xlabel("x (midpoint of each step)")
    bx.set_ylabel("local slope  d log y / d log x")
    bx.set_title("local slope between consecutive points")
    bx.legend(fontsize=8)
    bx.grid(True, which="both", linewidth=0.3)
    if title:
        fig.suptitle(title, fontsize=10)
    fig.tight_layout()
    fig.savefig(out, dpi=130)
    print("%s: %d points, %d law(s) -> %s" % (data, len(pts), len(laws), out))

if __name__ == "__main__":
    main()
