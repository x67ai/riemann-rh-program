# M2 `proof-mine` — the virtual-curve line in every proof of RH for curves (novel-approach wave 2, Session 37)

Agent: Opus 5.5 (seed M2). Started 2026-09-30. Charter: `../WAVE-CHARTER.md`, section "Seed M2 `proof-mine`".
Status: CLOSED T (2026-09-30). Sections were appended as they were finished; §0 is the summary.

**The object.** The virtual curve V = (q, a) = (5, 5): Z_V(u) = (1 − 5u + 5u²)/((1 − u)(1 − 5u)) over F₅, reciprocal roots
α, β = (5 ± √5)/2 (α = 3.618 > √5 = 2.236), zeros at Re s = 0.79899, 0.20101. It has rationality, the functional equation,
N_n ≥ 1 and b_d ≥ 0 integers, a standard Euler product, class number 1, Riemann–Roch-consistent divisor counts — and RH false.
**The control.** A genuine elliptic curve E₀/F₅ with trace a = 4 (same q, same g = 1), exhibited and counted in `verify/`.

**Method (per proof).** (i) the chain of steps, read at the page (`sources/`); (ii) the FIRST step V cannot supply, as a lemma
"the proof uses X; V has no X because Y"; (iii) wherever possible, the numerical line: the inequality the proof derives that V's
formal data violate, with the exact place (the extension degree, the divisor, the endomorphism); (iv) the control E₀ passes it.

## §0 Verdict

**CLOSE: T** — Theorem P (§4) and the table (§2). 14 rows: 12 proofs read at the page (Hasse; Weil's Jacobian/Rosati; Weil's
correspondences; Mattuck–Tate–Grothendieck; Bombieri–Stepanov; Deligne Weil I; Weil II via Laumon; Kedlaya's p-adic proof; Davenport–Hasse/
Weil 1949; CCM; Hrushovski; the automorphic check), 2 named-not-read. Each proof separates curves from V at one input: **A surface**
(def(Γ_π − 2Δ) = −2, formal index (2, 2)), **B family** (Weil I (7.1) on C × C: α² = 13.090 > q^{3/2} = 11.180), **C coordinates**
(Bombieri §III: V's twist has 41 points over F₂₅ against (7) ≤ 40), **D group** (deg(π − 2) = −1, Rosati trace −2). E₀: y² = x³ + 2x over F₅
passes every line. For g = 1 the A/D numbers are one binary form m² + tmn + qn²: the form is zeta-level, its positivity is RH.
Over Z (§3): A, B, D dead on the record; C is the one class not dead — its twist half exists and is unnecessary over Z (ζ(σ) < 0 on (0, 1),
so one-sided RH suffices, Z1); its Frobenius and finite-support Chebyshev forms are killed here (Z2; Lemma Z4: κ > 1); left alive: the
integer-polynomial auxiliary object (Gelfond–Schnirelman–Nair–Chudnovsky–Pritsker), open in print even at PNT strength (Pritsker 2013 p. 4).
**Findings for the orchestrator:** (1) tournament T24's G-line is wrong at the page (Bombieri 1973 p. 239: towers do not upgrade Stepanov's
bound; twists do) — verdict DEAD unaffected; (2) V sharpens Bombieri's printed RH-false example (ω₁ = q, ω₂ = 1); (3) the rung-1 twin rule
needs a one-sided caveat: V passes every upper bound because its off-line roots are real; the genus-2 twin V₂ = 1 − u + 11u² − 5u³ + 25u⁴
over F₅ (non-real off-line roots, N_n, b_d ≥ 0, h = 31) is caught by Bombieri's Theorem 1 alone at Q = 5⁶.

## §1 Baseline computations (V and the control E₀)

`verify/baseline.py` → `verify/baseline.log` (exact integers; sympy for Möbius and irreducibility; brute force in F_{5ⁿ}).

- **V.** N_1..N_8 = 1, 11, 76, 451, 2501, 13376, 70001, 361251; b_1..b_8 = 1, 5, 25, 110, 500, 2215, 10000, 45100; min N_n = min b_d = 1
  for n, d ≤ 60. α = 3.618034, β = 1.381966, αβ = 5; zeros at Re s = 0.79899, 0.20101; h = L(1) = 1; A_n = (5ⁿ − 1)/4; FE residual ≤ 9e−16.
  **Structure used below (computed):** α/√5 = φ = (1 + √5)/2 (the golden ratio) and β/√5 = 1/φ, so a_n := αⁿ + βⁿ = 5^{n/2}(φⁿ + φ⁻ⁿ) >
  2·5^{n/2} for EVERY n ≥ 1; and α − 2 = φ, a unit of Z[φ] of norm −1. Z[α] = Z[φ] is the ring of integers of the REAL quadratic field Q(√5).
- **E₀ (the control).** The short Weierstrass curves over F₅ with trace 4 are exactly one: E₀: y² = x³ + 2x (j = 1728), E₀(F₅) = {(0, 0), ∞}.
  Brute-force counts #E₀(F_{5ⁿ}) = 2, 20, 122, 640 (n = 1..4) equal 5ⁿ + 1 − (α₀ⁿ + β₀ⁿ) with α₀ = 2 + i, |α₀|² = 5 (RH true, Re s = ½).
  Its quadratic twist y² = x³ + 3x has 10 points over F₅, and 2 + 10 = 12 = 2(q + 1); over F₂₅ (brute force, `verify/lines.log` L4b)
  #E₀ = 20, #E₀^tw = 32, sum 52 = 2(25 + 1). Q[π₀] = Q(i), imaginary quadratic.
- **Bombieri's printed precursor of V** (Bourbaki 430, 1973, p. 239, `sources/bombieri-1973-bourbaki430-stepanov.pdf`, read at the page):
  "if ν_r = q^r − ω₁^r − ω₂^r + 1 and ω₁ = q, ω₂ = 1 then (2) [the functional equation] is verified, ν_r is always 0 but (3) [RH] is false."
  That formal object has Z ≡ 1, no points, class number L(1) = 0. V is strictly sharper: N_n ≥ 1, b_d ≥ 1, h = 1, a standard Euler product.
  `[novelty: single-check]` for "V sharpens Bombieri's 1973 example"; nearest published object (10(n)): Bombieri 1973 p. 239.

