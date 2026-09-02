# Q* FACE (b), KILL DIRECTION — the dissipation obstruction: no quasi-compact flow maps equivariantly into more than finitely many packets of X_0

**Program:** RH research program, direction C3-r (geometric substrate for a Weil-positivity proof of RH), milestone M2c, Route 2, step S4. **Session 14. Date: 2026-09-02.**
**Charter:** `results/c3-r/probe-9.3-adjudication.md` §5, question **Q-b** (the mapping face of Q*), kill direction.
**Author:** probe agent, Session 14; independent of the Session-14 Q-a probe.
**Standing orders observed:** SO-5 (nothing load-bearing from memory; every source claim read this session from the on-disk PDF at a stated printed page) and SO-7 (novelty ledger, §12).
**Provenance:** a previous run of this probe was killed by a usage limit after §2. That partial draft is preserved at `qb-kill.partial.bak`. Everything it asserted has been re-derived from the sources this session; **one of its five §0 consequences was found to be argued incorrectly and is repaired here** (§0 note (c) and §8.5): the partial draft deduced `cl(γ) = Γ^E_p` from closedness of the packet alone, which gives only "⊆". The equality is true — it is banked (Theorem A) and was discharged at referee grade in this same session — but not for the reason the draft gave.

---

## 0. VERDICT (stated first)

**THEOREM (NO).** Q-b is answered **NO**, and by a mechanism strictly stronger than the question asked. What is proved here, in full, is:

> **Main Theorem (§7.1).** Let X_0 = spec Z, C = ℂ, N_0 = N, let **E be any admissible class of characters** in the sense of [x-03] Def. 4.1 (printed p. 27), and let
>
>   **X_0 = X̌_0(C)_E ×_{Q^{>0}} R^{>0}**, φ^t([P_0,u]) = [P_0, u e^t]
>
> be Deninger's dynamical system ([x-03] §6, printed p. 38). Let (Y, φ) be a **nonempty quasi-compact** topological space carrying a continuous R-action, and let f : Y → X_0 be **continuous and flow-equivariant**. Then the set
>
>   **S = { p prime : f(Y) ∩ Γ^E_p ≠ ∅ }  is FINITE,**
>
> f(Y) ⊆ ⨆_{p ∈ S} Γ^E_p (so f(Y) contains no characteristic-zero point of X_0 at all), and Y = ⨆_{p ∈ S} f^{-1}(Γ^E_p) is a partition of Y into finitely many **clopen flow-invariant** pieces.

The proof has exactly two moving parts, both new, both elementary once set up:

* **Theorem D (§5.4, dissipation).** X_0 carries a **strictly positive, lower semicontinuous, flow-conformal weight of exponent one**: a function W : X_0 → (0, ∞] with W ∘ φ^t = e^t · W, finite exactly on the characteristic-zero locus (this last clause is where admissibility, i.e. (Tors), is consumed). A positive l.s.c. function on a nonempty quasi-compact set attains a **positive** minimum; a conformal weight of exponent one is driven to 0 along backward orbits. Hence **no nonempty quasi-compact flow-invariant subset of X_0 meets the characteristic-zero locus.**
* **Theorem S (§6, packet separation at infinity).** If z_i ∈ Γ^E_{p_i} with p_i → ∞ and z_i → z in X_0, then z lies over the **generic** point of spec Z. (One line, after the set-up: the rational prime q ∈ Z̄ has |P_i(q)| = 1 for every character over characteristic p_i ≠ q, but P(q) = 0 for every character over characteristic q; and evaluation at q is continuous for the topology of pointwise convergence.)

The two are contradictory for an infinite S, and that is the whole kill: the closed orbits must accumulate, the accumulation must land in characteristic zero, and characteristic zero is uniformly dissipative.

**Consequences, each a theorem (§8):**

1. **Q-b: NO.** No compact metrizable 3-dimensional lamination (Y, F, φ) with exactly one closed orbit γ_p of length log p per prime admits a continuous flow-equivariant f : Y → X_0 with f(γ_p) ⊂ Γ^E_p (such an f forces S = {all primes}). The hypotheses "dimension 3", "lamination", "foliated flow", "one orbit per prime", "metrizable" are **not used**: quasi-compactness and equivariance alone suffice. In particular no mean-dimension, entropy, minimal-set-complexity or holonomy input is needed — the charter's anticipated route (see §9) is not merely unnecessary, its central premise is false (§9.1).
2. **The same for the unitary system** (§8.2). Deninger's Y_0 = the closure of the union of all periodic orbits = the E-subsystem built from unitary characters ([x-03] §8 printed p. 49 and Thm 8.2 printed p. 50; [x-06] printed p. 12, verbatim) is a flow-invariant subspace of X_0, so the Main Theorem applies verbatim to any continuous equivariant f : Y → Y_0. **Corollary: Y_0 is not quasi-compact** — it meets every packet.
3. **Q-a: NO** (the subspace face, not this probe's charter but a corollary). Every nonempty quasi-compact flow-invariant **subspace** K ⊆ X_0 satisfies K ⊆ ⨆_{p ∈ S} Γ^E_p for a finite S. So no quasi-compact invariant subspace meets infinitely many packets — a fortiori none meets every packet in exactly one orbit, at dimension 3 or any other dimension, Hausdorff-in-itself or not. The hypotheses "Hausdorff in itself" and "dim = 3" of Q-a are not used.
4. **S4 is dead, and with it Route 2** (§8.4). Both alternatives of Deninger's own question ([x-03] printed p. 40: "Is there a sub-dynamical system Y_0 ⊂ X_0 … **or at least one which maps to X_0** …") are answered **NO** whenever the sought object is compact — which every reading in the program requires (a Riemann-surface lamination in the sense of [Ghy99]; ALKL hypothesis H1; the ledger's S4 statement). The closed half was already dead (banked Corollary B, adjudication §4 item 2); the mapping half dies here, and dies harder. Per adjudication §5, "a NO on both kills S4 and with it Route 2, firing the kill-criterion input."
5. **Sharpness (§10.1).** The theorem is exactly as strong as (Tors). In the E-free system X̌_0(C) ×_{Q^{>0}} R^{>0} there is an explicit nonempty quasi-compact flow-invariant set D meeting the fibre over **every** point of spec Z (§10.1) — so the Main Theorem's conclusion genuinely fails there. But [x-06] printed p. 12 states verbatim that (Tors) is a known requirement of any admissible global condition, so the E-free reading is not a legitimate S4 target; and the degenerate points D uses are not periodic, so they are not in any packet in the sense of [x-03] Thm 6.1.

**Notes on scope, stated in the verdict so they cannot be lost.**

(a) The theorem is about X_0 as constructed in [x-03] and its E-subsystems, including the unitary one. It says nothing about the conjectural Arakelov-type compactification X̄_0 predicted at [x-03] printed p. 39, whose added fixed points are exactly the archimedean end that W detects as it drives to 0. That is the single residual escape and it is named precisely in §11.4. It is not a gap in the proof; it is a different target.
(b) The theorem is about quasi-compact Y. Locally compact or σ-compact Y is untouched (§10.2), and must be: for finite S the objects exist ([probe B §6.3], re-derived at §10.2).
(c) **Q-c** (adjudication §5, bookkeeping) is **already settled YES** by the Session-14 referee pass recorded in the adjudication's dated block and in probe B §7. This note re-derives the "⊆" half (packets are closed: §2.4 (P1)) and records that the "⊇" half is banked Theorem A, **not** a consequence of closedness. Nothing here is new about Q-c; the partial draft's claim that closedness alone gives equality is withdrawn.

---

## 1. Sources read this session, with printed-page anchors

All extractions were made fresh this session with `pdftotext -layout` into the session scratchpad; every quotation below was read verbatim in those extractions. In both PDFs the printed page number equals the PDF page number (verified by inspecting the running page numbers on pages 1–4 of [x-03]).

