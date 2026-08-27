# The polarized-Frobenius axiom class: an S1 axiom statement with DH/Epstein witnesses (not a theorem)

**Deliverable:** C3-r M0 (axiom-format note), per the binding adjudication of 2026-08-26
(`results/adjudication-C3.json`, the mandatory repair beginning "Reprice M0 …"; recommission
order "C3-r" in `directions/C3-geometric-substrate.md`. Adjudication entries are cited by
quoted opening phrase throughout, never by array index).

**Status (read before citing).** This document is an **axiom statement plus a witness record**.
It is NOT a theorem, it is NOT "provable today," and it does NOT discharge the f1 scout's
"DH/Epstein have no F1-model" flag (which requires a formalized notion of F1-model and remains
open). The original "Lemma B" theorem framing of the C3 commission was killed by two independent
killer verdicts (blind replication) and upheld on adjudicator re-derivation
(`results/verdicts-c3d1.json` kill:C3 fatal 2, kill2:C3 fatal 1; `results/adjudication-C3.json`
computation b and the upheld killer finding beginning "Lemma B is not a theorem …"). What survives — per the adjudicator's partial
overrule of killer-1, via the referee's verified minor finding — is exactly this: **with
effectivity added as an axiom, the step-2 monoid computation under the degree reading is a
correct, cheap formal computation**, so the axiom-format note is a legitimate, nonzero
deliverable rather than pure re-dressing. The content remains quasi-definitional: it is barrier
zoo I.1's witness in a new dialect, whose sharper formal home is the Blomer–Leung
beyond-endoscopy **converse theorem** (zoo I.1; [BL26]). (**Dated correction, 2026-08-27:** this
sentence and the one in §7 previously read "Blomer–Leung monoid converse". The word *monoid*
belongs to the Braverman–Kazhdan/Ngô circle, not to Blomer and Leung: a case-insensitive count of
"monoid" in **both** arXiv versions of arXiv:2401.04037 — v1, 8 Jan 2024, and v2, 11 Jul 2026 — is
**zero**, with the split-hyphenation case checked and excluded. The gloss was this program's, and
is withdrawn as an attribution.)

> **DATED CITATION PASS (2026-08-27). Read before citing.** An independent novelty re-check
> (`results/arxiv/novelty-check.md`) returned **novel with citations** for this note and specified
> ~17 citation obligations. Every one was re-verified against a primary source before it was
> applied — Crossref, zbMATH Open, the arXiv abstract pages, the publishers' own records, and the
> program's on-disk corpus; the per-source evidence is in `results/arxiv/citation-verification/`.
> The result is the new §1.5 (prior art) and §10 (references), plus in-place citations. Four of
> the re-check's own claims did **not** survive verification and were **not** executed as written:
> (i) it asked to attribute `ψ_m ψ_n = ψ_mn` and "primitivity at the primes by unique
> factorization" to Borger arXiv:0906.3146 as printed text — that half is not in that paper, and
> only the ψ_p-Frobenius-family definition is quoted here; (ii) it read Deninger's item **2.3** as
> a trace axiom — 2.3 is the spectral axiom, **2.4** is the trace isomorphism, and the property his
> Theorem 2.13 actually refutes is **2.12**; (iii) it read Conrey–Li as an exemplar "on the same
> witness function χ₄" — their criterion fails for **ζ itself** as well, so the parallel is one of
> genre, not of a filter separating ζ from χ₄; (iv) it paired the Selecta *Geometry of the scaling
> site* with arXiv:1507.05818 — that preprint is the *Comptes Rendus* note; the Selecta preprint is
> arXiv:1603.03191. Two further corrections of record: Banaszak–Uetake's equivalence is to RH
> **plus simple zeros**, and "the only prior published axiomatization" is a universal negative that
> no source can establish, so §1.5 says "the closest prior work"; and the Montgomery–Vaughan
> pointer for the completely-multiplicative Euler product is **§1.3**, not §1.2.

**Role.** This note is the S1 **axiom citation** for C3-r and for every sibling direction that
wants to consume "multiplicativity as geometry" — nothing more. It supersedes the "LEMMA B
(target statement)" block of the C3 commission, which is retained verbatim in the direction file
as the immutable historical record.

---

## 1. Provenance and binding constraints