**The four numbers that recur.** Every positivity proof below, specialized to g = 1, evaluates one of the following on V and on E₀
(`verify/lines.py` → `verify/lines.log`):

| quantity (source of the inequality) | V (q, t) = (5, 5) | E₀ (5, 4) |
|---|---|---|
| formal degree deg(π − 2) = (α − 2)(β − 2) (Hasse: deg ≥ 0) | **−1** | 1 |
| def(Γ_π − 2Δ) = 2d₁d₂ − D² on C × C (Castelnuovo–Severi: ≥ 0) | **−2** | 2 |
| index of the formal intersection form on ⟨C₁, C₂, Δ, Γ_π⟩ (Hodge: one +) | **(2, 2)** | (1, 3) |
| Tr((π − 2)(π − 2)†), π† = q/π (Rosati: > 0) | **−2** | 2 |
| |α|² on H²(C × C) vs q^{3/2} = 11.180 (Weil I (7.1) at X = C × C) | **13.090 > 11.180** | 5 |
| Bombieri (7) bound at Q = 25 (= 40) vs the twist's count 2(Q + 1) − N_2 | **41 > 40** | 32 |

For g = 1 the first four are one binary form: deg(m + nπ) = m² + tmn + qn² = N_{Q(π)/Q}(m + nα), positive definite iff t² < 4q
(Hasse's discriminant; Milne p. 10's def form 2(gm² + amn + gqn²) at g = 1; Rosati's trace 2·deg). V's form has discriminant +5 and
represents −1 at π − 2 = φ. What differs from proof to proof is the OBJECT that makes the form positive — that is the row's line.

## §2 The table — one row per proof

Format: chain (at the page) → the LINE (first step V cannot supply, as a lemma) → the NUMBER (the inequality that step yields, on V) →
the CONTROL (E₀ at the same place). Classes: **A** surface (C × C with an index/positivity theorem), **B** family (a sheaf over a base curve
with monodromy and Rankin squaring), **C** coordinates (the function field itself: functions, Frobenius on functions, covers and twists),
**D** group (an abelian variety: endomorphisms acting on points; polarization). Numbers: `verify/lines.log` block Lk.

**R1. Hasse (1933–36), genus 1 — class D.** Source: Sutherland 18.783 L8, Thm 8.3 (`sources/sutherland-18783-hasse-lecture8.pdf`, p. 1–2).
Chain: (1) E(F_q) = ker(π_E − 1); (2) π_E − 1 separable (Lemma 8.1), so #ker = deg(π_E − 1) = q + 1 − t; (3) deg(rπ_E − s) = r²q − rst + s²
via the dual isogeny (Lemmas 7.14–7.15); (4) "noting that deg(r − π_E s) ≥ 0 … the discriminant t² − 4q cannot be positive".
LINE: step (4). *Lemma R1. The proof uses the endomorphism ring End(E) with deg ψ = #ker ψ · deg_i ψ ≥ 0 on all of Z[π_E]; V has no
End because it has no group of points on which π − 2 could act — its formal degree is the norm form of the real field Q(√5).* V supplies
(1)–(3) formally (N_1 = N(α − 1) = 1). NUMBER (L1): deg(π − 2) = (α − 2)(β − 2) = −1 (π − 2 = φ, a unit of norm −1); the zeta-level degrees
deg(1 − πⁿ) = N_n = 1, 11, 76, … are all positive — the failure is only at mixed elements. CONTROL: 5r² − 4rs + s² = (s − 2r)² + r² ≥ 1.

**R2. Weil 1940/1948b, the Jacobian and the Rosati involution — class D.** Source: Milne pp. 5, 21–23 (Thm 1.27, Cor 1.28–1.29, Thm 1.30,
Summary 1.31), `sources/milne-2015-…txt` lines 296–330, 1180–1300. Chain: J = Jac(C); † from a polarization; Thm 1.27 Tr(αα†) > 0,
proved by Tr(αα†) = (2g/(D^g))(D^{g−1}·α⁻¹(D)) and hyperplane sections ("by dimension theory, the intersection is nonempty"); Thm 1.30
ππ† = q via the Weil pairing e_λ(πx, πy) = q e_λ(x, y); Cor 1.29: † is complex conjugation on R ⊗ Q[π], so |ρ(π)| = q^{1/2}.
LINE: Thm 1.27. V SUPPLIES Thm 1.30's input: on a 2-dimensional V_ℓ any alternating form scales by det π = 5 = q. *Lemma R2. The proof uses
an ample divisor D on an abelian variety carrying π (positivity of (D^{g−1}·α⁻¹D)); V has no abelian variety: its formal Q[π] = Q(√5) is
real quadratic and π† = q/π is its Galois conjugation, whose trace form is indefinite.* NUMBER (L3): Tr((π − 2)(π − 2)†) = −2; Cor 1.29
fails (q/α = 1.382 ≠ ᾱ = 3.618). For g = 1, Tr(αα†) = 2 deg α, so R2 at g = 1 is R1's number. CONTROL: Tr = 2 at π₀ − 2; q/α₀ = ᾱ₀.

**R3. Weil 1941 / 1948a, correspondences and the equivalence defect — class A.** Source: Milne pp. 6, 10–12 (the "trace" σ, (8),
σ(D ∘ D′) = def(D), "Weil's inequality σ(D ∘ D′) ≥ 0 is a restatement of (5)"; the 1948a sketch); CCM §2.3 pp. 9–11 (same proof).
Chain: σ(D) = d₁ + d₂ − (D · Δ); reduce to D effective with d₂(D) = g "using the Riemann–Roch formula on C to show that one can achieve
effectivity" (CCM p. 9); view D as a multivalued map P ↦ {D₁(P), …, D_g(P)}; Φ(P) = det(φ_i(D_j(P))) with {φ_i} a basis of L(K_C) is a
rational function (squared, after a Galois covering of C × C) whose zeros count (Y₂ · Δ) and whose poles number ≤ (2g − 2)d₁(D); hence
σ(D ∘ D′) ≥ 2g d₁(D) ≥ 0; Weil proves σ(ξ ∘ ξ′) > 0 for ξ ≠ 0 (1948a Thm 10, p. 54, via Milne p. 12). LINE: the effective representative and
Φ. *Lemma R3. The proof uses rational functions on C (a basis of L(K_C), the function Φ with deg(zeros) = deg(poles)) and divisors on
C × C; V has neither — it has the NUMBER dim L(K) = g = 1 (Riemann–Roch-consistent counts) but no field of functions to evaluate.*
NUMBER (L2): σ((Γ_π − 2Δ) ∘ (Γ_π − 2Δ)′) = def(Γ_π − 2Δ) = −2. CONTROL: def(mΔ + nΓ_π) = 2(m² + 4mn + 5n²) ≥ 2 on nonzero (m, n).
Variants named by Milne p. 12–13 and NOT read (`[recalled, unverified]`, no load): Igusa 1949, Quigley 1953, Roquette 1953, Kani 1984.

**R4. Mattuck–Tate 1958 and Grothendieck 1958, the Hodge index theorem on C × C — class A.** Source: Milne pp. 8–10 (Lemma 1.1, Thm 1.2,
Cor 1.3–1.4, Thm 1.5, Cor 1.6, Ex. 1.7, the proof of RH), history p. 13. Chain: Riemann–Roch on the SURFACE gives l(mD) + l(K − mD) ≥
(D²/2)m² + …; with Lemma 1.1 (a hyperplane section meets an effective divisor positively) this gives Thm 1.2 (D·H = 0 ⇒ D² ≤ 0),
Cor 1.3 (index one on N(V)); Thm 1.5: D² ≤ 2d₁d₂; Cor 1.6; Ex. 1.7 def(Γ_f) = 2g₂ deg f; hence |(Δ · Γ_π) − q − 1| ≤ 2gq^{1/2}.
LINE: Thm 1.2 / Cor 1.3. *Lemma R4. The proof uses a projective surface V ⊃ Δ, Γ_π with Riemann–Roch and hyperplane sections; V (the
virtual curve) has no surface: the only "N(V × V)" it defines is the Gram matrix of its numbers, which has index 2.* NUMBER (L2): on
⟨C₁, C₂, Δ, Γ_π⟩ (and on ⟨C₁, C₂, Γ_{π⁰..π³}⟩, rank 4) the formal form has (+, −) = (2, 2); Thm 1.5 fails at D = Γ_π − 2Δ (def −2);
Cor 1.6 fails: |1 − 6| = 5 > 2√5 = 4.472; on span(Δ, Γ_{πⁿ}) it fails at every n = 1..6 (a_n > 2·5^{n/2}). CONTROL: (1, 3); 4 ≤ 4.472.

**R5. Stepanov 1969 (hyperelliptic; Kummer and Artin–Schreier covers of P¹), Schmidt (general curves) — class C.** Source: Bombieri p. 234–235
(at the page: "Stepanov himself proved (3) in special cases, e.g. if C was a Kummer or an Artin–Schreier covering of P¹, and a proof in
the general case has been also obtained by W. Schmidt"; the idea: a rational function f vanishing at every k-rational point to order ≥ m,
so m(ν₁ − m₀) ≤ #zeros = #poles; "they consider derivatives or hyperderivatives of f, of order up to m − 1"). Stepanov 1969 and Schmidt
are NOT read (`[recalled, unverified]`), so this row carries no verdict of its own: its line is R6's, with C → P¹ itself Galois (a Kummer
cover) so that C′ = C in R6's §III and the twists are y^n = c·f(x). NUMBER: R6's. CONTROL: R6's (E₀ → P¹ by x is the Kummer cover y² = f(x)).

**R6. Bombieri 1973, the Riemann–Roch form of Stepanov — class C.** Source: Bourbaki 430 pp. 234–241, read at the page (text layer and
page images). Chain: Theorem 1 (p. 236): q = p^α, α even, q > (g + 1)⁴ ⇒ "(5) ν₁ < q + (2g + 1)q^{1/2} + 1", from R_m = functions with
poles only at x₀ of order ≤ m, dimension counts from Riemann–Roch on C ((i)–(iii)), "(iv) R_m ∘ φ ⊆ R_{mq}", "(v) every element f ∘ φ of
R_m ∘ φ is a q-th power", the Lemma (injectivity of R_ℓ^{(p^μ)} ⊗ (R_m ∘ φ) → R_ℓ^{(p^μ)}(R_m ∘ φ) for ℓp^μ < q), the kernel of δ giving a
function vanishing to order ≥ p^μ at every fixed point, and (7) ν₁ ≤ ℓ + mq/p^μ + 1 (p. 239). §III (p. 239): "The argument given before
does not give a lower bound for ν₁, while this is needed if we want to deduce the Riemann hypothesis" (with the ω₁ = q, ω₂ = 1 example);
"The function field k̄(C) … contains a purely transcendental subfield k̄(t) such that k̄(C) is a separable extension of k̄(t). Hence there
is a normal extension …": C′ → C → P¹, C′ → P¹ Galois with group G; for each η ∈ G, (8) ν₁(C′, η) ≤ q + (2g′ + 1)q^{1/2} + 1 "arguing as
before, but using δ_η" (p. 240); (9) Σ_η ν₁(C′, η) = |G|ν₁(P¹) + O(1); hence (10) ν₁(C′, η) = q + O(q^{1/2}) and ν₁(C) = q + O(q^{1/2}).
LINE: §III, the separable t and the twists. Theorem 1 NEVER separates: V's own counts satisfy (5) and (7) at every admissible even r,
because a_r > 0 forces N_r < 5^r + 1 (L4). *Lemma R6. The proof uses a separable function t ∈ k̄(C), the Galois closure C′ → P¹ and, for
each η ∈ G, the auxiliary-function argument run on η ∘ φ (functions of C′, their q-th powers); V has no function field, hence no t, no G,
no twisted Frobenius η ∘ φ.* For g = 1 the cover is x: E → P¹ with G = {1, ι}, and (9) forces the twisted count ν₁(C, ι) = 2(Q + 1) − ν₁(C)
(= deg(π + 1)). NUMBER (L4): V's formal twist over F₂₅ has 2·26 − 11 = 41 points: (5) requires < 41 and (7) (μ = 1, m = 7, ℓ = 4,
hypotheses checked) gives ≤ 40 — violated at the FIRST admissible field Q = 5²; (8) as printed (≤ 41) is violated at Q = 5⁴ (801 > 701)
and Q = 5⁶ (17876 > 16001); the lower bound ν₁(V) ≥ 2(Q + 1) − (7) fails at Q = 25 (11 < 12), 625 (451 < 562), 15625 (13376 < 15312).
CONTROL: E₀'s twist has 32 (F₂₅), 612 (F₆₂₅), 15392 (F_{5⁶}) points, all ≤ (7); brute force at F₂₅ (L4b): 20 + 32 = 52 = 2(25 + 1).
**Correction to the record (for the orchestrator):** tournament row T24 describes the rung-1 mechanism as "the tower over F_{qⁿ}
upgrades the bound to RH"; Bombieri p. 239 says the opposite (the upper bound on the tower never gives RH: his example, and V), and the
upgrade is the twist step (9)–(10). T24's verdict (DEAD) is untouched; its G-line should read "upper bounds for all twists of a Galois
cover ⇒ lower bound ⇒ RH".

