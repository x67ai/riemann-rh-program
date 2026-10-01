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

**Theorem 1.6 (l. 105–115) — ✓, complete; two sharpenings (A1, A2 in §7).** Step by step: (1) ζ_P = ζ_c + sÊ on Re s > θ minus
{1} (1.5). (2) For real σ ∈ (θ, 1): σ∫₁^∞E u^{−σ−1}du ≥ −cσ∫₁^∞u^{−σ−1}du = −c. This uses σ > 0; the NOTE writes "θ < σ < 1"
without saying θ ≥ 0 — automatic for a discrete system (E jumps by ≥ 1 infinitely often, so E ≠ o(1) and no θ < 0 is possible).
(3) ζ_c(σ) = 1 − ρ/(1 − σ), so ζ_P(σ) ≥ 1 − c − ρ/(1 − σ), = 0 exactly at σ₀ = 1 − ρ/(1 − c). (4) σÊ(σ) is continuous at σ = 1
(absolute convergence on Re s > θ), so ζ_P(σ) → −∞ as σ → 1⁻ (residue ρ > 0). (5) IVT on [σ₀, 1). (6) Last step: for Re s > 1,
−ζ′_P/ζ_P = s∫ψ_P u^{−s−1}du (Euler product, convergent since π_P ≤ N); if ψ_P − u = O(u^a), a < σ*, then s/(s − 1) + H(s) is
analytic on Re s > a except at 1. **The connectedness sentence is complete:** ζ_P ≢ 0 (ζ_P(σ) → 1 as σ → ∞), so its zeros in
Re s > θ are isolated and form a closed discrete subset Z; an open half-plane minus the closed discrete set Z ∪ {1} is path-connected;
the identity theorem extends −ζ′_P/ζ_P = s/(s − 1) + H from Re s > 1 to that set; near σ* (> max(a, θ), since σ* ≥ σ₀ > θ) the left
side has a pole of residue −m, m ≥ 1, the right side is analytic: contradiction. So α ≥ σ*, β ≤ θ. **Endpoints.** σ₀ itself is a
possible zero only if ∫(E + c)u^{−σ₀−1}du = 0; for a DISCRETE system E is strictly decreasing between consecutive g-integers, so
{u : E(u) = −c} is countable and E > −c almost everywhere: the strict conclusion σ* ∈ (σ₀, 1) ALWAYS holds for discrete systems,
and the parenthetical hypothesis "E > −c on a set of positive measure" is automatic (A1). For continuous systems the closed endpoint
is attained: the template (E ≡ 0, c = 0) has its zero exactly at σ₀ = 1 − ρ. **Discreteness is used nowhere else**: the proof needs
only (A), (B), the Mellin identity and the Euler-product form of −ζ′/ζ, so it holds for every Beurling generalized system.
**Attempts to break it** (`verify-O/break_thm16.py`, `.log`; inf of E(u−) on [1, 2·10⁴]): odd integers (ρ = ½): inf E = −1 (at
every odd u ≥ 3; Thm 1.6 needs c < ½) — and indeed ζ(s)(1 − 2^{−s}) < 0 on (0, 1), no real zero; integers prime to 6 (ρ = ⅓):
E(5−) = −4/3 (needs c < ⅔); ideals of ℚ(√5) (ρ_K = 0.430409): inf E = −9.28; ℚ(√−3) (ρ_K = 0.604600): −13.63; ℚ(√−163)
(ρ_K = 0.246069): −25.80, and growing — lattice-point errors are unbounded below. In every case hypothesis (A) fails, consistent
with the absence of real zeros in (0, 1) [the absence for these three fields is recalled, unverified]. For number fields the theorem
reads as a Siegel-zero criterion: an ideal count with N_K(u) − ρ_K u ≥ r₀ > 0 and θ_K < r₀/(r₀ + ρ_K) would force a real zero of
ζ_K (hence of L(s, χ_d) for quadratic K) in [r₀/(r₀ + ρ_K), 1). No counterexample exists — the proof is complete — and the
template shows the bound σ₀ is sharp for continuous systems.
**Remark 1.6′ (l. 164–167) — ✓.** Same inequality with r₀ = 1 − ρ − c (ρσ/(σ − 1) + σ∫R u^{−σ−1} ≥ r₀ − ρσ/(1 − σ), > 0 iff
σ < r₀/(r₀ + ρ)); slightly more general (allows r₀ > 1 − ρ). "ℕ escapes because ⌊u⌋ − u ≤ 0" is right in this form (R ≤ 0).
**Cor. 1.7 (l. 116–119) — ✓.** (i) c = ½, σ₀ = 1 − 2ρ (implicitly ρ < ½). (ii) With U as printed (s37 NOTE l. 454–455: "Every
DISCRETE Beurling [α, β]-system satisfies α ≤ max{½, 2β}", [α, β] as in its l. 8): θ ≤ ½ − ρ < 1 − 2ρ, so α ≥ σ* > 1 − 2ρ ≥
max{½, 2θ} ≥ max{½, 2β} for ρ ≤ ¼ — U fails. S8(ρ) is a discrete Beurling system for every ρ (Lemmas 1.0–1.2; no transcendence
needed). (iii) ζ_P(σ₁) − F_X(σ₁) = σ₁∫_X^∞E u^{−σ₁−1}du > −½X^{−σ₁} (strict since E > −½): ✓.
**Prop. 2.1 (l. 146–151) — ✓ for k ≥ 1; for k = 0 (i)–(ii) fail** (E = −ρ(x − 1) on [1, p₁), ρg₀ = ½) — m2. (iii) ✓.

**§2.2–2.4 (l. 153–201).** Exact parts ✓: R = 1 − ρ + E; ζ_P = ρs/(s − 1) + s∫R u^{−s−1}du; ζ_c′(1 − ρ) = −ρ/ρ² = −1/ρ, so
σ* ≈ s₀ + ρζ_P(s₀) is Newton's first step. "Clipping is the only source of positive E" is Prop. 2.1(i) restated ✓. The queue law and
the complex-zero picture are labeled heuristic and used as such. Hilberdink Cor. 2(b) quoted correctly (§3).
**Dichotomy (l. 211–214) — ✓**, with one rounding error: ½ − π/32 = 0.40183, so "β(S8(π/32)) > 0.402 by Theorem 1.6 alone" overstates
(m4). The certified forms (> 0.395 from F_{10⁷}(0.79) > ½X^{−0.79}; > 0.445 from F_{10⁶}(0.89) = +0.043425 > 2.3·10⁻⁶) ✓.
**§3.1 S8^w, "E > −½ for every realization" (l. 222–227) — ✓, proof supplied.** Let x*_k = inf{x : D_{k−1}(x) ≥ ½}. Induction:
D_{k−1} < ½ on [1, x*_k), D_{k−1}(x*_k) = ½ (slope ρ, downward jumps only); p_k ≤ x*_k gives D_k ≤ D_{k−1} everywhere and
D_k(x*_k) ≤ −½, hence x*_{k+1} ≥ x*_k + t, the x*_k exhaust [1, ∞), and the final D < ½ everywhere, whatever the draws. GAP (minor,
m5): the window [x*_k − w, x*_k] must be cut to (1, ∞) — for w > t/2 a draw for p₁ can fall below 1, which is not a g-prime; the
NOTE's runs place p₁ at its deficit time (l. 232), a different rule for the first primes. Not load-bearing.
**"Lemma M is a short-interval PNT … i.e. Lemma G again" (l. 248–250) — only an implication.** By C(I) = ρ|I| − π(I) + ΔE(I),
Lemma M (A(I) ≤ ρ|I| − c|I|/log y for every I of length ≥ log³y) plus the fluctuation bound gives π(I) ≥ c|I|/log y − O(√(|I| log y))
on every such I, hence (taking |I| = K log³y, K large) prime gaps ≪ log³y — far stronger than Lemma G (gaps O(x^θ)); no converse is shown. Likewise "Lemma M,
equivalently (via the explicit formula) to Lemma Z" (l. 281–282) is "implied by". m6.
**§3.3 (l. 285–289).** "ζ_P is ζ_K times a factor positive on (0, 1), hence negative on (0, 1) when ζ_K is — so by Remark 1.6′ none of
them can satisfy R ≥ r₀ > ρ" drops the condition: for number fields with a real (Siegel) zero it is open; the correct conclusion is
"none whose ζ_K is negative on (0, 1)" (by Thm 1.6 these are exactly a Siegel-zero criterion, §1 above). m7.
**§3.4 (l. 291–313).** Legendre's identity ✓ (re-derived; needs freeness, so t transcendental, and the convention N = 0 below 1, i.e.
ΔE(J) = −ρ|J| for J ⊂ (0, 1), for the terms with d > b — unstated, m8); checked EXACTLY on six intervals of S8(π/16) up to
(10⁵, 2·10⁵] (`verify-O/legendre_check.log`: 19, 19, 20, 44, 777, 7668 = π(I) in every case). M ≥ M_lat ✓ (product over a subset of
factors in (0, 1)); M_lat(z)z^ρ = 1.0127 ✓ (mine 1.01268 at 10⁵); M(z) log z = 2.5438, 2.6990, 2.7751 at 10³, 10⁴, 10⁵ ✓. The
optimization ✓: max_h(−ρMh + √h·L) = L²/(4ρM) at h = L²/(4ρ²M²), so E ≪ u^{ρ/2}log²u under (i) and ≪ log³u under (ii).
**But the hypothesis of (i) and (ii) — two-sided square-root cancellation |S(I)| ≪ √|I|·log u + log²u — is FALSE for S8: see F1.**
"Lemma S … is equivalent to Lemma B" (l. 310): only S ⇒ B is shown; B ⇒ S would need π(I) ≥ ½ρ|I|M(√u) − O(u^θ) on every I,
a short-interval statement B does not give — m9. Lemma S as displayed (l. 301, one-sided, allowance ½ρ|I|M) is NOT refuted by F1.
**Theorems 4.1–4.2 (l. 317–327) — ✓** (values reproduced, §2; τ_X(σ) = σX^{−σ}(L²/σ + 2L/σ² + 2/σ³) re-derived and checked by
quadrature, `tau_check.log`), except the threshold "0.344" (needs K < 0.343888) — m10. The floating-point budget (l. 328–332) — F2.
**4.2 Rouché template (l. 334–339) — ✓** for boxes avoiding s = 1; F_X has the pole of ζ_c at 1, so for a box containing 1 the
winding number counts zeros minus one — relevant because §0 asks to "include t = 0 in every zero search" (l. 44). m11.

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

