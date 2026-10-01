# NOTE — unit `U7-patterns` of the stream `lemmaB-s41`: pattern discovery in exact data for S8(π/16), S8(π/32)

Session 41, started 16:55 IST 2026-10-01. Writer: Opus 5.5 (agent). Brief: `../CHARTER.md` §3 (U7) and the orchestrator's prompt
(four tasks: excursion anatomy; correlations and window variances; a Lyapunov / monotone quantity; thresholds ¼, ¾ and early offsets).
Labels: **[proved here]**, **[computed]** (script + log in `verify/`), **[quoted]**, **[recalled, unverified]** (never load-bearing).
Notation (charter §2(a)): t = 1/ρ; lattice x_k = 1 + (k − 1 + τ)t (τ = ½ unless stated); c_k = composites in (x_{k−1}, x_k];
e_k = N(x_k) − (k + 1) = max(e_{k−1} + c_k − 1, 0); a g-prime sits at x_k iff e_{k−1} = 0 and c_k = 0; E(x_k) = e_k + 1 − τ.

## §0. Close

(filled last)

## §1. The generator and its exactness

**1.1 Construction** [computed: `verify/s8gen.c`, written for this unit; the s40 generators were read only for their logged numbers].
Block sweep: if x_K is decided, every composite below p₁x_K has all prime factors below x_K, so the cells K+1, …, K′ with x_{K′} < p₁x_K
are filled by a depth-first enumeration of nondecreasing index sequences (j₁ ≤ j₂ ≤ …, at least two factors) over the g-primes decided so
far, then the queue is run over them (e_k = max(e_{k−1} + c_k − 1, 0); a g-prime at x_k iff e_{k−1} = 0 = c_k). Chunks of 2²⁵ cells bound
memory. g-primes are stored as lattice indices n (value 1 + (n − 1 + τ)t − δ, recomputed in double-double when needed). Variants: threshold
τ (lattice x_k = 1 + (k − 1 + τ)t) and early placement: the g-prime decided at x_k is placed at x_k − δ, 0 ≤ δ < τt (decision unchanged).
Per cell the generator writes c_k, e_k, c_k^{(1)} (composites whose smallest g-prime factor is p₁), c_k^{(Ω=2)} (two factors), the counts of
composites divisible by p₂, p₃, p₄ (d2–d4) and with smallest factor p₂, p₃, p₄ (s1–s3), all uint8,
and the list of prime cells; optional watch windows dump every composite of chosen cells with its factor indices.

**1.2 Exactness of every cell decision** [proved here]. Unit roundoff ε = 2⁻⁵³. Error-free transformations: two_sum (Knuth), fast
two-sum (Dekker; operands ordered), fma for the product error. Per operation, relative error of the double-double result: product ≤ 9ε²;
product by a double ≤ 4ε²; addition of the positive double 1 ≤ 2.1ε²; subtraction of δ (early runs only) ≤ 13.2ε² relative to the
result (since x_k/(x_k − δ) ≤ 2); stored t, ρ (correctly rounded hi and lo from 60-digit values, `consts.py`) ≤ 1.01ε². Hence each
g-prime value carries relative error ≤ 30ε², a product of j ≤ 64 of them ≤ 40jε² ≤ 3.2·10⁻²⁹, and u := (c − 1)ρ + 1 − τ carries absolute
error ≤ ρc·3.3·10⁻²⁹ + 3·10⁻³² ≤ 7·10⁻²⁰ for c ≤ 10¹⁰·2, ρ ≤ 0.2. The fractional part is formed as (u_hi − ⌊u_hi⌋) + u_lo, the first
difference exact (Sterbenz), the sum rounded once (≤ ε), the wrap-around once more (≤ ε): total ≤ 2.3·10⁻¹⁶. Every decision whose
computed margin min(f, 1 − f) is ≥ 10⁻¹⁵ is therefore correct (true margin > 7·10⁻¹⁶ > 0); smaller margins are written out (FLAG) for a
60-digit re-decision. Pruning bounds are widened by 10⁻¹³ relative, far above these errors, and the cell index alone decides membership,
so no composite is lost or counted twice (distinct index sequences give distinct values: the proof of Lemma 1.3 of the s40 theory NOTE
goes through for every rational τ ∈ (0, 1] and every δ = a + bt with a, b ∈ ℚ, a ≠ 1, since the g-primes are then the pairwise
non-associate linear polynomials (1 − a) + (n − 1 + τ − b)X of ℚ[X] evaluated at the transcendental t). A rounding at a block edge cannot let an undecided
g-prime in: such a prime is ≥ x_{K+1} − δ > x_K, while a factor of a block composite is < x_{K′}/p₁ ≤ x_K(1 + 10⁻¹⁵).

