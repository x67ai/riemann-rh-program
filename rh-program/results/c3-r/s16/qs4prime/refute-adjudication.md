# BINDING ADJUDICATION OF THE ADVERSARIAL PASS — Q-S4′, targets T1–T6 (A-II, A-III, A-IV, vacuity, clause (iv), N10)

**Program:** RH research program, direction C3-r. **Session:** 16. **Date:** 2026-09-06 (IST).
**Binding adjudicator:** Fable 5.1 — the model that did NOT write the derivations under test (they are Opus 5's,
`adjudication.md` §2 A-II, A-III, A-IV, the vacuity ruling inside S16-3, N10). **Inputs read in full:** `refute-F.md`
(refuter F, Fable 5.1), `refute-O.md` (refuter O, Opus 5), `adjudication.md` §0, §1 A1–A8, §2 (A-I to A-IV, B1, the
table), §3, §5, §6, §7, §8; ledger `m2c-feasibility-ledger.md` §15–§16 with the orchestrator's enactment note.
**Standing orders in force:** 5 (re-derive, never weigh testimony) and 7 (two models check one; a derivation STANDS
only if I can write its proof from the printed hypotheses). Every judgment below is mine and is labeled **[ADJ-B]**.
Every source anchor names the file on disk and the printed page I read this session (§8). U.S. English.

**Method.** For every target where F and O disagree (T2), and for every step of every target where either refuter
says FALLS or supplies a new theorem (F's Theorem F-1 and B1′; O's Theorems O-1 to O-6), I re-derived the mathematics
myself from the printed hypotheses before ruling. Where a refuter's theorem is correct I say so and it thereby becomes
dual-checked (refuter + me); where a refuter's theorem is correct but describes a class that another correct theorem
empties, I say that too — that is the decisive situation in this pass.

---

## §0. BINDING RULINGS

| Target | Derivation under test | **Binding verdict [ADJ-B]** | Binding statement (the exact narrowed form, or the gap) |
|---|---|---|---|
| **T1 = A-II** | Every compact preserved leaf of an S4′ object has χ = 0 and no fixed point; clause (iii)'s leaf is non-compact and (Rem. 7 + Candel) conformal to C, χ = +1 | **STANDS-NARROWED** | The fixed-point source property is an ADDED hypothesis (printed chain (31) ⇒ Rem. 4 ⇒ Rem. 5 ⇒ Fact, [Den05] pp. 31–33; Leichtnam prints it as a separate axiom (13)/(12)). S4′ must be amended by **clause (0) = (0-fix) + (0-coh)** (§1.1). Under (0-fix): A-II steps 1–5 STAND as written (each re-derived, §1.2–1.4) — every compact preserved leaf is a torus without fixed points, clause (iii)'s leaf is non-compact. Under (0-coh): stronger and simpler — **no compact preserved leaf exists at all and every preserved leaf is a hyperbolic Riemann surface** (Theorem A, §1.5). **"Conformal to C, χ = +1" FALLS**: it rests on an expectation ([Den05] p. 33 Rem. 7, "we would expect"), is circular with A-III, names no particular leaf, and is contradicted under (0-coh). If clause (iii)'s leaf has χ = +1 it is the **hyperbolic disk**, and the flow along it is **not conformal** for any t ≠ 0 (Corollary A.1). |
| **T2 = A-III** | A positive holonomy-invariant transverse measure NECESSARILY EXISTS (Candel p. 490) | **FALLS** | Candel's theorem applies verbatim to S4′ objects (§2.1), but its use needs a non-hyperbolic leaf, supplied only by T1's fallen tail. **The disagreement (F: FALLS; O: STANDS-NARROWED via Theorem O-1) is decided for F.** O's rescue A-III′ is a correct theorem in the class "(0)(b) leafwise-biholomorphic + a fixed point with \|dφ^t\| ≠ 1 + compact", but the measure it produces is supported in the non-transverse set N, hence flow-invariant (Theorem A(A)), which forces α = 0 in both senses of α; that class is disjoint from every α = 1 clause. Under the clause the program must carry, the intended witness (a euclidean preserved leaf) is impossible and **every invariant transverse measure gives N measure zero**. Existence stays an axiom (Leichtnam 5]). |
| **T3 = A-IV** | Closed leaf ⇒ compact; N closed and saturated, all its leaves preserved; the archimedean part is a compact saturated lamination, never one leaf, never finitely many compact ones; (α) ALKL never applies; (β) N1 vacuous; (γ) Leichtnam 2] inconsistent with compactness | **STANDS-NARROWED** | (a) TRUE, proof supplied (both refuters; re-derived §3.1). (b) TRUE for **N := union of the preserved leaves** (proof §3.2); the adjudicator's tangency definition {Y_φ ∈ TF} is unavailable on a foliated space and, for a merely continuous transverse flow, O's counterexample h^t(y) = (y^{1/3}+t)³ is valid. Structural conclusion STANDS **for S4′ + clause (0)**; under (0-coh) sharpened: N contains no compact leaf, all its leaves are hyperbolic, and N carries no invariant transverse measure. (α) STANDS (transverse simplicity is a hypothesis; ALKL §4.1.2 p. 100: "Then M⁰ is a finite union of compact leaves because every fixed point of φ̄ is isolated", read). (β) STANDS but is superseded by **B1′** (F; re-derived §3.4): on a closed 3-manifold the length-group kill extends to every N that is a finite union of finite-type leaves. (γ) RESTATED: "inconsistent with compactness of S_K, which Leichtnam does not print in 2008 §5.1 or 2013 §4.1 (verified by full-text search); his 2007 S_Q is declared a compactification (r3s-21 p. 2)". |
| **T4 = vacuity** | No S4′ object has N = finite union of compact leaves; the KMNT/ALKL kill does not bear; the closed-3-manifold case is OPEN | **STANDS-NARROWED** | Binding form (§4): *For S4′ objects carrying clause (0), N is never a finite union of compact leaves (nor of finite-type leaves, B1′), so N1/B1 does not bear. On a closed 3-manifold the case is OPEN only in the class where rank_Z H₁(M ∖ N) = ∞ and N is a measure-free lamination of hyperbolic preserved leaves containing an exceptional minimal set (Theorem O-5 as corrected, §4). Deninger's own printed manifold class ([x-06] p. 6, fixed points in finitely many compact leaves), KMNT's FDS³ and ALKL's transversely simple class are all excluded.* Without clause (0) the vacuity sentence is not derivable. |
| **T5 = clause (iv)** | (iv) must read: the necessarily-existing holonomy-invariant transverse measure is scaled by the flow with modulus e^{−t}; delete the ALKL justification | **STANDS-NARROWED** | "Necessarily exists" FALLS (T2). "Modulus exactly e^{−t}" STANDS under (0-coh) for any flow eigen-measure, automatic when H̄²_F ≅ R (Leichtnam 4]); if any invariant transverse measure exists at all, an e^{−t}-eigen-measure exists (O's Theorem O-6, Markov–Kakutani, re-derived with a sign corrected, §5.3). Corollary: µ(N) = 0 for every invariant transverse measure. "Delete the ALKL justification": **replace, do not delete** — ALKL's theorem does not apply, but the reason for the clause (Deninger's χ_Co(F,µ)δ₀ term, [Den05] (24) p. 23 and Rem. 6 p. 33; Leichtnam 5]'s L² structure on H̄¹_F) survives. Exact text in §5.5. |
| **T6 = N10** | Print forces α = 0 on a closed 3-manifold only under everywhere-transversality; with preserved leaves the manifold question is open | **STANDS-NARROWED** | The reading is right ([Den05] Cor. 5.5 p. 23 hypothesis "everywhere transversal to F", Rem. 2 p. 24 "the conditions of the corollary force α = 0"; [x-06] p. 8 α = 0 sentence after "we assumed that φ^t had no fixed points" — both read). The ruling over-reaches: **α = 0 is also forced by any compact preserved leaf** (global: area; cohomological: the Dirac measure of the leaf is flow-invariant, Theorem A(A)), so the whole KMNT/ALKL/[x-06] p. 6 class has α = 0, and [x-06] p. 8's escape is the solenoid, not fixed points ("α = 1 can be achieved if for X we allow the local structure (totally disconnected) × (3-dimensional ball)", p. 8–9, read). Corrected: *the manifold question for α = 1 is open exactly for foliated flows with a preserved leaf and no compact preserved leaf; under Deninger's global (31) with a fixed point it is closed negatively (Theorem A(D)).* |

### The two conflicts between the refuters, decided

**Conflict 1 — T2 (F: FALLS; O: STANDS-NARROWED).** Decided for F, by a theorem I re-derived in full (Theorem A,
§1.5, = F's Theorem F-1). O's Theorem O-1 is correct: if the flow acts biholomorphically on the leaf L of a fixed point
at which |dφ^t| ≠ 1, then L is conformally C. O's A-III′ is then correct: Candel puts a positive invariant transverse
measure µ in L̄. But L̄ lies in the non-transverse set N, and **any invariant transverse measure supported in N is
flow-invariant** (Theorem A(A)); pairing it with the area class gives e^{αt} = 1 in the cohomological sense, and
pairing it with leafwise area gives α = 0 in the global sense. So the class in which O's rescue works is the α = 0
class. It is disjoint from every class the program can use. Under the clause the program must carry, existence of
the measure is not derived and the witness is excluded. **T2 FALLS.**

**Conflict 2 — which clause (0) to add (O: the full (31); F: (0-fix) + (0-coh), explicitly not (31)).** Decided for
F. Theorem A(D), re-derived: **on a compact foliated space, Deninger's (31) along the leaf of a fixed point, together
with the α = 1 clause in either form, is inconsistent** (Schwarz–Pick makes the leaf C; Candel puts a measure in its
closure; that measure is flow-invariant; α = 1 forbids it). O's frontier paragraph ("for S4′ objects carrying clause
(0) … the leaf of any fixed point is conformally the plane C") therefore describes an empty class. O's Theorems O-1,
O-2, O-3, O-5, O-6 are each correct under their stated hypotheses and are used below; O's recommended clause (0) is
not adopted, and neither is his (0)(b).

**The theorem that fixes the frontier (F-1, now dual-checked — F derived it, I re-derived it; §1.5).** Under the α = 1
clause in Deninger's own cohomological form ([Den05] p. 27: "the flow φ^{t*} would act by multiplication with e^t on
the one-dimensional space H̄²_F(X)" = Leichtnam 4] (15)), a compact S4′-type object has: no compact preserved leaf;
no euclidean preserved leaf; every preserved leaf hyperbolic; a non-transverse set N of invariant-transverse-measure
zero; and a flow that is **not conformal** along the archimedean leaf for any t ≠ 0. The adjudication's corridor
("N contains a leaf conformal to C, χ = +1, carrying the measure") is the one configuration the α = 1 clause forbids.

---

## §1. T1 = A-II — STANDS-NARROWED

### 1.1 (a) The source property is an added hypothesis; the clause the program must add

**What is printed, read at the page.** [Den05] (`x-20`) p. 21, (20): "for some constant α and all x ∈ X and t ∈ R we
have: g(T_xφ^t(v), T_xφ^t(w)) = e^{αt}g(v, w) for all v, w ∈ T_xF" — a global axiom on the metric. p. 27, (31) is (20)
with α = 1, introduced by: "we must have α = 1. This means that the flow φ^{t*} would act by multiplication with e^t on
the one-dimensional space H̄²_F(X). As explained before this would be the case if φ^t were conformal on TF with factor
e^t: (31)". p. 31, Remark 7.6(4): "We will see below that in our new context metrics g on TF can exist for which the
flow has the conformal behaviour (31). **Assuming we are in such a situation** and that F is 2-dimensional, we have:
|det(T_xφ^{kl(γ)}|T_xF)| = e^{kl(γ)} … and |det(T_xφ^t|T_xF)| = e^t for a fixed point x. In the latter case, we even
have by continuity: det(T_xφ^t|T_xF) = e^t, the determinant being positive for t = 0." p. 32, Remark 5: "**In the
setting of the preceeding remark** the automorphisms … e^{−t/2}T_xφ^t of T_xF for a fixed point x are orthogonal
automorphisms." p. 33, the Fact: "**In the situation of the preceeding remark** … For fixed points, ε_x = 1 is automatic
and we have: T_xφ^t = e^{t/2}O_t for O_t ∈ SO(T_xF)." So in Deninger the fixed-point form is a one-line corollary of
the global (31) and has no other source. Leichtnam 2013 (`r3s-20` §4.1, read) prints it as a separate axiom 3] a) (13)
beside 3] b) (14) (= S4′ clause (ii)) and 4] (15); Leichtnam 2008 (author copy §5.1, read) prints only the fixed-point
form (12) and no closed-orbit form at all. **[ADJ-B] Both refuters are right: (ii∞) does not follow from (i)–(iv).**

