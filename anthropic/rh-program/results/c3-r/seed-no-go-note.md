# Products of the per-prime Tate curves of absolute geometry carry no correspondence calculus for the Weil explicit formula

> **DATED REVISION — PRIORITY CORRECTION (2026-08-27). Read before citing or circulating.**
> The independent novelty check of 2026-08-27 (`results/arxiv/novelty-check.md`) found, and this
> session verified from the primary sources, that **Theorems 1, 2 and 3 of this note are
> anticipated**, and that two of the note's own novelty/lineage statements are false. The no-go
> itself — Theorems 4, 5 and 6, and the conclusion that products of the per-prime Tate curves host
> no correspondence calculus — is **not** anticipated and stands.
>
> 1. **Theorems 1–3 are Winkelmann's, from 2002.** J. Winkelmann, *On elliptic curves in
>    SL₂(ℂ)/Γ, Schanuel's conjecture and geodesic lengths*, Nagoya Math. J. **176** (2004),
>    159–180; arXiv:math/0204195 (v1, 15 Apr 2002; v3, 8 Apr 2003). Studying `E_λ = ℂ*/λ^ℤ =
>    ℂ/⟨2πi, log λ⟩` for real algebraic `λ > 1`, his proof of Theorem 2 reads, verbatim (v3,
>    p. 14): *"Isogeny of E_i and E_j implies that there is a Q-linear relation between 4π²,
>    log λ_i log λ_j, 2πi log λ_i and 2πi log λ_j (see lemma 7). Now 4π² ∈ R and log λ_i log λ_j
>    ∈ R, while 2πi log λ_i and 2πi log λ_j are Q-linearly independent elements of iR. Therefore a
>    Q-linear relation can only exist if **4π²/(log λ_i log λ_j) ∈ Q**"*, then divides two such
>    relations to force `log λ_i / log λ_k ∈ Q` against multiplicative independence, on **three**
>    curves `E_i, E_j, E_k`, and concludes *"for each of these curves there is at most one other
>    curve in this family to which it is isogenous"*. Substituting `λ = p` (primes are real
>    algebraic > 1 and pairwise multiplicatively independent by unique factorization) gives this
>    note's Theorem 1 criterion, Theorem 2's one-exceptional-partner bound, and Theorem 3, of which
>    `{2,3,5}` is the numerical instance. **Verified by this session against the arXiv v3 PDF
>    itself, not through a secondary source.**
>
>    **Amended 2026-08-27 (second pass, against v1 *and* v3 and the publisher records).** Five
>    corrections to the paragraph above, all in the direction of precision, none affecting the
>    finding. (i) **There is no §7 in Winkelmann** — the paper has six sections, and the Schanuel
>    argument is **§3.2, Proposition 3, p. 14** ("Conjecture 1 holds, if Schanuels conjecture is
>    true"). (ii) His Theorem 2 assumes `Γ ∩ SL₂(R)` **Zariski-dense**, not cocompact;
>    cocompactness is his §5. (iii) The quoted sentence *"for each of these curves there is at
>    most one other curve in this family to which it is isogenous"* is the **v3 (2003)** wording;
>    v1 (15 April 2002) says "at most two of these `E_i` can be isogenous" — the mathematics is
>    2002, the phrasing is 2003, and the priority date is **15 April 2002**. (iv) He proves **one
>    direction only** of the criterion, necessity: *"a Q-linear relation can only exists if
>    4π²/(log λ_i log λ_j) ∈ Q"*. The converse is one line from his own Lemma 7, which is stated
>    as an equivalence — so the equivalence must be attributed to him too and **cannot** be claimed
>    here as an addition. (v) The word "Hom" does not occur in his paper; neither does "rank"; and
>    no occurrence of "degree" there is an isogeny degree. Nor does he ever take `λ` to be a prime
>    or index the family by primes (his three occurrences of "prime" are prime *ideals* in the §5
>    construction of Γ). What this note adds over him is therefore an **explication in the
>    prime-indexed case** — the group `Hom(E_p, E_q)` identified, its rank, and the degree of the
>    minimal isogeny — not a sharpening of a theorem, and no priority over Theorems 1–3 is
>    available. Bibliographic riders: his given name is **Jörg** (arXiv's metadata ASCII-izes it);
>    there is also a **v2**, 6 Nov 2002; the DOI is 10.1017/S0027763000009016 (Cambridge, not
>    Project Euclid); and both Crossref and Cambridge Core render the title with a spurious `Γ..`,
>    so the arXiv/zbMATH/title-page form is the one to copy.
> 2. **The (T1) rider is a named published conjecture.** §9's *"The question (T1) appears to be
>    unrecorded in the literature in this form and is stated here as open"* is **false**. (T1) is
>    D. Bertrand's **weak four-exponentials conjecture** (Madras Number Theory Symposium, January
>    1996), stated verbatim in G. Diaz, *J. Théor. Nombres Bordeaux* (1997) §I, whose Théorème 1
>    proves the equivalence this note re-derives and whose Propositions 1 and 3(1) give
>    unconditional partial results the note does not know about. The four-exponentials conjecture
>    itself is Schneider 1957, Problem 1.
> 3. **The lineage claim is off by nine and a half years.** §1.2 and §9 item 3 say the per-prime
>    elliptic-analogue idea first appears in the Connes–Consani orbit in **January 2025** [CC25].
>    It appears in **July 2015**: Connes–Consani, *The Scaling Site*, arXiv:1507.05818 (21 Jul
>    2015), abstract — *"The restriction of this structure to the periodic orbits of the scaling
>    flow gives, for each prime p, an analogue of an elliptic curve whose Jacobian is a cyclic
>    group of order p−1"* — published as *Geometry of the Scaling Site*, Selecta Math. **23**
>    (2017), which [CC26] itself cites for exactly this. **Verified against the arXiv abstract.**
>
>    **Amended 2026-08-27 (second pass).** The 2015 object must be described correctly or the
>    correction over-corrects. It is **`C_p = R^×_+/p^Z`**: a **real** circle of circumference
>    `log p` — the periodic orbit of the scaling flow — carrying a characteristic-one structure
>    sheaf of convex piecewise-affine functions with slopes in `Z[1/p]`, with `J(C_p) ≅ Z/(p−1)Z`
>    and a **real-valued** Riemann–Roch formula. Connes and Consani present it themselves as an
>    analogue: *"a quasi-tropical structure which turns this orbit into a variant `C_p = R^×_+/p^Z`
>    of the classical Jacobi description `C^*/q^Z` of an elliptic curve"* [CC17, abstract]. So the
>    **idea** of a per-prime elliptic-curve analogue is July 2015 and the note's "January 2025" is
>    off by nine years and five months; but the **complex Tate curve `E_p = C^×/p^Z`** — the object
>    this note actually works with, with its genuine complex structure, its lattice `Λ_p` and its
>    classical intersection theory — enters the Connes–Consani program in **June 2026** [CC26],
>    where `C_p` reappears as the connected component of `E_p`'s real locus and `E_p ≅ C_p × X̃_∞`.
>    Both statements are true and the note must carry both.
>
> 4. **Correction to a correction: the `[CC26]` title.** The clause "and the Fargues–Fontaine
>    curve" **is** part of the title — it is on the paper's own title page and in arXiv's HTML
>    full text — and the novelty report's request to drop it must **not** be executed. But the
>    mechanism recorded earlier in this program ("the arXiv API truncates the title at a TeX
>    macro") is **not** the right diagnosis and is withdrawn: the clause is absent from arXiv's
>    *metadata* generally — the abs page's `<h1>`, the `citation_title` meta tag, the API, the
>    PDF's own metadata dictionary, and zbMATH — while present in the rendered document. The
>    conclusion stands; the explanation was wrong.
>
> **Consequence for the framing.** This note may no longer present Theorems 1–3 as new. The honest
> framing is: Winkelmann's rigidity, transported to the Connes–Consani per-prime Tate curves of
> June 2026 and combined with the Néron–Severi collapse (Theorem 4), the prime-blind diagonal
> residue (Theorem 5, unconditional via Gelfond–Schneider) and Theorem 6, yields a no-go for the
> correspondence calculus that is new. `results/c3-r/prior-art-r7a.md` §5's sentence — "the
> obstruction is elementary lattice arithmetic that could in principle have been noted about ANY
> pair of complex tori … and no one has" — is **withdrawn**; it was noted, in 2002. The full
> citation list and the required textual repairs are in `results/arxiv/novelty-check.md` §D.


**A no-go note (barrier-zoo entry IV.10, publishable form).**
**Program:** RH program, direction C3 (geometric substrate), reduced recommission C3-r.
**Date:** 2026-08-26 (Session 6).
**Status:** adjudication-certified content (`results/adjudication-C3.json`, computation (a); blind-replicated by two independent killer cycles, `results/verdicts-c3d1.json`); prior-art gate **passed 2026-08-26** with verdict **novel-with-citations** (`results/c3-r/prior-art-r7a.md`); numerics in `results/c3-r/seed-no-go-checks.{py,json}`. Referee pass **completed 2026-08-26** (`results/c3-r/referee-seed-no-go.md`): FAIL-as-written on one fatal — the original §7 transcendence-status claims were false *in the note's own disfavor* — repaired in place with the referee's drafted replacement (dated record in §11); nine referee-applied mechanical repairs incorporated. **Circulation-ready.**

---

## 0. Summary

Connes–Consani's June-2026 absolute geometry of Spec **Z** [CC26] produces, for every prime `p`, a complex elliptic curve — the Tate curve `E_p = C^×/p^Z`, a rectangular torus with period lattice `Λ_p = Z ⊕ Z·τ_p`, `τ_p = i·log p/(2π)`. For the first time, the absolute-geometry program yields per-prime genus-1 fibers carrying *classical* intersection theory. The C3 commission's seed proposal (M2b) was to assemble the long-missing correspondence calculus for the Weil explicit formula — the "square of Spec **Z**" — from the `(p,q)`-graded family of classical abelian surfaces `E_p × E_q`, importing the Castelnuovo–Severi positivity fiber-by-fiber instead of waiting for the unbuilt characteristic-one square.

**This note proves that the proposal is empty — not approximately, not "bandwidth data in geometric dress," but empty.** The results:

**Attribution, stated at the top so nothing below is misread (2026-08-27).** Items 1–3 of the
list that follows — the isogeny criterion, the two-partner rigidity and the three-curve kill —
are **not new**: they are Winkelmann's, from 15 April 2002 [Wi04], transported here to the
per-prime Tate curves and specialized to primes. Items 4, 5 and 6 — the Néron–Severi collapse,
the prime-blind diagonal residue, and the no-go — are this note's, and are not anticipated. The
attribution is set out in full in the dated block at the head of this note and in the banner at
the top of §3; the citation-and-distinguish record is §9, item 8.

1. **Isogeny criterion (Theorem 1, iff; Winkelmann's, specialized):** for distinct primes `p ≠ q`, `Hom(E_p, E_q) ≠ 0` **iff** `log p · log q ∈ 4π²·Q` — a transcendence coincidence expected never to occur (open unconditionally; impossible under the four-exponentials conjecture, §7). When nonzero, `Hom` has rank 1 and is computed exactly.
2. **Two-partner rigidity (Theorem 2, unconditional; Winkelmann's, specialized):** each prime has at most **one** "exceptional partner" prime with which it could share a nonzero `Hom` — pure unique factorization, no transcendence input. The exceptional pairs, if any exist at all, form a partial matching on the primes.
3. **The {2,3,5} coherence kill (Theorem 3, unconditional; Winkelmann's three-curve run, specialized):** among the three surfaces `E_2×E_3`, `E_2×E_5`, `E_3×E_5`, at most one carries a nonzero correspondence group; no two of them can simultaneously do so. Any composition-coherent correspondence family over all pairs of primes is unconditionally impossible.
4. **Néron–Severi collapse (Theorem 4):** `NS(E_p × E_q) = Zξ₁ ⊕ Zξ₂ ⊕ Hom(E_p, E_q)` [BL, Ch. 5; reproved here]. Off the exceptional matching, NS has rank 2 (the two fiber classes): there are **no graph classes, no diagonal class**, every divisor class acts as **zero** on `H¹`, and the Castelnuovo–Severi/Hodge-index inequality — the positivity the seed was commissioned to harvest "for free" — is **vacuous** (its primitive domain is the zero group).
5. **Diagonal residue (Theorem 5):** the surfaces `E_p × E_p` do carry a correspondence calculus — `End(E_p) = Z` **unconditionally**, the CM alternative `(log p)² ∈ 4π²·Q` being impossible by Gelfond–Schneider (§7) — but its complete intersection profile `(Γ_m·Γ_n) = (m−n)²`, `(Γ_m·Δ) = (m−1)²` consists of **universal integers independent of `p`**. The explicit formula's transcendentally weighted prime terms `Λ(n) f(log n)/√n` cannot arise from it except by hand-inserting the weights into the test-family coefficients — barrier IV.1 re-entry ("no new data coordinate").
6. **No-go (Theorem 6):** no assignment of correspondence groups, composition data, and intersection pairing on the family `{E_p × E_q}` realizes the commissioned calculus for the Weil explicit formula. Three independent obstructions — no composition material (unconditional), no pairing target, prime-blind diagonal data — each individually fatal.

Of the two transcendence questions the construction raises, only one survives as a caveat: the diagonal coincidence `(log p)² ∈ 4π²Q` is **refuted unconditionally** (Gelfond–Schneider; §7, Proposition), and the off-diagonal coincidence `log p·log q ∈ 4π²Q` — (T1), an instance of the four-exponentials conjecture — is logged as the note's single open rider (§7) with numerical evidence; **the family-level kill is unconditional and consumes neither.**

Scope (§8): this kills the *substrate family*, not the direction. The Connes–Consani characteristic-one square (route A) and the Deninger leg (route C/M2c) are untouched; the note in fact sharpens why the square problem cannot be outflanked through the new complex fibers. Prior art (§9): the construction and the no-go (Theorems 4–6) are unanticipated; the rigidity (Theorems 1–3) is Winkelmann's, 2002; eight adjacent traditions are cited and distinguished.

---

## 1. Background: the curves and the proposal

### 1.1 The missing square

The classical template for proving a Riemann hypothesis — Weil's positivity argument on the square `C × C` of a curve over `F_q`, with the Castelnuovo–Severi inequality supplied by Riemann–Roch and ampleness — needs a doubled object. Over **Q** that object ("the square of Spec **Z**," a surface-like host on which the Weil explicit formula becomes an intersection-number computation) exists in no branch of mathematics. Connes' own summary of the stall, in print since 2015 and still accurate: *"[W]hat is missing is an intersection theory and a Riemann-Roch theorem on the square of the arithmetic site"* [CE15, §4.3.2; on-disk t-20b, quote program-verified]. The square does exist in characteristic one — Frobenius correspondences as congruences on the square of the arithmetic site [CC16] — but with no intersection theory and no Riemann–Roch, a decade on.

### 1.2 The per-prime Tate curves

The June-2026 paper [CC26] ("On the Absolute Geometry of Spec Z and the Fargues–Fontaine curve") changes the available raw material. Evaluating the points of `(Spec Z)_{F₁}` over **C**, the non-trivial points over a prime `p` form a torsor under the Weil group `W_∞ = C^×`; quotienting by the discrete Frobenius symmetries `p^Z ⊂ W_∞` produces the **complex Tate curve**

```
E_p := M_p^∞ / p^Z ≅ C^× / p^Z ,
```

*"which canonically carries the structure of an elliptic curve over C"* [CC26, eq. (4) and §4.1.2; all quotes from the program's on-disk full-text extraction, `sources-extracted/arxiv-2606.06604-absolute-geometry-specZ-fulltext.txt`, lines 240–260 and 1518–1600]. Lifting through `w ↦ exp(2πiw)` gives `E_p ≅ C/Λ_p` with

```
Λ_p = Z ⊕ Z·τ_p ,   τ_p = i·log p/(2π) ,
```

a rectangular torus defined over **R** (the paper's own statement, extraction line 1526). Complex conjugation descends to a canonical real structure whose real locus is two copies of the adelic periodic orbit `C_p = R⁺^×/p^Z`. The paper's Geometric Decomposition theorem (stated as Theorem 4 in its introduction and Theorem 5 in §4.3 of the HTML full text) gives a canonical global splitting

```
E_p ≅ C_p × X̃_∞ ,
```

where `C_p` (length `log p`) carries the entire dependence on `p` and the phase circle `X̃_∞` (length `2π`, an unramified double cover of the real Fargues–Fontaine analogue `X_∞ ≅ P¹(R)`) is **totally independent of `p`**; the modular parameter `τ_p` is exactly the ratio of the two invariant 1-forms' periods. We use three facts and only these: the lattice `Λ_p`; the reality/rectangularity; and the `p`-independence of the phase factor.

**Lineage (first-appearance record; rewritten 2026-08-27 against the primary sources — the previous version of this paragraph dated the idea to January 2025 and was wrong by nine years and five months).** The per-prime *elliptic-analogue* idea appears in the Connes–Consani orbit on **21 July 2015**, in the Comptes Rendus note *The scaling site* [CC16b] and at length in *Geometry of the scaling site* [CC17]. The object there is **`C_p = R^×_+/p^Z`**: the periodic orbit of the scaling flow, a **real** circle of circumference `log p`, given a quasi-tropical structure sheaf `O_p` of convex piecewise-affine functions with slopes in `Z[1/p]`, with Jacobian `J(C_p) ≅ Z/(p−1)Z` and a **real-valued** Riemann–Roch formula `Dim_R H⁰(D) − Dim_R H⁰(−D) = deg(D)` [CC16b, Lemma 6.3, Thm. 6.5, Thm. 6.7(ii)]. Its authors present it as an analogue and say so: *"a quasi-tropical structure which turns this orbit into a variant `C_p = R^×_+/p^Z` of the classical Jacobi description `C^*/q^Z` of an elliptic curve"* [CC17, abstract], and later, *"`C_p = R^×_+/p^Z` appears as an elliptic curve in characteristic one, similar to the Jacobi elliptic curve `C^*/q^Z`. The Riemann–Roch formula for `C_p` involves real valued dimensions"* [CC24a, §1].

What is **new in June 2026** is not the per-prime analogue but the **complex** curve: `E_p = C^×/p^Z` with a genuine complex structure, the lattice `Λ_p`, and classical intersection theory — with `C_p` reappearing inside it as the connected component of the real locus, `E_p ≅ C_p × X̃_∞` [CC26]. That is the object this note works with, and it is the reason the seed proposal became formulable at all. The intermediate paper [CC25] (*Knots, primes and class field theory*, January 2025), which the earlier version of this paragraph named as the first appearance, contributes something else again — a functor from finite abelian extensions of **Q** to finite covers of `X_Q`, under which the monodromy of the periodic orbit of length `log p` corresponds to the Galois action of Frobenius at `p` — and it cites [CC17] for the elliptic-curve analogue rather than introducing it.

Unchanged, and independently re-confirmed: **none** of these papers raises products of the `E_p`, correspondences between different primes, or any isogeny question — grep of the on-disk full text of [CC26] returns no isogeny/Hom/product-of-Tate-curves content, and [CC25]'s full text returns no hits for "isogen" or "Tate" [prior-art report §5; re-run 2026-08-27].

### 1.3 The seed proposal being killed

The C3 commission (2026-08-19; `directions/C3-geometric-substrate.md`, retained verbatim there as the immutable record) required, in the function-field template, a calculus with three components:

- **(R1) Doubled object + correspondence monoid.** Correspondence groups containing the diagonal `Δ`, the fiber classes `ξ₁, ξ₂`, and one Frobenius-type class `Ψ_p` per prime; closed under composition and transpose; multiplicativity `Ψ_m ∘ Ψ_n = Ψ_mn` with `Ψ_p` primitive exactly at primes.
- **(R2) The pairing.** An intersection pairing with `(Ψ_f · Δ) = W(f)` for test elements `Ψ_f = ∫ f(λ) Ψ_λ d*λ` — the Weil explicit formula as an intersection number, prime terms, archimedean term, and pole term all accounted.
- **(R3) Positivity.** A Hodge-index/Castelnuovo–Severi inequality on the host, derived from Riemann–Roch plus effectivity (the M1 non-circularity route, re-derived in `results/c3-r/m1-noncircularity.md`).

The seed (commission asset 3, milestone M2b) proposed to realize (R1)–(R3) on the `(p,q)`-graded family of classical abelian surfaces `E_p × E_q`, with the multiplicativity axiom realized as a descent/compatibility datum *across* the family, and the archimedean and pole terms hoped to live on the `X̃_∞` factor. The commission's own stated fear (gate Z5/risk R2) was that the family might only express *bilinear* data — `Λ(p^a)Λ(q^b)` cross-terms, bandwidth-style data in geometric dress. Theorems 1–6 below show the situation is worse: the family expresses **no** prime-facing correspondence data at all.

For the structure of the target, recall the explicit formula in one standard normalization (Weil 1952; the exact archimedean shape is immaterial here): for suitable test functions `f`, with `f̂(s) = ∫_R f(x) e^{(s−1/2)x} dx`,

```
W(f) = f̂(0) + f̂(1) − Σ_{n≥2} (Λ(n)/√n)·(f(log n) + f(−log n)) − W_∞(f) ,
```

`W_∞` an explicit archimedean integral. Only three structural features are load-bearing for this note:

- **(W-i)** the prime side is **linear** in `Λ(n)`, with transcendental weights `f(±log n)/√n` that vary with `n` and with `f`;
- **(W-ii)** there is an archimedean term;
- **(W-iii)** there are pole terms.

---

## 2. Notation and the lattice presentation

Throughout, `p, q, …` denote primes; set

```
y_p := log p/(2π) > 0 ,   τ_p := i·y_p ,   Λ_p := Z ⊕ Z·τ_p ,   E_p := C/Λ_p .
```

**Lemma 0 (lattice presentation; [CC26] §4.1.2).** `exp₂: C → C^×`, `w ↦ e^{2πiw}`, is a surjective homomorphism with kernel `Z`, and

```
exp₂(w + τ_p) = e^{2πiw}·e^{2πi·(i y_p)} = e^{2πiw}·e^{−log p} = p^{−1}·exp₂(w) .
```

Since `p^Z = (p^{−1})^Z` as subgroups of `C^×`, `exp₂` induces an isomorphism `C/Λ_p ≅ C^×/p^Z`. ∎

(Numerically confirmed to 55 digits — check A of `seed-no-go-checks.json`. The sign of `τ_p` is immaterial: `Z ⊕ Z(−τ_p) = Λ_p`.)

Standard facts used without further comment: every homomorphism of complex tori `C/Λ → C/Λ′` is induced by a unique `λ ∈ C` with `λΛ ⊆ Λ′` (lift to the universal cover); every holomorphic map between complex tori is a homomorphism followed by a translation (rigidity); `Hom(E, E′)` denotes the group of holomorphic homomorphisms.

---

## 3. Theorem 1: the isogeny criterion (iff)

> **ATTRIBUTION (added 2026-08-27; read before §§3–4).** **The rigidity proved in §§3–4 is
> Winkelmann's, from 15 April 2002** [Wi04], transported here to the Connes–Consani per-prime Tate
> curves of June 2026. It is not new, and it is not presented as new. Studying `E_λ = C^*/λ^Z`
> for eigenvalues `λ` of elements of a discrete subgroup of `SL₂(C)`, Winkelmann proves, inside the
> proof of his Theorem 2 (v3, p. 16; v1, pp. 12–13), exactly the three things §§3–4 prove:
>
> * **the criterion**, in the necessity direction — *"Isogeny of `E_i` and `E_j` implies that there
>   is a Q-linear relation between `4π²`, `log λ_i log λ_j`, `2πi log λ_i` and `2πi log λ_j` (see
>   lemma 7). Now `4π² ∈ R` and `log λ_i log λ_j ∈ R`, while `2πi log λ_i` and `2πi log λ_j` are
>   Q-linearly independent elements of `iR`. Therefore a Q-linear relation can only exists [sic] if
>   `4π²/(log λ_i log λ_j) ∈ Q`"* — which is Theorem 1's forward direction, by the same
>   real/imaginary separation used below. **The converse is not stated by him, but it is one line
>   from his own Lemma 7, which is an equivalence** (`C/Λ` and `C/Γ` are isogenous *iff*
>   `dim_Q ker Φ > 0`), so the "iff" of Theorem 1 is his too and is not claimed here.
> * **the two-partner rigidity of Theorem 2** — he divides two such relations to get
>   `log λ_i/log λ_k ∈ Q`, contradicting multiplicative independence, and concludes *"for each of
>   these curves there is at most one other curve in this family to which it is isogenous"* (v3
>   wording; v1: "at most two of these `E_i` can be isogenous");
> * **the three-curve run of Theorem 3** — his argument is stated on three curves `E_i, E_j, E_k`;
>   `{2,3,5}` is the numerical instance.
>
> **What is genuinely not in Winkelmann**, and is what §§3–4 add: the word "Hom" does not occur in
> his paper, nor does "rank", nor any isogeny degree; and he never takes `λ` to be a prime or
> indexes the family by primes. So the additions here are the **identification of the group
> `Hom(E_p, E_q)` and its rank, the degree `uv` of the minimal isogeny, and the specialization to
> primes** — an explication in the prime-indexed case, not a strengthening of his theorem. That
> the specialization was available to anyone since 2002 is precisely why the program's earlier
> prior-art sweeps missed it: they searched prime-indexed phrasing, and Winkelmann's is
> eigenvalue-and-geodesic-length phrasing.
>
> **The no-go itself — Theorems 4, 5 and 6 — is not anticipated and does not rest on any claim of
> priority over §§3–4.** Winkelmann's context is the geometry of `SL₂(C)/Γ` and hyperbolic geodesic
> length spectra; he raises no Néron–Severi group, no correspondence calculus, and no explicit
> formula. Proofs are given below in full because the note must be self-contained and because the
> prime-indexed forms differ in presentation from his.

**Theorem 1.** Let `p ≠ q` be distinct primes. Then

```
Hom(E_p, E_q) ≠ 0   ⟺   y_p·y_q ∈ Q   ⟺   log p · log q ∈ 4π²·Q .
```

Moreover, when the condition holds and `y_p y_q = u/v` in lowest terms (`u, v ∈ Z_{>0}`), the full homomorphism group is

```
Hom(E_p, E_q) = Z·λ₀ ,   λ₀ = i·v·y_q ,
```

of rank 1, and the isogeny induced by `λ₀` has degree `uv`.

**Proof.** A nonzero homomorphism is multiplication by some `λ ∈ C^×` with `λΛ_p ⊆ Λ_q`. Two containment conditions:

1. `λ·1 ∈ Λ_q`: so `λ = a + b·τ_q = a + i·b·y_q` for some `a, b ∈ Z`.
2. `λ·τ_p ∈ Λ_q`: compute `λ·τ_p = (a + i b y_q)·(i y_p) = −b·y_p y_q + i·a·y_p`. Writing this as `c + i·d·y_q` with `c, d ∈ Z`:
   - real part: `−b·y_p y_q = c ∈ Z`;
   - imaginary part: `a·y_p = d·y_q`.

*Case `a ≠ 0`.* Then `d ≠ 0` (as `y_p, y_q > 0`) and `y_p/y_q = d/a`, i.e. `log p/log q ∈ Q`, i.e. `a·log p = d·log q` with `a, d` nonzero integers, i.e. `p^a = q^d` (after clearing signs) — impossible for distinct primes by unique factorization. So `a = 0`, hence `d = 0`.

*Case `a = 0`.* Then `λ = i·b·y_q` with `b ≠ 0` (else `λ = 0`), and the surviving condition is `b·y_p y_q ∈ Z`, which forces `y_p y_q ∈ Q`. This proves the forward direction, and identifies `Hom = {i·b·y_q : b ∈ Z, b·y_p y_q ∈ Z}`. With `y_p y_q = u/v` in lowest terms, `b·u/v ∈ Z ⟺ v | b`, so `Hom = Z·(i·v·y_q)`.

*Converse.* If `y_p y_q = u/v`, then `λ₀ = i·v·y_q` satisfies `λ₀·1 = v·τ_q ∈ Λ_q` and `λ₀·τ_p = (iv y_q)(i y_p) = −v·y_p y_q = −u ∈ Z ⊆ Λ_q`, so `λ₀Λ_p ⊆ Λ_q` and `λ₀ ≠ 0` — a genuine isogeny. (Numerically confirmed on a synthetic pair with `y y′ = 3/7` exactly — check B.)

*Degree.* `covol(Λ_p) = y_p` and `covol(λ₀Λ_p) = |λ₀|²·y_p = v²y_q²·y_p`, so `deg = [Λ_q : λ₀Λ_p] = v²y_q²y_p / y_q = v²·(y_p y_q) = v²·(u/v) = uv`.

Finally `y_p y_q ∈ Q ⟺ log p log q = 4π²·y_p y_q ∈ 4π²Q`. ∎

*(Attribution, per the banner above: the forward direction is Winkelmann's argument [Wi04, proof
of Thm. 2, p. 16], and the converse is immediate from his Lemma 7. What is added here is the
computation of `Hom(E_p, E_q) = Z·λ₀` with `λ₀ = i·v·y_q`, its rank, and the isogeny degree `uv` —
none of which appears in his paper.)*

**Remark 1 (bookkeeping reconciliation, per the adjudication).** In the verification cycle one killer stated the criterion as `log p·log q ∈ 4π²·Q` and the other derived `b·log p·log q = −4π²c`, phrasing it as `log p·log q ∈ π²·Q`. These are the **same condition**: `4π²·Q = π²·Q` as subsets of **R**, because `4 ∈ Q^×` — a rational multiple of `π²` is a rational multiple of `4π²` and conversely. The normalization-free statement is `y_p·y_q ∈ Q`; we display the constant as `4π²` because `y_p y_q = log p·log q/(4π²)` makes it the natural one. The adjudication (computation (a)) records exactly this reconciliation.

**Remark 2 (symmetry).** The criterion is symmetric in `p` and `q`; hence `Hom(E_p,E_q) ≠ 0 ⟺ Hom(E_q,E_p) ≠ 0` (as the general theory also guarantees via the dual isogeny). "Exceptional partner" is therefore a symmetric relation.

---

## 4. Theorems 2 and 3: the unconditional family-level kill

**Theorem 2 (two-partner rigidity).** For every prime `p` there is **at most one** prime `q ≠ p` with `Hom(E_p, E_q) ≠ 0`. Consequently the set of "exceptional pairs" `{p, q}` (pairs with nonzero Hom), if nonempty, forms a **partial matching** on the primes: no prime appears in two of them.

**Proof.** Suppose `q ≠ q′` are two such primes. By Theorem 1, `y_p y_q ∈ Q^×` and `y_p y_{q′} ∈ Q^×`. Dividing: `y_q / y_{q′} = (y_p y_q)/(y_p y_{q′}) ∈ Q`, i.e. `log q / log q′ ∈ Q`, i.e. `q^m = q′^n` for some positive integers `m, n` — impossible for distinct primes by unique factorization. ∎

*(This is Winkelmann's division step verbatim, with multiplicative independence of `λ_i` and `λ_k`
replaced by unique factorization for `q` and `q′` [Wi04, proof of Thm. 2, p. 16].)*

Nothing here consumes any transcendence input: the proof is unique factorization plus linear algebra over **Q** applied to the products `y_p y_q`, and it is agnostic about whether any exceptional pair exists.

**Theorem 3 (the {2,3,5} coherence kill).** Among the three surfaces `E_2×E_3`, `E_2×E_5`, `E_3×E_5`, at most one carries a nonzero correspondence group; in particular **no two of them — a fortiori not all three — can simultaneously carry nonzero correspondence groups.** (By Theorem 4 below, "correspondence group of `E_p×E_q`" = `Hom(E_p,E_q)`.)

**Proof.** Any two of the three pairs `{2,3}, {2,5}, {3,5}` share a prime, so two simultaneously nonzero groups would give some prime two exceptional partners, contradicting Theorem 2. Directly: if `y_2y_3 = r₁ ∈ Q^×` and `y_2y_5 = r₂ ∈ Q^×` then `y_3/y_5 = r₁/r₂ ∈ Q`, i.e. `log 3/log 5 ∈ Q`, i.e. `3^m = 5^n` — impossible; the other two cases are identical. ∎

**Remark 3 (enlarging the family does not help).** Define `E_n := C^×/n^Z` for any integer `n ≥ 2` (modulus `y_n = log n/(2π)`) — the natural home for composite-index members `Ψ_{pq}` of the commissioned monoid. The computation of Theorem 1 goes through verbatim, with one new phenomenon: the case `a ≠ 0` now requires `log m/log n ∈ Q`, which for general integers means `m` and `n` are **multiplicatively dependent** (`m = k^a, n = k^b`), and then `E_m`, `E_n` are indeed isogenous (the subgroups `k^{aZ}, k^{bZ}` of `C^×` are commensurable). So the enlarged family admits exactly the isogenies of **one-generator towers** `{E_{k^a}}_a` — and across towers, by the two-partner argument applied to multiplicatively independent moduli, at most the same conjecturally-empty exceptional structure as in Theorem 2, now a partial matching of *towers* (two partners `n, n′` of a fixed `m` are forced into a single tower, and a cross-tower isogeny would need the same unproven rational-product coincidence as Theorem 1). This is a structural echo of the adjudicated Lemma-B fork on the same commission: the printed polarized-Frobenius axioms are satisfiable precisely by one-generator (single-prime) monoids — the char-`p` template is a one-prime template. The geometry says the same thing: per-prime towers exist; the cross-prime structure, which is where the arithmetic of ζ lives, is exactly what is absent.

**Remark 4 (what a failure of the transcendence rider would and would not change).** If some pair of primes actually satisfied `log p·log q ∈ 4π²Q` — spectacular transcendence news — Theorem 1 would produce one isogeny of computable degree `uv`. It would not revive the seed: Theorems 2 and 3 cap the total supply of cross-prime maps at a partial matching, and the obstructions O2 and O3 of Theorem 6 are untouched.

---

## 5. Theorem 4: Néron–Severi collapse off the matching

We first fix the classical dictionary. For elliptic curves `E, E′` over **C**, the group of *divisorial correspondences* from `E` to `E′` is `NS(E × E′)` modulo the subgroup generated by the two fiber classes `ξ₁ = [{0}×E′]`, `ξ₂ = [E×{0}]` (Weil's "trivial correspondences"):

```
Corr(E, E′) := NS(E × E′) / ⟨ξ₁, ξ₂⟩ .
```

**Theorem 4.** Let `E, E′` be elliptic curves over **C**. Then there is a canonical isomorphism

```
NS(E × E′) ≅ Z·ξ₁ ⊕ Z·ξ₂ ⊕ Hom(E, E′) ,
```

hence `Corr(E, E′) ≅ Hom(E, E′)` [BL, Ch. 5; self-contained proof below; for a precise modern
statement of the decomposition see also Rosen–Shnidman [RS14, Prop. 2.3], who preface it "is
well-known" — it is cited here as a locator, not as its origin]. Consequently, for distinct primes `p ≠ q` with `Hom(E_p, E_q) = 0` (i.e., every pair outside the — conjecturally empty — exceptional matching of Theorems 1–2):

- **(a) Rank collapse.** `NS(E_p × E_q) = Zξ₁ ⊕ Zξ₂` has rank 2, with intersection form `ξ₁² = ξ₂² = 0`, `ξ₁·ξ₂ = 1`: every divisor class is numerically `aξ₁ + bξ₂`, and `Corr(E_p, E_q) = 0`.
- **(b) `H¹`-inertness.** Every divisor class on `E_p × E_q` acts as **zero** on `H¹` (in both directions, `H¹(E_p) → H¹(E_q)` and the transpose). The correspondence calculus is not merely small; as a calculus of operators it is the zero calculus.
- **(c) No graphs, no diagonal.** The only holomorphic maps `E_p → E_q` are constants, so the only graph classes are fiber classes. There is no diagonal: not as a curve (a "diagonal" in a product of nonisomorphic curves means the graph of an isomorphism, and none exists), and not even as a numerical class — no `D ∈ NS` satisfies the diagonal's numerical triple `(D·ξ₁, D·ξ₂, D²) = (1, 1, 0)`, since `D·ξ₁ = D·ξ₂ = 1` forces `D = ξ₁ + ξ₂` and then `D² = 2 ≠ 0`.
- **(d) Castelnuovo–Severi vacuous.** The Hodge-index/Castelnuovo–Severi inequality on a product of curves is the statement that the intersection form is negative semidefinite on the *primitive* part `⟨ξ₁, ξ₂⟩^⊥ ⊂ NS`. Here that primitive part is `0`: if `D = aξ₁ + bξ₂` satisfies `D·ξ₁ = b = 0` and `D·ξ₂ = a = 0` then `D = 0`. Equivalently: every class of bidegree `(d₁, d₂)` satisfies `D² = 2d₁d₂` — Castelnuovo–Severi holds *with equality everywhere*, carrying zero information. The positivity the seed advertised as "free fiber-by-fiber" is free because there is nothing left for it to constrain.

**Proof of the decomposition.** All inputs are standard abelian-variety theory ([BL], Ch. 2 for the Poincaré bundle, seesaw, and rigidity; Ch. 5 for the endomorphism context; the statement itself is the classical correspondence dictionary). Write `Ê′ = Pic⁰(E′)` for the dual, `P` for the Poincaré bundle on `Ê′ × E′`, normalized so that `P|_{{α}×E′} ≅ α` for `α ∈ Ê′` and `P|_{Ê′×{0}}` is trivial.

*Step 1 (the homomorphism `φ_L`).* For `L ∈ Pic(E×E′)` put `L_x := L|_{{x}×E′}`; `deg L_x` is constant in `x`. Normalize:

```
L̃ := L ⊗ pr₁^*(L|_{E×{0}})^{−1} ⊗ pr₂^*(L₀)^{−1} ,
```

so that `L̃_x = L_x ⊗ L₀^{−1} ∈ Pic⁰(E′)` for all `x`, `L̃₀` is trivial, and `L̃|_{E×{0}}` is trivial. By the universal property of `(Ê′, P)` there is a unique morphism `φ_L : E → Ê′` with `(φ_L × id_{E′})^*P ≅ L̃` (the a-priori ambiguity by `pr₁`-pullbacks is killed by restricting to `E×{0}`, where both sides are trivial). Since `L̃₀` is trivial, `φ_L(0) = 0`; a pointed morphism of abelian varieties is a homomorphism (rigidity). So `φ_L ∈ Hom(E, Ê′)`.

*Step 2 (kernel; factorization through NS).* `L ↦ φ_L` is additive: normalization and restriction are additive in `L`, and uniqueness plus the biadditivity of the Poincaré bundle (`((add)×id)^*P ≅ pr₁₃^*P ⊗ pr₂₃^*P` on `Ê′×Ê′×E′`, [BL Ch. 2]) give `φ_{L⊗L″} = φ_L + φ_{L″}`. If `L ∈ Pic⁰(E×E′)` then, since the dual of a product is the product of the duals, `L = pr₁^*M ⊗ pr₂^*M′` with `M ∈ Pic⁰(E)`, `M′ ∈ Pic⁰(E′)`; the normalization annihilates it, so `φ_L = 0` and the map factors through `NS(E×E′)`. Conversely if `φ_L = 0` then `L̃_x` is trivial for every `x` and `L̃|_{E×{0}}` is trivial, so by the seesaw principle `L̃` is trivial; hence

```
L ≅ pr₁^*(L|_{E×{0}}) ⊗ pr₂^*(L₀) ,
```

whose Néron–Severi class is `deg(L|_{E×{0}})·ξ₁ + deg(L₀)·ξ₂` (the class of `pr₁^*` of a degree-`d` bundle is `d·[{pt}×E′] = d·ξ₁`, and symmetrically). So the kernel of `NS → Hom(E, Ê′)` is exactly `Zξ₁ ⊕ Zξ₂` (a free rank-2 group: the intersection numbers against `ξ₂, ξ₁` read off the coefficients).

*Step 3 (surjectivity and splitting).* For `ψ ∈ Hom(E, Ê′)` set `L^ψ := (ψ × id_{E′})^*P`. Then `L^ψ_x = P|_{{ψ(x)}×E′} = ψ(x) ∈ Pic⁰(E′)`, `L^ψ₀` is trivial, and `L^ψ|_{E×{0}} = ψ^*(P|_{Ê′×{0}})` is trivial — so `L^ψ` is already normalized and `φ_{L^ψ} = ψ` by uniqueness. Additivity of `ψ ↦ [L^ψ]` is the Poincaré biadditivity again. This splits the sequence:

```
NS(E×E′) ≅ Zξ₁ ⊕ Zξ₂ ⊕ Hom(E, Ê′) .
```

*Step 4 (eliminating the dual).* For an elliptic curve, `x ↦ [O_{E′}([x] − [0])]` is a canonical isomorphism `E′ ≅ Ê′` (the degree-one principal polarization; Abel–Jacobi), so `Hom(E, Ê′) ≅ Hom(E, E′)`. ∎

**Proof of (a)–(d).** (a) is immediate from the decomposition with `Hom = 0`, plus `ξ₁² = ξ₂² = 0` (disjoint parallel fibers) and `ξ₁·ξ₂ = 1` (one transverse point).

(b) The action of a correspondence on cohomology, `α ↦ pr₂_*([D] ∪ pr₁^*α)`, depends only on the class `[D] ∈ H²(E×E′, Z)`. Künneth: `H² = (H²⊗H⁰) ⊕ (H¹⊗H¹) ⊕ (H⁰⊗H²)`. A class `pr₁^*β` (`β ∈ H²(E)`) acts on `α ∈ H¹(E)` by `pr₂_*(pr₁^*(β ∪ α)) = 0` since `β ∪ α ∈ H³(E) = 0`; a class `pr₂^*β` acts by `β ∪ pr₂_*(pr₁^*α) = 0` since fiber integration drops the degree of `pr₁^*α ∈ H¹` below zero. Now `ξ₁ = pr₁^*[pt]` and `ξ₂ = pr₂^*[pt]`, so with `NS = Zξ₁ ⊕ Zξ₂` every *algebraic* class in `H²` has vanishing `H¹⊗H¹`-component and acts as zero on `H¹`. The transpose direction is identical using `Hom(E_q, E_p) = 0` (Remark 2).

(c) Rigidity: every holomorphic map `E_p → E_q` is a homomorphism followed by a translation; `Hom = 0` leaves the constants, whose graphs are horizontal fibers `E_p × {c} ≡ ξ₂`. The numerical computation is displayed in the statement.

(d) Displayed in the statement; the classical Castelnuovo–Severi inequality itself (for products of curves with actual correspondences) is re-proved from RR + ampleness, with no zeta input, in `results/c3-r/m1-noncircularity.md`, and is in the published literature at Milne [Mil16, Thm. 1.5, §1] so that a referee need not follow a program-internal file path — the engine is a real theorem whose domain of application is, on these surfaces, the zero group. ∎

**Remark 5 (what still exists on these surfaces).** Rank-2 NS does not mean the surfaces are curve-poor: `ξ₁ + ξ₂` is ample (Nakai: positive square, positive on every effective class), and general members of `|3(ξ₁+ξ₂)|` are irreducible curves dominating both factors. The point of (a)–(b) is that every such curve is *numerically* a fiber combination and acts as zero on `H¹`: as a correspondence it is invisible. The collapse is a collapse of the correspondence calculus, not of the surface's geometry — which is exactly what kills the seed, whose entire value proposition was the calculus.

---

## 6. Theorem 5: the diagonal residue is prime-blind — and the no-go

The one place the family genuinely has correspondences is the diagonal line `E_p × E_p`.

**Theorem 5 (diagonal residue).** Fix a prime `p`.

1. `End(E_p) = Z`, **unconditionally**. (The lattice computation below shows the only alternative would be `(log p)² ∈ 4π²·Q` — which would make `τ_p` imaginary quadratic and `E_p` a CM curve — and that coincidence is impossible: Gelfond–Schneider, §7, Proposition. No `E_p` has complex multiplication.)
2. By (1), `NS(E_p × E_p) = Zξ₁ ⊕ Zξ₂ ⊕ Z·[Δ]` has rank 3 and `Corr(E_p, E_p) ≅ End(E_p) = Z`, generated by the diagonal. The available correspondences are (combinations of fiber classes and) the graphs `Γ_m` of multiplication by `m ∈ Z`, with `Γ₁ = Δ`, and their complete intersection profile is:

```
Γ_m·ξ₁ = 1 ,   Γ_m·ξ₂ = m² ,   (Γ_m·Γ_n) = (m−n)²  (m ≠ n) ,   (Γ_m·Δ) = (m−1)²  (all m: at m = 1 this is Δ² = 0, by adjunction with K = 0 and e(E_p) = 0) .
```

3. **Every number in this profile is a universal integer, independent of `p`.** More precisely: under the real-affine identification `E_p ≅ R²/Z²` sending `(1, τ_p)` to the standard basis, the subtori `Γ_m, ξ₁, ξ₂` correspond to the *same* subtori for every `p`, and intersection numbers of divisor classes are topological (cup products of integral classes). The map `p ↦ (complete intersection profile of E_p × E_p)` is constant. The prime enters the surface only through its complex structure `τ_p`, and the complex structure enters the correspondence calculus only through `Hom`/`End` — which is the same ring `Z` for every `p` (part 1).

**Proof.** (1) `λΛ_p ⊆ Λ_p` with `λ = a + i b y_p` (from `λ·1 ∈ Λ_p`) requires `λ·τ_p = −b y_p² + i a y_p ∈ Λ_p`, i.e. `−b y_p² ∈ Z` (and the `τ_p`-coefficient `a ∈ Z`, automatic). If `b ≠ 0` then `y_p² ∈ Q`, i.e. `(log p)² ∈ 4π²Q` — impossible by the §7 Proposition (Gelfond–Schneider; a `b ≠ 0` endomorphism would make `τ_p² = −y_p² ∈ Q`, i.e. `τ_p` quadratic imaginary and `End` a CM order, and no `E_p` admits this). So `b = 0` and `λ = a ∈ Z`: `End(E_p) = Z` with no exceptional case.

(2) Theorem 4 with `E = E′ = E_p` gives `NS = Zξ₁ ⊕ Zξ₂ ⊕ End(E_p)`, and the graph of `id` is `Δ`. Intersection numbers: `Γ_m` meets a vertical fiber `{x}×E_p` in the single transverse point `(x, mx)`, so `Γ_m·ξ₁ = 1`. It meets a horizontal fiber `E_p×{c}` in the fiber `[m]^{−1}(c)`, which has `m²` points, all transverse (`[m]` is unramified), so `Γ_m·ξ₂ = m²`; here `#ker([k]) = #((1/k)Λ_p/Λ_p) = k²` (representatives `(i + j·τ_p)/k`, `0 ≤ i, j < k`; check D tabulates them for `k ≤ 7`). For `m ≠ n`, `Γ_m ∩ Γ_n = {(x, mx) : (m−n)x = 0} = ker([m−n])`, with `(m−n)²` points, each transverse (tangent directions `(1, m)` and `(1, n)` are independent), so `(Γ_m·Γ_n) = (m−n)²`; `n = 1` gives `(Γ_m·Δ) = (m−1)²` — which is also the Lefschetz number `1 − 2m + m²` of `[m]` (trace on `H⁰ − H¹ + H²`), the integer Lefschetz data of the family.

(3) The subtori `Γ_m` are the images of `x ↦ (x, mx)`, defined by the *integral* linear data `m` alone; under the identification by the basis `(1, τ_p)` they are the same integral subtori of `R⁴/Z⁴` for every `p`. Cup products of integral classes on a fixed topological manifold are `p`-independent. ∎

**Theorem 6 (the no-go).** No assignment of correspondence groups, composition data, and intersection pairings on the family of classical surfaces `{E_p × E_q}` (`p, q` prime; optionally enlarged by composite moduli `E_n` per Remark 3) realizes the commissioned calculus (R1)–(R3) for the Weil explicit formula. Specifically:

- **(O1) The composition material does not exist (unconditional at family level).** (R1) needs one primitive `Ψ_p` per prime with composites `Ψ_p ∘ Ψ_q` supported across the family — nonzero elements of cross-prime correspondence groups for essentially all pairs. By Theorem 4, `Corr(E_p, E_q) ≅ Hom(E_p, E_q)`; by Theorems 2–3 these groups vanish outside at most a partial matching of exceptional pairs, and already over `{2,3,5}` at most one of the three groups is nonzero. The correspondence category of the family (objects `E_p`, morphisms `Corr`) is unconditionally too disconnected to carry a multiplicative monoid indexed by all primes: the multiplicativity axiom has no material to act on. (Whether even a single exceptional pair exists is the open transcendence question (T1) of §7 — unneeded for this conclusion.)
- **(O2) The pairing target does not parse off the diagonal.** (R2) pairs test correspondences against the diagonal. On every off-matching surface `E_p × E_q` there is no diagonal and no graph class — not even a numerical class with the diagonal's profile (Theorem 4c) — and every class acts as zero on `H¹` (Theorem 4b), so no trace-type functional is available; the Castelnuovo–Severi inequality (R3) is vacuous there (Theorem 4d). The positivity engine is a real theorem with an empty domain.
- **(O3) The diagonal residue cannot host the prime terms.** On the surfaces `E_p × E_p` the calculus exists but its complete intersection profile is the universal integer data of Theorem 5, identical for every `p`. A test element `Ψ_f = Σ_m c_m(p)·Γ_m + a·ξ₁ + b·ξ₂` has

  ```
  (Ψ_f · Δ) = Σ_m c_m(p)·(m−1)² + a + b ,
  ```

  a fixed integer-coefficient linear functional of the coefficients. By (W-i) the explicit formula's prime side is linear in `Λ(n)` with weights `f(±log n)/√n` — transcendental, `n`-dependent, `f`-dependent, and non-constant in `p`. Since the geometric data is constant in `p`, *any* dependence of `(Ψ_f·Δ)` on `p` must be written into the coefficients `c_m(p)` by hand — i.e., the designer inserts the answer key `Λ(p)f(log p)/√p` into the test family and the geometry contributes nothing. This is precisely the program's barrier IV.1 ("Weil positivity in disguise" / no new data coordinate), the failure mode the commission's own Z2 clause promised to avoid: the prime contact was to be "the correspondence calculus itself or nothing." It is nothing. The archimedean term (W-ii) fares no better: the candidate home named by the commission — the phase factor `X̃_∞` — is `p`-independent *by the source paper's own decomposition theorem* ([CC26] Thm 5 and §4.3: "totally independent of p"), so it cannot source prime-dependent weights; and the pole terms (W-iii) have no candidate home at all.

Each obstruction is individually fatal; they are logically independent (O1 concerns the cross-prime category, O2 the off-diagonal surfaces, O3 the diagonal ones). ∎

**Rider (the escape routes forfeit the point).** The `p`-flow and `q`-flow are conjugate through the real-analytic maps `λe^{iθ} ↦ λ^{log q/log p}·e^{iθ}` — but these are not holomorphic, and a smooth (or characteristic-one) correspondence theory on the products gives up exactly the classical `(1,1)`-class positivity (Castelnuovo–Severi via RR + ampleness) that was the seed's entire selling point, landing back on the missing characteristic-one square with its absent intersection theory [CE15 §4.3.2]. There is no version of the family that keeps both the cross-prime maps and the classical positivity.

---

## 7. The transcendence status: (T2) refuted (Gelfond–Schneider), (T1) the single open rider

Two number-theoretic questions arise from Theorems 1 and 5 and are logged here per the adjudication's mandatory repair 1. One of them turns out not to be open at all: classical transcendence theory refutes it, in this note's favor.

- **(T1)** For distinct primes `p, q`: is `log p · log q ∈ 4π²·Q` possible? (Equivalently: can `E_p` and `E_q` be isogenous?) — **open unconditionally**; refuted under the four-exponentials conjecture (below), and refuted under the sharper statement identified in the next paragraph.

**(T1) is a named published conjecture, not an unrecorded question (corrected 2026-08-27).** Its
negation is printed as a displayed, labeled conjecture — **(C4E faible)** — on p. 231 of Diaz
[Dia97], attributed there to D. Bertrand (Madras Number Theory Symposium, January 1996; published
as [Ber97, §5]): for positive real algebraic `α₁, α₂ ≠ 1`, the numbers `π²` and
`(log α₁)(log α₂)` are **Q**-linearly independent. Substituting `α₁ = p`, `α₂ = q` gives exactly
`log p · log q ∉ π²·Q = 4π²·Q`, i.e. ¬(T1); and the sentence immediately following it in Diaz is
the same four-exponentials reduction this note performs below. Two riders, both from the
2026-08-27 verification and both binding on how this is cited. First, the English name "Bertrand's
weak four-exponentials conjecture" is **not a term of art**: Diaz's label is `(C4E faible)`, and
Waldschmidt uses no such English phrase in *Open Diophantine Problems*, in the AWS Lecture 5 notes,
or in *Linear Independence of Logarithms of Algebraic Numbers*. Call it "the weak form of the
four-exponentials conjecture, due to Bertrand" and cite Diaz's label. Second, Diaz's paper also
carries **unconditional partial results** bearing on this question — his Théorème 1 (the
equivalence (C0) ⟺ (C6)) and his Propositions 1 and 3(1) — which this note did not know about and
does not consume.

Winkelmann's own conjectural resolution is adjacent and worth recording: his **Conjecture 1**
[Wi04, §3.2, p. 13] states that for algebraic `α₁, α₂` with `|α_i| > 1`, the quotients
`C^*/α_i^Z` are isogenous **iff** `α₁, α₂` are multiplicatively dependent. Applied to `α₁ = p`,
`α₂ = q` — algebraic, `> 1`, and multiplicatively independent by unique factorization — it gives
`Hom(E_p, E_q) = 0`, hence ¬(T1) by the converse half of Theorem 1. He does not draw that
consequence and never mentions primes, so the implication is recorded here as a one-line deduction
from his conjecture and his Lemma 7, not as a result of his. He proves Conjecture 1 under
Schanuel's conjecture [Wi04, §3.2, Prop. 3, p. 14] — the same reduction §7 performs below,
seventeen years earlier.
- **(T2)** For a prime `p`: is `(log p)² ∈ 4π²·Q` possible? (Equivalently: can `E_p` have complex multiplication?) — **no; refuted unconditionally:**

**Proposition (no CM anywhere in the family).** For every prime `p`, `(log p)² ∉ 4π²·Q`. Hence no `E_p` has complex multiplication, and `End(E_p) = Z` for every prime, unconditionally (Theorem 5(1)).

*(A second, stronger unconditional route to the same conclusion, added 2026-08-27.)*
Barré-Sirieix, Diaz, Gramain and Philibert [BDGP96] proved the Mahler–Manin conjecture: for `q`
algebraic with `0 < |q| < 1`, the modular invariant `J(q)` is transcendental. The Tate curve
`E_p = C^×/p^Z` has nome `q = p^{−1}`, which is algebraic with `|q| < 1`, so `j(E_p)` is
transcendental — and a curve with transcendental `j` has no complex multiplication, since CM
forces `j` to be an algebraic integer. That gives `End(E_p) = Z` unconditionally, with more
information than the Gelfond–Schneider route below, which is retained because it is elementary,
self-contained, and settles the exact coincidence `(log p)² ∈ 4π²Q` rather than a consequence of
it.

**Proof (Gelfond–Schneider, 1934).** Suppose `(log p)² = 4π²·r` with `r ∈ Q`. Both sides are positive, so `r > 0`, and taking positive square roots, `log p = 2π√r`, i.e. `p = e^{2π√r}`. With the branch `log(−1) = iπ`,

```
p = e^{2π√r} = e^{(−2i√r)·(iπ)} = (−1)^{−2i√r} .
```

The base `−1` is algebraic, `≠ 0, 1`; the exponent `β = −2i√r` is algebraic (a product of `i` and the real algebraic number `√r`), nonzero, and purely imaginary — hence irrational, whether or not `√r` is itself rational. By the Gelfond–Schneider theorem, `(−1)^β` is transcendental. But it equals the integer `p` — contradiction. ∎

(Equivalently, in the linear-forms language: (T2) says `log p = (−2i√r)·(iπ)` — a **Q̄**-linear relation between the two **Q**-linearly independent logarithms `log p` and `log(−1) = iπ`, one real and one imaginary; their ratio would be the algebraic irrational `−2i√r`, exactly what Gelfond–Schneider forbids. The point is that this *quadratic* relation among `log p, π` **factors** into linear-forms territory because `√r` is algebraic. It is the classical family "`e^{π√d}` is transcendental" — the circle of Gelfond's constant `e^π` and the Ramanujan constant — specialized to `d = 4r`.)

**Status of (T1).** Known unconditionally: `log p/log q ∉ Q` (unique factorization — this is all Theorems 2, 3 consume), and the Proposition above on the diagonal. The genuinely quadratic *cross-prime* relation does not factor the same way — it involves two independent logarithms — and no proven theorem currently excludes it. It is, however, an **instance of the four-exponentials conjecture** [4EC] — and, more sharply, the
negation of the weak form of that conjecture due to Bertrand, printed as (C4E faible) in
[Dia97, p. 231] — not merely adjacent to either:

**(4EC ⟹ ¬(T1)).** Suppose `log p·log q = 4π²·u/v` (`u/v ∈ Q`, necessarily positive). Take `x₁ = 2πi`, `x₂ = log p` — **Q**-linearly independent (compare real and imaginary parts) — and `y₁ = 1`, `y₂ = log q/(2πi)` — **Q**-linearly independent (`y₂` is purely imaginary and nonzero, hence irrational). The four exponentials are `e^{x₁y₁} = 1`, `e^{x₁y₂} = q`, `e^{x₂y₁} = p`, and `e^{x₂y₂} = e^{log p·log q/(2πi)} = e^{−2πi·u/v}`, a root of unity. All four are algebraic — contradicting the four-exponentials conjecture. ∎

**The published state of the art on (T1), and why the proven machinery misses it.** The four-exponentials conjecture is Schneider's Problem 1 [Sch57, Ch. V, end of §4], formulated explicitly later by Lang [Lan66a, Lan66b] and Ramachandra [Ram68, part II, §4]; Waldschmidt's matrix form is Conjecture 3.7 of *Open Diophantine Problems*, with the matrix restatement on its p. 269 [Wal04]. The proven results closest to (T1) are Roy's [Roy92] and Diaz's [Dia07]. Diaz's Corollaire 1(1) [Dia07] is the natural instrument, and it does not reach: it requires the triple `(λ₀, λ₂, λ̄₂)` to be **Q̄**-linearly free, which fails here because `λ₂ = log q` is real, so `λ̄₂ = λ₂`. That is the citable reason (T1) is not settled by the available theorems, rather than merely "not settled".

The **proven** six-exponentials theorem does not obviously reach (T1), for an amusing reason: it needs a third row `x₃` with both `e^{x₃y₁}`, `e^{x₃y₂}` algebraic, and — taking `x₃ = log ℓ` for a third prime, the natural candidate — the algebraicity of `e^{x₃y₂}` would itself require a *second* rational-product coincidence `log ℓ·log q ∈ 4π²Q`, which this note's own Theorem 2 (two-partner rigidity) forbids alongside the first. The rigidity that makes the no-go unconditional is the same rigidity that keeps its one open rider out of the proven theorem's reach.

**Conditional resolution (Schanuel; retained as the stronger statement).** Schanuel's conjecture implies the full algebraic independence of `log p, log q, iπ` — hence ¬(T1), and it re-proves the Proposition. Take `x₁ = log p`, `x₂ = log q`, `x₃ = iπ`. These are **Q**-linearly independent: in `a·log p + b·log q + c·iπ = 0` the imaginary part forces `c = 0`, and then unique factorization forces `a = b = 0`. Schanuel then gives

```
trdeg_Q Q(log p, log q, iπ, e^{x₁}, e^{x₂}, e^{x₃}) = trdeg_Q Q(log p, log q, iπ, p, q, −1) ≥ 3 ,
```

and since `p, q, −1` are algebraic, `log p, log q, iπ` are algebraically independent over **Q**. In particular `log p·log q + r·(iπ)² ≠ 0` for every rational `r` — i.e. `log p·log q ∉ π²Q = 4π²Q`. ∎

**The status ladder for (T1):** open unconditionally ⊂ settled by the four-exponentials conjecture (as an instance) ⊂ settled by Schanuel (with full algebraic independence). Nothing in Theorems 2–6 consumes any rung of it: the family-level kill needs only unique factorization, which is exactly why it was engineered to be independent of (T1) — and (T2) is no longer a rider at all.

**Numerical evidence (honesty check; `seed-no-go-checks.{py,json}`, checks C and E).** Rows 1–3 below are evidence on the open question (T1); rows 4–5 concern (T2), which the Proposition settles, and are retained not as evidence but as **detector controls confirming a theorem** — the instruments correctly find no rational value where Gelfond–Schneider says none exists. At working precision 400 digits:

| target | value (first digits) | PSLQ (coeffs ≤ 10³⁰) | CF terms to `q_N > 10¹⁰⁰` | max partial quotient |
|---|---|---|---|---|
| `log2·log3/(4π²)` | 0.0192890205998215679007346039996508659… | no relation | 201 | 4591 |
| `log2·log5/(4π²)` | 0.0282579044193212256166934388383576738… | no relation | 201 | 1598 |
| `log3·log5/(4π²)` | 0.0447877188535867805034209039422156347… | no relation | 179 | 284 |
| `(log2)²/(4π²)` | 0.0121700170136801879558172286287261109… | no relation | 160 | 226 |
| `(log3)²/(4π²)` | 0.0305723743263550882536179008172733061… | no relation | 191 | 1521 |

PSLQ finds no integer relation `m·x + n = 0` with coefficients up to `10³⁰` for any target; the continued-fraction expansions, scanned until the convergent denominator exceeds `10¹⁰⁰`, do not terminate and show no anomalously large partial quotient — so **any rational value of any target has denominator exceeding `10¹⁰⁰`** (if `x = a/b` with `b ≤ q_N`, its continued fraction terminates within the scanned, precision-guaranteed range). Detector control in the positive direction: the same PSLQ instance recovers `log 8 = 3·log 2` instantly (check E). Status of this evidence: for (T1) it is evidence, not proof — and nothing in Theorems 2–6 consumes it; for (T2) the proof is the Proposition, and the numerics merely confirm the detectors work. In the exceptional-coincidence direction, Remark 4 records that even a true (T1) coincidence would create only a single isogeny inside the matching bound and would leave obstructions O2 and O3 intact.

---

## 8. Scope: what dies, what does not

**What dies (adjudication-executed; this note is the publishable record).**

- **M2b**, the Tate-curve assembly seed, as commissioned: struck. The `(p,q)`-graded family cannot carry (R1) (no composition material — unconditional), (R2) (no pairing target off-diagonal; prime-blind data on-diagonal), or a non-vacuous (R3).
- **N2**, the planned "first empirical data on the seed" sandbox over `{E_2×E_3, E_2×E_5, E_3×E_5}`: ill-posed twice over — Theorem 3 shows no coherent correspondence assignment over the three surfaces exists to be measured (unconditionally, at least two of the three carry no correspondence class at all), and off the conjecturally empty exceptional matching the surfaces contain no graph classes and no diagonal to enumerate against (Theorem 4).
- **Commission thesis asset 3** ("a genuinely new substrate option the literature has never raised"): the option is genuinely new (§9) and genuinely empty.

**What does not die.**

- **Route A (the Connes–Consani characteristic-one square).** Untouched — and complemented: the stall there is a *missing* intersection theory on an *existing* square [CC16; CE15 §4.3.2], whereas this note certifies that the classical-complex escape hatch out of characteristic one — the one the June-2026 curves seemed to open — is empty. The two results bracket the problem from opposite sides: the char-one square has correspondences (Frobenius congruences) but no positivity calculus; the complex surfaces have the full classical positivity calculus but no correspondences. What the explicit formula needs is *both at once*, and neither habitat supplies the pair. (C3-r keeps route A as a time-boxed watch: [CC7] re-check ≥ Nov 2026.)
- **Route C (the Deninger leg, M2c).** Untouched; it is C3-r's primary mathematical leg (ALKL conormal-current transplant to the Witt space; see `results/c3-r/m2c-feasibility-ledger.md`).
- **M3 (Hodge index over adelic curves).** Untouched, instrument-track; this note if anything sharpens its honest framing (the positivity engine is real and RH-free — M1 — but an engine is only as good as its substrate).
- **The curves `E_p` themselves.** Nothing here diminishes [CC26]'s construction; the no-go concerns only the pairwise *products* as a correspondence substrate — a use the paper itself never proposes.
- **Pair-indexed data as such.** The Kurokawa absolute-tensor-product line (§9, item 5) proves the *analytic* "square of Spec **Z**" exists at the zeta-function level, with genuine Euler products over pairs of primes. Jointly with this note, the failure is localized precisely: pair-of-primes data is realizable analytically; what is empty is the proposed *classical-geometric host* built from per-prime fibers.

**Taxonomy (barrier zoo IV.10).** This result is banked as `BARRIER-ZOO.md` Group IV, entry **IV.10** ("Tate-curve products carry no correspondence calculus"), with the executable test for future briefs: *for any per-prime-fiber assembly proposal, (i) compute `Hom` between two named fibers by the one-page lattice criterion; (ii) exhibit the diagonal/graph classes the calculus needs on the actual NS group; (iii) check whether any intersection number can carry a `log p` weight without hand-insertion.* It binds all per-prime-fiber substrate designs. Its relations to the neighboring taxonomy: it re-enters **IV.1** at the hand-insertion step (O3: weights inserted into test-family coefficients = "no new data coordinate"); it carries the rider (recorded at IV.10) that the commission's polarized-Frobenius axiom class as printed is a positivity filter, not an Euler-product filter (**I.1/I.2/III.21** cluster); and its process lesson is **V.1** (the Z5-class gate that would have caught this cost one page of lattice algebra and should have run at brief time — it is exactly the one-page computation of §3).

---

## 9. Prior art: citations and distinctions (extended R7(a) gate, verdict novel-with-citations)

The 2026-08-26 gate (`results/c3-r/prior-art-r7a.md`; ~10 search phrasings, three PDFs fetched and
read, five corpus items read on disk, unreachables logged) found no source anticipating either the
construction or the obstruction. **The construction half of that verdict stands; the obstruction
half is WITHDRAWN (2026-08-27).** The rigidity of Theorems 1–3 *is* anticipated — by Winkelmann,
15 April 2002 (item 8 below, and the attribution banner at §3) — and the gate's own sentence,
"elementary lattice arithmetic that could in principle have been noted about ANY pair of complex
tori … and no one has", is formally withdrawn at its source with the reason: the gate searched
prime-indexed phrasing and Winkelmann's is eigenvalue-and-geodesic-length phrasing. What survives
unanticipated is the construction (products of per-prime complex Tate curves as an
arithmetic-surface surrogate — unsurprising, since the `E_p` are two months old with no citing
literature) and the no-go proper, Theorems 4, 5 and 6. **Eight** adjacent traditions must be cited
and distinguished:

1. **Connes–Consani–Marcolli, "The Weil Proof and the Geometry of the Adeles Class Space" [CCM07].** The correspondence-calculus-for-the-explicit-formula tradition — but on the square of the *one* global adele class space, with correspondences built from graphs of the scaling action and analogs of degree/codegree (§7.1 there). Its §10.2 contains the germ of our objects: the tori `T_p ≅ R⁺^×/p^Z` as singular-fiber components in a vanishing-cycles analogy — one-dimensional *real* tori, no complex structure, no products, no intersection theory on products. **Distinction:** one global noncommutative space squared versus a `(p,q)`-family of classical surfaces; the no-go concerns only the latter. (The gate also checked the distinct CCM paper "Fun with F₁," arXiv:0806.2401 — zero Tate/elliptic/product content.)
2. **Connes–Consani, "Geometry of the arithmetic site" [CC16] + the Essay stall quote [CE15 §4.3.2].** The square *exists* in characteristic one, with Frobenius correspondences as congruences — and intersection theory/RR missing a decade on. **Distinction:** complementary result, as in §8: this note shows the classical-complex escape from that stall is empty, and the escape's price (smooth/char-one correspondences) is the classical positivity itself.
3. **The lineage inside the CC orbit [CC16b/CC17 → CC25 → CC26]** *(corrected 2026-08-27; the previous version dated the first appearance to January 2025 and was wrong by nine years and five months)*. First appearance of per-prime elliptic-analogue language: **July 2015** — the periodic orbit `C_p = R^×_+/p^Z`, a real circle of circumference `log p` with a characteristic-one structure sheaf, `J(C_p) ≅ Z/(p−1)Z`, and a real-valued Riemann–Roch [CC16b; CC17], described by its authors as "a variant … of the classical Jacobi description `C^*/q^Z` of an elliptic curve". [CC25] (January 2025) contributes the class-field-theory functor and cites [CC17] for the analogue rather than introducing it. The **complex** Tate curves are June 2026 [CC26], which never raises products, isogenies, or correspondences between primes (grep-confirmed on the on-disk full text). **Distinction:** both the construction and the obstruction of this note are additions to, not extractions from, that lineage — the lineage supplies per-prime fibers, never a cross-prime structure.

8. **Winkelmann's rigidity [Wi04]** *(added 2026-08-27; see the attribution banner at §3 and the dated block at the head)*. J. Winkelmann, *On elliptic curves in `SL₂(C)/Γ`, Schanuel's conjecture and geodesic lengths*, arXiv:math/0204195 (v1, 15 April 2002), Nagoya Math. J. **176** (2004), 159–180. Inside the proof of his Theorem 2 he derives `4π²/(log λ_i log λ_j) ∈ Q` as the necessary condition for isogeny of `C^*/λ_i^Z` and `C^*/λ_j^Z`, divides two such relations to force `log λ_i/log λ_k ∈ Q`, runs the argument on three curves and concludes that each curve in his family has at most one isogenous partner. **That is §§3–4 of this note, transported.** **Distinction:** his context is the geometry of `SL₂(C)/Γ` and hyperbolic geodesic length spectra; he never takes `λ` prime, never writes `Hom`, never computes a rank or an isogeny degree, and raises no Néron–Severi group, no correspondence calculus and no explicit formula. This note adds the prime-indexed explication (§§3–4) and the no-go (§§5–6); it claims no priority over the rigidity. Recording why the earlier gate missed it: it searched prime-indexed phrasing, and his is eigenvalue-and-geodesic-length phrasing.
4. **Banaszak–Uetake [BU1, BU2, BU3].** Independent operator-theoretic axiomatization of a Weil-style intersection calculus (axioms INT1–INT3 on a Hilbert-space operator, modeled on Weil's `C × C`), whose *existence* is equivalent to RH (+ semi-simplicity). **Distinction:** they posit the calculus abstractly and prove existence ⟺ RH; this note kills the one concrete classical-surface instantiation ever proposed from per-prime geometric data. Opposite poles: abstract axioms with RH-equivalent existence versus concrete surfaces with provably empty calculus.
5. **The Kurokawa absolute tensor product line [Ku92-line; Ak09; Ta20].** Kurokawa's 1992 proposal and the proven Euler products *over pairs of primes* for `ζ ⊗ ζ` and Dirichlet-L tensor squares (Koyama–Kurokawa; Akatsuka; Kurokawa–Wakayama; Tanaka) — "the square of Spec **Z**" at the zeta-function level, zeros at sums `ρ₁ + ρ₂`. **Distinction and sharpening:** the pair-indexed *analytic* object exists and factorizes; the proposed *geometric* host from per-prime Tate curves is empty. Jointly the two localize the failure of the square at the geometric hosting step, not at pair-indexed data. (This line is also the published calibration for what a pairwise-product family *would* express if it expressed anything: pair-supported data with summed zeros — not `W(f)`.)
6. **Haran's arithmetical-surface program [Ha91].** The closest non-CC surrogate proposal: `Spec Z ×_{alg} Spec Z` reduces to the diagonal (Haran: "the surface reduces to the diagonal!"), so Haran proposes *defining* intersection numbers of "Frobenius divisors" on the nonexistent surface by analytic means, aiming at a two-dimensional Riemann–Roch. **Distinction:** no per-prime elliptic fibers, no products of classical curves, no obstruction statement; Haran's program postulates the calculus's output, ours tests a concrete candidate host and finds it empty.
7. **Scholze `A_inf`/Fargues–Fontaine adjacency.** Nothing in that school produces cross-prime products of per-prime objects as a correspondence substrate (shtuka legs and `X_S`-families are all single-`p`), and no such no-go is published there. The one genuine contact runs through [CC26] itself: the phase factor `X̃_∞` as a *real analogue* of the Fargues–Fontaine curve — a per-prime-to-archimedean bridge, not a cross-prime one. **Distinction:** disjoint mechanism; cited for completeness of the search record.

**Transcendence background (rider citations; corrected 2026-08-27).** The Gelfond–Schneider theorem (1934) for the **unconditional refutation of (T2)** — the diagonal coincidence factors into a **Q̄**-linear relation between `log p` and `iπ`, squarely inside the classical theorem (§7, Proposition) — together with Barré-Sirieix–Diaz–Gramain–Philibert [BDGP96], whose proof of the Mahler–Manin conjecture gives the same conclusion by a different and stronger route (`j(E_p)` transcendental); Baker's theorem for the general linear-forms background; the four-exponentials conjecture [Sch57; Lan66a, Lan66b; Ram68; Wal04, Conj. 3.7], of which **(T1) is an instance** (not merely an adjacent open problem), with the proven six-exponentials theorem kept out of reach by Theorem 2 itself (§7), and the published state of the art on it in Roy [Roy92] and Diaz [Dia07]; Schanuel's conjecture for the stronger algebraic-independence resolution, and Winkelmann's Proposition 3 [Wi04, §3.2] for the same reduction seventeen years earlier.

**Withdrawn, 2026-08-27.** This section previously read: *"The question (T1) appears to be unrecorded in the literature in this form and is stated here as open; the question (T2) may be equally unrecorded …"*. **That is false and is withdrawn.** ¬(T1) is a displayed, labeled published conjecture — **(C4E faible)**, Diaz [Dia97, p. 231], attributed there to D. Bertrand (Madras, January 1996; [Ber97, §5]) — whose specialization to `α₁ = p, α₂ = q` is exactly (T1), and the same paper carries unconditional partial results this note did not know about (Diaz's Théorème 1 and Propositions 1 and 3(1)). The germ of the question is older still: Alaoglu and Erdős asked in 1944, in print, *"If `p` and `q` are different primes, is it true that `p^x` and `q^x` are both rational only if `x` is an integer?"* [AE44, p. 449], and recorded Siegel's three-prime theorem on their p. 455 — the exact four-versus-six-exponentials split this note rediscovers in §7. The one thing the withdrawal does **not** touch is the mathematics: (T1) is open, the family-level kill does not consume it, and (T2) is refuted unconditionally.

**Novelty statement (rewritten 2026-08-27; the previous version claimed Theorems 1–6 as new and was wrong about Theorems 1–3).** The construction — the `E_p × E_q` assembly proposal, born and killed inside this program — is new. **Theorems 1, 2 and 3 are not: they are Winkelmann's, from 15 April 2002, specialized here to primes** (item 8 above, and the attribution banner at §3). What is claimed as new is: the prime-indexed explication of the rigidity (the group `Hom(E_p, E_q)`, its rank, and the isogeny degree `uv`, none of which is in [Wi04]); **Theorem 4** (Néron–Severi collapse off the matching, with its four consequences — no graph classes, no diagonal, zero action on `H¹`, vacuous Castelnuovo–Severi); **Theorem 5** (the diagonal residue is prime-blind, unconditional via Gelfond–Schneider and via [BDGP96]); **Theorem 6** (the no-go, from three independent obstructions); and the identification of the seed proposal as empty. The eight citation-and-distinguish obligations above are discharged. The obstruction's ingredients are elementary — Birkenhake–Lange-level lattice arithmetic plus unique factorization — which is exactly why the rigidity half was available to be noticed in 2002, and was.

---

## 10. Provenance, verification discipline, and references

**Verification ledger (standing order 5).** Every load-bearing claim in this note is either (i) proved in full above from the on-disk source extraction, (ii) a program-verified computation, or (iii) explicitly tagged open:

| claim | status |
|---|---|
| `E_p ≅ C/(Z ⊕ Z·i·log p/2π)`, rectangular, real; `E_p ≅ C_p × X̃_∞` with `X̃_∞` `p`-independent | read from the on-disk full-text extraction of [CC26] (lines 240–300, 1518–1600); lattice presentation re-derived (Lemma 0) and numerically confirmed (check A) |
| Theorem 1 (iff criterion, `Hom` rank 1, degree `uv`) | proved §3; both directions; converse numerically confirmed (check B); matches adjudication computation (a) and both killers' blind replications. **Priority:** the criterion (necessity) and its "iff" completion are Winkelmann's [Wi04, proof of Thm. 2 and Lemma 7]; the `Hom` group, its rank and the degree `uv` are this note's — see §3's attribution banner |
| `4π²Q` vs `π²Q` bookkeeping | reconciled in Remark 1 (`4π²Q = π²Q` as sets; normalized invariant `y_p y_q ∈ Q`); per adjudication computation (a) |
| Theorems 2, 3 (two-partner rigidity; {2,3,5} kill) | proved §4, unconditional; unique factorization + linear algebra over **Q** only. **Priority: Winkelmann's** [Wi04, proof of Thm. 2, p. 16], with multiplicative independence replaced by unique factorization |
| Theorem 4 (NS decomposition and collapse) | proved §5 from seesaw + Poincaré-bundle universal property + rigidity ([BL] Ch. 2, 5 for the standard inputs; decomposition classical) |
| Theorem 5 (diagonal residue; `p`-blind integer profile) | proved §6; part (1) unconditional via the §7 Proposition (Gelfond–Schneider), and independently via the Mahler–Manin theorem [BDGP96] (`j(E_p)` transcendental ⟹ no CM); kernel counts tabulated (check D) and genuinely verified (referee suite R6) |
| Theorem 6 (no-go O1–O3) | proved §6 from Theorems 1–5 + the structural features (W-i)–(W-iii) of the explicit formula |
| (T1) off-diagonal non-coincidence `log p·log q ∉ 4π²Q` | **OPEN unconditionally**, and **published as a named conjecture**: it is the specialization to `α₁ = p, α₂ = q` of (C4E faible) [Dia97, p. 231], due to D. Bertrand [Ber97, §5]; an instance of the four-exponentials conjecture; settled by Schanuel with full algebraic independence, and by Winkelmann's Conjecture 1 [Wi04, §3.2] via the converse of Theorem 1 (§7). Unneeded for the family-level kill; numerical evidence checks C, E (PSLQ null to `10³⁰`, rational denominators `> 10¹⁰⁰`). *(The earlier "appears to be unrecorded" claim is withdrawn — §9.)* |
| (T2) diagonal non-coincidence `(log p)² ∉ 4π²Q` | **REFUTED unconditionally** — proved, Gelfond–Schneider 1934 (§7, Proposition); hence `End(E_p) = Z` for every prime and Theorem 5(1) carries no exception clause; numerics rows 4–5 of §7 retained as detector controls |
| explicit-formula display in §1.3 | schematic, normalization-hedged; only the tagged structural features (W-i)–(W-iii) are consumed |
| prior-art verdict and the eight distinctions | **partially withdrawn 2026-08-27** — the obstruction half of the verdict is false (Winkelmann 2002; §9 item 8); the construction half stands. `results/c3-r/prior-art-r7a.md` (2026-08-26; fetched PDFs + on-disk corpus + logged unreachables; Akatsuka's CNTP paper characterized via Tanaka's introduction and venue confirmations, full text paywalled — flagged there, nothing load-bearing rests on unread portions) |

Process provenance: the seed kill was constructed independently by two killer agents under the duplicate-killer protocol (identical mathematics, no shared text), re-derived in full by the adjudicator (`results/adjudication-C3.json`, computation (a)), and re-proved from scratch for this note. The commission file (`directions/C3-geometric-substrate.md`) retains the original seed proposal verbatim as the immutable record, with the adjudication and reduced recommission C3-r appended.

**Network conditions at gate time (standing order 1):** direct arxiv.org unreachable (ISP IPv6 issue); all needed PDFs fetched through the GCS arXiv mirror; per-resource unreachables logged in the prior-art report §7.

### References

- **[CC26]** A. Connes, C. Consani, *On the Absolute Geometry of Spec Z and the Fargues–Fontaine curve*, arXiv:2606.06604 (June 2026). **Title note, 2026-08-27 (read before "correcting" this entry):** the clause "and the Fargues–Fontaine curve" is absent from **every** arXiv metadata surface — the abs page's `<h1>`, the `citation_title` meta tag, the API, the PDF's own metadata dictionary — and from zbMATH; it survives only on the typeset title page and in arXiv's HTML rendering of the LaTeX `\title{}`. It is part of the title and must be kept. (This supersedes an earlier note in this program which diagnosed the omission as an API truncation at a TeX macro; the conclusion was right, the mechanism was not.) On disk: corpus u-15b; full-text extraction `sources-extracted/arxiv-2606.06604-absolute-geometry-specZ-fulltext.txt`.
- **[CC25]** A. Connes, C. Consani, *Knots, primes and class field theory*, arXiv:2501.06560 (January 2025). On disk: corpus u-18b. (**Dated correction, 2026-08-27:** this note previously named [CC25] as the first appearance of the per-prime elliptic-curve analogue. It is not — it cites [CC17] for that. Its own contribution is a functor from finite abelian extensions of **Q** to finite covers of `X_Q`, under which the monodromy of the periodic orbit of length `log p` corresponds to the Galois action of Frobenius at `p`. Its full text contains no occurrence of “isogen” or “Tate”.)
- **[CC16]** A. Connes, C. Consani, *Geometry of the arithmetic site*, Adv. Math. **291** (2016), 274–329; doi:10.1016/j.aim.2015.11.045; arXiv:1502.05580. (Cited for the char-one square + Frobenius correspondences; fields completed 2026-08-27.)
- **[CE15]** A. Connes, *An essay on the Riemann Hypothesis*, in: *Open Problems in Mathematics* (J. F. Nash Jr. and M. Th. Rassias, eds.), Springer, Cham, 2016, pp. 225–257; doi:10.1007/978-3-319-32162-2_5; arXiv:1509.05576, §4.3.2. On disk: corpus t-20b (stall quote program-verified; pin-cite by section, since the arXiv and book folios differ by about +224).
- **[CCM07]** A. Connes, C. Consani, M. Marcolli, *The Weil Proof and the Geometry of the Adeles Class Space*, arXiv:math/0703392 (Manin Festschrift, Birkhäuser). Fetched and read at gate time (title verified from the PDF).
- **[BU1]** G. Banaszak, Y. Uetake, *Abstract intersection theory and operators in Hilbert space*, arXiv:0908.2909 (publ. CNTP 5 (2011) per the on-disk filename). On disk: t-43b.
- **[BU2]** G. Banaszak, Y. Uetake, *Standard models of abstract intersection theory…*, arXiv:1210.3526. On disk: t-30b.
- **[BU3]** G. Banaszak, Y. Uetake, *Abstract intersection theory for zeta-functions: geometric aspects*, Funct. Approx. Comment. Math. 64.2 (2021) 251–265. On disk: t-58a. (**Dated correction 2026-08-27:** the title was previously elided to "*…: geometric aspects*", whose antecedent in the preceding bullet is BU2's stem — the wrong one. Verified from page 1 and the p. 265 running head of the on-disk published PDF t-58a, and from Crossref DOI 10.7169/facm/1916.)
- **[Ku92-line]** N. Kurokawa's absolute tensor product proposal (1992) and its proofs: Koyama–Kurokawa (`ζ ⊗ ζ`); H. Akatsuka, *The double Riemann zeta function*, Commun. Number Theory Phys. 3 (2009) 619–653 **[Ak09]**; Kurokawa–Wakayama; history and Dirichlet-L case in H. Tanaka, arXiv:2008.07752 **[Ta20]** (fetched and read at gate time — the line's history is cited through Tanaka's introduction; Akatsuka's full text is paywalled, flagged in the gate report).
- **[Ha91]** S. Haran, *Index theory, potential theory, and the Riemann hypothesis*, in *L-functions and Arithmetic* (Durham, 1989), J. Coates and M. J. Taylor (eds.), London Math. Soc. Lecture Note Ser. 153, Cambridge Univ. Press, Cambridge, 1991, pp. 257–270; doi:10.1017/CBO9780511526053.010; Zbl 0744.11042. (MR1110396 is reported by secondary listings but was not verified against MathSciNet, which is unreachable from this machine; prefer the Zbl number and the DOI.) The passage relied on is p. 259: `Spec Z × Spec Z ≅ Spec Z`, "the surface reduces to the diagonal!"; `⟨f, g⟩ := W(f * g*)` as the analytic intersection number of "Frobenius divisors" on the nonexisting surface; and "a two dimensional Riemann–Roch for Spec(Z) may very well exist!". Quoted verbatim and expanded in the survey K. Thas, *A taste of Weil theory in characteristic one*, in *Absolute Arithmetic and F₁-Geometry*, EMS Press, 2016, pp. 365–386; doi:10.4171/157-1/8; arXiv:1507.06480 (v1, 23 Jul 2015). (Editor and place of publication are uncorroborated by Crossref and are dropped here; the DOI and page range are verified.) **Dated correction, 2026-08-27:** the prior-art gate recorded arXiv:1507.06480 as Haran's own paper and this note inherited that; it is by **Koen Thas** (verified against the arXiv abstract page's `citation_author` metadata, the PDF title page, and the EMS volume contents). The content the gate extracted is Haran's, quoted by Thas from the 1991 chapter above; only the bibliographic pointer was wrong. **On disk (sponsor-fetched 2026-08-27): `fetched-r3/haran1991.pdf`, 14 pp, printed pages 257–270.** Every claim the §9 item-6 distinction makes is now **page-verified against Haran's own text**, not merely against Thas's survey. The three quotations are all on PDF page 3 = printed **p. 259**: “from the point of view of algebraic geometry, spec Z × spec Z = spec Z, i.e., the surface reduces to the diagonal!”; “for functions f, g : R⁺ → R smooth and compactly supported, to be thought of as representing ‘Frobenius divisors’ on the non-existing surface, we can define their intersection number: ⟨f, g⟩ = W(f * g*)”; and “Ergo our main point is: a two dimensional Riemann-Roch for spec Z may very well exist!”. The negative half of the distinction is confirmed by exhaustive search of the full text: zero occurrences of Tate curve, per-prime, isogeny or abelian variety; the only product of classical curves is `C × C` for a **single** curve over a **single** finite field F_p (p. 257, the Frobenius correspondences A_n = {(x, x^{pⁿ})} with A_0 = Diag), not a cross-prime product; and zero occurrences of any obstruction, impossibility or no-go claim — Haran's posture is existence-optimistic (“may very well exist!”). The five occurrences of “elliptic” are all in the bibliography and all denote **elliptic operators** (Atiyah, Bismut, Kasparov, Seeley — index theory), never elliptic curves.
- **[BL]** C. Birkenhake, H. Lange, *Complex Abelian Varieties*, 2nd augmented ed., Grundlehren der mathematischen Wissenschaften **302**, Springer, Berlin, 2004; doi:10.1007/978-3-662-06307-1; Ch. 2 (“Line Bundles on Complex Tori”) and Ch. 5 (“Endomorphisms of Abelian Varieties”). (Citation at chapter level per the adjudicated record; every fact consumed from it is re-proved in §5 so nothing load-bearing rests on a recalled page number.)
- **[We52]** A. Weil's explicit formula (1952); used only through the normalization-hedged structural display of §1.3. Program-internal small-support calibration copy on disk: corpus u-23a (Bombieri 2000).

**Added in the 2026-08-27 citation pass.** Every field below was verified against a primary source
this session (arXiv abstract pages and PDFs, Crossref, zbMATH Open, Numdam, the Comptes Rendus
publisher page, or the on-disk corpus); per-source evidence in
`results/arxiv/citation-verification/`. Items not obtained in full text are marked.

- **[Wi04]** J. Winkelmann, *On elliptic curves in `SL₂(C)/Γ`, Schanuel's conjecture and geodesic
  lengths*, Nagoya Math. J. **176** (2004), 159–180; doi:10.1017/S0027763000009016;
  arXiv:math/0204195 (v1, 15 Apr 2002; v2, 6 Nov 2002; v3, 8 Apr 2003). The author prints his
  given name **Jörg**; arXiv's metadata ASCII-izes it. **Cite the arXiv/zbMATH/title-page form of
  the title**: Crossref and Cambridge Core both render it with a spurious `Γ..`, a publisher-side
  artifact. Pin-cites used here: Lemma 7 (the isogeny ⟺ `dim_Q ker Φ > 0` equivalence); the proof
  of Theorem 2, p. 16 (the `4π²` criterion, the division step, and the one-partner conclusion);
  Conjecture 1, §3.2, p. 13; Proposition 3, §3.2, p. 14 (Conjecture 1 under Schanuel). **The paper
  has six sections; there is no §7.**
- **[Dia97]** G. Diaz, *La conjecture des quatre exponentielles et les conjectures de D. Bertrand
  sur la fonction modulaire*, J. Théor. Nombres Bordeaux **9** (1997), no. 1, 229–245;
  http://www.numdam.org/item?id=JTNB_1997__9_1_229_0. (C4E faible) is displayed on **p. 231**,
  attributed there to D. Bertrand; his Théorème 1 gives (C0) ⟺ (C6), and Propositions 1 and 3(1)
  are unconditional partial results. JTNB volumes of that era carry no DOI; the Numdam item id is
  the stable handle. Local copy:
  `results/arxiv/citation-verification/assets/diaz-1997-jtnb9-quatre-exponentielles-numdam.pdf`.
- **[Ber97]** D. Bertrand, *Theta functions and transcendence*, International Symposium on Number
  Theory (Madras, 1996), Ramanujan J. **1** (1997), no. 4, 339–350; doi:10.1023/A:1009749608672;
  Zbl 0916.11043. *(Paywalled and not read; the bibliographic fields are verified against Crossref
  and zbMATH. The §5 locator is on Diaz's word — [Dia97, p. 231] and its bibliography entry [2] —
  and on the zbMATH review, which is itself written by Diaz and is therefore non-independent. Cite
  it as "Bertrand, Ramanujan J. **1** (1997), §5, as reported by Diaz". Note also that
  "January 1996" is Diaz's prose; the printed conference designation is "International Symposium on
  Number Theory (Madras, 1996)".)*
- **[Sch57]** Th. Schneider, *Einführung in die transzendenten Zahlen*, Grundlehren der
  mathematischen Wissenschaften **81**, Springer-Verlag, Berlin–Göttingen–Heidelberg, 1957,
  150 pp.; Ch. V, end of §4, Problem 1. French translation: *Introduction aux nombres
  transcendants*, trans. P. Eymard, Gauthier-Villars, Paris, 1959, viii+151 pp., p. 139.
  *(Not held. Chapter and problem locator per Waldschmidt [Wal04, §3]; catalog fields from
  zbMATH.)*
- **[Lan66a]** S. Lang, *Nombres transcendants*, Séminaire Bourbaki, 18e année (1965/66),
  exp. no. 305, Feb. 1966, 407–414; http://www.numdam.org/item?id=SB_1964-1966__9__407_0. Local
  copy: `results/arxiv/citation-verification/assets/lang-1966-seminaire-bourbaki-305-nombres-transcendants-numdam.pdf`.
  *(Exposé number, title, date and page range verified from the Numdam item page. Calling this "a
  later explicit formulation" of the four-exponentials conjecture is Waldschmidt's characterization,
  not the page's: on the page itself the statement appears as one sentence of wishing — "On voudrait
  bien réduire d'une unité le nombre 3…" — not as a numbered conjecture.)*
- **[Lan66b]** S. Lang, *Algebraic values of meromorphic functions. II*, Topology **5** (1966),
  363–370; doi:10.1016/0040-9383(66)90028-0. *(Not read; its explicit formulation of the
  four-exponentials conjecture is reported by Waldschmidt, LIL, Ch. 1.)* Waldschmidt's own Lang
  locator is instead the book, S. Lang, *Introduction to Transcendental Numbers*, Addison-Wesley,
  Reading, MA, 1966, Ch. II §1, and *Transcendental numbers and Diophantine approximations*,
  Bull. Amer. Math. Soc. **77** (1971), 635–677, at p. 638.
- **[Ram68]** K. Ramachandra, *Contributions to the theory of transcendental numbers. I, II*,
  Acta Arith. **14** (1968), 65–72 and 73–88. These are **two** papers; the DOI
  doi:10.4064/aa-14-1-65-72 covers **part I only**, and part II's has not been verified, so none is
  attached to it. The four-exponentials conjecture is formulated in **part II, §4**.
- **[Wal04]** M. Waldschmidt, *Open Diophantine Problems*, Mosc. Math. J. **4** (2004), no. 1,
  245–305; doi:10.17323/1609-4514-2004-4-1-245-305; arXiv:math/0312440. Conjecture 3.7 and the
  matrix restatement immediately following it, p. 269. **Do not cite the AWS Lecture 5 notes for
  the weak four-exponentials conjecture**: verified 2026-08-27, their Conjectures 5.34 and 5.35
  are D. Bertrand's conjectures on the modular function `J`, the four-exponentials conjecture
  there is Conjecture 5.11 and the strong form Conjecture 5.8, and the weak form does not appear
  in that document at all.
- **[BDGP96]** K. Barré-Sirieix, G. Diaz, F. Gramain and G. Philibert, *Une preuve de la conjecture
  de Mahler–Manin*, Invent. Math. **124** (1996), no. 1–3, 1–9; doi:10.1007/s002220050044.
  *(Bibliographic fields verified against Crossref and zbMATH. The theorem statement used here —
  for `q` algebraic with `0 < |q| < 1`, `J(q)` is transcendental — was read at one remove, from
  Waldschmidt's Séminaire Bourbaki exposé 824, Astérisque **245** (1997), p. 108, and from the
  zbMATH review, which agree verbatim; Springer is paywalled and the paper's own first page was not
  read.)*
- **[Roy92]** D. Roy, *Matrices whose coefficients are linear forms in logarithms*, J. Number
  Theory **41** (1992), no. 1, 22–47; doi:10.1016/0022-314X(92)90081-Y. *(Not read; content via
  Diaz. Note that Waldschmidt's "[Ro 1992]" in* Open Diophantine Problems *is a different Roy 1992
  paper.)*
- **[Dia07]** G. Diaz, *Produits et quotients de combinaisons linéaires de logarithmes de nombres
  algébriques : conjectures et résultats partiels*, J. Théor. Nombres Bordeaux **19** (2007),
  no. 2, 373–391; doi:10.5802/jtnb.592. Corollaire 1(1) is the instrument that does not reach
  (T1), because it needs `(λ₀, λ₂, λ̄₂)` **Q̄**-linearly free and `λ₂ = log q` is real.
  (Crossref's 2008 date is a deposit date; the cover page says 2007.)
- **[AE44]** L. Alaoglu and P. Erdős, *On highly composite and similar numbers*, Trans. Amer.
  Math. Soc. **56** (1944), 448–469; doi:10.1090/S0002-9947-1944-0011087-2. The two-prime question
  is stated at **p. 449** — *"If `p` and `q` are different primes, is it true that `p^x` and `q^x`
  are both rational only if `x` is an integer?"* — and again at p. 455, where Siegel's three-prime
  result is recorded.
- **[CC16b]** A. Connes and C. Consani, *The scaling site*, C. R. Math. Acad. Sci. Paris **354**
  (2016), no. 1, 1–6; doi:10.1016/j.crma.2015.09.027; arXiv:1507.05818 (v1, 21 Jul 2015).
- **[CC17]** A. Connes and C. Consani, *Geometry of the scaling site*, Selecta Math. (N.S.) **23**
  (2017), no. 3, 1803–1850; doi:10.1007/s00029-017-0313-y; arXiv:1603.03191.
- **[CC19]** A. Connes and C. Consani, *The Riemann–Roch strategy: Complex lift of the Scaling
  Site*, in: *Advances in Noncommutative Geometry* (A. Chamseddine, C. Consani, N. Higson,
  M. Khalkhali, H. Moscovici and G. Yu, eds.), Springer, Cham, **2019**, 53–125;
  doi:10.1007/978-3-030-29597-4_2; arXiv:1805.10501. Its §§6.4–6.6 carry the CC program's own
  moduli of triangular elliptic curves with the equivalence relation generated by isogenies —
  adjacent to the construction here and previously uncited. (CC's own bibliographies date the
  chapter 2020; that is the online-first date.)
- **[CC24a]** A. Connes and C. Consani, *Knots, primes and the adele class space*,
  arXiv:2401.08401 (January 2024). Its §3 constructs `Γ \ (Q_p × Q_q × R)` with
  `Γ = {± p^m q^n}` — a genuine two-prime object inside the CC program, predating the lineage
  this note claimed. **Distinction:** a knot/linking-number analogy, not a correspondence calculus:
  no Néron–Severi group, no intersection pairing on a product of curves, no explicit formula.
- **[Mor25]** M. Morishita, *On a relation between Deninger's foliated dynamical systems and
  Connes–Consani's adelic spaces*, arXiv:2508.15971 (August 2025; revised through 21 Jan 2026);
  to appear in Münster J. Math. *(announced by the author; not independently verified)*. Single
  author. The current bridge between the two traditions this note keeps alive (§8).
- **[RS14]** J. Rosen and A. Shnidman, *Néron–Severi groups of product abelian surfaces*,
  arXiv:1402.2233 (2014); Proposition 2.3. Unpublished preprint as of August 2026; add no journal
  reference. They preface the decomposition "is well-known", so cite as a locator ("see e.g."),
  never as its origin.
- **[Nes96]** Yu. V. Nesterenko, *Modular functions and transcendence questions*, Mat. Sb. **187**
  (1996), no. 9, 65–96; doi:10.4213/sm158; English transl., Sb. Math. **187** (1996), no. 9,
  1319–1348; doi:10.1070/SM1996v187n09ABEH000158. With Yu. V. Nesterenko and P. Philippon (eds.),
  *Introduction to Algebraic Independence Theory*, Lecture Notes in Math. **1752**, Springer,
  Berlin, 2001; doi:10.1007/b76882.
- **[Mil16]** J. S. Milne, *The Riemann hypothesis over finite fields: from Weil to the present
  day*, in: *The Legacy of Bernhard Riemann After One Hundred and Fifty Years*, Vol. II (L. Ji,
  F. Oort and S.-T. Yau, eds.), Adv. Lect. Math. (ALM) **35**, part 2, International Press and
  Higher Education Press, 2016, 487–565; reprinted in ICCM Notices **4** (2016), no. 2, 14–52;
  doi:10.4310/ICCM.2016.v4.n2.a4; arXiv:1509.00797. Cited in §5(d) as a published locus for the
  classical Castelnuovo–Severi inequality (his Theorem 1.5, §1), so a referee need not follow a
  program-internal file path.

- **Program files:** `directions/C3-geometric-substrate.md` (commission + adjudication + C3-r); `results/adjudication-C3.json`; `results/verdicts-c3d1.json`; `results/c3-r/prior-art-r7a.md`; `results/c3-r/m1-noncircularity.md`; `BARRIER-ZOO.md` (entry IV.10); `results/c3-r/seed-no-go-checks.{py,json}` (this note's numerics).

---

## 11. Referee pass + fatal repair (dated record, 2026-08-26)

**Referee verdict (`results/c3-r/referee-seed-no-go.md`, 2026-08-26, independent referee): FAIL AS-WRITTEN → repaired in this revision.** All six theorems, both sharpenings, every quotation and file pointer, and the full numerics were verified by the referee (bit-for-bit rerun of `seed-no-go-checks.py`; an independent from-scratch suite `referee_seed_checks.{py,json}` with rigorous interval-arithmetic continued fractions and instrument-independent constants; WolframAlpha as a third instrument). One fatal-class defect was found, and it cut in the note's own disfavor — an *underclaim*:

- **The fatal (F1).** The original §7 claimed that (T1)/(T2) are "quadratic relations … outside the reach of any proven linear-forms result," that "no standard conjecture short of Schanuel-type algebraic independence settles them," and — bolded — that "no proven theorem currently excludes either coincidence." All three claims were false. (T2), the CM coincidence `(log p)² ∈ 4π²Q`, has been excluded **unconditionally** since 1934: it factors into a **Q̄**-linear relation between `log p` and `iπ` with an algebraic imaginary coefficient, which the Gelfond–Schneider theorem forbids (§7, Proposition — re-derived independently by referee and repair editor). And (T1) is settled by the four-exponentials **conjecture**, far short of Schanuel — though it does remain open unconditionally, the proven six-exponentials theorem being blocked from reaching it by this note's own Theorem 2.
- **The applied repair (this revision, per the referee's §2 draft).** §7 rewritten around the Gelfond–Schneider Proposition (one-paragraph proof, two routes) and (T1)'s corrected status ladder; Theorem 5(1) made unconditional (exception clause deleted, proof closed off, part 3 de-hedged); the §0 summary (items 1 and 5 and the closing rider line); Theorem 6(O1)'s parenthetical scoped to (T1); §9's transcendence-background paragraph; the §10 ledger row split into (T1) OPEN / (T2) REFUTED; §7's numerics rows 4–5 relabeled from evidence-on-an-open-question to detector controls confirming a theorem.
- **The strengthening consequence.** `End(E_p) = Z` for **every** prime, unconditionally — the diagonal residue (Theorem 5) and its prime-blindness (Theorem 6, O3) now carry no hedge at all, and the note has one honest open rider instead of two, with that rider precisely located (an instance of the four-exponentials conjecture; Schanuel gives more; unneeded by every theorem here).
- **Nine mechanical repairs, referee-applied before this revision** (report §5, items 1–9; already incorporated in the text above): §1.1 "only mechanism" → "classical template"; the "[W]hat is missing" quotation capitalization; "eight years" → "a decade" (§1.1 and §9); the [CC26] §4.1.2 → §4.3 theorem pointer; Remark 3's cross-tower claim made precise; the §8 N2 bullet reordered and scoped; the check-D wording softened to "tabulates" (the genuine kernel verification is the referee suite's R6); the O3 citation widened to "[CC26] Thm 5 and §4.3."
- **Residual open content after repair: exactly one item.** (T1) — `log p·log q ∉ 4π²Q` for distinct primes — open unconditionally, settled under the four-exponentials conjecture, consumed by nothing in this note.

Downstream dated amendments executed with this repair: `BARRIER-ZOO.md` entry IV.10 (dated brackets on its two hedge lines) and `directions/C3-geometric-substrate.md` (dated addenda to the Session-7 work-log seed-note line and the Current frontier line). `results/adjudication-C3.json` is immutable and untouched; its computation (a) concerns Theorem 1/(T1) and is unaffected by the (T2) correction.

---

*End of note. Referee pass completed and the one fatal repaired 2026-08-26 (§11); circulation-ready. U.S. English throughout. All file paths relative to the program root `anthropic/rh-program/`.*
