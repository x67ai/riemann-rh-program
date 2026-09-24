#!/usr/bin/env python3
"""o4_recheck.py -- Opus re-check (Session 24) of the fix pass's Part B column.

Independent of the author's planted_real_zero_fix.py: the real-zero share is computed in u-space,
share = 2 int_R w(u) k_y(u) du, k_y(u) = cosh(yu)/cosh(u/2), y = 1/2 - delta,
with w the inverse transform of what (what(xi) = int w e^{-iu xi} du) in closed form:
  Fejer    what = (1 - |s|/T)_+      -> w(u) = (1 - cos Tu)/(pi T u^2)
  Fejer^2  what = (1 - |s|/T)_+^2    -> w(u) = (2/(T u^2) - 2 sin(Tu)/(T^2 u^3))/pi
  Gauss    what = e^{-s^2/2 s^2}     -> w(u) = sigma/sqrt(2 pi) e^{-sigma^2 u^2/2}
  Poisson  what = 2a/(a^2 + s^2)     -> w(u) = e^{-a|u|}
Arch_K(w) = int what a_K over the full line, a_K(s) = (1/pi)[Re psi(1/2 + is/2) - log pi] + log|D|/2pi (check-O item 2).
The 32-element family is the one printed in siegel-world-scout.md section 2.3 (nine T for Fejer and Fejer^2, eight sigma, six a).
Margins: single = share - 2 what(0) - Arch; double = 2 share - 2 what(0) - Arch.
"""
import math, json
import numpy as np
from scipy.integrate import quad
from scipy.special import digamma as sdg
LOG = []
def say(s): print(s, flush=True); LOG.append(s)
LOGPI = math.log(math.pi)
def aK(s, absD): return (float(np.real(sdg(0.5 + 0.5j * s))) - LOGPI) / math.pi + math.log(absD) / (2 * math.pi)
def k(u, y):
    return math.exp((y - 0.5) * u) * (1 + math.exp(-2 * y * u)) / (1 + math.exp(-u))
def Q(f, a, b, **kw): return quad(f, a, b, limit=2000, epsabs=1e-13, epsrel=1e-11, **kw)[0]
U = 60.0
def share_u(kind, p, de):
    y = 0.5 - de
    pts = np.linspace(0, U, 241)
    if kind == "gauss":
        w = lambda u: p / math.sqrt(2 * math.pi) * math.exp(-p * p * u * u / 2)
        return 4 * sum(Q(lambda u: w(u) * k(u, y), a, b) for a, b in zip(pts[:-1], pts[1:])) + 4 * Q(lambda u: w(u) * k(u, y), U, np.inf)
    if kind == "poisson":
        return 4 * Q(lambda u: math.exp(-p * u) * k(u, y), 0, np.inf)
    if kind == "fejer":
        def w(u):
            if u < 1e-4: return p / (2 * math.pi) * (1 - (p * u) ** 2 / 12)
            return (1 - math.cos(p * u)) / (math.pi * p * u * u)
        head = sum(Q(lambda u: w(u) * k(u, y), a, b) for a, b in zip(pts[:-1], pts[1:]))
        tail = Q(lambda u: k(u, y) / (math.pi * p * u * u), U, np.inf) - Q(lambda u: k(u, y) / (math.pi * p * u * u), U, np.inf, weight="cos", wvar=p)
        return 4 * (head + tail)
    if kind == "fejer2":
        def w(u):
            if u < 1e-3: return (p / 3 - p ** 3 * u * u / 60) / math.pi   # (1/pi) int_0^T (1-x/T)^2 cos(ux) dx, Taylor
            return (2 / (p * u * u) - 2 * math.sin(p * u) / (p * p * u ** 3)) / math.pi
        head = sum(Q(lambda u: w(u) * k(u, y), a, b) for a, b in zip(pts[:-1], pts[1:]))
        tail = Q(lambda u: 2 * k(u, y) / (math.pi * p * u * u), U, np.inf) - Q(lambda u: 2 * k(u, y) / (math.pi * p * p * u ** 3), U, np.inf, weight="sin", wvar=p)
        return 4 * (head + tail)
