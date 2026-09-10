#!/usr/bin/env python3
"""clause5_constants.py -- clauses 3(ii)/Theorem G and 5 of confinement-note.md from the sources read at the page.

Sources (read 2026-09-10; on disk fetched-r6/):
  HSW  = Hasanalizade-Shen-Wong, arXiv:2107.06506v1, Corollary 1.2: for T >= e,
         |N(T) - (T/2pi) log(T/(2 pi e))| <= 0.1038 log T + 0.2573 log log T + 9.3675.            (1.5)
         Theorem 1.1's (1.4) bounds |N(T) - (T/2pi) log(T/2pie) + 1/8| by the same shape; to cover both readings this
         script uses E(T) := 0.1038 log T + 0.2573 log log T + 9.3675 + 1/8.
  HSW (1.7): |S(T)| <= 2.5167 for 0 <= T <= 30 610 046 000 (Platt's database); HSW (5.6): for e <= T <= 30 610 046 000,
         |N(T) - (T/2pi) log(T/2pie) + 1/8| <= 2.5167 + 1/(50e) + 1.
  TRU  = Trudgian, arXiv:1208.5846v2, (2.5): for T >= 1, |N(T) - (T/2pi) log(T/2pie) - 7/8| <= 0.2/T + |S(T)|;
         (1.2): |S(T)| <= 1 for 0 <= T <= 280, |S(T)| <= 2 for 0 <= T <= 6.8e6 (Trudgian citing [3, 11]).
Window count: for H > 0 and T - H >= e,  N(T+H) - N(T-H) >= (H/pi) log((T-H)/2pi) - E(T-H) - E(T+H)   (main term is
  int_{T-H}^{T+H} (1/2pi) log(x/2pi) dx >= (2H/2pi) log((T-H)/2pi)).
Psi lower bound (clause 5):  Psi(s) >= [N(s+H) - N(s-H)] / cosh(pi H).
Layer: 2/sin(pi delta) + eps3 <= Psi  with eps3 <= 4.03 e^{-4pi} = 1.41e-5.
Budget: seconds.
"""
import json, sys
import numpy as np

out = {}
def E(T):
    return 0.1038 * np.log(T) + 0.2573 * np.log(np.log(T)) + 9.3675 + 0.125
eps3 = 4.03 * np.exp(-4 * np.pi)
out["eps3_max"] = float(eps3)
Gmax = 2 * np.arccosh(1 / eps3) / np.pi
out["G_max_for_clause3_ii"] = float(Gmax)
print(f"eps3 max = 4.03 e^(-4pi) = {eps3:.4e};  G_max with 1/cosh(pi G/2) >= eps3: {Gmax:.4f};  1/cosh(7.5 pi/2) = {1/np.cosh(7.5*np.pi/2):.4e}")

# ---- Theorem G: all consecutive gaps <= G0 -------------------------------------------------------
G0 = 7.5
# (a) HSW (5.6) range: window (T, T+G0] count >= (G0/2pi) log(T/2pi) - 2*(2.5167 + 1/(50e) + 1) > 0
c56 = 2.5167 + 1 / (50 * np.e) + 1
T_a = 2 * np.pi * np.exp(2 * c56 * 2 * np.pi / G0)
out["thmG_range_a_HSW_5_6"] = dict(bound_const=float(c56), gaps_le_G0_for_T_ge=float(T_a), valid_up_to=30610046000 - G0)
print(f"Theorem G (a): via HSW (5.6) (const {c56:.4f}): every (T, T+{G0}] with T >= {T_a:.1f} and T + {G0} <= 3.061e10 contains a zero")
# (b) HSW Cor 1.2 range: count >= (G0/2pi) log(T/2pi) - 2 E(T+G0) > 0
f = lambda T: (G0 / (2 * np.pi)) * np.log(T / (2 * np.pi)) - 2 * E(T + G0)
lo, hi = 1e3, 1e30
for _ in range(200):
    mid = np.sqrt(lo * hi)
    if f(mid) > 0: hi = mid
    else: lo = mid
out["thmG_range_b_HSW_cor12"] = dict(gaps_le_G0_for_T_ge=float(hi))
print(f"Theorem G (b): via HSW Cor 1.2 (+1/8): every (T, T+{G0}] with T >= {hi:.3e} contains a zero  (covers the end of range (a): {hi < 30610046000 - G0})")
# (c) alternative via Trudgian (2.5) + (1.2): |S|<=1 for T<=280 -> count >= (G0/2pi) log(T/2pi) - 2(1 + 0.2/T)
for Sb, Tmax in ((1.0, 280.0), (2.0, 6.8e6)):
    g = lambda T: (G0 / (2 * np.pi)) * np.log(T / (2 * np.pi)) - 2 * (Sb + 0.2 / T)
    lo2, hi2 = 15.0, Tmax
    for _ in range(200):
        mid = 0.5 * (lo2 + hi2)
        if g(mid) > 0: hi2 = mid
        else: lo2 = mid
    print(f"Theorem G (c): via TRU (2.5) with |S| <= {Sb} (T <= {Tmax:.1e}): gaps <= {G0} for T in [{hi2:.2f}, {Tmax - G0:.1e}]")
    out[f"thmG_range_c_S_le_{Sb}"] = dict(from_T=float(hi2), to_T=float(Tmax - G0))
