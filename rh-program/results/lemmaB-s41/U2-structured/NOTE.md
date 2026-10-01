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
every coefficient positive, so b_n ≈ a_n/n ≈ τ'qⁿ/n — an exponentially large slack per norm point that absorbs any target
correction of size o(qⁿ/n) (Prop. 1.2; data: the only failures are at n ≤ 3). §2 shows that (E3) fails for every norm monoid of
rank ≥ 2 and that finite rank kills (B) on the real line, so the F_q mechanism has no exact real-scale substitute.

## §2. Exactness is a rank-one phenomenon

Setting. H = free commutative monoid on generators g_1, …, g_r (r ≤ ∞), w > 0 completely multiplicative on H, τ ∈ (0, 1). The FLAT
target is T(1) = 1, T(h) = τ·w(h) (h ≠ 1): a fixed fraction τ of the weight at every point (rank one: T_n = τqⁿ, the template of
Theorem 1.1 with m = τq). It is exactly realizable iff there are b(d) ≥ 0 (d ∈ H \ {1}, real or integer) with
Π_d (1 − [d])^{−b(d)} = Σ_h T(h)[h], i.e. iff F := log(1 − τ + τΠ_i(1 − w(g_i)x_i)^{−1}) has F_h = Σ_{j: h = d^j} b(d)/j with all
b ≥ 0. Since F_h is a sum of b's with positive weights, ONE negative coefficient F_h already rules out realizability.
(w only rescales x_i, so signs are those of the case w ≡ 1.)

**Theorem 2.1 (flat bookkeeping needs rank one)** [proved here]. (i) r = 1: every coefficient of F is positive, F_n = (1 − (1 − τ)ⁿ)/n.
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
period ≈ 9.8 at τ = 1/10 — the oscillation the non-real singularities predict.]