**1.3 Cross-check against Session 40** [computed: `verify/logs/regress.log`]. τ = ½, δ = 0. π/16, X = 10⁷: N = 1,963,496, π = 633,514,
sup E = 12.838454 at 9,701,099.12, largest gap 336.1352, at most 12 factors — identical to `free-greedy-s40/theory/verify-O/s8dd_pi16_1e7.log`
in every printed digit, as are the checkpoints at 10⁵, 10⁶ and the first six g-primes. π/32, X = 10⁸: N = 9,817,480, π = 4,822,578,
sup E = 9.857826 at 99,631,883, gap 397.2507, 10 factors — identical to `s8dd_pi32_1e8.log`; the smallest decision margin sits at
71,112,777, the same composite the s40 audit flagged as its tightest. Run times: 0.06 s (π/16, 10⁷), 0.3 s (π/32, 10⁸), 9.3 s and
330 MB (π/16, 10⁹), 3.9 s (π/32, 10⁹). FLAG count 0 in every run reported in this NOTE; smallest margins are listed per run.

## §2. The two systems to 10¹⁰ (headline data)

[computed: `verify/run_1e10.sh`, logs `verify/logs/b16_1e10.log`, `b32_1e10.log`; 118 s and 807 MB (π/16), 48 s and 556 MB (π/32);
smallest decision margins 3.0·10⁻¹¹ and 1.7·10⁻¹⁰ cell, FLAG = 0; at most 18 and 12 g-prime factors in a composite.]
π/16 to 10¹⁰: K = 1,963,495,408 cells, N(x_K) = 1,963,495,409, π = 449,911,828, composites 1,513,583,580. π/32 to 10¹⁰: K = 981,747,704,
N = 981,747,705, π = 409,388,073, composites 572,359,631. Both end with e_K = 0. G = largest g-prime gap, emax = max e_k.

| x | sup E π/16 | /log²x | emax | G (cells) | G/log²x | G/log³x | sup E π/32 | /log²x | emax | G (cells) | G/log²x | G/log³x |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10⁶ | 9.636 | 0.0505 | 9 | 49 | 1.31 | 0.095 | 6.393 | 0.0335 | 5 | 17 | 0.91 | 0.066 |
| 10⁷ | 12.838 | 0.0494 | 12 | 66 | 1.29 | 0.080 | 8.928 | 0.0344 | 8 | 25 | 0.98 | 0.061 |
| 10⁸ | 16.364 | 0.0482 | 15 | 106 | 1.59 | 0.086 | 9.858 | 0.0291 | 9 | 39 | 1.17 | 0.064 |
| 10⁹ | 18.537 | 0.0432 | 18 | 155 | 1.84 | 0.089 | 13.223 | 0.0308 | 12 | 53 | 1.26 | 0.061 |
| 10¹⁰ | 26.137 | 0.0493 | 25 | 240 | 2.31 | 0.100 | 15.434 | 0.0291 | 14 | 73 | 1.40 | 0.061 |

