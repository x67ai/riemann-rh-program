# read-O — second producer and line reader of `U6-certificate/NOTE.md`

Started 17:46 IST 2026-10-01, closed 18:17 IST 2026-10-01. Writer: Opus 5.5 (agent), independent second producer. Labels: **[proved here]**, **[computed]**
(script + log in `verify-O/`), **[quoted]** (source opened at the line), **[recalled, unverified]** (never load-bearing).
Independence: the NOTE was read; `verify/` (code, logs, data) and `read-F.md` were NOT opened until §2's numbers were final.
NOTE line numbers below refer to `NOTE.md` as read at 17:36 IST 2026-10-01 (335 lines).

**VERDICT LINE: CONFIRMED.** Both certificates are reproduced by an independent second producer (exact-integer cell decisions, own moment evaluator): identical counts wherever both computed them (N and π_P at all 14 half-decade checkpoints, N, π_P and E at x_K, for both densities), and F_X balls ~10⁴ times tighter — the zero of F_{x_K} lies in (0.794755370097380, 0.794755370097381) for S8(π/16) and in (0.895076517592160, 0.895076517592161) for S8(π/32); F_X(0.794755370097) = 1.8192·10⁻¹² > 0 and F_X(0.895076517592) = 1.44325·10⁻¹² > 0 are proved. NOTE §1, §6, §7 re-derived at the line: every statement ✓ or GAP-minor, none FALSE; all 14 σ₂ and the concavity bounds reproduced. 8 OLD/NEW pairs (§4), none moving a certificate or a threshold.

## §1. Re-derivations at the line (NOTE §1, §6, §7) [proved here unless marked]

Notation as in the NOTE: t = 1/ρ, x_k = 1 + (k − ½)t, w(u) = ρ(u − 1) + ½, T = ρ(u − 1) + 1, E = N − T, s(u) := ½ − {w(u)}.

**1.1 Lemma 1.1 (sawtooth floor), l. 41–44 — ✓.** E = N − w − ½; s40 Lemma 1.1 (E > −½, re-read at s40-NOTE l. 59–62) gives N > w;
N ∈ ℤ gives N ≥ ⌊w⌋ + 1, so E ≥ ⌊w⌋ + ½ − w = s(u). At u = x_k, w = k, so E(x_k) ≥ ½ (e_k ≥ 0); s has mean 0 per period. ✓

**1.2 Lemma 1.2 (positive tail), l. 46–52 — ✓.** On [x_k, x_{k+1}), w − k = ρ(u − x_k) ∈ [0, 1), so s = ½ − ρ(u − x_k); with
u = m_k ∓ v (m_k the midpoint, 0 < v ≤ t/2) s = ±ρv, and the period integral is ∫_0^{t/2}ρv[(m_k − v)^{−σ−1} − (m_k + v)^{−σ−1}]dv > 0
for every σ > −1 (strictly decreasing weight). |s| ≤ ½ and σ > 0 give absolute convergence, so the split over periods is legitimate. ✓

**1.3 Theorem 1.3 (criterion at a lattice point), l. 54–68 — ✓.** (i) F_X(s) = ζ_c(s) + s∫_1^X E u^{−s−1}du for all s ≠ 1 and all
X ≥ 1, re-derived: Σ_{n≤X}n^{−s} = X^{−s}N(X) + s∫_1^X N u^{−s−1}du (N(1−) = 0); with N = T + E and
X^{−s}T(X) − s∫_X^∞T u^{−s−1}du = −ρX^{1−s}/(s − 1) one gets Σ_{n≤X}n^{−s} = ζ_c(s) − ρX^{1−s}/(s − 1) + E(X)X^{−s} + s∫_1^X E u^{−s−1}du.
Both sides are meromorphic with the single pole s = 1. (ii) Under (B) the dyadic bound is immediate; under (B₂),
∫_Y^{2Y}|E|u^{−σ−1} ≤ Y^{−σ−1}·Y^{1/2}(∫_Y^{2Y}E²)^{1/2} ≪ Y^{θ₂−σ}; summed over Y = 2^m the Mellin integral converges absolutely and
locally uniformly on Re s > θ′, so ζ_P = ζ_c + sÊ continues there (pole at 1 only) and ζ_P(σ) = F_X(σ) + σ∫_X^∞E u^{−σ−1}du for real
σ ∈ (θ′, 1). (iii) Lemma 1.2 gives ζ_P(σ₁) > F_X(σ₁) ≥ 0 (strict even when F_X(σ₁) = 0). (iv) ζ_c(σ) = 1 − ρ/(1 − σ) → −∞ while σÊ(σ)
stays bounded on [σ₁, 1]; IVT. (v) The ψ-step: −ζ′_P/ζ_P − s/(s − 1) = s∫_1^∞(ψ_P − u)u^{−s−1}du on Re s > 1; if ψ_P − x = O(x^a),
a < σ*, the right side is analytic on Re s > a, and the identity extends to the connected set {Re s > max(a, θ′)} minus the
(isolated) zeros of ζ_P and the point 1, contradicting the pole of −ζ′_P/ζ_P at σ* > max(a, θ′). Only the continuation is used,
which (B₂) supplies. ✓ (θ < 0 in (B) is vacuous: N − ρu cannot tend to 0, N jumps by 1.)