**Counter-configuration (F's, verified).** A compact preserved leaf L ≅ S² on which φ^t|L is the flow of z ↦ e^{t/2}z on
Ĉ (a hyperbolic source at 0, a hyperbolic sink at ∞, no closed orbits) violates nothing in (i)–(iv): (i) forbids only
closed orbits inside leaves (§1.3); (ii) speaks of the γ_p, which are off L; (iii) is satisfied by L (χ = 2) if L lies
in the accumulation set; (iv) says nothing about L. A-II's step (2) — every zero is a source — is where the extra
hypothesis enters. (No object-level counterexample can exist while no S4′ object exists; the standard is whether the
derivation closes from the printed hypotheses, and it does not.)

**What the explicit formula actually forces at a fixed point [ADJ-B — a correction to both refuters' phrasing].**
[Den05] p. 32, read: the fixed-point term is W_x|_{R>0} = ε_x|1 − e^{κ_x t}|^{−1}, W_x|_{R<0} = ε_x e^t|1 − e^{κ_x|t|}|^{−1},
and "This fits perfectly with the explicit formula (6) if all ε_{γ_p}(k) = 1 and ε_{x_p} = 1." So the archimedean term
needs TWO things at x: det(T_xφ^t|T_xF) = e^t (the e^t on R<0) and ε_x = +1 for all t ≠ 0. Write T_xφ^t|T_xF = exp(tB).
det = e^{t·tr B}, so tr B = 1. ε_x = sign det(1 − e^{tB}). If B has real eigenvalues λ, µ with λ + µ = 1 and λ > 0 > µ
(O's saddle diag(2, −1)), then for t > 0, (1 − e^{λt})(1 − e^{µt}) < 0, so ε_x = −1: **the saddle is excluded by the
sign, not admitted** — O's sentence "the archimedean term compels only det = e^t, which a saddle satisfies" is wrong
by the ε_x half of Deninger's own requirement. If λ, µ are real of the same sign with sum 1, both are positive. If
λ, µ = a ± ib with 2a = 1, then a = 1/2 > 0 and det(1 − e^{tB}) = |1 − e^{ta}e^{itb}|² > 0. **So det = e^t and ε_x = +1
together force a source (both real parts positive), which is all A-II uses; they do not force the SO(2) form** (B =
diag(1/4, 3/4) is a non-conformal source with tr B = 1 and ε_x = +1). F's remark that "A-II needs only both real parts
positive" is right; F's parenthetical that ε_x = +1 alone admits a sink is also right (for λ, µ < 0 the product is
positive), and it is the determinant that removes the sink.

**Clause (0) to be adopted [ADJ-B, binding].**
- **(0-fix)** — Leichtnam (13) = Deninger's Fact: the flow has a fixed point x_∞ (one per archimedean place) lying in
  clause (iii)'s leaf, and at every fixed point e^{−t/2}T_xφ^t|T_xF ∈ SO(T_xF). (The weaker "det = e^t and ε_x = +1"
  suffices for A-II; the printed clause is kept.)
- **(0-coh)** — Deninger's definition of α = 1 ([Den05] p. 27) = Leichtnam 4] (15): H̄²_F(X) ≅ R·[λ_g] and
  φ^{t*}[λ_g] = e^t[λ_g], where g is the leafwise metric conformal to the leafwise complex structure (Leichtnam's
  "leafwise kaehler metric λ_g associated to g").
- **NOT (0-glob) = (31)**, and **NOT** O's (0)(b) "each φ^t acts on each leaf by a biholomorphism": with a fixed point on
  a compact space, either is inconsistent with (0-coh) (Theorem A(D), Corollary A.1, §1.5). Leichtnam already made
  this substitution in 2007 on Deninger's advice (`r3s-21` p. 11, read: "Deninger pointed out to us that the condition
  (4) (φ^t)^*g = e^t g was probably too strong for being generalized. That is why … we shall replace it by
  (φ^t)^*[λ_g] = e^t[λ_g]"), and 2013 Comment 6 (read) repeats the caution. Theorem A(D) turns "too strong" into
  "inconsistent".
- **Why the program must add it anyway.** The N p^k coefficients for k ≤ −1 come from |det(T_xφ^{kl(γ)}|T_xF)| =
  e^{kl(γ)} at closed orbits ([Den05] p. 31–32) — that is clause (ii); the archimedean term needs det = e^t and
  ε_x = +1 at the fixed point (above) — that is (0-fix) or its source form; and α = 1 itself is by definition the
  e^t-action on H̄²_F ([Den05] p. 27) — that is (0-coh). S4′ as posed carries none of the last two.

### 1.2 (b) Isolation of fixed points

Under (0-fix): t ↦ O_t = e^{−t/2}T_xφ^t|T_xF is a continuous one-parameter group in SO(2), so O_t = R(θt) and
T_xφ^t|T_xF = exp(t(½I + θJ)); the leafwise linearization of Y_φ at x has eigenvalues ½ ± iθ, both of real part ½:
x is a hyperbolic source of the C¹ leafwise flow (the flow is smooth along leaves, [Den05] 7.3 p. 30, read), hence
isolated in its leaf, with Poincaré–Hopf index sign det(½I + θJ) = +1. On a compact leaf isolated zeros are finitely
many. Under the source form (det = e^t, ε_x = +1) the same holds. **Without either, nothing forces isolation**: a leaf
fixed pointwise (φ^t|L = id) is a preserved leaf of any genus, and ALKL arrange exactly that ("up to leafwise
homotopies, we can assume φ^t = id on M⁰", memoir §1.3.1 p. 2, read). Note that a fixed point lies only in a
preserved leaf ([x-18] p. 4 Dictionary 4, read: "the leaf of F containing a fixed point is φ-invariant"). **(b) holds
under (0-fix).**

### 1.3 (c) Clause (ii) forces transversality; Poincaré–Bendixson on S²

**Transversality [ADJ-B, written out].** Let N be the union of the preserved leaves (§3.2). Suppose a closed orbit c
of φ, of least period ℓ, lies in a leaf L (i.e. c ⊂ N). The restriction φ^t|L is a smooth flow on the surface L whose
generator Y_φ|L is a vector field on L, nonzero along c. For x ∈ c, T_xφ^ℓ|T_xF = T_x(φ^ℓ|L) maps Y_φ(x) to
Y_φ(φ^ℓ x) = Y_φ(x): eigenvalue 1. By clause (i) c = γ_p for some p, ℓ = log p, and by clause (ii)
T_xφ^{log p}|T_xF = p^{1/2}·O with O orthogonal, all of whose eigenvalues have modulus p^{1/2} > 1. Contradiction. So
γ_p ∩ N = ∅ for every p, and every closed orbit of φ is transverse to F. This uses clause (i) in its "exactly" form;
Leichtnam's 2] ("a unique primitive closed orbit γ_P" per prime) does not exclude further closed orbits inside leaves,
so A-II is a theorem about S4′, not about Leichtnam's list. **Holds.**

**Poincaré–Bendixson [ADJ-B, written out].** Let L ≅ S² be a compact preserved leaf whose only equilibria are two
hyperbolic sources p₁, p₂. Take y ∈ L ∖ {p₁, p₂}. ω(y) is nonempty, compact, connected and invariant. A hyperbolic
source p is not in ω(y): choose a quadratic form Q > 0 near p with dQ(Y_φ) ≥ cQ, c > 0, on U = {Q < r}; the backward
flow preserves U and decreases Q exponentially, so if φ^{t_n}(y) ∈ U with t_n → ∞ then y ∈ U and Q(y) ≤ e^{−ct_n}r → 0,
i.e. y = p. Hence cl(orbit⁺(y)) = orbit⁺(y) ∪ ω(y) misses p₁ and is a compact subset of S² ∖ {p₁} ≅ R² on which the
flow is C¹; by the planar Poincaré–Bendixson theorem an ω-limit set that is compact, nonempty and free of equilibria is
a periodic orbit c ⊂ L. Then c is a closed orbit of φ inside a leaf, contradicting the paragraph above. **Holds.**

### 1.4 (d) Orientability and the classification

A leaf carries the leafwise complex structure, hence an orientation; a compact leaf is a closed orientable surface,
χ = 2 − 2g. Under (0-fix), Poincaré–Hopf for Y_φ|L with finitely many zeros all of index +1 gives χ(L) = #(Fix ∩ L) ≥ 0,
so g ∈ {0, 1}: a torus with no fixed point, or S² with exactly two sources — excluded by §1.3. **A-II steps 1–5 STAND
under (0-fix).** Under (0-coh) the conclusion is immediate and stronger (§1.5, Theorem A(C1)).

### 1.5 (e) Parabolicity — ASSUMED from an expectation, and FALSE under the α = 1 clause

**Where the adjudicator excludes the disk.** Only in A-II(c), through [Den05] p. 33 Remark 7 and Candel Theorem 4.3.
p. 33–34, read: "**If there does exist** a foliated dynamical system attached to spec o_K with the properties dictated
by our considerations **we would expect** in particular that for a preferred transverse measure µ we have χ_Co(F, µ) =
−log|d_{K/Q}| … since H̄²(X, F) must be one-dimensional, it follows that χ_Co(F, ν) < 0 for all non-trivial transverse
measures ν. Hence by a result of Candel [9] there is a Riemannian metric on TF, such that every F-leaf has constant
curvature −1 … In the unramified case, |d_{K/Q}| = 1 we must have χ_Co(F, ν) = 0 for all transverse measures by the
above argument. Hence there is an F-leaf which is either a plane, a torus or a cylinder c.f. [9]." Three defects, each
fatal on its own, both refuters found them and I confirm each at the page: (1) it is an expectation and it presupposes
a nonzero transverse measure — the very thing A-III then derives from the plane leaf (circular); (2) "there is an
F-leaf" — nothing identifies it with the preserved leaf of clause (iii); (3) for every K ≠ Q the same remark predicts
that every leaf is hyperbolic, while S16-4 declares "conformal to C … uniform in the number field". And the Euler
characteristic cannot separate C from the disk (both χ = +1).

**What is true under the clause the program must add.**

> **Theorem A [ADJ-B; re-derivation of F's Theorem F-1, now dual-checked].** Let X be a compact Riemann surface
> lamination (Candel §1.1 p. 491, read: separable locally compact metrizable, charts D_i × T_i, transition maps
> leafwise smooth with derivatives continuous in all variables; compact; leaves oriented by the complex structure),
> g a continuous leafwise metric in the conformal class, φ a foliated flow (a continuous R-action by homeomorphisms
> mapping leaves to leaves, smooth along leaves — [Den05] 7.3), N the union of the preserved leaves (closed,
> saturated, flow-invariant: §3.2).
>
> **(A) Every positive holonomy-invariant transverse measure µ with µ concentrated on N is flow-invariant, φ^t_*µ = µ.**
> *Proof.* Fix t and a chart transversal T. Let x ∈ T ∩ N. The path s ↦ φ^s(x), s ∈ [0, t], lies in L_x. Subdivide
> 0 = s₀ < … < s_k = t so that φ^{[s_i, s_{i+1}]}(x) ⊂ U_i for charts U_i; by uniform continuity of the flow on the
> compact [0, t] × X there is a neighborhood V_x of x in T such that φ^{[s_i, s_{i+1}]}(y) ⊂ U_i for all y ∈ V_x. For
> y ∈ V_x ∩ N the path lies in L_y; its U_i-transverse coordinate on [s_i, s_{i+1}] is a continuous function of s with
> values in the countable set L_y ∩ T_i (a leaf is a countable union of plaques, §3.1 Step 0), hence constant. So on
> each [s_i, s_{i+1}] the path stays in one plaque of L_y, and at each s_i it passes from the U_{i−1}-plaque to the
> U_i-plaque through the point φ^{s_i}(y), which is close to φ^{s_i}(x); the U_i-transverse coordinate of φ^{s_i}(y) is
> therefore τ_{i−1,i}(U_{i−1}-coordinate), τ_{i−1,i} the transverse transition germ at φ^{s_i}(x). Composing, the
> U_k-transverse coordinate of φ^t(y) equals h_x(y), where h_x = τ_{k−1,k} ∘ … ∘ τ_{0,1} is the holonomy map of the
> plaque chain along φ^{[0,t]}(x) — a homeomorphism from V_x (shrunk) onto an open subset of T_k. Hence for Borel
> B ⊂ V_x the plaque-projection to T_k of φ^t(B ∩ N) is h_x(B ∩ N), and µ(h_x(B ∩ N)) = µ(B ∩ N) by holonomy invariance.
> Since µ and φ^t_*µ are both concentrated on N (N is flow-invariant), and N ∩ T is covered by countably many V_x,
> φ^t_*µ = µ on every transversal. ∎
>
> **(B) Under (0-coh) [φ^{t*}[λ_g] = e^t[λ_g] in H̄²_F(X)] no nonzero such µ exists.** *Proof.* The Ruelle–Sullivan
> current C_µ, ⟨C_µ, ω⟩ = ∫_X ω dµ (plaque integrals against µ), is continuous on A²_F(X) and vanishes on d_F A¹_F(X)
> (leafwise Stokes plus holonomy invariance), hence on its closure, so it is a functional on H̄²_F(X). By (0-coh),
> ⟨C_µ, φ^{t*}λ_g⟩ = e^t⟨C_µ, λ_g⟩. By change of variables under the foliated homeomorphism φ^t, ⟨C_µ, φ^{t*}λ_g⟩ =
> ⟨C_{φ^t_*µ}, λ_g⟩ = ⟨C_µ, λ_g⟩ by (A). So (e^t − 1)m = 0 with m = ⟨C_µ, λ_g⟩ = total g-area mass of vol_g ⊗ µ, and
> 0 < m < ∞ (X compact, finitely many charts, g continuous, µ ≠ 0 finite on transversals). Contradiction. ∎
> Under (0-glob) the same follows without cohomology: φ^t_*(vol_g ⊗ µ) = e^{−t}(vol_g ⊗ µ) by the leafwise Jacobian
> e^t and (A), so the finite total mass satisfies m = e^{−t}m.
>
> **(C) Consequences for N under (0-coh).** (C1) **N contains no compact leaf**: for a compact leaf T ⊂ N the counting
> measure on T ∩ (transversals) is holonomy-invariant, finite (T compact ⇒ proper ⇒ finite intersections, §3.1),
> and concentrated on N — excluded by (B). (C2) **N contains no euclidean leaf**: if L ⊂ N were conformally C, apply
> Candel's p. 490 theorem to the compact sub-lamination L̄ ⊂ N: since L is not hyperbolic, g|L̄ is not conformal to a
> curvature −1 metric, so L̄ carries a positive invariant transverse measure µ ≠ 0 (Candel Thm. 4.3 p. 498, read,
> says more: supp µ ⊂ L̄ and χ = 0); extended by zero it is a holonomy-invariant transverse measure of X concentrated
> on N — excluded by (B). (C3) **Every preserved leaf is a hyperbolic Riemann surface**: N is a closed saturated set,
> hence a compact Riemann surface lamination; an invariant transverse measure of N extends by zero to one of X
> concentrated on N (holonomy of X preserves N and restricts to holonomy of N), so by (B) N has none, and Candel
> Cor. 4.2 (p. 497, read: "If M is a compact Riemann surface lamination with no invariant transverse measure, then M
> has a conformal metric with curvature −1 on each leaf") applies. (C4) **Every invariant transverse measure µ of X
> gives N measure zero**: µ|_N (restriction to N ∩ T on each transversal) is again holonomy-invariant (N saturated),
> concentrated on N, hence zero by (B). (C5) In particular clause (iii)'s leaf is non-compact and hyperbolic; if it
> has χ = +1 it is the hyperbolic disk.
>
> **(D) The globally conformal case is inconsistent.** Suppose, in addition to (0-coh) or (0-glob), that (31) holds
> along the leaf L of a fixed point x_∞: g(T_xφ^t v, T_xφ^t w) = e^t g(v, w) for x ∈ L. Then T_xφ^t|T_xL is a similarity
> with factor e^{t/2}, so φ^t|L is conformal; det(T_xφ^t|T_xL) is continuous and nonvanishing on the connected L × R
> and equals 1 at t = 0, so φ^t|L is orientation-preserving, hence holomorphic: {φ^t|L} is a one-parameter group in
> Aut(L) fixing x_∞ with |(φ^t)′(x_∞)| = e^{t/2} (the modulus of the complex derivative at a fixed point equals the
> g-operator norm since g is conformal). *L is not hyperbolic*: lift φ^t|L to the universal cover D fixing a lift x̃
> of x_∞; the lift is an automorphism of D fixing x̃ (its inverse is the lift of φ^{−t}), so by Schwarz |(Φ^t)′(x̃)| =
> 1, and π ∘ Φ^t = φ^t ∘ π gives |(φ^t)′(x_∞)| = 1 ≠ e^{t/2}. *L is not a torus or C^**: the identity component of
> Aut is translations, resp. z ↦ az, which fix a point only if trivial, giving derivative 1. *L is not Ĉ*: it is
> compact, excluded by (C1) (or: the second fixed point of z ↦ e^{ct}z has derivative modulus e^{−t/2} ≠ e^{t/2}).
> By uniformization **L ≅ C**, contradicting (C2). ∎ **So: (31) along the fixed point's leaf + (0-coh) + compact ⇒
> no object; in particular Deninger's working hypothesis 7.5 (compact solenoid, p. 34) with (31) and a fixed point
> is inconsistent.**

> **Corollary A.1 (the archimedean flow is not conformal) [ADJ-B, new in this pass].** Under (0-fix) + (0-coh) on a
> compact X, for every fixed point x_∞ with leaf L and every t ≠ 0, φ^t|L is not a conformal map of L. *Proof.* By
> (C3) L is hyperbolic. If φ^t|L were conformal it would be holomorphic or antiholomorphic; either way its lift to D
> fixing a lift of x_∞ is an isometry of the Poincaré metric, so |dφ^t(x_∞)| = 1 in any conformal metric; but (0-fix)
> gives e^{t/2}. ∎ This is the precise content of Deninger's "too strong": (31) is false on the archimedean leaf at
> every t ≠ 0, and O's (0)(b) is false there too.

**Reconciliation of O-1 with Theorem A [ADJ-B].** O's Theorem O-1 (biholomorphic flow + fixed point with |dφ^t| ≠ 1 ⇒
leaf ≅ C) is correct; I re-derived it (its steps are exactly the four cases of (D) minus the compactness input). Its
conclusion and (C2) are contradictory, so the hypotheses of O-1 and of (0-coh) cannot coexist on a compact X with a
fixed point. O's frontier statement, built on O-1 under "clause (0) = (31)", therefore describes no object. O-2
(area scaling forbids compact preserved leaves under (0-glob)) is correct and is the (0-glob) shadow of (C1).

**[NOVELTY — dual-model check 2026-09-06]** Prior art for Theorem A and Corollary A.1, binding (`results/c3-r/s16/novelty/adjudication.md`; two independent sweeps, every precursor opened by the adjudicator at the page). **(A) PARTIAL** — in the smooth manifold category (A) is one line from ÁLKL's printed "the leaves preserved by φ correspond to the H-orbits preserved by φ̄, which indeed form Fix(φ̄)" (memoir arXiv:2402.06671 §4.1.2 printed p. 100; *Simple foliated flows* p. 2), because there the transverse map induced by φ^t *is* φ̄ and it fixes N pointwise; **new** is exactly the hypothesis this proof is written for — a compact foliated space with a merely jointly continuous flow, where there is no infinitesimal generator and no φ̄, so the plaque-chain map h_x must be constructed and identified with holonomy on N, and "concentrated on N" must be handled by applying holonomy invariance to B ∩ N. **(B) PARTIAL** — the conclusion is Deninger's Remark 2, printed **without proof** at arXiv:math/0204110 p. 13 (Cor. 3.5) = math/0505354 p. 24 (Cor. 5.5), restated at [x-21] p. 18 and [x-18] p. 6, and — on the natural reading of the ambiguous [x-06] p. 8 — asserted for his manifold class with fixed points too; every ingredient of the proof is printed for one α = 1 object in Leichtnam arXiv:math/0603576v2 Prop. 2 (p. 15) items 2]–4] and Lemma 10.1. **(B) is not Remark 2 with transversality removed: it supplies the proof Remark 2 lacks** (transversality only *supplies* the invariant measure, via the canonical form ω_φ of KMNT published Lemma 1.9). **(C) PARTIAL** — Candel Cor. 4.2 (p. 497) and Thm. 4.3 with the compact-leaf Dirac sentence (p. 498) are the printed engine and (C1)'s printed mechanism; Deninger applies Candel to the whole of X at [x-20] pp. 33–34 Rem. 7. New: the localization to N, its independence of arithmetic input and of one-dimensionality, and (C4). **(D) and Corollary A.1 NOVEL** — no printed statement of the inconsistency; Leichtnam's report of Deninger's *private* caution is at **arXiv:math/0603576v2 printed p. 12** (this section's "Leichtnam 2007 p. 11" is corrected to p. 12; verified by running head), gives a different reason and no argument, and Deninger's own [x-20] pp. 31–33 assumes (31) together with a fixed point. **§3.1's "closed leaf ⇒ compact leaf" is ANTICIPATED** and must cite Epstein, Ann. Inst. Fourier 26 (1976) 265–282, §§2.3–2.4, printed p. 268 (Ehresmann foliated spaces; the program's own proof), never claim it.

### 1.6 Verdict on T1

**STANDS-NARROWED.** Binding narrowed statement: *For S4′ objects carrying clause (0) in the form (0-fix), every compact
preserved leaf is a torus without fixed points and clause (iii)'s leaf is non-compact (A-II steps 1–5 as written). For
S4′ objects carrying (0-coh), there is no compact preserved leaf at all, every preserved leaf — clause (iii)'s
included — is a hyperbolic Riemann surface (the disk if χ = +1), the non-transverse set has invariant-transverse-measure
zero, and the flow is not conformal along the archimedean leaf. For S4′ as posed, neither conclusion is derivable.*
**"Conformal to C with χ = +1" FALLS** and must be struck from S16-4 and from the adjudication's table row A3.

---

## §2. T2 = A-III — FALLS

### 2.1 Candel's theorem applies to S4′ objects — yes

Candel, Ann. Sci. ENS (4) 26 (1993), NUMDAM scan (`candel.txt`), p. 490, read: "THEOREM. — Let M be a compact oriented
surface lamination with a riemannian metric g. Then χ(M, µ) < 0 for every positive invariant transverse measure if and
only if g is conformal to a metric of curvature −1. In particular, this holds true if M has no invariant measure."
§1.1 p. 491, read: "Let M be a separable, locally compact, metrizable space. We say that M is a p-dimensional
lamination if there is a cover of M by open sets U_i (called flow boxes or charts) and homeomorphisms [onto D_i × T_i]
… smooth in the first variable and all its partial derivatives with respect to the first variable are continuous
functions of all the variables." A compact foliated 3-space with Riemann-surface leaves is exactly a compact
Riemann surface lamination in this sense (the transversal is any "piece of metric space"; nothing requires it to be an
interval or totally disconnected); orientation comes from the complex structure; a continuous leafwise metric exists
in the conformal class. Deninger himself routes through the same theorem ([Den05] p. 33). **Applies verbatim.**

### 2.2 It needs a non-hyperbolic leaf — yes, and A-III supplies one only through T1(e)

Candel §4.1 p. 498, read: "if M contains a leaf L which is not a hyperbolic Riemann surface, then there is a positive
invariant transverse measure µ with χ(M, µ) ≥ 0. This is elementary if L is compact, for then it would be either a
sphere or a torus, and the corresponding Dirac measure works." Theorem 4.3, read: "if L is a euclidean leaf, then
there exists µ with support in L̄ and χ(M, µ) = 0." The adjudicator's inference (no measure ⇒ all leaves hyperbolic ⇒ a
C-leaf forces a measure) is valid; its premise (a C-leaf) comes from A-II(c) alone, i.e. from the expectation of §1.5.
Strip the expectation and A-III has no premise.