**R7. Deligne 1974, Weil I (Lefschetz pencils, monodromy, Rankin squaring) — class B.** Source: Publ. IHES 43, read at the page:
Thm (1.6), Lemme (1.7) pp. 276–277; §3 pp. 283–287 (Thm 3.2, Lemmes 3.3–3.6, (3.7), Cor 3.8–3.9); §7 pp. 298–301 (Lemmes 7.1, 7.2, (7.3)).
Chain for a curve C (the route (7.3) takes, d = 1): "Pour tout entier k, α^k est valeur propre de F* agissant sur H^{kd}(X^k)" (Künneth);
for k even X^k = C^k has even dimension and Lemma (7.1) gives q^{kd/2 − 1/2} ≤ |α|^k ≤ q^{kd/2 + 1/2}; k → ∞. Lemma (7.1) is proved by
induction through a Lefschetz pencil (5.7) on X, whose vanishing-cycle sheaf over U ⊂ P¹ satisfies Thm 3.2's hypotheses: (i) an alternating
form ψ, (ii) the image of π₁(U) open in Sp (Kazhdan–Margulis 5.10), (iii) rational characteristic polynomials det(1 − F_x t) at every closed
point x; then (3.3)–(3.4) positivity of the local factors of ⊗^{2k}, (3.7) poles of Z(U₀, ⊗^{2k}) only at |t| = q^{−(kβ+1)} (H. Weyl's
invariants of Sp), (3.6) radius comparison: |α|^{2k} ≤ q^{kβ+1}. LINE: (7.1) for X = C × C (k = 2). *Lemma R7. The proof uses a smooth
projective variety of even dimension containing H¹(C)^{⊗2} in its middle cohomology (C × C) with a Lefschetz pencil, i.e. a family over an
open curve U with big symplectic monodromy and rational traces at every closed point of U; V has no C × C and no family: it is ONE
conjugacy class at ONE point, with no base whose closed points could amplify the Rankin positivity.* NUMBER (L5): (7.1) at X = C × C
requires 2.236 ≤ |α_iα_j| ≤ 11.180; V gives α² = 13.090 and β² = 1.910 — both sides violated; also at C⁴, C⁶. In the family form (V as
the fiber at a rational point of a weight-1 system with (i)–(iii)), Thm 3.2's inequality holds at 2k = 2 (13.09 ≤ 25) and first fails at
2k = 4 (171.35 > 125). CONTROL: |α₀|² = 5 ∈ [2.236, 11.180]; 5^k ≤ 5^{k+1} for every k.

