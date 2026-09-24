#!/usr/bin/env python3
"""planted_real_zero.py -- Session 24 item 2(c), section 2 of siegel-world-scout.md: the cone sector at t = 0 for zeta_K
against a PLANTED real zero beta = 1 - delta (the planted-defect method of results/c2-m2/campaign/); D = -20 unless stated.

Objects (confinement-note.md section 0.1 normalization; degree-2 archimedean density):
  A_K(r) = (1/2pi)[Re psi(1/4 + ir/2) + Re psi(3/4 + ir/2) - 2 log pi + log|D|],   a_K := mu_0 * A_K,
  B_K(w) = 2 what(0) + int what(s) a_K(s) ds,
  real-zero orbit {beta, 1-beta}: gamma-values -/+ i y, y = beta - 1/2 = 1/2 - delta; share = 2 Re ghat(-iy) = 2 (what * mu_y)(0)
      = 2 int what(s) mu_y(s) ds  (Lemma K at x = 0; mu_y even),
  certificate at delta: share > B_K(w);  margin := share - B_K(w).
  POLE CAP: (what * mu_y)(0) <= what(0) (|what| <= what(0) for w >= 0; int mu_y = 1), so share <= 2 what(0) and
      margin <= -int what a_K: a certificate for a SINGLE real zero needs Arch_K(w) = int what a_K < 0.
  Double real zero (two zeros or a double zero at beta): share_2 = 2 * share.
Part A: the de la Vallee Poussin element w_{a,t} of confinement-note section 4 (t = 0 is the Poisson element), closed form
  B_K(w_{a,t}) = sum_j d_j [2 Re(1/(s_j-1) + 1/s_j) + Re psi(s_j/2) + Re psi((s_j+1)/2) - 2 log pi + log|D|],  s_j = sigma + i j t,
  (Lemma A of the note applied to both Gamma_R factors; checked numerically here), share = 2 sum_k c_k Re pi_a(kt - iy).
Part B: the families Fejer_T (what = (1-|s|/T)_+), Fejer_T^2, Gaussian_sigma (what = e^{-s^2/2sigma^2}), Poisson_a (what = pi_a) at t = 0,
  margin computed on a grid; the thresholds D_0 (A_K >= 0 pointwise) and D_1 (a_K(0) >= 0); the reach vs |D|.
Controls (zoo V.4): NEGATIVE control = the planted DOUBLE real zero at D = -20 (must fire at small delta: Landau-Page);
  POSITIVE control = a planted SINGLE real zero at |D| >= D_1 (must be silent at every delta: the pole cap).
Budget: < 2 minutes.
"""
import json, sys, time
import numpy as np
import mpmath as mp
from scipy.special import digamma as sp_digamma

t0 = time.time(); out = {}
mp.mp.dps = 25
LOGPI = float(mp.log(mp.pi))
DELTAS = (0.1, 0.05, 0.02, 0.01, 0.001)

# ---------- Part A: the dlVP element ----------
def bracket_K(sigma, jt, logD):
    s = mp.mpc(sigma, jt)
    return float(2 * mp.re(1 / (s - 1) + 1 / s) + mp.re(mp.digamma(s / 2)) + mp.re(mp.digamma((s + 1) / 2)) - 2 * mp.log(mp.pi) + logD)
def B_K_dlvp(eta, t, logD):
    sigma = 1 + eta
    return 3 * bracket_K(sigma, 0.0, logD) + 4 * bracket_K(sigma, t, logD) + bracket_K(sigma, 2 * t, logD)
def share_real(eta, t, delta):
    a = 0.5 + eta; y = 0.5 - delta; s = 0.0
    for k, c in ((0, 3.0), (1, 2.0), (-1, 2.0), (2, 0.5), (-2, 0.5)):
        x = k * t
        s += c * ((a + y) / ((a + y) ** 2 + x * x) + (a - y) / ((a - y) ** 2 + x * x))
    return 2 * s
