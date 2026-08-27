#!/usr/bin/env python3
"""
C3 milestone M0, numerics item N1 — the Epstein witness for Lemma B.

For the class-number-2 discriminant D = -20, principal form Q1 = x^2 + 5y^2
(the non-principal class is Q2 = 2x^2 + 2xy + 3y^2), compute the von Mangoldt
coefficients Lambda_Q(n) of the Epstein zeta function

    zeta_Q(s) = sum_{(x,y) != (0,0)} Q(x,y)^{-s} = sum_n r_Q(n) n^{-s},

i.e. the coefficients of -zeta_Q'/zeta_Q(s) = sum_n Lambda_Q(n) n^{-s}, EXACTLY
(each Lambda_Q(n) is a rational combination of log p over primes p), and exhibit

    (i)  support off prime powers: Lambda_Q(n) != 0 for some n that is not p^k,
    (ii) negativity: Lambda_Q(n) < 0 for some n,

each rendered to 40 digits (target >= 30 per the C3 brief).

Normalization: r_Q(1) = 2 (units +-1), so the log-derivative is taken of
F(s) = zeta_Q(s)/2 = sum b_n n^{-s} with b_n = r_Q(n)/2 (half-integers), b_1 = 1.
A multiplicative constant does not change the log-derivative, so Lambda_Q is
independent of this normalization.

Cross-checks (standing order 5):
  1. Genus identity: for n >= 1,  (r_Q1(n) + r_Q2(n))/2 = sum_{d | n} chi_{-20}(d),
     chi_{-20} the Kronecker symbol (-20/.) — verified exactly for all n <= NMAX.
  2. Contrast object: Lambda_K(n) for zeta_K = zeta * L(chi_{-20}) (the full
     class-group average, WITH Euler product) is (1 + chi(p^k-part)) * Lambda(n):
     prime-power supported and >= 0 — verified over the same range. The witness
     is therefore a CLASS-ORBIT-BREAKING effect, exactly as Lemma B predicts.
  3. Numeric evaluation of the exact log-combinations at mp.dps = 50, reported
     to 40 digits.
"""

import json, math
from fractions import Fraction
from mpmath import mp, mpf, log as mplog, nstr

mp.dps = 50
NMAX = 200

# ---------- representation numbers by brute force ----------
def repr_counts(a, b, c, nmax):
    """r(n) = #{(x,y) in Z^2 : a x^2 + b x y + c y^2 = n}, 1 <= n <= nmax."""
    r = [0] * (nmax + 1)
    X = int(math.isqrt(4 * a * c * nmax)) + 2  # crude but safe bounds
    Y = X
    for x in range(-X, X + 1):
        for y in range(-Y, Y + 1):
            v = a * x * x + b * x * y + c * y * y
            if 1 <= v <= nmax:
                r[v] += 1
    return r

rQ1 = repr_counts(1, 0, 5, NMAX)   # x^2 + 5y^2
rQ2 = repr_counts(2, 2, 3, NMAX)   # 2x^2 + 2xy + 3y^2

# ---------- Kronecker symbol chi_{-20} and the genus cross-check ----------
def kronecker(a, n):
    """Kronecker symbol (a/n) for n >= 1."""
    if n == 0:
        return 1 if abs(a) == 1 else 0
    result = 1
    a %= n if n % 2 else a  # no-op guard; full algorithm below
    # standard algorithm
    a0, n0 = a, n
    if n0 < 0:
        raise ValueError
    # factor out 2s from n
    r = 1
    while n0 % 2 == 0:
        n0 //= 2
        if a0 % 2 == 0:
            return 0
        if a0 % 8 in (3, 5):
            r = -r
    a0 %= n0
    while a0 != 0:
        while a0 % 2 == 0:
            a0 //= 2
            if n0 % 8 in (3, 5):
                r = -r
        a0, n0 = n0, a0
        if a0 % 4 == 3 and n0 % 4 == 3:
            r = -r
        a0 %= n0
    return r if n0 == 1 else 0

def chi_m20(n):
    return kronecker(-20, n)

genus_ok = True
for n in range(1, NMAX + 1):
    lhs = Fraction(rQ1[n] + rQ2[n], 2)
    rhs = sum(chi_m20(d) for d in range(1, n + 1) if n % d == 0)
    if lhs != rhs:
        genus_ok = False
        print(f"GENUS CHECK FAIL at n={n}: {lhs} != {rhs}")
assert genus_ok, "genus identity failed"

# ---------- exact Lambda via the log-derivative recursion ----------
# b_n = r(n)/2; represent Lambda(n) as dict {p: Fraction} meaning sum c_p log p.
def factor_logs(n):
    """log n as {p: multiplicity} over primes."""
    out = {}
    m = n
    p = 2
    while p * p <= m:
        while m % p == 0:
            out[p] = out.get(p, 0) + 1
            m //= p
        p += 1
    if m > 1:
        out[m] = out.get(m, 0) + 1
    return out

