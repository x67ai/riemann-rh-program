"""
u5b_dh_offline.py -- locate Davenport-Heilbronn off-line zeros up to t = 260 (dh.py conventions) and map each one
to the S-index where the DH fingerprint shows its '-+-' motif (turning point t_n = 1/(2 sqrt al_n) of the
neighbouring positive coefficients).  Tests the visibility law: n_fail(T) ~ first n with t_n >= T.
"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'ccm-dh-test'))
import mpmath as mp
import dh
mp.mp.dps = 25
found = []
for (t0, t1) in [(60, 130), (130, 200), (200, 262)]:
    offs = dh.offline_scan((mp.mpf('0.52'), mp.mpf('1.2')), (mp.mpf(t0), mp.mpf(t1)), 12, int((t1 - t0) * 2.2))
    for r in offs:
        if r.real > 0.5 + 1e-8 and not any(abs(r - f) < 1e-6 for f in found):
            found.append(r)
found.sort(key=lambda z: z.imag)
print('DH off-line zeros (Re s > 1/2) with t <= 262:')
for r in found:
    print('   ', mp.nstr(r, 15), ' |f| =', mp.nstr(abs(dh.f_dh(r)), 3))
here = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(here, '..', 'tables', 'dh_real_P16000_S600.json')))
al = [mp.mpf(x['v']) for x in D['al']]
sg = D['al_signs']
motifs = [i + 1 for i in range(len(sg) - 2) if sg[i] == '-' and sg[i + 2] == '-' and sg[i + 1] == '+']
print('fingerprint -+- motifs start at S-index:', motifs)
rows = []
for m in motifs:
    # turning point just before the motif (last three positive, regular coefficients)
    tp = [1 / (2 * mp.sqrt(al[k - 1])) for k in range(m - 6, m - 1) if al[k - 1] > 0]
    rows.append({'motif_start': m, 'turning_points_before': [mp.nstr(x, 6) for x in tp]})
    print('  motif at', m, ' turning points t_n for n =', m - 6, '..', m - 2, ':', [mp.nstr(x, 5) for x in tp])
json.dump({'offline_zeros': [mp.nstr(r, 15) for r in found], 'motifs': rows},
          open(os.path.join(here, 'u5b_dh_offline.json'), 'w'), indent=1)
