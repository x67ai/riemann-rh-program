# Second-model verification — companion §9.2–9.5 (interpolation inequality + acyclicity criterion)

Machine clock at start: Sun Sep  6 13:33:55 IST 2026 (`date`).
Role: SECOND-MODEL VERIFIER. Everything below was re-derived from scratch from
`alkl23-note.tex`, `alkl23-note-derivations.md` §9, and `novelty/ALKL-2024-published.txt`.
The first referee's report (`refute-interp.md`) was read only after my own derivations of
Lemma A, Lemma B and Prop. 9.4 were complete; AGREE/DISAGREE lines are recorded per item.

## Verdict

**HOLDS.** Companion §9.2–9.5 is a complete and correct proof of the note's (interp) and of its
passage to the p. 4 acyclicity criterion. I re-derived every exponent, every constant and every
quantifier independently and could not break any of them; four numerical stress programs (Lemma A and Lemma B
against the proof's own explicit constants; Prop. 9.4 in the one-variable model against the proof's
constant chain; an adversarial parameter search on the raw ratio; and a sharpness probe) found no
violation of anything §9.4 asserts. I AGREE with the first referee on all six of its rulings (and DISAGREE with one subsidiary
sharpness claim inside its Item 3 — a factor-2 algebra slip, detailed under Item 3b), and I add
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

## Item 3b — is the hypothesis `N > |γ| + (m″−m′)/c` load-bearing, and is it sharp?

(The note does not ask; referee 1 asks it inside its Item 3 "attempted break (a)" and gets the
answer wrong by a factor of 2 — the DISAGREE below.)

Yes, and of the right shape. Take `d = 0`, `l = 1`, `γ = β ≥ 1`, `g_T(ξ) := θ(ξ − T)` (witness (a)'s
family), `θ` a fixed bump. Then `N_{m′}(g_T;β) ≍ T^{β−m′}`, `N_m(g_T;0) ≍ T^{−m}`,
`N_{m″}(g_T;β′) ≍ T^{β′−m″}`. Suppose (interp) held at fixed `R` with `Γ′ = {γ} ∪ {N′χ_S}`. Letting
`T → ∞` forces `β − m′ ≤ max(−m, max(β,N′) − m″)`, i.e. **either** `β ≤ m′−m` (equivalently
`c ≥ 1/2`) **or** `N′ ≥ |γ| + (m″−m′)`. So whenever `m′−m < |γ|` the set `Γ` must contain
derivatives of order at least `|γ| + (m″−m′)`; `Γ` therefore genuinely depends on `γ` and cannot be
replaced by one `γ`-independent finite set. Consequences:
* the note's quantifier order — "for **every** `γ` there are a finite set `Γ` and constants `C,R_0`"
  — is the correct one, and a reader who read it as one `Γ` serving all `γ` would be reading a
  false statement. The note's wording is right; this is worth knowing because §9.5 uses
  `⋃_i Γ_i` over the finitely many `γ_i` of the given neighborhood `O`, which is exactly what the
  correct quantifier order permits;
* a second, sharper family gives a stronger necessary condition, and it is where I **DISAGREE**
  with referee 1 (see the box below): `N ≥ |γ| + (m″−m′)/(2c)`. The companion's
  `N > |γ| + (m″−m′)/c` is a factor 2 above it in the second term — sufficient, of the right shape,
  and **not sharp**. That costs nothing (any finite `Γ` does); I record it only so that no later
  reader mistakes it for a sharp threshold.

### DISAGREE with referee 1 (Item 3, "attempted break (a)")

Referee 1 runs the oscillatory family `a(ξ) = A sin(λξ)ψ((ξ−ξ_0)/ℓ)` (`d=0`, `l=1`, `ℓ ≪ w_0 := 1+ξ_0`,
`λℓ ≫ 1`) and concludes: "*this holds for all μ iff … `(m′−m)(N−k) > 2k(m″−m′)` — and that is
`N > k + (m″−m′)/c` … The family reproduces the companion's threshold for `N` exactly.*"
**The factor 2 is spurious and the conclusion "exactly" is wrong.** My recomputation:
with `μ := λw_0`, `P := R^{−(m′−m)/2}w_0^{m′−m}`, `Q := R^{m″−m′}w_0^{−(m″−m′)}`, the inequality
reads `μ^k ≤ C[P + Qμ^N]` for all `μ ≥ 1`, and
`min_{μ>0}(Pμ^{−k}+Qμ^{N−k}) = \tfrac{N}{N−k}(\tfrac{k}{N−k})^{−k/N} P^{(N−k)/N}Q^{k/N} ≍ P^{(N−k)/N}Q^{k/N}`.
So the family is survivable iff `P^{N−k}Q^{k} ≳ 1`, i.e. iff

  `w_0^{(m′−m)(N−k)−(m″−m′)k} · R^{−(m′−m)(N−k)/2+(m″−m′)k} ≳ 1`.

