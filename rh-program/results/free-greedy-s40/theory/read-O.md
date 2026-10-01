# read-O — `free-greedy-s40/theory` (S8: identities, Theorem 1.6, the reduction of U to Lemma B_ρ) — Opus read at the line

**Reader:** Opus 5.5 (subagent; second model of the dual check; `read-F.md` and `verify-F/` NOT opened). **Started 14:40 IST 2026-10-01.**
**NOTE read:** `theory/NOTE.md`, SHA-256 `caeb71db64b81ea38ef493de06b9d37d428af51f774c8e90f51e35e30c472e8b`, 440 lines (whole). Line numbers
below refer to that hash. **Also read:** `theory/BRIEF.md`, `../CHARTER.md`, `../SHARED.md` (all blocks to 14:02), `novel-wave-s37/beurling-frontier/NOTE.md`
§0 notation (l. 6–9), §1.7, §2.1 (l. 72–91), §7.2 (l. 448–466: the statement of Conjecture U), the unit's `sources/` transcriptions named in §3, and the unit's
`verify/` scripts only as far as needed to identify what they compute (no code copied or imported).
**Independent re-run:** `theory/verify-O/` (own C generator `s8dd.c`, block-wise exact-lattice sweep with double-double values and a
near-tie audit; own Python checks; logs `*.log`). Built from the charter's definition and the NOTE's Lemma 1.2 only.

## VERDICT LINE

(pending — written last)

## §1 Re-derivations at the line (✓ = re-derived step by step; GAP; FALSE)

**1.0 well-definedness (l. 49–59) — ✓, one slip (m1).** Re-derived: N_k is a finite step function polynomial in log x (p_i > 1), so
D_k → ∞; D_k is right-continuous with slope ρ and only downward jumps, so at x* = inf{x ≥ p_k : D_k ≥ ½} both D_k(x*) and D_k(x*−)
equal ½ and no element of G_k sits at x*. D_k(p_k) = −½ needs N_k(p_k) = N_{k−1}(p_k) + 1, true because every other element of
G_k \ G_{k−1} is p_k·m with m ≥ p₁ > 1. (ii) and (iii) follow for k ≥ 1. **For k = 0, (iii) is false:** p₁ = 1 + t/2 < p₀ + t = 1 + t
(D₀(1) = 0, not −½). Nothing downstream uses (iii) at k = 0 (Lemma 1.2 states gaps between g-primes only).
**1.1 E > −½ (l. 61–64) — ✓.** On [p_k, p_{k+1}) D = D_k < ½ by the infimum; D(p_{k+1}) = −½. A left limit D(x−) = ½ at x ≠ p_{k+1}
forces a downward jump at x, i.e. an element of G at x (a tie). My data: inf E(c−) over composites −0.4999931 (π/16, 10⁷).
**1.2 lattice (l. 66–68) — ✓.** ρ(p_{k+1} − 1) + 1 − N_k(p_{k+1}) = ½ and N_k(p_{k+1}) = N(p_{k+1}−) (no jump of N_k there, N = N_k
below p_{k+1}). n_{k+1} ≥ N(p_k) = n_k + 1 because N jumps by exactly 1 at p_k. p₁ = 1 + t/2 reproduced (all densities).
**1.3 free monoid (l. 70–77) — ✓.** f_k = 1 + (n_k − ½)X has constant term 1 and distinct linear terms, so the f_k are pairwise
non-associate primes of ℚ[X]; a product with constant term 1 determines its exponent vector; evaluation at a transcendental t is
injective; a composite has degree ≥ 2 and cannot equal 1 + (m − ½)X. The transcendence of 4/π, 16/π, 32/π (Lindemann) is labeled
[recalled]; I accept it as standard but note that it is the only external input of 1.3.
**1.4 reflection (l. 79–91) — ✓.** E = π − V is the identity N = 1 + π + C. For x ∈ [p_k, p_{k+1}): V(y) = π(y) − E(y) < k + ½
(E > −½); V(y−) ≤ k + ½ with equality only if E(y−) = −½ and π(y−) = k, i.e. a prime or tie in (p_k, x] — excluded; the sup over a
compact interval of a càdlàg function with finitely many jumps is a value or a left limit, so M(x) < k + ½; M(x) ≥ V(p_k) = k − ½.
Hence ⌊M + ½⌋ = k and r = k − M ∈ (−½, ½] — the stated range is right. With a tie in (p_k, x], V(y−) = k + ½ and M ≤ k + ½, so the
floor overcounts by exactly one, as stated; the hitting-time form p_{k+1} = inf{y > p_k : V(y) ≥ k + ½} is right (V(p_{k+1}) = k + ½).
Odd-p rule: lattice numerators 2q + (2m − 1)p are odd, a j-fold product has odd numerator over (2q)^j, a lattice point over (2q)^j
has numerator odd·(2q)^{j−1}: ✓ (and confirmed exactly: 0 ties to 10⁶ for t = 5/4). **The example "3·143 = 13·33" (l. 90) is not an
instance** (3/8 < 1; 143/8 is not a g-prime of S8(4/5)); a real one is (33/8)(1743/8) = (83/8)(693/8) — m3.
**Cor. 1.4′ (l. 92–94) — ✓** under 1.4's no-tie hypothesis (V(y−) − V(x) = C[y, x] − ρ(x − y)); the corollary does not restate the
hypothesis — harmless, since it is stated inside 1.4's scope.
**1.5 template and Mellin (l. 96–103) — ✓, both forms.** ζ_c = 1 + ρ/(s − 1); log ζ_c and ∫u^{−s}(1 − u^{−ρ})du/log u have equal
s-derivatives 1/(s − 1 + ρ) − 1/(s − 1) and both → 0 as s → +∞ (dominated convergence, (1 − u^{−ρ}) ≤ ρ log u). ψ_c as stated.
Second form of F_X: −X^{−s}N(X) + (1 − ρ)X^{−s} = −X^{−s}(E(X) + ρX), and ρsX^{1−s}/(s − 1) − ρX^{1−s} = ρX^{1−s}/(s − 1): ✓. My
two independent evaluations agree to ≤ 10⁻¹² at every σ tested.

