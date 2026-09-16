# check-O.md — Job 2, the independent Opus 5 dual check of Theorem M2 (the Gevrey-localized single-defect separation theorem)

**Written 2026-09-16 (Session 22, build stream `c2-m2-s22`, Job 2; standing orders 5 and 7).** Object of the check: `results/c2-m2/separation-note.md` (Job 1, Fable 5.1, 445 lines), its `SHARED.md`, `hashes.txt` and the six scripts, six logs, six JSON files and three auxiliary files under `results/c2-m2/verify/`, against the contract of `results/c2-m5/PRICING-next-unit.md` §2.2 as reproduced in `results/c2-m2/BRIEF.md` (with its Addendum), the Lean tree `~/rh-lean-work/zeta-23-lean-main`, `BARRIER-ZOO.md` (§0, II.4, IV.1, IV.9, V.4, V.5), `sources-extracted/tx_032.txt`, and the Hua–Yang paper `fetched-r3/r3s-24-…2608.16034v2…pdf` read at the page.

**Method.** Clauses 2–3 and 5–6 were re-derived line by line on paper, from the objects, before the author's proof text was compared with the derivation; Lemma G, clause 1's reflection condition, clause 4 and clauses 7–8 were re-derived the same way. Every load-bearing constant was recomputed in code written for this check (`opus_independent.py`, a deliberately different code path — closed forms plus mpmath quadrature, no reuse of the author's functions; transcript quoted inline below). Separately, all six of the author's scripts were re-run in an isolated scratch tree and diffed against the logs on disk. The nine `#print axioms` lines were re-run by me on my own scratch file outside the Lean tree. No file of the author's was edited; no file inside the Lean tree was created, modified or rebuilt (verified by `find` — no file under `~/rh-lean-work/zeta-23-lean-main`, including the `.lake` build cache, has an mtime inside the last twelve hours). Nothing was committed by this job.

**Integrity of the deliverable.** All 31 SHA-256 lines of `hashes.txt` verify (`shasum -a 256 -c`: 31/31 OK, 0 failures). The Hua–Yang PDF hashes to `465a5c6dc3d6b780f493843b54ca9474b7dedbd83c208f6ad89196a76537a09d`, matching the note's §11 and §15 record byte for byte.

**Reproduction.** All six scripts reproduce **digit for digit**. The six `_run.log` files are byte-identical to the author's after stripping the timing lines (`real`/`user`/`sys`/`exit`/`done in`); the six `_out.json` files are byte-identical after removing the `runtime_s` key, including `dh_negative_control_out.json`, whose run took 16 min 18 s here against the author's 16 min 14 s. The heavy DH control was run once, as instructed; at most one heavy process at a time.

---

**HEADLINE.** **The theorem stands. All eight clauses CLOSE.** Every constant re-derives: κ₋ = κ_∞ = 1.4808831774 (a closed form), κ₊ = 1.5309456774, c_B = 2/√(72e) = 0.1429606475, C_B = e²/Z = 33.2845, b₁ = 8.6461283 at η* = 4.67274 (certified ≤ 8.6981), R₀ = 81 at L₀ = 50 with F̃(50) = −0.133397, the reflection constant 21 with margin 0.717 nats at L = 50, L₁ = 17.927, ℓ_R and the clause-6 balance. The nine deviations D1–D9 are **all UPHELD** as deviations; **one claim inside D3 is OVERRULED** (the reflection condition is *not* "numerically vacuous for every t ≥ 3"), and **one arithmetic value inside D9 is corrected** (the reflected double contributes 8t²B̂(2tL)², not 16t²B̂(2tL)²). Clause 5 — the one live failure mode — holds uniformly over depth ½, as the note claims; the §2.9 failure branch does not fire. The DH negative control ran zero-side, FIRED at the theorem's own bandwidth (ratio 6.24 to the bound, 17.9 at L = 100), and the positive control stayed silent (ζ: 2.09·10⁻⁷ at L*, four orders below the clause-4 noise bound and twelve below the DH signal); neither of the author's two caveats undermines it. The standing-order-7 novelty check confirms the note's own reduction of its novelty claim: Hua–Yang §9 has the *mechanism* of Lemma G and of clause 5's shell summation in print, with unspecified constants, at a height-proportional radius, for family-averaged second-order trace data; it has no single-defect separation statement and no single-zero or detection language at all (my greps: zero hits). **No clause is FIX-FIRST or FAILS.** §12 lists eleven exact wording corrections the record needs; three of them (§12.1, §12.2, §12.3) are misstatements a referee would call out and should be carried into the note's corrections section before the referees run. None touches a proof or moves a constant.

---

## §1 What was re-run, and what the Lean tree says

### §1.1 The six scripts

Copied to an isolated scratch tree (with `results/ccm-dh-test` symlinked so `dh_negative_control.py`'s `../../ccm-dh-test` resolves) and run sequentially, one process at a time:

```
gevrey_edge_law_rerun.py   LOGS IDENTICAL   JSON IDENTICAL (modulo runtime_s)
b1_constant.py             LOGS IDENTICAL   JSON IDENTICAL (modulo runtime_s)
edge_law_two_sided.py      LOGS IDENTICAL   JSON IDENTICAL (modulo runtime_s)
lemma_G_constants.py       LOGS IDENTICAL   JSON IDENTICAL (modulo runtime_s)
four_point_accounting.py   LOGS IDENTICAL   JSON IDENTICAL (modulo runtime_s)
dh_negative_control.py     LOGS IDENTICAL   JSON IDENTICAL (modulo runtime_s)
```

The author's `run_all.log` records an `exit=143` on the first `dh_negative_control.py` attempt (a kill, not a failure of the computation) and a second `lemma_G_constants.py` run; `run_rest.sh` re-ran both to completion. The logs and JSON on disk are the second, complete run. That is recorded in the log files themselves and needs no correction, but it is worth the record's knowing (§12.13).

### §1.2 `#print axioms`, run by me

Scratch file `axioms_opus_check.lean` **outside** the tree, compiled with `lake env lean` from `~/rh-lean-work/zeta-23-lean-main` against the existing build; toolchain `leanprover/lean4:v4.33.0-rc2`; 31 s wall. All nine theorems:

```
'Zeta23.EF.prop_EF_of_lit'                    depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.EF.paperFT_weilTest'                  depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.WeilEF.EF_lit_zetaZeroConfig'         depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.WeilEF.zeta_local_zero_count_explicit' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.Taper.gevrey_expNegInvGlue'           depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.Taper.abs_iteratedDeriv_theta_le'     depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.Taper.gevreyProfile_rhoTwo'           depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.Taper.integral_abs_iteratedDeriv_phi_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.Params.gevreyPhiBound_of_profile'     depends on axioms: [propext, Classical.choice, Quot.sound]
```

Confirmed, independently of `verify/print_axioms_run.log`. KICKSTART 10(f) is satisfied: after my run, no file under the tree — source or `.lake` build artifact — has an mtime inside the last twelve hours, so nothing was created, modified or rebuilt. (The tree is not itself a git checkout, so `git status` is not the instrument here; `find . -type f -newermt '-12 hours'` is, and it returns nothing.)

### §1.3 The cited Lean lines, read this session

Every name the note cites **exists under the stated name** — the brief's stop condition (d) does not fire. The line numbers are right for eleven of fourteen citations and drift for three:

| cited | actual | verdict |
|---|---|---|
| `paperFT` 44 | 44 | ✓ |
| `gammaOf` 105, `reflect` 108 | 105, 108 | ✓ |
| `ZeroConfig` 119–130 | `structure` at 120, fields to 133 | ✓ (range) |
| `Wsummand`/`W` 164–170 | 164, 170 | ✓ |
| `tilde`/`weilTest` 47–52 | 48, 52 | ✓ |
| `paperFT_weilTest` 188–191 | 189 | ✓ |
| `gammaBracket` 64, `literatureRHS` 69–73, `EF_lit` 81–84 | 64, 70, 81 | ✓ |
| `prop_EF_of_lit` 699–711 | docstring 699, theorem 703 | ✓ |
| `EF_lit_zetaZeroConfig` 268–270 | 270 | ✓ |
| `zeta_local_zero_count_explicit` 924–927 | docstring 924, theorem 926 | ✓ |
| `GevreyProfile` 45–52 | `structure` at 52, `bound` field at 58 | **drift** (§12.12) |
| `theta` line 55 | **61** | **drift** (§12.12) |
| `gevrey_expNegInvGlue` 183–185 | docstring 183, theorem 185 | ✓ |
| `abs_iteratedDeriv_theta_le` 282–284 | docstring 280, lemma 281 | ✓ (off by one) |
| `gb_mul_gb_le` 262–275 | **248** | **drift** (§12.12) |
| `gevreyProfile_rhoTwo` 393 | **401** | **drift** (§12.12) |
| `integral_abs_iteratedDeriv_phi_le` 202–205, `gevreyPhiBound_of_profile` 237 | 203, 237 | ✓ |
| `GevreyPhiBound` 17–27 | 19 | ✓ |

The quoted **text** is verbatim correct in every case, including the three that drift. One content omission: `prop_EF_of_lit`'s conclusion is a **three**-fold conjunction (`Summable ∧ Integrable ∧ W = ∫`); the note quotes two of the three (§12.12).

The structural facts the note asserts about `ZeroConfig` are right and worth stating for the referees: the Lean structure requires `reflect ρ = 1 − conj ρ` invariance with equal multiplicities and local finiteness in the ordinate, and does **not** require invariance under `ρ ↦ conj ρ`. In γ-coordinates, with `gammaOf ρ = (ρ − ½)/i` so that ρ = β + iτ ↦ γ = τ − i(β − ½):

* `reflect ρ = 1 − conj ρ` ↦ γ ↦ conj γ. (Check: 1 − β + iτ ↦ (½ − β)/i + τ = τ + i(β − ½) = conj γ.)
* `ρ ↦ conj ρ` ↦ γ ↦ −conj γ. (Check: β − iτ ↦ (β − ½)/i − τ = −τ − i(β − ½) = −conj γ.)
* The two together generate γ ↦ −γ.

So the note's §0.1 dictionary is exactly right, δ := |Im γ| = |Re ρ − ½| is the depth, and the strip 0 ≤ β ≤ 1 is |Im γ| ≤ ½.

---

## §2 Accounting point (i) — the four points, re-derived

`Zeta23/Defs.lean` 164–170 defines the summand as `m_ρ · h_f(γ_ρ) · conj(h_g(conj γ_ρ))`. With f = g, the term of a point γ is h_f(γ)·conj(h_f(conj γ)). From (0.1), h_f(r) = (r − t)B̂(L(r − t)) for every complex r (the integration by parts is correct: i∫(B_L)′e^{i(r−t)u}du = i·(−i(r−t))∫B_Le^{i(r−t)u}du, no boundary terms since B_L ∈ C_c^∞).

* B̂(−iδL) = ∫B(v)e^{i(−iδL)v}dv = ∫B(v)e^{δLv}dv = c(δL), real, since B is even. Likewise B̂(iδL) = c(δL).
* γ = t − iδ: h_f(γ) = (−iδ)c, conj γ = t + iδ, h_f(conj γ) = (iδ)c, conj of that is (−iδ)c. Term = (−iδc)(−iδc) = **−δ²c²**.
* γ = t + iδ: h_f(γ) = (iδ)c, conj γ = t − iδ, h_f(conj γ) = (−iδ)c, conj = (iδ)c. Term = (iδc)(iδc) = **−δ²c²**.
* **The pair at +t contributes −2δ²c(δL)²: two zeros, −δ²c² each.**

So the contract's main term is correct, the R1 factor-2 trap (`confinement-note.md` D1) is avoided, and the brief's stop condition (c) does not fire. **The note's §0.2 is confirmed.**

My own quadrature, at t = 30, δ = 0.3, L = 40, computing h_f by integrating i(B_L)′(u)e^{−itu}e^{iru} directly (`opus_independent.py` (6)):

```
(6a) h_f(t-i d) = (-4.1468708e-49 - 2.6425284j)  vs  -i d c(dL) = (0.0 - 2.6425284j)
(6c) the +t PAIR contributes (-13.96591261 + 0.0j) ; -2 d^2 c^2 = -13.96591261 ; rel err 0.00e+00
(6d) the -t pair E_- = (-1.09371e-25) ; |E_-|/(2 d^2 c^2) = 7.831e-27 ; e^{-L} = 4.248e-18
```

identical to `four_point_accounting_run.log` (2) to every printed digit.

The transcript's ledger is quoted faithfully. `sources-extracted/tx_032.txt` lines 17–23 read, verbatim: "(i) The pair γ0, ¯γ0: … is real; the pair contributes 2 Re[(−iδ)(−iδ)] c2 = −2δ2c2 ≤−2δ2 (times m0 ≥1). (ii) The reflected pair at −t0: |h(−t0 ∓iδ)| ≈2t0 | ˆBL(−2t0 ∓iδ)|, superpolynomially small in Lt0 — negligible." The recorded gap the note attributes to the transcript is at lines 50–51, also verbatim: "Recorded honestly: interference from unknown off-line zeros is not controlled by this argument."

## §3 Accounting point (ii) — the sign and the Hermitian convention

Three things, all confirmed.

1. **The sign is not a convention.** It is (−i)² = i² = −1, i.e. (r − t)² evaluated at r − t = ∓iδ. On a real point the term is m_ρ|h_f(γ)|² ≥ 0. So an on-line configuration has W_Z(f) ≥ 0 for every test and a defect is the only source of negative terms — the note's §0.3 claim, verified above and in the log's line (3), where the eight-point instance gives W_Z = −13.9655967426 with imaginary part exactly 0.0.
2. **Realness on a conjugation-invariant multiset.** Term(conj γ) = h_f(conj γ)·conj(h_f(γ)) = conj[Term(γ)], so pairing γ with conj γ makes the sum real. Confirmed.
3. **g is Hermitian, not real (D1).** g(x) = ∫f(y)conj(f(y − x))dy with f = i(B_L)′e^{−itu} gives g(x) = e^{−itx}a(x), a := the autocorrelation of the real odd function (B_L)′, which is real and even; hence g(−x) = conj g(x) and Im g ≢ 0. The log's (4) measures exactly that: `max|g(-x) - conj g(x)| = 0.0 (Hermitian), max|Im g(x)| = 0.000249 (NOT real)`. Nothing downstream needs g real: the Lean `EF_lit` takes `k : ℝ → ℂ` with only `ContDiff ℝ 2` and `HasCompactSupport`, and `paperFT_weilTest` is stated for all complex z. **D1 UPHELD.**

A two-point instance of my own, over and above the note's eight-point one: take Z = {t − iδ, t + iδ} alone (not reflection-invariant, so not a legal configuration, but a legitimate test of the summand). Its two terms are −δ²c² each, both real and negative, summing to −2δ²c² — which is the identity §0.2 asserts and my (6c) confirms to zero relative error.

---

## §4 Lemma G — the exponent bookkeeping, re-derived

This is the place the brief flags: *is the contract's B equal to θ^{1/4}, and is what the note claims about it right?* Yes, on both counts.

### §4.1 B is θ^{1/4}, and that is why the pricing's c_B is wrong

With x := v + ½, 1 − 4v² = (1 − 2v)(1 + 2v) = 4x(1 − x), so

B_raw(v) = exp(−1/(4x(1 − x))) = exp(−1/(4x))·exp(−1/(4(1 − x))) = g(4x)g(4(1 − x)) = g(4v + 2)g(2 − 4v),

using 1/(4x(1−x)) = 1/(4x) + 1/(4(1−x)). And θ(x) = g(x)g(1 − x) = exp(−1/(x(1−x))), so **B_raw(v) = θ(v + ½)^{1/4}** exactly. My grid check: `max |B_raw(v) − θ(v+½)^{1/4}| = 1.435e-41` on 99 points. **Lemma G0 confirmed; D2's premise confirmed.**

A quarter-power does not transfer a derivative bound, so the pricing's inference — take the Lean `abs_iteratedDeriv_theta_le` constant (36/e) and read off c_B = 2/(e√(36/e)) = 1/(3√e) = 0.202177 — is not available for B. The note's route (factorize, chain rule, Leibniz) is the right one, and it costs a factor 4^k per factor. **The constant that the Lean numbers actually give for the contract's bump is c_B = 2/√(72e) = 0.1429606475.** **D2 UPHELD.** (The note's D2 paragraph prints "0.14298"; §2 prints 0.142961 and §15 prints 0.14296. The exact value is 0.14296065. §12.6.)

### §4.2 Lemma G1, step by step

(i) *Affine chain rule.* d^k/dv^k[g(av + b)] = a^k g^{(k)}(av + b); with a = ±4 and the Lean (P1) bound |g^{(k)}| ≤ (18/e)^k k^{2k} (k ≥ 1, all real x), each factor obeys 4^k(18/e)^k k^{2k} = A₁^k k^{2k} with **A₁ = 72/e = 26.48732**. For k = 0, 0 ≤ g ≤ 1. Correct.

(ii) *Leibniz.* |B_raw^{(k)}| ≤ A₁^k Σ_{i=0}^k C(k,i)[i^i(k−i)^{k−i}]².

(iii) *The improvement over the on-disk route.* The note splits each term as [C(k,i)i^i(k−i)^{k−i}]·[i^i(k−i)^{k−i}] and bounds the first bracket by k^k (it is one term of the binomial expansion of k^k = (i + (k−i))^k, all of whose terms are nonnegative) and the second by k^i·k^{k−i} = k^k. Each of the k + 1 terms is therefore ≤ k^{2k}, and Σ ≤ (k+1)k^{2k}. **This is correct and it is elementary.** I verified the key inequality C(k,i)i^i(k−i)^{k−i} ≤ k^k exhaustively for 1 ≤ k ≤ 39 and every i: **True**. The Lean proof of `abs_iteratedDeriv_theta_le` instead bounds each product by (18/e)^k k^{2k} (`gb_mul_gb_le`) and sums the binomials to 2^k, which would give A = 144/e and c_B = 1/(6√e) = 0.101088; the note's step (iii) recovers a factor √2 in the decay constant. The note says so, and says exactly where.

Hence ‖B_raw^{(k)}‖₁ ≤ (k+1)A₁^k k^{2k} (support length 1; B_raw is C^∞ everywhere, so no boundary issue). Numerically, max over k ≤ 6 of |B_raw^{(k)}|/((k+1)A₁^k k^{2k}) = **0.0299** — the bound holds with two orders to spare at small k, as expected from Cauchy's estimate on |z − x| = x/2.

### §4.3 Lemma G

For η ≠ 0 and k ≥ 1, k integrations by parts give |B̂(η)| ≤ ‖B^{(k)}‖₁/|η|^k ≤ (k+1)A₁^k k^{2k}/(Z|η|^k); also |B̂| ≤ ∫B = 1. Put κ := √(|η|/A₁)/e.

* κ ≥ 1, k := ⌊κ⌋ ≥ 1: log(A₁^k k^{2k}/|η|^k) = k(log A₁ + 2 log k − log|η|) ≤ k(log A₁ + 2 log κ − log|η|) = −2k, since log A₁ + 2 log κ − log|η| = log A₁ + log(|η|/A₁) − 2 − log|η| = −2 exactly. And −2k ≤ −2(κ − 1). With k + 1 ≤ κ + 1: |B̂(η)| ≤ (e²/Z)(1 + κ)e^{−2κ}. Since 2κ = 2√|η|/(e√A₁) = c_B√|η| with c_B = 2/(e√(72/e)) = **2/√(72e)**, this is (G1) with **C_B = e²/Z = 33.2845**.
* κ < 1: |B̂| ≤ 1 while (G1)'s right side is ≥ (e²/Z)e^{−2} = 1/Z = 4.5045 > 1. Correct. (Sharper: the right side is ≥ 2/Z = 9.009 there, since (1+κ)e^{−2κ} is decreasing. Immaterial.)

(G2): (1 + s/2)e^{−s/8} has its maximum at s = 6, value 4e^{−3/4}, so (1 + s/2)e^{−s} ≤ 4e^{−3/4}e^{−7s/8}; hence c_B′ = (7/8)c_B = 0.12509057 and C_B′ = 4e^{−3/4}C_B = **62.889938** (the note prints 62.890).

Complex case: for ζ = ξ − iη′, |e^{iζv}| = e^{η′v} ≤ e^{|η′|/2} on the support, and the same k integrations by parts give |B̂(ζ)| ≤ e^{|η′|/2}‖B^{(k)}‖₁/|ζ|^k ≤ e^{|η′|/2}‖B^{(k)}‖₁/|ξ|^k, so choosing k from |ξ| gives e^{|η′|/2}G(|ξ|). **This is the step the whole theorem rests on, and it is correct.** Monotonicity of G: in s = c_B√η, d/ds[(1+s/2)e^{−s}] = −(½ + s/2)e^{−s} < 0.

Numerically, min over η ∈ {0, 1, 4, 16, 64, 256, 1024, 4096, 16384} of G(η)/|B̂(η)| = **31.53** — the bound holds with a factor of about 10^{1.5} throughout, as the note's §2 numerical record states.

**Lemma G CLOSES.** The honest gap to the numerical decay rate (≈ 0.85 per √η against 0.143) is stated by the note and is the price of three generous steps, exactly as the note says: the Lean Cauchy estimate, the 4^k, and Leibniz. The note also correctly records (§14) that a direct Cauchy estimate on B's own holomorphic extension would improve every downstream constant, and that it was not attempted because the brief asked for the constant the Lean bounds give. That is the right call and it is declared.

---

## §5 Clause 2 (the two-sided edge law) — re-derived line by line

### §5.1 The Laplace representation

c(λ) = ∫B(v)cosh(λv)dv = ∫B(v)e^{λv}dv (B even). Substituting v = ½ − s on s ∈ (0,1), and 1 − 4v² = 4s(1 − s):

**c(λ) = e^{λ/2}I(λ)/Z, I(λ) = ∫_0^1 exp(−λs − 1/(4s(1−s)))ds.** ✓ (3.1).

Writing 1/(4s(1−s)) = 1/(4s) + ¼[1 + s + s²/(1−s)] (from 1/(1−s) = 1 + s + s²/(1−s), which is an identity) gives, with μ := λ + ¼,

**I(λ) = e^{−1/4}∫_0^1 e^{−μs − 1/(4s)}e^{−s²/(4(1−s))}ds.** ✓ (3.2).

My independent check of (3.1) against the definition: at λ = 25, both give 732.417149524 with relative difference 4.6·10⁻⁴¹; at λ = 60, 965890092.689 with 1.4·10⁻⁴⁰.

J(μ) = μ^{−1/2}K₁(√μ) and J₂(μ) = ¼μ^{−3/2}K₃(√μ) with K_ν(x) = ∫_0^∞ e^{−x cosh θ}cosh(νθ)dθ: the substitutions s = σ/√μ then σ = ½e^θ give σ + 1/(4σ) = cosh θ, dσ = ½e^θdθ, and ½∫_ℝ e^{−x cosh θ}e^θdθ = ∫_0^∞ e^{−x cosh θ}cosh θ dθ = K₁(x) (the sinh half is odd); for J₂, σ²dσ = ⅛e^{3θ}dθ and ⅛∫_ℝ e^{−x cosh θ}e^{3θ}dθ = ¼K₃(x). ✓ (3.3). The log's line (0) checks all of these against `mpmath.besselk` to 12 digits at three values.

### §5.2 Lemma K

cosh θ = 1 + 2sinh²(θ/2); y = sinh(θ/2), dθ = 2dy/√(1+y²) gives K₁(x) = 2e^{−x}∫_0^∞ e^{−2xy²}(1+2y²)(1+y²)^{−1/2}dy. The two envelope claims:

* **Upper:** (1+2y²)(1+y²)^{−1/2} ≤ 1 + (3/2)y², i.e. (1+2y²)² ≤ (1+y²)(1+(3/2)y²)². LHS = 1 + 4y² + 4y⁴; RHS = 1 + 4y² + (21/4)y⁴ + (9/4)y⁶. ✓
* **Lower:** (1+y²)^{−1/2} ≥ 1 − y²/2. For y² ≤ 3 because (1−y²/2)²(1+y²) = 1 − (3/4)y⁴ + y⁶/4 ≤ 1 there (arithmetic checked: (1 − y² + y⁴/4)(1+y²) = 1 − (3/4)y⁴ + y⁶/4; ≤ 1 iff y² ≤ 3); trivially for y² > 2 where the left factor is negative. The two ranges cover ℝ₊. Then (1+2y²)(1−y²/2) = 1 + (3/2)y² − y⁴. ✓

Gaussian moments ∫_0^∞ y^{2n}e^{−2xy²}dy = ½√(π/(2x))(2n−1)!!/(4x)^n (n = 0,1,2,3 giving 1, 1/(4x), 3/(16x²), 15/(64x³)) — verified. Hence

√(π/(2x))e^{−x}(1 + 3/(8x) − 3/(16x²)) ≤ K₁(x) ≤ √(π/(2x))e^{−x}(1 + 3/(8x)). ✓

For K₃: cosh 3θ = 4cosh³θ − 3cosh θ = 4(1+2y²)³ − 3(1+2y²) = 1 + 18y² + 48y⁴ + 32y⁶ (expansion checked term by term), and dropping (1+y²)^{−1/2} ≤ 1 gives K₃(x) ≤ √(π/(2x))e^{−x}(1 + 4.5/x + 9/x² + 7.5/x³). ✓ **Lemma K is correct**, and the log's line (1) confirms the three ratios on x ∈ [5, 60] (K₁/upper ∈ [0.9962, 1), K₁/lower ∈ (1, 1.0033], K₃/upper ∈ [0.946, 1)).

### §5.3 The upper bound

Drop e^{−s²/(4(1−s))} ≤ 1, extend to (0, ∞): I(λ) ≤ e^{−1/4}J(μ) ≤ e^{−1/4}√(π/2)μ^{−3/4}e^{−√μ}(1 + 3/(8√μ)). With κ(λ) := log c(λ) − λ/2 + √λ + ¾log λ and κ_∞ := log(√(π/2)e^{−1/4}/Z):

κ(λ) ≤ κ_∞ + (√λ − √μ) + ¾log(λ/μ) + log(1 + 3/(8√μ)).

√μ ≥ √λ(1 + ε/2 − ε²/8) with ε = 1/(4λ) gives √λ − √μ ≤ −1/(8√λ) + 1/(128λ^{3/2}); log(λ/μ) ≤ 0; log(1 + 3/(8√μ)) ≤ 3/(8√λ). Sum: **κ(λ) ≤ κ_∞ + 1/(4√λ) + 1/(128λ^{3/2})**, decreasing, equal at λ = 25 to κ_∞ + 0.05 + 0.0000625 = **1.5309457**. ✓ κ₊ = 1.53095.

### §5.4 The lower bound

Restrict to s ∈ (0, ½] and use e^{−z} ≥ 1 − z with z = s²/(4(1−s)) ≤ s²/2 there:

I(λ) ≥ e^{−1/4}[J(μ) − ∫_{1/2}^∞ e^{−μs}ds − ½J₂(μ)] = e^{−1/4}[μ^{−1/2}K₁(√μ) − e^{−μ/2}/μ − ⅛μ^{−3/2}K₃(√μ)].

Dividing by the main factor M := √(π/2)μ^{−3/4}e^{−√μ}: the first term is ≥ 1 + 3/(8√μ) − 3/(16μ); the second is E₁(λ) = √(2/π)μ^{−1/4}e^{√μ−μ/2}; the third is ≤ E₂(λ) = (1/(8μ))(1 + 4.5/√μ + 9/μ + 7.5/μ^{3/2}). Each of the three ratios is what the note states — I recomputed all three. Hence

κ(λ) ≥ κ_∞ + (√λ − √μ) + ¾log(λ/μ) + log(1 + u), u := 3/(8√μ) − 3/(16μ) − E₁ − E₂,

with √λ − √μ ≥ −1/(8√λ) (from √(1+ε) ≤ 1 + ε/2) and ¾log(λ/μ) ≥ −3/(16λ). The residual D(λ) := −1/(8√λ) − 3/(16λ) + log(1 + u) must be ≥ 0 for λ ≥ 25. The note's chain, re-verified constant by constant at λ ≥ 25:

* u ≤ 3/(8·5) = 0.075, so log(1+u) ≥ u − u²/2 ≥ 0.9625u ✓;
* √μ ≤ 1.005√λ (from √(1+1/(4λ)) ≤ 1 + 1/(8λ) ≤ 1.005 at λ ≥ 25), so 3/(8√μ) ≥ 0.373134/√λ ✓ (note: 0.3731);
* 3/(16μ) ≤ 3/(16λ) ✓; E₂ ≤ (1/(8λ))(1 + 0.9 + 0.36 + 0.06) = 0.2895/λ ≤ 0.29/λ ✓ (each of the three ratios checked at μ ≥ 25.25);
* D(λ) ≥ 0.9625(0.373134/√λ − 0.1875/λ − 0.29/λ) − 0.125/√λ − 0.1875/λ − 0.9625E₁ = **0.234141/√λ − 0.647094/λ − 0.9625E₁** ✓ (note: 0.234/√λ − 0.647/λ);
* (0.234√λ − 0.647)/λ ≥ 0.52/λ at λ ≥ 25 and grows ✓;
* λE₁(λ) ≤ 25E₁(25) = 0.0045 ✓. (The note justifies this by "E₁(λ) ≤ 0.8e^{−1.51√λ} and λe^{−1.51√λ} is decreasing", which gives the weaker 0.8·25e^{−7.55} = 0.0105 — still ample. The direct route is cleaner and is available: d/dλ log(λE₁) = 1/λ − 1/(4μ) + 1/(2√μ) − ½ < 0 for λ ≥ 25, so λE₁ is decreasing outright. §12.10, a strengthening, not a correction: **either route gives D(λ) > 0**, since 0.52 − 0.9625·0.0105 = 0.510 > 0.)

So D(λ) ≥ (0.52 − 0.0044)/λ > 0 and **κ(λ) ≥ κ_∞ for every λ ≥ 25: κ₋ = κ_∞ = 1.4808831774**, a closed form and the true asymptotic constant. Also u > 0 throughout (0.373/√λ dominates 0.4775/λ + E₁ at λ ≥ 25), which log(1+u) needs.

### §5.5 Numerical confirmation, independent

My own quadrature of c(λ) via (3.1) with nodes resolved at the saddle s* = 1/(2√λ):

```
kappa_- = 1.4808831774  kappa_+ = 1.5309456774
  lam=25       kappa=1.510507097   in-band=True
  lam=100      kappa=1.501267878   in-band=True
  lam=400      kappa=1.492264973   in-band=True
  lam=2500     kappa=1.485706805   in-band=True
  lam=10000    kappa=1.483339264   in-band=True
  lam=100000   kappa=1.482371994   in-band=True
```

matching `edge_law_two_sided_run.log` (2) at every shared λ (1.5105071, 1.5012679, 1.492265, 1.4857068, 1.4833393), monotonically decreasing toward κ_∞. (At λ = 10⁶ my quadrature loses the value to underflow — an artifact of my node choice, not a violation; the proof covers every λ ≥ 25 regardless.)

**CLAUSE 2 CLOSES.** The note proves a two-sided law; it does not fit one. **D6 UPHELD**: the pricing's 1.515 is the constant of a two-parameter least-squares fit (slope 1.0012, reproduced in the log), the proved band [1.4809, 1.5310] contains every exact value, and |κ± − 1.515| ≤ 0.035 ≤ 0.1, so the brief's stop condition (a) does not fire and λ₀ = 25 stands.

## §6 Clause 3 (the slack) — re-derived

c(λ)² ≥ e^{λ}exp(−2√λ − (3/2)log λ + 2κ_∞), so c(λ)² ≥ e^{λ/2} follows from m(λ) := λ/2 − 2√λ − (3/2)log λ + 2κ_∞ ≥ 0.

m(25) = 12.5 − 10 − 1.5·3.2188758 + 2·1.4808832 = 12.5 − 10 − 4.8283137 + 2.9617664 = **0.63345262** (my value; the log prints 0.633453), and m′(λ) = ½ − 1/√λ − 3/(2λ) = 0.24 > 0 at λ = 25 and increasing. Proved margin e^{m(25)} = **1.8841** against the computed ratio c(25)²/e^{12.5} = **1.99911**. Both reproduce the log exactly. The note's record that the proved inequality first holds at λ = 23 while the contract fixes λ₀ = 25 is in the log and is correct.

**CLAUSE 3 CLOSES.** The reading the note attaches — that the Gevrey loss e^{−√λ}λ^{−3/4} is absorbed by the slack (1 − c₀)λ = λ/2 from λ = 25 on, which is repair 2's content against C2 line 70's inconsistency — is exactly what the two displayed facts say.

---

## §7 Clause 5 (out-window contamination, uniform over depth ½) — re-derived, and R₀ recomputed

This is the clause the pricing named as the one live failure mode. **It does not fail.**

### §7.1 Part (a) — the pointwise bound, and where the uniformity comes from

For γ = x − iy with |y| ≤ ½ and u := |x − t|: h_f(γ) = (γ − t)B̂(L(γ − t)), with |γ − t| = √(u² + y²) ≤ √(u² + ¼) ≤ u + ½ and L(γ − t) = L(x − t) − iLy, so Lemma G's complex case gives |B̂(L(γ − t))| ≤ e^{L|y|/2}G(Lu) ≤ e^{L/4}G(Lu). The same holds at conj γ = x + iy (same u, same |y|). Multiplying:

|h_f(γ)·conj(h_f(conj γ))| ≤ (u + ½)²·e^{L/2}·G(Lu)².

**Correct.** And the structural point the note makes is the right one and is worth the referees' attention: the depth enters *only* through e^{L|y|/2} ≤ e^{L/4} per factor, i.e. through a factor e^{L/2} that does not depend on u at all, while the decay factor is exp(−2c_B√(Lu)) ≤ exp(−2c_B√R₀·L) at u ≥ R₀L — an exponential in L with coefficient 2c_B√81 = 2.573, which beats ½ + ¼ + 1 = 1.75 with room. That is exactly why Gevrey decay does what the transcript's polynomial decay could not: ‖(B_Le^{yu})‴‖₁/|x|³ ~ e^{L/4}/|x|³ is ≥ 1 for |x| ≤ e^{L/12}, so the polynomial route needs an exclusion zone exponential in L, and the transcript records exactly that fallback (tx_032 line 46: "no off-line zeros with |Re γ − t₀| ≤ R_L := e^{L/12}L, or global isolation"). **The uniformity over depth is real and the mechanism is identified correctly.**

### §7.2 Part (b) — the shells, the absorption, and F̃

Reconstructed from the note's text (not from the author's code) and then implemented in my own script:

1. A point with |Re γ − t| ≥ R lies in a shell k ≤ u < k+1 with k ≥ ⌊R⌋ ≥ R − 1 =: u₀. The shell lies in [t+k, t+k+1) ∪ (t−k−1, t−k], each of length 1, each inside a unit-radius window of the class definition centered at t ± (k+½); so the count is ≤ 2C₁log(3 + |t ± (k+½)|) ≤ 2C₁log(3.5 + t + k). ✓ (Both centers: on the left |t − k − ½| ≤ t + k + ½.)
2. log(3.5 + t + k) ≤ log(3.5 + t) + k, since log(1 + k/(3.5+t)) ≤ k/(3.5+t) ≤ k for t ≥ 3. ✓
3. S_Z ≤ 2C₁e^{L/2}[log(3.5+t)Σ₂ + Σ₃], Σ_m := Σ_{k≥u₀}(k + 3/2)^m G(Lk)², using k(k+3/2)² ≤ (k+3/2)³. ✓
4. Absorption: 2C₁ ≤ e^{L/8}/b₁ from L/8 ≥ log(2b₁C₁); log(3.5+t) ≤ 1.05log(3+t) ≤ 1.05e^{L/8} from L/8 ≥ log log(3+t). Both follow from the single hypothesis L ≥ 8(log log(3+t) + log(2b₁C₁)) because both summands are positive. The 1.05 covers log(3.5+t)/log(3+t) ≤ log 6.5/log 6 = 1.0447 at t = 3, decreasing. ✓
5. Hence S_Z ≤ (e^{3L/4}/b₁)(1.05Σ₂ + Σ₃). (The Σ₃ term actually carries only e^{5L/8}; writing e^{3L/4} in front of both is a safe over-estimate. ✓)
6. φ_m(u) := u^m(1 + (c_B/2)√(Lu))²e^{−2c_B√(Lu)} is decreasing on [u₀, ∞): (log φ_m)′(u) ≤ (m+1)/u − c_B√L/√u < 0 for u > (m+1)²/(c_B²L), and u₀ ≥ 81·50 − 1 = 4049 ≫ 16/(c_B²·50) = 15.66. ✓ So Σ_m ≤ β^mC_B²[φ_m(u₀) + ∫_{u₀}^∞φ_m], β = 1 + 3/(2u₀).
7. ∫_{u₀}^∞φ_m = (2/L^{m+1})∫_{s₀}^∞ s^{2m+1}(1 + (c_B/2)s)²e^{−2c_Bs}ds, s₀ = √(Lu₀), a combination of incomplete-gamma integrals ∫_{s₀}^∞s^ne^{−as}ds = e^{−as₀}Σ_{j=0}^n (n!/j!)s₀^j a^{−(n+1−j)} with a = 2c_B and n = 2m+1, 2m+2, 2m+3, coefficients 1, c_B, c_B²/4. ✓ (Substitution u = s²/L, du = 2s ds/L, checked.)
8. Relaxations: s₀ = √(L(R₀L − 1)) ≥ √R₀·L − 1/√R₀ (from √(1−ε) ≥ 1−ε), so e^{−2c_Bs₀} ≤ e^{2c_B/√R₀}e^{−2c_B√R₀·L}; and u₀ ≤ R₀L, s₀ ≤ √R₀·L in every polynomial factor; β ≤ 1 + 3/(2(R₀L₀ − 1)). ✓
9. S_Z ≤ e^{2c_B/√R₀}e^{(3/4 − 2c_B√R₀)L}P(L)/b₁, and S_Z ≤ e^{−L} iff F̃(L) := (7/4 − 2c_B√R₀)L + 2c_B/√R₀ + log(P(L)/b₁) ≤ 0. ✓
10. (log P)′ ≤ 5/L, so F̃ is decreasing on [5/(2c_B√R₀ − 7/4), ∞) = [6.073, ∞) at R₀ = 81. Hence **F̃(50) ≤ 0 plus 6.073 ≤ 50 gives S_Z ≤ e^{−L} for every L ≥ 50**. ✓

