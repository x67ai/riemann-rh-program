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

---

## §2. T2 = A-III

### 2.1 Does Candel's theorem apply to S4′ objects?

Candel, *Uniformization of surface laminations*, Ann. Sci. ENS (4) 26 (1993) 489–516 (NUMDAM scan, `candel.txt` in the
session scratchpad; OCR-degraded but the quoted sentences legible). p. 490, first theorem, verbatim: "Let M be a compact
oriented surface lamination with a riemannian metric g. Then χ(M, µ) < 0 for every positive invariant transverse measure
if and only if g is conformal to a metric of curvature −1. In particular, this holds true if M has no invariant measure."
p. 491, §1.1: "Let M be a separable, locally compact, metrizable space. We say that M is a p-dimensional lamination if
there is a cover of M by open sets U_i … and homeomorphisms φ_i : U_i → D_i × T_i with D_i open in R^p, and such that the
overlap maps … are of the form (z, t) ↦ (ψ_{ij}(z, t), τ_{ij}(t)) where each map ψ_{ij} is of class C^∞ in the first
variable with all partial derivatives continuous in all variables." p. 493: "A riemannian metric on the lamination M is a
smooth and positive definite section of S²T*M" (smooth = leafwise smooth, transversally continuous). p. 489–490: a Riemann
surface lamination is the same as an oriented surface lamination with a conformal class of such metrics (Ahlfors–Bers).
**An S4′ object — compact metrizable foliated 3-space with Riemann-surface leaves — is exactly a compact Riemann surface
lamination in Candel's sense** ([Den05] p. 28–29's definition of foliated space, read, is the same local model). The
theorem applies verbatim. **Yes.**

### 2.2 Does the conclusion need a parabolic leaf?

The adjudicator's inference is the contrapositive of the "in particular" clause: no invariant measure ⇒ g conformal to
curvature −1 ⇒ every leaf hyperbolic; so a non-hyperbolic leaf ⇒ an invariant measure exists. Candel's Theorem 4.3 (p. 498,
read) is the sharp form: "If χ(M, µ) < 0 for every positive invariant transverse measure µ, then all leaves are hyperbolic
Riemann surfaces. In fact, if L is a euclidean leaf, then there exists µ with support in L̄ and χ(M, µ) = 0", and p. 498
above it: the compact cases (sphere, torus) are handled by the Dirac measure. So the conclusion **needs a non-hyperbolic
leaf** — plane, cylinder, sphere or torus — and A-III supplies it **only through A-II(c)**, i.e. through T1(e), which
falls (§1.5). **Yes, and yes.**

### 2.3 If the archimedean leaf could be hyperbolic, does A-III fall? — It does, and more

(1) Under S4′ as posed plus (0-fix) only, nothing constrains the conformal type of the archimedean leaf, so no
non-hyperbolic leaf is available and Candel gives nothing. (2) Under (0-coh), Theorem F-1 (§1.5) shows the archimedean
leaf and every other preserved leaf **is** hyperbolic, and that the archimedean lamination N carries **no** invariant
transverse measure. So A-III's intended witness (a euclidean preserved leaf) is not merely undetermined; it is excluded.
(3) Could an invariant transverse measure still exist for some other reason? Only if some **non-preserved** leaf is
non-hyperbolic (Candel 4.3 then gives µ supported in its closure), or if the object is arranged so (Leichtnam 5] posits
one). Neither is derivable from S4′ + clause (0). Under Deninger's expectation-level Remark 7 for K = Q (χ_Co(F, ν) = 0
for the preferred ν), the euclidean leaf it produces must therefore be a *non-preserved* leaf whose closure carries µ,
while N stays measure-free and hyperbolic; for K ≠ Q Remark 7 wants all leaves hyperbolic and gives no measure at all.
I record this as a consistency remark, not a ruling (it rests on an expectation).

### 2.4 Verdict on T2

**FALLS.** The derivation's only non-trivial input (a euclidean archimedean leaf) is not derived from the printed
hypotheses and is contradicted under the α = 1 clause. The proposition "an invariant transverse measure exists" is
**undetermined** as a consequence of S4′ + clause (0); it remains what Leichtnam printed it as — an assumption (2013 5],
2008 5], read). What *is* a theorem (F-1(B)): whatever invariant transverse measure clause (iv) posits, **it is not
supported in N**.

---

## §3. T3 = A-IV

### 3.1 (a) Closed leaf ⇒ compact leaf, for compact foliated spaces (laminations) — PROVED

**Claim.** Let X be a compact metrizable foliated space with a finite atlas of charts U_i ≅ D_i × T_i (D_i an open disk in
R², T_i a locally compact metrizable space; transition maps of the form (x, y) ↦ (f_{ij}(x, y), g_{ij}(y)) with g_{ij} a
local homeomorphism between open subsets of transversals). If a leaf L is closed as a subset of X, then L is compact in
its leaf topology; conversely a compact leaf is closed (compact subset of a Hausdorff space).

