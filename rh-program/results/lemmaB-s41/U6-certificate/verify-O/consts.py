#!/usr/bin/env python3
"""consts.py — certified integer constants for the second-producer generator s8gen.c (read-O, U6).

For S8(pi/D), t = D/pi, the generator decides every cell by W(c) = (E_1+1)/2 + sum_{r>=2} E_r * kappa_r,
kappa_r = t^(r-1)/2^r (E_r = elementary symmetric functions of b_i = 2 n_i - 1 over the factors x_{n_i}).
This script writes K_r = floor(kappa_r 2^F) (F = 90) and KH_r = floor(kappa_r 2^320), and for every integer
checkpoint V the enclosures floor(w(V) 2^F), floor(w(V) 2^320), w(V) = pi (V - 1)/D + 1/2.
Each constant is certified TWICE and the two must agree exactly:
  (a) arb (python-flint) at 1200 bits: the ball times 2^F must lie strictly inside (k, k+1);
  (b) exact rationals: pi enclosed by Machin's formula 16 atan(1/5) - 4 atan(1/239), each atan bracketed by
      consecutive partial sums of its alternating series (terms decrease), then both ends of the induced
      interval of the constant floor to the same integer.
Usage: consts.py D KFIN out_params
"""
import sys
from fractions import Fraction as Fr
from flint import arb, ctx

D = int(sys.argv[1]); KFIN = int(sys.argv[2]); OUT = sys.argv[3]
F, F2, R = 90, 320, 40

def atan_bracket(x, nterms):
    # atan(1/x) = sum_k (-1)^k / ((2k+1) x^(2k+1)); alternating, decreasing terms
    s = Fr(0); sums = []
    for k in range(nterms + 2):
        s += Fr((-1) ** k, (2 * k + 1) * x ** (2 * k + 1)); sums.append(s)
    a, b = sums[-1], sums[-2]
    return (min(a, b), max(a, b))

l5, u5 = atan_bracket(5, 300); l239, u239 = atan_bracket(239, 90)
PI_LO = 16 * l5 - 4 * u239; PI_HI = 16 * u5 - 4 * l239
assert PI_LO < PI_HI and PI_HI - PI_LO < Fr(1, 2 ** 1300)

ctx.prec = 1200
PI = arb.pi()
assert PI.lower() <= arb(PI_HI.numerator) / PI_HI.denominator  # consistency of the two pi's
assert (arb(PI_LO.numerator) / PI_LO.denominator) <= PI.upper()

def floor_exact(lo, hi):
    a = lo.numerator // lo.denominator; b = hi.numerator // hi.denominator
    assert a == b, "rational enclosure straddles an integer"
    return a

def floor_arb(x):
    f = x.floor(); k = f.unique_fmpz()
    assert k is not None, "arb ball straddles an integer"
    assert (x - int(k)).lower() > 0 and (x - int(k) - 1).upper() < 0
    return int(k)

def kappa_scaled(r, bits):
    # kappa_r 2^bits = D^(r-1) 2^(bits - r) / pi^(r-1): decreasing in pi
    num = Fr(D ** (r - 1) * 2 ** (bits - r))
    lo = num / PI_HI ** (r - 1); hi = num / PI_LO ** (r - 1)
    ke = floor_exact(lo, hi)
    ka = floor_arb(arb(D) ** (r - 1) * arb(2) ** (bits - r) / PI ** (r - 1))
    assert ke == ka, (r, bits)
    return ke

def w_scaled(V, bits):
    # w(V) 2^bits = (pi (V-1)/D + 1/2) 2^bits: increasing in pi
    lo = (PI_LO * (V - 1) / D + Fr(1, 2)) * 2 ** bits; hi = (PI_HI * (V - 1) / D + Fr(1, 2)) * 2 ** bits
    ke = floor_exact(lo, hi)
    ka = floor_arb((PI * (V - 1) / D + arb(1) / 2) * arb(2) ** bits)
    assert ke == ka
    return ke

def limbs(n, k=6):
    assert 0 <= n < 2 ** (64 * k)
    return " ".join("%016x" % ((n >> (64 * i)) & (2 ** 64 - 1)) for i in range(k))

t = arb(D) / PI
cps = sorted(set(int((arb(10) ** (arb(h) / 2)).floor().unique_fmpz()) for h in range(6, 21)))
# storage cap for g-primes: index n with x_n <= X/p1 (+ margin); X = x_KFIN, p1 = 1 + t/2
X = 1 + (arb(KFIN) - arb(1) / 2) * t
ncap = int(((X / (1 + t / 2) - 1) / t + arb(1) / 2).floor().unique_fmpz()) + 16
with open(OUT, "w") as f:
    f.write("D %d\nF %d\nF2 %d\nR %d\n" % (D, F, F2, R))
    f.write("TDBL %s\n" % float(t.mid()).hex())
    f.write("KFIN %d\nNCAP %d\n" % (KFIN, ncap))
    for r in range(2, R + 1):
        k1 = kappa_scaled(r, F); k2 = kappa_scaled(r, F2)
        assert k1 < 2 ** 127
        f.write("K %d %d %s\n" % (r, k1, limbs(k2)))
    for V in cps:
        f.write("CP %d %d %s\n" % (V, w_scaled(V, F), limbs(w_scaled(V, F2))))
print("pi: Machin rational enclosure of width < 2^-1300, contains arb's pi; all %d constants and %d checkpoint"
      " enclosures certified by both methods; NCAP %d; t = %s; written %s" % (2 * (R - 1), len(cps), ncap, t.str(20), OUT))
