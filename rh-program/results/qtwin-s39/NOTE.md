# NOTE — unit `qtwin-s39`: the last corner of Q_cond — weighted, clustering Beurling systems with Riemann's exact FE at q > 1

Session 39, 2026-10-01. Writer: Opus 5.5 (unit agent). Status: IN PROGRESS — built section by section; §0 carries the close.
Conventions (as in `qcond-s38/NOTE.md`, cited "QC", and `novel-wave-s37/beurling-fe/NOTE.md`, cited "BFE"): every load-bearing
claim is (P) proved here, (C) computed in `verify/` with its log, or (Q) quoted from a file on disk at the line.
`[recalled, unverified]` carries no load. Novelty: `[novelty: single-check]`. Distance-from-upstream lines (10(n)) marked "UPSTREAM".

## 0. The question, the record, the digest (close stated in §0.4 once reached)

### 0.1 Setting (QC §1.1; BFE §3, §8(b))
dN ≥ 0 on [1, ∞) of polynomial growth, F(s) = ∫x^{−s}dN(x), Λ_F(s) = (q/π)^{s/2}Γ(s/2)F(s), and (A): Λ_F(s) = Λ_F(1 − s), poles
only at 0 and 1 (simple), growth (G′). Beurling: dN = exp*(dΠ), dΠ ≥ 0 on (1, ∞) (weights allowed, atoms and continuous part
allowed), so dN({1}) = 1. Scaled: ν := image of dN under t ↦ t/√q, r := q^{−1/2}, ρ_q := √q·Res_{s=1}F, and
μ_q := ρ_qδ₀ + ν + ν^∨ is a positive, even, tempered measure with μ̂_q = μ_q and μ_q|_{(−r,r)} = ρ_qδ₀ (QC §1.1).
Q_cond (the corner this unit owns): is there such a system at some q > 1?

### 0.2 The record (Q, QC at the line)
- QC Theorem U_q (§2.4, 218–238): u.d. generalized integers + (A) at any q ⟹ q = 1 and ζ (weights allowed).
- QC Theorem L′ (§2.3, 196–211): ζ·D, D a non-constant finite generalized Dirichlet polynomial, is never Beurling with (A), any q.
- QC Cor. E2 (§2.2, 175–182): ∫u^{−1}dΠ_c ≤ log ρ_q; no purely continuous solution at any conductor.
- QC §2.6(c) (297): "WEIGHTED or MIXED systems whose atom masses take infinitely many values: Meyer's theorem does not apply;
  only (a) is known." QC §2.6(d) (298–302), the SHAPE of a surviving solution: "an infinite atomic prime set whose generalized
  integers cluster (pairs arbitrarily close), with c ≤ ρ_q, a thin continuous part, and — if discrete and Q4 holds — integers
  spread over ≥ 2 radical classes and a decomposition F = Σ_ψ P̃_ψL_ψ with at least two primitive characters".
- QC Theorem D (§2.7, 322–335): every DISCRETE system with (A) at any q is ζ, conditional on Meyer's finite-values theorem (Q4),
  which QC had only second-hand. The primary is now on disk: `fetched-r9/r9-05-meyer-1970-LNM117.ocr.txt`, scan page 25 (§1 below).
- BFE Theorem T (§4, 104–133): conductor 1, dN ≥ 0 ⟹ ρζ. BFE T′ (§12, 340–347): two-system version. BFE §8(a) (206–213): continuous
  RH-false systems with double poles at a, 1 − a. BFE §11(iii) (333–336): the Euler-side inequalities (QC Prop. E makes them
  identities). read-O R1 (`beurling-fe/read-O.md` 204–219): the SIGNED self-dual solution at conductor 1 with a zero at
  1.32691 + 33.26351i — positivity is the rigidifying input.

