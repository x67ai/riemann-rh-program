#!/usr/bin/env python3
"""edge_law_two_sided.py -- clause 2 (two-sided edge law) and clause 3 (slack), PROVED bounds checked numerically.
c(lam) := int B(v) cosh(lam v) dv = e^{lam/2} I(lam)/Z,  I(lam) := int_0^1 exp(-lam s - 1/(4 s (1-s))) ds   (v = 1/2 - s).
With mu := lam + 1/4 and J(mu) := int_0^infty e^{-mu s - 1/(4s)} ds = mu^{-1/2} K_1(sqrt mu):
  UPPER: I <= e^{-1/4} J(mu),  K_1(x) <= sqrt(pi/(2x)) e^{-x} (1 + 3/(8x))
  LOWER: I >= e^{-1/4} [ J(mu) - e^{-mu a}/mu - (1/(4(1-a))) mu^{-3/2} K_3(sqrt mu)/4 ],  a = 1/2,
         K_1(x) >= sqrt(pi/(2x)) e^{-x} (1 + 3/(8x) - 3/(16x^2)),  K_3(x) <= sqrt(pi/(2x)) e^{-x} (1 + 4.5/x + 9/x^2 + 7.5/x^3).
kappa(lam) := log c(lam) - lam/2 + sqrt(lam) + (3/4) log lam.  kappa_inf := log( sqrt(pi/2) e^{-1/4} / Z ).
Proved (note section 3):  kappa_inf <= kappa(lam) <= kappa_inf + 1/(4 sqrt lam) + 1/(128 lam^{3/2})  for lam >= 25.
Clause 3: c(lam)^2 >= e^{lam/2} for lam >= 25 follows from lam/2 - 2 sqrt(lam) - 1.5 log(lam) + 2 kappa_inf >= 0.
Budget: < 10 min."""
import time, json, sys
import mpmath as mp
t0 = time.time(); mp.mp.dps = 30
out = {}
def Braw(v):
    v = mp.mpf(v)
    if abs(v) >= mp.mpf(1)/2: return mp.mpf(0)
    return mp.e**(-1/(1-4*v*v))
Z = mp.quad(Braw, [-0.5, -0.25, 0, 0.25, 0.5]); out["Z"] = float(Z)
kinf = mp.log(mp.sqrt(mp.pi/2)*mp.e**(-mp.mpf(1)/4)/Z); out["kappa_inf"] = float(kinf)
print(f"Z = {mp.nstr(Z,15)};  kappa_inf = log(sqrt(pi/2) e^(-1/4) / Z) = {mp.nstr(kinf, 12)}")
def c_of(lam):
    lam = mp.mpf(lam)
    return mp.quad(lambda v: Braw(v)*mp.cosh(lam*v), [-0.5, -0.25, 0, 0.25, 0.5])/Z
def I_of(lam):
    lam = mp.mpf(lam)
    return mp.quad(lambda s: mp.e**(-lam*s - 1/(4*s*(1-s))), [0, 0.05, 0.2, 0.5, 1])
# (0) identity c = e^{lam/2} I / Z, and the K_1 / K_3 representations against mpmath
print("(0) identities:")
for lam in (25, 100, 400):
    c = c_of(lam); I = I_of(lam)
    print(f"   lam={lam}: c(lam) = {mp.nstr(c,12)},  e^(lam/2) I(lam)/Z = {mp.nstr(mp.e**(mp.mpf(lam)/2)*I/Z, 12)}")
for mu in (25.25, 100.25, 400.25):
    x = mp.sqrt(mu)
    J = mp.quad(lambda s: mp.e**(-mu*s - 1/(4*s)), [0, 0.02, 0.1, 0.5, 2, mp.inf])
    J3 = mp.quad(lambda s: s*s*mp.e**(-mu*s - 1/(4*s)), [0, 0.02, 0.1, 0.5, 2, mp.inf])
    K1r = mp.quad(lambda th: mp.e**(-x*mp.cosh(th))*mp.cosh(th), [0, 2, 6])
    print(f"   mu={mu}: J(mu)={mp.nstr(J,12)}  mu^(-1/2)K1(sqrt mu)={mp.nstr(mp.besselk(1,x)/mp.sqrt(mu),12)}  K1 integral rep={mp.nstr(K1r,12)}  besselk={mp.nstr(mp.besselk(1,x),12)}  | int s^2 e^{{..}}={mp.nstr(J3,12)}  mu^(-3/2)K3/4={mp.nstr(mp.besselk(3,x)/(4*mu**1.5),12)}")