Referee 1 factors this as `(w_0/R)^{a}(w_0R)^{b}` with `a = (m′−m)(N−k)/2 − (m″−m′)k`,
`b = (m′−m)(N−k)/2`; that reproduces the `w_0`-exponent but gives the `R`-exponent `−a+b = (m″−m′)k`,
whereas the true one is `−(m′−m)(N−k)/2 + (m″−m′)k`. Reading off `a > 0` then yields the spurious
factor 2. Doing it correctly: writing `R = w_0^{t}` (the binding range is `R_0 ≤ R < w_0`; for
`R ≥ w_0` case (i) settles the point trivially), the exponent of `w_0` is linear in `t` with value
`A_1 − A_2` at `t=0` and `A_1/2` at `t=1`, where `A_1 := (m′−m)(N−k)`, `A_2 := (m″−m′)k`. Since
`A_1/2 ≥ 0` always, the condition is `A_1 ≥ A_2`, i.e.

  **`N ≥ |γ| + (m″−m′)/(2c)`**  — not `N > |γ| + (m″−m′)/c`.

**Numerically confirmed** (`scratchpad/interp/sharp2.py`), at `m=0, m′=1, m″=3, k=1` (`c = 1/2`;
my threshold `N ≥ 3`, the companion's `N > 5`), running the family at its own optimal
`λ* = μ*/w_0` with `R = R_0`:

```
 N'=2 : raw ratio 1.994, 3.425, 6.250, 10.83, 19.77   at w0 = 1e3,3e3,1e4,3e4,1e5
        -> grows exactly like w0^{1/2} (19.77/1.994 = 9.91 vs 100^{1/2} = 10): (interp) is FALSE
           with Gamma = {k, 2}
 N'=3 : raw ratio 0.0672, 0.1479, 0.1599, 0.1602, 0.1602  -> saturates: borderline, as predicted
 N'=4 : raw ratio 0, 0, 0.0088, 0.0216, 0.0185           -> small and non-growing
```
So `N′ = 3 = |γ| + (m″−m′)/(2c)` already survives this family while the companion demands `N ≥ 6`.

**Consequence for the verdict: none.** Over-choosing `N` only enlarges `Γ`, which the statement
allows (`Γ` is any finite set). §9.4 remains correct as written, and referee 1's HOLDS on Item 3
stands. What falls is its subsidiary claim of sharpness — worth correcting so that no later reader
tries to "improve" §9.4 by trusting a threshold that was never established.

**Ruling: HOLDS** (hypothesis sufficient as stated; necessary in shape, with the true necessary
threshold a factor 2 lower in the second term).

## Item 4 — is the NOTE's (interp) exactly what §9.4 proves?

Note, §4, verbatim: "For a compact `K ⊂ U` let `S^m_K` be the closed subspace of `S^m(U×R^l)` of
symbols vanishing for `x ∉ K`, with the seminorms `N_m(a;γ)=‖a‖_{K,α,β,m}`, `γ=(α,β)`. For
`m<m′<m″` and every `γ` there are a finite set `Γ` of multi-indices and constants `C,R_0>0` such
that `N_{m′}(a;γ) ≤ C[R^{−(m′−m)/2}N_m(a;0)+R^{m″−m′}max_{γ′∈Γ}N_{m″}(a;γ′)]` `(a ∈ S^{m″}_K, R ≥ R_0)`,
proved by Taylor expansion (an inequality of Landau–Kolmogorov type) on boxes of side
`∼(1+|ξ|)^{−c}` in `x` and `(1+|ξ|)^{1−c}` in `ξ` in the region `1+|ξ|>R`".

Item by item against §9.4: the space and seminorms — companion §9.1, and (3.1) verbatim (p. 15) ✓;
quantifier order (`∀γ ∃Γ,C,R_0 ∀a ∀R≥R_0`) ✓ and, by Item 3b, the only correct one; the two
exponents `−(m′−m)/2` and `m″−m′` ✓ (recomputed in Item 3(e)); the box sides `h_x = w^{−c}`,
`h_ξ = w^{1−c}` and the region `w > R` ✓; "Landau–Kolmogorov type" ✓ (Lemma A is exactly the
Landau–Kolmogorov finite-interval inequality, obtained here by Vandermonde inversion rather than
by the classical extremal-function route). The `γ = 0` case, which the note's "every `γ`" includes,
is covered by §9.4's final display and is *stronger* than the displayed form (Item 3(f)).
`a ∈ S^{m″}_K` rather than `a ∈ S^m_K`: harmless — if `N_m(a;0) = ∞` the inequality is trivially
true, and every use in §9.5 has `a ∈ V ⊂ S^m_K` where it is finite.

One thing the note asserts that §9.4 does **not** prove, and which is used in §4: `S^m_K` is a
*Fréchet* space, and `⋃_m S^m_K` an LF-space with Fréchet steps (needed to invoke the p. 5
"steps Fréchet ⟹ the properties depend only on `X`" and "acyclic ⟺ boundedly/compactly/sequentially
retractive"). §9.1 asserts it in one parenthesis ("Fréchet (weighted `C^∞` space; Cauchy sequences
converge locally uniformly with all derivatives and the bounds pass to the limit)"). I checked it:
countably many seminorms `N_m(·;γ)`, `γ ∈ ℕ^{d+l}` ✓ metrizable; a Cauchy sequence converges in
`C^∞_loc(ℝ^d×ℝ^l)` (each `N_m(·;γ)` dominates the uniform norm of `∂^γ` on compacta up to a
positive weight factor), the limit vanishes off `K` and inherits every bound ✓; and the convergence
is in the `N_m` seminorms by the usual `ε/3` split at `|ξ| ≤ R`/`|ξ| > R` ✓. Complete ✓. So the
claim is true, but it is a one-line assertion in the companion, not a proof. Recorded as the only
gap I found in the note↔companion match, and it is a trivial one.

**Ruling: HOLDS.**  AGREE with referee 1's Item 4; the Fréchet-step verification is my addition.

## Item 5 — §9.5: (interp) ⟹ the p. 4 criterion; the transfer rules

**The criterion, quoted verbatim** (published p. 4, lines 199–204 of the .txt): "Some homological
theory of LCSs will be used (see [39] and references therein) For instance, for an inductive
spectrum of LCSs of the form `(X k ) = (X 0 ⊂ X 1 ⊂ · · · )`, the condition of being acyclic can be
described as follows [39, Theorem 6.1]: for all k, there is some `k ≥ k` such that, for all
`k ≥ k`, the topologies of `X k` and `X k` coincide on some 0-neighborhood of `X k` ." (the primes
are lost by `pdftotext`; the sense is `k′ ≥ k`, `k″ ≥ k′`, topologies of `X_{k′}` and `X_{k″}`,
0-neighborhood of `X_k`). Two things the paper says here that matter and that I checked:
* it is a **characterization** ("the condition of being acyclic can be described as follows"), so
  failing it is failing acyclicity — used in Item 5A;
* it is stated for a spectrum **indexed by `ℕ`** with inclusions. p. 5 licenses the passage from
  the `ℝ`-indexed symbol filtration: "The above concepts and properties also apply to an
  inductive/projective spectrum consisting of continuous inclusions `X r ⊂ X r` for `r < r` in `R`
  because `∪_r X_r = ∪_k X_{r_k}` and `∩_r X_r = ∩_k X_{s_k}` for sequences `r_k ↓ −∞` and
  `s_k ↑ ∞`." (The pairing of the two sequences with the two operations is transposed in the
  published typesetting — for an increasing family the union is cofinal along `s_k ↑ ∞` — but the
  cofinality point is unambiguous.) So the companion's "(indices in ℕ by cofinality, p. 5)" is
  correctly sourced. ✓

