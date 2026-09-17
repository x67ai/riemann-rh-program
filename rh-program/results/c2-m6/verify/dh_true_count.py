#!/usr/bin/env python3
"""dh_true_count.py -- M6 rung 1 fix pass (2026-09-17, after check-O.md §2 FIX-FIRST 2a): the EXACT count of n <= X = floor(e^L)
with Lambda_DH(n) != 0, at L = 10, by an exact-arithmetic recursion, plus the structural criterion that makes the count at
L = 20 computable by a sieve (verify/dh_count_L20.rs).

Exact arithmetic.  a(n) = (0, 1, kappa, -kappa, -1) by n mod 5 lies in Z[kappa], kappa = (sqrt(10 - 2 sqrt 5) - 2)/(sqrt 5 - 1),
whose minimal polynomial is kappa^4 + 2 kappa^3 - 6 kappa^2 - 2 kappa + 1 = 0 (found by mpmath.findpoly at 60 digits and
verified below at 80 digits).  Lambda_DH(n) = a(n) log n - sum_{d|n, 1<d<n} a(n/d) Lambda_DH(d) is therefore an element of the
free Z[kappa]-module on the symbols {log p}: Lambda_DH(n) = sum_{p | n} c_p(n) log p with c_p(n) in Z[kappa], and the recursion is
run on these coefficient vectors with integer arithmetic (tuples of four integers per prime, reduced modulo the minimal
polynomial).  Lambda_DH(n) = 0 as a real number if every c_p(n) = 0 (trivially); if some c_p(n) != 0 the real value is evaluated
at 50 digits and its size printed -- the smallest nonzero |Lambda_DH(n)| found is many orders above any evaluation error, so no
appeal to the linear independence of {log p} over the algebraic numbers is needed for the count.

Structural criterion (proved in the note, §1 of the fix pass).  Write chi for the character mod 5 with chi(2) = i; then
a(n) = Re chi(n) + kappa Im chi(n).  For n coprime to 5 write n = n1 n2 with n1 composed of the primes p == +-1 (mod 5) and n2
of the primes p == +-2 (mod 5); chi(n1) = +-1 is real, so a(n) = chi(n1) a(n2) and f_DH(s) = L1(s) F2(s) with the Euler product
L1(s) = prod_{p == +-1} (1 - chi(p) p^{-s})^{-1} and F2(s) = sum_{n2} a(n2) n2^{-s}.  Hence -f'/f = -L1'/L1 - F2'/F2, and
Lambda_DH(n) = chi(p)^k log p for n = p^k with p == +-1 (mod 5), Lambda_DH(n) = Lambda_{F2}(n) for n in T := {n : every prime
factor of n is == +-2 (mod 5)}, and Lambda_DH(n) = 0 for every other n (5 | n, or n has a prime factor == +-1 (mod 5) and is not a
power of it).  S := {p^k : p == +-1 (mod 5)} u T.  This script checks the criterion against the exact recursion at L = 10 and
tests whether Lambda_{F2}(n) vanishes anywhere on T (it does not, at L = 10).

Also printed: the plain f64 recursion (the Rust program's arithmetic, replicated) with its `!= 0.0` count, the f64 values at the
exact zeros (the roundoff floor) and at the exact nonzeros (the margin)."""
import math, json, os, sys, time, datetime
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
t0 = time.time()
L = 10; X = int(math.floor(math.exp(L)))
print(f"[{now()}] dh_true_count.py: L = {L}, X = {X}")

# ---------------------------------------------------------------- Z[kappa]
mp.mp.dps = 80
s5 = mp.sqrt(5); KAP = (mp.sqrt(10 - 2*s5) - 2)/(s5 - 1)
minpoly_val = KAP**4 + 2*KAP**3 - 6*KAP**2 - 2*KAP + 1
print(f"    kappa = {mp.nstr(KAP, 30)};  kappa^4 + 2kappa^3 - 6kappa^2 - 2kappa + 1 = {mp.nstr(minpoly_val, 3)} (80 digits)")
assert abs(minpoly_val) < mp.mpf(10)**-70
Z4 = (0, 0, 0, 0)
def kmul(u, v):
    r = [0]*7
    for i in range(4):
        ui = u[i]
        if ui == 0: continue
        for j in range(4):
            r[i + j] += ui*v[j]
    for deg in (6, 5, 4):            # kappa^4 = -2 kappa^3 + 6 kappa^2 + 2 kappa - 1
        c = r[deg]
        if c:
            r[deg] = 0
            r[deg - 1] += -2*c; r[deg - 2] += 6*c; r[deg - 3] += 2*c; r[deg - 4] += -c
    return tuple(r[:4])
