# S14 PROBE — Q* face (a), BUILD direction: the cut suspensions X₀^{E(a)} and the subspace face of S4

**Program:** RH program, direction C3-r, milestone M2c, Route 2, blocker S4. **Date:** 2026-09-02 (Session 14).
**Charter:** try to prove YES on Q-a by construction; first candidate = the cut suspensions X₀^{E(a)} of probe A's Theorem C(b). Determine (1) compactness, (2) Hausdorffness in the subspace topology, (3) topological dimension, (4) whether each packet is met in exactly one orbit for every choice of a. If the candidate fails, say exactly which property fails and why, as a theorem where possible.
**Author:** s14 Q-a build probe (independent; wrote nothing into any existing file).

---

## 0. VERDICT (stated first): **THEOREM (NO)** — Q-a is dead, unconditionally, and for a reason strictly stronger than the one the question anticipated

The construction fails, and it fails on clause **(2)**, catastrophically and provably. The exact statements established below:

> **Theorem 1 (packet indiscreteness).** Let X₀ = spec ℤ, let E be any admissible class of characters ([x-03] Def. 4.1, p. 27) with E ⊆ E_max, and let **X₀ = X̌₀(ℂ)_E ×_{ℚ^{>0}} ℝ^{>0}** be the suspension with its quotient topology ([x-03] §6 p. 38, §10 p. 63). Fix a prime p and let z, z′ be **any two points of the packet Γ^E_{(p)}**. Then z′ ∈ cl_{X₀}({z}). Equivalently: all points of a packet are topologically indistinguishable in X₀; **Γ^E_{(p)} carries the indiscrete topology as a subspace of X₀**; in particular **X₀ is not a T₀ space**, and its periodic orbits are indiscrete subspaces.

> **Corollary 1.2 (Q-a: NO).** There is **no** flow-invariant subspace Y ⊆ X₀ which is T₀ — a fortiori none which is Hausdorff — in its subspace topology and which meets even one packet in a full orbit. Since any S4 substrate in the subspace reading must contain, for every prime p, one periodic orbit inside Γ_{(p)}, and every periodic orbit is an infinite indiscrete subspace, **face (a) of Q\* has answer NO**. The answer is unconditional: it holds for every admissible E (certified E ⊇ E_f, E_max, E_tors, and every cut class E(a) alike), for the unitary system X̌₀(S¹) ×_{ℚ^{>0}} ℝ^{>0}, and it needs **no** hypothesis of compactness, dimension, metrizability or closedness. Compactness and dimension are therefore *moot* for Q-a; they are answered below anyway, as the charter asks.

The cut suspensions specifically:

| Charter question | Answer for X₀^{E(a)} | Grade |
|---|---|---|
| (1) compact? | **NO** for the minimal cut E(a) (empty in characteristic 0): X₀^{E(a)} is the topological coproduct ⨆_p γ_p of countably many pairwise clopen pieces (Prop. 7.1 + Cor. 7.2). **Undetermined** for the enlarged cut E(a)′ (generic stratum retained), and for X₀ and Y₀^Den themselves — [x-03] asserts compactness of neither (§7.3). | theorem / open |
| (2) Hausdorff in the subspace topology? | **NO**, in the strongest possible way: each γ_p is *indiscrete* (Theorem 1). This answers the adjudication §7 item "Hausdorffness of the CUT suspensions X₀^{E(a)}" — the last Hausdorff question with S4 relevance — in the negative. | theorem |
| (3) topological dimension? | **0**, not 3, for the minimal cut: covering, small- and large-inductive dimension all vanish because the space is a coproduct of indiscrete pieces (Cor. 7.3). Every packet Γ^E_{(p)} ⊂ X₀, in any E, likewise has covering dimension 0. | theorem |
| (4) exactly one orbit per packet, for **every** choice of a? | **YES.** E(a) is admissible, Γ^{E(a)}_{(p)} is a single circle of length log p for every prime and every choice a = (a₀(p))_p, and by [x-03] Thm. 6.1 these are *all* the periodic orbits of X₀^{E(a)} (§5). This is the one clause that survives — and it survives for the minimal and the enlarged cut alike. | theorem |