**1.4 Corollary 1.4, l. 70–79.** (a) **✓.** α ≥ σ* > σ₁ and 2β ≤ 2θ < σ₁, σ₁ > ½. *Exponent arithmetic:* the strict "θ < σ₁/2" is
more than needed — θ = σ₁/2 already gives 2β ≤ σ₁ < σ* ≤ α; likewise θ₂ = (3σ₁ − 2)/4 gives 2β ≤ 2(1 + 2θ₂)/3 = σ₁ < α. So the
NOTE's truncated thresholds (strictly below the true values, §2.4) are safe, and "≤" at the exact values would be too.
(b) **GAP (minor, conclusion unaffected).** The slope facts are right: for y ≥ x, E(y) − E(x) = N(y) − N(x) − ρ(y − x) ≥ −ρ(y − x).
For E(x) = H > 0, E ≥ H/2 on [x, x + H/(2ρ)], inside [x, 2x] iff H ≤ 2ρx; for E(x) = −H, E ≤ −H/2 on [x − H/(2ρ), x], inside
[x/2, x] iff H ≤ ρx. Either way ∫_{x/2}^{2x}E² ≥ H³/(8ρ). The parenthesis of l. 77, "a larger H only strengthens the bound: |E| ≥ H/2
on all of [x, 2x]", is false for ρx < H < 2ρx (the slope bound gives only E ≥ H − ρx < H/2 at u = 2x). Fix: split at 2ρx in the
positive case (window argument for H ≤ 2ρx; E ≥ H − ρ(u − x) ≥ H/2 on all of [x, 2x] for H ≥ 2ρx, giving H ≪ x^{θ₂}); the negative
case needs no split, since N ≥ 1 forces E ≥ −ρ(x − 1) > −ρx. Then H ≪ x^{(1+2θ₂)/3} in all cases, β ≤ (1 + 2θ₂)/3, and the
threshold θ₂ < (3σ₁ − 2)/4 follows: 2(1 + 2θ₂)/3 < σ₁ ⇔ θ₂ < (3σ₁ − 2)/4. ✓ after the fix.

**1.5 Remark 1.5, l. 81–84 — ✓.** s40 Cor. 1.7(iii) needed F_X(σ₁) > ½X^{−σ₁}; Theorem 1.3 needs F_X(σ₁) ≥ 0 at a lattice X. The gain
½X^{−σ₁}/|F′_X(σ₁)| is 4.59·10⁻⁸ at x_K ≈ 10⁸ (π/16; F′ = −4.78044) and 1.18·10⁻⁹ at 10¹⁰ [computed: `gain_O.py`, `logs/gain_pi16.log`].

**1.6 Proposition 1.6, l. 86–97.** (i) **✓ with one correction of scope.** F_{x_{k+1}}(σ) − F_{x_k}(σ) = σ∫_{x_k}^{x_{k+1}}E u^{−σ−1}du ≥
σ∫_{x_k}^{x_{k+1}}s(u)u^{−σ−1}du > 0 for σ > 0 — but both F's have a pole at σ = 1, so "for every σ > 0" must read "σ > 0, σ ≠ 1"
(the difference itself is entire, and at s = 1 it equals ∫_{x_k}^{x_{k+1}}E u^{−2}du > 0). Observed on data at every decade: F_{x_K}(0.79)
= 0.0222186866, 0.0222313187, 0.0222337969, 0.0222342698, 0.0222343584 for x_K ≈ 10⁶…10¹⁰ (π/16), and F_{x_K}(0.89) = 0.0434248213,
…, 0.0434265820 (π/32) [computed: `logs/certify_*.log`]. (ii) **✓** (strictly increasing, tail → 0 by absolute convergence; σ ≠ 1).
(iii) **✓ as stated, with σ* = the FIRST zero right of σ_a** (s_k needs the convention sup ∅ := σ_a for the finitely many k with
F_{x_k}(σ_a) ≤ 0). **GAP (statement after the proof, l. 99–100, and §0 l. 25–26, 30–31):** "Under (B), a real-zero certificate for
S8(ρ) can never pass σ*" is proved only for σ* := the LARGEST real zero of ζ_P in (θ′, 1) — which is what §7.2 uses ("ζ_P ≠ 0 on
(σ*, 1)"). With the σ* of (iii) it is unproved: if ζ_P had three real zeros (with multiplicity) in (σ_a, 1), F_{x_k}(σ) > 0 at a
σ between the second and third would be a valid certificate past the first. Nothing proved excludes this; Theorem 6.2 places
every real zero right of σ₁ in (σ₁, σ₂) under a tail hypothesis, but it does not give uniqueness (the NOTE says so, l. 311–312).
Fix: name the two objects — σ*_first = lim s_k (Prop. 1.6(iii)) and σ*_max = the ceiling (§7.2) — and write §0's "increase to the
real zero σ*" as "increase to σ*_first", the ceiling as σ*_max. The certificates themselves are untouched.

**1.7 Lemma 6.1 (tail bounds), l. 267–276 — ✓.** (a) I_n := ∫_X^∞log^n u·u^{−σ−1}du, I_0 = X^{−σ}/σ, I_n = X^{−σ}L^n/σ + (n/σ)I_{n−1} (by
parts), so σI_2 = σX^{−σ}(L²/σ + 2L/σ² + 2/σ³) = X^{−σ}(L² + 2L/σ + 2/σ²) = τ_X. (b) σ∫_X^∞C u^{ϑ−σ−1} = CσX^{ϑ−σ}/(σ − ϑ). (c) On
[Y, 2Y]: ∫|E|u^{−σ−1} ≤ Y^{−σ−1}Y^{1/2}(C²Y^{1+2ϑ})^{1/2} = CY^{ϑ−σ}; Y = 2^mX, m ≥ 0: σCX^{ϑ−σ}/(1 − 2^{ϑ−σ}). Each is an UPPER bound
on the tail using only an upper bound on E (σu^{−σ−1} > 0). Continuation: with E > −½ and E bounded on [1, X], (a) gives (B) for
every θ > 0, (b) gives (B) with exponent max(ϑ, 0), (c) gives (B₂) with θ₂ = ϑ; Theorem 1.3 at σ₁ then needs ϑ < σ₁, true for the
rows used (ϑ = σ₁/2 truncated). ✓

