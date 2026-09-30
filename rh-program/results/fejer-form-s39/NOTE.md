# NOTE — unit `fejer-form-s39`: the Fejér defect as a positive form transported to the zeros (Untried UT-4)

Session 39, 2026-10-01. Writer: Opus 5.5 (unit agent). Brief: `BRIEF.md` (SHA-256 35542ee1…). Written in order as results
land; §0 is filled at the close. Conventions as in the record: (P) proved here; (C) computed in `verify/` with its log;
(Q) quoted at the page from `sources/` or an on-disk source; `[recalled, unverified]` carries no load.

## 0. CLOSE — K (theorem; §7 Theorem K). Found nothing new, correctly (10(o)).

THE INEQUALITY EXISTS ON RUNG 1, AND IT IS WEIL POSITIVITY WITH MULTIPLIER 1; THE LITERAL FEJÉR TRANSPORT IS V-BLIND; THE Z-FORMS
SPLIT THE SAME WAY. Precisely (q = 5, 7, 11, g ≤ 2 computed exactly; (i)–(iii) proved for every q, g):
(i) I(Z) = Σ_j (1 − cos θ_j) = g − (q + 1 − N_1)/(2√q) is affine in the positive zeta data, vanishes at genus 0, is > 0 on every
    genuine curve of genus ≥ 1 (q not a square), has genus-1 defect 2sin²(θ/2), and separates: V −0.11803, E₀ +0.10557. The same
    Toeplitz family separates EVERY one of the 3825 RH-false data at q = 5, 7, 11, g ≤ 2 (the 111 included) by degree ≤ 3, and every
    genuine curve (all of them, by brute force: 9/11/13 elliptic traces, 115 and 192 genus-2 L-polynomials) satisfies all of it.
(ii) Theorem W: every functional affine in (g, N_1..N_M) vanishing at genus 0 IS the zeros-side Weil functional Σ_j f(θ_j),
    identically on every zeta datum; the separating ones are the Toeplitz cone = Hallouin–Perret's Hodge-index Gram cone on X × X;
    the optimum is Oesterlé's program, whose dual is HP19's SDP — all printed (§5). The best separator of V is Weil's lower bound
    N_1 ≥ q + 1 − 2g√q, and as a quadratic form in the angle it is proof-mine's norm form m² + tmn + qn² (−1 at (2, −1)). IV.1.
(iii) Theorem F: M1a's Fejér defect on q^Z is D_k = h(q^{g−1+k} − 1) (AHL Lemma 3.4): equality exactly at genus 0, genus-1 form
    (q − 1)[(√q − 1)² + 2√q(1 − cos θ)] — affine in (i)'s form — but > 0 on every zeta datum (V: 4). Positive for free because its
    positivity is dN ≥ 0: I.9. V sits at h = 1, the extreme point of free positivity, strictly below the RH floor (√5 − 1)² = 1.528.
(iv) Z side (§6): Z1 = M1a's (C_Q) is an identity passed by F_{2.9,2} (2.95 = 2.95), F_{5,5}, Epstein x² + 5y² (1.139355 vs
    1.139353); Z2 = the real-axis product is passed by F_{2.9,2}, DH, Epstein — both RH-blind; Z3 = the zeros form is violated by
    F_{2.9,2} (−872.45) and DH (−681.66; complete zero list, argument principle 47.0000) and vacuous on ζ's 10 142 zeros below 10⁴
    (+0.0069) — it is Weil's criterion.
