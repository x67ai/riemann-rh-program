#!/usr/bin/env python3
"""aform_O.py -- Opus reader, E5: the archimedean density a = mu_0 * A three independent ways.
 (D) definition: a(tau) = int sech(pi(tau - r)) A(r) dr, A(r) = (1/2pi)[Re psi(1/4 + ir/2) - log pi]   (mpmath quad)
 (U) reader's u-integral (psi(z) = int_0^inf [e^{-t}/t - e^{-zt}/(1-e^{-t})] dt, convolved; t = 2u):
     2 pi a(tau) + log pi = int_0^inf [ e^{-2u}/u - 4 cos(tau u) / ((e^u + 1)(1 - e^{-2u})) ] du
 (C) writer's closed form (2.1): a = (1/2pi)[Re{(1 - i tau) psi(1/2 + i tau/2) + i tau psi(1 + i tau/2)} - 1 - log pi]
 Reader's derivation of (C) from (U) (integration by parts; the boundary term is 2 h(0) = 1 with h(t) = 1/(e^{t/2}+1)) is in read-O.md.
 Also: tau_0, I_minus, and the float64 (scipy) closed form against mpmath (C) on [0, 1000] -- the error budget of the certificate check."""
import mpmath as mp, numpy as np, json, time
from scipy.special import digamma
mp.mp.dps = 30; t0 = time.time(); out = {}
def log(m): print(m, flush=True)
def A(r): return (mp.re(mp.digamma(mp.mpf(1)/4 + 0.5j*r)) - mp.log(mp.pi))/(2*mp.pi)
def a_D(tau):
    tau = mp.mpf(tau); pts = [tau - 40 + k for k in range(0, 81)]
    return mp.quad(lambda r: mp.sech(mp.pi*(tau - r))*A(r), pts)
def a_U(tau):
    tau = mp.mpf(tau)
    f = lambda u: mp.exp(-2*u)/u - 4*mp.cos(tau*u)/((mp.exp(u) + 1)*(1 - mp.exp(-2*u)))
    step = min(mp.mpf('0.25'), mp.pi/(4*max(tau, 1)))
    pts = [mp.mpf(0)] + [step*k for k in range(1, int(80/step) + 1)]
    # Gauss-Legendre: tanh-sinh nodes reach u ~ 1e-40 where the two 1/u terms cancel catastrophically at 30 digits
    with mp.workdps(50):
        v = mp.quad(f, pts, method="gauss-legendre")
    return (v - mp.log(mp.pi))/(2*mp.pi)
def a_C(tau):
    tau = mp.mpf(tau); z = 0.5j*tau
    return (mp.re((1 - 1j*tau)*mp.digamma(0.5 + z) + 1j*tau*mp.digamma(1 + z)) - 1 - mp.log(mp.pi))/(2*mp.pi)
res = {}
for tau in (0, 1, 6.31, 30):
    d, u, c = a_D(tau), a_U(tau), a_C(tau)
    res[str(tau)] = dict(def_=float(d), u_int=float(u), closed=float(c), dC_D=float(abs(c - d)), dC_U=float(abs(c - u)))
    log(f"tau = {tau:6}: a_def = {mp.nstr(d, 16)}  a_uint = {mp.nstr(u, 16)}  a_closed = {mp.nstr(c, 16)}  |C-D| = {mp.nstr(abs(c-d), 3)}  |C-U| = {mp.nstr(abs(c-u), 3)}  [{time.time()-t0:.0f}s]")
out["three_ways"] = res
a0 = a_C(0); log(f"a(0) = {mp.nstr(a0, 12)}  (= (psi(1/2) - 1 - log pi)/2pi = {mp.nstr((mp.digamma(0.5) - 1 - mp.log(mp.pi))/(2*mp.pi), 12)})")
tau0 = mp.findroot(a_C, 6.3); log(f"tau_0 = {mp.nstr(tau0, 12)}")
Im = 2*mp.quad(lambda t: -a_C(t), [0, 1, 2, 3, 4, 5, 6, tau0]); log(f"I_minus = 2 int_0^tau0 |a| = {mp.nstr(Im, 12)};  I_minus - 2 = {mp.nstr(Im - 2, 10)}")
out.update(a0=float(a0), tau0=float(tau0), I_minus=float(Im), iota=float(Im - 2))
# float64 closed form vs mpmath closed form
def a_f64(tau):
    tau = np.asarray(tau, float); z = 0.5j*tau
    return (np.real((1 - 1j*tau)*digamma(0.5 + z) + 1j*tau*digamma(1.0 + z)) - 1.0 - np.log(np.pi))/(2*np.pi)
rng = np.random.default_rng(7)
taus = np.concatenate([np.linspace(0, 20, 2001), rng.uniform(0, 1000, 2000), [1000.0]])
errs = np.array([abs(float(a_C(t)) - float(a_f64(t))) for t in taus])
log(f"float64 closed form vs mpmath (30 digits) at {len(taus)} points of [0, 1000]: max abs error {errs.max():.2e} at tau = {taus[errs.argmax()]:.3f}")
out["f64_max_err"] = float(errs.max())
# monotonicity of a (Lemma A3) numerically and the value at 1000
g = np.linspace(1e-6, 1000, 2000001); ag = a_f64(g); log(f"a increasing on (0, 1000] grid of 2e6 points: {bool(np.all(np.diff(ag) > 0))};  2 pi a(1000) = {2*np.pi*float(a_C(1000)):.6f}")
out["a_monotone_grid"] = bool(np.all(np.diff(ag) > 0)); out["twopi_a_1000"] = float(2*mp.pi*a_C(1000))
out["seconds"] = time.time() - t0; json.dump(out, open("aform_O_out.json", "w"), indent=1); log(f"done in {time.time()-t0:.1f}s")
