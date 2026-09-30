"""
monotone_check.py -- the ordering invariant on census files: list the zeros of a chain member in the
quarter-plane {Re s >= 1/2, Im s > 0} by increasing Im s; the invariant holds if the distance to the
line, Re s - 1/2, is nondecreasing along that list (real zeros have distance 0 and must all come first).
(In the t-variable, s = 1/2 + i t, this is: zeros in one quadrant listed by increasing real part have
nondecreasing |imaginary part|.)  Also reports the smallest distance to the line among off-line zeros.
Usage: python monotone_check.py census_*.json
"""
import sys, json
import mpmath as mp

mp.mp.dps = 30
for fn in sys.argv[1:]:
    rep = json.load(open(fn))
    zs = [(mp.mpf(t), mp.mpf(0)) for t in rep['real_zeros']]
    zs += [(mp.mpf(b), mp.mpf(a) - mp.mpf(1)/2) for (a, b) in rep['offline_zeros']]
    zs.sort(key=lambda x: x[0])
    viol = []
    for j in range(1, len(zs)):
        if zs[j][1] < zs[j - 1][1] - mp.mpf('1e-15'):
            viol.append((mp.nstr(zs[j - 1][0], 10), mp.nstr(zs[j - 1][1], 6), mp.nstr(zs[j][0], 10), mp.nstr(zs[j][1], 6)))
    offd = [d for (t, d) in zs if d > 0]
    print(f'{fn}: {len(zs)} zeros (quarter-plane), complete={rep.get("complete")}, violations={len(viol)}'
          + (f', min off-line distance = {mp.nstr(min(offd), 8)}' if offd else ''))
    for v in viol[:10]:
        print('   violation: (t, dist) =', v[:2], ' then ', v[2:])