**Net effect on the program.** Q\*'s face (a) is closed NO; face (b) (the mapping face) is **untouched** and remains the unique survivor of S4, exactly as the adjudication's delineation predicted (Theorem 1 makes the *target* coarser, which can only help a map into it — §9). The kill-criterion therefore still does **not** fire. Theorem 1 also **subsumes and strengthens** three banked items (Theorem A, Cor. A.2/row W12, and the closed-half kill) and **voids** one referee-pending item (probe A's Theorem B(b), whose Hausdorff hypothesis is now provably unsatisfiable) — see §8.

Nothing here is rounded up: what is proved is a *negative* theorem about the subspace face plus a *positive* set-level construction (clause (4)) that is not a substrate.

---

## 1. Sources read this session, with locations

All page numbers are the **printed** pages of the on-disk PDF; the text was extracted fresh this session with `pdftotext -layout` and every passage quoted below was read verbatim in that extraction. Nothing in §§2–7 is used from memory.

**[x-03]** C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`. Read this session:

| Item | Printed page | What was read |
|---|---|---|
| Def. of X̊(ℂ), the G-action and the N-action | p. 22 | "We define X̊(C) to be the set of pairs (x, P^×) where x ∈ X and P^× : κ(x)^× → C^× is a homomorphism… (x,P^×)σ = (x^σ, P^× ∘ σ) … **F_ν(x,P^×) = (x, P^× ∘ ( )^ν)** for ν ∈ N." |
| Remark 3.4 (points as multiplicative maps) | p. 23 | "we will identify the points (x,P) of X̊(C) with the multiplicative maps P : R → C satisfying … 1) P(0)=0, P(1)=1. 2) p := P^{-1}(0) is additively closed and hence a prime ideal. 3) We have a factorization P : R → R/p → C." |
| (Tors), (Image), **Def. 4.1** (admissible class), Prop. 4.2 | p. 27 | "A class E of characters χ : κ^× → C^× … is (N₀−)admissible if for any σ ∈ Autκ resp. ν ∈ N₀ the character χ is in E **if and only if** χ∘σ resp. χ_ν = χ∘( )^ν is in E. Moreover the characters in E should satisfy (Tors)." Prop. 4.2: X̊(ℂ)_E is G-invariant and forward/backward N₀-invariant; N₀ acts by injections. |
| Examples E_tors, E_max, E_f, E_fg, E_fd, E_fd0 | p. 28 | verbatim list |
| (32) reduction isomorphism i_x : μ^{(p)}(K) ≅ κ(x)^× | p. 31 | verbatim |
| (34) Gal(κ(x)/κ(x₀)) = Nx₀^Ẑ ↪ Aut(κ(x)^×) = Ẑ^×_{(p)}; (35) the (a,ν)-parametrization and its fibres | p. 32 | verbatim |
| (38), (39), (40): C_{x₀} ≅ (Ẑ^×_{(p)}/Nx₀^Ẑ) ×_{p^ℤ} ℚ^{>0}; "The set C_{x₀} fibres over the compact group Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p)^, **and the fibres are the ℚ^{>0}-orbits in C_{x₀}**"; the canonical projection (40) | p. 33 | verbatim |
| Prop. 5.1 (ρ = 1 ⟺ injective on μ(κ(x))) | p. 34 | verbatim |
| **Thm. 5.2**: the isotropy decomposition; "For any point P₀ ∈ C^E_{x₀} the isotropy group of P₀ is (ℚ^{>0}_0)_{P₀} = Nx₀^ℤ"; "If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}" | p. 34 | verbatim |
| Suspension: X₀ = X̌₀(ℂ)_E ×_{ℚ^{>0}_0} ℝ^{>0}, "(P₀,u)q = (P₀q, q^{-1}u) = (F_q(P₀), q^{-1}u)", the flow φ^t, Γ_{x₀} = C_{x₀} ×_{ℚ^{>0}_0} ℝ^{>0}, "The ℚ^{>0}_0-**bijection** (39) induces an ℝ^{>0}-**bijection**", "all ℝ^{>0}-orbits in Γ_{x₀} are circles ℝ^{>0}/Nx₀^ℤ and Γ_{x₀} fibres over Ẑ^×_{(p)}/p^Ẑ with fibres the ℝ^{>0}-orbits" | p. 38 | verbatim |
| **Thm. 6.1** (periodic points = ⨿_{x₀} Γ^E_{x₀}; isotropy Nx₀^ℤ) | p. 39 | verbatim |
| The S4 question ("Is there a sub-dynamical system Y₀ ⊂ X₀ … or at least one which maps to X₀ …") | p. 40 | verbatim |
| §7 opening: the topology of pointwise convergence, Tychonov, metrizability | p. 40 | verbatim |
| Lemma 7.1 (pr_X continuous) | p. 40 | verbatim, with proof |
| Lemma 7.3 + (51): F_ν continuous, **closed and open**; F_ν(X̊(ℂ)) = {P : P(μ_ν(K)) = 1} is closed and open | p. 42 | verbatim, with proof |
| **Prop. 7.4**: (a) X̊(ℂ) is a **closed and open** subspace of X̌(ℂ); (b) F_q is a **homeomorphism** of X̌(ℂ) for every q ∈ ℚ^{>0}_0; (c) G acts by homeomorphisms. The projections π̌ are continuous **and open** | p. 43 | verbatim, with proof |
| **Cor. 7.8** (X̊₀(ℂ) metrizable, δ(π(P),π(P′)) ≤ d(P,P′)), **Cor. 7.9** (X̊(ℂ), X̊₀(ℂ), X̌(ℂ), X̌₀(ℂ) Hausdorff for X₀ with an ample invertible sheaf) | p. 45 | verbatim, with proofs |
| **Thm. 7.10** + Remark 2 ("The continuous bijections in Theorem 7.10 are **not homeomorphisms in general**") | pp. 46–47 | verbatim |
| E-subspace topologies: "we equip X̊(ℂ)_E and X̊₀(ℂ)_E with the subspace topologies … They agree with the subspace topologies via X̌(ℂ)_E ⊂ X̌(ℂ) and X̌₀(ℂ)_E ⊂ X̌₀(ℂ) because the subspaces F_ν^{-1}X̊(ℂ) and F_ν^{-1}X̊₀(ℂ) are open" | p. 47 | verbatim |
| (66)–(68), and "**The ℚ^{>0}-action on Ȟ_{E_tors} × ℝ^{>0} is not properly discontinuous. In section 10, we will see that this works to our advantage.**" | pp. 48–49 | verbatim |
| §8 opening ("the dynamical system X₀ … is infinite dimensional … we will show that the system Y₀ is still infinite-dimensional"), Claim 8.1, and its status for number rings via [Per11, Thm 1] | pp. 49–50 | verbatim |
| **Thm. 8.2** (X̌(ℂ)_per‾ = X̌(S¹), X̌₀(ℂ)_per‾ = X̌₀(S¹)) and its proof, incl. "Since X̊(S¹) is closed in X̊(ℂ) the subspace X̌(S¹) is closed in X̌(ℂ)" | p. 50 | verbatim |
| **Thm. 9.6's proof**: "We will show below that the only open sets of Y are ∅ and Y … **The fact that Y carries the coarse topology follows from strong approximation for ℚ** … (excluding the infinite place, i.e. the Chinese remainder theorem)", for Y = ℚ^{>0}_0Ẑ^×/ℚ^{>0}_0 | p. 62 | verbatim, with proof |
| Cor. 9.7 (X and X₀ connected for E ⊃ E_f) | p. 62 | verbatim |
| §10: Def. 10.1; "**Note that in general the continuous bijection π|_{M×{u}} : M×{u} → π(M×{u}) will not be a homeomorphism if π(M×{u}) is equipped with the subspace topology of X.**"; "If Q acts properly discontinuously … then F is an actual 1-codimensional foliation. In general however the partition of X … **will not be locally trivial**." | p. 63 | verbatim |
| Thm. 10.2 (H⁰_F = ℝ) | p. 64 | verbatim, with proof |
| **Prop. 10.3** (Y = ℚ^{>0}_0Ẑ^× ×_{ℚ^{>0}_0} ℝ^{>0} is irreducible) and its **Remark**: "By [LR00, Lemma 3.1], the orbits of the ℚ^{>0}-action on ℚ^{>0}Ẑ^× × ℝ^{>0} are **closed** … it follows that the points of Y are closed, i.e. **Y is a T₁-space**." | p. 64 | verbatim |

**[x-06]** C. Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf` — §4 (Thm. 4.2's "compact subsets Γ_{x₀}", the packet paragraph) consulted for the wording of the packet statement only; nothing load-bearing.

**Program-internal, read in the order the charter prescribes** (used as *context and bookkeeping*, never as a substitute for a source): `results/c3-r/probe-9.3-adjudication.md` (binding; §2 anchors, §4 banked, §5 Q\*, §7 the open items), `probe-9.3-a.md` (Thms A, B, C; §4.1 reachability; §6–§7), `probe-9.3-b.md` (Thm A, Cors A.1–A.3, B; §6–§7), `probe-9.4-note.md` (Lemmas A–D, Prop. 1, Roads 1–3, DQ-M), `m2c-feasibility-ledger.md` (§5 rows, §8 Route 2, §9, §12 addendum), `s2-feasibility-note.md` (W3, model world), `directions/C3-geometric-substrate.md` ("Current frontier"), `results/corpus-routing.md` header caveats.

**Not cited for topology, per adjudication §4 item 4:** [r3s-08] Morishita. It is not used anywhere below. (Theorem 1 gives a fourth, and now decisive, reason why its "homeomorphism" wording cannot be read as the subspace topology of Γ_p: an indiscrete space of more than one point is homeomorphic to no product of a profinite group with a circle.)

---

## 2. The objects, written out

Throughout, **X₀ = spec ℤ**, K₀ = ℚ, K = ℚ̄, X = spec ℤ̄ (the normalization of spec ℤ in ℚ̄), G = Aut_ℚ(ℚ̄), C = ℂ. Since char X₀ consists of *all* prime numbers and char N₀ ⊇ char X₀, we have **N₀ = N** and ℚ^{>0}_0 = ℚ^{>0} ([x-03] §8 opening, p. 49: "we take N₀ = N").

**2.1 Points.** X̊(ℂ) is the set of pairs (x, P^×) with x ∈ X and P^× : κ(x)^× → ℂ^× a homomorphism ([x-03] p. 22). For affine X (here X = spec ℤ̄) these are identified with the multiplicative maps P : ℤ̄ → ℂ with P(0)=0, P(1)=1, p := P^{-1}(0) an ideal (hence a prime ideal), and P factoring through ℤ̄/p (Remark 3.4, p. 23). G acts on the right by (x,P^×)^σ = (x^σ, P^×∘σ); the Frobenius monoid acts by **F_ν(x,P^×) = (x, P^×∘( )^ν)** (p. 22). X̊₀(ℂ) := X̊(ℂ)/G.

**2.2 Topology.** X̊(ℂ) carries the topology of **pointwise convergence** on ℤ̄ — the subspace topology of the Tychonov topology on ℂ^{ℤ̄} — and is metrizable because ℤ̄ is countable ([x-03] §7 p. 40). X̊₀(ℂ) carries the quotient topology; it is metrizable, separable and Hausdorff (Cor. 7.8, p. 45), with a metric δ satisfying δ(π(P),π(P′)) ≤ d(P,P′). X̌(ℂ) = colim_{N₀} X̊(ℂ) carries the inductive-limit topology; X̊(ℂ) is a **closed and open** subspace of it and every F_q (q ∈ ℚ^{>0}) is a **homeomorphism** (Prop. 7.4, p. 43); π̌ : X̌(ℂ) → X̌₀(ℂ) is continuous and **open** (p. 43). Both X̌(ℂ) and X̌₀(ℂ) are Hausdorff, because spec ℤ is affine and hence carries an ample invertible sheaf (Cor. 7.9, p. 45). For an admissible E the spaces X̊(ℂ)_E, X̊₀(ℂ)_E, X̌(ℂ)_E, X̌₀(ℂ)_E carry the **subspace** topologies, and the inductive-limit topologies agree with them (p. 47).

**2.3 The suspension.** X₀ := X̌₀(ℂ)_E ×_{ℚ^{>0}} ℝ^{>0} is the quotient of X̌₀(ℂ)_E × ℝ^{>0} by the right ℚ^{>0}-action

  (P₀, u)·q = (F_q(P₀), q^{-1}u),  q ∈ ℚ^{>0}  ([x-03] p. 38),

with the flow φ^t[P₀,u] = [P₀, u e^t]. We write **q : X̌₀(ℂ)_E × ℝ^{>0} ↠ X₀** for the quotient map and give X₀ the **quotient topology**.

*Anchor for the quotient topology (judgment-grade reading, flagged; identical to the reading used by every previous probe and by the adjudication §2(ii)).* [x-03] never writes the words "quotient topology" for the suspension, but §10 p. 63 sets up exactly this projection, π : X̃ = M × ℝ^{>0} → X = M ×_Q ℝ^{>0}, uses its continuity to define the leafwise sheaf R_X = (π_*R_X̃)^Q ⊆ C⁰_X, and states verbatim: "*Note that in general the continuous bijection π|_{M×{u}} : M×{u} → π(M×{u}) will not be a homeomorphism if π(M×{u}) is equipped with the subspace topology of X.*" That sentence presupposes (i) a topology on X making π continuous and (ii) that the subspace topologies induced from X are strictly coarser than the model ones. The quotient topology is the finest such, and is what makes π|_{M×{u}} continuous with the stated failure of homeomorphy; §8 p. 49 likewise speaks of the "topological closure" of the periodic orbits inside X₀. Every result below uses only that q is **continuous** and **open**; the openness is proved in Lemma 3.1 from the ℚ^{>0}-action being by homeomorphisms (Prop. 7.4b), and continuity is the defining property of a quotient. *If one insisted on a strictly coarser topology on X₀ making q continuous, Theorem 1 would only get stronger.*

**2.4 Packets.** Fix a prime p, a point x ∈ X over p (so κ(x) = F̄_p), and an embedding ι : μ(ℚ̄) ↪ μ(ℂ). With i_x : μ^{(p)}(ℚ̄) ≅ κ(x)^× the reduction isomorphism ((32), p. 31), put χ := ι ∘ i_x^{-1} : F̄_p^× ↪ ℂ^×, an injective character. Since F̄_p^× ≅ ⊕_{ℓ≠p} ℚ_ℓ/ℤ_ℓ and Hom(ℚ_ℓ/ℤ_ℓ, ℂ^×) = ℤ_ℓ, every character of F̄_p^× is **χ^c := χ ∘ ( )^c** for a unique c ∈ Ẑ_{(p)} = ∏_{ℓ≠p}ℤ_ℓ, and Aut(F̄_p^×) = Ẑ^×_{(p)} ([x-03] (34), p. 32). The kernel of χ^c is finite iff c ∈ N·Ẑ^×_{(p)}, and then |ker χ^c| = ∏_ℓ ℓ^{v_ℓ(c)}. The Galois image is Gal(F̄_p/F_p) = p^Ẑ ⊆ Ẑ^×_{(p)} ((34), p. 32). Write

  **B_p := Ẑ^×_{(p)}/p^Ẑ** (a compact group, [x-03] p. 33; uncountable — adjudication §2, re-derived there).

C_{x₀} ⊂ X̌₀(ℂ) is the ℚ^{>0}-saturation of the fibre of pr₀ over x₀ = (p); (38)/(39) give C_{x₀} ≅ B_p ×_{p^ℤ} ℚ^{>0} as ℚ^{>0}-sets, "**and the fibres are the ℚ^{>0}-orbits in C_{x₀}**" (p. 33). Γ^E_{x₀} := C^E_{x₀} ×_{ℚ^{>0}} ℝ^{>0} ⊆ X₀ is the packet; by Thm. 6.1 (p. 39) the periodic points of X₀ are exactly ⨿_{x₀} Γ^E_{x₀}, and the isotropy of every packet point is Nx₀^ℤ = p^ℤ. By Prop. 5.1 (p. 34) every ℚ^{>0}-orbit inside C_{x₀} contains a point (x, χ^a) with a ∈ Ẑ^×_{(p)} (i.e. with injective character), so **every point of Γ^E_{(p)} can be written [ (x,χ^a)^G , w ] with a ∈ Ẑ^×_{(p)}, χ^a ∈ E and w ∈ ℝ^{>0}.** We abbreviate P^a := π(x, χ^a) ∈ X̊₀(ℂ).

---

## 3. Topology bookkeeping (three lemmas, proved in full)

These are the only structural facts about the suspension used later. All three are elementary; they are written out because everything downstream rests on them.

**Lemma 3.1 (q is open).** The quotient map q : X̌₀(ℂ)_E × ℝ^{>0} → X₀ is open.

*Proof.* Let U be open in X̌₀(ℂ)_E × ℝ^{>0}. Then q^{-1}(q(U)) = ⋃_{r ∈ ℚ^{>0}} U·r. For each r the map (P,u) ↦ (P,u)·r = (F_r P, r^{-1}u) is a homeomorphism of X̌₀(ℂ)_E × ℝ^{>0}: F_r is a homeomorphism of X̌(ℂ) ([x-03] Prop. 7.4b, p. 43), it commutes with G and π̌ is an open continuous surjection (p. 43), so F_r is a homeomorphism of X̌₀(ℂ); it preserves X̌₀(ℂ)_E in both directions (Prop. 4.2, p. 27) and hence is a homeomorphism of the subspace X̌₀(ℂ)_E (p. 47); and u ↦ r^{-1}u is a homeomorphism of ℝ^{>0}. Hence each U·r is open, so q^{-1}(q(U)) is open, so q(U) is open by definition of the quotient topology. ∎

**Lemma 3.2 (subspace = sub-suspension).** Let E′ ⊆ E be admissible classes. Then the natural continuous bijection
  X₀^{E′} = X̌₀(ℂ)_{E′} ×_{ℚ^{>0}} ℝ^{>0} ⟶ q( X̌₀(ℂ)_{E′} × ℝ^{>0} ) ⊆ X₀^E
is a **homeomorphism onto its image with the subspace topology**. The same holds for the ℚ^{>0}-invariant subset X̌₀(S¹)_E ⊆ X̌₀(ℂ)_E and its suspension Y₀^Den.

*Proof.* Put Z := X̌₀(ℂ)_E × ℝ^{>0}, A := X̌₀(ℂ)_{E′} × ℝ^{>0}. By Prop. 4.2 (p. 27) X̌₀(ℂ)_{E′} is ℚ^{>0}-invariant, so A is q-saturated, and A carries the subspace topology of Z (p. 47 for the character factor). Let q_A := q|_A : A → q(A). It is continuous and surjective. If U = A ∩ V with V open in Z, then q_A(U) = q(A) ∩ q(V): "⊆" is clear, and if y = q(a) = q(v) with a ∈ A, v ∈ V then v lies in the ℚ^{>0}-orbit of a, hence in A by saturation, so v ∈ A ∩ V and y ∈ q(A∩V). By Lemma 3.1 q(V) is open, so q_A(U) is open in q(A). Thus q_A is a continuous **open** surjection, i.e. a quotient map onto q(A) with the subspace topology; since its fibres are exactly the ℚ^{>0}-orbits, the induced bijection from A/ℚ^{>0} = X₀^{E′} is a homeomorphism. ∎

*Consequence used repeatedly:* for a cut class E(a) ⊆ E_max, the suspension X₀^{E(a)} built abstractly and the subset of X₀ = X₀^{E_max} that it names are the **same topological space**. So the four charter questions are unambiguous.

**Lemma 3.3 (packets are pairwise separated by open sets of X₀).** Let q₀ be a prime. There is an open set V_{q₀} ⊆ X₀ = X₀^{E_max} with
  Γ_{(q₀)} ⊆ V_{q₀}  and V_{q₀} ∩ Γ_{(p)} = ∅ for every prime p ≠ q₀.

*Proof.* Put D := { P ∈ X̊(ℂ) : |P(q₀)| < ½ } (evaluation at the element q₀ ∈ ℤ̄), an open subset of X̊(ℂ) since the topology is pointwise convergence (p. 40). *D is open in X̌(ℂ).* By the inductive-limit criterion (p. 42, after Lemma 7.3) it suffices that F_ν(D) ∩ X̊(ℂ) be open in X̊(ℂ) for every ν ∈ N. Since F_ν(P)(q₀) = P(q₀)^ν and F_ν is injective,
  F_ν(D) ∩ X̊(ℂ) = F_ν(X̊(ℂ)) ∩ { P : |P(q₀)| < 2^{-ν} },
which is open because F_ν(X̊(ℂ)) is open in X̊(ℂ) (Lemma 7.3 with (51), p. 42). Now let S := ⋃_{r ∈ ℚ^{>0}} F_r(D), open and ℚ^{>0}-invariant (Prop. 7.4b), and let V_{q₀} := q( π̌(S) × ℝ^{>0} ), which is open in X₀ (π̌ open, Lemma 3.1).

*Γ_{(q₀)} ⊆ V_{q₀}:* a point of Γ_{(q₀)} is [P^a, w] with P^a = π(x,χ^a), x over q₀; the representative (x,χ^a) ∈ X̊(ℂ) has (x,χ^a)(q₀) = 0 because q₀ ∈ p̄_x, so it lies in D.

*V_{q₀} ∩ Γ_{(p)} = ∅ for p ≠ q₀:* every point of Γ_{(p)} is [P′,w] with P′ ∈ C_{x₀}, x over p, and every ℚ^{>0}G-translate of P′ that lies in X̊(ℂ) is a pair (y, ψ) with y over p and ψ a character of F̄_p^×; its value at q₀ is ψ(q₀ mod p̄_y), and q₀ ∉ p̄_y because p ≠ q₀, so that value is a **root of unity**, of modulus 1 ≥ ½. (G-translates change nothing: q₀ ∈ ℚ is fixed by G, so P^σ(q₀) = P(q₀).) Hence no translate lies in D, i.e. [P′,w] ∉ V_{q₀}. ∎

---

## 4. The cut classes E(a): definition, admissibility, reachability

**4.1 Definition.** For each prime p fix a₀(p) ∈ Ẑ^×_{(p)} (equivalently, a base class [a₀(p)] ∈ B_p) and let χ_p := χ_{x_p}^{a₀(p)} be the corresponding injective character of F̄_p^×. Define
  **E(a)** := the smallest admissible class containing { χ_p : p prime } (with empty characteristic-0 part),
  **E(a)′** := E(a) ∪ { all characters χ : κ^× → ℂ^× with char κ = 0 satisfying (Tors) }.
Both are classes of characters on algebraically closed fields; note that Def. 4.1's two closure operations (pre-composition with Aut κ, and ν-th powers) never change the field κ, so a class may be prescribed characteristic by characteristic and E(a)′ is admissible as soon as E(a) is.

**4.2 The exponent computation (reachability), re-derived here.** In residue characteristic p the moves of Def. 4.1 act on exponents c ∈ Ẑ_{(p)} of χ^c by
  (i) c ↦ cσ, σ ∈ p^Ẑ = image of Aut(F̄_p) in Aut(F̄_p^×) ((34), p. 32);
  (ii) c ↦ cν, ν ∈ N;
  (iii) *backwards*: if cν is in the class and c ∈ Ẑ_{(p)}, then c is in the class (Def. 4.1's "if and only if").
Starting from a₀ := a₀(p) ∈ Ẑ^×_{(p)}, the reachable exponents are
  { d ∈ Ẑ_{(p)} : ∃ σ ∈ p^Ẑ, ν, ν′ ∈ N with dν = a₀σν′ }.
Write ν′/ν in lowest terms as m/n with gcd(m,n) = 1. Then d = a₀σ·m/n lies in Ẑ_{(p)} iff n is invertible in Ẑ_{(p)}, i.e. iff n = p^j; and p^{-j} ∈ p^ℤ ⊆ p^Ẑ. Splitting m = p^k m′ with p ∤ m′ we obtain

  **E(a)-locus in characteristic p = { χ^d : d ∈ a₀·p^Ẑ·N^{(p)} }**,  N^{(p)} := { m ∈ N : p ∤ m }.  (★)

*This set is admissible.* Forward closure under (i) and (ii) is immediate from (★). Backward closure: suppose χ^{dν} has exponent a₀σm with σ ∈ p^Ẑ, p ∤ m, and d ∈ Ẑ_{(p)}. Write ν = p^k ν′ with p ∤ ν′. Then ν′p^k d = a₀σm, so for every ℓ ≠ p, v_ℓ(d) = v_ℓ(m) − v_ℓ(ν′) ≥ 0, whence ν′ | m in ℤ and d = a₀σ p^{−k}(m/ν′) ∈ a₀p^Ẑ N^{(p)}. Closure under Aut κ is (i). (Tors) holds for every member: ker χ^{a₀σm′} = μ_{m′} ⊂ F̄_p^×, of order m′ ∈ N = N₀. ∎

*The injective members.* χ^d is injective iff d ∈ Ẑ^×_{(p)}, i.e. iff m′ = 1 in (★), i.e. **d ∈ a₀·p^Ẑ**: a single base class [a₀] ∈ B_p. (This re-derives probe A's Theorem C(b)/§4.1 and the adjudication §4 item 5b independently; the unit parts u(ℓ) of other primes are **not** reachable, because a₀σm′ is a unit only for m′ = 1.)

**4.3 Clause (4): one orbit per packet, for every choice of a — YES.**

**Proposition 4.1.** For every choice a = (a₀(p))_p and for E ∈ {E(a), E(a)′}: for every prime p,
  Γ^{E}_{(p)} = the single ℝ^{>0}-orbit through [P^{a₀(p)}, 1], a circle of length log p,
and by [x-03] Thm. 6.1 (p. 39) these are **all** the periodic orbits of X₀^{E}. In particular the T1 counting requirement "coefficient exactly 1 per prime" (ledger §3) is met at the level of *sets and orbits*.

*Proof.* By (★) the E-locus of C_{x₀} consists of the points whose (unique) injective ℚ^{>0}-representative has exponent in a₀p^Ẑ, i.e. of the points lying over the single base class [a₀] ∈ B_p under the fibration of (38)/(39). By [x-03] p. 33 verbatim, "*the fibres are the ℚ^{>0}-orbits in C_{x₀}*", so C^{E}_{x₀} is exactly one ℚ^{>0}-orbit, and Γ^{E}_{x₀} = C^{E}_{x₀} ×_{ℚ^{>0}} ℝ^{>0} is exactly one ℝ^{>0}-orbit. Its isotropy is p^ℤ (Thm. 5.2, p. 34), so it is a circle of length log p. Since E(a), E(a)′ ⊆ E_tors = E_max over spec ℤ ((Image) is vacuous: it constrains only characters of fields of positive characteristic whose multiplicative group is non-torsion, and κ(x)^× = F̄_p^× is torsion), Thm. 6.1 applies and gives that the points of X₀^E with non-trivial isotropy are exactly ⨿_{x₀} Γ^E_{x₀}. ∎

**Remark 4.2 (what clause (4) does and does not buy).** This is a genuine *construction*, and it is the only clause of the charter that succeeds. It is however exactly the object the adjudication already priced: the choice of a is an arbitrary point of the uncountable Cantor group B_p **for every prime**, no canonical selection exists (adjudication §4 item 5; 9.4 Prop. 1: no Aut(ℂ)-stable selection exists at all), and X₀^{E(a)} forfeits every theorem [x-03] proves for E ⊇ E_f (connectedness Cor. 9.7 p. 62, H⁰_F = ℝ Thm. 10.2 p. 64, and the closure identification Thm. 8.2 p. 50, whose approximants are arbitrary finite-kernel characters). Nothing below rests on re-proving any of those for E(a); the point of §§5–7 is that the *topology* of X₀^{E(a)} destroys the candidate regardless.

---

## 5. THEOREM 1: the packets are indiscrete subspaces of X₀

This is the result that decides face (a). It is proved from [x-03]'s definitions only; no result of any program note is used as an input.

**Lemma 5.1 (Frobenius twists converge).** Let p be a prime, a ∈ Ẑ^×_{(p)}, c ∈ Ẑ_{(p)}, and let (m_k) ⊂ N satisfy m_k → c in Ẑ_{(p)} = lim_{(M,p)=1} ℤ/M. Then
  (x, χ^{a m_k}) ⟶ (x, χ^{a c}) in X̊(ℂ),
and consequently P^{a m_k} = π(x,χ^{am_k}) → π(x,χ^{ac}) in X̊₀(ℂ), hence in X̌₀(ℂ), hence in X̌₀(ℂ)_E for any admissible E containing χ^a and χ^{ac}.

*Proof.* The topology on X̊(ℂ) is pointwise convergence of the multiplicative maps ℤ̄ → ℂ ([x-03] §7 p. 40). Fix r ∈ ℤ̄. If r ∈ p̄_x then both (x,χ^{am_k})(r) and (x,χ^{ac})(r) are 0 (Remark 3.4, p. 23). Otherwise r̄ := r mod p̄_x ∈ F̄_p^×; since F̄_p^× = μ^{(p)} is torsion of order prime to p, r̄ has finite order d with p ∤ d. Now χ^{am_k}(r) = χ(r̄)^{a m_k mod d}, and reduction Ẑ_{(p)} → ℤ/d is a ring homomorphism, so m_k → c in Ẑ_{(p)} gives a m_k ≡ a c (mod d) for all large k, i.e. χ^{am_k}(r) = χ^{ac}(r) **exactly, eventually**. Pointwise convergence follows. The push-forwards: π is continuous with δ(π(P),π(P′)) ≤ d(P,P′) (Cor. 7.8, p. 45); X̊₀(ℂ) is a subspace of X̌₀(ℂ) (Prop. 7.4a and p. 47); and the E-spaces carry the subspace topologies (p. 47), so a convergent sequence all of whose terms and whose limit lie in X̌₀(ℂ)_E converges there. Membership: χ^{am_k} = (χ^a)∘( )^{m_k} = F_{m_k}(χ^a) ∈ E by Def. 4.1's biconditional ν-closure (p. 27); and (Tors) holds with |ker| = (prime-to-p part of m_k) ∈ N = N₀. ∎

**Lemma 5.2 (simultaneous profinite and archimedean approximation).** Let p be a prime, c ∈ Ẑ_{(p)}, t ∈ ℝ^{>0}. Then there are m_k ∈ N and j_k ∈ ℤ with
  m_k → c in Ẑ_{(p)}  and m_k p^{-j_k} → t in ℝ^{>0}.

*Proof.* Set M_k := ∏_{ℓ ≤ k, ℓ ≠ p} ℓ^k, so that every integer M prime to p divides M_k for all large k. By the Chinese remainder theorem the reduction N ↠ ℤ/M_k is surjective, so pick c_k ∈ ℤ with c_k ≡ c (mod M_k). Choose j_k ∈ N so large that M_k p^{-j_k} < 1/k and t p^{j_k} > M_k. Let m_k be the unique integer in the interval [t p^{j_k}, t p^{j_k} + M_k) with m_k ≡ c_k (mod M_k) — the interval has length M_k, so exactly one residue-class representative lies in it. Then m_k > M_k > 0, so m_k ∈ N; m_k ≡ c (mod M_k), hence m_k ≡ c (mod M) for every fixed M prime to p and all large k, i.e. m_k → c in Ẑ_{(p)}; and |m_k p^{-j_k} − t| < M_k p^{-j_k} < 1/k. ∎

*(This is the same mechanism Deninger himself uses on the generic fibre: "The fact that Y carries the coarse topology follows from **strong approximation for ℚ** … (excluding the infinite place, i.e. the Chinese remainder theorem)", [x-03] proof of Thm. 9.6, p. 62. Here the "excluded infinite place" is restored by the p^ℤ-isotropy, which is exactly the extra freedom the packets have and the idelic space of Thm. 9.6 does not.)*

**THEOREM 1.** Let X₀ = spec ℤ, let E be **any** admissible class with E ⊆ E_max, and let X₀ = X̌₀(ℂ)_E ×_{ℚ^{>0}} ℝ^{>0} with the quotient topology. Fix a prime p and let

  z = [P^a, w] and z′ = [P^b, u],  a, b ∈ Ẑ^×_{(p)}, χ^a, χ^b ∈ E, w, u ∈ ℝ^{>0},

be **any two points of the packet Γ^E_{(p)}**. Then z′ ∈ cl_{X₀}({z}).

*Proof.* Put c := b a^{-1} ∈ Ẑ^×_{(p)} ⊆ Ẑ_{(p)} and t := w/u ∈ ℝ^{>0}. By Lemma 5.2 choose m_k ∈ N and j_k ∈ ℤ with m_k → c in Ẑ_{(p)} and m_k p^{-j_k} → t. Set r_k := m_k p^{-j_k} ∈ ℚ^{>0} and consider the points of the ℚ^{>0}-orbit of (P^a, w) in X̌₀(ℂ)_E × ℝ^{>0}:

  (P^a, w)·r_k = ( F_{r_k}(P^a), r_k^{-1} w ).

*First coordinate.* By [x-03] Thm. 5.2 (p. 34) the isotropy group of P^a ∈ C^E_{x₀} in ℚ^{>0} is exactly Nx₀^ℤ = p^ℤ, so F_{p^{-j_k}}(P^a) = P^a and therefore
  F_{r_k}(P^a) = F_{m_k}(F_{p^{-j_k}}(P^a)) = F_{m_k}(P^a) = π(x, χ^{a m_k}),
using F_ν(x,P^×) = (x, P^×∘( )^ν) (p. 22) and the exponent convention of (35) (p. 32). By Lemma 5.1, F_{m_k}(P^a) → π(x, χ^{ac}) = π(x, χ^{b}) = P^b in X̌₀(ℂ)_E.

*Second coordinate.* r_k^{-1} w = w/(m_k p^{-j_k}) → w/t = u in ℝ^{>0}.

Hence (P^a, w)·r_k → (P^b, u) in the product X̌₀(ℂ)_E × ℝ^{>0}. The quotient map q is continuous, and q((P^a,w)·r_k) = q(P^a,w) = z for every k by the definition of X₀ as the orbit space. So the **constant** sequence (z)_k converges in X₀ to q(P^b,u) = z′. Therefore every neighbourhood of z′ contains z, i.e. z′ ∈ cl_{X₀}({z}). ∎

**Remarks on the proof.**
1. *What makes it work.* The suspension identification lets one move along the orbit by any r ∈ ℚ^{>0}; the character coordinate sees only r modulo the isotropy p^ℤ, i.e. only the class of m_k in Ẑ_{(p)}, while the ℝ-coordinate sees the *real* number m_k p^{-j_k}. The two are decoupled precisely because p is a unit in Ẑ_{(p)} but not in ℝ. Deninger's own Remark after Prop. 10.3 (p. 64) shows that on the **idelic** model ℚ^{>0}Ẑ^× × ℝ^{>0} the ℚ^{>0}-orbits *are* closed and the quotient is T₁ — there is no isotropy there to decouple the two coordinates. The packets are exactly where the decoupling happens.
2. *No Hausdorffness, metrizability, compactness or closedness is used anywhere.* Only: F_ν(x,P^×) = (x,P^×∘( )^ν); the isotropy statement of Thm. 5.2; the pointwise-convergence topology; continuity of π, of the inclusions of the E-subspaces, and of q.
3. *Symmetry.* Applying the theorem with (z,z′) interchanged gives z ∈ cl({z′}): the two points are **topologically indistinguishable** in X₀.
4. *Generality.* The proof is written for spec ℤ because that is the S4 case. For a general arithmetic X₀, replace p by Nx₀ = |κ(x₀)| throughout; Lemma 5.1 is unchanged, and Lemma 5.2 needs m_k ∈ N₀ (rather than N) in a prescribed residue class prime to p and in a prescribed real window — obtainable from the prime number theorem in arithmetic progressions, since N₀ contains all but finitely many primes ([x-03] p. 62: "there is a finite set S of prime numbers such that N₀ is generated by all p ∉ S"). *That extension is a sketch and is flagged; nothing below uses it.*

### 5.1 Corollaries

**Corollary 1.1 (indiscreteness).** For every prime p and every admissible E ⊆ E_max, the packet Γ^E_{(p)} carries the **indiscrete** topology as a subspace of X₀: its only relatively open subsets are ∅ and Γ^E_{(p)}. The same holds for every ℝ^{>0}-orbit γ ⊆ Γ^E_{(p)} — in particular **a single periodic orbit of X₀ is an indiscrete subspace**, and it has continuum many points, being in ℝ^{>0}-equivariant bijection with ℝ^{>0}/p^ℤ ([x-03] p. 38). Consequently **X₀ is not T₀**.

*Proof.* Let U be open in X₀ with U ∩ Γ^E_{(p)} ≠ ∅, say z ∈ U. For any z′ ∈ Γ^E_{(p)}, Theorem 1 gives z ∈ cl({z′}), so every open set containing z′ contains z; equivalently (contrapositive) every open set containing z contains z′ — indeed by Remark 3 the two points have the *same* neighbourhood filter. Hence z′ ∈ U. So U ⊇ Γ^E_{(p)}. The same argument inside a single orbit gives the orbit statement, since an orbit is a subset of a packet and the two points of Theorem 1 may be taken with b = a. ∎

**Corollary 1.2 (Q-a is NO).** Let Y ⊆ X₀ be flow-invariant and suppose Y ∩ Γ^E_{(p)} ≠ ∅ for at least one prime p. Then Y is not T₀ in its subspace topology; a fortiori not Hausdorff, not metrizable, not a compact foliated space, not a lamination. In particular:
> **there is no compact, Hausdorff-in-its-subspace-topology, flow-invariant subspace Y ⊆ X₀ of any dimension meeting each packet in exactly one orbit.** Face (a) of Q\* has answer **NO**, for every admissible E, and equally for the unitary system Y₀^Den = X̌₀(S¹) ×_{ℚ^{>0}} ℝ^{>0} (Lemma 3.2 identifies its topology with the subspace topology in X₀, and the entire proof of Theorem 1 takes place inside the packet, whose characters are unitary — all their values are roots of unity).

*Proof.* Y flow-invariant and meeting a packet means Y contains a full ℝ^{>0}-orbit of X₀ inside that packet (packets are flow-invariant by Thm. 6.1, p. 39). That orbit is infinite and indiscrete in X₀ (Cor. 1.1), hence indiscrete in Y; a T₀ space has no indiscrete subspace with two distinct points. ∎

**Corollary 1.3 (Theorem A and W12 are special cases).** For any periodic orbit γ ⊆ Γ^E_{(p)}: cl_{X₀}(γ) ⊇ cl_{X₀}({z}) ⊇ Γ^E_{(p)} for z ∈ γ. This re-proves the banked **Theorem A** (packet-closure law) and, with Cor. 1.1, the banked **Corollary A.2 / ledger row W12** (X₀ non-Hausdorff along packets) — both now as corollaries of a strictly stronger statement, and by an argument that does not need the "two distinct base classes" hypothesis under which W12 was scoped (adjudication §3, scope note). In particular W12's stated exception — "*for probe A's minimal cut classes E(a₀), whose packet E-locus is a single orbit, this argument produces no second limit and decides nothing*" — is now removed: **the cut suspensions are non-Hausdorff too**, by Theorem 1 with b = a.

**Corollary 1.4 (the closed half of S4 dies again, and more cheaply).** No flow-invariant subset of X₀ containing a periodic orbit — closed or not, compact or not — is a compact metrizable lamination, since none is even T₀. This subsumes the banked "closed half of S4 is dead" (adjudication §4 item 2) without using Thm. 8.2, Claim 8.1/[Per11], the uncountability of B_p, or any dimension theory. Those routes remain correct and remain the right citation for the *orbit-count* statement (uncountably many closed orbits per prime); Theorem 1 adds an independent and more elementary route to the *topological* half.

**Corollary 1.5 (Deninger's own question, subspace alternative).** [x-03] p. 40 asks: "*Is there a sub-dynamical system Y₀ ⊂ X₀ = X̌₀(ℂ) ×_{ℚ^{>0}} ℝ^{>0} … such that dim Y₀ = 2d+1 … and such that Y₀ contains at least one periodic orbit in Γ_{x₀} for every closed point x₀ of X₀? If d = 1, is there such a Y₀ which is a Riemann surface lamination in the sense of [Ghy99]?*" Read with "sub-dynamical system" = flow-invariant **subspace** (with no closedness assumed) and "Riemann surface lamination" entailing (as it does) a Hausdorff, indeed metrizable, topology, the answer is **NO**, unconditionally: any such Y₀ contains a periodic orbit, which is an indiscrete subspace. The remaining alternative in Deninger's sentence — "*or at least one which maps to X₀*" — is untouched.

---

## 6. Interlude: the model description of a packet is not a topological description

Theorem 1 is not in conflict with anything [x-03] states, and the reason is worth recording because the program has stumbled over it once already (ledger row W11).

* Deninger's packet description is stated as a **bijection**, never a homeomorphism: "*The ℚ^{>0}_0-**bijection** (39) induces an ℝ^{>0}-**bijection** (Ẑ^×_{(p)}/Nx₀^Ẑ) ×_{p^ℤ/deg x₀} ℝ^{>0}/Nx₀^ℤ ≅ Γ_{x₀}*" ([x-03] p. 38). Theorem 7.10's Remark 2 (p. 47) warns in general: "*The continuous bijections in Theorem 7.10 are not homeomorphisms in general.*"
* §10 p. 63 states the failure for the transverse direction explicitly: "*Note that in general the continuous bijection π|_{M×{u}} : M×{u} → π(M×{u}) will not be a homeomorphism if π(M×{u}) is equipped with the subspace topology of X*", and adds that when the ℚ^{>0}-action is not properly discontinuous "*the partition of X … will not be locally trivial*". §7 p. 49 records that the action **is** not properly discontinuous — "*and in section 10, we will see that this works to our advantage*". Theorem 1 is the same phenomenon in the **flow** direction, taken to its extreme: the model circle ℝ^{>0}/p^ℤ maps continuously and bijectively onto γ_p ⊂ X₀, but γ_p's own topology is indiscrete.
* The character space is *not* to blame. X̌₀(ℂ) is Hausdorff (Cor. 7.9, p. 45, applicable since spec ℤ is affine), and the injective part of C_{x₀} is, with its subspace topology, the compact Hausdorff group B_p (pointwise convergence of χ^{c_k} at the finite-order elements of F̄_p^× is exactly convergence c_k → c in Ẑ_{(p)}). **All of the pathology is created by the suspension quotient**, i.e. by the ℚ^{>0}-action, precisely as Deninger's non-proper-discontinuity remark predicts.
* The contrast with Deninger's own T₁ statement is instructive. His Prop. 10.3 Remark (p. 64) says that on the idelic model the ℚ^{>0}-orbits on ℚ^{>0}Ẑ^× × ℝ^{>0} are **closed**, so that Y = ℚ^{>0}_0Ẑ^× ×_{ℚ^{>0}_0} ℝ^{>0} is T₁ (though irreducible, hence still non-Hausdorff). On the packet the orbits are **not** closed, and the single structural reason is the isotropy p^ℤ of Thm. 5.2: it makes the character coordinate blind to the p-part of q ∈ ℚ^{>0} while the ℝ-coordinate still sees it. Theorem 1's Lemma 5.2 is exactly the resulting "strong approximation with the infinite place put back in".

---

## 7. The four charter questions, answered for X₀^{E(a)}

Throughout, a = (a₀(p))_p is an arbitrary choice of base classes, E(a) the minimal cut (empty in characteristic 0) and E(a)′ the enlarged cut of §4.1, and γ_p := Γ^{E(a)}_{(p)} the unique periodic orbit over p (Prop. 4.1).

### 7.1 Structure of the minimal cut suspension

**Proposition 7.1.** X₀^{E(a)} = ⨆_p γ_p, and each γ_p is **open and closed** in X₀^{E(a)}. Hence X₀^{E(a)} is the topological coproduct of countably infinitely many indiscrete circles: its open sets are exactly the unions of the γ_p, so as a topological space it is (countable discrete set) with an indiscrete continuum sitting over each point.

*Proof.* Since E(a) has empty characteristic-0 part, every point of X̌₀(ℂ)_{E(a)} lies over a closed point of X = spec ℤ̄, so X₀^{E(a)} = ⋃_p Γ^{E(a)}_{(p)} = ⋃_p γ_p (Prop. 4.1), and the union is disjoint ([x-03] Thm. 6.1, p. 39: distinct closed points give disjoint packets). By Lemma 3.3 there is an open V_p ⊆ X₀^{E_max} with V_p ∩ Γ_{(q)} = ∅ for q ≠ p and V_p ⊇ Γ_{(p)}; by Lemma 3.2, V_p ∩ X₀^{E(a)} = γ_p is open in X₀^{E(a)}. Its complement ⋃_{q≠p} γ_q is open by the same argument, so γ_p is also closed. Finally, each γ_p is indiscrete (Cor. 1.1), so a set is open in X₀^{E(a)} iff it meets each γ_p in ∅ or γ_p. ∎

### 7.2 (2) Hausdorffness — **NO**, and this is the decisive failure

By Corollary 1.1, each γ_p ⊂ X₀^{E(a)} is indiscrete with continuum many points. So X₀^{E(a)} is not T₀, not T₁, not Hausdorff, not metrizable, not a foliated space, not a lamination, and does not embed in any Hausdorff space. The same holds for X₀^{E(a)′}, for X₀ itself, and for the unitary system. **This closes the adjudication §7 item "Hausdorffness of the CUT suspensions X₀^{E(a)} (the only Hausdorff question left with any S4 relevance)" with the answer NO**, and it removes the scope exception under which row W12 was recorded (adjudication §3, scope note).

### 7.3 (1) Compactness

**Corollary 7.2.** X₀^{E(a)} is **not compact** (and not connected, and not quasi-compact in any weaker sense): {γ_p}_p is an open cover with no finite subcover, by Prop. 7.1.

**Proposition 7.3 (three positive compactness facts, for the record).**
(a) *Every packet is compact.* Γ^E_{(p)} ⊂ X₀ is indiscrete (Cor. 1.1), hence compact. So Deninger's description of the packets as "compact" ([x-03] intro p. 2 "The compact packets Γ_{x₀}…"; [x-06] Thm. 4.2) is, in the subspace topology, **topologically vacuous** — it conveys no information whatever, and in particular it must not be read as evidence that packets are compact *Hausdorff*.
(b) *X̊(S¹) is compact Hausdorff, and so is X̊₀(S¹).* Indeed, by Remark 3.4 (p. 23), X̊(S¹) is the set of P ∈ T := ∏_{r∈ℤ̄}(S¹∪{0}) satisfying: P(0)=0, P(1)=1; P(rs)=P(r)P(s); P^{-1}(0) additively closed; and P(r)=P(r′) whenever P(r−r′)=0. In T (compact Hausdorff by Tychonov) each set {P : P(r)=0} is **clopen**, because {0} and S¹ are both closed in S¹∪{0}. Hence: the multiplicativity and normalization conditions are closed; the complement of the third condition is {P(r)=0}∩{P(s)=0}∩{P(r+s)≠0}, an intersection of clopen sets, so the condition is closed; the complement of the fourth is {P(r−r′)=0}∩{P(r)≠P(r′)}, clopen ∩ open, so that condition is closed too. Thus X̊(S¹) is closed in T, hence compact; it is Hausdorff by Cor. 7.9 (p. 45). X̊₀(S¹) = X̊(S¹)/G is then compact, and Hausdorff by Cor. 7.8 (p. 45).
(c) *X̌(S¹) and X̌₀(S¹) are **not** compact.* They are the increasing unions ⋃_ν F_ν^{-1}X̊(S¹) resp. ⋃_ν F_ν^{-1}X̊₀(S¹) of subsets which are open and closed (Prop. 7.4a, p. 43, together with F_ν a homeomorphism; downstairs because X̊(ℂ) is G-invariant and π̌ is open). The union is strictly increasing: for ν > 1 choose a prime p ∤ ν and a unitary character ψ of F̄_p^× injective on μ_ν(F̄_p); then ψ(μ_ν(K)) ≠ 1, so by (51) (p. 42) (x,ψ) ∉ F_ν(X̊(ℂ)), i.e. F_ν^{-1}(x,ψ) ∈ F_ν^{-1}X̊(S¹) ∖ X̊(S¹). A compact space covered by a directed family of open sets equals one of them; contradiction.

**What is NOT determined here (honesty).** Compactness of X₀^{E(a)′}, of X₀ = X₀^{E_max}, and of Y₀^Den = X̌₀(S¹) ×_{ℚ^{>0}} ℝ^{>0} is **left open**. Two remarks bound the question. (i) **[x-03] asserts none of them.** The only compactness statements in the paper are for the packets Γ_{x₀} (intro p. 2), for the group Ẑ^×_{(p)}/p^Ẑ (p. 33), and for the group G; §8 (p. 49) says only that X₀ and Y₀ are "infinite dimensional", and that phrase is used informally — no covering-dimension theorem for the suspension appears anywhere in [x-03]. (ii) The obvious routes both stall: X̌₀(ℂ)_E is not compact (it is not even bounded in ℂ^{ℤ̄} once characteristic-0 points are present), but X₀^E is a quotient of it and quotients of non-compact spaces may be compact; and the ℚ^{>0}-saturation of any chart-bounded open set is everything, so the chart exhaustion of Prop. 7.3(c) does not descend to the suspension. **This is moot for Q-a**: Corollary 1.2 kills face (a) with no compactness input whatever.

### 7.4 (3) Topological dimension

**Corollary 7.4.** (a) For every admissible E and every prime p, the packet Γ^E_{(p)} ⊂ X₀ has covering dimension 0, and small and large inductive dimension 0. (b) dim X₀^{E(a)} = 0 (in all three senses), **not** 3.

*Proof.* (a) A nonempty indiscrete space X has {X} as its only open cover, which refines itself with order 1, so dim X ≤ 0; and dim X ≥ 0 as X ≠ ∅. The base {X} consists of sets with empty boundary (∂X = cl X ∖ int X = ∅), so ind X = Ind X = 0. (b) Let {U_1,…,U_n} be a finite open cover of X₀^{E(a)}. By Prop. 7.1 each γ_p is contained in some U_{i(p)}; put V_i := ⋃_{p : i(p)=i} γ_p. The V_i are open, pairwise disjoint, refine the cover, and have order 1. Hence dim = 0; the inductive dimensions are 0 because {γ_p} is a base of clopen sets. ∎

**Comment.** The number 3 that S4 asks for is a property of the *model* (Cantor set) × (circle) × (leaf direction), and Theorem 1 shows the subspace topology retains none of it: the covering dimension of the actual subspace is 0, and the "1-dimensional Cantor-bundle-of-circles" picture of Γ_p is a picture of the bijection (39), not of the topology. Note that this also removes the *only* rigorous route the program had to "infinite-dimensionality of a subsystem": probe A's Theorem B(b) derived dim ≥ n for closed invariant S **assuming S Hausdorff in its subspace topology** — a hypothesis now provably unsatisfiable whenever S contains a periodic orbit (§8).

### 7.5 (4) One orbit per packet — **YES**, for every a

Proposition 4.1: for every choice a and both cut classes, Γ^{E}_{(p)} is a single circle of length log p for every prime p, and [x-03] Thm. 6.1 (p. 39) says these are all the periodic orbits. The choice-content and the theory-forfeiture are as the adjudication already priced them (Remark 4.2).