# check of the closed-form archimedean term against direct quadrature at one (a, t): (1/2pi) int ghat(r) bracket(r) dr with ghat = sum c_k pi_a(r + kt)
def check_lemmaA(eta, t, logD):
    a = 0.5 + eta
    f = lambda r: sum(c * 2 * a / (a * a + (r + k * t) ** 2) for k, c in ((0, 3.0), (1, 2.0), (-1, 2.0), (2, 0.5), (-2, 0.5))) * (mp.re(mp.digamma(mp.mpc(0.25, r / 2))) + mp.re(mp.digamma(mp.mpc(0.75, r / 2))) - 2 * mp.log(mp.pi) + logD)
    direct = mp.quad(f, [-mp.inf, -2 * t, -t, 0, t, 2 * t, mp.inf]) / (2 * mp.pi)
    closed = sum(d * (bracket_K(1 + eta, j * t, logD) - 2 * float(mp.re(1 / (mp.mpc(1 + eta, j * t) - 1) + 1 / mp.mpc(1 + eta, j * t)))) for j, d in ((0, 3), (1, 4), (2, 1)))
    return float(direct), closed
LOG20 = float(mp.log(20))
d1, c1 = check_lemmaA(0.3, 5.0, LOG20)
print(f"Lemma A (degree 2) check at eta = 0.3, t = 5, D = -20: direct quadrature {d1:.10f} vs closed form {c1:.10f} (diff {d1-c1:.1e})")
out["lemmaA_check"] = dict(direct=d1, closed=c1)
ETAS = np.exp(np.linspace(np.log(1e-3), np.log(1.0), 300))
def best_margin_dlvp(t, delta, logD, mult=1):
    best = (-np.inf, None)
    for e in ETAS:
        m = mult * share_real(e, t, delta) - B_K_dlvp(e, t, logD)
        if m > best[0]: best = (m, e)
    return best
tableA = []
print("Part A -- dlVP element, D = -20: max over eta of [share - B_K] (single real zero) and [2 share - B_K] (double)")
for t in (0.0, 1.0, 5.0, 28.0):
    for delta in DELTAS:
        m1, e1 = best_margin_dlvp(t, delta, LOG20, 1); m2, e2 = best_margin_dlvp(t, delta, LOG20, 2)
        tableA.append(dict(t=t, delta=delta, margin_single=m1, eta_single=e1, margin_double=m2, eta_double=e2))
        print(f"  t = {t:4.0f}, delta = {delta:6.3f}: single margin {m1:+10.4f} (eta {e1:.4f}) {'FIRES' if m1 > 0 else 'silent'};  double margin {m2:+10.4f} (eta {e2:.4f}) {'FIRES' if m2 > 0 else 'silent'}")
out["partA_D20"] = tableA
# the double's exclusion radius at t = 0 (largest delta excluded) for several |D| (Landau-Page shape c/log|D|)
def delta_max_double(logD, t=0.0):
    lo, hi = 1e-6, 0.5
    if best_margin_dlvp(t, lo, logD, 2)[0] <= 0: return 0.0
    if best_margin_dlvp(t, hi, logD, 2)[0] > 0: return 0.5
    for _ in range(40):
        mid = np.sqrt(lo * hi)
        if best_margin_dlvp(t, mid, logD, 2)[0] > 0: lo = mid
        else: hi = mid
    return lo
rowsD = []
for absD in (20, 100, 1000, 10**4, 10**6, 10**10):
    dm = delta_max_double(float(np.log(absD)))
    rowsD.append(dict(absD=absD, delta_max_double=dm, times_logD=dm * np.log(absD)))
    print(f"  double real zero excluded by the Poisson element (t = 0) for delta < {dm:.5f} at |D| = {absD:.0e};  delta_max * log|D| = {dm*np.log(absD):.4f}")
out["double_exclusion_vs_D"] = rowsD
# positive control: single planted zero at large |D| must be silent for every delta and eta
ctrl = []
for absD in (2005, 10**6, 10**12):
    worst = max(best_margin_dlvp(0.0, d, float(np.log(absD)), 1)[0] for d in DELTAS + (0.3, 0.5))
    ctrl.append(dict(absD=absD, max_margin_single=worst))
    print(f"  POSITIVE CONTROL |D| = {absD:.0e}: max over delta, eta of the single-zero margin = {worst:+.4f} -> {'silent (as the pole cap requires)' if worst < 0 else 'FIRED -- INVERTED'}")
