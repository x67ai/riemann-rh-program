# NOVELTY / PRIOR-ART SWEEP F — Session-14 claims C1–C10 (standing order 7; one of two independent sweeps)

**Program:** RH program, direction C3-r. **Session:** 14. **Date of sweep:** 2026-09-03 (all network queries this date unless stamped otherwise). **Author:** sweep F (Claude Fable 5.1). Nothing about the other sweep was assumed or consulted.
**Standing order 5:** every statement about a source below was read this session from the on-disk PDF/text at a stated page or from a document fetched this session at a stated location. Anything recalled is marked [RU] and carries no weight.
**Scope:** the ten claims C1–C10 of the task, each read from the cited file's own novelty ledger (list of program files opened in §4). The previous sweep (`referee-s14/novelty-F.md`, `novelty-O.md`, `novelty-adjudication.md`, all read in full this session) covered N1–N5; its searches are NOT repeated here — this file extends them (its coverage is summarized in §1.1).
**Status:** WRITTEN AS THE WORK PROCEEDS (RULE ONE). A section marked `[in progress]` is incomplete.

---

## 0. VERDICTS (stated first; filled in as each claim closes)

| # | Claim (short) | Verdict | One-line reason |
|---|---|---|---|
| C1 | packet / periodic-orbit indiscrete; X₀ not T₀ | [in progress] | |
| C2 | Theorem T: ℚ>0-suspension of a relatively compact orbit is not T₁; Y₀ not T₁ | [in progress] | |
| C3 | flow-conformal weight W; dissipation; packets clopen in periodic locus; finiteness | [in progress] | |
| C4 | backward escape: generic α-limit sets empty | [in progress] | |
| C5 | DQ-M: mapping-torus trace without non-degeneracy; index form; no ℤ-valued invariant f.a. measure | [in progress] | |
| C6 | W3: [ÁLKL23] coincidence statements false; acyclicity via Landau–Kolmogorov; sup-parametrization invariance | [in progress] | |
| C7 | cl(γ) = Γ^E_p exactly; packet = fiber of descended projection, closed, invariant | [in progress] | |
| C8 | closed embedded n-cube in every closed invariant set meeting every packet | [in progress] | |
| C9 | compact 3-dim source (torus + cabled solid tori); inert map; Theorem C; p^{1/2}·O return derivative | [in progress] | |
| C10 | S4′: inverse length-spectrum problem with spectrum {log p} and an archimedean leaf | [in progress] | |

---

## 1. Method

### 1.1 What the previous sweep already covered (not repeated)
Read this session: `referee-s14/novelty-F.md` §5 (W1–W26, C1–C6, citation graphs, on-disk grep list), `novelty-O.md` §6 (S-01…S-45), `novelty-adjudication.md` §5 (A-01…A-12). Covered vocabularies: orbit closure / minimal set / non-Hausdorff / not properly discontinuous / packets / Haar average / continuum of closed orbits / transverse measure / Fuller index / linking homomorphism / Aut(C) / admissible class / one orbit per prime; citation graphs of 1807.06400, 2301.11643, 2508.15971, 2402.06671, 2410.20758, 2508.05329, 1609.04717, 2401.08401 (Semantic Scholar, OpenAlex, Crossref, zbMATH API, arXiv API); Lutz thesis located and read; Google Scholar and zbMATH citing lists blocked.

### 1.2 Vocabularies used here (deliberately varied, per the Winkelmann lesson)
General topology (T₀ / T₁ / Kolmogorov quotient / indiscrete / specialization / orbit space of a dense-orbit action); ergodic-theoretic (dissipative / wandering / Lyapunov function / cocycle / α-limit / escape to infinity); foliation and index theory (Lefschetz–Hopf for fixed-point continua, Dold index, Fuller index, Fried's Lefschetz formulas for flows, flat bundle over a circle); harmonic analysis on profinite groups (invariant finitely additive measures on clopen algebras, dimension of compact abelian groups = torsion-free rank); functional analysis (LF-spaces, Retakh/Palamodov condition (M), Wengenroth, C(K,E) inductive limits, Bierstedt, symbol-class topologies, Hörmander's bounded-set convergence); low-dimensional dynamics (flows with prescribed periodic orbits, Kuperberg plugs, cabling, solenoids); physics (Berry–Keating, "periodic orbits of length log p").

