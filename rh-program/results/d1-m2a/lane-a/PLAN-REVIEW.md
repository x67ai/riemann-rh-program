# D1 M2a Lane A — PLAN.md review (REVIEWER, second model)

**Stamp:** 2026-09-09 21:10–21:25 IST, machine clock (Session 19, review of `PLAN.md` written 21:05 IST).
**Verdict: APPROVED** — the GO stands. No trust-critical defect. Six non-blocking items (F-1 … F-6), each with
the exact fix, in §7.

**The trust-critical question, answered first.** *Does `cert_of_checkAsym`'s conclusion, routed through the glue
lemma, match what `lambda_le_point2` consumes as `hLaneA`?* **Yes, verified by elaboration, not by eye.** I wrote
`review-shapes.lean` (a copy of the planner's scratch in namespace `LaneAReview`, importing the built
`Zeta23.DBN.Instance02` instead of only `Defs`) and fed `row2_laneA hAsym hTail` into the *real*
`lambda_le_point2`, `lambda_le_point2_arb` and `row2_ray_mp` from the working tree as their `hLaneA` argument.
`lake env lean` exit 0, zero errors, zero warnings, 2.28 s wall (log `review-shapes.log`). A one-character
mismatch would have failed to elaborate. `#print axioms row2_laneA` = `[propext, Classical.choice, Quot.sound]`.

---

## 0. What this review did

| step | how |
|---|---|
| read PLAN.md in full (427 lines) | plus `BRIEF.md`, SPEC §5/§6/§7.2/§7.4/§7.5/§7.6/§8.1–8.3/§13.2/§3.7, `v11/GLUE-NOTES.md` (all 122 lines), `v11/AUDIT.md` R-1, `RUN-REPORT.md` §6, `lean/README.md` §label |
| Lean tree opened | `~/rh-lean-work/zeta-23-lean-main/Zeta23/DBN/Instance02.lean` (lines 140–229 read directly), `Defs.lean` (`Polymath15Bridge'`, lines 170–177), `laneA-shapes-scratch.lean` (all 232 lines) |
| Mathlib names | `lake-manifest.json` rev **51e6992** confirmed = the plan's claim; every name `sed`-printed at the plan's exact `file:line`; deprecation context inspected around each |
| Lean re-elaboration | `review-shapes.lean` → `review-shapes.log`, exit 0 (composition test + 4 `decide +kernel` review facts) |
| producers re-run | a fresh **50-window** batch on BOTH legs (`review-batch/`), timed and memory-probed, then `crosscheck_lane_a.py review-batch` (exit 0) |
| arithmetic | L-A1, C-A1, C-A5, the window count, the tail margin and the projections re-derived from scratch in exact rationals |
| thermal | `pgrep` checked before each heavy step; never more than 2 heavy jobs (the two legs) at once; no `lake build`; `caffeinate` running |
| tree | **untouched** — nothing written under `~/rh-lean-work/`; all review output under `results/d1-m2a/lane-a/` |

---

## 1. Table A — PLAN §1 "Statements" (the trust-critical section)

