# Orchestrator (Session 40): greedy ascent in n for the lower bound a_n^known (g-primes <= 10^9 only) of S5(4/5).
import numpy as np, sys, math, time
sys.argv = [sys.argv[0], sys.argv[1]] + sys.argv[2:]
from factor_count import count
cand = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
exps = {2: 4, 3: 2, 5: 3, 7: 1, 13: 1, 19: 1, 29: 1}
maxlog = float(sys.argv[2]) if len(sys.argv) > 2 else 60.0     # stop when log10(n) exceeds this
t0 = time.time()
def val(ex):
    ps = sorted(ex); es = [ex[p] for p in ps]
    a, k = count(ps, es)
    ln = sum(e * math.log(p) for p, e in ex.items())
    return a, k, ln
a, k, ln = val(exps)
print(f"start log10 n = {ln/math.log(10):.2f}  a = {a:.6g}  exponent = {math.log(a)/ln:.4f}  gdiv = {k}", flush=True)
while ln / math.log(10) < maxlog:
    best = None
    for p in cand:
        ex = dict(exps); ex[p] = ex.get(p, 0) + 1
        a2, k2, ln2 = val(ex)
        gain = (math.log(a2) - math.log(a)) / math.log(p)
        if best is None or gain > best[0]: best = (gain, p, a2, k2, ln2, ex)
    gain, p, a, k, ln, exps = best
    fac = " ".join(f"{q}^{e}" for q, e in sorted(exps.items()))
    print(f"x{p:<3d} log10 n = {ln/math.log(10):6.2f}  a_known = {a:.6g}  exponent = {math.log(a)/ln:.4f}  marginal = {gain:.3f}  gdiv = {k}  t = {time.time()-t0:.0f}s  n = {fac}", flush=True)
    if time.time() - t0 > float(sys.argv[3]) if len(sys.argv) > 3 else False: break
