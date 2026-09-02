# NOVELTY / PRIOR-ART SWEEP — SESSION 14 CLAIMS C1–C10 — CHECK **O** (Opus 5)

**Program:** RH program, direction C3-r. **Session 14.** **Standing order 7** (two models,
independently). **Date of the sweep:** 2026-09-03 local.
**Author:** novelty agent, check **O**. The sibling check is a different model; I have not read its
output and nothing below is softened in the expectation that it will catch something.
**Standing order 5:** every statement below about a source is from a document I opened *in this
session* (URL or on-disk path + location stated). Nothing is from memory. Where a source could not
be reached it is named in full and marked UNDETERMINED.
**Extends, does not repeat:** `results/c3-r/referee-s14/novelty-O.md` §6 (search log S-01…S-45),
`novelty-F.md`, `novelty-adjudication.md`. Searches already run there are not re-run; where a
Session-14-earlier search bears on a claim here it is cited by its S-nn id.

*(status: in progress — sections appended as they are decided)*

---

## C6 — W3: the [ÁLKL23] coincidence statements, and the erratum question

**Claim under test.** (i) [ÁLKL23] = arXiv:2304.00798, *Topology of the space of conormal
distributions*, statements **Prop. 3.2, Cor. 3.4, Cor. 4.5, Prop. 6.10, Cor. 6.12, Cor. 6.19,
Cor. 7.11** are false as literally stated (explicit Cauchy-sequence witness; a one-point transversal
already suffices); (ii) Wengenroth's acyclicity criterion nevertheless holds for the compactly based
symbol spectra by a Landau–Kolmogorov-type interpolation; (iii) (M\*) is a formal invariant of
sup-seminorm parametrization over any compact Hausdorff T. Plus the charter's extra task: **find any
erratum, corrigendum, v4, or MathSciNet/zbMATH review noting the issue.**

### C6-a. The erratum question — ANSWERED, NEGATIVE, and the paper is PUBLISHED

| Fact | Source, opened this session |
|---|---|
| arXiv version history is **v1 (3 Apr 2023), v2 (29 Jul 2023), v3 (1 Jun 2024)**. **There is no v4.** Comments field is `55 pages, index of notation`; **no erratum/corrigendum note, no journal-ref on the abs page** | `https://arxiv.org/abs/2304.00798`, fetched 2026-09-03 |
| The paper **is published**: *J. Pseudo-Differ. Oper. Appl.* **15**:47 (2024), 68 printed pages, received 28 Jul 2023 / accepted 7 May 2024 / published online 9 Jun 2024, **© The Author(s) 2024, open access CC-BY** | published PDF, title page + running heads, opened this session |
| zbMATH Open record **Zbl 1564.46031** (zbMATH id 7901419), document_type `journal article`, DOI `10.1007/s11868-024-00617-y`, datestamp 2024-08-26. **The editorial contribution is of type `summary`, with `reviewer: name = null` and text `"zbMATH Open Web Interface contents unavailable due to conflicting licenses."` — i.e. there is NO independent zbMATH review, and nothing in the record notes any defect.** | zbMATH REST API `api.zbmath.org/v1/document/_search?search_string=Topology of the space of conormal distributions`, this session |
| Semantic Scholar: `citationCount: 0`; the citations endpoint for `arXiv:2304.00798` returns an **empty list**. So there is no citing work that could have recorded a correction | `api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11868-024-00617-y` and `.../paper/arXiv:2304.00798/citations`, this session |
| Unpaywall: `is_oa: true`, three OA locations (Springer, HAL `hal-04742200v1`, USC Minerva `hdl.handle.net/10347/34155`). **No "Correction to…" companion DOI is listed anywhere** | `api.unpaywall.org/v2/10.1007/s11868-024-00617-y`, this session |
| MathSciNet: **not searched** — permanently closed to this program (`results/corpus-routing.md` caveat 13). Named as the single residual gap for C6-a | — |

**Verdict C6-a: NO erratum, corrigendum, v4, retraction, correction-notice, or critical review exists
as of 2026-09-03.** The defective statements stand in the published, peer-reviewed, open-access text.
(Springer's own `link.springer.com` PDF endpoint is behind an Akamai "Client Challenge" JS wall and
returned a 3,038-byte HTML challenge page to `curl` on three attempts; the identical PDF was obtained
from the USC Minerva institutional repository, `https://minerva.usc.gal/bitstreams/f0f5fe37-86b7-464d-bf89-35de6fb7d44a/download`,
and is saved beside this file as `ALKL-2024-topology-conormal-distributions-PUBLISHED-JPDOA-15-47.pdf`.)

