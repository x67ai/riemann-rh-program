"""CHECKER task (1): 20 random zeros per height re-verified at 30 digits, + index->height map audit."""
import json, random, time, math, sys, os
from mpmath import mp, mpf, zetazero, siegelz, siegeltheta
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if False else "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/c2-m2/campaign"
out = {}
random.seed(20260916)
for tag in ["t1e3","t1e4","t1e5","t1e6"]:
    d = json.load(open(f"{BASE}/zeros_{tag}.json"))
    zs = d["zeros"]; t = d["t"]
    idx = [z[0] for z in zs]
    # index->height map audit: consecutive indices, monotone gammas, RvM count, gap test via Gram/RvM
    consecutive = (idx == list(range(idx[0], idx[0]+len(idx))))
    monotone = all(zs[i][1] < zs[i+1][1] for i in range(len(zs)-1))
    # Riemann-von Mangoldt: N(T) = theta(T)/pi + 1 + S(T); compare count against N(hi)-N(lo)
    with mp.workdps(30):
        NT = lambda T: siegeltheta(mpf(T))/mp.pi + 1
        rvm_lo, rvm_hi = float(NT(zs[0][1])), float(NT(zs[-1][1]))
    rvm_count = rvm_hi - rvm_lo + 1
    # main-term RvM N(T) ~ T/2pi log(T/2pi e) + 7/8 at the two endpoints -> expected index
    def Nmain(T): return (T/(2*math.pi))*math.log(T/(2*math.pi*math.e)) + 7/8
    picks = sorted(random.sample(range(len(zs)), 20))
    rows = []
    for j in picks:
        n, g_stored, res_stored = zs[j]
        t0 = time.time()
        with mp.workdps(30):
            g = zetazero(int(n)).imag
            # Newton on Z (siegelz) from the stored gamma, 30 digits
            x = mpf(repr(g_stored))
            for _ in range(60):
                f = siegelz(x)
                h = mpf(10)**(-15)
                fp = (siegelz(x+h)-siegelz(x-h))/(2*h)
                if fp == 0: break
                dx = f/fp
                x = x - dx
                if abs(dx) < mpf(10)**(-28): break
            zval = siegelz(g)
            zval_newton = siegelz(x)
            rows.append(dict(index=int(n), gamma_stored=g_stored, gamma_zetazero30=mp.nstr(g, 25),
                             gamma_newton30=mp.nstr(x, 25),
                             d_stored_vs_zetazero=float(abs(mpf(repr(g_stored))-g)),
                             d_newton_vs_zetazero=float(abs(x-g)),
                             absZ_at_zetazero=float(abs(zval)), absZ_at_newton=float(abs(zval_newton)),
                             secs=time.time()-t0))
        print(tag, n, rows[-1]["d_stored_vs_zetazero"], rows[-1]["d_newton_vs_zetazero"], flush=True)
    out[tag] = dict(t=t, n_zeros=len(zs), index_lo=idx[0], index_hi=idx[-1], consecutive_indices=consecutive,
                    gamma_monotone=monotone, count=len(zs), rvm_theta_count=rvm_count,
                    rvm_main_expected=Nmain(zs[-1][1])-Nmain(zs[0][1])+1,
                    max_d=max(r["d_stored_vs_zetazero"] for r in rows),
                    max_absZ=max(r["absZ_at_zetazero"] for r in rows), rows=rows)
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"zeros_check.json"),"w"), indent=1)
print("DONE")