**[x-03]** C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`. Read verbatim this session:

| Item | Printed page | What was read (verbatim fragments) |
|---|---|---|
| §3 set-up; X̊(C); G- and N-actions | 22 | "Let X be the normalization of X_0 in K … κ(x) is an algebraic closure of κ(x_0)"; "We define X̊(C) to be the set of pairs (x, P^×) where x ∈ X and P^× : κ(x)^× → C^× is a homomorphism"; "(x,P^×)σ = (x^σ, P^× ∘ σ)"; "F_ν(x,P^×) = (x, P^× ∘ ( )^ν) for ν ∈ N" |
| Remark 3.4 | 23 | "If X_0 = spec R_0 is affine, X = spec R, we will identify the points (x,P^×) of X̊(C) with the multiplicative maps P : R → C satisfying: 1) P(0)=0, P(1)=1. 2) p := P^{-1}(0) is additively closed and hence a prime ideal. 3) We have a factorization P : R → R/p → C" |
| Colimit description; pr_X on X̌ | 24–25 | "X̌(C) = colim_{N_0} X̊(C) and X̌_0(C) = colim_{N_0} X̊_0(C)"; "X̌_0(C) = X̌(C)/G"; "We can write the points of X̌(C) in the form F_ν^{-1}P for some ν ∈ N_0 and P in X̊(C)"; "pr_X : X̌(C) → X by setting pr_X(F_ν^{-1}P) = pr_X(P)" |
| (Tors), (Image), Def. 4.1, Prop. 4.2, (30)/(31) | 27 | "(Tors) the group ker(χ)_tors = ker(χ|_{μ(κ)}) is finite and \|(ker χ)_tors\| ∈ N_0"; "(Image) Only if char κ > 0. If χ(κ^×) is torsion, then κ^× is torsion as well"; Def. 4.1 "A class E … is (N_0−)admissible if for any σ ∈ Aut κ resp. ν ∈ N_0 the character χ is in E if and only if χ∘σ resp. χ_ν = χ∘( )^ν is in E. **Moreover the characters in E should satisfy (Tors)**"; Prop. 4.2 ("It is foreward- and backward invariant under the N_0-action, i.e. for P ∈ X̊(C) we have P ∈ X̊(C)_E if and only if F_ν(P) ∈ X̊(C)_E"; "The monoid N_0 acts by injections"); and "**Both pr_X and pr_{X_0} above extend Q^{>0}_0-equivariantly to maps pr_X : X̌(C)_E → X and pr_{X_0} : X̌_0(C)_E → X_0. Here we let Q^{>0}_0 act trivially on X and X_0**" |
| Examples E_tors, E_max | 28 | "1) E_tors : (Tors) holds. 2) E_max : (Tors) and (Image) hold" |
| C_{x_0} = pr_0^{-1}(x_0); (32) | 31 | "The fibres of pr_{X_0} : X̌_0(C)_{E_tors} → X_0 are Q^{>0}_0-invariant"; "C_{x_0} = pr_0^{-1}(x_0)^{Q^{>0}_0} = ⋃_{ν ∈ N_0} F_ν^{-1} pr_0^{-1}(x_0) ⊂ X̌_0(C)_{E_tors}"; (32) "i_x : μ^{(p)}(K) = μ^{(p)}(O_{X,x}) ≅ κ(x)^×" |
| Fibre description; (34), (35), (38), (39) | 32–33 | "The fibre pr_0^{-1}(x_0) consists of the G-orbits of all pairs (x,P^×) where x is a point of X over x_0 and P^× : κ(x)^× → C^× satisfies (Tors). Since κ(x)^× is torsion this means that ker P^× = (ker P^×)_tors is finite hence cyclic and \|ker P^×\| ∈ N_0"; (34) "N x_0^Ẑ = Gal(κ(x)/κ(x_0)) ↪ Aut(κ(x)^×) = Ẑ^×_{(p)}"; (38)/(39) the Q^{>0}_0-bijection (Ẑ^×_{(p)}/N x_0^Ẑ) ×_{p^Z} Q^{>0}_0 ≅ C_{x_0}; "It follows that all points P_0 ∈ C_{x_0} have isotropy subgroup (Q^{>0}_0)_{P_0} = N x_0^Z"; "The set C_{x_0} fibres over the compact group Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p)^, and the fibres are the Q^{>0}_0-orbits in C_{x_0}" |
| (40)–(46): **the map ρ** | 33 | (41) "ρ : X̊(C)_{E_tors} → N_0, (x,P^×) ↦ \|(Ker P^×)_tors\|"; "For ν ∈ N_0 let ν_x be the prime-to-char κ(x) part of ν. If char κ(x) = 0 then ν_x = ν"; (42) "\|(Ker P^× ∘ ( )^ν)_tors\| = ν_x \|(Ker P^×)_tors\|"; (43) "ρ(F_ν(P)) = ν_x ρ(P) for ν ∈ N_0 and P ∈ X̊(C)_E"; (44) "ρ : X̌(C)_{p,E_tors} → Q^{>0}_0/p^Z"; (45) "ρ : X̌(C)_{Q,E_tors} → Q^{>0}_0"; (46) the Q^{>0}_0-equivariant surjection; "The map ρ factors over a map ρ_0 on X̌_0(C)_{E_tors}"; and the definitions X̌(C)_{p,E_tors} = pr_X^{-1}(X ⊗ F_p), X̌(C)_{Q,E_tors} = pr_X^{-1}(X ⊗ Q) |
| Prop. 5.1 (with proof); Thm. 5.2 | 34 | "ρ(Q̌) = ν_x^{-1}\|(ker P^×)_tors\| in Q^{>0}_0 resp. Q^{>0}_0/p^Z"; Thm. 5.2 "{P_0 ∈ X̌_0(C)_E \| (Q^{>0}_0)_{P_0} ≠ 1} = ⨿_{x_0} C^E_{x_0}"; "For any point P_0 ∈ C^E_{x_0} the isotropy group of P_0 is (Q^{>0}_0)_{P_0} = N x_0^Z"; "If e.g. E ⊃ E_f then C^E_{x_0} = C_{x_0}" |
| Remark after Thm. 5.5 (the role of (Tors)) | 37 | "(Tors) does force the points P_0 ∈ X̌_0(C)_E over characteristic zero points of X_0 to have trivial stabilizer (Q^{>0}_0)_{P_0} = 1" |
| §6 opening: suspension, flow, packets | 38 | "X_0 = X̌_0(C)_E ×_{Q^{>0}_0} R^{>0}. It is the quotient of X̌_0(C)_E × R^{>0} by the right Q^{>0}_0-action given by (P_0,u)q = (P_0 q, q^{-1}u) = (F_q(P_0), q^{-1}u)"; "The group R^{>0} acts on X_0 via the second factor: [P_0,u]·v = [P_0,uv]"; "φ^t([P_0,u]) = [P_0, ue^t]"; "Γ_{x_0} = C_{x_0} ×_{Q^{>0}_0} R^{>0} ⊂ X_0"; the R^{>0}-bijection (Ẑ^×_{(p)}/N x_0^Ẑ) ×_{p^Z/deg x_0} R^{>0}/N x_0^Z ≅ Γ_{x_0}; "Thus all R^{>0}-orbits in Γ_{x_0} are circles R^{>0}/N x_0^Z and Γ_{x_0} fibres over Ẑ^×_{(p)}/p^Ẑ … with fibres the R^{>0}-orbits"; "We set Γ^E_{x_0} = C^E_{x_0} ×_{Q^{>0}_0} R^{>0} where C^E_{x_0} = C_{x_0} ∩ X̌_0(C)_E" |
| Thm. 6.1 | 39 | "{x_0 ∈ X_0 \| (R^{>0})_{x_0} ≠ 1} = ⨿_{x_0} Γ^E_{x_0}. For any point x_0 ∈ Γ^E_{x_0} the isotropy group of x_0 is (R^{>0})_{x_0} = N x_0^Z"; "Any periodic orbit γ in X_0 is contained in Γ^E_{x_0} for a uniquely determined point x_0 of X_0 with finite residue field" |
| The compactification remark | 39–40 | "X_0 should have a 'compactification' X̄_0 corresponding to an Arakelov compactification X̄_0 of X_0. The fixed points of the R-action on X̄_0 should be the set X_0(C)/F_∞"; "for z ∈ X_0(C) ∖ X_0(R) there are two orbits tending to the fixed point [z,0], namely [z,±1]u for u → 0+" |
| The S4 question | 40 | "The system X_0 may have to be replaced by a much smaller system: Is there a sub-dynamical system Y_0 ⊂ X_0 = X̌_0(C) ×_{Q^{>0}} R^{>0} or at least one which maps to X_0 such that dim Y_0 = 2d+1 where d = dim X_0 and such that Y_0 contains at least one periodic orbit in Γ_{x_0} for every closed point x_0 of X_0? If d = 1, is there such a Y_0 which is a Riemann surface lamination in the sense of [Ghy99]?" |
| §7 opening; Lemma 7.1 | 40 | "Viewing X̊(C) as a set of multiplicative maps P : R → C as in Remark 3.4 we give X̊(C) the topology of pointwise convergence. It is the subspace topology induced by the Tychonov topology of C^R = ∏_R C on X̊(C) via the inclusion X̊(C) ⊂ C^R, P ↦ (P(r))_{r ∈ R}. Since R is countable, X̊(C) is a metrizable topological space"; Lemma 7.1 (pr_X continuous, with proof) |
| Lemma 7.3; quotient topology on X̊_0(C) | 42 | "We equip X̊_0(C) = X̊(C)/G with the quotient topology. Using Lemma 7.1 one sees that pr_X : X̊(C) → X and hence also pr_{X_0} : X̊_0(C) → X_0 are continuous"; Lemma 7.3 "the group G acts by homeomorphisms on X̊(C) and the injective maps F_ν : X̊(C) ↪ X̊(C) for ν ∈ N are continuous, closed and open"; (51) "F_ν(X̊(C)) = {P ∈ X̊(C) \| P(μ_ν(K)) = 1}" |
| Colimit topology (53); Prop. 7.4; openness of π̌; continuity of pr | 43 | "We give X̌(C) = colim_{N_0} X̊(C) the inductive limit topology … Thus Z ⊂ X̌(C) is closed, resp. open if and only if F_ν(Z) ∩ X̊(C) is closed, resp. open in X̊(C) for all ν ∈ N_0"; Prop. 7.4 "a) X̊(C) is a closed and open subspace of X̌(C). b) F_q : X̌(C) → X̌(C) is a homeomorphism for every q ∈ Q^{>0}_0. c) The group G acts by homeomorphisms on X̌(C)"; "The projections π, π̌ are continuous and since G acts by homeomorphisms, also **open**. Moreover the projections pr_X : X̌(C) → X and pr_{X_0} : X̌_0(C) → X_0 are continuous" |
| Cor. 7.8, Cor. 7.9 | 45 | "The topological space X̊_0(C) is metrizable and separable and in particular Hausdorff"; "the spaces X̊(C), X̊_0(C), X̌(C) and X̌_0(C) are Hausdorff" |
| Thm. 7.10 and Remark 2) | 46–47 | the R^{>0}-equivariant **continuous bijections** from ⨿ of the "in"-strata onto X resp. X_0; "The continuous bijections in Theorem 7.10 are **not homeomorphisms in general**" |
| E-subspace topologies | 47 | "Given an admissible class E … we equip X̊(C)_E and X̊_0(C)_E with the subspace topologies"; "We give X̌(C)_E = colim_{N_0} X̊(C)_E and X̌_0(C)_E = colim_{N_0} X̊_0(C)_E the inductive limit topologies. They agree with the subspace topologies via X̌(C)_E ⊂ X̌(C) and X̌_0(C)_E ⊂ X̌_0(C) **because the subspaces F_ν^{-1}X̊(C) and F_ν^{-1}X̊_0(C) are open in X̌(C) resp. X̌_0(C) for all ν ∈ N_0**"; "the natural continuous bijection X̌(C)_E/G → X̌_0(C)_E is a homeomorphism. All preceding results in this section remain true if we replace X̊(C) etc. by X̊(C)_E etc." |
| (56)–(61): the r-map | 47–48 | "Ẑ ≅ Ĥ, a ↦ (ζ ↦ ι(ζ)^a)"; "The N-action by exponentiation of characters is just the action by multiplication on the abelian group Ĥ"; (58) "A_f = Ẑ ⊗ Q ≅ Ȟ"; (59) "r : X̊(C) → Ĥ, (x,P^×) ↦ (P^×|_{μ(κ(x))}) ∘ i_x is continuous … since r(P) = P|_{μ(K)} for P ∈ X̊(C)"; (60)/(61) "r : X̌(C) → Ȟ", "r : X̌(C) → A_f = Ẑ ⊗ Q", G- and Q^{>0}-equivariant |
| (65)–(68) | 48–49 | (65) "τ : Ȟ_{E_tors} → spec Z, sending Q^{>0}Ẑ^× to (0) and Q^{>0}(Ẑ^×_{(p)} × 0) to (p), is continuous"; the continuous "ρ : X̌(C)_E → Q^{>0} ⊔̇ ⊔̇_p Q^{>0}/p^Z … carries the quotient topology of Ȟ_{E_tors} or equivalently the subspace topology of A_f/Ẑ^×. For E = E_tors this is the same map as in (46)"; (67) the commuting square with pr_X and τ; (68) "X̃ = X̌(C)_E × R^{>0} → Ȟ_{E_tors} × R^{>0} = A^{>0} ⊔̇ ⊔̇_p A^{>0}_{(p)} ⊂ A"; "The Q^{>0}-action on Ȟ_{E_tors} × R^{>0} is **not properly discontinuous**. In section 10, we will see that this works to our advantage" |
| §8 opening; Y_0; Claim 8.1 | 49 | "the dynamical system X_0 = X̌_0(C) ×_{Q^{>0}} R^{>0} is infinite dimensional, whereas we are searching for a system of dimension 2 dim X_0 + 1, e.g. 3 in the case of X_0 = spec Z"; "In this section we will show that the system Y_0 is still infinite-dimensional: Namely, for one-dimensional X_0, flat over spec Z and conditionally for all X_0 we have Y_0 = X̌_0(S^1) ×_{Q^{>0}} R^{>0}"; Claim 8.1; "If spec A is a non-empty open subscheme of spec o_κ for some number field κ, then the set M in Claim 8.1 is always infinite … This follows from [Per11, Theorem 1]" |
| X̊(C)_per; Thm. 8.2; Lemma 8.3 | 50 | "X̊(C)_per = {(x,P^×) ∈ X̊(C) \| κ(x) ≅ F̄_p for some p and ker P^× is finite}"; Thm. 8.2 "X̌(C)_per = X̌(S^1) and X̌_0(C)_per = X̌_0(S^1)"; in the proof: "Any character of the torsion group F̄_p^× takes values in the roots of unity. Hence X̊(C)_per ⊂ X̊(S^1) … Since X̊(S^1) is closed in X̊(C) the subspace X̌(S^1) is closed in X̌(C) as well"; Lemma 8.3 (approximation of a unitary character by finite-kernel characters of finite residue fields) |
| Intro | 2 | "Each periodic orbit of X_0 lies in exactly one packet Γ_{x_0}. … The compact packets Γ_{x_0} are reminiscient of invariant tori. There are no fixed points of the flow." |

**[x-06]** C. Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf` (17 pages; printed = PDF page). Read verbatim:

| Item | Page | What was read |
|---|---|---|
| §4, construction of X_0 | 11 | "Set X_0 = (X̌_0(C) × R^{>0})/Q^{>0} where Q^{>0} acts diagonally. Let t ∈ R act on X_0 by setting φ^t[P,u] = [P, e^t u]"; and — **decisive for scope** — "**What we know for certain is that the restrictions of P^× to μ(κ(x)) must have finite kernels (condition E_tors)** and that for char κ(x) > 0 the image of P^× must not be torsion unless κ(x)^× is itself torsion" |
| Thm. 4.2 and its commentary | 11–12 | "{x_0 ∈ X_0^E \| φ^t(x_0) = x_0 for some t > 0} = ⨿_{x_0} Γ_{x_0}"; "The **compact** subsets Γ_{x_0} ⊂ X_0 consist of periodic orbits of length log N x_0 … and they are pairwise disjoint. In fact Γ_{x_0} is a fibre space over the compact group Aut(F̄_p)/Aut(F_p)^ … with fibres the compact orbits in Γ_{x_0}" |
| The closure of the compact orbits | 12 | "The space X_0^E is infinite dimensional if dim X_0 ≥ 1 and one could hope that the sub-dynamical system obtained as the closure of the union of all its compact orbits might be significantly smaller. However, this is not the case as follows from [Den22a, Theorem 8.2]. **The closure is the subsystem obtained by replacing X̊(C)_E in the previous constructions with the subspace of pairs (x,P^×) with P^× : κ(x)^× → S^1 a unitary character.**" |

**Program-internal (read in full this session, not re-derived here except where stated):** `results/c3-r/probe-9.3-adjudication.md` (binding; §2 verified anchors, §4 banked theorems including the dated Session-14 referee block, §5 Q*), `results/c3-r/probe-9.3-b.md` §§6–7 (the mapping face; the dated Q-c referee block), `results/c3-r/probe-9.3-a.md` §6 (G2), `results/c3-r/probe-9.4-note.md` §8 (DQ-M, Roads), `results/c3-r/m2c-feasibility-ledger.md` §8 (Route 2, S1–S5).

**Read but NOT cited for anything load-bearing:** [r3s-08] Morishita, arXiv:2508.15971 — per adjudication §4 item 4 the program must not cite it for topology, and nothing below does. Nothing in this note uses [r3s-08], [ALKL], [ÁLKL23], [ALKM], Leichtnam, or [D25]. **Nothing in this note uses [r3s-08]'s "homeomorphism" wording, and nothing uses Theorem 7.10's bijections as homeomorphisms** ([x-03] p. 47 states in terms they are not).

---

## 2. The objects, written out

Throughout: **X_0 = spec Z**, K_0 = Q, K = Q̄, **R = Z̄** (the ring of algebraic integers = the normalization of Z in Q̄), X = spec Z̄, G = Aut(Q̄/Q), **C = ℂ**, **N_0 = N**, Q^{>0}_0 = Q^{>0}. Everything in §2 is transcription from the anchors of §1; nothing here is new.

**2.1 Points.** X̊(C) is the set of pairs (x, P^×) with x ∈ X and P^× : κ(x)^× → C^× a character ([x-03] p. 22); equivalently (Remark 3.4, p. 23) the set of multiplicative maps P : Z̄ → C with P(0) = 0, P(1) = 1, whose zero set p_P := P^{-1}(0) is a prime ideal, P factoring through Z̄/p_P. Since X = spec Z̄ has Krull dimension 1 (Z̄ is integral over Z), x is either the **generic point** η (κ(η) = Q̄, p_η = (0)) or a **closed point** lying over a rational prime p, in which case κ(x) is an algebraic closure of F_p, i.e. κ(x) = F̄_p ([x-03] p. 22: "κ(x) is an algebraic closure of κ(x_0)"). We write

  **char(P) := char κ(x_P) ∈ {0} ∪ {primes},**

and note pr_X(P) = x_P, p_P ∩ Z = (char P) when char P > 0 and = (0) when char P = 0.

The topology on X̊(C) is that of **pointwise convergence on Z̄**, the subspace topology from the Tychonov topology of C^{Z̄} ([x-03] §7, p. 40, verbatim). Two consequences used constantly:

* **(T1) Evaluation is continuous.** For each r ∈ Z̄ the map ev_r : X̊(C) → C, P ↦ P(r), is continuous. (Definition of the product topology.)
* **(T2) Values at units are roots of unity when char P > 0.** If char P = p > 0 and r ∈ Z̄ ∖ p_P, then P(r) = P^×(r̄) with r̄ ∈ κ(x_P)^× = F̄_p^×, a **torsion** group; hence P(r) is a root of unity and |P(r)| = 1. Likewise, for any P and any root of unity ζ ∈ μ(Q̄) ⊂ Z̄^×, P(ζ) is a root of unity of order dividing ord(ζ) — indeed P(ζ)P(ζ^{-1}) = P(1) = 1 forces P(ζ) ≠ 0, and P(ζ)^{ord ζ} = P(ζ^{ord ζ}) = 1.

**2.2 Admissible classes.** E is admissible ([x-03] Def. 4.1, p. 27) iff for all σ ∈ Aut κ and ν ∈ N_0, χ ∈ E ⟺ χ∘σ ∈ E ⟺ χ^ν = χ∘( )^ν ∈ E, **and every χ ∈ E satisfies (Tors)**: ker(χ)_tors = ker(χ|_{μ(κ)}) is finite with |(ker χ)_tors| ∈ N_0. Three consequences used below:

* **(A1) (Tors) is not optional.** It is part of the definition of admissibility, so **every** E-system carries the finiteness that the weight of §5 measures. In particular the theorem below needs no hypothesis on E beyond admissibility, and covers the "cut" classes E(a_0) of probe A's Theorem C(b) and every class in the certified window E ⊇ E_f.
* **(A2) Over spec Z, (Image) is vacuous, so every admissible E satisfies E ⊆ E_max.** (Image) is imposed only when char κ > 0, where it reads "if χ(κ^×) is torsion then κ^× is torsion as well"; at the closed points of X = spec Z̄ the residue field is F̄_p, whose multiplicative group *is* torsion, so the conclusion always holds. Hence **Thm. 5.2 and Thm. 6.1 (whose hypothesis is "E admissible with E ⊂ E_max") apply to every admissible E over spec Z.**
* **(A3) Bi-invariance.** P ∈ X̊(C)_E ⟺ F_ν(P) ∈ X̊(C)_E (Prop. 4.2, p. 27). So the E-locus is F-saturated in both directions, and X̌(C)_E = colim_{N_0} X̊(C)_E with the **subspace** topology of X̌(C) (p. 47, verbatim).

**2.3 Colimit and suspension.** X̌(C) = colim_{N_0} X̊(C) along the injections F_ν(P) = P∘( )^ν, with the inductive-limit topology (p. 43); X̊(C) is open and closed in X̌(C) and each F_q, q ∈ Q^{>0}, is a homeomorphism of X̌(C) (Prop. 7.4, p. 43); each stratum F_ν^{-1}X̊(C) is open in X̌(C) (p. 47, verbatim); every point of X̌(C) has the form F_ν^{-1}P with P ∈ X̊(C), ν ∈ N_0 (p. 24, verbatim). X̌_0(C) = X̌(C)/G with the quotient topology; the projection **π̌ : X̌(C) → X̌_0(C) is continuous and open** (p. 43, verbatim), and the same holds for the E-versions (p. 47: "All preceding results in this section remain true if we replace X̊(C) etc. by X̊(C)_E etc."). Finally

  **X_0 = X̌_0(C)_E ×_{Q^{>0}} R^{>0} = (X̌_0(C)_E × R^{>0}) / Q^{>0},  (P_0,u)·q = (F_q(P_0), q^{-1}u),**

with the quotient topology, and φ^t[P_0,u] = [P_0, ue^t] ([x-03] §6, p. 38, verbatim). Write

  **Q : X̌_0(C)_E × R^{>0} ⟶ X_0**

for the quotient map. It is continuous and **open**: for O open, Q^{-1}(Q(O)) = ⋃_{q ∈ Q^{>0}} O·q is a union of images of O under homeomorphisms of X̌_0(C)_E × R^{>0}, hence open, hence Q(O) is open. (That each q acts by a homeomorphism is Prop. 7.4b plus the homeomorphism u ↦ q^{-1}u.)

**2.4 Packets and the base map.** Since pr_{X_0} : X̌_0(C)_E → X_0 is **continuous** (p. 43) and **Q^{>0}-equivariant for the trivial action on X_0** (p. 27, verbatim), the composite X̌_0(C)_E × R^{>0} → X_0, (P_0,u) ↦ pr_{X_0}(P_0), is constant on Q^{>0}-orbits and therefore descends along the quotient map Q to a continuous, **flow-invariant** map

  **Π : X_0 ⟶ X_0 = spec Z.**

