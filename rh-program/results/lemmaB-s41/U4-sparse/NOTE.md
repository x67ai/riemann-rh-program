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

(pending)

## §3. What fails beyond the sparse range

(pending)

## §4. The scaling limit τ = ρ log x: macroscopic law

(pending)

## §5. The local arrival process and the maximal queue length

(pending)

## §6. Numerical record (ρ = π/32, π/64, π/128)

(pending)