---

## 2. Per-claim evidence

### C1 — Packet indiscreteness: every packet and every periodic orbit of X₀ = X(Spec Z) (quotient topology, [x-03] p. 59) is an indiscrete subspace; X₀ is not T₀; no T₀ subspace meets a packet in two points (qstar-adjudication §3, adversarial/adjudication.md)

**Verdict: NOVEL as a statement about X₀ and its packets; the general-topology principle behind it is printed and must be cited (below).**

*Printed general principle (opened this session).* T. Yokoyama, *Quotient spaces and topological invariants of flows*, arXiv:2012.00849 (PDF downloaded; pdftotext), §2.3.3: "For a flow v on a topological space X, the orbit space X/v of X is a quotient space X/∼_v defined by x ∼_v y if O(x) = O(y). Similarly, the orbit class space X/v̂ of X is a quotient space X/∼_v̂ defined by x ∼_v̂ y if cl O(x) = cl O(y). Note that the orbit class space X/v̂ is the T₀-tification of the orbit space X/v." Example 2 (§12.1): a suspension flow v_{fw} on a solid torus with "each orbit of v_{fw} is periodic or non-closed recurrent, and each minimal set of v_{fw} is a periodic orbit or a torus. Therefore the orbit space M/v_{fw} is not T₀, the orbit class space M/v̂_{fw} is T₁ but not T₂". (Yokoyama's earlier arXiv:1708.06626 characterizes lower separation axioms of such quotients by preorders; abstract read.) In this vocabulary C1 says: **the Q>0-orbit space X₀ of X̌₀(C)_E × R>0 fails T₀ along every packet, and the Kolmogorov quotient collapses each packet to a point** (qa-kill Cor. 4.5 states this last clause explicitly). The criterion "X/G is not T₀ iff two distinct orbits have the same closure" is definition-level and is what Yokoyama's T₀-tification sentence records; the arithmetic content of C1 is the *simultaneous approximation* (qstar §3 Step 1: m_k → c in Ẑ_(p) and m_k p^{−j_k} → t in R>0), which makes every Q>0-orbit in the packet model dense in Ẑ×_(p) × R>0.

*Printed contrast that any circulated statement must confront.* [x-03] p. 64, Remark after Prop. 10.3 (pdftotext line 3780, re-read this session): "By [LR00, Lemma 3.1], the orbits of the Q>0-action on Q>0Ẑ× × R>0 are closed. The same argument works for Q₀>0 instead of Q>0 and it follows that the points of Y are closed, i.e. Y is a T₁-space." ([LR00] = M. Laca, I. Raeburn, *The ideal structure of the Hecke C*-algebra of Bost and Connes*, Math. Ann. 318 (2000) 433–451 = arXiv:math/9911134, located this session.) So Deninger records the **opposite** separation property (T₁) for the adelic model, with the adele topology on the base; C1 is about X₀ with the quotient topology of p. 59 and the compact profinite base Ẑ×_(p). The previous dual-model check already placed [x-03] pp. 47 (Rem. 2), 49, 63, 76 in front of "non-Hausdorff along packets" (N2a PARTIAL); the same anchors apply here, and the p. 64 Remark is the additional one this sweep adds.

*Adjacent, not anticipating.* Connes–Consani arXiv:2401.08401 (PDF downloaded this session; grep results in §3): the density of the generic orbit in each C_p is a non-T₁ statement about the scaling site X_Q, a different space with a different mechanism (adelic density of Q), already recorded as adjacent by the previous sweep.

*Not found anywhere:* a sentence saying that two points of a packet of X₀ (or two points of one periodic orbit) are topologically indistinguishable, that X₀ is not T₀, that the Kolmogorov quotient of X₀ collapses packets, or that no T₀ subspace of X₀ meets a packet in two points. On-disk: [x-03]/[z-19]/[x-06]/[r3s-08] contain no "indiscrete", "T₀", "Kolmogorov", "indistinguishable" (grep, §3 G-09). Searches S-03, S-04, S-23, C-04 (§3): no hit.

*Required change (MINOR):* cite the T₀-tification/orbit-class-space vocabulary (Yokoyama 2020) for the general principle and quote [x-03] p. 64's T₁ Remark as the printed contrast; state that the indiscreteness is created by the compactness of the packet base, exactly where the adelic model's base is not compact.

### C2 — Theorem T: for any Q>0-space Z and z with relatively compact Q>0-orbit, the Q>0-orbit of (z,u) in Z × R>0 is not closed; Z ×_{Q>0} R>0 is not T₁; hence Y₀ is not T₁ / not metrizable / not a foliated space (y0-witness/adjudication.md §4.3, §7 item 1)

**Verdict: PARTIAL.** The theorem's two ingredients are printed: (i) "X/G is T₁ iff every orbit is closed" is definition-level and is stated for flows in Yokoyama arXiv:2012.00849, proof of Lemma 7.2 ("a point x ∈ M is T₁ if and only if {x} is closed … and it is S₁ if and only if O(x) is closed with respect to the quotient topology τ_v on the orbit space M/v") and Cor. 7.3(1) ("O ⊆ Cl(v) if and only if O is T₁ as a point in the orbit space M/v"); (ii) the question "are the points of a Q>0-suspension closed?" is on Deninger's printed page with the **opposite answer for the adelic base**: [x-03] p. 64 Remark (quoted under C1) — the orbits of Q>0 on Q>0Ẑ× × R>0 are closed by [LR00, Lemma 3.1], so the adelic model Y is T₁ (and irreducible, Prop. 10.3, hence non-Hausdorff). Theorem T's content beyond these is the two-line observation that a **relatively compact** orbit in Z forces the orbit of (z,u) to accumulate at (w, v) with v ∉ uQ>0, so points of Z ×_{Q>0} R>0 are not closed whenever Z is compact — in particular for Y₀ = X̌₀(S¹) ×_{Q>0} R>0 (Cor. T1) and for every Q>0-suspension of a compact base (Cor. T2).

*Precise difference from the sources.* [LR00] treats the action on the (non-compact) adelic base and finds closed orbits; Deninger transfers that to his adelic model Y. No source states that the printed unitary system Y₀ is not T₁, not metrizable, or not a foliated space, nor that no Q>0-suspension of a compact base can be T₁. Laca–Raeburn's own object of study is the quasi-orbit space (abstract, arXiv:math/9911134: "the computation of the quasi-orbit space for the action of the multiplicative positive rationals on the space of finite adeles"), i.e. the T₀-tification — the same vocabulary as C1.

*Required change (MINOR):* cite the definition-level criterion; quote [x-03] p. 64 + [LR00, Lemma 3.1] as the printed T₁ statement for the adelic model and say explicitly that Theorem T does not contradict it (different base topology). Searches S-05, S-22, S-23, C-04: no hit on Y₀ or on compact-base suspensions.

### C7 — cl(γ) = Γ^E_p exactly (chartwise and globally, Spec Z); for every arithmetic scheme, admissible E and closed point x₀ the packet is the fiber of the continuous descended projection, hence closed and flow-invariant (referee-s14/B-corA1-adjudication.md §8 N-1, N-2)

**Verdict: PARTIAL — mechanism anticipated, statement not found (agreeing with the adjudication's own N-1 entry); the equality cl(γ) = Γ^E_p is a corollary of the dual-checked Theorem A plus N-1 and is not in the sources.**

*Anchors re-read this session.* [x-03] p. 31 (pdftotext line 1696): "The fibres of pr_{X₀}: X̌₀(C)_{E_tors} → X₀ are Q₀>0-invariant. We will now analyze the structures of the Q₀>0-sets C_{x₀} = pr_{X₀}^{−1}(x₀) in X̌₀(C)_{E_tors} for points x₀ of X₀ whose residue field κ(x₀) is finite." [x-03] Lemma 7.3 p. 43 (line 2425): "the injective maps F_ν … are continuous, closed and open. In particular F_ν(X(C)) is closed and open in X(C)"; Prop. 7.4 a) "X(C) is a closed and open subspace of X̌(C)"; continuity of pr (Lemma 7.1, p. 40; per the adjudication). [r3s-08] p. 14 displays the descended projection (per the adjudication; not re-read). The only "closed in" statements in [x-03] concern X(C) ⊂ X̌(C), X̌(S¹) ⊂ X̌(C) (line 2942) and X(C)′ (line 3115) — never a packet (grep "closed subset|closed subspace|is closed in|are closed in", §3 G-01).

*Not found:* "Γ_{x₀} is closed in X₀", "the closure of a periodic orbit is its packet", or "packets are minimal sets" — in any source, search or citation graph (the previous sweep's N1 searches plus S-03/S-23 here). Verdict unchanged from the adjudication's ledger; no new prior art surfaced.

### C10 — S4′ (m2c-feasibility-ledger §15): has anyone posed or studied the inverse length-spectrum problem for foliated flows with spectrum {log p} (once each, simple, return derivative p^{1/2}·O) and an archimedean leaf?

**Verdict: ANTICIPATED as a posed problem — by Deninger himself (2002, 2005), by Leichtnam (2006, as an explicit Open Question), and in the physics literature by Berry–Keating (1999); NOT found as a studied realizability/inverse problem in the dynamics literature (nothing beyond Deninger's own X₀ construction attacks it).**

*Deninger's posing (on disk, read this session).* [x-21] = *Number theory and dynamical systems on foliated spaces* (2002), pdftotext lines 660–672 (the correspondence table, then): "finite place p ≙ closed orbit γ = γ_p not contained in a leaf and hence transversal to F such that l(γ_p) = log Np and ε_{γ_p}(k) = 1 for all k ≥ 1. infinite place p ≙ fixed point x_p such that κ_{x_p} = κ_p and ε_{x_p} = 1. … In order to understand number theory more deeply in geometric terms it would be very desirable to find a system (X, φ^t, F) which actually realizes this correspondence. For this the class of compact 3-manifolds as phase spaces has to be generalized as will become clear from the following discussion." The same paragraph verbatim in [x-20] = Den05 (arXiv:math/0505354), lines 1255–1265 (printed p. 26), followed on p. 27 by "in a dynamical system corresponding to number theory we must have α = 1 … φ^t conformal on TF with factor e^t (31) … However … this is not possible in the manifold setting of corollary 5.5 which actually implies α = 0", and "Thus it becomes vital to find phase spaces X more general than manifolds for which the analogue of corollary 5.5 holds and where α ≠ 0 and in particular α = 1 becomes possible" (p. 28); and p. 33: "In the number theoretical case the eigenvalues of T_xφ^{log Np} on T_xF for x ∈ γ_p would therefore be complex conjugate numbers of absolute value Np^{1/2}." These are exactly S4′'s clauses (compact non-manifold phase space with Riemann-surface leaves; one closed orbit per prime, length log Np, ε = 1; archimedean fixed points/leaf; return derivative of modulus Np^{1/2}). [x-03] p. 40 (re-read) re-poses it as the sub-dynamical-system question inside X₀.

*Leichtnam's posing.* [r3s-21] = E. Leichtnam, *Scaling group flow and Lefschetz trace formula for laminated spaces with p-adic transversal* (arXiv:math/0603576v2), abstract: "The existence of such a foliated space and flow φ^t is still unknown except when Y is an elliptic curve (see Deninger [De02])"; p. 2: "Notice that the existence of such a quadruple (S_Q, F, g, φ^t) is still unknown"; Open Question 2 (lines 935–945): "Does there exist a laminated foliated space (S_Y = L_Y ×_{q^Z} R^{+*}, F, g, φ^t) satisfying all the assumptions of Proposition 2 and Theorem 2 and the following assumption: (A) One has a natural bijection w ↦ γ_w between the set of closed points of Y and the set of primitive closed orbits of (S_Y, φ^t) satisfying log Nw = l(γ_w)." — the function-field form of the inverse length-spectrum problem, posed in 2006. [r3s-20] (Leichtnam 2013, line 123): "it is not known whether or not the assumptions of Section 4 are" satisfiable.

*Physics posing.* M. V. Berry, J. P. Keating, *The Riemann zeros and eigenvalue asymptotics*, SIAM Review 41 (1999) (PDF fetched from empslocal.ex.ac.uk, pdftotext): abstract: "the 'Riemann dynamics' should be chaotic and have periodic orbits whose periods are multiples of logarithms of prime numbers"; table (2.14): "Periods m T_p | m log p"; §2: "primes acquire a new significance, as primitive periodic orbits, whose periods are log p"; summary item e: "The classical periodic orbits of the Riemann dynamics have periods that are independent of 'energy' t, and given by multiples of logarithms of prime numbers … each primitive orbit is labelled by its own symbol (the prime p)." A heuristic construction with exactly this spectrum: G. Sierra, arXiv:1404.4252 (J. Phys. A 47 (2014) 325204; abstract read): mirror accelerations "provide primitive periodic orbits associated to the prime numbers p, whose periods, measured by the observer's clock, are log p".

*Dynamics literature on inverse period/length problems (searched, S-13, S-26, C-03).* Nearest items: H. de Jong, *On sets of periodic orbit lengths in finitely presented dynamical systems*, ETDS 2025 (arXiv:2510.10848) — classification and realization of least-period sets for FP systems (discrete time, integer periods); Miyanishi, *Circle foliations revisited: periods of flows whose orbits are all closed* (arXiv:2408.06056); Kim–Morishita–Noda–Terashima, Münster J. Math. 14 (2021) 323–348 (PDF read): FDS³ examples "such that P_S is a countably infinite set" via a horseshoe insertion (Lemma 3.3) — countably many closed orbits, lengths not prescribed. Nothing poses or answers the realizability of {log p} once each with prescribed derivative in a compact foliated 3-space.

*Precise difference.* S4′ is Deninger's 2002/2005 desideratum restated in the program's S4 vocabulary (plus the χ ≠ 0 archimedean-leaf clause from the y0-witness Euler-characteristic constraint). The *problem* is not new and must be attributed to [x-21]/[x-20]/[r3s-21]; what is unclaimed anywhere is a realizability theorem or obstruction for that spectrum. Required change: MAJOR in wording if S4′ is presented as a new problem; none if presented as Deninger's problem re-scoped.

[remaining claims in progress]

---

## 3. Complete search log (engine · date · phrasing → result)

[in progress — appended as searches run]

---

## 4. Documents opened this session

**Program files:** `referee-s14/novelty-F.md`, `novelty-O.md`, `novelty-adjudication.md` (full); `s14/qstar-adjudication.md` §§1–4, §9; `s14/adversarial/adjudication.md` §8; `s14/adversarial/face-b-refuter-F.md` §0; `s14/qa-kill.md` §6, §10; `s14/dqm-adjudication.md` §10; `s14/w3-adjudication.md` §2, §8, §9; `s14/y0-witness/adjudication.md` §4.3, §7; `s14/y0-witness/verify-F.md` §7; `s14/y0-witness/verify-O.md` §9; `referee-s14/B-corA1-adjudication.md` §8, §10; `referee-s14/A-thmB-adjudication.md` §7; `m2c-feasibility-ledger.md` §15 (S4′ paragraph).

**Sources (on disk / fetched):** [appended as opened]

---

## 5. Unreachable sources (standing order 1)

[appended as encountered]
