#!/usr/bin/env python3
"""planted_real_zero_fix.py -- Session 24 fix pass (Fable 5.1) for siegel-world-scout.md, from check-O.md items 2-5 and 7.

Own code; the originals planted_real_zero.py / dh_repulsion.py are untouched. Every number the fix pass writes into the
report comes from a line of planted_real_zero_fix_run.log (cited as "fix:<line>").

Blocks (in log order):
 [1] a_K closed form (1/pi)[Re psi(1/2 + is/2) - log pi] + log|D|/2pi against quadrature of mu_0 * A_K in the two-digamma
     form of section 0; D_1 = 16 pi^2 e^{2 gamma}, D_0 = 64 pi^2 e^{2 gamma}; the even-character thresholds D_1^+, D_0^+;
     a_K(0) at D = -20, the root of a_K and the negative mass (check-O item 2).
 [2] the constant of the double-zero ledger: 2 gamma + 2 log 2 + 2 log pi = 4.8302, hence "log|D| - 6.830" (check-O item 3(d));
     the saturation roots of 16/d + 16/(1-d) = 8 log|D| - 8*4.8302 at |D| = 1e6, 1e12.
 [3] Part B of the scout rerun with the archimedean integral over the FULL line (closed-form a_K, adaptive quadrature),
     same 31-element family, same conductors (-20, -4, 2005, 1e6) and the reach-vs-|D| block (check-O item 3(e)).
 [4] closing conductor |D|* for ONE real zero, continuous Gaussian / pure-Poisson / Fejer families (check-O item 3(b)).
 [5] double real zero: delta_max * log|D| for the dlVP-Poisson element, the pure Poisson family and the Gaussian family,
     with the three Cauchy-limit asymptotes (check-O item 3(c)).
 [6] positive control (dlVP, single zero, |D| >= D_1) with the wider window eta in [1e-5, 3], delta in [1e-6, 1/2] (item 7.7).
 [7] section 3 classical column in the table's units: (2/3) log(1/delta_0) and, in Heath-Brown's normalization
     delta_HB = delta_0 log|D|, (2/3) log(1/(delta_0 log|D|)) (check-O item 4(c)).
 [8] growth of the low-zero share: Z_K(w_B) = B_K - P_K at fundamental discriminants -p, p = 3 mod 4 (check-O item 5(a)).
Budget: one process, a few minutes.
"""
import json, math, sys, time
import numpy as np
import mpmath as mp
import sympy
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar
from scipy.special import digamma as sdg, erfcx

T0 = time.time(); LOG = []; OUT = {}
def say(s):
    print(s, flush=True); LOG.append(s)
LOGPI = math.log(math.pi); LOG2 = math.log(2.0); GAM = float(mp.euler)
DELTAS = (0.1, 0.05, 0.02, 0.01, 0.001)

# ---------------- kernels and the archimedean density ----------------
def mu(s, de):
    """mu_y(s) with y = 1/2 - delta: sin(pi delta) cosh(pi s) / (sinh^2(pi s) + sin^2(pi delta)); mu(0) = 1/sin(pi delta)."""
    sd = math.sin(math.pi * de)
    if math.pi * abs(s) > 300: return 2 * sd * math.exp(-math.pi * abs(s))
    sh = math.sinh(math.pi * s)
    return sd * math.cosh(math.pi * s) / (sh * sh + sd * sd)
def aK(s, absD):
    """closed form of (mu_0 * A_K)(s) for chi_D odd (check-O item 2, sharpening 1)."""
    return (float(np.real(sdg(0.5 + 0.5j * s))) - LOGPI) / math.pi + math.log(absD) / (2 * math.pi)
def aK_quad_twodigamma(s, absD):
    """direct quadrature of mu_0 * A_K with A_K in the scout's two-digamma form (section 0, (0.3_K))."""
    f = lambda r: (1 / math.cosh(math.pi * (s - r))) * (float(np.real(sdg(0.25 + 0.5j * r))) + float(np.real(sdg(0.75 + 0.5j * r))) - 2 * LOGPI + math.log(absD)) / (2 * math.pi)
    return quad(f, s - 40, s + 40, limit=600, epsabs=1e-13, epsrel=1e-12)[0]
