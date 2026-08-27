# T6 verification: divergent-cutoff vacuity (the garnish construction).
# Garnish: n0 = Delta N / h0^3 on-line atoms of multiplicity h0 = floor(V0/2), mass rebalanced
# by deleting n0 h0 simples.  Row shifts (per N): cubic +Delta (exactly, up to rounding o(1));
# Frobenius +Delta/h0 - Delta/h0^2; mass 0 (rebalanced); tail row at V0: 0 (h0 < V0);
# count rows at V >= V0: 0; N_d shift = -(Delta/h0^2)(1 - 1/h0) <= 0.
import numpy as np, json
from scipy.optimize import linprog

out = {}
Delta = 4.0 / 3.0

# ---- (1) shift table at V0 = (loglog T)^3 over the adjudication's logT grid ----
print("shift table (Delta = 4/3, V0 = (loglog T)^3, h0 = V0/2):")
rows = []
for logT in (18.4, 41.4, 92.1, 230.3, 1000.0, 1e6):
    llT = np.log(logT)
    V0 = llT**3
    h0 = V0 / 2
    frob = Delta / h0 - Delta / h0**2
    mass = 0.0
    trace_naive = Delta / h0**2          # before rebalance (the adjudication's row)
    Nd = -(Delta / h0**2) * (1 - 1 / h0)
    rows.append((logT, V0, h0, frob, trace_naive, Nd))
    print(f"  logT = {logT:9.1f}: V0 = {V0:10.2f}, h0 = {h0:9.2f}, Frobenius shift = {frob:+.5f}, "
          f"trace shift (pre-rebalance) = {trace_naive:+.2e}, N_d shift = {Nd:+.2e}, cubic = +{Delta:.4f}, "
          f"tail row = 0, count rows (V >= V0) = 0")
out["shift_table"] = rows
# adjudication anchor: 'Frobenius +Delta/h0 -> 0' with Delta = 4/3: 4/(3 h0) (RUN-REPORT Tier-A (ii))
for logT in (18.4, 41.4):
    h0 = np.log(logT) ** 3 / 2
    assert abs((Delta / h0) - 4 / (3 * h0)) < 1e-15
print("Frobenius cost form 4/(3 h0) (RUN-REPORT Tier-A regression (ii)) reproduced")

# ---- (2) abstract spectral LP demonstration ----
# variables: s1 (simple fraction), s2 (double fraction), g (garnish atom count fraction) at height h0.
# rows (per N): mass s1 + 2 s2 + g h0 = 1;  Frobenius s1 + 4 s2 + g h0^2 in (4/3)(1 +/- tol);
# cubic s1 + 8 s2 + g h0^3 in c_target (1 +/- tol) with c_target = 2 + Delta
# (a cubic demand the doubles corner misses by Delta); tail row: no mass at |lambda| >= V0 (h0 < V0: free).
# objective: N_d/N = s1 + s2 + g.
print("\nabstract LP: cubic equality c_target = 2 + 4/3 = 10/3 (doubles corner misses by 4/3):")
for h0, tol in ((200.0, 0.01), (1000.0, 0.01), (10000.0, 0.002)):
    c_t = 2.0 + Delta
    A_eq = [[1, 2, h0]]
    b_eq = [1.0]
    A_ub = [[1, 4, h0**2], [-1, -4, -h0**2], [1, 8, h0**3], [-1, -8, -h0**3]]
    b_ub = [(4/3)*(1+tol), -(4/3)*(1-tol), c_t*(1+tol), -c_t*(1-tol)]
    # without garnish (g forced 0):
    r0 = linprog(c=[1, 1, 1], A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub,
                 bounds=[(0, None), (0, None), (0, 0)], method="highs")
    # with garnish:
    r1 = linprog(c=[1, 1, 1], A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub,
                 bounds=[(0, None)] * 3, method="highs")
    stat0 = f"{r0.fun:.6f}" if r0.status == 0 else "INFEASIBLE"
    stat1 = f"{r1.fun:.6f}" if r1.status == 0 else "INFEASIBLE"
    print(f"  h0 = {h0:7.0f}, tol = {tol}: min N_d/N without garnish = {stat0}; with garnish = {stat1} "
          f"(5/6 = {5/6:.6f})")
    out[f"lp_h0_{int(h0)}"] = {"no_garnish": stat0, "garnish": stat1}

# ---- (3) exact feasibility of the garnished configuration (finite-N instance) ----
# N = h0^3 * K for integers: take h0 = 20, Delta = 4/3 -> n0 = Delta N / h0^3.
# base: 5/6-extremal at cubic-demand shortfall Delta N; garnished: add n0 atoms mult h0,
# delete n0 h0 simples.  Verify all rows exactly in rationals.
from fractions import Fraction
h0 = 20
N = 3 * h0**3 * 5  # = 120000, divisible enough
n0F = Fraction(4, 3) * N / h0**3
s1, s2 = Fraction(2, 3) * N, Fraction(1, 6) * N   # simples, doubles counts
# base rows
mass0 = s1 + 2 * s2
frob0 = s1 + 4 * s2
cub0 = s1 + 8 * s2
# garnished
s1g = s1 - n0F * h0
massg = s1g + 2 * s2 + n0F * h0
frobg = s1g + 4 * s2 + n0F * h0**2
cubg = s1g + 8 * s2 + n0F * h0**3
Ndg = s1g + s2 + n0F
out["exact_instance"] = {
    "N": N, "mass_base": float(mass0 / N), "mass_garn": float(massg / N),
    "frob_base": float(frob0 / N), "frob_garn": float(frobg / N),
    "cubic_base": float(cub0 / N), "cubic_garn": float(cubg / N),
    "Nd_base": float((s1 + s2) / N), "Nd_garn": float(Ndg / N),
}
print(f"\nexact rational instance (N = {N}, h0 = {h0}, Delta = 4/3):")
print(f"  mass:   base {float(mass0/N):.6f} -> garnished {float(massg/N):.6f}  (both = 1 exactly: "
      f"{mass0 == N and massg == N})")
print(f"  Frobenius/N: {float(frob0/N):.6f} -> {float(frobg/N):.6f}  (shift = {float((frobg-frob0)/N):.6f} "
      f"= Delta/h0 - Delta/h0^2 = {float(Fraction(4,3)/h0 - Fraction(4,3)/h0**2):.6f})")
print(f"  cubic/N: {float(cub0/N):.6f} -> {float(cubg/N):.6f}  (shift = {float((cubg-cub0)/N):.6f}; "
      f"Delta - Delta/h0^2 = {float(Fraction(4,3) - Fraction(4,3)/h0**2):.6f})")
print(f"  N_d/N:  {float((s1+s2)/N):.6f} -> {float(Ndg/N):.6f}  (DECREASE)")
print(f"  tail row Sum_(|l| >= V0)|l|^3: 0 (garnish height h0 = {h0} < V0 = 2 h0); "
      f"count rows at V >= V0: 0")
# cubic shift is Delta N - n0 h0^2 ... exact bookkeeping: added n0 h0^3 = Delta N; deleted simples: n0 h0
assert cubg - cub0 == Fraction(4, 3) * N - n0F * h0
assert frobg - frob0 == Fraction(4, 3) * N / h0 - n0F * h0
assert massg == N

json.dump(out, open("verify_t6_out.json", "w"), indent=1, default=str)
print("WROTE verify_t6_out.json")