WHY (the zoo entries): positive-for-free and RH-sensitive are split exactly between the Fejér defect's POSITIONS form and its ZEROS
form, and the explicit formula maps one to the other; the first fails I.9, the second is IV.1 (III.20(B)'s Gram positivity on
X × X). Proof-mine's Theorem P(iii) says why no third option exists on rung 1: an inequality provable from the zeta datum alone holds
on V; a separator must come from an object — and every such object's output, read on the datum, is a member of this Weil family
(§5: Bombieri's twisted (5) is 4sin²(rθ/2) plus slack, recovering proof-mine's 41 = 41 at Q = 25). The one non-free positions
inequality (class-summed Clifford N_1 ≤ h, an Abel–Jacobi fact) does not see V or any of the 111 (§7).
Stop lines of the brief: line 1 did NOT fire (the genuine region never contains a virtual datum); line 2 FIRED (the best inequality
is a known Oesterlé/Serre bound; the transport adds no inequality); line 3 FIRED on Z1 and Z2 (RH-false controls pass).
Consequences: UT-4 CLOSED (K); wave-1's "Extremal characterization of ξ" answered at its first rung (C2 Untried line 168: the
extremal inequality exists on rung 1 and is IV.1). Instruments rows §8; Untried §9; waste line §10; zoo riders proposed §11.
Deliverables: `verify/` (r1_enumerate, r1_genuine, r1_lp, r1_lp_check, r1_V_detail, r1_transport, r1_clifford, z_forms,
z3_weil_fejer — each .py with its .log), `sources/` (Howe–Lauter 1202.6308, Hallouin–Perret 1409.2357, Aubry–Haloui–Lachaud
1201.4967, Hallouin–Moustrou–Perret 2506.05212, Odlyzko zeros1; text layers; `fetch_sources.log` with SHA-256 prefixes).

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

## 6. The Z side: the three Z-forms of the Fejér defect, on ζ and on the RH-false controls — (C) + (P)

The rung-1 split of §4 has three Z-analogs; each was run on ζ and on the controls (`verify/z_forms.{py,log}`,
`verify/z3_weil_fejer.{py,log}`; mpmath at 30 and 20 digits; every completed function checked against its FE, residual ≤ 1.3·10⁻³⁰).
Z1 — POSITIONS form (M1a's Fejér identity at conductor Q, Theorem C's (C_Q)). F_{a,q} = ζ(s)(1 + aq^{−s} + q^{1−2s}) at Q = q²:
  by Poisson, Σ_{n≥1} S(n/q²) = (q² − 1)/2, Σ S(m/q) = (q − 1)/2, Σ S(m) = 0, so both sides equal (q − 1)(q + 1 + a)/q FOR EVERY a
  (P). Computed: F_{2.9,2} (RH-FALSE, zeros at Re s = 0.8238766802): 2.950000000 = 2.950000000 (direct sum to 2·10⁶ + tail:
  2.950000203); F_{5,5} (RH-false): 8.8 = 8.8; F_{2,2} (RH-true): 2.5 = 2.5. Epstein x² + 5y², the same identity in dimension 2
  (disk of radius ½ in the gap of Z + √5iZ): defect Σ_{w ∈ L*∖0}|1̂_B(w)|² = 1.139355 against Poisson's √5π/4 − π²/16 = 1.139353.
  DH is odd: a positive-definite test with φ̂ ≥ 0 cannot be odd, so DH has no positive Fejér defect, and the pairing identity
  itself holds by its exact theta relation. VERDICT: passed by every RH-false control. Z1 is RH-BLIND — it is an identity of the FE.
Z2 — PRODUCT/LOG transport (the Z-analog of Theorem F(e), the class-number window): E_F(½ + x) ≥ E_F(½) for real x, E_F the entire
  completion (2ξ for ζ). Under RH every factor |½ + x − ρ|/|ρ − ½| ≥ 1; a factor < 1 needs |Im ρ| small against the offset, i.e.
  REAL zeros — the V-world, empty over Z (proof-mine Z1(b)). Computed on [½, 2]: E is monotone increasing for ζ, F_{2.9,2}, DH,
  and Epstein x² + 5y² (min of E(½ + x) − E(½) is 0, attained at x = 0). For F_{2.9,2} this is a theorem: E = 2√2·ξ(s)·H(s),
  H(½ + x) = 2cosh(x log 2) + 2.9/√2 > 0 increasing, and ξ(½ + x) is increasing since ξ(½ + z) = ∫Φ(u)cosh(zu)du with Φ > 0
  `[recalled, unverified: the positivity of Pólya's kernel Φ]`. VERDICT: passed by all three RH-false controls — RH-blind
  to non-real zeros, exactly as the rung-1 class-number test is blind to genus-2 pairs (§4: 194 of 199 RH-false data pass it).
