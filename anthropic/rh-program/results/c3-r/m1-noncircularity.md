# Castelnuovo–Severi/Hodge index on a surface from Riemann–Roch + ampleness: the non-circularity re-derivation

**Deliverable:** C3-r M1 — the non-circularity gate. Per the direction file and the binding
adjudication (`results/adjudication-C3.json`), **no C3-r substrate work may claim S4 credit
before this document exists**; it is the discharge, in writing, of the load-bearing [RU] flag
raised by the wave-1 arakelov scout ("the load-bearing non-circularity claim … should be
re-derived in the design phase").

**Status (read before citing).** This is a **re-derivation of standard material for the program
record; zero novelty is claimed.** Every statement below is graduate-textbook algebraic
geometry. Its value to the program is precisely the audit trail: the Hodge-index/
Castelnuovo–Severi inequality — the positivity engine of the only **positivity mechanism** that
has ever proved an RH† — is proved from Riemann–Roch on the surface, Serre duality, and
ampleness, **with no zeta-function, L-function, or RH input anywhere**. Both Session-6 killers
re-derived this argument independently; the lineage was tier-1-verified (killer-2 and the
adjudicator). The verification is recorded as "Verified in the brief's favor" in the direction
file's Phase-4 verdicts (`directions/C3-geometric-substrate.md`); the adjudication's own
wording is "the M1 gate is verified sound by both killers" (`results/adjudication-C3.json`;
`results/verdicts-c3d1.json` kill:C3 minor finding item (4), kill2:C3 minor finding item (1)).

† "Positivity mechanism" is the operative qualifier (restored per referee pass; it is the
direction file's own phrasing): RH for curves over finite fields was ALSO proved by the
elementary auxiliary-polynomial method of Stepanov (1969), streamlined and completed by
Bombieri, "Counting points on curves over finite fields (d'après S. A. Stepanov)," Sém.
Bourbaki Exp. 430 (1972/73), Springer LNM 383 (1974), 234–241 — a proof consuming only
Riemann–Roch on the *curve*: no surface, no Hodge index, no positivity engine. Deligne's
Weil I amplification is likewise a distinct engine. The claim above concerns the Hodge-index
positivity route only.

**Conventions.** X is a smooth projective (geometrically irreducible) surface over an
algebraically closed field k of **arbitrary characteristic** (char p included; nothing below is
characteristic-zero). Divisors are considered up to numerical equivalence where stated; K = K_X
is the canonical divisor; D·E is the intersection number; h^i(D) = dim_k H^i(X, O_X(D));
χ(D) = h⁰ − h¹ + h². "D numerically nontrivial" means D·E ≠ 0 for some divisor E. For a
non-closed base field, all quantities below are stable under base change to the algebraic
closure, so the inequalities descend; we work over k = k̄ throughout.

---

## 1. What is being certified and why

The C3-r mechanism template loads ALL of its Riemann-hypothesis content on a Hodge-index-type
inequality (S4). The known trap — enforced by barrier zoo IV.1 and the C1 precedent — is a
positivity step that is Weil positivity in disguise, i.e. an inequality whose proof secretly
consumes the statement to be proved. The function-field template is the existence proof that the
trap is avoidable: there, the master inequality has a proof whose inputs are
**Riemann–Roch on the surface, Serre duality, and ampleness** — nothing else. This document
re-derives that proof in full, itemizes the provenance of every input (§8), and states the
F_q-degeneration clause (§7): the inequality proved here is exactly the inequality Weil's proof
of RH for curves consumes, and it is proved before and independently of that application. That
is the non-circularity claim the direction leans on, now on paper rather than recalled.

## 2. Inputs, with provenance (and what is NOT an input)

The proof uses exactly the following, each a standard theorem with no analytic or arithmetic
content about zeta or L-functions:

- **(IN1) Riemann–Roch on a surface.** χ(D) = χ(O_X) + ½·D·(D − K). [Hartshorne, *Algebraic
  Geometry*, Thm. V.1.6; valid over any algebraically closed field.]
- **(IN2) Serre duality.** h²(D) = h⁰(K − D). [Hartshorne III.7.6.]
- **(IN3) Ample meets effective positively.** If H is ample and E is a nonzero effective
  divisor, then E·H > 0. [Degree of a nonzero curve in a projective embedding is positive;
  equivalently the easy direction of Nakai–Moishezon.]
- **(IN4) Ampleness absorbs any divisor.** For H ample and D arbitrary, D + nH is ample for all
  n ≫ 0. [Hartshorne, Exercise II.7.14(b); standard.]
- **(IN5) Trivial positivity.** h⁰, h¹, h² ≥ 0, hence h⁰(D) + h²(D) ≥ χ(D).
- **(IN6) The intersection pairing on Num(X)** is a well-defined, nondegenerate symmetric
  bilinear form on a finitely generated group. [Hartshorne V.1; nondegeneracy is the definition
  of numerical equivalence. Finite generation of Num(X) is the Néron–Severi theorem — proved by
  Picard-variety/finiteness arguments, no zeta input; it is consumed ONLY for ρ < ∞ in the
  signature statement §5, which sits off the load-bearing chain to §§6–7.]
- **(IN7) Nakai–Moishezon criterion (hard direction).** On a surface, if H² > 0 and H·C > 0 for
  every irreducible curve C ⊂ X, then H is ample. [Hartshorne Thm. V.1.10; the proof is
  cohomological (Riemann–Roch plus effectivity bootstrapping) — no zeta content. Consumed only
  in §6, to certify H = ξ₁ + ξ₂ ample. An elementary route avoiding it exists —
  m(ξ₁ + ξ₂) = p₁*(mP) + p₂*(mP′) is very ample for m ≫ 0 as the Segre-composed embedding of
  very ample divisors on the factors, an (IN4)-grade fact — but the criterion is what §6's
  printed verification uses, so it is listed as the input it is.]

**Not inputs:** the zeta function of any curve or surface; point counts; the Weil conjectures
in any form; positivity of any explicit-formula functional; any spectral or Hilbert-space
statement; any characteristic-zero comparison. No step of the proof (§§3–6) mentions them.
§7's degeneration clause consumes rationality and the functional equation of Z(C, T) —
Riemann–Roch-on-the-curve facts with no RH content — and produces point counts as OUTPUTS
(N₁ = Γ·Δ), exactly as itemized in the §8 ledger; §10 mentions the explicit formula only
inside the IV.10 fence, to state what the Tate-curve surfaces cannot host.

## 3. Lemma (effectivity criterion; Hartshorne V.1.8 lineage)

**Lemma.** Let H be ample on X and let D be a divisor with D² > 0 and D·H > 0. Then nD is
effective (h⁰(nD) > 0) for all sufficiently large n.

*Proof.* By (IN1), χ(nD) = χ(O_X) + ½·nD·(nD − K) = (n²/2)·D² − (n/2)·D·K + χ(O_X) → ∞ as
n → ∞, since D² > 0. By (IN2), h²(nD) = h⁰(K − nD). Since D·H > 0,
(K − nD)·H = K·H − n·(D·H) < 0 for all n ≫ 0; but h⁰(K − nD) > 0 would make K − nD linearly
equivalent to an effective divisor E ≥ 0 with (K − nD)·H = E·H ≥ 0 (zero only for E = 0,
positive otherwise by (IN3)) — impossible. So h⁰(K − nD) = 0 for all n ≫ 0, and by (IN5),
h⁰(nD) ≥ χ(nD) − h²(nD) = χ(nD) → ∞. ∎

*(This is the exact locus where the hypothesis D·H > 0 is consumed: it kills the h² term. The
compressed sketch recorded in the verdict files — "χ(nD) → ∞ forces ±nD effective" — silently
routes through this Lemma applied to an auxiliary ample divisor; the full route is Theorem 4.)*

## 4. Theorem (Hodge index; Hartshorne Thm. V.1.9 lineage)

**Theorem.** Let H be ample on X and let D be a divisor with D·H = 0 and D numerically
nontrivial. Then D² < 0.

*Proof.* Suppose for contradiction D² ≥ 0.

**Case 1: D² > 0.** By (IN4) choose m ≫ 0 with H′ := D + mH ample. Then
D·H′ = D² + m·(D·H) = D² > 0, so the Lemma applies to D with the ample divisor H′: nD is
effective and nonzero (D is numerically nontrivial, so nD ≢ 0) for some large n. By (IN3),
nD·H > 0, contradicting D·H = 0.

**Case 2: D² = 0.** Since D is numerically nontrivial, pick E with D·E ≠ 0. Replace E by
E′ := (H²)·E − (E·H)·H; then E′·H = (H²)(E·H) − (E·H)(H²) = 0 and
D·E′ = (H²)(D·E) − (E·H)(D·H) = (H²)(D·E) ≠ 0 (H² > 0 by (IN3): H ample ⟹ some multiple of H
is effective and nonzero, and it meets H positively, so H² = H·H > 0). For an integer n, set
D′ := nD + E′. Then D′·H = n·(D·H) + E′·H = 0 and
D′² = n²·D² + 2n·(D·E′) + E′² = 2n·(D·E′) + E′². Choosing n large with the sign of n·(D·E′)
positive gives D′² > 0 with D′·H = 0. If D′ is numerically nontrivial this contradicts Case 1;
and D′ numerically trivial is impossible since D′² > 0. Contradiction either way.

Hence D² < 0. ∎

## 5. Corollary (the signature statement)

**Corollary.** On Num(X) ⊗ R (rank ρ), the intersection form has signature (1, ρ − 1): it is
positive definite on the line R·H and negative definite on H^⊥.

*Proof.* H² > 0 gives the positive line. For the negative-definiteness of H^⊥: the Theorem
gives x² < 0 for every nonzero **rational** class x ∈ H^⊥ (clear denominators and apply the
Theorem to the resulting integral divisor class; numerical nontriviality is exactly nonvanishing
in Num). Negative *semi*definiteness on the real span follows by density and continuity of the
quadratic form. If some nonzero real x ∈ H^⊥ had x² = 0, then x would lie in the radical of the
semidefinite form restricted to H^⊥ (an isotropic vector of a semidefinite form is radical);
the radical is a rational subspace (the form and H^⊥ are defined over Q), so it would contain a
nonzero rational class y ∈ H^⊥ with y·z = 0 for all z ∈ H^⊥ and y·H = 0 — i.e. y numerically
trivial (write any w as λH + w^⊥), contradicting y ≠ 0 in Num(X) ⊗ Q. ∎

## 6. Corollary (Castelnuovo–Severi on C × C′)

Let C, C′ be smooth projective curves over k, S = C × C′, ξ₁ = {pt} × C′, ξ₂ = C × {pt}. Then
ξ₁² = ξ₂² = 0, ξ₁·ξ₂ = 1, and H := ξ₁ + ξ₂ is ample ((IN7) Nakai–Moishezon: H² = 2 > 0, and
every irreducible curve on S meets ξ₁ or ξ₂ positively and neither negatively). For a divisor D on S
write the **bidegree** (d₁, d₂) := (D·ξ₁, D·ξ₂) (for the graph Γ_f of a morphism f: C → C′,
(d₁, d₂) = (1, deg f)).

**Corollary (Castelnuovo–Severi inequality).** D² ≤ 2·d₁·d₂, with equality only if D is
numerically equivalent to d₂ξ₁ + d₁ξ₂.

*Proof.* Set D′ := D − d₁ξ₂ − d₂ξ₁. Then D′·ξ₁ = d₁ − d₁ = 0 and D′·ξ₂ = d₂ − d₂ = 0, hence
D′·H = 0. By the Theorem (and its trivial extension: D′² ≤ 0, with < 0 unless D′ ≡ 0),
0 ≥ D′² = D² − 2(d₁·(D·ξ₂) + d₂·(D·ξ₁)) + (d₁ξ₂ + d₂ξ₁)² = D² − 4d₁d₂ + 2d₁d₂ = D² − 2d₁d₂. ∎

The classical "equivalence defect" formulation and the positivity of Weil's trace form on
correspondences are algebraic reformulations of this inequality; the historical order (§9) ran
through exactly this statement.

## 7. The F_q degeneration clause: this is the inequality Weil's proof consumes

This section states, with the short computation, that the inequality of §6 — proved above from
(IN1)–(IN6) only — is the entire positivity input of Weil's proof of RH for curves over finite
fields. **That is the point of M1:** the same inequality the C3-r template must produce on an
arithmetic substrate is, in its home territory, proved with no RH input, so demanding an
RR + ampleness derivation (rather than a posited positivity) is a coherent, historically
grounded non-circularity contract.

Let C be a smooth projective geometrically irreducible curve of genus g over F_q, S = C × C
(base-changed to F̄_q for the intersection theory), F: C → C the q-power Frobenius, Γ = Γ_F its
graph, Δ the diagonal, N₁ = #C(F_q). The three standard geometric facts consumed — each an
intersection-theoretic computation with no zeta input:

- **(W1)** Γ has bidegree (1, q); Δ has bidegree (1, 1).
- **(W2)** Δ² = 2 − 2g (self-intersection = degree of the normal bundle N_Δ ≅ T_C) and
  Γ² = q(2 − 2g): via the embedding (id, F): C ≅ Γ ⊂ S one has T_S|_Γ ≅ T_C ⊕ F*T_C, so
  deg N_{Γ/S} = deg(T_S|_Γ) − deg T_Γ = deg F*T_C = q·deg T_C = q(2 − 2g).
- **(W3)** N₁ = (Γ·Δ): Γ and Δ meet transversally because dF = 0, so 1 is never an eigenvalue
  of the tangent map; the intersection points are exactly the F_q-rational points.

Apply §6 to D = rΔ + sΓ for integers r, s: bidegree (r + s, r + sq), and with t := (Γ·Δ),

D² = r²(2−2g) + 2rst + s²q(2−2g) ≤ 2(r+s)(r+sq).

Expanding and simplifying: g·r² − rs·(t − 1 − q) + g·q·s² ≥ 0 for all integers r, s, hence (by
homogeneity and density) for all real r, s; the discriminant condition gives

(t − (q+1))² ≤ 4g²q, i.e. **|N₁ − (q + 1)| ≤ 2g·√q.**

Replacing F by F^k gives |N_k − (q^k + 1)| ≤ 2g·q^{k/2} for every k ≥ 1; by the standard
power-sum/functional-equation bookkeeping (rationality of the zeta function of C and the α ↦ q/α
pairing — both consequences of Riemann–Roch on the *curve*, again with no RH input) this is
equivalent to |α_i| = √q for every Frobenius eigenvalue, i.e. RH for C. (The ⟹ direction is
the generating-function no-cancellation fact: the log-derivative generating function has
residue −m_α at T = 1/α, so poles at distinct points of equal modulus cannot cancel; the
uniform bound then forces radius of convergence ≥ q^{−1/2}, i.e. max_i |α_i| ≤ √q, and the
α ↦ q/α pairing pins equality.) Every input in this
chain is listed in §8; none is a zeta positivity.

**Consistency note with the M0 note (`results/c3-r/m0-axiom-note.md` §3.5).** The bidegrees
(1, q^k) of Γ_{F^k} are only the MAIN terms q^k + 1 of N_k; the zero side −Σα_i^k lives
exclusively in the Δ-intersection (W3). The positivity engine acts on the trace side through
§6's inequality — degrees alone never see a zero. (Numerically spot-verified in the
adjudication on y² = x³ + x + 1 over F₇: bidegrees (1,7), (1,49), (1,343) against counts
5, 55, 380.)

## 8. Non-circularity audit (step-by-step input ledger)

| Step | Uses | Provenance | Zeta/RH content |
|---|---|---|---|
| Lemma §3 growth of χ(nD) | (IN1) RR on surfaces | Hartshorne V.1.6 | none |
| Lemma §3 killing h² | (IN2) Serre duality + (IN3) | Hartshorne III.7.6; projective degree | none |
| Theorem §4 Case 1 | Lemma + (IN4) D+mH ample + (IN3) | Hartshorne Ex. II.7.14(b) | none |
| Theorem §4 Case 2 | (IN6) linear algebra in Num(X) | Hartshorne V.1 | none |
| Corollary §5 | Theorem + Q-rationality of Num | linear algebra | none |
| Corollary §6 (CS) | Theorem on C × C′ + (IN7) ampleness of H = ξ₁+ξ₂ | (IN7) Nakai–Moishezon, Hartshorne Thm. V.1.10 (cohomological proof) | none |
| §7 (W1)–(W3) | bidegree/normal-bundle/transversality computations | standard; dF = 0 | none |
| §7 discriminant step | §6 applied to rΔ + sΓ | quadratic forms | none |
| §7 closing equivalence | rationality + FE of Z(C, T) from RR on the curve | Weil rationality (RR-based) | none (no RH input; RH is the OUTPUT) |

**Statement of the non-circularity claim (the deliverable).** The Hodge-index/
Castelnuovo–Severi inequality on a surface, in any characteristic, is proved from Riemann–Roch
on the surface, Serre duality, and ampleness alone. No zeta function, no L-function, no point
count, no explicit-formula positivity, and no statement equivalent to or implied by any Riemann
hypothesis appears among its inputs. In particular, in the function-field template the
positivity engine is demonstrably **not Weil positivity in disguise**: it exists prior to, and
is consumed by, the RH proof — not conversely. This is the fact the C3-r S4 contract references,
and with this document on disk the contract's [RU] debt is discharged.

**Scope of the claim.** This certifies non-circularity of the *function-field template's*
engine. It does NOT assert that any arithmetic substrate exists on which the analogous
inequality can be derived (that is M2c/M3/M4, all open), and it confers no S4 credit by itself
on any substrate proposal — it is the gate such proposals must pass through, in the form: an
index inequality claimed on a substrate must be DERIVED from RR + effectivity/theta input on
that substrate and must degenerate to the present statement over F_q.

## 9. Lineage (as verified in the Session-6 adjudication cycle)

- **A. Mattuck, J. Tate**, Abh. Math. Sem. Univ. Hamburg 22 (1958) — the Castelnuovo–Severi
  inequality derived from Riemann–Roch on the surface (the first modern non-circular
  derivation; existence and content tier-1-verified this cycle).
- **A. Grothendieck**, "Sur une note de Mattuck–Tate," J. reine angew. Math. 200 (1958)
  208–215 — simplification and generalization: the inequality as an instance of the index
  theorem on an arbitrary surface (page range verified via Crelle/EuDML records this cycle).
- **R. Hartshorne**, *Algebraic Geometry*, GTM 52, Ch. V §1 — the textbook consolidation used
  above: Thm. V.1.6 (Riemann–Roch), Thm. V.1.9 (Hodge index), Thm. V.1.10 (Nakai–Moishezon,
  = (IN7)), Exercises V.1.9–V.1.10 (Castelnuovo–Severi on C × C′ and Weil's bound
  |N − (q+1)| ≤ 2g√q along exactly the route of §7). N.B. Hartshorne's theorem and exercise
  numbering are distinct series: "Thm. V.1.9" (the Hodge index theorem) and "Ex. V.1.9" (the
  CS exercise) are different items that happen to share a number. Two sub-item pins in this
  note — "Cor. V.1.8" for the effectivity criterion and the "(b)" of "Ex. II.7.14" — are
  recalled at the letter level only (the statements themselves are re-proved in full above, so
  nothing load-bearing depends on them); an online letter-check was attempted 2026-08-26
  without a conclusive page image, and a 30-second check against a physical copy remains
  worthwhile before print citation.

Verification record: both killers independently re-derived the argument of §3–§4 and confirmed
the lineage (`results/verdicts-c3d1.json` kill:C3 minor finding item (4); kill2:C3 minor
finding item (1) and its literature flag "Mattuck–Tate … and Grothendieck … verified to exist
with content as recalled — the brief's M1 [RU] is discharged"); the direction file's Phase-4
verdicts ("Verified in the brief's favor," `directions/C3-geometric-substrate.md`) record
"M1's [RU] non-circularity fact TRUE (Hodge index from RR + ampleness re-derived;
Mattuck–Tate Abh. Hamburg 22 (1958) + Grothendieck Crelle 200 (1958) 208–215 confirmed)";
the adjudication file's own wording is "the M1 gate is verified sound by both killers"
(`results/adjudication-C3.json`).

## 10. The E_p × E_p baseline remark (scoped by barrier zoo IV.10)

The only surviving contact between this gate and the former Tate-curve material is the
following remark, scoped strictly by `BARRIER-ZOO.md` IV.10. On the **diagonal** surfaces
E_p × E_p (E_p = C/(Z ⊕ Z·i·log p/2π) the per-prime Tate curve of arXiv:2606.06604;
End(E_p) = Z barring the unproven coincidence (log p)² ∈ 4π²Q), the Néron–Severi group is
generically Zξ₁ ⊕ Zξ₂ ⊕ ZΔ, and the index inequality of §4–§6 **holds classically** — these
are classical complex abelian surfaces and nothing in §3–§6 is special to them. But per IV.10
the available correspondence data on them is **prime-blind**: the graphs of multiplication-by-m
carry Lefschetz data deg([m] − 1) = (m − 1)² — integer polynomials in m with no log p weight —
so no intersection number on these surfaces can host the explicit formula's transcendentally
weighted prime terms without hand-inserting the answer key (barrier IV.1 re-entry). The
cross-prime surfaces E_p × E_q are dead as substrate (off-diagonal NS rank 2: no diagonal, no
graphs — zoo IV.10; M2b/N2 struck by the adjudication) and **nothing in this document revives
them**. The baseline therefore contributes to M1 exactly one sentence: the index inequality is
available on the diagonal Tate-curve surfaces for whatever classical purpose a future brief can
state — with zero prime-facing content, per IV.10.

## 11. Traceability

All paths relative to `anthropic/rh-program/`.

| Item | Source |
|---|---|
| M1 mandate; "gates all S4 credit"; [RU] flag origin | `directions/C3-geometric-substrate.md` (Milestone ladder M1; S4 row; adjudication + recommission sections) |
| Adjudicated verification of the argument and lineage | `directions/C3-geometric-substrate.md` Phase-4 verdicts ("Verified in the brief's favor"); `results/adjudication-C3.json` ("the M1 gate is verified sound by both killers"); `results/verdicts-c3d1.json` kill:C3 minor finding (4), kill2:C3 minor finding (1) + literature flags |
| Hodge-index proof skeleton as re-derived by the killers | `results/verdicts-c3d1.json` (both killers; reproduced here in full with the auxiliary-ample and D² = 0 steps made explicit — see the report note accompanying this deliverable) |
| F₇ spot-check numbers (1,7)/(1,49)/(1,343) vs 5/55/380 | `results/adjudication-C3.json` computation b |
| IV.10 scope of the E_p × E_p remark; (m−1)² Lefschetz data; NS ranks | `BARRIER-ZOO.md` IV.10; `results/adjudication-C3.json` computation a |
| Non-circularity contract language (derive from RR + effectivity; F_q degeneration clause) | `directions/C3-geometric-substrate.md` S4 row (f1-scout contract clause) |

*(C3-r M1 deliverable. Standard material re-derived for the record; zero novelty claimed.
U.S. English. Written Session 6, 2026-08-26.)*

---

## Referee pass + repairs (2026-08-26)

**Referee verdict** (`results/c3-r/referee-m1.md`, independent, same date): PASS WITH REPAIRS —
no fatal, 3 major, 6 minor. Every proof re-derived line by line; the input ledger verified
input-by-input with NO hidden zeta/L-function/RH content found anywhere; 13/13 numerical checks
pass (`results/c3-r/referee_m1_checks.py`); classical bibliography pinned online at page level.
All repairs below applied 2026-08-26.

- **MAJOR 1 (Nakai–Moishezon missing from the input list) — FIXED.** (IN7) Nakai–Moishezon
  criterion, hard direction [Hartshorne Thm. V.1.10; cohomological proof, no zeta content]
  added to §2, with the elementary Segre-embedding alternative noted; §6's invocation now tagged
  (IN7); the §8 ledger row for §6 updated to match. The listed-input route was chosen over
  rewriting §6 because the printed verification sketch uses the criterion, and the ledger
  already named it — §2, §6, and §8 now agree, and "exactly" in §2 is true.
- **MAJOR 2 ("No step below mentions them" falsified by §7/§10) — FIXED.** Scope sentence
  rewritten: no step of the PROOF (§§3–6) mentions the excluded items; §7 consumes rationality
  + FE of Z(C, T) (RR-on-the-curve facts, no RH content) and produces point counts as outputs;
  §10 mentions the explicit formula only inside the IV.10 fence.
- **MAJOR 3 (historical overclaim) — FIXED.** The "only POSITIVITY mechanism" qualifier
  restored in the status paragraph (the phrase's single occurrence in this note; a grep for
  variants found no second one), with the Stepanov–Bombieri footnote added: Stepanov (1969) /
  Bombieri, Sém. Bourbaki Exp. 430 (1972/73), LNM 383 (1974), 234–241 — an elementary RH-for-
  curves proof from RR on the curve, no surface, no Hodge index; Deligne's amplification noted
  as likewise distinct. Bombieri's exposé/volume/pages re-verified online this pass (numdam
  record SB_1972-1973__15__234_0; Springer LNM 383, 1974).