out["positive_control_dlvp"] = ctrl

# ---------- Part B: families at t = 0 on a grid ----------
S = np.linspace(-80, 80, 160001); ds = S[1] - S[0]
def mu0(x): return 1 / np.cosh(np.pi * x)
def mu_y(x, y): return 2 * np.cos(np.pi * y) * np.cosh(np.pi * x) / (np.cosh(2 * np.pi * x) + np.cos(2 * np.pi * y))
psi_sum = np.real(sp_digamma(0.25 + 0.5j * S)) + np.real(sp_digamma(0.75 + 0.5j * S))
def A_K(logD): return (psi_sum - 2 * LOGPI + logD) / (2 * np.pi)
# a_K = mu_0 * A_K on the grid (A_K grows like log|r|/pi; mu_0 decays like e^{-pi|x|}); compute on |s| <= 20 only
Sg = np.linspace(-20, 20, 4001)
M0 = mu0(Sg[:, None] - S[None, :]) * ds          # 4001 x 160001 would be 5 GB -- do it in chunks
def a_K_grid(logD):
    A = A_K(logD); res = np.empty_like(Sg)
    for i0 in range(0, len(Sg), 200):
        blk = Sg[i0:i0 + 200]
        res[i0:i0 + 200] = (mu0(blk[:, None] - S[None, :]) * A[None, :]).sum(axis=1) * ds
    return res
