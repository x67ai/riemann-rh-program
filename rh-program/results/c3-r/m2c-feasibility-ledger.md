# M2c FEASIBILITY LEDGER — transplanting the ALKL trace-formula framework to Deninger's Witt space X(Spec Z)

**Program:** RH program, direction C3-r (reduced recommission, binding adjudication 2026-08-26, `results/adjudication-C3.json`).
**Milestone:** M2c, clause (i) ONLY — the trace formula (the Weil explicit formula derived from a space: primes = closed orbits with lengths log p, archimedean place = fixed-point-type datum). Clause (ii) (positivity / leafwise Hodge / Kähler scalar product) is **quarantined behind guard Z2 and is not touched anywhere in this document**; no sentence below may be cited for positivity content.
**Date:** 2026-08-26 (Session 6). **Author:** M2c ledger agent (session-budgeted, per the adjudication's mandatory repair 5: "an obstruction ledger whose exhaustion counts as 'failed' so the lifecycle conversion can actually fire").

## VERDICT (stated first): **OPEN-WITH-LEDGER**

- The **direct transplant** of the Álvarez López–Kordyukov–Leichtnam (ALKL) framework to the Witt space X(Spec Z) **as Deninger constructed it is dead**: rows R1, R2, R4, R5, R6, R7, R8, R9, R15 below are OBSTRUCTED for that route, each with a source-tagged reason, most of them published by Deninger himself.
- **Verbatim ALKL output has the wrong shape for the Weil formula** even granting a space: three structural term-shape mismatches (rows R11–R13) are independent of all smoothness issues and are documented in print (Deninger math/0505354 pp. 19, 23–24, 27, 30–31; Leichtnam arXiv:1307.3851 §4.2/§4.4).
- **One route remains unobstructed** (Route 2, the solenoid/foliated-space intermediate): every analytic step in it is well-posed transplant work, **but the route runs through an existence problem that is not a work item** — the existence of a finite-dimensional arithmetic solenoid Y₀ with one orbit per prime, archimedean fixed-point data, and α = 1 leafwise conformal scaling. That is Deninger's own open problem (x-03 §6 end, §8), open since 1998 in one form or another, and the constructed Witt space is **negative evidence** for it in three independent ways (rows W6, W7, W9).
- Therefore: **not** `failed-ledger-exhausted` (Route 2 hits no OBSTRUCTED row — the kill-criterion does **not** fire on this leg today); **not** `feasible-route-identified` (Route 2's step S4 is an open existence question, not well-posed work). UNKNOWN rows remain that future sessions can attack (§9). The single decider is stated in §8/§9.
- **Program-level reading (honest):** M2c reduces to (a) an instrument-grade analysis transplant (ALKL machinery to foliated spaces/solenoids — real, publishable, arithmetic-free) plus (b) a substrate-existence problem. That is the same shape the adjudication found in M3 ("the non-field-base extension IS the substrate problem"): **on the Deninger leg too, the generator/analysis exists and the geometry does not.** The sweep's central finding recurs on its third leg.

---

## 1. Sources and evidence level

All load-bearing claims below are tagged to sources **read on disk this session**. Nothing is from memory. arXiv and github were unreachable (IPv6 ISP issue); PDFs were fetched via the Google-Cloud-Storage arXiv mirror (`storage.googleapis.com/arxiv-dataset/...`) and verified by page count and content.

**Fetched and read this session (scratchpad copies):**
- **[ALKL]** J.A. Álvarez López, Yu.A. Kordyukov, E. Leichtnam, *A trace formula for foliated flows*, arXiv:2402.06671v1, **176 pp** (page count verified — matches the Phase-4 killer verification). Read: abstract (p. v), Ch. 1 in full (pp. 1–8), §4.1 (pp. 99–101), bibliography (pp. 161–166). Not read linearly, per the task instruction; the hypothesis package is extracted from the abstract, §1.3, and the definitional §4.1 the main theorems invoke.
- **[ALKM]** J.A. Álvarez López, J. Kim, M. Morishita, *Regularized determinant formulas for the zeta functions of 3-dimensional Riemannian foliated dynamical systems*, arXiv:2410.20758v1, 33 pp. Read: abstract, Introduction, §1 (Definitions 1.1/1.4, Remark 1.2, Theorem 1.3).
- **[Den05]** C. Deninger, *Arithmetic geometry and analysis on foliated spaces*, arXiv:math/0505354v1, 48 pp. Read: §3 (Prop. 3.2 = the explicit formula), §4 (Thm 4.1 + the conformal-metric caveat), §5 (Conj. 5.1, Thm 5.3, Thm 5.4, Cor. 5.5 with Remarks 2–3), §6 (the dictionary and the α = 1 / weights discussion, pp. 26–27), §7 (foliated spaces/solenoids, working hypothesis 7.5, Thm 7.8 + CM-elliptic-curve example, remarks pp. 30–33).
- **[Lei13]** E. Leichtnam, *On the analogy between L-functions and Atiyah–Bott–Lefschetz trace formulas for foliated spaces*, arXiv:1307.3851v1, 29 pp. Read: §3 (Guillemin–Sternberg Prop. 1; ÁLK Hodge + trace formula Thm 1), §4.1 (axioms 1]–8] for the conjectural laminated space S_K), §4.2 (Lemma 1, Props. 2–4), §4.4 (the real-place incompatibility and its orbifold resolution).

