# Second-model verification — companion §9.2–9.5 (interpolation inequality + acyclicity criterion)

Machine clock at start: Sun Sep  6 13:33:55 IST 2026 (`date`).
Role: SECOND-MODEL VERIFIER. Everything below was re-derived from scratch from
`alkl23-note.tex`, `alkl23-note-derivations.md` §9, and `novelty/ALKL-2024-published.txt`.
The first referee's report (`refute-interp.md`) was read only after my own derivations of
Lemma A, Lemma B and Prop. 9.4 were complete; AGREE/DISAGREE lines are recorded per item.

## Verdict

**HOLDS.** Companion §9.2–9.5 is a complete and correct proof of the note's (interp) and of its
passage to the p. 4 acyclicity criterion. I re-derived every exponent, every constant and every
quantifier independently and could not break any of them; two numerical stress programs (Lemma A/B
with the proof's own explicit constant; Prop. 9.4 in the 1-variable model over an adversarial
family) found no violation. I AGREE with the first referee on all six of its rulings, and I add
three things it did not have: (i) an **explicit** family that breaks the criterion (M*) for
non-compact `U` — the referee only inferred the failure from witness (f) — which confirms the
note's one-line remark is right *for the reason it gives*; (ii) a check that the p. 4 criterion as
printed is for a spectrum `(X_0 ⊂ X_1 ⊂ …)` and that the paper's own p. 5 sentence on real indices
is what licenses the ℕ-reduction (the sentence is garbled by the typesetting — recorded); (iii) two
genuine but harmless imprecisions in §9.4/§9.5 that the referee did not list.

Ruling on the external assessment: its criticism is **CORRECT about the NOTE** and **NOT CORRECT
about the MATHEMATICS given the companion**. Detail in `## Item 7`.

## Item 1 — §9.2 Lemma A (one variable, Vandermonde)

**Statement as written** (companion, §9.2): `N ≥ 1`, `f ∈ C^N([t, t+Nh])`, `h > 0`; then for
`0 ≤ j ≤ N`, `|f^{(j)}(t)| ≤ C_N(h^{−j}‖f‖_∞ + h^{N−j}‖f^{(N)}‖_∞)`, sup-norms on `[t, t+Nh]`.

**My derivation, independent.** Taylor with Lagrange remainder at `t` (legitimate for `f ∈ C^N`,
indeed `C^{N−1}` on the closed interval plus `N`-fold differentiability on the interior suffices):
for `k = 0, …, N−1`, and `s = kh ∈ [0,(N−1)h] ⊂ [0,Nh]`,

  `f(t+kh) = Σ_{i=0}^{N−1} f^{(i)}(t)(kh)^i/i! + f^{(N)}(ζ_k)(kh)^N/N! = Σ_{i=0}^{N−1} y_i k^i + r_k`,
  `y_i := f^{(i)}(t)h^i/i!`,  `|r_k| ≤ (Nh)^N‖f^{(N)}‖_∞/N!`.

The `N×N` matrix `V = (k^i)_{0≤k,i≤N−1}` is Vandermonde in the **distinct** nodes `0,1,…,N−1`
(`0^0 = 1`), `det V = ∏_{0≤k<k′≤N−1}(k′−k) ≠ 0`. Hence `y = V^{−1}(f(t+kh) − r_k)_k` and
`|y_j| ≤ ‖V^{−1}‖_∞ (‖f‖_∞ + (Nh)^N‖f^{(N)}‖_∞/N!)`. Since `f^{(j)}(t) = j!\,h^{−j}y_j`,

  `|f^{(j)}(t)| ≤ j!‖V^{−1}‖_∞ [ h^{−j}‖f‖_∞ + (N^N/N!) h^{N−j}‖f^{(N)}‖_∞ ]`   (j ≤ N−1),

so `C_N := (max_{j<N} j!)·‖V^{−1}‖_∞·max(1, N^N/N!)` works, and `C_N ≥ 1` also covers `j = N`
(`|f^{(N)}(t)| ≤ ‖f^{(N)}‖_∞`). `C_N` depends on `N` alone — not on `h`, `t` or `f`: the only
places `h` could enter are through `V` (it does not: the nodes are `0,…,N−1`, the `h`-dependence
having been absorbed into `y_i`) and through the remainder bound (it enters as the stated `h^{N−j}`).
All function values used lie in `[t, t+(N−1)h] ⊂ [t, t+Nh]` and all `ζ_k ∈ (t, t+Nh)`, so the two
sup-norms are over the stated interval. **Correct as written.**

