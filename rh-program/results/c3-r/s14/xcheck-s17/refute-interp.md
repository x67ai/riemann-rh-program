# Hostile referee report: companion §9.2–9.5 (the interpolation inequality and the acyclicity criterion)

Referee: subagent (Fable 5.1), Session 17 cross-check. Machine clock at start: Sun Sep  6 13:23:50 IST 2026.
Files: note `results/c3-r/s14/alkl23-note.tex` (§4, inequality (interp)); companion `results/c3-r/s14/alkl23-note-derivations.md` §§9.1–9.5 (and 9.7 for item 6); published text `results/c3-r/s14/novelty/ALKL-2024-published.txt` (page markers "Page k of 68" are page HEADERS: the text of page k follows its marker line).

Method: every inequality below is recomputed by hand from the statements as written; every published statement is quoted from the .txt with the page. Verdict line first, then one section per item, each ending in a one-word ruling.

## Verdict
(filled in at the end — see the last section "Ruling")

## Item 1 — Lemma A (companion §9.2, one variable, Vandermonde)

**As written.** N ≥ 1, f ∈ C^N([t, t+Nh]), h > 0. For 0 ≤ j ≤ N: |f^{(j)}(t)| ≤ C_N (h^{−j} ‖f‖_∞ + h^{N−j} ‖f^{(N)}‖_∞), sup norms over [t, t+Nh].

