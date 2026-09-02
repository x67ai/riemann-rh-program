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

C_{x₀} ⊂ X̌₀(ℂ) is the ℚ^{>0}-saturation of the fiber of pr₀ over x₀ = (p) (p. 31); (38)/(39) give C_{x₀} ≅ B_p ×_{p^ℤ} ℚ^{>0} as ℚ^{>0}-sets, "**and the fibres are the ℚ^{>0}-orbits in C_{x₀}**" (p. 33). Γ^E_{x₀} := C^E_{x₀} ×_{ℚ^{>0}} ℝ^{>0} ⊆ X₀ is the packet; by Thm. 6.1 (p. 39) the periodic points of X₀ are exactly ⨿_{x₀} Γ^E_{x₀}, and the isotropy of every packet point is Nx₀^ℤ = p^ℤ. Under (37) the pair (a,ν) ∈ Ẑ^×_{(p)} × N maps to π(x, χ^{aν}); hence every ℚ^{>0}-orbit inside C_{x₀} contains a point (x, χ^a) with a ∈ Ẑ^×_{(p)} (its class [a] ∈ B_p is the orbit's coordinate in the fibration), so **every point of Γ^E_{(p)} can be written [ P^a , w ] with a ∈ Ẑ^×_{(p)}, χ^a ∈ E and w ∈ ℝ^{>0}**, where P^a := π(x,χ^a) ∈ X̊₀(ℂ).

*Frobenius acts trivially on P^a.* By (23) (p. 22) the stabilizer G_x surjects onto Gal(κ(x)/κ(x₀)) = Gal(F̄_p/F_p), so there is σ ∈ G with x^σ = x inducing y ↦ y^p on F̄_p. Then (x,χ^a)^σ = (x, χ^a∘( )^p) = (x, χ^{ap}) = F_p(x,χ^a). Hence **F_p(P^a) = P^a in X̌₀(ℂ)**, which is the isotropy statement of Thm. 5.2 (p. 34) made explicit.

---

## 3. Topology bookkeeping (three lemmas, proved in full)

These are the only structural facts about the suspension used later. All three are elementary; they are written out because everything downstream rests on them.

**Lemma 3.1 (q is open).** The quotient map q : X̌₀(ℂ)_E × ℝ^{>0} → X₀ is open.

*Proof.* Let U be open in X̌₀(ℂ)_E × ℝ^{>0}. Then q^{-1}(q(U)) = ⋃_{r ∈ ℚ^{>0}} U·r. For each r the map (P,u) ↦ (P,u)·r = (F_r P, r^{-1}u) is a homeomorphism of X̌₀(ℂ)_E × ℝ^{>0}: F_r is a homeomorphism of X̌(ℂ) ([x-03] Prop. 7.4b, p. 43), it commutes with G and π̌ is an open continuous surjection (p. 43), so F_r descends to a homeomorphism of X̌₀(ℂ); it preserves X̌₀(ℂ)_E in both directions (Prop. 4.2, p. 27) and hence is a homeomorphism of the subspace X̌₀(ℂ)_E (p. 47); and u ↦ r^{-1}u is a homeomorphism of ℝ^{>0}. Hence each U·r is open, so q^{-1}(q(U)) is open, so q(U) is open by definition of the quotient topology. ∎

**Lemma 3.2 (subspace = sub-suspension).** Let E′ ⊆ E be admissible classes. Then the natural continuous bijection
  X₀^{E′} = X̌₀(ℂ)_{E′} ×_{ℚ^{>0}} ℝ^{>0} ⟶ q( X̌₀(ℂ)_{E′} × ℝ^{>0} ) ⊆ X₀^E
is a **homeomorphism onto its image with the subspace topology**. The same holds for the ℚ^{>0}-invariant subset X̌₀(S¹) ⊆ X̌₀(ℂ) and its suspension Y₀^Den.

*Proof.* Put Z := X̌₀(ℂ)_E × ℝ^{>0}, A := X̌₀(ℂ)_{E′} × ℝ^{>0}. By Prop. 4.2 (p. 27) X̌₀(ℂ)_{E′} is ℚ^{>0}-invariant, so A is q-saturated, and A carries the subspace topology of Z (p. 47 for the character factor). Let q_A := q|_A : A → q(A). It is continuous and surjective. If U = A ∩ V with V open in Z, then q_A(U) = q(A) ∩ q(V): "⊆" is clear, and if y = q(a) = q(v) with a ∈ A, v ∈ V then v lies in the ℚ^{>0}-orbit of a, hence in A by saturation, so v ∈ A ∩ V and y ∈ q(A∩V). By Lemma 3.1 q(V) is open, so q_A(U) is open in q(A). Thus q_A is a continuous **open** surjection, i.e. a quotient map onto q(A) with the subspace topology; since its fibers are exactly the ℚ^{>0}-orbits, the induced bijection from A/ℚ^{>0} = X₀^{E′} is a homeomorphism. For X̌₀(S¹): it is ℚ^{>0}-invariant (F_ν(P)(r) = P(r)^ν has modulus 1 iff P(r) does) and is treated by [x-03] as a subspace of X̌₀(ℂ) (p. 50: "Since X̊(S¹) is closed in X̊(ℂ) the subspace X̌(S¹) is closed in X̌(ℂ)"), so the same argument applies. ∎

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

---

## 5. THEOREM 1: the packets are indiscrete subspaces of X₀

This is the result that decides face (a). It is proved from [x-03]'s definitions only; no result of any program note is used as an input.

**Lemma 5.1 (Frobenius twists converge).** Let p be a prime, a ∈ Ẑ^×_{(p)}, c ∈ Ẑ_{(p)}, and let (m_k) ⊂ N satisfy m_k → c in Ẑ_{(p)} = lim_{(M,p)=1} ℤ/M. Then
  (x, χ^{a m_k}) ⟶ (x, χ^{a c}) in X̊(ℂ),
and consequently P^{a m_k} = π(x,χ^{am_k}) → π(x,χ^{ac}) in X̊₀(ℂ), hence in X̌₀(ℂ), hence in X̌₀(ℂ)_E for any admissible E containing χ^{a} and χ^{ac}.

*Proof.* The topology on X̊(ℂ) is pointwise convergence of the multiplicative maps ℤ̄ → ℂ ([x-03] §7 p. 40). Fix r ∈ ℤ̄. If r ∈ p̄_x then both (x,χ^{am_k})(r) and (x,χ^{ac})(r) are 0 (Remark 3.4, p. 23). Otherwise r̄ := r mod p̄_x ∈ F̄_p^×; since F̄_p^× = μ^{(p)} is torsion of order prime to p, r̄ has finite order d with p ∤ d. Now χ^{am_k}(r) = χ(r̄^{\,a m_k}) depends only on a m_k mod d, and reduction Ẑ_{(p)} → ℤ/d is a ring homomorphism, so m_k → c in Ẑ_{(p)} gives a m_k ≡ a c (mod d) for all large k, i.e. χ^{am_k}(r) = χ^{ac}(r) **exactly, eventually**. Pointwise convergence follows. The push-forwards: π is continuous with δ(π(P),π(P′)) ≤ d(P,P′) (Cor. 7.8, p. 45); X̊₀(ℂ) is an open subspace of X̌₀(ℂ) (Prop. 7.4a and p. 47); and the E-spaces carry the subspace topologies (p. 47), so a convergent sequence all of whose terms and whose limit lie in X̌₀(ℂ)_E converges there. Membership: χ^{am_k} = (χ^a)∘( )^{m_k} = F_{m_k}(χ^a) ∈ E by Def. 4.1's biconditional ν-closure (p. 27); and (Tors) holds with |ker| = (prime-to-p part of m_k) ∈ N = N₀. ∎

**Lemma 5.2 (simultaneous profinite and archimedean approximation).** Let p be a prime, c ∈ Ẑ_{(p)}, t ∈ ℝ^{>0}. Then there are m_k ∈ N and j_k ∈ ℤ with
  m_k → c in Ẑ_{(p)}  and m_k p^{-j_k} → t in ℝ^{>0}.

*Proof.* Set M_k := ∏_{ℓ ≤ k, ℓ ≠ p} ℓ^k, so that every integer M prime to p divides M_k for all large k. By the Chinese remainder theorem the reduction N ↠ ℤ/M_k is surjective, so pick c_k ∈ ℤ with c_k ≡ c (mod M_k). Choose j_k ∈ N so large that M_k p^{-j_k} < 1/k and t p^{j_k} > M_k. Let m_k be the unique integer in the interval [t p^{j_k}, t p^{j_k} + M_k) with m_k ≡ c_k (mod M_k) — the interval has length M_k, so exactly one residue-class representative lies in it. Then m_k > M_k > 0, so m_k ∈ N; m_k ≡ c (mod M_k), hence m_k ≡ c (mod M) for every fixed M prime to p and all large k, i.e. m_k → c in Ẑ_{(p)}; and |m_k p^{-j_k} − t| < M_k p^{-j_k} < 1/k. ∎

*(This is the same mechanism Deninger himself uses on the generic fiber: "The fact that Y carries the coarse topology follows from **strong approximation for ℚ** … (excluding the infinite place, i.e. the Chinese remainder theorem)", [x-03] proof of Thm. 9.6, p. 62. Here the "excluded infinite place" is restored by the p^ℤ-isotropy, which is exactly the extra freedom the packets have and the idelic space of Thm. 9.6 does not.)*

**THEOREM 1.** Let X₀ = spec ℤ, let E be **any** admissible class with E ⊆ E_max, and let X₀ = X̌₀(ℂ)_E ×_{ℚ^{>0}} ℝ^{>0} with the quotient topology. Fix a prime p and let

  z = [P^a, w] and z′ = [P^b, u],  a, b ∈ Ẑ^×_{(p)}, χ^a, χ^b ∈ E, w, u ∈ ℝ^{>0},

be **any two points of the packet Γ^E_{(p)}**. Then z′ ∈ cl_{X₀}({z}).

*Proof.* Put c := b a^{-1} ∈ Ẑ^×_{(p)} ⊆ Ẑ_{(p)} and t := w/u ∈ ℝ^{>0}. By Lemma 5.2 choose m_k ∈ N and j_k ∈ ℤ with m_k → c in Ẑ_{(p)} and m_k p^{-j_k} → t. Set r_k := m_k p^{-j_k} ∈ ℚ^{>0} and consider the points of the ℚ^{>0}-orbit of (P^a, w) in X̌₀(ℂ)_E × ℝ^{>0}:

  (P^a, w)·r_k = ( F_{r_k}(P^a), r_k^{-1} w ).

*First coordinate.* By §2.4 (equivalently [x-03] Thm. 5.2, p. 34) the isotropy group of P^a ∈ C^E_{x₀} in ℚ^{>0} is exactly Nx₀^ℤ = p^ℤ, so F_{p^{-j_k}}(P^a) = P^a and therefore
  F_{r_k}(P^a) = F_{m_k}(F_{p^{-j_k}}(P^a)) = F_{m_k}(P^a) = π(x, χ^{a m_k}),
using F_ν(x,P^×) = (x, P^×∘( )^ν) (p. 22) and the exponent convention of (35) (p. 32). By Lemma 5.1, F_{m_k}(P^a) → π(x, χ^{ac}) = π(x, χ^{b}) = P^b in X̌₀(ℂ)_E.

*Second coordinate.* r_k^{-1} w = w/(m_k p^{-j_k}) → w/t = u in ℝ^{>0}.

Hence (P^a, w)·r_k → (P^b, u) in the product X̌₀(ℂ)_E × ℝ^{>0}. Now let U ⊆ X₀ be any open set containing z′ = q(P^b,u). Then q^{-1}(U) is open (q continuous) and contains (P^b,u), hence contains (P^a,w)·r_k for all large k; but q((P^a,w)·r_k) = q(P^a,w) = z for every k, by the definition of X₀ as the orbit space. So z ∈ U. As U was arbitrary, z lies in every neighborhood of z′, i.e. z′ ∈ cl_{X₀}({z}). ∎

**Remarks on the proof.**
1. *What makes it work.* The suspension identification lets one move along the orbit by any r ∈ ℚ^{>0}; the character coordinate sees only r modulo the isotropy p^ℤ, i.e. only the class of m_k in Ẑ_{(p)}, while the ℝ-coordinate sees the *real* number m_k p^{-j_k}. The two are decoupled precisely because p is a unit in Ẑ_{(p)} but not in ℝ. Deninger's own Remark after Prop. 10.3 (p. 64) shows that on the **idelic** model ℚ^{>0}Ẑ^× × ℝ^{>0} the ℚ^{>0}-orbits *are* closed and the quotient is T₁ — there is no isotropy there to decouple the two coordinates. The packets are exactly where the decoupling happens.
2. *No Hausdorffness, metrizability, compactness, closedness or sequential axiom is used anywhere.* Only: F_ν(x,P^×) = (x,P^×∘( )^ν); the isotropy statement of Thm. 5.2; the pointwise-convergence topology; continuity of π, of the inclusions of the E-subspaces, and of q. The final step is a bare neighborhood argument, not an appeal to uniqueness of sequential limits.
3. *Symmetry.* Applying the theorem with (z,z′) interchanged gives z ∈ cl({z′}): the two points are **topologically indistinguishable** in X₀, i.e. they have the same neighborhood filter.
4. *The single-orbit case is included.* Taking b = a and w ≠ u (so c = 1) gives: any two points of one periodic orbit are topologically indistinguishable. This is the case the adjudication's scope note (§3) explicitly left undecided for the cut classes.
5. *Generality.* The proof is written for spec ℤ because that is the S4 case. For a general arithmetic X₀, replace p by Nx₀ = |κ(x₀)| throughout; Lemma 5.1 is unchanged, and Lemma 5.2 needs m_k ∈ N₀ (rather than N) in a prescribed residue class prime to p and in a prescribed real window — obtainable from the prime number theorem in arithmetic progressions, since N₀ contains all but finitely many primes ([x-03] p. 62: "there is a finite set S of prime numbers such that N₀ is generated by all p ∉ S"). *That extension is a sketch and is flagged; nothing below uses it.*

### 5.1 Corollaries

**Corollary 1.1 (indiscreteness).** For every prime p and every admissible E ⊆ E_max, the packet Γ^E_{(p)} carries the **indiscrete** topology as a subspace of X₀: its only relatively open subsets are ∅ and Γ^E_{(p)}. The same holds for every ℝ^{>0}-orbit γ ⊆ Γ^E_{(p)} — in particular **a single periodic orbit of X₀ is an indiscrete subspace**, and it has continuum many points, being in ℝ^{>0}-equivariant bijection with ℝ^{>0}/p^ℤ ([x-03] p. 38). Consequently **X₀ is not T₀**.

*Proof.* Let U be open in X₀ with U ∩ Γ^E_{(p)} ≠ ∅, say z ∈ U. For any z′ ∈ Γ^E_{(p)}, Remark 3 gives that z and z′ have the same neighborhood filter, so z′ ∈ U. Hence U ⊇ Γ^E_{(p)}. The same argument inside a single orbit gives the orbit statement, taking b = a in Theorem 1 (Remark 4). ∎

**Corollary 1.2 (Q-a is NO).** Let Y ⊆ X₀ be flow-invariant and suppose Y ∩ Γ^E_{(p)} ≠ ∅ for at least one prime p. Then Y is not T₀ in its subspace topology; a fortiori not Hausdorff, not metrizable, not a foliated space, not a lamination. In particular:

> **there is no compact, Hausdorff-in-its-subspace-topology, flow-invariant subspace Y ⊆ X₀ of any dimension meeting each packet in exactly one orbit.** Face (a) of Q\* has answer **NO**, for every admissible E, and equally for the unitary system Y₀^Den = X̌₀(S¹) ×_{ℚ^{>0}} ℝ^{>0} (Lemma 3.2 identifies its topology with the subspace topology in X₀, and the entire proof of Theorem 1 takes place inside the packet, whose characters are unitary — all their values are roots of unity, so every point and every approximant used above lies in X̊₀(S¹)).

*Proof.* Y flow-invariant and meeting a packet means Y contains a full ℝ^{>0}-orbit of X₀ inside that packet (packets are flow-invariant, Thm. 6.1 p. 39). That orbit is infinite and indiscrete in X₀ (Cor. 1.1), hence indiscrete in Y; a T₀ space has no indiscrete subspace with two distinct points. ∎

**Corollary 1.3 (Theorem A, W12, and the closure equality are special cases).** For any periodic orbit γ ⊆ Γ^E_{(p)} and any z ∈ γ: cl_{X₀}({z}) ⊇ Γ^E_{(p)}, hence a fortiori cl_{X₀}(γ) ⊇ Γ^E_{(p)}. This re-proves the banked **Theorem A** (packet-closure law) and, with Cor. 1.1, the banked **Corollary A.2 / ledger row W12** (X₀ non-Hausdorff along packets) — both now as corollaries of a strictly stronger statement, and by an argument that does not need W12's "two distinct base classes" hypothesis (adjudication §3, scope note). Combining with the Session-14 referee-banked fact that every packet is a **closed** flow-invariant subset of X₀ (adjudication §4 item 1's 2026-09-02 block; probe B §7's block), one gets the sharp form

  **cl_{X₀}({z}) = Γ^E_{(p)} for every single point z of the packet** — not merely for every orbit.

In particular W12's stated exception — "*for probe A's minimal cut classes E(a₀), whose packet E-locus is a single orbit, this argument produces no second limit and decides nothing*" — is now removed: **the cut suspensions are non-Hausdorff too**, by Theorem 1 with b = a.

**Corollary 1.4 (the closed half of S4 dies again, and more cheaply).** No flow-invariant subset of X₀ containing a periodic orbit — closed or not, compact or not — is a compact metrizable lamination, since none is even T₀. This subsumes the banked "closed half of S4 is dead" (adjudication §4 item 2) without using Thm. 8.2, Claim 8.1/[Per11], the uncountability of B_p, or any dimension theory. Those routes remain correct and remain the right citation for the *orbit-count* statement (uncountably many closed orbits per prime, which Theorem 1 does not give); Theorem 1 adds an independent and more elementary route to the *topological* half.

**Corollary 1.5 (Deninger's own question, subspace alternative).** [x-03] p. 40 asks: "*Is there a sub-dynamical system Y₀ ⊂ X₀ = X̌₀(ℂ) ×_{ℚ^{>0}} ℝ^{>0} or at least one which maps to X₀ such that dim Y₀ = 2d+1 where d = dim X₀ and such that Y₀ contains at least one periodic orbit in Γ_{x₀} for every closed point x₀ of X₀? If d = 1, is there such a Y₀ which is a Riemann surface lamination in the sense of [Ghy99]?*" Read with "sub-dynamical system" = flow-invariant **subspace** (with no closedness assumed) and "Riemann surface lamination" entailing (as it does) a Hausdorff, indeed metrizable, topology, the answer is **NO**, unconditionally: any such Y₀ contains a periodic orbit, which is an indiscrete subspace. The remaining alternative in Deninger's own sentence — "*or at least one which maps to X₀*" — is untouched, and is exactly Q-b.

---

## 6. Interlude: the model description of a packet is not a topological description

Theorem 1 is not in conflict with anything [x-03] *states*, and the reason is worth recording because the program has stumbled over it once already (ledger row W11).

* Deninger's packet description in the technical paper is stated as a **bijection**, never a homeomorphism: "*The ℚ^{>0}_0-**bijection** (39) induces an ℝ^{>0}-**bijection** (Ẑ^×_{(p)}/Nx₀^Ẑ) ×_{p^ℤ/deg x₀} ℝ^{>0}/Nx₀^ℤ ≅ Γ_{x₀}*" ([x-03] p. 38). Theorem 7.10 supplies the same object as a continuous bijection X̊₀(ℂ)_{p,in} ×_{p^ℤ} ℝ^{>0} → X₀ (p. 46), and its Remark 2 (p. 47) warns: "*The continuous bijections in Theorem 7.10 are not homeomorphisms in general.*" Theorem 1 says exactly how badly this one fails.
* §10 p. 63 states the failure for the transverse direction explicitly: "*Note that in general the continuous bijection π|_{M×{u}} : M×{u} → π(M×{u}) will not be a homeomorphism if π(M×{u}) is equipped with the subspace topology of X*", and adds that when the ℚ^{>0}-action is not properly discontinuous "*the partition of X … will not be locally trivial*". §7 p. 49 records that the action **is** not properly discontinuous — "*and in section 10, we will see that this works to our advantage*". Theorem 1 is the same phenomenon in the **flow** direction, taken to its extreme: the model circle ℝ^{>0}/p^ℤ maps continuously and bijectively onto γ_p ⊂ X₀, but γ_p's own topology is indiscrete.
* **The one place where the wording must be read with care is the survey.** [x-06] p. 12 says: "*In fact Γ_{x₀} is a fibre space over the compact group Aut(F̄_p)/Aut(F_p)^ … with fibres the compact orbits in Γ_{x₀}*", and [x-03]'s introduction (pp. 2–3) says "*Γ_{x₀} is fibred over the compact group*" and calls the packets "*compact packets … reminiscient of invariant tori*". Read topologically in the subspace topology, "fibre space" is **false**: a continuous map from an indiscrete space to a Hausdorff group is constant, so the fibration map Γ_p → B_p is not continuous for the subspace topology, and Γ_p is not a fiber space over B_p in any topological sense. Read as a statement about the model (39) — which is how [x-03] states it, and which its own Remark 2 on p. 47 and §10 p. 63 instruct the reader to do — it is correct and is all Deninger claims. *This note therefore reads the intro/survey adjectives as model-level, and records the discrepancy explicitly rather than silently.* The word "compact" is separately harmless: an indiscrete space **is** compact, so the assertion is true but, in the subspace topology, topologically vacuous (Prop. 7.3(a) below) — and in particular it must never be read as "compact Hausdorff".
* The character space is *not* to blame. X̌₀(ℂ) is Hausdorff (Cor. 7.9, p. 45, applicable since spec ℤ is affine), and the injective part of C_{x₀} is, with its subspace topology, the compact Hausdorff group B_p (pointwise convergence of χ^{c_k} at the finite-order elements of F̄_p^× is exactly convergence c_k → c in Ẑ_{(p)}). **All of the pathology is created by the suspension quotient**, i.e. by the ℚ^{>0}-action, precisely as Deninger's non-proper-discontinuity remark predicts.
* The contrast with Deninger's own T₁ statement is instructive. His Prop. 10.3 Remark (p. 64) says that on the idelic model the ℚ^{>0}-orbits on ℚ^{>0}Ẑ^× × ℝ^{>0} are **closed**, so that Y = ℚ^{>0}_0Ẑ^× ×_{ℚ^{>0}_0} ℝ^{>0} is T₁ (though irreducible, hence still non-Hausdorff). On the packet the orbits are **not** closed, and the single structural reason is the isotropy p^ℤ of Thm. 5.2: it makes the character coordinate blind to the p-part of q ∈ ℚ^{>0} while the ℝ-coordinate still sees it. Theorem 1's Lemma 5.2 is exactly the resulting "strong approximation with the infinite place put back in". Deninger's p. 65 Remark 1 — the adele topology on Ẑ^× × ℝ^{>0} is "reminiscient of the subspace topology … on a dense leaf of a foliation" — is the same intuition; Theorem 1 shows that on the packets the leaf is not merely dense but topologically invisible.

---

## 7. The four charter questions, answered for X₀^{E(a)}

Throughout, a = (a₀(p))_p is an arbitrary choice of base classes, E(a) the minimal cut (empty in characteristic 0) and E(a)′ the enlarged cut of §4.1, and γ_p := Γ^{E(a)}_{(p)} the unique periodic orbit over p (Prop. 4.1).

### 7.1 Structure of the minimal cut suspension

**Proposition 7.1.** X₀^{E(a)} = ⨆_p γ_p, and each γ_p is **open and closed** in X₀^{E(a)}. Hence X₀^{E(a)} is the topological coproduct of countably infinitely many indiscrete circles: its open sets are exactly the unions of the γ_p, so as a topological space it is (a countable discrete set) with an indiscrete continuum sitting over each point.

*Proof.* Since E(a) has empty characteristic-0 part, every point of X̌₀(ℂ)_{E(a)} lies over a closed point of X = spec ℤ̄, so X₀^{E(a)} = ⋃_p Γ^{E(a)}_{(p)} = ⋃_p γ_p (Prop. 4.1), and the union is disjoint ([x-03] Thm. 6.1, p. 39: distinct closed points give disjoint packets). By Lemma 3.3 there is an open V_p ⊆ X₀^{E_max} with V_p ⊇ Γ_{(p)} and V_p ∩ Γ_{(q)} = ∅ for q ≠ p; by Lemma 3.2, X₀^{E(a)} carries the subspace topology of X₀^{E_max}, so V_p ∩ X₀^{E(a)} = γ_p is open in X₀^{E(a)}. Its complement ⋃_{q≠p} γ_q = (⋃_{q≠p}V_q) ∩ X₀^{E(a)} is open by the same argument, so γ_p is also closed. Finally, each γ_p is indiscrete (Cor. 1.1), so a set is open in X₀^{E(a)} iff it meets each γ_p in ∅ or γ_p. ∎

### 7.2 (2) Hausdorffness — **NO**, and this is the decisive failure

By Corollary 1.1, each γ_p ⊂ X₀^{E(a)} is indiscrete with continuum many points. So X₀^{E(a)} is not T₀, not T₁, not Hausdorff, not metrizable, not a foliated space, not a lamination, and does not embed in any Hausdorff space. The same holds for X₀^{E(a)′}, for X₀ itself, and for the unitary system. **This closes the adjudication §7 item "Hausdorffness of the CUT suspensions X₀^{E(a)} (the only Hausdorff question left with any S4 relevance)" with the answer NO**, and it removes the scope exception under which row W12 was recorded (adjudication §3, scope note).

### 7.3 (1) Compactness — **NO**, for every system named

**Corollary 7.2 (minimal cut).** X₀^{E(a)} is **not compact** (and not connected, and not quasi-compact in any weaker sense): {γ_p}_p is an open cover with no finite subcover, by Prop. 7.1.

The other three systems need an argument, because a quotient of a non-compact space can be compact and because the ℚ^{>0}-saturation of any chart-bounded open set is everything (so the chart exhaustion of Prop. 7.3(c) below does *not* descend to the suspension). The following settles them.

**Lemma 7.2.1 (rigidity of ℚ^{>0}-translates at a μ-injective point).** Let P ∈ X̊(ℂ) with P|_{μ(K)} injective (K = ℚ̄), and let q = ν/ν′ ∈ ℚ^{>0} in lowest terms. Then F_q(P) ∈ X̊(ℂ) if and only if ν′ = 1.

*Proof.* F_{ν′} is a homeomorphism of X̌(ℂ) (Prop. 7.4b, p. 43), so F_q(P) ∈ X̊(ℂ) ⟺ F_{ν′}F_q(P) = F_ν(P) ∈ F_{ν′}(X̊(ℂ)). By (51) (p. 42), F_{ν′}(X̊(ℂ)) = {Q ∈ X̊(ℂ) : Q(μ_{ν′}(K)) = 1}. Since F_ν(P) ∈ X̊(ℂ) automatically, the condition reads P(ζ)^ν = 1 for all ζ ∈ μ_{ν′}(K). Pick ζ of exact order ν′ (K = ℚ̄ contains it). As P is injective on μ(K), P(ζ) has exact order ν′, so ν′ | ν; with gcd(ν,ν′) = 1 this forces ν′ = 1. The converse is trivial. ∎

**THEOREM 2 (non-compactness of the suspension).** Let X₀ = spec ℤ and let E ⊆ E_max be admissible. Suppose the E-locus contains a point (x_η, Ψ) with x_η the generic point of X = spec ℤ̄ (so κ(x_η) = ℚ̄) and Ψ|_{μ(ℚ̄)} injective. Then X₀^E = X̌₀(ℂ)_E ×_{ℚ^{>0}} ℝ^{>0} is **not quasi-compact**. The same conclusion, by the same proof, holds for the unitary system Y₀^Den = X̌₀(S¹) ×_{ℚ^{>0}} ℝ^{>0}.

*Proof.* For n ≥ 1 put U_n := q( X̊₀(ℂ)_E × (1/n, ∞) ). Each U_n is open: X̊₀(ℂ)_E is open in X̌₀(ℂ)_E ([x-03] p. 47, the case ν = 1 of "the subspaces F_ν^{-1}X̊₀(ℂ) are open in X̌₀(ℂ)"), and q is open (Lemma 3.1). The U_n increase with n, and they cover: any point of X₀^E is [P̌, u] with P̌ ∈ X̌₀(ℂ)_E, so P̌ = F_μ^{-1}(P) for some μ ∈ N and P ∈ X̊₀(ℂ)_E, whence [P̌,u] = [F_μ P̌, μ^{-1}u] = [P, μ^{-1}u] ∈ U_n for n large. If X₀^E were quasi-compact, this increasing open cover would have a finite subcover, i.e. X₀^E = U_n for some n.

It does not. Let P := (x_η, Ψ) and consider the point [P, 1/n] (here we identify P with its class in X̊₀(ℂ)_E). Its representatives in X̌₀(ℂ)_E × ℝ^{>0} are exactly the (F_q P, q^{-1}/n) for q ∈ ℚ^{>0}. Since X̊(ℂ) is G-invariant, F_q P lies in X̊₀(ℂ) iff F_q(x_η,Ψ) lies in X̊(ℂ), which by Lemma 7.2.1 happens iff q ∈ N. For such q the second coordinate is 1/(qn) ≤ 1/n, so no representative has first coordinate in X̊₀(ℂ)_E and second coordinate > 1/n. Hence [P,1/n] ∉ U_n. ∎

**Corollary 7.2.2 (which systems this covers).** Such a Ψ exists in every class named in the S4 discussion, so **none of X₀^{E_f}, X₀^{E_fg}, X₀^{E_fd}, X₀^{E_fd0}, X₀^{E_max} = X₀^{E_tors}, X₀^{E(a)′}, Y₀^Den is quasi-compact**; and X₀^{E(a)} is not compact by Cor. 7.2. Existence:
(i) *For E ⊇ E_f (hence for E_max, E_tors and E(a)′, whose characteristic-0 parts contain all (Tors) characters of ℚ̄^×).* By [x-03] Lemma 4.3 (p. 28) with k = ℚ̄, C = ℂ (its hypotheses hold: card ℚ̄ = ℵ₀ ≤ card ℂ, ℂ^× ≠ μ(ℂ)) applied to the injective χ_μ = ι : μ(ℚ̄) ↪ μ(ℂ), there is Ψ : ℚ̄^× → ℂ^× with Ψ|_{μ(ℚ̄)} = ι and ker Ψ = ker ι = 1. Then |ker Ψ| = 1 ∈ N, so Ψ ∈ E_f; (Image) is vacuous in characteristic 0 (p. 27, "Only if char κ > 0").
(ii) *For the unitary system.* ℚ̄^× ≅ μ(ℚ̄) × V with V a ℚ-vector space of countable dimension (μ(ℚ̄) is divisible, hence a direct summand), and S¹ ≅ (ℚ/ℤ) ⊕ (ℝ/ℚ) with ℝ/ℚ a ℚ-vector space of dimension 2^{ℵ₀} (the torsion subgroup ℚ/ℤ of ℝ/ℤ is divisible, hence injective, so the extension splits). Choose a ℚ-linear injection V ↪ ℝ/ℚ and let Ψ be ι on μ(ℚ̄) and that injection on V. Then Ψ : ℚ̄^× ↪ S¹ is injective, unitary, satisfies (Tors) with trivial kernel, and (x_η,Ψ) ∈ X̊(S¹). Lemma 3.2 identifies Y₀^Den with the corresponding sub-suspension, and X̊₀(S¹) is open in X̌₀(S¹) (it is X̊₀(ℂ) ∩ X̌₀(S¹), and X̌₀(S¹) is treated as a subspace of X̌₀(ℂ), p. 50), so the proof of Theorem 2 applies verbatim. ∎

**Proposition 7.3 (three further compactness facts, for the record).**
(a) *Every packet is compact.* Γ^E_{(p)} ⊂ X₀ is indiscrete (Cor. 1.1), hence compact. So Deninger's description of the packets as "compact" ([x-03] intro p. 2; [x-06] p. 12) is, in the subspace topology, **topologically vacuous** — it conveys no information whatever, and in particular it must not be read as evidence that packets are compact *Hausdorff* (§6).
(b) *X̊(S¹) is compact Hausdorff, and so is X̊₀(S¹).* By Remark 3.4 (p. 23), X̊(S¹) is the set of P ∈ T := ∏_{r∈ℤ̄}(S¹∪{0}) satisfying: P(0)=0, P(1)=1; P(rs)=P(r)P(s) for all r,s; P^{-1}(0) additively closed; and P(r)=P(r′) whenever P(r−r′)=0. In T (compact Hausdorff by Tychonov) each set {P : P(r)=0} is **clopen**, because {0} is open and closed in S¹∪{0}. Hence: the multiplicativity and normalization conditions are closed (equalities of continuous functions); the complement of the third condition is ⋃_{r,s}({P(r)=0}∩{P(s)=0}∩{P(r+s)≠0}), a union of open sets, so that condition is closed; the complement of the fourth is ⋃_{r,r′}({P(r−r′)=0}∩{P(r)≠P(r′)}), clopen ∩ open, so that condition is closed too. Thus X̊(S¹) is closed in T, hence compact; it is Hausdorff by Cor. 7.9 (p. 45). X̊₀(S¹) = X̊(S¹)/G is then compact, and Hausdorff by Cor. 7.8 (p. 45). *(A monoid homomorphism from (ℤ̄/p ∖ 0, ×) into the group S¹ extends uniquely to the group completion κ(x)^×, so these P are exactly the points of X̊(S¹).)*
(c) *X̌(S¹) and X̌₀(S¹) are **not** compact.* They are the increasing unions ⋃_ν F_ν^{-1}X̊(S¹) resp. ⋃_ν F_ν^{-1}X̊₀(S¹) of subsets which are open (Prop. 7.4a, p. 43, together with F_ν a homeomorphism; downstairs because π̌ is open). The union is strictly increasing: for ν > 1 choose a prime p ∤ ν and a unitary character ψ of F̄_p^× injective on μ_ν(F̄_p); then ψ(μ_ν(K)) ≠ 1, so by (51) (p. 42) (x,ψ) ∉ F_ν(X̊(ℂ)), i.e. F_ν^{-1}(x,ψ) ∈ F_ν^{-1}X̊(S¹) ∖ X̊(S¹); applying F_ν gives F_{νμ}^{-1}X̊(S¹) ⊋ F_ν^{-1}X̊(S¹) for suitable μ. A compact space covered by a directed family of open sets equals one of them; contradiction.

**Honesty on what (1) now means.** Since X₀^E is not T₀ (Theorem 1), "compact" cannot in any of these systems be upgraded to "compact Hausdorff", so the charter's compactness question was in any case void for S4 purposes; Theorem 2 settles it in the stated sense (quasi-compactness) anyway, and does so for every ambient the program has named. *What remains genuinely open and is not claimed here:* whether X₀^E is locally compact anywhere, and whether any *proper* flow-invariant subspace of X₀ is quasi-compact (it need not be: quasi-compactness is not inherited by subspaces). Neither is needed: Cor. 1.2 kills face (a) with no compactness input whatever.

### 7.4 (3) Topological dimension

**Corollary 7.4.** (a) For every admissible E and every prime p, the packet Γ^E_{(p)} ⊂ X₀ has covering dimension 0, and small and large inductive dimension 0. (b) dim X₀^{E(a)} = 0 (in all three senses), **not** 3.

*Proof.* (a) A nonempty indiscrete space Z has {Z} as its only open cover, which refines itself with order 1, so dim Z ≤ 0; and dim Z ≥ 0 as Z ≠ ∅. The base {Z} consists of sets with empty boundary (∂Z = cl Z ∖ int Z = ∅), so ind Z = Ind Z = 0. (b) Let {U_1,…,U_n} be a finite open cover of X₀^{E(a)}. By Prop. 7.1 each γ_p is contained in some U_{i(p)}; put V_i := ⋃_{p : i(p)=i} γ_p. The V_i are open, pairwise disjoint, refine the cover, and have order 1. Hence dim = 0; the inductive dimensions are 0 because {γ_p} is a base of clopen sets. ∎

**Comment.** The number 3 that S4 asks for is a property of the *model* (Cantor set) × (circle) × (leaf direction), and Theorem 1 shows the subspace topology retains none of it: the covering dimension of the actual subspace is 0, and the "1-dimensional Cantor-bundle-of-circles" picture of Γ_p is a picture of the bijection (39), not of the topology. Note that this also empties the *only* rigorous route the program had to "infinite-dimensionality of a subsystem": probe A's Theorem B(b) derived dim ≥ n for closed invariant S **assuming S Hausdorff in its subspace topology** — a hypothesis now provably unsatisfiable whenever S contains a periodic orbit (§8).

### 7.5 (4) One orbit per packet — **YES**, for every a

Proposition 4.1: for every choice a and both cut classes, Γ^{E}_{(p)} is a single circle of length log p for every prime p, and [x-03] Thm. 6.1 (p. 39) says these are all the periodic orbits. The choice-content and the theory-forfeiture are as the adjudication already priced them (Remark 4.2).

### 7.6 The periodic locus is a coproduct of indiscrete packets — and the other candidate constructions die with it

The charter asked, should the cut suspension fail, that other constructions be examined: "the closure of the periodic set Y₀ = X̌₀(S¹) ×_{ℚ^{>0}} ℝ^{>0} restricted to characters with prescribed structure; Frobenius-closed sub-loci; the images of Kucharczyk–Scholze-type or [D25]-type constructions if on disk." **All of these die at once**, and it is worth saying exactly why, because the reason is structural rather than case-by-case.

**Proposition 7.5 (universality of the kill).** Let Y be *any* flow-invariant subset of X₀ (any admissible E, or of Y₀^Den) that contains at least one periodic orbit, equipped with the subspace topology. Then Y is not T₀. In particular this holds for: every "Frobenius-closed sub-locus" (a ℚ^{>0}-invariant subset of X̌₀(ℂ)_E, suspended — these are exactly the objects Lemma 3.2 covers); every sub-suspension cut out by prescribing structure on the characters (any such prescription defines a subset of X̌₀(ℂ), and if it is to be flow-invariant it is ℚ^{>0}-invariant); the closure of the periodic set Y₀^Den itself; and the image in X₀ of any construction whatsoever, whenever that image is being read as a *subspace*.

*Proof.* Corollary 1.2. ∎

**Proposition 7.6 (the periodic locus, exactly).** Let Per := ⨿_p Γ^E_{(p)} ⊆ X₀ be the set of periodic points ([x-03] Thm. 6.1, p. 39). In its subspace topology, Per is the **topological coproduct** of the packets, each of which is indiscrete: the relatively open subsets of Per are exactly the unions ⋃_{p ∈ S} Γ^E_{(p)}, S any set of primes.

*Proof.* Each such union is relatively open: take U := ⋃_{p∈S}V_p with V_p from Lemma 3.3; then U is open in X₀ and U ∩ Per = ⋃_{p∈S}Γ_{(p)}, because V_p ∩ Γ_{(q)} = ∅ for q ≠ p. Conversely, if U is open in X₀ and U ∩ Γ_{(p)} ≠ ∅ then U ⊇ Γ_{(p)} by Cor. 1.1; so U ∩ Per is a union of whole packets. ∎

**Corollary 7.7 (free continuity into the periodic locus).** A map g : Z → Per from any topological space Z is continuous if and only if the partition {g^{-1}(Γ^E_{(p)})}_p of Z is a partition into open sets. In particular, if Z is connected, a continuous g is a map into a **single** packet — and then *every* set-map into that packet is continuous.

This is the precise sense in which Theorem 1 destroys face (a) while *helping* face (b): as a target, the periodic locus imposes almost no continuity at all. Two immediate consequences, recorded for §9:

* **(An infinite one-orbit-per-packet witness.)** Let Y_∞ := ⨆_p ℝ/(log p)ℤ with the coproduct topology and the translation flow, and for a choice a = (a₀(p))_p let f : Y_∞ → X₀ send the p-th circle onto γ_{p,a₀(p)} by t ↦ [P^{a₀(p)}, e^t]. Then f is **continuous and flow-equivariant**, and meets each packet in exactly one orbit. (Continuity: by Cor. 7.7, since Y_∞ is the coproduct of the f^{-1}(Γ_{(p)}). Equivariance: φ^s f(t) = [P^{a₀(p)}, e^{t+s}] = f(t+s). Well-definedness on ℝ/(log p)ℤ: [P^{a₀(p)}, p u] = [F_p(P^{a₀(p)}), u] = [P^{a₀(p)}, u] by §2.4.) It is a continuous bijection onto its image and not a homeomorphism — which is exactly what Theorem 1 predicts. This extends probe B §6.3's finite-stage escapes from finite sets of primes to *all* primes.
* **(Where S4 actually lives.)** Y_∞ is not compact and not 3-dimensional. Since the map exists for free on the periodic part, **the entire content of S4's mapping face is the compactification**: whether the domain ⨆_p ℝ/(log p)ℤ can be enlarged to a compact 3-dimensional lamination Y in such a way that f extends continuously and equivariantly over the limit set A = Y ∖ ⋃_p γ_p. That is exactly probe B §6.4's formulation, now reached by a second and much shorter road.

---

## 8. Effect on the banked record (what is subsumed, what is sharpened, what is emptied, what is untouched)

Nothing that the Session-8 adjudication banked as a **verdict** changes. The following is a precise accounting, item by item.

**Subsumed and re-proved by a shorter route (no verdict changes).**
1. **Theorem A (packet-closure law).** cl(γ) ⊇ Γ^E_{(p)} is Cor. 1.3, now as a consequence of the point-level statement cl({z}) ⊇ Γ^E_{(p)}. This is a **fourth** independent derivation of Theorem A, by a mechanism that is a strict refinement of the three existing ones (they move only along the orbit's ℚ^{>0}-parameter with a *fixed* real target; Theorem 1 moves the profinite and the archimedean coordinate simultaneously).
2. **Corollary A.2 / ledger row W12** (X₀ non-Hausdorff along packets). Cor. 1.1 gives "not even T₀", and Cor. 1.3 removes W12's recorded scope exception: the adjudication §3 scope note said the two-limit argument "produces no second limit and decides nothing" for the minimal cut classes E(a₀). Theorem 1 with b = a decides them.
3. **The closed half of S4 (adjudication §4 item 2).** Cor. 1.4 re-derives it without Thm. 8.2, without Claim 8.1/[Per11], without the uncountability of B_p and without dimension theory. The original routes remain the correct citation for the *orbit-count* half (uncountably many closed orbits per prime), which Theorem 1 does not produce.

**Sharpened.**
4. **The Session-14 referee-banked closure equality** (adjudication §4 item 1, block dated 2026-09-02: packets are closed flow-invariant subsets of X₀; cl_{X₀}(γ) = Γ^E_{(p)} exactly). Combining that closedness with Theorem 1 upgrades it to **cl_{X₀}({z}) = Γ^E_{(p)} for every single point z of the packet**, and re-proves packet minimality in the strongest possible form: *every nonempty subset of a packet is dense in it*.
5. **Probe A's Theorem C(b) / adjudication §4 item 5b.** Prop. 4.1 re-derives the reachability computation independently (a fifth derivation of (★)) and extends the conclusion to the enlarged cut E(a)′ and to *every* choice of a, with the (Image)-vacuity step spelled out.
6. **Ledger row R1** ("Hausdorff known only for affine/ample; **compactness not established**"). Theorem 2 changes "not established" to **fails**, for X₀^{E_f}, …, X₀^{E_max}, X₀^{E(a)′} and Y₀^Den; Cor. 7.2 does the same for X₀^{E(a)}.
7. **Ledger row W11 / adjudication §4 item 4 (the Morishita flag).** A fourth and now conclusive reason not to read [r3s-08]'s packet "homeomorphism" wording as the subspace topology: an indiscrete space with more than one point is homeomorphic to no product of a profinite group with a circle. (Not cited for anything above; recorded only as flag reinforcement.) §6 adds the parallel observation about [x-06] p. 12's "fibre space … compact orbits" wording, which must likewise be read at the level of the model bijection (39).

**Emptied (a hypothesis is now provably unsatisfiable — the statement survives as vacuously true and can no longer be cited as evidence).**
8. **Probe A's Theorem B(b)** — "every closed invariant S as above *whose subspace topology is Hausdorff* has covering dimension ≥ n for all n". By Cor. 1.2 no such S exists (any closed invariant S meeting a packet contains a periodic orbit, hence is not T₀), so B(b) is vacuous. Its conclusion was never load-bearing: the closed-half kill is carried by B(a) and probe B's Corollary B (adjudication §4 item 6), and now independently by Cor. 1.4. **Two further observations for whoever runs B(b)'s outstanding referee pass** (this note did *not* re-derive the cell construction, so these are flags, not findings): (i) the step "S contains a homeomorphic copy of the n-cube" is inferred from a continuous injection Θ : [0,½]^n → X₀ out of a compact space — that inference needs the image to be Hausdorff, and X₀ is not, so it must be re-examined even before the Hausdorff hypothesis on S is applied; (ii) if the cell construction is to be salvaged, the natural repair is to state it about the *model* space of Thm. 7.10 rather than about a subspace of X₀.
9. **Probe A's §4.3** ("the cut system still dies as an embedded substrate, modulo G1") was already **void** by adjudication §3 consequence 1, because its mechanism was "compact ⟹ closed in a Hausdorff ambient" and G1 = NO. That remains void: the *argument* does not come back. But the *conclusion* is now true for an unrelated and unconditional reason — the cut suspensions are intrinsically non-T₀ (§7.2), so they are dead as embedded substrates without any ambient argument at all. The bookkeeping should record the conclusion as re-established with a new proof, and the old proof as still void.

**Untouched.**
10. **Q-b / face (b) of Q\*, probe A's G2, probe B §6.1–§6.4, and the S2 leg (W3).** Nothing in this note bears on them except favorably (§9).
11. **Probe 9.4's trichotomy, Prop. 1 (no Aut(ℂ)-stable selection), Lemma D (referee-pending), Road 2 / DQ-M.** Untouched; but see §9's remark on how Theorem 1 interacts with the Haar-average road.
12. **The kill-criterion.** Still does **not** fire: Route 2 is not exhausted, because face (b) is open. A NO on face (a) alone was never sufficient — the adjudication's Q\* is explicit that "**a NO on both** kills S4".

---

## 9. Where S4 now stands, and why face (b) is helped rather than hurt

**9.1 Face (a) collapses into face (b), formally.** The residual question Q\* was posed as two faces of one problem: (a) a Hausdorff-in-itself compact 3-dimensional flow-invariant **subspace** Y ⊆ X₀ with one orbit per packet; (b) a compact 3-dimensional lamination **mapping** equivariantly to X₀. Theorem 1 says the subspace topology on any candidate for (a) retains nothing at all — not dimension, not separation, not the circle structure. Hence there is no meaningful intermediate: either the lamination structure lives on a set with a **finer** topology of its own, and then the inclusion is a continuous equivariant map and one is exactly in case (b); or it lives in the subspace topology, and then it is indiscrete on every packet and dead. **Q\* has therefore been reduced from two faces to one**, and the surviving face is the one the program already identified as its hard core.

**9.2 The reduction is not vacuous — it deletes an entire class of would-be constructions.** Proposition 7.5 covers, in one line, every construction that produces its object as a subset of X₀: cut classes, Frobenius-closed sub-loci, character-structure prescriptions, the closure of the periodic set with any restriction imposed on it, and the *image* of any external construction (Kucharczyk–Scholze-type or [D25]-type) whenever that image is read as a subspace. None of these can ever be a lamination. This closes off the direction the charter opened as "if the cut suspension fails, examine other constructions", uniformly and permanently, and it is the main positive-direction content of this note.

**9.3 For face (b) the news is strictly good.** Continuity into an indiscrete space is free. Concretely:
* Corollary 7.7: a map into the periodic locus is continuous as soon as the packet-preimages are open. So no continuity obstruction to an S4 map exists **on the periodic part** at all, for any choice a.
* The Y_∞ witness of §7.6 realizes this: a continuous, flow-equivariant, one-orbit-per-packet map ⨆_p ℝ/(log p)ℤ → X₀ exists, over **all** primes simultaneously. Probe B §6.3 had this for finite sets of primes; the infinite version is now available and costs nothing, precisely because of Theorem 1.
* Both probes' delineations survive with more room. Probe A §6.1's forcing was conditional on G1-yes and was already void; probe B §6.1's observation that "compact images need not be closed in the non-Hausdorff X₀, so Theorem A does not apply to f(Y)" is strengthened — X₀ is not merely non-Hausdorff, it is non-T₀ along exactly the locus where the forcing was supposed to bite, and cl(f(Y)) contains whole packets automatically, so no information is transmitted back to Y.

**9.4 What the open question is now, stated exactly.** Fix a = (a₀(p))_p. Let Y_∞ = ⨆_p ℝ/(log p)ℤ with its translation flow and f_a : Y_∞ → X₀ the map of §7.6. **Q-b is equivalent to: does there exist a compact metrizable 3-dimensional lamination (Y, F, φ) containing Y_∞ as an invariant subspace whose closed orbits are exactly the circles of Y_∞, together with a continuous flow-equivariant extension f : Y → X₀ of f_a?** The whole content is the behavior on A := Y ∖ Y_∞, a nonempty closed invariant aperiodic set on which the lengths log p → ∞ accumulate, with f(A) inside the unitary locus ([x-03] Thm. 8.2's regime). That is probe B §6.4 verbatim, now derived without any packet input.

**9.5 One caution for the Haar-average road (9.4 note, Road 2 / DQ-M).** Road 2 proposes to renounce selection and weight each packet by its Haar measure on B_p. Theorem 1 does not refute it — a measure is not a topology, and the packet's Haar measure lives on the *model* B_p, transported through the bijection (39). But it does add a precise constraint that should be recorded before DQ-M is attempted: **the fibration Γ_p → B_p is not continuous for the subspace topology** (§6), so a transverse measure on the packet cannot be obtained by pulling back Haar along a continuous map, and every Borel structure used on Γ_p must be declared as coming from the model (39) and not from X₀. In the model world of DQ-M (a [Den05] §7-type suspension M̄ ×_Λ ℝ, where the periodic continuum genuinely *is* B × S¹ as a topological space) this distinction does not arise; it arises only when the model-world result is transported back to X₀. Flagged, not adjudicated; this note does not touch DQ-M's verdict.

---

## 10. Scope and honesty

**10.1 What is proved here, and at what grade.** Theorem 1, Theorem 2 and all corollaries in §§3–7 are proved in full from [x-03]'s definitions and from the anchors listed in §1, each read verbatim this session in a fresh `pdftotext -layout` extraction, with printed-page identity checked against the page footers. No step uses a program note as an input. No step uses a recalled result.

**10.2 The one judgment-grade reading, flagged.** That X₀ carries the **quotient** topology (§2.3). [x-03] never writes the phrase. The reading is supported by three passages (§2.3 items 1–3), the strongest being Prop. 10.3's Remark on p. 64, where Deninger himself infers "points of Y are closed" from "the ℚ^{>0}-orbits are closed" — an inference valid only for the quotient topology. It is the same reading used by probe A, probe B and the Session-8 adjudication (§2(ii)); if it were wrong, every result in this note *and* the banked Theorem A would have to be re-examined together. Note the asymmetry: a strictly **coarser** admissible topology would only strengthen Theorem 1; a strictly **finer** one would falsify Deninger's own p. 64 inference.

**10.3 What was NOT re-derived.**
* Probe A's Theorem B(b) cell construction (I record two observations about it in §8 item 8; I did not check the construction).
* The uncountability of B_p (banked, adjudication §2; used only in §7.2's remark that γ_p has continuum many points, which I derive instead from ℝ^{>0}/p^ℤ, and in §8's description of the orbit count — not in any proof).
* 9.4 Lemma D (Aut(ℂ) transitive on B_p) — cited nowhere below; it is referee-pending per the charter.
* The Session-14 referee-banked closedness of packets. I use it **only** in Cor. 1.3's sharp equality cl({z}) = Γ^E_{(p)}; the inclusion ⊇, which is all that Theorem 1 itself gives and all that Cor. 1.2 needs, is proved here from scratch.
* [x-03] §§11–16 (the p-adic and Witt-vector material), §9's Theorems 9.2/9.8, and the whole of [D25], [ALKL], [ÁLKL23], [ALKM], [Lei07/Lei13] — not read this session and not used.
* The general-arithmetic-scheme extension of Theorem 1 (Remark 5 in §5) is a **sketch**; only the spec ℤ case is proved. Nothing below uses the extension.

**10.4 [RU] items.** None. Every source statement used is quoted from the on-disk extraction with a printed page number. Classical facts used without citation are: Tychonov; a compact space covered by a directed family of open sets equals one of them; a continuous map from an indiscrete space to a Hausdorff space is constant; the group-completion universal property; divisibility ⟹ injectivity for abelian groups; dimension of an indiscrete space. These are textbook and are used as such.

**10.5 Prior art — an honest gap.** No new online prior-art sweep was run this session (this probe worked from the on-disk corpus only). Probe B §7's Session-8 sweep found nothing in the literature stating even the weaker non-Hausdorffness; Theorem 1 is strictly stronger, so that negative scan covers it a fortiori for the specific claim searched, but a fresh sweep on "non-T₀ suspension", "indiscrete orbit", "topologically indistinguishable" phrasings, and on the foliated-spaces cluster (x-17…x-24), [KS18] commentary and arXiv:2510.19456, is **owed before any external circulation**. Theorem 2 has had no prior-art check at all.

**10.6 What is deliberately not claimed.**
* This note does **not** claim S4 is dead. Face (b) is open; the kill-criterion does not fire.
* It does **not** claim Deninger's paper contains an error. Every technical statement in [x-03] that this note touches is stated there as a bijection or a set-level identification, exactly as it should be; only the informal adjectives in the introduction and in the survey [x-06] would be wrong if read topologically, and §6 records that as a reading caution, not as a correction to a theorem.
* It does **not** claim X₀ is locally compact, or that proper invariant subspaces of X₀ fail quasi-compactness (Theorem 2 is about the whole suspension; quasi-compactness is not subspace-hereditary).
* It does **not** re-open or re-decide anything on the S2 leg, on DQ-M, or on the 9.4 trichotomy.

---

## 11. Novelty ledger

Everything in this section is believed new relative to the on-disk corpus and to the program's own record, and each item is tagged for the dual-model sweep. Items are listed with the exact statement and the location of the proof.

1. **[novelty: single-check] Theorem 1 (§5): packet indiscreteness.** For X₀ = spec ℤ and every admissible E ⊆ E_max, any two points of a packet Γ^E_{(p)} ⊂ X₀ are topologically indistinguishable; the packet is an indiscrete subspace; X₀ is not T₀. *Strictly stronger than banked row W12 (non-Hausdorff along packets) and than banked Theorem A, both of which it implies.*
2. **[novelty: single-check] Lemma 5.2 (§5): simultaneous profinite/archimedean approximation.** For any p, c ∈ Ẑ_{(p)}, t ∈ ℝ^{>0} there are m_k ∈ N, j_k ∈ ℤ with m_k → c in Ẑ_{(p)} and m_k p^{-j_k} → t in ℝ^{>0}. *This is the mechanism; it is "strong approximation with the infinite place restored", made possible by the p^ℤ-isotropy.*
3. **[novelty: single-check] Corollary 1.1 (§5.1): a single periodic orbit of X₀ is an indiscrete subspace** with continuum many points.
4. **[novelty: single-check] Corollary 1.2 (§5.1): Q\* face (a) = NO**, unconditionally, for every admissible E and for the unitary system; and Corollary 1.5: the subspace reading of Deninger's own question ([x-03] p. 40) is answered NO with no closedness hypothesis.
5. **[novelty: single-check] Corollary 1.3 sharp form (§5.1): cl_{X₀}({z}) = Γ^E_{(p)} for every single point z of a packet** (uses the Session-14 referee-banked closedness for the ⊆ direction).
6. **[novelty: single-check] Theorem 2 with Lemma 7.2.1 (§7.3): the suspension is not quasi-compact** for every admissible E whose locus contains a characteristic-zero point injective on μ(ℚ̄), and for the unitary system Y₀^Den. With Cor. 7.2 (minimal cut) this settles compactness in the negative for every system the program names.
7. **[novelty: single-check] Proposition 7.1 with Corollaries 7.2 and 7.4 (§§7.1, 7.3, 7.4): the structure of the minimal cut suspension** — X₀^{E(a)} is the topological coproduct of countably many indiscrete circles; it is not compact, not connected, and has covering, small- and large-inductive dimension **0**, not 3.
8. **[novelty: single-check] Lemma 3.3 (§3): packets are pairwise separated by open sets of X₀** (the evaluation-at-q₀ chart, saturated and pushed down). Auxiliary but used four times.
9. **[novelty: single-check] Propositions 7.5–7.6 and Corollary 7.7 (§7.6): the periodic locus of X₀ is the topological coproduct of its indiscrete packets**, so a map into it is continuous exactly when the packet-preimages are open; hence continuity into the periodic locus is free, and every subspace-based candidate construction dies at once.
10. **[novelty: single-check] The Y_∞ witness (§7.6): a continuous flow-equivariant one-orbit-per-packet map ⨆_p ℝ/(log p)ℤ → X₀ over all primes simultaneously**, for every choice a. Extends probe B §6.3 from finite prime sets to all primes; reduces Q-b to a compactification/extension problem (§9.4).
11. **[novelty: single-check] Proposition 7.3(b),(c) (§7.3): X̊(S¹) and X̊₀(S¹) are compact Hausdorff; X̌(S¹) and X̌₀(S¹) are not compact.** (b) is elementary and may well be folklore — flagged as *likely known, not located in the on-disk sources*.
12. **[novelty: single-check] The reading correction of §6:** [x-06] p. 12's "Γ_{x₀} is a fibre space over the compact group … with fibres the compact orbits" and [x-03] pp. 2–3's "compact packets … fibred over the compact group" cannot be read in the subspace topology of X₀ — the fibration map Γ_p → B_p is not continuous there, since a continuous map from an indiscrete space to a Hausdorff group is constant. They are correct as statements about the model bijection (39), which is how [x-03] states them.
13. **[novelty: single-check] Proposition 4.1 (§4.3):** the one-orbit-per-packet property of the cut classes holds for **every** choice a and for the **enlarged** cut E(a)′ as well as the minimal one, with the (Image)-vacuity step over spec ℤ made explicit. Extends probe A's Theorem C(b) / adjudication §4 item 5b.

**Sweep guidance for the dual-model check, in order of consequence:** item 1's proof (the three ingredients are: the isotropy F_{p^{-j}}(P^a) = P^a from Thm. 5.2 + (23); Lemma 5.1's *exact eventual* pointwise agreement; and Lemma 5.2's interval-plus-CRT construction), then item 6's Lemma 7.2.1 (the use of (51) with gcd(ν,ν′) = 1), then item 8's saturation argument, then item 9's Prop. 7.6.

---

## 12. Bookkeeping (files and rows this result touches — none of them edited by this note)

**Q\* clauses** (`results/c3-r/probe-9.3-adjudication.md` §5).
* **Q-a — CLOSED, NO.** "Does X₀ (E ⊇ E_f) contain a compact, Hausdorff-in-its-subspace-topology, flow-invariant subspace Y … of topological dimension 3, meeting each packet in exactly one orbit?" Answer NO by Cor. 1.2, for every admissible E, with no compactness or dimension hypothesis used. Q\* becomes single-faced.
* **Q-b — unchanged and now the whole of Q\***; helped, not hindered (§9). Suggested restatement for the record: §9.4's extension form.
* **Q-c — unchanged** (already settled YES in the Session-14 referee block).

**Adjudication §7 open items** (same file).
* "Hausdorffness of the CUT suspensions X₀^{E(a)} (the only Hausdorff question left with any S4 relevance)" — **CLOSED, NO** (§7.2).
* Adjudication §3's scope note on W12 ("for probe A's minimal cut classes … this argument produces no second limit and decides nothing") — **superseded**; the cut suspensions are non-Hausdorff, indeed non-T₀ (Cor. 1.3).
* Adjudication §4 item 5's correction ("the cut systems are NOT additionally dead as embedded substrates") — the *argument* it voided stays void; the *conclusion* is now re-established unconditionally by §7.2 (see §8 item 9). This wording needs care in any annotation.
* Adjudication §4 item 6's outstanding referee debt on probe A's Theorem B(b) — see §8 item 8: the statement is now vacuous, and two further observations are flagged for whoever runs the pass.

**Ledger rows** (`results/c3-r/m2c-feasibility-ledger.md` §5, §12).
* **R1** ("compactness not established") → compactness **fails**, for every system named (Theorem 2 + Cor. 7.2).
* **R4 / R6 / W4 / W7** (closed-subsystem readings, theorem-backed dead) → a second, cheaper and hypothesis-free proof (Cor. 1.4); R6's "dim 3 subsystem" reading gains the explicit computation dim X₀^{E(a)} = 0 (Cor. 7.4).
* **W6** ("not a foliated space") → strengthened to "not even T₀ along the arithmetic locus", now for *every* admissible class including the cuts.
* **W12** (non-Hausdorff along packets) → subsumed by Theorem 1; its scope restriction is removed.
* **W11** (Morishita "homeomorphism" wording — do not cite for topology) → fourth, conclusive reason (§8 item 7); and a parallel caution for [x-06] p. 12's "fibre space" wording (§6, novelty item 12).
* **W9 / R15** (selection must be canonical and theory-preserving; no transverse measure) → unchanged in substance; add that the cut selections, which W9/R15 already priced as non-canonical and theory-forfeiting, are now *also* topologically inert, and that the Haar-average road inherits the §9.5 caution about the non-continuity of Γ_p → B_p.
* **§8 Route 2 / S4** → the substrate cannot be found *inside* X₀ in any form; S4's only surviving reading is the mapping one, which is Route 2's blocker as before. **Kill-criterion input: still does NOT fire.**

**Direction file** (`directions/C3-geometric-substrate.md`, "Current frontier"). Next-rung item (2) "Q\* — either face" should read "Q\* — face (b) only; face (a) closed NO (S14 `results/c3-r/s14/qa-build.md`)". Next-rung item (1)'s referee debt on probe A's Theorem B(b) is affected as in §8 item 8. Items (3) DQ-M and (4) S2/W3 are untouched apart from the §9.5 caution.

**Companion S14 files not read by this probe** (independence discipline): `results/c3-r/s14/qb-kill.md`, `w3-F.md`, `w3-O.md` were present on disk and were deliberately **not** opened, so that this note's face-(a) verdict is independent of the face-(b) probe running in parallel. Any cross-check between them is the orchestrator's to make.

— end of s14 Q-a build probe —