**(M*) at `(m,m′,m″)`, re-derived.** `V := {a ∈ S^m_K : N_m(a;0) < 1}` — a 0-neighborhood of
`S^m_K` (one seminorm ball) and absolutely convex (`N_m(·;0)` is a seminorm — in fact a norm). Let
`O = {N_{m′}(·;γ_i) < ε, i ≤ p}` be a basic 0-neighborhood of `S^{m′}_K`. §9.4 gives, for each `i`,
data `C_i, R_{0,i}, Γ_i`. Choose `R ≥ max_i R_{0,i}` with `C_i R^{−(m′−m)/2} < ε/2` for every `i`
(possible: `(m′−m)/2 > 0`), then `δ > 0` with `C_i R^{m″−m′}δ < ε/2`, and
`W := {N_{m″}(·;γ′) < δ : γ′ ∈ ⋃_i Γ_i}` — a **finite** family (Item 3b: each `Γ_i` is finite;
finitely many `i`). For `a ∈ V ∩ W`: `N_{m′}(a;γ_i) ≤ C_i[R^{−(m′−m)/2}·1 + R^{m″−m′}δ] < ε`. So
`V ∩ W ⊂ O`. ✓  **Imprecision found:** the companion writes "choose `R ≥ R_0`" where `R_0` should be
`max_i R_{0,i}` (it already writes `C_i` and `Γ_i`, so this is a slip of notation, not of thought).
Cosmetic; repair is the two words. Referee 1 flagged the same.

**(M*) ⟹ the topologies coincide on `V`, re-derived.** `N_{m″}(a;γ) ≤ N_{m′}(a;γ)` because
`(1+|ξ|) ≥ 1` and `m″ > m′`, so `τ_{m″}|_{S^{m′}_K}` is coarser than `τ_{m′}` and only one
inclusion needs proof. Fix `a ∈ V` and a basic `O`. By (M*) there is `W_0` with `V ∩ W_0 ⊂ ½O`
(`½O` is again basic). If `b ∈ V` and `b − a ∈ W_0`, then `(b−a)/2 ∈ V` (V absolutely convex,
`a,b ∈ V`) and `(b−a)/2 ∈ W_0` (`W_0` balanced), so `(b−a)/2 ∈ ½O`, i.e. `b − a ∈ O`. Hence
`(a+W_0) ∩ V ⊂ a+O`. ✓  I checked the one step this leaves implicit: to conclude that every
`τ_{m′}`-open subset of `V` is `τ_{m″}`-open in `V`, one applies this at *each* point `b` of
`(a+O)∩V` after shrinking `O` (possible since `O` is open) — the companion's "for `a ∈ V` and `O`"
is stated for arbitrary `a ∈ V`, so it does supply this. ✓

