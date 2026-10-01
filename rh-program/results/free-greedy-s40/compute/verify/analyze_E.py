# analyze_E.py TAG RHO [THETA] -- the law of E for one generator run.
# Reads verify/logs/TAG.log (S, F rows) and /private/tmp/rh-s40-free-greedy/TAG.hist (cumulative time-weighted
# histograms of E, cells 1/16 on [-1, 511), one record per half-decade sample).  Prints:
#  (1) per half-decade window: quantiles of E (time-weighted), window max, tail rate vs the queue value 2/(rho log x);
#  (2) fits of sup E on [1e3, X]: c log^2 x, c log^k x, C x^b (log-space least squares), residuals, local slopes.
import sys, math, warnings, numpy as np
warnings.filterwarnings("ignore")
V = __file__.rsplit("/", 1)[0]
tag, rho = sys.argv[1], float(eval(sys.argv[2], {"pi": math.pi, "e": math.e, "sqrt": math.sqrt}))
S, F = [], []
for ln in open(f"{V}/logs/{tag}.log"):
    p = ln.split()
    if not p: continue
    if p[0] == "S": S.append([float(v) for v in p[1:]])
    elif p[0] == "F": F.append([float(v) for v in p[1:]])
S, F = np.array(S), np.array(F)
H = np.fromfile(f"/private/tmp/rh-s40-free-greedy/{tag}.hist", dtype=np.float64).reshape(-1, 8193)
hx, hm = H[:, 0], H[:, 1:]
edges = -1.0 + np.arange(8193) / 16.0
print(f"# analyze_E {tag} rho={rho:.12f}")
print("# (1) windows (x_{j-1}, x_j]: time-weighted quantiles of E; tail fit log P(E>y) = a - lam*y on 1e-1 > P > 1e-4")
print("#  x_j        meanE   q50    q90    q99    q99.9  maxE_win(*)  lam_fit  lam_queue=2/(rho log xc)  ratio")
prev = np.zeros(8192); xprev = 1.0
for k in range(len(hx)):
    m = hm[k] - prev; prev = hm[k].copy()
    tot = m.sum()
    if tot <= 0: xprev = hx[k]; continue
    cdf = np.cumsum(m) / tot
    def q(a):
        j = int(np.searchsorted(cdf, a)); j = min(j, 8191)
        c0 = cdf[j - 1] if j > 0 else 0.0
        return edges[j] + (a - c0) / max(cdf[j] - c0, 1e-300) / 16.0
    mean = float((m * (edges[:-1] + 1 / 32)).sum() / tot)
    nz = np.nonzero(m > 1.0)[0]; emax = edges[nz[-1] + 1] if len(nz) else float("nan")   # level held >= 1 time unit
    if S.shape[1] >= 27:
        r = np.nonzero(np.isclose(S[:, 0], hx[k], rtol=1e-9))[0]
        if len(r): emax = S[r[0], 26]                                                    # exact window max (wMaxE)
    surv = 1.0 - cdf  # P(E > right edge of cell)
    sel = (surv < 1e-1) & (surv > 1e-4)
    lam = float("nan")
    if sel.sum() >= 8:
        A = np.vstack([np.ones(sel.sum()), edges[1:][sel]]).T
        coef = np.linalg.lstsq(A, np.log(surv[sel]), rcond=None)[0]; lam = -coef[1]
    xc = math.sqrt(xprev * hx[k]) if xprev > 1 else hx[k]
    lq = 2.0 / (rho * math.log(xc))
    print(f"{hx[k]:10.3e} {mean:7.3f} {q(.5):6.2f} {q(.9):6.2f} {q(.99):6.2f} {q(.999):6.2f} {emax:8.2f} {lam:8.4f} {lq:10.4f} {lam / lq:12.3f}")
    xprev = hx[k]
print("# (*) maxE_win: exact window maximum of E when the log carries it (wMaxE column), else the highest level E held for >= 1 unit of time")
print("# (2) sup E growth (running sup at 100 points per decade, x >= 1e3)")
x, sE = F[:, 0], F[:, 5]
sel = x >= 1e3; x, sE = x[sel], sE[sel]
L, Y = np.log(x), np.log(sE)
def fit(cols, name):
    A = np.vstack(cols).T; c, *_ = np.linalg.lstsq(A, Y, rcond=None); r = Y - A @ c
    print(f"  {name:28s} params {np.array2string(c, precision=4)}  rms(log resid) {math.sqrt((r * r).mean()):.4f}  max|resid| {abs(r).max():.4f}  resid at X {r[-1]:+.4f}")
    return c
A2 = Y - 2 * np.log(L); a2 = A2.mean(); r2 = A2 - a2
print(f"  {'c log^2 x':28s} c = {math.exp(a2):.4f}  rms(log resid) {math.sqrt((r2 * r2).mean()):.4f}  max|resid| {abs(r2).max():.4f}  resid at X {r2[-1]:+.4f}")
ck = fit([np.ones_like(L), np.log(L)], "c log^k x  [log c, k]")
cb = fit([np.ones_like(L), L], "C x^b      [log C, b]")
print("#  local slopes d log supE / d log x per decade (running sup):")
for d in range(3, int(math.log10(x[-1])) + 1):
    a, b = 10.0 ** (d - 1), 10.0 ** d
    ia, ib = np.argmin(abs(x - a)), np.argmin(abs(x - b))
    if ia != ib and abs(x[ia] / a - 1) < 0.03 and abs(x[ib] / b - 1) < 0.03:
        print(f"  [{a:8.0e},{b:8.0e}]  supE {sE[ia]:8.3f} -> {sE[ib]:8.3f}  slope {math.log(sE[ib] / sE[ia]) / math.log(10):+.3f}   supE/log^2 x at b: {sE[ib] / math.log(b) ** 2:.4f}")