**1.8 Lemma 6.3 (concavity), l. 280–290 — ✓, numbers reproduced independently.** d²/dσ²[σu^{−σ−1}] = u^{−σ−1}(σ log²u − 2 log u)
and ζ_c″ = −2ρ/(1 − σ)³ ≤ −2ρ/(1 − σ_a)³ on [σ_a, 1); |σ log²u − 2 log u| ≤ log²u + 2 log u and u^{−σ−1} ≤ u^{−σ_a−1}; |E| ≤ E + 1
since E ≥ −½; ∫_1^∞u^{−σ−1}(2 log u + log²u) = 2/σ² + 2/σ³. So Q ≤ 2A_1 + A_2 + 2/σ_a² + 2/σ_a³. My evaluation of A_m by a
different route (A_m = Σ_{n≤X}G_m(n) − N(X)G_m(X) − ∫_1^X T u^{−σ−1}log^m u, G_m(y) := ∫_y^∞u^{−σ−1}log^m u; per block a first-order
expansion of G_m with a proved second-order remainder; closed form for the T-integral) [computed: `concavity_O.py`, logs
`concavity_pi{16,32}_1e10.log`]: A_0 = −0.0545312, A_1 = 0.081589, A_2 = 0.5887 at σ_a = 0.794755370097 (π/16), Q ≤ 7.90238 ± 10⁻⁵
< 45.4197; π/32: A = (−0.0718601, −0.0269554, 0.155384), Q ≤ 5.38685 < 169.985. Self-test A_0 = (F_X − ζ_c)/σ to 10⁻⁸. The step
"F(σ₁) > 0 > F(σ₁ + 10⁻¹²) ⇒ exactly one zero, strictly decreasing on [σ₁ + 10⁻¹², 1)" is the secant property of concave functions. ✓

**1.9 Theorem 6.2 (the zero boxed), l. 292–312 — ✓, table reproduced digit for digit.** Monotonicity of the bounds: τ_X =
X^{−σ}(L² + 2L/σ + 2/σ²) is a product of positive decreasing factors; for (b), d/dσ log[σX^{ϑ−σ}/(σ − ϑ)] = 1/σ − L − 1/(σ − ϑ) has the
sign of −ϑ − σL(σ − ϑ) < 0; for (c), σX^{ϑ−σ} decreases once σL > 1 (L = 23.03) and 1/(1 − 2^{ϑ−σ}) decreases. With F_X decreasing on
[σ₂, 1) (1.8; σ₂ − σ₁ ≥ 7·10⁻⁹ > 10⁻¹²): ζ_P ≤ F_X + bound < 0 on [σ₂, 1), ζ_P(σ₁) > 0, so every real zero right of σ₁ is in (σ₁, σ₂)
and their number with multiplicity is odd. All fourteen σ₂ of the table recomputed with my own F_X and bounds, each the smallest
9-decimal point with F_X + bound < 0 proved and > 0 proved one step below [computed: `bracket_O.py`, logs
`bracket_pi{16,32}_1e10.log`]: π/16 0.794755510, 0.794756766, 0.794769322, 0.794894399, 0.794799754, 0.798716538, 0.794828566;
π/32 0.895076525, 0.895076591, 0.895077248, 0.895083814, 0.895083982, 0.895805019, 0.895089041 — identical to the NOTE.

**1.10 §7.1 (what is left) — ✓.** From my certified brackets (§2): σ₁/2 = 0.3973776850486900… (π/16), 0.4475382587960800… (π/32),
0.4738170951117875… (π/64), 0.4871322811644820… (π/128) and (3σ₁ − 2)/4 = 0.0960665275730350…, 0.1713073881941200…,
0.2107256426676812…, 0.2306984217467230…; every truncated threshold of l. 317–321 lies below the corresponding value. ✓ "Nothing in
this unit bounds E from above" — correct; the data statement "E = O(log²x) to 10¹⁰" is an observation, not a bound.

**1.11 §7.2 (ceiling), l. 326–332 — ✓ as stated there** (σ* is defined there as a zero with ζ_P ≠ 0 on (σ*, 1), i.e. σ*_max; under
(B) or (B₂) the real zeros in [σ₁, 1) are finitely many — ζ_P is analytic on (θ′, 1), not ≡ 0, and → −∞ at 1⁻ — so σ*_max exists
once ζ_P(σ₁) > 0). The numerical corollary (l. 331–332: within 1.4·10⁻⁷ and 7.4·10⁻⁹ of the ceiling; exponents relaxable by at most
7·10⁻⁸ and 3.7·10⁻⁹) is (σ₂ − σ₁) and (σ₂ − σ₁)/2 for the 0.1·log²u row: 1.399·10⁻⁷/2 = 7.0·10⁻⁸ and 7.41·10⁻⁹/2 = 3.7·10⁻⁹. ✓,
conditional on E(u) ≤ 0.1 log²u beyond X, as the NOTE says. "Two ways past the ceiling" (l. 333–335) is a correct description;
(a) quotes s40's exploratory winding count, which I did not re-check.

