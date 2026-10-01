# read-O driver: generate (dzsim.gen), enumerate (gcount bins), store counts + metadata. Primes go to /private/tmp.
import sys, json, subprocess, math, time, numpy as np
from dzsim import gen
TMP = "/private/tmp/rh-s40-dz-half-s39"
X = 1e7; Y = 1e9; B = 2048
for tag in sys.argv[1:]:                     # tags like R1 C3
    tpl, seed = tag[0], int(tag[1:])
    t = time.time()
    P, lr, info = gen(tpl, 1000 + seed, X=X, Y=Y)
    pf = f"{TMP}/dz_{tag}.f64"; P.astype(np.float64).tofile(pf)
    out = subprocess.run(["./gcount", "bins", pf, "%g" % X, str(B), f"data/dz_{tag}.i64"], capture_output=True, text=True).stdout
    meta = dict(tag=tag, template=tpl, seed=1000 + seed, rng="numpy Philox", X=X, Y=Y, B=B, log_rho=lr, rho=math.exp(lr),
                n_primes=int(len(P)), has15=bool(np.any(P == 1.5)), gcount=out.strip(), secs=round(time.time() - t, 1), **info)
    json.dump(meta, open(f"data/dz_{tag}.json", "w"), indent=1)
    print(json.dumps(meta), flush=True)
