"""Certified ledger windows.
S1(d)  = 8 nu(d) / (2 abar(2d)^2)                          single-pair condition
Sgen(d;Y) = [8 nu(d) + 4 sup_{0<d'<=Y}(nu(d+d') + nu(|d-d'|))] / (2 abar(2d)^2)
           multi-pair condition with half-half charge, per-cell perturber cap 2.
Find largest Y with sup_{d<=Y} Sgen(d;Y) <= 1.
Also: Lipschitz data for rigorous grid certification:
  |d nu / dy| <= sum_k sup_cell |d/dy R_y| <= sum_k sup_cell |(psi^2)'(x+iy)| =: L(y)
  (since d/dy Re psi^2(x+iy) = -Im (psi^2)'(x+iy), |...| <= |(psi^2)'|)
  and (psi^2)' = 2 psi psi'.
"""
import numpy as np
from pairchan_core import N, abar, psiN, U, JJ

Delta = N / 65.0
ys = np.round(np.arange(0.01, 1.001, 0.01), 3)
xs = np.linspace(0, N, 12001, endpoint=False)
cell_idx = np.floor((xs / Delta) + 0.5).astype(int) % 65

nu_tab = {}
for y in ys:
    R = np.array([(psiN(x + 1j * y) ** 2).real for x in xs])
    nu_tab[y] = sum(max(0.0, float(np.max(-R[cell_idx == k]))) for k in range(65))

def nu(y):
    # conservative lookup: round UP to nearest tabulated y (nu increasing)
    yy = min([t for t in ys if t >= y - 1e-12], default=ys[-1])
    return nu_tab[yy]

print("single-pair condition S1(d) = 8nu/(2 abar(2d)^2):")
S1max = 0.0
for y in ys:
    s1 = 8 * nu_tab[y] / (2 * abar(2 * y) ** 2)
    S1max = max(S1max, s1)
print(f"  max over d in (0,1]: S1 = {S1max:.4f}  (must be < 1)")

def Sgen(d, Y):
    sup_term = 0.0
    for dp in ys:
        if dp > Y + 1e-12:
            break
        s = nu(d + dp) + nu(abs(d - dp)) if abs(d - dp) > 5e-3 else nu(d + dp)
        sup_term = max(sup_term, s)
    return (8 * nu(d) + 4 * sup_term) / (2 * abar(2 * d) ** 2)

print("\nmulti-pair window search:")
for Y in (0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.155, 0.159, 0.16, 0.17, 0.18, 0.20):
    worst = max(Sgen(d, Y) for d in ys if d <= Y + 1e-12)
    print(f"  Y = {Y:5.3f}: sup_d Sgen = {worst:.4f}  {'OK' if worst <= 1 else 'FAIL'}")

# Lipschitz constant for nu on (0, 1]: L(y) = sum_k sup_cell 2|psi||psi'| at height y
def dpsi1(z):
    return complex(np.sum(U * (-2j * np.pi * JJ / N) * np.exp(-2j * np.pi * JJ * z / N)))
xs_c = np.linspace(-Delta / 2, Delta / 2, 81)
def Lip(y):
    tot = 0.0
    for k in range(65):
        g = k * Delta
        tot += max(2 * abs(psiN(g + x + 1j * y)) * abs(dpsi1(g + x + 1j * y)) for x in xs_c)
    return tot
for y in (0.2, 0.4, 0.6, 0.8, 1.0):
    print(f"Lip nu at y={y}: {Lip(y):9.3f};  nu(y)={nu_tab[min([t for t in ys if t>=y])]:9.4f}; "
          f"2 abar(2y)^2 = {2*abar(2*y)**2:12.3f}")

# margin of S1 on a finer grid near the peak (worst region 0.25-0.5)
print("\nfine S1 near peak:")
for y in np.arange(0.30, 0.451, 0.01):
    R = np.array([(psiN(x + 1j * y) ** 2).real for x in xs])
    nuv = sum(max(0.0, float(np.max(-R[cell_idx == k]))) for k in range(65))
    print(f"  y={y:5.2f}: S1 = {8*nuv/(2*abar(2*y)**2):.4f}")
