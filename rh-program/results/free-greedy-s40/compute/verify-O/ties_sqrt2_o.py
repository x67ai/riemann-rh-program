# ties_sqrt2_o.py -- exact product coincidences among lattice points L = 1 + (k - 1/2) sqrt2 (= (m + sqrt2)/sqrt2, m = 2k-1)
# products of r lattice points = prod(m_i + sqrt2) / sqrt2^r ; search r = 3 (same length) exactly in Z[sqrt2]. Opus reader.
from itertools import combinations_with_replacement as cwr
M = 401
odd = list(range(1, M + 1, 2))
seen = {}; hits = []
for tr in cwr(odd, 3):
    a, b = 1, 0
    for m in tr: a, b = a * m + 2 * b, a + b * m        # (a + b s)(m + s) = (am + 2b) + (a + bm) s
    key = (a, b)
    if key in seen: hits.append((seen[key], tr))
    else: seen[key] = tr
print(f"triples of odd m <= {M}: {len(seen)} distinct products, {len(hits)} coincidences")
for h in hits[:12]:
    (p, q) = h; kp = tuple((m + 1) // 2 for m in p); kq = tuple((m + 1) // 2 for m in q)
    import math
    val = math.prod(1 + (k - 0.5) * math.sqrt(2) for k in kp)
    print("k-triples", kp, kq, "product %.6f" % val)