### 0.3 The digest, quoted (Q: `novel-wave-s37/insights-digest.md`, SHA-256 e86f642a…)
§B5 (lines 151–154): "An RH-false object with Riemann's exact Γ-factor exists once any one hypothesis of Theorem T is dropped —
positivity (the signed R1 solution), the pole structure (continuous systems with double poles at a, 1 − a), frequencies ≥ 1
(Nakamura's f(s, χ)), or conductor 1 (F_{5,5}) — and the only drop not yet paid WITH Λ ≥ 0 and a discrete system is conductor
q > 1 (Q_cond; discrete systems with extra poles are the other open case, fe §8(d))."
§B6 (lines 158–160): "The Q-side location of the virtual curve is conductor q > 1, not conductor 1: over F_q the completed zeta's
'conductor' q^{2g−2} is minimal and rigid at g = 0 (Liouville) and V (g = 1) sits one step above; over Q the minimal conductor 1
is rigid (Theorem C) and T forbids a twin there."
§F.2 item 1 (lines 352–357): "**U2 — Q_cond** … Contract clause: 'a Beurling system (dΠ ≥ 0) with Riemann's exact FE at some
q > 1, verified by the Fejér test (a new Group-I control — the Q-side twin of V), or a rigidity theorem for every q in [1, Q₀] with
the infeasibility certificate on disk (or for all q)' … Why first: both outcomes are theorems; the construction branch gives the
program's first Q-side control with {Euler product, Λ ≥ 0, exact FE} (B5, B6); the refutation branch extends B1 to every
conductor (then {Euler product, Λ ≥ 0, exact Riemann FE at any conductor} has one model)."
QC answered this for u.d. systems (U_q) and, given Q4, for discrete ones (D); this unit owns the residue, QC §2.6(c).

## 1. Meyer's finite-values theorem at the page, and Theorem D made unconditional

### 1.1 What Meyer prints (Q: `fetched-r9/r9-05-meyer-1970-LNM117.ocr.txt`, scan page 25 = printed p. 25, OCR lines 677–709)
§4.2 (lines 680–707), in the UNIT-MASS case: "Supposons, en effet, qu'il existe une mesure, à valeurs complexes, μ telle que
a) sup_x ∫_x^{x+1} d|μ|(t) < +∞, b) μ̂ = Σ_{λ∈Λ} δ(x − λ)." Then (OCR 690–704, repaired): Λ is closed with every point isolated;
with φ ∈ C^∞_c real, φ(0) = 1, and ψ the rapidly decreasing function whose FT is φ, "grâce à a), la suite des normes (ou
variations totales) des mesures dμ_n = [OCR: "ny(n7lx)au(x)"] est une suite bornée"; μ̂_n(t) = Σ_λ φ(n(t − λ)) → 1_Λ(t) (the normalization that
gives this is dμ_n = n^{−1}ψ(n^{−1}x)dμ(x)); "Il existe
donc une mesure ν portée par le compactifié de Bohr de R dont la transformée de Fourier vaut 1 sur Λ et 0 ailleurs (ν est la
limite vague des μ_n). D'après une conséquence du théorème de Paul Cohen due à P.H. Rosenthal, ([7] th. 1.6 p. 22) Λ est à un
ensemble fini près, la réunion de k parties de R de la forme α_jZ + β_j (1 ≤ j ≤ k)." ([7] = Rosenthal, Thèse, Memoirs AMS; OCR
line 1928.) Page 26, line 713: "On retrouve donc la formule de Poisson habituelle."
So the primary proves the unit-mass case, with a finite exceptional set; QC's secondary quote Q4 (Kurasov–Sarnak: "If aλ take values
in a finite set … then µ is a generalized Dirac comb") is the finitely-valued extension. It is proved here (Lemma M, M1).

### 1.2 LEMMA M (finitely many values) — (P, on top of Meyer p. 25)
Let μ be a complex Radon measure on R with ‖μ‖_TB := sup_x |μ|([x, x+1]) < ∞ whose Fourier transform μ̂ (tempered) is a Radon
measure. Put a(t) := μ̂({t}) and suppose a(R) ⊂ V ∪ {0}, V ⊂ C∖{0} finite. Then for each v ∈ V the level set Λ_v := {a = v} is,
up to a finite set, a finite union of arithmetic progressions α_jZ + β_j.
 Proof. (1) Meyer's step, with μ̂ a general measure: μ_n := n^{−1}ψ(x/n)μ has ‖μ_n‖ ≤ C(ψ)‖μ‖_TB (Riemann sums of |ψ| on the grid
 Z/n), and μ̂_n(t) = ∫φ(n(t − λ))dμ̂(λ) → μ̂({t}) = a(t) for every t (dominated convergence on [t − R, t + R], supp φ ⊂ [−R, R]).
 (2) Push μ_n to the Bohr compactification bR (dual group R_d); a weak-* cluster point ν ∈ M(bR) has ν̂(t) = lim μ̂_n(t) = a(t),
 because each character is continuous on bR and the sequence μ̂_n(t) converges. So a ∈ B(R_d), the Fourier–Stieltjes algebra.
 (3) LAGRANGE. B(R_d) is an algebra under pointwise product (ν̂₁ν̂₂ = (ν₁∗ν₂)^). For v ∈ V put
      P_v(z) := (z/v)·Π_{w∈V∖{v}}(z − w)/(v − w),  so P_v(0) = 0, P_v(v) = 1, P_v(w) = 0 (w ∈ V∖{v}).
 P_v has no constant term, so P_v(a) = Σ_{k≥1}c_k a^k ∈ B(R_d), and P_v(a) = 1_{Λ_v} pointwise: an idempotent, 1_{Λ_v} = ν̂_v.
 (4) Λ_v is closed and discrete: |μ̂|(K) ≥ min_{w∈V}|w|·#(Λ_v ∩ K) for compact K. Meyer's last sentence applies verbatim to Λ_v
 (its two inputs are exactly: a measure on bR with FT 1_Λ, and Λ closed with isolated points). ∎
 UPSTREAM (10(n)): Meyer 1970 p. 25 (unit masses, purely atomic μ̂); the Lagrange step is the standard reduction of finitely
 valued Fourier–Stieltjes transforms to idempotents; Kurasov–Sarnak's quote (u-20b 43–44) states the result. `[single-check]`

