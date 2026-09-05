# BINDING ADJUDICATION — Q-S4′: is the length spectrum {log p} realizable by a foliated dynamical system?

**Program:** RH research program, direction C3-r (geometric substrate), Grossmann sweep.
**Session:** 16. **Date:** 2026-09-05. **Adjudicator:** Opus 5 (1M), binding.
**Inputs adjudicated:** `scout-O.md` (Opus 5) and `scout-F.md` (Fable 5.1), both in this directory, both read in full.
**Standing orders in force:** 1 (prior-art gate, online primary sources), 5 (no recalled theorem is evidence),
6 (Grossmann before Riemann), 7 (dual-model adjudication — this file is the ruling). U.S. English.

**Method note.** I opened every source on which either scout rests a load-bearing claim and re-read the cited
page myself; where a scout claimed a consequence, I re-derived it and checked the theorem's hypotheses against
an S4′ object. I did not count votes. Where the scouts disagree, or where both are wrong, §3 says so.
Everything labeled **[ADJ]** is my own derivation and is new to this session.

---

## §0. BINDING CLASSIFICATION AND VERDICT

### CLASSIFICATION: **INSTRUMENT**

— with two named DEAD-ENDs for specializations, one clause whose *stated rationale* is dead, and a correction
that removes the load-bearing obstruction both scouts placed at the center of their reports.

**Verdict.** S4′ is not a program invention and it is not unstudied. It is **Leichtnam's printed axiom list**:
Leichtnam 2008 (author copy, §5.1, Assumptions 1]–7]) and Leichtnam 2013 (arXiv:1307.3851, §4.1, Assumptions
1]–8]) print clause (i) verbatim ("To each prime ideal P of O_K there corresponds a **unique primitive closed
orbit** γ_P of φ^t of length log NP"), clause (ii) verbatim for closed orbits (2013, (14)), clause (iv)
verbatim (Assumption 5], "there exists a transverse measure µ"), and a fixed-point form of clause (iii)
(Assumptions 2], 7], 8]). Clause (ii) is Deninger's own ([Den05] pp. 32–33, read). **Nobody has constructed
the object, in any class, for any number field; the only solved case in print is Deninger's [De02]
elliptic-curve solenoid, whose length group is (log q)Z of rank 1 and which has no fixed point.** Both scouts
established this and I confirmed it independently (arXiv listing sweep, §1 A9).

**What print does to it, once the hypotheses are actually checked, is different from what either scout
reported.**

1. **The obstruction both scouts made central is vacuous against S4′.** Both derived, independently, that the
   closed-orbit length group of a foliated flow on a *closed 3-manifold with finitely many compact preserved
   leaves* is finitely generated, while ⟨log p⟩ has infinite rank — hence "every closed-3-manifold model is
   dead" (scout O, D-I; scout F, R2). The derivation is correct **and I confirm it** (§2 row B1). But its
   hypothesis — *the preserved leaves are finitely many and compact* — is not a theorem: it is the standing
   assumption of KMNT's Definition 1.5(i) and the consequence of ALKL's *transverse simplicity* hypothesis
   (both read this session; scout O's attribution of the finiteness to KMNT Corollary 2.2.4 is a misreading,
   §3.2). And **[ADJ] derivation A-IV below proves that no S4′ object can ever satisfy that hypothesis**: the
   archimedean leaf is non-compact, therefore not closed in the compact phase space, therefore its closure
   contains further preserved leaves. So the length-group obstruction kills a class that S4′ objects
   provably do not inhabit. **The closed-3-manifold case for S4′ is therefore NOT closed by print.** Deninger's
   own sentence "the class of compact 3-manifolds as phase spaces has to be generalized" ([Den05] p. 26) is a
   printed *expectation*; the printed *theorems* behind it (Cor. 5.5 Remarks 2 and 3, p. 24) both assume the
   flow is **everywhere transversal to F**, i.e. has no fixed points, and [x-06] p. 8's α = 0 sentence sits
   under the same standing assumption ("we assumed that φ^t had no fixed points", p. 8, read).

