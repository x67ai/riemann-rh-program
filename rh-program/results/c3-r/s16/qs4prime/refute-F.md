# REFUTATION PASS F — Q-S4′ adjudication, single-check derivations A-II, A-III, A-IV, the vacuity ruling, the clause-(iv) restatement, N10

**Program:** RH research program, direction C3-r. **Session:** 16. **Date:** 2026-09-06 (IST, after midnight of 2026-09-05).
**Refuter:** F (Fable 5.1), adversarial verifier under standing orders 5 and 7. **Target file:** `adjudication.md` in this
directory (Opus 5, binding), §0, §2 (A-I to A-IV, B1, table), §3, §5, §7 — all read in full. Also read in full: `scout-O.md`
D-II/D-III, `scout-F.md` §0 and R1; ledger `m2c-feasibility-ledger.md` §15–§16 with the orchestrator's enactment note.
**Every judgment below is mine** and is labeled [F]. Every source anchor names the PDF on disk and the printed page I read.
U.S. English.

**How to read the verdicts.** The six targets are derivations. A derivation STANDS only when I could write its proof from
the printed hypotheses; STANDS-NARROWED when it is true under an extra or corrected hypothesis that I state exactly;
FALLS when I exhibit the gap or a counterexample. Where a target bundles several claims, the table gives one label and
§1–§6 give the per-claim breakdown.

---

## §0. VERDICT TABLE