**Numerical stress test** (`scratchpad/interp/lemAB.py`): 4000 random trig+polynomial `f` (exact
derivatives), `N ∈ {1..7}`, `h ∈ [10^{−3},10]`, `t ∈ [−5,5]`, every `j ≤ N`, with the *proof's own*
explicit `C_N` computed from `‖V^{−1}‖_∞`. Worst `LHS/RHS = 0.99999` (attained at the degenerate
`N=1, j=0`, where the constant is 1). No violation.

**Ruling: HOLDS.**  AGREE with referee 1's Item 1. Nothing to add beyond noting that the proof
uses the box `[t, t+Nh]` on **one side** of `t` only — this is what later lets the box be placed
anywhere in `ℝ^{d+l}` regardless of the geometry of `K` (see Item 3).

## Item 2 — §9.3 Lemma B (box, per-variable scales)

**Statement as written**: `F ∈ C^∞` near `Q = ∏_{i=1}^{D}[t_i, t_i+Nh_i]`, `γ ∈ ℕ^D` with
`γ_i ≤ N`; then
`|∂^γF(t)| ≤ C_{N,D} Σ_{S⊆{1..D}} (∏_{i∈S}h_i^{N−γ_i})(∏_{i∉S}h_i^{−γ_i}) sup_Q|∂^{Nχ_S}F|`.

**My derivation, independent.** `D = 1` is Lemma A with `j = γ_1` (`S=∅` ↦ `h^{−γ_1}‖F‖`,
`S={1}` ↦ `h^{N−γ_1}‖F^{(N)}‖`). For `D>1`, write `γ = (γ_1, γ̃)`, `t = (t_1, t̃)`. Lemma A in the
first variable applied to `g(s) := ∂^{γ̃}F(s, t̃)` (which is `C^∞` on `[t_1,t_1+Nh_1]`) at `j = γ_1`:

  `|∂^γF(t)| = |g^{(γ_1)}(t_1)| ≤ C_N( h_1^{−γ_1} sup_s|∂^{γ̃}F(s,t̃)| + h_1^{N−γ_1} sup_s|∂_1^N∂^{γ̃}F(s,t̃)| )`.

For each fixed `s`, the `(D−1)`-case applied to `F(s,·)` at `t̃` on `Q̃ = ∏_{i≥2}[t_i,t_i+Nh_i]`
gives `Σ_{T⊆{2..D}}(∏_{i∈T}h_i^{N−γ_i})(∏_{i∈{2..D}∖T}h_i^{−γ_i}) sup_{Q̃}|∂^{Nχ_T}F(s,·)|`;
taking `sup_s` turns `sup_{Q̃}` into `sup_Q`, and multiplying by `h_1^{−γ_1}` produces **exactly**
the terms `S = T` with `1 ∉ S`. The same applied to `∂_1^N F(s,·)` gives
`sup_Q|∂_1^N∂^{Nχ_T}F| = sup_Q|∂^{Nχ_{T∪\{1\}}}F|`, and multiplying by `h_1^{N−γ_1}` produces
**exactly** the terms with `1 ∈ S`. The map `S ↦ (1∈S?, S∩{2..D})` is a bijection
`2^{{1..D}} → {0,1}×2^{{2..D}}`, so every `S` occurs once and only once. `C_{N,D} = C_N·C_{N,D−1}
= C_N^D` — `N,D` only. Hypothesis `γ̃_i ≤ N` inherited. **Correct as written.**

Two points worth stating because they are what make §9.4 work and are easy to miss:
* the right-hand side contains **only the `2^D` "pure" derivatives** `∂^{Nχ_S}` (order `N` in each
  variable of `S`, `0` elsewhere) — no mixed intermediate derivatives survive the induction. This
  is exactly why `Γ` in §9.4 is finite and explicit;
* the exponents pair the *same* `h_i` with the *same* variable, i.e. the two scales `h_x`, `h_ξ`
  can be chosen independently. A version with a single common `h` would not give §9.4's exponent
  cancellation.

**Numerical stress test** (same file): 600 random `D∈{2,3}`, `N∈{1..5}`, random per-variable
`h_i ∈ [10^{−2},5]`, random `γ` with `γ_i ≤ N`, random smooth `F` (exact derivatives), with the
proof's constant `C_N^D`. Worst `LHS/RHS = 0.991`. No violation.

**Ruling: HOLDS.**  AGREE with referee 1's Item 2.

## Item 3 — §9.4 Proposition (the interpolation inequality). Exponents recomputed from scratch