**Proof.** *Step 0: each leaf is a countable union of plaques.* A plaque P of U_i is a connected open subset of R²; P ∩ U_j
is open in P, hence has countably many components, and each component maps into a single plaque of U_j (the transition
map preserves the transverse coordinate). Starting from one plaque and iterating over plaque chains, L is a countable
union of plaques; in particular L ∩ T_i is countable for every i. *Step 1: shrink the plaques.* Choose closed disks
D̄'_i ⊂ D_i such that the sets D'_i × T_i still cover X (compactness of X and a Lebesgue-number argument on a finite atlas
with a compatible metric). Then every closed plaque D̄'_i × {y} is compact, hence closed in X, and L is the countable union
of the closed plaques D̄'_i × {y}, y ∈ L ∩ T_i. *Step 2: Baire.* L is closed in the compact metrizable X, so L with the
subspace topology is a compact metric space, hence a Baire space. A countable union of closed sets covering a Baire space
has one member with nonempty interior: there are i, y₀ ∈ L ∩ T_i and an open W ⊂ X with ∅ ≠ W ∩ L ⊂ D̄'_i × {y₀}. Pick
(x₀, y₀) ∈ W ∩ L with x₀ ∈ D'_i; W contains a product neighborhood D'' × V of (x₀, y₀). For z ∈ V ∩ L, (x₀, z) ∈ W ∩ L ⊂
D̄'_i × {y₀}, so z = y₀: **L ∩ V = {y₀}**, i.e. y₀ is isolated in L ∩ T_i. *Step 3: holonomy propagates isolation.* Let
y₁ ∈ L ∩ T_j be arbitrary. A plaque chain in L from the plaque of y₀ to that of y₁ defines a holonomy map h: V₀ → T_j, a
homeomorphism from an open neighborhood V₀ ⊂ V of y₀ onto an open neighborhood of y₁, with h(y₀) = y₁. Holonomy along a
leafwise path maps points of L to points of L and its inverse does too, so h(V₀ ∩ L) = h(V₀) ∩ L; since V₀ ∩ L = {y₀},
h(V₀) ∩ L = {y₁}: every point of L ∩ T_j is isolated in L ∩ T_j. *Step 4: the topologies agree.* In every chart, L ∩ U_j
is a disjoint union of plaques D_j × {y}, y ∈ L ∩ T_j, each of which is open in L ∩ U_j for the subspace topology (product
of D_j with the open set {y} of L ∩ T_j). So the subspace topology on L is the leaf topology, and L, compact in the
former, is a compact surface. ∎

**Remarks.** (i) The adjudicator's parenthetical "(a closed leaf is proper …)" asserts Step 4 without Steps 2–3; the
argument is standard for foliations of manifolds and, as shown, needs only Baire and holonomy, so it holds for
laminations. (ii) The same proof works with X replaced by any locally compact metrizable open saturated subset W (used in
§3.4): a leaf closed in W is proper in W. **(a) STANDS.**

### 3.2 (b) N is closed, saturated, flow-invariant, and consists exactly of the preserved leaves — PROVED

On a foliated space TX does not exist, so "Y_φ(x) ∈ T_xF" must be replaced. **Definition.** A foliated flow is a continuous
R-action by homeomorphisms that in charts has the form φ^t(x, y) = (f_t(x, y), g_t(y)) for small t (leafwise smooth f,
continuous g); this is the local form under which the phrases "maps leaves to leaves" and "smooth along leaves" ([Den05]
7.3, p. 30, read) make sense, and it is what KMNT Lemma 1.10's proof uses on manifolds (`kmnt.txt`, read). Set
**N := {x ∈ X : φ^t(x) ∈ L_x for all t ∈ R}.**

*Local characterization.* x = (x₀, y) ∈ N iff g_t(y) = y for all small t (the induced local transverse flow is stationary
at y). (⇐) If g_t(y) = y for |t| < ε, the orbit of x stays in the plaque of x for |t| < ε, hence in L_x. Let A = {t :
φ^t(L_x) = L_x}; it is a subgroup of R (φ^t maps leaves to leaves, so φ^t(L_x) is a leaf, equal to L_x iff φ^t(x) ∈ L_x)
and contains (−ε, ε), hence A = R. (⇒) If the orbit lies in L_x, the path t ↦ φ^t(x) is continuous into X with values in
L_x; in a chart its transverse coordinate is a continuous map from an interval into the countable set L_x ∩ T (Step 0 of
§3.1), hence constant (a connected subset of a countable metric space is a point). So g_t(y) = y for small t.

*Saturation.* If x ∈ N and x' lies in the same plaque, x' ∈ N (same y). If x'' lies in an adjacent plaque of the same
leaf, pick z in the overlap: z ∈ N by the plaque step; in the chart of x'', z's transverse coordinate is stationary because
the orbit of z stays in the plaque of z, which meets the chart of x'' inside the plaque of x''. Induct along plaque
chains: L_x ⊂ N. Conversely a preserved leaf lies in N by definition. So **N is the union of the preserved leaves.**

