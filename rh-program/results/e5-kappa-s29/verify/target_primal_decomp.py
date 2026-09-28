#!/usr/bin/env python3
"""target_primal_decomp.py -- independent check of the best primal element via the explicit formula: B(w) = Z(w) + P(w)
(confinement-note (0.3)); P from a von Mangoldt sieve to 10^7 (w evaluated from fhat directly), Z from the first 200 zeros
(what = autocorrelation of fhat, supported in [-W, W] with W < 15, so only the first few zeros' sech tails contribute).
Also reports the arithmetic anatomy of the value: which primes and which zeros carry B."""
import numpy as np, json, time, mpmath as mp
from scipy.special import digamma
t0 = time.time()
best = json.load(open("target_primal_out.json"))["best"]
c = np.array(best["c"]); hx = best["hx"]; n = len(c); xs = (np.arange(n) + 0.5)*hx
kappa_ub = best["kappa_ub"]
# w(u) = |f(u)|^2, f(u) = (1/2pi) int fhat(x) e^{iux} dx  (piecewise constant fhat: exact cell integrals)
def w_of(u):
    u = np.asarray(u, float)[:, None]
    # int_{x_i - hx/2}^{x_i + hx/2} e^{iux} dx = e^{iu x_i} * 2 sin(u hx/2)/u
    ker = np.where(np.abs(u) < 1e-12, hx, 2*np.sin(u*hx/2)/np.where(np.abs(u) < 1e-12, 1, u))
    f = (c[None, :]*np.exp(1j*u*xs[None, :])).sum(axis=1)*ker[:, 0]/(2*np.pi)
    return np.abs(f)**2
what0 = hx*np.sum(c**2)/(2*np.pi)          # what(0) = int w = (1/2pi) int fhat^2
w0 = float(w_of(np.array([0.0]))[0])
# P = 4 sum Lambda(n) w(log n)/(n+1), sieve to N
N = 10_000_000
lam = np.zeros(N + 1); is_p = np.ones(N + 1, bool); is_p[:2] = False
for p in range(2, int(N**0.5) + 1):
    if is_p[p]: is_p[p*p::p] = False
for p in np.nonzero(is_p)[0]:
    pk = p
    while pk <= N: lam[pk] = np.log(p); pk *= p
nn = np.nonzero(lam)[0]
wl = np.concatenate([w_of(np.log(nn[i:i+200000])) for i in range(0, len(nn), 200000)])
terms = 4*lam[nn]*wl/(nn + 1)
P = terms.sum()
# tail beyond N: w(u) <= ? use the computed decay: bound by 4 * int_{log N}^inf w(u) du with w ~ max over last decade
utail = np.linspace(np.log(N), np.log(N) + 30, 3001); wt = w_of(utail); P_tail = 4*np.trapezoid(wt, utail)
# Z = 2 sum_gamma (what * mu_0)(gamma), what from autocorrelation on a fine tau grid
taus = np.arange(-(n-1), n)*hx; what = np.correlate(c, c, mode="full")*hx/(2*np.pi)
zeros = [float(mp.zetazero(k).imag) for k in range(1, 201)]
def conv_mu0(g): return np.trapezoid(what/np.cosh(np.pi*(g - taus)), taus)
Zt = [2*conv_mu0(g) for g in zeros]; Z = sum(Zt)
B = kappa_ub*what0
print(f"what(0) = {what0:.6f}, w(0) = {w0:.6f};  B = kappa_ub * what(0) = {B:.6e}")
print(f"P (sieve to 1e7) = {P:.6e} (+ tail bound {P_tail:.1e});  Z (200 zeros) = {Z:.6e};  P + Z = {P+Z:.6e};  (P+Z)/what(0) = {(P+Z)/what0:.7f} vs kappa_ub = {kappa_ub:.7f};  relative discrepancy {(P+Z-B)/B:+.2e}")
order = np.argsort(-terms)[:12]
print("largest prime-power terms 4 Lambda(n) w(log n)/(n+1), as fraction of B:", [(int(nn[i]), f"{terms[i]/B:.3f}") for i in order])
print("zero shares 2(what*mu0)(gamma)/B for gamma_1..5:", [f"{z/B:.3e}" for z in Zt[:5]])
print(f"w(log n)/w(0) for n = 2..13: {[(int(m), f'{float(w_of(np.array([np.log(m)]))[0])/w0:.1e}') for m in range(2,14)]}")
print(f"cumulative P over log n <= U: " + ", ".join(f"U={U}: {terms[np.log(nn) <= U].sum()/B:.3f}" for U in (1, 2, 3, 4, 6, 8, 10, 14)))
json.dump(dict(what0=what0, w0=w0, B=B, P=P, P_tail=P_tail, Z=Z, rel=(P+Z-B)/B, top=[(int(nn[i]), float(terms[i]/B)) for i in order], Zshares=[float(z/B) for z in Zt[:5]], seconds=time.time()-t0), open("target_primal_decomp_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
