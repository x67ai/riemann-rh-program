# Second-model verification: companion §9.6–9.7 and §10 (b-collar model, assembly, repairs)

**Stamp:** started Sun Sep  6 13:12 IST 2026 (machine clock). Agent: SECOND-MODEL VERIFIER (hostile referee),
Session 17 cross-check. Task: re-derive independently, then AGREE/DISAGREE with each ruling of
`xcheck-s17/refute-assembly.md`.
**Method:** every inequality recomputed from scratch before looking at the first referee's arithmetic;
every quoted page and statement number re-grepped verbatim from `novelty/ALKL-2024-published.txt`.
Default ruling FALLS/UNDECIDED.

(Report appended item by item as the work proceeds.)

## Verdict

**HOLDS-WITH-REPAIR.** Items 1, 3, 4, 5, 6, 7 HOLD; Item 2 (assembly) HOLDS-WITH-REPAIR — the "steps are
Fréchet" assertion is unsupported for A^m(M) (p. 38 calls it only an "LCS") and must be filled, cheapest by
citing Cor. 6.38 + Remark 6.41. No counterexample to any step of §9.6–9.7 or §10 was found. I AGREE with
every ruling of `refute-assembly.md`; I DISAGREE with its implicit clean bill for two sentences (the
companion's c-sign in §9.6 and the note's dangling "on which" in the Claim-6.46 clause), and I add four
findings it missed. Full statement in the closing "## Verdict" section.

## Item 1 — companion §9.6, the b-collar model

### 1a. Change of variable (recomputed from scratch)
x = e^{−ϱ} ⟺ ϱ = −log x on x > 0. dϱ/dx = −1/x ⟹ ∂_x = (dϱ/dx)∂_ϱ = −x^{−1}∂_ϱ ⟹ **x∂_x = −∂_ϱ**.
x^{−m} = (e^{−ϱ})^{−m} = **e^{mϱ}**. Both as stated. Consequently (x∂_x)^a∂_y^b = (−1)^a ∂_ϱ^a∂_y^b, so
N^b_m(v;(a,b)) := sup e^{mϱ}|∂_ϱ^a∂_y^b v| = sup_{M̊∩U_j} x^{−m}|(x∂_x)^a∂_y^b (λ_j u)|.

Published (6.41), p. 38, verbatim (read):
"Let { P_j | j ∈ ℕ_0 } be a countable C^∞(M)-spanning set of Diff_b(M). The topology of A^m(M) can be
described by the semi-norms ‖·‖_{k,m} (k ∈ ℕ_0) given by  ‖u‖_{k,m} = ‖P_k u‖_{x^m L^∞} = ess sup_M x^{−m}|P_k u|
= sup_{M̊} x^{−m}|P_k u|, using (6.33) in the last expression."
So N^b_m(v_j;γ) is literally a (6.41)-seminorm for P = (x∂_x)^a∂_y^b∘λ_j. AGREE with referee 1.

### 1b. Inclusion direction
Published (6.38), p. 38, verbatim: "Note that (6.37) yields a continuous inclusion  A^m(M) ⊂ A^{m′}(M) (m′ < m)."
and (6.37), p. 37: "for m′ < m, from x^{m−m′} ∈ L^∞(M), we easily get a continuous inclusion
x^m L^∞(M) ⊂ x^{m′}L^∞(M)."
Model check: m′ < m, ϱ ≥ ϱ_0 ⟹ e^{m′ϱ}|∂^γ v| = e^{(m′−m)ϱ}·e^{mϱ}|∂^γ v| ≤ e^{(m′−m)ϱ_0}N^b_m(v;γ)
(the factor is ≤ e^{(m′−m)ϱ_0} because m′−m < 0 and ϱ ≥ ϱ_0). So B^m ⊂ B^{m′} for m′ < m. Matches (6.38). ✓

### 1c. Interpolation in the b-model — recomputed independently
**Warning on the companion's phrasing (new, referee 1 did not flag it).** "the inequality of 9.4 holds with
w := e^ϱ in place of 1+|ξ|" read *literally with the same c* is FALSE: 9.4 sets c := (m′−m)/(2|γ|), and here
m = −k, m′ = −k′ with k < k′, so (m′−m)/(2|γ|) = −(k′−k)/(2|γ|) < 0, giving h = w^{−c} = w^{|c|} → ∞,
so Nh ≤ 1 fails and R_0 = N^{1/c} is meaningless. The companion's own exponent line fixes the reading:
the substitution is m_{9.4} ↦ k (the index that *increases with the space*, B^{−k} ⊂ B^{−k′} for k < k′), i.e.
**c := (k′−k)/(2|γ|) > 0**. With that reading everything below works. This is a presentational defect in one
sentence, not a mathematical one; it should be made explicit before the companion is sent.

