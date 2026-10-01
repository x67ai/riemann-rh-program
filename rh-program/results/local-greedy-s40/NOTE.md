# NOTE — unit `local-greedy-s40`: S7, integer-level feedback acting only at prime powers (the prime-local class on ℕ)

Session 40, 2026-10-01. Writer: Opus 5.5 (agent). Labels as in `u-offsurgery-s39/NOTE.md`: **[proved here]**, **[computed]** (script +
log under `verify/`), **[quoted]** (source on disk, page/line), **[recalled, unverified]** (never load-bearing), **[novelty: single-check]**.
Notation as there: [α, β]-system: ψ_P(x) = x + O(x^{α+ε}), N_P(x) = ρx + O(x^{β+ε}). **Conjecture U** (fr/NOTE §7.2): every discrete
[α, β]-system has α ≤ max{½, 2β}. Paths: `fr/` = `results/novel-wave-s37/beurling-frontier/`, `uo/` = `results/u-offsurgery-s39/`.

## §0. Close (filled last)

**STOP LINE (c) MET — reported before proving (SHARED.md, block of 11:49 IST).** S7(ρ) — the integer-greedy rule allowed to act
only at prime powers, so every g-prime is a prime power and a_n is multiplicative (Lemma 1.1) — crosses Conjecture U's line
numerically, and the crossing is zero-driven. At ρ = 0.6, X = 4·10⁹ (exact counts; generator re-derived independently, 0 mismatches
to 10⁷; ρ = 1 returns the primes): **β ≈ 0.26–0.31** (running sup of |E| on windows [10^k, 4·10⁹), k = 3…7, falling as the window
starts later) and **α ≈ 0.80–0.82 by three routes** — running sup of |ψ_P − x| (0.796–0.810), the zeros of ζ_P (ρ₁ = 0.8209965 +
11.0877411i and ρ₂ = 0.8052963 + 20.2490762i, stable to 2·10⁻⁵ from X = 10⁷ to 10⁹, each with winding number 1 on a box at X = 10⁹;
no other zero in σ ≥ 0.70 below height 100), and the Beurling Möbius sums (γ = 0.795–0.817, which Neamah–Hilberdink Thm 1 forces
to equal α when β < ½). **α − max{½, 2β} = +0.18…+0.29 on every window**, over six and a half decades; ρ = 0.75, 0.8, 0.9, 1.1 are
also above the line at 10⁹ from 10⁴–10⁵ on (+0.05…+0.31), and their top zeros (X = 10⁸) sit at Re 0.806, 0.746, 0.840 for
ρ = 0.75, 0.8, 1.1 (§3.6); ρ = 1.25 sits below the line; ρ = 1.5 runs away (§2). The prime-side
fluctuation is coherent, not a random walk (sup|T|/V = 12.6 at 10⁹, growing like x^{0.3}, §3.5).
**The capped variant S7^{≤2}(0.6) (m_n ≤ 2; brief task 4) is the K-candidate with tame multiplicities** (§4.2): a_n ≪ n^ε is proved
(Lemma 4.1: the Ramanujan condition), g(p) = ±1 at 96.6 % of primes (a feedback-chosen pseudo-character), and at X = 10⁹ β ≈ 0.19–0.22,
α ≈ 0.79–0.83 (route 1), the zero z₁ = 0.8243658 + 11.0306646i (route 2, boxed at 10⁹), γ = 0.78–0.82 (route 3): **α − 2β =
+0.36…+0.44**, the hypothesis of its K-theorem (|C(u)| ≤ u^{0.40}) holding at every computed u ∈ [10³, 10⁹] (constant ≤ 0.93).
**Close: K-candidate (both systems) + K-conditional theorems + G.**
- **K₇^{≤2} and K₇ (Theorems, §4)** [proved here, modulo the floating-point evaluation of F_X on the box boundaries]: if
  |N_P(u) − 0.6⌊u⌋| ≤ u^{0.40} for all u > 10⁹, then **Conjecture U is false** — for P = S7^{≤2}(3/5) (zero in [0.8044, 0.8444] ×
  [11.0107, 11.0507], a_n ≪ n^ε) and for P = S7(3/5) (zero in B₁ = [0.8010, 0.8410] × [11.0677, 11.1077]). On the computed range the
  hypothesis holds with constant ≤ 0.93 on all of [10³, 10⁹] and 0.10 in the top decade for S7^{≤2}; 0.35 in the top decade for S7.
  S5's analog (uo §4) needed θ ≤ 0.35 against data ≈ 0.30 and had exploding multiplicities; S7^{≤2} needs θ ≤ 0.40 against data
  ≈ 0.19–0.22 with bounded ones.
- **G (the exact missing lemma): Lemma H₇^{≤2} / H₇** (§4), a growth bound for one explicit Lindley-type recursion that acts only at
  prime powers: for S7, E(x) is, within ½, the excess of g-integers since the last prime power at which the rule added a copy; for
  S7^{≤2} a prime power raises E by at most A(q) + 2 − ρ, so a deep deficit is repaid over several prime powers (inf E = −197.8).
  Smallest undecided class: S7^{≤2}(ρ) and S7(ρ), ρ ∈ [0.6, 1.1].
- **Multiplicities — the brief's expectation corrected** [proved + computed]: they are bounded by ρ·(prime-power gap) + 1 + ρ
  (Lemma 1.2), so S5's factorization-counting explosion cannot occur, but they are not small: 84–94 % of primes are refused in
  [10⁸, 10⁹), the rest receive m_p up to 79–219, mean m_p = 1.000; the refused fraction rises with x. E's records come from clusters of
  moderate a_n (10–150), not from one multiplicity (sup E/max a_n = 1.7; S5: 1.0).
- **T-side facts** [quoted + proved]: Klurman Thm 1.6 and Tao Cor. 1.2 concern ±1 functions and do not reach S7's g (values up to 78);
  the hyperbola bound gives only β ≤ κ/(1 + κ − μ) = 2/3 here (§5(iii)); E is a ~30× cancellation between two terms of size M_g
  (§2.4). No theorem of this unit says the prime-local class cannot cross U; the periodic sub-class cannot without an off-line
  Dirichlet zero (uo §3.3), and Hilberdink 2012 confines periodic-error members to finite deletions.
Consequence for the record: a second non-surgery discrete system in the corner β < α/2, now with multiplicative coefficients — the
numerical counterexample to DMV's p. 4 speculation and the support for BDR's populating conjecture no longer rest on S5's
multiplicities. U implies RH, not conversely: nothing here touches RH.

## §1. The object, the generator, the controls

