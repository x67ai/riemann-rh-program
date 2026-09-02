# DQ-M — measured trace formula for orbit continua (probe O)

**Program:** RH research program, direction C3-r (geometric substrate for a Weil-positivity proof of RH), milestone M2c, Route 2 (solenoid intermediate), blocker S4.
**Date:** 2026-09-02 (Session 14). **Author:** probe O (independent; a parallel probe on a different model was run on the same charter — nothing here assumes anything about it).
**Charter:** decide DQ-M (`results/c3-r/probe-9.4-note.md` §8 item 2) in the MODEL WORLD. Program (1) the trivial model; (2) the nontrivial model inside an aperiodic ambient flow, with [ALKL]'s formula quoted from the memoir on disk, the exact place where hypothesis H4 is consumed, and whether the sum over orbits may be replaced by an integral against a transverse measure; (3) consequences for Q*.
**Standing orders:** 5 (nothing load-bearing from memory; every source claim read from the on-disk PDF at a stated page) and 7 (everything believed new is tagged `[novelty: single-check]` and listed in the novelty ledger). U.S. English.
**Status:** COMPLETE. Written in two sittings (the first was cut short by a usage limit); the second re-extracted every source anchor from the PDFs, re-derived every load-bearing proof, corrected two page citations, one proof, one citation label and one non-example, and added Lemma 4.0, Remark 4.0′, Lemma 5.1, Remark 9.3, Theorem F and Construction 12.1. Full record in §1 ("Verification-pass record") and §13.

---

## §0. VERDICT (stated first)

> **THEOREM (NO).** In the model world DQ-M specifies — a [Den05] §7.7 suspension `Y = M̄ ×_Λ R` whose periodic set is a continuum `B × S¹` of closed orbits of common length ℓ — **the distributional trace of the flow on leafwise forms EXISTS, and its orbital side is NOT the Haar average of the single-orbit contribution.**
>
> The aggregate contribution of the continuum is
> ```
>            ℓ · ι_k(B) · δ_{kℓ}          (k ∈ Z^×),      ι_k(B) ∈ Z,
> ```
> where `ι_k(B)` is the **fixed-point index** of the leafwise return map `φ^{kℓ}` on B — a Z-valued topological invariant. The Haar-averaged proposal predicts `ℓ · 1 · δ_{kℓ}`. The two agree **iff ι_k(B) = 1**.
>
> Three fully computed counterexamples in the model world (§7), each a genuine [Den05] §7.7 suspension with `dim F = 2` (the dimension Deninger's program needs) and a continuum of closed orbits of common length ℓ:
>
> | model | continuum B | true weight ι | Haar prediction |
> |---|---|---|---|
> | `Y = S² × (R/ℓZ)`, φ = rotation | `B = S²` | **+2** | +1 |
> | `Y = T² × (R/ℓZ)`, φ = rotation | `B = T²` (compact group, Haar) | **0** | +1 |
> | `Y = Σ_g × (R/ℓZ)`, φ = rotation | `B = Σ_g` | **2 − 2g** | +1 |
> | mapping torus of a diffeo of S² with Cantor fixed set (§7.4) | `B ≅` Cantor set | **+2** | ±1 |
> | mapping torus of `(ψ(x),y)` on T² (§7.5) | `B ≅ S¹` (compact group, Haar) | **0** | ±1 |
> | genuine solenoid, `Γ̄ = Z_2`, `M = T²`, `f = (2x,y)` (§10) | `B ≅ S¹` (compact group, Haar) | **0** | ±1 |
>
> **Sharper, and this is the content:** in DQ-M's own trivial model with `dim F = dim B`, the exact evaluation is
> ```
>      Σ_n (−1)^n Tr(φ* | H̄^n(F))  =  χ(B) · ℓ · Σ_{k ∈ Z} δ_{kℓ} ,
> ```
> so the weight of the continuum is **χ(B), the Euler characteristic**, and the DQ-M identity holds iff χ(B) = 1. For B a compact group this forces B = {1}: a single orbit. **A Haar-measured orbit continuum weighs exactly zero, not one.**
>
> **Three further theorems:**
> * **(Equivariance no-go, Theorem D, §9 — conditional; see §9.3 for its exact grade.)** If the continuum B is an infinite profinite group and the model carries any symmetry group acting on B by translations (the exact property that made Haar measure the *canonical* candidate in 9.4 §7 Road 2 — Aut(C) acts transitively on B_p by translations), then the index measure `ι` is a translation-invariant Z-valued finitely additive measure on the clopen algebra of B, and **every such measure is identically 0.** The canonicity that recommends Haar is precisely what forces the weight to vanish.
> * **(Category theorem, Theorem E, §5.)** In a [Den05] §7.7 suspension the closed orbits are in canonical bijection with the finite f-orbits on the *base manifold* M ([Den05] = `x-20`, p. 35, verbatim). Hence an orbit continuum is always a **leafwise** object. Haar measure on B is a **leafwise** measure; only **transverse** measures enter the trace formula linearly, and leafwise data enters only through index densities (the leafwise Euler density and the signs ε). DQ-M's phrase "the transverse measure on the continuum" has no referent in the framework: it is a category error, and §5 proves it is one.
> * **(Index–measure dichotomy, Theorem F, §11.1.)** The general form of the verdict, and the proposed text of new ledger row W13: in a codimension-one foliated flow the *only* transverse direction is the flow direction and it is already spent on the factor `ℓ(γ)`; orbit families deform leafwise (`Nφ ≅ TF`); leafwise data enters the trace formula only through index densities; so a family's multiplicity is a fixed-point index, never a transverse measure. The one regime where an orbit family is genuinely transverse is `dim F = 0` — and there the cohomological trace does not exist at all (Prop. 4.3).
>
> **What is NOT claimed.** This is a theorem in the model world, not in `X_0 = X(Spec Z)`. `X_0` is infinite-dimensional, non-Hausdorff along packets, and is not known to be a foliated space; no trace formula exists for it. The verdict therefore does **not** kill S4, and does **not** fire the C3 kill-criterion. What it kills is **Road 2** of `probe-9.4-note.md` §7 ("renounce selection; Haar-average the packet") **as a repair of the orbit count inside any trace formula of the Deninger/ÁLK02/ALKL type**, and it forbids the re-scoping of Q* that Road 2 proposed.
>
> **One positive by-product (a different re-scoping of Q*, §12).** The trace formula does not demand *one orbit per prime*; it demands **index one per prime**. `Q*`'s clause "meeting each packet in exactly one orbit" may be relaxed to "meeting each packet in a compact orbit family of fixed-point index 1". This is **not vacuous**: Construction 12.1 exhibits a [Den05] §7.7 suspension of `S²` whose periodic set is a closed disk `D` of degenerate closed orbits of length ℓ plus one simple orbit, with `ind(h^k, D) = +1` for every `k ∈ Z^×` — a continuum that weighs exactly one orbit. But index-1 continua are never homogeneous (Lemmas 9.1–9.2), so this exit is disjoint from Road 2 and is not available for Deninger's packets, which are homogeneous by construction.

---

## §1. Sources read this session, with pages

All page references are to the **printed** page of the document. Every quotation below was read from the on-disk PDF via a fresh `pdftotext -layout` extraction; nothing in this note is recalled.

**Verification-pass record (this session).** This note was written across two sittings; the second re-extracted **every** anchor listed below from the PDFs and re-derived the load-bearing proofs independently. All [Den05] anchors (pp. 20, 21, 22, 33, 34, 35), all [ALKL] anchors (pp. v, 2, 3, 6, 8, 71, 99, 100, 101, 153, 154, 155, 156) and both [Lei06] anchors (pp. 3, 17) were confirmed **verbatim**. Two page citations in the first draft were **wrong and have been corrected**: [ALKL] Theorem 1.3.10 is on printed **p. 8** (not 7 — Theorem 1.3.8 is on p. 6, the statement of 1.3.10 falls on the next printed page), and the Guillemin–Sternberg expression together with the ÁLK00 formula in [Lei06] is on printed **p. 3** (not 4). One proof step was **wrong and has been replaced** (Lemma 9.2, step (b): the first draft enumerated the open normal subgroups of `B`, which presumes there are countably many — false in general, e.g. for `B = (Z/2)^I` with `I` uncountable; the maximal-index argument now given uses no enumeration). Everything else below survived the re-check unchanged, and the second sitting added Lemma 4.0, Remark 4.0′, Lemma 5.1, Theorem F, Construction 12.1, and the calibration Remark 9.3.

**Source-tag caution.** `[Lei06]` in this note denotes `r3s-21` = Leichtnam, arXiv:math/0603576v2 (*Scaling group flow and Lefschetz trace formula for laminated spaces with p-adic transversal*). Two collisions to keep straight: the program's own `m2c-feasibility-ledger.md` calls this same file **[Lei07]**; and *inside* that paper the symbol "[Lei06]" refers to a different, then-forthcoming work of the author. Nothing here cites either of those.

| tag | file on disk | pages read | what was taken |
|---|---|---|---|
| **[Den05]** | `fetched/x-20-deninger-2005-arithmetic-geometry-and-analysis-on-foliated-spaces.pdf` (PDF page = printed page) | 20, 21, 22, 33, 34, 35 | §5 non-degeneracy hypothesis; ε_x, ε_γ(k); Conjecture 5.1 (22); Theorem 5.3 = ÁLK02 formula (23); Theorem 5.4; §7.7 suspension construction; Theorem 7.8; χ_Co(F,μ) = χ(M)·l |
| **[ALKL]** | `fetched-r3/r3s-17-alvarez-lopez-kordyukov-leichtnam-trace-formula-foliated-flows-arxiv-2402.06671v1-SESSION8-FETCH.pdf` (**PDF page = printed page + 6**) | v, 1, 2, 3, 4, 5, 6, 7, 8, 71, 99, 100, 101, 153, 154, 155, 156 | abstract; §1.1–§1.2 (leafwise Hodge for Riemannian foliations); §1.3.1 (definition of a simple closed orbit, ℓ(c), ε_c(k)); Theorems 1.3.7, 1.3.8, 1.3.10; §2.9.11 (simple fixed point, ε_p, Proposition 2.9.6); §4.1.1 (C(φ), P(φ), simplicity ⟹ local finiteness); §4.1.2 (Nφ ≅ TF on M¹; Hector case (c)); §7.3 (Theorem 7.3.1, Proposition 7.3.2, properties (N)–(R), display (7.3.8)) |
| **[Lei06]** | `fetched-r3/r3s-21-leichtnam-scaling-group-flow-laminated-p-adic-transversal-arxiv-math0603576v2-SESSION8-FETCH.pdf` (PDF page = printed page) | 3, 17 | the ÁLK00 formula as Leichtnam states it; the **Guillemin–Sternberg local expression** for the geometric contribution of a closed orbit; Theorem 2 = the *laminated, transverse-measure* trace formula, and its hypotheses ("closed orbits … are non degenerate", "L has a dense leaf") |
| **[x-03]** | `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` | — | **not re-extracted this session.** All facts about X_0 used here (packets, B_p, non-Hausdorffness, Theorem A) are taken from the *program's own* referee-passed record `results/c3-r/probe-9.3-adjudication.md` §2–§4, which re-derived them from this file. Flagged accordingly in §13. |
| program docs | `results/c3-r/probe-9.3-adjudication.md`; `results/c3-r/probe-9.4-note.md` §7–§8 | full / §7–§8 | binding context: Theorem A, Q* (§5 of the adjudication), Road 2 and the DQ-M charter statement |

**Verbatim anchors** (each transcribed from the extraction, not paraphrased):

* **[Den05] p. 20**, the non-degeneracy hypothesis: *"Assume that the fixed points and the periodic orbits of the flow are non-degenerate in the following sense: For any fixed point x and every t > 0, the tangent map T_xφ^t has eigenvalues different from 1. For any closed orbit γ of length l(γ) and any x ∈ γ and integer k ≠ 0 the automorphism T_xφ^{kl(γ)} of T_xX should have the eigenvalue 1 with algebraic multiplicity one."*
* **[Den05] p. 21**: *"For a closed orbit γ and k ∈ Z ∖ 0 set ε_γ(k) = sgn det(1 − T_xφ^{kl(γ)} | T_xX/RY_{φ,x}). It does not depend on the point x ∈ γ."*
* **[Den05] p. 22, Theorem 5.3 ([2] = ÁLK02)**: *"Under the conditions of (5.2), for every test function φ ∈ D(R) = C_0^∞(R) the operator A_φ = ∫_R φ(t)φ^{t*} dt on Ĥ^n(X,R) is of trace class. Setting Tr(φ*|H̄^n(X,R))(φ) = tr A_φ defines a distribution on R. The following formula holds in D′(R): Σ_{n=0}^{dim F}(−1)^n Tr(φ*|H̄^n(X,R)) = χ_Co(F,μ)δ_0 + Σ_γ l(γ) Σ_{k∈Z∖0} ε_γ(k) δ_{kl(γ)}."* — preceded on the same page by *"We assume that all periodic orbits are non-degenerate."*
* **[Den05] p. 35, §7.7**: *"The map γ ↦ γ_M = γ ∩ (M̄ ×_Λ Λ) gives a bijection between the closed orbits γ of the flow on X and the finite orbits γ_M of the f̄- or Λ-action. These in turn are in bijection with the finite orbits of the original f-action on M. We have: l(γ) = |γ_M| l."* and *"Theorem 7.8 In the situation of 7.7 **assume that all periodic orbits of φ are non-degenerate**."* and *"χ_Co(F,μ) = χ(M) · l."*
* **[ALKL] p. v (abstract)**: *"Assume the closed orbits of φ are simple and its preserved leaves are transversely simple."*
* **[ALKL] p. 2, (1.2.2)–(1.2.3)**: *"It follows that there is a leafwise Hodge decomposition C^∞(M;ΛF) = ker ∆_F ⊕ im d_F ⊕ im δ_F, and therefore the orthogonal projection Π_F = e^{−∞∆_F} to ker ∆_F induces a leafwise Hodge isomorphism H̄^•(F) ≅ ker ∆_F."*
* **[ALKL] p. 3**: *"The condition on c to be simple means that id − φ_*^{kℓ(c)} : T_pF → T_pF is an isomorphism for any p ∈ c and k ∈ Z^×, whose determinant is independent of p, and its sign denoted by ε_c(k)."*
* **[ALKL] p. 6, Theorem 1.3.8**: *"lim_{u↓0} ^b Str(P̄_{μ,u,f}) = ^bχ_{|ω¹|}(F¹) f(0) + Σ_c ℓ(c) Σ_{k∈Z^×} ε_c(k) f(kℓ(c)), where c runs in the set of closed orbits of φ."*
* **[ALKL] p. 8, Theorem 1.3.10**: *"L_dis(φ) = Σ_L χ(L) W_L + ^bχ_{|ω¹|}(F¹) δ_0 + Σ_c ℓ(c) Σ_{k∈Z^×} ε_c(k) δ_{kℓ(c)}."*
* **[ALKL] p. 71, §2.9.11**: *"Recall that a fixed point p of φ is called simple if the eigenvalues of φ_* : T_pM → T_pM are different from 1. This means that the graph of φ is transverse to ∆ in M² at (p,p); **in particular, p is isolated in Fix(φ)**. … Take any relatively compact open neighborhood W of p in U such that W ∩ Fix(φ) = {p}."* and **Proposition 2.9.6**: *"For all z ∈ C, lim_{t↓0} ∫_{q∈W} str(φ_z^* k_{z,t}(φ(q),q)) = ε_p(φ)."*
* **[ALKL] p. 99, §4.1.1**: *"Every simple closed orbit c, there are neighborhoods, V where c in M and I of ℓ(c) in R, such that c is the only closed orbit whose first positive period is in I … The flow φ is called simple if all of its fixed points and closed orbits are simple. **If moreover M is closed, then Fix(φ) is finite, and C_I(φ) are finite for all compact I ⊂ R. Therefore P(φ) is a discrete subset of R.**"*
* **[ALKL] p. 100, §4.1.2**: *"Moreover φ is transverse to the leaves on M¹. So there is a canonical isomorphism **Nφ ≅ TF** on M¹."*
* **[ALKL] p. 101**: Hector's cases; *"(c) F is given by a fiber bundle M → S¹ with connected fibers."*
* **[ALKL] p. 155, properties (N)–(R) in the proof of Proposition 7.3.2(ii)**: *"(N) There is a unique γ_0 ∈ Γ_l such that t_0 = −h_l(γ_0). (O) We have k_j := t_0/ℓ(c_j) ∈ Z … (P) There is some y_j ∈ L_l such that π_l : R × {y_j} → c_j is a C^∞ covering map … (Q) For all p̃ ∈ R × {y_j}, we have γ_0 · φ̃_l^{t_0}(p̃) = p̃. **(R) For all x ∈ R, every y_j is a simple fixed point of the diffeomorphism T_{γ_0}φ̃_{l,x}^{t_0} of L_l** with ε_{y_j}(T_{γ_0}φ̃_{l,x}^{t_0}) = ε_{c_j}(k_j, φ) = ε_{c_j}(k_j)."* followed by *"In particular, there are no other fixed points of T_{γ_0}φ̃_{l,x_j}^{t_0} in some open neighborhood W_j of y_j in L_l."*
* **[Lei06] p. 3**, the Guillemin–Sternberg local expression: *"the geometric contribution of a closed orbit ±kγ should be: l(γ)α(±kl(γ)) Σ_{j=0}^2 (−1)^j Tr((Dφ^{±kl(γ)})^* : ∧^j T_y^*F ↦ ∧^j T_y^*F) / |det(id − Dφ|_{T_yF}^{±kl(γ)})|."*
* **[Lei06] p. 17, Theorem 2**: *"Assume that the closed orbits γ of the flow φ^t acting on S = L×R^{+*}/q^Z are **non degenerate**. Assume the four properties (i) to (iv), that W(L,F) is a factor and that **L has a dense leaf**."*

---

## §2. DQ-M made precise

`probe-9.4-note.md` §8 item 2 poses:

> **DQ-M.** Let `Y = M̄ ×_Λ R` be a [Den05]-§7-type suspension whose periodic set is a continuum `B × S¹` of closed orbits of common length ℓ, B a Cantor group with Haar probability measure μ. Does the distributional trace of the flow on leafwise forms exist, with orbital side `∫_B (single-orbit contribution) dμ` = the single-orbit contribution?

Two things must be pinned down before the question has a truth value.

### 2.1 What "the single-orbit contribution" is

From [Den05] p. 22 (Theorem 5.3) and [ALKL] p. 8 (Theorem 1.3.10), which agree: a closed orbit c of least period ℓ(c) contributes to the orbital side
```
        ℓ(c) · Σ_{k ∈ Z^×}  ε_c(k) · δ_{k ℓ(c)} ,        ε_c(k) ∈ {±1}.
```
So "the single-orbit contribution" for an orbit of length ℓ with all ε = +1 is `ℓ Σ_{k∈Z^×} δ_{kℓ}`, and the Haar-averaged proposal is
```
   (DQ-M claim)     Σ_{orbits in the continuum}  ↝  ∫_B ( ℓ Σ_k ε δ_{kℓ} ) dμ(b)  =  ℓ Σ_k ε δ_{kℓ},
```
because μ is a probability measure and the integrand does not depend on b (all orbits have the same length ℓ; this constancy is exactly what 9.4 §7 Road 2 records).

### 2.2 What "the distributional trace" is

Two inequivalent objects go by that name, and DQ-M does not distinguish them. Both are on disk.

* **(T-coh) the cohomological (Lefschetz) trace.** [Den05] p. 22: `A_φ = ∫_R φ(t) φ^{t*} dt` on the Hilbert completion `Ĥ^n(X,R)` of the leafwise reduced cohomology is **of trace class**, and `Tr(φ*|H̄^n)(φ) := tr A_φ`. Equivalently [Den05] p. 35, Theorem 7.8, which sets `Tr(φ*|H̄^n(X,R)) := Σ_{λ ∈ Sp_n(Θ)} e^{tΘ}` where `Sp_n(Θ)` is *"the set of eigenvalues with their algebraic multiplicities of the infinitesimal generator Θ of φ^{t*} on H̄^n(X,R)"* (verbatim, p. 35). **Typographical note:** the printed summand is `e^{tΘ}`; since the sum is indexed by `λ ∈ Sp_n(Θ)`, the intended summand is plainly `e^{tλ}`, and that is how it is used below. This is a typo in the source, recorded here because the anchor is quoted. This is the trace whose alternating sum is the left-hand side of the dynamical Lefschetz trace formula, and the one Deninger's program needs: the sought spectral side is the set of zeros of ζ **with multiplicities**, i.e. the point spectrum of Θ on `H̄^1`, counted.
* **(T-meas) the measured (von Neumann / Ruelle–Sullivan) trace.** Given an invariant transverse measure Λ of F, one integrates the leafwise Schwartz kernel over the diagonal against Λ. [Lei06] p. 17 builds his Hilbert spaces `H^j_τ` with the Ruelle–Sullivan current `C(Λ)` of the transverse measure `Λ = μ_L dx`; note however that his `TR` is then the **ordinary** trace on that Hilbert space, and his part 1] asserts trace-classness — a hypothesis-laden statement (`W(L,F)` a factor, `L` has a dense leaf), not a free lunch.

