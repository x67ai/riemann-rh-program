# ADVERSARIAL CHECK (Opus 5) OF THEOREM F-1 / THEOREM A, COROLLARY A.1, B1′ AND THE ε_x CORRECTION
## Stream (c″), direction C3-r, Session 16 — 2026-09-06

**Role.** Opus 5, adversarial verifier. The items below were derived by Fable 5.1 (refuter F,
`refute-F.md` §1.5 Theorem F-1, §3.4) and re-derived by Fable 5.1 (the binding adjudicator,
`refute-adjudication.md` §1.5 Theorem A + Corollary A.1, §3.4, §1.1). Both passes are on ONE model.
This is the second model. Standing order 5: I re-derived every item from the printed hypotheses and
the primary sources; I weighed no testimony. A target STANDS only where I wrote the proof myself.

**Bottom line.** Nothing falls. Every target is true, but four of the seven printed statements carry
hypotheses that are too weak for the instruments they invoke, or conclusions stronger than the proofs
deliver. The corrections are listed in §8 with exact wording. One of them (B1′'s "finitely generated")
is a real over-statement: the proof gives *finite rank*, not finite generation, and the gap between
those two is not closable by the argument given. The S4′ kill is unaffected.

---

## §0. VERDICT TABLE

| Target | Verdict | One-line reason |
|---|---|---|
| **(A)** µ concentrated on N ⇒ φ^t_*µ = µ | **STANDS** | Proof re-derived in full (§1). Needs only: φ a jointly continuous R-action, leaves = countable unions of plaques. Agreement with holonomy is claimed and used only on N, which is exactly what the proof establishes and all it needs. |
| **(B)** under (0-coh) no such µ ≠ 0 | **STANDS** | Proof re-derived (§2), and it is *stronger* than printed: one-dimensionality of H̄²_F is not used, only φ^{t*}[λ_g] = e^t[λ_g]; and the "concentrated on N" hypothesis enters only through (A). C_µ descends to reduced cohomology because it is bounded in the C⁰ seminorm, which is one of the seminorms of Deninger's Fréchet topology ([x-20] p. 14, p. 29). |
| **(C)** C1–C4 | **STANDS-NARROWED** | C1, C4 stand as printed (C4 needs the precise phrasing, §3.4). **C2 and C3 need g in Candel's regularity class** (leafwise smooth with *all leafwise derivatives continuous in all variables*, Candel §1.2 p. 492), not the printed "continuous leafwise metric": Deninger's A^•_F asks only for continuity transversally ([x-20] p. 30, Warning), so the printed hypothesis does not license Candel's theorems. |
| **(D)** (31) along L + fixed point + compact ⇒ no object | **STANDS-NARROWED** | True; the hypothesis set must be printed in full (§4.6) and includes the Candel regularity of (C). Two proof repairs: the orientation step must be justified (adjudicator does, F does not), and **the Ĉ case does not need (C1)/(0-coh)** — (31) along L kills it by itself, which shortens the dependency chain. Consistency with [De02] checked at source: that example has **no fixed point** ([x-20] p. 35, verbatim) and satisfies (31) globally with α = 1 on a compact space with *euclidean* leaves — the exact boundary case, and a guard against over-reading Theorem A. |
| **(corA1)** flow not conformal along L; χ = +1 ⇒ disk | **STANDS-NARROWED** | First half stands. Second half holds only under an explicit reading of clause (iii)'s "nonzero Euler characteristic": *L is of finite topological type and χ(L) = 2 − 2g − n*. Then χ = +1 ⟺ L ≈ R², and hyperbolic + simply connected ⇒ conformally D. For an infinite-type leaf χ is not defined and the clause is empty. |
| **(B1′)** length group | **STANDS-NARROWED** | Three corrections. (i) **"finitely generated" is not derivable — the proof gives finite RANK** (dim_Q Λ⊗Q < ∞); a subgroup of R of finite Q-rank need not be finitely generated (Z[1/2]). (ii) Λ must be restricted to closed orbits **transverse to F**; orbits inside N are invisible to ω. (iii) N must be read as the **tangency set** {Y_φ ∈ TF}, assumed a finite union of leaves — under that hypothesis it coincides with the union of preserved leaves. With these, the proof is correct and I re-derived it, including KMNT Lemma 1.10's independence of transverse simplicity and of compactness of the leaves in N (verified in KMNT's own proof). The S4′ kill survives all three. |
| **(ε)** det = e^t and ε_x = +1 force a leafwise source | **STANDS** | Re-derived from [x-20] p. 31 Rem. 7.6(2), p. 31 W_x, and the archimedean W_p of the explicit formula at p. 10 (κ_p = −1 complex, −2 real, both **negative**). ε_x = sign det(1 − T_xφ^t|T_xF) — the LEAF, not the normal direction. Matching the explicit formula forces ε_x = +1 *and* det = e^t, and the 2×2 algebra then forces both eigenvalues into the open right half-plane. O's saddle diag(2, −1) gives ε_x = −1 and is excluded. Neither condition, nor both, forces the SO(2) form. |

---

## §1. TARGET (A) — STANDS