Set w := e^ϱ, weight w^{−k} (= e^{mϱ} with m = −k), k < k′ < k″, γ = (a,b) ≠ 0, D = 1 + (n−1) = n variables,
c := (k′−k)/(2|γ|), N > |γ| + (k″−k′)/c, R_0 := max{1, N^{1/c}}, all box sides h := w^{−c}.
- **Box fits.** Nh = N w^{−c} ≤ 1 ⟺ w ≥ N^{1/c}; then ϱ′ ∈ [ϱ, ϱ+1] and e^{ϱ′} ∈ [w, ew]. ✓ (companion's claim).
  The ϱ-box [ϱ, ϱ+Nh] ⊂ [ϱ_0,∞) since ϱ ≥ ϱ_0, h > 0 (the box runs *toward* the boundary x → 0, where the
  model is unbounded — this is what makes the one-sided half-line harmless). ✓
- **Sup bounds on Q.** |v| ≤ N^b_{−k}(v;0)(w′)^{k} ≤ e^{|k|}w^{k}N^b_{−k}(v;0) (w′ ∈ [w,ew]);
  |∂^{Nχ_S}v| ≤ e^{|k″|}w^{k″}N^b_{−k″}(v;Nχ_S). Note **no w-power gain from ϱ-derivatives** — correct, the
  b-weight carries no |β|-shift, so all the (1−c)|β| bookkeeping of 9.4 simply disappears.
- **Lemma B with equal sides.** (∏_{i∈S}h^{N−γ_i})(∏_{i∉S}h^{−γ_i}) = h^{N|S|−|γ|} = w^{−c(N|S|−|γ|)}. ✓
- **S = ∅**, times the weight w^{−k′}: exponent = c|γ| + k − k′ = (k′−k)/2 + k − k′ = **−(k′−k)/2 < 0**,
  and w > R ⟹ ≤ R^{−(k′−k)/2}N^b_{−k}(v;0). Matches the companion's "c|γ| + k − k′ = −(k′−k)/2". ✓
- **S ≠ ∅**: exponent = −c(N|S|−|γ|) + k″ − k′ ≤ −c(N−|γ|) + k″ − k′ < 0 by N > |γ| + (k″−k′)/c;
  w > R ≥ 1 ⟹ w^{exponent} < 1, contribution ≤ C N^b_{−k″}(v;Nχ_S) ≤ C R^{k″−k′}N^b_{−k″}(v;Nχ_S). ✓
- **w ≤ R**: w^{−k′}|∂^γ v| = w^{k″−k′}·w^{−k″}|∂^γ v| ≤ R^{k″−k′}N^b_{−k″}(v;γ) (k″−k′ > 0). ✓
- **γ = 0**: w ≤ R gives R^{k″−k′}N^b_{−k″}(v;0); w > R gives w^{k−k′}·w^{−k}|v| ≤ R^{k−k′}N^b_{−k}(v;0). ✓
So N^b_{−k′}(v;γ) ≤ C[R^{−(k′−k)/2}N^b_{−k}(v;0) + R^{k″−k′}max_{Γ}N^b_{−k″}(v;γ′)], C = C(N,D,k,k″) uniform in K.
9.5's passage to (M*) then runs verbatim with V = {N^b_{−k}(·;0) < 1}, and V is independent of k″.
**AGREE with referee 1** on the arithmetic (I get the same two exponents), and I add the c-sign remark above.

### 1d. Local form of Diff_b — quotes checked verbatim
p. 30: "x∂_x, ∂_{y^1}, …, ∂_{y^{n−1}} and x^{−1}dx, dy^1, …, dy^{n−1} extend to smooth local frames around
boundary points" (for bTM, bT*M). p. 35: "the Lie subalgebra and C^∞(M)-submodule X_b(M) ⊂ X(M) of
vector fields tangent to ∂M, called b-vector fields. There is a canonical identity X_b(M) ≡ C^∞(M; bTM).
Using X_b(M) like in Sect. 2.7, we get the filtered C^∞(M)-submodule and filtered subalgebra
Diff_b(M) ⊂ Diff(M)." §2.7, p. 9: "Every Diff^m(M) (m ∈ ℕ_0) is spanned as C^∞(M)-module by all
compositions of up to m elements of X(M)". (6.26), p. 35: "Diff(M̆, ∂M)|_M = Diff_b(M)". p. 50:
"For every j, Diff(U_j, L∩U_j) is spanned by x∂_x, ∂^1_j, …, ∂^{n−1}_j using the operations of C^∞(U_j)-module
and algebra".
Hence on an adapted chart X_b(U) = C^∞(U)·{x∂_x, ∂_{y^i}} and every P ∈ Diff^k_b(M) restricts there to
Σ_{a+|b|≤k} c_{ab}(x,y)(x∂_x)^a∂_y^b with c_{ab} smooth up to x = 0 (bounded on the compact supp λ_j).
**AGREE**; and I confirm the converse direction needs the one-line cut-off fill referee 1 supplies:
(x∂_x)^a∂_y^b∘λ_j is realized globally as Σ_{a′≤a,b′≤b} C·[(x∂_x)^{a−a′}∂_y^{b−b′}λ_j]·(λ̃_j x∂_x)^{a′}(λ̃_j∂_y)^{b′}
with λ̃_j ∈ C_c^∞(U_j), λ̃_j ≡ 1 near supp λ_j — the extra terms carrying derivatives of λ̃_j are killed by the
coefficient, which is supported where λ̃_j ≡ 1. Referee 1's version of the fill is correct.

**Ruling for Item 1: HOLDS.** (AGREE with referee 1; one presentational addition, §1c "warning".)

## Item 2 — companion §9.7, assembly for I, A, Ȧ, 𝒦, J, K

### 2a. The criterion and the transfer rules (re-derived, not read off referee 1)
p. 4 verbatim: "for an inductive spectrum of LCSs of the form (X_k) = (X_0 ⊂ X_1 ⊂ ···), the condition of
being acyclic can be described as follows [39, Theorem 6.1]: for all k, there is some k′ ≥ k such that, for
all k″ ≥ k′, the topologies of X_{k′} and X_{k″} coincide on some 0-neighborhood of X_k."
p. 5 verbatim: "If the steps X_k are Fréchet spaces, the above properties of (X_k) depend only on the
LF-space X [39, Chapter 6, p. 111] … In this case, X is acyclic if and only if it is boundedly/compactly/
sequentially retractive [39, Proposition 6.4]. As a consequence, acyclic LF-spaces are complete and
regular [39, Corollary 6.5]." Also p. 5: "The above concepts and properties also apply to an
inductive/projective spectrum consisting of continuous inclusions X_r ⊂ X_{r′} for r < r′ in R because
⋃_r X_r = ⋃_k X_{r_k} …" — this licenses the companion's "indices in ℕ by cofinality". ✓
Also p. 5: "(X_k) is compact if the inclusion maps are compact operators. In this case, (X_k) is clearly
acyclic" — the shortcut the companion correctly says does not apply.

(M*) ⇒ the quoted coincidence, re-derived: V absolutely convex 0-nbhd of X_k with V ∩ W ⊂ O.
τ_{k″}|_V ≤ τ_{k′}|_V always. Conversely, given a ∈ V and a τ_{k′}-nbhd a+O, pick balanced W_0 (0-nbhd of
X_{k″}) with V ∩ W_0 ⊂ ½O; if b ∈ V and b−a ∈ W_0, then (b−a)/2 ∈ V (V absolutely convex) and
(b−a)/2 ∈ W_0 (balanced), so (b−a)/2 ∈ ½O, b−a ∈ O. Hence (a+W_0)∩V ⊂ a+O and τ_{k′}|_V ≤ τ_{k″}|_V. ✓
Initial-topology rule: V_Y := j^{−1}(V)∩Y_k, W_Y := j^{−1}(W)∩Y_{k″}; V_Y ∩ W_Y = j^{−1}(V∩W)∩Y_k
⊂ j^{−1}(O)∩Y_{k′} ⊂ O_Y. ✓ Finite products and constant spectra: immediate. ✓ **AGREE.**

### 2b. I(M,L) — quotes verified verbatim
p. 22: "the following map is required to be a TVS-embedding: (4.10) I^m(M,L) → C^∞(M∖L) ⊕ ⊕_j
S^{m̄}(N*L_j; ΩN*L_j), u ↦ (hu, (a_j))", preceded by "we get semi-norms on I^m(M,L), which becomes a
Fréchet space [25, Sections 6.2 and 6.10]"; (4.9) "m̄ = m + n/4 − n′/2"; the partition is "{h, f_j} a C^∞
partition of unity of M subordinated to the open covering {M∖L, U_j}" (so supp h ⊂ M∖L, hence h ≡ 0 on a
neighborhood of L — used in Item 6); (4.11) "I^m(M,L) ⊂ I^{m′}(M,L) (m < m′)"; (4.12)
"I^{(−m−n/4+ε)}(M,L) ⊂ I^m(M,L) ⊂ I^{(−m−n/4−ε)}(M,L), for all m ∈ R and ε > 0", "So I(M,L) = ⋃_m I^m(M,L)".
(4.12) is mutual cofinality with continuous inclusions in both directions, so ind_m I^m = ind_s I^{(s)}. ✓
a_j vanishes for x″ outside the compact projection K_j of supp f_j, so the target may be replaced by
C^∞(M∖L) × ∏_j S^{m̄}_{K_j} with the induced (hence still initial) topology. ✓ **AGREE.**

