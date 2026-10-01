#!/usr/bin/env python3
"""Proof that F_X is strictly concave on [sigma_a, 1) (NOTE §6, Lemma 6.3), from the block moments.

F_X''(s) = zeta_c''(s) + int_1^X E(u) u^{-s-1} (s log^2 u - 2 log u) du,  zeta_c'' = -2 rho/(1-s)^3, so for s >= sigma_a
F_X''(s) <= -2 rho/(1-sigma_a)^3 + Q,   Q := int_1^X |E| u^{-sigma_a-1}(2 log u + log^2 u) du,
and |E| <= E + 2 max(0, -floor) <= E + 1 (Lemma 1.1) gives Q <= 2 A_1 + A_2 + 2/sa^2 + 2/sa^3, A_m := int_1^X E u^{-sa-1} log^m u du.
A_m = int N w_m - int T w_m with w_m = u^{-s-1} log^m u:
  int_1^X N w_m = N(X) W_m(X) + sum_n n^{-s} P_m(log n),  W_m(u) = -u^{-s} P_m(log u),
  P_0 = 1/s, P_1 = L/s + 1/s^2, P_2 = L^2/s + 2L/s^2 + 2/s^3;
  int_1^X T w_m = rho J_m(1-s) + (1-rho)(W_m(X) - W_m(1)),  J_m(b) = int_1^X u^{b-1} log^m u du.
S_m(s) = sum_{n<=X} n^{-s} log^m n from the block moments: n^{-s} log^m n = a^{-s} sum_i C(m,i) log^{m-i}a * g_i(x),
g_i(x) = (1+x)^{-s} log^i(1+x) = sum_j c_ij x^j, |tail_{j>=7}| <= 15 x^7 (x <= 2^-8); perturbation n~ vs n bounded below.
Self-tests: A_0 = (F_X - zeta_c)/s; S_1 = -S'(s) against a central difference.
Usage: concavity.py <file.mom> <den> <sigma_a>"""
import sys
from flint import arb, fmpq
from feval import Moments, U, pm

def Sm(mo, s):
    s = arb(s)
    b = [arb(1)]
    for j in range(1, 7):
        b.append(b[-1] * (-s - (j - 1)) / j)
    l = [arb(0)] + [arb((-1) ** (k + 1)) / k for k in range(1, 7)]
    l2 = [sum((l[i] * l[k - i] for i in range(1, k)), arb(0)) for k in range(7)]
    c = [b,
         [sum((l[k] * b[j - k] for k in range(1, j + 1)), arb(0)) for j in range(7)],
         [sum((l2[k] * b[j - k] for k in range(2, j + 1)), arb(0)) for j in range(7)]]
    out = [arb(0), arb(0), arb(0)]
    for (loga, Z, rj, rem, pert), (e, i, cnt, om, lo, hi) in zip(mo.pre, mo.blocks):
        G = []
        tail = 15 * rj[7] * arb(hi[6]) * arb(2) ** -62
        for ii in range(3):
            acc = sum((c[ii][j] * rj[j] * Z[j] for j in range(7)), arb(0))
            G.append(acc + pm(tail))
        w = (-s * loga).exp()
        Lb = (loga.exp() * (1 + rj[1])).log()           # >= log n for n in the block
        for m in range(3):
            if m == 0: val = G[0]
            elif m == 1: val = loga * G[0] + G[1]
            else: val = loga * loga * G[0] + 2 * loga * G[1] + G[2]
            p = arb(cnt) * arb("1.001") * (2 + Lb) ** m * arb("4.0003") * om * U * (1 + rj[1])
            out[m] += w * (val + pm(p))
    return out

def A_m(mo, s, S):
    s = arb(s); X = mo.X; L = X.log(); rho = mo.rho; b = 1 - s
    P = [lambda L_: 1 / s, lambda L_: L_ / s + 1 / s ** 2, lambda L_: L_ ** 2 / s + 2 * L_ / s ** 2 + 2 / s ** 3]
    W = lambda m, u, Lu: -(u ** (-s)) * P[m](Lu)
    Xb = X ** b
    J = [(Xb - 1) / b, Xb * (L / b - 1 / b ** 2) + 1 / b ** 2, Xb * (L ** 2 / b - 2 * L / b ** 2 + 2 / b ** 3) - 2 / b ** 3]
    sumP = [S[0] / s, S[1] / s + S[0] / s ** 2, S[2] / s + 2 * S[1] / s ** 2 + 2 * S[0] / s ** 3]
    out = []
    for m in range(3):
        intN = mo.N * W(m, X, L) + sumP[m]
        intT = rho * J[m] + (1 - rho) * (W(m, X, L) - W(m, arb(1), arb(0)))
        out.append(intN - intT)
    return out

if __name__ == "__main__":
    mo = Moments(sys.argv[1], int(sys.argv[2]))
    sa = fmpq(*[int(v) for v in sys.argv[3].split('/')]) if '/' in sys.argv[3] else arb(sys.argv[3])
    print("#", mo.head[:120])
    S = Sm(mo, sa)
    A = A_m(mo, sa, S)
    zc = 1 - mo.rho / (1 - arb(sa))
    print(f"S0 = {S[0].str(15)}  S(sigma) from feval = {mo.S(sa).str(15)}")
    h = fmpq(1, 10**6)
    num = -(mo.S(arb(sa) + h) - mo.S(arb(sa) - h)) / (2 * h)
    print(f"S1 = {S[1].str(12)}  central difference -S' = {num.str(12)}  S2 = {S[2].str(12)}")
    print(f"selftest A_0 = {A[0].str(12)}  (F_X - zeta_c)/sigma = {((mo.F(sa) - zc) / arb(sa)).str(12)}")
    print(f"A_1 = {A[1].str(10)}  A_2 = {A[2].str(10)}")
    s = arb(sa)
    Q = 2 * A[1] + A[2] + 2 / s ** 2 + 2 / s ** 3
    need = 2 * mo.rho / (1 - s) ** 3
    print(f"Q <= {Q.str(10)}   2 rho/(1 - sigma_a)^3 = {need.str(10)}   concave on [sigma_a, 1): {bool(Q < need)}")