My independent implementation of steps 6–10:

```
(3a) F~(50) at R0=81, b1=8.6981: -0.133397 ; at R0=80.5: 0.237029 ; at R0=80: 0.608523
(3c) decrease threshold 5/(2 c_B sqrt R0 - 7/4) at R0=81: 6.0732
     F~ at L = 60, 100, 403, 1000, 1e4: -7.4768, -37.898, -280.44, -767.41, -8165.5
(3e) my least R0 (step 1/2, L0=50) = 81.0
(3d) (3/(4 c_B))^2 = 27.5226 ; (7/(8 c_B))^2 = 37.4613
```

**Every number matches `lemma_G_constants_run.log` (d) to the printed digits, including the sign and size of F̃(50) = −0.133 and the whole F̃ table. R₀ = 81 is confirmed, and it is the least value on the note's own half-integer grid.** The asymptote is (7/(8c_B))² = 37.46 and the contract's (3/(4c_B))² = 27.52 is what the exponent budget 3/2 (strip ½ + target 1, with no prefactor absorption) would give. **D5 UPHELD.**

### §7.3 Two observations on clause 5, neither a defect

**(i) P is a Laurent polynomial, not a polynomial.** In step 7 the term (2/L^{m+1})·s₀^j contributes L^{j−m−1}, which is a negative power of L for j < m+1. So P(L) is a Laurent polynomial with nonnegative coefficients and top degree 5, not "a polynomial in L with nonnegative coefficients and degree 5" (note §6; script comment). The conclusion is unaffected: for P = Σ_j a_jL^j with a_j ≥ 0 and every j ≤ 5, P′/P ≤ 5/L still holds, because the terms with j < 0 contribute ja_jL^{j−1} < 0 ≤ 5a_jL^{j−1}. §12.7 records the wording.

