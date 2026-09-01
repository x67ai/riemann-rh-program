# REFEREE REPORT — probe A, Theorem B(b): the n-cell construction and the infinite-dimensionality conclusion

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Session 14.**
**Date:** 2026-09-02. **Referee:** referee **O** (one of two independent referees on this item; the second referee is a different model and nothing below was softened in expectation of their pass).
**Item under review:** `results/c3-r/probe-9.3-a.md` §3, **Theorem B(b)** — the n-cell construction and the infinite-dimensionality conclusion — together with the parts of Theorem B(a), Corollary (i)/(ii) and scope notes (i)–(iii) on which (b) depends.
**Debt discharged:** adjudication `results/c3-r/probe-9.3-adjudication.md` §4 item 6 ("Checked at proof-sketch level against the sources, not line-by-line: probe A's Theorem B(b) cell construction … Before any external circulation, Theorem B(b) and Cor. A.1 owe a dedicated referee pass").
**Standing orders honored:** SO5 (nothing load-bearing from memory; every source claim below is quoted verbatim from the on-disk PDF at a stated printed page, and classical inputs that are *not* on disk are labeled **[RU]** and carry no weight); SO7 (the novelty/priority question is answered here on its own evidence).

---

## 0. VERDICT BLOCK (stated first)

**VERDICT: PASS-WITH-REPAIRS.**

The mathematical core of Theorem B(b) **re-derives correctly, line by line**, from the on-disk primary sources. Every step the adjudication flagged as unchecked — the splitting `Q̄^× = μ(Q̄) × V`, the Q-linear independence of the V-components of distinct rational primes, the definition and well-definedness of the unitary characters `Ψ_t`, their satisfaction of (Tors) and (Image) and hence membership in the `E_max`-locus, the appeal to [x-03] Thm 8.2 including its unconditional status for `Spec Z`, continuity of `Θ` **in the actual colimit/quotient/suspension topology**, injectivity of `Θ`, the compact-to-Hausdorff step and the dimension-monotonicity step — checks out, with the qualifications listed below. I could not break any of them.

But the theorem **as stated and as used** must change, for four reasons of substance and seven of detail:

| # | Sev. | One line |
|---|---|---|
| **J1** | **MAJOR** | (b)'s first sentence asserts *unconditionally* that `S` contains a homeomorphic copy of the n-cube; the proof establishes only a **continuous injection** `[0,½]^n → S`, upgraded to an embedding **only** under the Hausdorff hypothesis stated in the second sentence. |
| **J2** | **MAJOR** | Post-adjudication (G1 = NO), the hypothesis "`S` … whose subspace topology is Hausdorff" is **unsatisfiable**: by (a), `S` contains a full packet, and a packet's subspace topology is non-Hausdorff. So (b) is **vacuously true**, and Corollary (ii)'s "by (b)" must be re-routed: its conclusion follows from **(a) + non-Hausdorffness alone**, with no cells and no dimension theory. |
| **J3** | **MAJOR** (priority, SO7) | The *conclusion* of (b) for the closure system `Y₀` is asserted in print by Deninger **twice, without proof** ([x-03] p. 49 and p. 5; [x-06] p. 12). The note's blanket novelty claim for "Theorem B" must be qualified: what is new is a **proof**, plus the extension from `Y₀` to arbitrary closed invariant subsets meeting every packet (that extension is Theorem A's contribution). |
| **J4** | **MAJOR** (cross-cutting; addressed to the adjudicator) | Adjudication §4 item 2 certifies probe B's **Corollary B** "outright" on the ground that "every input published and verified on disk". One of its inputs — the `§8` "still infinite-dimensional" line — is an **unproved assertion in the source**, not a theorem. Probe A's B(b), once repaired as **(b1)** below, is exactly the missing proof. Contrary to §4 item 6 ("nothing in the adjudicated verdicts rests on them"), B(b) *is* load-bearing for the dimension clause of the banked closed-half kill. |
| M1–M7 | MINOR | dimension monotonicity needs *normality*, not merely Hausdorffness; citation for the colimit-stratum embedding; "§8 operates in `E_max`"; page range for the `E`-examples; scope note (i) understated; (Tors) quoted without its `∈ N₀` clause; the classical dimension inputs are **[RU]** (no dimension-theory source on disk). |

**Fatals 0 · Majors 4 · Minors 7.**

Replacement text for every repair is in **§7**. The one-paragraph statement of what is now established at referee grade, and its exact scope, is **§9**.

---

## 1. The text under review, quoted exactly

From `results/c3-r/probe-9.3-a.md` §3:

> **Theorem B.** Let X₀ = Spec Z and E_f ⊆ E ⊆ E_max … Let S ⊆ X₀ be closed and flow-invariant, and suppose that for every prime p, S contains at least one periodic orbit of Γ_{(p)}. Then:
> **(a)** S contains **every** periodic orbit of every packet — in particular, for each p, uncountably many pairwise distinct closed orbits of primitive length log p (parametrized by the Cantor group B_p).
> **(b)** If moreover E = E_max (equivalently E_tors over Spec Z, §1.2), then S contains, for every n ≥ 1, a homeomorphic copy of the n-cube. Hence every closed invariant S as above **whose subspace topology is Hausdorff** (in particular: every candidate compact metrizable lamination) has covering dimension ≥ n for all n, i.e. is infinite-dimensional.

and its Corollary (ii):

> (ii) For E = E_max (= the system in which [x-03] §8 operates) and for the unitary system Y₀^Den = X̌₀(S¹) ×_{Q>0} R>0 … there is in addition **no** compact finite-dimensional (in any dimension, in particular 3) lamination Y₀ ⊆ X₀, closed and flow-invariant, containing at least one periodic orbit in Γ_{(p)} for every p, by (b). The first alternative of Deninger's question ([x-03] §6 p. 40) has answer **NO**.

The proof of (b) is reproduced in full in §4 below, step by step, as I re-derive it.

---

## 2. Source anchors — every one read on disk this session, quoted verbatim with its printed page

The file is `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` (119 pp.). **Printed page = PDF page** throughout (verified by reading the page footers at pp. 26, 27, 28: the footers print `26`, `27`, `28` on those PDF pages). Extraction: `pdftotext -layout`, fresh this session.

**A2.1 — (Tors), (Image) [p. 27].**
> "(Tors) the group ker(χ)_tors = ker(χ |_{µ(κ)}) is finite and |(ker χ)_tors| ∈ N₀.
> (Image) Only if char κ > 0. If χ(κ^×) is torsion, then κ^× is torsion as well, i.e. κ^× ⊗ Q ≠ 0 implies χ(κ^×) ⊗ Q ≠ 0."

**A2.2 — Definition 4.1 [p. 27].**
> "Definition 4.1. A class E of characters χ : κ^× → C^× on algebraically closed fields κ is (N₀−)admissible if for any σ ∈ Autκ resp. ν ∈ N₀ the character χ is in E if and only if χ ◦ σ resp. χ^ν = χ ◦ ( )^ν is in E. Moreover the characters in E should satisfy (Tors)."

**A2.3 — Proposition 4.2 [p. 27], the sentence the note cites for the colimit.**
> "Proposition 4.2. Given an admissible class of characters E on the κ(x)^× for x ∈ X, the set X̊(C)_E = {(x, P^×) ∈ X̊(C) | P^× is in E} ⊂ X̊(C) is G-invariant. It is foreward- and backward invariant under the N₀-action, i.e. for P ∈ X̊(C) we have P ∈ X̊(C)_E if and only if F_ν(P) ∈ X̊(C)_E. … **The monoid N₀ acts by injections on X̊(C)_E and X̊₀(C)_E.**"

**A2.4 — the splitting Deninger himself uses [p. 28, proof of Lemma 4.3].**
> "The sequences 1 → µ(k) → k^× → k^×/µ(k) → 1 and 1 → µ(C) → C^× → C^×/µ(C) → 1 are both split since µ(k) and µ(C) are divisible. … Here k^×/µ(k) and C^×/µ(C) are uniquely divisible abelian groups and therefore Q-vector spaces."

**A2.5 — the examples of admissible classes [pp. 28–29].**
> "Example. 1) E_tors : (Tors) holds  2) E_max : (Tors) and (Image) hold" [p. 28]
> "3) E_f : (Tors) and ker χ is finite. Equivalently: | ker χ| ∈ N₀  4) E_fg : (Tors) and ker χ is finitely generated  5) E_fd : (Tors) and ker χ ⊗ Q is finite dimensional  6) E_fd0 : (Tors) and (ker χ |_{κ(x₀)^×}) ⊗ Q is finite dimensional where x₀ = π(x) … We have inclusions in the appropriate sense E_f ⊂ E_fg ⊂ E_fd ⊂ E_fd0 ⊂ E_max ⊂ E_tors." [p. 29]

**A2.6 — Remark 3.4 (points as multiplicative maps) and the G-action [p. 23].**
> "Remark 3.4. If X₀ = spec R₀ is affine, X = spec R, we will identify the points (x, P^×) of X̊(C) with the multiplicative maps P : R → C satisfying the following properties: 1) P(0) = 0, P(1) = 1. 2) p := P^{−1}(0) is additively closed and hence a prime ideal. 3) We have a factorization P : R → R/p → C. … Then we have P^σ = (p, P^×)^σ where P^σ = P ◦ σ."

**A2.7 — the topology upstairs [p. 40, §7 opening].**
> "We begin with the affine case X₀ = spec R₀ and write X = spec R. Viewing X̊(C) as a set of multiplicative maps P : R → C as in Remark 3.4 we give X̊(C) the topology of pointwise convergence. It is the subspace topology induced by the Tychonov topology of C^R = ∏_R C on X̊(C) via the inclusion X̊(C) ⊂ C^R, P ↦ (P(r))_{r∈R}. Since R is countable, X̊(C) is a metrizable topological space."

**A2.8 — `N₀` and the Frobenii [p. 42].**
> "Lemma 7.3. For any arithmetic scheme X₀, the group G acts by homeomorphisms on X̊(C) and the injective maps F_ν : X̊(C) ↪ X̊(C) for ν ∈ N are continuous, closed and open. In particular F_ν(X̊(C)) is closed and open in X̊(C)."
> "As usual let N₀ be the submonoid of N generated by a set of prime numbers char N₀ ⊃ char X₀ and let Q₀^{>0} be the subgroup of Q^{>0} generated by N₀."

**A2.9 — the colimit topology, and that the ν = 1 stratum is a clopen subspace [p. 43].** *(This is the anchor the referee brief asks for: the actual topology on X̌, not an assumed product topology.)*
> "We give X̌(C) = colim_{N₀} X̊(C) the inductive limit topology. It is the finest topology such that for all ν ∈ N₀ the inclusions F_ν^{−1}|_{X̊(C)} : X̊(C) ↪ X̌(C) (53) are continuous. Thus Z ⊂ X̌(C) is closed, resp. open if and only if F_ν(Z) ∩ X̊(C) is closed, resp. open in X̊(C) for all ν ∈ N₀."
> "Proposition 7.4. a) X̊(C) is a closed and open subspace of X̌(C). b) F_q : X̌(C) → X̌(C) is a homeomorphism for every q ∈ Q₀^{>0}. c) The group G acts by homeomorphisms on X̌(C)."
> "We give X̌₀(C) = X̌(C)/G the quotient topology. Then X̌₀(C) is homeomorphic to colim_{N₀} X̊₀(C) with the inductive limit topology. The projections π : X̊(C) → X̊₀(C) and π̌ : X̌(C) → X̌₀(C) are continuous and since G acts by homeomorphisms, also open."

