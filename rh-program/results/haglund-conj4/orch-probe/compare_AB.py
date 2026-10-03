# compare_AB.py -- the orchestrator's number-by-number comparison of the two producers' landings (x*, u*).
# A: A-track/data/census_k<k>.json (level-curve tracer, Arb).  B: the landings printed in B-track's SHARED blocks / NOTE
# (Newton continuation on a tau grid, mpmath), typed here from SHARED.md blocks of 16:45, 16:58, 17:24 IST 2026-10-03.
import json, math, io
B = {1: [(22.142378, 2.48042), (31.254957, 8.92812), (38.516854, 14.16819)],
     2: [(44.560600, 3.24730), (50.852817, 8.29249), (57.272541, 13.06910), (62.128208, 15.97922)],
     3: [(67.930995, 0.22526), (73.067283, 3.31630), (78.002167, 7.89953), (83.534272, 12.12625), (87.983898, 15.96853),
         (93.140202, 19.20114), (96.958744, 21.52466), (102.069222, 25.82349)]}
worst_x = 0.0; worst_tau = 0.0
for k in sorted(B):
    d = json.load(io.open('A-track/data/census_k%d.json' % k))
    A = sorted((b['z_end'][0], -math.log(b['u_end'])) for b in d['branches'] if b['end'] == 'landed')
    assert len(A) == len(B[k]), (k, len(A), len(B[k]))
    for (xa, ta), (xb, tb) in zip(A, B[k]):
        worst_x = max(worst_x, abs(xa - xb)); worst_tau = max(worst_tau, abs(ta - tb))
        print("k=%d  A: x*=%.6f tau*=%.5f   B: x*=%.6f tau*=%.5f   dx=%.1e dtau=%.1e" % (k, xa, ta, xb, tb, xa - xb, ta - tb))
    ends = {'landed': 0, 'nonreal': 0, 'exit': 0}
    for b in d['branches']:
        e = b['end']; ends['landed' if e == 'landed' else 'exit' if 'exit' in e or 'left' in e or 'edge' in e else 'nonreal'] += 1
    print("k=%d  A ends: %s ; worst step change of Im z over all branches: %.2e ; smallest margin %.3f" % (k, ends, max(b['worst_dy'] for b in d['branches']), min(b['min_margin'] for b in d['branches'])))
print("largest disagreement A vs B over %d landings: |dx| = %.1e, |dtau| = %.1e" % (sum(len(v) for v in B.values()), worst_x, worst_tau))
