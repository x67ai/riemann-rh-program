#!/usr/bin/env python3
"""feval_O.py — rigorous ball evaluation of F_X(s) = sum_{n<=X} n^-s + rho X^(1-s)/(s-1) - E(X) X^-s for S8(pi/D) at the
lattice point X = x_K, from the integer moments written by s8gen (read-O, U6). python-flint arb, pi = arb's constant.
Per block (cells [2^j + iL, 2^j + (i+1)L), L = 2^(j-14), centre W0, lambda = W0 - 1/2 + rho, g0 = t lambda, h = (L/2)/lambda):
  sum_{n in block} n^-s = g0^-s [cnt + c1 S1/lambda + c2 S2/lambda^2 + c3 S3/lambda^3 + R],  c_k = binom(-s, k),
  |R| <= cnt |c4| h^4 (1 - h)^(-s-4)   (Lagrange remainder of (1 + delta)^-s, |delta| <= h),
with S1 in [s1lo, s1hi] 2^-64, S2 = s2 2^-64 +- (4 a2 + 4 cnt) 2^-64, S3 = s3 2^-48 +- (6 q3 + 12 a3 + 8 cnt) 2^-48.
Individually stored g-integers (cells < 2^16): n = 1 + (W - 1/2) t with W in [lo, hi] 2^-F."""
import struct, sys
from flint import arb, fmpq, ctx

F = 90
MOM = struct.Struct("<Q8x" + "16s" * 7 + "QQ")      # cnt, pad, s1lo s1hi s2 a2 s3 q3 a3, wmax, pad (144 bytes)

def i128(b): return int.from_bytes(b, "little", signed=True)
def u128(b): return int.from_bytes(b, "little", signed=False)

class System:
    def __init__(self, D, K, base, prec=256):
        ctx.prec = prec
        self.D, self.K = D, K
        self.pi = arb.pi(); self.t = arb(D) / self.pi; self.rho = self.pi / D
        self.X = 1 + (arb(K) - arb(1) / 2) * self.t
        self.ind = []
        with open(base + ".ind", "rb") as f:
            n = struct.unpack("<Q", f.read(8))[0]
            for _ in range(n):
                cell = struct.unpack("<Q", f.read(8))[0]; lo = u128(f.read(16)); hi = u128(f.read(16))
                W = arb(fmpq(lo + hi, 2 ** (F + 1)), fmpq(hi - lo, 2 ** (F + 1)))   # ball [lo, hi] 2^-F
                self.ind.append((cell, 1 + (W - arb(1) / 2) * self.t))
        self.blocks = []; self.Ntot = len(self.ind)
        with open(base + ".blk", "rb") as f:
            nb = struct.unpack("<Q", f.read(8))[0]
            for idx in range(nb):
                rec = MOM.unpack(f.read(MOM.size))
                cnt = rec[0]
                if cnt == 0: continue
                s1lo, s1hi, s2, a2, s3, q3, a3 = (i128(rec[1]), i128(rec[2]), i128(rec[3]), u128(rec[4]),
                                                  i128(rec[5]), u128(rec[6]), u128(rec[7]))
                j = 16 + (idx >> 14); i = idx & 16383; L = 2 ** (j - 14)
                W0 = 2 ** j + i * L - 1 + L // 2
                lam = arb(W0) - arb(1) / 2 + self.rho
                S1 = arb(fmpq(s1lo + s1hi, 2 ** 65), fmpq(s1hi - s1lo, 2 ** 65))
                S2 = arb(fmpq(s2, 2 ** 64), fmpq(4 * a2 + 4 * cnt, 2 ** 64))
                S3 = arb(fmpq(s3, 2 ** 48), fmpq(6 * q3 + 12 * a3 + 8 * cnt, 2 ** 48))
                h = arb(L) / 2 / lam
                self.blocks.append((cnt, (self.t * lam).log(), S1 / lam, S2 / lam ** 2, S3 / lam ** 3, h ** 4, 1 - h))
                self.Ntot += cnt
        self.EX = arb(self.Ntot) - self.K - arb(1) / 2

    def F(self, s, terms=False):
        s = arb(fmpq(*s)) if isinstance(s, tuple) else arb(s)
        c1 = -s; c2 = s * (s + 1) / 2; c3 = -s * (s + 1) * (s + 2) / 6; c4 = s * (s + 1) * (s + 2) * (s + 3) / 24
        tot_ind = arb(0)
        for cell, n in self.ind:
            tot_ind += (-s * n.log()).exp()
        tot_blk = arb(0); rem = arb(0)
        for cnt, lg0, A1, A2, A3, h4, omh in self.blocks:
            g0s = (-s * lg0).exp()
            tot_blk += g0s * (cnt + c1 * A1 + c2 * A2 + c3 * A3)
            rem += g0s * cnt * c4 * h4 * omh ** (-s - 4)
        R = arb(0, rem.upper())                         # |R_total| <= rem
        main = self.rho * self.X ** (1 - s) / (s - 1) - self.EX * self.X ** (-s)
        val = tot_ind + tot_blk + R + main
        if terms:
            return val, dict(ind=tot_ind, blk=tot_blk, rem=rem, main=main)
        return val

if __name__ == "__main__":
    D, K, base = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    S = System(D, K, base)
    print("D=%d K=%d X=%s N(X)=%d E(X)=%s blocks=%d individual=%d" % (D, K, S.X.str(25), S.Ntot, S.EX.str(5),
          len(S.blocks), len(S.ind)))
    for sv in sys.argv[4:]:
        v, tm = S.F(fmpq(int(sv.replace(".", "")), 10 ** len(sv.split(".")[1])), terms=True)
        print("F(%s) = %s   [remainder bound %s]" % (sv, v.str(20, radius=True), tm["rem"].str(3)))
