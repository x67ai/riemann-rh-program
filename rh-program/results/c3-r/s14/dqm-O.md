# DQ-M — measured trace formula for orbit continua (probe O)

**Program:** RH research program, direction C3-r (geometric substrate for a Weil-positivity proof of RH), milestone M2c, Route 2 (solenoid intermediate), blocker S4.
**Date:** 2026-09-02 (Session 14). **Author:** probe O (independent; a parallel probe on a different model was run on the same charter — nothing here assumes anything about it).
**Charter:** decide DQ-M (`results/c3-r/probe-9.4-note.md` §8 item 2) in the MODEL WORLD. Program (1) the trivial model; (2) the nontrivial model inside an aperiodic ambient flow, with [ALKL]'s formula quoted from the memoir on disk, the exact place where hypothesis H4 is consumed, and whether the sum over orbits may be replaced by an integral against a transverse measure; (3) consequences for Q*.
**Standing orders:** 5 (nothing load-bearing from memory; every source claim read from the on-disk PDF at a stated page) and 7 (everything believed new is tagged `[novelty: single-check]` and listed in the novelty ledger). U.S. English.

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
> **Two further theorems, both proved here:**
> * **(Equivariance no-go, Theorem D, §9.)** If the continuum B is an infinite profinite group and the model carries any symmetry group acting on B by translations (the exact property that made Haar measure the *canonical* candidate in 9.4 §7 Road 2 — Aut(C) acts transitively on B_p by translations), then the index measure `ι` is a translation-invariant Z-valued finitely additive measure on the clopen algebra of B, and **every such measure is identically 0.** The canonicity that recommends Haar is precisely what forces the weight to vanish.
> * **(Category theorem, Theorem E, §5.)** In a [Den05] §7.7 suspension the closed orbits are in canonical bijection with the finite f-orbits on the *base manifold* M ([x-03 = x-20] p. 35, verbatim). Hence an orbit continuum is always a **leafwise** object. Haar measure on B is a **leafwise** measure; only **transverse** measures enter the trace formula linearly, and leafwise data enters only through index densities (the leafwise Euler density and the signs ε). DQ-M's phrase "the transverse measure on the continuum" has no referent in the framework: it is a category error, and §5 proves it is one.
>
> **What is NOT claimed.** This is a theorem in the model world, not in `X_0 = X(Spec Z)`. `X_0` is infinite-dimensional, non-Hausdorff along packets, and is not known to be a foliated space; no trace formula exists for it. The verdict therefore does **not** kill S4, and does **not** fire the C3 kill-criterion. What it kills is **Road 2** of `probe-9.4-note.md` §7 ("renounce selection; Haar-average the packet") **as a repair of the orbit count inside any trace formula of the Deninger/ÁLK02/ALKL type**, and it forbids the re-scoping of Q* that Road 2 proposed.
>
> **One positive by-product (a different re-scoping of Q*, §12).** The trace formula does not demand *one orbit per prime*; it demands **index one per prime**. `Q*`'s clause "meeting each packet in exactly one orbit" may be relaxed to "meeting each packet in a compact orbit family of fixed-point index 1". Index-1 continua exist (any continuum with χ = 1 — e.g. a closed disk of fixed points). They are never homogeneous spaces, so this exit is disjoint from Road 2 and is not available for Deninger's packets, which are homogeneous by construction.

---

## §1. Sources read this session, with pages

All page references are to the **printed** page of the document. Every quotation below was read this session from the on-disk PDF via a fresh `pdftotext -layout` extraction; nothing in this note is recalled.

