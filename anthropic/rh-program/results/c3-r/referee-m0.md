# Referee report: `results/c3-r/m0-axiom-note.md` (C3-r M0, the polarized-Frobenius axiom-format note)

**Referee pass owed per the binding reduced recommission** (`directions/C3-geometric-substrate.md`,
"Current frontier": "both notes then face a referee pass before any external circulation").
**Referee:** independent (wrote none of the inputs). **Date:** 2026-08-26.
**Verdict: PASS WITH REPAIRS — 0 fatal, 3 major, 7 minor.** No mathematical error found; every
witness, closed form, and model computation replicated exactly under independent re-derivation;
conformance to the adjudicated repair list is complete. The majors are a PF5 audit gap (two
manifestations of one root), one load-bearing citation with a volume discrepancy found online, and
one ambiguity at the mathematical heart of §5. All are fixable in a single sitting; none is
structural. The note must not circulate externally until the three majors land.

---

## 1. Conformance to the adjudicated repair list (binding; direction file, "THE REDUCED RECOMMISSION")

| Required item | Where in the note | Verdict |
|---|---|---|
| Fork stated, with exhaustiveness | §3.1–3.4 | ✅ (see minor 5 on the exhaustiveness argument's form) |
| Effectivity axiom added | (PF4), §2 | ✅ with the correct attribution ("original definition omitted it and its step 3 is false without it") |
| FE/duality (transpose/Rosati) axiom added | (PF5), §2 | ✅ present; but see MAJOR 1 — its printed content is never audited against the note's own later claims |
| I.2 clause in writing; axiom DMV worlds violate = "currently none; candidate = M4-level theta-effectivity" | §7, verbatim | ✅ exact adjudicated phrasing |
| I.7 clause: Kaczorowski–Perelli degree-one rigidity as closing-bracket target | §7 | ✅; citations verified online this pass (Acta Math. 182 (1999) 207–241; Ann. of Math. 173 (2011) 1397–1441) |
| Total-multiplicativity degree-one scope restriction | §4(a)–(b) | ✅ both halves (Euler-shape pin; one-generator char-p monoid contrast) |
| Char-p sentence corrected (F₇ accounting: degrees see main terms; zero side in the Δ-intersection) | §3.5 | ✅ and independently re-verified (below) |
| All six exact witnesses | §6.1 (four DH) + §6.2 (two Epstein) | ✅ all six replicated digit-for-digit (below) |
| May-NOT-be-cited-for list | §8, five items | ✅ complete: not-provable-today, not-a-theorem, no-f1-discharge, no-S1-beyond-format (incl. Beurling non-exclusion and no S1=5 self-score), no seed revival |
| Traceability table | §9 | ✅ every number routes to an on-disk source; see minors 1 and 4 |
| Formal home cross-cited to Blomer–Leung | §1, §7 | ✅ cross-cited; see MAJOR 2 (volume discrepancy) |
| Overclaim discipline (adjudication R4/vacuity: nothing beyond the S1 axiom-format role) | §0 status block, §1, §5, §7, §8 | ✅ no revived struck claim found anywhere; scope sentences are uniformly correct |

Reference-integrity spot-checks: the note's "kill:C3 fatal 2, kill2:C3 fatal 1" correctly names
the two Lemma-B fatals in `results/verdicts-c3d1.json` (kill:C3's finding 2 and kill2:C3's finding
1 are the fork fatals; the seed fatals are the others). The §7 IV.10-rider sentence matches
`BARRIER-ZOO.md` IV.10's rider on I.1/III.21. The §6.1 FE depth (5.6e−40) and zero residual
(7.6e−41) match `results/decisive-tests/ccm-dh-filter.json` verbatim. But see minor 1: the note's
bracketed array indices into `adjudication-C3.json` mix 0-based and 1-based conventions.

## 2. Independent re-derivation ledger (standing order 5 — nothing reused; all recomputed from scratch)

Script: session scratchpad `referee_m0_verify.py` (mpmath 60 dps; exact `Fraction` rational-log
vectors for Epstein/χ₄/ζ_K; brute-force lattice enumeration for representation numbers; direct
finite-field enumeration for the F₇ curve).

1. **κ surd.** (√(10−2√5) − 2)/(√5 − 1) = 0.28407904384041229602829183239312616909108808844574…
   The note's 41-digit value ...909109 is the correctly ROUNDED 41st digit (true continuation
   ...9091088…). Matches the program record.
