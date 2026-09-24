#!/usr/bin/env python3
"""o2_planted_margins.py -- Opus independent check of the Siegel-zero scout, items 2-4 (numerics).

Own code, from confinement-note section 0.1 / section 4 formulas; nothing imported from the scout's verify/.
 * closed form (derived in check-O.md item 2):  a_K(s) = (mu_0 * A_K)(s) = (1/pi)[Re psi(1/2 + is/2) - log pi] + log|D|/(2pi)  (odd chi)
   => D1 = 16 pi^2 e^{2 gamma} = D0/4,  D0 = 64 pi^2 e^{2 gamma}.  Checked here against direct quadrature of mu_0 * A_K.
 * dlVP element w_{a,t} (note section 4), degree-2 budget via duplication:
   B_K = sum_j d_j [2 Re(1/(s_j-1) + 1/s_j) + 2 Re psi(s_j) - 2 log 2 - 2 log pi + log|D|],  s_j = 1 + eta + i j t, d = (3,4,1).
   real-zero share (two-point orbit, y = 1/2 - delta): 2 sum_k c_k Re pi_a(k t - i y); double zero: twice that.
 * one-parameter families with what(0) = 1-normalized closed/quadrature shares: Gaussian what = e^{-s^2/2 sig^2},
   pure Poisson what = pi_a (w = e^{-a|u|}), Fejer what = (1-|s|/T)_+ ; continuous optimization of the parameter.
"""
import json, math, time
import numpy as np
import mpmath as mp
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, brentq
from scipy.special import digamma as sdg

T0 = time.time(); LOG = []; out = {}
def say(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); LOG.append(s)
LOGPI = math.log(math.pi); LOG2 = math.log(2)

# ---------- a_K closed form vs quadrature ----------
def aK_closed(s, absD): return (np.real(sdg(0.5 + 0.5j * s)) - LOGPI) / math.pi + math.log(absD) / (2 * math.pi)
def aK_quad(s, absD):
    f = lambda r: (1 / math.cosh(math.pi * (s - r))) * (2 * np.real(sdg(0.5 + 1j * r)) - 2 * math.log(2 * math.pi) + math.log(absD)) / (2 * math.pi)
    return quad(f, s - 35, s + 35, limit=500, epsabs=1e-13)[0]
err = max(abs(aK_closed(s, 20) - aK_quad(s, 20)) for s in (0, 0.3, 1.54, 3, 10, 40))
say("a_K closed form (1/pi)[Re psi(1/2+is/2) - log pi] + log|D|/2pi vs quadrature of mu_0*A_K at s in {0,0.3,1.54,3,10,40}, D=-20: max diff %.2e" % err)
g = float(mp.euler)
say("D1 = 16 pi^2 e^{2 gamma} = %.6f ; D0 = 64 pi^2 e^{2 gamma} = %.6f ; a_K(0; D1) = %.2e" % (16 * math.pi**2 * math.exp(2*g), 64 * math.pi**2 * math.exp(2*g), aK_closed(0, 16 * math.pi**2 * math.exp(2*g))))
out["D1"] = 16 * math.pi**2 * math.exp(2*g); out["D0"] = 64 * math.pi**2 * math.exp(2*g)

# ---------- dlVP element ----------
C = {0: 3.0, 1: 2.0, -1: 2.0, 2: 0.5, -2: 0.5}; DW = (3, 4, 1)
def rpi(a, x, y):   # Re pi_a(x - i y)
    return (a + y) / ((a + y)**2 + x*x) + (a - y) / ((a - y)**2 + x*x)
def B_dlvp(eta, t, absD):
    tot = 0.0
    for j, d in enumerate(DW):
        s = complex(1 + eta, j * t)
        tot += d * (2 * ((1 / (s - 1)).real + (1 / s).real) + 2 * sdg(s).real - 2 * LOG2 - 2 * LOGPI + math.log(absD))
    return tot
def share_real(eta, t, delta):   # two-point orbit
    a = 0.5 + eta; y = 0.5 - delta
    return 2 * sum(c * rpi(a, k * t, y) for k, c in C.items())
def best_eta(f, lo=1e-5, hi=3.0):
    xs = np.exp(np.linspace(math.log(lo), math.log(hi), 400)); v = [f(x) for x in xs]; i = int(np.argmax(v))
    a_, b_ = xs[max(i - 1, 0)], xs[min(i + 1, len(xs) - 1)]
    r = minimize_scalar(lambda x: -f(x), bounds=(a_, b_), method="bounded", options={"xatol": 1e-12})
    return (-r.fun, r.x) if -r.fun >= v[i] else (v[i], xs[i])