**Statement I can prove.** *Let X be a compact metrizable foliated space with 2-dimensional leaves,
φ: R × X → X a jointly continuous R-action by homeomorphisms each of which maps leaves to leaves
([x-20] 7.3 p. 30, read: "A flow φ on X is a continuous R-action such that the induced R-actions on
the leaves of L are smooth"). Let N := {x ∈ X : φ^s(x) ∈ L_x for all s ∈ R} = the union of the leaves
preserved by the flow. Then every positive holonomy-invariant transverse measure µ concentrated on N
satisfies φ^t_*µ = µ for all t.*

### 1.1 Three preliminaries I need, each derived

**(P1) N is exactly the union of the preserved leaves, and N is closed, saturated, flow-invariant.**
If φ^s(x) ∈ L_x for all s, then for y ∈ L_x, φ^s maps L_x into a leaf containing φ^s(x) ∈ L_x, so that
leaf is L_x: L_x is preserved. Conversely a point of a preserved leaf satisfies the condition. So N is
saturated and flow-invariant, and the two descriptions agree. *Closed:* let x_n → x, x_n ∈ N. Choose a
chart U ∋ x, U ≅ D × T. By continuity of φ at (0, x) and compactness of [−δ, δ] there are δ > 0 and a
neighborhood W ∋ x with φ([−δ, δ] × W) ⊂ U. For x_n ∈ W the segment φ^{[−δ,δ]}(x_n) lies in L_{x_n}
(as x_n ∈ N) and in U, so by (P2) below its T-coordinate is constant: pr_T(φ^s(x_n)) = pr_T(x_n) for
|s| ≤ δ. Letting n → ∞ and using continuity of φ and of pr_T: pr_T(φ^s(x)) = pr_T(x) for |s| ≤ δ, i.e.
φ^s(x) lies in the plaque of x, hence in L_x, for |s| ≤ δ. The set {s : φ^s(x) ∈ L_x} is a subgroup of R
(if φ^s(x) ∈ L_x and φ^{s'}(x) ∈ L_x then φ^{s+s'}(x) = φ^{s'}(φ^s(x)) ∈ φ^{s'}(L_x) = L_{φ^{s'}(x)} = L_x)
containing (−δ, δ), hence all of R. So x ∈ N. ∎ *(This re-proves `refute-adjudication.md` §3.2 (b)
independently; I did not use their argument.)*

**(P2) A leaf meets each chart in countably many plaques, and a connected orbit segment inside a leaf
and inside a chart lies in a single plaque.** X is compact metrizable, so finitely many charts U_1, …,
U_r suffice. A leaf L is the set of endpoints of plaque chains from a fixed plaque; chains are finite
words in {1, …, r} (countably many), and a word determines at most one plaque of L by continuation, so
L ∩ U_i is a countable union of plaques and pr_{T_i}(L ∩ U_i) is countable. If σ: [a, b] → L ∩ U_i is
continuous, pr_{T_i} ∘ σ is a continuous map of a connected set into a countable subset of a metric
space, hence constant (a connected metric space with ≥ 2 points is uncountable). ∎

**(P3) Tube lemma for the chain.** Fix t > 0 and x. Choose 0 = s_0 < … < s_k = t and charts U_0, …,
U_{k−1} with φ^{[s_i, s_{i+1}]}(x) ⊂ U_i (possible by continuity and compactness of [0, t]). By the tube
lemma there is a neighborhood W ∋ x with φ^{[s_i, s_{i+1}]}(W) ⊂ U_i for every i. ∎ *No uniform
continuity is needed, and no transverse regularity of the flow beyond joint continuity.*

### 1.2 The proof

Let T be a standard transversal of a chart U_0, x ∈ T ∩ N, and let V_x := T ∩ W with W from (P3),
shrunk further so that the plaque-chain holonomy germ
h_x := τ_{k−1,k} ∘ … ∘ τ_{0,1} : (nbhd of x in T) → T_{k−1}
along the chain P_0, …, P_{k−1} of plaques through φ^{[0,t]}(x) is defined on V_x and injective (each
τ_{i,i+1} is the transverse component of a chart transition at φ^{s_i}(x), a homeomorphism of germs).

Let y ∈ V_x ∩ N. Each segment φ^{[s_i, s_{i+1}]}(y) lies in L_y (y ∈ N) and in U_i (P3), hence in a
single plaque of L_y ∩ U_i (P2). At the junction s_i the point φ^{s_i}(y) belongs to both the
U_{i−1}-plaque and the U_i-plaque, so those two plaques correspond under the transition germ τ_{i−1,i}
and pr_{T_i}(φ^{s_i}(y)) = τ_{i−1,i}(pr_{T_{i−1}}(φ^{s_{i−1}}(y))). Composing over i:

  **pr_{T_{k−1}}(φ^t(y)) = h_x(y)  for every y ∈ V_x ∩ N.**  (★)

This is the exact content of the claim, and it is claimed and used **only on N**. Off N the left side is
still defined but need not be constant along the segment (indeed if φ is transverse to F at y the
segment crosses plaques), and (★) is false there. Nothing in the argument needs it there.

Now fix a Borel B ⊂ V_x. The set φ^t(B ∩ N) is a Borel transversal (φ^t is a foliated homeomorphism, so
it maps sets meeting each leaf countably to sets meeting each leaf countably), it lies in U_{k−1}, and
pr_{T_{k−1}} is injective on it by (★) and injectivity of h_x. A regular transversal on which the plaque
projection is injective is carried to its projection by a holonomy transformation (Candel §1.1 p. 492,
read: "A regular transversal can be slid along the plaques into one of the standard transversals"), so
by holonomy invariance of µ,
  µ(φ^t(B ∩ N)) = µ(pr_{T_{k−1}}(φ^t(B ∩ N))) = µ(h_x(B ∩ N)) = µ(B ∩ N),
the last equality again by holonomy invariance — applied to the *Borel set* B ∩ N, which is legitimate
precisely because holonomy invariance is a statement about all Borel subsets of transversals. This
answers the second attack in the brief: "concentrated on N" is enough exactly because holonomy
invariance is available for arbitrary Borel sets, so it may be applied to B ∩ N.

T is a separable metric space, hence Lindelöf, so T ∩ N is covered by countably many V_{x_n}; disjointify
(B_n := B ∩ V_{x_n} ∖ ⋃_{m<n} V_{x_m}) and add. Hence µ(φ^t(B ∩ N)) = µ(B ∩ N) for every Borel B in every
transversal. Since µ is concentrated on N and φ^t_*µ is concentrated on φ^t(N) = N (P1), this gives
(φ^t_*µ)(B) = µ(φ^{−t}B) = µ(φ^{−t}(B) ∩ N) = µ(φ^{−t}(B ∩ N)) = µ(B ∩ N) = µ(B). ∎

### 1.3 The three attacks, answered

1. *Does the induced transverse map agree with holonomy on a neighborhood or only on N?* **Only on N**,
   and the proof asserts no more. (★) is the precise statement.
2. *Is "concentrated on N" enough given that holonomy invariance quantifies over all Borel sets?* Yes —
   that quantifier is what makes the restriction to B ∩ N legal. The measure of the non-N part is zero by
   hypothesis, and φ^t_*µ is also concentrated on N because N is flow-invariant.
3. *Is uniform continuity in y available?* It is not needed. Joint continuity of the R-action plus the
   tube lemma (P3) is enough, and joint continuity is what [x-20] 7.3 prints. Under *separate* continuity
   the argument would fail; that hypothesis should be stated.

**Verdict (A): STANDS.** The proof closes from the printed hypotheses. Add to the statement: "φ a
continuous R-action (jointly continuous)".

---

## §2. TARGET (B) — STANDS (and is stronger than printed)

**Statement I can prove.** *Let X be a compact foliated space with 2-dimensional oriented leaves, g a
continuous leafwise metric smooth along leaves, λ_g its leafwise area form, and suppose
φ^{t*}[λ_g] = e^t[λ_g] in H̄²_F(X) for all t. Then there is no nonzero positive holonomy-invariant
transverse measure µ with φ^t_*µ = µ. Combined with (A): none concentrated on N.*

### 2.1 The four attacks, answered at the sources

**(a) Does C_µ vanish on the CLOSURE of the leafwise exact forms — i.e. is it continuous for the
topology that defines reduced cohomology?** Yes, and this is the load-bearing point. [x-20] p. 14, read
verbatim: "H̄^n(X, R) = Ker d^n_F / Im d^{n−1}_F. Here the quotient is taken with respect to the
topological closure of Im d^{n−1}_F in the natural Fréchet topology on A^n_F(X)"; and for foliated spaces
p. 29, read: "As before, one also considers the maximal Hausdorff quotient H̄^i(X, R) of this cohomology,
obtained by dividing by the closure of Im d_F in the natural Fréchet topology." The Fréchet topology on
A^n_F(X) is generated by seminorms including the C⁰ sup-norm. Now

  |⟨C_µ, ω⟩| ≤ ‖ω/λ_g‖_∞ · m,  m := ⟨C_µ, λ_g⟩ < ∞ (see (c)),

so C_µ is bounded for the sup-norm, a fortiori continuous for the finer Fréchet topology. A functional
that vanishes on a set and is τ-continuous vanishes on the τ-closure of that set. Hence C_µ kills
cl(Im d_F) and descends to H̄²_F(X). **The continuity comes from a coarser norm than the one defining the
closure, which is why the argument works; had C_µ only been continuous in some finer or unrelated
topology, it would not.** I record this as the step the printed proofs assert without argument.

That C_µ vanishes on Im d_F at all is the closedness of the Ruelle–Sullivan current: the classical
partition-of-unity computation, C_µ(d_F η) = −Σ_i ∫_{T_i} ∫_{P_t} dρ_i ∧ η dµ, in which holonomy
invariance of µ is used to transport all the transversal integrals to a common transversal, where
Σ_i dρ_i = 0. Candel p. 490 prints the resulting statement as an isomorphism: "The Ruelle–Sullivan map
gives an isomorphism between H_p(M, R_F) and the space of invariant transverse measures for M." Note
Candel's H_p = Hom(H^p, R) is the dual of the *un*reduced cohomology, so the printed isomorphism gives
vanishing on Im d_F but not, by itself, the descent to H̄²; the sup-norm bound supplies the rest.

**(b) Is 0 < m < ∞?** *Finite:* take a regular cover U_1, …, U_r with U_i ⊂⊂ V_i (Candel p. 492, read:
"we may assume the cover {U_i, φ_i} is regular … U_i compact ⊂ V_i"); plaques of U_i are relatively
compact and g is continuous, so their λ_g-areas are bounded by a constant A; µ is Radon and the T_i may
be taken relatively compact, so µ(T_i) < ∞; hence m ≤ r · A · max_i µ(T_i) < ∞. *Positive:* µ ≠ 0 means
µ(B) > 0 for some Borel B in some standard transversal T_i; the corresponding plaques have positive
g-area; with a partition of unity {ρ_i} summing to 1 the contributions are non-negative and at least one
is positive. So m > 0. **Compactness of X and continuity of g are both used, and both are hypotheses.**

**(c) Is (15) a statement in reduced cohomology, and does the pairing respect it?** Yes. Leichtnam 2013
(`r3s-20`) §4.1 4], read verbatim: "We have (Frechet) reduced real leafwise cohomology groups H̄^j_{F,K}
(0 ≤ j ≤ 2) … H̄²_{F,K} ≃ R[λ_g] where [λ_g] denotes the class in H̄²_{F,K} of the leafwise kaehler
metric λ_g associated to g. Moreover, we assume that ∀t ∈ R, (φ^t)^*([λ_g]) = e^t[λ_g], (15)". And
[x-20] p. 27, read: "we must have α = 1. This means that the flow φ^{t*} would act by multiplication
with e^t on the one-dimensional space H̄²_F(X)". The pullback φ^{t*} is a continuous map of reduced
cohomology algebras ([x-20] p. 14–15, printed), and pairing is by (a).

**(d) Does the argument need N ≠ ∅, or µ concentrated on N at all?** **No.** The core theorem is
"under φ^{t*}[λ_g] = e^t[λ_g] there is no nonzero *flow-invariant* holonomy-invariant transverse
measure"; (A) is only the device that converts "concentrated on N" into "flow-invariant". If N = ∅ the
statement is vacuous but true. This is a strengthening of the printed statement and should be recorded
as such.

### 2.2 The proof

φ^t is a foliated homeomorphism, so φ^t_*µ is again a holonomy-invariant transverse measure and
(φ^t)_*C_µ = C_{φ^t_*µ} (naturality of Ruelle–Sullivan, immediate from the plaque-wise change of
variables; φ^t preserves the leafwise orientation because det(T_xφ^t|T_xF) is continuous in (t, x),
nonvanishing, and +1 at t = 0). Hence

  ⟨C_µ, φ^{t*}λ_g⟩ = ⟨C_{φ^t_*µ}, λ_g⟩ = ⟨C_µ, λ_g⟩ = m  (by (A): φ^t_*µ = µ),

while by (a) and (15), φ^{t*}λ_g − e^tλ_g ∈ cl(Im d_F) ⊂ ker C_µ, so ⟨C_µ, φ^{t*}λ_g⟩ = e^t m. Thus
(e^t − 1)m = 0 for all t with 0 < m < ∞. Contradiction. ∎

**Two remarks that improve the printed version.** (i) One-dimensionality of H̄²_F is never used; only
the eigenvalue equation. (ii) The degenerate case [λ_g] = 0 needs no separate treatment but is worth
noting: then m = ⟨C_µ, λ_g⟩ = 0 directly, contradicting m > 0 — so under "φ^{t*} = e^t·id on H̄²_F" the
conclusion holds whether or not [λ_g] spans.

**The (0-glob) shadow.** If instead (31) holds globally, φ^{t*}λ_g = e^tλ_g *pointwise*, and no
cohomology is needed: for f = 1 the Ruelle–Sullivan measure obeys m_µ(1 ∘ φ^{−t}) = e^t m_µ(1) by the
leafwise change of variables together with φ^{−t}_*µ = µ, so m = e^t m. Same contradiction.

**Verdict (B): STANDS**, in the strengthened form: *φ^{t*}[λ_g] = e^t[λ_g] in H̄²_F(X) ⇒ no nonzero
flow-invariant holonomy-invariant transverse measure.*

---

## §3. TARGET (C) — STANDS-NARROWED (regularity of g)

### 3.1 The narrowing, stated first

Candel's Theorem 4.1, Corollary 4.2 and Theorem 4.3 are theorems about *a riemannian metric on the
lamination*, and Candel §1.2 p. 492–493 defines that to be a **smooth** section, where "smooth" is his
class C_l^∞: "smooth in the first variable and all its partial derivatives with respect to the first
variable are continuous functions of all the variables" (§1.1 p. 491, read; §1.2 p. 492, read: "A
riemannian metric on the lamination M is a smooth and positive definite section of the bundle S²T*M").
Deninger's leafwise forms and metrics are weaker: [x-20] p. 29, read, "sections are by definition
continuous and smooth on the leaves", and p. 30, **Warning**, read verbatim: "A manifold with a (smooth)
foliation is also a foliated space. However the sheaves R and A^i_F are different in the two contexts:
In the first one demands smoothness also in the transversal direction whereas in the second one only
wants continuity."

**So the printed hypothesis "g a continuous leafwise metric in the conformal class" does not license
Candel's theorems.** (C2) and (C3) must carry "g a riemannian metric on the lamination in Candel's
sense". This costs nothing in practice — every construction in the program produces such a g, and
Leichtnam 1] prints "g denotes a leafwise riemannian metric" — but it must be printed, because the whole
of (C2), (C3), and hence the last step of (D), rests on Candel.

(C1), (C4) and (B) do not need it: they use only continuity of g and compactness of X.

### 3.2 (C1) — N contains no compact leaf. STANDS.

Let L ⊂ N be a compact leaf. *L meets each standard transversal of a regular cover in a finite set.*
L is compact, hence embedded (a continuous bijection from a compact space to a Hausdorff space is a
homeomorphism), so L ∩ U_i is open in L and is a disjoint union of plaques each open in L. If infinitely
many plaques met the compact set L ∩ cl(U_i) ⊂ V_i, a sequence of points in distinct plaques would
converge to some p ∈ L, whose own plaque is an L-neighborhood of p — contradiction. So L ∩ ({z} × T_i)
is finite. Hence counting measure on L is a Radon transverse measure, nonzero, holonomy-invariant
(holonomy preserves leaves), and concentrated on N (L ⊂ N). Excluded by (B). ∎
*The hypothesis "L ⊂ N" is essential and is stated: a compact leaf elsewhere in X is untouched.*

### 3.3 (C2) and (C3) — no euclidean preserved leaf; every preserved leaf hyperbolic. STANDS-NARROWED.

*N is a compact Riemann surface lamination in Candel's sense.* N is closed in X (§1.1 (P1)) and
saturated, so the charts D_i × (T_i ∩ N) satisfy Candel §1.1 verbatim (D_i open in C, transition maps
of the same shape, leafwise holomorphic); N is compact, locally compact, separable, metrizable; the
leaves of N are precisely the leaves of X inside N; g|N is a conformal metric of the same regularity
class as g. Candel p. 496 §3.2, read, notes that a Riemann surface lamination is automatically oriented
("the cover U_i gives M an orientation because jacobian determinants of holomorphic maps are positive"),
which supplies the "oriented" hypothesis of Theorem 4.1.

*N has no nonzero invariant transverse measure.* If ν is one on N, define ν̃(B) := ν(B ∩ N) on
transversals of X. Standard transversals of X meet N in standard transversals of N; holonomy of X
preserves N (saturated) and restricts to holonomy of N; so ν̃ is a nonzero holonomy-invariant transverse
measure of X concentrated on N, excluded by (B). ∎

*Conclusion.* Candel Theorem 4.3 (p. 498, re-extracted by me from the NUMDAM scan, first sentence:
"If χ(M, µ) < 0 for every positive invariant transverse measure µ, then all leaves are hyperbolic
Riemann surfaces") applies to N with vacuous hypothesis — Candel explicitly sanctions the vacuous
reading, p. 497 after Theorem 4.1: "Remark that the theorem includes the case no invariant transverse
measure exists", which is exactly Corollary 4.2. Hence **every leaf of N is a hyperbolic Riemann
surface**, which is (C3) and contains (C2). ∎

*Two notes on the citation.* (i) The printed proofs route (C2) through Theorem 4.3's second sentence
("if L is a euclidean leaf, then there exists µ with support in L̄ and χ(M, µ) = 0"); the NUMDAM OCR
renders that as "support in L" (the bar is lost), and the second sentence also leaves the nonvanishing
of µ implicit. **The route above avoids both problems** and should replace it: it uses only Theorem
4.3's first sentence / Corollary 4.2, applied to N, with the hypothesis vacuously satisfied by (B).
Either reading of the support clause gives supp µ ⊂ N since L ⊂ N and N is closed, so the ambiguity was
harmless — but it need not be relied on. (ii) Candel's unconditional statement at p. 498 §4.1 ("if M
contains a leaf L which is not a hyperbolic Riemann surface, then there is a positive invariant
transverse measure µ with χ(M, µ) ≥ 0") is the honest one-line form of (C2)+(C3) and is worth citing.

### 3.4 (C4) — every invariant transverse measure gives N measure zero. STANDS, with the exact phrasing.

The printed "gives N measure zero" is not a well-formed statement about a transverse measure (a
transverse measure is not a measure on X). The precise statement, which is what the proof gives:

> **(C4)** For every positive holonomy-invariant transverse measure µ of X and every regular
> transversal T of X, µ_T(T ∩ N) = 0.

*Proof.* B ↦ µ(B ∩ N) is a positive holonomy-invariant transverse measure (N is saturated, so holonomy
maps T ∩ N into T′ ∩ N), Radon, concentrated on N; by (B) it is zero. ∎

Equivalently, and more usefully for the trace formula: the Ruelle–Sullivan measure m_µ on X gives N
measure zero, and Connes' χ_Co(F, µ) receives no contribution from N.

**Verdict (C): STANDS-NARROWED.** Binding form: *(C1) and (C4) for any continuous leafwise g; (C2) and
(C3) with g a riemannian metric on the lamination in Candel's regularity class C_l^∞.*

---

## §4. TARGET (D) — STANDS-NARROWED (hypothesis set; one proof step repaired, one shortened)

### 4.1 "Conformal ⇒ holomorphic": right, but only with the orientation argument

(31) restricted to TF|L says g(T_xφ^t v, T_xφ^t w) = e^t g(v, w) for x ∈ L, so T_xφ^t|T_xL is a
similarity of ratio e^{t/2}. A similarity of an oriented 2-plane is C-linear or C-antilinear according
to the sign of its determinant, which here is ±e^t. The function (t, x) ↦ det(T_xφ^t|T_xL) is continuous
on the connected set R × L (the flow is smooth along leaves, [x-20] 7.3), never zero, and equals +1 at
t = 0; hence it is +e^t throughout, and φ^t|L is orientation-preserving, hence **holomorphic**. F's
write-up asserts "orientation-preserving conformal diffeomorphism hence holomorphic" without the
argument; the adjudicator supplies it. I confirm the adjudicator's version and note that **the step is
not free** — a conformal diffeomorphism as such is holomorphic *or antiholomorphic*.

### 4.2 |dφ^t(x_∞)| = e^{t/2}, and why the conformal factor cancels

Write g = ρ²|dz|² in a holomorphic coordinate z near x_∞. For v ∈ T_{x_∞}L,
|(φ^t)′(x_∞)|_{eucl} = |T φ^t v|_{eucl}/|v|_{eucl} = (|Tφ^t v|_g/ρ(x_∞))/(|v|_g/ρ(x_∞)) = e^{t/2},
because φ^t(x_∞) = x_∞ makes the *same* factor ρ(x_∞) appear upstairs and downstairs. **This is exactly
why the modulus of the derivative at a fixed point is an invariant of the conformal class** — it is not
true at a non-fixed point. So the answer to the brief's question is: yes, and the cancellation is the
fixed-point condition, not a property of g. And yes, |T_{x_∞}φ^t| = e^{t/2} is what (31) gives.

### 4.3 The four conformal types

* **Hyperbolic.** Let π: D → L be the universal cover, x̃ over x_∞. φ^t|L is a homeomorphism fixing
  x_∞, so it has a unique lift Φ^t with Φ^t(x̃) = x̃; the corresponding lift Ψ of φ^{−t}|L satisfies
  Ψ ∘ Φ^t = lift of id fixing x̃ = id, so Φ^t ∈ Aut(D) with Φ^t(x̃) = x̃. By the Schwarz lemma applied to
  Φ^t and (Φ^t)^{−1}, |(Φ^t)′(x̃)| = 1; π ∘ Φ^t = φ^t ∘ π and π′(x̃) ≠ 0 give |(φ^t)′(x_∞)| = 1 ≠ e^{t/2}
  for t ≠ 0. **Excluded.**
* **Torus.** Every holomorphic automorphism of C/Λ lifts to z ↦ az + b with aΛ = Λ, so |a| = 1;
  derivative modulus 1 ≠ e^{t/2}. **Excluded.** (This is cleaner than "the identity component has no
  fixed points", and covers automorphisms outside the identity component.)
* **C^\*.** Aut(C^\*) = {z ↦ az} ∪ {z ↦ a/z}. The first has a fixed point in C^\* only for a = 1; the
  second fixes z with z² = a and has derivative −a/z² = −1 there. Modulus 1 in both cases. **Excluded.**
* **Ĉ.** **Correction / improvement to both printed proofs.** They exclude Ĉ by (C1) (compactness),
  which imports (0-coh). It is not needed: a Möbius transformation ≠ id is either parabolic — one fixed
  point, derivative of modulus 1 there (in the coordinate w = 1/z, w ↦ w/(1 + tw) has derivative 1 at 0)
  — or has two fixed points with reciprocal derivatives, whose moduli are r and 1/r. Since **(31) holds
  along all of L, hence at every fixed point of φ^t|L**, both moduli would have to equal e^{t/2} > 1.
  Impossible. **Excluded by (31)-along-L alone.** The adjudicator's parenthetical ("the second fixed
  point … has derivative modulus e^{−t/2}") is the same observation; I promote it from a parenthetical
  to the primary argument, because it removes a dependency.
* **C.** Survives the derivative test (z ↦ x_∞ + a_t(z − x_∞), |a_t| = e^{t/2}), and is killed only by
  (C2): L ⊂ N is a euclidean preserved leaf, impossible under (B). **This is where (0-coh) enters and
  it is the only place it enters.**

### 4.4 The exact hypothesis set

> **(D).** X a compact foliated space whose leaves are Riemann surfaces; g a leafwise metric in the
> conformal class, of Candel's regularity class C_l^∞ (§3.1); φ a foliated flow (continuous R-action,
> leafwise smooth, leaves to leaves); **(0-coh)** φ^{t*}[λ_g] = e^t[λ_g] in H̄²_F(X) (or (0-glob) = (31)
> globally); a fixed point x_∞ with leaf L; and **(31) restricted to TF|L**. Then no such object exists.

So the brief's suspicion is right: **(D) needs BOTH (0-coh) and (31)-along-L**, plus compactness of X
(for m < ∞ in (B), for (C1), and for N to be a *compact* lamination in (C3)) and the Candel regularity
of g. The dependency chart, after §4.3: (31)-along-L alone kills hyperbolic, torus, C^\*, Ĉ; (0-coh) +
compact + Candel kills C.

### 4.5 Consistency with Deninger's own elliptic-curve example — CHECKED AT SOURCE, and it is the sharp boundary case

[x-20] §7.7 and the Example, pp. 34–36, read verbatim by me this session:
* "Translation in the R-variable φ^t[m, t′] = [m, t + t′] defines an F-compatible flow φ on X which is
  everywhere transverse to the leaves of F and **in particular has no fixed points**." (p. 35)
* "The leaves of F are the images in X of the manifolds M̃ × {γ} × {t}" (p. 35) — with M = C/Γ an
  elliptic curve, M̃ = C, so **every leaf is conformally C, a euclidean leaf**.
* "the metric g on TF given by g_{[z,y,t]}(ξ, η) = e^t Re(ξη̄) … **satisfies the conformality condition
  (20) for α = 1**" (p. 36) — i.e. (31) holds *globally*.
* Theorem 7.8 (p. 35) computes with "a certain canonical transverse measure µ" and gives
  χ_Co(F, µ) = χ(M)·l = 0 — so a **nonzero** holonomy-invariant transverse measure exists on this X.

So [De02] is a compact object with (31) globally, α = 1, every leaf euclidean, and a nonzero transverse
measure — and no fixed point. **This is fully consistent with (A)–(D) and it pins down what each of them
does and does not say:**
1. (D) is sharp: delete the fixed point and the theorem is false. The fixed point is what forces
   φ^t|L to have a fixed point of derivative modulus e^{t/2}.
2. (C2) is about leaves **in N** only. Here N = ∅ (no preserved leaves), so the euclidean leaves are not
   a counterexample. Any restatement of (C2) that drops "⊂ N" is false, and [De02] is the witness.
3. (B) is about **flow-invariant** measures only. The canonical µ here is not flow-invariant — the same
   pairing shows m_{φ^t_*µ} = e^t m_µ. Any restatement of (B) that drops flow-invariance is false, and
   [De02] is again the witness.
4. The α = 1 clause is **not** self-contradictory on a compact space. Theorem A must never be quoted as
   "α = 1 is impossible"; it is "α = 1 plus a fixed point plus (31) along its leaf is impossible".

This check should be printed in the ledger as a guard; without it, §16-bis's rulings read as stronger
than they are.

### 4.6 Verdict

**(D): STANDS-NARROWED.** The theorem is true. The narrowing is the hypothesis set of §4.4 (in
particular the Candel regularity, absent from the printed statement) plus the two proof notes of
§4.1 and §4.3. And "Deninger's (31) + α = 1 + fixed point + compact ⇒ no object" is a fair one-line
summary **provided "fixed point" is glossed "a fixed point on a leaf along which (31) holds"**.

---

## §5. TARGET (corA1) — STANDS-NARROWED (the reading of χ)

### 5.1 First half: the flow is not conformal along the archimedean leaf, for any t ≠ 0

Under (0-coh) (+ Candel regularity), L ⊂ N is hyperbolic by (C3). Suppose φ^t|L were a conformal map
of L for some t ≠ 0. Then it is holomorphic or antiholomorphic; by the orientation argument of §4.1 —
which needs only that det(T_xφ^t|T_xL) is continuous, nonvanishing and +1 at t = 0, and does **not**
need (31) — it is holomorphic. By §4.3 (hyperbolic case) |(φ^t)′(x_∞)| = 1. But (0-fix) gives
e^{−t/2}T_{x_∞}φ^t|T_{x_∞}F ∈ SO(2), i.e. T_{x_∞}φ^t is a similarity of ratio e^{t/2}, so by §4.2 the
conformal-class-invariant modulus of the derivative at the fixed point is e^{t/2} ≠ 1. Contradiction. ∎

This is the precise content of Deninger's private "(31) is probably too strong", reported by Leichtnam
2007 p. 11, read verbatim: "Deninger pointed out to us that the condition (4) (φ^t)^*g = e^t g was
probably too strong for being generalized. That is why in Proposition 2.2] we shall replace it by
(φ^t)^*[λ_g] = e^t[λ_g]". Under (0-fix) + (0-coh) the correct word is **inconsistent**, not "too strong".

### 5.2 Second half: "χ = +1 ⇒ the leaf is the hyperbolic disk". Needs a stated reading.

The brief's three questions have sharp answers.

* *Is χ of a non-compact surface well-defined?* Only for surfaces of **finite topological type**, where
  χ(L) = 2 − 2g − n (g the genus, n the number of ends/punctures). For infinite genus or infinitely many
  ends there is no finite χ, and clause (iii)'s "nonzero Euler characteristic" says nothing.
* *Does χ = +1 force simple connectivity?* Among finite-type surfaces, 2 − 2g − n = 1 forces
  2g + n = 1, i.e. g = 0, n = 1: L ≈ R². So yes — **within the finite-type reading**, and only there.
* *What does clause (iii)'s "nonzero Euler characteristic" mean for a non-compact leaf?* The reading
  under which the corollary holds:

> **Reading (iii)′.** Clause (iii)'s leaf L is of finite topological type and χ(L) := 2 − 2g(L) − n(L).
> Under (0-coh) L is non-compact (C1) and hyperbolic (C3); if in addition χ(L) = +1 then L ≈ R² and,
> being hyperbolic and simply connected, L is conformally the unit disk D (uniformization).

Two further remarks. (a) χ(L) = +2 (the sphere) is excluded by (C1) under (0-coh) — this is where the
old A-II route went, and it is why "χ = +1" and not "χ > 0" is the live case. (b) The provenance of
"χ = +1" in the program is Poincaré–Hopf with a single index-+1 zero; on a *non-compact* leaf
Poincaré–Hopf does not apply without control at the ends, so **χ = +1 is not derivable from (0-fix)
plus "one fixed point per leaf"** — it is a reading of clause (iii), i.e. a hypothesis. The corollary is
therefore conditional, and must be printed as conditional.

**Verdict (corA1): STANDS-NARROWED**, with Reading (iii)′ printed alongside.

---

## §6. TARGET (B1′) — STANDS-NARROWED (three corrections, one of them substantive)

### 6.1 Does KMNT's ω exist on M ∖ N without transverse simplicity? YES — verified in KMNT's own proof

KMNT (arXiv:1906.02424, text read on disk this session) Definition 1.5 defines an FDS³ by (1) M a
connected closed smooth 3-manifold, (2) F a complex foliation by Riemann surfaces, (3) φ a smooth flow,
plus (i) "there are finite number of compact leaves L^∞_1, …, L^∞_r, which may be empty, such that for
any i and t we have φ^t(L^∞_i) = L^∞_i and that any orbit of the flow φ is transverse to leaves in
M ∖ ∪L^∞_i", and (ii) each φ^t maps leaves to leaves. **Lemma 1.10, read verbatim:** "For an FDS³
S = (M, F, φ), there is the unique closed smooth 1-form ω on M_0 satisfying (C) ω|TF = 0, ω(φ̇^t) = 1.
More precisely, let (M, F, φ) be a triple satisfying (1), (2), (3) and (i) in Definition 1.5. Then there
is the unique smooth 1-form ω on M_0 satisfying (C), and the condition (ii) is equivalent to that ω is
closed."

Reading the proof: uniqueness/existence uses only that on M_0 the flow is transverse to F, so that in a
foliated chart ω|U = h(z,t)dt with h determined by ω(φ̇) = 1; closedness uses only (ii), via the
flow-box coordinates "φ^s(z, t) = (z, t + s)" whose existence needs only transversality on the open set.
**Compactness of the leaves in N is never used, and neither is anything resembling transverse
simplicity.** So B1′'s step (1) is legitimate: the ω exists on M_0 = M ∖ N whenever the flow is
transverse to F on M_0 and maps leaves to leaves. Definition 1.11 supplies the period homomorphism
[ω_S]: H_1(M_0; Z) → R and the period group Λ_S = im[ω_S]. Both read verbatim.

*Regularity note.* KMNT assume smooth data; B1′ states C¹. With C¹ F and φ the form ω is only
continuous, so "dω = 0" must be read as "ω is locally exact" — which is exactly what KMNT's proof
produces (ω|U_i = dt_i in the flow-box charts). That still defines a class in H¹(M_0; R) and a period
homomorphism, so the argument survives; but the C¹ statement should say "locally exact", not "closed".

### 6.2 Which N? The statement must use the TANGENCY set

B1′ says "N its non-transverse set", and its proof says "On M_0 the flow is transverse to F". Those two
are compatible only if N ⊇ {x : Y_φ(x) ∈ T_xF}. Elsewhere in the pass (and in `refute-adjudication.md`
§3.2, correctly) N is *defined* as the union of the preserved leaves, which is in general a **proper
subset** of the tangency set: a single tangency point whose orbit leaves L_x is in the tangency set and
in no preserved leaf. If N is the union of preserved leaves, M ∖ N can contain tangency points and
KMNT's ω does not exist there. **The hypothesis repairs this**: if the tangency set is a finite union of
leaves, then along each such leaf Y_φ ∈ TF everywhere, so orbits through it stay in it and it is
preserved; conversely every preserved leaf is in the tangency set. So under B1′'s own hypothesis the two
definitions coincide — but the statement must say which set it is assuming to be a finite union of
leaves, and it must be the tangency set.

### 6.3 Which closed orbits? Only those transverse to F

**As printed, "the group Λ generated by the lengths of the closed orbits of φ" is not what the proof
bounds.** A closed orbit meeting N lies entirely in N (§1.1 (P1)), and its length is invisible to ω on
M_0. Nothing in the hypotheses forbids a preserved leaf carrying closed orbits of many incommensurable
periods. The correct statement bounds Λ_{M_0} = ⟨ℓ(c) : c a closed orbit contained in M_0⟩ = ⟨ℓ(c) : c a
closed orbit transverse to F⟩.

*For the S4′ application this costs nothing, and I can close the gap:* under clause (ii), each γ_P is
transverse to F. Indeed if γ_P ⊂ L for a leaf L, then Y_φ(x) ∈ T_xF for x ∈ γ_P and
T_xφ^{ℓ}(Y_φ(x)) = Y_φ(x), so T_xφ^{ℓ}|T_xF has the eigenvalue 1; but clause (ii) (Leichtnam (14),
read: e^{−(log NP)/2}D_yφ^{log NP}(x̃)|T_x̃F ∈ SO₂) makes both eigenvalues of modulus NP^{1/2} ≠ 1.
Contradiction. Together with clause (i) in its "exactly" form (the γ_P are *all* the closed orbits),
Λ = Λ_{M_0} = ⟨log NP⟩ and the kill goes through.

### 6.4 "Finitely generated" is NOT what the proof gives — it gives FINITE RANK

The proof bounds dim_Q H_1(M_0; Q) < ∞ and concludes "Λ is finitely generated". **That inference is
invalid.** Λ ⊂ R is the image of H_1(M_0; Z) → R; it is torsion-free and lies in the Q-subspace
[ω](H_1(M_0; Q)) of R, of dimension ≤ dim_Q H_1(M_0; Q) < ∞. But a subgroup of R lying in a
finite-dimensional Q-subspace need **not** be finitely generated — Z[1/2] ⊂ Q is rank 1 and not finitely
generated — and H_1 of an open 3-manifold can be infinitely generated. So the derivable conclusion is:

> **B1′ (corrected).** …then the group Λ_{M_0} generated by the lengths of the closed orbits of φ that
> are transverse to F has **finite rank**: dim_Q (Λ_{M_0} ⊗ Q) ≤ dim_Q H_1(M_0; Q) < ∞.

**The S4′ kill is untouched and is in fact cleaner in this form:** {log p : p prime} is Q-linearly
independent (unique factorization), so it spans an infinite-dimensional Q-subspace of R and cannot lie
in a finite-dimensional one. The contradiction is a dimension count, not a generation count. Every
downstream use ("the closed-orbit length group is finitely generated", S16-3; "the period group … is
finitely generated", §16-bis) must be reworded to "has finite rank".

### 6.5 The rest of the proof, re-derived

* **(2) Double cover.** M orientable alone does **not** make a leaf two-sided: a non-orientable properly
  embedded surface in an orientable 3-manifold is one-sided. Pass instead to the **transverse
  orientation double cover** (and the orientation cover if needed): there every leaf is two-sided with
  trivial normal bundle. Lifted closed orbits have length ℓ or 2ℓ, so Λ ⊂ ½Λ′; a subgroup of a
  finite-rank group has finite rank, so finite rank descends. The flow lifts because R is simply
  connected; the tangency set lifts to a finite union of leaves.
* **(3) Some leaf of N_k is closed in W_k.** Among the leaves of N_k = N ∩ W_k choose L_a with
  cl_{W_k}(L_a) minimal for inclusion. Closures of saturated sets are saturated, so if
  cl(L_a) ⊋ L_a there is a leaf L_b ⊂ cl(L_a), b ≠ a, with cl(L_b) ⊆ cl(L_a); minimality gives
  cl(L_b) = cl(L_a) =: K, in which both L_a and L_b are dense. K is closed in the locally compact W_k,
  hence a Baire space, and is a *countable* union of compact plaques (each leaf meets each chart in
  countably many plaques, finitely many leaves), so some plaque P ⊂ L_c has nonempty interior V in K.
  V meets the dense L_a and the dense L_b, and V ⊂ L_c, so a = c = b. Contradiction. Hence
  cl_{W_k}(L_a) = L_a: L := L_a is closed in W_k, hence properly embedded, hence (after 2) two-sided with
  a tubular neighborhood ν ≅ L × (−1, 1). *(This is the printed argument; the two write-ups garble the
  order — F/adjudicator introduce a preorder ≼ whose minimal element already yields the contradiction in
  one line, making the Baire step look redundant. Ordering by closure-inclusion, as above, is what
  actually needs Baire.)*
* **(4) Mayer–Vietoris** for W_k = (W_k ∖ L) ∪ ν, (W_k ∖ L) ∩ ν ≃ L ⊔ L, Q-coefficients:
  H_1(L)² → H_1(W_k ∖ L) ⊕ H_1(L) → H_1(W_k) exact gives
  dim H_1(W_k ∖ L) + dim H_1(L) ≤ dim H_1(W_k) + 2 dim H_1(L), i.e.
  dim H_1(W_k ∖ L) ≤ dim H_1(W_k) + dim H_1(L). ✓
* **(5)** dim_Q H_1(M_0; Q) ≤ dim_Q H_1(M; Q) + Σ_a dim_Q H_1(L_a; Q) < ∞ (M closed ⇒ finite). ✓

### 6.6 The necessary condition

Unchanged in substance: for a closed 3-manifold to carry S4′ (i) + (ii) with tangency set N a finite
union of leaves, one needs **dim_Q H_1(M ∖ N; Q) = ∞** — so N has infinitely many leaves or a leaf of
infinite topological type. The disk (H_1 = 0) is finite-type, so "one plane/disk leaf plus finitely many
others of finite type" is dead on a closed 3-manifold, independently of Theorem A.

**Verdict (B1′): STANDS-NARROWED**, in the form of §6.4 with the qualifications of §6.2, §6.3, §6.5.

---

## §7. TARGET (ε) — STANDS. The 2×2 algebra, written out.

### 7.1 What ε_x is, read off Deninger's own equations

[x-20] p. 31, working hypothesis 7.5 and the display after it, read verbatim: "The distributions W_x on
R^\* are given by: W_x|_{R>0} = ε_x|1 − e^{κ_x t}|^{−1} and
W_x|_{R<0} = ε_x det(−T_xφ^t | T_xF) |1 − e^{κ_x|t|}|^{−1}." Remark 7.6(2), same page, read verbatim,
supplies where these come from: "Since Y_{φ,x} = 0, they should be given by:
det(1 − T_xφ^t | T_xF) / |det(1 − T_xφ^{|t|} | T_xX)| = W_x."

T_xF is T_xφ-invariant and the induced action on the 1-dimensional T_xX/T_xF is multiplication by
e^{κ_x t} (this is what κ_x means; Leichtnam 2013 7]/8], read: Ψ(v e^{−2t}) = φ^t(Ψ(v)) at a real place,
Ψ(v e^{−t}) = φ^t(Ψ(v)) at a complex place). Hence the determinant is block-triangular:

  det(1 − T_xφ^{|t|}|T_xX) = det(1 − T_xφ^{|t|}|T_xF) · (1 − e^{κ_x|t|}).

Substituting into 7.6(2), for t > 0:

  W_x = [det(1 − T_xφ^t|T_xF) / |det(1 − T_xφ^t|T_xF)|] · |1 − e^{κ_x t}|^{−1},

so comparing with the printed W_x|_{R>0}:

  **ε_x = sign det(1 − T_xφ^t | T_xF)  (t > 0).**

**It is the sign of det(1 − T_xφ^t) on the LEAF tangent space**, the normal direction having been split
off into the factor |1 − e^{κ_x|t|}|^{−1}. (Consistency check on R<0: for t = −s < 0, in dimension 2,
det(1 − T_xφ^{−s}) = det(T_xφ^{−s})·det(1 − T_xφ^{s}), which reproduces exactly Deninger's
W_x|_{R<0} = ε_x det(−T_xφ^t|T_xF)|1 − e^{κ_x|t|}|^{−1} since det(−A) = det(A) for 2×2 A.)

### 7.2 The explicit formula FORCES both ε_x = +1 and det = e^t (not merely "fits")

[x-20] p. 10, read verbatim: for p | ∞, "If φ has support in R_{>0} then W_p(φ) = ∫ φ(t)/(1 − e^{κ_p t}) dt
where **κ_p = −1 if p is complex and κ_p = −2 if p is real**. If φ has support on R_{<0} then
W_p(φ) = ∫ φ(t)/(1 − e^{κ_p|t|}) e^t dt." Since κ_p < 0, for t > 0 we have 1 − e^{κ_p t} ∈ (0, 1), so the
archimedean coefficient on R_{>0} is **positive**: matching W_{x_p} = W_p forces **ε_x = +1**. On R_{<0}
the coefficient is +e^t, so with ε_x = +1 matching forces **det(T_xφ^t|T_xF) = e^t**. Deninger's p. 32
sentence "This fits perfectly with the explicit formula (6) if all ε_{γp}(k) = 1 and ε_{x_p} = 1" states
sufficiency; the sign of κ_p makes it **necessary**. So the adjudicator's §1.1 correction to refuter O is
right, and is stronger than it claims.

### 7.3 The linear algebra

Write T_xφ^t|T_xF = exp(tB), B ∈ M_2(R) the leafwise linearization of the vector field at x. Then
det = e^{t·tr B}, so **det = e^t ⟺ tr B = 1**; and ε_x = sign det(1 − e^{tB}) for t > 0. Let λ, µ be the
eigenvalues of B, λ + µ = 1.

| case | det(1 − e^{tB}), t > 0 | ε_x | verdict |
|---|---|---|---|
| λ > 0 > µ (**saddle**, e.g. O's diag(2, −1)) | (1 − e^{λt})(1 − e^{µt}) = (neg)(pos) < 0 | **−1** | **EXCLUDED** |
| λ, µ > 0 real distinct (**source**) | (neg)(neg) > 0 | +1 | admitted |
| λ = µ = ½, B = ½I + N nilpotent (**source**) | det((1 − e^{t/2})I − te^{t/2}N) = (1 − e^{t/2})² > 0 | +1 | admitted |
| λ, µ = ½ ± ib (**spiral source**) | (1 − e^{λt})(1 − e^{λ̄t}) = \|1 − e^{λt}\|² > 0 | +1 | admitted |
| λ, µ < 0 (**sink**) | (pos)(pos) > 0 | +1 | admitted by ε_x, **excluded by tr B = 1** |
| λ = 0 | 0 | undefined | excluded by non-degeneracy (7.5) |

λ + µ = 1 makes "both real, both negative" impossible, so the only surviving configurations are those
with **Re λ, Re µ > 0: a leafwise hyperbolic SOURCE**. Both conditions are needed: ε_x = +1 alone admits
the sink; det = e^t alone admits the saddle. ∎

**They do not force the SO(2) form.** B = diag(1/4, 3/4) has tr B = 1 and det(1 − e^{tB}) > 0 for t > 0,
so det = e^t and ε_x = +1, yet e^{−t/2}exp(tB) = diag(e^{−t/4}, e^{t/4}) ∉ SO(2). So (0-fix)'s SO(2)
clause is strictly stronger than what the explicit formula forces, and A-II's use (both real parts
positive ⇒ index +1 source ⇒ isolated zero) is the part that is forced. Conversely, under (31) the SO(2)
form is a theorem, not an axiom: [x-20] p. 33 Fact, read verbatim — "For fixed points, ε_x = 1 is
automatic and we have: T_xφ^t = e^{t/2}O_t for O_t ∈ SO(T_xF)" — because a similarity of ratio e^{t/2}
with positive determinant is e^{t/2}·SO(2), and then det(1 − e^{t/2}O_t) = |1 − e^{t/2}e^{iθ}|² > 0.

**Verdict (ε): STANDS.** O's sentence "the archimedean term compels only det = e^t, which a saddle
satisfies" is wrong by the ε_x half, exactly as the adjudicator says.

---

## §8. WHAT THIS DOES TO LEDGER §16-bis's PROVISIONAL LABELS

§16-bis states: *"the adjudicator writes 'dual-checked' for Theorem A = refuter F's F-1 (A)–(D),
Corollary A.1 and B1′; those were derived by Fable 5.1 (refuter F) and re-derived by Fable 5.1 (the
adjudicator) — two passes on ONE model. They are enacted PROVISIONALLY here and become binding only
after the Opus 5 check launched as stream (c″)."* This is that check. Its disposition, item by item.

### 8.1 What becomes BINDING as written

* **Theorem A(A)** — "every positive holonomy-invariant transverse measure concentrated on N is
  flow-invariant". **BINDING.** Add to the hypothesis list: "φ a jointly continuous R-action".
* **Theorem A(B)** — **BINDING**, and may be strengthened: replace "Under (0-coh) no nonzero such µ
  exists" by *"φ^{t*}[λ_g] = e^t[λ_g] in H̄²_F(X) ⇒ there is no nonzero flow-invariant holonomy-invariant
  transverse measure; with (A), none concentrated on N."* One-dimensionality of H̄²_F is not used.
* **Theorem A(C1), A(C4)** — **BINDING** (C4 in the phrasing of §8.2 below).
* **Theorem A(D)** — **BINDING** with the hypothesis set of §4.4 printed.
* **Corollary A.1**, first half ("the flow is not conformal along the archimedean leaf for any t ≠ 0") —
  **BINDING.**
* **The ε_x correction to refuter O** (§1.1 of `refute-adjudication.md`) — **BINDING**, and upgraded:
  the archimedean term does not merely "fit" with ε_x = +1, it **forces** it, because κ_p < 0
  ([x-20] p. 10). ε_x = sign det(1 − T_xφ^t|T_xF), on the leaf.
* **Everything already labeled dual-model (Fable + Opus) and BINDING** in §16-bis is untouched by this
  pass; I re-derived N's closedness (§1.1 (P1)) and confirm §3.2 of the adjudication independently.

### 8.2 Sentences that must be NARROWED, with exact wording

**(N-1) The "Verification labels" paragraph of §16-bis.** Replace the last sentence
("They are enacted PROVISIONALLY here and become binding only after the Opus 5 check launched as stream
(c″) (`results/c3-r/s16/qs4prime/f1-check-O.md`).") by:

> [ENACTED 2026-09-06, `f1-check-O.md` — Opus 5, second model.] The Opus check re-derived all seven
> items from the printed hypotheses and the primary sources. Nothing falls. Theorem A(A), A(B), A(C1),
> A(C4), A(D), Corollary A.1 (first half) and the ε_x correction are now **dual-model and BINDING**;
> A(B) is binding in the strengthened form (only φ^{t*}[λ_g] = e^t[λ_g] is used). Theorem A(C2), A(C3),
> A(D) and Corollary A.1 additionally require **g to be a riemannian metric on the lamination in
> Candel's regularity class** (leafwise smooth, all leafwise derivatives continuous in all variables,
> Candel §1.1–1.2 pp. 491–493) — Deninger's A^•_F asks only for transverse continuity ([x-20] p. 30,
> Warning), so the weaker phrase "continuous leafwise metric" does not license Candel's theorems.
> Corollary A.1's second half is conditional on Reading (iii)′ (below). **B1′ is narrowed: it gives
> finite RANK, not finite generation.**

