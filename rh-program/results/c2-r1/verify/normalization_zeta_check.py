#!/usr/bin/env python3
"""normalization_zeta_check.py -- the identity (0.3) of confinement-note.md checked against zeta itself
(reproducing PRICING-next-unit section 0's check in this note's own code), plus the budget-floor numbers of section 8.

Conventions: what(xi) = int w e^{-i u xi};  g = w/cosh(u/2);  mu_0 = 1/cosh(pi xi);  A(r) = (1/2pi)(Re psi(1/4 + i r/2) - log pi);
  B(w) = 2 what(0) + int (what * mu_0)(r) A(r) dr = 2 what(0) + int what(tau) a(tau) dtau,  a := mu_0 * A  (A even);
  P(w) = 4 sum_n Lambda(n) w(log n)/(n+1);   Z_on(w) = 2 sum_{gamma>0} (what * mu_0)(gamma).
Fejer family: what_T(tau) = (1 - |tau|/T)_+,  w_T(u) = (T/2pi) sinc^2(T u/2),  int w_T = 1.
Also: a(0), the zero crossing tau_0 of a, I_minus = int_{a<0} |a| (both sides), the Fejer-family minimum of B/what(0)
(the primal upper bound for kappa = inf B(w)/what(0), section 8).
Budget: < 1 minute (sieve to 4e6; first 200 zeros by mpmath.zetazero).
"""
import json, sys, time
import numpy as np
from scipy.special import digamma
import mpmath as mp

t0 = time.time(); out = {}

def A(r):
    z = 0.25 + 0.5j * np.asarray(r, dtype=float)
    return (digamma(z).real - np.log(np.pi)) / (2 * np.pi)
def mu0(x):
    return 1.0 / np.cosh(np.pi * x)

# a(tau) = (mu_0 * A)(tau) on [0, 60]
tau = np.linspace(0, 60, 6001)
xg = np.linspace(-10, 10, 4001)
mug = mu0(xg)
a = np.array([np.trapezoid(A(tt - xg) * mug, xg) for tt in tau])
Atau = A(tau)
def first_root(x, f):
    s = np.where(np.diff(np.sign(f)) != 0)[0]
    i = s[0]
    return float(x[i] - f[i] * (x[i + 1] - x[i]) / (f[i + 1] - f[i]))
tau0 = first_root(tau, a)
I_minus = 2 * float(-np.trapezoid(np.where(a < 0, a, 0.0), tau))
out.update(a_at_0=float(a[0]), A_at_0=float(Atau[0]), tau0_a=tau0, I_minus_both_sides=I_minus, two_minus_I_minus=2 - I_minus)
print(f"a(0) = {a[0]:.6f}, A(0) = {Atau[0]:.6f}, zero crossing of a at tau_0 = {tau0:.4f}, I_minus (both sides) = {I_minus:.6f}, 2 - I_minus = {2 - I_minus:.6f}")
for tt in (8, 10, 20, 60):
    i = int(round(tt / (tau[1] - tau[0])))
    print(f"   tau={tt:4.1f}: a = {a[i]:.6f}, (1/2pi) log(tau/2pi) = {np.log(tt/(2*np.pi))/(2*np.pi):.6f}")

# primes: Lambda(n) to N
N = 4_000_000
lam = np.zeros(N + 1)
is_p = np.ones(N + 1, dtype=bool); is_p[:2] = False
for p in range(2, int(N ** 0.5) + 1):
    if is_p[p]:
        is_p[p * p::p] = False
for p in np.nonzero(is_p)[0]:
    pk = p; lp = np.log(p)
    while pk <= N:
        lam[pk] = lp; pk *= p
n = np.arange(2, N + 1); logn = np.log(n); lam_n = lam[2:]
print(f"sieve to {N}: sum Lambda(n)/n = {np.sum(lam_n/n):.4f} (log N - gamma = {np.log(N) - 0.5772157:.4f}); {time.time()-t0:.1f}s")

zeros = [float(mp.zetazero(k).imag) for k in range(1, 201)]
out["gamma_1"] = zeros[0]; out["gamma_200"] = zeros[-1]
print(f"first 200 zeros: gamma_1 = {zeros[0]:.6f}, gamma_2 = {zeros[1]:.6f}, gamma_200 = {zeros[-1]:.4f}; {time.time()-t0:.1f}s")

def w_T(u, T):
    x = T * u / 2
    s = np.where(np.abs(x) < 1e-12, 1.0, np.sin(x) / np.where(np.abs(x) < 1e-12, 1.0, x))
    return (T / (2 * np.pi)) * s * s
def whatT(x, T):
    return np.maximum(0.0, 1 - np.abs(x) / T)

rows = []
for T in (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 25, 30, 40):
    arch = 2 * np.trapezoid(whatT(tau, T) * a, tau)           # a even: int_R what_T a = 2 int_0^60
    B = 2 + arch
    P = 4 * np.sum(lam_n * w_T(logn, T) / (n + 1))
    P_tail = 4 * (2 / (np.pi * T)) / np.log(N)                # w_T ~ 1/(pi T u^2) on average beyond log N
    Z = 2 * sum(np.trapezoid(whatT(g - xg, T) * mug, xg) for g in zeros)   # zeros beyond gamma_200 = 396 see no mass for T <= 40
    rows.append(dict(T=T, B=float(B), P=float(P), P_tail=float(P_tail), Z=float(Z), shares=float(P + P_tail + Z), diff=float(B - P - P_tail - Z)))
    print(f"T={T:5.1f}  B = 2 + {arch: .5f} = {B: .5f}   P = {P:.5f} (+{P_tail:.5f} tail)   Z = {Z:.5f}   shares = {P+P_tail+Z:.5f}   B - shares = {B-P-P_tail-Z: .5f}")
out["fejer_rows"] = rows
mn = min(rows, key=lambda r: r["B"])
out["fejer_min_B_over_what0"] = mn
print(f"min over the Fejer family of B(w_T)/what_T(0): T = {mn['T']}, B = {mn['B']:.5f}  (primal upper bound for kappa)")
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "normalization_zeta_check_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