*Closedness.* X ∖ N is open: if x ∉ N, some small t has g_t(y) ≠ y; by continuity of g_t and Hausdorffness of T, g_t(y') ≠
y' for y' near y, so a neighborhood of x misses N. **N is closed.** Flow-invariance is immediate from the definition.

*Answer to the orchestrator's sub-questions.* "Is the transverse component leafwise constant?" — in the only sense
available on a foliated space, yes: stationarity of the induced transverse local flow is a property of the plaque and
propagates along plaque chains, as shown. "Is N closed when the transverse structure is only topological?" — yes, by the
open-complement argument, which uses only continuity of g_t. **(b) STANDS.**

### 3.3 The structural conclusion, and consequences (α), (β), (γ)

*Steps 2–3 of A-IV.* Given a non-compact preserved leaf L: L is not closed (§3.1), so L̄ ⊋ L; L ⊂ N and N closed give
L̄ ⊂ N; the closure of a leaf is saturated (if z ∈ L̄ and z' is in z's plaque, every product neighborhood of z' meets L
because L ∩ U is a union of full plaques), so L̄ ∖ L is a nonempty union of leaves, each in N, each preserved by §3.2.
**Verified.** The input "L non-compact" comes from T1: under (0-fix) via A-II; under (0-coh) via Theorem F-1(C1) with no
fixed-point analysis. Under S4′ as posed it is not available (§1.1). So the conclusion "N is a compact saturated
lamination of preserved leaves, never one leaf, never a finite union of compact leaves" **STANDS for S4′ + clause (0)**,
and under (0-coh) it strengthens to: *N contains no compact leaf at all and every leaf of N is hyperbolic.*

*(α) ALKL.* `r3s-17` Abstract (memoir p. v, read): "Assume the closed orbits of φ are simple and its preserved leaves are
transversely simple. In this case, there are finitely many preserved leaves, which are compact." §1.1 (p. 1): "If these
fixed points of φ̄ are simple, then the leaves preserved by φ are called transversely simple." §4.1.2 (p. 100, read):
"The leaves preserved by φ that correspond to simple fixed points of φ̄ are said to be transversely simple. If all leaves
preserved by φ are transversely simple, then φ (or Z) is called transversely simple … Suppose φ is transversely simple
unless otherwise stated. Then M⁰ is a finite union of compact leaves because every fixed point of φ̄ is isolated."
Remark 4.1.1 (p. 101): "Only the completeness of Z and compactness of M⁰ are needed to extend the indicated notions."
`r3s-30` p. 2 (read): "A preserved leaf L is called transversely simple if the corresponding fixed points p̄ of φ̄ are
simple. In this case, φ̄^t_* = e^{κt} on T_{p̄}Σ ≡ R for some κ = κ_L ∈ R^×." So: the finiteness and compactness of the
preserved leaves are **consequences of the hypothesis "transversely simple" (a nonzero transverse exponent at each
preserved leaf), which ALKL REQUIRE** for Theorem 1.3.10 — they do not merely treat that case. A non-compact preserved leaf
violates the consequence, hence the hypothesis. **(α) STANDS** for S4′ + clause (0). (The memoir's own words for the
missing case: p. 1, "more generality is needed to draw arithmetic consequences".)

*(β) B1 vacuous.* True as stated for S4′ + clause (0), since N is not a finite union of compact leaves. **But see §3.4:
the mechanism of B1 reaches further than its printed hypothesis, and "the closed-3-manifold case is OPEN" is overstated.**

*(γ) Leichtnam's Assumption 2].* The inconsistency argument is: compactness of S_K + Leichtnam's own axioms ((13) = (0-fix),
or 4] (15) = (0-coh)) ⇒ the archimedean leaf is non-compact ⇒ its closure adds preserved leaves ⇒ 2]'s "transverse to all
the leaves different from the ones containing the r₁ + r₂ fixed points" fails. Valid **given compactness.** Does Leichtnam
assume S_K compact? I searched the extracted text: in `r3s-20` §4 (pp. 13–22) the string "compact" occurs only inside
"C_compact" (test functions) and in §3.4's unrelated example; in the 2008 author copy §5.1 likewise only "C_compact".
Leichtnam 2013 1] says "the path connected components of S_K are three dimensional" and nothing about compactness;
Comment 7 (p. 16) wants transversals "of the type ]0,1[×Z_p". Leichtnam 2007 (`r3s-21` p. 2, read): L is "σ-compact" and
"The quotient L/Q^{+*} allows to **compactify** the space L × R^{+*}/Q^{+*}" — so the 2007 S_Q is presented as a
compactification, i.e. compact, and its archimedean part L/Q^{+*} is a whole sublamination with "a fixed point in
L/Q^{+*}", not a single leaf. The adjudicator's "compactness is required by his own Assumption 6] (trace-class)" is an
inference, not print. **(γ) must be restated:** *"Leichtnam's Assumption 2] (2008, 2013) is inconsistent with compactness
of S_K; Leichtnam does not print compactness in either axiom list, so the lists are not self-contradictory as printed;
but every compact realization — including the 2007 compactified shape S_Q — must weaken 2]."* Not a defect of the axioms
as printed; a defect of any compact model of them.