## §2 Independent re-run (`verify-O/`; reproduce with `sh verify-O/run_all.sh`, about 15 s)

**Method (different from the unit's on three counts).** (1) *Algorithm:* block sweep, not a heap. Composites in (B, U] with U ≤ p₁B
involve only g-primes ≤ B, so once the sweep has passed B they are enumerated by a depth-first walk over multisets of known g-primes,
sorted, and merged with the thresholds x*(N) = 1 + (N − ½)t (`s8dd.c`, written from CHARTER §1 and Lemma 1.2 only). (2) *Arithmetic:*
double-double (~106 bits; t = 1/ρ from mpmath at 60 digits, error ≤ 3.4·10⁻³³ relative), not double. (3) *Audit of BOTH decision
classes:* a composite c may sit just BELOW the live threshold (c counted first) or just ABOVE a threshold at which a prime was placed
(prime first); both decide the system. Every decision with relative margin < 10⁻¹² was re-run with its factorization printed and
re-decided at 60 significant digits from the lattice indices alone (`close_paths.sh`, `mp_recheck.py`, `mp_recheck.log`): **23 of 23
confirmed** (1 for π/16 at 10⁷, 3 for π/4 at 10⁷, 19 for π/32 at 10⁸). Exact control: S8(4/5) in integer arithmetic (`r08_exact.py`).

**Reproduced digit for digit** (NOTE value → mine; logs `s8dd_<ρ>_<X>.log`):

| Quantity (NOTE line) | NOTE | read-O |
|---|---|---|
| π/16, X = 10⁷: F_X(0.79) (l. 16, 321) | +0.022231 | +0.022231318724 (two forms agree to 8·10⁻¹⁵) |
| π/16, X = 10⁷: F_X(0.80) (l. 322) | −0.025711 | −0.025711158284 |
| π/16: real zero of F_X at 10⁶ / 10⁷ / 5·10⁷ (l. 134) | 0.794752 / 0.794755 / 0.794755 | 0.7947523020 / 0.7947547814 / 0.7947551892 |
| π/16: N, π_P at 10⁷ (l. 234) | —, 633,514 | 1,963,496, 633,514 |
| π/16: sup E at 10³…10⁷, 10^7.5 (l. 410) | 3.04, 3.54, 6.88, 9.64, 12.84, 14.71 | 3.0381, 3.5351, 6.8801, 9.6362, 12.8385, 14.7145 |
| π/16: largest gap at 10⁷ / 10^7.5 (l. 151, 410) | 336.1 / 432.9 | 336.135 / 432.901 |
| π/4, X = 10⁷: F_X(½), F_X(0.55) (l. 324–325) | +0.067067, −0.173679 | +0.067066520612, −0.173679388824 |
| π/4: N(10⁶), π(10⁶); first g-primes (l. 127; charter) | 785,400, 78,134; 1.6366 … 16.9155 | identical |
| π/4: sup E 10³…10⁷ (charter table) | 8.22, 13.33, 26.63, 39.53, 47.86 | 8.2174, 13.3304, 26.6312, 39.5303, 47.8635 |
| π/32, X = 10⁶: F_X(0.89) (l. 213) | +0.0434 | +0.043424821306 |
| π/32 to 10⁸: sup E 10⁵…10⁸; gap; σ* (l. 215–216) | 4.83, 6.39, 8.93, 9.86; 397; 0.895077 | 4.8308, 6.3931, 8.9279, 9.8578; 397.251; 0.8950765135 |
| §1.8 table, X = 10⁶, σ* for π/64 … 0.95π/3 (l. 132–138) | 0.947634, 0.895076, 0.794752, 0.656529, 0.521753, 0.514036, 0.402156 | 0.9476341712, 0.8950763346, 0.7947523020, 0.6565294313, 0.5217527368, 0.5140359978, 0.4021560255 |
| same, sup E (l. 132–138) | 3.51, 6.39, 9.64, 15.35, 21.33, 39.53, 82.38 | 3.5062, 6.3931, 9.6362, 15.3493, 21.3263, 39.5303, 82.3797 |
| ρ = 4/5 to 10⁶: ties; sup E (l. 123; charter) | 0; 41.2 | 0 (exact integers); 41.1953 |
| Thm 4.1(ii)/4.2(ii) thresholds K = |F_X|/τ_X (l. 322–325) | 33.7; 121; 3.78; 0.344 | 33.7577; 121.393; 3.78306; **0.343888** (`tau_check.log`) |

Lemma 1.1 on data: inf E(c−) over all composites = −0.4999931 (π/16, 10⁷), −0.4999981 (π/4, 10⁷); E(p−) = −½ exactly at every prime.

**The ordering margins do NOT reproduce as stated** (they are one-sided). Minimum relative margin by decision class (my dd audit;
the 60-digit recheck agrees on every one):

| Run | composite just below its live threshold (the class the NOTE measured) | composite just above a threshold where a prime was placed (not measured) | NOTE says |
|---|---|---|---|
| π/16 to 10⁷ | 1.0550·10⁻¹¹ at 8.37·10⁶ | **5.0731·10⁻¹³** at 2,817,412.73 (= p·p′ with lattice indices 19, 5810) | "≥ 1.0·10⁻¹¹" (l. 17), "1.06·10⁻¹¹" (l. 329) |
| π/4 to 10⁷ | 5.5822·10⁻¹³ at 4.40·10⁶ | **6.4111·10⁻¹⁴** at 5,603,354.44 (4 factors) | "5.6·10⁻¹³" (l. 329), "≥ 5.6·10⁻¹³" (l. 409) |
| π/16 to 5·10⁷ | 1.1495·10⁻¹³ at 2.51·10⁷ | **6.1102·10⁻¹⁴** at 3.59·10⁷ | "1.1·10⁻¹³ to 5·10⁷" (l. 410) |
| π/32 to 10⁸ | 6.4327·10⁻¹⁵ at 7.11·10⁷ | 3.6957·10⁻¹⁴ at 9.08·10⁷ | "6.5·10⁻¹⁵ at 7.1·10⁷" (l. 217) — reproduces |
| π/32 to 10⁶ | 2.9983·10⁻⁹ | 7.6244·10⁻¹⁰ | "≥ 1.0·10⁻¹¹" (l. 17) — true |

The NOTE's own log `verify/bracket_pi4_1e7.log` prints "min rel. distance composite->live threshold = 5.580e-13 at x=4.39764e+06",
which is exactly my first column: its audit never measured the second class. Consequence: the stated margins overstate the safety
factor by 20× (π/16) and 9× (π/4); the CONCLUSION survives — the double-precision event order equals S8's to 10⁷ for both densities
(the smallest true margin, 6.4·10⁻¹⁴, is a 4-factor product whose double rounding is ≲ 10⁻¹⁵), and my double-double run, whose
decisions are re-checked at 60 digits, reproduces every certificate value to 12 digits. Also "a product of ≤ 25 doubles" (l. 330)
is false for π/4: products below 10⁷ have up to **32** g-prime factors (my walk's maximum; p₁^32 = 7.0·10⁶), 12 for π/16, 14 for π/16
to 5·10⁷, 10 for π/32 to 10⁸. See F2.

**Exact control (ρ = 4/5, `r08_exact.py`, integers):** to 10⁶, N = 800,000, π = 75,988, ties = 0 (as NOTE l. 87–89 proves for odd
numerator), and **25,180 equal-valued composite pairs** (1,686 below 10⁵): the first is (33/8)(1743/8) = (83/8)(693/8) = 898.734375.
The double-double generator returns the same N, π and sup E (values are dyadic, so exact). The NOTE's illustration "3·143 = 13·33
in numerators" (l. 90) is not an instance: 3/8 < 1 is not a g-prime, and 143/8 is not a g-prime of S8(4/5) either (the g-prime
numerators run 13, 33, 53, 83, 123, 133, 193, 213, …). See m3.
