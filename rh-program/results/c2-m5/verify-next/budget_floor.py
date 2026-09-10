#!/usr/bin/env python3
"""budget_floor.py -- sanity computation for the Sector-I confinement theorem (candidate R1).

Conventions (derived in PRICING-next-unit.md section 1.1; Lean EF_lit uses h(z) = int k(u) e^{izu} du,
identical for even k):
  cone element  w >= 0, what >= 0, supp w in [-L, L];  g = w / cosh(u/2);  what(xi) = int w(u) e^{-i u xi} du
  on-line zero share      sum_gamma (what * mu_0)(gamma),   mu_0(xi) = 1/cosh(pi xi)   (mass 1, peak 1)
  orbit {+-t +- iy}       4 (what * mu_y)(t),  mu_y(xi) = 2 cos(pi y) cosh(pi xi) / (cosh(2 pi xi) + cos(2 pi y))
  pole                    2 what(0)
  archimedean             int (what * mu_0)(r) A(r) dr,  A(r) = (1/2pi) (Re psi(1/4 + i r/2) - log pi)
  prime share             4 sum_n Lambda(n) w(log n) / (n + 1)
  identity                zero share + prime share = B(w) := 2 what(0) + int (what*mu_0) A   (EF_lit, Zeta23/WeilEF)

Computes:
  (1) a(tau) := (mu_0 * A)(tau); its zero crossing tau_0; I_minus := int_{a<0} |a| (the budget-floor constant);
      the floor kappa := 2 - I_minus if positive (Lemma F of the pricing note).
  (2) For the Fejer family what_T(tau) = (1 - |tau|/T)_+  (w_T(u) = (T/2pi) sinc^2(Tu/2), int w_T = 1):
      B(w_T) = 2 + int (1-|tau|/T)_+ a(tau) dtau   versus   prime share + zero share (first 200 zeros + tail estimate),
      a normalization check of the whole identity, and the minimum of B(w_T)/what(0) over T.
Budget: < 10 minutes.
"""
import time, json, sys
import numpy as np
from scipy.special import digamma
import mpmath as mp

t0 = time.time()
out = {}

# ---- (1) A(tau), a = mu_0 * A --------------------------------------------------------------
def A(tau):
    z = 0.25 + 0.5j * np.asarray(tau, dtype=float)
    return (digamma(z).real - np.log(np.pi)) / (2 * np.pi)

def mu0(xi):
    return 1.0 / np.cosh(np.pi * xi)

# check mass of mu_0 and of mu_y
xi = np.linspace(-12, 12, 480001)
dxi = xi[1] - xi[0]
mass_mu0 = np.trapz(mu0(xi), xi)
def mu_y(xi, y):
    return 2 * np.cos(np.pi * y) * np.cosh(np.pi * xi) / (np.cosh(2 * np.pi * xi) + np.cos(2 * np.pi * y))
mass_mu_y = {y: float(np.trapz(mu_y(xi, y), xi)) for y in (0.0, 0.25, 0.4, 0.45, 0.49)}
peak_mu_y = {y: (float(mu_y(np.array([0.0]), y)[0]), 1 / np.cos(np.pi * y)) for y in (0.0, 0.25, 0.4, 0.45, 0.49)}
out["mass_mu0"] = float(mass_mu0)
out["mass_mu_y"] = mass_mu_y
out["peak_mu_y_vs_1_over_cos"] = peak_mu_y
print("mass mu_0 =", mass_mu0, " mass mu_y:", mass_mu_y)
print("peak mu_y vs 1/cos(pi y):", peak_mu_y)

# a(tau) on a grid by direct quadrature of the convolution (mu_0 decays like e^{-pi|xi|})
tau = np.linspace(0, 60, 6001)
K = 10.0
xg = np.linspace(-K, K, 4001)
dx = xg[1] - xg[0]
mu_g = mu0(xg)
a = np.array([np.trapz(A(tt - xg) * mu_g, xg) for tt in tau])
A_tau = A(tau)
# zero crossing of a and of A
def first_root(x, f):
    s = np.where(np.diff(np.sign(f)) != 0)[0]
    if len(s) == 0:
        return None
    i = s[0]
    return float(x[i] - f[i] * (x[i + 1] - x[i]) / (f[i + 1] - f[i]))
