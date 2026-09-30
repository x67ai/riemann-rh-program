"""
u4b_primes.py -- does the prime side show up in the Jacobi fingerprint, and how?

Model: 'smooth zeta' zero set t_k with N0(t_k) = k - 1/2, N0(t) = theta(t)/pi + 1 (theta = Riemann-Siegel theta),
i.e. the zeros zeta would have if S(t) were a pure sawtooth.  al_n(model) by Lanczos (full reorth) on +-1/t_k,
k <= K, plus the smooth tail; al_n(zeta) from the certified Arb table.  Residual r_n = al_n(zeta)/al_n(model) - 1.
Question: does r_n, as a function of the WKB height t_n = 1/(2 sqrt al_n), carry lines at omega = log p (the explicit
formula's frequencies)?  Compare with the periodogram of the zero displacements d_k = gamma_k - t_k.
Threads pinned to 1 (charter: one core per agent).
"""
import os
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['OPENBLAS_NUM_THREADS'] = '1'
import sys, json, time
import numpy as np
import mpmath as mp
here = os.path.dirname(os.path.abspath(__file__)); tab = os.path.join(os.path.dirname(here), 'tables')
logf = open(os.path.join(here, 'u4b_primes.log'), 'w')
def say(*a):
    t = ' '.join(str(x) for x in a); print(t, flush=True); logf.write(t + '\n'); logf.flush()
mp.mp.dps = 30
K = 8000          # model zeros (t_K ~ 8000); run 1 used 2600 and broke down (see u4b_primes_run1_broken.log)
NMAX = 1000
# ---- model zeros
def theta(t): return mp.siegeltheta(t)
tk = []
t = mp.mpf(13)
for k in range(1, K + 2):
    target = mp.pi * (k - mp.mpf(3) / 2)
    t = mp.findroot(lambda x: theta(x) - target, t + (0 if k == 1 else 0.5))
    tk.append(t)
tk = np.array([float(x) for x in tk])
say('model zeros: t_1..t_5 =', tk[:5], ' t_K =', tk[K - 1])
# ---- zeta zeros (Arb file)
g = []
with open(os.path.join(tab, 'zeta_zeros_arb.txt')) as fh:
    for line in fh:
        g.append(float(line.split()[1]))
        if len(g) >= K + 1:
            break
g = np.array(g)
say('zeta zeros: gamma_1..5 =', g[:5], ' gamma_K =', g[K - 1])

def dtheta(t):
    return float((mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * mp.mpf(t) / 2)) - mp.log(mp.pi)) / 2)

def lanczos_sym(u, W, nmax):
    x = np.concatenate([u, -u]); w = np.concatenate([W, W]) / 2
    Q = np.zeros((len(x), nmax + 1)); Q[:, 0] = np.sqrt(w) / np.sqrt(w.sum())
    out = []; bprev = 0.0
    for k in range(nmax):
        v = x * Q[:, k] - (bprev * Q[:, k - 1] if k > 0 else 0.0)
        for _ in range(2):
            v -= Q[:, :k + 1] @ (Q[:, :k + 1].T @ v)
        b = np.linalg.norm(v)
        if not np.isfinite(b) or b == 0:
            raise RuntimeError('Lanczos breakdown at step %d' % k)
        out.append(b * b); Q[:, k + 1] = v / b; bprev = b
    return np.array(out)

def with_tail(zs, Tt, S_T):
    # Gauss-Legendre on v = log(t/T) in [0, 40] (tail mass beyond T e^40 is ~e^-40 of the tail): the run-1
    # Gauss-Laguerre nodes reached t ~ T e^230, underflowed in the Lanczos vectors and broke the recurrence.
    xg, wg = np.polynomial.legendre.leggauss(80)
    v = 20.0 * (xg + 1.0); wv = 20.0 * wg
    tt = Tt * np.exp(v)
    wt = wv * np.exp(-v) * np.array([dtheta(x) / np.pi for x in tt]) / Tt   # t^-2 dens dt = T^-1 e^-v dens dv
    u = np.concatenate([1 / zs, 1 / tt])
    W = np.concatenate([1 / zs ** 2, wt])
    if S_T != 0:
        # boundary term -f(T) S(T): fold into the first tail node (tiny)
        W[len(zs)] += -S_T * Tt ** -2
    return u, W