| Target | Claim under test | Verdict [F] | Narrowed statement / gap, in one line |
|---|---|---|---|
| **T1 = A-II** | Every compact preserved leaf of an S4′ object has χ = 0 and no fixed point; clause (iii)'s leaf is non-compact, conformal to C, χ = +1 | **STANDS-NARROWED** | Non-compactness STANDS **only after S4′ is amended by clause (0)** — either (0-fix): at every fixed point e^{−t/2}T_xφ^t\|T_xF ∈ SO(2) (Leichtnam 3]a (13)), or (0-coh): φ^{t*} = e^t on H̄²_F (Deninger p. 27 = Leichtnam 4] (15)). Neither is among S4′'s four clauses; without one, a compact S² leaf carrying a source–sink flow satisfies (i)–(iv) restricted to the leaf (§1.1). **"Conformal to C, χ = +1" FALLS**: it rests on [Den05] p. 34 Rem. 7, an expectation that presupposes a transverse measure, that does not identify which leaf is euclidean, and that for every K ≠ Q predicts the opposite (all leaves hyperbolic). Worse: under (0-coh) a euclidean preserved leaf is **impossible** (Theorem F-1, §1.5); under (0-fix) alone the conformal type is unconstrained. |
| **T2 = A-III** | A positive holonomy-invariant transverse measure necessarily exists on an S4′ object (Candel p. 490) | **FALLS** | Candel's theorem applies verbatim to S4′ objects (compact Riemann surface lamination), but its conclusion needs a **non-hyperbolic leaf**, supplied only by T1(e), which falls. Under (0-coh) the intended witness — a euclidean *preserved* leaf — is excluded by Theorem F-1, and the archimedean lamination N carries **no** invariant transverse measure at all. Existence of clause (iv)'s measure remains an axiom (Leichtnam 5]), not a consequence. |
| **T3 = A-IV** | Closed leaf ⇒ compact; N closed and saturated; archimedean part is a compact saturated lamination of preserved leaves, never one leaf, never finitely many compact ones; (α) ALKL never applies; (β) B1 vacuous; (γ) Leichtnam 2] inconsistent with compactness | **STANDS-NARROWED** | (a) and (b) STAND — I wrote both proofs for laminations (§3.1–3.2). The structural conclusion STANDS **given clause (0)** in either form (under (0-coh) it needs no fixed-point analysis: a compact preserved leaf T gives the flow-invariant Dirac measure δ_T, contradicting (15)). (α) STANDS (ALKL's transverse simplicity is a hypothesis that forces compact preserved leaves, §4.1.2 read). (β) STANDS as stated but is **sharpened by B1′** (§3.4): B1's mechanism also kills every N that is a *finite union of finite-type leaves*. (γ) must be restated: "inconsistent with compactness of S_K, **which Leichtnam does not print** in 2008 §5.1 or 2013 §4.1 (verified: the word does not occur in either list); his 2007 S_Q is presented as a compactification (r3s-21 p. 2)". |
| **T4 = vacuity ruling** | No S4′ object has N = finite union of compact leaves; the KMNT/ALKL kill does not bear; the closed-3-manifold case is OPEN | **STANDS-NARROWED** | Binding form: **"For S4′ objects carrying clause (0) (either form), N is never a finite union of compact leaves, so N1/B1 as printed does not bear. But B1′ (mine) kills every closed-3-manifold realization whose N is a finite union of leaves of finite type; in every case rank_Z H₁(M ∖ N) = ∞ is necessary. The closed-3-manifold case is open only in the class where N has infinitely many leaves or a leaf of infinite type — and, under (0-coh), N is a hyperbolic lamination without invariant transverse measure containing an exceptional minimal set."** Without clause (0): B1 kills the finitely-many-compact-leaves subclass, B1′ the finitely-many-finite-type-leaves subclass, the rest is open. |
| **T5 = clause (iv)** | (iv) must read: the holonomy-invariant transverse measure that necessarily exists is scaled by the flow with modulus e^{−t}; the ALKL justification is deleted | **STANDS-NARROWED** | "Necessarily exists" FALLS (T2). "Modulus exactly e^{−t}" STANDS under **(0-coh) plus either H̄²_F ≅ R or the eigen-measure hypothesis φ^t_*µ = c(t)µ** — and I give a proof (§5.2) that needs no global conformality: pair the Ruelle–Sullivan current with (15). A-I as printed STANDS under its own printed hypotheses (global (31) + eigen-measure), which S4′ as posed does not supply. Corollary: **µ is never supported in N.** "Delete the ALKL justification" — replace, do not delete: a transverse measure is still what any leafwise trace formula (Deninger's χ_Co(F,µ)δ₀ term; Leichtnam 5]'s L² structure) needs; only the citation of ALKL's *theorem* is void. Exact text in §5.4. |
| **T6 = N10** | Print forces α = 0 on a closed 3-manifold only when the flow is everywhere transverse to F; with preserved leaves the manifold question is open | **STANDS-NARROWED** | [Den05] p. 24 Rem. 2 is indeed under Cor. 5.5's "everywhere transversal" (read). But α = 0 is **also forced, trivially, by any compact preserved leaf** (global (31): area(T) = e^{αt}area(T); cohomological (15): δ_T is flow-invariant), so the whole KMNT/ALKL class has α = 0 — which is what [x-06] p. 8 asserts in its p. 6 setting ("fixed points … in finitely many compact leaves"). Correct form: **the manifold question for α = 1 is open only for foliated flows none of whose preserved leaves is compact.** |

**The one finding that changes the frontier (mine, single-check, written out in §1.5 and §2.3 — Theorem F-1).** Under
the α = 1 clause the program must add in *some* form — Deninger's own definition of α = 1 is "φ^{t*} acts by e^t on the
one-dimensional H̄²_F(X)" ([Den05] p. 27, read) = Leichtnam 4] (15) — **no holonomy-invariant transverse measure of a
compact S4′ object can be supported in the non-transverse set N**, because on N every leaf is preserved, so any such
measure is automatically flow-invariant, and its Ruelle–Sullivan pairing with (15) gives m = e^t·m. Consequences: N
contains no compact leaf and no euclidean leaf; by Candel Cor. 4.2 (p. 497, read) **every preserved leaf is hyperbolic**;
and if the flow is *globally* conformal along the archimedean leaf ((31) on TF|L) and has a fixed point there, Schwarz–Pick
forces that leaf to be C, Candel Thm 4.3 (p. 498, read) puts an invariant measure inside N, and **no such object exists**.
So the adjudication's corridor ("N contains a leaf conformal to C, χ = +1, carrying the measure") is not merely unproved;
it is the one configuration the α = 1 clause forbids. Leichtnam's printed caution (2013 Comment 6, read: Deninger "told us
privately that this assumption (φ^t)^*(g) = e^t g might be too strong") is thereby made precise: with a fixed point on a
compact lamination, (31) is not too strong, it is inconsistent.

---

## §1. T1 = A-II

### 1.1 (a) The source property is an additional hypothesis, not a consequence of S4′'s four clauses

**Where the adjudicator's hypothesis comes from in print.** [Den05] = `x-20`, p. 31, Remark 7.6(4), verbatim: "We will see
below that in our new context metrics g on TF can exist for which the flow has the conformal behaviour (31). **Assuming we
are in such a situation** and that F is 2-dimensional, we have: |det(T_xφ^{kl(γ)}|T_xF)| = e^{kl(γ)} … and
|det(T_xφ^t|T_xF)| = e^t for a fixed point x." p. 32, Remark 5: "**In the setting of the preceeding remark** the
automorphisms e^{−(k/2)l(γ)}T_xφ^{kl(γ)} … respectively e^{−t/2}T_xφ^t of T_xF for a fixed point x are orthogonal
automorphisms." p. 33, the Fact: "**In the situation of the preceeding remark** … For fixed points, ε_x = 1 is automatic
and we have: T_xφ^t = e^{t/2}O_t for O_t ∈ SO(T_xF)." So in Deninger the fixed-point conformality is a *corollary of the
global conformality (31)*, g(T_xφ^t v, T_xφ^t w) = e^t g(v, w) for all v, w ∈ T_xF (p. 27, read). Leichtnam 2013 (`r3s-20`
p. 14) prints it as a separate axiom 3]a, (13), and p. 15 Comment 6 says why: "The stronger assumption ∀t, (φ^t)^*(g) =
e^t g implies (13) … Deninger told us privately that this assumption (φ^t)^*(g) = e^t g might be too strong."