### 3.4 B1′ — the length-group kill extends to finitely many finite-type leaves [F, single-check]

**Statement.** Let M be a closed 3-manifold, F a C¹ codimension-one foliation, φ a C¹ foliated flow, N its non-transverse
set, M₀ = M ∖ N. If N is a finite union of leaves L₁, …, L_m each with rank_Z H₁(L_a) < ∞ (finite type), then the group Λ
generated by the lengths of the closed orbits of φ is finitely generated. Hence no such (M, F, φ) satisfies S4′ (i)+(ii).

**Proof.** (1) On M₀ the flow is transverse to F and foliated, so KMNT's 1-form ω (ω|TF = 0, ω(φ̇) = 1) is defined and
closed (`kmnt.txt` Lemma 1.10 and its proof, read: closedness ⇔ the flow maps leaves to leaves, proved in flow-box
coordinates, which exist on any open set where the flow is transverse). For a closed orbit c ⊂ M₀ of least period ℓ(c),
∫_c ω = ℓ(c). Every γ_p lies in M₀ (§1.3). So Λ ⊂ [ω](H₁(M₀; Z)), and it suffices to show rank H₁(M₀) < ∞. (2) Pass to the
orientation double cover of M if M is non-orientable; the lifted flow's closed orbits have lengths in {ℓ, 2ℓ}, N lifts to
a finite union of finite-type leaves, and finite generation descends. So assume M orientable; then a properly embedded
orientable surface is two-sided. (3) Remove the leaves of N one at a time. Given the open manifold W_k = M ∖ (L₁ ∪ … ∪
L_k) and N_k = N ∩ W_k, closed in W_k and a finite union of leaves: among them there is one closed in W_k. [Order the
leaves of N_k by L_a ≼ L_b iff L_a ⊂ cl_{W_k}(L_b) and take a ≼-minimal L_a. If cl(L_a) ⊋ L_a then some L_b ⊂ cl(L_a) with
b ≠ a, so by minimality L_a ⊂ cl(L_b), and K := cl(L_a) = cl(L_b) is a closed set in which both L_a and L_b are dense. K is
locally compact and a countable union of compact plaques belonging to finitely many leaves, so by Baire some leaf L_c ⊂ K
has a plaque with interior in K; §3.1 Step 3 then makes L_c open in K; an open subset of K meets the dense L_a, so c = a;
but L_b is also dense in K and disjoint from the open L_a — contradiction. Hence cl(L_a) = L_a.] By §3.1 Remark (ii), that
leaf L is properly embedded in W_k, two-sided, with a product tubular neighborhood ν ≅ L × (−1, 1). (4) Mayer–Vietoris
for W_k = (W_k ∖ L) ∪ ν, with (W_k ∖ L) ∩ ν ≃ L ⊔ L:
H₁(L) ⊕ H₁(L) → H₁(W_k ∖ L) ⊕ H₁(L) → H₁(W_k), so rank H₁(W_k ∖ L) ≤ rank H₁(W_k) + rank H₁(L). (5) Iterating,
rank H₁(M₀) ≤ rank H₁(M) + Σ_a rank H₁(L_a) < ∞. So Λ is finitely generated, while ⟨log p⟩ has infinite rank (unique
factorization). ∎

**Consequences.** (i) The adjudicator's picture "one plane leaf (χ = +1) whose closure adds a few compact leaves" is dead
on a closed 3-manifold by the *same* period-group mechanism as B1: a plane has H₁ = 0. (ii) The exact necessary condition
for S4′ (i)+(ii) on a closed 3-manifold is **rank_Z H₁(M ∖ N; Z) = ∞** (equivalently: the period group of ω on M ∖ N has
infinite rank). (iii) Therefore N must have infinitely many leaves, or a leaf of infinite type (infinite genus or
infinitely many ends). This matches, rather than contradicts, the route the adjudicator names in §5 (Duminy: semiproper
leaves of an exceptional minimal set have a Cantor set of ends — `r3s-29` §5, read — such leaves have infinitely generated
H₁), and under (0-coh) it is forced in a stronger form (§4).

### 3.5 Verdict on T3

**STANDS-NARROWED.** (a), (b), (α) STAND as written, with proofs supplied. The structural conclusion and (β) STAND for S4′
amended by clause (0) (either form), and are sharpened: under (0-coh) N has no compact leaf and is hyperbolic; B1′ closes
the finitely-many-finite-type-leaves case. (γ) STANDS-NARROWED with the compactness qualification stated verbatim in §3.3.

---

## §4. T4 = the vacuity ruling

### 4.1 Status given T1 and T3

