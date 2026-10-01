# NOTE — unit `U4-sparse` (stream `lemmaB-s41`): the sparse regime of S8(ρ) and the scaling limit ρ → 0

Session 41, started 17:07 IST 2026-10-01. Writer: Opus 5.5 (agent). Labels as in `../CHARTER.md` §4: **[proved here]**,
**[computed]** (script + log in `verify/`), **[quoted]**, **[recalled, unverified]** (never load-bearing). Gaps are marked GAP.

**Notation.** S8(ρ) as in `../../free-greedy-s40/CHARTER.md` §1. t := 1/ρ (as in the Session-40 NOTE). Lattice points
x_k := 1 + (k − ½)t = t(k + δ), δ := ρ − ½, k ≥ 1; p₁ = x₁ = 1 + t/2. The charter's scaling variable "t = ρ·log x" is written
**τ := ρ log x** here, to avoid the clash with t = 1/ρ. Lindley form (charter §2(a)): c_k = composites in (x_{k−1}, x_k],
e_k = max(e_{k−1} + c_k − 1, 0), prime at x_k iff e_{k−1} + c_k = 0. Template prime fraction per step f₀(τ) := (1 − e^{−τ})/τ,
template load λ₀(τ) := 1 − f₀(τ).

## §0. Close (filled last)

**Close, theorem-shaped.** (1) *Sparse range.* On every range where the feedback-free lattice monoid has load S_ρ ≤ 1 — i.e. up to
τ_c(ρ), with τ_c(ρ) → τ_c = 1.54609037074481 (root of I₁(2√τ)/√τ = 2) — S8 obeys **E(x) ≤ 3/2 + Q(x + t) ≤ 3/2 + 4ρ²(x + t)·e^{2τ+4ρ} + τ/(ρ log p₁)**,
and E(x) ≤ 2 + ρ√(x + t) on the pure two-fold range x < p₁³ (Thm 2.3, §2) [proved here]. The proof class "pathwise domination by the
lattice monoid + one count per component" cannot go further, for two named reasons: beyond τ_c(ρ) the comparison queue has load
Λ(τ) > 1 because domination forgets which lattice points are busy (overcount Λ − λ₀ = τ²/4 − 5τ³/144 + …) — the pathwise alternating
brackets of Prop. 3.3 are the systematic repair, and in the limit their even levels carry the range only to τ = 2.25, 2.98, 3.72, 4.46
(levels 2, 4, 6, 8), ≈ 0.73 per pair of levels, and at π/32 the level-2 queue stays ≤ 16 to 10⁹ while level 0 exceeds 65,535;
inside the range it cannot
beat Q because the only cluster bound it has is "+1 per component", and anything better is the shifted divisor problem for (ℤ + δ)² in
hyperbolic shells of width mρ (§3.2, Prop. 3.2: a cluster bound K gives E ≤ K + 3/2). Q is 10²–10³ times the truth (π/128: Q(10¹⁰) =
7,381, sup E = 7.09). (2) *Scaling limit.* For every S, uniformly on 1 ≤ y < x, p₁² ≤ x ≤ e^{S/ρ} as ρ → 0: π(y, x] = Π₀(y, x] + o(ρx), C(y, x] = Λ₀(y, x] + o(ρx),
E(x) = o(ρx); on all of 1 ≤ x ≤ e^{S/ρ}, −½ < E(x) ≤ ½ + o(ρx); and Σ_{p≤x} 1/p → Ein(τ) (Thm 4.4; with the rate C_S·ρ log(1/ρ), Thm 4.4′) [proved here; second read agrees, corrections applied]: the queue's arrival process
has intensity λ₀(τ) = 1 − (1 − e^{−τ})/τ per step at EVERY τ, the same function for every ρ, with no restriction to τ < τ_c. The
local structure is conjecturally Poisson(λ₀(τ)) (Conj. 5.2); its finite-ρ deviations are exactly those of the random-phase model of
independent progressions m′·P (one point per period m′ ≥ p₁ steps), with no free parameter (π/256, τ = 0.3: window dispersion D(16) =
0.897 measured, 0.896 predicted; P(c = 2)/Poisson = 0.938 vs 0.938), and they vanish like ρ² at fixed τ. For the Poisson limit queue,
P(e ≥ h) ≤ e^{−κh} and ρ·max_{x≤e^{τ/ρ}} e → η(τ) = τ/κ(λ₀(τ)) ~ τ²/2 (Prop. 5.3) [proved here, for the model]; for S8 the maximum is
proved o(ρe^{τ/ρ}) and explicitly bounded below τ_c, and conjectured to satisfy ρ·max E → η(τ) (Conj. 5.4).

