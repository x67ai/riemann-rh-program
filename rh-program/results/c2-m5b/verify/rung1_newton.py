#!/usr/bin/env python3
"""rung1_newton.py — FORMULATION.md §3 rung 1 (H3). Exact arithmetic (Python ints, Fractions, sympy).
Hyperelliptic curves y^2 = f(x) over F_7, f squarefree of odd degree 2g+1 (one point at infinity):
   g = 1: f = x^3 + x + 1;   g = 2: f = x^5 + 3x + 1 (irreducible mod 7);   g = 3: f = x^7 + x + 1 (f' = 1 mod 7).
   (x^5 + x + 1, the brief's example, is NOT squarefree over F_7: (x - 4)^2 | f; recorded in the note.)
(1) Brute-force point counts N_n = #C(F_{7^n}) for n <= 4 (F_{7^n} = F_7[x]/(irreducible); chi(z) = z^{(q^n-1)/2}).
(2) Newton's identities: from N_1..N_g the power sums s_n = q^n + 1 - N_n pin a_1..a_g of
    P(t) = prod(1 - alpha_i t) = sum a_k t^k; the functional equation a_{2g-k} = q^{g-k} a_k pins the rest.
    Checks: the pinned P predicts N_{g+1}..N_4 (compared with brute force); all |alpha_i| = sqrt q (mpmath).
(3) Below g counts (m < g): the honest class at "bandwidth" m = configurations of 2g points, symmetric under
    alpha -> q/alpha (FE) and conjugation, integer multiplicities, power sums s_1..s_m equal to the curve's;
    points on the circle |alpha| = sqrt q (on-line) or in the strip 1 <= |alpha| <= q (off-line).
    Orbit types: Q(b): 2 points, factor (1 - b t + q t^2)  [on circle iff |b| < 2 sqrt q; real off-circle iff
    2 sqrt q < |b| <= q+1];  F(b, r): 4 points off the circle, (1 - b t + r^2 t^2)(1 - (q b/r^2) t + (q^2/r^2) t^2),
    1 < r < q, r != sqrt q, |b| < 2r;  R+/R-: the real points +-sqrt q, factors (1 -+ sqrt q t).
    For every multiplicity pattern we solve the m coefficient equations exactly (sympy), check the parameter
    ranges, and report the exact minimum of the double fraction N_d/N (distinct points / 2g), on the circle
    and in the strip, against the Toeplitz rank bound rank T_m <= N_d (T_m = [c_{|j-k|}], c_k = s_k q^{-k/2},
    c_0 = 2g) and against the two-moment-type relaxation that keeps only c_k^2 (forgets the SIGNS of s_k).
< 5 minutes on one process.
"""
import itertools, time
from fractions import Fraction
import sympy as sp
t0 = time.time(); q = 7
def irreducible(n):
    if n == 1: return [0, 1]
    for coeffs in itertools.product(range(q), repeat=n):
        f = list(coeffs) + [1]
        if any(sum(c*pow(a, i, q) for i, c in enumerate(f)) % q == 0 for a in range(q)): continue
        if n == 4:
            bad = False
            for b0 in range(q):
                for b1 in range(q):
                    r = f[:]
                    for k in range(n, 1, -1):
                        c = r[k] % q
                        if c: r[k] = 0; r[k-1] = (r[k-1] - c*b1) % q; r[k-2] = (r[k-2] - c*b0) % q
                    if r[0] % q == 0 and r[1] % q == 0: bad = True; break
                if bad: break
            if bad: continue
        return f
def field(n):
    mod = irreducible(n)
    def mul(a, b):
        r = [0]*(2*n - 1)
        for i, xx in enumerate(a):
            if xx:
                for j, y in enumerate(b): r[i+j] = (r[i+j] + xx*y) % q
        for k in range(2*n - 2, n - 1, -1):
            c = r[k]
            if c:
                for i in range(n): r[k - n + i] = (r[k - n + i] - c*mod[i]) % q
        return tuple(r[:n])
    def add(a, b): return tuple((xx + y) % q for xx, y in zip(a, b))
    def pw(a, e):
        res = tuple([1] + [0]*(n-1)); base = a
        while e:
            if e & 1: res = mul(res, base)
            base = mul(base, base); e >>= 1
        return res
    return [tuple(c) for c in itertools.product(range(q), repeat=n)], add, mul, pw
def count_points(fcoeffs, n):
    elems, add, mul, pw = field(n); one = tuple([1] + [0]*(n-1)); zero = tuple([0]*n); e = (q**n - 1)//2; total = 1
    for xx in elems:
        v = zero; xp = one
        for c in fcoeffs:
            if c: v = add(v, tuple((c*t) % q for t in xp))
            xp = mul(xp, xx)
        total += 1 if v == zero else (2 if pw(v, e) == one else 0)
    return total
def newton_P(s, g):
    e = [Fraction(1)]
    for k in range(1, g + 1): e.append(sum((-1)**(i-1) * e[k-i] * s[i-1] for i in range(1, k+1)) / k)
    a = [(-1)**k * e[k] for k in range(g + 1)]
    for k in range(g + 1, 2*g + 1): a.append(Fraction(q)**(k - g) * a[2*g - k])
    return a