2. **DH witnesses, numeric (von Mangoldt recursion on a_n = (1, κ, −κ, −1, 0) mod 5, rebuilt from
   scratch).** Λ_DH(3) = −0.312092728516…, Λ_DH(4) = −1.442231964606…, Λ_DH(6) =
   +1.936356076621…, Λ_DH(12) = −0.762877471988… — all four match the note (see minor 2 on the
   Λ_DH(4) rendering). Λ_DH(5) = Λ_DH(10) = 0 as required.
3. **DH closed forms, verified symbolically AND numerically to < 10⁻³⁰:** Λ_DH(3) = −κ log 3;
   Λ_DH(4) = −(2+κ²) log 2; Λ_DH(6) = (1+κ²) log 6; Λ_DH(12) = −κ[κ² log 6 + (2+κ²) log 2 + log 3].
   Referee's remark (no repair needed): the Λ_DH(12) form simplifies to −κ(1+κ²) log 12 —
   verified equal; the note may prefer the shorter form.
4. **DH functional equation, INDEPENDENTLY verified** (not merely traced to the on-disk record):
   with F(s) := (5/π)^((s+1)/2) Γ((s+1)/2) f_DH(s), F(s) = F(1−s) holds to relative residual
   ≤ 3.6e−61 at three test points (dps 60); and f_DH = [(1−iκ)/2]L(s,χ) + [(1+iκ)/2]L(s,χ̄) (χ odd
   mod 5, χ(2) = i) verified to 1.2e−61. The note's "satisfies a functional equation
   (program-verified to 5.6e−40)" is if anything conservative.
5. **DH off-line zero, independently re-verified** via Hurwitz-zeta evaluation: |f_DH(ρ)| =
   5.3e−16 at the printed 15-digit ρ (the expected truncation floor); Newton refinement converges
   to ρ = 0.80851718245663738555… + 85.69934848537759217193…i with residual 2.7e−60; Re ρ > 1/2;
   |f_DH(1/2 + 85.699348485377592i)| = 0.357 (no on-line zero nearby). Consistent with the
   program's 7.6e−41 record at dps ≈ 41.
6. **Epstein Q = x² + 5y², exact arithmetic (Fraction-valued log-vectors, own lattice
   enumeration):** Λ_Q(6) = 2 log 2 + 2 log 3 and Λ_Q(36) = −4 log 2 − 4 log 3 EXACTLY; 40-digit
   renderings match the note and `results/c3-m0-epstein/n1_epstein_witness.json` digit-for-digit
   (3.583518938456110001624954716761404545446; −7.167037876912220003249909433522809090892).
   Full nonzero-Λ set for n ≤ 100 = exactly the 22 entries of the on-disk JSON, every exact form
   and value matching; support off prime powers = {6, 14, 21, 36, 46, 54, 69, 84, 86, 94} and
   negative set = {36, 54, 84}, both matching the note.
7. **Genus identity** (r_{Q₁}(n) + r_{Q₂}(n))/2 = Σ_{d|n} χ₋₂₀(d): holds EXACTLY for all
   n ≤ 200 (own Jacobi-symbol implementation, own enumeration of both forms). **ζ_K contrast:**
   Λ_K from c_n = Σ_{d|n} χ₋₂₀(d) is prime-power-supported and ≥ 0 with zero violations to
   n = 200. Both checks replicate.
8. **χ₄:** Λ_{χ₄}(3) = −log 3 exactly (rational-vector recursion).
9. **Char-p accounting:** E: y² = x³ + x + 1 counted by direct enumeration over F₇, F₄₉ =
   F₇[t]/(t²+1), F₃₄₃ = F₇[t]/(t³+t+1): N₁ = 5, N₂ = 55, N₃ = 380 (points at infinity included);
   trace a = 3, and N₂, N₃ reproduce from α+β = 3, αβ = 7. Bidegrees of Γ_{F^k} = (1, 7^k) —
   degrees see only the main terms; the zero side −(α^k+β^k) lives in the Δ-intersection.
   The note's §3.5 is correct in every particular.