| # | claim in PLAN §1 | verified how | verdict |
|---|---|---|---|
| A1 | `hLaneA`'s type, quoted verbatim | read `Instance02.lean` lines 163–164 (`row2_ray_mp`), 182–183 (`row2_ray_arb`), 208–209 (`lambda_le_point2`), 220–221 (`lambda_le_point2_arb`) — all four identical, character-for-character the plan's quote | **OK** |
| A2 | consumed as (ii′) of `Polymath15Bridge'` at line 169 / line 188; passed through at line 213 | read those lines; `refine hH3.1 (93/500) 5000000194858 (16733/100000) … (hH1_row2 hH1) hLaneA ?_` at 169 and 188; `exact row2_ray_mp hH1 hEncl hLaneA hH3 t (le_trans row2_bound_le_point2 ht)` at 213 (and 225 for `_arb`) | **OK** |
| A3 | (ii′) is the slot `hLaneA` fills | `Defs.lean:170–177`: `Polymath15Bridge'`'s third hypothesis is `∀ x y : ℝ, X + 1 ≤ x → y₀ ≤ y → y^2 ≤ 1 - 2*t₀ → Ht t₀ (x + y*I) ≠ 0`; at `t₀ = 93/500, X = 5000000194858, y₀ = 16733/100000` that is exactly `hLaneA` | **OK** |
| A4 | `AsymRow`/`TailRow`/`AsymData`/`checkAsymRow`/`consecutive`/`lastNhi`/`checkAsym` as printed | compared clause-by-clause with SPEC §8.2 lines 880–883 and the normative SPEC §7.4 lines 766–772; the scratch's text (lines 27–76) matches | **OK** |
| A5 | clause map C-A1 = first eight conjuncts, C-A2 = `0 < rows.length`, C-A3 = `rows.all checkAsymRow`, C-A4 = `consecutive`, C-A5 = `tail.N1 = lastNhi + 1`, C-A6 = last six | SPEC §7.4 read line by line against `checkAsym`'s body; K ≥ 1, `1 ≤ t0d`, `0 < t0n`, `1 ≤ y0d`, `0 < y0n`, `1 ≤ yAd`, `0 ≤ yAn`, `(t0d − 2·t0n)·yAd² ≤ yAn²·t0d` = SPEC's C-A1 exactly | **OK** |
| A6 | only ℤ/ℕ arithmetic, `decide +kernel`, no `native_decide` | inspected `checkAsym`; `+`, `*`, `^2`, `≤`, `<`, `=`, `List.length`, `List.all`; `grep native_decide` over the scratch: zero hits | **OK** |
| A7 | `AsymEnclOK` / `TailOK` as SPEC §8.1 lines 845, 849 | `sed -n '845p;849p' SPEC.md` — identical text | **OK** |
| A8 | `cert_of_checkAsym` "statement verbatim" from SPEC §8.3 lines 899–902 | `sed -n '899,902p' SPEC.md` vs scratch lines 119–122 — identical, including the `∀ x y : ℝ, ∀ r ∈ d.rows` order and the `(r.Nlo : ℝ) ≤ windowIdx (At0 d) x` hypothesis | **OK** |
| A9 | proof uses only C-A4 for coverage, and C-A1(K≥1)/C-A3/C-A4/C-A5 in the main theorem | read the `obtain` pattern at scratch line 125: exactly `hK, hrows, hcons, hN1` kept, the rest discarded with `-` — so C-A2, C-A6 and C-A1's yA² conjunct are **checked but unconsumed**, which is SPEC §5.1's design ("the theorem does not consume the row"). The plan says this in §1.4 item 2 | **OK** (see note F-6) |
| A10 | `cover_of_consecutive` is correct | re-derived by hand on `[]`, `[r0]`, `r0 :: s :: l`; the `hs`/`omega` step is the only use of C-A4; re-elaborated in `review-shapes.lean` | **OK** |
| A11 | L-A2 `windowIdx_mono` statement and proof | scratch lines 152–158; `Nat.floor_mono ∘ Real.sqrt_le_sqrt ∘ div_le_div_of_nonneg_right`; elaborates | **OK** |
| A12 | L-A1 `row2_windowIdx_ge (x) (hx : 5000000194858 + 1 ≤ x) : (630783 : ℝ) ≤ windowIdx (93/500) x` | scratch lines 163–176; elaborates; matches SPEC §6's obligation "L-A1 N(X + 1) ≥ N_start from a rational bound on π" and SPEC §5.3 lines 576–582 | **OK** |
| A13 | L-A1 arithmetic: `4·3.141593·630783² − 3.141593·(93/500)/4 = 4 999 998 482 392.06`, margin `1 712 466.9`; equivalently `(X+1)/(4·3.141593) + t₀/16 − 630783² = 136 273.8 > 0` | recomputed in exact `Fraction`: **4 999 998 482 392.057**, margin **1 712 466.943**, second form **136 273.774**; `x_{N₀}` (true π) = 4 999 997 931 063.317, matching SPEC's `row2_arith.log` bracket | **OK** |
| A14 | "so N_start = N₀ with no need for N₀ − 1" | follows from A13 (margin > 0) and is *proved*, not argued: `row2_windowIdx_ge` elaborates | **OK** |
| A15 | "it holds with **a third** of that slack to spare" | 1 712 466.9 / 2 263 794.7 = **0.756** — three quarters, not a third; the π-rounding costs 551 328.7 (a quarter), not the ≈1.6·10⁶ SPEC §5.3's cruder 10⁻⁶ estimate implies | **FIX F-4** |
| A16 | `#print axioms` = `[propext, Classical.choice, Quot.sound]` for the four theorems, `[propext]` for the kernel fact | re-run independently: identical five lines, my own log `review-shapes.log` | **OK** |
| A17 | two negative controls return `false` by `decide +kernel` | present at scratch lines 193–199 (row gap → C-A4; tail sum + 4·10²¹ → C-A6); both elaborate in my re-run | **OK** |
| A18 | the glue lemma's conclusion "is character-for-character the type of `hLaneA`" | **the composition test**: `lambda_le_point2 hH1 hEncl (row2_laneA hAsym hTail) hH3` and the `_arb` and `row2_ray_mp` variants all elaborate against the built tree, exit 0 | **OK — the trust-critical check passes** |
| A19 | `y ≤ yA` from `y² ≤ 157/250 < yA²`, `le_of_sq_le_sq` | `yA² − 157/250 = 3556329/(25·10¹²) = 1.4225·10⁻⁷ > 0` recomputed exactly (the plan's own figure); C-A1 cross-multiplied: `314·5000000² = 7 850 000 000 000 000 ≤ 3962323²·500 = 7 850 001 778 164 500` ✓ | **OK** |
| A20 | `Ht ≠ 0` from `Ht/Bt ≠ 0` by `div_ne_zero_iff` (L-B3 not needed inside `cert_of_checkAsym`) | scratch line 221 `exact (div_ne_zero_iff.mp hg).1`; elaborates | **OK** |
| A21 | the replacement in `Instance02.lean`: binder `hLaneA` → `(hAsym) (hTail)` in all four theorems, token `hLaneA` → `(row2_laneA_mp hAsym hTail)` at 169/188, the two `lambda_le_point2*` bodies pass `hAsym hTail` | consistent with what I read at lines 160–225; the composition test shows the substituted term is accepted at the (ii′) slot | **OK** |
| A22 | each leg keeps its own Lane A literal paired with its own Lane B literal (D-R3, legs never merged) | matches `Instance02.lean`'s existing two-theorem structure; the producers share no code (below, D6) | **OK** |
| A23 | module placement `Zeta23/DBN/Asym.lean` + `Instance02/Asym_{mp,arb}.lean`, `lake build -j2` | consistent with SPEC §7.6 item 2's pattern and the existing `Instance02/` layout (114 modules, `mp_0000.lean` = 32 255 B for 184 rows — the plan's "32 KB for 184 rows" verified) | **OK** |
| A24 | after the change the label is SPEC §3.7's (H1, H2-B, H2-A, H-TAIL, H3) and RUN-REPORT §6 item 4's short sentence becomes licensed with §3.7's gloss (audit ruling R-1) | SPEC §3.7 lines 365–376 read; AUDIT R-1 (line 29) and RUN-REPORT §6's dated Session-16 note both gate the short sentence on **item 3 landing**, which is this stream — so the plan's reading is right | **OK**, but two files carry the "NOT licensed" wording and are not in the plan's phase-3 list → **FIX F-5** |

