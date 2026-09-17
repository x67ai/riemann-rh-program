#!/usr/bin/env python3
"""r0_73_check.py -- the out-window radius R_0 = 73 of check-O.md section 12.8 (referee-O.md item 8), reproduced by the author
(Session 23 item 2, the addendum to separation-note.md).  Run from results/c2-m2/verify/.

Clause 5's chain (separation-note.md section 6) bounds the out-window sum by  S_Z <= 2 C1 e^{L/2} [log(3.5+t) Sigma_2 + Sigma_3].
The record spends the L-hypothesis  L/8 >= log log(3+t) + log(2 b1 C1)  TWICE (2 C1 <= e^{L/8}/b1 and log(3.5+t) <= 1.05 e^{L/8}),
for the exponent 3/4 + 1 = 7/4 to beat and R_0 = 81.  Spending it ONCE -- e^{L/8} >= 2 b1 C1 log(3+t) directly, so
2 C1 log(3.5+t) <= 1.05 e^{L/8}/b1 and 2 C1 <= e^{L/8}/b1 -- gives  S_Z <= (e^{5L/8}/b1)(1.05 Sigma_2 + Sigma_3), the exponent
5/8 + 1 = 13/8, the asymptote (13/(16 c_B))^2, and the one-point check
    F13(L) := (13/8 - 2 c_B sqrt R_0) L + 2 c_B/sqrt R_0 + log((1.05 P_2(L) + P_3(L))/b1) <= 0 at L_0 = 50,  F13 decreasing from 5/(2 c_B sqrt R_0 - 13/8) <= L_0,
with P_2, P_3 the SAME relaxed Laurent polynomials as lemma_G_constants.py (d) (functions copied verbatim).  The record's 7/4 chain is
re-run first as a regression check (must give 81, F(50) = -0.13339).  Constants read from the record, not re-derived."""
import json, sys, time
import mpmath as mp
t0 = time.time(); mp.mp.dps = 30
out = {}
gj = json.load(open("lemma_G_constants_out.json")); bj = json.load(open("b1_constant_out.json"))
cB = mp.mpf(gj["c_B"]); CB = mp.mpf(gj["C_B"]); b1 = mp.mpf(bj["b1_certified_upper"]); Z = mp.mpf(bj["Z"])
assert abs(cB - 2/mp.sqrt(72*mp.e)) < mp.mpf('1e-12') and abs(CB - mp.e**2/Z) < mp.mpf('1e-9')
print(f"constants (read from the record): c_B = {mp.nstr(cB,8)}, C_B = {mp.nstr(CB,7)}, b1 = {mp.nstr(b1,6)} (certified upper)")
# --- copied verbatim from lemma_G_constants.py (d) ---
def gamma_poly(n, a, s):      # sum_{j=0}^n n!/j! s^j / a^{n+1-j}  (= e^{a s} int_s^inf x^n e^{-a x} dx)
    return mp.fsum(mp.factorial(n)/mp.factorial(j)*s**j/a**(n+1-j) for j in range(n+1))
def P_relaxed(m, L, R0, L0):
    L = mp.mpf(L); R0 = mp.mpf(R0); a = 2*cB; sR = mp.sqrt(R0)*L; u0 = R0*L
    beta = 1 + 3/(2*(R0*mp.mpf(L0) - 1))
    phi0 = u0**m*(1 + cB/2*sR)**2
    integ = (2/L**(m+1))*(gamma_poly(2*m+1, a, sR) + cB*gamma_poly(2*m+2, a, sR) + cB**2/4*gamma_poly(2*m+3, a, sR))
    return beta**m*CB**2*(phi0 + integ)
# --- end of the copy; the exponent is now a parameter ---
def Ftilde(L, R0, L0, ex):
    L = mp.mpf(L); R0 = mp.mpf(R0)
    return (ex - 2*cB*mp.sqrt(R0))*L + 2*cB/mp.sqrt(R0) + mp.log((mp.mpf('1.05')*P_relaxed(2, L, R0, L0) + P_relaxed(3, L, R0, L0))/b1)
def least_R0(L0, ex):
    R0 = mp.mpf(1)
    while not (Ftilde(L0, R0, L0, ex) <= 0 and 2*cB*mp.sqrt(R0) - ex > 0 and 5/(2*cB*mp.sqrt(R0) - ex) <= L0):
        R0 += mp.mpf('0.5')
    return R0