### 2.3 O's rescue, and why it cannot be used

O's A-III′: for S4′ objects carrying (0)(b) and a fixed point with |dφ^t| ≠ 1, an invariant transverse measure exists
(O-1 gives L ≅ C, Candel gives µ with supp µ ⊂ L̄). **Correct as a theorem.** But L̄ ⊂ N, so by Theorem A(A) that µ is
flow-invariant, and then (i) under (0-coh) Theorem A(B) is a contradiction; (ii) under (0-glob) the mass argument gives
α = 0; (iii) without any α clause, pairing C_µ with the area class gives φ^{t*}[λ_g] = [λ_g] on the part of H̄²_F that
C_µ sees — the object has α = 0 in Deninger's sense. So the class in which A-III′ produces a measure is the α = 0 class,
disjoint from every S4′ + α = 1 class. O's own Theorem O-6 shows the same thing from the other side: it needs
M(φ^t_*µ) = e^{αt}M(µ) with α ≠ 0, which a flow-invariant µ violates; so O-6's base B cannot contain any measure
concentrated on N. **The rescue rescues A-III into a class the program cannot inhabit.**

### 2.4 Could existence follow from clause (0) some other way?

Not that I can derive. [ADJ-B, standard Hahn–Banach/Sullivan argument, recorded for the record:] a positive
holonomy-invariant transverse measure exists on X if and only if no leafwise strictly positive 2-form lies in the
closure of d_F A¹_F(X) (separate the weak-* compact convex base of positive currents from the closed subspace of closed
currents; the separating form annihilates all closed currents, hence lies in the closure of the exact forms, and is
positive on Dirac currents). (0-coh) says only that [λ_g] ≠ 0 spans H̄²_F; it does not say that every fλ_g with f > 0
has nonzero class, and (15) alone does not decide it. Leichtnam posits µ separately (5], both lists, read), and
Deninger's Remark 7 assumes "a preferred transverse measure µ". **Existence remains an axiom.** What IS a theorem
(Theorem A(C4)): whatever invariant transverse measure clause (iv) posits gives N measure zero; and (O-6, §5.3) if any
exists, an e^{−t}-eigen-measure exists.

