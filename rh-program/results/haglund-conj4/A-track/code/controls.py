# controls.py -- A-track positive controls of the detectors: the pencil built on Xi + lam instead of Xi
# (S^lam_k = (Xi_{k+1} + lam)/Phi_{k+1}); with lam = 5e-5 the reader read-O reports (SHARED, 16:46 and 17:01 IST) a local
# minimum of S^lam_1 at 24.34012104 with value 0.611995156161, and a zero beta = 28.6324463545442 + 8.52426881931311i of
# Xi + lam with Im f'(beta) > 0 whose pencil branch rises for k = 2..8. Our scanner and tracer must see both.
import sys, json, time
import a_core, axis, tracer
from a_core import acb, arb, ctx, XiN_T_ad, XiN_L, Phi_fast, _PREC, STATS, _rel
LAM = float(sys.argv[1]) if len(sys.argv) > 1 else 5e-5

def S_control(k, z, route="T", bits=40):
    key = ("Sc", k, route)
    prec0 = ctx.prec
    p = _PREC.get(key, 96)
    try:
        while True:
            ctx.prec = p
            num = XiN_L(k + 1, z) + arb(LAM)          # route L: the tail ball of route T is sized for Xi_{k+1}, not Xi_{k+1} + lam
            s = num / Phi_fast(k + 1, z)
            if _rel(s) <= 2.0 ** (-bits):
                _PREC[key] = max(64, int(p * 0.8))
                return s
            p *= 2
            if p > 20000:
                raise RuntimeError("runaway")
    finally:
        ctx.prec = prec0

a_core.S = S_control
axis.S = S_control
out = {"lam": LAM}
r = axis.scan(1, 0.0, 76.0)
out["axis_k1"] = {"n_max": r["n_max"], "n_min": r["n_min"], "extrema01": r["extrema01"], "consistent": r["all_consistent"]}
print("axis k=1 lam=%g: max %d min %d extrema %s" % (LAM, r["n_max"], r["n_min"], [(round(e["x"], 8), e["u"], e["type"]) for e in r["extrema01"]]), flush=True)
beta = complex(28.6324463545442, 8.52426881931311)
for k in (2, 3, 5, 8):
    z0, ok = tracer.newton_S(k, beta, 1.0)          # zero of Xi_k + lam near beta: S^lam_k = 1
    s, d = a_core.SdS(k, z0)
    rr = tracer.trace(k, z0, -1, keep_path=False)
    out["trace_k%d" % k] = {kk: rr[kk] for kk in ("start", "end", "z_end", "u_end", "worst_dy", "min_margin", "steps")}
    print("k=%d start %s (Newton ok %s) margin at start %.4g -> %s worst_dy %.3g min_margin %.3g" % (
        k, z0, ok, -d.imag / abs(d), rr["end"], rr["worst_dy"], rr["min_margin"]), flush=True)
json.dump(out, open("../data/controls_lam%g.json" % LAM, "w"), indent=0)
