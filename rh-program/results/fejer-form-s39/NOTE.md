# NOTE — unit `fejer-form-s39`: the Fejér defect as a positive form transported to the zeros (Untried UT-4)

Session 39, 2026-10-01. Writer: Opus 5.5 (unit agent). Brief: `BRIEF.md` (SHA-256 35542ee1…). Written in order as results
land; §0 is filled at the close. Conventions as in the record: (P) proved here; (C) computed in `verify/` with its log;
(Q) quoted at the page from `sources/` or an on-disk source; `[recalled, unverified]` carries no load.

## 0. CLOSE (filled last)

(pending)

## 1. The object and the rung-1 setting (definitions; nothing new)

The candidate (digest §F.3 UT-4; fe/NOTE.md:317–319). M1a's Theorem T is the equality case of a Fourier-side LP inequality: for
a positive self-dual μ = ρδ₀ + dN + dN^∨ with the gap (−1, 1), pairing μ̂ = μ with the Fejér triangle φ = (1 − |x|)₊ gives
2Σ_k sinc²(n_k) = 0 — a positive form in the POSITIONS n_k of the generalized integers. UT-4 asks whether that form, carried to
the ZEROS, is a positivity generator (S4) that is not Weil's cone. The brief fixes the first rung: rung 1, the norm group q^Z.

Zeta data (proof-mine §4, verbatim definition). Z(u) = L(u)/((1 − u)(1 − qu)), L ∈ Z[u] of degree 2g, L(0) = 1,
L(u) = q^g u^{2g} L(1/(qu)); N_n = q^n + 1 − s_n ≥ 0 with s_n = Σ_i α_i^n (α_i the reciprocal roots); closed-point counts
b_d = (1/d)Σ_{e|d} μ(d/e)N_e ∈ Z_{≥0}; h = L(1) ≥ 1. Write α_j = √q e^{±iθ_j} (j = 1..g); θ_j is real iff RH holds for the
pair, and for V (q, t) = (5, 5) it is θ_V = i·log φ (φ the golden ratio; cos θ_V = √5/2, proof-mine §1). Normalized power
sums p_n := s_n q^{−n/2} = Σ_j 2cos(nθ_j) (real for every datum, genuine or not); p_0 := 2g.
Positions side (P). A_n := #effective divisors of degree n = coefficient of u^n in Z; Θ_n := (q − 1)A_n + h for n ≥ 0 and
Θ_n := h for n < 0 (on a curve, Θ_n = Σ_{deg c = n} q^{ℓ(c)} over the h classes of degree n). The FE of Z is equivalent to
Θ_n = q^{n−g+1}Θ_{2g−2−n} for all n ∈ Z (class-summed Riemann–Roch; proof: expand (q − 1)Z(u) + hΣ_{n<0}u^n and apply the FE
termwise — checked on every datum below, §4). This is the "discrete self-dual measure on q^Z" of the brief.
Controls (zoo I.9; brief). V: t = 5 over F₅ (RH-false, real off-line pair). E₀: y² = x³ + 2x over F₅, t = 4. V₂ and the 111
genus-2 data over F₅ with non-real off-line roots (proof-mine verify/twin_g2.log; o_twin.log). They are RH-FALSE: a separating
inequality must be VIOLATED by them. (The brief's parenthesis "E₀ and all 111 genus-2 / genus-1 data satisfy" is read as
"E₀ and all GENUINE genus-1 / genus-2 data satisfy"; the 111 are virtual, and §3 reports them as violators.)

## 2. Rung-1 census: every zeta datum at q = 5, 7, 11, g ≤ 2, and every genuine curve at q = 5, 7 — (C)

`verify/r1_enumerate.{py,log}` (exact integers; admissible = N_n ≥ 0 and b_d ∈ Z_{≥0} for n, d ≤ 8, and separately to 40 —
the two lists coincide at every (q, g); box forced by N_n ≥ 0, no hit on its edge). `verify/r1_genuine.{py,log}` (brute
force: all short Weierstrass curves; all y² = f(x), f squarefree of degree 5 or 6 — every f at q = 5, normal forms at q = 7;
N_1, N_2 by direct count over F_q and F_{q²}).