### 1.3 COROLLARY M1 (no exceptional points when μ is purely atomic) — (P)
If in addition μ is purely atomic, then μ̂ = Σ_{j≤J} κ_j δ_{β_j+α_jZ} exactly (finite, κ_j ∈ C): no finite correction survives.
 Proof. By Lemma M and inclusion–exclusion (a finite intersection of progressions is a progression, one point, or empty),
 μ̂ = C + e with C a finite combination of progression combs and e = Σ_{t∈E} e_tδ_t, E finite. Invert: FT(δ_{β+αZ}) is pure point
 (Poisson), FT(δ_t) is the function e^{−2πitx} (absolutely continuous). μ is purely atomic, so the a.c. density Σ_t e_t e^{−2πitx}
 vanishes identically, and by independence of characters every e_t = 0. ∎
 Sanity check (the three level sets of a Poisson pair π_a, a² ∉ Q: masses 1 + 1/a at 0, 1 on aZ∖0, 1/a on Z/a∖0): the corrections
 at 0 are (1 + 1/a) − 1 − 1/a = 0, as M1 requires.

### 1.4 THEOREM D, now unconditional — (P)
Every DISCRETE Beurling system (multiset of reals > 1, integer multiplicities) whose Λ_F satisfies (A) at some conductor q > 0 is
the set of rational primes, and q = 1.
 Proof. QC §2.7 with its only unproved input Q4 replaced: μ_q is purely atomic, positive and self-dual, hence translation bounded
 (QC Lemma TB); its masses lie in {1, ρ_q} (QC Cor. E3). Lemma M + M1 give μ_q = μ̂_q = Σ_j κ_jδ_{β_j+α_jZ}, a generalized Dirac comb
 with CONSTANT weights — a special case of the form Σ_j g_jσ_j used in QC §2.7 step (1). Steps (2)–(6) of QC §2.7 (finite group of
 radical classes, periodic coefficients per class, Saias–Weingartner Thm 1, Lemma S–W′, Theorem L′, BFE Theorem T) are unchanged. ∎
 STATUS. QC §2.6(b)'s conditional clause and QC §5's "T given one printed theorem on disk only second-hand" are discharged.

## 2. Route (i), finitely many lattices: THEOREM G1 — finite generalized Dirac combs with ANY weights are rigid (P)

