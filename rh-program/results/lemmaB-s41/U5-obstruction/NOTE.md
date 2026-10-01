# NOTE — unit `lemmaB-s41/U5-obstruction`: can (A) and (B) hold together for a DISCRETE Beurling system?

Session 41, started 17:06 IST 2026-10-01. Writer: Opus 5.5 (agent), the adversary of the stream. Labels as in the charter §4:
**[proved here]**, **[computed]** (script + log in `verify/`), **[quoted]** (source at page/line on disk), **[recalled, unverified]**
(never load-bearing). Notation as in `../CHARTER.md` §1 and `free-greedy-s40/theory/NOTE.md`: t = 1/ρ, T(x) = ρ(x − 1) + 1, E = N − T,
R(u) = N(u) − ρu = 1 − ρ + E(u), C = composites, ζ_c(s) = (s − 1 + ρ)/(s − 1) (the template), F_X = truncated ζ_P (s40 NOTE 1.5).
(A): R ≥ r₀ > ρ on [1, ∞). (B): R = O(u^θ), θ < ½·r₀/(r₀ + ρ).

## §0. Close

**Close: the obstruction is NOT proved. Proved instead: "proof class X cannot yield it, because of the controls below", the exact form
the obstruction must take, and one weak joint statement. Stop condition (ii) of the charter.**