### 2c. A(M) — the note's literal claim, checked line by line
Definitions verbatim (p. 38): "A^m(M) = {u ∈ C^{−∞}(M) | Diff_b(M)u ⊂ x^m L^∞(M)}. This is another
C^∞(M)-module and **LCS**, with the projective topology given by the maps P: A^m(M) → x^m L^∞(M)
(P ∈ Diff_b(M))."  (6.38) "A^m(M) ⊂ A^{m′}(M) (m′ < m)";  (6.39) "A^{(s)}(M) ⊂ A^m(M) ⊂
A^{(min{m,0})}(M) (m < s − n/2 − 1)";  (6.40) "A(M) = ⋃_m A^m(M)";  (6.33) p. 36 "By elliptic regularity,
we also get continuous inclusions [25, Eq. (4.1.4)] Ȧ(M)|_{M̊}, A(M) ⊂ C^∞(M̊)";  p. 39 "From (2.1) and
(6.33), we also get the continuous semi-norms ‖·‖_{K,k,m}" (= (6.42)).
(i) **λ_j-component continuous:** N^b_m(v_j;(a,b)) = ‖(x∂_x)^a∂_y^b λ_j u‖_{x^mL^∞} is a (6.41)-seminorm for
   P = (x∂_x)^a∂_y^b∘λ_j ∈ Diff_b(M) (Item 1d). ✓ literally true.
(ii) **μ-component continuous:** A^m → A(M) continuous by (6.40); A(M) ⊂ C^∞(M̊) continuous by (6.33);
   multiplication by μ ∈ C_c^∞(M̊) continuous on C^∞(M̊). Or directly (6.42). ✓ Citation "(6.33)" is right.
(iii) **Projective topology over Diff_b(M) = initial topology of Λ.** u = Σ_jλ_ju + μu ⟹ Pu = Σ_jP(λ_ju) + P(μu).
   On supp λ_j (compact, boundary face included) P ∈ Diff_b^k is Σ_{a+|b|≤k}c_{ab}(x∂_x)^a∂_y^b with c_{ab}
   smooth up to x = 0, hence bounded: sup x^{−m}|P(λ_ju)| ≤ C Σ_{a+|b|≤k}N^b_m(v_j;(a,b)).
   sup_{M̊}x^{−m}|P(μu)| ≤ (max_{K′}x^{−m})·C_P‖μu‖_{C^k(K′)} < ∞ since K′ = supp μ ⋐ M̊ and x > 0 there
   (finite for either sign of m). So every (6.41)-seminorm is dominated by finitely many Λ-seminorms;
   with (i)–(ii) the two topologies are equal. ✓ **The note's sentence is literally true.**
(iv) **Is C^∞(M̊) needed?** Yes. The μu piece lies in no collar chart. Conversely its C^k(K′)-seminorms *are*
   dominated by (6.41)-seminorms: with ν ∈ C_c^∞(M̊), ν ≡ 1 near K′, νx^{−1} ∈ C^∞(M), so
   νx^{−1}(x∂_x) ∈ Diff_b(M) agrees with ∂_x on K′; iterating, every ∂^α|_{K′} is a b-operator on K′. So the
   C^∞(M̊)-factor contributes a constant spectrum and costs nothing. ✓
(v) Λ is m-independent (fixed partition of unity). ✓  Injectivity is not used by the transfer rule. ✓

### 2d. Ȧ, 𝒦, J, K — quotes verified verbatim
(6.47) p. 40: "Ȧ^m(M) = I^m_M(M̆, ∂M) ⊂ I^m(M̆, ∂M) (m ∈ R), which are closed subspaces satisfying the
analogs of (4.11) and (4.12). Thus Ȧ(M) = ⋃_m Ȧ^m(M) …" — note Ȧ^m is *defined* as that closed subspace,
so the transfer needs nothing from Cor. 6.20. ✓
p. 41: "K^{(s)}(M) = Ȧ^{(s)}_{∂M}(M), K^m(M) = Ȧ^m_{∂M}(M), K(M) = Ȧ_{∂M}(M). These are closed subspaces
of Ȧ^{(s)}(M), Ȧ^m(M) and Ȧ(M), respectively; more precisely, they are the null spaces of the corresponding
restrictions of the map (6.36). They satisfy the analogs of (4.4), (4.11) and (4.12)." ✓
p. 56: "(7.10) restricts to a TVS-isomorphism π^*: A(**M**) → J(M,L) (7.26) … We also get spaces
J^{(s)}(M,L) and J^m(M,L) (s, m ∈ R) corresponding to A^{(s)}(**M**) and A^m(**M**) via (7.26)"; (7.27)
"J^m(M,L) = {u ∈ C^{−∞}(M,L) | Diff(M,L)u ⊂ **x**^m L^∞(M)}, equipped with topologies like in Sects. 6.8
and 6.10. These spaces satisfy the analogs of (4.4), (6.29) and (6.38)–(6.40)." ✓
p. 58: "K^{(s)}(M,L) = I_L^{(s)}(M,L), K^m(M,L) = I_L^m(M,L), K(M,L) = I_L(M,L). These are closed subspaces
of I^{(s)}(M,L), I_L^m(M,L) and I(M,L), respectively". **I confirm the printed "I_L^m(M,L)" in the second
list is a slip for I^m(M,L)** (a set is not a proper closed subspace of itself). Harmless. ✓

### 2e. The Fréchet gap — I AGREE it is real, and I add two cheaper fills and one caveat
The paper calls A^m(M) an "LCS" (p. 38) and never asserts Fréchet for it; the Fréchet property is asserted
for I^m (p. 22) and for the *Sobolev* steps only: Prop. 4.1 (I^{(s)}), Prop. 6.6 (Ȧ^{(s)}, A^{(s)}), Prop. 6.25
(K^{(s)}(M)), Cor. 7.11 (J^{(s)}), Cor. 7.20 (K^{(s)}(M,L)). Since p. 5's [39, Prop. 6.4] and the "property of
the LF-space" sentence are both conditioned on Fréchet steps, and the companion runs (M*) on the
**symbol-order** spectra, the assertion "the steps being Fréchet" is unsupported for A^m — hence for
J^m ≅ A^m(**M**) — as referee 1 says. **AGREE: HOLDS-WITH-REPAIR.**
Three fills, in increasing cheapness:
 (a) referee 1's completeness argument. I checked it and it is correct, with one step it left implicit:
     to get u_ν → u one uses 1 ∈ Diff_b^0(M) = C^∞(M), so 1 = Σ_i f_i P_i for the spanning set {P_i} and
     u_ν = Σ_i f_i P_i u_ν converges in the Banach space x^mL^∞(M); then x^mL^∞(M) ⊂ C^{−∞}(M)
     continuously (p. 37, read) and P continuous on C^{−∞}(M) give Pu = lim Pu_ν ∈ x^mL^∞(M).
 (b) **cheapest — a citation, no proof:** Cor. 6.38 (p. 46) "A^m(M) ≡ x^m H_b^∞(M) ≡ x^{m+1/2}H^∞(M̊)
     (m ∈ R)" with Remark 6.41 (p. 47) "Corollary 6.39 and the first identities of Corollaries 6.38 and 6.40
     are independent of g. So they hold true without the assumptions (A) and (B)". x^m H_b^∞(M) is a
     countable projective limit of Hilbertian spaces, hence Fréchet. I checked by grep that §§6.19–6.21
     nowhere cite Prop. 6.12, Cor. 6.14, Cor. 6.21, Cor. 4.5 or Cor. 3.4 (the only citations of those in the
     whole paper are at pp. 17–18, 23, 39, 40, 41, 48–49, 56), so this route is not circular. For J^m the
     same is Cor. 7.16 plus "The analog of Remark 6.41 makes sense for J(M,L)" (p. 57).
 (c) an alternative that avoids the question: (6.39)+(6.40) make (A^m)_m and (A^{(s)})_s mutually cofinal
     with continuous inclusions, and the p.-4 criterion transfers along mutual cofinality (given j take
     k with Y_j ⊂ X_k; take k′ from (X); take j′ with X_{k′} ⊂ Y_{j′}; for j″ ≥ j′ take k″ ≥ k′ with
     Y_{j″} ⊂ X_{k″}; then X_{k′} ⊂ Y_{j′} ⊂ Y_{j″} ⊂ X_{k″}, so on the 0-nbhd V ∩ Y_j of Y_j the four
     topologies are sandwiched and the outer two coincide). Then acyclicity holds for (A^{(s)})_s, whose
     steps are Fréchet by Prop. 6.6. This costs the same two lines as (a).