**A2.10 — Hausdorffness and metrizability downstairs [pp. 45].**
> "Corollary 7.8. For any affine arithmetic scheme X₀ = spec R₀ there are a G-invariant metric d on X̊(C) and a metric δ on X̊₀(C) = X̊(C)/G inducing the topology on X̊(C) and the (quotient-)topology on X̊₀(C). … **The topological space X̊₀(C) is metrizable and separable and in particular Hausdorff.**"
> "Corollary 7.9. Let X₀ be an arithmetic scheme which carries an ample invertible sheaf. Then the spaces X̊(C), X̊₀(C), X̌(C) and X̌₀(C) are Hausdorff."

**A2.11 — the E-subspaces carry the subspace topology [p. 47].**
> "Given an admissible class E as in Definition 4.1 we equip X̊(C)_E and X̊₀(C)_E with the subspace topologies of X̊(C) and X̊₀(C). … We give X̌(C)_E = colim_{N₀} X̊(C)_E and X̌₀(C)_E = colim_{N₀} X̊₀(C)_E the inductive limit topologies. **They agree with the subspace topologies via X̌(C)_E ⊂ X̌(C) and X̌₀(C)_E ⊂ X̌₀(C) because the subspaces F_ν^{−1}X̊(C) and F_ν^{−1}X̊₀(C) are open in X̌(C) resp. X̌₀(C) for all ν ∈ N₀.** … In the rest of the section, for simplicity, we assume that X₀ → spec Z is surjective and hence char K₀ = 0 and **N₀ = N**."

**A2.12 — packets: the fibration and its fibres [pp. 32–33, 38].**
> "N x₀^Ẑ = Gal(κ(x)/κ(x₀)) ↪ Aut(κ(x)^×) = Ẑ^×_{(p)}. (34)" [p. 32]
> "Ẑ^×_{(p)} × N₀ ↠ S , (a, ν) ↦ χ_x · (a, ν) := χ_x ◦ ( )^a ◦ ( )^ν. (35) Two elements (a, ν) and (a′, ν′) are in the same fibre of this map if and only if ν′ = νp^n and a = p^n a′ for some n ∈ Z." [p. 32]
> "(Ẑ^×_{(p)}/N x₀^Ẑ) ×_{p^Z} Q₀^{>0} ≅ C_{x₀}. (38) … **The set C_{x₀} fibres over the compact group Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p)^, and the fibres are the Q₀^{>0}-orbits in C_{x₀}.**" [pp. 32–33]
> "Thus all R^{>0}-orbits in Γ_{x₀} are circles R^{>0}/N x₀^Z and Γ_{x₀} fibres over Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p) with fibres the R^{>0}-orbits in Γ_{x₀}." [p. 38]

**A2.13 — Theorem 5.2 [p. 34].**
> "Theorem 5.2. Let E be an admissible class with E ⊂ E_max. The following decomposition holds, where x₀ runs over the points of X₀ with finite residue field κ(x₀) and where C^E_{x₀} = C_{x₀} ∩ X̌₀(C)_E : {P₀ ∈ X̌₀(C)_E | (Q₀^{>0})_{P₀} ≠ 1} = ∐_{x₀} C^E_{x₀} (47). For any point P₀ ∈ C^E_{x₀} the isotropy group of P₀ is (Q₀^{>0})_{P₀} = N x₀^Z where N x₀ = |κ(x₀)|. **If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}.**"

**A2.14 — the suspension and Theorem 6.1 [pp. 38–39].**
> "consider the suspension X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0}. It is the quotient of X̌₀(C)_E × R^{>0} by the right Q₀^{>0}-action given by (P₀, u)q = (P₀q, q^{−1}u) = (F_q(P₀), q^{−1}u) for q ∈ Q₀^{>0}. … φ^t([P₀, u]) = [P₀, u e^t]. For a point x₀ of X₀ with finite residue field of characteristic p set Γ_{x₀} = C_{x₀} ×_{Q₀^{>0}} R^{>0} ⊂ X₀. … We set Γ^E_{x₀} = C^E_{x₀} ×_{Q₀^{>0}} R^{>0} … If e.g. E_f ⊂ E then Γ^E_{x₀} = Γ_{x₀}." [p. 38]
> "Theorem 6.1. Let E be an admissible class with E ⊂ E_max. The following decomposition holds, where x₀ runs over the points of X₀ with finite residue fields κ(x₀): {x₀ ∈ X₀ | (R^{>0})_{x₀} ≠ 1} = ∐_{x₀} Γ^E_{x₀}. For any point x₀ ∈ Γ^E_{x₀} the isotropy group of x₀ is (R^{>0})_{x₀} = N x₀^Z." [p. 39]

**A2.15 — Deninger's question [p. 40].**
> "The system X₀ may have to be replaced by a much smaller system: Is there a sub-dynamical system Y₀ ⊂ X₀ = X̌₀(C) ×_{Q>0} R^{>0} or at least one which maps to X₀ such that dim Y₀ = 2d + 1 where d = dim X₀ and such that Y₀ contains at least one periodic orbit in Γ_{x₀} for every closed point x₀ of X₀? If d = 1, is there such a Y₀ which is a Riemann surface lamination in the sense of [Ghy99]?"

**A2.16 — §8: the assertion, Claim 8.1, [Per11], Theorem 8.2, Lemma 8.3 [pp. 49–51].**
> "For an integral normal scheme X₀ of finite type over spec Z with dim X₀ ≥ 1 the dynamical system X₀ = X̌₀(C) ×_{Q>0} R^{>0} is infinite dimensional, whereas we are searching for a system of dimension 2 dim X₀ + 1, e.g. 3 in the case of X₀ = spec Z. … **In this section we will show that the system Y₀ is still infinite-dimensional: Namely, for one-dimensional X₀, flat over spec Z and conditionally for all X₀ we have Y₀ = X̌₀(S¹) ×_{Q>0} R^{>0}.** Here X̌₀(S¹) = X̌(S¹)/G where X̌(S¹) = colim_N X̊(S¹) and X̊(S¹) is the subspace of X̊(C) consisting of points (x, P^×) with P^× : κ(x)^× → S¹ a unitary character. This follows from Theorem 8.2 below which depends on the following assertion **which is known for number rings A** and that we expect to hold in general." [p. 49]
> "If dim A = 0 i.e. if A = κ is a finite field, the claim holds trivially. **If spec A is a non-empty open subscheme of spec o_κ for some number field κ, then the set M in Claim 8.1 is always infinite, and it even has a positive Dirichlet density. This follows from [Per11, Theorem 1].**" [p. 50]
> "Consider the subset X̌(C)_per = colim_N X̊(C)_per ⊂ X̌(C) where X̊(C)_per = {(x, P^×) ∈ X̊(C) | κ(x) ≅ F̄_p for some p and ker P^× is finite}." [p. 50]
> "**Theorem 8.2. Let X₀ be an integral normal scheme of finite type over spec Z. If dim X₀ ≥ 2 or dim X₀ = 1 and char K₀ > 0 assume that Claim 8.1 holds. Then we have  cl(X̌(C)_per) = X̌(S¹)  and  cl(X̌₀(C)_per) = X̌₀(S¹).**" [p. 50]
> "Proof. … Any character of the torsion group F̄_p^× takes values in the roots of unity. Hence X̊(C)_per ⊂ X̊(S¹) … Since X̊(S¹) is closed in X̊(C) the subspace X̌(S¹) is closed in X̌(C) as well … Equality will follow if we show that X̊(C)_per is dense in X̊(S¹)." [p. 50]
> "**Lemma 8.3.** Let ψ : κ(x)^× → S¹ be a character. Fix a finite subset T ⊂ κ(x)^× and some ε > 0. Then there are a maximal ideal m̄ of R̄ and a character **χ : (R̄_m̄/m̄R̄_m̄)^× = (R̄/m̄)^× → S¹ with finite kernel**, such that T ⊂ R̄_m̄ \ m̄R̄_m̄ and |ψ(t) − χ(t mod m̄)| < ε for all t ∈ T. (70)" [p. 50]
> "Using the character χ of the lemma we obtain a point Q = (m, χ) ∈ X̊(C)_per." [p. 51]

**A2.17 — the intro assertion [p. 5].**
> "**For all conditions E that we consider the space X̌₀(C)_E is infinite dimensional** whereas ideally we would want it to be of dimension 2 dim X₀ if e.g. X₀ is flat, normal and of finite type over spec Z. … Using results by Perucca [Per11] we determined this closure if X₀ is the spectrum of the ring of integers in a number field. … **The resulting dynamical system is still infinite dimensional.**"

**A2.18 — [x-06] = `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`, printed p. 12 (= PDF p. 12; page footers verified).**
> "**The space X₀^E is infinite dimensional if dim X₀ ≥ 1** and one could hope that the sub-dynamical system obtained as the closure of the union of all its compact orbits might be significantly smaller. **However, this is not the case as follows from [Den22a, Theorem 8.2].** The closure is the subsystem obtained by replacing X̊(C)_E in the previous constructions with the subspace of pairs (x, P^×) with P^× : κ(x)^× → S¹ a unitary character. For dim X₀ ≥ 2 this is conditional on a result in Diophantine approximation which should be provable and which is known for dim X₀ = 1 and X₀ flat over spec Z."

and [x-06] p. 11:
> "the infinite dimensional connected Hausdorff space W_rat(spec Z)(C)"
> "Here σ ∈ G acts on X̊(C) via (x, P^×)^σ = (x^σ, P^× ◦ σ) and ν ∈ N acts G-equivariantly via F_ν(x, P^×) = (x, P^× ◦ ( )^ν)."

**A2.19 — negative sweeps (SO7 evidence).** `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf` (27 pp.) and `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf` (32 pp.) were extracted in full and searched for `dimension|dimensional|Hausdorff|cube|cell|closure of the periodic|unitary`. **Morishita** returns exactly two hits, neither about these spaces' topological dimension ("dimensional over C" at p. 11 about a multiplicative map; "1-codimensional foliation structure" at p. 14). **[D25]** returns three hits, all about equidimensional cycles in §27, nothing about `X̌₀`. **Neither contains any dimension or Hausdorffness statement about the Deninger spaces, and neither contains a cell construction.**

---

## 3. The objects, fixed once, in my own words