**`V` is independent of `m″` — the point the task flags.** `V = {N_m(·;0)<1}` is defined from `m`
alone. So the single `V` serves **all** `m″ > m′` simultaneously, which is what "for all `k″ ≥ k′`
… on some 0-neighborhood of `X_k`" demands (the 0-neighborhood is quantified after `k″` in the
printed sentence, so the weaker reading — `V` allowed to depend on `k″` — would also be satisfied;
the companion proves the stronger, Retakh-type form, so **either reading of [39, Thm. 6.1] is
covered**). With `k′ = k+1` (i.e. `m′ = m+1`) and any `k″ ≥ k′`; for `k″ = k′` the assertion is
vacuous. ✓  No copy of Wengenroth is in the repo, so [39, Thm. 6.1] itself is taken as the paper
quotes it — the companion is careful to prove the form the paper prints, which is the right
standard for a note addressed to these authors.

**Transfer rules, each written out and checked.**
1. *Constant spectrum* `X_k ≡ X`: `V := X` (the whole space is a 0-neighborhood), and given `O`
   take `W := O`; `V ∩ W = O ⊂ O`. ✓
2. *Finite products*: a basic 0-neighborhood of `∏_{i≤r}X^{(i)}_{k′}` contains `∏_i O_i`; take
   `V := ∏_i V_i`, `W := ∏_i W_i`; `V ∩ W = ∏_i (V_i ∩ W_i) ⊂ ∏_i O_i ⊂ O`. Needs a common `k′`,
   which is free here since `k′ = k+1` for every factor. ✓
3. *Initial topology of a fixed linear map* `j` with `j(Y_k) ⊂ X_k`, `Y_k ⊂ Y_{k′}`: basic
   0-neighborhoods of `Y_k` are `j^{−1}(U) ∩ Y_k`. Put `V_Y := j^{−1}(V) ∩ Y_k`. Given a
   0-neighborhood `O_Y ⊇ j^{−1}(O) ∩ Y_{k′}` of `Y_{k′}`, take `W_Y := j^{−1}(W) ∩ Y_{k″}`. If
   `y ∈ V_Y ∩ W_Y` then `y ∈ Y_k ⊂ Y_{k′}` and `j(y) ∈ V ∩ W ⊂ O`, so
   `y ∈ j^{−1}(O) ∩ Y_{k′} ⊂ O_Y`. ✓ **Injectivity of `j` is not used**, and neither is
   `j(Y_{k″}) ⊄ X_{k′}`-type care — only `j(Y_k) ⊂ X_k` for each `k`. ✓
4. *Subspaces* (closed or not) with the induced topology: rule 3 with `j =` inclusion. ✓
   (Closedness is needed later, for the steps to be Fréchet and for the Montel argument, not for
   (M*).)

