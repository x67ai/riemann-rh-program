# VERIFICATION OF REFUTER F'S Y₀-WITNESS — verifier F — Session 14 (2026-09-03)

**Program:** RH research program, direction C3-r, milestone M2c, Route 2 residue (R-ii) of `results/c3-r/m2c-feasibility-ledger.md` §14. **Role:** verifier F of two (standing orders 5 and 7; the other verifier runs on a different model and nothing here assumes anything about it). **Model:** Claude Fable 5.1 (same model as refuter F — recorded per standing order 7). **Object under verification:** the construction of `results/c3-r/s14/adversarial/face-b-refuter-F.md` §3.1–3.4 (a compact metrizable 3-dimensional flow space Y with exactly one closed orbit of period log p per prime and a continuous flow-equivariant map f : Y → Y₀ = X̌₀(S¹) ×_{ℚ>0} ℝ>0 with f(C_p) ⊂ Γ_p), checked by the adjudicator in `adjudication.md` §4.1 and enacted as residue (R-ii) in the ledger §14.

**Inputs read in full this session:** `face-b-refuter-F.md` (all); `adjudication.md` §§3, 4, 4.1, 5; `face-b-refuter-O.md` §3; ledger §§2, 3, 8, 14; `s2-feasibility-note.md` §3.1–3.2; `directions/C3-geometric-substrate.md` (Session-14 state paragraph). **Source pages read verbatim this session** (fresh `pdftotext -layout`, one file per page, footers checked; printed page = PDF page): [x-03] = `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` pp. 22–25, 27, 31–34, 37–40, 42–43, 47, 49–50, 59, 63–64; [x-06] = `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf` pp. 11–12; [ALKL] = `fetched-r3/r3s-17-alvarez-lopez-kordyukov-leichtnam-trace-formula-foliated-flows-arxiv-2402.06671v1-SESSION8-FETCH.pdf` abstract and §1.1–1.3.1 (pp. 1–3). Nothing below about a source is from memory. U.S. English.

---

## 0. VERDICT (stated first)

**CONSTRUCTION-VERIFIED.** Every property refuter F claims for (Y, φ, f) is true and is proved below in full: Y is compact, metrizable, of covering dimension 3; the flow is a jointly continuous ℝ-action; its closed orbits are exactly the cores C_p, one of minimal period log p for each prime p and nothing else (§2.5); f is well defined, continuous in the quotient topology of Y₀, flow-equivariant, and sends C_p bijectively onto a genuine periodic orbit γ̃_p of Deninger's packet Γ_p, through a character in E_f (§3). Three things refuter F left unspecified are specified here, and each specification is necessary: the tube vector field must be Lipschitz at the core (a bare "h(0) = 0, h > 0" allows non-unique backward solutions leaving the core — §2.2); the solid tori need an explicit 3-dimensional embedding in the 4-dimensional T² × ℝ² (§2.1); and the tube radii need explicit bounds for pairwise disjointness (§2.1). None of these is an error in refuter F's text; they are the choices a construction must make, and every choice works. One record correction: **Y is not a lamination**, and refuter F never said it was ("Y is not a lamination in the local-product sense", face-b-refuter-F §3.5(i)); the ledger §14 sentence "refuter F strengthens the source to a compact metrizable 3-dimensional lamination (torus + cabled solid tori)" and this task's brief both mislabel it. §2.6 proves the stronger statement that **no foliated-space structure with 2-dimensional leaves exists on Y at all** (for any choice of foliation on the pieces), and no 3-dimensional solenoid structure either.

**NOT S4-SHAPED.** Of the S4 clauses (ledger §8, S4 row, read this session) Y meets exactly the bookkeeping ones — compact; one closed orbit of period log p per prime and no others; a continuous equivariant map into a Deninger space reaching every packet — and fails every structural one: it is not a foliated space / Riemann-surface lamination (§2.6, proved); "simple closed orbit with ε ≡ +1" is meaningful only relative to a leaf tangent space, and the disc foliation of the pieces that makes it true (§2.7) does not extend across the torus; there is no fixed-point set and no preserved leaf with a transverse rate κ_L (the torus core carries a minimal irrational flow; the absorbing orbit Ω of the target has stabilizer ℚ>0, not ℝ); there is no transverse measure and no leafwise cohomology on Y, hence no leafwise trace formula and no T1 orbital side to compare. Worse for the lead: §4.3 proves that **the map f carries no structure**. For any compact Y with a continuous ℝ-action, a continuous equivariant map into the E-free unitary Y₀ meeting infinitely many packets forces Y = Y_η ⊔ ⨆_p Y_p with each Y_p clopen and Y_η = f⁻¹(generic locus) a nonempty closed set on which f lands in the (Tors)-violating unitary generic characters; and conversely any such decomposition with the trivial period bookkeeping (orbits of Y_p have period in (log p)ℤ ∪ {∞}; orbits of Y_η have period in log ℚ>0 ∪ {∞}) admits such a map — continuity is automatic (§4.3, Theorem C). The target certifies nothing about the source that is not already read off the source's clopen decomposition and orbit periods. "The first positive S4-shaped object in the program's record" (ledger §14) should read: the E-free Y₀ admits a universal, structurally inert comparison map from every prime-indexed clopen-decomposed compact flow; refuter F's Y is one such, chosen so that the core has no closed orbits. The lead (Q-b″: "whether that source lamination carries a trace formula with the T1 orbital side, and what Ω's contribution is") is answered: the source is not a lamination, no leafwise trace formula is defined on it, and Ω is not a trace-formula term of anything.

**Whether any variant survives (§5.4):** a genuinely foliated variant would need, per prime, a compact foliated piece with a foliated flow having a single simple transverse closed orbit of period log p and no other closed orbits, the pieces accumulating in local-product fashion onto a compact foliated core with no closed orbits. §5.4 records a Lefschetz obstruction in the sub-case where the piece is a mapping torus of a closed surface (impossible for every closed surface); the general sub-case is open and is not decided here. Even if such a variant existed, Theorem C shows that mapping it into the E-free Y₀ would add nothing: the honest continuation of Route 2 is a trace formula on a source built without reference to Y₀, i.e. the S2/S4 problem exactly as the ledger already states it, with the E-free target deleted from the specification because it is inert.

---

## 1. The objects, written out from the source with pages

**1.1 Points and Frobenius ([x-03] p. 22).** X̊(ℂ) = pairs (x, P^×), x ∈ X = Spec ℤ̄, P^× : κ(x)^× → ℂ^× a homomorphism; G = Aut(ℚ̄/ℚ) acts by (x,P^×)σ = (x^σ, P^×∘σ); F_ν(x,P^×) = (x, P^×∘( )^ν) commutes with G; X̊₀(ℂ) = X̊(ℂ)/G. Remark 3.4 (p. 23): affine case, points are multiplicative P : ℤ̄ → ℂ with P(0) = 0, P(1) = 1, P⁻¹(0) prime. Over Spec ℤ, x is the generic point η (κ = ℚ̄) or a closed point over a prime p (κ = 𝔽̄_p; "κ(x) is an algebraic closure of κ(x₀)", p. 22).

**1.2 Colimit (pp. 24–25).** X̌(ℂ) = colim_ℕ X̊(ℂ); points F_ν⁻¹P; "F_ν⁻¹P = F_{ν′}⁻¹P′ is equivalent to F_{ν′}P = F_νP′, an equality in X̊(ℂ)" (p. 25); pr_X(F_ν⁻¹P) = pr_X(P); ℚ>0 acts; X̌₀(ℂ) = X̌(ℂ)/G; π̌ is ℚ>0-equivariant.

**1.3 (Tors), admissibility (p. 27, verbatim).** "(Tors) the group ker(χ)_tors = ker(χ|_{μ(κ)}) is finite and |(ker χ)_tors| ∈ N₀." Def. 4.1: E admissible iff χ ∈ E ⟺ χ∘σ ∈ E ⟺ χ^ν ∈ E, and "the characters in E should satisfy (Tors)."