THEOREM G1. Let dN = exp*(dΠ), dΠ ≥ 0 (weights allowed), satisfy (A) at some q > 0, and suppose μ_q is a finite generalized Dirac
comb, μ_q = Σ_{j≤J} g_jσ_j with σ_j = Σ_{n∈Z}δ_{y_j+α_jn} and g_j trigonometric polynomials (the masses may take infinitely many
values). Then q = 1 and F = ζ.
 Proof. Step 0. μ_q is pure point, so dN = Σ_{x∈𝒩}c(x)δ_x with c > 0 on 𝒩 := supp dN; 𝒩 ∋ 1 is a multiplicative monoid (exp*(tΠ),
 t > 0, all have the same atoms, and dN∗dN = exp*(2Π) has an atom at xy of mass ≥ c(x)c(y)). 𝒩 is infinite (F has a pole).
 Step 1 (finitely many radical classes). 𝒩/√q ⊂ ∪_j(y_j + α_jZ). QC §2.4 Step 2 verbatim (an infinite A ⊂ 𝒩 in one coset; for
 x ∈ 𝒩, xA ⊂ 𝒩 puts two points xa, xa′ in one coset) gives x ∈ (α_i/α_j)Q: the classes [x] ∈ R_{>0}/Q_{>0}, x ∈ 𝒩, form a finite
 submonoid of a group, hence a finite group Γ; fix representatives β_γ (β_γ^{|Γ|} ∈ Q).
 Step 2 (merge). Group the lattices by commensurability; in a group take α with every α_jZ ⊂ αZ. Each y_j + α_jZ lies in one coset
 of αZ, where its weight n ↦ g_j(y_j + αn)·1[n ≡ n_j mod α_j/α] is a trigonometric polynomial in n. Summing, μ_q = Σ_C W_Cδ_C over
 finitely many cosets C = y_C + α_CZ, W_C(n) = Σ_θ b_{C,θ}e^{2πiθn} (finite; θ mod 1), cosets of one refined lattice disjoint, cosets
 from different groups meeting in ≤ 1 point. Hence μ_q({y_C + α_Cn}) = W_C(n) for all but finitely many n.
 Call C RATIONAL if √q·y_C and √q·α_C lie in one set β_γQ. A non-rational C meets each set ±β_γQ/√q in at most one point (two
 points force both √qα_C and √qy_C into that set), so it carries ≤ 2|Γ| + 1 points of supp μ_q: W_C(n) = 0 for all but finitely
 many n, hence W_C ≡ 0 (Bohr–Parseval: the mean of |W_C|² over [N, N + M] tends to Σ_θ|b_{C,θ}|²). Drop them.
 Step 3 (irrational frequencies cancel — the Fourier side). Split μ_q = ω_R + ω_I, ω_I := Σ_{C rational}Σ_{θ∉Q}b_{C,θ}e^{2πiθn}δ_C.
 Poisson: FT(Σ_n e^{2πiθn}δ_{y+αn}) is carried by the coset (θ + Z)/α. For θ ∈ Q that coset lies in the set α^{−1}Q; for θ ∉ Q it
 meets every set βQ in at most one point ((θ+m)/α, (θ+m′)/α ∈ βQ with m ≠ m′ force θ ∈ Q). Now μ̂_q = μ_q is carried by
 {0} ∪ ∪_γ(±β_γQ/√q), and ω̂_R by finitely many sets α_C^{−1}Q; so ω̂_I = μ̂_q − ω̂_R is carried by the intersection of a finite
 union of sets βQ with finitely many irrational cosets — a FINITE set E. Then ω_I is absolutely continuous (density
 Σ_{t∈E}e_te^{2πitx}) and pure point at once: ω_I = 0. So μ_q = ω_R: every surviving weight is PERIODIC along its coset.
 Step 4 (periodic coefficients per class). Rational cosets of class γ lie in β_γD^{−1}Z/√q for one D ∈ N, and cosets of different
 classes meet only at 0; so c(β_γn/D) = a_γ(n) with a_γ periodic, and F(s) = Σ_{γ∈Γ}(β_γ/D)^{−s}G_γ(s), G_γ = Σ_{n≥1}a_γ(n)n^{−s}.
 This is exactly the output of QC §2.7 step (3); its steps (4)–(6) (Saias–Weingartner Thm 1, Lemma S–W′ with F ≠ 0 on Re s > 1,
 the pole at 1 making the character trivial, Theorem L′, BFE Theorem T) give F = ζ and q = 1. ∎
COROLLARY G1′ (finitely many mass values). A purely atomic Beurling system (weights allowed) with (A) at some q whose atom masses
take finitely many distinct values is ζ. (Lemma M + M1 make μ_q a finite generalized Dirac comb with constant weights; G1.)
WHERE THE HYPOTHESES ENTER. Positivity of Π: the monoid (Step 0/1) and F ≠ 0 on Re s > 1 (QC step 5). Self-duality: Step 3 (the
only place the FT is used) and, through L′, the FE. Finiteness of the comb: Step 1 (finitely many cosets) and Step 2 (finitely many
frequencies). Integrality of masses: nowhere. `[novelty: single-check]`
CONTROLS (the theorem must fail exactly where the hypotheses fail; `verify/v2_controls_G1.{py,log}`): F_{5,5} = π_{1/5} + (5/2)π_1 is a
positive finite comb with (A) at q = 25 — Steps 0–4 go through (𝒩 = N is a monoid, one class, periodic weights) and it is excluded
only at QC step (6)/L′, i.e. by Π(25) = −7 < 0; Davenport–Heilbronn (q = 5, complex periodic weights) and read-O R1 (signed, q = 1)
fail Step 0 (no positive measure, no monoid) — G1 says nothing about them, as it must not.

## 3. Rung 1 first — the weighted mechanism, and the rung-1 image of each design route (C: `verify/v1_rung1_weighted.{py,log}`)

Over F₅, genus 1, L(u) = 1 − tu + 5u² with t REAL (weights: b_d ≥ 0 real, no integrality). Rigorous root isolation (arb balls)
of the integer polynomials d·b_d(t), d ≤ 60:
 (W1) weighted Beurling over F₅ ⟺ t ∈ [−5, 6] exactly (the lower end is b₂(−5) = 0; t = 6 is the empty system Z ≡ 1). Weights add
      nothing to the integer answer {−5, …, 6}: the admissible set is its convex hull.
 (W2) RH-FALSE part: t ∈ [−5, −2√5) ∪ (2√5, 6] — a whole interval of RH-false weighted systems at rung 1.
 (W3) Q-side q-part positivity of the transplant ζ(s)L(5^{−s}) (QC §3 D4: s_n ≤ 1 ∀n): s₁ ≤ 1 ⟺ t ≤ 1; s₂ ≤ 1 ⟺ |t| ≤ √11;
      s₃ ≤ 1 ⟺ t ∈ (−∞, −3.8392] ∪ [−0.0667, 3.9059]; s₄ ≤ 1 ⟺ |t| ∈ [1.6907, 4.1402]. The intersection is EMPTY: Theorem L′'s
      obstruction holds at rung 1 for every real t, weights allowed — a four-line exact certificate.
 (W4) positive Poisson mixtures at rung 1 = L with nonnegative coefficients ⟺ t ≤ 0; with (W1): t ∈ [−5, 0].