2. **What IS dead, and at which clause.**
   - **DEAD-END (a) — clause (i), on the KMNT/ALKL class.** No closed 3-manifold carrying a foliated flow whose
     non-transverse set is a finite union of compact leaves has closed orbits of length log p for infinitely
     many p. Confirmed; hypotheses stated exactly (§2 B1).
   - **DEAD-END (b) — clause (iii), for every compact preserved leaf, in any phase space. [ADJ] A-II.** A
     preserved leaf L with χ(L) ≠ 0 must be **non-compact**. Proof (§2 A-II, written out in full): by the
     printed fixed-point conformality ([Den05] p. 33, Fact; Leichtnam 2013 (13); 2008 (12)) every fixed point
     is a leafwise source of Poincaré–Hopf index +1; a compact leaf carrying a leafwise holomorphic structure
     is a closed orientable surface, so χ(L) = #Fix(φ)∩L forces χ(L) = 2 and L ≅ S² with exactly two sources;
     Poincaré–Bendixson on S² then produces a closed orbit inside L, contradicting clause (i) (every γ_p is
     transverse to F, because Tφ^{log p}|TF has no eigenvalue 1). Hence a compact preserved leaf carries no
     fixed point at all and has χ = 0. **This kills every realization with a compact archimedean leaf** — in
     particular, by ALKL's abstract ("there are finitely many preserved leaves, which are compact"), it kills
     S4′ on any closed manifold carrying a *transversely simple* foliated flow, independently of the
     length-group route. It also settles scout O's open "Q-S4‴ (parity)" question: the obstruction is not a
     parity accident of r₁ + r₂; it is uniform in K.
   - **DEAD-END (c) — Leichtnam's printed Assumption 2] is inconsistent with compactness. [ADJ] A-IV.**
     Leichtnam 2008 2] and 2013 2] require "the flow is transverse to all the leaves different from the one(s)
     containing the fixed point(s)", i.e. exactly one preserved leaf per archimedean place. By A-II that leaf
     is non-compact; a non-compact leaf of a compact foliated space is not closed; its closure lies in the
     (closed, saturated) non-transverse set, and every leaf of that set is preserved. So there are strictly
     more preserved leaves than Leichtnam's axiom allows. **The archimedean part of any S4′ object is never a
     single leaf: it is a compact saturated lamination of preserved leaves, containing a non-compact leaf with
     χ ≠ 0.** Leichtnam's Assumption 2] must be weakened before anyone builds against it.

3. **Clause (iv)'s stated rationale is dead, and the clause itself must be restated twice over.** The program
   posed clause (iv) as "there is a transverse measure (needed for the leafwise trace formula of
   Álvarez López–Kordyukov–Leichtnam)". By A-IV, an S4′ object never satisfies ALKL's transverse-simplicity
   hypothesis, so **the ALKL trace formula can never be the trace formula of an S4′ object** — not on a
   manifold, not anywhere. Separately, both scouts derived, correctly and independently, that a *finite,
   flow-invariant* transverse measure forces α = 0 and so is incompatible with clause (ii)'s α = 1 (§2 A-I).
   **[ADJ]** I add the missing existence half: by Candel's theorem (Ann. Sci. ENS 26 (1993) p. 490, read —
   "χ(M,µ) < 0 for every positive invariant transverse measure iff g is conformal to a metric of curvature −1;
   in particular this holds true if M has no invariant measure"), a compact surface lamination with a leaf
   conformal to C **must** carry a positive holonomy-invariant transverse measure. Clause (iii) forces such a
   leaf (χ = +1; §2 row C2). So the correct clause (iv) is not "there is a transverse measure" but
   **"the holonomy-invariant transverse measure that necessarily exists is scaled by the flow with modulus
   exactly e^{−t}"** — which is Leichtnam 2007's printed type-III_{1/q} mechanism (Lemma 6.1, Prop. 2.4, read).

4. **What survives untouched.** S4′ as the program posed it — compact foliated 3-space, leaves Riemann
   surfaces, clauses (i)–(iv) with (iv) restated — is **not killed by anything in print, and not by anything
   in this adjudication.** It is pushed into a precisely described corridor: a compact foliated space whose
   non-transverse set is a saturated lamination containing a non-compact leaf conformal to C, whose period
   group has infinite rank, whose transverse measure is holonomy-invariant and e^{−t}-scaled, and for which
   **no trace formula exists in print at all**. Whether the phase space may still be a closed 3-manifold is
   now an OPEN question, reopened by this adjudication.

