# D1 M2a Lane A — PLAN (planner, "price first, batch, never shrink")

**Stamp:** written 2026-09-09 21:05 IST (Session 19, run wf_ab066aa4-165, phase 1), machine clock. Resumes the Session-17
stream stopped by the sponsor on 2026-09-06 during phase 1; every s17 partial output in this directory was verified and
reused, not redone (§3.0). **Verdict: GO** (§4). Brief: `BRIEF.md`. Authorities read in the brief's order: `SPEC.md` §5,
§7.2, §7.4, §7.6, §8, §10, §11, §13.2, §14; `v11/GLUE-NOTES.md`; `RUN-REPORT.md` §5–6; the three leg notes; the Lane B
producer code; the Lean tree (`Instance02.lean`, `lean-shapes-scratch.lean` §C, the pinned Mathlib).

Trust vocabulary (D-R3/D-R8, binding): everything the producers emit is UNTRUSTED; the kernel checks only C-A1…C-A6 on
the integers; the analytic claims H2-A and H-TAIL stay DISPLAYED. Never "fully machine-checked". Λ bracket of record:
0 ≤ Λ ≤ 0.2. U.S. English.

---

## 1. Statements

### 1.1 `hLaneA` as displayed today (`~/rh-lean-work/zeta-23-lean-main/Zeta23/DBN/Instance02.lean`, verbatim)

The binder, identical in `row2_ray_mp` (lines 163–164), `row2_ray_arb` (182–183), `lambda_le_point2` (208–209) and
`lambda_le_point2_arb` (220–221):

    (hLaneA : ∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y →
      y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (x + y * I) ≠ 0)

It is consumed at exactly one place per leg — as hypothesis (ii′) of `Polymath15Bridge'` (line 169 of `row2_ray_mp`,
line 188 of `row2_ray_arb`):

    refine hH3.1 (93 / 500) 5000000194858 (16733 / 100000) (by norm_num) (by norm_num) (by norm_num)
      (by norm_num) (hH1_row2 hH1) hLaneA ?_

and passed through by `lambda_le_point2` (line 213: `exact row2_ray_mp hH1 hEncl hLaneA hH3 t (le_trans …)`).
GLUE-NOTES ("Left for the Lane A stream"): "(ii′) is consumed exactly where `hLaneA` is passed."

### 1.2 The data and the checker (SPEC §7.2 lines 732–742, §7.4 lines 764–772, §8.2 lines 880–883; Lean text =
`lean-shapes-scratch.lean` §C lines 179–233, re-elaborated this session in `laneA-shapes-scratch.lean`, log
`laneA-shapes-typecheck.log`, zero errors)

    def windowIdx (t x : ℝ) : ℕ := ⌊Real.sqrt (x / (4 * π) + t / 16)⌋₊          -- P15 (19), p6

    structure AsymRow where  Nlo Nhi T E : ℤ                 -- written one field per line in the module
    structure TailRow where  N1 Q1 Q2 Q3 Q4 E1 : ℤ
    structure AsymData where K t0n t0d y0n y0d yAn yAd : ℤ;  rows : List AsymRow;  tail : TailRow

    def checkAsymRow (r : AsymRow) : Bool :=
      decide (r.Nlo ≤ r.Nhi) && decide (0 ≤ r.E) && decide (r.E < r.T)
    def consecutive : List AsymRow → Bool
      | [] => true
      | [_] => true
      | r :: s :: l => decide (s.Nlo = r.Nhi + 1) && consecutive (s :: l)
    def lastNhi : List AsymRow → ℤ
      | [] => 0
      | [r] => r.Nhi
      | _ :: s :: l => lastNhi (s :: l)
    def checkAsym (d : AsymData) : Bool :=
      decide (1 ≤ d.K) && decide (1 ≤ d.t0d) && decide (0 < d.t0n) && decide (1 ≤ d.y0d)
        && decide (0 < d.y0n) && decide (1 ≤ d.yAd) && decide (0 ≤ d.yAn)
        && decide ((d.t0d - 2 * d.t0n) * d.yAd ^ 2 ≤ d.yAn ^ 2 * d.t0d)
        && decide (0 < d.rows.length)
        && d.rows.all checkAsymRow && consecutive d.rows
        && decide (d.tail.N1 = lastNhi d.rows + 1)
        && decide (0 ≤ d.tail.Q1) && decide (0 ≤ d.tail.Q2) && decide (0 ≤ d.tail.Q3)
        && decide (0 ≤ d.tail.Q4) && decide (0 ≤ d.tail.E1)
        && decide (d.tail.Q1 + d.tail.Q2 + d.tail.Q3 + d.tail.Q4 + d.tail.E1 < 2 * d.K)

The checks, clause by clause (SPEC §7.4): **C-A1** = the first eight conjuncts (K ≥ 1, denominators ≥ 1, t₀ > 0,
y₀ > 0, yA ≥ 0, and yA² ≥ 1 − 2t₀ cross-multiplied as (t0d − 2·t0n)·yAd² ≤ yAn²·t0d); **C-A2** = `0 < d.rows.length`;
**C-A3** = `d.rows.all checkAsymRow` (Nlo ≤ Nhi and 0 ≤ E < T per row); **C-A4** = `consecutive d.rows`
(next.Nlo = Nhi + 1); **C-A5** = `d.tail.N1 = lastNhi d.rows + 1`; **C-A6** = the last six conjuncts (all five ≥ 0 and
Q₁ + Q₂ + Q₃ + Q₄ + E₁ < 2K). Everything is +, ·, ^2 and comparisons on ℤ and a ℕ length — `decide +kernel`, no
`native_decide` (SPEC §8.2 last paragraph).

    def At0 (d : AsymData) : ℝ := (d.t0n : ℝ) / d.t0d      -- likewise Ay0, AyA
    def AsymEnclOK (g : ℂ → ℂ) (d : AsymData) : Prop :=                                   -- H2-A, SPEC §8.1 l.845
      ∀ r ∈ d.rows, ∀ x y : ℝ, (r.Nlo : ℝ) ≤ windowIdx (At0 d) x → (windowIdx (At0 d) x : ℝ) ≤ r.Nhi →
        Ay0 d ≤ y → y ≤ AyA d → ((r.T : ℝ) - r.E) / d.K ≤ ‖g (x + y * I)‖
    def TailOK (g : ℂ → ℂ) (d : AsymData) : Prop :=                                       -- H-TAIL, l.849
      ∀ x y : ℝ, (d.tail.N1 : ℝ) ≤ windowIdx (At0 d) x → Ay0 d ≤ y → y ≤ AyA d → g (x + y * I) ≠ 0