**1.4 Packets (pp. 31–34).** For x₀ = (p): "The fibres of pr_{X₀} : X̌₀(ℂ)_{E_tors} → X₀ are ℚ>0₀-invariant"; C_{x₀} = pr₀⁻¹(x₀)ℚ>0₀ = ⋃_ν F_ν⁻¹pr₀⁻¹(x₀) (p. 31). "Given x and composing the fixed injection ι : μ(K) ↪ μ(C) … with (32) we obtain the injective character χ_x = ι∘i_x⁻¹ : κ(x)^× ↪ C^×" (p. 32). (35): every P : κ(x)^× → ℂ^× with finite cyclic kernel is χ_x∘( )^a∘( )^ν, (a,ν) ∈ Ẑ^×_{(p)} × ℕ; "Any point y in X over x₀ is conjugate to our chosen point x by an element of G" (p. 32). (38) and "It follows that all points P₀ ∈ C_{x₀} have isotropy subgroup (ℚ>0₀)_{P₀} = N x₀^ℤ" (pp. 32–33). (41)–(43): ρ(x,P^×) = |(ker P^×)_tors|, ρ(F_νP) = ν_x ρ(P). Thm. 5.2 (p. 34): for admissible E ⊂ E_max, the points with nontrivial isotropy are ∐ C^E_{x₀}, isotropy N x₀^ℤ; "If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}." Remark after Thm. 5.2 / p. 37: "(Tors) does force the points P₀ ∈ X̌₀(C)_E over characteristic zero points of X₀ to have trivial stabilizer."

**1.5 The suspension (p. 38–39).** X₀ = X̌₀(ℂ)_E ×_{ℚ>0₀} ℝ>0, "the quotient of X̌₀(C)_E × ℝ>0 by the right ℚ>0₀-action given by (P₀,u)q = (P₀q, q⁻¹u) = (F_q(P₀), q⁻¹u)"; φ^t([P₀,u]) = [P₀, ue^t]; Γ_{x₀} = C_{x₀} ×_{ℚ>0₀} ℝ>0, "all ℝ>0-orbits in Γ_{x₀} are circles ℝ>0/N x₀^ℤ". Thm. 6.1 (p. 39): points with nontrivial ℝ>0-isotropy = ∐ Γ^E_{x₀}, isotropy N x₀^ℤ. p. 39: "In the following observation we omit E from the notation." p. 40, the question: "Is there a sub-dynamical system Y₀ ⊂ X₀ = X̌₀(C) ×_{ℚ>0} ℝ>0 or at least one which maps to X₀ such that dim Y₀ = 2d + 1 where d = dim X₀ and such that Y₀ contains at least one periodic orbit in Γ_{x₀} for every closed point x₀ of X₀? If d = 1, is there such a Y₀ which is a Riemann surface lamination in the sense of [Ghy99]?" — no word "compact".

**1.6 Topology (pp. 40, 42–43, 47).** X̊(ℂ): pointwise convergence on ℤ̄, Tychonov subspace, metrizable (p. 40). Lemma 7.3 (p. 42): F_ν continuous, closed, open, injective; (51) F_ν(X̊(ℂ)) = {P : P(μ_ν(K)) = 1}. X̌(ℂ): inductive-limit topology, "Z ⊂ X̌(C) is closed, resp. open if and only if F_ν(Z) ∩ X̊(C) is closed, resp. open in X̊(C) for all ν" (p. 43). Prop. 7.4: X̊(ℂ) clopen in X̌(ℂ); F_q homeomorphisms; G by homeomorphisms. "We give X̌₀(C) = X̌(C)/G the quotient topology … π and π̌ … are continuous and since G acts by homeomorphisms, also open. Moreover the projections pr_X : X̌(C) → X and pr_{X₀} : X̌₀(C) → X₀ are continuous." (p. 43). E-loci: subspace topologies; the inductive-limit topologies agree with them "because the subspaces F_ν⁻¹X̊(C) and F_ν⁻¹X̊₀(C) are open" (p. 47).

**1.7 The quotient topology on the suspension (p. 59, verbatim).** "Let E be an admissible class as in Definition 4.1. We give X = X̌(C)_E ×_{ℚ>0₀} ℝ>0 and X₀ = X̌₀(C)_E ×_{ℚ>0₀} ℝ>0 the quotient topologies." (Printed for admissible E; the E-free suspension below receives the same recipe, as [x-06] p. 11 "X₀ = (X̌₀(C) × ℝ>0)/ℚ>0" and [x-03] §10 p. 63 "π : X̃ = M × ℝ>0 → X = M ×_Q ℝ>0" do.)

**1.8 The unitary closure (pp. 49–50; [x-06] pp. 11–12).** p. 49: "replace X₀ by the dynamical system Y₀ obtained as the topological closure of the union of all periodic orbits coming from closed points of X₀ … Y₀ = X̌₀(S¹) ×_{ℚ>0} ℝ>0. Here X̌₀(S¹) = X̌(S¹)/G where X̌(S¹) = colim_ℕ X̊(S¹) and X̊(S¹) is the subspace of X̊(C) consisting of points (x,P^×) with P^× : κ(x)^× → S¹ a unitary character." Thm. 8.2 (p. 50): X̌(ℂ)_per = X̌(S¹), X̌₀(ℂ)_per = X̌₀(S¹), where X̊(ℂ)_per = {(x,P^×) : κ(x) ≅ 𝔽̄_p, ker P^× finite}; "Since X̊(S¹) is closed in X̊(C) the subspace X̌(S¹) is closed in X̌(C)". [x-06] p. 11: "What we know for certain is that the restrictions of P^× to μ(κ(x)) must have finite kernels (condition E_tors)"; "In general, the dynamical system (X₀, φ^t) has too many periodic orbits". [x-06] p. 12: "The closure is the subsystem obtained by replacing X̊(C)_E in the previous constructions with the subspace of pairs (x,P^×) with P^× : κ(x)^× → S¹ a unitary character."

**Reading flagged (J1).** [x-03] p. 39 declares "we omit E from the notation" before p. 40's question and before §8; so the printed Y₀ of p. 49 is ambiguous between the E-free X̌₀(S¹) (the adjudication's and both refuters' reading, supported by the E-free wording of X̊(S¹) and by [x-06] p. 12) and X̌₀(S¹)_E (the closure taken inside X₀^E). I follow the record's E-free reading for the verification — the construction is only about that reading — and note that under the p. 39 convention it is not the only reading. This does not affect any verdict below: §4.3 shows the E-free target is inert either way.

**1.9 The foliated-space definition the program uses** (`s2-feasibility-note.md` §3.1, quoting [Den05] §7.1 after [MS88] Ch. II, read this session): "a foliated space with d-dimensional leaves is a separable metrizable space X with charts φᵢ : Uᵢ → Fᵢ × Tᵢ, Fᵢ ⊂ ℝ^d open, such that (a) transitions have the form φⱼ∘φᵢ⁻¹(x,y) = (f_{ij}(x,y), g_{ij}(y)), and (b) all partial derivatives D_x^α f_{ij}(x,y) exist and are continuous as functions of x and y. A (generalized) solenoid of dimension a is such an X locally homeomorphic to Lᵢ × Tᵢ with Tᵢ totally disconnected … A codimension-one foliation F inside an a-dimensional solenoid (X, L): a second foliated-space structure with leaves of dimension d = a − 1 … A flow: a continuous ℝ-action, smooth on L-leaves, F-compatible if each φᵗ maps F-leaves to F-leaves." [ALKL] p. 2 (read): "A flow φ = {φ^t} on M is said to be foliated if it maps leaves to leaves"; p. 3: "The condition on c to be simple means that id − φ_*^{kℓ(c)} : T_pF → T_pF is an isomorphism for any p ∈ c and k ∈ ℤ^×, whose determinant is independent of p, and its sign denoted by ε_c(k)."

---

## 2. The source (Y, φ): the construction written out, and every property proved

### 2.1 The pieces (explicit choices supplied)

Fix v = (1, β) ∈ ℝ² with β irrational. For each prime p let n_p ∈ ℤ² be an integer vector nearest to (log p)·v and v_p := n_p / log p, so |v_p − v| ≤ 1/(√2 · log p) → 0. Fix a base point θ_p ∈ T² = ℝ²/ℤ² and a unit vector w_p ⊥ v_p. Choose tube radii ε_p with

  0 < ε_p ≤ min{ 1/(4p(p+1)), 1/(4p |n_p|) }.   (2.1)

Define the embedding of the closed solid torus V := (ℝ/(log p)ℤ) × D̄² (coordinates θ ∈ ℝ/(log p)ℤ, (r,ψ) polar on the unit disc) into T² × ℝ² by

  ι_p(θ, r, ψ) := ( θ_p + θ v_p + ε_p r cos ψ · w_p ,  (1/p + ε_p r sin ψ) · e^{2πiθ/log p} ),   (2.2)

and put N_p := ι_p(V), C_p := ι_p({r = 0}) = {(θ_p + θv_p, (1/p)e^{2πiθ/log p})}. Put

  Y := (T² × {0}) ∪ ⋃_p N_p ⊂ T² × ℝ².

