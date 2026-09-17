# Opus 5 check of the (R*) + R₀ = 73 addendum to Theorem M2's note — Session 23 item 2, Job 2

**Written 2026-09-17 (Session 23; checker, Opus 5, 1M context). Contract: `results/c2-m2/followups/ADDENDUM-BRIEF.md` Job 2, against `followups/PRICING.md` §4 and §5(e)'s Addendum line. Target of the check: the dated section "Addendum 2026-09-17 (Session 23): clause 1′ = (R*), and R₀ = 73" at the end of `results/c2-m2/separation-note.md` (lines 507–579), with its scripts `verify/rstar_table.py`, `verify/rstar_slack_scan.py`, `verify/r0_73_check.py`. Nothing outside this file was edited and nothing was committed. The author's three scripts were NOT run: every number below comes from four scripts of my own, written from the note's §3.3, §4, §6 and §7.1 text, listed in §9. The constants c_B, C_B, κ₋ and Z were recomputed here at 40 digits from their closed forms, not read from the author's output; b₁ = 8.698080741088287 was read at `verify/b1_constant_out.json`.**

---

## §0 Headline

**VERDICT: CLOSES, with two FIX-FIRST one-line edits, neither of which touches a headline, a constant, or the close.** Every load-bearing number of the addendum reproduces in my arithmetic, most of them to every digit printed. The stop condition of PRICING §5(e) does **not** fire.