### 1.3 The soundness theorem (SPEC §8.3 lines 899–902, statement verbatim), L-A1, L-A2

    theorem cert_of_checkAsym (g : ℂ → ℂ) (d : AsymData) (hc : checkAsym d = true)
        (hEncl : AsymEnclOK g d) (hTail : TailOK g d) :
        ∀ x y : ℝ, ∀ r ∈ d.rows, (r.Nlo : ℝ) ≤ windowIdx (At0 d) x →
          Ay0 d ≤ y → y ≤ AyA d → g (x + y * I) ≠ 0

**L-A2** (SPEC §5.3 line 583, §6 line 696 "monotonicity of `windowIdx` in x"):

    theorem windowIdx_mono (t : ℝ) {x x' : ℝ} (h : x ≤ x') : windowIdx t x ≤ windowIdx t x'

**L-A1** (SPEC §5.3 lines 576–582, §6 line 695 "N(X + 1) ≥ N_start from a rational bound on π"), for the instance
N_start = N₀ = 630783 (the plan's first Nlo; SPEC §5.3's option N₀ − 1 is not needed, see the margin):

    theorem row2_windowIdx_ge (x : ℝ) (hx : 5000000194858 + 1 ≤ x) : (630783 : ℝ) ≤ windowIdx (93 / 500) x

Arithmetic (exact rationals, π < 3.141593 = `Real.pi_lt_d6`): 4·3.141593·630783² − 3.141593·(93/500)/4 =
4 999 998 482 392.06 < 5 000 000 194 859 = X + 1, margin 1 712 466.9; equivalently (X+1)/(4·3.141593) + t₀/16 − 630783² =
136 273.8 > 0. (SPEC §5.3 called this "tight" against the ≈ 2.26·10⁶ slack of x_{N₀}; it holds with a third of that slack
to spare, so N_start = N₀.)

### 1.4 Proof plan of `cert_of_checkAsym` per SPEC §5.6 — now PROVED in the scratch, standard axioms

The proof in `laneA-shapes-scratch.lean` (checked with `lake env lean` from the tree, tree untouched; 2.4 s wall):

1. **Coverage lemma** `cover_of_consecutive` — for a list with `consecutive l = true`, if r ∈ l, r.Nlo ≤ n and
   n ≤ lastNhi l (integers) then some r′ ∈ l has r′.Nlo ≤ n ≤ r′.Nhi. Structural recursion on the list: `[]` (vacuous),
   `[r0]` (r = r0, lastNhi = r0.Nhi), `r0 :: s :: l` (if r ∈ s :: l recurse; if r = r0 then either n ≤ r0.Nhi, done, or
   n ≥ r0.Nhi + 1 = s.Nlo by C-A4 and recurse from s). Only C-A4 is used here.