*ι_p is an embedding.* The ℝ²-coordinate determines e^{2πiθ/log p}, i.e. θ mod log p, and determines ε_p r sin ψ (since ε_p < 1/p the modulus 1/p + ε_p r sin ψ > 0 and is injective in r sin ψ). Given θ, the T²-coordinate θ_p + θv_p + s·w_p with |s| ≤ ε_p < 1/2 determines s = ε_p r cos ψ (a segment of length < 1 in a fixed direction embeds in T²). So (r cos ψ, r sin ψ) is determined; ι_p is injective and continuous on a compact set, hence an embedding. N_p is a 3-dimensional closed solid torus (3-manifold with boundary torus ∂N_p = ι_p({r = 1})); it is a genuine 3-dimensional subset of the 4-dimensional T² × ℝ² — refuter F's phrase "thin closed tubular neighborhood" must be read this way, since a tubular neighborhood of a curve in a 4-manifold is 4-dimensional.

*C_p is an embedded circle of "length" log p.* The parametrization θ ↦ ι_p(θ,0,·) is injective on [0, log p) (second coordinate) and log p-periodic (θ_p + (log p)v_p = θ_p + n_p ≡ θ_p). Here "length" means the time-period of the flow below; the geometric length is irrelevant and is ≈ |n_p|.

*Pairwise disjointness.* The ℝ²-modulus on N_p lies in [1/p − ε_p, 1/p + ε_p]. For primes p < q, 1/p − 1/q ≥ 1/(p(p+1)) > ε_p + ε_q by (2.1). So N_p ∩ N_q = ∅, and N_p ∩ (T² × {0}) = ∅.