**Standing order 6: does it license a construction attempt? My ruling: NO, not yet — but for a different
reason than either scout gave, and with a different next step.** Both scouts proposed a gate about the *rank*
of the length group. That gate is now the wrong one: A-IV shows the rank argument's hypothesis never applies,
so a rank construction would decide nothing about S4′. The cheap decider is now §5's **Q-S4⁗**, a question
about the *archimedean lamination*, which is decidable from the foliation literature alone and which the
sweep located an exact open problem for (Hurder's Problem 5.4, read).

---

## §1. THE CONFIRMED HIT LIST

Convention: **CONFIRMED** = I opened the source this session at the stated page and read the quoted words.
**CONFIRMED-BY-SCOUT-ONLY** = I did not open it; the claim carries only the scout's weight and is so marked.
Page numbers below are the printed page of the PDF on disk unless noted.

### 1.A Direct constructions and the printed statement of the problem

**A1. Deninger, *Arithmetic geometry and analysis on foliated spaces*, arXiv:math/0505354 = on-disk `x-20`
([Den05]). CONFIRMED, pp. 23–24, 26, 27, 32–33.**
- **Corollary 5.5, p. 23, hypotheses verbatim:** "Let X be a compact 3-manifold with a foliation F by surfaces
  having a dense leaf. Let φ^t be a non-degenerate F-compatible flow which is **everywhere transversal to F**.
  Assume that φ^t is conformal as in (20) with respect to a metric g on TF."
- **Remark 2, p. 24, verbatim:** "Actually the conditions of the corollary force α = 0 i.e. the flow must be
  isometric with respect to g. We have chosen to leave the α in the fomulation since there are good reasons to
  expect the corollary to generalize to more general phase spaces X than manifolds, where α ≠ 0 becomes
  possible i.e. to Sullivan's generalized solenoids."
- **Remark 3, p. 24, verbatim:** "One can show that the group generated by the lengths of closed orbits is a
  finitely generated subgroup of R under the assumptions of the corollary. In order to achieve an infinitely
  generated group the flow must have fixed points."
  → **Pagination correction:** both Remarks are on **p. 24**, not p. 23 (the page break falls inside Remark 1).
  Scout F is right; scout O's citation is off by one page. Cite p. 24.
  → **Scope, which matters:** both Remarks are *under Corollary 5.5's hypotheses*, which include "everywhere
  transversal to F". They say nothing about a flow with fixed points. See §3.1.
- **p. 26, dictionary, verbatim:** "finite place p ≙ closed orbit γ = γ_p not contained in a leaf and hence
  transversal to F such that l(γ_p) = log N p and ε_{γ_p}(k) = 1 for all k ≥ 1"; "infinite place p ≙ fixed
  point x_p such that κ_{x_p} = κ_p and ε_{x_p} = 1." → clauses (i) and (iii) in Deninger's own words.
- **p. 26, the desideratum, verbatim:** "In order to understand number theory more deeply in geometric terms
  it would be very desirable to find a system (X, φ^t, F) which actually realizes this correspondence. For
  this the class of compact 3-manifolds as phase spaces has to be generalized as will become clear from the
  following discussion."
- **p. 27, verbatim:** "in a dynamical system corresponding to number theory we must have α = 1. … However as
  mentioned before, this is not possible in the manifold setting of corollary 5.5 which actually implies
  α = 0."
- **pp. 32–33, the Fact, verbatim (clause (ii), Deninger's own):** "ε_k(γ) = +1 for all k ∈ Z∖0 if and only if
  on T_xF we have: T_xφ^{kl(γ)} = e^{(k/2)l(γ)}·O_k for O_k ∈ SO(T_xF). **For fixed points, ε_x = 1 is
  automatic and we have: T_xφ^t = e^{t/2}O_t for O_t ∈ SO(T_xF).**" And: "In the number theoretical case the
  eigenvalues of T_xφ^{log N p} on T_xF for x ∈ γ_p would therefore be complex conjugate numbers of absolute
  value N p^{1/2}."  → **the second sentence is the hypothesis my derivation A-II runs on.**
- **p. 33, Remark 7, verbatim:** "If there does exist a foliated dynamical system attached to spec o_K with the
  properties dictated by our considerations we would expect in particular that for a preferred transverse
  measure µ we have: χ_Co(F, µ) = − log|d_{K/Q}|. … In the unramified case, |d_{K/Q}| = 1 we must have
  χ_Co(F, ν) = 0 for all transverse measures by the above argument. Hence there is an F-leaf which is either a
  plane, a torus or a cylinder c.f. [9]."  ([9] = Candel.) → this is an *expectation*, flagged as such by
  Deninger's own "we would expect". Both scouts used it; both marked it correctly.
- **p. 26, Fact 6.1 (Connes), verbatim:** "Let F be a foliation of a compact 3-manifold by surfaces such that
  the union of the compact leaves has µ-measure zero, then χ_Co(F, µ) ≤ 0."
- **§7.7, Thm 7.8 and the p. 36 Example** (the one solved case; X = M̄ ×_Λ R, Λ = lZ, the ordinary elliptic
  curve with α = 1 conformality). **CONFIRMED-BY-SCOUT-ONLY** (both scouts read it; I did not re-open §7.7).
  Rank-1 length group, no fixed points: fails clauses (i) and (iii) by an infinite margin.

**A2. Deninger, *Analogies between analysis on foliated spaces and arithmetic geometry*, arXiv:0709.2801 =
on-disk `x-18`, LMS LNS 354 (2008), p. 3–4. CONFIRMED.**
- Construction 3, verbatim: "let ω_φ be the one-form on X defined by ω_φ|TF = 0 and ⟨ω_φ, Y_φ⟩ = 1. **One
  checks that dω_φ = 0 and that ω_φ is φ^t-invariant** i.e. φ^{t*}ω_φ = ω_φ for all t ∈ R. We may view the
  cohomology class ψ = [ω_φ] in H¹(X, R) … as a homomorphism ψ : π₁^{ab}(X) → R. Its image Λ ⊂ R is called the
  group of periods."
- verbatim: "**It is known that F is a fibration if and only if rank Λ = 1.**"
- p. 4, verbatim: "So the foliation setting allows for a product formula where the Nγ are not all powers of
  the same number. **If one wants an infinitely generated Λ, one must allow the flow to have fixed points**
  (≙ infinite places)."
- Dictionary 4, verbatim: "X(C)/F_∞ … ≙ set of fixed points of φ^t. **Note that the leaf of F containing a
  fixed point is φ-invariant.**"
  → **Ruling on a scout disagreement:** scout O quoted these sentences as read; scout F wrote that he could not
  re-locate them in this pass and quoted them from the program record. **Scout O is right; the sentences are
  there, verbatim, on pp. 3–4.** Note also that Construction 3 is stated for triples "as in the dictionary
  above", where the flow is transverse to F; with fixed points ω_φ exists only off the preserved leaves.

**A3. Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643 = `x-06`, pp. 7–9, 11. CONFIRMED
(pp. 8–9 re-read by me; pp. 7 and 11 CONFIRMED-BY-SCOUT-ONLY, quoted identically by both scouts).**
- p. 8, verbatim, **with its standing assumption, which both scouts dropped**: "Formula (9) does not contain a
  term corresponding to (1−e^{−2t})^{−1} in (8) because **we assumed that φ^t had no fixed points**. If we
  allow fixed points, then the distributional trace defined above may no longer exist. … One can show that the
  conformal factor e^{αt} for a metric g_F as above necessarily has to be 1, i.e. α = 0 … This is only one
  instance which shows that the class of smooth compact manifolds is too restrictive…"
- p. 9, verbatim: "One can show that α = 1 can be achieved if for X we allow the local structure (totally
  disconnected) × (3-dimensional ball), c.f. [Lei07]."
- p. 7 (open, by name): "The question whether a natural dynamical system with this property exists is quite
  old…"; p. 11: "the dynamical system (X₀, φ^t) has too many periodic orbits".

**A4. Leichtnam, *Scaling group flow and Lefschetz trace formula for laminated spaces with p-adic transversal*,
arXiv:math/0603576v2 = Bull. Sci. Math. 131 (2007) 638–669 = on-disk `r3s-21`. CONFIRMED, pp. 2, 13, 17.**
- p. 2, verbatim: "1) A Riemannian foliated space of the form (S_Q = L×R^{+*}/Q^{+*} ∪ L/Q^{+*}, F, g) where L
  is a **σ-compact** complex 1-dimensional laminated space on which Q^{+*} acts. … 2) A flow φ^t acting on
  (S_Q …, F) whose **primitive closed orbits correspond to the primes of Q and admitting a fixed point in
  L/Q^{+*}**. The action of φ^t on the L-leaf space R^{+*}/Q^{+*} ∪ {pt} should be given by φ^t([x]) = [e^{−t}x]
  and φ^t(pt) = pt. Moreover (φ^t)_*[λ_g] = e^t[λ_g] … The quotient L/Q^{+*} allows to **compactify** the space
  L×R^{+*}/Q^{+*}. … **Notice that the existence of such a quadruple (S_Q, F, g, φ^t) is still unknown.**"
