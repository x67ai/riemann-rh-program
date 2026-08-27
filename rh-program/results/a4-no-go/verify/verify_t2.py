# T2 verification: atom-only corner theorem, both benchmarks.
# (a) min N_d/N = 5/6 - (2/3)eps  under  mass = N, F1 <= (4/3)N(1+eps)
# (b) min p1  = 2 - (4/3)(1+eps)  (simple fraction)
# plus per-atom integrality identities and cross-checks against the shipped gate numbers.
import numpy as np, json, itertools
from fractions import Fraction
from scipy.optimize import linprog

out = {}

# --- (1) the per-atom inequalities behind both bounds (exhaustive over marks 1..50) ---
ms = np.arange(1, 51)
chk_a = np.all(2 * 1 >= 3 * ms - ms**2)          # 1 >= (3m - m^2)/2  <=> (m-1)(m-2) >= 0
chk_b = np.all((ms == 1).astype(int) >= 2 * ms - ms**2)  # 1_{m=1} >= 2m - m^2
eq_a = [int(m) for m in ms if 2 == 3 * m - m**2 + 2 - 2 or (m - 1) * (m - 2) == 0]
out["atom_ineq_Nd_all_m"] = bool(chk_a)
out["atom_ineq_p1_all_m"] = bool(chk_b)
print("per-atom: (m-1)(m-2) >= 0 for m in 1..50:", chk_a, "| equality at m in {1,2}")
print("per-atom: 1_{m=1} >= 2m - m^2 for m in 1..50:", chk_b, "| equality at m in {1,2}")

# --- (2) random integer-mark stress test of the aggregated bounds ---
rng = np.random.default_rng(1)
viol = 0
for r in range(20000):
    n_at = rng.integers(1, 65)
    m = rng.integers(1, 9, size=n_at)
    Nd, n1, mass, S2 = len(m), int(np.sum(m == 1)), int(m.sum()), int(np.sum(m**2))
    if 2 * Nd < 3 * mass - S2 or 2 * n1 < 2 * (2 * mass - S2) / 2 * 2 - 2 * (2 * mass - S2) + 2 * n1:
        pass
    if Nd < (3 * mass - S2) / 2 - 1e-12: viol += 1
    if n1 < (2 * mass - S2) - 1e-12: viol += 1
out["random_stress_violations"] = viol
print("random integer-mark stress (20000 draws): violations of either bound =", viol)

# --- (3) exact LP over grid k-doubles columns (laws), N = 64, both objectives ---
# column k: k doubles + (N - 2k) simples on the 65-site grid; F1 = N + 2k EXACT (T1);
# N_d = N - k; n1 = N - 2k.  LP over weights w_k: min E[obj] s.t. E[F1] <= B(1+eps)
# (and, checked separately, the two-sided band).
N = 64
ks = np.arange(0, N // 2 + 1)
for eps in (0.10, 0.05, 0.02, 0.002):
    B = Fraction(4, 3) * N
    Bup = float(B * (1 + Fraction(eps).limit_denominator(10**6)))
    for obj_name, obj in (("Nd", (N - ks) / N), ("p1", (N - 2 * ks) / N)):
        A_ub = [(N + 2 * ks).astype(float)]
        res = linprog(c=obj, A_ub=A_ub, b_ub=[Bup],
                      A_eq=[np.ones_like(ks, dtype=float)], b_eq=[1.0],
                      bounds=[(0, None)] * len(ks), method="highs")
        pred = 5 / 6 - (2 / 3) * eps if obj_name == "Nd" else 2 - (4 / 3) * (1 + eps)
        dev = abs(res.fun - pred)
        out[f"LP_{obj_name}_eps{eps}"] = {"lp": res.fun, "closed_form": pred, "dev": dev}
        print(f"eps={eps}: min {obj_name} = {res.fun:.10f}  closed form {pred:.10f}  dev {dev:.2e}")

# two-sided band does not change the optimum (upper edge is active):
eps = 0.05
res2 = linprog(c=(N - ks) / N,
               A_ub=[(N + 2 * ks).astype(float), -(N + 2 * ks).astype(float)],
               b_ub=[float(Fraction(4,3)*N*Fraction(105,100)), -float(Fraction(4,3)*N*Fraction(95,100))],
               A_eq=[np.ones_like(ks, dtype=float)], b_eq=[1.0],
               bounds=[(0, None)] * len(ks), method="highs")
out["LP_Nd_twosided_eps0.05"] = res2.fun
print(f"two-sided band, eps=0.05: min Nd = {res2.fun:.10f} (same as one-sided: "
      f"{abs(res2.fun - (5/6 - (2/3)*0.05)):.2e})")

# --- (4) exact rational corner at eps where (B-N)/2 is an integer ---
# eps = 1/16: B(1+eps) = (4/3)(64)(17/16) = 272/3; (B'-N)/2 = (272/3-64)/2 = 40/3 not integer.
# Use eps = 1/4: B' = (4/3)(64)(5/4) = 320/3 ... use exact-fraction LP by hand instead:
# E[k] = (B(1+eps) - N)/2 exactly; E[Nd]/N = 1 - E[k]/N = 5/6 - (2/3)eps (Fraction arithmetic).
for eps in (Fraction(1, 20), Fraction(1, 50), Fraction(1, 500)):
    Ek = (Fraction(4, 3) * N * (1 + eps) - N) / 2
    P = 1 - Ek / N
    assert P == Fraction(5, 6) - Fraction(2, 3) * eps
    n1frac = (N - 2 * Ek) / N
    assert n1frac == 2 - Fraction(4, 3) * (1 + eps)
print("exact Fraction arithmetic: P = 5/6 - (2/3)eps and p1 = 2 - (4/3)(1+eps) at eps = 1/20, 1/50, 1/500: PASS")
out["fraction_corner_check"] = "pass"

# --- (5) cross-checks against the shipped gate numbers ---
import os
gate_dir = "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/a4-m2-gate"
g = json.load(open(os.path.join(gate_dir, "gate-result.json")))
w = json.load(open(os.path.join(gate_dir, "witness_N64.json")))
# witness: P and E[F1] must satisfy P = (3N - E[F1])/(2N) (the corner law at the matched upper edge)
EF1 = sum(col["weight"] * col["F1"] for col in w["law"])
P_pred = (3 * N - EF1) / (2 * N)
out["witness_P"] = w["P"]; out["witness_EF1"] = EF1; out["witness_P_pred_from_corner"] = P_pred
print(f"shipped witness: P = {w['P']:.7f}; E[F1] = {EF1:.4f}; corner law (3N - E[F1])/(2N) = {P_pred:.7f}; "
      f"dev = {abs(w['P'] - P_pred):.2e}")
# each witness column: F1 = sum m^2 (grid Parseval) and Nd = #atoms
for col in w["law"]:
    S2 = sum(mm**2 for _, mm in col["atoms"])
    assert abs(col["F1"] - S2) < 1e-8, (col["tag"], col["F1"], S2)
    assert col["Nd"] == len(col["atoms"])
print("witness columns: F1 = sum m^2 and Nd = #atoms verified for all 3 columns")
# followup p1 numbers: matched cell 0.6101914 = 2 - (B1/N)(1+eps), B1/N = matched m2(1) center
fu = json.load(open(os.path.join(gate_dir, "followup-p1.json")))
out["followup_p1_keys"] = list(fu.keys())[:8]
print("followup-p1.json keys:", list(fu.keys())[:8])

json.dump(out, open("verify_t2_out.json", "w"), indent=1, default=float)
print("WROTE verify_t2_out.json")
