#!/usr/bin/env python3
"""kronecker_instance.py -- M6 rung 1, statement (E): the instance numbers for the prime sum P_X(g_t).

P_X(g_t) = sum_{n <= X} w_n cos(t log n),  w_n = 2 Lambda(n) n^{-1/2} a(log n),  a(x) = L^{-3} A(x/L)  (t-independent coefficients).
Grouping by primes, with theta_p := t log p mod 2pi:  P = sum_p phi_p(theta_p),  phi_p(theta) = sum_{k >= 1} w_{p^k} cos(k theta).
By Kronecker (the {log p} are Q-linearly independent), the closure of {(t log p)_p mod 2pi : t in R} is the whole torus, so
  sup_t P_X(g_t) = sum_p max_theta phi_p(theta),   sup_t (-P_X(g_t)) = sum_p max_theta (-phi_p(theta)),
and sup_t |P_X(g_t)| = max of the two; for p > sqrt X only k = 1 occurs and max phi_p = |w_p|.
This script computes those sups EXACTLY (up to the numerical maximization of a trig polynomial of degree <= log X/log p
for the p <= sqrt X, from the (p, k, w_{p^k}) list the Rust program writes), the l^1 norms, the two trivial bounds, and the
PNT-approximation  l^1 ~ (2/L^2) int_0^1 e^{Lv/2} |A(v)| dv  which is then tabulated at the twelve campaign points
L = L_sign(delta, t) (results/c2-m2/campaign/summary_<tag>.json, 'derived') against the signal 2 delta^2 c(delta L)^2.
"""
import json, math, os, glob, datetime
import numpy as np
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ---------------------------------------------------------------- A(v) and c(lambda) in numpy (own trapezoid, M = 8192)
M = 8192
w = np.arange(1, M)/M - 0.5
with np.errstate(all='ignore'):
    q = 1 - 4*w*w; braw = np.exp(-1/q); bd1 = braw*(-8*w/(q*q))
braw[~np.isfinite(braw)] = 0; bd1[~np.isfinite(bd1)] = 0
Z = braw.sum()/M
def A(v):
    """A(v) = Z^-2 int Braw'(w) Braw'(w - v) dw by the trapezoid rule (vectorized over the nodes)."""
    v = abs(v)
    if v >= 1: return 0.0
    ws = w - v
    with np.errstate(all='ignore'):
        qs = 1 - 4*ws*ws; b2 = np.where(np.abs(ws) < 0.5, np.exp(-1/qs)*(-8*ws/(qs*qs)), 0.0)
    return float((bd1*b2).sum()/M/(Z*Z))
def c_edge(lam):
    return float((braw*np.cosh(lam*w)).sum()/braw.sum())
A0 = A(0.0)
print(f"[{now()}] Z = {Z:.16f}, A(0) = {A0:.12f} (record ||B'||_2^2 = 16.62196535)")

def l1_pnt(L, n=20000):
    """(2/L^2) int_0^1 e^{Lv/2} |A(v)| dv by Simpson on n intervals (the PNT approximation of sum_n 2 Lambda(n) n^{-1/2} |a(log n)|)."""
    vs = np.linspace(0, 1, n + 1)
    f = np.array([math.exp(L*v/2)*abs(A(v)) for v in vs])
    h = 1.0/n
    return float(2/L**2*h/3*(f[0] + f[-1] + 4*f[1:-1:2].sum() + 2*f[2:-1:2].sum()))

def max_trig(coeffs):
    """max over theta of sum_k c_k cos(k theta), k = 1..K: grid of 20000 points then golden-section refinement around the best."""
    K = len(coeffs); c = np.array(coeffs)
    th = np.linspace(0, 2*np.pi, 20001)
    vals = (c[:, None]*np.cos(np.outer(np.arange(1, K + 1), th))).sum(0)
    i = int(np.argmax(vals)); a, b = th[max(i - 1, 0)], th[min(i + 1, len(th) - 1)]
    f = lambda x: float((c*np.cos(np.arange(1, K + 1)*x)).sum())
    gr = (math.sqrt(5) - 1)/2
    x1, x2 = b - gr*(b - a), a + gr*(b - a)
    for _ in range(60):
        if f(x1) < f(x2): a, x1 = x1, x2; x2 = a + gr*(b - a)
        else: b, x2 = x2, x1; x1 = b - gr*(b - a)
    return max(f((a + b)/2), float(vals[i]))