**Pattern 2.1 (two different polylog laws)** [computed]. sup_{u≤x} E(u)/log²x stays in [0.043, 0.052] (π/16) and [0.029, 0.035]
(π/32) over 10⁵–10¹⁰, while the largest gap G(x)/log²x rises steadily (1.29 → 2.31 for π/16) and G(x)/log³x is flat (0.061 ± 0.003 for π/32
over 10⁷–10¹⁰; 0.080–0.100 for π/16). Both match a queue of load λ = 1 − π′ with π′ ≍ 1/(ρ log x) the idle fraction per cell: the stationary
tail rate is κ ≍ π′, so sup e ≍ log(#cells)/κ ≍ ρ log²x, while a busy period of length L needs ≈ L arrivals in L cells, a large deviation of
rate ≍ π′²/2, so G ≍ log(#cells)/π′² ≍ ρ² log³x [heuristic]. **Consequence for the proof units:** Prop. 2.1 (E ≤ ρG − ½) loses a full
factor log x against the data, so Lemma G_ρ is the weaker target only in name: the route through gaps must prove a log³-type bound, the
direct route a log²-type bound; both give B_ρ with any θ > 0.

## §3. Arrivals and queue: correlations, window variances, tails (task 2)

**3.1 Per half-decade** [computed: `verify/stats.c` → `verify/logs/b16_1e10.stats`, `b32_1e10.stats`; table by `verify/sumstats.py`].
π′ = idle (g-prime) fraction per cell, λ = 1 − π′ + (drift of e) = mean arrivals per cell; κ = least-squares decay rate of the empirical
P(e_k ≥ h) (h ≥ 2, ≥ 30 cells); κ_P = root of λ(e^κ − 1) = κ, the rate a Poisson(λ)-arrival queue with one service per step would have;
X₁ = ΔE(W/p₁) over the build-up W of an excursion (exact, §4.1). Selected bands (all bands in the logs):

| ρ | x band | π′ | λ | Fano(1) | mean e | κ | κ_P | κ/κ_P | κ/π′ | #excursions | mean height | corr(h, X₁) | max gap (cells) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| π/16 | [10⁵, 10^5.5) | 0.3831 | 0.6169 | 0.936 | 0.347 | 1.352 | 0.899 | 1.50 | 3.53 | 4,202 | 1.39 | 0.375 | 30 |
| π/16 | [10^6.5, 10⁷) | 0.3125 | 0.6875 | 0.955 | 0.563 | 1.119 | 0.708 | 1.58 | 3.58 | 140,676 | 1.58 | 0.411 | 66 |
| π/16 | [10^7.5, 10⁸) | 0.2766 | 0.7234 | 0.963 | 0.718 | 0.980 | 0.616 | 1.59 | 3.54 | 1,403,250 | 1.68 | 0.438 | 106 |
| π/16 | [10^8.5, 10⁹) | 0.2475 | 0.7525 | 0.968 | 0.883 | 0.868 | 0.544 | 1.59 | 3.51 | 13,743,345 | 1.79 | 0.463 | 155 |
| π/16 | [10^9.5, 10¹⁰) | 0.2236 | 0.7764 | 0.972 | 1.053 | 0.760 | 0.487 | 1.56 | 3.40 | 133,248,949 | 1.89 | 0.485 | 240 |
| π/32 | [10^6.5, 10⁷) | 0.5249 | 0.4751 | 0.960 | 0.173 | 1.802 | 1.341 | 1.34 | 3.43 | 47,289 | 1.26 | 0.220 | 25 |
| π/32 | [10^7.5, 10⁸) | 0.4811 | 0.5189 | 0.965 | 0.230 | 1.611 | 1.195 | 1.35 | 3.35 | 533,583 | 1.32 | 0.236 | 39 |
| π/32 | [10^8.5, 10⁹) | 0.4429 | 0.5571 | 0.972 | 0.295 | 1.431 | 1.075 | 1.33 | 3.23 | 5,803,363 | 1.39 | 0.254 | 53 |
| π/32 | [10^9.5, 10¹⁰) | 0.4092 | 0.5908 | 0.976 | 0.365 | 1.310 | 0.974 | 1.34 | 3.20 | 61,398,284 | 1.45 | 0.271 | 73 |

π′ agrees with the template prime density per cell (1 − x^{−ρ})/(ρ log x) to 3 digits (0.2241 vs 0.2236 at the last π/16 band).
**Pattern 3.1 (geometric queue tail, sub-Poisson by a fixed factor)** [computed]. On every band with enough data, P(e ≥ h) decays
geometrically with rate κ = (1.50–1.66)·κ_P (π/16) and (1.31–1.43)·κ_P (π/32), the factor stable over five decades; equivalently
κ ≈ (3.2–3.6)·π′. With π′ ≍ 1/(ρ log x) this is the log² law of §2 (sup e ≈ log(#cells)/κ). Conjectured form for a proof unit:
  **(C3.1)** for every half-decade band B = [x₀, x₁) and every h ≥ 1: #{k : x_k ∈ B, e_k ≥ h} ≤ #{k : x_k ∈ B}·exp(−c·h·π′_c(x₁)),
  π′_c(x) := (1 − x^{−ρ})/(ρ log x) (the template idle fraction), with c = 2.5. Checked: π/16 and π/32, all bands 10⁴–10¹⁰ with ≥ 10³
  cells, all h; the largest admissible c is 2.94 (π/16, [10^9.5, 10¹⁰), h = 3) and 3.05 (π/32, [10⁴, 10^4.5), h = 4).
(C3.1) with any c > 0 gives sup e = O(ρ log² x) (take h = 2 log(#cells)/(c π′_c)); it is the statement U3 (first bound) or U1 (a rule with
a proved tail) would aim at. The single-cell Fano factor is 0.94–0.98: the sub-Poisson effect is not visible in one cell; it is built up
over windows (3.2).

## §4. Anatomy of the twenty largest excursions (task 1)

**4.1 Two exact identities** [proved here]. (I1) *Divisible arrivals are the system at a smaller scale.* For a g-integer d and lattice
indices j < k with x_j ≥ d: #{composites n ∈ (x_j, x_k] : d | n} = (k − j)/d + E(x_k/d) − E(x_j/d). *Proof.* In the free monoid n ↦ n/d is a
bijection from the multiples of d in (x_j, x_k] onto G ∩ (x_j/d, x_k/d]; none of these multiples is a g-prime (a g-prime divisible by d is
d ≤ x_j); and N(y) = ρ(y − 1) + 1 + E(y) for y ≥ 1 with ρ(x_k − x_j) = k − j. ∎ In particular the arrivals with smallest factor p₁ in a window
W are (k − j)/p₁ + ΔE(W/p₁), and E(x_k/d) = #{composites ≤ x_k divisible by d} − ρ(x_k/d − 1) is read off exactly from the per-cell
divisibility counts (checked: `verify/check_I1.py`, log `verify/logs/check_I1.log`).
(I2) *Exact bookkeeping of a burst.* For an excursion e_{a−1} = 0 < e_a, …, e_{k*} with build-up W = cells a..k* (ℓ = k* − a + 1 cells),
h := e_{k*} = Σ_W (c_i − 1) = Σ_classes (C_cls(W) − ℓ·w_cls) − ℓ·M(√x), where the classes are the smallest-factor ranges, w_q =
(1/q)Π_{p<q}(1 − 1/p) summed over the class, and M(z) = Π_{p≤z}(1 − 1/p) (telescoping: Σ_{q≤z} w_q = 1 − M(z); every composite ≤ x has its
smallest factor ≤ √x). By (I1) the p₁-class excess is exactly ΔE(W/p₁). The last term −ℓM(√x) is Legendre's prime share (the 2e^{−γ}
term of read-O F1).

**4.2 The data** [computed: `verify/anatomy.py` on the watch dumps of the second 10¹⁰ runs (`verify/run_multi.sh`; every composite of the
cells [a − 40, b] of each excursion, with its factor indices, plus 60 control windows); output `verify/logs/b16_1e10.anat.txt`,
`b32_1e10.anat.txt`]. Columns: height h, start x, build-up ℓ (cells), class excesses C − ℓw for smallest factor p₁ | p₂ | p₃ | p₄–p₁₀ |
p₁₁–p₁₀₀ | p₁₀₁–p₁₀₀₀ | > p₁₀₀₀, then −ℓM(√x) (the row sums to h), then ΔE(W/p_q) for q = 1, …, 5 (E's rise at the five smaller scales over
the dilated window) and the largest e at the lower scale inside W/p₁.

| # | h | x | ℓ | p₁ | p₂ | p₃ | p₄–₁₀ | p₁₁–₁₀₀ | p₁₀₁–₁₀₀₀ | >p₁₀₀₀ | −ℓM | ΔE(W/p_q), q = 1..5 | max e on W/p₁ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| π/16 #0 | 25 | 6.45·10⁹ | 55 | +4.5 | +5.4 | +1.1 | +2.6 | +11.0 | +7.5 | +6.4 | −13.5 | +4.5 +4.6 +0.1 +0.7 +2.1 | 5 |
| #1 | 25 | 6.57·10⁹ | 68 | +2.8 | +3.4 | +1.7 | +7.3 | +12.3 | +7.4 | +6.8 | −16.7 | +2.8 +1.1 +1.4 +1.2 +2.7 | 2 |
| #2 | 25 | 7.96·10⁹ | 34 | +5.4 | +2.2 | +1.9 | +8.7 | +5.7 | +7.2 | +2.3 | −8.3 | +5.4 +3.1 +6.2 +0.6 +3.8 | 6 |
| #3 | 24 | 9.92·10⁹ | 70 | +7.3 | +0.2 | +0.6 | +5.2 | +11.0 | +6.2 | +10.4 | −16.9 | +7.3 +0.9 +0.3 +4.1 +1.6 | 7 |
| #4 | 24 | 6.74·10⁹ | 83 | +6.6 | +5.1 | +2.2 | +1.9 | +12.4 | +6.1 | +10.0 | −20.3 | +6.6 +7.4 +2.6 +1.5 +3.1 | 7 |
| #5 | 24 | 4.98·10⁹ | 63 | +9.2 | +3.8 | +0.9 | +5.8 | +2.9 | +10.8 | +6.2 | −15.6 | +9.2 +4.7 −0.3 +0.4 +1.8 | 8 |
| #6 | 24 | 6.32·10⁹ | 41 | +6.4 | +4.6 | +2.6 | +5.0 | +5.8 | +2.6 | +7.1 | −10.1 | +6.4 +7.2 +3.8 +3.3 +1.6 | 6 |
| #7 | 24 | 8.95·10⁹ | 45 | +7.3 | −0.7 | +2.5 | +2.6 | +9.2 | +9.3 | +4.7 | −10.9 | +7.3 −0.2 +2.6 +1.1 +2.5 | 8 |
| #8 | 24 | 8.91·10⁹ | 32 | +7.0 | +3.3 | +3.9 | +2.9 | +6.9 | +4.3 | +3.4 | −7.8 | +7.0 +4.3 +6.3 +0.7 +0.9 | 6 |
| #9 | 23 | 6.66·10⁹ | 37 | +6.6 | +2.9 | +0.8 | +4.4 | +6.3 | +4.9 | +6.2 | −9.1 | +6.6 +2.7 +0.0 −0.6 −0.3 | 6 |
| mean of 20 (π/16) | 23.1 | | 54.9 | +5.68 | +2.64 | +1.80 | +5.49 | +8.08 | +6.56 | +6.27 | −13.43 | +5.68 +2.95 +1.94 +1.51 +1.71 | 5.5 |
| Poisson z of the mean | | | | +1.5 | +1.3 | +1.4 | +2.4 | +3.1 | +3.1 | +4.0 | | share with ΔE > 0: 1.00 .85 .90 .95 .90 | |
| mean of 20 (π/32) | 12.8 | | 15.4 | +3.03 | +0.76 | +0.59 | +2.01 | +4.56 | +5.12 | +3.42 | −6.64 | +3.03 +1.21 +0.82 +0.98 +0.53 | 2.4 |
| Poisson z of the mean | | | | +2.0 | +1.0 | +0.9 | +1.9 | +3.5 | +4.5 | +4.4 | | share with ΔE > 0: 1.00 .85 .90 .75 .60 | |

(Rows #10–#19 for π/16 and all twenty for π/32 are in the logs; z = excess/√(ℓw), the excess measured in Poisson standard deviations.)

**4.3 What the anatomy shows** [computed; the all-excursion averages by `verify/inherit.c`, lines XDEC of `verify/logs/b16_1e10.inh`,
`b32_1e10.inh`, which apply (I2) with the classes p₁ | p₂ | p₃ | p₄ | rough (> p₄) to every one of the 2.0·10⁸ (π/16) and 8.9·10⁷ (π/32)
excursions to 10¹⁰, checked to sum to h in each].
*P4.1 (inherited layer).* In all 40 top excursions ΔE(W/p₁) > 0 (mean +5.7 for π/16, +3.0 for π/32); in 16 of 20 (π/16) the dilated window
W/p₁ itself contains an excursion of height ≥ 4. ΔE(W/p_q) > 0 for q = 2, …, 5 in 60–95 % of them. A large burst at x sits on a rise of
the same system at x/p₁, x/p₂, …: the lower scale "was rising just before".
*P4.2 (coincidence layer).* The classes with smallest factor > p₁₀ carry 57 % (π/16) and 64 % (π/32) of the gross excess, each class at
+3 to +4.5 Poisson standard deviations; the excess is mostly in Ω = 2 (+8 to +32 per burst): semiprimes qp with q ∈ (p₁₀, √x], i.e.
simultaneous g-prime surpluses in the windows W/q at hundreds of scales x/q, each window shorter than one cell there (a 0/1 event per q).
*P4.3 (the rigid class cannot keep up).* Mean share of the height carried by each class, by height (π/16; π/32 in brackets):

| height | p₁ | p₂ | p₃ | p₄ | rough (> p₄) |
|---|---|---|---|---|---|
| 1 | 48 % [40 %] | 14 % [13 %] | 5 % [7 %] | 4 % [5 %] | 29 % [35 %] |
| 3 | 40 % [29 %] | 14 % [12 %] | 6 % [7 %] | 4 % [5 %] | 36 % [47 %] |
| 9–12 | 33 % [22 %] | 13 % [9 %] | 6 % [6 %] | 5 % [5 %] | 43 % [58 %] |
| ≥ 18 [13–17] | 28 % [28 %] | 12 % [7 %] | 6 % [4 %] | 5 % [4 %] | 49 % [57 %] |

(Shares of the ARRIVALS at 10¹⁰: p₁ 36 % [28 %], rough 45 % [55 %].) The p₁ class is the system at x/p₁ (I1), so its excess over a window is
at most the range of E there; its share of large bursts falls below its share of arrivals and the rough class takes over. Equivalently
(Theorem 5.1 below) e_k ≤ E(x_k/p₁) + τ + r_k^{(1)}, and at the top of the range the rough queue r^{(1)} is nearly as large as e itself.
**For the proof units.** U3: the inherited layer is controlled by induction on scale through (I1) at no cost; everything left is the
coincidence layer, a sum over q > p₁₀ of 0/1 events "W/q contains a g-prime" at well-separated scales — the place for a second-moment or
large-sieve bound. U1: a rule cannot remove composites; its only lever on a burst at x is the placement of g-primes at the scales x/q for
q in the coincidence range (q > p₁₀ = 64.7 for π/16, 118.1 for π/32; p₁₁ = 79.9, 128.3; p₁₀₀₀ ≈ 1.0·10⁴, 1.5·10⁴), all fixed by the time
the sweep passes x/p₁₁ — a look-ahead rule must therefore look at least a factor p₁₁ ahead to see the coincidence layer coming.
