# Q* FACE (b), KILL DIRECTION — the archimedean-escape obstruction: no compact flow maps equivariantly onto more than finitely many packets of X_0

**Program:** RH research program, direction C3-r (geometric substrate for a Weil-positivity proof of RH), milestone M2c, Route 2, step S4. **Session 14. Date: 2026-09-02.**
**Charter:** `results/c3-r/probe-9.3-adjudication.md` §5, question **Q-b** (the mapping face of Q*), kill direction.
**Author:** probe agent, Session 14; independent of the Session-14 Q-a probe.
**Standing orders observed:** SO-5 (nothing load-bearing from memory; every source claim read this session from the on-disk PDF at a stated printed page) and SO-7 (novelty ledger, §10).

---

## 0. VERDICT (stated first)

**THEOREM (NO).** Q-b is answered **NO**, and by a mechanism strictly stronger than the question asked. What is proved here, in full, is:

> **Main Theorem (§5.3).** Let X_0 = spec Z, C = ℂ, N_0 = N, let E be **any** admissible class of characters in the sense of [x-03] Def. 4.1, and let
> X_0 = X̌_0(C)_E ×_{Q^{>0}} R^{>0} be Deninger's dynamical system with its flow φ^t([P_0,u]) = [P_0, ue^t] ([x-03] §6, p. 38).
> Let (Y, φ) be a **nonempty quasi-compact** topological space carrying a continuous R-action, and let f : Y → X_0 be **continuous and flow-equivariant**. Then there is a **finite** set S of primes with
>
>   **f(Y) ⊆ ⨆_{p ∈ S} Γ^E_p ,  and Y = ⨆_{p ∈ S} f^{-1}(Γ^E_p) is a partition of Y into clopen flow-invariant pieces.**
>
> In particular the image of f is contained in the union of finitely many packets: it contains no characteristic-zero point of X_0 at all.

**Consequences, each a theorem (§6):**