tau0_a = first_root(tau, a)
tau0_A = first_root(tau, A_tau)
neg = a < 0
I_minus_half = -np.trapz(np.where(neg, a, 0.0), tau)   # one side
I_minus = 2 * I_minus_half
out["a_at_0"] = float(a[0]); out["A_at_0"] = float(A_tau[0])
out["tau0_a"] = tau0_a; out["tau0_A"] = tau0_A
out["I_minus_total_both_sides"] = float(I_minus)
out["kappa_floor_2_minus_Iminus"] = float(2 - I_minus)
print(f"a(0) = {a[0]:.6f}   A(0) = {A_tau[0]:.6f}")
print(f"zero crossing: a at tau0 = {tau0_a:.5f};  A at {tau0_A:.5f}")
print(f"I_minus (both sides) = {I_minus:.6f}   ->  2 - I_minus = {2 - I_minus:.6f}")
# a few values for the record
for tt in (0, 1, 2, 3, 4, 5, 6, 8, 10, 14, 20, 30, 60):
    i = int(round(tt / (tau[1] - tau[0])))
    print(f"  tau={tt:5.1f}  A={A_tau[i]: .6f}  a={a[i]: .6f}  (1/2pi)log(tau/2pi)={(np.log(max(tt,1e-9)/(2*np.pi))/(2*np.pi)) if tt>0 else float('nan'): .6f}")
out["table"] = {str(tt): [float(A_tau[int(round(tt/(tau[1]-tau[0])))]), float(a[int(round(tt/(tau[1]-tau[0])))])] for tt in (0,1,2,3,4,5,6,8,10,14,20,30,60)}

# ---- (2) Fejer family: B(w_T) two ways ------------------------------------------------------
# primes side: sieve Lambda(n) to N
N = 4_000_000
lam = np.zeros(N + 1)
is_p = np.ones(N + 1, dtype=bool); is_p[:2] = False
for p in range(2, int(N ** 0.5) + 1):
    if is_p[p]:
        is_p[p * p::p] = False
primes = np.nonzero(is_p)[0]
for p in primes:
    pk = p
    lp = np.log(p)
    while pk <= N:
        lam[pk] = lp
        pk *= p
n = np.arange(2, N + 1)
logn = np.log(n)
lam_n = lam[2:]
print(f"sieve to {N} done at {time.time()-t0:.1f}s; sum Lambda(n)/n = {np.sum(lam_n/n):.4f} (~ log N - gamma = {np.log(N)-0.5772:.4f})")

def w_T(u, T):
    x = T * u / 2
    s = np.where(np.abs(x) < 1e-12, 1.0, np.sin(x) / np.where(np.abs(x) < 1e-12, 1.0, x))
    return (T / (2 * np.pi)) * s * s

# zeros
zeros = [float(mp.zetazero(k).imag) for k in range(1, 201)]
print(f"200 zeros at {time.time()-t0:.1f}s; gamma_1 = {zeros[0]:.6f}, gamma_200 = {zeros[-1]:.4f}")

def whatT(tt, T):
    return np.maximum(0.0, 1 - np.abs(tt) / T)

results = []
for T in (4, 5, 6, 6.5, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 25, 30, 40):
    # archimedean route: B = 2 + int what_T a  (a even; tau grid to 60 covers T <= 40)
    arch = 2 * np.trapz(whatT(tau, T) * a, tau)
    B_arch = 2 + arch
    # prime share, exact to N, plus PNT tail estimate 4 * int_{log N}^inf w_T(u) du (w_T ~ 2/(pi T u^2) averaged)
    P_exact = 4 * np.sum(lam_n * w_T(logn, T) / (n + 1))
    P_tail = 4 * (2 / (np.pi * T)) / np.log(N)   # average of sinc^2 = 1/2 -> w ~ (T/2pi)(2/(T u))^2 /2 = 1/(pi T u^2); times 4, integrated
    # zero share: 2 * sum_gamma (what_T * mu_0)(gamma), first 200 zeros, plus tail over gamma > gamma_200 via density
    nu = lambda s: np.trapz(whatT(s - xg, T) * mu_g, xg)
    Z_exact = 2 * sum(nu(g) for g in zeros)
    # tail: the Fejer transform vanishes beyond T; (what*mu_0)(s) for s > T + 10 is < e^{-pi (s-T)} -- negligible for T <= 40 vs gamma_200 ~ 396
    Z_tail = 0.0
    tot = P_exact + P_tail + Z_exact + Z_tail
    results.append(dict(T=T, B_arch=float(B_arch), arch_term=float(arch), prime_exact=float(P_exact), prime_tail_est=float(P_tail), zero_share=float(Z_exact), sum_shares=float(tot), diff=float(B_arch - tot)))
    print(f"T={T:5.1f}  B_arch=2+{arch: .5f}={B_arch: .5f}   P={P_exact:.5f}(+{P_tail:.5f} tail)  Z={Z_exact:.5f}   shares={tot:.5f}   diff={B_arch-tot: .5f}")
out["fejer_family"] = results
mins = min(results, key=lambda r: r["B_arch"])
out["fejer_min"] = mins
print("min over the Fejer family: T =", mins["T"], " B/what(0) =", mins["B_arch"])
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "budget_floor_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
