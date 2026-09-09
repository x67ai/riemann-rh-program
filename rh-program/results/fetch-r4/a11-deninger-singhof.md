# Round-4 ingest report — agent a11-deninger-singhof (Session 18, 2026-09-09)

**File:** `fetched-r4/r4-05-contemp-math-290-2001-VOLUME-deninger-singhof-note-dynamical-trace-formulas-pp41-55.pdf`
(27.2 MB, 210 PDF pages, tiff2pdf image-only, no text layer; read by rendering with `pdftoppm -r 110` and vision).

**List item:** 5 (P2). C. Deninger, W. Singhof, *A note on dynamical trace formulas*, in *Dynamical, Spectral, and
Arithmetic Zeta Functions* (San Antonio 1999), Contemp. Math. 290, AMS 2001, pp. 41–55 (MR1868467).

**Flagged at:** `results/c3-r/s16/novelty/adjudication.md` §4 item 1 (and §1 N-A items 2, 5); sweep-F.md line 134;
`FETCH-LIST-ROUND4.md` item 5. Cross-reference: `results/fetch-r4/a01-12-warsaw.md` (ALK 2002 cites this note as
"[11] manuscript, 2000" and says the Deninger ICM-98 conjecture "under some additional assumptions … was proved in [11, 18]").

Status: COMPLETE (see §6).

## §1. Identity verification (read by vision, PDF pp. 1–12)

- **PDF p. 1** (cover): "CONTEMPORARY MATHEMATICS 290 — Dynamical, Spectral, and Arithmetic Zeta Functions — AMS Special
  Session on Dynamical, Spectral, and Arithmetic Zeta Functions, January 15–16, 1999, San Antonio, Texas — Michel L.
  Lapidus, Machiel van Frankenhuysen, Editors — American Mathematical Society".
- **PDF p. 6** (title page): same, "Providence, Rhode Island".
- **PDF p. 7** (copyright page): Editorial Board Dennis DeTurck (managing), Andreas Blass, Andy R. Magid, Michael
  Vogelius. "This volume contains the proceedings of the AMS Special Session on Dynamical, Spectral, and Arithmetic
  Zeta Functions held at the Annual Meeting of the American Mathematical Society in San Antonio, Texas on January
  15–16, 1999." 2000 MSC Primary 11F67, 11Mxx, 11Y35, 11N05, 28A80, 30F40, 37Axx, 58J35. LC CIP: "(Contemporary
  mathematics, ISSN 0271-4132 ; 290) … ISBN 0-8218-2079-6 (alk. paper) … QA351.A73 1999, 515′.56—dc21, 2001053944".
  "© 2001 by the American Mathematical Society." Print line "10 9 8 7 6 5 4 3 2 1  06 05 04 03 02 01".
- **PDF p. 8** (Contents, printed p. vii): lists "A note on dynamical trace formulas — Christopher Deninger and
  Wilhelm Singhof — 41" (full TOC transcribed in §4).
- **PDF p. 10–11** (Preface, printed pp. ix–x, dated July 2001, signed Lapidus and van Frankenhuysen): "The volume
  consists of eleven papers, seven of which were presented at the meeting." Contributor affiliations: Deninger,
  Mathematisches Institut, WWU Münster; Singhof, Mathematisches Institut, Universität Düsseldorf.
