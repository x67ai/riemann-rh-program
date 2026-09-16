# check-O.md — M6 rung 1, the Opus 5 DUAL CHECK (Job 2; standing orders 5 and 7)

**Written 2026-09-17 (Session 22/23 stream 2, Job 2, Opus 5; machine clock via `date`). Contract: the "Job 2" paragraph of `results/c2-m6/BRIEF.md` with `results/c2-m2/followups/PRICING.md` §3 behind it, both read in full; `results/c2-m6/m6-rung1-note.md` read end to end (§0–§12), `zoo-IV19-proposed.md`, `SHARED.md`, `hashes.txt`, `verify/` (source, twelve scripts, `logs/`, `out/`). Every number below is printed by my OWN implementation, written from the mathematical definitions and not from `verify/` — an independent sieve, an independent A(v) quadrature, an independent B̂, an independent archimedean integral, an independent Λ_DH recursion, an independent zero side; scripts in the session scratchpad (`own/core.py`, `zeta_prime.py`, `arch.py`, `pole.py`, `dh_coeff.py`, `dh_count.py`, `rec_corr.py`, `fastB.py`, `zsides.py`, `sup_E.py`). The Lean tree was read only; nothing was committed by this job. Standing order 4: nothing here is a statement about RH.**

## HEADLINE

**The rung's COMPUTATIONS CLOSE and the RECORD CORRECTION IS CONFIRMED — and statement (E) is a published theorem, in a strictly stronger (effective) form, so the zoo entry may not be inserted as drafted.**

Every control value in the note was reproduced from an independent implementation, most of them to the last printed digit: ζ at (85.7, 10) matches the zero side to **3.6·10⁻¹⁷** on my own numbers (the note's 2.3·10⁻¹⁶; budget 2.0·10⁻¹⁴), DH fires coefficient-side at **W = −0.269812074198289** (the note's −0.269812074198287), the exact Kronecker supremum at L = 10 is **1.422174** to seven digits, the cost line's class boundaries land at **L = 28.37 / 31.63** against the note's 28.35 / 31.61 on rates I re-measured on this machine. The record correction of §5.3 is real, independently reproduced zero for zero, and its blast radius is **provably confined to the W_{Z′} and W_Z columns of the DH control tables**: every separation, ratio and "fires" column in the record is a difference in which the on-line part cancels identically, so **no record headline moves** (the ×6.24 ratio recomputes to 6.2373 against the record's 6.2375; the 26 off-line orbits are refined on f_DH itself and are untouched; the campaign's ζ-side closes never see a DH zero).

Two FIX-FIRST findings, one of them structural:

* **(E) is classical.** Turán, *Acta Sci. Math. Szeged* 21 (1960) 311–318, Lemma p. 313 gives the window-uniform Kronecker statement for the frequencies {log p} with an EFFECTIVE window length; Weber, *Uniform Distribution Theory* 4 (2009) 97–116 (arXiv:0806.3990), Theorem 1 with (3.17)–(3.18), states it for a general Dirichlet polynomial, explicitly uniform in the window position and effective. The note's own Remark (ii) concedes its H₀ "is not effective in any useful sense". The note's §6 proof is correct and is a correct independent proof — of a weaker version of a 1960 theorem. The 10(n) "nearest published object" line (Bohr's almost periodicity) understates the distance by sixty-six years.
* **The note's DH "term count" is a floating-point artifact.** "15 346 coefficients" at L = 10 (§0.2, §2.2, §5.1, §9, §10, and three times in the zoo draft) is the number of n ≤ 22 026 whose Λ_DH survives an `!= 0.0` test in f64. The number of n ≤ 22 026 with Λ_DH(n) ≠ 0 is **8 562**, stable under recomputation at 30, 60 and 100 digits. The note's own mpmath diagnostic printed 15 442 by the same test at higher precision and the note never reconciled the two. No value moves; every count does.

Verdict per deliverable: **(1) CLOSES · (2) CLOSES with a FIX-FIRST on the term count · (3) CLOSES (correction CONFIRMED, blast radius confined) · (4) proof CLOSES, LABELS FIX-FIRST · (5) CLOSES · (6) FIX-FIRST (four wording corrections) · (7) CLOSES with two exceptions · (8) FIX-FIRST · (9) zoo IV.19: FIX-FIRST, six amendments before insertion.**

---

## §1 Deliverable 1 — the ζ positive control at (85.7, 10), from my own implementation: **CLOSES**

**What I built, and why it is independent.** From the §0.1 normalization only: B(v) = Z⁻¹exp(−1/(1 − 4v²)); A(v) = ∫B′(w)B′(w − v)dw by a 16 384-node trapezoid over [−½, ½] evaluated **per term** (no table, no Hermite interpolation — the note's route), checked against `mpmath.quad` at 30 digits; B̂ by the periodic trapezoid (2 048 nodes at 40 digits), checked against subdivided `mpmath.quad`; Λ(n) by an smallest-prime-factor sieve in Python; the phase cos(t log n) in `mpmath` at 30 digits (no double-double); ARCH by (1/(2πL³))∫η²B̂(η)²·bracket(t + η/L)dη with **`scipy.special.digamma` on complex argument** (the note used `mpmath.digamma`), spot-checked against mpmath at three points to 3·10⁻¹⁶; the pole terms by ĝ(z) = h_f(z)·conj(h_f(z̄)) at 35 digits; the zero side from `mpmath.zetazero` at **40** digits (the note used 30), 112 zeros to γ = 256.38, reflections −γ included.

| quantity | **mine** | note / `out/` | agreement |
|---|---|---|---|
| Z = ∫exp(−1/(1−4v²))dv | 0.2219969080840397189115245 | 0.2219969080840397 | exact |
| A(0) = ‖B′‖₂² | 16.621965346933933 | 16.62196534693389 | 4·10⁻¹⁵ |
| A(0.1234567) / A(0.5) / A(0.87654321) | 9.848192099927974 / −5.209362663929435 / −0.610135483531584 | 9.848192099927926 / −5.209362663929407 / −0.610135483531583 | ≤ 5·10⁻¹⁴ |
| terms (n ≤ 22 026, Λ ≠ 0) | 2 532 = 2 466 primes + 66 prime powers | 2 532 = 2 466 + 66 | exact |
| ℓ¹ = Σ|w_n| | 1.4568633200341718 | 1.456863 | exact to printed |
| **P_X(g_t)** | **+0.039608507012439213221** | +0.039608507012439246 (`P_dd`) | 3.3·10⁻¹⁷ |
| my float64 phase minus my 30-digit phase | 8.743·10⁻¹⁶ | 8.7·10⁻¹⁶ (`P_dd_minus_P_double`) | independent confirmation of the budget line |
| **ARCH_ζ** | **+0.04343137352211606** | +0.04343137352211607 | 1·10⁻¹⁷ |
| ∫η²B̂²dη (Parseval vs 2πA(0)) | 104.43888844430352 vs 104.43888844430353 | 104.438888444304 vs …303 | exact |
| ĝ(i/2) + ĝ(−i/2) | −1.469578717·10⁻¹⁵ | −1.470·10⁻¹⁵ | exact to printed |
| **W_rhs = pole + ARCH − P** | **+0.0038228665096753772** | +0.003822866509676 | — |
| **W_zero (112 zeros, 40 digits, + reflections)** | **+0.0038228665096753416** | +0.0038228665096754 | 6·10⁻¹⁷ |
| **W_rhs − W_zero** | **+3.56·10⁻¹⁷** | +2.3·10⁻¹⁶ | both ≪ budget |

**My error budget at (85.7, 10)** (independent of the note's): Λ and the sieve exact (integers); phase 30-digit ⇒ ≤ 10⁻²⁸; A(v) per-term quadrature, worst relative deviation from mpmath 3.6·10⁻¹⁶ × ℓ¹ = **5·10⁻¹⁶**; ARCH quadrature, h → h/2 changes 6.9·10⁻¹⁸, range 2000 → 1500 changes 0, node count doubled changes 0, and the digamma's own 10⁻¹⁶ enters as (∫Â)·10⁻¹⁶/(2πL³) = **7·10⁻¹⁷**; pole terms computed, 10⁻¹⁵ in size and correct to ~10⁻¹⁸; zero side truncation |γ − t| > 140 contributes 3.6·10⁻²², reflections 3.4·10⁻¹⁹ (included), zero precision 0 at 40 digits; double-rounding floor of the assembled value 10⁻¹⁷. **Budget ≈ 7·10⁻¹⁶; observed 3.6·10⁻¹⁷.** The note's budget of 2.0·10⁻¹⁴ is larger only because its A-table interpolation line (8·10⁻¹⁵) and its 10⁻¹⁴ assembly floor are larger than mine; both budgets are honest and both are met by two orders or better. **The contract's 10⁻⁴ is met by twelve orders. Stop condition 1 does not fire.**

**Two further points checked and passed, not required by my contract.** (85.7, 20): W_rhs = +0.000866034231848014 against my own W_zero = +0.000866034231848011, residual **+3.1·10⁻¹⁸** (the note: +6.9·10⁻¹⁷); the prime side there is from the note's `twisted_sum.rs` rebuilt by me (`rustc -O -C target-cpu=native`, rustc 1.98.1), the archimedean term, the pole term and the zero side mine. (10⁶, 10): my own 2 532-term sum at 35 digits gives P = −0.052207475557697350 and W_rhs = **+0.25129928439258918** against the campaign's N_Z = 0.25129928436203747, residual **+3.055·10⁻¹¹** — the note's +3.1·10⁻¹¹ to three digits, inside its 1.9·10⁻⁸ zero-precision budget.

**Verdict: CLOSES.** The pipeline is certified on the case known to hold, by a second implementation that shares no code with the first.

---

## §2 Deliverable 2 — the DH negative control, coefficient side, at (85.7, 10): **CLOSES; one FIX-FIRST**

**The four witnesses first (BRIEF rule 3), reproduced before anything else**, from my own recursion Λ_DH(n) = a(n)log n − Σ_{d|n, 1<d<n}a(n/d)Λ_DH(d) at 30 digits with a(n) ∈ {1, κ, −κ, −1, 0} by n mod 5, κ = (√(10 − 2√5) − 2)/(√5 − 1) = 0.2840790438404122960282918:

| n | mine | closed form (`m0-axiom-note.md` §6.1) | difference |
|---|---|---|---|
| 2 | +0.196908588294147 | κ log 2 | 0 |
| 3 | −0.312092728516164 | −κ log 3 | 0 |
| 4 | −1.44223196460646 | −(2 + κ²)log 2 | −2·10⁻³¹ |
| 6 | +1.93635607662104 | (1 + κ²)log 6 | 0 |
| 12 | −0.762877471988412 | −κ(1 + κ²)log 12 | +1·10⁻³¹ |
| 5, 10, 25, 50 | 0 | 0 (5 | n) | exact |

Λ_DH(12) < 0 is zoo I.1's one-line witness and it is reproduced. **Independent confirmation of the coefficient convention:** −f′_DH/f_DH(s) against Σ_{n≤22026}Λ_DH(n)n^{−s} gives **1.4·10⁻¹⁶ at s = 4 + 20i**, 2.0·10⁻¹⁹ at s = 5, 4.3·10⁻¹² at s = 3 + 5i (tail-limited) — the note's 1.4·10⁻¹⁶ and 4·10⁻¹² exactly. **DH's archimedean bracket checked at the source:** `finisher_weilext.py` `params('dh')` returns a = 3/4, log(q/π) = log(5/π), `use02 = False`; so the bracket is Re ψ(¾ + ir/2) + log(5/π) and there are **no** ĝ(±i/2) terms (Ξ_DH entire) — the note's (1.2) is right, and it is NOT ζ's bracket.

| quantity | **mine** | note / `out/dh_t85p7_L10.json` |
|---|---|---|
| **P (coefficient sum)** | **+0.33999546892892616905** | +0.3399954689289246 |
| ℓ¹ of the DH weights | 3.29236846776 | 3.292368467762117 |
| max |Λ_DH(n)|, n ≤ 22 026 | 157.796 at n = 19 656 | 157.8 at n = 19 656 |
| **ARCH_DH** | **+0.0701833947306374** | +0.07018339473063738 |
| **W_DH = ARCH − P** | **−0.26981207419828877** | −0.269812074198287 |

**It FIRES: W < 0 at L = 10, from 22 026 Dirichlet coefficients and no zero of f_DH computed.** My value differs from the note's coefficient side by **1.8·10⁻¹⁵** and from the note's FULL corrected zero side (−0.269812074198325) by **+3.6·10⁻¹⁴** (the note's own residual: +3.8·10⁻¹⁴). **Stop condition 2 does not fire.**

### **FIX-FIRST (2a) — the term count 15 346 is a floating-point artifact; the true count is 8 562**

The note prints "15 346" as the number of DH coefficients at L = 10 in five places and the zoo draft repeats it. Arithmetic: 22 025 integers in [2, 22 026], of which 4 405 are divisible by 5 (Λ_DH = 0 there, by the note's own induction), leaving 17 620. The note's §1 says "Λ_DH(n) = 0 exactly at 2178 further n ≤ 22026 coprime to 5", which forces 17 620 − 2 178 = **15 442** — the number its own mpmath diagnostic printed (`logs/dh_coeff_check.log` line 12), not the 15 346 the Rust printed (line 13). Neither is the count of nonzero coefficients. Recomputing the recursion at 30, 60 and 100 digits and counting |Λ_DH(n)| above 10⁻²², 10⁻⁵², 10⁻⁹² gives **8 562 every time**, while the naive `≠ 0` test gives 15 442, 15 512, 15 766 — i.e. the "nonzero" count grows with the working precision, which is the signature of a roundoff floor. Spot check at 200: n = 38, 58, 66, 76, 88, 99, 114, 116, 122, 124, 132, 133, 142 read −1.97·10⁻³¹ at dps 30, 0 or 10⁻⁶¹ at dps 60, 0 or 10⁻¹²¹ at dps 120 — they are exact structural zeros. **Corrections required:** "15 346" → **8 562** wherever it appears as a coefficient count (note §0.2, §2.2, §5.1 table, §9, §10; zoo IV.19 STATEMENT and THE TWO CONTROLS); "2178 further n ≤ 22026 coprime to 5" (§1) → **9 058**; and "340 796 040 terms" / "3.4·10⁸ coefficients" at L = 20 is inflated by the same mechanism and must be either recomputed or labeled "f64-nonzero count, an upper bound on the true term count". **No computed value moves** — the spurious terms carry |Λ_DH| ≤ 10⁻³¹ and contribute below 10⁻³⁰ to P. What moves is every sentence that prices the channel by its coefficient count, which is the rung's own cost claim.

**Verdict: CLOSES on the number and the firing; FIX-FIRST on the count.**

---

## §3 Deliverable 3 — the record correction of §5.3: **CONFIRMED, independently; blast radius CONFINED; no headline moves**

**I re-ran the record's own recipe, verbatim.** `mp.mp.dps = 15`; sign changes of Z_DH(u) = Re Ξ_DH(½ + iu) on [t − 30, t + 30] at step 0.05; `mp.findroot(..., solver='illinois')`. It returns **36** on-line points — the record's 36, and the same list to the printed digits (57.0415, 58.3952, 59.7670, 61.7021, …, 112.377). I then refined each at **40 digits** on the gamma-normalized real function S(u) = Z_DH(u)/[(5/π)^{3/4}|Γ(¾ + iu/2)|], the note's fix.

| | recorded u | refined u (40 digits) | displacement | |f_DH(½+iu)| recorded | |f_DH(½+iu)| refined |
|---|---|---|---|---|---|
| the note's example 1 | 87.647527835149 | 87.6474763325597388 | **−5.15·10⁻⁵** | 2.56·10⁻⁴ | 3.5·10⁻³⁹ |
| the note's example 2 | 89.43961870346 | 89.4391887988165135 | **−4.299·10⁻⁴** | 1.98·10⁻³ | 3.1·10⁻³⁹ |
| worst in ±30 | 102.82034971047 | 102.819209827108413 | **−1.14·10⁻³** | 3.7·10⁻³ | 2.5·10⁻³⁹ |
| best in ±30 | 100.59899262113 | 100.598993807792285 | +1.19·10⁻⁶ | 4.85·10⁻⁶ | 1.3·10⁻⁴⁰ |

The note's two quoted examples are reproduced **to every printed digit**. Max |f_DH| over the 36 refined points: **3.5·10⁻³⁹**. Max |Z_DH| over the RECORDED points: **4.3·10⁻²²** — the record's checker criterion ("max |Z_DH(γ)| = 1.9·10⁻³²", `results/c2-m2/SHARED.md` checkpoint (5)) is scale-blind exactly as the note says: |Ξ_DH(½ + iu)| carries the factor |Γ(¾ + iu/2)| ≈ e^{−πu/4} ≈ 10⁻²⁰…10⁻³³ across this window, so an absolute |f| < tol stopping test is met after one secant step and certifies nothing. **The diagnosis is correct and the mechanism is exactly as stated.**

**The record's numbers, recomputed both ways (my own transform, 40 digits):**

| L | W_{Z′} with RECORDED zeros | W_{Z′} with REFINED zeros | relative | W_Z recorded | W_Z refined |
|---|---|---|---|---|---|
| 10 | 0.0048010831908 (record log: 0.0048010832) | **0.0048001176057** (note: 0.0048001176) | −2.01·10⁻⁴ | −0.26981111059 (record −0.26981111) | −0.26981207617 (note −0.26981208) |
| 20 | 4.4642881736·10⁻⁵ (record 4.4642882·10⁻⁵) | **4.465246591·10⁻⁵** (note: 4.4652·10⁻⁵) | +2.15·10⁻⁴ | −0.74823115488 | −0.74823114530 |
| 86.907 (= L*) | 3.4282149942·10⁻¹⁰ (record 3.4·10⁻¹⁰) | **3.4044546582·10⁻¹⁰** | −6.9·10⁻³ | −394251.68287 | −394251.68287 |

Every figure of §5.3 is reproduced. My recomputed record configuration at L = 10, −0.269812076170907 in the note, comes out at −0.26981207617 — the same eleven digits.

**Which record files the correction touches.** The mislocating recipe (sign changes of Z_DH refined by `findroot` on Z_DH itself, at dps 15) is in `results/c2-m2/verify/dh_negative_control.py` (lines 22–29), `results/c2-m2/campaign/dh_offline_scan.py` (`online_count`, line 75), and `results/c2-m2/campaign/dh_control_new_heights.py` (`online_count`, line 35). Downstream: `dh_negative_control_run.log` / `_out.json` (the W_{Z′} and W_Z columns of the nine L-rows), `dh_offline_scan.json` (`control_rows`, `online_window`), the control tables at t = 114.163343, 166.479306, 176.702461 printed in `CAMPAIGN.md` §1, `separation-note.md` §8 rung 2 (the W_{Z′} = 3.4·10⁻¹⁰ figure and the sentence "the in-window on-line noise is 3·10⁻¹⁰"), and `results/c2-m2/SHARED.md` checkpoint (5) (the criterion itself).

**Which headlines move: NONE — and for a stronger reason than the note gives.** The note argues "the main term dominates". The exact reason is better: every record script forms W_Z = W(orbit ∪ on-line) and W_{Z′} = W(on-line), so **W_Z − W_{Z′} = W(orbit) identically**, and the on-line positions cancel out of it exactly. Therefore the separation column, the "ratio to δ²e^{δL/2}" column and the "fires (≥ 1)" column of every DH control table — at t = 85.7, 114.16, 166.48, 176.70 — are **unaffected to machine precision**, whatever the on-line zeros are. Concretely:

* **The ×6.24 ratio** (separation-note §8 rung 2; IV.9's 2026-09-16 rider; `check-O.md` §11.1 of M2). Recomputed with the refined zeros: |W_Z − W_{Z′}| = 394251.682869, bound δ²e^{δL/2} = 63208.6, **ratio 6.23731** against the record's 6.2375 — a fourth-digit move that is my truncation of L* to 86.907, not the zero correction. **STANDS.**
* **The 26 off-line orbits** (`dh_offline_scan.json`; CAMPAIGN §1). Located by a bounded damped Newton on f_DH via f′/f and re-refined in `dh_control_new_heights.py` by `mp.findroot(dh.f_dh, …, tol=1e-24)` — on f_DH itself, never on Z_DH. **Untouched**, as the note says. The block "excess" logic that drives the search counts sign changes; a mislocated root is still a correctly counted one, so the scan's orbit count is untouched too. **STANDS.**
* **The campaign's closes** (stop conditions (i)–(iv), the positive controls, the L_sign/L_bal3 tables, `rows_t1e*.json`). All ζ-side, all from `mpmath.zetazero`. **No DH zero enters any of them. STANDS.**
* **The M2 theorem and its constants.** Zero-side statements about abstract configurations; the DH rung is a control, not an input. **STANDS.**

**One record question this rung incidentally SETTLES, and the note does not claim it.** `separation-note.md` §8 rung 2 leaves open whether the record's 36 on-line zeros in ±30 are complete ("the phase count … = 40.1 against 36 + 2 found is indicative only — the difference is … a further off-line pair or a close on-line pair missed by the sign-change scan"). The note's §5.2 argument-principle count on [−1, 2] × [t − 60, t + 60] returns exactly 79 = 75 on-line + 2 orbits × 2, on two rectangles, so the step-0.05 scan misses nothing in ±60 and therefore nothing in ±30: the 40.1 is S(T) fluctuation. **Worth promoting into the corrections line for §8 rung 2 — it closes a caveat, at no cost.**

### Exact-wording corrections for §5.3

* "the returned 'zero' is off by 5·10⁻⁵ to 1.4·10⁻³" → the range over the 36 points of the record's own window is **1.2·10⁻⁶ to 1.1·10⁻³** (the note's 5·10⁻⁵ is the smallest of its three quoted examples, not the smallest displacement; 1.4·10⁻³ is from the wider ±60 window, which is correct there).
* "at the recorded points f_DH(½ + iu) is 10⁻⁴–10⁻³ in size" → **4.9·10⁻⁶ to 3.7·10⁻³**.
* Add the cancellation argument above to the "what this changes on the record" paragraph: it converts "the headlines stand because the main term dominates" (an estimate) into "the separation, ratio and fires columns are identically independent of the on-line positions" (an identity).
* "that digit string is good to roughly one digit" (about W_{Z′} at L*) → measured: 3.4282·10⁻¹⁰ → 3.4045·10⁻¹⁰, **good to two digits**; the note's inference from L*·Δγ was conservative and can be replaced by the computation.

**Verdict: CLOSES. The correction is real, correctly diagnosed, correctly fixed, and correctly scoped. The recommended repair (re-run the three scripts with the rescaled S(u)) is right and should be carried out; it is a reprint of W_{Z′} columns, not a re-decision of anything.**

---

## §4 Deliverable 4 — Theorem (E): the proof is CORRECT; the numbers CLOSE; **the LABEL is FIX-FIRST**

### §4.1 The proof, re-derived line by line: **correct**

*Step 1.* Σ_p m_p log p = 0 with m ∈ ℤ^N ⟹ Π_{m_p>0}p^{m_p} = Π_{m_p<0}p^{−m_p} ⟹ m = 0 by unique factorization. Correct; λ_m ≠ 0 for m ≠ 0. ✔
*Step 2.* |(1/H)∫_T^{T+H}e^{iλt}dt| = |e^{iλH} − 1|/(H|λ|) ≤ 2/(H|λ|). Correct, and the T-independence is exactly the step the classical statement over (0, T) does not give. ✔
*Step 3.* K_M = Σ_{|k|≤M}(1 − |k|/(M+1))e^{ikx} = (M+1)⁻¹(sin((M+1)x/2)/sin(x/2))² ≥ 0, (1/2π)∫K_M = 1, and K_M(x) ≤ ((M+1)sin²(ρ/2))⁻¹ on ρ ≤ |x| ≤ π — standard and correctly stated. F_M = Π_jK_M(x_j)/(2π)^N has ∫F_M = 1 and the union bound ∫_{max|x_j|≥ρ}F_M ≤ N/((M+1)sin²(ρ/2)) is right (the other factors integrate to 1). σ_Mχ = χ ∗ F_M is a trigonometric polynomial of degree ≤ M in each variable with the same constant term, and |σ_Mχ − χ| ≤ ω_χ(ρ) + 2‖χ‖_∞N/((M+1)sin²(ρ/2)). ✔
*Step 4.* Φ(θ) = Σ_pφ_p(θ_p) is a sum in separated variables, so max Φ = Σ_p max φ_p — correct, and this is the step that gives the prime-power grouping rather than the ℓ¹ norm. χ = Π_p max(0, 1 − |θ_p − θ*_p|/ρ₀) has constant term (2π)^{−N}∫χ = (ρ₀/2π)^N = c₀ > 0 (each tent integrates to ρ₀). Q := σ_Mχ − c₀/2 satisfies Q ≤ χ, q₀ = c₀/2 > 0, and Q(θ) > 0 ⟹ χ(θ) > 0 ⟹ Φ(θ) > S − ε/2. ✔
*Step 5.* Q(θ(t)) = Σ_m q_me^{iλ_mt}; (1/H)∫_T^{T+H}Q ≥ q₀ − 2Σ_{m≠0}|q_m|/(H|λ_m|) ≥ c₀/4 for H ≥ H₀ := (8/c₀)Σ_{m≠0}|q_m|/|λ_m|, a finite sum over |m_j| ≤ M, independent of T. Hence a good t in every window of length ≥ H₀. With P ≤ S everywhere, sup_{[T,T+H]}P ∈ (S − ε, S]. The infimum and |P| statements follow. ✔ **∎ The proof is correct as written; I found no gap.**

**One line the proof earns and does not print, and the zoo entry needs it.** Since Q ≤ χ ≤ 1 and ∫_T^{T+H}Q ≥ (c₀/4)H, we get meas{t ∈ [T, T + H] : Q(θ(t)) > 0} ≥ (c₀/4)H. So the near-maximizers occupy a set of **lower density ≥ c₀/4 in every window of length ≥ H₀**, not merely one point. The zoo draft's EXECUTABLE TEST already asserts "a set of heights of positive lower density in every long window (Theorem (E), Step 5)" — true, but Step 5 as printed gives only existence. **Add the two-line measure remark to §6 Step 5, or weaken the zoo's test.**

### §4.2 The instance numbers, recomputed from my own coefficients: **every one reproduced**

`own/sup_E.py`: prime-power grouping by smallest prime factor, max_θ φ_p by a 200 001-point grid plus golden-section refinement to 10⁻¹⁵.

| quantity at L = 10 | **mine** | note §6 |
|---|---|---|
| ℓ¹ = Σ|w_n| | 1.4568633200341718 | 1.456863 |
| primes part / prime-power part | 1.411211185939921 / 0.04565213409425 | 1.411211 / 0.04565 |
| **Σ_p max_θ φ_p = sup_t P** | **1.4201549249138394** | 1.420155 |
| **Σ_p max_θ(−φ_p) = sup_t(−P)** | **1.4221742500577328** | 1.422174 |
| **sup_t |P|** | **1.4221742500577328** | **1.422174** |
| sup/ℓ¹ (alignment defect 1 − ·) | 0.976189207663197 (2.381 %) | 0.9762 (2.4 %) |
| trivial 4√X·a₀ | 9.867569213876054 | 9.868 |
| 2a₀·Σ_{n≤X}Λ(n)n^{−1/2} | 9.774122502821134 | 9.774 |
| PNT approximation (2/L²)∫₀¹e^{Lv/2}|A(v)|dv | 1.4778050121321007 (L = 10), 12.542505591259488 (L = 20) | 1.4778, 12.5425 |
| primes carrying a k ≥ 2 harmonic | 34 | (implied by 66 prime powers) |

**The trivial-bound correction is right.** P = Σ_{n≤X}Λ(n)n^{−1/2}(g(log n) + g(−log n)) with |g(±log n)| ≤ g(0) = a₀ gives |P| ≤ 2a₀Σ_{n≤X}Λ(n)n^{−1/2} ≈ 4√X·a₀ — the factor 2 the pricing's "2√X‖g‖_∞" omitted. Measured: 9.868 (and the sharper 9.774 with the exact Chebyshev-type sum), against the attained supremum 1.4222 — **a factor 6.94 at L = 10 and 14.61 at L = 20**, the note's "7 and 15 times". The sharp trivial bound is the ℓ¹ norm, as the note says. ✔ And the note's §11(ii) is right that PRICING §3(b)'s "ℓ¹ norm Σ_{n≤X}Λ(n)n^{−1/2}|w_n|" double-counts the weight and that there is no "t-independent part" to subtract (log n ≠ 0 whenever Λ(n) ≠ 0). ✔

### §4.3 **FIX-FIRST — the novelty label and the 10(n) line (deliverable 8, standing order 7)**

I ran the corpus and the online prior-art gate (V.2; the builder ran neither, by contract). Findings, with the sources at the page:

* **The citation the note does make is accurate.** Steuding, *Value-Distribution of L-Functions*, LNM 1877, printed p. 17 (running head "1.3 Voronin's Universality Theorem 17"): "**Lemma 1.8.** (i) Let a₁,…,a_N be real numbers, linearly independent over ℚ, and let γ be a subregion of the N-dimensional unit cube with Jordan content Γ. Then lim_{T→∞}(1/T) meas{τ ∈ (0,T) : (τa₁,…,τa_N) ∈ γ mod 1} = Γ." Steuding introduces it as Weyl's refinement of Kronecker's approximation theorem, and the sentence the note quotes is on the following page verbatim: "The unique prime factorization of integers implies the linear independence of the logarithms of the prime numbers over the field of rational numbers." Lemma 1.8(i) is a density statement over the growing interval (0, T) with no uniformity in T and no supremum, so the note's description of it as "the equidistribution form of what follows" is exact and is **not** an overclaim.
* **But (E) itself is in print, in a stronger form.** **Turán**, *Acta Sci. Math. (Szeged)* 21 (1960) 311–318, **Lemma p. 313**, gives the window-uniform simultaneous-approximation statement for the frequencies {log p} with an explicit window length T = e^{17ωN²log N}. **Weber**, "On localization in Kronecker's diophantine theorem", *Uniform Distribution Theory* 4 (2009) 97–116 (arXiv:0806.3990), §3 pp. 8–9, **Theorem 1** with **(3.17)–(3.18)**, gives the general statement: for ℚ-independent λ and a Dirichlet polynomial D_L(t) = Σα_n n^{it}, the torus supremum minus the supremum over an interval of length ≥ T(N, ω) is ≤ (2π/ω)Σ|α_n|Ω(n), and — verbatim — "the supremum of the Dirichlet polynomials D_L over large intervals (of length greater than T(N,ω)) is comparable to the supremum over the real line… Further estimate (3.18) is uniform over d." Weber also records the note's own §11(i) correction (Dirichlet's theorem is the homogeneous special case β = d = 0 of Kronecker's, his (3.19)). Companion survey arXiv:0907.4931 states (67) unique factorization ⇒ independence, (68) "H. Bohr's observation" sup_ℝ = sup_{𝕋^μ}, (69) sup_ℝ|Σd(n)e^{−itφ_n}| = Σ|d(n)| "an immediate consequence of Kronecker's Theorem". Same circle: Bohr (1913); Konyagin–Queffélec, *Real Anal. Exchange* 27 (2001/02) 155–176; Balasubramanian–Calado–Queffélec, *Studia Math.* 175 (2006); Defant–Frerick–Ortega-Cerdà–Ounaïes–Seip, *Ann. of Math.* 174 (2011).
* **Corpus.** Steuding `fetched/p3-29c` is the only on-disk carrier of the mechanism. Titchmarsh, Karatsuba–Voronin, Ivić, Montgomery–Vaughan *MNT I*, and every Bohr almost-periodicity text are **not** on disk; `PRICING.md` line 216 already lists "Kronecker's theorem / Bohr's sup theorem for Dirichlet polynomials" as recalled-and-classical.
* **Farmer 2211.11671 §9.3 says nothing of this shape** (verified at the page, p. 44: Conjecture 9.7 LH, the U(N) analogue (9.2)–(9.3), Backlund's Theorem 9.8, Proposition 9.9 — no Kronecker, no torus, no ℓ¹, no prime sum, no window supremum). The mechanism surfaces twice elsewhere in that paper and **neither place is (E)**: §10.1 p. 47 "One should expect a central limit theorem to hold for the sum over primes, because the log p are linearly independent over the rationals"; and §13 p. 64 on the Deuring–Heilbronn function — DH has ≫T zeros in σ > 1 "but that is not any extra information because Dirichlet series are almost periodic functions (of t) in σ > 1: so once there is one zero in that region, there must be ≫ T zeros in that region" (Principle 13.2). **That second passage is worth citing beside the rung's own DH control**; it is the recurrence half of the same mechanism applied to the rung's own negative control, and no C2 file names it.

**Corrections required.** (a) §6's theorem header becomes "**Theorem (E)** (Bohr 1913; **Turán 1960, Lemma p. 313**, for the frequencies {log p}; **Weber, Unif. Distrib. Theory 4 (2009) 97–116, Theorem 1 and (3.17)–(3.18)**, in general and **effective**) — proof reproduced here for this coefficient system; the published form is effective, this one is not". (b) The §6 "Nearest published object (10(n))" paragraph is rewritten: the nearest published object is Weber 2009 Theorem 1, not Bohr's theorem in the abstract, and the exact difference shrinks to *the specific coefficient system, the prime-power grouping, the numbers, and the use as an impossibility for a detector's estimate route*. (c) `[novelty: single-check]` on the statement becomes **`[classical: cited at the page]`**; the `[novelty: dual-model check 2026-09-17]` label attaches only to the instance numbers and to the impossibility reading. (d) §11's "Recalled, labeled, none load-bearing: Bohr's original almost-periodicity theorem" is no longer the right shelf — the object is now read and cited. (e) Same edits in the zoo draft (§9 below).

**What stays the program's, after the check:** the exact supremum for w_n = 2Λ(n)n^{−1/2}a(log n) with the prime-power grouping (1.422174 at L = 10, 12.529890 at L = 20; defect 2.38 % / 0.08 %); the twelve-point ℓ¹/signal table; the correction of PRICING §3(a)'s trivial bound to the ℓ¹ norm; and the *reading* of the classical supremum as the wall for the M6 estimate route ("the detector is an evaluation"). The last is an interpretation, not a theorem, and must be labeled as one. **No paper found states that reading.**

**Verdict: the proof CLOSES; the instance CLOSES; the label and the 10(n) line are FIX-FIRST.**

---

## §5 Deliverable 5 — the cost line, re-measured on this machine: **CLOSES**

I rebuilt `verify/twisted_sum.rs` from source (rustc 1.98.1, `-O -C target-cpu=native`) and re-ran the timing points. Two independent single-thread runs each, at X = 485 165 195, 25 617 272 terms (the term split 25 614 562 primes + 2 710 prime powers is reproduced; P = 4.562999824717394·10⁻³ reproduces `out/zeta_t85p7_L20.json` exactly).

| rate | **mine** | note §7 |
|---|---|---|
| sieve only, 1 thread | 0.994 s, 0.993 s ⇒ **r_sieve = 2.049 ns / sieved integer** | 0.994 s ⇒ 2.05 |
| full, 1 thread | 5.523 s, 5.522 s ⇒ **r_term = 176.8 ns / term** | 5.640 s ⇒ 181.4 |
| full, 8 threads | 1.115 s ⇒ **S = 4.95** | 1.144 s ⇒ 4.93 |

Solving wall(X) = [(li(X) + Σ_{k≥2}li(X^{1/k}))·r_term + X·r_sieve]/S against 1 h and 24 h:

| boundary | **my rates** | the note's rates, re-solved by me | note §7 |
|---|---|---|---|
| A/B (1 h) | **L = 28.369**, X = 2.09·10¹² | L = 28.345, X = 2.04·10¹² | **L = 28.35, X = 2.0·10¹²** |
| B/C (24 h) | **L = 31.632**, X = 5.46·10¹³ | L = 31.608, X = 5.34·10¹³ | **L = 31.61, X = 5.3·10¹³** |
| one year | L = 37.661 | L = 37.639 | 37.64 |

**The note's two class boundaries are exactly what its own rates imply, and my independently measured rates move them by 0.024 in L (1.2 % in X).** The twelve campaign points reproduce class for class on my rates: (0.05, 10³) at L_sign = 32.1 → 1.58 d, **C**; (0.05, 10⁶) at 33.3 → 5.10 d, **C**; medians 31.4 → 0.80 d **B** and 29.0 → 1.85 h **B**; every δ ≥ 0.1 point class **A**. The note's readings of the pricing's own classes ("the pricing's boundaries land in the right classes for the wrong reason": term count is li(X), not X; 181 ns not 50 ns; the sieve is a second cost) are arithmetic and correct.

**One wording point.** §7 says "the model reproduces the 8-thread measurement at X₀ exactly (1.144 s)". It is fitted to it by construction (S is defined as the ratio), so "exactly" is a tautology, not a validation; say "the model is normalized at X₀". My own rates give 1.116 s against my measured 1.115 s, which is the same tautology.

**Verdict: CLOSES.**

---

## §6 Deliverable 6 — the conditional-detector paragraph and the "Lindelöf lock SHARED" sentence: **FIX-FIRST (four corrections)**

**Farmer §9.3 is accurate at the page.** Read at p. 44 of arXiv:2211.11671v4: Conjecture 9.7 is LH in the form Z(t) = O_ε(t^ε), displays (9.1)–(9.2) (and (9.3) is the U(N) analogue max_{|z|=1}Z_A(z) = e^{o(N)}); Theorem 9.8 is Backlund's equivalence, LH ⟺ N(σ, T + 1) − N(σ, T) = o_σ(log T) for all σ > ½, displays (9.4)–(9.5); and the sentence the note quotes — "for any fixed A > 0 and any fixed-width strip around the critical line, a negligible proportion of the zeros with T ≤ γ ≤ T + A lie outside that strip" — is **verbatim**, immediately after (9.5). The §12.1 and §14.3 readings are as PRICING §3(c) quotes them. ✔

### FIX-FIRST (6a) — §8 drops the hypothesis that §6 carries, and the dropped clause is the load-bearing one

§8 reads: "What does NOT improve is the **pointwise value** of P_X(g_t) at the given t: by (E) **no bound uniform over a window** certifies it". As written this is false — a bound uniform over a window of length 1/L is exactly what a short-Dirichlet-polynomial estimate is, and (E) says nothing about it. The hypothesis is "uniform over a window of length ≥ H₀", and H₀ here is of the size of Turán's e^{17ωN²log N} with N = π(e^L) — astronomically beyond any height the channel will ever visit. This matters precisely here, because `results/full-map.md` line 203 defines the program's Lindelöf lock as "an a-priori bound λ_max(G̃/ℓ₁) = O(1) — **equivalently bounds for P_X(τ) = Σ_{n≤X}Λ(n)n^{−1/2−iτ} on windows of length ≍ 1/L**". **(E) closes that route only through the T-uniformity of the constant, not through the window length.** Correct wording: "*by (E), no bound on |P_X(g_t)| whose constant is uniform in the height certifies it — the constant would have to exceed the torus supremum; a bound with a T-dependent constant is an evaluation by another name.*" The note's §6 "What it does NOT say" paragraph already says the right thing; §8 must say it too.

### FIX-FIRST (6b) — the o(1) sentence needs its normalization

§8: "the number of off-line zeros in a unit window is o(log T), so **the proportion of heights t ∈ [T, 2T] at which an orbit of depth ≥ δ sits within the kernel's reach ≈ 5/L of t is o(1)**". As Lebesgue proportion of [T, 2T] at **fixed** L this does not follow: Backlund's form gives ≤ T·o_δ(log T) such zeros in [T, 2T], each capturing a set of measure ≈ 10/L, so the proportion is (10/L)·o(log T), which is unbounded for fixed L. It is o(1) **as a proportion of the zeros** — equivalently, when the reach 5/L is measured in units of the mean spacing 2π/log(t/2π), which is exactly the note's own §4 reading ("the datum reads ≈ 2 zeros at L = 10 and t = 10⁶"). Correct wording: "*a proportion o(1) of the zeros in [T, 2T] lie at depth ≥ δ, so the datum at a height sampled from the zeros sits near a deep orbit with probability o(1)*". The italic restatement that follows (PRICING's own words, "the proportion of heights in [T, 2T] at which an orbit of depth ≥ δ would be missed … is o(1)") inherits the same defect and should carry the same normalization.

### FIX-FIRST (6c) — "the Lindelöf lock of zoo IV.7" mis-anchors the pointer

Zoo **IV.7** is the garnish-absorption barrier (divergent-cutoff scalar Schatten rows). Its STATEMENT, its Session-6 closure, its riders and its 2026-09-10 pointer contain **no** occurrence of "Lindelöf", "λ_max", "Dirichlet polynomial", "pointwise", "mean-square" or "large-value" (grep over lines 392–403 of `BARRIER-ZOO.md`: zero hits). In the zoo the phrase is named at **IV.6** ("the ONLY visible routes around the odd-degree sign problem: (a) a λ_max(Q)-type hypothesis (= **the Lindelöf lock**, to be proven not assumed)") and in the protocol §0 item 5(b) ("is any 'second-order/technical' step secretly … a Lindelöf-strength λ_max bound (IV.3, IV.4, IV.6)?"); it is **defined** in `directions/A4-lindelof-lock.md`, and IV.7's Session-6 closure is where the *Schatten-3 route to it* was decided (absorption, δ₀ = 0). The mis-anchor is inherited, not invented here: IV.9's 2026-09-16 rider says "M6, the pointwise short-Dirichlet-polynomial wall shared with the campaign residue; zoo IV.7's Session-6 closure", PRICING §3(a) repeats it ("The pointwise short-Dirichlet-polynomial bounds of zoo IV.7's Session-6 closure"), and the note and the zoo draft inherit it from PRICING. **Correct wording, everywhere: "the Lindelöf lock (`directions/A4-lindelof-lock.md`; named at zoo IV.6 and in the §0 protocol item 5(b); the Schatten-3 route to it decided at IV.7's Session-6 closure; the prime-side form is `results/full-map.md` line 203)".** The orchestrator should also put a one-line rider on IV.9 so the chain stops propagating.

### FIX-FIRST (6d) — cite Farmer by section and page, not by pdftotext line

§8 and §12 locate the Farmer quotations by "text lines 2594–2640 of the pdftotext extraction". My own `pdftotext` of the same file puts §9.3 at lines 2923–2975. Line numbers of a text extraction are not a citation; the reproducible anchors are §9.3, Conjecture 9.7, (9.1)–(9.3), Theorem 9.8, (9.4)–(9.5), **p. 44**. Same for the Steuding reference (Lemma 1.8(i), **p. 17**, which the note does give correctly) and for §12's row.

**What is right in §8 and should be kept.** The two-branch structure (t-averaged improves, pointwise does not); the refusal to claim the averaged branch as new territory ("the campaign residue's statement in new clothes and is claimed as such"); the single-defect regime declared a computation with a cost curve and not a theorem; and the Farmer bearing (σ = ¾ is δ = ¼, class A at every height; the valleys are the shallow regime where the first-order datum is blind — the honest scope line). Repair 6's requirement is discharged in substance; the four corrections above are wording and pointers.

**Verdict: FIX-FIRST.**

---

## §7 Deliverable 7 — "cannot"/"never" sentences, the ladder, the zoo protocol, 10(g), U.S. English: **CLOSES, with two exceptions**

* **10(g) hedges.** Case-insensitive grep for "clearly", "obviously", "easy to see", "well known" over `m6-rung1-note.md`, `zoo-IV19-proposed.md`, `SHARED.md`, `verify/*.py`, `verify/*.rs`, `verify/*.sh`: **no hits**. ✔
* **U.S. English.** Grep for sixty-odd British forms (the -our, -re, -ise/-yse, -lled and maths/grey/towards/programme families) over the same files: **no hits**. ✔ The one form to watch on the next edit is the noun spelling of "license" in any new citation line.
* **Every "cannot"/"never" sentence.** Four occurrences. §6's consequence ("the sign of W … is therefore never certified by an estimate of that class") carries its hypothesis in the same sentence ✔, and I add that it is safe beyond the tabulated points: sup_𝕋|Φ| ≍ ℓ¹ ≍ (2/L²)∫₀¹e^{Lv/2}|A| grows like e^{L/2}, while the signal 2δ²c(δL)² grows like e^{δL}, so for every δ < ½ the supremum eventually dominates the signal — the note may state the claim for δ < ½ rather than only at the twelve points. §7's "memory is never the wall for ζ" carries the base-prime count ✔ (and is true to L ≈ 38 on this machine: √X = 1.5·10⁸ at X = 2.2·10¹⁶, 8·10⁶ base primes). §10's "fails" sentence is quoted and refuted ✔. **Exception:** §8's "no bound uniform over a window certifies it" — the hypothesis is dropped; see §6a above. **Exception:** the zoo draft's "the estimate is false on a set of heights of positive lower density in every long window" asserts more than §6 Step 5 prints; see §4.1.
* **Ladder (10(b)).** Rung 2 (DH, RH false) first, decided coefficient-side at L = 10 ✔; rung 4 (ζ) silent at four points ✔; rung 1 (function fields) recorded degenerate, consistent with `separation-note.md` §8 ✔; rung 3 (ζ_K) not run and its bracket labeled `[recalled, unverified]` ✔. The brief required DH first and the SHARED.md checkpoint order records that the rehearsal at (85.7, 10) ran first end to end (10(l)) ✔.
* **Zoo protocol §0, in order.** (1) scope declared "refutation channel + a refutation-shaped theorem about the estimate class" ✔. (2) I.1 run at the AXIOM level, and correctly: the channel's inputs are (a) the explicit formula of the function at hand, (b) its Dirichlet coefficients to e^L, (c) its archimedean bracket, (d) the sign of W; DH satisfies (a)–(c) and the OUTPUT differs. I.1's own EXECUTABLE TEST clause (c) is written for full-RH briefs and exempts proportion briefs; a **refutation channel** is the third case, and the note's answer — "the RH-false world satisfies every input, and the channel's output distinguishes it, which is what a refutation channel is for; a full-RH brief consuming only (a)–(d) would be returned by I.1, and this rung is not one" — is the right reading and should be promoted into I.1 as a clause, since this is the first refutation-channel brief to meet it. The I.1 witness Λ_DH(12) = −0.7629 < 0 is reproduced here exactly. ✔ (3) II: correctly declared not certificate-class; II.4's rider cited ✔. (4) III: III.1 named as the regime the averaged branch collapses to, claimed and not evaded ✔; III.9/III.10 correctly placed on the estimate side ✔. (5) IV: IV.1, IV.2, IV.3/IV.4/IV.6 (the λ_max/Lindelöf-strength smuggling question, answered "not consumed") ✔, IV.7 named — see §6c on the anchor. (6) IV.9 visibility: the visible regime is L ≥ L_sign with its term count ✔, and the entry correctly supersedes the rider **only** on the sign side while preserving "not computable" for certifying the theorem's bound ✔. (7) V: V.2 prior art was deferred to this job by design and is now run (§4.3, and it FIRES); V.4 both controls named with their runs and run before any number was quoted ✔; V.5 no null-literature claim is load-bearing ✔.
* **Traceability (§12).** Every number I checked resolves to the named log or JSON. Two rows need repair: the Farmer/Steuding row's pdftotext line numbers (§6d), and the term-count rows (§2a).

**Verdict: CLOSES, with the two exceptions carried into the FIX-FIRST list.**

---

## §8 Deliverable 8 — the standing-order-7 novelty check

Delivered in **§4.3** above. Summary: (E)'s statement and proof mechanism are classical and in print in a stronger, effective form (Turán 1960; Weber 2009); the citation the note does make (Steuding Lemma 1.8(i), p. 17) is accurate at the page and correctly characterized; Farmer §9.3 says nothing of this shape, though Farmer §13 p. 64 applies the same almost-periodicity mechanism to the rung's own DH control and deserves a citation line. What stays the program's: the instance, the trivial-bound correction, and the impossibility reading, the last labeled as an interpretation.

---

## §9 Deliverable 9 — zoo IV.19 as drafted: **FIX-FIRST; six amendments before insertion**

**Statement.** Mathematically correct as written, and better scoped than §8 of the note: it carries "valid uniformly over a window of length ≥ H₀ — in particular any height-uniform estimate" in the CONSEQUENCE, which is the right hypothesis. The Lean anchor (`EF_lit_zetaZeroConfig`, `WeilEF/Main.lean` 270; `ExplicitFormula.lean` 70–74 `literatureRHS`) is quoted accurately: I read lines 64–84 and 260–275 and the note's block is verbatim, including `gammaBracket r = (Complex.digamma (1/4 + I*r/2)).re - Real.log π` and the two hypotheses `ContDiff ℝ 2 k`, `HasCompactSupport k` that g satisfies.

**KILLS scope.** Correct and correctly hedged. It kills (i) briefs certifying a first-order datum's sign at a chosen height by a **t-uniform** prime-side estimate — hypothesis stated; (ii) briefs pricing the prime-side evaluation by L* rather than L_sign — and it explicitly preserves IV.9's "not computable" for certifying the theorem's BOUND, which is the honest split; (iii) briefs quoting "2√X‖g‖_∞" as the size of the prime sum — verified here (the trivial bound is 4√X‖g‖_∞ = 9.868 at L = 10 and the sharp one is the ℓ¹ norm 1.4569, attained to 97.6 %). No overreach found in the KILLS clause.

**EXECUTABLE TEST.** Runnable as written; I ran its first half (`kronecker_instance.py`'s computation, reimplemented) and reproduced 1.422174. Two repairs: the "positive lower density" claim needs the two-line measure remark added to §6 Step 5 (§4.1); and the PNT shortcut "(2/L²)∫₀¹e^{Lv/2}|A(v)|dv suffices above L = 20" should carry its measured accuracy (1.4778 vs 1.4569 at L = 10 is 1.4 % high; 12.5425 vs 12.5397 at L = 20 is 0.02 % high — so "above L = 20" is right and the number should be printed).

**Grade.** The entry is a **Group IV** entry, correctly placed. Its content after this check is: a **classical theorem, cited**; a **computationally-verified** instance and cost line, both now dual-model reproduced; and an **impossibility reading**, which is the program's and is an interpretation.

**The six amendments required before insertion (count 57):**

1. **(E)'s attribution.** "**THEOREM (E)** (`m6-rung1-note.md` §6, proved in one and a half pages …)" → "**THEOREM (E)** (Bohr 1913; Turán, *Acta Sci. Math. Szeged* 21 (1960) 311–318, Lemma p. 313, for {log p}, with an effective window; Weber, *Unif. Distrib. Theory* 4 (2009) 97–116, Theorem 1 and (3.17)–(3.18), in general and effective; proof reproduced for this coefficient system in `m6-rung1-note.md` §6, non-effective)".
2. **The coefficient counts.** "15 346 coefficients" → **8 562**; "3.4·10⁸ coefficients" → labeled as the f64-nonzero count and an upper bound, or recomputed (§2a).
3. **The IV.7 anchor.** "the Lindelöf lock of IV.7" → "the Lindelöf lock (`directions/A4-lindelof-lock.md`; named at IV.6 and §0 item 5(b); Schatten-3 route decided at IV.7's Session-6 closure; prime-side form at `full-map.md` line 203)" (§6c), in both the STATEMENT and the SOURCE.
4. **The density clause** of the EXECUTABLE TEST, backed by the added measure remark in §6 Step 5 (§4.1).
5. **STATUS.** "**pending dual check**" → "**program-adjudicated (dual-model)**, `results/c2-m6/check-O.md` 2026-09-17", with the label split written as: theorem **`[classical: cited at the page]`**; instance + both controls + the cost line **`computationally-verified` (dual-model, independent implementation)**; the reading of (E) as the M6 estimate wall **`[novelty: dual-model check 2026-09-17]`**. Delete "the mechanism is Bohr's/Weyl's; the statement for this coefficient system over every long window … are the program's" — the window-uniform statement is Turán's and Weber's; only the coefficient system and the reading are the program's.
6. **SOURCE.** Add Weber (arXiv:0806.3990, UDT 4 (2009) 97–116) and Turán (1960, Lemma p. 313); add Farmer §13 p. 64 (Principle 13.2, almost periodicity ⇒ ≫T zeros in σ > 1 for DH) next to the DH control; replace the Farmer pdftotext line numbers with §/page anchors.

With those six made, **the entry is insertable and I endorse it.** Without amendment 1 it is a novelty claim for a 1960 theorem and must not go in.

---

## §10 The FIX-FIRST list, in the order the orchestrator should work it

1. **(E)'s attribution and novelty label** — note §6 (theorem header, "Nearest published object", the `[novelty: single-check]` line), note §11 (move Bohr off the "recalled" shelf), zoo IV.19 amendments 1, 5, 6. *Structural: without it the rung claims a published theorem.*
2. **The DH coefficient counts** — note §0.2, §1 ("2178" → 9 058), §2.2, §5.1 table, §9, §10; zoo IV.19 twice. True count at L = 10 is **8 562**; the L = 20 count must be recomputed or labeled.
3. **§8's dropped hypothesis** ("no bound uniform over a window" → "whose constant is uniform in the height") and **§8's o(1) normalization** (proportion of the zeros, not Lebesgue proportion of [T, 2T]).
4. **The IV.7 → IV.6 / A4 anchor**, in the note §8, §9, §11, §12 and in the zoo draft; plus a one-line rider on IV.9 so the mis-anchor stops propagating into future briefs.
5. **§5.3's stated displacement and |f_DH| ranges** (1.2·10⁻⁶ to 1.1·10⁻³ in ±30; |f_DH| 4.9·10⁻⁶ to 3.7·10⁻³), and the **cancellation argument** replacing "the main term dominates" as the reason the headlines stand.
6. **Citation hygiene:** Farmer and Steuding by section/page, not pdftotext line numbers (note §8, §11, §12; zoo SOURCE).
7. **Two small ones:** §6 Step 5's measure remark (two lines, earns the zoo's density clause); §7's "reproduces the 8-thread measurement exactly" → "is normalized at X₀".

Nothing in this list is a FAILS. Nothing in it moves a number that the rung computed. Items 1 and 2 must be made before the zoo entry is inserted; items 3–7 before the note is cited by a successor brief.

---

## §11 What I checked and did not check (standing order 5)

* **Read at the page, this job:** `results/c2-m6/BRIEF.md`; `PRICING.md` §3(a)–(d); `m6-rung1-note.md` §0–§12 in full; `zoo-IV19-proposed.md`; `SHARED.md`; `hashes.txt`; `verify/twisted_sum.rs` (the term-counting path, lines 214–244, 307–318, 325–418) and `verify/run_twisted_sums.sh`; `verify/out/dh_t85p7_L10.json`, `zeta_t85p7_L20*.json`; `verify/logs/dh_coeff_check.log`, `run_twisted_sums.log`; `results/c2-m2/verify/dh_negative_control.py` and its full run log; `results/c2-m2/campaign/dh_offline_scan.py`, `dh_control_new_heights.py`; `CAMPAIGN.md` §0–§1 and the DH control tables; `separation-note.md` §8; `results/ccm-dh-test/dh.py`, `finisher_weilext.py` `params`; `results/c3-r/m0-axiom-note.md` §6.1 (via the note's quotations and my own closed-form recomputation); `Zeta23/ExplicitFormula.lean` 60–90 and `Zeta23/WeilEF/Main.lean` 260–280; `BARRIER-ZOO.md` §0 (protocol items 1–7 and the binding rule), I.1, IV.6, IV.7 (all of lines 392–403), IV.9 with both 2026-09-16 riders, V.4, V.5; `results/full-map.md` line 203; `KICKSTART.md` item 10 (b), (c), (g), (l), (m), (n), (o); Farmer arXiv:2211.11671v4 §9.3 at p. 44 from my own `pdftotext` extraction; Steuding LNM 1877 p. 17 (Lemma 1.8(i) and the independence sentence, quoted verbatim in §4.3).
* **Computed independently (session scratchpad, ≈ 6 minutes of wall time plus two rebuilt Rust timing runs):** the ζ prime side, archimedean integral, pole terms and zero side at (85.7, 10) and (85.7, 20) and the prime side at (10⁶, 10); the Λ_DH recursion and its four witnesses at 30 digits, the Dirichlet-series identity at three points, the DH coefficient side and archimedean term at (85.7, 10); the true nonzero-coefficient count at three precisions; the record's on-line-zero recipe at dps 15 and its 40-digit refinement, and W_Z / W_{Z′} both ways at L = 10, 20, 86.907; the exact torus supremum, ℓ¹ norm, alignment defect, trivial bounds and PNT approximation at L = 10 (and the PNT value at L = 20); the cost-line rates and the class boundaries.
* **Not done:** no run at L = 20 for the DH coefficient side (the note's 3.4·10⁸-coefficient point is checked only through the note's own logs; my term-count finding is stated for L = 10 and flagged, not recomputed, at L = 20); no independent ζ prime side at L = 20 in my own code (the 25.6 M-term sum there is the note's Rust, rebuilt by me from its source; the archimedean, pole and zero sides at that point are mine); no re-run of the record's three DH scripts (that is the orchestrator's repair); no Lean edits and no Lean build; no Epstein instance; no commit.
* **Labeled inferences of mine:** the claim that the L = 20 DH term count is inflated by the same mechanism is an inference from the L = 10 measurement, labeled as such; the statement that sup_𝕋|Φ| dominates the signal for every δ < ½ is an asymptotic reading of two growth rates (e^{L/2} against e^{δL}), not a computation at every (δ, t); the reading of Turán 1960 is from Weber's citation of it at the page, not from Turán's paper, which is not on disk `[cited through Weber, arXiv:0806.3990 §3]`.

---

## §12 Traceability

| number | where it comes from |
|---|---|
| Z, A(0), A(v) checks, Λ sieve, ℓ¹, **P = 0.039608507012439213** | `own/core.py`, `own/zeta_prime.py`, `own/zeta_prime_L10.json` |
| **ARCH_ζ, ARCH_DH, Parseval 104.43888844430352**, convergence in h, H and node count | `own/arch.py`, `own/arch.json` (scipy complex digamma; mpmath spot checks at r = 85.7, 89.4, 10⁶) |
| **ĝ(i/2) + ĝ(−i/2) = −1.469578717·10⁻¹⁵ / +2.022621358·10⁻²¹** | `own/pole.py` (35 digits) |
| **κ, the four Λ_DH witnesses, P_DH = 0.33999546892892617, ℓ¹ = 3.29236846776, max |Λ_DH| = 157.796 at 19 656** | `own/dh_coeff.py`, `own/dh_coeff.json` |
| **the true nonzero count 8 562** at dps 30 / 60 / 100 against 15 442 / 15 512 / 15 766 by the `≠ 0` test | `own/dh_count.py` |
| the Dirichlet-series identity 1.4·10⁻¹⁶ / 4.3·10⁻¹² / 2.0·10⁻¹⁹ | inline mpmath run against `own/lamdh.pkl` |
| **the record recipe's 36 points, their 40-digit refinements, displacements, |f_DH| both ways, max |Z_DH| = 4.3·10⁻²²** | `own/rec_corr.py`, `own/rec_corr.json` |
| **ζ zero side 0.0038228665096753416 / 0.00086603423184801095 (112 zeros, 40 digits); W_{Z′} and W_Z recorded vs refined at L = 10, 20, 86.907; ratio 6.23731** | `own/fastB.py`, `own/zsides.py`, `own/zsides.json` |
| **sup_t P = 1.4201549249, sup_t(−P) = 1.4221742501, defect 2.381 %, 4√X a₀ = 9.867569, 2a₀ΣΛn^{−1/2} = 9.774123, PNT 1.4778 / 12.5425** | `own/sup_E.py`, `own/sup_E_L10.json` |
| **r_sieve = 2.049 ns, r_term = 176.8 ns, S = 4.95, A/B at L = 28.369, B/C at 31.632** | `own/out/z20_{th1_1,th1_2,so1_1,so1_2,th8,so8}.json` from my rebuild of `verify/twisted_sum.rs`; boundary solve inline with `mpmath.li` |
| Steuding Lemma 1.8(i) verbatim, p. 17; Weber UDT 4 (2009) Theorem 1 and (3.17)–(3.18); Turán 1960 Lemma p. 313 (through Weber); Farmer §9.3 p. 44 and §13 p. 64 | corpus read and online prior-art gate, this job; working notes in the session scratchpad (`novelty-E.md`) |
| the IV.7 grep (zero hits for Lindelöf / λ_max / Dirichlet polynomial / pointwise over `BARRIER-ZOO.md` lines 392–403) | inline grep, recorded in §6c |

*End of check. SHA-256 of this file is in `results/c2-m6/SHARED.md`'s Job-2 block and in the final report.*
