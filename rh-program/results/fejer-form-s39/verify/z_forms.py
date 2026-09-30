"""Unit fejer-form-s39, Z side.  Z1: the positions-side Fejer identity (M1a Theorem C, (C_Q)) on RH-false controls.
Z2: the product/log transport of Theorem F(e) to Z: E_F(1/2 + x) >= E_F(1/2) on the real axis (E_F the entire completion).
Controls: F_{2.9,2} = zeta(s)(1 + 2.9*2^-s + 2*4^-s) (Riemann Gamma, conductor Q = 4; off-line zeros Re s = 0.82388);
Davenport-Heilbronn (chi mod 5, chi(2) = i; completed with Gamma((s+1)/2), root number 1); Epstein x^2 + 5y^2."""
import math
import numpy as np
import mpmath as mp
from scipy.special import j1
mp.mp.dps = 30
S = lambda x: (math.sin(math.pi * x) / (math.pi * x))**2
print("== Z1: (C_Q) for F_{a,q} = zeta(s)(1 + a q^-s + q^{1-2s}), conductor Q = q^2 ==")
for a, q in ((2.9, 2), (2.0, 2), (5.0, 5)):
    Q = q * q; rhoQ = math.sqrt(Q) * (1 + a / q + 1 / q)
    lhs = rhoQ * (1 - Q**-0.5)
    exact = (2 / math.sqrt(Q)) * ((Q - 1) / 2 + a * (q - 1) / 2 + 0.0)   # Poisson: sum_{n>=1} S(n lam) = (1/(2 lam)) - 1/2 for 1/lam in Z
    N = 2_000_000; n = np.arange(1, N + 1, dtype=np.float64)
    c = 1 + a * (n % q == 0) + q * (n % Q == 0)
    Sv = (np.sin(np.pi * n / Q) / (np.pi * n / Q))**2
    part = float(np.sum(c * Sv)); tail = (1 + a / q + 1 / q) * Q**2 / (2 * math.pi**2 * N)   # mean of sin^2 is 1/2
    rhs = (2 / math.sqrt(Q)) * (part + tail)
    print("a=%.1f q=%d: LHS rho_Q(1-Q^-1/2) = %.9f ; RHS exact (Poisson) = %.9f ; RHS summed to 2e6 + tail = %.9f ; RH %s"
          % (a, q, lhs, exact, rhs, "FALSE" if a > 2 * math.sqrt(q) and a < q + 1 else "true (factor zeros on the line or on Re s = 0, 1)"))
print("== Z1 in dimension 2: Epstein x^2 + 5y^2; lattice L = Z + Z sqrt5 i, covol sqrt5, gap: shortest vector 1 ==")
R = 1000.0; A = int(R) + 1; B = int(R * math.sqrt(5)) + 1
tot = 0.0
for aa in range(-A, A + 1):          # dual lattice L* = Z (1,0) + Z (0, 1/sqrt5)
    b = np.arange(-B, B + 1); w = np.sqrt(aa * aa + (b / math.sqrt(5))**2); m = (w > 0) & (w <= R)
    ww = w[m]; tot += float(np.sum((j1(math.pi * ww) / (2 * ww))**2))
tail = math.sqrt(5) / (2 * math.pi * R)
print("disk radius 1/2: phi = 1_B*1_B supported in |v| < 1 (the gap); defect sum_{w in L* - 0} |1_B^(w)|^2 = %.6f (+tail %.6f) ; Poisson predicts sqrt5 pi/4 - pi^2/16 = %.6f"
      % (tot + tail, tail, math.sqrt(5) * math.pi / 4 - math.pi**2 / 16))
print("== Z2: E_F(1/2 + x) >= E_F(1/2) on the real axis ==")
def xi(s): return s * (s - 1) * mp.pi**(-s / 2) * mp.gamma(s / 2) * mp.zeta(s) / 2
def E_F29(s): return s * (s - 1) * (4 / mp.pi)**(s / 2) * mp.gamma(s / 2) * mp.zeta(s) * (1 + mp.mpf('2.9') * 2**(-s) + 2 * 4**(-s))
kappa = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
chi = [0, 1, 1j, -1j, -1]            # chi mod 5, chi(2) = i  (2 -> i, 4 -> -1, 3 -> -i)
chib = [0, 1, -1j, 1j, -1]
def Ldir(s, ch): return 5**(-s) * sum(ch[k] * mp.zeta(s, mp.mpf(k) / 5) for k in range(1, 5))
def DH(s): return ((1 - 1j * kappa) / 2) * Ldir(s, chi) + ((1 + 1j * kappa) / 2) * Ldir(s, chib)
def E_DH(s): return (5 / mp.pi)**((s + 1) / 2) * mp.gamma((s + 1) / 2) * DH(s)
def kron(D, n):
    return int(mp.re(mp.mpf(0))) if False else None
def chi_m20(n): return [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1][n % 20]
def chi_m4(n): return [0, 1, 0, -1][n % 4]
def chi_5(n): return [0, 1, -1, -1, 1][n % 5]
def Lmod(s, f, m): return m**(-s) * sum(f(k) * mp.zeta(s, mp.mpf(k) / m) for k in range(1, m + 1) if f(k) != 0)
def Z_ep(s): return mp.zeta(s) * Lmod(s, chi_m20, 20) + Lmod(s, chi_m4, 4) * Lmod(s, chi_5, 5)
def E_ep(s): return s * (s - 1) * (mp.sqrt(20) / (2 * mp.pi))**s * mp.gamma(s) * Z_ep(s)
checks = [("zeta (2 xi)", lambda s: 2 * xi(s)), ("F_{2.9,2}", E_F29), ("DH", E_DH), ("Epstein x^2+5y^2", E_ep)]
s0 = mp.mpc('0.3', '7.1')
for name, E in checks:
    fe = abs(E(s0) - E(1 - s0)) / abs(E(s0))
    vals = [mp.mpf(1) / 2] + [mp.mpf(1) / 2 + (mp.mpf(k) + mp.mpf(1) / 2) / 100 for k in range(0, 150)]   # grid avoids s = 1
    ev = [mp.re(E(v)) for v in vals]; e0 = ev[0]
    mono = all(ev[i + 1] >= ev[i] for i in range(len(ev) - 1)) if e0 > 0 else all(ev[i + 1] <= ev[i] for i in range(len(ev) - 1))
    sgn = 1 if e0 > 0 else -1
    worst = min(sgn * (e - e0) for e in ev)
    print("%-18s FE residual %.1e ; E(1/2) = %s ; min over x in [0, 1.5] of sign*(E(1/2+x) - E(1/2)) = %s ; |E| monotone on [1/2, 2]: %s"
          % (name, float(fe), mp.nstr(e0, 10), mp.nstr(worst, 6), mono))
if True:
    s1 = mp.mpc('0.808517', '85.699348')
    print("DH at its recorded off-line zero 0.808517 + 85.699348 i: |DH| = %s (|DH| at 0.5 + 85.699348 i: %s)"
          % (mp.nstr(abs(DH(s1)), 5), mp.nstr(abs(DH(mp.mpc('0.5', '85.699348'))), 5)))
