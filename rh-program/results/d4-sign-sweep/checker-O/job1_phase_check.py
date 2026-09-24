# job1_phase_check.py — Job 2 part A item (a): Job 1's reduced_phase_dd + dd log, whole path, against mpmath at 50 digits,
# on rows Job 1's own binary printed for n chosen by OUR seeds (777; 31337 with 200 000 rows).
# Separates: log error dl = (hi+lo) - log n; whole-path phase error dphi = red - (t log n mod 2pi);
# product+reduction residual = dphi - t*dl (mod 2pi) — should vanish to ~1e-26 if the whole error is the log's.
import json, sys, time, mpmath as mp
mp.mp.dps = 50
twopi = 2*mp.pi
def wrap(x):
    x = mp.fmod(x, twopi)
    if x > mp.pi: x -= twopi
    if x < -mp.pi: x += twopi
    return x
out = {}
# the three-double 2pi
c0, c1, c2 = mp.mpf(6.283185307179586), mp.mpf(2.4492935982947064e-16), mp.mpf(-5.989539619436679e-33)
out["twopi_three_double_residual"] = float(twopi - (c0 + c1 + c2))
# what c2 should be: the double nearest to 2pi - c0 - c1
out["c2_nearest_double"] = repr(float(twopi - c0 - c1))
out["c1_nearest_double"] = repr(float(twopi - c0))
for path in sys.argv[1:]:
    t0 = time.time()
    j = json.load(open(path))
    t = mp.mpf(j["t_exact"])
    rows = j["phase_selftest"]
    mx_log = mx_ph = mx_res = mp.mpf(0); n_at = None
    by_k = {}
    for n, lh, ll, rh, rl, c in rows:
        n = int(n)
        ln = mp.log(n)
        dl = (mp.mpf(lh) + mp.mpf(ll)) - ln
        dphi = wrap((mp.mpf(rh) + mp.mpf(rl)) - t*ln)
        res = wrap(dphi - t*dl)
        k = n.bit_length() - 1
        by_k[k] = max(by_k.get(k, 0.0), float(abs(dl)))
        if abs(dphi) > mx_ph: mx_ph = abs(dphi); n_at = n
        mx_log = max(mx_log, abs(dl)); mx_res = max(mx_res, abs(res))
    out[path.split("/")[-1]] = dict(t=j["t_exact"], rows=len(rows), seed=j.get("selftest_seed"),
        max_abs_log_err=float(mx_log), max_phase_err_rad=float(mx_ph), max_phase_err_over_t=float(mx_ph/t), n_at_max=n_at,
        max_prod_red_residual_rad=float(mx_res), max_log_err_by_binade_k={str(k): by_k[k] for k in sorted(by_k)}, seconds=round(time.time()-t0,1))
    print(path, json.dumps(out[path.split("/")[-1]])[:400], flush=True)
json.dump(out, open("out/job1_phase_check.json", "w"), indent=1)
print(json.dumps({k: out[k] for k in ("twopi_three_double_residual", "c2_nearest_double", "c1_nearest_double")}))
