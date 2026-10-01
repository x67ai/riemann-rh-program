# read-O — Opus dual read of `lemmaB-s41/U5-obstruction` (NOTE.md)

**Reader:** Opus 5.5 (second model of the dual-model check; agent). **Started:** 18:12 IST 2026-10-01.
**NOTE read:** `results/lemmaB-s41/U5-obstruction/NOTE.md`, SHA-256 `55df58db6caaf4304f3b96428cba934ad6012f6c7045e5f1951e9efc6189a4ee`,
353 lines (all line numbers below are at this hash).
**Also read:** `READ-BRIEF-O.md` (generic rules), `lemmaB-s41/CHARTER.md`, `lemmaB-s41/ORCH-NOTES.md`, `free-greedy-s40/theory/NOTE.md`
(Lemma 1.5, Thm 1.6, Cor. 1.4′, Cor. 1.7), the unit's `verify/` logs named below; sources at the line: Hilberdink JNT 112 (2005),
Hilberdink–Lapidus (2006, arXiv text), Hilberdink Acta Arith. 152 (2012), Neamah–Hilberdink arXiv:1901.06866v2. `read-F.md` not opened.
**Independent re-run:** `results/lemmaB-s41/U5-obstruction/verify-O/` (own code from the NOTE's definitions; mpmath at 30–50 digits,
exact rationals/integers where possible; nothing imported or copied from `verify/`).

## VERDICT LINE

(filled last)

## §1. Re-derivations at the line

Marks: ✓ = re-derived step by step; GAP = what is missing (+ fix); FALSE = failing step or counterexample.

