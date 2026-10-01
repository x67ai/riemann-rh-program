# NOTE — unit `U2-structured` (stream `lemmaB-s41`): an object with a computable count

Session 41, started 17:26 IST 2026-10-01. Writer: Opus 5.5 (agent). Labels as in the charter §4: **[proved here]**, **[computed]**
(script + log in `verify/`), **[quoted]** (source at page/line, on disk), **[recalled, unverified]** (never load-bearing).
Notation: a Beurling system P (g-primes with multiplicity), N = N_P (formal products, with multiplicity, 1 included), ρ > 0 the
density, R(u) := N(u) − ρu, E(u) := N(u) − ρ(u − 1) − 1 = R(u) − (1 − ρ); (A) R ≥ r₀ > ρ on [1, ∞); (B) R = O(u^θ) with
θ < ½·r₀/(r₀ + ρ). Over F_q: norms qⁿ, A_n = #g-integers of degree n, b_d = #g-primes of degree d, Z(u) = Σ A_n uⁿ = Π_d (1 − u^d)^{−b_d}.

## §0. Close

(filled last)

## §1. Rung 1: what makes exact regularity possible over F_q

**1.0 The F_q greedy** [proved here]. Given integer targets T_0 = 1, T_n ≥ 0, put b_n := T_n − C_n, C_n := [uⁿ]Π_{d<n}(1 − u^d)^{−b_d}
(degree-n g-integers that are products of ≥ 2 g-primes of lower degree; a g-prime of degree n contributes only to A_n itself).
The system is EXACT (A_n = T_n for all n) iff every b_n ≥ 0; otherwise the greedy clips (b_n = 0) and overshoots. Writing
a_n := Σ_{d|n} d·b_d, one has u·Z′/Z = Σ a_n uⁿ (since log Z = Σ_d b_d Σ_j u^{dj}/j), hence b_n = (1/n)Σ_{d|n} μ(n/d)a_d:
exactness ⇔ every Möbius sum of the coefficients of u·(log Z_T)′ is ≥ 0, Z_T := Σ T_n uⁿ.

