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

VERDICT LINE: AGREES-WITH-CORRECTIONS on the close "T: for almost every realization of DZ Thm 17.14, N_B(x) − k₂x =
Ω((x/log x)^{1/2}), so β₀ = ½ and P_B is a [1, ½]-system (BDR fn. 4); P_R is [½, ½]". Theorem 1 re-derived at the line
(Lemmas 2.1–2.3, Berry–Esseen, constants K and ε_x): valid. The passage from one-scale anti-concentration to "lim sup > 0
a.s." is the Fatou bound P(lim inf A_n) ≤ lim inf P(A_n) — it needs no independence across scales and no 0–1 law, as the
NOTE says. Prop. 2.4 valid: unboundedness of ζ_B on the real axis does exclude O(x^τ), τ < ½, by the elementary Mellin
bound (not Landau's theorem). Two FIX-FIRST items, both record-level: (F1) a quoted 10⁻⁶-size gap and a percentage range
in §3.1 do not reproduce (a quadrature artifact in the NOTE's continuum integral); (F2) the book's own normalization
(§17.10) may add an INFINITE sequence of primes, which Lemma 2.5 does not cover — the claim survives with one sentence.
Seven minor items. Re-run by independent routes: 54/54 grid variances to 10 digits; simulation at 10⁷ (5 seeds per template)
gives sup-slopes 0.496 ± 0.022 / 0.485 ± 0.026, within 1 se of the NOTE's 10⁸ values; one-scale identity 16/16; P_det
constant −0.5998 reproduced. Prior art: not settled in print (dual-checked); the question is older than BDR (DZ book p. 196,
"optimality is not known for θ ≤ 1/2"). Addition A1 (single-check): a.s. lim sup |N − ρx|/(x/log x)^{1/2} = +∞ (with
Landau, lim inf = −∞), which answers the NOTE's U-2; θ = ½ (is N − ρx = O(x^{1/2})?) stays open.

## §1. Re-derivations at the line

(a) §1.1–1.3, the construction at the page ✓ (with one record defect, F2). Lemma 17.2's proof (book l. 11627–11631)
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
    DEFECT (F2): Remark 17.12 (l. 12117–12120) says "a finite number of changes", but the book's own normalization in
    §17.10 (l. 13473–13505, book pp. 226–227) ends with "a finite or infinite sequence {w_n} … We enlarge P_X to contain
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
    bounds ✓. RECORD DEFECT (m1): §0 (l. 25) says Lemma 2.3 gives "E[R²|G]^{1/2} ≪ κ/log x"; the lemma proves only the
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
    the NOTE does not claim one (U-2 lists lim sup = ∞ as open; proved in §7 A1 by another route) ✓. Integers n suffice since lim sup_x ≥ lim sup_n ✓.
    Berry–Esseen is labeled [recalled, unverified]; it is classical and the proof needs only some absolute C₀ — see §3
    for the page check.

(f) Proposition 2.4 ✓ (second proof valid; two record items). (1) If E = O(x^τ), τ < ½, the Mellin form
    ζ_B = k₂s/(s − 1) + s∫₁^∞E x^{−s−1}dx continues ζ_B to σ > τ, s ≠ 1, and keeps it bounded on the real segment [½, ½ + δ];
    it agrees with DZ's continuation on the common connected domain ✓. So "unbounded on the real axis as σ → ½+" IS enough
    to exclude O(x^τ), τ < ½ — the step is the elementary Mellin bound (as in BDR Cor. 3.3, z-02 l. 672–676), not Landau's
    nonnegative-coefficient theorem; the name "Landau step" is loose but harmless (m4). (2) −F₁(σ) = Σ_p Σ_{j≥2}p^{−jσ}/j ≥ 0 ✓
    (book's F₁, l. 12915). (3) For real σ, 4^k(σ − ρ̄_k) is the conjugate of z = 4^k(σ − ρ_k) and G has real Taylor
    coefficients, so the k-th factor of (17.39) is |G(z)|² ✓; Re z = 1 − 4^k(1 − σ) ≥ 1 − 4^k/2, |z| ≥ 4^k e^{4^k} ✓;
    |G(z) − 1| = |e^{−z} − e^{−2z}|/|z| ≤ (e^{4^k/2−1} + e^{4^k−2})/(4^k e^{4^k}) = (e^{−4^k/2−1} + e^{−2})/4^k ≤ 0.19·4^{−k} ✓
    (k = 1: 0.0463); c₀ = Π(1 − 0.19·4^{−k})² ≈ 0.88 ✓; σ/(1 − σ) ≥ 1 on [½, 1) ✓. (4) F₂ = W + Δ cell by cell ✓ (the
    split is legitimate only cell-wise — Σ X_k v_k^{−σ} and ∫v^{−σ}f diverge separately for σ ≤ 1; the NOTE's Δ is a
    cell sum, so fine). W(σ) converges a.s. at each σ > ½ (Σ p_k v_k^{−2σ} < ∞) ✓; GAP (m3, wording): the lim sup over
    σ → ½+ needs W defined for all σ > ½ at once — true because a general Dirichlet series Σ a_k e^{−s log v_k} that
    converges at σ₀ converges for σ > σ₀, applied at σ = ½ + 1/n; add one clause. V(σ) ≥ (1/8)∫_{v_*}^∞ f v^{−2σ} ✓
    (p_k ≤ ½, v_k ≤ 2v) and → ∞ like log(1/(2σ − 1)) ✓; Lyapunov (summands ≤ 1, V → ∞) ✓; P(sup W > M) ≥ ½ for
    every M, δ, decreasing intersection ⟹ P(lim sup W = ∞) ≥ ½ ✓; invariance under finitely many coordinate changes puts
    the event in the tail σ-field (a measurable set invariant under changes of coordinates 1..n is a cylinder on the rest)
    ⟹ probability 1 ✓. (5) ✓. Remark: the prime squares alone give −F₁(σ) ≥ ½Σ_p p^{−2σ} ≍ ½log(1/(2σ − 1)) → +∞, which
    beats the typical size √log(1/(2σ − 1)) of W; turning that into a proof would need an upper LIL bound on −W — the NOTE
    rightly does not use it (but combined with the Mellin bound and lim sup W = ∞ it gives §7 A1).

(g) Lemma 2.5 ✓. N_P = Σ_j N_{P′}(·/q^j) ✓, ρ = ρ′/(1 − 1/q) ✓, E(x) = Σ_{j≥0}E′(x/q^j) with E′(y) = −ρ′y for y < 1 ✓,
    E′ = E − E(·/q) ✓; Σ_j (x/q^j)^τ ≪_τ x^τ ✓; Σ_{x/q^j ≥ 2} s_{x/q^j} ≪ s_x (split at x/q^j = √x) ✓; the o(s_x) version
    by the usual ε-split ✓. Adding a prime is the same map reversed ✓.

(h) Corollary 2.6 ✓. ψ_P = ψ^c + Σ_{k∈B}X_k log v_k exactly (q² > x) ✓; conditional variance ≥ ½log²(x/2)·Σ_{k∈B}p_k ≍
    x log x ✓; summands ≤ log x, so the Berry–Esseen error is O(log x/(x log x)^{1/2}) ✓; no density coupling (x is
    deterministic) ✓; 17.11(iv) ⟹ ψ_R = x + O(x^{1/2}log x) ✓ (BDR's α is defined through ψ, z-02 fn. 2 ✓). α(P_R) = ½ a.s. ✓.

(i) Corollary 2 and its proof ✓: (H0)–(H2) on Γ ✓ (m(x) ≤ 1.84·2^{1−⌊x/2⌋} ≤ 2^{2−⌊x/2⌋}; mesh ≤ ½ ✓), (H3) ✓ (a);
    BDR's [1, β] definition (z-02 l. 98–100: "(1.2) holds for every ε > 0 and no ε < 0, but the primes are not α-well-
    behaved for any α < 1") is met with β = ½ ✓. Scope paragraph (null set not covered) ✓. The normalized system: see F2.

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
      gap there is −1.53·10⁻⁶ (F1). Every other quoted gap reproduces: −1.755·10⁻¹ (x = 6), −6.79·10⁻² (8), −1.095·10⁻² (12),
      −1.944·10⁻³ (16), −1.639·10⁻⁴ (22, κ = 0.7, N₀ = 0) ✓. Decay per Δx = 2 is a factor 2.58 → 2.25, i.e. 2^{−x/2} times
      the 1/(x/log x) normalization, as §3.2's bound says ✓.
    - Theorem-B asymptotic at x = 22: (x/log x)·I/σ²_cont − 1 ranges over −26 % … +3.8 % across the six (κ, N₀) cases
      (κ = 1, N₀ = 0: −26.4 %; κ = 0.7, N₀ = 1: +3.8 %), not "10–20 %" (l. 224) (F1).

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
    zero envelope violations among ≈ 4.7·10⁸ f_C candidates; the residue identity log|G(1 − 4ie⁴)|² = −2∫a₁(t)cos(e⁴t)dt holds to
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

(d) §4.3, the deterministic grid control P_det — `verify-O/pdet_O.py`, `logs/pdet_O.log`, `data/pdet_O.json`. Own route: q*_j =
    F_R^{−1}(j) by Newton on the closed-form series, rounded up to Γ below 53 (first primes 2.25, 4, 5.875, 8.1328125, …);
    ρ_det and H(½) with midpoint-rule tails in the quantile variable (B(½) through ∫₁^Y v^{−1/2}f_R = 2 Shi(½log Y)).
    H(½) = −0.751728 (NOTE −0.7517 ✓); √(2/π)H(½) = −0.599792 (NOTE −0.5998 ✓); measured octave means of E/(x/log x)^{1/2}:
    −0.5905 (2¹⁶–2¹⁷), −0.5947 (2¹⁸–2¹⁹), −0.5985 (2²⁰–2²¹), −0.6026 (2²¹–2²²), −0.5997 (2²²–2²³) — the NOTE's −0.587 (10⁵),
    −0.595 (1.6·10⁶), −0.597 (6.3·10⁶) ✓ to the third digit. The [heuristic] constant is confirmed by an independent code.
    Verdict on §3–§4: every number the close leans on reproduces by an independent route; the one discrepancy (F1) is a
    quadrature artifact in a 10⁻⁶-size gap.

## §3. Prior art at the page

- BDR fn. 4 quoted exactly ✓ (z-02 l. 165: "Most likely the value of β0 equals 1/2, but in principle it is still possible
  that β0 could be smaller."); main text l. 133–136 ✓; Zhang sentence l. 118–124 ✓ ("Due to the probabilistic nature of
  the method, no precise value of α and β could be determined"); definitions l. 95–101 and fn. 2 (α through ψ_P − x, β
  through N_P − ax) ✓. Cor. 3.3 (l. 668–679: "N_P(x) − ax ≪ x^{1/2−ε} cannot hold … as that would make … ζ_P analytic
  around 1/2"), Cor. 3.4 (Hilberdink's max{α, β} ≥ 1/2), Rem. 3.5(1) (l. 688–711, P_β = P ∪ {p^{1/β}}) ✓ as the NOTE says.
  NOTE NOT SAID (m6): Cor. 3.3 with α = β = ½ already prints [½, ½]-systems, so Corollary 2.6 is new only as a statement
  about the book's P_R, not as an exponent pair.
- MISSED (m5): the question is posed in the Diamond–Zhang book itself, before BDR — book p. 196 (`sources/…book.txt`
  l. 11531–11532): "In each case, the Beurling g-number system that is constructed satisfies (17.3) with θ ∈ (1/2, 1)
  (optimality is not known for θ ≤ 1/2)", (17.3) being N(x) = kx + O(x^θ) (l. 11516). The NOTE answers θ < ½ (a.s.); the
  endpoint θ = ½ (is N_B − k₂x = O(x^{1/2})?) is NOT settled by Theorem 1 (Ω((x/log x)^{1/2}) is weaker than Ω(x^{1/2})),
  nor by my §7 addition. No novelty label changes (a question, not an answer), but §0 and §5 should cite it.
- Broucke 2507.13780 Thm 1.6 (l. 246–254: "(1) N_P(x) = Ax + O_ε(x^{1/2+ε}) for some A > 0 and every ε > 0") ✓ — upper
  bound only; Thm 5.1 = BV Thm 1.2 with "|π_P(x) − F(x)| ≤ 2" applied with F = Π_c (l. 1263–1275) ✓.
- Broucke–Hilberdink 2024 (t-19a, abstract): N(x) − ρx = Ω(x^{1/2}e^{−(log x)^β}) needs ψ(x) = x + O(x^α), α < ½ — does
  not apply to P_B (α = 1); Révész 2022/23, BDV 2020, BV 2021, DMV 2006 on disk: no Ω-statement for N of a random system
  (grep for Omega/almost surely/lower bound).
- My own searches (2026-10-01, `verify-O/sources/`): arXiv abs:Beurling AND abs:random (15 entries), abs:"well-behaved"
  AND abs:Beurling (4), abs:Beurling AND abs:integers (37, newest 2026-09-28), abs:"generalized primes" (65), abs:Diamond
  AND abs:Zhang AND abs:primes (2); Semantic Scholar citers of 2309.01567 (2507.13780, 2407.12746, 2307.00239, 2209.01689 —
  the NOTE's four); OpenAlex citers of the Trans. AMS version W4400813659 (one: the Carlson-type zero-density paper). None
  determines the integer exponent of the DZ/Zhang/DMV random systems. NOTE's "not settled in print" ✓ (dual-checked).
- Berry–Esseen, the NOTE's only [recalled, unverified] load-bearing citation, now checked at a page: Tyurin, arXiv
  0912.0726, p. 1, inequality (1): for independent non-identically distributed X_j with E|X_j|³ < ∞,
  sup_x |P(S_n ≤ x) − P(N ≤ x)| ≤ C·ε_n, ε_n = Σβ_j/σ³, "Esseen [6] showed that C ⩽ 7.5"; Theorem 7: C ≤ 0.5606
  (`verify-O/sources/tyurin-0912.0726v1.pdf`). The NOTE's use (finitely many bounded summands, Σβ_j ≤ Mσ²) fits exactly.

## §4. FIX-FIRST pairs (2)

F1 — a number that does not reproduce (record-level; no conclusion depends on it). The N₀ = 1 continuum values in
`verify/logs/onescale_A.log` carry a quadrature error of 10⁻⁶–10⁻⁵ (a fixed 200 001-point rule across the jump of n₀(x/v) at
v = 2x/3; §2(a)), so the smallest quoted gap has the wrong sign and size; and the Theorem-B offsets at x = 22 range wider.
OLD (l. 223): 1.5 ∉ P; 4 192 256 cells), down to 7.6·10⁻⁷ (κ = 1, 1.5 ∈ P): it shrinks like 2^{−x/2}, as the bound says. The
NEW (l. 223): 1.5 ∉ P; 4 192 256 cells), down to −1.5·10⁻⁶ (κ = 1, 1.5 ∈ P; continuum split at v = 2x/3 — the unsplit fixed-grid rule of `onescale.py` gave +7.6·10⁻⁷, an artifact): it shrinks like 2^{−x/2} up to the 1/(x/log x) normalization, as the bound says. The
OLD (l. 224): Theorem-B asymptotic (x/log x)I(κ; n₀) is 10–20 % off at x = 22 — the O(1/log x) — and 3–5 % off at x = 2²³ (3.3).
NEW (l. 224): Theorem-B asymptotic (x/log x)I(κ; n₀) is 4–26 % off at x = 22 (κ = 0.7, N₀ = 1: +3.8 %; κ = 1, N₀ = 0: −26 %) — the O(1/log x) — and 3–5 % off at x = 2²³ (3.3).

F2 — a gap in a stated coverage claim. Remark 17.12 says "a finite number of changes", but the book carries the
normalization out in §17.10 (book pp. 226–227, `sources/…book.txt` l. 13499–13505) with "a finite or infinite sequence {w_n}
… We enlarge P_X to contain the collection {w_n}", #{w_n ≤ x} = O(log x), Σ w_n^{−1/2} < ∞. Lemma 2.5 covers finite changes
only. The claim survives: deterministic added primes in (x/2, x] go into N^c and ρ^c, which stay G-measurable, and the
block's conditional variance is unchanged; (H3) for the normalized system is §17.10(ii).
OLD (l. 105–106): The same holds after any finite change of / the g-primes (Remark 17.12's normalization; Lemma 2.5).
NEW (l. 105–106): The same holds after any finite change of the g-primes (Lemma 2.5) and for the normalized system of Remark 17.12 as the book builds it in §17.10 — which may add an infinite, O(log x)-sparse deterministic sequence {w_n}: Theorem 1 applies verbatim with the w_n ∈ (x/2, x] counted in N^c and ρ^c.
OLD (l. 210–211): Lemma 2.5 carries / all of it through Remark 17.12's finite changes; Corollary 2.6 gives α(P_R) = ½. ∎
NEW (l. 210–211): Lemma 2.5 carries all of it through finite changes, and Theorem 1 (with the deterministic w_n inside G) through the §17.10 normalization of Remark 17.12, whose sequence {w_n} may be infinite; Corollary 2.6 gives α(P_R) = ½. ∎

## §5. Minor pairs (7)

m1 — §0 overstates what Lemma 2.3 proves (the L² bound is true but not proved there; the proof uses the tail bound).
OLD (l. 25): Linearizing e^{S} leaves a remainder R with E[R²|G]^{1/2} ≪ κ/log x (Lemma 2.3); the linear part has conditional variance
NEW (l. 25): Linearizing e^{S} leaves a remainder R with P(|R| > u | G) ≤ E[D²|G](1 + eκx/(2u)), E[D²|G] ≤ 5C_*/(x log x) (Lemma 2.3); the linear part has conditional variance

m2 — v_* unstated for f_C.
OLD (l. 66): (H) c_* /log v ≤ f(v) ≤ C_*/log v for v ≥ v_*, with (c_*, C_*) = (0.49, 1) for f_R (v_* = 100), (0.16, 1.84) for f_C.
NEW (l. 66): (H) c_* /log v ≤ f(v) ≤ C_*/log v for v ≥ v_*, with (c_*, C_*) = (0.49, 1) for f_R (v_* = 100), (0.16, 1.84) for f_C (v_* = e⁴; (1 − c)(1 − e⁻⁴) = 0.1604).

m3 — Prop. 2.4(4) takes lim sup over σ of a series shown to converge only at each fixed σ.
OLD (l. 186): (mesh ≤ 1) — bounded on [½, 1). W converges a.s. for σ > ½ (independent centered terms, Σ p_k v_k^{−2σ} < ∞). Its variance
NEW (l. 186): (mesh ≤ 1) — bounded on [½, 1). W converges a.s. at each σ > ½ (independent centered terms, Σ p_k v_k^{−2σ} < ∞), hence a.s. for all σ > ½ at once (take σ = ½ + 1/n; a Dirichlet series convergent at σ₀ converges for σ > σ₀) and is continuous there. Its variance

m4 — the step is the elementary Mellin bound, not Landau's theorem (a referee will ask).
OLD (l. 179): *Proof.* (1) Landau step: if E(x) = O(x^τ), τ < ½, then ζ_B(s) = s∫₁^∞ N_B(x)x^{−s−1}dx = k₂s/(s − 1) + s∫₁^∞ E(x)x^{−s−1}dx
NEW (l. 179): *Proof.* (1) Mellin step (absolute convergence only; Landau's nonnegativity theorem is not used): if E(x) = O(x^τ), τ < ½, then ζ_B(s) = s∫₁^∞ N_B(x)x^{−s−1}dx = k₂s/(s − 1) + s∫₁^∞ E(x)x^{−s−1}dx

m5 — the question is older than BDR and has an open endpoint (§3).
OLD (l. 82): no precise value of α and β could be determined." BDR's definition (l. 97–101): β = lim sup log|N(x) − ax|/log x.
NEW (l. 82): no precise value of α and β could be determined." BDR's definition (l. 97–101): β = lim sup log|N(x) − ax|/log x. The question is older: DZ book p. 196 (`sources/…book.txt` l. 11531–11532) — the constructed systems satisfy "(17.3) with θ ∈ (1/2, 1) (optimality is not known for θ ≤ 1/2)", (17.3) being N(x) = kx + O(x^θ). The THEOREM settles θ < ½ almost surely; θ = ½ stays open.

m6 — "Zhang's system" is the book's P_R (Zhang 2007 not read), and the pair [½, ½] is already in print.
OLD (l. 107): (Corollary 2.6), so Zhang's system is a [½, ½]-system — the value BDR l. 123–124 say "could not be determined".
NEW (l. 107): (Corollary 2.6), so the book's P_R — its version of Zhang's construction [Zh07], not read here — is a [½, ½]-system, the value BDR l. 123–124 say "could not be determined" for Zhang's system (the pair [½, ½] itself is in print: BDR Cor. 3.3 with α = β = ½, z-02 l. 668–679).

m7 — Untried U-2 is answered (read-O §7, A1, single-check).
OLD (l. 394): - **U-2 The sharp order.** Is lim sup |E|/(x/log x)^{1/2} = ∞ a.s.? Heuristically the dyadic blocks add Var E(x) ≍
NEW (l. 394): - **U-2 The sharp order.** lim sup |E|/(x/log x)^{1/2} = ∞ a.s. (read-O §7 A1, single-check: prime-square branch point × Prop. 2.4's lim sup W = ∞; with Landau's theorem lim inf E/(x/log x)^{1/2} = −∞); still open: is N − ρx = O(x^{1/2}) (DZ p. 196, θ = ½)? Heuristically the dyadic blocks add Var E(x) ≍

Total: 9 items (2 FIX-FIRST, 7 minor), 11 OLD/NEW pairs, all quoted at NOTE hash b5ff31f1….

## §6. Novelty per result

| NOTE result | verdict | page evidence |
|---|---|---|
| Theorem 1 (one-scale Ω for Bernoulli-selected primes) | new (not found in print); tools printed (Berry–Esseen, Tyurin 0912.0726 (1); DZ's selection, book l. 11627–11631) | §3 searches |
| Corollary 2 (β₀ = ½, P_B a [1, ½]-system, a.s.) | new — answers BDR fn. 4 and DZ p. 196 (θ < ½) for a.e. realization | z-02 l. 165; book l. 11531–11532 |
| Prop. 2.4 (ζ_B unbounded at ½ a.s.) | new as a statement on a printed core (DZ's ζ_B = ζ_C e^{−F₁+F₂}, book l. 12913–12925) | — |
| Lemma 2.5 (finite changes) | not new (inclusion–exclusion; DZ §17.10 invokes it for (ii), l. 13493–13495) | book l. 13493 |
| Corollary 2.6 (α(P_R) = ½, P_R a [½, ½]-system) | new for P_R only; the pair [½, ½] is in print (BDR Cor. 3.3 at α = β = ½) | z-02 l. 668–679 |
| §4.3 P_det (β ≥ ½ by the prime-square branch point; constant) | new as a statement; the mechanism (π priced instead of Π gives (2s − 1)^{−1/2}) is folklore [recalled, unverified] | — |
| Remark 5.1 (Broucke Thm 1.6 systems exact [1, ½], conditional) | new, conditional (hypothesis unchecked, U-3) | 2507.13780 l. 1263–1275 |
The NOTE's own labels (§6.1) agree with this table except m6 (Cor. 2.6) and m5 (DZ p. 196).

## §7. Additions (single-check)

A1 — THEOREM (stronger than Theorem 1; answers U-2). For almost every realization of P_B (and of P_R),
  lim sup_{x→∞} |N(x) − ρx| / (x/log x)^{1/2} = +∞.
Proof. Work on the a.s. event where (17.46)–(17.47) hold (so DZ's continuation and (H3) hold) and lim sup_{σ→½+} W(σ) = +∞
(Prop. 2.4(4), m3). For real σ ∈ (½, 1): ζ_B(σ) = ζ_C(σ)exp{−F₁(σ) + W(σ) + Δ(σ)} with every exponent real, |ζ_C(σ)| ≥ c₀
(Prop. 2.4(3)), |Δ| ≤ D₀. Since every term of −F₁ is ≥ 0, −F₁(σ) ≥ ½Σ_p p^{−2σ}, and Σ_p p^{−2σ} = log ζ_C(2σ) +
∫₁^∞ v^{−2σ} d(π_B − F_C)(v), where log ζ_C(2σ) ≥ log(1/(2σ − 1)) + log c₀ (Lemma 17.21 at w = 2σ > 1; the G-product is ≥ c₀
there by the same |G − 1| bound) and the second term is bounded on σ ≥ ½ by (17.47) after integrating by parts
(|π_B − F_C| ≪ v^{1/2}, ∫v^{1/2−2σ−1}dv ≤ 2). Hence |ζ_B(σ)| ≥ c₁(σ − ½)^{−1/2} e^{W(σ)}. If |E(x)| ≤ K(x/log x)^{1/2} for
x ≥ x₀, then ζ_B(σ) = k₂σ/(σ − 1) + σ∫₁^∞E x^{−σ−1}dx converges absolutely on σ > ½ and, with x = e^u,
σ∫_{x₀}^∞|E|x^{−σ−1}dx ≤ σK∫u^{−1/2}e^{−(σ−½)u}du = σKΓ(½)(σ − ½)^{−1/2}; so |ζ_B(σ)| ≤ C(σ − ½)^{−1/2} near ½. Then
e^{W(σ)} ≤ C/c₁ for σ ∈ (½, ½ + δ), contradicting lim sup W = +∞. For P_R replace ζ_C by s/(s − 1) (|·| ≥ 1 on [½, 1), and
(17.17) gives the bounded remainder). ∎ (Uses only DZ's printed facts and Prop. 2.4, which §1(f) re-derived.)
A1′ — one-sided form. ζ_C(σ) < 0 on (½, 1) (σ/(σ − 1) < 0, G-product > 0), so ζ_B(σ) ≤ −c₁(σ − ½)^{−1/2}e^{W(σ)}. If
E(x) ≥ −K(x/log x)^{1/2} for x ≥ x₀, Landau's theorem for Mellin transforms of eventually non-negative functions
[recalled, unverified: Widder, *The Laplace Transform* (1941), Ch. II §5] applied to E + K(x/log x)^{1/2} shows that
σ∫₁^∞E x^{−σ−1}dx converges on σ > ½ and is ≥ −C(σ − ½)^{−1/2}; contradiction as before. So a.s.
lim inf_{x→∞} (N(x) − ρx)/(x/log x)^{1/2} = −∞. This is what §2(b) sees: E < 0 on ≥ 89 % of the top two octaves in 9 of
10 runs, the largest |E|/s in the runs with large ρ.
A2 — what A1 does not reach: E = O(x^{1/2}) (θ = ½ in DZ p. 196). W(σ) ≈ √(log(1/(2σ − 1))) in size (LIL scale), far below
the ½log(1/(σ − ½)) needed to beat (σ − ½)^{−1} — the Mellin route cannot decide it; heuristically |E| ≈ s_x e^{W} with
e^{W} = (log x)^{o(1)}, so O(x^{1/2}) may well hold. Proposed as the new Untried item (replacing U-2).
A3 — the Fatou form of the end of Theorem 1's proof is one line: P(lim sup_n |E(n)|/s_n < λ) ≤ lim inf_n P(|E(n)| < λs_n) ≤ h(λ).
A4 — the residue identity of `verify/residue_check.py` holds to 16 digits with QAWO on the polynomial pieces of g (§2(b)),
replacing the NOTE's 3.8·10⁻⁶ step-limited agreement.

## §8. What I could not check, and why

- Zhang 2007 (Math. Ann. 337) is not on disk and was not fetched: whether the book's P_R is literally Zhang's original
  construction (grid, template) is unverified — hence m6's wording. DMV's dΠ_C against (H1) (NOTE §1.5, U-5): not checked.
- The book PDF page image for (17.13): the text extraction drops the ℓ glyph; I relied on the surviving "1 ≤" and on
  Remark 17.6's closure (Γ needs ℓ = 0). Nothing in Theorem 1 depends on the reading; §3's 1.5 and the simulation do.
- Scale: I re-ran the construction at X = 10⁷ (the brief's target), not the NOTE's 10⁸; the frontier controls T_0.90,
  T_0.95 and T₁ were not re-run (they calibrate the pipeline, not the close).
- Landau's theorem in A1′ is [recalled, unverified] (Widder Ch. II); A1 does not use it.
- Remark 5.1's hypothesis on Broucke's ζ_c (U-3) not checked at the page.
- Re-run reproducibility: `verify-O/` regenerates everything in ≈ 3 min (`python3 var_grid.py`; `python3 run_sim.py R1 R2 R3 R4
  R5 C1 C2 C3 C4 C5`; `python3 analyze_O.py`; `python3 onescale_O.py R2 C3 R4 C1`; `python3 pdet_O.py`); prime lists
  (≈ 5 MB each) live in /private/tmp/rh-s40-dz-half-s39/ and are rebuilt by the seeded generator.
