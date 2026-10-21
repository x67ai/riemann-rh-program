"""Rigorous certificate for the revised primary finite atom-only theorem.

Run: python3 certificate.py
Dependency: python-flint==0.6.0. All model inputs are exact integers or decimal
rationals in witness-data.json. No optimizer, floating-point rationalization,
coordinate snapping, or feasibility grace enters this certificate.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
from flint import arb, acb, acb_mat, ctx

ctx.prec = 256
BASE = Path(__file__).resolve().parent
raw = (BASE / 'witness-data.json').read_bytes()
data = json.loads(raw)

def exact(value):
    q = Fraction(str(value))
    return arb(q.numerator) / q.denominator

def inertia_above(h, threshold):
    n = h.nrows()
    lower = [[acb(0) for _ in range(n)] for _ in range(n)]
    pivots = []
    for i in range(n):
        value = acb(threshold) - h[i, i]
        for j in range(i):
            value -= lower[i][j] * lower[i][j].conjugate() * pivots[j]
        pivot = value.real  # the exact Hermitian Schur pivot is real
        if not (pivot > 0 or pivot < 0):
            raise RuntimeError(('unresolved LDL pivot', threshold, i, str(pivot)))
        pivots.append(pivot)
        lower[i][i] = acb(1)
        for k in range(i + 1, n):
            value = -h[k, i]
            for j in range(i):
                value -= lower[k][j] * lower[i][j].conjugate() * pivots[j]
            lower[k][i] = value / pivot
    return sum(d < 0 for d in pivots)

N, M, mp = data['N'], data['grid_size'], data['half_band_size']
assert (N, M, mp) == (64, 65, 33)
rows, counts = [], []
for column in data['columns']:
    marks = column['marks']
    assert len(marks) == M and all(type(m) is int and 0 <= m <= 2 for m in marks)
    assert sum(marks) == N
    assert sum(m > 0 for m in marks) == column['distinct']
    assert sum(m == 1 for m in marks) == column['simple']
    assert sum(m*m for m in marks) == column['F1']
    coeff = {}
    for s in range(mp):
        coeff[s] = sum((acb(0, arb.pi() * (-2*s*k) / M).exp() * m
                        for k, m in enumerate(marks) if m), acb(0))
        if s:
            coeff[-s] = coeff[s].conjugate()
    h = acb_mat([[coeff[j-k] / mp for k in range(mp)] for j in range(mp)])
    h2, h3 = h*h, h*h*h
    fp = sum((h2[j,j].real for j in range(mp)), arb(0))
    cp = sum((h3[j,j].real for j in range(mp)), arb(0))
    rows.append([exact(column['F1']), fp, cp])
    counts.append([inertia_above(h, v) for v in (2,3,4)])
assert counts == [[0,0,0],[16,2,0],[3,2,0]]

b1, b2, b3 = (exact(data[k]) for k in ('B1','B2','B3'))
eps = exact(data['epsilon'])
u = b1 * (1+eps)
r = (u-64)/32
c0,c1,c2 = (row[2] for row in rows)
denominator = c0 - 2*c1 + c2
assert denominator < 0
w2 = (b3-c0*(1-r)-c1*r)/denominator
w1 = r-2*w2
w0 = 1-r+w2
weights = [w0,w1,w2]
assert all(w>0 for w in weights)
mean_fp = sum((w*row[1] for w,row in zip(weights,rows)),arb(0))
fp_margins = [mean_fp-b2*(1-eps),b2*(1+eps)-mean_fp]
assert all(v>0 for v in fp_margins)

# The equalities sum w=1, E[F1]=u and E[Cp]=B3 hold by the defining algebra.
# Only strict inequalities and inertia decisions require interval checks.
# Atom matrices are PSD, so |eigenvalue|=eigenvalue.
mean_n2 = sum((weights[j]*counts[j][0] for j in range(3)),arb(0))
mean_n3 = sum((weights[j]*counts[j][1] for j in range(3)),arb(0))
C = exact(data['C_ladder'])
buckets = {
    '0<V<=2': C*N/(2**4)-mp,
    '2<V<=3': C*N/(3**4)-mean_n2,
    '3<V<4': C*N/(4**4)-mean_n3,
}
assert all(v>0 for v in buckets.values())
# At V>=4 all counts are zero; at V=2,3 LDL proves no eigenvalue equals V.

corner_nd = (Fraction(3*N)-Fraction(data['B1'])*(1+Fraction(data['epsilon'])))/(2*N)
corner_p1 = 2-Fraction(data['B1'])*(1+Fraction(data['epsilon']))/N
result = {
    'status':'PASS', 'arithmetic':'Arb 256-bit outward balls via python-flint',
    'data_sha256':hashlib.sha256(raw).hexdigest(),
    'row_enclosures':[[str(v) for v in row] for row in rows],
    'counts_at_2_3_4':counts,'weight_enclosures':[str(v) for v in weights],
    'denominator':str(denominator),'mean_Fp':str(mean_fp),
    'Fp_strict_margins':[str(v) for v in fp_margins],
    'all_threshold_bucket_margins':{k:str(v) for k,v in buckets.items()},
    'equalities':'By exact definitions: sum weights=1, mean F1=B1(1+epsilon), mean Cp=B3',
    'cubic_absolute_slack':str(eps*N),
    'distinct_corner_exact':str(corner_nd),'simple_corner_exact':str(corner_p1),
    'scope':'One N=64 atom-only model with all-V ladder C=10 (and hence every C>=10).',
}
(BASE/'certificate-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