def I(f, lo, hi, pts):
    pts = sorted(set(p for p in pts if lo < p < hi)); edges = [lo] + pts + [hi]
    return sum(quad(f, a, b, limit=400, epsabs=1e-13, epsrel=1e-11)[0] for a, b in zip(edges[:-1], edges[1:]))
def brk(de):
    return [de, 3 * de, 10 * de, 30 * de, 100 * de, 0.3, 1.0, 3.0, 10.0]

# ---------------- [1] closed form, thresholds ----------------
say("[1] a_K closed form vs quadrature of mu_0 * A_K (two-digamma form), D = -20:")
mx = 0.0
for s in (0.0, 0.3, 1.0, 1.5384, 3.0, 10.0, 40.0):
    c, q = aK(s, 20), aK_quad_twodigamma(s, 20); mx = max(mx, abs(c - q))
    say("    s = %6.4f: closed %.12f quad %.12f diff %.1e" % (s, c, q, c - q))
say("    max |closed - quad| = %.2e" % mx); OUT["aK_closed_vs_quad_maxdiff"] = mx
D1 = 16 * math.pi ** 2 * math.exp(2 * GAM); D0 = 64 * math.pi ** 2 * math.exp(2 * GAM)
D1_psi = math.pi ** 2 * math.exp(-2 * float(mp.digamma(0.5)))
say("D_1 = 16 pi^2 e^{2 gamma} = %.6f ; pi^2 e^{-2 psi(1/2)} = %.6f ; a_K(0; D_1) = %.1e" % (D1, D1_psi, aK(0.0, D1)))
say("D_0 = 64 pi^2 e^{2 gamma} = %.6f ; exp(2 log pi - psi(1/4) - psi(3/4)) = %.6f ; D_0 / D_1 = %.12f" % (D0, math.exp(2 * LOGPI - float(mp.digamma(0.25) + mp.digamma(0.75))), D0 / D1))
# even character (D > 0): bracket 2 Re psi(1/4 + ir/2) - 2 log pi + log D; a_K^+(0) = int mu_0 (2 Re psi(1/4+ir/2))/(2pi) - log pi / pi + log D / 2pi
I_even = quad(lambda r: 2 / math.cosh(math.pi * r) * 2 * float(np.real(sdg(0.25 + 0.5j * r))), 0, 40, limit=400, epsabs=1e-13)[0]
D1p = math.exp(2 * LOGPI - I_even); D0p = math.pi ** 2 * math.exp(-2 * float(mp.digamma(0.25)))
say("D > 0 (chi_D even, two Gamma_R(s) factors): D_1^+ = exp(2 log pi - int mu_0 . 2 Re psi(1/4 + ir/2)) = %.2f ; D_0^+ = pi^2 e^{-2 psi(1/4)} = %.1f" % (D1p, D0p))
OUT.update(D1=D1, D0=D0, D1_plus=D1p, D0_plus=D0p)
aK0 = aK(0.0, 20); AK0 = (2 * float(mp.digamma(0.5)) - 2 * LOGPI - 2 * LOG2 + math.log(20)) / (2 * math.pi)
root = brentq(lambda s: aK(s, 20), 0.5, 3.0, xtol=1e-12)
negmass = 2 * quad(lambda s: -aK(s, 20), 0, root, limit=200, epsabs=1e-13)[0]
say("D = -20: A_K(0) = %.6f ; a_K(0) = %.6f ; a_K < 0 exactly on |s| < %.4f ; negative mass %.6f" % (AK0, aK0, root, negmass))
OUT.update(aK0_D20=aK0, AK0_D20=AK0, aK_root_D20=root, negmass_D20=negmass)
# a_K increasing in |s|: derivative of Re psi(1/2 + is/2) in s is positive for s > 0 (series); sampled sign check
ds = 1e-6; mono = all(aK(s + ds, 20) > aK(s, 20) for s in np.linspace(0.0, 50, 501))
say("a_K strictly increasing on s in [0, 50] (sampled at 501 points, step 1e-6 forward difference): %s" % mono)

