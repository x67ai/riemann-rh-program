# p1_seeded.py -- P1 census for pencil k with the zeros of Xi_k found independently of the previous pencil (seed grid
# near the departure height 4(k+1)^2, then the march; completeness by the argument principle as in census.py).
# Used for k = 11, 12 to run them in parallel with k = 10.
import sys, os, json, time
from census import *
from p2 import p2_seeds

if __name__ == "__main__":
    k = int(sys.argv[1])
    xa, xb, nxt = 0.0, Xk(k), Xk(k + 1)
    ctx.prec = 96
    T0 = time.time()
    sk = p2_seeds(k, xa, xb)
    json.dump({"N": k, "zeros": jl(sk), "from": "p1_seeded seed scan + march"}, open(os.path.join(DATA, "zeros_Xi%d_indep.json" % k), "w"))
    log("  %d independent seeds for Xi_%d (%.0fs)" % (len(sk), k, time.time() - T0))
    R = run(k, xa, xb, "P1", next_xb=nxt, seeds_k=sk)
    hygiene(R)
    s = summarize(R)
    log("SUMMARY k=%d P1: %s" % (k, json.dumps({kk: v for kk, v in s.items() if kk != "other_ends"})))
    log("hygiene: %s" % json.dumps(R["hygiene"]))
    fn = os.path.join(DATA, "census_k%d.json" % k)
    json.dump(R, open(fn, "w"), separators=(",", ":"))
    log("wrote %s (%.0f kB)" % (fn, os.path.getsize(fn) / 1024.0))
