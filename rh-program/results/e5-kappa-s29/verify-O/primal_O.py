#!/usr/bin/env python3
"""primal_O.py -- Opus reader, E5: the writer's best primal element (verify/target_primal_fine_best.json: c_i >= 0, hx = 0.005,
fhat = c_i on [i hx, (i+1) hx), w = |f|^2, f(u) = (1/2pi) int fhat e^{iu xi} d xi) re-evaluated three ways with the reader's code:
 (T) tau-space: what = (1/2pi) fhat (autocorrelation) fhat, piecewise linear with knots at k hx -> int what a by 8-point Gauss per segment;
 (U) u-space (reader's u-integral for a, Fubini): int what a = -log(pi) w(0) + int_0^inf [ w(0) e^{-2u}/u - 4 w(u)/((e^u+1)(1-e^{-2u})) ] du;
 (EF) the explicit formula: B = Z + P with P = 4 sum Lambda(n) w(log n)/(n+1) (sieve to N) and Z = 2 sum_{j<=200} int what(tau) sech(pi(gamma_j - tau)) dtau.
Also: cone membership (c >= 0 -> what >= 0; w >= 0 by construction), what's support, and the anatomy of B."""
import numpy as np, json, time, mpmath as mp
from scipy.special import digamma
t0 = time.time(); out = {}
def log(m): print(m, flush=True)
J = json.load(open("../verify/target_primal_fine_best.json")); c = np.array(J["c"], float); hx = float(J["hx"]); n = len(c)
log(f"element: n = {n} cells, hx = {hx}, min c = {c.min():.3e} (cone: c >= 0 -> {bool(c.min() >= 0)}); writer's kappa_ub = {J['kappa_ub']:.10f}")
LOGPI = np.log(np.pi)
def a_fn(t):
    t = np.asarray(t, float); z = 0.5j*t
    return (np.real((1 - 1j*t)*digamma(0.5 + z) + 1j*t*digamma(1.0 + z)) - 1.0 - LOGPI)/(2*np.pi)
# (T)
ac = np.correlate(c, c, mode="full")[n-1:]            # ac[k] = sum_i c_i c_{i+k}
knots = hx*np.arange(n); what_k = hx*ac/(2*np.pi)       # what(k hx)
what0 = what_k[0]
xg, wg = np.polynomial.legendre.leggauss(8)
tl = knots[:-1][:, None] + (xg[None, :] + 1)/2*hx; lam = (xg + 1)/2
wv = what_k[:-1][:, None]*(1 - lam) + what_k[1:][:, None]*lam
last = np.nonzero(what_k > 0)[0].max()
I_T = 2*np.sum(wg[None, :]*hx/2*wv*a_fn(tl))           # even: 2 x int_0^inf
R_T = 2 + I_T/what0
log(f"(T) what(0) = {what0:.10e}; what support |tau| <= {knots[last] + hx:.4f}; min what at knots {what_k.min():.2e}; int what a = {I_T:.10e}; B/what(0) = {R_T:.10f}")
# (U)
mid = (np.arange(n) + 0.5)*hx
def w_of(u):
    u = np.asarray(u, float); outp = np.empty(len(u))
    for i in range(0, len(u), 2000):
        uu = u[i:i+2000, None]
        f = (np.exp(1j*uu*mid[None, :]) @ c)*hx*np.sinc(u[i:i+2000]*hx/(2*np.pi))/(2*np.pi)
        outp[i:i+2000] = np.abs(f)**2
    return outp
w0 = (hx*c.sum()/(2*np.pi))**2
edges = np.arange(0, 60 + 1e-12, 0.02); ul = edges[:-1][:, None] + (xg[None, :] + 1)/2*0.02
uflat = ul.ravel(); wu = w_of(uflat)
integ = w0*np.exp(-2*uflat)/uflat - 4*wu/((np.exp(uflat) + 1)*(-np.expm1(-2*uflat)))
I_U = -LOGPI*w0 + np.sum(integ.reshape(ul.shape)*wg[None, :]*0.01)
R_U = 2 + I_U/what0
intw = np.sum(wu.reshape(ul.shape)*wg[None, :]*0.01)*2
log(f"(U) w(0) = {w0:.6e}; int w over |u| <= 60 = {intw:.10e} (vs what(0) {what0:.10e}); int what a = {I_U:.10e}; B/what(0) = {R_U:.10f};  |T - U| = {abs(R_T - R_U):.2e}")
out.update(what0=what0, R_T=R_T, R_U=R_U, I_T=I_T, I_U=I_U, support=float(knots[last] + hx))
B = 2*what0 + I_T
# (EF): primes
N = 10**7
sieve = np.ones(N + 1, bool); sieve[:2] = False
for p in range(2, int(N**0.5) + 1):
    if sieve[p]: sieve[p*p::p] = False
primes = np.nonzero(sieve)[0]
nn = []; LL = []
for p in primes:
    q = int(p)
    while q <= N: nn.append(q); LL.append(np.log(p)); q *= int(p)
nn = np.array(nn, float); LL = np.array(LL); order = np.argsort(nn); nn, LL = nn[order], LL[order]
wl = w_of(np.log(nn)); terms = 4*LL*wl/(nn + 1)
P = terms.sum(); P6 = terms[nn <= 1e6].sum()
log(f"(EF) prime powers <= 1e7: {len(nn)}; P(1e6) = {P6:.10e}, P(1e7) = {P:.10e}; max w/w(0) on log n in (log 1e6, log 1e7] = {wl[nn > 1e6].max()/w0:.2e}  [{time.time()-t0:.0f}s]")
mp.mp.dps = 20; zs = np.array([float(mp.im(mp.zetazero(j))) for j in range(1, 201)])
tt = np.concatenate([-tl[::-1].ravel(), tl.ravel()]); ww = np.concatenate([(wg[None, :]*hx/2*wv)[::-1].ravel(), (wg[None, :]*hx/2*wv).ravel()])
shares = np.array([2*np.sum(ww/np.cosh(np.minimum(np.abs(np.pi*(g - tt)), 700))) for g in zs])
Z = shares.sum()
log(f"(EF) Z (200 zeros) = {Z:.10e} (gamma_1 share {shares[0]:.4e}, gamma_2 share {shares[1]:.3e}); P + Z = {P+Z:.10e}; B = {B:.10e}; (P+Z)/what(0) = {(P+Z)/what0:.10f}; relative (P+Z-B)/B = {(P+Z-B)/B:.3e}")
anat = {int(k): float(v/B) for k, v in zip(nn[:40], terms[:40]) if v/B > 0.01}
log(f"anatomy (share of B > 1%): gamma_1 {shares[0]/B:.3f}; prime powers {anat}; P(log n <= 2)/B = {terms[np.log(nn) <= 2].sum()/B:.3f}")
lg = np.array([2, 3, 4, 5, 7], float); log(f"w/w(0) at log 2, 3, 4, 5, 7: {np.round(w_of(np.log(lg))/w0, 7).tolist()}")
out.update(P=P, P_1e6=P6, Z=Z, B=B, rel_EF=(P+Z-B)/B, gamma1_share=shares[0]/B, seconds=time.time()-t0)
json.dump(out, open("primal_O_out.json", "w"), indent=1); log(f"done in {time.time()-t0:.1f}s")
