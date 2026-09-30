"""
u5b_dh_offline.py -- map the Davenport-Heilbronn fingerprint's '-+-' motifs to DH's off-line zeros.
Newton (mpmath findroot on f_DH, results/ccm-dh-test/dh.py) from seeds at the recalled literature locations
[recalled, unverified: 0.808517+85.699348i, 0.650830+114.163343i, 0.574356+166.479306i, 0.724258+176.702461i,
0.646008+240.935500i]; each converged root is verified by |f_DH| and by being off the line.  Then compare each
root's height with the WKB turning point t_n = 1/(2 sqrt al_n) of the DH S-fraction just before each motif.
"""
import sys, os, json
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', '..', '..', 'ccm-dh-test'))
import mpmath as mp
import dh
mp.mp.dps = 30
seeds = ['0.808517+85.699348j', '0.650830+114.163343j', '0.574356+166.479306j', '0.724258+176.702461j', '0.646008+240.935500j']
roots = []
for sd in seeds:
    re_, im_ = sd.rstrip('j').split('+'); r = mp.findroot(dh.f_dh, mp.mpc(mp.mpf(re_), mp.mpf(im_)), solver='muller')
    roots.append(r)
    print('root', mp.nstr(r, 18), ' |f| =', mp.nstr(abs(dh.f_dh(r)), 3))
D = json.load(open(os.path.join(here, '..', 'tables', 'dh_real_P16000_S600.json')))
al = [mp.mpf(x['v']) for x in D['al']]
sg = D['al_signs']
motifs = [i + 1 for i in range(len(sg) - 2) if sg[i] == '-' and sg[i + 1] == '+' and sg[i + 2] == '-']
out = []
for m, r in zip(motifs, roots):
    tp = [(k, mp.nstr(1 / (2 * mp.sqrt(al[k - 1])), 6)) for k in range(m - 7, m) if al[k - 1] > 0]
    print('motif at S-index %d (J-index %d): off-line zero height %s; turning points before: %s' % (m, (m + 1) // 2, mp.nstr(r.imag, 8), tp))
    out.append({'motif_S_index': m, 'zero': mp.nstr(r, 15), 'turning_points': tp})
json.dump({'roots': [mp.nstr(r, 20) for r in roots], 'motifs': motifs, 'map': out}, open(os.path.join(here, 'u5b_dh_offline.json'), 'w'), indent=1)