**Caveat on referee 1's phrasing:** it also demands the fill for the collar models B^m_K. That is not needed —
the transfer rule requires only (M*) of the target spectrum, never completeness of its steps. Same for S^m_K.
The fill is needed exactly for the six *step* spaces whose LF-spaces are claimed acyclic, i.e. only for A^m
(and thence J^m); Ȧ^m, K^m(M), K^m(M,L) are closed subspaces of Fréchet spaces once I^m is.

### 2f. Montel clauses — recomputed
B ⊂ S^m_K bounded, C_γ := sup_B N_m(·;γ). Every a ∈ B satisfies |∂^γa| ≤ C_γ max{1,(1+|ξ|)^m}, so
Arzelà–Ascoli + diagonal gives a C^∞_loc-convergent subsequence a_ν → a; a vanishes off K and
N_m(a;γ) ≤ C_γ, so a ∈ S^m_K. For m′ > m: N_{m′}(a_ν−a;γ) ≤ 2C_γ(1+R)^{m−m′} +
max{1,(1+R)^{|β|−m′}}·sup_{K×B̄_R}|∂^γ(a_ν−a)|; let ν → ∞ then R → ∞. So B is relatively compact
in the metrizable S^{m′}_K. ✓ The I(M,L) argument (bounded retractivity → B bounded in I^m with matching
topologies; image relatively compact at level m̄′; B closed in I^{m′}; (4.10)(I^{m′}) closed in the product
because I^{m′} is Fréchet and (4.10) an embedding; so B compact) is correct, and Cor. 4.2 (p. 20) supplies
barreledness. ✓
Non-compactness of S^m_K → S^{m′}_K: given a basic 0-nbhd {N_m(·;γ)<ε_γ, γ ∈ F}, put k_0 := max{|α|},
a_λ := ελ^{−k_0}sin(λx_1)θ_1(x)θ(ξ); N_m(a_λ;(α,β)) ≤ Cε for |α| ≤ k_0 and all λ ≥ 1, while
N_{m′}(a_λ;((k_0+1)e_1,0)) ≳ ελ → ∞. So the p.-5 shortcut genuinely does not apply. ✓ **AGREE.**

**Ruling for Item 2: HOLDS-WITH-REPAIR** (same repair as referee 1, narrowed to A^m/J^m; cheapest fill is
the Cor. 6.38 + Remark 6.41 citation).

## Item 3 — companion §10.1, repair of Claim 6.46 (pp. 48–49)

### 3a. A methodological point referee 1 could not have settled from the .txt
`pdftotext` drops the prime glyph entirely: A^m(M) and A^{m′}(M) both come out as "Am (M)", and even
(6.38) — which must read A^m ⊂ A^{m′} — prints as "Am (M) ⊂ Am (M)". So the .txt **cannot** decide the
index bookkeeping of Claim 6.46's proof. I therefore rendered PDF pages 48–49 and read them directly.
Referee 1's quotation happens to be right, but it was not verifiable from its stated source.

### 3b. Printed proof, verbatim from the rendered page (p. 48, continuing p. 49)
"**Claim 6.46** For all bounded subset A ⊂ 𝒜(M), there is some bounded subset B ⊂ 𝒜̇(M) such that, for
all 0-neighborhood U ⊂ 𝒜̇(M), there is a 0-neighborhood V ⊂ 𝒜(M) so that A ∩ V ⊂ R(B ∩ U).
  Since 𝒜(M) is boundedly retractive (Corollary 6.16), A is contained and bounded in some step 𝒜^m(M).
For any **m′ > m**, let E_{m′}: **𝒜^m(M)** → 𝒜̇^{(s)}(M) be the partial extension map given by Proposition
6.29. Then B := E_{m′}(A) is bounded in 𝒜̇^{(s)}(M), and therefore in 𝒜̇(M). Moreover, given any
0-neighborhood U ⊂ 𝒜̇(M), there is some 0-neighborhood W ⊂ **𝒜^{m′}(M)** so that E_{m′}(W) ⊂
U ∩ 𝒜̇^{(s)}(M). By Corollary 6.14, there is some 0-neighborhood V ⊂ 𝒜(M) such that V ∩ 𝒜^m(M) =
W ∩ 𝒜^m(M). Hence E_{m′}(V ∩ 𝒜^m(M)) ⊂ U ∩ 𝒜̇^{(s)}(M), yielding
A ∩ V = R(E_{m′}(A ∩ V)) ⊂ R(E_{m′}(A) ∩ E_{m′}(V ∩ 𝒜^m(M))) ⊂ R(B ∩ U)."
(Prop. 6.45's frame, same page: "By Corollary 6.8 and [39, Lemma 7.6], it is enough to prove that the map
(6.36) satisfies the following condition of 'topological lifting of bounded sets.'" — *aside:* the paper has no
Corollary 6.8; this is a slip for Proposition 6.8, p. 37. Not material, not mentioned in the note.)

Prop. 6.29, p. 42, verbatim: "For all m ∈ R, there is a continuous linear partial extension map
E_m: A^m(M) → Ȧ^{(s)}(M), where s = 0 if m ≥ 0, and m > s ∈ Z^− if m < 0. For m ≥ 0,
E_m: A^m(M) → Ȧ^{(0)}(M) is a continuous inclusion map." Definition, p. 42: "Given linear subspaces,
X ⊂ A(M) and Y ⊂ Ȧ(M), a map E: X → Y is called a partial extension map if R(Y) ⊂ X and RE = 1 on X."
Cor. 6.14, p. 39, verbatim: "If m′ < m, then the topologies of A^{m′}(M) and C^∞(M̊) coincide on A^m(M).
Therefore the topologies of A(M) and C^∞(M̊) coincide on A^m(M)."