**(N-2) S16-3, the B1′ clause.** Replace
"(B1′: on a closed 3-manifold the period group is finitely generated whenever N is a finite union of
leaves with finite-rank H₁; dual-checked, refuter F + binding adjudicator)" by:

> (B1′ [NARROWED 2026-09-06, `f1-check-O.md` §6]: on a closed 3-manifold, if the **tangency set**
> N = {x : Y_φ(x) ∈ T_xF} is a finite union of leaves each with dim_Q H₁ < ∞, then the group generated by
> the lengths of the closed orbits **transverse to F** has **finite rank**, dim_Q(Λ ⊗ Q) ≤
> dim_Q H₁(M ∖ N; Q) < ∞. "Finitely generated" is not derivable — a finite-rank subgroup of R need not be
> finitely generated. The kill of S4′ (i)+(ii) is a dimension count: {log p} is Q-linearly independent.
> Closed orbits *inside* N are not controlled by the argument; under clause (ii) there are none, because
> an orbit inside a leaf gives T_xφ^ℓ|T_xF the eigenvalue 1 while (ii) makes both eigenvalues of modulus
> NP^{1/2}. Dual-model: refuter F + binding adjudicator (Fable), re-derived by Opus 5.)

Likewise in §16-bis's S16-3 block, "the period group is finitely generated" → "the period group has
finite rank"; and in S16-3's headline sentence "The closed-orbit length group of a foliated flow on a
closed 3-manifold whose non-transverse set is a finite union of compact leaves is finitely generated" —
that KMNT-based sentence is about compact leaves and is not what B1′ generalizes; leave it, but append
"(for the finite-type generalization the derivable conclusion is finite rank, not finite generation —
§16-bis (N-2))".

