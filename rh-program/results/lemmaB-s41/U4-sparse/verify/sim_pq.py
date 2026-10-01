#!/usr/bin/env python3
"""U4-sparse: Poisson-model queue with the SAME number of steps per bin and the bin's measured arrival rate lambda_hat.
e_k = max(e_{k-1} + c_k - 1, 0), c_k ~ Poisson(lambda_hat(bin)) i.i.d.; computed in chunks via e_k = S_k - min(0, min_{j<=k} S_j)
(with the state carried across chunks). Reports, per bin, the measured max e and the replicate distribution of the model max.
Usage: sim_pq.py file.tsv [n_top_bins=10] [replicates=10] [seed=1]"""
import sys, math
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from ana import parse

def run_model(bins, rng, chunk=1 << 24):
    e = 0; out = []
    for n, lam in bins:
        left = n; mx = 0
        while left > 0:
            m = min(left, chunk); left -= m
            inc = rng.poisson(lam, m).astype(np.int64) - 1
            S = np.cumsum(inc); S += e                      # walk started at the carried state
            run_min = np.minimum.accumulate(S)
            q = S - np.minimum(run_min, 0)                  # reflected at 0
            mx = max(mx, int(q.max())); e = int(q[-1])
        out.append(mx)
    return out

if __name__ == '__main__':
    fn = sys.argv[1]; ntop = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    R = int(sys.argv[3]) if len(sys.argv) > 3 else 10; seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    rho, kv, rows = parse(fn)
    rows = [r for r in rows if r['nsteps'] > 0]
    bins = [(r['nsteps'], r['ncomp'] / r['nsteps']) for r in rows]
    rng = np.random.default_rng(seed)
    reps = np.array([run_model(bins, rng) for _ in range(R)])     # R x nbins (per-bin maxima)
    cum = np.maximum.accumulate(reps, axis=1)
    meas = np.maximum.accumulate(np.array([r['emax'] for r in rows]))
    print(f"# {fn} rho={rho:.6g}  Poisson-model queue, {R} replicates, seed {seed}")
    print("# tau_hi  nsteps  lam_hat  meas_cummax_e  model_cummax: min  median  max")
    for i in range(len(rows) - ntop, len(rows)):
        r = rows[i]
        print(f"{rho*math.log(r['xhi']):.4f} {r['nsteps']:>11d} {bins[i][1]:.4f} {meas[i]:>4d}   "
              f"{cum[:, i].min():>3d} {np.median(cum[:, i]):>6.1f} {cum[:, i].max():>3d}")