- p. 2, verbatim: "Notice nevertheless that A_Q×R/Q^* does not satisfy the properties required for
  (S_Q, F, g, φ^t)."  → Leichtnam himself rules out the Connes adele-class space as a candidate.
- **The flow is NOT a plain suspension**, verbatim, p. 2: "φ^t(l, x) = (ψ_x^t(l), x e^{−t})." → this matters
  for §3.4.
- p. 13, axioms (i)–(ii), verbatim: "M_q ∈ M_m(Z_p) ∩ GL_m(Q_p) is such that **Jac M_q = 1/q**"; "for any l ∈ L
  one has: ∀u ∈ T_lL, **g̃(q_*(u)) = q g̃(u)**."  → the printed α = 1 mechanism: leafwise metric multiplied by q,
  transverse p-adic Haar measure divided by q.
- p. 17, Open Question 2 1], verbatim (function-field case only): "Does there exist a laminated foliated space
  (S_Y = L_Y×R^{+*}/q^Z, F, g, φ^t) satisfying all the assumptions of Proposition 2 and Theorem 2 and the
  following assumption: (A) One has a natural bijection w ↦ γ_w between the set of closed points of Y and the
  set of primitive closed orbits of (S_Y, φ^t) satisfying log Nw = l(γ_w)."

**A5. Leichtnam, *On the analogy between arithmetic geometry and foliated spaces* — author copy dated
27 Nov 2008, recovered from the Wayback Machine by scout F and saved in this directory. CONFIRMED, §5.1.**
Scout F identifies this with Rend. Mat. Appl. (7) 28 (2008) 163–188. **I could not verify that identification**
(the running head of the recovered file is "TALK"; journal pagination unverified; the journal server is dead —
§4). Content, verbatim, §5.1 Assumptions:
- **1]** "The leaves are Riemann surfaces and the path connected components of S_Q are three dimensional.
  Moreover, g denotes a leafwise riemannian metric, (φ^t)_{t∈R} is a flow acting on (S_Q, F) and permuting the
  leaves."