Throughout `X₀ = Spec Z`, `K₀ = Q`, `K = Q̄`, `R = Z̄` (the integral closure of `Z` in `Q̄`), `X = Spec Z̄`, `G = Aut(Q̄/Q)`, `C = ℂ`. By A2.8/A2.11, `char X₀` is the set of all primes, so **`N₀ = N` and `Q₀^{>0} = Q^{>0}`** — I use `N`, `Q^{>0}` from here on, and every `∈ N₀` side-condition in (Tors) is automatic.

1. **Points (A2.6).** `X̊(C)` = multiplicative maps `P : Z̄ → ℂ` with `P(0)=0`, `P(1)=1`, `p := P^{-1}(0)` prime, `P` factoring through `Z̄/p`; equivalently pairs `(x, P^×)` with `x ∈ X` and `P^× : κ(x)^× → ℂ^×` a character. For `x = x_η := (0)` we have `κ(x_η) = Q̄` and `P` is nowhere zero off `0`. Since `Q̄^×` is generated as a group by `Z̄ ∖ {0}` (every algebraic number is a ratio of algebraic integers), `P^×` is determined by `P|_{Z̄}`, and pointwise convergence on `Z̄` implies pointwise convergence on `Q̄^×`.
2. **Topology upstairs (A2.7).** Pointwise convergence on `R = Z̄`, i.e. the subspace topology from `ℂ^{Z̄}`. `Z̄` is countable, so `X̊(C)` is metrizable.
3. **`G`-action (A2.6, A2.18).** Right action `(x,P^×)^σ = (x^σ, P^× ∘ σ)`. `X̊₀(C) = X̊(C)/G` with the quotient topology; it is **metrizable, separable, Hausdorff** (A2.10, Cor. 7.8 — `Spec Z` is affine with countable function field, i.e. an arithmetic scheme in Deninger's sense, A2.7).
4. **Colimit (A2.9).** `X̌(C) = colim_N X̊(C)` along the injective transition maps `F_ν`, with the **inductive-limit topology**; `X̊(C)` sits in it as a **clopen subspace** (Prop. 7.4 a)); `X̌₀(C) = X̌(C)/G ≅ colim_N X̊₀(C)`; `X̌₀(C)` is **Hausdorff** (A2.10, Cor. 7.9 — `Spec Z` affine, hence `O_X` ample).
5. **`E`-loci (A2.11).** `X̌₀(C)_E ⊂ X̌₀(C)` carries the **subspace** topology; the ν-strata `F_ν^{-1}X̊₀(C)` are open in `X̌₀(C)`.
6. **Suspension (A2.14).** `X₀ = X̌₀(C)_E ×_{Q^{>0}} R^{>0}`, quotient of `X̌₀(C)_E × R^{>0}` by `(P₀,u)·q = (F_q(P₀), q^{-1}u)`; quotient map `q̄` continuous (definition of the quotient topology) and open (the group acts by homeomorphisms, so saturations of opens are open). Flow `φ^t[P₀,u] = [P₀, u e^t]`.
7. **Packets (A2.12–A2.14).** `Γ_{x₀} = C_{x₀} ×_{Q^{>0}} R^{>0}`; orbits in `Γ_{(p)}` are circles of primitive length `log p`, parametrized by the compact group `B_p := Ẑ^×_{(p)}/p^Ẑ`, the fibres of the fibration being exactly the orbits.

**Two book-keeping facts I will use repeatedly, both proved here rather than assumed.**

**(F-i) Over `Spec Z`, `X̊(C)_{E_max} = X̊(C)_{E_tors}`, and at closed points both coincide with the finite-kernel locus.**
The fields occurring are `κ(x_η) = Q̄` (characteristic 0) and `κ(x) = F̄_p` at closed points. By A2.1, (Image) is imposed "**Only if char κ > 0**", and then only through the implication "`κ^× ⊗ Q ≠ 0 ⟹ χ(κ^×) ⊗ Q ≠ 0`". For `κ = F̄_p` the group `κ^×` is torsion, so `κ^× ⊗ Q = 0` and the implication is vacuously true. Hence (Image) constrains nothing on either field, so `E_max` and `E_tors` cut out the same subset of `X̊(C)`. At a closed point, `κ(x)^× = F̄_p^× = µ(F̄_p)`, so (Tors) reads "`ker P^×` finite (with order in `N₀ = N`)" — which is verbatim the `E_f` condition (A2.5, item 3). **Consequence:** over `Spec Z` *every* admissible `E` with `E ⊇ E_f` has full packets, `C^E_{x₀} = C_{x₀}`, without invoking Thm 5.2's "`E ⊃ E_f`" clause; and the closed-point locus of `X̌₀(C)_{E_max}` is precisely `X̌₀(C)_per` of A2.16.

**(F-ii) `∐_p Γ_{(p)} = q̄( X̌₀(C)_per × R^{>0} )`, and this is exactly the periodic point set of `X₀`.**
By A2.16, `X̊(C)_per = {(x,P^×) : κ(x) ≅ F̄_p, ker P^× finite}`; by A2.12 (§5 opening, p. 31) `pr₀^{-1}(x₀)` consists of the `G`-orbits of pairs `(x,P^×)` with `x` over `x₀` satisfying (Tors), and `C_{x₀} = ∪_ν F_ν^{-1} pr₀^{-1}(x₀)`. By (F-i) these two descriptions agree, so `∐_{x₀ closed} C_{x₀} = X̌₀(C)_per`. Suspending gives `∐_p Γ_{(p)} = q̄(X̌₀(C)_per × R^{>0})`, and by Thm 6.1 (A2.14) this is exactly `{x₀ ∈ X₀ : (R^{>0})_{x₀} ≠ 1}`, the set of periodic points (there are no fixed points: isotropy is `p^Z ≠ R^{>0}`).

---

## 4. Line-by-line re-derivation of Theorem B(b)

I re-derive each step in full. A reader can check §4 without the note.

### 4.0 The premise: part (a), and whether it holds on the whole window

**Claim.** Let `E` be admissible with `E_f ⊆ E ⊆ E_max`, `S ⊆ X₀` closed and flow-invariant, containing for each prime `p` at least one periodic orbit `γ_p ⊂ Γ_{(p)}`. Then `S ⊇ Γ_{(p)}` for every `p`, hence `S` contains the whole periodic-point set.