def kval(u):  # numeric value at 50 digits
    return u[0] + u[1]*KAP + u[2]*KAP**2 + u[3]*KAP**3
A = {1: (1, 0, 0, 0), 2: (0, 1, 0, 0), 3: (0, -1, 0, 0), 4: (-1, 0, 0, 0)}   # a(n) by n mod 5; a = 0 at 0

# ---------------------------------------------------------------- factorization (smallest prime factor sieve)
spf = list(range(X + 1))
for i in range(2, int(math.isqrt(X)) + 1):
    if spf[i] == i:
        for j in range(i*i, X + 1, i):
            if spf[j] == j: spf[j] = i
def factor(n):
    f = {}
    while n > 1:
        p = spf[n]; f[p] = f.get(p, 0) + 1; n //= p
    return f

# ---------------------------------------------------------------- the exact recursion
lam = [None]*(X + 1)
for n in range(2, X + 1):
    r = n % 5
    if r == 0: lam[n] = {}; continue
    av = A[r]
    lam[n] = {p: tuple(c*v for c in av) for p, v in factor(n).items()}
for d in range(2, X + 1):
    ld = lam[d]
    if not ld: continue
    j = 2; m = 2*d
    while m <= X:
        aj = j % 5
        if aj:
            av = A[aj]; target = lam[m]
            for p, c in ld.items():
                prod = kmul(av, c)
                old = target.get(p, Z4)
                new = (old[0] - prod[0], old[1] - prod[1], old[2] - prod[2], old[3] - prod[3])
                if new == Z4: target.pop(p, None)
                else: target[p] = new
        j += 1; m += d
print(f"[{now()}] exact recursion done in {time.time()-t0:.1f}s")

# witnesses against the closed forms of m0-axiom-note.md §6.1 (as elements of the module)
def show(n): return " + ".join(f"({c}) log {p}" for p, c in sorted(lam[n].items())) or "0"
print("    witnesses (coefficient vectors (c0, c1, c2, c3) meaning c0 + c1 kappa + c2 kappa^2 + c3 kappa^3):")
for n in (2, 3, 4, 6, 12):
    print(f"      Lambda_DH({n}) = {show(n)}")
# closed forms: 2: kappa log 2; 3: -kappa log 3; 4: -(2 + kappa^2) log 2; 6: (1 + kappa^2)(log 2 + log 3); 12: -kappa(1+kappa^2)(2 log 2 + log 3)
assert lam[2] == {2: (0, 1, 0, 0)} and lam[3] == {3: (0, -1, 0, 0)} and lam[4] == {2: (-2, 0, -1, 0)}
assert lam[6] == {2: (1, 0, 1, 0), 3: (1, 0, 1, 0)}
k1k2 = kmul((0, 1, 0, 0), (1, 0, 1, 0))   # kappa (1 + kappa^2)
assert lam[12] == {2: tuple(-2*c for c in k1k2), 3: tuple(-c for c in k1k2)}
print("    the five closed forms of m0-axiom-note.md §6.1 hold EXACTLY in Z[kappa]")

# ---------------------------------------------------------------- counts
nonzero = [n for n in range(2, X + 1) if lam[n]]
zero_coprime = [n for n in range(2, X + 1) if n % 5 and not lam[n]]
mult5 = [n for n in range(5, X + 1, 5)]
assert all(not lam[n] for n in mult5)
print(f"[{now()}] EXACT: #{{n in [2, {X}] : Lambda_DH(n) != 0}} = {len(nonzero)};  zeros coprime to 5: {len(zero_coprime)};  multiples of 5 (all zero): {len(mult5)};  total {len(nonzero)+len(zero_coprime)+len(mult5)} = {X-1}")
print(f"    first 40 zeros coprime to 5: {zero_coprime[:40]}")

# structural sets
def in_T(n): return n % 5 != 0 and all(p % 5 in (2, 3) for p in factor(n))
def is_pp1(n):
    f = factor(n); return len(f) == 1 and next(iter(f)) % 5 in (1, 4)
