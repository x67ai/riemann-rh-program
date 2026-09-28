#!/usr/bin/env python3
"""sec6_O.py -- Opus reader, E5 section 6: layer constant C = 4(1 + iota/kappa), iota = I_minus - 2 (aform_O_out.json),
the non-vacuity threshold l' > pi C, the exact (6.2) layer at l' = 1e4, 1e5, the mu_y tail beyond t/4 at t = 28, and
the near-window inequality a(3t/4) >= log(3t/8pi)/2pi - 1e-3 for t >= 28."""
import json, mpmath as mp
mp.mp.dps = 30
J = json.load(open("aform_O_out.json")); iota = mp.mpf(J["iota"])
def log(m): print(m, flush=True)
out = {}
for name, k in (("kappa_ub", mp.mpf("0.000998530503213635")), ("kappa_lb_writer", mp.mpf("6.588984853380834e-05")), ("record_0.136", mp.mpf("0.13597"))):
    C = 4*(1 + iota/k); th = mp.pi*C
    lay = {L: float(mp.asin(4*mp.pi*(iota + k)/(k*L))/mp.pi) if 4*mp.pi*(iota + k)/(k*L) < 1 else None for L in (1e4, 1e5)}
    log(f"{name}: kappa = {mp.nstr(k, 8)}  C = {mp.nstr(C, 8)}  non-vacuous iff l' > pi C = {mp.nstr(th, 8)}  exact layer delta_alpha at l' = 1e4, 1e5: {lay}  (linearized C/l': {float(C/1e4):.5f}, {float(C/1e5):.6f})")
    out[name] = dict(C=float(C), threshold=float(th), layer=lay)
# mu_y tail: int_{|xi| > t/4} mu_y <= ?  mu_y <= sin(pi d) cosh(pi xi)/sinh^2(pi xi)
for d in (mp.mpf('0.5'), mp.mpf('0.1'), mp.mpf('0.001')):
    y = mp.mpf('0.5') - d
    mu = lambda x: 2*mp.cos(mp.pi*y)*mp.cosh(mp.pi*x)/(mp.cosh(2*mp.pi*x) + mp.cos(2*mp.pi*y))
    tail = 2*mp.quad(mu, [7, 20, mp.inf])
    log(f"delta = {d}: int_(|xi| > 7) mu_y = {mp.nstr(tail, 6)};  (4/pi) sin(pi delta) e^(-7 pi) = {mp.nstr(4/mp.pi*mp.sin(mp.pi*d)*mp.exp(-7*mp.pi), 6)}")
aC = lambda t: (mp.re((1 - 1j*t)*mp.digamma(0.5 + 0.5j*t) + 1j*t*mp.digamma(1 + 0.5j*t)) - 1 - mp.log(mp.pi))/(2*mp.pi)
worst = min(aC(mp.mpf(3)*t/4) - mp.log(3*mp.mpf(t)/(8*mp.pi))/(2*mp.pi) for t in [28, 30, 40, 60, 100, 1000, 10**5])
log(f"min over t in {{28,...,1e5}} of a(3t/4) - log(3t/8pi)/2pi = {mp.nstr(worst, 6)} (claim: >= -1e-3)")
json.dump(out, open("sec6_O_out.json", "w"), indent=1)
