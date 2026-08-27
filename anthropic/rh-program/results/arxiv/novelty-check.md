# Independent novelty check — the four circulation documents

**Date: 2026-08-27.** CIRCULATION-PREP.md STEP 2 deliverable.

**Method.** Each of the four documents was given to two independent agents: a first-pass sweep
(read the document in full, then run a fresh literature sweep) and an adversary whose only brief
was to *refute* the sweep by finding an anticipation. Where the two disagree, this report
adjudicates explicitly and says which was followed; the verdicts below are not an average of the
two. **Where the adversary produced a verified anticipation, the adversary wins.**

**Prior homework on disk, cross-referenced throughout:**

* `results/c3-r/prior-art-r7a.md` — the extended R7(a) gate (2026-08-26), verdict
  NOVEL-WITH-CITATIONS with 7 citation obligations, written primarily for the seed note and
  covering the three C3-r notes.
* `LOG.md` Session 7 — records the A4 referees' external prior-art sweep as "CLEAN (novelty
  survives)", with no queries logged and no standalone gate report on disk.

**Already-established dated correction, recorded here for the register.** `prior-art-r7a.md` §5
and §6 item 6 originally attributed arXiv:1507.06480, *A taste of Weil theory in characteristic
one*, to M. J. Shai Haran. **It is by Koen Thas** (EMS 2016 chapter in *Absolute Arithmetic and
F₁-Geometry*, pp. 365–386); Thas's chapter surveys Haran's program and quotes him verbatim, so the
*content* of the gate's Haran claim is correct but the source was wrong. The primary source is
S. Haran, *Index theory, potential theory, and the Riemann hypothesis*, LMS Lecture Note Ser. 153,
CUP 1991, 257–270, at p. 259 (MR1110396). The correction was applied on **2026-08-27** to
`results/c3-r/prior-art-r7a.md` §§5–6, to `results/c3-r/seed-no-go-note.md`, and to
`results/arxiv/seed-no-go/main.tex` (key `Ha15` → `Ha91`). Both agents on the seed note
re-confirmed the misattribution independently this session; the adversary additionally confirmed
the repair is already on disk, so the sweep's report of it as a live defect is **stale**.

---

## Summary of verdicts

| Document | File | Verdict | Citation actions |
|---|---|---|---|
| A4 no-go (two-moment certificate under cubic augmentation) | `results/a4-no-go/paper.md` | **NOVEL-WITH-CITATIONS** | 10 MUST + 3 SHOULD |
| M0 axiom class (polarized-Frobenius) | `results/c3-r/m0-axiom-note.md` | **NOVEL-WITH-CITATIONS** | 10 MUST + 7 SHOULD |
| M1 non-circularity (Castelnuovo–Severi / Hodge index) | `results/c3-r/m1-noncircularity.md` | **ANTICIPATED-BY** (standard mathematics; the note says so itself and is right) | 10 MUST + 4 SHOULD |
| Seed no-go (per-prime Tate curve products) | `results/c3-r/seed-no-go-note.md` | **ANTICIPATED-BY** on the rigidity; the no-go survives | 10 MUST + 5 SHOULD |

**59 citation actions in total (40 MUST, 19 SHOULD)**, plus nine textual repairs that are not
citations. Details in "Actions required before posting".

---

# 1. A4 no-go — `results/a4-no-go/paper.md`

*"The two-moment certificate is robust under Rudnick–Sarnak-range cubic augmentation with capacity
control"* (dated revision 2026-08-27).

## Verdict: NOVEL-WITH-CITATIONS

The headline — δ₀ = 0 exactly, for a λ′ = 1/2 cubic/ladder/capacity block adjoined to a
bandwidth-one Frobenius baseline, at both the 5/6 and 2/3 corners — is not stated anywhere either
agent could reach, and the adversary attacked it hard and failed. But the paper is **not postable
on its current citation apparatus**: the External References section carries two entries while the
body relies on at least ten external results by name, and two of the closest neighbors in the
world are unmentioned.

## Adjudication of the disagreement

The sweep and the adversary agree on the verdict and disagree on two things. **The adversary wins
both.**

**(a) The closest published third-party paper.** The sweep did not find it; the adversary did, by
citation-graph traversal from Chirre–Gonçalves–de Laat rather than keyword search:

> **F. Gonçalves, D. de Laat, N. Leijenhorst, "Multiplicity of nontrivial zeros of primitive
> L-functions via higher-level correlations", Mathematics of Computation (2024),
> doi:10.1090/mcom/4005; arXiv:2303.01095 (v2, 20 Mar 2025).**

This is a semidefinite program on the Hejhal / Rudnick–Sarnak *n*-level correlation asymptotic in
the restricted support Σ|x_j| < 2/m, bounding the fraction of zeros of multiplicity ≤ n−1. Under
GRH it gives at least 96.14% of zeta zeros of multiplicity ≤ 2 and 97.87% of multiplicity ≤ 3 —
i.e. **for them the third-level datum pays**. Their §1 also remarks, of the very row system A4
uses: *"We also adapted the problem in (4) to bound N_n(T) directly, but we were not able to
improve over the results in (6) in this way"*, where N_k(T) = Σ m^{k−1} is exactly A4's power-moment
trace system. It does not anticipate δ₀ = 0 (GRH-conditional; full n-level distribution against
arbitrary admissible test functions rather than one scalar trace row of total Fourier support
(k−1)λ′ = 1 + o(1); different target; positive answer, not negative), but a referee reading A4's
"adds exactly nothing" against a Math. Comp. paper that gets a new bound from the third level will
require the reconciliation paragraph. **MUST cite, in §1.2 and again at Theorem 3.4.**

**(b) The grade on Claim 2 (the affine-plane identity / "cubic blindness").** The sweep graded it
NOVEL-WITH-CITATIONS. The adversary downgrades the **atom half** to STANDARD-MATHEMATICS and is
right: GdLL equation (5), N_n(T) = Σ_k S(n,k) M_k(T) with S the Stirling numbers of the second
kind, gives at n = 3 exactly

    C − 3F + 2·Mass  =  Σ m³ − 3 Σ m² + 2 Σ m  =  Σ m(m−1)(m−2),

which is the atom half of A4's Theorem 3.4 character for character, including the consequence A4
draws (vanishing on marks {1,2}) — that is precisely why GdLL target "multiplicity ≤ n−1" with the
falling factorial rather than the simple-zero count. The adversary re-derived the translation and
it is exact. **What survives as A4's own is the pair term** 6 Σ m_p²(m_p−1)A_p² — signature-(1,1)
blocks sitting on the plane c = 3F − 2 at *every* depth — and it survives only because GdLL assume
GRH and therefore have no off-line blocks. That half is the half that matters for `lemmaR_tight`.

## Claim-by-claim

| # | Claim | Verdict |
|---|---|---|
| 1 | δ₀ = 0 exactly under two-bandwidth cubic augmentation, both benchmarks | **NOVEL-WITH-CITATIONS** |
| 2 | Affine-plane identity / cubic blindness | **STANDARD-MATHEMATICS on the atom class** (GdLL eq. (5)); **NOVEL** on the pair class |
| 3 | Grid Parseval decoupling at bandwidth one | Identity **STANDARD-MATHEMATICS**; two-bandwidth decoupling **NOVEL-WITH-CITATIONS** |
| 4 | Sharp capacity theorem, constant 2√2 | **NOVEL** (method standard) |
| 5 | Garnish theorem (divergent-cutoff vacuity) | **NOVEL** (moral is optimization folklore) |
| 6 | Fractional-mark discovery (5/6 is an integrality theorem) | **NOVEL-WITH-CITATIONS**; the abstract moral is the textbook integrality gap |
| 7 | Pair-interference channel closure | **NOVEL** (objects internal to the gate model) |

**On claim 1, the nearest prior art is the parent paper's own §7.2(e)** — and the manuscript's only
engagement with it is one passing clause pointing at a **"Section 7.5(e)" that does not exist**
(the parent's §7 has 7.1, 7.2 with items (a)–(f), 7.3, then Remark 7.1 and Appendix A). Both agents
read the parent's §7.2 verbatim from `sources-extracted/v5_p13.txt` and agree. The current arXiv
version says *"…at X ≍ T this allows only k = 1. Thus, unconditionally, higher moments add
nothing."* The **earlier version** — whose title the manuscript actually cites — says it at exactly
A4's operating point: *"for λ ∈ (½,1) this allows at most k = 3 (and only for λ < ⅔), and an odd
moment does not lower Λ₁(0). Thus, unconditionally, higher moments add nothing to the n₊-bound on
(½,1) … while for λ ≤ ½, where many moments are available, Proposition 7.4 makes them useless."*
A4's question is genuinely different — the parent's remark is single-bandwidth, A4's is a λ′ = 1/2
block adjoined to a bandwidth-one baseline, and rows useless alone can bind when adjoined — but a
**quoting-and-distinguishing paragraph is mandatory**, or the abstract reads as re-deriving a
remark already in print.

**On claim 4, the sweep re-derived Theorem 7.1 independently and confirms it.** h³ ≤ a h² +
(h³ − a h²)₊; Tonelli against the ladder gives 2C/a; minimizing a ε_g + 2C/a at a = √(2C/ε_g) gives
2√2·√(C ε_g); the density 4C h⁻⁵ on (a,∞) attains it. Proposition 7.2's refutation of the 5/√3
profile also checks out. **Claim 4 is correct as printed.**

**Two further findings the sweep did not have** (adversary, verified on disk from
`fetched/w-08-…pdf`): Chirre–Gonçalves–de Laat is not merely a missing reference entry — their
Corollary 3 gives distinct zeros N_d ≥ 0.8477 N (RH) / 0.8486 N (GRH), **above** A4's model corner
5/6 = 0.8333, via their inequality (7) attributed there to "an argument of Ghosh", which is the
published convex-programming form of the second integrality level A4's Lemma 4.2 uses. And their
history line quotes **Farmer–Gonek–Lee's published distinct-zeros constant 0.8051**, which collides
to four decimals with A4's headline LP optimum 0.8050956815843511. In a paper about distinct zeros
of zeta, one disambiguating sentence is needed wherever 0.8051 appears.

## Cross-reference to prior homework

**CORRECTS `LOG.md` Session 7.** The A4 referees' sweep is recorded there as "CLEAN (novelty
survives)" with no queries logged. Novelty does survive, but the record is not clean: the parent's
own §7.2(e) is an informal precursor that the manuscript neither quotes nor distinguishes and
points at with a nonexistent section number; the closest published third-party work
(Gonçalves–de Laat–Leijenhorst, Math. Comp. 2024) is unmentioned; and ten external results are
named in the body with no reference entry. Session 7's verdict should be re-recorded as
NOVEL-WITH-CITATIONS with the obligations below.

## Searches run (A4)

Sweep:

* WebSearch: "More than two thirds of the zeros of the Riemann zeta function lie on the critical line" (located parent: arXiv:2608.13637 + two Anthropic-hosted CDN PDFs)
* curl https://arxiv.org/abs/2608.13637 — title, abstract, authors (Levent Alpöge, Ralph Furman), v1 13 Aug 2026 / v2 19 Aug 2026
* Semantic Scholar graph API: `paper/arXiv:2608.13637` with references + citations (33 references; 1 citing paper, arXiv:2608.16034)
* curl https://arxiv.org/abs/2608.16034 — abstract of the only citing paper (prime-modulus Dirichlet family; no cubic-augmentation content)
* curl of the two Anthropic-hosted parent PDFs + pdftotext + grep `third trace|tr G3|third moment|higher moments` (recovered the earlier-version §7.2(e) wording)
* arXiv API: `all:"triple correlation" AND all:"zeta"`; `all:"triple correlation" AND all:"simple zeros"`
* arXiv API: `all:"simple zeros" AND all:"linear programming" AND all:"zeta"`
* arXiv API: `all:"Fourier optimization" AND all:"Riemann zeta"`; `… AND all:"pair correlation"`
* arXiv API: `all:"explicit formula" AND all:"no-go"`
* arXiv API: `all:"pair correlation" AND all:"n-level" AND all:"simple zeros"`
* arXiv API: `all:"higher correlations" AND all:"alternative hypothesis"` (surfaced Lagarias–Rodgers 1905.12123)
* arXiv API: `abs:"proportion of simple zeros" AND abs:"pair correlation"`
* arXiv API: `all:"semidefinite programming" AND all:"zeros of the Riemann zeta"`
* arXiv API: `all:"three-level" AND all:"zeros" AND all:"zeta" AND all:"proportion"`
* arXiv API: `abs:"n-level correlations" AND abs:"lattice"` (surfaced Lagarias–Rodgers 1907.03391)
* arXiv API: `all:"realizability" AND all:"point processes" AND all:"correlation functions"`; `au:"Kuna" AND abs:"realizability"`
* arXiv API: `all:"Schatten" AND all:"zeros of the Riemann zeta"`
* arXiv API: `all:"eigenvalue counting" AND all:"explicit formula" AND all:"Gabor"`; `all:"Gabor" AND all:"Riemann zeta"`
* arXiv API: `abs:"third moment" AND abs:"zeros" AND abs:"critical line"`; `abs:"cubic" AND abs:"zeros of the Riemann zeta"`
* arXiv API: `all:"Weil" AND all:"Hermitian form" AND all:"zeros" AND all:"compression"`
* arXiv API: `all:"sine kernel" AND all:"Gram matrix" AND all:"moments"`
* arXiv API author listings: `au:"Lagarias" AND abs:"point process"`; `au:"Chirre" AND cat:math.NT` (23); `au:"Baluyot" AND cat:math.NT` (11); `au:"Rodgers_B" AND cat:math.NT`
* WebSearch: third trace moment "adds nothing" zeta zeros certificate proportion simple zeros linear programming
* WebSearch: Rudnick Sarnak range third moment Gram matrix zeros zeta unconditional bandwidth 1/2 cubic
* WebSearch: limitations obstruction "explicit formula" linear programming bound zeros L-functions "cannot be improved" higher moments
* WebSearch: Cohn Elkies linear programming bound higher order constraints "no improvement" three-point bound sphere packing limitation
* WebSearch: Tao Lagarias Rodgers higher correlations alternative hypothesis counterexample point process zeta zeros
* WebSearch: "pair correlation method" limit "cannot" exceed 2/3 simple zeros Montgomery method exhausted optimal
* WebSearch: Lagarias Rodgers "Band-limited mimicry of point processes by point processes supported on a lattice"
* WebSearch: Kuna Lebowitz Speer realizability problem point processes truncated moment two-point correlation existence
* WebSearch: "marginal value" adding third moment constraint linear program zero density certificate no improvement number theory 2025 2026
* WebSearch: integrality multiplicities relaxation unsound extremal problem zeros zeta linear programming fractional counterexample
* WebSearch: Markov Krein one-sided Chebyshev bound moment problem "odd moment" does not improve Christoffel function even order Karlin Studden
* WebSearch: Montgomery 1973 pair correlation extremal configuration two thirds simple zeros five sixths distinct zeros Cheer Goldston multiplicity
* WebSearch: arXiv 2026 "cubic" OR "third trace" augmentation certificate "two-moment" zeta zeros no-go absorption
* Semantic Scholar search API: "third moment does not improve linear programming bound zeros zeta" (total 0)
* Abstracts fetched and read: arXiv 2501.14545, 2511.20059, 2603.28104, 2507.06823, 2508.10857, 2412.15481, 2502.05106, 2310.01913, 1810.08843, 1905.12123, 1907.03391, 2607.16795, 2604.05733, 2206.15373, math-ph/0612075, 0910.1710
* On-disk corpus greps (`sources-extracted/`, `fetched/`, `fetched-r2/`, `fetched-r3/`): "triple correlation", "3-level|three-level"; full reads of Lagarias–Rodgers (w-09) and Rudnick–Sarnak (w-16); pdftotext + grep of Chirre–Gonçalves–de Laat (w-08) and Conrey–Ghosh–Gonek (w-10); parent bibliography verified from `sources-extracted/v5_p16.txt`, `v5_p17.txt`

Adversary (additional):

* **Citation-graph traversal** (the technique that found GdLL): Semantic Scholar `/paper/{arXivId}/citations` on 1810.08843 (21 citing papers, all title-screened), 1905.12123 (7), 1907.03391 (3)
* arXiv metadata: `"higher-level correlations" AND "multiplicity"` (2 results, one is GdLL); `"third trace" AND "zeros"`; `"cubic augmentation"`; `"Gabor" AND "explicit formula" AND "zeros"`
* Fetched and read in full: arXiv:2303.01095 (GdLL, 18 pp) — eq. (5), Theorem 1, the N_n remark, the Cohn–de Laat–Salmon remark
* On-disk PDFs opened that the sweep never opened, grepped for higher-correlation / no-improvement / limitation remarks: Carneiro–Chandee–Chirre–Milinovich 2022 (w-14, §2.1.3 read in full), Carneiro–Chandee–Littmann–Milinovich 2017 (w-15), Goldston–Gonek–Özlük–Snyder 2000 (w-19), Hejhal 1994 (w-20), Chirre–Gonçalves–de Laat 2020 (w-08), Carneiro–Milinovich 2025 (y-25), Grover–Mezzadri–Simm 2026 (p3-22d5 = arXiv:2604.03051)
* Re-read `sources-extracted/v5_p13.txt` and verified the parent's §7.2(a)–(f) verbatim, including the absence of any §7.5
* Optimization vocabulary: Lasserre/SoS level collapse, Delsarte LP limitations, integrality gap, Markov moment problem principal representations, Krein–Nudelman / Karlin–Studden odd-moment principle
* Random matrix / quantum chaos vocabulary: CUE higher-order moments, spectral form factor, Bogomolny–Keating, derivative moments
* Goldston-school series 2501.14545, 2503.15449, 2507.06823, 2508.10857, 2511.20059 — abstracts fetched and screened
* MathOverflow / folklore search: "why higher correlations do not improve the simple-zero proportion"
* Pre-1992 layer: Gallagher (Crelle 362, 1985), Montgomery 1973, Montgomery–Taylor, Cheer–Goldston 1993, Mueller
* Cross-arithmetic on the manuscript's own constants (produced the 0.8051 / Farmer–Gonek–Lee collision)

## Unreachable (A4), and what was substituted

* **arXiv full-text search** — the public API indexes metadata only (title/abstract/authors); no working full-text endpoint. Substituted: abstracts + WebSearch + grep over the program's on-disk PDF corpus + Semantic Scholar citation-graph traversal. **Absence in arXiv full text is therefore unproven, not established.**
* **Semantic Scholar `/paper/search`** — HTTP 429 on every attempt across two runs for the sweep. Substituted: the `/paper/arXiv:{id}` lookup and `/citations` endpoints, which worked and supplied the parent's reference/citation graph and (for the adversary) the traversal that found GdLL.
* **Google Scholar** — not attempted (blocked per standing guidance). Substituted: WebSearch, arXiv API, Semantic Scholar, on-disk corpus.
* **zbMATH Open** — not queried; coverage obtained from arXiv + Semantic Scholar + the parent's own bibliography verified on disk.
* **Math. Comp. published version of GdLL** (doi:10.1090/mcom/4005) — paywalled; worked from arXiv v2, whose journal-ref confirms the venue. Volume/issue/page numbers taken from search-surfaced AMS metadata, not from the AMS page (HTTP 403).
* **Leijenhorst's Delft PhD thesis** — not obtained. It is the most likely home for an explicit "higher levels do not improve the simple-zero bound" statement and is **the single most probable remaining source of a genuine anticipation.** See "Sponsor decisions".
* **Tao's blog treatment of the Alternative Hypothesis** — not fetched; known second-hand via Lagarias–Rodgers's abstract. Recorded as second-hand.
* **Kuna–Lebowitz–Speer page numbers** — DOIs and arXiv ids verified; exact volume/page for the J. Stat. Phys. 2007 paper not verified and not asserted.

---

# 2. M0 axiom class — `results/c3-r/m0-axiom-note.md`

*"The polarized-Frobenius axiom class: an axiom statement with Davenport–Heilbronn and Epstein
witnesses (not a theorem)"*.

## Verdict: NOVEL-WITH-CITATIONS

Both agents agree, and the adversary could not break the note as a whole after attacking it from
sixteen angles. The **substrate choice is genuinely unclaimed**: arXiv metadata search returns zero
for `"adelic curve" AND "correspondence"`, zero for `"adelic curves" AND "Riemann hypothesis"`,
zero for `"polarized Frobenius"`, zero for `"adelic curve" AND "Frobenius"`; and an exhaustive
enumeration of **all 99 papers** citing Chen–Moriwaki (38) and Yuan–Zhang (61) shows not one
touching zeta, Riemann, Frobenius, correspondence, Euler product, L-function, or Weil. The
adversary attacked the same claim through the rival model-theoretic formalization —
`all:"globally valued field"` returns 7 papers, none zeta-facing; `"globally valued fields" AND
"zeta"` returns 0 — and it held. Nobody has pointed the adelic-curve framework at zeta functions.

**But the axioms are not new, and the note cites none of the relevant literature.** The
(PF2)+(PF3) content — a Frobenius family indexed by the primes with a total multiplicative
composition law and primitivity exactly at the primes — is prior published mathematics in two
independent dialects, and the adversary added a third source that contains the note's own §7
*diagnosis*.

## Adjudication of the disagreement

The adversary set `anticipation_found: false` and endorsed the verdict, so the document-level
verdict stands. It corrects the sweep in four places, and **the adversary wins all four**, because
each correction rests on a verbatim read of a document in the program's own corpus:

1. **The sweep never searched the program's own PDF corpus.** It ran two greps of
   `sources-extracted/` and declared the corpus thin. All four of the adversary's heaviest
   findings are program-fetched PDFs in `fetched/` and `fetched-r2/`, and one of them
   (Conrey–Li) had already been given a full human-grade read by an earlier session of this
   program, recorded in `FETCH-LIST-RESPONSE.md` §4 and `FETCH-VERIFICATION.md`. **Standing
   process change: any future novelty gate for this program greps the on-disk PDF corpus before
   going online.**
2. **Claim 4's grade.** The sweep called the χ₄ over-breadth witness "the sharpest genuinely new
   observation in the note." Conrey–Li (IMRN 2000) refute a proposed positivity condition
   sufficient for RH by exhibiting RH-true objects that fail it, and the objects are ζ and
   L(s, χ₄) — the same witness function. The mathematical condition differs (de Branges
   reproducing-kernel positivity vs. Λ_D ≥ 0), so this is not an anticipation of the *statement*,
   but the *move* is a published standard of the field. §6.3 must cite it.
3. **Claim 3's ground is too narrow.** "Nothing surfaced that runs the Beurling test against a
   *geometric* axiom class" is true and beside the point. Diamond–Zhang's published conclusion
   quantifies over all proofs: *"Thus, a proof of the Riemann hypothesis will require more than
   just the multiplicative structure of integers and smallness of N(x) − x."* The note's class is,
   by its own account, multiplicativity plus a positivity consequence. **This is the closest thing
   to an outright anticipation of a headline claim in the note, and it comes with both directions
   in one chapter** (Theorem 17.11 an RH-*true* g-number system; Theorem 17.14 the dlVP-optimal
   RH-false one). It supersedes the sweep's SHOULD-cite of W.-B. Zhang, Math. Ann. 337 (2007).
4. **The §7 diagnosis is Connes's.** The sweep offered the "Riemann–Roch strategy" preprint as a
   SHOULD. The stronger and earlier statement is Connes's 2016 essay §4.3.2: *"At this point, what
   is missing is an intersection theory and a Riemann–Roch theorem on the square of the arithmetic
   site."* The same essay's §2.3 lists as numbered basic facts of Weil's proof the exact
   ingredients the note axiomatizes as (PF1) and (PF4) plus the §5 chain — including *"If D is a
   strictly positive divisor then D·ξ₀ + D·ξ₁ > 0"*, which is precisely "nef against effective is
   ≥ 0", the one geometric ingredient the note's computation consumes.

## Claim-by-claim

| # | Claim | Verdict |
|---|---|---|
| 1 | The axiom class (PF1)–(PF6) over a proper adelic curve | **NOVEL-WITH-CITATIONS** — substrate new, axioms not |
| 2 | The negative result on the D-attachment clause | **NOVEL-WITH-CITATIONS** — the vacuity *certificate* is new; the Euler-product half is textbook and the P¹×P¹ exhibit is the Bost–Connes/Adams family |
| 3 | Beurling/DMV instantiability; the class cannot decide RH | **ANTICIPATED** for the general conclusion (Diamond–Zhang 2016, Ch. 1 §1.1 and Ch. 17); **NOVEL** only for the axiom-by-axiom accounting and the naming of θ-effectivity as the missing input |
| 4 | DH and Epstein witnesses; KP structure theory not derived | **STANDARD-MATHEMATICS** for the facts; the exact von Mangoldt witness table is unanticipated but elementary; the χ₄ over-breadth *move* is published (Conrey–Li 2000) |
| 5 | Blomer–Leung as "the sharper formal home" | **NOVEL-WITH-CITATIONS**, positioning claim; **citation-accuracy repair required** |

**Repair required on claim 5.** The sweep downloaded the full Blomer–Leung text and grepped it:
the word "monoid" occurs **zero** times. "Beyond-endoscopy monoid converse theorem" is a
program-internal label, not the authors' terminology. Their Theorem 1.1 reads: *"Suppose that a
sequence B(n,m) of complex numbers satisfies the usual Hecke relations, the Ramanujan conjecture
and the Voronoi summation formula. Then this sequence is the set of Fourier coefficients of an
automorphic form on GL(3) whose archimedean Langlands parameter is determined by the gamma factors
in the Voronoi summation formula."* Restate in the authors' terms, mark "monoid" as the note's own
gloss, and add one sentence on how a *converse* theorem hosts an *exclusion* (the contrapositive).
Propagate to `BARRIER-ZOO.md` I.1. The Adv. Math. 485 (2026) art. 110716 citation itself is correct.