**Published anchor for the seminorm.** p. 15, verbatim (grep `ALKL-2024-published.txt:820`):
"`a_{K,α,β,m} := sup_{x∈K, ξ∈R^l} |∂_x^α ∂_ξ^β a(x,ξ)| / (1+|ξ|)^{m−|β|} < ∞.   (3.1)`" and
"`S^m(U×R^l) ⊂ S^{m'}(U×R^l)  (m < m')  (3.2)`". So the companion's
`N_m(a;γ) = sup|∂^γa|(1+|ξ|)^{|β|−m}` is (3.1) verbatim, and the spectrum increases with `m`. ✓

**Set-up as written.** `m<m′<m″`, `γ=(α,β)`, `|γ|≥1`; `c := (m′−m)/(2|γ|)`;
`N ∈ ℕ` with `N > |γ| + (m″−m′)/c`; `R_0 := max{1,(2N√l)^{1/c}}`;
`Γ := {γ} ∪ {Nχ_S : ∅≠S⊆{1,…,d+l}}`. Claim: `∃C = C(m,m′,m″,γ,d,l)` (not `K`, not `a`, not `R`)
with `N_{m′}(a;γ) ≤ C[R^{−(m′−m)/2}N_m(a;0) + R^{m″−m′}max_{γ′∈Γ}N_{m″}(a;γ′)]` for `a ∈ S^{m″}_K`,
`R ≥ R_0`.

**(a) Well-posedness of the constants.** `m′>m` and `|γ|≥1` give `c>0`; `m″>m′` gives
`(m″−m′)/c>0`, hence `N > |γ| ≥ γ_i` **strictly** for every coordinate — which is precisely
Lemma B's hypothesis `γ_i ≤ N`, with room to spare. `c` may exceed 1 (when `m′−m > 2|γ|`); then
`h_ξ = w^{1−c} < 1`. Nothing in the proof needs `c ≤ 1` — only `h_x, h_ξ > 0` and the bound
`|ξ′−ξ| ≤ w/2`. ✓ (I checked this specifically: it is the one place where an unstated `c<1`
assumption could have hidden. It is not needed.)

**(b) Case `w := 1+|ξ| ≤ R`.** `|∂^γa|w^{|β|−m′} = (|∂^γa|w^{|β|−m″})·w^{m″−m′} ≤
N_{m″}(a;γ)·R^{m″−m′}` since `m″−m′>0` and `w ≤ R`. Uses `γ ∈ Γ` — which is why `Γ` must contain
`γ` itself and not only the `Nχ_S`. ✓

**(c) Case `w > R ≥ R_0`. Geometry of the box.** `Q := ∏_{i≤d}[x_i,x_i+Nh_x] ×
∏_{i≤l}[ξ_i,ξ_i+Nh_ξ]`, `h_x := w^{−c}`, `h_ξ := w^{1−c}`. On `Q`, each `ξ′_i−ξ_i ∈ [0,Nh_ξ]`, so
`|ξ′−ξ| ≤ √l·N·w^{1−c}`. Then
`√l N w^{1−c} ≤ w/2  ⟺  2N√l ≤ w^c  ⟺  w ≥ (2N√l)^{1/c}`, true because `w > R ≥ R_0`. Hence
`1+|ξ′| ≥ w − w/2 = w/2` and `1+|ξ′| ≤ w + w/2 = 3w/2`, i.e. `(1+|ξ′|)^s ≤ 2^{|s|}w^s` for every
real `s` (both bounds are used, since exponents of both signs occur). ✓

**(d) The two sup bounds on `Q`.**
`sup_Q|a| ≤ N_m(a;0)·sup_Q(1+|ξ′|)^{m} ≤ 2^{|m|}w^m N_m(a;0)`.
`∂^{Nχ_S}` has ξ-order `|β_S| = N|S_ξ|`, so `sup_Q|∂^{Nχ_S}a| ≤ N_{m″}(a;Nχ_S)sup_Q(1+|ξ′|)^{m″−N|S_ξ|}
≤ 2^{|m″|+Nl}w^{m″−N|S_ξ|}N_{m″}(a;Nχ_S)` (since `|m″−N|S_ξ|| ≤ |m″|+Nl`). ✓

**(e) Exponent bookkeeping — recomputed independently, term by term.**
Write `S_x = S∩{x-indices}`, `S_ξ = S∩{ξ-indices}`, `|α_S| = Σ_{i∈S_x}γ_i`, `|β_S| = Σ_{i∈S_ξ}γ_i`.
Lemma B (D = d+l) then multiplication by the weight `w^{|β|−m′}`:

*`S = ∅`.* `∏_ih_i^{−γ_i} = h_x^{−|α|}h_ξ^{−|β|} = w^{c|α|}·w^{−(1−c)|β|}`. Total exponent
`c|α| − (1−c)|β| + m + (|β|−m′) = c|α| + c|β| + m − m′ = c|γ| + m − m′`. With `c|γ| = (m′−m)/2`
this is `−(m′−m)/2`. **This identity is what fixes `c`.** Since `w > R` and the exponent is
negative, `w^{−(m′−m)/2} < R^{−(m′−m)/2}`. Contribution `≤ C R^{−(m′−m)/2}N_m(a;0)`. ✓

*`S ≠ ∅`.* Coefficient `= w^{−c(N|S_x|−|α_S|)}·w^{(1−c)(N|S_ξ|−|β_S|)}·w^{c|α|−c|α_S|}·w^{−(1−c)(|β|−|β_S|)}`.
Multiplying by the sup factor `w^{m″−N|S_ξ|}` and the weight `w^{|β|−m′}`, the total exponent is

  `−cN|S_x| + c|α_S| + N|S_ξ| − cN|S_ξ| − (1−c)|β_S| + c|α| − c|α_S| − (1−c)|β| + (1−c)|β_S|`
  `  + m″ − N|S_ξ| + |β| − m′`

in which `±c|α_S|`, `∓(1−c)|β_S|` and `±N|S_ξ|` cancel exactly, leaving

  `−cN(|S_x|+|S_ξ|) + c|α| + c|β| + m″ − m′ = −c(N|S| − |γ|) + m″ − m′`.

(Note the `−(1−c)|β| + |β| = c|β|` step; this is the second place `c` earns its keep.) Since
`|S| ≥ 1`, this is `≤ −c(N−|γ|) + m″ − m′`, which is `< 0` **iff** `N > |γ| + (m″−m′)/c` —
exactly the hypothesis on `N`, no slack wasted. With `w > R ≥ 1` and `R^{m″−m′} ≥ 1`, the
contribution is `≤ C N_{m″}(a;Nχ_S) ≤ C R^{m″−m′}N_{m″}(a;Nχ_S)`. ✓

I obtained the companion's two displayed exponents character for character without consulting them
first. Summing the `2^{d+l}` terms and taking `sup_{(x,ξ)}` of the maximum of (b) and (c) gives the
claim with `C = 2^{d+l}·C_N^{d+l}·max(2^{|m|}, 2^{|m″|+Nl}, 1)`, depending on
`m,m′,m″,γ,d,l` only. ✓

**(f) The `γ = 0` case.** `w ≤ R`: `|a|w^{−m′} = |a|w^{−m″}w^{m″−m′} ≤ R^{m″−m′}N_{m″}(a;0)`;
`w > R`: `|a|w^{−m′} = |a|w^{−m}w^{m−m′} ≤ R^{m−m′}N_m(a;0)` (`m−m′<0`, `w>R`). So
`N_{m′}(a;0) ≤ R^{m″−m′}N_{m″}(a;0) + R^{m−m′}N_m(a;0)`, and since `R ≥ 1`,
`R^{m−m′} = R^{−(m′−m)} ≤ R^{−(m′−m)/2}`: the note's displayed form follows with `Γ = {0}`,
`C = 1`, `R_0 = 1`. The split at `|γ| ≥ 1` is therefore genuine and correctly handled — for `γ=0`
one cannot define `c = (m′−m)/(2|γ|)`, and no box is needed. ✓