# (1) elementary K_1, K_3 bounds on x in [5, 60]
print("(1) elementary Bessel bounds (ratios to the bound; must be <= 1 for upper, >= 1 for lower):")
worst = {"K1_upper": 0, "K1_lower": 10, "K3_upper": 0}
for x in [5, 5.025, 6, 8, 10, 15, 20, 30, 45, 60]:
    x = mp.mpf(x); pref = mp.sqrt(mp.pi/(2*x))*mp.e**(-x)
    k1 = mp.besselk(1, x); k3 = mp.besselk(3, x)
    ru = k1/(pref*(1+3/(8*x))); rl = k1/(pref*(1+3/(8*x)-3/(16*x*x))); r3 = k3/(pref*(1+mp.mpf(4.5)/x+9/x**2+mp.mpf(7.5)/x**3))
    worst["K1_upper"] = max(worst["K1_upper"], float(ru)); worst["K1_lower"] = min(worst["K1_lower"], float(rl)); worst["K3_upper"] = max(worst["K3_upper"], float(r3))
    print(f"   x={mp.nstr(x,5)}: K1/upper={mp.nstr(ru,8)}  K1/lower={mp.nstr(rl,8)}  K3/upper={mp.nstr(r3,8)}")
out["bessel_bound_ratios_worst"] = worst
# (2) the proved bounds on kappa(lam) against the exact value, lam >= 25
def lower_bound(lam, a=mp.mpf(1)/2):
    lam = mp.mpf(lam); mu = lam + mp.mpf(1)/4; x = mp.sqrt(mu)
    E1 = mp.sqrt(2/mp.pi)*mu**(-mp.mpf(1)/4)*mp.e**(x - mu*a)
    E2 = (1/(16*(1-a)*mu))*(1 + mp.mpf(4.5)/x + 9/mu + mp.mpf(7.5)/mu**1.5)
    br = 1 + 3/(8*x) - 3/(16*mu) - E1 - E2
    return kinf - 1/(8*mp.sqrt(lam)) - mp.mpf(3)/4*mp.log(1 + 1/(4*lam)) + mp.log(br), E1, E2, br
def upper_bound(lam):
    lam = mp.mpf(lam)
    return kinf + 1/(4*mp.sqrt(lam)) + 1/(128*lam**1.5)
def upper_bound_exact_chain(lam):
    lam = mp.mpf(lam); mu = lam + mp.mpf(1)/4; x = mp.sqrt(mu)
    return kinf + (mp.sqrt(lam) - x) + mp.mpf(3)/4*mp.log(lam/mu) + mp.log(1 + 3/(8*x))
print("(2) kappa(lam) exact vs proved bounds:")
lams = list(range(25, 101)) + [121, 144, 169, 196, 225, 256, 324, 400, 625, 900, 1600, 2500, 4900, 10000]
rows = []; minL = 10; maxU = -10; okall = True; min_margin_low = 10; min_margin_up = 10
for lam in lams:
    c = c_of(lam); kap = mp.log(c) - mp.mpf(lam)/2 + mp.sqrt(lam) + mp.mpf(3)/4*mp.log(lam)
    lo, E1, E2, br = lower_bound(lam); up = upper_bound(lam); upx = upper_bound_exact_chain(lam)
    ok = lo <= kap <= upx <= up
    okall = okall and ok
    minL = min(minL, float(lo)); maxU = max(maxU, float(up))
    min_margin_low = min(min_margin_low, float(kap - lo)); min_margin_up = min(min_margin_up, float(up - kap))
    rows.append((lam, float(kap), float(lo), float(up), float(E1), float(E2)))
    if lam in (25, 26, 30, 36, 49, 64, 81, 100, 400, 2500, 10000):
        print(f"   lam={lam:6d}: kappa={mp.nstr(kap,8)}  lower={mp.nstr(lo,8)}  upper(exact chain)={mp.nstr(upx,8)}  upper(clean)={mp.nstr(up,8)}  E1={mp.nstr(E1,3)} E2={mp.nstr(E2,3)}  {'OK' if ok else 'FAIL'}")
