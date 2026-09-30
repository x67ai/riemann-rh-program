# SHARED — unit `fejer-form-s39` (writer Opus 5.5, Session 39, 2026-10-01). Dated blocks, appended as work lands.

## Block 0 — 04:58 IST 2026-10-01 — inputs read at the line (SHA-256 prefixes)
35542ee1c6835ea1 results/fejer-form-s39/BRIEF.md (read whole)
e86f642a47cf4bde results/novel-wave-s37/insights-digest.md (§B7 lines 164–170; §F.3 UT-4 lines 415–418)
c3e46d120337c8c3 results/novel-wave-s37/beurling-fe/NOTE.md (§3, §4, §8, §9, §10 incl. lines 317–319, §11, §12)
36e9f69188a60467 results/novel-wave-s37/beurling-fe/read-F.md (§4(a)–(c))
fa0d729377df6a53 BARRIER-ZOO.md (I.9 line 136; III.20 line 376; IV.1 line 401)
eb5f3bb932f2827d results/novel-wave-s37/proof-mine/NOTE.md (§0, §1, R6, §3, §4 Theorem P, Z1)
73353b19df97e6a4 results/novel-wave-s37/proof-mine/verify/twin_g2.py (+ .log, verify-O/o_twin.log: 111 box hits)
0b22b7fce070b9e7 results/novel-wave-s36/tournament/NOTE.md (§2.1 DD1)
0cd5a38fe442b5b2 results/novel-wave-s36/tournament/verify/dd1_rung1_virtual.py (+ .log)
04496dce0b444d48 directions/C2-rigidity-conservation.md (Instruments table shape line 99; Untried line 161 ff.)
Plan: (1) exact enumeration of zeta data q = 5, 7, 11, g <= 2; genuine curves by brute force; (2) LP / Toeplitz
separation, expressed as a form in the Frobenius angles; (3) the disguise audit (IV.1); (4) the Fejér transport on q^Z;
(5) the Z-forms on zeta and the RH-false controls; (6) prior art at the page; (7) close T / K / G.

## Block 1 — 05:20 IST 2026-10-01 — census and separation computed
verify/r1_enumerate.log: zeta data q=5,7,11, g<=2 (counts in NOTE §2); 111 non-real-x genus-2 data at q=5 reproduced.
verify/r1_genuine.log: genuine L at q=5 (g=1: t=-4..4; g=2: 115 pairs from 60 000 squarefree models), q=7 (192 pairs), q=11 (g=1).
verify/r1_lp.log: every RH-true datum has Toeplitz T_M PSD (worst eigenvalue -6e-15); EVERY RH-false datum (3825 of them)
leaves the Weil region by M <= 3; the Weil LP class (A) catches all; class (B) (nonnegative only at genuine angles) catches
all but its optimum is never a Weil test (uses the discrete spectrum: RH + integrality).
verify/r1_V_detail.log: closed forms lambda_min(T_M(V)) = (M+1) - |u||v| match to 1e-10; LP(A) at M=1 is f = 1 - cos(theta)
(Weil's lower bound N_1 >= q+1-2g sqrt q); (1/2) x^T T_1(V) x = m^2 + 5mn + 5n^2 (proof-mine's norm form, -1 at (2,-1)).
Sources fetched (sources/fetch_sources.log): Howe-Lauter 1202.6308 (p. 2: explicit formulae = best bound from Weil RH + b_d >= 0),
Hallouin-Perret 1409.2357 (Gram of Frobenius graphs = normalized Toeplitz; p. 2: "same numerical upper bound ... Oesterle";
"We were not been able to understand this experimental observation"), Aubry-Haloui-Lachaud 1201.4967 (class-number bounds).

## Block 2 — 05:40 IST 2026-10-01 — Theorem W (§3) and Theorem F (§4) written; prior art at the page
verify/r1_lp_check.log: 890 class-(B) separations re-checked without BLAS; 0 are Weil tests (max min f = -0.1276).
verify/r1_transport.log: (R) on all 4591 data; D_k = h(q^{g-1+k}-1) > 0 on all 3825 RH-false data (V-blind); product formula ok;
class-number window catches all genus-1 RH-false data, 5/199, 47/675, 416/2935 at genus 2.
Printed (at the page): AHL 1201.4967 Lemma 3.4 = (R) + D_k formula; AHL p. 1 = the class-number window; HPM 2506.05212 p. 4:
the Hodge-index Gram SDP "is closely related to the dual of the optimization problem solved by Oesterle, as shown in [HP19]"
(HP19 = Trans. AMS 372 (2019) 5409-5451, not fetched; HP 2014 p. 2 had called it an unexplained "experimental observation").
Rung-1 verdict so far: K on both transports (zeros form = Weil test with multiplier 1; positions form = V-blind). Next: Z side.

## Block 3 — 06:10 IST 2026-10-01 — Z side done (§6)
verify/z_forms.log: Z1 (C_Q) for F_{2.9,2} 2.95 = 2.95 (RH-false passes; identity for every a); Epstein 2-D Fejer defect 1.139355
vs Poisson 1.139353; Z2 real-axis monotonicity passed by zeta, F_{2.9,2}, DH, Epstein (FE residuals <= 1.3e-30).
verify/z3_weil_fejer.log: zeta (10142 Odlyzko zeros < 1e4) min W = +0.0069 (vacuous); F_{2.9,2} min W = -872.45 at T = 13.80;
DH 47 zeros in (50,120) (argument principle 47.0000 = 43 on + 4 off), min W = -681.66 at T = 85.49 (off-line share -681.87).
Close forming: K. Rung-1 LP = Weil (IV.1, multiplier 1; printed: Serre-Oesterle, HP19); positions-side Fejer = V-blind (I.9);
Z1/Z2 passed by controls (RH-blind); Z3 = Weil's criterion.

## Block 4 — 06:30 IST 2026-10-01 — §7 (Clifford + Theorem K), §8 Instruments, §9 Untried, §10 waste line, §11 riders written
verify/r1_clifford.log: class-summed Clifford N_1 <= h at g = 2 catches 0/199 (q=5), 1/675 (q=7), 2/2935 (q=11); none of the 111.
Theorem K stated (NOTE §7). Zoo riders on IV.1 and I.9 proposed in BLOCK form (NOT inserted). Remaining: §0 close, final hashes.
