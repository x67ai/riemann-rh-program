# NOTE — unit `U4-sparse` (stream `lemmaB-s41`): the sparse regime of S8(ρ) and the scaling limit ρ → 0

Session 41, started 17:07 IST 2026-10-01. Writer: Opus 5.5 (agent). Labels as in `../CHARTER.md` §4: **[proved here]**,
**[computed]** (script + log in `verify/`), **[quoted]**, **[recalled, unverified]** (never load-bearing). Gaps are marked GAP.

**Notation.** S8(ρ) as in `../../free-greedy-s40/CHARTER.md` §1. t := 1/ρ (as in the Session-40 NOTE). Lattice points
x_k := 1 + (k − ½)t = t(k + δ), δ := ρ − ½, k ≥ 1; p₁ = x₁ = 1 + t/2. The charter's scaling variable "t = ρ·log x" is written
**τ := ρ log x** here, to avoid the clash with t = 1/ρ. Lindley form (charter §2(a)): c_k = composites in (x_{k−1}, x_k],
e_k = max(e_{k−1} + c_k − 1, 0), prime at x_k iff e_{k−1} + c_k = 0. Template prime fraction per step f₀(τ) := (1 − e^{−τ})/τ,
template load λ₀(τ) := 1 − f₀(τ).

## §0. Close (filled last)

