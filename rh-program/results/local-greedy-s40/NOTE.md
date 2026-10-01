# NOTE — unit `local-greedy-s40`: S7, integer-level feedback acting only at prime powers (the prime-local class on ℕ)

Session 40, 2026-10-01. Writer: Opus 5.5 (agent). Labels as in `u-offsurgery-s39/NOTE.md`: **[proved here]**, **[computed]** (script +
log under `verify/`), **[quoted]** (source on disk, page/line), **[recalled, unverified]** (never load-bearing), **[novelty: single-check]**.
Notation as there: [α, β]-system: ψ_P(x) = x + O(x^{α+ε}), N_P(x) = ρx + O(x^{β+ε}). **Conjecture U** (fr/NOTE §7.2): every discrete
[α, β]-system has α ≤ max{½, 2β}. Paths: `fr/` = `results/novel-wave-s37/beurling-frontier/`, `uo/` = `results/u-offsurgery-s39/`.

## §0. Close (filled last)

(pending)

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

RMS exponents b_rms (k = 3…7) at ρ = 0.6: .265 .243 .228 .217 .204; the M_g exponent μ ≈ 0.50–0.52 at every density ≤ 1.1.
Integer-error fits fall as the window starts later at every ρ ≤ 1.1 (no sign of a rising exponent on [10³, 10⁹]); α-fits are flat.

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
- **Novelty: single-check.** S7 as a construction (orchestrator's brief), the numerical crossing with multiplicative coefficients,
  the two zeros, Lemma 1.2, the K₇ statement; §5(iii) is a routine hyperbola computation and may be classical.
- **Distance from upstream (10(n)).** Nearest published objects: Dedekind zeta functions (prime-local, a_p ∈ {0, …, d}, β > 0,
  zeros = GRH territory) and BDR's region-III systems (RH-conditional surgery). Exact difference: S7's local data (m_p) are chosen
  by feedback on the integer count, not by a field or a deletion; its a_p are unbounded (Lemma 1.2: ≤ ρ·gap + 1 + ρ). Every proved
  statement here uses no printed input except the quoted theorems named at their lines.

**3.1 Strip counts at X = 10⁷** (`verify/logs/zeros/zcount_r06_1e7.log`; the a_n are the first 10⁷ of the 10⁹ dump). Winding numbers
of F_X on the strips × [0.1, 100]: σ ∈ [1.00, 1.10], [0.95, 1.00], [0.90, 0.95], [0.85, 0.90]: 0 (largest phase step on the box
contours 0.10, 0.15, 0.27, 0.76 rad); **[0.80, 0.85]: 2** (boxes × [10, 20] and × [20, 30]; step ≤ 1.59 rad, min|F| 0.024);
[0.75, 0.80], [0.70, 0.75]: 0 (≤ 1.59, 0.71 rad); [0.65, 0.70]: 4, [0.60, 0.65]: 13, [0.55, 0.60]: 10 — these last three with
phase steps up to 2.95 rad, so their counts are indicative only (aliasing possible; the zeros there are not refined here). So
below height 100 and right of σ = 0.70 F_X has exactly two zeros, and the largest real part is that of the zero near 11.09.
Hilberdink 2005 Cor. 2(b) (via uo §5) predicts infinitely many zeros in every strip η′ < σ < 1 with η′ ∈ (β, ½) when β < ½; the
27 zeros counted in [0.55, 0.70] are consistent with that.

**3.2 Newton and stability under X** (`logs/zeros/newton_r06_X1e7.log`, `…_X1e8.log`, `…_X1e9.log`): see the table in §3.3.