t0 = time.time()
Tm = (tk[K - 1] + tk[K]) / 2
Sm = K - (float(theta(mp.mpf(Tm))) / np.pi + 1)
um, Wm = with_tail(tk[:K], Tm, Sm)
al_model = lanczos_sym(um, Wm, NMAX)
Tz = (g[K - 1] + g[K]) / 2
Sz = K - (float(theta(mp.mpf(Tz))) / np.pi + 1)
uz, Wz = with_tail(g[:K], Tz, Sz)
al_zeros = lanczos_sym(uz, Wz, NMAX)
say('Lanczos done %.1fs; S_model(T) = %.4f, S_zeta(T) = %.4f' % (time.time() - t0, Sm, Sz))
Z = json.load(open(os.path.join(tab, 'zeta_real_P24000_S1000.json')))
al_arb = np.array([float(mp.mpf(r['v'])) for r in Z['al']])
n = np.arange(1, 1000)
trunc = np.abs(al_zeros[:999] / al_arb - 1)
say('truncation check (K = %d zeros + tail) vs Arb: max rel err n<=300: %.2e, n<=600: %.2e, n<=999: %.2e'
    % (K, trunc[:300].max(), trunc[:600].max(), trunc.max()))
r = al_arb / al_model[:999] - 1
tn = 1 / (2 * np.sqrt(al_model[:999]))
say('r_n = al(zeta)/al(model) - 1: rms over n in [50,999] = %.4f; first values n=1..8: %s' % (np.sqrt(np.mean(r[49:] ** 2)), np.round(r[:8], 4)))

def periodogram(x, tvals, omegas):
    x = x - x.mean()
    return np.array([abs(np.sum(x * np.exp(1j * w * tvals))) ** 2 for w in omegas]) / len(x)

omegas = np.linspace(0.2, 3.0, 2801)
sel = (n >= 60)
P_r = periodogram(r[sel], tn[sel], omegas)
d = g[:K] - tk[:K]
selz = (tk[:K] > 40) & (tk[:K] < tn[-1])
P_d = periodogram(d[selz], tk[:K][selz], omegas)
def peaks(P, om, top=8):
    idx = [i for i in range(1, len(P) - 1) if P[i] > P[i - 1] and P[i] >= P[i + 1]]
    idx.sort(key=lambda i: -P[i])
    return [(round(float(om[i]), 4), float(P[i])) for i in idx[:top]]
say('periodogram peaks of r_n vs t_n (omega, power):', peaks(P_r, omegas))
say('periodogram peaks of zero displacements d_k vs t_k:', peaks(P_d, omegas))
lp = {'log2': np.log(2), 'log3': np.log(3), 'log4': np.log(4), 'log5': np.log(5), 'log7': np.log(7)}
def power_at(P, w0):
    i = np.argmin(np.abs(omegas - w0)); lo, hi = max(0, i - 6), min(len(P), i + 7)
    return float(P[lo:hi].max())
bg_r = float(np.median(P_r)); bg_d = float(np.median(P_d))
say('power at log p (r_n / median):', {k: round(power_at(P_r, v) / bg_r, 1) for k, v in lp.items()})
say('power at log p (d_k / median):', {k: round(power_at(P_d, v) / bg_d, 1) for k, v in lp.items()})
json.dump({'K': K, 'trunc_max_rel_err': float(trunc.max()), 'r_rms': float(np.sqrt(np.mean(r[49:] ** 2))),
           'peaks_r': peaks(P_r, omegas), 'peaks_d': peaks(P_d, omegas),
           'logp_power_r_over_median': {k: power_at(P_r, v) / bg_r for k, v in lp.items()},
           'logp_power_d_over_median': {k: power_at(P_d, v) / bg_d for k, v in lp.items()},
           'r_n_first_200': [float(x) for x in r[:200]], 't_n_first_200': [float(x) for x in tn[:200]]},
          open(os.path.join(here, 'u4b_primes.json'), 'w'), indent=1)
