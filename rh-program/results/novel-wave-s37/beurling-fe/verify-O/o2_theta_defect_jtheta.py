#!/usr/bin/env python3
"""o2 -- OPUS READER, seed M1a beurling-fe.  Theta-relation defect of the v2 near-solutions by an INDEPENDENT route.

Writer's route (verify/v2b): brute sum of exp(-pi n^2 x) over generalized integers <= 80, 60 digits, x = 2^-3..2^3.
Reader's route: psi_P(x) = sum_e E(e) psi_Z(e^2 x), psi_Z(y) = (jtheta3(0, e^{-pi y}) - 1)/2 (mpmath Jacobi theta),
E = the signed Euler-factor measure of o1; x = 2^-6..2^6 (wider range).  Defect (Prop. R (B)):
  D_rho(x) = rho + 2 psi_P(1/x) - sqrt(x) (rho + 2 psi_P(x)),  for rho = rho_true (the residue, which (B) requires) and rho = 1.
Also the Mellin-side failure of the FE: xi_P(s)/xi(s) = E(s), so the FE holds iff E(s) = E(1-s); print |E(s) - E(1-s)|.
"""
import mpmath as mp
mp.mp.dps = 40

def E_atoms(free, removed, emax):
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

def psiZ(y):
    return (mp.jtheta(3, 0, mp.exp(-mp.pi * y)) - 1) / 2

def Efun(s, free, removed):
    v = mp.mpf(1)
    for p in removed: v *= (1 - mp.mpf(p) ** (-s))
    for p in free: v /= (1 - mp.mpf(p) ** (-s))
    return v

near = {
    "K=3": [8.470247], "K=4": [5.391211, 9.447272], "K=5": [6.044415, 8.385313, 10.877985],
    "K=6": [4.947145, 9.162317, 9.753555, 10.894816], "K=7": [5.560587, 7.580187, 9.110379, 10.341306, 10.5167],
    "Z (control)": [],
}
XS = [mp.mpf(2) ** k for k in range(-6, 7) if k != 0]
for name, fr in near.items():
    rem = [5, 7, 11] if fr else []          # 2, 3 cancel exactly (they are both removed and re-added)
    rho = mp.mpf(1)
    for p in rem: rho *= (1 - mp.mpf(1) / p)
    for p in fr: rho /= (1 - mp.mpf(1) / p)
    at = E_atoms(fr, rem, 200)
    psiP = lambda x: mp.fsum(w * psiZ(e * e * x) for e, w in at.items())
    PS = {x: psiP(x) for x in XS}
    def D(r, x): return r + 2 * PS[1 / x] - mp.sqrt(x) * (r + 2 * PS[x])
    dT = max(abs(D(rho, x)) for x in XS); d1 = max(abs(D(mp.mpf(1), x)) for x in XS)
    d1_narrow = max(abs(D(mp.mpf(1), x)) for x in XS if mp.mpf(1) / 8 <= x <= 8)
    s = mp.mpc(0.3, 7)
    gap = abs(Efun(s, fr, rem) - Efun(1 - s, fr, rem)) if fr else abs(Efun(s, [], []) - Efun(1 - s, [], []))
    print(f"{name}: rho_true = {mp.nstr(rho, 8)}   max|D| over x=2^-6..2^6: rho=rho_true {mp.nstr(dT, 4)}, rho=1 {mp.nstr(d1, 4)}"
          f"  (rho=1 on 2^-3..2^3: {mp.nstr(d1_narrow, 4)})   |E(s)-E(1-s)| at s=0.3+7i: {mp.nstr(gap, 4)}")
