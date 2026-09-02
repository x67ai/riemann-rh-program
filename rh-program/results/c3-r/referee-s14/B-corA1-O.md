# REFEREE REPORT — probe B, Corollary A.1: the converse inclusion cl(γ) ⊆ Γ^E_p

**Program:** RH research program, direction C3-r (geometric substrate, reduced recommission).
**Session:** 14. **Date:** 2026-09-02. **Referee:** O (Claude Opus 5), one of two independent
referees on this item under standing order 7. I have not opened referee F's report
(`B-corA1-F.md`), the dedicated adjudication of this item (`B-corA1-adjudication.md`), or the
earlier run of this report (`B-corA1-O.md`, preserved as `B-corA1-O-run1-0809.md`). I *was*
required to read `probe-9.3-adjudication.md` and the note, both of which have been amended in
place with the prior run's outcome — see the disclosure in §0.2, which states exactly what that
cost.
**Note under review:** `results/c3-r/probe-9.3-b.md`, read in full.
**Item:** Corollary A.1 and, specifically, the converse inclusion cl(γ) ⊆ Γ^E_p — adjudication
§4 item 6's outstanding debt, probe B's own Q-c.
**Machine checks:** `results/c3-r/referee-s14/B-corA1-O-rerun-checks.py`,
results in `B-corA1-O-rerun-checks.json` (5/5 pass). They check only the finite arithmetic;
all topology in this report is checked by hand.

---

## 0. Verdict, stated first

### 0.1 Verdict block

| | |
|---|---|
| **VERDICT** | **PASS-WITH-REPAIRS** |
| FATAL | **0** |
| MAJOR | **3** (F1, F2, F3 — all against the note's *argument*, none against its *conclusion*) |
| MINOR | **8** (m1–m6 against the note; N1–N2 are new findings against a cited source, filed at MINOR) |
| Is the converse inclusion TRUE? | **YES.** Established here at referee grade, in a strictly stronger form than the note claims, by a proof independent of the note's. |
| Is the note's *proof* of it adequate? | **NO.** The parenthetical argument is proposition-grade at best; taken literally its stated exclusion criterion would make the conclusion **false** (F2). |

**Headline.** `cl_{X₀}(γ) = Γ^E_{x₀}` is a theorem, with **no "char-p part" hedge, in every chart
of the colimit, and globally in X₀**, for X₀ = Spec Z and in fact for every arithmetic scheme.
It is *not* a statement about limits of characters at all: the packet Γ^E_{x₀} is the **fiber over
the closed point x₀ of a continuous map Π : X₀ → X₀** obtained by descending pr_{X₀} through the
suspension quotient, and a fiber of a continuous map over a closed point is closed. Everything the
note's parenthetical tries to do with subnets and (Tors) is subsumed by that one observation,
which needs no separation axiom, no compactness, no metrizability and no density.
The density input (CRT) is needed only for the **other** inclusion (Theorem A), which was not
under review.

### 0.2 Disclosure required by standing order 5 (this check was NOT blind)

The task mandates reading `results/c3-r/probe-9.3-adjudication.md` and the note in full before
starting. **Both files have already been amended in place with the outcome of a previous run of
this same referee item**, including its verdict, its finding numbering, and the full replacement
text ("Proposition A.1′"):

* `probe-9.3-adjudication.md` §4 carries a block "**[REFEREE PASS 2026-09-02 — Session 14]**"
  stating "That converse is now DISCHARGED at referee grade … two independent referee reports F
  and O, adjudicated PASS-WITH-REPAIRS, 0 FATAL / 2 MAJOR", and naming the mechanism
  ("the fiber over the closed point x₀ of a continuous map X₀ → X₀ descended from pr_{X₀}").
* `probe-9.3-b.md` §5 carries a block reproducing Prop. A.1′ with its proof and a
  finding list.

There is therefore no way to perform this check blind while obeying the reading instruction, and
I do not pretend to have done so. What I have done instead, and what the reader may check line by
line below: **I re-derived every step from the on-disk PDFs**, and the proof I give in §4–§6 is
*not* the one in the note's block — it is shorter, uses strictly fewer hypotheses (no
compactness of Ẑ_{(p)}, no Hausdorffness or metrizability of X•(C), no openness of the G-quotient,
no chart bookkeeping for the ⊆ half), and it generalizes from Spec Z to every arithmetic scheme.
Two of my findings (**N1**, **N2**) are *not* in the note's block, are adverse to the program's
current bookkeeping, and were reached by opening [r3s-08] at pages the note does not cite for
this purpose. Under standing order 7 I state them at full strength and do not soften them in the
expectation that the other referee will find them.

### 0.3 Findings index

| # | Severity | Location | One line |
|---|---|---|---|
| **F1** | MAJOR | note §5, Cor. A.1 parenthetical, clause 1 | The instrument (subnet limits of {F_n(P₀)} upstairs, in one chart, at one prime) does not reach the target (cl in the suspension X₀); three descents are missing, and the third — the Q^{>0}-quotient — provably does **not** reflect convergence. |
| **F2** | MAJOR | same, clause 2 | The stated exclusion criterion ("some component of b equal to 0") is **not** the (Tors) criterion; it is strictly weaker. If it were correct the corollary would be **false**. Counterexample given. |
| **F3** | MAJOR | same, clause 3, and the corollary's headline | "cl(γ) ∩ (char-p part) = Γ^E_p" is, for Spec Z, *logically equivalent to Theorem A* and carries **zero** converse content; yet the corollary's headline ("orbit closure", "smallest closed invariant set", "minimal sets") asserts exactly the converse. |
| m1 | MINOR | "With Step 5's converse inclusion" | Wrong cross-reference: Step 5 is the sweep ⊇ and contains no converse. |
| m2 | MINOR | "(char-p part)" | Undefined in the note; and, once defined from [x-03] p. 33, redundant. |
| m3 | MINOR | "so they leave the space" | Under-specified. The operative fact is `cl_A(S) = cl_X(S) ∩ A`; the excluded limits *do* exist in the un-cut X̌₀(C), where the equality **fails**. |
| m4 | MINOR | "by compactness of Ẑ_{(p)}" | Compactness is not what is used and is not needed; see §4.4. |
| m5 | MINOR | dated block, part (f) | Miscitation: "p. 47: the inductive-limit and subspace topologies agree" is about E vs. un-cut, not about chart vs. colimit. Correct warrant: Prop. 7.4 a) (p. 43). Also the sentence conflates two different "pointwise" topologies. |
| m6 | MINOR | dated block, part (b) | "F_{m/m′}P₀ lies in the chart F_ν^{-1}(X•₀(C)^E) iff m′ \| ν" is **false as stated** (take m′ = p, ν = 1). Needs "m′ prime to p". |
| **N1** | MINOR (priority) | new | The engine of the repair — continuity of Π : X₀ → X₀ — is **already asserted in the literature**: [r3s-08] p. 14 defines **pr**_K : 𝔛_K → X_K and states it is continuous; p. 15 defines C_𝔭 := p̌r_K^{-1}(𝔭) and Γ_𝔭 := C_𝔭 ×_{Q₊} R₊. Closedness of the packet is then one line. Prop. A.1′ must not be recorded as novel. |
| **N2** | MINOR (source defect, new) | new | [r3s-08] (2.2.7) p. 16's surjection "↠" is **false** in his own un-cut setting (Remark 2.1.13 p. 13 omits Deninger's (Tors) refinement): Hom_Gr(F̄_p^×, ℂ^×) ≅ Ẑ_{(p)} while the image is N·Ẑ×_{(p)} ⊊ Ẑ_{(p)}. Hence his C_𝔭 = p̌r_K^{-1}(𝔭) is **strictly larger** than Deninger's C_{x₀}, and Thms 2.2.8(1)/2.2.9(1) hold only after the refinement is restored. Program consequence: the repair may **not** be short-cut by citing [r3s-08] pp. 14–15. This is a *second*, independent defect in the statements already carried as ledger row W11. |

---

## 1. The text under review, quoted exactly

From `results/c3-r/probe-9.3-b.md`, §5, immediately after Theorem A (the original text, which
the note preserves "unchanged for the record"):

> **Corollary A.1 (packets are minimal sets; the "invariant tori" made precise).** Every orbit of
> Γ^E_p is dense in Γ^E_p; Γ^E_p is the orbit closure of each of its points and is the smallest
> closed invariant set containing any one of its orbits. (With Step 5's converse inclusion — every
> limit of {F_n(P₀)}_n along any subnet is P₀^b for some b ∈ Ẑ_{(p)}, by compactness of Ẑ_{(p)} and
> the same pointwise evaluation; limits with some component of b equal to 0 kill a μ_{ℓ^∞} and
> violate (Tors), so they leave the space — one gets cl(γ) ∩ (char-p part) = Γ^E_p exactly.
> Stated proposition-grade; the kill only needs ⊇.)

Three assertions are in play and they must be kept apart:

* **(A1-head)** Γ^E_p is *the orbit closure of each of its points* and *the smallest closed
  invariant set containing any one of its orbits*; packets are *minimal sets*.
* **(A1-par)** the parenthetical *argument* for the converse.
* **(A1-concl)** the parenthetical's stated conclusion, `cl(γ) ∩ (char-p part) = Γ^E_p`.

(A1-head) **requires** the converse inclusion — indeed it requires Γ^E_p to be closed: a minimal
set is by definition a nonempty **closed** invariant set with no proper nonempty closed invariant
subset, and "orbit closure" is a two-sided statement. Theorem A alone gives only that every closed
invariant set meeting the packet contains it. So the note asserts the converse in its headline
and relegates the proof to a parenthetical it itself labels proposition-grade. That is the debt.

---

## 2. Source policy and page conventions

Everything below is read from the on-disk PDFs this session; nothing is recalled. Text was
extracted with `pdftotext -layout` into the session scratchpad and every quotation was re-read
in that extraction; one passage ([r3s-08] p. 14) was additionally read as a rendered page image
because the extraction garbles it.

* **[x-03]** Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, 119 pp.
  `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`.
  **PDF page = printed page** (verified: the printed folio at the foot of each page matches).
* **[x-06]** Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643.
  `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`. PDF page = printed page.
* **[r3s-08]** Morishita, arXiv:2508.15971v5.
  `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`. PDF page = printed page.

Per `results/corpus-routing.md` caveat 14, [r3s-08] on disk is the v5 (21 Jan 2026) the C3 brief
cites; per the same file, [x-03] is cited as v4 (published = Indag. Math. 37 (2026) 25–136).

---

## 3. Brief item (1) and (2): the exact topology on X₀, and whether "pointwise convergence" describes it

I re-derive the topology from [x-03] §§3–7 with the defining sentences quoted verbatim, then
answer item (2) precisely.

### 3.1 The bottom chart X•(C): pointwise convergence, and metrizability

[x-03] §7 opening, printed p. 40, verbatim:

> "We now introduce topologies on our spaces. We only consider integral normal schemes X₀ whose
> function field K₀ is countable. For brevity we call them **arithmetic schemes**. … We begin with
> the affine case X₀ = spec R₀ and write X = spec R. **Viewing X•(C) as a set of multiplicative
> maps P : R → C as in Remark 3.4 we give X•(C) the topology of pointwise convergence. It is the
> subspace topology induced by the Tychonov topology of C^R = ∏_R C on X•(C) via the inclusion
> X•(C) ⊂ C^R, P ↦ (P(r))_{r∈R}. Since R is countable, X•(C) is a metrizable topological space.**"

