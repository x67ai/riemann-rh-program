# NOTE — unit `qtwin-s39`: the last corner of Q_cond — weighted, clustering Beurling systems with Riemann's exact FE at q > 1

Session 39, 2026-10-01. Writer: Opus 5.5 (unit agent). Status: IN PROGRESS — built section by section; §0 carries the close.
Conventions (as in `qcond-s38/NOTE.md`, cited "QC", and `novel-wave-s37/beurling-fe/NOTE.md`, cited "BFE"): every load-bearing
claim is (P) proved here, (C) computed in `verify/` with its log, or (Q) quoted from a file on disk at the line.
`[recalled, unverified]` carries no load. Novelty: `[novelty: single-check]`. Distance-from-upstream lines (10(n)) marked "UPSTREAM".

## 0. The question, the record, the digest (close stated in §0.4 once reached)

### 0.1 Setting (QC §1.1; BFE §3, §8(b))
dN ≥ 0 on [1, ∞) of polynomial growth, F(s) = ∫x^{−s}dN(x), Λ_F(s) = (q/π)^{s/2}Γ(s/2)F(s), and (A): Λ_F(s) = Λ_F(1 − s), poles
only at 0 and 1 (simple), growth (G′). Beurling: dN = exp*(dΠ), dΠ ≥ 0 on (1, ∞) (weights allowed, atoms and continuous part
allowed), so dN({1}) = 1. Scaled: ν := image of dN under t ↦ t/√q, r := q^{−1/2}, ρ_q := √q·Res_{s=1}F, and
μ_q := ρ_qδ₀ + ν + ν^∨ is a positive, even, tempered measure with μ̂_q = μ_q and μ_q|_{(−r,r)} = ρ_qδ₀ (QC §1.1).
Q_cond (the corner this unit owns): is there such a system at some q > 1?

### 0.2 The record (Q, QC at the line)
- QC Theorem U_q (§2.4, 218–238): u.d. generalized integers + (A) at any q ⟹ q = 1 and ζ (weights allowed).
- QC Theorem L′ (§2.3, 196–211): ζ·D, D a non-constant finite generalized Dirichlet polynomial, is never Beurling with (A), any q.
- QC Cor. E2 (§2.2, 175–182): ∫u^{−1}dΠ_c ≤ log ρ_q; no purely continuous solution at any conductor.
- QC §2.6(c) (297): "WEIGHTED or MIXED systems whose atom masses take infinitely many values: Meyer's theorem does not apply;
  only (a) is known." QC §2.6(d) (298–302), the SHAPE of a surviving solution: "an infinite atomic prime set whose generalized
  integers cluster (pairs arbitrarily close), with c ≤ ρ_q, a thin continuous part, and — if discrete and Q4 holds — integers
  spread over ≥ 2 radical classes and a decomposition F = Σ_ψ P̃_ψL_ψ with at least two primitive characters".
- QC Theorem D (§2.7, 322–335): every DISCRETE system with (A) at any q is ζ, conditional on Meyer's finite-values theorem (Q4),
  which QC had only second-hand. The primary is now on disk: `fetched-r9/r9-05-meyer-1970-LNM117.ocr.txt`, scan page 25 (§1 below).
- BFE Theorem T (§4, 104–133): conductor 1, dN ≥ 0 ⟹ ρζ. BFE T′ (§12, 340–347): two-system version. BFE §8(a) (206–213): continuous
  RH-false systems with double poles at a, 1 − a. BFE §11(iii) (333–336): the Euler-side inequalities (QC Prop. E makes them
  identities). read-O R1 (`beurling-fe/read-O.md` 204–219): the SIGNED self-dual solution at conductor 1 with a zero at
  1.32691 + 33.26351i — positivity is the rigidifying input.

### 0.3 The digest, quoted (Q: `novel-wave-s37/insights-digest.md`, SHA-256 e86f642a…)
§B5 (lines 151–154): "An RH-false object with Riemann's exact Γ-factor exists once any one hypothesis of Theorem T is dropped —
positivity (the signed R1 solution), the pole structure (continuous systems with double poles at a, 1 − a), frequencies ≥ 1
(Nakamura's f(s, χ)), or conductor 1 (F_{5,5}) — and the only drop not yet paid WITH Λ ≥ 0 and a discrete system is conductor
q > 1 (Q_cond; discrete systems with extra poles are the other open case, fe §8(d))."
§B6 (lines 158–160): "The Q-side location of the virtual curve is conductor q > 1, not conductor 1: over F_q the completed zeta's
'conductor' q^{2g−2} is minimal and rigid at g = 0 (Liouville) and V (g = 1) sits one step above; over Q the minimal conductor 1
is rigid (Theorem C) and T forbids a twin there."
§F.2 item 1 (lines 352–357): "**U2 — Q_cond** … Contract clause: 'a Beurling system (dΠ ≥ 0) with Riemann's exact FE at some
q > 1, verified by the Fejér test (a new Group-I control — the Q-side twin of V), or a rigidity theorem for every q in [1, Q₀] with
the infeasibility certificate on disk (or for all q)' … Why first: both outcomes are theorems; the construction branch gives the
program's first Q-side control with {Euler product, Λ ≥ 0, exact FE} (B5, B6); the refutation branch extends B1 to every
conductor (then {Euler product, Λ ≥ 0, exact Riemann FE at any conductor} has one model)."
QC answered this for u.d. systems (U_q) and, given Q4, for discrete ones (D); this unit owns the residue, QC §2.6(c).
