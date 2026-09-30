"""Unit fejer-form-s39, rung 1: the one positions-side inequality that is GEOMETRIC, not free.  Class-summed Clifford
(l(D) <= deg D/2 + 1 for 0 <= deg D <= 2g-2, l integral): Theta_n <= h q^{floor(n/2)+1}.  At g = 2 the only non-identity case
is n = 1: (q-1)A_1 + h <= h q, i.e. N_1 <= h (a genus >= 1 curve has C(F_q) -> Pic^1 injective).  n = 2 = 2g-2 is (R), an identity.
In angles: h - N_1 = (q - x1)(q - x2) + q (x_j = 2 sqrt q cos theta_j).  Tested on every zeta datum at q = 5, 7, 11."""
import json
Z = json.load(open('r1_zeta_data.json')); G = json.load(open('r1_genuine.json'))
for q in (5, 7, 11):
    rows = [r for r in Z[str(q)] if r['g'] == 2]
    bad = [r for r in rows if r['N'][0] > r['h']]
    ident = all(r['h'] - r['N'][0] == (q * q - q * (-r['a1']) + (r['a2'] - 2 * q)) + q for r in rows)   # (q-x1)(q-x2) = q^2 - q(x1+x2) + x1 x2
    gen = set(map(tuple, G.get('g2_q%d' % q, [])))
    print("q=%d g=2: data %d; N_1 > h (Clifford violated): %d (RH-false among them: %d; genuine among them: %d); identity h - N_1 = (q-x1)(q-x2)+q: %s"
          % (q, len(rows), len(bad), sum(not r['rh'] for r in bad), sum((r['a1'], r['a2']) in gen for r in bad), ident))
    if bad: print("   violators (a1, a2, N_1, h):", [(r['a1'], r['a2'], r['N'][0], r['h']) for r in bad][:12])
    nr = [r for r in rows if r['kind'] == 'nonreal-x']
    print("   non-real-x RH-false data (the 111-type): %d, caught by Clifford: %d" % (len(nr), sum(r['N'][0] > r['h'] for r in nr)))