| item | what it is | verdict |
|---|---|---|
| 1 | (R*) re-derived from clause 1's explicit bound fed into clause 6's slack; monotonicity in δ; worst case δ = ½ | **CLOSES** |
| 2 | the least-t table at δ = ½, the asymptotic ratio 1/(128c_B²), and the 481-vs-483 discrepancy | **CLOSES** (481 is right; referee F's 483 is an isolated slip — §3) |
| 3 | the δ-scan of the slack claim \|E₋\| ≤ 2.7δ²e^{δL/2}; the worst δ; the 2N variant | **CLOSES** (min margin 0.068116 at (50, ½); 0.068023 with 2N) |
| 4 | R₀ = 73 by check-O §12.8's 13/8 chain, and the 7/4 regression to 81.0 / −0.13339 | **CLOSES** (both reproduced exactly) |
| 5 | the DH margin −2.405 nats at (85.7, 87, 0.3085) and t_min(87, 0.3085) = 100.3 | **CLOSES** |
| 6 | the t = 10³ line, the t = 10⁴ line, and scoping (a) against CAMPAIGN.md §5 and §6 | **FIX-FIRST** (one false clause about §6's grid rows; the conclusion is right — §7) |
| 7 | "(R) ⟹ (R*) with gap ≥ 49.7 nats" | **FIX-FIRST** (the infimum is 49.6667, so "≥ 49.7" is false by 0.033 — §8) |
| 8 | the "moves / does not move" sentences, the three consumer lines, 10(g) lint, append-only byte identity | **CLOSES** (apart from the item-6 clause, which recurs once in the CAMPAIGN consumer line) |

**Which close of PRICING §5(e) applies: the *lands* branch.** PRICING's target sentence was "(R*) holds for all L ≥ 50 and δ ∈ [25/L, ½]; the theorem is silent only below t ≈ 250 at δ = 0.1". I confirm it with the constant corrected: the slack check holds at **every** δ ∈ [25/L, ½] for every L ≥ 50, with minimum margin **0.068116** in units of δ²e^{δL/2} at (L, δ) = (50, ½); and the theorem's silence at δ = 0.1 ends at **t = 239.4** (L* = 376), i.e. t ≈ 240, not 250. The *fails* branch ("(R*) holds on the stated sub-range; 21L stands elsewhere") does not fire: no sub-range is needed.

**The two FIX-FIRST edits are given verbatim in §7 and §8.** Both are single clauses inside the addendum; neither changes (R*), R₀ = 73, the table, the slack verdict, or any of the three consumer lines' substance (one of the three lines carries the item-6 clause and gets the same one-line repair).

---

## §1 Item 1 — (R*) re-derived from clause 1 and clause 6

**The derivation.** Clause 1 (§4, proved for every (t, δ, L), unconditionally) gives |E₋| ≤ 2(4t² + δ²)e^{δL}G(2tL)² with G(η)² = C_B²(1 + (c_B/2)√η)²e^{−2c_B√η}. Demanding 2(4t² + δ²)e^{δL}G(2tL)² ≤ 2.7δ²e^{δL/2}, dividing by 2δ²e^{δL} and taking logarithms with s := √(2tL) gives exactly

  2c_B s − 2log(1 + (c_B/2)s) ≥ δL/2 + log((4t² + δ²)C_B²/(1.35δ²)),

which is the addendum's display and referee F's display at `referee-F.md` §6, read at the line. I did not accept this as a rearrangement in words: my script evaluates **both sides of the original inequality** and the margin of (R*) at 84 points (t ∈ {3, 10, 85.7, 167, 10³, 10⁴, 10⁶} × L ∈ {50, 87, 376, 10³} × δ ∈ {25/L, 0.1, ½}) and checks that the two truth values agree. **0 mismatches** (`o_rstar.log` (1)). The 1.35 is 2.7/2, as the addendum says.

**Monotonicity in δ.** The left side is free of δ; the right side has δ-derivative L/2 + 2δ/(4t² + δ²) − 2/δ ≥ L/2 − 2/δ, which is ≥ 0 for δ ≥ 4/L, and 25/L ≥ 4/L. So the right side increases on [25/L, ½] and **δ = ½ is the worst case for (R*) itself** — confirmed. The author's log records "derivative ≥ 21.0 on a 1001-point grid"; my grids over the same (L, t) give minimum **21.0** exactly, attained at L = 50 where the admissible δ-range collapses to the single point δ = ½ and L/2 − 2/δ = 25 − 4 = 21 (`o_rstar.log` (2)).

**Monotonicity in t.** d/ds[2c_B s − 2log(1 + c_B s/2)] = c_B(1 + c_B s)/(1 + c_B s/2) ≥ c_B (verified algebraically), ds/dt = √(L/(2t)), and the right side's t-derivative is 8t/(4t² + δ²) ≤ 2/t; hence the margin's t-derivative is > 0 for t > 8/(c_B²L), which is **7.8287** at L = 50 and **0.39143** at L = 1000 (author: 7.83, 0.39). The "least t" is therefore a genuine threshold on that half-line.

*One edge the addendum does not mention, checked and harmless.* The monotonicity argument covers only t > 8/(c_B²L), which at L = 50 is 7.83 > 3, so t ∈ [3, 7.83) is outside it. I evaluated the margin directly there at δ = ½: −20.85 (t = 3), −20.82 (4), −20.72 (5), −20.59 (6), −20.43 (7), −20.30 (7.82) — uniformly far negative, so no admissible t hides below the threshold and the half-line description stands (`o_edge.log`). No edit is owed.

**The clause bookkeeping of A1 ("which clauses consume which").** Checked against the sources: clause 5's own hypothesis-check paragraph (note §6, and `referee-O.md` §7.4, which confirms it) lists exactly the strip, the local count and the L-hypothesis — no (R), no (R*); clause 4 likewise; clauses 2 and 3 are statements about c(λ). Clause 1's *explicit* bound is unconditional (note §4 as written); clause 1's contract form consumes (R). Clause 6 under (R*) consumes clause 1's explicit bound, clause 2's lower bound in the form c(λ)² ≥ e^{m(λ)}e^{λ/2} with m(λ) = λ/2 − 2√λ − (3/2)log λ + 2κ₋, and (7.1)'s slack. I re-derived that form of clause 2: c(λ) ≥ e^{λ/2}exp(−√λ − ¾log λ + κ₋) squares to e^{λ}exp(−2√λ − (3/2)log λ + 2κ₋) = e^{λ/2}e^{m(λ)}, and **m(25) = 0.6334526** (author 0.6335), m′(λ) = ½ − 1/√λ − 3/(2λ) = 0.24 at λ = 25 > 0. Correct as stated.

**The uniform form.** At δ = ½ the right side is L/4 + log((16t² + 1)C_B²/1.35), since (4t² + ¼)/(¼) = 16t² + 1. Correct as displayed.

**Verdict: CLOSES.**

---

## §2 Item 2(a) — the least-t table and the asymptotic ratio

Constants, computed here at 40 digits by my own quadrature of Z = ∫_{−½}^{½}e^{−1/(1−4v²)}dv and cross-checked against the record's JSON (`o_rstar.log` (0)):

| constant | this check | record (`*_out.json`) | \|diff\| |
|---|---|---|---|
| Z | 0.22199690808403971891 | 0.2219969080840397 | 6.5·10⁻¹⁸ |
| c_B = 2/√(72e) | 0.14296064749345113275 | 0.14296064749345114 | 4.6·10⁻¹⁸ |
| C_B = e²/Z | 33.284500053187363306 | 33.284500053187365 | 1.9·10⁻¹⁵ |
| κ₋ = log(√(π/2)e^{−¼}/Z) | 1.4808831774009448911 | 1.480883177400945 | 1.0·10⁻¹⁶ |

Least t under (R*) at δ = ½, by bisection under the proved t-monotonicity, 40 digits (`o_rstar.log` (4)):

| L | this check, t_min | ceiling | author | referee F |
|---|---|---|---|---|
| 50 | **166.15964** | 167 | 166.2 | 167 |
| 87 | **150.90124** | 151 | 150.9 | 151 |
| 100 | **151.15980** | 152 | 151.2 | — |
| 200 | **175.73944** | 176 | 175.7 | — |
| 376 | **239.45059** | 240 | 239.5 | 240 |
| 403 | **249.70333** | 250 | 249.7 | 250 |
| 1000 | **480.74296** | **481** | 480.7 | **483** |
| 10⁴ | **3942.6279** | 3943 | 3943 | — |

Asymptotic ratio: **1/(128c_B²) = 0.38225838** (author 0.38226; referee F 0.382); t_min/L = **0.38243356** at L = 10⁶ and **0.38226070** at L = 10⁸ (author 0.38243, 0.38226). At the row's own depth: t_min(376, 0.1) = **30.4606**, t_min(1000, 0.1) = **35.1479** (author 30.5, 35.1), and the own-δ balance t/L ≥ δ²/(32c_B²) is **0.0152903** at δ = 0.1 (author 0.0153).

**Every entry of the author's table reproduces.** Verdict on 2(a): **CLOSES**.

---

## §3 Item 2(b) — the 481-vs-483 resolution

**The least t at L = 1000, δ = ½, is 480.7; the ceiling is 481. Referee F's 483 is wrong, and it is an isolated arithmetic slip in that single entry — not a different constant, not a different equation, and not a rounding of c_B or C_B.**

The margin of (R*) at L = 1000, δ = ½ (`o_rstar.log` (5)):

| t | 480 | 480.7 | 481 | 482 | 483 | 484 |
|---|---|---|---|---|---|---|
| margin (nats) | −0.2121 | −0.01226 | +0.07335 | +0.35851 | +0.64338 | +0.92796 |

The local slope is **0.2853 nats per unit t**. For the ceiling to read 483 the least t must exceed 482, i.e. the margin must fall by **0.3585 nats at fixed t** — a large amount against the digits the referee quotes. The sensitivity sweep:

| variant | t_min(1000, ½) | ceiling |
|---|---|---|
| record constants | 480.74296 | **481** |
| c_B rounded to 0.1429 | 481.15706 | 482 |
| c_B rounded to 0.14296 | 480.74738 | 481 |
| c_B rounded to 0.143 | 480.47454 | 481 |
| c_B = 0.14298 (D2's typo) | 480.61093 | 481 |
| C_B = 33.28 | 480.74201 | 481 |
| C_B = 33.3 | 480.74622 | 481 |
| coefficient 1.35 → 1.0 (i.e. \|E₋\| ≤ 2δ²e^{δL/2}) | 481.79511 | 482 |
| coefficient 1.35 → 0.942 (i.e. clause 3's 1.884 used in place of 2.7) | 482.00473 | **483** |
| coefficient 1.35 → 1.384 (the true cap 2.768/2) | 480.65580 | 481 |
| 4t² + δ² → 4t² | 480.74296 | 481 |
| c_B = 0.1429 AND C_B = 33.3 AND coefficient 1.0, together | 482.21338 | **483** |

Two variants do reach 483 — but **neither is consistent with the referee's other four entries**, which is what settles it. Ceilings at L = 50 / 87 / 376 / 403 / 1000 under each hypothesis:

* record constants: **167 / 151 / 240 / 250 / 481** ← agrees with referee F on four, differs on the fifth
* c_B = 0.1429: 167 / 152 / 240 / 250 / 482
* coefficient 1.0: 170 / 154 / 241 / 251 / 482
* coefficient 0.942: 171 / 154 / 241 / 252 / **483**
* c_B = 0.1429 and coefficient 1.0: 170 / 154 / 241 / 252 / **483**

So no single reading of the constants or of the inequality produces referee F's table. The four agreeing entries pin the referee to the record constants and to the displayed (R*) with 1.35; under those, L = 1000 gives 480.74 and the ceiling 481. **Resolution: 481 is correct; 483 is a slip confined to that entry.** It is conservative (it overstates the least admissible height by 2.3, i.e. by 0.64 nats of margin), so nothing stated anywhere on the record with 483 becomes false — the addendum, the IV.9 rider and the Instruments row should all read **481**, as the author has written them.

**One nit in the author's own sentence about this.** A1 says the difference is "0.5 %, 0.33 nats at that slope". The margin difference between t = 483 and t = 480.74 is **0.643 nats**, not 0.33; the 0.33 comes from using the weak lower bound c_B√(L/(2t)) = 0.1458 for the slope instead of the true local slope 0.2853 (`o_edge.log`). This is a nit, not a FIX-FIRST — the larger figure only strengthens the author's conclusion that rounding cannot explain the gap. Suggested tidy, if the orchestrator is editing anyway: "0.33 nats at that slope" → "0.64 nats".

**Verdict on 2(b): CLOSES** (the discrepancy is resolved in the author's favor; the author flagged it honestly rather than smoothing it over, which is the right call).

---

## §4 Item 3 — the δ-scan of the slack claim

**The chain, re-derived here.** §7.1's proof splits W_Z = (−2δ²c² + E₋) + N_Z + O_Z and W_{Z′} = N_{Z′} + O_{Z′}, with 0 ≤ N_Z, N_{Z′} ≤ N and |O_Z|, |O_{Z′}| ≤ e^{−L}. Because both noise terms are **nonnegative**, their difference is bounded by N and not 2N — this is exactly the D8 slack the note itself flags ("using clause 1 under (R) and N ≤ 2N (D8)"), so **A2's use of one N is legitimate**, and I confirm it as an argument, not only as a number. Under (R*), |E₋| ≤ 2.7δ²e^{δL/2}, and in units of U := δ²e^{δL/2} the claim is

  M(δ, L) := 2c(δL)²/e^{δL/2} − 2.7 − N/U − 2e^{−L}/U − 1 ≥ 0,

with the **proved** lower bound 2e^{m(δL)} for the first term (clauses 2 and 3).

**N/U.** From the L-hypothesis, e^{δL/2} ≥ (log(3 + t))²δ^{−4}(2b₁C₁)², so N/U ≤ ℓ_Rδ²/(2b₁C₁L²(log(3 + t))²); with ℓ_R ≤ 1.1log(3 + t) + L, C₁ ≥ 1, and (1.1x + L)/x² decreasing in x = log(3 + t) ≥ log 6, N/U ≤ (1.1log 6 + L)δ²/(2b₁L²(log 6)²). My values: **9.30567·10⁻⁵** (L = 50), 5.262·10⁻⁵ (87), 1.197·10⁻⁵ (376), 1.116·10⁻⁵ (403), 4.485·10⁻⁶ (1000), all at δ = ½ where this term is worst. Author: "max N/U = 9.31·10⁻⁵ at L = 50". **Agrees.** The reciprocal is 1.07·10⁴, so the author's "it is ≥ 10⁴" is right, and referee F's "≥ 1740" is a weaker statement of the same slack.

**The scan.** 13 153 points: δ on 2001-point grids of [25/L, ½] plus both endpoints for L = 50, 87, 376, 403, 1000; then L = 50…1000 step 1 and 1000…10⁵ geometric, at δ ∈ {25/L, midpoint, ½} (`o_slack.log` (3)).

| quantity | this check | author |
|---|---|---|
| e^{m(25)} | 1.88410445 | 1.8841 |
| min M over the whole scan | **0.068115852** at (L, δ) = (50, ½) | 0.068116 at (50, ½) |
| M at δ = 25/L | 0.0681159 (L = 50) … 0.0682089 (L ≥ 10⁴) | "0.0682 at every L" |
| M at δ = ½, L = 87 | 698.955 | 699 |
| M at δ = ½, L = 1000 | 4.9004·10⁸⁶ | 4.9·10⁸⁶ |
| largest coefficient the chain absorbs | **2.768115852** | 2.768 |
| min M with the record's 2N | **0.068022795** at (50, ½) | 0.0680 |

**HOLDS at every point.** The claim "HOLDS on [25/L, ½] for every L ≥ 50, min margin 0.068 at (50, ½)" is **confirmed**, and so is the 2N variant: still positive at 0.0680.

**The worst δ for the slack.** Confirmed as the author states, and for the reason the author gives: 2e^{m(δL)} increases in δL and is therefore smallest at δ = 25/L (λ = 25), while N/U increases in δ and is largest at δ = ½ — but N/U ≤ 9.31·10⁻⁵ against a first term running from 3.768 upward, so the first effect dominates. At L = 87, M(25/L) − M(½) = −698.89 < 0: the 25/L end is the worse one. At L = 50 the two ends coincide (25/L = ½), which is why the global minimum sits there. So the worst δ for the slack is the **opposite end** from (R*)'s own worst case, and both hold — as A2 says.

**Sanity rows** (computed, not part of the proof): exact c(λ)²/e^{λ/2} = 1.999107, 2990.523, 2.151886·10¹¹ at λ = 25, 50, 100, against the proved e^{m(λ)} = 1.884104, 2840.105, 2.065919·10¹¹. Author: 1.9991, 2990.5, 2.15·10¹¹ / 1.8841, 2840.1, 2.07·10¹¹. **Agrees.**

**Verdict: CLOSES. The stop condition of PRICING §5(e) does not fire.**

---

## §5 Item 4 — R₀ = 73

I rebuilt clause 5's one-point check from the note's §6 text alone — the shell bound, β = 1 + 3/(2(R₀L₀ − 1)), φ_m(u₀) + ∫_{u₀}^∞φ_m, the three incomplete-gamma sums with a = 2c_B and n = 2m+1, 2m+2, 2m+3, and the three relaxations (e^{−2c_Bs₀} ≤ e^{2c_B/√R₀}e^{−2c_B√R₀L}; u₀ ≤ R₀L and s₀ ≤ √R₀L in polynomial factors; β frozen at L₀) — and did not read the author's script. The test of that reconstruction is the regression.

**Regression, the record's 7/4 chain** (`o_r0.log` (1)):

| quantity | this check | record |
|---|---|---|
| least half-integer R₀ at L₀ = 50 | **81.0** | 81.0 |
| F̃(50) at R₀ = 81 | **−0.13339478** | −0.13339478 (`lemma_G_constants_out.json`), referee O −0.133615 |
| F̃(50) at R₀ = 80.5 | +0.23703 | — (so 81.0 is least) |
| decrease from L = | 6.0732 | referee O 6.073 |
| F̃(L) at 60 / 100 / 403 / 10³ / 10⁴ | −7.4767 / −37.898 / −280.44 / −767.41 / −8165.5 | −7.48 / −37.9 / −280 / −767 / −8166 |
| R₀(L₀) at 100 / 200 / 403 / 10³ / 10⁴ | 58.5 / 48 / 43 / 40 / 38 | identical |
| asymptote (7/(8c_B))² | 37.461321 | 37.46 |

My independent reconstruction reproduces F̃(50) to all eight printed digits. That is the license for the 13/8 result below.

**The 13/8 chain (check-O §12.8, adopted by A3).** The hypothesis L/8 ≥ log log(3 + t) + log(2b₁C₁) gives e^{L/8} ≥ 2b₁C₁log(3 + t) directly, so 2C₁log(3.5 + t) ≤ 1.05e^{L/8}/b₁ in **one** use and 2C₁ ≤ e^{L/8}/b₁; the budget is 5/8 + 1 = 13/8. The 1.05 covers log(3.5 + t)/log(3 + t), which is **1.0446727** at t = 3 and decreasing (1.0147 at t = 10, 1.0010 at 10², 1.0000 at 10⁶) — author: "≤ 1.0447 at t = 3, decreasing". **Agrees.**

| quantity | this check | author |
|---|---|---|
| least half-integer R₀ at L₀ = 50 | **73.0** | 73.0 |
| F₁₃(50) at R₀ = 73 | **−0.32272321** | −0.3227 |
| F₁₃(50) at R₀ = 72.5 | **+0.06603193** | +0.066 |
| decrease from L = | **6.11312** (≤ 50) | 6.11 |
| F₁₃(L) at 60 / 100 / 403 / 10³ / 10⁴ / 10⁵ | −7.6135 / −37.822 / −278.73 / −762.49 / −8112.2 / −81712.8 | −7.61 / −37.8 / −278.7 / −762.5 / −8112 / −81713 |
| R₀(L₀) at 100 / 200 / 403 / 10³ / 10⁴ | **51.5 / 42 / 37.5 / 34.5 / 33** | identical |
| asymptote (13/(16c_B))² | **32.300833** | 32.30 (check-O: 32.30) |

**R₀ = 73 is confirmed**, with the one-point check valid (F₁₃(50) ≤ 0 and 6.113 ≤ 50) and 72.5 excluded.

**The downstream statements of A3, checked.** ℓ_R = log(4 + t + R₀L) is smaller at 73 than at 81 — 8.2044 against 8.3082 at (t, L) = (3, 50), 13.8445 against 13.8476 at (10⁶, 403) — so clause 4's bound and (7.1) only improve, as A3 says. The auxiliary R₀L ≤ e^L − 1 of §7.1 holds (3650 ≤ e⁵⁰ − 1). The DH control's unverified window R₀L* at L* = 86.907 is **6344.2** (was 7039.5), i.e. "≈ 6.3·10³ (was ≈ 7·10³)" — correct. The direction of the supersession is right: the window hypothesis is "on-line within R₀L of t", so a *smaller* R₀ is a *weaker* hypothesis, and every statement made with 81 stays true — A3's parenthetical "(a configuration on-line within 81L of t is on-line within 73L)" states this correctly. A3's quotation of the second corrections section item (g) is verbatim against `separation-note.md` line 495.

*Wording nit, no edit required.* A3 writes "the same Laurent polynomials P₂, P₃"; §6 defines a single Laurent polynomial P (check-O §12.7 and referee-O corrected "polynomial" to "Laurent polynomial", and (log P)′ ≤ 5/L survives). The plural is harmless bookkeeping for the two shells m = 2, 3.

**Verdict: CLOSES.**

---

## §6 Item 5 — the DH control

| quantity | this check | author / referee F |
|---|---|---|
| (R*) margin at (t, L, δ) = (85.7, 87, 0.3085) | **−2.4051088 nats** | −2.405 (author); −2.4 (referee F, `referee-F.md` line 89) |
| (R*) margin at the log's values (85.6993485, 86.907, 0.3085172) | **−2.409217** | −2.409 |
| t_min(87, 0.3085) | **100.327** | 100.3 |
| uniform (δ = ½) margin at (85.7, 87) | **−9.7695916** | −9.77 |
| t_min(87, ½) | 150.901 | 150.9 |

**The DH control stays outside the hypotheses under (R*).** This is the point PRICING §4 and referee F both make, and it is confirmed: (R*) fails at DH by 2.4 nats where t ≥ 21L failed by a factor 21, so MAJOR-2's status (mechanism and datum confirmed on explicit finite configurations; NOT an instance of the theorem's hypotheses) is unchanged, and the window hypothesis stays unverified there. **CLOSES.**

---

## §7 Item 6 — the t = 10³ line and the scoping against CAMPAIGN.md

**The t = 10³ / 10⁴ lines** (`o_rstar.log` (7)); the largest L at which (R*) holds at fixed t, by bisection on the upper crossing (the margin is strictly concave in L: its L-derivative c_B t(1 + c_B s)/(s(1 + c_B s/2)) − δ/2 is strictly decreasing, which I verified algebraically, so the admissible set is a single interval):

| (t, δ) | this check, L_max | author |
|---|---|---|
| (10³, ½) | **2341.2608** | 2341 |
| (10³, 0.05) | **258 176.65** | 2.58·10⁵ |
| (10³, 0.1) | **63 794.516** | 6.38·10⁴ |
| (10³, 0.25) | **9876.2223** | 9876 |
| (10⁴, ½) | **25 817.665** | 2.58·10⁴ |
| 21L form: t = 10³ | L ≤ 47.619 | 47.6 |
| 21L form: t = 10⁴ | L ≤ 476.19 | 476 |

And t_min(376, ½) = 239.45 < 10³, so L* = 375.8 at (δ, t) = (0.1, 10³) is inside — the check the brief asks for. **All confirmed.**

**CAMPAIGN.md §5, read at the page.** The six t = 10³ record rows are exactly (δ, C₁, L*) = (0.05, 1, 862.48), (0.05, 2.4·10⁹, 2590.38), (0.10, 1, 375.79), (0.10, 2.4·10⁹, 1239.74), (0.25, 1, 120.99), (0.25, 2.4·10⁹, 466.57), all flagged `inside` = False. My (R*) margins at their own δ: **316.95, 547.94, 194.28, 352.25, 93.665, 184.69** (author: 317, 548, 194, 352, 93.7, 185). In the uniform δ = ½ form: 127.50, **−30.296**, 122.35, 107.52, 79.93, 127.76 — so all but the (0.05, 2.4·10⁹, L* = 2590.38) row, whose L* exceeds 2341. **Exactly as A4 states.** At t = 10⁴ the three rows flagged False are (0.05, 1, 885.46), (0.05, 2.4·10⁹, 2613.36), (0.10, 2.4·10⁹, 1251.23) — I confirm these are the three False rows at that height in §5 — and their δ = ½ margins are 942.54, 1373.36, 1077.83, so "margins ≥ 942 at δ = ½" is right.

**CAMPAIGN.md §6, read at the page — this is the FIX-FIRST.** The grid is at δ = 0.1 with L ∈ {4, 6, 8, …, 30, 40, 50, …, 120} at all four heights (max L = 120 at every height, as A4 says). The addendum's sentence reads:

> §6's grid rows (L ≤ 120 at every height) do NOT come inside: **(R*) holds at all of them**, but at t = 10³ every grid row has L < L*(δ, 10³) …

The clause in bold is false, twice over.

1. **Out of range.** (R*) is stated in A1 for δ ∈ [25/L, ½]. At δ = 0.1 that needs L ≥ 250; every §6 grid row has L ≤ 120, so no grid row lies in the range on which the addendum states (R*) at all. (Equivalently δL ≤ 12 < 25 = λ₀, so clauses 2 and 3 are not available there either.)
2. **False even as a formal evaluation.** At t = 10³, δ = 0.1, the margin of (R*) is **−5.14465 at L = 4**; the lower crossing is at L = **5.9389**, so the L = 4 row fails and the L = 6 row passes with margin +0.1477 (`o_grid.log`). At t = 10⁴, 10⁵ and 10⁶ the margin is positive on the whole grid (minimum +43.44, +211.46, +757.55 at L = 4).

The **conclusion** the sentence supports — that §6's grid rows do not come inside — is right, and so is the §6 header wording it defends. Only the parenthetical justification is wrong. The same clause recurs, in shorter form, in the CAMPAIGN consumer line ("§6's grid rows stay below the hypotheses through L < L*(δ, t) **alone**").

**FIX-FIRST edit 1 (A4, the `campaign/CAMPAIGN.md` bullet).** Replace

    §6's grid rows (L ≤ 120 at every height) do NOT come inside: (R*) holds at all of them, but at t = 10³ every grid row has L < L*(δ, 10³)

by

    §6's grid rows (L ≤ 120 at every height) do NOT come inside: at δ = 0.1 they lie outside (R*)'s stated range δ ∈ [25/L, ½] altogether (which needs L ≥ 250), and evaluated formally the inequality still fails at the L = 4 row at t = 10³ (margin −5.14; it holds from L = 5.94 on, and on the whole grid at t ≥ 10⁴) — and in any case every grid row at t = 10³ has L < L*(δ, 10³)

**FIX-FIRST edit 2 (A4, inside the dated line written out for the orchestrator to add to `CAMPAIGN.md` §1).** Replace

    §6's grid rows stay below the hypotheses through L < L*(δ, t) alone.

by

    §6's grid rows stay below the hypotheses through L < L*(δ, t) (and at t = 10³, L = 4, through the reflection condition as well).

With those two clauses repaired, item 6 **CLOSES**.

*Nit, no edit required.* A4 says "at the row's own δ the threshold is t ≈ 31"; my value is t_min(375.79, 0.1) = **30.462**, which A1 itself already prints as 30.5. "≈ 31" over-rounds in the safe direction (it claims silence over a marginally wider range) but does not match the author's own digit; "≈ 30" would be the number.

---

## §8 Item 7 — "(R) ⟹ (R*) with gap ≥ 49.7 nats"

The algebra is right. RHS(R) − RHS(R*) = L + 2√(δL) + (3/2)log(δL) − 2κ₋ + log((4t² + δ²)C_B²/δ²) − δL/2 − log((4t² + δ²)C_B²/(1.35δ²)) = L − δL/2 + 2√(δL) + (3/2)log(δL) − 2κ₋ + log 1.35, which is the addendum's display; the (4t² + δ²)C_B² factors cancel exactly, so the gap is free of t.

**The number is not right.** The minimum over L ≥ 50, δ ∈ [25/L, ½] is attained at (L, δ) = (50, ½) — the only admissible δ at L = 50 — because ∂/∂L = 1 − δ/2 + √(δ/L) + 3/(2L) > 0. There

  50 − 12.5 + 2√25 + 1.5log25 − 2(1.4808831774) + log 1.35 = **49.666652**.

So "**which is ≥ 49.7**" is false by 0.033 nats. My 2001-point sweep over L ∈ {50, 60, 87, 100, 200, 376, 403, 10³, 10⁴, 10⁵} confirms the minimum at 49.666652 (`o_rstar.log` (6)).

Nothing downstream moves: the gap is positive with room, so **t ≥ 21L ⟹ (R′) ⟹ (R) ⟹ (R*)** stands, and so does the rest of the paragraph — the (R*) margin at t = 21L, δ = ½ is **50.383745** nats at L = 50 and **1561.3137** at L = 1000 (author: 50.4, 1561). But a stated lower bound that the quantity does not satisfy is exactly the kind of thing this check exists to catch.

**FIX-FIRST edit 3 (A1, the "(R) implies (R*)" paragraph).** Replace

    which is ≥ 49.7 on δ ∈ [25/L, ½], L ≥ 50 (log (f));

by

    which is ≥ 49.66 on δ ∈ [25/L, ½], L ≥ 50, its minimum 49.6667 being attained at (L, δ) = (50, ½) — the only admissible δ at L = 50 (log (f));

With that, item 7 **CLOSES**.

---

## §9 Item 8 — "moves / does not move", the consumer lines, lint, byte identity

**Append-only and byte identity — verified, not taken on trust.** `git show 9de589d:./results/c2-m2/separation-note.md` (the commit before the addendum) is 503 lines and hashes **ac019b7868950f0c05f0c84742c2aefd9bfab7df98bb84718e3876297bb0f3eb**; `head -503` of the current note hashes identically and `diff` of the two is empty. Line 504 is blank, 505 is `---`, 506 blank, 507 the addendum heading. So the append is genuinely append-only and the author's "ac019b78…" is right. The nine script/log/JSON hashes in `verify/hashes-addendum.txt` all recompute correctly against the files on disk.

**10(g) lint (KICKSTART item 10(g), line 74): "clearly / obviously / easy to see / well known".** Zero hits in lines 505–579, and zero hits for "evidently" and "trivially" as well. The constants' dependency chain is stated in A1 and A3 and introduces no cycle (c_B, C_B, κ₋, b₁ are all upstream of (R*) and of R₀, and R₀ = 73 is not used in deriving (R*)). The slack ledger is A2's table. **Clean.**

**U.S. English.** Zero hits for the usual British forms across the addendum. **Clean.**

**The "moves / does not move" sentences, each against the file it names:**

| A4 claim | checked against | verdict |
|---|---|---|
| "No headline number moves" | §13's close; the separation bound δ²e^{δL/2} ≥ 1 is untouched, and both changes weaken hypotheses | correct |
| §7.1's hypothesis list gains clause 1′ and R₀ = 73 | note §7.1 lines 323–325 | correct |
| §13's close would read "on-line within 73L of t … log(17.4C₁) … and (R*) — in particular for t ≥ 21L" | §13 line 406 reads "within 81L" and "log(17.3C₁)"; the second corrections section item (b) (line 495) already re-reads 17.3 as **17.4** at b₁ = 8.70 | correct, and correctly cites the correction rather than the stale body figure |
| D3's "silence below ≈ 21L*, at δ = 0.1 below ≈ 8·10³" becomes "below t ≈ 240" | §4's D3 paragraph, verbatim; 21 × 376 = 7896 ≈ 8·10³; t_min(375.79, ½) = **239.371** | correct (the own-δ figure is 30.5, not 31 — §7's nit) |
| "The DH control's status is unchanged" | §6 above; MAJOR-2 as corrected 19:39 IST | correct |
| the flag `inside_hypotheses` = (L ≥ L*) and (t ≥ 21L) "(§0 line 11)" | `campaign/CAMPAIGN.md` line 11 is the "Derived bandwidths" bullet, which carries exactly that definition | correct to the line |
| §5's six t = 10³ rows and the three t = 10⁴ False rows | `CAMPAIGN.md` §5 table | correct (§7 above) |
| §6's grid rows | `CAMPAIGN.md` §6 | **one false clause — FIX-FIRST edit 1** |
| the §6 headers' sentence "rows with L above 47.6 are below the theorem's hypotheses" | `CAMPAIGN.md` line 155, verbatim | quoted correctly |
| IV.9's "subject to t ≥ 21L*, with the window 81L* around t on-line except for the orbit" | `BARRIER-ZOO.md` line 149 — found verbatim | quoted correctly |
| IV.9's "the PROVED reflection condition t ≥ 21L* = 1825 fails there by the factor 21" | `BARRIER-ZOO.md` line 149 — found verbatim; 21 × 86.907 = 1825.0 | quoted correctly |
| C2 Instruments row "Out-window radius R₀ (clause 5, uniform over depth ½)" | `directions/C2-rigidity-conservation.md` line 101, currently "81 proved (73 available; asymptote 37.5) \| …§6, §12.8 \| 2026-09-16" | the row exists, the four-column shape matches, and the proposed replacement value "73 proved (all L ≥ 50; asymptote 32.3); 81 superseded" is what my §5 proves |
| the proposed new Instruments row "(R*) least admissible height t(L)": 167 / 151 / 240 / 250 / 481, t/L → 0.382, DH outside by 2.4 nats | §2, §3, §6 above | every number correct |
| "PRICING §4's two numbers": "t ≈ 250" is 240 at L* = 376; "≈ 2.5·10³" is 2341 at t = 10³ | §2, §7 above | correct |

**The three consumer lines** are therefore safe to write as drafted, with the one repair of FIX-FIRST edit 2 inside the CAMPAIGN line. The IV.9 rider and the two Instruments rows need no change.

**The author's honesty note, checked.** Its two recorded-not-resolved items are exactly the two things a checker would have flagged: the 483 (resolved here in the author's favor, §3) and the brief's phrase about "the t = 10³ rows above L = 47" being true of §5 and false of §6 (correct; and §7 above sharpens why). The one-N accounting is declared with its D8 license and the 2N value is given. I found no undeclared inference.

**Verdict: CLOSES, subject to FIX-FIRST edits 1 and 2.**

---

## §10 What I checked, and what I did not

**Checked, in my own arithmetic:** the derivation of (R*) from clause 1's explicit bound and the 2.7δ²e^{δL/2} target, as an inequality and not only as a rearrangement; the δ- and t-monotonicity, including the edge t ∈ [3, 8/(c_B²L)); the full least-t table and the asymptotic ratio at L = 10⁶ and 10⁸; the 481/483 question under eleven variants of the constants and three of the inequality; the whole slack chain including the one-N argument, the N/U bound and its worst-case reasoning, on 13 153 (δ, L) points; clause 5's one-point check rebuilt from §6's text, regressed against the record's R₀ = 81 / F̃(50) = −0.13339478 and then run at 13/8; the DH margins at both the referee's and the log's coordinates; the t = 10³ and t = 10⁴ lines and the concavity in L that makes them intervals; every CAMPAIGN §5 row and the whole §6 grid; the quoted phrases in `BARRIER-ZOO.md` and `CAMPAIGN.md` at their lines; the byte identity of the first 503 lines against `git show`; the nine file hashes; the 10(g) and U.S.-English lints.

**Not checked, deliberately:** I did not run `rstar_table.py`, `rstar_slack_scan.py` or `r0_73_check.py`, and did not read their source before writing mine (I read their logs and JSON only to compare numbers afterward). I did not re-prove clauses 2, 3, 4, 5 or Lemma G — they are the record, dual-checked and twice refereed, and I used their statements; in particular b₁ = 8.698080741 is taken from `verify/b1_constant_out.json` rather than re-derived, and κ₊, ‖B‴‖₁ are not used here. I did not verify the window hypothesis for DH (it remains unverified, as the note says), and I did not recompute referee F's 70 or referee O's 57 — both are fixed-(t, C₁) values that item (g) already records as non-uniform. I did not check the Lean side (M4 is a separate unit) and did not re-examine the two re-run blocks that precede the addendum.

---

## §11 Traceability — every number above to the script that produced it

All four scripts are mine, written for this check, and live in the session scratchpad at
`/private/tmp/claude-501/-Users-jaytyagi-…-riemann/adce32e7-65bc-4d2c-8cd1-cc33a29d9028/scratchpad/ocheck/`
(they are scratch by the brief's instruction "scratch under the session scratchpad; edit nothing else"). Each writes a `.log` beside itself.

| numbers | script, section of its log |
|---|---|
| Z, c_B, C_B, κ₋ at 40 digits and their agreement with the record's JSON | `o_rstar.py` → `o_rstar.log` (0) |
| the 84-point identity check that (R*) **is** the inequality \|E₋\| ≤ 2.7δ²e^{δL/2} | `o_rstar.log` (1) |
| the δ-derivative minimum 21.0; the worst case δ = ½ | `o_rstar.log` (2) |
| 8/(c_B²L) = 7.8287 (L = 50), 0.39143 (L = 1000) | `o_rstar.log` (3) |
| t_min(L, ½) = 166.15964, 150.90124, 151.15980, 175.73944, 239.45059, 249.70333, 480.74296, 3942.6279; 1/(128c_B²) = 0.38225838; t_min/L at 10⁶ and 10⁸; t_min(376, 0.1) = 30.4606; t_min(1000, 0.1) = 35.1479; δ²/(32c_B²) = 0.0152903 | `o_rstar.log` (4) |
| the margin table at L = 1000 near t = 481; the slope 0.2853; the eleven-variant sensitivity sweep; the five-row ceiling comparison | `o_rstar.log` (5) |
| RHS(R) − RHS(R*) minimum 49.666652 at (50, ½); the (R*) margins at t = 21L (50.383745, 1561.3137) | `o_rstar.log` (6) |
| L_max = 2341.2608, 258176.65, 63794.516, 9876.2223, 25817.665; the 21L comparisons | `o_rstar.log` (7) |
| the DH margins −2.4051088 and −2.409217; t_min(87, 0.3085) = 100.327; the uniform −9.7695916 | `o_rstar.log` (8) |
| the CAMPAIGN §5 margins at t = 10³ and 10⁴, own-δ and δ = ½ | `o_rstar.log` (9) |
| t_min(375.79, ½) = 239.371 and t_min(375.79, 0.1) = 30.4623 | `o_rstar.log` (10) |
| m(25) = 0.6334526, e^{m(25)} = 1.88410445; the N/U table; min M = 0.068115852; the δ = 25/L and δ = ½ rows; the worst-δ comparison at L = 87; min M with 2N = 0.068022795; the cap 2.768115852; the exact-c sanity rows | `o_slack.py` → `o_slack.log` (0)–(8) |
| the 7/4 regression (R₀ = 81.0, F̃(50) = −0.13339478, the F̃ row, the R₀(L₀) table, asymptote 37.461321); the log-ratio 1.0446727; the 13/8 results (R₀ = 73.0, F₁₃(50) = −0.32272321, +0.06603193 at 72.5, decrease from 6.11312, the F₁₃ row, the table 51.5/42/37.5/34.5/33, asymptote 32.300833); ℓ_R at 73 vs 81; R₀L* = 6344.2 vs 7039.5 | `o_r0.py` → `o_r0.log` (0)–(3) |
| the (R*) margins on CAMPAIGN §6's grid rows at all four heights; the lower crossing L = 5.9389 at (10³, 0.1) | `o_grid.py` → `o_grid.log` |
| the t ∈ [3, 7.83) edge evaluation; the 0.643-vs-0.33 slope point | `o_edge.py` → `o_edge.log` |
| `ac019b78…`, the 503-line diff, the nine file hashes, the lints, the verbatim phrase checks | shell, quoted inline in §9 |