10. **P¹×P¹ counterexample:** Γ_n ≡ nξ₁ + ξ₂ verified consistent three ways (Γ_n·ξ₁ = 1,
    Γ_n·ξ₂ = n, self-intersection 2n against adjunction g = 0); Δ ≡ ξ₁ + ξ₂ (Δ² = 2 = deg T_{P¹});
    (Γ_n·Δ) = n + 1 by classes AND by the fixed-point count (n−1 roots of z^{n−1} = 1, plus 0, ∞;
    all transverse since d/dz(z^n) ≠ 1 there); (Γ₆·Δ) = 7 ≠ 12 = (Γ₂·Δ)(Γ₃·Δ). Composition
    Γ_m∘Γ_n = Γ_mn is exact function composition; bidegree multiplicativity
    d_i(Ψ′∘Ψ) = d_i(Ψ′)d_i(Ψ) re-derived (generic-fiber composition). The system satisfies
    (PF1)–(PF4) as claimed: O(1,1) ample hence nef; Γ_p primitive exactly at primes; every Γ_n an
    effective irreducible curve. It does NOT satisfy PF5's family-stability clause (Γ_n^t has
    bidegree (n,1), not of the form Γ_m) — see MAJOR 1(ii).
11. **§5 monoid computation re-derived:** for totally multiplicative a_n with a₁ = 1,
    D = Π_p(1−a_p p^{−s})^{−1} and −D′/D = Σ_p Σ_k a_p^k log p · p^{−ks} — prime-power support
    and Λ_D(p^k) = a_p^k log p are formal; with effectivity + nef, a_p ≥ 0, hence Λ_D ≥ 0.
    Correct and cheap as claimed — modulo the attachment ambiguity of MAJOR 3.
12. **Fork exhaustiveness examined:** the airtight form of the dichotomy is "the counting
    functional either factors through composition (Horn A) or it does not (any non-multiplicative
    reading — trace or otherwise — breaks step 2's formal monoid algebra and needs a tie axiom,
    which makes the exclusion definitional; Horn B's analysis applies verbatim)". The note's
    printed version routes through the H⁰/H²-vs-H¹ cohomological gloss with an empirical clause
    ("in every known template") — see minor 5. The conclusion (axiom statement on every branch)
    is unaffected.

**Citation checks (standing order 1 — online where reachable).** Network this session: direct
arxiv.org/github.com unreachable (IPv6 ISP issue); WebSearch (server-side) worked; on-disk PDFs
used where the program's source IS the disk. Verified: DMV = Diamond–Montgomery–Vorhauer,
"Beurling primes with large oscillation", Math. Ann. 334 (2006) 1–36 — confirmed from the on-disk
PDF title page (`fetched/p1-02`). Kaczorowski–Perelli I (Acta Math. 182 (1999) 207–241) and VII
(1 < d < 2, Ann. of Math. 173 (2011) 1397–1441) — confirmed online. Broucke-school IDs confirmed
online: arXiv:2309.01567 (Broucke–Debruyne–Révész, [α,β]-systems; published Trans. AMS 378 (2025)
477–501), arXiv:2507.13780 (Broucke, zeros on prescribed contours, none to the right),
arXiv:2102.08478 (Broucke–Vindas discretization; Math. Z. 307 (2024), art. 62). Bost
arXiv:1512.08946 (theta invariants h⁰_θ) confirmed online. NOT independently re-confirmed this
pass (program-verified upstream; flagged per standing order 5): van der Geer–Schoof math/9802121;
Yuan–Zhang arXiv:2105.13587 v9 = Annals of Mathematics Studies 223; Chen–Moriwaki arXiv:1903.10798
(the volume identity q-13a WAS verified by the adjudication's direct PDF inspection, computation
f). Blomer–Leung: see MAJOR 2.

---

## 3. FATAL findings

None.

## 4. MAJOR findings (must fix before external circulation)

### MAJOR 1 — PF5's printed content is never audited against the note's own claims (two manifestations of one root).

**(i) The I.2 clause vs PF5's FE shadow.** §2 (PF5) says the axiom's "numerical shadow is the
s ↦ 1−s … symmetry of the functional equation of D." §7 then says: "**The axiom a DMV world
violates: currently NONE**" and "Every coefficient-level consequence of (PF1)–(PF6) (prime-power
support + Λ ≥ 0) holds in these worlds by construction." A hostile referee will put these side by
side and object: generic Beurling/DMV zeta functions satisfy NO functional equation, so they
violate PF5's stated shadow — either "currently none" is wrong or PF5 is not an axiom. The
resolution is already implicit in the note (PF5 is "stated here at template level only: no
candidate substrate currently instantiates it for any D," hence contributes no operative,
checkable coefficient-level consequence) but it is left for the reader to assemble. Note also
that the zoo IV.10 rider, the note's source for the positivity-filter classification, scopes the
Beurling-instantiability claim to the axiom class "AS PRINTED" — i.e., pre-PF5; the note's
extension of that claim to "(PF1)–(PF6)" is exactly where this gap opens.
**(ii) The §3.2 counterexample vs PF5's stability clause.** §3.2 scopes the P¹×P¹ exhibit to
"(PF1)–(PF4)" and adds "Whether (PF5) in a sharpened form excludes it is not adjudicated and not
claimed." In fact no sharpening is needed for the stability half: the printed PF5's "The family
is stable under transpose" ALREADY fails for {Γ_{z↦z^n}} (Γ_n^t has bidegree (n,1), which is not
any Γ_m). So the exhibit certifies vacuity of the (PF1)–(PF4) fragment, and the note's "the
identical system would serve D = ζ, D = DH, or D = Epstein indifferently" is a statement about
that fragment — as printed, a careful referee will catch that the full six-axiom class has no
known trivial member and ask whether the vacuity argument still bites.