| tag | file on disk | pages read | what was taken |
|---|---|---|---|
| **[Den05]** | `fetched/x-20-deninger-2005-arithmetic-geometry-and-analysis-on-foliated-spaces.pdf` (PDF page = printed page) | 20, 21, 22, 33, 34, 35 | §5 non-degeneracy hypothesis; ε_x, ε_γ(k); Conjecture 5.1 (22); Theorem 5.3 = ÁLK02 formula (23); Theorem 5.4; §7.7 suspension construction; Theorem 7.8; χ_Co(F,μ) = χ(M)·l |
| **[ALKL]** | `fetched-r3/r3s-17-alvarez-lopez-kordyukov-leichtnam-trace-formula-foliated-flows-arxiv-2402.06671v1-SESSION8-FETCH.pdf` (**PDF page = printed page + 6**) | v, 1, 2, 3, 4, 5, 6, 7, 8, 71, 99, 100, 101, 153, 154, 155, 156 | abstract; §1.1–§1.2 (leafwise Hodge for Riemannian foliations); §1.3.1 (definition of a simple closed orbit, ℓ(c), ε_c(k)); Theorems 1.3.7, 1.3.8, 1.3.10; §2.9.11 (simple fixed point, ε_p, Proposition 2.9.6); §4.1.1 (C(φ), P(φ), simplicity ⟹ local finiteness); §4.1.2 (Nφ ≅ TF on M¹; Hector case (c)); §7.3 (Theorem 7.3.1, Proposition 7.3.2, properties (N)–(R), display (7.3.8)) |
| **[Lei06]** | `fetched-r3/r3s-21-leichtnam-scaling-group-flow-laminated-p-adic-transversal-arxiv-math0603576v2-SESSION8-FETCH.pdf` (PDF page = printed page) | 4, 17 | the ÁLK00 formula as Leichtnam states it; the **Guillemin–Sternberg local expression** for the geometric contribution of a closed orbit; Theorem 2 = the *laminated, transverse-measure* trace formula, and its hypotheses ("closed orbits … are non degenerate", "L has a dense leaf") |
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
* **[ALKL] p. 7, Theorem 1.3.10**: *"L_dis(φ) = Σ_L χ(L) W_L + ^bχ_{|ω¹|}(F¹) δ_0 + Σ_c ℓ(c) Σ_{k∈Z^×} ε_c(k) δ_{kℓ(c)}."*
* **[ALKL] p. 71, §2.9.11**: *"Recall that a fixed point p of φ is called simple if the eigenvalues of φ_* : T_pM → T_pM are different from 1. This means that the graph of φ is transverse to ∆ in M² at (p,p); **in particular, p is isolated in Fix(φ)**. … Take any relatively compact open neighborhood W of p in U such that W ∩ Fix(φ) = {p}."* and **Proposition 2.9.6**: *"For all z ∈ C, lim_{t↓0} ∫_{q∈W} str(φ_z^* k_{z,t}(φ(q),q)) = ε_p(φ)."*
* **[ALKL] p. 99, §4.1.1**: *"Every simple closed orbit c, there are neighborhoods, V where c in M and I of ℓ(c) in R, such that c is the only closed orbit whose first positive period is in I … The flow φ is called simple if all of its fixed points and closed orbits are simple. **If moreover M is closed, then Fix(φ) is finite, and C_I(φ) are finite for all compact I ⊂ R. Therefore P(φ) is a discrete subset of R.**"*
* **[ALKL] p. 100, §4.1.2**: *"Moreover φ is transverse to the leaves on M¹. So there is a canonical isomorphism **Nφ ≅ TF** on M¹."*
* **[ALKL] p. 101**: Hector's cases; *"(c) F is given by a fiber bundle M → S¹ with connected fibers."*
* **[ALKL] p. 155, properties (N)–(R) in the proof of Proposition 7.3.2(ii)**: *"(N) There is a unique γ_0 ∈ Γ_l such that t_0 = −h_l(γ_0). (O) We have k_j := t_0/ℓ(c_j) ∈ Z … (P) There is some y_j ∈ L_l such that π_l : R × {y_j} → c_j is a C^∞ covering map … (Q) For all p̃ ∈ R × {y_j}, we have γ_0 · φ̃_l^{t_0}(p̃) = p̃. **(R) For all x ∈ R, every y_j is a simple fixed point of the diffeomorphism T_{γ_0}φ̃_{l,x}^{t_0} of L_l** with ε_{y_j}(T_{γ_0}φ̃_{l,x}^{t_0}) = ε_{c_j}(k_j, φ) = ε_{c_j}(k_j)."* followed by *"In particular, there are no other fixed points of T_{γ_0}φ̃_{l,x_j}^{t_0} in some open neighborhood W_j of y_j in L_l."*
* **[Lei06] p. 4**, the Guillemin–Sternberg local expression: *"the geometric contribution of a closed orbit ±kγ should be: l(γ)α(±kl(γ)) Σ_{j=0}^2 (−1)^j Tr((Dφ^{±kl(γ)})^* : ∧^j T_y^*F ↦ ∧^j T_y^*F) / |det(id − Dφ|_{T_yF}^{±kl(γ)})|."*
* **[Lei06] p. 17, Theorem 2**: *"Assume that the closed orbits γ of the flow φ^t acting on S = L×R^{+*}/q^Z are **non degenerate**. Assume the four properties (i) to (iv), that W(L,F) is a factor and that **L has a dense leaf**."*

