# read-O.md — Opus reader, unit `conj-O-s38` (dual-model check, standing orders 5, 7, 11(c))

Reader: Opus 5.5 (independent of the orchestrator's read; not waited for). Started 2026-10-01.
Object: `NOTE.md` (41,290 bytes, 340 lines, read whole; SHA-256 c1050e62fd1892ff67c01354bd7abe2e0f3f03e517361caec3faeb02f32188e4),
`BRIEF.md`, `SHARED.md` (batches 0–5), `verify/` (thin2.c, thin_fr.c, rnums.c, dyadic_ms.py, t1/t3 scripts, logs), `sources/`,
and the frontier it builds on (`fr/NOTE.md`, `fr/read-O.md`, `fr/read-F.md`). Independent re-runs: `verify-O/` (shares no code with `verify/`).

**Verdict line (2026-10-01):** VERDICT-PLACEHOLDER

Status marks: ✓ = re-derived at the line and correct; GAP = a step that does not follow as written (FIX-FIRST pair, §5);
MINOR = prose/constant (pair, §6); UNVERIFIED = a tool or fact not readable at the page in any source on disk.

## §1. Re-derivations at the line

**1.1 Proposition 1.1, both forms, and the Parseval constant.**
- (a) additive. {y} = ½ − Σ_{h≠0}e(hy)/(2πih) ✓; for finite R, E = −Σ_{m|Q}μ(m){x/m} = Σ_{m|Q}μ(m)Σ_{h≠0}e(hx/m)/(2πih) (Σ_{m|Q}μ(m) = 0) ✓.
  h/m = a/b in lowest terms iff b | m and h = am/b ✓; coefficient Σ_{b|m|Q}μ(m)b/(2πiam) = (μ(b)/(2πia))Π_{p|Q,p∤b}(1 − 1/p) =
  ρμ(b)b/(2πiaφ(b)) ✓. **GAP (F1):** the same computation holds for **b = 1**: the integer frequencies carry c(a) = ρ/(2πia) ≠ 0
  (R = {2}: E = −{x} + {x/2}, c(1) = 1/(2πi) − 1/(4πi) = ρ/(2πi)). The statement's "b > 1" is wrong, and the Parseval product the
  NOTE writes, Π_{p∈R}(1 + (p+1)/(p−1)), already contains the b = 1 term (its "1"); summed over b > 1 only it is short by ρ²/12.
  "Σ_{m|Q}μ(m) = 0 kills the constant" removes a = 0, not b = 1. `verify-O/euler_O.py` (B): c(a/1) = ρ/(2πia) to 10⁻³⁰ on four
  sets; without b = 1 the Parseval sum is 0.0625 instead of 1/12 for R = {2}. (The writer's `t1_classsums.py` skips b = 1 in its
  coefficient loop — `if b == 1: continue` — so the slip was never tested.) Nothing downstream uses b > 1.
- Parseval: Σ_{a≠0,(a,b)=1}a^{−2} = (π²/3)Π_{p|b}(1 − p^{−2}) ✓, (1 − p^{−2})/(1 − 1/p)² = (p+1)/(p−1) ✓, Σ_{b|Q}Π_{p|b}(p+1)/(p−1)
  = Π_{p∈R}2p/(p−1) = 2^{|R|}/ρ ✓, so Σ|c|² = ρ2^{|R|}/12 = fr Prop. 5.1 ✓. Exact rationals, eight sets (euler_O (C)): (1/Q)∫₀^Q E² =
  ρ2^{|R|}/12 on every one (e.g. R = {5, 7, 11, 13}: 768/1001 both) ✓.
- (b) reflected. n = ka, m = kb, k = (n, m); m squarefree in ⟨R⟩ forces k, b ∈ ⟨R⟩, (k, b) = 1 ✓; (ka)^{s−1}(kb)^{−s} =
  k^{−1}a^{s−1}b^{−s} ✓; Σ_{k∈⟨R⟩,(k,b)=1}μ(k)/k = Π_{p∈R,p∤b}(1 − 1/p) = ρ/Π_{p|b}(1 − 1/p) (absolutely convergent) ✓. Diagonal:
  Σ_{a≥1,(a,b)=1}a^{2σ−2} = ζ(2 − 2σ)Π_{p|b}(1 − p^{2σ−2}) (σ < ½) ✓, multiplicative in b ✓ ⇒ the corrected product ✓. **The
  correction to the brief is right**: the sketch drops (1 − p^{2σ−2}). Divergence locus ✓: for 0 < σ < ½, 1 − p^{2σ−2} ∈ [½, 1),
  so the product diverges iff Σ_{p∈R}p^{−2σ} = ∞, i.e. for 2σ < α_R (and possibly 2σ = α_R).
- Independent check (euler_O (A), `verify-O/logs/euler_O.log`): the class sums are computed by RAW grouping of the pairs (n, m)
  by the reduced fraction n/m — not from the formula — on five sets, at real and complex s (0.3 + 7.5i, 0.1 − 3i): every complete
  class equals a^{s−1}b^{−s}μ(b)ρ/Π_{p|b}(1 − 1/p) to 10⁻³⁰; diagonal (brute a ≤ A, Hurwitz tail) = corrected product to ≤ 6·10⁻³⁰;
  the sketch is off by 12–55%. This also tests the class-sum formula itself, which the writer's check (b) takes as input.
- MINOR (m1): the NOTE's example "R = {2}, σ = 0.2: 6.92914577326 (sum) = … (corrected product)" is the diagonal WITHOUT the
  factor ρ² (= ¼) of the displayed formula; with it both sides are 1.73228644332.

**1.2 "In what sense a mean value".** No half-plane of convergence for F = ζ(1−s)D_R(s) ✓; Σ|c|² = (ρ²/12)Π2p/(p−1) = ∞ for
infinite R ✓; "E is not B²" ✓ by Bessel (a finite B² seminorm bounds Σ|Bohr coefficients|²; see §7 for a local, quantitative
version). Mellin: ∫₀^∞E x^{−s−1}dx = ρ/(s−1) + (ζ_P(s)/s − ρ/(s−1)) = ζ_P(s)/s on β₂ < σ < 1 ✓ (E = −ρx on (0, 1)). Plancherel under
x = e^u ✓. MINOR (m2): ∫₀^∞E²x^{−2σ−1}dx = ρ²/(2 − 2σ) + V(σ), so Prop. 1.3(i)'s bound should read 2π(2T+1)²(V(σ) + ρ²/(2 − 2σ));
harmless. "E = O(x^τ) permits ∫_T^{2T}|F|² ≍ T^{1+2σ}" ✓ (|χ|² ≍ t^{1−2σ}).

**1.3 Proposition 1.3 (RH, α_R < ½ ⇒ β₂ ≥ α_R/4) — AGREES.**
- (i) Cauchy–Schwarz: ∫₁^∞|E|x^{−σ″−1} ≤ V(σ′)^{½}(∫₁^∞x^{2σ′−2σ″−1})^{½} = V(σ′)^{½}(2(σ″ − σ′))^{−½} ✓; ζ_P = ρs/(s−1) + s∫₁^∞E x^{−s−1}
  (σ > 1) ✓ continues to σ > β₂ with |ζ_P| ≪ |t| ✓; Plancherel gives ∫_T^{2T}|ζ_P|² ≪ T² ✓ (constant per m2).
- (ii) {σ > β₂} = {β₂ < σ < ½} ∪ {σ > α_R} (α_R < ½): ζ_P/ζ on the first (ζ ≠ 0 there under RH), the product on the second, equal
  on the overlap ✓. 1/ζ(s) = 1/(χ(s)ζ(1−s)), |1/χ| ≍ |t|^{σ−½}, |1/ζ(1−s)| ≪ |t|^ε since Re(1−s) ≥ 1 − α_R − δ > ½ ✓. Pointwise
  |ζ_P| ≪ |t| would give T^{2+2σ}; the NOTE's T^{1+2σ+ε} correctly uses the mean-square bound on ζ_P times sup|1/ζ|² ✓.
- (iii) Mellin–Barnes: e^{−y} = (1/2πi)∫_{(2)}Γ(w)y^{−w}dw ✓; shift to Re w = −η crosses only w = 0 ✓ (η < 1); |Γ(u+iv)| ≤
  Γ(u+3)/|v|³ from Γ(w) = Γ(w+3)/(w(w+1)(w+2)) and |Γ(x+iy)| ≤ Γ(x) ✓ (near v = 0 use |Γ(−η+iv)| ≤ Γ(3−η)/(η(1−η)(2−η))). Weighted
  Cauchy–Schwarz in v and Fubini give ∫_T^{2T}|shifted|² ≪ N^{−2η}T^{1+2σ+ε} ✓ (the |v| > T/2 part is killed by |v|^{−3} against
  polynomial growth of D_R, which holds on σ ≥ β₂ + δ by (i)–(ii)).
- (iv) Expanding |Σa_n n^{−it}|² and integrating over [T, 2T]: the off-diagonal is two bilinear forms Σ_{m≠n}x_mȳ_n/(λ_m − λ_n) with
  λ_n = log n, |x_n| = |y_n| = |a_n|, δ_n ≥ log(1 + 1/n) ≥ 1/(n+1); (G.27) bounds each by (3π/2)Σ|a_n|²(n+1) ✓ ⇒ ≥ Σ|a_n|²(T − 3π(n+1))
  ✓. With N = T^{1−η}, n > T/(10π) terms total ≪ N²e^{−T^η/(5π)} ✓; e^{−2n/N} ≥ e^{−2} on n ≤ N ✓. Hence Σ_{m∈⟨R⟩,m≤N}m^{−2σ} ≪
  N^{(2σ+ε)/(1−η)}, and Q_R(N) ≥ π_R(N) ≥ N^{α_R−ε} i.o. ⇒ α_R ≤ 4σ + O(ε + η) ✓; σ ↓ β₂ ✓. (MV (G.27) read at the page, §3.)
- β ≥ β₂ ✓ (E = O(x^{β+ε}) ⇒ V(σ) < ∞ for σ > β); "(1/X)∫_X^{2X}E² ≫ X^{α_R−ε} i.o. ⇔ β₂ ≥ α_R/2" both directions ✓ (dyadic sums).

**1.3′ Remark 1.3′ (η(2s)) — AGREES-WITH-CORRECTIONS (MINOR m3).** η(2s) = Σ(−1)^{n−1}(n²)^{−s}: coefficients ±1 on the squares
(counting exponent ½) ✓; entire (1 − 2^{1−2s} kills the pole at ½) ✓; on 1/6 < σ < ¼, |χ(2s)| ≍ t^{½−2σ} and (RH) |ζ(1−2s)| ≪ t^ε
on Re(1−2s) ∈ (½, ⅔) ✓ ⇒ ∫_T^{2T}|f|² ≪ T^{2−4σ+ε} ≤ T^{1+2σ} iff σ ≥ 1/6 ✓; diagonal Σn^{−4σ} = ∞ iff σ ≤ ¼ ✓. So "finite order
+ Bohr mean square ≪ T^{2σ} ⇒ convergent diagonal" is false, and no growth-only lemma reaches α/2 ✓. Two precisions: (1) the
interval (α/3, α/2) is the α = ½ instance; the family η(ks) (α = 1/k) gives only (α/(2 + 2α), α/2) — k = 2 is the best case;
(2) the example shows growth information cannot pass α/3 (at α = ½); it does NOT show that α/4 (Prop. 1.3) is the limit, so the
§1.3 heading "and why growth information stops there" and §0's "pushed to its limit" overstate: the true limit of growth-only
input lies somewhere in [α/4, α/3] at α = ½ and is not determined.

**1.4 Theorem Z (RH; P_R continues with finite order past α_R/2 ⇒ β₂ ≥ α_R/2) — AGREES (two MINOR precisions).**
- Lemma Z.a (Borel–Carathéodory): h = g − g(z₀), Re h ≤ M′ = M + |g(z₀)| on the circle, hence inside (harmonic max principle —
  needed for 2M′ − h ≠ 0, not stated; MINOR m4); |φ| ≤ 1 ⟺ Re h ≤ M′ ✓; Schwarz |φ| ≤ r/ρ₁ ✓; h = 2M′φ/(1+φ) ⇒ |h| ≤ 2M′r/(ρ₁−r) ✓;
  adding |g(z₀)| gives exactly 2rM/(ρ₁−r) + ((ρ₁+r)/(ρ₁−r))|g(z₀)| ✓.
- Lemma Z.b (Phragmén–Lindelöf): Re cos(λ(s−m)) = cos(λ(σ−m))cosh(λt) ≥ cos(λ(b−a)/2)cosh(λt) > 0 for λ < π/(b−a) ✓; λ > c makes
  f_ε → 0 as t → ∞ ✓; max modulus on truncations, T′ → ∞, ε → 0 ✓.
- (Z1) as Prop. 1.3(i) ✓. (Z2) for s ∈ U₊: Re(ks) ≥ σ > τ₀ and |Im ks| ≥ |t| > T₀, so every P_R(ks) is defined ✓; the k-tail is
  uniformly O(2^{−kσ_min}) on compacta (needs σ > 0 — why U₊ has σ > max(τ₀, 0)) ✓; |L| ≪ |t|^A on σ ≥ τ + δ/2 (k₀ ≍ (α_R+2)/(τ+δ/2)
  terms) ✓; L = log Π(1 − p^{−s}) on σ > α_R ✓; e^L analytic and zero-free ✓; e^L = ζ_P/ζ on U₊ ∩ {σ > β₂} (identity theorem per
  component, each meets σ > 1) ✓ — the NOTE says "on U₊", but ζ_P/ζ is only defined on σ > β₂; all later uses are there (m5).
- (Z3) T₁ is never defined; it must exceed T₀ (so that U′ ⊂ U₊) (m5). Right of ½ + δ′: |ζ_P||1/ζ| ≪ |t|^{1+ε} (RH) ✓; left of
  ½ − δ′: |1/χ||1/ζ(1−s)| ≪ |t|^{σ−½+ε} ⇒ |D_R| ≪ |t|^{1+ε} ✓; band: f = D_R·(−i(s−½))^{−2} (an integer power — no branch needed)
  is ≤ C on both sides and the compact bottom edge, ≤ exp(Ct^A) ≤ exp(C′e^{ct}) inside ✓ ⇒ |D_R| ≪ t² ✓. So Re L ≤ 2log|t| + C ✓.
- (Z4) disc centre α_R + 2 + it₀, radius ρ₁ = α_R + 2 − τ − δ/2: leftmost point τ + δ/2 ✓; vertical extent ≤ ρ₁ < α_R + 2, so
  |t₀| ≥ T₂ = T₁ + α_R + 2 keeps the disc in U′ ✓; |L(z₀)| = O(1) ✓; r = ρ₁ − δ/2 reaches σ = τ + δ ✓ ⇒ |L| ≪_δ log|t| ✓.
- (Z5) the contour keeps Re w = 2 on |Im(s+w)| ≤ T₂ and joins at Im(s+w) = ±T₂ ✓ (there |Im w| ≍ T, |Γ| ≪ T^{−3}, |N^w| ≤ N², L
  bounded) ⇒ O(N²T^{−3}) = O(T^{−1−2η}) ✓; only the pole w = 0 is crossed (δ < 1) ✓; on Re w = −δ, Re(s+w) = τ + δ, inside (Z4) ✓
  ⇒ O(N^{−δ}log T) ✓. MV lower bound with a_n = b_n n^{−σ*}e^{−n/N}, |b_n| ≤ 1 ✓ ⇒ Σ_{p∈R,p≤N}p^{−2σ*} ≪ (log N)² for ALL large N,
  while π_R(N) ≥ N^{α_R−δ} i.o. gives ≥ N^{α_R−2τ−5δ} → ∞ (2τ + 6δ < α_R) ✓. ∎ ✓
- "What RH does": only (Z3) ✓. The logarithm converts polynomial growth into log growth — exactly Hilberdink's device (§3).

**1.5 Corollary Z.1 (RH: every regular deletion, every c) — AGREES.** Partial summation: ∫u^{−s}dF = cP(s+1−α) − Σ_{p≤p₀}(cp^{α−1}−1)p^{−s}
✓, boundary terms vanish for σ > θ ✓, |H| ≪ |s|/(σ−θ) ✓. P(w) = Σμ(m)m^{−1}log ζ(mw) ✓ (Möbius inversion of log ζ = ΣP(kw)/k).
Under RH each component {Re w > ½, ±Im w ≥ 1} is simply connected and ζ ≠ 0, ∞ there, so log ζ is single-valued analytic ✓; m ≥ 2
terms have Re(mw) > 1 ✓. Re log ζ ≤ C log|Im w| needs only a polynomial bound for ζ (convexity suffices; RH is used for the zero-
freeness of the discs) ✓; B–C ⇒ |log ζ| ≪ log|Im w| on Re w ≥ ½ + δ/2 ✓ ⇒ |P_R| ≪ |t| on U ✓ (A = 1). τ₀ = max(θ, α − ½, 0) < α/2
⟺ θ < α/2 and α < 1 ✓. Theorem-C class (θ < α/k_c ≤ α/2) ⊂ this class ✓, so A8 is covered: **the A8 corner is closed as a
refutation corner** — if RH fails, U fails at (ℙ, ℕ) (fr read-O A1); if RH holds, no regular deletion violates O ✓.
Locator slip (m6): "fr §6.3(iv)" is the paragraph (iv) at fr NOTE l. 373, which sits at the end of §6.2′ (fr §6.3 begins at l. 379);
its content (BDR's Broucke–Vindas selection has |π_S − F| ≤ 1, c = 1, θ = 0; z-02 ll. 1117–1118) is as the NOTE uses it ✓.

**1.6 Lemma G, (G′), Proposition 1.6 — AGREES-WITH-CORRECTIONS (F2).**
- "RH + Lemma G ⇒ O (mean square, pure deletions)" ✓ (Theorem Z). **F2 (what kind of G this is):** for each R, under RH, Lemma G
  is EQUIVALENT to O₂(R) := "β₂(R) ≥ α_R/2": Lemma G + Theorem Z ⇒ O₂(R); and O₂(R) makes Lemma G's hypothesis false, so Lemma G
  holds vacuously. So Lemma G is not a weaker missing input but a reformulation of the conjecture as an analytic-continuation
  statement ("a mean-square saving forces the continuation of P_R"). That is a legitimate G (the brief asks for "the named lemma"),
  but the NOTE should say so; otherwise "the exact missing lemma" reads as a reduction in strength. Its genuine content is the
  anatomy (Prop. 1.6) and the sufficient conditions (regular decomposition; natural boundary), which are one-directional.
- (G′) ⇔ Lemma G (given RH and β₂ < α_R/2): ⇒: e^L = ζ_P/ζ is zero- and pole-free, so ζ_P ≠ 0 off ζ's zeros and vanishes to ζ's
  order at them ✓. ⇐: a zero-free analytic D_R on a simply connected component has a logarithm L; P_R = −Σ_mμ(m)m^{−1}L(ms)
  converges (L(ms) = O(2^{−mσ})) ✓; growth: Re L = log|D_R| and B–C give |L| ≪ polynomial ✓. The critical-line clause is automatic
  for α_R < ½ (D_R is the convergent, non-vanishing product on σ > α_R ∋ ½) ✓. MINOR (m7): "fails exactly when … infinitely many
  branch points" drops the "or infinite order" alternative kept in Theorem Z's contrapositive; state both, or prove the alternative
  vacuous (ζ_P/ζ = ζ_P·(1/ζ) with ζ of order 1 has |1/ζ| ≤ exp(Ct log t) on suitable horizontals, so a finite-order bound is available).
- Prop. 1.6(i) (unconditional) ✓: β₂ < α_R/2 ⇒ ζ_P analytic on σ > β₂ (Z1), D_R = ζ_P/ζ meromorphic there (D_R(1) = ρ, no
  singularity at s = 1) ✓; P_R = −Σ_mμ(m)m^{−1}L(ms) ✓ (Möbius inversion checked: Σ_{m|n}μ(m) = [n = 1]); branch points at ρ′/m, only
  finitely many in a compact K since D_R has no zeros/poles on σ > α_R ✓. So P_R has no natural boundary in σ > β₂, and **a natural
  boundary of P_R on σ = σ_b ≥ α_R/2 implies β₂ ≥ α_R/2 unconditionally** ✓ — a clean, checkable sufficient condition.
  (ii) = Theorem Z's contrapositive ✓; the location "(τ₀, α_R]" for off-line zeros of ζ_P ✓ (ζ_P = ζ·D_R ≠ 0 on σ > α_R off σ = ½).
  (iii) ✓ as the contrapositive of 1.5. MINOR (m8): "as for random R, which Theorem B excludes almost surely" — Theorem B is a
  sup-norm statement (fr read-O §1.3: "not … a mean-square statement"). Its mean-square form does hold a.s. by a three-line addition:
  Theorem B(3) gives P(|E(x)| ≤ λ₀x^{α/2}(log x)^{−½}) ≤ ½ for x ≥ x₀; Fubini on [X, 2X] and P(f ≥ ¼) ≥ ⅓ for f ∈ [0, 1] with
  Ef ≥ ½ give P((1/X)∫_X^{2X}E² ≥ (λ₀²/4)X^α/log 2X) ≥ ⅓ for every X; reverse Fatou along X = 2^j gives probability ≥ ⅓ of "i.o.",
  and {β₂ ≥ α/2} is invariant under finite changes of R (E′(x) = E(x) − E(x/q), E(x) = Σ_jE′(x/q^j)), so Kolmogorov's 0–1 law gives 1.

**1.7 Additions — AGREES; the "any A" clause is probably false, reader's heuristic concurs.** With frequencies {k log p} ∪ {k log a}
distinct and δ-separated as stated, (G.27) holds for arbitrary distinct reals ✓; δ_n ≥ e^{−Kλ_n} bounds the error term by N^KΣ|a_n|²,
so N = T^{1/K−ε} already suffices (the NOTE's T^{1/(K+1)} is safe, not needed; m9); the rest of (Z1)–(Z5) is unchanged and the
diagonal only gains terms ✓ ⇒ β₂ ≥ max(α_R, α_A)/2 under the stated continuation hypothesis ✓ (distinctness excludes a ∈ R, and
a^k = p^j, which would merge coefficients — worth one clause, m9). Near-cancelling pairs a_p = p(1 + e^{−p}): the dipole
δ_{a_p} − δ_p has Mellin transform a_p^{−s} − p^{−s} = O(|s|e^{−p}p^{−σ}), and ∫{x/u}d(δ_{a_p} − δ_p) = {x/a_p} − {x/p} is ≈ −x e^{−p}/p
unless an integer lies in (x/a_p, x/p] (probability ≈ x e^{−p}/p): only p ≲ log x act, so E_sys(x) = (log x)^{O(1)} is the expected
size — the reader's heuristic agrees with the NOTE's "β ≈ 0", and α_sys = Θ (ψ changes by O(Σ_p log(1 + e^{−p}))) ✓, so it does not
bear on U ✓. The recommendation (a separation hypothesis in O's A-clause) is right.

**1.8 NOTE §2 (resonance) — AGREES as a named obstruction.** Kronecker: sup_t|Π_{p∈R,p≤Y}(1 − p^{−σ−it})| = Π(1 + p^{−σ}) ✓
(Q-independence of log p). Dirichlet's pigeonhole bound for simultaneous alignment ✓ (an upper bound on the height needed; the
converse "only π_R(p) ≲ log T/log q primes can be aligned" is heuristic, correctly labelled in the o(1)). Σ_{p∈R,π_R(p)≤K}p^{−σ} ≈
K^{1−σ/α_R} ⇒ exp((log T)^{1−σ/α_R+o(1)}) = T^{o(1)} ✓ (heuristic). (b) the converse needs |ζ_P| ≫ |t|^{1+δ} or Bohr mean square
≫ T^{2+δ} ✓ (from Z1/Plancherel); under RH that is |D_R| ≫ |t|^{½+σ+δ} on σ < ½ — far above T^{o(1)} ✓. (c)–(d) are interpretive;
the "L² form = Theorem Z" reading is accurate (Z5 is a Parseval/Carlson converse on log D_R). Nothing here is claimed as a theorem.

**1.9 NOTE §3 (computations) — claims checked against the data with the reader's own code (details §2).**
- 3.1 exactness ✓: on [n, n+1) E(n+u) = e_c − ρ(u − ½), ∫₀¹ = e_c² + ρ²/12 ✓; the writer's C code (thin_fr.c `emit_bins`) accumulates
  exactly Σ(N(n) − ρ(n + ½))² ✓. Window convention (six bins of 20/decade aligned at 10⁴) ✓.
- 3.2 rung 1 ✓ (reader: exact rationals, §2.2). 3.3: every number in the paragraph is reproduced by `verify-O/seeds_O.py` from the
  CSVs (0.723 ± 0.018, 0.787 ± 0.059, 0.392 ± 0.016, 0.450 ± 0.009, 0.363 ± 0.014, 0.674 ± 0.029, 0.783 ± 0.030) ✓; the writer's
  data are exact (reader's independent code with the writer's hash reproduces seed 5 at 10¹⁰ bin for bin, §2.3). The verdict
  sentence needs a correction (**F3**, §5): see §2.4.
- 3.4 ✓ (`verify-O/greedy_O.py`): ms-slopes 0.445/0.433, 0.577/0.594, 0.497/0.522, 0.676/0.467; sup 0.238, 0.308, 0.278, 0.354;
  κ vs M_diag 3.00 ± 0.15, 2.80 ± 0.15, 2.32 ± 0.24, 5.92 ± 0.31 — all as printed (top-three-decade slopes differ in the third decimal:
  0.439/0.599/0.538/0.440 vs 0.447/0.598/0.527/0.442, a window-edge convention). Relative to X^α (exponent fixed at α) the c = 2, α = 0.6
  deficit is κ₀ = 1.40 ± 0.24 (c = 1: 3.00, 2.80) — the "same form and size" holds only relative to M_diag. "Theorem C in mean-square
  form, one line" ✓ (the Mellin integral converges absolutely on σ > β₂, so ζ_P would be analytic across α/k_c on the real segment;
  coincidence points as in fr Theorem C). **F4** (§5): "provably log-powers" overstates — what is proved is β₂ ≥ α/2 (c = 1
  unconditionally, c = 2 under RH), i.e. the pure-power deficit cannot persist; the log-power form with κ ≈ 2.3–3 is a fit
  (the writer's own `t3_kappa.py` docstring: "over one data range both fit").
- 3.5 ✓ (`verify-O/feedback_O.py`): corr α = 0.75 K = 2: ms-slope [10⁴, 10⁹] 0.458, M/M_diag 0.737, 0.198, 0.076, 0.035 (1.6·10⁸),
  0.043 (last window); continued to 10¹⁰: 0.736, 0.194, 0.068, 0.024, 0.077, 0.441 and ms-slope [10⁷, 10¹⁰] 1.226 — as printed.
  Headers: ρ(10⁹ run) − ρ(10¹⁰ run) = 7.56·10⁻⁸ ✓ ("7.6·10⁻⁸"), D(10⁹) = −70.0, D(10¹⁰) = 3140.5 ✓ ("≈ 3·10³"). The identity
  E = e + ρx∫_x^∞(D(u) − D(x))u^{−2}du + O(1 + D²/x) re-derived: ρ/ρ̂ = exp(−∫_x^∞dD/u + O(1/x)), ∫_x^∞dD/u = ∫_x^∞(D(u) − D(x))u^{−2}du
  by parts ✓; D = Ku^{α/2} gives ρKx^{α/2}(α/2)/(1 − α/2) ✓; "deleting q changes E(y) by −E(y/q)" ✓ (fr Thm B step (2)).
