# E5 (F2) — the Opus reader's read of the writer's NOTE: the budget-floor constant κ of IV.18 rider (ii)

Reader: Opus 5, Session 29. Started Mon Sep 28 21:53 IST 2026; closed Mon Sep 28 22:20 IST 2026 (machine clock). Inputs hashed at launch and matching the brief: `BRIEF.md` 015d6978…, `PREDERIVATION.md` dfd54af3…, `NOTE.md` 61aa86bd55f264ab… (194 lines), `BARRIER-ZOO.md` 840f4362…, `results/c2-m5/PRICING-next-unit.md` f7a4006c…. Own scripts, logs and JSON are in `results/e5-kappa-s29/verify-O/`. The re-run of the writer's rung-0 scripts is in `verify-O/rerun/`. Sources the reader fetched are in `verify-O/fetched-O/`. NOTE.md and every other existing file were left unedited. Nothing was committed.

## Verdict table

| Row | Verdict | Reader's own evidence |
|---|---|---|
| **K0** (§1) | **UPHELD.** All three of the writer's attack questions are answered correctly: every share is ≥ 0 on the cone, the identity is the on-disk one, and nothing uses RH. κ ≥ 6.34642725586·10⁻¹⁹ reproduced to all 12 printed digits. | `k0_O_run.log`: a(0) from the **definition** (quadrature of sech(πr)A(r), not the closed form) = −0.653846689381654; γ₁ from mpmath; with G = {γ₁} and with the first 30 zeros, ε* passes, 10ε* fails (−1.867·10⁻¹⁸) and ε*/2 passes; the ratio 2Ψ/\|a\| is increasing on [0, 6.30]; the float64 trap is confirmed (`1 − ε == 1.0`). |
| **D′ and the fixed-ε reduction** (§5) | **UPHELD, with one garbled sentence** (A4). The reduction is exact: with ψ̃ = 2πa_ε − σ̂ ≥ 0 and σ ≥ −d̃, multiplying by ε gives ψ = εψ̃, σ_g = εσ, D = εd̃, so κ ≥ ε(2 − d̃). Weak duality is applied correctly: φ = d·du + σ is any positive measure, ∫w dσ = (1/2π)∫ŵσ̂ holds for even w and finite σ, and ψ ≥ 0 is paired with ŵ ≥ 0. | Re-derived by hand (below). The hat discretization makes σ the piecewise-linear interpolant of the s_k, so σ ≥ min s_k. |
| **The certificate re-verified** (`target_dual_eps_s_U8_hu0.01_eps0.03.npy`) | **CERTIFIED.** The reader's κ_lb is **6.5890·10⁻⁵** at the writer's repair η = 2·10⁻⁵, which matches. It is **6.6490·10⁻⁵** at η = 0: the reader's second-derivative verifier needs no repair. One small defect: the certificate has min s_k = −1.99778367191, which is 2·10⁻¹⁰ below the LP's d = 1.99778367172 (HiGHS tolerance), so d must be taken as −min s_k. This moves κ_lb by 4·10⁻¹⁵ and changes no printed digit (A6). | `cert_O.py` → `cert_O_U8_eps0.03_run.log`. Own a(τ) from (2.1) in float64, checked against mpmath at 4002 points to 9·10⁻¹⁴ (`aform_O_run.log`). Own 200 zeros. The Ψ_G part is bounded per cell by π²e^{πh}·min(endpoint values). The σ̂″ bound is M_σ = 747.6. The σ̂ values agree with a BLAS-free long-double loop to 5·10⁻¹⁵. Tail: 2πa(1000) − 4S₀/(hu·10⁶) = 3.35 > 0. Minimum ψ at cell ends is 9.64·10⁻⁵ at τ = 12.436. Spot checks: ε = 0.02 → 5.6485·10⁻⁵ and ε = 0.01 → 4.2003·10⁻⁵ both reproduced. ε = 0.05 fails with ψ(44.71) = −1.23·10⁻⁴, a real dip between the LP's 0.01 fine-grid points beyond τ = 40. |
| **Lemma A and the primal** (§4) | **UPHELD.** Lemma A's approximation w·χ(·/n) (cubic B-spline, K_n of mass 1, K_n ∗ a → a uniformly on compacts) is correct, so 9.985·10⁻⁴ bounds the record's κ, which is the infimum over C²_c. κ_ub = 0.0009985305 is reproduced in τ-space and, independently, in u-space: the two agree to 1.8·10⁻¹⁵. **One attribution is wrong** (A7). The residual in the explicit-formula check comes from the prime tail beyond 10⁷, not from zero or quadrature truncation. | `primal_O_run.log`: ŵ ≥ 0 structurally (c ≥ 0, min 0); support \|τ\| ≤ 14.40. (EF): P(10⁷) = 5.21423·10⁻⁷, Z = 2.72769·10⁻⁷ (γ₂'s share is 1·10⁻¹⁶), (P + Z)/ŵ(0) = 0.00099801, relative −5.2·10⁻⁴. `ptail_O_run.log`: the PNT-density estimate of the tail beyond 10⁷ is 2.51·10⁻¹⁰, calibrated on (10⁶, 10⁷] to 0.2%. It closes the residual to −2.0·10⁻⁴. The anatomy (γ₁ 34.3%, n = 4 35.1%, n = 3 8.0%, …) and w/w(0) at log 2, 3, 4, 5, 7 are reproduced. |
| **Closed form (2.1)** | **UPHELD, re-derived.** Integration by parts (below) gives the boundary term 2h(0) = 1 directly. At τ = 0, 1, 6.31, 30 the closed form, the definition and the reader's u-integral agree to ≤ 2·10⁻³¹ (target 10⁻¹⁰). τ₀ = 6.31003394, I₋ = 2.24152327, a increasing (2·10⁶-point grid). | `aform_O_run.log` |
| **§6** | **UPHELD in substance, with three repairs.** C = 4(1 + (I₋ − 2)/κ) re-derived: the peak μ_y(0) = 1/sin πδ is the maximum, because c/(c² − sin²πy) decreases in c = cosh πξ. The record's "0.24" is ι = 0.2415233. C(κ_ub) = 971.5, the threshold is ℓ′ > 3052.1, C(κ_lb) = 14 666, and ℓ′ > 46 075. Repairs: the μ_y tail bound has sin πδ in the numerator (A9); "δ ≥ 0.097 at ℓ = 10⁴" is the linearized value, while (6.2) itself gives 0.0987 (A10); and "the 1 + ι/κ factor is forced" is a heuristic, not a theorem (A11). Route (α)'s close is correct as stated for the pricing's route (α), which is PRICING-next-unit §1.1(b)'s floor-plus-split. | `sec6_O_run.log`: ∫_{\|ξ\|>7}μ_y = (4/π)sin(πδ)e^{−7π} = 3.58·10⁻¹⁰ at δ = ½. a(3t/4) − log(3t/8π)/2π ≥ −6.0·10⁻⁵ on the sampled t ≥ 28. |
| **Rung 0** (§3) | **UPHELD.** A re-run gives the bracket [0.100000, 0.100001], gap 1.44·10⁻⁶. B re-run gives LP 0.0998183, certified 0.09976834345890817, identical to the writer's, gap 0.23%. Both "known answers" were re-derived by hand. Note that A's lower end is an uncertified window LP value, which the note says. | `verify-O/rerun/rung0A_run.log`, `rung0B_run.log` (994 s) |
| **Prior art** | **UPHELD: no printed κ**, so stop line (iv) does not fire. **The writer missed the nearest classical object in the same cone** (A12): the Odlyzko–Poitou unconditional discriminant bounds, which use F = f/cosh(x/2) with f ≥ 0 and f̂ ≥ 0, the same strip-positive cone and the same explicit formula, with a different functional and normalization (F(0) = 1). Their Open Problem 2.1 is the extremal problem over this cone. Miller 2002 (Lemma 3.1) prints the strip-positivity of C2 line 16. | Read at the page (below) |
| **§7 lines** | **Amend** (A1–A3, A5, A8, A13–A15). Two logged numbers are misreported in §5/§7: the ε = 0.01 row, and an ε-mixed series. The plain-class value at U = 8 comes from an **unconverged** cutting-plane round. The claim that coarser grids at U = 12–32 fail verification is contradicted by the writer's own certified U = 16 and U = 24 runs. None of these moves the bracket. | Every §5 row checked against its `_run.log` (listing in "Checks made") |

**Group-IV decision.** This is a **rider on IV.18 (ii), not an entry.** K0 is one paragraph and is now three-model: orchestrator, writer, reader. The bracket is certified numerics in validated floating point, not interval arithmetic, dual-model at κ_lb = 6.5890·10⁻⁵ and κ_ub = 9.9853·10⁻⁴. **It does not merit two blind referees under 10(d).** The gap is a factor 15, not the factor 2 the brief set for "a lemma for the next digest". The rider closes an existence question and supersedes a price rather than opening a theorem. The first new mathematics, K0, is too short for refereeing to add information beyond the three re-derivations. Two referees become worth their price if a later unit narrows the bracket to within a factor 2 **with interval arithmetic**.

## Checks made (re-derivations and own code)

**(a) K0.** The shares: Re sech(π(ξ − iy)) = 2cos(πy)cosh(πξ)/(cosh 2πξ + cos 2πy), which is > 0 for 0 ≤ y < ½. Every zero of ζ has 0 < Re ρ < 1, so y < ½ always. The orbit of four zeros contributes 2ĝ(t − iy) + 2ĝ(t + iy) = 4Re ĝ(t − iy), using ŵ even and real. The pair ±γ of an on-line zero contributes 2(ŵ ∗ μ₀)(γ) = 2∫ŵΨ_{γ}. Z ≥ 2∫ŵΨ_G then follows by dropping nonnegative terms. The identity is `EF_lit_zetaZeroConfig`, read at the page: `/Users/jaytyagi/rh-lean-work/zeta-23-lean-main/Zeta23/WeilEF/Main.lean` line 270, "theorem EF_lit_zetaZeroConfig : Zeta23.EF.EF_lit zetaZeroConfig". `EF_lit` is at `Zeta23/ExplicitFormula.lean` 81–84, with hypotheses `ContDiff ℝ 2 k → HasCompactSupport k`, `literatureRHS` at 69–73 and `gammaBracket` at 64. Term by term, with g = w/cosh(u/2): the pole terms give 2∫w; the prime term gives Λ(n)n^{−1/2}·2g(log n) = 4Λ(n)w(log n)/(n + 1); and the archimedean term gives ∫(ŵ ∗ μ₀)A, because ∫e^{−iur}/cosh(u/2)du = 2π sech(πr). RH is not used: an off-line zero enters only as a dropped nonnegative orbit share. Numbers are in the verdict table.

**(b) D′.** For w in the cone, with the notation above: B = (1 − ε)(Z + P) + ε(2ŵ(0) + ∫ŵa) ≥ 2εŵ(0) + (1/2π)∫ŵ[4π(1 − ε)Ψ_G + 2πεa]. At fixed ε, write 4π(1 − ε)Ψ_G + 2πεa = ε·2πa_ε with a_ε = a + 2((1 − ε)/ε)Ψ_G. Theorem D for a_ε (d̃, σ ≥ −d̃, ψ̃ ≥ 0) gives (1/2π)∫ŵ·2πa_ε ≥ −d̃ŵ(0). So B ≥ ε(2 − d̃)ŵ(0). The reduction is an identity, not a relaxation. The margin and the repair live in the scaled problem and are paid as ε·η. Using Ψ_G with 200 zeros only weakens the bound, since G is a subset.

**(c) Certificate.** See the verdict row. The reader's method differs from the writer's: second-derivative cells instead of first-derivative ones, a different verifier code path, own zeros, and a BLAS-free cross-check. It closed the whole of [0, 1000] in 1.1·10⁵ cells at depth ≤ 5. The writer needed 1.13·10⁷ cells at depth 15, and the extra η it required was an artifact of the first-derivative bound. The macOS/Accelerate `matmul` RuntimeWarnings in both the writer's and the reader's logs are spurious. The reader asserts that every value is finite and cross-checks against the long-double loop.

**(d) Lemma A and the primal.** χ = cubic B-spline with χ(0) = 1, so w_n = wχ(·/n) ∈ C²_c with w_n ≥ 0 and ŵ_n = ŵ ∗ K_n ≥ 0, where K_n = (n/2π)χ̂(n·) has mass χ(0) = 1. Then ŵ_n(0) → ŵ(0), and ∫ŵ_n a = ∫ŵ(K_n ∗ a) → ∫ŵa because ŵ has compact support and K_n has τ⁻⁴ tails against a growth of log τ. So κ ≤ B(w)/ŵ(0). The u-space formula used for the independent evaluation is the reader's own: ∫ŵa = −log π·w(0) + ∫₀^∞[w(0)e^{−2u}/u − 4w(u)/((e^u + 1)(1 − e^{−2u}))]du. It agrees with the writer's Lemma A2, since ∫₀^∞[e^{−t}/t − e^{−t}/(1 − e^{−t})]dt = ψ(1) = −γ.

**(e) Closed form.** From ψ(x) = ∫₀^∞[e^{−t}/t − e^{−xt}/(1 − e^{−t})]dt, convolving with μ₀ (whose transform is sech(t/4) at frequency t/2) gives 2πa(τ) + log π = ∫₀^∞[e^{−t}/t − 2cos(τt/2)/((e^{t/2} + 1)(1 − e^{−t}))]dt. Now let z = iτ/2 and h(t) = 1/(e^{t/2} + 1). Then (1 − 2z)ψ(½ + z) + 2zψ(1 + z) = ∫[e^{−t}/t − e^{−zt}e^{−t/2}/(1 − e^{−t})]dt + ∫2z e^{−zt}(e^{−t/2} − e^{−t})/(1 − e^{−t})dt, and the second integrand is 2z e^{−zt}h(t). Integrating by parts gives 2h(0) + 2∫e^{−zt}h′dt = 1 + 2∫e^{−zt}h′dt. **This is the boundary term → 1.** Finally, e^{−t/2}/(1 − e^{−t}) − 2h′(t) = 2x²/((x − 1)(x + 1)²) with x = e^{t/2}, which is the kernel above. Taking real parts gives (2.1). Numerical agreement is in the verdict table.

**(f) §6.** See the verdict row, and PRICING-next-unit §1.1(b) ("B(w) ≥ (2 − I₋)ŵ(0) + m·ℓ′/π … C ≈ 4(1 + 0.24/κ)"), which is the assembly re-derived here.

**(g) Rung 0.** A: the exact value 0.1 is attained by the certificate (d₀, σ₀, ψ = 0). For w supported in [−U₁, U₁], ∫w dσ₀ = −d₀∫w. B: p ≥ 0 gives ≥ 0.1, and band-limited squares inside |τ| < 60 give the primal value. The logs match the writer's line for line.

**(h) Prior art (own pass, 2026-09-28).** Web searches: "Odlyzko Poitou discriminant bounds explicit formula test function nonnegative Fourier transform unconditional survey"; "explicit formula positivity nonnegative Fourier transform lower bound conductor Mestre Miller highest lowest zero"; "infimum Weil explicit formula archimedean term doubly positive test functions … certified linear programming". Fetched and read at the page (`verify-O/fetched-O/`, SHA-256 prefixes):
1. **Odlyzko, "Bounds for discriminants and related estimates for class numbers, regulators and zeros of zeta functions: a survey of recent results", J. Théor. Nombres Bordeaux 2 (1990) 119–141 (numdam PDF 2c862713…), pp. 122–123.** The unconditional method "selects F(x) ≥ 0 … and Re(Φ(s)) ≥ 0 for all s in the critical strip, so that the contributions of the prime ideals and zeros are nonnegative. The above nonnegativity conditions … are equivalent to the requirement that [F(x) = f(x)/cosh(x/2)] where f(x) ≥ 0 and f(x) has nonnegative Fourier transform". Also "Open Problem 2.1. What functions f(x) satisfying f(x) ≥ 0 and having nonnegative Fourier transforms give the best unconditional lower bounds for discriminants?" The displayed formulas (2.3)–(2.4) are images and are not in the text layer; the bracketed form is `[reader's reading of the sentence around the image, consistent with C2 line 16]`. **This is the same strip-positive cone and the same explicit formula** (pole term, archimedean term, prime and zero terms all ≥ 0). The difference is the objective: a lower bound for log D normalized by F(0) = f(0) = w(0), per degree n. κ is normalized by ŵ(0) = ∫w and asks for the degree-1 budget's positive floor. It is not κ, but it is the nearest published object, nearer than any the writer lists.
2. **Miller, "The highest-lowest zero and other applications of positivity", arXiv:math/0112196v1 (Duke Math. J. 2002) (b1b78140…), pp. 8–9, Lemma 3.1:** "If an even function g(x)'s Fourier transform is positive on the real line, then the Fourier transform of g(x)/cosh(x/2) is positive in the strip −½ < Im r < ½". This is C2 line 16's strip positivity in print. His test functions are supported in |x| ≤ 2p with p ≤ log 2 and vanish on the prime logarithms: the published instance of "hiding from the primes". Not κ.
3. **Bober–Conrey–Farmer–Fujii–Koutsoliotas–Lemurell–Rubinstein–Yoshida, "The highest lowest zero of general L-functions", arXiv:1211.5996 (cc6a0d7f…):** the same positivity technique. Not κ.
4. The writer's eight arXiv texts (in `fetched/`) were spot-checked at the pages cited for items 1, 4 and 8 (1708.04122 p. 2, the "folkloric problem … Cohn-Elkies problem … Fejér kernel" remark; 2502.05106 §1.3 (EP1); 2608.24827 abstract and Thms 1.1–1.2). The quotations are accurate.
5. Connes–Consani arXiv:2006.13771 and Zhu arXiv:2608.24827 were returned again by the third search. Nothing new.

Verdict: no source prints κ, a value of κ, or inf B(w)/ŵ(0) over the cone. `[novelty: dual-check 2026-09-28, with the Odlyzko–Poitou problem named as nearest object]`.

**(i) Numbers against logs.** §1: `k0_rederive_run.log` ✓. §3: `rung0_run.log` and `rung0B_run.log` ✓. §4: `target_primal_run.log` (0.135976, 0.134298 at 10.5321, and the table X = 3 … 8.5) ✓, `target_primal_fine_run.log` 0.00099853 ✓, `target_primal_decomp_run.log` ✓ (but see A7), `primal_cone_run.log` 0.0018856, with **violations 6263–12 450 still open at every round**; the label `[computed, not certified]` is correct. §5: every table row matches its log **except ε = 0.01** (A1). The plain class: U = 3 at 2.10940 ✓, U = 4 at 2.03888 ✓, U = 6 at 2.004572 (config 7, converged) ✓, **U = 8 at 2.00038 from round 1 of `target_dual_run_C.log` with 1016 violations and min ψ = −0.97, unconverged** (A5; replace every occurrence). Unlisted logs: `target_dual_eps_U16_run.log` has ε = 10⁻³ **CERTIFIED 1.0815·10⁻⁵** (η = 2·10⁻⁵, 3.95·10⁸ cells, 6314 s); `target_dual_eps_U24_run.log` has ε = 2·10⁻³ and 10⁻³ certified (in the table); `target_dual_eps_U12_run.log`: κ̃(10⁻³) = 0.010752 and κ̃(10⁻⁴) = 0.020645. §6: `sec6_O_run.log` ✓.

## Amendments (EXACT; OLD → NEW, in NOTE.md unless stated)

**A1** (§5 table, ε = 0.01 row: its log `target_dual_eps_U8_eps1e-2_m1e-4_run.log` reads "kappa_cert = 4.200298892748442e-05"; the printed certified value exceeds the row's own LP value, which is impossible)
OLD: `| 8 | 0.01 | 0.01 | 10⁻⁴ | 1.995780 | 0.004220 | 4.220e-05 | 6.5890e-05 | η = 2.0e-05, 12.2·10⁶ cells, depth 15 |`
NEW: `| 8 | 0.01 | 0.01 | 10⁻⁴ | 1.995780 | 0.004220 | 4.220e-05 | 4.2003e-05 | η = 2.0e-05, 12.2·10⁶ cells, depth 15 |`

**A2** (§5 reading (ii): 0.0206 is κ̃ at ε = 10⁻⁴, not 10⁻³; the ε = 10⁻³ series saturates)
OLD: `(ii) At fixed ε = 10⁻³, κ̃ grows with the support of the correction: 0.0062, 0.0101, 0.0206 at U = 6, 8, 12 — not the e^{−U} saturation of the plain class but roughly linear in U so far; the runs at U = 16, 24, 32 test where it saturates.`
NEW: `(ii) At fixed ε = 10⁻³, κ̃ grows with the support of the correction and then saturates: 0.0062, 0.0101, 0.0108, 0.0108, 0.0103, 0.0104 at U = 6, 8, 12, 16, 24, 32 (hu = 0.01, 0.01, 0.02, 0.02, 0.04, 0.04; `target_dual_eps_U*_run.log`) — the support of the correction is not what limits the mixed class beyond U ≈ 12 at this ε.`

**A3** (§5 bracket paragraph: the ε-range is stale and a parenthesis is duplicated)
OLD: `the ε-scan at U = 8 (10⁻⁵ … 5·10⁻³) has its certified maximum at the largest ε of the scan that verified (with the LP margin raised to 10⁻⁴; at margin 2·10⁻⁵ the ε ≥ 3·10⁻³ certificates failed the pointwise check) (with the LP margin raised to 10⁻⁴; at margin 2·10⁻⁵ the ε ≥ 3·10⁻³ certificates failed the pointwise check).`
NEW: `the ε-scan at U = 8 (10⁻⁵ … 5·10⁻²) has its certified maximum at the largest ε of the scan that verified, ε = 3·10⁻² (with the LP margin raised to 10⁻⁴; at margin 2·10⁻⁵ the ε ≥ 3·10⁻³ certificates failed the pointwise check at η = 2·10⁻⁵ and verified only at a repair that ate most of κ̃; at ε = 5·10⁻² the LP certificate is negative at τ = 44.71, between the LP's fine-grid points beyond τ = 40 — `verify-O/cert_O_U8_eps0.05_run.log`).`
Also in the same paragraph (string verified present once), OLD: `(coarser hats at U ≥ 12 give LP values of the same size, 0.0103–0.0108 at ε = 10⁻³, but their spikier σ̂ fails the pointwise check by 10⁻⁵ dips near τ ≈ 12 unless the repair η eats most of κ̃)` NEW: `(coarser hats at U ≥ 12 give LP values of the same size, 0.0103–0.0108 at ε = 10⁻³; U = 16 (hu 0.02) verifies at η = 2·10⁻⁵ to 1.0815·10⁻⁵ and U = 24 (hu 0.04) only at η ≥ 1.6·10⁻³, while U = 12 and U = 32 fail by 10⁻⁵-size dips — none exceeds the U = 8 value at the same ε)`.

**A4** (§5 Theorem D′ paragraph: garbled)
OLD: `the plain class is the point ε = 1 (D = d − 2·1 + … : with ε = 1 the Ψ_G term vanishes and 2 − D = 2 − d)`
NEW: `the plain class is the point ε = 1 (the Ψ_G term vanishes, D = d, and the bound reads κ ≥ 2 − d)`

**A5** (§5 plain class and §7(3): the U = 8 value is from an unconverged cutting-plane round)
OLD: `d − 2 = 0.109, 0.039, 0.0046, 0.0004 at U = 3, 4, 6, 8`
NEW: `d − 2 = 0.109, 0.039, 0.0046 at U = 3, 4, 6 and ≥ 0.0004 at U = 8 (the U = 8 figure is round 1 of a cutting-plane LP with 1016 violated constraints, `target_dual_run_C.log` config 8 — a relaxation, so only a lower bound on d − 2)`
Also: OLD `plain duals certify nothing (d − 2 ~ e^{−U})` NEW `plain duals certify nothing at U ≤ 8 (d − 2 = 0.109, 0.039, 0.0046 at U = 3, 4, 6; the e^{−U} reading is inferred from three points)`.

**A6** (§5, certification formula: d must dominate −min s_k; the LP's d is below it by 2·10⁻¹⁰)
OLD: `Certified value κ = ε·(2 − d̃ − η).`
NEW: `Certified value κ = ε·(2 − d_eff − η), d_eff := max(d̃, −min_k s_k) (the LP returns s_k below −d̃ by up to 2·10⁻¹⁰ at solver tolerance; the effect on every certified value is < 10⁻¹⁴).`

**A7** (§4, explicit-formula check: the attribution)
OLD: `(P + Z)/ŵ(0) = 0.0009980 against 0.0009991 from the archimedean side (−0.1%, the size of the zero-sum and quadrature truncation)`
NEW: `(P + Z)/ŵ(0) = 0.0009980 against 0.0009991 from the archimedean side (−0.1%; the zero-sum truncation is ~10⁻¹⁶ — γ₂'s share is 1·10⁻¹⁶ of B — and the residual is the prime tail beyond 10⁷, slowly convergent because w decays only polynomially: for the hx = 0.005 element the reader's check gives −5.2·10⁻⁴ with the sieve to 10⁷ and −2.0·10⁻⁴ after the PNT-density tail estimate 2.5·10⁻¹⁰, `verify-O/primal_O_run.log`, `ptail_O_run.log`; the stated "tail bound 5·10⁻¹⁰" is below the observed residual and is not a bound)`

**A8** (rider and C2 Untried row: contradicted by the writer's own U = 16 and U = 24 logs)
OLD: `coarser grids at U = 12–32 give LP values of the same size but fail the pointwise verification`
NEW: `coarser grids at U = 12–32 give LP values of the same size (κ̃ ≈ 0.0103–0.0108 at ε = 10⁻³); U = 16 (hu 0.02) certifies 1.08·10⁻⁵ and U = 24 (hu 0.04) certifies only after a large repair, neither above U = 8 at the same ε`
OLD: `certificates at hu ≥ 0.02 fail verification by 10⁻⁵ dips near τ = 12`
NEW: `certificates at hu ≥ 0.02 verify only at U = 16 (ε = 10⁻³) or with a large repair; the ε ≥ 5·10⁻² LP misses dips beyond τ = 40, where its fine grid is 0.01`
OLD: `` `[computed, not certified]` = LP values at hu ≥ 0.02 (U = 12, 16, 24, 32) ``
NEW: `` `[computed, not certified]` = LP values at hu ≥ 0.02 for U = 12, 32 and U = 16 at ε = 2·10⁻³ (U = 16 at ε = 10⁻³ and U = 24 are certified, `target_dual_eps_U16_run.log`, `target_dual_eps_U24_run.log`) ``

**A9** (§6, the μ_y tail: sin πδ belongs in the numerator; `sec6_O_run.log`)
OLD: `with ε_t ≤ 4·e^{−πt/4}/(π sin πδ)·… ≤ 10⁻⁹ for t ≥ 28 (Lemma P(iii) of confinement-note §0.3: μ_y(ξ) ≤ 4πδe^{−π|ξ|}·sin(πδ)⁻¹·… — the tail is exponentially small and is absorbed`
NEW: `with ε_t := ∫_{|ξ|>t/4}μ_y ≤ (4/π)(1 + 10⁻⁹)·sin(πδ)·e^{−πt/4} ≤ 3.6·10⁻¹⁰ for t ≥ 28 (from μ_y(ξ) ≤ sin(πδ)cosh(πξ)/sinh²(πξ); checked by quadrature at δ = ½, 0.1, 10⁻³ — the tail is exponentially small and is absorbed`

**A10** (§6 numbers)
OLD: `at ℓ = 10⁴ the layer is δ ≥ 0.097`
NEW: `at ℓ′ = 10⁴ the layer is δ ≥ 0.0987 by (6.2) (0.0972 linearized)`

**A11** (§6, the "forced" sentence: a heuristic, labeled)
OLD: `the 1 + ι/κ factor is forced).`
NEW: `the 1 + ι/κ factor is forced) `[heuristic — it shows each ingredient of the floor-plus-split assembly is individually tight, not that no other configuration-free argument does better; the load-bearing close is about the pricing's route (α), PRICING-next-unit §1.1(b)]`.`

**A12** (§0: add the nearest classical object; append after item 9 and name it in §2's 10(n) paragraph)
OLD: `9. Beurling–Selberg majorants`
NEW: `9′. (Reader's pass, `verify-O/fetched-O/`.) Odlyzko, J. Théor. Nombres Bordeaux 2 (1990) 119–141, pp. 122–123: the unconditional discriminant bounds take F = f/cosh(x/2) with f ≥ 0, f̂ ≥ 0 — the same strip-positive cone with the same explicit formula (Poitou's form), a different functional (log D, per degree, normalized by F(0) = f(0)); Open Problem 2.1 asks for the best such f. Miller, arXiv:math/0112196v1, Lemma 3.1 (pp. 8–9) prints the strip positivity of C2 line 16, with test functions supported in |x| ≤ 2 log 2 that avoid the primes. Neither prints κ; Odlyzko–Poitou is the nearest published object on the same cone.
9. Beurling–Selberg majorants`

**A13** (the rider's label, after this read; also §1's label `[re-derived, dual-model with the orchestrator's pre-derivation; the Opus reader owed]` → `[re-derived, three-model: orchestrator, writer, Opus reader read-O.md]`)
OLD: `writer Fable 5.1, reader Opus 5 owed).]`
NEW: `writer Fable 5.1, reader Opus 5 `read-O.md`).]`
OLD: `` `[re-derived, dual-model: orchestrator's pre-derivation + writer's own script; reader owed]` ``
NEW: `` `[re-derived, three-model: orchestrator's pre-derivation, writer's and reader's own scripts]` ``

**A14** (the rider's certification label: add rigor level and the reader's value)
OLD: `with the pointwise positivity verified on disk;`
NEW: `with the pointwise positivity verified on disk by two independent verifiers (writer: first-derivative cells; reader: second-derivative cells, own a(τ) and zeros; validated floating point, not interval arithmetic; the reader's verifier also certifies the same certificate without repair, κ ≥ 6.649·10⁻⁵ `[single-model]`);`

**A15** (§7 C2 Instruments row: add the nearest object)
OLD: `route (α) closed (C ≥ 972)`
NEW: `route (α) closed (C ≥ 972); nearest published object on the same cone: the Odlyzko–Poitou unconditional discriminant problem (Odlyzko 1990 JTNB, Open Problem 2.1)`

The bracket, C(κ), the e^{3052} and e^{46 000} heights, K0's value and the 10(c) sentence for route (α) all stand as printed. None of A1–A15 moves a load-bearing number.

## Stop lines

(i) does not fire. (ii) does not fire: rung 0 was reproduced. (iii) fires as the writer states: the certified value stalls below 10⁻³, and the bracket is the result. (iv) does not fire: the Odlyzko–Poitou problem is a different functional and is cited, not a printed κ.