# ---------------- [2] the ledger constant and the saturation roots ----------------
C48 = 2 * GAM + 2 * LOG2 + 2 * LOGPI
say("[2] ledger constant 2 gamma + 2 log 2 + 2 log pi = %.4f ; double-zero ledger at eta, delta -> 0: 32/(eta + delta) + 32 > 16/eta + 16 + 8(log|D| - %.4f), i.e. 32/(eta + delta) > 16/eta + 8(log|D| - %.3f)" % (C48, C48, C48 + 2))
say("    asymptote: z < x(2 - x)/(2 + x), max at x = 2 sqrt2 - 2 = %.4f, z* = 6 - 4 sqrt2 = %.6f" % (2 * math.sqrt(2) - 2, 6 - 4 * math.sqrt(2)))
OUT["ledger_constant"] = C48
for absD in (1e6, 1e12):
    rhs = 8 * math.log(absD) - 8 * C48
    r = brentq(lambda d: 16 / d + 16 / (1 - d) - rhs, 1e-6, 0.5 - 1e-9)
    say("    saturation root of 16/d + 16/(1 - d) = 8 log|D| - %.4f at |D| = %g: d = %.5f ; d log|D| = %.4f" % (8 * C48, absD, r, r * math.log(absD)))
    OUT["saturation_root_%g" % absD] = r

# ---------------- [3] Part B rerun, full-line archimedean integral ----------------
def families():
    for T in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0):
        yield "Fejer T=%g" % T, (lambda s, T=T: max(0.0, 1 - abs(s) / T)), 1.0, T, T
        yield "Fejer^2 T=%g" % T, (lambda s, T=T: max(0.0, 1 - abs(s) / T) ** 2), 1.0, 2 * T / 3, T
    for sg in (0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0):
        yield "Gauss sigma=%g" % sg, (lambda s, sg=sg: math.exp(-s * s / (2 * sg * sg))), 1.0, sg * math.sqrt(2 * math.pi), 14 * sg
    for a in (0.55, 0.6, 0.75, 1.0, 1.5, 2.0):
        yield "Poisson a=%g" % a, (lambda s, a=a: 2 * a / (a * a + s * s)), 2 / a, 2 * math.pi, math.inf
def share_w(wf, de, hi):
    return 4 * I(lambda s: wf(s) * mu(s, de), 0, hi, brk(de) + ([hi] if hi != math.inf else []))
def arch1_w(wf, hi):
    """int what(s) (1/pi)[Re psi(1/2 + is/2) - log pi] ds over the full line (|D| = 1); add log|D| int what / 2pi for |D|."""
    return 2 * I(lambda s: wf(s) * (float(np.real(sdg(0.5 + 0.5j * s))) - LOGPI) / math.pi, 0, hi, [0.5, 2, 10, 30])
FAM = [(name, wf, w0, mass, hi) for name, wf, w0, mass, hi in families()]
say("[3] Part B rerun: %d elements; share = 2 int what mu_y (adaptive), Arch_K(w) = int what a_K over the FULL line (closed-form a_K)" % len(FAM))
A1 = {name: arch1_w(wf, hi) for name, wf, w0, mass, hi in FAM}
SH = {(name, de): share_w(wf, de, hi) for name, wf, w0, mass, hi in FAM for de in DELTAS}
capmax = max(SH[(name, de)] / (2 * w0) for name, wf, w0, mass, hi in FAM for de in DELTAS)
say("    pole-cap check: max over the family and delta of share/(2 what(0)) = %.6f" % capmax); OUT["partB_capmax"] = capmax
# Poisson closed-form cross-checks: arch1 = 2[psi(1/2 + a/2) - log pi]; share = 4 pi / cos(pi(a - y)) ... u-space: 4 int_0^inf e^{-a u} cosh(y u)/cosh(u/2) du
for a in (0.55, 0.6):
    name = "Poisson a=%g" % a
    say("    Poisson a=%.2f cross-check: arch1 quad %.10f closed 2[psi(1/2 + a/2) - log pi] %.10f ; share(0.1) xi-quad %.10f u-space %.10f"
        % (a, A1[name], 2 * (float(mp.digamma(0.5 + a / 2)) - LOGPI), SH[(name, 0.1)], 4 * float(mp.quad(lambda u: mp.exp(-a * u) * mp.cosh(0.4 * u) / mp.cosh(u / 2), [0, mp.inf]))))