---

## 2. Table B — every Mathlib/core name PLAN §1.4 lists, at the pinned revision

Pinned Mathlib **rev 51e6992efd06126df61a496bebf8f49482a4e129** (`lake-manifest.json`) = the plan's claim.
Each name printed with `sed -n '<line>p'` at the plan's own `file:line`; the four lines above each were also read to
check for a `@[deprecated]` attribute. **All twelve exist, at exactly the cited line, none deprecated.**

| name | plan's citation | what the line actually says | verdict |
|---|---|---|---|
| `Real.pi_lt_d6` | `Analysis/Real/Pi/Bounds.lean:184` | `theorem pi_lt_d6 : π < 3.141593 := by` | **OK** |
| `Real.pi_gt_d6` | same file :178 | `theorem pi_gt_d6 : 3.141592 < π := by` | **OK** |
| `Real.pi_pos` | `Analysis/SpecialFunctions/Trigonometric/Basic.lean:157` | `theorem pi_pos : 0 < π :=` | **OK** |
| `Real.sqrt_le_sqrt` | `Analysis/Real/Sqrt.lean:209` | `theorem sqrt_le_sqrt (h : x ≤ y) : √x ≤ √y` | **OK** |
| `Real.le_sqrt_of_sq_le` | `Analysis/Real/Sqrt.lean:258` | `theorem le_sqrt_of_sq_le (h : x ^ 2 ≤ y) : x ≤ √y` | **OK** |
| `Nat.floor_mono` | `Algebra/Order/Floor/Semiring.lean:89` | `theorem floor_mono : Monotone (floor : R → ℕ)` | **OK** |
| `Nat.le_floor` | `Algebra/Order/Floor/Defs.lean:143` | `theorem le_floor (h : (n : α) ≤ a) : n ≤ ⌊a⌋₊` | **OK** |
| `div_le_div_of_nonneg_right` | `Algebra/Order/GroupWithZero/Basic.lean:1199` | `lemma … (hab : a ≤ b) (hc : 0 ≤ c) : a / c ≤ b / c` (attrs `@[mono, gcongr, bound]`, not deprecated) | **OK** |
| `le_div_iff₀` | same file :1134 | `lemma le_div_iff₀ (hc : 0 < c) : a ≤ b / c ↔ a * c ≤ b` | **OK** |
| `div_pos` | same file :880 | `lemma div_pos (ha : 0 < a) (hb : 0 < b) : 0 < a / b` | **OK** |
| `div_ne_zero_iff` | `Algebra/GroupWithZero/Units/Basic.lean:291` | `theorem div_ne_zero_iff : a / b ≠ 0 ↔ a ≠ 0 ∧ b ≠ 0` | **OK** |
| `le_of_sq_le_sq` | `Algebra/Order/Ring/Abs.lean:134` | `theorem le_of_sq_le_sq (h : a ^ 2 ≤ b ^ 2) (hb : 0 ≤ b) : a ≤ b` | **OK** |
| `norm_zero`, `norm_pos_iff` | `Analysis/Normed/Group/Basic.lean:134, 993` | both are the `@[to_additive (attr := simp) …]` names on those lines | **OK** |
| `Int.cast_natCast`, `Int.cast_le` | `Data/Int/Cast/Basic.lean:71`; `Algebra/Order/Ring/Cast.lean:56` | `theorem cast_natCast (n : ℕ) : ((n : ℤ) : R) = n`; `@[simp, norm_cast] lemma cast_le` | **OK** |
| core `List`/`Bool` lemmas | Lean core (Init) | all used inside the scratch, which elaborates with zero errors | **OK** |
| "`push_neg` is deprecated in this Mathlib — use `push Not`" | — | `Mathlib/Tactic/Push.lean:283,350`: `logWarning "\`push_neg\` has been deprecated. Prefer using \`push Not\` instead."` | **OK** |
| "the names check `names-check.lean` (38 `#check`s): 15.5 s wall" (§3.6) and "`#check` in `names-check.lean`" (§1.4) | — | **the file does not exist** anywhere under `rh-program/` or the Lean tree (`find … -name 'names-check*'` → nothing). The *claim* is true — I verified all twelve names independently — but its cited evidence is missing | **FIX F-1** |