### 2.5 Verdict on T2

**FALLS.** The only non-trivial input of the derivation is not derived from the printed hypotheses; under the clause
the program must carry it is contradicted; under the alternative hypotheses that make it true, the object has α = 0.
"A holonomy-invariant transverse measure NECESSARILY EXISTS" must be struck from S16-6, table row A2, §0 item 3 and N7.

---

## §3. T3 = A-IV — STANDS-NARROWED

### 3.1 (a) A closed leaf of a compact foliated space is compact — PROVED (both refuters; re-derived)

**Claim.** X a compact metrizable foliated space with a finite atlas U_i ≅ D_i × T_i (D_i an open disk, T_i a locally
compact metrizable space, transitions (x, y) ↦ (f_{ij}(x, y), g_{ij}(y))). If a leaf L is closed in X, then L is
compact in its leaf topology; conversely a compact leaf is closed.

**Proof [ADJ-B].** *Step 0.* Each leaf is a countable union of plaques: a plaque P is second countable, P ∩ U_j has
countably many components, each inside one plaque of U_j; iterate along plaque chains. Hence L ∩ T_i is countable.
*Step 1.* Shrink: choose closed disks D̄′_i ⊂ D_i with the D′_i × T_i still covering X (Lebesgue number on the finite
atlas). Then L is a countable union of the compact — hence closed — sets D̄′_i × {y}, y ∈ L ∩ T_i. *Step 2 (Baire).*
L closed in compact metrizable X is a compact metric space, hence Baire; some D̄′_i × {y₀} has nonempty interior in L:
there is an open W ⊂ X with ∅ ≠ W ∩ L ⊂ D̄′_i × {y₀}. W ∩ (D_i × {y₀}) is a nonempty open subset of the plaque D_i × {y₀}
⊂ L meeting D̄′_i, hence meeting the interior D′_i: pick (x₀, y₀) ∈ W ∩ L with x₀ ∈ D′_i, and a product neighborhood
D″ × V ⊂ W of it. For z ∈ V ∩ L the whole plaque D_i × {z} lies in L, so (x₀, z) ∈ W ∩ L ⊂ D̄′_i × {y₀}, forcing z = y₀:
**L ∩ V = {y₀}**, y₀ is isolated in L ∩ T_i. *Step 3 (holonomy propagates isolation).* For any y₁ ∈ L ∩ T_j, holonomy h
along a plaque chain in L from y₀'s plaque to y₁'s is a homeomorphism from a neighborhood V₀ ⊂ V of y₀ onto a
neighborhood of y₁ with h(V₀ ∩ L) = h(V₀) ∩ L (holonomy along a leafwise path carries points of L to points of L and
so does its inverse); so h(V₀) ∩ L = {y₁}. *Step 4.* In every chart L ∩ U_j is a disjoint union of plaques D_j × {y}
with y isolated in L ∩ T_j, each open in L for the subspace topology; so the subspace topology is the leaf topology,
and L, compact in the former, is a compact surface. ∎ (The same proof, with "L closed in a locally compact metrizable
open saturated W" in place of X, shows a leaf closed in W is proper in W — used in §3.4.) Contrapositive: a
non-compact leaf of a compact foliated space is not closed; L̄ ∖ L ≠ ∅. **(a) STANDS**; the adjudicator asserted
properness, the refuters proved it, and I re-derived it.

### 3.2 (b) N is closed, saturated, flow-invariant and consists exactly of the preserved leaves — PROVED for the right N

On a foliated space TX does not exist, so the adjudicator's N = {x : Y_φ(x) ∈ T_xF} is not even defined; the
definition must be **N := {x ∈ X : φ^t(x) ∈ L_x for all t ∈ R}** = the union of the preserved leaves.
*Saturated and flow-invariant:* immediate ({t : φ^t(x) ∈ L_x} depends only on L_x; φ^t maps leaves to leaves).
*Subgroup:* if φ^s(x), φ^t(x) ∈ L_x then φ^{s+t}(x) ∈ φ^t(L_x) = L_x; so the set is a subgroup of R, and if it contains
(−ε, ε) it is R. *Closed:* in a chart U′ ⊂ U ≅ D × T and for |t| < ε with φ^t(U′) ⊂ U, the flow induces a continuous
local map h^t on T (a plaque piece is leafwise connected, φ^t is leafwise continuous, so its image lies in one plaque
of U; the transverse coordinate of the image is continuous in y); x = (x₀, y) ∈ N iff h^t(y) = y for |t| < ε (⇐ by the
subgroup step; ⇒ because the transverse coordinate of φ^s(x) is a continuous function of s into the countable set
L_x ∩ T, hence constant). So N ∩ U′ = D′ × ⋂_{|t|<ε} Fix(h^t), an intersection of closed sets. ∎ No transverse
regularity is used. **(b) STANDS with this N.** On a C¹ manifold with a C¹ flow the two definitions agree (the tangency
set is flow-invariant since Tφ^t(TF) = TF and Y_φ(φ^t x) = Tφ^t Y_φ(x)); for a merely continuous transverse flow O's
counterexample O-4 — h^t(y) = (y^{1/3} + t)³, a genuine flow with h^t(0) = t³ ≠ 0 yet d/dt h^t(0)|₀ = 0 — shows the
tangency definition strictly contains the preserved set, so the adjudicator's step (1) as worded ("every leaf in N is
preserved") is false there. **Repair by definition; nothing downstream changes.**

### 3.3 The structural conclusion, (α), (γ)

*A-IV steps 2–3.* Given a non-compact preserved leaf L: L̄ ⊋ L (§3.1); L ⊂ N closed gives L̄ ⊂ N; the closure of a leaf
is saturated (L ∩ U is a union of full plaques), so L̄ ∖ L is a nonempty union of leaves, all in N, hence preserved.
The input "L non-compact" comes from T1: under (0-fix) via A-II; under (0-coh) via Theorem A(C1) directly. **The
conclusion "N is a compact saturated lamination of preserved leaves, never one leaf, never a finite union of compact
leaves" STANDS for S4′ + clause (0)**, and under (0-coh) strengthens to: *N contains no compact leaf, every leaf of N
is hyperbolic, and N has invariant-transverse-measure zero.* Not derivable for S4′ as posed.

*(α) ALKL.* `r3s-17` Abstract (read): "Assume the closed orbits of φ are simple and its preserved leaves are
transversely simple. In this case, there are finitely many preserved leaves, which are compact." §1.1 (p. 1, read):
"If these fixed points of φ̄ are simple, then the leaves preserved by φ are called transversely simple." §4.1.2
(p. 100, read): "Suppose φ is transversely simple unless otherwise stated. Then M⁰ is a finite union of compact
leaves because every fixed point of φ̄ is isolated." `r3s-30` p. 2 (read): "A preserved leaf L is called transversely
simple if the corresponding fixed points p̄ of φ̄ are simple. In this case, φ̄^t_* = e^{κt} on T_p̄Σ ≡ R for some κ ∈ R^×";
Theorem 1.1 (read) classifies the closed manifolds carrying such flows and in cases (iii)–(v) "there is a finite
number of compact leaves, which are the preserved leaves of every transversely simple foliated flow". So finiteness
and compactness of the preserved leaves are **consequences of a hypothesis ALKL require** (a nonzero transverse
exponent at every preserved leaf), on a closed manifold. An S4′ + clause (0) object violates the consequence, hence
the hypothesis. **(α) STANDS**, and is over-determined (manifold vs. lamination; A-IV; and under any α = 1 clause a
compact preserved leaf is impossible outright — Theorem A(C1)/O-2).

*(γ) Leichtnam 2].* The inconsistency argument needs compactness of S_K: compactness + (13) [or (15)] ⇒ the archimedean
leaf is non-compact ⇒ its closure adds preserved leaves ⇒ 2]'s "transverse to all the leaves different from the ones
containing the r₁ + r₂ fixed points" fails. Does Leichtnam assume S_K compact? Full-text search of `r3s-20` §4.1 and
of the 2008 author copy §5.1 (both read in full): the string "compact" occurs in the axiom lists only inside
"C_compact" (test functions). His 2007 S_Q (`r3s-21` p. 2, read): "L is a σ−compact complex 1−dimensional laminated
space … The quotient L/Q^{+*} allows to compactify the space L × R^{+*}/Q^{+*}" — compactness is the declared purpose,
and the archimedean part is a whole quotient L/Q^{+*}, not a single leaf. The adjudicator's "compactness is required
by his own Assumption 6] (trace-class)" is an undefended inference and is not adopted. **(γ) RESTATED:** *Leichtnam's
Assumption 2] (2008; 2013) is inconsistent with compactness of S_K given his own (13) or (15); he does not print
compactness in either list, so the lists are not self-contradictory as printed; every compact realization — including
the 2007 compactified shape — must weaken 2].* Also N8's novelty note should read "new as a derivation; the shape
'archimedean part = a whole quotient' is already Leichtnam 2007's" (O's point, correct).