**On disk (program corpus, per `results/corpus-routing.md` — header caveats checked; none of the files below is on the vision-only or broken-text-layer lists):**
- **[x-03]** C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400**v4**, `fetched/x-03-...pdf`, 119 pp (cite v4 only; published = Indag. Math. 37 (2026) 25–136 = z-19). Read: Introduction (pp. 1–7), §1 (rational Witt vectors), §5–§10 in targeted depth (orbit packets, suspension structure, Arakelov-compactification discussion, topology, closure of periodic orbits, connectedness, leafwise cohomology).
- **[x-06]** C. Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643 (= [Den23] in ALKL's bibliography), `fetched/x-06-...pdf`. Read: §3 (the manifold analogy, formula (7), the α-obstruction paragraph p. 8), §4 (Theorems 4.1–4.4 and the packet discussion).
- **[r3s-08]** M. Morishita, *On a relation between Deninger's foliated dynamical systems and Connes–Consani's adelic spaces*, arXiv:2508.15971**v5** (21 Jan 2026), `fetched-r3/r3s-08-...pdf`. Read: abstract + introduction.
- **[x-04]** C. Deninger, arXiv:2204.02714 (the real-coefficient Weil-cohomology no-go) — cited via its verified program record and via x-06's own reference to it ([Den22b] there); not re-read this session.

**Online prior-art checks (standing order 1 — server-side WebSearch, 4 queries, all returned):** (1) "Deninger rational Witt dynamical system trace formula 2025" — no trace formula on the Witt spaces exists; newest Deninger item is arXiv:2508.05329 (*Rational Witt vectors and associated sheaves*, Aug 2025), sheaf-theoretic foundations only. (2) "Álvarez López Kordyukov Leichtnam 2025/2026 solenoid arithmetic" — no post-2024 transplant of the ALKL conormal framework to non-manifold or arithmetic settings found; no announced Part II. (3) arXiv:2508.05329 content check — confirmed no dynamical/trace-formula content beyond citing [x-03]. (4) "Junhyeong Kim trace formula solenoid 2025" — nothing beyond [ALKM] and Kim's S¹-fiber-bundle paper (arXiv:1712.04181). **Conclusion: as of 2026-08-26 nobody has published either the transplant or a no-go; both remain open in the literature.** (Resource limitation disclosed: arxiv.org listing pages themselves were unreachable; searches were server-side and could miss very recent postings.)

---

## 2. The ALKL hypothesis package (what the framework REQUIRES)

Extracted from [ALKL] abstract (p. v), §1.3.1 (pp. 2–4), §1.3.5–1.3.6 (pp. 5–8), §4.1 (pp. 99–101). The theorem chain is Theorems 1.3.1–1.3.10; the trace formula is:

> **Theorem 1.3.10** ([ALKL] p. 7). L_dis(φ) = Σ_L χ(L)·W_L + ᵇχ_{|ω¹|}(F¹)·δ₀ + Σ_c ℓ(c) Σ_{k∈Z^×} ε_c(k)·δ_{kℓ(c)},
> with ⟨W_L, f⟩ = ∫₀^∞ [ (f(t)+f(−t))/|e^{κ_L t}−1| − 2f(0)/(|κ_L|t) ] dt ([ALKL] p. 7, after [Bar81]).

**H1 — Phase space:** M a **closed smooth manifold** ([ALKL] abstract; §4.1.2 "F a transversely oriented smooth foliation of codimension one on a closed manifold M"). Compactness is used essentially: finiteness of preserved leaves, finiteness of C_I(φ), b-calculus on the compact cut manifold M̄.
**H2 — Foliation:** F smooth, codimension one, transversely oriented; defined by a 1-form ω with dω = η∧ω ([ALKL] §1.3.1 p. 2).
**H3 — Flow:** φ a foliated flow (leaves to leaves; generator Z projects to a Bott-parallel section of NF) ([ALKL] §1.1 p. 1).
**H4 — Nondegeneracy:** closed orbits **simple** — id − φ_*^{kℓ(c)} : N_pφ → N_pφ an isomorphism for all k ∈ Z^×, with N_pφ ≅ T_pF on M¹ ([ALKL] §4.1.1 p. 99); preserved leaves **transversely simple** — the induced local flow φ̄ on the 1-dim local transversal Σ has simple fixed points, φ̄^t_*(x) = e^{κ_L t}x ([ALKL] §4.1.2 p. 100). Consequences: Fix(φ̄) isolated ⟹ **finitely many preserved leaves, all compact**; C_I(φ) finite for compact I; the period set P(φ) discrete in R ([ALKL] §4.1.1 p. 99).
**H5 — Transversality:** φ transverse to all non-preserved leaves; on M¹ = M∖M⁰ the foliation F¹ becomes a transversely complete R-Lie foliation; F is almost without holonomy, with the ÁLKL22 classification (cases (c)–(f), holonomy of the compact leaves = groups of germs of homotheties, Hol L finitely generated abelian) ([ALKL] §1.3.1 p. 2, §4.1.2 pp. 100–101).
**H6 — Metric structure:** a Riemannian metric g on M with ω the transverse volume form; leafwise metric g_F; on M¹ the bundle-like metric g¹ of **bounded geometry** with Z of norm one on NF¹; invariant transverse density |ω¹| ([ALKL] §1.3.1 p. 3).
**H7 — Tubular/defining structure at M⁰:** T ≅ (−ε,ε)×M⁰ with defining function ρ, d_Fρ = ρη, φ^t_*ρ = e^{κ_L t}ρ; the class ξ = [η|_{M⁰}] ∈ H¹(M⁰) is fixed by F but η, g|_{M⁰} are **choices** ([ALKL] §1.3.1 p. 3).
**H8 — The analytic apparatus:** conormal and dual-conormal distributions at the smooth submanifold M⁰ (Sobolev spaces H^s(M), the filtered algebra Diff(M, M⁰), the LF-space I = ∪ I^(s), its dual I′; spaces K, J, K′, J′ and the two short exact sequences (1.3.1)/(1.3.2)) ([ALKL] §1.3.2 pp. 4–5); the **small b-calculus** on the compact manifold-with-boundary M̄ obtained by cutting along M⁰, b-metrics, b-integrals with a trivialization ν of N∂M̄, and the **b-trace of smoothing b-pseudodifferential operators** (not a trace — it does not vanish on commutators) ([ALKL] §1.3.1 pp. 3–4, §1.3.5 p. 7); **Witten perturbations** d_{F,μ} = d_F + μη∧ = ρ^{−μ}d_Fρ^μ and leafwise heat operators e^{−uΔ_{F,μ}} on H^{±∞}(M̊; ΛF) ([ALKL] §1.3.3–1.3.4 p. 5).
**H9 — Two cohomologies, not one:** the Lefschetz distribution has **no reasonable definition on a single leafwise reduced cohomology**; it is assembled from H̄•I(F) AND H̄•I′(F) via the K/J and K′/J′ exact sequences, with the leaf contributions **split by the sign of κ_L t** ("the other leaves in M⁰ are omitted as a way of renormalization") and the J-side defined through iterated limits of b-supertraces ([ALKL] §1.3.6 pp. 7–8, verbatim: "It seems there is no reasonable definition of L_dis(φ) with a single leafwise reduced cohomology").
**H10 — Even leaf dimension + choices:** dim F even (dim F = 2 is "the relevant case in Deninger's program"); Theorem 1.3.9 holds only after choosing η and g on M⁰ so that the defect distribution Z_μ → 0 as μ → ±∞ — for general choices the limits are nonzero multiples of δ₀ (an eta-invariant-like b-trace anomaly) ([ALKL] §1.3.5 p. 7).
**H11 — Test class:** f ∈ C_c^∞(R); Z_μ tempered ([ALKL] Thms 1.3.7–1.3.9).
**H12 — Output shape:** orbit terms ℓ(c)ε_c(k)δ_{kℓ(c)} with ε_c(k) ∈ {±1} for ALL k ∈ Z^× (positive and negative); leaf terms χ(L)W_L with W_L **even in t**; δ₀-coefficient the b-Connes–Euler characteristic ([ALKL] Thm 1.3.8, Thm 1.3.10, p. 6–7).

**ALKL's own arithmetic caveat, verbatim** ([ALKL] §1.1 pp. 1–2): "It became clear that more generality is needed to draw arithmetic consequences (perhaps foliated flows on possibly singular foliated spaces of arithmetic nature). … we believe that the techniques developed in this paper will be useful in arithmetic **once the appropriate framework allowing to interpret the Weil's explicit formulae for arithmetic zeta functions as Lefschetz trace formulae will have been discovered**." The authors themselves place the framework discovery BEFORE their techniques apply; they cite [Den22] = x-03 and [Den23] = x-06 as "further developments", not as an application target their theorem covers.

---

## 3. The target identity (what clause (i) must produce)

Weil explicit formula in Deninger's dynamical normalization ([Den05] Prop. 3.2, formula (4), pp. 9–10), for a number field K, Φ(s) = ∫ φ(t)e^{ts}dt:

> Φ(0) − Σ_ρ Φ(ρ) + Φ(1) = −log|d_{K/Q}|·φ(0) + Σ_{p∤∞} log Np [ Σ_{k≥1} φ(k log Np) + Σ_{k≤−1} **Np^k** φ(k log Np) ] + Σ_{p|∞} W_p(φ),
> with W_p(φ) = ∫ φ(t)/(1−e^{κ_p t}) dt on supp φ ⊂ R_{>0} and W_p(φ) = ∫ φ(t)·**e^t**/(1−e^{κ_p|t|}) dt on supp φ ⊂ R_{<0}; κ_p = −2 (real), −1 (complex).

Term classes a space-derived trace formula must reproduce, for K = Q:
- **T1 (primes, k ≥ 1):** log p · δ_{k log p} with coefficient exactly 1, one orbit per prime.
- **T2 (primes, k ≤ −1):** log p · **p^k** · δ_{k log p} — exponentially weighted.
- **T3 (archimedean):** ONE real-place term W_∞, **asymmetric in t** (bare 1/(1−e^{−2t}) for t > 0, extra factor e^t for t < 0).
- **T4 (poles):** Φ(0) + Φ(1) on the spectral side — the H⁰-trace (Θ = 0) and an H²-type trace with **Θ = 1** (the flow must scale the leafwise volume class by e^t: "α = 1").
- **T5 (discriminant):** −log|d_{K/Q}|·φ(0); = 0 for Q — matching ALKL's ᵇχ·δ₀ slot (dictionary: ᵇχ_{|ω¹|}(F¹) ↔ −log|d_{K/Q}|, [Den05] (29) p. 26). A genuine consistency check, and the only term class with no shape problem.
- **Signs:** all ε ≡ +1 ([Den05] remark 4 p. 31: "fits perfectly with the explicit formula … if all ε_{γ_p}(k) = 1 and ε_{x_p} = 1"; [x-06] §3).

Clause (i) splits: **(i-a)** the geometric-side identity (trace formula on the space); **(i-b)** identification of the spectral side with Φ(0) − ΣΦ(ρ) + Φ(1), i.e. Θ-spectrum on the H¹-object = nontrivial zeros with multiplicity. (i-b) carries no positivity — Meyer's theorem (zoo/Z3: unconditional RH-empty spectral realizations exist) applies; nothing here claims RH content.

---

## 4. What the Witt space actually provides

From [x-03] (v4) with [x-06] as Deninger's own summary. The object: for X₀ = Spec Z, the ringed space W_rat(X₀) = (X₀^top, W_rat(O_{X₀})) (sheafified rational Witt vectors; **not a locally ringed space**, [x-03] intro p. 4); its C-points X₀^•(C) = W_rat(X₀)(C) = space of multiplicative maps with commuting injective Frobenius endomorphisms F_p; X̌₀(C) = colim_N X₀^•(C) (Frobenii inverted, a Q^{>0}-action); and the dynamical system

> **X₀ = X̌₀(C)_E ×_{Q^{>0}} R_{>0}**, φ^t[m, u] = [m, e^t u] ([x-03] intro pp. 2, 5; §6),

after imposing an "admissible condition" E on characters — needed because the raw system "has too many periodic orbits, since the N-space W_rat(X₀)(C) does not know enough about the addition in O_{X₀}"; a minimal workable E exists "but it does not look natural" ([x-03] intro p. 5; [x-06] §4 p. 11).

- **W1 — Topology:** X₀^•(C) carries the topology of pointwise convergence (Tychonov subspace of C^R); metrizable, separable; Hausdorff when X₀ is affine or carries an ample invertible sheaf, **unknown in general** ([x-03] §7, Cor. 7.9 + following Remark, pp. 46–47). Compactness of X₀: **not established anywhere in the paper**; only the packets Γ_{x₀} are compact. **Infinite-dimensional** for dim X₀ ≥ 1 ([x-03] §8 p. 49; [x-06] p. 12). **Not locally Euclidean; no smooth structure; no metric structure.**
- **W2 — R-action:** genuine continuous R_{>0}(≅ R)-flow, mapping "leaves" to "leaves", transverse to them in the suspension sense. Real and unconditional.
- **W3 — Closed orbits, the one correct datum:** points with nontrivial isotropy decompose as ⨿_{x₀} Γ^E_{x₀} over the closed points x₀ (primes p for Spec Z), isotropy N x₀^Z, i.e. **every periodic orbit has length exactly log p for its prime, and every prime occurs** ([x-03] Thm 6.1 pp. 38–39; [x-06] Thm 4.2). This is precisely T1's length data — the provision no manifold can match (see R14).
- **W4 — Packet degeneracy:** the orbits of length log p form a **compact packet** Γ_{x₀}, a fiber space over the **uncountable** compact group Ẑ×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p)^, with fibers the individual orbits ([x-03] intro p. 2, §5 (39)–(40) p. 32; [x-06] Thm 4.2). "The correspondence … is not one-to-one but a bit more involved. The compact packets Γ_{x₀} are reminiscent of invariant tori" ([x-03] p. 2). So per (p, k) the would-be orbit sum has **uncountable multiplicity**; orbits are **not isolated** (they form continua).
- **W5 — Fixed points:** "**There are no fixed points of the flow**" ([x-03] intro p. 2). The archimedean datum exists only as a PREDICTION about a compactification X̄₀ ("X₀ should have a 'compactification' X̄₀ corresponding to an Arakelov compactification"; fixed-point set X₀(C)/F_∞; the immersion X₀(C)×_{F_∞}R ↪ X̄₀ "should extend") — with Deninger's own printed caveat: "**it is unclear, why X̄₀ would not contain many more fixed points** obtained in the same way from the points in X̌₀(C)∖X₀(C)" ([x-03] §6 pp. 39–40).
- **W6 — Not a foliation, not even a foliated space:** the leaf partition {images of X̌₀(C)×{u}} is in general **not locally trivial**, and the leaf bijection π|_{M×{u}} is **not a homeomorphism onto its image**: "If Q acts properly discontinuously on M×R^{>0} and if M is a manifold, then F is an actual 1-codimensional foliation. **In general however the partition of X into the disjoint spaces π(M×{u}) … will not be locally trivial**" ([x-03] §10 p. 63). The scare quotes on "foliation" are Deninger's own throughout. X₀ is therefore **not** a foliated space in the Moore–Schochet sense and **not** a solenoid (leaves are infinite-dimensional, transversals are not totally disconnected).
- **W7 — Small subsystems fail so far:** the closure of the union of all periodic orbits is Y₀ = X̌₀(S¹)×_{Q^{>0}}R_{>0} — **still infinite-dimensional** ([x-03] §8, Thm 8.2 pp. 49–50, unconditional for dim X₀ = 1 flat via Perucca). Deninger's open question, verbatim: "The system X₀ may have to be replaced by a much smaller system: Is there a sub-dynamical system Y₀ ⊂ X₀ … or at least one which maps to X₀ such that dim Y₀ = 2d+1 … If d = 1, is there such a Y₀ which is a Riemann surface lamination in the sense of [Ghy99]?" ([x-03] §6 p. 40).
- **W8 — Cohomology:** only the sheaf-theoretic leafwise cohomology H•_F(X) = H•(X, R_X) (R_X = continuous functions locally constant along leaves) is defined; the single computed group is H⁰_F = R ([x-03] §10, Thm 10.2 pp. 63–64). No differential forms, no leafwise de Rham complex (leaves are not manifolds), no Hodge theory, no heat flow, no trace-class structure, no conormal theory. Regular functions give genuine functions on X₀^•(C) but only "generalized functions" on X̌₀(C) and X₀ ([x-03] §§11–12).
- **W9 — The local case knows the fix, the global case does not:** p-adically, Deninger finds the natural Frobenius-invariant subsystem Y⋄ (mod-p-additive multiplicative maps), which recovers **the closed points of the Fargues–Fontaine curve** ([x-03] §§13–15, Thm 15.6). Globally: "In the local p-adic situation below, we know the right modification to make. However in the global case presently we can only impose an 'admissible' condition E" ([x-06] §4 p. 11). The correct global subsystem — the one a trace formula would live on — is **not known**.
- **W10 — Connectedness/irreducibility flavor:** X₀ is connected (Thm 9.x, via de Jong alterations for dim ≥ 2), and the proof of H⁰_F = R runs through **irreducibility** of an adele-topology quotient ([x-03] §§9–10, Prop. 10.3) — the topology is scheme-like ("bad" adele topology working to advantage), far from the manifold/solenoid regime where trace formulas live.
- **W11 — The Morishita bridge adds no structure usable here:** [r3s-08] constructs a continuous, Galois-equivariant, flow-ANTI-equivariant map from Deninger's systems (abelian number fields) into Connes–Consani adelic spaces, matching closed orbits (its Thm 3.6); it is class-field-theoretic topology (the linking homomorphism lk_p: p^Ẑ → Ẑ×_{(p)} as monodromy). It transports no smooth, metric, foliated-space, or analytic structure and states no trace formula. (Consistent with C3-r caution R5: comparison map only.)

---

## 5. THE LEDGER

Statuses: **TRANSFERS** / **TRANSFERS-WITH-WORK** (work named) / **OBSTRUCTED** (reason named) / **UNKNOWN** (decider named). "Direct" = transplant ALKL to X₀ as constructed; the solenoid route is priced separately in §8.

| # | ALKL requirement | What the Witt space offers | Status (direct transplant to X₀) |
|---|---|---|---|
| R1 | Closed smooth manifold M (H1) | Metrizable separable topological space; Hausdorff known only for affine/ample; compactness not established; infinite-dimensional; no smooth structure [W1] | **OBSTRUCTED** — no element of the smooth category exists; Deninger in print: the smooth-compact-manifold class is "too restrictive" for the explicit formulas ([x-06] p. 8) |
| R2 | Smooth codim-1 transversely oriented foliation, ω with dω = η∧ω (H2) | Leaf partition not locally trivial; leaf maps not homeomorphisms; "foliation" in scare quotes; not a foliated space/solenoid [W6] | **OBSTRUCTED** — fails Deninger's own §10 test ([x-03] p. 63) |
| R3 | Foliated flow φ (H3) | Genuine continuous R-flow, leaves to leaves, transverse [W2] | **TRANSFERS** |
| R4 | Simple (isolated, nondegenerate) closed orbits; N_pφ ≅ T_pF finite-dim (H4) | Orbits in uncountable compact packets — not isolated; no tangent spaces exist, nondegeneracy unstatable; per-(p,k) multiplicity uncountable [W4] | **OBSTRUCTED** — hypothesis fails in every reading; repair = pass to a one-orbit-per-packet subsystem, whose existence is open (→ S4) |
| R5 | Finitely many compact preserved leaves, transversely simple (archimedean home) (H4/H7) | **No fixed points at all** [W5]; archimedean datum lives in an unconstructed compactification with a published over-supply problem [W5] | **OBSTRUCTED** — the T3 term has no home in X₀; Deninger's own caveat ([x-03] p. 40) |
| R6 | dim F even, = 2; dim M = 3 (H10) | Leaves infinite-dimensional; the wanted 3-dim subsystem is Deninger's open question; closure of orbits still infinite-dim [W7] | **OBSTRUCTED** as constructed; **UNKNOWN** via Y₀ (decider: existence of the 3-dim lamination) |
| R7 | Bundle-like metric, leafwise metric, bounded geometry on M¹, invariant transverse density (H6) | No metric or differentiable structure of any kind; only the sheaf R_X [W8] | **OBSTRUCTED** (direct); exists on solenoids ([Den05] §7.1–7.2) |
| R8 | Conormal/dual-conormal theory at M⁰; b-calculus on the cut manifold; Witten perturbations; b-trace (H8) | No M⁰ (no preserved leaves); no Sobolev/distribution theory; nothing to cut along [W5, W8] | **OBSTRUCTED** (direct) |
| R9 | The two-cohomology L_dis definition with its renormalizations and (η, g)-choices (H9, H10) | Only H⁰_F known; no candidate for I/I′; the DS01 counterexample (§7 below) forbids the naive single-cohomology shortcut | **OBSTRUCTED** (direct) |
| R10 | Test class C_c^∞(R), output in D′(R) (H11) | The pairing ⟨f, φ*⟩ is meaningful once a trace exists; no trace-class structure available | **UNKNOWN** — parasitic on R7/R8 |
| R11 | Orbit-weight shape: theorem outputs ε_c(k) ∈ {±1} for all k; leafwise return Jacobian ≡ 1 (H12) | Target T2 needs Np^k for k ≤ −1, i.e. leafwise Jacobian e^{ℓ(c)} per period ("α = 1") | **OBSTRUCTED for any verbatim ALKL transplant, on any space**: in the manifold setting \|det(T_xφ^{kℓ}\|T_xF)\| = 1 ([Den05] remark 3 p. 30) and conformality forces α = 0 ([Den05] Cor. 5.5 remark 2 p. 24); the α-twisted weight ε_γ(k)e^{kℓ(γ)} is exactly what Deninger says the new context must produce ([Den05] p. 27). Achievable on solenoids: [Den05] Thm 7.8 (weights det(−T_xφ^{kℓ}\|T_xF) for k ≤ −1) and the CM elliptic-curve example with α = 1 metric g = e^t·Re(ξη̄) ([Den05] pp. 34–35); [x-06] p. 8: α = 1 possible iff local structure (totally disconnected)×(3-ball), citing [Lei07] |
| R12 | Archimedean-term shape: χ(L)·W_L, **even in t** (H12) | Target T3 is **asymmetric** (factor e^t for t < 0). Published mismatch: the real-place fixed-point contribution in the Guillemin–Sternberg/ALKL shape gives e^{2t}/(1−e^{2t}) for t < 0, the explicit formula needs e^t/(1−e^{2t}) ([Lei13] Prop. 2.2, "a priori embarrassing", p. 17); resolution requires a **mild singularity (orbifold point)** at the real place, computed on the ramified double cover S_{Q[i]} → S_Q averaged over the Galois action ([Lei13] §4.4, Prop. 4) | **OBSTRUCTED for verbatim ALKL** (its W_L can never equal W_∞ on all of R for any κ_L — checked directly this session: κ_L = −2 matches on t > 0 and misses by e^{−t} on t < 0); TRANSFERS-WITH-WORK in the solenoid route with the orbifold local model added |
| R13 | Pole terms T4: Θ = 1 on the H²-object plus a discrete-spectrum theory of Θ on the H¹-object **in the presence of preserved leaves** | Nothing; and no such theory exists even on manifolds: ALKL (preserved leaves) prove no eigenvalue expansion of L_dis; ALKM's spectral machinery (A1)–(A4) **requires Riemannian, i.e. forbids preserved leaves** ([ALKM] Def. 1.1(4), Remark 1.2(1): transversality ⟹ no fixed leaves; [ALKL] §1.2: preserved leaves ⟹ F non-Riemannian) | **OBSTRUCTED in the published framework**: the archimedean term and the spectral expansion currently live in disjoint hypothesis classes; reconciling them is unbuilt mathematics even in the model world (→ S2/S5) |
| R14 | Length-spectrum capacity: {ℓ(c)} ⊇ {log p, all p} (infinite Q-rank by unique factorization) | X₀ **has** exactly this data [W3] — its one decisive provision | **TRANSFERS** (and forces the non-manifold setting: any closed-manifold ALKL system has orbit lengths in the finitely many finitely generated holonomy groups of the M¹-components — ÁLKL22 structure, [ALKL] §4.1.2 cases (c)–(f) with Hol L finitely generated, π₁ of a compact manifold finitely generated — hence finite Q-rank. [Derived this session — corroborated in print for the Riemannian case by [Den05] Cor. 5.5 remark 3 p. 24. Corroborative only; no verdict weight rests on it.]) |
| R15 | Counting measure: each (p, k) contributes once, sign +1 (§3, ε ≡ +1) | Uncountable packet per prime; no canonical transverse measure selecting/normalizing one orbit per packet is constructed anywhere in [x-03]; sign structure unstatable without linearization | **OBSTRUCTED** (direct); in a solenoid route this becomes a design constraint (ε ≡ +1 achieved in the [Den05] §7.7 examples) |
| R16 | (Meta) A framework in which "the appropriate interpretation of Weil's formulae" exists | ALKL's own intro places this discovery BEFORE their techniques apply ([ALKL] pp. 1–2) | — recorded as the framework authors' own assessment |