**(N-3) S16-4, the (0-coh) sentence.** Replace
"For S4′ + (0-coh): no compact preserved leaf exists, every preserved leaf is a hyperbolic Riemann
surface, clause (iii)'s leaf is the hyperbolic disk if χ = +1, and the flow is not conformal along it for
any t ≠ 0 (Theorem A, Corollary A.1, dual-checked)." by:

> For S4′ + (0-coh), with g in Candel's regularity class: no compact preserved leaf exists, every
> preserved leaf is a hyperbolic Riemann surface, every holonomy-invariant transverse measure of X gives
> every transversal's intersection with N measure zero, and the flow is not conformal along the
> archimedean leaf for any t ≠ 0 (Theorem A, Corollary A.1; dual-model, `f1-check-O.md`). **Reading
> (iii)′, required for the disk:** clause (iii)'s "nonzero Euler characteristic" is read as "L is of
> finite topological type and χ(L) = 2 − 2g − n"; then χ(L) = +1 forces L ≈ R², and hyperbolic + simply
> connected gives L ≅ D. For a leaf of infinite type χ is undefined and clause (iii) says nothing.

**(N-4) S16-4, the (31) sentence — keep, and gloss.** "on a compact space, (31) along the fixed point's
leaf together with α = 1 is inconsistent (Theorem A(D), dual-checked)" stands; append:

> [Opus 5, 2026-09-06.] The full hypothesis set is: X compact, Riemann-surface-leaved, g in Candel's
> class; (0-coh) (or (0-glob)); a fixed point x_∞ with leaf L; and (31) on TF|L. Both ingredients are
> needed and each does distinct work: (31)-along-L alone excludes the hyperbolic, torus, C^\* **and Ĉ**
> cases (Ĉ by the second fixed point of a Möbius one-parameter group, whose derivative modulus is the
> reciprocal — so (C1) and hence (0-coh) are **not** needed there, contrary to the printed proofs);
> (0-coh) + compactness + Candel is needed only to exclude L ≅ C.

**(N-5) S16-5 and S16-6, "measure zero".** "it has invariant-transverse-measure zero" (S16-5) and
"it gives the non-transverse set N measure zero" (S16-6) are not well-formed for a transverse measure.
Replace both by: *"for every holonomy-invariant transverse measure µ of X and every regular transversal
T, µ(T ∩ N) = 0; equivalently the Ruelle–Sullivan measure of µ gives N measure zero, so N contributes
nothing to χ_Co(F, µ)."*

**(N-6) S16-6, the existence half.** The strike stands. Add the reason in one line: *the only printed
route to existence is Candel via a non-hyperbolic leaf, and under (0-coh) every preserved leaf is
hyperbolic (Theorem A(C3)) — while a non-preserved non-hyperbolic leaf, which does produce a measure, is
consistent and in fact occurs in Deninger's own example (§8.3).*