**R8. Deligne 1980 (Weil II) via Laumon 1987 (the ℓ-adic Fourier transform); Katz's lectures — class B.** Source: Laumon, Publ. IHES 65,
read at the page: intro p. 133–134 ("les ingrédients essentiels de cette preuve sont la transformation de Fourier-Deligne (et son
involutivité) et le critère de pureté dégagé par Deligne"), Thm (4.1.3) and Cor (4.1.3.1) p. 204, (4.2.1.3) p. 205, (4.2.2.1),
Cor (4.3.1.1) and Prop (4.3.2.1) p. 206. Deligne 1980 and Katz's lectures NOT read (`[recalled, unverified]`, no load). Chain for a curve
C = X, U = X, F = Q_ℓ (pure of weight 0): (4.3.2.1) "On peut supposer X = D en projetant j_*F sur D à l'aide d'une fonction" (D = P¹);
(4.3.1.1) for a lisse, irreducible, non-geometrically-constant F on U ⊂ A¹: |ι(α)| ≤ q^{(w+1)/2} on H¹_c(A ⊗ k, j_!F), proved through the
Fourier transform (a sheaf on the dual line: a FAMILY of twists by L_ψ(tx)) and the purity criterion (4.2.1.3) "les sous-quotients lisses
irréductibles de tout Q̄_ℓ-faisceau lisse ι-réel sur une courbe … sont ι-purs" (Deligne's Rankin argument, Weil II (1.5.1)).
LINE: (4.3.2.1)'s function, then the Fourier family. *Lemma R8. The proof uses a nonconstant function C → P¹ (to push Q_ℓ to a lisse sheaf
on U ⊂ A¹) and the Fourier-transform family over the dual line, made pure by Rankin squaring over its base; V has neither a function nor a
sheaf, so it has no family.* NUMBER (L6): for g = 1, H¹_c(A, j_!F) ⊇ H¹(E) (F the Kummer sheaf of y² = f(x), w = 0), and (4.3.1.1) gives
|α| ≤ q^{1/2} = 2.236; V has α = 3.618 (formal weights 1.598 and 0.402 against 1). No intermediate inequality of Laumon's chain is exhibited
on V: the row's number is the conclusion of (4.3.1.1), honestly labeled so. CONTROL: |α₀| = 2.236 (equality), weights 1, 1.