**Theorem (method classes; §2, Thm 2.1, Cor. 2.2, Rem. 2.3)** [proved here; novelty: single-check]. Fix ρ < ¼.
(i) No argument whose premises on the system are (A), (B) and integrality of N — Parseval/Plancherel and Carlson mean values on vertical
lines, the L² abscissa ½ of integer-coefficient series, Hilberdink 2005's (3.2)–(3.4), Remark C and Cor. 2, Neamah–Hilberdink's Thm 1,
Landau's theorem on R − r₀ ≥ 0, Theorem 1.6 — can prove that (A) and (B) are incompatible, nor even that E is unbounded: the lattice
control L_ρ(s) = 1 + ρ^s ζ(s, ½ + ρ) (atoms at 1 and at S8's prime lattice 1 + (k − ½)/ρ) satisfies all those premises with
E_L ∈ (−½, ½] and has a real zero in (1 − 2ρ, 1) (π/16: 0.788933; S8: 0.794755; template: 0.803650) plus complex zeros right of ½.
(ii) No argument using positivity of the prime measure (PNT, Mertens, Λ ≥ 0, non-vanishing on Re s = 1) without integrality can: the
template has all of it with E ≡ 0. (iii) Integrality and positivity together, with a real zero > ½, still allow an exactly regular count when the
norms lie on a geometric lattice: the virtual curve V over F₅ has both, a real zero 0.79899 and a constant degree-level integer error
−¼ (it undershoots, so it fails (A)); a proof must use the continuum of norms, or (A) beyond its consequence "there is a real zero".
**Where discreteness must enter: the clip.** L_ρ is S8's lattice with every composite cancelled by integer Euler exponents of
alternating sign (m = −1 at every 2-fold product, (−1)^{k+1}(k − 1)! at k distinct factors; Prop. 1.1(v)). A proof must use that composites of a
discrete positive system are atoms of weight +1 that nothing removes (Π ≥ 0 at products of g-primes), at real (archimedean) positions.

**Consequences proved here.** (a) Conjecture U is FALSE for signed discrete systems: L_ρ has α_L ≥ σ*_L > ½ = max{½, 2β_L} (§1.3); with the
known failure for continuous systems, U, if true, rests on positivity AND integrality. (b) Clip bound: any discrete system with E ≥ −c has
sup_{u≤x}E ≥ Q(x) − c, Q the composite excess; for S8 the converse holds (s40 Cor. 1.4′), so **for S8, (B) ⟺ Q(x) = O(x^θ): the obstruction
for S8 is exactly an Ω-theorem for the composite excess** (§5.1). (c) Integrality alone says only (1/U)∫_U^{2U}E² ≥ 1/12 − o(1), attained
uniquely by the lattice (Prop. 3.2). (d) No discrete Beurling system satisfying (A) for any r₀ > 0 has N(x) − ρx periodic (Cor. 6.1, from
Hilberdink 2012 Thm A at the page) — the only joint (D)+(P) result found, and it does exclude L_ρ, whose R is periodic.

**GAP (exact).** The obstruction, and already its weakest form "E is unbounded on class (A)", reduce (§5.3, §6.2) to one statement:
*keeping E small forces some product of g-primes to be missing* — equivalently, products of a bounded number of large g-primes cluster
by x^θ in windows of length ≲ x^θ·log x (orchestrator O4). Neither direction has a tool; it is the bilinear object on which Lemma B_ρ is
stuck from the other side. The discrete local form of positivity, (★) of §6.2, is the inequality such a proof would have to violate.

**Evidence against the obstruction** [computed; U7 quoted]. For S8(π/16) the composite excess is Q = 9.75, 12.75, 16.66 at 10⁶, 10⁷, 10⁸
(own generator; sup E within ½ of Q at every decade) and sup E = 26.14 at 10¹⁰ (U7): Q/log²x = 0.049 flat, Q/x^{σ*/2} = 0.040 → 0.0028.
The square-root heuristic behind U assumes a prime deficit placed independently of the composites; S8 refuses exactly the slots the
composites took (s40 Prop. 2.1), and randomizing the placement by width 50 raises sup E at 10⁷ from 12.8 to 58–171 (s40 §3.1, quoted). The real zero is a first-order (mean
density) property; E is a second-order (clustering) property; L_ρ, T and S8 share the first and differ in the second.

## §1. Three objects: the template, the lattice control, S8

**1.1 Template T** [quoted: s40 NOTE Lemma 1.5, l. 96–98]. dN_c = δ₁ + ρdu, ζ_c = (s − 1 + ρ)/(s − 1), prime density (1 − u^{−ρ})/log u ≥ 0,
E ≡ 0, one zero s = 1 − ρ. So R_c ≡ 1 − ρ: (A) with r₀ = 1 − ρ (> ρ when ρ < ½), (B) with every θ ≥ 0. T is a CONTINUOUS system with a
positive prime measure, a real zero > ½ and no integer error.

**1.2 The lattice control L_ρ** [novelty: single-check]. Atoms of weight 1 at 1 and at the S8 prime lattice ℓ_k := 1 + (k − ½)t, k ≥ 1:
  L_ρ(s) := 1 + Σ_{k≥1} ℓ_k^{−s} = 1 + ρ^s ζ(s, ½ + ρ)   (ζ(s, a) Hurwitz; ℓ_k = t(k − ½ + ρ)).
**Proposition 1.1** [proved here unless marked]. (i) N_L(x) = 1 + ⌊ρ(x − 1) + ½⌋ for x ≥ 1, so E_L(x) = ⌊ρ(x − 1) + ½⌋ − ρ(x − 1) ∈ (−½, ½]:
R_L ≥ ½ − ρ =: r₀ (hypothesis (A) when ρ < ¼) and R_L is bounded ((B) with θ = 0). (ii) L_ρ(s) = ζ_c(s) + sÊ_L(s) (Mellin identity of s40
1.5, which uses only N), analytic on Re s > 0 except the pole at 1 (residue ρ); the continuation to ℂ is Hurwitz's [recalled, not used].
(iii) The proof of Theorem 1.6 uses only (A), (B) and that identity (read-O A1: no positivity, no discreteness of Π), so L_ρ(σ) ≥ ½ − ρ/(1 − σ)
on (0, 1) and L_ρ has a real zero σ*_L ∈ (1 − 2ρ, 1). (iv) −L′/L has a pole at σ*_L, so ψ_L(x) − x ≠ O(x^a) for a < σ*_L (last paragraph of
the proof of Thm 1.6; again no positivity). (v) **Signed integer Euler product.** Let t be transcendental. Then formally
  L_ρ(s) = Π_λ (1 − λ^{−s})^{−m_λ},  λ over the multiplicative semigroup generated by the ℓ_k,  m_λ ∈ ℤ,
  m_λ = Σ_{j | g} μ(j)·c(e/j)/j,  c(e) := (−1)^{k+1}(k − 1)!/Π_i e_i!,  for λ = Π_i ℓ_i^{e_i}, k = Σe_i, g = gcd(e_i).
So m = +1 at every ℓ_k; m = −1 at every ℓ_aℓ_b (a ≠ b) and every ℓ_a²; m = (−1)^{k+1}(k − 1)! at a product of k distinct lattice points.
*Proof of (v).* Integrality: order the λ; m_λ := (coefficient of L at λ) − (coefficient at λ of Π_{μ<λ}(1 − μ^{−s})^{−m_μ}); each factor has
integer coefficients for m_μ ∈ ℤ, so by induction every m_λ ∈ ℤ, and the product reproduces L up to λ (the factor at λ adds m_λ at λ and
only larger terms beyond). Formula: log L = Σ_j (−1)^{j+1}X^j/j with X = Σ_kℓ_k^{−s}; the products Πℓ_i^{e_i} are the values at t of the
pairwise distinct polynomials Π(1 + (i − ½)X)^{e_i} ∈ ℚ[X] (s40 Lemma 1.3: distinct multisets give distinct products), so the coefficient
of λ in X^k is the multinomial k!/Πe_i! and the coefficient of log L at λ is c(e). On the other side the coefficient of log Π(1 − μ^{−s})^{−m_μ}
at λ is Σ_{j: μ^j = λ} m_μ/j, and μ^j = λ forces j | g, μ = λ^{1/j} (unique factorization again); Möbius inversion over j | g gives m_λ. ∎
*Check* [computed: `verify/hurwitz_control.py`, log `hurwitz_control.log`]: ρ = π/16, all λ ≤ 400: 78 lattice points (m = +1), 35 two-fold
products (m = −1), six ℓ_a²ℓ_b (m = +1), ℓ₁³ (m = 0), ℓ₁³ℓ₂ (m = −1), ℓ₁⁴ (m = 0); the truncated signed product gives 1.0247170 and 1.0501612
at s = 3, 2.5 against L = 1.0247173, 1.0501717 (truncation tail ≈ 6·10⁻⁷, 2·10⁻⁵). E_L ∈ [−0.5000, 0.5000] on a 2·10⁵-point grid.

*Every (A)-parameter has a control* [proved here, same proof]: for 0 < ρ < r₀ < 1 − ρ, L_{ρ,r₀}(s) := 1 + ρ^s ζ(s, 1 − r₀) has atoms
at 1 and (k − r₀)/ρ, k ≥ 1, N − ρx ∈ (r₀, r₀ + 1], and a real zero in [r₀/(r₀ + ρ), 1) by Remark 1.6′ of s40; L_ρ is the case r₀ = ½ − ρ.

**1.3 What L is.** L is S8's prime lattice with EVERY lattice point an atom of N and every composite cancelled by integer multiplicities (−1 at 2-fold products).
S8 has the same slots, but its composites are forced atoms with multiplicity +1 that nothing removes: the rule can only refuse slots
(the clip, s40 §2.2). L is therefore a *signed discrete Beurling system* (integer N, integer Euler exponents of both signs) satisfying
(A) and (B) with θ = 0, a real zero > ½ (for ρ ≤ ¼), and α_L ≥ σ*_L by (iv): **Conjecture U fails for signed discrete systems** [proved here].

**1.4 The real zeros side by side** [computed: `hurwitz_control.log`; S8 values quoted from s40 NOTE §1.8, l. 130–137]:

| ρ | 1 − 2ρ | T: 1 − ρ | L: σ*_L | first-order s₀ + ρL(s₀) | S8: σ* | L(0) = 1 − ρ |
|---|---|---|---|---|---|---|
| π/64 | 0.9018 | 0.950913 | 0.947589 | 0.947802 | 0.947634 | 0.950913 |
| π/32 | 0.8037 | 0.901825 | 0.893876 | 0.894460 | 0.895076 | 0.901825 |
| π/16 | 0.6073 | 0.803650 | 0.788933 | 0.789824 | 0.794752 | 0.803650 |
| π/8 | 0.2146 | 0.607301 | 0.589399 | 0.589755 | 0.656529 | 0.607301 |

The three objects have real zeros within 0.015 of each other for ρ ≤ π/16 and integer errors 0, O(1) and (numerically) ≈ 0.05 log²x.
L(0) = 1 + ζ(0, ½ + ρ) = 1 − ρ is the logarithmic mean of R_L (Abelian limit of sF(s), F = Mellin transform of R).

**1.5 S8 data from this unit's own generator** [computed: `verify/s8u5.c` (event heap, double; statistics only), logs
`s8u5_pi16_1e7.log`, `s8u5_pi16_1e8.log`, `s8u5_pi32_1e8.log`]: π/16: sup E = 9.636, 12.839, 16.364 at 10⁶, 10⁷, 10⁸; π(10⁷) = 633,514;
largest gap 66 cells at 10⁷; π/32: sup E = 6.393, 8.928, 9.858 — the s40 values (NOTE l. 134, 215) to the printed digits. sup Q, the largest
composite excess sup_{y≤x}(C[y, x] − ρ(x − y)), is within ½ of sup E at every decade (Cor. 1.4′ of s40): 9.754, 12.748, 16.655 (π/16).