The ruling is "no S4′ object has a non-transverse set that is a finite union of compact leaves, so the KMNT/ALKL
length-group kill does not bear on S4′ and the closed-3-manifold case is OPEN." It is T1 (non-compact archimedean leaf)
plus T3 steps 2–3. Given my verdicts:

- **For S4′ as posed (no clause (0)):** not derivable. A compact S² archimedean leaf with a source–sink flow (§1.1) is
  compatible with (i)–(iv); if all preserved leaves are compact and finitely many, B1 applies and kills the object on a
  closed 3-manifold. So without clause (0) the ruling's first sentence is false as a universal statement, and B1 does
  bear on the subclass it was written for.
- **For S4′ + clause (0) (either form):** the first sentence STANDS (T1 non-compactness + T3). B1 as printed (hypothesis:
  finite union of compact leaves) indeed does not bear.
- **"The closed-3-manifold case is OPEN" is overstated in both cases**, because B1's mechanism is not exhausted by its
  printed hypothesis (B1′, §3.4), and because under (0-coh) Theorem F-1 pins N further.

### 4.2 What the binding manifold statement should be

**Case A — S4′ + clause (0), the case the program will actually work in.** *Let (M, F, φ) be a closed 3-manifold with a C¹
codimension-one foliation by Riemann surfaces and a C¹ foliated flow satisfying S4′ (i)–(iv) and clause (0) (in the form
(0-fix) + (0-coh)). Then: (1) the non-transverse set N is a compact saturated set containing no compact leaf; every leaf
of N is preserved and hyperbolic, and N carries no holonomy-invariant transverse measure (Theorem F-1); (2) N contains a
minimal set K which is neither a compact leaf nor M (the γ_p are off N), i.e. an exceptional minimal set in Hurder's sense
(`r3s-29` §5, read: "a minimal set K is exceptional if K is not a compact leaf, and not an open set"); (3) rank_Z H₁(M ∖
N; Z) = ∞ (B1′); in particular N is not a finite union of finite-type leaves; (4) the printed obstructions — [Den05] p. 24
Rem. 2–3 (everywhere transverse), KMNT Def. 1.5 / ALKL transverse simplicity (finitely many compact preserved leaves), and
B1 — all have hypotheses that S4′ + clause (0) objects violate, and none of them decides this class. The class is OPEN in
print; the decisive instruments are Duminy's theorem and Hurder's Problem 5.4 for the leaves of K, and Sacksteder-type
results for measure-free exceptional minimal sets, all for C² foliations.*

**Case B — S4′ as posed.** *If N is a finite union of compact leaves (KMNT/ALKL class), or more generally a finite union
of finite-type leaves, the object does not exist (B1, B1′). If N contains a non-compact leaf of infinite type or infinitely
many leaves, the case is OPEN in print. Which of these an S4′ object without clause (0) falls into is not determined by
(i)–(iv).*

### 4.3 Verdict on T4

**STANDS-NARROWED**, to Case A above. The enacted S16-3 sentence "[ADJ-A-IV] no S4′ object has a non-transverse set of that
form, so the result does not bear on S4′. The closed-3-manifold case for S4′ is OPEN" should read: "For S4′ objects
carrying clause (0), the non-transverse set is never a finite union of compact leaves — nor of finite-type leaves (B1′) —
so N1 does not bear; the closed-3-manifold case is OPEN only in the class where M ∖ N has infinitely generated H₁, N
contains an exceptional minimal set of hyperbolic preserved leaves, and N carries no invariant transverse measure."

---

## §5. T5 = the clause-(iv) restatement

### 5.1 A-I re-derived from [Den05] (20)/(31) and [x-18] Construction 3

*Inputs read.* [Den05] p. 23 Cor. 5.5 hypothesis "conformal as in (20)"; p. 27 (31): g(T_xφ^t(v), T_xφ^t(w)) = e^t g(v, w)
for v, w ∈ T_xF, i.e. (20) with α = 1; [x-18] p. 3 Construction 3: "ω_φ|TF = 0 and ⟨ω_φ, Y_φ⟩ = 1. One checks that dω_φ = 0
and that ω_φ is φ^t-invariant"; its scope is the dictionary triple with the flow transverse to F.