So on the bottom chart of an **affine** arithmetic scheme the topology is *exactly* pointwise
convergence, and it is metrizable (Prop. 7.6, p. 44, exhibits a G-invariant metric explicitly).
For X₀ = Spec Z the relevant X = Spec Z̄ = Spec(ring of all algebraic integers) is affine, R = Z̄
is countable, so this applies verbatim.

For a **non-affine** arithmetic scheme, p. 41, verbatim:

> "We give X•(C) the topology for which O ⊂ X•(C) is open if and only if O ∩ X′•(C) is open in
> X′•(C) for any X′₀."

i.e. the topology glued from the affine charts, each of which is open in X•(C) (Lemma 7.2, p. 41).
This is irrelevant for Spec Z but matters for the general statement in §6.3.

**Two facts I will use, both from [x-03] p. 40 and p. 42–43:**

* **(T1) Lemma 7.1, p. 40, verbatim.** "For affine arithmetic schemes X₀, the natural map
  pr_X : X•(C) → X, (x, P^×) ↦ x or P ↦ 𝔭 = P^{-1}(0) is continuous." The proof shown there uses
  only that the closed sets of X are {𝔭 ⊃ I}. It is extended on p. 42: "Using Lemma 7.1 one sees
  that pr_X : X•(C) → X and hence also pr_{X₀} : X•₀(C) → X₀ are continuous."
* **(T2) p. 43, verbatim.** "Moreover the projections pr_X : X̌(C) → X and pr_{X₀} : X̌₀(C) → X₀
  are continuous. It suffices to show that pr_X is continuous, i.e. that
  pr_X ∘ (F_ν^{-1}|_{X•(C)}) : X•(C) → X is continuous for each ν ∈ N₀. Since pr_X = pr_X ∘ F_ν,
  this follows from the continuity of pr_X : X•(C) → X which was noted before Lemma 7.3."

(T2) is the single most important sentence in this whole report.

### 3.2 The G-quotient X•₀(C) = X•(C)/G: well behaved, and it *does* reflect convergence

[x-03] p. 42, verbatim: "Let G = Aut_{K₀}(K). We equip X•₀(C) = X•(C)/G with the quotient
topology." Prop. 7.5 (p. 44) gives continuity of the action map X•(C) × G → X•(C); Prop. 7.6
(p. 44) gives a G-invariant metric d; Prop. 7.7 (p. 44) gives, for a compact group of isometries,
the quotient metric

  δ(xG, yG) = min_{σ,τ} d(x^σ, y^τ) = min_σ d(x^σ, y) = min_τ d(x, y^τ),

and states "The metric δ induces the quotient topology. In particular X/G is Hausdorff."
Corollary 7.8 (p. 45) concludes: "The topological space X•₀(C) is metrizable and separable and in
particular Hausdorff." Corollary 7.9 (p. 45) extends Hausdorffness to X•(C), X•₀(C), X̌(C), X̌₀(C)
for X₀ carrying an ample invertible sheaf — Spec Z is affine, so this covers it.

**Consequence used below.** Because G is a *compact* group acting by isometries, this quotient is
tame: π is open (p. 43: "The projections … are continuous and since G acts by homeomorphisms,
also open"), π is closed (compact orbits), and π(P_n) → π(P) **implies** the existence of σ_n ∈ G
with P_n^{σ_n} → P (read off Prop. 7.7's proof: δ(x_nG, xG) → 0 means d(x_n^{σ_n}, x) → 0).
So the first descent in the note's argument is harmless. The third is not.

### 3.3 The colimit X̌(C) = colim_{N₀} X•(C): the charts are open **and closed**

[x-03] p. 43, verbatim:

> "We give X̌(C) = colim_{N₀} X•(C) the inductive limit topology. It is the finest topology such
> that for all ν ∈ N₀ the inclusions F_ν^{-1}|_{X•(C)} : X•(C) ↪ X̌(C) are continuous. **Thus
> Z ⊂ X̌(C) is closed, resp. open if and only if F_ν(Z) ∩ X•(C) is closed, resp. open in X•(C) for
> all ν ∈ N₀.**"

and Proposition 7.4, p. 43, verbatim: "a) **X•(C) is a closed and open subspace of X̌(C).**
b) F_q : X̌(C) → X̌(C) is a homeomorphism for every q ∈ Q^{>0}₀. c) The group G acts by
homeomorphisms on X̌(C)." (Lemma 7.3, p. 42: F_ν is "continuous, closed and open"; and (51)
p. 42: F_ν(X•(C)) = {P ∈ X•(C) : P(μ_ν(K)) = 1}.)

Three consequences, all re-derived here:

* **(C1) Each chart U_ν := F_ν^{-1}(X•(C)) is an open subspace of X̌(C), and F_ν : U_ν → X•(C) is a
  homeomorphism.** (7.4 a) for ν = 1, then 7.4 b).) Hence *the topology of X̌(C) restricted to a
  chart is exactly the pointwise-convergence topology transported by F_ν*. There is **no**
  refinement inside a chart.
* **(C2) The charts are directed by divisibility and cover X̌(C); each is open; therefore a net
  z_k → z in X̌(C) is eventually contained in a single chart** (pick ν with z ∈ U_ν; U_ν is an open
  neighbourhood of z) **and converges there in the pointwise topology.** So convergence in X̌(C)
  is exactly "eventually in some chart, and pointwise there".
* **(C3) Closure is chartwise.** For an open cover {U_ν}, cl(S) ∩ U_ν = cl_{U_ν}(S ∩ U_ν) and
  cl(S) = ⋃_ν cl_{U_ν}(S ∩ U_ν).

**Answer to the second half of brief item (2).** The colimit topology *is* strictly finer than the
"global pointwise" topology one might put on X̌(C) using Corollary 3.8's description
(X̌(C) = {(x, P̌^×) : P̌^× a continuous character of lim_{←N₀} κ(x)^×}, p. 26): a net can converge
pointwise on lim_← κ(x)^× while wandering across infinitely many charts, and such a net does not
converge in X̌(C). But this refinement lives **between** charts only; *inside* any one chart the
two agree by (C1). Hence a subnet-limit computation performed inside one chart is legitimate as
far as it goes — and that is exactly as far as it goes. (This corrects the phrasing of the note's
dated block, part (f); see m5.)

### 3.4 The E-subspaces

[x-03] p. 47, verbatim:

> "Given an admissible class E as in Definition 4.1 we equip X•(C)_E and X•₀(C)_E with the subspace
> topologies of X•(C) and X•₀(C). Equip X•(C)_E/G with the quotient topology. … We give
> X̌(C)_E = colim_{N₀} X•(C)_E and X̌₀(C)_E = colim_{N₀} X•₀(C)_E the inductive limit topologies.
> **They agree with the subspace topologies via X̌(C)_E ⊂ X̌(C) and X̌₀(C)_E ⊂ X̌₀(C)** because the
> subspaces F_ν^{-1}X•(C) and F_ν^{-1}X•₀(C) are open in X̌(C) resp. X̌₀(C) for all ν ∈ N₀. As above,
> the natural continuous bijection X̌(C)_E/G → X̌₀(C)_E is a homeomorphism. **All preceding results
> in this section remain true if we replace X•(C) etc. by X•(C)_E etc.**"

So: E-spaces carry subspace topologies, everything in §7 transfers, and — the point that does the
work in §6.2 below — **closure in a subspace is the ambient closure intersected with the
subspace**. That, and not "leaving the space", is the correct rendering of the note's third clause.

### 3.5 The suspension X₀: is it the quotient topology?

[x-03] §6, p. 38, defines X₀ = X̌₀(C)_E ×_{Q^{>0}₀} R^{>0} as **a set**: "It is the quotient of
X̌₀(C)_E × R^{>0} by the right Q^{>0}₀-action given by (P₀,u)q = (P₀q, q^{-1}u) = (F_q(P₀), q^{-1}u)".
§6 precedes §7 and declares no topology. The topology is nevertheless pinned by three on-disk
warrants, the first of them Deninger's own:

1. **[x-03] §10, p. 63, verbatim.** For "π : X̃ = M × R^{>0} → X = M ×_Q R^{>0}", Deninger writes
   > "Consider the following subsheaf R_X of C⁰_X:  R_X = (π_*R_X̃)^Q ⊂ (π_*C⁰_X̃)^Q = **C⁰_X**."
   The displayed identity (π_*C⁰_X̃)^Q = C⁰_X says: *Q-invariant continuous real functions on
   π^{-1}(U) are precisely the continuous functions on U*. That is the universal property of the
   quotient topology, for every open U. Theorem 10.2 (p. 64) applies this with M = X̌₀(C), i.e. to
   X₀ itself. This is decisive.
2. **[x-06] p. 11, verbatim.** "Set X₀ = (X̌₀(C) × R^{>0})/Q^{>0} where Q^{>0} acts diagonally."
3. **[r3s-08] p. 14, verbatim** (read as a page image; the text layer garbles it):
   "We equip 𝔛_K twith he quotient topology of the product X̌_K(ℂ) × ℝ₊." (the transposition
   "twith he" is in the source).

I therefore take X₀ to carry the quotient topology, with q : X̌₀(C)^E × R^{>0} → X₀ the quotient
map. **This is load-bearing** — a strictly coarser topology on X₀ would void the continuity of Π
in §4 — and the note's original §3.1 justified it only as "implicit throughout §§8, 10". Warrant 1
above is the fix and is now in the note's dated block; I confirm it independently.

### 3.6 What q does and does not do — the crux of F1

* **q is open.** Q^{>0}₀ acts by homeomorphisms (F_q is a homeomorphism of X̌₀(C)^E by Prop. 7.4 b)
  + p. 47; u ↦ q^{-1}u is a homeomorphism of R^{>0}), so for open U,
  q^{-1}(q(U)) = ⋃_{q∈Q^{>0}₀} U·q is open. ✔
* **q is continuous and surjective.** ✔ (definition of the quotient topology)
* **q is NOT proper, and the action is NOT properly discontinuous.** [x-03] p. 49, verbatim, at the
  end of §7: "**The Q^{>0}-action on Ȟ_{E_tors} × R^{>0} is not properly discontinuous.** In
  section 10, we will see that this works to our advantage." And p. 63: "If Q acts properly
  discontinuously on M × R^{>0} and if M is a manifold, then F is an actual 1-codimensional
  foliation. **In general however the partition of X into the disjoint spaces π(M × {u}) for
  u ∈ R^{>0} mod Q will not be locally trivial**"; and "**Note that in general the continuous
  bijection π|_{M×{u}} : M × {u} → π(M × {u}) will not be a homeomorphism** if π(M × {u}) is
  equipped with the subspace topology of X."
* **Therefore q does NOT reflect convergence.** A net z_k → z in X₀ need admit *no* lift
  z̃_k → z̃ in X̌₀(C)^E × R^{>0}. Concretely, X₀ is non-Hausdorff along the packets (probe B's
  Cor. A.2, adjudicated 2026-08-26 in `probe-9.3-adjudication.md` §3), so one and the same net has
  two distinct limits downstairs while upstairs it has at most one in any given chart. **This is
  precisely why "compute all subnet limits of {F_n(P₀)} upstairs" cannot, by itself, be an
  argument about cl_{X₀}(γ).**
