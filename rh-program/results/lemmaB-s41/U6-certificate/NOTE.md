# NOTE — unit `lemmaB-s41/U6-certificate`: interval certificates for the real zero of S8(π/16) and S8(π/32)

Started 17:04 IST 2026-10-01. Writer: Opus 5.5 (agent). Labels as in `../CHARTER.md` §4: **[proved here]**, **[computed]**
(script + log in `verify/`), **[quoted]** (source opened at the line), **[recalled, unverified]** (never load-bearing).
Notation as in `free-greedy-s40/theory/NOTE.md` (cited below as s40-NOTE): t = 1/ρ, lattice points x_k = 1 + (k − ½)t,
T(u) = ρ(u − 1) + 1, E = N − T, w(u) := ρ(u − 1) + ½ (so w(x_k) = k), F_X(s) = Σ_{n≤X} n^{−s} + ρX^{1−s}/(s − 1) − E(X)X^{−s}.

## §0. Close

(filled last)

## §1. A sharper finite criterion: the sawtooth floor

**Lemma 1.1 (sawtooth floor)** [proved here]. For S8(ρ), any ρ ∈ (0, 1], and all u ≥ 1: E(u) ≥ ½ − {w(u)}.
*Proof.* E(u) = N(u) − ρ(u − 1) − 1 = N(u) − w(u) − ½. By s40-NOTE Lemma 1.1 [quoted: s40-NOTE l. 61–64, dual-read], E(u) > −½,
i.e. N(u) > w(u). N(u) is an integer, so N(u) ≥ ⌊w(u)⌋ + 1 and E(u) ≥ ⌊w(u)⌋ + ½ − w(u) = ½ − {w(u)}. ∎
(At a lattice point the floor is E(x_k) ≥ ½, i.e. e_k ≥ 0; just before it, −½. The floor has mean 0 over each period.)

**Lemma 1.2 (the tail beyond a lattice point is positive)** [proved here]. Let X = x_K (K ≥ 1), 0 < σ < 1, and assume
∫_X^∞ |E(u)|u^{−σ−1}du < ∞. Then σ∫_X^∞ E(u)u^{−σ−1}du ≥ σ∫_X^∞ (½ − {w(u)})u^{−σ−1}du > 0.
*Proof.* The first inequality is Lemma 1.1 times σu^{−σ−1} > 0. The floor is bounded by ½, so its integral converges absolutely
and may be split over the periods [x_k, x_{k+1}), k ≥ K. On such a period w(u) − k = ρ(u − x_k) ∈ [0, 1), so the floor equals
½ − ρ(u − x_k). With m_k := (x_k + x_{k+1})/2 and u = m_k ∓ v, 0 < v ≤ t/2, the floor takes the values ±ρv, so
∫_{x_k}^{x_{k+1}}(½ − {w})u^{−σ−1}du = ∫_0^{t/2} ρv[(m_k − v)^{−σ−1} − (m_k + v)^{−σ−1}]dv > 0, because u ↦ u^{−σ−1} is strictly
decreasing. A convergent sum of positive terms is positive. ∎

**Theorem 1.3 (finite criterion at a lattice point)** [proved here]. Let P = S8(ρ), ρ ∈ (0, 1), X = x_K (K ≥ 1), and σ₁ ∈ (0, 1)
with F_X(σ₁) ≥ 0. Assume one of
  (B) N_P(u) − ρu = O(u^θ) for some θ < σ₁ (any implied constant), or
  (B₂) ∫_Y^{2Y} E(u)²du = O(Y^{1+2θ₂}) for all Y ≥ 1, some θ₂ < σ₁ (the mean-square form of `../ORCH-NOTES.md` O1).