- Minor 1 (quote misattribution) — fixed in the status block, §9, AND the §11 row: "Verified
  in the brief's favor" now attributed to the direction file's Phase-4 verdicts; the
  adjudication cited for its own wording "the M1 gate is verified sound by both killers".
- Minor 2 (killer-1 tier-1 overstatement) — fixed: "both killers re-derived the argument; the
  lineage was tier-1-verified (killer-2 and the adjudicator)".
- Minor 3 (spurious "(IN1)" in §4 Case 2) — fixed: H² > 0 now credited to (IN3) alone.
- Minor 4 ((IN6) finite-generation provenance) — fixed: Néron–Severi theorem named inside
  (IN6), with the scope note that it is consumed only for ρ < ∞ in §5, off the load-bearing
  chain.
- Minor 5 (silent lemma in §7's closing equivalence) — fixed: the generating-function
  no-pole-cancellation clause added (residue −m_α at T = 1/α; radius ≥ q^{−1/2}; FE pairing
  pins equality).
- Minor 6 (numbering-coincidence guard + letter-checks) — fixed: §9 now states that
  Hartshorne's theorem and exercise numbering are distinct series. The two letter-level pins
  ("Cor. V.1.8", the "(b)" of Ex. II.7.14) remain recalled-only: an online letter-check was
  attempted 2026-08-26 (three targeted searches; no conclusive page image) and both are flagged
  in §9 as re-proved-in-full/non-load-bearing, pending a 30-second physical-copy check.

**Rejected/deferred:** none rejected. One residue deferred, exactly as the referee left it: the
two Hartshorne sub-item letter-checks above await a physical copy (non-load-bearing; both
statements proved in full in this note).

*(Repairs editor, Session 6+, 2026-08-26. With the three majors landed, this note is
external-circulation ready per the referee's §8 assessment; program-internal S4-gate use was
already sound.)*
