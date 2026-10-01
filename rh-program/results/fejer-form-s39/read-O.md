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