**"Initial topology of a fixed map" is the correct description of `I^m(M,L)`.** Published p. 22,
verbatim: "applying the versions of semi-norms (2.1) on `C^∞(M\L)` to `hu` and versions of
semi-norms (3.1) on `S^{m̄}(N*L_j;N*L_j)` to every `a_j`, we get semi-norms on `I^m(M,L)`, which
becomes a Fréchet space [25, Sections 6.2 and 6.10]. In other words, the following map is required
to be a TVS-embedding: `I^m(M,L) → C^∞(M\L) ⊕ ⊕_j S^{m̄}(N*L_j;N*L_j), u → (hu,(a_j)).  (4.10)`".
A TVS-embedding is precisely: the topology is the initial topology of that map. ✓ The map is
`m`-independent: `h` and `f_j` are fixed once (p. 22: "Let `{h, f_j}` be a `C^∞` partition of unity
of `M` subordinated to the open covering `{M\L, U_j}`"), and `a_j` is obtained from `f_j u` by the
fixed partial Fourier transform (4.8), `a(x″,ξ) = ∫ e^{−i⟨x′,ξ⟩}u(x′,x″)dx′` (p. 21) — no `m`
anywhere. Only the *target's topology* moves with `m`, through `m̄ = m + n/4 − n″/2` (4.9), which is
affine increasing in `m`, so `m<m′<m″ ⟹ m̄<m̄′<m̄″`. ✓ And §9.1's refinement is right: `supp f_j`
is compact (closed in the compact `M`, contained in `U_j`), so by (4.8) `a_j(x″,ξ)` vanishes for
`x″` outside the compact projection `K_j` of `supp f_j`, giving `a_j ∈ S^{m̄}_{K_j}`. ✓ This is the
whole reason the compactly-based model is the right one — and it is exactly what the printed proof
of Cor. 4.7 does **not** use (see Item 6).

**Ruling: HOLDS-WITH-REPAIR** (repair = "`R ≥ R_0`" → "`R ≥ max_i R_{0,i}`" in §9.5, one line, no
mathematical content). AGREE with referee 1's Item 5, and I add the two published-text points on
the criterion (characterization; `ℕ`-indexing plus the p. 5 cofinality sentence, whose printed form
is transposed).

## Item 5A — the non-compact question, settled by an explicit counterexample (my addition)

The task asks whether the same argument would go through for `S^m(U×R^l)` **without** compact
`x`-support, i.e. whether the failure for non-compact `U` is really about the seminorms being over
compact `K` rather than about the inequality. Referee 1 answered "yes, it is about the seminorms",
citing witness (f). That is right, but (f) is an argument about *regularity*, not about (M*)
directly. Here is the direct object, which I could not find in the note, the companion, or
referee 1's report.

**(A) The inequality itself survives, in local form.** The proof of §9.4 never uses `supp_x a ⊂ K`
(Item 3(g)). For `w > R` the `x`-box has side `Nw^{−c} < NR^{−c}`, so with
`K′ := {x : dist(x,K) ≤ √d·N R_0^{−c}}` (compact and `⊂ U` once `R_0` is large enough that
`√d N R_0^{−c} < dist(K, ∂U)`), the identical computation gives, for every `a ∈ S^{m″}(U×R^l)` and
`R ≥ R_0`,

  `‖a‖_{K,γ,m′} ≤ C[ R^{−(m′−m)/2}‖a‖_{K′,0,0,m} + R^{m″−m′} max_{γ′∈Γ}‖a‖_{K′,γ′,m″} ]`.

So the *inequality* is not what fails; it merely acquires a slightly larger compact on the right.

**(B) The criterion fails anyway, and here is the witness.** Let `U ⊂ R^n` be open and
**non-compact**, `l ≥ 1`, `X_k = S^{m_k}(U×R^l)` with `m_k ↑ ∞`. Fix `k`, write `m = m_k`, let
`m′ = m_{k′} > m` and `m″ = m_{k″} > m′` be arbitrary, and let `V` be **any** 0-neighborhood of
`X_k`. Then `V ⊇ {a : ‖a‖_{K_i,α_i,β_i,m} < ε_i, i ≤ p}` for finitely many compacts `K_i ⊂ U`.
Since `U` is non-compact, `U ∖ ⋃_i K_i` is a nonempty open set; choose a compact `K` inside it with
nonempty interior, `χ ∈ C_c^∞(int K)`, `χ ≢ 0`, and `θ ∈ C_c^∞(R^l)` with
`supp θ ⊂ B(e_1, ½)`, `θ ≢ 0`. For `T ≥ 2` and `M_T > 0` put

  `a_T(x,ξ) := M_T · χ(x) · θ(ξ/T)`.

*Facts.* (i) `a_T ∈ C_c^∞(U×R^l) ⊂ S^{−∞} ⊂ X_k`. (ii) `supp_x a_T ⊂ K` is disjoint from every
`K_i`, so every constraint defining `V` reads `0 < ε_i`: **`a_T ∈ V`, for every `M_T`.** (iii) The
family is *flat*: `∂_x^α∂_ξ^β a_T = M_T(∂^αχ)(x)T^{−|β|}(∂^βθ)(ξ/T)`, and on the support
`|ξ| ∈ [T/2, 3T/2]`, so `1+|ξ| ∈ [T/2, 2T]` and

  `2^{−||β|−s|}·M_T c_{α,β}·T^{−s} ≤ ‖a_T‖_{K″,α,β,s} ≤ 2^{||β|−s|}·M_T c_{α,β}·T^{−s}`
  for every compact `K″ ⊇ supp χ`, with `c_{α,β} = sup|∂^αχ|·sup|∂^βθ|` **independent of `T`**.

Every seminorm at level `s`, of every order, scales as `M_T T^{−s}`: taking more derivatives buys
nothing. Now let `O := {‖·‖_{K,0,0,m′} < 1}`, a 0-neighborhood of `X_{k′}`, and let `W` be **any**
0-neighborhood of `X_{k″}`, so `W ⊇ {‖·‖_{K_j′,α_j,β_j,m″} < δ_j, j ≤ q}`. Choose

  `M_T := (min_j δ_j / (2 max_j 2^{||β_j|−m″|}c_{α_j,β_j})) · T^{m″}`.

Then `‖a_T‖_{K_j′,α_j,β_j,m″} ≤ δ_j/2 < δ_j`, so `a_T ∈ W`; while

  `‖a_T‖_{K,0,0,m′} ≥ 2^{−|m′|}M_T c_{0,0}T^{−m′} = const · T^{m″−m′} ⟶ ∞`.

Hence for `T` large `a_T ∈ V ∩ W ∖ O`: **no `W` works**, so the topologies of `X_{k′}` and `X_{k″}`
do not coincide on `V`, for **every** `V`, every `k′ > k` and every `k″ > k′`. Since p. 4 presents
the condition as a *characterization* of acyclicity, this is an independent proof — not using
regularity, not using witness (f) — that `S^∞(U×R^l)` is not acyclic for non-compact `U`, i.e. that
the acyclicity clause of Cor. 3.6 fails there.

**(C) Why the compact base kills exactly this family — the note's remark is the right diagnosis.**
In `S^m_K` the neighborhood is `V = {N_m(·;0) < 1}` with `N_m(·;0)` a **global** supremum, so
`a_T ∈ V` forces `M_T c_{0,0}T^{−m} ≲ 1`, i.e. `M_T ≲ T^{m}`, and then
`‖a_T‖_{K,0,0,m′} ≍ M_T T^{−m′} ≲ T^{m−m′} → 0`. The family dies precisely because the `m`-level
seminorm sees it. So the note's one-clause explanation — "compact base support makes `N_m(a;0)` a
global supremum, which is exactly what fails in (f)" — is not merely accurate, it names the
operative mechanism. The sharper statement (Item 3(g)) is that what is needed is *globality of the
seminorm*, not compactness of the support: §9.4 and §9.5 both hold verbatim for the uniform symbol
spaces `S^m_{ub}(R^d×R^l)`, and `S^m_K` is a closed subspace of those.

**Ruling: HOLDS.** AGREE with referee 1's conclusion; the explicit witness `a_T` is my addition and
upgrades the conclusion from "inferred from (f)" to "proved directly".

## Item 6 — the stronger clauses the note uses in §4, and what is missing for which reader

**(a) "The inclusions `S^m_K → S^{m′}_K` map bounded sets to relatively compact sets, by
Arzelà–Ascoli and the tail bound `(1+|ξ|)^{m−m′}`."** Re-derived. Let `B ⊂ S^m_K` with
`C_γ := sup_{a∈B}N_m(a;γ) < ∞`. Take `(a_ν) ⊂ B`. All derivatives are locally uniformly bounded, so
Arzelà–Ascoli + a diagonal argument give a subsequence converging in `C^∞_loc(R^d×R^l)` to some `a`;
`a` vanishes off `K` and satisfies `|∂^γ a|(1+|ξ|)^{|β|−m} ≤ C_γ`, so `a ∈ S^m_K`. Then for `m′ > m`
and any `R > 0`,
`N_{m′}(a_ν−a;γ) ≤ max{ sup_{K×B̄_R}|∂^γ(a_ν−a)|·(1+R)^{|β|−m′}_{+} , 2C_γ(1+R)^{m−m′} }`;
the second term is `< ε/2` for `R` large (as `m−m′<0`) and the first `→ 0` for that fixed `R`. So
`a_ν → a` in `S^{m′}_K`. `S^{m′}_K` is metrizable (countably many seminorms), so `B̄` is compact.
✓ **Correct, and it holds for every `m′>m` and every compact `K`.**

The analogous statement the note uses for the printed semi-Montel step of Cor. 3.6 — "for `m′>m`,
`S^{m′}`- and `C^∞`-convergence agree on bounded subsets of `S^m(U×R^l)`" — is the same split and is
true for **arbitrary** `U` (bounded in `S^m` supplies `2C_{K,α,β}(1+R)^{m−m′}` on `|ξ|>R`; `C^∞`
convergence supplies the rest). ✓

**(b) "They are not compact operators, so the remark on p. 5 about compact spectra does not apply
as it stands."** The p. 5 remark, verbatim: "Assume the steps `X k` are LCHSs. It is said that
`(X k )` is compact if the inclusion maps are compact operators. In this case, `(X k )` is clearly
acyclic, and so `X` is Hausdorff." Re-derived the companion's refutation: let
`U_0 = {a : N_m(a;γ)<1, γ ∈ F}` be a basic 0-neighborhood, `k_0 := max{|α| : (α,β) ∈ F}`, and
`a_λ := ελ^{−k_0}\sin(λx_1)θ_1(x)θ(ξ)` with `θ_1 ∈ C_c^∞(int K)`, `θ ∈ C_c^∞(R^l)`. For `|α| ≤ k_0`,
`|∂_x^α(\sin(λx_1)θ_1)| ≤ C_αλ^{|α|}`, so `N_m(a_λ;γ) ≤ εC_γ` for all `λ ≥ 1`; taking `ε` small,
`a_λ ∈ U_0` for every `λ ≥ 1`. But with `α_0 = (k_0+1)e_1`,
`N_{m′}(a_λ;(α_0,0)) ≥ c ελ^{−k_0}λ^{k_0+1} = cελ → ∞`. So `U_0`'s image is unbounded in
`S^{m′}_K`: the inclusion is **not** compact. ✓ (Caveat the companion does not state: this needs
`int K ≠ ∅`. If `int K = ∅` then a symbol vanishing off `K` vanishes on a dense set, so
`S^m_K = {0}` and the inclusion trivially *is* compact. Harmless — the `K_j` arising from (4.10)
have nonempty interior — but the sentence should read "for `K` with nonempty interior".)
So the shortcut is genuinely unavailable and the interpolation route is genuinely needed. ✓

**(c) The Montel assembly (§9.7, adjacent to my item — checked because §4 of the note asserts it).**
Companion: for closed bounded `B ⊂ I(M,L)`, bounded retractivity puts `B` bounded in some `I^m`;
its (4.10)-image is bounded in `C^∞(M∖L) × ∏_j S^{m̄}_{K_j}`, hence relatively compact at level
`m̄′` (by (a), and `C^∞` Montel); `I^{m′}` is closed in the `m̄′`-level product (Fréchet, hence
complete, and (4.10) is a TVS-embedding), `B` is closed in `I^{m′}` because `I^{m′} → I(M,L)` is
continuous, so `B` is compact in `I^{m′}` and therefore in `I(M,L)`. With barreledness this gives
Montel. I checked the barreledness source: **Cor. 4.2 (p. 20), verbatim** — "Since every
`I^{(s)}(M,L)` is a Fréchet space (Proposition 4.1), the following analog of Proposition 3.1 holds
true by the same reason. **Corollary 4.2** `I(M,L)` is barreled, ultrabornological and webbed." — so
Cor. 4.2 rests on Prop. 4.1 alone and is **not** contaminated by the false Cors. 3.4/4.5. ✓ The
argument is correct; the clause "with the `I(M,L)`- and `I^{m′}`-topologies agreeing on `B`" is not
needed for it (compactness in `I^{m′}` transports to `I(M,L)` by continuity alone) and is a
harmless surplus.

**(d) Confirming the note's routing was necessary.** The printed proof of Cor. 4.7, p. 23, verbatim:
"Like in Corollary 3.6, by Corollaries 4.2 and 4.5, it is enough to prove that `I(M,L)` is
semi-Montel. … Then `I(M,L)` is semi-Montel because `C^∞(M\L)` and `S^∞(N*L_j;N*L_j)` are Montel
spaces (Corollary 3.6)". `L_j = L ∩ U_j` is an open, generally **non-compact**, subset of `L`, so
the printed proof leans on Cor. 3.6 over a non-compact base twice over — once through Cor. 4.5 and
once through the Montel clause. The companion's route (base = the compact `K_j`) avoids both; the
note carries this in the single clause "whose symbols vanish outside the compact base projections
of the `f_i`". Verified against p. 21 (4.8) and p. 22. ✓ Also confirmed on p. 23: "Corollary 4.7 has
extensions for `∪_m I^m(M,L)` and `I_{·/c}(M,L)`, except acyclicity in the case of `I(M,L)`" —
which is the exception the note's §3(f) parenthetical points at.

**(e) What is genuinely missing, for which reader.**
*For a reader of the NOTE alone*: all of §9.2–§9.5 — Lemma A, Lemma B, the choice of `c`, `N`,
`R_0`, `Γ`, both exponent computations, the `w ≤ R` case, the `γ=0` case, the `ε–δ` construction of
(M*), the absolute-convexity step, and the four transfer rules; plus the Fréchet-ness of `S^m_K`
and the Arzelà–Ascoli argument in (a). That is **exactly** the external reader's list (1)–(5), with
(a) as a sixth. The note does not claim otherwise: §5 says "Full derivations of (a)–(f), of
(interp), and of §4 are available on request."
*For a reader of NOTE + COMPANION*: nothing of mathematical substance. Two cosmetic repairs
(`R ≥ max_i R_{0,i}` in §9.5; "`int K ≠ ∅`" in the non-compactness remark of §9.7) and one
one-line assertion that deserves its two lines of proof (`S^m_K` Fréchet, Item 4).

**Optional three-line repair to the note**, if the sponsor wants (interp) checkable from the page:
after "proved by Taylor expansion …", insert `c=(m′−m)/(2|γ|)`, `N>|γ|+(m″−m′)/c`,
`Γ={γ}∪{Nχ_S : ∅≠S}`, `R_0=max\{1,(2N√l)^{1/c}\}`, and the two exponent identities
`c|γ|+m−m′=−(m′−m)/2` and `−c(N|S|−|γ|)+m″−m′<0`. That is one sentence and it makes the estimate
verifiable without the companion. I do **not** recommend changing "stands once this is done" on
mathematical grounds — with the companion it is true — but the external reader's softening is a
defensible editorial choice for a note that ships without its appendix.

**Ruling: HOLDS.**  AGREE with referee 1's Item 6; the `int K ≠ ∅` caveat and the Cor. 4.2
provenance check are my additions.

## Item 7 — the ruling on the external assessment's criticism

The assessment says: "*this is the part I would not yet call proved in the note as it stands. The
estimate is the essential new theorem. The sentence saying it follows from Taylor expansion is not
enough for a reader to verify: (1) the precise choice of boxes in x and ξ, (2) how derivatives in
both variables are controlled simultaneously, (3) why the finite set Γ is sufficient uniformly in ξ,
(4) the dependence of C, R_0, (5) and exactly how (1) implies the topological coincidence criterion
being invoked.*"

**As a statement about the NOTE: CORRECT, and its five bullets are exactly right.** The note gives
(interp) with a 32-word justification. Of the five: (1) the note *does* give the box sides
(`(1+|ξ|)^{-c}` in x, `(1+|ξ|)^{1-c}` in ξ) and the region `1+|ξ|>R`, but never says what `c` is —
and `c=(m′−m)/(2|γ|)` is the whole trick, since it is what makes the `S=∅` exponent collapse to
`−(m′−m)/2` (Item 3(e)); (2) is Lemma B, absent; (3) is the choice of `N` and the fact that only
the `2^{d+l}` *pure* derivatives survive Lemma B, absent — and by Item 3b there is no
`γ`-independent `Γ`, so a reader could not guess it; (4) absent; (5) absent (the `ε–δ` and the
absolute-convexity step are three lines, but three lines the note does not have). Bullet (3)'s
wording "uniformly in ξ" is slightly off-target — the real content is uniformity in `γ`'s companion
set, not in `ξ` — but the criticism it points at is genuine.

**As a statement about the MATHEMATICS given the companion: NOT CORRECT.** §9.2–§9.5 prove
(interp) and its passage to the p. 4 criterion completely. I re-derived Lemma A, Lemma B, both
exponent computations, the geometry of the box, the `w ≤ R` and `γ=0` cases, the (M*) construction,
the (M*)⟹coincidence step and all four transfer rules independently; every one is correct as
written, with two cosmetic slips (Items 5, 6(b)) and one one-line assertion that wants two lines
(Item 4). Numerical stress testing of Lemmas A and B against the proof's own explicit constants,
and of Prop. 9.4 against both the proof's constant chain and an adversarial parameter search, found
no violation. The estimate is not "a credible repair strategy"; it is a proved theorem whose proof
was simply not shipped with the note.

The assessment's closing "**The key estimate needs a full proof**" is therefore right about what the
reader had in front of him and wrong about the state of the mathematics. Its suggested softening of
"stands once this is done" is a presentation judgment about the standalone note, not a mathematical
objection; it is defensible if the note ships without its appendix, and unnecessary if the
companion (or the three-line insertion in Item 6(e)) goes with it.

**Ruling: the criticism HOLDS as a description of the note; it FALLS as a statement about the
mathematics.**

## AGREE / DISAGREE with referee 1, item by item

| Referee 1 item | Its ruling | Mine | Note |
|---|---|---|---|
| 1. Lemma A | HOLDS | **AGREE** — HOLDS | Re-derived; independent numerics (4000 cases) |
| 2. Lemma B | HOLDS | **AGREE** — HOLDS | Re-derived; independent numerics (600 cases) |
| 3. Prop. 9.4 | HOLDS | **AGREE** — HOLDS | Exponents recomputed from scratch, match character for character; added the `c>1` branch, the "uniform symbols" sharpening, and Item 3b (necessity of the bound on N) |
| 4. note vs companion | HOLDS | **AGREE** — HOLDS | Added: `S^m_K` Fréchet is asserted, not proved, in §9.1 (true; two lines) |
| 5. §9.5 + criterion | HOLDS | **AGREE** — HOLDS-WITH-REPAIR | Same cosmetic repair found (`max_i R_{0,i}`); added the p. 4/p. 5 quantifier and cofinality checks |
| 6. stronger clauses | HOLDS | **AGREE** — HOLDS | Added the `int K ≠ ∅` caveat and verified Cor. 4.2's provenance (p. 20) |
| — non-compact `U` | inequality survives locally; criterion fails (via (f)) | **AGREE, and strengthened** | Item 5A gives an explicit family `a_T` refuting (M*) directly for every `V`, independent of (f) |
| — ref. 1, Item 3, break (a): "the family reproduces the companion's threshold for N exactly" | (subsidiary claim) | **DISAGREE** | Factor-2 algebra slip; true necessary threshold is `N ≥ |γ|+(m″−m′)/(2c)`. Verified numerically (`sharp2.py`). Does not affect its HOLDS on Item 3 |

I agree with all six of referee 1's **rulings**; the single DISAGREE above is on a subsidiary
sharpness claim inside its Item 3, not on the ruling. It marked nothing FALLS or UNDECIDED, and
I found nothing that should have been.

## Appendix — numerical stress tests (raw output)

Scripts: `scratchpad/interp/lemAB.py`, `prop94.py`, `adv.py` (session scratchpad
`/private/tmp/claude-501/…/67ed06f0-…/scratchpad/interp/`).

```
Lemma A: worst LHS/RHS with proof constant = 0.999988574194337   (N=1, h=1.4e-3, j=0)
Lemma B: worst LHS/RHS with constant C_N^D  = 0.9913924880107    (D=2, N=1, gamma=(0,0))
Prop 9.4, d=0,l=1: worst N_{m'}(a;b)/[proof bound] = 0.00234
   at m=1.239, m'=3.432, m''=3.514, beta=1, N=2, R=R0=3.541

sharpness test (sharp2.py), m=0 m'=1 m''=3 k=1, c=1/2, R=R0:
 Gamma={k,2}: ratio 1.994 -> 19.77 as w0 = 1e3 -> 1e5   (grows like w0^{1/2}: FAILS)
 Gamma={k,3}: ratio saturates at 0.1602                 (borderline, = my necessary threshold)
 Gamma={k,4}: ratio <= 0.022                            (companion demands N >= 6)

adversarial search, RAW ratio (all constants stripped):
 m=0.0 m'=1.0 m''=2.0 beta=1:  sup raw ratio = 0.04573  (x0=1.0, L=42.8, om=0, R=R0=64, N=4)
 m=0.0 m'=1.0 m''=2.0 beta=3:  sup raw ratio = 4.17e-12 (N=10, R0=6.4e7)
 m=0.0 m'=4.0 m''=5.0 beta=1:  sup raw ratio = 0.4348   (x0=1.58, L=1.51, om=1.0, R=R0=2, N=2)  <- c=2>1 branch
 (three regimes skipped: they required N>10 or R0>1e8, outside the grid)
```
The raw ratio never approaches 1; in the tightest regime found (`c = 2 > 1`) the inequality holds
with an absolute constant near 2.3 even before any of the proof's constants are applied.

---
Report closed. Machine clock: Sun Sep  6 13:54:55 IST 2026
