"""o2_toeplitz_exact.py — read-O: exact PSD test of the Toeplitz matrices T_M(Z) = [p_|a-b|], p_n = s_n q^{-n/2}.
Route (different from verify/r1_lp.py's float eigenvalues): T_M is congruent, via D = diag(q^{a/2}), to the INTEGER
matrix H_M = [s_|a-b| q^{min(a,b)}]_{a,b=0..M} (s_0 = 2g), so T_M is PSD iff H_M is; H_M is tested by exact
symmetric elimination over Fractions with largest-diagonal pivoting (a PSD matrix has max diagonal >= 0, and a zero
pivot row must vanish). Input: o1_data.json. Output: o2_toeplitz_exact.log."""
import json
from fractions import Fraction
from collections import Counter
import mpmath as mp

def psd_exact(H):
    A = [[Fraction(x) for x in row] for row in H]
    idx = list(range(len(A)))
    while idx:
        p = max(idx, key=lambda i: A[i][i])
        d = A[p][p]
        if d < 0: return False
        if d == 0:
            if any(A[p][j] != 0 for j in idx): return False
            idx.remove(p); continue
        idx.remove(p)
        for i in idx:
            f = A[i][p] / d
            if f:
                for j in idx: A[i][j] -= f * A[p][j]
    return True

def power_sums(c, nmax):
    s = [0] * (nmax + 1)
    for k in range(1, nmax + 1):
        acc = -k * (c[k] if k < len(c) else 0)
        for j in range(1, k):
            if k - j < len(c): acc -= s[j] * c[k - j]
        s[k] = acc
    return s

def Lc(q, g, a):
    c = [1] + list(a) + [0] * g
    for k in range(g + 1, 2 * g + 1): c[k] = q ** (k - g) * c[2 * g - k]
    return c

def H(q, s, M): return [[s[abs(a - b)] * q ** min(a, b) for b in range(M + 1)] for a in range(M + 1)]

data = json.load(open("o1_data.json"))
out = []
for key, rows in data.items():
    q, g = map(int, key.split("_"))
    first = Counter(); rh_bad = 0
    for r in rows:
        s = power_sums(Lc(q, g, r["a"]), 8); s[0] = 2 * g
        if r["kind"] == "RH":
            if not all(psd_exact(H(q, s, M)) for M in range(1, 9)): rh_bad += 1
        else:
            m = next((M for M in range(1, 9) if not psd_exact(H(q, s, M))), None)
            first[m] += 1
    out.append("q=%d g=%d: RH-true %d, of which not PSD for some M <= 8: %d ; RH-false %d, first failing M: %s"
               % (q, g, sum(1 for r in rows if r["kind"] == "RH"), rh_bad, sum(first.values()), dict(sorted(first.items(), key=lambda t: str(t[0])))))
# V closed form: T_M(V) = u v^T + v u^T, lambda_min = (M+1) - sqrt(P_M), P_M = (M+1) + sum_{d=1}^M (M+1-d) Lucas_{2d}
luc = [2, 1]
for _ in range(40): luc.append(luc[-1] + luc[-2])
mp.mp.dps = 30
vals = []
for M in range(1, 9):
    P = (M + 1) + sum((M + 1 - d) * luc[2 * d] for d in range(1, M + 1))
    vals.append((M, P, mp.nstr((M + 1) - mp.sqrt(P), 12)))
out.append("V: P_M = |u|^2|v|^2 (exact integers) and lambda_min(T_M(V)): %s" % vals)
# cross-check against mpmath eigenvalues of T_M(V) itself
phi = (1 + mp.sqrt(5)) / 2
for M in (1, 2, 8):
    T = mp.matrix(M + 1, M + 1)
    for a in range(M + 1):
        for b in range(M + 1): T[a, b] = phi ** abs(a - b) + phi ** (-abs(a - b))
    out.append("   M=%d mpmath eigsy min = %s" % (M, mp.nstr(min(mp.eigsy(T)[0]), 12)))
# V2 and E0
for name, q, g, a in (("V2", 5, 2, (-1, 11)), ("E0", 5, 1, (-4,)), ("V", 5, 1, (-5,))):
    s = power_sums(Lc(q, g, a), 8); s[0] = 2 * g
    lam = []
    for M in (1, 2, 3):
        T = mp.matrix(M + 1, M + 1)
        for i in range(M + 1):
            for j in range(M + 1): T[i, j] = s[abs(i - j)] / mp.sqrt(q) ** abs(i - j)
        lam.append(mp.nstr(min(mp.eigsy(T)[0]), 7))
    I = g - mp.mpf(s[1]) / (2 * mp.sqrt(q))
    out.append("%s: lambda_min(T_1..3) = %s ; I(Z) = g - (q+1-N_1)/(2 sqrt q) = %s" % (name, lam, mp.nstr(I, 10)))
open("o2_toeplitz_exact.log", "w").write("\n".join(out) + "\n")
print("\n".join(out))