THE RUNG-1 IMAGE OF EACH DESIGN ROUTE (P, dictionary of QC §3 D1–D5):
 (i) Poisson mixtures ζ·D, D J-symmetric (J: b ↦ q/b, weight √q/b). Rung-1 image: Z_{P¹}(u)·D(u) with D(1/(qu)) = q^{−g}u^{−2g}D(u),
     i.e. an L-polynomial; frequencies q^k, 0 ≤ k ≤ 2g — always FINITELY many, in a rank-1 group. Infinite mixtures have no image.
 (ii) cut-and-project (model-set) measures need an archimedean internal space; over F_q((1/T)) every window is compact open and
     every model set is a finite union of lattice cosets: the image is degenerate (finite combs = (i)).
 (iii) continuous prime measures: none over F_q (degrees are integers).
READING (the calibration). The rung-1 mechanism that makes RH-false twins is ONE thing: the pole of the base zeta, at u = 1/q, lives
in the same local variable u as the zeros of L and absorbs them (W1 ∋ t = −5 while W3 = ∅). On the Q side a multiplier D is
supported on the monoid of its own frequencies; the pole of ζ is visible there only through the Euler factors at the rational primes
S that occur in that monoid. QC's Theorem L′ is the case S finite (no pole visible). §4 below shows the obstruction persists while
Σ_{p∈S}p^{−σ} < ∞ for some σ < ½, and that it disappears exactly when the rational part of the frequency group involves a prime
set of abscissa σ_S ≥ ½ — the only Q-side place where the rung-1 mechanism could be imitated, and one with NO rung-1 image
(over F_q the frequency group is q^Z, rank 1).

## 4. Route (i), infinitely many lattices: the Poisson-mixture cone and THEOREM L‴ (thin rational part) — (P)

SETTING. F = ζ·D with D(s) = ∫_{[1,Q]}b^{−s}dm(b), m a finite real measure on a BOUNDED range (atoms and continuous part allowed,
infinitely many atoms allowed). Every μ_q in QC's closed cone 𝒦_r = {∫π_a dm̃(a)} is of this form (QC §1.2(a): D = ∫(b^{−s} +
√q b^{−1}(q/b)^{−s})dm̃(b), b ∈ [1, q]), so this is route (i) with a continuum of lattices.
LEMMA A (atomic reduction). If such F is a Beurling system with (A) at q, then so is F_a := ζ·D_a, D_a := ∫b^{−s}dm_a (m_a the
atomic part of m), and Π_{F_a} = the atomic part of Π_F.
 Proof. dN({1}) = m({1}) = 1. For σ ≥ σ₀, ‖m − δ₁‖_{σ} := ∫_{(1,Q]}b^{−σ}d|m| < ½ (dominated convergence), and ‖·‖_σ is a Banach-
 algebra norm for multiplicative convolution; so log*(m) = Σ_j(−1)^{j+1}(m − δ₁)^{*j}/j converges, and Π_F = Π_ζ + log*(m). Write
 m = m_a∗(δ₁ + κ), κ := m_a^{*−1}∗m_c continuous (a convolution with a continuous measure has no atoms). Then log*(m) = log*(m_a) +
 log*(δ₁ + κ): the first term is atomic, the second continuous (norm limits preserve both classes). Hence (Π_F)_atomic =
 Π_ζ + log*(m_a) ≥ 0: F_a is Beurling. (A) for F: dividing Λ_F = q^{s/2}ξ(s)D(s) by ξ(s) = ξ(1 − s) gives D(1 − s) = q^{s−½}D(s); by
 uniqueness of Fourier–Stieltjes transforms this says m is invariant under J (the map b ↦ q/b with density √q/b), and J maps atoms
 to atoms: D_a(1 − s) = q^{s−½}D_a(s), and Λ_{F_a} = q^{s/2}ξ(s)D_a(s) satisfies (A) (D_a entire, bounded in vertical strips). ∎