**Overstatement to soften in §7.** The note says θ-effectivity h⁰_θ(D) ≥ deg D + O(1) is "a
substrate-level input no current object supplies." Connes–Consani proved a Riemann–Roch theorem for
divisors on the Arakelov compactification of Spec Z, with cohomologies, an integer-valued dimension
and Serre duality. Cite it and say precisely why it is or is not the M4 input wanted.

**One unprobed internal tension**, raised by the adversary as a probe, **not** a finding, and not
verified against any source: the note's §5 admissibility condition in its strict printed
degree-one shape (a_n completely multiplicative, a_p ≥ 0, a_1 = 1) run against the note's own §7
citation of Kaczorowski–Perelli's degree-one classification appears to collapse the printed
admissible class to something close to ζ alone — which would sharpen the positivity-filter
classification and sits awkwardly beside §7's claim that the class does not exclude Beurling worlds
(whose generalized primes are not rational primes, so the two statements may be about different
index sets and never meet). **This is a computation, not a search.** It is the first thing a
referee would probe.

## Cross-reference to prior homework

**EXTENDS `results/c3-r/prior-art-r7a.md`.** The gate was written primarily for the seed note and
its m0 coverage is thin, as the brief said. It correctly flagged Banaszak–Uetake and Haran for the
seed note; both belong in m0 too. Neither the gate nor either agent found anything that overturns
the gate's verdict for this document. What this check adds beyond the gate: Borger, the
Connes–Consani arithmetic-site composition theorem, the Riemann–Roch for Spec Z-bar, Deninger's
1998 conjecture and Flach–Morin's formalization, Deninger's 2022 published *no-go* theorem for a
real-coefficient Weil cohomology on arithmetic curves, Connes's 2016 essay, the Diamond–Zhang
monograph, Conrey–Li, and the Blomer–Leung terminology repair.

## Searches run (M0)

Sweep — arXiv API:

* `all:"adelic curve" AND all:"Frobenius"`; `all:"adelic curve" AND all:"correspondence"` (raw feed checked: totalResults = 0)
* `all:"adelic curves" AND all:"Riemann hypothesis"`; `all:"adelic curves" AND all:"zeta"`; `abs:"adelic curve" OR abs:"adelic curves"` (20-result recency sweep)
* `all:"polarized Frobenius"`; `all:"Frobenius correspondence" AND all:"Arakelov"`; `all:"Frobenius correspondences"` (15 results)
* `all:"adelic line bundles" AND all:"correspondences"`; `… AND all:"Hodge index"`; `all:"adelic curve" AND all:"Hodge index"`
* `abs:"Frobenius" AND abs:"Riemann hypothesis" AND abs:"correspondences"`; `abs:"Riemann hypothesis" AND abs:"axioms"` (20 results)
* `abs:"no-go" AND abs:"zeta"`; `abs:"Selberg class" AND abs:"axioms" AND abs:"Euler product"` (0 results)
* `abs:"monoid" AND abs:"converse theorem" AND abs:"Euler product"` (0); `all:"beyond endoscopy" AND all:"converse theorem"`
* `au:Borger AND all:"field with one element"`; `abs:"Lambda-rings" AND abs:"field with one element"`
* `au:Consani AND au:Connes` (20-result listing sweep, 2008–2026); `ti:"scaling site"`
* `au:Haran AND all:"Frobenius"`; `au:Deninger AND all:"Riemann hypothesis"`
* `abs:"explicit formula" AND abs:"positivity" AND abs:"correspondences"`; `abs:"Weil positivity"`
* `all:"globally valued fields"`; `all:"Beurling" AND all:"number systems" AND abs:"Riemann hypothesis"`
* `all:"Effectivity of Arakelov divisors"`; `abs:"theta invariants"`
* id_list verification: 2507.13780, 2102.08478, 2309.01567, 1502.05580, 1603.03191, 0806.2401, 2205.01391, 1507.05818, 1805.10501

Sweep — Semantic Scholar / Crossref:

* Semantic Scholar graph API: **all 38** papers citing arXiv:1903.10798 (Chen–Moriwaki), full title enumeration
* Semantic Scholar graph API: **all 61** papers citing arXiv:2105.13587 (Yuan–Zhang), full title enumeration
* Crossref record verification: Connes–Consani *Geometry of the arithmetic site* (Adv. Math.); *Riemann–Roch for Spec Z-bar* (Bull. Sci. Math.); *Geometry of the scaling site* (Selecta Math.); Connes–Consani–Marcolli *Fun with F₁* (JNT); Flach–Morin (Münster J. Math.); Bombieri–Ghosh (Russian Math. Surveys); Banaszak–Uetake (CNTP); Diamond–Montgomery–Vorhauer (Math. Ann.)

Sweep — WebSearch (abbreviated titles): axiom system "Frobenius correspondences" over "Spec Z" Arakelov no-go; Beurling generalized primes counterexample shows axioms insufficient; "generalized number system" used to show a proposed proof strategy cannot suffice; Davenport–Heilbronn shows Euler product axiom essential; Deninger axioms hypothetical cohomology theory RH; Flach–Morin consequences/constraints; proposed axiomatic framework shown vacuous; Borger Λ-rings descent commuting Frobenius lifts; Λ-structure Adams operations Arakelov RH; "adelic curve" Chen Moriwaki Frobenius zeta proposal; Beurling as test case for the Connes trace formula; Diamond–Montgomery–Vorhauer Math. Ann. 334; Kaczorowski–Perelli structure of the Selberg class; van der Geer–Schoof effectivity/θ-divisor; Davenport–Heilbronn 1936 second paper Epstein; Bombieri "A variational approach"; Bombieri Clay RH description; Deninger + DH/Epstein; Deninger ICM 1998 Documenta; Riemann–Roch Spec Z Connes–Consani vs van der Geer–Schoof; 2025/2026 new axiomatic Frobenius-square frameworks; Epstein zeta von Mangoldt coefficients negative

Sweep — full texts fetched and read: arXiv:1502.05580 (Thm 1.2, Thm 7.7 verbatim); arXiv:0906.3146 (Λ-structure definition verbatim); arXiv:2401.04037v2 (Theorem 1.1 verbatim; `grep -c -i monoid` = 0); Flach–Morin Münster J. Math. 13 PDF; abstracts of 2401.04037, 1512.08946, 1805.10501, 2205.01391, 2602.04022, 2305.10398, 2209.08536, math/0410270. On-disk greps of `sources-extracted/` for "arithmetic site" and "Frobenius correspondence".

Adversary (additional, corpus-first):

* Systematic grep of `fetched/`, `fetched-r2/`, `fetched-r3/` filenames and pdftotext extractions for Davenport, Epstein, Beurling, Frobenius correspondences, Riemann–Roch, arithmetic site, vacuous
* Read the on-disk Deninger cluster (x-01 … x-24) — found `x-04` = arXiv:2204.02714, the published no-go; read its axiom list 2.1–2.12 and Theorem 2.13 verbatim
* Read Connes 2016 essay (`fetched-r2/t-20b`) §2.3, §4.3.1, §4.3.2 verbatim (Weil template, the three basic facts, the N^× Frobenius action, eqs. (31)–(32), the "what is missing" passage)
* Read Diamond–Zhang (`fetched-r2/t-50`) Ch. 1 §1.1 answer (2), the back cover, Ch. 17 §17.1, Theorem 17.11, Theorem 17.14
* Read Conrey–Li (`fetched/p1-06`) introduction and §3.2 with both χ₄ numerical witnesses
* Cross-field vocabulary, physics: arXiv API `all:"Davenport-Heilbronn" AND all:"Euler product"` (totalResults = 2) — LeClair–Mussardo 2307.01254 and Franca–LeClair 1407.4358, both abstracts fetched verbatim
* Cross-field vocabulary, model theory: `all:"globally valued field"` (7 results); `all:"globally valued fields" AND all:"zeta"` (0)
* Terminology ownership: `abs:"Frobenius correspondences"` (6 results total; four are Connes–Consani/CCM)
* Authoritative-survey attack: downloaded Bombieri's Clay problem description and grepped locally — **zero** occurrences of "Davenport", "Epstein", "Beurling", "generalized prime", "Selberg class". Hypothesis refuted; recorded so it is not re-chased
* Selberg-class route: grepped the on-disk cluster (Conrey–Ghosh 1993 Duke, Perelli 2017 BUMI, Kaczorowski–Perelli 1999 Acta Math.) for Davenport/Epstein/Beurling — zero hits in all three
* No-go/vacuity genre: `abs:"Riemann hypothesis" AND abs:"vacuous"` (1, a crank paper); `abs:"no-go" AND abs:"Riemann hypothesis"` (12, none relevant); `abs:"obstruction" AND abs:"Weil" AND abs:"Spec Z"` (0); `abs:"axioms" AND abs:"Riemann hypothesis" AND abs:"insufficient"` (0)
* `abs:"Selberg class" AND abs:"nonnegative"` (1, unrelated)
* Re-verified the sweep's dismissals: re-fetched Haran arXiv:2209.08536's abstract; fetched Flach–Morin's PDF from Bordeaux; confirmed Deninger x-04's venue from the arXiv abs page
* Program-provenance: grepped Manin's Astérisque 228 (`fetched/x-02`) for the Spec Z × Spec Z / absolute Frobenius program statement

## Unreachable (M0), and what was substituted

* **link.springer.com article pages** — every fetch returns a 303 redirect to `idp.springer.com` (institutional auth). Affected: Math. Ann. 337 (2007) landing page for W.-B. Zhang; a Doklady Math. item. Substituted: Crossref API metadata (title, authors, container, volume, pages, DOI, issued date). Cited on Crossref-verified bibliographic data only, with **no claim about internal content**.
* **uni-muenster.de** — direct curl timed out after 75 s on the retry loop, but the Flach–Morin PDF had already landed from the first attempt and was read locally.
* **api.semanticscholar.org** — HTTP 429 on the first two attempts; recovered on retry; both 99-title citation sweeps completed.
* **Google Scholar** — not attempted (blocked). Substituted: Semantic Scholar graph API, Crossref, arXiv Atom API, WebSearch.
* **MathSciNet** — permanently closed to this program (corpus-routing caveat 13); not used.
* **zbMATH Open** — not queried; every reference in the citation list carries a DOI or arXiv id verified against a live source.
* **Blomer–Leung published Adv. Math. version** — paywalled; the `monoid` grep result is from arXiv v2 (11 Jul 2026), not the published version.
* **Bombieri, "A variational approach to the explicit formula", CPAM** — paywalled (Wiley); not read; nothing here depends on it and it is not in the citation list.
* **AMS/Springer full texts for Segre-era and monograph items** — see the per-reference "not independently verified" marks below.

---

# 3. M1 non-circularity — `results/c3-r/m1-noncircularity.md`

*"Castelnuovo–Severi / Hodge index from Riemann–Roch + ampleness (non-circularity note)"*.

## Verdict: ANTICIPATED-BY — this is STANDARD MATHEMATICS, and the note is right to say so

The note's own status paragraph reads *"This is a re-derivation of standard material for the
program record; zero novelty is claimed."* **That self-assessment is confirmed by both agents and
should ship intact.** Every theorem in §§3–7 is published, in the same order, with the same inputs:

* **A. Grothendieck, "Sur une note de Mattuck–Tate", J. reine angew. Math. 200 (1958), 208–215.**
  His §2 already itemizes the note's input list by number: (2.1) the Riemann–Roch inequality,
  which he says follows *"de l'égalité de Riemann-Roch … et du théorème de dualité de Serre"*
  (2.2) = (IN1)+(IN2); (2.3) l(D+D′) ≥ l(D′) if l(D) > 0 = (IN5); (2.4) *"l(D) > 1 implique
  D·H > 0"* = (IN3). His Theorem 1.1 "(Hodge–Segre–Bronowski)" is the note's §§4–5; his (1.8) is
  the note's §6 with the equality case. He also makes the note's own (IN6) scoping remark:
  *"Il serait évident comment formuler le théorème 1 si on voulait ignorer le théorème de Néron."*
* **J. S. Milne, arXiv:1509.00797, §1** publishes the note's §§3–7 end to end, through to
  |N₁ − (q+1)| ≤ 2g√q.

Both agents read both sources at the source. The non-circularity *conclusion* is **correct** and
neither agent could break it (Riemann–Roch for surfaces in char p is Zariski 1952 / Serre 1956;
Serre duality 1955; (IN3)–(IN5) elementary; Nakai–Moishezon's proof is cohomological and does not
invoke V.1.9; rationality and the functional equation of Z(C,T) are Riemann–Roch-on-the-curve).
The sweep re-derived the §7 discriminant step by hand and it is as printed; the adversary
re-derived it independently and agrees.