- **2]** "To each prime p ∈ P there corresponds a **unique primitive closed orbit γ_p of φ^t of length log p**.
  To the archimedean absolute value of Q there corresponds a **unique fixed point x_∞** = φ^t(x_∞), ∀t ∈ R, of
  the flow. **The flow is transverse to all the leaves different from the one containing x_∞.**"
- **3]** "(12) ∀t ∈ R, e^{−t/2} D_yφ^t(x_∞)|T_{x_∞}F ∈ SO₂(T_{x_∞}F)."
- **5]** "there exists a **transverse measure µ** on (S_Q, F) such that ∫_{S_Q}(α ∧ ⋆β)µ defines a scalar
  product on H̄¹_F."
- **7]** "The fixed point x_∞ ∈ S_Q should be a **limit point of a trajectory γ_∞**: lim_{t→+∞} φ^t(y) = x_∞ …
  Lastly we require that γ_∞ is transverse at x_∞ to T_{x_∞}F." (with the R≥0-orbifold structure v ↦ ve^{−2t},
  i.e. the κ = −2 of the archimedean term).
- **Comment 8**, verbatim: "Deninger told us privately that this assumption (φ^t)^*(g) = e^t g might be too
  strong."
- **Note:** the 2008 list does **not** print the closed-orbit derivative (clause (ii)); only the fixed-point
  version (12). Scout F is right about this and scout O did not report the 2008 list at all.