THEOREM L‴ (bounded-frequency multipliers with thin rational part). Let F = ζ·D be as in the setting, Beurling, with (A) at some q > 0.
Let Γ be the group generated by the atoms of m, S the set of rational primes dividing some element of Γ ∩ Q_{>0}, and σ_S the
abscissa of convergence of Σ_{p∈S}p^{−s} (σ_S := −∞ if S is finite). If σ_S < ½, then q = 1 and F = ζ.
 Proof. By Lemma A work with F_a. Let B be the atom set of m_a, G the monoid generated by B ∪ S. (1) G meets the prime powers only in
 {p^k : p ∈ S} (QC L′(2): p^k = γs, γ ∈ ⟨B⟩, s ∈ ⟨S⟩ ⟹ γ ∈ Γ ∩ Q). (2) log*(m_a) is carried by ⟨B⟩ ⊂ G, so the restriction of
 Π_{F_a} ≥ 0 to G is log*(m_a) + Σ_{p∈S}Σ_k δ_{p^k}/k, whose transform is log h, h(s) := D_a(s)Π_{p∈S}(1 − p^{−s})^{−1}, analytic on
 Re s > σ* := max(σ_S, 0). (3) Landau–Widder (a Laplace–Stieltjes transform of a positive measure is singular at the real point of
 its abscissa σ_a; no local finiteness is needed): if σ_a > σ*, then either D_a(σ_a) ≠ 0 and log h continues analytically across σ_a,
 or D_a(σ_a) = 0 and h(σ) → 0 as σ ↓ σ_a although h(σ) = e^{(positive)} ≥ 1 for σ > σ_a. Both are impossible, so σ_a ≤ σ* and
 D_a = e^{series}·Π_S(1 − p^{−s}) ≠ 0 on Re s > σ*. (4) The FE gives D_a ≠ 0 on Re s < 1 − σ*. Since σ* < ½ the two half-planes cover
 C; D_a is entire of order ≤ 1 (|D_a(s)| ≤ ‖m_a‖·max(1, Q^{−σ})), so D_a = e^{α+βs}, m_a is one atom, m_a = δ₁, D_a ≡ 1, and the FE
 forces q = 1. BFE Theorem T: F = ζ. ∎
COVERAGE. S finite (Γ ∩ Q_{>0} finitely generated): QC's L′ is the case "m finite atomic"; L‴ adds countably many atoms, continuous
parts, any irrational frequencies. Hence EVERY positive self-dual measure in the closed Poisson-pair cone 𝒦_r whose atoms generate a
group with thin rational part (σ_S < ½) — e.g. all atoms in a finitely generated group, or in {b : b transcendental over Q(b₀)}·Q_S
with S finite — is excluded at every conductor. `[novelty: single-check]` UPSTREAM: Landau 1905 / Widder, The Laplace Transform,
Thm II.5b `[recalled, standard]`; QC Theorem L′.
THE RESIDUE OF ROUTE (i) (named): (R-i-1) Poisson-pair mixtures whose atoms generate a group with THICK rational part, σ_S ≥ ½
(e.g. atoms at b_p = (p + 1)/p for all primes p, weights summable): the Landau obstruction proves D_a zero-free only on Re s > σ_S,
which no longer reaches past the critical line; the pole of ζ becomes visible on the monoid of D's frequencies through infinitely
many Euler factors. This is exactly the Q-side imitation of the rung-1 mechanism (§3 READING). Finite truncations of such m are all
infeasible (L′), but Π(x) depends on every atom once x ≥ q, so truncation certificates say nothing about the infinite mixture.
(R-i-2) mixtures that also contain infinitely many twisted combs Σχ(n)δ_{n/√m} (F = ζ·D + Σ_χ E_χL(s, χ) with infinitely many χ):
Saias–Weingartner's two-character theorem (QC Lemma S–W′) needs finitely many characters.

## 5. Route (ii): cut-and-project (Pisot model-set) measures — exact reduction, acceptance test, and why the route stays open

### 5.1 The exact reduction (P; C: `verify/v3_pisot_model_set.{py,log}`)
K = Q(√5), O_K = Z[φ], σ: √5 ↦ −√5, c := 5^{1/4}. The lattice {(x/c, x^σ/c) : x ∈ O_K} ⊂ R² has covolume 1 and (trace form) dual
{(z/c, −z^σ/c)}; Poisson summation for g ⊗ k gives, for μ_k := Σ_{x∈O_K}k(x^σ/c)δ_{x/c}:
      μ̂_k = μ_{k̂}   (Fourier transform on R; k even),   so μ_k is EXACTLY self-dual iff k̂ = k.
Every even Hermite combination k = Σ_m a_m h_{4m} (eigenvalue 1) passes. Acceptance test on k = e^{−πt²} (v3 Part A): theta pairing
equal to 2.7e−51 at y = 0.37, 1, 2.2 (whole lattice, terms < 1e−60 dropped); Fejér pairing at L = 0.3, 0.7, 1.3 equal within the
explicit ξ^{−2} tail bound (diff 8.4e−4 / 3.6e−4 / 2.0e−4 against bounds 1.8e−3 / 7.6e−4 / 4.1e−4). These measures are positive, pure
point, with DENSE support and infinitely many mass values — exactly QC §2.6(d)'s shape — and they are not generalized Dirac combs.
GAP AND MONOID. Put the atom "1" at x₁ = φ^{−j} (a unit, so the generalized integers n = x/x₁ = xφ^j form a sub-monoid of O_K):
q = √5·φ^{2j} (2.236, 5.854, 15.33, 40.12 for j = 0..3), 𝒩 ⊂ O_K ∩ [1, ∞), c(n) = K_j(n^σ) with K_j(t) := k(tφ^j/c). The gap
(−r, r) is EQUIVALENT to k = 0 on the cut-and-project set
      Z_j := {n^σφ^j/c : n ∈ O_K, 0 < |n| < 1}   (uniformly discrete, relatively dense, density 2/(cφ^j) per unit length),