partB = {}
def run_family(absD, label):
    L = math.log(absD); rows = {}
    infarch = min((A1[name] + L * mass / (2 * math.pi)) / w0 for name, wf, w0, mass, hi in FAM)
    infname = min(FAM, key=lambda e: (A1[e[0]] + L * e[3] / (2 * math.pi)) / e[2])[0]
    say("    Part B [%s]: inf over the family of Arch_K(w)/what(0) = %+.6f (%s)" % (label, infarch, infname))
    for de in DELTAS:
        best = (-math.inf, None); bestd = (-math.inf, None)
        for name, wf, w0, mass, hi in FAM:
            arch = A1[name] + L * mass / (2 * math.pi); sh = SH[(name, de)]
            m1 = sh - 2 * w0 - arch; m2 = 2 * sh - 2 * w0 - arch
            if m1 > best[0]: best = (m1, name)
            if m2 > bestd[0]: bestd = (m2, name)
        rows[str(de)] = dict(single=best[0], single_elem=best[1], double=bestd[0], double_elem=bestd[1])
        say("      delta = %6.3f: best single margin %+.5f [%s] %s ; best double margin %+.5f [%s] %s"
            % (de, best[0], best[1], "FIRES" if best[0] > 0 else "silent", bestd[0], bestd[1], "FIRES" if bestd[0] > 0 else "silent"))
    return rows
partB["D20"] = run_family(20, "D = -20")
partB["D4"] = run_family(4, "D = -4")
partB["D2005"] = run_family(2005, "|D| = 2005 (positive control)")
partB["D1e6"] = run_family(1e6, "|D| = 1e6 (positive control)")
# the scout's printed Poisson entries, full line vs truncated to |s| <= 20
say("    the scout's Poisson entries at D = -20, full-line Arch vs Arch truncated to |s| <= 20 (the scout's grid Sg):")
for a, des in ((0.6, (0.1,)), (0.55, (0.05, 0.02, 0.01, 0.001))):
    name = "Poisson a=%g" % a; wf = lambda s, a=a: 2 * a / (a * a + s * s)
    tail = 2 * quad(lambda s: wf(s) * aK(s, 20), 20, math.inf, limit=400, epsabs=1e-13)[0]
    for de in des:
        full = SH[(name, de)] - 2 * (2 / a) - (A1[name] + math.log(20))
        say("      Poisson a=%.2f delta=%.3f: margin full %+.5f ; truncated %+.5f ; Arch tail |s| > 20 = %.5f" % (a, de, full, full + tail, tail))
for absD in (2005, 1e6):
    name = "Poisson a=0.55"
    for de in (0.1, 0.001):
        m2 = 2 * SH[(name, de)] - 2 * (2 / 0.55) - (A1[name] + math.log(absD))
        say("      double, |D| = %g, Poisson a=0.55 delta=%.3f: margin full %+.5f" % (absD, de, m2))
OUT["partB"] = partB
say("    reach vs |D| (best single margin / what(0) over the 31-element family, full-line Arch):")
SH2 = {(name, de): share_w(wf, de, hi) for name, wf, w0, mass, hi in FAM for de in (0.1, 0.01) if (name, de) not in SH}
SH.update(SH2)
reach = []
for absD in (3, 4, 7, 8, 11, 15, 19, 20, 23, 24, 40, 100, 200, 300, 500, 1000, 2000, 2005, 5000):
    L = math.log(absD); row = dict(absD=absD)
    for de in (0.1, 0.01):
        b = max(((SH[(name, de)] - 2 * w0 - (A1[name] + L * mass / (2 * math.pi))) / w0, name) for name, wf, w0, mass, hi in FAM)
        row["delta_%g" % de] = b[0]; row["elem_%g" % de] = b[1]
    reach.append(row)
    say("      reach vs |D| = %5d: best single margin/what(0) at delta = 0.1: %+.5f [%s], at delta = 0.01: %+.5f [%s]" % (absD, row["delta_0.1"], row["elem_0.1"], row["delta_0.01"], row["elem_0.01"]))