**A6. Leichtnam, *On the analogy between L-functions and Atiyah–Bott–Lefschetz trace formulas for foliated
spaces*, arXiv:1307.3851v1 = on-disk `r3s-20`, §4.1. CONFIRMED, printed pp. 14–16.** This is the single most
important hit of the whole sweep and **scout O missed it entirely**. Verbatim:
- **2]** "To each prime ideal P of O_K there corresponds a **unique primitive closed orbit γ_P of φ^t of length
  log NP**. There is a bijection between the set S_∞ of archimedean absolute values and the set of fixed point
  y_∞ = φ^t(y_∞), ∀t ∈ R, of the flow. **Each leaf contains at most one fixed point and the flow is transverse
  to all the leaves different from the ones containing the r₁ + r₂ fixed points.**"
- **3] a) (13)** "∀t ∈ R, e^{−t/2} D_yφ^t(y_∞)|T_{y_∞}F ∈ SO₂(T_{y_∞}F)."
- **3] b) (14)** "For any prime P of O_K and any x̃ ∈ γ_P: **e^{−(log NP)/2} D_yφ^{log NP}(x̃)|T_x̃F ∈
  SO₂(T_x̃F)**."  → **clause (ii) verbatim, in print, since 2013.**
- **5]** "there exists a transverse measure µ on (S_K, F) such that ∫(α ∧ ⋆β)µ defines a scalar product on
  H̄¹_{F,K}."  → clause (iv) verbatim.
- **4] (15)** "(φ^t)^*([λ_g]) = e^t[λ_g]"; **7], 8]** the real/complex archimedean fixed points as limits of
  trajectories transverse to F.
→ **Consequence for the program's novelty record: the Session-14 C10 verdict "PARTIAL for the four sharpened
clauses" is wrong and must be corrected to: (i) ANTICIPATED (Leichtnam 2008 2], 2013 2]); (ii) ANTICIPATED
(Leichtnam 2013 (14); Deninger [Den05] p. 33); (iv) ANTICIPATED (Leichtnam 2008 5], 2013 5]); (iii) PARTIAL
(the preserved leaf and the accumulating trajectory are printed — 2008 7], 2013 7]–8]; "χ(L) ≠ 0" and
"the leaf lies in the accumulation set of the closed orbits" are the program's own sharpening).** Scout F
found this; I confirm it; it is binding.

**A7. Álvarez López–Kordyukov–Leichtnam, *A trace formula for foliated flows*, arXiv:2402.06671v1 = on-disk
`r3s-17`. CONFIRMED: Abstract, §§1.2–1.3, Theorem 1.3.10 (memoir p. 8), §4.1.2 (memoir p. 100).**
- **Abstract, verbatim:** "Let F be a transversely oriented foliation of codimension one on **a closed
  manifold M**, and let φ = {φ^t} be a foliated flow on (M, F). Assume the closed orbits of φ are simple and
  **its preserved leaves are transversely simple. In this case, there are finitely many preserved leaves,
  which are compact.**"
- **§4.1.2, memoir p. 100, verbatim:** "Suppose φ is transversely simple unless otherwise stated. **Then M⁰ is
  a finite union of compact leaves because every fixed point of φ̄ is isolated.**"
  → the finiteness and compactness are **consequences of the transverse-simplicity hypothesis**, not free.
- **Theorem 1.3.10, memoir p. 8, verbatim:** "Using the preserved leaves L and the closed orbits c, we have
  L_dis(φ) = Σ_L χ(L) W_L + ^bχ_{|ω¹|}(F¹) δ₀ + Σ_c ℓ(c) Σ_{k∈Z^×} ε_c(k) δ_{kℓ(c)}."
  With, memoir p. 7, verbatim: "L_dis,K,K′(φ) = Σ_L χ(L)/|e^{κ_L t} − 1|" and Barlet's regularization
  ⟨W_L, f⟩ = ∫₀^∞ ((f(t)+f(−t))/|e^{κ_L t}−1| − 2f(0)/(|κ_L| t)) dt.
- **§1.1, memoir p. 1, verbatim:** "It became clear that more generality is needed to draw arithmetic
  consequences (perhaps foliated flows on possibly singular foliated spaces of arithmetic nature)."
- **The closed-orbit coefficients are the signs ε_c(k) ∈ {±1}**, i.e. the α = 0 shape, not the arithmetic
  N p^k shape of [Den05] p. 27. Scout F saw this and stated it; scout O did not.
- **[ADJ] Binding consequence (§2 A-IV):** an S4′ object never satisfies "preserved leaves transversely
  simple", so ALKL's theorem never applies to it. The program's clause (iv) rationale must be rewritten.

