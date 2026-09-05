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

## §2. THE BINDING CONSTRAINT TABLE, WITH HYPOTHESES CHECKED

The four derivations the table cites are written out in full first. Each uses only statements I read this
session, and each states its hypotheses so that the program can check whether an S4′ object satisfies them.
**A-I is a corrected joint form of scout O's D-III and scout F's R1 (dual-check). B1 is a corrected joint form
of scout O's D-I and scout F's R2 (dual-check). A-II, A-III and A-IV are mine (single-check).**

### A-I. The conformal factor equals the modulus of the transverse measure. [dual-check, corrected]

*Statement.* Let X be a **compact** foliated space with 2-dimensional leaves, g a leafwise Riemannian metric
continuous on X, φ^t a foliated flow with g(Tφ^t v, Tφ^t w) = e^{αt} g(v, w) on TF ([Den05] (20)/(31)), and µ a
holonomy-invariant transverse measure, finite on transversals, with φ^t_*µ = e^{−βt}µ for some β ∈ R. Then
**α = β**.

*Proof.* Let m = vol_g ⊗ µ be the induced measure on X: on a foliated chart B² × T it is (leafwise area of g)
⊗ µ. Compactness of X plus continuity of g plus finiteness of µ on transversals give 0 < m(X) < ∞ (finitely
many charts of finite mass). The flow scales leafwise areas by e^{αt} and pushes the transverse factor by
holonomy composed with the transverse flow, so m(φ^t A) = e^{αt} e^{−βt} m(A) for Borel A. Take A = X: since
φ^t(X) = X, m(X) = e^{(α−β)t} m(X) for all t, and 0 < m(X) < ∞ forces α = β. ∎

*Hypotheses checked against an S4′ object.* X compact ✓ (clause of S4′). g leafwise, continuous ✓. α = 1
required ✓ ([Den05] p. 27, read; it is what produces the N p^k coefficients and, via the Fact of pp. 32–33, the
p^{1/2} of clause (ii)). µ finite on transversals ✓ on a compact lamination. **So β = 1: the transverse measure
of an S4′ object is scaled by the flow with modulus exactly e^{−t}, and the return map along γ_p scales it by
exactly 1/p.**

*What this re-derives and what it corrects.* It re-derives Deninger's printed Remark 2 ([Den05] p. 24) in the
one case where the transverse measure is forced to be flow-invariant: on a closed 3-manifold with φ everywhere
transverse to F, the canonical measure is |ω_φ| and ω_φ is **φ-invariant** ([x-18] Construction 3, read,
verbatim: "ω_φ is φ^t-invariant"), so β = 0 and α = 0. **It also shows exactly where that argument stops:**
in the presence of preserved leaves ω_φ exists only on M ∖ M⁰ and has infinite mass there (ALKL's b-density,
memoir §1.3, read), so m(X) = ∞ and the argument gives nothing. Deninger says as much on [x-06] p. 8
("we assumed that φ^t had no fixed points"). Leichtnam's printed mechanism is the β = 1 case: Jac M_q = 1/q
against g̃(q_*u) = q g̃(u) (r3s-21 p. 13, read).

*Correction to the program's clause (iv):* "there is a transverse measure" is not the right clause. The right
clause is **"the holonomy-invariant transverse measure is scaled by the flow with modulus e^{−t}"** — never
flow-invariant with finite mass.

### A-II. A preserved leaf with χ ≠ 0 is non-compact. [ADJ, single-check]

*Statement.* Let (X, F, φ) be a compact foliated space with 2-dimensional leaves carrying a leafwise
holomorphic structure, satisfying S4′ clause (i) (every closed orbit of φ is one of the γ_p, and each γ_p
satisfies clause (ii)) and the printed fixed-point conformality **(ii∞)**: at every fixed point x of φ,
e^{−t/2} T_xφ^t|T_xF ∈ SO(T_xF) ([Den05] p. 33, Fact, read; Leichtnam 2013 (13), read; 2008 (12), read).
Then **every compact preserved leaf L has χ(L) = 0 and contains no fixed point.** In particular a preserved
leaf with χ(L) ≠ 0 — clause (iii)'s leaf — is **non-compact**.

*Proof.* Let L be a compact preserved leaf. Y_φ is tangent to L (φ^t(L) = L), so Y_φ|L is a vector field on the
closed surface L, and its zero set is Fix(φ) ∩ L.
(1) *L is a closed orientable surface.* The leafwise holomorphic structure orients L; L compact and without
boundary. So χ(L) = 2 − 2g ∈ {2, 0, −2, −4, …}.
(2) *Every zero is a source of index +1.* By (ii∞), T_xφ^t|T_xF = e^{t/2}O_t with O_t ∈ SO(2). Differentiating
at t = 0, the linearization of Y_φ|L at x is (1/2)·Id + S with S skew, whose eigenvalues are 1/2 ± iθ. Both
have positive real part, so x is a hyperbolic source of the leafwise flow, isolated, with Poincaré–Hopf index
+1.
(3) *If Fix(φ) ∩ L = ∅* then Y_φ|L is nowhere zero on the closed surface L, so χ(L) = 0 by Poincaré–Hopf.
(4) *If Fix(φ) ∩ L ≠ ∅* then by Poincaré–Hopf χ(L) = Σ_{x ∈ Fix∩L} index(x) = #(Fix ∩ L) ≥ 1. Combined with
(1), the only possibility is **χ(L) = 2, i.e. L ≅ S², with exactly two fixed points, both sources.**
(5) *That case is impossible.* Take any y ∈ L which is not a fixed point. Its ω-limit set ω(y) ⊂ L is nonempty
(L compact), compact, connected and invariant. A source p cannot lie in ω(y) for y ≠ p: a hyperbolic source has
a neighborhood U with ∩_{t ≤ 0} φ^t(U) = {p}, so φ^{t_n}(y) → p with t_n → +∞ forces y = p. Hence ω(y) contains
no zero. By the Poincaré–Bendixson theorem on S² (valid there; the flow is C¹ with finitely many zeros), an
ω-limit set containing no zero is a **closed orbit**. That closed orbit lies inside the leaf L, hence is a
closed orbit of φ contained in a leaf. But clause (i) says the closed orbits of φ are exactly the γ_p, and each
γ_p is **transverse to F**: if γ_p ⊂ leaf then Y_φ ∈ TF along γ_p and Tφ^{log p}|TF fixes the flow direction,
giving eigenvalue 1, contradicting clause (ii)'s "both eigenvalues of modulus p^{1/2}". Contradiction. ∎

*Corollaries.*
(a) **Under Deninger's dictionary for K = Q** ([Den05] p. 26, read: exactly one infinite place ≙ exactly one
fixed point) or **Leichtnam's axiom "each leaf contains at most one fixed point"** (2013 2], read), step (4)
already gives χ(L) = 1 for a compact archimedean leaf, which no closed orientable surface has. The obstruction
is therefore **uniform in the number field**, not a parity accident of r₁ + r₂ — this settles scout O's
proposed open question "Q-S4‴ (parity)" in the negative sense he hoped for.
(b) **No closed manifold with a transversely simple foliated flow realizes S4′.** By ALKL's Abstract (read),
transverse simplicity on a closed manifold forces the preserved leaves to be finitely many and **compact**;
by A-II each then has χ = 0; clause (iii) demands one with χ ≠ 0. **Clause (iii) fails.** This is independent
of the length-group route (B1) and does not use the ALKL trace formula at all.
(c) Combined with [Den05] p. 33 Remark 7 (read: for K = Q, χ_Co(F, ν) = 0 for all transverse measures, hence a
leaf that is a plane, a torus or a cylinder) and Candel Theorem 4.3 (read: the non-hyperbolic leaves are the
sphere, torus, plane, cylinder), and since torus and cylinder have χ = 0 and the sphere is compact (excluded by
A-II), **clause (iii)'s leaf is conformal to the euclidean plane C, with χ = +1** — which is also the value the
ALKL weight χ(L) would need in order to reproduce the archimedean coefficient r₁ = 1 of the explicit formula.