(Continuity: Q is a quotient map, and Π∘Q is continuous. Flow-invariance: the flow moves only the R^{>0}-coordinate.) Write

  **X_0^{(p)} := Π^{-1}((p))  and  X_0^{(0)} := Π^{-1}((0))**

for the fibres over the closed point (p) and over the generic point. Then:

* **(P1) X_0^{(p)} = Γ^E_p, and it is closed.** By p. 31 the fibre pr_{X_0}^{-1}((p)) in X̌_0(C)_{E_tors} is already Q^{>0}-invariant, so C_{(p)} = pr_{X_0}^{-1}((p)) and C^E_{(p)} = pr_{X_0}^{-1}((p)) ∩ X̌_0(C)_E is the full fibre of pr_{X_0} : X̌_0(C)_E → X_0 over (p) (using E ⊆ E_tors, admissibility). Hence Γ^E_p := Γ^E_{(p)} = C^E_{(p)} ×_{Q^{>0}} R^{>0} = Π^{-1}((p)). Since {(p)} is closed in spec Z and Π is continuous, **Γ^E_p is closed in X_0**. (This is the referee-discharged Prop. A.1′ of the Session-14 pass, re-derived; it is *not* new.) Distinct packets are fibres over distinct points, hence **pairwise disjoint** — as [x-06] Thm. 4.2 (p. 12) also states.
* **(P2) X_0 = X_0^{(0)} ⊔ ⨆_p Γ^E_p.** Immediate from (P1) and dim spec Z = 1. We call X_0^{(0)} the **characteristic-zero locus**. It is flow-invariant.
* **(P3) (Thm. 5.2 p. 34, Thm. 6.1 p. 39, with (A2).)** The points of X_0 with non-trivial R^{>0}-isotropy are exactly ⨆_p Γ^E_p, and every point of Γ^E_p has isotropy p^Z, i.e. **lies on a circle of length log p**. In particular **the flow on X_0^{(0)} is free**: no point of the characteristic-zero locus is periodic. (Equivalently, [x-03] p. 37 verbatim: "(Tors) does force the points P_0 ∈ X̌_0(C)_E over characteristic zero points of X_0 to have trivial stabilizer".)

**2.5 The unitary system.** X̊(S^1) ⊂ X̊(C) is the subspace of (x,P^×) with P^× valued in S^1; it is closed in X̊(C) ([x-03] p. 50, verbatim). Deninger's Y_0 = the topological closure of the union of all periodic orbits equals X̌_0(S^1) ×_{Q^{>0}} R^{>0} (Thm. 8.2, p. 50; unconditional for X_0 = spec Z via [Per11, Theorem 1], p. 49 verbatim), and — [x-06] p. 12, verbatim — it "is the subsystem obtained by replacing X̊(C)_E in the previous constructions with the subspace of pairs (x,P^×) with P^× : κ(x)^× → S^1 a unitary character". Taken inside X_0 = X̌_0(C)_E ×_{Q^{>0}} R^{>0} for an admissible E — which is how Route 2 uses it, and the only reading in which the packet theory of §2.4 is available — **Y_0 is a closed flow-invariant subspace of X_0**, and everything below applies to it verbatim. (§10.1 treats the literal E-free reading and shows exactly what changes.)

**2.6 The statement of Q-b** (adjudication §5). *Does a compact metrizable 3-dimensional lamination (Y, F, φ) with exactly one closed orbit γ_p of length log p per prime admit a continuous flow-equivariant map f : Y → X_0 (or to the unitary system X̌_0(S^1) ×_{Q^{>0}} R^{>0}) with f(γ_p) ⊂ Γ_p?*

---

## 3. Three rigidity lemmas in X̊(C)

Everything the proof needs about the topology of X̊(C) is contained in three statements, each proved from (T1), (T2) and the definitions of §2.1. Nets are used throughout; no metrizability, first countability, Hausdorffness or properness is invoked anywhere in this note.

**Notation.** For P ∈ X̊(C) put

  **ρ̂(P) := | ker( P^×|_{μ(κ(x_P))} ) | ∈ N ∪ {∞}  if char P = 0,  ρ̂(P) := +∞  if char P > 0.**

For char P = 0 we have κ(x_P) = Q̄ and μ(Q̄) = μ_∞, and, identifying μ_∞ with Q/Z, every subgroup of μ_∞ is of the form ⊕_ℓ μ_{ℓ^{n_ℓ}} with n_ℓ ∈ N ∪ {∞}; such a subgroup is finite iff all n_ℓ are finite and almost all vanish, in which case it equals μ_M with M = ∏_ℓ ℓ^{n_ℓ}. Hence

  **(3.0)  ρ̂(P) = sup { N ∈ N : μ_N(Q̄) ⊆ ker P^× }  ∈ N ∪ {∞}   (char P = 0),**

the sup being attained when finite. When char P = 0 and P satisfies (Tors), ρ̂(P) = |(ker P^×)_tors| = **ρ(P)**, Deninger's map (41) of [x-03] p. 33. (For char P > 0 our ρ̂ deliberately **differs** from Deninger's ρ: his is finite there, ours is +∞. §5.1 explains why.)

**Lemma 3.1 (root-of-unity rigidity).** Let (P_i) be a net in X̊(C) with P_i → P, and let N ∈ N be such that P(ζ) = 1 for all ζ ∈ μ_N(Q̄). Then there is i_0 with P_i(ζ) = 1 for all ζ ∈ μ_N(Q̄) and all i ≥ i_0.

*Proof.* Fix ζ ∈ μ_N(Q̄). By (T2), P_i(ζ) ∈ μ_{ord ζ}(C) ⊆ μ_N(C), a **finite** subset of C. By (T1), P_i(ζ) → P(ζ) = 1. A net in a finite subset of a Hausdorff space converging to one of its points is eventually equal to that point (take the neighborhood of 1 that excludes the other, finitely many, values). So P_i(ζ) = 1 eventually. As μ_N(Q̄) is finite, one i_0 serves all ζ ∈ μ_N(Q̄) simultaneously. ∎

**Lemma 3.2 (p-adic inflation at a positive-characteristic limit).** Let (P_i) be a net in X̊(C) with P_i → P and char P = p > 0. Then for every k ≥ 1 there is i_0 such that P_i(ζ) = 1 for all ζ ∈ μ_{p^k}(Q̄) and all i ≥ i_0. Consequently, if char P_i = 0 then ρ̂(P_i) ≥ p^k for i ≥ i_0.

*Proof.* Let ζ ∈ μ_{p^k}(Q̄). Then ζ ∈ Z̄^× (its inverse ζ^{-1} = ζ^{p^k−1} is an algebraic integer), so ζ ∉ p_P and P(ζ) = P^×(ζ̄) with ζ̄ ∈ κ(x_P)^× ⊆ F̄_p^×. Now ζ̄^{p^k} = 1 in a field of characteristic p forces (ζ̄ − 1)^{p^k} = ζ̄^{p^k} − 1 = 0, hence ζ̄ = 1, hence **P(ζ) = 1**. Apply Lemma 3.1 with N = p^k. The consequence is (3.0): μ_{p^k} ⊆ ker P_i^× gives ρ̂(P_i) ≥ p^k. ∎

**Lemma 3.3 (lower semicontinuity of ρ̂).** ρ̂ : X̊(C) → [1, ∞] is lower semicontinuous: for every real M the set {ρ̂ > M} is open. Equivalently, P_i → P implies lim inf_i ρ̂(P_i) ≥ ρ̂(P).

*Proof.* Let P_i → P and let M < ρ̂(P) be real; we show ρ̂(P_i) > M eventually.

*Case char P = 0.* By (3.0) choose an integer N with M < N ≤ ρ̂(P) and μ_N ⊆ ker P^×, i.e. P(ζ) = 1 for ζ ∈ μ_N. By Lemma 3.1, eventually P_i(ζ) = 1 for all ζ ∈ μ_N. For such i: if char P_i = 0 then μ_N ⊆ ker P_i^×, so ρ̂(P_i) ≥ N > M by (3.0); if char P_i > 0 then ρ̂(P_i) = ∞ > M by definition.

*Case char P = p > 0.* Then ρ̂(P) = ∞. Choose k with p^k > M. By Lemma 3.2, eventually P_i(ζ) = 1 on μ_{p^k}; for such i, ρ̂(P_i) ≥ p^k > M if char P_i = 0, and ρ̂(P_i) = ∞ otherwise. ∎

**Remark 3.4 (ρ̂ is *not* continuous, and this is essential).** On the characteristic-zero locus ρ̂ can jump up in the limit. Indeed if P_i → P with all characteristics 0 and P(ζ) ≠ 1 for some ζ ∈ μ_∞, then by (T1)+(T2) P_i(ζ) ≠ 1 eventually; so for each fixed N, ker P_i^× ∩ μ_N = ker P^× ∩ μ_N eventually. But the *total* kernel may still blow up: if ρ̂(P) = m and ρ̂(P_i) = m·ℓ_i with distinct primes ℓ_i → ∞, then for each fixed N the intersections agree eventually while ρ̂(P_i) → ∞. This is exactly the "adelic" phenomenon behind [x-03] (66)–(67): valuations stabilize on finite sets of primes, the module does not. Lower semicontinuity is therefore the *sharp* statement, and — see §5.4 — it is also exactly the amount of regularity the argument consumes.

**Lemma 3.5 (modulus-one rigidity: no escape from positive characteristic to positive characteristic).** Let (P_i)_{i ∈ I} be a net in X̊(C) with char P_i = p_i > 0, and suppose the characteristics are **unbounded along the net**: for every bound B there is i_0 with p_i > B for i ≥ i_0. If P_i → P in X̊(C), then **char P = 0**.

*Proof.* Suppose char P = q > 0. The rational prime q, viewed as an element of Z̄, satisfies q ∈ p_P (because p_P ∩ Z = (q)), so **P(q) = 0**. On the other hand, for i with p_i > q we have q ∉ p_{P_i}: otherwise q ∈ p_{P_i} ∩ Z = (p_i), so p_i | q, so p_i = q, contradiction. Hence by (T2) **|P_i(q)| = 1** for all such i. By (T1), P_i(q) → P(q) = 0, contradicting |P_i(q)| = 1. ∎