E74 = mp.mpf(7)/4; E138 = mp.mpf(13)/8
# regression: the record's chain
r81 = least_R0(50, E74)
print(f"(0) regression, the record's exponent 7/4: least R_0 at L_0 = 50 = {mp.nstr(r81,4)}, F~(50) = {mp.nstr(Ftilde(50, r81, 50, E74),5)} (record: 81.0, -0.13339), decrease from L = {mp.nstr(5/(2*cB*mp.sqrt(r81) - E74),4)}")
out["regression_R0_74"] = float(r81); out["regression_F50_74"] = float(Ftilde(50, r81, 50, E74))
assert r81 == 81
# the sharper chain
print("(1) the L-hypothesis spent once: exponent 13/8; least R_0 (step 0.5) with F13(L0) <= 0 and 5/(2 c_B sqrt R_0 - 13/8) <= L0:")
R0tab = {}
for L0 in (50, 100, 200, 403, 1000, 10000):
    r = least_R0(L0, E138); R0tab[L0] = float(r)
    print(f"    L0 = {L0:6d}: R_0 = {mp.nstr(r,4)}   F13(L0) = {mp.nstr(Ftilde(L0, r, L0, E138),5)}   decrease from L = {mp.nstr(5/(2*cB*mp.sqrt(r) - E138),4)}   [record's 7/4 chain: {mp.nstr(least_R0(L0, E74),4)}]")
R0 = mp.mpf(R0tab[50])
print(f"    THE ADDENDUM'S R_0 (all L >= 50): {mp.nstr(R0,4)} (check-O section 12.8: 73);  asymptote (13/(16 c_B))^2 = {mp.nstr((13/(16*cB))**2,5)} (check-O: 32.30);  record's (7/(8 c_B))^2 = {mp.nstr((7/(8*cB))**2,5)}")
out["R0_138"] = float(R0); out["R0_table_by_L0_138"] = R0tab; out["asymptote_138"] = float((13/(16*cB))**2); out["asymptote_74"] = float((7/(8*cB))**2)
print(f"    one-point check at L0 = 50, R_0 = {mp.nstr(R0,4)}: F13(50) = {mp.nstr(Ftilde(50, R0, 50, E138),5)} <= 0: {bool(Ftilde(50, R0, 50, E138) <= 0)};  5/(2 c_B sqrt R_0 - 13/8) = {mp.nstr(5/(2*cB*mp.sqrt(R0) - E138),4)} <= 50: {bool(5/(2*cB*mp.sqrt(R0) - E138) <= 50)};  at R_0 = {mp.nstr(R0 - mp.mpf('0.5'),4)}: F13(50) = {mp.nstr(Ftilde(50, R0 - mp.mpf('0.5'), 50, E138),5)} (> 0, so 73 is least on the half-integer grid)")
out["F13_50_at_R0"] = float(Ftilde(50, R0, 50, E138)); out["F13_50_at_R0_minus_half"] = float(Ftilde(50, R0 - mp.mpf('0.5'), 50, E138)); out["decrease_from_L"] = float(5/(2*cB*mp.sqrt(R0) - E138))
worstF = -mp.inf
for L in [50, 55, 60, 70, 80, 100, 150, 200, 300, 403, 500, 1000, 2000, 5000, 10000, 100000]:
    F = Ftilde(L, R0, 50, E138); worstF = max(worstF, F)
    if L in (50, 60, 100, 403, 1000, 10000, 100000): print(f"    L = {L}: F13(L) = {mp.nstr(F,5)}")
print(f"    max F13 over the L-grid at R_0 = {mp.nstr(R0,4)}: {mp.nstr(worstF,5)}")
out["max_F13_grid"] = float(worstF)
# the absorption step itself, checked as inequalities on a grid of (t, C1) that satisfy the hypothesis with equality margin 0
print("(2) the single-use absorption: for L = 8(log log(3+t) + log(2 b1 C1)) exactly, e^{L/8} = 2 b1 C1 log(3+t), so 2 C1 log(3.5+t) <= 1.05 e^{L/8}/b1 needs log(3.5+t)/log(3+t) <= 1.05 and 2 C1 <= e^{L/8}/b1 needs log(3+t) >= 1:")
worst_ratio = max(mp.log(mp.mpf('3.5') + t)/mp.log(3 + mp.mpf(t)) for t in [3 + k/10 for k in range(0, 10000)])
print(f"    max log(3.5+t)/log(3+t) on t in [3, 1003]: {mp.nstr(worst_ratio,5)} (at t = 3; decreasing) <= 1.05: {bool(worst_ratio <= mp.mpf('1.05'))};  log(6) = {mp.nstr(mp.log(6),5)} >= 1: True")
out["max_log_ratio"] = float(worst_ratio)
# what the sharper window costs downstream: nothing but l_R
for L in (50, 403, 1000):
    print(f"    l_R at t = 1e6, L = {L}: log(4 + t + 81 L) = {mp.nstr(mp.log(4 + 10**6 + 81*L),6)} -> log(4 + t + 73 L) = {mp.nstr(mp.log(4 + 10**6 + 73*L),6)} (smaller: clause 4's bound and (7.1) only improve)")
print("(3) for the record: referee F's 70 (direct summation at L = 50) and referee O's crossing near 57 (t = 3, C1 = 1) fix (t, C1) and are not uniform; not recomputed here -- the note's second corrections section item (g) records them as such")
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "r0_73_check_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
