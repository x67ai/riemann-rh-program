#!/usr/bin/env python3
"""Reader-O: the T_0.75 seed statistics recomputed with own code from the CSVs on disk (writer's seeds 1-12) and from the reader's
own numpy runs (seeds 1001 at 1e9; 1002-1009 at 1e10). Log: logs/seeds_O.log
 sup-slope  = fr fit.py convention: running max over bins of max(maxE+, -minE-) vs bin upper edge, LSQ in log10-log10 on bins with
              upper edge in [w0, Xmax];
 ms-slope   = NOTE §3.1 convention: six-bin windows of the 20/decade grid aligned at 1e4, M = (sum sumEc2 + count rho^2/12)/sum count,
              LSQ of log10 M vs log10(window start) over windows starting in [w0, Xmax);
 drift      = LSQ slope a of the bin midrange (maxE+ + minE-)/2 against x over bins in [Xmax/10, Xmax]; a*Xmax vs sup|E| at the top and
              vs the rho-tail standard deviation rho*sqrt(Y^(alpha-2)/((2-alpha) ln Y))*Xmax.
"""
import glob, math, re, itertools, sys
import numpy as np

HERE = sys.path[0]; ROOT = HERE + "/../../"
FR = ROOT + "novel-wave-s37/beurling-frontier/verify/"; WR = HERE + "/../verify/"

def parse(path):
    """returns {run: (rho, Y, rows[lo, hi, mx, mn, s2, cnt])}; handles thin.c multi-run files and thin_O files."""
    runs = {}; cur = None
    for line in open(path):
        if line.startswith("#"):
            m = re.search(r"run=(\S+)", line) or re.search(r"seed=(\d+)", line)
            if m and "rho=" in line:
                cur = m.group(1) if "run=" in line else "O_s" + m.group(1)
                runs[cur] = [float(re.search(r"rho=([0-9.eE+-]+)", line).group(1)), float(re.search(r"Y=(\d+)", line).group(1)), []]
            continue
        f = line.strip().split(",")
        if len(f) == 8: runs[f[0]][2].append([float(v) for v in f[1:7]])
        elif len(f) == 6: runs[cur][2].append([float(v) for v in f])
    return {r: (v[0], v[1], np.array(v[2])) for r, v in runs.items()}

def sup_slope(a, w0, X):
    hi = a[:, 1]; M = np.maximum.accumulate(np.maximum(a[:, 2], -a[:, 3])); m = (hi >= w0) & (hi <= X)
    return np.polyfit(np.log10(hi[m]), np.log10(M[m]), 1)[0]

def ms_windows(a, rho):
    k0 = int(np.argmin(np.abs(a[:, 0] - 1e4))); out = []
    for j in range(k0, a.shape[0] - 5, 6):
        b = a[j:j + 6]; out.append((b[0, 0], (b[:, 4].sum() + b[:, 5].sum() * rho * rho / 12) / b[:, 5].sum()))
    return np.array(out)

def ms_slope(W, w0):
    m = W[:, 0] >= w0 * 0.999
    return np.polyfit(np.log10(W[m, 0]), np.log10(W[m, 1]), 1)[0]

def drift(a, rho, Y, X, alpha=0.75):
    m = a[:, 0] >= X / 10.0; x = np.sqrt(a[m, 0] * a[m, 1]); mid = 0.5 * (a[m, 2] + a[m, 3])
    slope = np.polyfit(x, mid, 1)[0]; supE = max(a[m, 2].max(), -a[m, 3].min())
    tail_sd = rho * math.sqrt(Y ** (alpha - 2) / ((2 - alpha) * math.log(Y))) * X
    return slope * X, supE, tail_sd

def stat(v):
    v = np.array(v); return f"{v.mean():.3f}±{v.std(ddof=1) / math.sqrt(len(v)):.3f} (n={len(v)})"