**1.12 §0 summary claims.** l. 10–21: the two theorems and the thresholds — ✓ (numbers in §2). l. 16–18: "1.51·10⁹ and 5.7·10⁸ cell
decisions" — these include the composites of (x_K, 10¹⁰] (1 and 2 of them; §3), my composite counts to x_K are 1,513,583,580 and
572,359,631. l. 22–26: ✓ with the σ ≠ 1 and σ*_first/σ*_max corrections of 1.6. l. 27–29: ✓ (1.9). l. 30–32: ✓ for σ*_max (1.6,
1.11). l. 33–37: the cross-check statements are about the first producer's own runs; my counts confirm every number quoted there
that I could produce (§3).

## §2. The second certificate (own generator, own evaluator; `verify-O/`)

**2.0 Decision rule (no floating point in any decision)** [proved here]. A composite c = x_{n_1}⋯x_{n_j} (j ≥ 2) has, with
b_i := 2n_i − 1 (odd) and E_r := e_r(b_1, …, b_j) ∈ ℤ_{>0} (elementary symmetric functions), x_{n_i} = 1 + b_i t/2, hence
c = Σ_{r≥0}E_r(t/2)^r and **W(c) := ρ(c − 1) + ½ = (E_1 + 1)/2 + Σ_{r=2}^{j}E_r κ_r, κ_r := t^{r−1}/2^r.** The cell of c is
m = ⌊W(c)⌋ + 1 (x_{m−1} < c < x_m ⇔ m − 1 < W < m). With K_r := ⌊κ_r 2^90⌋ and the certified STRICT K_r < κ_r2^90 < K_r + 1
(no transcendence used; a composite exactly on a lattice point would only make the 320-bit path stop, and that path never ran):
2^90·W(c) ∈ (H_lo, H_lo + Σ_{r≥2}E_r), H_lo := (E_1 + 1)2^89 + Σ_{r≥2}E_rK_r — exact unsigned 128-bit integers (E_rK_r ≤ 2^90 W(c) <
2^122 for every product evaluated; a double guard skips products above twice the segment end). The cell is decided iff both ends
have the same integer part; otherwise a 320-bit path recomputes E_r from the factor list and uses KH_r := ⌊κ_r 2^320⌋ in 6-limb
integers (the program stops if that straddles too). Integer checkpoints V use ⌊w(V)2^90⌋ and ⌊w(V)2^320⌋ the same way.
*Constants* [computed: `consts.py`, header lines of each `logs/gen_*.log`]: every K_r, KH_r and checkpoint floor is certified twice
and the two must agree: arb at 1200 bits (ball strictly inside (k, k + 1)), and exact rationals from a Machin enclosure
π ∈ [16L(1/5) − 4U(1/239), 16U(1/5) − 4L(1/239)] (L, U consecutive partial sums of the alternating arctan series; width < 2^−1300).
*Per composite* (prefix g, last factor b): E_r(gq) = E_r(g) + bE_{r−1}(g), so H_lo = (E_1(g) + b + 1)2^89 + A_g + b·B_g with
A_g = Σ_{r≥2}E_r(g)K_r, B_g = Σ_{r≥2}E_{r−1}(g)K_r precomputed per prefix: one 64×128 multiply per decision.
**Enumeration** [proved here]. Cells are processed in segments [m₀, m₁), m₁ ≤ 2m₀ + 1, 2^27 cells at most. Causality: a composite
in a cell ≤ 2m₀ is < x_{2m₀} < p₁x_{m₀} (the difference is (m₀ − ½)t(t/2 − 1) > 0 for t > 2), so each of its prime factors is
< x_{m₀}, i.e. already placed. Each multiset of ≥ 2 stored g-primes is visited once as prefix × last factor with non-decreasing list
index; the last-factor range starts at a binary-search point computed in doubles with relative slack 10⁻⁹ (only conservative), the
exact cell decides membership, and the loop stops at the first exact cell ≥ m₁ (cells are monotone in the last factor). Prefixes are
extended only while g·q² ≤ x_{m₁−1}(1 + 10⁻⁹) (conservative). Then the cells are swept: N(x_m−) = N(x_{m−1}) + c_m (+1 in cell 1 for
the g-integer 1); a g-prime at x_m iff N(x_m−) = m; the program stops if N(x_m−) < m (never). Stored g-primes: lattice index
≤ ⌊w(x_K/p₁)⌋ + 16, enough for every composite ≤ x_K.
**Validation** [computed: `validate_small.sh`, `brute.py`, `logs/validate_small.log`]. At X = 2·10⁵ a definition-level brute
force (mpmath 60 digits; min-heap of g-integer values; a g-prime at x_m iff the count below x_m equals m; tie check 10⁻⁴⁰; no
symmetric functions, no fixed point) gives the cell of every composite: identical for all 23,187 (π/16) and 7,293 (π/32) composites,
identical g-prime lists, identical counts at V = 10³…10⁵. Segments of 16 cells, and the exact path forced on every decision with
fast-path margin < 2⁻³ (6,040 and 1,948 decisions through the 320-bit path), give byte-identical moment files.

