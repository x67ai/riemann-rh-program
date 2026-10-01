#!/usr/bin/env python3
"""read-O analysis of sq = {nextprime(p^2)} from the own sieve (o_sieve_bins.c), exact in high precision.
(1) per-bin exact sum (N(n) - rho(n+1/2))^2 from integer sums, compared with the unit's CSV (sumE2, maxE, minE, count);
(2) dyadic M(X) on windows of 6 bins from 10^4 (cO 3.1), slopes (OLS log10 M vs log10 X, X = window lower edge) for X >= 10^k
    and 'top3' (X >= xmax/1e3/1.9999), running-sup slope; (3) M_diag = rho^2 W/12 with W = sum_{b in <R>, b <= Xe-1} prod (p+1)/(p-1)
    by own DFS; kappa from log(M/M_diag) = a - kappa log ln X (X >= 1e6); (4) explicit formula over the first Z zeros:
    E(x) ~ 2 Re sum c_rho x^{rho/2}, c_rho = zeta(rho/2) C(rho/2)/(rho zeta'(rho)); bin means vs exact bin averages, both / x^{1/4}."""
import sys, re, math, numpy as np, mpmath as mp
mp.mp.dps = 50
fam = sys.argv[1]; tag = sys.argv[2]; Z = int(sys.argv[3]) if len(sys.argv) > 3 else 0
ucsv = f"../verify/data/{fam}2_{tag}.csv"
T = "/private/tmp/rh-s40-lemmaG/"
rho_me = mp.mpf(open(T + f"rho_{fam}_1e10.txt").readline().strip())
rho_unit = mp.mpf(re.search(r"rho=([0-9.]+)", open(ucsv).readline()).group(1))
rows = [l.split("\t") for l in open(T + f"{fam}_{tag}_bins.tsv")]
lo = [int(r[0]) for r in rows]; hi = [int(r[1]) for r in rows]; cnt = [int(r[2]) for r in rows]
S1 = [int(r[3]) for r in rows]; S2 = [int(r[4]) for r in rows]; SN = [int(r[5]) for r in rows]
mx = [float(r[6]) for r in rows]; mn = [float(r[7]) for r in rows]
def sq_sum(a, b):          # sum_{n=a}^{b} (n+1/2)^2 = sum n^2 + sum n + cnt/4, exact rational
    f2 = lambda m: m * (m + 1) * (2 * m + 1) // 6; f1 = lambda m: m * (m + 1) // 2
    return mp.mpf(f2(b) - f2(a - 1) + f1(b) - f1(a - 1)) + mp.mpf(b - a + 1) / 4
def s2(rho): return [mp.mpf(S2[i]) - rho * SN[i] + rho ** 2 * sq_sum(lo[i], hi[i]) for i in range(len(lo))]
s2_me, s2_unit = s2(rho_me), s2(rho_unit)
unit = [l.strip().split(",") for l in open(ucsv) if not l.startswith("#")]
assert [int(u[1]) for u in unit] == lo and [int(u[2]) for u in unit] == hi
d_cnt = max(abs(int(u[6]) - cnt[i]) for i, u in enumerate(unit))
rel = [abs(float(s2_unit[i]) / float(u[5]) - 1) for i, u in enumerate(unit) if float(u[5]) > 0]
rel_me = [abs(float(s2_me[i]) / float(u[5]) - 1) for i, u in enumerate(unit) if float(u[5]) > 0]
dmx = max(abs(mx[i] - float(u[3])) for i, u in enumerate(unit)); dmn = max(abs(mn[i] - float(u[4])) for i, u in enumerate(unit))
print(f"[{tag}] bins={len(lo)} N(X)={S1[-1] if cnt[-1] == 1 else 'n/a'}  rho_me - rho_unit = {mp.nstr(rho_me - rho_unit, 5)}")
print(f"  count diffs: max {d_cnt};  sumE2 rel. diff vs unit CSV (7 sig. digits printed): with unit rho max {max(rel):.2e}, "
      f"with own rho max {max(rel_me):.2e};  |maxE diff| <= {dmx:.2e}, |minE diff| <= {dmn:.2e} (own rho; Δrho*X = "
      f"{float((rho_me - rho_unit) * hi[-1]):.2e})")