**A8. Kim–Morishita–Noda–Terashima, *On 3-dimensional foliated dynamical systems and Hilbert type reciprocity
law*, arXiv:1906.02424 = Münster J. Math. 14 (2021). CONFIRMED (PDF fetched and read this session: Def. 1.5,
Lemma 1.10, Def. 1.11, Thm. 2.2.2, Cor. 2.2.4, Prop. 2.2.5).**
- **Definition 1.5, verbatim:** "(1) M is a connected, closed smooth 3-manifold, (2) F is a complex foliation by
  Riemann surfaces on M, (3) φ is a smooth dynamical system on M, and these data must satisfy … **(i) there are
  finite number of compact leaves L^∞_1, …, L^∞_r, which may be empty, such that for any i and t we have
  φ^t(L^∞_i) = L^∞_i and that any orbit of the flow φ is transverse to leaves in M ∖ ∪L^∞_i**; (ii) for each
  t ∈ R the diffeomorphism φ^t of M maps any leaf to a leaf."
  → **finiteness and compactness of the preserved leaves are a HYPOTHESIS of the definition.**
- **Lemma 1.10, verbatim:** "For an FDS³ S = (M, F, φ), there is the unique closed smooth 1-form ω on M₀
  satisfying (C) ω|TF = 0, ω(φ̇^t) = 1."  M₀ := M ∖ L^∞.
- **Definition 1.11, verbatim:** "the period homomorphism [ω_S] : H₁(M₀; Z) → R; [ℓ] ↦ ∫_ℓ ω_S, and the period
  group of S is defined by the image of [ω_S], which we denote by Λ_S."
- **Theorem 2.2.2, verbatim:** "(1) X_a is a surface bundle over S¹ or an open interval, and F|X_a is the
  bundle foliation. (2) X_a is a surface-bundle over S¹ and any leaf in F|X_a is dense in X_a."
- **Corollary 2.2.4 III, verbatim:** "P_S^∞ is a non-empty (finite) set."
  → **the "(finite)" is Definition 1.5(i)'s hypothesis restated, not a theorem.** Scout O cited Cor. 2.2.4 as
  *proving* finiteness (his D-I step 3). That is a misreading; §3.2 rules on it.
- **Proposition 2.2.5, verbatim:** "If S is of type I or of type III-1, then the period group Λ_S = Z.
  Conversely, if the Λ_S has rank one … and M₀ is connected, then S is of type I or of type III-1."

**A9. Coverage of the post-2019 literature. CONFIRMED independently.** I ran the arXiv API on
`all:"foliated dynamical system" OR all:"foliated flow"`, newest first, 40 rows. Every post-2019 hit is one of:
2508.15971 (Morishita, Deninger↔Connes–Consani bridge), 2410.20758 (Álvarez López–Kim–Morishita, regularized
determinants), 2402.06671 (ALKL trace formula), 1912.02159 (Kim), 1906.06753 (ALKL, *Simple foliated flows*),
1906.02424 (KMNT), plus one unrelated Coulomb-gas paper. **None constructs a foliated system whose closed
orbits are indexed by the primes.** This agrees with both scouts' independent citing-set sweeps (scout O:
Semantic Scholar citation lists of 1807.06400, 2301.11643, math/0505354; scout F: OpenAlex `cites:` for eleven
works plus Semantic Scholar for Bull. Sci. Math. 131). **Ruling: the coverage claim is dual-checked and I add a
third check. No construction attempt exists in print, 2019–2026.**

**A10. Morishita, arXiv:2508.15971v5, and Connes–Consani, *The Scaling Site* / *Knots, primes and the adele
class space*. CONFIRMED-BY-SCOUT-ONLY (both scouts read the abstracts; scout O read Morishita pp. 1–6).**
The scaling site carries a flow with one distinguished periodic orbit C_p ≅ R/(log p)Z per prime — the orbit
*spectrum* of clause (i) — but is a non-Hausdorff/noncommutative quotient with no 2-dimensional leafwise
Riemann-surface structure, no p^{1/2} return derivative and no transverse measure. Leichtnam's own printed
verdict (A4, p. 2, CONFIRMED) settles it: "A_Q×R/Q^* does not satisfy the properties required for
(S_Q, F, g, φ^t)." Both scouts' claim that C_p is not the *unique* closed orbit of its length is a judgment
from the definition of the scaling action, not a printed statement; I leave it at that weight.