### 3c. Is the note's index remark correct? YES — independently checked
Three separate places in the printed proof force m′ < m:
 1. Prop. 6.29 indexes E by its domain: E_{m′} lives on A^{m′}(M). Its being applied to A ⊂ A^m(M) needs
    A^m ⊂ A^{m′}, i.e. **m′ < m** by (6.38).
 2. "W ⊂ A^{m′}(M)" with "E_{m′}(W) ⊂ U ∩ Ȧ^{(s)}" only makes sense with the same domain, again m′ < m.
 3. Cor. 6.14 supplies "V ∩ A^m = W ∩ A^m" from a 0-nbhd W of A^{m′} only in the stated direction m′ < m.
Under the only alternative reading (E_{m′} is Prop. 6.29's E with domain literally A^m, and "m′" a mere
label) step 2 collapses: a 0-neighborhood W of the *smaller* space A^{m′} ⊂ A^m need not meet A^m in a
0-neighborhood, and Cor. 6.14 in the direction m > m′ gives nothing. So under either reading the printed
"m′ > m" is wrong and m′ < m repairs it. **The note's parenthesis is correct. AGREE with referee 1.**

### 3d. The replacement, re-derived from scratch
Γ(A) := absolutely convex hull of A; bounded (in any LCS the absolutely convex hull of a bounded set is
bounded: bounded sets are absorbed by the absolutely convex 0-nbhds, which form a base), and 0 ∈ Γ(A).
Bounded retractivity of A(M) (Item 2 + p. 5 [39, Prop. 6.4]) gives m with Γ(A) bounded in A^m(M) and
τ_{A(M)}|_{Γ(A)} = τ_{A^m}|_{Γ(A)}. For m′ < m the inclusions A^m ⊂ A^{m′} ⊂ A(M) are continuous, so
τ_{A(M)} ≤ τ_{A^{m′}} ≤ τ_{A^m} on Γ(A) and **all three coincide there**. E_{m′}: A^{m′}(M) → Ȧ^{(s)}(M)
with RE_{m′} = 1 on A^{m′}(M) (Prop. 6.29 + the definition). B := E_{m′}(Γ(A)) is bounded in Ȧ^{(s)}(M)
(continuous image of a set bounded in A^{m′}) hence in Ȧ(M) (Ȧ(M) = ⋃_sȦ^{(s)}, (6.29)). **B is fixed
before U**, as Claim 6.46 demands. Given U: W := E_{m′}^{−1}(U ∩ Ȧ^{(s)}) is a 0-nbhd of A^{m′}(M);
W ∩ Γ(A) is a relative-A^{m′} neighborhood of 0 in Γ(A), hence a relative-A(M) one, so there is a 0-nbhd V
of A(M) with V ∩ Γ(A) ⊂ W. For a ∈ A ∩ V ⊂ Γ(A) ∩ V ⊂ W: E_{m′}a ∈ B ∩ U and a = R(E_{m′}a) ∈ R(B ∩ U). ∎
Ingredients used: Prop. 6.29, the definition of partial extension map, bounded retractivity of A(M). None is
a coincidence statement. The conclusion is in fact *cleaner* than the printed chain (no "=" of traces needed).
Taking the hull is essential and for exactly the reason the companion gives: the coincidence of topologies is
needed at the point 0, which need not lie in A. ✓

