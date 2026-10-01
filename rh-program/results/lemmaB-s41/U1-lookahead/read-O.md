# read-O — OPUS READER on unit `lemmaB-s41/U1-lookahead` (NOTE.md: a placement rule with a proved bound, or a class theorem)

Reader: Opus 5.5 (second model of the dual-model check; standing orders 5, 7, 11(c)). Started 18:09 IST 2026-10-01.
NOTE read whole at SHA-256 54c5e5dd8e128289ced033f777dcfe6e561f2082ee38d7d340751e508498807b (31 684 bytes, 277 lines). Also read:
`lemmaB-s41/CHARTER.md`, `ORCH-NOTES.md`, the U1 blocks of `SHARED.md`, `free-greedy-s40/theory/NOTE.md` §1 (1.0–1.7), §2.1–2.2,
§3.1; the unit's `verify/` scripts and logs named below. `read-F.md` was not opened. Independent re-run: `verify-O/` (own code
written from the NOTE's definitions; nothing imported or copied from `verify/`). Conventions: ✓ = re-derived at the line;
GAP = stated with the fix; FALSE = counterexample or failing line given.

VERDICT LINE: (pending — filled last)

## §1. Re-derivations at the line

**1.1 Theorem 4.1 (l. 152–161) — ✓.** Re-derived step by step. (1) On [1, p₁) only the unit is counted, so E(u) = −ρ(u − 1) there; E ≥ −τ
on [1, p₁) gives sup_{u<p₁} ρ(u − 1) = ρ(p₁ − 1) ≤ τ, i.e. p₁ ≤ p* = 1 + τ/ρ (equality allowed: greedy has p₁ = p* exactly). A system
with no g-prime has E = −ρ(u − 1) → −∞, so p₁ exists. (2) p₁ʲ ∈ G for all j, so N(u) ≥ 1 + ⌊log u/log p₁⌋ ≥ 1 + ⌊log u/log p*⌋ = 1 + k(u);
hence E ≥ max(−τ, k − ρ(u − 1)) = −τ + (k − ρ(u − 1) + τ)⁺. Repeated g-primes (p₁ = p₂ = …) only add g-integers. (3) For Re s > 1,
ζ_P(s) = s∫_1^∞N u^{−s−1}du, and s∫_1^∞(ρ(u − 1) + 1)u^{−s−1}du = 1 + ρ/(s − 1) = ζ_c(s); E = O(u^θ) makes s∫E u^{−s−1}du analytic on
Re s > θ, so ζ_P(σ) = 1 − ρ/(1 − σ) + σ∫E u^{−σ−1}du on (θ, 1) (continuation). Inserting (2) and σ∫_1^∞u^{−σ−1}du = 1 (σ > 0; θ ≥ 0
because E jumps by integers and falls with slope ρ, so E ≠ o(1)) gives ζ_P ≥ Λ_{ρ,τ}. (4) σÊ(σ) is bounded near 1 (|Ê| ≤ C/(σ − θ)), so
ζ_P(σ) → −∞ as σ → 1⁻; IVT gives σ* ∈ (σ₁, 1); α ≥ σ* > σ₁ by the s40 Thm 1.6 argument (−ζ′/ζ has a pole at σ*, while s/(s − 1) + H
is analytic on Re s > a for every a < σ*; the domain {Re s > max(a, θ)} minus the isolated zeros and 1 is connected) — ✓.
*Where (B) is used:* only for the continuation of ζ_P to (θ, 1) (and the boundedness of σÊ near 1). *Where discreteness is used:* only in
(1)–(2) — a first g-prime exists and its powers are g-integers with unit jumps. The template (continuous, E ≡ 0, ζ_c(σ) = 1 − ρ/(1 − σ))
violates the conclusion: at ρ = π/16, τ = 1/100, σ = 0.98, Λ = +9.830 > 0 > ζ_c = −8.818 (`verify-O/thm41_tests.log`) — the theorem
is genuinely a discrete statement. ℕ (ρ = τ = 1, outside the stated ranges ρ, τ ∈ (0, 1) but the proof runs unchanged, p* = 2 = p₁):
ζ(σ) ≥ Λ_{1,1}(σ) on a 199-point grid of (0, 1), min gap 0.177, and Λ_{1,1} < 0 throughout — consistent with Remark 4.5.
*Finite-sum remark (l. 162–163)* ✓: the primitive of (k + τ + ρ − ρu)u^{−σ−1} is as printed; piece k is nonempty iff p*ᵏ < c_k; if
p*ᵏ ≥ c_k and (p* − 1)(k + ρ + τ) ≥ 1 then p*^{k+1} ≥ p*c_k ≥ c_k + 1/ρ = c_{k+1}, and the second condition persists, so all later pieces
are empty (my code stops on exactly this test). *"Always improves s40 Thm 1.6" (l. 164)* ✓, strictly: the integrand equals 1 at u = p*.