---

## §2. DQ-M made precise

`probe-9.4-note.md` §8 item 2 poses:

> **DQ-M.** Let `Y = M̄ ×_Λ R` be a [Den05]-§7-type suspension whose periodic set is a continuum `B × S¹` of closed orbits of common length ℓ, B a Cantor group with Haar probability measure μ. Does the distributional trace of the flow on leafwise forms exist, with orbital side `∫_B (single-orbit contribution) dμ` = the single-orbit contribution?

Two things must be pinned down before the question has a truth value.

### 2.1 What "the single-orbit contribution" is

From [Den05] p. 22 (Theorem 5.3) and [ALKL] p. 7 (Theorem 1.3.10), which agree: a closed orbit c of least period ℓ(c) contributes to the orbital side
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

* **(T-coh) the cohomological (Lefschetz) trace.** [Den05] p. 22: `A_φ = ∫_R φ(t) φ^{t*} dt` on the Hilbert completion `Ĥ^n(X,R)` of the leafwise reduced cohomology is **of trace class**, and `Tr(φ*|H̄^n)(φ) := tr A_φ`. Equivalently [Den05] p. 35, Theorem 7.8: `Tr(φ*|H̄^n(X,R)) := Σ_{λ ∈ Sp_n(Θ)} e^{tΘ}` over the eigenvalues of the infinitesimal generator **with their algebraic multiplicities**. This is the trace whose alternating sum is the left-hand side of the dynamical Lefschetz trace formula, and the one Deninger's program needs: the sought spectral side is the set of zeros of ζ **with multiplicities**, i.e. the point spectrum of Θ on `H̄^1`, counted.
* **(T-meas) the measured (von Neumann / Ruelle–Sullivan) trace.** Given an invariant transverse measure Λ of F, one integrates the leafwise Schwartz kernel over the diagonal against Λ. [Lei06] p. 17 builds his Hilbert spaces `H^j_τ` with the Ruelle–Sullivan current `C(Λ)` of the transverse measure `Λ = μ_L dx`; note however that his `TR` is then the **ordinary** trace on that Hilbert space, and his part 1] asserts trace-classness — a hypothesis-laden statement (`W(L,F)` a factor, `L` has a dense leaf), not a free lunch.

**This note answers DQ-M for (T-coh)** — that is the trace "of the flow on leafwise forms" in the sense of every formula on disk, and the only one for which a trace formula exists. §4.3 computes (T-meas) as well in the one model where it is unambiguously defined, and records exactly why its apparent success there is an artifact of `dim F = 0`.

### 2.3 The hypothesis at issue: H4

Call **H4** the standing simplicity/non-degeneracy hypothesis. It appears in the sources in three equivalent guises:

* [Den05] p. 20: `T_xφ^{kℓ(γ)}` has eigenvalue 1 with **algebraic multiplicity one** (the eigenvector being the flow direction `Y_{φ,x}`);
* [Den05] p. 21 / [ALKL] p. 3: `id − φ_*^{kℓ(c)} : T_pF → T_pF` is an **isomorphism**, whose determinant's sign is `ε_c(k)`;
* [ALKL] p. 99: a simple closed orbit is **isolated among closed orbits of nearby period**, and on a closed manifold this forces `C_I(φ)` finite for compact `I` and `P(φ)` discrete.

An orbit continuum violates H4 maximally: if closed orbits of period ℓ accumulate at c, then `id − φ_*^{ℓ}` kills the accumulation direction inside `T_pF`, so `det(id − φ_*^{ℓ}|T_pF) = 0` and `ε_c(k)` is **undefined**. DQ-M is therefore, before anything else, a question about what replaces `ε_c(k)`.

