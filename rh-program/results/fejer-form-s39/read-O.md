# read-O — OPUS READER on unit `fejer-form-s39` (NOTE.md: the Fejér defect as a positive form transported to the zeros, UT-4)

Reader: Opus 5.5 (second model of the dual-model check; standing orders 5, 7, 11(c)). Started 10:59 IST 2026-10-01 (machine clock).
NOTE read whole at SHA-256 3ad9a31e775ccece1ff4a7959eeda3266110d3f7fed82332ed19f11d3dacd292 (39 419 bytes, 330 lines). Also read:
BRIEF.md (unit), READ-BRIEF-O.md (this read), SHARED.md (Blocks 0–5), the unit's `verify/` scripts and logs (read for
definitions and numbers only; nothing imported or copied), `sources/` (text layers checked against the PDFs page by page),
BARRIER-ZOO.md IV.1 and I.9. Independent re-run: `verify-O/` (own code from the NOTE's definitions; exact integers and
rationals where the NOTE used floats). Not opened: read-F.md, verify-F/ (independence). No git.
Conventions: ✓ = re-derived at the line; GAP = stated with the fix; FALSE = counterexample or failing line given.
Line numbers below are NOTE.md lines at the hash above.

VERDICT LINE: (filled at the close of the read)

## §1. Re-derivations at the line

(a) §1 definitions (lines 47–56) ✓, with one silent step made explicit. The parametrization α_j = √q e^{±iθ_j}, j = 1..g,
    needs the roots ±√q to occur with even multiplicity. True for every datum with the sign-(+1) FE: a factor (1 − √q u) has FE
    sign −1, (1 + √q u) and every (1 − xu + qu²) sign +1, so the multiplicity of √q is even and 2g even forces that of −√q even
    (AHL 1201.4967 p. 13 states it, citing Stichtenoth). Also A_n ≥ 0 ⟹ h ≥ 0 (A_n = h(q^{n−g+1} − 1)/(q − 1) for n > 2g − 2), so
    "h ≥ 1" excludes exactly h = 0 (t = q + 1 at g = 1). b_d ∈ Z is automatic for Z ∈ 1 + uZ[[u]]; the constraint is b_d ≥ 0.
(b) THEOREM W (lines 88–109). (i) ✓: s_n = q^{n/2}Σ_j 2cos nθ_j; a functional a_0 + a_g g + Σ b_nN_n vanishing at P¹ is
    a_g g + Σ b_n(N_n − q^n − 1), i.e. c_0 = a_g, c_n = −b_n q^{n/2}. (ii) ✓, re-derived in three steps: (1) a real PSD Toeplitz T_M
    is the moment matrix of a positive measure on the circle (Carathéodory–Toeplitz), symmetrizable since p_n ∈ R; a symmetric
    measure of mass 2g is ∫ g(δ_θ + δ_{−θ}) d(μ/2g)(θ), so by Carathéodory in R^M, W_{g,M} = conv{equal-angle configurations} =
    conv{all real-angle configurations}, compact; (2) an affine functional ≥ 0 on W_{g,M} is ≥ 0 at (θ, …, θ), i.e. g·f_c(θ) ≥ 0,
    so f_c ≥ 0 on R, and conversely; (3) x*T_Mx = ℓ_Z(|P_x|²), mean |x|², Fejér–Riesz, ℓ_Z sees only the even part and the even
    part of an f ≥ 0 is ≥ 0 — so λ_min(T_M) = 2 min I_c. (iii) ✓. Scope: "separated" in (ii) means separated from W_{g,M}; lines
    98–99 say so, and K(ii) / §0(ii) drop it (F2).