OUT["reach_vs_D"] = reach

# ---------------- [4] closing conductor, continuous families ----------------
CF = {
    "gauss":   (lambda s, p: math.exp(-s * s / (2 * p * p)), lambda p: 1.0, lambda p: p * math.sqrt(2 * math.pi), lambda p: 14 * p, (1e-4, 5.0)),
    "poisson": (lambda s, p: 2 * p / (p * p + s * s), lambda p: 2 / p, lambda p: 2 * math.pi, lambda p: math.inf, (1e-4, 5.0)),
    "fejer":   (lambda s, p: max(0.0, 1 - abs(s) / p), lambda p: 1.0, lambda p: p, lambda p: p, (0.05, 12.0)),
}
cache = {}
def logD_close(fam, p, de, mult=1):
    wh, w0, mass, hi, rng = CF[fam]; key = (fam, round(p, 12), de)
    if key not in cache:
        H = hi(p); cache[key] = (share_w(lambda s: wh(s, p), de, H), arch1_w(lambda s: wh(s, p), H))
    sh, a1 = cache[key]
    return 2 * math.pi * (mult * sh - 2 * w0(p) - a1) / mass(p)
def best_close(fam, de, mult=1, npts=60):
    lo, hi = CF[fam][4]
    xs = np.exp(np.linspace(math.log(lo), math.log(hi), npts)); v = [logD_close(fam, x, de, mult) for x in xs]; i = int(np.argmax(v))
    r = minimize_scalar(lambda x: -logD_close(fam, x, de, mult), bounds=(xs[max(i - 1, 0)], xs[min(i + 1, npts - 1)]), method="bounded", options={"xatol": 1e-7})
    return (max(-r.fun, v[i]), r.x if -r.fun >= v[i] else xs[i])
say("[4] closing conductor for ONE real zero, best element of each continuous family (|D|* = exp of the largest log|D| at which a certificate exists):")
closing = {}
for de in (0.1, 0.05, 0.01, 0.001, 1e-4, 1e-6):
    row = {}
    for fam in CF:
        Lc, p = best_close(fam, de); row[fam] = (math.exp(Lc), p)
    closing[str(de)] = row
    say("    delta = %-7g: gauss |D|* = %8.2f (sigma %.4f) ; poisson %8.2f (a %.4f) ; fejer %8.2f (T %.4f)" % (de, row["gauss"][0], row["gauss"][1], row["poisson"][0], row["poisson"][1], row["fejer"][0], row["fejer"][1]))
say("    (sup over the cone tends to D_1 = %.3f as delta -> 0: check-O item 2, sharpening 2)" % D1)
OUT["closing_single"] = closing

# ---------------- [5] double real zero: three families ----------------
def B_dlvp0(eta, absD):
    s = 1 + eta
    return 8 * (2 * (1 / (s - 1) + 1 / s) + float(mp.digamma(s / 2)) + float(mp.digamma((s + 1) / 2)) - 2 * LOGPI + math.log(absD))
def share_dlvp0(eta, de):
    a = 0.5 + eta; y = 0.5 - de
    return 16 * (1 / (a + y) + 1 / (a - y))
def best_eta(f, lo=1e-5, hi=3.0):
    xs = np.exp(np.linspace(math.log(lo), math.log(hi), 400)); v = [f(x) for x in xs]; i = int(np.argmax(v))
    r = minimize_scalar(lambda x: -f(x), bounds=(xs[max(i - 1, 0)], xs[min(i + 1, 399)]), method="bounded", options={"xatol": 1e-12})
    return (max(-r.fun, v[i]), r.x if -r.fun >= v[i] else xs[i])