## Adjudication of the disagreement — the adversary breaks the sweep's one remaining novelty claim

The sweep held that the *framing* — an explicit itemized non-circularity audit addressed to an RH
program — is unpublished, having grepped Milne and Kleiman for the word "circular" and found zero
hits. **The adversary refuted this, and wins.** The literature's phrase is not "circular"; it is
"avoid the Weil conjecture":

> **K. Ito, T. Ito, T. Koshikawa, "The Hodge standard conjecture for self-products of K3
> surfaces", arXiv:2206.10086 (v1, 21 Jun 2022); J. Algebraic Geom. 34 (2025), no. 2, 299–330**
> *(journal record from search-surfaced AMS metadata only — the AMS page returned HTTP 403)*,
> Remark 1.3, read verbatim from the fetched PDF:
> *"Let us recall again that if X is defined over a finite field, the Hodge standard conjecture
> for X² and the Lefschetz standard conjecture for X imply the Weil conjecture for X, and Theorem
> 1.2 justifies the assumption. **However, we did not attempt to avoid the Weil conjecture in our
> proof of Theorem 1.2.**"*

That is the M1 audit, stated as an audit, about the M1 positivity engine, by authors who raise the
direction of implication explicitly and then disclose as a limitation that their own proof consumes
it. Paired with **G. Ancona, "Standard conjectures for abelian fourfolds", arXiv:1806.03216,
Invent. Math. 223 (2021)** — whose introduction publishes the sweep's own recommended §9 lineage
repair verbatim, and whose Lemma 7.10 proof opens *"Recall that the Weil conjectures imply
ᾱ = q/α"* — the published record now contains the note's thesis as a documented pair: the surface
case is Weil-free (Segre 1937 / Bronowski 1938; Grothendieck 1958), and both higher cases proved
since are not, and both author teams say so. **Milne's LFF abstract** (arXiv:2011.06563)
classifies a standard conjecture by whether its known proof consumes the Weil conjectures, which is
the note's §8 ledger column in the field's own idiom.

**Net effect: the note's framing is not merely uncontested-and-unrecorded; it is
uncontested-and-recorded.** That strictly strengthens the STANDARD-MATHEMATICS verdict and removes
the last thing about the note that could have been called new.

## Three further corrections to the sweep, all adjudicated in the adversary's favor

1. **The sweep's repair 3(b) is wrong and must not be made.** It proposed changing §7's "this is
   the inequality Weil's proof consumes" to "the Mattuck–Tate/Grothendieck proof". Milne's §1
   "Correspondences" computes τ(D ∘ D′) = def(D) and concludes verbatim *"Thus Weil's inequality
   τ(D ∘ D′) ≥ 0 is a restatement of (5)"*, (5) being Castelnuovo–Severi. The note is
   content-correct as written.
2. **Grothendieck's Prop. 2.1 is not the note's §3 Lemma.** The note's §3 Lemma assumes D² > 0
   *and* D·H > 0 for ample H. Grothendieck's Prop. 2.1 assumes only D² > 0 and concludes, after
   possibly replacing D by −D, that l(D′+nD) → ∞ — no ample or hyperplane hypothesis at all. The
   correct finding is stronger than the sweep's: **Grothendieck's route needs no positivity
   hypothesis on D whatsoever.**
3. **§8 should say "a proof", not "the proof".** Bombieri's Clay text gives a *different* Weil-free
   input list for the same theorem — *"The proof uses the Riemann-Roch theorem on X and the
   finiteness of families of curves on X of a given degree"* — Severi's boundedness route, with no
   ampleness and no Serre duality. Segre/Bronowski are a third. Multiple independent Weil-free
   routes strengthen the conclusion, but a headline claiming uniqueness is not supported.

## Claim-by-claim

| # | Claim | Verdict |
|---|---|---|
| 1 | Hodge index + Castelnuovo–Severi from RR + Serre duality + ampleness, with a no-Weil-bound ledger | **STANDARD-MATHEMATICS**; the conclusion is correct, and the *framing* is also published (Ito–Ito–Koshikawa, Ancona, Milne LFF) |
| 2 | The (IN1)–(IN7) input list | **ANTICIPATED** outright by Grothendieck §2. (IN4) and (IN7) are Hartshorne artifacts; Grothendieck and Milne both run the argument on hyperplane sections and need neither |
| 3 | Non-circularity of importing CS positivity onto E_p × E_p | Positive half **STANDARD-MATHEMATICS** (complex abelian surfaces; NS rank 3 for End(E) = ℤ; deg([m]−1) = (m−1)²). Negative half belongs to the companion seed note and is carried by reference inside the IV.10 fence |

## The one paragraph that is genuinely exposed

**§8 "Scope of the claim"** says the note does not assert that any arithmetic substrate exists on
which the analogous inequality can be derived. A referee answers in one line: **arithmetic Hodge
index theorems exist, are proved, and do not yield RH** — Faltings–Hriljac for arithmetic surfaces,
Moriwaki in higher dimension, Künnemann/Gillet–Soulé on the arithmetic standard conjectures,
Yuan–Zhang for adelic line bundles. Künnemann's introduction, read at source, records that the
Hodge-type statement *"for divisors is a consequence of the positivity of the Néron–Tate height"*;
Deninger's *Hilbert–Pólya strategy and height pairings* (on disk, `x-17`) says the same and reads
it as **support** for a positivity route to RH. The sweep rated this SHOULD; the adversary
upgrades it to **MUST**, and that is followed.

## The one load-bearing unread item

If §9's lineage is rewritten to lean on a 1937 characteristic-free algebraic proof — which both
agents recommend, and which genuinely strengthens the note — then **Segre 1937 and Bronowski 1938
become load-bearing recalled facts with a single ultimate source.** Neither agent fetched the
originals. The claim rests on Grothendieck's sentence, Milne's footnote 16, and Ancona's
introduction, and Ancona is plausibly repeating Grothendieck. Note also that the Grothendieck
retranscription used (denisevellachemla.eu) prints "Segre, Annali di Mat. 16 (1957)" and
"G. Bronowski, JLMS 13 (1958)" — **years and initial both corrupted** relative to Milne's
bibliography. **Use Milne's dates and initials, not the retranscription's.**

## Cross-reference to prior homework

**EXTENDS and partially CORRECTS `results/c3-r/prior-art-r7a.md`.** The gate's coverage of M1 is
incidental — M1 is largely an audit of classical mathematics and the gate did not gate it as such.
This check supplies the missing verdict (ANTICIPATED-BY / standard mathematics) and the ten MUST
citations. It **corrects** any impression that the gate's global NOVEL-WITH-CITATIONS verdict
extends to this document: it does not, and the note itself never claimed it did.

## Searches run (M1)

Sweep — WebSearch: Hodge index theorem proof does not use Riemann hypothesis for curves circularity Weil bound; Mattuck–Tate 1958 Castelnuovo–Severi Riemann–Roch surface proof; "standard conjecture of Hodge type" surfaces char p Kleiman; "circular"/"circularity" proof RH curves finite fields intersection theory positivity; Connes–Consani Weil positivity circularity concern; mathoverflow Hodge index circular reasoning; "Nakai-Moishezon" OR "Riemann-Roch for surfaces" logical independence char p; "non-circularity" argument RH program import; zbMATH Castelnuovo–Severi survey/history; arXiv 2025 2026 Hodge index positivity approach RH arithmetic surface; "reverse mathematics"/dependency audit Weil conjectures; arithmetic Hodge index Faltings Hriljac Moriwaki Yuan Zhang; arXiv 2606.06604 citing papers; "we do not use the Weil conjectures" / "without assuming the Riemann hypothesis for curves"; "dependency ledger"/"input ledger" non-circularity certificate; "Weil's proof" curves "no circularity" logical order; Segre 1937 Bronowski 1938 Severi 1906 first algebraic proof; Vainsencher–Voloch, Kani equivalence defect; Grothendieck "Sur une note de Mattuck-Tate" content; critique of failed RH proofs "assumes what it wants to prove"; "per-prime" elliptic products NS prime-blind Lefschetz (m−1)²; Hartshorne V.1 theorem/corollary numbering

Sweep — arXiv API: `all:"Castelnuovo-Severi" AND all:"Riemann hypothesis"` (0); `all:"Castelnuovo-Severi inequality"` (1); `abs:"Hodge index" AND abs:"Riemann hypothesis"` (0); `all:"Mattuck-Tate"` (**2 entries only** — Connes–Consani 1805.10501 and Connes 1509.05576); `all:"Weil positivity" AND all:"Riemann-Roch"` (0); `abs:"Castelnuovo" AND abs:"index theorem"` (0); `abs:"Riemann hypothesis" AND abs:"function field" AND abs:"positivity"` (4, none relevant); `id_list=1509.00797`

Sweep — other: Semantic Scholar Graph API (2 queries, both HTTP 429); zbMATH Open (JS shell, no rows); direct fetch + full read of Grothendieck 1958 (denisevellachemla retranscription), Milne pRH.pdf, Bombieri Clay p. 9, Kleiman 1968 scan (uni-mainz), Hallouin–Perret 1409.2357, Connes 2602.04022; grep for "circular" in Milne/Kleiman/Szamuely/Raskin/1807.10812 (no relevant hits); on-disk pdftotext grep for "circular|circularit" across ~300 corpus PDFs (34 hits, all unrelated senses); `grep -ril mattuck|castelnuovo` over `sources-extracted/` and `fetched*/`; pdftotext + grep of `fetched/y-06` (Connes–Consani Riemann–Roch strategy); WebFetch mathnet.ru/eng/mat127 (Mattuck–Tate bibliographic record)

Adversary (additional):

* Re-verified **every** primary source the sweep quoted, at the source (Grothendieck all 12 pp; Milne §1 + footnotes 12/14/15/16 + bibliography; Bombieri pp. 9–10; Kleiman Thm 4.7 + Introduction; Connes–Consani §3; Hallouin–Perret p. 1)
* **Vocabulary shift that produced the break**: searched the standard-conjectures-in-char-p literature 2018–2025 for "avoid the Weil conjecture" rather than "circular" — surfaced Ito–Ito–Koshikawa 2206.10086 and Ancona 1806.03216, both fetched and read
* Full-corpus re-extraction: pdftotext over all 377 PDFs in `fetched/`, `fetched-r2/`, `fetched-r3/` into a fresh 44 MB text cache, then `grep -ril "vicious circle|circular reasoning|circular argument|circularity|begging the question|cercle vicieux"` → 2 files, both unrelated
* Negative control: `grep -c -i circular` = 0 in Milne pRH, Kleiman 1968, Ancona, Ito–Ito–Koshikawa, Hallouin–Perret
* Arithmetic-substrate attack: fetched and read Künnemann, Compositio Math. 99 (1995) 109–128 from Numdam; read Deninger `x-17` from the corpus; confirmed Gillet–Soulé PSPM 55.1, Moriwaki alg-geom/9403011, Faltings–Hriljac, Yuan–Zhang
* Operator-algebra / NCG vocabulary: Connes–Consani 2006.13771; the Banaszak–Uetake trilogy (t-30b/t-43b/t-58a); Connes essay t-20b; Connes 2026 u-14b; CCM y-07 — all read/grepped
* Explicit-formula vocabulary: Bombieri, Rend. Lincei 11 (2000) (u-23a); AIM "Weil's positivity criterion" page
* F₁ / tropical: Haran 1991 (`fetched-r3/haran1991.pdf`); Manin Astérisque 228 (`x-02`) — zero hits for Castelnuovo/Mattuck/Hodge index
* More-general-theorem attack: checked that Kleiman 1968 Thm 4.7 at X = C specializes to the note's §7; checked Milne 0709.3040 §9 and Aside 9.4
* Currency check on claim 3: Semantic Scholar citations of arXiv:2606.06604 → `{"data": []}`; `all:"Tate curves" AND all:"Spec Z"` → one irrelevant hit
* Internal-loop check: verified Hartshorne V.1.10 (Nakai–Moishezon) is proved from V.1.8, not V.1.9, so using (IN7) inside §6 does not circle back through §4. **No internal circularity found.**

## Unreachable (M1), and what was substituted

