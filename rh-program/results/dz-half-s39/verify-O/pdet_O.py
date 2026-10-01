# read-O check of NOTE section 4.3 (P_det: j-th g-prime = first grid point with F_R >= j), own code.
# F_R(v) = sum t^n/(n n!), t = log v (closed form); q*_j = F_R^{-1}(j) by Newton; grid rounding for q* < 53.
# rho_det and H(1/2) with midpoint-rule tails in the quantile variable u = F_R(v); E/s at octave edges up to 1e7.
import math, subprocess, json, numpy as np
from scipy.special import exp1, shichi
from scipy.integrate import quad

def FR(v):
    t = np.log(v); term = np.ones_like(t); s = np.zeros_like(t)
    for n in range(1, 140):
        term = term * t / n            # t^n/n!
        s = s + term / n
    return s
fR = lambda v: (1 - 1 / v) / np.log(v)

def quantiles(J):
    j = np.arange(1, J + 1, dtype=float)
    tab_v = np.exp(np.linspace(1e-6, math.log(2e7), 400001)); tab_F = FR(tab_v)
    v = np.interp(j, tab_F, tab_v)
    for _ in range(6):
        v = v - (FR(v) - j) / fR(v)
    return v

def to_grid(q):
    out = q.copy(); m = q < 53
    n = np.floor(q[m]); l = np.ceil((q[m] - n) * 2.0**n)
    out[m] = n + l / 2.0**n
    return out

X = 1e7; TMP = "/private/tmp/rh-s40-dz-half-s39"
J0 = int(FR(np.array([X]))[0]) + 2
qs = quantiles(J0); q = to_grid(qs); q = q[q <= X]; J = len(q)
assert np.all(FR(q) >= np.arange(1, J + 1) - 1e-7)
phi = -np.log1p(-1 / q)
FX = float(FR(np.array([X]))[0]); T = math.log(X)
Ein = np.euler_gamma + math.log(T) + exp1(T)
v_half = float(quantiles(J + 1)[-1]) if False else None
# tail T(X) = int_X^inf (phi - 1/v) f dv - phi(X) (J + 1/2 - F(X))
tail = quad(lambda v: (-math.log1p(-1 / v) - 1 / v) * (1 - 1 / v) / math.log(v), X, np.inf, limit=200)[0] \
       - (-math.log1p(-1 / X)) * (J + 0.5 - FX)
log_rho = float(np.sum(phi)) - Ein + tail; rho = math.exp(log_rho)
# H(1/2) = -exp(B(1/2) + B(1)/2 + sum_q [-log(1 - q^-1/2) - q^-1/2 - 1/(2q)])
B1 = float(np.sum(1 / q)) - Ein + (quad(lambda v: 0.0, X, X + 1)[0]) - (1 / X) * (J + 0.5 - FX)
shi = shichi(T / 2)[0]
Bh = float(np.sum(q**-0.5)) - 2 * shi - X**-0.5 * (J + 0.5 - FX)
r = float(np.sum(-np.log1p(-q**-0.5) - q**-0.5 - 0.5 / q))
r += quad(lambda v: (-math.log1p(-v**-0.5) - v**-0.5 - 0.5 / v) * (1 - 1 / v) / math.log(v), X, np.inf, limit=200)[0]
H = -math.exp(Bh + 0.5 * B1 + r); pred = math.sqrt(2 / math.pi) * H
pf = f"{TMP}/pdet.f64"; q.astype(np.float64).tofile(pf)
print(subprocess.run(["./gcount", "bins", pf, "%g" % X, "2048", "data/pdet.i64"], capture_output=True, text=True).stdout.strip())
c = np.fromfile("data/pdet.i64", dtype=np.int64); N = np.cumsum(c); e = 2.0 ** ((np.arange(len(c)) + 1) / 2048)
E = N - rho * e; s = np.sqrt(e / np.log(e))
res = dict(J=J, rho=rho, log_rho=log_rho, B_half=Bh, B1=B1, H_half=H, pred=pred, first_primes=[float(a) for a in q[:6]])
for j in (16, 18, 20, 21, 22):
    sl = slice(j * 2048, (j + 1) * 2048); res[f"mean_E_over_s_oct{j}"] = float(np.mean(E[sl] / s[sl]))
print(json.dumps(res, indent=1)); json.dump(res, open("data/pdet_O.json", "w"), indent=1)
