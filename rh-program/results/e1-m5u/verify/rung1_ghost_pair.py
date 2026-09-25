#!/usr/bin/env python3
"""E1 rung-1 rehearsal (KICKSTART 10(l)): an EXACT integer-atomic ghost pair on the function-field rung.
Two genus-2 curves y^2 = f(x) over F_7 with the SAME first point count N_1 (the same datum s_1 at bandwidth m = 1 < g = 2)
but DIFFERENT L-polynomials P(t): two positive integer-atomic configurations (4 points each on |alpha| = sqrt 7, marks = multiplicities)
whose difference has a 'spectral gap' at the first frequency n = 1 and is nonzero. Exact arithmetic (Python integers).
Normalization: results/c2-m5b/FORMULATION.md section 3.1 (Newton + FE from s_1, s_2)."""
import itertools, time, sys
q = 7
def is_squarefree_mod(f, p):
    # f: coefficient list high->low over Z; check gcd(f, f') = 1 in F_p[x]
    def trim(a):
        while a and a[0] % p == 0: a = a[1:]
        return [c % p for c in a]
    def polymod(a, b):
        a = trim(a); b = trim(b)
        if not b: raise ZeroDivisionError
        inv = pow(b[0], -1, p)
        while a and len(a) >= len(b):
            c = a[0] * inv % p
            for i in range(len(b)): a[i] = (a[i] - c * b[i]) % p
            a = trim(a)
        return a
    def gcd(a, b):
        while trim(b):
            a, b = b, polymod(a, b)
        return trim(a)
    d = len(f) - 1
    fp = [(d - i) * f[i] for i in range(d)]
    g = gcd(f, fp)
    return len(g) == 1
def N1(f):
    # #C(F_7) for y^2 = f(x), f quintic (one point at infinity)
    n = 1
    for x in range(q):
        v = 0
        for c in f: v = (v * x + c) % q
        if v == 0: n += 1
        elif pow(v, (q - 1) // 2, q) == 1: n += 2
    return n
# F_49 = F_7[i], i^2 = -1 (x^2+1 irreducible mod 7 since -1 is a non-residue mod 7)
def N2(f):
    n = 1
    for a in range(q):
        for b in range(q):
            # x = a + b i; evaluate f(x) in F_49
            re, im = 0, 0
            for c in f:
                re, im = (re * a - im * b + c) % q, (re * b + im * a) % q
            if re == 0 and im == 0: n += 1
            else:
                # quadratic residue test in F_49: z^((49-1)/2) == 1
                zr, zi = 1, 0
                e = (q * q - 1) // 2
                br, bi = re, im
                while e:
                    if e & 1: zr, zi = (zr * br - zi * bi) % q, (zr * bi + zi * br) % q
                    br, bi = (br * br - bi * bi) % q, (2 * br * bi) % q
                    e >>= 1
                if zr == 1 and zi == 0: n += 2
    return n
def Ppoly(f):
    s1 = q + 1 - N1(f); s2 = q * q + 1 - N2(f)
    a1 = -s1; a2 = (s1 * s1 - s2) // 2
    return (1, a1, a2, q * a1, q * q)   # P(t) = 1 + a1 t + a2 t^2 + q a1 t^3 + q^2 t^4 (Newton + FE, g = 2)
t0 = time.time()
curves = {}
for coeffs in itertools.product(range(q), repeat=5):
    f = [1] + list(coeffs)   # monic quintic
    if not is_squarefree_mod(f, q): continue
    n1 = N1(f)
    curves.setdefault(n1, {})
    P = Ppoly(f)
    curves[n1].setdefault(P, []).append(f)
print("rung-1 rehearsal: genus-2 curves y^2 = f(x), f monic squarefree quintic over F_7; grouped by N_1 (datum s_1) and by P(t)")
found = None
for n1 in sorted(curves):
    Ps = curves[n1]
    print(f"N_1 = {n1:2d} (s_1 = {q+1-n1:+d}): {len(Ps)} distinct P(t) among {sum(len(v) for v in Ps.values())} curves")
    if len(Ps) >= 2 and found is None: found = n1
n1 = found
Ps = sorted(curves[n1].items())
print()
print(f"EXACT GHOST PAIR at m = 1 (bandwidth one count), N_1 = {n1}, s_1 = {q+1-n1:+d}:")
for P, fs in Ps[:2]:
    f = fs[0]
    print(f"  y^2 = x^5 + {f[1]}x^4 + {f[2]}x^3 + {f[3]}x^2 + {f[4]}x + {f[5]}  :  N_1 = {N1(f)}, N_2 = {N2(f)},  P(t) = 1 + ({P[1]})t + ({P[2]})t^2 + ({P[3]})t^3 + ({P[4]})t^4")
print("Both configurations have 4 points on |alpha| = sqrt(7) (RH, Weil), integer marks, the same s_1 (the datum at m = 1),")
print("different s_2: the difference mu = nu_1 - nu_2 is a nonzero symmetric integer-atomic measure with s_1(mu) = 0 (the gap at n = 1) and s_2(mu) != 0.")
print(f"elapsed {time.time()-t0:.2f} s")