**Remark 3.6.** Lemma 3.5 says nothing about *which* characteristic-zero points arise as such limits; §9.2 records what is known (they are unitary, by [x-03] Thm. 8.2's mechanism, re-derived there). The Main Theorem does not need that refinement — only the dichotomy.

---

## 4. Uniformization of X_0 by open maps, and lifting of nets

The three lemmas of §3 live in X̊(C). X_0 is two quotients and a colimit away. The following two lemmas transport them, and they are the only "topology bookkeeping" in the note. Both are elementary; neither uses Hausdorffness (which fails for X_0, adjudication §4 item 3).

**Lemma 4.1 (net lifting through an open map).** Let g : Z → W be continuous, open and surjective onto an **open** subset g(Z) ⊆ W′, let (w_i)_{i ∈ I} be a net in W′ with w_i → w ∈ g(Z), and let z ∈ Z with g(z) = w. Then there are a subnet (w_{i(j)})_{j ∈ J} and points z_j ∈ Z with g(z_j) = w_{i(j)} and z_j → z.

*Proof.* Since g(Z) is open and w ∈ g(Z), we may discard an initial segment and assume w_i ∈ g(Z) for all i. Let 𝒱 be the neighborhood filter of z in Z, directed by reverse inclusion. Put

  J := { (i, V) ∈ I × 𝒱 : w_i ∈ g(V) },  (i,V) ≤ (i′,V′) :⟺ i ≤ i′ and V ⊇ V′.

J is directed: given (i,V), (i′,V′) ∈ J, set V″ = V ∩ V′; g(V″) is an open neighborhood of w (g open, z ∈ V″), so w_{i″} ∈ g(V″) for all i″ beyond some index, and we may take i″ ≥ i, i′; then (i″,V″) ∈ J dominates both. The map J → I, (i,V) ↦ i, is monotone and cofinal (for any i_1 ∈ I, g(Z) ∋ w so w_i ∈ g(Z) for all i, and picking any V and any i ≥ i_1 with w_i ∈ g(V) gives (i,V) ∈ J above (i_1, ·)); hence (w_{i(j)})_{j ∈ J} is a subnet of (w_i). For j = (i,V) choose z_j ∈ V with g(z_j) = w_i. Then z_j → z: given V_0 ∈ 𝒱, for all j = (i,V) ≥ (i_0, V_0) (any admissible i_0) we have z_j ∈ V ⊆ V_0. ∎

**Lemma 4.2 (the charts R_ν).** For ν ∈ N_0 define

  **R_ν : X̊(C)_E × R^{>0} ⟶ X_0,  R_ν(P, u) := [ π̌(F_ν^{-1}P), u ] = Q( π̌(F_ν^{-1}P), u ).**

Then: (a) each R_ν is continuous and **open**, with **open** image; (b) ⋃_{ν ∈ N_0} R_ν(X̊(C)_E × R^{>0}) = X_0; (c) Π(R_ν(P,u)) = the image in spec Z of pr_X(P) — in particular **R_ν(P,u) ∈ Γ^E_p ⟺ char P = p, and R_ν(P,u) ∈ X_0^{(0)} ⟺ char P = 0.**

*Proof.* (a) Write R_ν = Q ∘ (π̌ × id) ∘ (j_ν × id) with j_ν := (F_ν|_{X̊(C)_E})^{-1}. By Prop. 7.4b (p. 43) F_ν is a homeomorphism of X̌(C), and it restricts to a homeomorphism of X̌(C)_E by (A3); it carries F_ν^{-1}X̊(C)_E bijectively onto X̊(C)_E, so j_ν : X̊(C)_E → F_ν^{-1}X̊(C)_E is a homeomorphism onto a subset that is **open** in X̌(C)_E (p. 47, verbatim: "the subspaces F_ν^{-1}X̊(C) … are open in X̌(C)", intersected with the E-locus, whose topology is the subspace topology, p. 47). Hence j_ν is continuous, open and has open image. π̌ is continuous and open (p. 43, and p. 47 for the E-version), and Q is continuous and open (§2.3). A composite of continuous open maps is continuous and open, and the image of an open set under an open map is open, so R_ν has open image.
(b) Every point of X̌(C)_E is F_ν^{-1}P for some ν ∈ N_0 and P ∈ X̊(C) (p. 24, verbatim), and then P = F_ν(F_ν^{-1}P) ∈ X̊(C)_E by (A3); π̌ and Q are surjective.
(c) pr_X(F_ν^{-1}P) = pr_X(P) (p. 25, verbatim), pr_{X_0} ∘ π̌ = (X → X_0) ∘ pr_X, and Π ∘ Q = pr_{X_0} ∘ (first projection) by construction (§2.4). Then use (P1)/(P2). ∎

**Remark 4.3.** Lemma 4.2 is the substitute for a "chart" structure on X_0: the R_ν form an open cover of X_0 by continuous open images of the metrizable space X̊(C)_E × R^{>0}. Every statement below is checked on the charts and pushed forward. Note that R_ν is *not* injective and its image is *not* Hausdorff; neither is needed.

**Corollary 4.4 (semicontinuity descends along the charts).** Let F : X_0 → [−∞, ∞] be a function such that F ∘ R_ν is lower semicontinuous on X̊(C)_E × R^{>0} for every ν ∈ N_0. Then F is lower semicontinuous on X_0.

*Proof.* For a ∈ R, {F > a} = ⋃_ν ( {F > a} ∩ R_ν(·) ) and {F > a} ∩ R_ν(X̊(C)_E × R^{>0}) = R_ν( {F ∘ R_ν > a} ), an open set by Lemma 4.2(a). A union of open sets is open. ∎

---

## 5. The escape function: a positive l.s.c. conformal weight of exponent one

### 5.1 Definition

Extend ρ̂ from X̊(C) to X̌(C) by

  **ρ̂(F_ν^{-1}P) := ν^{-1} ρ̂(P)  (P ∈ X̊(C), ν ∈ N_0),**

with the conventions ν^{-1}·∞ = ∞ and q·∞ = ∞ for q ∈ Q^{>0}.

**Lemma 5.1.** (i) ρ̂ is well defined on X̌(C). (ii) ρ̂(F_q(P̌)) = q · ρ̂(P̌) for all q ∈ Q^{>0} and P̌ ∈ X̌(C). (iii) ρ̂ is G-invariant, hence descends to ρ̂_0 on X̌_0(C). (iv) ρ̂(P̌) = ∞ if and only if either char P̌ > 0, or char P̌ = 0 and P̌^×'s restriction to μ has infinite kernel; under (Tors) — i.e. on X̌(C)_E for E admissible — the second alternative is empty, so **{ρ̂_0 = ∞} = pr_{X_0}^{-1}({closed points})**. (v) On the characteristic-zero part of X̌(C)_{E_tors}, ρ̂ coincides with Deninger's ρ of [x-03] (41)/(45).

*Proof.* (i) If F_ν^{-1}P = F_{ν′}^{-1}P′ then F_{ν′}P = F_ν P′ in X̊(C). If char P = 0 then char P′ = 0 (the characteristic is F-invariant, p. 22: F_ν(x,P^×) = (x, P^×∘( )^ν)); (42)/(43) of [x-03] p. 33 with ν_x = ν give ν′ ρ̂(P) = ν ρ̂(P′) when the values are finite, so ν^{-1}ρ̂(P) = ν′^{-1}ρ̂(P′). When ρ̂(P) = ∞ we must check ρ̂(P′) = ∞: by (51) of [x-03] p. 42, F_{ν′}P = F_ν P′ means P∘( )^{ν′} = P′∘( )^{ν}; a root of unity ζ lies in ker(F_{ν′}P)^× iff ζ^{ν′} ∈ ker P^×, and the map μ_∞ → μ_∞, ζ ↦ ζ^{ν′}, is surjective with finite fibres, so ker(F_{ν′}P)^× ∩ μ_∞ is infinite iff ker P^× ∩ μ_∞ is; the same for the other side. If char P > 0 both sides are ∞ by definition. (ii) For q = ν/ν′ this is (i) together with (43) (char 0) and the convention (char > 0). (iii) ker((P^×∘σ)|_μ) = σ^{-1}(ker(P^×|_μ)) has the same cardinality, and σ preserves the characteristic. (iv) is (3.0) and Def. 4.1. (v) is (41)/(45) of p. 33 read off. ∎

**Definition 5.2 (the weight).** Define **W : X_0 → (0, ∞]** by

  **W([P_0, u]) := ρ̂_0(P_0) · u.**

This is well defined: by Lemma 5.1(ii), W((P_0,u)·q) = ρ̂_0(F_q P_0)·q^{-1}u = q·ρ̂_0(P_0)·q^{-1}u = W([P_0,u]).

**Remark 5.3 (what W is, adelically).** Under Deninger's identifications ([x-03] (56)–(61), pp. 47–48, verbatim), r : X̌(C) → A_f is continuous, G- and Q^{>0}-equivariant with r(P) = P|_{μ(K)} on the chart X̊(C), and for a ∈ Ẑ the module ‖a‖ = ∏_ℓ |a_ℓ|_ℓ equals 1/ρ̂. So

  **W([P_0,u]) = u / ‖ r(P_0) ‖,**

the ratio of the archimedean suspension coordinate to the finite-adelic module. That the Q^{>0}-action multiplies the module by q^{-1} while multiplying u by q^{-1} in the opposite factor is exactly why W is Q^{>0}-invariant, and is the content of the "diagonal" in [x-03] (68). We do **not** use this formulation in any proof — every step below is carried out with the elementary ρ̂ of §3, so that no property of the topology on A_f/Ẑ^× has to be verified — but it is the right way to see what the weight is, and it is precisely the instrument probe B §7 named ("the r-map … is the natural instrument … any kill via r must use dynamics, not dimension"). The dynamics is Theorem 5.5.

**Why ρ̂ = ∞ over positive characteristic.** Deninger's ρ takes the *finite* value ν_x^{-1}|ker P^×| ∈ Q^{>0}/p^Z there ([x-03] (44), p. 33) — but only modulo p^Z, so ρ·u is well defined on Γ^E_p just as a point of the **circle** R^{>0}/p^Z, not as a positive real. Setting ρ̂ = ∞ over positive characteristic is the unique choice that (a) keeps W well defined and R-conformal on all of X_0, and (b) makes W lower semicontinuous (Theorem 5.4: the packets are approached from characteristic zero only with ρ → ∞). It is not a truncation or a convention of convenience: Lemma 3.2 says the value ∞ is *forced* by semicontinuity.

### 5.2 The two structural properties

**Theorem 5.4 (the weight).** For every arithmetic scheme in the sense of [x-03] §7 with X_0 = spec Z and every admissible class E, the function W : X_0 → (0, ∞] of Definition 5.2 satisfies:

1. **Positivity:** W > 0 everywhere.
2. **Conformality of exponent one:** W(φ^t z) = e^t W(z) for all t ∈ R, z ∈ X_0 (with e^t·∞ = ∞).
3. **Lower semicontinuity:** {W > a} is open in X_0 for every a ∈ R.
4. **Finiteness locus:** {W < ∞} = X_0^{(0)}, the characteristic-zero locus. (Here and only here admissibility, i.e. (Tors), is used.)

*Proof.* 1. and 2.: immediate from Definition 5.2 (ρ̂_0 ≥ 1 > 0 and φ^t[P_0,u] = [P_0, ue^t]). 4.: Lemma 5.1(iv) together with (P1)/(P2).

3.: By Corollary 4.4 it suffices to prove that W ∘ R_ν is l.s.c. on X̊(C)_E × R^{>0} for each ν. By construction

  **W(R_ν(P,u)) = ρ̂(F_ν^{-1}P) · u = ν^{-1} · ρ̂(P) · u.**

Now ρ̂ : X̊(C)_E → [1,∞] is l.s.c. (Lemma 3.3, restricted to the subspace X̊(C)_E — restriction of an l.s.c. function to a subspace is l.s.c.), (P,u) ↦ u is continuous and strictly positive, and ν^{-1} > 0 is a constant. A product of a [0,∞]-valued l.s.c. function with a continuous strictly positive function is l.s.c.: if f_i → f in the l.s.c. sense and g_i → g > 0 continuously, then lim inf f_i g_i ≥ (lim inf f_i)(lim g_i) ≥ f g, with the convention ∞·(positive) = ∞. Hence W ∘ R_ν is l.s.c. ∎

**Theorem 5.5 (dissipation).** Let K ⊆ X_0 be **nonempty, quasi-compact and flow-invariant** (in the subspace topology; no Hausdorffness, metrizability or closedness assumed). Then **W ≡ ∞ on K**; equivalently, by Theorem 5.4(4),

  **K ⊆ ⨆_p Γ^E_p:  K contains no characteristic-zero point of X_0.**

*Proof.* W|_K is l.s.c. on K (restriction) and strictly positive. Two steps.

*Step 1: an l.s.c. function on a nonempty quasi-compact space attains its infimum.* Let m := inf_K W ∈ [0, ∞]. If m is not attained then for every z ∈ K there is a real a > m with W(z) > a, so the open sets U_a := {W > a} ∩ K, a > m real, cover K. Quasi-compactness gives a finite subcover, i.e. K ⊆ U_{a_0} for a_0 := max of the finitely many a's (the U_a decrease in a), whence m = inf_K W ≥ a_0 > m — a contradiction. So m = W(z_0) for some z_0 ∈ K, and **m > 0** because W > 0 everywhere (including the value ∞).

*Step 2.* Suppose some z ∈ K has W(z) < ∞. Since K is flow-invariant, φ^{-t}z ∈ K for all t > 0, and by Theorem 5.4(2), W(φ^{-t}z) = e^{-t}W(z) → 0 as t → +∞. Hence m = inf_K W = 0, contradicting m > 0. Therefore W ≡ ∞ on K. ∎

**Remark 5.6 (the mechanism in words).** The characteristic-zero locus of X_0 is *uniformly dissipative*: it carries a positive weight that the flow rescales by e^t and that is lower semicontinuous, hence bounded away from 0 on any quasi-compact piece. Backward time destroys any such bound. Equivalently, in the coordinates of Remark 5.3: a point of characteristic zero has a finite adelic module, and the R^{>0}-coordinate of the suspension is measured against it; flowing backwards shrinks that ratio to zero, which is the archimedean end of [x-03] p. 40 ("two orbits tending to the fixed point [z,0] … for u → 0+"). What Theorem 5.5 shows is that **the escape to the archimedean end cannot be caught by compactness**: the would-be limit is not in X_0 at all, it is in the conjectural X̄_0.

**Remark 5.7 (immediate sanity checks).** (i) Γ^E_p is compact ([x-06] p. 12) and invariant, and indeed W ≡ ∞ on it. (ii) X_0 itself is **not** quasi-compact: it contains characteristic-zero points (for E ⊇ E_f, by Cor. 4.4 of [x-03] p. 28 prX_0 is surjective), so Theorem 5.5 would be contradicted. This is consistent with, and independent of, Deninger's infinite-dimensionality statements. (iii) The *closure* of a quasi-compact invariant set need not be quasi-compact, and indeed cl(γ) = Γ^E_p (Theorem A) is compact while cl(⨆_p Γ^E_p) = Y_0 is not (§8.2).

---

## 6. Packet separation at infinity

**Theorem 6.1.** Let (z_i)_{i ∈ I} be a net in X_0 with z_i ∈ Γ^E_{p_i} for primes p_i, and assume the p_i are **unbounded along the net** (for every B there is i_0 with p_i > B for i ≥ i_0). If z_i → z in X_0, then **z ∈ X_0^{(0)}**: the limit lies over the generic point of spec Z. Equivalently, **no point of any packet is a limit of packet points of unboundedly growing characteristic.**

*Proof.* Suppose z ∈ Γ^E_q for a prime q. By Lemma 4.2(b) choose ν and (P, u) ∈ X̊(C)_E × R^{>0} with R_ν(P,u) = z; by Lemma 4.2(c), char P = q. The image of R_ν is open (Lemma 4.2(a)) and contains z, so after discarding an initial segment we may assume all z_i lie in it. By Lemma 4.1 applied to g = R_ν there are a subnet (z_{i(j)}) and points (P_j, u_j) ∈ X̊(C)_E × R^{>0} with

  R_ν(P_j, u_j) = z_{i(j)} and (P_j, u_j) → (P, u).

By Lemma 4.2(c), char P_j = p_{i(j)}. A subnet is cofinal, so the characteristics p_{i(j)} are unbounded along j. Hence P_j → P in X̊(C)_E ⊆ X̊(C) with unbounded positive characteristics and char P = q > 0 — contradicting Lemma 3.5. ∎

**Remark 6.2.** Theorem 6.1 is where the arithmetic enters most cheaply: the rational prime q is a *global* element of Z̄ which is invisible (value 0) to every character over characteristic q and unimodular (value a root of unity) to every character over any other positive characteristic. Note that the statement is false without the growth hypothesis — a net inside a single Γ^E_p converges inside it, and by Theorem A its orbits are even dense there.

**Remark 6.3 (what fails at bounded characteristic, and why it does not matter).** If the p_i take a fixed value p infinitely often, the limit may of course lie in Γ^E_p. The Main Theorem only ever applies Theorem 6.1 to nets with genuinely unbounded characteristic, obtained from an infinite set S of primes directed by magnitude.

---

## 7. The Main Theorem

### 7.1 Statement and proof

**Theorem 7.1 (Main Theorem).** Let X_0 = spec Z, C = ℂ, N_0 = N, let E be **any** admissible class of characters ([x-03] Def. 4.1), and let X_0 = X̌_0(C)_E ×_{Q^{>0}} R^{>0} with the flow φ^t[P_0,u] = [P_0, ue^t]. Let (Y, φ) be a nonempty **quasi-compact** topological space with a continuous R-action, and let f : Y → X_0 be continuous and flow-equivariant. Then

  **S := { p prime : f(Y) ∩ Γ^E_p ≠ ∅ } is finite,  f(Y) ⊆ ⨆_{p ∈ S} Γ^E_p,**

and Y = ⨆_{p ∈ S} f^{-1}(Γ^E_p) is a partition of Y into finitely many **clopen, flow-invariant** subsets. In particular f(Y) ∩ X_0^{(0)} = ∅ and S ≠ ∅.

*Proof.* Put K := f(Y). It is nonempty, quasi-compact (continuous image of a quasi-compact space) and flow-invariant (φ^t(K) = φ^t(f(Y)) = f(φ^t(Y)) = f(Y) = K, by equivariance and invariance of Y).

*(1) No characteristic-zero point.* Theorem 5.5 gives W ≡ ∞ on K, so by Theorem 5.4(4), K ⊆ ⨆_p Γ^E_p and K ∩ X_0^{(0)} = ∅. Since K ≠ ∅ and the packets partition X_0 ∖ X_0^{(0)}, S ≠ ∅.

*(2) S is finite.* Suppose S is infinite. Direct S by magnitude (p ≤ p′), a directed set. For each p ∈ S choose z_p ∈ K ∩ Γ^E_p and y_p ∈ f^{-1}(z_p). The net (y_p)_{p ∈ S} lies in the quasi-compact space Y, hence has a convergent subnet y_{p_j} → y ∈ Y (a space is quasi-compact iff every net has a convergent subnet; no separation axiom is needed for this direction). By continuity f(y_{p_j}) → f(y), i.e. z_{p_j} → f(y) in X_0, with z_{p_j} ∈ Γ^E_{p_j}. A subnet of a net indexed by the directed set S is cofinal, so the primes p_j are unbounded along j. Theorem 6.1 now gives f(y) ∈ X_0^{(0)} — contradicting step (1), since f(y) ∈ K. Hence S is finite.

*(3) The partition.* By (1) and (2), Y = ⋃_{p ∈ S} f^{-1}(Γ^E_p), and the sets f^{-1}(Γ^E_p), p ∈ S, are pairwise disjoint (the packets are, by (P1)), closed (packets are closed by (P1), f continuous) and flow-invariant (packets are, f equivariant). A finite cover of a space by pairwise disjoint closed sets is a cover by clopen sets: the complement of each member is the union of the finitely many others, hence closed. ∎

### 7.2 What the proof used, and what it did not

**Used:** the topology of pointwise convergence on X̊(C) ([x-03] p. 40); openness of π̌ and of the Frobenius homeomorphisms F_ν, and openness of the strata F_ν^{-1}X̊(C) (pp. 42, 43, 47); continuity and Q^{>0}-equivariance of pr_{X_0} (pp. 27, 43); Deninger's ρ-identity (43) (p. 33); (Tors) from Def. 4.1 (p. 27); the definition of the suspension and its flow (p. 38). Nothing else. In particular:

**Not used:** Theorem A (packet closure) — although the result is consistent with it and §8.5 records the interaction; the non-Hausdorffness of X_0; Theorem 5.2/6.1's isotropy classification (used only to *interpret* the result, §8.1 and §9, never in the proof); Theorem 8.2 and Claim 8.1 (hence the result is **unconditional** and does not depend on [Per11] or on any Diophantine input); the model bijections (38)/(39) and Theorem 7.10 (which [x-03] p. 47 warns are not homeomorphisms); dimension theory, mean dimension, entropy, minimal-set structure theory, holonomy, transverse measures, metrizability, and any property of laminations.

**Robustness.** The theorem is stated for X_0 = spec Z because that is Route 2's target and because Lemma 3.5 uses the rational prime q ∈ Z̄. The same proof runs verbatim for any arithmetic scheme X_0 in the sense of [x-03] §7 that is **flat of finite type over spec Z**, replacing "the rational prime q" by "any element of Γ(X_0, O) that lies in the prime corresponding to the limit point but in no prime of unboundedly large residue characteristic" — for spec o_k the rational prime below q serves. We do not develop this; it is not needed and it is flagged as **not verified** in §11.

---

## 8. Consequences

### 8.1 Q-b: NO

**Corollary 8.1.** Let (Y, F, φ) be a compact metrizable 3-dimensional lamination whose flow has exactly one closed orbit γ_p of length log p for each prime p (and whatever further S3/α = 1 structure the ledger's S4 demands). Then there is **no** continuous flow-equivariant map f : Y → X_0 = X̌_0(C)_E ×_{Q^{>0}} R^{>0} with f(γ_p) ⊂ Γ^E_p for all p, for any admissible class E.

*Proof.* Y is nonempty (it contains γ_2), compact and flow-invariant, and such an f would give f(Y) ∩ Γ^E_p ⊇ f(γ_p) ≠ ∅ for every prime p, i.e. S = {all primes}, contradicting the finiteness of S in Theorem 7.1. ∎

**The hypotheses that were not used.** "3-dimensional", "lamination", "foliated flow", "metrizable", "exactly one orbit per prime", the ε ≡ +1 sign data, the leafwise conformal structure, the transverse measure — none appears. What is used is: Y nonempty quasi-compact, φ continuous, f continuous and equivariant, and f meeting infinitely many packets. So Corollary 8.1 kills a much wider class of candidate substrates than Q-b names, and it is insensitive to every parameter the ledger's S4 row can be tuned in.

**Where the *specific* hypothesis f(γ_p) ⊂ Γ_p enters.** Only to make S infinite. Any weaker demand that still forces infinitely many packets to be met — for instance "f(Y) contains at least one periodic orbit of length log p for every p", which is literally Deninger's condition at [x-03] p. 40 ("such that Y_0 contains at least one periodic orbit in Γ_{x_0} for every closed point x_0") since by Thm. 6.1 every periodic orbit of X_0 lies in a unique packet — kills equally. This is recorded as Corollary 8.4 below.

### 8.2 The unitary system, and its non-compactness

**Corollary 8.2.** Let Y_0 ⊆ X_0 be the closure of the union of all periodic orbits, i.e. Deninger's X̌_0(S^1)-system ([x-03] §8 p. 49 and Thm. 8.2 p. 50; [x-06] p. 12), regarded as a flow-invariant subspace of X_0 = X̌_0(C)_E ×_{Q^{>0}} R^{>0}. Then Corollary 8.1 holds verbatim with X_0 replaced by Y_0. Moreover **Y_0 is not quasi-compact.**

*Proof.* The inclusion ι : Y_0 ↪ X_0 is continuous and flow-equivariant, so ι ∘ f is continuous and equivariant whenever f is, and (ι∘f)(γ_p) = f(γ_p) ⊂ Γ^E_p; apply Theorem 7.1. For the last claim: Y_0 is nonempty and flow-invariant and Y_0 ⊇ Γ^E_p for every p (each packet consists of periodic orbits, Thm. 6.1); if Y_0 were quasi-compact, Theorem 7.1 applied to Y = Y_0, f = ι would force S finite, contradiction. ∎

**Remark 8.3.** Corollary 8.2's last sentence is a new, sharp complement to [x-03] §8. Deninger's §8 result is that Y_0 is *still infinite-dimensional* — a dimension statement, conditional in general on Claim 8.1 and unconditional for spec Z via [Per11]. The statement here is that Y_0 is not even quasi-compact, and it is **unconditional and independent of Claim 8.1** (it uses only Theorems 5.5 and 6.1 above, whose inputs are §7 of [x-03] and Def. 4.1). Two distinct reasons why the "closure of the periodic orbits" cannot be the sought substrate; the compactness reason is the one Route 2 actually needs, since ALKL's hypothesis H1 and the [Ghy99] lamination notion both demand compactness before dimension is even asked.

### 8.3 Q-a: NO

**Corollary 8.4.** Let K ⊆ X_0 be a nonempty **quasi-compact** flow-invariant subspace. Then K meets only finitely many packets; in particular:

(a) There is **no** compact flow-invariant subspace of X_0 meeting each packet in exactly one orbit — with or without the hypotheses "Hausdorff in its subspace topology" and "topological dimension 3". **Q-a is answered NO.**
(b) There is no compact flow-invariant subspace of X_0 containing at least one periodic orbit of length log p for every prime p. **Hence the *first* alternative of Deninger's question at [x-03] p. 40 is dead for compact Y_0 by a second, independent route** (the first being banked Corollary B / Theorem B via Theorem A, adjudication §4 item 2). Note the two routes kill different things: Theorem A kills *closed* subsystems, this kills *quasi-compact* ones, and in a non-Hausdorff space neither class contains the other.

*Proof.* Apply Theorem 7.1 to Y = K with the restricted flow (continuous, and K is invariant) and f the inclusion. ∎

### 8.4 S4, and hence Route 2

Per adjudication §5: "A YES on either face permanently retires the packet-mechanism kill …; **a NO on both kills S4 and with it Route 2, firing the kill-criterion input.**" Corollary 8.1 answers Q-b NO and Corollary 8.4(a) answers Q-a NO. Both faces are therefore closed in the negative, **for every admissible class E, unconditionally, with no dimension, Hausdorffness or metrizability hypothesis on the candidate substrate**. Consequently:

> **S4 is dead.** There is no compact object — subspace or continuous equivariant source — realizing "one closed orbit of length log p per prime, sitting over Deninger's packets". Both alternatives of [x-03] p. 40 are answered NO under compactness. Route 2's chain S1–S5 breaks at S4, its unique open existence step; S1 (published), S2 (TRANSFERS-WITH-WORK), S3, S5 are untouched as *instrument* results but have no arithmetic object to act on along this route.

The kill is *not* a dimension obstruction, *not* an orbit-multiplicity obstruction, *not* a monodromy obstruction, and *not* a packet obstruction. It is a **conformal-weight/dissipation** obstruction: the closed orbits must accumulate as p → ∞ (compactness), the accumulation must land over the generic point (Theorem 6.1), and over the generic point the flow admits a positive l.s.c. weight it rescales by e^t, which no quasi-compact invariant set can support (Theorem 5.5). Informally: **X_0's characteristic-zero locus is entirely "escaping to the archimedean end", and compactness cannot catch it because the end is not in X_0.**

### 8.5 Q-c and the interaction with Theorem A (bookkeeping only, nothing new)

Q-c asks whether cl_{X_0}(γ) = Γ^E_p for a periodic orbit γ ⊂ Γ^E_p. It is **already settled YES** in this program: the "⊇" half is banked **Theorem A** (three independent derivations, adjudication §2 and §4 item 1) and the "⊆" half was discharged at referee grade in the Session-14 pass recorded in the adjudication's dated block and probe B §7 — precisely by the observation re-derived here as (P1): Γ^E_p is the fibre over (p) of the continuous flow-invariant map Π : X_0 → spec Z. Nothing in this note adds to Q-c. **The partial draft's claim that closedness alone yields the equality is withdrawn**: closedness gives only "⊆", and the reverse inclusion is a genuine theorem about profinite Frobenius-return accumulation, not a formal consequence.

Consistency of the present results with Theorem A is worth recording, since the two pull in opposite directions:

* Theorem A says packets are minimal and every periodic orbit is dense in its packet. Theorem 7.1 says a quasi-compact invariant set meets finitely many packets. Both hold: Γ^E_p is itself compact ([x-06] p. 12) and meets exactly one packet.
* Theorem A applies to *closed* invariant sets, Theorem 7.1 to *quasi-compact* invariant sets. In the non-Hausdorff X_0 (adjudication §4 item 3) these classes are incomparable, which is exactly why probe B §6.1 correctly concluded that Theorem A exerts no force through a continuous equivariant map — and why a *different* mechanism was needed. Theorem 5.5 is that mechanism, and it is compactness-driven rather than closure-driven, so the non-Hausdorff escape that defeated the packet argument does not touch it.
* **Corollary 8.5 (classification of the compact minimal sets).** If M ⊆ X_0 is nonempty, compact, flow-invariant, **closed in X_0**, and minimal (no proper nonempty closed invariant subset), then M = Γ^E_p for a single prime p. *Proof.* Theorem 7.1 gives M ⊆ ⨆_{p ∈ S} Γ^E_p with S finite; each M ∩ Γ^E_p is closed and invariant, so minimality forces M ⊆ Γ^E_{p_0} for one p_0. M contains an orbit γ, necessarily periodic (P3), and cl_{X_0}(γ) = Γ^E_{p_0} by Theorem A + (P1); as M is closed, Γ^E_{p_0} ⊆ M. ∎ Combined with Theorem 5.5: **the characteristic-zero locus of X_0 contains no nonempty quasi-compact invariant set whatsoever, hence no minimal set, no compact orbit closure, and no compactly supported invariant probability measure.**

---

## 9. The three charter lines, answered in full

The charter asked for three developments. All three are carried out; the first two are answered, and the answer to the first is *stronger and structurally different* from what the charter anticipated, which is why the anticipated route (equicontinuous factors, eigenvalues, mean dimension) is not merely unnecessary but inapplicable.

### 9.1 The structure of the unitary-locus flow

**(i) The action, written out.** On X̊(C) the monoid N acts by F_ν(x, P^×) = (x, P^× ∘ ( )^ν) ([x-03] p. 22, verbatim). Since P^×(y^ν) = P^×(y)^ν, this is precisely **raising the character to its ν-th power**, i.e. multiplication by ν in the abelian group Hom(κ(x)^×, C^×); restricted to roots of unity and transported by ι, it is literally multiplication by ν on Ẑ ≅ Ĥ = Hom(μ(K), μ(C)) ([x-03] p. 47, verbatim: "The N-action by exponentiation of characters is just the action by multiplication on the abelian group Ĥ"). Passing to the colimit turns this into the **Q^{>0}-action by multiplication** on Ȟ ≅ A_f ([x-03] (58), p. 48). For unitary characters (P^× valued in S^1) nothing changes: X̊(S^1) is F-stable and closed in X̊(C) ([x-03] p. 50).

The **R^{>0}-action does not act on characters at all.** By construction ([x-03] p. 38, verbatim) it acts only on the suspension coordinate,

  **[P_0, u]·v = [P_0, uv],  φ^t[P_0,u] = [P_0, u e^t],**

and the *only* reason the flow has non-trivial dynamics on characters is the identification [P_0, u] = [F_q P_0, q^{-1}u]. So: **the unitary locus flow is the suspension (mapping-torus-at-scale-Q^{>0}) of the multiplication action of Q^{>0} on the unitary character space**, mapped equivariantly and continuously into the Bost–Connes-type object A^{>0}/Q^{>0} by [x-03] (68) (p. 49, verbatim). Deninger records that this Q^{>0}-action is **not properly discontinuous** (p. 49, verbatim), which is why the suspension is non-Hausdorff (adjudication §4 item 3) and why no naive "compact group rotation" picture can hold.

**(ii) Orbit structure.** By Thm. 5.2/6.1 ([x-03] pp. 34, 39; applicable to every admissible E over spec Z by (A2)):
* over each closed point (p): every orbit is a **circle of length log p**; the packet Γ^E_p is the union of these, model-bijective to B_p × (R^{>0}/p^Z) with B_p = Ẑ^×_{(p)}/p^Ẑ an uncountable compact group (banked; [x-03] p. 38 for the bijection, adjudication §2 for the uncountability);
* over the generic point: the isotropy is trivial ([x-03] p. 37, verbatim), so **every orbit is a free, injectively parametrized copy of R**; there are no periodic orbits and no fixed points at all ([x-03] intro p. 2, verbatim: "There are no fixed points of the flow").

**(iii) Minimal sets — the answer, and why the charter's route is void.** The charter asked whether the unitary flow is equicontinuous / a rotation on a compact group / torus-like, and proposed to constrain f|_A by "images of minimal sets are minimal sets", equicontinuous factors and eigenvalues. The correct answer is more drastic:

> **The characteristic-zero part of the unitary locus carries no nonempty quasi-compact invariant subset at all** (Theorem 5.5 + Theorem 5.4(4)). Hence it has **no minimal sets**, **no point with quasi-compact orbit closure**, **no compactly supported invariant measure**, and a fortiori **no compact equicontinuous factor and no non-trivial eigenvalue theory**: there is no compact invariant object to carry one. Its only compact minimal sets are the packets, and those are *not* in the characteristic-zero part (Corollary 8.5).

The charter's step "f restricted to A semi-conjugates the compact aperiodic flow (A, φ) into that action" therefore has no target: f(A) would be a nonempty quasi-compact invariant subset of the characteristic-zero locus, and there is none. The obstruction is not a mismatch of two dynamical structures; it is the non-existence of one of them. This also explains, in retrospect, why probe A §6.2's list of cheap kills (dimension, periodicity, rank) all failed: each tried to compare *structures* on the two sides, whereas the true obstruction is that the receiving side is empty.

**(iv) Is the flow equicontinuous?** No, and the question is ill-posed in the useful sense: X_0 is not Hausdorff and not compact, so "equicontinuous" has no uniform structure canonically attached. What can be said precisely is: **log W is a lower semicontinuous additive cocycle of the flow** on X_0^{(0)} (log W ∘ φ^t = log W + t), i.e. the characteristic-zero locus admits an l.s.c. "time function" strictly increasing along orbits with unit speed. Such a function is incompatible with recurrence of any kind on a quasi-compact set, and it is *not continuous* (Remark 3.4) — the failure of continuity is exactly the adelic phenomenon that lets the packets attach themselves to the characteristic-zero locus as limits.

### 9.2 The p → ∞ constraint and the limits of packet points

**(i) What the limits are.** Let (P_j) be a net in X̊(C) with char P_j = p_j positive and unbounded, and P_j → P. Then:

* **char P = 0** (Lemma 3.5). So limits of packet points at unbounded characteristic lie over the generic point of spec Z.
* **P is unitary**: |P(r)| = 1 for every r ∈ Z̄ ∖ {0}. *Proof.* Fix r ≠ 0 and let m := |N_{Q(r)/Q}(r)| ∈ N, m ≥ 1. If r ∈ p_{P_j}, then N(r) ∈ p_{P_j} ∩ Z = (p_j), so p_j | m; since m ≠ 0 this happens for finitely many values of p_j, hence for j beyond some index (unboundedness) r ∉ p_{P_j} and |P_j(r)| = 1 by (T2). By (T1), P(r) = lim P_j(r) has modulus 1. ∎
  This is the inclusion half of [x-03] Thm. 8.2 ("X̌(C)_per ⊂ X̌(S^1)", p. 50), re-derived here directly; Deninger's own argument for that half is the same observation ("Any character of the torsion group F̄_p^× takes values in the roots of unity … Since X̊(S^1) is closed in X̊(C)…", p. 50, verbatim). The converse half — that *every* unitary point is such a limit — is Deninger's Lemma 8.3 (p. 50) with Claim 8.1, **unconditional for X_0 = spec Z, flat over spec Z, via [Per11, Theorem 1]** (p. 49, verbatim). So the answer to the charter's question "which characters arise as limits" is: **exactly the unitary ones**, and that is [x-03] Thm. 8.2, which the present note does not need but does confirm on the easy side.
* **No constraint survives on ρ̂.** By Lemma 3.3 and the convention ρ̂ = ∞ over positive characteristic, l.s.c. gives no information at such a limit; and indeed under (Tors) the limit has finite ρ̂ while all the approximants have ρ̂ = ∞ in our normalization. This is not a defect: the semicontinuity is used only in the *other* direction (Lemma 3.2: approaching a packet from characteristic zero forces ρ → ∞).

**(ii) The constraint on f, and the charter's dimension question.** Suppose Y is compact with closed orbits γ_p of length log p for all p and f is continuous equivariant with f(γ_p) ⊂ Γ^E_p. Let

  **A := ⋂_{N ≥ 1} cl_Y( ⋃_{p ≥ N} γ_p )**

be the accumulation set of the closed orbits. Then A is **nonempty** (a decreasing net of nonempty closed subsets of a compact space has nonempty intersection — the finite intersection property), **closed**, **flow-invariant**, and every point of A is a limit of points of γ_{p_k} with p_k → ∞. By continuity and Theorem 6.1, **f(A) ⊆ X_0^{(0)}**. But f(A) is nonempty, quasi-compact and flow-invariant, so Theorem 5.5 forbids it. This is the Main Theorem again, in the form the charter posed it, and it answers the charter's question

> "whether continuity of f forces A's image to be a set that no 3-dimensional compact lamination's aperiodic part can map onto equivariantly (dimension/mean-dimension/entropy or minimal-set-complexity obstruction)"

with: **stronger — no compact flow, of any dimension, mean dimension or entropy, maps into that locus at all, because the locus contains no nonempty compact invariant set.** No invariant of Y is compared with any invariant of X_0 anywhere in the proof. Consistently with probe A §6.2 and probe B §7, dimension arguments are indeed unavailable (continuous maps raise dimension); the kill uses dynamics only, exactly as probe B predicted it would have to.

**(iii) Aperiodicity of A is not needed.** The charter (and probe B §6.4) expected A to consist of non-periodic points. It does — if y ∈ A had period T then f(y) would be a periodic point, hence in some packet by Thm. 6.1, contradicting f(A) ⊆ X_0^{(0)}; alternatively, in Y the lengths log p → ∞ prevent period stabilization only under extra hypotheses, which we do not need. The proof of Theorem 7.1 never uses aperiodicity of A: it uses only that *some* limit point exists.

### 9.3 The local structure at a closed orbit, and what f does to a transversal

**(i) The packet, as a model.** For x_0 = (p) in spec Z one has N x_0 = p and deg x_0 = 1, so [x-03] p. 38 (verbatim) gives the R^{>0}-equivariant **bijection**

  **B_p × ( R^{>0} / p^Z )  ≅  Γ_{(p)},  B_p := Ẑ^×_{(p)} / p^Ẑ = Aut(F̄_p)/Aut(F_p)^,**

with the flow acting by rotation on the second factor and **trivially on B_p**; the fibres of Γ_{(p)} → B_p are exactly the R^{>0}-orbits ([x-03] p. 38 and p. 33, verbatim; [x-06] p. 12, verbatim). B_p is an uncountable compact group (banked; adjudication §2). So in the *model*, the transversal to a closed orbit inside the packet is the totally disconnected B_p and the first-return map on it is the **identity**: the packet direction is fixed by the flow. This is the precise sense of the charter's "in X_0 the packet Γ_p has base B_p and the flow fixes the base", and it is the reason both probes rejected the ledger's fibre-flow-minimality and fibration-monodromy sketches (adjudication §2).

**(ii) The warning, which the charter's phrasing invites one to forget.** That decomposition is a **bijection, not a homeomorphism**. [x-03] p. 47 states verbatim that the analogous continuous bijections of Theorem 7.10 "are not homeomorphisms in general"; the subspace topology on Γ^E_p is **non-Hausdorff** and, by **Theorem A**, *every* orbit is dense in Γ^E_p — so Γ^E_p is a minimal set and its subspace topology is emphatically not (profinite) × (circle) (adjudication §4 items 3 and 4, binding; the program must not cite [r3s-08]'s "homeomorphism" wording for topology). Consequently there is **no honest transversal return map at a closed orbit of X_0 in the subspace topology of the packet**, and no local return-dynamics comparison can be set up on the X_0 side. This is a second, independent reason why the charter's line (3) cannot produce an obstruction: the object one would compare against does not exist as a product.

**(iii) What f does to γ_p.** Let γ ⊂ Y be a closed orbit of length log p and f(γ) ⊂ Γ^E_p. Parametrize γ = R/(log p)Z by the flow. Equivariance forces f(γ) to be a single R-orbit of X_0 (the image of an orbit is an orbit), lying in Γ^E_p, hence by Thm. 6.1 periodic with isotropy exactly (log p)Z. The induced map R/(log p)Z → f(γ) is therefore a continuous equivariant **bijection**. Whether it is a homeomorphism onto its image is *undetermined by the present tools*, because the subspace topology on a single orbit of Γ^E_p is delicate (by Theorem A its closure is the whole packet, and adjudication §4 item 3 records that no periodic orbit is closed as a subset). We record this as **not decided** and flag that nothing below depends on it: the Main Theorem uses only that f(γ_p) meets Γ^E_p.

**(iv) What f does to a 2-dimensional transversal in Y.** Let τ ⊂ Y be a 2-dimensional transversal at a point y ∈ γ_p with first-return map h : τ ⊇ τ′ → τ. Equivariance gives no commuting square with any "return map on the X_0 side", precisely by (ii). What *is* forced: f(τ) is a compact-in-Y-image subset of X_0 meeting Γ^E_p, and by Theorem 7.1 applied to the invariant saturation ⋃_t φ^t(cl τ) — if that saturation is compact and invariant, which it need not be — one gets finiteness of the packets it meets. We do **not** use this: no transversal argument is needed, and none is claimed. **Conclusion of line (3): the local structure at a closed orbit imposes no obstruction, and cannot, for the two structural reasons in (ii). The obstruction is global and is the accumulation p → ∞.**