**2.1 Evaluation of F_X** [proved here: the bounds; computed: `feval_O.py`]. For cells < 2^16 every g-integer is a ball
n = 1 + (W − ½)t, W ∈ [H_lo, H_hi]·2^−90. For cells in [2^j, 2^{j+1}), j ≥ 16, blocks of L = 2^{j−14} cells with centre W₀ (integer)
store exact integer sums of Δ = W − W₀: count; S₁ ∈ [Σ⌊2^64Δ_lo⌋, Σ(⌊2^64Δ_hi⌋ + 1)]·2^−64; S₂ = ΣD₂²·2^−64 ± (4Σ|D₂| + 4·cnt)·2^−64 with
D₂ = ⌊2^32Δ_lo⌋ (since 2^32Δ ∈ [D₂, D₂ + 2)); S₃ = ΣD₃³·2^−48 ± (6ΣD₃² + 12Σ|D₃| + 8·cnt)·2^−48 with D₃ = ⌊2^16Δ_lo⌋. With λ = W₀ − ½ + ρ,
g₀ = tλ, δ = Δ/λ, |δ| ≤ h := (L/2)/λ ≤ 2^−15 (λ ≥ 2^j): Σ_block n^{−σ} = g₀^{−σ}[cnt + c₁S₁/λ + c₂S₂/λ² + c₃S₃/λ³ + R],
c_k = C(−σ, k), |R| ≤ cnt·|c₄|h⁴(1 − h)^{−σ−4} (Lagrange). F_X = Σ + ρX^{1−σ}/(σ − 1) − E(X)X^{−σ}, X = 1 + (K − ½)·D/π, E(X) = N(X) − K − ½,
arb at 256 bits, σ an exact rational. Total proved error at 10¹⁰: ≤ 6·10⁻¹⁷ (π/16), ≤ 7·10⁻¹⁸ (π/32). *Check:* at x_K ≈ 10⁷ (π/16) the
moment evaluation F(0.79) = 0.02223131872339904 ± 4.2·10⁻¹⁸ contains the direct ball sum over all 1,963,496 g-integers,
0.022231318723399041112 ± 2·10⁻²² (`fdirect.py` over the s8gen dump; `logs/fdirect_pi16_1e7.log`). Certified constants: `data/params_pi{16,32,64,128}_1e10.txt`.

**2.2 Statements proved** [computed: the inequalities, `logs/gen_pi{16,32}_1e10.log`, `logs/certify_pi{16,32}_1e10.log`; proved here:
the implications, by NOTE Theorem 1.3 and Corollary 1.4 as re-derived in §1].
**Theorem O.1 (S8(π/16)).** K = 1,963,495,408, X = x_K = 9,999,999,995.939530952…: N_P(X) = 1,963,495,409, π_P(X) = 449,911,828,
E(X) = ½, and **F_X(0.794755370097380) = (2.6 ± 0.04)·10⁻¹⁵ > 0**, F_X(0.794755370097381) = (−2.2 ± 0.03)·10⁻¹⁵ < 0. So (B) or (B₂)
with an exponent < 0.794755370097380 gives a real zero in (0.794755370097380, 1), and (B) with θ ≤ 0.397377685048690 (or (B₂) with
θ₂ ≤ 0.096066527573035) refutes U.
**Theorem O.2 (S8(π/32)).** K = 981,747,704, X = 9,999,999,993.393…: N = 981,747,705, π_P = 409,388,073, E = ½,
**F_X(0.895076517592160) = (8.78 ± 0.01)·10⁻¹⁵ > 0**, F_X(0.895076517592161) = (−1.9 ± 0.02)·10⁻¹⁶ < 0; thresholds θ ≤ 0.447538258796080,
θ₂ ≤ 0.171307388194120.
**At the NOTE's σ₁, my X:** F_X(0.794755370097) = (1.8192 ± 0.0001)·10⁻¹², F_X(0.794755370098) = −2.9613·10⁻¹²; F_X(0.895076517592) =
1.44325·10⁻¹², F_X(0.895076517593) = −7.52222·10⁻¹² (same X as the NOTE; its (2.0 ± 0.6)·10⁻¹² and (1.4 ± 0.1)·10⁻¹² contain mine).

**2.3 σ₁ at every decade** (zero of F_{x_K}, K = ⌊ρ(10^d − 1) + ½⌋, bracketed to 10⁻¹⁵; each bracket proved at both ends):

| X ≈ | π/16 | π/32 |
|---|---|---|
| 10⁶ | (0.794752301959441, …442) | (0.895076334603972, …973) |
| 10⁷ | (0.794754781368432, …433) | (0.895076489528701, …702) |
| 10⁸ | (0.794755262462011, …012) | (0.895076513462146, …147) |
| 10⁹ | (0.794755353284414, …415) | (0.895076517060808, …809) |
| 10¹⁰ | (0.794755370097380, …381) | (0.895076517592160, …161) |

Addendum (§5.4 of the NOTE): π/64, K = 490,873,852, N = 490,873,853, π_P = 310,847,297, zero in (0.947634190223575, …576);
π/128, K = 245,436,926, N = 245,436,927, π_P = 196,463,063, zero in (0.974264562328964, …965) [computed: same programs].