1. **Q-b: NO.** No compact metrizable 3-dimensional lamination (Y, F, φ) with one closed orbit γ_p of length log p per prime admits a continuous flow-equivariant map f : Y → X_0 with f(γ_p) ⊂ Γ_p. (Such an f would give S = {all primes}, infinite.) The hypotheses "dimension 3", "lamination", "foliated flow", "exactly one orbit per prime", "metrizable" are **not used**: compactness and equivariance alone suffice.
2. **The same statement for the unitary system** X̌_0(S^1)_E ×_{Q^{>0}} R^{>0} — Deninger's Y_0, the closure of the union of all periodic orbits ([x-03] §8 p. 49; [x-06] §4 p. 12, which states verbatim that this closure *is* the E-subsystem built from unitary characters, hence satisfies (Tors)). The unitary system is a flow-invariant subspace of X_0, so the Main Theorem applies verbatim.
3. **Q-a: NO** (the subspace face, which was not this probe's charter but falls out). Every nonempty quasi-compact flow-invariant **subspace** K ⊆ X_0 satisfies K ⊆ ⨆_{p∈S} Γ^E_p for a finite set S of primes. So no quasi-compact invariant subspace meets infinitely many packets — a fortiori none meets every packet in exactly one orbit, of dimension 3 or any other dimension, Hausdorff-in-itself or not.
4. **S4 is dead, hence Route 2 is dead.** Both alternatives of Deninger's own question ([x-03] §6 p. 40: "Is there a sub-dynamical system Y_0 ⊂ X_0 … **or at least one which maps to X_0** …") are answered **NO** whenever Y_0 is required to be compact — which every reading in the program (a Riemann-surface lamination in the sense of [Ghy99]; ALKL hypothesis H1) requires. The closed half was already dead (banked Corollary B, adjudication §4.2); the mapping half dies here, and dies harder: the obstruction is not dimension, not orbit multiplicity, not monodromy — it is that **the accumulation of the closed orbits as p → ∞ is forced into the characteristic-zero locus of X_0, and that locus is uniformly dissipative: it carries a lower semicontinuous, strictly positive, flow-conformal weight of exponent one.**
5. **Q-c (adjudication §5, bookkeeping) is answered affirmatively as a by-product:** cl_{X_0}(γ) = Γ^E_p exactly, for every periodic orbit γ ⊂ Γ^E_p (§6.5) — because Γ^E_p is the fibre of a continuous map X_0 → spec Z and is therefore **closed**.

**What is NOT claimed.** The theorem is about X_0 as constructed in [x-03] (and its E-subsystems, including the unitary one). It says nothing about the conjectural Arakelov-type compactification X̄_0 that [x-03] p. 39 predicts, whose added fixed points are exactly the archimedean end that the escape function detects. That is the single residual escape and it is named precisely in §9.3. It is not a gap in the proof; it is a different target.

---

## 1. Sources read this session, with printed-page anchors

All extractions were made fresh this session with `pdftotext -layout` into the session scratchpad; every quotation below was read verbatim in those extractions. Printed pages were computed from the page markers of the extraction (a line-number → printed-page table was built mechanically; each anchor below was checked against it).

**[x-03]** C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`. Read verbatim this session:

| Item | Printed page | What was read |
|---|---|---|
| Remark 3.4 | 23 | points of X̊(C) as multiplicative maps P : R → C |
| (Tors), (Image), Def. 4.1, Prop. 4.2, (30)/(31) | 27 | "(Tors) the group ker(χ)_tors = ker(χ\|_{μ(κ)}) is finite and \|(ker χ)_tors\| ∈ N_0"; "(Image) Only if char κ > 0. If χ(κ^×) is torsion, then κ^× is torsion as well"; Def. 4.1 "A class E … is (N_0−)admissible if for any σ ∈ Aut κ resp. ν ∈ N_0 the character χ is in E if and only if χ∘σ resp. χ_ν = χ∘( )^ν is in E. **Moreover the characters in E should satisfy (Tors)**"; Prop. 4.2 (G-, N_0-, Q^{>0}-invariance; "The monoid N_0 acts by injections"); the maps pr_X, pr_{X_0} and "**Both pr_X and pr_{X_0} above extend Q^{>0}_0-equivariantly to maps pr_X : X̌(C)_E → X and pr_{X_0} : X̌_0(C)_E → X_0. Here we let Q^{>0}_0 act trivially on X and X_0**" |
| Examples E_tors, E_max | 28 | "1) E_tors : (Tors) holds. 2) E_max : (Tors) and (Image) hold" |
| chain E_f ⊂ … ⊂ E_max ⊂ E_tors | 29 | inclusion chain |
| C_{x_0} = pr_0^{-1}(x_0) | 31 | "The fibres of pr_{X_0} : X̌_0(C)_{E_tors} → X_0 are Q^{>0}_0-invariant … C_{x_0} = pr_0^{-1}(x_0)^{Q^{>0}_0} = ⋃_{ν∈N_0} F_ν^{-1} pr_0^{-1}(x_0)"; and "The fibre pr_0^{-1}(x_0) consists of the G-orbits of all pairs (x,P^×) where x is a point of X over x_0 and P^× : κ(x)^× → C^× satisfies (Tors). Since κ(x)^× is torsion this means that ker P^× = (ker P^×)_tors is finite hence cyclic and \|ker P^×\| ∈ N_0" |
| (40), (41), (42), (43), (44), (45), (46) | 33 | **the map ρ**: "(41) ρ : X̊(C)_{E_tors} → N_0, (x,P^×) ↦ \|(Ker P^×)_tors\|"; "For ν ∈ N_0 let ν_x be the prime-to-char κ(x) part of ν. If char κ(x) = 0 then ν_x = ν"; "(42) \|(Ker P^×∘( )^ν)_tors\| = ν_x \|(Ker P^×)_tors\|"; "(43) ρ(F_ν(P)) = ν_x ρ(P)"; "(45) ρ : X̌(C)_{Q,E_tors} → Q^{>0}_0" (Q^{>0}_0-equivariant); "The map ρ factors over a map ρ_0 on X̌_0(C)_{E_tors}" |
| Prop. 5.1 and its proof; Thm. 5.2 | 34 | "ρ(Q̌) = ν_x^{-1}\|(ker P^×)_tors\|" for Q̌ = F_ν^{-1}(x,P^×); Thm. 5.2: "{P_0 ∈ X̌_0(C)_E \| (Q^{>0}_0)_{P_0} ≠ 1} = ⨿_{x_0} C^E_{x_0}"; "For any point P_0 ∈ C^E_{x_0} the isotropy group of P_0 is (Q^{>0}_0)_{P_0} = N x_0^Z" |
| §6 opening: suspension, flow, Γ_{x_0} | 38 | "X_0 = X̌_0(C)_E ×_{Q^{>0}_0} R^{>0} … the quotient of X̌_0(C)_E × R^{>0} by the right Q^{>0}_0-action given by (P_0,u)q = (P_0 q, q^{-1}u) = (F_q(P_0), q^{-1}u)"; "The group R^{>0} acts on X_0 via the second factor: [P_0,u]·v = [P_0,uv]"; "φ^t([P_0,u]) = [P_0, ue^t]"; "Γ_{x_0} = C_{x_0} ×_{Q^{>0}_0} R^{>0} ⊂ X_0"; "all R^{>0}-orbits in Γ_{x_0} are circles R^{>0}/N x_0^Z"; "We set Γ^E_{x_0} = C^E_{x_0} ×_{Q^{>0}_0} R^{>0} where C^E_{x_0} = C_{x_0} ∩ X̌_0(C)_E" |
| Thm. 6.1; "we omit E from the notation" | 39 | Thm. 6.1 verbatim; and "In the following observation we omit E from the notation" |
| the S4 question | 40 | "The system X_0 may have to be replaced by a much smaller system: Is there a sub-dynamical system Y_0 ⊂ X_0 = X̌_0(C) ×_{Q^{>0}} R^{>0} or at least one which maps to X_0 such that dim Y_0 = 2d+1 … If d = 1, is there such a Y_0 which is a Riemann surface lamination in the sense of [Ghy99]?" |
| §7 opening; Lemma 7.1 | 40 | "we give X̊(C) the topology of pointwise convergence. It is the subspace topology induced by the Tychonov topology of C^R"; "Since R is countable, X̊(C) is a metrizable topological space"; Lemma 7.1 (pr_X continuous) |
| Lemma 7.3; quotient topology on X̊_0(C) | 42 | "We equip X̊_0(C) = X̊(C)/G with the quotient topology. Using Lemma 7.1 one sees that pr_X : X̊(C) → X and hence also pr_{X_0} : X̊_0(C) → X_0 are continuous"; Lemma 7.3: "the injective maps F_ν : X̊(C) ↪ X̊(C) for ν ∈ N are continuous, closed and open. In particular F_ν(X̊(C)) is closed and open in X̊(C)" |
| colimit topology (53); Prop. 7.4; X̌_0(C) = X̌(C)/G; openness of π, π̌; continuity of pr | 43 | "We give X̌(C) = colim_{N_0} X̊(C) the inductive limit topology … Thus Z ⊂ X̌(C) is closed, resp. open if and only if F_ν(Z) ∩ X̊(C) is closed, resp. open in X̊(C) for all ν ∈ N_0"; Prop. 7.4 "a) X̊(C) is a closed and open subspace of X̌(C). b) F_q : X̌(C) → X̌(C) is a homeomorphism for every q ∈ Q^{>0}_0. c) The group G acts by homeomorphisms on X̌(C)"; "We give X̌_0(C) = X̌(C)/G the quotient topology … The projections π, π̌ are continuous and since G acts by homeomorphisms, also **open**. Moreover the projections pr_X : X̌(C) → X and pr_{X_0} : X̌_0(C) → X_0 are continuous" |
| Cor. 7.8, Cor. 7.9 | 45 | Hausdorffness of X̊_0(C), X̌_0(C) |
| E-subspace topologies | 47 | "We give X̌(C)_E = colim_{N_0} X̊(C)_E and X̌_0(C)_E = colim_{N_0} X̊_0(C)_E the inductive limit topologies. They agree with the subspace topologies … because the subspaces F_ν^{-1}X̊(C) and F_ν^{-1}X̊_0(C) are open in X̌(C) resp. X̌_0(C) for all ν ∈ N_0" |
| (65)–(67): ρ continuous into A_f/Ẑ^× | 48 | "we obtain a **continuous** map which is independent of ι, ρ : X̌(C)_E → Q^{>0} ⊔̇ ⊔̇_p Q^{>0}/p^Z. Here the right hand side carries the quotient topology of Ȟ_{E_tors} or equivalently the subspace topology of A_f/Ẑ^×. For E = E_tors this is the same map as in (46)" |
| (68); "not properly discontinuous" | 49 | "The Q^{>0}-action on Ȟ_{E_tors} × R^{>0} is not properly discontinuous. In section 10, we will see that this works to our advantage" |
| §8 opening; Y_0; Claim 8.1 | 49 | "the dynamical system X_0 = X̌_0(C) ×_{Q^{>0}} R^{>0} is infinite dimensional, whereas we are searching for a system of dimension 2 dim X_0 + 1, e.g. 3 in the case of X_0 = spec Z"; "Y_0 = X̌_0(S^1) ×_{Q^{>0}} R^{>0}"; "the system Y_0 is still infinite-dimensional"; Claim 8.1; "known for number rings"; "[Per11, Theorem 1]" |
| Thm. 8.2; Lemma 8.3 | 50 | "X̌(C)_per = X̌(S^1) and X̌_0(C)_per = X̌_0(S^1)"; "X̊(C)_per = {(x,P^×) ∈ X̊(C) \| κ(x) ≅ F̄_p for some p and ker P^× is finite}"; "Since X̊(S^1) is closed in X̊(C) the subspace X̌(S^1) is closed in X̌(C) as well"; Lemma 8.3 statement and the density argument |
| §6 remark on the compactification | 39 | "X_0 should have a 'compactification' X̄_0 corresponding to an Arakelov compactification X̄_0 of X_0. The fixed points of the R-action on X̄_0 should be the set X_0(C)/F_∞"; and "for z ∈ X_0(C) ∖ X_0(R) there are two orbits tending to the fixed point [z,0], namely [z,±1]u for u → 0+" |
| intro | 2 | "Each periodic orbit of X_0 lies in exactly one packet Γ_{x_0}. … The **compact** packets Γ_{x_0} are reminiscient of invariant tori. There are no fixed points of the flow." |

**[x-06]** C. Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`. Read verbatim: Theorem 4.2 (printed p. 11) and its commentary (p. 12): "The **compact** subsets Γ_{x_0} ⊂ X_0 consist of periodic orbits of length log N x_0 … and they are pairwise disjoint"; and — decisive for the scope of the Main Theorem — p. 12: "The space X_0^E is infinite dimensional if dim X_0 ≥ 1 and one could hope that the sub-dynamical system obtained as the closure of the union of all its compact orbits might be significantly smaller. However, this is not the case as follows from [Den22a, Theorem 8.2]. **The closure is the subsystem obtained by replacing X̊(C)_E in the previous constructions with the subspace of pairs (x,P^×) with P^× : κ(x)^× → S^1 a unitary character.**"

**Program-internal (read in full, not re-derived here):** `results/c3-r/probe-9.3-adjudication.md` (binding; §2 verified anchors, §4 banked theorems, §5 Q*), `results/c3-r/probe-9.3-a.md`, `results/c3-r/probe-9.3-b.md`, `results/c3-r/probe-9.4-note.md`, `results/c3-r/m2c-feasibility-ledger.md` §§2–4, 8–10, 12, `directions/C3-geometric-substrate.md` "Current frontier".

**Read but NOT cited for anything load-bearing:** [r3s-08] Morishita, arXiv:2508.15971 — per adjudication §4 item 4 the program must not cite it for topology, and nothing below does. Nothing in this note uses [r3s-08], [ALKL], [ÁLKL23], [ALKM], Leichtnam, or [D25].

---

## 2. The objects, written out

Throughout: **X_0 = spec Z**, K_0 = Q, K = Q̄, X = spec Z̄ (the normalization of X_0 in K), G = Aut(Q̄/Q), **C = ℂ**, **N_0 = N**, Q^{>0}_0 = Q^{>0}. All of §2 is transcription from the anchors of §1; nothing here is new.

**2.1 Points.** X̊(C) is the set of pairs (x, P^×) with x ∈ X and P^× : κ(x)^× → C^× a character; equivalently ([x-03] Remark 3.4, p. 23) the set of multiplicative maps P : Z̄ → C with P(0) = 0, P(1) = 1, whose zero-set p̄_x := P^{-1}(0) is a prime ideal, P factoring through Z̄/p̄_x. Since X = spec Z̄ has Krull dimension 1, x is either the **generic point** η (κ(η) = Q̄, p̄_η = (0)) or a **closed point** over a rational prime p (κ(x) = F̄_p). The topology is pointwise convergence on Z̄, a metrizable subspace topology of the Tychonov topology of C^{Z̄} ([x-03] §7, p. 40).

**2.2 Admissible classes.** E is admissible (Def. 4.1, p. 27) iff for all σ ∈ Aut κ and ν ∈ N_0, χ ∈ E ⟺ χ∘σ ∈ E ⟺ χ^ν = χ∘( )^ν ∈ E, **and every χ ∈ E satisfies (Tors)**: ker(χ)_tors = ker(χ|_{μ(κ)}) is finite with |(ker χ)_tors| ∈ N_0. Two consequences used constantly below:

* **(Tors) is not optional.** It is part of the definition of admissibility, so **every** E-system carries the finiteness that the escape function of §3.2 measures. (This is why the Main Theorem needs no hypothesis on E beyond admissibility, and in particular covers the "cut" classes E(a_0) of probe A's Theorem C(b).)
* **Over spec Z, (Image) is vacuous**, hence E_tors = E_max as conditions. Indeed (Image) is imposed only when char κ > 0, and then reads "if χ(κ^×) is torsion then κ^× is torsion as well"; the residue fields at the closed points of X = spec Z̄ are F̄_p, whose multiplicative groups are torsion, so the conclusion always holds. Therefore every admissible E over spec Z satisfies E ⊆ E_max, and Theorem 5.2 and Theorem 6.1 apply to it.

**2.3 Colimit and suspension.** X̌(C) = colim_{N_0} X̊(C) along the injections F_ν(P) = P∘( )^ν, with the inductive-limit topology; each stratum F_ν^{-1}X̊(C) is open (Prop. 7.4a + 7.4b, p. 43); every point of X̌(C) has the form F_ν^{-1}(P) with P ∈ X̊(C), ν ∈ N_0 (Deninger's own notation, Prop. 5.1's proof, p. 34). X̌_0(C) = X̌(C)/G with the quotient topology; the projections π, π̌ are continuous and **open** (p. 43). The E-versions carry the subspace = inductive-limit topologies (p. 47). Finally

  **X_0 = X̌_0(C)_E ×_{Q^{>0}} R^{>0} = (X̌_0(C)_E × R^{>0}) / Q^{>0}, (P_0,u)·q = (F_q(P_0), q^{-1}u),**

with the quotient topology, and φ^t[P_0,u] = [P_0, ue^t] ([x-03] §6, p. 38). The quotient map

  **Q : X̌_0(C)_E × R^{>0} ⟶ X_0**

is continuous and **open** (the quotient of a space by a group acting by homeomorphisms; the saturation of an open set is a union of homeomorphic translates). This openness is used three times below and is the only topological fact about X_0 that the proof needs beyond §1's anchors.

**2.4 Packets.** For a closed point x_0 = (p) of X_0 = spec Z, C_{x_0} = pr_{X_0}^{-1}(x_0) ⊂ X̌_0(C)_{E_tors} (p. 31, verbatim), C^E_{x_0} = C_{x_0} ∩ X̌_0(C)_E, and Γ^E_p := Γ^E_{x_0} = C^E_{x_0} ×_{Q^{>0}} R^{>0} ⊂ X_0 (p. 38). Two facts recorded verbatim and used below:

* **(P1) Γ^E_p is exactly the set of points of X_0 lying over (p).** This is the displayed definition C_{x_0} = pr_{X_0}^{-1}(x_0) together with Q^{>0}-invariance of the fibres (p. 31) and the definition of Γ^E_{x_0} (p. 38). Since pr_{X_0} is Q^{>0}-equivariant for the trivial action on X_0 (p. 27), the fibres of pr_{X_0} descend to the suspension. **Consequently the packets are pairwise disjoint** (distinct fibres) — as [x-06] Thm. 4.2 (p. 12) also states.
* **(P2) Every point of X_0 lies over (0) or over exactly one (p).** Immediate from (P1) and dim spec Z = 1. Write

    **X_0^{Q} := {z ∈ X_0 : z lies over the generic point (0) of spec Z} = X_0 ∖ ⨆_p Γ^E_p**

  for the **characteristic-zero locus**. It is flow-invariant and Q^{>0}-invariant (F_q does not change x).
* **(P3) (Thm. 6.1, p. 39; Thm. 5.2, p. 34.)** The points of X_0 with nontrivial isotropy for the R^{>0}-action are exactly ⨆_{x_0} Γ^E_{x_0}, and each point of Γ^E_p has isotropy p^Z, i.e. lies on a **circle of length log p**. In particular **every point of X_0^{Q} lies on an injectively parametrized R-orbit**: the flow on the characteristic-zero locus is free and has no periodic orbits.

**2.5 The unitary system.** X̊(S^1) ⊂ X̊(C) is the subspace of (x,P^×) with P^× valued in S^1; it is closed in X̊(C) ([x-03] p. 50, verbatim). Deninger's Y_0 = X̌_0(S^1)×_{Q^{>0}}R^{>0} is the closure of the union of all periodic orbits (Thm. 8.2, p. 50, unconditional for spec Z via [Per11]), and — [x-06] p. 12, verbatim — it is "the subsystem obtained by replacing X̊(C)_E … with the subspace of pairs (x,P^×) with P^× unitary", i.e. it is the **E-subsystem** X̌_0(S^1)_E ×_{Q^{>0}} R^{>0} with (Tors) in force. It is therefore a flow-invariant subspace of X_0 and everything below applies to it verbatim.

**2.6 The statement of Q-b.** (Adjudication §5.) Does a compact metrizable 3-dimensional lamination (Y, F, φ) with exactly one closed orbit γ_p of length log p per prime admit a continuous flow-equivariant f : Y → X_0 (or to the unitary system) with f(γ_p) ⊂ Γ_p?
