# The polarized-Frobenius axiom class: an S1 axiom statement with DH/Epstein witnesses (not a theorem)

**Deliverable:** C3-r M0 (axiom-format note), per the binding adjudication of 2026-08-26
(`results/adjudication-C3.json`, mandatory_repairs[1]; recommission order "C3-r" in
`directions/C3-geometric-substrate.md`).

**Status (read before citing).** This document is an **axiom statement plus a witness record**.
It is NOT a theorem, it is NOT "provable today," and it does NOT discharge the f1 scout's
"DH/Epstein have no F1-model" flag (which requires a formalized notion of F1-model and remains
open). The original "Lemma B" theorem framing of the C3 commission was killed by two independent
killer verdicts (blind replication) and upheld on adjudicator re-derivation
(`results/verdicts-c3d1.json` kill:C3 fatal 2, kill2:C3 fatal 1; `results/adjudication-C3.json`
computation b and killer_findings_upheld[2]). What survives — per the adjudicator's partial
overrule of killer-1, via the referee's verified minor finding — is exactly this: **with
effectivity added as an axiom, the step-2 monoid computation under the degree reading is a
correct, cheap formal computation**, so the axiom-format note is a legitimate, nonzero
deliverable rather than pure re-dressing. The content remains quasi-definitional: it is barrier
zoo I.1's witness in a new dialect, whose sharper formal home is the Blomer–Leung monoid converse
(zoo I.1; Adv. Math. 471 (2026) 110716).

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

## 2. The axiom class (repaired definition)

Let S = (K, (Ω, ν), (|·|_ω)) be a **proper adelic curve** in the Chen–Moriwaki sense
(arXiv:1903.10798; "proper" = the product formula holds). A **polarized Frobenius system** for a
Dirichlet series D(s) over S consists of:

- **(PF1) Polarized square.** A fibered square X over S carrying a nef adelic Q-line bundle L̄
  in the Yuan–Zhang adelic-line-bundle calculus (arXiv:2105.13587 v9; Annals of Mathematics
  Studies 223), with the two fiber classes ξ₁, ξ₂ and a correspondence composition ∘ and
  transpose t.
- **(PF2) Frobenius family.** A family of correspondences {Ψ_n}_{n≥1} on X with Ψ₁ = Δ (the
  identity correspondence).
- **(PF3) Composition law and primitivity.** Ψ_m ∘ Ψ_n = Ψ_mn for **all** m, n ≥ 1, and Ψ_p is
  primitive (not a composition of non-identity members) exactly at the primes p.
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
   so the identical system would serve D = ζ, D = DH, or D = Epstein indifferently. (Both
   killers constructed this counterexample independently; adjudicator re-verified. Whether (PF5)
   in a sharpened form excludes it is not adjudicated and not claimed.)
3. Therefore, under Horn A, "reproduce the counting data of D" must itself be an **axiom — an
   admissibility condition on D**, not a property the geometry proves. Under that admissibility
   axiom, prime-power support and Λ_D ≥ 0 follow by the correct, cheap monoid computation of §5
   — **quasi-definitionally**: the only geometric ingredient consumed is that degrees of
   effective correspondences against a nef polarization are ≥ 0, which is a basic property of
   the Yuan–Zhang calculus, not a theorem being put to work.

### 3.3 Horn B — the trace reading