### C6-b. **MATERIAL FINDING — the program's statement numbers are arXiv-v1 numbers and DO NOT match the published article**

I read both texts side by side this session (`pdftotext -layout` of
`fetched-r3/r3s-18-…-arxiv-2304.00798v1-SESSION8-FETCH.pdf` and of the published PDF). §§3–4 keep
their numbering; **§§6–7 are renumbered in the published version.** The published statements are word
for word the same mathematics, so the refutation transfers — but every program citation of a §6/§7
number currently points at the wrong published statement.

| Statement | arXiv v1 (program's number) | **Published (J. Pseudo-Differ. Oper. Appl. 15:47)** | Published text, verbatim |
|---|---|---|---|
| symbol semi-norms | Prop. 3.2 | **Prop. 3.2** (unchanged) | "The semi-norms (3.4) and (3.5) together describe the topology of S^m(U × R^l)." |
| symbol coincidence | Cor. 3.4 | **Cor. 3.4** (unchanged) | "For m < m′, the topologies of S^{m′}(U × R^l) and C^∞(U × R^l) coincide on S^m(U × R^l). Therefore the topologies of S^∞(U × R^l) and C^∞(U × R^l) coincide on S^m(U × R^l)." |
| acyclicity of S^∞ | Cor. 3.6 | **Cor. 3.6** (unchanged) | "S^∞(U × R^l) is an acyclic Montel space, and therefore complete, boundedly retractive and reflexive." Proof: "Corollary 3.4 gives the property of being acyclic…" |
| conormal coincidence | Cor. 4.5 | **Cor. 4.5** (unchanged) | "For m < m′, m″, the topologies of I^{m′}(M, L) and I^{m″}(M, L) coincide on I^m(M, L)." Proof, in full: "Use Corollary 3.4 and the TVS-embeddings (4.10)." |
| A^m semi-norms | Prop. 6.10 | **Prop. 6.12** | "The semi-norms (6.42) and (6.43) together describe the topology of A^m(M)." |
| A-coincidence | Cor. 6.12 | **Cor. 6.14** | "If m′ < m, then the topologies of A^{m′}(M) and C^∞(M̊) coincide on A^m(M). Therefore the topologies of A(M) and C^∞(M̊) coincide on A^m(M)." |
| Ȧ-coincidence | Cor. 6.19 | **Cor. 6.21** | "For m < m′, m″, the topologies of Ȧ^{m′}(M) and Ȧ^{m″}(M) coincide on Ȧ^m(M)." |
| K(M)-coincidence (program says TRUE) | Cor. 6.24 | **Cor. 6.27** | "For m < m′, m″, the topologies of K^{m′}(M) and K^{m″}(M) coincide on K^m(M)." |
| J-coincidence | Cor. 7.11 | **Cor. 7.13** | "If m′ < m, then the topologies of J^{m′}(M, L) and C^∞(M\L) coincide on J^m(M, L). Therefore the topologies of J(M, L) and C^∞(M\L) coincide on J^m(M, L)." |
| K(M,L)-coincidence (program says TRUE) | Cor. 7.20 | **Cor. 7.22** | "For m < m′, m″, the topologies of K^{m′}(M, L) and K^{m″}(M, L) coincide on K^m(M, L)." |

Note the trap: in the **published** text, `Cor. 7.11` and `Cor. 7.20` are *totally-reflexive-Fréchet*
statements ("J^{(s)}(M, L) is a totally reflexive Fréchet space"; "K^{(s)}(M, L) is a totally
reflexive Fréchet space") — **true, and unrelated to the coincidence question.** A referee checking
the program's list against the published paper would find the program apparently calling a true and
elementary reflexivity statement false. Likewise published `Prop. 6.10` is a *density* statement
("For m′ < m, C_c^∞(M̊) is dense in x^m L^∞(M) with the topology of x^{m′}L^∞(M)"), not the
semi-norm statement the program refutes.

**Action owed (source-integrity, severity MAJOR for external circulation, nil for the mathematics):**
`results/c3-r/s14/w3-adjudication.md` §0, §3.1–§3.5, §5.1, §9 rows N1–N5, N9, N16 and every
downstream ledger line must cite **both** numberings, e.g. "[ÁLKL23] Cor. 6.12 (v1) = Cor. 6.14
(published)". The `w3-adjudication.md` header states the probes diffed v1 against v3 and found the
statements verbatim; that is consistent with what I see, but v3 is the accepted manuscript and the
**published** renumbering was not caught by either probe or by the adjudicator.

### C6-c. Prior-art verdicts on the substance

| Sub-claim | Verdict | Evidence |
|---|---|---|
| Prop. 3.2 / Cor. 3.4 / Cor. 4.5 / (v1) Prop. 6.10, Cor. 6.12, Cor. 6.19, Cor. 7.11 are **false as literally stated** | **NOVEL** | No erratum, no critical citing work, no review (C6-a); zero citations; the statements are printed unaltered in the peer-reviewed version. Nobody has published the observation. |
| Wengenroth acyclicity of the compactly based symbol spectra via a Landau–Kolmogorov-type interpolation | **PARTIAL — see C6-d below** | the *conclusion* (acyclicity/boundedly-retractive symbol LF-spaces) is in print elsewhere; the *verification of Wengenroth's 0-neighborhood criterion by interpolation* is what is new |
| (M\*) is a formal invariant of sup-seminorm parametrization over any compact Hausdorff T, both directions | **NOVEL (folklore-grade)** | no source located; see search log C6-S5…C6-S7 |

---

## C1 — Packet indiscreteness; X₀ not T₀. **Verdict: PARTIAL — MAJOR credit obligation.**

**Claim.** In X₀ = X(Spec ℤ) with the quotient topology ([x-03] p. 59), every packet and every
periodic orbit is an indiscrete subspace; X₀ is not T₀; no T₀ subspace meets a packet in two points.
(`s14/qstar-adjudication.md` §3 + §9 item 1: *"none appears in [x-03], [x-06], or the pre-Session-14
program record"*.)

**What I found that the Session-14 referee sweep missed.** The earlier sweep grepped for `Hausdorff`,
`irreducible`, `properly discontinuous`, `non-Hausdorff` (its S-38, S-44). It did **not** grep for
`coarse`. Deninger's own word for "indiscrete" is **coarse**, and he uses it — with a proof.

> **[x-03] printed p. 61, inside the proof of Theorem 9.6** (verified verbatim in a fresh
> `pdftotext -layout` extraction this session, and again in the published
> [z-19] = Indag. Math. **37** (2026) 25–136, printed pp. 81–82):
>
> "we obtain a continuous open and surjective map π : X_η ↠ Y := Q₀^{>0}Ẑ^× / Q₀^{>0}. … **We will
> show below that the only open sets of Y are ∅ and Y.** … **The fact that Y carries the coarse
> topology follows from strong approximation for ℚ:** … For proving that Y carries the coarse
> topology it therefore suffices to show that if U ⊂ Y is open with 1 ∈ U, then U = Y. … Hence every
> a ∈ Ẑ^× is contained in U′ and therefore U′ = Y and U = Y."

So: **Deninger already proves, in print, an indiscreteness theorem for a ℚ^{>0}-quotient occurring
inside the very construction, and proves it by exactly the mechanism the program re-derives as its
own novelty item 2** (`qstar-adjudication.md` §9 item 2, "simultaneous profinite/archimedean
approximation" — Deninger's is strong approximation for ℚ / CRT, the same instrument, the same
conclusion-shape). His Y is the ℚ^{>0}-quotient of Ẑ^×; the program's object is a packet's *subspace*
topology in X₀. Different objects — but "the ℚ^{>0}-quotient here is coarse, by strong approximation"
is printed on the page.

**And the second half of the mechanism is also printed.** [x-03] printed p. 63:

> "**Note that in general the continuous bijection π|_{M×{u}} : M × {u} → π(M × {u}) will not be a
> homeomorphism if π(M × {u}) is equipped with the subspace topology of X.** … In general however the
> partition of X into the disjoint spaces π(M × {u}) for u ∈ ℝ^{>0} mod Q will not be locally
> trivial."

That is precisely the phenomenon the program's Theorem 1 quantifies: the topology X₀ induces on a
piece is strictly coarser than the piece's own topology. Deninger states the phenomenon and declines
to quantify it; the program quantifies it to *indiscrete*.

**Background folklore, for completeness.** The general principle — collapsing the leaves of a
foliation with a dense leaf gives an indiscrete quotient — is standard. Opened this session:
I. Moerdijk, *Models for the Leaf Space of a Foliation*, in *European Congress of Mathematics
(Barcelona 2000)*, Progr. Math. 201, Birkhäuser, p. 1: "Identifying each of the leaves to a single
point yields a very uninformative, **'coarse' quotient space**, and the problem is to define a more
refined quotient M/F."

**What remains genuinely new in C1** (and I found nothing against it): (i) that the *subspace*
topology on a **packet**, and on a **single periodic orbit**, in X₀ is indiscrete; (ii) that X₀ is
**not T₀** (Deninger nowhere discusses separation axioms of X₀ — searched); (iii) the corollary that
no T₀ subspace meets a packet twice, hence face (a) of Q\* is NO.

**Required change (severity MAJOR).** `qstar-adjudication.md` §9 item 1's parenthetical "none appears
in [x-03]" and item 2's claim of a new mechanism must be replaced by: *"the coarse-topology
phenomenon and the strong-approximation mechanism are Deninger's own ([x-03] pp. 61, 63 = [z-19]
pp. 81–82, 84); what is new is their application to the subspace topology of a packet and the
resulting non-T₀ statement for X₀."* Item 2 should be demoted from `novelty` to `credited: [x-03]
p. 61`.

---

## C2 — Theorem T (ℚ^{>0}-suspensions are never T₁; Y₀ not T₁/metrizable). **Verdict: PARTIAL.**

**Statement not located anywhere** in the stated generality ("for any ℚ^{>0}-space Z and any z with
relatively compact orbit, the ℚ^{>0}-orbit of (z, u) in Z × ℝ^{>0} is not closed"), nor its
consequence that Y₀ is not metrizable and not a foliated space.

**But the mechanism is textbook and the closest instance is again Deninger's own.**
1. *Closed-orbit ⇒ separated-quotient* is classical. Opened this session: E. Akin and J. Auslander,
   *Compactifications of Dynamical Systems*, arXiv:1004.0323v1 (2 Apr 2010), proof of Theorem 6.3(b),
   PDF p. 99: "Let E = O(φ ∪ φ^{−1}). By (v) this is a closed equivalence relation and so by
   Proposition 6.2 **the quotient space X/E is Hausdorff.**" The converse direction — orbits not
   closed ⇒ quotient not T₁ — is the elementary half of the same equivalence.
2. Deninger prints the failure for his own action: [x-03] printed p. 47 — "**The ℚ^{>0}-action on
   Ȟ_{E_tors} × ℝ^{>0} is not properly discontinuous.** In section 10, we will see that this works to
   our advantage."; and p. 63 — the non-homeomorphism warning quoted under C1; and p. 61 — the coarse
   topology of a ℚ^{>0}-quotient.
3. Deninger's §8 is explicitly a negative result about Y₀ ([x-03] pp. 49–50): he introduces Y₀ as the
   closure of the periodic orbits precisely in order to show it is **still infinite-dimensional**, so
   the "Y₀ is not the object" conclusion is his.

**Precise difference (what is new).** The *uniform* statement — that **no** ℚ^{>0}-suspension of a
base with a relatively compact orbit is T₁, so no compact base whatever can furnish the S4 object —
and the consequent non-metrizability / non-foliated-space verdict for Y₀. Neither is in [x-03],
[x-06], [z-19], [r3s-08] (all searched this session) nor in anything I could find.

**Required change (severity MINOR).** `s14/y0-witness/adjudication.md` §7 item 1 should cite
[x-03] pp. 47, 61, 63 as the printed antecedents and Akin–Auslander (or Bhatia–Szegő) for the
closed-orbit/separation criterion, and keep the theorem as new.

---

## C3 — The flow-conformal escape weight W and the dissipation theorems. **Verdict: PARTIAL.**

**What I found — the vocabulary the program is missing is "dispersive / parallelizable".** A positive
function W with W∘φ^t = e^t·W is the exponential of a **time function** f = log W satisfying
f(φ^t x) = t + f(x). The existence of such a function is the classical characterization of a
*parallelizable* flow, and parallelizable ⟺ dispersive ⟺ **all limit sets empty** ⟺ no nonempty
compact invariant set. This is a 65-year-old body of theory that the program's notes nowhere cite.

Opened this session — E. Akin and J. Auslander, *Compactifications of Dynamical Systems*,
arXiv:1004.0323v1, §6 (introduction, PDF p. 8; theorem restated as Thm. 6.3, PDF pp. 96–99):

> "**6. Parallelizable Systems: Following Antosiewicz and Dugundji as well as Markus, we characterize
> parallelizable flows.** That is, flows (X, φ) which are isomorphic to the product of a constant flow
> and the translation flow on ℝ."
>
> "**Theorem 0.5** … (b) The following are equivalent: (i) Oφ is closed and there are no periodic
> points … **(iv) Ωφ = ∅** … **(vi) φ is parallelizable.**"
>
> "we will call φ … **parallelizable if there is a homeomorphism from X to ℝ × Y** for some space Y
> which is an isomorphism from φ to the translation τ. The space Y is then called a **section** for φ."

Primary sources named there and reachable by name (not opened; bibliographic data complete):
H. A. Antosiewicz and J. Dugundji, *Parallelizable flows and Lyapunov's second method*, Ann. of Math.
(2) **73** (1961) 543–555; O. Hájek, *Parallelizability revisited*, Proc. Amer. Math. Soc. **27**
(1971) 77–84; N. P. Bhatia and G. P. Szegő, *Stability Theory of Dynamical Systems*, Grundlehren 161,
Springer 1970 (repr. 2002), ch. on dispersive and parallelizable systems; N. P. Bhatia, *Criteria for
dispersive flows*, Math. Nachr. **32** (1966).

**Precise difference (what survives as new).**
* Deninger's X₀ is **not** parallelizable and not dispersive — it has periodic orbits — so the
  classical equivalences do not apply to X₀. The program's W is an **extended-real, lower
  semicontinuous** conformal weight, finite on the generic locus and **= +∞ exactly on the packets**.
  That "partial time function with an ∞-locus that is exactly the recurrent set" is the genuinely new
  device; I found no analogue.
* The two consequences — *no nonempty quasi-compact flow-invariant subset meets the generic locus*
  and *packets are clopen in the periodic locus, so any such set meets finitely many packets* — are
  not in print. The first is the classical "a maximum of W on a compact invariant set is
  impossible" argument, applied to a case where W is only l.s.c. and only partially finite.

**Required change (severity MODERATE).** `qstar-adjudication.md` §9 items 4 and 5 should credit the
dispersive/parallelizable framework (Antosiewicz–Dugundji 1961; Hájek 1971; Bhatia–Szegő 1970) as the
classical setting, and restate the novelty as the l.s.c. extended weight and the packet ∞-locus.
Without that citation a referee in dynamical systems will read item 4 as a rediscovery.

---

## C4 — Backward escape: every generic point of X₀ has empty α-limit set. **Verdict: PARTIAL.**

Same finding as C3, on the limit-set side. "All limit sets empty" is precisely condition (iv) of
Akin–Auslander's Theorem 0.5(b)/6.3(b) quoted above, and is the classical definition of a **dispersive**
flow; the objects, the name, and the equivalences are 60 years old.

**What is new and survives:** (i) the theorem *for X₀*, where the flow is **not** globally dispersive
(the periodic locus is entirely recurrent) but the **generic locus** is, so the statement is a
localization no classical theorem delivers; (ii) the arithmetic instrument that proves it — the chart
criterion "F_{m/n}π(η, Ψ) lies in the first chart ⟺ n | m·|ker(Ψ|_μ)|" read off [x-03] (51)/Lemma 4.6,
with the quantitative bound m/n ≥ 1/e. Nothing like that instrument exists in the dynamics literature,
because it is arithmetic.

**Required change (severity MINOR).** `s14/qa-kill.md` §10 item 9 should say "the flow is dispersive
in the sense of Bhatia–Szegő on the generic locus" and cite the classical framework; the theorem stays.

---

## C5 — DQ-M (leafwise trace of a §7.7 mapping torus; index vs. Haar; no ℤ-valued invariant measure).

| Sub-claim | Verdict |
|---|---|
| **(a)** For every [Den05] §7.7 mapping torus the leafwise trace exists **without any non-degeneracy hypothesis** and equals ℓ Σ_k tr((h\*)^k) δ_{kℓ} | **NOVEL** — nothing located. The program itself flags it "(F) expected folklore"; I extend the earlier sweep's S-34/S-35 with four further searches (log C5-S1…C5-S4) and found no printed statement dropping the non-degeneracy hypothesis. Named residual gap: Álvarez López–Kordyukov's 2002 *examples* section (not on disk, not reachable) — see §UNDETERMINED. |
| **(b)** A continuum B of closed orbits of common length ℓ contributes ℓ·ind(h^k, B)·δ_{kℓ}, **never the Haar mass** | **NOVEL.** The nearest printed neighbors, both opened or identified this session: the **equivariant Fuller index** (C. Wendl-school; arXiv:1301.7304, *Genericity in equivariant dynamical systems and equivariant Fuller index theory* — "an equivariant version of the Fuller index detects group orbits of periodic orbits of the flow, distinguished by their isotropy … locally, Fuller's index is the fixed point index of a Poincaré map for a periodic orbit, multiplied with the inverse 1/k of its multiplicity"), and Zelditch's clean/Bott–Morse Duistermaat–Guillemin formula (prior sweep S-26). Neither states the index-versus-measure dichotomy, and neither is cited by the program. |
| **(c)** No nonzero translation-invariant **ℤ-valued** finitely additive measure on the clopen algebra of an infinite profinite group | **NOVEL (folklore-grade).** The *framework* is completely standard and I opened a source for it: K. Ardakov and S. Wadsley, *Equivariant line bundles with connection on the p-adic upper half plane*, arXiv:2309.05462, §2.1 — M(Z, a) = finitely additive a-valued measures on the clopen algebra of a profinite set Z, with "Proposition 2.1.3 … (a) There is a natural additive isomorphism M(Z, a) → Hom_ℤ(C(Z, ℤ), a)". Within that standard framework the *non-existence under translation invariance* is one line (index divisibility), and I could not find it stated. Report it as an observation, not a theorem with a name. |
| **(d)** Hence a packet-symmetric continuum has index 0 | **NOVEL**, as a consequence of (b)+(c). |

**Required change (severity MINOR).** Add the equivariant-Fuller-index literature and the
M(Z, ℤ)-measure framework as the neighboring print; do not claim the ℤ-valued-measure lemma as more
than an elementary observation.

---

## C7 — cl(γ) = Γ^E_p exactly; the packet as the fiber of a continuous descended projection.
**Verdict: NOVEL for the closure equality; PARTIAL for the fiber/closedness clause.**

* **Source-currency check (new, and it clears).** The program's [r3s-08] is
  `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`. I confirmed this session that the
  arXiv record has **five versions** — v1 (21 Aug 2025), v2 (30 Aug), v3 (4 Sep), v4 (19 Dec 2025),
  v5 (21 Jan 2026) — Comments: *"26 pages. minor change (v2), corrected typos (v3), minor changes and
  corrected misprints (v4); **to appear in Münster Journal of Mathematics**"*. **The on-disk file is
  already v5** (its arXiv stamp line reads `arXiv:2508.15971v5 [math.NT] 21 Jan 2026`) and its
  `pdftotext` output is **line-for-line identical** to a fresh fetch of v5 made this session
  (1,326 lines each, `diff -q` clean). So `B-corA1-adjudication.md` finding N-9 (the (2.2.7)
  non-surjectivity defect, and C_𝔭/Γ_𝔭 being the un-cut fibers) stands against the **current, final,
  accepted** text. No erratum, no correction. *This closes a live risk nobody had checked.*
* **The closure equality cl(γ) = Γ^E_p** — the earlier dual-model sweep already graded the underlying
  Theorem A NOVEL-DUAL-CHECKED (`referee-s14/novelty-adjudication.md`); I add nothing against it,
  and my C1 finding (Deninger's coarse-topology proof, [x-03] p. 61) does not touch it, because
  Deninger's Y is a quotient of the *generic* fiber, not a packet.
* **"The packet is the fiber of the continuous descended projection, hence closed and
  flow-invariant"** — the program's own ledger already grades this "ANTICIPATED in mechanism"
  (pr_{X₀} continuous is [x-03] Lemma 7.1 p. 40; the descended 𝔭𝔯_K is asserted continuous, without
  proof, at [r3s-08] p. 14). I confirm the anchor and add: [r3s-08] v5 uses the word **packet**
  itself (p. 897 of my extraction, "By Theorem 2.2.9 (2), the packet …"), so the *object* is
  Morishita's too; only its closedness is not stated. **PARTIAL**, novelty LOW, exactly as the
  program's own ledger says. No change required.

---

## C8 — The closed embedded n-cube in every closed flow-invariant subset meeting every packet.
**Verdict: NOVEL (the proof); the conclusion is Deninger's own assertion.**

I checked the one thing the earlier sweep left open — *does [x-03] §8 contain a dimension argument?*
It does not. Read verbatim this session, [x-03] printed pp. 49–50:

> "For an integral normal scheme X₀ of finite type over spec ℤ with dim X₀ ≥ 1 the dynamical system
> X₀ = X̌₀(ℂ) ×_{ℚ^{>0}} ℝ^{>0} **is infinite dimensional**, whereas we are searching for a system of
> dimension 2 dim X₀ + 1 … **In this section we will show that the system Y₀ is still
> infinite-dimensional:** Namely, for one-dimensional X₀, flat over spec ℤ and conditionally for all
> X₀ we have Y₀ = X̌₀(S¹) ×_{ℚ^{>0}} ℝ^{>0}. This follows from Theorem 8.2 below …"

and Theorem 8.2 itself is a **density/identification** statement (X̌(ℂ)_per = X̌(S¹)), proved through
Lemma 8.3, a simultaneous-approximation lemma. **There is no covering-dimension argument, no cube, no
dimension-theoretic input anywhere in §8.** Deninger deduces "infinite-dimensional" from the shape of
the identification and leaves it there. So the program's N-2/N-3 self-assessment is correct: the
conclusion is [x-03]'s (pp. 5, 49, and [x-06] p. 12), the **proof** — explicit closed embedded
n-cubes K_n, separation-free, via Lemma K from [x-03] (51), extended to every closed flow-invariant
S meeting every packet with E_fd ⊆ E ⊆ E_max — is not in [x-03], [z-19], [x-06], [r3s-08] or anything
I located. **NOVEL.**

*Housekeeping, verified:* `A-thmB-adjudication.md` §8's action item "fetch a dimension-theory source
before external circulation" is **discharged** — `fetched-r3/` now holds
`r3s-27-hurewicz-wallman-1941-dimension-theory-princeton-SPONSOR-PURCHASE.pdf`,
`r3s-28-engelking-1995-theory-of-dimensions-…` (PDF + OCR text) and
`r3s-25-schultz-2012-notes-topological-dimension-theory-ucr-SESSION14-FETCH.pdf`. The [RU] on
"dim [0,1]ⁿ = n" can be cleared by citation.

---

## C9 — The compact 3-dimensional source realizing {log p}; Theorem C; the p^{1/2}·O return derivative.
**Verdict: PARTIAL — and one printed sentence of Deninger's pre-empts the structural half.**

### C9-a. **The decisive hit: Deninger states the fixed-point requirement in print.**

Christopher Deninger, *Analogies between analysis on foliated spaces and arithmetic geometry*, in
*Groups and Analysis*, LMS Lecture Note Ser. **354**, CUP 2008, pp. 174–190 (on disk as
`fetched/x-18-…`; MSC/zbMATH record Zbl, listed as reference [8] of [ÁLKL23]). **Printed p. 3 of the
preprint text, "Construction 3" and the paragraph immediately following, read verbatim this session:**

> "Let ω_φ be the one-form on X defined by ω_φ|_{TF} = 0 and ⟨ω_φ, Y_φ⟩ = 1. One checks that
> dω_φ = 0 … We may view the cohomology class ψ = [ω_φ] in H¹(X, ℝ) … as a homomorphism
> ψ : π₁^{ab}(X) → ℝ. **Its image Λ ⊂ ℝ is called the group of periods of (X, F, φ^t).**
> **It is known that F is a fibration if and only if rank Λ = 1.** In this case there is an
> ℝ-equivariant fibration X → ℝ/Λ whose fibres are the leaves of F."
>
> "So the foliation setting allows for a product formula where the Nγ are not all powers of the same
> number. **If one wants an infinitely generated Λ, one must allow the flow to have fixed points
> ( ≙ infinite places).** A product formula in this more general setting is given in [Ko]."

and in his Dictionary 4, part 2, the row: "**Number of residue characteristics |char(𝒳)| of 𝒳  ↔
rank of period group Λ of (X, F, φ^t)**".

This is the S4′ constraint, in print, in 2007–2008. Its two consequences for the program:
1. **The "one closed orbit of length log p per prime" spectrum is an infinitely generated period
   group, and Deninger says in print that such a Λ forces the flow to have fixed points.** The
   Session-14 witness has **no** fixed points (ledger §15: "the limit torus has χ = 0; **there are no
   fixed points**") — so Deninger's printed sentence *predicts exactly the gap the adjudication found*
   (unmet half (b): "an archimedean leaf with χ ≠ 0 in that accumulation set"). The program reached
   the right conclusion; it did not know the conclusion was already anticipated.
2. **"F is a fibration if and only if rank Λ = 1"** pre-empts, in mechanism, the y0-witness novelty
   item 2 (*"every §7.7 suspension solenoid has cyclic closed-orbit length group, so the class in
   which S1 is proved can never carry T₁"*). The same statement, for smooth foliated 3-manifolds with
   transverse flow, is **published**: J. Kim, M. Morishita, T. Noda, Y. Terashima, *On 3-dimensional
   foliated dynamical systems and Hilbert type reciprocity law*, **Münster J. Math. 14 (2) (2021)**
   = arXiv:1906.02424 (fetched and read this session), **Proposition 2.2.5**: "If S is of type I or of
   type III-1, then the period group Λ_S = ℤ. Conversely, if the Λ_S has rank one … and M₀ is
   connected, then S is of type I or of type III-1", with their own remark "**Although this may be
   known (cf. [CCI; 9.3], [Fa; 2.1])**, we give a proof … for the sake of readers" — i.e. the authors
   themselves grade it folklore, and point at Candel–Conlon, *Foliations I*, §9.3.

### C9-b. Prior constructions of foliated dynamical systems with prescribed orbit structure

All read this session; **none realizes the spectrum {log p}**, and each has a finitely generated
period group:

| Construction | Period group / spectrum | Source |
|---|---|---|
| Deninger's solenoid for an **elliptic curve over 𝔽_q** — the one case where the object exists | lengths in (log q)·ℤ, rank Λ = 1 | [De02] = `fetched/x-22-…`; named as the sole existing case by Leichtnam, below |
| Leichtnam's class (S = L × ℝ^{+*}/q^ℤ, L locally D × ℤ_p^m) | q^ℤ-suspension; rank 1 | [r3s-21] = arXiv:math/0603576v2, abstract |
| KMNT Example 3.I: mapping torus of a pseudo-Anosov Σ_g-diffeomorphism with the suspension flow | **Λ_S = ℤ**; countably infinitely many closed orbits | arXiv:1906.02424 §3, read this session |
| KMNT Lemma 3.2: replace a solid-torus neighborhood V = D × S¹ of a closed orbit γ by the mapping torus of a **horseshoe**, obtaining "countably infinitely many closed orbits around γ" with ω_S unchanged | Λ unchanged | ibid. |
| KMNT Example 3.II.1/3.II.2: T³-type systems, dense leaves | **Λ_{S₁} = ℤ + ρ(m)ℤ + ρ(l)ℤ**, rank ≤ 3 | ibid. |
| KMNT Examples 3.III-1.1 (Reeb foliation on S³ + horseshoe flow), 3.III-1.2 (open book) | Λ_S = ℤ | ibid. |

The **surgery shape** of the program's witness — insert a controlled flow into a solid-torus
neighborhood of a closed orbit of a flow on a 3-manifold, leaving the rest intact — is therefore
*exactly* KMNT's Lemma 3.2 mechanism, published in Münster J. Math. 14 (2021). What the program does
with it (one **cabled** solid torus per prime, radii O(p^{-2}), accumulating on a 2-torus with an
irrational flow, producing **one simple orbit of length log p per prime and nothing else**) is not
there, and the resulting spectrum is of a kind KMNT's period-group proposition shows cannot occur on
a foliated 3-*manifold* at all.

### C9-c. Verdicts

| Sub-claim | Verdict |
|---|---|
| The compact 3-dimensional source with **exactly** one simple closed orbit of length log p per prime (torus + cabled solid tori) | **NOVEL as a construction** — no realization of {log p} located anywhere. But the surgery technique is KMNT Lemma 3.2 (published), and Deninger [x-18] p. 3 pre-states that such a spectrum cannot live on a foliated object without fixed points. **Credit both.** |
| Its **inert** equivariant map into the E-free Y₀ | **NOVEL** |
| **Theorem C** (any compact source hitting infinitely many packets splits as Y_η ⊔ ⨆_p Y_p clopen, and conversely) | **NOVEL.** Nearest print is KMNT **Theorem 2.2.2 / Corollary 2.2.4**, "a decomposition theorem … which yields a classification of FDS³'s": M cut along the finitely many non-transverse compact leaves decomposes into components each of which is a surface bundle over S¹ or over an interval, or has all leaves dense. **Different hypotheses, different conclusion** (theirs is intrinsic and geometric; the program's is about the fibers of an equivariant map into Y₀ and is purely topological) — but it is the same *kind* of theorem in the same field, it is published, and the program does not cite it. |
| A repelling core of rate ½ gives return derivative p^{1/2}·O and T1 + T2 exactly on the pieces | **ANTICIPATED — this is Deninger's own printed prescription.** The program already records it as such ([Den05] p. 33, "complex conjugate numbers of absolute value Np^{1/2}"; y0-witness §7 item 4 grades it "CONFIRMED-FROM-SOURCE"). No change needed. |

**Required change (severity MAJOR for external circulation).** `s14/y0-witness/adjudication.md` §7
items 1, 2 and 6, and `m2c-feasibility-ledger.md` §15, must cite **[x-18] p. 3** (the period group Λ,
the rank-1 ⟺ fibration statement, and *"if one wants an infinitely generated Λ, one must allow the
flow to have fixed points"*) and **KMNT, Münster J. Math. 14 (2021) = arXiv:1906.02424**
(Prop. 2.2.5, Thm. 2.2.2/Cor. 2.2.4, Lemma 3.2). Without this the note's central structural findings
read as unaware of the two printed sources closest to them.
