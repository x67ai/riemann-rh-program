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
Per cell the generator writes c_k, e_k, c_k^{(1)} (composites whose smallest g-prime factor is p₁) and c_k^{(Ω=2)} (two factors), all uint8,
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
