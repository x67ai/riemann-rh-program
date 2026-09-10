#!/usr/bin/env python3
"""gevrey_edge_law.py -- sanity computation for candidate M2 (mandatory repair 2).

Bump B(v) = exp(-1/(1-4v^2)) on |v| < 1/2 (the transcript's tx_032 bump; Gevrey order alpha = 2, the class
Zeta23/Taper/Gevrey.lean formalizes for the profile expNegInvGlue), normalized to int B = 1.
B_L(u) = B(u/L)/L, so hat B_L(x) = hat B(Lx) and

  c(lam) := hat B_L(i delta) = int B_L(u) cosh(delta u) du = int B(v) cosh(lam v) dv,   lam = delta L.

Checks:
  (a) the corrected edge law  c(lam) = e^{lam/2} exp(-C lam^{1/2} + o(lam^{1/2}))  (killer, C2 line 70; repair 2, line 74):
      fit  log c(lam) - lam/2  against  -C sqrt(lam) - (3/4) log lam + const  (Laplace saddle: s* = 1/(2 sqrt lam),
      exponent -sqrt(lam), prefactor ~ lam^{-3/4});
  (b) the polynomial-edge law of the design (C2 line 18) would be  e^{lam/2} (c/lam)^{k+1}  -- shown NOT to hold for this B;
  (c) the slack: 2 C sqrt(lam) <= c0 lam  iff  lam >= (2C/c0)^2  -- threshold for c0 in {0.1, 0.25, 0.5};
  (d) transform decay |hat B(eta)| vs exp(-c sqrt(eta)) (Gevrey-2), and b1 = sup |eta hat B(eta)|^2, ||B'||_1;
  (e) the balance of the separation theorem (C2 line 39; tx_032 (iii)):  2 delta^2 c(delta L)^2  >  n1 b1 / L^2
      with n1 = C1 log t, C1 = 1 (a placeholder density constant): the least L for t in {1e3, 1e6, 1e12}, delta in {0.05, 0.1, 0.25},
      against the predicted law L* ~ C0 delta^{-1} (log log t + log(1/delta)).
Budget: < 10 minutes.
"""
import time, json, sys
import numpy as np
import mpmath as mp

t0 = time.time()
out = {}
mp.mp.dps = 30

def Braw(v):
    v = mp.mpf(v)
    if abs(v) >= mp.mpf(1) / 2:
        return mp.mpf(0)
    return mp.e ** (-1 / (1 - 4 * v * v))

Z = mp.quad(Braw, [-0.5, 0, 0.5])
B = lambda v: Braw(v) / Z
out["normalization_Z"] = float(Z)

# (a) c(lam)
lams = [1, 2, 4, 8, 16, 25, 36, 49, 64, 81, 100, 144, 196, 256, 324, 400]
rows = []
for lam in lams:
    c = mp.quad(lambda v: B(v) * mp.cosh(lam * v), [-0.5, -0.25, 0, 0.25, 0.5])
    logc = mp.log(c)
    rows.append((lam, float(c), float(logc - mp.mpf(lam) / 2)))
    print(f"lam={lam:4d}  c={float(c): .6e}  log c - lam/2 = {float(logc - mp.mpf(lam)/2): .5f}   -sqrt(lam) = {-np.sqrt(lam): .5f}   e^{{lam/2}}/c = {float(mp.e**(mp.mpf(lam)/2)/c): .4e}")
out["c_lam"] = rows
# fit: log c - lam/2 = -C sqrt(lam) - (3/4) log lam + const  on lam >= 25
X = np.array([[-np.sqrt(l), 1.0] for l, _, _ in rows if l >= 25])
Y = np.array([y + 0.75 * np.log(l) for l, _, y in rows if l >= 25])
coef, *_ = np.linalg.lstsq(X, Y, rcond=None)
C_fit, const_fit = coef
resid = Y - X @ coef
out["fit_C"] = float(C_fit); out["fit_const"] = float(const_fit); out["fit_max_resid"] = float(np.max(np.abs(resid)))
print(f"fit on lam >= 25:  log c - lam/2 + (3/4) log lam = -{C_fit:.4f} sqrt(lam) + {const_fit:.4f};  max resid {np.max(np.abs(resid)):.4f}  (saddle predicts C = 1)")
# (b) polynomial-edge law test: does (log c - lam/2) behave like -(k+1) log lam + const for any k? compare slopes in log lam
ls = np.array([l for l, _, _ in rows if l >= 25]); ys = np.array([y for l, _, y in rows if l >= 25])
slope_loglam = np.polyfit(np.log(ls), ys, 1)[0]
out["slope_in_log_lam_over_25_400"] = float(slope_loglam)
print(f"(b) if the law were e^(lam/2)(c/lam)^(k+1), log c - lam/2 would be linear in log lam; fitted slope over lam in [25,400] = {slope_loglam:.3f} (and the residual curvature is what the sqrt fit captures)")
# local exponents: d(log c - lam/2)/d(log lam) at successive points
locs = [(ls[i], (ys[i+1]-ys[i])/(np.log(ls[i+1])-np.log(ls[i]))) for i in range(len(ls)-1)]
out["local_log_slopes"] = [(float(a), float(b)) for a, b in locs]
print("   local slopes d(log c - lam/2)/d log lam:", [f"{a:.0f}:{b:.2f}" for a, b in locs])

