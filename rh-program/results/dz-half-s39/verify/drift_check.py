#!/usr/bin/env python3
"""drift_check.py — the prime-square branch point as the finite-range drift of E(x) for the DZ runs [heuristic test].
For real s in (1/2, 1): log zeta_P(s) = log zeta_T(s) + sum_{p<=X} -log(1 - p^{-s}) - int_1^X v^{-s} f dv + tail,
  int_1^X v^{-s} f_R dv = Ei((1-s)T) - Ei(-sT) - log((1-s)/s)  (T = log X),
  f_C: minus 2 int_0^T a_1(t) e^{(1-s)t} cos(gamma_1 t) dt (k = 2 term < 1e-4, dropped), and
  zeta_C(s) = s/(s-1) prod_k |G(4^k (s - rho_k))|^2, k = 1, 2 (k >= 3 contribute <= 0.006 to the log);
  tail mean = (1/2) E1((2s - 1) T) (prime squares above X); tail sd = E1((2s-1)T)^{1/2} (reported).
Prediction: mean E over block j ~ sqrt(2/pi) Hhat(s_x) (x/log x)^{1/2}, Hhat(s) = (2s - 1)^{1/2} zeta_P(s), s_x = 1/2 + c/log x.
For P_det the same formula with the realized quantiles converges (B analytic), which predict_det.py checks exactly."""
import json, math, glob
import numpy as np
from scipy.special import expi, exp1
from dzcommon import g_of_logu, G_entire

def log_zetaT(name, s):
    v = math.log(s / (1 - s))                     # log |s/(s-1)|, sign handled separately (negative)
    if name == "C":
        for k in range(1, 3):   # k >= 3: |log|G|^2| <= 2(0.19)4^{-k}, total <= 0.006, dropped
            lam = 4.0 ** k; gam = math.exp(lam); rho = 1 - 1 / lam + 1j * gam
            v += 2 * math.log(abs(G_entire(lam * (s - rho))))
    return v

def int_f(name, s, T):
    val = float(expi((1 - s) * T) - expi(-s * T) - math.log((1 - s) / s))
    if name == "C":
        t = np.linspace(4.0, T, int((T - 4.0) * 4000) + 1)
        a1 = g_of_logu(t / 4.0) / 4.0 * np.exp(-t / 4.0)
        val -= 2 * float(np.trapezoid(a1 * np.exp((1 - s) * t) * np.cos(math.exp(4.0) * t), t))
    return val

def main(c=1.0):
    out = {}
    for f in sorted(glob.glob("data/dz_*_s[0-9].json")):
        m = json.load(open(f)); name = m["template"]; P = np.fromfile(f[:-5] + ".primes.f64")
        st = json.load(open(f[:-5] + ".stats.json")); T = math.log(m["X"]); rows = []
        for b in st["blocks"]:
            if b["j"] < 8:
                continue
            x = b["xm"]; s = 0.5 + c / math.log(x)
            lz = log_zetaT(name, s) + float(np.sum(-np.log1p(-P ** -s))) - int_f(name, s, T) + 0.5 * float(exp1((2 * s - 1) * T))
            H = -math.sqrt(2 * s - 1) * math.exp(lz)
            pred = math.sqrt(2 / math.pi) * H; meas = b["mean"] / math.sqrt(x / math.log(x))
            rows.append((b["j"], x, meas, pred, math.sqrt(float(exp1((2 * s - 1) * T)))))
        out[f] = rows
        r = np.array([(a[2], a[3]) for a in rows])
        cc = np.corrcoef(r[:, 0], r[:, 1])[0, 1] if len(r) > 2 else float("nan")
        print("%s rho=%.3f  corr(meas,pred)=%.3f" % (f.split("/")[-1][:-5], m["rho"], cc))
        for a in rows[::3]:
            print("   j=%2d x~%.2e  E/s measured %+8.3f  predicted %+8.3f  (tail sd of log zeta %.2f)" % a)
    json.dump(out, open("data/drift_check.json", "w"), indent=1)

if __name__ == "__main__":
    main()
