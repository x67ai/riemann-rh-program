# read-O — OPUS READER on unit `dz-half-s39` (NOTE.md: Diamond–Zhang's random Beurling systems have β = ½ almost surely)

Reader: Opus 5.5 (second model of the dual-model check; standing orders 5, 7, 11(c)). Date: 2026-10-01, started 10:59 IST.
NOTE read whole at SHA-256 b5ff31f10e4eb33e2412b7e352b795a29107c81b885acd6dfbd7e8dc23142953 (41 605 bytes, 407 lines).
Also read: BRIEF.md; SHARED.md (blocks 1–7); the Diamond–Zhang book text `sources/t-50-diamond-zhang-2016-book.txt` at
l. 11590–11740 (Lemma 17.2, Remark 17.4, the Borel–Cantelli step), 11835–11909 (Lemma 17.5, grid (17.13), Remark 17.6,
Lemma 17.7), 12100–12230 (Thm 17.11, Remark 17.12, proof of 17.11), 12283–12330 (Thm 17.14, (17.22)), 12436–12511
(Lemma 17.16, (17.29)–(17.31)), 12600–12680 (§17.7, (17.37)–(17.39)), 12824–12930 (Lemma 17.21, (17.44)–(17.47), the
representation ζ_B = ζ_C e^{−F₁+F₂}), 13165–13215 and 13470–13540 (§17.9 start, §17.10 normalization, §17.11 notes);
BDR (`novel-wave-s37/beurling-frontier/sources/z-02-…txt`) l. 95–168 and 664–715; Broucke 2507.13780 (`sources/`) l. 240–262,
1258–1290; Broucke–Hilberdink 2024 (t-19a, abstract and §1); BV 2024 (z-18), DMV 2006 (p1-02), BDV 2020 (z-01) by grep.
Independent re-run: `verify-O/` (own code written from the NOTE's definitions and the book's; nothing imported or copied
from `verify/`). Conventions: ✓ = re-derived at the line; GAP = what is missing, with the fix; FALSE = failing step.

VERDICT LINE: (written last; see the end of §4)

## §1. Re-derivations at the line

(a) §1.1–1.3, the construction at the page ✓ (with one record defect, m-level). Lemma 17.2's proof (book l. 11627–11631)
    uses independent Bernoulli X_k with P[X_k = 1] = p_k on ([0, 1], B, Lebesgue) ✓; Lemma 17.5 (l. 11846–11853) sets
    p_k = ∫_{v_{k−1}}^{v_k} f ✓; Remark 17.4 (l. 11624–11626) "for almost all subsequences (in the statistical sense) …
    by the easy part of the Borel–Cantelli lemma" ✓; the proof then fixes ω₀ off the null set (l. 11726) ✓. Grid (17.13)
    (l. 11885) reads "v0 = 1 and vk = n + [ℓ]/2n, for k = 2n + [ℓ], n = 0, 1, 2, …, 1 ≤ [ℓ] < 2n" (the ℓ glyph is lost
    in the extraction; the "1 ≤" survives) — the NOTE's reading Γ = {1} ∪ {n + ℓ/2ⁿ : n ≥ 1, 0 ≤ ℓ < 2ⁿ} is forced by
    Remark 17.6 (closure under addition: 1.5 + 1.5 = 3 needs ℓ = 0) ✓; I checked closure of Γ under + and × by hand
    (the denominator of n + ℓ/2ⁿ divides 2^{⌊·⌋}, and ⌊xy⌋ ≥ ⌊x⌋ + ⌊y⌋, ⌊x + y⌋ ≥ max) ✓. Thm 17.11 (l. 12108–12116)
    and Thm 17.14 (l. 12285–12297) quoted exactly ✓. P_R is selected by Lemma 17.7 → (17.16) (l. 12156–12162) and P_B
    by Lemma 17.7 → (17.46) (l. 12896–12906); both proofs are deterministic after that (the proof of 17.11 uses only
    (17.16)–(17.18), l. 12164–12228; 17.14 proceeds "as in the proof of Theorem 17.11", l. 12913) ✓, so (i)–(iv) of both
    hold off a null set and (H3) holds a.s. ✓. f_R (l. 12152–12155) ✓; (17.44), (17.45), "For v < e⁴ … f_C(v) =
    (1 − v⁻¹)/log v" (l. 12833–12892) ✓; ℓ_k = 4^k, γ_k = e^{4^k}, β_k = 1 − 4^{−k} (l. 12651–12660) ✓; (17.39) ✓;
    G(z) = 1 − (e^{−z} − e^{−2z})/z (17.22, l. 12307) ✓; g = Σχ^{*n}/n with multiplicative convolution, χ = 1_{[e,e²]}
    (17.30, l. 12445–12451) ✓. The representation ζ_B = ζ_C exp{−F₁ + F₂} with F₁, F₂ analytic on σ > ½ (l. 12913–12925) ✓.
    DEFECT (m1): Remark 17.12 (l. 12117–12120) says "a finite number of changes", but the book's own normalization in
    §17.10 (l. 13488–13513, book pp. 226–227) ends with "a finite or infinite sequence {w_n} … We enlarge P_X to contain
    the collection {w_n}", #{w_n ≤ x} = O(log x). Lemma 2.5 covers finite changes only. The claim survives (the w_n are
    deterministic; in Lemma 2.1 those in (x/2, x] go into N^c and ρ^c, which stay G-measurable, and the block's
    conditional variance is untouched), but the NOTE should say so instead of resting on "finite".