**Definition (BRIEF).** Fix ρ > 0. Walk n = 2, 3, …; A(n) = number of representations of n by the g-primes chosen so far; if n = p^k
is a prime power, m_n := max(0, ⌊ρ(n − 1) + 1 − N(n − 1) − A(n) + ½⌋) copies of n become g-primes; otherwise m_n := 0;
a_n = A(n) + m_n, N(n) = N(n − 1) + a_n. Write E(n) := N(n) − ρ(n − 1) − 1 (sup of N(x) − ρx − (1 − ρ) over [n, n + 1) is E(n), the
inf is E(n) − ρ), C(y) := N(y) − ρ⌊y⌋.

**Lemma 1.1 (structure)** [proved here]. Every g-prime is a prime power, so a_n = Π_{p^e‖n} c_p(e) with c_p(e) = [u^e] F_p(u),
F_p(u) = Π_{k≥1}(1 − u^k)^{−m_{p^k}}; a is multiplicative, ζ_P(s) = Σ a_n n^{−s} = Π_p F_p(p^{−s}) = ζ(s)L_g(s) for σ > 1, where
g = μ ∗ a is multiplicative with g(p^e) = c_p(e) − c_p(e − 1), g(p) = m_p − 1 ∈ {−1, 0, 1, …}.
*Proof.* A product of g-primes p₁^{k₁}⋯ (prime powers) equals n iff, for each prime p, the g-primes that are powers of p multiply to
the p-part of n; representations therefore factor over p, and the number of ways to write p^e as an unordered product of the
chosen powers of p (with multiplicities m_{p^k}) is [u^e]Π_k(1 − u^k)^{−m_{p^k}}. The Euler product converges absolutely for
σ > 1 because N(x) = ρx + o(x) on the data (§2) — as a statement for all x this is part of the system's definition as a density-ρ
system, not proved. g = μ ∗ a has local factor (1 − u)F_p(u). ∎

**Lemma 1.2 (the downward side is bounded by prime-power gaps)** [proved here]. After every prime-power step, E(q) > −½; for
consecutive prime powers q < q′ and q ≤ n < q′, E(n) > −½ − ρ(n − q); hence inf_{x≤X}(N(x) − ρx − (1 − ρ)) > −½ − ρ·G(X) with G(X)
the largest gap between consecutive prime powers up to X, and every multiplicity satisfies m_q < ρ + 1 + ρ·G(q).
*Proof.* Put y := ρ − E(q − 1) − A(q) + ½, so m_q = max(0, ⌊y⌋) and E(q) = E(q − 1) + A(q) + m_q − ρ = ½ − y + m_q. If ⌊y⌋ ≥ 1
then E(q) = ½ − {y} ∈ (−½, ½]; otherwise y < 1 and E(q) = ½ − y > −½. Between prime powers a_n ≥ 0, so E decreases by at most ρ per
step. Finally m_q ≤ y ≤ ρ + ½ − E(q − 1) (as A(q) ≥ 0) < ρ + 1 + ρ(q − 1 − q_prev), q_prev the previous prime power. ∎
(The unconditional size of G(X) is a printed gap theorem I have not opened: **[recalled, unverified]** G(X) ≪ X^{0.525}; Cramér's
conjecture would give log²X. On the data, max m_p = 79 at ρ = 0.6, X = 10⁹, against ρ·(max prime gap below 10⁹) — the gap itself
[recalled, unverified] 282 — the rule fills deficits well before the worst gap.)