# degree-2 Lemma A spot check: (1/2pi) int pi_a(r - x)[2 Re psi(1/2+ir) - 2 log 2pi + log|D|] dr vs 2 Re psi(1/2 + a + ix) - 2log 2pi + log|D|
for (a, x) in ((0.8, 0.0), (0.8, 5.0), (1.3, 28.0)):
    lhs = quad(lambda r: 2*a/(a*a + (r-x)**2) * (2*np.real(sdg(0.5+1j*r)) - 2*math.log(2*math.pi) + math.log(20)) / (2*math.pi), -np.inf, np.inf, limit=800, epsabs=1e-12)[0]
    rhs = 2*np.real(sdg(0.5 + a + 1j*x)) - 2*math.log(2*math.pi) + math.log(20)
    say("Lemma A degree 2 (duplication form), a=%.1f x=%.1f: quad %.10f closed %.10f diff %.1e" % (a, x, lhs, rhs, lhs - rhs))
say("Part A (dlVP, D = -20): continuous max over eta of single margin [share - B_K] and double margin [2 share - B_K]")
partA = []
for t in (0, 1, 5, 28):
    for de in (0.1, 0.05, 0.02, 0.01, 0.001):
        ms, es = best_eta(lambda e: share_real(e, t, de) - B_dlvp(e, t, 20))
        md, ed = best_eta(lambda e: 2 * share_real(e, t, de) - B_dlvp(e, t, 20))
        partA.append(dict(t=t, delta=de, single=ms, eta_s=es, double=md, eta_d=ed))
        say("  t=%3d delta=%.3f single %+10.4f (eta %.4f) %s ; double %+10.4f (eta %.4f) %s" % (t, de, ms, es, "FIRES" if ms > 0 else "silent", md, ed, "FIRES" if md > 0 else "silent"))
out["partA"] = partA
# positive control: sup over delta, eta of the dlVP single margin at t = 0 for |D| >= D1
for absD in (501, 2005, 1e6, 1e12):
    best = -1e9
    for de in np.exp(np.linspace(math.log(1e-6), math.log(0.5), 120)):
        m, _ = best_eta(lambda e: share_real(e, 0, de) - B_dlvp(e, 0, absD)); best = max(best, m)
    say("positive control dlVP t=0, |D| = %g: sup over delta in [1e-6, 0.5], eta of single margin = %+.4f" % (absD, best))
# the double-zero asymptote for the dlVP-Poisson element (t = 0)
def dmax_double_dlvp(absD):
    f = lambda de: best_eta(lambda e: 2 * share_real(e, 0, de) - B_dlvp(e, 0, absD))[0]
    if f(0.4999) > 0: return 0.5
    return brentq(f, 1e-9, 0.4999, xtol=1e-14)
for absD in (1e3, 1e4, 1e6, 1e10, 1e20, 1e40, 1e80):
    d = dmax_double_dlvp(absD); say("dlVP-Poisson double real zero excluded for delta < %.6f at |D| = %g ; delta_max log|D| = %.4f" % (d, absD, d * math.log(absD)))
say("  asymptote 6 - 4 sqrt2 = %.6f" % (6 - 4 * math.sqrt(2)))

# ---------- one-parameter families (what(0) = 1 up to Poisson's 2/a) ----------
def mu(s, de):   # stable form of mu_y, y = 1/2 - delta
    sd = math.sin(math.pi * de)
    if math.pi * abs(s) > 300: return 2 * sd * math.exp(-math.pi * abs(s))
    sh = math.sinh(math.pi * s)
    return sd * math.cosh(math.pi * s) / (sh * sh + sd * sd)
def brk(de, extra=()):
    return sorted(set([de, 3*de, 10*de, 30*de, 100*de, 0.3, 1.0, 3.0] + list(extra)))
def I(f, lo, hi, pts):
    pts = [p for p in pts if lo < p < hi]
    edges = [lo] + pts + [hi]; tot = 0.0
    for a, b in zip(edges[:-1], edges[1:]):
        tot += quad(f, a, b, limit=400, epsabs=1e-13, epsrel=1e-11)[0]
    return tot