for rho, s2v, name in ((rho_unit, s2_unit, "unit rho"), (rho_me, s2_me, "own rho")):
    k0 = lo.index(10000); X, Xe, M = [], [], []
    k = k0
    while k + 6 <= len(lo):
        c = sum(cnt[k:k + 6]); X.append(lo[k]); Xe.append(hi[k + 5] + 1)
        M.append(float((sum(s2v[k:k + 6]) + c * rho ** 2 / 12) / c)); k += 6
    X, Xe, M = np.array(X, float), np.array(Xe, float), np.array(M)
    def slope(x, y, a=None):
        m = (x >= a) if a else np.ones(len(x), bool)
        return float(np.polyfit(np.log10(x[m]), np.log10(y[m]), 1)[0])
    A = np.maximum.accumulate(np.maximum(np.array(mx), -np.array(mn))); H = np.array(hi, float)
    sup = float(np.polyfit(np.log10(H[H >= 1e4]), np.log10(A[H >= 1e4]), 1)[0])
    print(f"  ({name}) ms-slope [1e4,X] {slope(X, M, 1e4):.3f} [1e5,X] {slope(X, M, 1e5):.3f} [1e6,X] {slope(X, M, 1e6):.3f} "
          f"[1e7,X] {slope(X, M, 1e7):.3f} top3 {slope(X, M, Xe.max() / 1e3 / 1.9999):.3f}; sup-slope [1e4,X] {sup:.3f}")
print("  M(X) windows:", ", ".join(f"{x:.3g}:{m:.6g}" for x, m in zip(X, M)))
# W(X) by DFS over squarefree R-numbers <= max Xe
R = sorted(int(l) for l in open(T + f"R_{fam}_1e10.txt") if int(l) <= Xe.max())
Y = int(Xe.max()); bs, ws = [], []
sys.setrecursionlimit(100000)
def dfs(i0, b, w):
    bs.append(b); ws.append(w)
    for i in range(i0, len(R)):
        p = R[i]
        if b * p > Y: break
        dfs(i + 1, b * p, w * (p + 1) / (p - 1))
dfs(0, 1, 1.0)
order = np.argsort(bs); bsa = np.array(bs, float)[order]; cw = np.cumsum(np.array(ws)[order])
W = cw[np.searchsorted(bsa, Xe - 1, side="right") - 1]; Md = float(rho_me) ** 2 * W / 12; ratio = M / Md
m6 = X >= 1e6
kap = np.linalg.lstsq(np.c_[np.ones(m6.sum()), -np.log(np.log(X[m6]))], np.log(ratio[m6]), rcond=None)[0][1]
print(f"  #<R> <= {Y}: {len(bs)};  M/M_diag at window X: " + ", ".join(f"{x:.2g}:{r:.3g}" for x, r in zip(X, ratio))
      + f";  kappa (X>=1e6, X = lower edge) = {kap:.2f}")
if Z:
    mp.mp.dps = 20
    zs = [mp.zetazero(j) for j in range(1, Z + 1)]
    ps = np.array([math.isqrt(r) for r in R if r <= 10 ** 10], float); rs = np.array([r for r in R if r <= 10 ** 10], float)
    cs = []
    for z in zs:
        s = complex(z) / 2
        logC = np.sum(np.log1p(-np.exp(-s * np.log(rs))) - np.log1p(-np.exp(-2 * s * np.log(ps))))
        cs.append(complex(mp.zeta(z / 2)) * np.exp(logC) / (complex(z) * complex(mp.zeta(z, derivative=1))))
    print("  |c_rho| for rho_1, rho_2, rho_5:", ", ".join(f"{abs(cs[j]):.4f}" for j in (0, 1, 4)))
    x1 = np.array(lo, float); x2 = np.array(hi, float) + 1; L = x2 - x1; xc = np.sqrt(x1 * x2)
    Emean = np.array([float((S1[i] - rho_me * (mp.mpf(lo[i] + hi[i] + 1) * cnt[i] / 2)) / cnt[i]) for i in range(len(lo))])
    pred = np.zeros(len(lo))
    for z, c in zip(zs, cs):
        w = complex(z) / 2 + 1
        pred += 2 * np.real(c * (np.exp(w * np.log(x2)) - np.exp(w * np.log(x1))) / (w * L))
    for a in (1e4, 1e6, 1e8):
        m = (x1 >= a) & (L > 1)
        u, v = Emean[m] / xc[m] ** 0.25, pred[m] / xc[m] ** 0.25
        print(f"  explicit formula ({Z} zeros), bins x >= {a:.0e} (n={m.sum()}): corr {np.corrcoef(u, v)[0, 1]:.4f}, "
              f"resid rms {np.sqrt(np.mean((u - v) ** 2)):.4f}, signal rms {np.sqrt(np.mean(u ** 2)):.4f}")