---

## 3. Table C — PLAN §2 "Producers", and the window count re-derived from SPEC C-A5

| # | claim | verified how | verdict |
|---|---|---|---|
| C1 | the two legs are independent code, sharing only the untrusted plan (P-1, D-R3) | `p9_mp.py` imports `ball.py` + `ft_mp.py` + `mpmath.iv`; `p9_arb.py` imports `producer_arb.py` + `flint`; neither imports the other; the only common input is `rows-plan.json` | **OK** |
| C2 | scales K = 10²⁴ (mp) and 10¹² (Arb); floors `⌊K·lower⌋`, bounds `⌈K·upper⌉` | `--K` defaults in both `main()`s; `floor_frac(K*T_lo)`, `ceil_frac(K*E_hi)` in `run_rows`; `ceil_frac` for all five tail parts | **OK** |
| C3 | Lemma T restated: Q₁, Q₂, Q₃, Q₄, E₁, (S1)–(S4), κ_T, a, a″, c_γ, k₁, ρ₁, σ_{N₁}, σ″ | compared word for word with SPEC §5.4 Steps 2–5 (lines 596–648). Every definition matches: `σ″ := σ_{N₁} − y₀ − k₁`, `a := (1−y₀)/2 + ε`, `a″ := (1+y₀)/2 + ε + k₁`, `κ_T := max(√(2/(e t)), 2/(e t u₁))`, `c_γ := e^{0.02}ρ₁`, `k₁ := t·yA/(2(x_{N₁} − 6))` | **OK** |
| C4 | (S1)–(S4) hold "with room": u₁ = 15.4528 vs 2a/t = 4.477 and 2a″/t = 6.276 | recomputed: `log 5141000 = 15.452758`, `2a/t = 4.476720`, `2a″/t = 6.275968` | **OK** |
| C5 | **N₁ = 5 141 000**, least float N₁ = 5 140 982, S(10⁶) = 2.6526, S(6·10⁶) = 1.9591, S(N₁) = 1.99700 | `plan-run.txt` (the s17 run record) prints all five verbatim; the certified legs reproduce S ≤ 1.996999372834 | **OK** |
| C6 | the SPEC/STATUS "6–8·10⁶" is SPEC §5.4's own indicative rounding, crossing ≈ 4.6·10⁶ | SPEC §5.4 lines 649–654 read; `plan-run.txt`'s crude table gives 2−A−B = −0.0864 at 3·10⁶ and +0.0758 at 6·10⁶ → linear crossing 4.60·10⁶; Q₃+Q₄ = 0.0377 moves it to 5.14·10⁶. SPEC §13.2 line 1131 is the STATUS bullet the plan cites, correctly | **OK** |
| C7 | "no sharper admissible Lemma T in the SPEC" | SPEC §5.4 lines 654–656 (mollified tail "a different lemma … out of this contract's scope") and §11 line 1047 confirm | **OK** |
| C8 | "nothing shrunk" — coverage 630783…5140999 consecutive, tail at 5141000, yA² ≥ 1−2t₀ | a *smaller* N₁ means fewer windows to cover and a *stronger* certified tail inequality; the obligation "cover every x ≥ X+1" is met by rows ∪ tail. C-A5 and C-A1 re-derived below | **OK** |
| C9 | **windows = N₁ − N_start = 4 510 217**, 3 rows of 115 713 / 722 945 / 3 671 559 | re-derived twice: `5141000 − 630783 = 4510217`; and `(746495−630783+1) + (1469440−746496+1) + (5140999−1469441+1) = 115713 + 722945 + 3671559 = 4510217`. Also as kernel facts (`review_windows`, `review_rowwidths` in `review-shapes.lean`, `decide +kernel`) | **OK** |
| C10 | C-A5 `tail.N1 = lastNhi rows + 1` for the plan's rows | `5140999 + 1 = 5141000`; kernel fact `review_CA5 : lastNhi row2AsymPH.rows + 1 = row2AsymPH.tail.N1` by `decide +kernel` | **OK** |
| C11 | C-A1 `yA² ≥ 1 − 2t₀` for `yA = 3962323/5000000` | kernel fact `review_CA1 : (500 − 2·93)·5000000² ≤ 3962323²·500` by `decide +kernel`; margin `3556329/(25·10¹²)` — the plan's own number | **OK** |
| C12 | planned E = 1.03·10⁻⁷ / 7.6·10⁻⁸ / 2.1·10⁻⁸, E/T ≤ 10⁻⁵ | `rows-plan.json` and `plan-run.txt` agree; worst planned E/T = 1.031e-7/0.012025 = 8.6·10⁻⁶ | **OK** |
| C13 | the literal is 25 integers (7 + 3×4 + 6), ≈700 B of data | counted on the placeholder literal in the scratch, which is exactly that shape and kernel-checks in the 2.28 s file | **OK** |
| C14 | SPEC §7.6 batching not needed; Lane B's 17 947-row monolith took 28.2 s | `kernel-time.log`: `real 28.18` for the two Lane B kernel facts; the Lane A literal is 3 rows | **OK** |
| C15 | the s17 crash was a duplicate `N1=` keyword, fixed in BOTH legs | `pricing/tail-arb-crash-s17.log` shows `TypeError: dict() got multiple values for keyword argument 'N1'` at `p9_arb.py:309`; the current `p9_arb.py:309` and `p9_mp.py:396` both read `tr["N1"] = str(tr["N1"])  # 2026-09-09 (Session 19) …` and the `dict(...)` calls no longer pass `N1` twice | **OK** |
| C16 | `--direct` added to the mp leg | `--direct` present in both `main()`s; `pricing/batches/mp-tail.json` records `direct.contained = True` | **OK** |