Every mathematical claim below was either (i) re-derived independently by both killers and the
adjudicator in the Session-6 cycle, or (ii) computed and stored on disk with exact closed forms.
The adjudication record is binding: claims the adjudication struck (theorem status, "provable
today," "discharges the f1 flag," any S1 credit beyond the axiom-format role) do not appear here
except in the negative. Consistency obligations: barrier zoo entries I.1, I.2, I.7, III.21, and
IV.10 (`BARRIER-ZOO.md`), each engaged explicitly below.

## 1.5 Prior art and what is new (added 2026-08-27)

Six lines of published work stand upstream of this note. Each is named here, with the
differentiator, so that no part of §§2–7 is mistaken for a discovery. Full references in §10.

- **Λ-rings (Borger [Bor09]).** A commuting family of Frobenius endomorphisms indexed by the
  primes is, in Λ-algebraic geometry, a *definition*, not an axiom. (PF2)+(PF3) are that
  definition; this note claims nothing there.
- **The square, in characteristic one (Connes–Consani [CC16]; Connes [CE15]).** The polarized
  square with fiber classes, the Frobenius family with its composition law, and the diagnosis
  that intersection theory and Riemann–Roch are what is missing, are all in print. The
  differentiators are stated at (PF1) in §2: a divisible index monoid **R**^×₊ with no
  primitivity notion, no nef-degree calculus, no effectivity axiom, and a characteristic-one
  semi-ringed topos rather than an adelic curve.
- **Absolute Descartes powers (Manin [Man95]).** "Spec **Z** × … × Spec **Z**" as an absolute
  power, and "a canonical absolute Frobenius", are Manin's, from 1995 — thirty years before this
  note's vocabulary.
- **The genre: no-go theorems about an explicitly stated axiom class (Deninger [Den22]).** This
  note's genre is not new either. Deninger states the expected properties of a real-coefficient
  "Weil-"cohomology for an arithmetic curve as numbered items 2.1–2.12 and then proves
  (Theorem 2.13) that no such theory exists. The parallel is exact at the level of method — state
  the axioms, then show what they cannot do — and the differentiator is the conclusion's strength:
  his is an impossibility theorem, this note's is a **vacuity** certificate at coefficient level.
  (Precision, verified 2026-08-27: the property his Theorem 2.13 refutes is **2.12**, the
  Galois-equivariant order-of-vanishing property, not his spectral axiom 2.3 and not his
  positivity hypothesis 2.7.)
- **Taking an RH axiom framework seriously (Flach–Morin [FM20]).** The precedent for treating a
  conjectural RH framework as an object of study and working out what it does and does not give:
  they conjecture a long exact sequence tying Deninger's conjectural cohomology to Weil–Arakelov
  cohomology, and prove it for smooth projective varieties over finite fields with finitely
  generated Weil-étale motivic cohomology.
- **The closest prior work: an axiomatized intersection calculus for zeta (Banaszak–Uetake
  [BU1, BU2, BU3]).** They introduce axioms (INT1–INT3) for an abstract intersection theory
  attached to a Hilbert-space operator and prove them equivalent to RH for that operator; in the
  sharp form, for the operator attached to L(s, χ) — for Γ = SL₂(**Z**), to ζ itself — "RH for
  L(s, χ) together with simplicity of all its nontrivial zeros holds if and only if a standard
  model exists" [BU2, Thm. 5.4], and they say so themselves: *"The existence of this model is
  equivalent to the RH (plus the simple zero conjecture)"* [BU3, §1]. **The differentiator is the
  polarity.** Theirs is an abstract axiom set whose *existence* is RH-equivalent — non-vacuous but
  circular, and it buys no exclusion. This note's is a concrete axiom set whose coefficient-level
  consequences are **provably satisfied by RH-false objects** (§7, Beurling/DMV) and **provably
  violated by an RH-true one** (§6.3, χ₄) — vacuous as an RH filter, and the vacuity is certified
  rather than conjectured. ("The closest prior work" is deliberate: "the only prior published
  axiomatization" is a universal negative over the literature that no search can establish, and
  the 2026-08-27 verification declined to assert it.)

**What is new here, then, is exactly three things:** the *conjunction* (PF1)–(PF6) as a printed
axiom class over a Chen–Moriwaki adelic curve with a Yuan–Zhang nef polarization; the
**definitional fork** of §3, which shows the D-attachment clause admits exactly two readings and
that both make the DH/Epstein exclusion definitional; and the **vacuity certificate** — the
P¹×P¹ system of §3.2 satisfying (PF1)–(PF4) while touching no coefficient of any D, together with
the §6 witnesses and the §7 Beurling clause. Nothing else in this note is claimed as new.

## 2. The axiom class (repaired definition)

Let S = (K, (Ω, ν), (|·|_ω)) be a **proper adelic curve** in the Chen–Moriwaki sense
(arXiv:1903.10798; "proper" = the product formula holds). A **polarized Frobenius system** for a
Dirichlet series D(s) over S consists of:

- **(PF1) Polarized square.** A fibered square X over S carrying a nef adelic Q-line bundle L̄
  in the Yuan–Zhang adelic-line-bundle calculus (arXiv:2105.13587 v9; Annals of Mathematics
  Studies 221, 2026 — corrected 2026-08-27 from “223”, which is a different volume), with the two fiber classes ξ₁, ξ₂ and a correspondence composition ∘ and
  transpose t.

  *Prior art for (PF1), and the differentiators.* The polarized square with fiber classes, and the
  basic fact this note's §5 chain uses — "if D is a strictly positive divisor then
  D·ξ₀ + D·ξ₁ > 0" — are printed in Connes' essay [CE15, §2.3]; the Frobenius monoid over **N**^×
  with its composition law is [CE15, §4.3.1]; and §4.3.2 there states this note's own §7 diagnosis
  verbatim: *"At this point, what is missing is an intersection theory and a Riemann-Roch theorem
  on the square of the arithmetic site."* Moreover the square itself **exists** in characteristic
  one: Connes–Consani [CC16] realize Frobenius correspondences as congruences in the square of the
  arithmetic site and prove Ψ(λ) ∘ Ψ(λ′) = Ψ(λλ′) (their Theorem 1.2, restated as Theorem 7.7).
  Four differentiators separate that from the class printed here, and they are stated rather than
  left to the reader: (a) their correspondences are indexed by **R**^×₊, which is *divisible*, so
  "primitivity at the primes" — the whole content of (PF3) — has no analogue there (the essay
  keeps the two index sets apart: **N**^× for the Frobenius endomorphisms of the structure sheaf,
  **R**^×₊ for the correspondences Ψ(λ) on the square); (b) there is no nef-polarization degree
  calculus; (c) there is no effectivity axiom; (d) the ambient object is a characteristic-one
  semi-ringed topos, not an adelic curve in the Chen–Moriwaki sense — the phrase "adelic curve"
  does not occur in [CC16].
- **(PF2) Frobenius family.** A family of correspondences {Ψ_n}_{n≥1} on X with Ψ₁ = Δ (the
  identity correspondence).
- **(PF3) Composition law and primitivity.** Ψ_m ∘ Ψ_n = Ψ_mn for **all** m, n ≥ 1, and Ψ_p is
  primitive (not a composition of non-identity members) exactly at the primes p.

  *Prior art for (PF2)+(PF3), stated so that no novelty is implied at this point.* Borger's
  Λ-algebraic geometry already makes a family of this kind a **definition** rather than an axiom:
  for X flat over **Z**, a Λ-structure on X *is* "a commuting family of endomorphisms
  ψ_p : X → X, one for each prime p, such that ψ_p agrees with the p-th power Frobenius map on
  X ×_{Spec Z} Spec **F**_p" [Bor09, §1.1], and the Λ-ideals there are "ordered by divisibility on
  m" [Bor09, §6], which is the standard Λ-ring composition law. What this note adds at (PF2)+(PF3)
  is nothing; what it adds is the polarized square (PF1), the effectivity clause (PF4), and the
  D-attachment clause (PF6) — and the demonstration, in §3, that the attachment cannot be
  formalized innocently. (The specific identity `ψ_m ψ_n = ψ_mn` is *not* printed in
  arXiv:0906.3146 — that paper defers the general-m construction to Borger's Witt-vector papers —
  so it is not quoted against that reference.)
- **(PF4) Effectivity** *(axiom added by the adjudicated repair; the original definition omitted
  it and its step 3 is false without it — general correspondence classes are differences of
  effective ones and can have negative degrees)*. Every Ψ_n is effective.
- **(PF5) FE/duality (transpose/Rosati-type)** *(axiom added by the adjudicated repair; the
  original definition's "closed under transpose" was never tied to the Ψ_n by any axiom)*. The
  family is stable under transpose, and a fixed Rosati-type identity ties Ψ_n^t to Ψ_n through
  the polarization L̄, whose numerical shadow is the s ↦ 1−s (eigenvalue α ↦ q/α) symmetry of
  the functional equation of D. Template: in characteristic p the functional equation IS
  Rosati/Poincaré duality, relating Γ_F^t to the dual "q/F" (Γ_F^t ∘ Γ_F = q·Δ for the purely
  inseparable Frobenius F of degree q). Over an adelic curve this axiom is stated here at
  template level only: **no candidate substrate currently instantiates it for any D**, and this
  note makes no claim about how a sharpened transpose axiom would cut down the model class of
  §3.2 (unadjudicated).
- **(PF6) D-attachment.** The counting data of D(s) is reproduced by the system. This clause is
  the definitional joint, and it cannot be formalized innocently: §3 shows that every reading
  makes the DH/Epstein exclusion **definitional**, which is why this document is an axiom
  statement and not a theorem.

**PF5 status (read together with §3.2 and §7).** Two bookkeeping facts about (PF5), stated here
so that no reader has to assemble them: **(a)** PF5's transpose-stability clause already fails
for the model system of §3.2 — Γ_{z↦z^n}^t has bidegree (n, 1), which is not the bidegree
(1, m) of any Γ_m — so that exhibit certifies vacuity of the **(PF1)–(PF4) fragment**, and no
transpose-stable instantiation of the full six-axiom class is currently known for any D. This
is consistent with PF5's uninstantiated-template status and changes nothing in the fork of §3:
Horn A's steps 1 and 3 do not use the exhibit. **(b)** In the §7 accounting, PF5 is excluded
from "the axiom a DMV world violates" because it is an uninstantiated template contributing no
operative, checkable coefficient-level consequence. If its FE **shadow** were instead imposed
directly on D as an analytic requirement, FE-free Beurling systems would fail it — but that
would be an analytic condition inserted by hand, not an axiom any substrate enforces, and the
class would still sit below the I.7 bracket (no Ramanujan input, no degree-one-rigidity
derivation). The positivity-filter classification and the relocation order of §7 are unchanged
either way.

## 3. Why this is an axiom statement and not a theorem: the definitional fork

### 3.1 Preliminary: bidegrees multiply under composition; traces do not

For correspondences on a square, the bidegrees (d₁, d₂) = (Z·ξ₁, Z·ξ₂) are multiplicative under
composition: d_i(Ψ′∘Ψ) = d_i(Ψ′)·d_i(Ψ) (over a generic point the fibers compose; verified on
graph models, four pairs, adjudication computation b). Intersection numbers against the diagonal
are NOT: (Ψ′∘Ψ · Δ) is not a function of (Ψ′·Δ) and (Ψ·Δ). Concretely, on P¹×P¹ with
Γ_n = graph(z ↦ z^n): (Γ_n·Δ) = n+1, verified two ways (numerical classes: Γ_n ≡ nξ₁+ξ₂,
Δ ≡ ξ₁+ξ₂, product = n+1; fixed points of z^n = z: the n−1 roots of z^{n−1} = 1 plus 0 and ∞).
And n+1 is not multiplicative: (Γ₆·Δ) = 7 ≠ 3·4 = (Γ₂·Δ)(Γ₃·Δ).

### 3.2 Horn A — the degree reading

Read (PF6) as: *the degrees of the Ψ_n against the two fibers reproduce the counting data of D*
(the reading the original commission's own template sentence mandated). Then:

1. By §3.1 the attached degree data is **completely multiplicative by definition** — an Euler
   product is forced by (PF3) before any geometry is consulted.
2. **The class touches no coefficient of any D.** The system X = P¹×P¹ over the adelic curve of
   Q with the standard nef bundle O(1,1) and Ψ_n = Γ_{z↦z^n} satisfies every axiom
   (PF1)–(PF4): Ψ_m∘Ψ_n = Ψ_mn exactly, Ψ_p primitive exactly at primes, every Ψ_n an effective
   irreducible curve, bidegrees (1, n). Nothing in (PF1)–(PF4) references the coefficients of D,
   so the identical system would serve D = ζ, D = DH, or D = Epstein indifferently. Nor is the family new as a *Frobenius* family: on the roots-of-unity locus, z ↦ z^n is
   precisely the Bost–Connes endomotive's endomorphism σ_n : e(γ) ↦ e(nγ), whose composition law
   σ_nm = σ_n σ_m is this note's (PF3), and Connes, Consani and Marcolli treat exactly these maps
   as Frobenius correspondences over **F**₁ — *"the endomorphisms σ_n describe the Frobenius
   correspondence, in the sense that on the algebra **Z**[**Q**/**Z**] ⊗_**Z** K, for K a perfect
   field of characteristic p > 0, the endomorphisms σ_n, n = p^ℓ (ℓ ∈ **N**) coincide with the
   Frobenius correspondence"* [CCM09, Thm. 6.2(b); for general n the weaker §6.1 statement, that
   the σ_n are the Ẑ-powers of the Frobenius of **F**₁^∞/**F**₁]. Citing this **strengthens** the
   vacuity point: the graph packaging on P¹×P¹ is what this note adds, and it is what makes the
   degree bookkeeping computable — and, as this section shows, worthless. (The word "graph" does
   not occur in [CCM09]; they work with σ_n on the pro-variety μ(∞) = lim μ(n), not with a graph
   correspondence on a surface.) (Both
   killers constructed this counterexample independently; adjudicator re-verified. The printed
   (PF5) already excludes it — its transpose-stability clause fails, Γ_n^t having bidegree
   (n, 1), not any Γ_m — so the exhibit certifies vacuity of the (PF1)–(PF4) fragment; see the
   PF5 status paragraph, §2. Whether some sharpened transpose axiom would cut down the model
   class further is not adjudicated and not claimed.)
3. Therefore, under Horn A, "reproduce the counting data of D" must itself be an **axiom — an
   admissibility condition on D**, not a property the geometry proves. Under that admissibility
   axiom, prime-power support and Λ_D ≥ 0 follow by the correct, cheap monoid computation of §5
   — **quasi-definitionally**: the only geometric ingredient consumed is that degrees of
   effective correspondences against a nef class are ≥ 0, which is a basic property of
   the Yuan–Zhang calculus, not a theorem being put to work.

### 3.3 Horn B — the trace reading

Read (PF6) as: *the counting data of D is reproduced by intersection against the diagonal,
(Ψ_n·Δ)-type numbers* — the only reading matching where counting data actually lives in the
char-p template (§3.5). Then the original step 2 ("composition law + primitivity ⟹ prime-power
support; formal monoid algebra; no analysis") is **false as a formal claim**: by §3.1 trace data
does not factor through composition ((Γ₆·Δ) = 7 ≠ 12 on P¹×P¹), and no formal argument forces
(Ψ₆·Δ)-type data to vanish. What is needed is a **Lefschetz-tie axiom** ("the counting data of D
is trace-organized by the monoid") — in characteristic p that tie is a THEOREM about the
existing cohomology (the Grothendieck–Lefschetz trace formula); over Q it is exactly the missing
substrate (M2). **Positing such a tie as an axiom rather than proving it is not new:** Deninger
[Den98] put a conjectural Lefschetz-type trace formula of exactly this shape in print in 1998 —
twenty-eight years ago — tying the zeros of zeta and motivic L-functions, as eigenvalues of a flow
generator on H¹, to the closed orbits of a foliated dynamical system, and noting that the formula
"does not seem to be established" [Den98, §4]. His setting (leafwise cohomology of a foliated
dynamical system) is not this note's (counting data of an arithmetic correspondence read against
the diagonal in a Yuan–Zhang-style calculus), so the two are the same *move*, not the same
statement; the precedence is what is being cited. Adding it as an axiom
makes the D-attachment Euler-organized by definition, so the DH/Epstein exclusion again follows
from the definition plus the one-line coefficient witnesses of §6 — definitional once more.

### 3.4 Exhaustiveness of the fork

The primary dichotomy is formal, not empirical: the counting functional attached by (PF6)
either **factors through composition** — through composition-multiplicative invariants
(bidegrees and monomials in them; equivalently the induced action on H⁰/H²) — which is Horn A;
or it **does not**. Any non-multiplicative reading whatsoever — the H¹ trace or any other —
breaks step 2's formal monoid algebra and therefore needs an organizing tie axiom, which makes
the exclusion definitional: Horn B's analysis applies verbatim to all of them. The
H⁰/H²-versus-H¹ trichotomy is the template interpretation of this split (in every known
template the zero side IS the H¹ trace), not the load-bearing case division. Under Horn A the
statement is an admissibility definition; under Horn B it needs a Lefschetz-type axiom that
makes it an admissibility definition. Hence: axiom statement, on every branch. (Both killers,
independently; upheld in adjudication.)

### 3.5 The char-p accounting, corrected

The commission's template sentence ("the char-p model — degrees of graph-of-Frobenius powers on
C × C reproducing point counts — is the template") was **factually wrong** and is corrected here.
On C × C over F_q, the bidegrees of Γ_{Frob^k} are (1, q^k) — these are only the **main terms**
of #C(F_{q^k}) = q^k + 1 − Σ_i α_i^k. The zero side −Σ_i α_i^k lives **exclusively in the
Δ-intersection** (Lefschetz: N_k = (Γ_{F^k}·Δ)); degrees never see it. A degree-based reading is
therefore structurally blind to zeros. Numerically verified in the adjudication (computation b)
on E: y² = x³ + x + 1 over F₇: bidegrees (1, 7), (1, 49), (1, 343) versus counts
N₁ = 5, N₂ = 55, N₃ = 380 (Frobenius trace a = 3: α+β = 3, αβ = 7).

## 4. The scope restriction: total multiplicativity pins degree-one Euler shape

(PF3) demands Ψ_m ∘ Ψ_n = Ψ_mn for **all** m, n — not merely coprime pairs. Two consequences,
both stated here as adjudicated obligations:

- **(a) Degree-one Euler shape.** Matched at the level of the Dirichlet coefficients a_n of D,
  totally multiplicative coefficient data is exactly the Euler shape
  D(s) = Π_p (1 − a_p p^{−s})^{−1} — **degree one**. (This equivalence is textbook: Apostol
  [Ap76, Ch. 11], or Montgomery–Vaughan [MV07, §1.3, Thm. 1.9, p. 20], who say "totally
  multiplicative" where Apostol says "completely multiplicative". It is cited by chapter and
  section, not put to work as a theorem.) The axiom class as printed excludes every
  higher-degree Euler-intact L-function (e.g. ζ_K for a quadratic field K has degree-2 Euler
  factors and non-totally-multiplicative coefficients; it satisfies the coefficient-level
  consequence class of §5 but not the printed degree-one shape). A relaxed composition law
  (e.g. coprime-only multiplicativity plus per-prime tower data) is NOT provided by the printed
  axioms; any future widening is new design, outside this note.
- **(b) Relation to the one-generator function-field monoid.** The char-p template's Frobenius
  monoid is generated by ONE element: {Γ_{F^k} : k ≥ 0} ≅ (N, +), indexed by the exponent k
  (the extension degree), with a single "prime." The printed multi-prime monoid {Ψ_n} over
  (N^×, ·) — free commutative on all rational primes — is a different object: the commission's
  template was a one-prime template misread as a multi-prime one. (The multiplicative monoid **N**^× acting on a half-line is itself a live object in this
  literature: the **scaling site** is the semidirect product of the half-line by that monoid
  [CC16b, CC17], and its complex lift is [CC19].) Total multiplicativity across
  distinct primes is exactly the new, restrictive content: at coefficient level it pins the
  degree-one Euler shape (a); if instead the degree data were matched against Λ-type
  (prime-power-supported) counting data directly, complete multiplicativity would contradict
  vanishing at products of distinct primes (c_pq = c_p·c_q ≠ 0 whenever two primes carry
  nonzero data) unless at most one prime carries data — i.e. exactly the one-generator char-p
  monoid again. (Both killers; referee minor finding; upheld.)

## 5. The admissibility axiom and the exclusion computation (the correct cheap part)

**Definition (admissible D).** D(s) = Σ a_n n^{−s} (a₁ = 1) is *admissible* for the
polarized-Frobenius axiom class if, writing −D′/D(s) = Σ_n Λ_D(n) n^{−s}, the counting data
satisfies: **Λ_D is supported on prime powers and Λ_D(n) ≥ 0 for all n** (with the FE/duality
clause (PF5) named as a further requirement whose substrate-level content is currently
uninstantiated). In the strict printed (degree-one) shape, Λ_D(p^k) = a_p^k · log p with
a_p ≥ 0.

**The computation (correct, cheap, and quasi-definitional).** Under Horn A plus the
admissibility axiom, the attachment functional is fixed explicitly:
**a_n := d₂(Ψ_n) = (Ψ_n · ξ₂), the second-fiber degree** — the char-p analog of
deg F^k = q^k. (This is the multiplicative choice: by §3.1 the individual bidegree components
d_i, and monomials in them, are monoid homomorphisms under composition, whereas the degree
against the polarization itself — an (ξ₁+ξ₂)-type pairing — is NOT: on graphs,
(1+n)(1+m) ≠ 1+nm. Everything below runs verbatim for any declared multiplicative monomial in
the bidegrees; nothing below may be read against the non-multiplicative polarization pairing.)
(PF3) then makes n ↦ a_n = d₂(Ψ_n) a monoid homomorphism, i.e. totally multiplicative, forcing
the degree-one Euler shape (§4a); primitivity places the generators exactly at the primes;
hence −D′/D has Λ_D(p^k) = a_p^k log p and Λ_D(n) = 0 off prime powers — formal monoid
algebra, no analysis. (PF4) effectivity plus (PF1) nefness gives a_p = d₂(Ψ_p) = (Ψ_p·ξ₂) ≥ 0,
because ξ₂ is nef and Ψ_p is effective, hence Λ_D(n) ≥ 0. This is the step-2/step-3 chain the
referee verified by writing out the monoid computation, valid **once effectivity is an axiom**
— and it is an unpacking of the definition, not a theorem about D: the geometry contributes
only "nef against effective is ≥ 0."

**What would restore theorem status.** Nothing currently available: a genuine exclusion theorem
would require a substrate on which the Lefschetz tie of §3.3 is *proved* rather than posited —
i.e. M2. Until then the correct citation form is: "D is inadmissible for the polarized-Frobenius
axiom class [this note, §5–6]," never "D admits no polarized Frobenius system [theorem]."

## 6. The witnesses (exact)

All values below are on disk with exact closed forms; sources in §9. "Inadmissible" always means:
fails the §5 admissibility condition, with the named witness.

### 6.1 Davenport–Heilbronn (RH-false, and inadmissible)

*Sources.* The function and its off-line zeros are [DH36a, DH36b]; the standard modern survey,
which this note now cites in place of resting on the 1936 originals alone, is Bombieri–Ghosh
[BG11]. The reading that GRH needs the Euler product and that Davenport–Heilbronn is the
standing counterexample is also in print in physics vocabulary — LeClair–Mussardo [LM24] and
França–LeClair [FL14] — and is cited here rather than asserted from search-result text.

Coefficient system: a_n periodic mod 5, (a₁,…,a₅) = (1, κ, −κ, −1, 0), with the Gauss-sum surd

κ = (√(10−2√5) − 2)/(√5 − 1) = 0.28407904384041229602829183239312616909109 (41 digits; last
digit rounded — the true continuation is …9091088…).

DH is entire, satisfies a functional equation (program-verified to 5.6e−40), and has the
verified off-line zero ρ = 0.808517182456637 + 85.699348485377592i (Newton residual 7.6e−41).
Its counting data violates BOTH halves of admissibility. Closed forms below follow from the von
Mangoldt recursion a_n log n = Σ_{d|n} Λ_DH(d) a_{n/d} on the periodic coefficient array and match
the on-disk record digit-for-digit at the printed precision:

| n | exact form | value | reading |
|---|---|---|---|
| 3 | −κ·log 3 | **−0.3120927…** | negativity at a **prime** (cheapest witness) |
| 4 | −(2+κ²)·log 2 | **−1.44223196…** | negativity at a **prime power** |
| 6 | +(1+κ²)·log 6 | **+1.93635607662…** | support **off prime powers** (6 = 2·3) |
| 12 | −κ·[κ²·log 6 + (2+κ²)·log 2 + log 3] = −κ·(1+κ²)·log 12 | **−0.762877471988…** | negativity at a composite (the commission's original one-line witness) |

Λ_DH(3) < 0 and Λ_DH(4) < 0 are the adjudication-adopted "cheaper witnesses": negativity is
visible on prime powers alone, with no support-off-prime-powers preamble needed.

### 6.2 Epstein, Q = x² + 5y² (D = −20, h = 2; RH-false class, and inadmissible)

"RH-false class" is classical: for binary quadratic forms of class number h(D) > 1, the
Epstein zeta function has infinitely many zeros in Re s > 1 ([DH36b]; the h(D) even case is
[DH36a], whose closing sentence promises the odd case "in a second note") —
cited for the label only; nothing in the exclusion computation below depends on it.

Normalization (as on disk): F(s) = ζ_Q(s)/2, b_n = r_Q(n)/2, b₁ = 1; Λ_Q from −F′/F
(independent of the constant). Exact rational-log arithmetic, not floating point; numeric
rendering at 40 digits. The two witnesses:

- **Λ_Q(6) = 2·log 2 + 2·log 3 = 2·log 6 = +3.583518938456110001624954716761404545446**
  — support off prime powers (6 = 2·3): the composition-law/primitivity conclusion fails.
- **Λ_Q(36) = −4·log 2 − 4·log 3 = −4·log 6 = −7.167037876912220003249909433522809090892**
  — Λ_Q < 0: the effectivity/nef-positivity conclusion fails.

Support off prime powers for n ≤ 100 at {6, 14, 21, 36, 46, 54, 69, 84, 86, 94}; negative
values at {36, 54, 84}.

**The two structural checks** (`results/c3-m0-epstein/`, both passed exactly for all n ≤ 200):

1. **Genus identity.** (r_{Q₁}(n) + r_{Q₂}(n))/2 = Σ_{d|n} χ₋₂₀(d) exactly, where
   Q₁ = x²+5y² (principal) and Q₂ = 2x²+2xy+3y² (non-principal) — the coefficient machinery is
   verified against class-field theory, not merely enumerated.
2. **Contrast object.** ζ_K = ζ·L(χ₋₂₀) (the full class-group average, Euler product intact)
   has Λ_K supported on prime powers and ≥ 0 over the same range. What is **proved** is the
   pair: (a) ζ_Q fails admissibility (the exact witnesses above); (b) the class-group average
   ζ_K — a theorem-level Euler product, being a Dedekind zeta — satisfies it. The violation
   therefore **tracks exactly the class-orbit-breaking**: the orbit average passes, the
   single-class evaluation fails; evaluating a single CM point of the Eisenstein torus period
   instead of the full class-group orbit is exactly what destroys Euler factorization. That
   mechanism attribution is the interpretation of (a) + (b) — the mechanism claim of the
   original Lemma B, surviving here at witness level.

### 6.3 The over-breadth witness: χ₄ (RH-true, and inadmissible)

Λ_{χ₄}(3) = a₃·log 3 = **−log 3 = −1.0986…** < 0 (adjudication computation c, 50 dps).
An RH-true, degree-one, Euler-intact Dirichlet L-function fails the admissibility condition.
The filter is therefore **over-broad in a revealing way**: it is a *positivity* filter, not an
Euler-product filter. Any GL(2) object with some a_p < 0 is excluded alongside DH.

*The published exemplar of this move.* Conrey and Li [CL00] give the same genre of result: a
positivity condition sufficient for GRH, published as such, falsified by direct computation
against the very L-functions it was meant to cover — *"we shall give examples showing that de
Branges' positivity conditions, which imply the generalized Riemann hypothesis, are not satisfied
by defining functions of reproducing kernel Hilbert spaces associated with the Riemann zeta
function ζ(s) and the Dirichlet L-function L(s, χ₄)"* [CL00, introduction]. Two precisions, both
mandatory (2026-08-27 verification): the conditions in question are **de Branges'** positivity
conditions on reproducing-kernel Hilbert spaces H(E) and F(W) — *not* Li's own coefficient
criterion λ_n ≥ 0, which a reader will otherwise assume — and their criterion fails for **ζ
itself** as well as for L(s, χ₄), so the parallel with §6.3 is one of genre and not of a filter
that separates ζ from χ₄, which is what the filter here does.

## 7. The I.2/I.7 clauses (in writing, as the adjudication requires)

**(I.2 — Beurling/DMV instantiability.)** The axiom class as printed does **NOT** exclude
Beurling/DMV worlds. Beurling generalized number systems (DMV: Diamond–Montgomery–Vorhauer,
Math. Ann. 334 (2006) 1–36, on disk `fetched/p1-02`; the Broucke-school factories,
arXiv:2309.01567, 2507.13780, 2102.08478) carry a full Euler product, multiplicativity at every
generalized prime, and Λ_P(n) ≥ 0 pointwise **automatically** — while violating RH maximally.
Every **operative** coefficient-level consequence of the axiom class (prime-power support +
Λ ≥ 0) holds in these worlds by construction; (PF5), an uninstantiated template, contributes
no operative coefficient-level consequence to check — its exclusion from this accounting, and
why imposing its FE shadow by hand would change nothing, are stated in the PF5 status
paragraph, §2. **The axiom a DMV world violates: currently NONE.** The candidate
DMV-violated input, named per the adjudicated repair, is the **M4-level theta-effectivity**
h⁰_θ(D) ≥ deg D + O(1) (Bost [Bo20]; van der Geer–Schoof [vdGS00]).

**(Softened 2026-08-27, and distinguished.)** This note previously called that a "substrate-level
input no current object supplies". As an absolute that is now overstated: Connes and Consani have
since proved a Riemann–Roch theorem for Arakelov divisors on `Spec Z`-bar [CC23], strengthened for
the ring **Z** in [CC24], in which the two cohomologies are modules over the sphere spectrum and
carry **integer-valued** dimensions. What survives, and is the accurate statement, is the
distinction: their h⁰ is a *different* invariant from the real-valued theta invariant h⁰_θ of van
der Geer–Schoof and Bost — they describe the log-theta number as a dimension that *"remains
virtual … for the obvious reason that it outputs real numbers rather than integers"* — and their
result is an **Euler-characteristic identity** `χ(D) = h⁰(D) − h¹(D)` for `Spec Z` alone, which
yields no lower bound on h⁰(D) by itself without a separate H¹-vanishing or duality input. So the
DMV-violated M4-level input `h⁰_θ(D) ≥ deg D + O(1)` is **still not supplied by any current
object**; what is withdrawn is the stronger suggestion that no Riemann–Roch machinery over
`Spec Z`-bar exists at all. Until an axiom of that kind exists and is instantiated, the class
cannot decide RH.

**(What the filter is.)** The polarized-Frobenius axiom class as printed is a **POSITIVITY
filter separating {DH, Epstein} from {ζ} ∪ {all Beurling worlds}**, and it additionally
**excludes RH-true signed-coefficient L-functions** (Λ_{χ₄}(3) = −log 3 < 0, §6.3). At the
coefficient level the substrate could only ever attach to nonnegative-Λ objects (ζ, ζ_K,
Rankin–Selberg squares). It is not an Euler-product filter and not an RH filter.

**(I.7 — degree-one rigidity, the closing bracket.)** The two-sided calibration any de-novo
axiom set must clear: below {FE + Euler product + Ramanujan} at degree one, counterexamples are
mass-produced (I.2); at them, rigidity — Selberg class degree 1 = ζ + shifted Dirichlet
L-functions only, no elements of degree 1 < d < 2 (**Kaczorowski–Perelli**, Acta Math. 182
(1999) 207–241; Ann. of Math. 173 (2011) 1397–1441). The printed axioms do not derive this
classification; it is hereby cited as the **closing-bracket target** the axiom class must
eventually contain. The gap between I.2-death and I.7-rigidity is where a sufficient axiom set
must sit; the present class sits below it.

**Open item (author's, not a search result; logged 2026-08-27).** The 2026-08-27 citation pass
flagged a question this note does not answer and does not claim to: run §5's admissibility
condition against the Kaczorowski–Perelli degree-one classification just cited, and either report
the collapse — that the admissible degree-one objects are exactly the ζ and shifted-L family with
nonnegative Λ, in which case §5 and I.7 meet — or state why the two coefficient frames never meet
(the classification is stated for the Selberg class with its axioms, and admissibility is a
condition on Λ_D alone). This is arithmetic, not literature search, and it is left open here
rather than guessed at.

**(Relocation of RH content.)** Consequently, **all RH content must sit in the substrate +
Hodge-index composite** (the M1 gate → M2c substrate → M3/M4 positivity chain of C3-r). This
note carries S1 credit ONLY in the axiom-format role: it names the axioms a future substrate
must instantiate and records which objects provably cannot satisfy their coefficient-level
consequences. Sibling directions consuming "multiplicativity as geometry" should cite this note
for the axiom statement and the **Blomer–Leung beyond-endoscopy converse theorem** [BL26]
(zoo I.1) as the sharper formal home of the same exclusion — one axiom, two
dialects; coordinate at synthesis per the direction file's cross-links.

**What Blomer–Leung actually prove, and how a converse theorem hosts an exclusion.** Their
Theorem 1.1, verbatim: *"Suppose that a sequence `B(n, m)` of complex numbers satisfies the usual
Hecke relations, the Ramanujan conjecture and the Voronoi summation formula. Then this sequence is
the set of Fourier coefficients of an automorphic form on GL(3) whose archimedean Langlands
parameter is determined by the gamma factors in the Voronoi summation formula."* Their "Hecke
relations" mean that `B(n, m)` is multiplicative in both arguments and locally a PGL(3) Schur
polynomial in Satake parameters with `α_p β_p γ_p = 1`. That is a **saturation** statement, and its
contrapositive is the exclusion: a coefficient sequence that is not the Fourier-coefficient set of
a GL(3) automorphic form must fail one of the three hypotheses; and since the Voronoi formula is
equivalent (by Kıral–Zhou, as they note) to the twisted functional equations, an object carrying
the full functional-equation package must fail the **Hecke relations** — i.e. multiplicativity,
which is exactly the axiom Davenport–Heilbronn lacks. **Scope caveat, binding:** their theorem is
for **GL(3)** and Davenport–Heilbronn is a degree-2 object, so Blomer–Leung do *not* exclude DH.
What they supply is the sharpest formal home of the *shape* of the exclusion — a converse theorem
whose hypothesis list is tight enough that dropping the Hecke/Euler axiom is the only escape. Zoo
I.1's hedge ("the sharpest formal home") is correct and is kept here.

**(IV.10 rider consistency.)** This section implements, in writing, the rider recorded on zoo
I.1/III.21 by entry IV.10: any future axiom-level S1 filter must add FE/duality +
degree-one-rigidity clauses and relocate RH content to the substrate + generator composite.

## 8. What this note may NOT be cited for (adjudicated exclusions)

1. **Not "provable today."** Struck by the adjudication; the phrase may not be revived for any
   part of this material beyond the §5 monoid unpacking, which is quasi-definitional.
2. **Not a theorem.** "DH/Epstein admit no polarized Frobenius system" is not a theorem under
   either reading of the definition (§3); the citable statement is inadmissibility (§5–6).
3. **Not a discharge of the f1 flag.** The f1 scout's flag asked for a proof that DH/Epstein
   have no F1-*model*; that requires a formalized notion of F1-model and remains open.
4. **No S1 credit beyond the axiom-format role.** In particular: no claim that the axiom class
   excludes Beurling/DMV worlds (§7 states the opposite); no vacuous "zeta instantiates the
   axioms" credit (the P¹×P¹ system of §3.2 shows axiom-level instantiation can be worthless);
   no S1 = 5 self-score for C3-r while no zeta instantiation of the axioms exists at any rank.
5. **Not a seed revival.** Nothing here bears on per-prime-fiber assemblies; the E_p × E_q seed
   is dead (zoo IV.10) and M2b/N2 remain struck.

## 9. Traceability (every number to its on-disk source)

All paths relative to `anthropic/rh-program/`.

| Item | Source |
|---|---|
| Fork (both horns), P¹×P¹ counterexample, bidegree multiplicativity, (Γ_n·Δ) = n+1, non-multiplicativity 7 ≠ 12 | `results/verdicts-c3d1.json` kill:C3 fatal 2, kill2:C3 fatal 1; `results/adjudication-C3.json` computation b |
| Char-p correction; F₇ verification (1,7)/(1,49)/(1,343) vs 5/55/380 | `results/adjudication-C3.json` computation b; `results/verdicts-c3d1.json` (both killers) |
| Effectivity axiom + degree-one scope restriction | `results/verdicts-c3d1.json` ref:C3 minor finding 1 (verified monoid computation); adjudication, the mandatory repair beginning "Reprice M0 …" |
| FE/duality (transpose/Rosati) axiom absence | `results/verdicts-c3d1.json` kill2:C3 major finding 2; adjudication, the mandatory repair beginning "Reprice M0 …" |
| κ (41 digits), Λ_DH(3), Λ_DH(4), Λ_DH(6), Λ_DH(12) | `results/adjudication-C3.json` computation d; `results/verdicts-c3d1.json` (three independent computations, digit-for-digit); underlying DH machinery `results/decisive-tests/ccm-dh-filter.json`, `results/ccm-dh-test/` |
| DH off-line zero, FE verification depth | `results/decisive-tests/ccm-dh-filter.json`; restated in `directions/C3-geometric-substrate.md` §Z1 |
| Epstein exact pair, 40-digit values, support/negativity lists, genus identity, ζ_K contrast | `results/c3-m0-epstein/n1_epstein_witness.json` (+ `.py`); adjudication computation d |
| Λ_{χ₄}(3) = −log 3 | `results/adjudication-C3.json` computation c |
| Positivity-filter classification; Beurling instantiability; relocation order | `results/adjudication-C3.json` computation c + the mandatory repair beginning "Rewrite the S1 section …"; `BARRIER-ZOO.md` I.2, IV.10 rider |
| Kaczorowski–Perelli, Blomer–Leung, DMV citations | `BARRIER-ZOO.md` I.7, I.1, I.2 |
| Chen–Moriwaki / Yuan–Zhang framework citations | `directions/C3-geometric-substrate.md` (corpus note: q-13a = 2019 LNM norms/heights volume; the intersection-theory Mémoire arXiv:2103.15646 was NOT on disk at adjudication time — adjudication computation f — and has since been fetched and title-verified 2026-08-26 as `fetched-r3/r3s-07`, per `results/corpus-routing.md` caveat 14) |

**Closed-form note.** The exact expressions −κ log 3, −(2+κ²) log 2, +(1+κ²) log 6, and
−κ[κ² log 6 + (2+κ²) log 2 + log 3] are unpacked in this write-up from the standard von Mangoldt
recursion on the periodic DH coefficient array; each was checked against the on-disk decimal
record and agrees to all printed digits (§6.1). The Epstein closed forms are on disk verbatim.

*(C3-r M0 deliverable. U.S. English. Written Session 6, 2026-08-26.)*

---

## 10. References

External references, every field verified against a primary source in the 2026-08-27 citation
pass (Crossref, zbMATH Open, the arXiv abstract pages, the publishers' own records, or the
program's on-disk corpus); the per-source evidence is in
`results/arxiv/citation-verification/`.

- **[Ap76]** T. M. Apostol, *Introduction to Analytic Number Theory*, Undergraduate Texts in
  Mathematics, Springer-Verlag, New York, 1976, Ch. 11 ("Dirichlet Series and Euler Products"),
  pp. 224–248; doi:10.1007/978-1-4757-5579-4.
- **[BG11]** E. Bombieri and A. Ghosh, *Around the Davenport–Heilbronn function*, Russian Math.
  Surveys **66** (2011), no. 2, 221–270; doi:10.1070/RM2011v066n02ABEH004740; Russian original,
  Uspekhi Mat. Nauk **66** (2011), no. 2, 15–66; doi:10.4213/rm9410.
- **[BL26]** V. Blomer and W. H. Leung, *A GL(3) converse theorem via a "beyond endoscopy"
  approach*, Adv. Math. **485** (2026), art. 110716; doi:10.1016/j.aim.2025.110716;
  arXiv:2401.04037 (v1, 8 Jan 2024; v2, 11 Jul 2026).
- **[Bo20]** J.-B. Bost, *Theta invariants of Euclidean lattices and infinite-dimensional
  Hermitian vector bundles over arithmetic curves*, Progress in Mathematics **334**, Birkhäuser,
  2020; arXiv:1512.08946. *(Series and number via Connes–Consani's bibliography; the arXiv title
  and authorship are primary.)*
- **[Bor09]** J. Borger, *Lambda-rings and the field with one element*, preprint (2009), 31 pp.,
  arXiv:0906.3146 [math.NT]. (Unpublished; v1, 17 Jun 2009, is the only version.)
- **[BU1]** G. Banaszak and Y. Uetake, *Abstract intersection theory and operators in Hilbert
  space*, Commun. Number Theory Phys. **5** (2011), no. 3, 699–712;
  doi:10.4310/CNTP.2011.v5.n3.a4; arXiv:0908.2909. On disk: corpus t-43b.
- **[BU2]** G. Banaszak and Y. Uetake, *Standard models of abstract intersection theory for
  operators in Hilbert space*, Bull. Pol. Acad. Sci. Math. **63** (2015), no. 2, 149–175;
  doi:10.4064/ba63-2-5; arXiv:1210.3526. On disk: corpus t-30b.
- **[BU3]** G. Banaszak and Y. Uetake, *Abstract intersection theory for zeta-functions:
  geometric aspects*, Funct. Approx. Comment. Math. **64** (2021), no. 2, 251–265;
  doi:10.7169/facm/1916. On disk: corpus t-58a. (No arXiv version — verified absent.)
- **[CC16]** A. Connes and C. Consani, *Geometry of the arithmetic site*, Adv. Math. **291**
  (2016), 274–329; doi:10.1016/j.aim.2015.11.045; arXiv:1502.05580. Theorem 1.2 (restated as
  Theorem 7.7) is the composition law Ψ(λ) ∘ Ψ(λ′) = Ψ(λλ′) for Frobenius correspondences as
  congruences in the square.
- **[CC16b]** A. Connes and C. Consani, *The scaling site*, C. R. Math. Acad. Sci. Paris **354**
  (2016), no. 1, 1–6; doi:10.1016/j.crma.2015.09.027; arXiv:1507.05818 (21 Jul 2015).
- **[CC17]** A. Connes and C. Consani, *Geometry of the scaling site*, Selecta Math. (N.S.) **23**
  (2017), no. 3, 1803–1850; doi:10.1007/s00029-017-0313-y; arXiv:1603.03191. (**Note,
  2026-08-27:** arXiv:1507.05818 is the preprint of [CC16b], *not* of this article; the novelty
  report paired them wrongly and the pairing is corrected here.)
- **[CC19]** A. Connes and C. Consani, *The Riemann–Roch strategy: Complex lift of the Scaling
  Site*, in: A. Chamseddine, C. Consani, N. Higson, M. Khalkhali, H. Moscovici and G. Yu (eds.),
  *Advances in Noncommutative Geometry: On the Occasion of Alain Connes' 70th Birthday*, Springer,
  Cham, 2019, pp. 53–125; doi:10.1007/978-3-030-29597-4_2; arXiv:1805.10501.
- **[CC23]** A. Connes and C. Consani, *Riemann–Roch for Spec Z-bar* (the overline spans
  *Spec Z*), Bull. Sci. Math. **187** (2023), art. 103293; doi:10.1016/j.bulsci.2023.103293;
  arXiv:2205.01391.
- **[CC24]** A. Connes and C. Consani, *Riemann–Roch for the ring Z*, C. R. Math. Acad. Sci. Paris
  **362** (2024), 229–235; doi:10.5802/crmath.543; arXiv:2306.00456.
- **[CCM09]** A. Connes, C. Consani and M. Marcolli, *Fun with F₁*, J. Number Theory **129**
  (2009), no. 6, 1532–1561; doi:10.1016/j.jnt.2008.08.007; arXiv:0806.2401.
- **[CE15]** A. Connes, *An essay on the Riemann Hypothesis*, in: *Open Problems in Mathematics*
  (J. F. Nash Jr. and M. Th. Rassias, eds.), Springer, Cham, 2016, pp. 225–257;
  doi:10.1007/978-3-319-32162-2_5; arXiv:1509.05576. On disk: `fetched-r2/t-20b`. Pin-cites are
  by **section** (§2.3, §4.3.1, §4.3.2), which are common to both versions; page folios differ
  between the arXiv version and the book by about +224.
- **[CL00]** J. B. Conrey and X.-J. Li, *A note on some positivity conditions related to zeta and
  L-functions*, Internat. Math. Res. Notices **2000**, no. 18, 929–940;
  doi:10.1155/S1073792800000489; arXiv:math/9812166. On disk: `fetched/p1-06`.
- **[Den98]** C. Deninger, *Some analogies between number theory and dynamical systems on foliated
  spaces*, in: Proceedings of the International Congress of Mathematicians (Berlin, 1998), Vol. I,
  Doc. Math. Extra Vol. ICM I (1998), 163–186; doi:10.4171/dms/1-1/2.
- **[Den22]** C. Deninger, *There is no "Weil-"cohomology theory with real coefficients for
  arithmetic curves*, Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) **25** (2024), no. 3, 1717–1725;
  doi:10.2422/2036-2145.202204_005; arXiv:2204.02714. On disk: `fetched/x-04`. (Published since
  the prior-art gate ran; the "to appear" form is superseded.)
- **[DH36a]** H. Davenport and H. Heilbronn, *On the zeros of certain Dirichlet series*,
  J. London Math. Soc. **11** (1936), no. 3, 181–185; doi:10.1112/jlms/s1-11.3.181. On disk:
  `fetched-r3/davenport1936.pdf`.
- **[DH36b]** H. Davenport and H. Heilbronn, *On the zeros of certain Dirichlet series (Second
  paper)*, J. London Math. Soc. **11** (1936), no. 4, 307–312; doi:10.1112/jlms/s1-11.4.307. On
  disk: `fetched-r3/davenport1936-2.pdf`. (The printed page carries "(Second paper)", capitalized
  as here, and is primary; Crossref drops the clause entirely.)
- **[DMV06]** H. G. Diamond, H. L. Montgomery and U. M. A. Vorhauer, *Beurling primes with large
  oscillation*, Math. Ann. **334** (2006), 1–36; doi:10.1007/s00208-005-0638-2. On disk:
  `fetched/p1-02`.
- **[DZ16]** H. G. Diamond and W.-B. Zhang, *Beurling Generalized Numbers*, Mathematical Surveys
  and Monographs **213**, Amer. Math. Soc., Providence, RI, 2016; doi:10.1090/surv/213. On disk:
  `fetched-r2/t-50`. Pin-cites: p. 1, §1.1(2) for the RH remark; Theorem 17.11 (p. 205) for an
  RH-**true** Beurling system and Theorem 17.14 (p. 208) for an RH-**false** one, in one chapter.
  Chapter 17 is the book-form account of [Zh07] and [DMV06] and supersedes a bare citation of
  either.
- **[FL14]** G. França and A. LeClair, *A theory for the zeros of Riemann ζ and other L-functions
  (updated)*, preprint, arXiv:1407.4358 (v1, Jul 2014; v2, Aug 2024).
- **[FM20]** M. Flach and B. Morin, *Deninger's conjectures and Weil–Arakelov cohomology*, Münster
  J. Math. **13** (2020), no. 2, 519–540; doi:10.17879/90169642993 *(a Universität Münster
  repository DOI, not Crossref-registered; attested independently by zbMATH and HAL, but not
  watched to resolve end to end)*; open-access preprint HAL hal-02407608. There is **no** arXiv
  version — two searches returned nothing; do not manufacture an id.
- **[KP1]** J. Kaczorowski and A. Perelli, *On the structure of the Selberg class, I: 0 ≤ d ≤ 1*,
  Acta Math. **182** (1999), 207–241.
- **[KP7]** J. Kaczorowski and A. Perelli, *On the structure of the Selberg class, VII:
  1 < d < 2*, Ann. of Math. (2) **173** (2011), 1397–1441.
- **[LM24]** A. LeClair and G. Mussardo, *Riemann zeros as quantized energies of scattering with
  impurities*, J. High Energy Phys. **2024** (2024), no. 4, paper 062, 20 pp.;
  doi:10.1007/JHEP04(2024)062; arXiv:2307.01254.
- **[Man95]** Yu. I. Manin, *Lectures on zeta functions and motives (according to Deninger and
  Kurokawa)*, in: Columbia University Number Theory Seminar (New York, 1992), Astérisque **228**
  (1995), 121–163; MR 1330931; Zbl 0840.14001. On disk: `fetched/x-02`. The phrases "absolute
  Descartes powers" and "a canonical absolute Frobenius" are on pp. 121 and 123.
- **[MV07]** H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I: Classical
  Theory*, Cambridge Studies in Advanced Mathematics **97**, Cambridge University Press,
  Cambridge, 2007, §1.3 ("Euler products and the zeta function"), pp. 19–30, Theorem 1.9, p. 20.
  (**Correction of record, 2026-08-27:** the novelty report cited §1.2; §1.2 is "Analytic
  properties of Dirichlet series". The Euler-product material is §1.3.)
- **[vdGS00]** G. van der Geer and R. Schoof, *Effectivity of Arakelov divisors and the theta
  divisor of a number field*, Selecta Math. (N.S.) **6** (2000), no. 4, 377–398;
  arXiv:math/9802121. *(Journal fields via Connes–Consani's bibliography — a secondary source; the
  arXiv title and authorship are primary.)*
- **[Zh07]** W.-B. Zhang, *Beurling primes with RH and Beurling primes with large oscillation*,
  Math. Ann. **337** (2007), 671–704; doi:10.1007/s00208-006-0051-5. Superseded for citation
  purposes by [DZ16, Ch. 17], which is its book-form account.

Also cited in place and unchanged by this pass: Chen–Moriwaki (arXiv:1903.10798) for adelic
curves; Yuan–Zhang (arXiv:2105.13587 v9; Annals of Mathematics Studies **221**, 2026) for the
adelic-line-bundle calculus; the Broucke-school Beurling factories (arXiv:2309.01567, 2507.13780,
2102.08478).


---

## Referee pass + repairs (2026-08-26)

**Referee verdict** (`results/c3-r/referee-m0.md`, independent, same date): PASS WITH REPAIRS —
0 fatal, 3 major, 7 minor; no mathematical error; all six witnesses, both closed-form families,
the F₇ accounting, and the P¹×P¹ counterexample replicated from scratch; FE and off-line zero
independently re-verified to residuals ≤ 1e−60. All repairs below applied 2026-08-26.

- **MAJOR 1 (PF5 audit gap) — FIXED.** "PF5 status" paragraph added to §2 (transpose-stability
  already fails for the §3.2 family, so the exhibit certifies (PF1)–(PF4)-fragment vacuity; PF5
  excluded from the §7 DMV accounting as an uninstantiated template with no operative
  coefficient-level consequence); §3.2 item 2 and §7's "(PF1)–(PF6)" sentence amended to match.
  The bidegree fact (Γ_n^t ≡ ξ₁ + nξ₂, not any Γ_m ≡ mξ₁ + ξ₂ for n ≥ 2) re-derived before
  editing.
- **MAJOR 2 (Blomer–Leung volume) — FIXED, verified authoritatively online.** arXiv:2401.04037's
  journal-ref field and Crossref metadata for DOI 10.1016/j.aim.2025.110716 agree: Advances in
  Mathematics **485** (2026), art. 110716 (published February 2026). The note's two occurrences
  of "Adv. Math. 471" corrected to 485 with the arXiv handle added; `BARRIER-ZOO.md` I.1
  corrected identically.
- **MAJOR 3 (§5 attachment ambiguity) — FIXED.** The attachment functional is now explicit:
  a_n := d₂(Ψ_n) = (Ψ_n·ξ₂), the second-fiber degree (char-p analog of deg F^k = q^k), with the
  non-multiplicative polarization-pairing reading expressly barred and the monomial
  generalization noted.
- Minor 1 (mixed index bases) — fixed: all adjudication-array references now cite by quoted
  opening phrase, stated in the front matter.
- Minor 2 (decimal conventions) — fixed: Λ_DH(4) printed as −1.44223196… (truncation); κ's
  41-digit value marked last-digit-rounded with the true continuation shown.
- Minor 3 (bare Λ in the recursion) — fixed: Λ_DH in the displayed identity.
- Minor 4 (stale corpus statement) — fixed: §9 row updated to record the Mémoire's post-
  adjudication fetch as `fetched-r3/r3s-07` (corpus-routing caveat 14).
- Minor 5 (exhaustiveness under-defended) — fixed: §3.4 rewritten to the airtight form (primary
  dichotomy = factors through composition or not; any non-multiplicative reading needs a tie
  axiom; H⁰/H²-vs-H¹ demoted to template interpretation).
- Minor 6 (uncited "RH-false class") — fixed: Davenport–Heilbronn (Second paper), J. London
  Math. Soc. 11 (1936) 307–312 added to §6.2, label-only; identification of the Epstein
  h(D) > 1, Re s > 1 result with the second paper verified online this pass.
- Minor 7 ("provably" compression) — fixed: §6.2 check 2 now separates the proved pair (a)+(b)
  from the mechanism attribution, per the referee's recommended phrasing.
- Referee's no-repair remark adopted: the Λ_DH(12) closed form now also shows the equivalent
  short form −κ(1+κ²)·log 12 (equality re-derived symbolically before adding).

**Rejected/deferred:** none — every referee item applied.

*(Repairs editor, Session 6+, 2026-08-26. This note is now external-circulation ready per the
referee's §6 assessment with all three majors landed and all minors swept.)*