(b) Lemma 2.1 ✓ (re-derived; "exactly true" as the brief asks). Block primes q, q′ ∈ (x/2, x] have qq′ > x²/4 ≥ x and
    q² > x for x ≥ 4, so a g-integer ≤ x holds at most one block prime, to the first power ✓; its cofactor m′ ≤ x/q < 2 has
    only g-primes in (1, 2), none in the block (x/2 ≥ 2), and every g-integer < 2 is of that kind, so n₀(y) = N(y) for
    y < 2 ✓. The block B = {k : v_k ∈ (x/2, x]} is defined on the grid points themselves, and X_k attaches to v_k, so (a) is
    an identity with no boundary cells ✓. (b): every g-integer of Q is uniquely q^j·m (formal products), so
    N_Q(y) = Σ_j N_{Q∖q}(y/q^j) and N_{Q∖q}(y) = N_Q(y) − N_Q(y/q) ✓; ρ_{Q∖q} = ρ_Q(1 − 1/q) ✓; ρ^c = ρe^{−S} ✓, a
    function of (X_k)_{k∉B} ✓. (c): ρ^c x e^{S} = κx e^{D} = κx + κxD + κx(e^D − 1 − D) with κ = ρ^c e^{μ}; collecting gives
    Y + L + R with exactly the NOTE's Y, L, R ✓ (I redid the algebra term by term).

(c) Lemma 2.2 ✓. φ = n₀ − κy has N₀ + 1 linear pieces of slope −κ on [1, 2) ✓; {|φ| < θ} has measure ≤ 2θ(N₀ + 1)/κ = ½
    at θ = κ/(4(N₀ + 1)) ✓; J has ≤ 2(N₀ + 1) components ✓. 0 ≤ −log(1 − 1/v) − 1/v ≤ 1/v² for v ≥ 2 ✓, so
    |c_k − φ(x/v_k)| ≤ κx/v_k² ≤ 4κ/x ≤ θ/2 for x ≥ 32(N₀ + 1) ✓. p_k(1 − p_k) ≥ p_k/2 needs m(x) ≤ ½, which is in the
    definition of x₁ ✓. Miscounting: a cell meeting a component of J_x with v_k outside it must straddle the right end, so at
    most 2(N₀ + 1) cells, each ≤ m(x) — the NOTE's (4N₀ + 6)m(x) is generous ✓. |J_x| = x∫_J dy/y² ≥ x|J|/4 ≥ x/8 ✓,
    f ≥ c_*/log x on (x/2, x] once x/2 ≥ v_* ✓. (θ²/8)·c_*x/(16 log x) = c_*κ²x/(2^{11}(N₀ + 1)² log x) ✓. x₁ depends on
    N₀, v_*, c_*, m(·) only ✓; N₀ is G_x-measurable for every x ≥ 4 ✓ (the block lies in (2, x]).
    Constants of (H1) on DZ's templates ✓: c = 2·0.410616/(1 − e⁻⁴) = 0.83655 (c₁ at book l. 12814) ✓; (1 − c)(1 − e⁻⁴) =
    0.1604 ≥ 0.16 ✓ (so v_* = e⁴ for f_C — the NOTE names v_* only for f_R; m2); (1 + c) ≤ 1.84 ✓.