**S4′ as posed** (ledger §15, read): clause (ii) is the closed-orbit half of the Fact only; clause (iii) says "a
flow-preserved leaf of nonzero Euler characteristic" and mentions no fixed point; there is no α clause. The adjudicator's
A-II statement does list "(ii∞)" as a hypothesis, but the enacted S16-4 says "In any S4′ object …" without it.

**[F] The fixed-point behavior does not follow from (i)–(iv).** Counter-configuration at the level of the leaf: let L ≅ S² be
a compact preserved leaf and let φ^t|L be a gradient-like flow from a hyperbolic source at the north pole to a hyperbolic
sink at the south pole (in the linearizations, Y = (1/2)·Id at the source and Y = −(1/2)·Id at the sink; this is a smooth
flow on S², e.g. the flow of z ↦ e^{t/2}z on Ĉ). It has no closed orbits, so it is consistent with clause (i) restricted to
L (which only forbids closed orbits inside leaves, §1.3); clause (ii) concerns the γ_p, which lie off L; clause (iii) is
satisfied by L itself (χ = 2 ≠ 0) whenever L lies in the accumulation set of the γ_p; clause (iv) says nothing about L.
Nothing in (i)–(iv) distinguishes the sink from a source. So A-II's step (2) — "every zero is a source of index +1" — is
exactly where an extra hypothesis enters, and without it A-II's conclusion (χ(L) = 0 for every compact preserved leaf)
is not derivable: this S² leaf has χ = 2 and two fixed points. **Verdict on (a): (ii∞) is an added clause.**