### 1.B–1.E Inverse problems, rigidity, counting, trace formulas — the short ruling

I confirm both scouts' negative findings and add nothing to them except scoping.

- **Inverse period-set results.** Nothing in print constrains which subsets of R_{>0} are the primitive-period
  sets of a *flow* on a compact foliated 3-space. The two positive results located — de Jong, "On sets of
  periodic orbit lengths in finitely presented dynamical systems", *Ergodic Theory and Dynamical Systems*,
  published online 15 June 2026, DOI 10.1017/etds.2026.10313 (existence and date CONFIRMED via Cambridge Core
  search this session; abstract CONFIRMED-BY-SCOUT-ONLY) and the rank-one/common-period Reeb results
  (Cristofaro-Gardiner–Mazzucchelli, Comment. Math. Helv. 95 (2020); Miyanishi, arXiv:2408.06056) — are for
  discrete-time finitely presented systems and for rank-one contact spectra respectively. **Neither constrains
  S4′.** Both scouts reached this; I agree.
- **Seifert-conjecture technology (Wilson plugs, Schweitzer, Harrison, K. Kuperberg; Ghys, Sém. Bourbaki 785,
  read by scout F).** Gives arbitrary *finite* prescribed orbit sets on any closed 3-manifold and, per Ghys
  pp. 295–296 (CONFIRMED-BY-SCOUT-ONLY), no Poincaré–Hopf-type global index theorem for periodic orbits. Plugs
  are foliation-destroying; silent in the foliated category. **No constraint on S4′; no construction either.**
- **Periodic-data rigidity (Kalinin–Sadovskaya, de la Llave–Marco–Moriyón, Gogolev, Gogolev–Rodriguez Hertz).**
  **Hypotheses fail.** By clause (ii) both leafwise eigenvalues at γ_p have modulus p^{1/2} > 1 and the flow
  direction is neutral, so **every γ_p is a source**, the stable bundle is empty, and the flow is neither
  Anosov nor Axiom A with a contracting direction. Every theorem in this family is stated over a transitive
  Anosov base. **Ruling: this family neither constrains nor kills S4′.** (Both scouts; I re-derived the source
  property from [Den05] p. 33, which I read.) The one *positive* use — Kalinin–Sadovskaya's "conformal periodic
  data ⟹ globally conformal cocycle" (arXiv:1008.2563 abstract, CONFIRMED-BY-SCOUT-ONLY) — is a genuinely
  useful design heuristic but its Anosov hypothesis does not hold, so it is not evidence.
- **Counting.** #{γ : ℓ(γ) ≤ T} = π(e^T) ∼ e^T/T is exactly the Margulis/Parry–Pollicott asymptotic
  e^{hT}/(hT) at h = 1. **No obstruction; entropy 1.** The Parry–Pollicott asymptotic is *recalled* by both
  scouts and by me; nothing rests on it.
- **Ruelle zeta / Fried's conjecture (Dyatlov–Zworski; Cekić–Delarue–Dyatlov–Paternain; Dang–Guillarmou–
  Rivière–Shen; Cekić–Paternain; Chaubet–Dang).** An S4′ object would have ζ_R(s) = ζ(s) identically, hence
  ord_{s=0} ζ_R = 0 and ζ_R(0) = −1/2. Every theorem in the Fried family assumes an **Anosov (usually contact
  Anosov) flow on a closed manifold**; by the source property above, S4′'s flow is neither. **Ruling:
  INSTRUMENT-shaped, inapplicable; it is the right place to look for a future obstruction and no
  foliated-space version exists in print.** Both scouts; I agree.
- **Fuller index.** The closed-orbit set of an S4′ object accumulates on the archimedean lamination, so it is
  not an isolated compact invariant set and no Fuller index of the whole set can be formed; at a single γ_p
  the index is +1 for every iterate (det(1 − p^{k/2}O_k) = |1 − p^{k/2}e^{ikθ}|² > 0). **No constraint.** Both
  scouts; I agree.
- **Deninger, *There is no Weil-cohomology theory with real coefficients for arithmetic curves*,
  arXiv:2204.02714 = `x-04`.** Bears on the *payoff*, not on existence: leafwise cohomology always carries a
  real structure, and the arithmetic H¹ cannot. **Downstream constraint, recorded, not an obstruction.**

---
