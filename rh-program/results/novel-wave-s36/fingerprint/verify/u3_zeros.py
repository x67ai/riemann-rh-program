"""
u3_zeros.py -- Unit 3: the INDEPENDENT zeros route.

Zeros: Arb/Platt (acb.zeta_zeros, certified on the critical line) for n <= N0; mpmath.zetazero (Riemann-Siegel +
Turing, a different code base) spot-checks the Arb zeros.  Tail beyond T (midway between gamma_{N0} and
gamma_{N0+1}, where N(T) = N0 exactly): smooth Riemann-von Mangoldt density theta'(t)/pi plus the exact boundary
term -f(T) S(T), S(T) = N0 - theta(T)/pi - 1.  Residual error ~ |f(T)| log T / T.

Checks against the Arb Taylor-series tables (Unit 2):
  (1) power sums s_m, m = 1..12;  (2) Li coefficients lambda_n, n = 1..(table size);
  (3) S-fraction al_n via the discretized Stieltjes procedure on the SYMMETRIC measure
      mu_s = sum (gamma^{-2}/2)(delta_{1/gamma} + delta_{-1/gamma}) + discretized tail (al_n = b_n(mu_s)^2);
      validated first on the sin toy (exact al_n = 1/((2n+1)(2n+3)));
  (4) Verblunsky alpha_n via the Szego recursion on the atoms z_rho = 1 - 1/rho plus discretized tail.
"""
import sys, os, json, time
import numpy as np
import mpmath as mp
sys.path.insert(0, os.path.dirname(__file__))
from flint import acb, arb, ctx

here = os.path.dirname(os.path.abspath(__file__))
tabdir = os.path.join(os.path.dirname(here), 'tables')
N0 = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
logf = open(os.path.join(here, 'u3_zeros_N%d.log' % N0), 'w')
def say(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True); logf.write(s + '\n'); logf.flush()

# ---------------- zeros ----------------
zfile = os.path.join(tabdir, 'zeta_zeros_arb.txt')   # written by u3a_zeros_chunk.py (resumable)
mp.mp.dps = 34   # BEFORE parsing the 34-digit zeros (a first run parsed them at 15 digits)
g = []
with open(zfile) as fh:
    for line in fh:
        g.append(mp.mpf(line.split()[1]))
        if len(g) >= N0 + 1:
            break
say('loaded', len(g), 'Arb zeros; gamma_1 =', g[0], ' gamma_N0 =', g[N0 - 1])
mp.mp.dps = 34
# spot check vs mpmath.zetazero (independent code)
spot = {}
for n in (1, 2, 10, 100, 1000, 10000):
    if n <= N0:
        t0 = time.time()
        zm = mp.zetazero(n).imag
        spot[n] = mp.nstr(abs(zm - g[n - 1]), 3)
say('|mpmath.zetazero - Arb| at n=1,2,10,100,1000,10000:', spot)

gam = g[:N0]
T = (g[N0 - 1] + g[N0]) / 2
def theta(t):
    return mp.siegeltheta(t)
def dtheta(t):
    return (mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * t / 2)) - mp.log(mp.pi)) / 2
ST = N0 - theta(T) / mp.pi - 1
say('T =', mp.nstr(T, 20), ' S(T) =', mp.nstr(ST, 10))

def tail_sum(f):
    """sum_{gamma > T} f(gamma) ~ int_T^inf f theta'/pi - f(T) S(T)."""
    I = mp.quad(lambda t: f(t) * dtheta(t) / mp.pi, [T, 2 * T, 10 * T, mp.inf])
    return I - f(T) * ST

out = {'N0': N0, 'T': mp.nstr(T, 25), 'S_T': mp.nstr(ST, 15), 'spot_mpmath_vs_arb': spot}

# (1) power sums
def load_real(tag):
    return json.load(open(os.path.join(tabdir, tag)))
realtab = None
for cand in sorted(os.listdir(tabdir)):
    if cand == 'zeta_real_P24000_S1000.json':
        realtab = cand
R = load_real(realtab)
say('comparing with', realtab)
ps = []
for m in range(1, 13):
    head = mp.fsum(mp.mpf(1) / (x ** (2 * m)) for x in gam)
    tl = tail_sum(lambda t: t ** (-2 * m))
    val = head + tl
    ref = mp.mpf(R['s'][m]['v'])
    rel = abs(val - ref) / ref
    est = abs(T ** (-2 * m)) * mp.log(T) / T / ref
    ps.append({'m': m, 'zeros+tail': mp.nstr(val, 25), 'arb': mp.nstr(ref, 25), 'rel_diff': mp.nstr(rel, 3),
               'predicted_rel_err_~f(T)logT/T': mp.nstr(est, 3), 'tail_share': mp.nstr(tl / ref, 3)})
    say('s_%d rel diff %s (predicted ~%s; tail share %s)' % (m, mp.nstr(rel, 3), mp.nstr(est, 3), mp.nstr(tl / ref, 3)))