def lam_exact(r, nmax):
    b = [None] + [Fraction(r[n], 2) for n in range(1, nmax + 1)]
    assert b[1] == 1
    lam = [dict() for _ in range(nmax + 1)]  # lam[n]: {p: Fraction}
    for n in range(2, nmax + 1):
        acc = {}
        if b[n] != 0:
            for p, k in factor_logs(n).items():
                acc[p] = acc.get(p, Fraction(0)) + b[n] * k
        # subtract sum_{d*e = n, 1 < d < n} lam[d] * b[e]
        for d in range(2, n):
            if n % d == 0:
                e = n // d
                if b[e] != 0 and lam[d]:
                    for p, c in lam[d].items():
                        acc[p] = acc.get(p, Fraction(0)) - c * b[e]
        lam[n] = {p: c for p, c in acc.items() if c != 0}
    return lam

lamQ1 = lam_exact(rQ1, NMAX)

def lam_value(d):
    """numeric value at 50 dps from exact {p: Fraction}."""
    v = mpf(0)
    for p, c in d.items():
        v += mpf(c.numerator) / mpf(c.denominator) * mplog(p)
    return v

def lam_str(d):
    if not d:
        return "0"
    return " + ".join(f"({c})*log({p})" for p, c in sorted(d.items()))

def is_prime_power(n):
    f = factor_logs(n)
    return len(f) == 1

# ---------- contrast object: Lambda for zeta_K = zeta * L(chi_{-20}) ----------
# coefficients of zeta_K: a_K(n) = sum_{d|n} chi(d); Euler product holds.
aK = [0] * (NMAX + 1)
for n in range(1, NMAX + 1):
    aK[n] = sum(chi_m20(d) for d in range(1, n + 1) if n % d == 0)
lamK = lam_exact([0] + [2 * aK[n] for n in range(1, NMAX + 1)], NMAX)  # *2 then /2 = same
contrast_ok = True
for n in range(2, NMAX + 1):
    d = lamK[n]
    if d:
        if not is_prime_power(n):
            contrast_ok = False
            print(f"CONTRAST FAIL: Lambda_K({n}) != 0 off prime powers: {lam_str(d)}")
        v = lam_value(d)
        if v < -mpf(10) ** (-40):
            contrast_ok = False
            print(f"CONTRAST FAIL: Lambda_K({n}) < 0: {nstr(v, 40)}")
assert contrast_ok, "contrast object failed — recursion or chi wrong"

# ---------- the witnesses ----------
off_pp = [(n, lamQ1[n]) for n in range(2, 101)
          if lamQ1[n] and not is_prime_power(n)]
negs = [(n, lamQ1[n]) for n in range(2, 101)
        if lamQ1[n] and lam_value(lamQ1[n]) < 0]

print(f"genus identity check (n <= {NMAX}): PASS")
print(f"contrast object Lambda_K prime-power-supported & >= 0 (n <= {NMAX}): PASS")
print(f"\nLambda_Q1 support off prime powers, n <= 100: {[n for n, _ in off_pp]}")
print(f"Lambda_Q1 negative values, n <= 100: {[n for n, _ in negs]}")

w1_n, w1 = off_pp[0]
# headline negativity witness: smallest n with negative value
w2_n, w2 = negs[0]

print(f"\nWITNESS (i): Lambda_Q({w1_n}) = {lam_str(w1)} = {nstr(lam_value(w1), 40)}")
print(f"WITNESS (ii): Lambda_Q({w2_n}) = {lam_str(w2)} = {nstr(lam_value(w2), 40)}")

out = {
    "deliverable": "C3 M0 / N1 — Epstein witness for Lemma B (second one-line witness)",
    "date": "2026-08-26",
    "form": {"Q": "x^2 + 5y^2", "discriminant": -20, "class_number": 2,
             "non_principal_class": "2x^2 + 2xy + 3y^2", "units_w": 2},
    "normalization": "F(s) = zeta_Q(s)/2, b_n = r_Q(n)/2, b_1 = 1; Lambda_Q from -F'/F (independent of the constant)",
    "checks": {
        "genus_identity_exact_to_n": NMAX,
        "contrast_zetaK_prime_power_supported_nonnegative_to_n": NMAX,
    },
    "support_off_prime_powers_n_le_100": [n for n, _ in off_pp],
    "negative_n_le_100": [n for n, _ in negs],
    "witness_i": {
        "n": w1_n, "exact": lam_str(w1),
        "value_40_digits": nstr(lam_value(w1), 40),
        "reading": "support off prime powers — the composition-law/primitivity axiom (Lemma B step 2 conclusion) fails for Epstein h=2",
    },
    "witness_ii": {
        "n": w2_n, "exact": lam_str(w2),
        "value_40_digits": nstr(lam_value(w2), 40),
        "reading": "Lambda_Q < 0 — the effectivity/nef-positivity conclusion (Lemma B step 3) fails for Epstein h=2",
    },
    "all_nonzero_lambda_n_le_100": {
        str(n): {"exact": lam_str(lamQ1[n]), "value": nstr(lam_value(lamQ1[n]), 40)}
        for n in range(2, 101) if lamQ1[n]
    },
    "precision": "exact rational log-combinations; numeric rendering mp.dps=50, printed to 40 digits",
}
with open(__file__.replace("n1_epstein_witness.py", "n1_epstein_witness.json"), "w") as f:
    json.dump(out, f, indent=1)
print("\nJSON written.")
