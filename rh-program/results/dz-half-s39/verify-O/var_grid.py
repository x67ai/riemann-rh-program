# read-O independent re-run, NOTE section 3.1/3.2: one-scale conditional variance on DZ's grid.
# Written from the NOTE's definitions and the book's (17.13); nothing taken from verify/.
# Method: cell integrals p_k = F_R(v_k) - F_R(v_k - h) from the closed form
#   F_R(v) = sum_{n>=1} t^n/(n n!),  t = log v   (antiderivative of (1-1/v)/log v, F_R(1) = 0),
# evaluated as a difference without cancellation: t_b^n - t_a^n = d * S_n, d = log1p(h/a).
# Continuum integral by mpmath (30 digits), split at the jump of n0(x/v).
# For x <= 22 the block lies below e^4, where f_C = f_R (book l. 12888-12890), so one template serves both.
import numpy as np, mpmath as mp, sys

def cell_int(a, b):
    ta = np.log(a); tb = np.log(b); d = np.log1p((b - a) / a)
    S = np.ones_like(a); tap = np.ones_like(a); tot = S.copy(); fact = 1.0
    for n in range(2, 70):
        tap = tap * ta; S = tb * S + tap; fact *= n
        tot = tot + S / (n * fact)
    return d * tot

def block_cells(x):
    vs, hs = [], []
    for n in range(int(np.floor(x / 2)), int(np.ceil(x))):
        l = np.arange(1, 2**n + 1, dtype=np.float64)
        v = n + l / 2.0**n
        m = (v > x / 2) & (v <= x)
        vs.append(v[m]); hs.append(np.full(m.sum(), 2.0**-n))
    return np.concatenate(vs), np.concatenate(hs)

def n0(y, N0):
    return 1.0 + (N0 == 1) * (y >= 1.5)

def grid_var(x, kap, N0, v, h):
    p = cell_int(v - h, v)
    a = -np.log1p(-1.0 / v)
    c = n0(x / v, N0) - kap * x * a
    return float(np.sum(p * (1 - p) * c * c)), float(p.max()), len(v)

def cont_var(x, kap, N0):
    mp.mp.dps = 30
    X = mp.mpf(x); K = mp.mpf(kap)
    f = lambda w: (1 - 1 / w) / mp.log(w)
    def integrand(w, n0v):
        return f(w) * (n0v + K * X * mp.log(1 - 1 / w))**2
    if N0 == 0:
        return float(mp.quad(lambda w: integrand(w, 1), [X / 2, X]))
    # n0(x/v) = 2 for x/v >= 1.5, i.e. v <= 2x/3
    return float(mp.quad(lambda w: integrand(w, 2), [X / 2, 2 * X / 3]) +
                 mp.quad(lambda w: integrand(w, 1), [2 * X / 3, X]))

def I_closed(kap, N0):
    if N0 == 0:
        return 0.5 - 2 * kap * np.log(2) + kap**2
    return 1 - (2 * np.log(1.5) + 4 * np.log(4 / 3)) * kap + kap**2

if __name__ == "__main__":
    xs = [int(a) for a in sys.argv[1:]] or [6, 8, 10, 12, 14, 16, 18, 20, 22]
    for x in xs:
        v, h = block_cells(x)
        for kap in (0.7, 1.0, 2.4):
            for N0 in (0, 1):
                g, pmax, npts = grid_var(x, kap, N0, v, h)
                c = cont_var(x, kap, N0)
                asym = x / np.log(x) * I_closed(kap, N0)
                print(f"x={x:2d} kappa={kap:.1f} N0={N0} cells={npts:8d} grid={g:.10g} cont={c:.10g} "
                      f"rel={(g - c) / c:+.3e} asym={asym:.5g} pmax={pmax:.3g}", flush=True)