### 3.4 B1′ — the length-group kill extends to finitely many finite-type leaves [F; re-derived, now dual-checked]

**Statement.** M a closed 3-manifold, F a C¹ codimension-one foliation, φ a C¹ foliated flow, N its non-transverse
set, M₀ = M ∖ N. If N is a finite union of leaves L₁, …, L_m with dim H₁(L_a; Q) < ∞, then the group Λ generated by the
lengths of the closed orbits of φ is finitely generated; hence no such (M, F, φ) satisfies S4′ (i) + (ii).

**Proof [ADJ-B].** (1) On M₀ the flow is transverse to F and maps leaves to leaves, so KMNT's 1-form ω (ω|TF = 0,
ω(φ̇) = 1) exists and is closed — KMNT Lemma 1.10 and its proof (`kmnt.txt`, read: closedness is proved in flow-box
coordinates φ^s(z, t) = (z, t + s), which exist on any open set where the flow is transverse; nothing in the proof uses
the global hypothesis beyond transversality on M₀). For a closed orbit c ⊂ M₀ of least period ℓ(c), ∫_c ω = ℓ(c); every
γ_p lies in M₀ (§1.3). So ⟨log p⟩ ⊂ [ω](H₁(M₀; Z)), and it suffices that dim H₁(M₀; Q) < ∞. (2) Pass to the
orientation double cover if needed (lengths become ℓ or 2ℓ; N lifts to a finite union of finite-type leaves; finite
generation descends); assume M orientable, so an orientable properly embedded surface is two-sided. (3) Remove the
leaves of N one at a time. Given the open W_k = M ∖ (L₁ ∪ … ∪ L_k) with N_k = N ∩ W_k closed in W_k and a finite union of
leaves, some leaf of N_k is closed in W_k: order them by L_a ≼ L_b iff L_a ⊂ cl(L_b) and take L_a ≼-minimal; if cl(L_a)
⊋ L_a then some L_b ⊂ cl(L_a) with b ≠ a, so L_a ⊂ cl(L_b) by minimality and K := cl(L_a) = cl(L_b) is a locally compact
set, a countable union of compact plaques of finitely many leaves; by Baire some plaque of some L_c ⊂ K has interior in
K, §3.1 Steps 2–3 then make L_c open in K, and both dense leaves L_a, L_b must meet the open L_c, so a = c = b —
contradiction. So L := L_a is closed in W_k, hence proper (§3.1 remark), two-sided, with a product neighborhood
ν ≅ L × (−1, 1). (4) Mayer–Vietoris for W_k = (W_k ∖ L) ∪ ν, intersection ≃ L ⊔ L:
H₁(L)² → H₁(W_k ∖ L) ⊕ H₁(L) → H₁(W_k), so dim H₁(W_k ∖ L) ≤ dim H₁(W_k) + dim H₁(L) (Q-coefficients). (5) Iterating,
dim H₁(M₀; Q) ≤ dim H₁(M; Q) + Σ_a dim H₁(L_a; Q) < ∞; so the period group is finitely generated, while ⟨log p⟩ is free
abelian of infinite rank (unique factorization). ∎