# (c) slack thresholds
thr = {c0: (2 * C_fit / c0) ** 2 for c0 in (0.1, 0.25, 0.5)}
out["slack_threshold_lam0"] = {str(k): float(v) for k, v in thr.items()}
print("(c) slack absorbs the Gevrey loss (2C sqrt(lam) <= c0 lam) once lam = delta L >= (2C/c0)^2:", {k: round(v, 1) for k, v in thr.items()})
# exact check: for each c0, least lam in table with log c - lam/2 >= -c0 lam/2  (i.e. c^2 >= e^{(1-c0) lam})
for c0 in (0.1, 0.25, 0.5):
    ok = [l for l, _, y in rows if y >= -c0 * l / 2]
    print(f"    exact: c(lam)^2 >= e^((1-{c0}) lam) holds for lam in table >= {min(ok) if ok else None}")
    out[f"exact_least_lam_c0_{c0}"] = min(ok) if ok else None

# (d) transform decay and b1
def Bhat(eta):
    return mp.quad(lambda v: B(v) * mp.cos(eta * v), [-0.5, -0.25, 0, 0.25, 0.5])
etas = [0.5, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
dec = []
for e in etas:
    bh = Bhat(e)
    dec.append((e, float(bh), float(mp.log(abs(bh))) if bh != 0 else None))
    print(f"eta={e:6.1f}  Bhat={float(bh): .4e}   log|Bhat| = {float(mp.log(abs(bh))) if bh!=0 else float('nan'): .3f}   -sqrt(eta) = {-np.sqrt(e): .3f}   -2 sqrt(eta) = {-2*np.sqrt(e): .3f}")
out["Bhat_decay"] = dec
# b1 = sup_eta |eta Bhat(eta)|^2
grid = np.linspace(0, 40, 4001)
vals = np.array([float(abs(g * Bhat(g))) for g in grid[::20]])  # coarse
gmax = grid[::20][np.argmax(vals)]
fine = np.linspace(max(0, gmax - 0.5), gmax + 0.5, 201)
vals_f = np.array([float(abs(g * Bhat(g))) for g in fine])
b1 = float(np.max(vals_f) ** 2)
Bp1 = float(mp.quad(lambda v: abs(mp.diff(B, v)), [-0.5, -0.25, 0, 0.25, 0.5]))
out["b1_sup_eta_Bhat_sq"] = b1; out["argmax_eta"] = float(fine[np.argmax(vals_f)]); out["norm_Bprime_L1"] = Bp1
print(f"(d) b1 = sup |eta Bhat(eta)|^2 = {b1:.5f} at eta = {fine[np.argmax(vals_f)]:.3f};  ||B'||_1 = {Bp1:.4f}  (tx_032: b1 <= ||B'||_1^2 = {Bp1**2:.4f})")

# (e) balance: least L with 2 delta^2 c(delta L)^2 > C1 log t * b1 / L^2, C1 = 1 (placeholder), and compare with predicted law
def c_of(lam):
    return float(mp.quad(lambda v: B(v) * mp.cosh(lam * v), [-0.5, -0.25, 0, 0.25, 0.5]))
bal = {}
for t in (1e3, 1e6, 1e12):
    for d in (0.05, 0.1, 0.25):
        Lstar = None
        for L in np.arange(2, 2000, 1.0):
            lhs = 2 * d * d * c_of(d * L) ** 2
            rhs = np.log(t) * b1 / L ** 2
            if lhs > rhs:
                Lstar = float(L); break
        pred = (np.log(np.log(t)) + np.log(1 / d)) / d
        bal[f"t={t:.0e},delta={d}"] = dict(L_star=Lstar, delta_Lstar=None if Lstar is None else d * Lstar, predicted_unit=float(pred), ratio=None if Lstar is None else Lstar / pred)
        print(f"(e) t={t:.0e} delta={d}: least L = {Lstar}  (delta L = {None if Lstar is None else round(d*Lstar,2)});  delta^-1(loglog t + log 1/delta) = {pred:.1f};  ratio = {None if Lstar is None else round(Lstar/pred,3)}")
out["balance"] = bal
# separation growth for the C2 line-54 comparison: 2 delta^2 c(delta L)^2 at delta = 0.1, L = 20 and 120
s20, s120 = 2 * 0.01 * c_of(2.0) ** 2, 2 * 0.01 * c_of(12.0) ** 2
out["sep_delta0.1_L20_L120"] = [s20, s120, s120 / s20, float(np.log(s120 / s20) / 100)]
print(f"2 delta^2 c(delta L)^2 at delta=0.1: L=20 -> {s20:.4e}, L=120 -> {s120:.4e}; ratio {s120/s20:.3e} = e^({np.log(s120/s20):.2f}); growth rate per unit L = {np.log(s120/s20)/100:.4f} (C2 line 54 measured 0.30 -> 132, rate {np.log(132/0.30)/100:.4f})")
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "gevrey_edge_law_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