The answer, visible already in the sources: [Lei06] p. 4 records the Guillemin–Sternberg local expression for the contribution of `±kγ`,
```
        ℓ(γ) α(±kℓ(γ)) ·  Σ_{j=0}^{2} (−1)^j Tr( (Dφ^{±kℓ(γ)})^* : ∧^j T_y^*F → ∧^j T_y^*F )
                          -----------------------------------------------------------------
                                        | det( id − Dφ^{±kℓ(γ)} |_{T_yF} ) |
```
The numerator is `det(id − Dφ^{±kℓ(γ)}|T_yF)` (the alternating sum of traces on exterior powers **is** the determinant of `id − Dφ`), so the quotient is `sign det(id − Dφ) = ε_γ(k)`. On a continuum **numerator and denominator both vanish**: the local formula is `0/0`. What resolves a `0/0` of an Euler-form-over-Jacobian type is an **index**, not a measure. Everything below is the rigorous version of that one-line diagnosis.

---

## §3. Where exactly H4 is consumed in ALKL's proof

[ALKL]'s trace formula is Theorem 1.3.10 (p. 7); the orbital half is Theorem 1.3.8 (p. 6), proved in Chapter 7 as Theorem 7.3.1 (p. 153) via Proposition 7.3.2 (p. 154). Tracking H4 through that proof:

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

Since `M⁰ = ∅`, [ALKL] Theorem 1.3.10 (p. 7) collapses to the ÁLK02 formula, i.e. [Den05] (23) p. 22:
```
   (TF)      Σ_{n} (−1)^n Tr(φ* | H̄^n(F))  =  χ_Co(F, μ_⊥) δ_0  +  Σ_γ ℓ(γ) Σ_{k∈Z^×} ε_γ(k) δ_{kℓ(γ)} ,
```
with `μ_⊥ = |ds|`. This is the identity DQ-M asks about.

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

*Proof.* Direct: `L²(B,μ)` is infinite-dimensional because `B` is an infinite compact group (its dual `B̂` is infinite); `1 ⊗ C_f` has the eigenvalues of `C_f` each with multiplicity `dim L²(B)`. `C_f ≠ 0` for suitable `f`. ∎

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

* **(E-a) The escape "put the packet in the Cantor direction" is closed in the model world.** One might hope to model a packet `Γ_p ≅ B_p × S¹` by spreading the orbits along the solenoid's own profinite factor `Γ̄`, where a Haar measure *is* transverse. (E2) forbids it: `Γ̄` contributes no closed orbits. The profinite direction of a §7.7 solenoid is a direction of **leaves**, not of orbits.
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

**Remark 6.4 (a bookkeeping discrepancy in the sources, not load-bearing).** [Den05] Theorem 7.8 (p. 35) writes the negative-time orbital terms with an extra factor `det(−T_xφ^{kl(γ)}|T_xF)`, whereas [Den05] Theorem 5.3 (p. 22) and [ALKL] Theorems 1.3.8/1.3.10 (pp. 6–7) write `ε_γ(k)` symmetrically for all `k ∈ Z^×`, and [Lei06] p. 4 remarks explicitly *"Notice that here there is no dissymmetry for the coefficients of α(−kl(γ)) and α(kl(γ))"*. Theorem A agrees with the symmetric version: the two coincide whenever `|det(T_xφ^{ℓ}|T_xF)| = 1` (e.g. every example in this note), and differ otherwise. Nothing below uses negative `k`; the verdict is drawn from `k ≥ 1`. Flagged, not adjudicated.

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
* every orbit in the continuum is maximally degenerate: `h` is the time-1 flow of a vector field vanishing on `K`, so `dh_p = id` at each `p ∈ K` that is an accumulation point of `K` — i.e. at every point of `K` (`K` is perfect) — hence `det(id − φ^{kℓ}_*|T_pF) = 0` and `ε_c(k)` is undefined, exactly as diagnosed in §2.3;
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
> * `B` contractible (e.g. a closed disk of fixed points of a map isotopic to `id` rel the disk): `ind = χ(B) = 1` ✓ — **an orbit continuum can weigh exactly one orbit**, but only for topological reasons.
> * `B` a nontrivial compact connected Lie group: `ind = χ(B) = 0` ✗ (Lemma 9.1).
> * `B` an infinite profinite group with translation symmetry: `ind = 0` ✗ (Theorem D).