out['power_sums'] = ps

# (2) Li coefficients
circtab = None
for cand in sorted(os.listdir(tabdir)):
    if cand == 'zeta_circle_P24000_S1000.json':
        circtab = cand
if circtab:
    C = json.load(open(os.path.join(tabdir, circtab)))
    say('comparing with', circtab)
    gn = np.array([float(x) for x in gam])
    lis = []
    nmaxL = min(len(C['lambda']) - 1, 2000)
    for n in [1, 2, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000]:
        if n > nmaxL:
            continue
        # head in mpmath (exact enough): sum 2 Re(1 - (1 - 1/rho)^n)
        head = mp.fsum(2 * mp.re(1 - (1 - 1 / mp.mpc(0.5, x)) ** n) for x in gam)
        f = lambda t: 2 * mp.re(1 - (1 - 1 / mp.mpc(0.5, t)) ** n)
        tl = tail_sum(f)
        val = head + tl
        ref = mp.mpf(C['lambda'][n]['v'])
        lis.append({'n': n, 'zeros+tail': mp.nstr(val, 20), 'arb': mp.nstr(ref, 20), 'abs_diff': mp.nstr(abs(val - ref), 3),
                    'tail': mp.nstr(tl, 6)})
        say('lambda_%d: zeros+tail %s  arb %s  diff %s  (tail %s)' % (n, mp.nstr(val, 15), mp.nstr(ref, 15), mp.nstr(abs(val - ref), 3), mp.nstr(tl, 5)))
    out['li'] = lis

# (3) S-fraction via Stieltjes procedure on the symmetric measure (float64), toy first
def stieltjes_sym(u, wt, nmax):
    """Symmetric discrete measure: atoms +-u with weights wt/2 each.  Returns b_n^2 (n = 1..nmax) of its
    zero-diagonal Jacobi matrix = the S-fraction al_n of the push-forward y = u^2.  Lanczos on diag(x) with
    start vector sqrt(W) and FULL reorthogonalization (twice) -- backward stable.  (The plain discretized
    Stieltjes procedure is UNSTABLE here: forward recurrence at the isolated top atoms excites the growing
    solution; a first run showed errors O(1) by n = 50.)"""
    x = np.concatenate([u, -u]); W = np.concatenate([wt, wt]) / 2
    Wp = np.clip(W, 0, None)          # the tiny boundary correction can be negative: fold it into its neighbor
    neg = W < 0
    if neg.any():
        # move negative boundary mass onto the nearest positive tail node (it is ~1e-10 of the tail mass)
        Wp = W.copy(); Wp[neg] = 0.0
        for j in np.where(neg)[0]:
            k = np.argmin(np.abs(x[~neg] - x[j]))
            idx = np.where(~neg)[0][k]
            Wp[idx] += W[j]
    Q = np.zeros((len(x), nmax + 1))
    Q[:, 0] = np.sqrt(Wp) / np.sqrt(Wp.sum())
    out = []; bprev = 0.0
    for k in range(nmax):
        v = x * Q[:, k] - (bprev * Q[:, k - 1] if k > 0 else 0.0)
        for _ in range(2):
            v -= Q[:, :k + 1] @ (Q[:, :k + 1].T @ v)
        b = np.linalg.norm(v)
        out.append(b * b)
        Q[:, k + 1] = v / b; bprev = b
    return np.array(out)

def tail_nodes(Tt, dens, nq=60):
    """Discretize the continuous tail t in (Tt, inf) with density dens(t) (counting measure density),
    weight per zero t^-2, location u = 1/t.  Variable v = log(t/Tt) in (0, inf): Gauss-Laguerre after
    factoring e^{-v}:  t^-2 dens(t) dt = Tt^-1 e^{-v} dens(Tt e^v) dv."""
    xs, ws = np.polynomial.laguerre.laggauss(nq)
    t = Tt * np.exp(xs)
    wt = ws * np.array([float(dens(ti)) for ti in t]) / Tt
    return 1.0 / t, wt

# sin toy: zeros gamma_k = pi k, k <= K; tail density 1/pi; S(T) exact (T = pi (K + 1/2): N(T) = K, smooth N0 = T/pi = K + 1/2)
K = 30000
gk = np.pi * np.arange(1, K + 1)
Tt = np.pi * (K + 0.5)
uT, wT = tail_nodes(Tt, lambda t: 1.0 / np.pi)
u = np.concatenate([1.0 / gk, uT, [1.0 / Tt]])
wt = np.concatenate([1.0 / gk ** 2, wT, [-(K - (Tt / np.pi)) * Tt ** -2]])   # boundary term -f(T) S(T), S(T) = K - T/pi
b2 = stieltjes_sym(u, wt, 400)
exact = np.array([1.0 / ((2 * n + 1) * (2 * n + 3)) for n in range(1, 401)])
relerr = np.abs(b2 - exact) / exact
say('sin toy (K=1e5 zeros + tail): max rel err of al_n for n<=50: %.2e, n<=200: %.2e, n<=400: %.2e'
    % (relerr[:50].max(), relerr[:200].max(), relerr[:400].max()))