### A-III. A holonomy-invariant transverse measure necessarily exists. [ADJ, single-check]

*Statement.* An S4′ object carries a positive holonomy-invariant transverse measure.

*Proof.* Candel, *Uniformization of surface laminations*, Ann. Sci. École Norm. Sup. (4) 26 (1993) 489–516,
p. 490, first theorem, verbatim (read this session, numdam scan): "Let M be a compact oriented surface
lamination with a riemannian metric g. Then χ(M, µ) < 0 for every positive invariant transverse measure if and
only if g is conformal to a metric of curvature −1. **In particular, this holds true if M has no invariant
measure.**" If the S4′ object had no positive invariant transverse measure, its leafwise metric would be
conformal to one of curvature −1, so **every** leaf would be a hyperbolic Riemann surface — contradicting
A-II(c), which puts a leaf conformal to C in the object. ∎

*Why this matters.* Together with A-I it says: an S4′ object **must** carry a finite holonomy-invariant
transverse measure, and the flow **must** scale it by e^{−t}. Clause (iv) is therefore not an extra axiom to be
arranged; its existence half is automatic and its content is the *modulus*. Neither scout had this half.

### A-IV. The archimedean part is never one leaf, and never finitely many compact ones. [ADJ, single-check]

*Statement.* Let (X, F, φ) be an S4′ object: X **compact** (and Hausdorff, as a foliated space), leaves
2-dimensional and leafwise holomorphic, clauses (i), (ii), (ii∞), (iii). Let N := {x ∈ X : Y_φ(x) ∈ T_xF} be
the non-transverse set. Then:
1. N is closed and F-saturated, and every leaf contained in N is preserved by φ.
2. The leaf L of clause (iii) is non-compact (A-II), hence **not closed in X**, hence L̄ ∖ L ≠ ∅.
3. L̄ ⊆ N, and L̄ ∖ L is a nonempty union of leaves, **all of them preserved**.
Consequently **the preserved-leaf set of an S4′ object contains at least two leaves, at least one of them
non-compact, and it is never a finite union of compact leaves.**

*Proof.* (1) In a foliated chart U ≅ B² × T the flow induces a continuous local transverse flow on T, whose
generating transverse component is a continuous function on T; N ∩ U is its zero set, hence closed in U, and
N is F-saturated because that transverse component depends only on the plaque (φ^t maps leaves to leaves, so
the induced map on the local leaf space is well defined). If a leaf L′ lies in N then Y_φ is tangent to L′
everywhere on L′, so the integral curves of Y_φ through points of L′ stay in L′ (a leaf is a maximal integral
manifold of TF), giving φ^t(L′) = L′.
(2) If a leaf L′ is closed as a subset of X, then L′ is compact in the subspace topology (a closed subset of a
compact space), and for a closed leaf the leaf topology and the subspace topology agree (a closed leaf is
proper: each plaque chain meeting a small transversal meets it in a set with no accumulation point in L′), so
L′ is compact as a surface. Contrapositively, L is non-compact by A-II, hence not closed in X, hence L̄ ⊋ L.
(3) L ⊆ N because L is preserved, and N is closed, so L̄ ⊆ N. The closure of a leaf is F-saturated, so L̄ ∖ L is
a union of leaves; each lies in N, hence is preserved by (1). ∎

*Three binding consequences.*
- **(α) The ALKL trace formula can never apply to an S4′ object.** Its standing hypothesis is that the preserved
  leaves are transversely simple, which forces them to be finitely many and compact (Abstract and §4.1.2, read).
  A-IV says an S4′ object never satisfies that. **So clause (iv) as the program worded it — "a transverse
  measure (needed for the leafwise trace formula of Álvarez López–Kordyukov–Leichtnam)" — rests on a false
  premise, and the program's expected payoff route through ALKL is closed.** This is the single most consequential
  finding of the adjudication.
- **(β) The length-group DEAD-END (B1) is vacuous against S4′.** Its hypothesis is exactly "the non-transverse
  set is a finite union of compact leaves" (KMNT Def. 1.5(i); ALKL transverse simplicity). A-IV says an S4′
  object never satisfies it. So B1 kills a class S4′ objects cannot inhabit. **The closed-3-manifold case for
  S4′ is reopened.** Both scouts' headline obstruction does not do the work they assigned it.
- **(γ) Leichtnam's printed Assumption 2] is inconsistent with compactness.** "The flow is transverse to all the
  leaves different from the one(s) containing the r₁ + r₂ fixed points" (2008 2], 2013 2], read) says N is
  exactly those leaves; A-IV says N properly contains them. Since Leichtnam does not print "S_Q is compact" in
  the axiom list itself (I checked: the word does not occur in §5.1 of the 2008 author copy), the list is not
  *literally* self-contradictory — but compactness is required by his own Assumption 6] (trace-class) and by
  the S4′ statement, and with it the list is inconsistent. **Anyone building against Leichtnam's list must
  weaken 2] first.**

### B1. The length group is finitely generated when the preserved leaves are finitely many and compact. [dual-check, hypotheses corrected]

*Statement.* Let M be a closed 3-manifold, F a codimension-one foliation by surfaces, φ a foliated flow whose
non-transverse set L^∞ is a **finite union of compact leaves** (KMNT Def. 1.5(i); or ALKL transverse simplicity
on a closed manifold). Put M₀ = M ∖ L^∞. Then the group generated by the lengths of the closed orbits of φ in
M₀ is finitely generated; hence clauses (i)+(ii) are unrealizable on M.

*Proof.* (1) KMNT Lemma 1.10 (read): there is a unique closed smooth 1-form ω on M₀ with ω|TF = 0 and
ω(φ̇) = 1; KMNT Def. 1.11 (read): Λ = [ω](H₁(M₀; Z)). (2) For a closed orbit c ⊂ M₀ of least period ℓ(c),
∫_c ω = ∫₀^{ℓ(c)} ω(φ̇) dt = ℓ(c), so ℓ(c) ∈ Λ. (3) L^∞ is a finite disjoint union of closed embedded surfaces,
so cutting M along L^∞ yields a **compact** 3-manifold with boundary M̄ whose interior is homeomorphic to M₀;
hence M₀ is homotopy equivalent to a finite CW complex and H₁(M₀; Z) is finitely generated, so Λ is a finitely
generated subgroup of R. (4) Every γ_p lies in M₀: a closed orbit inside a leaf would give Tφ^{ℓ}|TF the
eigenvalue 1 along the orbit direction, contradicting clause (ii). (5) {log p} is Z-linearly independent (if
Σ n_p log p = 0 then Π p^{n_p} = 1, so all n_p = 0 by unique factorization), so ⟨log p⟩ has infinite rank.
(2)+(3)+(4)+(5) contradict. ∎