## §2. The method-class theorem: what any obstruction proof must use

A *datum* is a non-decreasing right-continuous N on [1, ∞) with N(1) = 1, dN = exp*(dΠ) for a real measure Π on (1, ∞) (Π := log* N
always exists as a formal Mellin–Stieltjes logarithm). Two properties a proof may use:
- **(D) integrality**: N is a step function, all jumps positive integers, at a locally finite set;
- **(P) positivity**: Π ≥ 0.
A discrete Beurling system has (D) and (P). Under (D) alone, Π = Σ_λ m_λ Σ_j δ_{λ^j}/j with m_λ ∈ ℤ (induction of 1.2(v), which used only
integer coefficients); (P) then says Σ_{j: μ^j = λ} m_μ/j ≥ 0 at every λ, i.e. m_λ ≥ 0 wherever λ is not a perfect power.

**Theorem 2.1 (two controls)** [proved here]. Fix ρ ∈ (0, ¼).
(a) The lattice control L_ρ has (D), (A) with r₀ = ½ − ρ > ρ, and (B) with θ = 0 (Prop. 1.1); it violates (P) exactly at the products of
an even number of atoms (Π_L(λ) = c(e) of Prop. 1.1(v) has the sign (−1)^{k+1}; −1 at every 2-fold product).
(b) The template T has (P), (A) with r₀ = 1 − ρ, and (B) with E ≡ 0; it violates (D) (N is continuous on (1, ∞)).
Consequently: (c) no statement of the form "(A) and (D) imply E ≠ O(f)" with f → ∞ is true, and no such statement follows from (A) and (P);
in particular "E is unbounded" — the weakest Ω-statement — is already false on each of the two classes separately. (d) Any proof that
(A) and (B) are incompatible for discrete Beurling systems, and any proof that E is unbounded there, must use (D) and (P) TOGETHER, and
must use (P) at products of g-primes: an argument valid on {(D), (P) at non-products} is valid for L_ρ (whose Π equals +1 at each atom
ℓ_k, the analog of g-primes) and so cannot reach a contradiction.
*Proof.* (a), (b): §1. (c), (d): a deduction from premises that a control satisfies yields a statement true of the control; L_ρ and T
satisfy (A), (B) and have bounded E. ∎

**What (c)–(d) mean in words.** Discreteness enters only through the CLIP: a composite of a discrete positive system is an atom of N of
weight +1 that no later choice can remove (Π ≥ 0 at products), while the g-primes themselves are placed freely. The template has no atoms
to clip; the lattice control removes every composite by multiplicities of alternating sign. The obstruction, if true, is a statement about how
unavoidable composites cluster — §5 makes this exact for S8.

**Scope of the controls (stated so that nobody over-reads 2.1).** (i) L_ρ does NOT have an Euler product with Π ≥ 0, so it need not satisfy
consequences of (P) on Re s ≥ 1: non-vanishing of ζ on Re s ≥ 1, Λ ≥ 0, the PNT ψ ~ x, Mertens' product. Its log-series converges
absolutely only for Re s > σ₁ > 1 (§3.4 computes σ₁), and zeros of L in 1 < Re s < σ₁ are possible (searched for in §3.4). (ii) T satisfies
all of those (Λ_c(u) = 1 − u^{−ρ} ≥ 0, ψ_c(x) ~ x, ζ_c ≠ 0 on Re s ≥ 1) but has no atoms. So the only arguments NOT covered by Theorem 2.1
are those that combine an integrality input with a positivity input (PNT, Mertens, Λ ≥ 0, non-vanishing on Re s = 1). The ones in print
that we have at the page are treated in §6: the Legendre–Mertens identity (s40 read-O F1) and Hilberdink 2012 (periodic integer error).

**Corollary 2.2 (the named analytic methods).** Each of the following is valid, as an argument, for every datum with (D) and the analytic
hypotheses it states, hence for L_ρ; so none of them can prove the obstruction, or even E unbounded, on class (A):
(1) Parseval/Plancherel for Ê on vertical lines and Carlson-type mean values of Σ a_n n^{−s} (§3); (2) Hilberdink's mean-value inequality
(3.2)–(3.3) and its contradiction scheme (JNT 112, pp. 337–340), and his Remark C (§4); (3) Neamah–Hilberdink's Theorem 1 (§4);
(4) Landau's theorem applied to the non-negative function R − r₀ (§6.3(a)); (5) Theorem 1.6 and every bound on the location of the real
zero derived from it. Verification for each item is in the section named.