| (q, g) | zeta data (h ≥ 1) | RH-true | RH-false: real off-line / non-real x | genuine L realized | RH-true, not a curve |
|---|---|---|---|---|---|
| (5, 1) | 11 (t = −5..5) | 9 | 2 (t = ±5) / 0 | 9 (t = −4..4) | 0 |
| (5, 2) | 326 | 127 | 88 / **111** (= twin_g2's 111, V₂ among them) | 115 | 12 |
| (7, 1) | 15 (t = −7..7) | 11 | 4 (t = ±6, ±7) / 0 | 11 | 0 |
| (7, 2) | 880 | 205 | 295 / 380 | 192 | 13 |
| (11, 1) | 23 (t = −11..11) | 13 | 10 / 0 | 13 | 0 |
| (11, 2) | 3336 | 401 | 1247 / 1688 | not enumerated | — |

Reproduced from the record: V's N_1..N_8 = 1, 11, 76, 451, 2501, 13376, 70001, 361251 and b_1..b_8 = 1, 5, 25, 110, 500, 2215,
10000, 45100 (tournament dd1 log; proof-mine baseline); the 111 genus-2 non-real-x data at q = 5 (twin_g2.log). The degenerate
t = q + 1 (Z ≡ 1, h = 0) is excluded by h ≥ 1, as in proof-mine §4. Every genuine L is RH-true (Weil's theorem, seen in the
data) and admissible. The RH-true data realized by no curve (q = 5: (a1, a2) = (±5, 16), (±3, 12), (±2, −1), (±1, 10), (0, −9),
(0, −8), (7, 22), (8, 26)) are irrelevant to RH: every inequality below that is valid on all RH-true data is valid on them too;
that some Weil polynomials of abelian surfaces are not Jacobians is classical (Maisner–Nart 2002, Howe–Nart–Ritzenthaler 2009
`[recalled, unverified]`; not load).

## 3. Rung 1, the LP: every separating inequality is a Weil test; the best one for V is Weil's lower bound — (P) + (C)

THEOREM W (rung-1 Weil completeness). Fix q and M ≥ 1.
(i) (the explicit formula as an identity on zeta data.) For c = (c_0, …, c_M) ∈ R^{M+1} and every zeta datum Z of genus g
(genuine or virtual; θ_j complex allowed),
      I_c(Z) := c_0·g + Σ_{n=1}^{M} c_n q^{−n/2}(q^n + 1 − N_n(Z)) = Σ_{j=1}^{g} f_c(θ_j),   f_c(θ) := c_0 + 2Σ_n c_n cos nθ.   (E)
Every functional affine in (g, N_1, …, N_M) that vanishes at P¹ (g = 0, N_n = q^n + 1) is an I_c; and I_c = 0 at genus 0.
(ii) (the Weil region.) For a datum of genus g let T_M(Z) := [p_{|a−b|}]_{a,b=0..M}, p_0 = 2g. Then
      λ_min(T_M(Z)) = 2·min{ I_c(Z) : f_c ≥ 0 on R, deg f_c ≤ M, c_0 = 1 },
so Z is separated from the RH-true data by an affine count inequality of degree ≤ M iff T_M(Z) is not PSD, and every such
separating inequality is Σ_j f(θ_j) ≥ 0 with f ≥ 0 on the circle — a Weil test, multiplier 1 (IV.1's form, on rung 1).
(iii) (validity on genuine curves.) If f_c ≥ 0 on R then I_c ≥ 0 on every genuine curve (Weil's RH makes every θ_j real),
with I_c = 0 at genus 0 and I_c > 0 at genus g ≥ 1 unless every θ_j is a zero of f_c.
Proof. (i) s_n = Σ_i α_i^n = q^{n/2}Σ_j 2cos(nθ_j), so Σ_j f_c(θ_j) = g c_0 + Σ_n c_n p_n with p_n = q^{−n/2}(q^n + 1 − N_n).
An affine functional a_0 + a_g g + Σ b_n N_n vanishing at P¹ is a_g g + Σ_n b_n(N_n − q^n − 1): take c_0 = a_g, c_n = −b_n q^{n/2}.
(ii) For x ∈ C^{M+1}, x*T_M x = Σ_{a,b} x_a x̄_b p_{|a−b|} = ℓ_Z(|P_x|²), where P_x(z) = Σ x_a z^a and ℓ_Z(Σ_n F_n e^{inθ}) :=
Σ_n F_n p_{|n|} (formally Σ_j [f(θ_j) + f(−θ_j)]); ℓ_Z sees only the even part of f, and for a cosine polynomial ℓ_Z(f_c) = 2I_c.
By Fejér–Riesz every trigonometric polynomial f ≥ 0 of degree ≤ M is |P|² with deg P ≤ M, and ∫|P_x|²dθ/2π = |x|²; so the
minimum of x*T_M x over |x| = 1 is the minimum of ℓ_Z over f ≥ 0 of mean 1. (iii) ℓ_Z(f) = Σ_j[f(θ_j) + f(−θ_j)] ≥ 0 for real θ_j. ∎
Status: the pieces are printed — (E) is Serre's explicit formula for curves, the Gram/Toeplitz form of (ii) is Hallouin–Perret's
(1409.2357 p. 7 eq. (5), from the Hodge index theorem on X × X), and its duality with Oesterlé's LP is HP19 (§5 below, at the page).

THE COMPUTATION (`verify/r1_lp.{py,log}`, `verify/r1_V_detail.{py,log}`; M = 8; scipy HiGHS).
- Every RH-true datum at q = 5, 7, 11, g ≤ 2 has T_M PSD for all M ≤ 8 (worst eigenvalue −6·10⁻¹⁵, rounding).
- EVERY RH-false datum (3825: q = 5: 2 + 199; q = 7: 4 + 675; q = 11: 10 + 2935) has T_M indefinite at some M ≤ 3
  (first failing M: g = 1 always M = 1; q = 5, g = 2: M = 2 for 113, M = 3 for 86). So the LP region of genuine curves never
  contains a virtual datum: the brief's first stop line ("the LP region … contains V") does NOT fire.
- Class (A) (f ≥ 0 on the circle) catches all 3825. Class (B) (f ≥ 0 only at the genuine angles, the LP over the genuine
  finite set) catches all, and its optimum is NEVER a Weil test (min f on the circle < 0 in all 2 + 199 + 4 + 675 + 10 cases):
  class B consumes the discrete spectrum, i.e. RH plus integrality of the traces — a refinement of the Weil test, not a new
  generator (its validity proof is RH + t ∈ Z; §5).
- V in closed form: θ_V = iy, e^y = φ, T_M(V) = uvᵀ + vuᵀ (u_k = φ^{−k}, v_k = φ^k), λ_min = (M + 1) − |u||v| =
  −0.2361, −1, −2.7082, −6, −11.889, −22, −38.957, −67 (M = 1..8); LP(A) reproduces half of each to 10⁻⁷.
- The best inequality at M = 1 is f = 1 − cos θ = 2sin²(θ/2), i.e. I(Z) = g − (q + 1 − N_1)/(2√q) ≥ 0 ⟺ N_1 ≥ q + 1 − 2g√q:
  WEIL'S LOWER BOUND. V: I = 1 − √5/2 = −0.11803 (N_1 = 1 < 1.5279); E₀: I = +0.10557; P¹: I = 0.
  As a quadratic form in the Frobenius angle: ½xᵀT_1(Z)x with x = (m, n√q) is m² + tmn + qn² — proof-mine's norm form
  (B7's second form); at V it is −1 at (m, n) = (2, −1) (computed). So the rung-1 "Fejér form in the angles" that separates V
  and proof-mine's decisive quadratic form are the same object: the 2 × 2 Toeplitz (Gram) matrix of the Frobenius angle.
- V₂ (q = 5, (a1, a2) = (−1, 11)): T_1 PSD (λ = 3.553), T_2 not (λ = −0.2932, eigenvector ≈ (−0.70, 0.15, −0.70), i.e.
  f = 0.4894·|1 − 0.2083e^{iθ} + e^{2iθ}|²); the Fejér kernels catch it first at M = 3 (untwisted −0.145, twisted −0.055).

## 4. The transport: the Fejér pairing on q^Z, its defect, and its form in the zeros — (P) + (C)

The rung-1 analog of M1a's Step 1. On a curve, K ⊂ A_K is a self-dual lattice and Poisson summation for the box 1_{O(D)} is
Riemann–Roch; the GAP is L(D) = {0} for deg D < 0 (analog of supp dN ⊂ [1, ∞)); a box of degree −k (k ≥ 1) is the Fejér test
(supported in the gap, Fourier transform a positive multiple of the dual box, of degree 2g − 2 + k); the gap side sees only the
zero function ("⟨μ, φ⟩ = ρ"), the dual side sees 1 + #(L(K − D)∖0) ("ρφ̂(0) + 2Σ_k S(n_k)"). Summed over the h classes of a
degree (the only form a virtual datum has), this is identity (R) of §1 at n = −k [recalled for the adelic reading, Tate/Weil;
nothing below uses it — (R) is proved from the FE].

THEOREM F (the Fejér defect on q^Z and its transport). For every zeta datum Z of genus g over F_q and every k ≥ 1:
(a) Θ_{−k} = h and Θ_{2g−2+k} = q^{g−1+k}·Θ_{−k}; so the Fejér defect D_k(Z) := Θ_{2g−2+k} − Θ_{−k} = (q − 1)A_{2g−2+k} =
    h(q^{g−1+k} − 1).
(b) D_1 = h(q^g − 1) ≥ 0, with EQUALITY EXACTLY AT GENUS 0 (h ≥ 1).
(c) h = Π_{j=1}^{g} [(√q − 1)² + 2√q·w_j], w_j := 1 − cos θ_j. At g = 1: D_1 = (q − 1)[(√q − 1)² + 2√q·w(θ)] — an explicit form in
    the Frobenius angle, AFFINE in §3's separating form w = 1 − cos θ (the M = 1 twisted Fejér / Weil lower-bound test).
(d) D_k > 0 on every zeta datum. Its positivity is dN ≥ 0 (A_n ≥ 0 for n > 2g − 2 is h ≥ 0) and h ∈ Z_{≥1}: positive for free.
(e) For genuine curves (√q − 1)^{2g} ≤ h ≤ (√q + 1)^{2g}, i.e. Σ_j f_±(θ_j) ≥ 0 for f_±(θ) := ±log[(q + 1 − 2√q cos θ)/(√q ∓ 1)²],
    two Weil tests (f_± ≥ 0 on the real circle; log(q + 1 − 2√q cos θ) = log q − 2Σ_{n≥1} q^{−n/2}cos(nθ)/n).
Proof. Partial fractions: deg L = 2g, so Z(u) = R(u) − (h/(q − 1))/(1 − u) + (hq^{1−g}/(q − 1))/(1 − qu) with deg R ≤ 2g − 2,
using L(1) = h and L(1/q) = q^{−g}h (the FE at u = 1/q). Hence A_n = h(q^{n−g+1} − 1)/(q − 1) for n > 2g − 2, so
Θ_{2g−2+k} = hq^{g−1+k}, while Θ_{−k} = h by definition: (a). (b) from (a). (c) L(u) = Π_j(1 − x_j u + qu²) with
x_j = 2√q cos θ_j, so h = L(1) = Π_j(q + 1 − x_j). (d) from (a), h ≥ 1. (e) RH gives x_j ∈ [−2√q, 2√q]; take logs. ∎
Printed: (R) with (a) is Aubry–Haloui–Lachaud's Lemma 3.4, (10)–(11) (`sources/arxiv-1201.4967.txt` lines 811–814, printed p. 14 —
"A_n = q^{n+1−g}A_{2g−2−n} + P(1)π_{n−g}" and "A_n = P(1)π_{n−g}, n ≥ 2g − 1", for their "virtual zeta functions" §3.2); the
window in (e) is theirs too, p. 1: "(q + 1 − 2q^{1/2})^g ≤ |A(F_q)| ≤ …, which is an immediate consequence of Weil's inequality".
The READING of (R) as the Fejér pairing of M1a on q^Z, and (c)'s affine link at g = 1, are this unit's `[novelty: single-check]`
(a reading of printed identities; no mathematics is claimed new).

COMPUTED (`verify/r1_transport.{py,log}`, exact integers except (c)): (R) holds on all 4591 data for n ∈ [−4, 2g + 2]; D_k =
h(q^{g−1+k} − 1) for k = 1, 2, 3 on all; (c) to 10⁻⁶ on all; D_k > 0 on ALL 3825 RH-false data — so the positions-side form
cannot see a single virtual datum. V: A_n = 1, 1, 6, 31, 156, … = (5ⁿ − 1)/4 (V's divisor counts are P¹'s shifted one degree:
Z_V = 1 + u·Z_{P¹}, since 1 − 5u + 5u² = (1 − u)(1 − 5u) + u), h = 1, D_1 = 4.
WHERE V SITS. At g = 1, free positivity (h ≥ 1) is w ≥ 1 − √q/2 and RH is w ≥ 0; the gap between them is
1 ≤ h < (√q − 1)² = 1.528 at q = 5 — exactly one integer, h = 1, which is V (w(V) = 1 − √5/2 = −0.11803, the extreme point of
the free region). At q = 7 the gap is h ∈ {1, 2} (t = 7, 6); at q = 11, h ∈ {1..5} (t = 11..7) — the RH-false data of §2's
lower side, exactly. The upper side (t = −5, −7, −6, −11..−7) is h > (√q + 1)².
The RH form (e) at genus 2 (C): it catches every genus-1 RH-false datum but only 5 of 199 (q = 5), 47 of 675 (q = 7), 416 of 2935
(q = 11) genus-2 ones — one Weil test (a single f_±) is weak; §3's Toeplitz family catches all.
READING. The Fejér defect of M1a, carried to rung 1 exactly, splits in two: its POSITIONS form D_k is positive for free and
V-blind (zoo I.9: "a mechanism the virtual curve passes cannot be the generator"), and its ZEROS form — the factor
(√q − 1)² + 2√q·w in (c), normalized by its RH floor — is a Weil test. B7's phrase "only the first is positive for free" is,
on rung 1, a theorem with a mechanism: it is positive for free BECAUSE its positivity is dN ≥ 0, which V has.

## 5. The disguise audit (zoo IV.1, III.20) and the prior-art gate at the page (standing orders 1, 7; 10(n))

IV.1's EXECUTABLE TEST, run on rung 1. Observables: the prime-side counts N_1..N_M (closed-point data, band n ≤ M). Theorem W(i)
expresses every affine count functional vanishing at genus 0 as the classical Weil test Σ_j f(θ_j) with MULTIPLIER 1 on the band
— the expression succeeds, so the LP route has no new data coordinate; its "generator" f ≥ 0 is the Toeplitz cone, which is the
Hodge-index Gram cone of the Frobenius graphs on X × X (HP 1409.2357 eq. (5), p. 7: "Gram(γ_0, …, γ_n)" = the normalized
Toeplitz matrix) — III.20(B)'s doubled-object positivity, restricted to the band. Analytic-continuation leak: none (the Fejér
family K_M is indexed by the band M, one band per member). Class (B) is a cone restriction by integrality whose validity proof
takes RH as input (HPM 2506.05212 §1.2, p. 4: Serre's refinement from "{ω_1, …, ω_g, ω̄_1, …, ω̄_g} stable under Gal(Q̄/Q)").
The positions form D_k is NOT a Weil test (it is nonlinear in the prime data and positive for free) and fails I.9 instead.
Its RH form (Theorem F(e)) is, after the log, the pair of Weil tests f_± with multiplier 1 on the full band.
The other rung-1 classes read on zeta data (proof-mine Theorem P). Every output inequality of the four proof classes is a Weil
test of this family, specialized to g = 1: A and D give ½xᵀT_1x = m² + tmn + qn² (the 2 × 2 Toeplitz, §3); C (Bombieri 1973
p. 236 (5), `results/novel-wave-s37/proof-mine/sources/bombieri-1973-bourbaki430-stepanov.pdf`) gives, with Q = q^r,
Q + (2g + 1)√Q + 1 − N_r = √Q[1 + Σ_j(2 + 2cos rθ_j)] — the UNTWISTED test 2 + 2cos rθ plus slack √Q, which V passes
(cos(r·iy) = cosh ry > 0: proof-mine R6, "Theorem 1 NEVER separates") — and for the quadratic twist of a g = 1 cover
(ν_1(ι) = 2(Q + 1) − N_r) it gives √Q[1 + Σ_j(2 − 2cos rθ_j)] = √Q[1 + Σ_j 4sin²(rθ_j/2)], the TWISTED Fejér test of §3 at
frequency r. At V, Q = 25: 5[1 + 2 − 2cosh(2 log φ)] = 5[3 − L_2] = 0, so (5)'s strict "< 41" fails at equality 41 = 41 —
proof-mine's L4 number, recovered from the angle form. `[reading: single-check]`. So on rung 1 the separating INEQUALITY is
always the same Weil functional; what the four proofs differ in is the OBJECT that proves it (Theorem P) — this unit adds no object.

Prior-art table (at the page unless marked).
| item here | nearest published object | where read |
|---|---|---|
| identity (E); the LP over zeta data | Serre's explicit formulae, optimized by Oesterlé: "the best bound … that can be obtained formally using only Weil's 'Riemann hypothesis' for curves and the fact that for every d ≥ 0 the number of degree-d places on a curve is non-negative" | Howe–Lauter 1202.6308 p. 2 |
| the Weil test class | "any trigonometric polynomial f which is nonnegative on the unit circle and whose coefficients in the cosine expansion are nonnegative gives a lower bound on t_1" | HPM 2506.05212 §1.1 p. 3 |
| Theorem W(ii) (Toeplitz / Gram) and its dual | HP's Gram matrix (5); "this semi-definite program is closely related to the dual of the optimization problem solved by Oesterlé, as shown in [HP19]" (HP19 = Trans. AMS 372 (2019) 5409–5451, not fetched) | HP 1409.2357 p. 7; HPM p. 4 |
| V's best separating inequality | Weil's lower bound N ≥ q + 1 − 2g√q (HPM's (1)) | HPM p. 1–2 |
| Theorem F(a) (the Fejér pairing on q^Z) | "A_n = q^{n+1−g}A_{2g−2−n} + P(1)π_{n−g}" and "A_n = P(1)π_{n−g}, n ≥ 2g − 1", for "virtual zeta functions" | AHL 1201.4967 Lemma 3.4, p. 14 |
| Theorem F(e) | "(q + 1 − 2q^{1/2})^g ≤ |A(F_q)| …, an immediate consequence of Weil's inequality" | AHL p. 1 |
| class (B) | Serre's refinement, algebraic integers + Galois stability | HPM §1.2 p. 4 |
| Drinfeld–Vlăduţ via Fejér-type kernels | the asymptotic explicit-formula bound | HP 1409.2357 §2.7 recovers DV "as a bound of infinite order"; the Fejér kernel in Serre's proof `[recalled, unverified]` |
WHAT IS NEW RELATIVE TO OESTERLÉ (10(n)): nothing in the LP — it is Oesterlé's program, and its dual is HP19's Hodge-index SDP.
The transport adds only readings of printed identities: the positions-side Fejér defect on q^Z is AHL's (11) (D_k = h(q^{g−1+k} − 1),
V-blind), and its RH form is Weil's class-number window. Brief stop line 2 fires ("the best inequality is a known Oesterlé/Serre
bound … the unit is 'found nothing, correctly' unless the transport adds something"); the transport adds no inequality.