**2.4 Checkpoints, count for count** [computed: `logs/gen_pi{16,32}_1e10.log`, `checkpoints_O.py`, `logs/checkpoints_O.log`].
V = ⌊10^{h/2}⌋; N(V), π_P(V) exact (every composite in V's cell compared with V by the certified enclosure of w(V));
E(V) = N(V) − ρ(V − 1) − 1 (arb, 10 digits). Also on the record there: N and E at the lattice point just below each V.

| V | N(V) π/16 | π_P(V) π/16 | E(V) π/16 | N(V) π/32 | π_P(V) π/32 | E(V) π/32 |
|---|---|---|---|---|---|---|
| 1,000 | 198 | 118 | 0.8468086915 | 99 | 75 | -0.07659565426 |
| 3,162 | 622 | 340 | 0.3391013752 | 311 | 232 | -0.3304493124 |
| 10,000 | 1,964 | 990 | -0.2990589528 | 983 | 700 | 0.3504705236 |
| 31,622 | 6,211 | 2,888 | 1.231168802 | 3,105 | 2,106 | -0.3844155988 |
| 100,000 | 19,637 | 8,415 | 1.242264605 | 9,818 | 6,350 | -0.3788676977 |
| 316,227 | 62,092 | 24,680 | 0.1700953696 | 31,047 | 19,139 | 0.5850476848 |
| 1,000,000 | 196,350 | 72,603 | -0.3444998212 | 98,177 | 57,724 | 1.327750089 |
| 3,162,277 | 620,914 | 214,016 | 1.559361043 | 310,457 | 174,263 | 0.2796805213 |
| 10,000,000 | 1,963,496 | 633,514 | -0.2121440799 | 981,749 | 526,606 | 0.3939279600 |
| 31,622,776 | 6,209,119 | 1,879,642 | 0.6483673141 | 3,104,560 | 1,592,734 | 0.3241836571 |
| 100,000,000 | 19,634,955 | 5,593,120 | 0.1114133331 | 9,817,480 | 4,822,578 | 2.055706667 |
| 316,227,766 | 62,091,178 | 16,689,630 | 0.5384300286 | 31,045,590 | 14,616,923 | 0.7692150143 |
| 1,000,000,000 | 196,349,548 | 49,924,829 | 6.346987463 | 98,174,771 | 44,345,886 | -0.3265062683 |
| 3,162,277,660 | 620,911,771 | 149,701,129 | 3.617154418 | 310,455,884 | 134,673,637 | -0.1914227909 |
| x_K | 1,963,495,409 | 449,911,828 | 0.5 | 981,747,705 | 409,388,073 | 0.5 |

**2.5 Run data** [computed: `run_gen.sh`, `logs/gen_*.log`; Apple arm64, one core]. π/16 to x_K: 1,513,583,580 composites (= N − 1 − π_P),
up to 18 factors, 0 exact-path decisions (cell and checkpoint), 73 s, 0.85 GB; π/32: 572,359,631 composites, up to 12 factors,
0 exact-path decisions, 29 s, 0.60 GB. Closest decisions (lower bounds of |W(c) − lattice|): π/16 c = x(1)x(2)x(13)x(533658) in cell
1,057,291,198, margin > 3.0205·10⁻¹¹ in W (1.5383·10⁻¹⁰ in u); π/32 c = x(1)x(33405216), cell 203,536,582, > 1.6626·10⁻¹⁰ in W
(1.6935·10⁻⁹ in u) — against fast-path enclosure widths ≤ 2^−50, which is why no decision needed the 320-bit path.
max_m E(x_m) = 25.5 (m = 1,266,139,765) and 14.5 (m = 645,060,223): the lattice values only, a lower bound for sup E.
Moment files (35 MB each, kept in the scratch directory `/private/tmp/rh-s41-U6-second/`, not in the repo; `run_gen.sh` regenerates them deterministically in about a minute, and the sha256 in each log identifies them): `m_pi16_1e10.blk` ae402998…c574, `m_pi32_1e10.blk` 32e42d7d…611d.

## §3. Comparison with the first producer (done after §2 was final; `verify/` logs read as data, its code read only to explain two counters)

**Counts — identical everywhere.** All 14 checkpoints V = ⌊10^{h/2}⌋, 10³ ≤ V ≤ 10^9.5, both densities: my N(V) and π_P(V) equal the
first producer's and s8o's (`verify/logs/crosscheck_pi{16,32}.log`) — 56 integers, 0 mismatches. At x_K: N, π_P, e_K equal for π/16,
π/32, π/64, π/128. E(10^d) from s8o (−0.3445, −0.212144, 0.111413, 6.346987 for π/16; 1.32775, 0.393928, 2.055707, −0.326506 for
π/32) equal my E(V) to every printed digit (§2.4). max_m e_m = 25 and 14, = its "maxe". Two counters differ, both explained:
(i) its "decisions" 1,513,583,581 and 572,359,633 exceed my composite counts to x_K by 1 and 2 — its emission bound is
x_K(1 + 2⁻³⁰) (`s8cert.c` l. 22, l. 359), so it also decides the 1 and 2 composites in (x_K, 10¹⁰] that the NOTE §4 uses to explain
N(10¹⁰) − N(x_K); (ii) its stored g-primes 134,178,740 and 71,517,727 exceed mine (134,178,606; 71,517,665) because its storage cap is
X/p₁·(1 + 10⁻⁶) (l. 361) and mine is the lattice index of x_K/p₁ plus 16: a parameter, not a property of S8.
**Closest decisions — identical.** Same composites, same cells, same margins: x(533658)x(13)x(2)x(1), k = 1,057,291,198, x_k − c =
1.53831·10⁻¹⁰ (its 80-digit recheck) vs my fast-path lower bound 1.538307·10⁻¹⁰; x(33405216)x(1), k = 203,536,582, 1.6935·10⁻⁹.
**F_X — mine inside every one of its balls.**

| quantity | first producer (ball) | read-O (ball radius ≤ 6·10⁻¹⁷) |
|---|---|---|
| π/16, F_{x_K}(0.794755370097) | 2e-12 ± 5.79e-13 | 1.8192e-12 |
| π/16, F_{x_K}(0.794755370098) | −3e-12 ± 4.17e-13 | −2.9613e-12 |
| π/32, F_{x_K}(0.895076517592) | 1.4e-12 ± 6.43e-14 | 1.44325e-12 |
| π/32, F_{x_K}(0.895076517593) | −7.5e-12 ± 4.48e-14 | −7.52222e-12 |
| π/64, F_{x_K}(0.947634190223) / (…224) | 1.030e-11 ± 6.5e-15 / −7.59e-12 ± 7.2e-15 | 1.0303392e-11 / −7.585906e-12 |
| π/128, F_{x_K}(0.974264562328) / (…329) | 3.572e-11 ± 1.6e-15 / −1.31e-12 ± 1.7e-15 | 3.5719323e-11 / −1.309126e-12 |
| π/16 at 10⁷: F(0.78), F(0.79), F(0.80), F(0.81) | 0.0659546434367, 0.0222313187234, −0.0257111582844, −0.0785447458226 (± ≤ 7·10⁻¹⁴) | 0.06595464343671125, 0.02223131872339904, −0.02571115828437418, −0.07854474582261392 |

**σ₁ per decade.** Its 12-decimal σ₁ (largest with F > 0 proved) equals the 12-decimal truncation of my lower bracket end at 9 of the
10 entries; at π/16, 10⁸ it is 0.794755262461 against my zero 0.794755262462011…, i.e. its value is a correct lower bound, one unit
of 10⁻¹² lower because its ball (± 2.7·10⁻¹³) cannot prove F(0.794755262462) = +5.439·10⁻¹⁴ > 0 (`logs/check_pi16_1e8_note_entry.log`) — its own log says so
("F_X(sigma_1+1e-12)<0 proved? False"), but the NOTE's §4 heading calls every entry "the zero of F_{x_K} to 10⁻¹²" (§4 below).
**§6 numbers.** All 14 σ₂ identical (§1.9). Lemma 6.3: its A_1 = 0.0815893397, A_2 = 0.588730803, Q ≤ 7.902383680 (π/16) and
A_1 = −0.02695538982, A_2 = 0.1553843823, Q ≤ 5.386854069 (π/32) lie inside my balls (§1.8), obtained by a different expansion.
**Methods compared.** Ordering: it uses doubles with a proved relative error bound and a GMP/Machin fallback (4,726 and 785 fallbacks);
mine uses no floating point in any decision (integer symmetric functions × certified integer constants) and needed no fallback.
Evaluation: it stores power sums of the computed double positions in 256 blocks per octave, 7 moments, plus a position-error term
P_b ≈ 4Ωu per term, which dominates its radius (≈ 6·10⁻¹³); mine stores integer moments of the exactly enclosed lattice coordinate
W (width ≤ 2⁻⁵⁰), 2¹⁴ blocks per octave, 4 moments, so its radius (≤ 6·10⁻¹⁷) is set by the Taylor remainder alone. The agreement is
therefore between two independent decision procedures and two independent evaluations.

## §4. Corrections (OLD quoted exactly from the NOTE; none affects a certificate or a threshold)

C1 (Cor. 1.4(b), l. 77 — GAP, §1.4):
OLD: (a larger H only strengthens the bound: |E| ≥ H/2 on all of [x, 2x] or [x/2, x])
NEW: (if E(x) = H with ρx < H ≤ 2ρx the window [x, x + H/(2ρ)] still lies in [x, 2x]; if H > 2ρx then E ≥ H − ρ(u − x) ≥ H/2 on all of [x, 2x], which gives the stronger H ≪ x^{θ₂}; and E(x) = −H forces H < ρx, since N ≥ 1 gives E ≥ −ρ(x − 1))

C2 (Prop. 1.6(i), l. 87 — scope, §1.6):
OLD: (i) *Unconditionally*, for every σ > 0 and k ≥ 1: F_{x_{k+1}}(σ) > F_{x_k}(σ).
NEW: (i) *Unconditionally*, for every σ > 0 with σ ≠ 1 and every k ≥ 1: F_{x_{k+1}}(σ) > F_{x_k}(σ) (at σ = 1 both have a pole; their difference is entire and equals ∫_{x_k}^{x_{k+1}}E u^{−2}du > 0 there).

C3 (after Prop. 1.6, l. 98 — which zero, §1.6):
OLD: So the computed σ₁(X) of §4–§5 is (up to the interval radius) the sequence s_k, increasing toward the real zero; Theorem 5.1/5.2 and
NEW: So the computed σ₁(X) of §4–§5 is (up to the interval radius) the sequence s_k, increasing toward σ*_first, the smallest real zero of ζ_P right of σ_a (the only one, if it is unique — not proved); Theorem 5.1/5.2 and

C4 (l. 99 — the ceiling is the LARGEST real zero, §1.6, §1.11):
OLD: the table in §4 are its values at x_K ≈ 10⁶ … 10¹⁰. Under (B), a real-zero certificate for S8(ρ) can never pass σ*, so this route
NEW: the table in §4 are its values at x_K ≈ 10⁶ … 10¹⁰. Under (B), a real-zero certificate for S8(ρ) can never pass σ*_max, the largest real zero of ζ_P in (θ′, 1) (§7.2; it can pass σ*_first if ζ_P has three or more real zeros there, which is not excluded), so this route

C5 (§0, l. 26):
OLD: σ₁(x_k) increase to the real zero σ*.
NEW: σ₁(x_k) increase to σ*_first, the smallest real zero right of σ_a (Prop. 1.6(iii)).

C6 (§0, l. 30):
OLD: **Ceiling (§7.2)** [proved here]: under (B), no real-zero certificate can pass σ*, so this proof class cannot relax the exponent of
NEW: **Ceiling (§7.2)** [proved here]: under (B), no real-zero certificate can pass σ*_max, the largest real zero of ζ_P in (θ′, 1), so this proof class cannot relax the exponent of

C7 (§4, l. 199 — one table entry is not the zero to 10⁻¹², §3):
OLD: to 10⁻¹²) against the s8o zero of F_{10^d} (10 digits) and the s8dd root (12 digits):
NEW: to 10⁻¹², except π/16 at 10⁸, where the zero is 0.794755262462011… [read-O §2.3] and the entry is a valid lower bound 1.01·10⁻¹² below it — `sigma_table_pi16.log` marks that row "False") against the s8o zero of F_{10^d} (10 digits) and the s8dd root (12 digits):