(pending)

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
−ψ(½) = 1.9635 [ψ = digamma]. **So on the sparse range E(x) ≤ 2 + 4ρ²x·e^{2τ+4ρ} + τ/(ρ log p₁): the integer error is at most
O(ρ) times the number of steps, explicitly.** The exact Q is far smaller (table below): its j-element part is ≈ c_j ρ^j z^{j/(j+1)}
(Q₁(z) = #{a : x_a² ≤ z} ≤ ρ√z + 1), so for small τ the bound is ≈ ρ√x.

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

**3.2 The exact failing steps.**
(F1) *Beyond τ_c(ρ): the domination of Theorem 2.1 is the step that fails.* There the comparison queue has arrival rate Λ(τ) > 1 per
step and grows linearly [computed, `logs/r32_m1_1e9.tsv`]: max e^lat = 26 to 10⁷ (τ = 1.58, rate 0.892), 368,982 to 10⁸ (τ = 1.81, rate
1.072), 20,032,408 to 10⁹ (rate 1.264), while S8's own queue stays ≤ 13 there. The information Theorem 2.1 throws away is exactly the
set of BUSY lattice points (lattice points that are not g-primes, a fraction λ₀(τ′) ≈ τ′/2 of the steps at scale τ′): the lattice monoid
overcounts S8's arrival rate by Λ(τ) − λ₀(τ) = τ²/4 − 5τ³/144 + O(τ⁴), the rate of lattice products with at least one busy factor.
No argument that forgets which lattice points are busy can pass τ_c(ρ). To pass it one needs a LOWER bound for the busy set at scales
≤ x/p₁, i.e. a lower bound for composites there, i.e. an upper bound for primes further down: the alternating scheme of §4.3, of
which Theorem 2.1 is the zeroth term.
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
Template counts: Π₀(y, x] := ∫_y^x ρf₀(ρ log u)du (primes), Λ₀(y, x] := ρ(x − y) − Π₀(y, x] (composites). Additive measures in
the variable v = ρ log u: μ_ρ := Σ_p p^{−1}δ_{ρ log p}, μ̃_ρ := Σ_p Σ_{k≥1} k^{−1}p^{−k}δ_{kρ log p}, ν_ρ := Σ_{n∈G} n^{−1}δ_{ρ log n}.

**Theorem 4.1 (below τ_c)** [proved here]. For 0 < S < τ_c there are ρ₁(S) > 0 and C(S) < ∞ such that for ρ < ρ₁(S):
E(x) ≤ 2 + C(S)ρ²x + S/(ρ log p₁) for all 1 ≤ x ≤ e^{S/ρ}. So E(x)/(ρx) = O(ρ) + O(1/(ρ²x log(1/ρ))) there.
*Proof.* By Prop. 3.1, S_ρ(e^{S/ρ} + 2t) → Λ(S) < 1, so S_ρ ≤ 1 on the range for small ρ. Theorem 2.3 gives E(x) ≤ 3/2 + Q(x + t),
and §2 gives Q(z) ≤ 4ρ²z·e^{2σ_z} + log z/log p₁ with σ_z ≤ S + 2ρ. ∎

**Lemma 4.2 (exact identities)** [proved here]. For 1 ≤ y < x: (i) π(y, x] + C(y, x] = ρ(x − y) + E(x) − E(y);
(ii) C(y, x] = Σ_{M′} π(J_{M′}), over nonempty multisets M′ of g-primes, J_{M′} := (y/m′, x/m′] ∩ [P⁺(M′), ∞), and every element of
every M′ that contributes is ≤ √x; (iii) E(x) ≤ ½ + sup_{1≤y<x}(C(y, x] − ρ(x − y))⁺.
*Proof.* (i) N(u) = ρ(u − 1) + 1 + E(u) and N(x) − N(y) = π(y, x] + C(y, x]. (ii) n ↦ (M′, P⁺(n)) as in Lemma 2.2 (now for g-primes);
if Q ∈ M′ then Q² ≤ Q·P⁺(n) ≤ n ≤ x. (iii) For x < p₁, E(x) ≤ 0. Otherwise let y be the largest g-prime ≤ x; E(y) = ½ [quoted:
Session-40 NOTE l. 52, 1.0(ii)] and π(y, x] = 0, so (i) gives E(x) = ½ + C(y, x] − ρ(x − y). ∎

**Lemma 4.3 (integer regularity gives the prime law, vaguely)** [proved here]. Suppose E(x) ≤ ε_ρρx + K for 1 ≤ x ≤ e^{S/ρ},
with ε_ρ → 0 and K fixed. Then for every interval I ⊂ [0, S]: μ_ρ(I) → ∫_I f₀(v)dv; in particular Σ_{p ≤ x} 1/p → Ein(τ) :=
∫₀^τ (1 − e^{−v})/v dv uniformly for τ = ρ log x ∈ [0, S].
*Proof.* (a) ν_ρ = exp*(μ̃_ρ) (additive convolution exponential on [0, ∞)): the g-integers are the free commutative monoid on the
g-primes, so ν_ρ = ⊛_p Σ_{k≥0} p^{−k}δ_{kρ log p} = ⊛_p exp*(Σ_{k≥1} k^{−1}p^{−k}δ_{kρ log p}), using Σ_{k≥0}y^k = exp(Σ_{k≥1}y^k/k) in the
convolution algebra (y = p^{−1}δ_{ρ log p}). On [0, S] all sums are finite, since every term is supported on [s₁, ∞), s₁ := ρ log p₁.
(b) For I = (v₁, v₂] with a = e^{v₁/ρ}, b = e^{v₂/ρ}: ν_ρ(I) = ∫_{(a,b]}dN(u)/u = ρ log(b/a) + E(b)/b − E(a)/a + ∫_a^b E(u)u^{−2}du
(insert N = ρ(u − 1) + 1 + E; the other terms cancel). With −½ < E ≤ ερu + K and a ≥ p₁ ≥ 1/(2ρ) when v₁ ≥ s₁ (and ν_ρ puts no
mass on (0, s₁)), this gives |ν_ρ(I) − |I|| ≤ ε_ρ|I| + β_ρ for every I ⊂ (0, S], β_ρ := (4K + 6)ρ log(1/ρ) → 0.
(c) σ_ρ := ν_ρ − δ₀ satisfies σ_ρ(I) ≤ 2|I| + β_ρ. Let U be the uniform probability on [0, β_ρ]; σ_ρ * U has density
σ_ρ([w − β_ρ, w])/β_ρ ≤ 3, so σ_ρ^{*n}([0, S]) ≤ (σ_ρ*U)^{*n}([0, S + nβ_ρ]) ≤ 3^n(S + nβ_ρ)^n/n!. On [0, S] only n ≤ S/s₁ occur and
nβ_ρ ≤ S(4K + 6)log(1/ρ)/log(1/(2ρ)) ≤ (8K + 12)S, so Σ_{n>n₀} σ_ρ^{*n}([0, S])/n → 0 as n₀ → ∞ uniformly in ρ.
(d) σ_ρ → Lebesgue measure vaguely on [0, ∞), with uniform local bounds; convolution is jointly continuous for vague convergence of
such measures on [0, ∞) (products of the restrictions to [0, S + 1]² converge weakly, and u + v ≤ S is a compact condition), so
σ_ρ^{*n} → (v^{n−1}/(n − 1)!)dv for each n, also on intervals (the limit is absolutely continuous).
(e) μ̃_ρ = Σ_{n≥1}((−1)^{n+1}/n)σ_ρ^{*n} on [0, S] (convolution logarithm; a finite sum there). By (c)–(d), μ̃_ρ(I) →
∫_I Σ_{n≥1}(−1)^{n+1}v^{n−1}/n! dv = ∫_I f₀. Finally μ̃_ρ − μ_ρ has total mass ≤ 2Σ_a x_a^{−2} ≤ 10ρ² (prime powers). ∎
*Corollary* [proved here]: below τ_c (Theorem 4.1 gives the hypothesis with ε_ρ = O(ρ)), the Mertens-type law Σ_{p≤x} 1/p →
Ein(ρ log x) holds uniformly on τ ≤ S < τ_c. For the lattice itself Σ_{x_a≤x} 1/x_a → τ; Ein(τ) = τ − τ²/4 + … records the busy steps.
**Theorem 4.4 (macroscopic law in the scaling limit, every τ)** [proved here; single-check]. For every S > 0, as ρ → 0,
  sup_{1≤y<x≤e^{S/ρ}} |π(y, x] − Π₀(y, x]|/(ρx) → 0,  sup |C(y, x] − Λ₀(y, x]|/(ρx) → 0,  sup_{x≤e^{S/ρ}} (E(x) − ½)/(ρx) → 0
(the first two over x ≥ p₁²). So at every τ the queue's arrival intensity per step is λ₀(τ) = 1 − (1 − e^{−τ})/τ in every window of
fixed relative length (y = x(1 − η)), the g-primes fill the fraction f₀(τ), the queue content is o(ρx), and by Lemma 4.3
Σ_{p≤x} 1/p → Ein(τ) for every τ — no restriction to τ < τ_c.
*Proof.* Put α_ρ(v) := sup{|π(y, x] − Π₀(y, x]|/(ρx) : 1 ≤ y < x, p₁² ≤ x ≤ e^{v/ρ}}, β_ρ(v) the same with C, Λ₀; both are
nondecreasing in v and bounded (α_ρ ≤ 2 since π(y, x] ≤ ρ(x − y) + 1; β_ρ ≤ Λ(S) + 2 by Theorem 2.1's C ≤ C^lat and Lemma 2.2).
Let A, B be their limsups as ρ → 0.
*Step 1 (queue).* Lemma 4.2(iii) and Λ₀(y, x] ≤ ρ(x − y) give −½ < E(x) ≤ ½ + β_ρ(v)ρx for x ≤ e^{v/ρ}.
*Step 2 (primes).* Lemma 4.2(i) with ρ(x − y) = Π₀ + Λ₀ gives π − Π₀ = (Λ₀ − C) + E(x) − E(y), so α_ρ(v) ≤ 2β_ρ(v) + 4ρ (as
1/(ρp₁²) ≤ 4ρ). Hence A ≤ 2B.
*Step 3 (composites).* By Lemma 4.2(ii), C(y, x] − Λ₀(y, x] = T₁ + T₂ with T₁ := Σ_{M′}(π(J_{M′}) − Π₀(J_{M′})) and
T₂ := Σ_{M′}Π₀(J_{M′}) − Λ₀(y, x]. Each J_{M′} is a window with right end x/m′. If x/m′ ≥ p₁² its error is ≤ α_ρ(v − u)ρx/m′,
u := ρ log m′; if x/m′ < p₁², all lattice points in J are g-primes (Lemma 1.1) and the error is ≤ ρ(x/m′)·2s₁ + 1. With
κ_ρ := Σ_{M′: m′P⁺(M′)≤x} δ_{ρ log m′}/m′ and Q(x) ≤ 4ρ²x e^{2S+4ρ} (§2):
  |T₁| ≤ ρx∫α_ρ(v − u)dκ_ρ(u) + 2s₁ρx·κ_ρ([0, v]) + Q(x).
κ_ρ is dominated by the lattice monoid exp*(λ_ρ) − δ₀; smoothing λ_ρ (λ_ρ(I) ≤ |I| + 2ρ) by the uniform law on [0, 2ρ] as in
Lemma 4.3(c) gives κ_ρ(I) ≤ K_S(|I| + ρ log(1/ρ)), K_S := 4e^{2S+2}. As α_ρ is nondecreasing, summing over a partition of [0, v]
into intervals of length δ_ρ := (ρ log(1/ρ))^{1/2} gives |T₁| ≤ ρx[K_S∫₀^v α_ρ(w)dw + o(1)].
For T₂ use Lemma 4.6 below: |T₂| ≤ ρx[L_S·D_ρ(v/2) + O(ρ)], D_ρ(w) := sup_{I⊂[0,w]} |μ_ρ(I) − ∫_I f₀|, L_S := 4e^{S+2}.
*Step 4 (discrepancy from window errors).* For I = (w₁, w₂] ⊂ [2s₁, w], a = e^{w₁/ρ}, b = e^{w₂/ρ}: μ_ρ(I) − ∫_I f₀ =
Δ(b)/b − Δ(a)/a + ∫_a^b Δ(u)u^{−2}du with Δ(u) := π(a, u] − Π₀(a, u] (integration by parts on dπ − dΠ₀), and |Δ(u)| ≤ α_ρ(ρ log u)ρu;
so |μ_ρ(I) − ∫_I f₀| ≤ 2ρα_ρ(w) + ∫_{w₁}^{w₂}α_ρ. On [0, 2s₁] every lattice point is a g-prime and the discrepancy is ≤ λ_ρ-vs-Lebesgue
error + 2s₁·(1 − f₀(2s₁)) = O(ρ log(1/ρ)). Hence D_ρ(w) ≤ ∫₀^w α_ρ + o(1).
*Step 5 (closing).* Steps 3–4 give β_ρ(v) ≤ (K_S + L_S)∫₀^v α_ρ + o(1); with Step 2 and reverse Fatou (0 ≤ α_ρ ≤ 2 on [0, S]):
A(v) ≤ 2(K_S + L_S)∫₀^v A(w)dw, A nondecreasing and bounded. If A ≢ 0 on [0, S], let v₁ := inf{v : A(v) > 0}; for
v₁ < v < v₁ + 1/(4(K_S + L_S)): A(v) ≤ 2(K_S + L_S)(v − v₁)A(v) ≤ ½A(v), so A(v) = 0 — a contradiction. So A ≡ 0, B ≤ (K_S + L_S)∫A ≡ 0,
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
(c) Sections. Write f₀(v − s) = f₀(v) − ∫₀^s f₀′(v − r)dr·(−1)… precisely, for s ∈ [0, v]: f₀(v − s) = f₀(v − v) − ∫_s^v ψ(r)dr with
ψ(r) := −(d/dr)f₀(v − r) ≤ 0, so f₀(v − s) = 1 − ∫₀^v ψ(r)·1{r ≥ s}dr·(−1) — i.e. a mixture, with total weight TV(f₀) ≤ 1, of the
constant 1 and indicators 1{s ≤ r}. Likewise h(r′) = ∫₀^1 1{h(r′) > θ}dθ and {h > θ} = {r′ > r_θ}. Hence g₁(Σu, max u) is a mixture,
with total weight ≤ 2, of indicators of sets R = {u ∈ [0, v/2]^j : Σu ≤ r, Σu + max u < v − r_θ}. For fixed coordinates u_k (k ≠ i), the
section of R in u_i is an interval [0, c) (both conditions are monotone in u_i). Telescoping μ^{⊗j} − μ₀^{⊗j} = Σ_i μ^{⊗(i−1)} ⊗ (μ − μ₀)
⊗ μ₀^{⊗(j−i)} and integrating the i-th factor over the section first: |(μ^{⊗j} − μ₀^{⊗j})(R)| ≤ j·D_ρ(v/2)·M^{j−1}, M := v/2 + 2ρ
(masses of μ_ρ, μ₀ on [0, v/2]). Summing over j with weights 1/j! and the mixture weight 2: |T₂|/(ρx) ≤ 2e^{M}D_ρ(v/2) + O(ρ). ∎
(The constant L_S = 4e^{S+2} of Theorem 4.4 covers 2e^{M}.)
*Status of Theorem 4.4.* Every step is written above; it is single-checked (this unit only). The two places most worth a second
reader: the uniform local mass bound for κ_ρ (smoothing argument, Step 3) and the section argument of Lemma 4.6(c), which needs
each region to have interval sections — true here because Σu and Σu + max u are nondecreasing in every coordinate.



## §5. The local arrival process and the maximal queue length

(pending)

## §6. Numerical record (ρ = π/32, π/64, π/128)

(pending)
