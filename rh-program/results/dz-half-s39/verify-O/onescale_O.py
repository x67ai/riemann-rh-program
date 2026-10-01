# read-O one-scale checks on own realized systems (NOTE Lemma 2.1, Lemma 2.2/section 3.3), own code.
# (a) identity N(x) - N^c(x) = #B + [1.5 in P] * #{q in B : 1.5 q <= x}, both sides by separate enumerations (gcount count);
# (b) block resampled (Poisson with intensity f on (x/2, x]) with the EXACT coupling E' = N^c + sum n0(x/q') - rho^c x e^{S'};
#     Var(E')/sigma2_cont, skew, excess kurtosis, KS p, z of the realized E(x).
import sys, json, math, subprocess, numpy as np
from scipy.integrate import quad
from scipy import stats
from dzsim import fR, fC, C_ENV
TMP = "/private/tmp/rh-s40-dz-half-s39"

def count(pf, x, lo, hi):
    return int(subprocess.run(["./gcount", "count", pf, repr(x), repr(lo), repr(hi)], capture_output=True, text=True).stdout)

def run(tag, m, R, seed=7):
    meta = json.load(open(f"data/dz_{tag}.json")); rho = meta["rho"]; h15 = meta["has15"]; tpl = meta["template"]
    pf = f"{TMP}/dz_{tag}.f64"; P = np.fromfile(pf); x = 2.0**m
    f = (lambda v: fC(np.array([v]))[0]) if tpl == "C" else (lambda v: (1 - 1 / v) / math.log(v))
    Nx = count(pf, x, 0.0, 0.0); Nc = count(pf, x, x / 2, x)
    Q = P[(P > x / 2) & (P <= x)]
    rhs = len(Q) + (int(np.sum(Q * 1.5 <= x)) if h15 else 0)
    rhoc = rho * float(np.prod(1 - 1 / Q)); E = Nx - rho * x
    a = lambda v: -math.log1p(-1 / v)
    n0 = lambda y: 1 + (1 if (h15 and y >= 1.5) else 0)
    pts = [x / 2, 2 * x / 3, x] if h15 else [x / 2, x]
    lim = 4000
    mu = sum(quad(lambda v: f(v) * a(v), u, w, limit=lim)[0] for u, w in zip(pts[:-1], pts[1:]))
    kap = rhoc * math.exp(mu)
    s2 = sum(quad(lambda v: f(v) * (n0(x / v) - kap * x * a(v))**2, u, w, limit=lim)[0] for u, w in zip(pts[:-1], pts[1:]))
    I = (1 - (2 * math.log(1.5) + 4 * math.log(4 / 3)) * kap + kap**2) if h15 else (0.5 - 2 * kap * math.log(2) + kap**2)
    rng = np.random.Generator(np.random.Philox(seed + 100 * m + 7919 * sum(map(ord, tag))))
    env = (1 + (C_ENV if tpl == "C" else 0)) * (1 - 2 / x) / math.log(x / 2)
    Ep = np.empty(R)
    for r in range(R):
        k = rng.poisson(env * x / 2); v = x / 2 + (x / 2) * rng.random(k)
        fv = fC(v) if tpl == "C" else fR(v); q = v[rng.random(k) * env < fv]
        S = float(np.sum(-np.log1p(-1 / q)))
        n0s = len(q) + (int(np.sum(q * 1.5 <= x)) if h15 else 0)
        Ep[r] = Nc + n0s - rhoc * x * math.exp(S)
    sd = Ep.std(ddof=1); zs = (Ep - Ep.mean()) / sd
    return dict(tag=tag, m=m, has15=h15, nblock=len(Q), identity_resid=(Nx - Nc) - rhs, kappa=kap,
                s2cont_norm=s2 / (x / math.log(x)), I=I, var_ratio=sd**2 / s2, skew=float(stats.skew(Ep)),
                exkurt=float(stats.kurtosis(Ep)), ks_p=float(stats.kstest(zs, "norm").pvalue),
                z_real=(E - Ep.mean()) / sd, R=R)

if __name__ == "__main__":
    for tag in sys.argv[1:]:
        for m, R in ((14, 2000), (17, 2000), (20, 1000), (23, 300)):
            d = run(tag, m, R)
            print(json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in d.items()}), flush=True)