---

## 6. Structural term-shape mismatches (independent of all smoothness issues)

Even if X₀ were magically smooth, compact, and foliated, verbatim ALKL output (H12) cannot equal W(f):

1. **Negative-time weights (T2 vs H12).** ALKL: ±1. Weil: Np^k. Deninger, verbatim: "An equally important difference between formulas (5) and (24) is between the coefficients of δ_{kl(γ)} and of δ_{k log Np} for k ≤ −1. In the first case it is ±1 whereas in the second it is Np^k" ([Den05] p. 27). The mechanism: the trace formula sees the leafwise return Jacobian, which is ≡ 1 in the manifold/Riemannian world ([Den05] p. 30) but must be e^{ℓ(γ)} = Np arithmetically. This is not a normalization artifact: symmetrizing the test function moves the asymmetry, never removes it.
2. **Archimedean asymmetry + orbifold structure (T3 vs H12).** ALKL's W_L is even in t; W_∞ is not; and the real place needs the S_Q-orbifold/double-cover mechanism ([Lei13] §4.4). So the archimedean local model is **not** a smooth preserved leaf — one more reason the target space is not a manifold, published since 2013.
3. **Pole terms (T4).** Φ(1) requires Θ = 1 on the top leafwise cohomology, i.e. the α = 1 volume scaling — the same non-manifold requirement again ([Den05] pp. 26–27; [x-06] p. 8: "One can show that the conformal factor e^{αt} … necessarily has to be 1, i.e. α = 0 … the class of smooth compact manifolds is too restrictive to actually rewrite the explicit formulas of analytic number theory as a transversal index theorem").

These three are the precise, source-tagged content of the C3 brief's "[Deninger in print:] the phase space 'cannot be a manifold'" — now verified against the sources rather than the scout's recall. (The scout's other quote, "such a metric will not exist for dynamical systems relevant to number fields" [Den05] p. 19, refers to the conformal TOY mechanism and belongs to clause (ii)'s territory; it is NOT used here.)

## 7. The Deninger–Singhof leak into clause (i) — checked, and it does leak

[DS01] = Deninger–Singhof, *A counterexample to smooth leafwise Hodge decomposition for general foliations **and to a type of dynamical trace formulas***, Ann. Inst. Fourier 51 (2001) 209–219 (title and citation verified from [ALKL] bibliography p. 162). The C3 brief filed Deninger–Singhof under clause (ii) (Hodge). **The counterexample's second half is a clause-(i) fact:** it kills the naive trace formula on the single leafwise reduced cohomology H̄•(F) for non-Riemannian foliations — ALKL, verbatim: "H̄•(F) is not appropriate in general [DS01]" ([ALKL] p. 1) — and preserved leaves force non-Riemannian ([ALKL] §1.3.1 p. 2). Consequence for any transplant: the cohomological side MUST be the conormal/dual-conormal pair (H9), whose very definition consumes the smooth submanifold M⁰. On X₀ there is no M⁰ (W5) and no distribution theory (W8): **the only trace-formula design that survives DS01 is exactly the one X₀ cannot express.** (Positivity/Hodge-decomposition content of DS01 remains quarantined; nothing here uses it.)

**Adjacent warning row (logged, not an obstruction to (i)):** Deninger's real-coefficients no-go [x-04] leaks a WARNING into (i-b): leafwise cohomologies "always have natural real structures", while a Weil-type cohomology for Spec o_K "cannot have a functorial real structure"; "We are missing a fundamental 'twist' excluding real structures on cohomology somewhere" ([x-06] p. 8, citing [Den22b] = x-04). A transplanted (i-b) whose H¹-object had all the expected functoriality would collide with x-04; any future success must locate the twist. Not counted as an obstruction row because a bare trace formula is not yet a Weil cohomology (Meyer/Z3 discipline), but it must be re-checked at any (i-b) milestone.

---

## 8. Route sketches

### Route 1 — Direct transplant to X₀ = X(Spec Z). **DEAD.**
Hits OBSTRUCTED rows R1, R2, R4, R5, R6, R7, R8, R9, R15 (and R11–R13 independently). Every analytic ingredient of ALKL (H6–H9) lacks a counterpart, the archimedean datum is absent, and the orbit count is wrong by an uncountable factor. No repair short of replacing the space itself addresses R4/R5/R6. **This route is exhausted.**

### Route 2 — The solenoid/foliated-space intermediate. **The only live route. No OBSTRUCTED row; one open EXISTENCE step.**
Chain (each step named with status):
- **S1. Trace formula on smooth solenoids, no fixed leaves, α-twisted weights: EXISTS.** [Den05] Thm 7.8 (suspensions M̄×_Λ R of profinite covering towers; weights det(−T_xφ^{kℓ}|T_xF) for k ≤ −1 — the correct T2 shape; χ_Co(F,μ)·δ₀ term; proof attributed to [Lei07] = E. Leichtnam, *Scaling group flow and Lefschetz trace formula for laminated spaces with p-adic transversal*, Bull. Sci. Math. 131 (2007), per [x-06] bibliography), plus the CM-elliptic-curve example where the RHS **equals the explicit-formula RHS for ζ_E** with an honest α = 1 metric ([Den05] pp. 35–36). Status: **TRANSFERS** (published theorems).
- **S2. Add preserved leaves / fixed points to the foliated-space setting — i.e. transplant ALKL's conormal + b-calculus machinery from manifolds to foliated spaces with totally disconnected transversal factor: TRANSFERS-WITH-WORK.** The work, named: (a) conormal and dual-conormal leafwise currents at a solenoidal "leaf at infinity" (leafwise the theory is classical — leaves are manifolds; the new content is uniformity/continuity in a totally disconnected transversal parameter, the regime of Moore–Schochet tangential analysis); (b) a b-calculus for the leafwise cut with transversal parameter, b-trace included; (c) bounded-geometry leafwise heat estimates (the ÁLK bounded-geometry theory is already leafwise); (d) the ÁLKL22-type structure theory for foliated flows on such spaces. Nothing in (a)–(d) is ill-posed; it is a substantial memoir-scale analysis project with no known obstruction. Note honestly: [Den05] remark 6 (p. 33): "even the simpler conjecture 5.1 has not yet been verified in the presence of fixed points!" — written pre-ALKL; ALKL now covers the manifold case, and S2 is its foliated-space extension. As of the §1 online checks, **nobody has done or announced S2**.
- **S3. Archimedean local model — the orbifold/ramified-double-cover structure at real places: TRANSFERS-WITH-WORK** (finite-group-quotient refinement of S2; the formal computation matching W_∞ exactly is already in [Lei13] §4.4 Prop. 4; making it rigorous rides on S2's machinery).
- **S4. EXISTENCE of the arithmetic object: a compact foliated space / Riemann-surface lamination Y₀ (dim 3 in the lamination sense), with (per §3): one simple closed orbit of length log p per prime with ε ≡ +1, the S3 fixed-point data at the archimedean place, α = 1 leafwise conformal structure, and a transverse measure making the counting exact. STATUS: UNKNOWN — an open existence problem, not a work item.** What is known cuts against the two natural candidates: the constructed X₀ is not such a space (W1, W4, W5, W6), its periodic-orbit closure is still infinite-dimensional (W7), the right global "smallness" condition is not known even at the level of admissible classes (W9, E "does not look natural"), and the conjectural compactification over-supplies fixed points (W5). Deninger poses exactly this as a question ([x-03] p. 40) and has since moved to foundations ([2508.05329]). This step is **the substrate problem of C3 in Deninger-leg clothing**.
- **S5. Derive W(f) on the S4 object and identify the spectral side ((i-b)): TRANSFERS-WITH-WORK once S2–S4 exist** — requires additionally the Θ-spectral theory in the presence of preserved leaves (R13), which is unbuilt even in the model world; plus the [x-04] twist check (§7 warning row).

**Chain verdict:** S1 ✓ published; S2, S3, S5 well-posed hard analysis (instrument-grade, arithmetic-free, publishable independently); S4 open existence. **The chain is unobstructed but incomplete at S4; it cannot be certified feasible.**

### Route 3 — A new trace theory directly on X₀'s sheaf cohomology (bypass analysis). **NOT WELL-POSED.**
Would need: a supertrace theory on H•(X₀, R_X) (only H⁰ computed; nothing beyond degree 0 exists, W8); DS01 (§7) already rules out the naive single-cohomology design that this route would naturally attempt, and the DS01-compliant design needs the missing M⁰. No literature exists (§1 checks). Graded UNKNOWN-not-well-posed: no decidable next question can currently be written down that is not secretly S2+S4.

---

## 9. What a future session can decide (the UNKNOWN rows, made concrete)

1. **[Kill direction, cheap]** Formalize the closed-manifold no-go (R14 + §6): *no closed-manifold system in ALKL's hypothesis class has orbit-length data of infinite Q-rank, and no such system reproduces T2/T3/T4 shapes.* All ingredients are cited above; a short note makes the "the transplant target cannot be a manifold" folklore into a theorem with the ÁLKL22 structure theory as input. Publishable as a boundary-marker; zero risk.
2. **[Instrument direction, well-posed]** S2 feasibility note: specify the conormal-at-a-solenoidal-leaf function spaces and check the two exact sequences (1.3.1)/(1.3.2) survive the totally-disconnected transversal parameter. First genuine mathematical test of the transplant; failure here would convert Route 2's S2 to OBSTRUCTED and (with §8's route exhaustion) fire the kill-criterion.
   **[EXECUTED 2026-08-26, Session 8 → `results/c3-r/s2-feasibility-note.md`. Verdict: TRANSFERS-WITH-WORK — no obstruction; the sequences' exactness proofs ([ÁLKL23] Cor. 7.30 / Prop. 6.42+Claim 6.43 / Prop. 8.8, all read at proof level) consume only partial extension maps (1-dimensional in the defining-function variable, transversal passive), acyclicity via symbol-seminorm topology-coincidence (pointwise in the transversal — the note's single named residual-risk item W3), and category-level [Wen03] machinery; Montel/reflexivity FAIL over C(T) but are provably not consumed by the sequences. Kill-criterion does NOT fire; S4 remains Route 2's unique blocker. Sources re-fetched to `fetched-r3/` as r3s-17…r3s-21 (ALKL memoir, ÁLKL23, ALKM, Lei13, and Lei07 = arXiv:math/0603576v2 — the published precedent whose function spaces are exactly the Moore–Schochet uniformity design).]**
