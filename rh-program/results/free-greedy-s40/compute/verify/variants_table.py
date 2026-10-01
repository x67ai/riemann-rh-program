# variants_table.py -- task 4: the same table for every variant run at X = 1e8 (S rows of verify/logs/*.log)
# columns: rho, theta, N(1e8), pi_P(1e8), sup E, sup E / log^2 x, mean E (last window), tail rate x log x (last window),
# exact ties (consecutive g-integers within 1e-28 relative, all windows), min relative gap, max cluster, sup|psi - x|,
# its slope over [1e7, 1e8], psi - x at 1e8.
import math, glob, numpy as np, sys
V = __file__.rsplit("/", 1)[0]
runs = [("pi4_1e8", "pi/4", 0.5), ("var_eoverpi_th0.5_1e8", "e/pi", 0.5), ("var_rsqrt2_th0.5_1e8", "1/sqrt2", 0.5),
        ("var_r0995_th0.5_1e8", "0.95pi/3", 0.5), ("var_r098_th0.5_1e8", "0.6sqrt2pi/e", 0.5), ("var_r08_th0.5_1e8", "4/5", 0.5),
        ("var_pi4_th0.25_1e8", "pi/4", 0.25), ("var_pi4_th0.75_1e8", "pi/4", 0.75), ("ctrl_sieve_1e8", "1 (primes)", 0.0)]
R = {"pi/4": math.pi / 4, "e/pi": math.e / math.pi, "1/sqrt2": 1 / math.sqrt(2), "0.95pi/3": 0.95 * math.pi / 3,
     "0.6sqrt2pi/e": 0.6 * math.sqrt(2) * math.pi / math.e, "4/5": 0.8, "1 (primes)": 1.0}
print("# tag | rho | theta | N(1e8) | pi_P(1e8) | sup E | supE/log^2 | meanE(win) | lam*log x (win) | ties | min rel gap | max clu | sup|psi-x| | slope 1e7->1e8 | psi-x(1e8)")
for tag, rn, th in runs:
    S = np.array([[float(v) for v in ln.split()[1:27]] for ln in open(f"{V}/logs/{tag}.log") if ln.startswith("S ")])
    last = S[-1]; i7 = np.argmin(abs(S[:, 0] - 1e7))
    ties = int(S[:, 14].sum()); mrel = S[:, 13].min(); clu = int(S[:, 11].max())
    H = np.fromfile(f"/private/tmp/rh-s40-free-greedy/{tag}.hist", dtype=np.float64).reshape(-1, 8193)
    m = H[-1, 1:] - H[-2, 1:]; tot = m.sum(); edges = -1 + np.arange(8193) / 16
    surv = 1 - np.cumsum(m) / tot; sel = (surv < 1e-1) & (surv > 1e-4); lam = float("nan")
    if sel.sum() >= 8:
        A = np.vstack([np.ones(sel.sum()), edges[1:][sel]]).T
        lam = -np.linalg.lstsq(A, np.log(surv[sel]), rcond=None)[0][1]
    xc = math.sqrt(S[-2, 0] * S[-1, 0])
    sl = math.log(last[19] / S[i7, 19]) / math.log(10) if S[i7, 19] > 0 else float("nan")
    print(f"{tag} | {rn} | {th} | {int(last[1])} | {int(last[2])} | {last[4]:.3f} | {last[4] / math.log(1e8) ** 2:.4f} | {last[6]:.3f} | {lam * math.log(xc):.3f} | {ties} | {mrel:.2e} | {clu} | {last[19]:.4g} | {sl:+.3f} | {last[20]:.4g}")