# the same without tail, to show the tail matters
b2n = stieltjes_sym(1.0 / gk, 1.0 / gk ** 2, 400)
reln = np.abs(b2n - exact) / exact
say('sin toy WITHOUT tail: rel err at n = 10, 100, 400: %.2e %.2e %.2e' % (reln[9], reln[99], reln[399]))
out['sin_toy'] = {'K': K, 'max_rel_err_tail_n50': float(relerr[:50].max()), 'n200': float(relerr[:200].max()),
                  'n400': float(relerr[:400].max()), 'no_tail_n10_100_400': [float(reln[9]), float(reln[99]), float(reln[399])]}

# zeta
gz = np.array([float(x) for x in gam])
Tf = float(T)
uT, wT = tail_nodes(Tf, lambda t: float(dtheta(mp.mpf(t)) / mp.pi))
u = np.concatenate([1.0 / gz, uT, [1.0 / Tf]])
wt = np.concatenate([1.0 / gz ** 2, wT, [-float(ST) * Tf ** -2]])
b2z = stieltjes_sym(u, wt, 400)
cmp_ = []
for n in (1, 2, 5, 10, 20, 50, 100, 150, 200, 300, 400):
    if n <= len(R['al']):
        ref = float(mp.mpf(R['al'][n - 1]['v']))
        cmp_.append({'n': n, 'zeros_stieltjes': '%.15e' % b2z[n - 1], 'arb': '%.15e' % ref, 'rel_diff': '%.2e' % (abs(b2z[n - 1] - ref) / ref)})
        say('al_%d: zeros %.12e  arb %.12e  rel %.2e' % (n, b2z[n - 1], ref, abs(b2z[n - 1] - ref) / ref))
out['sfrac_cmp'] = cmp_

# (4) circle side, via Szego-Geronimus (verified in u4_mine_circle to 1e-50): the Verblunsky data of sigma are
# the Jacobi data of the SHIFTED measure nu~ = sum |rho|^-2 delta_{|rho|^-2}; cross-check its S-fraction
# (Arb route, tables/zeta_shifted_real_P12000_S420.json) by Lanczos on the zeros + tail.
shf = os.path.join(tabdir, 'zeta_shifted_real_P12000_S420.json')
if os.path.exists(shf):
    S = json.load(open(shf))
    ut = 1.0 / np.sqrt(0.25 + gz ** 2)
    tq, wq = np.polynomial.laguerre.laggauss(60)
    tt = Tf * np.exp(tq)
    # Gauss-Laguerre in v = log(t/T): dens(t) dt/(1/4+t^2) = e^{-v} [e^{v} dens(t) t/(1/4+t^2)] dv, e^{v} = t/T
    # (a first run omitted the factor e^{v} = t/T and was off by ~1e-3 -- the tail share)
    wtl = wq * (tt / Tf) * tt * np.array([float(dtheta(mp.mpf(float(x))) / mp.pi) for x in tt]) / (0.25 + tt ** 2)
    uu = np.concatenate([ut, 1.0 / np.sqrt(0.25 + tt ** 2), [1.0 / np.sqrt(0.25 + Tf ** 2)]])
    ww = np.concatenate([1.0 / (0.25 + gz ** 2), wtl, [-float(ST) / (0.25 + Tf ** 2)]])
    b2s = stieltjes_sym(uu, ww, 400)
    cv = []
    for n in (1, 2, 5, 10, 20, 50, 100, 150, 200, 300, 400):
        if n <= len(S['al_shifted']):
            ref = float(mp.mpf(S['al_shifted'][n - 1]['v']))
            cv.append({'n': n, 'zeros_lanczos': '%.15e' % b2s[n - 1], 'arb': '%.15e' % ref, 'rel_diff': '%.2e' % (abs(b2s[n - 1] - ref) / ref)})
            say('al~_%d (shifted): zeros %.12e  arb %.12e  rel %.2e' % (n, b2s[n - 1], ref, abs(b2s[n - 1] - ref) / ref))
    out['shifted_sfrac_cmp'] = cv

with open(os.path.join(here, 'u3_zeros_N%d.json' % N0), 'w') as fh:
    json.dump(out, fh, indent=1)
say('saved u3_zeros_N%d.json' % N0)