3. **[Kill direction, hard]** Attack S4 negatively: prove that no compact 3-dim lamination mapping to X₀ (or to X̌₀(S¹)×_{Q>0}R_{>0}) can carry one orbit per packet. Candidate mechanism to probe: the packet fibration over Ẑ×_{(p)}/p^Ẑ (W4) is Galois-monodromy-forced ([r3s-08]'s lk_p is exactly this monodromy) — if every subsystem inheriting the orbit of one prime must inherit its whole packet closure, S4 dies and with it Route 2. This is the sharpest decidable question the ledger isolates. (Cheap kills were checked and FAIL: solenoids can have infinite-rank period groups — the adelic solenoid does — so no rank obstruction; ν(x) ~ e^x/x growth is admissible under ALKM (A2).)
4. **[Positive direction, speculative]** S4 positively via W9: transplant the local Y⋄/Fargues–Fontaine "mod-p additivity" selection principle to the global setting to replace the unnatural condition E. Deninger flags this as the known-unknown ([x-06] §4). Any progress here is progress on C3's substrate problem generally.
5. **[Watch]** ALKL group / Kim–Morishita for a foliated-space sequel (none announced as of 2026-08-26, §1); Deninger's 2508.05329 line for new structure on W_rat.

## 10. Bookkeeping for C3-r

- **Kill-criterion status:** M2c is NOT failed (Route 2 unexhausted). The C3 conversion clause ("if M2 fails on all three sub-routes while M0 stands") does not fire from this leg today. M2a remains watch-only; M2b is struck (adjudicated).
- **This ledger may NOT be cited for:** (1) any positivity/Hodge/clause-(ii) claim (Z2); (2) any claim that a trace formula, if obtained, is RH progress (Meyer/Z3: spectral realization alone is RH-empty; the Connes-1999 caveat also stands); (3) the R14 derived remark as a load-bearing theorem (it is corroborative until item 9.1 is written); (4) any claim that S2–S3–S5 success would by itself yield W(f) — without S4 there is no arithmetic object to evaluate on.
- **What this ledger banks:** the complete requirement-vs-provision map with sources; the three published shape obstructions (§6) assembled in one place; the DS01 clause-(i) leak (§7) — a correction to the C3 brief's filing of Deninger–Singhof under (ii) only; the identification of S4 as the unique blocker and of 9.2/9.3 as its decidable probes; the verified negative prior-art scan (§1).
- **Z1 discipline note (DH check):** nothing in this ledger constructs an object claimed as progress, so no DH-differentiating axiom is owed by this document. Any future S2-note must state which of its axioms fails for a DH-type length spectrum (expected answer: none — a trace formula is arithmetic-blind, which is exactly why clause (i) carries no S1 credit; this is already priced by the commission).

## 11. Citation table (exact locations for every load-bearing claim)

| Claim | Source, location |
|---|---|
| ALKL hypothesis package H1–H12 | [ALKL] abstract p. v; §1.3.1 pp. 2–4; §1.3.2–1.3.6 pp. 4–8; §4.1 pp. 99–101 |
| Trace formula Thm 1.3.10; W_L formula; ε_c(k) ∈ {±1}; b-trace anomaly and (η,g)-choices | [ALKL] pp. 6–7 (Thms 1.3.8–1.3.10) |
| "No reasonable definition … with a single leafwise reduced cohomology" | [ALKL] §1.3.6 p. 7 |
| ALKL arithmetic caveat ("once the appropriate framework … will have been discovered") | [ALKL] §1.1 pp. 1–2 |
| DS01 full title (Hodge AND trace-formula counterexample) | [ALKL] bibliography p. 162 |
| Weil formula, Deninger normalization, Np^k and e^t asymmetries | [Den05] Prop. 3.2 (4), pp. 9–10 |
| α = 0 forced on manifolds; finitely generated length group; fixed points needed for infinite generation | [Den05] Cor. 5.5 remarks 2–3, p. 24 |
| ±1 vs Np^k weights as the k ≤ −1 discrepancy; α-twisted target shape | [Den05] pp. 26–27 |
| \|det(T_xφ^{kℓ}\|T_xF)\| = 1 in the manifold setting; = e^{kℓ} wanted | [Den05] remarks 3–4, pp. 30–31 |
| Solenoid trace formula with correct k ≤ −1 weights; CM curve example, α = 1 metric | [Den05] §7.7 Thm 7.8 + example, pp. 34–36; proof ref. [31] = Leichtnam (→ [Lei07], Bull. Sci. Math. 131 (2007), via [x-06] bibliography) |
| Conjecture 5.1 unverified with fixed points (pre-ALKL) | [Den05] p. 21 and remark 6 p. 33 |
| S_K axioms 1]–8]; real-place mismatch Prop. 2.2; orbifold resolution | [Lei13] §4.1 pp. 15–16; §4.2 pp. 16–17; §4.4 pp. 19–20 |
| X₀ construction, suspension form, condition E unnatural | [x-03] intro pp. 2, 5; [x-06] §4 p. 11 |
| No fixed points; packets over Ẑ×_{(p)}/p^Ẑ; invariant-tori remark | [x-03] intro p. 2; §5 (39)–(40) p. 32; Thm 6.1 pp. 38–39; [x-06] Thm 4.2 |
| Arakelov compactification prediction + too-many-fixed-points caveat + Y₀ lamination question | [x-03] §6 pp. 39–40 |
| Topology: Tychonov, metrizable, Hausdorff (affine/ample), Thm 7.10 bijections not homeomorphisms | [x-03] §7 pp. 40–47 |
| Closure of periodic orbits still infinite-dimensional | [x-03] §8 Thm 8.2 pp. 49–50 |
| Leaf partition not locally trivial ("not an actual foliation") | [x-03] §10 p. 63 |
| H⁰_F(X₀) = R | [x-03] Thm 10.2 pp. 63–64 |
| Local Y⋄ / Fargues–Fontaine; global modification unknown | [x-03] §§13–15, Thm 15.6; [x-06] §4 p. 11 |
| "Smooth compact manifolds too restrictive"; α = 1 iff (totally disconnected)×(3-ball); real-structure twist missing | [x-06] p. 8 |
| ALKM hypothesis package (Riemannian ⟹ no preserved leaves; (A1)–(A4)) | [ALKM] Introduction pp. 3–5; Def. 1.1, Remark 1.2, Def. 1.4 |
| Morishita bridge: continuous, Galois-equivariant, flow-anti-equivariant, orbits correspond; no analytic structure | [r3s-08] abstract + introduction |
| Online negative prior-art scan | §1 of this document (4 WebSearch queries, 2026-08-26) |

---

## 12. DATED ADDENDUM — Session 8, 2026-08-26: adjudicated disposition of §9.2 and §9.3 (append-only; binding record in `results/c3-r/probe-9.3-adjudication.md`)

Inputs: `probe-9.3-a.md`, `probe-9.3-b.md` (two independent §9.3 probes), `s2-feasibility-note.md` (§9.2), all Session 8. Adjudicated by an independent agent with re-derivation of the shared core and of the one inter-probe disagreement from the primary sources on disk ([x-03] §§4–8, [r3s-08] §§1.2/2.2, [ALKL]/[ÁLKL23] cited passages — all read verbatim this session).

**§9.2 (S2 feasibility) — EXECUTED, adjudicated: TRANSFERS-WITH-WORK, accepted.** The sequences (1.3.1)/(1.3.2) survive the totally disconnected transversal at feasibility-note grade; pivotal citations spot-verified on disk (ALKL pp. 4–5 verbatim; Prop. 2.5.1 with proof; ÁLKL23 Prop. 6.42 + Claim 6.43). Single residual-risk item: W3 of the note (C(T)-valued topology-coincidence/acyclicity). No obstruction; Route 2's blocker remains S4.

**§9.3 (S4 kill-probe) — EXECUTED twice independently, adjudicated: UNDECIDED-WITH-PROGRESS, with three sub-parts DECIDED:**