* **Semantic Scholar Graph API** — HTTP 429 for the sweep on every attempt across two batches; **worked for the adversary**, which used it for the 2606.06604 citation check. Sweep substituted the arXiv API, WebSearch, and publisher/EuDML/mathnet records.
* **zbMATH Open** — returns a JavaScript shell with no result rows over curl. Substituted: Numdam, De Gruyter/EuDML DOI records (Grothendieck doi:10.1515/crll.1958.200.208, eudml 150382; Vainsencher–Voloch doi:10.1515/crll.1988.390.114, eudml 153062), mathnet.ru/eng/mat127.
* **Mattuck–Tate, Abh. Math. Sem. Univ. Hamburg 22 (1958), 295–299** — full text paywalled; Springer redirects to an IdP endpoint. Bibliographic record verified (MR0098747, Zbl 0081.37604); **content** characterized from Grothendieck §1, Milne, and Milne's "The Work of John Tate". Nothing here rests on unread portions.
* **Segre 1937, Bronowski 1938, Hodge 1937, Severi 1906** — originals not fetched by anyone in this gate chain. See "the one load-bearing unread item".
* **AMS Journal of Algebraic Geometry page** for Ito–Ito–Koshikawa — HTTP 403. Volume/issue/pages taken from search-surfaced AMS metadata; the arXiv v1 was fetched and read in full.
* **Kleiman 1994, "The standard conjectures" (Motives, PSPM 55)** — the available copy is an image scan with no text layer, not OCR'd. Kleiman 1968 was read instead and carries Theorem 4.7.
* **Hartshorne, GTM 52** — no copy on disk or online in readable form. The exercise numbers V.1.9/V.1.10 and p. 368 are now double-confirmed via Hallouin–Perret p. 1; the two letter-level pins the note itself flags ("Cor. V.1.8", the "(b)" of "Ex. II.7.14") remain unverified and are non-load-bearing.

---

# 4. Seed no-go — `results/c3-r/seed-no-go-note.md`

*"Products of the per-prime Tate curves of absolute geometry carry no correspondence calculus for
the Weil explicit formula"*.

## Verdict: ANTICIPATED-BY on the rigidity (claims 2, 3, 4). The no-go itself survives.

Both agents independently reach the same anticipation, and the adversary — whose brief was to break
the sweep — **verified it from the primary source in two arXiv versions rather than trusting the
sweep's quotation, and then pushed the priority date roughly five years earlier.** This overturns
the R7(a) gate's verdict for this document.

> **J. Winkelmann, "On elliptic curves in SL₂(ℂ)/Γ, Schanuel's conjecture and geodesic lengths",
> Nagoya Math. J. 176 (2004), 159–180; arXiv:math/0204195 (v1 15 Apr 2002, v3 8 Apr 2003).**

Winkelmann studies exactly E_λ = ℂ*/λ^ℤ = ℂ/⟨2πi, log λ⟩ for real algebraic λ > 1. In the proof of
his Theorem 2 — **present already in v1** — he derives that isogeny of E_i and E_j forces
4π²/(log λ_i log λ_j) ∈ ℚ (the note's **Theorem 1** criterion, by the identical real/imaginary
separation of the ⟨1, τ, σ, τσ⟩ relation), divides two such relations to reach
log λ_i / log λ_k ∈ ℚ against multiplicative independence (the note's **Theorem 2** proof, line for
line), frames the whole argument on **three** curves E_i, E_j, E_k (the note's **Theorem 3**, of
which {2,3,5} is the numerical instance), and states the conclusion as *"for each of these curves
there is at most one other curve in this family to which it is isogenous"* (the note's Theorem 2,
partial matching). His Proposition 3 (v1: Proposition 2) is the note's §7 Schanuel paragraph with
the same x₁ = 2πi, x₂ = log α₁, x₃ = log α₂ and the same two-case split. His Conjecture 1
(v1: Conjecture 3.2) is the note's (T1)-refuting statement, posed as a named conjecture in 2002 and
still open.

Substituting λ = p (primes are real algebraic > 1, pairwise multiplicatively independent by unique
factorization) gives the note's Theorems 1–3. **The R7(a) gate's §5 sentence — "the obstruction is
elementary lattice arithmetic that could in principle have been noted about ANY pair of complex
tori … and no one has" — is false.** It was noted, in 2002/2004, for exactly ℂ*/λ^ℤ with λ real
algebraic.

**The transcendence rider (T1) is likewise a named published conjecture.** The note's §9 says
*"The question (T1) appears to be unrecorded in the literature in this form and is stated here as
open."* It is D. Bertrand's **weak four-exponentials conjecture**, stated verbatim in Diaz (JTNB
1997) §I: *"(C4E faible) Soient a₁, a₂ des nombres réels algébriques positifs différents de 1.
Alors π² et (log a₁)(log a₂) sont ℚ-linéairement indépendants"* — with a₁ = p, a₂ = q this **is**
(T1) — followed in the next sentence by the note's own four-exponentials reduction. Diaz's
Théorème 1 proves the equivalence of (C0) (isogeny of two algebraic-parameter Tate curves implies
multiplicative dependence) with (C6) (the log-product vs π² statement), and his Propositions 1 and
3(1) give unconditional partial results about the (T1) scenario the note does not know about.

**Priority pushed earlier (adversary):** Bertrand's conjecture originates at the **Madras Number
Theory Symposium, January 1996**; the four-exponentials conjecture itself is **Schneider 1957**,
Problem 1 (verified twice independently — Diaz §0 and Waldschmidt's *Linear independence of
logarithms of algebraic numbers* Ch. 1); and the two-distinct-primes germ is **Alaoglu–Erdős
1944**, who needed exactly "p₁^x and p₂^x both rational implies x integral" and could not prove it.

## Adjudication — where sweep and adversary disagree, the adversary wins twice

1. **The sweep's finding (E1) is STALE.** It reports the `[Ha15]` Haran/Thas misattribution as a
   live defect requiring rewrites. The note fixed it on 2026-08-27 with a page-verified primary
   source (git commits `cd1a40b`, `ff4e909`), and the gate report carries a dated correction. **No
   action.** Recorded at the head of this report for the register.
2. **The sweep's finding (E3) is FALSE and must not be executed.** It asks that the `[CC26]`
   reference drop the "and the Fargues–Fontaine curve" clause, on the ground that the arXiv
   metadata title omits it. The adversary established that the arXiv API **truncates the title at
   the TeX macro** `\operatorname{Spec}\mathbf{Z}`; the note's own record already adjudicated this
   (commit `cc70ee9`). Executing the sweep's fix would replace a correct citation with a wrong one.
3. **Version hygiene.** The sweep quotes Winkelmann with mixed numbering — "Conjecture 3.2" and
   "Proposition 2" are v1; "see lemma 7" is v3. A referee will bounce that. **Cite v3 / the Nagoya
   published version consistently, and note that the argument is already in v1 (2002).**
4. **Credit allocation between Winkelmann and Diaz.** The sweep over-credits Diaz for Theorem 1.
   Diaz proves an equivalence of universally quantified *conjectures*, not the unconditional
   pairwise criterion. **Winkelmann alone anticipates Theorem 1 as a theorem; Diaz anticipates the
   (T1) rider and the 4EC reduction.** Followed.
5. **The sweep's finding (E2) — the lineage error — is CONFIRMED** by the adversary from the arXiv
   abstract of 1507.05818 directly. The note's §1.2 says the per-prime elliptic-analogue idea
   "first appears in the Connes–Consani orbit in January 2025." The abstract of **The Scaling
   Site** (arXiv:1507.05818, July 2015) reads *"The restriction of this structure to the periodic
   orbits of the scaling flow gives, for each prime p, an analogue of an elliptic curve whose
   Jacobian is a cyclic group"*. **Off by about nine and a half years**, and CC26 itself cites
   *Geometry of the Scaling Site*, Selecta Math. 23 (2017), for it.

## Claim-by-claim

| # | Claim | Verdict |
|---|---|---|
| 1 | E_p × E_q as arithmetic-surface surrogate / correspondence substrate | **NOVEL-WITH-CITATIONS** — attacked from six directions and unbroken |
| 2 | Hom(E_p, E_q) ≠ 0 ⟺ log p · log q ∈ 4π²ℚ | **ANTICIPATED** (Winkelmann 2004; Diaz 1997) |
| 3 | At most one exceptional partner prime, unconditionally | **ANTICIPATED** (Winkelmann 2004, including the proof) |
| 4 | {2,3,5} coherence-impossible | **ANTICIPATED** (instance of the same Winkelmann paragraph) |
| 5 | Off-diagonal NS rank 2; no diagonal/graph classes; CS vacuous | **STANDARD-MATHEMATICS** (Birkenhake–Lange; Rosen–Shnidman) |
| 6 | Diagonal residue (m−1)², prime-blindness | Profile **STANDARD-MATHEMATICS**; the prime-blindness *inference* **NOVEL** but modest — and it is the obverse of Deninger's standing point that log p enters as an orbit **length**, not a cohomological invariant |
| 7 | End(E_p) = ℤ for every prime, unconditionally | **STANDARD-MATHEMATICS** — three published one-line routes |

**On claim 7**, the note's Gelfond–Schneider argument is correct (both agents checked it), and the
note already concedes the claim is "a two-line specialization of a classical theorem." It should
name the theorems. The strongest anchor is **Barré-Sirieix–Diaz–Gramain–Philibert (Invent. Math.
124 (1996) 1–9)**: for algebraic q with 0 < |q| < 1, J(q) is transcendental, so j(E_p) = J(1/p) is
transcendental, so E_p has no CM — strictly more than Gelfond–Schneider gives here. Diaz 1997
Prop. 3(1) gives y_p transcendental directly; Nesterenko 1996 gives the same and more.

**What survives, and the honest reframing.** The no-go (Theorem 6) is **unaffected** and is
arguably strengthened: obstruction O1 now rests on a published rigidity rather than a new one. The
residual novelty is (a) the *construction* — assembling per-prime genus-1 fibers into a
(p,q)-graded family of classical abelian surfaces intended to host the explicit formula, which
nothing published does; (b) the exact Hom group (rank 1, generator λ₀ = i·v·y_q) and the isogeny
degree uv, which Winkelmann does not need — one paragraph, about a case the note itself believes
never occurs; and (c) the Néron–Severi and diagonal-residue consequences that kill the proposal.
The note must be rewritten to say so.

## Cross-reference to prior homework

**CORRECTS `results/c3-r/prior-art-r7a.md`.** The gate is a dedicated, thorough, ten-sweep gate for
exactly this note and it returned NOVEL-WITH-CITATIONS with the finding that the specific rigidity
"appears NOWHERE". **That finding does not survive.** Two causes, both structural and both worth
recording as process lessons:

* The gate ran **when arxiv.org was unreachable**, so everything went through the GCS mirror or
  search snippets. Both agents this session had arxiv.org, export.arxiv.org, zbMATH Open,
  Centre Mersenne and Numdam directly reachable, and fetched Winkelmann's PDF in two versions.
* **Semantic Scholar reports zero citations of arXiv:math/0204195.** A 2002 preprint published in
  Nagoya Math. J. with no recorded citations is invisible to citation-graph search and nearly
  invisible to keyword search in this program's vocabulary. It surfaced only on the query
  "multiplicatively independent algebraic numbers unit disc J(q) isogeny elliptic curves partial
  matching rigidity family".

The gate's other findings are **CONFIRMED**: the Haran-program adjacency (with the dated
attribution correction, already applied), the absence of citing literature for arXiv:2606.06604
(re-verified this session by a direct Semantic Scholar citations query returning `{"data": []}`,
an endpoint the gate could not reach), and the Banaszak–Uetake / Kurokawa / F₁ clearances.

## Searches run (seed no-go)

Sweep:

* arXiv API `id_list=1507.06480` (authorship check: sole author **Koen Thas**); `au:"Shai Haran"` full listing (2509.10959, 2402.04456, 2209.08536, 2204.03107, 2105.14537); `id_list=2209.08536`; `id_list=2606.06604,2501.06560`; direct fetch of the 2606.06604 abs page
* Full fetch + pdftotext + grep of arXiv:1507.06480 (Thas) for haran / diagonal / "Frobenius divisor" / "intersection number" / Tate curve / elliptic — located the Haran 1991 quotation and reference [9]
* Full fetch + pdftotext + grep of arXiv:2209.08536 (Haran) for Riemann hypothesis / Spec Z / arithmetical surface / intersection / Weil / diagonal
* Semantic Scholar Graph API: `paper/arXiv:2606.06604/citations` → `{"data": []}`
* WebSearch: Hom between complex tori ℂ/(ℤ+ℤ i log p/2π) isogeny criterion log p log q rational multiple of π²; NS of product of two elliptic curves rank 2 non-isogenous (surfaced Rosen–Shnidman 1402.2233); Connes–Consani absolute geometry Spec Z Tate curve per prime 2026 citing; CC 2026 "Jacobian of Spec Z"
* arXiv API: `all:"product of Tate curves"` (0); `all:"log p log q"` (8, none relevant); `abs:"Tate curve" AND abs:"explicit formula"`; `abs:"complex tori" AND abs:isogen AND abs:transcend` (0); `abs:"four exponentials"`; `abs:"four-exponentials conjecture"`; `all:"six exponentials theorem"`; `au:Banaszak AND au:Uetake` (2); `all:"absolute tensor product"`; `all:"Spec Z times Spec Z"`; `abs:"arithmetic site"` (15)
* WebSearch: Waldschmidt four exponentials "product of two logarithms" π²; is (log 2)(log 3) a rational multiple of π²; fetch + grep of arXiv:math/0312440 (Conjectures 3.4, 3.6, 3.7 read)
* zbMATH Open API: `ti:"Tate curve" & ti:"product"`; `"Neron-Severi" & "product of elliptic curves" & "non-isogenous"`; `ab:"logarithms of primes" & ab:transcendence & ab:elliptic`; `ab:"explicit formula" & ab:intersection & ab:"Riemann hypothesis" & ab:surface`; `ab:"for each prime" & ab:"elliptic curve" & ab:"Riemann hypothesis"`; `ti:"absolute tensor product"`; `ab:"four exponentials conjecture"` (surfaced Diaz 1997 and 2007); record fetches for Diaz 2007, Winkelmann 2004, Barré-Sirieix et al., Bertrand 1997, the CC Scaling Site papers
* Full fetch + read of Diaz 2007 (Centre Mersenne) and Diaz 1997 (Numdam/Centre Mersenne, in two pdftotext renderings)
* WebFetch of the six-exponentials-theorem reference page (confirming that Roy's **strong** version needs linear independence over the algebraic numbers, which is what blocks the obvious route to (T1))
* WebSearch: Barré-Sirieix–Diaz–Gramain–Philibert Mahler–Manin 1996; Bertrand conjecture algebraic independence J(q₁), J(q₂); Waldschmidt AWS Lecture 5 (Conjectures 5.28–5.35 read verbatim); Kaneko et al. criterion (Nesterenko Theorem A read)
* WebSearch: "multiplicatively independent" algebraic numbers "unit disc" J(q) isogeny partial matching rigidity family — **this is the query that surfaced arXiv:math/0204195**
* Full fetch + pdftotext of arXiv:math/0204195 **v1 and v3**: abstract, Lemma 4/7, Lemma 5, Conjecture 3.2 / Conjecture 1, Proposition 2 / 3, Theorem 2 with full proof, Theorem 3, Corollary 3
* WebSearch: Winkelmann conjecture isogenous ℂ*/ multiplicatively dependent Nagoya 2004 progress since (no post-2004 unconditional progress surfaced)
* WebSearch: Deninger foliated dynamical system obstruction cross-prime; `id_list=2508.15971` (Morishita bridge paper)
* WebSearch: "square of the scaling site" Frobenius correspondences periodic orbits two primes; "Castelnuovo-Severi" vacuous product non-isogenous; no-go theorem obstruction correspondence calculus Weil explicit formula 2025 2026; graph of multiplication by m intersection number (m−n)² diagonal Lefschetz; elliptic curve CM iff τ quadratic imaginary Gelfond–Schneider; Haran 1991 LMS LNS 153 record (MR1110396, Zbl 0744.11042); Haran Compositio 2007 / LNM 1941 / Mysteries of the Real Prime; CC product "C_p" two primes 2024–2026 (surfaced arXiv:2401.08401)
* Fetch + grep of arXiv:2401.08401, 1507.05818, 1603.03191, 1502.05580 §6, 1805.10501
* On-disk: pdftotext + grep of `fetched-r2/u-15b` (CC26) and `u-14b` (Connes 2026 survey) for Tate curve / elliptic / isogen / Hom / End / square / correspondence; `ls`+grep of `sources-extracted/`, `fetched/`, `fetched-r2/`, `fetched-r3/` for haran / kurokawa / four exponentials / Gelfond

Adversary (additional):

* **Verify-don't-trust:** re-fetched arXiv:math/0204195 in **both v1 and v3** and re-extracted with pdftotext independently — confirmed the passage is present already in v1 (15 Apr 2002) and caught the sweep's mixed version numbering
* **Verify-don't-trust:** re-fetched Diaz JTNB 9 (1997) from Centre Mersenne and read §0, §I, §II (Théorème 1), §III (Théorèmes 3–4), §IV (Propositions 1–3), and the full bibliography in a `-layout` rendering
* **Pre-arXiv / non-English / seminar literature:** fetched and read Bertrand, *Fonctions modulaires, courbes de Tate et indépendance algébrique*, Séminaire Delange-Pisot-Poitou 19 (1977–78), exp. 36, from Numdam — the strongest pre-1992 French candidate; **CLEARED** (contains neither the isogeny/multiplicative-dependence statement nor the log-log vs π² statement)
* **Bourbaki:** fetched and grepped Waldschmidt, Sém. Bourbaki 824 (1996–97), from Numdam; **CLEARED**
* Traced the conjecture's origin through Diaz's bibliography to Bertrand's **Madras lecture, January 1996**; established the four-exponentials conjecture as **Schneider 1957 Problem 1**, verified twice independently; found the two-distinct-primes germ in **Alaoglu–Erdős 1944** via Waldschmidt's LIL Ch. 1
* Matrix / quadratic-relation vocabulary: Roy 1992 and Roy–Waldschmidt 1995 (bibliographic data recovered from Diaz's references after Project Euclid and J-STAGE both failed)
* **Different field — complex geometry:** Hopf, Kodaira, Inoue surfaces, Cousin groups, where ℂ*/λ^ℤ is the standard elliptic fiber. `all:"Hopf surface" AND all:isogenous` → 0. **CLEARED**
* **Different field — F₁ / absolute geometry:** Smirnov, Borger, Deitmar, Lorscheid, Durov, Thas's survey — none uses per-prime elliptic fibers or their products. **CLEARED**
* **Different field — dynamical systems:** Deninger's foliated spaces (math/0505354, SWC notes), Morishita 2508.15971, Consani–Marcolli archimedean cohomology. Adjacent in spirit to obstruction O3 (log p as a **length**) but no products and no obstruction statement. **CLEARED with a caveat recorded**
* **Invented vocabulary:** noticed log p · log q = 4π² is Ramanujan's αβ = π² reciprocity with α = (log p)/2, β = (log q)/2, and searched the Berndt–Straub / generalized-Lambert-series literature for a transcendence statement about half-logarithms of primes. Nothing surfaced
* More-general-theorem attack: tested whether Theorem 4 + O1/O2 reduce to "a family of pairwise non-isogenous elliptic curves supports no correspondence calculus" — **it does**, which is why the mathematical weight sits entirely on the non-isogeny
* Citation graph: Semantic Scholar citations of arXiv:math/0204195 → **zero**
* zbMATH review-text: `ab:"multiplicatively dependent" & ab:isogenous`; `ab:"Tate curve" & ab:transcendence`; `ab:"four exponentials" & ab:modular`; `au:Winkelmann & ti:"elliptic curves" & ti:Schanuel`
* On-disk: grepped `sources-extracted/arxiv-2606.06604-absolute-geometry-specZ-fulltext.txt` (1785 lines) for `isogen|Hom(|End(|product of.*curve|correspondence` — clean
* Audited the sweep's own findings against the repository's git log, which is how (E1) was found stale and (E3) false

## Unreachable (seed), and what was substituted

* **alainconnes.org/publications/** — HTTP 403. Substituted: arXiv API author/id queries, zbMATH Open, Semantic Scholar, WebSearch.
* **eudml.org/doc/55503** (Diaz 2007) — HTTP 403. Substituted: the geodesic.mathdoc.fr item record and the Centre Mersenne full PDF, both fetched and read.
* **api.semanticscholar.org** — intermittent HTTP 429; retried. The load-bearing query (citations of 2606.06604) succeeded. Its citation count of 0 for arXiv:math/0204195 is unreliable for a 2002 preprint; the publication record came from zbMATH Open instead.
* **MathSciNet** — no access. Substituted by zbMATH Open throughout, which supplied the Winkelmann, Diaz (1997 and 2007), Barré-Sirieix et al., Bertrand, and Connes–Consani records.
* **D. Bertrand, Ramanujan J. 1 (1997), 339–350** — paywalled; not read directly. Its §5 content reached through two independent secondary sources read in full: Diaz 1997 §I (which quotes and cites "[2], §5" twice) and Waldschmidt's AWS Lecture 5.
* **D. Roy, J. Number Theory 41 (1992), 22–47** — not fetched. Its Corollary 2 (strong six exponentials) reached through Diaz 2007 Théorème 3, Diaz 1997 Lemme 6(B), and a reference page.
* **Th. Schneider, *Einführung in die transzendenten Zahlen*, 1957** — not held. Attribution verified twice independently (Diaz 1997 §0, citing the French edition p. 139; Waldschmidt LIL Ch. 1).
* **Alaoglu–Erdős, Trans. AMS 56 (1944), 448–469** — not read directly; reported verbatim in Waldschmidt LIL Ch. 1.
* **Akatsuka, CNTP 3 (2009), 619–653** — paywalled; not attempted. Nothing here depends on it.
* **Diaz, JTNB 9 (1997)** — the Numdam/Centre Mersenne PDF is an OCR'd scan with partly garbled symbols. Mitigated by reading two renderings and cross-checking every load-bearing statement against Diaz 2007 and Waldschmidt's AWS Lecture 5.

---

# Actions required before posting

Keyed to the file that must change. **MUST** = a referee in the field will name it on sight;
**SHOULD** = it strengthens the paper or forestalls a predictable objection.

## A. `results/a4-no-go/paper.md` — 10 MUST, 3 SHOULD, 3 textual repairs

**MUST cite:**

1. **F. Gonçalves, D. de Laat, N. Leijenhorst, "Multiplicity of nontrivial zeros of primitive
   L-functions via higher-level correlations", Mathematics of Computation (2024),
   doi:10.1090/mcom/4005; arXiv:2303.01095.** Cite in §1.2 and again at Theorem 3.4, with a
   paragraph reconciling "3-level correlations give 96.14% multiplicity ≤ 2 (GRH, support 2)" with
   "the λ′ = 1/2 cubic trace row adds exactly nothing (unconditional, effective support 1)". Their
   eq. (5) is the atom half of Theorem 3.4; their N_n remark is a published negative of the same
   species. *(Volume/issue/pages not independently verified — AMS page HTTP 403.)*
2. **L. Alpöge and R. Furman, "More than two thirds of the zeta zeros are simple and on the
   critical line", arXiv:2608.13637 (v1 13 Aug 2026; v2 19 Aug 2026)** — this is `[P]`. Give the
   arXiv id, authors and version; cite the **earlier** version separately where its fuller §7.2(e)
   wording is relied on. Add a quoting-and-distinguishing paragraph in §1.2 or §1.3.
3. **J. C. Lagarias and B. Rodgers, "Higher correlations and the Alternative Hypothesis",
   Quart. J. Math. (Oxford) 71 (2020), no. 1, 257–280; doi:10.1093/qmathj/haz043;
   arXiv:1905.12123.** §1.5's Alternative-Hypothesis scoping statement currently cites nothing.
4. **J. C. Lagarias and B. Rodgers, "Band-limited mimicry of point processes by point processes
   supported on a lattice", Ann. Appl. Probab. 31 (2021), no. 1, 351–376; doi:10.1214/20-AAP1592;
   arXiv:1907.03391.** Their Thm 1.4 + Prop. 3.4 record the critical-sampling degeneracy Theorem
   3.9 exploits; A4's grid parameters sit in the region their Figure 1 leaves white.
5. **H. L. Montgomery, "The pair correlation of zeros of the zeta function", in Analytic Number
   Theory (St. Louis, 1972), Proc. Sympos. Pure Math. 24, AMS, 1973, 181–193.** Named in Theorem
   4.3, Corollary 4.4 and §6; absent from the reference list.
6. **J. B. Conrey, A. Ghosh and S. M. Gonek, "Simple zeros of the Riemann zeta-function",
   Proc. London Math. Soc. (3) 76 (1998), 497–522.** The second integrality level.
7. **D. A. Hejhal, "On the triple correlation of zeros of the zeta function", Internat. Math. Res.
   Notices 1994, no. 7, 293–302.**
8. **Z. Rudnick and P. Sarnak, "Zeros of principal L-functions and random matrix theory",
   Duke Math. J. 81 (1996), 269–322** — plus one sentence pinning which statement is invoked
   (Thm 1.1 unconditional for smooth h; a characteristic function requires RH, their Thm 1.2).
   This bears directly on flag F2 in §8.3.
9. **H. M. Bui and D. R. Heath-Brown, "On simple zeros of the Riemann zeta-function", Bull. London
   Math. Soc. 45 (2013), 953–961.** Cited as `[BHB13]` with no entry.
10. **A. Chirre, F. Gonçalves and D. de Laat, "Pair correlation estimates for the zeros of the zeta
    function via semidefinite programming", Adv. Math. 361 (2020), 106926; arXiv:1810.08843.**
    Cited as `[CGdL20]` with no entry — and add one sentence on their Corollary 3
    (N_d ≥ 0.8477 N (RH) / 0.8486 N (GRH)) and their inequality (7), the published convex-programming
    form of the device Lemma 4.2 uses.

**SHOULD cite:**

11. **T. Kuna, J. L. Lebowitz and E. R. Speer, "Realizability of point processes", J. Stat. Phys.
    (2007), doi:10.1007/s10955-007-9393-y, arXiv:math-ph/0612075; and "Necessary and sufficient
    conditions for realizability of point processes", Ann. Appl. Probab. 21 (2011), no. 4,
    doi:10.1214/10-AAP703, arXiv:0910.1710.** §2.4 re-argues their problem from scratch.
    *(Volume/page numbers for the 2007 paper not independently verified.)*
12. **H. Cohn, D. de Laat and A. Salmon, "Three-point bounds for sphere packing",
    arXiv:2206.15373** — now a one-line aside only; GdLL is the in-field comparandum and makes the
    sphere-packing comparison itself.
13. **S. Karlin and W. J. Studden, *Tchebycheff Systems: With Applications in Analysis and
    Statistics*, Interscience, 1966** *(reference not independently verified)*, for the one-sided
    Chebyshev–Markov–Stieltjes principle under which odd moments do not improve one-sided bounds.

**Textual repairs (not citations):**

* Both **"Section 7.5(e)"** pointers (§1.2 and the `[P]` reference entry) → **§7.2(e)**. There is
  no §7.5 in the parent.
* **Relabel the atom half of Theorem 3.4 / Proposition 3.3** as the Stirling change of basis
  between power sums and falling factorials, and confine the novelty claim to the pair term
  6 Σ m_p²(m_p−1)A_p².
* **Disambiguate 0.8051** wherever it appears: A4's finite-N matched-budget corner
  (3N − B₁(1+ε))/(2N) at ε = 0.05 is *not* Farmer–Gonek–Lee's published distinct-zeros constant,
  which is also 0.8051 to four decimals.
* Optional but recommended: label Lemma 3.8 / Prop. 3.11 as critical-sampling Parseval and
  Shannon–Whittaker orthogonality; label the "convexified analyses are unsound" moral as the
  textbook integrality gap; keep the proofs for the Lean queue.

## B. `results/c3-r/m0-axiom-note.md` — 10 MUST, 7 SHOULD, 2 textual repairs

**MUST cite:**

1. **J. Borger, "Lambda-rings and the field with one element", arXiv:0906.3146 (2009)** — carries
   the whole (PF2)+(PF3) content: a Λ-structure on a flat ℤ-space *is* a commuting family of
   Frobenius endomorphisms indexed by the primes, with ψ_m ψ_n = ψ_mn and primitivity at the
   primes by unique factorization.
2. **A. Connes and C. Consani, "Geometry of the arithmetic site", Adv. Math. 291 (2016), 274–329;
   doi:10.1016/j.aim.2015.11.045; arXiv:1502.05580** — Thm 1.2 / Thm 7.7 prove
   Ψ(λ) ∘ Ψ(λ′) = Ψ(λλ′) for Frobenius correspondences realized as congruences in the **square**.
   State the differentiators explicitly (their index monoid ℝ*₊ is divisible, so "primitivity at
   the primes" has no analogue; no nef-polarization degree calculus; no effectivity axiom;
   characteristic-one semiringed topos, not an adelic curve).
3. **A. Connes, "An essay on the Riemann Hypothesis", arXiv:1509.05576; in *Open Problems in
   Mathematics* (J. F. Nash Jr. and M. Th. Rassias, eds.), Springer, 2016** — §2.3 contains the
   note's (PF1) polarized square with fiber classes and the numbered basic fact *"If D is a
   strictly positive divisor then D·ξ₀ + D·ξ₁ > 0"* (the note's §5 chain); §4.3.1 the N^× Frobenius
   monoid and the composition law; **§4.3.2 the note's own §7 diagnosis**: *"At this point, what is
   missing is an intersection theory and a Riemann–Roch theorem on the square of the arithmetic
   site."* On disk at `fetched-r2/t-20b`.
4. **H. G. Diamond and W.-B. Zhang, *Beurling Generalized Numbers*, AMS Mathematical Surveys and
   Monographs 213, 2016**, Ch. 1 §1.1 and Ch. 17 — the published general form of §7's conclusion
   (*"a proof of the Riemann hypothesis will require more than just the multiplicative structure of
   integers and smallness of N(x) − x"*), with an RH-**true** system (Thm 17.11) and the RH-false
   one (Thm 17.14) in one chapter. On disk at `fetched-r2/t-50`. **This supersedes the sweep's
   SHOULD-cite of W.-B. Zhang, Math. Ann. 337 (2007), 671–704.**
5. **C. Deninger, "There is no 'Weil-'cohomology theory with real coefficients for arithmetic
   curves", arXiv:2204.02714v2 (final version for Annali SNS Pisa, Cl. Sci.)** — a published no-go
   theorem about an explicitly stated axiom class for an RH substrate on an arithmetic curve: the
   note's exact genre. Its 2.3 is the note's (PF6) trace reading, 2.6 its (PF5), 2.7 its M3/M4
   chain, and Theorem 2.13 is the impossibility. On disk at `fetched/x-04`.
6. **A. Connes and C. Consani, "Riemann–Roch for Spec Z-bar", Bull. Sci. Math. 187 (2023),
   art. 103293; doi:10.1016/j.bulsci.2023.103293; arXiv:2205.01391; with the sequel
   "Riemann–Roch for the ring Z", C. R. Math. Acad. Sci. Paris 362 (2024), 229–235;
   doi:10.5802/crmath.543** — §7's "a substrate-level input no current object supplies" is
   overstated; cite and distinguish from h⁰_θ.
7. **C. Deninger, "Some analogies between number theory and dynamical systems on foliated spaces",
   Documenta Mathematica, Extra Volume ICM 1998, I, 163–186** — §3.3's "Lefschetz-tie axiom" is
   Deninger's conjecture, in print for 28 years.
8. **J. B. Conrey and X.-J. Li, "A note on some positivity conditions related to zeta and
   L-functions", Internat. Math. Res. Notices 2000, no. 18, 929–940; arXiv:math/9812166** — the
   published exemplar of §6.3's over-breadth move, on the same witness function χ₄. On disk at
   `fetched/p1-06`; already given a human-grade read by an earlier session of this program.
9. **E. Bombieri and A. Ghosh, "Around the Davenport–Heilbronn function", Russian Math. Surveys
   66:2 (2011), 221–270; doi:10.1070/rm2011v066n02abeh004740 (= Uspekhi Mat. Nauk 66:2 (2011),
   15–66, doi:10.4213/rm9410)** — the standard modern survey; §6.1 cites only the 1936 originals.
10. **G. Banaszak and Y. Uetake:** "Abstract intersection theory and operators in Hilbert space",
    Comm. Number Theory Phys. 5 (2011), 699–712 (arXiv:0908.2909); "Standard models of abstract
    intersection theory for operators in Hilbert space", Bull. Polish Acad. Sci. Math. 63 (2015),
    149–175 (arXiv:1210.3526); "Abstract intersection theory for zeta-functions: geometric
    aspects", Funct. Approx. Comment. Math. 64.2 (2021), 251–265. The only prior published
    axiomatization of a Weil-style intersection calculus for zeta. Distinguish: theirs is
    equivalent to RH (non-vacuous but circular); this note's is shown vacuous at coefficient level.

**SHOULD cite:**

11. **M. Flach and B. Morin, "Deninger's conjectures and Weil–Arakelov cohomology", Münster J.
    Math. 13 (2020), 519–540; doi:10.17879/90169642993** — the precedent for taking an RH axiom
    framework seriously and working out what it does and does not give.
12. **A. Connes, C. Consani and M. Marcolli, "Fun with F₁", J. Number Theory 129 (2009), 1532–1561;
    doi:10.1016/j.jnt.2008.08.007** — the §3.2 exhibit {graph(z ↦ zⁿ)} is the Bost–Connes
    endomotive's own Frobenius family, treated there as Frobenius correspondences over F₁. Citing
    it **strengthens** the vacuity point.
13. **A. Connes and C. Consani, "Geometry of the scaling site", Selecta Math. (N.S.) 23 (2017),
    1803–1850; doi:10.1007/s00029-017-0313-y; and "The Scaling Site", arXiv:1507.05818** — the
    scaling site is the semidirect product of the half-line by the monoid of positive integers
    acting by multiplication, i.e. the note's own (ℕ^×, ·). Relevant to §4(b).
14. **A. Connes and C. Consani, "The Riemann–Roch strategy: complex lift of the scaling site", in
    *Advances in Noncommutative Geometry*, Springer, 2019, 53–125;
    doi:10.1007/978-3-030-29597-4_2; arXiv:1805.10501.**
15. **A standard text for the completely-multiplicative ⟹ Euler-product identity:** T. M. Apostol,
    *Introduction to Analytic Number Theory*, Springer, 1976, the Dirichlet-series/Euler-product
    chapter; or H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I*, CUP, 2007,
    §1.2. Cite by chapter, not by theorem number *(no theorem number was verified)*.
16. **A. LeClair and G. Mussardo, "Riemann zeros as quantized energies of scattering with
    impurities", arXiv:2307.01254; and G. França and A. LeClair, "A theory for the zeros of Riemann
    zeta and other L-functions (updated)", arXiv:1407.4358** — the "GRH requires the Euler product,
    and DH is the counterexample" reading, in print in physics vocabulary. Use these in §6.1 rather
    than resting on unfetched search-result text.
17. **Yu. I. Manin, "Lectures on zeta functions and motives (according to Deninger and Kurokawa)",
    Astérisque 228 (1995), 121–163** — the provenance of "absolute Descartes powers
    Spec ℤ × … × Spec ℤ" and "a canonical absolute Frobenius", thirty years earlier. On disk at
    `fetched/x-02`.

**Textual repairs (not citations):**

* **Blomer–Leung**: drop "monoid" as the authors' word (`grep -c -i monoid` = 0 in arXiv v2),
  restate Theorem 1.1 in their terms, mark "monoid" as the note's own gloss, and add one sentence
  on how a converse theorem hosts an exclusion. **Propagate the same fix to `BARRIER-ZOO.md` I.1.**
  The Adv. Math. 485 (2026), art. 110716 citation is correct.
* **Soften §7's last sentence** on θ-effectivity so it does not assert that no current object
  supplies a Riemann–Roch on the arithmetic curve.
* Add a "Prior art and what is new" section (a new §2.0 or an appendix) naming Borger,
  Connes–Consani, Deninger, Flach–Morin and Banaszak–Uetake with one sentence each.
* **Open item for the author, not a search result:** run §5's admissibility condition against the
  note's own §7 Kaczorowski–Perelli citation and either report the collapse or say why the two
  coefficient frames never meet.

## C. `results/c3-r/m1-noncircularity.md` — 10 MUST, 4 SHOULD, 4 textual repairs

**MUST cite:**

1. **J. S. Milne, "The Riemann Hypothesis over Finite Fields: From Weil to the Present Day",
   arXiv:1509.00797; in *The Legacy of Bernhard Riemann After One Hundred and Fifty Years*
   (S.-T. Yau et al., eds.), ALM 35; reprinted ICCM Notices 4 (2016), no. 2, 14–52** — §1 publishes
   the note's §§3–7 end to end, and supplies (IN1)'s provenance and §9's correct history.
2. **E. Bombieri, "Problems of the Millennium: The Riemann Hypothesis", Clay Mathematics Institute
   official problem description, pp. 9–10** — the closest published statement of the note's thesis,
   inside the official RH problem statement, with a **different** Weil-free input list
   (Riemann–Roch plus finiteness of families of curves of given degree, attributed to Severi 1906).
3. **A. Connes and C. Consani, "The Riemann–Roch strategy: complex lift of the Scaling Site",
   arXiv:1805.10501, §3 and §3.1** — the leading contemporary RH program adopts exactly the route
   the note certifies and states the same logical requirement in its own words.
4. **A. Grothendieck, "Sur une note de Mattuck–Tate", J. reine angew. Math. 200 (1958), 208–215;
   doi:10.1515/crll.1958.200.208** — cite for **content**, not merely existence: his §2 itemizes
   the input list by number and his post-Theorem-1.1 remark is the note's own (IN6) scoping.
5. **B. Segre, Ann. Mat. Pura Appl. (4) 16 (1937), 157–163, and J. Bronowski, J. London Math. Soc.
   13 (1938), 86–90** — algebraic proofs of the index theorem valid in **any characteristic**,
   twenty years before Mattuck–Tate and ten before Weil 1948. *(Originals not fetched by any agent;
   dates and pages taken from Milne's bibliography, which both agents read. Do **not** use the
   denisevellachemla retranscription's bibliography, which prints 1957/1958 and "G. Bronowski".)*
6. **S. L. Kleiman, "Algebraic Cycles and the Weil Conjectures", in *Dix exposés sur la cohomologie
   des schémas*, North-Holland, 1968, 359–386**, Theorem 4.7 and Remark 3.10 — the
   standard-conjectures template whose whole architecture presupposes that Hodge-type positivity is
   logically upstream of RH.
7. **K. Ito, T. Ito and T. Koshikawa, "The Hodge standard conjecture for self-products of K3
   surfaces", arXiv:2206.10086; J. Algebraic Geom. 34 (2025), no. 2, 299–330** *(journal
   volume/pages from search-surfaced AMS metadata only)*, **Remark 1.3** — the published
   non-circularity audit of the same positivity engine.
8. **G. Ancona, "Standard conjectures for abelian fourfolds", arXiv:1806.03216; Invent. Math. 223
   (2021)** — §1 "Brief historical panorama" publishes the note's §9 lineage repair verbatim; Lemma
   7.10 is the matching case where the proof *does* consume the Weil conjectures.
9. **J. S. Milne, "Grothendieck's standard conjecture of Lefschetz type over finite fields",
   arXiv:2011.06563 (jmilne.org/math/articles/LFF.pdf, v1.1, 14 Jul 2022)**, abstract; with
   **J. S. Milne, "The Tate conjecture over finite fields (AIM talk)", arXiv:0709.3040**,
   footnote 4 and Aside 9.4 — the same dependency bookkeeping as ordinary professional practice.
10. **The arithmetic branch, for §8's scope paragraph:** K. Künnemann, "Some remarks on the
    arithmetic Hodge index conjecture", Compositio Math. 99 (1995), no. 2, 109–128; H. Gillet and
    C. Soulé, "Arithmetic analogs of the standard conjectures", in *Motives* (Seattle 1991),
    PSPM 55.1 (1994), 129–140 *(reference not independently verified)*; A. Moriwaki, "Hodge index
    theorem for arithmetic cycles of codimension one", alg-geom/9403011; X. Yuan and S.-W. Zhang,
    "The arithmetic Hodge index theorem for adelic line bundles" I and II, arXiv:1304.3538 /
    arXiv:1304.3539 (Math. Ann. 367 (2017)); with Faltings–Hriljac for arithmetic surfaces
    *(reference not independently verified)*.

**SHOULD cite:**

11. **E. Hallouin and M. Perret, "From Hodge Index Theorem to the number of points of curves over
    finite fields", arXiv:1409.2357** — the modern continuation, and the source that independently
    confirms §9's Hartshorne exercise pins with the page number ("[Har77, exercice 1.9, 1.10
    p. 368]").
12. **E. Kani, "On Castelnuovo's equivalence defect", J. reine angew. Math. 352 (1984), 24–70**
    *(reference not independently verified; known via Milne footnote 14)* — an independent route to
    the defect inequality in characteristic p.
13. **I. Vainsencher and J. F. Voloch, "On the Castelnuovo–Severi inequality", J. reine angew.
    Math. 390 (1988), 114–116; doi:10.1515/crll.1988.390.114** — a further short published proof.
14. **C. Deninger, "The Hilbert–Pólya strategy and height pairings"** *(venue not independently
    verified; read from the on-disk corpus at `fetched/x-17`)* — reads the Néron–Tate positivity as
    **support** for a positivity route to RH, which is the reading §8 must answer.

**Textual repairs (not citations):**

* **§9 lineage**: replace "the first modern non-circular derivation" for Mattuck–Tate 1958 with
  Ancona's published sentence and the Segre/Bronowski/Severi record.
* **§8 headline**: "**a** proof", not "**the** proof" — Bombieri's and Segre/Bronowski's routes are
  independent Weil-free derivations of the same theorem.
* **Do NOT make the sweep's repair 3(b)** ("Weil's proof" → "the Mattuck–Tate/Grothendieck proof").
  Milne's §1 says τ(D ∘ D′) ≥ 0 *is* a restatement of Castelnuovo–Severi. The note is correct as
  written.
* **§8 "Scope of the claim"**: rewrite against the arithmetic Hodge index theorem (item 10), saying
  why the codimension-one arithmetic inequality is not the missing piece. As written the paragraph
  invites a one-line refutation.
* Optional: drop (IN4)+(IN7) in favor of Grothendieck's hyperplane-section route, which shortens
  the ledger; and correct the description of Grothendieck's Prop. 2.1, which needs **no** positivity
  hypothesis on D.

## D. `results/c3-r/seed-no-go-note.md` — 10 MUST, 5 SHOULD, 4 textual repairs

**MUST cite:**

1. **J. Winkelmann, "On elliptic curves in SL₂(ℂ)/Γ, Schanuel's conjecture and geodesic lengths",
   Nagoya Math. J. 176 (2004), 159–180; preprint arXiv:math/0204195 (v1 15 Apr 2002, v3 8 Apr
   2003)** — anticipates Theorems 1, 2 and 3 and the §7 Schanuel argument; his Conjecture 1 is the
   note's (T1)-refuting statement. Restate Theorems 1–3 as a specialization and cite consistently
   from v3 / the published version, noting the argument is already in v1.
2. **G. Diaz, "La conjecture des quatre exponentielles et les conjectures de D. Bertrand sur la
   fonction modulaire", J. Théor. Nombres Bordeaux 9 (1997), no. 1, 229–245** — states (T1)
   verbatim as (C4E faible), gives the note's own four-exponentials reduction in the next sentence,
   and proves (C0) ⟺ (C6). Propositions 1 and 3(1) are unconditional partial results the note
   should report.
3. **D. Bertrand, "Theta functions and transcendence", Madras Number Theory Symposium, January
   1996; Ramanujan J. 1 (1997), no. 4, 339–350, §5** — the origin of the weak four-exponentials
   conjecture and of the algebraic-independence conjecture (CDB). *(Paywalled; content and the §5
   attribution read via Diaz 1997 §I and its bibliography entry [2], and via Waldschmidt's AWS
   Lecture 5 Conjectures 5.34/5.35. Reference not independently verified from the source.)*
4. **Th. Schneider, *Einführung in die transzendenten Zahlen*, Springer, 1957, Ch. V §4, Problem 1
   (French ed.: *Introduction aux nombres transcendants*, Gauthier-Villars, 1959, p. 139)** — the
   four-exponentials conjecture, with the later explicit formulations by S. Lang (Sém. Bourbaki 305,
   1965/66; Topology 5 (1966), 363–370) and K. Ramachandra (Acta Arith. 14 (1968), 65–88).
   *(Not held; attribution verified twice via Diaz 1997 §0 and Waldschmidt LIL Ch. 1.)*
5. **K. Barré-Sirieix, G. Diaz, F. Gramain and G. Philibert, "Une preuve de la conjecture de
   Mahler–Manin", Invent. Math. 124 (1996), no. 1–3, 1–9** — gives j(E_p) transcendental, hence
   End(E_p) = ℤ, unconditionally and with more information than Gelfond–Schneider yields here. Cite
   alongside Gelfond–Schneider, not instead of it.
6. **A. Connes and C. Consani, "The Scaling Site", C. R. Math. Acad. Sci. Paris 354 (2016), 1–6;
   arXiv:1507.05818 (July 2015); and "Geometry of the Scaling Site", Selecta Math. (N.S.) 23
   (2017), 1803–1850; arXiv:1603.03191** — **lineage repair.** These, not arXiv:2501.06560, are the
   first appearance of the per-prime elliptic-curve analogue.
7. **A. Connes and C. Consani, "The Riemann–Roch strategy: complex lift of the Scaling Site", in
   *Advances in Noncommutative Geometry*, Springer, 2019, 53–125; arXiv:1805.10501** — the CC
   program's own moduli of triangular elliptic curves with the equivalence relation generated by
   isogenies. Adjacent to the construction and currently uncited.
8. **A. Connes and C. Consani, "Knots, Primes and the adele class space", arXiv:2401.08401 (January
   2024)** — a genuine two-prime construction inside the CC program (Γ\(ℚ_p × ℚ_q × ℝ) with
   Γ = {±p^m q^n}), predating the note's claimed lineage. Distinguish: knot/linking-number analogy,
   not a correspondence calculus.
9. **D. Roy, "Matrices whose coefficients are linear forms in logarithms", J. Number Theory 41
   (1992), 22–47** *(not fetched; content via Diaz)* **and G. Diaz, "Produits et quotients de
   combinaisons linéaires de logarithmes de nombres algébriques: conjectures et résultats
   partiels", J. Théor. Nombres Bordeaux 19 (2007), no. 2, 373–391; doi:10.5802/jtnb.592** — the
   published state of the art on (T1), and the citable reason the proven machinery misses it
   (Diaz 2007 Corollaire 1(1) needs (λ₀, λ₂, λ̄₂) to be ℚ̄-free, which fails for λ₂ = log q real).
10. **M. Waldschmidt, "Open Diophantine Problems", Moscow Math. J. 4 (2004), 245–305;
    arXiv:math/0312440, Conjecture 3.7; and M. Waldschmidt, AWS Lecture 5 "Conjectures and open
    problems", Conjectures 5.34 and 5.35** — the canonical matrix statement of 4EC and the printed
    statement of Bertrand's conjecture.

**Already done — no action:** **S. Haran, "Index theory, potential theory, and the Riemann
hypothesis", in *L-functions and Arithmetic* (Durham, 1989), LMS Lecture Note Ser. 153, CUP, 1991,
257–270, at p. 259 (MR1110396, Zbl 0744.11042)**, with **K. Thas, "A taste of Weil theory in
characteristic one", arXiv:1507.06480**, as the surveying chapter that quotes him. Applied
2026-08-27; key `Ha15` → `Ha91`. Note for §1.3: Haran's ⟨f, g⟩ := W(f * g*) **is** the commission's
requirement (R2), proposed in print in 1991.

**SHOULD cite:**

11. **J. Rosen and A. Shnidman, "Néron–Severi groups of product abelian surfaces",
    arXiv:1402.2233 (2014)** — the precise modern reference for Theorem 4's decomposition, beyond a
    chapter-level pointer to Birkenhake–Lange.
12. **Yu. V. Nesterenko, "Modular functions and transcendence questions", Mat. Sb. 187 (1996),
    no. 9, 65–96; and Yu. V. Nesterenko and P. Philippon (eds.), *Introduction to Algebraic
    Independence Theory*, Lecture Notes in Math. 1752, Springer, 2001** *(the latter not
    independently verified)*.
13. **M. Morishita, "On a relation between Deninger's foliated dynamical systems and
    Connes–Consani's adelic spaces", arXiv:2508.15971 (August 2025)** — the current bridge between
    the two traditions the note keeps alive.
14. **L. Alaoglu and P. Erdős, "On highly composite and similar numbers", Trans. Amer. Math. Soc.
    56 (1944), 448–469** *(not read directly; reported verbatim in Waldschmidt LIL Ch. 1)* — the
    1944 germ of the same question about two distinct primes.
15. **J. S. Milne, "The Riemann Hypothesis over Finite Fields: From Weil to the Present Day",
    arXiv:1509.00797** — a published survey pointer for the classical Castelnuovo–Severi inequality
    used in §5(d), so a referee need not follow a program-internal file path.

**Textual repairs (not citations):**

* **Delete** the §9 sentence "The question (T1) appears to be unrecorded in the literature in this
  form and is stated here as open" and any §9 claim that nothing anticipates the obstruction.
* **Fix §1.2's lineage sentence** ("first appears … in January 2025") — see MUST item 6.
* **Do NOT change the `[CC26]` title.** The sweep's request to drop "and the Fargues–Fontaine
  curve" is based on an arXiv API truncation at a TeX macro; the note's record (commit `cc70ee9`)
  already adjudicated this correctly.
* **Reframe §§2–4**: state plainly that the rigidity is Winkelmann's, specialized here to the
  Connes–Consani per-prime Tate curves (June 2026), sharpened to the exact Hom group and isogeny
  degree, and that the new work is the Néron–Severi and diagonal-residue consequences and the
  resulting no-go.

---

# Notes for the register

* **Where the program's value lies.** Three of the four documents are, in substantial part,
  standard mathematics, and two of them say so themselves. M1 is standard mathematics with a
  published framing and should ship with its "zero novelty is claimed" paragraph intact. The seed
  note's headline rigidity is a 2002 theorem. That is not a failure of the program; it is the gate
  working. What survives — A4's δ₀ = 0, the capacity theorem, the garnish theorem, the pair-channel
  closure, M0's adelic-curve substrate proposal and vacuity certificate, the seed note's
  construction and no-go — survives because it was attacked and held.
* **Process lesson 1 (from M0 and the seed note): grep the program's own PDF corpus before going
  online.** Four of the M0 adversary's heaviest findings, including one the program had already
  read line by line in an earlier session, were sitting in `fetched/` and `fetched-r2/`.
* **Process lesson 2 (from A4): traverse the citation graph, do not keyword-search your own
  vocabulary.** The closest published third-party paper to A4 in the world was found by Semantic
  Scholar `/citations` traversal from a paper the sweep had already identified, and by nothing else.
* **Process lesson 3 (from M1): search the literature's phrase, not yours.** "Circular" returns
  zero hits in Milne, Kleiman, Ancona, Ito–Ito–Koshikawa and Hallouin–Perret. "Avoid the Weil
  conjecture" returns the anticipation.
* **A standing limitation on every "nothing published surfaced" statement in this report.** arXiv
  full-text search is genuinely unavailable — the public API indexes metadata only. Every negative
  here means "nothing surfaced under the queries run against abstracts, WebSearch, Semantic
  Scholar, Crossref, zbMATH Open where reachable, and the program's on-disk corpus." It does not
  mean "nothing exists."