**(ii) The note's own hypothesis supports a sharper R₀ than the note takes.** Step 4 spends the L-hypothesis twice, once for 2C₁ ≤ e^{L/8}/b₁ and once for log(3.5+t) ≤ 1.05e^{L/8}, for a combined e^{L/4}. But the hypothesis L/8 ≥ log log(3+t) + log(2b₁C₁) gives directly e^{L/8} ≥ 2b₁C₁·log(3+t), so 2C₁log(3.5+t) ≤ 1.05e^{L/8}/b₁ in **one** use — and the term without the log factor needs only 2C₁ ≤ e^{L/8}/b₁, also one use. The exponent budget is then 5/8 + 1 = 13/8 instead of 7/4, the asymptote becomes (13/(16c_B))² = 32.30, and my search gives **R₀ = 73 at L₀ = 50** in place of 81. This is an improvement the record may take or leave; the note's 81 is valid and conservative, and no downstream number depends on the difference except the window size. §12.8.

### §7.4 The hypothesis check the brief asks for

*Is clause 5's hypothesis exactly what its proof uses?* **Yes.** The proof consumes exactly: (i) the multiset lies in |Im γ| ≤ ½ (the strip weight e^{L|y|/2}); (ii) the local count #{|Re γ − x| ≤ 1} ≤ C₁log(3 + |x|) for every real x (the shell counts, both sides); (iii) L ≥ 50 and L ≥ 8(log log(3+t) + log(2b₁C₁)) (the absorption in step 4 and the monotonicity in step 6). It uses **nothing** about the points inside the window, nothing about conjugation or reflection invariance, and nothing about the orbit. I checked each step against that list; the note's own hypothesis-check paragraph is accurate as written.

Absolute convergence of the full W_Z(f) over Z ∈ 𝒞(C₁) is indeed the same computation without the truncation, since every shell k ≥ 1 is covered by the same estimate and shell 0 is a finite count.

### §7.5 Is 𝒞(C₁) what ζ and DH satisfy?

**ζ: yes, but the constant needs a factor.** `Zeta23/WeilEF/Effective.lean` 924–927 gives `Ncount t (t+1) ≤ 540000000·log(|t| + 3)` for every real t — a count over a half-open window of **length 1**. The class asks for a window of **length 2**, |Re γ − x| ≤ 1. Covering [x−1, x+1] needs two (strictly, three, to catch the left endpoint) applications, and log(|x±1| + 3) ≤ log(|x| + 4) ≤ (log 4/log 3)·log(|x| + 3). So ζ's configuration lies in 𝒞(C₁) with **C₁ ≤ 1.4·10⁹**, not 5.4·10⁸ as §1, §7.3 and §8 rung 4 state. Nothing downstream moves materially: log(2b₁C₁) goes from 22.96 to 23.91, so the note's "L* = 1208 at δ = 0.1, t = 10⁶ with ζ's formal C₁" becomes **L* ≈ 1246**. §12.5.

**DH: the claim is correctly flagged, and one further point is owed.** The note labels the DH local-density claim `[recalled, unverified — the standard argument (Titchmarsh Ch. 9 for ζ) applies verbatim; no on-disk source; §8 uses only a finite window of DH zeros computed directly]`. That is the honest treatment under V.3, and it is not load-bearing: the §8 control fixes Z and Z′ as explicit finite multisets, so no C₁ is consumed anywhere in the control. I confirm there is no on-disk source for a DH Riemann–von Mangoldt constant.

The further point, which the note does not make and a referee will: **DH has zeros outside the critical strip** (f_DH has infinitely many zeros with β > 1), and the class 𝒞(C₁) lives in 0 ≤ β ≤ 1. The restriction of DH's zero multiset to the closed strip is nevertheless a legal configuration, because both of the symmetries used — ρ ↦ 1 − conj ρ (the functional equation Ξ(s) = Ξ(1−s)) and ρ ↦ conj ρ (real coefficients) — map the strip to itself; and the restricted multiset still contains the off-line orbit at ρ₀ = 0.808517… + 85.699…i. So the I.1 model-world argument survives intact, but it should be stated with the restriction. §12.4.

**CLAUSE 5 CLOSES.** The failure branch of PRICING §2.9 does not fire, and the note's §13 statement that the failure sentence is FALSE as a description of this outcome is correct.

---

## §8 Clause 1 (the orbit clause) and the reflection condition

### §8.1 The exact bound

E₋ = 2Re[h_f(−t − iδ)·conj(h_f(−t + iδ))] — correct, since the terms of the two points −t ∓ iδ are complex conjugates of one another. With h_f(−t ∓ iδ) = (−2t ∓ iδ)B̂(L(−2t ∓ iδ)) and Lemma G's complex case at ξ = −2tL, η′ = ±δL:

|E₋| ≤ 2|h_f(−t−iδ)||h_f(−t+iδ)| ≤ 2(4t² + δ²)e^{δL}G(2tL)².

**Correct, and it holds for every (t, δ, L) with no side condition.** That is the clause's real content and the note says so ("What the clause does not say").

### §8.2 The reflection condition (R), re-derived

The contract's relative form |E₋| ≤ 2δ²c(δL)²e^{−L} needs, after inserting clause 2's lower bound c(δL)² ≥ e^{δL}exp(−2√(δL) − (3/2)log(δL) + 2κ₋) and cancelling e^{δL},

(4t² + δ²)G(2tL)² ≤ δ²exp(−L − 2√(δL) − (3/2)log(δL) + 2κ₋),

i.e., taking logarithms with G(2tL)² = C_B²(1 + (c_B/2)√(2tL))²e^{−2c_B√(2tL)},

**(R)  2c_B√(2tL) − 2log(1 + (c_B/2)√(2tL)) ≥ L + 2√(δL) + (3/2)log(δL) − 2κ₋ + log((4t² + δ²)C_B²/δ²).**

I re-derived this from scratch and it is exactly the note's (R). The relaxation to (R′) for δ ∈ [25/L, ½] uses 2√(δL) ≤ √(2L), (3/2)log(δL) ≤ (3/2)log(L/2), δ^{−2} ≤ L²/625, 4t² + δ² ≤ 4t² + ¼ — all four correct.

My independent evaluation of (R′):

```
(4a) margin at t = 21L:  L=50: 0.71709 ; L=100: 34.067 ; L=1000: 753.94 ; L=1e5: 84762.0
(4b) margin at t = 20L, L=50: -1.3714 ;  at t=3, L=50: -70.512 ;  asymptote 1/(8 c_B^2) = 6.11613
```

matching `lemma_G_constants_run.log` (e) (margin 0.717 at L = 50, nondecreasing; T₁/L → 1/(8c_B²) = 6.12). **21 is the least integer multiplier on the grid: at t = 20L the margin at L = 50 is −1.37.** **D3 UPHELD as a deviation.**

### §8.3 Is the reflection condition necessary?

*Necessary for the truth of clause 1's contract form:* **no.** The exact reflected term at t = 30, δ = 0.3, L = 40 — where (R) fails by 70 nats — is |E₋|/(2δ²c²) = 7.83·10⁻²⁷ against e^{−L} = 4.25·10⁻¹⁸, nine orders inside the contract's target. The same holds at DH's parameters (§10).

*Necessary for this proof, with this c_B:* **yes, and unavoidably so.** The route must make exp(−2c_B√(2tL)) beat e^{L}, which forces 2c_B√(2tL) ≳ L, i.e. t ≳ L/(8c_B²) = 6.12L. So some condition t ≳ 6.1L is intrinsic to the route once c_B = 0.143 is the decay constant; 21 versus 6.12 is the gap between the finite-L condition at L = 50 and its asymptote. The only escape is a larger c_B, which needs a direct Cauchy estimate on B's own holomorphic extension (§14 of the note lists this as not done, with the reason). Note also that the proof already uses the *sharp* comparison — clause 2's lower bound on c(δL), which cancels the strip weight e^{δL} exactly; using clause 3's weaker c² ≥ e^{δL/2} would make the condition worse. There is no slack left in the route.

### §8.4 The "numerically vacuous" claim — **OVERRULED**

Three places in the note claim that with the numerically observed decay rate the reflection condition is vacuous for every t ≥ 3:

* line 5 (the summary): "a 'reflection condition' enters the hypotheses; numerically it is vacuous for every t ≥ 3";
* D3, line 39: "With the numerically observed decay rate 0.8 the threshold would read t/L ≥ 0.2, vacuous for every t ≥ 3 and L ≥ 50";
* §4's numerical record, line 255: "a condition that with the numerical decay rate 0.85 would read t ≥ 0.17L (vacuous for t ≥ 3, L ≥ 50)".