### 8.3 A guard that must be added to the ledger — [De02] is the sharp boundary case

Ledger §16-bis nowhere records that Deninger's solved case satisfies the α = 1 clause **and** (31)
globally **and** has euclidean leaves **and** carries a nonzero transverse measure — on a compact space.
Read at source ([x-20] pp. 34–36): the flow there "is everywhere transverse to the leaves of F and in
particular has no fixed points"; the leaves are images of C; g = e^t Re(ξη̄) "satisfies the conformality
condition (20) for α = 1"; Theorem 7.8 uses "a certain canonical transverse measure µ". Proposed
sentence for §16-bis:

> [GUARD, Opus 5, 2026-09-06.] Deninger's solved case [De02] = [x-20] §7.7 Example is a **compact** object
> satisfying (31) globally with α = 1, all of whose leaves are conformally C, carrying a nonzero
> holonomy-invariant transverse measure — and with **no fixed point** (p. 35, verbatim). It is therefore
> consistent with Theorem A and pins its scope: (C2) forbids euclidean leaves only **inside N**; (B)
> forbids only **flow-invariant** measures; (D) is false without the fixed point. Theorem A must never be
> paraphrased as "α = 1 is impossible on a compact space": what is impossible is α = 1 together with a
> fixed point on a leaf along which (31) holds.