C8 (§5, l. 245 — last π/32 increment, from 15-digit zeros [read-O §2.3]):
OLD: (π/16; ratios 5.15, 5.30, 5.40) and by 1.55·10⁻⁷, 2.39·10⁻⁸, 3.60·10⁻⁹, 5.32·10⁻¹⁰ (π/32; ratios 6.47, 6.65, 6.76), as the tail
NEW: (π/16; ratios 5.15, 5.30, 5.40) and by 1.55·10⁻⁷, 2.39·10⁻⁸, 3.60·10⁻⁹, 5.31·10⁻¹⁰ (π/32; ratios 6.47, 6.65, 6.77), as the tail

## §5. Additions

**A1 (a floating-point-free cell test)** [proved here, §2.0]. For any S8(ρ): W(x_{n_1}⋯x_{n_j}) = (E_1 + 1)/2 + Σ_{r≥2}E_r t^{r−1}/2^r with
E_r the elementary symmetric functions of the odd integers 2n_i − 1. So every ordering question of S8 against the lattice is the
fractional part of an integer combination of the fixed constants t^{r−1}/2^r; with ⌊2^90 t^{r−1}/2^r⌋ certified once, a decision costs
one 64×128-bit multiply and is exact unless the margin is below Σ_{r≥2}E_r·2⁻⁹⁰ ≤ 2⁻⁵⁰ (never, to 10¹⁰; the closest margins are
3.0·10⁻¹¹ and 1.7·10⁻¹⁰). Any later unit can reuse `verify-O/s8gen.c` (73 s to 10¹⁰ for π/16, one core).
**A2 (the zeros of F_{x_K} to 15 decimals)** [computed, §2.3]: π/16 0.794755370097380 < z < 0.794755370097381; π/32 0.895076517592160 <
z < …161; π/64 0.947634190223575 < z < …576; π/128 0.974264562328964 < z < …965. Hence the exact U-thresholds from these certificates
(Corollary 1.4 with equality allowed, §1.4): θ ≤ 0.397377685048690, 0.447538258796080, 0.473817095111787, 0.487132281164482; θ₂ ≤
0.096066527573035, 0.171307388194120, 0.210725642667681, 0.230698421746723 (each the value at the lower bracket end).
**A3 (non-strict exponents suffice)** [proved here, §1.4]: θ = σ₁/2 and θ₂ = (3σ₁ − 2)/4 themselves already refute U, because α ≥ σ* > σ₁.
**A4 (two zeros, two roles)** [proved here, §1.6]: σ*_first = lim s_k is what the computation approaches; σ*_max is the ceiling of the
certificate route. They coincide iff ζ_P has a single distinct real zero in (σ_a, 1) (a double zero followed by a sign change would separate them); under
E ≤ 0.1·log²u beyond 10¹⁰ both lie in (σ₁, σ₂), an interval of length 1.4·10⁻⁷ (π/16) and 7.4·10⁻⁹ (π/32).
**A5 (monotonicity on data)** [computed]: F_{x_K}(σ) increases with K at every decade for σ = 0.79, the NOTE's σ₁ (π/16) and 0.89,
the NOTE's σ₁ (π/32) — Prop. 1.6(i) seen on 20 values (§1.6); F_{x_K}(σ₁^NOTE) < 0 at every X ≤ 10⁹ (e.g. −5.15·10⁻⁷ at 10⁸ for π/16),
as the monotone sequence requires.
**A6 (Lemma 6.3 at the small densities)** [computed: `logs/concavity_pi{64,128}_1e10.log`]: Q ≤ 4.31611 < 683.686 (π/64), 3.96687 <
2879.89 (π/128) — the NOTE's 4.32 and 3.97 reproduced.

