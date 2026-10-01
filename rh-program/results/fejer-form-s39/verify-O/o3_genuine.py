"""o3_genuine.py — read-O: genuine curves by brute force (own code; numpy point counts over F_q and F_{q^2}).
g = 1: every short Weierstrass y^2 = x^3 + ax + b (q = 5, 7, 11; disc != 0) -> traces.
g = 2: y^2 = f(x), f squarefree of degree 5 or 6 (q odd: every genus-2 curve). q = 5: EVERY f. q = 7: degree 6 with
leading coefficient in {1, nu} and x^5-coefficient 0 (translation + scaling by squares; covers every curve, since a
degree-5 model has a non-root c in F_7 to move infinity to), plus degree-5 forms with x^4-coefficient 0 as a cross-check.
(a1, a2) from N_1, N_2: a1 = N_1 - q - 1, a2 = (a1^2 - (q^2 + 1 - N_2))/2. Output o3_genuine.log, o3_genuine.json."""
import itertools, json
import numpy as np

def setup(q):
    nu = next(v for v in range(2, q) if pow(v, (q - 1) // 2, q) == q - 1)
    els = [(a, b) for b in range(q) for a in range(q)]            # a + b*i, i^2 = nu ; index a + q b
    mul = lambda x, y: ((x[0] * y[0] + nu * x[1] * y[1]) % q, (x[0] * y[1] + x[1] * y[0]) % q)
    sq = np.full(q * q, -1); sq[0] = 0
    for x in els[1:]:
        y = mul(x, x); sq[y[0] + q * y[1]] = 1
    pw = np.zeros((7, q * q, 2), dtype=np.int64)                  # x^k components
    for j, x in enumerate(els):
        p = (1, 0)
        for k in range(7):
            pw[k, j] = p; p = mul(p, x)
    chi1 = np.array([0] + [1 if pow(v, (q - 1) // 2, q) == 1 else -1 for v in range(1, q)])
    return nu, sq, pw, chi1

def squarefree(f, q):  # f: coefficient list low->high over F_q; gcd(f, f') == 1
    def trim(p):
        while p and p[-1] % q == 0: p = p[:-1]
        return p
    def pmod(a, b):
        a = trim([x % q for x in a]); b = trim(b); inv = pow(b[-1], q - 2, q)
        while len(a) >= len(b):
            c = a[-1] * inv % q; s = len(a) - len(b)
            for i in range(len(b)): a[s + i] = (a[s + i] - c * b[i]) % q
            a = trim(a)
        return a
    a, b = trim(list(f)), trim([(k * f[k]) % q for k in range(1, len(f))])
    if not b: return False
    while b: a, b = b, pmod(a, b)
    return len(a) == 1

def counts(F, q, sq, pw, chi1):  # F: array (n, 7) coeffs low->high, all over F_q
    deg = np.where(F[:, 6] % q != 0, 6, 5)
    re = np.einsum('nk,kj->nj', F, pw[:, :, 0]) % q; im = np.einsum('nk,kj->nj', F, pw[:, :, 1]) % q
    v2 = sq[re + q * im]                                          # chi over F_{q^2}
    base = np.arange(q)                                           # F_q = {a + 0 i}: indices 0..q-1
    v1 = chi1[re[:, base]]                                        # chi over F_q (NOT the F_{q^2} table)
    lead = np.where(deg == 6, F[:, 6], F[:, 5]) % q
    inf1 = np.where(deg == 6, 1 + chi1[lead], 1); inf2 = np.where(deg == 6, 2, 1)
    N1 = q + v1.sum(axis=1) + inf1; N2 = q * q + v2.sum(axis=1) + inf2
    a1 = N1 - q - 1; a2 = (a1 * a1 - (q * q + 1 - N2)) // 2
    return set(zip(a1.tolist(), a2.tolist()))

out, res = [], {}
for q in (5, 7, 11):
    ts = sorted({q + 1 - (1 + sum(1 + (0 if (x ** 3 + a * x + b) % q == 0 else (1 if pow((x ** 3 + a * x + b) % q, (q - 1) // 2, q) == 1 else -1)) for x in range(q)))
                 for a in range(q) for b in range(q) if (4 * a ** 3 + 27 * b * b) % q})
    out.append("q=%d genus 1: realized traces %s (%d)" % (q, ts, len(ts))); res["%d_1" % q] = ts
for q in (5, 7):
    nu, sq, pw, chi1 = setup(q)
    polys = []
    if q == 5:
        for c in itertools.product(range(q), repeat=7):
            if c[6] or c[5]: polys.append(c)
    else:
        for lead in (1, nu):
            for c in itertools.product(range(q), repeat=5):
                polys.append(tuple(c) + (0, lead))                # degree 6, x^5 coefficient 0
            for c in itertools.product(range(q), repeat=4):
                polys.append(tuple(c) + (0, lead, 0))             # degree 5, x^4 coefficient 0
    sf = [p for p in polys if squarefree(list(p), q)]
    F = np.array(sf, dtype=np.int64)
    S = set()
    for i in range(0, len(F), 20000): S |= counts(F[i:i + 20000], q, sq, pw, chi1)
    res["%d_2" % q] = sorted(S)
    out.append("q=%d genus 2: %d squarefree models of %d; realized (a1, a2): %d" % (q, len(sf), len(polys), len(S)))
data = json.load(open("o1_data.json"))
for q in (5, 7):
    rh = {tuple(r["a"]) for r in data["%d_2" % q] if r["kind"] == "RH"}
    allz = {tuple(r["a"]): r["kind"] for r in data["%d_2" % q]}
    S = set(map(tuple, res["%d_2" % q]))
    out.append("q=%d g=2: realized not in census: %d ; realized not RH-true: %d ; RH-true not realized: %d %s"
               % (q, len(S - set(allz)), sum(1 for x in S if allz.get(x) != "RH"), len(rh - S), sorted(rh - S) if q == 5 else ""))
open("o3_genuine.log", "w").write("\n".join(out) + "\n")
json.dump(res, open("o3_genuine.json", "w"))
print("\n".join(out))
