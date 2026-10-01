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

**1.6 Q1 and Theorem 2.1 (l. 60–74) — ✓.** Q1 opened at the line: Hilberdink, JNT 112 (2005) p. 336, Cor. 2(b) (`novel-wave-s37/
beurling-frontier/sources/w-18a-…txt` l. 211–214): "If N_P(x) = ρx + O(x^β) for some constants ρ > 0 and β < ½, then for every η ∈ (β, ½),
ψ_P(x) − x = Ω(x^η) and ζ_P(s) has infinitely many zeros in the strip {η < Re s < 1}" (Greek letters lost in the transcription,
structure unambiguous); g-prime systems are sequences 1 < p₁ ≤ p₂ ≤ … (l. 31–34); proof l. 669–673 via Remark B(ii) (l. 233–235)
and Remark C (l. 496–501), as the NOTE says. Proof of 2.1 re-derived: Π_P ≤ N_P = O(u) under (ii), so log ζ_P = ∫u^{−s}dΠ_P on Re s > 1;
by (i), η̂ = ∫u^{−s}dD is analytic on Re s > α′ (absolute convergence after one integration by parts; the "−D(1)" term is the
convention ∫_{(1,∞)}, harmless); ζ_P = ζ_ref·e^{η̂} on Re s > 1; both sides meromorphic on the half-plane Re s > γ₁ = max(α′, γ₀, θ)
(the left by (ii)), so equal there; finitely many zeros in Re s > γ₁ contradict Q1 applied with β = θ and any η ∈ (γ₁, ½) ✓. Q1 is used at the statement level
only; its proof in print is terse (the step "then P is an [α′, β′]-system", i.e. finitely many zeros ⟹ a power-saving PNT, is standard
but not written there) — recorded, not a defect of the NOTE.
**1.7 Corollaries 2.2–2.3 (l. 75–85) — ✓ with one GAP (m4) and one overreach in the headline (F2).** (a) Π_P − Π_F = Σ_k(π_P − F)(u^{1/k})/k
needs the series to converge: for k > log u/log p₁, π_P(u^{1/k}) = 0 and the terms are −F(u^{1/k})/k, so F(v) → 0 as v → 1⁺ at a rate
(e.g. F(v) = O(log v)) is required, else Π_F is undefined ("any function F" is too wide). F_c satisfies it: F_c(v) ~ (6/π²)ρ log v. The
Möbius identity Σ_k F_c(u^{1/k})/k = Π_c(u) ✓ (absolutely convergent: Π_c(u^{1/n}) ≤ ρ log u/n·(1 + o(1))). (b) ζ_F = Π_k ζ_c(ks)^{1/k} ✓;
the k = 2 factor blows up like (s − ½)^{−1/2} at ½ while the k ≥ 3 factors and e^{η̂} are analytic and nonzero near ½ ✓. 2.3 is the
contrapositive ✓. **But** the theorem's class is "within u^{α′}, α′ < ½, of a reference meromorphic and finitely zeroed right of some
γ₀ < ½"; the headlines (l. 22–25 "So … by fixing the primes in advance is impossible"; §2 title l. 58) drop that qualifier. As worded
they are false: ℕ's primes are fixed in advance and ℕ has N − u = O(1). Theorem 2.1 is silent on ℕ only because ζ has infinitely many
zeros on Re s = ½ > γ₀ (any reference ζ_ref with infinitely many zeros right of ½ − ε escapes it). Fix in §4.
**1.8 Proposition 3.1 (l. 102–111) — ✓.** Composites in [B, Bh) have all prime factors < B (a factor q ≥ B gives qm ≥ p₁B); the least
x₀ with π_G(B, x₀] > π_R(B, x₀] exists (right-continuous integer steps) and is a greedy prime, so E_G(x₀−) = −τ and no composite sits at
x₀ (it would be counted first, lifting E_G to 1 − τ); minimality forces π_R(B, x₀) = π_G(B, x₀) and no R-prime at x₀, so E_R(x₀) = −τ and
E_R < −τ on (x₀, min(x₁, Bh)) — nonempty even if R's next event is beyond Bh ✓. Notation (m5): with B = p₁ᵏ (the generator's blocks) a
composite sits AT B, so f and the counts should run over [B, x], not (B, x].
**1.9 Proposition 3.2 (l. 116–126) — ✓ with a label defect (m6).** (a), (b) ✓; residue ρe^{η̂(1)}, η̂(1) = −D(1) + ∫D u^{−2} ✓. (c) rests on
Wiener–Ikehara, labeled [recalled, unverified] (not on disk) yet load-bearing. The (B)-failure needs no Tauberian theorem: if
N_{P₀}(x) ≤ (ρ + δ)x + C for all x, then ζ_{P₀}(σ) = σ∫N_{P₀}u^{−σ−1} ≤ (ρ + δ)σ/(σ − 1) + C, so ρ₀ ≤ ρ + δ; hence ρ₀ > ρ gives
limsup(N_P − ρx)/x ≥ ρ₀ − ρ > 0 by (a), and (B) fails for every θ < 1. Only the "≥ (ρ₀ − ρ)x(1 + o(1)) for all large x" form needs W–I.
**1.10 Proposition 3.3 (l. 128–148) — ✓ under two implicit hypotheses (m8), reproduced numerically.** (i) Moving primes down maps each
g-integer to one ≤ it, so N_{P′} ≥ N_P pointwise ✓. (ii) For x < y₀ only g-integers with exactly ONE moved prime factor, to the first power,
can cross x — this needs y₀ < a_J², i.e. y₀ > p_J² ("y₀ large"); such an n = qm crosses iff m·a_j ≤ x < m·q, so m ≤ x/a_j < p_j (the NOTE
writes "<" for the first), m lies in the finite set, x in a window of relative width < δ₀/2. "At most one pair (j, m) per x" needs
m p_{j′} ≠ m′ p_j for distinct pairs — δ₀ only separates DISTINCT values. That holds in a free monoid (m p_{j′} = m′ p_j with j ≠ j′ forces
p_j | m, impossible for m < p_j), e.g. S8 with t transcendental (s40 Lemma 1.3), but not for a general "discrete system P" as stated: add
"with unique factorization". Then N_{P′} − N_P ≤ n_j ≤ ¼Kx^θ + 1 and |E_{P′}| ≤ Kx^θ for x ≥ max(a_J, (4/K)^{1/θ}); below a_J nothing moved ✓.
(iii) ✓ if no moved prime sat exactly at a_j (else its dilate was already ≤ y₀: take the windows (a_j, a_j + H_j]). **Re-run**
(`verify-O/prop33.py`, own code, `prop33.log`): S8(π/16) greedy to 2.04·10⁵, θ = ¼, K := 2 sup_{x≤y₀}|E_P|/x^θ = 1.2668, y₀ = 2·10⁵, the
n_j = ⌈¼K a_j^θ⌉ primes just above a_j moved to a_j: (i) min(N_{P′} − N_P) = 0; (ii) sup_{x<y₀}|E_{P′}|/x^θ = 0.6334 = K/2 (on [a_J, y₀) it
rises 0.46 → 0.55, J = 12); (iii) E_{P′}(y₀) − E_P(y₀) = 23 = Σn_j (J = 6) and 41 = Σn_j (J = 12), the latter 41.29 > K y₀^θ = 26.79: the bound
breaks at y₀ exactly as stated. The window hypothesis H_j < δ₀a_j/2 is NOT met at this scale (max H_j/a_j = 0.0118 vs δ₀/2 = 4.3·10⁻⁴),
and (ii) held anyway. Control (same n_j bunched at a_j(1 + 0.005j/J), not aligned with y₀/p_j): E(y₀) unchanged (0.288).
**1.11 §6 (l. 249–269).** 6.1: with threshold τ, E = 1 − τ after a prime and −τ just before the next, so C(p_k, p_{k+1}) = ρg_k − 1 and
E ≤ ρG − τ ✓. 6.3: Σ_{n∈W}log n = Σ_{m∈G}ψ(W/m) is log = Λ ∗ 1 on a free monoid ✓, and the equivalence with Lemma M ✓ (for W = [y, y + |W|],
log n = log y + O(|W|/y)). The constant is wrong (m7): Σ_{m≤y}1/m = N(y)/y + ∫_1^y N u^{−2}du = ρ log y + 1 + ∫_1^∞E u^{−2}du + o(1), so
c_G = 1 + ∫_1^∞E(u)u^{−2}du, not 1 − ρ + …; check ℕ: 1 − ∫_1^∞{u}u^{−2}du = γ (the NOTE's form gives γ − 1). Not load-bearing.

## §2. Independent re-run (`verify-O/`; own code from the NOTE's definitions; nothing imported from `verify/`)

**2.1 Λ_{ρ,τ} and its root** (`lambda_arb.py`, `run_lambda.py`; logs `cert_lambda.log`, `roots_lambda.log`). Method A: python-flint arb,
256-bit balls, closed-form pieces, every comparison decided on balls (piece 0 handled exactly: p*¹ = c₀). Method B: mpmath quadrature
of each piece (no closed form). The 11 rows of Cor. 4.2, Λ(σ₁) (A; B agrees to all 12 printed digits):
π/16: ½ 0.000612754264850 · 1/10 0.0127408950976 · 1/50 0.460598275921 · 1/100 1.65304587503; π/32: ½ 0.00286841455839 · 1/100 0.425925405077;
π/8 1/100 2.30589386653; π/4: 1/10 0.0111543097896 · 1/100 3.61160532388 · 1/1000 387.958571893; 0.95π/3 1/100 4.30798442436 — all balls
> 0 with radius ≤ 5·10⁻¹⁰, equal to `verify/powerbump_iv.log` digit for digit. Largest roots σ_L (scan + 60 bisections): π/16: ½ 0.7631837176,
¼ 0.8316293090, 1/10 0.9114976726, 1/20 0.9518050842, 1/50 0.9799719898, 1/100 0.9899247148; π/32: ½ 0.8883704158, 1/100 0.9904126364;
π/8 1/100 0.9896617268; π/4: 1/10 0.8692342333, 1/100 0.9895250389, 1/1000 0.9989929612, ½ none in (0.30, 0.99999); 0.95π/3 1/100
0.9894958025 — equal to `powerbump_bound.log` to its 8 digits. So "any θ < 0.4945 at τ = 1/100 for each of the five densities" is
right (σ_L/2 ≥ 0.494748), and σ₁ = 0.989 (0.990 for π/32) is a valid certified point for each.
**2.2 Generator** (`bf_greedy.py`): min-heap enumeration, each g-integer generated once as (largest prime) × (cofactor) at the later of
its two factors' appearance; 80-digit arithmetic; a-posteriori certificate = least relative gap over all placement decisions (≥ 2.6·10⁻⁹
in every run, against a rounding error < 10⁻⁷⁶). Different algorithm (theirs: closure + insort at 50 digits) and different precision.
(a) The unit's four validated cases (π/16, τ ∈ {0.02, 0.25, 0.5}; π/4, τ = ½; X = 2·10⁴): N, π, composites, sup E, inf E(x−), max gap
identical to `validate_bf.log`. (b) **Target (d): τ = 1/100, π/16** — the unit's FIXED `rules2.cpp` (compiled to scratch) against mine:
X = 2·10³: N 398, π 19, comp 378; 2·10⁴: 3,930, 191, 3,738; 2·10⁵: 39,272, 1,903, 37,368; sup E 73.2724 (at x ≈ 50, the power bump), inf E(x−)
−0.010000, max gap 662.08 — identical in every field at all three X. The fixed generator is confirmed at τ = 1/100.
**2.3 Sharpness** (`sigma_star.py` on my dumps, X = 2·10⁵, `sigma_star.log`): σ* = 0.9899264 (τ = 1/100; NOTE 0.98993, σ_L 0.9899247),
0.9799828 (τ = 1/50; NOTE 0.97998, σ_L 0.9799720), 0.7947458 (τ = ½; NOTE 0.794752 at 10⁶, 0.794755 at 10⁷). The 4–5-digit agreement
of σ* with σ_L for small τ reproduces, and σ* > σ_L as the theorem requires.
**2.4 Explicit systems against Theorem 4.1** (`thm41_tests.py`, `cor44_counterexample.py`): template Λ(0.98) = 9.830 > ζ_c(0.98) = −8.818
(discreteness is necessary); ℕ: ζ ≥ Λ_{1,1}, min gap 0.177 on a grid, Λ_{1,1} < 0 on (0, 1); Q′ = ℕ ∪ {1 + τ/ρ}: inf E_{π/4} = −0.0100000 exactly
(at q⁻; integers alone keep E ≥ 0 beyond u = 5.66), N − ρ′X = −163, −255, −343, −442 at X = 10, …, 10⁴ (≈ −0.6 log X/log q): β(Q′) = 0.