out = dict(date=now(), A0=A0, Z=float(Z), instances={})
for tag in ['zeta_t85p7_L10', 'zeta_t85p7_L20', 'zeta_t1e6_L10', 'zeta_t1e6_L20']:
    d = json.load(open(os.path.join(HERE, 'out', tag + '.json')))
    L = d['L']; X = d['X']
    # group the small prime powers by p
    byp = {}
    for p, k, wv in d['small_prime_powers']:
        byp.setdefault(p, {})[k] = wv
    sup_plus = 0.0; sup_minus = 0.0; l1_small = 0.0; n_small = 0
    for p, ks in byp.items():
        K = max(ks); c = [ks.get(k, 0.0) for k in range(1, K + 1)]
        sup_plus += max_trig(c); sup_minus += max_trig([-x for x in c]); l1_small += sum(abs(x) for x in c); n_small += 1
    # the primes above sqrt X: only k = 1, max = |w_p| for both signs; their l1 = l1_norm - l1_small
    l1_big = d['l1_norm'] - l1_small
    sup_plus += l1_big; sup_minus += l1_big
    sup_abs = max(sup_plus, sup_minus)
    row = dict(L=L, X=X, t=d['t'], n_terms=d['n_terms'], n_primes=d['n_primes'], n_prime_powers=d['n_prime_powers'],
               P_value=d['P_dd'], l1_norm=d['l1_norm'], l1_primes=d['l1_primes'], l1_prime_powers=d['l1_prime_powers'],
               sup_P_exact=sup_plus, sup_minusP_exact=sup_minus, sup_absP_exact=sup_abs, sup_over_l1=sup_abs/d['l1_norm'],
               n_small_primes=n_small, l1_small_primes=l1_small,
               trivial_4sqrtX_a0=d['trivial_bound_4sqrtX_a0'], trivial_2a0_sumLambda=2*d['a0']*d['sum_lambda_over_sqrt_n'],
               l1_pnt_approx=l1_pnt(L), a0=d['a0'], abs_P_over_sup=abs(d['P_dd'])/sup_abs)
    out['instances'][tag] = row
    print(f"[{now()}] {tag}: L={L:g} X={X} terms={d['n_terms']}: P = {d['P_dd']:.6e};  l1 = {d['l1_norm']:.6f} (primes {d['l1_primes']:.6f}, prime powers {d['l1_prime_powers']:.3e});  "
          f"EXACT sup_t P = {sup_plus:.6f}, sup_t(-P) = {sup_minus:.6f}, sup|P| = {sup_abs:.6f} (= {sup_abs/d['l1_norm']:.6f} x l1);  "
          f"trivial 4 sqrtX a0 = {d['trivial_bound_4sqrtX_a0']:.4f}, 2 a0 sum Lambda/sqrt n = {2*d['a0']*d['sum_lambda_over_sqrt_n']:.4f};  PNT approx of l1 = {l1_pnt(L):.6f};  |P|/sup = {abs(d['P_dd'])/sup_abs:.2e}")

# ---------------------------------------------------------------- the twelve campaign points: l1 (PNT approx) vs the signal at L_sign
camp = {}
for tag, t in [('t1e3', 1e3), ('t1e4', 1e4), ('t1e5', 1e5), ('t1e6', 1e6)]:
    s = json.load(open(os.path.join(HERE, '..', '..', 'c2-m2', 'campaign', f'summary_{tag}.json')))
    camp[t] = s['derived']
table = []
print(f"[{now()}] the twelve campaign points (L_sign at t from summary_<tag>.json 'derived'): l1-norm of the prime sum (PNT approx) against the orbit signal 2 delta^2 c(delta L)^2 and the margin-3 requirement")
for t in (1e3, 1e4, 1e5, 1e6):
    for dl in ('0.05', '0.1', '0.25'):
        delta = float(dl); Ls = camp[t][dl]['L_sign']; Lb = camp[t][dl]['L_bal3']
        for L, lab in ((Ls, 'L_sign'), (Lb, 'L_bal3')):
            sig = 2*delta**2*c_edge(delta*L)**2
            l1 = l1_pnt(L)
            X = math.exp(L)
            table.append(dict(t=t, delta=delta, which=lab, L=L, X=X, signal=sig, l1_pnt=l1, ratio_l1_over_signal=l1/sig, ratio_l1_over_halfsignal=l1/(sig/2)))
            print(f"   t={t:8.0e} delta={delta:5.2f} {lab}={L:5.1f}: X = e^L = {X:.2e};  signal 2d^2c^2 = {sig:.4e};  l1(P) ~ {l1:.4e};  l1/signal = {l1/sig:.3e}")
out['campaign_points'] = table
json.dump(out, open(os.path.join(HERE, 'out', 'kronecker_instance.json'), 'w'), indent=1)
print(f"[{now()}] wrote out/kronecker_instance.json")