**Remark 2.3 (a third control at rung 1: (D) and (P) jointly are still not enough)** [re-derived and computed: `verify/curveV_check.py`
→ `curveV_check.log`; the object is the orchestrator's suggestion, SHARED 17:30, from `results/novel-wave-s39/insights-digest.md` §C].
The virtual curve V over F₅, Z(u) = (1 − 5u + 5u²)/((1 − u)(1 − 5u)), u = 5^{−s}: A_n = (5^n − 1)/4 for n ≥ 1 (A₀ = 1); closed-point counts
b_d = 1, 5, 25, 110, 500, 2215, 10000, 45100, … are non-negative integers (checked to d = 16), so V has (D) and (P); its zeros are at
Re s = 0.79899 and 0.20101 (u = (5 ∓ √5)/10). Its degree-level integer error A_n − 5^n/4 = −1/4 is CONSTANT, and Z(5^{−σ}) changes sign at
0.79899 exactly as in Theorem 1.6 (Z → −∞ as σ → 1⁻), although V undershoots and so fails (A). So a real zero > ½, integer weights and a
positive prime measure coexist with a perfectly regular count once the norms are confined to the geometric lattice 5^ℤ. Together with
Theorem 2.1: a proof of the obstruction must use (D) and (P) jointly at products AND the archimedean feature V lacks — that g-integers
take a continuum of values, so that (B) constrains N between the norms of its own elements — or use (A) beyond its consequence "there is
a real zero" (V has the zero without (A)).

## §3. Mean square, Parseval, the L² abscissa ½ — at the line, with tests

**3.1 Parseval on vertical lines** [proved here; standard]. If E = O(u^θ) and σ > θ, then v ↦ E(e^v)e^{−σv} lies in L¹ ∩ L²(0, ∞) and
Ê(σ + it) is its Fourier transform, so ∫_ℝ|Ê(σ + it)|²dt = 2π∫_1^∞E(u)²u^{−2σ−1}du; and ζ_P = ζ_c + sÊ. Any mean-square argument on a
vertical line is a statement about the two sides of this identity.

**Proposition 3.2 (the whole content of integrality for the size of E)** [proved here]. Let N have unit atoms (D) and density ρ, with
n(U) = ρU + o(U) atoms in [U, 2U]. Then (1/U)∫_U^{2U}E(u)²du ≥ (1/12)(1 + o(1)), with equality iff the atoms in the block are equally spaced
and E is centred on each gap — the lattice control L_ρ attains it exactly.
*Proof.* Between consecutive atoms E is linear with slope −ρ; on a gap of length ℓ_i, ∫(e_i − ρv)²dv over v ∈ [0, ℓ_i] ≥ ρ²ℓ_i³/12 (minimum
at e_i = ρℓ_i/2). Hölder: Σℓ_i³ ≥ (Σℓ_i)³/n² = U³/n². So ∫_U^{2U}E² ≥ ρ²U³/(12n²) = (U/12)(1 + o(1)). Equality forces all ℓ_i equal to
1/ρ and e_i = ½, which is E_L. ∎ Consequence (summing dyadic blocks): ∫_1^∞E²u^{−2σ−1}du ≥ (1 + o(1))/(48σ log 2) as σ → 0⁺, i.e. "E is
not o(1) in mean square" — and nothing more, since L_ρ meets the bound with E_L bounded. *Test* [computed: `meansq_split.log` (4)]: block
mean squares 0.5392, 0.7037, 1.1351, 1.4879 (S8(π/16), U = 10³, 10⁴, 10⁵, 4.9·10⁵) against 0.083395, 0.083349, 0.083333, 0.083333 (L).

**3.3 Where S8 and L differ on a vertical line** [computed: `verify/meansq_split.py`, log `meansq_split.log`; X = 10⁵, both truncated
at X; 1500 stratified t-samples per window]. Parseval check: Σ over windows |t| ≤ 2048 gives 1.0267 (S8) and 0.6714 (L) at σ = 0.3 against
the exact 2π∫_1^X E²u^{−1.6} = 1.0543 and 0.6875 (σ = 0.45: 0.4821/0.4835, 0.3946/0.3955); the shortfall is the tail |t| > 2048.
Energy ∫_W|Ê(σ + it)|²dt by frequency window, ratio S8/L:

| window W | σ = 0.10 | σ = 0.30 | σ = 0.45 | (1/|W|)∫_W|Σ_{n≤X}n^{−s}|² at σ = 0.3: S8 / L / Σ_{n≤T}n^{−0.6} |
|---|---|---|---|---|
| [0, ¼] | 89.4 | 5.28 | 0.70 | 756233 / 756071 / 1 |
| [½, 1] | 6.15 | 2.75 | 2.11 | 374466 / 374432 / 1 |
| [8, 16] | 2.44 | 1.46 | 1.19 | 3002.6 / 3001.7 / 1.96 |
| [64, 128] | 2.48 | 1.45 | 1.18 | 52.16 / 50.85 / 3.90 |
| [256, 512] | 2.84 | 1.45 | 1.10 | 12.20 / 9.55 / 6.43 |
| [1024, 2048] | 3.69 | 1.73 | 1.26 | 18.50 / 11.11 / 10.86 |

Reading: (i) the Dirichlet polynomials of S8 and L have the same mean square to 0.2 % up to T = 32 (the smooth part ρX^{1−s}/(1 − s)
dominates); (ii) beyond T ≈ 100 L's mean square tracks the diagonal Σ_{n≤T}n^{−2σ} (the lattice's dual-sum cancellation, as for ζ), while
S8's exceeds it — off-diagonal terms of g-integers closer than 1/ρ: local clustering; (iii) the low-frequency energy |t| ≲ 1, which is the
multiplicatively smoothed amplitude of E, is where the two differ most (factor 3–89 at σ ≤ 0.3). The L² abscissa ½ is the statement that
the high-frequency energy decays only like |t|^{−1−2σ} (unit jumps at density ρ) — met by both.