first points (v3 Part C) j = 0: ±1.0820, ±1.7508, ±2.8328, …; j = 1: ±1.7508, ±2.8328, ±4.5836, …. For k = e^{−πt²} the gap fails
(v3 Part B: largest masses inside (0, r): 2.5e−2 (j = 0), 6.6e−5 (j = 1), 1.1e−11 (j = 2), 2.2e−29 (j = 3)).
PROPOSITION P1 (finite Hermite expansions are excluded exactly). If k = P(t)e^{−πt²} with P a polynomial (every finite Hermite
combination), k has finitely many zeros, while Z_j is infinite: no member of the finite-dimensional exactly-self-dual families has the
gap, at any q = √5φ^{2j}. (P; one line.)
PROPOSITION P2 (Fourier uniqueness does NOT close the route) (Q: `sources/arxiv-2306.14013-kulikov-nazarov-sodin.txt`, Definition 2
lines 101–118, Theorem 1(ii) lines 137–139): a pair (Λ, M) with lim inf_{|j|→∞}|λ_j|^{p−1}(λ_{j+1} − λ_j) > ½ and the same for M (1/p + 1/q = 1)
is a NON-uniqueness pair for S. Z_j is uniformly discrete, so (Z_j, Z_j) is subcritical for every p > 1: there are f ∈ S∖{0} with
f|_{Z_j} = f̂|_{Z_j} = 0. The zero conditions alone therefore do not force k = 0; positivity (k ≥ 0, double zeros) and the Euler
condition remain. [A density-product heuristic considered while writing — "uniqueness when q < 4" — is WRONG for S and is retracted.]

### 5.2 The Euler condition in route (ii) (C: `verify/v3d_pisot_beurling_probe.{py,log}`; P for the mechanism)
Probe on k = e^{−πt²} normalized so that c(1) = 1 (not admissible — it violates the gap — but it shows the multiplicative test):
 j = 0 (q = √5, ρ = 4.08): first Π < 0 at n = 4/φ = 2.4721 (Π = −2.5e−8), from 4/φ = 2·(2/φ) with c(2)c(2/φ) = 2.5e−8 ≫ c(4/φ) =
   1.1e−25; 150 negative values in [1, 60], worst Π(6 + 9φ) = −0.215.
 j ≥ 1: the UNIT ORBIT already fails: Π(φ²) = c(φ²) − c(φ)²/2 = −24.0 (j = 1), −7.0e4 (j = 2), −1.7e13 (j = 3).
MECHANISM (P). (a) Along the units, c(φ^m) = k(φ^{j−m}/c)/k(φ^j/c) rises from 1 to ρ = k(0)/k(φ^j/c); the orbit {φ^m} is a divisor-
closed submonoid, so Σ_m c(φ^m)u^m = exp(Σ π_m u^m) with π_m ≥ 0 — e.g. Π(φ²) ≥ 0 ⟺ 2c(φ²) ≥ c(φ)²; for a Gaussian this fails as
soon as e^{πφ^{2j−2}/√5} > 2, i.e. for every j ≥ 1. (b) For n = n₁n₂ with c(n) tiny and c(n₁)c(n₂) not, Π(n) < 0 at first order; a
weight decaying faster than every power of |t| makes K_j(t₁t₂) ≪ K_j(t₁)K_j(t₂) once |t₁|, |t₂| > 1. So an admissible k must decay at
most polynomially along the multiplicative structure — hence (k̂ = k) k cannot be smooth — AND vanish on Z_j, AND rise gradually
along the unit orbit. Positive self-dual k with polynomial decay exist (k = e^{−2π|t|} + 1/(π(1 + t²)): FT pairs, sum self-dual,
decay 1/(πt²)); whether one of them also vanishes on Z_j is the open harmonic-analysis core of route (ii).
VERDICT route (ii): no member of any finite-dimensional exactly-self-dual family has the gap (P1); the zero conditions are not
contradictory (P2); the Gaussian member fails the Euler condition on the unit orbit (j ≥ 1) and on 4/φ (j = 0). The route survives
only in an infinite-dimensional, non-smooth class — named in §0.4 as part of the residue.

