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
