# REFEREE REPORT O — probe 9.4 note, Lemmas A–D and Proposition 1 (the transplant trichotomy D1–D3)

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Date:** 2026-09-02 (Session 14).
**Referee:** referee O, one of two independent referees on this item (the other is a different model; no communication, no assumption about its findings — standing order 7).
**Note under review:** `results/c3-r/probe-9.4-note.md` (probe 9.4, dated 2026-08-26, Session 8), §§3–7, specifically Lemmas A, B, C, D and Proposition 1 with its Corollary, plus §3's freshman's-dream N-invariance argument and §7 Road 2's Haar formal count.
**Binding context read first, in full:** `results/c3-r/probe-9.3-adjudication.md` (Session-8 adjudication, with its three Session-14 bookkeeping paragraphs), then the whole 9.4 note.
**Standing order 5 discipline:** every source claim below was read this session from the on-disk PDF, with pdftotext extractions made fresh, and is quoted verbatim with its printed page (printed page = PDF page for both [x-03] and [x-06]; verified by page footers). Nothing is asserted from memory; the two places where I reason from unsourced standard algebra are labeled **[RU]** and carry no weight in any verdict.

---

## 0. VERDICT (stated first)

**PASS-WITH-REPAIRS.** 0 FATAL, 6 MAJOR, 11 MINOR.

Every one of the five displayed results survives re-derivation **as a mathematical statement about the objects the note actually applies them to** (X₀ = Spec Z; κ(x) = F̄_p; C = ℂ). I re-derived all of them line by line and, where the note's derivation was incomplete, supplied the missing derivation myself; I also attempted to break each one and failed in every case. The six MAJOR findings are: one over-general hypothesis (Lemma A), one internal contradiction with the adjudication over what "admissible" means (§4 Consequence 2), one asserted-but-not-derived step (§3), one over-reaching definability schema (Proposition 1's Corollary), one unsound interpretive inference (§6's closing paragraph, which I refute by explicit counterexample), and one under-derived constancy claim (§7's Haar count). None of them touches the trichotomy's conclusion; all six have replacement text supplied in §10 below.

Per-lemma verdicts, each argued in its own section:

| Item | Verdict | Findings |
|---|---|---|
| **Lemma A** (mod-p-additive ⇔ Teichmüller) and its converse | **PASS-WITH-REPAIRS** | O-M1 (hypothesis too general); O-m6, O-m7, O-m9 |
| **§3** freshman's-dream N-invariance | **PASS-WITH-REPAIRS** | O-M3 (asserted, not derived — full derivation supplied) |
| **Lemma B** (archimedean threshold empty on the periodic locus) | **PASS** (statement), **PASS-WITH-REPAIRS** (§6's closing inference) | O-M5 (the closing inference is false — counterexample given); O-m2 |
| **Lemma C** (Aut(C) ↠ Aut(μ(C)) = Ẑ^×) | **PASS** | O-m4, O-m5, O-m11 |
| **Lemma D** (i)(ii)(iii) | **PASS** | O-m6, O-m7, O-m8 (all strengthenings, no error found) |
| **Proposition 1** | **PASS** | O-m3, O-m4 |
| **Prop. 1's Corollary** (the no-go schema) | **PASS-WITH-REPAIRS** | O-M4 |
| **§4 Consequence 2** (D3, the transport collapse) | **PASS-WITH-REPAIRS** | O-M2 |
| **§7 Road 2** Haar formal count | **PASS-WITH-REPAIRS** | O-M6, O-m10 |

**Not re-derived (declared):** nothing in this item. Two inputs are consumed from other program documents rather than re-derived here, and are flagged as such wherever used: (i) probe A's Theorem C(b) reachability computation (adjudication §4 item 5b), which I use only to *name* the cut class E(a₀), and (ii) the adjudication's own re-derivations of the (34)–(39) anchors — which I nevertheless re-read verbatim on disk this session anyway (§1 below), so nothing here rests on them at second hand.

---

## 1. Sources read this session, with the verbatim anchors

Extractions: `pdftotext -layout` on the two on-disk PDFs named in the task, plus a 4-page extraction of [D25]. Printed page = PDF page in both [x-03] and [x-06] (checked against page footers on pp. 2, 27, 33, 34, 38, 40, 94, 99, 114, 116 and [x-06] pp. 11, 12, 13).

**[x-03] = Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`.** Pages read in full this session: 2, 5, 6, 26, 27, 28, 29, 31, 32, 33, 34, 37, 38, 39, 40, 89, 90, 91, 94, 95, 99, 104, 113, 114, 116.

- **p. 2** — "If p = char κ(x₀), then Γ_{x₀} is fibred over the compact group  Aut(F̄_p^×)/Aut(F̄_p) = Ẑ^×_{(p)}/p^Ẑ". Also, same page: "the closed points x₀ of X₀ correspond bijectively to compact packets Γ_{x₀} of periodic orbits of length log N x₀ on  X₀ = X̌₀(C) ×_{Q^{>0}} R^{>0}."
- **p. 6** — "Incidentally, if we consider points of W_rat(X) with values in rings without "small multiplicative subgroups" like the complex number field C this process does not give more points." And: "The answer is simple, Y⋄ consists of all the diagrams in X⋄_c(o) whose maps are not only multiplicative but mod p also additive." And: "Thus the process of "completion" to pass from X̌₀(o) to X⋄₀(o) was necessary to obtain something interesting."
- **p. 27** — "(Tors) the group ker(χ)_tors = ker(χ|_{μ(κ)}) is finite and |(ker χ)_tors| ∈ N₀."  "(Image) Only if char κ > 0. If χ(κ^×) is torsion, then κ^× is torsion as well, i.e. κ^× ⊗ Q ≠ 0 implies χ(κ^×) ⊗ Q ≠ 0."  "**Definition 4.1.** A class E of characters χ : κ^× → C^× on algebraically closed fields κ is (N₀−)admissible if for any σ ∈ Autκ resp. ν ∈ N₀ the character χ is in E if and only if χ ∘ σ resp. χ_ν = χ ∘ ( )^ν is in E. Moreover the characters in E should satisfy (Tors)."  Also "The best condition on the characters P^× is not clear to me." Also Prop. 4.2 (E-loci G-invariant, forward- and backward N₀-invariant).
- **p. 28** — "Example. 1) E_tors : (Tors) holds  2) E_max : (Tors) and (Image) hold".
- **p. 29** — "3) E_f : (Tors) and ker χ is finite. Equivalently: |ker χ| ∈ N₀  4) E_fg : (Tors) and ker χ is finitely generated  5) E_fd : (Tors) and ker χ ⊗ Q is finite dimensional  6) E_fd0 : (Tors) and (ker χ|_{κ(x₀)^×}) ⊗ Q is finite dimensional where x₀ = π(x)". And the Remark: "in the p-adic case where we will deal with multiplicative maps P into a p-adic valuation ring and N₀ = p^Z, the right condition E is the following: P is additive mod p. This can be rephrased in terms of absolute values and translated to the case where C is the complex number field. However the resulting class E is not N-invariant."
- **p. 31** — "Fix an injective homomorphism ι : μ(K) ↪ μ(C)." "Let C be an algebraically closed field which satisfies the conditions before Corollary 4.4." The isomorphism (32) i_x : μ^{(p)}(K) ≅ κ(x)^×.
- **p. 32** — (34) "N x₀^Ẑ = Gal(κ(x)/κ(x₀)) ↪ Aut(κ(x)^×) = Ẑ^×_{(p)}"; (35) "Ẑ^×_{(p)} × N₀ ↠ S , (a, ν) ↦ χ_x·(a,ν) := χ_x ∘ ( )^a ∘ ( )^ν", with "Two elements (a, ν) and (a′, ν′) are in the same fibre of this map if and only if ν′ = νp^n and a = p^n a′ for some n ∈ Z"; and (38) "(Ẑ^×_{(p)}/N x₀^Ẑ) ×_{p^Z} Q₀^{>0} ≅ C_{x₀}".
- **p. 33** — "The set C_{x₀} fibres over the compact group  Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) ,  and the fibres are the Q₀^{>0}-orbits in C_{x₀}." And: "The maps (37), (38) and the fibration map depend on our choices of x and ι."
- **p. 34** — "**Theorem 5.2.** … {P₀ ∈ X̌₀(C)_E | (Q₀^{>0})_{P₀} ≠ 1} = ∐_{x₀} C^E_{x₀}. For any point P₀ ∈ C^E_{x₀} the isotropy group of P₀ is (Q₀^{>0})_{P₀} = N x₀^Z where N x₀ = |κ(x₀)|. If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}."
- **p. 38** — the suspension: "X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0}. It is the quotient of X̌₀(C)_E × R^{>0} by the right Q₀^{>0}-action given by  (P₀, u)q = (P₀q, q^{−1}u) = (F_q(P₀), q^{−1}u)"; "φ^t([P₀,u]) = [P₀, ue^t]"; "Γ_{x₀} = C_{x₀} ×_{Q₀^{>0}} R^{>0} ⊂ X₀"; and decisively **"Thus all R^{>0}-orbits in Γ_{x₀} are circles R^{>0}/N x₀^Z and Γ_{x₀} fibres over Ẑ^×_{(p)}/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) with fibres the R^{>0}-orbits in Γ_{x₀}."**
- **p. 39** — "**Theorem 6.1.** … {x₀ ∈ X₀ | (R^{>0})_{x₀} ≠ 1} = ∐_{x₀} Γ^E_{x₀}. For any point x₀ ∈ Γ^E_{x₀} the isotropy group of x₀ is (R^{>0})_{x₀} = N x₀^Z."
- **p. 40** — "**In this section, C is an algebraically closed field with a valuation | | and the corresponding topology.** … we give X(C)• the topology of pointwise convergence. It is the subspace topology induced by the Tychonov topology of C^R = ∏_R C … Since R is countable, X(C)• is a metrizable topological space."
- **p. 89** — "Let o be a p-adically complete rank one valuation ring with quotient field C, maximal ideal m and residue field k of characteristic p." And: "In the following we only consider the monoid N₀ generated by p i.e. the F_p = ( )^p action."
- **p. 90** — Definition 14.1 (triples (x, y, P^×) with the commutative diagram κ(y)→k, O_{{x},y}→o, κ(x)→C; equivalently multiplicative P_y : O_{{x},y} → o "sending 1 to 1 and 0 to 0"); Definition 14.2 (the p-adic continuity condition).
- **p. 94** — "**Definition 14.5.** … Y̌_α = {(x,y,P̌_y) ∈ X̌_c(o) | |P̌_y(r+s) − P̌_y(r) − P̌_y(s)| ≤ α for r, s ∈ Ô_{{x},y}}." "For α = 1/p we are looking at multiplicative maps P̌_y which mod p are also additive. Set Y̌ = Y̌_{1/p}." "**Proposition 14.7.** For 0 < α < 1 we have F_p(Y̌_α) = Y̌_α and Y̌_α ⊂ Y̌, and hence Y̌_α = Y̌ for α ≥ 1/p." Also (172) W_p(P̌_y) : W_p(Ô^♭) = lim ZÔ^♭/I^n → lim o/ω_α^n = o, and (174).
- **p. 95** — the proof of Prop. 14.7: "= |(P̌_y(r+s) − P̌_y(r) − P̌_y(s))^{p^ν} + pc| for some c ∈ o  ≤ max(|P̌_y(r+s)−P̌_y(r)−P̌_y(s)|^{p^ν}, |p|)  ≤ max(α^{p^ν}, 1/p)."
- **p. 99** — Definition 14.12 = (183); and the Remark: "I do not know how to transport such conditions to the points of X̌(C), where X is a scheme of finite type over spec Z and C is the complex number field."
- **p. 104** — "**Remark 14.17.** … G × Aut(o) operates F_p-equivariantly on X(o)• = W_rat(X)(o) and X̌(o). Since automorphisms of o are p-adically continuous we have compatible G × Aut(o)-operations on X_c(o)•, X̌_c(o), X⋄_c(o) and Y⋄ in the obvious way."
- **p. 113** — "For (x,y) = (s,s) the continuous local ring homomorphisms P̂_y^♭ : κ → o^♭ with P̂_y^♭(f) ≠ 0 … are simply the ring homomorphisms P̂_y : κ ↪ k ⊂ o^♭". "**Theorem 15.6.** … 1) There is a natural G × Aut(o) × ⟨F_p⟩-equivariant identification Y⋄ = Hom_cont(ô_K^♭, o^♭)".
- **p. 114** — "Y⋄_s := pr_X^{−1}(s) = Hom(κ, k)."  "Y⋄_{0s₀} := pr_{X₀}^{−1}(s₀) ≅ ∐_{τ₀}{0}/o^×_{K₀} = Hom(κ₀, k)."  "6) The only periodic (i.e. finite) orbit of the F_p-action on Y⋄₀ is Y⋄_{0s₀}. It has order log_p N(π₀) = r if q = p^r."
- **p. 116** — "**Proposition 15.8.** For X₀ = spec Z_p and o = o_p, the set Y̌₀ ⊂ Y⋄₀ consists of the F_p-fixed point s₀ = (ô_p^♭ → F̄_p → ô_p^♭)G and the (infinite) F_p^Z-orbit of η₀ = (ô_p^♭ →^{id} ô_p^♭)G."

**[x-06] = Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`.** Pages read: 11, 12, 13.

- **p. 11** — Theorem 4.1, including the group actions verbatim: "Here σ ∈ G acts on X(C)• via (x, P^×)^σ = (x^σ, P^× ∘ σ) and ν ∈ N acts G-equivariantly via F_ν(x, P^×) = (x, P^× ∘ ( )^ν)."  And: "the dynamical system (X₀, φ^t) has too many periodic orbits, since the N-space W_rat(X₀)(C) does not know enough about the addition in O_{X₀}. In the local p-adic situation below, we know the right modification to make. However in the global case presently we can only impose an "admissible" condition E on the characters P^× : κ(x)^× → C^×".  "**Theorem 4.2.** … {x₀ ∈ X₀^E | φ^t(x₀) = x₀ for some t > 0} = ∐_{x₀} Γ_{x₀}."
- **p. 12** — "The compact subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log N x₀ where N x₀ = |κ(x₀)| (= |R₀/m₀|) and they are pairwise disjoint. In fact Γ_{x₀} is a fibre space over the compact group Aut(F̄_p^×)/Aut(F̄_p) where p = char κ(x) with fibres the compact orbits in Γ_{x₀}."
- **p. 13** — Theorem 4.4 and "In view of Theorem 4.3 the map in the theorem is not a homeomorphism since X₀ is connected, whereas the left hand side is disconnected." Also, relevant to Lemma D(iii): "Consider a field of characteristic zero containing all roots of unity, and fix an injective homomorphism ι : μ(F) = μ(F̄) ↪ C^×. … **One can show that the connected components of W_rat(spec F)(C) are parametrized by the embeddings μ(F) ↪ C^×** and that X_F(C) is the component corresponding to ι." And "The absence of the Steinberg relations in rational cohomology is an indication that the space X_F(C) and hence also our space W_rat(X)(C) do not encode enough information about the additive structure of F resp. O_X."

**[D25] = Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1, `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf`.** Introduction (pp. 1–3) extracted and grepped: the note's §7 Road 1 quote is present verbatim — "The algebra ZA knows nothing about the addition in A. However, the larger G is, … may be interesting to experiment with stronger descent conditions than the Galois … additive structure of A to remedy the defects in the constructions of [KS16] and [Den24]". Quote confirmed; not otherwise load-bearing for this item.

**Not consulted for this item:** [r3s-08] Morishita. The adjudication's §4 item 4 and its third Session-14 bookkeeping paragraph forbid citing [r3s-08] §2.2 for the packet identification or for topology; nothing in Lemmas A–D or Proposition 1 needs it, and I cite it nowhere.