del M0
psi_conv0 = (mu0(S) * psi_sum).sum() * ds
D0 = float(mp.exp(2 * mp.log(mp.pi) - mp.digamma(0.25) - mp.digamma(0.75)))
D1 = float(np.exp(2 * LOGPI - psi_conv0))
print(f"thresholds: A_K(0) >= 0 iff |D| >= D_0 = exp(2 log pi - psi(1/4) - psi(3/4)) = {D0:.3f};  a_K(0) = (mu_0 * A_K)(0) >= 0 iff |D| >= D_1 = {D1:.3f}")
out["D0_AK_nonneg"] = D0; out["D1_aK0_nonneg"] = D1
aK20 = a_K_grid(LOG20)
print(f"D = -20: A_K(0) = {float(A_K(LOG20)[len(S)//2]):.6f}, a_K(0) = {aK20[len(Sg)//2]:.6f}, a_K minimal at s = {Sg[aK20.argmin()]:.3f} (min {aK20.min():.6f}); a_K > 0 for |s| > {Sg[aK20 > 0][Sg[aK20 > 0] > 0].min():.3f}; negative mass int_{{a_K<0}} |a_K| = {(-aK20[aK20 < 0]).sum()*(Sg[1]-Sg[0]):.6f}")
out["aK20"] = dict(A0=float(A_K(LOG20)[len(S)//2]), a0=float(aK20[len(Sg)//2]), argmin=float(Sg[aK20.argmin()]), neg_mass=float((-aK20[aK20 < 0]).sum()*(Sg[1]-Sg[0])), pos_from=float(Sg[aK20 > 0][Sg[aK20 > 0] > 0].min()))
dsg = Sg[1] - Sg[0]
# graded grid for the share integral 2 int what(s) mu_y(s) ds: mu_y has a peak of height 1/sin(pi delta) and width ~ delta at s = 0
SF = np.concatenate([np.linspace(-20, -5, 1501)[:-1], np.linspace(-5, -0.5, 4501)[:-1], np.linspace(-0.5, 0.5, 200001), np.linspace(0.5, 5, 4501)[1:], np.linspace(5, 20, 1501)[1:]])
def share_of(what_fn, d):
    return 2 * np.trapezoid(what_fn(SF) * mu_y(SF, 0.5 - d), SF)
# quadrature check of the pole cap on the graded grid: int mu_y = 1 at every delta used
capcheck = {str(d): float(np.trapezoid(mu_y(SF, 0.5 - d), SF)) for d in DELTAS}
print("graded-grid check: int mu_y over |s| <= 20 =", {k: f"{v:.9f}" for k, v in capcheck.items()})
out["int_mu_y_graded"] = capcheck
def families():
    for T in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0):
        yield f"Fejer T={T}", (lambda s, T=T: np.clip(1 - np.abs(s) / T, 0, None))
        yield f"Fejer^2 T={T}", (lambda s, T=T: np.clip(1 - np.abs(s) / T, 0, None) ** 2)
    for sg in (0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0):
        yield f"Gauss sigma={sg}", (lambda s, sg=sg: np.exp(-s ** 2 / (2 * sg * sg)))
    for a in (0.55, 0.6, 0.75, 1.0, 1.5, 2.0):
        yield f"Poisson a={a}", (lambda s, a=a: 2 * a / (a * a + s ** 2))
def run_family(logD, label):
    aK = a_K_grid(logD)
    best = {d: (-np.inf, None) for d in DELTAS}; bestdbl = {d: (-np.inf, None) for d in DELTAS}
    inf_arch = (np.inf, None); capmax = 0.0
    for name, wf in families():
        w0 = float(wf(np.array([0.0]))[0]); arch = np.trapezoid(wf(Sg) * aK, Sg)
        inf_arch = min(inf_arch, (arch / w0, name))
        for d in DELTAS:
            sh = share_of(wf, d)
            capmax = max(capmax, sh / (2 * w0))
            m = sh - 2 * w0 - arch; m2 = 2 * sh - 2 * w0 - arch
            if m > best[d][0]: best[d] = (m, name)
            if m2 > bestdbl[d][0]: bestdbl[d] = (m2, name)
    print(f"Part B [{label}]: inf over the family of Arch_K(w)/what(0) = {inf_arch[0]:+.6f} ({inf_arch[1]});  max over family, delta of share/(2 what(0)) = {capmax:.6f} (pole cap 1)")
    for d in DELTAS:
        print(f"    delta = {d:6.3f}: best single margin {best[d][0]:+.5f} [{best[d][1]}] {'FIRES' if best[d][0] > 0 else 'silent'};  best double margin {bestdbl[d][0]:+.5f} [{bestdbl[d][1]}] {'FIRES' if bestdbl[d][0] > 0 else 'silent'}")
    return dict(inf_arch_ratio=inf_arch[0], inf_arch_elem=inf_arch[1], cap_max=capmax,
                single={str(d): dict(margin=best[d][0], elem=best[d][1]) for d in DELTAS},
                double={str(d): dict(margin=bestdbl[d][0], elem=bestdbl[d][1]) for d in DELTAS})
out["partB_D20"] = run_family(LOG20, "D = -20")
out["partB_D4"] = run_family(float(np.log(4)), "D = -4 (Q(i), no real zero: L(chi_4) -- the small-|D| regime where the cone reaches)")
out["partB_D2005"] = run_family(float(np.log(2005)), "|D| = 2005 >= D_0 (positive control: pole cap, silent)")
out["partB_D1e6"] = run_family(float(np.log(1e6)), "|D| = 1e6 (positive control)")
# reach vs |D| at delta = 0.1 and 0.01 (single zero), family best
reach = []
for absD in (3, 4, 7, 8, 11, 15, 19, 20, 23, 24, 40, 100, 200, 300, 500, 1000, 2000, 2005, 5000):
    aK = a_K_grid(float(np.log(absD)))
    row = dict(absD=absD)
    for d in (0.1, 0.01):
        b = -np.inf
        for name, wf in families():
            w0 = float(wf(np.array([0.0]))[0]); arch = np.trapezoid(wf(Sg) * aK, Sg)
            b = max(b, (share_of(wf, d) - 2 * w0 - arch) / w0)
        row[f"best_margin_over_w0_delta_{d}"] = b
    reach.append(row)
    print(f"  reach vs |D| = {absD:5d}: best single margin/what(0) at delta = 0.1: {row['best_margin_over_w0_delta_0.1']:+.5f}, at delta = 0.01: {row['best_margin_over_w0_delta_0.01']:+.5f}")
out["reach_vs_D"] = reach
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "planted_real_zero_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