def dmax_dlvp_double(absD):
    f = lambda de: best_eta(lambda e: 2 * share_dlvp0(e, de) - B_dlvp0(e, absD))[0]
    if f(0.4999) > 0: return 0.5
    return brentq(f, 1e-7, 0.4999, xtol=1e-10)
say("[5] double real zero, delta_max * log|D| (largest excluded depth times log|D|):")
dbl = {}
for absD in (1e3, 1e4, 1e6, 1e10, 1e20, 1e40, 1e80):
    d = dmax_dlvp_double(absD); dbl["dlvp_%g" % absD] = d
    say("    dlVP-Poisson (w = 8 e^{-a|u|} cosh(u/2)), |D| = %g: delta_max = %.6f ; delta_max log|D| = %.4f" % (absD, d, d * math.log(absD)))
for absD in (1e3, 1e6, 1e10, 1e20, 1e40, 1e80, 1e160):
    L = math.log(absD); row = {}
    for fam in ("gauss", "poisson"):
        f = lambda de: best_close(fam, de, mult=2, npts=40)[0] - L
        row[fam] = 0.5 if f(0.4999) > 0 else brentq(f, 1e-7, 0.4999, xtol=1e-10)
    dbl["fam_%g" % absD] = row
    say("    |D| = %g: Gaussian delta_max log|D| = %.4f ; pure Poisson (w = e^{-a|u|}) %.4f" % (absD, row["gauss"] * L, row["poisson"] * L))
zr = minimize_scalar(lambda z: -(2 * math.sqrt(math.pi) * z * (4 * erfcx(z) - 2)), bounds=(1e-3, 3), method="bounded", options={"xatol": 1e-12})
say("    Cauchy-limit asymptotes: dlVP-Poisson 6 - 4 sqrt2 = %.6f ; pure Poisson 12 - 8 sqrt2 = %.6f ; Gaussian max_z 2 sqrt(pi) z (4 e^{z^2} erfc z - 2) = %.6f at z = %.4f"
    % (6 - 4 * math.sqrt(2), 12 - 8 * math.sqrt(2), -zr.fun, zr.x))
OUT["double"] = dbl; OUT["gauss_asymptote"] = -zr.fun

# ---------------- [6] positive control with the wider window ----------------
say("[6] positive control, dlVP single real zero, sup over delta in [1e-6, 1/2] (120 log-spaced points) and eta in [1e-5, 3]:")
for absD in (501, 2005, 1e6, 1e12):
    sup = max(best_eta(lambda e: share_dlvp0(e, de) - B_dlvp0(e, absD))[0] for de in np.exp(np.linspace(math.log(1e-6), math.log(0.5), 120)))
    OUT["poscontrol_%g" % absD] = sup
    say("    |D| = %g: sup of the single-zero margin = %+.4f -> %s" % (absD, sup, "silent" if sup < 0 else "FIRED"))
say("    (the scout's window eta in [1e-3, 1], delta in {0.1, 0.05, 0.02, 0.01, 0.001, 0.3, 0.5} gave -26.17, -75.86, -186.39 at 2005, 1e6, 1e12: planted_real_zero_run.log lines 29-31)")

# ---------------- [7] the section 3 classical column, correct units ----------------
say("[7] section 3 table, classical column in the table's units delta * log(|D|(2 + t)):")
say("    (2/3) log(1/delta_0) at delta_0 = 1e-3 / 1e-6: %.3f / %.3f (independent of the row)" % (2 / 3 * math.log(1e3), 2 / 3 * math.log(1e6)))
cone = {(20, 28): (3.198, 3.198), (20, 1e3): (1.032, 1.469), (20, 1e4): (0.838, 1.243), (1e6, 28): (0.821, 1.274), (1e6, 1e3): (0.694, 1.134), (1e6, 1e4): (0.640, 1.079)}
col = {}
for (absD, t), (c3, c6) in cone.items():
    hb3 = 2 / 3 * math.log(1 / (1e-3 * math.log(absD))); hb6 = 2 / 3 * math.log(1 / (1e-6 * math.log(absD)))
    col["%g,%g" % (absD, t)] = dict(hb3=hb3, hb6=hb6)
    say("    (|D|, t) = (%g, %g): HB-normalized (2/3) log(1/(delta_0 log|D|)) = %.2f / %.2f ; cone column (dh_repulsion_run.log) %.3f / %.3f ; ratio classical/cone (plain units) %.2f / %.2f, (HB units) %.2f / %.2f"
        % (absD, t, hb3, hb6, c3, c6, 2 / 3 * math.log(1e3) / c3, 2 / 3 * math.log(1e6) / c6, hb3 / c3, hb6 / c6))