**The claim is false on two counts, and it is false in the note's own summary sentence.**

(a) *It is not vacuous.* t ≥ 0.17L at L = 50 is t ≥ 8.5, which t ≥ 3 does not give. The two hypotheses are not jointly vacuous for any of the stated pairs.

(b) *0.17L and 0.2L are the asymptotic ratios, not the finite-L thresholds.* Re-running (R′) with c_B replaced by 0.85 and everything else unchanged:

```
(4c) with rate 0.85: least admissible t at L=50  is 24.965 (t/L = 0.4993)
(4c) with rate 0.85: least admissible t at L=87  is 32.941 (t/L = 0.3786)
(4c) with rate 0.85: least admissible t at L=100 is 35.657 (t/L = 0.3566)
```

The threshold at L = 50 is t ≳ 25, not t ≳ 8.5; the ratio 0.17 = 1/(8·0.85²) is only approached as L → ∞, exactly as 6.12 is approached from 21 in the proved case.

**What is true, and what the record should say instead:** with the numerically observed rate the condition is *satisfied at every parameter this program uses*, including the DH control (t = 85.7, L = 87 requires t ≥ 32.9) and the campaign's operating point (t = 10⁶, L* = 403), and its asymptotic form is t ≳ 0.17L. That is a strong statement; it is not vacuity. §12.1 gives the replacement wording. The mathematical content of D3 is untouched: **D3 stays UPHELD; the vacuity claim inside it is OVERRULED.**

**CLAUSE 1 CLOSES**, with §12.1 owed.

---

## §9 Clause 4 (in-window on-line noise) — re-derived

**b₁.** b₁ := sup_η|ηB̂(η)|². My independent computation, by maximizing |ηB̂(η)| on a grid of 400 points and then polishing with `findroot` on the derivative:

```
(5a) b1 = sup|eta Bhat|^2 = 8.6461283 at eta* = 4.67274
(5b) ||B'||_1 = 3.3142754 => b1 <= ||B'||_1^2 = 10.984421
```

matching `b1_constant_run.log` (8.64612831 at η* = 4.67274; ‖B′‖₁ = 3.31427535948) and the note's §5. The certified enclosure [8.64613, 8.6981] in the author's log is built correctly — grid maximum on [0, 40] at step 10⁻², refined to 10⁻⁵, plus the Lipschitz increment |d/dη(ηB̂)| ≤ 1 + η∫|v|B = 1 + 0.16723η per cell, plus the tail |ηB̂(η)| ≤ ‖B″‖₁/η ≤ 0.72 for η ≥ 40. The hand-proved bound b₁ ≤ ‖B′‖₁² = 10.984 is correct and elementary: ∫B′(v)e^{iηv}dv = −iη B̂(η), so |ηB̂(η)| ≤ ‖B′‖₁.

**One precision item the referees will raise (§12.2).** b₁ appears in clause 4 and clause 6 as an **upper** bound on a supremum, and it appears in the theorem's L-hypothesis through log(2b₁C₁). The value 8.64613 is a computed grid maximum — a *lower* bound on the sup. The value that makes the statements theorems is the certified **8.6981** (or the fully proved 10.99). The note's §5 anticipates this ("the theorem may be read with b₁ replaced by 8.70 throughout at no visible cost") but §7.1's constant list prints 8.6461. The author's own scripts use `b1_certified_upper` = 8.6981 in the R₀ computation, which is the right choice; the effect of the mismatch is 0.006 nats against F̃(50)'s margin of 0.133 (I recomputed F̃(50) with 8.64613: **−0.127404**, still negative), so nothing moves. The theorem should be stated with b₁ = 8.70.

**The shells.** Shell 0: points with |γ − t| ≤ 1 number ≤ C₁log(3+t) ≤ C₁ℓ_R, each term (L(γ−t))²B̂(L(γ−t))²/L² ≤ b₁/L². ✓ Shells k ≥ 1: **the factor 2 the contract omitted is real** — the shell is two intervals, one on each side of t, each needing its own window of the class definition. **D4(a) UPHELD.**

**T₁ by the polynomial route.** |B̂(η)| ≤ ‖B‴‖₁/|η|³, so each term is ≤ (γ−t)²‖B‴‖₁²/(L|γ−t|)⁶ = ‖B‴‖₁²/(L⁶|γ−t|⁴) ≤ ‖B‴‖₁²/(L⁶k⁴); summing, T₁^{poly} = 2ζ(4)‖B‴‖₁²C₁ℓ_R/L⁶. This is ≤ b₁C₁ℓ_R/L² iff L⁴ ≥ 2ζ(4)‖B‴‖₁²/b₁ = 1.033·10⁵, i.e. **L ≥ L₁ = 17.927** (my value; the log prints 17.9). ✓ **D4(b) UPHELD**: with c_B = 0.143 the contract's Gevrey form of T₁ does not fall below b₁C₁ℓ_R/L² until L ≈ 1.1·10⁴, so the transcript's polynomial route is the operative one and the Gevrey form is proved alongside with its honest L₁. Both are proved; the assembly uses the one that works at L ≥ 50.

**D7 (ℓ_R = log(4 + t + R)).** Correct and needed: the shell centers are at t ± (k + ½), so the class's log is log(3.5 + t + k) ≤ log(4 + t + R) for k ≤ R. The contract's log(3 + t + R) is not quite what the shell decomposition produces. **D7 UPHELD.**

**CLAUSE 4 CLOSES**, with §12.2 owed.

---

## §10 Clauses 6, 7, 8 — the assembly, the tight pair, the scope

### §10.1 Clause 6, re-derived

Split: W_Z = (−2δ²c² + E₋) + N_Z + O_Z, W_{Z′} = N_{Z′} + O_{Z′}, with 0 ≤ N_Z, N_{Z′} ≤ N := b₁C₁ℓ_R/L² + T₁ and |O_Z|, |O_{Z′}| ≤ e^{−L}. Then

W_{Z′} − W_Z ≥ 2δ²c² − |E₋| − N − 2e^{−L} ≥ 2δ²c²(1 − e^{−L}) − 2N − 2e^{−L}

(clause 1 under (R) for the first step; N ≤ 2N for the second). Clause 5's L-hypothesis L ≥ 8(log log(3+t) + log(2b₁C₁)) does follow from the displayed one, since 4/δ ≥ 8 and 2log(1/δ) ≥ 0. ✓ The reduction to

**(7.1)  δ²e^{δL/2}(1 − 2e^{−L}) ≥ 4b₁C₁ℓ_R/L² + 2e^{−L}**

is correct algebra (using c² ≥ e^{δL/2} from clause 3 at λ = δL ≥ 25 and N ≤ 2b₁C₁ℓ_R/L² from clause 4).

Each step of (7.1)'s proof, re-checked:

* From the L-hypothesis, δL/2 ≥ 2(log log(3+t) + 2log(1/δ) + log(2b₁C₁)), so e^{δL/2} ≥ (log(3+t))²δ^{−4}(2b₁C₁)² and δ²e^{δL/2} ≥ 4b₁²C₁²(log(3+t))²/δ² ≥ 16b₁²C₁²(log(3+t))² (δ ≤ ½). ✓
* ℓ_R = log(4+t+R₀L) ≤ log(4+t) + log(1+R₀L) ≤ 1.1log(3+t) + L (the first from (4+t)(1+R₀L) ≥ 4+t+R₀L; the second from log(4+t)/log(3+t) ≤ log7/log6 = 1.086 at t = 3, decreasing, and R₀L ≤ e^L − 1 at L ≥ 50). ✓
* ℓ_R/L² ≤ 1.1log(3+t)/2500 + 1/50 ≤ 0.02log(3+t) ≤ (log(3+t))² (using log(3+t) ≥ log 6 = 1.79). ✓
* So 4b₁C₁ℓ_R/L² ≤ 4b₁C₁(log(3+t))², a quarter of the lower bound just obtained, and the two e^{−L} terms are below 10⁻²⁰ of it at L ≥ 50. ✓

Finally δ²e^{δL/2} ≥ 1 iff δL/2 ≥ 2log(1/δ), and the L-hypothesis gives δL ≥ 8log(1/δ), i.e. δL/2 ≥ 4log(1/δ) — a factor 2 to spare. ✓ **D8's second half UPHELD.**

**CLAUSE 6 CLOSES.**

**D8's first half, and a wording point.** The note records that "the contract's first inequality in clause 6 omits E₋; the proved chain is [with the (1 − e^{−L}) factor], which the contract's right-hand side implies once E₋ is folded in." The logical relation stated is true (the contract's RHS is the larger quantity, so a bound by it implies the bound by the proved one) — but it is stated the wrong way round for a *deviation* record, where the point is that the contract's literal form is **not** proved and what is proved is weaker by the factor (1 − e^{−L}). Since 2δ²c²e^{−L} is not absorbable into the 2e^{−L} term (c² ≥ e^{δL/2} is unbounded), the contract's form genuinely is not available, and D8 is a real deviation. The final conclusion (≥ δ²e^{δL/2} ≥ 1) is unchanged. §12.9. **D8 UPHELD.** The parenthetical that one N would do in place of 2N is also correct: |N_Z − N_{Z′}| ≤ max(N_Z, N_{Z′}) ≤ N, since both are nonnegative.

**The dependency chain, checked for cycles (10(g)).** Z (quadrature) → b₁, ‖B′‖₁, ‖B″‖₁, ‖B‴‖₁, κ_∞; Lean (18/e) → A₁ = 72/e → c_B, C_B → {R₀ (also uses b₁), the reflection constant 21 (also uses κ₋), T₁^{Gev}}; ‖B‴‖₁ and b₁ → L₁; κ₋ → λ₀ = 25; c₀ = ½ → C₀ = 2/(1 − c₀) = 4. **No constant depends on a later one.** The slack ledger the note prints is accurate: clause 3's margin e^{0.6335} = 1.88 at λ = 25; (7.1) with a factor ≥ 4; F̃(50) = −0.133; the reflection margin 0.717 nats at L = 50.

### §10.2 Clause 7 (the tight pair) — one arithmetic correction

h_f(t) = (t − t)B̂(0) = 0 by (0.1), so the double at +t contributes exactly 0 to W_{Z′}(f). Confirmed numerically: h_f(t) = 7.1·10⁻⁵¹ − 5.6·10⁻⁴⁹i in my quadrature.

**D9's value is a factor 2 too large.** The double at −t is the *point* −t with *multiplicity 2*; its term in `Wsummand` is m_ρ·h_f(−t)·conj(h_f(−t)) = 2|h_f(−t)|². With h_f(−t) = (−2t)B̂(−2tL) and B̂ real and even on the reals, |h_f(−t)|² = 4t²B̂(2tL)², so the contribution is **8t²B̂(2tL)²**, not the note's "2·2|h_f(−t)|² = 16t²B̂(2tL)²". My check at t = 30, L = 40:

```
(6e) double at -t contributes mult*|h_f(-t)|^2 = 2*9.04182e-32 = 1.80836e-31 ;
     note's "2*2|h_f(-t)|^2 = 16 t^2 Bhat(2tL)^2" = 3.61673e-31 (a factor 2 too large)
(6f) 8 t^2 Bhat(2tL)^2 = 1.80836e-31  (the correct value)
```

**The error is harmless**: the term is nonnegative and is absorbed into N_{Z′} or O_{Z′} exactly as any other real point of Z′, so a factor 2 in an over-estimate changes nothing in clause 6's proof or in clause 7's conclusion. But it is an arithmetic mis-statement in the note's body and belongs in the corrections. §12.3. **D9 UPHELD in substance, value corrected.**