### 8.4 Consequence for S16-8's re-posed gate

Unchanged in substance. Two refinements: (i) the manifold half should read "rank_Q H₁(M ∖ N; Q) = ∞"
(§6.4/§6.6), with N the tangency set; (ii) the hyperbolic-disk leaf in the corridor is conditional on
Reading (iii)′, so the gate should say "a leaf of finite type with χ = +1, i.e. conformally D".

---

## §9. HONESTY — read versus recalled

**Read on disk or extracted by me in this session (all with `pdftotext` from the PDFs named):**
* [x-20] = Deninger 2005, `fetched/x-20-…pdf`: pp. 3–13 (the explicit formula and κ_p = −1/−2), pp. 14–20
  (definition of H̄^n as the quotient by the *closure* of Im d_F in the Fréchet topology; pullbacks),
  pp. 25–28 (Corollary 5.5, (28), the dictionary, p. 26 "very desirable", p. 27 α = 1 and (31)),
  pp. 29–32 (7.2, 7.3, 7.5, the Warning on p. 30, W_x, Remarks 7.6(2)(4)(5)), pp. 33–36 (the Fact,
  Remark 7, §7.7, Theorem 7.8, the elliptic-curve Example). Every quotation in this file from [x-20] was
  re-extracted by me this session, not copied from the earlier passes.