# (d) Cor 1.4 second bound + (2.5): |S(T)| <= 0.1095 log T + 0.2042 log log T + 3.0305
h = lambda T: (G0 / (2 * np.pi)) * np.log(T / (2 * np.pi)) - 2 * (0.1095 * np.log(T + G0) + 0.2042 * np.log(np.log(T + G0)) + 3.0305 + 0.2 / T)
lo3, hi3 = 10.0, 1e12
for _ in range(300):
    mid = np.sqrt(lo3 * hi3)
    if h(mid) > 0: hi3 = mid
    else: lo3 = mid
out["thmG_range_d_cor14_plus_2_5"] = dict(gaps_le_G0_for_T_ge=float(hi3))
print(f"Theorem G (d): via HSW Cor 1.4 (second bound) + TRU (2.5): gaps <= {G0} for all T >= {hi3:.3e}")

# ---- clause 5: optimize H ------------------------------------------------------------------------
Hs = np.linspace(0.3, 3.0, 27001)
m = (Hs / np.pi - 2 * 0.1038) / np.cosh(np.pi * Hs)
i = int(np.argmax(m)); Hstar = float(Hs[i]); mstar = float(m[i])
C_uncond = 2 / (np.pi * mstar)
out["clause5_H_star"] = Hstar; out["clause5_m_star"] = mstar; out["clause5_C_uncond_asymptotic"] = float(C_uncond)
print(f"clause 5: m(H) = (H/pi - 0.2076)/cosh(pi H) is maximal at H* = {Hstar:.4f}, m* = {mstar:.6f};  C_uncond = 2/(pi m*) = {C_uncond:.2f}")
print(f"          (the contract's H = 4 pi c1 = {4*np.pi*0.1038:.4f} gives m = {((4*0.1038) - 2*0.1038)/np.cosh(np.pi*4*np.pi*0.1038):.6f}, C = {2/(np.pi*((4*0.1038) - 2*0.1038)/np.cosh(np.pi*4*np.pi*0.1038)):.1f})")

def Elog(logT):
    return 0.1038 * logT + 0.2573 * np.log(logT) + 9.3675 + 0.125
def Psi5(logt, H):
    # everything in terms of log t to avoid overflow: log((t-4-H)/2pi) = logt + log1p(-(4+H)e^{-logt}) - log 2pi
    q = (4 + H) * np.exp(-min(logt, 700.0))
    return ((H / np.pi) * (logt + np.log1p(-q) - np.log(2 * np.pi)) - 2 * Elog(logt + np.log1p(q))) / np.cosh(np.pi * H)
# t0: least log t with max_H Psi5 >= 2 + eps3
def best_Psi5(logt):
    Hs2 = np.linspace(0.5, 2.0, 1501)
    v = np.array([Psi5(logt, H) for H in Hs2])
    j = int(np.argmax(v)); return float(v[j]), float(Hs2[j])
lo4, hi4 = 5.0, 5000.0
for _ in range(100):
    mid = 0.5 * (lo4 + hi4)
    if best_Psi5(mid)[0] >= 2 + eps3: hi4 = mid
    else: lo4 = mid
out["clause5_log_t0"] = float(hi4)
print(f"clause 5: the statement becomes non-vacuous (Psi_5 >= 2) from log t0 = {hi4:.1f}  (t0 = e^{hi4:.0f})")
tab = []
for logt in (hi4, 400.0, 500.0, 1000.0, 3000.0, 1e4, 1e5):
    v, H = best_Psi5(logt)
    if v > 2 + eps3:
        d5 = float(np.arcsin(2 / (v - eps3)) / np.pi)
        tab.append(dict(log_t=float(logt), H=H, Psi5=v, delta5=d5, delta5_times_logt=d5 * logt, C_over_logt_with_C_uncond=float(C_uncond / logt)))
        print(f"  log t = {logt:8.1f}: best H = {H:.3f}, Psi_5 = {v:.4f}, uncertifiable from delta_5 = {d5:.5f}  (delta_5 log t = {d5*logt:.2f}; asymptote C_uncond = {C_uncond:.2f})")
out["clause5_table"] = tab
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "clause5_constants_out.json", "w"), indent=1)
print("done")