(c) §3 numbers ✓. V: s_n = 5^{n/2}(φ^n + φ^{−n}), so T_M(V) = uvᵀ + vuᵀ (u_k = φ^{−k}, v_k = φ^k), eigenvalues (M + 1) ± |u||v| and
    0; |u|²|v|² = (M + 1) + Σ_{d=1}^{M}(M + 1 − d)L_{2d} = 5, 16, 45, 121, 320, 841, 2205, 5776 (exact integers, o2), giving all eight
    λ_min of lines 125–126. By hand: I(V) = 1 − 5/(2√5) = 1 − √5/2 = −0.1180339887; E₀: x³ + 2x takes 0, 3, 2, 3, 2 at x = 0..4 and
    the squares mod 5 are {0, 1, 4}, so N_1 = 1 + 1 = 2, t = 4, I(E₀) = 1 − 2/√5 = +0.1055728090. ½xᵀT_1x at x = (m, n√q) is
    m² + tmn + qn², = −1 at (2, −1) for V ✓. V₂: λ_min(T_1) = 4 − 1/√5 = 3.552786, λ_min(T_2) = −0.2931712 ✓.
(d) THEOREM F (lines 144–161). (a) ✓: Z = R − (h/(q−1))/(1 − u) + (hq^{1−g}/(q−1))/(1 − qu), using L(1/q) = q^{−g}L(1) from the FE,
    so A_n = h(q^{n−g+1} − 1)/(q − 1) for n > 2g − 2 and Θ_{2g−2+k} = hq^{g−1+k}. (R) for 0 ≤ n ≤ 2g − 2 follows from
    Z(u) = q^{g−1}u^{2g−2}Z(1/(qu)), which I re-derived from L's FE. AHL's Lemma 3.4 is stated "assume g ≥ 2" (p. 14); (10) holds
    for g = 0, 1 by a one-line check (and o1 verifies (R) on all 4591 data, g = 1 included) — m2. (b) ✓ AS STATED, for D_1 only:
    D_k at genus 0 is q^{k−1} − 1 > 0 for k ≥ 2 (P¹ over F_5: D_1, D_2, D_3 = 0, 4, 24; o1). So "equality exactly at genus 0" is
    FALSE for D_k, k ≥ 2, where §0(iii), K(iii), the §8 row and the I.9 rider attach it to D_k — F1. (c) ✓:
    q + 1 − 2√q cos θ = (√q − 1)² + 2√q(1 − cos θ); at g = 1, D_1 = (q − 1)(√q − 1)² + 2(q − 1)√q·I(Z). (d) ✓. (e) ✓, with
    log(q + 1 − 2√q cos θ) = log q + log|1 − q^{−1/2}e^{iθ}|² = log q − 2Σ q^{−n/2}cos(nθ)/n.
    The "Fejér pairing" reading (lines 137–142), re-derived: for deg D = −k, Riemann–Roch/Poisson gives 1 = q^{1−g−k}·q^{ℓ(K−D)},
    so each class's dual box holds q^{g−1+k} functions and the class-summed count of its nonzero ones is Θ_{2g−2+k} − Θ_{−k} = D_k ✓.
    The analog of M1a's φ̂(0) = 1 is vol O(D) = q^{1−g−k}, which is 1 only at (g, k) = (0, 1): D_1 is the exact transcription of
    the gap-width Fejér test; k ≥ 2 is a box narrower than the gap (positive defect already at genus 0, as a narrower Fejér
    kernel has at ζ). This supports F(b)'s restriction to D_1 and is the reason F1 is a real error, not a slip of notation.
(e) "WHERE V SITS" (lines 167–170) ✓: h = (√q − 1)² + 2√q w ≥ 1 ⟺ w ≥ 1 − √q/2; (√5 − 1)² = 6 − 2√5 = 1.5279 (h = 1 only, t = 5);
    (√7 − 1)² = 2.708 (h = 1, 2; t = 7, 6); (√11 − 1)² = 5.367 (h = 1..5; t = 11..7); upper side h > (√q + 1)² = 10.47, 13.29, 18.63
    gives t = −5; −6, −7; −7..−11 ✓. Genus-2 window counts 5/199, 47/675, 416/2935 ✓ (o1, exact comparison with (√q ± 1)^4 =
    q² + 6q + 1 ± 4(q + 1)√q; split below/above 5/0, 30/17, 195/221).