def what(kind, p):
    return {"gauss": lambda s: math.exp(-s * s / (2 * p * p)), "poisson": lambda s: 2 * p / (p * p + s * s),
            "fejer": lambda s: max(0.0, 1 - abs(s) / p), "fejer2": lambda s: max(0.0, 1 - abs(s) / p) ** 2}[kind]
def arch(kind, p, absD):
    f = what(kind, p); hi = p if kind in ("fejer", "fejer2") else np.inf
    pts = [x for x in (0.5, 2, 10, 30) if x < hi]
    e = [0.0] + pts + [hi]
    return 2 * sum(Q(lambda s: f(s) * aK(s, absD), a, b) for a, b in zip(e[:-1], e[1:]))
FAM = []
for T in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0): FAM += [("Fejer T=%g" % T, "fejer", T), ("Fejer^2 T=%g" % T, "fejer2", T)]
for sg in (0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0): FAM.append(("Gauss sigma=%g" % sg, "gauss", sg))
for a in (0.55, 0.6, 0.75, 1.0, 1.5, 2.0): FAM.append(("Poisson a=%g" % a, "poisson", a))
say("family size: %d" % len(FAM))
# transform sanity: w(0) = (1/2pi) int what
for name, kind, p in FAM[:4]:
    pass
DEL = (0.1, 0.05, 0.02, 0.01, 0.001)
SH = {(n, d): share_u(kd, p, d) for n, kd, p in FAM for d in DEL}
# cross-check u-space share against xi-space share for four elements at delta = 0.1 and 0.001
def mu(s, de):
    sd = math.sin(math.pi * de)
    if math.pi * abs(s) > 300: return 2 * sd * math.exp(-math.pi * abs(s))
    sh = math.sinh(math.pi * s); return sd * math.cosh(math.pi * s) / (sh * sh + sd * sd)
for n, kd, p in [FAM[6], FAM[7], FAM[23], FAM[26]]:
    for d in (0.1, 0.001):
        f = what(kd, p); hi = p if kd in ("fejer", "fejer2") else np.inf
        e = [0.0] + [x for x in (d, 10 * d, 100 * d, 1, 5, 20) if x < hi] + [hi]
        xs = 4 * sum(Q(lambda s: f(s) * mu(s, d), a, b) for a, b in zip(e[:-1], e[1:]))
        say("  share cross-check %-16s delta=%.3f: u-space %.10f xi-space %.10f diff %.1e" % (n, d, SH[(n, d)], xs, SH[(n, d)] - xs))
w0 = {n: (2 / p if kd == "poisson" else 1.0) for n, kd, p in FAM}
capmax = max(SH[(n, d)] / (2 * w0[n]) for n, kd, p in FAM for d in DEL)
say("pole-cap ratio max share/(2 what(0)) over family and delta = %.6f" % capmax)
OUT = {}
for absD, lab in ((20, "D = -20"), (2005, "|D| = 2005"), (1e6, "|D| = 1e6")):
    AR = {n: arch(kd, p, absD) for n, kd, p in FAM}
    say("[%s]" % lab)
    for d in DEL:
        s1 = sorted(((SH[(n, d)] - 2 * w0[n] - AR[n], n) for n, kd, p in FAM), reverse=True)
        s2 = sorted(((2 * SH[(n, d)] - 2 * w0[n] - AR[n], n) for n, kd, p in FAM), reverse=True)
        say("  delta=%.3f: best single %+.5f [%s] (runner-up %+.5f [%s]) %s ; best double %+.5f [%s] %s" % (
            d, s1[0][0], s1[0][1], s1[1][0], s1[1][1], "FIRES" if s1[0][0] > 0 else "silent", s2[0][0], s2[0][1], "FIRES" if s2[0][0] > 0 else "silent"))
        OUT["%s|%g" % (lab, d)] = dict(single=s1[0], double=s2[0])
    if absD == 20:
        for n in ("Poisson a=0.6", "Poisson a=0.55", "Gauss sigma=1"):
            say("  %s single margins: %s" % (n, ", ".join("%+.5f" % (SH[(n, d)] - 2 * w0[n] - AR[n]) for d in DEL)))
json.dump(dict(log=LOG, out={k: [list(v["single"]), list(v["double"])] for k, v in OUT.items()}), open(__file__.replace(".py", "_out.json"), "w"), indent=1)