**Consequences.** The necessary condition for S4′ (i)+(ii) on a closed 3-manifold is **rank H₁(M ∖ N) = ∞**: N has
infinitely many leaves or a leaf of infinite type. The adjudication's picture "a plane leaf (H₁ = 0) plus a few compact
leaves" is dead on a closed 3-manifold by the same mechanism as B1 — independently of Theorem A, which kills it
anyway.

### 3.5 Verdict on T3

**STANDS-NARROWED.** (a), (b) [with N := union of preserved leaves], (α) STAND with proofs supplied. The structural
conclusion and (β) STAND for S4′ + clause (0) and are sharpened (under (0-coh): no compact leaf in N, all hyperbolic,
measure zero; B1′ closes the finitely-many-finite-type-leaves case). (γ) STANDS-NARROWED in the wording of §3.3.

---

## §4. T4 = the vacuity ruling — STANDS-NARROWED

**Status given T1 and T3.** The ruling is T1 (non-compact archimedean leaf) + T3 steps 2–3. *For S4′ as posed:* not
derivable (a compact S² archimedean leaf with a source–sink flow is compatible with (i)–(iv); if all preserved leaves
are compact and finitely many, B1 applies). *For S4′ + clause (0):* the first sentence STANDS and B1 as printed does
not bear. *"The closed-3-manifold case is OPEN"* is overstated in both cases: B1′ (§3.4) kills every N that is a
finite union of finite-type leaves, and under (0-coh) Theorem A pins N further.

**Theorem O-5, corrected [O; re-derived with the hypothesis it needs].** Under (0-coh) [not under (0-fix) alone — there
a compact torus leaf in L̄ ∖ L could be the minimal set], with X compact: let L be clause (iii)'s leaf. L̄ is a nonempty
compact saturated set, so it contains a minimal set K (Zorn; chains of nonempty compact saturated sets have nonempty
compact saturated intersections). K is not a compact leaf (Theorem A(C1)). K is not open in X: by clause (iii) L lies
in the closure of ⋃_p γ_p, so L̄ ⊂ cl(⋃γ_p), and a nonempty open K inside that closure would meet some γ_p, but K ⊂ N
and γ_p ∩ N = ∅ (§1.3). So K is an **exceptional minimal set** in Hurder's sense (`r3s-29` §5, read: "a minimal set K
is exceptional if K is not a compact leaf, and not an open set"), consisting of hyperbolic preserved leaves and
carrying no invariant transverse measure. ∎ (O's proof used "N ≠ X ⇒ K not open", which needs X connected; the
clause-(iii) route above does not.)

**Binding manifold statements.**

*Case A — S4′ + clause (0) = (0-fix) + (0-coh), the case the program will work in.* Let (M, F, φ) be a closed
3-manifold with a C¹ codimension-one foliation by Riemann surfaces and a C¹ foliated flow satisfying (i)–(iv) and
clause (0). Then: (1) the non-transverse set N is a compact saturated set of non-compact hyperbolic preserved leaves,
of invariant-transverse-measure zero (Theorem A); (2) N contains an exceptional minimal set K ⊂ L̄ (O-5 corrected);
(3) rank H₁(M ∖ N; Q) = ∞, so N is not a finite union of finite-type leaves (B1′); (4) the flow is not conformal along
the archimedean leaf (Corollary A.1); (5) every printed obstruction — [Den05] p. 24 Rem. 2–3 (everywhere transverse),
KMNT Def. 1.5(i) / ALKL transverse simplicity / [x-06] p. 6 (finitely many compact preserved leaves), B1, B1′ — has a
hypothesis such objects violate. **The class is OPEN in print.** The decisive instruments are Duminy's theorem
(semiproper leaves of K have a Cantor set of ends — Hurder §5, read; report-level, Cantwell–Conlon not read) and
Hurder's Problem 5.4, both for C² foliations, plus measure-free exceptional minimal sets (Sacksteder-type results,
recalled only, not relied on).

*Case B — S4′ as posed.* If N is a finite union of compact leaves (KMNT/ALKL class) or of finite-type leaves, the object
does not exist on a closed 3-manifold (B1, B1′). Otherwise the case is OPEN in print. Which of these an S4′ object
without clause (0) falls into is not determined by (i)–(iv).

*Case C — S4′ + Deninger's global (31) with a fixed point.* No object, on a manifold or elsewhere (Theorem A(D)).

**Verdict on T4: STANDS-NARROWED**, to Case A. The enacted vacuity sentence in S16-3 must read (exact text in §7).

---

## §5. T5 = the clause-(iv) restatement — STANDS-NARROWED

### 5.1 A-I re-derived from [Den05] (20)/(31) and [x-18] Construction 3

*Inputs read.* [Den05] p. 21 (20), p. 27 (31); [x-18] p. 3 Construction 3, verbatim: "let ω_φ be the one-form on X
defined by ω_φ|TF = 0 and ⟨ω_φ, Y_φ⟩ = 1. One checks that dω_φ = 0 and that ω_φ is φ^t-invariant i.e. φ^{t*}ω_φ = ω_φ
for all t ∈ R" — stated for triples "as in the dictionary above", where (Dictionary 1 part 1, same page) "The leaves of
F should be transversal to the R-orbits"; so ω_φ exists only off N (ω_φ|TF = 0 and ⟨ω_φ, Y_φ⟩ = 1 are incompatible where
Y_φ ∈ TF), as the adjudicator says.

*Derivation [ADJ-B].* X compact, g continuous leafwise with (20) for the constant α, µ a positive holonomy-invariant
transverse measure finite on transversals which is a flow eigen-measure: µ(φ^t(B)) = e^{−βt}µ(B) for transverse Borel
sets B (this "image" convention is the one under which the adjudicator's "α = β" is correct; with the pushforward
convention φ^t_*µ = e^{−βt}µ the same computation gives β = −α — a notational slip in A-I's symbolic hypothesis and in
O's §5.1, harmless because both draw the right verbal conclusion). Put m = vol_g ⊗ µ, 0 < m(X) < ∞ (finite atlas,
continuous g, µ finite on transversals). For a small Borel set A in a chart with φ^t(A) in a chart,
m(φ^t A) = ∫ area_g(φ^t(A) ∩ P′_{y′}) dµ(y′); substituting y′ = φ̄^t(y) (the induced transverse map, which on a
transversal is holonomy composed with the local transverse flow) and using dµ(φ̄^t y) = e^{−βt}dµ(y) and
area_g(φ^t(A ∩ P_y)) = e^{αt}area_g(A ∩ P_y) (in dimension 2 the metric factor e^{αt} is the area factor), one gets
m(φ^t A) = e^{(α−β)t}m(A). Summing over a finite Borel partition and taking A = X = φ^t(X): m(X) = e^{(α−β)t}m(X), so
**α = β**. ∎ The content is convention-free: *the flow multiplies the transverse measure of a set by exactly the inverse
of the factor by which it multiplies leafwise area*; with α = 1, µ(φ^t B) = e^{−t}µ(B) and the return map along γ_p
scales µ by 1/p — Leichtnam 2007 Lemma 6 (`r3s-21` p. 14, read: "µ_L(q·T) = (1/q)µ_L is a consequence of Assumption (i)
(Jac M_q = 1/q)").
Special case ([Den05] p. 24 Rem. 2): closed 3-manifold, flow everywhere transverse, µ = |ω_φ| holonomy-invariant and
flow-invariant, so β = 0 and α = 0. **A-I STANDS under its printed hypotheses** (global (20) + eigen-measure), which
S4′ as posed does not supply.

### 5.2 The cohomological form — what the program should carry

Under (0-coh), if φ^t_*µ = c(t)µ for a holonomy-invariant µ ≠ 0, then ⟨C_µ, φ^{t*}λ_g⟩ = e^t⟨C_µ, λ_g⟩ (C_µ kills the
closure of exact forms) and = ⟨C_{φ^t_*µ}, λ_g⟩ = c(t)⟨C_µ, λ_g⟩, so c(t) = e^t: µ(φ^t B) = e^{−t}µ(B). **Same modulus,
no global conformality.** The eigen hypothesis is automatic when H̄²_F(X) ≅ R (Leichtnam 4]): the dual of H̄²_F is the
space of closed 2-currents, so all invariant transverse measures are proportional (Deninger uses exactly this on
p. 33). Corollary (Theorem A(C4)): µ(N) = 0 — the measure lives entirely off the archimedean lamination.

### 5.3 Existence of the eigen-measure given existence of some measure — Theorem O-6 [O; re-derived, sign corrected]

Let M ≠ {0} be the cone of positive holonomy-invariant transverse measures, identified with positive closed
2-currents; M(µ) := ⟨C_µ, λ_g⟩ ∈ (0, ∞). B = {µ : M(µ) = 1} is convex, weak-* closed (positivity, closedness and the
normalization are weak-* closed conditions) and bounded (|⟨C_µ, ω⟩| ≤ ‖ω/λ_g‖_∞), hence weak-* compact. Under (0-coh),
M(φ^t_*µ) = ⟨C_µ, φ^{t*}λ_g⟩ = e^t M(µ) (O wrote e^{−αt}; the sign is immaterial), so S^t := e^{−t}φ^t_* is a commuting
family of weak-* continuous affine maps of B into B; Markov–Kakutani gives µ₀ ∈ B with φ^t_*µ₀ = e^tµ₀, i.e.
µ₀(φ^t B) = e^{−t}µ₀(B). ∎ So: **if any invariant transverse measure exists, one with modulus exactly e^{−t} exists**;
uniqueness needs H̄²_F ≅ R.

### 5.4 The three halves of the restatement

- "the holonomy-invariant transverse measure that **necessarily exists**" — FALLS (T2).
- "is scaled by the flow with modulus **exactly e^{−t}**" — STANDS under (0-coh) for the eigen-measure (unique when
  H̄²_F ≅ R; existent whenever any measure exists, O-6); never flow-invariant; never charging N.
