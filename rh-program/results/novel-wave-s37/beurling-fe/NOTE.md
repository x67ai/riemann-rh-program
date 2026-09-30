# NOTE — seed M1a `beurling-fe`: is Spec Z rigid among Beurling systems with Riemann's functional equation?

Session 37, 2026-09-30. Writer: Opus 5.5 (seed agent). Status: IN PROGRESS (sections are appended as they are finished).
Conventions: every load-bearing claim is (P) proved here, (C) computed in `verify/` with its log, or (Q) quoted from `sources/`
at the line. `[recalled, unverified]` marks recalled statements, which carry no load. Novelty claims are `[novelty: single-check]`.

## 0. Definitions and the question

A Beurling system is a multiset P = {1 < p₁ ≤ p₂ ≤ …} ⊂ R with p_j → ∞; its integers 𝒩_P = {n_k} are the multiset of finite
products (with multiplicity), n₀ = 1 (empty product). Write c(x) ≥ 0 for the multiplicity of x as a generalized integer,
N_P(x) = Σ_{n_k ≤ x} 1, ζ_P(s) = Σ_k n_k^{−s} = Π_j (1 − p_j^{−s})^{−1}, assumed absolutely convergent for Re s > 1.

(FE) ξ_P(s) := π^{−s/2} Γ(s/2) ζ_P(s) continues meromorphically to C, with poles only at s = 0 and s = 1, both simple, and
ξ_P(s) = ξ_P(1 − s); plus the growth condition (G): (s − 1)s·ξ_P(s) is entire of finite order (Hamburger's standing condition).

QUESTION (charter). Is P = {rational primes} the only Beurling system satisfying (FE)+(G)?

## 1. DRAFT (written the moment it was found; attacked in §4) — the Fejér argument

Let μ = ρδ₀ + Σ_k(δ_{n_k} + δ_{−n_k}) (multiplicity counted), n_k ≥ 1, and suppose μ is tempered with μ̂ = μ
(convention f̂(ξ) = ∫f(x)e^{−2πixξ}dx). Take φ(x) = (1 − |x|)₊, so φ̂(ξ) = (sin πξ/πξ)² ≥ 0, zero exactly on Z∖{0}.
Since supp μ ∩ (−1, 1) = {0} and φ(±1) = 0:   ⟨μ, φ⟩ = ρ.   And ⟨μ, φ̂⟩ = ρ + 2Σ_k (sin πn_k/πn_k)².
μ̂ = μ gives ⟨μ, φ⟩ = ⟨μ, φ̂⟩ (φ is not Schwartz: justified by mollification, §3), hence Σ_k sin²(πn_k)/n_k² = 0:
EVERY GENERALIZED INTEGER IS A RATIONAL INTEGER. Then μ is supported on Z, so μ̂ is 1-periodic; μ̂ = μ forces μ 1-periodic:
the mass at every n ∈ Z equals the mass at 0, i.e. c(n) = ρ for all n ≥ 1; c(1) = 1 gives ρ = 1 and 𝒩_P = N (each once).
So ζ_P = ζ and P = {rational primes}. No Euler product, no uniform discreteness, no Hamburger is used — only
(i) dN_P ≥ 0, (ii) supp dN_P ⊂ [1, ∞), (iii) exact self-duality. The same proof covers CONTINUOUS Beurling systems.
