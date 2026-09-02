# REFEREE REPORT — probe A, Theorem B(b): the n-cell construction and the infinite-dimensionality conclusion

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Session 14.**
**Date:** 2026-09-02. **Referee:** **O**, one of two independent referees on this item (the second is a different model; nothing below was softened in anticipation of that pass — standing order 7).
**Item under review:** `results/c3-r/probe-9.3-a.md` §3, **Theorem B(b)** and its Corollary (i)/(ii) and scope notes (i)–(iii), together with every part of the note on which (b) depends.
**Debt discharged:** `results/c3-r/probe-9.3-adjudication.md` §4 item 6 — "Checked at proof-sketch level against the sources, not line-by-line: probe A's Theorem B(b) cell construction … Before any external circulation, Theorem B(b) and Cor. A.1 owe a dedicated referee pass."
**Standing orders.** SO5: every claim about a source below is quoted from the on-disk PDF at a stated **printed** page (printed page = PDF page throughout for [x-03]; verified at pp. 2, 5, 27, 50). Classical results with **no on-disk source** are labeled **[RU]** and carry no weight. SO7: the priority question is answered here on its own evidence (§7, finding **J3**).
**Note on the file.** This report replaces an earlier same-slot draft of 2026-09-02 02:22 (git `ce3a0a7`). The mathematical content differs materially: the earlier draft recorded the embedding step as recoverable only under a Hausdorff hypothesis; **this pass supplies an unconditional proof of the embedding** (§4.10), which converts finding J1 from a defect-with-loss into a defect-with-strengthening.

---

## 0. VERDICT BLOCK (stated first)

**VERDICT: PASS-WITH-REPAIRS.**
**FATAL 0 · MAJOR 4 · MINOR 8.**

The mathematics of Theorem B(b) survives a line-by-line re-derivation and comes out **stronger** than stated. Every input the adjudication left unchecked verifies against the printed sources: the splitting `Q̄^× = μ(Q̄) × V` (which is *printed in [x-03] itself*, twice), the Q-linear independence of the V-components of distinct rational primes, the construction and well-definedness of the unitary characters `Ψ_t`, their satisfaction of (Tors) and their exemption from (Image), their membership in the `E_max`-locus, the appeal to Thm 8.2 including its **unconditional status for Spec Z** via [Per11], the continuity of `Θ` **against Deninger's actual colimit/quotient topology**, and the injectivity of `Θ`. I could not break any of them, and I tried (§5).

But the theorem **as printed** must change. Four things of substance:

| # | Sev. | One line |
|---|---|---|
| **J1** | **MAJOR** | The first sentence of (b) asserts *unconditionally* that `S` contains a homeomorphic copy of the n-cube; the note's proof yields only a **continuous injection**, and upgrades it to an embedding **only** under the Hausdorff hypothesis that appears in the *second* sentence. As printed the first sentence is unproved. **Repair supplied and proved: `Θ` is an open map onto its image, hence an embedding, with no Hausdorffness hypothesis anywhere** (§4.10). The first sentence becomes a theorem; the second sentence's hypothesis becomes unnecessary for it. |
| **J2** | **MAJOR** | Post-adjudication (G1 = NO), the hypothesis "`S` … whose subspace topology is Hausdorff" is **unsatisfiable**: by (a), `S` contains a full packet, and the packet's subspace topology is non-Hausdorff (adjudication §3; independently re-derived here, §6.1). So the second sentence of (b) **as printed is vacuously true** and Corollary (ii)'s "by (b)" runs through a vacuous premise. Repaired statement (b1)/(b2) in §7. |
| **J3** | **MAJOR** (priority, SO7) | The **conclusion** of (b) for Deninger's own `Y₀` is **asserted in print, three times, without proof**: [x-03] p. 5 (twice) and p. 49; [x-06] p. 12. There is **no dimension-theoretic argument anywhere in [x-03]** (verified by exhaustive search and by reading §8 in full). What probe A contributes is therefore (i) a **proof** of a printed assertion and (ii) the **extension** from `Y₀` to every closed invariant `S` meeting every packet. The note's blanket novelty claim for "Theorem B" (§0 item 1, §9 item 2, §8 item 5) must be qualified accordingly. |
| **J4** | **MAJOR** (sourcing) | The dimension step rests on classical dimension theory for which **no source is on disk anywhere in the three corpora**. Under SO5 those inputs are **[RU]** and carry no weight, yet the note's §0 calls the resulting kill "referee grade" and its scope note (iii) merely calls them "standard". Either a dimension-theory source is fetched, or the S4-relevant conclusion must be routed through the two on-disk routes (repaired (b1) + metrizability; or non-Hausdorffness of packets). Exact statements needing a source are given in §4.11. |

Minor findings M1–M8 are in §7. Replacement text for every repair is in §7. What is now established at referee grade, and its exact scope, is §9.

**Two results proved in the course of this pass that are not in the note** (§8): (N1) `Θ` is an **open** injection onto its image — the unconditional embedding; (N2) `X₀` is **non-Hausdorff at the cell's own endpoints**, i.e. in the char-0 unitary locus, by an explicit elementary two-limit construction — a strictly new datum extending the adjudication's §3 (which established non-Hausdorffness only along packets), and one which bears on the adjudication's residual question Q-a.

---

## 1. What was read, and how