(d) Lemma 2.3 ✓ as stated (a tail bound). a_k ≤ (2/x)(1 + 2/x) on B ✓; Σ_{k∈B} p_k ≤ ∫_{x/2−1}^{x} f ≤ C_*x/log x for
    large x ✓; E[D²|G] ≤ 4C_*(1 + 2/x)²/(x log x) ≤ 5C_*/(x log x) ✓; on |D| ≤ 1, |e^D − 1 − D| ≤ (e/2)D² ✓; two Chebyshev
    bounds ✓. RECORD DEFECT (m3): §0 (l. 25) says Lemma 2.3 gives "E[R²|G]^{1/2} ≪ κ/log x"; the lemma proves only the
    Chebyshev tail bound (which is all the proof uses). The L² statement is true (E[e^{2D}|G] = 1 + O(1/(x log x)) since
    Σ p_k(e^{2a_k} − 1 − 2a_k) ≪ Σ p_k a_k²; then E[(e^D − 1 − D)²|G] ≪ E[D⁴|G] ≪ (x log x)^{−2}) but is not proved there.

(e) Proof of Theorem 1 ✓, including the passage the brief singles out. Given G, ξ_k = (X_k − p_k)c_k are independent and
    centered, |c_k| ≤ (N₀ + 1) + κx·a_k ≤ N₀ + 1 + 3κ ✓, Σ E|ξ_k|³ ≤ Mσ² ✓; Berry–Esseen (non-identical summands, any
    absolute C₀) gives the window bound 4λs_x/(σ√(2π)) + 2C₀M/σ for every G-measurable Y ✓; inserting Lemma 2.2 gives K =
    2^{7.5}/√(2πc_*) and ε_x exactly as printed ✓ (I recomputed both). κ_x = ρe^{−D_x} → ρ in L²-probability ✓, x₁(N₀) < ∞
    a.s. ✓, Φ_x → min{1, Kλ(N₀ + 1)/ρ} in probability and dominated convergence ✓. THE PASSAGE: A_{x₀} = {|E(n)| ≤ λs_n
    ∀ n ≥ x₀} lies inside every single-scale event {|E(n)| ≤ λs_n}, n ≥ x₀, so P(A_{x₀}) ≤ lim inf_n P(|E(n)| ≤ λs_n) ≤ h(λ);
    A_{x₀} ↑ and {lim sup_n |E(n)|/s_n < λ} ⊂ ∪A_{x₀}, so P(lim sup < λ) ≤ h(λ) → 0 (dominated convergence; ρ > 0, N₀ < ∞
    a.s.) ✓. This is the Fatou bound P(lim inf A_n) ≤ lim inf P(A_n); it needs NO independence across scales and no 0–1
    law — the NOTE's Remark (i) is correct. What it does not give: a deterministic lower constant (lim sup ≥ c a.s.) —
    the NOTE does not claim one (U-2 lists lim sup = ∞ as open) ✓. Integers n suffice since lim sup_x ≥ lim sup_n ✓.
    Berry–Esseen is labeled [recalled, unverified]; it is classical and the proof needs only some absolute C₀ — see §3
    for the page check.