---

## 4. Table D — PLAN §3 "Pricing", checked against a fresh 50-window batch run by the reviewer

**The re-run.** `review-batch/plan.json`: row 0 = `[630783, 630783]` (1 window, = pricing row 1), row 1 =
`[5140999, 5140999]` (1 window, = pricing row 12), row 2 = `[2500000, 2500047]` (**48 windows, a width neither
the plan nor s17 ever ran**) — 50 windows exactly, the brief's cap. Both legs, in parallel (2 heavy jobs, half the
thermal cap), `/usr/bin/time -l`. Logs `review-batch/rows-{mp,arb}.log`, records `review-batch/batches/`,
`review-batch/STATUS.json`, cross-check `review-batch/crosscheck.txt`.

| # | claim | measured by the reviewer | verdict |
|---|---|---|---|
| D1 | mp costs 13.3–13.8 s per row | **13.5 s, 13.5 s, 13.7 s**; 40.70 s for the 3 rows (41.05 s real) | **OK** |
| D2 | Arb costs ≈ 0.5 s per row | **0.4 s, 0.4 s, 0.4 s**; 1.33 s for the 3 rows (1.41 s real) | **OK** |
| D3 | the per-row cost is width-independent (M-8: 10 000 head terms + 4 000 integrand evaluations per G, whatever N₊) | a 48-window row cost 13.7 s against 13.5 s for a singleton (mp) and 0.4 s vs 0.4 s (Arb) — the s17 finding reproduces at a third width | **OK** |
| D4 | mp RSS ≈ 31.7 MB, Arb 24–25 MB, "< 35 MB each" | `maximum resident set size` **31 653 888 B = 31.65 MB** (mp), **25 018 368 B = 25.02 MB** (Arb) | **OK** |
| D5 | the s17 pricing numbers are reproducible | rows 0 and 1 reproduce pricing rows 1 and 12 **bit-identically**: same `T_lo`, same `E_hi`, same emitted integers `T`, `E`, on **both** legs | **OK** |
| D6 | T_lo up to 0.4238 at N₁ − 1; minimum over the 13 probes 0.02742; E_hi ≤ 1.031·10⁻⁷; E/T ≤ 3.8·10⁻⁶ | recomputed over all 13 pricing records: min `T_lo` = **0.0274170**, max `E/T` = **3.760·10⁻⁶**, `T_lo(5140999)` = **0.42381267** (my own re-run agrees to every printed digit) | **OK** |
| D7 | the P-11 rule as amended (T_lo and Q₁…Q₄ to rtol 10⁻⁹; E_hi/E₁ as hull upper bounds, consistent if max/min ≤ 1+10⁻³, larger leg recorded) | read `crosscheck_lane_a.py` in full: `close()` for T and Q, `ub_ok()` for E and E₁, `ok` verdicts compared, exit 1 on any disagreement. Matches the Lane B rule it cites | **OK** |
| D8 | "14/14 items CONSISTENT, 0 disagreements", T_lo to ≤1.6·10⁻⁷⁹, E to 3·10⁻⁷ (singletons) and 2–6·10⁻⁴ (wide rows), tail Q to 1e-81, E₁ to 4.3·10⁻⁸ | `pricing/crosscheck.txt` re-read end to end: "compared 14 items; disagreements 0; max E rel diff 6.24e-04 (etol 1e-03); CONSISTENT" | **OK** |
| D9 | my own batch cross-checks | `crosscheck_lane_a.py review-batch` → 3/3 **OK**, **exit 0**; T_lo rel diff 1.6·10⁻⁷⁹ / 4.2·10⁻⁸¹ / 7.3·10⁻⁸¹; E rel diff 3.1·10⁻⁷ / 7.9·10⁻⁸ / **3.06·10⁻⁶** (the 48-window row); all 8 y-pieces agree on every row | **OK** |
| D10 | tail: Arb 12.3 s / 24.9 MB, mp 415.2 s / 31.7 MB, sum < 2 with margin 3.0·10⁻³, (S1)–(S4) true, direct containment true on both | `pricing/batches/{mp,arb}-tail.json`: mp `sum_int = 1 996 999 372 832 115 735 567 933` at K = 10²⁴, Arb `1 996 999 372 834` at K = 10¹²; `(2K − Σ)/K = 3.000627·10⁻³` on both; `side` all true; `direct.contained = true` on both; `seconds` 414.85 / 12.19 | **OK** |
| D11 | `run_leg.sh` is detached, resumable, one checkpoint per row | read: `--resume` on rows, `--direct` on tail, `assemble` last; `run_rows` skips a row whose batch file exists | **OK** on the happy path; see **FIX F-3** for the failure path |
| D12 | `STATUS.json` carries `{phase, windows_done, windows_total, started, updated, eta_hours, errors}` per the brief | `review-batch/STATUS.json` written by my run carries exactly those plus `rows_done/rows_total/elapsed_s/last_row/last_T/last_E`, merged per leg | **OK** (minor: the `tail-done` update replaces the leg's dict, so `windows_*` disappear once the tail runs — cosmetic, noted in F-3's fix) |
| D13 | Lean cost "2.4 s wall (1.8 s user), zero errors, zero warnings" | my re-elaboration of a *larger* file (same content + the composition test + 4 kernel facts + the whole `Instance02` import chain): **2.28 s wall, 1.74 s user, zero errors, zero warnings** | **OK** |
| D14 | selftests OK on both legs (G enclosure contains the direct sums at three ranges; head sum at N₀ ≈ 2.2789) | `selftest-mp.txt`, `selftest-arb-s19.txt` read: `contains: True` ×3 on each leg, head sum `[2.278881, 2.278883]` vs the SPEC's indicative 2.2789 | **OK** |