**R9. Kedlaya 2006, p-adic Weil II (rigid cohomology); Dwork 1960 checked — class B.** Source: Kedlaya, Compositio 142, arXiv
math/0210149v3, read at the page: abstract ("a transcription into rigid (p-adic) cohomology of Laumon's proof of Deligne's 'Weil II'
theorem … This yields a complete, purely p-adic proof of the Weil conjectures when combined with recent results on p-adic differential
equations"), §1.3 p. 5 (determinantal weights; "global monodromy"; "Deligne's analogue of the Rankin squaring trick"), §1.4 p. 7
("the Rankin–Selberg method only gives this result on a curve"). So a complete p-adic proof of RH for curves IS in print, and it is R8's
proof transcribed: same class, same line (a function to P¹, the Fourier family, Rankin squaring), same number. **Dwork:** Kedlaya p. 2
calls Dwork [Dw1] "the first proof of the rationality of the zeta function of a variety" — RATIONALITY, which V HAS; Dwork's method is not a
proof of RH and does not separate V (a proof V passes would have to be reported at once; this is not one: its conclusion is true of V).

**R10. Davenport–Hasse 1935, Weil 1949: diagonal (Fermat-type) curves via Gauss and Jacobi sums — class C (special curves).** Source: Milne
p. 23 (at the page: Weil "obtained an expression in terms of Gauss sums for the number of solutions … Using a relation, due to Davenport and
Hasse (1935), between Gauss sums in a finite field and in its extensions"; the zeta function of a diagonal equation is explicit). Weil 1949
itself NOT obtained (BAMS behind a bot wall). Chain: N = Σ over characters χ_i of F_q^× of products of Jacobi sums J(χ₁, …); the reciprocal
roots are ± products of Gauss sums over q; RH ⟸ |g(χ)|² = q (Parseval on the additive group F_q). LINE: the first step. *Lemma R10. The
proof uses the curve's EQUATION (its solutions as a subset of F_q² on which the characters of F_q^× and F_q act — the μ_m-Kummer cover
of P¹ and its twists, R6's object in explicit form); V has no equation, and its α is not a product of Gauss sums: α ∈ R, α² = 13.09 ≠ 5.*
NUMBER (L7): over F₅, |g(χ)|² = 5.000000000000 for the characters of order 2 and 4; the Jacobi sums are ±1 ± 2i, all of norm 5.
CONTROL: E₀'s Frobenius 2 + i is a unit multiple of a Jacobi sum of F₅ (L7: True); V's α is not of absolute value √5 in its real embedding.

**R11. Modular / automorphic methods and CM — checked; no independent proof found in the sources read.** Source: Milne pp. 49, 51, 58–59 at the
page. (a) Weil, Deuring, Eichler–Shimura proved the HASSE–WEIL conjecture (continuation of the global zeta function over a number field)
for CM and modular curves "by expressing their zeta functions in terms of Hecke L-functions" / "by identifying their zeta functions with the
Mellin transforms of modular forms" — statements about Q, not RH over F_q. (b) The Ramanujan conjecture is DEDUCED from the Weil
conjectures through Eichler–Shimura/Verdier (Deligne's interview, Milne p. 49; Rankin's theorem and Langlands' remark, Milne p. 51:
Rankin's idea "could be used to prove a generalized Ramanujan conjecture provided one knew enough about the poles of a certain family of
Dirichlet series"). So modular methods CONSUME RH for curves. (c) For a CM curve over F_q the Frobenius is an element of the CM field with
ππ̄ = q — that is R1/R2's input (End(E) ⊗ Q imaginary quadratic), class D; E₀ is such a curve (Q[π₀] = Q(i)). Standing order V.5:
"none found" is not "none exists"; no verdict rests on it.

**R12. Connes–Consani–Marcolli 2007, the Weil proof on the adèle class space (a translation) — class A.** Source: arXiv math/0703392v1
(= `fetched/y-07`), read at the page: §2.3 pp. 9–11 (Weil positivity "(2.35) Tr(Z ⋆ Z′) > 0 … proved using the Riemann–Roch formula on C to
show that one can achieve effectivity"; for g = 1 "Z ⋆ Z′ = d′(Z)Δ, with Tr(Z ⋆ Z′) = 2d′(Z) ≥ 0"), the dictionary p. 12 ("Riemann–Roch ↔
Index theorem"; "Frobenius correspondence ↔ Z(f) = ∫_{C_K} f(g)Z_g d*g"; "Parts of the dictionary sketched below are very tentative"),
Prop 6.2 p. 29 (RH for all Hecke L-functions of K ⟺ the trace-pairing positivity (6.10)). What it proves: for curves, Weil's proof restated;
for number fields, Weil's criterion restated. LINE and NUMBER: R3's (V has no global field K, so no C_K; the positivity it would need is
def(Γ_π − 2Δ) ≥ 0, and V gives −2). CONTROL: R3's.

**R13. Hrushovski 2004/2022, the elementary theory of the Frobenius automorphisms — class A for curves (consumes RH elsewhere).** Source:
arXiv math/0406514v2, read at the page: p. 3 ("The fundamental fact is Weil's Riemann Hypothesis for curves, entering via the Lang–Weil
estimates"; Theorem 1.1, the twisted Lang–Weil estimate); p. 10 ("§11.4 for a proof for curves: indeed Weil's proof, using positivity in the
intersection product on a surface, works in our case too. For general varieties … we use the cohomological representation and Deligne's
theorem"); Example 11.4 p. 114 (S · Φ_q = q deg_cor(S) + deg_cor(S^t) + e with |e| ≤ ((2g)(2 deg_cor(S) deg_cor(S^t) − |S · S^t|))^{1/2} q^{1/2},
via Weil's bilinear form β). What it proves for curves: Weil's inequality for correspondences S ⊂ C × C^{φ_q}, by Weil's positivity — no new
separating input. NUMBER (L8): S = Δ gives |e| ≤ 2g√q = 4.472; V has e = −5. CONTROL: e = −4.

**R14. Named but not read (no row verdict; `[recalled, unverified]`).** Manin 1956 (elementary proof of Hasse's theorem; recalled to use
E's group law over its function field — class D if so); Igusa 1949, Quigley 1953, Roquette 1953, Kani 1984 (class-A variants, named by Milne
pp. 12–13); Deligne 1980 Weil II itself (class B, represented by R8 at the page); Stark's g = 2 refinement (named by Bombieri p. 234–235,
class C); Stöhr–Voloch-type Frobenius-order bounds (recalled, class C). Fetching any of them is a bounded task; none is expected to open
a fifth class, but that expectation is a guess, labeled as one.

## §3 The separating inputs and their analogs over Z (the program's record)

Status words: EXISTS (an object over Z with the property is on the record or classical), REFUTED (a record theorem kills it), RH-RESTATED
(on the record it is equivalent to RH, so it is not an independent input), UNBUILT (no record entry constructs or kills it).

| class | separating input (the first object V lacks) | analog over Z on the record | status |
|---|---|---|---|
| **A** surface | a surface containing Δ and the Γ_{πⁿ} with an index-one intersection form (Riemann–Roch on the surface + hyperplane sections, R4), or Weil's σ(ξ ∘ ξ′) > 0 (Riemann–Roch on C + rational functions, R3) | the SPEC's target Y: A8, A11, A13 item 2 are MISSING over Z (`results/f1-spec-s29/SPEC.md` §2); zoo IV.20 Theorem R: "NO target … in particular no surface over a field in Weil's form, of any genus, with or without the Hodge index theorem" carries ζ's diagonal row; `results/d4-infty-s36/NOTE.md` Theorem S: under A9⁺ "the lattice form of the Hodge index is dead over Z"; ibid. Proposition C: the smeared index theorem "is Weil's criterion with multiplier 1" | REFUTED (lattice, finite rank) / RH-RESTATED (smeared); CCM's dictionary row "Riemann–Roch ↔ Index theorem" is "very tentative" (CCM p. 12) — its positivity is Prop 6.2 = Weil's criterion |
| **B** family | a sheaf over a base curve U (a Lefschetz pencil on C × C, R7; the Fourier transform of a sheaf on A¹, R8–R9) with big monodromy or ι-reality, rational traces at every closed point, and RATIONAL global L-functions of the tensor powers with poles fixed by invariants | zoo III.20: "Deligne's squeeze additionally needs RATIONALITY … the exact coordinate with no archimedean analog, where the transfer dies"; IV.20 KILLS "Deligne-style rationality (finitely many eigenvalues whose traces are integers …) as available on a square of Spec Z"; III.14 (no real-coefficient Weil cohomology); tournament T21 DEAD, T22 EQUIV (DD3: the needed continuation is RH-equivalent), T23 DEAD ("no amplification"); Milne p. 51 at the page: Langlands — Rankin's idea proves Ramanujan "provided one knew enough about the poles of a certain family of Dirichlet series" (Ramanujan, not RH) | REFUTED (rationality) / RH-RESTATED (squeeze); a base carrying ζ-type fibers is UNBUILT but every priced form of it needs rationality or the square |
| **C** coordinates | (C1) functions with Frobenius acting as the q-th power, Bombieri (iv)–(v): vanishing to order p^μ at every rational point for free; (C2) a separable t, the Galois closure and its twists (Bombieri §III); (C′) an explicit equation with characters (R10) | T24 DEAD at brief time (kills: "primes are not fixed points of an algebraic self-map"; III.4 parity for sieve weights; III.20(A) "the n-th power tower is missing" — premise corrected in R6); SPEC A1: Z's Λ-structure exists. NEW here (`verify/z_side.log`): (C2) EXISTS over Z (Dirichlet/Hecke/Artin twists) and is NOT NEEDED (Z1 below); (C1) holds only to first order over Z (Z2); weak auxiliary integers EXIST (Chebyshev, Z3; Gelfond–Schnirelman–Nair–Chudnovsky, Pritsker 2013 at the page) | C2 EXISTS (vacuous over Z); C1 REFUTED in Frobenius-identity form, EXISTS in weak Chebyshev form, sharp form UNBUILT (and ≡ one-sided RH) |
| **D** group | an abelian variety carrying π: endomorphisms acting on points with deg = #ker ≥ 0 (R1), or an ample divisor making the Rosati involution positive (R2) | SPEC A4 over Z: "End = {id} (R-b′)"; IV.20 Lemma F: "every β with End_β(B) = {id} … fails A9"; IV.10: per-prime Tate curves have End(E_p) = Z, no cross-prime correspondences; positivity of an involution on an algebra containing the Frobenius = Weil positivity (IV.1); for g = 1, D's form is A's restricted to graph classes (Γ_φ · Γ_ψ = deg(φ − ψ)), so D inherits Theorem S | REFUTED (End = {id}) / RH-RESTATED (positivity) |

**Why class C's twist step costs nothing over Z (Z1; proof on the page, `[novelty: single-check]` for the reading only).**
*Lemma Z1.* (a) On rung 1, an upper bound N_r ≤ q^r + 1 + Cq^{r/2} for all r cannot see a reciprocal root α > √q that is REAL POSITIVE
(then a_r > 0 for every r); V is exactly such a world (α = 3.618), and so is Bombieri's printed example. Bombieri therefore needs the twists.
(b) Over Z the corresponding world is a real zero of ζ in (½, 1), and there is none: η(σ) = Σ(−1)^{n−1}n^{−σ} ≥ 1 − 2^{−σ} > 0 (alternating,
decreasing terms) and ζ(σ) = η(σ)/(1 − 2^{1−σ}) with 1 − 2^{1−σ} < 0, so ζ(σ) < 0 on (0, 1) (checked at 99 grid points, `z_side.log` Z1).
(c) Hence one-sided RH suffices over Z: if ψ(x) ≤ x + Cx^θ for x ≥ 1, put f(x) = x + Cx^θ − ψ(x) ≥ 0; its Mellin transform
F(s) = ∫₁^∞ f(x)x^{−s−1}dx = 1/(s − 1) + C/(s − θ) + ζ′(s)/(sζ(s)) is analytic on the real half-line (θ, ∞) (the pole at 1 cancels; by (b)
no real zeros). Landau's lemma — for f ≥ 0 the Taylor series of F at a real point s₀ > σ_c has nonnegative-term expansion
F(s₀ − h) = ∫ f(x)x^{−s₀+h−1}dx by monotone convergence, so analyticity on the real segment pushes the abscissa σ_c below θ — gives F
analytic on Re s > θ, i.e. ζ(s) ≠ 0 there. So the Z-analog of Bombieri's §III EXISTS (character twists with exact orthogonality) and is
UNNECESSARY: what class C needs over Z is its upper-bound half alone.
**Why the upper-bound half has no sharp Z-analog on the record (Z2, Z3).** Bombieri's (v) makes f ∘ φ = f^q an identity of functions,
so the auxiliary function vanishes to order p^μ at every rational point. Over Z the Frobenius congruence n^p ≡ n holds mod p for every n
but mod p² at exactly p of the p² residues (the Teichmüller residues; `z_side.log` Z2, all 29 primes < 110): first order only — the
numerical content of T24's kill "no Frobenius to differentiate against". What does exist is the order-one auxiliary integer: Chebyshev's
C(2n, n), divisible by every prime of (n, 2n], of size 2n log 2 — constant 1.386 per unit length where Stepanov's count has 1 (Z3:
ratio 1.40532, 1.39846, 1.38854, 1.38614 at n = 10³..10⁶). Its dual lower-bound form (Gelfond–Schnirelman) is refuted for PNT in one
variable ("0.4213 < t_Z([0, 1]) < 0.4232", Gorshkov 1956, via Pritsker 2013 p. 2, `sources/pritsker-…1307.5361.pdf`), reaches 0.99035 in
Nair–Chudnovsky's multivariable form (Pritsker (1.11)), and whether a sequence of weights reaches PNT is open in print ("this does not
preclude the possibility that such a proof can be obtained by finding a sequence of weights w_n with B(w_n) → 1", p. 4).

## §4 The partition theorem and the close

**Definition.** A zeta datum of genus g over F_q is Z(u) = L(u)/((1 − u)(1 − qu)) with L ∈ Z[u] of degree 2g, L(0) = 1,
L(u) = q^g u^{2g} L(1/(qu)), N_n = q^n + 1 − Σα_iⁿ ∈ Z_{≥0}, closed-point counts b_d ∈ Z_{≥0}, h = L(1) ≥ 1, and the Riemann–Roch-consistent
divisor counts A_n. Write 𝒵_{q,g} for the set of zeta data; V ∈ 𝒵_{5,1} (baseline.log), and so is ζ_{E₀}.

**Theorem P (the partition).** (i) Every proof of RH for curves read at the page in this note (R1–R4, R6–R13) derives RH through an
inequality I_c attached to one of four inputs c ∈ {A surface, B family, C coordinates, D group}:
I_A: def(D) = 2d₁d₂ − D² ≥ 0 on span(Δ, Γ_{πⁿ}) (R3, R4, R12, R13); I_B: q^{(k−1)/2} ≤ |α|^k ≤ q^{(k+1)/2} on H^k(C^k), k even
(R7), resp. |α| ≤ q^{(w+1)/2} for H¹_c of a pure sheaf of weight w on U ⊂ A¹ (R8, R9); I_C: ν₁(C′, η) ≤ Q + (2g′ + 1)Q^{1/2} + 1 for
every twist η of a Galois cover, with (7) at Q = p^α, α even (R6; R10 in explicit form); I_D: deg(rπ − s) ≥ 0, resp.
Tr(xx†) > 0 on Q[π] (R1, R2). (ii) V ∈ 𝒵_{5,1} violates each I_c at an explicit place and E₀ satisfies it there:
I_A at D = Γ_π − 2Δ (def −2; formal index (2, 2)); I_B at X = C × C (α² = 13.090 > 11.180, β² = 1.910 < 2.236) and at 2k = 4 in the family
form; I_C at Q = 5² for the twist (41 against (5) "< 41" and (7) "≤ 40"); I_D at π − 2 (deg −1, trace −2). (iii) Hence no input of any
class is a function of the zeta datum alone: if an input of class c could be built from Z ∈ 𝒵_{q,g} by any rule under which the proof's
lemma holds, the rule applied to V would yield I_c(V), which is false by (ii).

**Proof of Theorem P.** (i) is the table §2, row by row, each chain read at the page (R5 and R14 are excluded because not read; R11
records that the automorphic results read are consumers of RH, not proofs of it). (ii) is `verify/lines.log` L1–L8 with `baseline.log`
(exact integers except the eigenvalue magnitudes in L5–L6, which are closed forms: α² = (15 + 5√5)/2, q^{3/2} = 5√5). (iii): the proofs
use, besides their input, only zeta-level facts (rationality, FE, N_n, Riemann–Roch dimension counts), all of which V has; so a rule
building the input from Z would make the proof run on V and prove I_c(V). ∎ For g = 1, I_A and I_D are one statement: the binary form
m² + tmn + qn² (= deg(m + nπ) = ½def(mΔ + nΓ_π) = ½Tr((m + nπ)(m + nπ)†)) is positive on Z² \ {0}. The FORM is a function of the zeta
datum (it is the norm form of Q(π)); its POSITIVITY is exactly t² < 4q, i.e. RH for g = 1 — so on rung 1 every positivity proof proves
the positivity of a zeta-level form from an object the zeta datum does not supply, and V is the zeta datum whose form is indefinite
(Q(√5), unit φ of norm −1). `[novelty: single-check]` for Theorem P as a stated partition with a common witness; its parts are printed.

**Lemma Z4 (finite-support Chebyshev auxiliary integers never reach the sharp constant; proof on the page, `verify/z_side.log` Z4).**
Let c: N → Z have finite support with Σ_k c_k/k = 0, F_x := Π_k (⌊x/k⌋!)^{c_k}, g(t) := Σ_k c_k⌊t/k⌋ (bounded). Then
log F_x = Σ_n Λ(n) g(x/n) = Ax + O(log x) with A := −Σ_k c_k (log k)/k, and A = ∫₀^∞ g(t)t^{−2}dt (Mellin: ∫₀^∞⌊t/k⌋t^{−s−1}dt =
k^{−s}ζ(s)/s, let s → 1⁺). If g ≥ 0 and g ≥ 1 on [1, T), then ψ(x) − ψ(x/T) ≤ log F_x, whence ψ(x) ≤ κx + O(log²x) with
κ = AT/(T − 1) = ∫g t^{−2} / ∫₁^T t^{−2} ≥ 1; and κ = 1 would force g = 1_{[1,T)}, i.e. Σ_{k|m} c_k = [m = 1] − [m = T], i.e. c = μ ∗ (δ₁ − δ_T),
which has infinite support (c_ℓ = μ(ℓ) = −1 at every prime ℓ > T). So κ > 1: Chebyshev (T = 6) κ = 1.105550, the binomial C(2n, n) κ = 2 log 2
= 1.386294 (computed). The infinite-support limit c = μ gives F_x = e^{ψ(x)} = lcm(1, …, ⌊x⌋) exactly — the tautological auxiliary
integer, whose sharp bound is RH itself. `[novelty: single-check]`; nearest published object (10(n)): Chebyshev 1852 via Pritsker (1.2)
at the page; Diamond–Erdős 1980 on sharp elementary estimates `[recalled, unverified]` (not load-bearing).

**The one input whose Z-analog is not already dead.** A, B, D: dead on the record (§3: REFUTED in lattice / rationality / End form,
RH-RESTATED in their smeared / squeeze / positivity forms). C: its twist half EXISTS over Z and is unnecessary there (Z1); its
Frobenius-identity half holds to first order only (Z2); its finite-support Chebyshev half is killed by Lemma Z4; its infinite-support
Chebyshev limit is RH restated. **What remains alive is one input: class C's auxiliary object in the integer-polynomial form
(Gelfond–Schnirelman, multivariable Nair–Chudnovsky–Pritsker weighted capacity)** — at the page its PNT-strength is OPEN (Pritsker p. 4:
"this does not preclude the possibility that such a proof can be obtained by finding a sequence of weights w_n with B(w_n) → 1"), its
fixed-weight form cannot give PNT (ibid.), and by Z1 + Landau its RH-strength form is exactly one-sided RH for ∫ψ (Pritsker p. 4 records
∫₁^x ψ − x²/2 = O(x^{3/2}) under RH). Named gap: a sequence of polynomial weights w_n with 1 − B(w_n) → 0, and at a rate. **Cheapest
construction-or-refutation unit:** compute Pritsker's B(w) for the weights w = Π(integer Chebyshev factors)^{α_i} over [0, 1]ⁿ, n ≤ 6, by
his extremal-measure formula (a finite-dimensional optimization, one agent, one session, no new theory) and fit 1 − B(w_n) against the
number of factors; a plateau below 1 with a proof of an upper bound sup_w B(w) < 1 over polynomial-type weights REFUTES the class; a
decay to 0 is a construction of an elementary PNT route whose rate is then the RH question. Prior-art gate first: Pritsker's later
papers and Montgomery's Ten Lectures ch. 10 (neither on disk).

**Caveat for the rung-1 twin test (a correction to how the control may be used; `verify/twin_g2.{py,log}`; `[novelty: single-check]`).**
The tournament's rule "a mechanism the virtual curve passes cannot be the generator" (tournament read-F §3) is too strict for ONE-SIDED
mechanisms. For g = 1 every RH-false zeta datum has t² > 4q, hence REAL reciprocal roots, hence a_r > 0 (or of alternating sign) and it
passes every upper bound at even r — the F_q-shadow of a real off-line zero. Over Z that world is empty (Z1), and a one-sided bound
ψ(x) ≤ x + Cx^θ implies ζ ≠ 0 on Re s > θ. The right twin for one-sided mechanisms has NON-REAL off-line roots, which needs g ≥ 2; exact
search over F₅ (x_i non-real ⟺ a₁² − 4(a₂ − 2q) < 0): 111 genus-2 zeta data in the box |a₁| ≤ 20, |a₂| ≤ 60 with non-real off-line roots,
N_n ≥ 0 and b_d ≥ 0 (n, d ≤ 40), h ≥ 1. The first, **V₂: L(u) = 1 − u + 11u² − 5u³ + 25u⁴** (h = 31; N_1..4 = 5, 47, 143, 507;
b_1..4 = 5, 21, 46, 115; |α| = 2.7138, 1.8425; zeros at Re s = 0.6203, 0.3797), violates Bombieri's one-sided Theorem 1 by itself, with no
twist, at Q = 5⁶: N_6 − Q − 1 = 693 > 5Q^{1/2} = 625. Rule proposed for the zoo control (V.4 negative-control rule): test two-sided
and positivity mechanisms on V; test one-sided mechanisms on V₂ (V passing a one-sided mechanism is not evidence against it over Z).

**CLOSE: T.** Theorem P (the partition, with proof) and the table §2 (12 proofs read at the page, 2 rows named-not-read). Every proof of
RH for curves read here separates genuine curves from V through one of four inputs — A surface, B family, C coordinates, D group — none
a function of the zeta datum (witness V; control E₀ passes every line). On the record over Z, A, B and D are dead (REFUTED in their
lattice / rationality / End forms, RH-RESTATED in their smeared / squeeze / positivity forms); C is the one class not dead: its twist
half exists and is unnecessary over Z, its Frobenius and finite-support Chebyshev forms are killed here (Z2, Lemma Z4), and the input
left alive is its integer-polynomial auxiliary object (Gelfond–Schnirelman–Nair–Chudnovsky–Pritsker), open in print at PNT strength,
with the cheapest deciding unit stated above. Stop condition (a proof V passes) did NOT fire: Dwork's rationality theorem is passed by V
and is not a proof of RH (R9).