## §6. What I could not check

- s40's exploratory winding count (NOTE l. 334–335, "no zero right of σ* below height 60") — not re-run; it is quoted there as not
  a certificate, and nothing proved depends on it.
- The NOTE's floating-point lemmas (Lemma 2.1, Lemma 3.1–3.2) were not re-derived line by line: my decisions and my evaluation do not
  use them, and every number they produce was reproduced by the independent route, so they are no longer load-bearing for any result.
- sup E to 10¹⁰ (26.137, 15.434): my generator records only lattice values (max E(x_m) = 25.5, 14.5, consistent lower bounds); the
  in-cell supremum needs the order of composites inside a cell, which I did not keep.
- Trust base of my certificate: python-flint 0.6.0 / Arb ball arithmetic (rigorous by design [recalled, unverified]), the C compiler
  and one Apple arm64 machine. Mitigations on disk: every integer constant certified twice (Arb and exact Machin rationals); the
  generator agrees cell by cell with a 60-digit mpmath brute force at 2·10⁵ and count for count with two other generators (s8o, s8cert)
  to 10^9.5; the moment evaluation agrees with a direct ball sum over all 1,963,496 g-integers at 10⁷.
- Uniqueness or simplicity of the real zero in (σ₁, σ₂) — not proved by the NOTE nor here (A4).