**Against II.4's exact statement.** I re-read `BARRIER-ZOO.md` lines 134–146. The note's quotation of II.4's STATEMENT is verbatim correct, including the final clause "Tightness is relative to the invariant list {tr, ‖·‖²_F, atom norms ≤ 1, n₊}". The note's three-part answer is the right one and it is complete: (i) the datum W_Z(f_{t,L}) is a single first-order sum rule at one test, not a function of that list, so it is **outside II.4's data class** and II.4 — a theorem *about* that list — is untouched; (ii) the separation degenerates as δ → 0 (L* → ∞ like δ^{−1}log(1/δ), and at fixed L the orbit's contribution → 0 like δ²), which is II.4's own "depth → 0" regime; (iii) II.4's EXECUTABLE TEST demands a depth-continuity check ("any separation claim must be depth-uniform or priced over the depth family"), and the note prices it — L*(t, δ) is the price and it is explicitly not uniform in δ. II.4's test also says "name the invariant beyond the list … and run IV.6/IV.7 on it"; the note's §12 runs IV.6 (no pair-correlation input) and IV.7 (no tail row, no cubic; the Session-6 closure cited for the wall's name only). **No formalized no-go is moved. CLAUSE 7 CLOSES.**

### §10.3 Clause 8 (scope)

The identification of the datum for ζ uses `EF_lit_zetaZeroConfig` (hypothesis-free) and `prop_EF_of_lit` with k = g = f ⋆ f̃, which is C^∞ and compactly supported in [−L, L] — but `prop_EF_of_lit` asks for `tsupport f, g ⊆ Icc (−L/2) (L/2)`, which is exactly where f_{t,L} lives, and `EF_lit` itself asks only `ContDiff ℝ 2 k` and `HasCompactSupport k`. Both are satisfied. The displayed right-hand side is `literatureRHS` transcribed correctly (`paperFT k (I/2) + paperFT k (−I/2)` + the archimedean integral with `gammaBracket r = Re ψ(¼ + ir/2) − log π` − the von Mangoldt sum). ✓

The scope statement — clauses 1–7 consume neither axiom P nor any prime-side estimate nor the explicit formula, and for ζ the prime-side evaluation is M6 behind the pointwise short-Dirichlet-polynomial wall — is accurate and correctly cited (C2 line 64; repair 6, C2 line 74; zoo IV.7's Session-6 closure at BARRIER-ZOO line 392). **CLAUSE 8 CLOSES.**

---

## §11 The controls, the prior art, and the process gates

### §11.1 The DH negative control (zoo V.4) — it ran zero-side, and it FIRED

**Zero-side.** I read `dh_negative_control.py` in full. It contains no von Mangoldt function, no prime sum, no Dirichlet polynomial; the only occurrence of ζ is `mpmath.zetazero`, which supplies ζ's **zeros** for the positive control. The file's own header says "ZERO-SIDE only (no prime-side evaluation)", and that is what the code does. **Confirmed, as the brief's Addendum requires.**

**It fired.** Re-run here, byte-identical:

```
L= 86.907: W_Z = -394292.19  W_Z' = 3.432164e-10  (Z''-Z' = 2.34e-38)
           main -2d^2c^2 = -394292.19  |W_Z - W_Z'| = 394292.19
           bound d^2 e^(dL/2) = 63212.9   ratio = 6.2375   fires(>=1): True
L= 100.0:  |W_Z - W_Z'| = 8536115.2   bound = 476348.0   ratio = 17.92   fires: True
```

At the theorem's own bandwidth L* = 86.907 the datum separates DH's off-line orbit from the on-line configuration by 3.943·10⁵, a factor **6.24** above the clause-6 bound and 4·10⁵ above 1, and it equals the main term −2δ²c(δL)² to the printed digits. The tight-pair line is there in numbers: the on-line double at ±t moves the datum by 2.3·10⁻³⁸ while the pair at depth 0.3085 moves it by −3.9·10⁵.

**A cross-check the note does not draw, and which strengthens it.** Below the theorem's threshold the ratio to the bound is < 1 (0.33 at L = 30 up to 0.987 at L = 60, δL = 18.5) and crosses 1 between L = 60 and L = 70 (ratio 1.84 at L = 70, δL = 21.6). The proved slack inequality of clause 3 first holds at λ = 23 and the contract fixes λ₀ = 25. The empirical crossing (δL ≈ 19), the proved threshold (λ ≥ 23) and the contract's λ₀ = 25 are in the right order with the right gaps: **λ₀ = 25 is close to optimal for this bump, and the bound is not slack by much where it first applies.**

**The positive control stayed silent.** ζ's 25 zeros in the same window, all on-line: W_ζ(f_{t,L}) = 8.66·10⁻⁴, 1.08·10⁻⁵, 2.09·10⁻⁷, 3.78·10⁻⁸ at L = 20, 40, 86.907, 100 — nonnegative at every L (as §3 requires of an on-line configuration), below the clause-4 noise bound b₁log(3+t+W)/L² at every L (0.103, 0.0258, 0.00547, 0.00413), and **twelve orders of magnitude** below the DH signal at L*. Both controls sit at the same t and the same bandwidths, and at L* the depth in play satisfies δL* = 26.8 ≥ λ₀ = 25, so both are in the detector's visible regime as IV.9 and V.4 jointly require.

**The two caveats: do they undermine the control? No — and here is the precise reason.**

*Caveat (i): the theorem's window hypothesis is not verified for DH.* R₀L* ≈ 7·10³, and DH's further off-line zeros in that range were not located. What this costs is **not** the control but the *theorem-instance*: the run does not verify that Theorem M2's hypotheses hold for DH's true configuration at that height. What V.4 asks of a falsification channel is different — that the channel FIRE on a case known to fail and stay SILENT on a case known to hold. The channel here is "the bandwidth-L datum computed from the zeros is ≤ −1". It fired on DH and stayed silent on ζ, on explicit finite configurations that are exactly what the channel would be fed. That is the control, and it is valid. The note is right to fix Z and Z′ as explicit finite multisets and right to print the caveat. (It is also worth saying that an unlocated further off-line orbit in the window would, by §0.2's sign computation, push the datum further *negative* — the direction that makes the detector fire, not silence it. The control is conservative in that respect.)

*Caveat (ii): the reflection condition t ≥ 21L fails at t = 85.7, L = 87 (t/L = 0.99).* Clause 1's relative e^{−L} bound is therefore not asserted at the control's parameters. But the control does not use clause 1: it computes the reflected pair directly, and the run finds it at 10⁻¹⁵ of the main term, exactly as §4's independent instance found 7.8·10⁻²⁷ at t = 30, L = 40. And by §8.4's recomputation, with the numerically observed decay rate the condition at L = 87 reads t ≥ 32.9, which t = 85.7 satisfies comfortably. So the caveat records a gap between the proved constant and the true behavior, not a defect in the control.

**Verdict: the DH control STANDS.** Both halves of V.4 are discharged, both in the visible regime, with the caveats correctly stated.

*One budget note.* The run took 974 s = 16.2 min against the brief's 10-minute per-script budget. The note declares this in §8 caveat (iii) and in §14. It is a declared overrun of a soft budget, not a defect.

### §11.2 Prior art — standing order 7, run independently

**Hua–Yang, arXiv:2608.16034v2, read at the page by me.** SHA-256 `465a5c6d…` confirmed. I extracted the text layer myself and read §2.2 (the Gevrey class), §5 (Gevrey Gabor compression), §9 in full, §12 (uniformity and endpoint limitations) and §13 (conclusion).

*What is in print.* Three things, all of which the note identifies:

1. **Lemma G's mechanism.** Lemma 9.1: "∥u(r − iδ)∥₂² ≤ CL²e^{L|δ|}exp[−c{L dist(r, J)}^{1/s}]", proved by "m integrations by parts against the whole complex exponential", using ‖ψ^{(m)}‖₁ ≤ C₀R₀^m(m!)^s, m! ≤ m^m, and the optimized integer order m = ⌊c₀(L|r − τ|)^{1/s}⌋, with "the trivial estimate covers the bounded range omitted by the integer choice of m" and the strip weight e^{L|δ|/2} per factor ((9.1.3)). **This is exactly Lemma G's proof**, including the treatment of the small-|η| range that the note handles by |B̂| ≤ ∫B = 1. The note's identification is correct at the page.
2. **Clause 5's shell summation.** (9.2) is the local count #{ρ : |Im ρ − t| ≤ 1} ≪ log(q(|t|+3)); (9.2.3), (9.2.7) and (9.2.8) sum the exterior orbits over unit shells against it, with a local (|γ| ≤ 4T+1) / remote (|γ| > 4T+1) split. **This is the mechanism of clause 5(b).**
3. **The polynomial-to-Gevrey replacement as such**, stated as their own motivation (text-layer line 1954, verbatim): "The Gevrey estimate removes the fixed-power requirement TQ ≥ Q^η that would result from a direct polynomial-decay argument." The note quotes this correctly.

*What is not in print, and what therefore stays novel.* My own greps over the full text layer: **"single zero" — 0 hits; "detect" — 0 hits; "isolated zero" — 0 hits; "individual zero" — 0 hits; "separat*" — 1 hit, and it is about lattice depths ("scaled depths separated by 2π", line 1001), not about configurations.** The paper's conclusion says in terms: "The result remains a family-level theorem for one prime modulus; no individual-character conclusion is asserted." Four differences, each real:

* **Object.** Hua–Yang bound a trace-norm block of a Gabor Gram matrix (second-order data, ‖·‖₁ on an operator) and average over a family of characters; the note bounds one first-order sum-rule value at one height for one configuration. The note's §11 says this and it is right.
* **Radius.** Their exterior region is at distance ≥ θT from J with T the height, i.e. the excluded window is proportional to the **height**; the note's is R₀L, proportional to the **bandwidth**. For a single-height statement these are different claims, and the note's is the one a detector needs.
* **Constants.** Every constant in §9 is an implied constant "depending only on the fixed window and the lattice spacing" — c, C, c₀, c₁, c₂, C₁, C₂ are never evaluated. The note's c_B, C_B, R₀, κ± are explicit and traceable to a machine-checked derivative bound. That is bookkeeping, and the note grades it as such ((d), "bookkeeping, not mathematics").
* **The test.** Their sampled vectors are p_k(t) = φ̂(t − τ_k) with φ(u) = ψ(u/L) — modulated Gevrey windows on a lattice of centers (§5, (5.5)); the note's test is a single center and the **derivative** of the window, which is what makes h_f(t) = 0 and gives clause 7 its content. The note's 10(n) line states exactly this difference, and I confirm it at §5 of the paper.

*The corpus and the listing.* The author's eight arXiv queries are on record with their hit lists; I ran six further queries of my own with different terms, all returning **0 entries** (`opus_arxiv_queries.log`): `Gevrey AND "critical line"`; `ultradifferentiable AND zeta`; `"explicit formula" AND "off-line" AND zeros`; `"sum rule" AND zeros AND "explicit formula"`; `bandlimited AND zeros AND zeta`; `Gevrey AND "zeta function"`. The corpus route (`results/corpus-routing.md`, row 259 for r3s-24) and the paper itself are the decisive evidence, and nothing I found alters the picture. **Note that under V.5 none of this grounds a verdict**: the note is careful to use the absence only to attach `[novelty: single-check]` labels, never to support a dead end, and its §12 step-7 paragraph says so explicitly. That is the correct use.

**Novelty verdict.** The note's four novelty items (a)–(d) stand, and its "NOT new" list — Lemma G's mechanism, the shell summation, the modulated derivative-bump test, the cosh gain — is correct and complete. The labels may be upgraded from `[novelty: single-check]` to **`[novelty: dual-model check 2026-09-16]`** on items (a), (b), (c); item (d) is self-described as bookkeeping and needs no label. The single most important thing this check changes: **the note has already reduced its own novelty claim by the right amount.** Hua–Yang §9 is the Gevrey decay mechanism *and* the out-window localization mechanism in print; what remains novel is the statement — separation of two configuration classes by one first-order datum at an explicit bandwidth with an explicit bandwidth-proportional window — together with the two-sided edge law and the tight-pair corollary.

Two attributions in the note that I checked and confirm: the paper does cite "an Anthropic manuscript" for the inertia/rank–trace ingredient (text-layer line 100, and references [17]–[19]); and `Zeta23/Taper/Gevrey.lean`'s header does describe the downstream Gevrey tail lemma as not on disk, so Lemma G is its Fourier-side content for this bump, as the note says.

### §11.3 "Cannot" and "never" sentences, and the 10(g) lint

**10(g) lint: clean.** No occurrence of "clearly", "obviously", "easy to see", "well known" or "well-known" anywhere in the note.

**U.S. English: clean.** No British spelling in the note (checked against the full list in the standing instruction: -ise/-yse, -our, -re, -ll- before suffix, maths, grey, towards, programme, defence/offence/licence/practise).

**The "cannot"/"never" discipline.** Five sentences carry one of the words. Four are theorems with their hypotheses stated in place: line 313 (the polynomial bound is ≥ 1 for |x| ≤ e^{L/12} — the justification is in the sentence); line 364 (the theorem cannot tell DH from ζ — because it consumes no axiom P and holds for both, clause 8); line 372 first (the theorem never consumes Λ ≥ 0 — with the list of what clauses 1–7 do consume); line 398 (the RH-false world satisfies every input, so the theorem cannot decide RH — this is I.1's model-world argument, and it is a theorem). **One is not:** line 372's "a separation theorem about configurations cannot, without an arithmetic input, tell which configuration is ζ's" is a general impossibility claim about *all* separation theorems, which nothing in the note proves. It should be restricted to this theorem or labeled. §12.11.

### §11.4 The zoo brief-time protocol

I re-ran §0's checklist against the note's §12 and agree with every step. Step 2 (I.1): correct, with the strip-restriction point of §7.5 owed. Step 3 (II.4): correct, and §10.2 above. Step 5 (IV.1): the hit is real — the observable of clause 8 is a Weil test at bandwidth L with no multiplier, a point of the classical data class — and the evasion is written and is the right one: the theorem claims no new data coordinate, its content is a **lower bound on the separation between two values of the same datum**, i.e. a sensitivity statement. That is precisely the shape IV.1 does not kill. Step 6 (IV.9): §10's two numbers are computed and both sides are named. Step 7 (V.2, V.4, V.5): discharged, §11.1 and §11.2.

One number in §10 I re-derived: the theorem's L* at δ = 0.1, t = 10⁶, C₁ = 1 is 40·(2.6259 + 4.6052 + 2.8500) = **403.2**, matching the log's 403.5 (which carries b₁ = 8.6981 in log(2b₁)); the pricing's "≈ 250" is 25/δ, the non-binding term, exactly as the note says. The balance-only value 50 reproduces the pricing's log line for line, and the note's description of `gevrey_edge_law_rerun_DIFF.txt` is exact: the file is `46d45\n< \n`, i.e. **one blank line**, an artifact of the grep filter, and no numeric difference anywhere.

---

## §12 The exact wording corrections the record needs

The author's body is not edited by this check. What follows is the list the orchestrator appends as a dated corrections section, in the pattern of `confinement-note.md`'s "Corrections after the dual check". Items 1–3 are the ones a referee would call out; items 4–13 are precision and citation.

**§12.1 — the reflection condition is not "numerically vacuous". (Three places; the first is the note's own summary.)**

*Line 5, summary, "(a 'reflection condition' enters the hypotheses; numerically it is vacuous for every t ≥ 3)"* → **"(a 'reflection condition' enters the hypotheses; with the numerically observed decay rate it is satisfied at every parameter this program uses, including the DH control at t = 85.7, L = 87 and the campaign's operating point t = 10⁶, L* = 403)"**.

*D3, line 39, "With the numerically observed decay rate 0.8 the threshold would read t/L ≥ 0.2, vacuous for every t ≥ 3 and L ≥ 50 (computed, not proved)"* → **"With the numerically observed decay rate 0.85 the same chain gives the finite-L thresholds t ≥ 25.0 at L = 50, t ≥ 32.9 at L = 87 and t ≥ 35.7 at L = 100, with the asymptotic ratio t/L → 1/(8·0.85²) = 0.17 (computed, not proved) — satisfied at every parameter used in this program, but not implied by t ≥ 3 alone."**

*§4, line 255, "a condition that with the numerical decay rate 0.85 would read t ≥ 0.17L (vacuous for t ≥ 3, L ≥ 50; computed, not proved)"* → **"a condition whose asymptotic form at the numerical decay rate 0.85 is t ≳ 0.17L, and whose finite-L thresholds there are t ≥ 25.0 at L = 50 and t ≥ 32.9 at L = 87 (computed, not proved)"**.

**§12.2 — state the theorem with b₁ = 8.70.** §7.1's constant list prints "b₁ = sup|ηB̂|² = 8.6461", which is a computed grid maximum, i.e. a *lower* bound on the supremum, while b₁ is used everywhere as an *upper* bound (clause 4's noise bound, and the L-hypothesis via log(2b₁C₁)). Replace by **"b₁ = sup|ηB̂|² ∈ [8.64613, 8.6981]; every statement below is made with b₁ = 8.70, the certified upper end, which is what `verify/lemma_G_constants.py` uses (`b1_certified_upper`); the fully proved bound b₁ ≤ ‖B′‖₁² = 10.99 may be substituted throughout at the cost of 0.24 nats in the L-hypothesis."** §5 already anticipates this; §7.1 should match it. Effect on F̃(50): −0.133 at 8.6981, −0.127 at 8.64613 — nothing moves.

**§12.3 — clause 7 / D9: the reflected double contributes 8t²B̂(2tL)², not 16t²B̂(2tL)².** D9 (line 51) and §7.2's proof both read "2·2|h_f(−t)|² = 16t²B̂(2tL)²". The point −t carries multiplicity 2 and its `Wsummand` is m_ρ|h_f(−t)|² = 2·4t²B̂(2tL)² = **8t²B̂(2tL)²**. Verified numerically at t = 30, L = 40: 1.80836·10⁻³¹, half the note's figure. The term is nonnegative and absorbed into N_{Z′} or O_{Z′}, so nothing downstream changes; the value in the text is wrong by a factor 2.

**§12.4 — DH's zeros outside the strip.** §8 rung 2 and §12 step 2 say the theorem "holds for DH" and that "the RH-false world satisfies every input". f_DH has zeros with β > 1, which are not points of any configuration in 𝒞(C₁). Add: **"DH's zero multiset restricted to the closed strip 0 ≤ β ≤ 1 is a legal configuration — both symmetries used, ρ ↦ 1 − conj ρ (the functional equation) and ρ ↦ conj ρ (real coefficients), map the strip to itself — and it contains the off-line orbit at ρ₀; the zeros of f_DH with β > 1 lie outside the class and are simply not part of Z."** The I.1 argument is unaffected; the sentence as written is imprecise.

**§12.5 — ζ's C₁ is 1.4·10⁹, not 5.4·10⁸.** `zeta_local_zero_count_explicit` bounds a window of length 1 (`Ncount t (t+1)`); the class 𝒞(C₁) asks for |Re γ − x| ≤ 1, a window of length 2, which needs two (strictly three, to catch the left endpoint) applications, plus log(|x| + 4) ≤ (log 4/log 3)log(|x| + 3). So in §1, §7.3 and §8 rung 4 read **C₁ ≤ 1.4·10⁹**. Consequence: log(2b₁C₁) = 23.91 in place of 22.96, so rung 4's "L* = 1208 at δ = 0.1, t = 10⁶" becomes **L* ≈ 1246**. Nothing else moves.

**§12.6 — c_B's fourth decimal.** D2 (line 37) prints "c_B = 2/√(72e) = 0.14298"; §2 prints 0.142961 and §15 prints 0.14296. The value is **0.14296065**. Make D2 read 0.14296.

**§12.7 — P is a Laurent polynomial.** §6 and the script comment say "P an explicit polynomial in L with nonnegative coefficients and degree 5". The incomplete-gamma terms carry L^{j−m−1} with j down to 0, so P is a **Laurent** polynomial with nonnegative coefficients and top degree 5. The conclusion (log P)′ ≤ 5/L is unaffected — negative-power terms contribute ja_jL^{j−1} < 0 ≤ 5a_jL^{j−1} — but the sentence should say "Laurent polynomial … and top degree 5".

**§12.8 — a sharper R₀ is available from the same hypothesis (optional).** §6 spends L/8 ≥ log log(3+t) and L/8 ≥ log(2b₁C₁) separately, for a combined e^{L/4}; the single hypothesis gives e^{L/8} ≥ 2b₁C₁·log(3+t) directly, so 2C₁log(3.5+t) ≤ 1.05e^{L/8}/b₁ in one use. The exponent to beat becomes 13/8 rather than 7/4, the asymptote becomes (13/(16c_B))² = 32.30, and the least R₀ at L₀ = 50 becomes **73**. The note's 81 is valid and conservative; if the record prefers the sharper constant, the same one-point check proves it.

**§12.9 — D8's "implies" reads the wrong way for a deviation record.** "the proved chain is [with (1 − e^{−L})], which the contract's right-hand side implies once E₋ is folded in" is logically true but inverts the point. Read: **"the contract's form is not what is proved; what is proved is weaker by the factor (1 − e^{−L}) on the main term, because 2δ²c(δL)²e^{−L} is not absorbable into the target's 2e^{−L} (c(δL)² ≥ e^{δL/2} is unbounded). The final conclusion, ≥ δ²e^{(1−c₀)δL} ≥ 1, is unchanged."**

**§12.10 — a cleaner justification for λE₁(λ) ≤ 25E₁(25) (optional).** §3.2's parenthetical ("E₁(λ) ≤ 0.8e^{−1.51√λ}, and λe^{−1.51√λ} is decreasing") yields only λE₁ ≤ 0.0105, not 0.0045. The direct route gives the stated bound: d/dλ log(λE₁(λ)) = 1/λ − 1/(4μ) + 1/(2√μ) − ½ < 0 for λ ≥ 25, so λE₁ is decreasing outright. Either way D(λ) > 0, since 0.52 − 0.9625·0.0105 = 0.510 > 0.

**§12.11 — one "cannot" sentence is not a theorem.** §9 (line 372): "a separation theorem about configurations cannot, without an arithmetic input, tell which configuration is ζ's" is a general impossibility claim about all such theorems and is not proved anywhere in the note. Restrict it — **"*this* separation theorem cannot, without an arithmetic input, tell which configuration is ζ's: clauses 1–7 hold verbatim for DH (rung 2), so no consequence of them distinguishes ζ's configuration from DH's"** — or label it `[reading]`.

**§12.12 — four Lean citations.** `Zeta23/Taper/Gevrey.lean`: `def theta` is at **61**, not 55; `gb_mul_gb_le` is at **248**, not 262–275; `gevreyProfile_rhoTwo` is at **401**, not 393; `GevreyProfile`'s `structure` line is 52 with its `bound` field at 58, so "lines 45–52" should read "lines 44–58". All four names exist and all quoted text is verbatim correct, so the brief's stop condition (d) does not fire. Also: `prop_EF_of_lit`'s conclusion is a **three**-fold conjunction (`Summable ∧ Integrable ∧ Z.W f g = ∫ …`); §1 quotes two of the three.

**§12.13 — three small record items.** (i) §0.3 says the (0.2) check has "relative difference 10⁻⁶ at trapezoid resolution"; `four_point_accounting_run.log` (4) prints `rel diff = 1.0e-9`. (ii) §6 says the transcript "fell back to an exponential exclusion zone e^{L/8}"; tx_032 line 46 reads R_L := **e^{L/12}**L, and the same sentence in the note uses e^{L/12} correctly two clauses earlier. (iii) §14's compute list records `dh_negative_control.py` once; `verify/run_all.log` shows a first attempt terminated at `exit=143` and `run_rest.sh` re-running it and `lemma_G_constants.py` to completion. The logs on disk are the complete run; a one-line note in §14 would close the loop.

---

## §13 Verdicts

### §13.1 Per clause

| clause | verdict | the derivation or computation behind it |
|---|---|---|
| **1** — orbit clause | **CLOSES** | Four-point accounting re-derived (§2) and confirmed by my own quadrature to zero relative error; the exact bound \|E₋\| ≤ 2(4t²+δ²)e^{δL}G(2tL)² re-derived from Lemma G's complex case (§8.1); (R) re-derived line by line and (R′) re-evaluated — margin 0.717 at t = 21L, L = 50, and −1.371 at t = 20L, so 21 is least (§8.2). §12.1 owed. |
| **2** — edge law, two-sided | **CLOSES** | (3.1)–(3.3) re-derived; Lemma K's four envelope inequalities checked algebraically; both bounds re-derived constant by constant; κ₋ = κ_∞ = 1.4808831774, κ₊ = 1.5309456774; my own quadrature puts κ(λ) in the band at λ = 25 … 10⁵ (§5). |
| **3** — slack | **CLOSES** | m(25) = 0.63345262 > 0 and m′ > 0 for λ ≥ 25; proved margin 1.8841 against the computed 1.99911 (§6). |
| **4** — in-window noise | **CLOSES** | b₁ = 8.6461283 at η* = 4.67274 independently; the factor-2 shell count verified; T₁^{poly} re-derived and L₁ = 17.927 recomputed (§9). §12.2 owed. |
| **5** — out-window contamination | **CLOSES** | All ten steps re-derived (§7.2); my own implementation of F̃ gives F̃(50) = −0.133397 at R₀ = 81, +0.237 at R₀ = 80.5, and the full F̃ table matches; uniformity over depth ½ verified at the source (the depth enters only through e^{L\|y\|/2}); the hypothesis is exactly what the proof uses (§7.4). |
| **6** — separation | **CLOSES** | The split, the two bounds, (7.1) and each of its four steps re-checked; the dependency chain re-checked for cycles; the final δL/2 ≥ 2log(1/δ) holds with a factor 2 to spare (§10.1). |
| **7** — tight pair | **CLOSES** | h_f(t) = 0 confirmed; II.4 re-read at BARRIER-ZOO 134–146 and the note's quotation verified verbatim; the three-part answer (outside the data class, degeneration stated, depth-continuity priced) is complete (§10.2). §12.3 owed. |
| **8** — scope | **CLOSES** | `EF_lit`'s hypotheses are met by g = f ⋆ f̃; `literatureRHS` transcribed correctly; the M6 wall and IV.7's Session-6 closure cited by line and correct (§10.3). |

**No clause is FIX-FIRST. No clause FAILS.**

### §13.2 Per deviation

| | verdict | reason |
|---|---|---|
| **D1** g is Hermitian, not real | **UPHELD** | g(x) = e^{−itx}a(x) with a real even; the log measures max\|g(−x) − conj g(x)\| = 0 and max\|Im g\| = 2.5·10⁻⁴. Nothing downstream needs g real: `EF_lit` takes `k : ℝ → ℂ`. |
| **D2** c_B = 2/√(72e) = 0.14296, not 0.20 | **UPHELD** | B_raw(v) = θ(v+½)^{1/4} exactly (checked to 10⁻⁴¹), and a quarter power does not transfer a derivative bound; the factorization + 4^k chain rule + Leibniz route is the right one and gives 2/√(72e). The pricing's 1/(3√e) is θ's constant. §12.6 (a fourth-decimal print). |
| **D3** reflection condition t ≥ 21L | **UPHELD as a deviation; the vacuity claim inside it OVERRULED** | The condition is necessary for this route (t ≳ 1/(8c_B²)·L = 6.12L asymptotically, 21L at L = 50) and unnecessary for the truth (E₋/main = 7.8·10⁻²⁷ where (R) fails by 70 nats). But the claim "numerically vacuous for every t ≥ 3", made in the summary and twice more, is false: at the numerical rate the finite-L thresholds are t ≥ 25.0 (L = 50), 32.9 (L = 87), 35.7 (L = 100). §12.1. |
| **D4** the factor 2 in the shell count; the polynomial route for T₁ | **UPHELD** | The shell k ≥ 1 is two intervals, one each side of t; each needs its own class window. The Gevrey form of T₁ needs L ≈ 1.1·10⁴ with c_B = 0.143, the polynomial route L₁ = 17.927 — both proved, the second operative. |
| **D5** R₀ = 81 for L ≥ 50; asymptote (7/(8c_B))² = 37.46 | **UPHELD** | Independently reproduced, including that 81 is the least value on the half-integer grid at L₀ = 50. The contract's (3/(4c_B))² = 27.52 is the budget 3/2, which omits the prefactor absorption the hypothesis forces. (§12.8: 13/8 and R₀ = 73 are available from the same hypothesis.) |
| **D6** κ₋ = 1.48088 (closed form), κ₊ = 1.53095; 1.515 was a fit | **UPHELD** | κ_∞ = log(√(π/2)e^{−1/4}/Z) re-derived and recomputed; the band contains every exact κ(λ) I computed on λ ∈ [25, 10⁵]; \|κ± − 1.515\| ≤ 0.035 ≤ 0.1, so stop condition (a) does not fire and λ₀ = 25 stands. |
| **D7** ℓ_R = log(4 + t + R) | **UPHELD** | The shell centers are t ± (k + ½), so the class's log is log(3.5 + t + k); the contract's log(3 + t + R) is not what the decomposition produces. Costs under 3 % in clause 6's chain, as the note says. |
| **D8** clause 6's chain carries (1 − e^{−L}); the last condition is automatic | **UPHELD** | 2δ²c²e^{−L} is not absorbable into 2e^{−L}, so the contract's literal form is not proved; the final bound is unchanged. δL/2 ≥ 4log(1/δ) ≥ 2log(1/δ) verified. §12.9 (wording). |
| **D9** the reflected on-line double contributes a nonnegative real-point term | **UPHELD in substance; the value corrected** | h_f(t) = 0 kills the +t double; the −t double contributes m\|h_f(−t)\|² = **8t²B̂(2tL)²**, not the note's 16t²B̂(2tL)². Nonnegative and absorbed either way. §12.3. |

### §13.3 The items the brief asked this check to settle

* **The exponent bookkeeping.** The contract's B *is* θ^{1/4}; the note's claim is right and is the reason the pricing's c_B = 0.20 is unavailable. The chain B_raw = g(4v+2)g(2−4v) → 4^k → Leibniz with C(k,i)i^i(k−i)^{k−i} ≤ k^k → (k+1)A₁^kk^{2k} → the optimized k = ⌊√(η/A₁)/e⌋ → c_B = 2/√(72e), C_B = e²/Z is correct at every step (§4).
* **Clause 5's hypothesis is exactly what its proof uses** (§7.4), and 𝒞(C₁) is what ζ satisfies with C₁ ≤ 1.4·10⁹ (§12.5) and what DH's strip-restricted configuration satisfies, with the DH density claim correctly flagged as recalled and not load-bearing (§7.5, §12.4).
* **The four-point accounting and the W_Z convention** check out against `Zeta23/Defs.lean` 164–170, against the γ-coordinate dictionary, and against a two-point instance of my own (§2, §3).
* **`#print axioms`** re-run by me on my own scratch file outside the tree: all nine clean (§1.2).
* **The DH negative control** ran zero-side, fired at the theorem's bandwidth (ratio 6.24) and below it, and the positive control stayed silent; neither caveat undermines it (§11.1).
* **Standing order 7**: Hua–Yang §9 is Lemma G's mechanism and clause 5's shell summation in print, with unspecified constants, at a height-proportional radius, for family-averaged second-order trace data; the single-defect separation statement, the explicit constants, the bandwidth-proportional window, the derivative test with h_f(t) = 0, and the two-sided edge law are not (§11.2).
* **Lint and English**: clean (§11.3). One "cannot" sentence needs a hypothesis or a label (§12.11).

### §13.4 The six points Job 1 asked this check to look at (its SHARED block, 18:26 IST)

* **(a) Lemma G1's step (iii) and the choice k = ⌊√(η/A₁)/e⌋.** Both correct. C(k,i)i^i(k−i)^{k−i} ≤ k^k is one term of the nonnegative binomial expansion of k^k = (i + (k−i))^k, and the second factor i^i(k−i)^{k−i} ≤ k^ik^{k−i} = k^k is immediate; each of the k+1 terms is then ≤ k^{2k}. Verified exhaustively for 1 ≤ k ≤ 39 and every i. The choice of k makes log A₁ + 2log κ − log|η| equal to exactly −2, which is why the bound is (e²/Z)(1+κ)e^{−2κ}; the κ < 1 branch is covered by |B̂| ≤ ∫B = 1 against 1/Z = 4.50 > 1. (§4.2, §4.3.)
* **(b) Clause 2's lower bound — Lemma K's K₃ bound and D(λ) ≥ 0.** Both correct. cosh 3θ = 1 + 18y² + 48y⁴ + 32y⁶ in the variable y = sinh(θ/2), and dropping (1+y²)^{−1/2} ≤ 1 gives the four-term envelope; the Gaussian moments are right. Every constant in the D(λ) chain re-checked at λ ≥ 25 (0.373134, 0.29, 0.234141, 0.647094, 0.52); the only loose step is the parenthetical justification of λE₁ ≤ 0.0045, which a one-line derivative argument fixes and which changes nothing (§12.10). (§5.4.)
* **(c) Clause 5's F̃ and "decreasing from L = 6.1".** Correct, with one wording fix: P is a Laurent polynomial with nonnegative coefficients and top degree 5, for which P′/P ≤ 5/L still holds, so F̃′ < 0 for L > 5/(2c_B√R₀ − 7/4) = 6.073 (§12.7). My own implementation reproduces F̃(50) = −0.133397 and the whole table. (§7.2, §7.3.)
* **(d) (R) → (R′) → t ≥ 21L.** Correct at every step, and 21 is the least integer multiplier (the margin at t = 20L, L = 50 is −1.371). The condition is intrinsic to the route at this c_B (t ≳ 1/(8c_B²)·L) and is not needed for the truth of the clause. (§8.2, §8.3.)
* **(e) The DH control's configuration choice and its two caveats.** The choice — explicit finite Z, Z′, Z″ — is the right one, and neither caveat undermines the control; §11.1 gives the reason in each case, including the observation that an unlocated further off-line orbit inside the window would push the datum further negative, i.e. the control is conservative in the direction that matters.
* **(f) "Is Hua–Yang Lemma 9.1 the same mechanism? I say yes."** **Confirmed at the page.** Lemma 9.1's proof is m integrations by parts against the whole complex exponential, ‖ψ^{(m)}‖₁ ≤ C₀R₀^m(m!)^s, m! ≤ m^m, m = ⌊c₀(L|r − τ|)^{1/s}⌋, the strip weight e^{L|δ|/2} per factor, and "the trivial estimate covers the bounded range omitted by the integer choice of m" — Lemma G's proof, step for step, at s = 2. Their constants are never evaluated, their radius is height-proportional, and their target is a trace norm of second-order family-averaged data. The reading is correct, and so is the note's reduction of its own novelty claim. (§11.2.)

### §13.5 Recommendation

**CLOSES.** The two blind referees (Jobs 3 and 4) may be launched. I recommend the orchestrator append §12 to the note as a dated corrections section **before** they run, because §12.1 and §12.3 are statements a referee will independently find, and §12.2 is a statement a careful referee will call a gap in the theorem's constant list. None of the three is a mathematical defect: the theorem, its eight clauses, and every constant in its chain survive this check intact.

---

## §14 This check's own artifacts and hashes

The transcripts quoted above are complete. All of it is on disk under **`results/c2-m2/verify-O/`**.

| file | what it is |
|---|---|
| `opus_independent.py` / `.log` / `_out.json` | my independent recomputation of Z, κ_∞, κ(λ), m(25), c_B, C_B, c_B′, C_B′, A₁, the θ^{1/4} identity, Lemma G1's Leibniz step (exhaustive for k ≤ 39), G1 against \|B̂\|, F̃ and the least R₀ at both exponent budgets, the (R′) margins at the proved and numerical rates, b₁ and η*, ‖B′‖₁, L₁, and the four-point / tight-pair quadratures |
| `axioms_opus_check.lean.txt` / `axioms_opus_check_run.log` | my `#print axioms` scratch file and its output (the file itself was compiled from the session scratchpad, outside the Lean tree) |
| `rerun-logs/` | the six `_run.log` files from my isolated re-run of the author's scripts (`results/ccm-dh-test` symlinked so `dh_negative_control.py` resolved); byte-identical to `verify/` after the timing lines are stripped |
| (scratchpad `hy.txt`) | my own `pdftotext -layout` extraction of the Hua–Yang PDF (2092 lines), read at §2.2, §5, §9, §12, §13; not copied into the repository, since `fetched-r3/` already holds the PDF and `verify/sources-read-excerpts.txt` the passages |
| `opus_arxiv_queries.log` | my own six arXiv listing queries (terms independent of the author's eight), all 0 entries |

`hashes.txt` of the note's deliverable: **31 of 31 verify** (`shasum -a 256 -c`, 0 failures). Hua–Yang PDF: `465a5c6dc3d6b780f493843b54ca9474b7dedbd83c208f6ad89196a76537a09d`, matching the note.

*End of check. SHA-256 of this file recorded in `results/c2-m2/SHARED.md` and in the final report.*