### 3e. One editorial defect in the NOTE that referee 1 passed over
The note's §4 reads: "the absolutely convex hull of A is bounded in some A^m(M), **on which** the topologies
of A(M), A^{m′}(M) and A^m(M) coincide by bounded retractivity". The nearest antecedent of "on which" is
"A^m(M)" — and read that way the sentence asserts that the three topologies coincide on the whole step
A^m(M), which is precisely Cor. 6.14, the statement witness (e) refutes. The intended antecedent is the hull.
Since this note's whole point is that such coincidence fails on a step, an author of [ALKL24] reading it
quickly will see a self-contradiction. **Recommended fix (one word):** "…is bounded in some A^m(M), and on
that hull the topologies of A(M), A^{m′}(M) and A^m(M) coincide by bounded retractivity …".
(The companion §10.1 is unambiguous: "A ⊂ A^m(M) bounded and the A(M)-topology equals the A^m-topology
on A".)

**Ruling for Item 3: HOLDS** (mathematics), with the one-word wording fix in 3e. AGREE with referee 1's
ruling; DISAGREE that the note's sentence is beyond criticism as printed.

## Item 4 — companion §10.2, Prop. 8.8 (p. 64)

Verbatim, p. 64: "The following analog of Proposition 6.45 holds true with formally the same proof, using
Proposition 7.29 and Corollaries 7.13, 7.15 and 7.31. **Proposition 8.8** The dual-conormal sequence of M at
L is exact in the category of continuous linear maps between LCSs."
Verbatim, p. 60: "**Corollary 7.31** For all m ∈ R, there is a continuous linear partial extension map
E_m: J^m(M,L) → I^{(s)}(M,L), where s = 0 if m ≥ 0, and m > s ∈ Z^− if m < 0. *Proof* By the commutativity
of (7.38), we can take E_m equal to the composition J^m(M,L) → A^m(**M**) → Ȧ^{(s)}(M) → I^{(s)}(M,L),
where this map E_m is given by Proposition 6.29." So R E_m = 1 on J^m(M,L) with R = (7.31), p. 57 — the
exact analog of Prop. 6.29, indexed by its domain in the same way. ✓
Substitution table, checked term by term against the printed proof of Prop. 6.45/Claim 6.46:
 (6.36) ↦ (7.31); Prop. 6.8 ↦ **Prop. 7.29** (p. 60: "The following analog of Proposition 7.4 holds true with
 formally the same proof, using (7.38)"; Prop. 7.4, p. 54, read in full: a diagram chase in (7.21) plus the
 open mapping theorem for webbed/ultrabornological spaces — **no coincidence input**);
 Cor. 6.16 ↦ **Cor. 7.15** ("J(M,L) is an acyclic Montel space, and therefore complete, boundedly retractive
 and reflexive", p. 57), repaired in Item 2 through J^m ≅ A^m(**M**) with **M** compact with boundary;
 Prop. 6.29 ↦ **Cor. 7.31**; Cor. 6.14 ↦ Cor. 7.13, whose sole role is the false "V ∩ J^m = W ∩ J^m" and which
 is replaced verbatim by Item 3d with X_m := J^m(M,L), Y_s := I^{(s)}(M,L), R = (7.31).
The same index correction applies: E_{m′} must be indexed by m′ < m. The companion's §10.2 does not
repeat that correction ("Same lemma with X_m := J^m(M,L) …"); since it says "same lemma", and the lemma
as stated in §10.1 carries m′ < m, this is adequate, but a half-line would be safer.
"Cor. 7.13 is not needed there" — confirmed. **Ruling for Item 4: HOLDS. AGREE with referee 1.**

## Item 5 — companion §10.3, direct proof of Cor. 3.5 (p. 17)

**Printed statement and proof, verbatim (p. 17–18):** "**Corollary 3.5** For m < m′, C_c^∞(U × R^l) is dense in
S^m(U × R^l) with the topology of S^{m′}(U × R^l). Therefore C_c^∞(U × R^l) is dense in S^∞(U × R^l).
*Proof* The first assertion is given by Corollary 3.4 and the density of C_c^∞(U × R^l) in C^∞(U × R^l).
[p. 18] To prove the second assertion, take any open O ≠ ∅ in S^∞(U × R^l). We have O ∩ S^m(U × R^l) ≠ ∅
for some m. This intersection is open in S^m(U × R^l) with the topology of any S^{m′}(U × R^l) for all
m′ ≥ m. So O ∩ C_c^∞(U × R^l) ≠ ∅ by the first assertion."
So the assertion is density **in S^m for the S^{m′}-topology**, plus density in S^∞ — nothing about S^m in its
own topology. The second assertion's derivation uses only that O ∩ S^{m′} is S^{m′}-open and meets S^m in
O ∩ S^m; **Cor. 3.4 is not used there.** ✓ "the second assertion follows as printed" is right.

**Leibniz estimate, recomputed.** χ ∈ C_c^∞(R^l), χ ≡ 1 on B(0,1), supp χ ⊂ B(0,2), χ_R := χ(·/R), R ≥ 1,
a ∈ S^m. ∂_x^α∂_ξ^β[(1−χ_R)a] = Σ_{β′≤β} C(β,β′) ∂_ξ^{β′}(1−χ_R)·∂_x^α∂_ξ^{β−β′}a.
 β′ = 0: |(1−χ_R)∂_x^α∂_ξ^βa| ≤ ‖a‖_{K,α,β,m}(1+|ξ|)^{m−|β|}, and the factor vanishes for |ξ| ≤ R.
 β′ ≠ 0: ∂_ξ^{β′}(1−χ_R) = −R^{−|β′|}(∂^{β′}χ)(ξ/R), supported in R ≤ |ξ| ≤ 2R, where 1+|ξ| ≤ 3R, i.e.
  R^{−|β′|} ≤ 3^{|β′|}(1+|ξ|)^{−|β′|}; times |∂_x^α∂_ξ^{β−β′}a| ≤ ‖a‖_{K,α,β−β′,m}(1+|ξ|)^{m−|β|+|β′|} gives
  ≤ C(1+|ξ|)^{m−|β|}.
So ‖a − χ_Ra‖_{K,α,β,m′} ≤ C_{α,β}(a)·sup_{|ξ|≥R}(1+|ξ|)^{m−m′} = C(1+R)^{m−m′} → 0 (m < m′), the constant
depending on finitely many S^m-seminorms of the fixed a. ✓
**Independent numerical confirmation** (my own script, `scratchpad/cor35_v2.py`; l = 1, m = 1, m′ = 2,
two genuine S^1 symbols including an oscillatory one, β = 0,1,2,3, R = 10…320, sup taken away from the
grid edge to avoid one-sided-difference artifacts): R·‖a − χ_Ra‖_{β} stays bounded (0.33–0.55 for β = 0;
1.4–2.5 for β = 1; 8.7–19 for β = 2; 220–480 for β = 3), i.e. the rate is exactly R^{m−m′} = R^{−1}. A control
run with the *non*-symbol (1+ξ²)^{1/2}cos ξ shows no decay, confirming that C genuinely depends on the
S^m-seminorms of a — as the proof says.
**x cut-off.** ϕ ∈ C_c^∞(U), ϕ ≡ 1 on a neighborhood of K ⟹ ϕχ_Ra ∈ C_c^∞(U × R^l) and every
‖·‖_{K,α,β,m′}-seminorm of (1−ϕ)χ_Ra vanishes (all x-derivatives of 1−ϕ vanish on a neighborhood of K).
Given finitely many seminorms take K := ⋃K_i. ✓ This is exactly the printed first assertion. **Enough.**
Cor. 4.6's printed proof (p. 23, read verbatim) uses only Cor. 3.5 and Prop. 4.3, so it survives. ✓
**Addition referee 1 missed:** the paper itself already offers an escape hatch — **Remark 3.7, p. 18**:
"Another proof of Corollary 3.5 could be given like in Proposition 6.10." It is only a sketch ("could be
given"), so the companion's self-contained Leibniz proof is still the right thing to send; but the note may
wish to acknowledge Remark 3.7, since the authors will notice that their own remark anticipates the repair.

**Ruling for Item 5: HOLDS. AGREE with referee 1.**

## Item 6 — companion §10.4, Cor. 6.27 (p. 41) and Cor. 7.22 (p. 58)

**Statements and printed proofs, verbatim.** p. 41: "Now the following analogs of Corollaries 6.21 and 6.22
hold true with formally the same proofs, using Corollaries 6.21, 6.22 and 6.26. **Corollary 6.27** For
m < m′, m″, the topologies of K^{m′}(M) and K^{m″}(M) coincide on K^m(M)." p. 58: "Thus we get the
following consequences of Propositions 6.24 and 6.25 and Corollaries 6.26 to 6.28. … **Corollary 7.22** For
m < m′, m″, the topologies of K^{m′}(M,L) and K^{m″}(M,L) coincide on K^m(M,L)." So both printed proofs
do route through Cor. 6.21 (hence Cor. 4.5, hence Cor. 3.4), as the note says. ✓
p. 59: "**Proposition 7.26** The map (7.36) is a TVS-isomorphism, which induces TVS-isomorphisms
⊕_{m<−s−1/2} C^1_m → K^{(s)}(M,L) (s < −1/2)", where (7.36) is "⊕_{m=0}^∞ C^1_m → K(M,L), where
C^1_m = C^∞(L; Ω^{−1}NL) for all m ∈ N_0", the restriction of (7.24) built from (7.22)–(7.23) (u ↦ ∂_x^mδ^v_L).
I read its whole proof (pp. 59–60): Prop. 7.7, (4.17), (7.1), (2.19), Lemma 7.25, elliptic regularity, and the
open mapping theorem with Cor. 7.21. **No coincidence statement.** ✓ So every element of K(M,L) is a
*finite* sum Σ_k ∂_x^kδ_L ⊗ v_k with v_k ∈ C^∞(L; Ω^{−1}NL). ✓

**Local symbol (recomputed).** Codimension one (§7), adapted chart (x,y), L = {x = 0}, (4.8)
a(y,ξ) = ∫e^{−ixξ}u(x,y)dx. For u = ∂_x^kδ(x)v(y): a(y,ξ) = (−1)^k∂_x^k(e^{−ixξ})|_{x=0}v(y) = (−1)^k(−iξ)^kv(y)
= (iξ)^k v(y) — a polynomial in ξ of degree **exactly** k. ✓
Cut-off: ⟨f∂_x^kδ, φ⟩ = (−1)^k(fφ)^{(k)}(0) = Σ_{i≤k}C(k,i)(−1)^{k−i}f^{(k−i)}(0)·(−1)^iφ^{(i)}(0), so
f·∂_x^kδ = Σ_{i≤k}C(k,i)(−1)^{k−i}(∂_x^{k−i}f)|_{x=0}∂_x^iδ. ✓ (companion's formula verified). Hence the
symbol of f_j u is Σ_{i≤k_0}(iξ)^i w_{j,i}(y), w_{j,i} = Σ_{k≥i}C(k,i)(−1)^{k−i}(∂_x^{k−i}f_j)(0,y)v_k(y) ∈ C_c^∞,
**top coefficient w_{j,k_0} = f_j(0,y)v_{k_0}(y)**.

**Threshold — is "k > m̄" exactly right?** Σ_{k≤k_0}(iξ)^kw_k ∈ S^{m̄} ⟺ w_k = 0 for k > m̄:
(⇐) |∂_y^α∂_ξ^β[(iξ)^kw_k]| ≤ C‖∂^αw_k‖_∞|ξ|^{k−β} (zero for β > k), times (1+|ξ|)^{β−m̄} gives
≤ C(1+|ξ|)^{k−m̄} ≤ C. (⇒) with k_1 > m̄ maximal and w_{k_1}(y_0) ≠ 0, |a(y_0,ξ)|(1+|ξ|)^{−m̄} ∼
|w_{k_1}(y_0)||ξ|^{k_1−m̄} → ∞. Globally: supp h ⊂ M∖L (p. 22, verified) ⟹ h ≡ 0 on a neighborhood of L ⟹
hu = 0 and Σ_jf_j = 1 on L, so some f_j(0,y_0) ≠ 0 and w_{j,k_1} ≢ 0. Hence
**K^m(M,L) = {Σ_{k≤m̄} ∂_x^kδ_L⊗v_k} exactly**, with m̄ = m + n/4 − 1/2 by (4.9) with n′ = 1.
Two independent cross-checks that the threshold is not off by a constant:
 (i) (7.37) says ∂_x^kδ_L ∈ K^{(s)} ⟺ k < −s − 1/2; combined with (4.12) K^{(−m−n/4+ε)} ⊂ K^m ⊂
     K^{(−m−n/4−ε)} this pins the threshold into (m̄−ε, m̄+ε] for every ε > 0, i.e. exactly m̄ (the direct
     symbol computation settles the boundary case k = m̄, which (4.12) cannot).
 (ii) a = 1 ∈ S^0 for δ_L gives δ_L ∈ I^m ⟺ m ≥ 1/2 − n/4, the standard order of the delta of a
     codimension-one submanifold under the convention m̄ = m + n/4 − n′/2 of (4.9).
**Not off by a constant. The note's "iff v_k = 0 for k > m̄" is exactly right.** ✓

**Coefficient topology on polynomials — proved both ways.** P_{k_0}(K) := {Σ_{k≤k_0}(iξ)^kw_k : w_k ∈ C_c^∞(K)},
m̄_1 ≥ k_0, ξ ∈ R.
 (≤) N_{m̄_1}(a;(α,β)) ≤ Σ_{k≥β}(k!/(k−β)!)‖∂^αw_k‖_∞ sup_ξ|ξ|^{k−β}(1+|ξ|)^{β−m̄_1} ≤ CΣ_k‖∂^αw_k‖_∞,
     because (1+|ξ|)^{k−m̄_1} ≤ 1 for k ≤ k_0 ≤ m̄_1.
 (≥) ∂_ξ^{k_0}a = i^{k_0}k_0!w_{k_0}(y) identically, so evaluating at ξ = 0 (weight (1+0)^{k_0−m̄_1} = 1)
     ‖∂^αw_{k_0}‖_∞ ≤ N_{m̄_1}(a;(α,k_0))/k_0!; then a − (iξ)^{k_0}w_{k_0} ∈ P_{k_0−1} has
     N_{m̄_1}-seminorms ≤ N_{m̄_1}(a;(α,β)) + C‖∂^αw_{k_0}‖_∞, and downward induction gives
     ‖∂^αw_k‖_∞ ≤ C max_{β≤k_0}N_{m̄_1}(a;(α,β)) for all k ≤ k_0.
So on P_{k_0} the S^{m̄_1}-seminorms are equivalent to the C^∞(K)-seminorms of the coefficient tuple, for
**every** m̄_1 ≥ k_0. ✓ **PROVED, not merely plausible.**

**Conclusion.** For u ∈ K^m(M,L): hu = 0 and every a_j ∈ P^{(j)}_{k_0} with the *same* k_0 = ⌊m̄⌋ ≤ m̄ < m̄′, m̄″.
The I^{m′}- and I^{m″}-topologies on K^m(M,L) are the initial topologies of the same map (4.10) into
C^∞(M∖L) ⊕ ⊕_jS^{m̄′}_{K_j} and ⊕_jS^{m̄″}_{K_j}, and both restrict on the image to the coefficient topology.
Hence they coincide: **Cor. 7.22 holds.** (If m̄ < 0 then K^m = 0 and it is vacuous.) ✓

**Addition referee 1 missed — Cor. 6.27 need not go through (6.49).** The note and companion derive
Cor. 6.27 from Cor. 7.22 "via (6.49)". (6.49) is printed as a consequence of **Corollary 6.20**, which is proved
from Prop. 6.19, which is proved "using Proposition 6.18 and **Corollary 6.16**" — i.e. via one of the very
statements the note is repairing. There is no circularity (9.7's proof of Cor. 6.16 uses none of this), but the
dependency is avoidable and the note reads better without it: by (6.47) Ȧ^m(M) **is defined** as
I^m_M(M̆,∂M) ⊂ I^m(M̆,∂M), and K^m(M) := Ȧ^m_{∂M}(M) is then literally I^m_{∂M}(M̆,∂M) = K^m(M̆,∂M),
with the same subspace topology — no appeal to Cor. 6.20 needed at the level of the symbol filtration.
Recommended: cite **(6.45)/(6.47)** rather than (6.49) in that clause of the note.

**Cosmetic, confirming referee 1:** "polynomials in ξ with the v_k as coefficients" is literally true only before
the cut-off f_j; afterwards the coefficients are the w_{j,i} above. Degree and leading coefficient are
unchanged, so nothing in the argument depends on it.

**Ruling for Item 6: HOLDS. AGREE with referee 1**, plus the (6.49) → (6.47) simplification.

## Item 7 — the note's §1 sentence, and the external reader's proposed softening

**The sentence:** "The main package of the paper (acyclicity and retractivity of I, A, Ȧ, 𝒦, J, K for compact
M, and the exact sequences) stands once this is done."

**What §9–§10 actually deliver (on my items).** (M*) for the six symbol-order spectra ⟹ acyclicity ⟹
(Fréchet steps, p. 5, [39, Prop. 6.4]/[39, Cor. 6.5]) complete, regular, boundedly/compactly/sequentially
retractive; plus the Montel clauses (Item 2f); plus the two non-acyclicity consumers, Claim 6.46/Prop. 6.45
and Prop. 8.8 (Items 3–4); plus Cors. 6.27/7.22 (Item 6); plus Cor. 3.5 and thence Cor. 4.6 (Item 5).
The remaining exact sequences are Cor. 6.23 ("Proposition 6.8 has the following direct consequence", p. 41)
and Cor. 7.30 (from Prop. 7.29): both rest on open-mapping arguments (Props. 6.2, 6.8, 7.4, 7.29 — read;
Prop. 7.4's proof, quoted in Item 4, is a chase in (7.21) plus the open mapping theorem for
webbed/ultrabornological spaces), with no coincidence input. So the parenthetical list is covered.
All of this is **conditional on** (i) the interpolation inequality of §9.4 (another agent's item; I re-verified
the identical exponent bookkeeping in its b-version, Item 1c) and (ii) the Fréchet fill of Item 2e.

**Consumers I checked by exhaustive grep** (every internal citation of Prop. 3.2, Cor. 3.4, Cor. 4.5,
Prop. 6.12, Cor. 6.14, Cor. 6.21, Cor. 7.13 in the whole paper): pp. 17 (Cor. 3.5), 18 (Cor. 3.6, Rem. 3.8),
23 (Cor. 4.5, Cor. 4.7), 39 (Rem. 6.17), 40 (Cors. 6.21, 6.22), 41 (Cors. 6.27, 6.28), 48–49 (Claim 6.46),
56–58 (Cors. 7.13–7.15, 7.22, 7.23), 64 (Prop. 8.8). Nothing outside the note's §2 list and §4 re-routing.
**One observation the note does not record** (outside my item, flagged for the sponsor): Cor. 4.7's printed
proof (p. 23) is "Like in Corollary 3.6, by Corollaries 4.2 and 4.5 … I(M,L) is semi-Montel because
C^∞(M∖L) and S^∞(N*L_j; ΩN*L_j) are Montel spaces (Corollary 3.6)" — i.e. it invokes not only the false
Cor. 4.5 but also the **Montel clause of Cor. 3.6 over the generally non-compact base L_j**, whose status the
note's §2 leaves open (§2 lists only the acyclicity and bounded-retractivity clauses of Cor. 3.6 as false).
This does no harm — §9.7's Montel argument goes through the compactly based S^{m̄}_{K_j} and bounded
retractivity and needs neither — but the note's §4 sentence "and then of their Montel clauses" is doing more
work than a reader will realize. A half-clause would help.

**Verdict on the sentence.** As a claim about the mathematics it is **justified**, conditional on (i) and (ii).
As a claim about what the *note* demonstrates, the external reader is right: on the note's face (interp) is
asserted with a one-line justification and the Fréchet property of the steps is asserted with none. The
proposed softening ("The principal conclusions appear recoverable after replacing the false
topology-coincidence statements by bounded-set or compact-base estimates") is therefore an accurate
description of the note-as-shipped, but it understates what has been derived and checked. **The softening is
not mathematically warranted; it is a presentational choice.** Cheapest honest fixes, in order:
 1. send the companion alongside the note (with the Item 2e fill and the Item 3e wording fix);
 2. or append "(derivations available on request)" to the §1 sentence, not only to §5;
 3. or, if the sentence must stand alone, add "for compact M and compact L" and a clause excluding the
    non-compact-base clauses of Cor. 3.6 and of the p. 18 bundle extension — §2 already excludes them, but
    the §1 sentence is what a busy author will read.

**Ruling for Item 7: HOLDS** (sentence justified by §9–§10, conditional on 9.4 and the Fréchet fill);
softening optional. **AGREE with referee 1**, with the Cor. 4.7 observation added.

## Verdict

**HOLDS-WITH-REPAIR.** Items 1, 3, 4, 5, 6, 7 HOLD; Item 2 (assembly) HOLDS-WITH-REPAIR. I re-derived
every inequality and re-checked every quoted page against the published text (and, for pp. 48–49, against
the rendered PDF, because pdftotext destroys the primes). **I found no counterexample to any step of
§9.6, §9.7 or §10, and I confirm referee 1's six HOLDs and its one repair.**

Agreements and disagreements with `refute-assembly.md`, item by item:
- Item 1: **AGREE (HOLDS).** Same exponents. **Added:** the companion's "the inequality of 9.4 holds with
  w := e^ϱ" is false on a literal reading (c would be negative); the substitution is m_{9.4} ↦ k. One
  sentence of the companion should say so.
- Item 2: **AGREE (HOLDS-WITH-REPAIR).** The Fréchet gap is real — p. 38 calls A^m(M) only an "LCS", and
  p. 5 conditions [39, Prop. 6.4] and the "property of the LF-space" statement on Fréchet steps.
  **Narrowed:** the fill is needed only for A^m(M) (hence J^m); B^m_K and S^m_K need none, since the
  transfer rule uses only (M*) of the target. **Cheapest fill:** cite Cor. 6.38 + Remark 6.41 (A^m(M) ≡
  x^mH_b^∞(M), Fréchet, independent of g) — a citation instead of a proof; I verified by grep that
  §§6.19–6.21 are free of the broken statements. A second route (mutual cofinality with (A^{(s)}), Fréchet
  by Prop. 6.6, plus a two-line transfer of the p.-4 criterion along cofinality) is given in 2e(c).
- Item 3: **AGREE on the ruling (HOLDS); DISAGREE that the note's sentence is clean.** Referee 1 could not
  have verified the index bookkeeping from the .txt at all (pdftotext prints A^m and A^{m′} identically —
  even (6.38) comes out as "A^m ⊂ A^m"); I confirmed the printed "For any m′ > m" and "W ⊂ A^{m′}(M)" and
  "E_{m′}: A^m(M) → Ȧ^{(s)}(M)" from the rendered page. The note's index remark is correct. **But** the
  note's own replacement sentence has a dangling relative clause — "bounded in some A^m(M), on which the
  topologies … coincide" — whose nearest antecedent makes the note assert exactly the false Cor. 6.14.
  One-word fix given in 3e. Also noted: p. 48's "By Corollary 6.8" is a slip for Proposition 6.8.
- Item 4: **AGREE (HOLDS).** Added: §10.2 should repeat the m′ < m index correction explicitly.
- Item 5: **AGREE (HOLDS).** Leibniz bound re-derived and independently re-run numerically (my own script,
  two genuine S^1 symbols, β up to 3, edge artifacts removed). **Added:** the paper's own Remark 3.7, p. 18
  ("Another proof of Corollary 3.5 could be given like in Proposition 6.10") already anticipates the repair;
  the note should acknowledge it.
- Item 6: **AGREE (HOLDS).** Threshold k ≤ m̄ confirmed exact by two independent cross-checks ((7.37)+(4.12);
  the standard order of δ_L). Coefficient-topology lemma proved in both directions. **Added:** Cor. 6.27 is
  better derived from **(6.45)/(6.47)** than from (6.49) — (6.49) rests on Cor. 6.20 ← Prop. 6.19 ←
  **Cor. 6.16**, i.e. on one of the statements being repaired (no circularity, but an avoidable dependency).
- Item 7: **AGREE.** Added the Cor. 4.7 observation (its printed Montel proof also invokes Cor. 3.6 over a
  non-compact base).

Net recommendation to the sponsor: the companion's §§9.6, 9.7, 10 survive hostile re-derivation. Before
sending, make four edits — (a) the A^m-Fréchet citation in §9.7; (b) the c-sign sentence in §9.6; (c) the
"on which" wording in the note's §4 Claim-6.46 clause; (d) swap (6.49) for (6.45)/(6.47) in the Cor. 6.27
clause. (a) is mathematically necessary; (b)–(d) are correctness-of-reading matters that a hostile author
would seize on.

Finished: machine clock below.
Sun Sep  6 13:34:08 IST 2026
