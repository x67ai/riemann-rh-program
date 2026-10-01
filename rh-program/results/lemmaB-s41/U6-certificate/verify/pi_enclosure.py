#!/usr/bin/env python3
"""Rigorous rational enclosure of pi (Machin's formula, exact Fractions, alternating-series bounds),
and the derived enclosures used by s8cert.c for t = 1/rho = 16/pi and 32/pi.

Output (stdout and params.txt): for each system
  name  t_double(hex)  rho_double(hex)  D  T_lo  T_hi
with T_lo/2^D <= t <= T_hi/2^D (integers), and a check that t_double = RN(t) (so |t_double - t| <= ulp/2).
Cross-check: the enclosure is compared with python-flint's arb value of pi.
"""
from fractions import Fraction as Fr
import math, sys, os

def arctan_bounds(x, eps):
    """x = 1/q, 0 < x < 1. Returns (lo, hi) with lo <= arctan(x) <= hi, hi - lo <= eps.
    Partial sums of an alternating series with decreasing terms bracket the sum."""
    s = Fr(0); n = 0; last = None
    while True:
        term = x ** (2 * n + 1) / (2 * n + 1)
        s_new = s + term if n % 2 == 0 else s - term
        if n >= 1 and term <= eps:
            lo, hi = (s, s_new) if n % 2 == 0 else (s_new, s)
            assert lo <= hi
            return lo, hi
        s = s_new; n += 1

def pi_bounds(eps=Fr(1, 10**60)):
    l5, h5 = arctan_bounds(Fr(1, 5), eps)
    l239, h239 = arctan_bounds(Fr(1, 239), eps)
    lo = 16 * l5 - 4 * h239
    hi = 16 * h5 - 4 * l239
    return lo, hi

def rn_double(q):
    """Round-to-nearest double of a positive Fraction, exactly (ties impossible here; asserted)."""
    f = float(q)  # Python's Fraction.__float__ is correctly rounded (int/int true division)
    # verify: |f - q| <= ulp(f)/2
    ulp = math.ulp(f)
    assert abs(Fr(f) - q) <= Fr(ulp) / 2
    return f

def main():
    lo, hi = pi_bounds()
    width = hi - lo
    print(f"# pi enclosure (Machin, exact rationals): width = {float(width):.3e}")
    print(f"# pi_lo = {lo.numerator * 10**50 // lo.denominator}e-50 (floor)")
    try:
        import flint
        flint.ctx.prec = 300
        p = flint.arb.pi()
        # agreement check of the leading 58 digits of arb's pi with the Machin lower bound
        s = p.str(60, radius=False)
        print(f"# arb pi (60 digits) = {s}")
        lo60 = lo.numerator * 10**58 // lo.denominator
        assert s.replace('.', '')[:58] == str(lo60)[:58], "arb pi disagrees with Machin enclosure"
        print("# arb cross-check: first 58 digits agree")
    except ImportError:
        print("# python-flint not available; arb cross-check skipped")
    D = 200
    out = []
    for name, num in (("pi16", 16), ("pi32", 32), ("pi64", 64), ("pi128", 128)):
        t_lo_q = Fr(num) / hi
        t_hi_q = Fr(num) / lo
        T_lo = (t_lo_q * 2**D).numerator // (t_lo_q * 2**D).denominator          # floor
        T_hi = -((-(t_hi_q * 2**D).numerator) // (t_hi_q * 2**D).denominator)     # ceil
        assert Fr(T_lo, 2**D) <= t_lo_q and Fr(T_hi, 2**D) >= t_hi_q
        td_lo = rn_double(t_lo_q); td_hi = rn_double(t_hi_q)
        assert td_lo == td_hi, "t not determined to double precision"
        td = td_lo
        # |td - t| <= ulp/2 for every t in [t_lo_q, t_hi_q]: check at both ends with the true ulp bound
        u = Fr(math.ulp(td)) / 2
        assert abs(Fr(td) - t_lo_q) <= u and abs(Fr(td) - t_hi_q) <= u
        rel = max(abs(Fr(td) - t_lo_q), abs(Fr(td) - t_hi_q)) / t_lo_q
        assert rel <= Fr(1, 2**53), "relative error of t_double exceeds u"
        rho_q = lo / num  # any value; rho_double used only for non-rigorous guesses
        rd = float(rho_q)
        out.append(f"{name} {td.hex()} {rd.hex()} {D} {T_lo} {T_hi}")
        print(f"# {name}: t_double = {td!r} ({td.hex()}), |t_double - t|/t <= {float(rel):.3e} <= 2^-53;"
              f" T_hi - T_lo = {T_hi - T_lo}")
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "params.txt")
    with open(path, "w") as fh:
        fh.write("\n".join(out) + "\n")
    for line in out:
        print(line)

if __name__ == "__main__":
    main()