**What clause (0) must be, and why the program must add it anyway.** Two forms, both printed, both needed for the
explicit formula:
- **(0-fix)** = Leichtnam (13) = Deninger's fixed-point Fact: at every fixed point x, e^{−t/2}T_xφ^t|T_xF ∈ SO(T_xF).
  *Why needed:* the archimedean term of the explicit formula is +r₁(1 − e^{−2t})^{−1} on t > 0 and has the e^t-twisted shape
  on t < 0 ([Den05] (35) p. 32; Leichtnam 2013 (12) p. 14). Deninger's fixed-point contribution W_x carries the sign
  ε_x = sign det(1 − T_xφ^t|T_xF) and the factor det(T_xφ^t|T_xF) = e^t on R<0 (p. 32, read). ε_x = +1 for all t excludes
  a saddle but *not* a sink (for both eigenvalues real and negative, (1 − e^{tλ})(1 − e^{tμ}) > 0 as well); it is the
  determinant condition det = e^t, i.e. Re λ + Re μ = 1, together with ε_x = 1, that forces both real parts positive — a
  source. (13) is the conformal sharpening of that. A-II needs only "both real parts positive"; I keep (13) as the clause
  because it is the printed one.
- **(0-coh)** = Deninger's definition of α = 1 = Leichtnam 4] (15): H̄²_F(X) is one-dimensional, spanned by the class
  of a leafwise area form λ_g, and φ^{t*}[λ_g] = e^t[λ_g]. [Den05] p. 27, verbatim: "in a dynamical system corresponding to
  number theory we must have α = 1. **This means that the flow φ^{t*} would act by multiplication with e^t on the
  one-dimensional space H̄²_F(X).** As explained before this would be the case if φ^t were conformal on TF with factor
  e^t: (31)". *Why needed:* the N p^k coefficients for k ≤ −1 (p. 27, last paragraph) and clause (ii)'s p^{1/2} are the
  α = 1 shape; without an α clause, S4′ has no mechanism producing them beyond the orbits themselves.
- **(0-glob)** = (31) itself. **The program must NOT add this one** (Theorem F-1(c), §1.5): with a fixed point on a compact
  lamination it is inconsistent.

**[F] Recommended clause (0) for S4′:** "(0) the flow has a fixed point x_∞ (one per archimedean place) lying in clause
(iii)'s leaf, at which e^{−t/2}T_{x_∞}φ^t|T_{x_∞}F ∈ SO(2) [(13)]; and φ^{t*} = e^t on the one-dimensional H̄²_F(X)
[(15)]." Global conformality (31) is explicitly *not* assumed.

### 1.2 (b) Isolation of fixed points

Under (0-fix): T_xφ^t|T_xF = e^{t/2}O_t with t ↦ O_t a continuous one-parameter subgroup of SO(2), hence O_t = exp(tS)
with S skew, so T_xφ^t|T_xF = exp(t((1/2)Id + S)) and the leafwise linearization of Y_φ at x has eigenvalues 1/2 ± iθ.
Both real parts are 1/2 > 0: x is a hyperbolic source of the leafwise flow φ^t|L, hence isolated in L (inverse function
theorem applied to Y_φ|L, which is C¹ since the flow is smooth along leaves). On a compact L, isolated ⇒ finitely many.
**Without (0-fix) nothing forces isolation** (a leafwise flow can have a curve of zeros). Note also that a fixed point of φ
lies only in a preserved leaf ([x-18] p. 4 Dictionary 4, read: "the leaf of F containing a fixed point is φ-invariant"),
so the leafwise analysis is the whole analysis. **(b) holds under (0-fix).**

### 1.3 (c) Transversality of the γ_p, and Poincaré–Bendixson on S²