**Theorem 1.1 (the F_q template is a necklace system)** [proved here]. Let q ≥ 2 and 1 ≤ m ≤ q − 1 be integers and T_n = m·q^{n−1}
(n ≥ 1). Then b_n = M(q, n) − M(q − m, n) ≥ 0 for every n, where M(Q, n) := (1/n)Σ_{d|n}μ(n/d)Q^d; the system is exact,
Z(u) = (1 − (q − m)u)/(1 − qu), and its only zero is u = 1/(q − m), i.e. s* = log(q − m)/log q.
*Proof.* Z_T = 1 + mu/(1 − qu) = (1 − (q − m)u)/(1 − qu), so u(log Z_T)′ = Σ_n (qⁿ − (q − m)ⁿ)uⁿ, a_n = qⁿ − (q − m)ⁿ, and Möbius
inversion gives b_n = M(q, n) − M(q − m, n). Nonnegativity: every word of length n over a Q-letter alphabet is v^{n/d} for a unique
primitive v of length d | n, so Σ_{d|n} P(Q, d) = Qⁿ with P = number of primitive words; Möbius gives P(Q, n) = n·M(Q, n). Fix m
"special" letters. The primitive words over q letters that use at least one special letter number P(q, n) − P(q − m, n); cyclic
rotation acts freely on primitive words of length n (orbits of size exactly n) and preserves "uses a special letter", so this number
is n times a nonnegative integer. Hence b_n = (P(q, n) − P(q − m, n))/n ∈ ℤ_{≥0}. ∎
*Real-line reading* [proved here]. With ρ := m/(q − 1), N_F(qⁿ) = 1 + Σ_{k≤n} m q^{k−1} = 1 + ρ(qⁿ − 1) = N_c(qⁿ): the F_q template is
the REAL template N_c(x) = 1 + ρ(x − 1) sampled exactly at the norms qⁿ (Diamond's continuous system, §0 of the s40 charter), and its
zero s*(q) = log(1 + (1 − ρ)(q − 1))/log q tends to the template zero 1 − ρ as q → 1⁺ and to 1 as q → ∞. Between norms the count is
the step function, N_F(x) − N_c(x) ∈ (−ρ(q − 1)qⁿ, 0] on [qⁿ, q^{n+1}): over ℝ the error is linear and log-periodic (β = 1).
Exactness needs m·q^{n−1} ∈ ℤ for all n, which forces q ∈ ℤ (if q = a/b in lowest terms with b > 1, b^{n−1} | m for all n; if q
is irrational, q = (mq²)/(mq) is rational): the exact template exists only on integer norm ratios. [computed: `verify/fq_greedy.py`,
log `verify/logs/fq_greedy.log`, part (a): the greedy reproduces b_n = M(q, n) − M(q − m, n) and A_n = T_n exactly for every
1 ≤ m < q, q ∈ {2, 3, 4, 5, 7, 16}, n ≤ 40.]

**Proposition 1.2 (one-sided targets)** [proved here]. For T_n = m q^{n−1} + c (n ≥ 1) with integer c ≥ 1:
Z_T(u) = [1 − Su + Pu²]/((1 − u)(1 − qu)), S = q + 1 − m − c, P = q − m − cq < 0, so a_n = qⁿ + 1 − ω₁ⁿ − ω₂ⁿ with
ω₁ ∈ (q − m, q − m + cm/(q − m − 1 + c)) and ω₂ = P/ω₁ ∈ (−(q(c − 1) + m)/(q − m), 0). (f(ω) = ω² − Sω + P has f(0) = P < 0,
f(q − m) = −cm < 0, f(q) = m(q − 1) > 0, and f(q − m + δ) = −cm + δ(q − m − 1 + c) + δ² > 0 for δ = cm/(q − m − 1 + c).)
Since n·b_n ≥ a_n − Σ_{d|n, d<n}|a_d| and |a_d| ≤ 2q^d + 1 + |ω₂|^d, every b_n with n ≥ 3 is positive as soon as
q ≥ max(2m, m + 1 + c, 16c², 116/m²) [crude; the steps: ω₁ ≤ q − m/2, |ω₂| < 2c ≤ √q/2, then (m/2)q^{n−1} > 5q^{n/2} + n·q^{n/4}],
and b_2 = mq + c − (m + c)(m + c + 1)/2 ≥ 0 iff 2mq + 2c ≥ (m + c)(m + c + 1). So for every c ≥ 1 the one-sided target is exactly
realizable for all large q, with A_n − (m/q)qⁿ = c for n ≥ 1 — an F_q system with "(A)" (r_n ≡ c > 0), "(B)" with θ = 0, and the
real zero s* = log ω₁/log q ∈ (log(q − m)/log q, 1). [computed, part (b): no negative b_n to n = 40 except where the n = 2 (or n = 3)
condition fails: q = 5, m = 1, c ∈ {3, 5}; q = 7, c = 5; q = 11, m = 2, c = 5 — always at n ≤ 3; part (c): rounded targets
⌈ρqⁿ⌉ + c, ρ ∈ {1/π, 1/e, √2 − 1}, exact to n = 30 except q = 5, ρ = √2 − 1, c = 2 at n = 2.]

**1.3 What makes exact regularity possible on rung 1 — the answer.** Three things, and the third is the one that does not transfer:
(E1) the norm map is a homomorphism onto a discrete group q^ℤ, so "the count at a norm" is one integer A_n and the target is a
sequence, not a function of position; (E2) triangularity — C_n depends on b_1, …, b_{n−1} only, b_n is free; (E3) the norm monoid
q^ℕ ≅ (ℕ, +) has RANK ONE, and for rank one the flat target's logarithm is Σ (1 − (1 − τ)ⁿ)(qu)ⁿ/n (compositions of n), with
every coefficient positive, so b_n ≈ a_n/n ≈ τ'qⁿ/n — an exponentially large slack per norm point that absorbs bounded target
corrections (Prop. 1.2; data: the only failures are at n ≤ 3), and plausibly any correction small against qⁿ/n (not proved here). §2 shows that (E3) fails for every norm monoid of
rank ≥ 2 and that finite rank kills (B) on the real line, so the F_q mechanism has no exact real-scale substitute.

## §2. Exactness is a rank-one phenomenon

Setting. H = free commutative monoid on generators g_1, …, g_r (r ≤ ∞), w > 0 completely multiplicative on H, τ ∈ (0, 1). The FLAT
target is T(1) = 1, T(h) = τ·w(h) (h ≠ 1): a fixed fraction τ of the weight at every point (rank one: T_n = τqⁿ, the template of
Theorem 1.1 with m = τq). It is exactly realizable iff there are b(d) ≥ 0 (d ∈ H \ {1}, real or integer) with
Π_d (1 − [d])^{−b(d)} = Σ_h T(h)[h], i.e. iff F := log(1 − τ + τΠ_i(1 − w(g_i)x_i)^{−1}) has F_h = Σ_{j: h = d^j} b(d)/j with all
b ≥ 0. Since F_h is a sum of b's with positive weights, ONE negative coefficient F_h already rules out realizability.
(w only rescales x_i, so signs are those of the case w ≡ 1.)

**Theorem 2.1 (flat bookkeeping needs rank one)** [proved here; novelty: single-check — the ingredients are classical]. (i) r = 1:
every coefficient of F is positive, F_n = (1 − (1 − τ)ⁿ)/n, so no obstruction of the kind in (ii) (existence, with integer
multiplicities, is Theorem 1.1 when w(g) = q and τq are integers).
(ii) r ≥ 2: for every τ ∈ (0, 1), F has infinitely many negative coefficients, already at monomials x_1^a x_2^b with a, b ≥ 1. So no
Beurling system supported on a free norm monoid of rank ≥ 2 carries a fixed fraction τ ∈ (0, 1) of the weight at every point.
*Proof.* (i) log(1 − τ + τ/(1 − x)) = log(1 − (1 − τ)x) − log(1 − x). (ii) Setting x_3 = x_4 = … = 0 keeps exactly the coefficients
supported on {1, 2}, so take r = 2 and s := 1 − τ. Since 1 − τ + τ/((1 − x)(1 − y)) = (1 − s(x + y) + sxy)/((1 − x)(1 − y)), the
MIXED part of F (coefficients with a, b ≥ 1) is M(x, y) := log(1 − s(x + y) + sxy) − log(1 − sx) − log(1 − sy). On the diagonal,
μ(z) := M(z, z) = log[(1 − 2sz + sz²)/(1 − sz)²] = Σ_n m_n zⁿ with m_n = Σ_{a+b=n, a,b≥1} F_{(a,b)}. The roots of 1 − 2sz + sz²
are z_± = 1 ± i(1/s − 1)^{1/2}, of modulus s^{−1/2} < s^{−1}; so μ is analytic in |z| < s^{−1/2} (simply connected, argument of the
log nonvanishing, μ(0) = 0) and has logarithmic singularities at z_±: its radius of convergence is exactly s^{−1/2}. On the real axis
1 − 2sz + sz² = s(z − 1)² + 1 − s > 0 and (1 − sz)² > 0 at z = s^{−1/2}, so μ is analytic at the positive point z = s^{−1/2}. If every
m_n were ≥ 0, the Vivanti–Pringsheim theorem [recalled, unverified — a standard theorem of complex analysis: a power series with
nonnegative coefficients is singular at the positive point of its circle of convergence] would make z = s^{−1/2} singular. Hence some
m_n < 0, so some F_{(a,b)} < 0 with a, b ≥ 1; applied to μ minus any polynomial, infinitely many. ∎
*Two sharper forms* [proved here]. (a) r = ∞, squarefree points: in ℚ[[x]]/(x_i²), Π(1 − x_i)^{−1} = Σ_S x_S, and the coefficient of
x_1⋯x_k in F is Σ_{set partitions π of [k]} (−1)^{|π|−1}(|π| − 1)! τ^{|π|} = κ_k(τ), the k-th cumulant of a Bernoulli(τ) variable
(all its moments equal τ). K(t) = log(1 − τ + τe^t) has its nearest singularities at t = log((1 − τ)/τ) ± iπ (non-real) and is analytic on
(0, ∞), so by the same Pringsheim argument κ_k(τ) < 0 for infinitely many k [the size |κ_k| ≈ 2(k − 1)!·R^{−k}|cos(kφ + φ₀)|,
R = |log((1−τ)/τ) + iπ|, from the two logarithmic singularities, is a heuristic transfer, not proved here].
(b) r = 2, diagonal points: F_{(n,n)} = −½∫_{−1}^{1−2τ} ((1 + t)/2)^{n−1} P_n(t) dt (P_n Legendre) — from ∂_s of the mixed part and
the Legendre generating function for the diagonal of 1/(1 − s(x + y) + sxy), which is (1 − 2s(2s − 1)z + s²z²)^{−1/2}.
[computed: `verify/rank_cumulants.py`, `verify/rank2_legendre.py`, logs alongside. First negative cumulant k = 6, 5, 5, 4, 4, 4, 3, 3
for τ = 1/20, 1/10, 1/5, 1/4, 1/3, 1/2, 2/3, 9/10; rank 2: first negative F_{(a,b)} at degree 18, 12, 9, 8, 7, 6, 5, 4 (e.g.
F_{(6,6)} = −3.42·10⁻⁴ at τ = 1/10); rank 3: degree 10 … 3, with F_{(1,1,1)} = κ_3 < 0 for τ > ½; the Legendre formula matches the
direct coefficients exactly, and sign(F_{(n,n)}) is periodic in n with period 2π/arccos(1 − 2τ): ++−− at τ = ½, +++−−− at τ = ¼,
period ≈ 9.8 at τ = 1/10 — the oscillation the non-real singularities predict. The function μ of the proof: its coefficients
equal the direct sums Σ_{a+b=n} F_{(a,b)} (n ≤ 24) and the first negative m_n is at n = 24, 17, 10, 7, 4 for τ = 1/20, 1/10, ¼, ½,
9/10 (`verify/rank2_mixed_diagonal.py`).]

**Proposition 2.2 (finite rank kills (B) on the real line)** [proved here]. If the g-prime norms of a discrete Beurling system
(multiplicities allowed) lie in a monoid Λ generated by finitely many λ_1, …, λ_r > 1, then for every ρ > 0 and x ≥ 2,
sup_{u∈[x,2x]} |N(u) − ρu| ≥ ρx/(2K + 2), K := Π_i(1 + log 2x/log λ_i) ≪ (log x)^r. So N − ρu ≠ O(u^θ) for every θ < 1.
*Proof.* Every g-integer norm lies in Λ, and |Λ ∩ [1, 2x]| ≤ K (exponent vectors a with Σ a_i log λ_i ≤ log 2x). The at most K + 2
points of (Λ ∩ [x, 2x]) ∪ {x, 2x} cut [x, 2x] into at most K + 1 pieces, one of length ≥ x/(K + 1); N is constant on its interior
while ρu grows by ≥ ρx/(K + 1), so |N − ρu| ≥ ρx/(2K + 2) at one of its ends. ∎ (Rung 1 is r = 1: the log-periodic sawtooth of §1.)

**Corollary 2.3 (the structural dichotomy)** [proved here, from 2.1–2.2]. A discrete system satisfying (B) with any θ < 1 has norm
monoid of infinite rank. On a free norm monoid of infinite rank, FLAT per-point bookkeeping (a(h) = τ·w(h) at every point) is exact
only for τ = 1 (Theorem 2.1), i.e. a(h) = w(h), and the two natural readings of that are:
(P) multiplicity one — each norm carries one g-integer (S8 with transcendental 1/ρ, s40 Lemma 1.3): the per-point count is the
τ = 1 flat target (realizable: it is the monoid itself), and ALL of the regularity is positional — which cells the norms fall in;
(M) τ = 1 with weights — a(h) = w(h) at every point (e.g. Π_p Z_{F_p[T]}(p^{−s}) = ζ(s − 1), each p carrying the rank-one necklace
system of Theorem 1.1 with m = q = p): realizable, but then the density and the zeros are those of the weighted monoid, and on the real
line the power dilation h ↦ h^κ (needed to turn weight w(n) = n^{κ−1} into a density) has jumps a(n) = n^{κ−1} = x^{1−1/κ} at x = n^κ,
so β ≥ 1 − 1/κ; exact integrality of n^{κ−1} for all n forces κ ∈ ℤ (for k > κ − 1 the k-th difference of n ↦ n^{κ−1} is an
integer tending to 0, hence eventually 0, so n^{κ−1} is eventually a polynomial), hence β ≥ ½ (κ = 2: ζ_P(s) = ζ(2s − 1), N_P(x) = Σ_{n≤√x} n,
β = ½, zeros on Re s = ¾ by Hardy's theorem [recalled, unverified], (A) fails since R(n²−) = −n/2). Every flat target with
τ ∈ (0, 1) is excluded by Theorem 2.1. So **the F_q mechanism (exact counts per norm point with slack) does not survive on the real
line**: in rank ≥ 2 a fixed fraction τ < 1 per point needs negative primes, and τ = 1 either is multiplicity one (no slack: one
integer per norm, regularity becomes the queue) or has jumps x^{1−1/κ} ≥ x^{½}.
*Remark (where the realizable dilations sit relative to U).* ζ(κ(s − 1) + 1) has zeros on Re s = 1 − 1/(2κ) (α = 1 − (1 − Θ)/κ,
Θ := sup Re of the zeros of ζ) and β = 1 − 1/κ; with Θ = ½, U's inequality 1 − 1/(2κ) ≤ max{½, 2 − 2/κ} holds for κ > 1 iff κ ≥ 3/2. The integer κ ≥ 2 that are exactly realizable obey U; the family would
cross U's line only for non-integral κ ∈ (1, 3/2), where exact realization is impossible — rounding n^{κ−1} to integers puts the
first-order term ±δ(p)·w(n/p) into the prime coefficient b(n) at squarefree n (from Σ_{π∋B}(−1)^{|π|−1}(|π| − 1)! = (−1)^{k−|B|}),
i.e. negative primes of the size of a whole jump, and a greedy repair of those is S5's multiplicity problem again (s39 §2).

## §3. The multiplicity regime on the real line: the candidate P_κ and why it fails

**3.0 The object** [definition; (A) proved here]. The closest real analog of the F_q greedy with slack per norm point: norm points n^κ
(n ∈ ℕ, κ > 1), g-primes at norm points with multiplicity b(n) ≥ 0, a(n) := g-integers at n^κ (formal products), N_D(n) := Σ_{m≤n} a(m)
= N_P(u) on [n^κ, (n + 1)^κ). Target T(n) := ⌈ρ(n + 1)^κ + r₀⌉ (so N_D(n) ≥ T(n) for all n IS (A) with r₀), per-point target
T(n) − T(n − 1) ≈ ρκn^{κ−1} = τ·w(n), τ := ρκ, w(n) := n^{κ−1} completely multiplicative. Greedy: c(n) := a(n) before the g-primes at n
are added, b(n) := max(0, T(n) − N_D(n − 1) − c(n)); E_D(n) := N_D(n) − T(n) ≥ 0. Then (A) holds by construction (if ρ2^κ + r₀ ≤ 1),
and sup_{[n^κ,(n+1)^κ)}(N_P − ρu) ≤ T(n) − ρn^κ + E_D(n) ≤ ρκ(n + 1)^{κ−1} + r₀ + 1 + E_D(n): (B) holds with θ = 1 − 1/κ iff
E_D(n) = O(n^{κ−1}). For κ < 2 and small ρ this θ is far below U's threshold ½·r₀/(r₀ + ρ) — the per-point slack of rung 1 restored.
[s39's S5 is the case κ = 1.]

**Lemma 3.1 (forced overshoot is rule-independent)** [proved here]. For ANY system on the norm points n^κ satisfying (A):
E_D(n) ≥ c(n) − (T(n) − T(n − 1)) for every n, because N_D(n) ≥ N_D(n − 1) + c(n) and N_D(n − 1) ≥ T(n − 1) (an integer count above
ρn^κ + r₀ is ≥ its ceiling). So (A) + (B) with exponent θ force c(n) ≤ ρκ(n + 1)^{κ−1} + 1 + O(n^{κθ}) at EVERY norm point.

**Proposition 3.2 (the cumulant forces excess at squarefree points)** [proved here]. Let h be squarefree in the norm monoid with k
generators (in ℕ: ω(h) = k), and suppose every proper divisor d of h has |a(d) − τw(d)| ≤ ε·τw(d). Then
a(h) ≥ (τ − κ_k(τ) − Err_k(τ, ε))·w(h), Err_k := Σ_{π ⊢ [k], |π|≥2} (|π| − 1)!·τ^{|π|}((1 + ε)^{|π|} − 1) → 0 as ε → 0.
*Proof.* Restricted to the divisors of h, the series is that of the Boolean lattice of its k generators, and the coefficient of
log at h is b(h) = Σ_{π ⊢ [k]} (−1)^{|π|−1}(|π| − 1)! Π_{B∈π} a(h_B) (h_B := product of the generators in B; for squarefree h
no proper power is involved). The term π = {[k]} is a(h); for the others insert a(h_B) = τw(h_B)(1 + δ_B), |δ_B| ≤ ε, and use
Π_B w(h_B) = w(h): the unperturbed sum is (κ_k(τ) − τ)w(h) (Theorem 2.1(a)), the perturbation is at most Err_k·w(h). Now b(h) ≥ 0. ∎
So when κ_k(τ) < 0 (k ≥ k₀(τ), the first negative cumulant: k₀ = 7, 6, 5, 4 for τ = 0.03, 0.075, 0.15, 0.30), a system that is
nearly flat below h overshoots AT h by ≥ (|κ_k(τ)| − Err_k)·w(h), whatever its rule; by Lemma 3.1 this enters E_D.

**3.3 The clipped-cumulant law, measured** [computed: `verify/pkappa.c`, `verify/clipped_cumulant_model.py`; logs
`pkappa_k1.5_r*_r04_1e7.log`, `pkappa_k1.5_r0.05_r04_1e8.log`, `clipped_cumulant_model.log`, `cumulant_predictions.log`].
The greedy cannot place negative primes. MODEL: at squarefree points with j generators it places b_j = κ_j(τ)w for j < k₀ and
b_j = 0 for j ≥ k₀ (measured mean b/target at j = 1, …, 5 for τ = 0.075: 0.88, 0.83, 0.72, 0.49, 0.14, against κ_j/τ = 1, 0.925,
0.786, 0.540, 0.132); the composite load at a squarefree point with k generators is then, in units of the per-point target,
C_k = (M_k − b_k)/τ with
M_k = k![t^k] exp(Σ_{j<k₀} κ_j(τ)t^j/j!). For κ = 1.5, squarefree n ∈ [Y/2, Y], Y = 10⁷ (mean c(n)/target by ω(n) = k):

| τ = ρκ | k₀ | measured C_k, k = 4, 5, 6, 7, 8 | model C_k, k = 4 … 8 | forced-overshoot fraction at k = k₀ − 1, k₀, k₀ + 1 |
|---|---|---|---|---|
| 0.03 | 7 | 0.131, 0.312, 0.700, 1.47, 2.93 | 0.199, 0.407, 0.778, 1.40, 2.42 | 0.004, 1.000, 1.000 |
| 0.075 | 6 | 0.481, 0.889, 1.44, 2.23, 3.62 | 0.460, 0.868, 1.47, 2.37, 3.89 | 0.290, 0.9998, 1.000 |
| 0.15 | 5 | 0.695, 1.25, 2.06, 3.58, 7.09 | 0.800, 1.32, 2.03, 3.25, 5.81 | 0.275, 0.914, 1.000 |
| 0.30 | 4 | 1.00, 1.56, 2.53, 4.45, 7.93 | 1.18, 1.70, 2.59, 4.41, 8.13 | 0.323, 0.710, 0.9997 |

(k = 8 rows rest on 1 point.) The onset of forced overshoot sits exactly at the first negative Bernoulli cumulant for every τ, and
the load follows the model within 10 % at k = k₀ − 1 and k₀ for all four τ (within 35 % on every entry; the model ignores the busy
periods, ≈ 3–19 % of points, in which the greedy places no primes at all). The model's ratio C_{k+1}/C_k grows (1.6 at k₀ to 3.7 at k = 24 for τ = 0.075): the
moments of exp(polynomial of degree k₀ − 1) grow like (k!)^{1 − 1/(k₀−1)}·Cᵏ [standard for entire functions of finite order; recalled,
unverified], so at the most factored points (k ≈ log n/log log n) the forced overshoot would be n^{1 − 1/(k₀−1) − o(1)}·w(n) — a
power of n, not a polylog [heuristic extrapolation, not proved].

**3.4 The queue of P_κ grows like a power** [computed: `pkappa_k1.5_r0.05_r04_1e8.log` (28 s, 1.2 GB), `pkappa_k1.2_r005_1e7.log`].
κ = 1.5, ρ = 0.05, r₀ = 0.4, to Y = 10⁸ (x = Y^κ = 10¹²): max E_D/n^{κ−1} per dyadic block of n = 0.102, 0.118, 0.142, 0.147, 0.187,
0.249, 0.304, 0.353, 0.426, 0.506, 0.626, 0.749, 0.923 (blocks from 1.2·10⁴ to 10⁸); on the last five blocks E_D/w grows by
2^{0.27}, 2^{0.25}, 2^{0.31}, 2^{0.26}, 2^{0.30} per doubling, i.e. E_D ≈ n^{0.78}, so E_P(x) ≈ x^{0.52} on [10¹⁰, 10¹²] — already above
every exponent U could use (½·r₀/(r₀ + ρ) = 0.444 here). The maximizers are the superior highly composite numbers 720720, 1441440,
2882880, 4324320 (ω = 6, 7); the busy fraction rises 4.3 % → 15.9 %; 91 % of the g-primes sit at composite n. κ = 1.2 (ρ = 0.05,
r₀ = 0.5, to 10⁷; per-point target only 1–2 integers, integrality dominates): E_D/w grows by 2^{0.12} per doubling, x-exponent ≈ 0.27
so far, with the same maximizers (1441440, 8648640). **Verdict on P_κ: not a candidate.** Its integer error is driven by the forced
overshoot of Proposition 3.2 at the most factored norms — the multiplicity mechanism that s39 found in S5 (κ = 1), now identified as
the sign pattern of the Bernoulli cumulants, i.e. as Theorem 2.1 acting on the real line; it does not depend on S5's rule (Lemma 3.1).

## §4. The multiplicity-one regime: the real-scale substitute is the Lindley recursion

**4.1 Dictionary** [proved here, from s40 Prop. 2.1 and the charter §2(a), re-derived: on a prime gap N grows only by composites].

| rung 1 (F_q, rank one) | real line, multiplicity one (S8) |
|---|---|
| degree n (one norm point qⁿ) | lattice cell (x_{k−1}, x_k], x_k = 1 + (k − ½)/ρ |
| target T_n = τqⁿ integers at qⁿ | target 1 integer per cell |
| composites C_n (from b_1, …, b_{n−1}) | c_k = composites in cell k (from g-primes < x_k/p₁) |
| b_n = T_n − C_n | a g-prime at x_k iff e_{k−1} = 0 and c_k = 0 |
| exact ⇔ C_n ≤ T_n for all n | exact (E ∈ (−½, ½]) ⇔ c_k ≤ 1 for all k (queue never busy) |
| slack per point T_n − C_n ≈ τqⁿ/n | slack per cell: 1 − mean(c_k) = g-primes per cell ≈ (1 − x^{−ρ})/(ρ log x) (template value), < 1 once ρ log x > 1 |
| no carry needed | carry e_k = max(e_{k−1} + c_k − 1, 0) (Lindley) |

So the real-scale substitute of b_n = T_n − C_n is the Lindley recursion, and the F_q slack (exponentially many integers per norm
point) becomes a slack of less than one integer per cell: the clip that is never active over F_q is active on a positive fraction
of cells (U7: busy cells with e_k > 0). Exactness on the real line means bounded one-sided discrepancy of the composites:

**Lemma 4.1 (no rule beats the composite discrepancy)** [proved here]. For any discrete Beurling system with E ≥ −c and any y ≤ x,
E(x) ≥ C[y, x] − ρ(x − y) − c, C[y, x] := composites in [y, x]. *Proof.* N(x) − N(y−) ≥ C[y, x] (g-primes only add), and
E(x) − E(y−) = N(x) − N(y−) − ρ(x − y), with E(y−) ≥ −c. ∎ S8 attains this within ½: E(x) = sup_{y≤x}(C[y, x] − ρ(x − y)) + r(x),
r ∈ (−½, ½] (s40 Cor. 1.4′, [quoted: `free-greedy-s40/theory/NOTE.md` l. 92–94]). So among never-undershooting systems with a given
composite set S8 is optimal to O(1); a better object must have better-spread composites, i.e. a different placement of its g-primes —
the domain of U1 (rules).

**4.2 The trade-off, stated** [from Theorem 2.1, Prop. 3.2, Lemma 4.1]. Slack per norm point and positivity of the prime measure
pull against each other on a free monoid of infinite rank: (M) many integers per norm point give F_q-type slack, but then a flat
fraction τ < 1 needs negative primes (Theorem 2.1) and the clipped system overshoots at the most factored points, by a load that grows
with ω (Prop. 3.2, §3.3–3.4); (P) one integer per norm point has no cumulant obstruction (τ = 1 is the free monoid itself) but no
slack either: per cell the margin is the prime density, less than one integer, and all the regularity must come from where the
products fall (Lemma 4.1). The F_q mechanism needs both at once — many integers per point AND rank one — and the real line with
(B) offers neither combination (Prop. 2.2).

## §5. Other structured classes, closed

**Lemma 5.1 (periodic integer counts violate (A) by ρ)** [proved here]. If N(u + L) = N(u) + ρL for all u ≥ 0 (N = 0 on [0, 1)), then
R((L + 1)−) = R(1−) = −ρ, so inf_{u≥1} R ≤ −ρ. This covers every system whose g-integers form a periodic subset of ℕ: ℕ, the odd
numbers, the integers prime to Q (finite deletions, s37 §5.3), and any periodic multiplicative subset.

**Lemma 5.2 (exact arithmetic progressions: only ℕ and the odd numbers)** [proved here]. If the g-integers of a Beurling system are
exactly the numbers 1 + kt (k ≥ 0), each counted once, then t ∈ {1, 2}. *Proof.* The least g-prime is 1 + t, and (1 + t)² = 1 + kt
forces t = k − 2 ∈ ℕ. So G = {n ≡ 1 mod t}, and "each counted once" means unique factorization into the atoms of this monoid. For
t ≥ 3: n_j := t·(p_1⋯p_j) − 1 ≡ −1 (mod t) is coprime to t and to p_1, …, p_j and has a prime factor ≢ 1 (mod t); so there are
infinitely many primes ≢ 1 (mod t), two of them, p ≠ q, in one class g ≢ 1 of order m ≥ 2. The numbers p^i q^{m−i} (0 ≤ i ≤ m) lie in
G and are atoms (a proper factor p^a q^b in G needs m | a + b with 0 < a + b < m), and p^m·q^m = (p^{m−1}q)(pq^{m−1}): two distinct
factorizations. ∎ [computed sanity check, t = 3 … 12: `verify/progression_atoms.py`.] Both survivors violate (A) (Lemma 5.1: R ∈ (−1, 0] for ℕ, (−½, ½] for the odd numbers). The S8 lattice itself,
1 + (k − ½)/ρ, is exactly realizable only as a SIGNED system (U5's L_ρ, [quoted: SHARED 17:16, U5 batch 1]).

**5.3 Non-adaptive structured prime sets** [quoted: `u-offsurgery-s39/NOTE.md` §3.2, l. 141–151, where Hilberdink 2005 Remark C is
quoted at the page]. If the g-primes track a template R with finitely many zeros, Π_P − Π_R = O(x^a) with a < ½, then β(P) ≥ ½.
Lattices, Beatty sets, block patterns or hierarchical choices fitted to a smooth prime density are of this kind; a structured design
can only escape through feedback from the integer count, which is §3 (multiplicity) or §4 (positions).

**5.4 Gluing** [proved here]. If P = P₁ ⊔ P₂ then ζ_P = ζ_{P₁}ζ_{P₂}, each factor an absolutely convergent nonvanishing Euler product
right of its abscissa σ_i. If σ₁, σ₂ < 1 then N_P = O(x^{max σ_i + ε}) has no linear term; so one factor (say P₁) has σ₁ = 1, and every
zero of ζ_P in (σ₂, 1) is a zero of ζ_{P₁}: the real zero of Theorem 1.6 must already be carried by a full-density component. Building
by independent blocks or several independent lattices does not create it.

## §6. Controls, gaps, untried

**6.1 Freeness is load-bearing — a second signed control** [proved here + computed: `verify/monoid_mN.py`]. The monoid
G_m = {1} ∪ mℕ is multiplicatively closed, N(u) − u/m = 1 + ⌊u/m⌋ − u/m ∈ (0, 1] (bounded, one-signed), and Z(s) = 1 + m^{−s}ζ(s) has
a real zero in (0, 1) (Z(0) = ½ > 0, Z(σ) → −∞ as σ → 1⁻): 0.4836, 0.5951, 0.7402, 0.8764 for m = 2, 3, 5, 10. It is not a
Beurling system: log Z has negative coefficients (first at 36 for m = 2, 3: −½, i.e. the 3 ordered factorizations 2·18, 18·2, 6·6
against one element), 156, 102, 42, 11 of them below 2000. Exact ADDITIVE bookkeeping gives integer error O(1) and a real zero right
of ½ for free; positivity of the prime measure at products is what it costs (compare U5's L_ρ on S8's lattice).

**6.2 Gaps.** (G1) The rule-independent form of §3 is not proved: *for every system on the norm points n^κ, 1 < κ < 2, satisfying
(A), sup_{n≤y} E_D(n)/n^{κ−1} ≥ y^δ for some δ > 0*. Proved: Lemma 3.1 (forced overshoot is c(n) minus the per-point target, for any
rule) and Prop. 3.2 (near-flatness below a squarefree point forces excess ≥ |κ_k(τ)|w at it). Missing: a lower bound for the
greedy's b at the divisors of the most factored n that survives the busy periods (the clipped-cumulant model ignores them; the data
fit it within 10 % at the onset). (G2) The growth (k!)^{1−1/(k₀−1)} of the clipped-cumulant load is quoted from the theory of entire
functions of finite order [recalled, unverified]; only the values to k = 24 are computed. (G3) Vivanti–Pringsheim is used as
recalled (standard); everything else in §1–§2 is complete on the page.
**6.3 Untried.** (a) A multiplicity rule that never places g-primes at squarefree points with ω ≥ k₀ − 1: it removes the clipped
load but changes the density's log power (the τ^{ω(n)} weighting of Selberg–Delange [recalled]); not run. (b) A positional system
with a degree grading (S8 whose g-primes of "degree d" are confined to [q^d, q^{d+1}) and spread by feedback): reduces to Lemma 4.1,
i.e. to U1's problem. (c) Exact realizability with τ > 1 (more than the weight per point): fails already in rank one for τ > 2
(F_2 = (1 − (τ − 1)²)/2 < 0); irrelevant here (τ = ρκ < 1).

