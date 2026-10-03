"""Re-run sample branches of pencil k (a) at dps 60 on the same tau-grid, (b) at dps 30 on the halved grid,
and compare with the main run at the common grid values.  usage: python3 checks.py k i1,i2,... [main.json]"""
import sys, json, time
sys.path.insert(0, '.')
import mpmath as mp, track
k = int(sys.argv[1])
main = json.load(open(sys.argv[3] if len(sys.argv) > 3 else '../data/k%d-track.json' % k))
if sys.argv[2] == 'auto':
    # first and last landing branch, a middle branch ending at t = 1, the last branch starting in W
    import math
    X = 2*math.pi*(k + 2)**2 + 30
    B = main['branches']
    land = [i for i, b in enumerate(B) if b['status'] == 'axis-approach']
    ends = [i for i, b in enumerate(B) if b['status'] == 'end-t1' and float(b['start'][0]) <= X]
    inW = [i for i, b in enumerate(B) if float(b['start'][0]) <= X]
    idx = sorted(set(([land[0], land[-1]] if land else []) + ([ends[len(ends)//2]] if ends else []) + ([inW[-1]] if inW else [])))
else:
    idx = [int(a) for a in sys.argv[2].split(',')]
print('sample', idx); sys.stdout.flush()
dtau = main['dtau']; tau_max = main['tau_max']
out = dict(k=k, checks=[])
t0 = time.time()
for i in idx:
    br = main['branches'][i]
    z0 = br['start']
    ref = {round(r['tau'], 6): r for r in br['records']}
    res = dict(index=i, start=z0)
    for label, dps, dt in (('dps60', 60, dtau), ('half-grid', 30, dtau/2)):
        mp.mp.dps = dps
        r = track.follow(k, mp.mpc(z0[0], z0[1]), mp.mpf(dt), tau_max)
        mp.mp.dps = 30
        dmax = 0.0; sign_mismatch = 0; ncommon = 0
        for q in r['records']:
            key = round(q['tau'], 6)
            if key in ref:
                ncommon += 1
                a = mp.mpc(*ref[key]['z']); b = mp.mpc(*q['z'])
                dmax = max(dmax, float(abs(a - b)))
                if (q['imdzdt'] > 0) != (ref[key]['imdzdt'] > 0): sign_mismatch += 1
        res[label] = dict(status=r['status'], n_common=ncommon, max_dist=dmax, sign_mismatch=sign_mismatch,
                          worst_increase_Im=r['worst_increase_Im'], n_pos=len(r['grid_pos_imdzdt']),
                          end_t1=r['end_t1'], landing=r['landing'])
        print(i, label, json.dumps(res[label])[:400], '%.0f s' % (time.time() - t0)); sys.stdout.flush()
    out['checks'].append(res)
    json.dump(out, open('../data/k%d-checks.json' % k, 'w'), indent=1)