- "its ALKL justification must be **deleted**" — half right: ALKL's *theorem* does not apply (§3.3 (α)), but the
  *reason* for clause (iv) survives — Deninger's trace formula carries χ_Co(F, µ)δ₀ ([Den05] (24) p. 23; Rem. 6 p. 33,
  read) and Leichtnam 5] needs µ for the L² scalar product on H̄¹_F. **Replace the citation; keep the rationale.**

### 5.5 Verdict on T5 and the clause (iv) I enact

**STANDS-NARROWED.** Clause (iv) shall read:

> **(iv)** there is a positive holonomy-invariant transverse measure µ, finite on transversals. Its existence is an
> axiom (Leichtnam 2008 5], 2013 5]), not a consequence of (i)–(iii) or of clause (0); it is what the leafwise trace
> formula needs (the χ_Co(F, µ)δ₀ term, [Den05] (24); the L² structure on H̄¹_F, Leichtnam 5]). Under clause (0)
> [φ^{t*} = e^t on the one-dimensional H̄²_F], µ is unique up to scale and the flow scales it with modulus exactly
> e^{−t} (return map along γ_p: factor 1/p; Leichtnam 2007 Lemma 6, Prop. 2); in particular µ is never flow-invariant
> and gives the non-transverse set N measure zero. The Álvarez López–Kordyukov–Leichtnam trace formula
> (arXiv:2402.06671) does not apply to such objects (its transverse-simplicity hypothesis forces finitely many compact
> preserved leaves); no trace formula in print covers them.

---

## §6. T6 = N10 — STANDS-NARROWED

### 6.1 The two pages, read

[Den05] p. 23, Corollary 5.5: "Let X be a compact 3-manifold with a foliation F by surfaces having a dense leaf. Let
φ^t be a non-degenerate F-compatible flow which is **everywhere transversal to F**. Assume that φ^t is conformal as in
(20) with respect to a metric g on TF." p. 24, Remark 2: "Actually **the conditions of the corollary** force α = 0 i.e.
the flow must be isometric with respect to g. We have chosen to leave the α in the fomulation since there are good
reasons to expect the corollary to generalize to more general phase spaces X than manifolds, where α ≠ 0 becomes
possible i.e. to Sullivan's generalized solenoids." Remark 3: "One can show that the group generated by the lengths of
closed orbits is a finitely generated subgroup of R **under the assumptions of the corollary**. In order to achieve an
infinitely generated group the flow must have fixed points." So the printed theorem is under everywhere-transversality
— the adjudicator's reading is correct; both scouts had dropped the hypothesis.

[x-06] p. 6 sets the class: "The fixed points of φ should lie in finitely many compact leaves. All other leaves should
be non-compact and the flow should be transversal to them." p. 8: "Formula (9) does not contain a term corresponding
to (1 − e^{−2t})^{−1} in (8) because **we assumed that φ^t had no fixed points**. … One can show that the conformal
factor e^{αt} for a metric g_F as above necessarily has to be 1, i.e. α = 0 … This is only one instance which shows that
the class of smooth compact manifolds is too restrictive … One can show that α = 1 can be achieved if for X we allow the
local structure (totally disconnected) × (3-dimensional ball), c.f. [Lei07]." The scope of the α = 0 sentence is
ambiguous on the page (the (9) discussion is fixed-point-free; the metric "as above" is the one of the general triple);
mathematically it is true in the whole p. 6 class (§6.2). And Deninger's printed escape for α ≠ 0 is the solenoid, not
fixed points (O's reading, confirmed).

### 6.2 α = 0 is forced by any compact preserved leaf [F and O; re-derived]

Under global (20): a compact preserved leaf T has area_g(T) = area_g(φ^t T) = e^{αt}area_g(T), so α = 0 (O-2). Under the
cohomological α (φ^{t*}[λ_g] = e^{αt}[λ_g]): the counting measure δ_T of T on transversals is holonomy-invariant, finite,
concentrated on N, hence flow-invariant (Theorem A(A)), and the pairing of §1.5(B) gives e^{αt} = 1. Either way **the
entire KMNT / ALKL / [x-06] p. 6 class (fixed points inside finitely many compact leaves) has α = 0** — consistent with
ALKL Theorem 1.3.10's ±1 closed-orbit coefficients (memoir p. 8; adjudication §1 A7). So "with preserved leaves the
manifold question is open" is wrong whenever a preserved leaf is compact; and under Deninger's own (31) with a fixed
point the question is closed negatively on any compact space, manifold or not (Theorem A(D)).

### 6.3 Verdict on T6

**STANDS-NARROWED.** Corrected statement: *Print's theorem ([Den05] Rem. 2) forces α = 0 under "everywhere transversal
to F"; α = 0 is also forced, on manifolds and laminations alike, by any compact preserved leaf, which covers Deninger's
printed manifold class ([x-06] p. 6) and KMNT's FDS³; [x-06] p. 8's sentence is therefore true in its own setting, and
its printed escape is the solenoid. The closed-3-manifold question for α = 1 is open exactly for foliated flows with a
preserved leaf and no compact preserved leaf — the S4′ + clause (0) situation — and is closed negatively under global
(31) with a fixed point.*

---

## §7. THE BINDING FRONTIER STATEMENT, AND THE LEDGER WORDING

### 7.1 Frontier paragraph (ready to paste into `directions/C3-geometric-substrate.md`)

FRONTIER (Session 16, after the adversarial pass; binding, 2026-09-06). S4′ is Leichtnam's printed axiom list (2008
§5.1; 2013 §4.1), unrealized in every class except Deninger's rank-1 elliptic-curve solenoid, and it must be read with
clause (0) = (0-fix) + (0-coh) — the fixed-point SO(2) axiom (Leichtnam (13)) and Deninger's own α = 1, "φ^{t*} acts by
e^t on the one-dimensional H̄²_F" ([Den05] p. 27 = Leichtnam (15)) — because the four clauses imply neither; Deninger's
global conformality (31) must not be added, since on a compact space (31) along the fixed point's leaf together with
α = 1 is inconsistent (Schwarz–Pick makes the leaf C, Candel puts an invariant transverse measure in its closure, and any
transverse measure carried by preserved leaves is flow-invariant). For S4′ + clause (0) the archimedean lamination
N — the closure of the χ ≠ 0 leaf, always strictly larger than it — contains no compact leaf, consists of hyperbolic
Riemann surfaces, has invariant-transverse-measure zero, and carries a flow that is not conformal along the archimedean
leaf (the hyperbolic disk, if χ = +1) at any time; the clause-(iv) measure, whose existence remains an axiom, lives off
N and is scaled with modulus e^{−t}. On a closed 3-manifold the printed length-group kill (KMNT/ALKL class) does not bear,
but its mechanism extends to every N that is a finite union of finite-type leaves, so the manifold case is open exactly
where rank H₁(M ∖ N) = ∞ and N contains an exceptional minimal set of hyperbolic preserved leaves — Duminy's theorem and
Hurder's Problem 5.4 are the instruments, now applied to a disk leaf. Nothing in print constructs or kills this class;
no construction attempt is licensed until Q-S4⁗ is re-posed for a hyperbolic, measure-free archimedean lamination.

### 7.2 Exact wording for ledger §16 (dated addenda; ENACT / NARROW / STRIKE)

**S16-3, vacuity sentence — NARROW.** Replace "But [ADJ-A-IV] no S4′ object has a non-transverse set of that form, so the
result does not bear on S4′. The closed-3-manifold case for S4′ is OPEN." by:

> [NARROWED 2026-09-06, `refute-adjudication.md` §4 — binding.] For S4′ objects carrying clause (0) [(0-fix) + (0-coh),
> S16-4 as narrowed] the non-transverse set N is never a finite union of compact leaves — nor of finite-type leaves
> (B1′: on a closed 3-manifold the period group is finitely generated whenever N is a finite union of leaves with
> finite-rank H₁; dual-checked, refuter F + binding adjudicator) — so the length-group result does not bear on them;
> the necessary condition on a closed 3-manifold is rank H₁(M ∖ N) = ∞. The closed-3-manifold case for such objects is
> OPEN only in the class where N is a measure-free lamination of hyperbolic preserved leaves containing an exceptional
> minimal set. For S4′ as posed (no clause (0)) the vacuity claim is not derivable and B1 bears on the subclass it was
> written for. The α = 0 note is extended: α = 0 is also forced by any compact preserved leaf, so Deninger's printed
> manifold class ([x-06] p. 6) has α = 0; under global (31) with a fixed point on a compact space no object exists.

**S16-4 — NARROW (strike "conformal to C, χ = +1"; strike the unconditional "In any S4′ object").** Replace by:

> S16-4 [NARROWED 2026-09-06]. CLAUSE (0) REQUIRED; THE OBSTRUCTION AT CLAUSE (iii). S4′'s four clauses do not imply the
> fixed-point source property: [Den05] p. 33's Fact is a corollary of the global conformality (31) (pp. 31–33, "in the
> situation of the preceeding remark"), and Leichtnam prints it as the separate axiom 3]a (13) [2008: 3] (12)]. S4′ is
> amended by clause (0) = (0-fix) [a fixed point per archimedean place lying in clause (iii)'s leaf, with
> e^{−t/2}T_xφ^t|T_xF ∈ SO(2) at every fixed point] + (0-coh) [H̄²_F ≅ R[λ_g] and φ^{t*}[λ_g] = e^t[λ_g] — Deninger's
> definition of α = 1, p. 27 = Leichtnam 4] (15)]. Deninger's global (31) is NOT added: on a compact space, (31) along
> the fixed point's leaf together with α = 1 is inconsistent (Theorem A(D), dual-checked); Leichtnam's 2007 replacement
> of (31) by (15) on Deninger's advice (r3s-21 p. 11) is thereby made necessary. For S4′ + (0-fix): every compact
> preserved leaf is a torus without fixed points and clause (iii)'s leaf is non-compact (A-II steps 1–5, dual-checked;
> uses clause (i) in its "exactly" form). For S4′ + (0-coh): no compact preserved leaf exists, every preserved leaf is a
> hyperbolic Riemann surface, clause (iii)'s leaf is the hyperbolic disk if χ = +1, and the flow is not conformal along
> it for any t ≠ 0 (Theorem A, Corollary A.1, dual-checked). STRUCK: "conformal to C, χ = +1" — it rested on [Den05]
> p. 33 Rem. 7, an expectation that presupposes a transverse measure, names no particular leaf, and for K ≠ Q predicts
> hyperbolic leaves. Retained: no closed manifold with a transversely simple foliated flow realizes S4′ + clause (0).