(f) §5 Bombieri reading (lines 189–197) ✓. Algebra: Q + (2g + 1)√Q + 1 − N_r = (2g + 1)√Q + s_r = √Q[1 + Σ_j(2 + 2cos rθ_j)];
    with the twist count 2(Q + 1) − N_r the sign of s_r flips, giving √Q[1 + Σ_j 4sin²(rθ_j/2)]. At the page (Bombieri 1973,
    p. 236, PDF page 4, read as an image): "THEOREM 1.– Assume q = p^α, where α is even. Then if q > (g + 1)^4 we have
    (5) ν_1 < q + (2g + 1)q^{1/2} + 1." At Q = 25, g = 1 the hypotheses hold (α = 2, 25 > 16); V's twist has 2·26 − 11 = 41 =
    25 + 15 + 1 points, so the strict (5) fails at equality ✓; cosh(2 log φ) = L_2/2 = 3/2 gives 5[1 + 2 − 3] = 0 ✓.
(g) §6 Z1 ✓ (P). (C_q) is M1a's line 216: ρ_q(1 − q^{−1/2}) = 2q^{−1/2}∫S(t/q)dN(t). For F_{a,q} at conductor Q = q²:
    ρ_Q = q·Res = q + 1 + a; Poisson Σ_{n∈Z}S(n/N) = N gives RHS = (2/q)[(q² − 1)/2 + a(q − 1)/2 + q·0] = (q − 1)(q + 1 + a)/q = LHS
    identically in a ✓ (2.95, 8.8, 2.5). Epstein ✓: φ = 1_B∗1_B vanishes on |v| ≥ 1 (shortest vector of Z + √5iZ is 1), so
    Σ_{v∈L}φ(v) = φ(0) = π/4 and Σ_{L*∖0}|1̂_B|² = √5·π/4 − π²/16 = 1.139354 — an identity of the lattice, as the NOTE says. Z2 ✓:
    1 + a2^{−s} + 2^{1−2s} = 2^{1/2−s}(2cosh((s − ½)log 2) + a/√2), so H(½ + x) = 2cosh(x log 2) + 2.9/√2 ✓ (Pólya's Φ > 0 is
    labeled recalled and carries no load — the Z2 verdict rests on the computation). Z3 definitions ✓ (o4a, o4b; §2).
(h) §7 Clifford (lines 246–254) ✓. h − N_1 = q(q + 1) − q(x_1 + x_2) + x_1x_2 = (q − x_1)(q − x_2) + q ✓. Class-summed Clifford:
    n = 1 gives (q − 1)N_1 + h ≤ hq ⟺ N_1 ≤ h ✓; n = 0 gives h ≥ 1 (free); n = 2 = 2g − 2 gives Θ_2 = qΘ_0 = q² − q + qh, equal to
    the bound (identity) ✓. Injectivity of C(F_q) → Pic¹(F_q) for g ≥ 1 and #Pic¹(F_q) = h (Pic¹ nonempty by F. K. Schmidt) are
    standard ✓. (a1, a2) = (−4, −15), q = 7: N_1 = 4, h = 1 − 4 − 15 − 28 + 49 = 3, x = 2 ± √33 ✓ by hand.