---

## 5. Table E — PLAN §4 GO / NO-GO arithmetic

| # | claim | recomputed | verdict |
|---|---|---|---|
| E1 | mp full run ≈ 8 min = 3 × ≈14 s rows + ≈415 s tail | 3 × 13.57 s (my measurement) = 40.7 s, + 414.85 s (recorded) = **455.6 s = 7.6 min** | **OK** |
| E2 | Arb full run ≈ 15 s | 1.33 s + 12.19 s = **13.5 s** | **OK** |
| E3 | "≈ 10 minutes for the whole Lane A compute, against the 48-hour line", "two to three orders of magnitude to spare" | 48 h = 172 800 s; 455.6 s is **0.26 %** of it, a factor **379** = 2.6 orders of magnitude | **OK** |
| E4 | two heavy jobs, half the cap of 4; RSS < 35 MB each; no `lake` during the producers | reproduced exactly in my run (2 python3, 31.65 + 25.02 MB, no lake); `pgrep` clean before and after | **OK** |
| E5 | a kill loses at most one row (≤ 14 s); `--resume` skips rows on disk | one JSON per row written by `atomic_json` after each row; `--resume` verified in the code | **OK** on the happy path; **FIX F-3** on the failure path |
| E6 | the literal is kernel-checkable as one module per leg, no batching | the identical-shape placeholder's `decide +kernel` sits inside a 2.28 s file whose import load dominates; Lane B's 17 947-row comparison from `kernel-time.log` is real | **OK** |
| E7 | residual risk (i): a certified T could differ from the float plan by ≈10⁻⁶, immaterial against E ≈ 10⁻⁷ at T ≈ 0.012; split a row rather than shorten coverage | sound, and the measured evidence supports it (float model 0.02756 vs certified 0.0275565 on the singleton; all 13 probes agree to 4–5 digits). The mitigation "split, never shorten" is the right one | **OK** |
| E8 | residual risk (ii): the hull slack of E on the 3.7·10⁶-window row may exceed the cross-check's 10⁻³ | **understated — this is likely, not merely possible.** Measured E cross-leg ratio vs row width: 7.9·10⁻⁸…3.1·10⁻⁷ (width 1, ten rows), **3.06·10⁻⁶ (width 48, mine)**, 1.95–2.48·10⁻⁴ (width 1 000), 6.24·10⁻⁴ (width 10 000). The planned rows are 115 713 / 722 945 / 3 671 559 wide — 12× to 367× the widest probe, and the ratio has risen monotonically with width at every point measured. §4 step (c) as written ("must exit 0, else stop") therefore collides with §4 risk (ii) ("record the ratio rather than gate") | **FIX F-2** |
| E9 | residual risk (iii): the honest label is SPEC §3.7's; never "fully machine-checked" | correct, and required | **OK** |

---

## 6. What the replacement actually buys (stated so the phase-3 label is exact)

Not a review finding — a fact the phase-3 report should carry, because the plan's §1.5 does not spell it out.

Today `hLaneA` displays the *conclusion* "no zero of `H_{93/500}` anywhere in x ≥ 5 000 000 194 859, y₀ ≤ y,
y² ≤ 157/250". After the replacement:

* the window range **N ∈ [630 783, 5 140 999]** — i.e. x from 5.0·10¹² up to x_{N₁} ≈ **3.32·10¹⁴** — stops being a
  displayed nonvanishing claim. What is displayed there is `AsymEnclOK`, a *floor enclosure* (‖g‖ ≥ (T−E)/K on each
  window), and the step from those floors to nonvanishing on the whole range is the kernel-checked coverage
  argument (C-A3, C-A4, C-A5 + L-A1 + L-A2). That is the real gain.
* what remains a displayed nonvanishing *conclusion* is `TailOK`: N(x) ≥ 5 141 000, i.e. **x ≳ 3.32·10¹⁴**.
* one asymmetry worth recording rather than glossing: `TailOK`'s y-band is [y₀, yA] with yA = 0.7924646, which is
  **1.5·10⁻⁷ wider** than `hLaneA`'s y ≤ √(157/250) = 0.79246451… So `TailOK` is not literally a sub-statement of
  `hLaneA`; it is a vastly smaller x-region with a hair-wider y-band. Both directions are covered — the glue lemma
  derives y ≤ yA from y² ≤ 157/250 — but the label should say "the tail region N ≥ N₁, y ∈ [y₀, yA]", not "part of
  what `hLaneA` said".
  [DATED CORRECTION 2026-09-09 22:25 IST, phase-3(d) audit (AUDIT-3d.md A-1).] "1.5·10⁻⁷ wider" above is the gap in the
  SQUARES (yA² − 157/250 = 3556329/(25·10¹²) = 1.4225·10⁻⁷). The gap in y itself is yA − √(157/250) = 8.975·10⁻⁸ ≈
  9.0·10⁻⁸. The bullet's point — that `TailOK`'s y-band is a hair WIDER than the conclusion's, so `TailOK` is not
  literally a sub-statement of `hLaneA` — is unaffected.