**Generator** [computed]. `verify/s7gen.c`: segmented over [L, R) with R − L ≤ L, so every composite non-prime-power n in a segment
has all prime-power factors ≤ n/2 < L, already decided; prime powers in the segment are decided in increasing order (A(p^e) =
c_p^{old}(e) needs only m_{p^k}, k < e). Exact integer arithmetic for the rule: ρ = num/den, the floor computed in int128 as
⌊(2num(n − 1) + 2den(1 − N − A) + den)/(2den)⌋. **Irrational ρ** is not used here (the brief's densities are rational); the generator
takes num/den up to 10¹⁸, so an irrational ρ is run through a continued-fraction convergent p/q, and the run equals the true S7(ρ)
up to X unless some ρ(n − 1) + ½ falls within X|ρ − p/q| of an integer — a condition the int128 arithmetic can check at each prime
power. Memory: one byte per odd q ≤ X/2 (m_q), segment arrays of 2²² entries; 387 MB at X = 10⁹; 50 s per 10⁹.
**Independent generator** `verify/s7dp.c`: the additive DP of S5's generator (`uo/verify-F/s5gen_F.c`) — "a[kq] += a[k], k
increasing" for each copy of each g-prime — with the rule allowed only at prime powers; no multiplicativity is used.

**Controls** (`verify/check_s7.py`, `verify/logs/check_s7_1e7.log`, `verify/logs/controls/`) [computed]: (a) ρ = 1 returns the 664,579
primes ≤ 10⁷ with E ≡ 0 (both generators); (b) a_n identical term by term over n ≤ 10⁷ between s7gen and s7dp at ρ = 0.8, 1.5, 1
(0 mismatches; N(10⁷), sup E, inf E, max a_n agree); (c) a(mn) = a(m)a(n) on 10⁶ random coprime pairs (m log-uniform): 0 failures;
(d) Σ_{d|n} g(d) = a_n for n ≤ 10⁵: 0 mismatches; (e) max a_n against d(n) at 10⁷, ρ = 0.8: max a_n = 72 at 5,825,921 (d = 4);
max a_n/d(n) = 23.5 at the prime 9,353,411 (m = 47); a_n > d(n) for 287,082 n ≤ 10⁷.

## §2. The numbers [computed]

Logs: `verify/logs/sweep/s7_v0_r<num>-<den>_X<X>.log` (20 log-bins per decade: sup/inf E over real x, RMS of E at integers,
sup|ψ_P − x|, max/min M_g, sup|Tt|, sup|W|; per-decade prime decisions; E records), fits `verify/fit7.py` →
`logs/sweep/fits_v0_1e8.log`, `fits_v0_1e9.log`; half-decade tables `logs/sweep/halfdecade_r06_r08_1e9.log`. Exponents are
least-squares slopes of log(running sup) against log x over the bins of [10^k, X); b from sup|E|, a from sup|ψ_P − x|, μ from sup|M_g|.

**2.1 X = 10⁹, six densities** (ρ = 1.5 runs away already at 10⁷: N(10⁸)/10⁸ = 1.5099, b ≈ 0.9 — not a density-ρ system on the range):

| ρ | sup E | inf E | sup\|ψ_P − x\| | sup\|M_g\| | max a_n | max m_p | b_sup, k = 3…7 | a_sup, k = 3…7 | a − 2b, k = 3…7 |
|---|---|---|---|---|---|---|---|---|---|
| 0.6 | 948.8 | −93.2 | 5.57·10⁶ | 9087 | 550 | 79 | .315 .303 .281 .278 .264 | .794 .801 .802 .811 .808 | **+.16 +.20 +.24 +.26 +.28** |
| 0.75 | 763.0 | −93.0 | 9.14·10⁵ | 9212 | 234 | 93 | .333 .316 .276 .261 .267 | .718 .734 .735 .760 .843 | +.05 +.10 +.18 +.24 +.31 |
| 0.8 | 1048 | −103.6 | 1.03·10⁶ | 11610 | 270 | 104 | .353 .329 .297 .296 .276 | .715 .723 .712 .685 .696 | +.01 +.07 +.12 +.09 +.14 |
| 0.9 | 969.8 | −106.2 | 7.17·10⁵ | 6596 | 247 | 102 | .366 .340 .307 .282 .287 | .704 .699 .707 .733 .736 | −.03 +.02 +.09 +.17 +.16 |
| 1.1 | 3839 | −174.4 | 3.68·10⁶ | 20270 | 825 | 142 | .416 .393 .337 .274 .240 | .796 .801 .791 .790 .787 | −.04 +.02 +.12 +.24 +.31 |
| 1.25 | 23000 | −219 | 1.05·10⁷ | 45230 | 1827 | 219 | .466 .451 .425 .426 .454 | .830 .828 .826 .815 .843 | −.10 −.07 −.02 −.04 −.07 |

**X = 4·10⁹, ρ = 0.6** (`logs/sweep/s7_v0_r3-5_X4000000000.log`, `fits_v0_r06_4e9.log`; 1.17 GB, 4 min): sup E = 1304.4,
inf E = −105.6, sup|ψ_P − x| = 1.75·10⁷, sup|M_g| = 19,814, max a_n = 825, max m_p = 106; b_sup (k = 3…7) = .307 .295 .276 .272 .259,
a_sup = .796 .802 .803 .810 .807, **a − 2b = +.18 +.21 +.25 +.27 +.29**; local slope of sup E from 10⁹ to 4·10⁹: 0.23.
RMS exponents b_rms (k = 3…7) at ρ = 0.6: .265 .243 .228 .217 .204; the M_g exponent μ ≈ 0.50–0.52 at every density ≤ 1.1.
Integer-error fits fall as the window starts later at every ρ ≤ 1.1, up to rises ≤ 0.01 on the last window at ρ = 0.75 and 0.9
(no sign of a rising exponent on [10³, 10⁹]); α-fits are flat to ±0.03 except ρ = 0.75 (0.72 → 0.84).

**2.2 Anatomy: refused, doubled, tripled** (decade [10⁸, 10⁹), 45,086,079 primes; `D 8` lines of the logs). Fractions with
m_p = 0 / 1 / 2 / 3 / ≥ 4: ρ = 0.6: .844 / .022 / .017 / .017 / .100; 0.75: .854 / .017 / .016 / .018 / .095; 0.8: .865 / .013 /
.016 / .014 / .093; 0.9: .868 / .011 / .018 / .012 / .092; 1.1: .912 / .004 / .009 / .004 / .071; 1.25: .940 / .001 / .003 / .003 /
.052. Mean m_p per decade = 1.000 ± 0.005 at every density (the density condition Σ(m_p − 1)/p ≈ 0 is met on average). Higher prime
powers with m > 0 in that decade: 134–288. The refused fraction RISES with x (ρ = 0.8: .80 in [10⁶, 10⁷), .865 in [10⁸, 10⁹)), so the
support of a thins like Π_{refused p ≤ x}(1 − 1/p) and the values on it grow: the system becomes lumpier with x — the opposite of
the brief's expectation that local multiplicities stay small. Lemma 1.2 caps them by ρ·(prime-power gap) + 1 + ρ.

**2.3 Where E's records come from** (`logs/sweep/s7_v0_r3-5_X1000000000_dump.log`, lines `rec`). Records of E at ρ = 0.6 are
reached at moderate a_n (10–150), in bursts (e.g. 424.2, 437.8, 462.8 at n = 35,885,294, …333, …338): E's excursions are clusters
of large-valued g-integers, not a single multiplicity (contrast S5, where sup E equals the largest a_n: free-greedy-s40/CHARTER §0).
sup E/max a_n = 1.7 at ρ = 0.6, X = 10⁹.

**2.4 The decomposition E = Tt + W − (1 − ρ)** (task 5(i); Tt(n) = n(Σ_{d≤n} g(d)/d − ρ), W(n) = −Σ_{d≤n} g(d){n/d}). Neither
dominates: both are of the size of M_g and cancel to leave E. At ρ = 0.6 on [3.16·10⁸, 10⁹): sup|Tt| = 9055, sup|W| = 8973,
RMS 3028 and 3027, against sup E = 948.8 and RMS(E) = 95.4. The RMS ratio Tt : E GROWS with x — 2.0, 3.6, 6.2, 13, 32 at the
half-decades starting 10⁴, 10⁵, 10⁶, 10⁷, 3.16·10⁸ (ρ = 0.6; ρ = 0.8 alike): the two terms grow like M_g, E much more slowly. So the hyperbola-type bound through M_g (§5) is far from sharp here: E ≈ x^{0.3} while M_g ≈ x^{0.5}.

## §3. Route 2: the zeros of ζ_P (ρ = 0.6) [computed]

**3.0 The function and the truncation bound.** For an ℕ-supported system, ζ_P(s) − ρζ(s) = Σ_{n≥1}(a_n − ρ)n^{−s} has partial sums
C(y) = N(y) − ρ⌊y⌋; if (H_θ) |C(u)| ≤ u^θ for all u > X, partial summation gives convergence in σ > θ and
|ζ_P(s) − F_X(s)| ≤ |C(X)|X^{−σ} + |s|∫_X^∞ u^{θ−σ−1}du = |C(X)|X^{−σ} + |s|X^{θ−σ}/(σ − θ), F_X(s) := ρζ(s) + Σ_{n≤X}(a_n − ρ)n^{−s}
(uo §2.1, §4 step (1); the argument uses nothing about S5). Since ζ_P = ζ·L_g (Lemma 1.1), the zeros of ζ_P in σ > ½ below height
100 are the zeros of L_g there (ζ has none off the line below height 100 **[recalled, unverified]**; not load-bearing: the zeros
found below are zeros of F_X, whatever their origin).
**Instruments.** `verify/zline.c` (memory-mapped a_n; vertical lines by recurrence in t, horizontal segments by recurrence in σ,
point mode with D_X and D_X′, Taylor-moment mode M_k = Σ(a_n − ρ)n^{−s₀}(−log n)^k/k!; ζ by Euler–Maclaurin, M = 60, ten Bernoulli
terms, as uo/verify/zscan.c — checked here against mpmath at 0.75 + 30i, 0.6 + 14.2i, 0.9 + 77.7i to all printed digits);
`verify/scan7.sh` + `verify/zcount7.py` (argument principle on the 10 × 10 boxes of [0.55, 1.10] × [0.1, 100], lines σ = 0.55, …,
1.10, t-step 0.025; horizontal segments at t = 0.1, 10, …, 100, σ-step 0.005); `verify/newton7.py` (Newton, all zeros per pass).

**3.1 Strip counts at X = 10⁷** (`verify/logs/zeros/zcount_r06_1e7.log`; the a_n are the first 10⁷ of the 10⁹ dump). Winding numbers
of F_X on the strips × [0.1, 100]: σ ∈ [1.00, 1.10], [0.95, 1.00], [0.90, 0.95], [0.85, 0.90]: 0 (largest phase step on the box
contours 0.10, 0.15, 0.27, 0.76 rad); **[0.80, 0.85]: 2** (boxes × [10, 20] and × [20, 30]; step ≤ 1.59 rad, min|F| 0.024);
[0.75, 0.80], [0.70, 0.75]: 0 (≤ 1.59, 0.71 rad); [0.65, 0.70]: 4, [0.60, 0.65]: 13, [0.55, 0.60]: 10 — these last three with
phase steps up to 2.95 rad, so their counts are indicative only (aliasing possible; the zeros there are not refined here). So
below height 100 and right of σ = 0.70 F_X has exactly two zeros, and the largest real part is that of the zero near 11.09.
Hilberdink 2005 Cor. 2(b) (via uo §5) predicts infinitely many zeros in every strip η′ < σ < 1 with η′ ∈ (β, ½) when β < ½; the
27 zeros counted in [0.55, 0.70] are consistent with that.

**3.2 Newton and stability under X** (`logs/zeros/newton_r06_X1e7.log`, `…_X1e8.log`, `…_X1e9.log`; |F| ≤ 4·10⁻¹³ at the end):

| X | ρ₁ | ρ₂ |
|---|---|---|
| 10⁷ | 0.8209861 + 11.0877395i | 0.8052896 + 20.2491013i |
| 10⁸ | 0.8210037 + 11.0877501i | 0.8052939 + 20.2490886i |
| 10⁹ | **0.8209965 + 11.0877411i** (\|F′\| = 3.412) | **0.8052963 + 20.2490762i** (\|F′\| = 4.406) |

Stable to ~2·10⁻⁵ over a hundredfold range of X. Amplitude: 2x^{0.821}/|ρ₁| + 2x^{0.805}/|ρ₂| ≈ 6·10⁶ at x = 10⁹ against the observed
sup|ψ_P − x| = 5.57·10⁶ (§2.1): the two zeros account for route 1's α ≈ 0.80.

**3.3 Winding-number boxes at X = 10⁹** (`verify/cert7.py`; `logs/zeros/cert_r06_z1_1e9.log`, `…_z2_1e9.log`). F_X on ∂B evaluated
from 25 Taylor moments at the centre (one pass over the 10⁹ coefficients; |M₂₄|h²⁴ ≤ 3·10⁻³⁹), validated at the four corners by
direct sums (agreement ≤ 1.8·10⁻¹²); 400 boundary points.
- B₁ = [0.8010, 0.8410] × [11.0677, 11.1077]: winding number 1.000000, min_{∂B₁}|F_X| = 0.0654, largest phase step 0.021 rad;
  C(10⁹) = −2. Tail bound max over ∂B₁ under H_θ: 0.00069 (θ = 0.30), 0.00216 (0.35), **0.00683 (0.40; ratio 9.6)**, 0.0220 (0.45).
- B₂ = [0.7853, 0.8253] × [20.2291, 20.2691]: winding number 1.000000, min|F_X| = 0.0838; tail 0.0018, 0.0056, 0.0179 (θ = 0.40;
  ratio 4.7), 0.058.
**H_θ on the computed range** (`verify/hcheck.c`, `logs/zeros/hcheck_r06_1e9.log`): max |C(n)|/n^θ per decade [10^k, 10^{k+1}),
k = 3…8: θ = 0.40: 1.05, 0.86, 0.93, 0.60, 0.45, **0.35**; θ = 0.35: 1.53, 1.43, 1.74, 1.23, 1.05, 0.88; θ = 0.32: …, 1.54.
The θ = 0.40 ratio falls by a factor ≈ 0.75 per decade, as |C| ≈ u^{0.28} would make it.

**3.4 Third route: the Beurling Möbius sums** (`logs/sweep/s7_v0_r3-5_X4000000000.log`, lines `MP`; fit in
`logs/sweep/fits_v0_r06_4e9.log`). μ_P = a^{∗−1} (local factor 1/F_p(u)), M_P(x) = Σ_{n≤x} μ_P(n); control: at ρ = 1 the generator
returns M(10⁶) = 212, equal to an independent numpy sieve (`logs/controls/mertens_1e6.log`). At ρ = 0.6: sup|M_P| = 2.9·10⁴,
1.8·10⁵, 1.4·10⁶, 4.4·10⁶ by 10⁷, 10⁸, 10⁹, 4·10⁹; exponent γ over [10^k, 4·10⁹), k = 3…7: 0.795, 0.808, 0.807, 0.814, 0.817.
Neamah–Hilberdink Thm 1 (§5(v)) forces γ = α when β < ½: the measured γ equals route 1's α and route 2's Re ρ₁ to ±0.02.

**3.5 The prime-side fluctuation is coherent, not a walk** (`verify/analyze_x.py`, `logs/sweep/analyze_x_r06_1e9.log`). With
T(x) = Σ_{p≤x}(m_p − 1)log p (the prime part of ψ_P − ψ; T(10⁹) = 3.73·10⁶ against ψ_P(10⁹) − 10⁹ = 3.78·10⁶) and the walk scale
V(x) = (Σ_{p≤x}(m_p − 1)²log²p)^{1/2} (the size T would have with independent signs), sup|T|/V = 1.4, 2.0, 3.2, 3.5, 5.3, 12.6 at
x = 10⁴, 10⁵, 10⁶, 10⁷, 10⁸, 10⁹. The ratio grows like x^{0.3} ≈ x^{Re ρ₁ − ½}: the m_p − 1 are long-range correlated exactly as an
explicit formula with a zero at 0.82 + 11.09i requires. So route 1's a_sup is not the artifact flagged in the 11:49 SHARED block.

**3.6 Route 2 at ρ = 0.75, 0.8, 1.1** (`verify/run_family.sh`: a_n to 10⁸, scans of F_X at X = 10⁷ on [0.70, 1.00] × [0.1, 100],
`verify/zmap.py` to locate, Newton at 10⁸; logs `logs/zeros/zcount_r{075,08,11}_1e7.log`, `zmap_family_1e7.log`,
`newton_r{075,08,11}_X1e{7,8}.log`; moves 10⁷ → 10⁸ ≤ 1.1·10⁻⁴). Zero counts in the σ-strips [0.70, 0.80] / [0.80, 0.90] / [0.90, 1.00]:

| ρ | counts | top zero (X = 10⁸) | further zeros (X = 10⁸) | a_sup at 10⁹ | α − 2b_sup (route 2, k = 3…7 range) |
|---|---|---|---|---|---|
| 0.75 | 3 / 1 / 0 | 0.80563 + 92.34370i | 0.75449 + 46.69157i, 0.72829 + 29.76598i, 0.70844 + 30.70061i | 0.72–0.84 | +0.14…+0.28 |
| 0.8 | 3 / 0 / 0 | 0.74647 + 30.69772i | 0.74615 + 29.85767i, 0.73874 + 59.17205i | 0.69–0.72 | +0.04…+0.19 |
| 1.1 | 6 / 2 / 0 | 0.83989 + 20.33964i | 0.81395 + 29.98087i (+ six in [0.70, 0.80], not refined) | 0.79–0.80 | +0.01…+0.36 |

Route 2 tracks route 1 at every density tried; the crossing is clear at 0.6 and 0.75, marginal on early windows at 0.8, and
window-dependent at 1.1 (its b-fits fall from 0.42 to 0.24). No box certificates were made at these three densities.

## §4. What is proved: U reduces, for S7(3/5), to one growth bound with room

**Theorem K₇ (conditional refutation of U)** [proved here, modulo the floating-point evaluation of F_X on ∂B₁ recorded in §3.3].
Let P = S7(3/5) and C(u) = N_P(u) − 0.6⌊u⌋. If (H_θ) |C(u)| ≤ u^θ for all u > 10⁹ holds for some θ ≤ 0.40, then ζ_P has exactly one
zero in B₁ = [0.8010, 0.8410] × [11.0677, 11.1077], P is an [α, β]-system with α ≥ 0.8010 and β ≤ θ, and **Conjecture U is false**
(α ≥ 0.8010 > 0.80 ≥ 2β, and α > ½).
*Proof.* Word for word the proof of uo §4 Theorem K′, which uses only that P is ℕ-supported: (1) under H_θ, Σ(a_n − 0.6)n^{−s}
converges in σ > θ and ζ_P = F_X + T_X with |T_X| ≤ |C(X)|X^{−σ} + |s|X^{θ−σ}/(σ − θ); (2) on ∂B₁, |T_X| ≤ 0.00683 < 0.0654 ≤ |F_X|,
so by Rouché ζ_P has as many zeros in B₁ as F_X, namely the winding number 1; (3) N_P(x) − 0.6x = C(x) − 0.6{x} = O(x^θ); (4)
ψ_P(x) − x = O(x^σ) with σ < Re ρ₁ would make −ζ_P′/ζ_P − s/(s − 1) = s∫(ψ_P − x)x^{−s−1}dx analytic at the zero, a contradiction. ∎
The Rouché step alone survives to θ ≈ 0.47 (ratio 2.97 at θ = 0.45); the U-conclusion needs 2θ < 0.8010.

**Lemma H₇ (the exact missing statement).** For S7(3/5): |N_P(u) − 0.6⌊u⌋| ≤ u^{0.40} for all u > 10⁹. In Lindley form: E(x)
equals, within ½, the excess N(x) − N(q*) − 0.6(x − q*) since the last prime power q* ≤ x at which the rule added a copy (Lemma 1.2's
proof), so H₇ says (a) that excess stays ≤ x^{0.40} — the upward side, the clusters of §2.3 — and (b) the deficit stays ≥ −x^{0.40}.
Lemma 1.2 reduces (b) to prime-power gaps G(x) ≤ (x^{0.40} − 1.6)/0.6; the best gap bound I know of, x^{0.525} [recalled,
unverified], does not reach that, so even the downward half is not unconditional by this route (the data: inf E = −93.2 at 10⁹,
far above −0.6·G). Verified on [10⁴, 10⁹] with constant ≤ 0.93 and 0.35 in the top decade; S5's Lemma H needed θ ≤ 0.35 against
data ≈ 0.30, S7's needs θ ≤ 0.40 against data ≈ 0.26–0.28: more room, same logical position.
**"Tame multiplicities" — what holds and what does not.** Multiplicities are bounded by ρ·(prime-power gap) + 1 + ρ (Lemma 1.2), so
a_n is multiplicative with local values that are polylogarithmic if Cramér's conjecture holds [recalled, unverified]; but they are
NOT bounded (max m_p = 79 at 10⁹) and the refused fraction rises with x (§2.2), so a_n ≪ n^ε is not proved here (§8, UT-L4).

**4.2 The capped variant S7^{≤2}: tame by construction** (brief task 4, variant "cap m_n ≤ 2", `s7gen` variant 2: m_n := min(m_n, 2)).
**Lemma 4.1** [proved here]. If every m_{p^k} ≤ 2, then a_n ≪_ε n^ε for every ε > 0.
*Proof.* Coefficientwise c_p(e) ≤ p₂(e) := [u^e]Π_{k≥1}(1 − u^k)^{−2} (all coefficients are ≥ 0 and (1 − u^k)^{−m} ≤ (1 − u^k)^{−2}
coefficientwise for m ≤ 2). For 0 < x < 1, 1 − x^j = (1 − x)(1 + ⋯ + x^{j−1}) ≥ j(1 − x)x^{j−1}, so x^j/(1 − x^j) ≤ 1/(j(1 − x)) and
log Σ_e p₂(e)x^e = 2Σ_{j≥1} j^{−1}x^j/(1 − x^j) ≤ (2/(1 − x))Σ_j j^{−2} = π²/(3(1 − x)). With 1 − x = 1/√e (the exponent e ≥ 4; −log(1 − δ) ≤ δ/(1 − δ)):
x^{−e} ≤ exp(√e/(1 − 1/√e)) ≤ exp(2√e), so p₂(e) ≤ exp((2 + π²/3)√e) ≤ exp(6√e); directly p₂(1), p₂(2), p₂(3) = 2, 5, 10. Hence
c_p(e) ≤ exp(7√e) for all e ≥ 1, and a_n ≤ exp(7Σ_{p|n}√e_p) ≤ exp(7√(ω(n)Ω(n))) (Cauchy–Schwarz). Ω(n) ≤ log₂n, and n ≥ ω! ≥
(ω/2.72)^ω (Euler's number; the product of the first ω primes is ≥ ω!) gives ω(n) ≪ log n/log log n; so a_n ≤ exp(O(log n/√(log log n))) = n^{o(1)}. ∎
So S7^{≤2} satisfies the Ramanujan condition of Révész–Pintz's class (ℕ-supported, a_n ≪ n^ε); on the data a_n ≤ 72, a_n > d(n) for
15,033 n ≤ 10⁹ only, max a_n/d(n) = 2.5. The price of the cap: the rule can no longer refill a deficit at one prime, so the
downward side grows (inf E = −197.8 against −93.2 uncapped) — and yet sup|E| falls fourfold.
**Route 1 at X = 10⁹, ρ = 0.6** (`logs/sweep/s7_v2_r3-5_X1000000000.log`, `fits_v2_r06_1e9.log`) [computed]: m_p = 0 / 1 / 2 for
24,626,463 / 1,710,292 / 24,510,779 primes ≤ 10⁹ (so g(p) = m_p − 1 = ±1 for 96.6 % of primes, in nearly equal numbers — a
feedback-chosen ±1 pseudo-character at the primes; higher prime powers with m > 0 in [10⁸, 10⁹): 1,063, of which 990 with m = 2); sup E = 218.4, inf E = −197.8, sup|ψ_P − x| = 5.0·10⁶, sup|M_g| =
7803; b_sup (k = 3…7) = .215 .207 .204 .204 .192, b_rms = .152 .138 .126 .120 .113, a_sup = .794 .804 .804 .806 .827;
**a − 2b = +.36 +.39 +.40 +.40 +.44** — a wider crossing than the uncapped system's, with provably tame coefficients.
**Route 2 and route 3** [computed] (`logs/zeros/zcount_v2r06_1e7.log`, `newton_v2r06_X1e{7,8,9}.log`, `cert_v2r06_z1_1e9.log`,
`hcheck_v2r06_1e9.log`; a_n dump `/private/tmp/rh-s40-local-greedy/a_v2r06_1e9.u16`): at X = 10⁷ F_X has exactly two zeros in
[0.70, 1.00] × [0.1, 100] (none with σ ≥ 0.85; phase steps ≤ 1.23 rad on the boxes holding them); Newton at X = 10⁷, 10⁸, 10⁹ gives
**z₁ = 0.8243658 + 11.0306646i** (|F′| = 3.617) and z₂ = 0.7665284 + 20.2045626i, stable to 9·10⁻⁶ — near the uncapped ρ₁, ρ₂ (the
two systems share their early decisions). Box B^{≤2} = [0.8044, 0.8444] × [11.0107, 11.0507] at X = 10⁹: winding number 1.000000,
min|F_X| = 0.0692, phase step ≤ 0.021 rad, corners agree with direct sums to 1.7·10⁻¹², C(10⁹) = −20; tail bound under H_θ: 0.00064,
0.00199, **0.00629 (θ = 0.40, ratio 11.0)**, 0.0202 (0.45). H_θ on the data: max|C(n)|/n^{0.40} per decade = 0.93, 0.52, 0.34, 0.21,
0.15, 0.10 (k = 3…8; ≤ 0.93 on all of [10³, 10⁹]); max|C(n)|/n^{0.30} in the top decade 0.66. Beurling Möbius exponent γ =
.783 .802 .803 .814 .815 (`fits_v2_r06_1e9.log`), equal to α as Neamah–Hilberdink requires.
**Theorem K₇^{≤2}** [proved here, modulo the floating-point evaluation of F_X on ∂B^{≤2}]. Let P = S7^{≤2}(3/5). If |N_P(u) −
0.6⌊u⌋| ≤ u^θ for all u > 10⁹ with θ ≤ 0.40, then ζ_P has exactly one zero in B^{≤2}, P is an [α, β]-system with α ≥ 0.8044 > 2θ,
β ≤ θ, and a_n ≪ n^ε (Lemma 4.1) — and **Conjecture U is false**. *Proof.* As Theorem K₇, with 0.00629 < 0.0692 on ∂B^{≤2}. ∎
**Lemma H₇^{≤2}** (the exact missing statement): |N_P(u) − 0.6⌊u⌋| ≤ u^{0.40} for all u > 10⁹, for P = S7^{≤2}(3/5) — true with
constant ≤ 0.93 at every computed u ≥ 10³ and 0.10 in the top decade; the data put the true exponent near 0.19–0.22.

## §5. Theory for the class (task 5; shortened by the stop rule)

**5(i) E through g.** E = Tt + W − (1 − ρ) exactly (§2.4) [proved here: N(n) = Σ_{d≤n} g(d)⌊n/d⌋, split ⌊n/d⌋ = n/d − {n/d}].
On the data neither term dominates: both are of size M_g ≈ x^{0.5} and cancel to E ≈ x^{0.3}.

**5(ii) What Tao and Klurman force.** [quoted] Tao, Discrete Analysis 2016:1 (`sources/tao-1509.05363v6.txt` l. 57–63), Cor. 1.2:
every ±1 sequence has infinite discrepancy; for completely multiplicative ±1 functions Σ_{j≤n} f(jd) = f(d)Σ_{j≤n} f(j), so their
partial sums are unbounded; Example 1.4 (l. 85–123, Borwein–Choi–Coons χ̃₃): the partial sums can grow as slowly as log n.
Klurman, Compositio 153 (2017) 1622–1657 (`sources/klurman-1603.08453v1.txt` l. 337–361, arXiv p. 6–7), Thm 1.6: a multiplicative
f: ℕ → {−1, 1} has bounded partial sums iff f is periodic with Σ_{n=1}^{m} f(n) = 0 (and then f(2^k) = −1, f(p^k) = f((p^k, m))).
*Consequence for S7* [proved here, one line each]: S7's g takes values in {−1, 0, 1, 2, …} (g(p) = m_p − 1 reaches 78 at ρ = 0.6),
so neither theorem applies to S7 itself. They apply to the λ-rule variant (g completely multiplicative ±1): there M_g is unbounded
(Tao), but E = Σ_{m≤x}M_g(x/m) − ρx is not controlled by M_g in either direction (bounded M_g with unbounded E: g = χ₋₄, where E is
the circle-problem error; unbounded M_g with bounded E: none known to me), so Tao's theorem does not by itself make E unbounded.
The question "is E unbounded for every non-periodic member" is open here; it is listed in §8.

**5(iii) The hyperbola bound** [proved here]. For any y ∈ [1, x]: N(x) = Σ_{d≤y} g(d)⌊x/d⌋ + Σ_{m≤x/y} M_g(x/m) − ⌊x/y⌋M_g(y), so
E(x) + (1 − ρ) = −Σ_{d≤y} g(d){x/d} + Σ_{m≤x/y} M_g(x/m) − ⌊x/y⌋M_g(y) − xΣ_{d>y} g(d)/d (using ρ = Σ_d g(d)/d, which needs
M_g = o(x)). With Σ_{d≤y}|g(d)| ≪ y^{κ+ε} and M_g(u) ≪ u^{μ+ε} (μ ≤ κ ≤ 1; the tail is ≪ y^{μ−1} by partial summation):
E ≪ y^κ + x^μ(x/y)^{1−μ} + x y^{μ−1} ≪ y^κ + x y^{μ−1}, and y = x^{1/(1+κ−μ)} gives **β ≤ κ/(1 + κ − μ)**; for bounded g (κ = 1)
this is β ≤ 1/(2 − μ) ≤ ½ + μ/2 (the brief's form; (1 + μ)(2 − μ) ≥ 2). Nothing below ½ comes out unless κ < 1: the sawtooth
Σ_{d≤y} g(d){x/d} is bounded only by Σ|g|. On S7 the support of g has density close to 1 (≈ 98 % of primes are exceptional in
[10⁸, 10⁹)) and |g| is unbounded, so κ = 1, μ ≈ 0.5 and the bound reads β ≤ 2/3, against the observed 0.26–0.32: the true E lives on
the cancellation between Tt and W (§2.4), which no bound through |g| and M_g sees. For a feedback-chosen g I have no route below ½.

**5(iv) If M_g ≪ x^ε.** Then L_g(s) = Σ g(n)n^{−s} converges in σ > 0, ζ_P = ζL_g there, the hyperbola bound gives β ≤ ½ + ε (κ = 1),
and the zeros of ζ_P in σ > 0 are those of ζ and of L_g. Nothing confines the zeros of L_g: in that case U only asks α ≤ 2β, and
2β may be as large as 1 by this bound. Where M_g is bounded and g is ±1, Klurman makes g periodic, L_g a finite combination of
Dirichlet L-functions times finitely many Euler factors, and uo §3.3 applies (a U-crossing then needs an off-line Dirichlet zero).
S7 is far from that regime: μ ≈ 0.50 on [10³, 10⁹].

**5(v) Neamah–Hilberdink as a third route to α** [quoted] (IJNT 2019, `sources/neamah-hilberdink-1901.06866v2.txt` l. 104–105,
Thm 1): with ψ_P = x + O(x^{α+ε}), N_P = ρx + O(x^{β+ε}), M_P = O(x^{γ+ε}) (M_P = partial sums of the Beurling Möbius function
μ_P = a^{∗−1}), "the two largest of α, β, γ must be the same and at least ½". So if S7(0.6) has β ≈ 0.3 and α ≈ 0.82, then
γ = α: the exponent of M_P is an independent check of route 2 (computed in §3.4).

## §6. Prior art at the page, novelty, distance from upstream

- Révész–Pintz arXiv:2407.12746 (abstract only, `uo/sources/abstracts-related.txt` l. 9–10; arXiv metadata `sources/api_ids_1.xml`):
  Carlson-type zero-density estimates for Beurling ζ when the integers are natural numbers and the Ramanujan condition holds —
  S7's class when a_n ≪ n^ε. Density estimates allow sparse zeros in (½, 1); no conflict with §3. Full text not opened **[gap]**.
- Neamah–Hilberdink, IJNT 2019 (arXiv:1901.06866v2, `sources/neamah-hilberdink-1901.06866v2.txt` l. 104–105): Thm 1, the two
  largest of α, β, γ are equal and ≥ ½ — used in §5(v) as a third route to α. S7(0.6) obeys it on the data (§3.4).
- Hilberdink 2012 (`fr/sources/p3-22c2-…`, abstract l. 46–51): N(x) − cx periodic (finitely many jumps per bounded interval) ⇒ the
  usual primes minus finitely many. S7's E is not periodic (it grows, §2), so the theorem does not reach it; read backwards, it
  says the only periodic-error members of the prime-local class are finite deletions.
- Hilberdink 2005 (`fr/sources/w-18a-…`, via uo §5): max{α, β} ≥ ½ and, for β < ½, infinitely many zeros in every strip
  {η′ < σ < 1}, η′ ∈ (β, ½) — S7(0.6) has α ≈ 0.82 > ½ and the scan of §3 finds zeros at several heights (consistent).
- Tao 2016 and Klurman 2017 (§5(ii), opened at the lines given); Borwein–Choi–Coons only through Tao's Example 1.4 (l. 85–123):
  their paper itself not opened **[recalled, unverified]** beyond that example.
- BDR 2309.01567 and DMV 2006 (via uo §5, fr/sources z-02, p1-02): BDR's populating conjecture (l. 84–86) and DMV's p. 4 question
  (l. 203–207) — S7(0.6) is a second numerical non-surgery system in the corner β < α/2, now with multiplicative coefficients.
- arXiv API queries from this unit (`sources/api_ids_1.xml`, `sources/api_hilberdink.xml`), one at a time: no construction of a
  Beurling system by integer-level feedback, prime-local or otherwise, among the returned records (they were not a sweep — the
  on-disk sweeps of fr/ and uo/, 228 abstracts, are the gate, as in uo §5).
- **Novelty: single-check.** S7 and its cap as constructions (orchestrator's brief), the numerical crossings with multiplicative
  coefficients (tame ones for the cap), the zeros, Lemmas 1.2 and 4.1, the K₇ and K₇^{≤2} statements; §5(iii) is a routine hyperbola computation and may be classical.
- **Distance from upstream (10(n)).** Nearest published objects: Dedekind zeta functions (prime-local, a_p ∈ {0, …, d}, β > 0,
  zeros = GRH territory) and BDR's region-III systems (RH-conditional surgery). Exact difference: S7's local data (m_p) are chosen
  by feedback on the integer count, not by a field or a deletion; its a_p are unbounded (Lemma 1.2: ≤ ρ·gap + 1 + ρ). Every proved
  statement here uses no printed input except the quoted theorems named at their lines.

## §7. Instruments rows (shape of `directions/B2-refutation-program.md`; records, never ranks; not applied — for the digest)

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| (α, β) of the prime-local integer-greedy system S7(ρ) (g-primes are prime powers, a_n multiplicative; numerical, not proved) | ρ = 0.6, X = 4·10⁹: β ≈ 0.26–0.31 (running sup of \|E\|, windows 10³…10⁷ → 4·10⁹: .307 .295 .276 .272 .259, falling), α ≈ 0.80–0.81 (running sup of \|ψ_P − x\|), γ (Beurling Möbius sums) 0.80–0.82; α − 2β = +0.18…+0.29 on every window. X = 10⁹: ρ = 0.75 / 0.8 / 0.9 / 1.1 above the line from 10⁴ / 10⁴ / 10⁵ / 10⁵ (+0.05…+0.31); ρ = 1.25 below (−0.02…−0.10); ρ = 1.5 runs away. One producer; generator re-derived independently (additive DP, 0 mismatches to 10⁷) | `local-greedy-s40/NOTE.md` §2; `…/verify/logs/sweep/fits_v0_1e9.log`, `fits_v0_r06_4e9.log` | 2026-10-01 |
| Off-line zeros of S7(0.6)'s ζ_P (route 2; the zeros behind Theorem K₇) | ρ₁ = 0.8209965 + 11.0877411i, ρ₂ = 0.8052963 + 20.2490762i (Newton at X = 10⁷, 10⁸, 10⁹; stable to 2·10⁻⁵); winding number 1 on B₁ = [0.8010, 0.8410] × [11.0677, 11.1077] (min\|F_X\| = 0.0654 vs tail ≤ 0.0068 under H_0.40) and on B₂ (0.0838 vs 0.018); no other zero in σ ≥ 0.70, t ≤ 100 at X = 10⁷. Route 2 also at ρ = 0.75 / 0.8 / 1.1: top zeros 0.80563 + 92.34370i / 0.74647 + 30.69772i / 0.83989 + 20.33964i (X = 10⁸, not boxed). One producer. Scratch data: `/private/tmp/rh-s40-local-greedy/a_r06_1e9.u16` (a_n, n ≤ 10⁹), `x_r06_1e9.u32` (non-default decisions) | `local-greedy-s40/NOTE.md` §3; `…/verify/logs/zeros/cert_r06_z1_1e9.log`, `newton_r06_X1e9.log`, `zcount_r06_1e7.log` | 2026-10-01 |
| (α, β) of the capped prime-local system S7^{≤2}(ρ) (m_n ≤ 2, a_n ≪ n^ε proved; the K-candidate with tame multiplicities; numerical, not proved) | ρ = 0.6, X = 10⁹: β ≈ 0.19–0.22 (b_sup .215 .207 .204 .204 .192), α ≈ 0.79–0.83 (a_sup), zero z₁ = 0.8243658 + 11.0306646i (Newton 10⁷…10⁹, stable to 9·10⁻⁶; winding 1 on [0.8044, 0.8444] × [11.0107, 11.0507], min\|F_X\| = 0.0692 vs tail 0.0063 under H_0.40), γ = 0.78–0.82; α − 2β = +0.36…+0.44; max\|C(n)\|/n^{0.40} ≤ 0.93 on [10³, 10⁹], 0.10 in the top decade. One producer | `local-greedy-s40/NOTE.md` §4.2; `…/verify/logs/sweep/fits_v2_r06_1e9.log`, `…/logs/zeros/cert_v2r06_z1_1e9.log`, `hcheck_v2r06_1e9.log` | 2026-10-01 |
| Lemma H₇ on the computed range (the one hypothesis of Theorem K₇) | max\|N(u) − 0.6⌊u⌋\|/u^{0.40} per decade 10³…10⁹: 1.05, 0.86, 0.93, 0.60, 0.45, 0.35 (needed: ≤ 1 for all u > 10⁹) | `local-greedy-s40/verify/logs/zeros/hcheck_r06_1e9.log` | 2026-10-01 |

## §8. Untried (format of the directions' lists)

- **UT-L1 Prove Lemma H₇** for S7(3/5): |N(u) − 0.6⌊u⌋| ≤ u^{0.40} for u > 10⁹ (with Theorem K₇ it refutes U). Both halves open: the
  upward half bounds the clusters of §2.3; the downward half, by Lemma 1.2's route, would need prime-power gaps ≤ (x^{0.40} − 1.6)/0.6,
  beyond the known gap bound [recalled, unverified], so a proof has to use the composites that arrive inside gaps. Target: B2.
- **UT-L2 Interval certification of B₁** (python-flint arb) at X = 10⁹, the floating-point step of K₇. Target: B2.
- **UT-L0 Prove Lemma H₇^{≤2}** (|N(u) − 0.6⌊u⌋| ≤ u^{0.40}, u > 10⁹, for the capped system) — the cleanest route to refuting U on the
  record: bounded multiplicities, data exponent ≈ 0.2, constant ≤ 0.93 on the whole computed range. Certify B^{≤2} in arb. Target: B2.
- **UT-L3 Three variants unrun** (brief task 4): act only at primes; look-ahead at 2p, 3p; the λ-rule m_p ∈ {0, 2} with p² for
  refused p (completely multiplicative ±1 g: Tao's setting) — implemented in `s7gen` (variants 1, 3, 4), NOT run because of the stop
  rule; only the cap (variant 2) was run, to settle the K-close's "tame multiplicities" clause. Densities ≠ 0.6 for the cap: unrun. Target: B2.
- **UT-L4 Transient test for β.** The refused fraction rises (ρ = 0.6: .844 in [10⁸, 10⁹), .861 in [10⁹, 4·10⁹)); multiplicities grow
  (max m_p 79 → 106); b-fits still fall at 4·10⁹. Going to 10¹¹ needs the m-table compressed (now one byte per odd q ≤ X/2). Target: B2.
- **UT-L5 Theory left open:** is E unbounded for every non-periodic prime-local member; a quantitative lower bound; the λ-rule under
  Tao/Klurman; why the feedback produces a zero near 0.82 + 11.09i (a pseudo-character whose L-function has an off-line zero). Target: C2.
- **UT-L6 Zeros in σ ∈ [0.55, 0.70]** (27 counted at X = 10⁷ with phase steps up to 2.95 rad): refine at 10⁸–10⁹. Target: B2.
- **UT-L7 Prior art:** Révész–Pintz 2407.12746 full text; Borwein–Choi–Coons at the page. Target: standing order 1.

## §9. Waste line (10(o))

Spent for nothing: the first control-script run (uniform pair sampling almost never hit mn ≤ X; killed after six minutes, fixed by
log-uniform sampling) and one scan launch whose log directory did not exist (relaunched at once) — "spent on the wrong thing", small;
two shell loops lost to zsh's lack of word splitting (seconds, re-run under bash). Found: stop line (c), two certified boxes, a third
route agreeing, and the capped variant S7^{≤2} — tame and further across the line. Not done because of the stop rule: three of the
four variants of task 4, most of task 5, part of task 6.