**Re-derivation.** Theorem A (adjudicated CONFIRMED, three independent derivations; I re-checked its six steps against A2.7, A2.9, A2.12, A2.14 and found them correct — in particular Step 1's normalization: by (35) every finite-cyclic-kernel character of `F̄_p^×` is `χ_x ◦ ( )^a ◦ ( )^ν`, and `F_ν^{-1}(x, χ^{aν'}) = F_{ν'/ν}(x, χ^a)`, so every point of `C_{x₀}` lies on the `Q^{>0}`-orbit of some `(x, χ^{a})` with `a ∈ Ẑ^×_{(p)}`; admissibility's `ν`-biconditional (A2.2) plus Prop. 4.2's forward/backward invariance (A2.3) keep `χ^a ∈ E`) gives `cl(γ_p) ⊇ Γ^E_{(p)}`. `S` closed and `γ_p ⊆ S` give `S ⊇ cl(γ_p) ⊇ Γ^E_{(p)}`. By (F-i), `Γ^E_{(p)} = Γ_{(p)}` for every `E ⊇ E_f` over `Spec Z`. By (F-ii), `S ⊇ ∐_p Γ_{(p)}` = all periodic points. ∎

**Answer to the brief's question "does part (a) really hold on the whole window?" — YES**, and in fact on a wider one: `(a)` holds for **every** admissible `E ⊆ E_max` with `E ⊇ E_f`, and the appeal to Thm 5.2's "`E ⊃ E_f`" clause can be replaced by the elementary observation (F-i). The uncountability of the orbit family is the uncountability of `B_p`, which I re-checked: `Ẑ^×_{(p)} = ∏_{ℓ≠p} Z_ℓ^× ↠ ∏_{ℓ∈T}(Z/ℓ)^×/(\text{squares}) ≅ (C₂)^{|T|}` for any finite set `T` of odd primes `≠ p`; the closure `p^Ẑ` maps onto the (order `≤ 2`) subgroup generated by the image of `p`; so `B_p` surjects onto a group of order `≥ 2^{|T|−1}` for every `T`, hence is infinite; an infinite profinite group is perfect and therefore uncountable (Baire). ✔

### 4.1 Step 1 — `S` contains the closure of the periodic set, computed in `X̌₀(C)_{E_max}` and pushed down

Put `A := X̌₀(C)_per`. By (F-i), `A ⊆ X̌₀(C)_{E_max}`, and by A2.11 the latter carries the subspace topology of `X̌₀(C)`. Therefore
`cl_{X̌₀(C)_{E_max}}(A) = X̌₀(C)_{E_max} ∩ cl_{X̌₀(C)}(A)`
— the elementary identity `cl_Y(B) = Y ∩ cl_Z(B)` for `B ⊆ Y ⊆ Z` with `Y` carrying the subspace topology. (The note argues this with sequences; the identity is unconditional and shorter, and does not need first countability of `X̌₀`.) Let `j₁ : X̌₀(C)_{E_max} → X₀`, `P ↦ [P,1]`; it is continuous (composite of `P ↦ (P,1)` with `q̄`). Continuity gives `j₁(cl A) ⊆ cl(j₁(A)) ⊆ cl(∐_p Γ_{(p)}) ⊆ cl(S) = S` using (F-ii) and §4.0. **So: for every `P ∈ X̌₀(C)_{E_max} ∩ cl_{X̌₀(C)}(X̌₀(C)_per)`, the point `[P,1]` lies in `S`** — and by flow-invariance `[P,v] ∈ S` for every `v ∈ R^{>0}`. ✔

### 4.2 Step 2 — Theorem 8.2: statement, hypotheses as printed, and unconditional status for `Spec Z`

Theorem 8.2 (A2.16) is stated for `X̌(C)` and `X̌₀(C)` — **the unrestricted spaces, with no admissible class in sight**. Its hypothesis is: "*If dim X₀ ≥ 2 or dim X₀ = 1 and char K₀ > 0 assume that Claim 8.1 holds.*" For `X₀ = Spec Z` we have `dim X₀ = 1` **and** `char K₀ = char Q = 0`, so **neither disjunct fires and no assumption is made**: Theorem 8.2 is unconditional for `Spec Z`. ✔ Independently, the paper's own discharge of Claim 8.1 covers every ring that arises in the proof for `Spec Z`: in the proof of Lemma 8.3 (p. 51) `A` is the normalization of `R̄₀ = Z/p₀` in a finite extension `κ` of `κ(x₀)`, so either `p₀ = (p)` and `A` is a **finite field** ("If dim A = 0 … the claim holds trivially", p. 50) or `p₀ = (0)` and `A = o_κ` for a **number field** `κ`, where "*the set M in Claim 8.1 is always infinite … This follows from [Per11, Theorem 1]*" (p. 50). **The note's claim of unconditional status, and its [Per11] citation, are correct as printed.** ✔

Two further checks the note needs and that hold:
* **the approximants lie in the `E_f`-locus.** Lemma 8.3 produces `χ : (R̄/m̄)^× → S¹` **with finite kernel**, and the assembled approximant is `Q = (m, χ) ∈ X̊(C)_per` (p. 51). For `X₀ = Spec Z` and `x = x_η` we have `R̄ = Z̄`, so `R̄/m̄ = F̄_p` and `χ` is a finite-kernel character of `F̄_p^×`; by (F-i) this is exactly the `E_f`-condition, and `E_f ⊂ E_max`. ✔
* **the closure statement transports to the `E_max`-subspace.** Done in §4.1, by `cl_Y(B) = Y ∩ cl_Z(B)`. ✔

**Correction of one parenthetical (MINOR M3).** The note writes "E = E_max (= the system in which [x-03] §8 operates)". §8 operates in the *unrestricted* `X̌₀(C)`; over `Spec Z` that space is strictly larger than `X̌₀(C)_{E_max}` (a character of `Q̄^×` with infinite kernel on `µ(Q̄)` violates (Tors) but is a legitimate point of `X̌₀(C)`). Nothing breaks — the argument intersects with the `E_max`-locus, as §4.1 does — but the parenthetical as written is false.

### 4.3 Step 3 — the splitting `Q̄^× = µ(Q̄) × V` with `V` uniquely divisible

`Q̄` is algebraically closed, so `Q̄^×` is a **divisible** abelian group, and its torsion subgroup is exactly `µ(Q̄)`, which is divisible. A divisible subgroup of an abelian group is a direct summand (divisible ⟺ injective `Z`-module) — **[RU], classical**, but note this is *Deninger's own step*: A2.4 (p. 28) performs exactly this splitting for an arbitrary `k` and records that the complement is "uniquely divisible … and therefore [a] Q-vector space". So the note's step is anchored on disk. Write `Q̄^× = µ(Q̄) × V` with `V ≅ Q̄^×/µ(Q̄)`; `V` is divisible (quotient of divisible) and torsion-free (the full torsion was split off), hence **uniquely divisible**, hence a `Q`-vector space, of countable dimension since `Q̄^×` is countable. For `v ∈ V` and `a ∈ Q` the symbol `v^a` is the unique solution of `(v^a)^m = v^{k}` for `a = k/m`; `a ↦ v^a` is an isomorphism `Q ≅ Q·v` when `v ≠ 1`. ✔

### 4.4 Step 4 — Q-linear independence of the V-components of distinct rational primes

Let `ℓ₁,…,ℓ_n` be distinct rational primes and `ℓ_i = ζ_i · v_i` the decomposition in `µ(Q̄) × V`. Suppose `∏_i v_i^{k_i} = 1` with `k_i ∈ Q`. Multiply the exponents by a common denominator `N ∈ N`: `∏_i v_i^{N k_i} = 1` with `N k_i ∈ Z`. Then
`∏_i ℓ_i^{N k_i} = (∏_i ζ_i^{N k_i}) · (∏_i v_i^{N k_i}) = ∏_i ζ_i^{N k_i} ∈ µ(Q̄)`,
while the left-hand side lies in `Q^×`. Hence `∏_i ℓ_i^{N k_i} ∈ µ(Q̄) ∩ Q^× = {±1}`. Unique factorization in `Q^×` (the `ℓ_i` are distinct primes) forces `N k_i = 0` for all `i`, i.e. `k_i = 0`. **The V-components of distinct rational primes are Q-linearly independent.** ✔ (The note's one-line version, "a multiplicative relation `∏ℓ_i^{k_i} ∈ µ(Q̄) ∩ Q^× = {±1}` forces `k = 0`", is correct; the clearing-of-denominators move is the only thing it leaves implicit.)

### 4.5 Step 5 — the characters `Ψ_t`: well-definedness, unitarity, (Tors), (Image), `E_max`-membership

Extend `{v₁,…,v_n}` to a `Q`-basis `B` of `V`. For `t = (t₁,…,t_n) ∈ [0,½]^n` define `Ψ_t : Q̄^× → S¹` by
* `Ψ_t|_{µ(Q̄)} = ι`, the fixed injection `µ(K) ↪ µ(C)` of [x-03] §5 (p. 31);
* `Ψ_t(v_i^a) = e^{2πi t_i a}` for `a ∈ Q`, `1 ≤ i ≤ n`;
* `Ψ_t(b^a) = 1` for `b ∈ B ∖ {v₁,…,v_n}`, `a ∈ Q`.

**Well-defined.** `V = ⊕_{b∈B} Q·b` and each `Q·b ≅ Q` via `a ↦ b^a` (Step 3); `a ↦ e^{2πi t_i a}` is a homomorphism `Q → S¹`; a homomorphism out of a direct sum is determined by, and exists for, arbitrary homomorphisms on the summands. Combined with `ι` on the direct factor `µ(Q̄)`, `Ψ_t` is a well-defined group homomorphism `Q̄^× → S¹`. ✔

**Unitary.** `ι(µ(Q̄)) ⊆ µ(ℂ) ⊂ S¹` and all other values are on `S¹`. So `(x_η, Ψ_t) ∈ X̊(S¹)` in Deninger's sense (A2.16, p. 49). ✔

**(Tors).** `ker(Ψ_t)_{tors} = ker(Ψ_t|_{µ(Q̄)}) = ker ι = 1`, which is finite with `|·| = 1 ∈ N₀ = N`. So (Tors) holds — **including the `∈ N₀` clause of A2.1, which the note's paraphrase of (Tors) omits (MINOR M6; harmless here because `N₀ = N` over `Spec Z`, A2.11)**. ✔

**(Image).** `κ(x_η) = Q̄` has characteristic 0 and A2.1 imposes (Image) "Only if char κ > 0". Vacuous. ✔

**Hence** `(x_η, Ψ_t)` lies in the `E_max`-locus, and by (F-i) equally in the `E_tors`-locus. ✔

**Kernel size — the honest scope fact.** `Ψ_t(Q̄^×)` is contained in the subgroup of `S¹` generated by `µ(ℂ)` and `e^{2πi t₁},…,e^{2πi t_n}`, which has `Q`-rank `≤ n` modulo torsion. `Q^×` has infinite rank. Hence `(ker Ψ_t|_{Q^×}) ⊗ Q` is **infinite dimensional**, so `Ψ_t ∉ E_{fd0}`, and therefore `Ψ_t ∉ E_f, E_{fg}, E_{fd}, E_{fd0}` (A2.5's chain, p. 29). This is independent of the splitting and of `t`, and it **sharpens** the note's scope note (i) from "may fall outside E" to "falls outside every named class strictly below `E_max`". ✔

### 4.6 Step 6 — `[Ψ_t, 1] ∈ S`

By Step 5, `(x_η, Ψ_t) ∈ X̊(S¹)`, hence its class lies in `X̌₀(S¹)`, which by **Theorem 8.2** (unconditional here, §4.2) equals `cl_{X̌₀(C)}(X̌₀(C)_per)`. By Step 5 it also lies in `X̌₀(C)_{E_max}`. By §4.1, `[Ψ_t, 1] ∈ S`, and `[Ψ_t, v] ∈ S` for all `v`. ✔

### 4.7 Step 7 — continuity of `Θ : t ↦ [Ψ_t, 1]`, checked against the **actual** topology

This is the step the brief singles out ("this needs the actual topology on `X₀` — the colimit/suspension topology of [x-03] §§3–5 — state it and check continuity against it, not against an assumed product topology"). The topology is A2.9 (inductive limit, `Z` open iff `F_ν(Z) ∩ X̊(C)` open for all `ν`) followed by two quotients. The check:

1. `t ↦ (x_η, Ψ_t) ∈ X̊(C)` is continuous **for the pointwise-convergence topology (A2.7)**: it suffices that `t ↦ Ψ_t(r)` be continuous for each fixed `r ∈ Z̄`. Write `r = ζ_r · ∏_{b∈B} b^{a_b(r)}` with only finitely many `a_b(r) ≠ 0`. Then `Ψ_t(r) = ι(ζ_r) · exp(2πi ⟨t, a(r)⟩)` where `a(r) = (a_{v₁}(r),…,a_{v_n}(r)) ∈ Q^n` **does not depend on `t`**. This is a continuous (indeed real-analytic) function of `t`. ✔ Note the map lands in the *metrizable* space `X̊(C)`, so no colimit subtlety arises yet.
2. `X̊(C) → X̊₀(C)` is continuous (quotient map, A2.9). ✔
3. The image lies in `X̊₀(C)_{E_max}` (Step 5), which carries the **subspace** topology (A2.11), so the corestriction is continuous. ✔
4. **The colimit step.** `X̊₀(C)_{E_max} ↪ X̌₀(C)_{E_max}` is the ν = 1 stratum. By A2.9/Prop. 7.4 a) and A2.11 it is an inclusion of an **open (indeed clopen) subspace**, in particular continuous and a homeomorphism onto its image. So the whole cell lives inside one stratum and the colimit topology restricted there is just the metrizable topology of item 1. **There is no "assumed product topology" anywhere in the argument, and none is needed.** ✔
5. `X̌₀(C)_{E_max} → X̌₀(C)_{E_max} × R^{>0} → X₀`, `P ↦ (P,1) ↦ [P,1]`, is continuous (`q̄` is a quotient map, A2.14). ✔
6. Since the image lies in `S` and `S` carries the subspace topology, `Θ : [0,½]^n → S` is continuous. ✔

**Verdict on this step: continuity holds, and for a stronger reason than the note gives** — the entire cell sits in the ν = 1 stratum, which is a clopen metrizable subspace of `X̌₀(C)`; the inductive-limit topology never has to be probed.

### 4.8 Step 8 — injectivity of `Θ`

Suppose `Θ(t) = Θ(t')`, i.e. `[Ψ_t, 1] = [Ψ_{t'}, 1]` in `X₀ = X̌₀(C)_{E_max} ×_{Q^{>0}} R^{>0}`.

1. **Phase.** By A2.14 the equivalence is orbit equivalence for the `Q^{>0}`-action `(P,u)·q = (F_q P, q^{-1}u)`. So there is `q ∈ Q^{>0}` with `(Ψ_{t'}, 1) = (F_q Ψ_t, q^{-1}·1)`. The second coordinate gives `q^{-1} = 1`, i.e. `q = 1`, hence `Ψ_{t'} = Ψ_t` **as points of `X̌₀(C)_{E_max}`**. ✔
2. **Descend from the colimit.** `X̊₀(C)_{E_max} → X̌₀(C)_{E_max}` is **injective**. Two independent on-disk anchors: (α) Prop. 4.2 (A2.3) says `N₀` acts by injections on `X̊₀(C)_E`; a filtered colimit of sets along injective transition maps has injective canonical maps, and Deninger's `colim_{N₀}` is filtered (directed by divisibility, A2.18's phrase "the colimit space over N viewed as a poset ordered by divisibility"). (β) Sharper and purely topological: Prop. 7.4 a) (A2.9) says `X̊(C)` is a **clopen subspace** of `X̌(C)`; if `P, P'` ∈ `X̊(C)` have equal images in `X̌₀(C)` then `P^σ = P'` in `X̌(C)` for some `σ ∈ G`, and both sides lie in the subspace `X̊(C)`, so `P^σ = P'` already in `X̊(C)`. Either way, equality holds already in `X̊₀(C)`. ✔ **(MINOR M2: the note cites only (α), by page; (β) is the anchor that also delivers the topology, and should be cited alongside.)**
3. **Galois.** Equality in `X̊₀(C) = X̊(C)/G` means `(x_η, Ψ_{t'}) = (x_η, Ψ_t)^σ = (x_η^σ, Ψ_t ∘ σ)` for some `σ ∈ G`. The generic point is `G`-fixed, and A2.6/A2.18 give the action `P^σ = P ∘ σ`. So `Ψ_{t'} = Ψ_t ∘ σ`. ✔
4. **Evaluate at the rational primes.** `ℓ_i ∈ Q^× ⊂ Q̄^×` is fixed by every `σ ∈ G`. Hence `Ψ_{t'}(ℓ_i) = Ψ_t(σ(ℓ_i)) = Ψ_t(ℓ_i)`. With `ℓ_i = ζ_i v_i` and `c_i := ι(ζ_i)` (a constant independent of `t`), `Ψ_t(ℓ_i) = c_i e^{2πi t_i}`; so `e^{2πi t_i} = e^{2πi t'_i}`, i.e. `t_i ≡ t'_i (mod 1)`, and since `t_i, t'_i ∈ [0,½]` we get `t_i = t'_i`. ✔