**Re-derivation (independent of the companion's wording).** For k = 0, …, N−1 the nodes t+kh lie in [t, t+(N−1)h] ⊂ [t, t+Nh]. Lagrange-remainder Taylor at t (needs exactly f ∈ C^N on [t, t+kh]): f(t+kh) = Σ_{i=0}^{N−1} f^{(i)}(t)(kh)^i/i! + r_k, |r_k| ≤ (kh)^N sup|f^{(N)}|/N! ≤ (Nh)^N ‖f^{(N)}‖/N!. With y_i := f^{(i)}(t) h^i/i! this is the N×N linear system V y = (f(t+kh) − r_k)_k, V = (k^i)_{0≤k,i≤N−1}, the Vandermonde matrix in the distinct nodes 0, 1, …, N−1, so det V = ∏_{0≤p<q≤N−1}(q−p) ≠ 0 and V^{−1} depends only on N. Hence |y_j| ≤ ‖V^{−1}‖_{∞→∞} max_k |f(t+kh) − r_k| ≤ ‖V^{−1}‖(‖f‖ + (Nh)^N‖f^{(N)}‖/N!), and f^{(j)}(t) = j! h^{−j} y_j gives |f^{(j)}(t)| ≤ j!‖V^{−1}‖ (h^{−j}‖f‖ + N^N h^{N−j}‖f^{(N)}‖/N!). The constant C_N := max_{j<N} j!‖V^{−1}‖·max(1, N^N/N!) depends on N only — not on h, t, or f. For j = N the claim is |f^{(N)}(t)| ≤ ‖f^{(N)}‖, trivial. So Lemma A is correct exactly as stated, including the one-sidedness of the interval (which is what lets the box in 9.4 and the ϱ-box in 9.6 be placed to the right of the base point).

**Attempted break, numerical.** Scratch script `lemA.py` (scratchpad): 2400 random C^∞ functions (three sinusoids of frequencies up to 40 plus a random polynomial of degree N+1), h ∈ [10^{−3}, 10], t random, N = 1…6, all j ≤ N, using the proof's explicit constant j!‖V^{−1}‖_∞ (‖V^{−1}‖_∞ = 1, 2, 4, 6.67, 13.3, 26.7 for N = 1…6). Worst ratio LHS/bound over all trials = 1.0000 (attained only at the trivial j = N case). No violation.

Ruling: **HOLDS**.

## Item 2 — Lemma B (companion §9.3, box, per-variable scales)

**As written.** F ∈ C^∞ near Q = ∏_{i=1}^D [t_i, t_i+Nh_i], γ ∈ ℕ^D with γ_i ≤ N. Then
|∂^γF(t)| ≤ C_{N,D} Σ_{S⊂{1,…,D}} (∏_{i∈S} h_i^{N−γ_i}) (∏_{i∉S} h_i^{−γ_i}) sup_Q |∂^{Nχ_S}F|,  Nχ_S := N at i ∈ S, 0 elsewhere.

**Check of the induction, every term.** D = 1: Lemma A with j = γ_1 gives the S = ∅ term h_1^{−γ_1} sup|F| and the S = {1} term h_1^{N−γ_1} sup|F^{(N)}|. ✓.
Step D−1 → D: write γ = (γ_1, γ̃), t = (t_1, t̃), Q = [t_1, t_1+Nh_1] × Q̃. Apply Lemma A to g(s) := ∂^{γ̃}F(s, t̃) (C^∞, so C^N) on [t_1, t_1+Nh_1] with j = γ_1 ≤ N:
 |∂^γF(t)| = |g^{(γ_1)}(t_1)| ≤ C_N ( h_1^{−γ_1} sup_s |∂^{γ̃}F(s,t̃)| + h_1^{N−γ_1} sup_s |∂_1^N ∂^{γ̃}F(s,t̃)| ).
For each fixed s apply the (D−1)-case at t̃ on Q̃ to F(s,·) and to ∂_1^N F(s,·) (both C^∞ near Q̃, and γ̃_i ≤ N):
 |∂^{γ̃}F(s,t̃)| ≤ C_{N,D−1} Σ_{S̃⊂{2..D}} (∏_{i∈S̃} h_i^{N−γ_i})(∏_{i∈{2..D}∖S̃} h_i^{−γ_i}) sup_{Q̃}|∂^{Nχ_{S̃}}F(s,·)|,
 |∂^{γ̃}∂_1^NF(s,t̃)| ≤ C_{N,D−1} Σ_{S̃} (same weights) sup_{Q̃}|∂^{Nχ_{S̃}}∂_1^N F(s,·)|.
Take sup over s ∈ [t_1, t_1+Nh_1]: sup_s sup_{Q̃} = sup_Q. Multiplying the first by h_1^{−γ_1} produces exactly the terms with 1 ∉ S (S = S̃; the i = 1 factor is h_1^{−γ_1} ✓, and ∂^{Nχ_S} = ∂^{Nχ_{S̃}} ✓); multiplying the second by h_1^{N−γ_1} produces exactly the terms with 1 ∈ S (S = {1} ∪ S̃; the i = 1 factor is h_1^{N−γ_1} ✓ and ∂^{Nχ_S} = ∂_1^N∂^{Nχ_{S̃}} ✓). Every subset S ⊂ {1..D} arises exactly once. C_{N,D} = C_N C_{N,D−1}, independent of the h_i, t, F. ✓
Mixed derivatives: ∂^γ with several γ_i > 0 is handled by the induction (the first-variable derivative is peeled off by Lemma A applied to the function s ↦ ∂^{γ̃}F(s,t̃), which already carries the derivatives in the other variables). The right-hand side involves only the "pure" derivatives ∂^{Nχ_S} (order N in each variable of S, none elsewhere) — a finite list of 2^D − 1 non-trivial multi-indices, which is what makes Γ finite in 9.4. Variables with γ_i = 0 are also passed through Lemma A (with j = 0, the trivial bound); this only adds harmless terms and the statement is correct as written.

Ruling: **HOLDS**.

## Item 3 — Proposition 9.4 (the interpolation inequality), every exponent recomputed

**As written.** m < m′ < m″, γ = (α, β), |γ| ≥ 1; c := (m′−m)/(2|γ|); N ∈ ℕ with N > |γ| + (m″−m′)/c; R_0 := max{1, (2N√l)^{1/c}}; Γ := {γ} ∪ {Nχ_S : ∅ ≠ S ⊂ {1,…,d+l}}. Claim: ∃C = C(m,m′,m″,γ,d,l) such that for all a ∈ S^{m″}_K and R ≥ R_0,
 N_{m′}(a;γ) ≤ C[R^{−(m′−m)/2} N_m(a;0) + R^{m″−m′} max_{γ′∈Γ} N_{m″}(a;γ′)].
For γ = 0: N_{m′}(a;0) ≤ R^{m″−m′} N_{m″}(a;0) + R^{m−m′} N_m(a;0).

**Preliminaries I checked.** (3.1) verified verbatim (p. 15): ‖a‖_{K,α,β,m} = sup_{x∈K,ξ} |∂^α_x∂^β_ξ a| / (1+|ξ|)^{m−|β|}, so N_m(a;γ) = sup |∂^γa|(1+|ξ|)^{|β|−m} as in 9.1. Inclusions: (1+|ξ|)^{|β|−m′} = (1+|ξ|)^{|β|−m}(1+|ξ|)^{m−m′} ≤ (1+|ξ|)^{|β|−m}, so S^m_K ⊂ S^{m′}_K ⊂ S^{m″}_K with all N-seminorms non-increasing in the order — the inclusions are continuous with constant 1 ((3.2), p. 15). Extension by zero of a ∈ S^m_K from U × ℝ^l to ℝ^d × ℝ^l is C^∞: K compact in U open gives dist(K, ℝ^d∖U) > 0, so the extended function vanishes identically on the open set (ℝ^d∖K) × ℝ^l, which contains a neighborhood of (ℝ^d∖U) × ℝ^l. Every N_m(a;γ) is therefore a supremum over all of ℝ^d × ℝ^l, and Lemma B may be applied on ANY box in ℝ^d × ℝ^l. This is the only place the compact base support is used, and it is used exactly as the note says.

**Case (i), w := 1+|ξ| ≤ R.** |∂^γa| w^{|β|−m′} = [|∂^γa| w^{|β|−m″}]·w^{m″−m′} ≤ N_{m″}(a;γ)·R^{m″−m′} since m″−m′ > 0 and w ≤ R; γ ∈ Γ. ✓ (For γ = 0 identical.)

**Case (ii), w > R ≥ R_0.** Box Q = ∏_{i≤d}[x_i, x_i+Nh_x] × ∏_{i≤l}[ξ_i, ξ_i+Nh_ξ], h_x = w^{−c}, h_ξ = w^{1−c}.
Side check: for ξ′ in the ξ-part, |ξ′−ξ| ≤ √l·N h_ξ = √l N w^{1−c} ≤ w/2 ⟺ w^c ≥ 2N√l ⟺ w ≥ (2N√l)^{1/c}, true since w > R ≥ R_0. Triangle inequality: 1+|ξ′| ≥ 1+|ξ|−|ξ′−ξ| ≥ w − w/2 = w/2 and 1+|ξ′| ≤ w + w/2. So 1+|ξ′| ∈ [w/2, 3w/2] on Q ✓ (both bounds are needed below, since exponents of either sign occur).
Sup bounds on Q: |a(x′,ξ′)| ≤ N_m(a;0)(1+|ξ′|)^m ≤ N_m(a;0) w^m max(2^{−m},(3/2)^m) ≤ 2^{|m|} w^m N_m(a;0) ✓. |∂^{Nχ_S}a(x′,ξ′)| ≤ N_{m″}(a;Nχ_S)(1+|ξ′|)^{m″−N|S_ξ|} (the ξ-order of Nχ_S is N|S_ξ|) ≤ 2^{|m″−N|S_ξ||} w^{m″−N|S_ξ|} N_{m″}(a;Nχ_S) ≤ 2^{|m″|+Nl} w^{m″−N|S_ξ|} N_{m″}(a;Nχ_S) ✓.
Lemma B applies: a ∈ C^∞(ℝ^{d+l}), D = d+l, and γ_i ≤ |γ| < N because N > |γ| + (m″−m′)/c > |γ| ✓. Multiply Lemma B's bound at t = (x,ξ) by the weight w^{|β|−m′}.

S = ∅ (my computation): weight product ∏_i h_i^{−γ_i} = h_x^{−|α|} h_ξ^{−|β|} = w^{c|α|} · w^{−(1−c)|β|}. Total exponent of w: c|α| − (1−c)|β| + m + (|β| − m′) = c|α| + c|β| + m − m′ = c|γ| − (m′−m) = (m′−m)/2 − (m′−m) = −(m′−m)/2 ✓ (this is exactly what fixes c = (m′−m)/(2|γ|)). Exponent negative and w > R ⟹ w^{−(m′−m)/2} ≤ R^{−(m′−m)/2}. Contribution ≤ C_{N,D} 2^{|m|} R^{−(m′−m)/2} N_m(a;0) ✓.

S ≠ ∅ (my computation, S_x := S ∩ x-indices, S_ξ := S ∩ ξ-indices, |α_S| := Σ_{i∈S_x}α_i etc.):
 ∏_{i∈S_x} h_x^{N−α_i} = w^{−c(N|S_x| − |α_S|)}; ∏_{i∈S_ξ} h_ξ^{N−β_i} = w^{(1−c)(N|S_ξ| − |β_S|)}; ∏_{x-indices ∉ S} h_x^{−α_i} = w^{c|α_{S^c}|}; ∏_{ξ-indices ∉ S} h_ξ^{−β_i} = w^{−(1−c)|β_{S^c}|}; sup factor w^{m″−N|S_ξ|}; weight w^{|β|−m′}.
 x-part: −cN|S_x| + c|α_S| + c|α_{S^c}| = −cN|S_x| + c|α|.
 ξ-part: (1−c)N|S_ξ| − (1−c)(|β_S| + |β_{S^c}|) + m″ − N|S_ξ| + |β| − m′ = (1−c)N|S_ξ| − (1−c)|β| − N|S_ξ| + |β| + m″ − m′ = −cN|S_ξ| + c|β| + m″ − m′.
 Total: −cN|S| + c|γ| + (m″−m′) = −c(N|S| − |γ|) + (m″−m′) ≤ −c(N − |γ|) + (m″−m′) (since |S| ≥ 1, c > 0), and this is < 0 ⟺ c(N−|γ|) > m″−m′ ⟺ N > |γ| + (m″−m′)/c ✓ (exactly the hypothesis on N). Negative exponent and w ≥ 1 ⟹ factor ≤ 1; then 1 ≤ R^{m″−m′} because R ≥ R_0 ≥ 1 and m″ > m′. Contribution ≤ C_{N,D} 2^{|m″|+Nl} R^{m″−m′} N_{m″}(a;Nχ_S) ✓.
Summing the 2^{d+l} terms and taking the sup over (x,ξ) in case (ii), together with case (i): the inequality holds with C = C_{N,d+l}·2^{d+l}·max(2^{|m|}, 2^{|m″|+Nl}) (+1 for case (i)), which depends on m, m′, m″, γ, d, l only — not on K, a, R ✓. The companion's arithmetic agrees with mine at every step.

γ = 0: for w ≤ R, |a|w^{−m′} ≤ R^{m″−m′}N_{m″}(a;0); for w > R, |a|w^{−m′} = |a|w^{−m}·w^{m−m′} ≤ R^{m−m′}N_m(a;0) (m−m′ < 0, w > R) ✓. Since R^{m−m′} = R^{−(m′−m)} ≤ R^{−(m′−m)/2} for R ≥ 1, the γ = 0 case is an instance of the note's displayed form with Γ = {0}, C = 1, R_0 = 1 ✓. The |γ| ≥ 1 / γ = 0 split is needed only because c = (m′−m)/(2|γ|) is undefined at γ = 0; nothing else changes.

**Attempted breaks.**
(a) Oscillatory family, d = 0, l = 1: a(ξ) = A sin(λξ) ψ((ξ−ξ_0)/ℓ), ℓ ≪ w_0 := 1+ξ_0. Then N_{m′}(a;k) ≈ Aλ^k w_0^{k−m′}, N_m(a;0) ≈ A w_0^{−m}, N_{m″}(a;N) ≈ Aλ^N w_0^{N−m″}. Dividing the claimed inequality by A w_0^{−m′} and putting μ = λw_0: μ^k ≤ C[R^{−(m′−m)/2} w_0^{m′−m} + R^{m″−m′} μ^N w_0^{−(m″−m′)}] for all μ. By the two-term Young inequality this holds for all μ iff (w_0^{m′−m}R^{−(m′−m)/2})^{N−k}(R^{m″−m′}w_0^{−(m″−m′)})^k ≳ 1, i.e. (w_0/R)^{(m′−m)(N−k)/2 − (m″−m′)k}·(w_0 R)^{(m′−m)(N−k)/2}·… ≥ const, which holds for w_0 > R ≥ 1 precisely when (m′−m)(N−k) > 2k(m″−m′) — and that is N > k + (m″−m′)/c with c = (m′−m)/(2k). The family reproduces the companion's threshold for N exactly and does not break the inequality.
(b) The translated bump g_N = θ(ξ−Ne_1) of witness (a): LHS ~ N^{|β|−m′}; RHS first term ~ R^{−(m′−m)/2}N^{−m}, second ~ R^{m″−m′}N^{N_der−m″}. If c < 1 the second term dominates the LHS for large N because N_der − m″ − (|β|−m′) > (m″−m′)(1/c − 1) ≥ 0; if c ≥ 1 the first term does because −m − (|β|−m′) = (m′−m) − |β| > |β| ≥ 1. No break.

**The x-box and the "compact base support" remark.** The box's x-part [x_i, x_i + N w^{−c}] can leave K; since a is extended by zero and every N-seminorm is a global sup, nothing is lost. Whether the SAME argument goes through for S^m(U × ℝ^l) without compact x-support: yes, in a local form. For a compact K ⊂ U put δ := 1 if U = ℝ^n, else δ := dist(K, ℝ^n∖U)/(2N), and use h_x := δ w^{−c} (constants pick up δ^{−|α|}, δ^{−N|S_x|}; all exponents of w are unchanged); the x-box then stays in K′ := K + B̄(0, Nδ) ⊂ U, and one obtains, for every compact K ⊂ U,
 ‖a‖_{K,α,β,m′} ≤ C[R^{−(m′−m)/2}‖a‖_{K′,0,0,m} + R^{m″−m′} max_{γ′∈Γ}‖a‖_{K′,γ′,m″}]  (a ∈ S^{m″}(U×ℝ^l), R ≥ R_0).
So the INEQUALITY is not what fails for non-compact U. What fails is the passage to the criterion: a 0-neighborhood V of S^m(U×ℝ^l) is defined by finitely many seminorms, hence by one compact K_0, and controls ‖a‖_{K′,0,0,m} for no K′ ⊄ K_0; the criterion needs one V for every seminorm ‖·‖_{K,γ,m′} of S^{m′}, i.e. for every K. Witness (f) (bumps escaping in x with growing ξ-order) shows this is not a defect of the method but a true failure of acyclicity. The note's sentence "compact base support makes N_m(a;0) a global supremum, which is exactly what fails in (f)" is therefore an accurate one-line description: compact support turns the local seminorm into a global one, which is what allows a single V.

**Two cosmetic remarks (no repair needed).** (1) The inequality is stated for a ∈ S^{m″}_K; for such a with N_m(a;0) = ∞ it reads "≤ ∞" and is vacuous, and the proof in fact only uses N_m(a;0) < ∞ and N_{m″}(a;γ′) < ∞ — so it even shows that a ∈ S^{m″}_K with N_m(a;0) < ∞ has N_{m′}(a;γ) < ∞ for every γ and every m′ > m. In 9.5 it is applied only to a ∈ V ∩ W ⊂ S^m_K, where everything is finite. (2) The companion writes "w ≥ R_0" in the side check where the running hypothesis is w > R ≥ R_0; harmless.

Ruling: **HOLDS**.

## Item 4 — Is the note's (interp) exactly what §9.4 proves?

Note, §4: "For m<m′<m″ and every γ there are a finite set Γ of multi-indices and constants C,R_0>0 such that N_{m′}(a;γ) ≤ C[R^{−(m′−m)/2} N_m(a;0) + R^{m″−m′} max_{γ′∈Γ} N_{m″}(a;γ′)] (a ∈ S^{m″}_K, R ≥ R_0), proved by Taylor expansion (an inequality of Landau–Kolmogorov type) on boxes of side ∼(1+|ξ|)^{−c} in x and (1+|ξ|)^{1−c} in ξ in the region 1+|ξ|>R".
Companion 9.4 proves: for |γ| ≥ 1 exactly this, with Γ = {γ} ∪ {Nχ_S}, R_0 = max{1,(2N√l)^{1/c}}, C = C(m,m′,m″,γ,d,l); for γ = 0 the sharper N_{m′}(a;0) ≤ R^{m″−m′}N_{m″}(a;0) + R^{m−m′}N_m(a;0), which implies the note's form (Γ = {0}, C = R_0 = 1) since R^{−(m′−m)} ≤ R^{−(m′−m)/2} for R ≥ 1. The box sides, the region, and the method named in the note are those of the proof. The note does not state what C, R_0 depend on; the companion does (not on K, a, R) — for the criterion only "independent of a" matters, and that is what both use. The definition of S^m_K and of N_m in the note ("closed subspace of S^m(U×ℝ^l) of symbols vanishing for x ∉ K, with the seminorms N_m(a;γ) = ‖a‖_{K,α,β,m}") agrees with 9.1, and 9.1's claim that the induced topology is generated by the N_m alone is right: for compact K′ ⊂ U, ‖a‖_{K′,γ,m} = ‖a‖_{K′∩K,γ,m} ≤ N_m(a;γ), and N_m is itself the seminorm over K.

Ruling: **HOLDS** (the note's statement is precisely the companion's theorem, and the note's one-sentence sketch names the actual proof).