**3.4 Zeros right of ½ and the abscissa σ₁ of L** [computed, exploratory: `verify/zeros_newton.py` → `zeros_newton.log`; `sigma1_L.log`;
`zeros_L_S8.log`]. Newton from minima of |f| on five vertical lines, kept if |f| < 10⁻⁸ (not an exhaustive count): L_{π/16} has ≥ 12 zeros
in ½ < Re s < 1, 0 < Im s < 100 (e.g. 0.730915 + 42.089392i, 0.512474 + 22.437213i); F_{10⁶} of S8(π/16) has ≥ 6, among them
0.573259 + 30.779677i (s40 NOTE l. 194 to all six digits), 0.523335 + 16.080818i, 0.587661 + 62.291038i. Both objects are "RH-false" in the
same way — a real zero near 1 − ρ plus complex zeros right of ½ (Cor. 2(b) of Hilberdink predicts infinitely many for both) — with
E_L bounded. σ₁ (where Σ_kℓ_k^{−σ₁} = 1) is 1.181340 (π/16) and 1.091222 (π/32): log L converges absolutely only beyond it. A scan of
|L| on Re s = 1.02, 0 < t < 1000, for zeros right of 1 exceeded 30 minutes and was stopped (stop line (iii); `zeros_L_S8.log`): whether
L vanishes in 1 < Re s < σ₁ was not settled numerically.

## §4. Hilberdink 2005 and Neamah–Hilberdink at the page

**4.1 What is proved there** [quoted: `novel-wave-s37/beurling-frontier/sources/w-18a-…JNT112.txt`; JNT 112 (2005)].
Theorem 1 (l. 195, p. 335): for an [α, β]-system, max{α, β} ≥ ½. Cor. 2(b) (l. 211–214, p. 336): if N_P(x) = ρx + O(x^β), β < ½, then for
every γ ∈ (β, ½), ψ_P(x) − x = Ω(x^γ) and ζ_P has infinitely many zeros in γ < Re s < 1. Remark C (l. 496–501, p. 340): for β < α, if
ζ_P has finitely many zeros in Re s > η with η ∈ (β, α), then η ≥ ½. The mechanism (l. 268–494, pp. 336–340): (3.2)–(3.3), the
Fejér-averaged mean square of the partial sums ζ_N(σ + it) = Σ_{n≤N} n^{−σ−it} is ≥ (k₁/2)R²N^{1−2σ} for N ≤ (k₁/2k₂)R — its only inputs
are integer weights (Σ* with multiplicities squared ≥ Σ n^{−2σ} ≥ k₁N^{1−2σ}, l. 301–307), N ~ ρx, and the positivity of the Fejér sum
Σ_r sin((2r − 1)log(n/m)) for 0 < log(n/m) < log 2 (l. 334–341); (3.4), |ζ_N(σ + it)| = O(|t|^ε) for N^{1−σ} ≤ |t| < N⁵, from ZERO ORDER of
ζ_P on Re s = σ, supplied by Hilberdink–Lapidus Thm 2.3 or by Remark B(ii) (finitely many zeros). The contradiction is (3.3) vs (3.4).
Where Theorem 2.3 uses positivity [quoted: `…/p3-22c1-hilberdink-lapidus-2006-…arxiv.txt` l. 748–812]: Borel–Carathéodory on log ζ in
Re s > Θ, then Hadamard three circles with the bound M₁ = max_{C₁}|φ| ≤ φ(1 + η) = O(1) on Re s > 1 (l. 788), i.e. |Σ Λ(n)n^{−s}| ≤ Σ Λ(n)n^{−σ}.

**4.2 What the mechanism gives on class (A)** [proved here]. With (A) and (B) for θ < ½: α ≥ σ* > ½ (Thm 1.6), so Theorem 1 is satisfied
and says nothing; Cor. 2(b)/Remark C say ζ_P has infinitely many zeros in η < Re s < 1 for every η ∈ (θ, ½). That is a statement about
zeros. The step that would bear on E is (3.4) — an upper bound for the partial sums — and it is available only where ζ_P has zero order,
i.e. (Remark B(ii)) to the right of all but finitely many zeros; the real zero σ* and the infinitely many zeros of Cor. 2(b) are exactly
what removes it. So in class (A) the method has no inequality left that involves the size of E.

**4.3 The method on the lattice control** [proved here]. (3.2)–(3.3) hold for L_ρ verbatim (integer weights, N_L ~ ρx). The three-circles
step needs |φ| bounded on some right half-plane; for L this holds on Re s ≥ σ₁ + η, σ₁ > 1 the abscissa where Σ_kℓ_k^{−σ₁} = 1 (log L
absolutely convergent beyond it), and the proof runs with 1 replaced by σ₁ (κ → (σ₁ − σ)/(σ₁ − Θ) < 1: zero order again). Hence every
conclusion of 4.1–4.2 holds for L_ρ (with E_L bounded): Cor. 2(b) predicts infinitely many zeros of L in η < Re s < 1 for each
η ∈ (0, ½); exploratory counts are in §3.4. So no strengthening of this method to "β ≥ f(σ*)" with f > 0 is possible: L_ρ is an
object to which the method applies, with σ*_L > ½ and β_L = 0.

**4.4 Neamah–Hilberdink** [quoted: `results/local-greedy-s40/sources/neamah-hilberdink-1901.06866v2.txt` l. 104–105 (Thm 1), l. 226–244
(proof)]. With γ the exponent of M_P(x) = Σ_{n≤x}μ_P(n): of α, β, γ the two largest are equal and ≥ ½. The proof applies a Tauberian
converse (their Thm A) to 1/ζ_P, with zero order of 1/ζ_P on H_Θ from Hilberdink–Lapidus Thm 2.3 (their Thm B). On class (A):
β ≤ θ < ½ < σ* ≤ α, so γ = α ≥ σ*: M_P(x) = Ω(x^{σ*−ε}) — a statement about M_P, not E. On L_ρ: 1/L has integer coefficients μ_L (on the
semigroup of §1.2), and the same steps (with σ₁ for 1, as in 4.3) give γ_L = α_L ≥ σ*_L with β_L = 0. Nothing in it touches E.