fams = {
  "gauss":   dict(what=lambda s, p: math.exp(-s*s/(2*p*p)), w0=lambda p: 1.0, mass=lambda p: p*math.sqrt(2*math.pi), hi=lambda p: 12*p, rng=(1e-4, 5.0)),
  "poisson": dict(what=lambda s, p: 2*p/(p*p+s*s), w0=lambda p: 2/p, mass=lambda p: 2*math.pi, hi=lambda p: math.inf, rng=(1e-4, 5.0)),
  "fejer":   dict(what=lambda s, p: max(0.0, 1-abs(s)/p), w0=lambda p: 1.0, mass=lambda p: p, hi=lambda p: p, rng=(0.05, 12.0)),
}
def share_f(F, p, de):   # 2 int what mu_y  (two-point orbit)
    hi = F["hi"](p); ex = [p] if hi == p else []
    return 2 * 2 * I(lambda s: F["what"](s, p) * mu(s, de), 0, hi if hi != math.inf else math.inf, brk(de, ex))
def arch1(F, p):   # int what (1/pi)[Re psi(1/2+is/2) - log pi]
    hi = F["hi"](p); ex = [p] if hi == p else []
    return 2 * I(lambda s: F["what"](s, p) * (np.real(sdg(0.5+0.5j*s)) - LOGPI) / math.pi, 0, hi, [0.5, 2, 10] + ex)
# closed-form cross-checks for pure Poisson: arch1 = 2[psi(1/2 + a/2) - log pi]; share = 2 * 2pi / cos(pi(a - y)) for a < 1/2 + y
F = fams["poisson"]
for a in (0.3, 0.6):
    say("Poisson closed-form checks a=%.1f: arch1 quad %.10f closed %.10f ; share(delta=0.1) xi-quad %.10f u-space 2 int w k_y %.10f"
        % (a, arch1(F, a), 2*(float(mp.digamma(0.5 + a/2)) - LOGPI), share_f(F, a, 0.1),
           2*2*float(mp.quad(lambda u: mp.exp(-a*u)*mp.cosh(0.4*u)/mp.cosh(u/2), [0, mp.inf]))))
cache = {}
def logD_close(fam, p, de, mult=1):
    """largest log|D| at which the element still certifies against a single (mult=1) or double (mult=2) real zero at depth de"""
    F = fams[fam]; key = (fam, round(p, 12), de)
    if key not in cache: cache[key] = (share_f(F, p, de), arch1(F, p))
    sh, a1 = cache[key]
    return 2 * math.pi * (mult * sh - 2 * F["w0"](p) - a1) / F["mass"](p)
def best_close(fam, de, mult=1):
    lo, hi = fams[fam]["rng"]
    xs = np.exp(np.linspace(math.log(lo), math.log(hi), 90)); v = [logD_close(fam, x, de, mult) for x in xs]; i = int(np.argmax(v))
    r = minimize_scalar(lambda x: -logD_close(fam, x, de, mult), bounds=(xs[max(i-1,0)], xs[min(i+1,len(xs)-1)]), method="bounded", options={"xatol": 1e-7})
    return max(-r.fun, v[i]), (r.x if -r.fun >= v[i] else xs[i])
say("closing conductor for ONE real zero, best element of each family (|D|* = exp of the largest log|D| at which a certificate exists):")
closing = {}
for de in (0.1, 0.05, 0.01, 0.001, 1e-4, 1e-6):
    row = {}
    for fam in fams:
        L, p = best_close(fam, de); row[fam] = (math.exp(L), p)
    closing[de] = row
    say("  delta=%-7g gauss |D|*=%9.2f (sigma %.4f) ; poisson %9.2f (a %.4f) ; fejer %9.2f (T %.4f)" % (de, row["gauss"][0], row["gauss"][1], row["poisson"][0], row["poisson"][1], row["fejer"][0], row["fejer"][1]))
out["closing_single"] = {str(k): v for k, v in closing.items()}
say("  (the sup over the whole cone tends to D1 = %.3f as delta -> 0 by the argument of check-O item 2)" % out["D1"])
# pole-cap ratio for the families
mx = 0
for fam in fams:
    for p in np.exp(np.linspace(math.log(fams[fam]["rng"][0]), math.log(fams[fam]["rng"][1]), 12)):
        for de in (0.1, 0.01, 0.001):
            mx = max(mx, share_f(fams[fam], p, de) / (2 * fams[fam]["w0"](p)))
