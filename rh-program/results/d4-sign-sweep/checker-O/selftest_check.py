# selftest_check.py — Job 2 part A: check twsumO's phase (in turns) against mpmath at 50 digits
import json, sys, mpmath as mp
mp.mp.dps = 50
d = json.load(open(sys.argv[1]))
t = mp.mpf(d["t_exact"])
twopi = 2*mp.pi
worst = (0, None)
errs = []
for n, hi, lo in d["selftest_rows"]:
    ref = t*mp.log(n)/twopi
    ref = ref - mp.floor(ref + mp.mpf(1)/2)
    got = mp.mpf(hi) + mp.mpf(lo)
    e = got - ref
    e = e - mp.floor(e + mp.mpf(1)/2)
    e_rad = abs(e)*twopi
    errs.append(float(e_rad))
    if e_rad > worst[0]:
        worst = (e_rad, n)
errs.sort()
print(json.dumps({"file": sys.argv[1], "t": d["t_exact"], "count": len(errs), "max_phase_err_rad": float(worst[0]), "at_n": worst[1],
                  "median_rad": errs[len(errs)//2], "max_over_t": float(worst[0]/t)}))