**1.2 Corollary 4.2 (l. 167–185) — ✓, with a rounding defect in the table (m1).** N − ρu = O(u^θ) ⟹ E = O(u^θ); θ < σ₁/2 < σ₁, so 4.1
gives α > σ₁; β ≤ θ; hence α > σ₁ > 2θ ≥ 2β and α > σ₁ > ½ (every σ₁ in the table is ≥ 0.763), i.e. α > max{½, 2β}: U fails. ✓.
My arb evaluation (256-bit balls, closed-form pieces; second method: mpmath quadrature of each piece) certifies Λ(σ₁) > 0 at all 11
rows; values agree with `verify/powerbump_iv.log` to every printed digit (§2.1). But the column "certified Λ(σ₁) ≥" rounds to nearest in
seven rows, overstating the lower bound in the last digit: 0.461 (true 0.460598…), 0.00287 (0.0028684…), 0.426 (0.425925…), 2.306
(2.305894…), 0.0112 (0.011154…), 3.612 (3.611605…), 4.308 (4.307984…). Positivity, which is all that is used, is unaffected.

**1.3 Proposition 4.3 (l. 186–192) — ✓.** For τ ≤ ρ: τ/(2ρ) ≤ a = log(1 + τ/ρ) ≤ τ/ρ (log(1 + x) ≥ x − x²/2 ≥ x/2 on [0, 1]); U = 1/(ρa) ∈
[1/τ, 2/τ], so U ≥ 1. On [1, U]: k ≥ log u/a − 1, hence (k − ρ(u − 1) + τ)⁺ ≥ log u/a − 1 − ρu; dropping (U, ∞) lowers the integral.
∫_1^U log u·u^{−σ−1} ≥ ∫_1^U log u·u^{−2} = 1 − (1 + log U)/U (σ < 1); σ∫_1^U u^{−σ−1} ≤ 1; ∫_1^U u^{−σ} = (U^{1−σ} − 1)/(1 − σ) ≤ U^{1−σ}log U.
With (1 + log U)/U = ρa(1 + log U) this is the printed line; then σ/a ≥ (1 − cτ)ρ/τ, σρ(1 + log U) ≤ ρ(1 + log(2/τ)), U^{cτ} ≤ (2/τ)^{cτ} ≤ 2
for small τ give Λ(1 − cτ) ≥ (ρ/τ)(1 − 1/c) − cρ − τ − ρ(1 + log(2/τ))(1 + 2) > 0 for τ < τ₀(ρ, c). Λ is continuous on (0, 1) and → −∞ at 1,
so its largest root is > 1 − cτ. ✓. Numerically 1 − σ_L = 1.008τ (π/16, 1/100), 1.007τ (π/4, 1/1000): c > 1 is needed and suffices.

**1.4 Corollary 4.4 (l. 205–208) — FALSE as worded; true once β is read relative to the density ρ (F1).** "Every discrete system with
E ≥ −1/100 has β ≥ 0.4945" fails if β is the system's own exponent (the program's [α, β] convention: N = ρ′x + O(x^{β+ε}) for the
system's own ρ′). Counterexample: Q′ := ℕ with one extra g-prime q = 1 + τ/ρ (τ = 1/100, ρ = π/4, q = 1.012732…). N_{Q′}(x) =
Σ_{j≥0}⌊x/qʲ⌋ = x/(1 − 1/q) + O(log x), so β(Q′) = 0; and E_ρ := N_{Q′} − ρ(u − 1) − 1 ≥ −1/100 for every u (on [1, q) E_ρ = −ρ(u − 1) >
−1/100; on [q, 2) the powers qʲ outrun ρu; for u ≥ 2, N_{Q′}(u) ≥ ⌊u⌋ + ⌊log(u/2)/log q⌋ ≫ ρu). Theorem 4.1 does not apply (E_ρ grows
linearly), and U is not contradicted (ζ_{Q′} = ζ(s)/(1 − q^{−s}), α(Q′) = α(ℕ)). The proof of 4.4 from 4.2 is correct for the quantity
it actually controls: N − ρu ≠ O(u^θ) for every θ < 0.4945, with the same ρ as in E ≥ −τ. The same reading is needed in §0 (1) (l. 19–20).
"Would have to reach u^{0.4945} — about 9,000 at u = 10⁸ — eventually" (l. 208) is also loose: β ≥ 0.4945 says |N − ρu|/u^θ is
unbounded for each θ < 0.4945; it does not say |N − ρu| ≥ u^{0.4945} ever, nor anything at u = 10⁸ (m2).

**1.5 Remark 4.5 (l. 209–212) — ✓, one wording slip (m3).** No real zero in (θ, 1) and ζ_P → −∞ at 1 ⟹ ζ_P < 0 on (θ, 1) ⟹ Λ ≤ ζ_P < 0
there with τ = −inf E (the proof of 4.1 needs only E ≥ −τ; τ = 1 for ℕ is outside the stated range but harmless). For ℕ the bump
(k − (u − 1) + 1)⁺ is 2 − u on [1, 2) and 3 − u on [2, 3): two unit right triangles (a sawtooth), not "a single unit triangle on [1, 3)".
