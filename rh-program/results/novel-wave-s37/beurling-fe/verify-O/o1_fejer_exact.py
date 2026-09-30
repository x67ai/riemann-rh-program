#!/usr/bin/env python3
"""o1 -- OPUS READER, seed M1a beurling-fe.  INDEPENDENT route to the Fejer identity (F) of Theorem T.

Writer's route (verify/v2b): brute-force sum of sinc^2 over generalized integers <= 20000 (truncated tail).
Reader's route: CLOSED FORM via Poisson + multiplicative structure, no truncation in n.
  S(x) = (sin pi x / pi x)^2,  T(e) := sum_{n>=1} S(n e)  (e > 0).
  Poisson for x -> S(e x) (FT = e^{-1} (1 - |xi|/e)_+):  sum_{n in Z} S(n e) = e^{-1} sum_{|k|<e} (1 - |k|/e),
  so T(e) = ( e^{-1}(1 + 2 sum_{1<=k<e}(1 - k/e)) - 1 ) / 2 ;  T(e) = 0 exactly iff e in N.
A system P = (rational primes) minus {2,3,5,7,11} plus free primes has zeta_P = zeta * E(s), E = prod_{removed}(1-p^-s)
* prod_{free}(1-p^-s)^-1, i.e. dN_P = dN_Z (*) E (multiplicative convolution), so
  S_F(P) := int S dN_P = sum_e E(e) T(e)     (absolutely convergent: T(e) <= 1/(6 e^2)).
Theorem T predicts S_F = 0 for any system with Riemann's FE; S_F(Z) = T(1) = 0 exactly.
"""
import itertools, math
import mpmath as mp
mp.mp.dps = 40

def T(e):
    e = mp.mpf(e)
    K = int(mp.ceil(e)) - 1
    s = 1 + 2 * mp.fsum(1 - k / e for k in range(1, K + 1))
    return (s / e - 1) / 2

def S(x):
    x = mp.mpf(x)
    return (mp.sin(mp.pi * x) / (mp.pi * x)) ** 2

def E_atoms(free, removed, emax):
    """Signed measure E = prod_{removed}(delta_1 - delta_p) * prod_{free} sum_k delta_{p^k}, atoms e <= emax."""
    atoms = {mp.mpf(1): mp.mpf(1)}
    for p in removed:
        new = {}
        for e, w in atoms.items():
            new[e] = new.get(e, 0) + w
            if e * p <= emax: new[e * p] = new.get(e * p, 0) - w
        atoms = new
    for p in free:
        p = mp.mpf(p); new = {}
        for e, w in atoms.items():
            f = e
            while f <= emax:
                new[f] = new.get(f, 0) + w; f *= p
        atoms = new
    return atoms

near = {  # best-per-K near-solutions, as printed in verify/v2_lsq_exotic_search.log (the objects the NOTE discusses)
    "K=3 {2,3,8.470247}": [2, 3, 8.470247],
    "K=4 {2,3,5.391211,9.447272}": [2, 3, 5.391211, 9.447272],
    "K=5 {2,3,6.044415,8.385313,10.877985}": [2, 3, 6.044415, 8.385313, 10.877985],
    "K=6 {2,3,4.947145,9.162317,9.753555,10.894816}": [2, 3, 4.947145, 9.162317, 9.753555, 10.894816],
    "K=7 {2,3,5.560587,7.580187,9.110379,10.341306,10.5167}": [2, 3, 5.560587, 7.580187, 9.110379, 10.341306, 10.5167],
    "Z (control)": [2, 3, 5, 7, 11],
}
removed_all = [2, 3, 5, 7, 11]

print("T(e) sanity: T(1..4) =", [mp.nstr(T(k), 5) for k in range(1, 5)], "; T(1.5) =", mp.nstr(T(1.5), 12),
      " brute sum_{n<=2e5} S(1.5n) =", mp.nstr(mp.fsum(S(1.5 * n) for n in range(1, 200001)), 12))
for name, free in near.items():
    # the free primes 2, 3 cancel against the removed 2, 3 exactly; keep the multiset honest anyway
    rem = list(removed_all); fr = []
    for p in free:
        if p in rem: rem.remove(p)
        else: fr.append(p)
    rho = mp.mpf(1)
    for p in rem: rho *= (1 - mp.mpf(1) / p)
    for p in fr: rho /= (1 - mp.mpf(1) / p)
    out = []
    for emax in (1e6, 1e10):
        at = E_atoms(fr, rem, emax)
        out.append(mp.fsum(w * T(e) for e, w in at.items()))
    print(f"{name}\n   removed {rem} added {fr}   residue rho_true = {mp.nstr(rho, 10)}"
          f"\n   S_F exact (atoms e<=1e6) = {mp.nstr(out[0], 12)}   (e<=1e10) = {mp.nstr(out[1], 12)}"
          f"   Fejer defect 2*S_F = {mp.nstr(2 * out[1], 6)}")