*Derivation.* Let X be compact, g a continuous leafwise metric with (20): leafwise areas scale by e^{αt} under φ^t. Let µ be
a positive holonomy-invariant transverse measure, finite on transversals, with µ(φ^t(B)) = e^{−βt}µ(B) for transverse
Borel sets B (this is the eigen-measure hypothesis; sign convention: β = 1 means the flow contracts the measure by e^{−t},
and the return map at a closed orbit of length ℓ multiplies it by e^{−ℓ}). Put m = vol_g ⊗ µ, 0 < m(X) < ∞ (finitely many
charts, bounded plaque areas, µ ≠ 0). For a Borel set A in a chart, small enough that φ^t(A) sits in a chart,
m(φ^t A) = ∫ area_g(φ^t(A) ∩ P'_{y'}) dµ(y'); substituting y' = φ̄^t(y) (the induced transverse map, a countable-to-one local
homeomorphism, holonomy-equivalent on overlaps) and using dµ(φ̄^t y) = e^{−βt} dµ(y) and area_g(φ^t(A ∩ P_y)) = e^{αt}
area_g(A ∩ P_y), m(φ^t A) = e^{(α−β)t} m(A). Summing over a finite partition and taking A = X: m(X) = e^{(α−β)t}m(X), so
**α = β**. ∎ Special case (Deninger's Remark 2, p. 24): closed 3-manifold, flow everywhere transverse; µ = |ω_φ| is
holonomy-invariant (ω_φ closed, ker ω_φ = TF) and flow-invariant (φ^{t*}ω_φ = ω_φ), so β = 0 and α = 0. General case with
α = 1: β = 1, µ(φ^t B) = e^{−t}µ(B), and the return map along γ_p scales µ by 1/p — exactly Leichtnam 2007 Lemma 6.1
(`r3s-21` p. 14, read: "µ_L(q·T) = (1/q)µ_L is a consequence of Assumption (i) (Jac M_q = 1/q)") and Prop. 2.4] (p. 15,
read: "W(S, F) ⋊ R is a type III_{1/q}-factor"). **A-I STANDS under its printed hypotheses.**

*Where the hypotheses come from.* A-I needs (20) globally, or — see 5.2 — the cohomological (15), plus the eigen-measure
hypothesis. **S4′ as posed supplies neither.** And clause (ii) alone does not exclude a finite flow-invariant measure: with
β = 0, m(X) = m(φ^t X) = ∫_X j_t dm where j_t is the leafwise g-Jacobian of φ^t, so only the m-average of j_t is pinned to
1, and (ii) constrains j_{log p} = p only on the m-null set ∪_p γ_p. So "never flow-invariant with finite mass" is a
statement about S4′ + clause (0), not about S4′.

### 5.2 The cohomological form, which is what the program should carry [F]

Leichtnam 2007 p. 11 (read): "Deninger pointed out to us that the condition (4) (φ^t)^*g = e^t g was probably too strong
for being generalized. That is why in Proposition 2.2] we shall replace it by (φ^t)^*[λ_g] = e^t[λ_g]" — i.e. (0-coh),
already in 2007. Under (0-coh) the modulus follows without global conformality: if φ^t_*µ = c(t)µ for a holonomy-invariant
µ ≠ 0 (automatic when H̄²_F(X) ≅ R, since its dual is the space of invariant transverse measures, so µ is unique up to
scale), then ⟨C_µ, φ^{t*}λ_g⟩ = e^t⟨C_µ, λ_g⟩ by (15) and = ⟨C_{φ^t_*µ}, λ_g⟩ = c(t)⟨C_µ, λ_g⟩, so c(t) = e^t, i.e.
µ(φ^t B) = e^{−t}µ(B). **Same modulus, weaker hypothesis.** Corollary (Theorem F-1(B)): µ is not supported in N, and every
invariant measure supported in N is excluded — so the archimedean lamination is measure-free.

### 5.3 The two halves of the restatement

- **"the holonomy-invariant transverse measure that necessarily exists"** — FALLS (T2). Existence is Leichtnam 5]'s
  axiom; nothing in S4′ + clause (0) produces it, and the adjudicator's route to it (a euclidean preserved leaf) is
  excluded under (0-coh).
- **"is scaled by the flow with modulus exactly e^{−t}"** — STANDS under (0-coh) [or (0-glob)] together with "H̄²_F(X) ≅ R"
  or "µ is a flow eigen-measure". Without the eigen hypothesis the flow may permute extremal invariant measures and no
  modulus is defined; with H̄²_F one-dimensional (Deninger p. 27 and Rem. 7 both assume it; Leichtnam 4]) it is automatic.
- **"its ALKL justification must be deleted"** — half right. ALKL's *theorem* does not apply to S4′ + clause (0)
  objects (§3.3 (α)). But the *reason* for clause (iv) survives: Deninger's trace formula carries χ_Co(F, µ)δ₀ ([Den05]
  (24) p. 23; Rem. 6 p. 33) and Leichtnam 5] needs µ for the L² scalar product on H̄¹_F. Replace the citation, keep the
  rationale.

### 5.4 Verdict on T5 and the exact text I would enact

**STANDS-NARROWED.** Clause (iv) should read:

> **(iv)** there is a positive holonomy-invariant transverse measure µ, finite on transversals, needed for the leafwise
> trace-formula side (the χ_Co(F, µ)δ₀ term and the L² structure on H̄¹_F; Leichtnam 2013 5]). Its existence is an axiom,
> not a consequence of (i)–(iii). Under clause (0) [φ^{t*} = e^t on the one-dimensional H̄²_F], µ is unique up to scale and
> the flow scales it with modulus exactly e^{−t} (return map at γ_p: factor 1/p; Leichtnam 2007 Lemma 6.1, Prop. 2.4); in
> particular µ is never flow-invariant and is never supported in the non-transverse set N. The theorem of Álvarez
> López–Kordyukov–Leichtnam (arXiv:2402.06671) does not apply to such objects (its transverse-simplicity hypothesis forces
> compact preserved leaves); no trace formula in print covers them.