2. **Main theorem.** Unpack `hc` (`simp only [checkAsym, Bool.and_eq_true, decide_eq_true_eq, List.all_eq_true]`, then
   one `obtain` on the left-nested conjunction) into hK (C-A1's K ≥ 1), hrows (C-A3), hcons (C-A4), hN1 (C-A5). Let
   n := windowIdx (At0 d) x; from (r.Nlo : ℝ) ≤ n get r.Nlo ≤ (n : ℤ) by `exact_mod_cast`. Case n ≤ lastNhi d.rows: the
   coverage lemma gives r′; `hEncl r′` gives (T′ − E′)/K ≤ ‖g z‖; C-A3 (E′ < T′) and K ≥ 1 give (T′ − E′)/K > 0
   (`div_pos`, casts, `linarith`); if g z = 0 then ‖g z‖ = 0 (`norm_zero`), contradiction. Case n > lastNhi: C-A5 gives
   d.tail.N1 ≤ n (`omega`), cast to ℝ, and `hTail x y` closes. — Exactly SPEC §5.6 ("either N(x) ∈ [N₋, N₊] for some row
   … or N(x) ≥ N₁"); `Bt t₀ ≠ 0` (L-B3) is not needed here because g is the quotient and the glue (1.5) uses
   `div_ne_zero_iff`.
3. **L-A2**: `unfold windowIdx; apply Nat.floor_mono; apply Real.sqrt_le_sqrt`, then `div_le_div_of_nonneg_right`
   and `linarith`. **L-A1**: `Nat.le_floor`, `Real.le_sqrt_of_sq_le`, then the key inequality
   630783² − 93/500/16 ≤ x/(4π) by `le_div_iff₀` + `nlinarith [Real.pi_lt_d6, Real.pi_pos]`.

`#print axioms` (log `laneA-shapes-typecheck.log`, verbatim): `cert_of_checkAsym`, `windowIdx_mono`,
`row2_windowIdx_ge`, `row2_laneA` → `[propext, Classical.choice, Quot.sound]`; the kernel fact `row2AsymPH_check` →
`[propext]`. Two negative controls (a gap in the rows → C-A4 fails; a tail sum ≥ 2K → C-A6 fails) return `false` by
`decide +kernel`.

**Every Mathlib/core name used, verified to exist in the pinned Mathlib (`.lake/packages/mathlib`, rev 51e6992;
`#check` in `names-check.lean` and `grep`), name → file:line:**

| name | file (under `Mathlib/`) |
|---|---|
| `Real.pi_lt_d6` (π < 3.141593) | `Analysis/Real/Pi/Bounds.lean:184` (also `pi_gt_d6`:178) |
| `Real.pi_pos` | `Analysis/SpecialFunctions/Trigonometric/Basic.lean:157` |
| `Real.sqrt_le_sqrt` (x ≤ y → √x ≤ √y) | `Analysis/Real/Sqrt.lean:209` |
| `Real.le_sqrt_of_sq_le` (x² ≤ y → x ≤ √y) | `Analysis/Real/Sqrt.lean:258` |
| `Nat.floor_mono` (Monotone Nat.floor) | `Algebra/Order/Floor/Semiring.lean:89` |
| `Nat.le_floor` ((n : α) ≤ a → n ≤ ⌊a⌋₊) | `Algebra/Order/Floor/Defs.lean:143` |
| `div_le_div_of_nonneg_right` | `Algebra/Order/GroupWithZero/Basic.lean:1199` |
| `le_div_iff₀` (0 < c → (a ≤ b / c ↔ a * c ≤ b)) | `Algebra/Order/GroupWithZero/Basic.lean:1134` |
| `div_pos` | `Algebra/Order/GroupWithZero/Basic.lean:880` |
| `div_ne_zero_iff` (a / b ≠ 0 ↔ a ≠ 0 ∧ b ≠ 0) | `Algebra/GroupWithZero/Units/Basic.lean:291` |
| `le_of_sq_le_sq` (a² ≤ b² → 0 ≤ b → a ≤ b) | `Algebra/Order/Ring/Abs.lean:134` |
| `Int.cast_natCast`, `Int.cast_le` (via `exact_mod_cast`) | `Data/Int/Cast/Basic.lean:71`; `Algebra/Order/Ring/Cast.lean:56` |
| `norm_zero`, `norm_pos_iff` (to_additive of `norm_zero'`/`norm_pos_iff'`) | `Analysis/Normed/Group/Basic.lean:134, 993` |
| `List.all_eq_true`, `Bool.and_eq_true`, `decide_eq_true_eq`, `List.mem_cons`, `List.mem_cons_self`, `List.mem_cons_of_mem`, `List.mem_singleton`, `List.not_mem_nil` | Lean core (Init), `#check`-verified |
| tactics `omega`, `linarith`, `nlinarith`, `positivity`, `push Not` (`push_neg` is deprecated in this Mathlib), `norm_num`, `exact_mod_cast`, `decide +kernel` | — |

Not needed: `Real.pi_lt_d20`, `Real.le_sqrt` (both exist; `le_sqrt_of_sq_le` is the cleaner form).

### 1.5 How `cert_of_checkAsym` on the literal yields (ii′) in the form `hLaneA` consumes it

With `row2AsymMP : AsymData` the mp leg's literal (and `row2AsymARB` the Arb leg's), `row2AsymMP_check : checkAsym
row2AsymMP = true := by decide +kernel`, and the three `simp` facts `At0 row2AsymMP = 93/500`, `Ay0 … = 16733/100000`,
`AyA … = 3962323/5000000`, the glue lemma (proved in the scratch as `row2_laneA`, on the placeholder literal; its text
does not depend on the integers beyond the first row's Nlo = 630783):

    theorem row2_laneA_mp
        (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)
        (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP) :
        ∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y →
          y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (x + y * I) ≠ 0 := by
      intro x y hx hy0 hy2
      have hyA : y ≤ 3962323 / 5000000 := by apply le_of_sq_le_sq _ (by norm_num); nlinarith
      have hg := cert_of_checkAsym _ row2AsymMP row2AsymMP_check hAsym hTail x y
        ⟨630783, 746495, T₀, E₀⟩ (by simp [row2AsymMP])            -- the first row, T₀/E₀ its integers
        (by rw [row2AsymMP_t0]; exact row2_windowIdx_ge x hx)
        (by rw [row2AsymMP_y0]; exact hy0) (by rw [row2AsymMP_yA]; exact hyA)
      exact (div_ne_zero_iff.mp hg).1

Its conclusion is character-for-character the type of `hLaneA`. (y ≤ yA comes from y² ≤ 157/250 < yA² =
157/250 + 3556329/(25·10¹²), `le_of_sq_le_sq` with yA ≥ 0; the G at t₀ is the same `fun t z => Ht t z / Bt t z`
that `hEncl` names, applied at t = 93/500; `Ht … ≠ 0` from `Ht/Bt ≠ 0` is `div_ne_zero_iff`'s first component.)

**The replacement in `Instance02.lean` (the whole change outside the new module):** in `row2_ray_mp` /
`row2_ray_arb` / `lambda_le_point2` / `lambda_le_point2_arb` the binder `(hLaneA : …)` becomes the pair
`(hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)`
`(hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)` (ARB in the Arb theorems), and at the one
consumption point the token `hLaneA` becomes `(row2_laneA_mp hAsym hTail)` (line 169; `(row2_laneA_arb hAsym hTail)` at
line 188); the two `lambda_le_point2*` bodies pass `hAsym hTail` where they passed `hLaneA`. Each leg pairs its own Lane
A literal with its own Lane B literal — the legs are never merged (D-R3). After the change the displayed hypotheses are
H1, H2-B, H2-A (`hAsym`, window rows), H-TAIL (`hTail`), H3 — the SPEC §3.7 label (lines 365–376) as written, and
RUN-REPORT §6 item 4's short sentence becomes licensed with §3.7's gloss (audit ruling R-1). `#print axioms` expected
unchanged: `[propext, Classical.choice, Quot.sound]`.

Module placement (builder): `Zeta23/DBN/Asym.lean` — `windowIdx`, the three structures, `checkAsym` and helpers, the
four Props, `cover_of_consecutive`, `cert_of_checkAsym`, `windowIdx_mono` (importing `Zeta23.DBN.Defs` and
`Mathlib.Analysis.Real.Pi.Bounds`); the two literals + kernel facts + `row2_windowIdx_ge` + the glue lemmas in
`Zeta23/DBN/Instance02/Asym_mp.lean` / `Asym_arb.lean` (emitted, back-parse-verified as Lane B's); `Instance02.lean`
imports them. `lake build -j2`. Copy back to `lean/Zeta23/DBN/` afterwards as Session 16 did.

---

## 2. Producers

Both legs implement the same derivation from the same quoted formulas, in independent code (P-1, D-R3): `p9_mp.py`
(mpmath `iv`, prec 288, ball.py `iv_exp/iv_log/iv_pi` — the M1/M2a platform assumption) and `p9_arb.py` (python-flint
0.6.0 `arb`, prec 320, the exact ball→rational helpers of `producer_arb.py` D-P1…D-P4). Shared input: only the UNTRUSTED
plan `rows-plan.json` (data). Scales: mp K = 10²⁴, Arb K = 10¹² (each leg its own transcript and literal, as Lane B:
`Instance02.lean` header). Every emitted integer is ⌊K·lower⌋ for floors, ⌈K·upper⌉ for bounds, on exact rationals.

### 2.1 P-9 — a window row (N₋, N₊, T, E)   [SPEC §5.2 lines 551–573; P-9 line 1016; P-6 line 1007]

Row semantics (SPEC line 551–554): for all x with N(x) ∈ [N₋, N₊] and y ∈ [y₀, yA], |f_{t₀}(x+iy)| ≥ T/K and
e_A + e_B + e_{C,0} ≤ E/K, hence |g_{t₀}| ≥ (T − E)/K (Corollary 1.4, SPEC §2.5 line 196). Per row the producers compute:

**T (derivation M, mollified triangle inequality; the SPEC's first option "Lemma 10.1, Euler-2 mollifier", line 561–564).**
Sources: P15 (14)/(92) with the overline on s* (SPEC §14 erratum 1), (15), (19), (20)–(22) (SPEC §2.3 lines 162–176),
(80) p38, Lemma 10.1 p65, Lemma 8.2's proof p43 (SPEC §2.7 lines 215–224), p52 (96). Setting: t = t₀, N = N(x) ∈ [N₋, N₊],
y ∈ [y_a, y_b] ⊂ [y₀, yA] (the row's y-range is split into 8 pieces with endpoints 0.16733, 0.18, 0.2, 0.23, 0.27, 0.32,
0.40, 0.55, 0.7924646; T = min over pieces; the lowest piece binds), σ := Re s*.

* M-1 (SPEC §5.4 Step 2(b), lines 601–606): x ≥ x_N := 4π(N² − t/16) ⇒ σ ≥ σ_N(y) := (1+y)/2 + (t/2) log N − ε_N,
  ε_N := −(t/4) log(1 − t/(16N²)) + t/(2x_N²); σ_N(y) increases in N and y, so σ ≥ σ_lo := σ_{N₋}(y_a) on the sub-box.
  (The positive part in (21) — or in Prop. 6.6(ii)'s variant, SPEC §14 erratum 2 — is ≤ 1 for x ≥ 200, y ≤ 1, so both
  readings give this bound.)
* M-2 (Lemma 10.1 on A = Σ_{n≤N} b_n n^{−s*}): E := 1 − β₂, β₂ := b₂2^{−s*}; β₂α_{n/2} = θ_n α_n with
  θ_n := b₂b_{n/2}/b_n = exp(−(t/2)(log 2)log(n/2)) ∈ (0, 1], so |E·A| ≥ 1 − Σ_{n=3}^{2N} m_n n^{−σ} with m_n = b_n (odd n ≤ N),
  (1−θ_n)b_n (even n ≤ N), θ_n b_n (even n ∈ (N, 2N]).
* M-3 (the C-series): C = C₀ + R, C₀ := Σ n^y b_n n^{−conj s*}, |R| ≤ Z := Σ n^y b_n n^{−σ}(n^{|κ|} − 1) (p52 (96));
  |E·C₀| = |E·conj C₀| and conj C₀ = Σ α′_n with α′_n := n^y b_n n^{−s*}, β₂α′_{n/2} = 2^{−y}θ_n α′_n (real factor in (0,1)),
  so Lemma 10.1's upper display gives |E·conj C₀| ≤ Σ_{n=1}^{2N} m′_n n^{−σ}, m′_n = n^y b_n (odd n ≤ N),
  n^y b_n(1 − 2^{−y}θ_n) (even n ≤ N), 2^{−y}θ_n n^y b_n (even n ∈ (N, 2N]).
* M-4: |E f| ≥ |E A| − |γ||E C₀| − |γ||E| Z and |E| ≤ 1 + b₂2^{−σ} ≤ 1 + β, β := b₂2^{−σ_lo}; when L_A − U_C ≥ 0,
  |f| ≥ (L_A − U_C)/(1 + β) − Z̄.
* M-5 (uniformity in N): with θ_n ≤ ½ for n > N₋ (certified per row; needs N₋ + 1 ≥ 2e^{2/t} ≈ 93 600, true for every row),
  m_n(N) ≤ m_n(N₊) and m′_n(N) ≤ m′_n(N₊) for all N ∈ [N₋, N₊], and n^{−σ} ≤ n^{−σ_lo}: the N = N₊ sums at σ_lo bound
  every window of the row.
* M-6 (uniformity in y, SPEC Step 2(c)–(d) lines 606–610): |γ| n^y ≤ e^{0.02y_b} ρ_{N₋} (n/N₋)^{y_a} =: w_n/b_n for n ≤ N,
  ρ_N := (1 − t/(16N²))^{−1/2}; 1 − 2^{−y}θ_n ≤ 1 − 2^{−y_b}θ_n; |κ| ≤ k := t y_b/(2(x_{N₋} − 6)) ((22)).
* M-7 (parity re-indexing, n = 2m: θ_{2m} b_{2m} = b₂b_m): with G(s′, a, b) := Σ_{a<n≤b} b_n n^{−s′}, s′ := σ_lo − y_a,
  c := e^{0.02y_b}ρ_{N₋}, h := ⌊N₊/2⌋:
    L_A = 2 − G(σ_lo, 0, N₊) + β G(σ_lo, 0, h) − β G(σ_lo, h, N₊),
    U_C = c N₋^{−y_a}[G(s′, 0, N₊) − 2^{−y_b} b₂2^{−s′} G(s′, 0, h) + β G(s′, h, N₊)],
    Z̄ = (N₊^{k} − 1) c N₋^{−y_a} G(s′, 0, N₊)          (M-Z: n^{|κ|} − 1 ≤ N₊^{k} − 1 for n ≤ N₊),
    T_sub = (L_A − U_C)/(1 + β) − Z̄  (upper enclosure ends on added terms, lower on subtracted; β and c as balls).
* M-8 (G enclosure): exact ball summation for n ≤ N_c = 10 000; for (M, b] with (t/2)log b < s′ (certified; Lemma 8.2's
  monotonicity) the integral test with u = log v: Σ_{M<n≤b} φ(n) ≤ ∫_{log M}^{log b} ψ ≤ trapezoid (ψ(u) = exp((1−s′)u +
  (t/4)u²) convex) and ≥ ∫_{log(M+1)}^{log(b+1)} ψ ≥ midpoint sum, m = 2000 panels. **This is why the cost of a row is
  independent of its width N₊ − N₋ + 1** (§3): six G's per y-piece, each 10 000 head terms + 4 000 integrand evaluations.

**E (M-E; P-6/P-9, SPEC §5.2 lines 567–573, §4.4 lines 420–424; Prop. 6.6(iv)–(vi) p31, (82)–(86) p39–41, the 10.50 form
D-2.4 SPEC lines 185–195).** On the hull x ∈ [x_{N₋}, x_{N₊+1}], y ∈ [y₀, yA] (interval/ball arithmetic = the sup by
inclusion isotonicity): e_A + e_B ≤ (e^{δ₁} − 1)(1 + e^{0.02y}ρ_{N₋}N₊^{κ})·F_{N₊}(σ_lo(y₀)), δ₁ = ((t²/16)log²(x/4π) +
0.626)/(x − 6.66) (the D-F4/D-A2 majorization of 6.6(iv)–(v), SPEC §14 erratum 3), F ≤ 1 + (N₊^{1−ρ} − 1)/(1 − ρ) with
ρ = σ − (t/4)log N₊ (D-F5); e_{C,0} at N = N₋ in the (N − 1/8) term — the mp leg by Prop. 6.6(vi) as printed, the Arb
leg by the 10.50 form (both admissible per D-2.4: "the 10.50 form (or 6.6(vi) itself), never the displayed 10.44").
Recorded per row: T_lo, E_hi as exact rationals, the per-piece σ_lo, β, c, ρ, k, L_A, U_C, Z̄ and the six G enclosures,
the E parts, seconds, stamp (`batches/<leg>-row_NNNN.json`); the transcript's `producer` block carries them (SPEC §7.2).

### 2.2 P-10 — the tail row (N₁, Q₁, Q₂, Q₃, Q₄, E₁)   [SPEC §5.4 lines 589–657; P-10 line 1018]

Exactly SPEC §5.4 (M-T): u₁ = log N₁, ε := ε_{N₁} (Step 2(b)), σ_{N₁} := σ_{N₁}(y₀), ρ₁ := ρ_{N₁},
k₁ := t·yA/(2(x_{N₁} − 6)), c_γ := e^{0.02}ρ₁ (Step 2(c)–(d), lines 606–610); a := (1 − y₀)/2 + ε, a″ := (1 + y₀)/2 + ε + k₁,
ψ(v) := a v − (t/4)v², ψ″ likewise, κ_T := max(√(2/(e t)), 2/(e t u₁)) (Step 3 lines 611–626, Step 4 lines 627–633);
**Q₁** = G(σ_{N₁}, 0, N₁) (upper end), **Q₂** = c_γ N₁^{−y₀} G(σ″, 0, N₁) with σ″ := σ_{N₁} − y₀ − k₁, **Q₃** =
e^{ψ(u₁)} κ_T, **Q₄** = c_γ N₁^{−y₀} e^{ψ″(u₁)} κ_T; **E₁** (Step 5 lines 635–638) = the M-E form at x = x_{N₁}, N = N₁,
y ∈ [y₀, yA], with F ≤ 1 + 1/(ρ_F − 1), ρ_F := (1 + y₀)/2 + (t/4)u₁ − ε > 1 (certified) and the factor
1 + e^{0.02yA}ρ₁N₁^{k₁} — valid for all x ≥ x_{N₁}, N ≥ N₁ because δ₁, every factor of e_{C,0} (SPEC §5.2 lines 569–571)
and log N/(x_N − 6) decrease in x resp. N. Side conditions (S1) ε < (1 + y₀)/2, (S2) u₁ ≥ 2a/t, (S3) (1 − y₀)/2 > ε + k₁,
(S4) u₁ ≥ 2a″/t as directed-rounded inequalities, recorded with σ_{N₁}, σ″, ε, k₁, ρ₁, a, a″, κ_T, ρ_F, u₁ (lines 644–648).
Integers ⌈K·Q_i⌉, ⌈K·E₁⌉; the kernel checks C-A5 and C-A6. `--direct` additionally sums Q₁'s and Q₂'s Dirichlet sums
term by term (5 141 000 terms each) and checks containment in the M-8 enclosure — a validation of M-8 at the largest range
used anywhere in the lane (both legs: contained = True, §3).

### 2.3 N₁ and the window count (C-A5, SPEC line 771; §5.4 lines 649–657; STATUS "N₁ ≈ 6–8·10⁶")

* **Recomputed.** Lemma T's sum S(N₁) := Q₁ + Q₂ + Q₃ + Q₄ + E₁ as a function of N₁, with the formulas above in the
  float64 planning model (`plan_rows.py`, `plan-run.txt`, 2026-09-06): S(10⁶) = 2.6526, S(6·10⁶) = 1.9591; the least N₁ with
  S < 2 − 0.003 is 5 140 982; rounded up to a multiple of 1000: **N₁ = 5 141 000**, S = 1.99700 (Q₁ = 1.7807, Q₂ = 0.1786,
  Q₃ = 0.01864, Q₄ = 0.01901, E₁ = 1.8·10⁻⁹). **Certified this session on both legs** (§3): S ≤ 1.996999372834 < 2
  (margin 3.0·10⁻³), (S1)–(S4) all true with room (u₁ = 15.4528 against 2a/t = 4.477 and 2a″/t = 6.276; ε = 2.0·10⁻¹⁷,
  k₁ = 2.2·10⁻¹⁶, ρ₁ − 1 = 2·10⁻¹⁶, ρ_F = 1.3022).
* **Why smaller than the 6–8·10⁶ of STATUS / SPEC §13.2 line 1131.** That figure is SPEC §5.4's own "indicative"
  reading (lines 649–654) of `row2_tail_indicative.log`: the crude Step-1 sums at y = y₀ give 2 − A − B = −0.086 at
  N = 3·10⁶ and +0.076 at 6·10⁶, and the text rounded the crossing up to "≈ 6–8·10⁶". The crossing itself is at ≈ 4.6·10⁶,
  and Lemma T's Q₃ + Q₄ ≈ 0.038 (the Lemma 8.2 max terms) moves it to 5.14·10⁶. No sharper lemma was used: Q₁…Q₄ are
  SPEC §5.4's five quantities verbatim.
* **Is there a sharper admissible Lemma T in the SPEC?** No. §5.4 lines 654–656: "the producer fixes N₁ rigorously (a
  mollified tail in the style of Gomila's `TAIL_LEMMA.md` would lower N₁ but is a different lemma and is out of this
  contract's scope)"; §11 line 1047 keeps the tail decision for M2a′ only. The only freedoms the SPEC grants are N₁ (the
  producer's, rigorously) and the row partition ("the number of rows is the producer's choice", line 656). Nothing in the
  requirement is shrunk: coverage is consecutive from N_start = 630 783 to N_end = 5 140 999, the tail at N₁ = 5 141 000,
  y from y₀ to yA with yA² ≥ 1 − 2t₀ (C-A1: yA² − 157/250 = 3556329/(25·10¹²) > 0).
* **Windows: N₁ − N_start = 4 510 217**, partitioned by the plan into **3 rows** [630783, 746495] (115 713 windows,
  planned T = 0.01202), [746496, 1469440] (722 945, T = 0.01202), [1469441, 5140999] (3 671 559, T = 0.1544); planned E =
  1.03·10⁻⁷, 7.6·10⁻⁸, 2.1·10⁻⁸ (E/T ≤ 10⁻⁵ everywhere; the paper's Table-1 floor at N₀ is 0.0376 against e_{C,0} ≈ 10⁻⁷,
  SPEC §5.2 line 572). The partition was chosen adaptively (largest N₊ with the binding piece's floor ≥ 0.012); the
  certified legs recompute every number — a row whose certified T came out ≤ E would be split, never dropped (none is
  expected: the float model matched the certified probes to 4–5 digits on all 13 pricing rows).

### 2.4 The literal in Lean

`row2AsymMP : AsymData` = 7 header integers + 3 rows × 4 integers + 6 tail integers = 25 integers, the largest 25 digits
(K = 10²⁴; the Arb literal's are 13 digits): about 700 bytes of data, a module of ≈ 3–4 KB with header and docstrings
(Lane B's `mp_0000.lean` is 32 KB for 184 rows). `decide +kernel` on it is trivially feasible: the placeholder literal of
the same shape, its two negative controls, and every proof of §1.4 elaborate together in **2.4 s wall** (`lake env lean`,
imports included; the kernel facts take milliseconds). Comparison (RUN-REPORT §5, `kernel-time.log`): Lane B's monolithic
`decide +kernel` on 17 947 rows took 28.2 s (1.57 ms/row); Gomila's 883-prism/3.1·10⁶-singleton-row lane is the case
that needs SPEC §7.6's packaging (items 2–3, lines 792–812: chunks of ≤ 1 000 rows, one module per unit, `maxRecDepth
100000`). Not needed here — one module per leg, one `decide +kernel` each. Even a 10⁴-row refinement (if larger floors
were ever wanted) would stay in one module at ≈ 15 s of kernel time.

---

## 3. Pricing, measured

### 3.0 What was reused from Session 17 (verified, not redone)

| item | s17 output | verification this session |
|---|---|---|
| planning model + partition | `plan_rows.py`, `rows-plan.json`, `plan-run.txt` (16:30 IST 2026-09-06) | re-read; formulas = derivation M/M-T; the 13 certified pricing rows agree with the model to 4–5 digits (e.g. singleton N₀, piece [y₀, 0.18]: model 0.02756, certified 0.027556) |
| producers | `p9_mp.py`, `p9_arb.py`; `selftest-{mp,arb}.txt` OK (G enclosure vs direct sums, 3 ranges) | `selftest-arb-s19.txt` OK after the patch; both compile; **defect fixed** (below) |
| pricing batch, rows | `pricing-plan.json` (13 probe rows spread over [N₀ − 1, N₁ − 1], 12 010 windows), `pricing/batches/{mp,arb}-row_0000…0012.json`, `pricing/rows-{mp,arb}.log`, `pricing/STATUS*.json` | all 26 records ok = True; timings below; cross-checked (§3.3) |
| pricing batch, tail | Arb crashed (`pricing/tail-arb-crash-s17.log`: `dict()` got two values for keyword `N1` at `p9_arb.py:309`); mp never reached | fixed in BOTH legs (`p9_mp.py` had the same line): `tr["N1"] = str(tr["N1"])` and `N1=` dropped from the `dict(...)` call; the record now carries N1 once, as a decimal string (what `assemble` and the cross-check expect). Added `--direct` to the mp leg (the Arb leg had it). Both tails run this session (§3.2). |
| cross-check tool | `crosscheck_lane_a.py` (s17 draft applied rtol 10⁻⁹/atol 10⁻¹² to E as well) | amended to the Lane B P-11 rule (§3.3); run record `pricing/crosscheck.txt` |

### 3.1 Row rates (the pricing batch, 2026-09-06 16:37–16:40 IST; `pricing/rows-{mp,arb}.log`, `STATUS.json`)

| leg | rows | windows | wall | per row | notes |
|---|---|---|---|---|---|
| mp (prec 288, N_c 10 000, m 2 000, 8 pieces) | 13 | 12 010 | 177.8 s | 13.3–13.8 s | width-independent: 13.3 s (1 window), 13.5 s (1 000), 13.7 s (10 000) |
| Arb (prec 320, same N_c, m, pieces) | 13 | 12 010 | 6.2 s | 0.5 s | width-independent likewise |

Re-measured this session with memory: mp probe row 9 ([2500000, 2509999], 10 000 windows): 14.6 s wall, **31.7 MB
RSS** (`/usr/bin/time -l`); Arb: 24–25 MB RSS (selftest, tail). All 13 rows, both legs: T_lo ≥ 0.02742 (the widest
probe) up to 0.4238 (N₁ − 1), E_hi ≤ 1.031·10⁻⁷, E/T ≤ 3.8·10⁻⁶.

**Rates.** Per row: mp ≈ 260 rows/h, Arb ≈ 7 000 rows/h. Because a row's cost does not depend on its width (M-8: every
G is a 10 000-term head plus 4 000 integrand evaluations, whatever N₊), "windows per hour" is a property of the
partition: for the plan's 3 rows, mp covers 4 510 217 windows in ≈ 41 s (≈ 4·10⁸ windows/h), Arb in ≈ 1.5 s.

### 3.2 The tail row (this session, 2026-09-09 20:52 IST; `pricing/tail-{mp,arb}.log`, `pricing/batches/{mp,arb}-tail.json`)

| leg | wall | of which `--direct` | RSS | Q₁ + Q₂ + Q₃ + Q₄ + E₁ (certified, ⌈K·⌉ per part) | (S1)–(S4) | direct contained |
|---|---|---|---|---|---|---|
| Arb | 12.3 s | 12.2 s | 24.9 MB | 1 996 999 372 834 / 10¹² = 1.996999372834 < 2 | all true | True |
| mp | 415.2 s | 414.2 s | 31.7 MB | 1 996 999 372 832 115 735 567 933 / 10²⁴ = 1.996999372832… < 2 | all true | True |

Without `--direct` the tail row costs < 1 s on either leg. Parts (Arb, floats of the exact rationals): Q₁ = 1.7807386837,
Q₂ = 0.1786072313, Q₃ = 0.0186384670, Q₄ = 0.0190149890, E₁ = 1.8229·10⁻⁹; the M-8 enclosure of Q₁'s sum is
[1.78073825, 1.78073868] (width 4.3·10⁻⁷) and the direct sum 1.7807384676 lies inside it.

### 3.3 Cross-check per row (P-11; `crosscheck_lane_a.py pricing` → `pricing/crosscheck.txt`, exit 0)

Rule, carried over from Lane B (arb-leg-notes §5, INSTANCE-REPORT §2 item 3): T_lo and the tail's Q₁…Q₄ are the SAME
derived numbers computed independently — they must agree to rtol 10⁻⁹ and both legs must reach the same ok verdict (else
stop the line); E_hi and E₁ are upper bounds evaluated on hulls, reported side by side, consistent if max/min ≤ 1 + 10⁻³
(Lane B saw the Arb E larger by < 10⁻⁴ on a 1-wide box). Result: **14/14 items CONSISTENT, 0 disagreements** —
T_lo agrees on every row and every piece to ≤ 1.6·10⁻⁷⁹ relative (both legs compute the same real number to ≈ 80 digits);
E_hi agrees to ≤ 3.1·10⁻⁷ on singleton rows and to 2.0–6.2·10⁻⁴ on the 1 000/10 000-window rows (the Arb ball's hull
slack; Arb's bound is the larger on every row); the tail's Q₁…Q₄ agree to ≤ 5·10⁻⁸¹, E₁ to 4.3·10⁻⁸; ok = True on both
legs for all 14 items; direct containment true on both. The s17 draft tool flagged the three wide rows on E under
atol 10⁻¹² — a tool calibration, not a producer disagreement; recorded and amended (docstring dated). Each leg's transcript
keeps its own E (two literals, two theorems).

### 3.4 Projection for the full run (3 rows + tail per leg, under the thermal cap)

| leg | rows | tail (`--direct`) | assemble | total wall | processes |
|---|---|---|---|---|---|
| mp | 3 × ≈ 14 s ≈ 42 s | ≈ 415 s | < 1 s | **≈ 8 min** | 1 |
| Arb | 3 × ≈ 0.5 s | ≈ 12 s | < 1 s | **≈ 15 s** | 1 |

Two heavy jobs in all (the two legs in parallel) — half the cap of 4; no `lake` process during the producer run; RSS
< 35 MB each. Lean afterwards: emit + back-parse (seconds), `lake build -j2` of `Asym.lean` (proofs: seconds) and the two
literal modules (kernel: milliseconds; import-dominated ≈ 3–4 s each), `#print axioms`. **Projected wall-clock for the
whole Lane A compute ≈ 10 minutes, against the 48-hour line.** Batching: one row = one batch = one checkpoint file; a kill
loses at most one row (≤ 14 s of work); `--resume` skips rows on disk.

### 3.5 Exact command lines (run from this directory; `OUT` = this directory so that `STATUS.json` is
`results/d1-m2a/lane-a/STATUS.json` as the brief asks)

    # pricing (what was run; s17 rows 2026-09-06, s19 tails 2026-09-09) — outputs under pricing/
    python3 p9_mp.py  rows --plan pricing-plan.json --out pricing            # 177.8 s, 13 rows
    python3 p9_arb.py rows --plan pricing-plan.json --out pricing            # 6.2 s
    nohup /usr/bin/time -l python3 p9_arb.py tail --plan pricing-plan.json --out pricing --direct > pricing/tail-arb.log 2>&1 &
    nohup /usr/bin/time -l python3 p9_mp.py  tail --plan pricing-plan.json --out pricing --direct > pricing/tail-mp.log  2>&1 &
    /usr/bin/time -l python3 p9_mp.py rows --plan pricing-plan.json --out <scratch> --rows 9          # memory probe
    python3 crosscheck_lane_a.py pricing > pricing/crosscheck.txt

    # the full run (phase 3, only on GO) — detached, one process per leg, resumable
    nohup ./run_leg.sh mp  . > producers-mp.log  2>&1 &
    nohup ./run_leg.sh arb . > producers-arb.log 2>&1 &
    #   = python3 p9_<leg>.py rows --plan rows-plan.json --out . --resume
    #     python3 p9_<leg>.py tail --plan rows-plan.json --out . --direct
    #     python3 p9_<leg>.py assemble --plan rows-plan.json --out . --name asym-<leg>.json
    python3 crosscheck_lane_a.py .                                           # after both legs finish; exit 0 required
    # then: emit the two literals (successor of emit_lean_m2a.py for the asymptotic kind), back-parse, lake build -j2

Polling: `STATUS.json` (merged; per leg `{phase, leg, rows_done, rows_total, windows_done, windows_total, started,
updated, elapsed_s, eta_hours, errors, last_row, last_T, last_E}`; phases rows → rows-done → tail-done), `STATUS-mp.json`,
`STATUS-arb.json`, `batches/<leg>-row_000k.json`, `batches/<leg>-tail.json`, `asym-<leg>.json`. Re-launching the same
`run_leg.sh` command after a kill resumes.

### 3.6 Lean cost, measured (`laneA-shapes-typecheck.log`)

`lake env lean laneA-shapes-scratch.lean` — the §1 definitions, the four proofs, a 3-row placeholder literal with its
kernel fact and two negative-control kernel facts: **2.4 s wall** (1.8 s user), zero errors, zero warnings after the
`push Not` change. The names check `names-check.lean` (38 `#check`s): 15.5 s wall (cold import load).

---

## 4. GO / NO-GO

**GO.** Both criteria hold with two to three orders of magnitude to spare:

1. **Wall-clock ≪ 48 h under the cap.** The measured row cost is width-independent (13.3–13.8 s mp, 0.5 s Arb, on rows of
   1, 1 000 and 10 000 windows) and the plan needs 3 rows; the tail row is done and certified on both legs. Projection
   ≈ 8 min (mp, with the optional 7-minute direct-sum validation) and ≈ 15 s (Arb), two processes, < 35 MB each.
2. **The literal is kernel-checkable as one module per leg** (25 integers; the placeholder of identical shape checks in
   milliseconds inside a 2.4 s file), no batching needed; SPEC §7.6's provision stands unused.

What phase 3 does, in order: (a) Lean builder writes `Zeta23/DBN/Asym.lean` from `laneA-shapes-scratch.lean` (proofs
already checked; `#print axioms` standard), `lake build -j2`; (b) launch the two detached producers (`run_leg.sh mp`,
`run_leg.sh arb`), poll `STATUS.json`; (c) after both legs: `crosscheck_lane_a.py .` must exit 0 (else stop, record); (d)
emit the two literals, back-parse, kernel-check, replace `hLaneA` per §1.5, `#print axioms`, Opus audit. Nothing in the
Lean tree was edited by this phase; the full run was not launched.

Residual risks, stated: (i) a certified T for one of the three wide plan rows could differ from the float plan by the
enclosure width (≈ 10⁻⁶) — immaterial against E ≈ 10⁻⁷ at T ≈ 0.012; if a row ever came out with T ≤ E, split it (one
more row = 14 s), never shorten the coverage; (ii) the hull slack of E on the widest row (3.7·10⁶ windows) will be larger
than on the 10⁴-window probe — E's bound is still ≤ 10⁻⁵ of T; the cross-check's etol 10⁻³ may need the widest row's
ratio recorded rather than gated if it exceeds 10⁻³ (record, compare E against T, do not merge legs); (iii) the honest
label after the replacement is SPEC §3.7's — say "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3", never
"fully machine-checked".

Files written this phase (all under `results/d1-m2a/lane-a/`): `PLAN.md` (this), `p9_mp.py`/`p9_arb.py` (patched, dated
comments), `crosscheck_lane_a.py` (amended, dated), `run_leg.sh`, `laneA-shapes-scratch.lean` + `laneA-shapes-typecheck.log`,
`selftest-arb-s19.txt`, `pricing/tail-{mp,arb}.log`, `pricing/batches/{mp,arb}-tail.json`, `pricing/tail-arb-crash-s17.log`
(the s17 crash, kept), `pricing/tail-launch-stamp-s19.txt`, `pricing/crosscheck.txt`, `pricing/STATUS*.json` (tail-done).