(i) THEOREM K (lines 256–273). (i) ✓ (for non-square q, all θ_j = 0 would need (1 − √q u)^{2g} ∈ Z[u]). (ii) ✓ only for separation
    from W_{g,M}; and "the optimum is Oesterlé's program" mis-describes the printed object: Oesterlé's program optimizes the UPPER
    bound on N_1 under Weil + "N_k ≥ N_1" (HPM p. 4 (4): "t_k ≤ t_1 + q^k − q"), a sign-constrained class that cannot see V (the
    NOTE's own line 122: "the untwisted Fejér kernels K_M (all c_n ≥ 0, the upper-bound class) catch t = −5 but NOT V") — F2.
    (iii) ✓ for D_1 (F1 for D_k). (iv) ✓ (numbers reproduced; Z3's are grid minima — m4).
(j) The meta-claim of §0 lines 28–30 ("a separator must come from an object — and every such object's output, read on the datum,
    is a member of this Weil family") is FALSE as worded if "this Weil family" is the Toeplitz cone: class-(B) separators are
    outputs of objects and are not in the cone. Counterexample (exact): I(Z) := 4g + N_1 − 6 over F_5. It is affine in (g, N_1),
    vanishes at P¹ (N_1 = 6), is ≥ 0 on EVERY genuine curve over F_5 (g = 1: N_1 ≥ ⌈6 − 2√5⌉ = 2; g ≥ 2: 4g − 6 > 0), and
    I(V) = −1. In Theorem W(i)'s form c_0 = 4, c_1 = −√5, f(θ) = 4 − 2√5 cos θ, f(0) = −0.472 < 0: not a Weil test. A printed
    nonlinear relative: AHL Cor. 2.10 (p. 8; announced p. 1), "|A(F_q)| ≥ (q + 1 − m)^g", m = ⌊2q^{1/2}⌋ — at q = 5, h ≥ 2^g,
    which V (h = 1) violates. Both are "Weil + integrality" (§3's class (B), Serre's refinement), so the CLOSE stands; the wording must name
    class (B) (F2). The final sentence of K (lines 271–273) also claims the Z conclusion "on Z" in general, while three Z-forms
    were tested (m5).

## §2. Independent re-run (`verify-O/`, own code from the NOTE's definitions; nothing imported from `verify/`)

| NOTE claim (line) | route in verify-O | result |
|---|---|---|
| census, §2 table (69–76): 11/326/15/880/23/3336; 9+2, 127+88+111, 11+4, 205+295+380, 13+10, 401+1247+1688 | o1_census: exact integers, box |a1| ≤ 12q, |a2| ≤ 40q² (3× the rigorous box |a1| ≤ 4q, |a2| ≤ 6q², which follows from |α| ≤ q, itself forced by N_n ≥ 0 for all n via Pringsheim on log Z); admissible to 8, 40 and 60; kinds by exact integer tests | every count reproduced exactly; lists to 8, 40, 60 coincide; max |a1|, |a2| = 8, 31 (q = 5), 12, 57 (q = 7), 18, 124 (q = 11) |
| V's N_1..N_8, the 111, V₂ (78–79) | o1 | reproduced; V₂ = (−1, 11) NONREAL-X |
| genuine curves (66–72, 80–82): 9/11/13 traces; 115 and 192 genus-2 L-polynomials; 12 RH-true non-curves at q = 5 | o3_genuine: numpy point counts over F_q and F_{q²}; every f at q = 5; degree-6 normal forms at q = 7 | 115, 192 (60000 and 32928 squarefree models); the 12 = the NOTE's list exactly; 13 at q = 7; all genuine L RH-true and in the census |
| every RH-true datum PSD to M = 8; every RH-false datum exits by M ≤ 3; first-exit distribution (112–114; r1_lp.log Mstar) | o2_toeplitz_exact: T_M ≅ H_M = [s_{|a−b|}q^{min(a,b)}] (integer), exact Fraction elimination with largest-diagonal pivoting — no rounding | RH-true: PSD exactly (no −6e−15 issue); exits {1:2}, {2:113, 3:86}, {1:4}, {1:12, 2:471, 3:192}, {1:10}, {1:184, 2:2359, 3:392} = r1_lp.log |
| λ_min(T_M(V)), M = 1..8 (125–126) | o2: closed form with exact integers |u|²|v|² and mpmath eigsy | −0.2360679775, −1, −2.7082039325, −6, −11.88854382, −22, −38.9574275275, −67 ✓ |
| I(V), I(E₀), V₂ (127–133) | o2 + hand | −0.1180339887, +0.105572809; V₂ 3.552786, −0.2931712 ✓ |
| (R), D_k, window, Clifford (163–171, 250–252) | o1 (exact) | (R) and D_k (k = 1..3) on all 4591; D_1 > 0 on all 3825 RH-false; window 5/199, 47/675, 416/2935; Clifford (−4, −15); (−8, −23), (−7, −34) ✓; P¹: D_2 = q − 1 ≠ 0 (F1) |
| Z3 on ζ: +0.0069 (234–235) | o4a: Odlyzko zeros1, 10 142 zeros < 10⁴, both signs; W(0) at 30 digits | 0.006926 at T = 0 (0.006925902025); interior minimum 0.007220 at T = 5.65 — the minimum sits at the endpoint T = 0 |
| Z3 on F_{2.9,2}: −872.45 at T = 13.80 (235–236) | o4a: factor zeros closed form, ζ zeros; grid then golden section at 30 digits | grid min −872.4505 at 13.80 (digit for digit); continuous min −872.7931 at T = 13.80176 |
| DH: 47 zeros in (50, 120), 43 on, 4 off; −681.66 at T = 85.49 (236–239) | o4b: own DH; FE residual 5e−20; on-line zeros by sign change; FULL-rectangle argument principle on [−2, 3]×[50, 120] (the NOTE used the right half path); off-line zeros located by box counts, no recalled seeds | N = 47 = 43 + 2 + 2; 0.808517182457 + 85.6993484854i, 0.65083008061 + 114.163342731i; grid min −681.6591 at 85.49 (off-line share −681.8654, on-line 0.2063); continuous min −682.3798 at T = 85.49290 |
| Z1, Epstein (219–225) | by hand (§1(g)) — identities | (q − 1)(q + 1 + a)/q for every a; √5π/4 − π²/16 = 1.139354 ✓ |

Two slips of mine, both fixed before the logged runs: o3's first run applied the F_{q²} square table to F_q values; o4b's first
run tracked the argument along undivided 70-unit sides and accepted a non-zero point as a zero by an absolute test on Λ (whose Γ
factor is ~10^{−29} at that height). The logged runs use the F_q character, ≤ 0.05 steps, and the test |f| < 10^{−12}.
Not re-run: the class-(A+)/(B) and Fejér-kernel catch counts of lines 116–124 (scipy LP; not load-bearing for the close; the
class-(B) phenomenon is re-derived by hand in §1(j)).

## §3. Prior art at the page (every PDF page checked with `pdftotext -f N -l N` against the text layer)

| NOTE's citation (line) | what the page says (quoted) | verdict |
|---|---|---|
| Howe–Lauter 1202.6308 p. 2 (202, 264, 286) | "and Serre [38] developed the “explicit formulæ” method (optimized by Oesterlé), which gives the best bound on Nq(g) that can be obtained formally using only Weil’s “Riemann hypothesis” for curves and the fact that for every d ≥ 0 the number of degree-d places on a curve is non-negative." (PDF p. 2) | quote exact. It is about UPPER bounds on N_q(g) under Weil + b_d ≥ 0 — not the separation LP of §3 (see F2) |
| HPM 2506.05212 §1.1 p. 3 (203) | "any trigonometric polynomial f which is nonnegative on the unit circle and whose coefficients in the cosine expansion are nonnegative gives a lower bound on t1." | exact. Same page, (3): the Gram matrix [2g, t1, t2, …; t1, 2gq, qt1, …; t2, qt1, …] — this is literally verify-O's integer matrix H_M |
| HPM p. 4 (186, 204, 264, 286) | "Therefore, the vector (t1, …, tn) must belong to a spectrahedron, and by minimising t1 over this convex set, one gets a lower bound on t1 for any curve. In fact, this semi-definite program is closely related to the dual of the optimization problem solved by Oesterlé, as shown in [HP19]" — the spectrahedron includes (4) "tk ≤ t1 + q^k − q" | exact; note "closely related to the dual", and that HP's SDP contains (4) (closed-point positivity), which §3's class (A) does not (m6, F2) |
| HPM §1.2 p. 4 (186, 208) | "with |ωj| = √q, and {ω1, …, ωg, ω̄1, …, ω̄g} stable under the action of Gal(Q̄/Q)" | exact |
| HPM "(1)", "p. 1–2" (205) | p. 1: "(q + 1) − 2g√q ≤ ♯X(Fq) ≤ (q + 1) + 2g√q" (unnumbered); (1) "|N1 − (1 + q)| ≤ 2g√q" is on p. 3 | page/label mismatch — m7 |
| HP 1409.2357 p. 7 (5) (109, 183, 204, 263) | Definition 4, (3) p. 6: "xi = ⟨γk, γk+i⟩ = ((q^i + 1) − ♯X(Fq^i))/(2g√(q^i))"; p. 7: "the Gram matrix of the family γ0, …, γn in E is" (5), 1 on the diagonal, xi off it | exact: (5) = T_M/(2g) ✓. The arXiv paper has one version (v1, 8 Sep 2014; abs page on disk); its p. 3: "we always recover the very same numerical upper bound for Nq(g) than those coming from Oesterlé bounds! We were not been able to understand this experimental observation." (SHARED Block 1 says "p. 2"; it is p. 3) |
| HP19 = Trans. AMS 372 (2019) 5409–5451 ("not fetched", 204, 297) | fetched for this read (DOI 10.1090/tran/7813 via Crossref; AMS abstract page via Firecrawl, `verify-O/sources/hp19-abstract.md`; the PDF itself redirected to the abstract): "We relate this set of bounds to those of Oesterlé, proving that these are inverse functions in some sense. We explain how the Riemann hypothesis for the curve X can be merely seen as a euclidean property coming from the Toeplitz shape of some intersection matrix on the surface X×X together with the general theory of symmetric Toeplitz matrices." | Theorem W(ii)'s mechanism (RH for X as Toeplitz-PSD of the Frobenius-graph Gram matrix) is printed in HP19's abstract; the Oesterlé relation is "inverse functions in some sense", not "its dual is" — m6. §9's Untried "HP19 at the page" is half-done (abstract only) |
| AHL 1201.4967 Lemma 3.4 p. 14 (54, 157–158, 206, 265) | "Lemma 3.4. Let P ∈ Pg(q), and assume g ≥ 2. If n ∈ Z, then (10) An = q^{n+1−g}A2g−2−n + P(1)πn−g, assuming that An = 0 si n < 0. In particular, (11) An = P(1)πn−g, n ≥ 2g − 1." (text-layer lines 811–814 ✓) | exact; the hypothesis g ≥ 2 is omitted in the NOTE while (R) is applied at g = 1 (true, §1(d)) — m2 |
| AHL p. 1 (159, 207) | "(q + 1 − m)^g ≤ |A(Fq)| ≤ (q + 1 + m)^g (Corollary 2.10 and 2.2) … m is the integer part of 2q^{1/2}. This inequality improves on (q + 1 − 2q^{1/2})^g ≤ |A(Fq)| ≤ (q + 1 − 2q^{1/2})^g, which is an immediate consequence of Weil’s inequality." | the NOTE's ellipsis is faithful (the printed upper bound carries a sign typo). Cor. 2.10 (p. 8), "|A(Fq)| ≥ (q + 1 − m)^g", is a PRINTED class-(B) separator of V (q = 5: h ≥ 2 > 1) — used in F2 |
| Bombieri 1973, Sém. Bourbaki 430, p. 236 (5) (191) | "THEOREM 1.– Assume q = p^α, where α is even. Then if q > (g + 1)^4 we have (5) ν1 < q + (2g + 1)q^{1/2} + 1." (PDF page 4, read as an image) | exact; hypotheses hold at Q = 25, g = 1 |
| M1a NOTE line 216 (C_q); lines 317–319 (42, 219) | (C_q) as quoted in §1(g); 317–319: "the defect 2Σ_k sinc²(n_k) is a positive form — but in the POSITIONS OF THE GENERALIZED INTEGERS, not in the zeros. Transporting it to the zero side is not done here and is not claimed." | exact |
| proof-mine Theorem P (28, 189) | lines 266–279: (iii) "no input of any class is a function of the zeta datum alone" | faithful paraphrase |
| C2 directions "line 99", "Untried line 168" (35, 275, 300) | at the recorded hash 04496dce…: line 99 is the Instruments header ✓; line 168 is blank, the "Extremal characterization of ξ" entry is line 176 | m8 |

## §4. FIX-FIRST pairs (OLD quoted exactly at NOTE hash 3ad9a31e…, line number first)

**F1 — "equality exactly at genus 0" is true for D_1 only; and "every zeta datum" includes P¹, where D_1 = 0.** Theorem F(b)
(line 147) is right; the close and its copies attach the equality clause to the whole family D_k. At genus 0, L = 1, h = 1:
D_k(P¹) = q^{k−1} − 1, i.e. 0, 4, 24 at q = 5 for k = 1, 2, 3 (o1). §1(d) gives the reason: only the degree −1 box is the
gap-width Fejér test. The fix is wording only; no conclusion moves (D_1 alone carries the positions-side verdict). Six pairs:

F1a, line 19
OLD: (iii) Theorem F: M1a's Fejér defect on q^Z is D_k = h(q^{g−1+k} − 1) (AHL Lemma 3.4): equality exactly at genus 0, genus-1 form
NEW: (iii) Theorem F: M1a's Fejér defect on q^Z is D_k = h(q^{g−1+k} − 1) (AHL Lemma 3.4); D_1 = h(q^g − 1) vanishes exactly at genus 0 (D_k(P¹) = q^{k−1} − 1 > 0 for k ≥ 2), genus-1 form

F1b, line 20
OLD: but > 0 on every zeta datum (V: 4)
NEW: but > 0 on every zeta datum of genus ≥ 1 (V: 4)

F1c, line 150
OLD: (d) D_k > 0 on every zeta datum.
NEW: (d) D_k > 0 on every zeta datum of genus ≥ 1 (at genus 0, D_1 = 0 and D_k = q^{k−1} − 1 for k ≥ 2).

F1d, lines 265–266
OLD: M1a's Fejér defect on q^Z is D_k = h(q^{g−1+k} − 1) (Theorem F; AHL Lemma 3.4): equality
OLD: exactly at genus 0, genus-1 form (q − 1)[(√q − 1)² + 2√q(1 − cos θ)] in the angle — but D_k > 0 on every zeta datum, V
NEW: M1a's Fejér defect on q^Z is D_k = h(q^{g−1+k} − 1) (Theorem F; AHL Lemma 3.4); D_1 vanishes
NEW: exactly at genus 0, genus-1 form (q − 1)[(√q − 1)² + 2√q(1 − cos θ)] in the angle — but D_k > 0 on every zeta datum of genus ≥ 1, V

F1e, line 281 (Instruments row)
OLD: — V-blind; = 0 exactly at genus 0 |
NEW: — V-blind; D_1 = 0 exactly at genus 0 (D_k(P¹) = q^{k−1} − 1 > 0 for k ≥ 2) |

F1f, line 329 (I.9 rider; two fragments)
OLD: with equality exactly at genus 0 and genus-1 form
NEW: with D_1 = 0 exactly at genus 0 (D_k(P¹) = q^{k−1} − 1 > 0 for k ≥ 2) and genus-1 form
OLD: it is > 0 on every zeta datum, V included (D_1(V) = 4)
NEW: it is > 0 on every zeta datum of genus ≥ 1, V included (D_1(V) = 4)

**F2 — "the separating ones are [exactly] the Toeplitz cone" is true only for separation from the Weil region W_{g,M}; and
"the optimum is Oesterlé's program, whose dual is HP19's SDP" mis-describes the printed objects.** Theorem W(ii) (lines 93–99)
is correct and scoped; the close drops the scope. Counterexample to the unscoped wording (exact, `verify-O/o5_classB.log`):
I(Z) := 17g/4 + N_1 − 6 over F_5 is affine in (g, N_1), vanishes at P¹, is > 0 on EVERY genuine curve over F_5 of genus ≥ 1
(min 1/4 at g = 1 since N_1 ≥ 6 − ⌊2√5⌋ = 2; min 5/2 on the 115 genus-2 L-polynomials; 3·17/4 − 6 > 0 for g ≥ 3), I(V) = −3/4 —
so it meets the brief's contract clause exactly — and in Theorem W(i)'s form f(θ) = 17/4 − 2√5 cos θ, f(0) = −0.222 < 0: NOT in
the Toeplitz cone. The window ⌊2√q⌋ < c_0 < 2√q gives the same at q = 7, 11 (c_0 = 21/4, 25/4). It is §3's class (B) (Weil +
integrality), and its M = 1 boundary member is PRINTED: the Weil–Serre lower bound, HPM p. 2, "(q + 1) − g⌊2√q⌋ ≤ ♯X(Fq)"
(c_0 = ⌊2√q⌋ = 4 at q = 5: V gives 1 < 2, E₀ gives equality); nonlinear relative: AHL Cor. 2.10 (p. 8), "|A(Fq)| ≥ (q + 1 − m)^g",
m = ⌊2q^{1/2}⌋ (V: h = 1 < 2). So brief stop line 2 ("a known Oesterlé/Serre bound") fires for class (B) too. Separately: Oesterlé's
program (Howe–Lauter p. 2) is the UPPER-bound optimization under Weil + b_d ≥ 0 — the sign class the NOTE itself shows is V-blind
(line 122) — while V's separator is a lower bound; and the printed relation is "closely related to the dual" (HPM p. 4) /
"inverse functions in some sense" (HP19 abstract), not "its dual is". The close K stands: class (B) is Weil + integrality. Five pairs:

F2a, lines 16–17
OLD: identically on every zeta datum; the separating ones are the Toeplitz cone = Hallouin–Perret's Hodge-index Gram cone on X × X;
OLD: the optimum is Oesterlé's program, whose dual is HP19's SDP — all printed (§5). The best separator of V is Weil's lower bound
NEW: identically on every zeta datum; those separating a datum from the Weil region W_{g,M} (all real-angle data) are the Toeplitz cone = Hallouin–Perret's Hodge-index Gram cone on X × X, while separators from the genuine integer data alone form the larger class (B), Weil + integrality (e.g. 17g/4 + N_1 − 6 ≥ 0 over F_5: V −3/4, f(0) < 0);
NEW: the method is Serre's explicit formula (Oesterlé optimized it for UPPER bounds, a class that does not see V), and HP's Gram SDP "is closely related to the dual of the optimization problem solved by Oesterlé" (HPM p. 4) — all printed (§5). The best Weil-test separator of V is Weil's lower bound

F2b, line 29
OLD: on V; a separator must come from an object — and every such object's output, read on the datum, is a member of this Weil family
NEW: on V; a separator must come from an object — and every such object's output found here, read on the datum, is a member of this Weil family or of its integrality refinement (class (B), which also separates V), class-summed Clifford excepted

F2c, lines 263–264
OLD: Σ_j f(θ_j) (Theorem W(i)); the separating ones are exactly the Toeplitz cone = the Hodge-index Gram cone of the Frobenius graphs on
OLD: X × X (HP 1409.2357 (5)); the optimum is Oesterlé's program (Howe–Lauter p. 2) and its dual is HP19's SDP (HPM p. 4). IV.1.
NEW: Σ_j f(θ_j) (Theorem W(i)); those separating a datum from the Weil region W_{g,M} are exactly the Toeplitz cone = the Hodge-index Gram cone of the Frobenius graphs on
NEW: X × X (HP 1409.2357 (5)); separators from the genuine integer data alone form class (B), Weil + integrality (17g/4 + N_1 − 6 over F_5; AHL Cor. 2.10); the method is Serre's explicit formula, optimized for upper bounds by Oesterlé (Howe–Lauter p. 2), and HP's Gram SDP "is closely related to the dual" of Oesterlé's problem (HPM p. 4; HP19). IV.1.

F2d, line 210
OLD: WHAT IS NEW RELATIVE TO OESTERLÉ (10(n)): nothing in the LP — it is Oesterlé's program, and its dual is HP19's Hodge-index SDP.
NEW: WHAT IS NEW RELATIVE TO OESTERLÉ (10(n)): nothing in the LP — it is Serre's explicit-formula method (Oesterlé's program is its upper-bound optimization); HP's Hodge-index Gram SDP is "closely related to the dual" of Oesterlé's problem (HPM p. 4), the two bounds being "inverse functions in some sense" (HP19, abstract).

F2e, line 325 (IV.1 rider; three fragments)
OLD: the inequalities of this shape that separate a datum from the RH-true data are exactly the Toeplitz cone
NEW: the inequalities of this shape that separate a datum from the convex hull of the real-angle data are exactly the Toeplitz cone (separation from the RH-true integer data alone admits class (B), Weil + integrality, e.g. 17g/4 + N_1 − 6 ≥ 0 over F_5)
OLD: the LP optimum is Oesterlé's (
NEW: the method is Serre's explicit formula, optimized for upper bounds by Oesterlé (
OLD: and its dual is HP19's SDP (Hallouin–Moustrou–Perret arXiv:2506.05212 p. 4)
NEW: and HP's Gram SDP "is closely related to the dual of the optimization problem solved by Oesterlé, as shown in [HP19]" (Hallouin–Moustrou–Perret arXiv:2506.05212 p. 4)