Corollary C3 is the honest replacement statement: **the measured formula for orbit continua is true, with the fixed-point-index measure `ι` in place of the transverse measure; and `ι` is Z-valued, so it is never a probability measure on an infinite `B`.** Indeed:

> **Lemma C4.** If `B` is an infinite profinite group and `ι = c·μ` for `μ` the Haar probability measure and some `c ∈ R`, then `c = 0`.
> *Proof.* For every open subgroup `H ≤ B` of index `n`, `H` is clopen and `μ(H) = 1/n`, so `ι(H) = c/n` must lie in `Z`. Since `B` is infinite profinite, `n` is unbounded over open subgroups, forcing `c = 0`. ∎

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

(b) *Every coset of an open subgroup has index value 0.* Fix an open subgroup `H ≤ B`, `n := [B:H] < ∞`. Translation invariance gives `ι(bH) = ι(H) =: m` for every `b`, and finite additivity over the partition `B = ⊔_{i=1}^n b_iH` gives `ι(B) = n·m`. Hence `n | ι(B)` **for every** open subgroup `H`. Because `B` is infinite profinite, the set of indices `[B:H]` of open subgroups is unbounded (if it were bounded by `N`, the intersection of all open subgroups of index `≤ N` would be an open subgroup — a finite intersection, as there are finitely many such by compactness/openness — contained in every open subgroup, hence equal to `⋂` of a neighborhood basis of `1`, i.e. `{1}`, forcing `B` finite). So `ι(B)` is divisible by arbitrarily large integers, whence `ι(B) = 0`, and then `m = ι(B)/n = 0` for every open `H`.

(c) By (a) and (b) and finite additivity, `ι(U) = 0` for every clopen `U`. ∎

> **THEOREM D (equivariance no-go) [novelty: single-check].** Let `(Y, F, φ)` be a model-world system whose periodic set at length ℓ is a continuum `B × S¹` with `B` an **infinite profinite group**, and suppose there is a group `G` of homeomorphisms of `Y` commuting with `φ` and preserving `F`, acting on the parameter space `B` **by translations, transitively** (the exact hypothesis Road 2 invokes for `Aut(C)` acting on `B_p`). Then the index measure `ι_k` of Proposition C2 is translation-invariant, hence `ι_k ≡ 0` by Lemma 9.2. In particular the **total** weight is `ι_k(B) = 0`, and the packet's contribution to the orbital side of the trace formula **vanishes identically**:
> ```
>        aggregate contribution of the continuum  =  0 · ℓ · δ_{kℓ}  =  0 ,
> ```
> where the trace formula needs `ℓ δ_{kℓ}` (one orbit's worth).

*Proof.* A flow-commuting, foliation-preserving homeomorphism carries closed orbits to closed orbits of the same period and conjugates the leafwise return map `h^k` to itself; the fixed-point index is invariant under such conjugation, so `ι_k(gU) = ι_k(U)` for `g ∈ G`. `G` acts on `B` by translations, so `ι_k` is translation-invariant, and `ι_k` is Z-valued and finitely additive by Proposition C2. Lemma 9.2 applies. ∎

**Grade.** Lemma 9.1 and Lemma 9.2 are proved here in full. Theorem D inherits the grade of Proposition C2 (proposition grade — it needs the local index measure to exist). Theorem B, the verdict, does **not** depend on Theorem D.

**What Theorem D says in words.** Road 2's argument was: *selections are non-canonical, but Haar measure is canonical, therefore average.* Theorem D says: *the canonicity is real, and it is fatal.* An orbit continuum on which a symmetry group acts transitively by translations is exactly a continuum whose fixed-point index must be spread evenly over arbitrarily fine clopen partitions; an integer spread evenly over `n` parts for every `n` is `0`. The naturality test Haar passes is the same test that forces the answer to be `0` rather than `1`.

**The same statement for the connected case**, without index theory: a nontrivial compact connected group `B` has `χ(B) = 0` (Lemma 9.1), and by §4.2 the weight is `χ(B)`. So *both* kinds of compact group — connected and profinite — give weight `0`. The only compact group whose orbit continuum weighs `1` is the trivial group: a single closed orbit.