*Ruling on the two scouts' versions.* Both derived this independently; the derivations agree and are correct.
**Scout F states the hypothesis correctly and flags the loophole; scout O states the conclusion without the
hypothesis ("no 3-dimensional foliated dynamical system on a closed 3-manifold has closed orbits of length
log p for infinitely many primes p"), which is not what the argument proves, and attributes the finiteness to
KMNT Cor. 2.2.4, which merely restates Definition 1.5(i)'s hypothesis. On this point scout F is right and
scout O is wrong.** And by A-IV(β) the hypothesis can never hold for an S4′ object, so the result — correct as
it is — does not bear on S4′.

*What B1 does still do.* It is the sharp form of Deninger's [Den05] p. 24 Remark 3 in the presence of fixed
points, and it shows that the escape Deninger names there ("the flow must have fixed points") is **not
sufficient** inside the KMNT/ALKL class. That is a genuine strengthening of a printed remark, and it is
dual-checked. It should go on the record as such — but not as a kill of S4′.

### The table

| # | What an S4′ object must satisfy | Source, with hypotheses checked | Binding status |
|---|---|---|---|
| A1 | Conformal factor α = 1 on TF; T_xφ^{log p}\|T_xF = p^{1/2}·O, O ∈ SO(2); at fixed points e^{−t/2}T_xφ^t ∈ SO(2) | [Den05] p. 27 and pp. 32–33 Fact (read); Leichtnam 2013 (13), (14) (read); 2008 (12) (read) | **Printed axiom.** Clause (ii) is anticipated in print, not a program sharpening. |
| A2 | Transverse measure: exists (Candel), holonomy-invariant, finite, and **scaled by the flow with modulus e^{−t}**; return map at γ_p scales it by 1/p | A-III (Candel p. 490, read) + A-I (dual-check) + Leichtnam 2007 p. 13, Lemma 6.1, Prop. 2.4 (read) | **Clause (iv) restated.** Never flow-invariant with finite mass. |
| A3 | Archimedean leaf: **non-compact**, conformal to C, χ = +1, carrying exactly one fixed point (for K = Q), which is a leafwise source of rate 1/2 | A-II (mine); [Den05] p. 33 Rem. 7 (read, an expectation); Candel Thm. 4.3 and p. 490 (read) | **Clause (iii) determined.** Kills every compact archimedean leaf, in any phase space. |
| A4 | Preserved-leaf set: a compact saturated lamination with **at least two leaves**, never finitely many compact ones | A-IV (mine) | **Kills the KMNT/ALKL class for S4′; voids clause (iv)'s stated rationale; contradicts Leichtnam's Assumption 2].** |
| A5 | Period group Λ = ⟨log p⟩ has **infinite rank**, so F is not a fibration and the flow must have fixed points | [x-18] p. 3 ("F is a fibration if and only if rank Λ = 1"), p. 4 ("If one wants an infinitely generated Λ, one must allow the flow to have fixed points") — both read | **Printed.** Forces clause (iii) from clause (i). |
| A6 | On a closed 3-manifold whose non-transverse set is a finite union of compact leaves, Λ is finitely generated — so clauses (i)+(ii) fail there | B1 (dual-check), from KMNT Lemma 1.10, Def. 1.11 (read) + cutting; printed antecedent [Den05] p. 24 Rem. 3 | **True, and VACUOUS for S4′** by A-IV(β). Does not close the manifold case. |
| A7 | Every γ_p is a **source**: T_xX = T_xF ⊕ RY_φ with Tφ^{ℓ} = p^{1/2}·O on T_xF; empty stable bundle | [Den05] pp. 32–33 (read); immediate | **Removes the whole Anosov toolkit**: periodic-data rigidity, prime-orbit theorems, Fried/Dyatlov–Zworski order-at-zero, marked-length-spectrum rigidity all have hypotheses that fail. |
| A8 | Counting: #{γ : ℓ(γ) ≤ T} = π(e^T) ∼ e^T/T = the h = 1 Margulis/Parry–Pollicott shape | PNT; asymptotic **recalled**, not read | **No obstruction.** Consistency marker only. |
| A9 | Ruelle zeta: ζ_R(s) = Π_γ(1 − e^{−sℓ(γ)})^{−1} = ζ(s); simple pole at s = 1, ord_{s=0} = 0, ζ_R(0) = −1/2 | [x-18] p. 3 dictionary (read); [Den05] p. 33 (ε_γ(k) = +1) (read) | **Marker.** No printed theorem applies (A7). |
| A10 | χ_Co(F, ν) = 0 for every transverse measure (K = Q, unramified) | [Den05] p. 33 Rem. 7 (read) — Deninger's **expectation**, not a theorem | Consistent with A3 (a plane leaf gives χ_Co = 0 by Candel Thm. 4.3, read). Note a **compact** leaf L would give the Dirac transverse measure with χ_Co = χ(L), so A10 independently forbids a compact leaf with χ ≠ 0. |
| A11 | Trace formula: **none exists in print for this class.** ALKL's is for closed manifolds with transversely simple flows (excluded by A-IV); Leichtnam 2007's α = 1 formula is for a compact p-adic-transversal solenoid with no preserved leaves and a rank-1 spectrum | ALKL Abstract, Thm. 1.3.10 (read); Leichtnam 2007 Thm. 2 (CONFIRMED-BY-SCOUT-ONLY) | **The program's real gap.** No printed instrument covers an object with both α = 1 and preserved leaves. |
| A12 | Even a successful S4′ object cannot supply the cohomological half without a further "twist" | [x-04] via [x-06] p. 9 (read) | Downstream, on the payoff. |

---

## §3. THE DISAGREEMENTS, DECIDED