say("pole cap: max over families (12 params each) and delta in {0.1,0.01,0.001} of share/(2 what(0)) = %.6f" % mx)
# double zero: delta_max(|D|) for Gaussian and pure Poisson (compare dlVP-Poisson above)
say("double real zero, delta_max * log|D| by family (best parameter):")
dbl = []
for absD in (1e3, 1e6, 1e10, 1e20, 1e40, 1e80, 1e160):
    L = math.log(absD); row = {}
    for fam in ("gauss", "poisson"):
        f = lambda de: best_close(fam, de, mult=2)[0] - L
        row[fam] = 0.5 if f(0.4999) > 0 else brentq(f, 1e-7, 0.4999, xtol=1e-10)
    dbl.append(dict(D=absD, **row))
    say("  |D| = %g: gauss %.4f ; pure poisson %.4f" % (absD, row["gauss"] * L, row["poisson"] * L))
out["double"] = dbl
say("  Cauchy-limit asymptotes (check-O item 3): gauss pi/4 = %.4f ; pure poisson 1/2" % (math.pi / 4))

# ---------- scout section 3 spot checks (dlVP with a planted real zero) ----------
def dh_complex(absD, t, d0):
    def f(de):
        def m(e):
            a = 0.5 + e; y = 0.5 - de
            shO = 4 * sum(c * rpi(a, (1 + k) * t, y) for k, c in C.items())
            return shO - (B_dlvp(e, t, absD) - share_real(e, t, d0))
        return best_eta(m, 1e-7, 3.0)[0]
    return 0.5 if f(0.4999) > 0 else brentq(f, 1e-9, 0.4999, xtol=1e-13)
for (absD, t, d0) in ((1e6, 1e3, 1e-3), (1e6, 28, 1e-6), (20, 1e4, 1e-2), (20, 28, None)):
    if d0 is None:
        def f(de):
            return best_eta(lambda e: 4 * sum(c * rpi(0.5+e, (1+k)*t, 0.5-de) for k, c in C.items()) - B_dlvp(e, t, absD), 1e-7, 3.0)[0]
        d = brentq(f, 1e-9, 0.4999, xtol=1e-13)
    else:
        d = dh_complex(absD, t, d0)
    say("section 3 spot check |D|=%g t=%g delta0=%s: delta_max log(|D|(2+t)) = %.4f" % (absD, t, d0, d * math.log(absD * (2 + t))))
def dh_second(absD, d0):
    f = lambda d1: best_eta(lambda e: share_real(e, 0, d1) - (B_dlvp(e, 0, absD) - share_real(e, 0, d0)), 1e-9, 3.0)[0]
    return 0.5 if f(0.4999) > 0 else brentq(f, 1e-10, 0.4999, xtol=1e-13)
for (absD, d0) in ((1e6, 1e-1), (1e6, 1e-6), (1e12, 1e-6)):
    d1 = dh_second(absD, d0); say("section 3 second real zero |D|=%g delta0=%g: delta1_max = %.5f ; delta1_max log|D| = %.4f" % (absD, d0, d1, d1 * math.log(absD)))
for absD in (1e6, 1e12):
    L = math.log(absD); d1 = brentq(lambda x: 16/x + 16/(1-x) - (8*L - 8*(2*LOG2 + 2*LOGPI - 2*float(mp.digamma(1)))), 1e-6, 0.5)
    say("  saturation root 16/d + 16/(1-d) = 8 log|D| - %.4f at |D|=%g: %.5f" % (8*(2*LOG2 + 2*LOGPI - 2*float(mp.digamma(1))), absD, d1))

# ---------- (D_{0,y}) with my zeros ----------
z = json.load(open(__file__.replace("o2_planted_margins.py", "o1_identity_thresholds_out.json")))["L_zeros"]
zz = [float(mp.im(mp.zetazero(n))) for n in range(1, 41)]
allz = np.array(z + zz)
S = np.arange(0, 4.0001, 0.001)
PsiS = np.array([np.sum(1/np.cosh(np.pi*(s - allz))) + np.sum(1/np.cosh(np.pi*(-s - allz))) for s in S])
for de in (0.1, 0.05, 0.02, 0.01, 0.5):
    lhs = np.array([2 * mu(s, de) for s in S]); bad = S[lhs > PsiS]
    say("(D_{0,y}) delta=%.2f: 2 mu_y(0) = %.4f vs Psi_K(0)+Psi_K(-0) = %.4e ; violated on s in [%.3f, %.3f]" % (de, 2*mu(0, de), PsiS[0], bad.min(), bad.max()))
say("done in %.1fs" % (time.time() - T0))
json.dump(out, open(__file__.replace(".py", "_out.json"), "w"), indent=1, default=str)
open(__file__.replace(".py", "_run.log"), "w").write("\n".join(LOG) + "\n")
