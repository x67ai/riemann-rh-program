# THE C⁰ SUP-NORM AS A SEMINORM OF THE "NATURAL FRÉCHET TOPOLOGY" ON LEAFWISE FORMS
## Session 17, direction C3-r, queue item 5 — closing the one recalled step in Theorem A(B)
## Stamp: Sun Sep  6 15:58:22 IST 2026

**Task.** `f1-check-O.md` §9 (Session 16, Opus 5) lists one recalled, load-bearing step: that the C⁰
sup-norm is among the seminorms of Deninger's "natural Fréchet topology" on leafwise forms ([x-20] p. 14),
which §2.1(a) uses to descend the Ruelle–Sullivan current C_µ to reduced cohomology H̄²_F. This file matches
Deninger's phrase against the explicit definitions printed by Álvarez López–Kordyukov–Leichtnam (ÁLKL) in
*Analysis on Riemannian foliations of bounded geometry* (arXiv:1905.12912v3, `fetched-r3/r3s-40-…pdf`) and in
the memoir *Trace formula for foliated flows* (arXiv:2402.06671v2, `fetched-r3/r3s-39-…pdf`), and then
relabels the §9 reliance as printed. All quotations below were extracted by me this session with
`pdftotext -layout` from the PDFs named; page numbers are the printed page numbers of each PDF.