**This note answers DQ-M for (T-coh)** — that is the trace "of the flow on leafwise forms" in the sense of every formula on disk, and the only one for which a trace formula exists. §4.3 computes (T-meas) as well in the one model where it is unambiguously defined, and records exactly why its apparent success there is an artifact of `dim F = 0`.

### 2.3 The hypothesis at issue: H4

Call **H4** the standing simplicity/non-degeneracy hypothesis. It appears in the sources in three equivalent guises:

* [Den05] p. 20: `T_xφ^{kℓ(γ)}` has eigenvalue 1 with **algebraic multiplicity one** (the eigenvector being the flow direction `Y_{φ,x}`);
* [Den05] p. 21 / [ALKL] p. 3: `id − φ_*^{kℓ(c)} : T_pF → T_pF` is an **isomorphism**, whose determinant's sign is `ε_c(k)`;
* [ALKL] p. 99: a simple closed orbit is **isolated among closed orbits of nearby period**, and on a closed manifold this forces `C_I(φ)` finite for compact `I` and `P(φ)` discrete.

An orbit continuum violates H4 maximally: if closed orbits of period ℓ accumulate at c, then `id − φ_*^{ℓ}` kills the accumulation direction inside `T_pF`, so `det(id − φ_*^{ℓ}|T_pF) = 0` and `ε_c(k)` is **undefined**. DQ-M is therefore, before anything else, a question about what replaces `ε_c(k)`.

The answer, visible already in the sources: [Lei06] p. 3 records the Guillemin–Sternberg local expression for the contribution of `±kγ`,
```
        ℓ(γ) α(±kℓ(γ)) ·  Σ_{j=0}^{2} (−1)^j Tr( (Dφ^{±kℓ(γ)})^* : ∧^j T_y^*F → ∧^j T_y^*F )
                          -----------------------------------------------------------------
                                        | det( id − Dφ^{±kℓ(γ)} |_{T_yF} ) |
```
The numerator is `det(id − Dφ^{±kℓ(γ)}|T_yF)` (the alternating sum of traces on exterior powers **is** the determinant of `id − Dφ`), so the quotient is `sign det(id − Dφ) = ε_γ(k)`. On a continuum **numerator and denominator both vanish**: the local formula is `0/0`. What resolves a `0/0` of an Euler-form-over-Jacobian type is an **index**, not a measure. Everything below is the rigorous version of that one-line diagnosis.

---

## §3. Where exactly H4 is consumed in ALKL's proof

[ALKL]'s trace formula is Theorem 1.3.10 (p. 8); the orbital half is Theorem 1.3.8 (p. 6), proved in Chapter 7 as Theorem 7.3.1 (p. 153) via Proposition 7.3.2 (p. 154). Tracking H4 through that proof:

**(H4-a) — the formula's right-hand side must be a distribution at all (setup, p. 99).**
[ALKL] §4.1.1: *"If moreover M is closed, then Fix(φ) is finite, and `C_I(φ)` are finite for all compact `I ⊂ R`. Therefore `P(φ)` is a discrete subset of R."* Without H4 the sum `Σ_c` in Theorems 1.3.8/1.3.10 is a sum over an **uncountable** index set of identical nonzero terms, hence not a distribution: the right-hand side is meaningless before any analysis begins. This is the first and crudest consumption.

**(H4-b) — the case split of Proposition 7.3.2 (p. 154).**
The proposition splits by a compact interval `I ⊃ supp f`: (i) `I ∩ P_l = ∅`, (ii) `I ∩ P_l = {t_0}`, (iii) `0 ∈ I`, `I ∩ P_l = ∅`. That this exhausts the cases *after shrinking `I`* is exactly the discreteness of `P(φ)` from (H4-a). With a continuum of orbits of common length ℓ the set `P` is still `ℓZ`, so this particular split survives; it is (H4-c) and (H4-d) that do not.

**(H4-c) — the finite list `C_{l,t_0} = {c_1, …, c_m}` and the isolating neighborhoods (p. 155).**
The proof of (ii) opens: *"let `C_{l,t_0} = {c_1, …, c_m}`"* and then, from property (R), *"In particular, there are no other fixed points of `T_{γ_0}φ̃^{t_0}_{l,x_j}` in some open neighborhood `W_j` of `y_j` in `L_l`. Then `π_l([0,ℓ(c_j)] × W_j)` is a neighborhood of `c_j`, whose interior is denoted by `V_j`, which does not intersect other closed orbits with period in `I`."* Both the finiteness of the list and the existence of the isolating `W_j` are H4. On a continuum, neither exists.

**(H4-d) — the local Lefschetz computation, Proposition 2.9.6 (p. 71).**
This is the load-bearing step: display (7.3.8) on p. 156 evaluates
```
   lim_{u↓0} ∫_{V_j} str( φ̃^{t_0*}_{l,z} T^*_{γ_0} k̃_{l,z,u}(T_{γ_0} φ̃^{t_0}_l(p̃), p̃) ) f(t_0) |ω_{b,l}|(p)  =  f(t_0) ℓ(c_j) ε_{c_j}(k_j),
```
using *"But, by Proposition 2.9.6, `lim_{u↓0} ∫_{W_j} str(φ̃^{t_0*}_{l,x,z} T^*_{γ_0} k̃_{l,x,u,z}(T_{γ_0}φ̃^{t_0}_{l,x}(y), y)) = ε_{y_j}(T_{γ_0}φ̃^{t_0}_{l,x}) = ε_{c_j}(k_j)`."* Proposition 2.9.6 is stated for a **simple** fixed point `p` and a neighborhood `W` with `W ∩ Fix(φ) = {p}` (p. 71). Its proof is *"like in the analytic proof of the Lefschetz trace formula [AB67]"*. This is the unique point at which the number `ε` — the ±1 that DQ-M wants to Haar-average — is produced. **It is produced as a local Lefschetz index of an isolated simple fixed point, and by nothing else.**

**(H4-e) — the ℓ(c) prefactor (p. 156).**
The factor `ℓ(c_j)` arises from the `∫_0^{ℓ(c_j)} … |dx|` in the displayed chain on p. 156: it is the length of the orbit in the *flow* direction, i.e. genuinely a transverse-measure factor. This is the **one** place where a measure legitimately enters an orbital term, and it measures the orbit's own circle — not a family of orbits. Note the asymmetry: the ℓ is a measure, the ε is an index. DQ-M proposes to append a *second* measure factor `μ(B) = 1` where the framework has an *index*.

**Diagnosis.** (H4-a) and (H4-c) are bookkeeping: they can be repaired by replacing the sum over orbits by a sum/integral over a **clopen decomposition of the continuum**. (H4-d) cannot be repaired by a measure: the object it produces is an index. §8 gives the correct replacement; §7 shows that the replacement is not `∫ dμ`.

**Note on the laminated precedent.** [Lei06] Theorem 2 (p. 17) is the *only* trace formula on disk that is genuinely laminated (Cantor/p-adic transversal) and built on a transverse measure — precisely the setting Road 2 would need. It **still** assumes *"the closed orbits γ of the flow φ^t … are non degenerate"*, and its orbital side is still a discrete sum over primitive closed orbits with integer coefficients. So the "measured" framework closest to Road 2 does not average orbits either; it counts them, and it needs H4 to do so.

---

## §4. Program item (1): the trivial model `Y = B × (R/ℓZ)`, computed honestly

Throughout, `S¹_ℓ := R/ℓZ` and `φ^t(b,s) = (b, s+t)`.

### 4.1 Which foliation, which spaces, which transverse measure

`Y = B × S¹_ℓ`. The flow must be **transverse to F** ([Den05] (5.2) p. 21: *"Let φ be a flow on X which is everywhere transversal to the leaves of F"*; [ALKL] p. 100: φ transverse on `M¹`). Hence the leaves are the slices `B × {s}` and
```
        dim F = dim B ,      codim F = 1 ,      F  has no preserved leaf (M⁰ = ∅).
```
* **Leafwise forms:** `C^∞(Y; Λ^nF)` = smooth families `s ↦ α_s ∈ Ω^n(B)`, `s ∈ S¹_ℓ`; `d_F = d_B`.
* **The trace:** (T-coh), i.e. `Tr(φ*|H̄^n(F))(f) = tr A_f`, `A_f = ∫_R f(t) φ^{t*} dt` ([Den05] p. 22), equivalently `Σ_{λ∈Sp_n(Θ)} e^{tλ}` ([Den05] p. 35).
* **The transverse measure:** the invariant transverse measure of F is `|ds|` on the circle factor, of total mass ℓ. **The Haar measure μ on B is *not* a transverse measure of F**; it is a measure along the leaves. This is not a quibble — §5 shows it is the whole obstruction.

Since `M⁰ = ∅`, [ALKL] Theorem 1.3.10 (p. 8) collapses to the ÁLK02 formula, i.e. [Den05] (23) p. 22:
```
   (TF)      Σ_{n} (−1)^n Tr(φ* | H̄^n(F))  =  χ_Co(F, μ_⊥) δ_0  +  Σ_γ ℓ(γ) Σ_{k∈Z^×} ε_γ(k) δ_{kℓ(γ)} ,
```
with `μ_⊥ = |ds|`. This is the identity DQ-M asks about.

**Two preliminaries that make the refutation airtight.** Both were added in the verification pass; neither was needed for the arithmetic of §§4.2–7, but a referee is entitled to both.

> **Lemma 4.0 (the `δ_0` coefficient is flow-independent, and equals `χ(B)·ℓ`).** Let `X` be a compact foliated space with `codim F = 1`, an invariant transverse measure `μ_⊥`, and a leafwise metric. Connes' Euler characteristic is
> ```
>        χ_Co(F, μ_⊥)  =  ∫  e(F, g_F)  dμ_⊥ ,
> ```
> the integral of the **leafwise Euler density** against the transverse measure ([ALKL] p. 3, which forms exactly this product: *"the product of the leafwise Euler density `e(F)` and `|ω^b|` … obtaining a b-calculus version of the Connes' `|ω^b|`-Euler characteristic of `F`"*). **This quantity does not refer to the flow at all.** For `Y = B × S¹_ℓ` with `F` the slice foliation, a product metric, and `μ_⊥ = |ds|`,
> ```
>        χ_Co(F, |ds|)  =  ∫_0^ℓ ( ∫_{B×{s}} e(B, g_B) ) ds  =  ∫_0^ℓ χ(B) ds  =  χ(B)·ℓ ,
> ```
> by Chern–Gauss–Bonnet on the closed manifold `B`. The same computation for the mapping torus of Setup 6.0 (each leaf `≅ Σ`, transverse mass ℓ) gives `χ_Co(F,|ds|) = χ(Σ)·ℓ`.