S_pp1 = [n for n in range(2, X + 1) if is_pp1(n)]
T_set = [n for n in range(2, X + 1) if in_T(n)]
S = set(S_pp1) | set(T_set)
nz = set(nonzero)
print(f"    structural: #{{p^k <= X, p == +-1 (5)}} = {len(S_pp1)};  #T = #{{n <= X: all prime factors == +-2 (5)}} = {len(T_set)};  |S| = {len(S)}")
print(f"    exact nonzero set == S ?  {nz == S}   (nonzero not in S: {sorted(nz - S)[:10]};  S with Lambda = 0: {sorted(S - nz)[:10]})")
# prime powers of +-1 primes: Lambda = chi(p)^k log p
ok_pp = True
for n in S_pp1:
    p, k = next(iter(factor(n).items()))
    chi = 1 if p % 5 == 1 else -1
    if lam[n] != {p: (chi**k, 0, 0, 0)}: ok_pp = False; print("      MISMATCH at", n, show(n))
print(f"    Lambda_DH(p^k) = chi(p)^k log p for every p == +-1 (5), p^k <= X:  {ok_pp}")

# numeric sizes
mp.mp.dps = 50
vals = {n: mp.fsum(kval(c)*mp.log(p) for p, c in lam[n].items()) for n in nonzero}
nmin = min(nonzero, key=lambda n: abs(vals[n])); nmax = max(nonzero, key=lambda n: abs(vals[n]))
print(f"    smallest nonzero |Lambda_DH(n)| at L = 10: {mp.nstr(abs(vals[nmin]), 6)} at n = {nmin} ({show(nmin)});  largest: {mp.nstr(abs(vals[nmax]), 6)} at n = {nmax}")

# ---------------------------------------------------------------- the f64 recursion (the Rust program's arithmetic, replicated)
kf = (math.sqrt(10 - 2*math.sqrt(5)) - 2)/(math.sqrt(5) - 1)
af = [0.0, 1.0, kf, -kf, -1.0]
lf = [0.0]*(X + 1)
for m in range(2, X + 1): lf[m] = af[m % 5]*math.log(m)
for d in range(2, X + 1):
    ld = lf[d]
    if ld == 0.0: continue
    j = 2; m = 2*d
    while m <= X:
        aj = af[j % 5]
        if aj != 0.0: lf[m] -= aj*ld
        j += 1; m += d
f64_nonzero = sum(1 for n in range(2, X + 1) if lf[n] != 0.0)
floor_max = max(abs(lf[n]) for n in zero_coprime); floor_arg = max(zero_coprime, key=lambda n: abs(lf[n]))
margin_min = min(abs(lf[n]) for n in nonzero); margin_arg = min(nonzero, key=lambda n: abs(lf[n]))
worst_err = max(abs(lf[n] - float(vals[n])) for n in nonzero)
print(f"[{now()}] f64 recursion: `!= 0.0` count = {f64_nonzero} (the note's Rust: 15 346; mpmath dps 30 `!= 0`: 15 442);  "
      f"roundoff floor at the {len(zero_coprime)} exact zeros: max |lambda_f64| = {floor_max:.3e} at n = {floor_arg};  "
      f"margin at the {len(nonzero)} exact nonzeros: min |lambda_f64| = {margin_min:.6e} at n = {margin_arg};  worst |f64 - exact| over the nonzeros = {worst_err:.3e}")
print(f"    the floor/margin ratio at L = 10 is {floor_max/margin_min:.2e}; a threshold anywhere in ({floor_max:.1e}, {margin_min:.1e}) separates the two sets exactly")
json.dump(dict(date=now(), L=L, X=X, minpoly="kappa^4 + 2kappa^3 - 6kappa^2 - 2kappa + 1", exact_nonzero=len(nonzero), zeros_coprime_to_5=len(zero_coprime),
               multiples_of_5=len(mult5), first_zeros_coprime=zero_coprime[:40], n_pp_pm1=len(S_pp1), n_T=len(T_set), S_size=len(S), nonzero_set_equals_S=(nz == S),
               pp_closed_form_ok=ok_pp, min_nonzero_abs=mp.nstr(abs(vals[nmin]), 10), argmin=nmin, max_abs=mp.nstr(abs(vals[nmax]), 10), argmax=nmax,
               f64_nonzero_count=f64_nonzero, f64_floor_max=floor_max, f64_floor_argmax=floor_arg, f64_margin_min=margin_min, f64_margin_argmin=margin_arg,
               f64_worst_abs_err=worst_err, seconds=time.time()-t0), open('out/dh_true_count.json', 'w'), indent=1)
print(f"[{now()}] wrote out/dh_true_count.json ({time.time()-t0:.1f}s)")