**Verdict: CLOSED for the foliated-manifold reading (the setting of [x-20] p. 14, the page §9 cites),
as printed in ÁLKL. For the foliated-space (lamination) reading of Theorem A(B) — Deninger's p. 29 phrase —
the reliance does not disappear but narrows to one printed reference that is not on disk: Moore–Schochet,
*Global analysis on foliated spaces* (Deninger's [33]), Chapter II, whose tangentially-smooth topology is
built from the same seminorms with leafwise derivatives only. Details in §4.**

---

## §1. The reliance, verbatim

`f1-check-O.md` §9, "Recalled, not re-verified at a source":

> "That the Fréchet topology on A^n_F(X) has the C⁰ sup-norm among its seminorms. Deninger says 'the
> natural Fréchet topology' without listing the seminorms; **this is the one place where I rely on the
> standard reading of an unspecified phrase**, and §2.1(a) depends on it. If that topology were defined
> by seminorms not dominating the sup-norm, C_µ's descent to H̄²_F would need a separate argument."

What §2.1(a) actually uses: |⟨C_µ, ω⟩| ≤ ‖ω/λ_g‖_∞ · m, so C_µ is bounded for the sup-norm; if the
sup-norm is a continuous seminorm of the topology τ that defines the closure of Im d_F, then C_µ is
τ-continuous, vanishes on cl_τ(Im d_F), and descends to H̄²_F. The reliance is exactly: *τ is finer than
the sup-norm topology.*

## §2. Definition 1 — Deninger, [x-20] (2005), verbatim

**p. 13** (setting of §4 "Foliations and their cohomology"): "A d-dimensional foliation F = F_X of a smooth
manifold X of dimension a is a partition of X into immersed connected d-dimensional manifolds F, the
'leaves'." … "On an open subset U of X the differential forms of order n along the leaves are defined as
the smooth sections of the real vector bundle Λ^n T^*F, A^n_F(U) = Γ(U, Λ^n T^*F)."

**p. 14:** "For our purposes these invariants are actually too subtle. We therefore consider the reduced
leafwise cohomology H̄^n(X, R) = Ker d^n_F / \overline{Im d^{n−1}_F}. Here the quotient is taken with respect
to the topological closure of Im d^{n−1}_F in the natural Fréchet topology on A^n_F(X). The reduced
cohomologies are nuclear Fréchet spaces."

**p. 28–29** (foliated spaces): "Explicitly A^i_F(U) = Γ(U, Λ^i T^*F) for every open subset U of X. Here
sections are by definition continuous and smooth on the leaves." … "As before, one also considers the
maximal Hausdorff quotient H̄^i(X, R) of this cohomology, obtained by dividing by the closure of Im d_F in
the natural Fréchet topology." And the **p. 29 Warning:** "A manifold with a (smooth) foliation is also a
foliated space. However the sheaves R and A^i_F are different in the two contexts: In the first one
demands smoothness also in the transversal direction whereas in the second one only wants continuity."

Deninger names no seminorms on either page. His only pointer in §7 is to "[33] p. 43" (Moore–Schochet,
*Global analysis on foliated spaces*, MSRI Publ. 9, 1988) for the tangent bundle T F of a foliated space
(p. 28), not for the topology.

## §3. Definition 2 — ÁLKL, verbatim

### 3.1 The bounded-geometry paper, r3s-40 (arXiv:1905.12912v3)

**§2.1 p. 4:** "Let M be a (smooth, i.e., C^∞) manifold of dimension n, and let E be a (smooth complex)
vector bundle over M. The space of smooth sections, C^∞(M; E), is equipped with the (weak) C^∞ topology
(see e.g. [32])." — [32] = M.W. Hirsch, *Differential topology*, GTM 33 (p. 42 of the PDF, bibliography).

**§3.2 p. 11** ("Uniform spaces"): "For every m ∈ N_0, a function u ∈ C^m(M) is said to be C^m-uniformly
bounded if there is some C_m ≥ 0 with |∇^{m′} u| ≤ C_m on M for all m′ ≤ m. These functions form the uniform
C^m space C^m_ub(M), which is a Banach space with the norm ‖·‖_{C^m_ub} defined by the best constant C_m. As
usual, the super-index 'm' may be removed from this notation if m = 0, and we have C_ub(M) = C(M) ∩ L^∞(M).
Equivalently, we may take the norm ‖·‖′_{C^m_ub} defined by the best constant C′_m ≥ 0 such that
|∂_I(u y_p^{−1})| ≤ C′_m on B for all p ∈ M and |I| ≤ m; … The uniform C^∞ space is C^∞_ub(M) =
⋂_m C^m_ub(M), with the inverse limit topology, called uniform C^∞ topology. … **Of course, if M is
compact, then the C^m_ub topology is just the C^m topology, and the notation ‖·‖_{C^m} and ‖·‖′_{C^m} is
preferred.**" Same page, for bundles: "For a Hermitian vector bundle E of bounded geometry over M, the
uniform C^m space C^m_ub(M; E), of C^m-uniformly bounded sections, can be defined by introducing
‖·‖′_{C^m_ub} like the case of functions, using local trivializations of E to consider every u y_p^{−1} in
C^m(B, C^l) for all u ∈ C^m(M; E). Then, as above, we get the uniform C^∞ space C^∞_ub(M; E) … equipped
with the uniform C^∞ topology."

**§4.10.1 p. 23** ("The leafwise complex"): "Let d_F ∈ Diff^1(F; ΛF) be given by (d_F ξ)|_L = d_L(ξ|_L) for
every leaf L and ξ ∈ C^∞(M; ΛF). Then (C^∞(M; ΛF), d_F) is a differential complex, called the leafwise
(de Rham) complex. This gives rise to the (reduced) leafwise cohomology (with complex coefficients),
H^*(F) = H^*(F; C) and H̄^*(F) = H̄^*(F; C)."

### 3.2 The memoir, r3s-39 (arXiv:2402.06671v2)

**§1.1 p. 1** ("Deninger's program"): "The leafwise cohomology, H^•(F), is defined with the complex of
differential forms on the leaves that are smooth on M, C^∞(M; ΛF) (ΛF = ⋀T^*F ⊗ C), equipped with de Rham
differential operator along the leaves, d_F. This differential complex is not elliptic, it is only leafwise
elliptic. Therefore H^•(F) may be of infinite dimension and non-Hausdorff **with the topology induced by
the C^∞ topology**. Thus it makes sense to consider the reduced leafwise cohomology, H̄^•(F) = H^•(F)/\overline{0}."

**§2.1.2 p. 10, (2.1.2):** "For any open U ⊂ R^n … we use the Fréchet space C^∞(U) of smooth (K-valued)
functions on U, whose topology is described by the semi-norms ‖u‖_{K,C^k} = sup_{x∈K, |I|≤k} |∂^I u(x)|, for
any compact K ⊂ U, k ∈ N_0 and I ∈ N_0^n, with standard multi-index notation."

**§2.1.4 p. 11:** "Consider the Fréchet space C^∞(M; E) of smooth sections of E, whose topology is described
by semi-norms ‖·‖_{K,C^k} defined like in (2.1.2), using charts (U, x) of M and diffeomorphisms of
triviality E_U ≡ U × K^l with K ⊂ U."

**§2.1.13 p. 19:** "If moreover C is a TVS and d is continuous, then (C, d) is called a topological complex.
… Its maximal Hausdorff quotient, H̄^•(C, d) := H^•(C, d)/\overline{0} ≡ ker d/\overline{im d}, is called the reduced
cohomology."

**§2.4.3 p. 28** (the C^m_ub norms, identical in substance to r3s-40 §3.2): "These functions form the uniform
C^m space C^m_ub(M), which is a Banach space with the norm ‖·‖_{C^m_ub} defined by the best constant C_m. As
usual, we write C_ub(M) = C^0_ub(M) = C(M) ∩ L^∞(M). … The uniform C^∞ space is the Fréchet space
C^∞_ub(M) = ⋂_m C^m_ub(M), with the semi-norms ‖·‖_{C^m_ub} or ‖·‖′_{C^m_ub}."

**§3.2.1 p. 82** ("The leafwise complex"): "Then (C^∞(M; ΛF), d_F) is a differential complex, called the
leafwise or tangential (de Rham) complex. The elements of C^∞(M; ΛF) are called leafwise forms … The
leafwise complex is not elliptic if n′ > 0, and therefore it makes sense to consider also its reduced
cohomology H̄^•(F) (Section 2.1.13)."

## §4. The match

**4.1 Foliated manifolds (Deninger p. 14; Theorem A(B) read on a compact foliated manifold).** Both authors
take the same space, A^n_F(X) = C^∞(M; Λ^n T^*F) = smooth sections of a smooth vector bundle, and the same
quotient, ker d_F / closure(im d_F). ÁLKL, writing explicitly about Deninger's program, name the topology:
"the topology induced by the C^∞ topology" (memoir p. 1), i.e. the weak C^∞ topology of C^∞(M; E) (r3s-40
p. 4; memoir p. 11), whose defining seminorms are ‖u‖_{K,C^k} = sup_{x∈K, |I|≤k} |∂^I u(x)| in charts and
trivializations (memoir (2.1.2), p. 10). The k = 0 member of that family is the sup over a compact chart
piece of the trivialized section. On a **compact** M there is a finite family of charts (U_i, x_i) with
compact K_i ⊂ U_i covering M, and any continuous fiber metric on Λ^n T^*F is comparable, on each K_i, with
the Euclidean norm of the trivialization (continuity and compactness). Hence
sup_M |u| ≤ C · max_i ‖u‖_{K_i, C^0}, i.e. **the C⁰ sup-norm is dominated by finitely many defining
seminorms and is therefore a continuous seminorm of the C^∞ topology.** r3s-40 §3.2 p. 11 says the same
thing in its own notation and in one sentence: the m = 0 norm ‖·‖_{C^0_ub} is the best constant with |u| ≤ C_0
on M, i.e. exactly the sup-norm; C^∞_ub(M; E) carries the inverse-limit topology of these norms (the
sup-norm being the first); and "if M is compact, then the C^m_ub topology is just the C^m topology", so
C^∞_ub(M; E) = C^∞(M; E) with the sup-norm among its defining seminorms outright. The two definitions
match, and the recalled step is printed. No change to §2.1(a) or to Theorem A(B)'s manifold reading.

Two remarks. (i) The identification "Deninger's natural Fréchet topology = the C^∞ topology" is
ÁLKL's printed reading of Deninger (memoir p. 1), not Deninger's own sentence; Deninger prints no seminorms.
That is as close as the fetched corpus comes, and it is the reading every printed treatment of the reduced
leafwise cohomology uses. (ii) The property used — "τ is finer than the sup-norm topology" — is exactly
what "sup-norm is a continuous seminorm" says; if a reader preferred any other Fréchet topology on
C^∞(M; ΛF) with continuous d_F and pullbacks, the argument would need re-checking, but no such alternative
is printed anywhere in the corpus.

**4.2 Foliated spaces / laminations (Deninger p. 29; Theorem A(B) as stated, on a compact foliated space).**
Here A^i_F(X) consists of sections "continuous and smooth on the leaves" (p. 28), and the p. 29 Warning
says the sheaf differs from the manifold one. ÁLKL's three printed definitions (§3 above) are all for smooth
manifolds M and smooth bundles E; neither r3s-39 nor r3s-40 defines a topology on tangentially-smooth forms
of a foliated space. So the fetched sources close the manifold half only. For the lamination half the
standard construction is the tangentially-smooth (C^{∞,0}) topology: the same seminorms as (2.1.2), sup over
compact chart pieces of leafwise derivatives up to order k, with no transverse derivatives — its k = 0
seminorm is again the local sup-norm, and compactness of X gives the global sup-norm as above. That is the
topology of Moore–Schochet 1988 Chapter II (tangential cohomology), which is Deninger's [33] and the
reference he gives for foliated spaces (p. 28) — **not on disk, and therefore still recalled.** The
reliance thus narrows from "the standard reading of an unspecified phrase" to "Deninger's p. 29 phrase means
Moore–Schochet's tangentially-smooth topology". Should a reader want it printed: Moore–Schochet Ch. II is the
one fetch (optional; `FETCH-LIST-ROUND4.md` is the sponsor's list — this file does not add to it).

**4.3 What a mismatch would have changed.** None found. Had the topology been defined by seminorms not
dominating the sup-norm, §2.1(a) would need C_µ's continuity re-proved for that topology; nothing else in
Theorem A(B) depends on the choice. Since both printed definitions include the sup-norm (manifold case) and
the only unprinted case (laminations) uses the same family with fewer derivatives, §2.1(a) stands as written.

## §5. The relabeling of §9 "as printed"

Replacement sentence for the §9 bullet (entered below as a dated block after the bullet, not by
rewriting it):

> "That the Fréchet topology on A^n_F(X) has the C⁰ sup-norm among its seminorms — PRINTED for foliated
> manifolds: Deninger's 'natural Fréchet topology' is the C^∞ topology of C^∞(M; ΛF) (ÁLKL memoir
> arXiv:2402.06671v2 §1.1 p. 1, §2.1.4 p. 11 with the seminorms (2.1.2) p. 10, §3.2.1 p. 82; ÁLKL
> arXiv:1905.12912v3 §2.1 p. 4, §4.10.1 p. 23), and on compact M its defining seminorms ‖·‖_{C^m}
> (= ‖·‖_{C^m_ub}) begin with the sup-norm ‖·‖_{C^0} = sup_M |u| (arXiv:1905.12912v3 §3.2 p. 11: 'if M is
> compact, then the C^m_ub topology is just the C^m topology'; memoir §2.4.3 p. 28). For foliated spaces
> (Deninger p. 29) the same family with leafwise derivatives only is Moore–Schochet 1988 Ch. II (Deninger's
> [33]), not on disk — that half remains recalled, now with a named printed source."

## §6. Honesty — read versus recalled

Read this session, by me, from the PDFs on disk: [x-20] pp. 13–14, 28–29 and the bibliography entries
[20], [33]; r3s-40 §2.1 p. 4, §3.1–3.2 pp. 9–11, §4.10.1 p. 23, §5 pp. 29–30 (Prop. 5.6–5.7 context), the
bibliography entry [32]; r3s-39 §1.1 p. 1, §2.1.2 p. 10, §2.1.4 p. 11, §2.1.13 p. 19, §2.4.1–2.4.3 pp. 27–29,
§3.2.1 p. 82; `f1-check-O.md` §0, §2.1(a)–(c), §9. Recalled: that Moore–Schochet Chapter II defines the
tangential de Rham complex with the topology of uniform convergence of tangential derivatives on compacta
(the book is not on disk); the elementary comparability of a continuous fiber metric with a trivialization's
Euclidean norm on a compact set. Not touched: any file other than this one and the §9 dated block in
`f1-check-O.md`.