## §3 Prior art at the page

**Citations the NOTE relies on — each opened at the line it names:**
- Diamond, Illinois J. Math. 14 (1970) p. 24 — `sources/pa-diamond1970-p24-transcription.txt`, checked against the OCR
  `pa-diamond1970-ijm14-ocr.txt` l. 694–716 ("An exampl of … Malliavin [3] … even if N (x) x 0 (1) … For c (0, 1/2) … whose
  continuation has a zero at s 1 c > 1/2 … r, (x) is an increasing function"): ✓ the template (s − 1 + c)/(s − 1), continuous.
- Malliavin, Acta Math. 106 (1961) §6, pp. 295–297 — `pa-malliavin1961-sec6-transcription.txt`: estimate (13) is for the continuous
  n(x); the discrete variant (jumps of ⌊π⌋) carries no integer estimate: ✓ as the NOTE says.
- Lagarias 1999 — `pa-lagarias1999-delone.txt` l. 44–50 (g-integers counted with multiplicity), l. 176–186 (Thm 1.1:
  G = (P \ E) ∪ C), l. 194–213 (Thm 1.2), l. 127–136 (reads Malliavin as giving (1.10) n_N(x) = Ax + O(x^ε) with a real zero in
  (1 − ε, 1)): ✓. The NOTE's "not supported at Malliavin's page" is right and can be sharpened: for the DISCRETE example it is
  refuted — ζ₁ has a single zero in σ > 0, so by Hilberdink 2005 Cor. 2(b) its integer exponent is ≥ ½ (the NOTE says this at l. 373).
- BDR arXiv:2309.01567v2 — `beurling-frontier/sources/z-02…txt` l. 183–184 (Thm 1.3, RH-conditional [α, β] with
  2α/(α + 2) ≤ β < ½) ✓; l. 999–1003 ("As the integers have to display the best behavior, it seems natural to define a Beurling
  system through the sequence of the integers … extremely difficult to show which behavior the primes must admit") ✓ verbatim;
  l. 1186–1200 (log ζ_S(s) = log ζ(s + 1 − α) + O(√log|t|), so ζ_S has a pole at α and the system's zeta a real zero there) ✓.
- Hilberdink, JNT 112 (2005) — `w-18a…txt` l. 195 (Thm 1), l. 211–214 (Cor. 2(b), p. 336) and the page-image transcription: ✓
  exactly as used at NOTE l. 187–189.
- Hilberdink 2012 Thm 2.1 — `p3-22c2…txt` l. 404–410: N(x) = cx + 1 − c, N̂(s) = 1 + c/(s − 1), ψ′ = 1 − x^{−c} ≥ 0 ✓ ("implicit").
- Olofsson 2010 — `beurling-fe/sources/olofsson-2010-…txt` l. 101–105 (Conj. 1.2), l. 112–116 (Thm 1.3), l. 523–533 (the system:
  remove two rational primes, add q = p_ip_j/(p_i + p_j − 1)), l. 659–664 (equal values ⇒ logarithmic growth), l. 675 (ζ_Q = ψ(s)ζ(s)): ✓.
- Diamond–Zhang book (`dz-half-s39/sources/t-50…txt`) l. 2828–2835, **Theorem 5.10**: Π_{p_i≤x}(1 − 1/p_i)^{−1}/log x → Ae^γ iff N has
  logarithmic density A. Not cited by the NOTE; it is what F1 rests on, and it turns the NOTE's "Mertens law … (data above; not
  proved)" (l. 305–306) into a theorem as soon as N ~ ρx (limit e^{−γ}/ρ = 2.8595 for π/16; NOTE data 2.81 at 10⁶).

**Search for Theorem 1.6 itself** (one-sided integer bound ⇒ real zero). On disk: `grep -ril "siegel zero|exceptional zero|real zero"`
over `fetched*/`, `sources-extracted/`, `novel-wave-s37/*/sources/`, `qcond-s38/sources/`, `conj-O-s38/sources/`, the unit's
`sources/`: no statement of the lemma (hits are off-topic or the unit's own log). arXiv API (`verify-O/sources/q1…q6*.xml`, one query at
a time): Epstein zeta + real zeros (0 and 6 hits, none with a counting-function criterion), Beurling + Siegel/real axis/real zero (4
hits, off-topic), "counting function" + real zero + zeta (0), Dirichlet series + nonnegative coefficients + real zero (0), generalized
primes/integers + one-sided/bounded below (6, off-topic). Web search: nothing. **What IS in print:**
(a) **Bateman–Grosswald, Acta Arith. 9 (1964) p. 367** (PDF from matwbn.icm.edu.pl, OCR saved at
`verify-O/sources/bateman-grosswald-1964-aa9-ocr-pp364-367.txt`): "Z(½) > 0 if k > 7.0556 … Since Z(s) approaches −∞ when s
approaches 1 from below, it follows from Theorem 3 that Z(s) vanishes in (½, 1) if k > 7.0556" — the same positivity + pole +
intermediate-value mechanism for a lattice (Epstein) zeta, with the positivity obtained from the Chowla–Selberg formula, not from a
one-sided bound on the counting function. Same page: Rosser's theorem that ζ_K < 0 on (0, 1) for imaginary quadratic K with
3 ≤ |d| ≤ 199 (which covers my ℚ(√−3), ℚ(√−163) tests in §1).
(b) Révész, IMRN 2023 (`beurling-frontier/sources/t-14b…txt` l. 230–231): "once ζ(ρ₀) = 0, we must have |Δ(x)| ≥ x^{β₀−ε} for some x
values tending to ∞ … extends easily to the generality of the Beurling case" — the last step of Theorem 1.6 (zero ⇒ α ≥ Re ρ₀), in
print (Phragmén); and his §7 (l. 1040–1056) constructs Beurling systems with PRESCRIBED zeros, real ones included, but with
θ = r ≥ ½ — consistent with U.
(c) Diamond 1970 p. 24: the equality case (template, c = 0, zero exactly at σ₀).
**Verdict on 1.6:** the Beurling statement "N(u) − ρu ≥ r₀ > 0 and N − ρu = O(u^θ), θ < r₀/(r₀ + ρ) ⇒ real zero in
(r₀/(r₀ + ρ), 1) and α ≥ it" was not found; its mechanism (Bateman–Grosswald 1964) and its last step (Phragmén, as in Révész 2023)
are printed. Label: **new as a statement on a printed core** (single-check, Opus side).

## §4 FIX-FIRST pairs (line numbers at NOTE hash caeb71db…)

**F1 — the "square-root cancellation in S(I)" route is aimed at a FALSE statement.** *Claim [proved here, single-check].* For S8(ρ),
any ρ ∈ (0, 1) with t transcendental, the hypothesis (H) |S(I)| ≤ K(√|I|·log u + log²u) for all large u and all I ⊂ [u, 2u] (even
for the single intervals I = (u, 2u]) is false. *Proof.* Assume (H). (1) The NOTE's own derivation (§3.4(i); a gap longer than a
dyadic block is cut into dyadic pieces, each with π = 0) gives E(x) ≪ x^{ρ/2}log³x = o(x), so N(x) ~ ρx. (2) Hence N has logarithmic
density ρ and, by Diamond–Zhang Thm 5.10 (book l. 2828–2835), M(z)·log z → e^{−γ}/ρ. (3) The identity on I = (u, 2u] (u ≥ √(2u)):
π(I) = ρu·M(√(2u)) + ΔE(I) + S(I) = ρu·e^{−γ}(1 + o(1))/(ρ·½log 2u) + o(u/log u) = (2e^{−γ} + o(1))·u/log u. (4) Summing dyadic
blocks, π_P(x) ~ 2e^{−γ}x/log x; prime powers add O(N(√x)log²x) = o(x), so ψ_P(x) ~ 2e^{−γ}x. (5) Abelian step: ψ_P ~ cx gives
−ζ′_P/ζ_P(σ) ~ c/(σ − 1) as σ → 1⁺, while N ~ ρx gives ζ_P(σ) ~ ρ/(σ − 1) and −ζ′_P(σ) = ∫log u·u^{−σ}dN ~ ρ/(σ − 1)², so c = 1.
But 2e^{−γ} = 1.1229. ∎ (This is Mertens' 2e^{−γ} paradox of Legendre's sieve, transported to S8.) *Data* (`verify-O/s8dd_pi16_5e7.sieve.log`):
S(u, 2u]/(u/log u) = −0.0185, −0.0184, −0.0271, −0.0452, −0.0533, −0.0617 at u = 10³, 10⁴, 10⁵, 10⁶, 5·10⁶, 2.5·10⁷, moving toward
1 − 2e^{−γ} = −0.1229 (finite-z Mertens: ρM log z = 0.527 at z = 7071 vs 0.5615); |S|/(√u·log u) = 0.012, 0.022, 0.065, 0.237, 0.50, 1.06 —
growing like √u/log²u, so no fixed K serves. If Lemma B_ρ holds, Theorem 1.6 adds a second deterministic term: the real zero puts
≍ −u^{σ*}/log u into π(u, 2u], hence into S. Only ONE-SIDED forms can hold; Lemma S as displayed (l. 301, allowance ½ρ|I|M) is
consistent with both terms and is not refuted. A one-sided form that keeps the slack (S(I) ≥ (1 − 2e^{−γ} − δ)|I|/log u −
O(√|I|·log u)) is equivalent, through the identity, to a lower bound for primes in every interval of length ≫ log⁴u — a Cramér-strength
statement, not a "first rung". The pairs:

OLD (l. 27–28): Lemma S (cancellation in the Möbius sum S(I) of E-increments at smaller scales — square-root cancellation with polylog loss gives θ = ρ/2 + ε with NO prime number theorem for the system).
NEW: Lemma S (the one-sided bound S(I) ≥ −½ρ|I|M(√u) − O(u^θ) on the Möbius sum S(I) of E-increments at smaller scales; two-sided square-root cancellation in S(I) is FALSE for S8 — S(u, 2u] carries the Mertens bias (1 − 2e^{−γ} + o(1))u/log u, read-O F1 — so the sieve form is a short-interval prime statement, not a PNT-free shortcut).

OLD (l. 303): Two consequences of the floor M ≥ M_lat: (i) square-root cancellation with polylog loss, |S(I)| ≪ √|I|·log u + log²u, gives
NEW: Two conditional consequences of the floor M ≥ M_lat — both VACUOUS, because their hypothesis is false for S8 (read-O F1: it would force ψ_P(x) ~ 2e^{−γ}x via Diamond–Zhang Thm 5.10): (i) square-root cancellation with polylog loss, |S(I)| ≪ √|I|·log u + log²u, would give

OLD (l. 304): E ≤ max_h(−ρhM + √h·log u) + log²u ≍ log²u/(ρM(√u)) ≪ u^{ρ/2}·log²u, i.e. **θ = ρ/2 + ε with no prime number theorem for the system**;
NEW: E ≤ max_h(−ρhM + √h·log u) + log²u = log²u/(4ρM(√u)) + log²u ≪ u^{ρ/2}·log²u (the arithmetic is right; the hypothesis is not);

OLD (l. 305–306): (ii) with the system's Mertens law M(z) ≍ 1/log z (data above; not proved) the same cancellation gives E = O(log³u).
NEW: (ii) the Mertens law M(z)·log z → e^{−γ}/ρ is a theorem once N ~ ρx (Diamond–Zhang Thm 5.10; 2.8595 for π/16, data 2.78 at 10⁵); with it a one-sided bound S(I) ≥ (1 − 2e^{−γ} − δ)|I|/log u − O(√|I|·log u) would give E = O(log³u), but that bound is a lower bound for primes in all intervals of length ≫ log⁴u.

OLD (l. 312–313): d live at different scales, and a martingale ordered by scale u/d would give (i) once the predictable part (E's drift at scale u/d, which depends on the queue state there) is shown to be uncorrelated with μ(d) [the gap, stated precisely in §0].
NEW: d live at different scales; the predictable part (E's drift at scale u/d) CANNOT be uncorrelated with μ(d): the correlation is what produces the Mertens bias (1 − 2e^{−γ})|I|/log u of S(I) (read-O F1), so a martingale argument can at most control fluctuations around that bias, i.e. give a one-sided statement.

OLD (l. 416–417): it refutes U with no computation. First rung: the sieve form, Lemma S (§3.4) — square-root cancellation with polylog loss already suffices (θ = ρ/2 + ε, no PNT needed). Target: B2.
NEW: it refutes U with no computation. The sieve form (§3.4) is NOT a shortcut: two-sided square-root cancellation in S(I) is false for S8 (Mertens bias, Diamond–Zhang Thm 5.10; read-O F1); the usable form is the one-sided Lemma S, which amounts to a short-interval lower bound for the primes of S8. Target: B2.

OLD (l. 418–419): - **UT-F2 Lemma S for the randomized rule S8^w** (early placement keeps E > −½ for every realization, §3.1): a martingale ordered by the scale u/d of the increments ΔE(I/d); the gap is the decorrelation of μ(d) from the queue drift at scale u/d. Positive probability
NEW: - **UT-F2 the one-sided Lemma S for the randomized rule S8^w** (early placement keeps E > −½ for every realization, §3.1): a martingale ordered by the scale u/d of the increments ΔE(I/d), controlling fluctuations AROUND the Mertens bias (decorrelation of μ(d) from the drift is false, read-O F1). Positive probability

**F2 — the floating-point budget measures only one of the two decision classes; its numbers do not reproduce.** A composite c decides
the event order whether it sits just BELOW the live threshold (counted first) or just ABOVE a threshold at which a prime was placed
(prime first). The NOTE's audit (`verify/bracket_pi4_1e7.log`: "min rel. distance composite->live threshold = 5.580e-13") measures
the first class only. Both classes, re-decided at 60 digits (§2): π/16 to 10⁷: **5.07·10⁻¹³** (not 1.06·10⁻¹¹); π/4 to 10⁷:
**6.41·10⁻¹⁴** (not 5.6·10⁻¹³); π/16 to 5·10⁷: **6.11·10⁻¹⁴** (not 1.1·10⁻¹³); π/32 to 10⁶: 7.6·10⁻¹⁰ (the "≥ 1.0·10⁻¹¹" holds).
Products below 10⁷ have up to 32 factors for π/4 (not ≤ 25). The certificates SURVIVE: the double-double run reproduces F_X to 12
digits and every close decision is confirmed at 60 digits.

OLD (l. 16–17): F_{10⁶}(0.89) = +0.0434 for π/32, ordering margins ≥ 1.0·10⁻¹¹ relative there, against ≤ 3·10⁻¹⁵ rounding)
NEW: F_{10⁶}(0.89) = +0.0434 for π/32, ordering margins ≥ 5.1·10⁻¹³ (π/16, both decision classes) and ≥ 7.6·10⁻¹⁰ (π/32) relative there, against ≲ 10⁻¹⁵ rounding; reproduced by an independent double-double generator with every close decision re-checked at 60 digits, read-O §2)

OLD (l. 328–330): *Floating-point budget.* The deficit process sees only counts at the threshold times x* = 1 + (N − ½)/ρ; the closest any composite comes to its live threshold up to 10⁷ is 1.06·10⁻¹¹ (π/16) and 5.6·10⁻¹³ (π/4) in relative terms, against ≤ 3·10⁻¹⁵ accumulated rounding in a product of ≤ 25 doubles,
NEW: *Floating-point budget.* The deficit process sees only counts at the threshold times x* = 1 + (N − ½)/ρ; counting both decision classes (a composite just below its live threshold, or just above a threshold where a prime was placed), the closest call up to 10⁷ is 5.07·10⁻¹³ (π/16; 1.06·10⁻¹¹ for the first class alone) and 6.41·10⁻¹⁴ (π/4, a 4-factor product; 5.6·10⁻¹³ for the first class) in relative terms, against ≲ 10⁻¹⁵ rounding for that product and ≲ 10⁻¹⁴ for the longest products (up to 32 factors for π/4, 12 for π/16),

OLD (l. 409, last cell but one): One producer (theory; double precision, ordering margin ≥ 5.6·10⁻¹³ relative to 10⁷)
NEW: Two producers for the certificate values (theory, double precision; read-O, double-double with a 60-digit recheck); ordering margin ≥ 6.4·10⁻¹⁴ relative to 10⁷ (both decision classes)

OLD (l. 410, fragment): (1.3–1.5 log²x; ordering margin 1.1·10⁻¹³ to 5·10⁷)
NEW: (1.3–1.5 log²x; ordering margin 6.1·10⁻¹⁴ to 5·10⁷, both decision classes)

**F3 — "sup E ≈ (0.37–0.53)·ρ·log²x" does not reproduce.** From the NOTE's own §1.8 table (reproduced in §2), sup E/(ρ log²X) at
X = 10⁶ is 0.374, 0.341, 0.257, 0.205, 0.213, 0.264 for ρ = π/64, π/32, π/16, π/8, π/6, π/4 (0.434 at 0.95π/3): the range is
0.20–0.37, BELOW the pure-Poisson (ρ/2)·log²x and scattered around the NOTE's sub-Poisson value 0.3ρ — the opposite of "above".

OLD (l. 35): sup E ≈ (0.37–0.53)·ρ·log²x across ρ.
NEW: sup E ≈ (0.20–0.37)·ρ·log²x for ρ ∈ [π/64, π/4] at X = 10⁶ (0.43 at 0.95π/3), around the sub-Poisson prediction 0.3ρ.

OLD (l. 181): sup E/log²x = 0.018, 0.034, 0.049, 0.080, 0.112, 0.207 at ρ = π/64 … π/4 (§1.8), i.e. (0.37–0.53)·ρ, against 0.3ρ predicted.
NEW: sup E/log²x = 0.018, 0.034, 0.050, 0.080, 0.112, 0.207 at ρ = π/64 … π/4 (§1.8), i.e. (0.37, 0.34, 0.26, 0.20, 0.21, 0.26)·ρ, scattered around the 0.3ρ predicted.

## §5 Minor pairs

m1 — Lemma 1.0(iii) at k = 0.
OLD (l. 52): so D(p_{k+1}) = −½; (iii) p_{k+1} ≥ p_k + t.
NEW: so D(p_{k+1}) = −½; (iii) p_{k+1} ≥ p_k + t for k ≥ 1 (p₁ = 1 + t/2).

m2 — Prop. 2.1 at k = 0 (E = −ρ(x − 1) on [1, p₁)).
OLD (l. 147): (i) E(x) = ½ + C(p_k, x] − ρ(x − p_k) for x ∈ [p_k, p_{k+1}); (ii) ρg_k = 1 + C(p_k, p_{k+1}); (iii) sup_{u≤x}E(u) ≤ ρG(x) − ½, G(x) :=
NEW: for k ≥ 1: (i) E(x) = ½ + C(p_k, x] − ρ(x − p_k) for x ∈ [p_k, p_{k+1}); (ii) ρg_k = 1 + C(p_k, p_{k+1}); (iii) sup_{u≤x}E(u) ≤ ρG(x) − ½, G(x) :=

m3 — the multiplicity example is not an instance.
OLD (l. 90): (t = 5/4, primes (10k + 3)/8) — although there EQUAL composites (multiplicities) can occur, e.g. 3·143 = 13·33 in numerators. With p even
NEW: (t = 5/4, primes (10k + 3)/8) — although there EQUAL composites (multiplicities) do occur: (33/8)(1743/8) = (83/8)(693/8), and 25,180 equal-valued pairs below 10⁶ (read-O, exact integers). With p even

m4 — rounding in the Dichotomy.
OLD (l. 213): β(S8(π/32)) > 0.402 by Theorem 1.6 alone
NEW: β(S8(π/32)) > 0.4018 by Theorem 1.6 alone

m5 — the early-placement window must stay above 1.
OLD (l. 223): Place p_k uniformly in [x*_k − w, x*_k], independently
NEW: Place p_k uniformly in [max(x*_k − w, 1 + t/2), x*_k], independently (a draw ≤ 1 is not a g-prime; the runs place p₁ at its deficit time)

m6 — Lemma M, G, Z are linked by implications, not equivalences.
OLD (l. 249–250): a short-interval PNT for the system at scale y, i.e. Lemma G again.
NEW: a short-interval lower bound for the primes of the system at scale log³y — it implies Lemma G (gaps ≪ log³y), not conversely.
OLD (l. 281–282): to **Lemma M**, equivalently (via the explicit formula) to **Lemma Z**
NEW: to **Lemma M**, which is implied (via the explicit formula) by **Lemma Z**
