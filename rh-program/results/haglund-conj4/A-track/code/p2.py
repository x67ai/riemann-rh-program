# p2.py -- A-track P2: frontier window [4(k+1)^2 - 40, 4(k+2)^2 + 40] for pencil k (branches that start in it).
# Zeros of Xi_k in the window: Newton from a seed grid near the departure height 4(k+1)^2, then a march along the zero
# curve, then strip-by-strip argument-principle completion (census.fill).
import sys, os, json, math, time
from census import *

def p2_seeds(N, xa, xb, route="T"):
    xdep = 4.0 * (N + 1) ** 2
    a0, b0 = max(xa, xdep - 40.0), min(xb, xdep + 25.0)
    first = seed_scan(N, a0, b0, 12.0, route) if b0 > a0 else []
    log("  seed scan N=%d on [%.1f, %.1f] x (0,12]: %d zeros" % (N, a0, b0, len(first)))
    zs = march(N, first, xb + 5, route) if len(first) >= 2 else first
    return zs

if __name__ == "__main__":
    k = int(sys.argv[1])
    xa, xb = 4.0 * (k + 1) ** 2 - 40, 4.0 * (k + 2) ** 2 + 40
    ctx.prec = 96
    T0 = time.time()
    sk = p2_seeds(k, xa, xb)
    json.dump({"N": k, "window": [xa, xb], "zeros": jl(sk)}, open(os.path.join(DATA, "p2_zeros_Xi%d_k%d.json" % (k, k)), "w"))
    log("  %d seeds for Xi_%d (%.0fs)" % (len(sk), k, time.time() - T0))
    R = run(k, xa, xb, "P2", seeds_k=sk)
    hygiene(R)
    s = summarize(R)
    log("SUMMARY k=%d P2: %s" % (k, json.dumps({kk: v for kk, v in s.items() if kk != "other_ends"})))
    log("hygiene: %s" % json.dumps(R["hygiene"]))
    fn = os.path.join(DATA, "frontier_k%d.json" % k)
    json.dump(R, open(fn, "w"), separators=(",", ":"))
    log("wrote %s (%.0f kB)" % (fn, os.path.getsize(fn) / 1024.0))