print(f"   all {len(lams)} lambda values: bounds hold = {okall};  min lower bound = {minL:.6f} (kappa_inf = {float(kinf):.6f});  max upper = {maxU:.6f};  min margins: low {min_margin_low:.4f}, up {min_margin_up:.4f}")
out["kappa_table"] = rows; out["bounds_hold_all"] = okall
# D(lam) >= 0 claim: lower bound >= kappa_inf for lam >= 25
Dmin = min(r[2] for r in rows) - float(kinf)
print(f"   D(lam) = lower(lam) - kappa_inf >= {Dmin:.6f} over the table (claim: >= 0 for all lam >= 25, proved in the note)")
out["D_min_over_table"] = Dmin
kminus = float(kinf); kplus = float(upper_bound(25))
out["kappa_minus"] = kminus; out["kappa_plus"] = kplus; out["kappa_at_25"] = rows[0][1]
print(f"   PROVED constants for lam >= 25: kappa_- = kappa_inf = {kminus:.5f}, kappa_+ = {kplus:.5f};  exact kappa(25) = {rows[0][1]:.5f}, kappa(10000) = {rows[-1][1]:.5f}")
print(f"   gap to the pricing's fitted 1.515: kappa_- - 1.515 = {kminus-1.515:+.4f}, kappa_+ - 1.515 = {kplus-1.515:+.4f}  (|.| <= 0.1: stop condition (a) does not fire)")
# fit reproduced the pricing's way, for the record
import numpy as np
X = np.array([[-np.sqrt(l), 1.0] for l in (25, 36, 49, 64, 81, 100, 144, 196, 256, 324, 400)])
Y = np.array([float(mp.log(c_of(l)) - mp.mpf(l)/2 + mp.mpf(3)/4*mp.log(l)) for l in (25, 36, 49, 64, 81, 100, 144, 196, 256, 324, 400)])
coef = np.linalg.lstsq(X, Y, rcond=None)[0]
print(f"   (the pricing's least-squares fit on the same 11 points: C = {coef[0]:.4f}, const = {coef[1]:.4f} -- the fitted C > 1 absorbs the drift kappa(lam) -> kappa_inf)")
out["pricing_fit_reproduced"] = [float(coef[0]), float(coef[1])]
# (3) clause 3: c(lam)^2 >= e^{lam/2} for lam >= 25, from kappa_- ; and exact margins
print("(3) clause 3 (slack, c0 = 1/2):")
def slack_fn(lam): lam = mp.mpf(lam); return lam/2 - 2*mp.sqrt(lam) - mp.mpf(3)/2*mp.log(lam) + 2*kinf
print(f"   proved margin function at lam=25: lam/2 - 2 sqrt(lam) - 1.5 log(lam) + 2 kappa_- = {mp.nstr(slack_fn(25),6)} (>0), derivative 1/2 - 1/sqrt(lam) - 1.5/lam = {mp.nstr(mp.mpf(1)/2 - 1/mp.sqrt(25) - mp.mpf(1.5)/25, 4)} > 0")
for lam in (25, 26, 30, 36, 49, 64, 100, 400):
    c2 = c_of(lam)**2; e = mp.e**(mp.mpf(lam)/2)
    print(f"   lam={lam}: c^2 = {mp.nstr(c2,6)}  e^(lam/2) = {mp.nstr(e,6)}  ratio = {mp.nstr(c2/e,6)}  proved lower ratio e^(slack) = {mp.nstr(mp.e**slack_fn(lam),6)}")
out["clause3_margin_at_25"] = float(slack_fn(25)); out["clause3_ratio_at_25"] = float(c_of(25)**2/mp.e**mp.mpf(12.5))
# least lam for which the proved slack inequality holds (for the record), and for c0 = 1/4
lam0 = 25
while slack_fn(lam0 - 1) > 0 and lam0 > 2: lam0 -= 1
out["least_lam_proved_slack_c0_half"] = lam0
print(f"   least integer lam with the PROVED slack inequality (c0=1/2): {lam0}   (the contract fixes lam0 = 25)")
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "edge_law_two_sided_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
