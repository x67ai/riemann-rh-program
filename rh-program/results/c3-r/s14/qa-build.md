# S14 PROBE — Q* face (a), BUILD direction: the cut suspensions X₀^{E(a)} and the subspace face of S4

**Program:** RH program, direction C3-r, milestone M2c, Route 2, blocker S4. **Date:** 2026-09-02 (Session 14).
**Charter:** try to prove YES on Q-a by construction; first candidate = the cut suspensions X₀^{E(a)} of probe A's Theorem C(b). Determine (1) compactness, (2) Hausdorffness in the subspace topology, (3) topological dimension, (4) whether each packet is met in exactly one orbit for every choice of a. If the candidate fails, say exactly which property fails and why, as a theorem where possible.
**Author:** s14 Q-a build probe (independent; wrote nothing into any existing file).
**Run history (honesty).** A first run of this probe was killed by a usage limit after §7.5. This file is the completed note: every statement of the partial draft was re-derived against the on-disk PDF this run before being kept, four page citations were corrected, one proof was simplified, and §§7.3, 7.6 and 8–12 are new. The partial draft's own §0 recorded compactness as *undetermined* for three of the four systems; that is now **settled** (Theorem 2, §7.3). The superseded draft is not part of the deliverable.

---

## 0. VERDICT (stated first): **THEOREM (NO)** — Q-a is dead, unconditionally, and for a reason strictly stronger than the one the question anticipated

The construction fails, and it fails on clause **(2)**, catastrophically and provably. The exact statements established below:

> **Theorem 1 (packet indiscreteness).** Let X₀ = spec ℤ, let E be any admissible class of characters ([x-03] Def. 4.1, p. 27) with E ⊆ E_max, and let **X₀ = X̌₀(ℂ)_E ×_{ℚ^{>0}} ℝ^{>0}** be the suspension with its quotient topology ([x-03] §6 p. 38, §10 p. 63). Fix a prime p and let z, z′ be **any two points of the packet Γ^E_{(p)}**. Then z′ ∈ cl_{X₀}({z}). Equivalently: all points of a packet are topologically indistinguishable in X₀; **Γ^E_{(p)} carries the indiscrete topology as a subspace of X₀**; in particular **X₀ is not a T₀ space**, and its periodic orbits are indiscrete subspaces.

> **Corollary 1.2 (Q-a: NO).** There is **no** flow-invariant subspace Y ⊆ X₀ which is T₀ — a fortiori none which is Hausdorff — in its subspace topology and which meets even one packet in a full orbit. Since any S4 substrate in the subspace reading must contain, for every prime p, one periodic orbit inside Γ_{(p)}, and every periodic orbit is an infinite indiscrete subspace, **face (a) of Q\* has answer NO**. The answer is unconditional: it holds for every admissible E (certified E ⊇ E_f, E_max, E_tors, and every cut class E(a) alike), for the unitary system X̌₀(S¹) ×_{ℚ^{>0}} ℝ^{>0}, and it needs **no** hypothesis of compactness, dimension, metrizability or closedness. Compactness and dimension are therefore *moot* for Q-a; they are answered below anyway, as the charter asks.

> **Theorem 2 (non-compactness).** For X₀ = spec ℤ and any admissible E ⊆ E_max whose locus contains one characteristic-zero point (x_η, Ψ) with Ψ injective on μ(ℚ̄) — in particular **E_f, E_fg, E_fd, E_fd0, E_max = E_tors, the enlarged cut E(a)′, and the unitary system Y₀^Den = X̌₀(S¹) ×_{ℚ^{>0}} ℝ^{>0}** — the suspension X₀^E is **not quasi-compact**. Together with Corollary 7.2 (which handles the minimal cut, whose characteristic-0 part is empty), **every** system named in the program's S4 discussion fails compactness. This settles charter question (1) uniformly in the negative, and upgrades ledger row R1's "compactness not established" to "compactness fails".

The cut suspensions specifically:

| Charter question | Answer for X₀^{E(a)} | Grade |
|---|---|---|
| (1) compact? | **NO**, for both cuts and for every other system named. Minimal cut E(a): X₀^{E(a)} is the topological coproduct ⨆_p γ_p of countably many pairwise clopen pieces (Prop. 7.1 + Cor. 7.2). Enlarged cut E(a)′, X₀ = X₀^{E_max}, and Y₀^Den: Theorem 2. | theorem |
| (2) Hausdorff in the subspace topology? | **NO**, in the strongest possible way: each γ_p is *indiscrete* (Theorem 1). This answers the adjudication §7 item "Hausdorffness of the CUT suspensions X₀^{E(a)}" — the last Hausdorff question with S4 relevance — in the negative. | theorem |
| (3) topological dimension? | **0**, not 3, for the minimal cut: covering, small- and large-inductive dimension all vanish because the space is a coproduct of indiscrete pieces (Cor. 7.4). Every packet Γ^E_{(p)} ⊂ X₀, in any E, likewise has covering dimension 0. | theorem |
| (4) exactly one orbit per packet, for **every** choice of a? | **YES.** E(a) is admissible, Γ^{E(a)}_{(p)} is a single circle of length log p for every prime and every choice a = (a₀(p))_p, and by [x-03] Thm. 6.1 these are *all* the periodic orbits of X₀^{E(a)} (§4.3). This is the one clause that survives — and it survives for the minimal and the enlarged cut alike. | theorem |