* **But q DOES transport closures**, because it is open. For any continuous open map f and any A
  in the target, `f^{-1}(cl A) = cl(f^{-1}A)`.
  *Proof.* ⊇: f^{-1}(cl A) is closed and contains f^{-1}A. ⊆: let y ∈ f^{-1}(cl A) and U ∋ y open;
  f(U) is open and contains f(y) ∈ cl A, so f(U) ∩ A ∋ a = f(u) for some u ∈ U, whence
  u ∈ U ∩ f^{-1}A ≠ ∅; so y ∈ cl(f^{-1}A). ∎
  Applied to q and A = γ, with q^{-1}(γ) = O(P₀) × R^{>0} where O(P₀) = {F_r P₀ : r ∈ Q^{>0}₀}:
  **cl_{X₀}(γ) = q( cl_{X̌₀(C)^E}(O(P₀)) × R^{>0} )** (using cl(A × B) = cl A × cl B and
  q(q^{-1}S) = S for surjective q). This is the *legitimate* upstairs route, and it is available;
  it is simply absent from the note's parenthetical.

**Answer to brief item (2), in one sentence.** "Pointwise convergence of characters" is an exact
description of the topology of the bottom chart X•(C) and, transported by F_ν, of every chart of
the colimit — but it is *not* a description of the topology of X̌(C) (which is strictly finer
between charts), and it is *not in any sense* a description of the topology of X₀, whose defining
quotient map is open but neither proper nor convergence-reflecting; consequently a limit computed
pointwise upstairs is a *sufficient* producer of limits downstairs (continuity) and never a
*necessary* one, and no enumeration of upstairs limits bounds cl_{X₀}(γ) from above without an
extra argument.

---

## 4. The converse inclusion, re-derived: the packet is a fiber of a continuous map

This section is self-contained: a reader who has not seen the note can check it from the quoted
source sentences alone.

### 4.1 The two set-theoretic inputs, verified verbatim

**(S1) [x-03] p. 27, verbatim.**
> "We will need the map  pr_X : X•(C)_E → X, (x, P^×) ↦ x  (30)  and the induced map
> pr_{X₀} : X•₀(C)_E → X₀  (31). … Both pr_X and pr_{X₀} are N₀-equivariant **if we let N₀ act
> trivially on X₀ and X**. Note that the maps pr_X and pr_{X₀} above extend Q^{>0}₀-equivariantly
> to maps  pr_X : X̌(C)_E → X and pr_{X₀} : X̌₀(C)_E → X₀. Here we let Q^{>0}₀ act trivially on X
> and X₀."

Two things are asserted there and I use both: (i) the maps exist on the colimit; (ii)
**pr_{X₀} ∘ F_q = pr_{X₀} for every q ∈ Q^{>0}₀** (equivariance with trivial target action).

**(S2) [x-03] p. 31, verbatim.**
> "The fibres of pr_{X₀} : X̌₀(C)_{Etors} → X₀ are Q^{>0}₀-invariant. We will now analyze the
> structures of the **Q^{>0}₀-sets C_{x₀} = pr_{X₀}^{-1}(x₀) in X̌₀(C)_{Etors}** for points x₀ of X₀
> whose residue field κ(x₀) is finite."

and, on the same page, the *construction* of the same object:
> "The fibre pr₀^{-1}(x₀) in X•₀(C)_{Etors} is N₀-invariant. Its extension to a Q^{>0}₀-invariant
> subset of X̌₀(C)_{Etors} is the set
> C_{x₀} = pr₀^{-1}(x₀)Q^{>0}₀ = ⋃_{ν∈N₀} F_ν^{-1} pr₀^{-1}(x₀) ⊂ X̌₀(C)_{Etors}."

**Lemma O.0 (the two displays agree).** In X̌₀(C)_{Etors},
`⋃_{ν∈N₀} F_ν^{-1} pr₀^{-1}(x₀) = pr_{X₀}^{-1}(x₀)`.
*Proof.* ⊆: for Q̌ = F_ν^{-1}(P₀) with pr₀(P₀) = x₀ we get pr_{X₀}(Q̌) = pr_{X₀}(F_ν Q̌) = pr₀(P₀) = x₀
by (S1)(ii). ⊇: every Q̌ ∈ X̌₀(C)_{Etors} is F_ν^{-1}(P₀) for some ν ∈ N₀ and P₀ ∈ X•₀(C)_{Etors}
(definition of the colimit, [x-03] p. 43), and then pr₀(P₀) = pr_{X₀}(Q̌) = x₀. ∎