Z3 — ZEROS form (the transported Fejér kernel as a Weil test): g_T(x) = 2(1 − |x|/L)₊cos(Tx), L = 20, W(T) = Σ_ρ ĝ_T(γ_ρ).
  ζ, Odlyzko's 10 142 zeros below 10⁴ (`sources/odlyzko-zeros1.txt`): min over T ∈ [0, 10⁴) of W = +0.0069 — vacuous, every
  term ≥ 0 because every γ is real. F_{2.9,2} (zeros closed-form): min W = −872.45 at T = 13.80 (the factor zeros at
  t = 3·4.5324). DH: all 47 zeros in 50 < t < 120 (43 on the line by sign changes; 4 off it — 0.808517 + 85.699348i and
  0.650830 + 114.163343i with their mirrors 1 − β + iγ, by findroot; the argument principle on the half-rectangle gives 47.0000): min W = −681.66
  at T = 85.49, of which the off-line pair contributes −681.87 and the 43 on-line zeros +0.21 (zeros outside the window move W by
  ≤ 0.03). VERDICT: violated by the controls — RH-SENSITIVE — and it is Weil's explicit-formula functional with a positive-definite
  test, multiplier 1: IV.1 by definition (the Z-form of §3's Theorem W).
So the Z side reproduces the rung-1 split exactly: the positions forms (Z1, Z2) are positive or identical for free and blind; the
zeros form (Z3) sees off-line zeros and is Weil's criterion. No Z-form of the Fejér defect is both RH-sensitive and outside IV.1.

## 7. One more positions-side candidate — geometric, not free (construct-or-refute) — and the close theorem

The only positions-side inequality on q^Z that is neither free nor a Weil test is class-summed Clifford: ℓ(D) ≤ deg D/2 + 1 for
0 ≤ deg D ≤ 2g − 2 gives Θ_n ≤ h·q^{⌊n/2⌋+1}. At g = 1 it is the identity N_1 = h; at g = 2 its only non-identity case is n = 1,
N_1 ≤ h (C(F_q) → Pic¹ is injective for g ≥ 1 and Pic¹(F_q) has h elements — `[recalled, standard; not load]`), and in the angles
h − N_1 = (q − x_1)(q − x_2) + q (x_j = 2√q cos θ_j; identity checked on all data) — a PRODUCT form, not Σ_j f(θ_j).
Computed (`verify/r1_clifford.{py,log}`): it holds on every genuine curve (q = 5, 7), is violated by 0 of the 199 RH-false genus-2
data at q = 5 (so by none of the 111, nor V₂), by 1 of 675 at q = 7 ((a1, a2) = (−4, −15): N_1 = 4 > h = 3, a trace x = 2 + √33 > q)
and by 2 of 2935 at q = 11. So a non-Weil, non-free positions inequality exists, and its generator is an object (Pic¹ and the
Abel–Jacobi map — proof-mine's class D) that V lacks; but it only sees traces beyond q, is an identity at g = 1, and V passes it.
REFUTED as a separator of V; recorded as the one exception to "positions forms are free" (it is free of RH, not of geometry).

THEOREM K (the close; q = 5, 7, 11, g ≤ 2 computed; (i)–(iii) for every q and g).
(i) (the inequality exists.) I(Z) := Σ_j (1 − cos θ_j) = g − (q + 1 − N_1)/(2√q) ≥ 0 — the M = 1 twisted Fejér form — is affine
    in the positive zeta data, vanishes at genus 0, is > 0 on every genuine curve of genus ≥ 1 over F_q for q not a square (Weil;
    for square q the Weil-minimal curves give 0), has genus-1 defect 2sin²(θ/2), is violated by V (−0.11803) and satisfied by E₀
    (+0.10557); and every one of the 3825 RH-false data at q = 5, 7, 11, g ≤ 2 (the 111 among them) violates a member of the same
    Toeplitz family of degree ≤ 3, while every genuine curve satisfies all of them.
(ii) (but it is Weil positivity with multiplier 1.) Every functional affine in (g, N_1, …, N_M) vanishing at genus 0 is identically
    Σ_j f(θ_j) (Theorem W(i)); the separating ones are exactly the Toeplitz cone = the Hodge-index Gram cone of the Frobenius graphs on
    X × X (HP 1409.2357 (5)); the optimum is Oesterlé's program (Howe–Lauter p. 2) and its dual is HP19's SDP (HPM p. 4). IV.1.
(iii) (the literal transport is V-blind.) M1a's Fejér defect on q^Z is D_k = h(q^{g−1+k} − 1) (Theorem F; AHL Lemma 3.4): equality
    exactly at genus 0, genus-1 form (q − 1)[(√q − 1)² + 2√q(1 − cos θ)] in the angle — but D_k > 0 on every zeta datum, V
    included (D_1(V) = 4): positive for free because its positivity is dN ≥ 0. I.9. Its RH form is Weil's class-number window
    (two Weil tests after the log; IV.1), and the one non-free positions inequality (Clifford) does not see V.
(iv) (the Z-forms.) Z1 (M1a's (C_Q)) and Z2 (the real-axis product) are passed by F_{2.9,2}, DH and Epstein x² + 5y² — RH-blind;
    Z3 (the zeros form) is violated by F_{2.9,2} and DH and is Weil's criterion — IV.1.
Hence the Fejér defect is not a positivity generator outside Weil's cone, on rung 1 or on Z: its POSITIONS form is positive for
free and blind, its ZEROS form is RH-sensitive and is Weil's functional, and the explicit formula maps one to the other (affinely
at g = 1, Theorem F(c)). Proof: (i) §3 and §2's logs; (ii) Theorem W and §5; (iii) Theorem F and §7's Clifford paragraph; (iv) §6. ∎

## 8. Instruments rows (the column shape of `directions/C2-rigidity-conservation.md` line 99: | Quantity | Current best value | Result file | Dated |; records, never ranks; not inserted by this unit)

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| Rung-1 exit degree from the Weil (Toeplitz / Hodge-index Gram) region, RH-false zeta data, q = 5, 7, 11, g ≤ 2 | every one of 3825 exits by M ≤ 3 (g = 1: M = 1; q = 5, g = 2: M = 2 for 113, M = 3 for 86); every RH-true datum PSD to M = 8 (worst −6·10⁻¹⁵) | `results/fejer-form-s39/verify/r1_lp.log` | 2026-10-01 |
| V's least Toeplitz eigenvalue λ_min(T_M(V)) (closed form (M + 1) − (Σφ^{2k}·Σφ^{−2k})^{1/2}) | −0.2361 at M = 1 (= 2 × Weil's lower-bound defect 1 − √5/2 = −0.11803); −1, −2.708, −6, −11.889, −22, −38.957, −67 at M = 2..8 | `results/fejer-form-s39/verify/r1_V_detail.log` | 2026-10-01 |
| Positions-side Fejér defect on q^Z, D_k = h(q^{g−1+k} − 1) (M1a's Step 1 on rung 1) | > 0 on all 4591 zeta data including all 3825 RH-false (V: D_1 = 4) — V-blind; = 0 exactly at genus 0 | `results/fejer-form-s39/verify/r1_transport.log` | 2026-10-01 |
| Class-number window (√q − 1)^{2g} ≤ h ≤ (√q + 1)^{2g} (two Weil tests after the log), catch rate on RH-false data | g = 1: all (16/16); g = 2: 5/199 (q = 5), 47/675 (q = 7), 416/2935 (q = 11) | `results/fejer-form-s39/verify/r1_transport.log` | 2026-10-01 |
| Class-summed Clifford N_1 ≤ h at g = 2 (non-free, non-Weil positions inequality) catch rate | 0/199 (q = 5; none of the 111), 1/675 (q = 7), 2/2935 (q = 11); identity at g = 1 (V passes) | `results/fejer-form-s39/verify/r1_clifford.log` | 2026-10-01 |
| Z3: zeros-side Weil–Fejér form, g_T = 2(1 − \|x\|/L)₊cos(Tx), L = 20 | ζ (10 142 Odlyzko zeros < 10⁴): min +0.0069 (vacuous); F_{2.9,2}: −872.45 at T = 13.80; DH (47 zeros in (50, 120), argument principle 47.0000): −681.66 at T = 85.49 | `results/fejer-form-s39/verify/z3_weil_fejer.log` | 2026-10-01 |
| Z1: M1a's (C_Q) on RH-false controls | F_{2.9,2}: 2.95 = 2.95 (exact for every a, by Poisson); F_{5,5}: 8.8 = 8.8; Epstein x² + 5y² 2-D defect 1.139355 vs 1.139353 | `results/fejer-form-s39/verify/z_forms.log` | 2026-10-01 |
| ↳ provenance | the rung-1 LP is Oesterlé's program (Howe–Lauter 1202.6308 p. 2); its dual is Hallouin–Perret's Hodge-index Toeplitz SDP (HPM 2506.05212 p. 4, citing HP19) | `results/fejer-form-s39/NOTE.md` §5 | 2026-10-01 |

## 9. Untried (the directions' "Untried" format; S1–S5 as in STATUS; nothing here is claimed)

- **Z3 on Epstein x² + 5y²** (NOTE §6). Fit: none of S1–S5 (Z3 is Weil's criterion; a violation would only confirm it). First rung:
  locate the first off-line Epstein zero (Potter–Titchmarsh-type search) and evaluate W(T) there. Target: C2 (controls). Low value.
- **A non-free positions inequality at g ≥ 3** (NOTE §7: class-summed Clifford is the only one found, and at g = 2 it sees only
  traces beyond q). Fit: S4 would need it to separate V-type data (real off-line pairs with SMALL h) — Clifford-type bounds are
  upper bounds on Θ_n and cannot, by the one-sided caveat (digest B4; V has the smallest possible A_n, P¹'s shifted); S1 through h ≥ 1.
  First rung: enumerate g = 3 zeta data at q = 5 and test Θ_n ≤ h·q^{⌊n/2⌋+1}, n = 1, 2, and the Castelnuovo/Martens refinements.
  Target: C2. Expected: refutes (recorded so the next unit does not re-derive it).
- **HP19 at the page** (Trans. AMS 372 (2019) 5409–5451; cited here through HPM p. 4). Fit: none (prior-art hygiene for Theorem
  W(ii)'s duality sentence). First rung: fetch (Firecrawl if walled) and read the duality theorem at the line. Target: C2.
- Closed by this unit: **UT-4** (digest §F.3) — K (NOTE §0); and, as its concrete instance, wave-1's **"Extremal characterization of
  ξ"** at its first rung (C2 Untried line 168: "the virtual curve (5, 5) must fail it and a genuine curve with |a| ≤ 2√5 must pass"):
  the extremal inequality exists on rung 1 (Theorem K(i)) and is Weil positivity (K(ii)). The Z-level variational problem was not
  posed; nothing on rung 1 suggests one outside IV.1.

## 10. The waste line (KICKSTART 10(o), with 10(m)'s three labels)

Found nothing, correctly (not waste): the rung-1 LP — it is Oesterlé's program, whose dual is HP19's Hodge-index SDP (brief stop line
2 fired: "a known Oesterlé/Serre bound"); the transport — AHL's Lemma 3.4 read as M1a's Fejér pairing (V-blind); the Z-forms — Z1
and Z2 passed by every RH-false control, Z3 is Weil's criterion (its run on ζ was vacuous, as predicted: every term ≥ 0).
Spent on the wrong thing: one recalled arXiv ID (1207.6230) was a physics paper — fetched, detected by its title, deleted, replaced
by an API search (1201.4967); cost one request. Label (iii) none: every slip is explained in the log where it happened — the first
r1_genuine run's JSON int64 error, the first z_forms run's evaluation at the pole s = 1 (grid moved off it), the spurious BLAS
matmul warnings in r1_lp (re-checked without BLAS: `verify/r1_lp_check.log`, 890/890 unchanged), two NOTE slips fixed in place
(an AHL line citation; a count 18 → 16).
(ii) budget / tool / time — re-queued with the missing input named: HP19 not fetched (Trans. AMS; §9); Serre's 2020 book (the
explicit formula and the Drinfeld–Vlăduţ proof) not on disk — read through Howe–Lauter and HPM at the page instead, and the
Fejér-kernel form of DV's proof left `[recalled, unverified]`; Epstein's off-line zeros not located, so Z3 was not run on it (§9).
Candidate LOG line: "fejer-form-s39 (UT-4): K. The inequality exists on rung 1 (Σ_j 2sin²(θ_j/2), V −0.118, E₀ +0.106, all 3825
RH-false data at q = 5, 7, 11, g ≤ 2 separated by degree ≤ 3) but is Weil positivity with multiplier 1 (Oesterlé's program; dual =
HP19's Hodge-index SDP); the literal Fejér transport D_k = h(q^{g−1+k} − 1) is V-blind; Z1/Z2 passed by F_{2.9,2}, DH, Epstein;
Z3 = Weil's criterion. Found nothing, correctly; one wrong recalled arXiv ID (cost one fetch)."

## 11. Proposed zoo riders (BLOCK format of `results/zoo-s26/zoo-entries-proposed.md`; NOT inserted — for the next zoo stream)

<!-- BLOCK:iv1 -->
- **[RIDER 2026-10-01, Session 39 (`results/fejer-form-s39/NOTE.md` §3, §5) — on rung 1 this entry is a theorem, and its dual is in print.]** Every functional affine in (g, N_1, …, N_M) that vanishes at genus 0 equals, identically on every zeta datum over F_q (virtual ones included), the zero-side Weil functional Σ_j f(θ_j), f = c_0 + 2Σ c_n cos nθ (Serre's explicit formula read as an identity); the inequalities of this shape that separate a datum from the RH-true data are exactly the Toeplitz cone, which is Hallouin–Perret's Hodge-index Gram cone of the Frobenius graphs on X × X (arXiv:1409.2357 p. 7 eq. (5)); the LP optimum is Oesterlé's ("the best bound … that can be obtained formally using only Weil's 'Riemann hypothesis' for curves and the fact that for every d ≥ 0 the number of degree-d places on a curve is non-negative", Howe–Lauter arXiv:1202.6308 p. 2), and its dual is HP19's SDP (Hallouin–Moustrou–Perret arXiv:2506.05212 p. 4). So "an LP over positive zeta data on rung 1" passes this entry's EXECUTABLE TEST with multiplier 1 before any generator is proposed. Computed: all 3825 RH-false zeta data at q = 5, 7, 11, g ≤ 2 leave the Toeplitz region by degree 3; V's best test is f = 2sin²(θ/2), Weil's lower bound, value −0.11803. `[novelty: single-check for the packaging; every piece printed]`
<!-- END:iv1 -->

<!-- BLOCK:i9 -->
- **[RIDER 2026-10-01, Session 39 (`results/fejer-form-s39/NOTE.md` §4, §6, §7) — positive forms in the POSITIONS of the generalized integers are V-blind.]** M1a's Fejér defect, carried exactly to the norm group q^Z (class-summed Riemann–Roch; the box of degree −k as the Fejér test), is D_k = h(q^{g−1+k} − 1) — Aubry–Haloui–Lachaud's Lemma 3.4 (11) (arXiv:1201.4967 p. 14) — with equality exactly at genus 0 and genus-1 form (q − 1)[(√q − 1)² + 2√q(1 − cos θ)]; it is > 0 on every zeta datum, V included (D_1(V) = 4): "positive for free" (insights digest s37 B7) because its positivity is dN ≥ 0, which V has. Its Z-forms are passed by the RH-false controls (M1a's (C_Q) on F_{2.9,2}: 2.95 = 2.95 for every a; the real-axis product on F_{2.9,2}, DH, Epstein x² + 5y²). KILLS: briefs claiming a positivity generator from a positive form in the positions of the generalized integers; RETURNS such a form to its zeros side, where it is a Weil test (IV.1 rider of this date). The one non-free positions inequality found (class-summed Clifford, N_1 ≤ h at g = 2) sees only traces beyond q (0 of 199 RH-false data at q = 5) and is an identity at g = 1. `[novelty: single-check]`
<!-- END:i9 -->
