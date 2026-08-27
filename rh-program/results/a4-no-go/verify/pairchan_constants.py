"""Constants for the capacity lemma:
  alpha  = sum over the 64 zeros of psi'^2  (exact: (pi/64)^2 * (65^2-1)/3)
  alpha*(y) = sum_k sup_{cell_k, 0<=t<=y} (|psi'|^2 + |psi||psi''|)(x+it)
  peak-cell dip check: min over peak cell of R_y
  nu(y) fine curve and the capacity comparisons
  c0 = min psi^2 on [-1/2,1/2] (stacking constant)
"""
import numpy as np
from pairchan_core import N, abar, psiN, U, JJ

def dpsi(z, k):
    return complex(np.sum(U * (-2j * np.pi * JJ / N) ** k * np.exp(-2j * np.pi * JJ * z / N)))

alpha_exact = (np.pi / 64) ** 2 * (65 ** 2 - 1) / 3.0
print(f"alpha (sum psi'^2 over zeros, exact) = {alpha_exact:.6f}")

Delta = N / 65.0
xs_cell = np.linspace(-0.5 * Delta, 0.5 * Delta, 141)

def alpha_star(y, nt=8):
    ts = np.linspace(0, y, nt)
    tot, peak = 0.0, 0.0
    for k in range(65):
        g = k * Delta
        best = 0.0
        for x in xs_cell:
            for t in ts:
                z = g + x + 1j * t
                v = abs(dpsi(z, 1)) ** 2 + abs(psiN(z)) * abs(dpsi(z, 2))
                best = max(best, v)
        tot += best
        if k == 0:
            peak = best
    return tot, peak

for y in (0.159, 0.2, 0.25, 0.318, 0.4, 0.64):
    tot, peak = alpha_star(y)
    print(f"alpha*({y:5.3f}) = {tot:9.4f}   (peak cell contributes {peak:7.4f}; "
          f"non-peak {tot-peak:8.4f})")

# peak-cell dip: min of R_y over the peak cell
print()
xs = np.linspace(-0.5 * Delta, 0.5 * Delta, 2001)
for y in (0.159, 0.25, 0.318, 0.4, 0.5, 0.64):
    Rmin = min((psiN(x + 1j * y) ** 2).real for x in xs)
    print(f"y={y:5.3f}: min over peak cell of R_y = {Rmin:9.5f} "
          f"({'no dip' if Rmin >= 0 else 'DIP IN PEAK CELL'})")

# c0: min psi^2 within half-cell radius; and psi^2 at 2y separations
print()
print(f"psi(Delta/2)^2 = {abs(psiN(Delta/2))**2:.6f}   (Delta/2 = {Delta/2:.4f})")
for r in (0.2, 0.32, 0.4, 0.5, 0.64):
    print(f"psi({r})^2 = {abs(psiN(r))**2:.6f}")

# fine nu(y) curve and the two comparisons:
#   single-pair need: 8 nu(y) <= 2 abar(2y)^2      (m=1)
#   analytic shallow: nu(y) <= alpha*(y) y^2, need 4 alpha*(y) y^2 <= abar(2y)^2
print()
xs2 = np.linspace(0, N, 16001, endpoint=False)
cell_idx = np.floor((xs2 / Delta) + 0.5).astype(int) % 65
print("   y        nu(y)     8nu       2a2^2     ratio    a*y^2   4a*y^2/a2^2")
for y in (0.05, 0.08, 0.1, 0.13, 0.159, 0.2, 0.25, 0.318, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.85, 1.0, 1.25, 1.5, 1.75, 2.0):
    R = np.array([(psiN(x + 1j * y) ** 2).real for x in xs2])
    nu = sum(max(0.0, float(np.max(-R[cell_idx == k]))) for k in range(65))
    a2 = abar(2 * y)
    ast, _ = alpha_star(min(y, 0.64), nt=5) if y <= 0.64 else (float("nan"), 0)
    r1 = 8 * nu / (2 * a2 ** 2)
    r2 = 4 * ast * y * y / a2 ** 2 if y <= 0.64 else float("nan")
    print(f"   {y:5.3f}  {nu:9.5f} {8*nu:9.4f} {2*a2**2:10.4f}  {r1:7.4f}  "
          f"{ast*y*y if y<=0.64 else float('nan'):8.4f}  {r2:7.4f}")