**4.5 Where the "L² abscissa ½" sits.** For a Dirichlet series with integer weights on a set of positive density, Σ a_n²n^{−2σ} = ∞ for
σ ≤ ½, so no such series has bounded mean square on a line Re s ≤ ½ (Carlson's theorem, quoted at Hilberdink l. 237–262, is the
well-spaced form; (3.2)–(3.3) is the form without spacing). This is a fact about the JUMPS of N (unit atoms at density ρ), and both S8
and L_ρ have the same jumps at the same density; its whole content for E is Prop. 3.2 (block mean square ≥ 1/12, attained by L_ρ).
§3.3 measures where S8 and L differ on vertical lines: (i) at |t| ≲ 1 — the AMPLITUDE of E, the thing (B) is about — by factors 3–89;
(ii) at |t| ≳ 100, by factors 1.2–3.7, through the off-diagonal terms of g-integers closer than the lattice spacing (local clustering,
which the rigid lattice lacks). A lower bound for (ii) would detect clustering, but the real zero is a statement at t = 0 and L_ρ has the
zero with no clustering at all. Integer weights force irregularity at additive scale 1, which is harmless; (B) is about multiplicative scale 1.

**4.6 U1's relative wall (SHARED 17:33), re-derived, and why it is an Ω for the PRIMES, not for E** [proved here, following U1's
sketch]. Let P have (D) and (B) with θ < ½, and suppose Π_P − Π_ref = O(u^{α′}), α′ < ½, for a reference whose ζ_ref is meromorphic with
finitely many zeros right of some γ₀ < ½ (e.g. ζ_c). Then ζ_P = ζ_ref·exp(η̂), η̂(s) = s∫(Π_P − Π_ref)u^{−s−1}du analytic on Re s > α′, so ζ_P
has finitely many zeros right of max(θ, α′, γ₀) < ½ — against Remark C/Cor. 2(b) (4.1; valid under (D), and for signed data by 4.3). So on
class (A)&(B) the g-primes deviate from every finitely-zeroed reference by u^{½−ε}: the primes must be wild. This does not touch E: ℕ has
wild primes and bounded E, and L_ρ satisfies the wall's conclusion (its Π_L is far from tame: ≥ 12 zeros right of ½, §3.4) with E_L
bounded. The obstruction would need the converse direction, wild primes ⇒ large E, which ℕ refutes in general.

## §5. Where discreteness must enter: the clip, and the exact form of the obstruction for S8

**Proposition 5.1 (the clip bound)** [proved here]. Let P be a discrete Beurling system with E ≥ −c on [1, ∞). For every interval
I = (a, b]: E(b) ≥ E(a) + C(I) − ρ|I| ≥ C(I) − ρ|I| − c, where C(I) is the number of composite g-integers in I (with multiplicity).
Hence sup_{u≤x}E(u) ≥ Q(x) − c, with Q(x) := sup_{I⊂[1,x]}(C(I) − ρ|I|) the *composite excess*.
*Proof.* N(b) − N(a) ≥ C(I), since every g-integer in I is counted by N and the g-primes in I add ≥ 0; subtract ρ|I|. ∎
(D) is used in "every composite is an atom of weight ≥ 1", (P) in "no later choice removes it" (m_λ ≥ 0 at products). For L_ρ the products
are not atoms at all (Prop. 1.1(v)), so 5.1 is empty there, which is how L escapes.
**For S8 the converse holds** [quoted: s40 NOTE Cor. 1.4′, l. 92–94]: E(x) = sup_{y≤x}(C[y, x] − ρ(x − y)) + r(x), r ∈ (−½, ½]. So
  **for S8(ρ): (B) with exponent θ ⟺ Q(x) = O(x^θ).** The obstruction for S8 is exactly an Ω-theorem for the composite excess.
[computed: `s8u5_*.log`] sup E − Q(x) ∈ [−0.30, +0.49] at every decade 10³…10⁸ for π/16 and π/32 (extremes −0.291 at 10⁸ for
π/16, +0.482 at 10⁵ for π/32), inside the (−½, ½] the identity allows.

**5.2 The square-root heuristic, written as an inequality and tested.** The heuristic behind Conjecture U (s37 NOTE §7.2: random
surgery gives β = α/2) predicts that a prime deficit of mass ≍ x^{σ*}/log x, placed without regard to the composites, leaves a composite
excess of order the square root of that mass: Q(x) ≥ c·x^{σ*/2}/log x infinitely often. For S8(π/16), σ*/2 = 0.3974 [computed + quoted]:

| x | Q(x) (this unit) | sup E | x^{σ*/2} | Q/x^{σ*/2} | Q/log²x |
|---|---|---|---|---|---|
| 10⁶ | 9.754 | 9.636 | 242 | 0.040 | 0.0511 |
| 10⁷ | 12.748 | 12.839 | 605 | 0.021 | 0.0491 |
| 10⁸ | 16.655 | 16.364 | 1511 | 0.011 | 0.0491 |
| 10¹⁰ | — | 26.137 (U7, SHARED 17:05) | 9420 | ≈ 0.0028 | ≈ 0.049 |

The ratio to x^{σ*/2} falls by a factor 14 over four decades, the ratio to log²x is flat. An Ω-statement cannot be refuted on a finite
range, but the heuristic's mechanism is visibly absent: in S8 the deficit is not placed at random — a slot is refused exactly when the
composites have taken it (Prop. 2.1 of s40: E = ½ + C(p_k, x] − ρ(x − p_k) on every gap), so the deficit tracks the composites instead of
adding independent noise to them. s40 §3.1 measured the converse: random offsets of width 50 raise sup E at 10⁷ from 12.8 to 58–171.