**3.1 "The closed-3-manifold class is dead." — BOTH SCOUTS OVERSTATE; scout O more than scout F.**
Scout O: "no 3-dimensional foliated dynamical system on a closed 3-manifold has closed orbits of length log p
for infinitely many primes p" and "the manifold class is provably dead on two independent grounds". Scout F:
the same conclusion, but stated with the hypothesis "finitely many compact preserved leaves" and with the
loophole explicitly flagged ("with infinitely many preserved compact leaves accumulating, H₁(M₀) can be
infinitely generated and the argument fails — a loophole I flag, not one I have explored").
**Ruling: scout F's formulation is correct and scout O's is not.** Neither noticed the decisive point:
**[ADJ] A-IV proves that S4′ objects always violate the hypothesis**, because the archimedean leaf is
non-compact (A-II) and its closure drags further preserved leaves into the non-transverse set. So the argument
is not merely incomplete for S4′ — it is inapplicable to it. **The closed-3-manifold case for S4′ is OPEN,
reopened by this adjudication.** What *is* dead on a closed 3-manifold is (a) the fixed-point-free case
(Deninger [Den05] p. 24, Remarks 2 and 3 — α = 0 and Λ finitely generated, both under Cor. 5.5's "everywhere
transversal" hypothesis) and (b) the KMNT/ALKL case (B1 and A-II(b)). Neither is S4′'s case.

**3.2 KMNT Corollary 2.2.4 as a proof of finiteness. — SCOUT O IS WRONG.**
Scout O's D-I step 3 cites "KMNT Corollary 2.2.4 (read, verbatim): 'III. P_S^∞ is a non-empty (finite) set'" as
establishing that the preserved leaves are finitely many. I read KMNT Definition 1.5(i) (quoted in full in
§1 A8): the finiteness and compactness of the non-transverse leaves are **hypotheses of the definition of an
FDS³**. Corollary 2.2.4 is a *classification* of FDS³'s and restates the standing assumption. Scout F reads
Def. 1.5 correctly and derives nothing from Cor. 2.2.4. **Scout F is right.**

**3.3 The parity obstruction (scout O's D-II). — WRONG AS ARGUED, RIGHT IN A DIFFERENT AND STRONGER FORM.**
Scout O derives a contradiction by matching ALKL Theorem 1.3.10's preserved-leaf term Σ_L χ(L)/|e^{κ_L t} − 1|
against the archimedean term (1 − e^{−2t})^{−1} of the explicit formula, concluding Σ_{κ_L = −2} χ(L) = 1 while
compact holomorphic leaves have even χ. **Two hypothesis failures.** (a) Inside ALKL's class the flow is
transversely simple on a closed manifold, where A-I forces α = 0 and the closed-orbit coefficients are the
signs ε_c(k), not N p^k ([Den05] p. 27, read; ALKL Thm. 1.3.10, read) — so the arithmetic identity being matched
cannot hold there in the first place, and the "contradiction" is between two things that already could not be
equated. (b) By A-IV(α) the ALKL formula never applies to an S4′ object at all. **However, scout O's own
Poincaré–Hopf cross-check is sound and is the right argument** — and it is stronger than he claimed: with the
Poincaré–Bendixson step added (A-II step 5), the conclusion needs no arithmetic input, no trace formula, and no
parity accident; it holds for every number field and in every phase space, compact manifold or not. **Ruling:
scout O's D-II is superseded by A-II. Credit for the mechanism (index +1 at an archimedean source) is his;
the theorem as it now stands is not the one he wrote.** Scout F declined to derive any Euler-characteristic
constraint from the orbit data ("χ(L) ≠ 0 must be imposed from the trace-formula side") — a defensible caution
that missed the argument.

**3.4 Clause (i) reduced to an isotropy condition (scout O's D-IV). — CORRECT COMPUTATION, OVERSTATED SCOPE.**
The computation is right and I re-derived it: for X = (L × R^{>0})/Q^{>0} with q·(l, u) = (q·l, qu) and
φ^t[l, u] = [l, e^t u], one has [l, e^T u] = [l, u] iff ∃q ∈ Q^{>0} with q·l = l and q = e^T; so the period
group of the orbit through [l, u] is log Isot_{Q^{>0}}(l), and clause (i) becomes: the isotropy groups are
exactly {1} and the p^Z, with one Q^{>0}-orbit per prime and none of rank ≥ 2. **But scout O asserts this
"for any object of Leichtnam's printed shape S_Q", and that is false.** Leichtnam's flow is **not** the plain
suspension: he prints (2007 p. 2, read) "φ^t(l, x) = (ψ_x^t(l), x e^{−t})", with a nontrivial family
(ψ_x^t) of diffeomorphisms of L (his property (iii), p. 13, read). With ψ ≠ id the closed orbits are not
governed by the isotropy of the Q^{>0}-action alone. **Ruling: D-IV is valid for Deninger's plain suspension
X̄₀ = X̌₀(C) ×_{Q^{>0}} R^{>0} and for any plain suspension, and it is a genuinely useful reduction there. It is
not valid for Leichtnam's shape, and the renormalization-group factor ψ_x^t is exactly the freedom Leichtnam
introduced to escape it.** Scout O's related re-scoping of the program's Theorem T (a Q^{>0}-suspension of a
*compact* base is never T₁, whereas Leichtnam's L is only σ-compact) is **correct and I endorse it**: Theorem T
should not be cited again as ruling out the suspension shape in general.

**3.5 Whether α = 0 is forced on closed manifolds unconditionally. — BOTH SCOUTS OVERSTATE.**
Scout F's table row 4 and scout O's L3 both read [x-06] p. 8 and [Den05] p. 24 Remark 2 as saying α = 0 on any
closed manifold. I read the surrounding text: [Den05] Remark 2 is under Corollary 5.5's hypothesis "everywhere
transversal to F", and [x-06] p. 8's sentence sits one paragraph after "we assumed that φ^t had no fixed
points". A-I shows why the restriction is essential: the argument needs a **finite** invariant transverse
measure, and ω_φ has infinite mass at a preserved leaf. **Ruling: print forces α = 0 on a closed 3-manifold
only when the flow is everywhere transverse to F. With preserved leaves the question is open, on manifolds as
well as on spaces.**

**3.6 Whether S4′ is the program's sharpening or Leichtnam's printed conjecture. — SCOUT F IS RIGHT AND
SCOUT O IS INCOMPLETE.**
Scout O identified Leichtnam 2007's conjectural quadruple and the zbMATH review of the 2005 Contemp. Math.
article, and concluded S4′ is "Leichtnam's printed conjecture". Scout F went further and found the **axiom
lists themselves**: Leichtnam 2008 §5.1 1]–7] (author copy) and Leichtnam 2013 §4.1 1]–8], the latter printing
clause (ii) verbatim as (14). I confirmed 2013 §4.1 on disk. **Scout F's finding is binding**, and it changes
the program's novelty record (§1 A6). Scout O did not open r3s-20 §4.1 and his novelty picture is one paper
behind.

**3.7 The next gate. — BOTH PROPOSALS SUPERSEDED.**
Scout O proposed Q-S4″(a,b), a purely group-theoretic isotropy question about Q^{>0}-spaces; by §3.4 that
question is about plain suspensions only, which Leichtnam's shape is not, so a negative answer would not close
S4′. Scout F proposed the "rank gate" — can any compact foliated 3-space with a foliated flow transverse to all
but finitely many compact preserved leaves have an infinite-rank length group; by A-IV(β) an S4′ object never
has "finitely many compact preserved leaves", so a negative answer there also would not close S4′, and a
positive one would not build toward it. **Ruling: both gates are the wrong gate. §5 states the right one.**

**3.8 Where the scouts agree and I confirm.** No published object satisfies (i)–(iv) for any number field
(dual-checked, plus my own third coverage check). The problem is stated open in print continuously from 2002 to
2026 (§1; the verbatim statements are in both scout files and I re-read six of them at source). Clause (ii)
plus compactness is incompatible with a finite flow-invariant transverse measure (A-I, dual-check). Every γ_p
is a source, which removes the Anosov toolkit (dual-check; I re-derived it). Counting is consistent at entropy
1 and imposes nothing. The Fuller index gives nothing. Deninger's no-Weil-cohomology result bears on the payoff,
not on existence.

---

## §4. SPONSOR-FETCH, CONSOLIDATED

1. **E. Leichtnam, *An invitation to Deninger's work on arithmetic zeta functions*, in M. Entov, Y. Pinchover,
   M. Sageev (eds.), *Geometry, spectral theory, groups, and dynamics* (Proceedings in memory of Robert Brooks,
   Haifa, 29 Dec 2003 – 9 Jan 2004), Contemporary Mathematics 387 / Israel Mathematical Conference
   Proceedings, AMS and Bar-Ilan University, Providence RI, 2005, pp. 201–236. DOI 10.1090/conm/387/07243;
   zbMATH Open document 2236599; OpenAlex W4205472627.**
   *Status: still unreached; VALUE NOW LOW.* Scout O recovered the full zbMATH review (confirming that §5
   states "a conjecture stating the existence of a Riemannian laminated foliated space (S̄_Q, F) endowed with a
   flow φ^t and satisfying certain geometric properties" and derives RH from it). Scout F recovered the 2008
   successor axiom list and I confirmed the 2013 one on disk. **The only thing the 2005 article could still add
   is whether the closed-orbit derivative axiom (2013's (14)) and any Euler-characteristic or accumulation
   clause were already there in 2005.** Blocked routes tried across the two scouts: not on arXiv; author page
   403 with and without a Chrome UA; Wayback captures of both author pages carry no copy; zbmath.org HTML 403
   (API works); no PDF located. **Demote from "highest-value fetch" to "nice to have".**
2. **E. Leichtnam, *On the analogy between arithmetic geometry and foliated spaces*, Rend. Mat. Appl. (7) 28
   (2008) 163–188.** The journal servers (`www1.mat.uniroma1.it`, `rendiconti.mat.uniroma1.it`) connection-fail;
   DOAJ empty. Scout F recovered an **author copy dated 27 Nov 2008** from the Wayback Machine and it is saved
   in this directory; its §5.1 is quoted in §1 A5 and I read it. **What remains unverified: that this author
   copy is the Rendiconti article** (its running head is "TALK") and its journal pagination. Cite it as an
   author manuscript until a journal copy is obtained. *Low cost, worth one attempt.*
3. **[ÁLKL22] J. A. Álvarez López, Y. A. Kordyukov, E. Leichtnam, *Simple foliated flows*, arXiv:1906.06753,
   Tohoku Math. J., DOI 10.2748/tmj.20201015b.** Scout O downloaded but did not read it; scout F read pp. 2–3
   and 9–10. **Not read by me.** It carries the Hector-case classification (c)–(f) that the memoir quotes and
   the precise definition of transverse simplicity. Worth reading once, to state A-IV's exclusion in the
   sharpest published vocabulary.
4. **G. Duminy's theorem and Hurder's Problem 5.4 — the fetch this adjudication creates.**
   S. Hurder, *Foliation geometry/topology problem set*, `homepages.math.uic.edu/~hurder/papers/58manuscript.pdf`
   (fetched and READ this session), §5, verbatim: "**Duminy's Theorem [84] shows that the semiproper leaves of
   K must have a Cantor set of ends.**" and, as an open problem, "**PROBLEM 5.4. Show that every leaf of K has
   a Cantor set of ends.**" (K = an exceptional minimal set of a codimension-one C² foliation of a compact
   manifold.) Reference [84] there is **J. Cantwell, L. Conlon, *Endsets of exceptional leaves; a theorem of
   G. Duminy*, in Foliations: Geometry and Dynamics (Warsaw, 2000), World Scientific, 2002.** *Not read.* This
   is now the **highest-value fetch for C3-r** — see §5.
5. **É. Ghys, *Laminations par surfaces de Riemann*, Panoramas et Synthèses 8 (1999) 49–95.** Located by both
   scouts (perso.ens-lyon.fr); scout F grepped it (no "flot"/"Deninger"/"zêta" hits); **not read by me.** It is
   Deninger's standing reference [Ghy99] and the right place to check whether a compact minimal Riemann-surface
   lamination with a **plane** leaf and a scaling transverse measure is known to exist.
6. **A. Connes, C. Consani, *Knots, primes and class field theory*, Contemp. Math. (Pisa Regulators V), AMS
   2025 = arXiv:2401.08401.** Abstract only, both scouts. Low value: Leichtnam's printed verdict (§1 A4) already
   excludes the adele-class space from the S4′ class.
7. **F. Kopei**, *A remark on a relation between foliations and number theory*, arXiv:math/0605184 (read by
   scout F), and *A foliated analogue of one- and two-dimensional Arakelov theory*, Abh. Math. Semin. Univ.
   Hambg. 81 (2011) 141–189 (**not read by anyone**). Bears on the arithmetic content, not on existence.
8. **Parry–Pollicott, Ann. of Math. 118 (1983) 573–591** (prime orbit theorem) and **Ruelle, Bol. Soc. Brasil.
   Mat. 9 (1978) 83–87** (Ruelle inequality): recalled by both scouts and by me, used only as consistency
   markers (table rows A8), never load-bearing. JSTOR-blocked.
9. **Standing, unchanged from Session 14:** Komatsu J. Math. Soc. Japan 19 (1967) Thm 6′; Wengenroth, Studia
   Math. 120 (1996); Antosiewicz–Dugundji; Mangino; Álvarez López–Kordyukov (Warsaw 2000); MathSciNet;
   ALKL LNM 2387 (2026) published memoir (paywalled; the arXiv v1/v2 was read instead and scout F confirms the
   quoted sentences are identical).

---

## §5. THE NEXT DECIDABLE QUESTION, AND THE STANDING-ORDER-6 RULING

### Where the adjudication leaves the object

An S4′ object, if it exists, is now pinned as follows, every item sourced in §2:
- compact foliated space, leaves Riemann surfaces, leafwise metric with α = 1 (A1);
- a holonomy-invariant transverse measure exists automatically and is scaled by the flow with modulus e^{−t}
  (A2, A-III);
- the closed orbits are sources, one per prime, transverse to F, with ζ_R = ζ (A7, A9);
- the non-transverse set N is a **compact saturated lamination of preserved leaves**, containing a
  **non-compact** leaf conformal to **C** with χ = +1, and containing at least one further leaf (A3, A4);
- the closed orbits accumulate on N (clause (iii));
- **no trace formula in print covers this object** (A11), and the one the program named (ALKL) provably cannot
  (A-IV(α)).

Everything now turns on the archimedean lamination N, not on the length spectrum. That is where the next
question must be put, and it is a question of **foliation theory alone** — no arithmetic in it.

### Q-S4⁗ — the archimedean-lamination gate

> **(a) [The general question.]** Does there exist a compact foliated space X with 2-dimensional
> leafwise-holomorphic leaves, a compact saturated sublamination N ⊊ X, and a leaf L ⊂ N **conformal to the
> euclidean plane C**, such that N is exactly the non-transverse set of a foliated flow on (X, F) whose orbits
> off N are transverse to F?
>
> **(b) [The manifold case, and the decisive instrument.]** On a **closed 3-manifold** with a C²
> codimension-one foliation, can a leaf conformal to C lie in a compact saturated set that is not a finite
> union of compact leaves?

**Why this is the right gate, and why both scouts' gates are not.** By A-IV every S4′ object is forced into
exactly this configuration, so a negative answer to (a) is a **theorem that S4′ is unrealizable**, at clause
(iii), in every phase space. A negative answer to (b) alone closes the closed-3-manifold case for good — which
is what Deninger asserts as an expectation on [Den05] p. 26 and which print does **not** currently prove once
fixed points are allowed (§3.5). By contrast, scout O's isotropy gate decides only plain suspensions (§3.4) and
scout F's rank gate assumes a hypothesis S4′ objects never satisfy (§3.7).

**The instrument the sweep located, and why it is decisive.** From S. Hurder's *Foliation geometry/topology
problem set* (`homepages.math.uic.edu/~hurder/papers/58manuscript.pdf`, fetched and READ this session), §5,
verbatim: "**Duminy's Theorem [84] shows that the semiproper leaves of K must have a Cantor set of ends.**"
(K = an exceptional minimal set of a codimension-one C² foliation of a compact manifold), with reference
[84] = **J. Cantwell, L. Conlon, *Endsets of exceptional leaves; a theorem of G. Duminy*, in Foliations:
Geometry and Dynamics (Warsaw, 2000), World Scientific, 2002.** A plane has exactly **one** end, so Duminy's
theorem forbids the archimedean leaf from being a semiproper leaf of an exceptional minimal set. Hurder prints
the remaining case as an **open problem**: "**PROBLEM 5.4. Show that every leaf of K has a Cantor set of
ends.**" So (b) reduces to two checkable sub-questions:
1. Must the archimedean leaf L, being non-compact and lying in the compact saturated set N whose leaves are all
   preserved, be a leaf of a *minimal* set — and if so, of an *exceptional* one?
2. Is L semiproper? If yes, Duminy applies and (b) is answered NO. If no, the case is exactly Hurder's open
   Problem 5.4, and the program should record that S4′'s manifold case is **equivalent to a named open problem
   in foliation theory** — a far more useful position than "probably impossible".

**The three first steps, in order, each cheap.**
1. **Read Cantwell–Conlon, *Endsets of exceptional leaves; a theorem of G. Duminy*** (World Scientific, 2002)
   and get the exact statement, its regularity hypothesis (C² is expected), and its definition of *semiproper*.
   Then check whether the archimedean leaf of an S4′ object is semiproper — this is decidable from A-IV's
   structure (L̄ ∖ L ≠ ∅ and L̄ ⊆ N) plus the definition.
2. **Read É. Ghys, *Topologie des feuilles génériques*, Ann. of Math. 141 (1995) 387–422** (recalled, NOT read
   — see §8), whose subject is exactly which surfaces occur as leaves in a minimal set, and **É. Ghys,
   *Laminations par surfaces de Riemann*, Panoramas et Synthèses 8 (1999)** for the compact-lamination version.
   These decide (a) for laminations, or say that it is open.
3. **Only if steps 1–2 leave (a) possible:** write down the candidate N directly — a compact lamination with a
   plane leaf and a scaling holonomy-invariant transverse measure — and check A-I's modulus condition on it.
   That, and not a length-spectrum construction, is the first genuine construction step for S4′.

**Two secondary items the adjudication produced, both cheap and both worth recording now.**
- **Correct the program's clause (iv).** It must read "the necessarily existing holonomy-invariant transverse
  measure is scaled by the flow with modulus e^{−t}" (A-I + A-III), and its parenthetical justification
  ("needed for the leafwise trace formula of Álvarez López–Kordyukov–Leichtnam") must be **deleted**: by
  A-IV(α) that formula can never apply to an S4′ object.
- **Correct the program's Session-14 novelty record.** C10's "PARTIAL for the four sharpened clauses" becomes
  (i), (ii), (iv) ANTICIPATED in Leichtnam 2008 §5.1 and 2013 §4.1; (iii) PARTIAL (§1 A6). And Theorem T should
  be re-scoped: it assumes a compact base, and Leichtnam's L is only σ-compact (§3.4).

### Standing order 6: is a construction attempt licensed?

**Ruling: NO for S4′; YES for a bounded literature decision on Q-S4⁗ and for nothing else.**

Standing order 6 asks whether the object, an obstruction to it, or the inverse problem for it already exists in
print. The answer this adjudication returns is: **(α)** the object is Leichtnam's printed axiom list
(2008 §5.1, 2013 §4.1), not a program invention, and it is stated open continuously from 2002 to 2026;
**(β)** the printed obstructions kill only classes that S4′ objects provably cannot inhabit (A-IV), so the
program does not in fact hold a kill; **(γ)** what the program does now hold is a **new** and previously
unstated obstruction — A-II/A-IV — which relocates the whole difficulty from the length spectrum to the
archimedean lamination and which invalidates one of Leichtnam's own printed axioms; **(δ)** the escape class
has **no trace formula in print at all**, so an object built there could not yet be used.

**Building the dynamical object before Q-S4⁗(a) is answered would be building against a configuration that may
be forbidden by a theorem that already exists (Duminy's) or by one that is a named open problem (Hurder 5.4).**
Six to ten pages of foliation literature decide it. That is the whole of the next session's C3-r work.

**If Q-S4⁗ returns "possible", the first three construction steps are:** (1) build the compact lamination N by
surfaces with a plane leaf and a holonomy-invariant transverse measure — the archimedean fiber; (2) suspend it
by a flow with normal exponent κ = −2 at the plane leaf, matching Leichtnam's R≥0-orbifold structure
(2008 7], read) and giving the archimedean term (1 − e^{−2t})^{−1}; (3) attach the transverse solenoidal part
carrying the γ_p, with transverse measure scaled by e^{−t} (A-I) and return derivative p^{1/2}·SO(2) (A1), and
verify that its closure meets N in exactly the lamination of step 1. **If Q-S4⁗(a) returns NO, the killing
clause is (iii)**, and S4′ is dead with a theorem the program owns.

---

## §6. PROPOSED TEXT (PROPOSED, NOT APPLIED)

The two blocks below are drafted for the program's durable files. **They are not applied by this file.** The
orchestrator should apply them, edit them, or reject them.

### 6.1 Proposed `results/c3-r/m2c-feasibility-ledger.md` §16

```
## §16. Q-S4′ adjudicated (Session 16, 2026-09-05) — INSTRUMENT; the obstruction moves to the archimedean leaf

Two scouts (Opus 5, Fable 5.1) swept the literature for S4′; a binding adjudication (Opus 5) re-opened every
load-bearing source. Files: results/c3-r/s16/qs4prime/{scout-O.md, scout-F.md, adjudication.md}.

S16-1. S4′ IS IN PRINT AS AN AXIOM LIST, NOT ONLY AS A DESIDERATUM. Leichtnam 2013 (arXiv:1307.3851 = r3s-20)
§4.1 Assumptions 1]–8] print clause (i) ("a unique primitive closed orbit γ_P of φ^t of length log NP",
Assumption 2]), clause (ii) verbatim ((14): e^{−(log NP)/2} D_yφ^{log NP}(x̃)|T_x̃F ∈ SO₂), clause (iv)
(Assumption 5], "there exists a transverse measure µ"), and the fixed-point form of clause (iii)
(Assumptions 2], 7], 8]). Leichtnam 2008 (author copy, §5.1 1]–7], recovered via Wayback and saved beside the
adjudication) prints the same list for K = Q, without (ii). CORRECTION TO S14 C10: the four clauses are
ANTICIPATED for (i), (ii), (iv) and PARTIAL for (iii) — not "PARTIAL" across the board.

S16-2. NO OBJECT EXISTS, IN ANY CLASS. The only solved case remains Deninger [De02] (ordinary elliptic curve
over F_q, rank-1 length group, no fixed point). Three independent coverage checks (Semantic Scholar, OpenAlex,
arXiv API) find no construction attempt 2019–2026.

S16-3. THE MANIFOLD KILL IS TRUE BUT VACUOUS FOR S4′. The closed-orbit length group of a foliated flow on a
closed 3-manifold whose non-transverse set is a finite union of compact leaves is finitely generated (KMNT
Lemma 1.10/Def. 1.11 + cutting; sharpens [Den05] p. 24 Rem. 3 to the fixed-point case) — dual-derived. But
[ADJ-A-IV] no S4′ object has a non-transverse set of that form, so the result does not bear on S4′. The
closed-3-manifold case for S4′ is OPEN. Note also that [Den05] p. 24 Rem. 2 and [x-06] p. 8 force α = 0 only
under "the flow is everywhere transversal to F" / "no fixed points" — both re-read.

S16-4. NEW OBSTRUCTION, AT CLAUSE (iii) [ADJ-A-II, single-check]. In any S4′ object every compact preserved
leaf has χ = 0 and carries no fixed point; hence clause (iii)'s leaf is NON-COMPACT, conformal to C, χ = +1.
Proof: the printed fixed-point conformality ([Den05] p. 33 Fact; Leichtnam 2013 (13)) makes every fixed point a
leafwise source of index +1; Poincaré–Hopf then forces χ(L) = 2 and L ≅ S² with two sources; Poincaré–Bendixson
on S² produces a closed orbit inside the leaf, contradicting clause (i). Uniform in the number field. Corollary:
no closed manifold with a transversely simple foliated flow realizes S4′ (ALKL's preserved leaves are compact).

S16-5. NEW STRUCTURAL FORCING [ADJ-A-IV, single-check]. The archimedean leaf, being non-compact in a compact
phase space, is not closed; its closure lies in the (closed, saturated) non-transverse set, every leaf of which
is preserved. So the archimedean part is always a compact saturated LAMINATION of preserved leaves, never one
leaf and never finitely many compact ones. Three consequences: (α) the ALKL trace formula can NEVER apply to an
S4′ object, so clause (iv)'s stated rationale is void; (β) S16-3 is vacuous for S4′; (γ) Leichtnam's printed
Assumption 2] ("the flow is transverse to all the leaves different from the one containing x_∞") is
inconsistent with compactness and must be weakened before anyone builds against it.

S16-6. CLAUSE (iv) RESTATED. A holonomy-invariant transverse measure NECESSARILY EXISTS (Candel, Ann. Sci. ENS
26 (1993) p. 490: a compact surface lamination with no invariant transverse measure has all leaves hyperbolic,
contradicting the plane leaf of S16-4), and the flow must scale it with modulus exactly e^{−t} (α = β; the
return map at γ_p scales it by 1/p) — Leichtnam 2007's type-III_{1/q} mechanism (Jac M_q = 1/q against
g̃(q_*u) = q g̃(u)). Clause (iv) must read "the transverse measure is scaled with modulus e^{−t}", and its
ALKL justification must be deleted.

S16-7. NEGATIVE SWEEP RESULTS (both scouts, confirmed). Every γ_p is a source with empty stable bundle, so the
Anosov toolkit — periodic-data rigidity, prime-orbit theorems, Fried/Dyatlov–Zworski order-at-zero,
marked-length-spectrum rigidity — has hypotheses that fail. Counting is consistent at entropy 1. The Fuller
index gives nothing (the orbit set is not isolated). Inverse period-set results in print are discrete-time or
rank-one and do not constrain S4′. Deninger's no-real-Weil-cohomology result bears on the payoff, not existence.

S16-8. NEXT GATE: Q-S4⁗ (adjudication §5) — can a compact saturated lamination by surfaces contain a leaf
conformal to C and be the non-transverse set of a foliated flow (general case), and can a plane leaf lie in a
compact saturated non-compact-leaf set of a C² codimension-one foliation of a closed 3-manifold (manifold
case)? Duminy's theorem (semiproper leaves of an exceptional minimal set have a Cantor set of ends — Hurder,
Foliation geometry/topology problem set §5, read) may already answer the manifold case NO; the remaining case
is Hurder's open PROBLEM 5.4. Standing order 6 licenses the literature decision, not a construction.
```

### 6.2 Proposed replacement for the frontier paragraph of `directions/C3-geometric-substrate.md`

```
FRONTIER (as of Session 16, 2026-09-05). Deninger's own candidate substrates are exhausted (§14–§15). The
standalone existence problem S4′ is Leichtnam's printed axiom list (2008 §5.1; 2013 §4.1, where clause (ii) is
equation (14)), open in print from 2002 to 2026, unrealized in every class except Deninger's rank-1
elliptic-curve solenoid. Session 16's adjudication moves the frontier off the length spectrum: the printed
length-group obstruction on closed 3-manifolds is real but VACUOUS for S4′, because an S4′ object's
archimedean leaf must be non-compact (χ ≠ 0 forces it; Poincaré–Hopf plus Poincaré–Bendixson) and therefore
drags a whole compact saturated lamination of preserved leaves with it — putting every S4′ object outside the
KMNT/ALKL class and outside the only proved preserved-leaf trace formula. The live question is now
Q-S4⁗: can a compact lamination by Riemann surfaces contain a plane leaf and be the non-transverse set of a
foliated flow? Duminy's theorem and Hurder's Problem 5.4 are the instruments; six to ten pages of foliation
literature decide it. Until they do, no construction attempt is licensed.
```

---

## §7. NOVELTY LEDGER — what this session derived that is not in print

Tags: **[dual-check]** = both scouts derived it independently and I confirmed it; **[single-check]** = one
scout, or me, derived it and it has had exactly one independent confirmation (mine, or none). Nothing here was
found in print by any of the three of us; each item names the printed statements it rests on.

| # | Statement | Rests on (all read) | Tag |
|---|---|---|---|
| N1 | On a closed 3-manifold whose non-transverse set is a finite union of compact leaves, the closed-orbit length group is finitely generated; hence clauses (i)+(ii) are unrealizable there. Sharpens [Den05] p. 24 Rem. 3 from the fixed-point-free case to the finitely-many-compact-preserved-leaves case. | KMNT Lemma 1.10, Def. 1.11; cutting along compact leaves; unique factorization | **[dual-check]** (scout O D-I, scout F R2, confirmed by me; hypotheses corrected — §3.1, §3.2) |
| N2 | On a compact foliated space, the leafwise conformal factor equals the flow-modulus of the transverse measure: α = β. Hence α = 1 forces a transverse measure scaled by e^{−t}, and the return map at γ_p scales it by 1/p. | [Den05] (20)/(31), p. 27; [x-18] Construction 3 (ω_φ φ-invariant); Leichtnam 2007 p. 13 | **[dual-check]** (scout O D-III, scout F R1, confirmed and sharpened by me into an equality) |
| N3 | Every γ_p is a source with empty stable bundle; consequently the entire Anosov/Axiom-A toolkit has hypotheses that fail against S4′. | [Den05] pp. 32–33 Fact | **[dual-check]** |
| N4 | Clause (i) of S4′ is, for a **plain** Q^{>0}-suspension, exactly an isotropy condition on the Q^{>0}-space (isotropy groups {1} and p^Z, one orbit per prime, none of rank ≥ 2). NOT valid for Leichtnam's shape, whose flow carries a nontrivial renormalization factor ψ_x^t. | Leichtnam 2007 p. 2 (both the shape and φ^t(l,x) = (ψ_x^t(l), xe^{−t})); [x-03] suspension convention | **[single-check]** (scout O D-IV; computation confirmed by me, scope corrected — §3.4) |
| N5 | Program Theorem T does not apply to Leichtnam's S_Q: Theorem T assumes a compact base, and Leichtnam prints L only σ-compact. | Leichtnam 2007 p. 2 ("σ-compact"); ledger §15 | **[single-check]** (scout O; endorsed by me) |
| N6 | **A-II.** In any S4′ object every compact preserved leaf has χ = 0 and carries no fixed point; clause (iii)'s leaf is therefore non-compact, and (with [Den05] p. 33 Rem. 7 + Candel) conformal to C with χ = +1. Uniform in the number field. | [Den05] p. 33 Fact; Leichtnam 2013 (13), 2008 (12); Poincaré–Hopf; Poincaré–Bendixson on S²; Candel Thm. 4.3 | **[single-check]** (mine; scout O's D-II contains the index germ but the argument he wrote is superseded — §3.3) |
| N7 | **A-III.** A positive holonomy-invariant transverse measure NECESSARILY EXISTS on an S4′ object. | Candel, Ann. Sci. ENS 26 (1993) p. 490, first theorem ("in particular, this holds true if M has no invariant measure") + N6 | **[single-check]** (mine; neither scout has it) |
| N8 | **A-IV.** The archimedean part of an S4′ object is always a compact saturated lamination of preserved leaves — never a single leaf, never finitely many compact ones. Consequences: (α) the ALKL trace formula can never apply to an S4′ object; (β) N1 is vacuous for S4′ and the closed-3-manifold case is reopened; (γ) Leichtnam's printed Assumption 2] is inconsistent with compactness. | Compactness + Hausdorffness of X; closedness and saturation of the non-transverse set; A-II; ALKL Abstract and §4.1.2; Leichtnam 2008 2], 2013 2] | **[single-check]** (mine; neither scout has it; this is the load-bearing new result) |
| N9 | A compact preserved leaf L would give the Dirac transverse measure with χ_Co(F, δ_L) = χ(L) by Gauss–Bonnet, so Deninger's own expectation χ_Co(F, ν) = 0 for all ν (K = Q, unramified) independently forbids a compact leaf with χ ≠ 0. | [Den05] p. 33 Rem. 7 (an expectation, so this is expectation-level) | **[single-check]** (mine) |
| N10 | Print forces α = 0 on a closed 3-manifold **only** when the flow is everywhere transverse to F; with preserved leaves the question is open on manifolds too (ω_φ has infinite mass at a preserved leaf — ALKL's b-density). | [Den05] p. 24 Rem. 2 in its Cor. 5.5 context; [x-06] p. 8 ("we assumed that φ^t had no fixed points"); A-I's finiteness requirement | **[single-check]** (mine; both scouts read the sentences without their standing assumption — §3.5) |
| N11 | Coverage: no construction attempt in print, 2019–2026. | Semantic Scholar citing sets (scout O), OpenAlex citing sets (scout F), arXiv API listing (mine) | **[dual-check]**, in fact triple |
| N12 | Corrected novelty record: S4′ clauses (i), (ii), (iv) are ANTICIPATED in Leichtnam 2008 §5.1 / 2013 §4.1; only (iii)'s "χ(L) ≠ 0" and "the leaf lies in the accumulation set" plus the inverse-spectrum framing are the program's own. | Leichtnam 2008 §5.1 1]–7]; 2013 §4.1 1]–8] | **[single-check]** (scout F; confirmed by me on disk — binding) |

