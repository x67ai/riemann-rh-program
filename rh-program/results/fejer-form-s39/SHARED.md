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

## Block 5 — 05:26 IST 2026-10-01 — CLOSE: K (NOTE §0, §7 Theorem K). Deliverables and hashes (SHA-256 prefixes)
3ad9a31e775ccece NOTE.md (39419 bytes; §0 close, §1–§11)
fd2c76adbe07895f verify/r1_clifford.py
077a8075f43730d3 verify/r1_enumerate.py
921cb4b6bf1f33f3 verify/r1_fejer_V.py
c4ff9e490d501f87 verify/r1_genuine.py
f6c31e555368be70 verify/r1_lp_check.py
77c0ab49f6ec1eff verify/r1_lp.py
423a1671667eb9cd verify/r1_transport.py
420054944442ac26 verify/r1_V_detail.py
dc78919b6a1009d2 verify/z_forms.py
8686d2486b82cda3 verify/z3_weil_fejer.py
Logs: every verify/*.py has its .log; data: verify/r1_zeta_data.json (all zeta data), r1_genuine.json, r1_lp_summary.json,
r1_transport_summary.json. Sources: sources/fetch_sources.log (5 items with SHA-256 prefixes + text layers).
Stop lines: 1 not fired; 2 fired (Oesterle/Serre; HP19 dual); 3 fired on Z1, Z2 (F_{2.9,2}, DH, Epstein pass). No git commands;
no file outside results/fejer-form-s39/ edited. Compute: one process at a time, longest run < 2 min.

## Block O-0 — 11:08 IST 2026-10-01 — Opus reader (read-O) starts
Reader: Opus 5.5, second model of the dual-model check (READ-BRIEF-O.md). NOTE read whole at SHA-256 3ad9a31e775ccece… (330 lines).
Writes only read-O.md, verify-O/, and O-blocks here. Plan: (1) re-derive Theorems W, F, K and the §7 Clifford claim; (2) exact
re-enumeration of the census q = 5, 7, 11, g <= 2 and genuine curves, exact-integer Toeplitz PSD test; (3) Z3 on zeta, F_{2.9,2}, DH;
(4) prior art at the page (Howe–Lauter, HP 2014, HPM 2025, AHL 2012, Bombieri 1973); (5) zoo riders against IV.1 and I.9.

## Block O-1 — 11:13 IST 2026-10-01 — census and exact Toeplitz test reproduced (verify-O/o1, o2)
o1_census.log (exact ints, own code, box |a1| <= 12q, |a2| <= 40q^2, admissible to 8, 40 and 60): 11/326/15/880/23/3336 data;
kinds 9+2, 127+88+111, 11+4, 205+295+380, 13+10, 401+1247+1688 — every NOTE §2 count reproduced; max |a1|, |a2| = 18, 124 at q = 11
(far inside the box). (R) and D_k = h(q^{g-1+k}-1) (k = 1..3) exact on all 4591; window catches 5/199, 47/675, 416/2935; Clifford
violators (-4,-15) at q=7, (-8,-23), (-7,-34) at q=11, none NONREAL-X. P^1: D_2 = q - 1 > 0 (equality at genus 0 holds for D_1 ONLY).
o2_toeplitz_exact.log (integer congruent matrix H_M = [s_|a-b| q^min(a,b)], exact Fraction elimination): every RH-true datum PSD to
M = 8 EXACTLY; first failing M for RH-false: {1:2}, {2:113, 3:86}, {1:4}, {1:12, 2:471, 3:192}, {1:10}, {1:184, 2:2359, 3:392} —
identical to r1_lp.log. V: P_M = 5, 16, 45, 121, 320, 841, 2205, 5776 (exact), lambda_min = -0.2360679775 … -67 as in the NOTE.
I(V) = -0.1180339887, I(E0) = +0.105572809; V2 lambda_min(T_1, T_2) = 3.552786, -0.2931712.

## Block O-2 — 11:26 IST 2026-10-01 — genuine curves and Z3 reproduced (verify-O/o3, o4a, o4b)
o3_genuine.log (own numpy point counts over F_q, F_{q^2}): g = 1 traces 9/11/13 at q = 5/7/11; g = 2: 60000 squarefree models at q = 5
-> 115 (a1, a2), 32928 at q = 7 -> 192; all RH-true and in the census; the 12 RH-true non-curves at q = 5 are exactly the NOTE's list.
(One slip of mine, fixed before the run that counts: the first run used the F_{q^2} square table for F_q values.)
o4a: zeta W(T) min 0.006926 at T = 0 (W(0) = 0.006925902025 at 30 digits; interior min 0.007220 at T = 5.65). F_{2.9,2}: grid min
-872.4505 at T = 13.80 (digit for digit); the continuous minimum is lower, -872.7931 at T = 13.80176 (W turns ~ 15 per 0.01 there).
o4b (own DH code; argument principle on the FULL rectangle [-2,3]x[50,120]; off-line zeros located by box counts, no recalled seeds):
N = 47 = 43 on + 2 off + 2 mirrors; off-line 0.808517182457 + 85.6993484854i, 0.65083008061 + 114.163342731i; FE residual 5e-20.
W grid min -681.6591 at T = 85.49 (off-line share -681.8654, on-line 0.2063) — reproduces the NOTE; continuous min -682.3798 at
T = 85.49290. Conclusion of §6 Z3 unaffected (grid minima stated as minima: a minor wording item).

## Block O-3 — 11:29 IST 2026-10-01 — read-O §1 (re-derivations) and §2 (re-run table) written
Every theorem re-derived: W(i)–(iii) ✓; F(a)–(e) ✓ (F(b) is stated for D_1 and is right); K(i), (iv) ✓; Clifford ✓; Bombieri (5) read
at the page (p. 236: "ν_1 < q + (2g + 1)q^{1/2} + 1", q = p^α, α even, q > (g+1)^4) ✓. Corrections forming:
F1 — "equality exactly at genus 0" attached to D_k (all k) in §0(iii), K(iii), §8 row, I.9 rider: FALSE for k >= 2 (D_k(P^1) = q^{k-1} - 1).
F2 — K(ii)/§0(ii)/§0 WHY/IV.1 rider: "the separating ones are the Toeplitz cone" holds for separation from the Weil region only;
counterexample to the unqualified wording: 4g + N_1 - 6 >= 0 over F_5 (all genuine curves, every genus; V: -1; f = 4 - 2 sqrt5 cos(theta)
< 0 at 0) — class (B); and "the optimum is Oesterle's program" mis-describes Oesterle's upper-bound LP, which cannot see V.
Minor so far: AHL Lemma 3.4's hypothesis g >= 2 not stated; C2 "Untried line 168" is line 176 at the recorded hash 04496dce…; Z3
values are grid minima (continuous: -872.7931, -682.3798); "on Z" in K's last sentence overreaches (three forms tested).