**Required fix (one short "PF5 status" paragraph, in §2 or §3.2):** state explicitly that
(a) PF5's transpose-stability clause already fails for the §3.2 family, so the exhibit
demonstrates vacuity of (PF1)–(PF4), and no transpose-stable instantiation of the full class is
known for any D — consistent with PF5's uninstantiated-template status and changing nothing in
the fork (Horn A's step 1 and step 3 do not use the exhibit); (b) in the §7 accounting, PF5 is
excluded from "the axiom a DMV world violates" because it is an uninstantiated template with no
operative coefficient-level consequence; if its FE shadow were imposed directly on D as an
analytic requirement, FE-free Beurling systems would fail it — but that would be an analytic
condition inserted by hand, not an axiom any substrate enforces, and the class would still sit
below the I.7 bracket (no Ramanujan input, no degree-one-rigidity derivation), so the
positivity-filter classification and the relocation order are unchanged.

### MAJOR 2 — The Blomer–Leung citation carries a volume number contradicted by this pass's online check.

The note (§1 and §7, following zoo I.1) cites "the Blomer–Leung monoid converse … **Adv. Math.
471 (2026) 110716**." Three independent web searches this session consistently identify the
Blomer–Leung beyond-endoscopy converse paper ("A GL(3) converse theorem via a 'beyond endoscopy'
approach," arXiv:2401.04037) as **Advances in Mathematics, Volume 485, February 2026**. I could
not independently confirm the article number 110716 for either volume (ScienceDirect and doi.org
unreachable from this machine), so this is a discrepancy flag, not a verified correction — but a
wrong volume in a load-bearing citation of an externally circulated note is exactly what a
hostile referee checks first. **Required fix:** re-verify the bibliographic record when the
network allows (or from the publisher's page), correct the volume in BOTH the note (two
occurrences) and `BARRIER-ZOO.md` I.1, and add the stable handle "arXiv:2401.04037" alongside the
journal citation so the reference survives any residual bibliographic drift.

### MAJOR 3 — §5's attachment functional is ambiguous exactly where the note's one positive claim lives.

§5: "(PF3) makes n ↦ (degree data of Ψ_n) a monoid homomorphism" and "a_p = (degree of the
effective Ψ_p against the nef polarization-normalized fiber data) ≥ 0." By the note's own §3.1,
only the individual bidegree components d_i(Ψ) = (Ψ·ξ_i) (and monomials in them) are
multiplicative under composition; the degree against the polarization itself
(Ψ·L̄, an ξ₁+ξ₂-type pairing) is NOT (e.g. on graphs, (1+n)(1+m) ≠ 1+nm). As printed, "degree
data … a monoid homomorphism" and "against the nef polarization-normalized fiber data" leave open
the non-multiplicative reading, and a hostile referee will ask which functional is meant — an
attack the program has already priced once (R8). **Required fix (one sentence):** fix the
attachment explicitly, e.g. "a_n := d₂(Ψ_n) = (Ψ_n · ξ₂), the second-fiber degree — the char-p
analog of deg(F^k) = q^k; d₂ is a monoid homomorphism by §3.1, and a_p = d₂(Ψ_p) ≥ 0 because ξ₂
is nef and Ψ_p effective" (or the declared multiplicative monomial in the bidegrees, if more
generality is wanted).

## 5. MINOR findings