**(ii) forces transversality — checked.** Let N = {x : the φ-orbit of x lies in the leaf L_x} (this is the correct
definition of the non-transverse set on a foliated space, where TX does not exist; §3.2 shows it is closed, saturated and
flow-invariant). If some point of γ_p were in N then γ_p ⊂ L for a leaf L, and the flow direction Y_φ(x) ∈ T_xF along γ_p
would be a fixed vector of T_xφ^{log p}|T_xF, i.e. an eigenvector with eigenvalue 1; but clause (ii) says
T_xφ^{log p}|T_xF = p^{1/2}·O, all of whose eigenvalues have modulus p^{1/2} ≠ 1. So γ_p ∩ N = ∅: γ_p is nowhere tangent to
F. (On a manifold the same reads: the tangency set {Y_φ ∈ TF} is flow-invariant because Tφ^t(TF) = TF, so tangency at one
point of γ_p means tangency along it, hence containment in a leaf for a C¹ foliation.) **Holds.**

**Poincaré–Bendixson step, written out.** Let L ≅ S² be a compact preserved leaf whose only equilibria are two hyperbolic
sources p₁, p₂ (this is what (0-fix) + Poincaré–Hopf leave, §1.4). Take y ∈ L ∖ {p₁, p₂}. Its ω-limit set ω(y) is nonempty,
compact, connected and invariant (L compact). *ω(y) contains no source:* a hyperbolic source p has a neighborhood U with
φ^{−s}(U) ⊂ U for s ≥ 0 and ∩_{s≥0} φ^{−s}(U) = {p} (Lyapunov function V = |z|² in linearizing coordinates, dV/dt > 0 on
U ∖ {p}); if φ^{t_n}(y) ∈ U for t_n → ∞ then y ∈ φ^{−t_n}(U) for all n, so y = p. Hence ω(y) is a compact invariant set
of a C¹ flow on S² containing no equilibrium, and the Poincaré–Bendixson theorem on the sphere (valid for C¹ flows; S²
minus a point of ω(y)'s complement is a plane) says ω(y) is a **periodic orbit** c ⊂ L. Then c is a closed orbit of φ
contained in a leaf, i.e. c ⊂ N. By clause (i) every closed orbit of φ is some γ_p, and by the paragraph above γ_p ∩ N = ∅.
**Contradiction. Holds** — but it consumes clause (i)'s "exactly": without the word "exactly" (Leichtnam 2] prints only an
injection primes → closed orbits) the S² case is not excluded by this route.

### 1.4 (d) Orientability and the classification

A leaf carries the leafwise holomorphic structure, hence a canonical orientation; a compact leaf is a closed surface
(leaves have no boundary). So L is a closed orientable surface, χ(L) = 2 − 2g. Under (0-fix), Poincaré–Hopf for the
C¹ vector field Y_φ|L with finitely many zeros all of index +1 gives χ(L) = #(Fix ∩ L) ≥ 0, hence g ∈ {0, 1}: either L ≅ T²
with no fixed point, or L ≅ S² with exactly two sources — excluded by §1.3. **Holds under (0-fix).** Under (0-coh) the same
conclusion is immediate and stronger (no compact preserved leaf at all): §1.5.

### 1.5 (e) Parabolicity: DERIVED or ASSUMED? — Assumed from an expectation, and false under the α = 1 clause

**Where the adjudicator excludes the disk.** A-II(c): "[Den05] p. 33 Remark 7 (read: for K = Q, χ_Co(F, ν) = 0 for all
transverse measures, hence a leaf that is a plane, a torus or a cylinder) and Candel Theorem 4.3 … since torus and cylinder
have χ = 0 and the sphere is compact, clause (iii)'s leaf is conformal to the euclidean plane C, with χ = +1." Three
defects, each fatal on its own:

1. **Remark 7 is an expectation and presupposes the measure.** p. 33–34, read: "we would expect in particular that for a
   preferred transverse measure µ we have χ_Co(F, µ) = −log|d_{K/Q}| … In the unramified case … Hence there is an F-leaf
   which is either a plane, a torus or a cylinder c.f. [9]." The inference runs through Candel: χ(X, ν) = 0 for a nonzero ν
   means the metric is not hyperbolic-conformal, so *some* leaf is non-hyperbolic. It needs a nonzero invariant ν to exist
   — the very thing A-III then claims to derive from the plane leaf. **Circular.**