---

## §6. T6 = N10

### 6.1 The two pages, read

[Den05] p. 23–24: Corollary 5.5's hypotheses include "everywhere transversal to F" and "conformal as in (20)"; Remark 2
(p. 24): "Actually the conditions of the corollary force α = 0 i.e. the flow must be isometric with respect to g." So the
printed *theorem* is under everywhere-transversality. ✓ as the adjudicator says.

[x-06] p. 6 (read) sets the scene: "triples (X̄, F, φ) where X̄ is a closed smooth 3-manifold with a 1-codimensional foliation
F by Riemann surfaces … The fixed points of φ should lie in finitely many compact leaves. All other leaves should be
non-compact and the flow should be transversal to them." p. 8: "If dim X̄ = 3 and there are not compact leaves, so that
X̄ = X and the flow is everywhere transverse to the leaves, then the following formula holds … (9) … Formula (9) does not
contain a term corresponding to (1 − e^{−2t})^{−1} in (8) because we assumed that φ^t had no fixed points. If we allow
fixed points, then the distributional trace defined above may no longer exist. … One can show that the conformal factor
e^{αt} for a metric g_F as above necessarily has to be 1, i.e. α = 0 …" The "as above" metric is the one introduced at the
top of p. 8 for the general triple, and the α = 0 sentence is a separate paragraph from the (9) discussion. Its scope is
ambiguous on the page; mathematically it is **true in the whole p. 6 class**, fixed points or not:

### 6.2 α = 0 is forced by any compact preserved leaf [F]

Under global conformality (20): a compact preserved leaf T has area_g(T) = area_g(φ^t T) = e^{αt} area_g(T), so α = 0.
Under the cohomological α (15): δ_T is a holonomy-invariant transverse measure supported in N, hence flow-invariant
(Theorem F-1(A)), and the pairing gives e^{αt} = 1. Either way the **entire KMNT/ALKL class (finitely many compact preserved
leaves, fixed points inside them) has α = 0** — consistent with ALKL Theorem 1.3.10's ±1 coefficients (memoir p. 8, read).
So "with preserved leaves the manifold question is open" is wrong for compact preserved leaves; it is open only when no
preserved leaf is compact, which by §3.3 and Theorem F-1 is the S4′ + clause (0) situation anyway.

### 6.3 Verdict on T6

**STANDS-NARROWED.** Corrected statement: *Print's theorem ([Den05] Rem. 2) forces α = 0 under "everywhere transversal";
in addition α = 0 is forced, trivially, by any compact preserved leaf. [x-06] p. 8's sentence is therefore correct in its
own p. 6 setting. The closed-3-manifold question for α = 1 is open exactly for foliated flows none of whose preserved
leaves is compact — the class every S4′ + clause (0) object lies in.*

---

## §7. BINDING FRONTIER STATEMENT (ready to paste)

FRONTIER (Session 16, after the adversarial pass; verifier F). S4′ is Leichtnam's printed axiom list (2008 §5.1; 2013 §4.1),
unrealized in every class except Deninger's rank-1 elliptic-curve solenoid, and it must be amended by a clause (0) that the
explicit formula requires and the four clauses omit: a fixed point per archimedean place in clause (iii)'s leaf with
e^{−t/2}T_{x_∞}φ^t|TF ∈ SO(2) (Leichtnam (13)), and φ^{t*} = e^t on the one-dimensional H̄²_F (Deninger p. 27 = Leichtnam
(15)); Deninger's global conformality (31) must NOT be added, since with a fixed point on a compact lamination it is
inconsistent (Schwarz–Pick + Candel). For S4′ + clause (0) the archimedean lamination N — the closure of the χ ≠ 0 leaf,
always strictly larger than that leaf — contains no compact leaf, carries no holonomy-invariant transverse measure, and
consists entirely of hyperbolic preserved leaves; clause (iv)'s measure lives off N and is scaled with modulus e^{−t}; the
adjudication's "leaf conformal to C, χ = +1" is struck. On a closed 3-manifold the printed length-group kill (KMNT/ALKL
class) does not bear, but its mechanism extends to every N that is a finite union of finite-type leaves, so the manifold
case is open only where rank H₁(M ∖ N) = ∞ and N contains an exceptional minimal set of hyperbolic leaves; Duminy's theorem
and Hurder's Problem 5.4 remain the instruments. Nothing in print constructs or kills the resulting class; no construction
attempt is licensed until Q-S4⁗ is re-posed for a *hyperbolic, measure-free* archimedean lamination.

---

## §8. HONESTY