1. **Mixed index bases in adjudication references.** Front matter cites "mandatory_repairs[1]"
   for the M0 repricing repair — 0-based (0-based [1] is the repricing entry). §9 cites
   "mandatory_repairs[3]" for the positivity-filter/S1 rewrite — 1-based (0-based would be [2]).
   §1 cites "killer_findings_upheld[2]" for the Lemma-B kill — 1-based (0-based [1]). Fix: cite
   by quoted opening phrase ("the repair beginning 'Reprice M0 …'") or normalize all indices to
   one convention and say which.
2. **Decimal-rendering convention.** §6.1's table prints Λ_DH(4) as "−1.4422320…"; the true
   expansion begins −1.44223196…, so under the ellipsis-means-truncation convention the printed
   digits are wrong (they are the 8-significant-digit ROUNDING). Print "−1.44223196…" or
   "≈ −1.4422320". Same convention note for κ: the 41st printed digit (9) is rounded (true
   continuation …9091088…); add "(rounded)" or truncate.
3. **§6.1's recursion display** "a_n log n = Σ_{d|n} Λ(d) a_{n/d}" uses bare Λ for Λ_DH; a reader
   primed by classical notation will misread Λ as the Riemann von Mangoldt function. Write
   Λ_DH (or Λ_D) in the displayed identity.
4. **Stale corpus statement in §9.** The traceability row says "the intersection-theory Mémoire
   arXiv:2103.15646 is NOT on disk — adjudication computation f." True at adjudication time,
   false now: `results/corpus-routing.md` caveat 14 records it fetched and title-verified
   2026-08-26 as `fetched-r3/r3s-07`. Update to "not on disk at adjudication time; since fetched
   as fetched-r3/r3s-07 (corpus-routing caveat 14)."
5. **§3.4's exhaustiveness is under-defended as printed.** The clause "in every known template
   the zero side IS the H¹ trace, so there is no third reading" is empirical; a referee can ask
   why a functional that is neither bidegree-multiplicative nor H¹-trace is impossible. The
   airtight form costs one sentence: the primary dichotomy is "factors through composition or
   not"; ANY non-multiplicative reading (trace or otherwise) breaks step 2's formal monoid
   algebra and needs an organizing tie axiom, which makes the exclusion definitional — Horn B's
   analysis verbatim; the H⁰/H²-vs-H¹ trichotomy is then the template interpretation, not the
   load-bearing case split.
6. **§6.2's "RH-false class" label carries no citation.** For external circulation, add the
   classical source for off-line zeros of Epstein zetas with h > 1 (Davenport–Heilbronn 1936,
   J. London Math. Soc. — zeros with σ > 1 for class-number > 1 forms), or the program's
   preferred on-disk equivalent; as printed the RH-false claim, though standard and not
   load-bearing for the exclusion computation, is the one unreferenced assertion in §6.
7. **§6.2 check 2's "provably the class-orbit-breaking" compresses a two-part argument.** What is
   proved: (a) ζ_Q fails admissibility (exact witnesses); (b) the full class-group average
   ζ_K = ζ·L(χ₋₂₀) satisfies it (a theorem — Dedekind zeta — numerically cross-checked to
   n ≤ 200). The mechanism attribution is the interpretation of (a)+(b). Recommended phrasing:
   "the violation tracks exactly the class-orbit-breaking: the orbit average (a theorem-level
   Euler product) passes, the single-class evaluation fails" — keeping "provably" attached to
   (a) and (b) rather than to the interpretive sentence.

## 6. External-circulation assessment

Would a hostile professional referee find an error? **No mathematical error exists to find**: all
six witnesses, both closed-form families, the F₇ accounting, and the P¹×P¹ counterexample are
correct and were replicated here from scratch, and the FE and off-line zero were re-verified
independently to residuals ≤ 1e−60. Would they find an overclaim? The scope discipline is the
strongest part of the document — the status block, §5's citation form ("D is inadmissible …,"
never "D admits no …"), §7's relocation order, and §8's negative list close every route the
adjudication struck. What a hostile referee WILL find, as printed: the PF5 tension of MAJOR 1
(reads as an internal contradiction until repaired), the §5 ambiguity of MAJOR 3 (the R8-style
attack surface, at the note's one positive claim), and — if they check references — the MAJOR 2
volume discrepancy. With those three repaired and the minors swept, the note is
external-circulation ready as an axiom statement plus witness record; nothing in it can be quoted
back as a theorem claim.

*(Referee pass complete. U.S. English. Session 6+, 2026-08-26.)*