**5.3 Where a composite clump must come from** [proved here: identity and bound; the reduction beyond it is a GAP]. Fix z and an
interval I = (a, b] with a > z. Inclusion–exclusion over squarefree d | P(z) (free monoid: the multiples of d are exactly d·G) gives
  C(I) − ρ|I| = [C_rough(I) − ρ|I|M(z)] − S_z(I),  S_z(I) := Σ_{d|P(z), d>1} μ(d)·ΔE(I/d),
with M(z) = Π_{p≤z}(1 − 1/p), ΔE(J) = N(J) − ρ|J|, and C_rough(I) the composites in I with every g-prime factor > z. (Derivation: the
composites with a factor ≤ z number N(I) − Σ_{d|P(z)}μ(d)N(I/d) = ρ|I|(1 − M(z)) − S_z(I), and the g-integers in I prime to P(z) are the
g-primes > z and the z-rough composites.) Every I/d (d > 1) lies below b/p₁, so
  |S_z(I)| ≤ 2^{π(z)+1}·max_{y≤b/p₁}|E(y)|.
So, for FIXED z, a composite excess at scale x larger than 2^{π(z)+1} times the largest |E| one scale down is a clump of z-ROUGH
composites in excess of their share ρ|I|M(z) (a share they split with the g-primes > z). For z = p₁ this is orchestrator note O3:
multiples of p₁ in a window are as regular as N one scale down. A power-size clump therefore has to be built from rough composites at
the scale where E first becomes large; the natural target — products of two g-primes in (x^{1/3}, x^{2/3}) clustering by x^θ in a
window of length ≲ x^θ·log x, orchestrator note O4 — is not reached by this bound (2^{π(z)} explodes when z grows with x). No unit has a
tool for rough-composite clustering in either direction; it is the object on which Lemma B_ρ's proof is stuck from the other side.

## §6. Attempts at a weaker Ω-theorem, and where each stops

**Corollary 6.1 (periodic integer error is impossible on class (A))** [proved here, from Hilberdink 2012 Thm A, quoted:
`novel-wave-s37/beurling-frontier/sources/p3-22c2-…periodic-counting.txt` l. 102–112; Acta Arith. 152 (2012)]. If a discrete Beurling
system has N(x) − ρx periodic, then inf_{x≥1}(N(x) − ρx) < 0; so no system satisfying (A) for any r₀ > 0 has periodic integer error.
*Proof.* A discrete system's N is a step function with locally finitely many jumps, so N lies in Hilberdink's class T (l. 268–270), and
"determines a g-prime system" is his Def. 1.3 (l. 326–333): Π = Σ_k π(x^{1/k})/k with π increasing — our (D)+(P). Thm A gives an integer
period P and N(x) = Σ_{n≤P, (n,P)=1}(⌊(x − n)/P⌋ + 1), so ρ = φ(P)/P. Since ⌊y⌋ − y has period-average −½, the period-average of
R = N − ρx is Σ_{n}(½ − n/P) over n ≤ P prime to P, which is φ(P)/2 − φ(P)/2 = 0 for P ≥ 2 (Σn = Pφ(P)/2) and −½ for P = 1. R is not
a.e. constant (it jumps by +1 at each integer prime to P), so it takes negative values. ∎
**The lattice control shows (P) is used:** N_L(x) − ρx = 1 − ρ + E_L(x) is periodic with period t and has inf = ½ − ρ > 0. Corollary 6.1
is therefore a genuine (D)+(P) statement — the only tool of that kind among the sources read for this unit (a search of the printed
literature was not made; §7) — and it separates L_ρ from every Beurling system.

**6.2 From periodic to bounded: where Hilberdink's argument stops** [reading at the page + proved here; the conclusion is a GAP].
His discontinuous case (§3, l. 488–600) uses (i) Thm 1.1(b), the jump part N_J of a system again determines a system (l. 371–378, uses
(P)); (ii) Props. 3.2–3.3 (l. 536–600): the discontinuities form finitely many residue classes mod P, so for irrational α at most k² of
them have αβ in the set, which inserted in the Chebyshev identity (N_J)_L = N_J ∗ ψ_J forces rational discontinuities. For BOUNDED R the
g-integers are only a bounded perturbation of an arithmetic progression (N(x) = ρx + O(1) ⟺ n_k = k/ρ + O(1)); the pigeonhole of 3.2
needs exact recurrence mod P and has no analog. The continuous case (Thm 2.1, l. 404–468) is a maximum principle for R′ at a recurring
maximum, using ψ′ ≥ 0; a discrete N has no R′. Its discrete form is local positivity of the primes: for I = (x, x + h], the Chebyshev
identity ∫_I log u dN(u) = Σ_β Λ(β)N(I/β) (exact; β over prime powers) isolates ψ(I) as the β ∈ I terms, and with N(J) = ρ|J| + ΔR(J)
and Mertens' Σ_{β≤x}Λ(β)/β = log x − A/ρ + o(1), A := ρ + ∫_1^∞R(u)u^{−2}du (the constant term of ζ_P at 1; the o(1) needs a PNT with
error o(x/log x) [recalled: Landau-type PNT under (B)]), ψ(I) ≥ 0 reads
  (★) Σ_{β≤x} Λ(β)·ΔR(I/β) ≤ ΔR(I)·log x + A·h + o(h) + O(N(I)·h/x).