* C-A6 (the tail row's Σ < 2K) is kernel-checked but **not consumed** by `cert_of_checkAsym` (§1, A9). It is
  recorded evidence for Lemma T's prose discharge, exactly as SPEC §5.1 designs it. The label must not imply the
  kernel checked the tail *reduction*.

---

## 7. Findings — six, none blocking, each with its fix

**F-1 — `names-check.lean` is cited but does not exist. (documentation / reproducibility)**
PLAN §1.4 ("`#check` in `names-check.lean` and `grep`") and §3.6 ("The names check `names-check.lean` (38
`#check`s): 15.5 s wall") both cite a file that is absent from `results/` and from the Lean tree
(`find … -name 'names-check*'` returns nothing). The underlying claim is TRUE — I verified all twelve Mathlib names
plus the two cast lemmas and the two norm lemmas at the plan's own `file:line`, none deprecated (Table B).
**Fix:** write `results/d1-m2a/lane-a/names-check.lean` (the 38 `#check`s) with a dated
`names-check.log`, *or* delete both sentences and cite the `sed`/`grep` evidence and the manifest rev instead.
Do not leave the citation pointing at nothing.

**F-2 — §4 step (c)'s "must exit 0" contradicts §4 residual risk (ii); decide it before the run. (phase-3 recipe)**
`crosscheck_lane_a.py` exits 1 whenever two legs' E upper bounds differ by more than `--etol` (default 10⁻³). The
measured cross-leg E ratio grows monotonically with row width — 3.1·10⁻⁷ (1 window) → 3.06·10⁻⁶ (48) → 2.5·10⁻⁴
(1 000) → 6.2·10⁻⁴ (10 000) — and the planned rows are 115 713, 722 945 and 3 671 559 windows wide. The gate will
very likely trip on the two wide rows for an entirely benign reason (Arb's ball hull slack, Arb always the larger),
and §4 as written then says "stop".
**Fix, to be written into §3.5 and §4(c) before phase 3 launches:**
"`python3 crosscheck_lane_a.py .` must exit 0. If it exits 1 **only** on the E max/min ratio of a wide row — i.e.
`T_lo` still agrees to ≲10⁻⁷⁰, the tail's Q₁…Q₄ still agree, and `ok = True` on both legs — that is hull slack, not
a producer disagreement: record the ratio and the larger leg in the run report, re-run with `--etol` set just above
the observed ratio, and note the widened tolerance in the transcript's `producer` block. Any `T_lo` or `Q_i`
disagreement, or an `ok` mismatch, remains a stop-the-line."
This costs the soundness argument nothing: each leg carries its own E in its own literal and its own theorem
(D-R3), and the gate that matters — E < T *per leg* — is already inside each leg's `ok`.

**F-3 — a failed row cannot stop `run_leg.sh`, and `--resume` makes it permanent. (phase-3 driver robustness)**
`run_rows` records a per-row exception or `ok = False` into the batch file and into `STATUS.json.errors`, then
returns **exit 0** (there is no `sys.exit` in `run_rows` on either leg). So `run_leg.sh`'s
`|| { echo "== $LEG rows FAILED"; exit 3; }` never fires and the leg proceeds to `tail` and `assemble`. And
`--resume` skips any row whose file merely *exists* (`p9_mp.py:349`, `p9_arb.py:262`), including one that recorded
an exception — so re-launching after a kill keeps the bad row for ever.
**Fix (two lines per leg):** (a) end `run_rows` with `if errors: sys.exit(6)`; (b) change the resume test to skip
only when the record loads and `rec.get("ok") is True` (else recompute). Optionally (c) have the `tail-done`
status update *merge* into the leg's dict rather than replace it, so `windows_done/windows_total` survive into the
tail phase. Downstream is already fail-loud — `crosscheck_lane_a.py` prints "ERROR recorded" and exits 1,
`assemble` raises `KeyError` on an error record, and `decide +kernel` fails on an `E ≥ T` row — so this is
robustness, not a soundness hole.

**F-4 — §1.3's "a third of that slack" is wrong. (arithmetic prose)**
The margin under π < 3.141593 is 1 712 466.94 against SPEC §5.3's 2 263 794.68 slack of x_{N₀}: that is **0.756**
of it. The π-rounding costs 551 328.74, a quarter — not the ≈1.6·10⁶ that SPEC §5.3's cruder `4·630783²·10⁻⁶`
estimate suggested.
**Fix:** replace "it holds with a third of that slack to spare" by "it holds with three quarters of that slack to
spare — the `pi_lt_d6` rounding costs 5.5·10⁵ of the 2.26·10⁶, not the ≈1.6·10⁶ SPEC §5.3's 10⁻⁶ estimate implies".

**F-5 — two files carrying the R-1 "NOT licensed" wording are missing from the phase-3 list. (label bookkeeping)**
§1.5's claim that the short public sentence becomes licensed once Lane A lands is correct (AUDIT R-1 line 29 and
RUN-REPORT §6's dated Session-16 note both gate it on item 3). But the wording R-1 installed lives in
`rh-program/lean/README.md` (the paragraph at lines ~142–149, "…is NOT licensed yet, with or without a gloss…")
and in `results/d1-m2a/v11/GLUE-NOTES.md` (lines 101–105, plus the H2-A row of its input table at line 11 and the
"Left for the Lane A stream" section at 107–113). Neither is named in §4's phase-3 list.
**Fix:** add to phase 3(d): update `lean/README.md`'s label paragraph, `v11/GLUE-NOTES.md` (§ input table, the
honest-label block, and "Left for the Lane A stream" → DONE), `RUN-REPORT.md` §6's dated note, and copy the
changed Lean files back to `rh-program/lean/Zeta23/DBN/` as Session 16 did. The plan already names the last of
these in §1.5's module-placement paragraph; the other three are new.

**F-6 — keep §1.4's honesty about what the kernel does not use. (no change needed; do not lose the sentence)**
`cert_of_checkAsym` consumes only K ≥ 1 (one conjunct of C-A1), C-A3, C-A4 and C-A5. C-A2, C-A6 and C-A1's
yA² ≥ 1 − 2t₀ are checked by `decide +kernel` and never used by the proof. PLAN §1.4 item 2 says so; SPEC §5.1
designs it so ("the row is evidence, the reduction is displayed"). **Carry that sentence into the phase-3 report
and the audit**, so nobody reads "C-A6 is kernel-checked" as "the tail reduction is kernel-checked".

**Also noted, no action:** the glue lemma pins the first row's four integers (`⟨630783, 746495, T₀, E₀⟩` and the
membership by `simp [row2AsymMP]`), so the emitter must write the glue lemma and the literal in one step. A
mismatch fails at elaboration — loudly, never silently — so this is a coupling to remember, not a defect.

---

## 8. Files this review wrote (all under `results/d1-m2a/lane-a/`)

| file | what |
|---|---|
| `PLAN-REVIEW.md` | this report |
| `review-shapes.lean` | the planner's scratch re-namespaced `LaneAReview`, importing the built `Zeta23.DBN.Instance02`, plus the three composition tests against the real `lambda_le_point2` / `lambda_le_point2_arb` / `row2_ray_mp` and four `decide +kernel` review facts (window count, row widths, C-A5, C-A1) |
| `review-shapes.log` | its `lake env lean` run: **exit 0**, zero errors, zero warnings, 2.28 s wall, the five `#print axioms` lines |
| `review-batch/plan.json` | the reviewer's 50-window plan (2 duplicated pricing rows + 1 fresh 48-window row) |
| `review-batch/rows-{mp,arb}.log` | the two legs' runs with `/usr/bin/time -l` (RSS) |
| `review-batch/batches/{mp,arb}-row_000{0,1,2}.json` | the six per-row records |
| `review-batch/STATUS{,-mp,-arb}.json` | the polling files written by the run |
| `review-batch/crosscheck.txt` | `crosscheck_lane_a.py review-batch` → 3/3 OK, exit 0 |

Nothing was written under `~/rh-lean-work/`; the Lean tree is untouched. No `lake build` was run. At most two
heavy jobs at any moment; `caffeinate` held for the session.
