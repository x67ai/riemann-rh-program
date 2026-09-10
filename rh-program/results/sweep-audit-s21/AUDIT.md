# Standing-order-6 REFINEMENT AUDIT of the closed Grossmann sweep

**Rank 4, Session 21. Written 2026-09-10. Literature-and-record only: no scouting, no construction, no re-run of the sweep.**
Brief: `results/sweep-audit-s21/BRIEF.md`. Deliverable written incrementally; a partial file is a valid input for the next session.

---

## §1 Method

### §1.1 The order being audited

Standing order 6 (STATUS.md line 34) carries a refinement adopted by the orchestrator on 2026-09-09,
after the sweep had already closed. Quoted verbatim from STATUS.md line 34:

> **Refinement (adopted by the orchestrator 2026-09-09, on the sponsor's observation; the sponsor left the decision to the program):** in 1912 no literature connected gravitation to Riemannian geometry; Grossmann matched Einstein's REQUIREMENT (metric = field, general covariance) against a branch on its internal properties. So every Grossmann-style scout judges fit against S1–S5 only; the absence of any published connection between a branch and ζ is never evidence against it — that absence is the Grossmann condition, not a defect. A scout that discards a branch for "no RH literature" has misread the order.

The sweep closed 2026-08-19. STATUS.md line ~52 records the closure verdict:

> **SWEEP VERDICT: NO GROSSMANN — "the generator exists but the geometry does not."**

The verdicts therefore predate the refinement and were never read against it. This audit reads them
against it, one report at a time.

### §1.2 The specification the scouts were judging against

STATUS.md lines 93–99, quoted for the record because every classification below turns on it:

> - S1 Euler-product sensitivity: consume an input DH/Epstein violate (multiplicativity at every prime beyond L²-means; Ramanujan; note Λ(n) ≥ 0 pointwise is itself such an input).
> - S2 o(N)-sensitivity: must see a SINGLE off-line zero; all density/proportion methods are structurally blind to o(N) exceptions.
> - S3 Multiplicity-visibility: on-line double vs off-line pair must be distinguishable (Weil-form signature is not; K_a de Branges kernels are).
> - S4 A new positivity GENERATOR, not just a bigger Weil-positivity cone (algebraic: Hodge index/ampleness; analytic: reflection positivity/complete monotonicity; combinatorial: Lorentzian polynomials; probabilistic: determinantal/negative association).
> - S5 Survive the named no-gos: AH world, Bombieri–Garrett 94%, parity, Conrey–Li, Λ ≥ 0, bandwidth/two-moment ceilings.

The S6 amendment (STATUS line ~52, "**S6 amendment to the spec (finite-rank/tower rationality + doubled object)**")
postdates the sweep and is not a ground any sweep verdict could have used; it is noted where a report's
material bears on it, but it is never used to classify.

### §1.3 The corpus

38 reports, all carrying the same schema (`branch`, `verdict`, `confidence`, `fit.S1`–`fit.S5`,
`key_objects`, `prior_attacks`, `live_entry_points`, `first_interface`, `access_failures`,
`verified_online`, `recalled_unverified`):

| file | reports | verdict split |
|---|---|---|
| `results/grossmann-sweep.json` | 27 | 21 instrument, 5 dead-end, 1 grossmann-candidate |
| `results/grossmann-sweep2.json` | 9 | 7 instrument, 2 dead-end |
| `results/grossmann-sweep2-partial.json` | 2 | 2 instrument |

There is no free-text `rationale` field. **The verdict rationale is the `fit.S1`–`fit.S5` block plus
`first_interface`**, and those are the fields quoted throughout. Reports are cited as `W1-nn`
(wave 1, `grossmann-sweep.json` index), `W2-nn` (`grossmann-sweep2.json` index), `WP-nn`
(`grossmann-sweep2-partial.json` index), with the field name attached to every quotation
(e.g. `W1-00 fit.S4`). Four branches were scouted twice by different models (determinantal ×2,
de Branges ×2 in wave 1); both runs are audited as separate rows, since each carries its own verdict.

Extraction was by `python3 -c "import json; ..."` over the three files; every rationale field of every
report was read in full, not grepped. Grep was used only afterwards, as a completeness check that no
absence-pattern sentence had been missed.

### §1.4 The two kinds of clause

Per the brief, each rationale sentence was sorted into one of two bins.

**Absence-of-literature clause** — a sentence whose force is that no one has published the
connection: patterns `no papers`, `nobody has`, `never been applied`, `no literature`, `unexplored`,
`not pursued`, `zero papers`, `no known connection`, `does not exist in the literature`,
`never made into an inequality by anyone`, `no theorem yet`, `nothing existing in the branch`,
and their paraphrases. Under the refinement these carry **no weight against a branch**.

**Internal S1–S5 clause** — a sentence stating a property of the branch's own mathematics that
fails the spec, independent of who has written about ζ:
(i) a *model-world kill* — DH/Epstein satisfy the branch's axioms, so the branch cannot separate them (S1);
(ii) *Weil positivity reparametrized* — the branch's positivity target is provably a change of coordinates on the Weil cone (S4);
(iii) *o(N)-blindness* — the branch's objects are densities, averages, measures, or limits that erase a single exception (S2);
(iv) *equivalence-level* — the branch's criterion is proven equivalent to RH, hence carries no independent content;
(v) *ensemble-level* — the statement is about a random ensemble, undefined for the single deterministic zero set;
(vi) *a no-go theorem in print* — a published impossibility aimed at the branch (Conrey–Li, Deninger's real-coefficient no-go, the AH world, Gesteau–Liu, Blomer–Leung, …).

A published no-go is an **internal** ground, not an absence ground: it says the mathematics cannot work,
not that no one has tried.

### §1.5 The classification test

Each row is assigned exactly one class:

- **(A)** verdict rests on internal S1–S5 grounds alone; any absence clause is missing or decorative.
- **(B)** MIXED — both kinds present, but the internal grounds are sufficient on their own.
- **(C)** MIXED — the internal grounds are INSUFFICIENT once the absence clause is struck.
- **(D)** rests on absence alone.

The (B)/(C) line is drawn by one strict question, applied to every mixed row: **strike every
absence-of-literature sentence from the rationale; does the recorded verdict still follow from what
remains?** If what remains is a model-world kill, a proven reparametrization, an o(N) argument, an
equivalence, an ensemble-level objection, or a no-go in print, the answer is yes and the row is (B).
If what remains is only a low score with no stated internal mechanism — or if the only stated
mechanism is that the bridge has not been built — the answer is no and the row is (C).

Two calibration notes, applied uniformly:

1. **"No mechanism exists" is ambiguous and is read in context.** "No deterministic certificate form
   exists in the literature" is an absence clause. "The objects are measures, so for a single
   deterministic configuration they are undefined" is an internal clause, and it is the one doing the
   work in that row. Where both appear in the same sentence — the pattern the reader flagged in
   `grossmann-sweep2.json` `wave2_summary` — the sentence is split and both halves are quoted.
2. **`instrument` is a weaker verdict than `dead-end`.** An `instrument` verdict says the branch
   supplies tools but is not itself the Grossmann branch; it does not discard the branch. A `dead-end`
   verdict certifies the corner closed and enters the zoo. The (C) test is therefore applied hardest
   to the `dead-end` rows and to the `instrument` rows whose fit block contains an explicit
   "not the branch" finding, since those are the verdicts the refinement could overturn.

3. **"The object does not exist" is internal; "no one has connected it to ζ" is absence.** Grossmann's
   Riemannian geometry existed as finished mathematics; what was missing was the published link to
   gravitation. A report that says the branch's own enabling object has never been built — the square
   of Spec Z, a cohomology with the required coefficients, a deterministic certificate form for a
   fixed configuration — is stating that the branch does not contain the generator, which is an S4
   ground about the mathematics, not a Grossmann-condition absence. It is classified internal, and is
   flagged in the row where it is load-bearing. A report that says no *paper* couples the branch to ζ,
   RH or L-functions is classified absence, whatever else the sentence contains.

### §1.6 Scope limits

This audit does not re-scout, does not evaluate whether any branch actually fits S1–S5, and does not
change any verdict. It classifies the *grounds on record*. Where a row is (C) or (D), §3 names the
S1–S5 fit question a re-scout would have to answer and the zoo entries that would bind it at brief
time — the question only, never an answer.

---

## §2 The table

Legend: **v** = recorded verdict/confidence. Quotations are ≤ 2 sentences per cell and carry the
field they came from. `…` marks elision inside a quoted sentence.

### W1-00 — determinantal point processes / negative association / rigidity (Ghosh–Peres, Lyons, hyperuniformity/stealth)

- **v:** instrument, 0.75
- **Internal S1–S5 grounds (quoted):** `fit.S2` — "Rigidity (Ghosh-Peres) and negative association are properties of a probability MEASURE (zero-one laws on tail sigma-algebras); for the single deterministic zero configuration they are literally undefined, and every deterministic shadow … erases o(N) off-line defects by construction." `fit.S5` — "The Alternative Hypothesis world (arXiv:2507.06823) is a direct kill: everything the branch can verify about zeta's zero statistics is band-limited (|alpha|<1), and AH-consistent processes match all of it."
- **Absence-of-literature clauses (quoted):** `fit.S4` — "But NO deterministic certificate form exists in the literature (verified by search: nobody has published 'fixed configuration satisfies checkable DPP-property X => on a line'), so the generator currently has no bridge to a fixed zero set." `fit.S3` — "No proof mechanism exists, but the reformulation is exactly S3-shaped."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** Strike both absence sentences and the ensemble-level objection (S2: measure-theoretic properties undefined on one deterministic configuration), the model-world kill (S1: "DH/Epstein zero ordinates satisfy every band-limited statistical property the branch can check at axiom level"), and the AH no-go in print (S5) all stand unchanged. The instrument verdict follows from those alone.

### W1-01 — de Branges spaces & Krein canonical systems (Suzuki, Lagarias, Kaltenbäck–Woracek)

- **v:** instrument, 0.72
- **Internal S1–S5 grounds (quoted):** `fit.S1` — "the axioms are pure entire-function/operator theory: DH and Epstein (h>1) inhabit the SAME classes (as indefinite/Pontryagin objects with kappa>0), so nothing in the framework consumes the Euler product at the axiom level". `fit.S4` — "every positivity target the branch has ever produced (Hermite-Biehler property, Hamiltonian H >= 0, screw-function non-positive-definiteness, Li's lambda_n >= 0, de Branges' conditions) is Weil positivity reparametrized (Bombieri-Lagarias for Li; Suzuki explicitly; H>=0 <=> HB <=> quasi-RH by construction)".
- **Absence-of-literature clauses (quoted):** `fit.S4` — "Only faint untested candidate for a new generator: the de Branges chain total-ordering rigidity, never made into an inequality by anyone."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The model-world kill (S1), the proven reparametrization (S4, with the Bombieri–Lagarias pin), and the Conrey–Li no-go plus this program's own C1 containment theorem (`fit.S5`: "Conrey-Li is a named S5 no-go aimed precisely at this branch") are each independently sufficient for `instrument`. The one absence sentence is a note on a residual candidate, not a ground.

### W1-02 — determinantal point processes / negative association / rigidity (second scout, independent model)

- **v:** instrument, 0.78
- **Internal S1–S5 grounds (quoted):** `fit.S2` — "Rigidity and negative association are properties of a probability MEASURE (tail sigma-algebra zero-one laws); for the single deterministic zero configuration they are undefined … even a proven 'zeros converge to sine process' would not imply RH." `fit.S5` — "stealth/maximal-rigidity machinery requires a structure-factor GAP (Lachieze-Rey arXiv:2512.10686, verified this run: gap or cone hypotheses, no NT content) which the zeta form factor F~|alpha| does not have".
- **Absence-of-literature clauses (quoted):** `fit.S4` — "But NO deterministic certificate form applicable to a fixed configuration exists anywhere in the literature (absence re-confirmed online this run, 2013-2026)". `fit.S1` — "no DPP-side theorem has a slot where Lambda(n)>=0 or multiplicativity could enter."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** Both absence sentences struck, the ensemble-level objection, the AH kill, and the structure-factor-gap mismatch (an internal property of the zeta form factor, not a literature fact) remain and carry the verdict. Note that the S1 absence clause has an internal twin in the same cell — "DH/Epstein ordinates satisfy every band-limited statistical property the branch can check at axiom level" — which is the model-world kill and survives on its own.

### W1-03 — F1-geometry: Λ-rings, blueprints, arithmetic site (Borger, Soulé, Deitmar, Lorscheid, Connes–Consani)

- **v:** instrument, 0.72
- **Internal S1–S5 grounds (quoted):** `fit.S4` — "however its own stated closing inequality (dim H^0(D)+dim H^0(-D) >= (1/2)D.D with D.D<0) is the Weil explicit-formula positivity restated geometrically - the generator is a target, not a theorem, and as of today the route terminates on Weil positivity in new clothes." `fit.S2` — "the enabling object (cohomology + intersection theory on the square) provably does not exist yet in any formalism (verified against Connes' own essay and the June 2026 paper)."
- **Absence-of-literature clauses (quoted):** `fit.S1` — "but no theorem yet converts this input into zero-location leverage."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The S4 ground is a reparametrization finding about the branch's own closing inequality and is decisive on its own; the S2 sentence is classified internal under §1.5 note 3 (the branch does not contain the object, as against no one having linked it to ζ). Striking the S1 absence clause leaves S1 scored 3/5 on a genuine axiom-level Euler input — "Borger's Lambda-structure IS 'compatible Frobenius lifts at every prime' … DH/Epstein admit no Lambda-structure or arithmetic-site analogue" — which strengthens the branch and still does not make it the Grossmann branch, because S4 fails internally.

### W1-04 — arakelov-hodge-index (Arakelov/arithmetic intersection theory, Hodge index over Spec Z, Connes–Consani absolute geometry)

- **v:** grossmann-candidate, 0.55 — the sweep's only candidate
- **Internal S1–S5 grounds (quoted):** `fit.S4` — "But over Spec Z the generator itself IS the missing ingredient; a lazily-built version collapses back into the Weil cone (Connes-Consani Selecta 2021 archimedean positivity is a reparametrized Weil-cone fragment)." `fit.S5` — "One branch-specific no-go verified: Deninger arXiv:2204.02714 — no finite-dimensional Weil cohomology with REAL coefficients exists for arithmetic curves — which kills the naive 'find H^1 with cup product' realization".
- **Absence-of-literature clauses (quoted):** none. The nearest sentence, `fit.S4` — "Score is for a theorem-shaped target, not an existing theorem" — is a statement about the branch's own mathematics, not about the ζ literature.
- **CLASSIFICATION: (A) internal alone.** The verdict is the sweep's one positive verdict, so an absence clause could not be operating against the branch in any case; the grounds recorded are an axiom-level S1 pass, an S2 mechanism claim (Castelnuovo/Hodge index "bounds EVERY Frobenius eigenvalue at once"), and two named internal obstructions.

### W1-05 — fourier-duality-crystalline (Fourier optimization / interpolation / crystalline measures & Fourier quasicrystals)

- **v:** instrument, 0.70
- **Internal S1–S5 grounds (quoted):** `fit.S1` — "the BRS interpolation duality holds for general Dirichlet series with FE (DH passes, so the filter fails at axiom level)". `fit.S4` — "Cohn-Elkies/Fourier-optimization is structurally a sign-constrained LP cone paired with the explicit formula, i.e., a reparametrized/bigger Weil cone (exactly what S4 bans)".
- **Absence-of-literature clauses (quoted):** `fit.S1` — "the one Euler-grade hook the framing exposes (prime-side spectrum positivity, Λ(n)≥0 pointwise — which DH violates) is used by NO theorem in the branch."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The model-world kill and the reparametrization finding each carry the verdict alone, and `fit.S5` adds a published classification acting as a no-go — "the explicit-formula pair is NOT a Fourier quasicrystal even under RH (prime-side measure Σ Λ(n)δ_{log n} has exponentially growing local mass; zero density grows), so zeta sits outside every rigidity theorem" — which is a class mismatch between zeta and the branch's theorems, not a gap in the literature.

### W1-06 — de Branges spaces & Krein canonical systems (second scout, independent model)

- **v:** instrument, 0.75
- **Internal S1–S5 grounds (quoted):** `fit.S4` — "Bombieri-Lagarias JNT 77 (1999) 274-287 shows the lambda_n are Weil-functional values at specific test functions (VERIFIED this run); Suzuki self-declares the analogy; H>=0 iff HB iff quasi-RH by the Krein-de Branges bijection itself." `fit.S4` — "The single distinct sufficient-condition family (de Branges' own) was killed by Conrey-Li IMRN 2000(18) 929-940 (VERIFIED: their examples show the conditions fail for the RKHS defining functions built from zeta)."
- **Absence-of-literature clauses (quoted):** `fit.S4` — "Only faint untested candidate for a new generator: the de Branges chain total-ordering rigidity, never converted into an inequality by anyone."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** Two source-pinned internal grounds — an equivalence-level finding (Li's λ_n are Weil-functional values; H ≥ 0 ⟺ quasi-RH by the bijection) and a published no-go verified against the paper — plus the S1 model-world kill ("DH and Epstein (h>1) inhabit the SAME classes"). The verdict stands with the absence sentence struck.

### W1-07 — automorphic forms / functoriality positivity (Rankin–Selberg nonnegativity, symmetric-power towers, period-square central-value positivity)

- **v:** instrument, 0.80 — the sweep's only S1 = 5
- **Internal S1–S5 grounds (quoted):** `fit.S4` — "two genuine, proven, non-Weil-cone positivity generators exist (RS coefficient nonnegativity in Re(s)>1 …; period-square/doubling nonnegativity of central values, Waldspurger/Lapid-Rallis), but each is domain-locked: the first to the edge of absolute convergence, the second to the central point — neither reaches arbitrary points of the critical line." `fit.S3` — "the one multiplicity-visible object (Zagier 1981: Casimir spectrum contains rho(1-rho) with multiplicity >= n for an n-fold zero) lives in a non-unitarizable representation, so no positivity attaches to it".
- **Absence-of-literature clauses (quoted):** `fit.S5` — "the 60-year edge-cap (pole-anchored positivity has never produced any interior zero-location result) functions as an unformalized ceiling."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The domain-lock is a proven analytic property of the two generators (region of absolute convergence; the single central point), not a fact about who has written what; with the 60-year sentence struck it still holds, and `fit.S2` adds the o(N)-blindness of the branch's interior tool ("in the strip interior the branch offers only density theorems (arXiv:2408.13682), which are structurally o(N)-blind") together with the named Bombieri–Garrett ~94% cap. The report itself is explicit that the absence sentence is not a theorem — it calls it "unformalized" — and its own `first_interface` proposes converting it into one, which is the correct disposal of an absence ground.

### W1-08 — additive combinatorics: Gowers uniformity of the primes (Green–Tao–Ziegler, Matomäki–Radziwiłł, Tao–Teräväinen, Leng–Sah–Sawhney, Pilatte)

- **v:** instrument, 0.80
- **Internal S1–S5 grounds (quoted):** `fit.S2` — "the branch's provable ceiling is log-power/quasi-log savings, structurally blind to any individual zero, and its bounds are themselves downstream of zeta zero-free regions (circularity)." `fit.S4` — "Gowers norms are averaging norms whose inverse theorem outputs nilsequence STRUCTURE, not a positivity certificate over zeros; nothing lands in any sanctioned generator class."
- **Absence-of-literature clauses (quoted):** `first_interface` — "any proposal claiming U^k input at the wall must exhibit signed power-saving cancellation, which no theorem in the branch provides."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The scale argument is quantitative and internal — log-power savings against the X^β scale at which a single off-line zero acts — and `fit.S5` names the parity problem as "this branch's own native wall". The single absence clause sits inside the interface proposal, not the fit block, and striking it changes nothing.

### W1-09 — noncommutative geometry: adele class space, prolate operators (Connes / Connes–Consani / CCM; Bost–Connes)

- **v:** instrument, 0.75
- **Internal S1–S5 grounds (quoted):** `fit.S5` — "Every proven positivity result in the branch currently sits inside the Bombieri small-support no-go zone (the campaign's own interval-arithmetic certification on [1/3,3], primes 2,3,5,7, was judged RH-content-nil by its own author); Meyer 2005 is a branch-internal no-go showing spectral realization alone has zero RH content." `fit.S4` — "the published quantities (Fuchs 1964 e^{-4 pi lambda^2} prolate-leakage law; CCM 2511.22755 Fig. 4 …) show the generator's margin collapses exponentially exactly at the semilocal step where primes enter".
- **Absence-of-literature clauses (quoted):** `fit.S3` — "no proven multiplicity-visible mechanism exists in the branch."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** Two branch-internal no-gos in print (Bombieri small support; Meyer 2005) plus a quantitative margin-collapse law with its own source pins carry the verdict without the S3 sentence. The S1 reservation — "the two missing theorems of the live strategy … have no identified step that fails for DH" — is an internal discrimination gap, and it was later settled inside the program by computation, not by literature search (STATUS: "CCM DH-filter DECIDED (Session 5, 2026-08-19): ARITHMETIC-BLIND, confidence 0.85").

### W1-10 — random-matrix-moments (Keating–Snaith, CFKRS recipe, ratios conjectures, FHK maxima, n-level correlations)

- **v:** instrument, 0.85
- **Internal S1–S5 grounds (quoted):** `fit.S2` — "the branch's classically maximal payoff is Lindelöf (verified: LH is EQUIVALENT to I_k << T^{1+eps} for all k, and LH does not imply RH); … a single off-line zero contributes O(1/N) and is invisible. Structural, not contingent." `fit.S1` — "the CUE/CbetaE model itself contains no primes and the a_k factor is glued on by a heuristic recipe (verified: Keating-Snaith CMP 2000 splits c_k = a_k·f_k with a_k inserted by hand), so nothing here excludes DH/Epstein at the axiom level."
- **Absence-of-literature clauses (quoted):** none. The negative sentences are properties of the objects — "the CFKRS/ratios formalism generates identities and asymptotics, not positivity" (`fit.S4`) — not statements about the literature's coverage.
- **CLASSIFICATION: (A) internal alone.** Every ground is a model-world kill, an o(N)/normalization argument, an equivalence (LH), or the AH no-go in print (`fit.S5`, arXiv:2507.06823).

### W1-11 — reflection-positivity-qft (Osterwalder–Schrader, chessboard/lattice RP, Neeb–Ólafsson, Bost–Connes and Knauf chains) — **DEAD-END**

- **v:** dead-end, 0.70
- **Internal S1–S5 grounds (quoted):** `fit.S4` — "every proven instance attaches positivity to the WRONG variable (external field / state positivity, not temperature), and every attempt to attach RP to the critical line itself collapses to Weil positivity ⟺ RH (the C1 adjudication's containment theorem is this program's formal proof of that collapse for prime-computable observables)." `fit.S5` — "The branch's proven statements stop at the Euler-region boundary (β=1 pole, β=2 magnetization transition), i.e. below even de la Vallée Poussin content about zeros".
- **Absence-of-literature clauses (quoted):** `fit.S1` — "but no theorem converts this axiom-level input into any constraint on zeros." `first_interface` — "the Ramanujan claim is relocated square-root cancellation with no known source, so the interface is a restatement of RH-strength input, not machinery for producing it."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** Tested at dead-end strictness: strike both absence sentences and what remains is a wrong-variable finding about the branch's own proven generators plus a proven collapse to Weil positivity ⟺ RH backed by this program's own C1 containment theorem — an S4 kill and an equivalence-level kill, either sufficient. The `first_interface` caveat is itself internal in its main clause ("its proven generators … provably yield only the trivial half-plane"); only the "no known source" tail is an absence clause.

### W1-12 — berry-keating-xp (Hilbert–Pólya operator constructions: xp and successors; CCM zeta spectral triples)

- **v:** instrument, 0.72
- **Internal S1–S5 grounds (quoted):** `fit.S5` — "self-adjointness-with-zeros-as-spectrum is essentially equivalent to RH, and the two rigorous audits of the genre (Bellissard on BBM; Feldmann on Yakaboylu, showing the needed completeness ≡ Nyman–Beurling) each found exactly that circularity." `fit.S3` — "the CCM mechanism is built on the Weil quadratic form, whose signature is exactly the multiplicity-blind object named in the spec".
- **Absence-of-literature clauses (quoted):** `fit.S5` — "but no published argument verifies escape, and the cap must be re-checked against any interface theorem." `fit.S1` — "but no theorem yet shows the DH/Epstein analogue of the construction FAILS the even-simple-ground-state hypothesis, so axiom-level discrimination is unproven."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The equivalence-level finding with two named audits, and the multiplicity-blindness of the Weil form, stand with both absence sentences struck. The S1 reservation was the one clause a literature search could not settle, and the program settled it by its own computation rather than by search — the CCM DH-filter test returned ARITHMETIC-BLIND at 0.85, which converts that reservation into an internal ground after the fact.

### W1-13 — transfer operators & thermodynamic formalism (Mayer/Gauss map, Lewis–Zagier, Ruelle zeta, Dolgopyat, Pollicott–Sharp)

- **v:** instrument, 0.72
- **Internal S1–S5 grounds (quoted):** `fit.S4` — "This is the fatal row. … The Fraczek-Mayer character-deformation experiments show determinant-of-nuclear-operator structure alone does NOT force zeros onto lines (lambda=+1 zeros move off under deformation)." `fit.S4` — "Dolgopyat/UNI cancellation is a genuinely non-Weil generator but structurally yields only resonance-free STRIPS (zero-free-region strength), never the line."
- **Absence-of-literature clauses (quoted):** `fit.S1` — "but no theorem in the branch consumes that input toward on-line-ness; it is only used to build the encoding." `fit.S3` — "no branch tool exploits this". `first_interface` — "no candidate Q_s is known".
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The report names S4 as "the fatal row" and supports it with a published counterexample family (Frączek–Mayer: nuclear-determinant structure does not force zeros onto a line) and a structural ceiling on the branch's one non-Weil generator (strips, not the line), reinforced by the Bombieri–Garrett cap on the natural repair (`fit.S5`). Three absence clauses are present and all three can be struck without touching that argument.

### W1-14 — Lorentzian polynomials & log-concavity technology (Brändén–Huh, Jensen–Pólya/GORZ, Borcea–Brändén stability preservers, Laguerre–Pólya/heat flow) — **DEAD-END**

- **v:** dead-end, 0.82
- **Internal S1–S5 grounds (quoted):** `fit.S1` — "VERIFIED arithmetic-blind at the axiom level: the branch's flagship theorems (Ki cosine universality, Gunns-Hughes extended-Selberg-class generalization, GORZ Hermite universality, Dobner's Lambda>=0) consume only FE + archimedean Taylor-coefficient asymptotics and hold verbatim for RH-violating extended-Selberg-class members and even Poisson random functions". `fit.S5` — "the branch walks directly into its own named no-go: Rodgers-Tao Lambda>=0 (extended by Dobner with 'no information about the zeros') says the Laguerre-Polya boundary has zero margin … the DH/Epstein filter kills every actually-built object in the branch."
- **Absence-of-literature clauses (quoted):** `fit.S1` — "zero published attempts to couple an Euler-product input into the Lorentzian/exchange-property framework (arXiv null searches)." `fit.S4` — "but there is no object anywhere encoding zeta zeros as a Lorentzian family". `first_interface` — "No publication attempts any statement of this shape".
- **CLASSIFICATION: (C) MIXED, internal INSUFFICIENT without the absence clause.** The internal grounds are decisive for everything the branch has actually built — the report says so in terms, "the DH/Epstein filter kills every actually-built object in the branch" — and would fully carry an `instrument` or "no current fit" verdict. They do not carry a **dead-end certificate**, which closes the corner including the sector the report itself describes as unbuilt: `fit.S4` grants that "Lorentzian polynomials ARE a sanctioned non-Weil positivity generator (discrete Hodge-Riemann …) and the generator genuinely exists as mathematics", and the only stated reason the unbuilt multiplicative-Lorentzian sector is closed is that nobody has written it — "zero published attempts", "no object anywhere", "No publication attempts any statement of this shape". Strike those three sentences and the closure of that sector has no remaining support; the Chassé/Farmer T² dispersal result and the Λ ≥ 0 no-margin wall both bind the Jensen/Taylor-coefficient wing, and the report's own `first_interface` says the replacement "coefficients must come from the prime side", i.e. from outside the wing those no-gos govern. This is the Grossmann condition being read as a defect.

### W1-15 — Deninger cohomological program & Weil-étale cohomology (foliated dynamical systems, regularized determinants; Lichtenbaum/Flach–Morin; Kucharczyk–Scholze)

- **v:** instrument, 0.75
- **Internal S1–S5 grounds (quoted):** `fit.S4` — "BUT if the scalar product on H^1_dyn is ASSUMED rather than derived from a constructed space, it is exactly Weil positivity in disguise (the campaign's known failure signature)." `fit.S4` — "Deninger states in print that the conformal-metric mechanism 'will not exist for dynamical systems relevant to number fields' (Kähler identities on cohomology needed) and that leafwise Hodge decomposition FAILS for non-Riemannian foliations (Deninger–Singhof counterexample)."
- **Absence-of-literature clauses (quoted):** none. `fit.S5` — "The route is blocked by its own 30-year existence problem (the space), not by any named no-go" — is classified internal under §1.5 note 3: the branch does not yet contain the object, which is an S4 statement about the mathematics.
- **CLASSIFICATION: (A) internal alone.** Two printed statements by the branch's own author function as branch-internal no-gos, and the circularity risk on the inner product is a reparametrization finding. The verdict is `instrument`, and the branch remained on the sweep's shortlist, so nothing was discarded here in any case.

### W1-16 — p-adic L-functions & Iwasawa theory — **DEAD-END**

- **v:** dead-end, 0.80
- **Internal S1–S5 grounds (quoted):** `first_interface` — "KNOWN STRUCTURAL OBSTRUCTION any proof must overcome (and the precise reason the branch is scored dead): the Amice/Mellin transform of a p-adic measure on Z_p^x sees exactly the continuous p-adic characters, whose archimedean shadows are the integers; the points 1/2+it with t real nonzero are not p-adic characters, and NO sequence of arithmetic points in weight space has archimedean shadows accumulating at them — the p-adic and archimedean topologies on the s-line are transverse away from the interpolation integers". `fit.S3` — "at the central interpolation point the branch is exactly multiplicity-visible …, but this visibility provably stops at the interpolation locus and never reaches generic zeros 1/2+it."
- **Absence-of-literature clauses (quoted):** `fit.S1` — "and no theorem consumes the motivic input toward archimedean zero location."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** Tested at dead-end strictness: the transversality obstruction is a structural fact about the p-adic and archimedean topologies, stated so that it binds any future construction and not merely the existing ones, and it is exactly the ground the report names as "the precise reason the branch is scored dead". The one absence sentence is redundant beside it.

### W1-17 — free-probability-operators (finite free convolution, MSS interlacing, heat flow, tracial Positivstellensätze)

- **v:** instrument, 0.78
- **Internal S1–S5 grounds (quoted):** `fit.S1` — "the finite-free/heat-flow machinery applies to arbitrary Laguerre-Pólya-type entire functions and would process an RH-false lookalike identically". `fit.S4` — "(a) real-rootedness/interlacing preservation under finite free convolution (MSS line) … PRESERVES rather than CREATES hyperbolicity, and Rodgers-Tao Λ>=0 (no margin below criticality) makes preservation-only arguments structurally insufficient for ξ; (b) … post-MIP*=RE the general trace-positivity cone is undecidable, and any encoding of the explicit-formula functional is Weil positivity in disguise."
- **Absence-of-literature clauses (quoted):** `fit.S3` — "no multiplicity-visible invariant exists in the branch."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** A model-world kill, a preserves-not-creates structural argument against the branch's own generator sharpened by the Λ ≥ 0 no-margin theorem, an undecidability result against the second generator, and a reparametrization finding — four internal grounds, none of which depends on the S3 sentence.

### W1-18 — motives-periods (Beilinson conjectures, mixed motives, motivic Galois groups, Kontsevich–Zagier periods)

- **v:** instrument, 0.72
- **Internal S1–S5 grounds (quoted):** `fit.S5` — "its proposed mechanism is a nonexistent cohomology whose postulated positivity risks being Weil positivity in disguise unless ampleness is independently constructed (Deninger's explicit-formula-as-Lefschetz reading is a repackaging of the Weil form)." `fit.S4` — "but over Z no positivity theorem exists, and the construction burden sits in the Arakelov/F1 scouts, not here."
- **Absence-of-literature clauses (quoted):** `fit.S1` — "but the branch supplies no operator that consumes this input toward zero location."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The reparametrization finding is the operative ground and is source-pinned to Deninger's own reading of the explicit formula; the verdict also correctly routes the branch's positive content (weight purity, the height-pairing blueprint) to the Arakelov/F1/Deninger scouts rather than discarding it, so the absence sentence is not carrying the verdict.

### W1-19 — selberg-ihara-worked-examples (comparative anatomy of the true RH cases: Weil/Deligne function fields, Selberg, Ihara/graph, Dwork, Goss)

- **v:** instrument, 0.78
- **Internal S1–S5 grounds (quoted):** `fit.S4` — "Design rule extracted: the generator always acts on a DOUBLED object, never on the zeta's own explicit formula; Weil positivity over Z is the diagonal shadow of the missing Hodge-index inequality — assuming it is assuming the conclusion, matching the campaign post-mortem." `fit.S2` — "even in the best random ensemble only ~69% of d-regular graphs are Ramanujan (Huang-McKenzie-Yau, verified), i.e. ensemble/density methods cap strictly below 1 even in the toy world where RH is decidable."
- **Absence-of-literature clauses (quoted):** `fit.S5` — "but survival for zeta itself hinges on a substrate (square of Spec Z, Frobenius tower) that published mathematics does not yet contain."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The branch is comparative anatomy of cases where RH is proven, so `instrument` is the only verdict available to it whatever the literature says; the internal grounds — the doubled-object design rule, the diagonal-shadow circularity, and a quantitative ensemble ceiling with its source pin — are what the verdict actually turns on. The S5 sentence is phrased as a literature absence but its content is the same missing-substrate fact recorded internally at W1-04 `fit.S4`.

### W1-20 — model theory, o-minimality, decidability (Pila–Wilkie/André–Oort, Zilber pseudoexponentiation, continuous logic, adelic model theory) — **DEAD-END**

- **v:** dead-end, 0.85
- **Internal S1–S5 grounds (quoted):** `fit.S1` — "fatal at the axiom level: R_an-definability of a restricted analytic box is IDENTICAL for zeta, Davenport-Heilbronn, and Epstein; nothing in o-minimality/model theory consumes Euler products, Lambda(n)>=0, or multiplicativity, so the branch cannot distinguish zeta from RH-false lookalikes even in principle." `fit.S5` — "it fails before them at the definability threshold (unrestricted zeta on the strip is not definable in any o-minimal expansion; Voronin universality makes the vertical-shift family anti-tame)".
- **Absence-of-literature clauses (quoted):** none.
- **CLASSIFICATION: (A) internal alone.** A model-world kill stated to hold "even in principle", a definability obstruction proved from the infinite discrete zero set and Voronin universality, and `fit.S4` = 0 — "the branch contains no positivity notion of any kind (no cone, no trace form, no log-concavity, no determinantal structure)". The report's own `first_interface` is explicit that the interface it names is "branch-CLOSING rather than branch-connecting" and that even the positive direction "still fails S1: Davenport-Heilbronn satisfies the identical definability hypothesis". Nothing here turns on what has been published.

### W1-21 — certified-computation-sat (certified computation as proof machinery; the Λ>0 disproof channel)

- **v:** instrument, 0.90
- **Internal S1–S5 grounds (quoted):** `fit.S1` — "DH-blind BY THEOREM: Dobner (Acta Arith. 201, 2021, verified) proves Lambda>=0 for the whole extended Selberg class from the functional equation alone, no Euler product". `fit.S4` — "no positivity generator at all: SAT/DRAT/LP/SDP technology is a certificate FORMAT, not a generator; the zeta-side LP/SDP instantiation is Fourier-optimization/small-support Weil positivity, which is another scout's branch and unconditional-hence-empty per Bombieri."
- **Absence-of-literature clauses (quoted):** none.
- **CLASSIFICATION: (A) internal alone.** A theorem in print (Dobner) supplies the model-world kill; the format-not-generator finding is a property of the technology. The verdict is `instrument` at the sweep's highest confidence, and the branch was commissioned as direction D1 rather than discarded.

### W1-22 — Beurling generalized primes: the negative space (DMV barriers, Zhang, Hilberdink, Broucke–Debruyne–Vindas–Révész)

- **v:** instrument, 0.87
- **Internal S1–S5 grounds (quoted):** `fit.S1` — "Beurling worlds have full Euler product, multiplicativity at every prime, and Lambda>=0 pointwise (automatic from the Euler product), yet violate RH maximally (DMV 2006; BDR 2023 [alpha,beta]-systems with beta=1/2+eps, alpha->1)". `fit.S4` — "The branch generates counterexamples, not positivity; it contains no positivity generator of any sanctioned class."
- **Absence-of-literature clauses (quoted):** none. `fit.S1` — "but the branch supplies no positive S1 input itself" — is a statement about the branch's own content, not about the ζ literature.
- **CLASSIFICATION: (A) internal alone.** The branch is the sweep's no-go engine: its own theorems build RH-false worlds satisfying the candidate axiom sets, which is an internal S1/S5 finding of the strongest kind, and `fit.S2` = 0 records density-blindness. `instrument` is the correct grade for a corner whose function is calibration.

### W1-23 — arithmetic-que-microlocal (arithmetic quantum ergodicity, Eisenstein QUE, entropy/measure rigidity, microlocal positivity) — **DEAD-END**

- **v:** dead-end, 0.72
- **Internal S1–S5 grounds (quoted):** `fit.S4` — "Sharp Garding/Fefferman-Phong certify positivity only modulo lower-order losses, while RH has zero margin (Rodgers-Tao Lambda>=0: 'barely true'), a structural mismatch". `fit.S5` — "the branch's equivalence statements (horocycle rate, Lax-Phillips causality) are Weil-positivity-style reparametrizations; exponent-1/2 rate statements are consistent with the AH world", together with the Bombieri–Garrett ~94% cap on its spectral corner.
- **Absence-of-literature clauses (quoted):** `fit.S4` — "verified NO prior art exists (arXiv full-text search 'Garding inequality'+'Riemann hypothesis' returns 0 results)". `fit.S2` — "(verified: no 2020-2026 progress toward 3/4 in the closed-horocycle literature)". `first_interface` — "45+ years of effective-unipotent technology has never beaten the spectral exponent 1/2 on the modular surface (verified through 2026)".
- **CLASSIFICATION: (B) MIXED, internal sufficient.** This row carries the purest absence sentence in wave 1 — a null arXiv search reported as a finding — and it is exactly the kind the refinement bars. It is nevertheless not load-bearing: struck, the same `fit.S4` cell still contains a margin mismatch that is a mathematical property of Gårding/Fefferman–Phong positivity against a zero-margin target, `fit.S1` still records that "every known proof of a horocycle rate routes back through zeta's own zero data (circular), and QUE technology consumes L-function bounds rather than producing them", and the Bombieri–Garrett no-go still caps the spectral corner. Verjovsky's optimality of the exponent 1/2 for rough observables, cited in `first_interface`, is a theorem, not an absence. Recorded here as a **near miss**: the row survives the test on the strength of one cell.

### W1-24 — hyperuniformity-coulomb (Coulomb gases, hyperuniformity, universality of log-gases, DLR/Gibbs description of Sine_β)

- **v:** instrument, 0.80
- **Internal S1–S5 grounds (quoted):** `fit.S1` — "the AH lattice processes (Lagarias-Rodgers 1905.12123, 1907.03391, verified) satisfy every statistical input the branch could consume, so it fails the DH filter at the axiom level." `fit.S3` — "the 1D log-gas lives on the projected line: an on-line double zero and an off-line pair produce identical counting measures there (the Weil-form blindness reproduced exactly)".
- **Absence-of-literature clauses (quoted):** `fit.S3` — "the honest 2D Coulomb picture (charges in the strip) has no line-condensation theorem and none is in sight."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The AH kill binds every statistic the branch can supply, not merely the ones written down; the projected-line multiplicity blindness is a property of the objects; and `fit.S5` adds the decisive already-in-hand argument — "zeta's hyperuniformity (number variance ~ log log T, far below Poisson) is ALREADY unconditionally known via Selberg's CLT yet decides nothing — the branch's flagship output is in hand for zeta and provably insufficient." That last is the opposite of an absence ground: the connection exists and has been evaluated.

### W1-25 — condensed mathematics & analytic stacks over Z (Clausen–Scholze: light condensed sets, analytic rings/stacks, six-functor formalism, Berkovich motives)

- **v:** instrument, 0.60 — the lowest confidence in wave 1
- **Internal S1–S5 grounds (quoted):** `fit.S2` — "that layer does not exist at all today — the required global object is described by the authors themselves as 'very speculative ... if such an object even exists' (Analytic Stacks Lecture 1, verified from crowd-sourced notes)." `fit.S4` — "the risk that 'ampleness over Spec Z x Spec Z' is itself RH-equivalent (Weil-positivity-in-disguise) is unexamined."
- **Absence-of-literature clauses (quoted):** `fit.S1` — "but no such formula exists in the corpus — verified: zero arXiv papers connect condensed math/analytic stacks to zeta or RH, and the Berkovich-motives paper (arXiv:2412.03382, JAMS 2026) never mentions zeta/Weil cohomology." `fit.S4` — "the branch contains ZERO positivity theorems, the authors nowhere name positivity as a target or obstruction in any written source I could access".
- **CLASSIFICATION: (C) MIXED, internal INSUFFICIENT without the absence clause.** Strike the two absence sentences and the fit block reads as a positive S1 statement — "A cohomological determinant/trace formula for completed zeta over a global analytic stack would consume the full arithmetic of Spec Z at the AXIOM level (DH/Epstein L-functions are not the zeta function of any geometric object, so they are excluded by construction, not by estimates)" — plus `fit.S4`'s "Hodge index/ampleness is precisely S4's sanctioned algebraic generator and this branch is the leading candidate SUBSTRATE to host it (proper smooth analytic curves over R exist: the FF curve over R / twistor-P1, verified)" and `fit.S5` = 3/5 exempting it from every named no-go. What is then left against it is that the global object has not been built — which is the same ground on which W1-04 (arakelov-hodge-index) was graded **grossmann-candidate**, not instrument. The relegation to `instrument` is therefore absence-assisted: two of the five fit cells are docked in terms by a null literature search and by what the authors have not written down.

### W1-26 — lee-yang-stat-mech (Lee–Yang circle theorem, Newman class L, Asano contraction, de Bruijn–Newman kernel)

- **v:** instrument, 0.72 — the synthesis calls this branch the sweep's "dark horse"
- **Internal S1–S5 grounds (quoted):** `fit.S1` — "Dobner (Acta Arith. 201 (2021), arXiv:2005.05142, verified) proves Newman's conjecture Λ≥0 for the WHOLE extended Selberg class (DH-type functions included), so the dBN/LP framework treats zeta and RH-false lookalikes identically". `fit.S5` — "Rodgers-Tao Λ≥0 means any Lee-Yang realization of Φ must be EXACTLY critical — zero margin, so all robust/perturbative/approximation-with-slack versions are excluded a priori".
- **Absence-of-literature clauses (quoted):** `fit.S1` — "the only S1-grade input (a prime-factorized ferromagnetic representation of the kernel Φ, which DH's kernel must provably lack since DH violates RH) is an unbuilt hypothetical, not existing machinery." `fit.S4` — "Docked 1 point because every KNOWN bridge to zeta (Ξ∈LP, Λ=0, Gröchenig's PF criterion, van Dantzig membership) is an RH-EQUIVALENT reformulation — the generator side has never been connected to xi."
- **CLASSIFICATION: (C) MIXED, internal INSUFFICIENT without the absence clause.** The report's own scores are S2 = 4/5 ("Lee-Yang is an exact all-zeros mechanism, not a density statement"), S4 = 4/5 ("genuinely NOT Weil positivity in disguise: coupling positivity J_ij≥0 is a strictly-stronger-than-conclusion sufficient condition with its own combinatorial proof engine"), S5 = 3/5 (survives the named no-gos). The Dobner kill lands on the dBN/LP wing as built, not on the prime-factorized ferromagnetic representation the report's own `first_interface` specifies; the S4 docking is scoped in terms to "every KNOWN bridge"; and the zero-margin constraint is a condition any realization must meet, which the interface accepts, not a proof that none exists. Strike the two absence sentences and what remains is a sanctioned non-Weil generator with an all-zeros mechanism, no binding no-go, and an unbuilt bridge — which is the Grossmann condition as the refinement defines it.

### W2-00 — pretentious-multiplicative (Granville–Soundararajan pretentious distance, Halász theory, Koukoulopoulos treatise)

- **v:** instrument, 0.85
- **Internal S1–S5 grounds (quoted):** `fit.S2` — "The school's own book formalizes the o(N)-blindness as a theorem: avg over |t|<=T of D(f,p^{it};x)^2 = log log x + O(1) … and 'we cannot hope, using only these methods, to improve the error term to better than (log log x)/log x' (GS book draft, Ex. 2.3.1 + p.74 verbatim) — … a single zero at any fixed sigma<1 is categorically invisible." `fit.S4` — "the 3-4-1 inequality, which is exactly Fejér-square positivity 3+4cos(t)+cos(2t)=2(1+cos t)^2>=0 — the identical 1899-vintage generator behind classical zero-free regions, edge-capped for 125 years".
- **Absence-of-literature clauses (quoted):** `fit.S3` — "no pretentious statement even mentions zero multiplicity."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The o(N)-blindness is a quantitative theorem out of the school's own textbook with a page pin, the S4 finding identifies the branch's positivity as a 125-year-old reparametrization, and `fit.S5` adds the parity wall in Granville's own words. The S3 sentence is an absence clause but its first half — "D counts primes, not zeros" — is the internal reason and stands alone.

### W2-01 — harper-multiplicative-chaos (random multiplicative functions, low moments, critical & Gaussian multiplicative chaos)

- **v:** instrument, 0.85
- **Internal S1–S5 grounds (quoted):** `fit.S2` — "Wintner 1944 is the canonical exhibit: RH holds a.s. in the model while nothing follows for mu." `fit.S4` — "multiplicative chaos is not determinantal/negatively associated, and Newman–Wu (arXiv:1708.08820, verified in wave-1) proved the Lee-Yang property FAILS for complex GMC — the branch's chaos objects demonstrably do not feed the analytic positivity generator."
- **Absence-of-literature clauses (quoted):** none.
- **CLASSIFICATION: (A) internal alone.** Every ground is a theorem or a structural property: an ensemble-level kill with a 1944 exhibit, a published failure of the Lee–Yang property for the branch's own objects, and `fit.S5`'s positive obstruction — "the model's sharp a.s. fluctuation scale sqrt(x)(loglog x)^{1/4} … disagrees with the Gonek–Ng conjectured sqrt(x)(logloglog x)^{5/4} for the true M(x) — the i.i.d.-on-primes model provably miscalibrates exactly at the scale where zero-correlation (RH-relevant) information lives."

### W2-02 — riemann-hilbert-painleve (Deift–Its school, isomonodromy, tau functions; Fokas unified-transform zeta program)

- **v:** instrument, 0.82
- **Internal S1–S5 grounds (quoted):** `fit.S1` — "Every zeta-DIRECT object in the branch (Its's theta-jump RHP, Fokas's linear integral equation …, Suzuki's integral operators) is built from functional-equation/theta/L^2-grade data that DH and Epstein … share identically at the axiom level". `fit.S4` — "RHP/isomonodromy theory is an identity-and-asymptotics technology, not a positivity technology: the Malgrange form on monodromy manifolds is symplectic, not positive; no positivity generator of any sanctioned class lives here".
- **Absence-of-literature clauses (quoted):** `fit.S1` — "the Euler product enters NO Riemann-Hilbert formulation anywhere in the literature (arXiv sweeps this run, 2003-2026)." `fit.S2` — "but no zeta-side instance exists".
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The symplectic-not-positive fact about the Malgrange form is a property of the branch's geometry and binds any future construction inside it, and the report draws the verdict from it explicitly in `first_interface`: "even full success yields an exact encoding instrument — the S4 generator would still have to be imported from elsewhere; this interface therefore certifies the branch as instrument, not candidate." The model-world kill and the Lindelöf ceiling on the Fokas route both survive the strike as well.

### W2-03 — tomita-takesaki-entropy (modular theory, Araki relative entropy, half-sided modular inclusions; Bost–Connes/adele-class modular structure) — **DEAD-END**

- **v:** dead-end, 0.72
- **Internal S1–S5 grounds (quoted):** `fit.S1` — "it is provably ERASED at the von Neumann/modular layer where the branch's positivity generators live: for beta in (0,1] the KMS GNS factor is the injective type III_1 factor, unique up to isomorphism (Connes-Haagerup), so every modular invariant … of the arithmetic system coincides with that of any sufficiently mixing counterfeit — the DH filter fails at exactly the layer where the machinery operates." `fit.S4` — "(ii) is published as unavailable for the arithmetic thermal system (Gesteau-Liu 2408.12642 Prop 2.11: the Riemannium/primon gas admits NO half-sided modular inclusion at ANY temperature — discrete spectral support {log p} kills it …)".
- **Absence-of-literature clauses (quoted):** `fit.S4` — "and (i) has no bridge, anywhere in the literature, from state-space entropy inequalities to zero locations — every executed arithmetic instance lands in the Euler region."
- **CLASSIFICATION: (B) MIXED, internal sufficient.** Tested at dead-end strictness. The uniqueness of the injective type III_1 factor is a classification theorem, and its consequence — that every modular invariant of the arithmetic system equals that of a counterfeit — is a model-world kill that binds any construction operating at that layer, not only the ones written down. Gesteau–Liu is a no-go in print aimed at the branch's second generator. The absence sentence covers the first generator (relative entropy) only, and even there the internal half — "every executed arithmetic instance lands in the Euler region" — is a location fact, not a coverage fact.

### W2-04 — weyl-group-mds (Bump–Friedberg–Goldfeld, Diaconu–Goldfeld–Hoffstein moments, Chinta–Gunnells, Sawin–Whitehead classification)

- **v:** instrument, 0.85
- **Internal S1–S5 grounds (quoted):** `fit.S2` — "in the continued MDS the zeta zeros appear as locations of polar divisors (scattering-type denominators), so the continuation is valid wherever the zeros happen to be — the mechanism is agnostic to, not constraining of, zero position; a single off-line zero of the diagonal zeta factor changes nothing the branch proves." `fit.S4` — "the one positivity present (L(1/2,chi_d) >= 0 …) is imported Waldspurger-square positivity …, and the function-field engine's positivity (Sawin's perverse sheaves, decomposition theorem) is imported Deligne purity — i.e., RH-already-proven substrate. The branch consumes positivity; it generates continuation."
- **Absence-of-literature clauses (quoted):** `fit.S4` — "No MDS-native positivity generator exists in the literature".
- **CLASSIFICATION: (B) MIXED, internal sufficient.** The agnosticism argument is the decisive internal ground — the machinery's conclusions are invariant under moving the diagonal factor's zeros — and it is reinforced by a printed natural-boundary theorem (`fit.S5`: "Diaconu-Garrett-Goldfeld proved the naive moment-MDS class has NATURAL BOUNDARIES (Progr. Math. 300, 2012)") and by the Lindelöf ceiling. The opening absence clause is immediately followed in the same cell by the internal reason (imported positivity), which is what carries the verdict.