**Net effect on the program.** Q\*'s face (a) is closed NO; face (b) (the mapping face) is **untouched** and remains the unique survivor of S4, exactly as the adjudication's delineation predicted — Theorem 1 makes the *target* coarser, which can only help a map into it (§9). The kill-criterion therefore still does **not** fire. Theorem 1 also **subsumes and strengthens** three banked items (Theorem A, Cor. A.2 / ledger row W12, and the closed-half kill), **sharpens** the Session-14 referee-banked closure equality to cl_{X₀}({z}) = Γ^E_{(p)} for a *single point* z, and **empties** one referee-pending item (probe A's Theorem B(b), whose Hausdorff hypothesis is now provably unsatisfiable, so that the statement becomes vacuously true and can no longer be cited as evidence) — see §8. Nothing that the adjudication banked as a *verdict* changes.

Nothing here is rounded up: what is proved is a *negative* theorem about the subspace face plus a *positive* set-level construction (clause (4)) that is not a substrate.

---

## 1. Sources read this session, with locations

All page numbers are the **printed** pages of the on-disk PDF; the text was extracted fresh this session with `pdftotext -layout` and every passage quoted below was read verbatim in that extraction. Printed page = extracted page was verified against the page footers (e.g. the footer "27" on the Definition-4.1 page). Nothing in §§2–9 is used from memory.

**[x-03]** C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`. Read this session:

| Item | Printed page | What was read |
|---|---|---|
| Intro: "the closed points x₀ of X₀ correspond bijectively to **compact packets** Γ_{x₀} of periodic orbits of length log Nx₀"; "Γ_{x₀} is fibred over the compact group Aut(F̄_p)/Aut(F_p)^ = Ẑ^×_{(p)}/p^Ẑ"; "The compact packets Γ_{x₀} are reminiscient of invariant tori" | pp. 2–3 | verbatim |
| Def. of X̊(ℂ), the G-action and the N-action | p. 22 | "We define X̊(C) to be the set of pairs (x, P^×) where x ∈ X and P^× : κ(x)^× → C^× is a homomorphism… (x,P^×)^σ = (x^σ, P^× ∘ σ) … **F_ν(x,P^×) = (x, P^× ∘ ( )^ν)** for ν ∈ N." Also (23): G_x ↠ Aut_{κ(x₀)}(κ(x)). |
| Remark 3.4 (points as multiplicative maps) | p. 23 | "we will identify the points (x,P^×) of X̊(C) with the multiplicative maps P : R → C satisfying … 1) P(0)=0, P(1)=1. 2) p := P^{-1}(0) is additively closed and hence a prime ideal. 3) We have a factorization P : R → R/p → C." |
| (Tors), (Image), **Def. 4.1** (admissible class), Prop. 4.2 | p. 27 | "A class E of characters χ : κ^× → C^× … is (N₀−)admissible if for any σ ∈ Autκ resp. ν ∈ N₀ the character χ is in E **if and only if** χ∘σ resp. χ_ν = χ∘( )^ν is in E. Moreover the characters in E should satisfy (Tors)." Prop. 4.2: X̊(ℂ)_E is G-invariant and forward/backward N₀-invariant; N₀ acts by injections. |
| Lemma 4.3 (extension of a character of μ(k) to k^× with the same kernel); Cor. 4.4 | p. 28 | verbatim, with proof (the splitting k^× ≅ μ(k) × (k^×/μ(k)) and the ℚ-linear injection) |
| Examples E_tors, E_max, E_f, E_fg, E_fd, E_fd0; the chain E_f ⊂ E_fg ⊂ E_fd ⊂ E_fd0 ⊂ E_max ⊂ E_tors | pp. 28–29 | verbatim (E_max on p. 28, the rest on p. 29) |
| Remark: "The topology of the R-dynamical systems that we will build from X̌(C)_E depends very much on the choice of E"; and the p-adic "P is additive mod p … the resulting class E is not N-invariant" | p. 29 | verbatim |
| (32) reduction isomorphism i_x : μ^{(p)}(K) ≅ κ(x)^×; the definition C_{x₀} = pr₀^{-1}(x₀)ℚ^{>0}_0 | p. 31 | verbatim |
| (34) Gal(κ(x)/κ(x₀)) = Nx₀^Ẑ ↪ Aut(κ(x)^×) = Ẑ^×_{(p)}; (35) the (a,ν)-parametrization χ_x·(a,ν) = χ_x∘( )^a∘( )^ν and its fibres ("(a,ν),(a′,ν′) same fibre iff ν′ = νp^n and a = p^n a′"); (37); **(38)** | p. 32 | verbatim |
| (39); "The set C_{x₀} fibres over the compact group Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p)^, **and the fibres are the ℚ^{>0}_0-orbits in C_{x₀}**"; the canonical projection (40) | p. 33 | verbatim |
| Prop. 5.1 (ρ = 1 ⟺ injective on μ(κ(x))) | p. 34 | verbatim |
| **Thm. 5.2**: the isotropy decomposition; "For any point P₀ ∈ C^E_{x₀} the isotropy group of P₀ is (ℚ^{>0}_0)_{P₀} = Nx₀^ℤ"; "If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}" | p. 34 | verbatim, with the opening of the proof |
| Suspension: X₀ = X̌₀(ℂ)_E ×_{ℚ^{>0}_0} ℝ^{>0}, "(P₀,u)q = (P₀q, q^{-1}u) = (F_q(P₀), q^{-1}u)", the flow φ^t, Γ_{x₀} = C_{x₀} ×_{ℚ^{>0}_0} ℝ^{>0}, "The ℚ^{>0}_0-**bijection** (39) induces an ℝ^{>0}-**bijection**", "all ℝ^{>0}-orbits in Γ_{x₀} are circles ℝ^{>0}/Nx₀^ℤ and Γ_{x₀} fibres over Ẑ^×_{(p)}/p^Ẑ with fibres the ℝ^{>0}-orbits" | p. 38 | verbatim |
| **Thm. 6.1** (periodic points = ⨿_{x₀} Γ^E_{x₀}; isotropy Nx₀^ℤ; "Any periodic orbit γ in X₀ is contained in Γ^E_{x₀} for a uniquely determined point x₀"); the Remark giving X₀ = X̊₀(ℂ)_E ×_{N₀} ℝ^{>0} | p. 39 | verbatim |
| The S4 question ("Is there a sub-dynamical system Y₀ ⊂ X₀ … or at least one which maps to X₀ … such that dim Y₀ = 2d+1 … If d = 1, is there such a Y₀ which is a Riemann surface lamination in the sense of [Ghy99]?") | p. 40 | verbatim |
| §7 opening: the topology of pointwise convergence, Tychonov, metrizability; Lemma 7.1 (pr_X continuous) | p. 40 | verbatim, with proof |
| Lemma 7.3 + (51): F_ν continuous, **closed and open**; F_ν(X̊(ℂ)) = {P : P(μ_ν(K)) = 1} is closed and open | p. 42 | verbatim, with proof |
| The inductive-limit criterion: "Z ⊂ X̌(C) is closed, resp. open if and only if F_ν(Z) ∩ X̊(C) is closed, resp. open in X̊(C) for all ν ∈ N₀"; **Prop. 7.4**: (a) X̊(ℂ) is a **closed and open** subspace of X̌(ℂ); (b) F_q is a **homeomorphism** of X̌(ℂ) for every q ∈ ℚ^{>0}_0; (c) G acts by homeomorphisms; π, π̌ continuous **and open** | p. 43 | verbatim, with proofs |
| **Cor. 7.8** (X̊₀(ℂ) metrizable, δ(π(P),π(P′)) ≤ d(P,P′)), **Cor. 7.9** (X̊(ℂ), X̊₀(ℂ), X̌(ℂ), X̌₀(ℂ) Hausdorff for X₀ with an ample invertible sheaf) | p. 45 | verbatim, with proofs |
| **Thm. 7.10** (the continuous bijections X̊₀(ℂ)_{Q,in} × ℝ^{>0} ⨿ ∐_p X̊₀(ℂ)_{p,in} ×_{p^ℤ} ℝ^{>0} → X₀) | p. 46 | verbatim, with proof |
| Thm. 7.10 **Remark 2**: "The continuous bijections in Theorem 7.10 are **not homeomorphisms in general**" | p. 47 | verbatim |
| E-subspace topologies: "we equip X̊(ℂ)_E and X̊₀(ℂ)_E with the subspace topologies … They agree with the subspace topologies via X̌(ℂ)_E ⊂ X̌(ℂ) and X̌₀(ℂ)_E ⊂ X̌₀(ℂ) because the subspaces F_ν^{-1}X̊(ℂ) and F_ν^{-1}X̊₀(ℂ) are open" | p. 47 | verbatim |
| (66)–(68) and "**The ℚ^{>0}-action on Ȟ_{E_tors} × ℝ^{>0} is not properly discontinuous. In section 10, we will see that this works to our advantage.**" | pp. 48–49 | verbatim |
| §8 opening ("the dynamical system X₀ … is infinite dimensional, whereas we are searching for a system of dimension 2 dim X₀ + 1, e.g. 3 in the case of X₀ = spec ℤ … we will show that the system Y₀ is still infinite-dimensional"), Claim 8.1, and its status for number rings via [Per11, Thm 1] | pp. 49–50 | verbatim |
| **Thm. 8.2** (X̌(ℂ)_per = X̌(S¹), X̌₀(ℂ)_per = X̌₀(S¹)) and its proof, incl. "Since X̊(S¹) is closed in X̊(ℂ) the subspace X̌(S¹) is closed in X̌(ℂ)"; Lemma 8.3 | p. 50 | verbatim |
| **Thm. 9.6's proof**: "We will show below that the only open sets of Y are ∅ and Y … **The fact that Y carries the coarse topology follows from strong approximation for ℚ** … (excluding the infinite place, i.e. the Chinese remainder theorem)", for Y = ℚ^{>0}_0Ẑ^×/ℚ^{>0}_0; also "there is a finite set S of prime numbers such that N₀ is generated by all p ∉ S" | p. 62 | verbatim, with proof |
| Cor. 9.7 (X and X₀ connected for E ⊃ E_f) and its Remark | p. 62 | verbatim |
| §10: Def. 10.1; the sheaf R_X = (π_*R_X̃)^Q; "**Note that in general the continuous bijection π|_{M×{u}} : M×{u} → π(M×{u}) will not be a homeomorphism if π(M×{u}) is equipped with the subspace topology of X.**"; "If Q acts properly discontinuously … then F is an actual 1-codimensional foliation. In general however the partition of X … **will not be locally trivial**." | p. 63 | verbatim |
| Thm. 10.2 (H⁰_F = ℝ) | p. 64 | verbatim, with proof |
| **Prop. 10.3** (Y = ℚ^{>0}_0Ẑ^× ×_{ℚ^{>0}_0} ℝ^{>0} is irreducible) and its **Remark**: "By [LR00, Lemma 3.1], the orbits of the ℚ^{>0}-action on ℚ^{>0}Ẑ^× × ℝ^{>0} are **closed** … it follows that the points of Y are closed, i.e. **Y is a T₁-space**." | p. 64 | verbatim |
| p. 65 Remark 1: "the topology of (Ẑ^× × ℝ^{>0})_adele is reminiscient of the subspace topology induced by the ambient space on a **dense leaf of a foliation**" | p. 65 | verbatim |
| Search performed for the words "Hausdorff", "T₁", "separated", "coarse topology", "indiscrete" over the whole extraction: **[x-03] asserts Hausdorffness of X̊(ℂ), X̊₀(ℂ), X̌(ℂ), X̌₀(ℂ) only (Cor. 7.9, p. 45), and nowhere of the suspension X₀** | whole paper | verified by exhaustive grep |

**[x-06]** C. Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`. Read p. 12 verbatim: "The **compact** subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log Nx₀ … In fact Γ_{x₀} is a **fibre space** over the compact group Aut(F̄_p)/Aut(F_p)^ where p = char κ(x) with fibres the **compact orbits** in Γ_{x₀}." Used only in §6, where its status is analyzed; nothing below rests on it.

**Program-internal, read in the order the charter prescribes** (used as *context and bookkeeping*, never as a substitute for a source): `results/c3-r/probe-9.3-adjudication.md` (binding; §2 anchors, §3 the G1 decision and its scope note, §4 banked items incl. the 2026-09-02 referee-pass block, §5 Q\*, §7 the open items), `probe-9.3-a.md` (Thms A, B, C; §4.1 reachability; §4.3; §6 on G2), `probe-9.3-b.md` (Thm A, Cors A.1–A.3, B; §6.1–§6.4 and §7 with its Session-14 referee block), `probe-9.4-note.md` (Lemmas A–D, Prop. 1, Roads 1–3, DQ-M in §8), `m2c-feasibility-ledger.md` (§5 rows R1/R4/R6/R15, §8 Route 2, §9, §12 addendum), `s2-feasibility-note.md` (W3, model world), `directions/C3-geometric-substrate.md` ("Current frontier"), `results/corpus-routing.md` header caveats.

**Not cited for topology, per adjudication §4 item 4:** [r3s-08] Morishita. It is not used anywhere below. (Theorem 1 supplies a fourth, and now decisive, reason why its "homeomorphism" wording cannot be read as the subspace topology of Γ_p: an indiscrete space with more than one point is homeomorphic to no product of a profinite group with a circle.)

---

## 2. The objects, written out

Throughout, **X₀ = spec ℤ**, K₀ = ℚ, K = ℚ̄, X = spec ℤ̄ (the normalization of spec ℤ in ℚ̄), G = Aut_ℚ(ℚ̄), C = ℂ. Since char X₀ consists of *all* prime numbers and char N₀ ⊇ char X₀, we have **N₀ = N** and ℚ^{>0}_0 = ℚ^{>0} ([x-03] §8 opening, p. 49: "we take N₀ = N").

**2.1 Points.** X̊(ℂ) is the set of pairs (x, P^×) with x ∈ X and P^× : κ(x)^× → ℂ^× a homomorphism ([x-03] p. 22). For affine X (here X = spec ℤ̄) these are identified with the multiplicative maps P : ℤ̄ → ℂ with P(0)=0, P(1)=1, p := P^{-1}(0) an additively closed set (hence a prime ideal), and P factoring through ℤ̄/p (Remark 3.4, p. 23). G acts on the right by (x,P^×)^σ = (x^σ, P^×∘σ); the Frobenius monoid acts by **F_ν(x,P^×) = (x, P^×∘( )^ν)** (p. 22), i.e. on multiplicative maps by F_ν(P)(r) = P(r^ν) = P(r)^ν. X̊₀(ℂ) := X̊(ℂ)/G.

**2.2 Topology.** X̊(ℂ) carries the topology of **pointwise convergence** on ℤ̄ — the subspace topology of the Tychonov topology on ℂ^{ℤ̄} — and is metrizable because ℤ̄ is countable ([x-03] §7 p. 40). X̊₀(ℂ) carries the quotient topology; it is metrizable, separable and Hausdorff (Cor. 7.8, p. 45), with a metric δ satisfying δ(π(P),π(P′)) ≤ d(P,P′). X̌(ℂ) = colim_{N₀} X̊(ℂ) carries the inductive-limit topology; X̊(ℂ) is a **closed and open** subspace of it and every F_q (q ∈ ℚ^{>0}) is a **homeomorphism** (Prop. 7.4, p. 43); π̌ : X̌(ℂ) → X̌₀(ℂ) is continuous and **open** (p. 43). Both X̌(ℂ) and X̌₀(ℂ) are Hausdorff, because spec ℤ is affine and hence carries an ample invertible sheaf (Cor. 7.9, p. 45). For an admissible E the spaces X̊(ℂ)_E, X̊₀(ℂ)_E, X̌(ℂ)_E, X̌₀(ℂ)_E carry the **subspace** topologies, and the inductive-limit topologies agree with them (p. 47). In particular **X̊₀(ℂ)_E is an open subspace of X̌₀(ℂ)_E** (p. 47 with ν = 1).

**2.3 The suspension.** X₀ := X̌₀(ℂ)_E ×_{ℚ^{>0}} ℝ^{>0} is the quotient of X̌₀(ℂ)_E × ℝ^{>0} by the right ℚ^{>0}-action

  (P₀, u)·q = (F_q(P₀), q^{-1}u),  q ∈ ℚ^{>0}  ([x-03] p. 38, verbatim),

with the flow φ^t[P₀,u] = [P₀, u e^t]. We write **q : X̌₀(ℂ)_E × ℝ^{>0} ↠ X₀** for the quotient map and give X₀ the **quotient topology**.

*Anchor for the quotient topology (judgment-grade reading, flagged; identical to the reading used by every previous probe and by the adjudication §2(ii)).* [x-03] never writes the words "quotient topology" for the suspension. Three passages fix it beyond reasonable doubt.
1. §10 p. 63 sets up exactly this projection, π : X̃ = M × ℝ^{>0} → X = M ×_Q ℝ^{>0}, uses its continuity to define the leafwise sheaf R_X = (π_*R_X̃)^Q ⊆ C⁰_X, and states verbatim: "*Note that in general the continuous bijection π|_{M×{u}} : M×{u} → π(M×{u}) will not be a homeomorphism if π(M×{u}) is equipped with the subspace topology of X.*" That sentence presupposes (i) a topology on X making π continuous and (ii) that the subspace topologies induced from X are strictly coarser than the model ones.
2. **Prop. 10.3's Remark (p. 64) computes with that topology explicitly**: "the orbits of the ℚ^{>0}-action on ℚ^{>0}Ẑ^× × ℝ^{>0} are closed … it follows that **the points of Y are closed, i.e. Y is a T₁-space**", for Y = ℚ^{>0}_0Ẑ^× ×_{ℚ^{>0}_0} ℝ^{>0}. The inference "orbits closed upstairs ⟹ points closed downstairs" is *precisely* the quotient-topology inference, and it is Deninger's own.
3. §8 p. 49 speaks of the "topological closure of the union of all periodic orbits" inside X₀.

Every result below uses only that q is **continuous** and **open**; openness is proved in Lemma 3.1 from the ℚ^{>0}-action being by homeomorphisms (Prop. 7.4b), and continuity is the defining property of a quotient. *If one insisted on a strictly coarser topology on X₀ making q continuous, Theorem 1 would only get stronger; a strictly finer one would break Deninger's own inference in item 2.*

**2.4 Packets.** Fix a prime p, a point x ∈ X over p (so κ(x) = F̄_p), and an embedding ι : μ(ℚ̄) ↪ μ(ℂ). With i_x : μ^{(p)}(ℚ̄) ≅ κ(x)^× the reduction isomorphism ((32), p. 31), put χ := ι ∘ i_x^{-1} : F̄_p^× ↪ ℂ^×, an injective character. Since F̄_p^× ≅ ⊕_{ℓ≠p} ℚ_ℓ/ℤ_ℓ and Hom(ℚ_ℓ/ℤ_ℓ, ℂ^×) = ℤ_ℓ, every character of F̄_p^× is **χ^c := χ ∘ ( )^c** for a unique c ∈ Ẑ_{(p)} = ∏_{ℓ≠p}ℤ_ℓ, and Aut(F̄_p^×) = Ẑ^×_{(p)} ([x-03] (34), p. 32). The kernel of χ^c is finite iff c ∈ N·Ẑ^×_{(p)}, and then |ker χ^c| = ∏_ℓ ℓ^{v_ℓ(c)}. The Galois image is Gal(F̄_p/F_p) = p^Ẑ ⊆ Ẑ^×_{(p)} ((34), p. 32). Write

  **B_p := Ẑ^×_{(p)}/p^Ẑ** (a compact group, [x-03] p. 33; uncountable — adjudication §2, re-derived there).

C_{x₀} ⊂ X̌₀(ℂ) is the ℚ^{>0}-saturation of the fibre of pr₀ over x₀ = (p) (p. 31); (38)/(39) give C_{x₀} ≅ B_p ×_{p^ℤ} ℚ^{>0} as ℚ^{>0}-sets, "**and the fibres are the ℚ^{>0}-orbits in C_{x₀}**" (p. 33). Γ^E_{x₀} := C^E_{x₀} ×_{ℚ^{>0}} ℝ^{>0} ⊆ X₀ is the packet; by Thm. 6.1 (p. 39) the periodic points of X₀ are exactly ⨿_{x₀} Γ^E_{x₀}, and the isotropy of every packet point is Nx₀^ℤ = p^ℤ. Under (37) the pair (a,ν) ∈ Ẑ^×_{(p)} × N maps to π(x, χ^{aν}); hence every ℚ^{>0}-orbit inside C_{x₀} contains a point (x, χ^a) with a ∈ Ẑ^×_{(p)} (its class [a] ∈ B_p is the orbit's coordinate in the fibration), so **every point of Γ^E_{(p)} can be written [ P^a , w ] with a ∈ Ẑ^×_{(p)}, χ^a ∈ E and w ∈ ℝ^{>0}**, where P^a := π(x,χ^a) ∈ X̊₀(ℂ).

*Frobenius acts trivially on P^a.* By (23) (p. 22) the stabilizer G_x surjects onto Gal(κ(x)/κ(x₀)) = Gal(F̄_p/F_p), so there is σ ∈ G with x^σ = x inducing y ↦ y^p on F̄_p. Then (x,χ^a)^σ = (x, χ^a∘( )^p) = (x, χ^{ap}) = F_p(x,χ^a). Hence **F_p(P^a) = P^a in X̌₀(ℂ)**, which is the isotropy statement of Thm. 5.2 (p. 34) made explicit.

---

## 3. Topology bookkeeping (three lemmas, proved in full)

These are the only structural facts about the suspension used later. All three are elementary; they are written out because everything downstream rests on them.

**Lemma 3.1 (q is open).** The quotient map q : X̌₀(ℂ)_E × ℝ^{>0} → X₀ is open.

*Proof.* Let U be open in X̌₀(ℂ)_E × ℝ^{>0}. Then q^{-1}(q(U)) = ⋃_{r ∈ ℚ^{>0}} U·r. For each r the map (P,u) ↦ (P,u)·r = (F_r P, r^{-1}u) is a homeomorphism of X̌₀(ℂ)_E × ℝ^{>0}: F_r is a homeomorphism of X̌(ℂ) ([x-03] Prop. 7.4b, p. 43), it commutes with G and π̌ is an open continuous surjection (p. 43), so F_r descends to a homeomorphism of X̌₀(ℂ); it preserves X̌₀(ℂ)_E in both directions (Prop. 4.2, p. 27) and hence is a homeomorphism of the subspace X̌₀(ℂ)_E (p. 47); and u ↦ r^{-1}u is a homeomorphism of ℝ^{>0}. Hence each U·r is open, so q^{-1}(q(U)) is open, so q(U) is open by definition of the quotient topology. ∎

**Lemma 3.2 (subspace = sub-suspension).** Let E′ ⊆ E be admissible classes. Then the natural continuous bijection
  X₀^{E′} = X̌₀(ℂ)_{E′} ×_{ℚ^{>0}} ℝ^{>0} ⟶ q( X̌₀(ℂ)_{E′} × ℝ^{>0} ) ⊆ X₀^E
is a **homeomorphism onto its image with the subspace topology**. The same holds for the ℚ^{>0}-invariant subset X̌₀(S¹) ⊆ X̌₀(ℂ) and its suspension Y₀^Den.

*Proof.* Put Z := X̌₀(ℂ)_E × ℝ^{>0}, A := X̌₀(ℂ)_{E′} × ℝ^{>0}. By Prop. 4.2 (p. 27) X̌₀(ℂ)_{E′} is ℚ^{>0}-invariant, so A is q-saturated, and A carries the subspace topology of Z (p. 47 for the character factor). Let q_A := q|_A : A → q(A). It is continuous and surjective. If U = A ∩ V with V open in Z, then q_A(U) = q(A) ∩ q(V): "⊆" is clear, and if y = q(a) = q(v) with a ∈ A, v ∈ V then v lies in the ℚ^{>0}-orbit of a, hence in A by saturation, so v ∈ A ∩ V and y ∈ q(A∩V). By Lemma 3.1 q(V) is open, so q_A(U) is open in q(A). Thus q_A is a continuous **open** surjection, i.e. a quotient map onto q(A) with the subspace topology; since its fibres are exactly the ℚ^{>0}-orbits, the induced bijection from A/ℚ^{>0} = X₀^{E′} is a homeomorphism. For X̌₀(S¹): it is ℚ^{>0}-invariant (F_ν(P)(r) = P(r)^ν has modulus 1 iff P(r) does) and is treated by [x-03] as a subspace of X̌₀(ℂ) (p. 50: "Since X̊(S¹) is closed in X̊(ℂ) the subspace X̌(S¹) is closed in X̌(ℂ)"), so the same argument applies. ∎

*Consequence used repeatedly:* for a cut class E(a) ⊆ E_max, the suspension X₀^{E(a)} built abstractly and the subset of X₀ = X₀^{E_max} that it names are the **same topological space**. So the four charter questions are unambiguous.

**Lemma 3.3 (packets are pairwise separated by open sets of X₀).** Let q₀ be a prime. There is an open set V_{q₀} ⊆ X₀ = X₀^{E_max} with
  Γ_{(q₀)} ⊆ V_{q₀}  and V_{q₀} ∩ Γ_{(p)} = ∅ for every prime p ≠ q₀.

*Proof.* Put D := { P ∈ X̊(ℂ) : |P(q₀)| < ½ } (evaluation at the element q₀ ∈ ℤ̄). Since the topology on X̊(ℂ) is pointwise convergence (p. 40), evaluation at q₀ is continuous and D is open in X̊(ℂ); since X̊(ℂ) is open in X̌(ℂ) (Prop. 7.4a, p. 43), **D is open in X̌(ℂ)**. D is G-invariant, because q₀ ∈ ℚ is fixed by every σ ∈ G and so (P∘σ)(q₀) = P(q₀). Let S := ⋃_{r ∈ ℚ^{>0}} F_r(D): it is open (each F_r is a homeomorphism of X̌(ℂ), Prop. 7.4b), ℚ^{>0}-invariant by construction, and G-invariant (G commutes with the F_r, p. 22). Put V_{q₀} := q( π̌(S) × ℝ^{>0} ), open in X₀ because π̌ is open (p. 43) and q is open (Lemma 3.1).

*Γ_{(q₀)} ⊆ V_{q₀}:* a point of Γ_{(q₀)} is [P^a, w] with P^a = π(x,χ^a), x over q₀ (§2.4); the representative (x,χ^a) ∈ X̊(ℂ) has (x,χ^a)(q₀) = 0 because q₀ ∈ p̄_x, so it lies in D ⊆ S.

*V_{q₀} ∩ Γ_{(p)} = ∅ for p ≠ q₀:* since S is ℚ^{>0}- and G-invariant, [P′,w] ∈ V_{q₀} iff P′ ∈ π̌(S) iff some representative of some ℚ^{>0}-translate of P′ lies in D. Now let P′ ∈ C_{x₀} with x over p. The projection pr_X is ℚ^{>0}-equivariant for the trivial action on X (p. 27), so every ℚ^{>0}G-translate of P′ that lies in X̊(ℂ) is a pair (y, ψ) with y over p and ψ a character of κ(y)^× = F̄_p^×; its value at q₀ is ψ(q₀ mod p̄_y), and q₀ ∉ p̄_y because p ≠ q₀, so q₀ mod p̄_y ∈ F̄_p^× is a root of unity and its ψ-value is a root of unity, of modulus 1 ≥ ½. Hence no translate lies in D, i.e. [P′,w] ∉ V_{q₀}. ∎

*(Correction to the partial draft: it derived the openness of D in X̌(ℂ) from the inductive-limit criterion, citing it to p. 42; the criterion is on p. 43, and the derivation is unnecessary because Prop. 7.4a already gives it. The simplified proof above is the one that stands.)*

---

## 4. The cut classes E(a): definition, admissibility, reachability

**4.1 Definition.** For each prime p fix a₀(p) ∈ Ẑ^×_{(p)} (equivalently, a base class [a₀(p)] ∈ B_p) and let χ_p := χ_{x_p}^{a₀(p)} be the corresponding injective character of F̄_p^×. Define

  **E(a)** := the smallest admissible class containing { χ_p : p prime } (with empty characteristic-0 part),
  **E(a)′** := E(a) ∪ { all characters χ : κ^× → ℂ^× with char κ = 0 satisfying (Tors) }.

Def. 4.1's two closure operations (pre-composition with Aut κ, and ν-th powers) never change the field κ, so a class may be prescribed field by field; E(a)′ is admissible as soon as E(a) is. *Well-definedness across isomorphic fields:* the prescription on an algebraically closed κ ≅ F̄_p requires an isomorphism, but the ambiguity is exactly Aut(F̄_p), and the class (★) below is Aut(F̄_p)-stable by construction, so the prescription is independent of the choice.

**4.2 The exponent computation (reachability), re-derived here.** In residue characteristic p the moves of Def. 4.1 act on exponents c ∈ Ẑ_{(p)} of χ^c by
  (i) c ↦ cσ, σ ∈ p^Ẑ = image of Aut(F̄_p) in Aut(F̄_p^×) ((34), p. 32);
  (ii) c ↦ cν, ν ∈ N (by (35), p. 32: χ_x·(a,ν) = χ_x∘( )^a∘( )^ν);
  (iii) *backwards*: if cν is in the class and c ∈ Ẑ_{(p)}, then c is in the class (Def. 4.1's "if and only if").

Note that every ν ∈ N is a non-zero-divisor in Ẑ_{(p)} = ∏_{ℓ≠p}ℤ_ℓ (each ℤ_ℓ is a domain and ν ≠ 0 in it), and p is a **unit** there; so the relation
  d ~ a₀ :⟺ ∃ σ ∈ p^Ẑ, ν, ν′ ∈ N with dν = a₀σν′
is reflexive, symmetric (σ ↦ σ^{-1}) and transitive (multiply the two equations and use commutativity), i.e. it is exactly the equivalence generated by (i)–(iii). Write ν′/ν in lowest terms as m/n with gcd(m,n) = 1. Then d = a₀σ·m/n lies in Ẑ_{(p)} iff n is a unit in every ℤ_ℓ with ℓ ≠ p, i.e. iff n = p^j; and p^{-j} ∈ p^ℤ ⊆ p^Ẑ. Splitting m = p^k m′ with p ∤ m′ we obtain

  **E(a)-locus in characteristic p = { χ^d : d ∈ a₀·p^Ẑ·N^{(p)} }**,  N^{(p)} := { m ∈ N : p ∤ m }.  (★)

*This set is admissible.* Forward closure under (i) and (ii) is immediate from (★). Backward closure: suppose χ^{dν} lies in (★), say dν = a₀σm with σ ∈ p^Ẑ, p ∤ m, and d ∈ Ẑ_{(p)}. Write ν = p^k ν′ with p ∤ ν′. Then p^k ν′ d = a₀σm, so for every ℓ ≠ p, v_ℓ(d) = v_ℓ(m) − v_ℓ(ν′) ≥ 0, whence ν′ | m in ℤ and d = a₀σ p^{−k}(m/ν′) ∈ a₀p^Ẑ N^{(p)}. Closure under Aut κ is (i). (Tors) holds for every member: ker χ^{a₀σm′} = μ_{m′} ⊂ F̄_p^×, of order m′ ∈ N = N₀. ∎

*The injective members.* χ^d is injective iff d ∈ Ẑ^×_{(p)}, i.e. iff m′ = 1 in (★), i.e. **d ∈ a₀·p^Ẑ**: a single base class [a₀] ∈ B_p. (This re-derives probe A's Theorem C(b)/§4.1 and the adjudication §4 item 5b independently; the unit parts u(ℓ) of other primes are **not** reachable, because a₀σm′ is a unit only for m′ = 1.)

**4.3 Clause (4): one orbit per packet, for every choice of a — YES.**

**Proposition 4.1.** For every choice a = (a₀(p))_p and for E ∈ {E(a), E(a)′}: for every prime p,
  Γ^{E}_{(p)} = the single ℝ^{>0}-orbit through [P^{a₀(p)}, 1], a circle of length log p,
and by [x-03] Thm. 6.1 (p. 39) these are **all** the periodic orbits of X₀^{E}. In particular the T1 counting requirement "coefficient exactly 1 per prime" (ledger §3) is met at the level of *sets and orbits*.

*Proof.* A point of C_{x₀} is, by (37)–(39), the class of a pair (a, ν) with a ∈ Ẑ^×_{(p)} (mod p^Ẑ) and ν ∈ ℚ^{>0}, and it lies in C^E_{x₀} iff the character of its X̊-representative, namely χ^{aν} for ν ∈ N, is in E (Prop. 4.2's backward invariance, p. 27). By (★), χ^{aν} ∈ E(a) iff aν ∈ a₀p^Ẑ N^{(p)}; comparing ℓ-valuations for all ℓ ≠ p (a is a unit) forces the N^{(p)}-factor to be the prime-to-p part ν^{(p)} of ν, whence a = a₀σ ν^{(p)}/ν = a₀σ p^{−v_p(ν)} ∈ a₀p^Ẑ. So C^{E}_{x₀} consists exactly of the points lying over the single base class [a₀] ∈ B_p. By [x-03] p. 33 verbatim, "*the fibres are the ℚ^{>0}-orbits in C_{x₀}*", so C^{E}_{x₀} is exactly one ℚ^{>0}-orbit, and Γ^{E}_{x₀} = C^{E}_{x₀} ×_{ℚ^{>0}} ℝ^{>0} is exactly one ℝ^{>0}-orbit. Its isotropy is p^ℤ (Thm. 5.2, p. 34), so it is a circle of length log p. Finally E(a), E(a)′ ⊆ E_tors = E_max over spec ℤ — (Image) constrains only characters of fields of positive characteristic whose multiplicative group is non-torsion, and κ(x)^× = F̄_p^× is torsion while (Image) is explicitly declared "Only if char κ > 0" (p. 27) — so Thm. 6.1 applies and gives that the points of X₀^E with non-trivial isotropy are exactly ⨿_{x₀} Γ^E_{x₀}. ∎

**Remark 4.2 (what clause (4) does and does not buy).** This is a genuine *construction*, and it is the only clause of the charter that succeeds. It is however exactly the object the adjudication already priced: the choice of a is an arbitrary point of the uncountable Cantor group B_p **for every prime**, no canonical selection exists (adjudication §4 item 5; 9.4 Prop. 1: no Aut(ℂ)-stable selection exists at all), and X₀^{E(a)} forfeits every theorem [x-03] proves for E ⊇ E_f (connectedness Cor. 9.7 p. 62, H⁰_F = ℝ Thm. 10.2 p. 64, and the closure identification Thm. 8.2 p. 50, whose approximants are arbitrary finite-kernel characters; also Cor. 4.4's surjectivity of pr_{X₀}, p. 28). Nothing below rests on re-proving any of those for E(a); the point of §§5–7 is that the *topology* of X₀^{E(a)} destroys the candidate regardless.
