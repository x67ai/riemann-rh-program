# read-O independent simulation of the Diamond-Zhang construction (book Thm 17.11 / 17.14, grid (17.13)).
# Own code, written from the book's definitions; nothing imported or copied from verify/.
# Selection: units n <= 20 every cell drawn (closed-form cell integrals); 21 <= n <= 52 exact independent Bernoulli by
# geometric skipping on the true grid + acceptance p_k/p_max; v >= 53 (grid finer than double) Poisson with intensity f.
# Density: log rho = sum_{p<=Y} -log(1-1/p) - int_1^Y f/v + log r_T + Gaussian tail beyond Y (Y = 1e9 by default).
import numpy as np, math
from scipy.special import exp1, comb
from scipy.integrate import quad
from var_grid import cell_int            # closed-form f_R cell integrals (own, verify-O)

E4 = math.exp(4.0); G1 = math.exp(4.0); G2 = math.exp(16.0)
C_ENV = 2 * 0.410616 / (1 - math.exp(-4)) + 1e-9    # c of (17.45), book l. 12814/12892

def fR(v):
    return (1 - 1 / v) / np.log(v)

def IH(n, y):                      # Irwin-Hall density of a sum of n U(0,1), y array
    y = np.asarray(y, float); out = np.zeros_like(y); m = (y > 0) & (y < n)
    for j in range(n + 1):
        t = y - j; out = out + np.where(m & (t > 0), (-1)**j * comb(n, j) * np.where(t > 0, t, 0)**(n - 1), 0.0)
    return out / math.factorial(n - 1)

def g_log(U):                       # g(e^U) = sum_n IH_n(U - n)/n  (17.30), multiplicative conv. = additive in U
    U = np.asarray(U, float); out = np.zeros_like(U)
    nmax = int(np.floor(U.max())) + 1 if U.size else 1
    for n in range(1, min(nmax, 40) + 1):
        out = out + IH(n, U - n) / n
    return out

def fC(v):
    v = np.asarray(v, float); t = np.log(v); out = fR(v)
    for k, gam in ((1, G1), (2, G2)):
        L = 4.0**k; U = t / L
        m = U >= 1
        if m.any():
            out = out - np.where(m, 2 * g_log(np.where(m, U, 0)) / L * np.exp(-U) * np.cos(gam * t), 0.0)
    return out

def Gfun(z):
    return 1 - (np.exp(-z) - np.exp(-2 * z)) / z

def log_rT():
    s = 0.0
    for k in (1, 2, 3):
        L = 4.0**k; rho_k = complex(1 - 1 / L, math.exp(L))
        s += 2 * math.log(abs(Gfun(L * (1 - rho_k))))
    return s

def osc_integral(T):                # int_1^{e^T} (f_R - f_C)/v dv = 2 sum_k int a_k(t) cos(gamma_k t) dt
    tot = 0.0
    for k, gam in ((1, G1), (2, G2)):
        L = 4.0**k; lo = L
        if T <= lo: continue
        a = lambda t: float(g_log(np.array([t / L]))[0]) / L * math.exp(-t / L)
        knots = [lo] + [L * j for j in range(2, 40) if L * j < T] + [T]
        for u, w in zip(knots[:-1], knots[1:]):          # g is a polynomial in t between knots
            tot += 2 * quad(a, u, w, weight='cos', wvar=gam, limit=2000, epsabs=1e-15, epsrel=1e-12)[0]
    return tot

def Ein(t):
    return np.euler_gamma + math.log(t) + exp1(t)

def gen(template, seed, X=1e7, Y=1e9, chunk=4_000_000):
    rng = np.random.Generator(np.random.Philox(seed))
    keep = []; logsum = 0.0; viol = 0; ncand = 0
    for n in range(1, 21):                                   # every cell
        l = np.arange(1, 2**n + 1, dtype=np.float64); v = n + l / 2.0**n; h = 2.0**-n
        p = cell_int(v - h, v); sel = v[rng.random(v.size) < p]
        keep.append(sel)
    for n in range(21, 53):                                  # geometric skipping, exact Bernoulli(p_k)
        M = 2**n; h = 2.0**-n; pmax = float(fR(np.array([float(n)]))[0]) * h * (1 + 1e-9)
        pos = 0; cand = []
        while True:
            pos += int(rng.geometric(pmax))
            if pos > M: break
            cand.append(pos)
        if cand:
            l = np.array(cand, dtype=np.float64); v = n + l / 2.0**n
            p = cell_int(v - h, v) if n < 30 else h * fR(v)   # below double resolution: midpoint value
            acc = rng.random(v.size) < p / pmax
            keep.append(v[acc])
    a = 53.0
    while a < Y:                                             # Poisson with intensity f, thinning
        env = (1 + (C_ENV if template == 'C' else 0)) * float(fR(np.array([a]))[0])
        b = min(Y, a * 1.05, a + chunk / env)
        k = rng.poisson(env * (b - a)); v = a + (b - a) * rng.random(k); ncand += k
        fv = fC(v) if template == 'C' else fR(v)
        viol += int(np.sum((fv > env) | (fv < 0)))
        v = np.sort(v[rng.random(k) * env < fv])
        logsum += float(np.sum(-np.log1p(-1 / v)))
        if a < X: keep.append(v[v <= X])
        a = b
    P = np.concatenate(keep); P.sort()
    small = P[P < 53]; logsum += float(np.sum(-np.log1p(-1 / small)))
    T = math.log(Y)
    lr = logsum - Ein(T)
    if template == 'C':
        lr += osc_integral(T) + log_rT()
    tail = rng.normal(1 / (2 * Y * T), math.sqrt(1 / (Y * T)))
    return P, lr + tail, dict(viol=viol, ncand=int(ncand), tail=tail, logsum=logsum)