def main():
    runs = {}
    runs.update({("W", r): v for r, v in parse(FR + "data_big/bern_a0.75.csv").items()})
    for f in sorted(glob.glob(WR + "data_big/bern_a0.75_s*.csv")): runs.update({("W", r): v for r, v in parse(f).items()})
    for f in sorted(glob.glob(HERE + "/data/bern_O_a0.75_s*_1e10_dec.csv")): runs.update({("O", r): v for r, v in parse(f).items()})
    X = 1e10; wins = (1e4, 1e6, 1e7); res = {}
    print("run            rho      sup[1e4] sup[1e6] sup[1e7] |  ms[1e4]  ms[1e6]  ms[1e7] | drift*X  sup|E|top  tail_sd*X")
    for key in sorted(runs, key=lambda k: (k[0], int(re.search(r"s(\d+)", k[1]).group(1)))):
        rho, Y, a = runs[key]
        if a[-1, 1] < 0.99 * X: continue
        W = ms_windows(a, rho); s = [sup_slope(a, w, X) for w in wins]; ms = [ms_slope(W, w) for w in wins]
        d = drift(a, rho, Y, X); res[key] = (s, ms, d)
        print(f"{key[0]} {key[1]:<12} {rho:.4f}  " + "  ".join(f"{v:7.3f}" for v in s) + " | " + "  ".join(f"{v:7.3f}" for v in ms)
              + f" | {d[0]:8.1f} {d[1]:9.1f} {d[2]:9.1f}")
    groups = {"writer seeds 1-4 (fr)": [k for k in res if k[0] == "W" and int(re.search(r"s(\d+)", k[1]).group(1)) <= 4],
              "writer seeds 5-12": [k for k in res if k[0] == "W" and int(re.search(r"s(\d+)", k[1]).group(1)) >= 5],
              "writer all 12": [k for k in res if k[0] == "W"], "reader 1002-1009": [k for k in res if k[0] == "O"],
              "writer 12 + reader 8": list(res)}
    for g, ks in groups.items():
        if len(ks) < 2: continue
        print(f"{g:<22} sup: " + "  ".join(stat([res[k][0][i] for k in ks]) for i in range(3)))
        print(f"{'':<22} ms : " + "  ".join(stat([res[k][1][i] for k in ks]) for i in range(3)))
    W12 = groups["writer all 12"]
    if len(W12) == 12:
        for lab, idx in (("sup[1e7]", (0, 2)), ("ms[1e7]", (1, 2))):
            vals = {k: res[k][idx[0]][idx[1]] for k in W12}; first = set(groups["writer seeds 1-4 (fr)"])
            obs = sum(1 for i in first for j in W12 if j not in first and vals[i] > vals[j])
            cnt = 0; tot = 0
            for c in itertools.combinations(W12, 4):
                u = sum(1 for i in c for j in W12 if j not in c and vals[i] > vals[j]); tot += 1; cnt += (u >= obs)
            print(f"rank test {lab}: fr seeds 1-4 beat {obs}/32 pairs; exact one-sided p = {cnt}/{tot} = {cnt / tot:.4f}")

if __name__ == "__main__" and len(sys.argv) == 1:
    main()

def at_1e9():
    """the reader's seed 1001 at X = 1e9 against the fr 1e9 seeds 1-8 and the writer's 12 seeds truncated at 1e9."""
    X = 1e9; wins = (1e4, 1e6, 1e7)
    ref = parse(FR + "data/bern_a0.75.csv"); t12 = {}
    t12.update(parse(FR + "data_big/bern_a0.75.csv"))
    for f in sorted(glob.glob(WR + "data_big/bern_a0.75_s*.csv")): t12.update(parse(f))
    mine = parse(HERE + "/data/bern_O_a0.75_s1001_1e9_dec.csv")
    def row(rho, a):
        a = a[a[:, 1] <= X]; W = ms_windows(a, rho)
        return [sup_slope(a, w, X) for w in wins], [ms_slope(W, w) for w in wins]
    print("\nX = 1e9 comparison (windows [1e4,1e9], [1e6,1e9], [1e7,1e9])")
    for name, d in (("fr seeds 1-8 at 1e9 (Y=4e9)", ref), ("writer 12 seeds truncated at 1e9", t12)):
        rs = [row(v[0], v[2]) for v in d.values()]
        print(f"{name:<34} sup: " + "  ".join(stat([r[0][i] for r in rs]) for i in range(3)))
        print(f"{'':<34} ms : " + "  ".join(stat([r[1][i] for r in rs]) for i in range(3)))
    for r, v in mine.items():
        s, ms = row(v[0], v[2])
        print(f"reader seed 1001 (numpy, PCG64)    sup: " + "  ".join(f"{x:.3f}" for x in s) + "   ms: " + "  ".join(f"{x:.3f}" for x in ms))
    dy = np.loadtxt(HERE + "/data/bern_O_a0.75_s1001_1e9_dya.csv", delimiter=",", comments="#")
    rho = float(open(HERE + "/data/bern_O_a0.75_s1001_1e9_dya.csv").readline().split("rho=")[1].split()[0])
    M = (dy[:, 4] + dy[:, 5] * rho * rho / 12) / dy[:, 5]; full = dy[:, 1] - dy[:, 0] + 1 == dy[:, 5]
    for w0 in (1e4, 1e6, 1e7):
        m = (dy[:, 0] >= w0) & full & (dy[:, 1] <= X)
        print(f"   true dyadic [2^j, 2^(j+1)) ms-slope from {w0:.0e}: {np.polyfit(np.log10(dy[m, 0]), np.log10(M[m]), 1)[0]:.3f} ({m.sum()} windows)")

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "1e9":
    at_1e9()