So Deninger's own notation already says it: **C_{x₀} is a full fiber of pr_{X₀}.** No new
mathematics is needed to see this; what is new (and what the note's parenthetical never does) is
to *use* it topologically.

**(S3) [x-03] §6, p. 38, verbatim.** "For a point x₀ of X₀ with finite residue field of
characteristic p set  Γ_{x₀} = C_{x₀} ×_{Q^{>0}₀} R^{>0} ⊂ X₀. … We set Γ^E_{x₀} = C^E_{x₀} ×_{Q^{>0}₀} R^{>0}
where C^E_{x₀} = C_{x₀} ∩ X̌₀(C)_E. If e.g. E_f ⊂ E then Γ^E_{x₀} = Γ_{x₀}."

**(S4) [x-03] Def. 4.1, p. 27, verbatim.** "A class E of characters χ : κ^× → C^× on algebraically
closed fields κ is (N₀−)admissible if for any σ ∈ Autκ resp. ν ∈ N₀ the character χ is in E if and
only if χ ∘ σ resp. χ^ν = χ ∘ ( )^ν is in E. **Moreover the characters in E should satisfy (Tors).**"
Hence **E ⊆ E_tors** for every admissible E, so X̌₀(C)^E ⊆ X̌₀(C)_{Etors} and, by (S2) + Lemma O.0,

  **C^E_{x₀} = pr_{X₀}^{-1}(x₀) ∩ X̌₀(C)^E**, the fiber computed inside the E-space.  (★)

### 4.2 Proposition O.1 (packets are closed and flow-invariant)

> **Proposition O.1.** Let X₀ be an arithmetic scheme ([x-03] §7 p. 40: integral, normal, countable
> function field), C an algebraically closed field satisfying the conditions preceding Cor. 4.4
> (p. 28), E an admissible class (Def. 4.1, p. 27), N₀ ⊆ N as in [x-03] §4, and x₀ a point of X₀
> whose residue field κ(x₀) is **finite**. Give X₀ = X̌₀(C)^E ×_{Q^{>0}₀} R^{>0} the quotient
> topology (§3.5). Then:
>
> 1. the assignment Π[P₀, u] := pr_{X₀}(P₀) is a **well-defined continuous** map Π : X₀ → X₀ into
>    the Zariski space of the scheme X₀;
> 2. Π ∘ φ^t = Π for all t, so every fiber of Π is flow-invariant;
> 3. **Γ^E_{x₀} = Π^{-1}(x₀)**;
> 4. {x₀} is closed in X₀;
> 5. hence **Γ^E_{x₀} is a closed, flow-invariant subset of X₀**, and consequently
>    **cl_{X₀}(γ) ⊆ Γ^E_{x₀}** for every subset γ ⊆ Γ^E_{x₀}, in particular for every periodic orbit.

*Proof.*

**(1)** The composite X̌₀(C)^E × R^{>0} --pr₁--> X̌₀(C)^E --pr_{X₀}--> X₀ is continuous: pr₁ is a
product projection, and pr_{X₀} is continuous on X̌₀(C) by (T2) ([x-03] p. 43) hence on the
subspace X̌₀(C)^E (restriction of a continuous map to a subspace; alternatively p. 47's blanket
"All preceding results in this section remain true … by X•(C)_E etc."). It is constant on
Q^{>0}₀-orbits: (P₀, u)q = (F_q P₀, q^{-1}u) and pr_{X₀}(F_q P₀) = pr_{X₀}(P₀) by (S1)(ii).
By the universal property of the quotient topology — the very identity (π_*C⁰_X̃)^Q = C⁰_X quoted
at [x-03] p. 63 — the map descends to a continuous Π on X₀ = (X̌₀(C)^E × R^{>0})/Q^{>0}₀. ∎(1)

**(2)** φ^t[P₀, u] = [P₀, u e^t] ([x-03] p. 38), and Π[P₀, ue^t] = pr_{X₀}(P₀) = Π[P₀, u]. ∎(2)

**(3)** Let q be the quotient map. C^E_{x₀} is Q^{>0}₀-stable ((S2): "The fibres of pr_{X₀} … are
Q^{>0}₀-invariant"; and X̌₀(C)^E is Q^{>0}₀-invariant by Prop. 4.2, p. 27). Hence
q^{-1}(Γ^E_{x₀}) = C^E_{x₀} × R^{>0}. On the other hand
q^{-1}(Π^{-1}(x₀)) = (pr_{X₀} ∘ pr₁)^{-1}(x₀) = (pr_{X₀}^{-1}(x₀) ∩ X̌₀(C)^E) × R^{>0}
= C^E_{x₀} × R^{>0} by (★). Two saturated sets with the same q-preimage are equal. ∎(3)

**(4)** Let Spec A ⊆ X₀ be an affine open containing x₀, and let 𝔭 ⊂ A be the corresponding prime.
Then A/𝔭 is an integral domain contained in its own fraction field κ(x₀), which is **finite**;
so A/𝔭 is a finite integral domain, hence a field; so 𝔭 is maximal and {x₀} is closed in Spec A.
Now let y ∈ cl_{X₀}{x₀} and pick any affine open V ∋ y. Then V is an open neighbourhood of y, so
V ∩ {x₀} ≠ ∅, i.e. x₀ ∈ V; the previous sentence applied to V gives cl_V{x₀} = {x₀}, and
y ∈ cl_{X₀}{x₀} ∩ V = cl_V{x₀} = {x₀}. Hence y = x₀. ∎(4)
(For X₀ = Spec Z: the points with finite residue field are exactly the (p), and the generic point
(0) is not among them.)

**(5)** Immediate from (1), (3), (4): Π^{-1}(x₀) is the preimage of a closed set under a continuous
map. Flow-invariance is (2). ∎

**What Proposition O.1 does *not* use.** No Hausdorffness, no metrizability, no separation axiom
on X₀ at all (X₀ is in fact non-Hausdorff, adjudication §3); no compactness of anything; no
countability of R; no density; no properness or proper discontinuity of the Q^{>0}₀-action; no
openness of q; no chart bookkeeping; no Theorem A. It holds for **every** arithmetic scheme, every
admissible E, every N₀, and every point with finite residue field — in particular also when the
packet is empty or is a single orbit.

### 4.3 Why this is the right instrument, and the note's is not

The converse inclusion is not a statement about which characters arise as limits. It is the
statement that the packet is **saturated for a continuous invariant** — namely the residue-field
characteristic-and-prime datum pr_{X₀} — and that this invariant separates x₀ from everything else
in X₀ because {x₀} is closed. Once phrased that way the proof is four lines and every hypothesis
is visible. The note's parenthetical instead attempts a *limit enumeration*, which requires
(i) knowing all subnet limits upstairs, (ii) knowing that upstairs limits exhaust downstairs
limits (**false**, §3.6), and (iii) a correct (Tors) criterion (**wrong as stated**, §5.2).

### 4.4 On "compactness of Ẑ_{(p)}" (finding m4)

The note attributes the enumeration of upstairs limits to "compactness of Ẑ_{(p)}". Compactness is
neither used nor needed. What is true and what I use in §5 is the *identification of the whole
upstairs fiber*:

> **Lemma O.1′.** Let x ∈ X lie over x₀ with κ(x₀) finite of characteristic p, so κ(x) = F̄_p and
> κ(x)^× ≅ μ^{(p)} ([x-03] (32), p. 31). Let C be algebraically closed with char C ∈ {0, p}. Then
> the map β : Ẑ_{(p)} → X•(C), b ↦ (x, χ_x ∘ ( )^b), is a **bijection onto pr_X^{-1}(x)** and is
> continuous.

*Proof.* End(μ^{(p)}) = ∏_{ℓ≠p} End(μ_{ℓ^∞}) = ∏_{ℓ≠p} End(Q_ℓ/Z_ℓ) = ∏_{ℓ≠p} Z_ℓ = Ẑ_{(p)}
— this is [x-03] (34), p. 32, verbatim: "The group of automorphisms of the abelian group κ(x)^×
is given by Ẑ×_{(p)} where Ẑ_{(p)} = ∏_{l≠p} Z_l", of which the endomorphism statement is the
unit-free version. Every homomorphism μ^{(p)} → C^× has image in μ(C) (a torsion group maps to
torsion elements), and for each ℓ ≠ p, μ_{ℓ^∞}(C) ≅ Q_ℓ/Z_ℓ because C is algebraically closed of
characteristic ≠ ℓ; hence Hom(μ^{(p)}, C^×) = ∏_{ℓ≠p} Hom(Q_ℓ/Z_ℓ, Q_ℓ/Z_ℓ) = Ẑ_{(p)}, and
composing with the injective reference character χ_x ([x-03] p. 32: "we obtain the injective
character χ_x = ι ∘ i_x^{-1} : κ(x)^× ↪ C^×") realizes this as b ↦ χ_x ∘ ( )^b. Since
pr_X^{-1}(x) = {(x, P^×) : P^× ∈ Hom(κ(x)^×, C^×)} — [x-03] p. 27, verbatim: "X•(C) consists of
pairs (x, P^×) where x ∈ X and P^× : κ(x)^× → C^× is a character" — β is onto pr_X^{-1}(x);
injectivity is immediate from injectivity of χ_x and End(μ^{(p)}) = Ẑ_{(p)}.
Continuity: in the pointwise topology it suffices that b ↦ β(b)(r) is continuous for each r ∈ R.
If r ∈ 𝔭_x the value is 0, constant. Otherwise r̄ ∈ κ(x)^× has finite order m prime to p, so
β(b)(r) = χ_x(r̄^b) depends only on b mod m: **locally constant**. ∎

Note the mechanism: continuity of β is *local constancy*, not compactness. Compactness of Ẑ_{(p)}
would give closedness of the image only after Hausdorffness of X•(C) is invoked; **Lemma O.1′
gives closedness for free**, because pr_X^{-1}(x) is the preimage of the closed point x under the
continuous pr_X (Lemma 7.1, p. 40; §4.2(4) shows x is closed in X by the same argument as for x₀,
since R/𝔭_x is a domain integral over the finite field A/𝔭₀, hence a field).

---

## 5. The exact closure, computed upstairs — an independent second proof, and the (Tors) audit

Proposition O.1 settles the converse inclusion. I now compute the closure *upstairs* as well, for
three reasons: it re-proves Theorem A as a by-product; it yields the **chart-level** statement the
brief's item (5) asks for; and it is the only place where the note's actual argument can be
repaired rather than replaced, so it is where findings F1 and F2 must be adjudicated.

Throughout §5: **X₀ = Spec Z**, C algebraically closed with char C = 0 (e.g. C = ℂ), **N₀ = N**
([x-03] §8 p. 49: "In this section C denotes the complex number field, and we take N₀ = N"),
E admissible, p a prime, x₀ = (p), x ∈ X = Spec Z̄ a point over x₀ (so κ(x) = F̄_p, [x-03] p. 31),
χ = χ_x the injective reference character (p. 32), a₀ ∈ Ẑ×_{(p)} with χ^{a₀} ∈ E, and

  P₀ := π(x, χ^{a₀}) ∈ X•₀(C)^E,  γ := {[P₀, w] : w ∈ R^{>0}} ⊂ Γ^E_p,
  S̃ := {(x, χ^{a₀ n}) : n ∈ N} ⊂ X•(C),  S := π(S̃) = {F_n P₀ : n ∈ N} ⊂ X•₀(C)^E,
  O(P₀) := {F_r P₀ : r ∈ Q^{>0}} ⊂ X̌₀(C)^E   (so q^{-1}(γ) = O(P₀) × R^{>0}).

### 5.1 Step 1 — the upstairs closure at the fixed prime

> **Lemma O.2.** cl_{X•(C)}(S̃) = pr_X^{-1}(x) = β(Ẑ_{(p)}).

*Proof.* **⊆.** x is a closed point of X (§4.4), pr_X is continuous ([x-03] Lemma 7.1, p. 40),
so pr_X^{-1}(x) is closed; and S̃ ⊆ pr_X^{-1}(x). **⊇.** N is dense in Ẑ_{(p)} = lim_{(M,p)=1} Z/M:
for every M prime to p and every residue class there is a positive integer in it (machine check
`crt_density_N_in_Zhat_p`). Since a₀ is a unit, a₀N is dense in Ẑ_{(p)}. β is continuous
(Lemma O.1′), so β(Ẑ_{(p)}) = β(cl(a₀N)) ⊆ cl(β(a₀N)) = cl(S̃). With Lemma O.1′'s surjectivity,
β(Ẑ_{(p)}) = pr_X^{-1}(x). ∎

**No compactness, no Hausdorffness, no metrizability.** (Compare the note's dated block (d), which
routes through "a homeomorphism onto a compact K" and hence silently through Cor. 7.8/7.9.)

### 5.2 Step 2 — the (Tors) audit: exactly which b survive (finding F2)

For b ∈ Ẑ_{(p)} write v_ℓ := v_ℓ(b_ℓ) ∈ {0,1,2,…,∞} (with v_ℓ = ∞ iff b_ℓ = 0). Then

  ker(( )^b : μ^{(p)} → μ^{(p)}) = ⊕_{ℓ≠p} μ_{ℓ^{v_ℓ}},  and  ker(χ^b) = ker(( )^b)

because χ is injective. Condition (Tors) ([x-03] p. 27, verbatim: "**(Tors)** the group
ker(χ)_tors = ker(χ|_{μ(κ)}) is finite and |(ker χ)_tors| ∈ N₀") reads, since κ(x)^× = μ^{(p)} is
itself torsion, simply "ker(χ^b) is finite of order in N₀". Therefore

> **(Tors) holds for χ^b  ⟺  v_ℓ < ∞ for every ℓ ≠ p **and** v_ℓ = 0 for all but finitely many ℓ
> ⟺ b ∈ N·Ẑ×_{(p)}.**

(If b = n·u with n ∈ N, u ∈ Ẑ×_{(p)}, then v_ℓ = v_ℓ(n), so the kernel has order = the prime-to-p
part of n ∈ N₀. Conversely if all v_ℓ < ∞ and almost all vanish, put n := ∏_ℓ ℓ^{v_ℓ} ∈ N; then
b/n ∈ Ẑ×_{(p)}.) This matches [x-03] (35) p. 32 exactly, which is a **surjection**
Ẑ×_{(p)} × N₀ ↠ S onto "the set S of homomorphisms P^× : κ(x)^× → C^× with finite cyclic kernel of
order in N₀", (a,ν) ↦ χ_x ∘ ( )^a ∘ ( )^ν — i.e. onto the exponents N₀·Ẑ×_{(p)}.

**The note's criterion is strictly weaker, and would falsify the corollary.** The note excludes
only "limits with some component of b equal to 0". Take

  **b := (ℓ)_{ℓ≠p} ∈ Ẑ_{(p)}**  (the element whose ℓ-component is the integer ℓ).

Every component of b is **nonzero**, so the note's criterion does not exclude it; but
v_ℓ(b) = 1 for *every* ℓ ≠ p, so ker(χ^b) = ⊕_{ℓ≠p} μ_ℓ is **infinite** and (Tors) fails. Hence
(x, χ^b) is a point of Deninger's un-cut X•(C) that is **not** in X•(C)_{Etors} and **not** a
packet point. If the note's criterion were the operative one, cl(γ) ∩ (char-p part) would contain
the images of all such b and would **strictly contain** Γ^E_p, so the asserted equality would be
false. The conclusion survives only because the true criterion is the larger exclusion.
(Machine check `tors_criterion_counterexample` exhibits exactly this one disagreement.)

Severity: **MAJOR**. The note's own argument, read literally, refutes the note's own conclusion.

### 5.3 Step 3 — descent to X•₀(C)^E

> **Lemma O.3.** cl_{X•₀(C)}(S) = pr₀^{-1}(x₀), the **full** fiber in the un-cut X•₀(C); and
> cl_{X•₀(C)^E}(S) = pr₀^{-1}(x₀) ∩ X•₀(C)^E.

*Proof.* π : X•(C) → X•₀(C) is continuous, so π(cl S̃) ⊆ cl(π S̃) = cl(S); by Lemma O.2,
π(pr_X^{-1}(x)) ⊆ cl(S). All points of X over x₀ are G-conjugate ([x-03] p. 32, verbatim: "Any
point y in X over x₀ is conjugate to our chosen point x by an element of G"), so
π(pr_X^{-1}(x)) = pr₀^{-1}(x₀). Conversely pr₀ is continuous ([x-03] p. 42) and {x₀} is closed
(§4.2(4)), so pr₀^{-1}(x₀) is closed and contains S; hence cl(S) ⊆ pr₀^{-1}(x₀). Equality.
The second claim is the subspace-closure identity cl_A(S) = cl_X(S) ∩ A for S ⊆ A ⊆ X. ∎

Two remarks. (i) This uses neither openness nor closedness of π, and in particular not the
compact-group argument of the note's dated block (c). (ii) It exhibits the (Tors) cut doing its
work exactly where §3.4 says it should: the excluded characters are *present* in cl_{X•₀(C)}(S) and
are removed by intersecting with the E-space — **not** by "leaving the space" in any dynamical
sense (finding m3).

### 5.4 Step 4 — the chart decomposition, and the closure in the colimit

> **Lemma O.4.** O(P₀) ∩ X•₀(C)^E = S; more generally, for every ν ∈ N₀,
> O(P₀) ∩ F_ν^{-1}(X•₀(C)^E) = F_ν^{-1}(S). Consequently
> **cl_{X̌₀(C)^E}(O(P₀)) = ⋃_{ν∈N₀} F_ν^{-1}( pr₀^{-1}(x₀) ∩ X•₀(C)^E ) = C^E_{x₀}.**

*Proof.* Fix r = m/m′ ∈ Q^{>0} in lowest terms. By (51) ([x-03] p. 42, verbatim:
"F_ν(X•(C)) = {P ∈ X•(C) | P(μ_ν(K)) = 1}"), F_r P₀ ∈ X•₀(C) iff F_m(x, χ^{a₀}) ∈ F_{m′}(X•(C)),
i.e. iff χ^{a₀m}|_{μ_{m′}(K)} = 1. Split m′ = p^j m″ with p ∤ m″. On μ_{p^j}(K) the map P is
identically 1 (p-power roots of unity reduce to 1 in characteristic p), so that factor imposes
nothing; on μ_{m″}(K) ≅ μ_{m″}(κ(x)) the condition is μ_{m″}^{a₀ m} = 1, i.e. m″ | m since a₀ is a
unit — and gcd(m, m′) = 1 forces m″ = 1. So **the denominator can only be a power of p**, and then
F_{m/p^j}P₀ = F_m F_{p^{-j}} P₀ = F_m P₀ because F_p P₀ = P₀ (isotropy exactly N x₀^Z = p^Z, [x-03]
Thm. 5.2, p. 34; equivalently Frobenius lies in the image of G_x → Gal(κ(x)/κ(x₀)), (34), p. 32).
Hence O(P₀) ∩ X•₀(C) = S, and intersecting with the Q^{>0}-invariant E-locus (Prop. 4.2, p. 27)
gives the first claim. The general ν follows by applying F_ν, a bijection with F_ν(O(P₀)) = O(P₀).

For the closure: the charts U_ν = F_ν^{-1}(X•₀(C)^E) are **open** in X̌₀(C)^E (Prop. 7.4 a) + p. 47)
and cover it, so cl(O(P₀)) = ⋃_ν cl_{U_ν}(O(P₀) ∩ U_ν) (§3.3 (C3)); F_ν : U_ν → X•₀(C)^E is a
homeomorphism (Prop. 7.4 b) + p. 47), so cl_{U_ν}(F_ν^{-1}S) = F_ν^{-1}(cl_{X•₀(C)^E}(S)); apply
Lemma O.3 and Lemma O.0 with (★). ∎

**This is the chart-level answer to brief item (5): the equality holds verbatim in every chart**,
in the form cl_{X•₀(C)^E}(S) = pr₀^{-1}(x₀) ∩ X•₀(C)^E, and the closure in the colimit is the union
of the chart closures — no cross-chart phenomenon occurs, precisely because the charts are open
(§3.3 (C2)–(C3)).

### 5.5 Step 5 — down to the suspension: both inclusions at once

By §3.6 (q open ⟹ q^{-1}(cl A) = cl(q^{-1}A)) and cl(A × B) = cl A × cl B:

  cl_{X₀}(γ) = q( cl_{X̌₀(C)^E}(O(P₀)) × R^{>0} ) = q( C^E_{x₀} × R^{>0} ) = **Γ^E_{x₀}**.

That is the full equality, obtained upstairs, without invoking Proposition O.1. It agrees with
Proposition O.1 + Theorem A, which is the required cross-check: **two independent proofs, one via
a continuous invariant and one via an explicit closure computation, give the same answer.**

---

## 6. The theorem, at referee grade, with its exact scope

> **Theorem O.5 (the packet closure law, both inclusions).**
>
> **(a) Closedness — full generality.** Let X₀ be any arithmetic scheme, C algebraically closed
> satisfying the conditions preceding [x-03] Cor. 4.4, E any admissible class, N₀ any admissible
> monoid, and x₀ any point of X₀ with finite residue field. Then Γ^E_{x₀} = Π^{-1}(x₀) is a
> **closed, flow-invariant** subset of X₀ = X̌₀(C)^E ×_{Q^{>0}₀} R^{>0}. In particular
> cl_{X₀}(γ) ⊆ Γ^E_{x₀} for every periodic orbit γ ⊆ Γ^E_{x₀}, and distinct packets have disjoint
> closures.
>
> **(b) Equality — X₀ = Spec Z (and, verbatim, any arithmetic scheme with N₀ dense in Ẑ_{(p)}).**
> Let in addition N₀ = N, x₀ = (p), and let γ ⊂ Γ^E_p be any periodic orbit. Then
>
>   **cl_{X₀}(γ) = Γ^E_p exactly** — no intersection, no "char-p part" hedge —
>
> and upstairs, chartwise, cl_{X̌₀(C)^E}(O(P₀)) = C^E_{x₀}, with
> cl_{X•₀(C)^E}(S) = pr₀^{-1}(x₀) ∩ X•₀(C)^E in every chart.
> Consequently cl(γ) meets **neither** the generic stratum Π^{-1}((0)) **nor** the packet Γ^E_{p′}
> of any other prime p′.
>
> **(c) Corollary A.1 is therefore true as stated in its headline.** Γ^E_p (when nonempty) is a
> **minimal set**: it is nonempty, closed (a), flow-invariant (a), and every nonempty closed
> invariant F ⊆ Γ^E_p contains some orbit γ, whence F ⊇ cl(γ) = Γ^E_p by (b). It is the orbit
> closure of each of its points and the smallest closed invariant set containing any one of its
> orbits.

### 6.1 What each half costs

| Ingredient | needed for (a) | needed for (b) |
|---|---|---|
| X₀ carries the **quotient** topology ([x-03] p. 63; [x-06] p. 11; [r3s-08] p. 14) | **yes** | **yes** |
| pr_{X₀} : X̌₀(C)^E → X₀ continuous ([x-03] Lemma 7.1 p. 40; p. 42; p. 43; p. 47) | **yes** | yes (via (a)) or via Lemma O.3 |
| C_{x₀} = pr_{X₀}^{-1}(x₀) ([x-03] p. 31 + Lemma O.0) and E ⊆ E_tors (Def. 4.1) | **yes** | yes |
| κ(x₀) finite ⟹ {x₀} closed | **yes** | yes |
| N₀ dense in Ẑ_{(p)} (CRT; true for N₀ = N) | no | **yes** |
| Hom(κ(x)^×, C^×) = Ẑ_{(p)} (Lemma O.1′; [x-03] (34)) | no | **yes** |
| q open (Prop. 7.4 b) — only for the upstairs route of §5.5 | no | optional |
| Hausdorffness / metrizability / compactness | **no** | **no** |
| Theorem A | no | (b) reproves it |

### 6.2 Consequences worth recording (all new relative to the note's text)

1. **The closedness half needs no arithmetic at all.** It is true for every arithmetic scheme,
   every admissible E and every N₀ — including the "cut" classes of probe A's Theorem C(b) and
   including cases where the packet is empty. The program should file it as a structural fact
   about the suspension, not as a Spec Z computation.
2. **When the packet is a single orbit, that orbit is closed.** If C^E_{x₀} consists of one
   Q^{>0}₀-orbit — which is exactly probe A's Theorem C(b) cut-class situation — then
   Γ^E_{x₀} = γ and Theorem O.5(a) says **γ is a closed subset of X₀**. This bounds the
   adjudication §4 item 3's corollary "**no periodic orbit is closed as a subset**": that sentence
   is true only under the scope already stated for item 3 (E realizing ≥ 2 base classes), and is
   **false** for one-orbit-per-prime cuts. Recommend the corollary sentence be scoped explicitly,
   since it is the kind of line that gets quoted alone. (Bookkeeping, adjacent to my item.)
3. **Packets are compact for E ⊇ E_f**, which [x-03] p. 2 and [x-06] p. 12 assert without proof
   ("the closed points x₀ of X₀ correspond bijectively to **compact** packets Γ_{x₀}";
   "The **compact** subsets Γ_{x₀} ⊂ X₀ …"). Proof: by (38)/(39) (p. 32–33) and Thm. 5.2
   (E ⊇ E_f ⟹ C^E_{x₀} = C_{x₀}), every point of Γ_{x₀} is [F_r π(x, χ^a), w] = [π(x, χ^a), rw]
   with a ∈ Ẑ×_{(p)}; and [P, pu] = [F_p P, u] = [P, u] on C_{x₀}; hence
   Γ_{x₀} = q( π(β(Ẑ×_{(p)})) × [1, p] ), a continuous image of a compact set. Combined with
   Theorem O.5(a), packets are **compact and closed** — so the failure of Hausdorffness in X₀
   (adjudication §3) is *not* the familiar "compact but not closed" pathology at the level of
   packets; it is entirely internal to each packet. That is a sharper statement than the note's,
   and it matters for Q* (a compact **non-closed** invariant subspace, if one exists, must cut
   each packet in a non-closed piece).
4. **Nowhere density.** For X₀ integral normal flat of finite type over Spec Z, C = ℂ, N₀ = N and
   E ⊇ E_f: [x-03] Thm. 9.2 (p. 54, verbatim) — "the fibres of X̌(C)_{Ef} and X̌₀(C)_{Ef} over η
   resp. η₀ are dense in X̌(C)′ resp. X̌₀(C)′" — with §9's "X̌(C)′ = X̌(C) etc. if N₀ = N" (p. 53)
   and Cor. 9.7's own use of it ("By Theorem 9.2 they are dense in X resp. X₀", p. 62), together
   with openness of q, make Π^{-1}(η₀) dense in X₀. It is disjoint from Γ^E_{x₀} = Π^{-1}(x₀).
   A closed set with dense complement is nowhere dense; hence **every packet is nowhere dense in
   X₀**, which is how closedness of the packets coexists with connectedness of X₀ (Cor. 9.7).

---

## 7. Attempts to break it (required by method item 4)

I tried five ways to make the converse inclusion false. Four fail; one **succeeds** and pins the
exact hypothesis the statement needs.

**B1 — Break it by removing the (Tors) cut. SUCCEEDS.** Work in the *un-cut* suspension
X̌₀(C) ×_{Q^{>0}} R^{>0} (not one of Deninger's systems — §6 requires an admissible E — but a
legitimate topological object). Choose n_k := ∏_{ℓ ≤ k, ℓ ≠ p} ℓ^k ∈ N. For each ℓ ≠ p,
v_ℓ(n_k) = k → ∞, so n_k → 0 in Z_ℓ and hence n_k → 0 in Ẑ_{(p)} = ∏_{ℓ≠p} Z_ℓ (product topology).
By Lemma O.1′, F_{n_k}(x, χ^{a₀}) = β(a₀ n_k) → β(0) = (x, **1**), the trivial character, and by
the suspension identity [P₀, n_k u] = [F_{n_k} P₀, u] one gets
[P₀, n_k u] → [π(x, 1), u]. Now F_q(x, 1) = (x, 1) for every q ∈ Q^{>0}, so this limit point has
Q^{>0}-isotropy **all of Q^{>0}**, whereas every point of Γ_p has isotropy exactly p^Z ([x-03]
Thm. 5.2, p. 34); hence [π(x,1), u] ∉ Γ_p. **In the un-cut suspension the equality fails, and the
packet is not closed.** Deninger's Prop. 9.1 (p. 53, verbatim: "X•(C)′ is the topological closure
of X•(C)_{Etors} in X•(C)", with X•(C)′ = X•(C) when N₀ = N) makes this systematic: the E_tors
locus is a **dense, non-closed** subspace of the un-cut space, so nothing about it can be closed
for free. Conclusion: **the hypothesis E ⊆ E_tors (i.e. admissibility, Def. 4.1) is necessary and
is exactly what is being used**, via (★) in §4.1. Deninger's own "There are no fixed points of the
flow" ([x-03] p. 3, verbatim) is a shadow of the same fact.

**B2 — Break it by finding a non-closed point with finite residue field. FAILS.** §4.2(4) shows
finite residue field ⟹ closed, for an arbitrary scheme, by A/𝔭 ⊆ κ(x₀) finite ⟹ A/𝔭 a finite
domain ⟹ a field. There is no arithmetic scheme where the argument leaks.

**B3 — Break it by exploiting non-Hausdorffness of X₀. FAILS.** X₀ is non-Hausdorff along packets
(adjudication §3, confirmed there by a two-limit witness). In a non-Hausdorff space compact sets
need not be closed and limits are not unique — so one might hope cl(γ) exceeds the packet. It
cannot: Proposition O.1 uses no separation axiom whatsoever. Preimages of closed sets under
continuous maps are closed in any topological space. What non-Hausdorffness does break is the
*converse* intuition (that a compact packet must be closed for topological reasons); here
closedness is proved directly, and compactness (§6.2 item 3) is a separate fact.

**B4 — Break it by cross-chart accumulation in the colimit. FAILS.** One might hope that a net
in γ, wandering across infinitely many charts F_ν^{-1}(X•₀(C)^E), accumulates at a point invisible
to any single chart. It cannot: the charts are **open** (Prop. 7.4 a) + p. 47), so any limit point
lies in some chart and the net is eventually inside it (§3.3 (C2)); and closure is the union of the
chart closures (C3). Also, upstairs the whole Q^{>0}-orbit O(P₀) meets each chart in a
*single* translate of S (Lemma O.4), so there is nothing extra to accumulate on. This is the
concrete answer to the brief's worry that "the colimit topology is FINER than pointwise
convergence": it is, but only *between* charts, and between charts there is nothing here to see.

**B5 — Break it by an N₀ for which N₀ is not dense in Ẑ_{(p)}. FAILS against (a), BITES against
(b).** Deninger allows N₀ to be the monoid generated by any set of primes containing char X₀
([x-03] p. 42). If, say, N₀ = p^N, then cl(a₀N₀) ⊊ Ẑ_{(p)} and Lemma O.2's ⊇ half collapses: the
sweep does not reach the whole fiber, so **Theorem A** (and with it the *equality* in
Theorem O.5(b)) may fail. Closedness — Theorem O.5(a) — is untouched, since it never used density.
This asymmetry is the honest scope statement and is recorded in §6.1's table. (Deninger himself
takes N₀ = N from §8 onward, and Prop. 10.3 assumes char N₀ contains almost all primes.)

---

## 8. The brief's five questions, answered explicitly

**(1) The exact topology on X₀ in which closures are taken.** §3. In order: pointwise convergence
on X•(C), metrizable ([x-03] p. 40, Prop. 7.6 p. 44); glued over affine opens for non-affine X₀
(p. 41); quotient by the compact group G (p. 42, Cor. 7.8 p. 45, metrizable); inductive limit over
N₀ with charts open **and closed** (p. 43, Prop. 7.4); E-subspaces with subspace topologies and all
of §7 transferring (p. 47); and finally the **quotient** topology on the suspension, warranted by
[x-03] p. 63's (π_*C⁰_X̃)^Q = C⁰_X, [x-06] p. 11 and [r3s-08] p. 14.

**(2) Is "pointwise convergence of characters" the right description?** §3.6, final paragraph:
exactly right in each chart; strictly too coarse for the colimit (which is finer *between* charts,
though this changes nothing here — B4); and simply not a description of X₀ at all, whose quotient
map is open but neither proper nor properly discontinuous and therefore does **not** reflect
convergence. The note's instrument is a chart-level instrument applied to a suspension-level
statement. That is finding **F1**.

**(3) Is a limit with a zero component excluded by (Tors), by E, or by the topology — and does it
matter for the closure computed *in* X₀?** By **(Tors)**, hence by admissibility (Def. 4.1), hence
by E — never by the topology. But the note's criterion is **incomplete**: the correct criterion is
b ∈ N·Ẑ×_{(p)} (§5.2), and there are exponents with no zero component that still fail (Tors)
(b = (ℓ)_{ℓ≠p}). And "leaving the space" is the wrong idiom: the excluded points are genuinely
present in cl_{X•₀(C)}(S) (Lemma O.3) and are removed by the subspace-closure identity
cl_A(S) = cl_X(S) ∩ A. It matters decisively: **B1** shows that without the cut the equality is
false. Findings **F2** and **m3**.

**(4) Could cl(γ) meet other strata?** **No.** cl(γ) ⊆ Π^{-1}(x₀) (Proposition O.1), and the
generic stratum is Π^{-1}((0)) while the packet of another prime p′ is Π^{-1}((p′)); the fibers of
a map are disjoint. This is the part the note's hedge "∩ (char-p part)" was standing in for, and it
is now unconditional. Note that it is a statement about the **whole** colimit and the **whole**
suspension, as the brief requires — Π is defined on all of X₀, not stratum by stratum.

**(5) What is proved, and where?** Equality **in every chart** of the colimit (Lemma O.4 +
Lemma O.3), equality **in the colimit** (Lemma O.4), and equality **in X₀** (§5.5, and independently
§4.2 + Theorem A). Not "only within the char-p part": the char-p part is *itself* the packet
(m2), so that formulation was vacuous.

---

## 9. Findings, with exact replacement text

Locations are in `results/c3-r/probe-9.3-b.md`. The adjudicator applies repairs; I do not edit the
note.

### F1 — MAJOR. The instrument does not reach the target.
**Location:** §5, Corollary A.1, parenthetical, clause 1 ("every limit of {F_n(P₀)}_n along any
subnet is P₀^b for some b ∈ Ẑ_{(p)}, by compactness of Ẑ_{(p)} and the same pointwise evaluation").
**The defect.** What is computed is the set of subnet limits of a **sequence** in **one chart** of
**X•(C)** at **one point x over p**. What is claimed is the closure of a **circle γ** in the
**suspension X₀**. Three descents separate them — π (the G-quotient), the colimit inclusion, and
q (the Q^{>0}-quotient) — and the third is not bookkeeping: q is an open quotient by a **not
properly discontinuous** action ([x-03] p. 49, verbatim), X₀ is non-Hausdorff along the packets
(adjudication §3), and consequently **q does not reflect convergence**: a net convergent in X₀ need
have no convergent lift. Enumerating upstairs limits therefore bounds nothing downstairs.
**Fillable?** Yes, two ways: (i) the open-map closure identity q^{-1}(cl A) = cl(q^{-1}A) (§3.6),
which makes the upstairs computation legitimate; or (ii) Proposition O.1, which bypasses limits
altogether. Both are given above.
**Replacement text (adjudicator: substitute for the whole parenthetical):**

> *(Proof of the converse. Write Π[P₀,u] := pr_{X₀}(P₀). This is well defined and continuous:
> pr_{X₀} : X̌₀(C)^E → X₀ is continuous ([x-03] Lemma 7.1 p. 40, p. 42, p. 43, p. 47) and satisfies
> pr_{X₀} ∘ F_q = pr_{X₀} (p. 27, N₀- and Q^{>0}₀-equivariance with trivial action on X₀), so
> (P₀,u) ↦ pr_{X₀}(P₀) is constant on Q^{>0}₀-orbits and descends through the quotient topology of
> X₀ ([x-03] p. 63: R_X = (π_*R_X̃)^Q ⊂ (π_*C⁰_X̃)^Q = C⁰_X; [x-06] p. 11; [r3s-08] p. 14).
> Since φ^t[P₀,u] = [P₀,ue^t], every fiber of Π is flow-invariant. By [x-03] p. 31,
> C_{x₀} = pr_{X₀}^{-1}(x₀) inside X̌₀(C)_{Etors}, and E ⊆ E_tors by Def. 4.1, so
> C^E_{x₀} = pr_{X₀}^{-1}(x₀) ∩ X̌₀(C)^E and hence Γ^E_{x₀} = Π^{-1}(x₀). A point with finite
> residue field is closed (A/𝔭 ⊆ κ(x₀) finite ⟹ A/𝔭 a finite domain ⟹ a field ⟹ 𝔭 maximal;
> and closedness in one affine open containing the point gives closedness in X₀). Therefore
> Γ^E_{x₀} is closed, and cl_{X₀}(γ) ⊆ Γ^E_{x₀}. With Theorem A, cl_{X₀}(γ) = Γ^E_p exactly — no
> intersection and no hedge; in particular cl(γ) meets neither the generic stratum nor any other
> packet. No separation axiom, compactness or metrizability is used.)*

### F2 — MAJOR. The stated exclusion criterion is wrong, and would falsify the corollary.
**Location:** §5, Corollary A.1, parenthetical, clause 2 ("limits with some component of b equal to
0 kill a μ_{ℓ^∞} and violate (Tors), so they leave the space").
**The defect.** True but not exhaustive. Since ker(χ^b) = ⊕_{ℓ≠p} μ_{ℓ^{v_ℓ(b_ℓ)}}, (Tors) holds
**iff** every component is nonzero **and** all but finitely many are units, i.e. iff
b ∈ N·Ẑ×_{(p)} — matching [x-03] (35), p. 32, whose surjection has image exactly N₀·Ẑ×_{(p)}.
**Counterexample to the criterion as stated:** b = (ℓ)_{ℓ≠p}. No component is zero, yet
ker(χ^b) = ⊕_{ℓ≠p} μ_ℓ is infinite. If the note's criterion were complete, cl(γ) would contain the
image of every such b and would strictly contain Γ^E_p — **the corollary would be false**.
**Fillable?** Yes; the conclusion survives with the larger exclusion.
**Replacement text (for clause 2):**

> *"the limit (x, χ^{a₀b}) satisfies (Tors) if and only if ker(( )^b) = ⊕_{ℓ≠p} μ_{ℓ^{v_ℓ(b_ℓ)}} is
> finite of order in N₀, i.e. if and only if b ∈ N·Ẑ×_{(p)} — every component nonzero **and** all
> but finitely many a unit. Exponents such as b = 0 (which kills every μ_{ℓ^∞}) and
> b = (ℓ)_{ℓ≠p} (no zero component, but infinitely many non-unit components) both fail (Tors), and
> both are points of Deninger's un-cut X•(C) that lie in no X•(C)^E."*

### F3 — MAJOR. The hedged conclusion carries no converse content, while the headline asserts one.
**Location:** §5, Corollary A.1, parenthetical, clause 3 ("one gets cl(γ) ∩ (char-p part) = Γ^E_p
exactly"), read against the corollary's headline.
**The defect.** For X₀ = Spec Z, Deninger's char-p locus is X̌(C)_{p,Etors} := pr_X^{-1}(X ⊗ F_p)
([x-03] p. 33, verbatim), and (p) is the **only** point of Spec Z of characteristic p; so the
char-p part of X₀ is precisely Π^{-1}((p)) = Γ^E_p. The equation "cl(γ) ∩ Γ^E_p = Γ^E_p" is
therefore **logically equivalent to Theorem A** (cl(γ) ⊇ Γ^E_p) and states nothing new. Meanwhile
the corollary's headline — "Γ^E_p is the orbit closure of each of its points", "the smallest closed
invariant set containing any one of its orbits", "packets are minimal sets" — **requires** the
converse (a minimal set is by definition closed). So the corollary's principal assertions were, at
the time of writing, unproved.
*(Caveat for the general statement: for X₀ ≠ Spec Z the char-p locus is a union of packets, one per
point of X₀ over p, so the hedge would not be quite vacuous there — but it would still not deliver
the converse. Recommend the hedge be deleted rather than generalized.)*
**Fillable?** Yes — by F1's replacement, which proves exactly what the headline asserts.
**Replacement text (for clause 3 and for the corollary's closing):**

> *"one gets cl_{X₀}(γ) = Γ^E_p exactly, in X₀ and in every chart of the colimit; the packet is a
> closed flow-invariant set, so it is a minimal set and is the orbit closure of each of its points.
> (Referee grade; the kill needs only ⊇, but the minimality statement in the headline needs both.)"*

### m1 — MINOR. Wrong cross-reference.
"With Step 5's converse inclusion" — Theorem A's Step 5 is the *sweep* (⊇) and contains no
converse. **Replacement:** "With the converse inclusion, proved below,".

### m2 — MINOR. "(char-p part)" is undefined in the note.
The note never defines it. If defined as Deninger's X̌₀(C)_{p,Etors} ([x-03] p. 33) it is, for
Spec Z, the packet itself (F3). **Replacement:** delete the hedge.

### m3 — MINOR. "so they leave the space" is under-specified.
The operative fact is `cl_A(S) = cl_X(S) ∩ A` for the E-subspace A ([x-03] p. 47: the E-spaces
carry subspace topologies). The excluded characters are genuinely **in** cl_{X•₀(C)}(S) — indeed
X•(C)_{Etors} is dense in X•(C) for N₀ = N ([x-03] Prop. 9.1, p. 53) — so nothing "leaves"; they
are cut away by the ambient choice. **Replacement:** "so they lie outside X̌₀(C)^E, and since the
closure is taken in the E-space, cl_{X̌₀(C)^E} = cl_{X̌₀(C)} ∩ X̌₀(C)^E removes them. In the un-cut
suspension the equality is false: taking n_k = ∏_{ℓ≤k, ℓ≠p} ℓ^k gives n_k → 0 in Ẑ_{(p)} and
[P₀, n_k u] → [π(x,1), u] ∉ Γ_p."

### m4 — MINOR. "by compactness of Ẑ_{(p)}" misnames the mechanism.
Compactness is not used. What is used is (i) Hom(κ(x)^×, C^×) = Ẑ_{(p)} ([x-03] (34), p. 32) so
that pr_X^{-1}(x) is exactly the b-family, (ii) continuity of b ↦ χ^b, which holds because each
coordinate is **locally constant**, and (iii) density of N in Ẑ_{(p)}. **Replacement:** "by
Hom(κ(x)^×,C^×) = Ẑ_{(p)} ((34), p. 32), local constancy of b ↦ χ^b(r) in b, and density of N".

### m5 — MINOR (in the dated block, part (f)). Miscitation and conflation.
"the colimit topology is not finer than the pointwise one on any chart (p. 47: the inductive-limit
and subspace topologies agree)" — p. 47's sentence is about **X̌(C)_E ⊂ X̌(C)** (E-cut vs. un-cut),
not about chart vs. colimit. The correct warrant is **Prop. 7.4 a), p. 43** ("X•(C) is a closed and
open subspace of X̌(C)") together with p. 43's characterization of the inductive-limit topology.
And the sentence conflates two topologies: the colimit topology **is** strictly finer than the
pointwise topology on the set X̌(C) (via Cor. 3.8's description, p. 26) — it is only on each chart
that the two agree. **Replacement:** "the subspace topology that the colimit induces on each chart
is the chart's own pointwise topology (Prop. 7.4 a), p. 43, with p. 43's description of the
inductive-limit topology), and closure is therefore computed chartwise; the colimit topology is
strictly finer than pointwise convergence on lim_{←} κ(x)^× *between* charts, which changes
nothing here because the charts are open and O(P₀) meets each in a single translate of S."

### m6 — MINOR (in the dated block, part (b)). A false "iff".
"F_{m/m′}P₀ lies in the chart F_ν^{-1}(X•₀(C)^E) iff m′ | ν" is false as written: take m = 1,
m′ = p, ν = 1. Then F_{1/p}P₀ = F_p^{-1}P₀ = P₀ ∈ X•₀(C)^E, yet p ∤ 1. **Replacement:** "writing
m′ = p^j m″ with p ∤ m″, one has F_{m/m′}P₀ = F_{m/m″}P₀ (because F_p P₀ = P₀), and F_{m/m″}P₀ lies
in F_ν^{-1}(X•₀(C)^E) iff m″ | ν; in lowest terms m″ = 1, so O(P₀) ∩ X•₀(C)^E = {F_n P₀ : n ∈ N}."

---

## 10. Two findings against a cited source, reached independently (N1, N2)

These are not in the note. They are adverse: N1 deflates the novelty of the repair, N2 adds a
second defect to statements the program already carries a caution about (ledger row W11,
adjudication §4 item 4). Standing order 7 requires them stated at full strength.

### N1 — MINOR (priority). The engine of the repair is already in print.

[r3s-08] p. 14 — read as a **rendered page image** because the text layer garbles it — verbatim:

> "Next we describe the structure of ℝ₊-orbits in 𝔛_K. By the definition (2.2.1) of 𝔛_K, it
> suffices to describe ℚ₊-orbits in X̌_K(ℂ). Let ṗr : Ẋ_K(ℂ) → X_K and p̌r : X̌_K(ℂ) → X_K be the
> projections defined by (𝔭, P) → 𝔭, and let **pr**_K : 𝔛_K → X_K be the composition of the
> projection 𝔛_K → X̌_K(ℂ) with p̌r_K. **These projections ṗr_K, p̌r_K and pr_K are continuous.**"

and p. 15, verbatim:

> "We set  C_𝔭 := p̌r_K^{-1}(𝔭) = ⋃_{n∈N} F_n^{-1}(ṗr_K^{-1}(𝔭)),  which is a ℚ₊-invariant subset of
> X̌_K(ℂ), and we set  Γ_𝔭 := C_𝔭 ×_{ℚ₊} ℝ₊ ⊂ 𝔛_K."

So the map I call Π, its continuity, and the identification of the packet as its fiber are all
**asserted in the literature**. Closedness of the packet is then a one-line consequence, given that
{𝔭} is closed. Program consequence: **Proposition A.1′ / Proposition O.1 must be recorded as
"immediate from [r3s-08] pp. 14–15 (assertions) and from [x-03] Lemma 7.1 p. 40 + p. 43 + p. 31
(proofs)", not as a new result.** What is genuinely contributed here is (i) proofs where [r3s-08]
gives assertions, (ii) the E-correction below, and (iii) the *use* — nobody in either source draws
the closedness conclusion or the equality cl(γ) = Γ_p.

*(Two textual cautions on that page: the phrase "the composition of the projection 𝔛_K → X̌_K(ℂ)
with p̌r_K" is a slip — there is no projection 𝔛_K → X̌_K(ℂ); the intended map is the descent of
p̌r_K ∘ pr₁ along the quotient, which is exactly Π. And "We equip 𝔛_K twith he quotient topology of
the product X̌_K(ℂ) × ℝ₊" contains a transposition. Both are in the source.)*

### N2 — MINOR (source defect, new). [r3s-08] (2.2.7) is not surjective, so his C_𝔭 is not the packet.

[r3s-08] Remark 2.1.13, p. 13, verbatim:

> "In [D7; Section 4], Deninger requires some conditions on P^× in (2.1.5) to make
> Ẋ_K(ℂ) = Ẋ_Q(ℂ)/Gal(Q̄/K) and hence X̌_K(ℂ) smaller space which would lead to a correct geometric
> model for X_K (cf. [D7; Section 4]). **We omit this refinement** on Ẋ_K(ℂ) and X̌_K(ℂ), since our
> purpose in this paper is to give a relation with Connes-Consani's adelic spaces."

and (2.1.5) p. 12: "Ẋ_Q(ℂ) = {(𝔭, P^×) | 𝔭 ∈ X_Q, P^× ∈ Hom_Gr(κ(𝔭)^×, ℂ^×)}" — **all**
characters, no (Tors). Then p. 16, (2.2.7), verbatim:

> "Ẑ×_{(p)} × N ↠ Hom_Gr(κ(P)^×, ℂ^×); (a, n) ↦ χ_P ∘ ( )^a ∘ ( )^n."

**This arrow is not a surjection.** By Lemma O.1′, Hom_Gr(κ(P)^×, ℂ^×) = Hom(μ^{(p)}, ℂ^×) ≅ Ẑ_{(p)},
while the image of the displayed map is {χ_P ∘ ( )^b : b ∈ N·Ẑ×_{(p)}} — the (Tors) locus, a proper
subset (§5.2). Witnesses outside the image: b = 0, and b = (ℓ)_{ℓ≠p} (machine check
`r3s08_2_2_7_not_surjective`). Consequences, all internal to [r3s-08]:

* his ṗr_K^{-1}(𝔭) and C_𝔭 = p̌r_K^{-1}(𝔭) are **strictly larger** than Deninger's pr₀^{-1}(x₀) and
  C_{x₀}, which live in X̌₀(C)_{Etors} by construction ([x-03] p. 31);
* Thm. 2.2.8(1) ("Ẑ×_{(p)} ×_{p^Z} ℚ₊ ≅ C_𝔭") and Thm. 2.2.9(1) are therefore **false for his own
  un-cut C_𝔭** and become correct only once Deninger's E_tors refinement is restored — at which
  point they are [x-03] (38)/(39), which are **bijections**, not homeomorphisms (the separately
  flagged W11 defect);
* his Γ_𝔭 = C_𝔭 ×_{ℚ₊} ℝ₊ is the **fiber**, not the **packet**: in the un-cut suspension the two
  differ, and the extra points include the flow-degenerate [π(x,1),u] of break attempt **B1**, so
  the "decomposition into connected closed ℝ₊-orbits" of Thm. 2.2.9(2) fails there as well, for a
  reason *independent* of the topology objection already on record.

**Program consequence, binding on the repair:** one may **not** shortcut Proposition O.1 by citing
[r3s-08] pp. 14–15, even though the ingredients are there, because his Γ_𝔭 is not Deninger's
packet. The fiber identification must be made **inside X̌₀(C)_{Etors}**, exactly as [x-03] p. 31
does and as (★) of §4.1 does. Recommend adding this as a second bullet under the existing
"Morishita flag" (adjudication §4 item 4 / ledger W11): *do not cite [r3s-08] §2.2 for topology,
and do not cite it for the identification of the packet either — its packet is the un-cut fiber.*

---

## 11. Novelty and priority (standing order 7)

Component by component, with the anchor that pre-empts it where one exists:

| Component of the converse | Status |
|---|---|
| X₀ carries the quotient topology | **Deninger's**: [x-03] p. 63 (π_*C⁰_X̃)^Q = C⁰_X; also [x-06] p. 11; stated outright by [r3s-08] p. 14. |
| pr_{X₀} continuous on X•(C), X̌(C), X̌₀(C) | **Deninger's**: [x-03] Lemma 7.1 p. 40, p. 42, p. 43, p. 47. |
| Π : X₀ → X₀ exists and is continuous | **Morishita's assertion**: [r3s-08] p. 14 (with a slipped definition, no proof). Deninger has all the ingredients but does not display the map on the suspension. |
| C_{x₀} = pr_{X₀}^{-1}(x₀); Γ_{x₀} = C_{x₀} ×_{Q^{>0}} R^{>0} | **Deninger's**: [x-03] p. 31, p. 38. Also [r3s-08] p. 15 (un-cut, hence not the packet — N2). |
| Points with finite residue field are closed | Standard commutative algebra. |
| **Γ^E_{x₀} is closed in X₀** | **Not stated in either source.** One line from the above; the contribution is the observation and its use, not the ingredients. Novelty: LOW. Do not bank as a theorem of the program without the pre-emption line above. |
| **cl_{X₀}(γ) = Γ^E_{x₀}** (equality) | **Not stated in either source**; needs Theorem A, whose novelty was separately dual-checked. Novelty: the equality is a corollary of Theorem A + closedness. |
| Packets are **compact** (§6.2 item 3) | **Asserted without proof** by Deninger: [x-03] p. 2, [x-06] p. 12. The proof here is new; the statement is not. |
| Packets are **nowhere dense** (§6.2 item 4) | Follows from [x-03] Thm. 9.2 p. 54 + Cor. 9.7 p. 62 + closedness. Not stated; low novelty. |
| Failure in the un-cut suspension (**B1**) | Consonant with [x-03] Prop. 9.1 p. 53 and with "There are no fixed points of the flow" p. 3. Not stated; low novelty. |

**Recommendation to the adjudicator.** Record the converse as *"discharged; mechanism is
Deninger's own continuous pr_{X₀} pushed through the suspension quotient, a map Morishita already
displays and asserts continuous ([r3s-08] p. 14). The program's contribution is the proof, the
E-correction (N2), and the consequences (minimality, compactness, nowhere-density)."* Any external
circulation must carry that attribution.

---

## 12. What is now established at referee grade, and its precise scope

**One paragraph, as required.** The converse inclusion is **true**, and more is true than the note
claimed: for *every* arithmetic scheme X₀ in Deninger's sense, *every* admissible class E, *every*
admissible monoid N₀, *every* algebraically closed C satisfying his standing hypotheses, and
*every* point x₀ of X₀ with finite residue field, the packet Γ^E_{x₀} is a **closed, flow-invariant**
subset of the suspension X₀ — because it is the fiber over the closed point x₀ of the continuous
map Π : X₀ → X₀ obtained by descending pr_{X₀} through the quotient topology of the suspension,
and no separation axiom, compactness, metrizability, density or Hausdorffness enters that
argument; hence cl_{X₀}(γ) ⊆ Γ^E_{x₀} for every periodic orbit γ in the packet, with no "char-p
part" hedge, and cl(γ) meets neither the generic stratum nor any other packet. Adding Theorem A —
which is where the arithmetic lives, and which needs N₀ dense in Ẑ_{(p)} (true for N₀ = N) and the
identification Hom(κ(x)^×, C^×) = Ẑ_{(p)} — gives **cl_{X₀}(γ) = Γ^E_{x₀} exactly**, for X₀ = Spec Z
and for any arithmetic scheme with N₀ = N, and the equality holds **verbatim in every chart of the
colimit** (cl_{X•₀(C)^E}(S) = pr₀^{-1}(x₀) ∩ X•₀(C)^E) as well as globally in X₀, the closure in the
colimit being the union of the chart closures because the charts are open. Consequently
Corollary A.1's headline is correct: packets are **minimal sets**, each is the orbit closure of
each of its points and the smallest closed invariant set containing any one of its orbits; they
are additionally **compact** when E ⊇ E_f and **nowhere dense** when X₀ is flat of finite type over
Spec Z with C = ℂ. The scope limits that must travel with the statement are four: **(i)** the
hypothesis E ⊆ E_tors — i.e. admissibility — is *necessary*, not decorative: in the un-cut
suspension the packet is not closed and the equality is **false** (break attempt B1, with
[x-03] Prop. 9.1 p. 53 as the systematic reason); **(ii)** the *equality* half fails for monoids
N₀ that are not dense in Ẑ_{(p)}, while the *closedness* half does not; **(iii)** when the packet
is a single orbit — probe A's Theorem C(b) cut classes — that orbit is itself **closed**, so the
program's unscoped sentence "no periodic orbit is closed as a subset" must be read only under the
scope already recorded for adjudication §4 item 3; **(iv)** nothing here touches the mapping face
of S4: a *compact but non-closed* invariant subspace, or a continuous equivariant image, is
unconstrained by closedness of the packets, so **Q\* of the Session-8 adjudication is unchanged**,
and its Q-c is now settled **YES** in the strong form. Finally, priority: the mechanism is not new
— Deninger proves pr_{X₀} continuous ([x-03] Lemma 7.1 p. 40, p. 43) and defines C_{x₀} as its
fiber (p. 31), and Morishita already displays the descended map on the suspension and asserts it
continuous ([r3s-08] p. 14); the contribution here is the proof, the correction that Morishita's
own packet is the *un-cut* fiber and hence not Deninger's packet (finding N2), and the
consequences drawn.

---

## 13. Sources — every page read this session

Extraction: `pdftotext -layout` into the session scratchpad, fresh this session; [r3s-08] p. 14 was
additionally read as a rendered page image (the text layer garbles it). Page numbers are the
**printed** ones; for all three files PDF page = printed page, verified against the printed folios.

**[x-03] Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4** —
`fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`.
Read: **p. 1** (Introduction, opening); **pp. 2–3** (compact packets, the fibration over
Ẑ×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p)^, "There are no fixed points of the flow", connectedness);
**p. 26** (Prop. 3.7, Cor. 3.8, §4 opening); **p. 27** ((Tors), (Image), **Def. 4.1**, **Prop. 4.2**,
(30)/(31) pr_X and pr_{X₀} with trivial N₀- and Q^{>0}₀-action on X, X₀); **p. 28** (Lemma 4.3,
conditions on C, Cor. 4.4, examples E_tors, E_max); **p. 29** (examples E_f, E_fg, E_fd, E_fd0;
the E-dependence remark; the p-adic "additive mod p" remark; stability/functoriality);
**p. 30** (Prop. 4.5 proof, Lemma 4.6); **p. 31** (§5 opening, (32), (33), **C_{x₀} = pr_{X₀}^{-1}(x₀)
in X̌₀(C)_{Etors}** and C_{x₀} = ⋃_ν F_ν^{-1}pr₀^{-1}(x₀)); **p. 32** (**(34)**, **(35)**, (36), (37),
**(38)**, the injective χ_x); **p. 33** ((39), the fibration over Ẑ×_{(p)}/p^Ẑ, (40)–(46), the
definition **X̌(C)_{p,Etors} = pr_X^{-1}(X ⊗ F_p)**); **p. 34** (Prop. 5.1, **Thm. 5.2** with
"If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}"); **p. 37** (Remark 5.4, Thm. 5.5); **p. 38** (§6: the
suspension, the flow, **Γ_{x₀} = C_{x₀} ×_{Q^{>0}₀} R^{>0}**, the R^{>0}-**bijection**, Γ^E_{x₀});
**p. 39** (**Thm. 6.1**, the packet/closed-point correspondence, the X₀(C) ×_{F∞} R^× immersion);
**p. 40** (the Y₀ question verbatim; **§7 opening: pointwise convergence, metrizability**;
**Lemma 7.1** with proof); **p. 41** (Lemma 7.2; the glued topology for non-affine X₀);
**p. 42** (the affine-cover criterion; the G-quotient topology; **"pr_X : X•(C) → X and hence also
pr_{X₀} : X•₀(C) → X₀ are continuous"**; **Lemma 7.3** and **(51)**); **p. 43** (the inductive-limit
topology and its closed/open criterion; **Prop. 7.4 a) b) c)**; the quotient X̌₀(C) = X̌(C)/G;
π, π̌ continuous and open; **"pr_X : X̌(C) → X and pr_{X₀} : X̌₀(C) → X₀ are continuous"** with proof);
**p. 44** (Prop. 7.5, Prop. 7.6, Prop. 7.7); **p. 45** (Prop. 7.7 proof; **Cor. 7.8**; **Cor. 7.9**);
**p. 46** (the separated-X₀ Hausdorff remark; the p/Q strata; **Thm. 7.10**); **p. 47** (Remarks 1
and 2 including "**not homeomorphisms in general**"; **the E-topologies paragraph**: subspace
topologies, colimit = subspace, "**All preceding results in this section remain true … by
X•(C)_E etc.**"); **p. 48** ((59)–(68), Ȟ_{Etors}, τ, ρ, the adele map);
**p. 49** (**"The Q^{>0}-action on Ȟ_{E_tors} × R^{>0} is not properly discontinuous. In section 10,
we will see that this works to our advantage."**; §8 opening: N₀ = N, "the system Y₀ is still
infinite-dimensional", Y₀ = X̌₀(S¹) ×_{Q^{>0}} R^{>0}, Claim 8.1); **p. 51** (Lemma 8.3 proof
context); **pp. 52–53** (Lemma 8.3 proof; **§9 opening**, X̌(C)′, "X̌(C)′ = X̌(C) etc. if N₀ = N",
**Prop. 9.1**); **p. 54** (**Thm. 9.2** with proof); **pp. 55–57** (Thm. 9.2/9.6 machinery, read for
context only); **p. 60** (the quotient-vs-subspace remark on pr_{X₀}^{-1}(η₀), (92)–(96));
**p. 62** (**Cor. 9.7** with proof; Thm. 9.8); **p. 63** (§10 opening; **R_X = (π_*R_X̃)^Q ⊂
(π_*C⁰_X̃)^Q = C⁰_X**; "will not be a homeomorphism … with the subspace topology of X"; "will not
be locally trivial"; Def. 10.1); **p. 64** (**Thm. 10.2**; Prop. 10.3 and its T₁ remark).

**[x-06] Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643** —
`fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`.
Read: **p. 10** (rational Witt spaces, the topology reference to [Den22a, §7]);
**p. 11** (**Thm. 4.1**; **"Set X₀ = (X̌₀(C) × R^{>0})/Q^{>0} where Q^{>0} acts diagonally"**; the
foliation; the admissible-E discussion; **Thm. 4.2**);
**p. 12** (**"The compact subsets Γ_{x₀} ⊂ X₀ … pairwise disjoint … fibre space over the compact
group Aut(F̄_p)/Aut(F_p)^ with fibres the compact orbits"**; Thm. 4.3; the "not significantly
smaller" closure statement; the p/Q strata and the in-loci).

**[r3s-08] Morishita, arXiv:2508.15971v5** —
`fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`.
Read: **p. 12** ((2.1.3)–(2.1.6): Ẋ_K(ℂ) with **no** condition on P^×; the pointwise topology;
(2.1.7)–(2.1.8)); **p. 13** (Prop. 2.1.9; the quotient topology on Ẋ_K(ℂ); the colimit X̌_K(ℂ);
(2.1.10)–(2.1.12); **Remark 2.1.13** — the refinement is omitted);
**p. 14** (**read as a page image**: (2.2.1); "**We equip 𝔛_K twith he quotient topology of the
product X̌_K(ℂ) × ℝ₊**"; (2.2.2); the foliation; ϖ_{L/K}; **"let pr_K : 𝔛_K → X_K … These
projections ṗr_K, p̌r_K and pr_K are continuous"**);
**p. 15** (**"C_𝔭 := p̌r_K^{-1}(𝔭) = ⋃_{n∈N} F_n^{-1}(ṗr_K^{-1}(𝔭))"**, "Γ_𝔭 := C_𝔭 ×_{ℚ₊} ℝ₊ ⊂ 𝔛_K";
(2.2.5); (2.2.6));
**p. 16** (the isomorphism Ẑ×_{(p)} ≅ Aut(F̄_p^×); **lk_p** and "the map lk_p is nothing but the
arithmetic linking homomorphism"; **(2.2.7)** — the non-surjective "↠" of finding N2; Thm. 2.2.8(1));
**p. 17** (Thm. 2.2.8(1)/(2); Thm. 2.2.9(1)); **p. 18** (Thm. 2.2.9(2), "decomposition into connected
closed ℝ₊-orbits"; §2.3 opening).

**Program files read (not sources):** `results/c3-r/probe-9.3-adjudication.md` (in full, including
the Session-14 insertions — see the disclosure in §0.2); `results/c3-r/probe-9.3-b.md` (in full,
including its Session-14 insertions); `results/corpus-routing.md` (header caveats, esp. 14 and 16).

**Not consulted (deliberately, for independence under standing order 7):** referee F's report on
this item, the prior adjudication of this item, the prior run of this report (preserved at
`results/c3-r/referee-s14/B-corA1-O-run1-0809.md`), probe A, and the M2c ledger.

— end of referee report O —