(f) Proposition 2.4 ✓ (second proof valid; two record items). (1) If E = O(x^τ), τ < ½, the Mellin form
    ζ_B = k₂s/(s − 1) + s∫₁^∞E x^{−s−1}dx continues ζ_B to σ > τ, s ≠ 1, and keeps it bounded on the real segment [½, ½ + δ];
    it agrees with DZ's continuation on the common connected domain ✓. So "unbounded on the real axis as σ → ½+" IS enough
    to exclude O(x^τ), τ < ½ — the step is the elementary Mellin bound (as in BDR Cor. 3.3, z-02 l. 672–676), not Landau's
    nonnegative-coefficient theorem; the name "Landau step" is loose but harmless. (2) −F₁(σ) = Σ_p Σ_{j≥2}p^{−jσ}/j ≥ 0 ✓
    (book's F₁, l. 12915). (3) For real σ, 4^k(σ − ρ̄_k) is the conjugate of z = 4^k(σ − ρ_k) and G has real Taylor
    coefficients, so the k-th factor of (17.39) is |G(z)|² ✓; Re z = 1 − 4^k(1 − σ) ≥ 1 − 4^k/2, |z| ≥ 4^k e^{4^k} ✓;
    |G(z) − 1| = |e^{−z} − e^{−2z}|/|z| ≤ (e^{4^k/2−1} + e^{4^k−2})/(4^k e^{4^k}) = (e^{−4^k/2−1} + e^{−2})/4^k ≤ 0.19·4^{−k} ✓
    (k = 1: 0.0463); c₀ = Π(1 − 0.19·4^{−k})² ≈ 0.88 ✓; σ/(1 − σ) ≥ 1 on [½, 1) ✓. (4) F₂ = W + Δ cell by cell ✓ (the
    split is legitimate only cell-wise — Σ X_k v_k^{−σ} and ∫v^{−σ}f diverge separately for σ ≤ 1; the NOTE's Δ is a
    cell sum, so fine). W(σ) converges a.s. at each σ > ½ (Σ p_k v_k^{−2σ} < ∞) ✓; GAP (m4, wording): the lim sup over
    σ → ½+ needs W defined for all σ > ½ at once — true because a general Dirichlet series Σ a_k e^{−s log v_k} that
    converges at σ₀ converges for σ > σ₀, applied at σ = ½ + 1/n; add one clause. V(σ) ≥ (1/8)∫_{v_*}^∞ f v^{−2σ} ✓
    (p_k ≤ ½, v_k ≤ 2v) and → ∞ like ½c_* log(1/(2σ − 1)) ✓; Lyapunov (summands ≤ 1, V → ∞) ✓; P(sup W > M) ≥ ½ for
    every M, δ, decreasing intersection ⟹ P(lim sup W = ∞) ≥ ½ ✓; invariance under finitely many coordinate changes puts
    the event in the tail σ-field (a measurable set invariant under changes of coordinates 1..n is a cylinder on the rest)
    ⟹ probability 1 ✓. (5) ✓. Remark: the prime squares alone give −F₁(σ) ≥ ½Σ_p p^{−2σ} ≍ ½log(1/(2σ − 1)) → +∞, which
    beats the typical size √log(1/(2σ − 1)) of W; turning that into a proof would need an upper LIL bound on −W — the NOTE
    rightly does not use it.

(g) Lemma 2.5 ✓. N_P = Σ_j N_{P′}(·/q^j) ✓, ρ = ρ′/(1 − 1/q) ✓, E(x) = Σ_{j≥0}E′(x/q^j) with E′(y) = −ρ′y for y < 1 ✓,
    E′ = E − E(·/q) ✓; Σ_j (x/q^j)^τ ≪_τ x^τ ✓; Σ_{x/q^j ≥ 2} s_{x/q^j} ≪ s_x (split at x/q^j = √x) ✓; the o(s_x) version
    by the usual ε-split ✓. Adding a prime is the same map reversed ✓.

(h) Corollary 2.6 ✓. ψ_P = ψ^c + Σ_{k∈B}X_k log v_k exactly (q² > x) ✓; conditional variance ≥ ½log²(x/2)·Σ_{k∈B}p_k ≍
    x log x ✓; summands ≤ log x, so the Berry–Esseen error is O(log x/(x log x)^{1/2}) ✓; no density coupling (x is
    deterministic) ✓; 17.11(iv) ⟹ ψ_R = x + O(x^{1/2}log x) ✓ (BDR's α is defined through ψ, z-02 fn. 2 ✓). α(P_R) = ½ a.s. ✓.

(i) Corollary 2 and its proof ✓: (H0)–(H2) on Γ ✓ (m(x) ≤ 1.84·2^{1−⌊x/2⌋} ≤ 2^{2−⌊x/2⌋}; mesh ≤ ½ ✓), (H3) ✓ (a);
    BDR's [1, β] definition (z-02 l. 98–100: "(1.2) holds for every ε > 0 and no ε < 0, but the primes are not α-well-
    behaved for any α < 1") is met with β = ½ ✓. Scope paragraph (null set not covered) ✓. The normalized system: see m1.

(j) §3.2 ✓ (bound and closed forms). Three error sources (−p_k², first-order Riemann sum with |c′| ≤ κx/(v(v − 1)), straddling
    cells) ✓; σ²_cont = (x/log x)I(κ; n₀)(1 + O(1/log x)) for f_R ✓ (v = x/y, x·a(x/y) = y + O(1/x)). Closed forms re-derived:
    N₀ = 0: I = ½ − 2κ log 2 + κ² ✓; N₀ = 1: I = 1 − (2 log(3/2) + 4 log(4/3))κ + κ², coefficient 0.810930 + 1.150728 =
    1.961658 ✓; minima ½ − (log 2)² = 0.019547 and 1 − 1.961658²/4 = 0.037972 ✓; 1.5 is the only point of Γ in (1, 2) ✓.

(k) §4.3 ✓ for the proved part. log ζ_det = Σ_k k^{−1}[log(ks/(ks − 1)) + B(ks)] ✓; B(w) = O(1/w) for large real w (the
    smallest g-prime is 2.25 and ∫v^{−w}f_R = log(w/(w − 1))) so Π_{k≥3} converges ✓; (2s − 1)^{−1/2} is the only
    non-analytic factor and the others are non-zero at ½ ✓ ⟹ β(P_det) ≥ ½ ✓. H(½) formula ✓ (k = 1, 2 terms split off);
    √(2/π)·(−0.7517) = −0.59977 ✓ (Hankel contour: (1/2πi)∫(s − ½)^{−1/2}x^s ds/s ↦ 2x^{1/2}(log x)^{−1/2}/√π) — the
    transfer is correctly labeled [heuristic] (no continuation left of ½).

(l) Remark 5.1 ✓ under its stated hypothesis: ζ_P = Π_k[ζ_c(ks)e^{B(ks)}]^{1/k} from |π_P − Π_c| ≤ C ✓; ζ_c(2σ) ~ r/(2σ − 1) ✓;
    the k ≥ 3 product converges when Π_c has bounded density near 1 ✓. Broucke's construction does use |π_P − Π_c| ≤ 2
    with F = Π_c (2507.13780 l. 1263–1275, read) ✓. Conditional label correct.

## §2. Independent re-run (`verify-O/`)

(a) §3.1–3.2, the one-scale variance on DZ's grid — `verify-O/var_grid.py`, `logs/var_grid.log`, `logs/cont_check.log`.
    Different method: every cell integral from the closed-form antiderivative F_R(v) = Σ_{n≥1}(log v)ⁿ/(n·n!) taken as a
    cancellation-free difference (t_bⁿ − t_aⁿ = d·S_n, d = log1p(h/a)) — no quadrature; checked against mpmath quad on four
    cells to 16 digits (p(1, 1.5] = 0.45056978, the NOTE's "max p_k = 0.4506" ✓). Continuum σ²_cont by mpmath at 30 digits,
    split at the jump v = 2x/3 of n₀(x/v); re-checked by split scipy quad (agreement to 10 digits). For x ≤ 22 the block lies
    below e⁴, where f_C = f_R (book l. 12888), so one table serves both templates. 9 values of x × κ ∈ {0.7, 1, 2.4} × N₀ ∈ {0, 1}.
    - Grid sums: all 54 agree with the NOTE's `onescale_A.log` to the 10 printed digits (e.g. x = 22, κ = 0.7, N₀ = 0:
      0.16808469 both; x = 6: 0.1119487944 both). Cell counts 56 … 4 192 256 ✓.
    - Continuum, N₀ = 0: all 27 agree to 10 digits. N₀ = 1: the NOTE's values are off by 10⁻⁶–10⁻⁵ relative (x = 6, κ = 0.7:
      0.2136748484 vs 0.21367327; x = 22, κ = 0.7: 0.8011257798 vs 0.8011205320). Cause: the NOTE's fixed 200 001-point rule
      (`verify/onescale.py` l. 39) straddles the jump of n₀(x/v) at v = 2x/3; an unsplit rule reproduces errors of this size
      (`logs/cont_check.log`). Consequence: the NOTE's smallest gap "7.6·10⁻⁷ (κ = 1, 1.5 ∈ P)" (l. 223) is an artifact; the
      gap there is −1.53·10⁻⁶ (m5). Every other quoted gap reproduces: −1.755·10⁻¹ (x = 6), −6.79·10⁻² (8), −1.095·10⁻² (12),
      −1.944·10⁻³ (16), −1.639·10⁻⁴ (22, κ = 0.7, N₀ = 0) ✓. Decay per Δx = 2 is a factor 2.58 → 2.25, i.e. 2^{−x/2} times
      the 1/(x/log x) normalization, as §3.2's bound says ✓.
    - Theorem-B asymptotic at x = 22: (x/log x)·I/σ²_cont − 1 ranges over −26 % … +3.8 % across the six (κ, N₀) cases
      (κ = 1, N₀ = 0: −26.4 %; κ = 0.7, N₀ = 1: +3.8 %), not "10–20 %" (l. 224) — wording only (m5).

(b) §4, the finite rung, re-run at X = 10⁷ by my own simulation — `verify-O/dzsim.py`, `gcount.c`, `run_sim.py`,
    `analyze_O.py`; logs `logs/run_sim_*.log`, `logs/analyze_O.log`; per-run bin counts and metadata in `verify-O/data/`
    (prime lists in /private/tmp/rh-s40-dz-half-s39/, regenerated by `python3 run_sim.py R1 … C5` in ≈ 90 s; seeds 1001–1005,
    numpy Philox). Differences of method from the NOTE: exact per-cell Bernoulli for units ≤ 20 with closed-form p_k;
    EXACT independent Bernoulli on the true grid for units 21–52 by geometric skipping + acceptance p_k/p_max (the NOTE
    switches to Poisson-with-rounding above 22); Poisson with intensity f only above 53, where the grid is finer than a
    double; ρ from primes streamed explicitly to Y = 10⁹ (Gaussian law only beyond 10⁹; the NOTE beyond 10⁸), log r_T in
    closed form from (17.22), ∫(f_R − f_C)/v by QAWO on the polynomial pieces of g; log2-uniform edges (2048 per octave).
    Instrument checks: rational primes give N(e−) = ⌈e⌉ − 1 at all 47 600 non-integer edges ≤ 10⁷ and N(10⁷) = 10⁷
    (`logs/ctl_rational.log`); my g reproduces (17.31); f_C/f_R ∈ [0.239, 1.761] on [e⁴, e^{16.2}] ⊂ [1 − c, 1 + c] and
    zero envelope violations in 4.7·10⁸ candidates; the residue identity log|G(1 − 4ie⁴)|² = −2∫a₁(t)cos(e⁴t)dt holds to
    16 digits (−0.00324451406048419 vs −0.00324451406048421; `logs/residue_identity.log`; the NOTE: 3.8·10⁻⁶ gap).
    Results over full octaves (5 seeds per template; ± = seed standard error):
    | template | sup [10³, X] | sup [10⁴, X] | sup [10⁵, X] | supL [10³, X] | msL [10³, X] |
    |---|---|---|---|---|---|
    | P_R | 0.496 ± 0.022 | 0.519 ± 0.030 | 0.562 ± 0.046 | 0.540 ± 0.022 | 0.533 ± 0.033 |
    | P_B | 0.485 ± 0.026 | 0.515 ± 0.022 | 0.570 ± 0.051 | 0.529 ± 0.026 | 0.530 ± 0.045 |
    Agreement with the NOTE's 10⁸ table on the comparable window [10³, X]: sup 0.492 ± 0.012 / 0.479 ± 0.020, msL 0.519 /
    0.522 — within one standard error in every entry ✓. Per-seed sup over [10⁵, X] spreads 0.43–0.76 (sd ≈ 0.11), the
    NOTE's "±0.14 per-seed systematic" ✓. Nothing points below ½. One observation the NOTE states only in passing (§4.4(b)):
    E is NEGATIVE on ≥ 89 % of the edges of the top two octaves in 9 of 10 runs, with E(X)/s_X from +0.35 to −16.5 and
    the largest |E|/s in the high-ρ, 1.5 ∈ P runs — the sign of the prime-square branch point (H(½) < 0 because ζ_T(½) = −1),
    with a random amplitude. At reachable x the realized error is dominated by that term, not by the one-scale block
    fluctuation (σ_cont ≈ 1.4 s_x for κ ≈ 2.4); both give exponent ½, and Theorem 1 does not depend on which dominates.
    Caveat: the R and C runs with equal seed share their primes below 53 (identical f there), so the two rows are
    correlated through ρ.

(c) §3.3, one scale on realized systems — `verify-O/onescale_O.py`, `logs/onescale_O_v2.log` (a first pass, `onescale_O.log`,
    reused one resampling stream per x across runs, which correlated the variance ratios; v2 uses independent streams and
    is the one reported). Four of my runs (R2, R4 with 1.5 ∈ P; C1, C3 without), x = 2¹⁴, 2¹⁷, 2²⁰, 2²³:
    - Lemma 2.1(a) identity N(x) − N^c(x) = #B + [1.5 ∈ P]·#{q ∈ B : 1.5q ≤ x}, both sides by separate enumerations:
      residual 0 in 16/16 cases (798 … 268 807 block primes) ✓ (NOTE: 8/8).
    - Block resampled with the EXACT coupling E′ = N^c + Σn₀(x/q′) − ρ^c x e^{S′} (2000/2000/1000/300 replicates):
      Var(E′)/σ²_cont ∈ [0.915, 1.046], every one within 1.91 sampling sd of 1 ✓ (NOTE: 0.967–1.070); skew |·| ≤ 0.14,
      excess kurtosis |·| ≤ 0.32, KS p 0.34–0.99 ✓; σ²_cont/((x/log x)I(κ; n₀)) = 1.023–1.063, the O(1/log x) ✓ (NOTE: 1.03–1.05).
    - Realized E(x) against its conditional law: 15 of 16 have |z| ≤ 1.58; C1 at 2¹⁴ has z = +3.05 (p ≈ 0.04 for one such
      value among 16; C1 is ordinary at 2¹⁷–2²³). Recorded, not used.
    Verdict on §3–§4: every number the close leans on reproduces by an independent route; the one discrepancy (m5) is a
    quadrature artifact in a 10⁻⁶-size gap.