1. **Packet-closure law (new Theorem A; three independent derivations — both probes + adjudicator; referee-grade).** In X₀ = X(Spec Z), any admissible E: the closure of any single periodic orbit contains its entire packet Γ^E_(p); packets are minimal sets. The §9.3 candidate mechanism's CONCLUSION is proved; its SKETCH (fiber-flow minimality / fibration monodromy) is refuted — the flow fixes the packet base (the fibers ARE the orbits, [x-03] §6; [r3s-08] Thm 2.2.9(2)); the true mechanism is profinite accumulation of Frobenius return exponents, forcing group = coker(lk_p) = the closure of the Frobenius-monoid twists ([x-03] (34)–(39) + CRT).
2. **Closed-subsystem half of S4 is DEAD** (per [x-03] p. 40's first alternative read with Y₀ closed): every closed flow-invariant subset of X₀ meeting every packet contains all packets (uncountable per-prime multiplicity — T1 coefficient-1 and ALKL H4 unsatisfiable) and contains the infinite-dimensional Y₀ = X̌₀(S¹)×_{Q>0}R>0 ([x-03] Thm 8.2, unconditional for Spec Z via [Per11]). Upgrades rows R4/R6/W4/W7 from evidence to theorem for the closed reading.
3. **NEW ROW W12: X₀ is NON-HAUSDORFF along its packets** (probe B Cor. A.2, adjudicator-re-derived: one Theorem-A sequence has two distinct limits — a rotation limit on the orbit and a twist limit off it). Scope: every E whose packet E-locus meets ≥ 2 base classes (all E ⊇ E_f; E_max; E_tors). Consequences: no periodic orbit is closed as a subset; the packet subspace topology is not (profinite)×(circle); compact invariant subsets need not be closed, so the embedded kill does NOT extend to compact-but-not-closed subspaces or to equivariant images; probe A's G1 is thereby DECIDED (NO) and its G1-conditioned clauses (cut-system ambient kill §4.3; §6.1 minimal-set forcing; the "G1-yes + G2-no" kill path) are VOID. Fourth independent negative datum for S4-positive-on-X₀ (after W6, W7, W9). Flag confirmed on W11: [r3s-08] Thms 2.2.8/2.2.9 "homeomorphism"/"closed orbits" wording is incompatible with the subspace topology — never cite it for topology.
4. **W9/R15 sharpened (probe A Theorem C, adjudicator-re-derived reachability):** the minimal admissible class of a chosen injective packet character cuts to exactly ONE orbit per prime (exponent reachability = a₀·p^Ẑ; unit parts of other primes unreachable), so one-orbit-per-prime admissible selections EXIST — but are non-canonical (an arbitrary point of the Cantor group B_p per prime, exactly [x-03]'s "does not look natural") and forfeit every theorem [x-03] certifies (connectedness, H⁰_F = R, Thm 8.2 all consume E ⊇ E_f); every certified system has irreducibly uncountable packets (Thm 5.2). A viable S4 selection must be canonical AND non-admissible — [x-03]'s own "additive mod p ... not N-invariant" remark marks the only exit → §9 item 4 (probe 9.4) is the sole positive road and is hereby sharpened.

**§9.3's question is REPLACED by the merged residue Q*** (adjudication §5): (Q-a) a compact Hausdorff-in-itself NON-closed flow-invariant 3-dimensional subspace of X₀ with one orbit per packet; (Q-b) a compact 3-dim lamination with one closed orbit of length log p per prime mapping equivariantly into X₀ with γ_p → Γ_p. Both faces reduce to a pure p → ∞ accumulation problem (orbits in compact Y accumulate on a closed invariant aperiodic set A with image in the unitary locus); the packet/monodromy mechanism is settled and exerts no further force. NO on both faces kills S4 and Route 2; YES on either retires the packet-mechanism kill and moves the burden to S3/R12–R13.

**Kill-criterion status: DOES NOT FIRE** (Session 8). Route 2 unexhausted: S2 unobstructed, S4's mapping half open. Not `failed-ledger-exhausted`.

**What remains decidable after this session:** Q* (both faces, kill or positive); probe 9.4 (canonical non-admissible selection — sharpened by Theorem C's price list as the constraint any candidate must beat); Q-c (closure equality, bookkeeping); Hausdorffness of the CUT suspensions X₀^{E(a)} (the only Hausdorff question left with S4 relevance); the W1–W7 program of the S2 note (W3 first).

---

## §13. Session-14 addendum (2026-09-02, orchestrator; status PENDING the adversarial dual-model pass — nothing below is enacted yet)

**Binding adjudications of the Session-14 probes (`results/c3-r/s14/{qstar,dqm,w3}-adjudication.md`):** Q* DECIDED-NO on both faces as a theorem (every admissible E; target X₀ and Y₀) — the kill-criterion INPUT FIRES per adjudication §5 of Session 8, single-check; DQ-M = NO (theorem in the model world; Road 2 closed; Q*'s one-orbit clause stands); W3 = PARTIAL (the literal coincidence target is refuted at source in [ÁLKL23]; the acyclicity core is proved and transplant-transparent; the S2 verdict is NOT reopened, its residual risk moves to the W1/W2 interface). Per standing orders 5 and 7 the kill is ENACTED only after an independent adversarial pass by both models on the two mechanisms (packet indiscreteness; the flow-conformal weight/dissipation argument) and the dual-model novelty sweep. The adjudicators' proposed annotation texts follow verbatim.

**[REPAIR 2026-09-03 — Session 14 repair pass]** *This section's "target X₀ and Y₀" and the Q\* addendum text reproduced below ("or into the unitary system Y₀ = X̌₀(S¹)×_{Q>0}R>0") carry the face-(b) Y₀ clause that the adversarial adjudication (`results/c3-r/s14/adversarial/adjudication.md` §7.2) ruled FALSE and STRUCK — the permitted replacement is Y₀^E := (X̌₀(S¹) ∩ X̌₀(C)_E)×_{Q>0}R>0 ⊆ X₀^E, with the E-free Y₀ an explicit counterexample. The four binding corrections (the quotient topology is [x-03] p. 59's definition; the Y₀ clause re-scoped to Y₀^E; the coarser-topology rationale inverted for face (b); "S4 is DEAD" restated as the death of the quasi-compact, fixed-point-free, two-sided-R equivariant-source construction inside X₀^E) are enacted in §14 and §15 below, which supersede the PENDING text of this section. [repair-pass wording]*

### Proposed by the Q* adjudicator

## 10. Proposed ledger / frontier annotations (text proposed, NOT applied — no existing file edited)

**For `m2c-feasibility-ledger.md` §12 (append a Session-14 dated addendum):**

> **DATED ADDENDUM — Session 14, 2026-09-02: Q\* adjudicated NO on both faces; kill-criterion input FIRES (binding record: `results/c3-r/s14/qstar-adjudication.md`).** Four independent probes (two kill, two build; both builds failed to build and proved NO) and the adjudicator's re-derivation from [x-03] establish: **(Q-a) DECIDED-NO** — every packet, indeed every single periodic orbit, is an indiscrete subspace of X₀ in the quotient topology, for every admissible E, so no T₀ (hence no Hausdorff/lamination) subspace meets a packet; **(Q-b) DECIDED-NO** — X₀ carries a positive l.s.c. flow-conformal weight of exponent one, ∞ exactly on the packets, so no quasi-compact flow-invariant set meets the generic locus and (packets clopen in the periodic locus) any such set meets finitely many packets; hence no compact equivariant source reaches infinitely many packets. Both unconditional, every admissible E, for X₀ and Y₀; lamination hypotheses unused. **S4 is DEAD for target X₀ = X(Spec Z); Route 2 breaks at S4; kill-criterion input FIRES** (single-check; dual-model sweep owed). Route 1 dead + Route 2 dead + Route 3 not-well-posed ⟹ Deninger-leg route list exhausted. **Residue (a different target, not a Route-2 survival):** the conjectural Arakelov compactification X̄₀ (p. 39–40), unbuilt; re-posed as Q-b′. **Rows:** R1 compactness → **fails** (X₀, Y₀, all cuts not quasi-compact); W1 → resolved NO; W5 (no fixed points / u→0⁺) → made quantitative by the escape weight; W12 (non-Hausdorff along packets) → subsumed and sharpened to **non-T₀ / indiscrete**, scope exception for cut classes removed; W7 → periodic-orbit closure Y₀ also not quasi-compact. **New rows:** **W13** — X₀ is dissipative (positive l.s.c. e^t-conformal weight, ∞ on packets; no quasi-compact invariant set meets the generic locus or > finitely many packets; archimedean end at infinite distance from every compact set); **W14** — packet points of unbounded characteristic converge only over the generic point. §8 Route 2 step S4: **UNKNOWN → DEAD (theorem).** §9 item 3 (replaced by Q\*): **EXECUTED-AND-DECIDED, NO.**

**For `directions/C3-geometric-substrate.md` "Current frontier" (replace the Session-8 next-rung item (2)):**

> **SESSION-14 STATE (supersedes the Session-8 paragraph on Q\*): Q\* is adjudicated NO on both faces (`results/c3-r/s14/qstar-adjudication.md`, binding); the S4 packet-mechanism kill FIRES for target X₀.** Face (a): packets are indiscrete subspaces (no Hausdorff subsystem). Face (b): X₀ is dissipative (escape weight), so no compact equivariant source reaches infinitely many packets. S4 dead for X₀; Route 2 dead at S4; with Route 1 dead and Route 3 not well-posed, the Deninger-leg route list is exhausted (single-check; dual-model sweep owed before external use). **What survives:** S3 / R12–R13 (archimedean, α = 1); Road 1 (descent enrichment [D25] — changes the space, not a map into X₀); the instrument track S1/S2/S3/S5 (S2 = TRANSFERS-WITH-WORK, residual risk W3), now without an arithmetic consumer along Route 2. **Next rungs:** (1) the standing-order-7 dual-model sweep of the eleven single-check items of the Q\* adjudication §9; (2) Q-b′ (the compactification face — targets the unbuilt X̄₀, i.e. the substrate problem re-posed; constraints in Prop. 7.4); (3) Road 1 / whether a descent enrichment yields a space with finitely many orbits per prime and a trace theory; (4) S2/W3 as an independent instrument result. The direction-level `failed-ledger-exhausted` determination for C3-r's Deninger leg is now ready to be made; this record supplies the S4 input.

---

### Proposed by the DQ-M adjudicator

## 11. Ledger / frontier annotations (PROPOSED text — this note applies nothing)

**`results/c3-r/m2c-feasibility-ledger.md`, new dated addendum §13 (append-only):**
> **§13. DATED ADDENDUM — Session 14, 2026-09-02: DQ-M (measured trace formula for orbit continua) adjudicated: NO. Road 2 CLOSED.** Inputs: `results/c3-r/s14/dqm-F.md`, `dqm-O.md` (two independent probes), adjudicated with full re-derivation in `results/c3-r/s14/dqm-adjudication.md`. **Decided:** (1) for every [Den05] §7.7 mapping torus the leafwise-cohomology trace exists with no non-degeneracy hypothesis and equals ℓ Σ_k L(h^k) δ_{kℓ} (three derivations); (2) an orbit continuum B of common length ℓ contributes ℓ·ind(return map, B)·δ_{kℓ} — an integer, never a Haar mass; explicit models give 0, 2, 2−2g against Haar's 1, including a Cantor continuum in T² (weight 0), a Cantor continuum in S² (weight 2) and a Haar-measured circle in a genuine Z_2-solenoid (weight 0); equality with one orbit holds iff the index is 1 (realized by a contractible disk plus one simple orbit); (3) a family with a transitive translation symmetry — the property that makes Haar canonical on B_p — has index 0 (Lemma 9.2 + classical index theory); (4) with the Cantor base transverse to the leaves the type I trace does not exist (1 ⊗ S never trace class; flat trace diverges); (5) the type II trace along the orbit lamination exists and returns the Haar identity but cannot carry T1/T2 on a compact substrate (finite packet mass, bounded mass per unit interval, evenness, blindness to null orbits) and is not a trace in the infinite-mass regime. **Rows:** R4 — the "Haar-measured family" repair is CLOSED (theorem); H4's content identified as the local Lefschetz index; a third repair, "index-1 family", is identified, strictly weaker, unavailable for homogeneous packets, and unstatable on X₀ (W6/W12). R11 — the measured trace is even in t: one more confirmation that the k ≤ −1 weights need the leaf-direction mechanism; correct the citation "[Den05] remark 3 p. 30" to p. 31. R15 — sharpened: no transverse measure can normalize the count on a compact substrate (Theorem N(a)); the design constraint is ind(return map, B_p) ≡ +1, sharper than per-orbit ε ≡ +1 (a continuum with ε ≡ +1 on every orbit can weigh 0 or 2). W9 — the Haar road is closed; surviving W9 repairs: descent enrichment ([D25]/[Lut25]) and per-place gluing. **New row W13 (index–measure dichotomy):** in any Deninger/ÁLK02/ALKL-type dynamical Lefschetz trace formula an orbit continuum's multiplicity is a fixed-point index (Z-valued, leafwise), never a transverse measure, and a continuum carrying a transitive translation symmetry has index 0; proved for mapping tori and for Model S, for isolated orbits in all §7.7 solenoids (Thm 7.8 counts them regardless of the Haar(Γ̄) ⊗ dt transverse measure), open for continua in general solenoids (D1). Sources: [Den05] pp. 20–22, 29–31, 34–35; [ALKL] pp. 2–3, 6, 8, 71, 99–101, 153–156; [x-22] pp. 5–6, 12–14, 18–20, 23; [Lei07] pp. 3–4, 15–17; [ALKM] p. 4; [x-18] p. 8; [x-19] p. 10. **§9 item 4 / DQ-M:** EXECUTED twice, adjudicated NO. **Kill-criterion: DOES NOT FIRE** (Q-a/Q-b undecided; S2 unaffected). **Next decidable:** D1 (solenoidal uniform law), D2 (clopen-local index form), D3 (a packet-symmetric model), D4 (Q-b in index form), D5 (adelic-solenoid inspection), D6 (Fuller index, locate-only) — see the adjudication §9.

**`results/c3-r/probe-9.4-note.md` (annotation only, not an edit):** §7 Road 2 → CLOSED by theorem (the named first obstacle is not a gap but a theorem against: the Haar count is wrong in the model world and vanishes under packet symmetry); the sentence "the packet's aggregate orbit contribution is ∫_{B_p}(single-orbit term) dHaar = the single-orbit term" is true only for the type II trace along orbits and for the product mixed trace, and false for the leafwise (Lefschetz) trace. §8 item 2 → EXECUTED, verdict NO, pointer to `dqm-adjudication.md`. §8 item 3 (DQ-L) → closed (done in the Session-14 novelty pass).

**`results/c3-r/probe-9.3-adjudication.md` §5 (annotation only):** Q\* unchanged; the conditional Road-2 re-scoping ("Haar-measured orbit family") is void; the alternative (Q\*-idx) is recorded in `dqm-adjudication.md` §8.2 as available in the model world and closed for homogeneous packets; Q-b in index form is next decidable D4.

**`directions/C3-geometric-substrate.md` "Current frontier" (proposed replacement of rung (3)):**
> **(3) DQ-M — DONE, NO** (Session 14; two independent probes F and O, adjudicated with full re-derivation in `results/c3-r/s14/dqm-adjudication.md`): the leafwise trace of a [Den05] §7.7 suspension exists without non-degeneracy and assigns an orbit continuum its fixed-point index, not its Haar mass (0 for every homogeneous compact-group family exhibited; 0 for any family with a transitive translation symmetry); Road 2 of the 9.4 note is CLOSED; Q\*'s one-orbit clause stands; the licensed re-scoping is "index one per packet", non-vacuous in the model world, closed for homogeneous packets, unstatable on X₀. Surviving W9 repairs: Road 1 (descent enrichment, [D25]) and Road 3 (per-place gluing). **Next rungs, in order:** (1) the Session-8 referee debts as before; (2) Q\* — either face (unchanged), with the index-form sharpening D4 available; (3) the cheap DQ-M follow-ups D5 (adelic-solenoid inspection) and D2 (clopen-local index form), then D1 (the solenoidal uniform law — the last model-world door on the measured reading); (4) S2 work program W3 first. Kill-criterion: not fired. Blocking: nothing.

---

### Proposed by the W3 adjudicator

## 10. Ledger / frontier annotations (PROPOSED text; nothing applied)

**10.1 For `results/c3-r/m2c-feasibility-ledger.md`, §12 dated addendum (append-only), proposed paragraph:**

> **§9.2 / S2, work item W3 — EXECUTED (Session 14, two independent probes `results/c3-r/s14/w3-F.md`, `w3-O.md`; binding adjudication `results/c3-r/s14/w3-adjudication.md`): PARTIAL, with the S2 verdict TRANSFERS-WITH-WORK NOT reopened.** (a) The topology-coincidence statements W3 was to transplant ([ÁLKL23] Prop. 3.2, Cor. 3.4 both assertions, Cor. 4.5, Prop. 6.10/Cor. 6.12, Cor. 6.19, Cor. 7.11; Cor. 3.6 and [ALKL] §2.1.8 for non-compact bases) are FALSE at source (arXiv v1 and v3), by explicit counterexamples re-derived three times; Cor. 6.24/7.20 are true but unproved there. (b) What acyclicity actually needs — Wengenroth's criterion on a 0-neighborhood of the m-step — is PROVED for the compactly based symbol and b-collar spectra by a Landau–Kolmogorov-type interpolation (two independent proofs), and is a formal invariant of sup-seminorm parametrization over any compact Hausdorff T, in both directions: the transplanted spectrum is acyclic iff the manifold-level one is. Total disconnectedness is never used; compactness of T is essential. (c) The manifold-level package the program consumes is re-secured with valid proofs (acyclicity/retractivities of I, A, Ȧ, K, J; Claim 6.43 and its J-analog in Prop. 8.8 from bounded retractivity + partial extension maps alone; density Cor. 3.5; Fréchet-ness of I^m from Prop. 4.3): [ALKL]'s (1.3.1)/(1.3.2) and Thms 1.3.3/1.3.6 are undamaged. (d) For the S2 note's I_τ, J_τ, Ȧ_τ, K_τ the result is conditional on the W1/W2 definitional interface (fixed-compact-support (4.10)_τ; global gluing of the chart identification I^{(s)}_τ = C(T; I^{(s)}); parametrized (4.12)/(6.38); parametrized E_m). **Residual risk of S2 clause (i) relocated:** from W3 to (i) that interface (definitional, not an acyclicity question) and (ii) a source-integrity row: every program citation of a coincidence, density, non-compact-base acyclicity, or topological-lifting statement from [ALKL]/[ÁLKL23] must route through the adjudication's §3–§5. Kill-criterion: does not fire. S4 (Q\*) remains Route 2's unique blocker. Next S2 rung: D1/D2 of the adjudication §8 (the interface as two lemmas). Publication check D4 open (journal text not consulted; no erratum found).

**10.2 For `directions/C3-geometric-substrate.md`, "Current frontier", proposed replacement of rung (4):**

> **(4) S2 work program — W3 DONE (Session 14, PARTIAL, adjudicated; `results/c3-r/s14/w3-adjudication.md`).** The acyclicity lemma is proved in corrected form: the source's whole-step coincidence statements are false ([ÁLKL23] Prop. 3.2, Cors. 3.4/4.5/6.12/6.19/7.11 — a defect found independently by both probes and re-derived), the 0-neighborhood criterion holds by interpolation and is transparent to the compact transversal (acyclic iff the manifold-level spectrum is; total disconnectedness irrelevant), and the manifold-level package [ALKL] consumes is re-secured. S2 stays TRANSFERS-WITH-WORK; its residual risk is now the W1/W2 definitional interface (adjudication §8 D1–D2, routine-to-moderate, arithmetic-free) plus a standing source-integrity flag on [ALKL]/[ÁLKL23] citations. **Next S2 rung: D1 (global chart identification I^{(s)}_τ = C(T; I^{(s)}), W1) and D2 (parametrized partial extension maps, W1).** Rungs (1)–(3) (referee debts, Q\*, DQ-M) unaffected; nothing here bears on S4.

**10.3 For `results/c3-r/s2-feasibility-note.md` (annotations only, not edits):** §2.2 (A6) → "(M\*) on the 0-neighborhood {N_m(·; 0) < 1}", not whole-step coincidence; §2.2 "exactness engine" and §4 row I-9 → Claim 6.43 uses TWO inputs (input (iii) deleted); §4 row I-8 → mechanism sentence struck and replaced (10.1(b)); §4 row I-10 → item (c) delivered, Montel loss now a theorem; §5 W3 → status per 10.1; §7 item (4) → W3 no longer "unproven", PARTIAL as stated; §8 citation rows for Cor. 4.5 and Prop. 6.42/Claim 6.43 → "false as stated / repaired — see s14/w3-adjudication.md §3, §4.6".

**10.4 For `results/c3-r/probe-9.3-adjudication.md` (annotation only):** §1 row 3 and §6 — "W3 … the single residual-risk item — its failure would reopen the verdict": W3 pressed (Session 14); it did not fail; residual risk relocated per 10.1; §6's description of Claim 6.43's inputs is now a theorem. Q\* untouched.

---

---

## §14. Session-14 ENACTMENT (2026-09-03, 03:40 IST, orchestrator) — Route 2 as specified: FAILED, kill-criterion FIRED (adversarially checked by both models)

**Basis.** `results/c3-r/s14/qstar-adjudication.md` (Fable) + the adversarial pass `results/c3-r/s14/adversarial/` (two refuters per face, Opus 5 + Fable 5.1; Opus adjudicator re-deriving both mechanisms from [x-03]): face (a) STANDS, face (b) STANDS-NARROWED, kill-criterion FIRES for the S4 target X₀^E. Four corrections are binding on every record of the result: (1) the quotient topology on the suspension is a printed DEFINITION, [x-03] p. 59 (§9), not a "reading of record" — the adjudication §2/§11, qa-kill §9.4(i), qa-build §2.3/§10.2 are wrong on this point, in the theorem's favor; (2) the clause "or into the unitary system Y₀ = X̌₀(S¹) ×_{Q>0} R>0" is FALSE and is STRUCK wherever it appears (verdict table, §4(D), §13 above, C3 frontier, novelty items 3/6/9/10): [x-03] p. 49 defines X̊(S¹) by unitarity alone, without (Tors), and the orbit Ω of the trivial generic character (isotropy all of Q>0, indiscrete) makes K = Ω ∪ ⋃_p γ_p a nonempty quasi-compact R-invariant subset of Y₀ meeting EVERY packet in exactly one orbit; refuter F strengthens the source to a compact metrizable 3-dimensional lamination (torus + cabled solid tori) — load-bearing steps checked by the Opus adjudicator, NOT yet dual-model-verified as a construction; (3) "a coarser topology preserves face (b)" is inverted — face (b) needs p. 59's topology or finer; (4) "S4 is DEAD" is restated: what is proved dead is the quasi-compact, fixed-point-free, two-sided-R-equivariant source construction inside X₀^E (any admissible E, (Tors) in force) and the subspace face; [x-03] p. 40's question imposes no compactness and X₀ receives no archimedean fixed points at all (p. 3), so Q-b was never S4's faithful shape.

**Status lines.** Route 2 (solenoid intermediate) with target X₀^E: **FAILED — `failed-ledger-exhausted`** (Route 1 exhausted §8; S4-into-X₀^E dead at theorem grade; the (Tors)-kill is the right target per [x-06] p. 11: the E-free system "has too many periodic orbits" and (Tors) is "known for certain"). Kill-criterion: FIRED for this specification.

**Residue — TWO escapes, one of them not unbuilt.** (R-i) The unbuilt Arakelov compactification X̄₀ with fixed points at u → 0⁺ (W5). (R-ii) **Deninger's own printed E-free unitary system Y₀** (relax (Tors) at the generic point): a compact-source equivariant map with one closed orbit of length log p per prime EXISTS there (refuter F's witness), the trivial-character orbit Ω absorbing the p → ∞ accumulation — the exact role S4 wanted an archimedean fixed set to play. Whether that source lamination carries a trace formula with the T1 orbital side, and what Ω's contribution is, is the next decidable question (Q-b″). This is the first positive S4-shaped object in the program's record and is treated as a LEAD, not a result, until dual-model-verified.

**[REPAIR 2026-09-03 — Session 14 repair pass]** *Corrections to §14, binding (`results/c3-r/s14/y0-witness/adjudication.md` §0.1, §4.1, §5; already enacted in §15 below — this block records the strike at the point it applies). (1) "lamination" is STRUCK for the witness Y: "a compact metrizable 3-dimensional lamination (torus + cabled solid tori)" in the Basis paragraph and "that source lamination" in the Residue paragraph read "a compact metrizable 3-dimensional space with a flow (a 2-torus with an irrational flow plus one cabled solid torus per prime)"; Y admits NO foliated-space structure with 2-dimensional leaves (y0-witness adjudication §4.1, Theorem B, proved and sharpened by leaf dimension: d = 3 and d = 0 excluded outright, d = 2 excluded by verify-F's proof, d = 1 exists but is trace-formula-empty). (2) "This is the first positive S4-shaped object in the program's record" is STRUCK and reads "a compact source realizing the orbit spectrum {log p} with an inert comparison map" (§15). (3) The construction needed four repairs D1–D4 (recorded as a dated block in `s14/adversarial/face-b-refuter-F.md` §3.4). [repair-pass wording; the replacement phrases are §15's.]*

## §15. Session-14, 04:25 IST — Q-b″ stage 1 DECIDED (`results/c3-r/s14/y0-witness/`, two verifiers on two models + Opus adjudicator): the Y₀ witness is a real construction but NOT an S4 object; the target Y₀ is inert and is itself not a lamination

**Corrections to §14, binding:** strike "lamination" for the witness Y (it is a compact metrizable 3-dimensional space with a flow — a 2-torus with an irrational flow plus one cabled solid torus per prime — and it admits NO foliated-space structure with 2-dimensional leaves: proved, ratified, sharpened by leaf dimension); replace "first positive S4-shaped object" by "a compact source realizing the orbit spectrum {log p} with an inert comparison map"; rewrite residue (R-ii) as below. The construction needed four repairs (Lipschitz tube field — a legal reading of the original admits non-unique backward solutions, so no R-action; an explicit rank-2 normal frame in the 4-dimensional ambient; radii O(p⁻²); the E-free proof of packet indiscreteness), all supplied.

**Theorem T (adjudicator, single-check):** for ANY Q>0-space Z and any z with relatively compact orbit, the Q>0-orbit of (z, u) in Z × R>0 is not closed, so the suspension Z ×_{Q>0} R>0 is not T₁. Hence Y₀ is not T₁, not metrizable, not a foliated space; no Q>0-suspension of a compact base can be the S4 object. Deninger's own §8 presents Y₀ as a negative result ([x-03] p. 49). **Theorem C (verifier F, ratified):** any compact source with a continuous equivariant map into the E-free Y₀ hitting infinitely many packets decomposes as Y_η ⊔ ⨆_p Y_p with Y_p clopen and Y_η mapping into the (Tors)-violating generic locus, and conversely any such decomposition admits such a map — continuity is automatic; the map pulls back no leafwise, transverse or cohomological structure. The E-free target is INERT.

**What the witness DOES establish (the positive residue, confirmed at source):** on each solid-torus piece, with a REPELLING core of rate ½ the leafwise return derivative is the homothety p^{1/2}·(orthogonal), the closed orbit is simple with ε ≡ +1, and |det A_p^k| = p^k — a [Den05] §7.5-type formula on such a piece returns T1 + T2 EXACTLY, which is [Den05] p. 33's printed prescription "absolute value Np^{1/2}". So the orbit-spectrum-and-weights half of S4 is cheaply realizable; the unmet half is entirely topological: (a) a foliated (Riemann-surface-leaved) structure that survives at the accumulation set, and (b) an archimedean leaf with χ ≠ 0 in that accumulation set (the limit torus has χ = 0; there are no fixed points). Any target from Deninger's construction plays no role.

**Residue, rewritten (R-ii → S4′).** The Deninger leg is EXHAUSTED for the substrate: X₀^E is killed (§14), Y₀ is inert and not a lamination (§15), X̄₀ is unbuilt (R-i, W5). What remains of S4 is a standalone existence problem in foliation dynamics, **S4′: a compact foliated 3-space (Riemann-surface leaves) with a foliated flow whose closed orbits are exactly one simple orbit of length log p per prime with return derivative p^{1/2}·O, whose accumulation set contains a preserved leaf of nonzero Euler characteristic, carrying a transverse measure** — and, separately, the S1 requirement that Euler-product arithmetic enter through the object's own structure (the substrate's raison d'être), since no comparison map to X₀ or Y₀ supplies it. Next decidable question: is the length spectrum {log p} (once each, simple, with prescribed derivative) REALIZABLE by such an object at all — the inverse length-spectrum problem for foliated flows with an archimedean leaf (Q-S4′).

**[NOVELTY — dual-model check 2026-09-03]** **§15's Theorem T, Theorem C and S4′, after the dual-model sweep** (`results/c3-r/s14/novelty/adjudication.md`, binding). **Theorem T (C2): PARTIAL** — "T₁ ⟺ orbits closed" is printed (Yokoyama arXiv:2012.00849 Lemma 7.2; Akin–Auslander arXiv:1004.0323 Thm 6.3) and Deninger prints the opposite answer for the adelic base ([x-03] p. 64 Remark, via Laca–Raeburn Math. Ann. 318 (2000) Lemma 3.1 "If u is an invertible adele, then the orbit ℚ*u is closed in 𝔸"); the compact-base statement and "Y₀ is not T₁/metrizable/foliated" are new. **Theorem C and the cabled source: NOVEL-DUAL-CHECKED**; surgery shape = Kim–Morishita–Noda–Terashima, Münster J. Math. 14 (2021) = arXiv:1906.02424 Lemma 3.2 (credit); the return derivative p^{1/2}·O is Deninger's prescription ([Den05] pp. 32–33). **S4′ (C10): ANTICIPATED as a posed problem** — it is Deninger's own desideratum, [x-21] 2002 = [Den05] p. 26: "it would be very desirable to find a system (X, φ^t, F) which actually realizes this correspondence. For this the class of compact 3-manifolds as phase spaces has to be generalized"; re-posed as the sub-system question at [x-03] p. 40; stated as open by Leichtnam, Bull. Sci. Math. 131 (2007) = arXiv:math/0603576, abstract "Precise conjectures were stated in our report [Lei03] on Deninger's work. The existence of such a foliated space and flow φ^t is still unknown except when Y is an elliptic curve (see Deninger [De02])", p. 2 "the existence of such a quadruple (S_ℚ, F, g, φ^t) is still unknown", and Open Question 2 (function-field form, "log Nw = l(γ_w)"); the solved case is [De02] = [x-22] (ordinary elliptic curve over 𝔽_p, [Den05] §7.7 Example). The physics posing is Berry–Keating, SIAM Rev. 41 (1999) ("periodic orbits whose periods are multiples of logarithms of prime numbers"). **PARTIAL** for the four sharpened clauses and the inverse-spectrum framing — not found posed or studied anywhere [CORRECTED 2026-09-05, §16 S16-1: clauses (i), (ii), (iv) are ANTICIPATED in Leichtnam 2008 §5.1 / 2013 §4.1 (r3s-20); only (iii)'s χ ≠ 0 and accumulation-set clauses and the inverse-spectrum framing are the program's own] (dynamics literature: only rank-one/common-period inverse results; Sullivan solenoids and Smale–Williams attractors have lattice-like spectra; Kucharczyk–Scholze's X_F carries no flow). The printed structural constraint must be cited: Deninger [x-18], *Groups and Analysis*, LMS LNS 354 (2008), p. 3 — "It is known that F is a fibration if and only if rank Λ = 1 … If one wants an infinitely generated Λ, one must allow the flow to have fixed points (≙ infinite places)". The printed axiom list, E. Leichtnam, *An invitation to Deninger's work on arithmetic zeta functions*, Contemp. Math. 387 (2005) 201–236, is UNDETERMINED (SPONSOR-FETCH) and may already contain clauses of S4′. **Required wording:** "What remains of S4 is a standalone existence problem" → "What remains of S4 is Deninger's and Leichtnam's published open existence problem, sharpened here to S4′ by four clauses".

**[REPAIR 2026-09-03 — Session 14 repair pass]** **S4′ is Deninger's printed desideratum (2002/2005) and Leichtnam's Open Question 2 (2007), re-scoped.** *(`results/c3-r/s14/novelty/adjudication.md` §0 C10, §2 C10, §3 R3 — MAJOR.) §15 must present S4′ as the published open problem, sharpened, with the solved case named. In print: Deninger, [x-21] 2002 = [x-20] (Den05) p. 26, "In order to understand number theory more deeply in geometric terms it would be very desirable to find a system (X, φ^t, F) which actually realizes this correspondence. For this the class of compact 3-manifolds as phase spaces has to be generalized as will become clear from the following discussion."; [x-03] p. 40, "Is there a sub-dynamical system Y₀ ⊂ X₀ = X̌₀(ℂ) ×_{ℚ^{>0}} ℝ^{>0} or at least one which maps to X₀ such that dim Y₀ = 2d + 1 … and such that Y₀ contains at least one periodic orbit in Γ_{x₀} for every closed point x₀ of X₀? If d = 1, is there such a Y₀ which is a Riemann surface lamination …?"; Leichtnam, Bull. Sci. Math. 131 (2007) 638–669 = arXiv:math/0603576 ([r3s-21]), abstract: "Precise conjectures were stated in our report [Lei03] on Deninger's work. The existence of such a foliated space and flow φ^t is still unknown except when Y is an elliptic curve (see Deninger [De02])"; p. 2: "Notice that the existence of such a quadruple (S_ℚ, F, g, φ^t) is still unknown"; Open Question 2: "Does there exist a laminated foliated space (S_Y = L_Y ×_{q^ℤ} ℝ^{+*}, F, g, φ^t) satisfying all the assumptions of Proposition 2 and Theorem 2 and the following assumption: (A) One has a natural bijection w ↦ γ_w between the set of closed points of Y and the set of primitive closed orbits of (S_Y, φ^t) satisfying log Nw = l(γ_w)." What S4′ adds (PARTIAL): the four sharpened clauses — exactly one simple orbit per prime; return derivative p^{1/2}·O (itself Deninger's prescription, [Den05] pp. 32–33); a preserved leaf of χ ≠ 0 in the accumulation set (from the program's Euler-characteristic constraint and [x-18] p. 3: "It is known that F is a fibration if and only if rank Λ = 1 … If one wants an infinitely generated Λ, one must allow the flow to have fixed points (≙ infinite places)"); a transverse measure — and the inverse-length-spectrum framing; not studied as a realizability problem by anyone reached. The solved case is [De02] = [x-22] (elliptic curves). Leichtnam's printed axiom list (*An invitation to Deninger's work on arithmetic zeta functions*, Contemp. Math. 387 (2005) 201–236) is UNDETERMINED → SPONSOR-FETCH (novelty/adjudication.md §4 item 1); it may already contain clauses (i)–(iv). [Quotations as read on disk by the Session-14 novelty adjudicator; connective sentences repair-pass wording.]*

---

**[ORCHESTRATOR ENACTMENT NOTE, 2026-09-05 23:55 IST, Session 16.]** The §16 below is the adjudicator's proposed text (`results/c3-r/s16/qs4prime/adjudication.md` §6.1), applied verbatim as a dated addendum. Enactment status, per standing orders 5 and 7: **S16-1, S16-2, S16-3's length-group statement, S16-7 and the coverage result are BINDING** (dual-derived by both scouts and confirmed by the adjudicator against the sources; S16-1's Leichtnam 2013 §4.1 read on disk, r3s-20). **S16-4, S16-5, S16-6 and the vacuity ruling inside S16-3 ("no S4′ object has a non-transverse set of that form") are the adjudicator's OWN derivations (novelty ledger N6, N7, N8, N10 — [single-check]) and are RECORDED PENDING the adversarial dual-model pass launched as the next stream (`results/c3-r/s16/qs4prime/refute-{F,O}.md`).** Until that pass reports, the binding frontier statement is: S4′ is Leichtnam's printed axiom list, unrealized, not killed by print; the closed-3-manifold kill holds for the KMNT/ALKL class (finitely many compact preserved leaves); whether S4′ objects can inhabit that class is the question the pending derivation A-IV answers.

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

---

## §16-bis. ENACTMENT after the adversarial dual-model pass (2026-09-06 00:54 IST, Session 16; refuters `results/c3-r/s16/qs4prime/refute-{F,O}.md`, binding adjudication `refute-adjudication.md`; run wf_f13af8e3-658)

Rulings: A-II STANDS-NARROWED; A-III FALLS; A-IV STANDS-NARROWED; the vacuity ruling STANDS-NARROWED; the clause-(iv) restatement STANDS-NARROWED; N10 STANDS-NARROWED. Root cause common to all six: S4′'s four clauses do not imply the fixed-point conformality; S4′ is amended by **clause (0) = (0-fix) + (0-coh)** (below), and Deninger's global (31) is NOT added.

**Verification labels for this block (orchestrator, standing order 7):** the adjudicator writes "dual-checked" for Theorem A = refuter F's F-1 (A)–(D), Corollary A.1 and B1′; those were derived by Fable 5.1 (refuter F) and re-derived by Fable 5.1 (the adjudicator) — two passes on ONE model. They are enacted PROVISIONALLY here and become binding only after the Opus 5 check launched as stream (c″) (`results/c3-r/s16/qs4prime/f1-check-O.md`). Everything else in this block (clause (0) required — three independent proofs, F + O + adjudicator; A-II steps 1–5 narrowed; A-IV (a)/(b) proofs; the vacuity narrowing; N10 narrowed; α = β; O-2 "a compact preserved leaf forces α = 0"; O-6 Markov–Kakutani; the A-III fall; the striking of "conformal to C, χ = +1") is dual-model (Fable + Opus) and BINDING now.

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

**[NOVELTY — dual-model check 2026-09-06]** B1′ is **PARTIAL**, not unanticipated (binding adjudication `results/c3-r/s16/novelty/adjudication.md` §1 N-D). Three printed relatives must lead any statement of it: **Cantwell–Conlon, *Tischler fibrations of open foliated sets*, Ann. Inst. Fourier 31 (1981) 113–135, proof of (3.11) at printed p. 127** — "P(ω) is the finitely generated image of ω : H₁(K;Z) → R" — a *proved* finite-generation theorem for the period group of an **open** F-saturated set in a closed manifold, via a compact nucleus (their P(ω) = {t : Φ^t maps every leaf of F|U onto itself}, §1 p. 114, is Deninger's Λ and KMNT's Λ_S), under hypotheses incomparable with B1′'s (all leaves of F|U dense, trivial holonomy, almost triviality) and with no rank bound and no length-spectrum consequence; **Deninger arXiv:math/0204110 p. 13 Rem. 3 = math/0505354 p. 24 Rem. 3** (the conclusion in the everywhere-transverse case, asserted with no proof and no reference, naming the fixed-point escape; repeated [x-18] p. 3); **ÁLKL *Simple foliated flows* printed p. 20 / memoir printed p. 114** (finite rank of Γ_l from compactness of M_l, in the compact-preserved-leaf class). What is new: the hypothesis (a finite union of leaves with dim_Q H₁ < ∞, not compact, no density or holonomy hypothesis), the bound dim_Q(Λ_{M₀} ⊗ Q) ≤ dim_Q H₁(M ∖ N;Q) by iterated Mayer–Vietoris, the Baire step, **finite rank rather than finite generation**, the restriction to transverse closed orbits, and the {log p} kill. Also binding: the α = 0 note's parenthesis is amended — **[x-06] p. 8 is ambiguous as printed**, and on the reading its antecedent ("a metric g_F as above" = the general assumption at the top of p. 8), its placement (after the "If we allow fixed points" paragraph) and its conclusion ("the class of smooth compact manifolds is too restrictive", remedy: laminations) support, Deninger asserts α = 0 **without proof for his whole manifold class including fixed points on compact leaves**; so "α = 0 is forced by any compact preserved leaf" is the *proof* of a printed assertion, not a statement print does not make.

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

**[NOVELTY — dual-model check 2026-09-06]** Prior-art status of this block (`results/c3-r/s16/novelty/adjudication.md` §0, §1): **N-F (every compact preserved leaf a fixed-point-free torus; clause (iii)'s leaf non-compact) is NOVEL** — no printed statement covers any part, and the printed literature asserts the **opposite arrangement as a hypothesis**, which must be cited with the claim: [x-06] p. 6 ("The fixed points of φ should lie in finitely many compact leaves"), KMNT Münster J. Math. 14 (2021) Def. 1.5(i) p. 327 with **Remark 1.6 p. 328** (the non-transverse *compact* leaves correspond to the infinite primes P_k^∞), ÁLKL memoir printed p. 100 ("M⁰ is a finite union of compact leaves"). Poincaré–Hopf and Poincaré–Bendixson are credited as inputs. **N-C (Theorem A(D)) is NOVEL**: the only printed suspicion is Deninger's *private* caution reported by Leichtnam at **arXiv:math/0603576v2 printed p. 12** (page corrected from "p. 11" — verified by running head) and repeated at arXiv:1307.3851 Comment 6 and 2008 §5.1 p. 17, given for a **different reason** ("too strong for being generalized") and with no argument, while Deninger himself assumes (31) *together with* a fixed point at [x-20] pp. 31–33. **Theorem A(A)–(C) is PARTIAL**: (A) is one line from ÁLKL's printed "the leaves preserved by φ correspond to the H-orbits preserved by φ̄, which indeed form Fix(φ̄)" (memoir §4.1.2 printed p. 100; SFF p. 2) **wherever φ̄ exists** — smooth flow, manifold — the foliated-space/jointly-continuous case being what is new; (B)'s conclusion is Deninger's unproved Remark 2 in the transverse manifold case and its ingredients are printed in Leichtnam Prop. 2 items 2]–4]; (C)'s engine is Candel Cor. 4.2 p. 497 / Thm. 4.3 p. 498, whose compact-leaf Dirac sentence (p. 498) *is* (C1)'s mechanism, and whose application to Deninger's objects is Deninger's own ([x-20] pp. 33–34 Rem. 7) — for all of X, conditional on arithmetic input. New in (C): the localization to N and (C4).

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

**[NOVELTY — dual-model check 2026-09-06]** **"closed leaf ⇒ compact leaf" is ANTICIPATED and must be cited, never claimed** (`results/c3-r/s16/novelty/adjudication.md` §1 N-E; both sweeps and the adjudicator opened the source): **D. B. A. Epstein, *Foliations with all leaves compact*, Ann. Inst. Fourier 26 (1976) no. 1, 265–282, §§2.2–2.4, printed p. 268** — "a leaf meets a coordinate neighbourhood in at most a countable number of slices" (2.2); "If L ∩ T₁ is infinite, then it has a limit point in L ∩ T. The holonomy construction … shows that each point of L ∩ T is a limit point of L ∩ T. In other words L ∩ T is perfect. By the Baire category theorem, no such a space is countable" (2.3); "**the subspace topology is equal to the leaf topology on a closed leaf**" (2.4). This is the program's own proof, ingredient for ingredient, and it is stated in **Ehresmann's foliated-space generality** (Epstein §§1.1–1.5; his §1.6 makes "manifold" an *extra* hypothesis), so it covers compact laminations; with X compact the remaining step is one sentence. The same correction applies wherever the device is used: `refute-F.md` §3.1, `refute-adjudication.md` §3.1, `f1-check-O.md` §6.5 step (3). Textbook second citations (Candel–Conlon, Moore–Schochet, Hector–Hirsch) remain unretrieved and **no proposition number is to be guessed**.

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

**[NOVELTY — dual-model check 2026-09-06]** The measure clause's prior art (`results/c3-r/s16/novelty/adjudication.md` §1 N-A, N-B): the e^{−t}-scaled transverse measure of an α = 1 object is **printed** — Leichtnam arXiv:math/0603576v2 Prop. 2, printed p. 15, items 2] "(φ^t)^*[λ_g] = e^t[λ_g]", 3] "µ_L dx defines a transverse measure denoted Λ", 4] "τ_Λ ∘ (φ^t)_* = e^{−t} τ_Λ" with the type III_{1/q} conclusion, and Lemma 10.1 "(λ_g ; C(Λ)) ≠ 0" with "the Ruelle–Sullivan current is closed" — so the modulus statement must credit Leichtnam, and only the *negative* theorem (no flow-invariant such measure; µ(T ∩ N) = 0) is new. Contrast worth printing: ÁLKL build their invariant transverse measure on **M¹ = M ∖ M⁰**, off the preserved leaves, with a b-density because it is not finite there (memoir printed p. 9 §1.3, p. 80 §3.1.4) — under Theorem A the δ₀ term receives **nothing** from N, while in ÁLKL's α = 0 world N is exactly where the density blows up. Hurder's vocabulary should be used rather than a new one: "an invariant transverse measure µ for F is **without atoms** if µ is zero on compact leaves" (`r3s-29`).

**S16-8 — consequential RE-POSING (recommended).** Q-S4⁗ as written asks for a compact lamination with a leaf conformal
to C; under (0-coh) that leaf is impossible, so the gate must ask instead: does there exist a compact foliated space X
with Riemann-surface leaves and a foliated flow whose non-transverse set N is a compact saturated sub-lamination with
no invariant transverse measure, all of whose leaves are hyperbolic, containing an exceptional minimal set, with a
hyperbolic-disk leaf on which the flow is a non-conformal source of rate 1/2 — and (manifold case) can such an N sit in
a closed 3-manifold with rank H₁(M ∖ N) = ∞? Duminy's theorem (semiproper leaves of an exceptional minimal set have a
Cantor set of ends; the disk has one) and Hurder's Problem 5.4 remain the instruments.

---

---

## §16-ter. Opus 5 check of the Fable-only items of §16-bis — ENACTED (2026-09-06 01:19 IST, Session 16; `results/c3-r/s16/qs4prime/f1-check-O.md`, run wf_b6cba300-2ae)

Verdicts: (A) STANDS; (B) STANDS (stronger: only φ^{t*}[λ_g] = e^t[λ_g] is used); (C) STANDS-NARROWED (Candel's regularity class for g); (D) STANDS-NARROWED (full hypothesis set; Ĉ excluded by (31)-along-L alone); Corollary A.1 STANDS-NARROWED (Reading (iii)′ for the disk); B1′ STANDS-NARROWED (finite RANK, tangency-set N, transverse orbits only); ε_x correction STANDS (forced, not merely fitting: κ_p < 0). **Every provisional label in §16-bis is hereby flipped to dual-model BINDING with the narrowings below, which are the Opus check's §8 verbatim and are enacted as written (N-1 … N-6, the [De02] GUARD of §8.3, and the §8.4 refinement of S16-8). The [De02] guard binds every future paraphrase: Theorem A must never be read as "α = 1 is impossible on a compact space".**

**[NOVELTY — dual-model check 2026-09-06]** Prior-art grades for the items §16-ter makes binding (`results/c3-r/s16/novelty/adjudication.md`, dual sweep + binding adjudication, every precursor opened at the page): **Theorem A(A)+(B) PARTIAL**, **(C) PARTIAL**, **(D) and Corollary A.1 NOVEL**, **B1′ PARTIAL**, **N1 PARTIAL**, **A-II-narrowed NOVEL**, **"closed leaf ⇒ compact leaf" ANTICIPATED (Epstein 1976, AIF 26, §§2.3–2.4 p. 268 — cite, do not claim)**. Nothing here is anticipated *as a theorem* except the last. Three relations must be printed as such: (i) (B) **supplies the proof** of Deninger's unproved Remark 2 ([Den05] p. 24 = math/0204110 p. 13) rather than generalizing it — Remark 2 says transversality + conformality ⇒ α = 0, (B) says α = 1 ⇒ no flow-invariant measure, and neither implies the other; transversality merely *supplies* the measure via |ω_φ| (KMNT published Lemma 1.9); (ii) (A) is a one-liner from ÁLKL's printed "preserved leaves ↔ Fix(φ̄)" (memoir printed p. 100) **in the smooth manifold category only**, the jointly-continuous foliated-space case being new; (iii) B1′ has a proved printed relative for open saturated sets in Cantwell–Conlon, AIF 31 (1981) 113–135, proof of (3.11) p. 127. Page corrections binding on all files: Leichtnam's "too strong" is at **arXiv:math/0603576v2 p. 12** (not p. 11); ÁLKL's finite-rank and period sentences are at memoir **printed pp. 114–115** (PDF 118–119); the published KMNT is **Münster J. Math. 14 (2021) 323–348** with **Lemma 1.9 / Def. 1.10 / Remark 2.8 / Cor. 2.9 / Prop. 2.10** (arXiv 1.10 / 1.11 / — / 2.2.4 / 2.2.5).

## §8. WHAT THIS DOES TO LEDGER §16-bis's PROVISIONAL LABELS

§16-bis states: *"the adjudicator writes 'dual-checked' for Theorem A = refuter F's F-1 (A)–(D),
Corollary A.1 and B1′; those were derived by Fable 5.1 (refuter F) and re-derived by Fable 5.1 (the
adjudicator) — two passes on ONE model. They are enacted PROVISIONALLY here and become binding only
after the Opus 5 check launched as stream (c″)."* This is that check. Its disposition, item by item.

### 8.1 What becomes BINDING as written

* **Theorem A(A)** — "every positive holonomy-invariant transverse measure concentrated on N is
  flow-invariant". **BINDING.** Add to the hypothesis list: "φ a jointly continuous R-action".
* **Theorem A(B)** — **BINDING**, and may be strengthened: replace "Under (0-coh) no nonzero such µ
  exists" by *"φ^{t*}[λ_g] = e^t[λ_g] in H̄²_F(X) ⇒ there is no nonzero flow-invariant holonomy-invariant
  transverse measure; with (A), none concentrated on N."* One-dimensionality of H̄²_F is not used.
* **Theorem A(C1), A(C4)** — **BINDING** (C4 in the phrasing of §8.2 below).
* **Theorem A(D)** — **BINDING** with the hypothesis set of §4.4 printed.
* **Corollary A.1**, first half ("the flow is not conformal along the archimedean leaf for any t ≠ 0") —
  **BINDING.**
* **The ε_x correction to refuter O** (§1.1 of `refute-adjudication.md`) — **BINDING**, and upgraded:
  the archimedean term does not merely "fit" with ε_x = +1, it **forces** it, because κ_p < 0
  ([x-20] p. 10). ε_x = sign det(1 − T_xφ^t|T_xF), on the leaf.
* **Everything already labeled dual-model (Fable + Opus) and BINDING** in §16-bis is untouched by this
  pass; I re-derived N's closedness (§1.1 (P1)) and confirm §3.2 of the adjudication independently.

### 8.2 Sentences that must be NARROWED, with exact wording

**(N-1) The "Verification labels" paragraph of §16-bis.** Replace the last sentence
("They are enacted PROVISIONALLY here and become binding only after the Opus 5 check launched as stream
(c″) (`results/c3-r/s16/qs4prime/f1-check-O.md`).") by:

> [ENACTED 2026-09-06, `f1-check-O.md` — Opus 5, second model.] The Opus check re-derived all seven
> items from the printed hypotheses and the primary sources. Nothing falls. Theorem A(A), A(B), A(C1),
> A(C4), A(D), Corollary A.1 (first half) and the ε_x correction are now **dual-model and BINDING**;
> A(B) is binding in the strengthened form (only φ^{t*}[λ_g] = e^t[λ_g] is used). Theorem A(C2), A(C3),
> A(D) and Corollary A.1 additionally require **g to be a riemannian metric on the lamination in
> Candel's regularity class** (leafwise smooth, all leafwise derivatives continuous in all variables,
> Candel §1.1–1.2 pp. 491–493) — Deninger's A^•_F asks only for transverse continuity ([x-20] p. 30,
> Warning), so the weaker phrase "continuous leafwise metric" does not license Candel's theorems.
> Corollary A.1's second half is conditional on Reading (iii)′ (below). **B1′ is narrowed: it gives
> finite RANK, not finite generation.**

**(N-2) S16-3, the B1′ clause.** Replace
"(B1′: on a closed 3-manifold the period group is finitely generated whenever N is a finite union of
leaves with finite-rank H₁; dual-checked, refuter F + binding adjudicator)" by:

> (B1′ [NARROWED 2026-09-06, `f1-check-O.md` §6]: on a closed 3-manifold, if the **tangency set**
> N = {x : Y_φ(x) ∈ T_xF} is a finite union of leaves each with dim_Q H₁ < ∞, then the group generated by
> the lengths of the closed orbits **transverse to F** has **finite rank**, dim_Q(Λ ⊗ Q) ≤
> dim_Q H₁(M ∖ N; Q) < ∞. "Finitely generated" is not derivable — a finite-rank subgroup of R need not be
> finitely generated. The kill of S4′ (i)+(ii) is a dimension count: {log p} is Q-linearly independent.
> Closed orbits *inside* N are not controlled by the argument; under clause (ii) there are none, because
> an orbit inside a leaf gives T_xφ^ℓ|T_xF the eigenvalue 1 while (ii) makes both eigenvalues of modulus
> NP^{1/2}. Dual-model: refuter F + binding adjudicator (Fable), re-derived by Opus 5.)

Likewise in §16-bis's S16-3 block, "the period group is finitely generated" → "the period group has
finite rank"; and in S16-3's headline sentence "The closed-orbit length group of a foliated flow on a
closed 3-manifold whose non-transverse set is a finite union of compact leaves is finitely generated" —
that KMNT-based sentence is about compact leaves and is not what B1′ generalizes; leave it, but append
"(for the finite-type generalization the derivable conclusion is finite rank, not finite generation —
§16-bis (N-2))".

**(N-3) S16-4, the (0-coh) sentence.** Replace
"For S4′ + (0-coh): no compact preserved leaf exists, every preserved leaf is a hyperbolic Riemann
surface, clause (iii)'s leaf is the hyperbolic disk if χ = +1, and the flow is not conformal along it for
any t ≠ 0 (Theorem A, Corollary A.1, dual-checked)." by:

> For S4′ + (0-coh), with g in Candel's regularity class: no compact preserved leaf exists, every
> preserved leaf is a hyperbolic Riemann surface, every holonomy-invariant transverse measure of X gives
> every transversal's intersection with N measure zero, and the flow is not conformal along the
> archimedean leaf for any t ≠ 0 (Theorem A, Corollary A.1; dual-model, `f1-check-O.md`). **Reading
> (iii)′, required for the disk:** clause (iii)'s "nonzero Euler characteristic" is read as "L is of
> finite topological type and χ(L) = 2 − 2g − n"; then χ(L) = +1 forces L ≈ R², and hyperbolic + simply
> connected gives L ≅ D. For a leaf of infinite type χ is undefined and clause (iii) says nothing.

**(N-4) S16-4, the (31) sentence — keep, and gloss.** "on a compact space, (31) along the fixed point's
leaf together with α = 1 is inconsistent (Theorem A(D), dual-checked)" stands; append:

> [Opus 5, 2026-09-06.] The full hypothesis set is: X compact, Riemann-surface-leaved, g in Candel's
> class; (0-coh) (or (0-glob)); a fixed point x_∞ with leaf L; and (31) on TF|L. Both ingredients are
> needed and each does distinct work: (31)-along-L alone excludes the hyperbolic, torus, C^\* **and Ĉ**
> cases (Ĉ by the second fixed point of a Möbius one-parameter group, whose derivative modulus is the
> reciprocal — so (C1) and hence (0-coh) are **not** needed there, contrary to the printed proofs);
> (0-coh) + compactness + Candel is needed only to exclude L ≅ C.

**(N-5) S16-5 and S16-6, "measure zero".** "it has invariant-transverse-measure zero" (S16-5) and
"it gives the non-transverse set N measure zero" (S16-6) are not well-formed for a transverse measure.
Replace both by: *"for every holonomy-invariant transverse measure µ of X and every regular transversal
T, µ(T ∩ N) = 0; equivalently the Ruelle–Sullivan measure of µ gives N measure zero, so N contributes
nothing to χ_Co(F, µ)."*

**(N-6) S16-6, the existence half.** The strike stands. Add the reason in one line: *the only printed
route to existence is Candel via a non-hyperbolic leaf, and under (0-coh) every preserved leaf is
hyperbolic (Theorem A(C3)) — while a non-preserved non-hyperbolic leaf, which does produce a measure, is
consistent and in fact occurs in Deninger's own example (§8.3).*

### 8.3 A guard that must be added to the ledger — [De02] is the sharp boundary case

Ledger §16-bis nowhere records that Deninger's solved case satisfies the α = 1 clause **and** (31)
globally **and** has euclidean leaves **and** carries a nonzero transverse measure — on a compact space.
Read at source ([x-20] pp. 34–36): the flow there "is everywhere transverse to the leaves of F and in
particular has no fixed points"; the leaves are images of C; g = e^t Re(ξη̄) "satisfies the conformality
condition (20) for α = 1"; Theorem 7.8 uses "a certain canonical transverse measure µ". Proposed
sentence for §16-bis:

> [GUARD, Opus 5, 2026-09-06.] Deninger's solved case [De02] = [x-20] §7.7 Example is a **compact** object
> satisfying (31) globally with α = 1, all of whose leaves are conformally C, carrying a nonzero
> holonomy-invariant transverse measure — and with **no fixed point** (p. 35, verbatim). It is therefore
> consistent with Theorem A and pins its scope: (C2) forbids euclidean leaves only **inside N**; (B)
> forbids only **flow-invariant** measures; (D) is false without the fixed point. Theorem A must never be
> paraphrased as "α = 1 is impossible on a compact space": what is impossible is α = 1 together with a
> fixed point on a leaf along which (31) holds.

### 8.4 Consequence for S16-8's re-posed gate

Unchanged in substance. Two refinements: (i) the manifold half should read "rank_Q H₁(M ∖ N; Q) = ∞"
(§6.4/§6.6), with N the tangency set; (ii) the hyperbolic-disk leaf in the corridor is conditional on
Reading (iii)′, so the gate should say "a leaf of finite type with χ = +1, i.e. conformally D".

---

---

## §16-quater. Dual-model NOVELTY verdicts on the Session-16 theorems — ENACTED (2026-09-06 02:53 IST; `results/c3-r/s16/novelty/{sweep-F,sweep-O,adjudication}.md`, run wf_e77765ff-28f)

Binding verdicts (Opus adjudicator, every precursor opened): **N-C Theorem A(D) NOVEL; N-F the narrowed A-II NOVEL** (each must travel with its printed contrast: Deninger's private caution reported by Leichtnam, math/0603576v2 printed p. 12, given for a different reason and without argument, while [x-20] pp. 31–33 assumes (31) together with a fixed point; and the printed manifold class puts the archimedean fixed points ON compact leaves — [x-06] p. 6, KMNT Def. 1.5(i) p. 327 with Remark 1.6 p. 328, ÁLKL memoir p. 100). **N-A, N-B, N-D, N-G PARTIAL**: Theorem A(A) is one line from ÁLKL's Fix(φ̄) identification in the smooth manifold category (new: foliated spaces with a merely jointly continuous flow); Theorem A(B) SUPPLIES THE PROOF of Deninger's unproved Remark 2 (math/0204110 p. 13 = math/0505354 p. 24) rather than generalizing it; Theorem A(C) localizes Deninger's own Candel inference (Rem. 7) to the preserved-leaf set; B1′ has the printed precursors Cantwell–Conlon, Ann. Inst. Fourier 31 (1981) 113–135, proof of (3.11) p. 127 (period group of an open saturated set finitely generated via a compact nucleus), Deninger's Remark 3, and ÁLKL memoir printed pp. 114–115 (finite rank in the transversely simple class); N1 likewise. **N-E ANTICIPATED: Epstein, Ann. Inst. Fourier 26 (1976) 265–282, §§2.3–2.4, printed p. 268, proves "closed leaf ⇒ leaf topology = subspace topology" in Ehresmann's foliated-space generality with the program's own proof — cite, never claim.** The adjudicator's eight required wording changes (its §3: Epstein citation; the [x-06] p. 8 reading; B1′'s prior-art line; two credit sentences for Theorem A; page corrections — Leichtnam p. 12 not p. 11, memoir pp. 114–115, KMNT published numbering Lemma 1.9/Def. 1.10/Cor. 2.9/Prop. 2.10, Deninger Cor. 3.5 (2002) = 5.5 (2005); the N-C guard note; the N-F contrast; the N-B sharpening) are BINDING and were inserted as dated `[NOVELTY — dual-model check 2026-09-06]` blocks at the claim points (five in this file, two in BARRIER-ZOO.md IV.13/IV.14, one in `refute-adjudication.md` §1.5). New sponsor-fetch items in STATUS. The six PDFs the sweeps fetched now live in `fetched-r3/` as r3s-31…r3s-36 (local-only).