2. **Remark 7 does not say which leaf.** "There is an F-leaf" — nothing identifies it with the archimedean (preserved)
   leaf. A compact torus leaf anywhere, or a non-preserved cylinder, satisfies it.
3. **For every K ≠ Q Remark 7 predicts the opposite.** |d_{K/Q}| > 1 for K ≠ Q (Minkowski), and p. 33, read: "If K/Q is
   ramified at some finite place … χ_Co(F, µ) < 0 … it follows that χ_Co(F, ν) < 0 for all non-trivial transverse measures
   ν. Hence by a result of Candel [9] there is a Riemannian metric on TF such that **every F-leaf has constant curvature
   −1**." So the very source cited makes the archimedean leaf *hyperbolic* for all K ≠ Q, while S16-4 declares "conformal
   to C … uniform in the number field."

**What is actually true under the clause the program must add — Theorem F-1 [F, single-check].**
*Setting.* X a compact Riemann surface lamination (compact metrizable foliated space with 2-dimensional leaves and
leafwise holomorphic charts; this is Candel's setting, `candel.txt` p. 491 §1.1, read), g a leafwise metric in the
conformal class, φ a foliated flow (leafwise smooth, transversally continuous, mapping leaves to leaves), N its
non-transverse set (§3.2: closed, saturated, and every leaf in N is preserved).
*(A) Any holonomy-invariant transverse measure µ with supp µ ⊂ N is flow-invariant, φ^t_*µ = µ.* Proof. Let T be a
transversal in a chart and x ∈ T ∩ N. The path s ↦ φ^s(x), s ∈ [0, t], lies in L_x (x ∈ N). Cover it by a finite plaque
chain; for y ∈ T near x the path s ↦ φ^s(y) runs through the same charts (uniform continuity), and for y ∈ N it lies in
L_y, so within each chart it stays in one plaque of L_y: it is the holonomy lift of the chain. Hence on V_x ∩ N (V_x a
neighborhood of x in T) the transverse map induced by φ^t coincides with the holonomy map h_x along that chain, and
µ(h_x(B)) = µ(B) for Borel B ⊂ V_x by holonomy invariance. Since µ is concentrated on N and T ∩ N is covered by countably
many V_x, µ(φ^t(B)) = µ(B) for every Borel B ⊂ T. ∎
*(B) Under (0-coh) no such µ ≠ 0 exists.* Proof. Let C_µ be the Ruelle–Sullivan current of µ: ⟨C_µ, ω⟩ = ∫_X ω dµ
(leafwise integration of the 2-form ω over plaques against µ). It is a closed, continuous current on A²_F(X), so it pairs
with the reduced cohomology H̄²_F(X). Change of variables under the foliated homeomorphism φ^t gives
⟨C_µ, φ^{t*}ω⟩ = ⟨C_{φ^t_*µ}, ω⟩ = ⟨C_µ, ω⟩ by (A). Apply to ω = λ_g: by (15), φ^{t*}λ_g = e^t λ_g + (limit of exact forms),
so ⟨C_µ, φ^{t*}λ_g⟩ = e^t⟨C_µ, λ_g⟩. Hence m_µ(X) := ⟨C_µ, λ_g⟩ = ∫ area_g dµ satisfies m_µ(X) = e^t m_µ(X) for all t, while
0 < m_µ(X) < ∞ (µ ≠ 0 positive, X compact, g continuous). Contradiction. ∎ (Under (0-glob) the same follows pointwise:
areas of pieces of preserved leaves scale by e^t while µ does not move — A-I with β = 0.)
*(C) Consequences for N.* (C1) N contains no compact leaf (its Dirac transverse measure δ_T is holonomy-invariant and
supported in N). (C2) N contains no euclidean leaf: Candel Thm 4.3 (`candel.txt` p. 498, verbatim: "if L is a euclidean
leaf, then there exists µ with support in L̄ and χ(M, µ) = 0") would give a µ supported in L̄ ⊂ N. (C3) N, being a closed
saturated subset of X, is itself a compact Riemann surface lamination; by (B) it has no invariant transverse measure, so by
Candel Cor. 4.2 (p. 497, verbatim: "If M is a compact Riemann surface lamination with no invariant transverse measure, then
M has a conformal metric with curvature −1 on each leaf") **every preserved leaf is hyperbolic.** (C4) In particular
clause (iii)'s leaf is non-compact (C1) — A-II's headline, obtained without any fixed-point hypothesis — and is a
hyperbolic Riemann surface, not C.
*(D) The globally conformal case is dead.* Suppose in addition that φ^t is conformal along the archimedean leaf L with
factor e^t ((31) restricted to TF|L) and has a fixed point x_∞ ∈ L. Then φ^t|L is an orientation-preserving conformal
diffeomorphism of the Riemann surface L, hence holomorphic, so {φ^t|L} is a one-parameter group in Aut(L) fixing x_∞ with
|T_{x_∞}φ^t| = e^{t/2} in the metric g. If L were hyperbolic, lift to the disk fixing a lift of x_∞: the lift is a
Poincaré isometry, so its derivative at the fixed point has modulus 1, and the modulus of a derivative at a fixed point is
the same in every conformal metric (the conformal factor cancels) — contradicting e^{t/2} ≠ 1 (Schwarz–Pick). So L is
non-hyperbolic: Ĉ, C, C^* or a torus (uniformization). Torus and C^*: the identity component of Aut is translations,
resp. z ↦ az, with no fixed point unless trivial — excluded. Ĉ: compact, excluded by (C1) (or: the second fixed point of a
one-parameter subgroup of PSL(2, C) is a sink, violating (0-fix), which (31) implies). Hence **L ≅ C**, and by (C2) this
contradicts (B). So: **(31) along L + a fixed point in L + compactness ⇒ no object.** ∎

*Hypotheses checked against S4′ + clause (0).* X compact ✓; Riemann surface lamination ✓ (S4′: "Riemann-surface
leaves"); leafwise metric continuous ✓; (15) = (0-coh) ✓ once added; a fixed point in the archimedean leaf ✓ once (0-fix)
is added in the form above (Deninger's dictionary p. 26; Leichtnam 2]). Candel's two statements are read at their pages.
**Nothing recalled is load-bearing** except: Ruelle–Sullivan currents of invariant transverse measures are closed and
continuous (standard; Candel p. 490 states the isomorphism between invariant transverse measures and H₂(M, R_F)), the
uniformization theorem, and the automorphism groups of Ĉ, C, C^*, tori.

**Verdict on (e): parabolicity was ASSUMED (from an expectation, circularly, for K = Q only), and it is FALSE under
(0-coh) and INCONSISTENT under (0-glob).** The adjudicator's table row A3 ("Archimedean leaf: non-compact, conformal to C,
χ = +1") and S16-4's "conformal to C, χ = +1" must be struck and replaced by "non-compact and hyperbolic".

### 1.6 Verdict on T1

**STANDS-NARROWED.** Narrowed statement: *For S4′ objects carrying clause (0) in the form (0-fix), every compact preserved
leaf is a torus without fixed points and clause (iii)'s leaf is non-compact (A-II steps 1–5, verified). For S4′ objects
carrying (0-coh), there is no compact preserved leaf at all, and every preserved leaf — clause (iii)'s included — is a
hyperbolic Riemann surface; a euclidean or spherical preserved leaf is impossible (Theorem F-1). For S4′ as posed (four
clauses, no clause (0)), neither conclusion is derivable (§1.1).* The clause "conformal to C with χ = +1" FALLS.