Then ζ_P(σ₁) > 0, ζ_P has a real zero σ* ∈ (σ₁, 1), and ψ_P(x) − x ≠ O(x^a) for every a < σ*; in particular α(P) ≥ σ* > σ₁.
*Proof.* Let θ′ := θ under (B), θ′ := θ₂ under (B₂). Under (B), ∫_Y^{2Y}|E|u^{−σ−1}du ≪ Y^{θ−σ}; under (B₂), by Cauchy–Schwarz,
∫_Y^{2Y}|E|u^{−σ−1}du ≤ Y^{−σ−1}·Y^{1/2}·(∫_Y^{2Y}E²)^{1/2} ≪ Y^{θ₂−σ} (re-derived here; it is O1's computation). Summing over
Y = 2^m, Ê(s) := ∫_1^∞E(u)u^{−s−1}du converges absolutely and locally uniformly on Re s > θ′, so it is analytic there and continuous
on [σ₁, 1]. By s40-NOTE Lemma 1.5 [quoted: l. 96–103] ζ_P(s) = ζ_c(s) + sÊ(s) for Re s > 1, ζ_c(s) = (s − 1 + ρ)/(s − 1); the right
side continues ζ_P to Re s > θ′ minus s = 1, and the truncated form (same lines) reads, for real σ ∈ (θ′, 1),
ζ_P(σ) = F_X(σ) + σ∫_X^∞E(u)u^{−σ−1}du. Lemma 1.2 (its hypothesis holds because the integral converges absolutely) gives
ζ_P(σ₁) > F_X(σ₁) ≥ 0. As σ → 1⁻, ζ_c(σ) = 1 − ρ/(1 − σ) → −∞ while σÊ(σ) stays bounded, so ζ_P(σ) → −∞; the intermediate value
theorem gives σ* ∈ (σ₁, 1). The last claim is the closing step of s40-NOTE Theorem 1.6 [quoted: l. 112–115]: if ψ_P(x) − x = O(x^a)
with a < σ*, then −ζ′_P/ζ_P − s/(s − 1) is analytic on Re s > max(a, θ′), contradicting the pole of −ζ′_P/ζ_P at σ*. That step
uses only the continuation of ζ_P, which (B₂) supplies as well as (B). ∎

**Corollary 1.4 (what a certificate leaves to prove)** [proved here]. In the setting of Theorem 1.3 with σ₁ > ½: if (B) holds with
θ < σ₁/2, then β(P) ≤ θ < σ₁/2 and α(P) > σ₁ > ½, so α(P) > max{½, 2β(P)} and **Conjecture U is false**. Under (B₂) with θ₂ < σ₁/2
the same holds for the mean-square variant of U (α ≤ max{½, 2β₂}, O1). So each certificate (F_{x_K}(σ₁) ≥ 0, proved in §5) leaves
exactly one statement to prove: **Lemma B with exponent θ < σ₁/2** (pointwise), or its mean-square form.

**Remark 1.5 (against s40 Cor. 1.7(iii)).** There the tail was bounded below by −½X^{−σ₁} (E > −½ alone), so the criterion read
F_X(σ₁) > ½X^{−σ₁}. Lemma 1.2 removes that term when X is a lattice point: the integrality of N turns the one-sided bound into a
floor of mean zero, and a decreasing weight makes its contribution positive. The gain in σ₁ is ½X^{−σ₁}/|F′_X| (about 5·10⁻⁸ at
X = 10⁸ for π/16), so σ₁ can now be pushed to the zero of F_X itself, up to the interval radius.

## §2. The generator `s8cert.c`: exact ordering

Written from the definition only (s40 CHARTER §1 and the Lindley form of `../CHARTER.md` §2(a)); s8o.cpp and s8dd.c were not
opened (their logs only, §4). Source `verify/s8cert.c`, runner `verify/run_cert.sh`, logs `verify/logs/`, moments `verify/data/`.

**2.0 The cell form (re-derived)** [proved here]. Put c_k := #composites in (x_{k−1}, x_k] and e_k := N(x_k) − (k + 1). Since
T(x_k) = k + ½, E(x_k) = e_k + ½, and E > −½ with N integral gives e_k ≥ 0. g-primes lie on the lattice (s40-NOTE Lemma 1.2), so on
(x_{k−1}, x_k) N grows by composites only. The rule places a g-prime at x_k iff D reaches ½ there, i.e. N(x_k−) = k with the tie
convention that a composite AT x_k counts first, i.e. iff N(x_{k−1}) + c_k = k, i.e. iff e_{k−1} = 0 and c_k = 0; then e_k = 0.
Otherwise N(x_k) = N(x_{k−1}) + c_k, e_k = e_{k−1} + c_k − 1 ≥ 0. With e_0 := 0, c_1 := 0 this starts correctly (N = 1 on [1, x_1),
g-prime p₁ = x_1). So the whole system is the sequence of CELL INDICES of its composites; nothing else is decided. The generator
decides, for every composite c ≤ X, the integer k(c) with x_{k−1} < c < x_k (strict: an equality would be undecidable by the exact
test below and the program stops; it never stopped).

**2.1 Enumeration.** Every composite (a multiset of ≥ 2 g-primes) is written once as c = P·q, q its largest g-prime (by lattice
index, ties allowed), P = c/q > 1. A *prefix* is a g-integer P > 1 with P·P⁺(P) ≤ X; each prefix carries a cursor into the stored
g-primes (from P⁺(P) upward). Windows of cells (K_{w−1}, K_w] are fixed in advance with x̃_{K_w}(1 + 10⁻⁶) ≤ p̃₁·x̃_{K_{w−1}} and
K_w − K_{w−1} ≤ 2²¹; in window w every prefix whose next product has computed value ≤ B_w := fl(x̃_{K_w}(1 + 2⁻³⁰)) emits its products
in cursor order, then is re-queued for the window of its next product (or, if that g-prime is not yet placed, of the lower bound
P·x̃_{K_{w−1}+1}(1 − 10⁻¹²)); the composites are counted by cell (a composite of a later cell is carried to the next window), and the
cells are then swept with the recursion of 2.0, placing g-primes. A g-integer is counted with multiplicity by construction (each
multiset once), so no freeness assumption is used anywhere; Lemma 1.3 of s40 (transcendence of t) is not load-bearing.

**Lemma 2.1 (floating-point values and the decision test)** [proved here]. Standard model: fl(a ∘ b) = (a ∘ b)(1 + δ), |δ| ≤ u = 2⁻⁵³,
round to nearest, compiled with `-ffp-contract=off` (no fused operations), no overflow or underflow in the ranges used.
(i) t̃ = RN(t) and |t̃ − t| ≤ u·t [computed: `pi_enclosure.py`, log `pi_enclosure.log` — π enclosed by Machin's formula in exact
rationals, width 1.3·10⁻⁶⁰, cross-checked against arb to 58 digits; both ends of the induced enclosure of t round to the same double].
(ii) x̃_k := fl(1 + fl((k − ½)t̃)) has |x̃_k − x_k| ≤ (3u + 5u²)x_k: with h = k − ½ exact, fl(ht̃) = ht(1 + ε)(1 + δ₁), |ε| ≤ u, and
|fl(1 + a) − (1 + ht)| ≤ |a − ht|(1 + u) + u(1 + ht) ≤ x_k[(2u + u²)(1 + u) + u].
(iii) A g-integer with Ω prime factors, computed as a chain of Ω − 1 products of values (ii): |ñ − n| ≤ ((1 + 3.0001u)^Ω(1 + u)^{Ω−1} − 1)n
≤ 4.0002·Ω·u·n for Ω ≤ 100.
(iv) Let dl = fl(c̃ − x̃_{k−1}), dr = fl(x̃_k − c̃), m = max(c̃, x̃_k), bnd = fl(1.01(4.02Ω + 3.0002)u·m). If dl > bnd and dr > bnd, then
x_{k−1} < c < x_k. *Proof.* c − x_{k−1} ≥ (c̃ − x̃_{k−1}) − |c − c̃| − |x̃_{k−1} − x_{k−1}| ≥ dl/(1 + u) − (4.0003Ω + 3.0002)u·m > 0, since
the computed bnd exceeds (1 + u)(4.0003Ω + 3.0002)u·m (the factor 1.01 absorbs the ≤ 5 roundings in bnd). Same on the right. ∎
(v) The test "n ≤ V" for an integer checkpoint V uses bnd = 1.01(4.02Ω + 1)u·max(ñ, V) in the same way.
**The exact path.** If (iv) or (v) fails, the decision is re-made in GMP integers: with TLO/2^D ≤ t ≤ THI/2^D (D = 200, from the
Machin enclosure; THI − TLO ≤ 7), c(t) = Π(1 + (k_i − ½)t) = Π(2^{D+1} + (2k_i − 1)T)/2^{(D+1)Ω} and x_m(t) are increasing in t, so
c > x_m is proved by c(TLO) > x_m(THI) and c < x_m by c(THI) < x_m(TLO), all exact integer comparisons; the lattice indices k_i of the
factors are recovered through parent pointers of the prefixes. If neither holds the program stops ("undecided"); it never did.

**Lemma 2.2 (completeness)** [proved here]. Every composite c ≤ X = x_{K_fin} is emitted exactly once, in a window w ≤ the window of
its cell, and only g-primes already placed are used. *Proof.* Uniqueness: one (P, q) per multiset, and the cursor of P moves
forward only. Availability: in window w any product P·q with computed value ≤ B_w has q ≤ B_w(1 + 10⁻¹³)/p₁ < x_{K_{w−1}} by the
schedule (all relative errors ≤ 10⁻¹³ ≪ 10⁻⁶), so q is stored; P ≤ c/p₁ is a g-integer of an earlier window, so its prefix record
exists, and P·P⁺(P) ≤ c ≤ X makes it a prefix (its computed first product is ≤ X(1 + 10⁻¹³) < fl(X̃(1 + 2⁻³⁰))). Timeliness: the
computed products v·q̃_j are nondecreasing in j (rounding is monotone), and a prefix is always queued for a window no later than
the first window whose bound exceeds its next computed product (the lower bound used for an unplaced g-prime is below that product);
so P·q is emitted in the first window w with c̃ ≤ B_w. If c ≤ x_{K_w} then c̃ ≤ x_{K_w}(1 + 10⁻¹³) < B_w, so the emission is no later
than the window of the cell; an early emission (c > x_{K_w}) is carried, and lands in window w + 1 because c̃ ≤ B_w < x_{K_{w+1}}.
The program checks these three facts at run time (stops on "composite in a finished cell", "carry beyond next window", "bucket
target not in the future"); none fired. ∎
**Validation of the exact path** [computed: `logs/exactpath_pi16_1e7.log`]. Run with the test hook `S8C_INFLATE=1e12` (bounds
inflated 10¹², so 1,329,907 of the 1,329,981 decisions to 10⁷ go through GMP): moment files and checkpoints are byte-identical to
the normal run (0 fallbacks); `S8C_INFLATE=1e6` (3,874 fallbacks): identical.

## §3. Interval evaluation of F_X

The sum Σ_{n≤X} n^{−σ} has N(X) ≈ ρX terms (1.96·10⁹ for π/16 at 10¹⁰). The generator does not evaluate n^{−σ}; it stores, per block
b = [a, a + W) with a = 2^e(1 + i/256), W = 2^{e−8} (256 blocks per octave), the count and enclosures of the power sums of
z̃_n := (ñ − a)/W ∈ [0, 1). Then F_X(σ) is assembled in arb for any σ afterwards (`verify/feval.py`, `verify/certify.py`).

**Lemma 3.1 (block expansion)** [proved here]. Let 0 < σ ≤ 1, r := W/a = 1/(256 + i), Ω_b the largest number of prime factors in
block b, Z_j := Σ_{n∈b} z̃_n^j. Then
  Σ_{n∈b} n^{−σ} = a^{−σ}·[cnt_b + Σ_{j=1}^{6} C(−σ, j)·r^j·Z_j + R_b + P_b],  |R_b| ≤ r⁷Z₇/(1 − r),  |P_b| ≤ 1.001·σ·cnt_b·4.0003Ω_b·u·(1 + r).
*Proof.* Each n is assigned by its computed value ñ, so x̃ := (ñ − a)/a = r·z̃ ∈ [0, r). For 0 < σ ≤ 1, |C(−σ, j)| = Π_{i<j}(σ + i)/(i + 1)
≤ 1, so (1 + x̃)^{−σ} = Σ_{j≤6} C(−σ, j)x̃^j + R with |R| ≤ Σ_{j≥7} x̃^j = x̃⁷/(1 − x̃) ≤ r⁷z̃⁷/(1 − r). The true value is n = a(1 + x),
|x − x̃| = |n − ñ|/a ≤ 4.0003Ω_b·u·ñ/a ≤ 4.0003Ω_b·u(1 + r) (Lemma 2.1(iii)), and |d/dx (1 + x)^{−σ}| ≤ σ(1 − 10⁻¹²)^{−2} ≤ 1.001σ on
the segment between them. Sum over n ∈ b. ∎
**Lemma 3.2 (the stored enclosures)** [proved here]. The generator stores integers lo_j ≤ 2⁶²Z_j ≤ hi_j (j = 1…7). *Proof.* ñ − a is
exact (same binade) and a multiple of ulp(ñ) = 2^{e−52}; dividing by W = 2^{e−8} is exact, so z̃ is a double, a multiple of 2⁻⁴⁴, and
2⁶²z̃ is an integer (j = 1 exact). For j ≥ 2 the computed power p_j = fl(p_{j−1}z̃) equals z̃^j(1 + θ), |θ| ≤ γ_{j−1} ≤ 6.0001u; with
q = 2⁶²p_j (exact scaling), fl(q − 2⁻⁴⁹q) ≤ q(1 − 16u)(1 + u) ≤ q(1 − 15u) ≤ 2⁶²z̃^j ≤ q(1 + 6.01u) ≤ q(1 + 16u)(1 − u) ≤ fl(q + 2⁻⁴⁹q);
floor and ceiling are exact conversions below 2⁶³; the accumulators are 128-bit integers (no overflow below 2⁹⁵). z̃ = 0 or z̃ ≥ 2⁻⁴⁴,
so no power underflows. ∎
**Assembly.** F_X(σ) = Σ_b a_b^{−σ}[…] + ρX^{1−σ}/(σ − 1) − E(X)X^{−σ} with X = x_K = 1 + (K − ½)·16/π (resp. 32/π), E(X) = e_K + ½
(exact: T(x_K) = K + ½), π from arb's rigorous constant, 200-bit balls; each Z_j enters as the ball [lo_j, hi_j]·2⁻⁶², R_b and P_b as
symmetric balls. `feval.py` asserts Σ_b cnt_b = N(x_K) (every g-integer ≤ X in exactly one block). σ is an exact rational.
**Check against s8dd at 10⁷** [computed: `logs/feval_pi16_1e7.log`]: at x_K = 9,999,996.373 (K = 1,963,495, N = 1,963,496,
E(x_K) = ½): F(0.79) = 0.0222313187234 ± 5.3·10⁻¹⁴, F(0.80) = −0.0257111582844 ± 6.9·10⁻¹⁴, F(0.78) = 0.0659546434367,
F(0.81) = −0.0785447458226 — the s8dd values at X = 10⁷ (read-O §2; `free-greedy-s40/theory/verify-O/s8dd_pi16_1e7.log`) are
0.022231318724, −0.025711158284, 0.065954643437, −0.078544745823 [quoted]: agreement to the 12 digits printed there, as it must be
(F_{10⁷} − F_{x_K} = σ∫_{x_K}^{10⁷}E u^{−σ−1}du, of size 10⁻¹³ here).

## §4. Cross-checks against the Session-40 generators

The s40 generators were not imported, compiled or opened; their on-disk logs were read as data: s8o (`free-greedy-s40/compute/
verify-O/logs/o_pi{16,32}_1e10.log`, `realzero_o_pi{16,32}.txt`) and s8dd (`free-greedy-s40/theory/verify-O/s8dd_pi16_1e7.log`,
`s8dd_pi32_1e8.log`). Runs [computed]: `logs/s8cert_pi16_1e10.log` (99 s, 0.62 GB, 1,513,583,581 cell decisions, 4,726 exact),
`logs/s8cert_pi32_1e10.log` (43 s, 572,359,633 decisions, 785 exact); machine: Apple arm64, one core.
**Counts** [computed: `logs/crosscheck_pi16.log`, `logs/crosscheck_pi32.log`]. At the 14 checkpoints V = ⌊10^{h/2}⌋, 10³ ≤ V ≤ 10^9.5,
N(V) and π_P(V) agree EXACTLY with s8o for both systems (e.g. π/16: N(10⁹) = 196,349,548, π_P(10⁹) = 49,924,829; π/32:
N(10⁹) = 98,174,771, π_P(10⁹) = 44,345,886; N(10^9.5) = 620,911,771 and 310,455,884). At the end, π_P(x_K) = 449,911,828 and
409,388,073 = s8o's π_P(10¹⁰) (no g-prime in (x_K, 10¹⁰]); N(x_K) is 1 and 2 below s8o's N(10¹⁰), consistent with s8o's E(10¹⁰):
E(x_K) − ρ(10¹⁰ − x_K) + (count in between) = ½ − 0.7972 + 1 = 0.7028 (s8o 0.702729) and ½ − 0.6486 + 2 = 1.8514 (s8o 1.851364). The
stored g-primes ≤ X/p₁ number 134,178,740 and 71,517,727, equal to s8o's "storedprimes". sup E agrees to 10⁻¹⁰…10⁻⁷ (mine is a
double-precision statistic, not certified; e.g. 18.5365159736 vs 18.5365160221 at 10⁹ for π/16).
**F_X and its zero** [computed: `logs/sigma_table_pi16.log`, `logs/sigma_table_pi32.log`]. The certified σ₁ (= the zero of F_{x_K}
to 10⁻¹²) against the s8o zero of F_{10^d} (10 digits) and the s8dd root (12 digits):

| X ≈ | σ₁(π/16), this unit | s8o / s8dd | σ₁(π/32), this unit | s8o / s8dd |
|---|---|---|---|---|
| 10⁶ | 0.794752301959 | 0.7947523020 | 0.895076334603 | 0.8950763346 |
| 10⁷ | 0.794754781368 | 0.7947547814 / **0.794754781368** | 0.895076489528 | 0.8950764895 |
| 10⁸ | 0.794755262461 | 0.7947552625 | 0.895076513462 | 0.8950765135 / **0.895076513462** |
| 10⁹ | 0.794755353284 | 0.7947553533 | 0.895076517060 | 0.8950765171 |
| 10¹⁰ | 0.794755370097 | 0.7947553701 | 0.895076517592 | 0.8950765176 |

(The shift X = 10^d → x_K changes F_X by σ∫E u^{−σ−1} over an interval of length < t, below 10⁻¹² from 10⁶ on.)
**Close calls** [computed: `logs/recheck_close_pi16.log`, `logs/recheck_close_pi32.log`]. Every exact-path decision with relative
margin < 10⁻¹⁶ is printed with its factorization (305 for π/16, 57 for π/32) and re-decided by `recheck_close.py` in mpmath at
80 digits (its own π; no GMP, no Machin): 0 disagreements. Closest cell decisions to 10¹⁰:
π/16 — c = x(533658)·x(13)·x(2)·x(1) = 5,384,739,852.8295799…, 1.538·10⁻¹⁰ below x_k, k = 1,057,291,198 (relative 2.86·10⁻²⁰);
π/32 — c = x(33405216)·x(1) = 2,073,206,595.9280907…, 1.6935·10⁻⁹ below x_k (relative 8.168·10⁻¹⁹), the same composite and margin
as s8o's audit line ("min|diff| = 1.693e-09 abs, 8.168e-19 rel"). For π/16, s8o's line gives 1.322·10⁻⁸ abs; the composite above is
150 times closer, so s8o's audit statistic covers a subset of the comparisons (plausibly the decisive ones only). This is not a
disagreement about the system: all checkpoint counts agree and my decision for that composite is confirmed at 80 digits; a cell
decision that does not change any g-prime placement would not be visible in the counts, so the counts alone do not prove that the
two generators agree on every cell.

## §5. The certificates (lower end σ₁)

`certify.py` bisects on 12-decimal rationals for the largest σ₁ with F_X(σ₁) > 0 PROVED (lower end of the arb ball positive), and
reports whether F_X(σ₁ + 10⁻¹²) < 0 is proved too (then the zero of F_X is located to 10⁻¹²). Logs [computed]:
`logs/certify_pi16_1e10.log`, `logs/certify_pi32_1e10.log`; data `data/pi16_K1963495408.mom`, `data/pi32_K981747704.mom` (with
`params.txt`, these files and `feval.py`/`certify.py` reproduce every number below in 5 s).

**Theorem 5.1 (S8(π/16))** [computed: the inequality; proved here: the implications, Theorem 1.3 and Corollary 1.4]. Let P = S8(π/16),
K = 1,963,495,408, X = x_K = 1 + (K − ½)·16/π = 9,999,999,995.93953… . Then N_P(X) = 1,963,495,409, π_P(X) = 449,911,828, E(X) = ½,
and **F_X(0.794755370097) = (2.0 ± 0.6)·10⁻¹² > 0** (and F_X(0.794755370098) < 0). Hence:
(i) if N_P(u) − (π/16)u = O(u^θ) for some θ < 0.794755370097 (any constant), or the mean-square bound (B₂) holds with such an exponent,
then ζ_P has a real zero in (0.794755370097, 1) and α(P) > 0.794755370097;
(ii) if N_P(u) − (π/16)u = O(u^θ) with **θ ≤ 0.3973776850**, then α(P) > max{½, 2β(P)} and Conjecture U is false.

**Theorem 5.2 (S8(π/32))** [same labels]. Let P = S8(π/32), K = 981,747,704, X = x_K = 1 + (K − ½)·32/π = 9,999,999,993.39305… . Then
N_P(X) = 981,747,705, π_P(X) = 409,388,073, E(X) = ½, and **F_X(0.895076517592) = (1.4 ± 0.1)·10⁻¹² > 0** (and F_X(0.895076517593) < 0).
Hence (i) as above with 0.895076517592, and (ii) U is false as soon as N_P(u) − (π/32)u = O(u^θ) with **θ ≤ 0.4475382587**.

**How far this moves the target.** Exponent of Lemma B needed to refute U: Theorem 1.6 alone ½ − ρ = 0.3037 (π/16), 0.4018 (π/32);
s40 certificates 0.395, 0.445 (from F_{10⁷}(0.79) and F_{10⁶}(0.89)); now **0.39737768 and 0.44753825**. The gain is in the third
decimal; the content of this section is that these values are proved (exact ordering, interval arithmetic) and sit at the zero of
F_X itself (Remark 1.5).

**σ₁ against the true zero.** σ₁(X) at x_K ≈ 10⁶…10¹⁰ (§4 table) increases by 2.48·10⁻⁶, 4.81·10⁻⁷, 9.08·10⁻⁸, 1.68·10⁻⁸ per decade
(π/16; ratios 5.15, 5.30, 5.40) and by 1.55·10⁻⁷, 2.39·10⁻⁸, 3.60·10⁻⁹, 5.32·10⁻¹⁰ (π/32; ratios 6.47, 6.65, 6.76), as the tail
σ∫_X^∞E u^{−σ−1} ≈ (mean E)·X^{−σ} predicts (X^{−σ} falls by 10^{0.79} = 6.2 and 10^{0.90} = 7.9 per decade, the mean of E grows like
log X). Geometric extrapolation [heuristic, not proved]: σ* ≈ 0.7947553738 (π/16) and 0.8950765177 (π/32), i.e. the certified σ₁ is
about 4·10⁻⁹ and 1·10⁻¹⁰ below the zero it bounds. Proved instead, under a stated hypothesis: §6 (the zero lies within 1.4·10⁻⁷,
resp. 7.4·10⁻⁹, of σ₁ if E(u) ≤ 0.1·log²u beyond X).

## §6. The upper bracket (σ₂) under stated tail hypotheses

**Lemma 6.1 (tail upper bounds)** [proved here]. Let X ≥ 1, 0 < σ < 1, L = log X.
(a) If E(u) ≤ K log²u for all u ≥ X, then σ∫_X^∞E(u)u^{−σ−1}du ≤ K·τ_X(σ), τ_X(σ) := σX^{−σ}(L²/σ + 2L/σ² + 2/σ³).
(b) If E(u) ≤ C·u^ϑ for all u ≥ X, with ϑ < σ, then the tail is ≤ C·σX^{ϑ−σ}/(σ − ϑ).
(c) If ∫_Y^{2Y}E(u)²du ≤ C²Y^{1+2ϑ} for all Y ≥ X, with ϑ < σ, then the tail is ≤ C·σX^{ϑ−σ}/(1 − 2^{ϑ−σ}).
*Proof.* (a) I_n := ∫_X^∞ log^n u·u^{−σ−1}du satisfies I_0 = X^{−σ}/σ and, integrating by parts, I_n = X^{−σ}L^n/σ + (n/σ)I_{n−1};
so I_2 = X^{−σ}(L²/σ + 2L/σ² + 2/σ³). (b) ∫_X^∞u^{ϑ−σ−1}du = X^{ϑ−σ}/(σ − ϑ). (c) On [Y, 2Y], u^{−σ−1} ≤ Y^{−σ−1} and, by
Cauchy–Schwarz, ∫_Y^{2Y}|E| ≤ Y^{1/2}(∫_Y^{2Y}E²)^{1/2} ≤ C·Y^{1+ϑ}; sum Y = 2^mX, m ≥ 0: σC·X^{ϑ−σ}Σ_m 2^{m(ϑ−σ)}. ∎
Each hypothesis, with E > −½, implies (B) or (B₂) for every exponent above ϑ (resp. every θ > 0 in (a)), so Theorem 1.3 applies
at σ₁ and ζ_P(σ₂) = F_X(σ₂) + tail ≤ F_X(σ₂) + (bound). **So F_X(σ₂) + bound(σ₂) < 0, proved in arb, puts a zero of ζ_P in
(σ₁, σ₂)** (an odd number of zeros, with multiplicity). The search (`certify.py`) returns the smallest 9-decimal σ₂ with this proved.
Scale of the hypotheses against the data [computed: `logs/s8cert_pi{16,32}_1e10.log`; s8o agrees, §4]: sup_{u≤x_K}E/log²u =
26.137/530.2 = 0.049 (π/16) and 15.434/530.2 = 0.029 (π/32); so K = 0.1 is about twice the measured envelope, K = 1, 10, 100 are generous.

**Theorem 6.2 (the zero boxed)** [computed: `logs/certify_pi{16,32}_1e10.log`; proved here: Lemma 6.1 + Theorem 1.3]. With P, X, σ₁
as in Theorems 5.1/5.2: if E satisfies the hypothesis of a row for all u ≥ X (row 7: for all Y ≥ X), then F_X(σ₂) + bound(σ₂) < 0
is proved, so ζ_P(σ₁) > 0 > ζ_P(σ₂) and ζ_P has a real zero in (σ₁, σ₂). ϑ is σ₁/2 truncated to 9 decimals (0.397377685 for π/16,
0.447538258 for π/32): rows 5–7 are Lemma B at the exponent that refutes U, with an explicit constant beyond X.

| hypothesis beyond X | σ₂ (π/16) | σ₂ − σ₁ | σ₂ (π/32) | σ₂ − σ₁ |
|---|---|---|---|---|
| E(u) ≤ 0.1·log²u | 0.794755510 | 1.40·10⁻⁷ | 0.895076525 | 7.4·10⁻⁹ |
| E(u) ≤ log²u | 0.794756766 | 1.40·10⁻⁶ | 0.895076591 | 7.3·10⁻⁸ |
| E(u) ≤ 10·log²u | 0.794769322 | 1.40·10⁻⁵ | 0.895077248 | 7.3·10⁻⁷ |
| E(u) ≤ 100·log²u | 0.794894399 | 1.39·10⁻⁴ | 0.895083814 | 7.3·10⁻⁶ |
| E(u) ≤ u^ϑ | 0.794799754 | 4.44·10⁻⁵ | 0.895083982 | 7.5·10⁻⁶ |
| E(u) ≤ 100·u^ϑ | 0.798716538 | 3.96·10⁻³ | 0.895805019 | 7.3·10⁻⁴ |
| ∫_Y^{2Y}E² ≤ Y^{1+2ϑ} | 0.794828566 | 7.32·10⁻⁵ | 0.895089041 | 1.25·10⁻⁵ |

So under Lemma B at the U-refuting exponent with constant 1 beyond 10¹⁰ (row 5), the real zero is pinned to 4.5·10⁻⁵ (π/16) and
7.5·10⁻⁶ (π/32); under the data-sized envelope 0.1·log²u to 1.4·10⁻⁷ and 7.4·10⁻⁹. Not proved here: that the zero in (σ₁, σ₂) is
unique, or that ζ_P < 0 on [σ₂, 1) (the sign change gives an odd number of zeros in the box, with multiplicity).

## §7. What is left to prove
