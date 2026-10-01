#!/usr/bin/env python3
"""concavity_O.py D K base sigma_a — re-derivation of NOTE Lemma 6.3's numbers (read-O, U6).
A_m := int_1^X E(u) u^(-s-1) log^m u du (s = sigma_a, X = x_K) = I_m - J_m with
  I_m = int_1^X N u^(-s-1) log^m u du = sum_{n<=X} G_m(n) - N(X) G_m(X),  G_m(y) = int_y^oo u^(-s-1) log^m u du,
  J_m = int_1^X (rho u + 1 - rho) u^(-s-1) log^m u du   (closed form).
Per block: sum_n G_m(n) = cnt G_m(g0) + G_m'(g0) t S1 + R, |R| <= (1/2) sup_block |G_m''| t^2 S2 (n - g0 = t Delta).
Self-test: A_0 = (F_X(s) - zeta_c(s))/s. Output: Q-bound 2A_1 + A_2 + 2/s^2 + 2/s^3 against 2 rho/(1 - s)^3."""
import sys, struct
from math import factorial
from flint import arb, fmpq
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from feval_O import System, MOM, i128, u128

D, K, base = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
s = arb(fmpq(int(sys.argv[4].replace(".", "")), 10 ** len(sys.argv[4].split(".")[1])))
S = System(D, K, base); t, rho, X = S.t, S.rho, S.X

def G(m, y):
    l = y.log()
    P = [1 / s, l / s + 1 / s ** 2, l ** 2 / s + 2 * l / s ** 2 + 2 / s ** 3][m]
    return y ** (-s) * P
def G1(m, y): return -(y ** (-s - 1)) * y.log() ** m
def G2(m, y):
    l = y.log(); return y ** (-s - 2) * ((s + 1) * l ** m - (m * l ** (m - 1) if m else 0))
def H(a, m):                     # int_1^X u^(a-1) log^m u du
    l = X.log()
    up = X ** a * sum(((-1) ** i * factorial(m) // factorial(m - i) * l ** (m - i) / a ** (i + 1) for i in range(m + 1)), arb(0))
    return up - (-1) ** m * factorial(m) / a ** (m + 1)

blocks = []
with open(base + ".blk", "rb") as f:
    nb = struct.unpack("<Q", f.read(8))[0]
    for idx in range(nb):
        rec = MOM.unpack(f.read(MOM.size))
        if rec[0] == 0: continue
        j = 16 + (idx >> 14); i = idx & 16383; L = 2 ** (j - 14); W0 = 2 ** j + i * L - 1 + L // 2
        cnt, s1lo, s1hi, s2, a2 = rec[0], i128(rec[1]), i128(rec[2]), i128(rec[3]), u128(rec[4])
        g0 = 1 + (arb(W0) - arb(1) / 2) * t
        S1 = arb(fmpq(s1lo + s1hi, 2 ** 65), fmpq(s1hi - s1lo, 2 ** 65))
        S2up = arb(fmpq(s2 + 4 * a2 + 4 * cnt, 2 ** 64))
        gball = arb(g0.mid(), (t * L / 2 + g0.rad()).upper())
        blocks.append((cnt, g0, S1, S2up, gball))
A = []
for m in range(3):
    tot = sum((G(m, n) for cell, n in S.ind), arb(0))
    rem = arb(0)
    for cnt, g0, S1, S2up, gb in blocks:
        tot += cnt * G(m, g0) + G1(m, g0) * t * S1
        rem += abs(G2(m, gb)).upper() / 2 * t ** 2 * S2up
    I = tot + arb(0, rem.upper()) - S.Ntot * G(m, X)
    J = rho * H(1 - s, m) + (1 - rho) * H(-s, m)
    A.append(I - J)
    print("A_%d(%s) = %s   [Taylor remainder bound %s]" % (m, sys.argv[4], A[m].str(12, radius=True), rem.str(3)))
zc = (s - 1 + rho) / (s - 1)
print("self-test: (F_X(s) - zeta_c(s))/s = %s" % ((S.F(s) - zc) / s).str(12, radius=True))
Q = 2 * A[1] + A[2] + 2 / s ** 2 + 2 / s ** 3
print("Q <= 2A_1 + A_2 + 2/s^2 + 2/s^3 = %s ;  2 rho/(1 - s)^3 = %s" % (Q.str(6, radius=True), (2 * rho / (1 - s) ** 3).str(6)))