## 6. Route (iii) and mixed systems: the FE SPLITS for ζ-divisible solutions — Proposition S and Theorem L‴ in general form (P)

Write m := dN ∗ μ_Möb (μ_Möb = Σμ(n)δ_n), so F = ζ·D, D(s) = ∫x^{−s}dm — always true formally; the question is where D converges.
PROPOSITION S (splitting). Let F be a Beurling solution with (A) at q, and suppose ∫x^{−σ₀}d|m| < ∞ for some σ₀ < ½. Then the
atomic part m_a satisfies the FE by itself, D_a(1 − s) = q^{s−½}D_a(s); D_a is entire of order ≤ 1; and F_a := ζ·D_a is a Beurling
solution of (A) at q with Π_{F_a} = (Π_F)_atomic.
 Proof. On Re s = ½ all four transforms D_a(s), D_a(1−s), D_c(s), D_c(1−s) converge absolutely (∫x^{−½}d|m| < ∞), and
 E(t) := D_a(½−it) − q^{it}D_a(½+it) = q^{it}D_c(½+it) − D_c(½−it). The left side is a uniformly almost periodic function of t
 (absolutely convergent generalized Dirichlet series); the right side is a combination of Fourier–Stieltjes transforms of the
 CONTINUOUS finite measures x^{−½}m_c (in the variable log x), whose quadratic means vanish (Wiener: lim (2T)^{−1}∫_{−T}^{T}|ν̂|² =
 Σ|atoms of ν|² = 0). So M(|E|²) = 0, every Bohr coefficient of E vanishes, E ≡ 0, and the FE of D_a holds on the line, hence on the
 strip σ₀ < σ < 1 − σ₀ where D_a converges; the FE then continues D_a to C, bounded in vertical strips and O(q^{|σ|}). The log*
 decomposition of Lemma A (§4) holds verbatim (‖m − δ₁‖_σ → 0 as σ → ∞ by dominated convergence), so (Π_F)_atomic = Π_ζ + log*(m_a)
 ≥ 0. ∎
THEOREM L‴ (general form). Let F be a Beurling solution with (A) at q. If (i) ∫x^{−σ₀}d|m| < ∞ for some σ₀ < ½ ("F is ζ-divisible
beyond the critical line") and (ii) the rational primes S occurring in the group generated by the atoms of m have σ_S < ½, then
q = 1 and F = ζ.  Proof. Proposition S, then §4 steps (1)–(4) verbatim for F_a (Landau–Widder needs no local finiteness; D_a entire of
order ≤ 1 by Prop. S), then BFE Theorem T. ∎   (§4's bounded-frequency case is σ₀ = −∞.)
ROUTE (iii) — VERDICT (P). (a) The continuous systems of BFE §8(a) buy positivity with double poles at a, 1 − a; (A) forbids them, and
E2 caps any continuous prime mass by log ρ_q, so the pole at 1 must be carried by atoms. (b) The exact-FE repairs of a continuous
head are not lost in general position: the conductor-q FE for F = ζ·G is G(1 − s) = q^{s−½}G(s), whose rational-times-exponential
solutions G = R(s) + q^{½−s}R(1 − s) have poles at the poles of R and at their mirrors; (A) allows them only at zeros of ζ. Example
(the "zeta-zero repair"): R(s) = 1 + Σ_ρ c_ρ/(s − ρ) over finitely many nontrivial zeros, c_ρ̄ = c̄_ρ. Then F = ζ·G satisfies (A)
EXACTLY (ζ(s)/(s − ρ) is entire; ζ(s)R(1 − s) likewise, 1 − ρ being a zero), and m = δ₁ + √qδ_q + Σ_ρ c_ρ[x^{ρ−1}1_{[1,∞)} −
q^{ρ−½}x^{−ρ}1_{[q,∞)}]dx: a positive-looking head plus oscillating densities ≍ x^{−½}. A direct computation shows the continuous part
G_c = Σ_ρ c_ρ[(s − ρ)^{−1} − √q q^{−s}(s − 1 + ρ)^{−1}] satisfies the FE BY ITSELF (q^{s−½}G_c(s) = G_c(1 − s), term by term), so
the atomic part 1 + √q q^{−s} must satisfy it alone — the case of Prop. S — and (Π_F)_atomic = Π_ζ + log*(δ₁ + √qδ_q) has the mass
Π_ζ(q²) − q/2 < 0 at q². More atoms in m_a lead back to L‴. So route (iii) produces no exact solution outside the residue of §4.
COVERAGE OF L‴ (general). All of route (i) with thin rational part, continuous parts included; every zeta-zero repair whose atomic
part is thin; every solution whose quotient F/ζ converges absolutely to the left of ½ with thin atoms. What it CANNOT see: solutions
with F/ζ not absolutely convergent beyond ½ (F does not contain ζ: Davenport–Heilbronn-like twisted combinations, model sets), and
the thick case.
