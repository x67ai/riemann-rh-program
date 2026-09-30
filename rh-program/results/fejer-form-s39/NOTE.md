# NOTE — unit `fejer-form-s39`: the Fejér defect as a positive form transported to the zeros (Untried UT-4)

Session 39, 2026-10-01. Writer: Opus 5.5 (unit agent). Brief: `BRIEF.md` (SHA-256 35542ee1…). Written in order as results
land; §0 is filled at the close. Conventions as in the record: (P) proved here; (C) computed in `verify/` with its log;
(Q) quoted at the page from `sources/` or an on-disk source; `[recalled, unverified]` carries no load.

## 0. CLOSE (filled last)

(pending)

## 1. The object and the rung-1 setting (definitions; nothing new)

The candidate (digest §F.3 UT-4; fe/NOTE.md:317–319). M1a's Theorem T is the equality case of a Fourier-side LP inequality: for
a positive self-dual μ = ρδ₀ + dN + dN^∨ with the gap (−1, 1), pairing μ̂ = μ with the Fejér triangle φ = (1 − |x|)₊ gives
2Σ_k sinc²(n_k) = 0 — a positive form in the POSITIONS n_k of the generalized integers. UT-4 asks whether that form, carried to
the ZEROS, is a positivity generator (S4) that is not Weil's cone. The brief fixes the first rung: rung 1, the norm group q^Z.

Zeta data (proof-mine §4, verbatim definition). Z(u) = L(u)/((1 − u)(1 − qu)), L ∈ Z[u] of degree 2g, L(0) = 1,
L(u) = q^g u^{2g} L(1/(qu)); N_n = q^n + 1 − s_n ≥ 0 with s_n = Σ_i α_i^n (α_i the reciprocal roots); closed-point counts
b_d = (1/d)Σ_{e|d} μ(d/e)N_e ∈ Z_{≥0}; h = L(1) ≥ 1. Write α_j = √q e^{±iθ_j} (j = 1..g); θ_j is real iff RH holds for the
pair, and for V (q, t) = (5, 5) it is θ_V = i·log φ (φ the golden ratio; cos θ_V = √5/2, proof-mine §1). Normalized power
sums p_n := s_n q^{−n/2} = Σ_j 2cos(nθ_j) (real for every datum, genuine or not); p_0 := 2g.
Positions side (P). A_n := #effective divisors of degree n = coefficient of u^n in Z; Θ_n := (q − 1)A_n + h for n ≥ 0 and
Θ_n := h for n < 0 (on a curve, Θ_n = Σ_{deg c = n} q^{ℓ(c)} over the h classes of degree n). The FE of Z is equivalent to
Θ_n = q^{n−g+1}Θ_{2g−2−n} for all n ∈ Z (class-summed Riemann–Roch; proof: expand (q − 1)Z(u) + hΣ_{n<0}u^n and apply the FE
termwise — checked on every datum below, §4). This is the "discrete self-dual measure on q^Z" of the brief.
Controls (zoo I.9; brief). V: t = 5 over F₅ (RH-false, real off-line pair). E₀: y² = x³ + 2x over F₅, t = 4. V₂ and the 111
genus-2 data over F₅ with non-real off-line roots (proof-mine verify/twin_g2.log; o_twin.log). They are RH-FALSE: a separating
inequality must be VIOLATED by them. (The brief's parenthesis "E₀ and all 111 genus-2 / genus-1 data satisfy" is read as
"E₀ and all GENUINE genus-1 / genus-2 data satisfy"; the 111 are virtual, and §3 reports them as violators.)