Read (PF6) as: *the counting data of D is reproduced by intersection against the diagonal,
(Ψ_n·Δ)-type numbers* — the only reading matching where counting data actually lives in the
char-p template (§3.5). Then the original step 2 ("composition law + primitivity ⟹ prime-power
support; formal monoid algebra; no analysis") is **false as a formal claim**: by §3.1 trace data
does not factor through composition ((Γ₆·Δ) = 7 ≠ 12 on P¹×P¹), and no formal argument forces
(Ψ₆·Δ)-type data to vanish. What is needed is a **Lefschetz-tie axiom** ("the counting data of D
is trace-organized by the monoid") — in characteristic p that tie is a THEOREM about the
existing cohomology; over Q it is exactly the missing substrate (M2). Adding it as an axiom
makes the D-attachment Euler-organized by definition, so the DH/Epstein exclusion again follows
from the definition plus the one-line coefficient witnesses of §6 — definitional once more.

### 3.4 Exhaustiveness of the fork

Any counting functional on the system either factors through composition-multiplicative
invariants (bidegrees; more generally the induced action on H⁰/H²) — Horn A — or involves
H¹-trace data — Horn B. In every known template the zero side IS the H¹ trace, so there is no
third reading. Under Horn A the statement is an admissibility definition; under Horn B it needs
a Lefschetz axiom that makes it an admissibility definition. Hence: axiom statement, on every
branch. (Both killers, independently; upheld in adjudication.)

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
  D(s) = Π_p (1 − a_p p^{−s})^{−1} — **degree one**. The axiom class as printed excludes every
  higher-degree Euler-intact L-function (e.g. ζ_K for a quadratic field K has degree-2 Euler
  factors and non-totally-multiplicative coefficients; it satisfies the coefficient-level
  consequence class of §5 but not the printed degree-one shape). A relaxed composition law
  (e.g. coprime-only multiplicativity plus per-prime tower data) is NOT provided by the printed
  axioms; any future widening is new design, outside this note.
- **(b) Relation to the one-generator function-field monoid.** The char-p template's Frobenius
  monoid is generated by ONE element: {Γ_{F^k} : k ≥ 0} ≅ (N, +), indexed by the exponent k
  (the extension degree), with a single "prime." The printed multi-prime monoid {Ψ_n} over
  (N^×, ·) — free commutative on all rational primes — is a different object: the commission's
  template was a one-prime template misread as a multi-prime one. Total multiplicativity across
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
admissibility axiom: (PF3) makes n ↦ (degree data of Ψ_n) a monoid homomorphism, i.e. totally
multiplicative (§3.1), forcing the degree-one Euler shape (§4a); primitivity places the
generators exactly at the primes; hence −D′/D has Λ_D(p^k) = a_p^k log p and Λ_D(n) = 0 off
prime powers — formal monoid algebra, no analysis. (PF4) effectivity plus (PF1) nefness gives
a_p = (degree of the effective Ψ_p against the nef polarization-normalized fiber data) ≥ 0,
hence Λ_D(n) ≥ 0. This is the step-2/step-3 chain the referee verified by writing out the monoid
computation, valid **once effectivity is an axiom** — and it is an unpacking of the definition,
not a theorem about D: the geometry contributes only "nef against effective is ≥ 0."

**What would restore theorem status.** Nothing currently available: a genuine exclusion theorem
would require a substrate on which the Lefschetz tie of §3.3 is *proved* rather than posited —
i.e. M2. Until then the correct citation form is: "D is inadmissible for the polarized-Frobenius
axiom class [this note, §5–6]," never "D admits no polarized Frobenius system [theorem]."

## 6. The witnesses (exact)

All values below are on disk with exact closed forms; sources in §9. "Inadmissible" always means:
fails the §5 admissibility condition, with the named witness.

### 6.1 Davenport–Heilbronn (RH-false, and inadmissible)

Coefficient system: a_n periodic mod 5, (a₁,…,a₅) = (1, κ, −κ, −1, 0), with the Gauss-sum surd

κ = (√(10−2√5) − 2)/(√5 − 1) = 0.28407904384041229602829183239312616909109 (41 digits).

DH is entire, satisfies a functional equation (program-verified to 5.6e−40), and has the
verified off-line zero ρ = 0.808517182456637 + 85.699348485377592i (Newton residual 7.6e−41).
Its counting data violates BOTH halves of admissibility. Closed forms below follow from the von
Mangoldt recursion a_n log n = Σ_{d|n} Λ(d) a_{n/d} on the periodic coefficient array and match
the on-disk record digit-for-digit at the printed precision:

| n | exact form | value | reading |
|---|---|---|---|
| 3 | −κ·log 3 | **−0.3120927…** | negativity at a **prime** (cheapest witness) |
| 4 | −(2+κ²)·log 2 | **−1.4422320…** | negativity at a **prime power** |
| 6 | +(1+κ²)·log 6 | **+1.93635607662…** | support **off prime powers** (6 = 2·3) |
| 12 | −κ·[κ²·log 6 + (2+κ²)·log 2 + log 3] | **−0.762877471988…** | negativity at a composite (the commission's original one-line witness) |

Λ_DH(3) < 0 and Λ_DH(4) < 0 are the adjudication-adopted "cheaper witnesses": negativity is
visible on prime powers alone, with no support-off-prime-powers preamble needed.

### 6.2 Epstein, Q = x² + 5y² (D = −20, h = 2; RH-false class, and inadmissible)

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
   has Λ_K supported on prime powers and ≥ 0 over the same range. The violation in Λ_Q is
   therefore **provably the class-orbit-breaking**: evaluating a single CM point of the
   Eisenstein torus period instead of the full class-group orbit is exactly what destroys Euler
   factorization — the mechanism claim of the original Lemma B, surviving here at witness level.

### 6.3 The over-breadth witness: χ₄ (RH-true, and inadmissible)

Λ_{χ₄}(3) = a₃·log 3 = **−log 3 = −1.0986…** < 0 (adjudication computation c, 50 dps).
An RH-true, degree-one, Euler-intact Dirichlet L-function fails the admissibility condition.
The filter is therefore **over-broad in a revealing way**: it is a *positivity* filter, not an
Euler-product filter. Any GL(2) object with some a_p < 0 is excluded alongside DH.

## 7. The I.2/I.7 clauses (in writing, as the adjudication requires)

**(I.2 — Beurling/DMV instantiability.)** The axiom class as printed does **NOT** exclude
Beurling/DMV worlds. Beurling generalized number systems (DMV: Diamond–Montgomery–Vorhauer,
Math. Ann. 334 (2006) 1–36, on disk `fetched/p1-02`; the Broucke-school factories,
arXiv:2309.01567, 2507.13780, 2102.08478) carry a full Euler product, multiplicativity at every
generalized prime, and Λ_P(n) ≥ 0 pointwise **automatically** — while violating RH maximally.
Every coefficient-level consequence of (PF1)–(PF6) (prime-power support + Λ ≥ 0) holds in these
worlds by construction. **The axiom a DMV world violates: currently NONE.** The candidate
DMV-violated input, named per the adjudicated repair, is the **M4-level theta-effectivity**
h⁰_θ(D) ≥ deg D + O(1) (Bost arXiv:1512.08946; van der Geer–Schoof math/9802121) — a
substrate-level input no current object supplies. Until such an axiom exists and is
instantiated, the class cannot decide RH.

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

**(Relocation of RH content.)** Consequently, **all RH content must sit in the substrate +
Hodge-index composite** (the M1 gate → M2c substrate → M3/M4 positivity chain of C3-r). This
note carries S1 credit ONLY in the axiom-format role: it names the axioms a future substrate
must instantiate and records which objects provably cannot satisfy their coefficient-level
consequences. Sibling directions consuming "multiplicativity as geometry" should cite this note
for the axiom statement and the **Blomer–Leung beyond-endoscopy monoid converse** (Adv. Math.
471 (2026) 110716; zoo I.1) as the sharper formal home of the same exclusion — one axiom, two
dialects; coordinate at synthesis per the direction file's cross-links.

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
| Effectivity axiom + degree-one scope restriction | `results/verdicts-c3d1.json` ref:C3 minor finding 1 (verified monoid computation); adjudication mandatory_repairs[1] |
| FE/duality (transpose/Rosati) axiom absence | `results/verdicts-c3d1.json` kill2:C3 major finding 2; adjudication mandatory_repairs[1] |
| κ (41 digits), Λ_DH(3), Λ_DH(4), Λ_DH(6), Λ_DH(12) | `results/adjudication-C3.json` computation d; `results/verdicts-c3d1.json` (three independent computations, digit-for-digit); underlying DH machinery `results/decisive-tests/ccm-dh-filter.json`, `results/ccm-dh-test/` |
| DH off-line zero, FE verification depth | `results/decisive-tests/ccm-dh-filter.json`; restated in `directions/C3-geometric-substrate.md` §Z1 |
| Epstein exact pair, 40-digit values, support/negativity lists, genus identity, ζ_K contrast | `results/c3-m0-epstein/n1_epstein_witness.json` (+ `.py`); adjudication computation d |
| Λ_{χ₄}(3) = −log 3 | `results/adjudication-C3.json` computation c |
| Positivity-filter classification; Beurling instantiability; relocation order | `results/adjudication-C3.json` computation c + mandatory_repairs[3]; `BARRIER-ZOO.md` I.2, IV.10 rider |
| Kaczorowski–Perelli, Blomer–Leung, DMV citations | `BARRIER-ZOO.md` I.7, I.1, I.2 |
| Chen–Moriwaki / Yuan–Zhang framework citations | `directions/C3-geometric-substrate.md` (corpus note: q-13a = 2019 LNM norms/heights volume; the intersection-theory Mémoire arXiv:2103.15646 is NOT on disk — adjudication computation f) |

**Closed-form note.** The exact expressions −κ log 3, −(2+κ²) log 2, +(1+κ²) log 6, and
−κ[κ² log 6 + (2+κ²) log 2 + log 3] are unpacked in this write-up from the standard von Mangoldt
recursion on the periodic DH coefficient array; each was checked against the on-disk decimal
record and agrees to all printed digits (§6.1). The Epstein closed forms are on disk verbatim.

*(C3-r M0 deliverable. U.S. English. Written Session 6, 2026-08-26.)*