*Why this matters.* [Den05] p. 35 states `χ_Co(F,μ) = χ(M)·l` **inside Theorem 7.8**, whose blanket hypothesis is that all periodic orbits are non-degenerate — a hypothesis every model in this note violates on purpose. Lemma 4.0 re-derives the same value with no hypothesis on `φ` whatsoever, so the note never leans on a source statement outside its stated scope. (It also independently confirms [Den05]'s formula.)

> **Remark 4.0′ (the logic of the refutation, and why it needs no convention).** Theorem A below computes the **left-hand side** of (TF) exactly, as a locally finite sum of Dirac masses at `ℓZ` with explicit integer-times-ℓ coefficients. Suppose *any* identity of the shape "(LHS) = (a distribution supported at 0) + (orbital terms at the periods)" holds for one of these systems, with the orbital term of a length-ℓ orbit family of the DQ-M shape `w·ℓ·δ_{kℓ}`. Then, **comparing coefficients at `δ_{kℓ}` for `k ≠ 0` only**, `w = L(h^k)`. So the refutation is independent of
> * the `δ_0` convention (whether or not the `t = 0` term is `χ_Co δ_0`; Lemma 4.0 says it is, but nothing needs that);
> * the presence of any additional `t = 0` renormalization of the [ALKL] `bχ`/`Z_μ` type;
> * whether a trace formula for degenerate systems exists at all — if one exists, its `k ≠ 0` coefficients are forced; if none exists, DQ-M's premise ("the distributional trace … with orbital side …") fails outright.
>
> It is also independent of `μ`: DQ-M's proposed orbital side is `∫_B (ℓ Σ_k ε δ_{kℓ}) dμ(b)`, whose value is `ℓ Σ_k ε δ_{kℓ}` for **every** probability measure `μ` on `B`, since the integrand is constant in `b`. Nothing in the claim uses the group structure of `B` or the invariance of Haar. Hence a single model with `|L(h^k)| ≠ 1` refutes DQ-M for every choice of measure at once — and a model with `L(h^k) = 0` refutes it for every choice of **normalization** as well.

### 4.2 Case A: B a closed manifold (`dim F = dim B > 0`) — the exact evaluation

This is the honest trivial model **in the dimension Deninger's program needs**: `dim F = 2` when B is a surface, `dim Y = 3`.

> **Theorem 4.1 (trivial model, exact).** Let B be a closed connected orientable manifold, `Y = B × S¹_ℓ`, `F` the foliation by the slices `B × {s}`, `φ^t` translation in `S¹_ℓ`. Then every point of Y is periodic of least period ℓ; the leafwise reduced cohomology is
> ```
>     H̄^n(F)  ≅  C^∞(S¹_ℓ) ⊗ H^n(B; C) ,
> ```
> `A_f` is trace class on each, and
> ```
>     Tr(φ* | H̄^n(F))  =  ℓ · dim H^n(B;C) · Σ_{k∈Z} δ_{kℓ} ,
>     Σ_n (−1)^n Tr(φ* | H̄^n(F))  =  χ(B) · ℓ · Σ_{k∈Z} δ_{kℓ}.
> ```
> Consequently, in (TF), `χ_Co(F,|ds|) = χ(B)·ℓ` and the **orbital side is**
> ```
>     Σ_{k ∈ Z^×}  χ(B) · ℓ · δ_{kℓ} .
> ```

*Proof.* Every orbit is `{b} × S¹_ℓ`, of least period ℓ. F is a fibration `Y → S¹_ℓ`, hence Riemannian with the product bundle-like metric; by [ALKL] (1.2.2)–(1.2.3) (p. 2) leafwise Hodge theory applies and `H̄^n(F) ≅ ker ∆_F`, which for the product metric is `{s ↦ α_s : α_s ∈ H^n_{harm}(B)}` = `C^∞(S¹_ℓ) ⊗ H^n(B;C)` (finite-rank coefficients), with `φ^{s*}` acting purely by translation in the circle variable. `A_f` acts by convolution: `(A_f v)(t) = ∫_R f(s) v(t+s) ds = ∫_{S¹_ℓ} K(t,t') v(t') dt'` with smooth kernel `K(t,t') = Σ_{k∈Z} f(t' − t + kℓ)`. A smooth kernel on the closed manifold `S¹_ℓ` with finite-rank coefficients is trace class with `tr = ∫_0^ℓ tr K(t,t) dt = ∫_0^ℓ Σ_k f(kℓ) dt · dim H^n = ℓ Σ_k f(kℓ) · dim H^n(B;C)`. Summing with signs gives `χ(B)`. Finally the `k = 0` term of the answer is `χ(B) ℓ δ_0`, and [Den05] p. 35 gives `χ_Co(F,μ) = χ(M)·l` for a §7.7 suspension — which `Y = B × S¹_ℓ` is (take `M = B`, `f = id_B`, an unramified covering of degree 1; then `Γ_i = Γ` for all i, `Γ̄` is a point, `M̄ = M`, and `Y = M̄ ×_Λ R` with `Λ = ℓZ`). So the `δ_0` coefficients match identically, and the remaining terms are the orbital side. ∎

> **Corollary 4.2 (DQ-M is false in its own trivial model).** In Theorem 4.1 the aggregate orbital contribution of the continuum `B` of closed orbits of common length ℓ is
> ```
>      χ(B) × (single-orbit contribution),        NOT       ∫_B (single-orbit contribution) dμ = 1 × (single-orbit contribution).
> ```
> Equality holds **iff χ(B) = 1**. Explicitly:
> * `B = S²`: weight `+2`. (`Y = S² × S¹_ℓ`, `dim F = 2`.)
> * `B = T²`, a compact group with Haar probability measure: weight `0`.
> * `B = Σ_g`: weight `2 − 2g`.
> * `B = S¹`: weight `0`.
> * `B = pt` (a single orbit): weight `1` — the classical case, and the only compact-group case that works.

**Reading.** The weight of an orbit continuum is its **Euler characteristic**, an index. Haar measure computes its **volume**, normalized to 1. These are different invariants of B; they coincide only for a point. Note in particular that the failure is not a normalization slip that a constant could absorb: the true weight can be `0` (so no rescaling of μ produces it) and can have the **wrong sign** (`Σ_g`, `g ≥ 2`).

**Where the divergence between the two invariants comes from.** χ(B) is the index of the leafwise de Rham complex on B; μ(B) is the mass of a leafwise measure. In (TF), leafwise data enters only through `e(F)` (the leafwise Euler density, giving `χ_Co`) and through the signs `ε` — both index-theoretic; transverse data enters through the transverse measure (giving the factor `ℓ(γ)` and the `μ_⊥` in `χ_Co`). Haar measure on B is leafwise; it has no slot.

### 4.3 Case B: B a Cantor group (`dim F = 0`) — the trace diverges

This is DQ-M's literal trivial model. Here `dim B = 0`, so `dim F = 0`, the leaves are **points**, `Λ^•F` is the trivial line bundle concentrated in degree 0, `d_F = 0`, and
```
        H̄^0(F) = C(Y) = C(B × S¹_ℓ),        H̄^n(F) = 0 for n > 0.
```
Take Haar `μ` on B and `|ds|/`(nothing) on the circle; on `L²(Y, μ ⊗ ds)` we have `L²(Y) = L²(B,μ) ⊗ L²(S¹_ℓ)` and `φ^{t*} = 1 ⊗ T_t` with `T_t` translation.

> **Proposition 4.3.** `A_f = 1_{L²(B,μ)} ⊗ C_f` with `C_f` the convolution operator on `L²(S¹_ℓ)` of smooth kernel `K(s,s') = Σ_k f(s'−s+kℓ)`, `tr C_f = ℓ Σ_k f(kℓ)`. Since `B` is an infinite compact group, `dim L²(B,μ) = ℵ_0`, hence `A_f` is **not** of trace class and
> ```
>      Tr(φ* | H̄^0(F))  =  "∞" · ℓ Σ_{k∈Z} δ_{kℓ}
> ```
> diverges. Equivalently, the generator `Θ` has spectrum `{2πin/ℓ : n ∈ Z}` with **infinite** multiplicity at each point, so the sum `Σ_{λ ∈ Sp_0(Θ)} e^{tλ}` of [Den05] p. 35 has no meaning. **The distributional trace does not exist.**

*Proof.* `L²(B,μ)` is infinite-dimensional: `B` is an infinite profinite group, so it has open subgroups of unbounded index (Lemma 9.2, step (b)), hence for every `n` a partition into `n` clopen sets of positive Haar measure, whose indicator functions are linearly independent in `L²(B,μ)`. Therefore `1 ⊗ C_f` carries each eigenvalue of `C_f` with multiplicity `dim L²(B,μ) = ∞`, and `C_f ≠ 0` for suitable `f`. ∎

**Consistency with §4.2.** Proposition 4.3 is Theorem 4.1 with `χ(B)` replaced by *"the number of points of B"* — which is what the Euler characteristic of a 0-dimensional space is, and which is `∞`. Same law, same failure mode: the trace **counts** the continuum; Haar **weighs** it.

### 4.4 The measured trace in the trivial model, and why its success is an artifact

If instead of (T-coh) one uses (T-meas) — integrate the Schwartz kernel over the diagonal against the measure `Λ = μ ⊗ ds` on Y — then in Case B
```
     Tr_Λ(A_f) = ∫_Y K_{A_f}(y,y) dΛ(y) = μ(B) · ∫_0^ℓ Σ_k f(kℓ) ds = ℓ Σ_{k∈Z} f(kℓ) ,
```
which **is** exactly the Haar-averaged answer: one orbit's worth. So DQ-M's claim is *true for the measured trace in the `dim F = 0` model*. Three reasons this does not rescue Road 2.

1. **It is a `dim F = 0` artifact.** For `dim F > 0` — the only relevant case, Deninger needs `dim F = 2` — the operator `A_f` is *not* an element of the foliation von Neumann algebra: `φ^{t*}` maps sections over the leaf `L_s` to sections over `L_{s−t}`, so it is not a leafwise operator and `Tr_Λ` is not defined on it. In Case B the ambiguity exists only because the leaves are points, so "leafwise" and "transverse" coincide. Repeating §4.4 in Case A is impossible.
2. **Even the laminated measured framework counts orbits.** [Lei06] p. 17 builds his Hilbert spaces from the Ruelle–Sullivan current of a transverse measure and *still* assumes the closed orbits are non-degenerate, and his orbital side is a discrete sum with integer coefficients.
3. **It changes the spectral side out of recognition.** (T-coh) delivers the point spectrum of Θ **with multiplicities** — the object Deninger's program must match with the zeros of ζ. (T-meas) delivers Λ-dimensions (real numbers). Nothing on disk supplies an arithmetic interpretation of the latter, and Road 2 was explicitly a repair *inside* the existing framework ("the packet's aggregate orbit contribution is `∫_{B_p}(single-orbit term) dHaar` = the single-orbit term", 9.4 §7), not a proposal to replace the framework.

**Summary of program item (1).** In the trivial model the distributional (cohomological) trace **exists** when `dim F > 0` and **diverges** when `dim F = 0`; in neither case is the orbital side the Haar average. The correct weight is `χ(B)`.

---

## §5. Where an orbit continuum can live: the category theorem

DQ-M speaks of "the transverse measure on the continuum". This section proves that in the specified model world there is no such thing.

**The §7.7 construction, as read on [Den05] pp. 34–35.** Let `f : M → M` be an unramified covering of a compact connected orientable `d`-manifold, `M̄ = lim(… → M → M → …)` the inverse limit with the shift `f̄`, `M̃` the universal cover, `Γ̄ = lim Γ/Γ_i` the profinite set, so that `M̃ ×_Γ Γ̄ ≅ M̄` (display (36), p. 34). Fix `l > 0`, `Λ = lZ`, `(m,t)·λ = (f̄^{−λ/l}(m), t+λ)`, and
```
        X = M̄ ×_Λ R ,        φ^t[m,t'] = [m, t+t'] ,
```
an `a = d+1`-dimensional smooth solenoid with a one-codimensional foliation F whose leaves are *"the images in X of the manifolds `M̃ × {γ} × {t}`"*, and φ is *"everywhere transverse to the leaves of F and in particular has no fixed points"* (p. 35, verbatim).

> **Theorem E (category theorem).** In any [Den05] §7.7 suspension `X = M̄ ×_Λ R`:
> **(E1)** the set of closed orbits of φ is in canonical bijection with the set of finite `f`-orbits on the **base manifold** `M`, an orbit of `n` points having length `n·l`;
> **(E2)** consequently every family of closed orbits — in particular every continuum `B` of closed orbits of common length ℓ — is canonically a compact `f`-invariant subset of the manifold `M`, i.e. a **leafwise** object; the profinite direction `Γ̄` carries **no** closed orbits at all;
> **(E3)** a measure on `B` is therefore a leafwise measure, never a transverse measure of `F`; the invariant transverse measure of `F` in the §7.7 model is one-dimensional (the flow direction) and is entirely consumed by the factor `ℓ(γ)` in the orbital term.

*Proof.* (E1) is [Den05] p. 35 verbatim: *"The map `γ ↦ γ_M = γ ∩ (M̄ ×_Λ Λ)` gives a bijection between the closed orbits γ of the flow on X and the finite orbits `γ_M` of the `f̄`- or Λ-action. These in turn are in bijection with the finite orbits of the original `f`-action on M. We have: `l(γ) = |γ_M| l`."* (E2) is immediate from (E1): the parameter space of closed orbits is a subset of `M`, and `M` is a `d`-manifold that the leaves `M̃` cover. Nothing in the bijection refers to `Γ̄`; in particular a family of closed orbits is never spread along the profinite factor. (E3) restates (E2) together with [ALKL] p. 100, *"there is a canonical isomorphism `Nφ ≅ TF` on `M¹`"*: the directions transverse to a closed orbit are exactly the leaf directions, and along them the trace formula's data are the leafwise Euler density and the signs `ε` — not a transverse measure. ∎

**Two consequences worth stating separately.**

* **(E-a) The escape "put the packet in the Cantor direction" is closed in the model world.** One might hope to model a packet `Γ_p ≅ B_p × S¹` by spreading the orbits along the solenoid's own profinite factor `Γ̄`, where a Haar measure *is* transverse. (E2) forbids it: `Γ̄` contributes no closed orbits. The profinite direction of a §7.7 solenoid is a direction of **leaves**, not of orbits. This is the one place where the verbatim bijection of [Den05] p. 35 is doing heavy work, so the verification pass proved it from the construction rather than quoting it:

> **Lemma 5.1 (no spreading in the profinite direction).** In the §7.7 construction, write points of `M̄ = lim(… →^f M →^f M → …)` as sequences `(m_i)_{i∈Z}` with `m_i = f(m_{i+1})`, and let `f̄` be the shift. Then for every `k ∈ Z^×` the projection to the `0`-th coordinate,
> ```
>        pr_0 :  Fix(f̄^k)  ⟶  Fix(f^k) ⊆ M ,
> ```
> is a **homeomorphism**. Consequently the set of closed orbits of `φ` of period `kℓ` is canonically homeomorphic to a compact subset of the base manifold `M`, and meets each fiber of `M̄ → M` in **at most one point**: an orbit family can never be spread along `Γ̄`.
>
> *Proof.* `f̄((m_i)) = (f(m_i))_i = (m_{i−1})_i`, so `f̄^k((m_i)) = (m_{i−k})_i`. Fixedness means `m_i = m_{i−k}` for all `i`, i.e. the sequence is `k`-periodic; combined with `m_i = f(m_{i+1})` this forces `m_0 = f^k(m_0)`, and conversely every `m ∈ Fix(f^k)` extends uniquely to such a `k`-periodic compatible sequence (`m_{−j} = f^j(m)` for `0 ≤ j < k`, then repeat). So `pr_0` is a bijection onto `Fix(f^k)`; it is continuous (a coordinate projection of the product topology) between compact Hausdorff spaces, hence a homeomorphism. For `k = 1` the fixed sequences are the constant ones, so `Fix(f̄) ≅ Fix(f)`. ∎
>
> The Cantor direction is thus invisible to the periodic set: it is a direction along which the *leaves* of `F` are stacked (`M̄ ≅ M̃ ×_Γ Γ̄`, [Den05] p. 34 display (36), leaves `= ` images of `M̃ × {γ} × {t}`), and the periodic set is a single "constant-sequence" cross-section of it.
* **(E-b) The dimension constraint.** In the arithmetically relevant case `dim F = 2`, `M` is a closed surface. A closed surface admits a self-covering of degree `> 1` **only if** `χ(M) = 0`, i.e. `M = T²` in the orientable case. Hence a §7.7 suspension with `dim F = 2` is either (i) `f` a diffeomorphism — then `Γ̄` is a point, `M̄ = M`, and `X` is the **mapping torus** of `f`, a closed 3-manifold (this is exactly Hector's case (c) in [ALKL] p. 101, *"F is given by a fiber bundle `M → S¹` with connected fibers"*); or (ii) `M = T²`, `χ(M) = 0`, and then `χ_Co(F,μ) = χ(M)·l = 0` by [Den05] p. 35.
  Case (i) is where the exact computations of §6–§7 live; case (ii) is treated in §10.

---

## §6. Program item (2), part one: the exact trace for mapping-torus systems

Case (i) of (E-b) is not a toy: it is a [Den05] §7.7 suspension, it is a closed manifold, it satisfies every hypothesis of [ALKL] except H4, and it is the setting in which H4 can be violated by a continuum **while everything else stays classical**. We compute the left-hand side of (TF) exactly, with no non-degeneracy assumption.

**Setup 6.0.** Let `Σ` be a closed connected orientable `d`-manifold, `h ∈ Diff(Σ)`, `ℓ > 0`, `Λ = ℓZ`, and
```
        Y = Σ ×_Λ R = (Σ × R)/∼,      (m,t) ∼ (h^{-1}m, t+ℓ);        φ^u[m,t] = [m,t+u].
```
`Y` is a closed `(d+1)`-manifold fibering over `S¹_ℓ` with fiber `Σ`; `F` = the fibration by the fibers `L_t = π(Σ × {t})`; `dim F = d`, `codim F = 1`; `φ` is transverse to `F` and has no fixed point and no preserved leaf. `F` is Riemannian (a fibration). This is [Den05] §7.7 with `M = Σ`, `f = h` (an unramified covering of degree 1), `M̄ = Σ`, `Γ̄ = pt`; and it is Hector case (c) of [ALKL] p. 101.

**Lemma 6.1 (the return map).** `φ^ℓ[m,t] = [m, t+ℓ] = [hm, t]`, so `φ^ℓ` preserves each leaf `L_t` and, under the identification `L_t ≅ Σ`, `m ↦ [m,t]`, it **is** `h`. Consequently, for `k ∈ Z^×`, the closed orbits of `φ` of period `kℓ` correspond bijectively to `Fix(h^k)`, an orbit of least period `nℓ` corresponding to a periodic `h`-orbit of `n` points. (This is [Den05] p. 35's bijection made explicit.) ∎

**Lemma 6.2 (leafwise forms and the monodromy).** Under `L_t ≅ Σ`, a leafwise `n`-form on `Y` is a smooth family `(α_t)_{t∈R}`, `α_t ∈ Ω^n(Σ)`, with `α_{t+ℓ} = h^* α_t`; `d_F = d_Σ`; and `(φ^{u*}α)_t = α_{t+u}`.
*Proof.* The point `[m,t+ℓ]` equals `[hm,t]`, so the two identifications of the same leaf at parameters `t` and `t+ℓ` differ by `h`; pulling back a form on `Y` gives `α_{t+ℓ} = h^*α_t`. `φ^u` maps `L_t` to `L_{t+u}` and is the identity of `Σ` in these coordinates. ∎

**Lemma 6.3 (leafwise Hodge).** Let `g` be any Riemannian metric on `Y` and `g_t` the induced metric on `L_t ≅ Σ`; then `g_{t+ℓ} = h^*g_t`. By [ALKL] (1.2.2)–(1.2.3) (p. 2), which apply because `F` is Riemannian on a closed manifold, `H̄^n(F) ≅ ker ∆_F`, and
```
        ker ∆^n_F  =  { (α_t) : α_t is g_t-harmonic, α_{t+ℓ} = h^*α_t } .
```
Identifying `g_t`-harmonic `n`-forms with `H^n(Σ;C)` (Hodge), this is
```
        H̄^n(F)  ≅  { u : R → V_n := H^n(Σ;C)  smooth,  u(t+ℓ) = A_n u(t) },        A_n := h^* on H^n(Σ;C),
```
with `φ^{s*}u(t) = u(t+s)`. In particular `H̄^n(F)` is Hausdorff and is the space of smooth sections of the flat bundle over `S¹_ℓ` with monodromy `A_n`.
*Proof.* `h^*` carries `g_t`-harmonic forms to `h^*g_t = g_{t+ℓ}`-harmonic forms, so the equivariance is consistent; the rest is Lemma 6.2 plus [ALKL] (1.2.3). ∎

> **Theorem A (exact trace, no non-degeneracy assumed).** In Setup 6.0, for every `f ∈ C_c^∞(R)` the operator `A_f = ∫_R f(s)φ^{s*}ds` is trace class on `H̄^n(F)` and
> ```
>       Tr( φ* | H̄^n(F) )  =  ℓ · Σ_{k ∈ Z}  tr( (h^*)^k | H^n(Σ;C) ) · δ_{kℓ} ,
> ```
> a well-defined distribution on R. Hence
> ```
>   (★)   Σ_{n=0}^{dim F} (−1)^n Tr( φ* | H̄^n(F) )  =  ℓ · Σ_{k ∈ Z}  L(h^k) · δ_{kℓ} ,
>         L(g) := Σ_n (−1)^n tr( g^* | H^n(Σ;C) )   (the Lefschetz number).
> ```
> Moreover the `k = 0` term is `ℓ·χ(Σ)·δ_0 = χ_Co(F,μ)·δ_0` exactly, by [Den05] p. 35 (`χ_Co(F,μ) = χ(M)·l`); so **the orbital side of (TF) is forced to be**
> ```
>   (★★)  Σ_{k ∈ Z^×}  ℓ · L(h^k) · δ_{kℓ} .
> ```

*Proof.* Choose `Ξ_n ∈ End(V_n)` with `e^{ℓΞ_n} = A_n` (possible: `A_n` is invertible; take a branch of `log`). The map `u ↦ v`, `v(t) := e^{−tΞ_n}u(t)`, is a topological isomorphism from `H̄^n(F)` of Lemma 6.3 onto `C^∞(S¹_ℓ) ⊗ V_n`, since `v(t+ℓ) = e^{−tΞ}e^{−ℓΞ}A_n u(t) = v(t)`. Under it,
```
        (φ^{s*}v)(t) = e^{−tΞ}u(t+s) = e^{sΞ} v(t+s),        i.e.   φ^{s*} = e^{sΞ_n} ∘ (translation by s).
```
Hence `A_f` has the smooth `End(V_n)`-valued kernel on `S¹_ℓ × S¹_ℓ`
```
        K(t,t') = Σ_{k ∈ Z} f(t' − t + kℓ) · e^{(t'−t+kℓ)Ξ_n} ,
```
(the sum is finite for each `(t,t')` because `f` has compact support). A smooth kernel on a closed manifold with finite-rank coefficients defines a trace-class operator whose trace is the integral of the pointwise trace over the diagonal:
```
        tr A_f = ∫_0^ℓ tr K(t,t) dt = ∫_0^ℓ Σ_k f(kℓ) tr(e^{kℓΞ_n}) dt = ℓ Σ_k f(kℓ) tr(A_n^k).
```
This is the assertion, and it is manifestly a distribution (`|tr A_n^k| ≤ C ρ^{|k|}` and the `δ_{kℓ}` are locally finite). Summing over `n` with signs gives (★); at `k = 0`, `tr(A_n^0) = dim H^n(Σ;C)` and `Σ_n(−1)^n dim H^n = χ(Σ)`. ∎

**Consistency check (the classical case).** If `h` has only simple fixed points then `Σ_{p ∈ Fix(h^k)} sign det(id − (h^k)_{*p}) = L(h^k)` (Lefschetz–Hopf), and the coefficient of `δ_{t_0}` in the orbital side of (TF) is `Σ_{γ : ℓ(γ) | t_0} ℓ(γ) ε_γ(t_0/ℓ(γ))`; grouping the points of `Fix(h^k)` into `h`-orbits and using `ℓ(γ) = |γ_M|ℓ` ([Den05] p. 35) turns this into `ℓ Σ_{p∈Fix(h^k)} ε_p = ℓ L(h^k)`, which is exactly (★★). **So Theorem A reproduces [Den05] Theorem 7.8 / [ALKL] Theorem 1.3.10 verbatim whenever H4 holds, and extends the left-hand side to the case where H4 fails.** That agreement — on both the `δ_0` term and every `δ_{kℓ}` — is the internal check that the computation is correctly normalized.

**Remark 6.4 (a bookkeeping discrepancy in the sources, not load-bearing).** [Den05] Theorem 7.8 (p. 35) writes the negative-time orbital terms with an extra factor `det(−T_xφ^{kl(γ)}|T_xF)`, whereas [Den05] Theorem 5.3 (p. 22) and [ALKL] Theorems 1.3.8/1.3.10 (pp. 6, 8) write `ε_γ(k)` symmetrically for all `k ∈ Z^×`, and [Lei06] p. 3 remarks explicitly *"Notice that here there is no dissymmetry for the coefficients of α(−kl(γ)) and α(kl(γ))"*. Theorem A agrees with the symmetric version: the two coincide whenever `|det(T_xφ^{ℓ}|T_xF)| = 1` (e.g. every example in this note), and differ otherwise. Nothing below uses negative `k`; the verdict is drawn from `k ≥ 1`. Flagged, not adjudicated.

---

## §7. The counterexamples — Theorem B (the NO)

Every model below is a [Den05] §7.7 suspension with `dim F = 2` (`d = 2`, `dim Y = 3` — the arithmetically targeted dimensions), no fixed points, no preserved leaves, and a **continuum of closed orbits of common length ℓ**. Theorem A evaluates the left-hand side of (TF) exactly in each. In each, the Haar-averaged orbital side of DQ-M is compared with the true one.

Recall the DQ-M prediction: the continuum contributes `1 × (single-orbit contribution) = ℓ Σ_{k∈Z^×} ε δ_{kℓ}` with `|ε| = 1`.

### 7.1 `Y = S² × S¹_ℓ` — weight `+2`

`Σ = S²`, `h = id`. Every point is periodic of least period ℓ; `B = S²`. `h^* = id`, so `L(h^k) = χ(S²) = 2`. By Theorem A,
```
        Σ_n (−1)^n Tr(φ*|H̄^n(F)) = 2ℓ Σ_{k∈Z} δ_{kℓ} ,       χ_Co(F,μ) = 2ℓ ,
        orbital side = 2ℓ Σ_{k ∈ Z^×} δ_{kℓ}          vs.       DQ-M's ±ℓ Σ_{k∈Z^×} δ_{kℓ}.
```
Off by a factor 2. (Not a normalization: see 7.2, 7.3.)

### 7.2 `Y = T² × S¹_ℓ` — weight `0`, with `B` a compact group carrying Haar measure

`Σ = T²`, `h = id`. `B = T²`, a compact connected abelian **group**, with its Haar probability measure — the closest a manifold model comes to DQ-M's hypothesis "B a compact group with Haar probability μ". `L(h^k) = χ(T²) = 0`. By Theorem A,
```
        Σ_n (−1)^n Tr(φ*|H̄^n(F)) = 0 ,       χ_Co(F,μ) = 0 ,
        orbital side = 0             vs.       DQ-M's ±ℓ Σ_{k∈Z^×} δ_{kℓ} ≠ 0.
```
**The true weight of a Haar-measured continuum of closed orbits here is exactly zero.** No rescaling of the measure repairs this.

### 7.3 `Y = Σ_g × S¹_ℓ` — weight `2 − 2g`, the wrong sign

`Σ = Σ_g`, `g ≥ 2`, `h = id`. Weight `χ(Σ_g) = 2 − 2g < 0`, against DQ-M's `+1`. So the discrepancy is not a positive factor: the orbital contribution of a continuum can be negative while a single orbit's is positive.

### 7.4 A Cantor continuum: `B ≅` Cantor set inside `S²` — weight `+2`

This realizes DQ-M's hypothesis on the *topology* of B (every infinite metrizable profinite group is a compact metrizable totally disconnected perfect space, hence homeomorphic to the Cantor set; so any Cantor group `B` can be identified homeomorphically with the `K` below, and its Haar measure transported).

> **Construction 7.4.1.** Let `W` be the smooth "north–south" vector field on `S²` (the gradient of the height function for the round metric), whose zero set is `{N,S}` and whose non-stationary orbits are the open meridians, each running monotonically from `S` to `N`. Let `K ⊂ S²` be a Cantor set with `N, S ∈ K`, and let `ρ ∈ C^∞(S², [0,∞))` with `ρ^{-1}(0) = K` (Whitney: any closed subset of a manifold is the zero set of a non-negative smooth function). Put `V := ρ·W`, a smooth vector field with `Z(V) = K`, and let `h := ` its time-1 flow.

> **Lemma 7.4.2.** `h` is a diffeomorphism of `S²`, isotopic to the identity, and `Fix(h^k) = K` for every `k ∈ Z^×`.
> *Proof.* `V` is smooth on a closed manifold, hence complete, and its time-1 map is a diffeomorphism, isotopic to `id` through the flow. `Fix(h^k) ⊇ Z(V) = K` trivially. Conversely let `p ∉ K`. Then `V(p) ≠ 0`, and the `V`-orbit of `p` is contained in the `W`-orbit of `p`, i.e. in an open meridian, along which `W` (hence `V`) points strictly from `S` toward `N`. The height function `H` is therefore strictly increasing along the `V`-orbit of `p`, so `H(h^k p) ≠ H(p)` for `k ≠ 0`, whence `h^k p ≠ p`. ∎

Now let `Σ = S²`, `Y = Σ ×_Λ R` the mapping torus of `h` (Setup 6.0). Then:
* the periodic set of `φ` is `K × S¹_ℓ` — **a Cantor continuum `B ≅ K` of closed orbits, all of common length ℓ**;
* the ambient flow is **aperiodic off the continuum**: by Lemma 7.4.2 there are no other closed orbits of any period;
* every orbit in the continuum is maximally degenerate. At `p ∈ K` the linearization of `V = ρW` is `∇V_p = ρ(p)·∇W_p + W_p ⊗ dρ_p = 0`, because `ρ(p) = 0` and because `ρ ≥ 0` attains its minimum at `p`, so `dρ_p = 0`. Hence `d(h^k)_p = exp(k·∇V_p) = id` for every `p ∈ K` and every `k ∈ Z`, so `det(id − φ^{kℓ}_*|T_pF) = det(id − id) = 0` and `ε_c(k)` is **undefined at every orbit of the continuum** — exactly as diagnosed in §2.3;
* `h ≃ id`, so `L(h^k) = χ(S²) = 2`, and Theorem A gives
```
        orbital side  =  2ℓ Σ_{k∈Z^×} δ_{kℓ}        vs.      DQ-M's  ±ℓ Σ_{k∈Z^×} δ_{kℓ}.
```

### 7.5 A Cantor-free normally hyperbolic continuum: `B ≅ S¹` in `T²` — weight `0`

Let `ψ` be an orientation-preserving diffeomorphism of `S¹` with `Fix(ψ) = {0, 1/2}`, `ψ'(0) = 1/2`, `ψ'(1/2) = 2` (take the time-1 map of a vector field vanishing simply at `0, 1/2`). Let `h(x,y) = (ψ(x), y)` on `Σ = T²`; `h` is a diffeomorphism isotopic to `id`. Because `ψ` moves monotonically on each complementary arc, `Fix(ψ^k) = Fix(ψ)` for all `k ≠ 0`, so
```
        Fix(h^k) = {0, 1/2} × S¹ ,
```
two disjoint circles of fixed points; the periodic set of the suspension flow is two continua `B_± ≅ S¹`, each a compact group with Haar measure, of closed orbits of common length ℓ, and each **normally hyperbolic** (`dψ = 1/2` resp. `2` in the normal direction). `L(h^k) = χ(T²) = 0`, so by Theorem A the total orbital side is `0`, whereas DQ-M predicts `2·(±ℓ)Σ_kδ_{kℓ} ≠ 0`. (Individually each circle contributes `0`; see §8.)

This model is worth isolating because it removes every possible objection that the failure is caused by total degeneracy: here the flow is normally hyperbolic transverse to the continuum, `det(id − dφ^{kℓ})` vanishes **only** along the continuum's own tangent direction, and the answer is still `0`, not `±1`.

> **THEOREM B (the NO).** There exist [Den05] §7.7 suspensions `Y = M̄ ×_Λ R` with `dim F = 2`, no fixed points, no preserved leaves, whose periodic set is a continuum `B × S¹` of closed orbits of common length ℓ with `B` respectively (a) a closed surface, (b) a compact connected group with its Haar probability measure, (c) a Cantor set (hence homeomorphic to any Cantor group, with Haar transported), such that the distributional trace of the flow on leafwise forms **exists** and the orbital side of the dynamical Lefschetz trace formula is
> ```
>        ℓ · L(h^k) · δ_{kℓ}   with  L(h^k) ∈ {2, 0, 2−2g} ,     never  ℓ · 1 · δ_{kℓ} .
> ```
> Hence **the answer to DQ-M is NO**: the orbital side is not `∫_B (single-orbit contribution) dμ`. ∎

**Sanity: is anything wrong with these models as models?** They satisfy every structural hypothesis a Deninger-type substrate must satisfy except H4: compact, three-dimensional, transversely oriented codimension-one foliation, foliated flow transverse to the leaves with no fixed points, `dim F = 2` even, and they are literally the objects of [Den05] §7.7 (an unramified covering `f = h` of degree 1). They are Hector case (c) of [ALKL] p. 101, which that memoir lists as one of the four cases its theory covers. The **only** hypothesis they violate is the one under test.

---

## §8. The correct law: the measured formula in *index* form

Theorem B refutes the Haar form. This section states what does hold, so that the negative result comes with the exact statement it replaces.

### 8.1 Global form (proved)

> **Theorem C1 (global measured formula, index form).** In Setup 6.0, for every `k ∈ Z^×` the total contribution of the periodic set of period `kℓ` to the orbital side of (TF) is
> ```
>        ℓ · L(h^k) · δ_{kℓ} ,
> ```
> where `L(h^k)` is the Lefschetz number of the leafwise return map `h^k`. When `Fix(h^k)` is finite and simple this is the classical `ℓ Σ_{p} ε_p δ_{kℓ}`; when `Fix(h^k)` is a continuum `B`, `L(h^k)` is the **total fixed-point index of `h^k` on `B`**, an integer.

*Proof.* The first assertion is (★★) of Theorem A. The identification of `L(h^k)` with the total fixed-point index when `Fix(h^k)` is compact is the Lefschetz–Hopf theorem. ∎ *(The Lefschetz–Hopf identification is classical and is **flagged** — see §13; nothing in Theorem B or in the verdict uses it, since Theorem A computes `L(h^k)` directly from cohomology.)*

**Special case, computed independently in §4.2:** if `h = id_B` then `L(h^k) = χ(B)` and the weight of the whole continuum is its Euler characteristic.

### 8.2 Clopen-local form (proposition grade)

For a Cantor continuum one wants the contribution of a *piece*. Recall the classical fixed-point index: if `g` is a continuous self-map of a manifold `L` and `C ⊆ Fix(g)` is compact **and open in `Fix(g)`**, then `ind(g, C) ∈ Z` is defined (as the degree of `id − g` on any isolating neighborhood of `C`), and it is (i) additive over disjoint such `C`, (ii) invariant under homotopies through maps whose fixed points stay in the isolating neighborhood, (iii) equal to `ε_p` at a simple fixed point, (iv) summing to `L(g)` over a clopen partition of `Fix(g)` (Lefschetz–Hopf).

> **Proposition C2 [proposition grade].** Let `B = Fix(h^k)` be the orbit continuum, and let `U ⊆ B` be **clopen in `B`**. Then the contribution of the sub-family of closed orbits parametrized by `U` to the coefficient of `δ_{kℓ}` in the orbital side of (TF) is
> ```
>        ℓ · ind(h^k, U) ∈ ℓ·Z ,
> ```
> and `U ↦ ι_k(U) := ind(h^k, U)` is a **Z-valued finitely additive measure on the clopen algebra of `B`**, with total mass `ι_k(B) = L(h^k)`.

*Justification and its grade.* Finite additivity and the total mass are properties (i) and (iv) of the index. The identification of the *local* contribution with `ind(h^k,U)` is the statement that [ALKL]'s localization survives the removal of H4 in the following exact sense: the proof of Proposition 7.3.2(ii) (pp. 155–156) is a **local** computation — it isolates a neighborhood `V_j` of each orbit and evaluates `lim_{u↓0}∫_{V_j}str(…)` by Proposition 2.9.6 (p. 71), which is a purely local heat-kernel Lefschetz computation. Replacing the isolating neighborhood of a *simple* fixed point by an isolating neighborhood of a *clopen compact* piece `U` of `Fix(h^k)` replaces `ε_p` by `ind(h^k,U)` — the standard Atiyah–Bott local index. **This step was not re-derived here**; it is flagged in §13. What *was* proved without it is the global statement C1, and Theorem B (the verdict) uses only C1.

### 8.3 The exact criterion

> **Corollary C3.** In the model world, the aggregate contribution of an orbit continuum `B` of common length ℓ equals the contribution of a **single simple orbit** with `ε = +1` if and only if
> ```
>          ind(h^k, B) = 1   for every k ∈ Z^× .
> ```
> Haar measure enters nowhere. In particular:
> * `B` a point (the classical case): `ind = 1` ✓.
> * `B` contractible: `ind = χ(B) = 1` ✓ — **an orbit continuum can weigh exactly one orbit**, but only for topological reasons. This case is realized by an explicit [Den05] §7.7 model, **Construction 12.1** (`Σ = S²`, `B = ` a closed disk of fixed points, one further simple orbit with `ε = +1`, `ind(h^k,B) = +1` for every `k`).
> * `B` a nontrivial compact connected Lie group: `ind = χ(B) = 0` ✗ (Lemma 9.1).
> * `B` an infinite profinite group with translation symmetry: `ind = 0` ✗ (Theorem D).

Corollary C3 is the honest replacement statement: **the measured formula for orbit continua is true, with the fixed-point-index measure `ι` in place of the transverse measure; and `ι` is Z-valued, so it is never a probability measure on an infinite `B`.** Indeed:

> **Lemma C4.** If `B` is an infinite profinite group and `ι = c·μ` for `μ` the Haar probability measure and some `c ∈ R`, then `c = 0`.
> *Proof.* For every open subgroup `H ≤ B` of index `n`, `H` is clopen and `μ(H) = 1/n`, so `ι(H) = c/n` must lie in `Z`. By Lemma 9.2, step (b), the index `n` is unbounded over the open subgroups of an infinite profinite group, forcing `c = 0`. ∎

---

## §9. Theorem D: the equivariance no-go — canonicity kills the weight

Road 2 of `probe-9.4-note.md` §7 recommends Haar measure on `B_p` for one reason, quoted: *"the packet base `B_p` is a compact group, its Haar probability measure is translation-invariant, and by Lemma D(iii) Aut(C) acts on `B_p` by group translations — so **Haar measure is canonical AND Aut(C)-equivariant: it passes exactly the naturality test that every selection fails**."* This section shows that this very property annihilates the weight.

### 9.1 The connected case

> **Lemma 9.1.** Let `G` be a compact connected Lie group of positive dimension. Then `χ(G) = 0`.
> *Proof.* Pick `0 ≠ ξ ∈ Lie(G)`; the left-invariant vector field it generates is nowhere zero on `G`. By Poincaré–Hopf, `χ(G) = 0`. ∎

Combined with §4.2 (`B = G`, `h = id`): a positive-dimensional compact connected group of closed orbits contributes **weight 0**. §7.2 (`G = T²`) and §7.5 (`G = S¹`) are instances, both computed independently by Theorem A.

### 9.2 The profinite case

> **Lemma 9.2 [novelty: single-check; elementary, possibly folklore].** Let `B` be an **infinite** profinite group and let `ι` be a finitely additive `Z`-valued set function on the algebra `Clop(B)` of clopen subsets of `B`, invariant under left translation (`ι(bU) = ι(U)` for all `b ∈ B`, `U ∈ Clop(B)`). Then `ι ≡ 0`.

*Proof.* (a) *Clopen sets are finite unions of cosets of open subgroups.* Let `U ∈ Clop(B)`. For each `u ∈ U`, openness gives an open normal subgroup `H_u ⊴ B` with `uH_u ⊆ U`. By compactness of `U`, finitely many `u_1H_{u_1}, …, u_rH_{u_r}` cover `U`; put `H := H_{u_1} ∩ … ∩ H_{u_r}`, an open normal subgroup. Then `U` is a union of `H`-cosets, and it is a **finite** union since `[B:H] < ∞`.

(b) *The indices of the open normal subgroups are unbounded.* **[Corrected in the verification pass — the first draft's argument enumerated the open normal subgroups of `B`, which presumes countably many; that is false in general, e.g. `B = (Z/2)^I` for uncountable `I` has `|I|`-many open subgroups. The following argument uses no enumeration.]** Suppose for contradiction that `[B:N] ≤ M` for every open normal `N ⊴ B`. The set `{[B:N] : N ⊴ B open}` is then a nonempty set of positive integers bounded by `M`, so it has a **maximum**; choose `N^*` open normal attaining it. Let `N ⊴ B` be any open normal subgroup. Then `N^* ∩ N` is open normal and contained in `N^*`, so `[B : N^*∩N] = [B:N^*]·[N^* : N^*∩N] ≥ [B:N^*]`; by maximality equality holds, so `[N^* : N^*∩N] = 1`, i.e. `N^* ⊆ N`. Since `B` is profinite, `⋂ {N : N ⊴ B open} = {1}`, so `N^* = {1}`. But `N^*` is open, so `{1}` is open, so `B` is discrete; being also compact, `B` is finite — contradicting the hypothesis that `B` is infinite. ∎(b)

(c) *Every coset of an open subgroup has index value 0.* Fix an open **normal** subgroup `N ⊴ B`, `n := [B:N] < ∞`. Translation invariance gives `ι(bN) = ι(N) =: m` for every `b ∈ B`, and finite additivity over the partition `B = ⊔_{i=1}^n b_iN` gives `ι(B) = n·m`. Hence `n | ι(B)` in `Z` **for every** open normal `N`. By (b) the integers `n` are unbounded, so the fixed integer `ι(B)` is divisible by arbitrarily large integers, whence `ι(B) = 0`, and then `m = ι(N) = ι(B)/n = 0` for every open normal `N`. Now let `H ≤ B` be any open subgroup. `H` has finite index, so it has finitely many conjugates and its normal core `N := ⋂_{b∈B} bHb^{-1}` is an open normal subgroup contained in `H`. Then `H` is the disjoint union of its `[H:N] < ∞` cosets of `N`, each of `ι`-value `0` by translation invariance, so `ι(H) = 0`, and `ι(bH) = 0` for every `b ∈ B`.

(d) By (a) and (c) and finite additivity, `ι(U) = 0` for every clopen `U` — `U` is a finite disjoint union of cosets of an open subgroup, each of value `0`. ∎

> **THEOREM D (equivariance no-go) [novelty: single-check].** Let `(Y, F, φ)` be a model-world system whose periodic set at length ℓ is a continuum `B × S¹` with `B` an **infinite profinite group**, and suppose there is a group `G` of homeomorphisms of `Y` commuting with `φ` and preserving `F`, acting on the parameter space `B` **by translations, transitively** (the exact hypothesis Road 2 invokes for `Aut(C)` acting on `B_p`). Then the index measure `ι_k` of Proposition C2 is translation-invariant, hence `ι_k ≡ 0` by Lemma 9.2. In particular the **total** weight is `ι_k(B) = 0`, and the packet's contribution to the orbital side of the trace formula **vanishes identically**:
> ```
>        aggregate contribution of the continuum  =  0 · ℓ · δ_{kℓ}  =  0 ,
> ```
> where the trace formula needs `ℓ δ_{kℓ}` (one orbit's worth).

*Proof.* A flow-commuting, foliation-preserving homeomorphism carries closed orbits to closed orbits of the same period and conjugates the leafwise return map `h^k` to itself; the fixed-point index is invariant under such conjugation, so `ι_k(gU) = ι_k(U)` for `g ∈ G`. `G` acts on `B` by translations, so `ι_k` is translation-invariant, and `ι_k` is Z-valued and finitely additive by Proposition C2. Lemma 9.2 applies. ∎

**Grade.** Lemma 9.1 and Lemma 9.2 are proved here in full. Theorem D inherits the grade of Proposition C2 (proposition grade — it needs the local index measure to exist). Theorem B, the verdict, does **not** depend on Theorem D.

**What Theorem D says in words.** Road 2's argument was: *selections are non-canonical, but Haar measure is canonical, therefore average.* Theorem D says: *the canonicity is real, and it is fatal.* An orbit continuum on which a symmetry group acts transitively by translations is exactly a continuum whose fixed-point index must be spread evenly over arbitrarily fine clopen partitions; an integer spread evenly over `n` parts for every `n` is `0`. The naturality test Haar passes is the same test that forces the answer to be `0` rather than `1`.

**The same statement for the connected case**, without index theory: a nontrivial compact connected group `B` has `χ(B) = 0` (Lemma 9.1), and by §4.2 the weight is `χ(B)`. So *both* kinds of compact group — connected and profinite — give weight `0`. The only compact group whose orbit continuum weighs `1` is the trivial group: a single closed orbit.

### 9.3 Calibration of Theorem D — what it is and what it is not (verification pass)

Theorem D is a **conditional structural theorem**, and honesty requires saying precisely how conditional, because two of its three ingredients have different grades and its hypothesis is not exhibited by any model in this note.

1. **The index-measure half is unconditional and classical.** The statement "let `g` be a self-map of a manifold, `B ⊆ Fix(g)` compact and open in `Fix(g)`; then `U ↦ ind(g,U)` is a `Z`-valued finitely additive set function on `Clop(B)`, invariant under any homeomorphism conjugating `g` to itself and carrying `B` to `B`" is classical fixed-point-index theory (additivity, commutativity/conjugation invariance). Combined with Lemma 9.2 — proved here in full — it gives, with no analysis at all:
   > **Theorem D(i) (index form, unconditional modulo classical index theory).** Let `g` be a self-map of a manifold whose fixed-point set contains a clopen-in-`Fix(g)` piece `B` that is an infinite profinite group, and suppose a group of homeomorphisms commuting with `g` acts on `B` transitively by translations. Then `ind(g, U) = 0` for every clopen `U ⊆ B`; in particular `ind(g, B) = 0`.
   (Transitivity by translations forces the acting translations to exhaust `B`: if `H ≤ B` acts transitively by left translation then `H = H·1 = B`.)
2. **The trace-formula half is Proposition C2, proposition grade.** Converting `ind(g,U) = 0` into "the continuum contributes `0` to the orbital side" needs the local index form (§8.2). When `B` is the **whole** periodic set at period `kℓ`, Proposition C2 is not needed: Theorem A gives the weight as `L(h^k)`, and Lefschetz–Hopf identifies `L(h^k) = ind(h^k, Fix(h^k)) = ind(h^k, B) = 0`. So Theorem D is unconditional (modulo classical index theory) in the case that matters most — a single homogeneous continuum carrying the whole periodic set — and proposition grade for proper clopen sub-families.
3. **The hypothesis is not exhibited here, and in the smooth closed-manifold sub-case it may be unrealizable.** No model in this note has an infinite profinite orbit continuum with a transitive translation symmetry. There is a structural reason to expect none among **closed manifolds** with **smooth** symmetries: by Bochner–Montgomery, a compact group acting effectively by diffeomorphisms on a manifold is a Lie group, and an infinite profinite group is not Lie (for merely continuous actions this is the Hilbert–Smith conjecture, open in general). `[RU — named, not re-derived, and not load-bearing: it is quoted only as a caution against reading Theorem D as an existence claim.]` The hypothesis **is** realizable outside the manifold category — a §7.7 solenoid `M̄ = M̃ ×_Γ Γ̄` with `Γ` abelian carries a genuine `Γ̄`-action by translations — and it is exactly the situation the arithmetic target presents (`Aut(C)` acting on `B_p` by translations, 9.4 Lemma D(iii), referee-pending). Theorem D is therefore stated and used as what it is: **a no-go for any framework in which a packet-symmetric continuum contributes at all**, not as a computation in an exhibited model.
4. **What *is* exhibited, unconditionally, is the connected case.** §7.2 (`B = T²`), §7.5 (`B ≅ S¹`) and §10.1 (`B ≅ S¹` in a genuine solenoid) are fully computed models in which `B` is a **compact group with its Haar probability measure**, `μ(B) = 1`, and the true weight is `0`. The verdict (Theorem B) rests on these and on §7.1/§7.3/§7.4, none of which uses Theorem D, Proposition C2, or any index theory.

---

## §10. Program item (2), part two: the genuine solenoid — a Cantor extension of an expanding map

The models of §7 are §7.7 suspensions but with `Γ̄` a point, so `X` is a manifold. This section runs the same test on a **genuinely solenoidal** model whose transversal has an infinite profinite (Cantor) factor — the structure of the arithmetic target — and whose base map is hyperbolic (expanding) in one direction. By (E-b) this forces `M = T²`.

### 10.1 Model S: `M = T²`, `f(x,y) = (2x, y)`

`f` is an unramified self-covering of `T²` of degree 2. Then
```
        Γ = Z² ,  Γ_i = 2^iZ × Z ,  Γ̄ = lim Z²/Γ_i = Z_2   (an infinite profinite group: a Cantor transversal),
        M̄ = lim(T² ←f— T² ← …) = Sol_2 × S¹   (Sol_2 = dyadic solenoid),
        X = M̄ ×_Λ R ,  Λ = ℓZ ,  dim X = 3 ,  dim F = 2 ,  leaves ≅ R² (dense in X).
```
By (E1), closed orbits ↔ finite `f`-orbits on `T²`: `Fix(f^k) = {x : 2^k x ≡ x} × S¹` = `(2^k − 1)` circles. In particular

> the periodic set of least period ℓ is **`B × S¹` with `B = {0} × S¹ ≅ S¹`, a compact connected group with Haar probability measure**, exactly DQ-M's shape; the flow is expanding in the `x`-direction (a Cantor extension of a hyperbolic map) and its generic orbit is non-closed.

Every orbit in `B × S¹` is degenerate: `df` has eigenvalue `1` along the `y`-direction.

### 10.2 The evaluation

`M̄ = Sol_2 × S¹` and `f̄ = (shift) × id`, hence
```
        X = X' × S¹ ,      X' := Sol_2 ×_Λ R ,      F = F' ⊞ T S¹ ,      φ = φ' × id ,
```
where `X'` is the §7.7 suspension of `(S¹, doubling)`, a 2-dimensional solenoid with `dim F' = 1`.

> **Lemma 10.1 (product decomposition) [flagged: proved below modulo the completed-tensor-product identification].** For `X = X' × N` with `N` a closed manifold and `F = F' ⊞ TN`, the leafwise de Rham complex satisfies
> ```
>        ( Ω^•_F(X), d_F )  ≅  ( Ω^•_{F'}(X'), d_{F'} )  ⊗̂  ( Ω^•(N), d_N ) ,
> ```
> and consequently `H̄^n(F) ≅ ⊕_{a+b=n} H̄^a(F') ⊗ H^b(N)` with `φ^{s*}` acting as `φ'^{s*} ⊗ id`.
>
> *Proof of the second statement from the first (this is the part that was left implicit in the first draft).* Fix a metric on `N` and let `Π` be the harmonic projection, `G` the Green operator, `κ := d_N^* G` — a **continuous** operator on `Ω^•(N)` with `Π = id − (d_N κ + κ d_N)`. Thus `(Ω^•(N), d_N) = (H^•(N), 0) ⊕ (A^•, d_N)` as topological complexes, where `A^• := (id − Π)Ω^•(N)` and `κ|_A` is a continuous contracting homotopy of `A^•`. Tensoring with `Ω^•_{F'}(X')` and completing, `id ⊗̂ κ` is a continuous contracting homotopy of `Ω^•_{F'}(X') ⊗̂ A^•` **in each total degree**, up to the sign convention of the tensor differential; hence that summand has *vanishing* (not merely vanishing-reduced) cohomology, and its `d`-image is closed. Therefore
> ```
>        H̄^n( Ω^•_{F'} ⊗̂ Ω^•(N) )  =  H̄^n( Ω^•_{F'} ⊗̂ H^•(N) )  =  ⊕_{a+b=n} H̄^a(F') ⊗ H^b(N) ,
> ```
> the last step because `H^b(N)` is finite-dimensional, so `⊗ H^b(N)` is exact and commutes with closures. Both `φ^{s*}` and `d` respect the splitting because `φ^s = φ'^s × id_N`. ∎
>
> *What remains flagged.* The first display — that the leafwise complex of a product lamination is the completed projective tensor product of the two complexes — is standard for nuclear Fréchet spaces (`Ω^•(N)` is nuclear Fréchet; the leafwise-smooth forms on a compact lamination are nuclear Fréchet), but the identification was **not written out here**, and Propositions 10.2–10.3 inherit that grade. The verdict (Theorem B) does not use Lemma 10.1.

> **Proposition 10.2.** In Model S, `Σ_n(−1)^n Tr(φ*|H̄^n(F)) = 0`, and `χ_Co(F,μ) = χ(T²)·ℓ = 0` ([Den05] p. 35). Hence the **orbital side vanishes identically**, and in particular the continuum `B ≅ S¹` of closed orbits of common length ℓ contributes `0`, against DQ-M's prediction `±ℓ Σ_{k∈Z^×}δ_{kℓ} ≠ 0`.

*Proof.* By Lemma 10.1 and multiplicativity of the alternating sum,
```
  Σ_n(−1)^n Tr(φ*|H̄^n(F)) = ( Σ_a(−1)^a Tr(φ'*|H̄^a(F')) ) · ( Σ_b(−1)^b dim H^b(S¹) ) = ( … ) · χ(S¹) = 0,
```
the first factor being a well-defined distribution by [Den05] Theorem 7.8 (p. 35), whose hypotheses hold for `X'`: `M = S¹` is a compact connected orientable 1-manifold, `f` = doubling is an unramified covering, and every periodic orbit is non-degenerate since `T_xφ^{kℓ}|T_xF' = 2^k ≠ 1`. ∎

**Remark.** All three of LHS, `χ_Co`, and the true orbital side vanish here; the information is that the *predicted* orbital side does not. The prediction's own sign is `ε = sign(1 − 2^k) = −1` in the transverse (`x`) direction, so DQ-M would give `−ℓ Σ_k δ_{kℓ}`.

### 10.3 Model S-Cantor: the same solenoid with a Cantor continuum

Perturb `f` inside its homotopy class so that the continuum becomes a Cantor set, keeping the covering property:
```
        f(x,y) = ( 2x , y + ψ(x,y) )  mod 1 ,        ∂_y(y + ψ) > 0 ,
```
so `f` is again an unramified covering of degree 2 of `T²` (fiberwise an orientation-preserving circle diffeomorphism over the doubling in `x`). Choose `ψ` with `ψ(0,·) : S¹ → (−1,1)` vanishing exactly on a Cantor set `K ⊂ S¹`. Then
```
        Fix(f) = {0} × K ,
```
so the periodic set of least period ℓ is `B × S¹` with **`B ≅ K` a Cantor set** inside a genuinely solenoidal `X` whose transversal contains `Γ̄ = Z_2`. This is the closest model on offer to the arithmetic target: 3-dimensional, `dim F = 2`, Cantor transversal, Cantor continuum of closed orbits of common length ℓ, hyperbolic ambient direction.

> **Proposition 10.3 [proposition grade].** The weight of `B` in Model S-Cantor is `L(f) = 1 − tr(A) + det(A) = 1 − 3 + 2 = 0`, where `A = diag(2,1)` is the matrix of `f_*` on `H_1(T²)` (`f` is homotopic to the linear map). Hence the Cantor continuum contributes `0`, not `±ℓΣ_kδ_{kℓ}`.
> *Grade:* this uses the **uniform §7.7 law** of §10.4, hence Proposition C2 and Lefschetz–Hopf; it is not an independent re-derivation. The rigorous counterexamples remain those of §7 and §10.2.

### 10.4 The uniform §7.7 law (recorded for the record)

Every computation in this note is an instance of one formula. For a [Den05] §7.7 suspension `X = M̄ ×_Λ R` of `f : M → M`,
```
   (§7.7-law)      Σ_n (−1)^n Tr(φ*|H̄^n(X,F))  "="  ℓ · Σ_{k ∈ Z} L(f^k) · δ_{kℓ} ,
```
with `L(f^0) = χ(M)`, so that the `k = 0` term is `χ(M)·ℓ·δ_0 = χ_Co(F,μ)·δ_0` — matching [Den05] p. 35 identically — and the `k ≠ 0` terms are `ℓ Σ_{p ∈ Fix(f^k)} ind_p = ℓ L(f^k)` by Lefschetz–Hopf, matching Theorem 7.8's orbital side identically whenever `f` is non-degenerate.

* **Proved here** (Theorem A) for `f` a diffeomorphism, i.e. `Γ̄ = pt`, `X` a mapping torus — with no non-degeneracy assumption.
* **Verified against [Den05] Theorem 7.8** in the non-degenerate solenoidal cases (`M = S¹`, `f` = doubling: `L(f^k) = 1 − 2^k`, `Fix(f^k)` = `2^k−1` points with `ε = −1`, product `ℓ(1−2^k)` ✓).
* **Not proved in general.** Flagged in §13. The verdict does not use it.

The law says in one line what this probe found: **the trace formula's orbital side is the Lefschetz number of the return map — a count with signs — and a continuum enters it through its index, never through its measure.**

---

## §11. Does the replacement "sum over orbits ↦ integral against a transverse measure" survive [ALKL]'s proof?

Collecting §3 and §8:

| step in [ALKL] | with H4 | with a continuum `B` |
|---|---|---|
| §4.1.1, p. 99: `C_I(φ)` finite, `P(φ)` discrete | the RHS is a locally finite sum | **fails**; repaired by replacing `Σ_{c}` with a sum over a **clopen decomposition** of `B` — a genuine "measured" reformulation, and the only part of DQ-M's proposal that survives |
| Prop. 7.3.2(ii), p. 155, list `{c_1,…,c_m}` + isolating `W_j` | finite, isolated | **fails**; repaired by isolating neighborhoods of clopen pieces of `B` |
| Prop. 2.9.6, p. 71: `lim_{u↓0}∫_{W_j} str(…) = ε_{y_j}` | the ±1 | **the ±1 does not exist** (`det(id − φ_*^{kℓ}|T_pF) = 0`); it is replaced by `ind(h^k, U) ∈ Z`, the local Lefschetz index of the clopen piece — **not** by `μ(U)` |
| the prefactor `ℓ(c)` (p. 156, the `∫_0^{ℓ(c_j)}|dx|`) | a transverse-measure factor | survives unchanged — it measures the orbit's own circle |
| Prop. 7.3.2(i) and (iii) | as stated | survive: they concern intervals containing no period, resp. `t = 0`; nothing there needs simplicity of the orbits, only that the closed orbits stay away from `I` |

> **Answer to program item (2).** The replacement of the sum over orbits by an integral over the continuum **does survive** [ALKL]'s proof — as an integral against the **fixed-point-index measure** `ι_k` on the clopen algebra of `B` (Proposition C2), whose total mass is the Lefschetz number of the return map. It does **not** survive as an integral against a transverse measure, and specifically not against Haar: the local step that would have to produce `dμ` (Proposition 2.9.6, p. 71) is a local **index** computation, not a volume computation, and no other step in the proof produces a measure on `B` (Theorem E: `B` is leafwise, and the only transverse measure in sight is one-dimensional and already used by `ℓ(c)`).

### 11.1 Theorem F — the index–measure dichotomy (verification pass)

The material of §§4–10 assembles into one statement, which is the general form of the verdict and the text proposed for ledger row W13.

> **THEOREM F (index–measure dichotomy) [novelty: single-check].** Let `(X,F,φ)` satisfy [Den05] (5.2) — `X` compact, `F` transversely oriented of codimension one, `φ` a foliated flow everywhere transverse to `F` — and let `B × S¹` be a family of closed orbits of common length ℓ, `B` the parameter space. Then:
>
> **(F1) There is only one transverse direction, and it is already spent.** `codim F = 1` and transversality give `T_pX = R·Y_{φ,p} ⊕ T_pF` at every point, so the invariant transverse measure of `F` is one-dimensional; on `M¹` the normal bundle of the orbit foliation is canonically the leaf bundle, `Nφ ≅ TF` ([ALKL] p. 100, verbatim). Hence the directions in which the family `B` deforms are **leafwise**, and the transverse measure's entire contribution to an orbital term is the factor `ℓ(γ)`, which measures the orbit's own circle ([ALKL] p. 156: the `∫_0^{ℓ(c_j)}|dx|`).
>
> **(F2) In a §7.7 suspension the parameter space is a compact subset of the base manifold**, meeting each fiber of `M̄ → M` at most once (Lemma 5.1); the profinite factor `Γ̄` carries no closed orbits.
>
> **(F3) The trace formula has no linear slot for a measure on `B`.** In (TF) leafwise data enters only through index densities — the leafwise Euler density `e(F)` in `χ_Co` (Lemma 4.0) and the signs `ε_c(k)`, which are produced by a **local Lefschetz index** computation and by nothing else ([ALKL] Prop. 2.9.6, p. 71; §3 (H4-d)).
>
> **(F4) Where the measure would go, an integer sits.** In every model of this note in which the left-hand side is computed exactly, the coefficient of `δ_{kℓ}` contributed by the family is `ℓ · L(h^k)` with `L(h^k) ∈ Z` the Lefschetz number of the leafwise return map (Theorem A) — equivalently, by Lefschetz–Hopf, the total fixed-point index of the family. It equals the Haar-averaged prediction `ℓ·(±1)` **iff** that index is `±1`, and it is `0` for every compact-group family exhibited here.
>
> **(F5) The one regime in which an orbit family is genuinely transverse is `dim F = 0`, and there the cohomological trace does not exist.** If the leaves are points then `X` is one-dimensional, "leafwise" and "transverse" coincide, and DQ-M's literal hypothesis (`B` a Cantor group whose Haar measure is transverse) can be met — but then `A_f` carries every eigenvalue with infinite multiplicity and is not trace class (Proposition 4.3): the object DQ-M asks about does not exist. The *formal* measured trace does return the Haar answer there (§4.4), which is the source of the temptation, and it does not extend to `dim F > 0` because `A_f` is then not a leafwise operator.
>
> **Conclusion.** For a family of closed orbits in a codimension-one foliated flow, "multiplicity" is a **fixed-point index**, not a **transverse measure**; the two agree only when the index is `1`, and a family carrying a transitive translation symmetry has index `0` (Theorem D). ∎ *(F1, F2, F4, F5 are proved above; F3 is a reading of the framework's shape, supported by (H4-d) and Lemma 4.0 — flagged as such in §13.)*

**The `0/0` made precise.** [Lei06] p. 3's Guillemin–Sternberg expression for the contribution of `±kγ` has numerator `det(id − Dφ^{±kℓ(γ)}|T_yF)` and denominator its absolute value. Both vanish along a continuum. Resolving such a quotient is exactly the passage from the isolated-fixed-point Lefschetz formula to the *clean* (Bott) one, whose local answer is a characteristic number of the fixed-point set — for the de Rham complex, an Euler characteristic. That is the mechanism of Theorem B, visible already in the sources.

---

## §12. Program item (3): consequences for Q*, Road 2, and the ledger

### 12.1 Road 2 is closed in the model world

`probe-9.4-note.md` §7 Road 2 reads, verbatim: *"Proposition 1 kills selections but not measures … At the formal level the T1 count then comes out right: the packet's aggregate orbit contribution is `∫_{B_p}(single-orbit term) dHaar` = the single-orbit term, since the integrand is constant"*, and it named its own first obstacle: *"no published trace formula admits a continuum of periodic orbits with a transverse measure on the continuum; building one is an S2-adjacent analysis question, well-posed in the model world (DQ-M, §8)."*

That obstacle is now decided, and the decision is worse than "unbuilt":

* **The formal count is wrong, not merely unjustified.** Theorem B: in the model world the aggregate contribution is `ι_k(B)` times the single-orbit term, and `ι_k(B) ∈ {2, 0, 2−2g, …}` in explicit models — never `1` for a homogeneous `B`.
* **Haar's canonicity is the reason it fails.** Theorem D: translation-invariance of the weight under a transitive symmetry forces the weight to be `0`. The one property that made Haar the natural candidate over a selection is the property that annihilates it.
* **The phrase "transverse measure on the continuum" has no referent.** Theorem E: in a §7.7 suspension the orbit continuum is a leafwise object; the transverse measure is one-dimensional and is already consumed by the factor `ℓ(γ)`.

Hence, in the language of `probe-9.4-note.md` §8 item 2: **DQ-M = NO, and Road 2 is closed.** By that note's own accounting, *"a NO closes Road 2 and, with this note's D1–D3, would leave Road 1 (function-ring enrichment) as the only surviving W9 repair on any current road map"* — Road 1 being the [D25] "stronger descent conditions" experiment, plus Road 3 (per-place coefficients) with its two named obstacles.

### 12.2 Q*: the Road-2 re-scoping must NOT be adopted; a different one is now available

`probe-9.3-adjudication.md` §5 states Q* with the clause, in both faces, *"meeting each packet in exactly one orbit"* (Q-a) / *"with exactly one closed orbit `γ_p` of length `log p` per prime"* (Q-b). `probe-9.4-note.md` §7 proposed, conditionally on a DQ-M YES, to re-scope this to *"meeting each packet in a Haar-measured orbit family"*.

* **That re-scoping is void.** DQ-M is NO. Q*'s clause stands as adjudicated. No edit to `probe-9.3-adjudication.md` §5 is warranted by this probe, and none is made.
* **A different, licensed re-scoping exists [novelty: single-check].** Corollary C3 shows that what the trace formula demands per prime is not *one orbit* but **index one**. So Q*'s clause may be honestly relaxed to
  > **(Q*-idx)** … meeting each packet in a compact family `B_p` of closed orbits of length `log p` whose leafwise return-map fixed-point index is `+1` for every `k ∈ Z^×`.
  This is a strictly weaker requirement than "exactly one orbit" (a single simple orbit with `ε = +1` has index `+1`), it is *not* the Haar relaxation, and **it is not vacuous** — the verification pass replaced the first draft's gesture at "a closed disk of fixed points" with an actual model, since a closed disk is not a closed manifold and Theorem 4.1 does not apply to it:

  > **Construction 12.1 (an orbit continuum of index exactly `+1`, inside a [Den05] §7.7 suspension) [novelty: single-check].** On `Σ = S²` let `W` be the north–south gradient field of the height function `H` for the round metric, with zeros `N` (maximum) and `S` (minimum) and non-stationary orbits the open meridians, along which `H` is strictly increasing. Let `D ⊂ S²` be a closed round disk with `N ∈ int D` and `S ∉ D`; take `ρ ∈ C^∞(S²,[0,∞))` with `ρ^{-1}(0) = D` (Whitney), and let `h` be the time-1 map of `V := ρW`. Form `Y = Σ ×_{ℓZ} R`, the mapping torus (Setup 6.0). Then:
  > * `Z(V) = D ∪ {S}`, and exactly as in Lemma 7.4.2, `Fix(h^k) = D ∪ {S}` for every `k ∈ Z^×` (off `Z(V)` the field `V` is a positive multiple of `W`, so `H` strictly increases along its orbits). So the periodic set of `φ` is `(D × S¹_ℓ) ⊔ ({S} × S¹_ℓ)`: **one continuum of closed orbits of length ℓ, plus exactly one further closed orbit**, and nothing else.
  > * The orbit over `S` is **simple with `ε = +1`**: `dV_S = ρ(S)·dW_S + W_S ⊗ dρ_S = ρ(S)·dW_S` because `W_S = 0`, and `ρ(S) > 0`; `S` is the minimum of `H`, so `dW_S` has two positive eigenvalues, hence `d(h^k)_S = exp(k ρ(S) dW_S)` has two eigenvalues `λ_1, λ_2 > 1`, and `det(id − d(h^k)_S) = (1−λ_1)(1−λ_2) > 0`, i.e. `ε_S(k) = +1` for all `k ∈ Z^×`.
  > * Every orbit of the continuum is maximally degenerate: `ρ ≥ 0` vanishes on `D`, so `dρ = 0` there, so `dV = 0` and `d(h^k)_p = id` for `p ∈ D`; `ε` is undefined on the continuum.
  > * `h ≃ id` (through the flow of `V`), so Theorem A gives the total weight `L(h^k) = χ(S²) = 2` for every `k`. By Lefschetz–Hopf and additivity of the index over the clopen decomposition `Fix(h^k) = D ⊔ {S}`,
  >   ```
  >         ind(h^k, D)  =  L(h^k) − ind(h^k, {S})  =  2 − 1  =  +1     for every k ∈ Z^× .
  >   ```
  > **So the continuum `D` weighs exactly one simple orbit with `ε = +1`, for every `k`** — the aggregate orbital contribution of `D × S¹_ℓ` is `ℓ Σ_{k∈Z^×} δ_{kℓ}`, indistinguishable in the trace formula from a single non-degenerate orbit of length ℓ with `ε ≡ +1`. This is a **positive** answer to the question DQ-M should have asked, and it uses no measure at all. *(Grade: the total `L(h^k) = 2` and `ε_S = +1` are proved here; the split into `ind(h^k,D) + ind(h^k,\{S\})` is classical Lefschetz–Hopf plus index additivity, flagged in §13. Note `χ(D) = 1`, consistent with §4.2's law.)*

  Note what Construction 12.1 does **not** have: `D` is contractible, hence very far from homogeneous. That is not an accident — it is Corollary C3 plus Lemmas 9.1–9.2.
* **But (Q*-idx) is unavailable for Deninger's packets, and this is a theorem, not an intuition.** An index-1 continuum can never be a nontrivial compact group (Lemma 9.1 and Lemma 9.2 give index 0 in both the connected and profinite cases), and Deninger's `B_p = Ẑ^×_{(p)}/p^Ẑ` is an infinite profinite group on which `Aut(C)` acts transitively by translations (9.4 Lemma D, **cited as referee-pending**). So the packets are exactly the continua that (Q*-idx) excludes.
* **Net effect on Q*.** Q-a and Q-b are unchanged; the relaxation (Q*-idx) is recorded as available in principle and closed in fact for `X_0`'s packets; the "measured" escape from the packet-count obstruction is removed from the road map.

### 12.3 Ledger rows touched (annotations only — this note edits nothing)

* **R4** (*"Simple (isolated, nondegenerate) closed orbits; `N_pφ ≅ T_pF` finite-dim (H4)"*, status OBSTRUCTED, *"repair = pass to a one-orbit-per-packet subsystem, whose existence is open (→ S4)"*). Annotation: a **second** candidate repair — "pass to a Haar-measured orbit family" — is now **closed** (this note, Theorem B/D). A **third** — "pass to an index-1 orbit family" — is now identified, is strictly weaker than the first, and is **unavailable for homogeneous packets** (Lemmas 9.1–9.2). H4's failure mode is now understood precisely: what H4 supplies is the local Lefschetz index `ε_c(k)`, and on a continuum that index survives as a Z-valued measure on clopen pieces which vanishes under packet symmetry.
* **R15** (*"Counting measure: each `(p,k)` contributes once, sign +1"*, status OBSTRUCTED, *"in a solenoid route this becomes a design constraint (ε ≡ +1 achieved in the [Den05] §7.7 examples)"*). Annotation: the design constraint is **sharper than ε ≡ +1**. Per-orbit `ε ≡ +1` is neither necessary nor sufficient once orbits come in families; the constraint is `ind(return map, B_p) ≡ +1`. In particular a §7.7 model with `ε ≡ +1` on every orbit of a continuum can still have total weight `0` (§7.5) or `2` (§7.4).
* **W9** (per 9.4 §10: *"9.4 trichotomy: transplant-as-selection closed (D1–D3); surviving roads: descent enrichment [D25], Haar measure (DQ-M), per-place gluing"*). Annotation: the **Haar-measure road is now closed**; the surviving roads are descent enrichment ([D25]/[Lut25]) and per-place gluing, each with the obstacles 9.4 §7 already named.
* **New row candidate W13** [novelty: single-check; the formal statement is **Theorem F**, §11.1]: *"Index–measure dichotomy. In any Deninger/ÁLK02/ALKL-type dynamical Lefschetz trace formula, an orbit continuum's multiplicity is a fixed-point index (Z-valued, leafwise), never a transverse measure; and a continuum carrying a transitive translation symmetry has index 0. Consequence: no canonical measure-theoretic repair of the packet count exists in the model world."* Sources: this note §§4–9; anchors [Den05] pp. 21–22, 35; [ALKL] pp. 3, 71, 99, 100, 155–156; [Lei06] p. 3.
* **Kill-criterion:** does **not** fire. Route 2's unique blocker S4 is untouched: Q-a and Q-b are about one orbit per packet, not about measured families, and neither face is decided here.

### 12.4 A caution the program should carry forward

The `dim F = 0` computation of §4.4 shows that the Haar answer *does* come out right for the **measured (von Neumann) trace**. That is a real fact and a real temptation. It is an artifact of the leaves being points: for `dim F > 0` the operator `A_f = ∫f(t)φ^{t*}dt` is not a leafwise operator and admits no `Λ`-trace, and the framework's only measured slot (`ℓ(γ)`, `χ_Co(F,μ_⊥)`) is transverse and already occupied. Any future proposal to "measure the packet" must therefore say **which trace**, on **which space**, against **which transverse measure** — and, per Theorem E, must explain how a leafwise family acquires a transverse measure. The present note holds that it cannot, in the model world.

---

## §13. Scope and honesty

**What was proved here, in full, from first principles plus on-disk anchors.**
* Theorem A (§6): the exact distributional trace, per degree, for every mapping-torus ([Den05] §7.7 with `Γ̄ = pt`) system, **with no non-degeneracy hypothesis**. Uses [ALKL] (1.2.2)–(1.2.3) (p. 2) for leafwise Hodge on a Riemannian foliation of a closed manifold, and elementary kernel calculus. Independently checked against [Den05] Theorem 7.8 / [ALKL] Theorem 1.3.10 in the non-degenerate case, including the `δ_0` coefficient `χ_Co(F,μ) = χ(M)·l`.
* Theorem B (§7): the counterexamples, including Construction 7.4.1 (a diffeomorphism of `S²`, isotopic to the identity, with Cantor fixed set and no other periodic points) proved in Lemma 7.4.2.
* Theorem E (§5): the category theorem, from [Den05] p. 35's bijection read verbatim and [ALKL] p. 100's `Nφ ≅ TF`.
* Proposition 4.3 and §4.4 (the trivial model in both traces).
* Lemma 9.1 (`χ` of a compact connected Lie group) and Lemma 9.2 (no nonzero invariant Z-valued finitely additive measure on an infinite profinite group) — both proved in full.
* Lemma C4 (`ι` cannot be a multiple of Haar).
* Proposition 10.2 (Model S), modulo Lemma 10.1 (below).
* **Added in the verification pass:** Lemma 4.0 (`χ_Co(F,μ_⊥)` computed directly from the leafwise Euler density, with no hypothesis on the flow — removing the note's only reliance on a source statement made under a hypothesis its models violate); Remark 4.0′ (the refutation compares coefficients at `k ≠ 0` only, hence is independent of the `δ_0` convention, of any `t = 0` renormalization, and of the choice of probability measure `μ`); Lemma 5.1 (`Fix(f̄^k) ≅ Fix(f^k) ⊆ M` is a homeomorphism — a proof of [Den05] p. 35's bijection from the construction, closing escape (E-a) rigorously); Theorem F (§11.1, the dichotomy); Construction 12.1 (an index-`+1` orbit continuum, making the (Q*-idx) relaxation non-vacuous); Remark 9.3 (the calibration of Theorem D).

**Corrections made in the verification pass** (recorded so a referee can see what did *not* survive the re-check):
* **Two page citations were wrong.** [ALKL] Theorem 1.3.10 is on printed **p. 8** (the first draft said p. 7 — Theorem 1.3.8 is on p. 6 and 1.3.10 falls on the next printed page); the Guillemin–Sternberg expression and the ÁLK00 formula in [Lei06] are on printed **p. 3** (the first draft said p. 4). Both corrected throughout. No mathematical claim changed.
* **One proof was wrong.** Lemma 9.2, step (b), enumerated the open normal subgroups of `B`; an infinite profinite group need not have countably many (`(Z/2)^I`, `I` uncountable). Replaced by a maximal-index argument that uses no enumeration. The lemma's statement is unchanged and Theorem D is unaffected.
* **One citation label was wrong.** `[x-03 = x-20]` in the first draft's §0 conflated two distinct Deninger papers; the §7.7 anchor is [Den05] `= x-20`. Corrected.
* **One example was not an example.** The first draft justified "index-1 continua exist" by "a closed disk of fixed points" — but a closed disk is a manifold *with boundary*, to which Theorem 4.1 does not apply, and inside a closed surface the index of the whole fixed set is pinned by `L(h^k)`, so the claim needed a model. Construction 12.1 supplies one, with the extra orbit that makes the arithmetic come out to `+1`.

**What was NOT re-derived, and is flagged.**
1. **Proposition C2 (the clopen-local index form).** The identification of the local contribution of a clopen piece with its fixed-point index uses classical Atiyah–Bott local index theory and the Lefschetz–Hopf theorem; neither was re-derived, and neither is on disk in this session's reading. Theorem D(ii), Construction 12.1's index split, and Corollary C3 inherit this grade (see §9.3 for the exact calibration: Theorem D(i) — the *index* statement — is unconditional modulo classical index theory, and Theorem D is unconditional when the homogeneous continuum carries the **whole** periodic set at that period). **The verdict (Theorem B) does not use it.**
1b. **Theorem F clause (F3).** "The trace formula has no linear slot for a measure on `B`" is a reading of the framework's shape — supported by (H4-d) (the `ε` is produced by Prop. 2.9.6 and by nothing else, verbatim) and by Lemma 4.0 (the only other leafwise entry is the Euler density) — not a proof that no future framework could have such a slot. Flagged as judgment-grade; clauses (F1), (F2), (F4), (F5) are proved.
1c. **Bochner–Montgomery** (§9.3 item 3) is named, not re-derived, and is not load-bearing: it is quoted only to warn against reading Theorem D as an existence claim in the smooth closed-manifold category.
2. **Lemma 10.1 (product decomposition of leafwise reduced cohomology).** Stated with a Hodge-splitting argument; the completed-tensor-product / nuclearity details were not written out. Proposition 10.2 inherits this grade. Proposition 10.3 additionally inherits (1) and the §10.4 law.
3. **The uniform §7.7 law (§10.4).** Proved for `Γ̄ = pt`; verified against [Den05] Theorem 7.8 in non-degenerate solenoidal cases; **not proved in general**.
4. **[x-03] was not re-extracted this session.** Every fact about `X_0` used in §12 (packets, `B_p` an infinite profinite group, `Aut(C)` transitive by translations, Theorem A the packet-closure law, Q*'s wording) is taken from `probe-9.3-adjudication.md` and `probe-9.4-note.md`, which re-derived them from [x-03]. `Aut(C)` transitivity on `B_p` is 9.4 Lemma D and is **cited as referee-pending**, exactly as the charter directs. If Lemma D fell, Theorem D's *application* to `X_0` would fall with it — Theorem D itself, being conditional on a translation symmetry, would not.
5. **[Den05] Theorem 7.8's negative-time normalization** disagrees with [Den05] Theorem 5.3 and [ALKL] Theorem 1.3.10 (Remark 6.4). Flagged, not adjudicated; nothing here depends on `k < 0`.
6. **The passage from the model world to `X_0` is not made and is not claimed.** `X_0` is infinite-dimensional ([x-03] §8, per the adjudication §2 anchor (viii)), non-Hausdorff along its packets (adjudication §4 item 3), and is not known to be a foliated space; no trace formula, of any of the kinds discussed, exists for it. Every theorem in this note is a theorem about compact three-dimensional model systems.
7. **No claim is made about positivity, Hodge-index, or clause (ii) of any Weil-positivity argument** (Z2 quarantine), nor about whether a repaired count would yield a trace formula (W1/W6/W12, R7–R13 stand).

**[RU] items.** None load-bearing. The classical facts invoked by name and not re-derived — Poincaré–Hopf (Lemma 9.1), Lefschetz–Hopf and the fixed-point index axioms (Theorem C1's second sentence, Proposition C2), Whitney's theorem that a closed subset of a manifold is a smooth function's zero set (Construction 7.4.1), Brouwer's characterization of the Cantor set (§7.4) — are standard textbook results, are marked where used, and only items (1)–(3) above carry any weight in the note's structure.

**Judgment-grade readings.** (a) The claim in §4.4 that the `dim F = 0` success of the measured trace is "an artifact" is a judgment about the framework, supported by the observation that `A_f` is not leafwise for `dim F > 0` — that observation is a fact, the word "artifact" is the judgment. (b) The reading of [ALKL] §7.3 as a *local* argument (used to motivate Proposition C2) is a reading of the proof's shape, not a quotation; the quoted material (pp. 155–156) supports it but does not state it. (c) §12.4's caution is advice, not a theorem.

---

## §14. Novelty ledger

Every item is tagged `[novelty: single-check]`; a separate dual-model sweep is to check them. "New" here means: not found in the on-disk sources read this session, and not present in the program's own notes as read.

1. **Theorem A (§6) — the exact leafwise-cohomology trace of a mapping-torus foliated flow, with no non-degeneracy hypothesis.** `Tr(φ*|H̄^n(F)) = ℓ Σ_k tr((h^*)^k|H^n(Σ;C)) δ_{kℓ}`, hence the supertrace `= ℓ Σ_k L(h^k) δ_{kℓ}`. `[novelty: single-check]` — the *non-degenerate* case is [Den05] Thm 7.8 / [ALKL] Thm 1.3.10; the point is that the left-hand side is computable, and finite, with H4 deleted. (The computation itself is elementary; the claim to novelty is its use as a probe of H4.)
2. **Theorem B (§7) — DQ-M is FALSE.** Explicit [Den05] §7.7 suspensions with `dim F = 2` and a continuum of closed orbits of common length ℓ (continuum a surface, a compact connected group with Haar, or a Cantor set) whose orbital side is `ℓ·L(h^k)·δ_{kℓ}` with `L(h^k) ∈ {2, 0, 2−2g}`, never `ℓ·1·δ_{kℓ}`. `[novelty: single-check]`
3. **The Euler-characteristic law in the trivial model (§4.2, Cor. 4.2):** in `Y = B × (R/ℓZ)` the weight of the orbit continuum `B` is `χ(B)`, and DQ-M holds iff `χ(B) = 1`. `[novelty: single-check]`
4. **Theorem C1/Cor. C3 (§8) — the correct measured formula is the index form**, and the exact criterion `ind(return map, B) = 1`. `[novelty: single-check]`
5. **Proposition C2 (§8.2) — the fixed-point-index measure `ι_k` on the clopen algebra of an orbit continuum** as the object replacing `ε_c(k)`. `[novelty: single-check]`, proposition grade (see §13 item 1).
6. **Lemma 9.2 (§9.2) — an infinite profinite group carries no nonzero translation-invariant `Z`-valued finitely additive measure on its clopen algebra.** `[novelty: single-check]`; elementary and quite possibly folklore, flagged as such.
7. **Theorem D (§9.2) — the equivariance no-go**: a packet-symmetric orbit continuum has weight `0`, so the canonicity that recommends Haar measure is precisely what annihilates the contribution. `[novelty: single-check]`
8. **Theorem E (§5) — the category theorem**: in a [Den05] §7.7 suspension the closed orbits are parametrized by the *base manifold*, so an orbit continuum is a leafwise object and admits no transverse measure; the profinite direction of the solenoid carries no closed orbits. With corollaries (E-a) (the "put the packet in the Cantor direction" escape is closed) and (E-b) (`dim F = 2` forces either a mapping torus or `M = T²`, hence `χ_Co = 0`). `[novelty: single-check]`
9. **Construction 7.4.1 / Lemma 7.4.2 — a diffeomorphism of `S²` isotopic to the identity whose fixed-point set is a prescribed Cantor set and which has no other periodic points**, used to produce a Cantor orbit continuum with total weight `+2` inside an otherwise aperiodic flow. `[novelty: single-check]`; the ingredients are standard, the assembly for this purpose is not.
10. **Model S / S-Cantor (§10) — a 3-dimensional [Den05] §7.7 solenoid with an infinite profinite transversal `Γ̄ = Z_2`, an expanding base direction, and a Haar-measured (resp. Cantor) continuum of closed orbits of common length ℓ, of total weight 0.** `[novelty: single-check]`
11. **The uniform §7.7 law (§10.4)** `Σ_n(−1)^n Tr = ℓ Σ_k L(f^k) δ_{kℓ}`, reproducing `χ_Co(F,μ) = χ(M)·l` as its `k = 0` term. `[novelty: single-check]`, proved only for `Γ̄ = pt`.
12. **The re-scoped clause (Q*-idx) (§12.2)** — "index one per packet" in place of "exactly one orbit per packet" — together with the theorem that it is unavailable for homogeneous packets. `[novelty: single-check]`
13. **The diagnosis of DQ-M as a conflation of two traces (§2.2, §4.4)**, with the `dim F = 0` computation showing the Haar answer is correct for the measured trace and the reason that success does not extend. `[novelty: single-check]`
14. **Theorem F (§11.1) — the index–measure dichotomy**, assembling (F1)–(F5) into the general statement: in a codimension-one foliated flow the multiplicity of an orbit family is a fixed-point index and never a transverse measure, the only transverse direction being the flow's and already spent on `ℓ(γ)`; the sole regime in which an orbit family is transverse is `dim F = 0`, where the cohomological trace fails to exist. `[novelty: single-check]`; (F3) is judgment-grade (§13 item 1b).
15. **Construction 12.1 — an orbit continuum of fixed-point index exactly `+1`** inside a [Den05] §7.7 suspension of `S²`: a closed disk `D` of totally degenerate closed orbits of common length ℓ plus one simple orbit with `ε ≡ +1`, with `ind(h^k, D) = +1` for every `k ∈ Z^×`. Shows that "a continuum can weigh exactly one orbit" is realizable, and that what makes it work is contractibility, not measure. `[novelty: single-check]`
16. **Lemma 5.1 — `pr_0 : Fix(f̄^k) → Fix(f^k)` is a homeomorphism**, so a §7.7 orbit family meets each fiber of `M̄ → M` at most once and can never be spread along `Γ̄`. `[novelty: single-check]`; this is a proof, from the construction, of the bijection [Den05] p. 35 asserts, sharpened to a homeomorphism and to the "at most one point per fiber" statement that closes escape (E-a).
17. **Remark 4.0′ — the refutation is convention-free and measure-free:** because the comparison is at `k ≠ 0`, no `δ_0` convention or `t = 0` renormalization can affect it; and because DQ-M's integrand is constant, the claim is the same for *every* probability measure on `B`, so the counterexamples refute it for all of them at once. `[novelty: single-check]`; elementary, recorded because it is what makes a single model decisive.

---

## §15. Bookkeeping

**What this note is.** A referee-grade decision of DQ-M in the model world, with a THEOREM (NO), the exact replacement statement, and two structural theorems (the equivariance no-go and the category theorem). Deliverable file: `results/c3-r/s14/dqm-O.md`.

**Ledger rows / Q* clauses / direction-file entries touched** (annotations proposed for the orchestrator; **this note edits nothing**):

| object | file | proposed annotation |
|---|---|---|
| `§9 item 4` → DQ-M sub-question | `results/c3-r/probe-9.4-note.md` §8 item 2 | **EXECUTED, verdict NO** (pointer here). Road 2 closed. |
| Road 2 | `probe-9.4-note.md` §7 | **CLOSED**: the named first obstacle is not a gap but a theorem against; the Haar count is wrong in the model world and vanishes under packet symmetry |
| W9 | `m2c-feasibility-ledger.md` | surviving roads reduce to descent enrichment ([D25]/[Lut25]) and per-place gluing |
| R4 | `m2c-feasibility-ledger.md` line 111 | H4's content identified as the local Lefschetz index; "Haar-measured family" repair closed; "index-1 family" repair identified and shown unavailable for homogeneous packets |
| R15 | `m2c-feasibility-ledger.md` line 122 | the design constraint is `ind(return map, B_p) ≡ +1`, strictly sharper than per-orbit `ε ≡ +1` |
| new row **W13** | `m2c-feasibility-ledger.md` | index–measure dichotomy (text in §12.3) |
| Q* clauses Q-a / Q-b | `probe-9.3-adjudication.md` §5 | **unchanged**; the Road-2 re-scoping ("Haar-measured orbit family") is void; the alternative (Q*-idx) is recorded but closed for `X_0`'s packets |
| Current frontier, rung (3) "DQ-M" | `directions/C3-geometric-substrate.md` | rung (3) **DONE, NO**; rungs (1), (2) Q*, (4) S2/W3 unaffected |
| kill-criterion | — | **does NOT fire**; S4 undecided; Route 2 not exhausted |

**This note may NOT be cited for:** (1) any claim about `X_0` itself — every theorem here is about compact 3-dimensional model systems (§13 item 6); (2) any positivity/Hodge/clause-(ii) statement (Z2 quarantine); (3) any claim that the packet count *can* be repaired — the note closes one repair and identifies a second that is itself closed for homogeneous packets, and says nothing about repairs outside the trace-formula framework; (4) topology of `Γ_p` from [r3s-08] (adjudication §4 item 4 stands); (5) Proposition C2 / Theorem D / Propositions 10.2–10.3 at theorem grade — they are flagged in §13; (6) `Aut(C)` transitivity on `B_p` as settled — it is 9.4 Lemma D, referee-pending.

**Standing-order 5 record.** Read verbatim from disk this session, and **re-extracted and re-confirmed in the verification pass**: every anchor listed in §1 from [Den05] (pp. 20, 21, 22, 33, 34, 35), [ALKL] (pp. v, 2, 3, 6, 8, 71, 99, 100, 101, 153, 154, 155, 156), [Lei06] (pp. 3, 17). Two page numbers were found wrong on re-check and corrected (§1, §13). The quoted program text was re-read and confirmed verbatim: `probe-9.4-note.md` line 120 (Road 2) and line 130 (the DQ-M statement), `probe-9.3-adjudication.md` §5 (Q-a, Q-b), §2 (uncountability of `B_p`, and `B_p = Ẑ^×_{(p)}/p^Ẑ`), §4 items 3–4, and 9.4 Lemma D(iii); the ledger rows cited are `m2c-feasibility-ledger.md` lines 111 (R4), 122 (R15), 96 (W9), 222 (W12). Derived in full here: Theorem A, Theorem B and its models, Theorem E, Lemma 5.1, Lemmas 6.1–6.3, 7.4.2, 9.1, 9.2, C4, Proposition 4.3, Lemma 4.0, Remark 4.0′, Corollary 4.2, Theorem F (clauses F1, F2, F4, F5), Construction 12.1 (up to the classical index split). Taken from referee-passed program documents without re-derivation: Theorem A of the adjudication (packet-closure law), `B_p` uncountable/profinite, non-Hausdorffness of `X_0`, Q*'s wording, 9.4's Road-2 text and Lemma D (referee-pending). Nothing rests on recalled literature; the classical results named in §13 are marked at each use.

**Independence record.** A parallel probe on this same charter ran on a different model. Nothing in this note was read from it, compared against it, or adjusted to it; every verdict, model, and proof here is this probe's own. Where the two agree, that is a genuine independent confirmation; where they disagree, this note's §§4–7 give explicit models that can be checked by hand in an afternoon, and that is the right way to settle it.

**Standing-order 7 record.** Seventeen items, all tagged `[novelty: single-check]`, listed in §14.

— end of DQ-M probe O note —