**1.1 Prop. 1.1(i) (l. 54–55)** ✓. ℓ_k = 1 + (k − ½)t ≤ x ⟺ k ≤ ρ(x − 1) + ½, so N_L = 1 + ⌊y + ½⌋, y = ρ(x − 1), and
E_L = ⌊y + ½⌋ − y ∈ (−½, ½]: +½ exactly at the atoms, → −½ from the left, never −½. So R_L = 1 − ρ + E_L > ½ − ρ = r₀ (> ρ iff ρ < ¼)
and R_L is bounded. [computed, verify-O `lattice_control_O.log`: E_L = +0.5 at 49 atoms, −0.5 + 10⁻²⁵ just left, range over 2697 points
(−0.4999…98, 0.5].]
**1.2 Prop. 1.1(ii) (l. 55–56)** ✓. ℓ_k = (k − ½ + ρ)/ρ, so Σ_kℓ_k^{−s} = ρ^s Σ_{n≥0}(n + ½ + ρ)^{−s} = ρ^sζ(s, ½ + ρ); L = ζ_c + sÊ_L
(s40 Lemma 1.5 uses only N), analytic on Re s > 0 minus s = 1, residue ρ. [computed: direct sum Σ_{k≤3000} + Euler–Maclaurin tail
= Hurwitz form to ≤ 4·10⁻²⁹ at s = 3 and 2.5, four values of ρ.]
**1.3 Prop. 1.1(iii) (l. 57–58)** ✓. With E_L > −½: L(σ) = 1 − ρ/(1 − σ) + σ∫E_Lu^{−σ−1}du > ½ − ρ/(1 − σ) on (0, 1); L(1⁻) = −∞; IVT.
[computed: floor checked at 199 grid points for four ρ; σ*_L = 0.947588629779 (π/64), 0.893875615744 (π/32), 0.788932804185 (π/16),
0.589399247686 (π/8), by bisection on the Hurwitz form at 30 digits — the NOTE's table (l. 85–88) to all printed digits, also the
first-order column 0.947802, 0.894460, 0.789824, 0.589755 and L(0) = 1 − ρ.]
**1.4 Prop. 1.1(iv) (l. 58–59)** conclusion ✓, cited route GAP. The last paragraph of s40 Thm 1.6 writes −ζ′/ζ = s∫ψu^{−s−1}du "for
Re s > 1"; for L the log-series converges only on Re s > σ₁ (1.7 below), so the identity holds there and the argument runs from σ₁, not 1.
The conclusion is true and far from sharp: by 1.8, ψ_L(x) − x ≠ O(x^a) for every a < σ₁ (σ₁ = 1.181340 at π/16).
**1.5 Prop. 1.1(v) (l. 59–68)** ✓. Integrality by graded peeling (each (1 − μ^{−s})^{∓m} has integer coefficients); log L = Σ(−1)^{j+1}X^j/j
with distinct multisets ↦ distinct products (t transcendental: ∏(1 + (i − ½)T)^{e_i} are pairwise distinct in ℚ[T], unique factorization);
coefficient of λ in log L is c(e) = (−1)^{k+1}(k − 1)!/∏e_i!; Σ_{j|g} m_{λ^{1/j}}/j = c(e) and Möbius give m_λ = Σ_{j|g}μ(j)c(e/j)/j.
[computed, `euler_O.log`: two exact routes in ℤ[[X₁..X₅]] to total degree 7 (log + Möbius; Witt-style peeling with no logarithm) agree
on all 791 monomials; all m_λ ∈ ℤ; m = (−1)^{k+1}(k − 1)! at every product of k ≤ 5 distinct atoms; m = −1 at every 2-fold product
including squares; ℓ₁³, ℓ₁⁴, ℓ₁⁶: m = 0; ℓ₁²ℓ₂: +1; ℓ₁³ℓ₂: −1. With real values at π/16 (`star_L_O.log`): λ ≤ 400 gives 78 atoms,
35 two-fold (31 + 4 squares), six ℓ_a²ℓ_b, ℓ₁³, ℓ₁³ℓ₂, ℓ₁⁴ — the NOTE's census (l. 69–70) exactly; truncated product 1.0247170 / 1.0501612
against L = 1.0247173 / 1.0501717 at s = 3 / 2.5 — the NOTE's digits.] Two small points (minor m1, m2): the measure weight Π_L(ℓ_a²) is
c = −½, not −1 (Thm 2.1(a), l. 109, conflates Π_L with m); and "formally" (l. 60) should say the product converges absolutely only on
Re s > σ₁.
**1.6 "Every (A)-parameter has a control" (l. 73–74)** ✓. Atoms (k − r₀)/ρ ≥ 1 iff r₀ ≤ 1 − ρ; N = 1 + ⌊ρx + r₀⌋ for x ≥ 1, so
N − ρx = r₀ + 1 − {ρx + r₀} ∈ (r₀, r₀ + 1]; Remark 1.6′ of s40 gives the zero.
**1.7 The abscissa σ₁ (l. 126, 189, 213)** ✓, sharpened. X(σ) := Σ_kℓ_k^{−σ} = ρ^σζ(σ, ½ + ρ) decreases strictly on (1, ∞) from +∞ to 0;
σ₁ is the root of X = 1. As distinct multisets give distinct λ (1.5), Σ_λ|Π_L(λ)|λ^{−σ} = Σ_jX(σ)^j/j = −log(1 − X(σ)), finite iff
σ > σ₁: the total-variation abscissa of Π_L is exactly σ₁ [proved here]. [computed: σ₁ = 1.18134039 (π/16), 1.09122235 (π/32) — the
NOTE's values — and 1.04623533 (π/64), 1.36405754 (π/8).]
**1.8 NEW: L_ρ has infinitely many zeros in 1 < Re s < σ₁ — the NOTE's open point (l. 126, 189–191) settled** [proved here; single-check].
Let ρ be transcendental (π/16, π/32 qualify).
Step 1 (independence). If ∏ℓ_k^{n_k} = 1 (n_k ∈ ℤ, finitely many ≠ 0) then ∏(2k − 1 + 2ρ)^{n_k} = (2ρ)^{Σn_k}, an identity in ℚ(T) at T = ρ;
T and T + k − ½ are pairwise non-associate primes of ℚ[T], so every n_k = 0. Hence log ℓ₁, log ℓ₂, … are ℚ-linearly independent.
Step 2 (a model with a zero). Fix σ₀ ∈ (1, σ₁); a_k := ℓ_k^{−σ₀}, so Σa_k = X(σ₀) > 1 and a₁ < 1. Take K with A_K := Σ_{k≤K}a_k ≥ 1 + τ_K,
τ_K := Σ_{k>K}a_k (A_K − τ_K → X(σ₀) > 1). The set {Σ_{k≤K}a_kw_k : |w_k| = 1} is the closed annulus with radii max(0, 2max a_k − A_K) ≤ a₁ < 1
and A_K, so it contains −1 − τ_K; fix such w_k (k ≤ K) and put w_k = 1 for k > K. Then f_w(s) := 1 + Σ_kw_kℓ_k^{−s} is analytic on Re s > 1,
f_w(σ₀) = 0, and f_w ≢ 0 (f_w(σ) → 1 as σ → ∞).
Step 3 (Kronecker + Rouché). Take r ∈ (0, σ₀ − 1) with f_w ≠ 0 on |s − σ₀| = r; δ := min of |f_w| there > 0. Take M with
2Σ_{k>M}ℓ_k^{−(σ₀−r)} < δ/2 and ε with ε·Σ_{k≤M}ℓ_k^{−(σ₀−r)} < δ/2. By Step 1 and Kronecker's theorem the set of t with |ℓ_k^{−it} − w_k| < ε
for all k ≤ M is unbounded. For such t, on the closed disc, |L(s + it) − f_w(s)| ≤ Σ_{k≤M}ℓ_k^{−Re s}|ℓ_k^{−it} − w_k| + 2Σ_{k>M}ℓ_k^{−Re s} < δ;
by Rouché L has a zero in |s − σ₀ − it| < r. Unboundedly many t give infinitely many zeros, with real parts in (σ₀ − r, σ₀ + r).
Step 4 (none on Re s ≥ σ₁). There |X(s)| ≤ X(σ₁) = 1, and X = −1 would need every ℓ_k^{−it} = −1: false for t = 0 (X > 0) and for t ≠ 0
(t·log(ℓ_{k+1}/ℓ_k) ∈ 2πℤ \ {0} for all k is impossible as log(ℓ_{k+1}/ℓ_k) → 0⁺).
**So the real parts of the zeros of L_ρ are dense in [1, σ₁] and their supremum is σ₁ (not attained).** Consequences [proved here]: −L′/L has
poles with real parts accumulating at σ₁, so its Dirichlet series (the signed Λ_L) converges nowhere left of σ₁ (a convergent Dirichlet series
is analytic in its half-plane and equals −L′/L there); ψ_L(x) − x ≠ O(x^a) for every a < σ₁, while ψ_L = O(x^{σ₁+ε}) by 1.7. **α_L = σ₁ > 1:
the prime number theorem ψ_L ~ x is false for L_ρ.** Likewise 1/L has poles in 1 < Re s < σ₁, so M_L(x) has exponent σ₁.
Numerically [computed, `zeros_O_B.log`, below]: no zero in 1 ≤ Re s ≤ 1.25 for Im s ≤ 1000 — consistent with Step 3, whose t come from
simultaneous Diophantine approximation of dozens of phases and are far beyond any scan; this is why the NOTE's scan (l. 189–191) found
nothing, and why the question had to be settled by proof.
**1.9 §1.3 "Conjecture U fails for signed discrete systems" (l. 76–79; close (a), l. 28–29)** — true as worded, misleading as argued.
α_L ≥ σ*_L > ½ = max{½, 2β_L} holds, but by 1.8 α_L = σ₁ > 1: L violates U through zeros RIGHT OF 1 — where (P) with N ~ ρx forbids
zeros (a positive Π has the abscissa of N) — and not through its real zero. In the class "integer N, signed integer Euler exponents" U
fails for a cruder reason than the NOTE says, and the example says nothing about signed systems that keep a prime number theorem. The
logical consequence drawn (U, if true, needs (P) and (D) together) stands. → FIX-FIRST F1.
**1.10 Theorem 2.1 (l. 107–117)** ✓ (a)–(d) as model-theoretic statements: L_ρ has (A) with r₀ = ½ − ρ, (B) with θ = 0, (D); T has (A),
(B), (P); both have bounded E, so no deduction from {(A), (D)} or {(A), (P)} yields "E unbounded". Sign of Π_L at λ is (−1)^{k+1} (1.5), so
(P) fails exactly at products of an even number of atoms ✓ (weight −½, not −1, at squares: m1). "(P) at non-products" in (d) is informal
(which points are products depends on the system); harmless.
**1.11 Corollary 2.2 and close (i): which named methods L_ρ actually defeats (target (b))** — FALSE for items (2)–(3) as classified.
The close (l. 15–18) lists Hilberdink 2005's (3.2)–(3.4), Remark C, Cor. 2 and Neamah–Hilberdink Thm 1 among "arguments whose premises on
the system are (A), (B) and integrality", and Cor. 2.2 (l. 131–132) says each is valid "for every datum with (D) and the analytic hypotheses
it states, hence for L_ρ". At the line:
- Hilberdink's results are for [α, β]-systems, ψ = x + O(x^{α+ε}) with α < 1 (w-18a l. 117–124); (3.4) needs zero order of ζ_P on Re s = σ,
  which comes from Theorem A = Hilberdink–Lapidus Thm 2.3 (w-18a l. 222–228). That proof uses ζ ≠ 0 for Re s > α (p3-22c1 l. 756: "By
  Theorem 2.1, ζ(s) is non-zero for ℜs > α, and so log ζ(s) exists") and |φ(z)| ≤ φ(ℜz) (l. 788, Λ ≥ 0). For L, log L is analytic on no
  half-plane Re s > Θ with Θ < σ₁ (1.8), so Borel–Carathéodory cannot start: "the proof runs with 1 replaced by σ₁ (… zero order again)"
  (l. 213–214) is false below σ₁.
- Cor. 2(b)'s proof (w-18a l. 670–673) passes from "finitely many zeros in (γ, 1)" to "[α′, β′]-system", which needs ζ ≠ 0 on Re s ≥ 1.
  For L that step fails, so the method yields only "infinitely many zeros in Re s > γ" — already true by 1.8. "Cor. 2(b) predicts infinitely
  many zeros of L in η < Re s < 1" (l. 215–216; also l. 188 "for both", l. 237 "for signed data by 4.3") does not follow. Remark C is vacuous
  for L (its hypothesis, finitely many zeros right of η ∈ (β, α) = (0, σ₁), never holds).
- Neamah–Hilberdink assume abscissa 1 and α ∈ [0, 1] (1901.06866 l. 83–84); Theorem B needs α, β < 1 (l. 205–209); the proof uses
  Σ_{x−1<n≤x}|μ_P(n)| ≤ N_P(x) − N_P(x − 1) (l. 230). For L, 1/L has poles in 1 < Re s < σ₁, and μ_L(ℓ₁ℓ₂ℓ₃) = (−1)³3! = −6 sits
  where N_L has no atom. "The same steps (with σ₁ for 1) give γ_L = α_L" (l. 222–223): the steps fail; the conclusion α_L = γ_L = σ₁,
  β_L = 0 is true by 1.8 directly.
- What survives: (3.2)–(3.3) hold for L verbatim ✓ (integer weights, N_L ~ ρx, Fejér positivity; w-18a l. 300–349); Parseval/Plancherel,
  Carlson (L is of finite order in vertical strips) and the L² abscissa ✓; Landau on R − r₀ ✓ (6.3(a)); Theorem 1.6 ✓. And the reason the
  contradiction schemes of (2)–(3) cannot prove the obstruction is NOT the control but §4.2 / §4.4, which I re-derive ✓: on class (A)&(B)
  with θ < ½, Cor. 2(b) gives infinitely many zeros in (γ, 1) for every γ ∈ (θ, ½), so zero order (the only source of (3.4)) is unavailable
  left of ½, where (3.3) bites; and N–H's conclusion there is α = γ ≥ σ*, with β unconstrained. → FIX-FIRST F2 (restate (i) and Cor. 2.2)
  and F3 (§4.3, §4.4 L-part, l. 188, l. 237).
**1.12 Remark 2.3, the function-field control V (l. 138–147; target (c))** ✓. 1/((1 − u)(1 − 5u)) = Σ(5^{n+1} − 1)/4·u^n, and multiplying by
1 − 5u + 5u² gives A_n = (5^n − 1)/4 (n ≥ 1), so A_n − 5^n/4 = −¼ exactly. log Z = Σ_n a_n u^n/n with a_n = 5^n + 1 − (w₁^n + w₂^n),
w₁,₂ = (5 ± √5)/2 (inverse roots of 1 − 5u + 5u²; |w| ≠ √5, so V violates the Weil bound, hence "virtual"), and b_d = (1/d)Σ_{j|d}μ(d/j)a_j.
b_d ≥ 0 for ALL d [proved here]: d·b_d ≥ a_d − Σ_{j≤d/2}a_j ≥ 5^d(1 − 2·0.7237^d) − (5/4)·5^{d/2} − d > 0 for d ≥ 41 (w₂ < w₁ = 0.7236·5), and d ≤ 40 is
checked exactly (the NOTE checked d ≤ 16). Zeros at u = (5 ∓ √5)/10: Re s = 0.79899371783272 and 0.20100628216728; Z(5^{−σ}) > 0 on
(½, 0.79899), < 0 on (0.79899, 1), → −∞ at 1⁻. [computed, `curveV_O.log`: A_n exact to n = 39; b₁..b₈ = 1, 5, 25, 110, 500, 2215, 10000,
45100 — the NOTE's list; the Euler product ∏(1 − u^d)^{−b_d} reproduces A_n exactly to n = 20.] The NOTE's reading — (D) and (P) jointly
with a real zero > ½ coexist with a perfectly regular degree-level count on a geometric norm set, while V fails (A) (−¼ < 0) — ✓. One
precision (minor m3): V has no archimedean density, so "(A)" and "integer error" for V are at degree level (N(5^n) = Σ_{m≤n}A_m); the
sentence "V undershoots and so fails (A)" (l. 143) should say "its degree-level error −¼ is negative".
**1.13 §3.1 Parseval (l. 151–153)** ✓ (u = e^v; Plancherel for v ↦ E(e^v)e^{−σv} ∈ L¹ ∩ L² when E = O(u^θ), θ < σ).
**1.14 Prop. 3.2 (l. 155–162; target (d))** ✓ with one repair and one constant. Between atoms E has slope −ρ; on a piece of length ℓ,
min_e∫_0^ℓ(e − ρv)²dv = ρ²ℓ³/12 at e = ρℓ/2 ✓. Repair (minor m4): the n atoms cut [U, 2U] into n + 1 pieces including the two boundary
pieces, Σℓ_i = U exactly, so ∫_U^{2U}E² ≥ ρ²U³/(12(n + 1)²) = (U/12)(1 + o(1)) — the boundary pieces must be counted, else Σℓ_i < U and
the Hölder step does not give U³. Equality case ✓ (all pieces 1/ρ, E = ±½ at their ends: E_L). Constant (minor m5): summing dyadic blocks
with u^{−2σ−1} ≥ (2U)^{−2σ−1} gives (1 + o(1))/(48σ log 2) ✓ as a lower bound, but the sharp constant is 1/(24σ) (blocks [U, (1 + η)U],
η → 0), attained by E_L; "L_ρ meets the bound" (l. 161) is off by the factor 2 log 2 = 1.386. [computed, `meansq_O.log`, below.]
[computed, `meansq_O.log`, closed-form piece integrals at 30 digits:] block mean squares of E_L at U = 10³, 10⁴, 10⁵, 4.9·10⁵: 0.083394547,
0.083348734, 0.083333363, 0.083333247 — the NOTE's L column (l. 162) ✓; σ·∫_1^∞E_L²u^{−2σ−1}du = 0.040358, 0.041155, 0.041413, 0.041540
at σ = 0.05, 0.02, 0.01, 0.005 → 1/24 = 0.041667, not 1/(48 log 2) = 0.030056.
**1.15 §3.3 (l. 164–182)** spot-checked. The "exact" Parseval right sides for L, 0.6875 (σ = 0.3) and 0.3955 (σ = 0.45) (l. 165–166), are
3-point Gauss–Legendre values per gap (`verify/meansq_split.py` l. 19–20), inaccurate on the first gap [1, ℓ₁) where u^{−2σ−1} varies by a
factor 4–6. Exact closed form: 0.689343 and 0.397362 (cross-checked by adaptive quadrature to ℓ₁₉₉ plus the mean-1/12 tail: 0.68944,
0.39737). Minor m6; the reading (shortfall = the tail |t| > 2048) is unchanged. The S8 values share the same first gap and are presumably
low by a similar 0.002 [not recomputed: no S8 dump of my own]. The energy table and readings (i)–(iii) were not re-run (§8).
**1.16 §3.4 zeros (l. 184–191; target (a))** ✓ and sharpened. Newton from the NOTE's values: 0.730915276980 + 42.089391949i and
0.512473951247 + 22.437212622i, |L| < 10⁻²¹. Argument principle (adaptive arg-tracking, |Δarg| < 0.3 per step, min|L| on every contour
≥ 0.012) [computed, `zeros_O_A.log`, `zeros_O_D.log`]: winding 5 on [½, 1] × [½, 50], 7 on [½, 1] × [50, 100], 12 on [½, ¾] × [½, 100],
0 on [¾, 1] × [½, 100], 1 on [½, 0.95] × [−½, ½] (the real zero only), 0 on [0.95, 1.2] × [0.05, ½]. So L_{π/16} has EXACTLY 12 zeros
with ½ < Re s < 1, 0 < Im s < 100 (the NOTE: "≥ 12"), all with Re s < ¾ — numerically, not interval-certified. Right of 1
[`zeros_O_B.log`]: winding 0 on [1, 1.25] × [½, 1000] in four boxes (min|L| ≥ 0.41), consistent with 1.8. Why no scan can see the zeros
of 1.8 [computed, `chernoff_O.log`; heuristic for heights, rigorous for the random model]: by Kronecker–Weyl the values X(σ + it) are
distributed as Σa_ke^{iθ_k} with independent uniform θ_k [recalled: Bohr–Jessen], and Chernoff with log I₀(x) ≤ x²/4 for the tail gives
P(Re X ≤ −1) ≤ 10^{−31.6}, 10^{−60.2}, 10^{−245.9} on Re s = 1.02, 1.05, 1.10 (π/16) — zeros there first occur at heights of that order.
"Cor. 2(b) of Hilberdink predicts infinitely many for both" (l. 188): false for L (1.11); for S8 it is conditional on (B) with θ < ½,
i.e. on Lemma B — minor m7 for the S8 half, F3 for the L half.
**1.17 §4.1–4.6 at the page (target (b))**. 4.1's quotations ✓ at the lines named (Thm 1 w-18a l. 195; Cor. 2(b) l. 211–214; Remark C
l. 496–501; (3.2) l. 317–320, Fejér l. 330–341, (3.3) l. 345–354; (3.4) l. 436–455), with one omission that matters: Theorem A needs an
[α, β]-system, and its proof uses ζ ≠ 0 right of α before positivity (1.11). 4.2 ✓ re-derived (class (A)&(B), θ < ½: Thm 1 is satisfied;
Cor. 2(b) gives infinitely many zeros in (γ, 1), γ ∈ (θ, ½); so zero order left of ½ is unavailable and (3.3) meets no (3.4)). 4.3 FALSE
below σ₁ (F3). 4.4: class-(A) reading ✓ (α ≥ σ* > ½ > θ ≥ β forces α = γ; β free); L-part route FALSE, conclusion true (F3). 4.5 ✓ as a
summary. 4.6 ✓ for (D) + (P): log ζ_P − log ζ_ref = s∫(Π_P − Π_ref)u^{−s−1}du = η̂, analytic on Re s > α′, so ζ_P inherits the finitely
many zeros of ζ_ref right of max(θ, α′, γ₀) < ½, against Cor. 2(b). "For signed data by 4.3" (l. 237) is unsupported: for signed Π the
three-circles step has no bounded M₁ (η̂ = O(|t|) only), and 4.3 is false (F3).
**1.18 Prop. 5.1, the clip bound (l. 244–249; target (d))** ✓. N(b) − N(a) = #g-primes in I + C(I) ≥ C(I), so E(b) − E(a) ≥ C(I) − ρ|I|, and
E(a) ≥ −c; sup over I ⊂ [1, x] gives sup_{u≤x}E ≥ Q(x) − c. "For S8 the converse holds" ✓: s40 Lemma 1.4/Cor. 1.4′ (no ties, t
transcendental) give E(u) = sup_{y≤u}(C[y, u] − ρ(u − y)) + r(u), r ∈ (−½, ½], hence |sup_{u≤x}E(u) − Q(x)| ≤ ½; with E > −½,
(B) with exponent θ ≥ 0 ⟺ Q(x) = O(x^θ) ✓. (Cited as s40 l. 92–94; at today's s40 text it is l. 90–92: m8.)
**1.19 §5.2 table (l. 259–264)** ✓ arithmetic: x^{σ*/2} with σ*/2 = 0.397376 gives 242, 605, 1511, 9420; Q/log²x = 0.0511, 0.0491,
0.0491, 0.0493; the ratio to x^{σ*/2} falls by 14.3. Q and sup E themselves are the unit's S8 data (not re-run, §8).
**1.20 §5.3 (l. 271–283)** ✓. #(g-integers in I prime to P(z)) = Σ_{d|P(z)}μ(d)N(I/d) (free monoid) = ρ|I|M(z) + ΔE(I) + S_z(I); these are
π(I) + C_rough(I) (a > z); with N(I) = π(I) + C(I) = ρ|I| + ΔE(I) this gives C(I) − ρ|I| = C_rough(I) − ρ|I|M(z) − S_z(I) exactly. |ΔE(J)| ≤
2max|E| and 2^{π(z)} − 1 terms give |S_z| ≤ 2^{π(z)+1}max_{y≤b/p₁}|E(y)| ✓.
**1.21 Cor. 6.1 (l. 287–297; target (d))** ✓ at the page: Hilberdink 2012 Thm A (p3-22c2 l. 102–110: N ∈ T, N(x) − cx of period P, N
determines a g-prime system ⇒ P ∈ ℕ, N(x) = Σ_{n≤P,(n,P)=1}([(x − n)/P] + 1), the integers prime to P); Def. 1.3 l. 326–333 ✓; class T
l. 264–270 ✓. Period-average of [y] − y is −½, so the average of R = N − (φ(P)/P)x is φ(P)/2 − (1/P)Σ_{(n,P)=1,n≤P}n = 0 (P ≥ 2;
Σn = Pφ(P)/2) or −½ (P = 1); R is not a.e. constant, so inf R < 0 ✓. L_ρ (periodic R, inf R = ½ − ρ > 0) is excluded only through
"determines a g-prime system", i.e. (P) ✓.
**1.22 §6.2, the local positivity inequality (★) (l. 299–320; target (e))** ✓ derivation, ✓ failure for L, one hypothesis to tighten.
Free monoid: log n = Σ_{β|n}Λ(β), so Σ_{n∈I}log n = Σ_βΛ(β)N(I/β) (exact). For I = (x, x + h] with x + h < p₁x, the β ∈ I terms give
ψ(I) (I/β ∋ 1 only); β > x + h give 0. Write N(J) = ρ|J| + ΔR(J); ∫_I log u dN = ρh log x + ΔR(I)log x + O((N(I) + h)h/x); Mertens
Σ_{β≤x}Λ(β)/β = log x − A/ρ + o(1) with A = ρ + ∫_1^∞Ru^{−2}du the constant term of ζ_P at 1 (ζ_P = ρs/(s − 1) + s∫Ru^{−s−1}du =
ρ/(s − 1) + A + O(s − 1), so −ζ′/ζ = 1/(s − 1) − A/ρ + …). Then ψ(I) ≥ 0 is exactly (★) ✓. Tighten (minor m9): the Mertens form needs
ψ(u) − u = o(u) and ∫_1^∞(ψ(u) − u)u^{−2}du convergent; "a PNT with error o(x/log x)" (l. 308) does not give the convergence. Under (B)
the PNT with error O(x e^{−c√log x}) is quoted at Hilberdink 2005 l. 126–131 (from Diamond), which does; and "(★) holds automatically for
every Beurling system" (l. 310) should read "for every Beurling system with (B)". For L [computed, `star_L_O.log`, h = 10⁻⁸, all
semigroup elements ≤ 9000, A_L = 1 + ρ log ρ − ρψ(½ + ρ) = 0.921962]: the exact identity holds (both sides 0 to 10⁻³⁰) and
LHS − RHS of (★) = −Π_L(λ)log λ in every window: +3.4223 (ℓ₁ℓ₂), +1.2660 (ℓ₁², Π = −½), +5.3310 (ℓ₂ℓ₅), +1.2660 (ℓ₁⁴, Π = −¼), +53.864
(ℓ₁ℓ₂ℓ₃ℓ₄, Π = −6) — (★) FAILS; −12.084 (ℓ₁ℓ₂ℓ₃), −4.688 (ℓ₁²ℓ₂), −1.266 (ℓ₁³), −13.903 (ℓ₁ℓ₂ℓ₇) — holds. So (★) fails for L exactly at
the windows around λ with Π_L(λ) < 0, i.e. k even — where the NOTE says ✓. "A = 0.937500 for S8(π/16) … a coincidence" (l. 318) is S8 data
(not re-run). The GAP statement (l. 313–315) is a correct description of what a proof along this line would need; it is not a theorem.
**1.23 §6.3 (l. 322–330)** ✓. (a) ζ_P = ρs/(s − 1) + r₀ + sĜ(s), Ĝ = Mellin transform of R − r₀ ≥ 0, |Ĝ(σ + it)| ≤ Ĝ(σ) ✓. (b) ζ_P(0⁺) =
lim sF(s) = log-mean of R ≥ r₀ (Abelian) and ζ_P(1⁻) = −∞ ✓ — gives a zero in (0, 1), not the sharper (σ₀, 1) (wording "a second proof
of the real zero" is fine); P ∖ {q} has R(x) − R(x/q) (N_{P∖q} = N(x) − N(x/q), density ρ(1 − 1/q)) ✓. (c) Ê(σ*) = −ζ_c(σ*)/σ* ✓:
−0.08838 for L (σ*_L = 0.788933), −0.05455 for S8 (σ* = 0.794752) ✓. (d) quoted, not re-derived (s40 read-O F1).

## §2. Independent re-run (`verify-O/`; own code from the NOTE's definitions; nothing imported from `verify/`)

| quantity (NOTE line) | NOTE | read-O (method) | agreement |
|---|---|---|---|
| σ*_L π/64, π/32, π/16, π/8 (l. 85–88) | 0.947589, 0.893876, 0.788933, 0.589399 | 0.947588630, 0.893875616, 0.788932804, 0.589399248 (bisection, Hurwitz, 30 digits; `lattice_control_O.log`) | all printed digits |
| first-order s₀ + ρL(s₀); L(0) (l. 85–88) | 0.947802 … 0.589755; 1 − ρ | 0.94780193, 0.89446023, 0.78982354, 0.58975476; L(0) = 1 − ρ to 10 digits | all digits |
| E_L range (l. 54, 71) | (−½, ½] | +½ at atoms, −½ + 10⁻²⁵ left of them; Hurwitz = direct sum to 4·10⁻²⁹ | ✓ |
| σ₁ π/16, π/32 (l. 189) | 1.181340, 1.091222 | 1.1813403944, 1.0912223517 (bisection) | ✓ |
| Euler exponents, census λ ≤ 400, truncated product (l. 62–71) | as listed; 1.0247170 / 1.0501612 | two exact routes to degree 7 (`euler_O.log`); census and 1.02471695 / 1.05016124 (`star_L_O.log`) | exact / 8 digits |
| zeros of L right of ½ (l. 185–186) | ≥ 12 below Im 100; 0.730915 + 42.089392i, 0.512474 + 22.437213i | exactly 12 (argument principle), all Re < ¾; both zeros to 12 digits (`zeros_O_A.log`, `zeros_O_D.log`) | ✓, sharpened |
| zeros of L in 1 < Re s < σ₁ (l. 189–191) | not settled | infinitely many (proof, §1.8); none with Re ≤ 1.25, Im ≤ 1000 (`zeros_O_B.log`); Chernoff 10^{−31.6} on Re s = 1.02 (`chernoff_O.log`) | settled |
| V: A_n, b_d, zeros (l. 140–142) | −¼; 1, 5, 25, 110, …; 0.79899, 0.20101 | exact to n = 39, d = 40; 0.79899371783, 0.20100628217 (`curveV_O.log`) | ✓ |
| L block mean squares (l. 162) | 0.083395, 0.083349, 0.083333, 0.083333 | 0.0833945, 0.0833487, 0.0833334, 0.0833332 (closed form; `meansq_O.log`) | ✓ |
| L Parseval right side σ = 0.3, 0.45 (l. 165–166) | 0.6875, 0.3955 | 0.689343, 0.397362 (closed form; quadrature 0.68944, 0.39737) | DIFFERS 0.3–0.5 % (m6) |
| σ → 0 constant of Prop 3.2 (l. 160) | 1/(48σ log 2) | σ·∫ → 0.041540 at σ = 0.005 → 1/24 | m5 |
| (★) for L (l. 310–313) | fails at even products | LHS − RHS = −Π_L(λ)log λ, 9 windows (`star_L_O.log`) | ✓ |
| S8(π/16) at 10³…10⁶ (l. 94–96, 252, 261) | π(10⁶) = 72,603 (l. 317); sup E 9.636; Q 9.754 | own sweep generator (`s8_O.py`): π = 72603, C = 123746, sup E = 9.6362, Q = 9.7537; 10³–10⁵ rows equal the unit's log | all digits |
| S8(π/32) sup E at 10⁶ (l. 95) | 6.393 | 6.3931 | ✓ |