**`Θ` is injective.** ∎ I attempted to break this at each of the four points (a nontrivial `q`; a colimit collapse; a `σ` moving the `ℓ_i`; a wrap-around in the exponential) and none is available.

### 4.9 Step 9 — compact-to-Hausdorff

If (and only if the hypothesis is granted) `S` is Hausdorff in its subspace topology, then `Θ : [0,½]^n → Θ([0,½]^n) ⊆ S` is a continuous bijection from a compact space onto a Hausdorff space, hence a **homeomorphism** (closed subsets of a compact space are compact; compact subsets of a Hausdorff space are closed; so `Θ` is a closed map). **[RU]-free**: this is a two-line argument, given here in full. ✔

**But note precisely what this shows and does not show.** Without the Hausdorff hypothesis one obtains only a **continuous injection**; a continuous injection of a compact space into a non-Hausdorff space need not be an embedding (standard example: the line with two origins receives a continuous injection from `[0,1]` whose image is not homeomorphic to `[0,1]`… more simply: any bijection from a compact space onto a set with the indiscrete topology is continuous). **This is finding J1**: the first sentence of Theorem B(b) asserts the embedded copy unconditionally; only the second sentence carries the hypothesis that earns it.

### 4.10 Step 10 — dimension monotonicity: the exact theorems, and their hypotheses

The note writes: "*If S is metrizable — every candidate lamination is — subspace monotonicity of covering dimension in separable metric spaces (Hurewicz–Wallman, classical) gives dim S ≥ n; more generally, for compact Hausdorff S the cell image is closed and closed-subspace monotonicity in normal spaces applies.*"

**No dimension-theory source is on disk** (I searched `fetched/`, `fetched-r2/`, `fetched-r3/` for Hurewicz, Wallman, Engelking, Nagata, "dimension theory" — nothing). Under SO5 the classical inputs must therefore be labeled **[RU]** and carry no weight until fetched. The precise statements needed, with their hypotheses, are:

* **[RU-1] `dim [0,1]^n = n`** (covering dimension; Lebesgue's covering theorem / Brouwer). Hypotheses: none beyond the space. *Standard reference to fetch: Hurewicz–Wallman, "Dimension Theory", Princeton 1941, Thm IV.1; or Engelking, "Dimension Theory", Thm 1.8.2.*
* **[RU-2] Monotonicity for arbitrary subspaces, separable metric.** "If `A ⊆ X` and `X` is separable metric then `dim A ≤ dim X`." *Hurewicz–Wallman Thm III.1.* Hypothesis: **separable metric** (their standing hypothesis for the whole book).
* **[RU-3] Monotonicity for closed subspaces, normal.** "If `A ⊆ X` is closed and `X` is normal then `dim A ≤ dim X`." *Engelking, Dimension Theory, Thm 3.1.4.* Hypothesis: **normality of `X`** plus **closedness of `A`**.

**MINOR M1 (statement/proof mismatch, second sentence).** Theorem B(b) concludes "every closed invariant `S` … whose subspace topology is **Hausdorff** … has covering dimension ≥ n". Hausdorffness alone is not enough for either [RU-2] or [RU-3]: covering dimension is not monotone on closed subspaces of a merely Hausdorff (non-normal) space. The proof text repairs this itself by naming the two cases that *are* covered (metrizable; compact Hausdorff, which is normal, with the cell image closed), so this is a statement-versus-proof defect, not an error. The statement must read **"Hausdorff and normal (in particular: metrizable, or compact Hausdorff)"**.

**A remark that makes the dimension step cheap in the repaired form (§7, R1).** If the conclusion is moved off the hypothetical `S` and onto Deninger's own spaces, the hypotheses are supplied by the source rather than assumed: `X̊₀(C)` is **metrizable and separable** by Cor. 7.8 (A2.10) — exactly [RU-2]'s hypothesis — and the whole cell lies in `X̊₀(S¹) ⊂ X̊₀(C)` (Step 7 item 4). So `dim X̊₀(S¹) ≥ n` for all `n`, with no extra assumption anywhere.

---

## 5. The interaction with the adjudicated non-Hausdorffness — the finding that changes the theorem's status (J2)

The brief asks: *"Theorem B(b) hypothesizes Hausdorffness of the SUBSYSTEM S in its subspace topology — confirm the proof never uses Hausdorffness of X₀ itself."*

**Confirmed: it never does.** Every step of §4 uses only (i) continuity of the quotient maps, (ii) the metrizable topology on the ν = 1 stratum, (iii) the subspace-topology identities of A2.11, and (iv) in Step 9, Hausdorffness **of `S`**. Theorem A likewise uses no Hausdorffness (adjudication §2, re-checked). Scope note (ii) of the note is therefore accurate. ✔

**But confirming that is not the end of the interaction.** The adjudicated fact (G1 = NO) does something worse than invalidate the proof: it **empties the hypothesis**. Here is the derivation, done independently by me from the sources rather than taken from the adjudication.

**Proposition (referee O).** Let `E` be admissible with `E_f ⊆ E ⊆ E_max`, `X₀ = Spec Z`, and let `S ⊆ X₀ = X̌₀(C)_E ×_{Q^{>0}} R^{>0}` be closed, flow-invariant, and contain at least one periodic orbit in `Γ_{(p)}` for some prime `p`. **Then `S` is not Hausdorff in its subspace topology.**

*Proof.* By §4.0, `S ⊇ Γ_{(p)}`. Normalize (Step 1 of Theorem A, A2.12 (35)/(38)) the given orbit as `γ = {[P₀,w] : w ∈ R^{>0}}` with `P₀ = (x, χ^{a₀})`, `a₀ ∈ Ẑ^×_{(p)}`, and fix `v ∈ R^{>0}`.

*Choice.* `B_p = Ẑ^×_{(p)}/p^Ẑ` is infinite (§4.0), so pick `c ∈ Ẑ^×_{(p)}` with `[c] ≠ [a₀]` in `B_p`. Since `N` is dense in `Ẑ_{(p)} = lim_{(M,p)=1} Z/M` (CRT: every residue class mod every `M` prime to `p` contains positive integers), choose `n_k ∈ N` with `n_k → c a₀^{-1}` in `Ẑ_{(p)}`. Set `z_k := [P₀, n_k v] ∈ γ ⊆ S`.

*First limit (Theorem A).* `(P₀, n_k v)·n_k = (F_{n_k}(P₀), n_k^{-1}·n_k v) = (F_{n_k}(P₀), v)`, so `z_k = [F_{n_k}(P₀), v]` with `F_{n_k}(P₀) = (x, χ^{n_k a₀})`. For fixed `r ∈ Z̄`: if `r ∈ x` both sides vanish; otherwise `r̄ ∈ F̄_p^×` has finite order `d` prime to `p`, and reduction `Ẑ_{(p)} → Z/d` is a ring map, so `n_k a₀ ≡ (c a₀^{-1}) a₀ = c (mod d)` for `k` large, whence `χ(r̄^{n_k a₀}) = χ(r̄^{c})` **eventually and exactly**. So `F_{n_k}(P₀) → (x,χ^{c})` pointwise, i.e. in `X̊(C)` (A2.7), hence in `X̊₀(C)_E`, hence in the clopen ν = 1 stratum of `X̌₀(C)_E` (A2.9/A2.11), and `z_k → [(x,χ^c), v]` by continuity of `q̄`.

*Second limit (rotation).* Frobenius lies in the Galois image `p^Ẑ` of (34) (A2.12), so `F_p(P₀) = (x, χ^{p a₀}) = (x, χ^{a₀} ∘ Frob) = P₀` in `X̊₀(C)`. Hence `[P₀,u] = [F_p(P₀), p^{-1}u] = [P₀, p^{-1}u]`, so `[P₀,u] = [P₀, p^{j}u]` for every `j ∈ Z`. Choose `j_k ∈ Z` with `p^{j_k} n_k v ∈ [v, pv)`; by compactness pass to a subsequence with `p^{j_k} n_k v → w^* ∈ [v, pv]`. Then `z_k = [P₀, p^{j_k} n_k v] → [P₀, w^*]` by continuity of `w ↦ q̄(P₀, w)`.

*The two limits are distinct.* If `[(x,χ^c), v] = [P₀, w^*]` then `(x,χ^c) = F_q(P₀)` for some `q ∈ Q^{>0}`, i.e. the two points lie in one `Q^{>0}`-orbit of `C_{(p)}`; but by A2.12 (p. 33) "**the fibres [of `C_{x₀} → Ẑ^×_{(p)}/p^Ẑ`] are the `Q₀^{>0}`-orbits**", so they would have the same base class, contradicting `[c] ≠ [a₀]`.

*Conclusion.* The sequence `(z_k)` lies in `γ ⊆ S`; its two limits `[(x,χ^c),v] ∈ Γ_{(p)} ⊆ S` and `[P₀,w^*] ∈ γ ⊆ S` are distinct points **of `S`**. In a Hausdorff space sequential limits are unique. Hence `S`, with its subspace topology, is not Hausdorff. ∎

*(This reproduces probe B's Cor. A.2 and the adjudication's §3 by an independent route; I re-derived it from A2.7, A2.9, A2.12 and A2.14 without consulting either derivation's text while doing so. The only extra observation is that the statement applies verbatim to `S` — since sequence and both limits lie inside `S` — not merely to the ambient `X₀`.)*

### 5.1 What follows

1. **Theorem B(b) is vacuously true.** No `S` satisfying its standing hypotheses is Hausdorff, so the conditional clauses ("whose subspace topology is Hausdorff … has covering dimension ≥ n") never fire. As stated the theorem has **no content** post-adjudication.
2. **Corollary (ii) is still true, but "by (b)" is the wrong citation.** A lamination in the sense of S4 / [Ghy99] is a compact **metrizable** foliated space; a subspace `Y₀ ⊆ X₀` carries the subspace topology; a metrizable space is Hausdorff. The Proposition above therefore forbids `Y₀` outright — **no cells, no dimension theory, no [RU] input**. And it forbids more: not just finite-dimensional laminations but **every** Hausdorff (in particular every metrizable, every compact-Hausdorff, every regular-plus-second-countable) closed invariant subspace meeting even one packet. This is a **stronger and cheaper** kill than the one Theorem B(b) was written to deliver.
3. **The cell construction is not thereby worthless — it must be relocated.** Its natural home is `X̌₀(C)` itself, which **is** Hausdorff by Cor. 7.9 and whose ν = 1 stratum `X̊₀(C)` is **metrizable and separable** by Cor. 7.8 (A2.10). There the compact-to-Hausdorff step is unconditional, the [RU-2] hypothesis is supplied by the source, and one obtains a genuine theorem: **`dim X̊₀(S¹) = dim X̌₀(S¹) = ∞`**, which is exactly the statement Deninger asserts without proof (A2.17, A2.16 p. 49, A2.18). That is repair **R1** below.

---

## 6. Break attempts (each gap: try to fill, try to break)

Per the brief, both directions are recorded.

| Step | Break attempt | Outcome |
|---|---|---|
| Splitting `Q̄^× = µ × V` | Is `µ(Q̄)` really a direct summand — could `Q̄^×` fail to split? | **No break.** It splits; and the step is Deninger's own (A2.4, p. 28). |
| Independence of `v_i` | Could two distinct primes have `Q`-dependent V-components through a hidden root-of-unity relation? | **No break.** §4.4 clears denominators and lands in `µ(Q̄) ∩ Q^× = {±1}`; unique factorization closes it. |
| `Ψ_t` well-defined | Could the value `e^{2πi t_i a}` fail to extend from `Z` to `Q`? | **No break.** `Q·v_i ≅ Q` and `a ↦ e^{2πi t_i a}` *is* a homomorphism on `Q`. |
| (Tors) | Could `|ker_{tors}| ∉ N₀` bite? | **No break.** `N₀ = N` over `Spec Z` (A2.11), and `ker_{tors} = 1`. |
| (Image) | Could (Image) bite at the generic point? | **No break.** char 0; A2.1 says "Only if char κ > 0". |
| Thm 8.2 | Is `Spec Z` really outside the conditional clause? Could `Claim 8.1` be needed for the generic fibre? | **No break.** `dim = 1`, `char K₀ = 0`; and even tracing the proof, the rings that arise are finite fields or `o_κ`, both discharged on p. 50. |
| Continuity | Could the inductive-limit topology be finer than expected and destroy continuity? | **No break.** Continuity *into* a colimit only needs continuity into one stratum, and the stratum is clopen (Prop. 7.4 a)). The colimit topology's fineness threatens continuity *out of* `X̌`, which is not used. |
| Injectivity | Could a nontrivial `q ∈ Q^{>0}` or `σ ∈ G` identify `Θ(t)` with `Θ(t')`? | **No break.** Phase kills `q`; `σ` fixes rational primes. |
| Compact-to-Hausdorff | Can the embedding be obtained without Hausdorffness of `S`? | **BREAKS.** It cannot; a continuous compact-to-arbitrary injection need not be an embedding. → **J1**. |
| The hypothesis itself | Does any Hausdorff `S` exist? | **BREAKS.** §5: none does. → **J2**. |
| Dimension for general `E` in the window | Can the cells be produced inside `E_f`? Attempted fill: send the remaining basis lines **injectively** into `S¹`, so that `Ψ_t` is injective and hence in `E_f`. | **FILL FAILS, and provably so.** Injectivity of the resulting `Ψ_t` fails exactly when `e^{2πi ⟨t,a⟩} ∈ ι(µ(Q̄))·D` for some `0 ≠ a ∈ Q^n`, where `D ⊂ S¹` is the (countable) image of the complementary lines. The good parameter set is the complement of a **countable** set of solutions, which is dense but contains no cube and no arc. So this route cannot give even a 1-cell inside `E_f`. Whether the `E_f`-unitary locus contains an arc at all is left **open** (recorded as a residual question in §9). |
| Novelty | Does any on-disk source already prove the dimension statement? | **PARTIAL BREAK of the novelty claim.** Deninger *asserts* the conclusion in three places (A2.16 p. 49, A2.17 p. 5, A2.18 [x-06] p. 12) without proof; no proof exists in [x-03], [x-06], [r3s-08] or [D25] (A2.19). → **J3**. |

---

## 7. Repairs — exact replacement text

The adjudicator applies these; I do not edit the probe note (per instruction).

### R1 — replace Theorem B(b) and its proof (fixes **J1**, **J2**, **M1**)

> **(b) [replacement].** Let `X₀ = Spec Z`. Write `Ψ_t` for the unitary characters of `Q̄^×` constructed below.
>
> **(b1) (unconditional; this is the content).** For every `n ≥ 1` the space `X̊₀(S¹) ∩ X̊₀(C)_{E_max} ⊆ X̊₀(C)` contains a homeomorphic copy of the `n`-cube. Since `X̊₀(C)` is **metrizable and separable** ([x-03] Cor. 7.8, p. 45), covering dimension is monotone on its subspaces, so
> `dim X̊₀(S¹) = dim X̌₀(S¹) = dim X̌₀(C)_{E_max} = dim X̌₀(C) = ∞.`
> *Proof.* Split `Q̄^× = µ(Q̄) × V` with `V` a countable-dimensional `Q`-vector space (the splitting used in [x-03] Lemma 4.3's proof, p. 28). Fix distinct rational primes `ℓ₁,…,ℓ_n` with V-components `v₁,…,v_n`; these are `Q`-linearly independent, since a relation `∏ v_i^{k_i} = 1` with `k_i ∈ Q` gives, after clearing denominators, `∏ ℓ_i^{Nk_i} ∈ µ(Q̄) ∩ Q^× = {±1}` and hence `k = 0` by unique factorization. Extend to a `Q`-basis `B`, and for `t ∈ [0,½]^n` define `Ψ_t : Q̄^× → S¹` by `Ψ_t|_{µ(Q̄)} = ι`, `Ψ_t(v_i^{a}) = e^{2πi t_i a}` (`a ∈ Q`), `Ψ_t(b^a) = 1` for `b ∈ B ∖ {v_i}`. Each `Ψ_t` is a well-defined unitary character with `ker(Ψ_t)_{tors} = 1`, so (Tors) holds with `|ker_{tors}| = 1 ∈ N₀ = N`, and (Image) is imposed only in positive characteristic ([x-03] p. 27), so `(x_η, Ψ_t)` lies in `X̊(S¹)` and in the `E_max`-locus. The map `t ↦ (x_η,Ψ_t)` is continuous for the pointwise topology (for fixed `r`, `Ψ_t(r) = ι(ζ_r)e^{2πi⟨t,a(r)⟩}` with `a(r) ∈ Q^n` independent of `t`), hence `Θ̊ : t ↦ [(x_η,Ψ_t)] ∈ X̊₀(C)` is continuous. `Θ̊` is injective: `[(x_η,Ψ_t)] = [(x_η,Ψ_{t'})]` gives `Ψ_{t'} = Ψ_t ∘ σ` for some `σ ∈ G`, and evaluating at the `G`-fixed rational primes `ℓ_i` gives `e^{2πi t_i} = e^{2πi t'_i}`, so `t = t'` in `[0,½]^n`. As `X̊₀(C)` is Hausdorff ([x-03] Cor. 7.8), `Θ̊` is a homeomorphism onto its image. The image lies in `X̊₀(S¹)`, and `X̊₀(C)` is an open subspace of `X̌₀(C)` ([x-03] Prop. 7.4 a), p. 43, and p. 47), which gives the four displayed equalities by monotonicity plus `dim [0,1]^n = n`. ∎
>
> **(b2) (the suspended form; conditional, and the condition is empty).** Let `S ⊆ X₀ = X̌₀(C)_{E_max} ×_{Q^{>0}} R^{>0}` be closed, flow-invariant, and meet every packet. Then for every `n ≥ 1` there is a **continuous injection** `Θ_n : [0,½]^n → S`, namely `t ↦ [Ψ_t, 1]` (by (a), `S` contains all periodic points; `S` closed then forces `S ⊇ [P,v]` for every `P ∈ X̌₀(C)_{E_max} ∩ cl(X̌₀(C)_per) = X̌₀(C)_{E_max} ∩ X̌₀(S¹)` — [x-03] Thm 8.2, p. 50, unconditional for `Spec Z` — and each `[Ψ_t]` is such a `P`). **If** the subspace topology of `S` is Hausdorff **and normal** (e.g. metrizable, or compact Hausdorff), then each `Θ_n` is an embedding and `dim S ≥ n` for all `n`, so `S` is infinite-dimensional.
>
> **(b3) (why (b2)'s conditional clause never fires, and what replaces it).** No such `S` is Hausdorff. Indeed by (a) `S` contains a full packet `Γ_{(p)}`, and inside `Γ_{(p)}` the Theorem-A sequence `z_k = [P₀, n_k v]` has two distinct limits — `[(x,χ^c),v]` with `[c] ≠ [a₀]` in `B_p` (Theorem A) and `[P₀, w^*]` with `w^*` a limit of `p^{j_k}n_k v` in `R^{>0}` (using `F_p(P₀) = P₀`, so `[P₀,u] = [P₀,p^j u]`) — both lying in `S`; distinctness because the fibres of `C_{x₀} → Ẑ^×_{(p)}/p^Ẑ` are exactly the `Q^{>0}`-orbits ([x-03] p. 33). Hence **`S` is never Hausdorff**, and the intended consequence is obtained without (b2): *no compact metrizable lamination — indeed no Hausdorff closed flow-invariant subspace whatever — of `X₀` meets even a single packet.* The first alternative of Deninger's question ([x-03] §6 p. 40) is answered **NO**, by (a) plus non-Hausdorffness alone.

### R2 — replace Corollary (ii) (fixes **J2**, **M3**)

> **(ii) [replacement].** For `E = E_max` and for the unitary system `Y₀^Den = X̌₀(S¹) ×_{Q^{>0}} R^{>0}` — the two spaces ledger §9.3 names — there is **no** compact lamination `Y₀ ⊆ X₀`, closed and flow-invariant, containing at least one periodic orbit in `Γ_{(p)}` for every `p`; indeed there is no such subspace that is Hausdorff in its subspace topology, of any dimension. This follows from **(a) together with the non-Hausdorffness of the packets** ((b3); adjudication §3), not from a dimension count. Independently, `(b1)` establishes that the space in which any such candidate would have to sit — Deninger's closure system, whose leaf space is `X̌₀(S¹)` — is genuinely infinite-dimensional, which is the statement [x-03] p. 49 and [x-06] p. 12 assert without proof. The first alternative of Deninger's question ([x-03] §6 p. 40) has answer **NO**. *(Note: [x-03] §8 operates in the unrestricted `X̌₀(C)`, not in `X̌₀(C)_{E_max}`; over `Spec Z` the latter is the proper subspace cut out by (Tors), and Thm 8.2 transports to it because `X̌₀(C)_E` carries the subspace topology, [x-03] p. 47.)*

### R3 — replace scope note (i) (fixes **M5**)

> **(i) [replacement].** The cell characters `Ψ_t` have image of `Q`-rank `≤ n` modulo torsion, while `Q^×` has infinite rank; hence `(ker Ψ_t|_{Q^×}) ⊗ Q` is infinite dimensional and `Ψ_t ∉ E_{fd0}` — and therefore `Ψ_t` lies outside **every** class in Deninger's named chain below `E_max`, i.e. outside `E_f, E_{fg}, E_{fd}, E_{fd0}` ([x-03] p. 29). So the construction is available only for `E = E_max` (= `E_tors` over `Spec Z`) and, natively, for the unitary system `X̌₀(S¹) ×_{Q^{>0}} R^{>0}`, where (Tors) is not imposed at all. The obvious attempt to repair this for `E = E_f` — make `Ψ_t` injective by sending the remaining basis lines injectively into `S¹` — provably fails: injectivity survives only off a countable set of parameters, whose complement contains no arc, let alone a cube. Whether the `E_f`-unitary locus contains an arc is **open**. Part (a) is unaffected and holds for every admissible `E ⊇ E_f`; over `Spec Z` this needs no appeal to [x-03] Thm 5.2, because at a closed point `κ(x) = F̄_p` is torsion, so (Tors) ⟺ finite kernel ⟺ the `E_f`-condition, and the packet locus is the same for every such `E`.

### R4 — replace the citation in the injectivity step (fixes **M2**)

> "…injectivity of the colimit strata, **[x-03] Prop. 4.2, p. 27** ('The monoid `N₀` acts by injections on `X̊(C)_E` and `X̊₀(C)_E`'), whence the canonical maps into the filtered colimit (indexed by `N` ordered by divisibility) are injective; the sharper anchor, which also fixes the topology, is **Prop. 7.4 a), p. 43** ('`X̊(C)` is a closed and open subspace of `X̌(C)`') together with the paragraph on **p. 47** ('They agree with the subspace topologies via `X̌(C)_E ⊂ X̌(C)` and `X̌₀(C)_E ⊂ X̌₀(C)` because the subspaces `F_ν^{-1}X̊(C)` and `F_ν^{-1}X̊₀(C)` are open …')."

### R5 — replace the novelty sentence in §0.1 / §8 item 5 (fixes **J3**)

> "Novelty of Theorem B, stated precisely. **(a)** is new: no on-disk source treats the closure of a *single* periodic orbit, and it is Theorem A's corollary. **(b)**: the *conclusion* — that the closure of the periodic orbits is still infinite-dimensional — is **asserted in print by Deninger, three times and without proof**: [x-03] p. 49 ('In this section we will show that the system `Y₀` is still infinite-dimensional', where what is actually shown is the identification `Y₀ = X̌₀(S¹) ×_{Q>0} R^{>0}'); [x-03] p. 5 ('For all conditions E that we consider the space `X̌₀(C)_E` is infinite dimensional'); [x-06] p. 12 ('The space `X₀^E` is infinite dimensional if `dim X₀ ≥ 1` … However, this is not the case as follows from [Den22a, Theorem 8.2]'). No proof of any of these appears in [x-03], [x-06], [r3s-08] or [D25] (full-text searches on disk, 2026-09-02). What is new here is therefore **(α)** a proof of that assertion — repaired form (b1) — and **(β)** its extension from Deninger's `Y₀` to *every* closed flow-invariant subset meeting every packet, which is Theorem A's contribution rather than the cell construction's."

### R6 — add to §8 the [RU] labels (fixes **M7**)

> "Classical inputs, none of which is on disk and all of which are therefore **[RU]** under standing order 5, to be fetched before external circulation: `dim [0,1]^n = n` (Lebesgue/Brouwer; Hurewicz–Wallman, *Dimension Theory*, Thm IV.1); monotonicity of covering dimension for arbitrary subspaces of **separable metric** spaces (Hurewicz–Wallman Thm III.1); monotonicity for **closed** subspaces of **normal** spaces (Engelking, *Dimension Theory*, Thm 3.1.4); divisible subgroups are direct summands (used by [x-03] itself at p. 28, so effectively anchored). The compact-to-Hausdorff criterion is proved inline and needs no citation."

### R7 — page range for the class examples (fixes **M4**)

> "Examples `E_f ⊂ E_{fg} ⊂ E_{fd} ⊂ E_{fd0} ⊂ E_max ⊂ E_tors` ([x-03] **pp. 28–29**; `E_tors` and `E_max` on p. 28, `E_f`…`E_{fd0}` and the inclusion chain on p. 29)."

### R8 — one line for the (Tors) paraphrase (fixes **M6**)

> "(Tors) as printed is: `ker(χ)_tors = ker(χ|_{µ(κ)})` is finite **and `|(ker χ)_tors| ∈ N₀`** ([x-03] p. 27). Over `Spec Z`, `N₀ = N` ([x-03] p. 47), so the second clause is automatic."

---

## 8. Priority / novelty, under standing order 7

I performed the on-disk half of the SO7 check independently, and report it without hedging.

1. **The conclusion of (b) is Deninger's, in print, unproved.** Three verbatim assertions, quoted at A2.16 (p. 49), A2.17 (p. 5) and A2.18 ([x-06] p. 12). At p. 49 the words "we will show that the system `Y₀` is still infinite-dimensional" are followed by a colon and the *identification* `Y₀ = X̌₀(S¹)×_{Q>0}R^{>0}` — the section proves the identification (Thm 8.2) and treats the infinite-dimensionality as evident. A full-text search of [x-03] for `dimension|dimensional` returns **no** occurrence anywhere in §§7–10 that constitutes or gestures at a proof (the hits are: p. 5 the assertion; p. 29 the definitions of `E_{fd}`/`E_{fd0}`; p. 48 an unrelated aside; p. 49 the assertion; p. 63 "1-codimensional foliation"; p. 66 "zero-dimensional" about `K^×`; p. 103 an unrelated remark). **[x-03] contains no dimension-theoretic argument.**
2. **No other on-disk source proves it.** [x-06] repeats the assertion and cites [x-03] Thm 8.2 for it (A2.18). [r3s-08] and [D25] contain nothing on dimension or Hausdorffness of these spaces (A2.19).
3. **The technique is partly Deninger's.** [x-03] §9 (pp. 57–58, Lemma 9.4) already constructs **one-parameter** families of characters by `Q`-linear interpolation on `V = K^×/µ(K)` and pushes them through the pointwise topology — for path-connectedness, not dimension, and into `H_inj` rather than the unitary locus. The note's `Θ` is the `n`-parameter unitary analogue. This is not a priority problem — the purpose and the conclusion are different — but an honest note should cite Lemma 9.4 as the antecedent technique.
4. **What is therefore genuinely new** is (α) the proof, and (β) the strengthening from `Y₀` to arbitrary closed invariant subsets meeting every packet, the latter carried by Theorem A. **The blanket phrase "this note claims novelty for Theorems A, B, C relative to [x-03], [x-06], [r3s-08]" (§8 item 5) is over-broad and must be replaced by R5.**
5. **Not discharged here:** the online half of the SO7 sweep. This referee pass is on-disk only; the note's own §8 item 5 already books a fresh online sweep before circulation, and that obligation stands, sharpened: search specifically for prior proofs that `Hom(K^×, S¹)`-type character spaces of number fields are infinite-dimensional (the Kucharczyk–Scholze circle, [KS18], is the obvious place a proof might already exist in print).

### 8.1 Consequence for the adjudication's own record (J4)

Adjudication §4 item 2 banks probe B's **Corollary B** as the route it "certifies outright", on the ground that "every input published and verified on disk". Corollary B's chain is: Theorem A ⟹ `Y ⊇ cl(∪_p Γ_p) = Y₀` (Thm 8.2, unconditional here — ✔ verified in §4.2) **⟹ `Y` is infinite-dimensional** because "*the system `Y₀` is still infinite-dimensional* ([x-03] §8 p. 49)". That last input is **an assertion in the source, not a theorem in it** (§8 item 1 above), and the implication also silently needs dimension monotonicity along `Y₀ ⊆ Y` (closed subspace of a normal space, [RU-3]) — which in turn needs `Y` normal, i.e. exactly the separation property §5 shows `Y` never has. So:

* the **dimension clause** of the banked closed-half kill was resting on an unproved sentence of [x-03] and on an inapplicable monotonicity;
* the **kill itself is unharmed and in fact strengthened**, because §5's Proposition removes any Hausdorff/metrizable `Y` outright, which is what the S4 target actually was;
* and probe A's B(b), in repaired form **(b1)**, supplies the missing proof of Deninger's assertion, so it is **load-bearing** for the dimension clause after all — contrary to adjudication §4 item 6's "nothing in the adjudicated verdicts rests on them."

**Recommended amendment to the adjudication (for the adjudicator to apply, not me):** §4 item 2's certification should be restated as — *"no closed flow-invariant subsystem of `X₀` meeting every packet is Hausdorff in its subspace topology (hence none is a lamination, a compact metrizable space, or a foliated space); and separately, the leaf space `X̌₀(S¹)` of the closure system is infinite-dimensional (referee-grade proof: probe A B(b1), repaired)."* §4 item 6's parenthetical should drop "(its (a)-part and probe B's Cor. B, which carry the whole S4-closed kill, do not need it)".

---

## 9. VERDICT BLOCK

**VERDICT: PASS-WITH-REPAIRS.** (Not PASS: two of the findings force the theorem statement and its corollary's justification to change. Not FAIL: nothing in (b) is false, and no step failed to re-derive. Not NOT-RE-DERIVED: every step was re-derived in full in §4–§5 from the on-disk sources.)

**Findings, severity-tagged, with locations in `results/c3-r/probe-9.3-a.md` (line numbers of the 159-line file as of 2026-09-02):**

| ID | Severity | Location | Finding | Repair |
|---|---|---|---|---|
| **J1** | **MAJOR** | line 77 (Theorem B, clause (b), first sentence); proof at line 91 | The statement asserts unconditionally that `S` "contains … a homeomorphic copy of the n-cube"; the proof delivers only a **continuous injection**, upgraded to an embedding solely under the Hausdorff hypothesis that appears in the *next* sentence. A continuous injection of a compactum into a non-Hausdorff space need not be an embedding. | **R1 (b1)/(b2)** |
| **J2** | **MAJOR** | line 77 (clause (b), second sentence); line 79 (Corollary (ii), "by (b)"); line 93 scope note (ii) | Post-adjudication (G1 = NO) the hypothesis "`S` … whose subspace topology is Hausdorff" is **unsatisfiable**: by (a), `S` contains a full packet, and §5's Proposition (re-derived here independently) shows the packet's subspace topology is non-Hausdorff. (b) is therefore **vacuous**; Corollary (ii) is still true but must be justified by **(a) + non-Hausdorffness**, which is cheaper *and* stronger (it excludes every Hausdorff closed invariant subspace, of any dimension, meeting even one packet). | **R1 (b3)**, **R2** |
| **J3** | **MAJOR** (priority, SO7) | line 155 (§8 item 5); line 13 (§0 item 1) | The blanket novelty claim for "Theorem B" is over-broad: the *conclusion* of (b) is asserted in print, without proof, by Deninger at [x-03] p. 49, [x-03] p. 5 and [x-06] p. 12. What is new is a proof plus the extension from `Y₀` to arbitrary closed invariant subsets. Also: the interpolation technique is the `n`-parameter unitary analogue of [x-03] Lemma 9.4 (pp. 57–58) and should cite it. | **R5** |
| **J4** | **MAJOR** (cross-cutting) | `probe-9.3-adjudication.md` §4 items 2 and 6 | The adjudication certifies probe B's Cor. B "outright" although its dimension clause rests on [x-03] p. 49's *unproved assertion* and on a monotonicity step whose normality hypothesis §5 shows is never met. The kill survives (strengthened, via non-Hausdorffness), but B(b1) is the missing proof and B(b) is therefore **load-bearing**, contrary to §4 item 6. | **§8.1 amendment** |
| M1 | MINOR | line 77 (second sentence of (b)) | "whose subspace topology is Hausdorff … has covering dimension ≥ n": covering-dimension monotonicity needs **normality** (closed subspace) or **separable metric** (arbitrary subspace), not bare Hausdorffness. The proof text covers the right cases; the statement does not. | **R1 (b2)** |
| M2 | MINOR | line 89 (proof, injectivity paragraph); line 152 (§8 item 2) | The colimit-embedding step cites only Prop. 4.2, p. 27 ("N₀ acts by injections"), which gives injectivity but not the topology. The topological anchor is Prop. 7.4 a) p. 43 plus the p. 47 subspace-topology paragraph. | **R4** |
| M3 | MINOR | line 79 (Corollary (ii)) | "`E = E_max` (= the system in which [x-03] §8 operates)" is false: §8 operates in the unrestricted `X̌₀(C)`, strictly larger over `Spec Z`. Harmless (the argument intersects with the `E_max`-locus), but wrong as written. | **R2** |
| M4 | MINOR | line 27 (§1.2) | "Examples `E_f ⊂ … ⊂ E_max ⊂ E_tors` ([x-03] p. 28)": `E_tors`/`E_max` are on p. 28, but `E_f`, `E_fg`, `E_fd`, `E_fd0` and the inclusion chain are on **p. 29**. | **R7** |
| M5 | MINOR | line 93 scope note (i) | Understated: the cell characters do not merely "may fall outside E" — they lie outside **every** named class below `E_max` (`Ψ_t ∉ E_{fd0}`, because the image has `Q`-rank ≤ n while `Q^×` has infinite rank). The failed repair for `E_f` should be recorded, and the (a)-on-the-whole-window claim can be made independent of Thm 5.2. | **R3** |
| M6 | MINOR | line 27 (§1.2) | (Tors) is paraphrased as "finite kernel on roots of unity", dropping the printed clause "**and `|(ker χ)_tors| ∈ N₀`**" ([x-03] p. 27). Harmless over `Spec Z` (`N₀ = N`, p. 47) but must be recorded, since it is not harmless for general `N₀`. | **R8** |
| M7 | MINOR | line 93 scope note (iii); line 152 | The classical dimension-theory inputs are **not on disk** and must be labeled **[RU]** with their exact hypotheses (separable metric for arbitrary-subspace monotonicity; normal + closed for the other). No dimension-theory source exists anywhere in `fetched/`, `fetched-r2/`, `fetched-r3/`. | **R6** |

**Counts: FATAL 0 · MAJOR 4 · MINOR 7.**

### What is now established at referee grade, and its precise scope

**Established.** Over `X₀ = Spec Z`, with `E = E_max` (equivalently, over `Spec Z`, `E_tors`) or in the unitary system `X̌₀(S¹) ×_{Q^{>0}} R^{>0}`: for every `n ≥ 1` the `n`-cube embeds in `X̊₀(S¹) ∩ X̊₀(C)_{E_max}`, by the explicit map `t ↦ [(x_η, Ψ_t)]` built from a splitting `Q̄^× = µ(Q̄) × V`, the `Q`-linear independence of the V-components of `n` distinct rational primes, and the `G`-fixedness of those primes; the embedding is unconditional because `X̊₀(C)` is metrizable, separable and Hausdorff by [x-03] Cor. 7.8 (p. 45), and the whole cell lies in the clopen ν = 1 stratum, so the inductive-limit topology of [x-03] p. 43 is never at issue. Consequently `dim X̊₀(S¹) = dim X̌₀(S¹) = ∞` — a **proof**, at referee grade, of the assertion Deninger makes without proof at [x-03] pp. 5 and 49 and [x-06] p. 12, and hence of the dimension clause that probe B's Corollary B and the Session-8 adjudication had been importing from those sentences on the author's word. In the suspended system, every closed flow-invariant `S ⊆ X₀` meeting every packet receives a continuous injection of the `n`-cube for every `n` (via [x-03] Thm 8.2, which is **unconditional for `Spec Z`** — `dim X₀ = 1` and `char K₀ = 0`, so neither disjunct of its hypothesis fires, and the rings arising in Lemma 8.3 are finite fields or rings of integers where Claim 8.1 holds by [Per11, Thm 1]).

**Scope, stated exactly.** (1) The cells exist only for `E = E_max`/`E_tors` and for the unitary system; they lie **outside** `E_f, E_{fg}, E_{fd}, E_{fd0}`, and the natural attempt to build them inside `E_f` provably fails (the injective parameters are the complement of a countable set and contain no arc). Whether the `E_f`-unitary locus contains an arc is **open**. (2) In the **suspension** `X₀`, the injection is *not* known to be an embedding, and cannot be made one by hypothesizing Hausdorffness of `S`, because §5 shows no such `S` is Hausdorff; the honest suspended statement is "continuous injection", and the dimension conclusion belongs to the leaf space `X̌₀(S¹)`, not to `S`. (3) The kill of Deninger's first alternative ([x-03] §6 p. 40) that the note attributes to (b) is true but is properly a consequence of (a) plus non-Hausdorffness, and in that form it is stronger: **no Hausdorff closed flow-invariant subspace of `X₀` — of any dimension, lamination or not — meets even one packet.** (4) Nothing here touches the mapping half of S4 (`Q*`, adjudication §5): the cells impose no constraint on a merely continuous equivariant image, since dimension does not pass backwards through continuous surjections. (5) All dimension-theoretic inputs remain **[RU]** until a dimension-theory reference is on disk; the embedding statement itself (n-cube ↪ `X̊₀(S¹)`) is [RU]-free.

---

## 10. Sources — every page read this session

**[x-03]** Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`, 119 pp. **Printed page = PDF page** (verified against the footers on pp. 26–28). Pages read in full: **5** (intro assertions), **23** (Remark 3.4, `P^σ = P ∘ σ`), **26** (footer calibration), **27** ((Tors), (Image), Def. 4.1, Prop. 4.2, (30)–(31)), **28** (Lemma 4.3 with the `µ × V` splitting, Cor. 4.4, `E_tors`/`E_max`), **29** (`E_f`…`E_{fd0}`, the inclusion chain, the "not N-invariant" remark, stability), **31** (§5 opening, `C_{x₀}`, (32)–(33)), **32** ((34)–(37)), **33** ((38)–(46), the packet fibration and its fibres), **34** (Prop. 5.1, Thm 5.2), **38** (§6: the suspension, `Γ_{x₀}`, `Γ^E_{x₀}`), **39** (Thm 6.1 and the packet remark), **40** (Deninger's `Y₀` question; §7 opening topology; Lemma 7.1), **41** (Lemma 7.2), **42** (topology for non-affine `X₀`, quotient topology, Lemma 7.3, definition of `N₀`), **43** ((53) the inductive-limit topology, Prop. 7.4, `X̌₀(C) ≅ colim X̊₀(C)`), **44** (Props. 7.5–7.7), **45** (Cors. 7.8, 7.9), **46** (the Hausdorff remark, Thm 7.10), **47** (Remarks 1–2 on Thm 7.10, the `E`-subspace topologies, `N₀ = N`), **48** ((62)–(66), the adele maps), **49** (§8 opening + the infinite-dimensionality assertion; Claim 8.1), **50** (Claim 8.1 cont., the [Per11] discharge, `X̌(C)_per`, **Theorem 8.2**, **Lemma 8.3**), **51** (proof of Lemma 8.3), **52–53** (continuation of that proof — read to confirm the note's page range "pp. 50–53", which is accurate), **57–58** (§9, Lemma 9.4 — the one-parameter antecedent of the cell construction). Full-text searches over all 119 pages for `dimension|dimensional`, `uniquely divisible|Q-vector space|path-connected|connectedness`.

**[x-06]** Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`, 17 pp. (printed = PDF page). Pages read: **11** (Thm 4.1, the `G`- and `N`-actions, "infinite dimensional connected Hausdorff space", the `E`-conditions), **12** (Thm 4.2 packets, Thm 4.3 connectedness, **the infinite-dimensionality assertion and its [Den22a, Thm 8.2] citation**). Full-text search over all 17 pp. for `dimension|dimensional|closure of|unitary`.

**[r3s-08]** Morishita, arXiv:2508.15971v5, `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`, 27 pp. Extracted in full and searched for `dimension|dimensional|Hausdorff|cube|cell|closure of the periodic|unitary`: two hits, neither about the topological dimension or separation of these spaces (p. 11 "dimensional over C" of a multiplicative map; p. 14 "1-codimensional foliation structure"). **Negative result recorded for SO7.**

**[D25]** Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1, `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf`, 32 pp. Extracted in full and searched with the same pattern: three hits, all "equidimensional" cycles in its §27. **Negative result recorded for SO7.**

**Program files read in full:** `results/c3-r/probe-9.3-adjudication.md` (107 lines); `results/c3-r/probe-9.3-a.md` (159 lines, the whole note, not only §3); `results/corpus-routing.md` header caveats 1–20 (no caveat applies to `x-03`, `x-06`, `r3s-08` or `r3s-22`; caveat 14 confirms `r3s-08` is the v5 the C3 brief cites). `results/c3-r/probe-9.3-b.md` §§0, 5.3 (Corollary B), 5.4, 6, 7, 8, 9 — read for the interaction only.

**Corpus search for dimension theory:** `fetched/`, `fetched-r2/`, `fetched-r3/` searched for `hurewicz|wallman|dimension|engelking|nagata|lamination|ghys|candel`. **No dimension-theory reference is on disk.** Hence the [RU] labels of R6.

— end of referee report (referee O) —
