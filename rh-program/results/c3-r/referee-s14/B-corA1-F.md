# REFEREE REPORT F — probe B, Corollary A.1, the converse inclusion cl(γ) ⊆ Γ^E_p

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Session 14, 2026-09-02.** **Referee:** F (Claude Fable 5.1), one of two independent referees on this item under standing order 7; referee O's report was **not opened**. **Item:** `results/c3-r/probe-9.3-b.md`, Corollary A.1, the parenthetical converse inclusion cl(γ) ⊆ Γ^E_p ("packets are exactly the orbit closures"), the debt recorded at `results/c3-r/probe-9.3-adjudication.md` §4 item 6 and probe B's own §7 Q-c. **Rules applied:** standing order 5 (every source claim below is read from the on-disk PDF at the stated printed page; nothing recalled is used — there is no [RU] item in this report), standing order 7, line-by-line re-derivation, U.S. English.

**Companion files (this run):** `B-corA1-F-rerun-checks.py` / `.json` (finite sanity checks, not load-bearing). **Provenance note:** a file `B-corA1-F.md` from an earlier run of this same referee slot (written 02:15 today) already existed at the target path; it was **not read before the derivation below was finished**, and it has been preserved verbatim as `B-corA1-F-run1-0215.md` (it is also in commit 1ec1709). The note under review already carries dated "[REFEREE PASS 2026-09-02 — Session 14]" blocks at §3, §5 and §7 that cite an adjudication file `results/c3-r/referee-s14/B-corA1-adjudication.md`; **that file is absent from disk and from git history** (only `B-corA1-adjudication-checks.py/.json` exist). The blocks themselves are on disk in the note and are therefore refereed here (§6.2) as part of the item.

---

## 0. VERDICT (stated first)

**PASS-WITH-REPAIRS.** FATAL 0 · MAJOR 2 · MINOR 8.

The converse inclusion is **TRUE** and is now established at referee grade in the strongest form the question admits:

> For X₀ = Spec Z, C = ℂ, N₀ = ℕ, any admissible class E (Def. 4.1), and any periodic orbit γ ⊂ Γ^E_p of X₀ = X̌₀(C)_E ×_{Q^{>0}} R^{>0} (quotient topology): **cl_{X₀}(γ) = Γ^E_p**, with no "char-p part" hedge, in every chart of the colimit, and globally — cl(γ) meets neither the generic stratum nor any other prime's packet. More generally, for **every** arithmetic scheme X₀, every admissible E and every point x₀ with finite residue field, Γ^E_{x₀} is a closed flow-invariant subset of X₀ (it is the fiber over the closed point x₀ of a continuous flow-invariant map X₀ → X₀), so cl(γ) ⊆ Γ^E_{x₀} for every periodic orbit γ ⊂ Γ^E_{x₀}.

The two MAJOR findings are against the note's **original** proof sketch (the parenthetical of Cor. A.1), which (F1) states an incomplete (Tors)-exclusion criterion and (F2) computes the closure of the wrong set in the wrong space. Both gaps are fillable — filled in §4 below by two independent routes — and the note's replacement block (already installed in the note) fills them correctly; my findings against that block are all MINOR (§6.2). Nothing in the adjudicated Session-8 verdicts rested on this converse; what did rest on it — the words "minimal sets" / "smallest closed invariant set" in Cor. A.1's headline and in adjudication §4 item 1 — is now backed.

---

## 1. What is under review (verbatim from the note)

The note's Corollary A.1 (probe B §5, the original text, retained "for the record" under the Session-14 block) reads:

> **Corollary A.1 (packets are minimal sets; the "invariant tori" made precise).** Every orbit of Γ^E_p is dense in Γ^E_p; Γ^E_p is the orbit closure of each of its points and is the smallest closed invariant set containing any one of its orbits. (With Step 5's converse inclusion — every limit of {F_n(P₀)}_n along any subnet is P₀^b for some b ∈ Ẑ_{(p)}, by compactness of Ẑ_{(p)} and the same pointwise evaluation; limits with some component of b equal to 0 kill a μ_{ℓ^∞} and violate (Tors), so they leave the space — one gets cl(γ) ∩ (char-p part) = Γ^E_p exactly. Stated proposition-grade; the kill only needs ⊇.)

Two things are claimed. (i) The headline: Γ^E_p is a minimal set — a nonempty **closed** invariant set every orbit of which is dense. Density of every orbit is Theorem A (⊇, not under review; three independent derivations banked). Closedness of Γ^E_p — equivalently cl(γ) ⊆ Γ^E_p for every orbit γ, given ⊇ — is exactly the converse under review. (ii) The parenthetical's argument for it. The task list (1)–(5) of the assignment is answered in §3 (items 1–2), §4.3 (items 3–5).

The note's §3.1 fixes the topological conventions the corollary lives in; the note's §5 Theorem A fixes the normalization γ = {[P₀, w]}, P₀ = π(x, χ^{a₀}), a₀ ∈ Ẑ×_{(p)} (checked in §4.0 below).

---

## 2. Sources opened, with the load-bearing sentences quoted verbatim

All extractions made this session with `pdftotext -layout` into the session scratchpad; every quotation below was re-read in the extraction at the stated **printed** page (for [x-03] the printed page equals the PDF page; verified at pp. 27 and 40).

**[x-03] Deninger, arXiv:1807.06400v4** (`fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`).

- p. 2 (intro): "the closed points x₀ of X₀ correspond bijectively to compact packets Γ_{x₀} of periodic orbits of length log N x₀ on X₀ = X̌₀(C) ×_{Q^{>0}} R^{>0}." p. 3: "Each periodic orbit of X₀ lies in exactly one packet Γ_{x₀}. … The compact packets Γ_{x₀} are reminiscient of invariant tori. There are no fixed points of the flow." (Compactness is asserted, not proved, here; a grep of the whole extraction for "compact" finds no proof of packet compactness anywhere in the paper — consistent with the note's Session-14 block.)
- p. 23, Remark 3.4: points of X•(C) for affine X₀ are "the multiplicative maps P : R → C satisfying … 1) P(0) = 0, P(1) = 1. 2) p := P^{-1}(0) is additively closed and hence a prime ideal. 3) We have a factorization P : R → R/p → C."
- p. 24–25: X̌(C) = colim_{N₀} X•(C), "We can write the points of X̌(C) in the form F_ν^{-1}P for some ν ∈ N₀ and P in X•(C). Then F_ν^{-1}P = F_{ν′}^{-1}P′ is equivalent to F_{ν′}P = F_νP′, an equality in X•(C)."
- p. 27, Definition 4.1: "A class E of characters χ : κ^× → C^× on algebraically closed fields κ is (N₀−)admissible if for any σ ∈ Autκ resp. ν ∈ N₀ the character χ is in E if and only if χ∘σ resp. χ^ν = χ∘( )^ν is in E. Moreover the characters in E should satisfy (Tors)." (Tors), same page: "the group ker(χ)_tors = ker(χ|_{μ(κ)}) is finite and |(ker χ)_tors| ∈ N₀." Proposition 4.2: "the set X•(C)_E … is G-invariant. It is foreward- and backward invariant under the N₀-action, i.e. for P ∈ X•(C) we have P ∈ X•(C)_E if and only if F_ν(P) ∈ X•(C)_E. The set X̌(C)_E = colim_{N₀} X•(C)_E ⊂ X̌(C) is G- and Q₀^{>0}-invariant." And: "Note that the maps pr_X and pr_{X₀} above extend Q₀^{>0}-equivariantly to maps pr_X : X̌(C)_E → X and pr_{X₀} : X̌₀(C)_E → X₀. Here we let Q₀^{>0} act trivially on X and X₀."
- p. 28–29: the example classes, "E_f ⊂ E_fg ⊂ E_fd ⊂ E_fd0 ⊂ E_max ⊂ E_tors."
- p. 31: "The fibres of pr_{X₀} : X̌₀(C)_{Etors} → X₀ are Q₀^{>0}-invariant. We will now analyze the structures of the Q₀^{>0}-sets C_{x₀} = pr_{X₀}^{-1}(x₀) in X̌₀(C)_{Etors} for points x₀ of X₀ whose residue field κ(x₀) is finite." … "C_{x₀} = pr₀^{-1}(x₀)Q₀^{>0} = ⋃_{ν∈N₀} F_ν^{-1} pr₀^{-1}(x₀) ⊂ X̌₀(C)_{Etors}."
- p. 32: "The group of automorphisms of the abelian group κ(x)^× is given by Ẑ×_{(p)} where Ẑ_{(p)} = ∏_{l≠p} Z_l. We have a natural inclusion N x₀^Ẑ = Gal(κ(x)/κ(x₀)) ↪ Aut(κ(x)^×) = Ẑ×_{(p)}. (34)" … "χ_x = ι∘i_x^{-1} : κ(x)^× ↪ C^×" … "(35) Ẑ×_{(p)} × N₀ ↠ S, (a, ν) ↦ χ_x·(a, ν) := χ_x∘( )^a∘( )^ν. Two elements (a, ν) and (a′, ν′) are in the same fibre of this map if and only if ν′ = νp^n and a = p^n a′ for some n ∈ Z." (S = "the set S of homomorphisms P^× : κ(x)^× → C^× with finite cyclic kernel of order in N₀".) (36): "S/N x₀^Ẑ → pr₀^{-1}(x₀), P^× mod N x₀^Ẑ ↦ π((x, P^×))."
- p. 33: "The set C_{x₀} fibres over the compact group Ẑ×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p)^, and the fibres are the Q₀^{>0}-orbits in C_{x₀}."
- p. 34, Theorem 5.2: "Let E be an admissible class with E ⊂ E_max. … {P₀ ∈ X̌₀(C)_E | (Q₀^{>0})_{P₀} ≠ 1} = ∐_{x₀} C^E_{x₀}. For any point P₀ ∈ C^E_{x₀} the isotropy group of P₀ is (Q₀^{>0})_{P₀} = N x₀^Z … If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}."
- p. 35: "The endomorphism ring of the abelian group κ(x)^× is End κ(x)^× = End(⊕_{l≠p} Q_l/Z_l) = Ẑ_{(p)}."
- p. 38, §6: "consider the suspension X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0}. It is the quotient of X̌₀(C)_E × R^{>0} by the right Q₀^{>0}-action given by (P₀, u)q = (P₀q, q^{-1}u) = (F_q(P₀), q^{-1}u) for q ∈ Q₀^{>0}." … "Γ_{x₀} = C_{x₀} ×_{Q₀^{>0}} R^{>0} ⊂ X₀. The Q₀^{>0}-bijection (39) induces an R^{>0}-bijection … → Γ_{x₀}. Thus all R^{>0}-orbits in Γ_{x₀} are circles R^{>0}/N x₀^Z and Γ_{x₀} fibres over Ẑ×_{(p)}/p^Ẑ = Aut(F̄_p)/Aut(F_p)^ with fibres the R^{>0}-orbits in Γ_{x₀}. We set Γ^E_{x₀} = C^E_{x₀} ×_{Q₀^{>0}} R^{>0} where C^E_{x₀} = C_{x₀} ∩ X̌₀(C)_E. If e.g. E_f ⊂ E then Γ^E_{x₀} = Γ_{x₀}." **No topology on X₀ is stated in §6.**
- p. 39, Theorem 6.1: "{x₀ ∈ X₀ | (R^{>0})_{x₀} ≠ 1} = ∐_{x₀} Γ^E_{x₀}. For any point x₀ ∈ Γ^E_{x₀} the isotropy group of x₀ is (R^{>0})_{x₀} = N x₀^Z." … "Any periodic orbit γ in X₀ is contained in Γ^E_{x₀} for a uniquely determined point x₀ of X₀ with finite residue field."
- p. 40, §7 opening: "We only consider integral normal schemes X₀ whose function field K₀ is countable. For brevity we call them arithmetic schemes. … C is an algebraically closed field with a valuation | | and the corresponding topology. We begin with the affine case X₀ = spec R₀ and write X = spec R. Viewing X•(C) as a set of multiplicative maps P : R → C as in Remark 3.4 we give X•(C) the topology of pointwise convergence. It is the subspace topology induced by the Tychonov topology of C^R = ∏_R C on X•(C) via the inclusion X•(C) ⊂ C^R, P ↦ (P(r))_{r∈R}. Since R is countable, X•(C) is a metrizable topological space." Lemma 7.1: "For affine arithmetic schemes X₀, the natural map pr_X : X•(C) → X, (x, P^×) ↦ x or P ↦ p = P^{-1}(0) is continuous." Proof: "A closed subset A of X has the form A = {p ⊃ I} for some ideal I in R. Consider a convergent sequence P_n → P in X•(C) where P_n ∈ pr_X^{-1}(A) for all n, i.e. p_n = P_n^{-1}(0) ⊃ I. Since P_n(r) → P(r) for all r ∈ R, it follows that P(r) = 0 for r ∈ I and hence p = P^{-1}(0) ⊃ I i.e. P ∈ pr_X^{-1}(A). Hence pr_X^{-1}(A) is closed and therefore pr_X is continuous."
- p. 41–42: for a general arithmetic scheme, "We give X•(C) the topology for which O ⊂ X•(C) is open if and only if O ∩ X′•(C) is open in X′•(C) for any X′₀" (affine open). p. 42: "We equip X•₀(C) = X•(C)/G with the quotient topology. Using Lemma 7.1 one sees that pr_X : X•(C) → X and hence also pr_{X₀} : X•₀(C) → X₀ are continuous." Lemma 7.3: "For any arithmetic scheme X₀, the group G acts by homeomorphisms on X•(C) and the injective maps F_ν : X•(C) ↪ X•(C) for ν ∈ N are continuous, closed and open. In particular F_ν(X•(C)) is closed and open in X•(C)." With (51): "F_ν(X•(C)) = {P ∈ X•(C) | P(μ_ν(K)) = 1} ⊂ X•(C)."
- p. 43: "We give X̌(C) = colim_{N₀} X•(C) the inductive limit topology. It is the finest topology such that for all ν ∈ N₀ the inclusions F_ν^{-1}|_{X•(C)} : X•(C) ↪ X̌(C) (53) are continuous. Thus Z ⊂ X̌(C) is closed, resp. open if and only if F_ν(Z) ∩ X•(C) is closed, resp. open in X•(C) for all ν ∈ N₀." Proposition 7.4: "a) X•(C) is a closed and open subspace of X̌(C). b) F_q : X̌(C) → X̌(C) is a homeomorphism for every q ∈ Q₀^{>0}. c) The group G acts by homeomorphisms on X̌(C)." Then: "We give X̌₀(C) = X̌(C)/G the quotient topology. Then X̌₀(C) is homeomorphic to colim_{N₀} X•₀(C) with the inductive limit topology. The projections π : X•(C) → X•₀(C) and π̌ : X̌(C) → X̌₀(C) are continuous and since G acts by homeomorphisms, also open. Moreover the projections pr_X : X̌(C) → X and pr_{X₀} : X̌₀(C) → X₀ are continuous."
- p. 44, Proposition 7.5: "Let X₀ be an arithmetic scheme. Then the right-action map X•(C) × G → X•(C) is continuous."
- p. 45, Corollary 7.9: "Let X₀ be an arithmetic scheme which carries an ample invertible sheaf. Then the spaces X•(C), X•₀(C), X̌(C) and X̌₀(C) are Hausdorff."
- p. 46, Theorem 7.10 (continuous bijections into "X₀ = X̌₀(C)_{Etors} ×_{Q₀^{>0}} R^{>0}"); p. 47, Remark 2: "The continuous bijections in Theorem 7.10 are not homeomorphisms in general."
- p. 47: "Given an admissible class E as in Definition 4.1 we equip X•(C)_E and X•₀(C)_E with the subspace topologies of X•(C) and X•₀(C). Equip X•(C)_E/G with the quotient topology. It is clear that the natural bijection X•(C)_E/G → X•₀(C)_E is continuous. It is also open since G acts by homeomorphisms and hence we may identify X•(C)_E/G and X•₀(C)_E as topological spaces. We give X̌(C)_E = colim_{N₀} X•(C)_E and X̌₀(C)_E = colim_{N₀} X•₀(C)_E the inductive limit topologies. They agree with the subspace topologies via X̌(C)_E ⊂ X̌(C) and X̌₀(C)_E ⊂ X̌₀(C) because the subspaces F_ν^{-1}X•(C) and F_ν^{-1}X•₀(C) are open in X̌(C) resp. X̌₀(C) for all ν ∈ N₀. As above, the natural continuous bijection X̌(C)_E/G → X̌₀(C)_E is a homeomorphism. All preceding results in this section remain true if we replace X•(C) etc. by X•(C)_E etc."
- p. 49: "The Q^{>0}-action on Ȟ_{Etors} × R^{>0} is not properly discontinuous. In section 10, we will see that this works to our advantage." §8 opening: "the dynamical system Y₀ obtained as the topological closure of the union of all periodic orbits coming from closed points of X₀."
- p. 54, Theorem 9.2: "the fibres of X̌(C)_{Ef} and X̌₀(C)_{Ef} over η resp. η₀ are dense in X̌(C)′ resp. X̌₀(C)′." p. 62, Corollary 9.7 and its proof: "By Theorem 9.6 the spaces X_η and X₀_{η₀} are connected. By Theorem 9.2 they are dense in X resp. X₀. Hence X and X₀ are connected as well."
- p. 63, §10: "Consider the projection: π : X̃ = M × R^{>0} → X = M ×_Q R^{>0}. … R_X = (π_* R_X̃)^Q ⊂ (π_* C⁰_X̃)^Q = C⁰_X. … Note that in general the continuous bijection π|_{M×{u}} : M × {u} → π(M × {u}) will not be a homeomorphism if π(M × {u}) is equipped with the subspace topology of X. If Q acts properly discontinuously on M × R^{>0} and if M is a manifold, then F is an actual 1-codimensional foliation."

**[x-06] Deninger, arXiv:2301.11643** (`fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`). p. 11: "Set X₀ = (X̌₀(C) × R^{>0})/Q^{>0} where Q^{>0} acts diagonally. Let t ∈ R act on X₀ by setting φ^t[P, u] = [P, e^t u]." p. 12, Theorem 4.2's text: "The compact subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log N x₀ … and they are pairwise disjoint. In fact Γ_{x₀} is a fibre space over the compact group Aut(F̄_p)/Aut(F_p)^ where p = char κ(x) with fibres the compact orbits in Γ_{x₀}." (Compactness of Γ_{x₀} asserted, not proved, in this survey.)

**[r3s-08] Morishita, arXiv:2508.15971v5** (`fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`). p. 13: "we equip Ẋ_K(C) ≃ Ẋ_Q(C)/Gal(Q̄/K) the quotient topology"; "X̌_K(C) := lim_→ Ẋ_K(C) equipped with the inductive limit topology." p. 14: "(2.2.1) X_K := X̌_K(C) ×_{Q+} R+. … We equip X_K twith he quotient topology of the product X̌_K(C) × R+." (transposition in the source). p. 15: "C_p := p̌r_K^{-1}(p) = ⋃_{n∈N} F_n^{-1}(ṗr_K^{-1}(p)) … Γ_p := C_p ×_{Q+} R+ ⊂ X_K." pp. 16–18: Theorems 2.2.8 and 2.2.9 assert "homeomorphism" for Ẑ×_{(p)}/Np^Ẑ ×_{p^Z} R+ → Γ_p and (2.2.9(2)) "the decomposition into connected closed R+-orbits Γ_p = ⊔ γ_{p,a}" — cited only as the note's §3.3 caution; nothing below uses them.

**[D25] Deninger, arXiv:2508.05329v1** (`fetched-r3/r3s-22-...-SESSION8-FETCH.pdf`). p. 1 (abstract/intro) read; full-text grep for "suspension", "packet", "Hausdorff", "closure", "quotient topology", "periodic orbit": no hits. The paper concerns sheaf properties of W_rat(O) in Grothendieck topologies and contains nothing bearing on the topology of the suspension or the packets. Not used.

**Program files read in full:** `results/c3-r/probe-9.3-adjudication.md`; `results/c3-r/probe-9.3-b.md` (all 169 lines, including the Session-14 blocks); `results/corpus-routing.md` header caveats 1–20 (none of the caveats touches the four PDFs above; all four have clean text layers).

---

## 3. The topology, settled from the sources (assignment items 1 and 2)

### 3.1 The chart: X•(C) for X₀ = Spec Z

X₀ = Spec Z is affine, X = Spec Z̄ (normalization of Z in Q̄), R = Z̄, countable. By p. 40 (quoted), X•(C) is the set of multiplicative maps P : Z̄ → C of Remark 3.4 with the **topology of pointwise convergence**, i.e. the subspace topology of the product C^{Z̄}. Consequences used below: X•(C) is Hausdorff (C is a valued field, products and subspaces of Hausdorff spaces are Hausdorff) and metrizable (p. 40). The affine description applies directly; the glued description of pp. 41–42 is not needed for Spec Z.

**Pointwise convergence at a characteristic-p point.** For x over (p) the residue field is κ(x) = F̄_p, κ(x)^× = μ^{(p)} (prime-to-p roots of unity), and every r ∈ Z̄ ∖ p_x has image r̄ of finite order m prime to p. A point (x, P^×) is the multiplicative map r ↦ 0 on p_x, r ↦ P^×(r̄) otherwise. Thus a net (x, P_α^×) at the **fixed** x converges pointwise to (x, P^×) iff P_α^×(ζ) → P^×(ζ) for every ζ ∈ μ^{(p)} — a condition modulo each finite level μ_M, M prime to p. This is the note's "pointwise evaluation"; on the fixed-x, chart-1 stratum it is exactly the right description. (Nets whose x varies are a different matter and are handled by the Galois step 4.2(R3) and by Lemma 7.1, not by pointwise evaluation at one x.)

### 3.2 The Galois quotient X•₀(C) = X•(C)/G

Quotient topology (p. 42). G = Gal(Q̄/Q) is compact, acts by homeomorphisms (Lemma 7.3), the action map X•(C) × G → X•(C) is jointly continuous (Prop. 7.5), and π : X•(C) → X•₀(C) is **open** (p. 43). X•₀(C) is metrizable, hence Hausdorff (Cor. 7.8; Spec Z affine).

### 3.3 The colimit X̌(C), X̌₀(C): is the colimit topology "finer than pointwise"?

By p. 43 (quoted), X̌(C) carries the **inductive limit topology**: Z ⊂ X̌(C) is open (closed) iff F_ν(Z) ∩ X•(C) is open (closed) in X•(C) for every ν. By Prop. 7.4(a) the chart X•(C) is **closed and open** in X̌(C); by Prop. 7.4(b) each F_ν is a homeomorphism of X̌(C); hence every chart

  U_ν := F_ν^{-1}(X•(C)) ⊂ X̌(C)  (ν ∈ N)

is open and closed in X̌(C), and F_ν : U_ν → X•(C) is a homeomorphism (restriction of a homeomorphism of X̌(C) to a subspace and its image). The charts are nested (U_ν ⊂ U_{νμ}) and cover X̌(C) (p. 24: every point is F_ν^{-1}P).

**Answer to assignment item (2).** The colimit topology is *not* finer than the pointwise topology on any chart: **on each chart it is the pointwise topology, transported by F_ν.** What the colimit topology does — and this is the only sense in which it is "finer" than a naive pointwise topology on characters of lim_← κ(x)^× (p. 25, (29)) — is to make each chart clopen, so that no net can converge to a point of U_ν without eventually lying in U_ν, and no net inside a chart can converge to a point outside it. The general closure formula that encodes this is elementary and is used repeatedly below:

> **(L1) Closure is local on open sets.** If U ⊂ Y is open and A ⊂ Y, then cl_Y(A) ∩ U = cl_U(A ∩ U). *Proof.* ⊇: cl_U(A ∩ U) ⊂ cl_Y(A ∩ U) ⊂ cl_Y(A), and it lies in U. ⊆: if z ∈ cl_Y(A) ∩ U and V ∋ z is open in U (hence in Y), then V ∩ A ≠ ∅ and V ∩ A ⊂ A ∩ U. ∎

So for any A ⊂ X̌(C): cl_{X̌(C)}(A) = ⋃_ν (cl(A) ∩ U_ν) = ⋃_ν cl_{U_ν}(A ∩ U_ν) = ⋃_ν F_ν^{-1}(cl_{X•(C)}(F_ν(A ∩ U_ν))). The feared failure mode of the assignment — "a subnet limit could exist pointwise but not in X₀, or conversely" — does not occur: for a set A contained in the closed chart X•(C) = U₁, cl_{X̌(C)}(A) = cl_{X•(C)}(A), computed pointwise. The genuine subtlety is different and is addressed in §4.2(R2): the orbit O(P₀) = {F_r P₀ : r ∈ Q^{>0}} is **not** contained in one chart, and its closure must be assembled chart by chart.

The same holds downstairs: X̌₀(C) = X̌(C)/G with the quotient topology is homeomorphic to colim X•₀(C) (p. 43); π̌ is open (p. 43), so the images π̌(U_ν) = F_ν^{-1}(X•₀(C)) are open, and (being G-saturated with G-saturated complement) closed as well — this is the sentence on p. 47, "the subspaces F_ν^{-1}X•(C) and F_ν^{-1}X•₀(C) are open in X̌(C) resp. X̌₀(C)". X̌₀(C) is Hausdorff (Cor. 7.9, Spec Z affine).

### 3.4 The E-subspaces

By p. 47 (quoted): X•(C)_E and X•₀(C)_E carry the subspace topologies; the inductive limit topologies on X̌(C)_E, X̌₀(C)_E **agree with the subspace topologies** inside X̌(C), X̌₀(C). I re-derived the "agree" claim, since it is load-bearing: (subspace ⟹ inductive) if Z = W ∩ X̌₀(C)_E with W open, then F_ν(Z) ∩ X•₀(C)_E = F_ν(W) ∩ X•₀(C)_E is open in X•₀(C)_E because F_ν(X̌₀(C)_E) = X̌₀(C)_E (Prop. 4.2); (inductive ⟹ subspace) if Z is inductively open, put V_ν := an open subset of X•₀(C) with V_ν ∩ X•₀(C)_E = F_ν(Z) ∩ X•₀(C)_E, and W := ⋃_ν F_ν^{-1}(V_ν), open in X̌₀(C) since the charts are open and F_ν is a homeomorphism; then W ∩ X̌₀(C)_E = ⋃_ν F_ν^{-1}(V_ν ∩ X•₀(C)_E) = ⋃_ν (Z ∩ F_ν^{-1}(X•₀(C)_E)) = Z, using X̌₀(C)_E ∩ X•₀(C) = X•₀(C)_E (backward invariance, Prop. 4.2). ✓ In particular the E-charts U^E_ν := F_ν^{-1}(X•₀(C)_E) = U_ν ∩ X̌₀(C)_E are open in X̌₀(C)_E, cover it, and are homeomorphic via F_ν to X•₀(C)_E; **closures in the E-spaces are closures in the ambient spaces intersected with the E-locus.**

### 3.5 The suspension X₀ and its topology (assignment item 1)

[x-03] §6 (p. 38, quoted) defines X₀ = X̌₀(C)_E ×_{Q₀^{>0}} R^{>0} as a quotient **set** and says nothing about its topology; §7 stops at X̌₀(C). The topology on X₀ is nevertheless fixed by the sources beyond reasonable doubt as the **quotient topology** of q : X̌₀(C)_E × R^{>0} → X₀:

- [x-03] §10 p. 63 (quoted) treats X = M ×_Q R^{>0} as a topological space with π : X̃ → X and identifies C⁰_X = (π_* C⁰_X̃)^Q — continuous functions on an open U ⊂ X are exactly the Q-invariant continuous functions on π^{-1}(U). This identity holds for the quotient topology (π^{-1}(U) → U is a quotient map for U open, since π is open — Q acts by homeomorphisms) and fails for any strictly coarser topology that fewer invariant continuous functions would detect; the remark on the same page that π|_{M×{u}} "will not be a homeomorphism if π(M × {u}) is equipped with the subspace topology of X" and the proviso "If Q acts properly discontinuously" are the standard quotient-topology caveats.
- [x-03] Theorem 7.10 (p. 46) speaks of continuous bijections **into** X₀ and its Remark 2 (p. 47) of the fibre over η being connected — statements about a topology on X₀ that can only be the quotient topology (continuity of a map X•₀(C)_{p,in} ×_{p^Z} R^{>0} → X₀ is obtained by composing with q).
- [x-03] §8 (p. 49) speaks of "the topological closure of the union of all periodic orbits" in X₀.
- [x-06] p. 11 (quoted): "Set X₀ = (X̌₀(C) × R^{>0})/Q^{>0} where Q^{>0} acts diagonally."
- [r3s-08] p. 14 (quoted): "We equip X_K [with the] quotient topology of the product X̌_K(C) × R+."

I adopt the quotient topology as the topology of X₀. Two properties of q, both used below: **q is open** (Q^{>0} acts on X̌₀(C)_E × R^{>0} by the homeomorphisms (P, u) ↦ (F_q P, q^{-1}u) — Prop. 7.4(b) restricted to the invariant subspace X̌₀(C)_E, times a dilation of R^{>0}; for a group acting by homeomorphisms, q^{-1}(q(U)) = ⋃_g U·g is open, so q(U) is open in the quotient topology); and **q is not assumed proper**, X₀ is **not** assumed Hausdorff (it is not: Cor. A.2, adjudication §3). Nothing below uses Hausdorffness of X₀.

> **(L2) Closures through an open continuous surjection.** If f : Y → Z is continuous, open and surjective and A ⊂ Z, then f^{-1}(cl A) = cl(f^{-1}A); consequently cl(A) = f(cl(f^{-1}A)). *Proof.* f^{-1}(cl A) is closed and contains f^{-1}A, so ⊇. If z ∉ cl(f^{-1}A), choose an open U ∋ z with U ∩ f^{-1}A = ∅; f(U) is open, contains f(z), and f(U) ∩ A = ∅ (a point f(u) ∈ A would put u ∈ U ∩ f^{-1}A); so f(z) ∉ cl A, i.e. z ∉ f^{-1}(cl A). ∎

### 3.6 The projection to the scheme

pr_X : X•(C) → X is continuous for affine X₀ (Lemma 7.1, p. 40; the proof, quoted in §2, uses only that the closed sets of Spec R are the {p ⊃ I} and pointwise convergence); pr_{X₀} : X•₀(C) → X₀ is continuous (p. 42: pr_{X₀}∘π = π_scheme∘pr_X is continuous and π is a quotient map); pr_X : X̌(C) → X and pr_{X₀} : X̌₀(C) → X₀ are continuous (p. 43: pr_X∘F_ν^{-1}|_{X•(C)} = pr_X, and π̌ is a quotient map); the restrictions to the E-subspaces are continuous (subspace topology, p. 47). By p. 27 (quoted) these maps are Q₀^{>0}-invariant: pr_{X₀}(F_q P) = pr_{X₀}(P). For X₀ = Spec Z the Zariski closed points are the (p) and the generic point (0) is not closed.

---

## 4. Line-by-line re-derivation of the converse inclusion

Throughout: X₀ = Spec Z, C = ℂ (only the facts that C is an algebraically closed valued field with μ(Q̄) ↪ C^× are used), N₀ = ℕ, E admissible (Def. 4.1), X₀ = X̌₀(C)_E ×_{Q^{>0}} R^{>0} with the quotient topology (§3.5). Fix a prime p, a point x ∈ X = Spec Z̄ over (p), the injective reference character χ := χ_x : κ(x)^× = μ^{(p)} ↪ C^× (p. 32), and write χ^c := χ∘( )^c for c ∈ Ẑ_{(p)} = End(μ^{(p)}) (p. 35). Under Remark 3.4, (x, χ^c) is the multiplicative map Z̄ → C, r ↦ 0 for r ∈ p_x, r ↦ χ(r̄)^c otherwise, where for r̄ of finite order m (prime to p) the symbol χ(r̄)^c means χ(r̄)^{c mod m}.

### 4.0 Normalization of the orbit (the note's Step 1, checked)

Let γ ⊂ Γ^E_p be a periodic orbit. By definition (p. 38) γ = q({P₀′} × R^{>0}) for some P₀′ ∈ C^E_{x₀} = C_{x₀} ∩ X̌₀(C)_E. By (38) (p. 32) P₀′ = F_r π(x, χ^a) with a ∈ Ẑ×_{(p)} and r ∈ Q^{>0}. Put P₀ := F_{r^{-1}}P₀′ = π(x, χ^a). Then q({P₀} × R^{>0}) = q({F_r P₀} × R^{>0}) = γ, since [F_r P₀, w] = [P₀, rw]; and P₀ ∈ X̌₀(C)_E (Q^{>0}-invariance, Prop. 4.2) ∩ X•₀(C) = X•₀(C)_E (backward invariance). So **WLOG γ = q({P₀} × R^{>0}) with P₀ = π(x, χ^{a₀}), a₀ ∈ Ẑ×_{(p)}, χ^{a₀} ∈ E.** ✓ Also F_p P₀ = P₀ in X•₀(C) (Thm 5.2: isotropy N x₀^Z = p^Z; concretely χ^{a₀ p} = χ^{a₀}∘Frob and Frob ∈ Gal(κ(x)/F_p) is induced by some σ ∈ G_x by (23)/(34)).

Write O(P₀) := {F_r P₀ : r ∈ Q^{>0}} ⊂ X̌₀(C)_E (the Q^{>0}-orbit) and S := {F_n P₀ : n ∈ ℕ} = {π(x, χ^{a₀ n}) : n ∈ ℕ} ⊂ X•₀(C)_E (Prop. 4.2), S̃ := {(x, χ^{a₀ n}) : n ∈ ℕ} ⊂ X•(C)_E.

### 4.1 Route I — the packet is a fiber of a continuous flow-invariant map (any arithmetic scheme)

**Proposition I.** Let X₀ be any arithmetic scheme, E admissible, x₀ ∈ X₀ with finite residue field. Then Γ^E_{x₀} is closed in X₀ and flow-invariant. Hence cl_{X₀}(γ) ⊆ Γ^E_{x₀} for every periodic orbit γ ⊂ Γ^E_{x₀}.

*Proof.* (I-1) The composite X̌₀(C)_E × R^{>0} → X̌₀(C)_E → X₀, (P, u) ↦ pr_{X₀}(P), is continuous (§3.6) and constant on Q^{>0}-orbits, since pr_{X₀}(F_q P) = pr_{X₀}(P) (p. 27). By the universal property of the quotient topology it descends to a continuous map

  Π : X₀ → X₀ (the scheme), Π[P, u] = pr_{X₀}(P).

Since φ^t[P, u] = [P, ue^t], Π∘φ^t = Π; every fiber of Π is flow-invariant.

(I-2) Π^{-1}(x₀) = q((pr_{X₀}^{-1}(x₀) ∩ X̌₀(C)_E) × R^{>0}). By p. 31 (quoted), C_{x₀} = pr_{X₀}^{-1}(x₀) inside X̌₀(C)_{Etors}; since E ⊂ E_tors (Def. 4.1 imposes (Tors)), X̌₀(C)_E ⊂ X̌₀(C)_{Etors} and C^E_{x₀} = C_{x₀} ∩ X̌₀(C)_E = pr_{X₀}^{-1}(x₀) ∩ X̌₀(C)_E. Hence Π^{-1}(x₀) = q(C^E_{x₀} × R^{>0}) = Γ^E_{x₀} (definition, p. 38). [Consistency: p. 31 also writes C_{x₀} = ⋃_ν F_ν^{-1}pr₀^{-1}(x₀); a point F_ν^{-1}Q lies in pr_{X₀}^{-1}(x₀) iff pr₀(Q) = x₀, which is the same set.]

(I-3) x₀ is a closed point of X₀. In an affine open Spec A ∋ x₀ with x₀ = 𝔭, the domain A/𝔭 embeds in the finite field κ(x₀), hence is a finite domain, hence a field; so 𝔭 is maximal and {x₀} is closed in Spec A. If y ∈ cl_{X₀}{x₀}, every affine open V ∋ y meets {x₀}, so x₀ ∈ V and y ∈ cl_V{x₀} = {x₀}. (For Spec Z this is just: (p) is a maximal ideal.)

(I-4) Γ^E_{x₀} = Π^{-1}(x₀) is the preimage of a closed set under a continuous map, hence closed; it is flow-invariant by (I-1). A closed set containing γ contains cl(γ). ∎

*Equivalent one-liner.* Under the quotient topology, Γ^E_{x₀} is closed in X₀ iff q^{-1}(Γ^E_{x₀}) = C^E_{x₀} × R^{>0} is closed in X̌₀(C)_E × R^{>0}; and C^E_{x₀} = pr_{X₀}^{-1}(x₀) ∩ X̌₀(C)_E is closed in X̌₀(C)_E as the preimage of the closed point x₀ under the continuous pr_{X₀}. Same content, no Π needed.

**Consequences (assignment item 4).** Since Γ^E_{x₀} = Π^{-1}(x₀) and the fibers of Π are disjoint, cl(γ) ⊂ Π^{-1}((p)) meets neither Π^{-1}((0)) (the generic stratum) nor Π^{-1}((ℓ)) for ℓ ≠ p (any other packet, and — for classes E ⊂ E_tors on schemes with non-closed positive-characteristic points, cf. Thm 5.5 — any other fiber whatever). This is a global statement about X₀ with its quotient topology, not a chart statement.

**With Theorem A** (⊇, banked): for X₀ = Spec Z, cl_{X₀}(γ) = Γ^E_p. Route I proves ⊆ by itself; it does not re-prove ⊇.

### 4.2 Route II — the explicit chart-by-chart computation (X₀ = Spec Z), proving both inclusions at once

**(R1) Reduce from X₀ to X̌₀(C)_E.** q^{-1}(γ) = q^{-1}(q({P₀} × R^{>0})) = ⋃_{r∈Q^{>0}} ({P₀} × R^{>0})·r = ⋃_r {F_r P₀} × r^{-1}R^{>0} = O(P₀) × R^{>0}. By (L2) with f = q (open, continuous, surjective, §3.5):

  cl_{X₀}(γ) = q(cl(O(P₀) × R^{>0})) = q(cl_{X̌₀(C)_E}(O(P₀)) × R^{>0}),

using that the closure of a product of subsets in a product space is the product of the closures. ✓

**(R2) Reduce from the colimit to chart 1.** The E-charts U^E_ν = F_ν^{-1}(X•₀(C)_E) are open in X̌₀(C)_E and cover it (§3.4). By (L1), cl(O(P₀)) = ⋃_ν cl_{U^E_ν}(O(P₀) ∩ U^E_ν), and F_ν : U^E_ν → X•₀(C)_E is a homeomorphism with F_ν(O(P₀) ∩ U^E_ν) = O(P₀) ∩ X•₀(C)_E (O(P₀) is Q^{>0}-stable). So

  cl_{X̌₀(C)_E}(O(P₀)) = ⋃_ν F_ν^{-1}( cl_{X•₀(C)_E}(O(P₀) ∩ X•₀(C)_E) ).

*Which orbit points lie in chart 1?* Let r = m/m′ ∈ Q^{>0} in lowest terms and write m′ = p^k m′_p with p ∤ m′_p. Then F_r P₀ = F_{m/m′_p}(F_{p^k}^{-1}P₀) = F_{m/m′_p}P₀ (F_p P₀ = P₀). By p. 24–25, F_{m′_p}^{-1}F_m P₀ ∈ X•₀(C) iff F_m P₀ ∈ F_{m′_p}(X•₀(C)). Since F commutes with G, F_{m′_p}(X•₀(C)) = π(F_{m′_p}(X•(C))), and π(Q̃) ∈ π(F_{m′_p}X•(C)) iff Q̃^σ ∈ F_{m′_p}X•(C) for some σ ∈ G iff (by (51), p. 42, applicable because Z̄ is integrally closed with algebraically closed fraction field, so Lemma 4.6's hypotheses hold) Q̃(σμ_{m′_p}(Q̄)) = Q̃(μ_{m′_p}(Q̄)) = 1. For Q̃ = (x, χ^{a₀ m}): the image of μ_{m′_p}(Q̄) in κ(x)^× is μ_{m′_p}(F̄_p) (reduction is injective on prime-to-p roots of unity, (32)), and χ^{a₀ m} kills it iff ( )^{m} kills μ_{m′_p} (a₀ is a unit, χ injective) iff m′_p | m iff m′_p = 1 (gcd(m, m′) = 1). Hence

  O(P₀) ∩ X•₀(C)_E = {F_{m/p^k}P₀} = {F_m P₀ : m ∈ ℕ} = S,  and O(P₀) ∩ U^E_ν = F_ν^{-1}(S),

so **cl(O(P₀)) = ⋃_ν F_ν^{-1}(cl_{X•₀(C)_E}(S)).** ✓ (Sanity check C3 in the companion script: the chart-1 criterion "prime-to-p part of the denominator is 1" verified for all coprime m, m′ < 60.)

**(R3) Reduce from X•₀(C) to X•(C) at the fixed x (the Galois step).** π : X•(C) → X•₀(C) is open (p. 43), so by (L2), cl_{X•₀(C)}(S) = π(cl(π^{-1}S)), and π^{-1}(S) = S̃·G.

> **(L3) Saturation of a closed set under a compact group is closed.** Let a compact group G act on a space Y with jointly continuous action map α : Y × G → Y, and A ⊂ Y closed. Then A·G = pr_Y(α^{-1}(A)) (z ∈ A·G iff z·h ∈ A for some h iff (z, h) ∈ α^{-1}(A)); α^{-1}(A) is closed and pr_Y : Y × G → Y is a closed map because G is compact (tube lemma). So A·G is closed. ∎

Apply (L3) with Y = X•(C), Prop. 7.5 (joint continuity), G profinite: cl(S̃)·G is closed and contains S̃·G, so cl(S̃·G) ⊂ cl(S̃)·G; conversely each right translation is a homeomorphism, so cl(S̃)·g = cl(S̃·g) ⊂ cl(S̃·G). Hence cl(S̃·G) = cl(S̃)·G and

  cl_{X•₀(C)}(S) = π(cl_{X•(C)}(S̃)),  cl_{X•₀(C)_E}(S) = π(cl_{X•(C)}(S̃)) ∩ X•₀(C)_E  (subspace topology, §3.4). ✓

**(R4) The closure of S̃ in X•(C): a copy of Ẑ_{(p)}.** Define β : Ẑ_{(p)} → X•(C), b ↦ (x, χ^{a₀ b}). It lands in X•(C) (any homomorphism κ(x)^× → C^× is allowed there; χ^{a₀b} is one, as a₀b ∈ End μ^{(p)}). It is **continuous**: in the coordinate r ∈ p_x the value is the constant 0; in a coordinate r ∉ p_x with r̄ of order m (prime to p) the value χ(r̄)^{a₀ b} depends only on b mod m, and Ẑ_{(p)} → Z/m is continuous — so every coordinate is locally constant in b, and a map into a product is continuous iff each coordinate is. It is **injective**: χ^{a₀b} = χ^{a₀b′} ⟹ y^{a₀(b−b′)} = 1 for all y ∈ μ^{(p)} (χ injective) ⟹ the endomorphism a₀(b − b′) of μ^{(p)} is 0 ⟹ a₀(b − b′) = 0 in Ẑ_{(p)} = End μ^{(p)} (faithful: c acts as 0 iff c ≡ 0 mod every m prime to p iff c = 0) ⟹ b = b′ (a₀ a unit). Ẑ_{(p)} is compact and X•(C) is Hausdorff (§3.1), so β is a homeomorphism onto its image K := β(Ẑ_{(p)}), which is compact, hence **closed** in X•(C). ℕ is dense in Ẑ_{(p)} = lim_← Z/M (M prime to p): a basic open set is a residue class mod M, and every residue class mod M contains a positive integer (CRT; check C1). Therefore

  cl_{X•(C)}(S̃) = cl(β(ℕ)) ⊇ β(cl ℕ) = β(Ẑ_{(p)}) = K ⊇ cl(S̃)  (S̃ ⊂ K closed),  i.e. **cl_{X•(C)}(S̃) = K = {(x, χ^{a₀ b}) : b ∈ Ẑ_{(p)}}.** ✓

This is the precise content of the note's "every limit of {F_n(P₀)} along any subnet is P₀^b for some b ∈ Ẑ_{(p)}, by compactness of Ẑ_{(p)} and the same pointwise evaluation" — correct **for S̃ in X•(C)**, at the fixed x. Note that no sequences or subnets are needed: the statement is about closures.

**(R5) Which points of K are in the space at all — the exact (Tors) criterion.** For b ∈ Ẑ_{(p)} with components b_ℓ ∈ Z_ℓ (ℓ ≠ p), the kernel of χ^{a₀b} on μ(κ(x)) = μ^{(p)} = ⊕_{ℓ≠p} μ_{ℓ^∞} is the kernel of the endomorphism a₀b, which is ⊕_{ℓ≠p} μ_{ℓ^∞}[a₀_ℓ b_ℓ], and μ_{ℓ^∞}[c] = μ_{ℓ^{v_ℓ(c)}} for c ≠ 0, = μ_{ℓ^∞} for c = 0. Hence

  ker(χ^{a₀b}|_{μ(κ(x))}) is finite ⟺ every b_ℓ ≠ 0 **and** v_ℓ(b_ℓ) = 0 for all but finitely many ℓ ⟺ b ∈ ℕ·Ẑ×_{(p)}

(write b = n·u with n = ∏ ℓ^{v_ℓ(b_ℓ)} ∈ ℕ, p ∤ n, and u a unit). When it is finite it is cyclic of order n ∈ ℕ = N₀, so (Tors) holds. **(Tors) is therefore violated in two ways, not one:** (i) some b_ℓ = 0 (the note's case: "kill a μ_{ℓ^∞}"); (ii) all b_ℓ ≠ 0 but infinitely many are non-units (e.g. b = (ℓ)_{ℓ≠p}, or any b with b_ℓ ∈ ℓZ_ℓ for infinitely many ℓ), where the kernel ⊕_ℓ μ_{ℓ^{v_ℓ}} is infinite though every summand is finite. Check C2 exhibits the three regimes at finite level (kernel size gcd(b, M) along M = ∏_{ℓ≤L, ℓ≠p} ℓ^L: stable at 6 for b = 6; 8, 32, 128, 2048 for a zero 2-component; 6, 6, 42, 462 for b = ∏ℓ, unbounded with no zero component).

The points of K that satisfy (Tors) are exactly {(x, χ^{a₀ n u})} = {(x, χ^{a ν})}_{(a,ν) ∈ Ẑ×_{(p)} × ℕ}, i.e. by (35)–(36) (p. 32) **all** (Tors)-characters at x — that is K ∩ X•(C)_{Etors} = pr_X^{-1}(x) ∩ X•(C)_{Etors}. Consequently, for our admissible E ⊂ E_tors,

  π(K) ∩ X•₀(C)_E = pr₀^{-1}(x₀) ∩ X•₀(C)_E.

(⊆ is clear. ⊇: a point of pr₀^{-1}(x₀) ∩ X•₀(C)_E is a G-orbit of E-points over x₀; G is transitive on the points over x₀ (p. 32), so the orbit contains a point (x, Q) at our x, and (x, Q) ∈ X•(C)_E by G-invariance of the E-locus (Prop. 4.2); Q satisfies (Tors), so by (35) Q = χ^{aν} = χ^{a₀ b} with b = a₀^{-1}aν ∈ Ẑ_{(p)}, i.e. (x, Q) ∈ K.) Combining with (R3):

  **cl_{X•₀(C)_E}(S) = π(K) ∩ X•₀(C)_E = pr₀^{-1}(x₀) ∩ X•₀(C)_E.** ✓

The excluded b — (i) and (ii) above — are genuine points of Deninger's un-cut X•(C) and genuine limit points of S̃ there; they are absent from X•(C)_E for **every** admissible E, by (Tors) alone; and since the E-spaces carry the subspace topology, "absent from the space" is exactly what removes them from the closure computed in X•₀(C)_E. This answers assignment item (3): the exclusion is by (Tors) (a property of the class E, forced by Def. 4.1), not by the topology; it matters only in the sense that if one worked in the un-cut suspension the equality would be false (§5.1).

**(R6) Assemble.** By (R2) and (R5),

  cl_{X̌₀(C)_E}(O(P₀)) = ⋃_ν F_ν^{-1}(pr₀^{-1}(x₀) ∩ X•₀(C)_E) = (⋃_ν F_ν^{-1}pr₀^{-1}(x₀)) ∩ X̌₀(C)_E = C_{x₀} ∩ X̌₀(C)_E = C^E_{x₀},

using F_ν^{-1}(A ∩ X•₀(C)_E) = F_ν^{-1}(A) ∩ F_ν^{-1}(X•₀(C)_E) and F_ν^{-1}(X•₀(C)_E) = F_ν^{-1}(X•₀(C)) ∩ X̌₀(C)_E (backward invariance, Prop. 4.2), and C_{x₀} = ⋃_ν F_ν^{-1}pr₀^{-1}(x₀) (p. 31). By (R1),

  **cl_{X₀}(γ) = q(C^E_{x₀} × R^{>0}) = Γ^E_p.** ∎

Both inclusions are obtained at once; in particular Route II independently re-derives Theorem A's ⊇ (the fourth derivation of it), and it shows that the equality holds **verbatim in every chart** (the closure in the colimit is the union over ν of the chart closures F_ν^{-1}(pr₀^{-1}(x₀)_E)), which settles the note's §7 Q-c affirmatively.

### 4.3 What is established, and its exact scope (assignment item 5)

1. **Closedness of packets — every arithmetic scheme, every admissible E, every x₀ with finite residue field** (Route I). Uses: Lemma 7.1 / pp. 42–43 / p. 47 (continuity of pr_{X₀} on X̌₀(C)_E), p. 27 (Q^{>0}-invariance), p. 31 (C_{x₀} = pr_{X₀}^{-1}(x₀)), Def. 4.1 (E ⊂ E_tors), the quotient topology on X₀. Does **not** use Theorem A, Hausdorffness of anything, C = ℂ, or X₀ = Spec Z.
2. **Equality cl_{X₀}(γ) = Γ^E_p — X₀ = Spec Z, C = ℂ (any algebraically closed valued C with the standing conditions would do), N₀ = ℕ, every admissible E, every periodic orbit γ ⊂ Γ^E_p**, in the quotient topology of X₀, chart by chart and globally (Route II, or Route I + Theorem A). For E ⊉ E_f the packet Γ^E_p may be smaller than Γ_p (Thm 5.2); the equality is with the E-packet, as it must be — e.g. for probe A's one-orbit cut classes it reads cl(γ) = γ.
3. **What is not established here and is not claimed:** compactness of Γ^E_p for E ⊉ E_f; Hausdorffness of Γ^E_p in its subspace topology (it is non-Hausdorff for E with ≥ 2 base classes E-realized — Cor. A.2, adjudication §3 — and the closedness proved here does not conflict with that: a closed subspace of a non-Hausdorff space may be non-Hausdorff); anything about the mapping face Q-b or the compact-non-closed face Q-a of Q*, which closedness of packets does not constrain (compact non-closed invariant subspaces and continuous equivariant images are untouched by the closedness of Γ^E_p).

---

## 5. Break attempts (all failed; each pins down a hypothesis)

**5.1 Drop (Tors) — the un-cut suspension.** In X₀^{uncut} := X̌₀(C) ×_{Q^{>0}} R^{>0} (no class E), (R1)–(R4) go through unchanged and (R5) becomes cl_{X•₀(C)}(S) = π(K); so cl(γ) = q((⋃_ν F_ν^{-1}π(K)) × R^{>0}) ⊋ Γ_p. Concretely, with n_k := ∏_{ℓ≤k, ℓ≠p} ℓ^k one has n_k → 0 in Ẑ_{(p)} (v_ℓ(n_k) = k for k ≥ ℓ; check C4), so F_{n_k}P₀ → π(x, 1), the trivial character at x, and [π(x, 1), u] ∈ cl(γ); this point has Q^{>0}-isotropy all of Q^{>0} — a fixed point of the flow — and is not in Γ_p. **So the equality fails without (Tors); (Tors), which every admissible E carries, is exactly what is needed.** This also confirms that the note's original exclusion sentence, though incomplete, pointed at the right hypothesis.

**5.2 Weaken the topology on X₀.** Route I needs the continuity of Π, i.e. that X₀ carries a topology at least as fine as the quotient topology on the relevant preimages; Route II needs q open, i.e. the quotient topology. If X₀ carried a strictly coarser topology, Γ^E_p could fail to be closed. This is not an escape: the quotient topology is the sourced reading (§3.5) and the only one under which [x-03] §§7–10 and [r3s-08] §2.2 make sense. Recorded as the one hypothesis a reader must accept.

**5.3 Subnets with unbounded denominators.** Could a net F_{r_α}P₀ with r_α = m_α/m′_α, m′_α → ∞ in the prime-to-p sense, converge in X̌₀(C)_E to a point outside C^E_{x₀}? No: any limit lies in some open chart U^E_ν, so the net is eventually in U^E_ν, which forces m′_{α,p} | ν eventually ((R2)), contradicting unboundedness. And a net inside one chart cannot leave it (charts are closed). This is the "colimit finer than pointwise" worry of the assignment, and it is harmless by (L1).

**5.4 Galois-created limit points.** Could cl(π(S̃)) contain π-images of limits of nets (x^{σ_α}, χ^{a₀n_α}∘σ_α) with σ_α not eventually constant — points not of the form π(x, χ^{a₀b})? No: (L3) gives cl(S̃·G) = cl(S̃)·G = K·G, and π(K·G) = π(K). The compactness of G and the joint continuity of the action (Prop. 7.5) are what is used; without joint continuity this step would be a genuine gap.

**5.5 Other strata.** Could cl(γ) meet the generic stratum or another prime's packet? No, by Route I: cl(γ) ⊂ Π^{-1}((p)). Alternatively by Route II: every limit point of O(P₀) upstairs lies over x (pointwise limits of maps vanishing exactly on p_x vanish on p_x — Lemma 7.1's argument — and by (R4) they are the (x, χ^{a₀b})). Note that Lemma 7.1 alone gives only P^{-1}(0) ⊇ p_x for a limit P; it is the explicit form (R4) that gives equality — a limit of the form (η, ·) over the generic point with P^{-1}(0) = 0 ⊉ p_x is excluded by Lemma 7.1, and a limit over (p) with P^{-1}(0) = p_x is the only possibility since p_x is maximal.

**5.6 The cut classes.** For an admissible E whose E-locus over x₀ is a single Q^{>0}-orbit (probe A's E(a₀)), Route II gives cl_{X₀}(γ) = q(C^E_{x₀} × R^{>0}) = γ: the orbit is closed. Consistent — no contradiction with Theorem A (whose ⊇ is then trivial) or with Cor. A.2 (which needs ≥ 2 base classes).

No counterexample exists to the statement as scoped in §4.3.

---

## 6. Assessment of the note's text

### 6.1 The original parenthetical of Corollary A.1 (the item as posed)

**F1 — MAJOR. Incomplete (Tors)-exclusion criterion.** Location: Cor. A.1, parenthetical, "limits with some component of b equal to 0 kill a μ_{ℓ^∞} and violate (Tors), so they leave the space". By (R5) the limit (x, χ^{a₀b}) is in the space iff b ∈ ℕ·Ẑ×_{(p)}; the sentence names only class (i) (a zero component) and is silent on class (ii) (all components nonzero, infinitely many non-units), which also violates (Tors). If the sentence's criterion were the whole story, then the limit points of class (ii) would remain in X•(C)_E, they are not in the packet, and the claimed equality would be **false**. The conclusion survives only because the true criterion excludes class (ii) as well. Fillable (filled in (R5)); the text must change.
*Replacement text:* "The limit point (x, χ^{a₀b}), b ∈ Ẑ_{(p)}, satisfies (Tors) if and only if ker(( )^{b}) = ⊕_{ℓ≠p} μ_{ℓ^∞}[b_ℓ] is finite, i.e. if and only if every component b_ℓ is nonzero and all but finitely many are units — equivalently b ∈ ℕ·Ẑ×_{(p)}. Exponents with a zero component, and exponents with all components nonzero but infinitely many non-units (e.g. b = (ℓ)_{ℓ≠p}), are points of the un-cut X•(C) but of no X•(C)_E; the remaining limit points are, by (35)–(36), exactly the (Tors)-characters at x."

**F2 — MAJOR. The closure computed is of the wrong set in the wrong space.** Location: same parenthetical, "every limit of {F_n(P₀)}_n along any subnet is P₀^b …; one gets cl(γ) ∩ (char-p part) = Γ^E_p exactly." What is computed is the closure of S̃ (one sequence, one chart, one fixed x, upstairs in X•(C)); what is claimed is the closure of the circle γ in the suspension X₀. Three reductions are missing and none is routine enough to leave implicit: (a) X₀ → X̌₀(C)_E through the open quotient map q, where q^{-1}(γ) = O(P₀) × R^{>0} is the whole Q^{>0}-orbit, not S ((R1)); (b) the colimit to chart 1, requiring that the charts be open and that O(P₀) ∩ chart 1 = S ((R2)); (c) X•₀(C) to X•(C) at the fixed x, requiring the open π and the compact-group saturation lemma ((R3)). Fillable (filled in §4.2); the text must change.
*Replacement text:* the block "(R1)–(R6)" of §4.2 above, or its equivalent already installed in the note's Session-14 replacement block ("Explicit form … (a)–(f)"), which I have verified line by line (§6.2).

**F3 — MINOR. The hedge "∩ (char-p part)".** Undefined in the note (no "char-p part" of X₀ is defined) and redundant: cl(γ) ⊂ Π^{-1}((p)) by Route I. Replacement: delete the hedge; write "cl_{X₀}(γ) = Γ^E_p".

**F4 — MINOR. Wrong cross-reference.** "With Step 5's converse inclusion": Theorem A's Step 5 is the sweep (⊇) and contains no converse. Replacement: "With the converse inclusion (Prop. A.1′ / (R1)–(R6))".

**F5 — MINOR (already repaired in the note's §3 block). The topology on X₀ is asserted without citation** in §3.1 ("implicit throughout §§8, 10"). Since the converse is exactly the statement whose truth depends on that topology (§5.2), the warrants of §3.5 above must be cited. The note's Session-14 §3 block now cites them; no further change.

**F6 — MINOR (headline bookkeeping).** The headline sentence "Γ^E_p is the orbit closure of each of its points and is the smallest closed invariant set containing any one of its orbits" needs ⊆, which the note itself left at proposition grade while asserting the headline without hedge; the Session-8 adjudication §4 item 1 ("packets are minimal sets") inherited this. Now backed (Route I). No text change beyond the dated blocks already present.

### 6.2 The Session-14 replacement block already in the note (Prop. A.1′, "Explicit form", new Cor. A.1) and the §3 / §5 dated blocks

I re-derived every step of the installed replacement against the sources (this is §4 above; Route I = Prop. A.1′, Route II = "Explicit form (a)–(f)"). The mathematics is correct and the page anchors are correct, with the following exceptions, all MINOR:

**F7 — MINOR. Misplaced citation for "the colimit topology is not finer than the pointwise one on any chart".** The block cites "p. 47: the inductive-limit and subspace topologies agree". p. 47's sentence is about the E-subspaces versus the ambient colimit; the fact actually needed — each chart F_ν^{-1}(X•(C)) is open and closed in X̌(C) and F_ν is a homeomorphism — is Prop. 7.4(a),(b) (p. 43) with Lemma 7.3 (p. 42). Replacement: "(Prop. 7.4 a–b, p. 43, with Lemma 7.3, p. 42: each chart is clopen and F_ν is a homeomorphism; p. 47 for the E-version)".

**F8 — MINOR. Misattributed remark on proper discontinuity.** The §3 block says "the Q^{>0}-action is not properly discontinuous (p. 49)". Deninger's sentence on p. 49 is "The Q^{>0}-action on Ȟ_{Etors} × R^{>0} is not properly discontinuous" — about the adelic target of (68), not about X̌₀(C)_E × R^{>0}. The statement about X̃ is true, but its warrant is Cor. A.2 / adjudication §3 (a non-Hausdorff quotient), not p. 49. Replacement: "and the Q^{>0}-action on X̌₀(C)_E × R^{>0} is not properly discontinuous (it has a non-Hausdorff quotient, Cor. A.2; compare Deninger's remark for the adelic image, p. 49)".

**F9 — MINOR. "then m′ = 1" in the incidental Step-5 correction.** The block's parenthetical "if F_r(x, χ^â) ∈ X•₀(C) for r = m/m′ ∈ Q^{>0} in lowest terms then m′ = 1" should read "then m′ is a power of p" ((R2): F_{p^k}^{-1} acts trivially on packet points, so denominators p^k are allowed; the subsequent "â′ = â·m·p^k" already accounts for this). Replacement: "then the prime-to-p part of m′ is 1".

**F10 — MINOR. Two items of bookkeeping.** (a) Step (c) of the "Explicit form" asserts cl(π^{-1}S) = cl(S̃)·G from "G is compact and acts continuously" without the one-line closed-projection argument (L3); add "(the saturation of a closed set under a compact group acting jointly continuously is closed: it is the projection of a closed subset of X•(C) × G)". (b) The three dated blocks cite `results/c3-r/referee-s14/B-corA1-adjudication.md`, which does not exist on disk or in git history (only the `-checks.py/.json` pair does); either the file must be written or the citations must point to the referee reports. Not a mathematical defect.

Everything else in the installed blocks checks: the (Tors) criterion (= (R5)); the compactness of Γ_{x₀} for E ⊇ E_f as q(π(β(Ẑ×_{(p)})) × [1, p]) (correct: every point of C_{x₀} is F_r π(x, χ^a) with a a unit by (38), [F_r P, w] = [P, rw], and [P, p^k u] = [P, u] on C_{x₀} by Thm 5.2 — so Γ_{x₀} is the continuous image of a compact set; this is a proof of the compactness asserted without proof at [x-03] pp. 2–3 and [x-06] p. 12); nowhere-density for E ⊇ E_f from Thm 9.2 + Cor. 9.7 (the generic fiber of the E_f-space is dense in X̌₀(C)′ = X̌₀(C) for N₀ = ℕ, a fortiori in X̌₀(C)_E, and q maps dense sets to dense sets; the generic stratum is Π^{-1}((0)), disjoint from Γ_{x₀}); the necessity of E ⊆ E_tors (= §5.1); the scope limits; the correction to Theorem A Step 5 ("rational units" — a positive integer is a unit of ∏_{ℓ≠p} Z_ℓ only if it is a power of p — correct); and the sharpened Morishita caution in the §3 block (Γ_p closed, compact for E ⊇ E_f, non-Hausdorff in the subspace topology, hence [r3s-08] Thms 2.2.8/2.2.9's "homeomorphism" and "closed R+-orbits" cannot be statements about the subspace topology — confirmed against pp. 16–18 of [r3s-08]).

---

## 7. VERDICT BLOCK

**Verdict: PASS-WITH-REPAIRS.** FATAL 0 · MAJOR 2 (F1, F2 — both against the original parenthetical, both fillable and filled, and already repaired in the note by the installed replacement block, which I verified independently) · MINOR 8 (F3–F10; F5 and F6 already addressed by the note's dated blocks; F7–F10 are repairs to the installed replacement block and its cross-references).

| # | Severity | Location | Finding | Repair |
|---|---|---|---|---|
| F1 | MAJOR | Cor. A.1 parenthetical | (Tors) exclusion criterion incomplete (misses all-nonzero/infinitely-many-non-unit exponents) | replacement sentence in §6.1 F1 |
| F2 | MAJOR | Cor. A.1 parenthetical | closure computed for S̃ in X•(C), not for γ in X₀; reductions (R1)–(R3) absent | §4.2 (R1)–(R6), or the installed "Explicit form (a)–(f)" |
| F3 | MINOR | same | hedge "∩ (char-p part)" undefined and redundant | delete; "cl_{X₀}(γ) = Γ^E_p" |
| F4 | MINOR | same | "Step 5's converse inclusion" — Step 5 has none | "the converse inclusion (Prop. A.1′ / (R1)–(R6))" |
| F5 | MINOR | §3.1 | topology of X₀ uncited (load-bearing) | already repaired (§3 block); warrants as in §3.5 above |
| F6 | MINOR | Cor. A.1 headline; adjudication §4 item 1 | "minimal set"/"smallest closed invariant set" needs ⊆ | now backed by Route I; dated blocks suffice |
| F7 | MINOR | installed block, "Explicit form (f)" | p. 47 cited for the chart/pointwise fact | cite Prop. 7.4 a–b p. 43 + Lemma 7.3 p. 42 |
| F8 | MINOR | installed §3 block | "not properly discontinuous (p. 49)" is Deninger's remark for Ȟ_{Etors} × R^{>0} | reword as in §6.2 F8 |
| F9 | MINOR | installed Step-5 correction | "then m′ = 1" | "then the prime-to-p part of m′ is 1" |
| F10 | MINOR | installed block (c); all three dated blocks | (a) saturation lemma unproved; (b) cited adjudication file absent from disk and git | (a) add (L3); (b) write the file or repoint the citations |

**What is now established at referee grade, and its precise scope.** For every arithmetic scheme X₀, every admissible class E, and every point x₀ with finite residue field, the packet Γ^E_{x₀} = Π^{-1}(x₀) is a closed, flow-invariant subset of the suspension X₀ = X̌₀(C)_E ×_{Q^{>0}} R^{>0} with its quotient topology, Π : X₀ → X₀ being the continuous flow-invariant map descended from pr_{X₀}; hence the closure of any periodic orbit γ ⊂ Γ^E_{x₀} lies in Γ^E_{x₀} and meets no other fiber of Π — not the generic stratum, not another packet. For X₀ = Spec Z (C = ℂ, N₀ = ℕ) and any admissible E, combining with Theorem A — or directly by the chart-by-chart computation (R1)–(R6), which proves both inclusions and shows the equality chart by chart — **cl_{X₀}(γ) = Γ^E_p exactly**, with no hedge; Γ^E_p is a minimal set (nonempty, closed, invariant, every orbit dense), and for E ⊇ E_f it is compact and nowhere dense in X₀. The hypotheses that carry the result and cannot be dropped are: the quotient topology on X₀ (the sourced reading, §3.5) and (Tors) (dropping it makes the equality false, §5.1). The result says nothing about, and does not constrain, the mapping face or the compact-non-closed face of Q*; the Session-8 adjudicated verdicts are unchanged except that the words "minimal sets" in adjudication §4 item 1 and the "smallest closed invariant set" headline of Cor. A.1 are now fully backed, and Q-c is settled YES.

---

## 8. Sources — every page read this session

- [x-03] `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` (printed page = PDF page): pp. 1–3 (intro: "compact packets", "no fixed points"); pp. 20–27 (§§2–4: Remark 3.4, colimit description pp. 24–25, Definition 3.6, Proposition 3.7, §4 opening, (Tors)/(Image), Definition 4.1, Proposition 4.2, (30)–(31) and the Q₀^{>0}-equivariant extensions of pr); pp. 28–30 (Lemma 4.3, Corollary 4.4, the example classes, Lemma 4.6); pp. 31–34 (§5: (32)–(46), Proposition 5.1, Theorem 5.2 statement); pp. 35–37 (proof of Theorem 5.2, Lemma 5.3, Remark 5.4, Theorem 5.5); pp. 38–40 (§6: suspension, Γ_{x₀}, Γ^E_{x₀}, Theorem 6.1, the Y₀ question); pp. 40–49 (§7 in full: pointwise topology, Lemma 7.1 with proof, Lemma 7.2, the glued topology, Lemma 7.3 with (51)–(52), the inductive limit topology (53), Proposition 7.4 with proof, Propositions 7.5–7.7, Corollaries 7.8–7.9, Remark, Theorem 7.10 with proof and Remarks 1–2, the E-version paragraph, (56)–(68), the "not properly discontinuous" sentence); pp. 49–54 (§8: opening, Claim 8.1, Theorem 8.2 with proof, Lemma 8.3 with proof; §9 opening, Proposition 9.1, Theorem 9.2 statement and start of proof); pp. 60–64 (end of §9: (90)–(100), Corollary 9.7 with proof and Remark, Theorem 9.8; §10 opening through Proposition 10.3 and its Remark). Whole-file greps for "quotient topology", "topological closure", "Hausdorff", "properly discontinuous", "subspace topology", "inductive limit topology", "compact".
- [x-06] `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`: pp. 9–13 (§4: rational Witt spaces, Theorem 4.1, the definition of X₀ on p. 11, Theorems 4.2–4.4 and the surrounding text on pp. 11–13).
- [r3s-08] `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`: pp. 13–18 (Proposition 2.1.9 and the topologies on Ẋ_K(C), X̌_K(C), Remark 2.1.13; §2.2 through Theorem 2.2.9; the opening of §2.3).
- [D25] `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf`: p. 1 (introduction), plus full-text greps ("suspension", "packet", "Hausdorff", "closure", "quotient topology", "periodic orbit", "topolog") — nothing relevant to the item.
- Program files: `results/c3-r/probe-9.3-adjudication.md` (entire); `results/c3-r/probe-9.3-b.md` (entire, 169 lines); `results/corpus-routing.md` (header and standing caveats 1–20); directory listing of `results/c3-r/referee-s14/` and the two `-checks.json` files there (for provenance only; referee O's report `B-corA1-O.md` was not opened; the prior-run file now preserved as `B-corA1-F-run1-0215.md` was not opened before §4 was written).
- Companion script: `results/c3-r/referee-s14/B-corA1-F-rerun-checks.py`, output `B-corA1-F-rerun-checks.json` — C1 (CRT density) true; C2 (three (Tors) regimes) true; C3 (chart-1 criterion) true; C4 (n_k → 0 example) true; C5 (rotation values equidistribute, max gap 0.0015 over 2000 terms) — informational.

— end of referee report F (re-run) —