Fresh `pdftotext -layout` extractions were made this session from the four primary PDFs named in the task; every quotation below was re-read in those extractions, and the one load-bearing formula whose overline the text layer drops (Theorem 8.2's closure bars) was **verified by rendering the page image** (§4.3). Page-number calibration for [x-03]: the folio printed at the foot of PDF page *n* is *n*, checked at PDF pages 2, 5, 27, 50 — so **printed page = PDF page** and all citations below are printed pages.

Complete page list in §10.

`results/corpus-routing.md` header caveats were read first. The two that touch this item: caveat 14 (`r3s-08` is Morishita arXiv:2508.15971 **v5**, title-page verified) and the routing line for `x-03` ("cite **v4 only**; published = Indag. Math. 37 (2026) 25–136"). Neither disturbs anything below; **nothing in Theorem B(b) depends on [r3s-08] at all** (§4.12, M9).

---

## 2. The text under review, quoted exactly

From `results/c3-r/probe-9.3-a.md` §3:

> **Theorem B.** Let X₀ = Spec Z and E_f ⊆ E ⊆ E_max ([x-03]'s designated window: Γ^E = Γ by Thm 5.2/6.1, and connectedness/H⁰ hold for E ⊇ E_f by [x-03] §§9–10). Let S ⊆ X₀ be closed and flow-invariant, and suppose that for every prime p, S contains at least one periodic orbit of Γ_{(p)}. Then:
>
> **(a)** S contains **every** periodic orbit of every packet — in particular, for each p, uncountably many pairwise distinct closed orbits of primitive length log p (parametrized by the Cantor group B_p).
>
> **(b)** If moreover E = E_max (equivalently E_tors over Spec Z, §1.2), then S contains, for every n ≥ 1, a homeomorphic copy of the n-cube. Hence every closed invariant S as above **whose subspace topology is Hausdorff** (in particular: every candidate compact metrizable lamination) has covering dimension ≥ n for all n, i.e. is infinite-dimensional.

and the proof of (b), quoted in full because it is what is under review:

> **Proof of (b).** By (a), S ⊇ ∐_p Γ_{(p)} = all periodic points of the system (suspended; [x-03] Thm 6.1). S closed ⟹ S contains the closure of this set in X₀^{E_max}. Now [x-03] Thm 8.2 (p. 50; unconditional for Spec Z — Claim 8.1 is known for number rings via [Per11, Theorem 1], [x-03] p. 50) states X̌₀(C)_per‾ = X̌₀(S¹): every unitary-character point is a limit of periodic points, and the approximants produced by its Lemma 8.3 (pp. 50–53) have finite-kernel characters, hence lie in X̌₀(C)_{E_f} ⊆ X̌₀(C)_{E_max}. So for any unitary target point that itself lies in the E_max-locus, the approximation takes place inside the subspace X̌₀(C)_{E_max} (a sequence in a subspace converging in the ambient space to a point of the subspace converges in the subspace topology). Suspending (§1.3): S contains [Ψ, v] for every unitary generic-fiber point Ψ in the E_max-locus and every phase v.
>
> Now construct the cells. Let x_η ∈ X be the generic point ((0) ⊂ Z̄, κ(x_η) = Q̄). Write Q̄^× = μ(Q̄) × V with V uniquely divisible (μ(Q̄) is divisible, hence a direct summand), a Q-vector space of countable dimension. Fix distinct primes ℓ_1, …, ℓ_n; their V-components v_1, …, v_n are Q-linearly independent (a multiplicative relation ∏ℓ_i^{k_i} ∈ μ(Q̄) ∩ Q^× = {±1} forces k = 0). Complete to a Q-basis and, for t ∈ [0, ½]^n, define the unitary character Ψ_t: Q̄^× → S¹ by: Ψ_t = inclusion on μ(Q̄) ⊂ S¹; on the line Q·v_i: Ψ_t(v_i^{a}) := e^{2πi t_i a} (a ∈ Q); trivial on the remaining basis lines. Each Ψ_t is a well-defined character, unitary, with ker Ψ_t ∩ μ(Q̄) = 1, so (Tors) holds; (Image) is vacuous in characteristic 0 ([x-03] p. 27). Hence (x_η, Ψ_t) ∈ X̊₀(S¹) ∩ E_max-locus for every t, and by Thm 8.2 each [Ψ_t, 1] lies in the closure of the periodic set, hence in S.
>
> The map Θ: [0, ½]^n → S, t ↦ [Ψ_t, 1], is continuous: for each r ∈ Z̄∖{0}, decomposing r = ζ_r · ∏v_i^{a_i(r)} · w_r in the fixed splitting, Ψ_t(r) = ι(ζ_r)·e^{2πi⟨t, a(r)⟩}, continuous in t; pointwise convergence is the topology upstairs, and the maps to X̊₀ and to the suspension are continuous.
>
> Θ is injective: suppose [Ψ_t, 1] = [Ψ_{t'}, 1]. Then (Ψ_{t'}, 1) = (F_q Ψ_t, q⁻¹) for some q ∈ Q>0, and comparing phases forces q = 1, so Ψ_{t'} and Ψ_t are equal as points of X̌₀(C). Since the colimit is along injections F_ν ([x-03] Prop. 4.2, p. 27), each stratum embeds, so equality holds already in X̊₀(C): Ψ_{t'} = Ψ_t ∘ σ for some σ ∈ G. Evaluate at the **rational** points ℓ_i (fixed by every σ ∈ G): Ψ_{t'}(ℓ_i) = Ψ_t(ℓ_i), i.e. c_i e^{2πi t'_i} = c_i e^{2πi t_i} with the constant c_i = ι(ζ_{ℓ_i}); since t_i, t'_i ∈ [0, ½], t' = t.
>
> So Θ is a continuous injection of the n-cube into S. If S is Hausdorff in its subspace topology, Θ is a homeomorphism onto its image (compact to Hausdorff), so S contains an n-cell. If S is metrizable — every candidate lamination is — subspace monotonicity of covering dimension in separable metric spaces (Hurewicz–Wallman, classical) gives dim S ≥ n; more generally, for compact Hausdorff S the cell image is closed and closed-subspace monotonicity in normal spaces applies. As n was arbitrary, dim S = ∞. ∎

with the three scope notes:

> **Scope notes (honesty).** (i) For E strictly between E_f and E_max the cell characters Ψ_t (which have infinite kernel) may fall outside E; part (a) — which already kills the counting — holds for the whole window, while (b) as stated needs E = E_max or the unitary system Y₀^Den = X̌₀(S¹) ×_{Q>0} R_{>0} itself (where the cells live natively and the identical argument applies). Both spaces named by ledger §9.3 ("X₀, or X̌₀(S¹)×_{Q>0}R_{>0}") are covered. (ii) The Hausdorffness hypothesis in (b) is on the **subsystem**, not on X₀; every lamination in the sense of S4 is metrizable, so nothing is lost for the kill. (iii) Classical inputs: CRT-density of N in Ẑ_{(p)}; direct-summand property of divisible subgroups; compact-to-Hausdorff homeomorphism criterion; subspace monotonicity of covering dimension. All standard; flagged for the referee.

---

## 3. The ambient objects, re-derived from the printed sources

A reader must be able to check §4 without the note. Everything in this section is quoted from [x-03] at the stated printed page.

**3.1 Points (p. 23, Remark 3.4).** For `X₀ = spec R₀` affine with normalization `X = spec R` in `K = K̄₀`:

> "Remark 3.4. If X₀ = spec R₀ is affine, X = spec R, we will identify the points (x, P^×) of X̊(C) with the multiplicative maps P : R → C satisfying the following properties: 1) P(0) = 0, P(1) = 1. 2) p := P^{−1}(0) is additively closed and hence a prime ideal. 3) We have a factorization P : R → R/p → C. … Then we have P^σ = (p, P^×)^σ where P^σ = P ∘ σ."

For us `X₀ = Spec Z`, `R₀ = Z`, `R = Z̄`, `K = Q̄`, `G = Aut(Q̄/Q)`, `C = ℂ`, and (per §8's opening, p. 49) `N₀ = N`.

**3.2 Topology (pp. 40–43, 45, 47).** p. 40:

> "We begin with the affine case X₀ = spec R₀ and write X = spec R. Viewing X̊(C) as a set of multiplicative maps P : R → C as in Remark 3.4 we give X̊(C) the topology of pointwise convergence. It is the subspace topology induced by the Tychonov topology of C^R = ∏_R C on X̊(C) … Since R is countable, X̊(C) is a metrizable topological space."

p. 42: `X̊₀(C) = X̊(C)/G` with the quotient topology; `π` continuous. p. 43, the colimit:

> "We give X̌(C) = colim_{N₀} X̊(C) the inductive limit topology. It is the finest topology such that for all ν ∈ N₀ the inclusions F_ν^{−1}|_{X̊(C)} : X̊(C) ↪ X̌(C) are continuous. Thus Z ⊂ X̌(C) is closed, resp. open if and only if F_ν(Z) ∩ X̊(C) is closed, resp. open in X̊(C) for all ν ∈ N₀."

> "Proposition 7.4. a) X̊(C) is a closed and open subspace of X̌(C). b) F_q : X̌(C) → X̌(C) is a homeomorphism for every q ∈ Q₀^{>0}. c) The group G acts by homeomorphisms on X̌(C)."

> "We give X̌₀(C) = X̌(C)/G the quotient topology. Then X̌₀(C) is homeomorphic to colim_{N₀} X̊₀(C) with the inductive limit topology. The projections π : X̊(C) → X̊₀(C) and π̌ : X̌(C) → X̌₀(C) are continuous and since G acts by homeomorphisms, also open."

p. 45, Corollary 7.8:

> "The topological space X̊₀(C) is metrizable and separable and in particular Hausdorff."

p. 45, Corollary 7.9: "the spaces X̊(C), X̊₀(C), X̌(C) and X̌₀(C) are Hausdorff" (for arithmetic schemes carrying an ample invertible sheaf; `Spec Z` is affine, so this applies).

p. 47 — **the paragraph that settles the topology on the E-loci**, and which the whole re-derivation leans on:

> "Given an admissible class E as in Definition 4.1 we equip X̊(C)_E and X̊₀(C)_E with the subspace topologies of X̊(C) and X̊₀(C). … We give X̌(C)_E = colim_{N₀} X̊(C)_E and X̌₀(C)_E = colim_{N₀} X̊₀(C)_E the inductive limit topologies. **They agree with the subspace topologies via X̌(C)_E ⊂ X̌(C) and X̌₀(C)_E ⊂ X̌₀(C) because the subspaces F_ν^{−1}X̊(C) and F_ν^{−1}X̊₀(C) are open in X̌(C) resp. X̌₀(C) for all ν ∈ N₀.** As above, the natural continuous bijection X̌(C)_E/G → X̌₀(C)_E is a homeomorphism. **All preceding results in this section remain true if we replace X̊(C) etc. by X̊(C)_E etc.**"

**Consequence used repeatedly below (and stated here once):** `X̊₀(C)_E` is an **open subspace** of `X̌₀(C)_E`, and its topology is the subspace topology inherited from `X̊₀(C)`, which by Cor. 7.8 is **metrizable and separable**. Hence a net in `X̊₀(C)_E` converging in `X̌₀(C)_E` to a point of `X̊₀(C)_E` converges in `X̊₀(C)_E`, and conversely; and `X̌₀(C)_E` is first countable at every point of `X̊₀(C)_E`.

**3.3 Admissibility (p. 27).** Verbatim:

> "(Tors) the group ker(χ)_tors = ker(χ|_{μ(κ)}) is finite and |(ker χ)_tors| ∈ N₀."
> "(Image) Only if char κ > 0. If χ(κ^×) is torsion, then κ^× is torsion as well, i.e. κ^× ⊗ Q ≠ 0 implies χ(κ^×) ⊗ Q ≠ 0."
> "Definition 4.1. A class E of characters χ : κ^× → C^× on algebraically closed fields κ is (N₀−)admissible if for any σ ∈ Autκ resp. ν ∈ N₀ the character χ is in E if and only if χ ∘ σ resp. χ^ν = χ ∘ ( )^ν is in E. Moreover the characters in E should satisfy (Tors)."
> "Proposition 4.2. Given an admissible class of characters E on the κ(x)^× for x ∈ X, the set X̊(C)_E = {(x, P^×) ∈ X̊(C) | P^× is in E} ⊂ X̊(C) is G-invariant. It is foreward- and backward invariant under the N₀-action … The set X̌(C)_E = colim_{N₀} X̊(C)_E ⊂ X̌(C) is G- and Q₀^{>0}-invariant. The quotients X̊₀(C)_E = X̊(C)_E/G resp. X̌₀(C)_E = X̌(C)_E/G = colim_{N₀} X̊₀(C)_E are foreward- and backward N₀- resp. Q₀^{>0}-invariant. **The monoid N₀ acts by injections on X̊(C)_E and X̊₀(C)_E.**"

**Prop. 4.2 is purely set-theoretic.** It contains no topological statement whatever. (Finding M1.)

**3.4 The named classes (pp. 28–29).** p. 28: "Example. 1) E_tors : (Tors) holds. 2) E_max : (Tors) and (Image) hold." p. 29: "3) E_f : (Tors) and ker χ is finite. Equivalently: |ker χ| ∈ N₀. 4) E_fg : (Tors) and ker χ is finitely generated. 5) E_fd : (Tors) and ker χ ⊗ Q is finite dimensional. 6) E_fd0 : (Tors) and (ker χ|_{κ(x₀)^×}) ⊗ Q is finite dimensional where x₀ = π(x) …" and

> "We have inclusions in the appropriate sense E_f ⊂ E_fg ⊂ E_fd ⊂ E_fd0 ⊂ E_max ⊂ E_tors."

**3.5 Packets and the suspension (pp. 32–34, 38–39).** p. 32, (34)–(35); p. 33, (38)–(41), (43):

> "The set C_{x₀} fibres over the compact group Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p)^, and the fibres are the Q₀^{>0}-orbits in C_{x₀}."
> "ρ : X̊(C)_{E_tors} → N₀, (x, P^×) ↦ |(Ker P^×)_tors|" (41), and "ρ(F_ν(P)) = ν_x ρ(P) for ν ∈ N₀" (43).

p. 34, Theorem 5.2: "Let E be an admissible class with E ⊂ E_max. … **If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}.**"

p. 38, the suspension, verbatim:

> "consider the suspension X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0}. It is the quotient of X̌₀(C)_E × R^{>0} by the right Q₀^{>0}-action given by (P₀, u)q = (P₀q, q^{−1}u) = (F_q(P₀), q^{−1}u) for q ∈ Q₀^{>0}. … [P₀, u]·v = [P₀, uv] … φ^t([P₀,u]) = [P₀, u e^t]. For a point x₀ of X₀ with finite residue field of characteristic p set Γ_{x₀} = C_{x₀} ×_{Q₀^{>0}} R^{>0} ⊂ X₀."
> "Thus all R^{>0}-orbits in Γ_{x₀} are circles R^{>0}/Nx₀^Z and Γ_{x₀} fibres over Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p)^ with fibres the R^{>0}-orbits in Γ_{x₀}. We set Γ^E_{x₀} = C^E_{x₀} ×_{Q₀^{>0}} R^{>0} … **If e.g. E_f ⊂ E then Γ^E_{x₀} = Γ_{x₀}.**"

p. 39, Theorem 6.1: "{x₀ ∈ X₀ | (R^{>0})_{x₀} ≠ 1} = ∐_{x₀} Γ^E_{x₀}", i.e. **the periodic points of `X₀` are exactly the union of the packets.**

**3.6 Two elementary properties of the quotient map `q : X̌₀(C)_E × R^{>0} → X₀` used below.**
(i) `q` is **continuous** — it is a quotient map by definition (p. 38).
(ii) `q` is **open**: for `U` open, `q^{-1}(q(U)) = ⋃_{r ∈ Q₀^{>0}} U·r`, and each translate `U·r` is open because `F_r` is a homeomorphism of `X̌₀(C)_E` (Prop. 7.4 b), p. 43, together with the last sentence of the p. 47 paragraph) and `u ↦ r^{-1}u` is a homeomorphism of `R^{>0}`. Hence `q(U)` is open. *(The note asserts this in §1.3 with the same one-line reason; I certify it.)*
(iii) The fibres of `q` are exactly the `Q₀^{>0}`-orbits (definition of the quotient).

**3.7 The identity `F_ν(X̊(C)) = {P ∈ X̊(C) | P(μ_ν(K)) = 1}` (p. 42, equation (51)).** Verbatim, inside the proof of Lemma 7.3:

> "First assume that X₀ = spec R₀ is affine. Lemma 4.6 implies the equations F_ν(X̊(C)) = {P ∈ X̊(C) | P(μ_ν(K)) = 1} ⊂ X̊(C), (51)"

This is the single fact that makes the **repair** of §4.10 work, and it is on disk.

---

## 4. Line-by-line re-derivation of Theorem B(b)

Throughout: `X₀ = Spec Z`, `E = E_max` (equivalently `E_tors`, see §4.6), `N₀ = N`, `C = ℂ`, `X₀ = X̌₀(C)_{E_max} ×_{Q^{>0}} R^{>0}`, `S ⊆ X₀` closed and flow-invariant and meeting every packet, `q` the quotient map of §3.6.

### 4.1 `S` contains every periodic point

By (a) (Theorem A + Thm 5.2), `S ⊇ Γ^{E}_{(p)} = Γ_{(p)}` for every prime `p`. By **Theorem 6.1 (p. 39)** the set of points of `X₀` with non-trivial isotropy is exactly `∐_{x₀} Γ^E_{x₀}`, and for `X₀ = Spec Z` the points `x₀` with finite residue field are exactly the primes. Hence

  `S ⊇ P := ∐_p Γ_{(p)} = {periodic points of (X₀, φ)}`.  ✓ **re-derived.**

*(Theorem A itself was re-derived three times already — probe A, probe B, adjudication §2 — and I re-verified each of its printed inputs while reading §§5–7 for this pass: (34)–(35) p. 32, (38)–(39) pp. 32–33, Thm 5.2 p. 34, the suspension identity p. 38, the strata paragraph p. 47. It stands. Note for the record that Theorem A needs `χ^c ∈ E` for the limit; for `E ⊇ E_f` this is automatic because `c` is a unit and the character is then injective. That is the only place the window `E ⊇ E_f` enters (a).)*

### 4.2 `S` contains the closure of the periodic set

`S` is closed, so `S ⊇ cl_{X₀}(P)`. ✓ Trivial, and no Hausdorffness is used.

Identify `P` upstairs. Deninger defines (p. 50):

> "X̊(C)_per = {(x, P^×) ∈ X̊(C) | κ(x) ≅ F̄_p for some p and ker P^× is finite}", and `X̌(C)_per = colim_N X̊(C)_per ⊂ X̌(C)`.

A point of `C_{x₀}` is `F_ν^{-1}(x, P^×)` with `κ(x) = F̄_p` and `|ker P^×| ∈ N₀` finite (p. 32, first paragraph), i.e. exactly a point of `X̌₀(C)_per`; conversely every point of `X̌₀(C)_per` lies over some closed point. Hence `X̌₀(C)_per = ⋃_{x₀} C_{x₀}` and

  `q(X̌₀(C)_per × R^{>0}) = ∐_{x₀} Γ_{x₀} = P`. ✓

Also `X̌₀(C)_per ⊆ X̌₀(C)_{E_max}`: for `κ(x) = F̄_p`, (Tors) holds because `ker(P^×)_tors = ker P^×` is finite of order in `N₀ = N`; (Image) holds vacuously because `κ(x)^× = F̄_p^×` is torsion, so `κ(x)^× ⊗ Q = 0`. ✓ (These are in fact in `E_f`, since `ker P^×` is finite — matching the note's claim that the approximants lie in `X̌₀(C)_{E_f} ⊆ X̌₀(C)_{E_max}`; the inclusion `E_f ⊂ E_max` is printed at p. 29.) ✓

### 4.3 Theorem 8.2: the hypotheses as printed, and unconditionality for `Spec Z`

The text layer of the PDF **drops the closure overbars** in Theorem 8.2. Because this is load-bearing, I rendered printed page 50 as an image and read it. The statement is, verbatim and with the bars:

> "**Theorem 8.2.** Let X₀ be an integral normal scheme of finite type over spec Z. If dim X₀ ≥ 2 or dim X₀ = 1 and char K₀ > 0 assume that Claim 8.1 holds. Then we have `cl(X̌(C)_per) = X̌(S¹)` and `cl(X̌₀(C)_per) = X̌₀(S¹)`."

**Hypothesis check for `X₀ = Spec Z`.** `dim Spec Z = 1` and `char K₀ = char Q = 0`. Neither disjunct of "dim X₀ ≥ 2 or (dim X₀ = 1 and char K₀ > 0)" holds. **Therefore Theorem 8.2 is applied with no assumption at all for `Spec Z`.** ✓ The note's parenthetical "unconditional for Spec Z" is correct.

**Why it is unconditional — the [Per11] chain, checked.** The proof of Thm 8.2 reduces to Lemma 8.3, whose proof (pp. 51–53) says "By assumption we may apply Claim 8.1 to our ring A", where `A` is the normalization of `R̄₀ = R₀/p₀` in a finite extension `κ` of `κ(x₀)`, and notes `dim A = dim R̄₀ ≤ dim R₀ = dim X₀`. For `X₀ = Spec Z`: if `p₀ = (0)` then `R̄₀ = Z`, `κ` is a number field and `A = o_κ`; if `p₀ = (p)` then `R̄₀ = F_p` and `dim A = 0`. Deninger covers exactly these two cases immediately after Claim 8.1 (p. 50), verbatim:

> "If dim A = 0 i.e. if A = κ is a finite field, the claim holds trivially. If spec A is a non-empty open subscheme of spec o_κ for some number field κ, then the set M in Claim 8.1 is always infinite, and it even has a positive Dirichlet density. **This follows from [Per11, Theorem 1].**"

with bibliography entry (p. 119 of the reference list): "[Per11] Antonella Perucca. On the reduction of points on abelian varieties and tori." ✓ **The note's citation is exact.**

**The approximants.** Lemma 8.3 (p. 50) produces "a maximal ideal m of R̄ and a character χ : (R̄_m/mR̄_m)^× = (R̄/m)^× → S¹ **with finite kernel**", and the proof of Thm 8.2 (p. 51) assembles from it a point `Q = (m, χ) ∈ X̊(C)_per`. So the approximants have finite-kernel characters at points with finite residue field. ✓ The note's description is exact.

**The subspace step.** Thm 8.2's closure is taken in `X̌₀(C)` (the unrestricted space). For a target `Ψ ∈ X̌₀(S¹)` that happens to lie in `X̌₀(C)_{E_max}`, the approximating net lies in `X̌₀(C)_per ⊆ X̌₀(C)_{E_max}` and converges in the ambient to a point of the subspace, hence converges **in the subspace topology** of `X̌₀(C)_{E_max}`. This is a general fact about subspaces, and — crucially — the note's use of it is legitimate here **only because of the p. 47 paragraph**, which certifies that `X̌₀(C)_E` carries the subspace topology of `X̌₀(C)` and not a strictly finer colimit topology. The note does not say this; it is nevertheless true and cited elsewhere in the note (§1.1). ✓ (Bookkeeping remark M2 in §7.)

**Suspending.** `q` is continuous, so `q(cl(A)) ⊆ cl(q(A))` for `A = X̌₀(C)_per × R^{>0}`. Since `cl(A) ⊇ {Ψ} × R^{>0}` for every `Ψ ∈ cl(X̌₀(C)_per)`, we get `[Ψ, v] ∈ cl_{X₀}(P) ⊆ S` for every phase `v`. ✓ **re-derived.**

### 4.4 The splitting `Q̄^× = μ(Q̄) × V`

Let `μ := μ(Q̄)` and `V := Q̄^×/μ`.

1. `Q̄^×` is divisible (every element of an algebraically closed field has n-th roots), so `μ = (Q̄^×)_tors` is divisible.
2. A divisible subgroup of an abelian group is a direct summand; hence `Q̄^× ≅ μ × V`, and a splitting `β : V → Q̄^×` exists.
3. `V` is divisible (quotient of a divisible group) and torsion-free (if `x^n ∈ μ` then `x ∈ μ`), hence **uniquely divisible**, hence a `Q`-vector space.
4. `dim_Q V ≤ card Q̄^× = ℵ₀`, and `dim_Q V` is infinite because the classes of the rational primes are independent (§4.5). So `dim_Q V = ℵ₀`.

**This is not a "classical input" that needs flagging: it is printed twice in [x-03].** p. 28, inside the proof of Lemma 4.3:

> "The sequences 1 → μ(k) → k^× → k^×/μ(k) → 1 and 1 → μ(C) → C^× → C^×/μ(C) → 1 are both split since μ(k) and μ(C) are divisible. Choose splittings and consider the induced isomorphisms k^× ≅ μ(k) × (k^×/μ(k)) and C^× ≅ μ(C) × (C^×/μ(C)). Here k^×/μ(k) and C^×/μ(C) are uniquely divisible abelian groups and therefore Q-vector spaces."

and — better still for our purpose, because it is the *topological* statement — p. 53, in the proof of Proposition 9.1:

> "Given a point P = (x, P^×) of X̊(C)′, since μ(κ(x)) is divisible, we can choose a splitting β of the exact sequence 1 → μ(κ(x)) → κ(x)^× ⇄ κ(x)^× ⊗ Q → 1. It induces a **topological isomorphism of groups** Hom(κ(x)^×, C^×) → Hom(μ(κ(x)), C^×) × Hom(κ(x)^× ⊗ Q, C^×), χ ↦ (χ|_{μ(κ(x))}, χ ∘ β)."

(For `κ` algebraically closed, `κ^× ⊗ Q = κ^×/μ(κ) = V`.) ✓ **Finding M4:** the note lists this among "classical inputs … flagged for the referee"; it should be **cited to [x-03] pp. 28 and 53**, and the p. 53 sentence should be cited for the continuity of `Θ` (§4.8), which it gives immediately.

### 4.5 `Q`-linear independence of the `V`-components of distinct rational primes

Let `π : Q̄^× ↠ V` be the projection and `v_i := π(ℓ_i)`.

Suppose `∑_{i=1}^n q_i v_i = 0` in `V` with `q_i ∈ Q`. Multiply by a common denominator: `∑ k_i v_i = 0` with `k_i ∈ Z` not all zero if the `q_i` are not all zero (this step is *elided in the note*, finding M6). Then `π(∏ ℓ_i^{k_i}) = 0`, i.e.

  `∏_i ℓ_i^{k_i} ∈ μ(Q̄) ∩ Q^× = μ(Q) = {±1}`.

The left side is a positive rational, so `∏ ℓ_i^{k_i} = 1`, and unique factorization in `Z` gives `k_i = 0` for all `i`. Contradiction. Hence `v_1, …, v_n` are `Q`-linearly independent. ✓ **re-derived; the note's parenthetical is correct as far as it goes.**

*(Same argument shows the `π(ℓ)` over **all** rational primes `ℓ` are `Q`-independent; this is used in §4.12.)*

### 4.6 The characters `Ψ_t`: well-definedness, (Tors), (Image), `E_max`

Fix once and for all: the injection `ι : μ(K) ↪ μ(C)` of [x-03] p. 31 ("Fix an injective homomorphism ι : μ(K) ↪ μ(C)"); a splitting `Q̄^× = μ × V`; and a `Q`-basis `B` of `V` containing `v_1, …, v_n`.

For `t ∈ [0, ½]^n` let `λ_t : V → R` be the unique `Q`-linear map with `λ_t(v_i) = t_i` and `λ_t(b) = 0` for `b ∈ B ∖ {v_1,…,v_n}`, and define

  `Ψ_t : Q̄^× = μ × V → S¹`,  `Ψ_t(ζ·v) := ι(ζ) · e^{2πi λ_t(v)}`.

- **Well-defined homomorphism:** it is the product of the homomorphism `ι` on the first factor and the homomorphism `exp(2πi λ_t)` on the second, on a direct product. ✓ (The note's notation "`Ψ_t(v_i^a) := e^{2πi t_i a}`" writes `V` multiplicatively; the content is the above.)
- **Unitary:** values lie in `μ(C) · S¹ = S¹`. ✓ So `(x_η, Ψ_t) ∈ X̊(S¹)` in Deninger's sense (p. 49: "X̊(S¹) is the subspace of X̊(C) consisting of points (x, P^×) with P^× : κ(x)^× → S¹ a unitary character"). ✓
- **A legitimate point of `X̊(C)`:** by Remark 3.4 (p. 23) we must exhibit a multiplicative `P : Z̄ → ℂ` with `P(0)=0`, `P(1)=1`, `P^{-1}(0)` additively closed, factoring through `Z̄/P^{-1}(0)`. Take `P := Ψ_t` on `Z̄ ∖ {0}` and `P(0) := 0`; then `P^{-1}(0) = (0)`, which is a prime ideal, and `x = x_η` is the generic point of `X = Spec Z̄` with `κ(x_η) = Q̄`. ✓
- **(Tors):** `ker Ψ_t ∩ μ = ker ι = 1`, so `ker(Ψ_t)_tors = ker(Ψ_t|_μ) = 1`, which is finite and `|·| = 1 ∈ N₀` (1 lies in every submonoid). ✓ *Note that the printed (Tors) has two clauses — "finite **and** |(ker χ)_tors| ∈ N₀" — and the note's §1.2 paraphrase drops the second (finding M5); here both hold.*
- **(Image):** printed as "**Only if char κ > 0.**" Here `κ(x_η) = Q̄` has characteristic 0, so (Image) is not imposed. ✓ The note's "(Image) is vacuous in characteristic 0 ([x-03] p. 27)" is exact.
- **Hence `Ψ_t ∈ E_max`,** and `(x_η, Ψ_t) ∈ X̊(C)_{E_max} ∩ X̊(S¹)`. ✓

**`E_max` vs `E_tors` over `Spec Z` (the note's §1.2 observation).** The residue fields occurring in `X = Spec Z̄` are `F̄_p` (closed points) and `Q̄` (generic point). For `F̄_p`, `κ^×` is torsion so `κ^× ⊗ Q = 0` and (Image) is vacuously satisfied; for `Q̄`, (Image) is not imposed. Hence the **loci** satisfy `X̌₀(C)_{E_max} = X̌₀(C)_{E_tors}` for `X₀ = Spec Z`. ✓ (As *classes of characters on all algebraically closed fields* they differ; the note's "equivalently `E_tors` over `Spec Z`" is about the loci and is correct.)

### 4.7 `[Ψ_t, 1] ∈ S`

`Ψ_t ∈ X̊₀(S¹) ⊆ X̌₀(S¹) = cl(X̌₀(C)_per)` by Thm 8.2 (§4.3); `Ψ_t` lies in the `E_max`-locus (§4.6); by §4.3 the approximation may be taken inside `X̌₀(C)_{E_max}`; and by §4.3's suspension step `[Ψ_t, v] ∈ cl_{X₀}(P) ⊆ S` for every `v`, in particular `v = 1`. ✓ **re-derived.** No Hausdorffness of anything is used.

### 4.8 Continuity of `Θ` — against the actual topology, not an assumed product topology

`Θ : [0,½]^n → X₀`, `t ↦ q(Ψ_t, 1)`, where `Ψ_t` also denotes `π(x_η, Ψ_t) ∈ X̊₀(C)_{E_max}`.

The topology chain, each link with its printed source:

1. **Into `X̊(C)`.** The topology is pointwise convergence on `Z̄` (p. 40). Fix `r ∈ Z̄ ∖ {0}` and write `r = ζ_r · β(w_r)` with `ζ_r ∈ μ`, `w_r ∈ V`; expand `w_r = ∑_i a_i(r) v_i + (basis terms outside {v_i})` with `a_i(r) ∈ Q`, finitely many terms. Then
   `Ψ_t(r) = ι(ζ_r) · e^{2πi ⟨t, a(r)⟩}`,
   which is continuous in `t ∈ R^n` (it is the exponential of an affine function of `t`). `Ψ_t(0) = 0` for all `t`. So `t ↦ (x_η, Ψ_t)` is continuous into the Tychonov subspace `X̊(C)`. ✓ *(This is exactly the "topological isomorphism" of [x-03] p. 53 read from right to left: continuity in the `Hom(V, C^×)`-factor is continuity of `t ↦ exp(2πiλ_t)` pointwise.)*
2. **Into `X̊₀(C)`.** `π : X̊(C) → X̊₀(C)` is continuous (p. 42). ✓
3. **Into `X̊₀(C)_{E_max}`.** The image lies in the `E_max`-locus (§4.6), which carries the **subspace** topology (p. 47). Continuity into a subspace containing the image follows. ✓
4. **Into `X̌₀(C)_{E_max}`.** `X̊₀(C)_{E_max}` is an open subspace (p. 47). ✓
5. **Into `X̌₀(C)_{E_max} × R^{>0}`.** Pair with the constant `1`. ✓
6. **Into `X₀`.** `q` is the quotient map (p. 38), hence continuous; continuity **into** a quotient of a space one maps continuously into is automatic. ✓

**Verdict on the step the task singled out.** The note's continuity argument is correct, and — this is the point — continuity is the *easy* direction here: the colimit topology on `X̌₀(C)_E`, the `G`-quotient topology on `X̊₀(C)`, and the `Q^{>0}`-quotient topology on `X₀` are all *coarser than or equal to* what a naive product picture would give, and one maps *into* each of them. **The topology bites in the opposite direction — whether `Θ` is a homeomorphism onto its image — and that is §4.10.** ✓ **re-derived, no defect.**

### 4.9 Injectivity of `Θ`, and exactly what Prop. 4.2 says

Suppose `Θ(t) = Θ(t')`, i.e. `q(Ψ_t, 1) = q(Ψ_{t'}, 1)`. The fibres of `q` are `Q^{>0}`-orbits (§3.6 (iii)), so `(Ψ_{t'}, 1) = (Ψ_t, 1)·r = (F_r Ψ_t, r^{-1})` for some `r ∈ Q^{>0}`. The second coordinate gives `r^{-1} = 1`, so `r = 1` and `Ψ_{t'} = Ψ_t` **in `X̌₀(C)_{E_max}`**. ✓ (The note's "comparing phases forces q = 1" — correct and one line.)

Both points lie in the `ν = 1` stratum `X̊₀(C)`, and the canonical map `X̊₀(C) → X̌₀(C) = colim_N X̊₀(C)` is **injective** because the colimit is along injections: [x-03] Prop. 4.2 (p. 27), last sentence, "The monoid `N₀` acts by injections on `X̊(C)_E` and `X̊₀(C)_E`". ✓ So `Ψ_{t'} = Ψ_t` in `X̊₀(C) = X̊(C)/G`, i.e. there is `σ ∈ G` with `(x_η, Ψ_{t'}) = (x_η, Ψ_t)^σ = (x_η^σ, Ψ_t ∘ σ)`. (`x_η` is the zero ideal of `Z̄`, hence `G`-stable, so the first coordinates match automatically.)

Now evaluate at the rational primes, which `G = Aut(Q̄/Q)` fixes pointwise:

  `Ψ_{t'}(ℓ_i) = Ψ_t(σ(ℓ_i)) = Ψ_t(ℓ_i)`,
  i.e. `ι(ζ_{ℓ_i}) e^{2πi t'_i} = ι(ζ_{ℓ_i}) e^{2πi t_i}`,
  i.e. `t'_i − t_i ∈ Z`.

Since `t_i, t'_i ∈ [0, ½]`, `|t'_i − t_i| ≤ ½ < 1`, so `t'_i = t_i`. ✓ **re-derived, and the parameter range `[0,½]` is exactly what makes the last line work** (on `[0,1]^n` the endpoints `0` and `1` would collide; the note's choice is correct and not accidental).

**Finding M1.** The note writes "Since the colimit is along injections `F_ν` ([x-03] Prop. 4.2, p. 27), **each stratum embeds**". Prop. 4.2 gives set-theoretic injectivity only; the *topological* statement ("embeds") is **Prop. 7.4 a) p. 43** ("X̊(C) is a closed and open subspace of X̌(C)") together with the p. 47 paragraph and the openness of `π̌` (p. 43). The injectivity argument needs only the set-theoretic half, so nothing is broken; the citation must be split.

### 4.10 The embedding step — THE GAP, and its repair (unconditional)

**The gap.** The note concludes: "So `Θ` is a continuous injection of the n-cube into `S`. **If `S` is Hausdorff in its subspace topology**, `Θ` is a homeomorphism onto its image (compact to Hausdorff), so `S` contains an n-cell." But the **first sentence of Theorem B(b)** asserts, with no hypothesis at all, "`S` contains, for every `n ≥ 1`, a homeomorphic copy of the n-cube". **As printed, that sentence is not proved.** A continuous injection of a compact space into a non-Hausdorff space need not be an embedding, and by §6.1 the ambient `X₀` *is* non-Hausdorff and so is `S`. This is finding **J1**, and it is a genuine defect of the printed statement, not a quibble: the *only* justification the note offers for the first sentence is a criterion whose hypothesis fails.

**The repair. `Θ` is an open map onto its image, hence a topological embedding, with no Hausdorffness hypothesis whatsoever.** I prove this now; the proof uses only [x-03] pp. 42 (51), 43, 45, 47.

*Step R1 (the cube embeds in the stratum).* Let `Θ̃ : [0,½]^n → X̊₀(C)_{E_max}`, `t ↦ Ψ_t`. It is continuous (§4.8 links 1–3) and injective (§4.9, which showed `Ψ_t = Ψ_{t'} ⟹ t = t'` already in `X̊₀(C)`). Its domain is compact and its target is Hausdorff — indeed **metrizable and separable**, Cor. 7.8 (p. 45), and the `E`-locus carries the subspace topology (p. 47). A continuous bijection from a compact space onto a Hausdorff space is a homeomorphism, so **`Θ̃` is a topological embedding.** ✓

*Step R2 (the arithmetic key).* **Claim.** Let `P ∈ X̊(C)` with `P|_{μ(K)}` injective, and let `r ∈ Q^{>0}` with `F_r(P) ∈ X̊(C)`. Then `r ∈ N`.

*Proof.* Write `r = m/n` in lowest terms, `m, n ∈ N`, `gcd(m,n) = 1`. Since `F_n ∘ F_r = F_m` and `F_r(P) ∈ X̊(C)`, we get `F_m(P) = F_n(F_r(P)) ∈ F_n(X̊(C))`. By (51) (p. 42), `F_n(X̊(C)) = {R ∈ X̊(C) | R(μ_n(K)) = 1}`, so `F_m(P)(ζ) = 1` for all `ζ ∈ μ_n(K)`, i.e. `P(ζ^m) = 1`. Because `gcd(m,n) = 1`, the map `ζ ↦ ζ^m` is an automorphism of the cyclic group `μ_n(K)`; hence `P(μ_n(K)) = 1`. But `P|_{μ(K)}` is injective, so `μ_n(K) = 1`, i.e. `n = 1` and `r = m ∈ N`. ∎

*(Two remarks. First: `X̊(C)` is `G`-invariant (Lemma 7.3, p. 42: "the group `G` acts by homeomorphisms on `X̊(C)`") and `F_r` commutes with `G`, so the same statement holds verbatim downstairs in `X̊₀(C)`. Second: `Ψ_s|_{μ(Q̄)} = ι` is injective for every `s`, so the Claim applies to every point of the cell — and it applies **in the unitary system too**, since it never mentions `E`.)*

*Step R3 (openness onto the image).* Let `U ⊆ [0,½]^n` be open. By R1 there is an open `W₁ ⊆ X̊₀(C)_{E_max}` with `Θ̃(U) = W₁ ∩ Θ̃([0,½]^n)`; shrinking, we may take `W₁` open in `X̌₀(C)_{E_max}` as well, since `X̊₀(C)_{E_max}` is open there (p. 47). Put

  `W := W₁ × (2/3, 3/2) ⊆ X̌₀(C)_{E_max} × R^{>0}`, an open set,

and `O := q(W)`, which is **open in `X₀`** because `q` is an open map (§3.6 (ii)).

I claim `O ∩ Θ([0,½]^n) = Θ(U)`.

  `⊇`: for `s ∈ U`, `(Ψ_s, 1) ∈ W₁ × (2/3,3/2) = W`, so `Θ(s) = q(Ψ_s,1) ∈ O`. ✓
  `⊆`: suppose `Θ(s) ∈ O` for some `s ∈ [0,½]^n`. Then some point of the `Q^{>0}`-orbit of `(Ψ_s, 1)` lies in `W`, i.e. `(F_r Ψ_s, r^{-1}) ∈ W₁ × (2/3, 3/2)` for some `r ∈ Q^{>0}`. From the first coordinate, `F_r Ψ_s ∈ W₁ ⊆ X̊₀(C)_{E_max} ⊆ X̊₀(C)`; by **Step R2**, `r ∈ N`. From the second coordinate, `r^{-1} > 2/3`, so `r < 3/2`, so `r = 1`. Hence `Ψ_s ∈ W₁`, so `Θ̃(s) ∈ W₁ ∩ Θ̃([0,½]^n) = Θ̃(U)`, so `s ∈ U` (R1), so `Θ(s) ∈ Θ(U)`. ✓

Therefore `Θ(U)` is open in the subspace `Θ([0,½]^n)`. Since `Θ` is a continuous bijection onto its image and open onto its image, **`Θ` is a homeomorphism onto its image.** ∎

**Consequences.**
1. The first sentence of Theorem B(b) is **true and proved with no hypothesis**: `S` contains a subspace homeomorphic to `[0,½]^n ≅ [0,1]^n`, for every `n ≥ 1`.
2. `Θ([0,½]^n)` is a **compact metrizable** (indeed cube-homeomorphic) subspace of `S`, hence Hausdorff — even though `S` itself is not (§6.1). There is no contradiction: a non-Hausdorff space can have Hausdorff compact subspaces.
3. The Hausdorff hypothesis in the printed second sentence is **not needed for the cell**; it was needed only because the note used compact-to-Hausdorff as its embedding criterion. It is still needed — or rather, something is still needed — for the *dimension* conclusion (§4.11).
4. The whole argument goes through verbatim in the **unitary system** `Y₀^Den = X̌₀(S¹) ×_{Q^{>0}} R^{>0}`: Step R2 never mentions `E`, Cor. 7.8/7.9 apply to `X̊₀(C) ⊇ X̊₀(S¹)`, and `q` is open there for the same reason.

### 4.11 The dimension step: exact theorems, exact hypotheses, and their [RU] status

The note writes: "If `S` is metrizable — every candidate lamination is — subspace monotonicity of covering dimension in separable metric spaces (Hurewicz–Wallman, classical) gives `dim S ≥ n`; more generally, for compact Hausdorff `S` the cell image is closed and closed-subspace monotonicity in normal spaces applies."

The theorems actually being used are:

- **[RU-1]** *(Hurewicz–Wallman, "Dimension Theory", Princeton Univ. Press 1941, Theorem III 1.)* If `X` is separable metric and `A ⊆ X`, then `dim A ≤ dim X`. (Their `dim` is the small inductive dimension `ind`.)
- **[RU-2]** *(Brouwer; Hurewicz–Wallman Theorem IV 1.)* `dim [0,1]^n = n`.
- **[RU-3]** *(Coincidence theorem; Hurewicz–Wallman Theorem V 8, or Katětov–Morita for general metric spaces.)* For separable metric spaces, `ind = Ind = ` Čech–Lebesgue covering dimension.
- **[RU-4]** *(Monotonicity on closed subspaces of normal spaces; e.g. Engelking, "Theory of Dimensions Finite and Infinite", Thm 3.1.4.)* If `X` is normal and `A ⊆ X` is closed, then `dim A ≤ dim X` for the covering dimension.

**None of [RU-1]–[RU-4] has a source on disk.** I searched `fetched/`, `fetched-r2/` and `fetched-r3/` for Hurewicz, Wallman, Engelking, Nagata, Pears and "dimension theory"; the only hits are Lapidus's *complex fractal dimensions* volumes and unrelated titles. Under standing order 5 these carry **no weight**. This is finding **J4**.

**Three corrections of substance to the dimension sentence, independent of the [RU] issue:**

(α) "*If `S` is metrizable*" is not enough for [RU-1]: the theorem is for **separable** metric spaces. A compact metrizable space is separable, so the intended application (a lamination) is fine; the printed hypothesis is not. (Finding M7.)

(β) `S` in Theorem B is a *closed invariant subset*, not assumed compact. So the fallback "for compact Hausdorff `S` the cell image is closed and closed-subspace monotonicity in normal spaces applies" is the only branch of the note's argument that is self-contained — and it needs `S` compact Hausdorff, which is not part of Theorem B's hypotheses.

(γ) Post-repair the correct logical shape is: the cell is a **compact metrizable subspace** of `S` for every `n`; hence **any separable metrizable subspace `T ⊆ S` containing the cells has `dim T ≥ n`**; hence **no compact metrizable finite-dimensional `Y₀` can be such an `S`**. That last statement — the only one S4 needs — is the one to bank.

**And it can be obtained with no dimension theory at all**, by the route the adjudication opened: by (a), `S ⊇ Γ_{(p)}`, whose subspace topology is non-Hausdorff (§6.1), so `S` is not metrizable and in particular is no lamination. **Two independent routes to the same S4 conclusion, one of them entirely on-disk.** This is the repair I recommend the adjudicator adopt (§7, J4).

### 4.12 The scope notes (i)–(iii)

**(i) "For E strictly between E_f and E_max the cell characters Ψ_t (which have infinite kernel) *may* fall outside E."** — **Understated; the truth is definite.** (Finding M3.)

Compute `ker Ψ_t`. For `ζ · v ∈ μ × V`, `Ψ_t(ζv) = ι(ζ)e^{2πiλ_t(v)} = 1` iff `e^{2πiλ_t(v)} = ι(ζ)^{-1} ∈ μ(C)`, i.e. iff `λ_t(v) ∈ Q`, and then `ζ` is uniquely determined (`ι` is injective with image `μ(C)`). Hence

  `ker Ψ_t ≅ V₀ := λ_t^{-1}(Q) ⊆ V` (as abstract groups, via `v ↦ (ζ(v), v)`),

and `V₀` is a `Q`-subspace of `V` containing `ker λ_t`, which has codimension `≤ n`. Since `dim_Q V = ℵ₀`, `V₀` is an **infinite-dimensional `Q`-vector space**. Therefore:

- `ker Ψ_t` is infinite ⟹ `Ψ_t ∉ E_f`;
- `ker Ψ_t` is a nonzero divisible group ⟹ not finitely generated ⟹ `Ψ_t ∉ E_fg`;
- `ker Ψ_t ⊗ Q = ker Ψ_t` is infinite-dimensional ⟹ `Ψ_t ∉ E_fd`;
- for `E_fd0` (`x₀` = the generic point of `Spec Z`, `κ(x₀) = Q`): whatever splitting is chosen, for each prime `ℓ ∉ {ℓ_1,…,ℓ_n}` write `ℓ = ζ_ℓ · β(w_ℓ)` with `λ_t(w_ℓ) = 0`; then `Ψ_t(ℓ) = ι(ζ_ℓ)`, a **root of unity**, of some finite order `N_ℓ`, so `ℓ^{N_ℓ} ∈ ker Ψ_t ∩ Q^×`. These elements, over the infinitely many primes `ℓ ∉ {ℓ_i}`, are multiplicatively independent (§4.5), so `(ker Ψ_t|_{Q^×}) ⊗ Q` is infinite-dimensional ⟹ `Ψ_t ∉ E_fd0`.

**So the constructed cells lie outside every one of Deninger's named intermediate classes, for every choice of splitting.** Scope note (i)'s conclusion — that (b) as constructed needs `E = E_max` (`= E_tors` over `Spec Z`) or the unitary system — is therefore **correct and in fact forced**, and the word "may" should be replaced by "do".

*Does part (a) hold on the whole window?* **Yes.** Theorem A is proved for **any** admissible `E ⊆ E_max` (its only `E`-input is Def. 4.1's `ν`-closure plus membership of the limit character, automatic for `E ⊇ E_f` since the limit character is injective), and packets are full for `E ⊇ E_f` by Thm 5.2 (p. 34) and its restatement for `Γ` on p. 38 ("If e.g. `E_f ⊂ E` then `Γ^E_{x₀} = Γ_{x₀}`"). ✓ The note's claim is exact.

*Is a cell family available inside `E_f`?* Unitary characters of `Q̄^×` with **trivial** kernel do exist (choose `λ : V → R` injective with `λ(V) ∩ Q = 0`; then `ker Ψ = 1`, so `Ψ ∈ E_f`). But a *continuous n-parameter family* of them is another matter: along any line `t ↦ λ_0 + t·π_1` the condition `λ_t^{-1}(Q) = 0` fails on a **dense** (countable) set of `t`, so this construction yields no cube. I could neither build an `E_f`-cell nor rule one out; **I record it as open, and it is not needed** — (a) already kills the S4 count on the whole window.

**(ii) "The Hausdorffness hypothesis in (b) is on the subsystem, not on `X₀`."** — **Correct as a statement about the proof** (I certify this in §6.2: no step uses Hausdorffness of `X₀`), but **now superseded**: post-repair no Hausdorffness hypothesis is needed for the cell at all, and post-adjudication the hypothesis on `S` is *unsatisfiable* (§6.1). The note's added clause "every lamination in the sense of S4 is metrizable, so nothing is lost for the kill" is right, and it is what makes finding J2 non-fatal.

**(iii) "Classical inputs: CRT-density of `N` in `Ẑ_{(p)}`; direct-summand property of divisible subgroups; compact-to-Hausdorff homeomorphism criterion; subspace monotonicity of covering dimension. All standard; flagged for the referee."** — Three corrections:
1. The **direct-summand/uniquely-divisible** input is **on disk**, [x-03] p. 28 and (with the topology) p. 53. It should be cited, not flagged. (M4.)
2. **CRT-density** is elementary and is a computation, not a citation; it belongs to Theorem A, not to (b).
3. **Compact-to-Hausdorff** is no longer used after the repair (§4.10); what replaces it is [x-03] (51) p. 42 plus Cor. 7.8 p. 45 — both on disk.
4. Only the **dimension** inputs remain classical, and those must be labeled **[RU]** with no source on disk (J4).

**M9 (verification, not a defect).** Nothing in Theorem B(b) uses [r3s-08]. I read [r3s-08] pp. 17–18 (Thms 2.2.8/2.2.9) this session to confirm this: they state `Γ_p ≅ Ẑ^×_{(p)}/Np^Ẑ ×_{p^Ẑ} R⁺` as a "homeomorphism" and call the orbit decomposition one "into connected **closed** `R⁺`-orbits" — wording the adjudication (§4 item 4) already flagged as not readable as the subspace topology of `Γ_p ⊂ X₀`. **B(b) is clean of it.** Similarly [D25] (arXiv:2508.05329v1, *Rational Witt vectors and associated sheaves*) was opened and searched: it concerns sheaf-theoretic properties of `W_rat(O)` in Grothendieck topologies and contains nothing bearing on the topology or dimension of `X₀`. It carries no weight here, in either direction.

---

## 5. Attempts to break

Per instruction, for each identified soft spot I both tried to fill it and tried to break it. Two break attempts were serious.

### 5.1 Break attempt against the embedding (§4.10) — succeeds against `X₀`, fails against the cell

Before finding the proof of §4.10 I tried to construct a failure of the embedding directly: a sequence in `X₀` witnessing that `Θ(t)` and `Θ(t')` cannot be separated. **The construction succeeds** — and therefore proves something new about `X₀` (§8, N2) — **but it cannot be promoted to a failure of the embedding**, because the witnessing points lie off the cell. Here it is in full, because it is the sharpest available test of the theorem.

Notation as in §4.6. Take `n = 1` for clarity (the general case differs only in bookkeeping): `t = (t_1, t_2, …)`, `t' = t + δ e_1` with `δ ≠ 0`, both in `[0,½]^n`. Write `ψ := λ_{t'} − λ_t`, so `ψ(v) = δ·π_1(v)` where `π_1` is the `v_1`-coordinate functional on `V`.

Put `L_k := lcm(1, …, k)`. Choose a prime `p_k > max(k, k L_k³/δ)`, set

  `c_k := round(p_k δ / L_k²)`, `d_k := L_k c_k`, `n_k := p_k`, `m_k := n_k + d_k`, `r_k := m_k / n_k`, `e_k := n_k/d_k`.

Then, by direct computation:

- `r_k − 1 = d_k/n_k = L_k c_k/p_k ≈ δ/L_k → 0`, so `r_k → 1` in `R^{>0}`. ✓
- `|e_k δ − L_k| ≤ L_k³/(p_k δ) < 1/k → 0`. ✓ (Substitute `c_k = p_kδ/L_k² + θ`, `|θ| ≤ ½`.)
- `gcd(n_k, L_k) = 1` (as `p_k > k`), and `L_k | d_k`. ✓

Define `u_k ∈ Ẑ^×` by `u_k ≡ p_k^{-1}` in `Z_ℓ` for `ℓ ≤ k` and `u_k = 1` in `Z_ℓ` for `ℓ > k` (legitimate: `ℓ ∤ p_k` for `ℓ ≤ k`), and `a_k := n_k u_k ∈ Ẑ`. Then for every fixed `M` and every `k ≥ M`: `a_k ≡ 1 (mod M)` and `r_k a_k = m_k u_k = a_k + L_k c_k u_k ≡ 1 (mod M)` since `M | L_k`. So

  `a_k → 1` and `r_k a_k → 1` in `Ẑ`. ✓

Define `f_k : V → S¹` by `f_k(v) := exp(2πi(e_k ψ(v) + λ_t(v)))` — a homomorphism, since `e_kψ + λ_t` is `Q`-linear — and let `A_k := π(x_η, P_k)` where `P_k := ι^{a_k}` on `μ` and `f_k` on `V`. Then `P_k` is unitary; `ker(P_k|_μ) = ker(ι^{a_k})` has order `n_k`, finite, so `(Tors)` holds and `A_k ∈ X̊₀(C)_{E_max} ∩ X̊₀(S¹)`; and `a_k ∈ Ẑ`, so `A_k` is in the `ν = 1` stratum.

Now:

- **`A_k → Ψ_t`.** At roots of unity: `ι(ζ)^{a_k} → ι(ζ)` because `a_k → 1` in `Ẑ`. On `V`: for fixed `v`, write `ψ(v) = (A/B)δ`; for `k ≥ B` one has `B | L_k`, and `e_kψ(v) = (A/B)(L_k + η_k)` with `|η_k| < 1/k`, whose integer part `AL_k/B ∈ Z`; hence `e_kψ(v) → 0 (mod 1)` and `f_k(v) → e^{2πiλ_t(v)}`. Pointwise convergence on `Z̄` follows. ✓
- **`F_{r_k}(A_k) → Ψ_{t'}`.** Its `μ`-part is `ι^{r_k a_k} → ι` ✓; its `V`-part is `v ↦ f_k(r_k v) = f_k(v)·f_k(v/e_k) = f_k(v)·exp(2πi(ψ(v) + λ_t(v)/e_k)) → e^{2πiλ_t(v)}·e^{2πiψ(v)} = e^{2πiλ_{t'}(v)}` ✓ (using `e_k ψ(v/e_k) = ψ(v)` exactly, and `e_k → ∞`). Also `r_k a_k = m_k u_k ∈ Ẑ`, so `F_{r_k}(A_k)` is again in the `ν = 1` stratum. ✓

Set `z_k := q(A_k, 1) = q(F_{r_k}A_k, r_k^{-1})`. Then `(A_k, 1) → (Ψ_t, 1)` and `(F_{r_k}A_k, r_k^{-1}) → (Ψ_{t'}, 1)` (since `r_k → 1`), and `q` is continuous, so

  **`z_k → Θ(t)` and `z_k → Θ(t')` simultaneously, with `Θ(t) ≠ Θ(t')`.**

**What this does and does not show.** It shows `X₀` (and equally `Y₀^Den`, since every point above is unitary) is **not Hausdorff at the endpoints of the cell** — a fact about the char-0, unitary locus, entirely disjoint from the packets, and hence **new relative to the adjudication's §3** (§8, N2). It does **not** break the embedding, and the reason is exactly Step R2: the witnesses `z_k` are *not* points of the cell (their `μ`-parts are `a_k ∉ Ẑ^×·1`), and the identifications they use have `r_k = m_k/n_k ∉ N`. The subspace `Θ([0,½]^n)` is separated by the traces of the open sets `q(W₁ × (2/3,3/2))` even though every ambient neighbourhood pair meets. **Break attempt: failed against (b), successful against the ambient's Hausdorffness.**

### 5.2 Break attempt against the vacuity claim (J2)

Could some closed invariant `S` meeting every packet nevertheless be Hausdorff in its subspace topology — i.e. is the adjudication's non-Hausdorffness really *internal* to the packet? I re-derived the adjudication's construction independently (§6.1) and confirmed that **the convergent sequence and both of its distinct limits lie inside `Γ^E_{(p)}`**, hence inside `S`. So no. `S` is never Hausdorff. J2 stands. (This is what makes J1's repair necessary rather than cosmetic: without it, the printed first sentence would have no proof at all in the only regime where it is asserted.)

### 5.3 Break attempt against the priority finding (J3)

Could Deninger's "still infinite-dimensional" be a theorem elsewhere in [x-03] that I missed? I searched the full extraction for every occurrence of "dimension"/"dimensional" (25 hits) and read each in context, and I read §8 in full (pp. 49–53). The only relevant occurrences are the three assertions quoted in §7/J3 plus the definitions of `E_fd`, `E_fd0` and the "2 dim X₀ + 1" target. **There is no dimension-theoretic argument in the paper**: no covering dimension, no inductive dimension, no cell, no essential map, no reference to any dimension-theory source in the bibliography. J3 stands.

---

## 6. Interaction with G1 = NO (`X₀` non-Hausdorff along packets)

### 6.1 Independent re-derivation of the packet non-Hausdorffness, and its consequence for `S`

*(The adjudication decided G1 = NO in §3. Because finding J2 turns on it, I re-derived it rather than importing it.)*

Fix `p`, and `γ = {[P₀, w] : w ∈ R^{>0}}` with `P₀ = (x, χ^{a₀})`, `a₀ ∈ Ẑ^×_{(p)}`, as in Theorem A's normalization. Choose `[c] ≠ [a₀]` in `B_p = Ẑ^×_{(p)}/p^Ẑ` (possible: `B_p` is infinite). Let `n_k → c a₀^{-1}` in `Ẑ_{(p)}` (CRT) and `z_k := [P₀, n_k v]`.

- **Limit 1.** By Theorem A's Steps 3–6, `z_k = [F_{n_k}(P₀), v] → [(x, χ^c), v]`.
- **Limit 2.** `F_p(P₀) = (x, χ^{p a₀}) = (x, χ^{a₀} ∘ Frob) = P₀` in `X̊₀(C)`, because the Galois image in `Aut(κ(x)^×)` is `p^Ẑ` ([x-03] (34), p. 32). Hence `[P₀, p w] = [F_p(P₀), w] = [P₀, w]`, so the map `R^{>0} → X₀`, `w ↦ [P₀, w]`, factors through the circle `R^{>0}/p^Z`, and is continuous. Choose `j_k ∈ Z` with `p^{j_k} n_k v → w^*` in `R^{>0}` (possible by compactness of `R^{>0}/p^Z`, after passing to a subsequence). Then `z_k = [P₀, p^{j_k} n_k v] → [P₀, w^*] ∈ γ`.
- **Distinctness.** If `[(x,χ^c), v] = [P₀, w]` then `(x, χ^c)` and `P₀` lie in one `Q^{>0}`-orbit of `C_{(p)}`, hence in one fibre of the canonical fibration `C_{x₀} → Ẑ^×_{(p)}/p^Ẑ` ([x-03] p. 33: "the fibres are the `Q₀^{>0}`-orbits in `C_{x₀}`"), contradicting `[c] ≠ [a₀]`.

So one sequence has two distinct limits, **and the sequence and both limits lie in `Γ^E_{(p)}`**. Hence `Γ^E_{(p)}` is non-Hausdorff **in its subspace topology**, and so is every subspace of `X₀` containing it. ✓ **Independently confirmed.** By (a), every `S` satisfying Theorem B's hypotheses contains `Γ^E_{(p)}`. **Therefore the hypothesis of B(b)'s second sentence is satisfied by no `S` at all.** (Finding J2.)

### 6.2 Certification: the proof of (b) never uses Hausdorffness of `X₀`

Walking the proof step by step (as re-derived in §4):

| step | what it uses | Hausdorffness of `X₀`? |
|---|---|---|
| §4.1 `S ⊇` periodic points | Theorem A, Thm 5.2, Thm 6.1 | **no** |
| §4.2 `S ⊇ cl(P)` | `S` closed | **no** |
| §4.3 Thm 8.2 + subspace + suspend | Thm 8.2 (p. 50), p. 47, continuity of `q` | **no** |
| §4.4–4.6 the characters | pp. 27–29, 28/53 splitting | **no** |
| §4.7 `[Ψ_t,1] ∈ S` | above | **no** |
| §4.8 continuity of `Θ` | pp. 40, 42, 43, 47, 38 | **no** |
| §4.9 injectivity of `Θ` | Prop. 4.2 p. 27, `G`-fixedness of `ℓ_i` | **no** |
| §4.10 embedding (**repaired**) | Cor. 7.8 p. 45 (Hausdorffness of `X̊₀(C)`), (51) p. 42, `q` open | **no** — it uses Hausdorffness of the **leaf space `X̊₀(C)`**, which Deninger proves, never of `X₀` |
| §4.11 dimension | [RU-1]–[RU-4] + Hausdorffness/metrizability **of `S`** | **no** |

**Certified: no step of Theorem B(b), as printed or as repaired, uses Hausdorffness of `X₀`.** The note's scope note (ii) is correct on this point, and the repaired proof strengthens it: it uses no Hausdorffness of `S` either.

### 6.3 What survives of Corollary (i)/(ii) after G1 = NO

- **Corollary (i)** (uncountable per-prime orbit count kills the T1 coefficient-1 target and ALKL H4) rests on (a) alone. **Unaffected.** ✓
- **Corollary (ii)** (no compact finite-dimensional lamination `Y₀ ⊆ X₀`, closed and invariant, meeting every packet) is **true**, and now has **three** proofs, of which two are wholly on-disk:
  1. *(on-disk)* `Y₀ ⊇ Γ_{(p)}` is non-Hausdorff (§6.1), so `Y₀` is not metrizable, so it is no lamination. **No dimension theory, no cells.**
  2. *(cells + [RU] dimension theory)* repaired (b1) gives `n`-cells in `Y₀` for all `n`; `Y₀` compact metrizable ⟹ separable metric ⟹ `dim Y₀ ≥ n` for all `n` by [RU-1]/[RU-2]. **This route does not use G1.**
  3. *(probe B's Corollary B)* `Y₀ ⊇ cl(⋃Γ_p) = X̌₀(S¹)×_{Q^{>0}}R^{>0}`, plus Deninger's *assertion* that this is infinite-dimensional. **This route consumes an unproved assertion** — see J3, and the already-recorded Session-14 annotation in `probe-9.3-b.md` §5, with which I concur independently.

The note's own derivation of (ii) "by (b)" is *formally* valid even with a vacuous premise (assume such `Y₀`; it is Hausdorff; apply (b); contradiction), but it is **misleading**, because it presents the cells as the engine when in the post-adjudication landscape the elementary route 1 already fires. The replacement text in §7 (J2) fixes this.

---

## 7. FINDINGS, with severity and replacement text

### J1 — MAJOR. The n-cube claim is asserted unconditionally but proved only under a Hausdorff hypothesis.
**Location:** `probe-9.3-a.md` §3, Theorem B(b) first sentence; proof of (b), penultimate paragraph ("So `Θ` is a continuous injection … If `S` is Hausdorff …").
**Defect:** the printed first sentence has no proof; the only justification offered is a criterion whose hypothesis is stated in the *next* sentence (and, by J2, never holds).
**Repair (proved in §4.10):** replace the last paragraph of the proof of (b) by:

> **Θ is a homeomorphism onto its image, unconditionally.** First, `Θ̃ : [0,½]^n → X̊₀(C)_{E_max}`, `t ↦ Ψ_t`, is a continuous injection of a compact space into a metrizable — hence Hausdorff — space ([x-03] Cor. 7.8, p. 45, together with the paragraph on p. 47 giving `X̊₀(C)_E` the subspace topology), so `Θ̃` is a topological embedding. Second, if `P ∈ X̊(C)` has `P|_{μ(K)}` injective and `F_r(P) ∈ X̊(C)` for some `r = m/n ∈ Q^{>0}` in lowest terms, then `F_m(P) = F_n(F_r(P)) ∈ F_n(X̊(C)) = {R | R(μ_n(K)) = 1}` by [x-03] (51), p. 42; since `gcd(m,n) = 1`, `ζ ↦ ζ^m` is an automorphism of `μ_n(K)`, so `P(μ_n(K)) = 1`, so `n = 1` by injectivity of `P|_μ`; i.e. **`r ∈ N`**. Third, let `U ⊆ [0,½]^n` be open, pick `W₁` open in `X̌₀(C)_{E_max}` with `W₁ ∩ Θ̃([0,½]^n) = Θ̃(U)`, and put `W := W₁ × (2/3, 3/2)`. The quotient map `q` is open (saturations of opens are unions of homeomorphic translates, [x-03] Prop. 7.4 b, p. 43), so `q(W)` is open in `X₀`; and if `Θ(s) ∈ q(W)` then `(F_rΨ_s, r^{-1}) ∈ W` for some `r ∈ Q^{>0}`, whence `r ∈ N` by the second step and `r < 3/2` by the second coordinate, so `r = 1` and `s ∈ U`. Thus `q(W) ∩ Θ([0,½]^n) = Θ(U)`, i.e. `Θ` is open onto its image. Hence `Θ` is a topological embedding and `S` contains a subspace homeomorphic to the n-cube. **No Hausdorffness of `S` or of `X₀` is used.** The same argument applies verbatim in the unitary system `X̌₀(S¹) ×_{Q^{>0}} R^{>0}`, since (51) does not refer to `E`.

### J2 — MAJOR. The Hausdorff hypothesis in (b) is unsatisfiable; the printed second sentence is vacuous.
**Location:** `probe-9.3-a.md` §3, Theorem B(b) second sentence; Corollary (ii); scope note (ii); §0 item 1; §9 item 2.
**Defect:** by (a) every admissible `S` contains a full packet, whose subspace topology is non-Hausdorff (adjudication §3, re-derived here §6.1). So the class of `S` to which the printed second sentence applies is empty.
**Repair:** replace Theorem B(b) by:

> **(b)** Assume moreover `E = E_max` (equivalently `E_tors` over `Spec Z`, §1.2), or replace `X₀` by the unitary system `Y₀^Den = X̌₀(S¹) ×_{Q^{>0}} R^{>0}`. Then:
> **(b1)** For every `n ≥ 1`, `S` contains a subspace homeomorphic to the n-cube `[0,1]^n`. *(No Hausdorffness or metrizability hypothesis; see the proof.)*
> **(b2)** Consequently every **separable metrizable** subspace of `S` containing these cells has covering dimension `≥ n` for all `n` [RU: Hurewicz–Wallman, Dimension Theory, Thms III 1, IV 1, V 8 — no on-disk source, see §(iii)]. In particular **no compact metrizable finite-dimensional space can occur as such an `S`**: no compact finite-dimensional lamination `Y₀ ⊆ X₀` is closed, flow-invariant, and meets every packet.
> **Remark (post-adjudication).** The hypothesis "`S` Hausdorff in its subspace topology", under which an earlier version of (b) was stated, is in fact **satisfied by no `S` at all**: by (a), `S` contains a packet `Γ_{(p)}`, and the packet's subspace topology in `X₀` is non-Hausdorff (adjudication §3). This gives an **independent and more elementary proof of the same conclusion** — a lamination is compact metrizable, hence Hausdorff, hence cannot contain a packet — which does not use (b1) at all. (b1) remains the only *dimension*-theoretic statement, and it is the one that proves Deninger's printed assertion that `Y₀` "is still infinite-dimensional".

and replace Corollary (ii)'s "by (b)" by "by (b1)+(b2), or independently by the non-Hausdorffness of packets".

### J3 — MAJOR (priority; SO7). The conclusion of (b) for `Y₀` is asserted in print by Deninger, three times, without proof; only the *proof* and the *extension* are new.
**Location:** `probe-9.3-a.md` §0 item 1 ("the embedded half is KILLED, at referee grade (Theorems A and B below, **new**)"); §2 Remark (iv); §8 item 5 ("this note claims novelty for Theorems A, B, C"); §9 item 2.
**Evidence, verbatim and on disk:**
- [x-03] **p. 5**: "For all conditions E that we consider the space `X̌₀(C)_E` is infinite dimensional whereas ideally we would want it to be of dimension `2 dim X₀` …" and, four lines later, "The resulting dynamical system is still infinite dimensional."
- [x-03] **p. 49**: "In this section we will show that the system `Y₀` is still infinite-dimensional: Namely, for one-dimensional `X₀`, flat over spec Z and conditionally for all `X₀` we have `Y₀ = X̌₀(S¹) ×_{Q^{>0}} R^{>0}`."
- [x-06] **p. 12**: "The space `X₀^E` is infinite dimensional if `dim X₀ ≥ 1` and one could hope that the sub-dynamical system obtained as the closure of the union of all its compact orbits might be significantly smaller. However, this is not the case as follows from [Den22a, Theorem 8.2]."

In every case what is *proved* is the identification `Y₀ = X̌₀(S¹)×_{Q^{>0}}R^{>0}` (Theorem 8.2); the infinite-dimensionality is stated, never argued, and **no dimension-theoretic argument occurs anywhere in [x-03]** (§5.3).
**Repair:** insert after Theorem B(b) in the note:

> **Priority note.** The *conclusion* "`Y₀` is infinite-dimensional" is asserted without proof by Deninger at [x-03] p. 5 (twice), [x-03] p. 49, and [x-06] p. 12; [x-03] contains no dimension-theoretic argument. What is new here is therefore (i) a **proof** of that assertion — the explicit `n`-cells `Θ([0,½]^n) ⊆ X̌₀(S¹)×_{Q^{>0}}R^{>0}` — and (ii) the **extension** of the conclusion from `Y₀` to *every* closed flow-invariant `S ⊆ X₀` meeting every packet, which is Theorem A's contribution. The bare statement "`Y₀` is infinite-dimensional" must not be claimed as new.

and amend §0 item 1 and §9 item 2 accordingly.

### J4 — MAJOR (sourcing, SO5). The dimension inputs have no on-disk source and are unlabeled.
**Location:** proof of (b), last two sentences; scope note (iii); §0 ("KILLED, at referee grade"); §8 item 2 ("compact-to-Hausdorff and dimension monotonicity (classical)").
**Defect:** the note's own S4-relevant conclusion (Corollary (ii)) is asserted at referee grade while resting on classical dimension theory that this program has never verified on disk. `fetched/`, `fetched-r2/`, `fetched-r3/` contain no Hurewicz–Wallman, Engelking, Nagata or Pears.
**Repair:** replace scope note (iii) by:

> **(iii) Inputs, with their status.** (1) The splitting `Q̄^× = μ(Q̄) × V` with `V` a `Q`-vector space, and the induced *topological* product decomposition of the character space, are **printed in [x-03]** — proof of Lemma 4.3, p. 28, and proof of Prop. 9.1, p. 53 — and are cited, not assumed. (2) The embedding of the cube uses only [x-03] (51) p. 42, Prop. 7.4 b) p. 43, Cor. 7.8 p. 45 and the E-topology paragraph p. 47; compact-to-Hausdorff is used only against `X̊₀(C)`, which Deninger proves Hausdorff. (3) CRT-density of `N` in `Ẑ_{(p)}` (used in (a), not in (b)) is an elementary computation, done in full in §2. (4) **The dimension step alone is classical and unsourced on disk, and is therefore labeled [RU] and carries no weight:** Hurewicz–Wallman, *Dimension Theory* (Princeton, 1941), Thm III 1 (monotonicity of `dim` on subspaces of separable metric spaces), Thm IV 1 (`dim [0,1]^n = n`), Thm V 8 (`ind = Ind = ` covering dimension for separable metric spaces); and, for the closed-subspace version, monotonicity of covering dimension on closed subspaces of normal spaces (Engelking, *Theory of Dimensions*, Thm 3.1.4). **Until a dimension-theory source is on disk, the S4 conclusion should be quoted through the packet-non-Hausdorffness route of the adjudication, which is entirely on-disk.**

**Action item for the sponsor/orchestrator:** fetch Hurewicz–Wallman (1941) or Engelking (1978/1995) before any external circulation of a claim of the form "`Y₀` is infinite-dimensional".

### M1 — MINOR. Prop. 4.2 cited for a topological statement.
**Location:** proof of (b), injectivity paragraph: "Since the colimit is along injections F_ν ([x-03] Prop. 4.2, p. 27), each stratum embeds".
**Replacement:** "Since the colimit is along injections `F_ν` (set-theoretic injectivity: [x-03] Prop. 4.2, p. 27, last sentence), the canonical map `X̊₀(C) → X̌₀(C)` is injective, so equality holds already in `X̊₀(C)`. (That the strata are *topologically* embedded — indeed open, and closed — is [x-03] Prop. 7.4 a), p. 43, together with the paragraph on p. 47; that is not needed here.)"

### M2 — MINOR. "the system in which [x-03] §8 operates" mis-describes §8.
**Location:** Corollary (ii): "For E = E_max (= the system in which [x-03] §8 operates)".
**Fact:** §8 opens "In this section C denotes the complex number field, and we take `N₀ = N`" and works in the **unrestricted** `X̌(C)`/`X̌₀(C)`; Theorem 8.2 carries no `E`. Per p. 5, `Y₀` is "the closure of the union of all periodic orbits of `X̌₀(C)_E` **in `X̌₀(C)`**", and equals `X̌₀(S¹)×_{Q^{>0}}R^{>0}`, which is contained in no `E_max`-locus (a unitary character may kill infinitely many roots of unity and then fails (Tors)).
**Replacement:** "For `E = E_max` and, separately, for the unitary system `Y₀^Den = X̌₀(S¹)×_{Q^{>0}}R^{>0}` in which [x-03] §8's Theorem 8.2 is stated (§8 works in the unrestricted `X̌₀(C)`; the closure defining `Y₀` is taken there, [x-03] p. 5)".

### M3 — MINOR. Scope note (i) understated.
**Replacement:** "For every `E` with `E_f ⊆ E ⊆ E_fd0` — that is, for `E_f`, `E_fg`, `E_fd`, `E_fd0`, every named intermediate class of [x-03] p. 29 — the cell characters `Ψ_t` **do** fall outside `E`, for every choice of splitting: `ker Ψ_t ≅ λ_t^{-1}(Q)` is an infinite-dimensional `Q`-vector space, and `ker(Ψ_t|_{Q^×})` contains `ℓ^{N_ℓ}` for every prime `ℓ ∉ {ℓ_1,…,ℓ_n}`, `N_ℓ` the order of `ι(ζ_ℓ)`, hence has infinite `Q`-rank. So (b) as constructed is available exactly for `E = E_max` (`= E_tors` over `Spec Z`) and for the unitary system. Whether some *other* cell family lives in a smaller admissible class is open and is not needed: part (a) already kills the S4 count on the whole window `E_f ⊆ E ⊆ E_max`."

### M4 — MINOR. The splitting is on disk and should be cited.
**Replacement:** in the proof of (b), after "Write `Q̄^× = μ(Q̄) × V` with `V` uniquely divisible", insert: "(this splitting, and the fact that the quotient is a `Q`-vector space, are Deninger's own: [x-03] proof of Lemma 4.3, p. 28; the induced **topological** isomorphism `Hom(κ^×, C^×) ≅ Hom(μ(κ), C^×) × Hom(κ^×⊗Q, C^×)` is [x-03] proof of Prop. 9.1, p. 53, and gives the continuity of `t ↦ Ψ_t` at once)".

### M5 — MINOR. (Tors) quoted without its `∈ N₀` clause.
**Location:** note §1.2, "and (Tors) (finite kernel on roots of unity)".
**Replacement:** "and (Tors): `ker(χ)_tors = ker(χ|_{μ(κ)})` is finite **and** `|(ker χ)_tors| ∈ N₀` ([x-03] p. 27)". *(Immaterial here — `N₀ = N` in §8 and the cell characters have `|ker_tors| = 1` — but the second clause must travel with the first whenever `N₀ ⊊ N`.)*

### M6 — MINOR. Two elisions in the independence argument.
**Replacement:** "…their `V`-components `v_1, …, v_n` are `Q`-linearly independent: a `Q`-relation `∑ q_i v_i = 0` clears denominators to a `Z`-relation `∑ k_i v_i = 0`, i.e. `∏ ℓ_i^{k_i} ∈ μ(Q̄) ∩ Q^× = μ(Q) = {±1}`; the left side is positive, so it is 1, and unique factorization forces `k = 0`." Also: `V` has **countably infinite** dimension, not merely "countable dimension".

### M7 — MINOR. Metrizable is not enough; separable metrizable is needed.
**Replacement:** "If `S` is **separable** metrizable — every compact metrizable candidate lamination is — then [RU] monotonicity of covering dimension on subspaces of separable metric spaces gives `dim S ≥ n`."

### M8 — MINOR. "Hence" hides the theorem.
**Replacement:** in the statement of (b), "…contains, for every `n ≥ 1`, a subspace homeomorphic to `[0,1]^n`. Hence, **by monotonicity of covering dimension** [RU], every separable metrizable subspace of `S` containing them has `dim ≥ n` for all `n`; in particular no such subspace is finite-dimensional." (Also spell "covering dimension" once, and prefer "`dim S = ∞`" to "is infinite-dimensional" where a definite invariant is meant.)

### M9 — verification, no defect.
Nothing in B(b) uses [r3s-08] (checked at pp. 17–18) or [D25] (checked). Recorded so the adjudicator need not re-check.

---

## 8. New results established in the course of this pass

**N1 (repairs J1, and strengthens the theorem).** *For `X₀ = Spec Z`, `E = E_max`, and equally for the unitary system `X̌₀(S¹) ×_{Q^{>0}} R^{>0}`, the map `Θ : [0,½]^n → X₀`, `t ↦ [Ψ_t, 1]`, is an **open** injection onto its image, hence a topological embedding — with no Hausdorffness or metrizability hypothesis on the ambient or on `S`.* Proof: §4.10. Inputs: [x-03] (51) p. 42, Prop. 7.4 b) p. 43, Cor. 7.8 p. 45, p. 47. This is what makes Theorem B(b)'s first sentence a theorem.

**N2 (new negative structural datum about `X₀`).** *`X₀` — and the unitary system `Y₀^Den` — is non-Hausdorff **in the characteristic-0 unitary locus**, not only along packets: for `t ≠ t'` in `[0,½]^n` differing in a single coordinate, there is an explicit sequence `z_k ∈ X₀` with `z_k → [Ψ_t,1]` and `z_k → [Ψ_{t'},1]`.* Proof: §5.1, fully elementary (lcm's, one prime per step, no equidistribution). This extends the adjudication's §3 (non-Hausdorffness along packets) to a locus disjoint from the packets, and it removes any temptation to read the packet phenomenon as an artifact of finite residue fields. Its mechanism is the same one Deninger flags at [x-03] p. 48: "The `Q^{>0}`-action on `Ȟ_{E_tors} × R^{>0}` is **not properly discontinuous**."

**N3 (program consequence, addressed to the adjudicator).** N1 and N2 together say: **a non-Hausdorff ambient does not prevent Hausdorff compact invariant-free subspaces**, and indeed `X₀` contains compact cube-subspaces at points where it is not Hausdorff. This is directly relevant to the adjudication's residual question **Q-a** ("Does `X₀` contain a compact, Hausdorff-in-its-subspace-topology, flow-invariant subspace `Y` — necessarily not closed — of topological dimension 3, meeting each packet in exactly one orbit?"). N1/N2 show that the *Hausdorff-in-itself* clause of Q-a is **not** obstructed by the ambient's non-Hausdorffness in general; any kill of Q-a must come from the flow-invariance and the packet-meeting clause, not from point-set topology. Conversely, the packets themselves are non-Hausdorff (§6.1), so a Q-a witness must meet each packet in **one orbit only** — which is exactly what Q-a asks, and the two-limit construction of §6.1 does not apply to a single orbit. **Q-a is not decided by anything in this report, and should not be recorded as leaning either way on account of non-Hausdorffness.**

---

## 9. What is now established at referee grade, and its precise scope

**Established, line by line, from the printed sources, with no hypothesis beyond those stated:** let `X₀ = Spec Z`, `N₀ = N`, `C = ℂ`, and let `S ⊆ X₀ = X̌₀(C)_{E_max} ×_{Q^{>0}} R^{>0}` be closed and flow-invariant and contain at least one periodic orbit over every prime. Then `S` contains every periodic point ([x-03] Thm 6.1 p. 39 + Theorem A + Thm 5.2 p. 34), hence the closure of the periodic set, which by [x-03] Thm 8.2 (p. 50 — **unconditional for `Spec Z`**, since `dim Spec Z = 1` and `char Q = 0`, the [Per11, Thm 1] case being the one that applies) contains `[Ψ, v]` for every unitary generic-fibre character `Ψ` satisfying (Tors) and every phase `v`; and the explicit family `Ψ_t`, `t ∈ [0,½]^n`, built from the splitting `Q̄^× = μ(Q̄) × V` ([x-03] pp. 28, 53) and the `Q`-independence of the `V`-components of `n` distinct rational primes, gives a map `Θ : [0,½]^n → S` which is continuous (pointwise-convergence topology p. 40, `G`-quotient p. 42, colimit p. 43, `E`-subspace p. 47, suspension quotient p. 38), injective (Prop. 4.2 p. 27 plus `G`-fixedness of the rational primes and the range `[0,½]`), **and an open map onto its image (this report, §4.10, via [x-03] (51) p. 42 and Cor. 7.8 p. 45)** — hence a topological embedding. **Therefore `S` contains a subspace homeomorphic to `[0,1]^n` for every `n ≥ 1`, unconditionally, and the same holds in Deninger's unitary system `X̌₀(S¹) ×_{Q^{>0}} R^{>0}`.** The **scope** of this is exactly: `E = E_max` (`= E_tors` over `Spec Z`) or the unitary system — for `E_f`, `E_fg`, `E_fd`, `E_fd0` the cells provably lie outside `E` (§4.12) — and it is a statement about `S` **containing cells**, not yet about `dim S`: the passage from "cells of every dimension" to "`dim S = ∞`" is classical dimension theory ([RU-1]–[RU-4]) for which **this program has no source on disk**, so at referee grade the infinite-dimensionality conclusion is available only for **separable metrizable** subspaces and only modulo [RU]. The S4-relevant corollary — *no compact finite-dimensional lamination is a closed flow-invariant subset of `X₀` meeting every packet* — stands, and now has an entirely on-disk proof that needs neither cells nor dimension theory (`S ⊇ Γ_{(p)}` is non-Hausdorff, §6.1), as well as the cell proof, which is the only one independent of the adjudicated G1 = NO. Finally, and this is the priority statement required by standing order 7: **the conclusion for Deninger's own `Y₀` is asserted in print three times without proof ([x-03] pp. 5, 49; [x-06] p. 12) and [x-03] contains no dimension argument anywhere — so what this note contributes is the proof and the extension to arbitrary closed invariant `S`, not the assertion.**

---

## 10. Sources — every page read this session

**[x-03] C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400**v4**, on disk as `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` (120 pp.; printed page = PDF page, calibrated at pp. 2, 5, 27, 50).** Pages read in full this session:
- **p. 2** (calibration), **p. 5** (intro: "For all conditions E … infinite dimensional"; "The resulting dynamical system is still infinite dimensional"; "a minimal condition E … does not look natural").
- **p. 23** (Remark 3.4: identification of `X̊(C)` with multiplicative maps; `P^σ = P ∘ σ`).
- **p. 27** ((Tors); (Image); Definition 4.1; Proposition 4.2 — "The monoid N₀ acts by injections"; maps `pr_X`, `pr_{X₀}` (30)–(31)).
- **p. 28** (Lemma 4.3 and its proof — the splitting `k^× ≅ μ(k) × (k^×/μ(k))`, uniquely divisible, `Q`-vector space; Corollary 4.4; Examples `E_tors`, `E_max`).
- **p. 29** (Examples `E_f`, `E_fg`, `E_fd`, `E_fd0`; the chain `E_f ⊂ E_fg ⊂ E_fd ⊂ E_fd0 ⊂ E_max ⊂ E_tors`; the "not `N`-invariant" remark; stability; Prop. 4.5).
- **p. 30** (Prop. 4.5 proof; Lemma 4.6).
- **p. 31** (Lemma 4.6 proof; §5 opening; "Fix an injective homomorphism `ι : μ(K) ↪ μ(C)`"; (32); (33)).
- **p. 32** ((34) `N x₀^Ẑ = Gal(κ(x)/κ(x₀)) ↪ Aut(κ(x)^×) = Ẑ^×_{(p)}`; (35); (36); (37); (38)).
- **p. 33** ((39); the fibration `C_{x₀} → Ẑ^×_{(p)}/p^Ẑ` "and the fibres are the `Q₀^{>0}`-orbits"; (40); (41) `ρ`; (42)–(46)).
- **p. 34** (Prop. 5.1 with proof; **Theorem 5.2** including "If e.g. `E ⊃ E_f` then `C^E_{x₀} = C_{x₀}`").
- **p. 38** (§6: the suspension `X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0}`, the action `(P₀,u)q = (F_q(P₀), q^{-1}u)`, the flow, `Γ_{x₀}`, the packet fibration, "If e.g. `E_f ⊂ E` then `Γ^E_{x₀} = Γ_{x₀}`").
- **p. 39** (**Theorem 6.1**; the "packets" paragraph; the `X₀(C) × R^{>0} → X₀` immersion discussion).
- **p. 40** (Deninger's question "Is there a sub-dynamical system `Y₀ ⊂ X₀` … or at least one which maps to `X₀` …"; §7 opening: pointwise-convergence topology, metrizability of `X̊(C)`; Lemma 7.1).
- **pp. 41–42** (Lemma 7.2; the topology on non-affine `X̊(C)`; `X̊₀(C) = X̊(C)/G` quotient topology; **Lemma 7.3 with (51) `F_ν(X̊(C)) = {P | P(μ_ν(K)) = 1}`**).
- **p. 43** (the colimit topology; **Proposition 7.4** a), b), c); `X̌₀(C) = X̌(C)/G`; `π`, `π̌` continuous **and open**).
- **p. 44** (Prop. 7.5; Prop. 7.6 — `G`-invariant metric, second countable, separable; Prop. 7.7).
- **p. 45** (**Corollary 7.8** — `X̊₀(C)` metrizable, separable, Hausdorff; **Corollary 7.9**).
- **pp. 46–47** (the Remark on separated `X₀`; Theorem 7.10 and its Remarks 1–2 — "The continuous bijections in Theorem 7.10 are not homeomorphisms in general"; **the E-topology paragraph**: "They agree with the subspace topologies … because the subspaces `F_ν^{-1}X̊(C)` and `F_ν^{-1}X̊₀(C)` are open"; "All preceding results in this section remain true if we replace `X̊(C)` etc. by `X̊(C)_E` etc.").
- **p. 48** (`Ȟ_{E_tors}`, (62)–(66); "**The `Q^{>0}`-action on `Ȟ_{E_tors} × R^{>0}` is not properly discontinuous.**").
- **p. 49** ((67)–(68); **§8 opening**: "`X₀ = X̌₀(C) ×_{Q^{>0}} R^{>0}` is infinite dimensional"; "we will show that the system `Y₀` is still infinite-dimensional: Namely … `Y₀ = X̌₀(S¹) ×_{Q^{>0}} R^{>0}`"; Claim 8.1 statement begins).
- **p. 50** (Claim 8.1 conditions 1)–3); "If `dim A = 0` … trivially"; "**This follows from [Per11, Theorem 1]**"; `X̌(C)_per` definition; **Theorem 8.2** — *read both from the text layer and from the rendered page image*, confirming the closure bars `cl(X̌(C)_per) = X̌(S¹)`, `cl(X̌₀(C)_per) = X̌₀(S¹)`; the proof; **Lemma 8.3** with "character … **with finite kernel**").
- **pp. 51–53** (proof of Thm 8.2 from Lemma 8.3; proof of Lemma 8.3 including "By assumption we may apply Claim 8.1 to our ring `A`" and `dim A = dim R̄₀ ≤ dim X₀`; end of the proof on p. 53; **§9 Prop. 9.1 proof, p. 53 — the splitting `β` and the "topological isomorphism of groups" `Hom(κ^×, C^×) ≅ Hom(μ(κ), C^×) × Hom(κ^× ⊗ Q, C^×)`**).
- **Bibliography**: "[Per11] Antonella Perucca. On the reduction of points on abelian varieties and tori."
- Exhaustive keyword search over the whole extraction for "dimension"/"dimensional" (25 occurrences, each read in context) to establish that **no dimension-theoretic argument occurs in the paper**.

**[x-06] C. Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf` (17 pp.).**
- **p. 11** (Theorem 4.1; "the infinite dimensional connected Hausdorff space `W_rat(spec Z)(C)`"; the admissibility paragraph; "For example `E` can be the conditions that `ker P^×` is always finite resp. finitely generated"; Theorem 4.2).
- **p. 12** (the packet paragraph; Theorem 4.3; "**The space `X₀^E` is infinite dimensional if `dim X₀ ≥ 1` … However, this is not the case as follows from [Den22a, Theorem 8.2].**").

**[r3s-08] M. Morishita, arXiv:2508.15971**v5**, `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`.** Pages **17–18** (Thms 2.2.8(1)(2), 2.2.9(1)(2): the "homeomorphism" wording and "decomposition into connected **closed** `R⁺`-orbits"; §2.3 opening). Read only to certify that **B(b) does not use it** (M9).

**[D25] C. Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1, `fetched-r3/r3s-22-…-SESSION8-FETCH.pdf`.** Title page and introduction read; whole extraction searched for "dimension", "Hausdorff", "topolog". Content is `W_rat(O)` as a (pre)sheaf in subcanonical and non-subcanonical Grothendieck topologies. **No bearing on this item, in either direction.**

**Program files read in full:** `results/c3-r/probe-9.3-adjudication.md`; `results/c3-r/probe-9.3-a.md`; `results/corpus-routing.md` header caveats 1–20 and the `x-03`/`r3s-08` routing lines; `results/c3-r/probe-9.3-b.md` §§0–8 (for the cross-check behind §6.3 route 3).

**Not on disk, labeled [RU], carrying no weight:** Hurewicz–Wallman, *Dimension Theory* (Princeton, 1941), Thms III 1, IV 1, V 8; Engelking, *Theory of Dimensions Finite and Infinite*, Thm 3.1.4; the standard definition of a Riemann-surface lamination as a compact metrizable foliated space ([Ghy99]).

— end of referee report —