- **PDF p. 12** = printed p. 1 (Chang–Mayer, running head "Contemporary Mathematics Volume 290, 2001").
- **Offset: PDF page = printed page + 11.** Deninger–Singhof printed pp. 41–55 = **PDF pp. 52–66**.
- Text layer: **NONE** (image-only, tiff2pdf). All quotations below transcribed by vision from 110-dpi renders.
- Match to the list citation: **EXACT** — volume, number (290), year (2001), publisher, editors, San Antonio 1999,
  and page range 41–55 (confirmed from the TOC and from the article's first/last pages, see §3).

## §2. What the program asked for (quoted from the flagged passages)

`results/c3-r/s16/novelty/adjudication.md` §4 item 1: "The likeliest printed home of a proof of the α = 0 remark. …
Value: MEDIUM (would settle whether the (B)-mechanism is printed anywhere in the manifold case)."

The "α = 0 remark" (same file, §1 N-A item 2, read by the adjudicator at Deninger math/0204110 p. 13 = math/0505354
p. 24, Remark 2 to Cor. 5.5): "Actually the conditions of the corollary force α = 0 i.e. the flow must be isometric
with respect to g." Cor. 5.5's hypotheses: "X a compact 3-manifold with a foliation F by surfaces having a dense leaf.
φ^t a non-degenerate F-compatible flow which is everywhere transversal to F. Assume φ^t is conformal as in (20)"
(i.e. φ^{t*} g_F = e^{αt} g_F on TF). The adjudicator found "no proof of Remark 2 is given, and no reference is
offered for it — the only citation in the neighbourhood is '[21] proof of 2.6' (= Deninger–Singhof, Contemp. Math.
290) for the isometric relation −Θ² = ∆¹|ker, which is used after assuming α = 0, not to derive it."

Theorem A(B) (the program's claim, same file §1 N-A): "if φ^{t*}[λ_g] = e^t[λ_g] in H̄²_F(X) there is no nonzero
flow-invariant holonomy-invariant transverse measure" — its mechanism is: a flow-invariant holonomy-invariant
transverse measure gives a closed Ruelle–Sullivan current pairing non-trivially with [λ_g], and flow-invariance of
the measure contradicts the eigen-relation e^t ≠ 1. The contrapositive "flow-invariant holonomy-invariant transverse
measure ⇒ α = 0" is what would count as the "(B)-mechanism in the manifold case".

Secondary question (from `results/fetch-r4/a01-12-warsaw.md`): ALK 2002 (Warsaw volume, p. 162) says of its
Theorem 1.3 (Lefschetz formula for simple closed orbits) "The following theorem proves, for this type of foliations,
a conjecture stated by Deninger in [10]. Under some additional assumptions, it was proved in [11, 18]", with [11] =
"C. Deninger and W. Singhof, A note on dynamical trace formulas, manuscript, 2000". What are the "additional
assumptions", and what exactly does the note prove?

## §3. The answer from the source (printed pp. 41–55 = PDF pp. 52–66; all by vision)

### §3.1 Front matter of the article, p. 41 (PDF 52)

Running head "Contemporary Mathematics Volume 290, 2001". Title "A Note on Dynamical Trace Formulas", Christopher
Deninger and Wilhelm Singhof. Footer: "1991 Mathematics Subject Classification. 37Cxx, 37C27, 53C12. Key words and
phrases. Flow, foliation, trace formula, leafwise cohomology. © 2001 American Mathematical Society", folio 41.

**Abstract (verbatim):** "We prove a dynamical Lefschetz trace formula for certain flows respecting a
one-codimensional foliation."

**§0 Introduction, p. 41–42 (verbatim, the load-bearing paragraphs):**
"In their book [GS] Ch. VI Guillemin and Sternberg established a trace formula for certain flows on closed manifolds
with coefficients in a vector bundle V. It expresses a suitable distributional trace of the induced flow on the
global sections of V as a sum of local contributions coming from the periodic orbits and the fixed points.
In the presence of a foliation respected by the flow, this formula has been used to heuristically derive formulas
for the alternating sum of distributional traces on leafwise cohomologies. The step which is difficult to justify
rigorously is the passage from an alternating sum of traces on global sections to the alternating sum of traces on
cohomology. In fact in [DS] it is shown that in general for codimension ≥ 2 this passage is not possible. However
in [G] an example is given where this heuristic method leads to a correct result, namely the Selberg trace formula.
Moreover in [D] §4 the first author pointed out that the resulting formula for codimension one foliations were
similar to the 'explicit formulas' of analytic number theory.
The aim of the present note is to show that in the case of a codimension one foliation which is everywhere
transversal to the flow the heuristic argument can be made to work in certain cases. This uses the leafwise Hodge
decomposition theorem of [AK1] and a crude estimate for the wave front sets of the Schwartz kernels of the Hodge
projectors. Our first proof of this estimate was unneccessarily complicated. Y. Kordyukov kindly pointed out to us
that it already followed from a simple application of the principle of propagation of singularities. An earlier
application due to Hörmander of this principle to the definition of the index of a transversally elliptic operator
was worked out in [S] and [NZ].
Our C^∞-approach to the trace formula requires some artificial conditions at the moment which could probably be
overcome with more effort. We refrain from this however since complete results have been obtained in the meantime
by Alvárez López and Kordyukov [AK2]. They also use harmonic forms along the leaves but base their arguments on
heat kernel asymptotics.
We would like to thank J. Alvárez López, U. Bunke and Y. Kordyukov for helpful explanations. The first author is
also grateful for the hospitality and support of the University of Santiago de Compostela and to J. Alvárez López
for inviting him there."

### §3.2 §1 "Estimates for wave front sets of certain Hodge projectors", pp. 42–44

**Standing setting, p. 42 (verbatim):** "We begin by reviewing the Hodge decomposition theorem of Alvárez López and
Kordyukov [AK1] Cor. 1.3. Consider a closed manifold X with a foliation F. We assume that F is Riemannian. This means
that there is a Riemannian metric g on X such that the foliation is locally defined by Riemannian submersions. A
metric with this property is called bundle-like. Alternatively a metric is bundle-like for a foliation if any geodesic
which is perpendicular to a leaf at one point remains perpendicular to the leaves at all other points. For example any
one-codimensional foliation given by a closed one-form without singularities is Riemannian.
Let V be a Riemannian vector bundle on X with a flat, Riemannian connection d_F along the leaves of the foliation. Let
A•(F, V) = Γ(X, Λ•T*F ⊗ V) be the de Rham complex of V-valued forms along the leaves of F on X with the differential
d_F. The graded Fréchet space A•(F, V) carries a canonical inner product ( , ). Since the foliation is Riemannian and
the metric bundle-like the operator δ_F defined by the de Rham coderivative on the leaves is adjoint to d_F with
respect to ( , ). The Laplace operator along the leaves ∆_F = d_F δ_F + δ_F d_F is leafwise elliptic and formally
self adjoint." (p. 43)

**Theorem 1.1, p. 43 (verbatim; attributed "In [AK1] Cor. 1.3 the following remarkable result is proved"):**
"THEOREM 1.1. *There is an orthogonal Hodge-decomposition:* A•(F, V) = ker ∆_F ⊕ \overline{im d_F} ⊕
\overline{im δ_F}." "In particular the reduced leafwise cohomology H•(F, V) = ker d_F / \overline{im d_F} is
isomorphic to ker ∆_F."
"REMARK The example in [DS] shows that this Hodge decomposition does not hold in general for non-Riemannian
foliations."

Then: "Let us write P_∆, P_d, P_δ : A•(F, V) → A•(F, V) for the projectors to ker ∆_F, \overline{im d_F} and
\overline{im δ_F} defined by the above decomposition. If P is anyone of them we may view its Schwartz kernel K_P as a
distributional section of End(Λ•T*F ⊗ V) on X × X with the defining property that for all test functions α, β in
A•(F, V) we have (1.1) ⟨K_P, α ⊗ β⟩ = (P(β), α). Let N*F be the conormal bundle to the foliation, and let N*∆ be the
conormal bundle to the diagonal ∆ ⊂ X × X. For any vector bundle F set F̃ := F ∖ 0."

**Proposition 1.2, p. 43 (verbatim):** "PROPOSITION 1.2. *The following estimates for the wave front set of K_P in
T̃*(X × X) hold:* WF(K_{P_∆}) ⊂ (N*F × N*F) ∖ 0. *Moreover* WF(K_{P_d}) *and* WF(K_{P_δ}) *are contained in the union
of* (N*F × N*F) ∖ 0 *with* Ñ*∆."

**Proof of Prop. 1.2, p. 44 (summary, the source says):** self-adjointness gives K_P = s*K_P, so it suffices to show
(1.2) WF(K_{P_∆}) ⊂ (N*F × T*X) ∖ 0 and WF(K_{P_d}) ∪ WF(K_{P_δ}) ⊂ Ñ*∆ ∪ (N*F × T*X) ∖ 0; (∆_F ⊗̂ id)(K_P) =
K_{P∆_F}; "By the principle of propagation of singularities [H] Theorem 8.3.1 we have WF(K_P) ⊂ WF(K_{P∆_F}) ∪
char(∆_F ⊗̂ id)"; leafwise ellipticity gives char(∆_F ⊗̂ id) ⊂ (N*F × T*X) ∖ 0; P∆_F = 0, d_F δ_F, δ_F d_F respectively.

p. 44 (verbatim): "In the interesting case where all leaves are dense we don't know how to improve the estimate in
the proposition which doesn't impose any restriction on the singular support of K_P if dim F < dim X. In general we
can do a little better by the following observation. It is known that the closures L̄ of the leaves L of the
foliation form a partition of X. Let R_F̄ ⊂ X × X denote the corresponding equivalence relation. It is a closed
subset of X × X."

**Proposition 1.3, p. 45 (verbatim):** "PROPOSITION 1.3. *The support of K_{P_∆} is contained in R_F̄.*" Proof via
P_∆(α) = lim_{t→∞} e^{−t∆_F}(α) ([AK1] Cor. 1.3) and the leafwise heat equation ∂u_α/∂t = ∆_F u_α, u_α(0, x) =
α(x): "Since heat evolves along the leaves … supp K_{P_∆} ⊂ R_F̄."

**1.4 — THE STANDING HYPOTHESES for the trace formula, p. 45 (verbatim):** "1.4. We now give a corollary of
proposition 1.2 which is relevant for the C^∞-approach to the trace formula in section 2. Let X be a closed manifold
with a flow φ : X × R → X which is everywhere transversal to a one-codimensional foliation F and such that φ^t maps
leaves to leaves for all t. Then F is Riemannian and we fix a bundle-like metric. The flow doesn't have fixed points.
It should be non-degenerate in the following sense:
If x lies on a periodic orbit γ of length l(γ) then for all integers k ≥ 1 (equivalently: for all nonzero integers k)
the 1-eigenspace of T_x φ^{kl(γ)} is one-dimensional. Note here that T_x φ^{kl(γ)} always has Y_{φ,x} as an
eigenvector with eigenvalue 1, Y_φ being the vector field generated by the flow.
We also assume that we are given a Riemannian bundle V with a connection as before. Moreover there should be a
smooth action ψ^t : φ^{t*}V → V which is compatible with the connection in the evident sense. The induced action
ψ^{t*} on A•(F, V) respects the differential d_F. For the bundle E = Λ•T*F ⊗ V consider the composition
ψ* : Γ(X, E) —(φ|_{X×R*})^{−1}→ Γ(X × R*, φ*E) —ψ→ Γ(X × R*, p*E) where p : X × R* → X is the projection."

**Corollary 1.5, p. 46 (verbatim):** "COROLLARY 1.5. *For P = P_∆, P_d, P_δ the wave front set of the Schwartz
kernels K_{ψ*∘P} and K_{(P⊗̂id)∘ψ*} and K_{(P⊗̂id)∘ψ*∘P} on X × R* × X is disjoint from the conormal bundle to the
"diagonal" ∆̃ : X × R* → X × R* × X defined by ∆̃(x, t) = (x, t, x). In particular the pullbacks ∆̃* tr_V K_{ψ*∘P}
and ∆̃* tr_V K_{(P⊗̂id)∘ψ*} and ∆̃* tr_V K_{(P⊗̂id)∘ψ*∘P} are defined, [H] Cor. 8.2.7.*"
Proof p. 46–47: K_{ψ*} is a smooth density on the graph Γ_φ ⊂ X × R* × X of φ|_{X×R*}, WF(K_{ψ*}) ⊂ Ñ*Γ_φ, with
N*Γ_φ = {(ξ_x, µ dt|_t, η_{φ^t(x)}) : ξ_x = −(T_x φ^t)*(η_{φ^t(x)}), µ = −⟨Y_{φ,φ^t(x)}, η_{φ^t(x)}⟩}; the sets
WF(K_{ψ*})_{X×R*} and WF′(K_{ψ*})_X are empty; [H] Th. 8.2.14 gives WF′(K_{ψ*∘P}) ⊂ WF′(K_{ψ*}) ∘ WF′(K_P) ∪
0_{X×R*} × T̃*X; and by Prop. 1.2 WF′(K_P) ⊂ (diagonal in T̃*X × T̃*X) ∪ (N*F × N*F) ∖ 0.

p. 47, end of proof of Cor. 1.5 (verbatim, the role of transversality): "The fact that the flow is non-degenerate is
equivalent to the intersection of Ñ*Γ_φ with N*∆̃ = {(ξ_x, 0_t, −ξ_x) | ξ_x ∈ T̃*_x X} being empty. Obviously
(0_{X×R*} × T̃*X) ∩ N*∆̃ = ∅. Finally, if an element (ξ_x, µ dt|_t, ζ_z) as above were in N*∆̃ then µ = 0 and hence
η_{φ^t(x)} would have to vanish since the flow is transversal to the foliation. Thus ξ_x = 0, and because of
ζ_z = −ξ_x also ζ_z = 0. Contradiction. Hence we have seen that: WF(K_{ψ*∘P}) ∩ N*∆̃ = ∅."

### §3.3 §2 "Application to a dynamical trace formula", pp. 47–52

**Setting, p. 47 (verbatim):** "The starting point is a trace formula in differential topology due to Guillemin and
Sternberg [GS] Ch. VI, p. 311. Consider a smooth compact manifold X with a flow φ^t without fixed points. We assume
that φ^t is non-degenerate in the sense of 1.4. Let T^0 = R·Y_φ ⊂ TX be the one-dimensional bundle of tangents to
the flow. Let V be a smooth vector bundle with a contravariant action ψ^t = ψ^t_V : φ^{t*}V → V. For any point x on a
periodic orbit γ of length l(γ) we get endomorphisms ψ_x^{kl(γ)} : V_{φ^{kl(γ)}(x)} = V_x → V_x for any integer k.
Note that the trace Tr(ψ_x^{kl(γ)} | V_x) is independent of the chosen point x ∈ γ."
p. 48: "Guillemin and Sternberg define the distributional trace of the composition ψ* : Γ(X, V) → Γ(X × R*, φ*V) →
Γ(X × R*, p*V) by the formula Tr(ψ* | Γ(X, V)) = π_* tr_V ∆̃* K_{ψ*} in D′(R*). Here p : X × R* → X and π : X × R* → R*
are the projections and K_{ψ*} is the Schwartz kernel of ψ*. The pullback of K_{ψ*} by the 'diagonal' ∆̃ … is
defined since the wave front set of K_{ψ*} is disjoint from N*∆̃, the flow being non-degenerate. Then according to
[GS] Ch. VI, p. 311 the following is true:"

**Proposition 2.1, p. 48 (verbatim — the Guillemin–Sternberg formula):** "PROPOSITION 2.1. *With assumptions as
above the following formula holds in D′(R*):*
Tr(ψ* | Γ(X, V)) = Σ_γ l(γ) Σ_{k∈Z∖0} [Tr(ψ_x^{kl(γ)} | V_x) / |det(1 − T_x φ^{kl(γ)} | T_x X / T^0_x)|] δ_{kl(γ)}.
*Here γ runs over the periodic orbits and in the sum x denotes any point on γ. Note that non-degeneracy of the flow
(1.4) implies that there are only finitely many orbits γ ⊂ X of length bounded by a given constant C.*"

p. 48 (verbatim): "Now assume that in addition X carries a smooth foliation F such that φ^t maps leaves to leaves for
any t. Hence T_x φ^t maps T_x F to T_{φ^t(x)} F and hence the dual map gives rise to a contravariant action T*φ^t :
φ^{t*}T*F → T*F. Now recall the formulas Σ_i (−1)^i Tr(Λ^i f | Λ^i E) = det(1 − f | E) and Tr(f ⊗ g | E ⊗ F) =
Tr(f | E) Tr(g | F) … Applying (2.1) [sic — Prop. 2.1] to the bundles Λ^i T*F ⊗ V with ψ^t = ψ^t_V ⊗ Λ^i T*φ^t and
taking the alternating sum over i we get in D′(R*):
(2.1)  Σ_i (−1)^i Tr(ψ* | A^i(F, V)) = Σ′_γ l(γ) Σ_{k∈Z∖0} ε_γ(k) [Tr(ψ_x^{kl(γ)} | V_x) / det(1 − T_x φ^{kl(γ)} |
T_x X / (T_x F ⊕ T^0_x))] δ_{kl(γ)}."
p. 49: "Here the prime at the sum over periodic orbits means that we only sum over those γ's which are not
contained in a leaf i.e. those for which Y_{φ,x} ∉ T_x F for one (equivalently: for every) point x ∈ γ. Observe here
that for the other closed orbits we have det(1 − T_x φ^{kl(γ)} | T_x F) = 0 for x ∈ γ, k ∈ Z ∖ 0 since
T_x φ^{l(γ)}(Y_{φ,x}) = Y_{φ,x}. Finally ε_γ(k) denotes the sign of the determinant det(1 − T_x φ^{kl(γ)} |
T_x X / T^0_x). It is independent of the chosen point x ∈ γ."

**The problem posed, p. 49 (verbatim):** "Let us now assume in addition that V carries a flat connection d_F along
the leaves which is compatible with ψ. One would like to know conditions under which the alternating sum in (2.1)
can be replaced by an alternating sum of traces on the reduced leafwise cohomologies H^i(F, V) of (V, d_F).
If F has codimension zero this is possible since the resulting formula is just Hopf's formula.
For F of codimension two this is not always possible as the example in [DS] §2 shows.
For Riemannian foliations and Riemannian connections a Hodge theoretic approach to the problem makes use of the
leafwise Hodge decomposition 1.1. If the wave front sets of the Schwartz kernels K_{ψ*∘P} are disjoint from N*∆̃ for
P = P_∆, P_d, P_δ the traces
(2.2)  Tr(ψ* | ker ∆_F) := π_* ∆̃* tr_V K_{ψ*∘P_∆};  Tr(ψ* | \overline{im d_F}) := π_* ∆̃* tr_V K_{ψ*∘P_d};
       Tr(ψ* | \overline{im δ_F}) := π_* ∆̃* tr_V K_{ψ*∘P_δ}
are well defined and we have for all i: Tr(ψ* | A^i(F, V)) = Tr(ψ* | ker ∆^i_F) + Tr(ψ* | \overline{im d^{i−1}_F}) +
Tr(ψ* | \overline{im δ^i_F}).
If one can show that
(2.3)  Σ_i (−1)^i Tr(ψ* | \overline{im d^i_F}) = Σ_i (−1)^i Tr(ψ* | \overline{im δ^i_F})
e.g. if
(2.4)  Tr(ψ* | \overline{im d^i_F}) = Tr(ψ* | \overline{im δ^i_F})  for all i"

p. 50 (verbatim): "then it follows that:
(2.5)  Σ_i (−1)^i Tr(ψ* | A^i(F, V)) = Σ_i (−1)^i Tr(ψ* | ker ∆^i_F).
We will now discuss this approach in the particular codimension one situation described in section 1.4. According to
Corollary 1.5 the problem of defining the individual traces (2.2) is solved in this case. Moreover the traces
π_* ∆̃* tr_V K_{(P⊗̂id)∘ψ*} and π_* ∆̃* tr_V K_{(P⊗̂id)∘ψ*∘P} are defined as well. It can be shown by a somewhat lengthy
calculation that these traces all agree i.e. that:
(2.6)  Tr(ψ* | ker ∆^i_F) = π_* ∆̃* tr_V K_{(P_∆⊗̂id)∘ψ*} = π_* ∆̃* tr_V K_{(P_∆⊗̂id)∘ψ*∘P_∆}
etc. In particular, because of the commutative diagram [ker ∆^i_F ≅ H^i(F, V), vertical arrows P∘ψ^{t*} and ψ^{t*}]
we may view Tr(ψ* | ker ∆^i_F) as a distributional trace of the flow on H^i(F, V). Of course there is still the
problem to express Tr(ψ* | ker ∆^i_F) purely in terms of the induced flow on H^i(F, V) without any reference to a
metric. In 2.5 below this is achieved for flows which are isometric for some bundle like metric.
We have been able to establish equation (2.3) in two special cases only:
2.2. If the leafwise cohomologies are Hausdorff then d_F induces an isomorphism d_F : im δ_F ≅ im d_F which commutes
with the flow. This may be used to prove (2.4). In general d_F induces only an isomorphism d_F : \overline{im δ_F} ≅
im d_F.
2.3. Assume φ^t and ψ^t are isometric and n = dim X is even. The Hodge star operator along the leaves *_F c.f. [AK1]
§3 commutes with ψ^{t*}. It maps \overline{im d^i_F} isomorphically onto \overline{im δ^{n−i−2}_F} where n = dim X.
From this one may deduce that Tr(ψ* | \overline{im d^i_F}) = Tr(ψ* | \overline{im δ^{n−i−2}_F}). Hence (2.3) follows
since dim X was supposed to be even."

**THEOREM 2.4, p. 51 (verbatim — the main trace formula):** "THEOREM 2.4. *In the situation of 1.4 assuming 2.2 or
2.3 the following trace formula holds as an equality in D′(R*):*
Σ_i (−1)^i Tr(ψ* | ker ∆^i_F) = Σ_γ l(γ) Σ_{k∈Z∖0} ε_γ(k) Tr(ψ_x^{kl(γ)} | V_x) δ_{kl(γ)}."
"REMARK Heat kernel methods lead to a stronger version of this result. In [AK2] Alvárez López and Kordyukov prove
the trace formula in the setting of 1.4 without any restrictions. Moreover they can prove a version in D′(R): Quite
beautifully there appears the contribution χ_Co(F, V)·δ_0 from the origin where χ_Co(F, _) is Connes' Euler
characteristic for foliated bundles.
In the case of isometric flows their formula also follows from the transverse index theorem of Lazarov [L] Theorem
2.10 combined with the leafwise Hodge decomposition of [AK1]."

**2.5 and THEOREM 2.6, p. 51 (verbatim):** "2.5. We now assume that φ^t and ψ^t are isometric. In this case the
distributional trace Tr(ψ* | ker ∆^i_F) is completely determined by the action of ψ^{t*} on the reduced leafwise
cohomology H^i(F, V) as follows. For α ∈ C let E_α ⊂ H^i(F, V) denote the subspace of H^i(F, V) where ψ^{t*} acts by
multiplication with e^{αt} for all t ∈ R. Since ψ^{t*} is an isometry on L²(ker ∆_F) the commutative diagram: (2.7)
[H^i(F, V) ≅ ker ∆^i_F, vertical ψ^{t*}] implies that E_α = 0 unless α is purely imaginary.
THEOREM 2.6. *The multiplicity dim E_α is finite for all α and non-zero for countably many values only. We have:*
Tr(ψ* | ker ∆^i_F) = Σ_α dim E_α · e^{αt}  *in* D′(R*). *Here the functions e^{αt} are viewed as distributions on R*
and the sum converges in D′(R*).*"
"As an example for such kinds of sums note that the sum over ν ≥ 1 of the functions e^{iνt} converges in D′(R) since
by partial integration for any φ ∈ D(R) ⟨e^{iνt}, φ⟩ = O(ν^{−N}) for all N ≥ 1. On the other hand the sum Σ e^{iνt}
does not converge for a single real t."

**Proof of 2.6, pp. 52–54 — this is the "[21] proof of 2.6" that [Den05]/math/0204110 cite for −Θ² = ∆|ker. p. 52
(verbatim):** "PROOF OF 2.6 Consider the orthogonal decomposition with respect to the bundle like metric TX = TF^⊥ ⊕
TF with TF^⊥ = R·Y_φ. It allows us to view Λ•T*F as a direct summand of Λ•T*X. Using a corresponding decomposition
of V we may view A•(F, V) as a direct summand of the space A•(V) of all smooth V-valued forms on X. Let Θ be the
infinitesimal generator of the induced flow ψ^{t*} on ker ∆^i_F. Then we have the equality
(2.8)  −Θ² = ∆^i |_{ker ∆^i_F}.
Here ∆^i is the ordinary Laplacian on A^i(V). In particular ∆^i maps ker ∆^i_F into itself. The proof of (2.8) goes as
follows. The orthogonal decomposition TX = TF ⊕ R·Y_φ corresponds to a decomposition d = d_F + d^0 of the exterior
differential. We set ∆^0 = d^0 d^{0*} + d^{0*} d^0. Using the fact that ∆_F ω = 0 if and only if d_F ω = 0 = d*_F ω we
find that for a form ω ∈ A^i(V) in ker ∆_F we have: ∆ω = ∆^0 ω + d_F d^{0*} ω + d*_F d^0 ω.
By isometry of the flow the function x ↦ ‖Y_{φ,x}‖ is constant and we may therefore assume that the metric on X is
normalized such that ‖Y_{φ,x}‖ = 1 for all x. Let ω_φ be the 1-form on X which is zero on TF and such that
⟨ω_φ, Y_φ⟩ = 1. Then ‖ω_{φ,x}‖ = 1 for all x and for any form α with values in Λ^p T*F ⊗ V we have
d^0 α = Θα ∧ ω_φ  and  d^{0*}(α ∧ ω_φ) = −Θα.
Here Θ is the infinitesimal generator of the induced flow on A•(V). Note that Θ is skew-symmetric since the flow is
isometric. It follows that ∆^0 = −Θ². Moreover d_F d^{0*}(α ∧ ω_φ) = −d_F Θα = −Θ d_F α = 0 if d_F(α ∧ ω_φ) = 0.
Hence for ω ∈ ker ∆_F we have d_F d^{0*} ω = 0. By isometry of the flow Θ commutes with the *-operator along the
leaves, *_F up to sign. Hence d*_F Θ = ±Θ d*_F since d*_F = ± *_F d_F *_F and therefore (p. 53) d*_F d^0 ω =
d*_F(Θω ∧ ω_φ) = ±Θ d*_F ω ∧ ω_φ = 0 if ω ∈ ker ∆_F. This completes the proof of equation (2.8)."
p. 53 (verbatim, continued): "Since E_α is the eigenspace of Θ the first assertions of the theorem follow from the
spectral theory of the ordinary Laplacian e.g. [BGV] ch. 2. Moreover it follows that there is an orthonormal basis
{ω_ν} of L²(ker ∆^i_F) of eigenvectors of Θ with ω_ν ∈ ker ∆^i_F. If Θω_ν = α_ν ω_ν then ψ^{t*} ω_ν = e^{tα_ν} ω_ν. A
short calculation now shows that: K_{(P_∆⊗̂id)∘ψ*∘P_∆} = Σ_ν e^{tα_ν} ω_ν ⊗ ω̄_ν, where the sum is a convergent sum of
distributional sections on X × R* × X. For any test function φ ∈ D′(R*) [sic] define a distributional section K_φ on
X × X by 'contraction': (2.9) K_φ = ⟨K_{(P_∆⊗̂id)∘ψ*∘P_∆}, φ⟩ = Σ_ν (∫_R e^{tα_ν} φ(t) dt) ω_ν ⊗ ω̄_ν. We claim that the
sum does not only converge in the distributional sense but even in the smooth topology. … (2.10) Σ_ν |∫_R e^{tα_ν}
φ(t) dt| ‖ω_ν ⊗ ω̄_ν‖_{2,k} for k ≥ 1 converge. … Since ∆^i_{X×X} = ∆^i_X ⊗ id + id ⊗ ∆^i_X and because of (2.8) we
have ‖ω_ν ⊗ ω̄_ν‖_{2,k} = (1 − α_ν² − ᾱ_ν²)^{k/2} = (1 + 2|α_ν|²)^{k/2}. On the other hand partial integration shows
that for any N ≥ 1 we have ∫_R e^{ty} φ(t) dt = O(y^{−N})"

p. 54 (verbatim, end of proof of 2.6): "as y → ∞. Hence up to finitely many terms the sum in (2.10) is majorised by a
constant times Σ_{α_ν≠0} |α_ν|^{−N}(1 + 2|α_ν|²)^{k/2}. Ths [sic] sum converges for large enough N = N(k) since the
numbers |α_ν|² are among the eigenvalues λ of the ordinary Laplacian ∆ on V-valued forms on X and since the sum
Σ_{λ≠0} λ^{−m} converges for m ≫ 0. We have therefore seen that the series (2.10) converge for all k ≥ 1.
A straightforeward [sic] argument using the definition of the pullback of distributions in [H] Theorem 8.2.4 shows
that if ∆ : X → X × X denotes the diagonal: ⟨π_* ∆̃* tr_V K_{(P_∆⊗̂id)∘ψ*∘P_∆}, φ⟩ = ⟨∆̃* tr_V K_{(P_∆⊗̂id)∘ψ*∘P_∆},
φ∘π⟩ = ⟨∆* tr_V K_φ, 1_X⟩. Since K_φ is a smooth section we have ⟨∆* tr_V K_φ, 1_X⟩ = ∫_X tr_V K_φ(x, x) dx. Using
(2.6) and equation (2.9) with its convergence in the smooth topology we find: ⟨Tr(ψ* | ker ∆^i_F), φ⟩ = Σ_ν ∫_R
e^{tα_ν} φ(t) dt, as desired. □"

**References of the note, pp. 54–55 (verbatim, all eleven):**
[AK1] J.A. Alvárez López, Y. Kordyukov, Long time behaviour of leafwise heat flow for Riemannian foliations.
Preprint dg-ga/9612010, 1996. To appear in Compositio Math.
[AK2] J.A. Alvárez López, Y. Kordyukov, Distributional Betti numbers of transitive foliations of codimension one.
Preprint 2000.
[BGV] N. Berline, E. Getzler, M. Vergne, Heat kernels and Dirac operators. Springer 1992
[D] C. Deninger, Some analogies between number theory and dynamical systems on foliated spaces. Doc. Math. J. DMV
Extra volume ICM I (1998), 23–46
[DS] C. Deninger, W. Singhof, A counterexample to smooth leafwise Hodge decomposition for general foliations and to
a type of dynamical trace formula. To appear in Ann. Inst. Fourier 2001
[G] V. Guillemin, Lectures on spectral theory of elliptic operators. Duke Math. J. 44 (1977), 485–517
[GS] V. Guillemin, S. Sternberg, Geometric asymptotics, Math. Surveys 14, Amer. Math. Soc., Providence, R.I. 1977
[H] L. Hörmander, The analysis of linear partial differential operators I. Springer 1983
[L] C. Lazarov, Transverse index and periodic orbits. GAFA 10 (2000), 124–159
[NZ] A. Neske, F. Zickermann, The index of transversally elliptic complexes. Proceedings of the 13th winter school
on abstract analysis (Srni, 1985). Rend. Circ. Mat. Palermo (2) Suppl. No. 9 (1986), 165–175
[S] I.M. Singer, Index theory for elliptic operators, Proc. Symp. Pure Math. 28 (1973), 11–31
Addresses p. 55: Deninger, Mathematisches Institut, WWU Münster, Einsteinstr. 62, 48149 Münster; Singhof,
Mathematisches Institut, Universitätsstr. 1, 40225 Düsseldorf. p. 56 (PDF 67) is blank; Fan–Jorgenson begins p. 57.

### §3.4 Inventory — every numbered statement and displayed formula in the note

| item | page | content (one line) |
|---|---|---|
| Thm 1.1 | 43 | Leafwise Hodge decomposition A• = ker ∆_F ⊕ cl(im d_F) ⊕ cl(im δ_F), Riemannian foliation, closed X — quoted from [AK1] Cor. 1.3, not proved here |
| (1.1) | 43 | ⟨K_P, α ⊗ β⟩ = (P(β), α) — definition of the Schwartz kernel of a projector |
| Prop 1.2 | 43 | WF(K_{P_∆}) ⊂ (N*F × N*F) ∖ 0; WF(K_{P_d}), WF(K_{P_δ}) ⊂ (N*F × N*F) ∖ 0 ∪ Ñ*∆ |
| (1.2) | 44 | the one-sided estimates proved in the proof of 1.2 |
| Prop 1.3 | 45 | supp K_{P_∆} ⊂ R_F̄ (leaf-closure equivalence relation) |
| 1.4 | 45 | STANDING HYPOTHESES (see §3.5) |
| Cor 1.5 | 46 | WF of K_{ψ*∘P} etc. disjoint from N*∆̃; the pulled-back traces are defined |
| Prop 2.1 | 48 | Guillemin–Sternberg trace formula in D′(R*) with V-coefficients (quoted from [GS] p. 311) |
| (2.1) | 48 | alternating sum over A^i(F, V), primed orbit sum, ε_γ(k), det on T_xX/(T_xF ⊕ T^0_x) |
| (2.2) | 49 | definition of Tr(ψ* | ker ∆_F), Tr(ψ* | cl im d_F), Tr(ψ* | cl im δ_F) |
| (2.3), (2.4) | 49 | the cancellation condition on cl(im d)/cl(im δ) traces (alternating / termwise) |
| (2.5) | 50 | Σ(−1)^i Tr(ψ*|A^i) = Σ(−1)^i Tr(ψ*|ker ∆^i_F) — follows from (2.3) |
| (2.6) | 50 | the three definitions of Tr(ψ*|ker ∆^i_F) agree ("somewhat lengthy calculation", not printed) |
| 2.2 | 50 | Special case: leafwise cohomologies Hausdorff ⇒ (2.4) |
| 2.3 | 50 | Special case: φ^t, ψ^t isometric and dim X even ⇒ (2.3) via *_F |
| **Thm 2.4** | 51 | **Σ_i(−1)^i Tr(ψ*|ker ∆^i_F) = Σ_γ l(γ) Σ_{k∈Z∖0} ε_γ(k) Tr(ψ_x^{kl(γ)}|V_x) δ_{kl(γ)} in D′(R*), under 1.4 and (2.2 or 2.3)** |
| Remark | 51 | [AK2] proves it "in the setting of 1.4 without any restrictions" and in D′(R) with χ_Co(F, V)·δ_0; isometric case also from Lazarov [L] Thm 2.10 + [AK1] |
| 2.5 / (2.7) | 51 | isometric φ^t, ψ^t; E_α ⊂ H^i(F, V) the e^{αt}-eigenspace; E_α = 0 unless α ∈ iR |
| **Thm 2.6** | 51 | **dim E_α finite, non-zero for countably many α; Tr(ψ*|ker ∆^i_F) = Σ_α dim E_α · e^{αt} in D′(R*)** |
| (2.8) | 52 | −Θ² = ∆^i|_{ker ∆^i_F} (isometric flow; Θ = generator of ψ^{t*} on ker ∆^i_F) — proved pp. 52–53 |
| (2.9), (2.10) | 53 | K_φ = Σ_ν(∫ e^{tα_ν}φ dt) ω_ν ⊗ ω̄_ν and its Sobolev-norm convergence |

There are no lemmas, no definitions numbered as such, and no theorem labeled "A" or "B" in the note. The only
"dynamical trace formulas" are Prop. 2.1 (Guillemin–Sternberg, quoted), (2.1), Thm 2.4 and Thm 2.6.

### §3.5 Standing hypotheses, answered item by item (the source says, with page)

- **Manifold?** Yes — "closed manifold X" (p. 42, p. 45), "smooth compact manifold X" (p. 47). No laminations, no
  foliated spaces, no solenoids anywhere in the note.
- **Compact?** Yes, closed (= compact without boundary) throughout.
- **Foliation regularity?** Smooth foliation F; **Riemannian** with a fixed **bundle-like metric** (p. 42–43, p. 45).
  Codimension one for §1.4 onward ("everywhere transversal to a one-codimensional foliation F", p. 45); §1 (Prop.
  1.2, 1.3) and Prop. 2.1/(2.1) are stated for arbitrary codimension. Leaves need not be dense (p. 44 treats the
  dense case as "the interesting case" where nothing better is known). Coefficients: a Riemannian bundle V with a
  flat leafwise Riemannian connection d_F and a compatible action ψ^t (p. 45).
- **Flow transverse?** Yes, **everywhere transversal** (p. 45: "a flow φ : X × R → X which is everywhere transversal
  to a one-codimensional foliation F and such that φ^t maps leaves to leaves for all t"). The note asserts, with no
  proof or citation, "Then F is Riemannian and we fix a bundle-like metric" (p. 45) — i.e. it takes for granted that
  a codimension-one foliation with a transverse leaf-preserving flow is Riemannian. Transversality is used
  explicitly at p. 47 (last step of the proof of Cor. 1.5: "η_{φ^t(x)} would have to vanish since the flow is
  transversal to the foliation") and at p. 49 (the primed sum; orbits inside leaves would give det = 0).
- **Fixed points allowed?** **No.** "The flow doesn't have fixed points." (p. 45); "a flow φ^t without fixed points"
  (p. 47). All trace formulas are in D′(R*), i.e. with the origin removed; the δ_0 term is explicitly left to [AK2].
- **Closed orbits simple?** Yes, "non-degenerate in the following sense: If x lies on a periodic orbit γ of length
  l(γ) then for all integers k ≥ 1 (equivalently: for all nonzero integers k) the 1-eigenspace of T_x φ^{kl(γ)} is
  one-dimensional." (p. 45). [I infer: under transversality T_xX = T_xF ⊕ R·Y_φ with Y_φ the fixed eigenline, so this
  is equivalent to det(1 − T_xφ^{kl(γ)}|T_xF) ≠ 0 for all k ≠ 0, which is ALK 2002's "simple" (a01-12-warsaw.md,
  ALK p. 162) applied at every iterate.]
- **Isometry?** NOT a standing hypothesis of the paper; it is the hypothesis of special case 2.3 (with dim X even),
  of 2.5 and of Thm 2.6 ("We now assume that φ^t and ψ^t are isometric", p. 51), and of the whole proof of (2.8).
- **Conformality / α?** The note contains no conformal hypothesis of any kind. The symbol α occurs only in 2.5–2.6
  as the exponent in ψ^{t*} = e^{αt} on the eigenspace E_α ⊂ H^i(F, V) — a spectral parameter of Θ, not Deninger's
  conformal factor. The words "conformal", "transverse measure", "holonomy", "Ruelle", "Sullivan", "current",
  "cycle", "λ_g", "dense leaf" (as a hypothesis) do not occur anywhere in pp. 41–55 (checked by reading every page).

### §3.6 THE KEY QUESTION — is the α = 0 mechanism, or Theorem A(B)'s mechanism, printed here?

**Plain answer: NO. Neither is stated, and neither is proved, in any form.**

*The source says.* The only statement in the note that has "the flow is isometric" as a **conclusion** rather than a
hypothesis is nothing — there is none. Isometry enters exclusively as a hypothesis (2.3, 2.5, Thm 2.6, (2.8)). The
note never considers a conformal flow φ^{t*}g_F = e^{αt}g_F, never asks when a transverse flow can be made isometric,
never mentions a transverse measure, a foliated cycle, or a cohomology class such as [λ_g]. The one thing the note
proves about "Re ρ = 0" is the trivial direction: **isometry ⇒ ψ^{t*} unitary on L²(ker ∆_F) ⇒ E_α = 0 unless α is
purely imaginary** (p. 51, (2.7)). That is the consequence Deninger draws *after* α = 0, not the mechanism that
forces α = 0.

*Resolution of Deninger's citation "[21] proof of 2.6".* It resolves exactly: the proof of Thm 2.6, p. 52, displays
(2.8) −Θ² = ∆^i|_{ker ∆^i_F} and proves it on pp. 52–53 under the hypothesis "By isometry of the flow" (used three
times: constancy of ‖Y_φ‖, skew-symmetry of Θ, and Θ commuting with *_F). So the adjudicator's reading at
`s16/novelty/adjudication.md` §1 N-A item 2 — that [21] is cited for the isometric relation "used after assuming
α = 0, not to derive it" — is **confirmed at the page**. The note is not the printed home of a proof of the α = 0
remark; that proof remains **unprinted** in every Deninger/Deninger–Singhof source the program has opened.

*What the note DOES prove instead (for the record).* (i) A wave-front-set estimate for the leafwise Hodge projectors
of a Riemannian foliation (Prop. 1.2), via propagation of singularities. (ii) That for a codimension-one foliation
with an everywhere-transverse, fixed-point-free, non-degenerate leaf-preserving flow, the Guillemin–Sternberg
distributional traces restricted to ker ∆_F, cl(im d_F), cl(im δ_F) are well defined on R* (Cor. 1.5). (iii) The
Lefschetz trace formula Thm 2.4 on R* (no δ_0 term) under the extra assumption that the leafwise cohomology is
Hausdorff (2.2) or that the flow is isometric and dim X is even (2.3). (iv) Thm 2.6: for isometric flows, the
distributional trace on ker ∆^i_F equals Σ_α dim E_α e^{αt} — the "spectral side" is a genuine eigenvalue sum on
reduced leafwise cohomology, with (2.8) as the tool that gives finite multiplicities and the Sobolev convergence.

*I infer (not printed).* Two devices in the note are adjacent to Theorem A(B)'s mechanism without touching it:
(a) p. 52 introduces "ω_φ the 1-form on X which is zero on TF and such that ⟨ω_φ, Y_φ⟩ = 1" — the same canonical
1-form as KMNT Lemma 1.9 (the object the adjudicator identifies as the *supply* of the flow-invariant holonomy-
invariant transverse measure in the transverse manifold case). The note does not say ω_φ is closed and does not use
it as a measure; it uses it only to write d^0 α = Θα ∧ ω_φ. (b) p. 45's unproved assertion "Then F is Riemannian"
for a codimension-one foliation with a transverse leaf-preserving flow is, in substance, the closedness of ω_φ (a
closed nonsingular 1-form defines a Riemannian foliation, p. 42). Neither device is turned toward the conformal
class or toward transverse measures. **Nothing here narrows the NOVEL/PARTIAL grading of Theorem A(B) recorded in
`s16/novelty/adjudication.md` §1 N-A; the note adds no printed relative of (B) and no printed relative of (A).**

### §3.7 Relation to ALK 2002 (Warsaw) Theorems 1.1/1.3 and to Deninger's ICM-98 conjecture

*The source says.* The note cites [D] = Deninger, Doc. Math. ICM 1998 extra vol. I, 23–46, and credits it only for
the observation (p. 41) that "in [D] §4 the first author pointed out that the resulting formula for codimension one
foliations were similar to the 'explicit formulas' of analytic number theory." It does not use the word
"conjecture" and does not display the ICM-98 formula. It cites [AK2] = "Distributional Betti numbers of transitive
foliations of codimension one. Preprint 2000" — i.e. the paper published in the Warsaw volume (r4-01+12, World
Scientific 2002, pp. 159–183) — and says twice that [AK2] supersedes it: p. 42 "complete results have been obtained
in the meantime by Alvárez López and Kordyukov [AK2]"; p. 51 Remark "In [AK2] Alvárez López and Kordyukov prove the
trace formula in the setting of 1.4 without any restrictions. Moreover they can prove a version in D′(R): Quite
beautifully there appears the contribution χ_Co(F, V)·δ_0 from the origin".

*Matching statements (the source says, both sides read this session or by a01-12).* ALK 2002 Thm 1.3 (a01-12, p. 162):
χ_dis(F) = Σ_c l(c) Σ_{k≥1} sign det(id − X*_{l(c)} : T_xF* → T_xF*) δ_{kl(c)} on R_+, under "all closed orbits of
the flow X_t on (M, F) are simple", for transitive codimension-one foliations of closed manifolds, in D′(R) with
Thm 1.1/5.1 handling the origin. DS Thm 2.4 (p. 51): Σ_i(−1)^i Tr(ψ*|ker ∆^i_F) = Σ_γ l(γ) Σ_{k∈Z∖0} ε_γ(k)
Tr(ψ_x^{kl(γ)}|V_x) δ_{kl(γ)} in D′(R*), with ε_γ(k) = sign det(1 − T_xφ^{kl(γ)}|T_xX/T^0_x) (p. 49), under 1.4
plus (2.2 Hausdorff leafwise cohomology) or (2.3 isometric + dim X even). So ALK's "Under some additional
assumptions, it was proved in [11, 18]" (a01-12 quoting ALK p. 162) is accurate and the additional assumptions are
exactly **2.2 or 2.3** (plus the absence of the δ_0 term, since DS work on R*). Differences: DS carry a flat
coefficient bundle V and sum over k ∈ Z ∖ 0 (both time directions); ALK 2002 has trivial coefficients, R_+ only,
and the transitivity hypothesis (DS require no dense leaf). DS's non-degeneracy ("1-eigenspace of T_xφ^{kl(γ)}
one-dimensional for all k ≥ 1") matches ALK's "simple" (see §3.5). DS do not assert that Thm 2.4 proves an ICM-98
conjecture; that framing is ALK's.

*Bearing on the a01-12 vision note about X*_{l(c)} vs X*_{kl(c)}.* DS print the sign **with the k-th iterate**:
ε_γ(k) is "the sign of the determinant det(1 − T_xφ^{kl(γ)}|T_xX/T^0_x)" (p. 49, verbatim), and Thm 2.4 carries
ε_γ(k) inside the k-sum. This is consistent with the ALK proof (p. 181, per a01-12) and with the k-dependent
reading, and supports the a01-12 suspicion that ALK's printed X*_{l(c)} in Thm 1.3 is a typographical slip — but
that is my inference across two sources; neither source comments on the other's typesetting.

*What is new in the note by its own account (p. 41–42):* "The aim of the present note is to show that in the case of
a codimension one foliation which is everywhere transversal to the flow the heuristic argument can be made to work
in certain cases" — i.e. Prop. 1.2 (wave front estimate; the authors credit the simple proof to Kordyukov), Cor.
1.5, Thm 2.4 under 2.2/2.3, and Thm 2.6 with (2.8). The status as "an earlier partial proof" (ALK's "[11] manuscript
2000") is therefore correct: the manuscript predates [AK2]'s "Preprint 2000" only in the sense that both circulated
in 2000; the printed note already defers to [AK2] as complete.

## §4. Anything else in the source a future session should know exists

**Full table of contents of Contemp. Math. 290 (printed p. vii = PDF p. 8; PDF page = printed + 11):**
- Preface — ix (PDF 10–11; dated July 2001; "eleven papers, seven of which were presented at the meeting")
- Cheng-Hung Chang and Dieter H. Mayer, *Eigenfunctions of the transfer operators and the period functions for
  modular groups* — 1 (PDF 12)
- Christopher Deninger and Wilhelm Singhof, *A note on dynamical trace formulas* — 41 (PDF 52–66)
- Carol E. Fan and Jay Jorgenson, *Small eigenvalues and Hausdorff dimension of sequences of hyperbolic
  three-manifolds* — 57 (PDF 68)
- Alexander Fel'shtyn, *Dynamical zeta functions and asymptotic expansions in Nielsen theory* — 67 (PDF 78)
- William F. Galway, *Computing the Riemann zeta function by numerical quadrature* — 81 (PDF 92)
- Shai Haran, *On Riemann's zeta function* — 93 (PDF 104)
- Michel L. Lapidus and Machiel van Frankenhuysen, *A prime orbit theorem for self-similar flows and Diophantine
  approximation* — 113 (PDF 124)
- A. M. Odlyzko, *The 10^22-nd zero of the Riemann zeta function* — 139 (PDF 150)
- Peter Perry, *Spectral theory, dynamics, and Selberg's zeta function for Kleinian groups* — 145 (PDF 156)
- C. Soulé, *On zeroes of automorphic L-functions* — 167 (PDF 178)
- H. M. Stark and A. A. Terras, *Artin L-functions of graph coverings* — 181 (PDF 192; ends by PDF 210 ≈ p. 199)
**There is no article by Connes in the volume**, and none by Kordyukov or Álvarez López.

One-line notes on the articles that touch the program (first pages read by vision):
- Haran, p. 93 (PDF 104): "We describe in §1 the Riemann Zeta function, the explicit sums, and the equivalence of
  Weil's positivity with the Riemann hypothesis. In §2 we reformulate the explicit sum in a suggestive form
  involving the trace of the action of the multiplicative group on the additive group. In §3 we describe the
  results of Landau–Pollack–Slepian. In §4 we describe the recent reformulation by Alain Connes. In §5 we describe
  the q-analogue interpolating between the p-adic numbers and the reals. In §6 we give a heuristic proof of the
  Riemann hypothesis." — MSC 11M26. Relevant to any Connes-side comparison; **"heuristic proof" is his own label**.
- Soulé, p. 167 (PDF 178): extends Connes' [C] operator D_χ to Jacquet–Godement L(s, π) of simple algebras;
  "we define a Hilbert space H_π and a natural operator D_π on H_π, the spectrum of which is the set of imaginary
  parts of the critical zeroes of L(s, π) (Theorem 2)"; he notes multiplicities "need not coincide" and that trace
  formulas analogous to [C] Th. 3–5 look "mysterious". MSC 11M26 11F55 11F70.
- Lapidus–van Frankenhuysen, p. 113 (PDF 124): explicit formula with error term for the prime orbit counting
  function of a suspended flow; self-similar flows; lattice vs. nonlattice; MSC 11N05, 28A80, 58F03, 58F20.
  (Suspended-flow prime orbit theorem — adjacent to the program's mapping-torus material, C5(a), but analytic
  number theory of fractal strings, not foliations.)
- Perry, p. 145 (PDF 156): survey of Selberg zeta for infinite co-volume Kleinian groups; Patterson–Sullivan;
  scattering resonances. Not bearing.
- Fel'shtyn, p. 67: dynamical zeta functions in Nielsen fixed-point theory — possible relative of the Fuller-index
  reading in C5(a) (not read beyond the TOC).
- The note's own p. 42 sentence "any one-codimensional foliation given by a closed one-form without singularities is
  Riemannian" and p. 45 "Then F is Riemannian" are printed **without proof or citation** — a future session wanting
  a citation for "transverse flow ⇒ Riemannian foliation (closed ω_φ)" should use KMNT Lemma 1.9, not this note.
- The note's [AK1] = Álvarez López–Kordyukov, *Long time behaviour of leafwise heat flow for Riemannian foliations*,
  cited as "Preprint dg-ga/9612010, 1996. To appear in Compositio Math." — Thm 1.1 (leafwise Hodge decomposition
  for Riemannian foliations) is attributed to its Cor. 1.3. The counterexample paper [DS] (= r3s-33) is cited as
  "To appear in Ann. Inst. Fourier 2001" and is the source for "in general for codimension ≥ 2 this passage is not
  possible" (p. 41; "[DS] §2", p. 49).

## §5. Caveats for `corpus-routing.md`

- `r4-05` — the whole 210-page volume, IMAGE-ONLY (tiff2pdf, no text layer); `pdftotext` returns nothing; grep
  cannot be used. Fix: render with `pdftoppm -r 110..130 -f N -l M -png` and read by vision; PDF page = printed
  page + 11; Deninger–Singhof = PDF 52–66.
- `r4-05` — the symbol α in the note (§2.5, Thm 2.6, E_α, e^{αt}) is the eigenvalue of the flow generator Θ on
  reduced leafwise cohomology, NOT Deninger's conformal exponent α of φ^{t*}g_F = e^{αt}g_F. A grep-style search for
  "α = 0" in this note would hit the wrong object. Fix: cite the note only for (2.8) −Θ² = ∆|ker under ISOMETRY and
  for Thm 2.4/2.6; never for the "α = 0 remark".
- `r4-05` — the note's non-degeneracy (p. 45) and ALK 2002's "simple" (Warsaw p. 162) are equivalent under
  transversality but worded differently; the note's ε_γ(k) is the sign at the k-th iterate. Fix: when comparing with
  ALK Thm 1.3, read the sign as k-dependent (see a01-12 vision note).
- `r4-05` — Deninger's later bibliographies cite this note as "[21]" ([Den05] = math/0505354) and ALK 2002 as "[11]
  manuscript 2000"; both resolve to these printed pages 41–55, no discrepancy in title or authors.

## §6. Honesty

Every page of the article (printed 41–55, PDF 52–66) plus PDF 1–12 and 67 was rendered and read by vision this
session; no text layer exists, no OCR was used, nothing was fetched from the network. Quotations are my
transcriptions of the renders; formula typography (bars, tildes, hats) was checked at 130 dpi and I found nothing
illegible. The four "other article" notes in §4 rest on first pages only (PDF 104, 124, 156, 178). The equivalence
"non-degenerate ⇔ simple" and the identification of ω_φ with KMNT's canonical 1-form are marked as my inferences.

Status: COMPLETE.