**T — proved here:** Lemmas 1.1–1.3 (bottom of the system; E ↔ Lindley queue; the template is exactly self-similar in τ);
Thm 2.1 (e_k ≤ e_k^lat pathwise); Lemma 2.2, Thm 2.3 (explicit bound) and the elementary bound on Q; Prop. 3.1 (S_ρ → Λ(τ),
vol{Σu + max u ≤ τ} = τ^j/(j+1)!); Props. 3.2, 3.3 (pathwise alternating brackets); Thm 4.1; Lemmas 4.2, 4.3, 4.6; **Thms 4.4, 4.4′** (second read `read-T44.md`: AGREES-WITH-CORRECTIONS; its one gap,
Step 3's local mass bound, filled; corrections applied); Prop. 5.1 (model); Prop. 5.3 (model).
**C — computed** (`verify/`, 12 production runs, ρ = π/16 … π/256 to 4·10⁹–10¹¹, exact ordering by double-double re-decision,
validated against Session 40): zero violations of e_k ≤ e_k^lat in 7.9·10⁷ steps; the RPM fits of §5.2; maxima vs the Poisson model
(13 vs 18, 9 vs 11.5, 7 vs 7.5, 5 vs 5 for π/32 … π/256); Mertens offsets Σ1/p − Ein(τ) falling like ρ log(1/ρ); τ_c(ρ) = 1.637,
1.681, 1.695 for π/16, π/24, π/32; Prop. 3.3's brackets with zero violations in 1.7·10⁸ steps, and the level-2 queue ≤ 16 at π/32
to 10⁹ (past τ_c(ρ)) while the lattice-monoid queue exceeds 65,535.
**G — gaps, named:** (G1) the cluster bound K(X, m) for lattice-monoid components in short windows (needed for any sharp bound on
τ < τ_c); (G2) Conjecture 5.2 needs joint equidistribution of the phases {x/m′ mod t} over all ≈ ρ√x cofactors (Kronecker–Weyl
gives any fixed finite set when t is transcendental); (G3) Conjecture 5.4 needs G2 in large-deviation form on windows of O(1/ρ) steps.
**For Lemma B_ρ (fixed ρ, τ → ∞).** Nothing here proves it. Theorem 4.4's argument uses no positive margin (only f₀ ≥ 0: the template never clips) and closes by Gronwall with
factor exp(2(K_S + L_S)S), super-exponential in S, against error terms that vanish only as ρ → 0; at fixed ρ those terms are fixed
positive numbers (of size ρ log(1/ρ), Thm 4.4′), so it gives nothing as τ → ∞ (§4.8). The data place Lemma B's corner opposite the
scaling limit: at fixed ρ the regularity of the arrivals INCREASES with τ (queue tail rate / Poisson-queue κ = 1.05, 1.16, 1.31 at
τ = 0.6, 1.0, 2.0, and Session 40's 1.45–1.65 at π/16, π/4), because the components with period below the excursion length become
exact progressions. That corner is favorable to B and is where a proof would have to live; this unit's tools do not reach it.
**For other units.** U1/U3: on τ < τ_c(ρ) the greedy feedback is not needed for upper bounds (Thm 2.1), and the scaling-limit
dynamics is the Volterra equation f = (1 − c[f])⁺ with unique solution f₀ — a rule whose template never clips and which has analogs of Lemma 4.2(iii) (a greedy reflection) and Lemma 1.3 (a
self-similar template) inherits Theorem 4.4's proof. U7: the sub-Poisson window structure is quantitatively the random-phase model (§5.1–5.2) plus exact
periodicity of components with period below the window; Session 40's factor 1.5 belongs to this finite-ρ structure (at fixed τ
the tail-rate factor shrinks as ρ decreases: 1.27 → 1.21 at τ = 1.5, 1.17 → 1.15 at τ = 1.15; `logs/collapse.log`).

## §1. Exact structure of the sparse regime

Facts used from Session 40 [quoted: `../../free-greedy-s40/theory/NOTE.md` l. 49–68, Lemmas 1.0–1.2]: E(x) > −½ for all x;
every g-prime is a lattice point; E(p) = ½ at every g-prime p. Throughout, multisets are counted with multiplicity, so nothing below
needs t transcendental unless said.

**Lemma 1.1 (the bottom of the system)** [proved here]. (i) No composite lies in [1, p₁²); every lattice point below p₁² is a
g-prime, and −½ < E ≤ ½ on [1, p₁²). (ii) On [p₁², p₁³) the composites are exactly the products x_a·x_b (a ≤ b) of two lattice
points that lie in [p₁², p₁³), each counted once. (iii) Hence on [1, p₁³) the queue of §2(a) of the charter is driven by a pure
lattice-point count: c_k = #{(a ≤ b) : x_a x_b ∈ (x_{k−1}, x_k]} for x_k < p₁³.
*Proof.* (i) A composite is a product of ≥ 2 g-primes, each ≥ p₁, so it is ≥ p₁². With no composites, N(x) = 1 + π(x) and the rule
places a g-prime at every lattice point (Lindley: e_{k−1} = 0 and c_k = 0 for all such k, by induction from e₀ = 0). On [x_k, x_{k+1})
E(x) = ½ − ρ(x − x_k) ∈ (−½, ½]; on [1, x₁), E = −ρ(x − 1) ∈ (−½, 0]. (ii) A composite n < p₁³ has exactly two prime factors (three
would give n ≥ p₁³); writing n = pq with p ≤ q, q = n/p ≤ n/p₁ < p₁², so q is a lattice point, and p ≤ q too. Conversely, if
x_a ≤ x_b and x_a x_b < p₁³ then x_b < p₁³/x_a ≤ p₁², so x_a, x_b are g-primes by (i) and their product is a composite. (iii) follows. ∎
In the variable τ = ρ log x the bottom ends at τ = 2ρ log p₁ and the pure two-fold range at 3ρ log p₁; both → 0 as ρ → 0
(ρ log p₁ = ρ log(1/(2ρ)) + O(ρ)). So "x ≤ e^{c/ρ}" is NOT a two-or-three-fold range: products of up to ≈ c/(ρ log(1/2ρ)) lattice
points occur there. What is true (§2) is that they are all products of LATTICE points, which is what makes the range tractable.

**Lemma 1.2 (E against the Lindley queue)** [proved here]. With e₀ := 0, e_k = max(e_{k−1} + c_k − 1, 0) as in the charter:
(i) E(x_k) = e_k + ½; (ii) for x ∈ [x_k, x_{k+1}): E(x) = e_k + ½ + C(x_k, x] − ρ(x − x_k) ≤ e_{k+1} + 3/2; (iii) Lindley's formula
e_k = max_{0≤j≤k} Σ_{i=j+1}^{k} (c_i − 1) (empty sum = 0). Hence max_{k≤K} e_k + ½ ≤ sup_{x < x_{K+1}} E(x) ≤ max_{k≤K+1} e_k + 3/2.
*Proof.* (i) is the definition e_k = N(x_k) − (k + 1) with T(x_k) = k + ½. (ii) N grows only by composites on (x_k, x_{k+1}), and
C(x_k, x] ≤ c_{k+1} ≤ e_{k+1} − e_k + 1 (from e_{k+1} ≥ e_k + c_{k+1} − 1). (iii) Induction: if e_{k−1} = max_{j≤k−1} Σ_{j+1}^{k−1},
then e_{k−1} + c_k − 1 = max_{j≤k−1} Σ_{j+1}^{k}, and the outer max with 0 is the term j = k. ∎ (Also: g-prime at x_k ⟺ e_{k−1} +
c_k = 0, and #g-primes among steps j+1..k = (k − j) − Σc_i + e_k − e_j: every step is a g-prime or serves one composite.)

**Lemma 1.3 (the template is exactly self-similar in τ)** [proved here]. The continuous template of S8(ρ) has prime density
(1 − u^{−ρ})/log u per unit length [quoted: Session-40 NOTE l. 96–98, Lemma 1.5]; per lattice step (length t = 1/ρ) this is
(1 − e^{−τ})/τ = f₀(τ), the same function for every ρ. Equivalently, with s := ρ log u, the template prime measure Σ_p p^{−1}δ_{ρ log p}
becomes f₀(s)ds and the template integer measure becomes δ₀ + ds; the identity exp*(f₀ds) = δ₀ + ds (additive convolution
exponential on [0, ∞)) is the Laplace identity exp(log(1 + 1/z)) = 1 + 1/z, since ∫₀^∞ e^{−zs}f₀(s)ds = log(1 + 1/z) (both sides have
z-derivative 1/(z+1) − 1/z and vanish at z = ∞). So the template's composite rate per step is λ₀(τ) = 1 − f₀(τ) = τ/2 − τ²/6 + …,
independent of ρ. *Proof.* Multiply the density by t and write u^{−ρ} = e^{−τ}. ∎

## §2. Domination by the feedback-free lattice queue, and the explicit bound

Let G^lat be the monoid of all finite multisets of lattice points (the system whose g-primes are ALL lattice points), c_k^lat the
number of its composites (multisets of ≥ 2 lattice points) with product in (x_{k−1}, x_k], and e_k^lat := max(e_{k−1}^lat + c_k^lat − 1, 0),
e₀^lat := 0. This queue is feedback-free: a fixed function of t alone, involving no greedy decision.

**Theorem 2.1 (pathwise domination)** [proved here]. For every k: c_k ≤ c_k^lat and e_k ≤ e_k^lat. Hence
sup_{1≤x<x_{K+1}} E(x) ≤ max_{k≤K+1} e_k^lat + 3/2.
*Proof.* The g-primes are lattice points. A composite of S8 is a multiset of ≥ 2 g-primes; read as a multiset of lattice points it is
a composite of G^lat with the same product, and distinct multisets stay distinct. So C(I) ≤ C^lat(I) for every interval I, in
particular c_k ≤ c_k^lat (same step convention (x_{k−1}, x_k] on both sides). Lindley's map (e, c) ↦ max(e + c − 1, 0) is
nondecreasing in both arguments; induction from e₀ = e₀^lat = 0. The last sentence is Lemma 1.2. ∎
[computed: `verify/s8sp.c` modes 1 and 0 run in lockstep through an e-dump, `verify/run_main.sh`, logs `logs/r*_m0_1e9.tsv` columns
viol/cmpd] zero violations of e_k ≤ e_k^lat in 24,543,693 (π/128), 49,087,385 (π/64) and 5,603,833 (π/32, until e^lat exceeds
65,535) consecutive steps to 10⁹. **Consequence: on any range where e^lat is small, upper bounds for S8 are a pure lattice-point
problem; the greedy feedback is not needed.**

**Lemma 2.2 (component count)** [proved here]. For z ≥ 1 put S(z) := Σ 1/m′ and Q(z) := #{M′}, both over nonempty multisets M′ of
lattice points with m′·P⁺(M′) ≤ z (m′ = product of M′, P⁺(M′) = its largest element). For every window W = (x_j, x_k] of m = k − j
steps: C^lat(W) ≤ m·S(x_k) + Q(x_k).
*Proof.* A lattice composite M with product in W has a largest element P; M ↦ (M′ := M minus one copy of P, P) is injective, M′ ≠ ∅
and P⁺(M′) ≤ P. For fixed M′ the admissible P are lattice points in (x_j/m′, x_k/m′], an interval of length mt/m′, so there are at
most m/m′ + 1 of them (spacing t), and none unless m′P⁺(M′) ≤ m′P ≤ x_k. Sum over M′. ∎
Each M′ is a "component": its multiples m′·P (P ≥ P⁺(M′)) form an arithmetic progression of step exactly m′ lattice steps, with
long-run rate 1/m′ per step; S is the total rate, Q the number of components. The "+1" is the only loss.

**Theorem 2.3 (explicit bound on the sparse range)** [proved here]. If S(x_{K+1}) ≤ 1, then
  sup_{1≤x<x_{K+1}} E(x) ≤ 3/2 + Q(x_{K+1}).
*Proof.* By Lemma 1.2(iii) for the lattice queue, e_k^lat = max_{j≤k}(C^lat(x_j, x_k] − (k − j)) ≤ max_{j≤k}(k − j)(S(x_k) − 1) + Q(x_k)
≤ Q(x_k), because S and Q are nondecreasing and S(x_k) ≤ 1. Then Theorem 2.1. ∎
*Elementary size of Q* [proved here]. Every M′ counted in Q(z) has m′ ≤ z/P⁺(M′) ≤ z/p₁, and also m′ ≤ z^{j/(j+1)} if |M′| = j
(as P⁺(M′) ≥ m′^{1/j}). Counting multisets of j lattice points with product ≤ Y by their largest element gives the recursion
N_j(Y) ≤ ρY·H_{j−1}(Y) + N_{j−1}(Y/p₁), H_n(Y) := Σ_{|M|=n, m≤Y} 1/m ≤ h_n(w) (complete homogeneous symmetric function of
w_a = 1/x_a, x_a ≤ Y), N₀ = 1. Since Σ_n h_n(w) = Π_a(1 − w_a)^{−1} ≤ exp(σ_Y/(1 − 1/p₁)), σ_Y := Σ_{x_a≤Y} 1/x_a, this unrolls to
  N^lat(Y) := Σ_j N_j(Y) ≤ 2ρY·e^{2σ_Y} + log Y/log p₁,  hence  Q(z) ≤ N^lat(z/p₁) ≤ 4ρ²z·e^{2σ_z} + log z/log p₁,
using p₁ ≥ 1/(2ρ). And σ_z = ρ(ψ(A + ½ + ρ) − ψ(½ + ρ)), A = #{a : x_a ≤ z}, so σ_z = τ_z + ρ(log ρ − ψ(½ + ρ)) + O(ρ/A), with
−ψ(½) = 1.9635 [ψ = digamma]. **So on the sparse range E(x) ≤ 3/2 + 4ρ²(x + t)·e^{2τ+4ρ} + τ/(ρ log p₁): the integer error is at most
O(ρ) times the number of steps, explicitly.** The exact Q is far smaller (table below): its j-element part is ≈ c_j ρ^j z^{j/(j+1)}
(Q₁(z) = #{a : x_a² ≤ z} ≤ ρ√z + 1), so for small τ the bound is ≈ ρ√x. On the pure two-fold range [1, p₁³) of Lemma 1.1 only one-element cofactors occur
(m′P⁺(M′) ≥ p₁³ when |M′| ≥ 2) and S < 1, so **E(x) ≤ 2 + ρ√(x + t) for x < p₁³** [proved here].

*Theorem 2.3 in numbers* [computed: `verify/qs.c` (exact enumeration of S, Q), logs `logs/qs_*.log`, `logs/tauc.log`; measured
sup E from `logs/r*_m0_*.tsv`; the S8 runs re-decide every composite within 10⁻⁵ steps of a lattice point in double-double: 2,706–7,354
re-decisions per run, 8–38 flips of the double-precision step, 0 unresolved]:

| ρ | S ≤ 1 holds for x ≤ | Q(10⁸) | Q(10⁹) | Q(10¹⁰) | sup_{x≤10⁸} E | sup_{x≤10⁹} E | sup_{x≤10¹⁰} E |
|---|---|---|---|---|---|---|---|
| π/32 | 3.16·10⁷ (τ = 1.695) | (S > 1) | — | — | 9.86 | 13.22 | — |
| π/64 | > 10¹² (S(10¹²) = 0.747) | 1,447 | 6,385 | 29,631 | 6.19 | 8.00 | 10.48 |
| π/128 | > 10¹² (S(10¹²) = 0.320) | 446 | 1,778 | 7,381 | 4.71 | 5.55 | 7.09 |
| π/256 | > 10¹² (S(10¹²) = 0.144) | 170 | 612 | 2,318 | 3.27 | 4.22 | 5.18 |

(π/32: Q(10⁷) = 1,279 against sup_{x≤10⁷} E = 8.93.) The theorem is correct and explicit, and it is loose by a factor 10²–10³:
all of the loss is the "+1 per component" of Lemma 2.2, i.e. the trivial bound for the number of components (cofactors M′) whose
progression has a point in a given short window. That is the step to improve inside the sparse range (§3.2).

## §3. What fails beyond the sparse range

**Proposition 3.1 (the lattice monoid's load in the scaling limit)** [proved here]. Uniformly for τ in compact subsets of [0, ∞),
S_ρ(e^{τ/ρ}) → Λ(τ) := Σ_{j≥1} τ^j/(j!(j+1)!) = I₁(2√τ)/√τ − 1 as ρ → 0; Λ is increasing and Λ(τ_c) = 1 at
**τ_c = 1.54609037074481** [computed: `verify/tauc.py`, mpmath, `logs/tauc.log`]. Λ(τ) = τ/2 + τ²/12 + τ³/144 + …: the j-th term is the
rate of products of j + 1 lattice points.
*Proof.* Let λ_ρ := Σ_a x_a^{−1}δ_{ρ log x_a} (the lattice in the variable s = ρ log u, weight 1/x_a). For 0 ≤ v₁ < v₂ ≤ V,
λ_ρ((v₁, v₂]) = ρΣ_{A₁<a≤A₂} 1/(a + δ) with A_i = ρe^{v_i/ρ} + O(1), which is v₂ − v₁ + O(ρ log(1/ρ)) uniformly (digamma, as in §2); so
λ_ρ → Lebesgue measure vaguely on [0, ∞), with λ_ρ([0, v]) ≤ v + 2ρ. In S_ρ, the j-element cofactors M′ are the points
u ∈ [0, ∞)^j (u_i = ρ log of the elements) of R_j(τ) := {Σu_i + max u_i ≤ τ}, weighted by e^{−Σu_i/ρ} = 1/m′. Ordered j-tuples with
distinct entries count each multiset j! times; multisets with a repeated element carry total weight ≤ (Σ_a x_a^{−2})·h_{j−2}(w)
(w_a = 1/x_a for x_a ≤ e^{τ/ρ}, h_n = complete homogeneous symmetric function, Σ_a x_a^{−2} = ρ²ψ′(½ + ρ) ≤ 5ρ²). Cauchy's bound on
Σ_n h_n ζ^n = Π_a(1 − w_aζ)^{−1} ≤ exp(σζ/(1 − ζ/p₁)), σ := Σw ≤ τ + 2ρ, at ζ = n/(2σ) when n ≤ σp₁ and ζ = p₁/2 when n > σp₁, gives
h_n ≤ η_n := (2eσ/n)^n resp. (4eρ)^n, summable uniformly for ρ ≤ 1/16. So S_j = (1/j!)λ_ρ^{⊗j}(R_j(τ)) + O(ρ²η_{j−2}). R_j(τ) is compact with Lebesgue-null
boundary, so λ_ρ^{⊗j}(R_j(τ)) → vol R_j(τ). Volume: the simplex {v ∈ [0,∞)^{j+1} : Σv = τ}, projected to its first j coordinates, is
{u : Σu ≤ τ}, of volume τ^j/j!; the part where v_{j+1} is the largest coordinate projects onto R_j(τ) and carries 1/(j+1) of it (the
simplex is symmetric in its j + 1 coordinates; ties are null). So vol R_j(τ) = τ^j/(j+1)!, and S_j → τ^j/(j!(j+1)!). Dominated
convergence in j: S_j ≤ σ^j/j! + 5ρ²η_{j−2}, summable. Uniformity: S_ρ is nondecreasing in z and
Λ is continuous (Pólya's argument). The Bessel form is the series of I₁. ∎
*Finite ρ* [computed, `logs/tauc.log`]: S_ρ = 1 at τ = 1.637 (π/16), 1.681 (π/24), 1.695 (π/32); the offset from τ_c comes from
Σ_{a≤A} 1/(a+δ) = log A − ψ(½ + ρ) + o(1) and is O(ρ log(1/ρ)), so the approach to τ_c is slow and not monotone in ρ.
Direct check [computed, `logs/lag1_and_S.log`]: S_ρ(z) − Λ(ρ log z) = −0.035, −0.059, −0.103, −0.181 at z = 10¹² for π/256, π/128,
π/64, π/32, i.e. ≈ −0.65·ρ log(1/ρ).

**3.2 The exact failing steps.**
(F1) *Beyond τ_c(ρ): the domination of Theorem 2.1 is the step that fails.* There the comparison queue has arrival rate Λ(τ) > 1 per
step and grows linearly [computed, `logs/r32_m1_1e9.tsv`]: max e^lat = 26 to 10⁷ (τ = 1.58, rate 0.892), 368,982 to 10⁸ (τ = 1.81, rate
1.072), 20,032,408 to 10⁹ (rate 1.264), while S8's own queue stays ≤ 13 there. The information Theorem 2.1 throws away is exactly the
set of BUSY lattice points (lattice points that are not g-primes, a fraction λ₀(τ′) ≈ τ′/2 of the steps at scale τ′): the lattice monoid
overcounts S8's arrival rate by Λ(τ) − λ₀(τ) = τ²/4 − 5τ³/144 + O(τ⁴), the rate of lattice products with at least one busy factor.
No argument that forgets which lattice points are busy can pass τ_c(ρ). To pass it one needs a LOWER bound for the busy set at scales
≤ x/p₁, i.e. a lower bound for composites there, i.e. an upper bound for primes further down: the alternating scheme of Prop. 3.3, of
which Theorem 2.1 is the zeroth term.
**Proposition 3.3 (pathwise alternating brackets)** [proved here]. Put P⁽⁰⁾ := all lattice points; given P⁽ʲ⁾, let C⁽ʲ⁾ be the
multiset products of ≥ 2 elements of P⁽ʲ⁾, e⁽ʲ⁾ its Lindley queue, and P⁽ʲ⁺¹⁾ := {x_k : e⁽ʲ⁾_{k−1} = 0 and c⁽ʲ⁾_k = 0} (its idle steps).
Then P⁽¹⁾ ⊆ P⁽³⁾ ⊆ … ⊆ P ⊆ … ⊆ P⁽²⁾ ⊆ P⁽⁰⁾, e⁽²ⁱ⁺¹⁾ ≤ e ≤ e⁽²ⁱ⁾ for all steps, and P⁽ʲ⁾ = P on [1, p₁^{j+2}). Every P⁽ʲ⁾ is a function of
t alone, so E ≤ e⁽²ⁱ⁾ + 3/2 bounds S8 by a feedback-free computable queue at every even level.
*Proof.* Let Φ(P′) be the idle set of the queue driven by the products of P′. If P′ ⊆ P″ then C′ ⊆ C″ (as multisets),
c′_k ≤ c″_k, and (Lindley is monotone) e′ ≤ e″, so Φ(P″) ⊆ Φ(P′): Φ is antitone. P⁽ʲ⁺¹⁾ = Φ(P⁽ʲ⁾), and S8's own g-prime set is the
fixed point P = Φ(P) (Lemma 1.2: a g-prime sits at x_k iff e_{k−1} + c_k = 0). From P ⊆ P⁽⁰⁾: P⁽¹⁾ = Φ(P⁽⁰⁾) ⊆ Φ(P) = P, then
P = Φ(P) ⊆ Φ(P⁽¹⁾) = P⁽²⁾, and so on. From P⁽²⁾ ⊆ P⁽⁰⁾: P⁽¹⁾ ⊆ P⁽³⁾, then P⁽⁴⁾ ⊆ P⁽²⁾, and so on. The queue inequalities follow from the
set inclusions by the same monotonicity. Exactness at the bottom:
P⁽⁰⁾ = P below p₁² (Lemma 1.1); if P⁽ʲ⁾ = P below p₁^{j+2}, then products below p₁^{j+3} have all factors below p₁^{j+2}, so C⁽ʲ⁾ = C,
e⁽ʲ⁾ = e and P⁽ʲ⁺¹⁾ = P below p₁^{j+3}. ∎
*What each level buys, in the scaling limit* [computed: `verify/brackets.py`, `logs/brackets.log`; grid h = 0.002 on [0, 12], check
c[f₀] = 1 − f₀ to 3·10⁻⁷]. Macroscopically P⁽ʲ⁾ has density fʲ := Tʲ(1) with the antitone map T(f) := (1 − c[f])⁺, c[f] := density of
exp*(f ds) − δ₀ − f ds; f^{2i} ≥ f₀ ≥ f^{2i+1}. The even-level load c[f^{2i}] stays below 1 up to τ = 1.548, 2.250, 2.978, 3.718, 4.460
for i = 0, 1, 2, 3, 4: each further pair of levels gains ≈ 0.73 in τ. So any fixed number of levels covers only a bounded τ-range,
and every level at finite ρ still pays a "+1 per component" count of its own; covering all τ needs unboundedly many levels, which
is what the Gronwall argument of Theorem 4.4 does in the limit.
*Prop. 3.3 at finite ρ* [computed: `verify/run_brackets.sh`, `check_brackets.py`, mode 2 of `s8sp.c` (generators read from the
previous level's idle set), log `logs/brackets_finite.log`; ρ = π/128, π/64, π/32 to 10⁹]: zero violations of P⁽¹⁾ ⊆ P ⊆ P⁽²⁾,
P⁽¹⁾ ⊆ P⁽³⁾ ⊆ P⁽²⁾ and e⁽¹⁾, e⁽³⁾ ≤ e ≤ e⁽²⁾ ≤ e⁽⁰⁾ in 2.5·10⁷, 4.9·10⁷, 9.8·10⁷ steps; P⁽ʲ⁾ first departs from P just above p₁^{j+2}
(π/128: 1.0044·10⁴, 2.147·10⁵, 4.589·10⁶ against 9.76·10³, 2.09·10⁵, 4.46·10⁶). **Level 2 passes τ_c:** for π/32 (τ_c(ρ) = 1.695)

| x ≤ (τ) | 10⁶ (1.36) | 10⁷ (1.58) | 10⁸ (1.81) | 10⁹ (2.03) |
|---|---|---|---|---|
| max e⁽⁰⁾ (lattice monoid) | 12 | 26 | > 65,535 | > 65,535 |
| max e⁽²⁾ (upper bracket) | 6 | 9 | 11 | 16 |
| max e (S8) | 5 | 8 | 9 | 12 |
| max e⁽¹⁾, e⁽³⁾ (lower brackets) | 5, 5 | 5, 8 | 6, 9 | 7, 12 |

so the feedback-free computable queue e⁽²⁾ bounds S8 pathwise well past τ_c(ρ), as the limit computation predicts (level-2 load < 1
up to τ ≈ 2.25 + finite-ρ offset). An explicit analytic bound at level 2 would need window counts of P⁽²⁾ (Lemma 2.2 with P⁽²⁾ in
place of the lattice), which is the same kind of problem one level up.
(F2) *Inside the range, the step that makes the bound weak is the "+1 per component" of Lemma 2.2.* Precisely: the bound needs
K(X, m) := max over windows W of m steps with right end ≤ X of #{M′ : the progression m′·P, P ≥ P⁺(M′), has a point in W}, and the
only available bound is K ≤ Q(X). For one-element cofactors this is the count #{(a ≤ b) : (a + δ)(b + δ) ∈ [Y, Y + mρ]}, Y = ρ²y: lattice
points of the shifted lattice (ℤ + δ)² in a hyperbolic shell of width mρ → 0 — the shifted divisor problem in very short intervals.
Integer-points-near-a-curve methods (second divided differences) give O(Y^{1/3+ε}) for it [recalled, unverified; not used]; the truth
is far smaller: the whole feedback-free queue has max e^lat = 7 to 10¹⁰ for π/128 (Q = 7,381) and 13 to 10¹⁰ for π/64 (Q = 29,631)
[computed, `logs/r128_m1_1e10.tsv`, `logs/r64_m1_1e10.tsv`].
**Proposition 3.2 (what a cluster bound would give)** [proved here]. If C^lat(W) ≤ m·S(x_k) + K for every window W = (x_j, x_k] with
x_k ≤ X and S(X) ≤ 1, then sup_{x<X} E(x) ≤ K + 3/2. (Same proof as Theorem 2.3.) So on τ < τ_c every Lemma B-type bound for S8 is
implied by a cluster bound for the feedback-free lattice monoid; a polylogarithmic K would give polylogarithmic E there.
(F3) *"Two- or three-fold" is true only at the very bottom.* All composites are two-fold only on [p₁², p₁³) (Lemma 1.1), i.e.
τ < 3ρ log p₁ → 0. At τ = c the cofactor table has non-empty classes up to |M′| = 8 already at 10⁹ for π/32 [`logs/qs_32.log`]: products
of up to ≈ c/(ρ log(1/2ρ)) lattice points occur. Their share of the load is small for small τ (Λ(τ) − τ/2 = τ²/12 + …) but not zero, and
in Lemma 2.2 every one of them costs its own "+1".

## §4. The scaling limit τ = ρ log x: macroscopic law

Throughout, ρ → 0 along any sequence in (0, 1/16], S > 0 is fixed, and "uniformly" means uniformly in 1 ≤ y < x ≤ e^{S/ρ}.
Template counts: Π₀(y, x] := ∫_{max(y,1)}^x ρf₀(ρ log u)du (primes), Λ₀(y, x] := ρ(x − y) − Π₀(y, x] (composites). Additive measures in
the variable v = ρ log u: μ_ρ := Σ_p p^{−1}δ_{ρ log p}, μ̃_ρ := Σ_p Σ_{k≥1} k^{−1}p^{−k}δ_{kρ log p}, ν_ρ := Σ_{n∈G} n^{−1}δ_{ρ log n}.

**Theorem 4.1 (below τ_c)** [proved here]. For 0 < S < τ_c there are ρ₁(S) > 0 and C(S) < ∞ such that for ρ < ρ₁(S):
E(x) ≤ 3/2 + C(S)ρ²(x + t) + S/(ρ log p₁) for all 1 ≤ x ≤ e^{S/ρ}. So E(x)/(ρx) = O(ρ) + O(1/(ρ²x log(1/ρ))) there.
*Proof.* By Prop. 3.1, S_ρ(e^{S/ρ} + 2t) → Λ(S) < 1, so S_ρ ≤ 1 on the range for small ρ. Theorem 2.3 gives E(x) ≤ 3/2 + Q(x + t),
and §2 gives Q(z) ≤ 4ρ²z·e^{2σ_z} + log z/log p₁ with σ_z ≤ S + 2ρ. ∎

**Lemma 4.2 (exact identities)** [proved here]. For 1 ≤ y < x: (i) π(y, x] + C(y, x] = ρ(x − y) + E(x) − E(y);
(ii) C(y, x] = Σ_{M′} π(J_{M′}), over nonempty multisets M′ of g-primes, J_{M′} := (y/m′, x/m′] ∩ [P⁺(M′), ∞), and every element of
every M′ that contributes is ≤ √x; (iii) E(x) ≤ ½ + sup_{1≤y<x}(C(y, x] − ρ(x − y))⁺.
*Proof.* (i) N(u) = ρ(u − 1) + 1 + E(u) and N(x) − N(y) = π(y, x] + C(y, x]. (ii) n ↦ (M′, P⁺(n)) as in Lemma 2.2 (now for g-primes);
if Q ∈ M′ then Q² ≤ Q·P⁺(n) ≤ n ≤ x. (iii) For x < p₁, E(x) ≤ 0. Otherwise let y be the largest g-prime ≤ x; E(y) = ½ [quoted:
Session-40 NOTE l. 49–50, 1.0(ii)] and π(y, x] = 0, so (i) gives E(x) = ½ + C(y, x] − ρ(x − y). ∎

**Lemma 4.3 (integer regularity gives the prime law, vaguely)** [proved here]. Suppose E(x) ≤ ε_ρρx + K for 1 ≤ x ≤ e^{S/ρ},
with ε_ρ → 0 and K fixed. Then for every interval I ⊂ [0, S]: μ_ρ(I) → ∫_I f₀(v)dv; in particular Σ_{p ≤ x} 1/p → Ein(τ) :=
∫₀^τ (1 − e^{−v})/v dv uniformly for τ = ρ log x ∈ [0, S].
*Proof.* (a) ν_ρ = exp*(μ̃_ρ) (additive convolution exponential on [0, ∞)): the g-integers are the free commutative monoid on the
g-primes, so ν_ρ = ⊛_p Σ_{k≥0} p^{−k}δ_{kρ log p} = ⊛_p exp*(Σ_{k≥1} k^{−1}p^{−k}δ_{kρ log p}), using Σ_{k≥0}y^k = exp(Σ_{k≥1}y^k/k) in the
convolution algebra (y = p^{−1}δ_{ρ log p}). On [0, S] all sums are finite, since every term is supported on [s₁, ∞), s₁ := ρ log p₁.
(b) For I = (v₁, v₂] with a = e^{v₁/ρ}, b = e^{v₂/ρ}: ν_ρ(I) = ∫_{(a,b]}dN(u)/u = ρ log(b/a) + E(b)/b − E(a)/a + ∫_a^b E(u)u^{−2}du
(insert N = ρ(u − 1) + 1 + E; the other terms cancel). With −½ < E ≤ ερu + K and a ≥ p₁ ≥ 1/(2ρ) when v₁ ≥ s₁ (and ν_ρ puts no
mass on (0, s₁)), this gives |ν_ρ(I) − |I|| ≤ ε_ρ|I| + b_ρ for every I ⊂ (0, S], b_ρ := (4K + 6)ρ log(1/ρ) → 0.
(c) σ_ρ := ν_ρ − δ₀ satisfies σ_ρ(I) ≤ 2|I| + b_ρ. Let U be the uniform probability on [0, b_ρ]; σ_ρ * U has density
σ_ρ([w − b_ρ, w])/b_ρ ≤ 3, so σ_ρ^{*n}([0, S]) ≤ (σ_ρ*U)^{*n}([0, S + nb_ρ]) ≤ 3^n(S + nb_ρ)^n/n!. On [0, S] only n ≤ S/s₁ occur and
nb_ρ ≤ S(4K + 6)log(1/ρ)/log(1/(2ρ)) ≤ (8K + 12)S, so Σ_{n>n₀} σ_ρ^{*n}([0, S])/n → 0 as n₀ → ∞ uniformly in ρ.
(d) σ_ρ → Lebesgue measure weakly on [0, S] (by (b), on every subinterval; nothing is assumed beyond S), with uniform local bounds; convolution is jointly continuous for vague convergence of
such measures on [0, ∞) (σ_ρ^{*n} on [0, S] depends only on σ_ρ restricted to [0, S], and products of these restrictions converge weakly on [0, S]², and u + v ≤ S is a compact condition), so
σ_ρ^{*n} → (v^{n−1}/(n − 1)!)dv for each n, also on intervals (the limit is absolutely continuous).
(e) μ̃_ρ = Σ_{n≥1}((−1)^{n+1}/n)σ_ρ^{*n} on [0, S] (convolution logarithm; a finite sum there). By (c)–(d), μ̃_ρ(I) →
∫_I Σ_{n≥1}(−1)^{n+1}v^{n−1}/n! dv = ∫_I f₀. Finally μ̃_ρ − μ_ρ has total mass ≤ 2Σ_a x_a^{−2} ≤ 10ρ² (prime powers). ∎
*Corollary* [proved here]: below τ_c (Theorem 4.1 gives the hypothesis with ε_ρ = O(ρ)), the Mertens-type law Σ_{p≤x} 1/p →
Ein(ρ log x) holds uniformly on τ ≤ S < τ_c. For the lattice itself Σ_{x_a≤x} 1/x_a → τ; Ein(τ) = τ − τ²/4 + … records the busy steps.
**Theorem 4.4 (macroscopic law in the scaling limit, every τ)** [proved here; second read `read-T44.md`: AGREES-WITH-CORRECTIONS,
one fillable gap (Step 3's local mass bound) filled there, all corrections applied]. For every S > 0, as ρ → 0,
  sup_{1≤y<x≤e^{S/ρ}} |π(y, x] − Π₀(y, x]|/(ρx) → 0,  sup |C(y, x] − Λ₀(y, x]|/(ρx) → 0,  sup_{x≤e^{S/ρ}} (E(x) − ½)/(ρx) → 0
(the first two over x ≥ p₁²). So at every τ the queue's arrival intensity per step is λ₀(τ) = 1 − (1 − e^{−τ})/τ in every window of
fixed relative length (y = x(1 − η)), the g-primes fill the fraction f₀(τ), the queue content is o(ρx), and by Lemma 4.3
Σ_{p≤x} 1/p → Ein(τ) for every τ — no restriction to τ < τ_c.
*Proof.* Put α_ρ(v) := sup{|π(y, x] − Π₀(y, x]|/(ρx) : 1 ≤ y < x, p₁² ≤ x ≤ e^{v/ρ}}, β_ρ(v) the same with C, Λ₀ (sup ∅ := 0, i.e. both vanish while e^{v/ρ} < p₁²); both are
nondecreasing in v and bounded (α_ρ ≤ 2 since π(y, x] ≤ ρ(x − y) + 1; β_ρ ≤ Λ(S) + 2 by Theorem 2.1's C ≤ C^lat and Lemma 2.2).
Let A, B be their limsups as ρ → 0.
*Step 1 (queue).* Lemma 4.2(iii) and Λ₀(y, x] ≤ ρ(x − y) give −½ < E(x) ≤ ½ + β_ρ(v)ρx for x ≤ e^{v/ρ}.
*Step 2 (primes).* Lemma 4.2(i) with ρ(x − y) = Π₀ + Λ₀ gives π − Π₀ = (Λ₀ − C) + E(x) − E(y), so α_ρ(v) ≤ 2β_ρ(v) + 4ρ (as
1/(ρp₁²) ≤ 4ρ). Hence A ≤ 2B.
*Step 3 (composites).* By Lemma 4.2(ii), C(y, x] − Λ₀(y, x] = T₁ + T₂ with T₁ := Σ_{M′}(π(J_{M′}) − Π₀(J_{M′})) and
T₂ := Σ_{M′}Π₀(J_{M′}) − Λ₀(y, x]. Each J_{M′} is a window with right end x/m′. If x/m′ ≥ p₁² its error is ≤ α_ρ(v − u)ρx/m′,
u := ρ log m′; if x/m′ < p₁², all lattice points in J are g-primes (Lemma 1.1) and the error is ≤ ρ(x/m′)·2s₁ + 1. With
κ_ρ := Σ_{M′: m′P⁺(M′)≤x} δ_{ρ log m′}/m′ and Q(x) ≤ 4ρ²x e^{2S+4ρ} + log x/log p₁ ≤ ρx(4ρe^{2S+4ρ} + 8ρ) for x ≥ p₁² (§2):
  |T₁| ≤ ρx∫α_ρ(v − u)dκ_ρ(u) + 2s₁ρx·κ_ρ([0, v]) + Q(x).
κ_ρ is dominated by the lattice multiset measure exp*(λ̃_ρ) − δ₀, λ̃_ρ := Σ_aΣ_{k≥1}k^{−1}x_a^{−k}δ_{kρ log x_a} (Euler product;
exp*(λ_ρ) alone gives a multiset with multiplicities (e_a) only 1/Πe_a! of its weight), and λ̃_ρ(I) ≤ |I| + 2ρ + Σ_a x_a^{−2} ≤ |I| + 3ρ
for every interval I. With U uniform on [0, 2ρ], λ̃_ρ * U has density ≤ 3; since ν(I) ≤ (ν * U^{*n})(I + [0, 2nρ]) for every measure
ν, λ̃_ρ^{*n}(I) ≤ 3^n(|I| + 2nρ)(2v)^{n−1}/(n − 1)! for I ⊂ [0, v] (only n ≤ v/s₁ occur, and then 2nρ ≤ 2v/log p₁ ≤ v). Dividing by n!
and summing over n: κ_ρ(I) ≤ 6I₀(2√(6S))(|I| + ρ) ≤ K_S(|I| + ρ), K_S := 4e^{2S+2} (6I₀(2√(6S)) ≤ 0.7·4e^{2S+2} for all S > 0)
[this bound is the second reader's fill of a gap in the first version; `read-T44.md` §2]. As α_ρ is nondecreasing, summing over a partition of [0, v]
into intervals of length δ_ρ := (ρ log(1/ρ))^{1/2} gives |T₁| ≤ ρx[K_S∫₀^v α_ρ(w)dw + o(1)].
For T₂ use Lemma 4.6 below: |T₂| ≤ ρx[L_S·D_ρ(v/2) + O(ρ)], D_ρ(w) := sup_{I⊂[0,w]} |μ_ρ(I) − ∫_I f₀|, L_S := 4e^{S+2}.
*Step 4 (discrepancy from window errors).* For I = (w₁, w₂] ⊂ [2s₁, w], a = e^{w₁/ρ}, b = e^{w₂/ρ}: μ_ρ(I) − ∫_I f₀ =
Δ(b)/b − Δ(a)/a + ∫_a^b Δ(u)u^{−2}du with Δ(u) := π(a, u] − Π₀(a, u] (integration by parts on dπ − dΠ₀), and |Δ(u)| ≤ α_ρ(ρ log u)ρu;
so |μ_ρ(I) − ∫_I f₀| ≤ 2ρα_ρ(w) + ∫_{w₁}^{w₂}α_ρ. On [0, 2s₁) every lattice point is a g-prime (p₁² itself can be a busy lattice point — for integer t ≡ 2 mod 4, e.g. ρ = 1/18,
p₁² = x₆ carries p₁·p₁ — and its mass 1/p₁² ≤ 4ρ² is absorbed) and the discrepancy is ≤ λ_ρ-vs-Lebesgue
error + 2s₁·(1 − f₀(2s₁)) = O(ρ log(1/ρ)). Hence D_ρ(w) ≤ ∫₀^w α_ρ + o(1).
*Step 5 (closing).* Steps 3–4 give β_ρ(v) ≤ (K_S + L_S)∫₀^v α_ρ + o(1); with Step 2 and reverse Fatou (0 ≤ α_ρ ≤ 2 on [0, S]):
A(v) ≤ 2(K_S + L_S)∫₀^v A(w)dw, A nondecreasing and bounded. Iterating from A ≤ 2: A(v) ≤ 2(2(K_S + L_S)v)^n/n! for every n, so A ≡ 0 on [0, S]. So A ≡ 0, B ≤ (K_S + L_S)∫A ≡ 0,
and Step 1 gives (E(x) − ½)/(ρx) ≤ β_ρ(S) → 0. ∎
**Lemma 4.6 (the cofactor functional is Lipschitz in the prime discrepancy)** [proved here]. For p₁² ≤ x ≤ e^{S/ρ}, v = ρ log x,
y < x: |Σ_{M′}Π₀(J_{M′}) − Λ₀(y, x]| ≤ ρx[L_S·D_ρ(v/2) + O(ρ)].
*Proof.* (a) Closed form. With L := log(x/y) and u = ρ log m′, σ = ρ log P⁺(M′), substituting w = x e^{−u/ρ−θ}:
Π₀(J_{M′}) = (ρx/m′)·g(u, σ), g(u, σ) := ∫₀^{min(L, (v−u−σ)/ρ)} f₀(v − u − ρθ)e^{−θ}dθ ∈ [0, 1] (g := 0 if v − u − σ < 0).
Replacing f₀(v − u − ρθ) by f₀(v − u) changes g by ≤ ρ sup|f₀′| ≤ ρ/2; so g = g₁ + O(ρ), g₁(u, σ) := f₀(v − u)·h(v − u − σ),
h(r) := 1 − e^{−min(L, r/ρ)} nondecreasing on [0, ∞), h := 0 on (−∞, 0).
(b) Multisets. Every element of a contributing M′ lies in [0, v/2] (Lemma 4.2(ii)). Σ_{M′}(1/m′)φ(M′) = Σ_{j≥1}(1/j!)∫φ dμ_ρ^{⊗j}
(μ_ρ restricted to [0, v/2]) up to repeated-element terms of total weight ≤ 5ρ²Σ_n η_n = O(ρ²) (as in Prop. 3.1), for any φ ∈ [0, 1].
The template satisfies the same decomposition by the largest element with μ₀ := f₀dv on [0, v/2] and no repetition terms (ties are
null), and Λ₀(y, x] = ρx Σ_j (1/j!)∫g(Σu_i, max u_i)dμ₀^{⊗j}: both sides count the products m′·P with P ≥ max(M′) in (y, x] for the
continuous prime measure (the largest-element decomposition of exp*(μ₀) − δ₀ − μ₀).
(c) Sections. φ(s) := f₀(v − s) is nondecreasing on [0, v] with values in [f₀(v), 1], so φ(s) = φ(0) + ∫_{(0,v]} 1{s ≥ r}dφ(r):
a mixture of 1 and of indicators 1{s ≥ r}, total weight φ(v) ≤ 1. Likewise h(r′) = ∫₀¹ 1{r′ > r_θ}dθ for nondecreasing h. Hence
g₁(Σu, max u) is a mixture, total weight ≤ 1, of indicators of sets R = {u ∈ [0, v/2]^j : Σu ≥ r, Σu + max u < v − r_θ} (r = 0 allowed).
For fixed u_k (k ≠ i) the section of R in u_i is an interval [c₁, c₂): Σu ≥ r is a lower bound on u_i, and Σu + max u is nondecreasing
in u_i. Telescoping μ^{⊗j} − μ₀^{⊗j} = Σ_i μ^{⊗(i−1)} ⊗ (μ − μ₀)
⊗ μ₀^{⊗(j−i)} and integrating the i-th factor over the section first: |(μ^{⊗j} − μ₀^{⊗j})(R)| ≤ j·D_ρ(v/2)·M^{j−1}, M := v/2 + 2ρ
(masses of μ_ρ, μ₀ on [0, v/2]). Summing over j with weights 1/j! and the mixture weight 1: |T₂|/(ρx) ≤ e^{M}D_ρ(v/2) + O(ρ). ∎
(The constant L_S = 4e^{S+2} of Theorem 4.4 covers e^{M}.)
*Status of Theorem 4.4.* Second read (`read-T44.md`, Opus agent, 18:14–18:37 IST): every step ✓ except Step 3's local mass bound,
whose first version used the wrong majorant exp*(λ_ρ) (it undercounts repeated elements) and did not write the local smoothing;
the reader's fill (now in Step 3) gives κ_ρ(I) ≤ 6I₀(2√(6S))(|I| + ρ). Nothing in §4 uses transcendental 1/ρ; the reader stress-tested
the identities exactly at ρ = 1/18, where every composite lies on the lattice (46,992 tie decisions).
**Theorem 4.4′ (with a rate)** [proved here; the argument is the second reader's (`read-T44.md` §5), re-derived by the writer]. For
ρ ≤ 1/16 and every S there is C_S = exp(O(e^{2S})) with
  sup|π(y, x] − Π₀(y, x]|/(ρx), sup|C(y, x] − Λ₀(y, x]|/(ρx), sup_{x≤e^{S/ρ}}(E(x) − ½)/(ρx) ≤ C_S·ρ log(1/ρ)
(the first two over 1 ≤ y < x, p₁² ≤ x ≤ e^{S/ρ}). *Proof.* (1) In Step 3 replace the partition by a layer cake: α_ρ(v − u) is
nonincreasing in u, so its superlevel sets are initial segments [0, u_s), and κ_ρ([0, u_s)) ≤ K_S(u_s + ρ) gives
∫α_ρ(v − u)dκ_ρ(u) ≤ K_S∫₀^v α_ρ + 2K_Sρ. (2) Every other error is O_S(ρ log(1/ρ)) uniformly in y and v ≤ S: 4ρ (Step 2); 2K_Sρ,
2s₁K_S(v + ρ), Q/(ρx) ≤ 4ρe^{2S+4ρ} + 8ρ (Step 3); ρe^{M} + O(ρ²) and 2ρL_Sα_ρ ≤ 4ρL_S (Lemma 4.6 with Step 4); the [0, 2s₁) part
of Step 4 (late start s₁ = ρ log p₁). (3) Hence, at fixed ρ, α_ρ(v) ≤ ε_ρ + c∫₀^v α_ρ with c := 2(K_S + L_S), ε_ρ = O_S(ρ log(1/ρ)), and
Gronwall gives α_ρ(S) ≤ ε_ρe^{cS}, β_ρ(S) ≤ ε_ρ(1 + (K_S + L_S)Se^{cS}); Step 1 then bounds E. ∎ The rate is the one measured in §4.7
(offsets falling like ρ log(1/ρ)). At fixed ρ the bound is informative only while exp(O(e^{2τ}))·ρ log(1/ρ) is small, i.e. for
τ ≲ ½ log log(1/ρ).
**4.7 The macroscopic law on the data** [computed: `logs/collapse.log`, `logs/mertens.log` (`verify/mertens.py`, runs `m_*_1e10`),
`verify/s8sp.c` with the per-bin sum of 1/p]. (i) Prime fraction per step minus f₀(τ), at fixed τ, ρ decreasing: τ = 0.3: +0.0377,
+0.0301, +0.0251 (ρ = 0.0245, 0.0164, 0.0123); τ = 0.6: +0.0398, +0.0333, +0.0288 (ρ = 0.0491, 0.0327, 0.0245); τ = 1.15: +0.0274,
+0.0259, +0.0235 (ρ = 0.0982, 0.0654, 0.0491). (ii) Σ_{p≤x}1/p − Ein(τ): τ ≈ 0.565: −0.0413 (π/64, x = 10⁵), −0.0280 (π/128, x = 10¹⁰);
τ ≈ 0.28: −0.0369 (π/128, 10⁵), −0.0240 (π/256, 10¹⁰). (iii) E/(ρx) ≤ 10⁻⁷ at the top of every run. The offsets fall like
ρ log(1/ρ) (halving ρ multiplies them by 0.65–0.68; ρ log(1/ρ) gives 0.59–0.62).
*Where the offset comes from* [proved here for the lattice; heuristic for S8]: in the variable v, the lattice has
λ_ρ([0, v]) = v − Δ_ρ + o(ρ), Δ_ρ := ρ(log(1/ρ) + ψ(½)) (digamma, §2): the discrete system starts "late" by Δ_ρ. Removing prime mass Δ
at v = 0 from the template and solving the linearized Volterra equation δf(v) = Δ − ∫₀^v δf (kernel = density 1 of exp*(f₀) − δ₀) gives
δf(v) = Δe^{−v}: about +0.022 at τ = 0.3 for π/256 against +0.0251 measured; a heuristic first-order account, not a proof.

**4.8 What Theorem 4.4 is and is not.** It identifies the MACROSCOPIC arrival process of the charter's queue in the scaling limit:
intensity λ₀(τ) per step at every τ, the same function for every ρ (Lemma 1.3), and the queue content o(ρx). It is a law of large
numbers in the window of relative size η, uniform on τ ≤ S for each fixed S. It is not a statement about S8(ρ) at fixed ρ as x → ∞:
the constants are K_S = 4e^{2S+2}, L_S = 4e^{S+2}, and the error o(ρx) is θ = 1 in the language of Lemma B. Why it says
nothing at fixed ρ, precisely: the proof uses no positive margin — only f₀ ≥ 0 (the template never clips, so Λ₀ ≤ ρ(x − y) in
Step 1), which holds at every τ — but it closes by Gronwall, α_ρ(S) ≤ ε_ρ·exp(2(K_S + L_S)S), where ε_ρ collects terms that vanish
only as ρ → 0 (the granularity 1/(ρp₁²) ≤ 4ρ, the late start s₁ = ρ log p₁, the Q and repeated-element terms). At fixed ρ, ε_ρ is a
fixed positive number and the factor is super-exponential in τ, so the same inequalities give no bound. The limit dynamics is the Volterra
equation f = (1 − c[f])⁺ (c[f] = Σ_{j≥2} f^{*j}/j!), whose unique solution is f₀ — f₀ ≥ 0, so the clip never binds; the comparison with
the template is exact at every scale (Lemma 4.6(b)), so no first-order expansion around the template is needed, which is where
Session 40's route (a) stopped (`../../free-greedy-s40/theory/NOTE.md` §3.1, Lemma M) [quoted].




## §5. The local arrival process and the maximal queue length

**5.1 The random-phase model.** By Lemma 2.2's decomposition the arrivals are a superposition of components, one per cofactor
M′: the points m′·P (P a g-prime ≥ P⁺(M′)), an arithmetic progression of step exactly m′ lattice steps, thinned by primality of P.
Every period is ≥ p₁ ≈ 1/(2ρ) steps, so in a window of m < p₁ steps each component has at most one point. The random-phase model
RPM(ρ, τ) replaces the phases of the components by independent uniform phases; for the dominant one-element cofactors x_a the count
in a window of m steps is then Poisson-binomial with probabilities w_a = m/x_a, Σ_a w_a = mλ₂, Σ_a w_a² = m²Σ_a x_a^{−2} = m²ρ²ψ′(½ + ρ)
(trigamma, ψ′(½) = π²/2).
**Proposition 5.1 (the model)** [proved here; Le Cam's inequality recalled, unverified, used only in (iii)]. In RPM, for one-element
cofactors and m < p₁: (i) Var/mean of the window count = 1 − mρ²ψ′(½ + ρ)/λ₂; (ii) P(c = 2)/Poisson_{λ₂}(2) = 1 − ρ²ψ′(½ + ρ)/λ₂² + O(ρ⁴),
and P(c = j)/Poisson(j) = exp(−binom(j, 2)ρ²ψ′/λ₂² + O(jρ²)) for fixed j; (iii) total-variation distance to Poisson(mλ₂) ≤ m²ρ²ψ′(½ + ρ).
*Proof.* (i) Var = Σw_a(1 − w_a); the same exclusion gives Cov(c_k, c_{k+1}) = −Σ_a x_a^{−2} when every period exceeds 2 steps. (ii) P(c = j) = e_j(w)Π_a(1 − w_a) with e_j the elementary symmetric function; e₂ = (σ² − p₂)/2,
and e_j = (σ^j/j!)(1 − binom(j,2)p₂/σ² + …) for small p₂/σ². (iii) Le Cam. ∎
As ρ → 0 at fixed τ all three corrections vanish (∝ ρ²), and for m = o(1/ρ) the window law tends to Poisson; in RPM the
superposition of many sparse independent components tends to a Poisson process (law of rare events).

**5.2 S8 against the model** [computed: `verify/collapse.py`, `logs/collapse.log`, `logs/collapse_pc.log`]. For small ρ the
model's formulas hold to three digits, with no free parameter:

| ρ, τ | quantity | measured | RPM (5.1) |
|---|---|---|---|
| π/256, 0.30 | D(1), D(4), D(16) | 0.992, 0.970, 0.897 | 0.993, 0.974, 0.896 |
| π/256, 0.30 | P(c=2), P(c=3) / Poisson | 0.938, 0.827 | 0.938, 0.83 |
| π/128, 0.59 | D(1), D(4), D(16) | 0.987, 0.953, 0.834 | 0.987, 0.949, 0.798 |
| π/96, 0.60 | D(1), D(4) | 0.976, 0.914 | 0.978, 0.912 |
| π/64, 1.16 | D(1), D(4), D(16) | 0.981, 0.930, 0.801 | 0.974, 0.894, 0.577 |
| π/256, 0.30 | lag-one correlation of c_k | −0.0077 | −0.0066 |
| π/128, 0.59 | lag-one correlation | −0.0121 | −0.0128 |
| π/96, 0.60 | lag-one correlation | −0.0225 | −0.0225 |

The model fails once m approaches p₁ or τ is large (three-fold products, and the thinning by primality, give extra points per
component); there the measured window counts are LESS sub-Poisson than RPM's one-element prediction. **At fixed τ every deviation
from Poisson shrinks as ρ decreases** (τ = 0.6, ρ = 0.0245/0.0327/0.0491: D(4) = 0.953/0.914/0.814; mean queue / M/D/1 mean =
0.915/0.844/0.676), and the feedback-free lattice monoid shows the same window structure (π/128: lattice monoid at τ = 0.48,
D(1, 2, 4, 8, 16) = 0.984, 0.969, 0.941, 0.886, 0.775; S8 at τ = 0.51: 0.983, 0.967, 0.939, 0.889, 0.794; `logs/r128_m1_1e9.tsv`,
`logs/r128_m0_1e9.tsv`), so it is arithmetic, not feedback. (In the table λ₂ is replaced by the measured arrival rate λ.)

**Conjecture 5.2 (local Poisson limit)** [conjecture]. For fixed τ > 0, η ∈ (0, 1) and m ≥ 1, with k uniform among the steps with
x_k ∈ (x(1 − η), x], x = e^{τ/ρ}: (c_{k+1}, …, c_{k+m}) → i.i.d. Poisson(λ₀(τ)) in law as ρ → 0. Evidence: §5.2 and the per-step law
(P(c = 0)/e^{−λ} = 0.996–1.000, lag-one correlation −0.012 at π/128). What a proof needs: asymptotic independence of the component
phases {x/m′ mod t}, jointly over all ≈ ρ√x cofactors. For any FIXED finite set of components this is Kronecker–Weyl (the
per-step phase increments ρ/(a + δ), together with 1, are rationally independent when t is transcendental: Σ n_a ρ/(a + δ) = n₀ with
ρ = δ + ½ is a polynomial identity in the transcendental δ, and at δ = −a it forces n_a(½ − a)Π_{b≠a}(b − a) = 0, so all n = 0); uniformly over all components it is again the shifted divisor problem in short intervals (§3.2 (F2)). GAP.
**5.3 The queue of the limit process** [proved here]. Let c_k be i.i.d. Poisson(λ), 0 < λ < 1, e₀ = 0, e_k = max(e_{k−1} + c_k − 1, 0),
and κ = κ(λ) the positive root of λ(e^κ − 1) = κ (g(κ) := λ(e^κ − 1) − κ is convex with g(0) = 0, g′(0) = λ − 1 < 0).
**Proposition 5.3.** (i) P(e_k ≥ h) ≤ e^{−κh} for all k, h ≥ 0; stationary mean λ²/(2(1 − λ)). (ii) For every ε > 0,
P((1 − ε)log n/κ ≤ max_{k≤n} e_k ≤ (1 + ε)log n/κ) → 1. (iii) Scaling form: if the steps with x_k ≤ e^{τ/ρ} carry independent
Poisson(λ₀(τ_k)) arrivals, τ_k := ρ log x_k, then ρ·max_{x_k≤e^{τ/ρ}} e_k → η(τ) := τ/κ(λ₀(τ)) in probability as ρ → 0.
*Proof.* (i) By Lemma 1.2(iii) and time reversal, e_k has the law of max_{j≤k} S_j, S_j := Σ_{i≤j}(c_i − 1). Since
E e^{κ(c−1)} = e^{−κ}e^{λ(e^κ−1)} = 1, e^{κS_j} is a martingale and Doob's maximal inequality gives P(max_{j≤k} S_j ≥ h) ≤ e^{−κh}.
Mean: squaring e_k = e_{k−1} + X_k + I_k (X = c − 1, I_k := 1{e_{k−1} + c_k = 0}, so (e_{k−1} + X_k)I_k = −I_k) gives
e_k² = (e_{k−1} + X_k)² − I_k; in stationarity E I = 1 − λ, E X² = λ + (1 − λ)², E[e]·2(λ − 1) + λ + (1 − λ)² − (1 − λ) = 0. (ii) Upper:
union bound with (i) at h = (1 + ε)log n/κ. Lower: under the tilted law (Poisson(λe^κ)) the step c − 1 has mean μ̃ = λ + κ − 1 > 0
(κ > 1 − λ, since e^y − 1 ≤ y/(1 − y) gives g(1 − λ) ≤ 0); on a block of L := ⌈h/μ̃⌉ steps the tilted mean of S_L is ≈ h, so
P(S_L ≥ h) = Ẽ[e^{−κS_L}; S_L ≥ h] ≥ e^{−κ(h + √L)}P̃(h ≤ S_L ≤ h + √L) ≥ c·e^{−κh − Cκ√h} (central limit theorem under P̃); e at the block's end is ≥ the block's increment, and
the ⌊n/L⌋ blocks are independent; with h = (1 − ε)log n/κ the expected number of successful blocks → ∞. (iii) λ₀ is increasing, so
the arrivals are stochastically dominated by i.i.d. Poisson(λ₀(τ)) (Lindley is monotone): with n ≤ ρe^{τ/ρ} + 1 steps, (ii) gives
ρ·max ≤ (1 + ε)τ/κ(λ₀(τ)) + o(1). For the lower bound restrict to the ≥ ρe^{τ/ρ}(1 − e^{−δ/ρ}) steps with τ_k ∈ [τ − δ, τ], which
dominate i.i.d. Poisson(λ₀(τ − δ)); let ε, δ → 0. ∎
η(τ) [computed, `logs/eta.log`]: 0.0540 (τ = 0.2), 0.0982 (0.31), 0.262 (0.61), 0.571 (1.0), 1.139 (1.5), 1.918 (2.0), 4.17 (3.0),
48.3 (10); η(τ) ~ τ²/2 as τ → ∞, which is Session 40's heuristic "(ρ/2)log²x" [quoted: Session-40 NOTE l. 174–177] as the large-τ
asymptote of the scaling-limit constant.

**5.4 What is proved about S8's maximal queue, and what is measured.** Proved: (a) Theorem 4.4: max_{x≤e^{τ/ρ}} E(x) = o(ρe^{τ/ρ})
for every τ; (b) Theorems 2.3, 4.1 on τ < τ_c(ρ): E(x) ≤ 3/2 + Q(x + t) ≤ 3/2 + 4ρ²(x + t)·e^{2τ+4ρ} + τ/(ρ log p₁), explicitly. Not proved:
any bound of order 1/ρ or polylog. **Conjecture 5.4** [conjecture]: ρ·max_{x≤e^{τ/ρ}} E(x) → η(τ). It would follow from
Conjecture 5.2 in a large-deviation form on windows of O(1/ρ) steps; in RPM the cumulant generating function of such a window count
differs from Poisson's by −(e^θ − 1)²Σ_a w_a²/2 = O(1) against a main term of order 1/ρ, so RPM is consistent with it.
Measured [computed: `verify/sim_pq.py`, logs `logs/sim_pq_*.log`; 10 replicates of the Poisson-model queue with the SAME number
of steps and the measured arrival rate in every quarter-decade bin]:

| ρ (top τ) | max e, S8 | Poisson model: median [min, max] | ρ(max e + ½) | η(τ) |
|---|---|---|---|---|
| π/256 (0.31) | 5 | 5 [5, 6] | 0.067 | 0.098 |
| π/128 (0.61) | 7 | 7.5 [7, 8] | 0.184 | 0.262 |
| π/64 (1.19) | 9 | 11.5 [10, 13] | 0.466 | 0.763 |
| π/32 (2.20) | 13 | 18 [17, 20] | 1.325 | 2.293 |

S8 approaches the Poisson model as ρ decreases (ratio of maxima 0.72, 0.78, 0.93, 1.0). The leading-order constant η(τ) is far
from reached at these ρ: the finite-n term −log(prefactor)/κ and the rate offset λ̂ < λ₀ (§4.7) are O(1) in max e, i.e. O(ρ) in
ρ·max e; they vanish as ρ → 0 but slowly.

**5.5 The two corners of the (ρ, τ) plane.** The scaling limit is ρ → 0 at fixed τ; Lemma B is τ → ∞ at fixed ρ. They do not
commute, and the data show the arithmetic regularity moving the other way along the second direction: at fixed ρ the queue's
excursions grow (length ~ τ² steps at large τ), the components with period x_a shorter than the excursion become perfectly regular
(⌊m/x_a⌋ or ⌈m/x_a⌉ points per window), and the measured tail rate exceeds the Poisson-queue κ by the factor 1.05 (π/128, τ = 0.6),
1.16 (π/64, 1.0), 1.31 (π/32, 2.0), and Session 40's 1.45–1.65 at π/16 and π/4 [quoted: Session-40 NOTE l. 178–183]. So at
fixed ρ, large τ, the arrival process is MORE regular than the scaling limit — favorable to Lemma B, but nothing proved here
controls that corner.


## §6. Numerical record (ρ = π/32, π/64, π/128, and six more values)

**Generator** `verify/s8sp.c` [computed]: block sweep (composites in [B, B′), B′ ≤ p₁B, are q·m with q a generator, q² < B′, and m a
stored element with spf(m) ≥ q, so every cofactor is known); Lindley queue per lattice step; mode 0 = S8, mode 1 = the feedback-free
lattice monoid; e-dumps for the step-by-step domination check. Exact ordering: every composite within 10⁻⁵ steps of a lattice
point is re-decided in double-double (t = D/π and each lattice factor in double-double, factorization read from the stored
spf/cofactor chain); no decision was unresolved at margin 10⁻²². Validation against Session 40 [quoted: Session-40 NOTE l. 127,
l. 133–134, l. 215, §3.1 l. 234]: π/4 to 10⁶: 78,134 g-primes, sup E = 39.5303; π/16 to 10⁷: 633,514 g-primes, sup E = 12.8385;
π/32 to 10⁶ and 10⁸: sup E = 6.3931, 9.8578; π/64 to 10⁶: 3.5062 (logs `logs/val_*.tsv`). Statistics per quarter decade:
arrival histogram, lag-one product, windows of 2^j steps (j ≤ 12), queue histogram, max e, sup E (exact, at every arrival),
Σ1/p (`verify/ana.py`, `collapse.py`, `mertens.py`, `sim_pq.py`, `eta.py`, `tauc.py`, `qs.c`; runners `run_main.sh`,
`run_extra.sh`, `run_sim.sh`). Runs (`logs/`, scratch binaries under `/private/tmp/rh-s41-lemmaB-U4-sparse/`):

| run | ρ | mode | X | steps | idle steps (g-primes in mode 0) | sup E | max e | re-decided / flips / unresolved | time |
|---|---|---|---|---|---|---|---|---|---|
| `r16_m0_4e9` | π/16 | 0 | 4·10⁹ | 7.854·10⁸ | 1.874·10⁸ | 22.26 | 21 | 11,888 / 41 / 0 | 56 s |
| `r24_m0_5e9` | π/24 | 0 | 5·10⁹ | 6.545·10⁸ | 2.226·10⁸ | 17.46 | 16 | 8,994 / 13 / 0 | 41 s |
| `r32_m0_5e9` | π/32 | 0 | 5·10⁹ | 4.909·10⁸ | 2.096·10⁸ | 14.39 | 13 | 5,337 / 10 / 0 | 27 s |
| `r32_m1_1e9` | π/32 | 1 | 10⁹ | 9.817·10⁷ | 2.354·10⁵ | 2.0·10⁷ | 2.0·10⁷ | 2,304 / 1 / 0 | 10 s |
| `r48_m0_1e10` | π/48 | 0 | 10¹⁰ | 6.545·10⁸ | 3.574·10⁸ | 13.36 | 12 | 5,868 / 15 / 0 | 31 s |
| `r64_m0_2e10` | π/64 | 0 | 2·10¹⁰ | 9.817·10⁸ | 6.126·10⁸ | 10.48 | 9 | 7,354 / 38 / 0 | 39 s |
| `r64_m1_1e10` | π/64 | 1 | 10¹⁰ | 4.909·10⁸ | 2.182·10⁸ | 14.16 | 13 | 5,326 / 26 / 0 | 26 s |
| `r96_m0_3e10` | π/96 | 0 | 3·10¹⁰ | 9.817·10⁸ | 7.140·10⁸ | 9.46 | 8 | 5,272 / 11 / 0 | 31 s |
| `r128_m0_5e10` | π/128 | 0 | 5·10¹⁰ | 1.227·10⁹ | 9.641·10⁸ | 7.77 | 7 | 5,271 / 16 / 0 | 32 s |
| `r128_m1_1e10` | π/128 | 1 | 10¹⁰ | 2.454·10⁸ | 1.865·10⁸ | 8.29 | 7 | 1,082 / 0 / 0 | 7 s |
| `r192_m0_1e11` | π/192 | 0 | 10¹¹ | 1.636·10⁹ | 1.392·10⁹ | 6.12 | 5 | 4,792 / 32 / 0 | 36 s |
| `r256_m0_1e11` | π/256 | 0 | 10¹¹ | 1.227·10⁹ | 1.090·10⁹ | 5.78 | 5 | 2,706 / 8 / 0 | 24 s |

(The 10⁹ runs `r*_m0_1e9`, `r*_m1_1e9` carry the domination check of Theorem 2.1; `m_*_1e10` carry Σ1/p; `br*_L0…L3`,
`br*_S8vs1`, `br*_S8vs2` with `logs/brackets_finite.log` carry the test of Prop. 3.3.) "Flips" are composites
whose double-precision step was wrong and was corrected by the double-double re-decision; without the re-decision these runs
would not be S8. For π/16 to 4·10⁹, sup E/log²x = 0.0456 (Session 40: 0.049 to 10^7.5).
**Lattice monoid vs S8 (same ρ, same X)**: max e^lat = 7 vs max e = 6 (π/128, to 10¹⁰); 13 vs 9 (π/64, to 10¹⁰): on the sparse range
the feedback-free queue is a good proxy, and Proposition 3.2 makes it the only object a sharp bound must control there.