def power_sums_from_P(a, nmax):
    deg = len(a) - 1; e = [(-1)**k * a[k] for k in range(deg + 1)]; s = []
    for n in range(1, nmax + 1):
        sn = sum((-1)**(i-1) * e[i] * s[n-i-1] for i in range(1, min(n-1, deg)+1))
        if n <= deg: sn += (-1)**(n-1) * n * e[n]
        s.append(Fraction(sn))
    return s
x, t = sp.symbols('x t'); sq = sp.sqrt(q)
curves = {1: [1, 1, 0, 1], 2: [1, 3, 0, 0, 0, 1], 3: [1, 1, 0, 0, 0, 0, 0, 1]}   # low -> high
for g, f in curves.items():
    poly = sp.Poly(list(reversed(f)), x, modulus=q); sqf = sp.gcd(poly, poly.diff(x)).degree() == 0
    N = [count_points(f, n) for n in range(1, 5)]
    s = [Fraction(q**n + 1 - N[n-1]) for n in range(1, 5)]
    a = newton_P(s[:g], g); s_pred = power_sums_from_P(a, 4); N_pred = [q**n + 1 - int(s_pred[n-1]) for n in range(1, 5)]
    import mpmath as mp
    mp.mp.dps = 40
    Pq = sp.Poly([sp.Rational(v.numerator, v.denominator) for v in reversed(a)], t)
    fl = sp.factor_list(Pq.as_expr(), t)[1]          # irreducible factors over Q with multiplicities
    absalpha = []; marks_info = []
    for fac, mult in fl:
        cf = [mp.mpf(str(c)) for c in sp.Poly(fac, t).all_coeffs()]
        rts = mp.polyroots(cf, maxsteps=500, extraprec=200)
        for r in rts: absalpha += [float(abs(1/r))]*mult
        marks_info.append((str(fac), mult))
    absalpha = sorted(absalpha)
    print(f"  factorization of P over Q (factor, multiplicity): {marks_info}   <- multiplicity > 1 = a DOUBLE Frobenius eigenvalue (an on-line double in the configuration)")
    print(f"\n=== genus {g}: y^2 = {sp.Poly(list(reversed(f)), x).as_expr()} over F_{q} (squarefree: {sqf}) ===")
    print(f"  brute-force counts N_1..N_4 = {N}   (time {time.time()-t0:.1f} s)")
    print(f"  power sums s_1..s_4 = {[int(v) for v in s]}")
    print(f"  Newton + FE from s_1..s_{g}: P(t) = {sp.Poly([sp.Rational(v.numerator, v.denominator) for v in reversed(a)], t).as_expr()}")
    print(f"  predicted N_1..N_4 from the pinned P = {N_pred}  -> match with brute force beyond n = g: {N_pred == N}")
    print(f"  |alpha_i| = {[round(v, 12) for v in absalpha]}  vs sqrt(q) = {q**0.5:.12f}  -> all on the circle: {all(abs(v - q**0.5) < 1e-9 for v in absalpha)}")
    if g < 2: continue
    for m in range(1, g):
        S = s[:m]; a_dat = newton_P(S + [Fraction(0)]*(g-m), g)   # a_1..a_m are the datum
        c = [sp.Integer(2*g)] + [sp.Rational(int(S[k-1])) / sq**k for k in range(1, m+1)]
        Tm = sp.Matrix(m+1, m+1, lambda i, j: c[abs(i-j)]); rank = Tm.rank()
        psd = all(sp.N(ev) >= 0 for ev in Tm.eigenvals().keys())
        print(f"\n  -- below g: m = {m} count(s) given, s_1..s_m = {[int(v) for v in S]} -> a_1..a_m = {[str(a_dat[k]) for k in range(1, m+1)]} --")
        print(f"     Toeplitz T_{m} = {Tm.tolist()}: rank {rank} (=> N_d >= {rank} for any on-circle configuration); PSD: {psd}")
        patterns = []
        for nQ in range(0, g+1):
            for nF in range(0, g//2+1):
                for eQ in itertools.product(range(1, g+1), repeat=nQ):
                    if list(eQ) != sorted(eQ, reverse=True): continue
                    for eF in itertools.product(range(1, g//2+1), repeat=nF):
                        if list(eF) != sorted(eF, reverse=True): continue
                        rest = 2*g - 2*sum(eQ) - 4*sum(eF)
                        if rest < 0: continue
                        for ep in range(0, rest+1): patterns.append((eQ, eF, ep, rest-ep))
        patterns.sort(key=lambda p: 2*len(p[0]) + 4*len(p[1]) + (p[2] > 0) + (p[3] > 0))
        best = {"circle": None, "strip": None}; feas_list = []; infeas = []
        import numpy as np
        Bgrid = np.linspace(-8.0, 8.0, 161); Rgrid = np.linspace(1.05, 6.95, 60)
        for (eQ, eF, ep, em) in patterns:
            Nd = 2*len(eQ) + 4*len(eF) + (ep > 0) + (em > 0)
            if time.time() - t0 > 420: print('     [wall-clock guard: search stopped at', (eQ, eF, ep, em), ']'); break
            if best["circle"] is not None and best["strip"] is not None and Nd > max(best["circle"][0], best["strip"][0]): break
            bs = sp.symbols(f'b0:{len(eQ)}', real=True); bf = sp.symbols(f'c0:{len(eF)}', real=True); rf = sp.symbols(f'r0:{len(eF)}', positive=True)
            P = sp.Integer(1)
            for i, e in enumerate(eQ): P *= (1 - bs[i]*t + q*t**2)**e
            for i, e in enumerate(eF): P *= ((1 - bf[i]*t + rf[i]**2*t**2)*(1 - (q*bf[i]/rf[i]**2)*t + (q**2/rf[i]**2)*t**2))**e
            P *= (1 - sq*t)**ep * (1 + sq*t)**em
            Pp = sp.Poly(sp.expand(P), t)
            eqs = [sp.expand(Pp.coeff_monomial(t**k) - sp.Rational(a_dat[k].numerator, a_dat[k].denominator)) for k in range(1, m+1)]
            unknowns = list(bs) + list(bf) + list(rf)
            if not unknowns:
                sols = [dict()] if all(sp.simplify(e) == 0 for e in eqs) else []
            else:
                try: sols = sp.solve(eqs, unknowns, dict=True)
                except Exception: sols = []
            found_on = found_strip = False
            for sol in sols:
                free = [u for u in unknowns if u not in sol]
                exprs = [sp.sympify(sol.get(u, u)) for u in unknowns]
                fn = sp.lambdify(free, exprs, 'numpy') if free else (lambda: [complex(v) for v in exprs])
                grids = [Rgrid if str(u).startswith('r') else Bgrid for u in free]
                for vals in (itertools.product(*grids) if free else [()]):
                    try: out = fn(*vals)
                    except Exception: continue
                    out = [complex(v) for v in out]
                    if any(abs(v.imag) > 1e-9 for v in out): continue
                    num = {u: v.real for u, v in zip(unknowns, out)}
                    on = all(abs(num[b]) < 2*q**0.5 - 1e-9 for b in bs) and not eF
                    strip = all(abs(num[b]) < 2*q**0.5 - 1e-9 or (2*q**0.5 + 1e-9 < abs(num[b]) <= q + 1 + 1e-9) for b in bs) and \
                            all(1 + 1e-9 < num[r] < q - 1e-9 and abs(num[r] - q**0.5) > 1e-6 and abs(num[b]) < 2*num[r] - 1e-9 for b, r in zip(bf, rf))
                    if on and best["circle"] is None: best["circle"] = (Nd, (eQ, eF, ep, em), {str(k): round(v, 6) for k, v in num.items()})
                    if strip and best["strip"] is None: best["strip"] = (Nd, (eQ, eF, ep, em), {str(k): round(v, 6) for k, v in num.items()})
                    found_on |= on; found_strip |= strip
                    if found_on and found_strip: break
                if found_on and found_strip: break
            if found_on or found_strip: feas_list.append((Nd, (eQ, eF, ep, em), 'circle' if found_on else 'strip'))
            else: infeas.append((Nd, (eQ, eF, ep, em)))
        print(f"     patterns searched in ascending N_d: infeasible = {infeas}")
        print(f"     feasible (N_d, (eQ, eF, e+, e-), where): {feas_list}")
        for w in ("circle", "strip"):
            b = best[w]
            print(f"     exact minimum of N_d {w.upper():6s}: N_d = {b[0] if b else None} of {2*g} -> N_d/N = {sp.Rational(b[0], 2*g) if b else None}; pattern {b[1] if b else None}; parameters {b[2] if b else None}")
        print(f"     Toeplitz rank bound N_d >= {rank}: {'ATTAINED' if best['circle'] and best['circle'][0] == rank else 'NOT attained'} on the circle")
        # two-moment-type relaxation: forget the signs of s_1..s_m; is the 2-point (single Q^g) pattern feasible for some sign choice?
        relax2 = False
        for signs in itertools.product([1, -1], repeat=m):
            S2 = [Fraction(int(v)*sg) for v, sg in zip(S, signs)]; a2d = newton_P(S2 + [Fraction(0)]*(g-m), g)
            b = Fraction(S2[0], g); ok = abs(float(b)) < 2*q**0.5   # (1 - b t + q t^2)^g: a_1 = -g b
            if m >= 2: ok = ok and (Fraction(g*q) + Fraction(g*(g-1), 2)*b*b == a2d[2])
            if ok: relax2 = True
        exact = sp.Rational(best['circle'][0], 2*g) if best['circle'] else None
        print(f"     two-moment-type relaxation (|c_k|^2 only, signs of s_k forgotten): the 2-point pattern Q^{g} feasible for some sign choice: {relax2}"
              f" -> relaxation minimum {'<= 1/'+str(g) if relax2 else '(2-point pattern not unlocked)'}; exact on-circle minimum {exact} -> relaxation {'NOT TIGHT' if relax2 and exact != sp.Rational(1, g) else 'tight'}")
print(f"\ntotal {time.time()-t0:.1f} s")