---

## §8. HONESTY

**Read by me, this session, at the page cited.** On disk: `x-20` ([Den05]) pp. 23–24 (Cor. 5.5 and Remarks
1–3), pp. 26–27 (dictionary, desideratum, Fact 6.1, the α = 1 sentence), pp. 32–33 (Remark 5, the Fact,
Remarks 6 and 7); `x-18` pp. 3–4 (Construction 3, the fibration/rank sentence, the infinitely-generated-Λ
sentence, Dictionary 4 part 2); `x-06` pp. 8–9 (the no-fixed-points standing assumption, the α = 0 sentence,
the α = 1/(totally disconnected) sentence, the Weil-cohomology twist); `r3s-17` (ALKL memoir) Abstract, §1.3
(the K/K′ Lefschetz distributions and W_L), Theorem 1.3.10, §4.1.2; `r3s-20` (Leichtnam 2013) §4.1 Assumptions
1]–8] including (13), (14), and the explicit formula (12); `r3s-21` (Leichtnam 2007) pp. 2, 13, 17 (the S_Q
shape, "still unknown", the Connes remark, the flow formula, axioms (i)–(ii), Open Question 2); the Leichtnam
2008 author copy §5.1 Assumptions 1]–7] and Comment 8. Fetched online and read: **KMNT arXiv:1906.02424** PDF
(Def. 1.5, Lemma 1.10 with proof, Def. 1.11, Lemma 1.12, Thm. 2.2.2, Rem. 2.2.3, Cor. 2.2.4, Prop. 2.2.5);
**Candel, Ann. Sci. ENS 26 (1993)** numdam scan (the two theorems of p. 490, Theorem 4.3 and the four
non-hyperbolic cases of pp. 497–498) — the scan is OCR-degraded but the quoted sentences are legible;
**S. Hurder, Foliation geometry/topology problem set** §5 (Duminy's theorem as quoted there, Problems 5.2–5.5);
the **arXiv API listing** for `all:"foliated dynamical system" OR all:"foliated flow"`, 40 rows newest-first;
a Cambridge Core search confirming the existence and date of de Jong, ETDS, DOI 10.1017/etds.2026.10313.

**Read only through the scouts (CONFIRMED-BY-SCOUT-ONLY), and marked as such wherever used.** [Den05] §7.7 and
Theorem 7.8 and the p. 36 elliptic-curve example; `x-22` ([De02]) throughout; `x-03`/`z-19` pp. 3, 40/60;
`x-04`; `r3s-08` (Morishita); `r3s-19`, `r3s-22`; Leichtnam 2007 §§3–5 (Prop. 2, Theorem 2, Lemma 6);
ÁLKL *Simple foliated flows* (arXiv:1906.06753); Ghys, Sém. Bourbaki 785; Kopei math/0605184; Fuller,
Bull. AMS 72 (1966); the Connes–Consani and Kucharczyk–Scholze abstracts; the Kalinin–Sadovskaya, Dyatlov–
Zworski, Cekić–Delarue–Dyatlov–Paternain, Dang–Guillarmou–Rivière–Shen, Barthelmé–Fenley and
Cristofaro-Gardiner–Mazzucchelli abstracts; the zbMATH review of Leichtnam 2005; the OpenAlex and Semantic
Scholar citing sets. **No verdict in §0 or §2 rests on any of these alone.**

**Recalled, not read, and load-bearing on nothing.** The Parry–Pollicott/Margulis prime orbit asymptotic
(table row A8, consistency only); Ruelle's inequality; the prime number theorem and unique factorization
(elementary, re-derived in situ); the Poincaré–Hopf theorem and the Poincaré–Bendixson theorem on S² (standard,
used in A-II and stated there with their hypotheses); Gauss–Bonnet (N9); **É. Ghys, *Topologie des feuilles
génériques*, Ann. of Math. 141 (1995) 387–422** — named in §5 step 2 as a fetch, on the basis of its title and
subject only, and carrying no weight in any ruling; the standard fact that a leaf of a foliation of a compact
space is compact iff it is closed (used in A-IV step 2; elementary and re-derived there).

**My own judgment calls, all flagged in place.** The classification INSTRUMENT and the whole of §0;
derivations A-I (corrected joint form), A-II, A-III, A-IV, B1 (corrected joint form) in §2; every ruling in
§3; the choice of Q-S4⁗ as the next gate and the standing-order-6 ruling in §5; the proposed texts in §6, which
are proposals only; the tags in §7.

**Defects found in my inputs.** (1) Scout O: [Den05] Remarks 2 and 3 are on p. 24, not p. 23; KMNT Cor. 2.2.4
does not prove the finiteness of the preserved-leaf set (Def. 1.5(i) assumes it); D-II applies the ALKL trace
formula outside its hypotheses; D-IV's scope claim ("any object of Leichtnam's printed shape") is false; the
D-I conclusion is stated without its hypothesis; Leichtnam 2013 §4.1 was not opened, so the novelty picture is
one paper behind. (2) Scout F: the [x-18] p. 3 fibration/rank sentences were quoted from the program record
rather than located — they are there, verbatim, and I confirmed them; the identification of the recovered
author copy with Rend. Mat. Appl. 28 (2008) 163–188 is unverified. (3) Both: the α = 0 sentences of [Den05]
p. 24 and [x-06] p. 8 were read without their standing "no fixed points" assumption; and both declared the
closed-3-manifold class dead on the strength of an obstruction whose hypothesis no S4′ object can satisfy.
(4) In the program's own record: `s14/novelty/adjudication.md` §2 C10's "PARTIAL for the four clauses" is
wrong (§1 A6), and the S4′ statement's clause (iv) parenthetical ("needed for the leafwise trace formula of
Álvarez López–Kordyukov–Leichtnam") is void (A-IV(α)).

**Nothing in this file was taken on trust from either scout without my opening the source, except where the
words CONFIRMED-BY-SCOUT-ONLY appear.**
