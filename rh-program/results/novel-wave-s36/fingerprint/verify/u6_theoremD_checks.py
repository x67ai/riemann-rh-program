"""
u6_theoremD_checks.py -- numerical checks of the Theorem D identities (task (d)).
(1) Lattice sum: the w-zeros of g_p(1/2 + i sqrt w), g_p(s) = (1 - p^-s)(1 - p^{s-1}), are w_k = (2 pi k/l + i/2)^2,
    k in Z (l = log p); sum_k 1/w_k = -l^2/(4 sinh^2(l/4)).  Hence c_0(xi g_p) = s_1(xi) - l^2/(4 sinh^2(l/4)).
    Compare with the Arb tables tables/eul-P_real_*.json (s_1 of xi*g_p computed from log(xi g_p) directly).
(2) Higher power sums: s_m(xi g_p) - s_m(xi) = sum_k w_k^{-m} (lattice), checked for m = 1..6.
(3) Hasse boundary: A + 2 cos(l t) has only real zeros iff |A| <= 2; the symmetrized Euler factor is
    p^{-1/2} (A_p - 2 cos(l t)) with A_p = sqrt p + 1/sqrt p > 2 (AM-GM), F_{a,q} has A = a/sqrt q.
"""
import json, os, mpmath as mp
mp.mp.dps = 40
here = os.path.dirname(os.path.abspath(__file__)); tab = os.path.join(os.path.dirname(here), 'tables')
Z = json.load(open(os.path.join(tab, 'zeta_real_P24000_S1000.json')))
sz = [None] + [mp.mpf(r['v']) for r in Z['s'][1:8]]
out = {}
for p in (2, 3, 7, 1000000007):
    E = json.load(open(os.path.join(tab, 'eul-%d_real_P3000_S60.json' % p)))
    se = [None] + [mp.mpf(r['v']) for r in E['s'][1:8]]
    l = mp.log(p)
    closed = -l ** 2 / (4 * mp.sinh(l / 4) ** 2)
    rows = []
    for m in range(1, 7):
        lat = mp.nsum(lambda k: 1 / ((2 * mp.pi * k / l + 0.5j) ** 2) ** m, [-mp.inf, mp.inf])
        rows.append((m, mp.nstr(se[m] - sz[m], 15), mp.nstr(mp.re(lat), 15), mp.nstr(abs(se[m] - sz[m] - mp.re(lat)), 3)))
    print('p =', p, ' c_0 = s_1(xi g_p) =', mp.nstr(se[1], 15), ' predicted s_1(xi) - l^2/(4 sinh^2(l/4)) =', mp.nstr(sz[1] + closed, 15))
    for r in rows:
        print('    m=%d  s_m(xi g_p)-s_m(xi) = %s   lattice sum = %s   |diff| = %s' % r)
    out[str(p)] = {'c0': mp.nstr(se[1], 20), 'pred': mp.nstr(sz[1] + closed, 20), 'rows': rows}
json.dump(out, open(os.path.join(here, 'u6_theoremD_checks.json'), 'w'), indent=1, default=str)