* **Candel**, *Uniformization of surface laminations*, ASENS (4) 26 (1993): the NUMDAM scan on disk
  (`candel.pdf` in the session scratchpad). Re-extracted by me: the introduction (p. 490, the two
  uniformization theorems and the Ruelle–Sullivan sentence), §1.1–1.2 pp. 491–493 (laminations,
  transversals, holonomy, regular covers, C_l^∞ smoothness, riemannian metric as a *smooth* section),
  §3.2 pp. 496–497 (Riemann surface lamination; automatic orientation; conformal metrics), and
  pp. 497–498 (Theorem 4.1, Corollary 4.2, §4.1's unconditional sentence, Theorem 4.3). **I did not
  re-fetch from NUMDAM** — the open-access scan was already on disk from an earlier session; I verified
  it is the NUMDAM PDF (metadata: Creator NUMDAM, Author Alberto Candel) and re-ran the extraction
  myself rather than reading the earlier session's dump.
* **KMNT** = Kim–Morishita–Noda–Terashima, arXiv:1906.02424, text on disk: Definition 1.5, (1.6),
  Lemma 1.10 **with its proof**, Definition 1.11, Lemma 1.12, Theorem 2.2.2 and Remark 2.2.3.
* **Leichtnam 2013** (`r3s-20`) §4.1: Assumptions 1], 2], 3]a (13), 3]b (14), 4] (15), 5], 7], 8],
  Comment 6, and (12) the explicit formula. **Leichtnam 2007** (`r3s-21`): the "too strong" passage.
* `refute-F.md` §1.5, §3.4; `refute-adjudication.md` §0, §1.1–1.5, §3.4; ledger §15, §16, §16-bis.

**Recalled, not re-verified at a source (and load-bearing where marked):**
* The uniformization theorem; Aut(D), Aut(Ĉ) = PSL(2, C), Aut(C), Aut(C^\*), Aut(C/Λ); the Schwarz
  lemma. *(Load-bearing in §4.3, §5.1.)*
* The Ruelle–Sullivan partition-of-unity computation showing C_µ vanishes on Im d_F. *(Load-bearing in
  §2.1(a). Candel p. 490 prints the resulting isomorphism, which is the statement, not the proof.)*
* Baire category for locally compact Hausdorff spaces; Mayer–Vietoris; the tubular neighborhood theorem
  for a C¹ properly embedded two-sided submanifold; the tube lemma; "a connected metric space with more
  than one point is uncountable"; a subgroup of a finite-rank torsion-free abelian group has finite rank;
  Z[1/2] is rank 1 and not finitely generated; {log p} is Q-linearly independent by unique factorization.
  *(All standard; the Z[1/2] fact is what breaks B1′'s "finitely generated".)*
* That the Fréchet topology on A^n_F(X) has the C⁰ sup-norm among its seminorms. Deninger says "the
  natural Fréchet topology" without listing the seminorms; **this is the one place where I rely on the
  standard reading of an unspecified phrase**, and §2.1(a) depends on it. If that topology were defined
  by seminorms not dominating the sup-norm, C_µ's descent to H̄²_F would need a separate argument. I flag
  it rather than hide it; every construction of leafwise Fréchet topologies in the literature (Deninger's
  own Theorem 5.4 estimates included) uses uniform convergence of leafwise derivatives, which contains
  the sup-norm.
  **[Session 17, 2026-09-06: reliance closed — as printed for foliated manifolds; narrowed to one named source
  for foliated spaces.** Report: `f1-check-C0-seminorm-s17.md` (same directory). Replacement sentence:
  "That the Fréchet topology on A^n_F(X) has the C⁰ sup-norm among its seminorms — PRINTED for foliated
  manifolds: Deninger's 'natural Fréchet topology' is the C^∞ topology of C^∞(M; ΛF) (ÁLKL memoir
  arXiv:2402.06671v2 §1.1 p. 1, §2.1.4 p. 11 with the seminorms (2.1.2) p. 10, §3.2.1 p. 82; ÁLKL
  arXiv:1905.12912v3 §2.1 p. 4, §4.10.1 p. 23), and on compact M its defining seminorms ‖·‖_{C^m}
  (= ‖·‖_{C^m_ub}) begin with the sup-norm ‖·‖_{C^0} = sup_M |u| (arXiv:1905.12912v3 §3.2 p. 11: 'if M is
  compact, then the C^m_ub topology is just the C^m topology'; memoir §2.4.3 p. 28). For foliated spaces
  (Deninger p. 29) the same family with leafwise derivatives only is Moore–Schochet 1988 Ch. II (Deninger's
  [33]), not on disk — that half remains recalled, now with a named printed source." Nothing in §2.1(a)
  changes.]

**Not checked, and out of scope:** Leichtnam 2008 §5.1 (the adjudicator's reading is not among my
targets); ALKL's memoir; the claim that Leichtnam prints no compactness for S_K; Duminy and Hurder
Problem 5.4.