OUT["classical_column"] = col

# ---------------- [8] growth of the low-zero share with |D| ----------------
def kron(D, n):
    """Kronecker symbol (D/n), D a fundamental discriminant, n >= 1."""
    r = 1
    for p, e in sympy.factorint(n).items():
        if p == 2:
            v = 0 if D % 2 == 0 else (1 if D % 8 in (1, 7) else -1)
        else:
            v = sympy.legendre_symbol(D % p, p) if D % p else 0
        r *= v ** e
    return r
NM = 4000
nn = np.arange(2, NM + 1)
lam = np.zeros(NM + 1)
for p in sympy.primerange(2, NM + 1):
    q = p
    while q <= NM: lam[q] = math.log(p); q *= p
wB0 = math.sqrt(math.pi / 2)             # what_B(0) for w_B = e^{-2u^2}; what_B(s) = sqrt(pi/2) e^{-s^2/8}, int what_B = 2 pi
wlB = np.exp(-2 * np.log(nn) ** 2)
say("[8] Z_K(w_B) = B_K - P_K, w_B = e^{-2u^2} (w(0) = 1, int what_B = 2 pi); B_K = 2 what_B(0) + int what_B a_K (closed-form a_K); P_K = 4 sum Lambda_K(n) w_B(log n)/(n + 1), n <= %d:" % NM)
archB1 = 2 * quad(lambda s: wB0 * math.exp(-s * s / 8) * (float(np.real(sdg(0.5 + 0.5j * s))) - LOGPI) / math.pi, 0, 60, limit=400, epsabs=1e-13)[0]
growth = []
for p in (20, 10007, 1000003, 100000007, 10 ** 10 + 19, 10 ** 12 + 39, 10 ** 16 + 63):
    if p == 20: Dd = -20
    else:
        q = sympy.nextprime(p - 1)
        while q % 4 != 3: q = sympy.nextprime(q)
        Dd = -int(q)
    chi = np.array([kron(Dd, int(n)) for n in nn], dtype=float)
    lamK = lam[2:] * (1 + chi)
    BK = 2 * wB0 + archB1 + math.log(abs(Dd))       # int what_B . log|D|/(2 pi) = log|D| . w(0) = log|D|
    PK = 4 * float(np.sum(lamK * wlB / (nn + 1)))
    ZK = BK - PK
    growth.append(dict(D=Dd, B_K=BK, P_K=PK, Z_K=ZK, mean=ZK / (4 * math.pi)))
    say("    D = %d: B_K %.4f P_K %.4f Z_K %.4f ; what_B-weighted mean of the zero density Z_K/(2 int what_B) = %.4f ; log|D|/(4 pi) = %.4f" % (Dd, BK, PK, ZK, ZK / (4 * math.pi), math.log(abs(Dd)) / (4 * math.pi)))
say("    (D = -20 control: the scout's siegel_setup_run.log prints B_K 2.021456839, Z_K 1.452311179 for w_B; the bound Z_K >= w(0) log|D| - C with C = 2 P_zeta(w_B) - 2 what_B(0) - archB1 = %.4f)" % (2 * 4 * float(np.sum(lam[2:] * wlB / (nn + 1))) - 2 * wB0 - archB1))
OUT["growth"] = growth
OUT["runtime_s"] = time.time() - T0
say("done in %.1fs" % (time.time() - T0))
base = __file__[:-3]
open(base + "_run.log", "w").write("\n".join(LOG) + "\n")
json.dump(OUT, open(base + "_out.json", "w"), indent=1, default=float)