**Read by me this session, at the page cited (pdftotext -layout of the files named).** `x-20` [Den05]: pp. 23–24 (Cor. 5.5,
Remarks 1–3), 25–27 (formula (28), dictionary, desideratum, Fact 6.1, the α = 1 definition and (31)), 28–31 (foliated
spaces 7.1–7.3, working hypothesis 7.5, Remarks 7.6(0)–(4)), 32–34 (the fixed-point determinant, Remark 5, the Fact,
Remarks 6–7, the unramified sentence — Remark 7 runs onto p. 34). `x-18`: pp. 1–5 (Dictionary 1, Construction 3, the
fibration/rank sentences, the product formula, Dictionary 4, §3's standing "no fixed points"). `x-06`: pp. 6–11. `r3s-20`
(Leichtnam 2013): pp. 13–17 (§4 intro, (12), Assumptions 1]–8], Comments 6–7, Lemma 1, Prop. 2–3) and a full-text search
for "compact" in §4. Leichtnam 2008 author copy: §5.1–5.3 (Assumptions 1]–7], Comments 8–10, Lemma 7, Prop. 2) and a
full-text search for "compact". `r3s-21` (Leichtnam 2007): pp. 2–3, 11, 13–15 (Definition 1, the "too strong" remark,
Lemma 6, Prop. 2). `r3s-17` (ALKL memoir): Abstract, §1.1–1.3 (pp. 1–3), §4.1.2 and Remark 4.1.1 (pp. 99–101), the opening
of §5.1 (p. 117). `r3s-30`: pp. 1–4 (definitions of simple, transversely simple, Theorem 1.1). `r3s-29` (Hurder): §5
lines on exceptional minimal sets, Problems 5.1–5.5, Duminy's theorem as quoted there. Candel 1993 (NUMDAM scan already in
the session scratchpad as `candel.txt`): pp. 489–493 (abstract, both introduction theorems, §1.1–1.2 definitions, the
metric definition), pp. 497–498 (Theorem 4.1, Corollary 4.2, §4.1, Theorem 4.3 and the four non-hyperbolic cases). KMNT
(`kmnt.txt`): Lemma 1.10 with proof, Definition 1.11. Program files: `adjudication.md` in full; `scout-O.md` D-II, D-III;
`scout-F.md` §0, R1 and the tables; ledger §15–§16 and the enactment note.

**Recalled, not read, and where it bears.** The Poincaré–Hopf theorem and the Poincaré–Bendixson theorem on S² (used in
§1.3–1.4, as the adjudicator used them; standard); the uniformization theorem and the automorphism groups of Ĉ, C, C^*
and tori (used in Theorem F-1(D); standard); the Schwarz–Pick lemma (F-1(D)); the fact that Ruelle–Sullivan currents of
holonomy-invariant transverse measures are closed, continuous, and exhaust the continuous dual of the reduced H̄²_F
(used in F-1(B) and §5.2; Candel p. 490 states the isomorphism in one direction, and Deninger p. 33 uses the
one-dimensionality of H̄²_F to conclude all ν are proportional — I rely on the standard duality); the Baire category
theorem; the Mayer–Vietoris sequence and the existence of product tubular neighborhoods for two-sided properly embedded
C¹ surfaces (B1′); the trichotomy for minimal sets of codimension-one foliations of closed manifolds (compact leaf / whole
manifold / exceptional), used only to name the minimal set in §4.2 with Hurder's definition read; Minkowski's bound
|d_K| > 1 for K ≠ Q (§1.5 point 3, which needs only that ramified fields exist, which Deninger states); unique
factorization. **None of the six verdicts changes if any of these is replaced by its textbook statement; each is used in
its textbook form.**

**Not read, not relied on.** Cantwell–Conlon's Duminy paper; Ghys 1995/1999; KMNT beyond Lemma 1.10/Def. 1.11 (Def. 1.5 is
taken from the adjudicator's verbatim quotation, marked as such, and bears only on the wording of B1's hypothesis, which
B1′ supersedes); Leichtnam 2005; the published ALKL LNM volume.

**My own derivations, all single-check, all flagged [F] in place:** the S² source–sink counter-configuration (§1.1); the
sink-versus-source analysis of ε_x (§1.1); Theorem F-1 (A)–(D) (§1.5), which is the load-bearing new result of this pass;
the lamination proofs of "closed ⇒ compact" and of the closedness/saturation of N (§3.1–3.2); B1′ (§3.4); the reading
of [x-06] p. 8's scope (§6); the cohomological form of A-I (§5.2); the clause texts in §1.1, §5.4 and §7. **Defects found in
the target file, beyond the verdicts:** (1) S16-4 drops A-II's own hypothesis "(ii∞)" when it says "in any S4′ object";
(2) A-II(c) is stated for K = Q in the proof and "uniform in the number field" in the conclusion; (3) A-III is circular
with Remark 7 (which presupposes the measure); (4) A-IV(γ) treats an inference (compactness from 6]) as if printed;
(5) the α = 1 clause is used throughout (A-I, A-II(c), A-III, table rows A1–A3) without being part of the S4′ statement
the adjudication claims to be about — the orchestrator's framing of this pass already noted the omission, and it is
where every single-check derivation either narrows or falls.