*Hausdorff convergence N_p → T² × {0} (load-bearing for Theorem B in §2.6, not for the construction's own properties).* Refuter F states C_p → T² × {0} in Hausdorff distance. True, but it needs an argument F omits: if n_p = g_p m_p with m_p primitive, the T²-projection of C_p is the closed geodesic in direction m_p, whose complement is a strip of width 1/|m_p|, so the Hausdorff distance is ≤ 1/(2|m_p|) + 1/p; and |m_p| → ∞ because otherwise, along a subsequence, m_p ∈ a finite set and (log p)v would lie within √2/2 of the line ℝm_p, while dist((log p)v, ℝm_p) = (log p)·dist(v, ℝm_p) → ∞ for v of irrational slope. Hence dist(y, C_p) ≤ 1/(2|m_p|) + 1/p → 0 for every y ∈ T² × {0}. The construction's own properties (§2.2–2.5, §3) use only v_p → v, ε_p → 0, 1/p → 0; Theorem B uses the convergence to find points of N_p near a given point of the torus.

### 2.2 The flow

*On T² × {0}:* ψ^t(θ, 0) = (θ + tv, 0), the linear flow. No closed orbits: ψ^t(θ) = θ iff tv ∈ ℤ², iff t = 0 (t ≠ 0 would give β = tβ/t ∈ ℚ). No fixed points.

*On N_p, in the coordinates of (2.2):* the vector field

  Z_p := ∂_θ + α_p r ∂_ψ − r(1 − r) ∂_r,   α_p := (2π/ log p)·λ with λ irrational.   (2.3)

This is refuter F's "∂_θ + α(r)∂_ψ − h(r)∂_r with α(0) = 0, α(1) irrational multiple of 2π/log p, h(0) = h(1) = 0, h > 0 on (0,1)" with the choices α(r) = α_p r, h(r) = r(1 − r). **The choice matters:** in Cartesian coordinates (x,y) = (r cos ψ, r sin ψ) on the disc, α(r)∂_ψ = α(r)(−y∂_x + x∂_y) and −h(r)∂_r = −(h(r)/r)(x∂_x + y∂_y); with (2.3) these are the smooth fields α_p(−y∂_x + x∂_y) and −(1 − r)(x∂_x + y∂_y), so Z_p is smooth on V, tangent to ∂V (the ∂_r-coefficient vanishes at r = 1), and generates a unique global flow φ_p^t on V by the standard theory. A choice such as h(r) = √r, which F's wording permits, is not Lipschitz at r = 0 and admits solutions that leave the core in backward time (r(t) = ((c − t)/2)² for t < c, r = 0 for t ≥ c), so the "flow" would not be a well-defined ℝ-action and the core would not be an orbit. This is the one specification a construction must make and F's text does not; (2.3) makes it. Transport the flow to N_p by ι_p.

*Closed orbits of φ_p on N_p.* dθ/dt = 1, so any closed orbit has period in (log p)ℤ_{>0}. On the core r = 0: the orbit θ ↦ ι_p(θ,0,·) has minimal period log p (injectivity on [0, log p)). On ∂N_p (r = 1): the field is ∂_θ + α_p∂_ψ on the torus ℝ/(log p)ℤ × ℝ/2πℤ; an orbit closing after time k log p needs k(log p)α_p = 2πkλ ∈ 2πℤ, i.e. kλ ∈ ℤ, impossible for k ≠ 0. In the interior 0 < r < 1: dr/dt = −r(1 − r) < 0, r is strictly decreasing along orbits, so no orbit is closed. **The closed orbits of φ_p are exactly the core C_p, of minimal period log p.** No fixed points (the ∂_θ-coefficient is 1).

*On Y:* φ^t := ψ^t on T² × {0}, φ^t := φ_p^t on N_p. Each piece is invariant, so this is an ℝ-action on the set Y.

### 2.3 Y is compact and metrizable, of covering dimension 3

Y ⊂ T² × ℝ² is bounded. Closed: let y_k ∈ Y converge in T² × ℝ² to y. If infinitely many y_k lie in T² × {0}, y ∈ T² × {0} (closed). If infinitely many lie in a single N_p, y ∈ N_p (closed). Otherwise, passing to a subsequence, y_k ∈ N_{p_k} with p_k → ∞, and the ℝ²-modulus of y_k is ≤ 1/p_k + ε_{p_k} → 0, so y ∈ T² × {0}. Hence Y is closed and bounded in a compact metrizable space, so compact and metrizable. Each N_p is compact and, by the same argument applied to Y ∖ N_p = (T² × {0}) ∪ ⋃_{q ≠ p} N_q, is **clopen in Y**; T² × {0} is closed in Y and not open (every neighborhood of a point of it meets N_p for all large p, since dist(N_p, T² × {0}) ≤ 1/p + ε_p → 0 and the T²-projection of C_p passes within 1/(2|m_p|) → 0 of every point).

Covering dimension: Y is a countable union of the closed subsets T² × {0} (dim 2) and N_p (dim 3), so dim Y ≤ 3 by the countable sum theorem for separable metrizable spaces; N_2 contains a 3-ball, so dim Y = 3. This "3" is the dimension of the pieces; the core is 2-dimensional. It is **not** "dim 3 in the lamination sense" (§2.6).

### 2.4 The flow is jointly continuous on ℝ × Y

At (t, y) with y ∈ N_p: ℝ × N_p is open in ℝ × Y (N_p clopen) and φ_p is the flow of a smooth vector field on a compact manifold with boundary, hence jointly continuous.

At (t, y) with y = (θ, 0): let (t_k, y_k) → (t, y). If y_k ∈ T² × {0} for all large k, continuity of ψ gives the claim. Otherwise, along the remaining terms, y_k ∈ N_{p_k} with p_k → ∞ (a neighborhood of y of ℝ²-modulus < δ meets only those N_p with 1/p − ε_p < δ). Write y_k = ι_{p_k}(θ_k, r_k, ψ_k). By (2.2) and (2.3), φ^{t_k}(y_k) = ι_{p_k}(θ_k + t_k, r_k′, ψ_k′) for some (r_k′, ψ_k′), so

  pr_{T²} φ^{t_k}(y_k) − pr_{T²}(y_k) = t_k v_{p_k} + (s_k′ − s_k) w_{p_k},  |s_k|, |s_k′| ≤ ε_{p_k},

which → tv since v_{p_k} → v, t_k → t, ε_{p_k} → 0; and pr_{T²}(y_k) → θ; so pr_{T²} φ^{t_k}(y_k) → θ + tv. The ℝ²-coordinate of φ^{t_k}(y_k) has modulus ≤ 1/p_k + ε_{p_k} → 0. Hence φ^{t_k}(y_k) → (θ + tv, 0) = φ^t(y). ∎

This is exactly the role of the "cabling": the θ-advance of the tube flow is carried to a T²-displacement t·v_p by (2.2), so the tube flows converge to the linear flow and the limit is not stationary. (Adjudication §4.1 makes the same point; I confirm it at the level of formulas.)

### 2.5 Theorem A (closed-orbit inventory). The closed orbits of (Y, φ) are exactly the cores C_p, p prime, C_p of minimal period log p; there are no other closed orbits and no fixed points.

Proof. Y is the disjoint union of the invariant sets T² × {0} and N_p; a closed orbit lies in one of them; §2.2 lists the closed orbits of each: none in T² × {0}, exactly C_p in N_p. Minimal periods log p are pairwise distinct, so "exactly one closed orbit of length log p per prime, and nothing else" holds in the strongest sense. ∎

### 2.6 Theorem B (Y is not a foliated space). There is no foliated-space structure with 2-dimensional leaves on Y in the sense of §1.9 (for any choice of foliation on the pieces, smooth or merely topological — only the local product form of the charts is used); and there is no 3-dimensional solenoid structure (locally ℝ³ × totally disconnected) on Y either.

Proof. Suppose h : F × T → U ⊂ Y is a chart (a homeomorphism onto an open set) with F ⊂ ℝ² an open disc and U ∋ y₀ := (θ₀, 0) ∈ T² × {0}; shrink F to a closed disc F̄ ⊂ F. Plaques h(F × {t}) are connected; each N_p is clopen in Y; so each plaque lies in T² × {0} or in a single N_p. Choose y_k ∈ N_{p_k} ∩ U with y_k → y₀ (possible, §2.3) and write h⁻¹(y_k) = (f_k, t_k); continuity of h⁻¹ gives t_k → t₀ where h(F × {t₀}) ∋ y₀, so h(F × {t₀}) ⊂ T² × {0} and h(F × {t_k}) ⊂ N_{p_k}. Joint continuity of h on the compact F̄ × {t₀, t_k : k} gives uniform convergence h(·, t_k) → h(·, t₀) on F̄.

Let γ ⊂ F̄ be a round circle about the center of F̄, small enough that J := h(γ, t₀) — a Jordan curve in the torus leaf T² × {0} — has diameter < 1/8, so that J and everything within 1/8 of it lift isometrically to a Euclidean disc B ⊂ ℝ² of radius 1/4 about a lift of h(center, t₀) =: (x₀, 0). J bounds a Jordan domain R ⊂ B containing a Euclidean disc of radius 3δ > 0. Then J is not contained in the δ-neighborhood N_δ(S) of any straight segment S ⊂ B: N_δ(S) is convex of width 2δ, a Jordan domain lies in the convex hull of its boundary curve (a point outside the hull is separated from J by a line, hence lies in the unbounded component), so J ⊂ N_δ(S) would give R ⊂ N_δ(S), contradicting the disc of radius 3δ > δ inside R. Take k with p_k large enough that sup_{F̄}|h(·,t_k) − h(·,t₀)| < δ/4 and ε_{p_k} < δ/4, and set J_k := h(γ, t_k) ⊂ N_{p_k}, a connected set within δ/4 of J. Its T²-projection pr(J_k) is connected, lies within δ/4 of J (pr is 1-Lipschitz and J ⊂ T² × {0}), hence inside the lifted disc B, and lies in pr(N_{p_k}), the strip of half-width ε_{p_k} around the closed geodesic pr(C_{p_k}). By (2.1), 2ε_{p_k} < 1/(2|n_{p_k}|) ≤ 1/(2|m_{p_k}|), i.e. less than half the spacing 1/|m_{p_k}| between consecutive parallel passes of the geodesic, so the strip's passes through B are pairwise disjoint straight bands and pr(J_k), being connected, lies in a single band, hence within ε_{p_k} < δ/4 of a straight segment S ⊂ B. Then J lies within δ/4 + δ/4 = δ/2 < δ of S — contradiction. Hence no chart exists at y₀.

For the solenoid statement: a chart U ≅ L × T with L ⊂ ℝ³ open around y₀ has connected plaques L × {t}; the plaque through y₀ lies in T² × {0} (clopen argument), so ℝ³ would embed in T², contradicting invariance of domain. ∎

Remarks. (i) The argument uses only that the tubes are thin relative to the spacing of the geodesic passes; (2.1) guarantees this, and refuter F's "tube radius ≪ 1/p" implies it for large p because 1/p ≪ 1/log p ≈ 1/|n_p|. A variant with fat, flat tubes (T²-half-width ≥ 1/|n_p|) is possible only for finitely many p, because pairwise disjointness of the tubes in the ℝ²-direction forces the sum of the ℝ²-thicknesses to converge while Σ_p 1/|n_p| ≍ Σ_p 1/log p diverges; and for the fat tubes themselves any codimension-one foliation of a solid torus (Reeb-type, by Novikov, or transverse to the boundary) has plaques that are vertical or small somewhere inside the tube, which the same uniform-convergence argument rules out at the accumulation. I record this variant analysis as a sketch [novelty: single-check], not as part of Theorem B, whose statement is about Y as specified. (ii) The ledger §14's "lamination" and the brief's "source lamination" are therefore wrong words for Y; refuter F's own §3.5(i) is right.

### 2.7 What structure the pieces do have (the local ALKL model at C_p)

On each N_p put F_p := the disc foliation {θ = const} of V. It is a smooth codimension-one foliation of the manifold with boundary N_p, transverse to ∂N_p, with leaves closed 2-discs (leaves with boundary — not admitted in §1.9's definition, which wants Fᵢ ⊂ ℝ² open, but the interior is a foliated space). The flow (2.3) has dθ/dt = 1, so φ_p^t maps {θ = c} to {θ = c + t}: it is a foliated flow transverse to F_p, with no preserved leaves. At the core, the linearization of the disc return map after time k log p is, in Cartesian coordinates, exp(k log p · (−I + α_p J)) = p^{−k}·R(2πkλ) (J the rotation generator): eigenvalues of modulus p^{−k} ≠ 1 for k ≠ 0, so id − φ_*^{k log p} : T_pF_p → T_pF_p is an isomorphism for every k ∈ ℤ^× — **C_p is a simple closed orbit in [ALKL]'s sense** (p. 3, quoted in §1.9) — and det(id − p^{−k}R(2πkλ)) = |1 − p^{−k}e^{2πikλ}|² > 0, so **ε_{C_p}(k) = +1 for all k**. The transverse measure dθ on the leaf space ℝ/(log p)ℤ is flow-invariant. The leaves are discs, trivially Riemann surfaces, and the flow is leafwise conformal (a similarity with rate 1 in (2.3); any rate is available by rescaling h). So each piece separately is the local [ALKL]/[Den05] model of a simple closed orbit with ε ≡ +1 — with boundary, and with nothing forcing the T2 weight or anything global. This structure does not extend to Y (Theorem B), and the pieces are not closed manifolds (H1).

---

## 3. The target and the map f : Y → Y₀

Throughout, X₀^full := X̌₀(ℂ) ×_{ℚ>0} ℝ>0 (all characters, no E) and Y₀ := X̌₀(S¹) ×_{ℚ>0} ℝ>0 (p. 49, E-free reading), both with the quotient topology Q : X̌₀(·) × ℝ>0 → (·) of the product topology (§1.7). Since X̌(S¹) is closed in X̌(ℂ) (p. 50) and G-invariant, X̌₀(S¹) = π̌(X̌(S¹)) is closed in X̌₀(ℂ) (π̌ open, so π̌(complement) is open) and ℚ>0-invariant; so Q⁻¹(Y₀) = X̌₀(S¹) × ℝ>0 is a saturated closed subset, and the restriction of the quotient map Q to it is a quotient map onto Y₀ with the subspace topology (restriction of a quotient map to a saturated closed set). **So Y₀'s quotient topology and its subspace topology from X₀^full coincide** — refuter F's §3 "Quotient topologies as in §1.6" is unambiguous.

### 3.1 The points (refuter F §3.1, re-derived)

(a) *P_p.* For each prime p fix x_p over (p) and χ_p := χ_{x_p} = ι∘i_{x_p}⁻¹ : 𝔽̄_p^× ↪ μ(ℂ) ⊂ S¹, the injective character of p. 32. Let L_p := prime-to-p part of lcm(1, …, p^p), ν_p := L_p², P_p := F_{ν_p}(x_p, χ_p) = (x_p, χ_p∘( )^{ν_p}). ker(P_p|_{μ(𝔽̄_p)}) = {ζ̄ : ζ̄^{ν_p} = 1} = μ_{ν_p}(𝔽̄_p), of order exactly ν_p because p ∤ ν_p. So P_p satisfies (Tors) with |ker| = ν_p ∈ ℕ, and ker P_p^× is finite, so **P_p ∈ E_f** (finite kernel; [x-06] p. 11 "E can be the conditions that ker P^× is always finite"), an admissible class ⊂ E_max over Spec ℤ, for which Thm. 5.2 (p. 34, "If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}") and Thm. 6.1 apply. P_p is unitary (values roots of unity), so P_p ∈ X̊(S¹). Its class π(P_p) lies in pr₀⁻¹((p)) ⊂ C_{(p)} (p. 31) and has ℚ>0-isotropy exactly p^ℤ (pp. 32–33; the isotropy of a point of an invariant subset is its isotropy in X̌₀(ℂ), since F_qP₀ = P₀ is an equation in X̌₀(ℂ)). Hence

  γ̃_p := {[π(P_p), u] : u ∈ ℝ>0} ⊂ Γ_p := C_{(p)} ×_{ℚ>0} ℝ>0 ⊂ Y₀

is a periodic orbit of the flow with ℝ>0-isotropy exactly p^ℤ, i.e. minimal period log p (Thm. 6.1). Note [π(P_p), u] = [π(F_{ν_p}χ_p), u] = [π(χ_p), ν_p u], so **γ̃_p is the same orbit as the orbit through π(χ_p) used by refuter O and the adjudicator**; the choice of P_p only fixes the base point of the parametrization. Which character: χ_p^{ν_p}, ν_p = L_p², in E_f; the orbit is the "a = 1" orbit of (38).

(b) *P_p → (η, 1).* (η, 1) is the trivial character of ℚ̄^×: P(0) = 0, P(r) = 1 for r ≠ 0, multiplicative, P⁻¹(0) = (0) prime — a point of X̊(ℂ) by Remark 3.4 (p. 23), unitary, so a point of X̊(S¹) as printed on p. 49; ker(P|_μ) = μ(ℚ̄) is infinite, so (Tors) fails and (η,1) lies in no X₀^E. Convergence: for r ∈ ℤ̄ ∖ {0}, r ∈ 𝔭_{x_p} implies N_{ℚ(r)/ℚ}(r) ∈ 𝔭_{x_p} ∩ ℤ = pℤ (the norm is r times a product of conjugates in ℤ̄), a nonzero integer, so this happens for finitely many p; for the other p, r̄ ∈ 𝔽̄_p^× generates 𝔽_{p^{f′}} with f′ ≤ f := [ℚ(r):ℚ] (r is a root of its monic minimal polynomial in ℤ[T], whose reduction r̄ satisfies), so ord(r̄) | p^{f′} − 1, is prime to p and ≤ p^f − 1 < p^p once p ≥ f; hence ord(r̄) | L_p | ν_p and P_p(r) = χ_p(r̄)^{ν_p} = 1. With P_p(0) = 0 this is pointwise convergence P_p → (η,1) in X̊(ℂ) (p. 40 topology). ✓

(c) *Ω.* F_ν(η,1) = (η, 1∘( )^ν) = (η,1), and F_ν⁻¹(η,1) = (η,1) by injectivity of F_ν on X̌(ℂ), so F_q π(η,1) = π(η,1) for all q ∈ ℚ>0. Ω := O_∞ := {[π(η,1), u] : u > 0} ≅ ℝ>0/ℚ>0 as a set.

### 3.2 Lemma A (packet indiscreteness in X₀^full — re-derived independently). Every open U ⊂ X₀^full meeting Γ_p contains Γ_p. In particular each γ̃_p is an indiscrete subspace.

Proof. By (35), (38) and G-transitivity (p. 32), every point of Γ_p is [π(x_p, χ_p∘( )^a), u] with a ∈ Ẑ^×_{(p)}, u > 0 (absorb ν and F_ν⁻¹ into u). Write P_a := (x_p, χ_p∘( )^a). Let U ∋ z₀ := [π(P_a), u₀]; Q⁻¹(U) is open and contains (π(P_a), u₀), hence a box W₀ × (α, β) with W₀ open in X̌₀(ℂ), α < u₀ < β. π̌⁻¹(W₀) ∩ X̊(ℂ) is an open neighborhood of P_a in X̊(ℂ) (π̌ continuous, X̊(ℂ) open in X̌(ℂ) with the pointwise topology, Prop. 7.4a), so it contains a basic set V′ = {P : |P(r_j) − P_a(r_j)| < ε, j = 1..k}, r_j ∈ ℤ̄ ∖ 𝔭_{x_p} (test elements in 𝔭_{x_p} give P(r_j) = 0 for every P over x_p and impose nothing). Let o_j := ord(r̄_j) (prime to p), D := lcm(o_j). Now let z = [π(P_b), u′] be any point of Γ_p, b ∈ Ẑ^×_{(p)}. **The p-adic trick:** for every s ≥ 0, P_b(μ_{p^s}(ℚ̄)) = 1 (ζ^{p^s} = 1 ⟹ (ζ̄ − 1)^{p^s} = 0 ⟹ ζ̄ = 1), so by (51) P_b ∈ F_{p^s}(X̊(ℂ)) and F_{p^s}⁻¹P_b = (x_p, χ_p∘( )^{b p^{−s}}) with ( )^{p^{−s}} the inverse Frobenius of 𝔽̄_p^× (as in the proof of Prop. 5.1, p. 34: "( )^p is an isomorphism on κ(x)^× if char κ(x) = p"). Hence F_{m/p^s}P_b = (x_p, χ_p∘( )^{b m p^{−s}}) ∈ X̊(ℂ) for every m ∈ ℕ, with value χ_p(r̄_j)^{b m p^{−s} mod o_j} at r_j. Choose s so large that p^s u′(1/α − 1/β) > D; the interval (p^s u′/β, p^s u′/α) has length > D and so contains an integer m ≥ 1 with m ≡ a b⁻¹ p^s (mod D) (b is a unit mod D). Then q := m/p^s satisfies q⁻¹u′ ∈ (α, β) and (F_qP_b)(r_j) = χ_p(r̄_j)^{a} = P_a(r_j) exactly for all j, so F_qP_b ∈ V′, π̌(F_qP_b) = F_q π(P_b) ∈ W₀, (F_qπ(P_b), q⁻¹u′) ∈ Q⁻¹(U), and z = Q((π(P_b),u′)·q) ∈ U. ∎

(This is the adjudication's face (a) — "strong approximation with the place p deleted" — re-derived with explicit open sets and extended from X₀^E to X₀^full; the mechanism is identical. It is load-bearing for the continuity of f on the pieces.)

### 3.3 Lemma B (Ω is indiscrete). Every open U ⊂ X₀^full meeting Ω contains Ω.

Proof. Q⁻¹(U) ⊇ W₀ × (α, β) ∋ (π(η,1), u₀). For any u′ > 0 pick q ∈ ℚ>0 with q⁻¹u′ ∈ (α, β) (density); then (F_qπ(η,1), q⁻¹u′) = (π(η,1), q⁻¹u′) ∈ Q⁻¹(U) and [π(η,1), u′] = Q((π(η,1),u′)·q) ∈ U. ∎

### 3.4 Key Lemma (uniform absorption; refuter F §3.2, re-derived). Let U ⊂ X₀^full be open with U ∩ Ω ≠ ∅. Then there is p₀ with γ̃_p ⊂ U for all primes p ≥ p₀.

Proof. By Lemma B, U ∋ [π(η,1), 1]; Q⁻¹(U) ⊇ W₀ × (a, b) ∋ (π(η,1), 1), a < 1 < b. π̌⁻¹(W₀) ∩ X̊(ℂ) ⊇ V := {P : |P(r_j) − 1| < ε, j = 1..k}, r_j ∈ ℤ̄ ∖ {0}. Choose an integer N₀ > 2/(1/a − 1/b) and p₀ so large that for p ≥ p₀: p > N₀ (so N₀ | L_p: N₀ ≤ p^p and p ∤ N₀), p ≥ [ℚ(r_j):ℚ] and p ∤ N(r_j) for all j (so ord(r̄_j) | L_p, by 3.1(b)). Fix p ≥ p₀ and u′ ≥ 1. The interval (N₀u′/b, N₀u′/a) has length N₀u′(1/a − 1/b) > 2 and contains an integer m ≥ 1; put q := m/N₀, so q⁻¹u′ ∈ (a, b). Since N₀ | ν_p, F_qP_p = F_mF_{N₀}⁻¹F_{ν_p}(x_p,χ_p) = F_{mν_p/N₀}(x_p, χ_p) ∈ X̊(ℂ), and its value at r_j is χ_p(r̄_j)^{mν_p/N₀} = 1 because ord(r̄_j) | L_p | ν_p/N₀ = L_p·(L_p/N₀). So F_qP_p ∈ V, F_qπ(P_p) ∈ W₀, (F_qπ(P_p), q⁻¹u′) ∈ Q⁻¹(U), and [π(P_p), u′] ∈ U. As u′ ranges over [1, p) this is all of γ̃_p (isotropy p^ℤ). ∎

Each step checked against the source: the box lifts by continuity of Q (definition of the quotient topology, p. 59); the basic neighborhood by p. 40; the chart membership by (51) p. 42 and the colimit relation p. 25; the divisibility by 3.1(b). The lemma is stronger than the adjudication's §4.1 version (which absorbs one point of γ_p and then invokes Lemma A); F's version absorbs the whole orbit directly by letting m range over an interval of length > 2.

### 3.5 K := Ω ∪ ⋃_p γ̃_p is nonempty, flow-invariant and quasi-compact ✓ (refuter F §3.3; each γ̃_p is the continuous image of the circle ℝ>0/p^ℤ under the orbit map u ↦ Q(π(P_p), u), which is continuous because Q is; a cover picks one member meeting Ω, which by the Key Lemma contains Ω and all γ̃_p with p ≥ p₀, and finitely many more members cover the remaining finitely many orbits). W ≡ +∞ on K (ρ̂ = ∞ at (η,1) and over closed points), so the dissipation half of face (b) is not contradicted; V_p ∩ Ω = ∅ for every p ((η,1)(p) = 1 ≠ 0 and Ω is F_q-fixed), so the packet-separation half simply does not cover K. ✓

### 3.6 The map f, its continuity and equivariance

Definition (refuter F §3.4). On N_p: f(ι_p(θ,0,·)) := [π(P_p), e^θ] on the core (well defined: θ ↦ θ + log p multiplies e^θ by p ∈ isotropy); on each non-closed orbit O ⊂ N_p choose y_O ∈ O and set f(φ^t y_O) := [π(P_p), e^t] (well defined since t ↦ φ^t y_O is injective on a non-closed orbit without fixed points — §2.2). On T² × {0}: every orbit is non-closed (§2.2); choose y_O on each and set f(ψ^t y_O) := [π(η,1), e^t] ∈ Ω. These choices use the axiom of choice on uncountably many orbits; no continuity of the choice is needed (below).

*Equivariance:* f(φ^t y) = φ^t f(y) on every orbit by construction ([P₀, u]·e^t = [P₀, ue^t], p. 38).

*f(C_p) = γ̃_p ⊂ Γ_p:* the core parametrization θ ↦ [π(P_p), e^θ] is a bijection ℝ/(log p)ℤ → γ̃_p (orbit map of a point with ℝ>0-isotropy p^ℤ). ✓

*Continuity on N_p:* N_p is open in Y and f(N_p) = γ̃_p ⊂ Γ_p. For U open in X₀^full, (f|_{N_p})⁻¹(U) = (f|_{N_p})⁻¹(U ∩ γ̃_p) ∈ {∅, N_p} by Lemma A, open. ✓ (Any map into an indiscrete subspace is continuous — this is why the orbit-wise base-point choices cost nothing.)

*Continuity at y ∈ T² × {0}:* f(y) ∈ Ω. For U ∋ f(y) open, Lemma B gives U ⊇ Ω and the Key Lemma gives U ⊇ γ̃_p for p ≥ p₀, so f⁻¹(U) ⊇ (T² × {0}) ∪ ⋃_{p ≥ p₀} N_p = Y ∖ ⋃_{p < p₀} N_p, which is open in Y (finite union of closed sets removed). ✓

*Continuity into Y₀:* f(Y) = K ⊂ Y₀ and Y₀ carries the subspace topology (§3 preamble), so f : Y → Y₀ is continuous. ✓

**§3 conclusion: (2) of the brief is verified in full.** f is a continuous flow-equivariant map from the compact metrizable 3-dimensional flow (Y, φ) into Y₀, with f(C_p) = γ̃_p a genuine periodic orbit of Γ_p (character χ_p^{ν_p} ∈ E_f, isotropy p^ℤ, Thms. 5.2/6.1 applicable) for every prime p, and f(T² × {0}) = Ω. Together with §2 this is refuter F's §3.4 sentence, verified: the adjudicated face-(b) sentence is false for the E-free Y₀ as printed on p. 49, with a compact metrizable 3-dimensional witness carrying exactly S4's orbit spectrum.

---

## 4. What f does — and what it cannot do

### 4.1 Ω, the torus, injectivity

Ω is a single ℝ-orbit of Y₀ whose stabilizer is ℚ>0 ⊂ ℝ>0 (dense, not closed): set-theoretically ℝ>0/ℚ>0, uncountable; topologically indiscrete (Lemma B); it is not a fixed point (e^t ∈ ℚ>0 fails for most t) and not a closed orbit (no minimal period: the period set is log ℚ>0, dense in ℝ). It lies over the generic point η of Spec ℤ, at W = +∞, in the (Tors)-violating locus. f maps the **whole 2-dimensional torus** onto Ω: every dense line-orbit of the irrational flow is sent onto Ω by t ↦ [π(η,1), e^t], with an arbitrary base point per orbit. So Ω is the image of a 2-dimensional invariant set (a compact minimal set of the source), not of a single orbit and not of a point — but since Ω is indiscrete, the restriction f|_{T² × {0}} is a map into an indiscrete space and carries no information whatsoever; any function T² → Ω that is equivariant would do.

f is injective exactly on each core C_p (bijective onto γ̃_p) and nowhere else: on N_p ∖ C_p the fibers are uncountable (all points of all non-closed orbits at "the same time" collide), on T² × {0} likewise. f is nowhere locally injective. The image f(Y) = K is the space Ω ⊔ ⨆_p γ̃_p whose topology is (§4.2) the pullback of the Alexandroff compactification {primes} ∪ {∞} with each point blown up to an indiscrete orbit.

### 4.2 The fibers of Y₀ over Spec ℤ are clopen; Y₀ is disconnected

Let Π : X₀^full → Spec ℤ be the descent of pr_{X₀} ∘ pr₁ (continuous, p. 43; constant on ℚ>0-orbits, p. 25), and Y₀(p) := Π⁻¹((p)) ∩ Y₀, Y₀(η) := Π⁻¹(η) ∩ Y₀.

Lemma D. Y₀(p) is clopen in Y₀ for every prime p; Y₀(η) is closed and not open; Y₀ = Y₀(η) ⊔ ⨆_p Y₀(p).

Proof. Closed: (p) is a closed point of Spec ℤ and Π is continuous. Open: let D := {P ∈ X̊(ℂ) : |P(p)| < ½} (open, ev_p continuous, p. 40), V_p := Q(π(D) × ℝ>0) = {[π(P), u] : P ∈ D, u > 0}, which is open in X₀^full: Q⁻¹(V_p) = ⋃_{q ∈ ℚ>0} (π(D) × ℝ>0)·q = ⋃_q F_q(π(D)) × ℝ>0 = π̌(⋃_q F_q(D)) × ℝ>0, and ⋃_q F_q(D) is open in X̌(ℂ) (D open in X̊(ℂ), X̊(ℂ) open in X̌(ℂ), F_q homeomorphisms, Prop. 7.4) and π̌ is open (p. 43) — the adjudication's (C), re-checked. For [P̌₀, u] ∈ Y₀ ∩ V_p: [P̌₀,u] = [π(P), u′] with P ∈ D, so π(P) = F_qP̌₀ for some q, and P̌₀ = π̌(F_ν⁻¹P′) with P′ unitary; thus P = (F_{q/ν}P′)σ for some σ ∈ G, and F_{q/ν}P′ ∈ X̊(ℂ) is unitary (if F_bP″ = F_aP′ then P″(r)^b = P′(r^a) ∈ S¹ ∪ {0}, so |P″(r)| ∈ {0,1}), so |P(p)| ∈ {0,1}, and P ∈ D forces P(p) = 0, i.e. P lies over (p), i.e. [P̌₀,u] ∈ Y₀(p). Conversely Y₀(p) ⊂ V_p (a point over p has a chart representative with P(p) = 0 ∈ D). So Y₀(p) = V_p ∩ Y₀ is open. Y₀(η) is the complement of the open union, hence closed; it is not open because Ω ⊂ Y₀(η) is accumulated by the γ̃_p (Key Lemma). ∎

So Y₀ is not connected (contrast [x-06] p. 12 Thm. 4.3 for X₀, X₀^E — connectedness there rides on the non-unitary generic characters, which Y₀ lacks; no printed statement asserts Y₀ connected). [novelty: single-check] I did not find Lemma D stated in the record; the adjudication's (C) proves the weaker "packets pairwise separated by open sets" and "closed with empty interior" for X₀^E.

### 4.3 Theorem C (the map is inert). Let Y be a compact space with a continuous ℝ-action and f : Y → Y₀ a continuous flow-equivariant map.

(i) Y = Y_η ⊔ ⨆_p Y_p with Y_p := f⁻¹(Y₀(p)) clopen and invariant and Y_η := f⁻¹(Y₀(η)) closed and invariant. If f meets infinitely many packets then infinitely many Y_p are nonempty and Y_η ≠ ∅ (compactness: the Y_p are disjoint clopen sets, so if Y_η = ∅ they would be a disjoint open cover with no finite subcover). If Y is connected, f(Y) lies in a single Y₀(p) or in Y₀(η).

(ii) f(Y_η) ⊂ Y₀(η) ∩ {W = ∞} = the unitary generic characters with infinite μ-kernel (the (Tors)-violating generic locus): Y_η is compact, invariant, and W is > 0, l.s.c., e^t-conformal on X₀^full (face (b) (A)–(B), which never use (Tors) — refuter F §2 lines (1)–(2), re-read), so W ≡ ∞ on f(Y_η). (Refuter F §3.5(iii) says this in words; here it is a statement about every compact witness.)

(iii) Conversely, let Y = Y_η ⊔ ⨆_{p ∈ S} Y_p be any compact space with a continuous ℝ-action without fixed points (Y₀ has none: the stabilizers are p^ℤ on Γ_p and ℚ>0 on Ω, never ℝ>0), S a set of primes, Y_p clopen invariant, Y_η closed invariant, such that every orbit in Y_p is non-closed or has minimal period in (log p)ℤ_{>0}, and every orbit in Y_η is non-closed or has minimal period in log ℚ>0. Then there is a continuous flow-equivariant f : Y → Y₀ with f(Y_p) = γ̃_p ⊂ Γ_p and f(Y_η) = Ω — with no further condition on Y.

Proof of (iii). Define f orbit-wise as in §3.6 (an orbit of minimal period k log p maps onto γ̃_p by t ↦ [π(P_p), e^t], well defined since e^{k log p} = p^k ∈ p^ℤ; an orbit of minimal period log q, q ∈ ℚ>0, maps onto Ω since q ∈ ℚ>0 = stabilizer). Continuity on Y_p by Lemma A (Y_p open, target indiscrete); continuity at y ∈ Y_η: for U ∋ f(y) open, Lemmas B and the Key Lemma give f⁻¹(U) ⊇ Y_η ∪ ⋃_{p ≥ p₀} Y_p = Y ∖ ⋃_{p < p₀} Y_p, open. ∎

**What f buys, exactly.** By (i)–(iii), the existence of a continuous equivariant map into the E-free Y₀ hitting every packet is equivalent to: a clopen decomposition of the source indexed by the primes, accumulating on a nonempty closed core, with the trivial period bookkeeping. The map pulls back no leafwise, transverse, cohomological or measure-theoretic structure — Y₀'s leaves (images of X̌₀(S¹) × {u}, [x-06] p. 11), its leafwise cohomology ([x-03] §10 Def. 10.1, p. 63), its ρ-map (p. 49) — because the image is a union of indiscrete orbits on which every continuous function is constant. The 1-dimensional bouquet (a circle of period log(3/2) with cabled circles C_p accumulating on it, refuter F's own remark) satisfies (iii) as well; the torus core was chosen only to make the core free of closed orbits (§2.2). **So "an equivariant map into Deninger's Y₀" is not a constraint on a source; it is a certificate that the source's orbit periods have been indexed by the primes.** This is the honest content of residue (R-ii).

---

## 5. The honest S4 comparison

### 5.1 The S4 specification (ledger §8, S4 row, read this session)

"a compact foliated space / Riemann-surface lamination Y₀ (dim 3 in the lamination sense), with (per §3): one simple closed orbit of length log p per prime with ε ≡ +1, the S3 fixed-point data at the archimedean place, α = 1 leafwise conformal structure, and a transverse measure making the counting exact" — the object on which S1/S2 (a leafwise trace formula of [Den05] Thm. 7.8 / [ALKL] type) is to produce the T1–T5 term classes of ledger §3, in particular **T1: log p · δ_{k log p} with coefficient exactly 1, one orbit per prime**, and T3: one archimedean term W_∞ from a fixed-point/preserved-leaf datum with κ = −2.

### 5.2 Clause-by-clause

| S4 / [ALKL] clause | Y of refuter F | Status |
|---|---|---|
| compact (ledger; not in [x-03] p. 40) | compact metrizable (§2.3) | met |
| foliated space with 2-dim leaves / Riemann-surface lamination, "dim 3 in the lamination sense" ([Den05] §7.1–7.3; [ALKL] H1–H2 closed manifold, codim-1 F) | no foliated-space structure exists (Theorem B); covering dim 3 only from the pieces; core is a 2-torus with a minimal flow | **fails, proved** |
| foliated flow (H3) | vacuous without F; on each piece the disc foliation makes φ a foliated flow transverse to F (§2.7) | fails globally |
| one closed orbit of period log p per prime, no others | Theorem A | met |
| simple closed orbits, ε ≡ +1 (H4) | true relative to the disc foliation on each N_p (§2.7); undefined on Y | met locally, undefined globally |
| S3 archimedean fixed-point data (T3; [ALKL] preserved leaves, transversely simple, κ_L) | no fixed points, no preserved leaf, no transverse rate; the absorbing set is the torus (source) / Ω (target, stabilizer ℚ>0) | **fails** |
| α = 1 leafwise conformal structure (T4/T2 weights) | disc leaves, flow a similarity with adjustable rate (§2.7); no global leaves | undefined globally |
| invariant transverse measure, counting exact (H6; ledger R15) | dθ on each piece; nothing across the accumulation | fails globally |
| carries a leafwise trace formula with the T1 orbital side (S1/S2 on the object) | no leafwise cohomology on Y (no F); [ALKL] needs a closed manifold; pieces are manifolds with boundary | **fails** |
| maps equivariantly into Deninger's space reaching every packet ([x-03] p. 40 "or at least one which maps to X₀") | yes, into the E-free Y₀ (§3); into no X₀^E (face (b)); and the map is inert (Theorem C) | met, vacuously |
| lands in an object Deninger proposes | the E-free Y₀ contains characters [x-06] p. 11 says "must" be excluded ("known for certain"); [x-03] p. 39's E-convention (J1) makes even the printed formula's E-freeness a reading | disputed target |

**Verdict: NOT S4-shaped.** The met clauses (compact; the orbit spectrum; an equivariant map) are exactly the clauses Theorem C shows to be trivially satisfiable; every clause with structural content fails, and two of them (lamination; trace formula) fail provably rather than merely unverified.

### 5.3 Q-b″ answered

Ledger §14: "Whether that source lamination carries a trace formula with the T1 orbital side, and what Ω's contribution is, is the next decidable question (Q-b″)." Decided: (a) the source is not a lamination (Theorem B), so no leafwise trace formula of the [Den05]/[ALKL] kind is defined on it — there is no leafwise cohomology to take a trace on; (b) on each piece N_p alone the local orbit datum is the [ALKL] one with ε ≡ +1 (§2.7), which would contribute log p Σ_{k ∈ ℤ^×} δ_{k log p} if a global formula existed, i.e. the T1 shape at k ≥ 1 and the unweighted (not T2) shape at k ≤ −1 unless the [Den05] α-weights are imposed leafwise — all of which is local and available on any solid torus; (c) "Ω's contribution" is not a question about Y: Ω is a point-set of the target, the source's absorbing set is the torus with a minimal flow, and it enters no trace formula because there is no formula. The S3 role that S4 assigns to the archimedean place — a preserved leaf/fixed set with a transverse rate κ producing the asymmetric W_∞ (T3) — is not played by Ω in any sense stronger than "the packets accumulate there", which is a topological statement about Y₀ (Lemma D, Key Lemma), not about a trace.

### 5.4 Whether any variant survives

By Theorem C(i), any compact source mapping into Y₀ and reaching every packet has the shape Y = Y_η ⊔ ⨆_p Y_p with Y_p clopen. A genuinely S4-shaped variant would therefore need: for each prime, a **compact foliated piece** Y_p (a compact 3-dimensional solenoid with a codimension-one Riemann-surface foliation, boundaryless leaves) with a foliated flow transverse to the leaves having **exactly one closed orbit, simple, of period log p**, and the pieces accumulating in local-product fashion (charts F × T with T = T_η ⊔ ⨆ T_p, which a totally disconnected T permits) onto a compact foliated core Y_η with no closed orbits, the flows converging. Two remarks, both [novelty: single-check]:

(a) *Lefschetz obstruction in the global-section sub-case.* If Y_p is the mapping torus of a diffeomorphism h of a closed surface Σ (leaves = fibers, flow = suspension with return time τ), closed orbits ↔ periodic orbits of h, and "exactly one, simple" means h has exactly one periodic orbit, a k-cycle of hyperbolic points. Then for every j ≥ 1 the fixed points of h^j have index sum L(h^j) = 2 − tr(h^j_* | H₁(Σ)) (orientation-preserving h), and a single hyperbolic k-cycle contributes 0 to L(h^j) for k ∤ j and ±k (the same sign for all m, the k points of the cycle being conjugate under h) to L(h^{mk}). *h ≃ id:* L(h^j) = χ(Σ) for all j; χ = 0 (torus) forces ±k = 0, impossible; χ ≠ 0 forces fixed points of h^j for every j, so more than one periodic orbit unless k = 1 with a single fixed point of index χ(Σ) ∉ {±1}, which is not hyperbolic. *Σ = T², h ≁ id:* with B := h^k_* ∈ SL₂(ℤ), L(h^{mk}) = 2 − tr(B^m) must be the constant ±k for all m ≥ 1, i.e. λ^m + λ^{−m} constant for the eigenvalues λ^{±1} of B, which forces λ = 1 and L = 0 ≠ ±k — impossible. *Σ = S²:* L(h^j) = 2 for all j, so h^j has fixed points for all j, and one hyperbolic cycle cannot carry index sum 2 for every j. *Genus g ≥ 2, h ≁ id:* the same power-sum argument forces the eigenvalues of h^k_* on H₁ to be all 1, hence k = 2g − 2 with index −1 (saddles), and the eigenvalues of h_* to be the multiset {1, 1} ∪ μ_{2g−2}; I have not excluded this case. So the obstruction is complete for h ≃ id (every surface), for the torus and the sphere (every h), and leaves open only genus ≥ 2 with h_* of the stated finite-order spectrum; every other S4 piece must have non-compact leaves or no global cross-section. Whether such a piece exists is open here.

(b) *Even if it existed, the E-free target adds nothing* (Theorem C). The specification "S4 with target Y₀ (E-free)" is equivalent to "S4 with no target at all, plus the prime-indexed clopen decomposition". Since the ledger's S4 already demands the orbit spectrum, the residue (R-ii) reduces to: build the compact foliated flow with the T1–T5 data directly. That is S4 as it stood before Session 14, minus the mapping clause. The mapping clause into X₀^E is dead (face (b), enacted); the mapping clause into the E-free Y₀ is alive and empty.

Consequently the honest statement of the residue is: **(R-ii) is not an escape from the S4 existence problem; it is the S4 existence problem with an inert target attached.** The only remaining genuine residue is (R-i), the unbuilt X̄₀.

---

## 6. Verdicts (schema)

- **construction:** VERIFIED. Every claimed property of (Y, φ, f) is proved (§§2–3), with the three specifications of §0 supplied (Lipschitz tube field (2.3); explicit 3-dimensional embedding (2.2); radius bounds (2.1)). No step of refuter F's §3.1–3.4 is wrong. Record correction: the word "lamination" for Y in ledger §14 and in this task's brief is wrong and must be struck; refuter F's §3.5(i) already says Y is not one, and Theorem B proves that no foliated-space structure exists on Y.
- **s4_shaped:** NO. Clauses met: compact; one closed orbit of period log p per prime and no others; a continuous equivariant map into the E-free Y₀ reaching every packet. Clauses failed: foliated space / lamination (proved impossible); global simplicity and ε (undefined); archimedean fixed-point/preserved-leaf data (absent); transverse measure and α = 1 structure (undefined globally); leafwise trace formula with T1 side (no leafwise cohomology exists). The met clauses are shown trivially satisfiable (Theorem C(iii)); the map carries no structure (Theorem C).
- **Q-b″:** decided negatively (§5.3). **Residue (R-ii):** collapses into the S4 existence problem with an inert target (§5.4); the ledger §14 phrase "the first positive S4-shaped object in the program's record" should be replaced by "a compact witness that the E-free unitary system admits a universal, structurally inert comparison map from any prime-indexed clopen-decomposed compact flow."

---

## 7. Novelty ledger (everything here not already in the record) — all [novelty: single-check]

1. **Theorem B** (§2.6): refuter F's Y admits no foliated-space structure with 2-dimensional leaves and no 3-solenoid structure; proof by uniform convergence of plaques against thin geodesic strips. (Refuter F asserted "not a lamination in the local-product sense" without proof and only for the natural foliation.)
2. **Lemma A in X₀^full** (§3.2): the whole packet Γ_p is indiscrete in the E-free suspension, by the p-adic (inverse-Frobenius) trick with explicit open sets; the adjudication proves it for X₀^E by nets.
3. **Lemma D** (§4.2): the fibers Y₀(p) of the E-free unitary system over the closed points are clopen; Y₀ is disconnected; Y₀(η) is closed, not open.
4. **Theorem C** (§4.3): forced clopen shape of every compact witness; the generic core maps into the (Tors)-violating locus; converse construction with only period bookkeeping; hence the E-free target is inert. This is the item that changes the reading of residue (R-ii).
5. **§2.7**: the disc foliation on each piece realizes [ALKL]'s simple-orbit datum with ε ≡ +1 at C_p (explicit linearization p^{−k}R(2πkλ)); dθ is an invariant transverse measure on the piece.
6. **§5.4(a)**: Lefschetz obstruction — a mapping torus of a closed surface with exactly one simple closed orbit is impossible for h ≃ id (all genera), for the torus and the sphere (all h), and is confined in genus ≥ 2 to h_* with spectrum {1,1} ∪ μ_{2g−2} and a (2g−2)-cycle of saddles (not excluded); otherwise a foliated S4 piece needs non-compact leaves or no global section.
7. **§2.2**: the regularity requirement on the tube field (F's wording admits non-Lipschitz h with non-unique backward solutions); (2.3) fixes it.
8. **J1** (§1.8): [x-03] p. 39's "we omit E from the notation" makes the E-freeness of p. 49's printed Y₀ a reading, not a certainty; recorded, not adjudicated, since Theorem C makes both readings inert for S4.

Items 2–4 use only [x-03] pp. 22–25, 31–34, 38–43, 49–50, 59 and the quotient-topology definition; items 1, 5–7 are differential topology of the source with no arithmetic input.

---

## 8. Honesty record (standing order 5)

**Re-derived in full this session:** §2 entire (with my own explicit choices); Lemma A (independent p-adic proof, not the adjudication's net); Lemma B; the Key Lemma step by step; quasi-compactness of K; continuity and equivariance of f; Lemma D; Theorem C; Theorem B; the §2.7 linearization; the §5.4(a) Lefschetz counts (for h ≃ id via L(h^j) = χ(Σ); for hyperbolic/elliptic A ∈ SL₂(ℤ) via L = 2 − tr A^j, where tr A^j ≠ 2 for infinitely many j).

**Read as printed, proofs not re-derived:** Lemma 7.3/(51) (p. 42), Prop. 7.4 (p. 43), openness of π̌ (p. 43), the p. 47 E-locus sentences, Thm. 5.2/6.1 (isotropy p^ℤ; used through pp. 32–33's explicit isotropy computation, which I did read), Thm. 8.2 (used only to identify Y₀; the closedness of X̊(S¹) in X̊(ℂ) from its proof), the face-(b) items (A)–(B) of the adjudication (W well defined, l.s.c., conformal — re-read in refuter F §2 lines (1)–(2), not re-derived here; used only in Theorem C(ii)).

**[RU] items:** whether [Ghy99]'s "Riemann surface lamination" includes compactness or admits dimension jumps (not on disk); if Ghys's definition were weaker than [Den05] §7.1's, Theorem B would not by itself settle the p. 40 clause — but it settles the program's S2/S4 specification, which is [Den05]'s. The countable sum theorem and "dim ≥ 3 because a 3-ball embeds" (standard dimension theory) and the restriction-of-quotient-maps fact (standard point-set topology) are used without source; I regard them as textbook facts, flagged.

**Judgment-grade readings, flagged:** (J1) E-free vs E-restricted printed Y₀ (§1.8). (J2) the quotient topology on the E-free suspension (§1.7; the printed definition p. 59 is for admissible E).

**Model note (standing order 7):** this verifier runs on the same model as refuter F. I therefore did not reuse F's proofs: Lemma A is proved by a different mechanism, Theorem B and Theorem C are new, and §2's specifications were chosen without consulting F's beyond the printed constraints. Every place where I agree with F is a place where I re-derived and found the same thing.

**Nothing rounded.** The construction is right and the lead is wrong: the object exists, it is not a lamination, and the map that made it look S4-shaped is provably empty.

— end of verify-F.md —