**S16-5 — NARROW.** Replace by:

> S16-5 [NARROWED 2026-09-06]. STRUCTURAL FORCING, for S4′ + clause (0). The archimedean leaf is non-compact, hence not
> closed (closed leaf ⇒ compact leaf, proved for compact laminations by Baire plus holonomy); its closure lies in
> N := the union of the preserved leaves, which is closed, saturated and flow-invariant (proved with this definition —
> the tangency definition {Y_φ ∈ TF} is unavailable on a foliated space and fails for merely continuous transverse
> flows). So the archimedean part is a compact saturated LAMINATION of preserved leaves, never one leaf and never
> finitely many compact ones; under (0-coh) it contains no compact leaf, every leaf of it is hyperbolic, and it has
> invariant-transverse-measure zero. (α) stands: ALKL's transverse simplicity is a hypothesis forcing finitely many
> compact preserved leaves on a closed manifold (memoir Abstract; §4.1.2 p. 100; r3s-30 Thm. 1.1), so their trace
> formula never applies. (β) stands and is superseded by B1′ (S16-3). (γ) RESTATED: Leichtnam's Assumption 2] is
> inconsistent with compactness of S_K given his own (13) or (15); he prints no compactness in 2008 §5.1 or 2013 §4.1;
> his 2007 S_Q is declared a compactification (r3s-21 p. 2) and its archimedean part is already a whole quotient, not
> a leaf; any compact model must weaken 2]. Not derivable for S4′ as posed.

**S16-6 — STRIKE the existence half; ENACT the modulus; REPLACE the deletion.** Replace by:

> S16-6 [NARROWED 2026-09-06]. CLAUSE (iv). STRUCK: "A holonomy-invariant transverse measure NECESSARILY EXISTS" and its
> Candel justification — the derivation needed a euclidean archimedean leaf, which is not derived and is impossible
> under (0-coh) (Theorem A(C2)); existence remains an axiom (Leichtnam 2008 5], 2013 5]). ENACTED: under clause (0) the
> measure — unique up to scale when H̄²_F ≅ R; an e^{−t}-eigen-measure exists whenever any invariant transverse measure
> exists (Markov–Kakutani on the normalized weak-* compact base; refuter O's Theorem O-6, re-derived) — is scaled by the
> flow with modulus exactly e^{−t}, the return map at γ_p scales it by 1/p (Leichtnam 2007 Lemma 6, Prop. 2), it is
> never flow-invariant, and it gives the non-transverse set N measure zero. REPLACED: the ALKL parenthetical is void as
> a justification (ALKL's theorem does not apply, S16-5 (α)), but the rationale for clause (iv) — the χ_Co(F, µ)δ₀ term
> of Deninger's trace formula ([Den05] (24) p. 23, Rem. 6 p. 33) and the L² structure of Leichtnam 5] — stands. Clause
> (iv) now reads as in `refute-adjudication.md` §5.5.

**S16-8 — consequential RE-POSING (recommended).** Q-S4⁗ as written asks for a compact lamination with a leaf conformal
to C; under (0-coh) that leaf is impossible, so the gate must ask instead: does there exist a compact foliated space X
with Riemann-surface leaves and a foliated flow whose non-transverse set N is a compact saturated sub-lamination with
no invariant transverse measure, all of whose leaves are hyperbolic, containing an exceptional minimal set, with a
hyperbolic-disk leaf on which the flow is a non-conformal source of rate 1/2 — and (manifold case) can such an N sit in
a closed 3-manifold with rank H₁(M ∖ N) = ∞? Duminy's theorem (semiproper leaves of an exceptional minimal set have a
Cantor set of ends; the disk has one) and Hurder's Problem 5.4 remain the instruments.

---

## §8. HONESTY — read versus recalled

**Read by me this session, at the page cited (pdftotext -layout of the files on disk; text extractions in the session
scratchpad).** `x-20` [Den05]: p. 21 (Thm. 4.1, (20)), pp. 23–24 (Cor. 5.5 with hypotheses, Remarks 1–3, the proof's
first lines), p. 27 (the α = 1 definition, (31), the N p^k paragraph), p. 30 (7.3 definition of a flow), pp. 31–34
(Remark 7.6(4), the determinant, (35), W_x, Remark 5, the Fact, Remark 6, Remark 7 in full, the unramified sentence),
p. 34 (7.5 working hypothesis). `x-18`: pp. 3–4 (Dictionary 1 part 1, Remark 2, Construction 3, the fibration/rank
sentence, the infinitely-generated-Λ sentence, Dictionary 4 part 2). `x-06`: p. 6 (the class), pp. 8–9 (the
no-fixed-points sentence, the α = 0 sentence, the solenoid escape). `r3s-20` (Leichtnam 2013): §4 intro, (12),
Assumptions 1]–8] including (13), (14), (15), Comments 6–7, Lemma 1; full-text search for "compact". Leichtnam 2008
author copy: §5.1 Assumptions 1]–7], Comments 8–9, §5.2 Lemma 7; full-text search for "compact". `r3s-21` (Leichtnam
2007): p. 2, p. 11 ("too strong"), Lemma 6 (p. 14). `r3s-17` (ALKL memoir): Abstract, §1.1 and §1.3.1 (pp. 1–3),
§4.1.2 (p. 100). `r3s-30`: p. 2 definition of transversely simple, Theorem 1.1 and its case list, Definition 4.1.
Candel 1993 (NUMDAM scan, `candel.txt`): p. 490 (both theorems, Ruelle–Sullivan sentence), §1.1 p. 491 (definition of
lamination), pp. 497–498 (Theorem 4.1, Corollary 4.2, §4.1's first paragraph, Theorem 4.3, the averaging-sequence
sentence). KMNT (`kmnt.txt`): Definition 1.5, Lemma 1.10 with proof, Definition 1.11, Lemma 1.12. `r3s-29` (Hurder): §5
(definition of exceptional minimal set, Problems 5.1–5.6, the Duminy sentence, reference [84]). Program files:
`refute-F.md`, `refute-O.md` in full; `adjudication.md` §0, §1 A1–A8, §2, §3, §5, §6, §7, §8; ledger §15–§16 with the
enactment note.

**Recalled, not read, used in textbook form with hypotheses stated in place.** Poincaré–Hopf; the planar
Poincaré–Bendixson theorem; the uniformization theorem and the automorphism groups of D, C, Ĉ, C^*, tori; the Schwarz
lemma / Schwarz–Pick; the Baire category theorem; Zorn's lemma; Banach–Alaoglu; the Markov–Kakutani fixed-point theorem;
the Ruelle–Sullivan correspondence (positive closed leafwise-top-degree currents = invariant transverse measures) and
the duality between H̄²_F and closed 2-currents (Candel p. 490 states the correspondence; Deninger p. 33 uses the
one-dimensionality of H̄²_F in the same way); Sullivan's Hahn–Banach dichotomy (§2.4, consistency remark only);
completeness of leafwise metrics on compact laminations; Mayer–Vietoris and product neighborhoods of two-sided properly
embedded C¹ surfaces (B1′); unique factorization. None of the six verdicts depends on any of these beyond its
textbook statement.

**Not read, not relied on.** Cantwell–Conlon (Duminy's theorem is cited only through Hurder's sentence, report-level,
exactly as in the adjudication); Ghys 1995/1999; Sacksteder (named once, not used); KMNT beyond Def. 1.5, Lemma 1.10,
Def. 1.11; ALKL Theorem 1.3.10 (taken from the adjudication's quotation, bearing only on the ±1 coefficients remark);
`s14/y0-witness/adjudication.md` §0 (offered as context only); the two scout files.

**My own derivations, all labeled [ADJ-B] in place.** The six binding verdicts and the two conflict rulings of §0; the
ε_x-plus-determinant lemma of §1.1 (the archimedean term forces a source but not SO(2); the saddle is excluded by the
sign, correcting O); the transversality and Poincaré–Bendixson write-ups of §1.3; the full re-derivation of Theorem A
(A)–(D) (F's F-1, now dual-checked) including the (C4) restriction argument; Corollary A.1 (non-conformality of the
archimedean flow; new in this pass); the reconciliation of O-1 with Theorem A; the ruling that O's rescue of A-III lands
in the α = 0 class; the lamination proofs of §3.1–3.2 (both refuters had them; re-derived); the re-derivation of B1′
(F; now dual-checked); the corrected Theorem O-5 (the (0-coh) hypothesis and the clause-(iii) route to non-openness);
the convention analysis of A-I (§5.1); the re-derivation of O-6 with the sign corrected; the clause texts and ledger
wording of §5.5 and §7.

**Defects found in the inputs.** *Refuter O:* recommends clause (0) = global (31), which Theorem A(D) makes inconsistent
with a fixed point on a compact space; the frontier paragraph built on O-1 describes an empty class; "the archimedean
term compels only det = e^t, which a saddle satisfies" misses Deninger's ε_x = +1 (the saddle has ε_x = −1); a
pushforward/image convention slip in §5.1 and in O-6's intermediate line (conclusions unaffected); O-5's "K not open"
step needs X connected or the clause-(iii) route. *Refuter F:* none load-bearing; F-1(D) should say explicitly that its
final step uses (0-coh) or (0-glob) globally, not only (31) along L (F's setting supplies it). *Adjudication:* A-I's
symbolic eigen-measure hypothesis is stated in the pushforward convention while its conclusion is in the image
convention; A-II(c), A-III, table rows A2–A3, §0 items 3–4, N6–N7 and S16-4/S16-6 carry the fallen "conformal to C" and
"necessarily exists"; A-IV(γ)'s trace-class inference for compactness is undefended; the S4′ statement is used with an
α = 1 clause it does not contain.

**Nothing above was taken on trust from either refuter or from the adjudication.** Every source I cite I opened; every
step I rule on I wrote out.