(★) holds automatically for every Beurling system. For L_ρ it fails at short windows around every product of an even number of atoms (where Π_L < 0), in
particular every ℓ_aℓ_b (for h → 0 the Mertens term is multiplied by h and drops out, so L's lack of a PNT does not matter): there the images
I/ℓ_a ∋ ℓ_b and I/ℓ_b ∋ ℓ_a carry atoms (left side ≈ log ℓ_a + log ℓ_b ≈ log x) while I carries none (right side ≈ 0) — the negative
"prime" of Prop. 1.1(v), seen locally. A proof that E is unbounded on class (A) along Hilberdink's lines must show that (A), (D) and
bounded R force a window violating (★) — that keeping R bounded forces some product of g-primes to be absent. That is §5.3's
composite-clump statement in its weakest form. **GAP: open; no tool in hand.**
*Test* [computed: `verify/star_check.py` → `star_check.log`; S8(π/16), own dump to 10⁶, primes identified as atoms on the lattice to
relative 10⁻¹³ (count 72,603 = the generator's π(10⁶)); 400 windows per h at x ∈ [2·10⁵, 9·10⁵]]: the exact identity holds to 1.1·10⁻¹³ in
all 1600 windows; A = ρ + ∫R u^{−2} = 0.937500 (template: 1; π/32: 0.931643 — so the π/16 value 15/16 is a coincidence); (★) holds in every
window, with minimal slack 0.057, 0.286, 1.147, 5.851 for h = 1, 5, 20, 100; slack − ψ(I) = (0.0645–0.0650)·h on average (max 0.078h) — the
Mertens remainder, which on the template is exactly h·x^{−ρ} = 0.076h at x = 5·10⁵: the real zero's prime deficit, seen locally.

**6.3 Four smaller attempts** [proved here unless marked]. (a) *Landau on R − r₀ ≥ 0.* Ĝ(s) := ∫_1^∞(R − r₀)u^{−s−1}du is a Laplace transform of a
non-negative function: |Ĝ(σ + it)| ≤ Ĝ(σ), and its abscissa is a real singularity. This gives |ζ_P(s) − ρs/(s − 1) − r₀| ≤ |s|Ĝ(σ), the
growth O(|t|) that (B) gives anyway, and abscissa ≤ θ. L_ρ satisfies it. (b) *The value at 0.* For bounded R, ζ_P(0⁺) = lim sF(s) is
the logarithmic mean of R (Abelian), ≥ r₀ > 0, while ζ_P(1⁻) = −∞: a second proof of the real zero when θ = 0. Each subsystem P ∖ {q}
has ζ(0⁺) = 0 (factor 1 − q^{−s}), i.e. R(x) − R(x/q) has log-mean 0. Consistent with R ≥ r₀; L_ρ satisfies all of it (log-mean 1 − ρ =
L(0), §1.4). (c) *The zero as a constraint on E.* ζ_P(σ*) = 0 ⟺ ∫_1^∞E(u)u^{−σ*−1}du = −ζ_c(σ*)/σ*: one linear functional of E, equal to
−0.0545 for S8(π/16) and −0.0884 for L_{π/16} [computed from §1.4]. It carries no information on the amplitude of E. (d) *Legendre–Mertens* [quoted: s40 read-O F1, l. 227–243; s40 NOTE §3.4]. Freeness and the system's Mertens
law, (D) and (P) jointly, give π(I) = ρ|I|M(√b) + ΔE(I) + S(I) and the bias S(u, 2u] = (1 − 2e^{−γ} + o(1))u/log u: a statement about long
intervals, consistent with small E; as a bound on E it gives only |S| ≤ 2 sup|E|·#{d} ≍ u (Legendre's sieve, here as for ℕ) — nothing.

## §7. Instruments, what was not done, and why

**Scripts and logs** (all in `verify/`; scratch dumps of g-integers under `/private/tmp/rh-s41-lemmaB-U5-obstruction/`, < 2 MB each):
`s8u5.c` (own S8 generator: event heap over largest-prime-index factorizations, double precision; per-decade N, π, C, sup E, sup Q,
largest gap; reproduces s40's π/16 and π/32 rows to every printed digit) → `s8u5_pi16_1e7.log`, `s8u5_pi16_1e8.log`, `s8u5_pi32_1e8.log`;
`hurwitz_control.py` → `hurwitz_control.log` (E_L range, σ*_L for four ρ, the Thm 1.6 floor, L(0), signed Euler exponents and the
truncated-product check); `zeros_L_S8.py` → `zeros_L_S8.log` (exploratory argument-principle counts for F_{10⁵} of S8(π/16) and for L,
σ₁ of L, search for zeros of L right of Re s = 1); `meansq_split.py` → `meansq_split.log` (§3); `star_check.py` → `star_check.log`
(§6.2: exact local Chebyshev identity and (★) on S8(π/16) windows at 2·10⁵–9·10⁵, template comparison); `zeros_newton.py` → `zeros_newton.log` and
`sigma1_L.log` (§3.4); `curveV_check.py` → `curveV_check.log` (Remark 2.3).

**Recalled, unverified (none load-bearing):** the continuation of Hurwitz ζ(s, a) to ℂ and its digamma constant term; Lindemann
(π transcendental, so t = 16/π, 32/π and ½ + ρ are transcendental — used only for the closed form of m_λ in Prop. 1.1(v); integrality
of m_λ holds for every ρ); Bohr's theorem on values of Dirichlet series with independent frequencies (only to explain why zeros of L
right of 1 should exist); a PNT with error o(x/log x) under (B) (only for the Mertens form of (★); the exact identity in §6.2 needs none).

**Not done, and why.** (i) The obstruction is not proved, and the weakest Ω — "E unbounded on class (A)" — is open (GAP of §6.2): every
argument I could write either applies to L_ρ or T (Theorem 2.1), or needs a statement about clustering of products of two large
g-primes in short windows (§5.3), for which neither direction has a tool. (ii) No search of the printed literature beyond the on-disk
sources was made for further joint (D)+(P) results; Hilberdink 2012 is the one found. (iii) The zero counts of §3.4 are exploratory
(no certified argument principle); nothing in the close rests on them. (iv) S8 data come from a double-precision generator: statistics,
not certificates (the ordering margin issue of s40 §3.0 applies above ~7·10⁷).