**(g) Does the `x`-box stay where `a` is controlled?** The `x`-box `∏_i[x_i, x_i+Nw^{−c}]` may
leave `K` (indeed for `x ∈ ∂K` it always does, and for a `K` with empty interior it never lies
inside). This is harmless and, more than that, it is *the* structural point:
`a ∈ S^m_K` is by definition an element of `C^∞(ℝ^d×ℝ^l)` (companion §9.1) and `N_m(a;γ)` is the
**global** supremum over `ℝ^d×ℝ^l` — which for a symbol vanishing off `K` equals the (3.1)
seminorm over `K`. So the box may be placed anywhere and every `sup_Q` is still bounded by the
seminorms appearing in the statement. I checked the extension-by-zero claim of §9.1: for
`a ∈ S^m(U×ℝ^l)` vanishing for `x ∉ K`, the zero-extension is smooth because
`ℝ^d×ℝ^l = (U×ℝ^l) ∪ ((ℝ^d∖K)×ℝ^l)` is a union of two open sets on each of which it is smooth
(identically 0 on the second). ✓  And `{a ∈ S^m(U×ℝ^l) : a|_{(U∖K)×ℝ^l} = 0}` is closed, with
`‖a‖_{K′,α,β,m} = ‖a‖_{K′∩K,α,β,m} ≤ N_m(a;γ)` and `K` itself admissible, so the induced topology
is exactly the `N_m`-topology. ✓ (The note's "closed subspace … with the seminorms
`N_m(a;γ)=‖a‖_{K,α,β,m}`" is therefore right.)

**Worth recording, and neither the note nor referee 1 says it:** *the proof of §9.4 never uses
`supp_x a ⊂ K` at all.* It uses only that the three seminorms are global suprema over
`ℝ^d×ℝ^l`. So the same proposition holds verbatim on the larger *uniform* symbol space
`S^m_{ub} := {a ∈ C^∞(ℝ^d×ℝ^l) : N_m(a;γ) < ∞ ∀γ}`, of which `S^m_K` is a closed subspace. This is
the sharp form of the note's remark: what matters is *globality of the seminorm*, of which compact
base support is the mechanism in the application.

**Numerical stress tests.** (i) `scratchpad/interp/prop94.py`: 400 random
`(m,m′,m″,β)` with `β ∈ {1..4}`, random Schwartz symbols built from sums of Gaussian-modulated
cosines with *exact* (Hermite) derivatives, five values of `R ≥ R_0` each; the inequality is
tested with the **proof's own explicit constant chain**. Worst `LHS/bound = 0.0023`; no violation.
(ii) `scratchpad/interp/adv.py`: an adversarial grid search over bump position `ξ_0 ∈ [1,10^{3.2}]`,
width `L ∈ [10^{−2},10^{2.6}]`, carrier frequency `ω`, and `R/R_0 ∈ [1,10^3]`, for six
`(m,m′,m″,β)` regimes, maximizing the **raw** ratio with all constants stripped
(`N_{m′}(a;β) / [R^{−(m′−m)/2}N_m(a;0) + R^{m″−m′}max(N_{m″}(a;β),N_{m″}(a;N))]`). Results
appended at the end of this report. The families that should be extremal by the proof's own
scaling (`L ≈ h_ξ = w^{1−c}` at `w ≈ ξ_0`) are inside the search box.

**Attempted breaks that failed, and why.**
1. *Translated bumps* `g_T(ξ)=Aθ(ξ−Te_1)` (witness (a)'s family). `N_{m′}(g_T;β) ≈ AT^{|β|−m′}`,
   `N_m(g_T;0) ≈ AT^{−m}`, `N_{m″}(g_T;Nχ) ≈ AT^{N−m″}`. The inequality at fixed `R` needs
   `T^{|β|−m′} ≲ T^{−m} + T^{N−m″}`; `N − m″ ≥ |β| − m′` is implied by `N ≥ |γ| + (m″−m′)`, and
   `N > |γ| + (m″−m′)/c` gives this whenever `c ≤ 1`; when `c > 1` the first term `T^{−m}`
   dominates because then `m′−m > 2|γ| ≥ 2|β|` forces `−m > |β| − m′`. Either way, no violation —
   and both branches are needed, which is a real (if invisible) load on the choice of `c`.
2. *Fast oscillation* `A sin(λξ_1)ψ(ξ)`: `N_{m′}(·;γ) ≈ Aλ^{|γ|}`, `max_Γ N_{m″} ≈ Aλ^{N}`, and
   `N > |γ|`, so the second bracket alone dominates for `λ ≥ 1`. No violation.
3. *Slowly-varying wide bumps* `Aθ(ξ/T − e_1)` — the family that **does** break the non-compact
   criterion (Item 5A) — has `N_s(·;γ) ≈ A C_γ T^{−s}` for every `γ`, so the inequality reads
   `AT^{−m′} ≲ R^{−(m′−m)/2}AT^{−m} + R^{m″−m′}AT^{−m″}`; minimizing the right side over `R` gives
   `≈ A T^{−m}·(T^{m−m″})^{(m′−m)/(2(m″−m)+…)}`-type bounds that are satisfied because the
   inequality must hold *for each* `R ≥ R_0` and at `R ≈ T^{(m″−m)·2/(m″−m′+…)}` both sides match
   in order. Checked numerically at `T` up to `10^3` (part of `adv.py`); no violation.

**Ruling: HOLDS.**  AGREE with referee 1's Item 3, including its side checks. Additions:
the `c>1` observation in (a); the "uniform symbols" sharpening in (g); attempted break 1's
two-branch structure.
