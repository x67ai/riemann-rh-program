#!/usr/bin/env python3
"""Interval (arb) evaluation of F_X(sigma) for S8(rho) from the block moments written by s8cert.c.

F_X(s) = S(s) + rho X^{1-s}/(s-1) - E(X) X^{-s},  X = x_K = 1 + (K - 1/2) t,  E(X) = e_K + 1/2 (exact),
S(s) = sum_{n <= X} n^{-s} = sum_b a_b^{-s} [ cnt_b + sum_{j=1}^{6} binom(-s,j) r_b^j Z_bj + R_b + P_b ]   (NOTE §3)
  a_b = 2^e (1 + i/256), r_b = 1/(256 + i), Z_bj in [lo_j, hi_j] 2^-62,
  |R_b| <= r_b^7 hi_7 2^-62 / (1 - r_b)                          (binomial tail, |binom(-s,j)| <= 1 for 0 < s <= 1)
  |P_b| <= cnt_b * s * 1.001 * 4.0003 * om_b * u * (1 + r_b)       (n~ vs n: |n~ - n| <= 4.0003 om u n~)
Usage: feval.py <file.mom> <rho_den: 16|32> [sigma ...]   (prints certified balls)
"""
import sys, re
from flint import arb, fmpq, ctx

ctx.prec = 200
U = arb(2) ** -53

def pm(b):
    """ball containing [-b, b] for an arb b >= 0"""
    return arb.union(-b, b)

class Moments:
    def __init__(self, path, den):
        self.den = den
        self.blocks = []
        with open(path) as fh:
            head = fh.readline()
            m = re.search(r"K=(\d+) N=(\d+) pi=(\d+) eK=(\d+)", head)
            self.K, self.N, self.pi, self.eK = map(int, m.groups())
            self.head = head.strip()
            for line in fh:
                if line.startswith('#'):
                    continue
                f = line.split()
                e, i, cnt, om = int(f[0]), int(f[1]), int(f[2]), int(f[3])
                lo = [int(x) for x in f[4:11]]; hi = [int(x) for x in f[11:18]]
                self.blocks.append((e, i, cnt, om, lo, hi))
        self.ntot = sum(b[2] for b in self.blocks)
        assert self.ntot == self.N, (self.ntot, self.N)   # every g-integer <= X is in exactly one block
        self.rho = arb.pi() / den
        self.t = den / arb.pi()
        self.X = 1 + (self.K - fmpq(1, 2)) * self.t
        self.EX = arb(fmpq(2 * self.eK + 1, 2))
        two62 = arb(2) ** -62
        self.pre = []
        for (e, i, cnt, om, lo, hi) in self.blocks:
            a = arb(2) ** (e - 8) * (256 + i)
            r = arb(fmpq(1, 256 + i))
            Z = [arb(cnt)] + [arb.union(arb(lo[j]) * two62, arb(hi[j]) * two62) for j in range(6)]
            rj = [arb(1)]
            for j in range(1, 8):
                rj.append(rj[-1] * r)
            rem = rj[7] * arb(hi[6]) * two62 / (1 - r)
            pert = arb(cnt) * arb("1.001") * arb("4.0003") * om * U * (1 + r)
            self.pre.append((a.log(), Z, rj, rem, pert))

    def S(self, s):
        s = arb(s)
        tot = arb(0)
        for (loga, Z, rj, rem, pert) in self.pre:
            acc = Z[0]
            b = arb(1)
            for j in range(1, 7):
                b = b * (-s - (j - 1)) / j
                acc += b * rj[j] * Z[j]
            acc += pm(rem) + pm(s * pert)
            tot += (-s * loga).exp() * acc
        return tot

    def F(self, s):
        s = arb(s)
        X = self.X
        return self.S(s) + self.rho * (X ** (1 - s)) / (s - 1) - self.EX * X ** (-s)

def tail_log2(s, X, K):
    """K * sigma * int_X^inf log^2 u u^{-s-1} du = K s X^{-s} (L^2/s + 2L/s^2 + 2/s^3), L = log X"""
    s = arb(s); L = X.log()
    return arb(K) * s * X ** (-s) * (L * L / s + 2 * L / s ** 2 + 2 / s ** 3)

def tail_pow(s, X, theta, C=1):
    """C * sigma * int_X^inf u^{theta-s-1} du = C s X^{theta-s}/(s-theta)"""
    s = arb(s); th = arb(theta)
    return arb(C) * s * X ** (th - s) / (s - th)

if __name__ == "__main__":
    mo = Moments(sys.argv[1], int(sys.argv[2]))
    print("#", mo.head)
    print(f"# K={mo.K} X={mo.X.str(15)} N={mo.N} E(X)={mo.eK}.5 blocks={len(mo.blocks)}")
    for a in sys.argv[3:]:
        f = mo.F(fmpq(*map(int, a.split('/'))) if '/' in a else arb(a))
        print(f"F({a}) = {f.str(15, radius=True)}")
