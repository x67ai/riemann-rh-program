# read-O — the Opus 5 reader's check of the D1(b) FORMULATION slot (Session 27, queue item 2)

Opened Fri Sep 25 22:18:06 IST 2026 (machine clock, `date`; each section stamped as it lands). Reader: Opus 5 (the independent second model, standing order 7). Brief: `results/c2-m5b/BRIEF.md` (SHA-256 91cba22f…6fce16976 — recomputed, MATCHES). Note under review: `results/c2-m5b/FORMULATION.md` (SHA-256 1ccce8c2a44b8dcfee263cf3a605e78ab99394a30e7a706315a0f26709d145e5 — recomputed, MATCHES the writer's final value; the earlier a4de4e7d… in SHARED is superseded, as SHARED says). Writer's scripts, recomputed: `archimedean_kernel_check.py` 7579a3bb… MATCHES, `window_residual.py` d7ce65f0… MATCHES, `rung1_newton.py` 7e12c88e… MATCHES. Fetched sources in the session scratchpad: Poltoratski arXiv:0908.2079v2 PDF 378856e9… MATCHES; Bombieri 2000 bdim PDF 20bd544f… MATCHES. The writer's two numeric scripts were also re-run unchanged in the scratchpad: both logs reproduce line for line (timings aside).

Reader's own scripts and logs: `results/c2-m5b/verify-O/` — `archimedean_O.py` → `archimedean_O_run.log` (2 s), `window_residual_O.py` → `window_residual_O_run.log` (108 s; the first run, unbounded Levenberg–Marquardt, is kept as `window_residual_O_run_v1_unbounded_LM.log` — it aliased, see row 4), `window_residual_O_out.json`, `rung1_O.py` → `rung1_O_run.log` (1.8 s). Nothing committed; FORMULATION.md, `zoo-entries-proposed.md`, direction files and the zoo untouched.

## Verdict table

| # | Section | Verdict | One line |
|---|---|---|---|
| 1 | §0 contract (conventions, K_A, (0.3), Lemma 0, class, (0.5)) | FIX-FIRST | K_A, c₁, c_A, the dilation law and Lemma 0 re-derived and CONFIRMED; eq. (0.5) is not an exact identity as written (hard window: missing (2π)⁻¹, convolution undefined, not a convolution for off-line points; the decay rate for R is unsupported) — replaced by an exact band-limited-taper form in which R ≡ 0, which STRENGTHENS the writer's reading |
| 2 | F1(a) | CLOSES (one precision) | re-derived independently (reader's own u-side kernel from μ_∞ via the integral for ψ); agrees; "every ε < min(L, log 2, 1)" must read "every sufficiently small ε" |
| 3 | F1(b), (b′), (c) | CLOSES | re-derived by a different route (scaling test + Vandermonde in γ²); no gap; Lemma 0 correct; (b′) correct |
| 4 | companion numerics (§1.4) | FIX-FIRST (wording) | writer's logs reproduced line for line; the reader's own design reproduces the shape; the "floor" is a best-found upper bound, optimizer-limited below the count (reader reaches 10⁻¹² relative); the V.4 control is REAL (bitwise, genuine quadratic convergence) but LOCAL; the prolate inference is now computed (Jacobian spectrum) |
| 5 | §2 gap / H2 | FIX-FIRST | refutation of H2(i) as an application of Poltoratski is RIGHT; but P1's "C_X = ∞ for every element of the class" rests on "mean gap → 0", which does not give a separated subsequence (clustering); true for every closed set containing ζ's zeros (maximal gap → 0, printed in Bombieri 2000 p. 225); height stratification is by count and must be labeled so in §7; α = ½ and the constant LW/π are right |
| 6 | §3 rung 1 / H3 | FIX-FIRST (one clause) | point counts, P(t)'s, (1 + 7t²)³, Toeplitz matrices and exact minima all reproduced by independent code; the "|c_k|²-relaxation is TIGHT, brief refuted" clause is vacuous — on all three instances rank T_m depends on |c_k| only; the brief's clause is untested, not refuted |
| 7 | §4 Krein / H4 | FIX-FIRST (attributions) | Theorem 4.4 p. 24, ref. [20], t-56a pp. 189–190 read as images — all CONFIRMED; change of variables right; "truncated-Hamburger existence set" is PRICING §5 line 143's phrase, not C2 line 43's; the AH "disjoint by rider B" argument is wrong (AH configurations are lattice SUBSETS, not periodic); literature.md line 29's "(1/p, p)" LOCATED (Bombieri p. 224 example; Connes–Consani p. 2) |
| 8 | §5 contract theorem | FIX-FIRST (one clause) | M5-U / M5-D and the YES / NO shapes are right; the M2 depth confinement "δ < 25/L" overstates M2 (the threshold is L*(t, δ), and (R*)); nearest printed neighbor of M5-U (Bombieri p. 224) to be named |
| 9 | §6 zoo protocol + three riders | FIX-FIRST (riders 2, 3) | protocol items read against the zoo; no existing entry states rider 1, 2 or 3 (grep); rider 1 CLOSES with A1; rider 2 carries the (0.5) and P1 corrections; rider 3's rider-B argument is wrong and must be replaced |
| 10 | §7 DECISION (NO-GO) | CLOSES | NO-GO follows from F1 alone (no finite instance; no dual certificate possible for a program with finitely many variables); the gap and count findings are supporting, not load-bearing; wording of the Poltoratski clause amended |
| 11 | Untried (§7.3) / Instruments (§7.4) texts | FIX-FIRST (wording) | tables' units and formats correct; none restates an existing row; the Poltoratski clause and the "floor" word must be amended as in rows 4–5 |
| 12 | novelty labels | see §12 | F1 packaging → dual-model check 2026-09-25; the Krein-reading novelty stays open (Yoshida 1992, Suzuki not on disk); rider 2's "nothing is printed" is struck (Bombieri p. 224–225) |

**DECISION verdict: CLOSES.** NO-GO for an implementation slot is the right reading. Details in §10.

---

## §1 Row 1 — §0, the contract (landed Fri Sep 25 22:19:04 IST 2026)

**Checks made.** (i) C2 line 14 opened: the datum, A, μ_∞, the strip, the two symmetries, axiom RvM and the conservation system are quoted verbatim in §0.1 — CONFIRMED. (ii) Digest §F: sentences 1, 2, 5, 6, 10, 12, 13 sit at lines 310, 311, 314, 315, 319, 321, 322 of `results/program-digest-s25.md` and are quoted verbatim — CONFIRMED. (iii) PRICING §1.1(v) (line 22) and §1.1(iv) (line 20) quotes — CONFIRMED. (iv) Zoo I.1 line 49 ("Λ_DH(12) = −0.7629 < 0 — the one-line witness") and C2 Instruments line 104 (C₁ ≤ 2.4·10⁹) — CONFIRMED.

**(v) The u-side kernel, re-derived by the reader** `[derivation, reader]`. From μ_∞(τ) = (2π)⁻¹[Re ψ(¼ + iτ/2) − log π] and ψ(z) = −γ_E + ∫₀^∞(e^{−t} − e^{−zt})/(1 − e^{−t})dt (Re z > 0): Fubini is justified by |e^{−t} − e^{−t/4}cos(τt/2)| ≤ t + min(2, τ²t²/8), whose integral against dt/(1 − e^{−t}) over (0, 1] is O(1 + log(1 + |τ|)), integrable against |ĝ(τ)| ≤ C/(1 + τ²) (g ∈ C²_c). Fourier inversion ((2π)⁻¹∫ĝ(τ)cos(τt/2)dτ = g(t/2), (2π)⁻¹∫ĝ = g(0)) and t = 2u give the reader's form

      A_∞(g) = −(γ_E + log π)g(0) − ∫₀^∞[g(u)e^{u/2} − g(0)e^{−u}]/sinh u du.        (R)

It equals the writer's (0.2) iff ∫₀^∞(1 − e^{−u})/sinh u du = 2 log 2 (the integrand is 2e^{−u}/(1 + e^{−u})) — true, so (R) = (0.2) exactly. On u ≠ 0, K_A is the function 2cosh(u/2) − ½e^{|u|/2}/sinh|u| = −1/(2|u|) + O(1); a distribution equal off 0 to a function that is not locally integrable at 0 is not of order 0 there (test φ = 1 on [η, δ/2], supp φ ⊂ [0, δ]: ⟨K_A, φ⟩ ≍ −½log(1/η) while ‖φ‖_∞ = 1), so **K_A is not a Radon measure near 0** — the writer's statement, CONFIRMED. Dilation law, reader's closed form: A(g_ε) = g(0)log(1/ε) + a(g) + O(ε), a(g) = −∫₀¹(g(v) − g(0))v⁻¹dv + g(0)[K − c₂ − γ_E − log π], K := ∫₀¹(e^{w/2}/sinh w − 1/w)dw + ∫₁^∞e^{w/2}/sinh w dw, c₂ := ∫₀^∞(e^{u/2} − e^{−u})/sinh u du (supp g ⊂ [−1, 1]). `[computed, reader]` (`verify-O/archimedean_O_run.log`): identity 2 log 2 to 20 digits; c₁ = 2.2639435073548, c_A = 5.3721834192257 (writer's values CONFIRMED); (R) against the direct τ-integral with scipy's complex digamma and QAWO transforms (a different quadrature from the writer's mpmath one): −1.71873149397 vs −1.71873149399 for (1 − u²)³ and −2.43966910262 vs −2.43966910262 for (1 − (u/2)²)⁴ (|τ| ≤ 400; differences 2.8·10⁻¹¹, 3.2·10⁻¹²). For g = (1 − u²)³: predicted a(g) = −1.49842606464; A(g_ε) − log(1/ε) = −0.6935527, −1.3383454, −1.4664238, −1.4904259, −1.4968261, −1.4981061 at ε = 0.5 … 2·10⁻⁴ — the writer's six values reproduced to every printed digit — and minus a(g) the remainders are 0.80, 0.160, 0.032, 0.0080, 0.0016, 0.00032: **O(ε) with constant ≈ 1.6**, so the writer's "o(1)" is O(ε).

(vi) Lemma 0 — CONFIRMED (the odd part pairs to 0 with an even distribution; the even part is a C²_c test).

**(vii) Eq. (0.5) — FIX-FIRST.** The writer flagged it; the reader finds three defects in the hard-window form and one exact replacement. (a) For an on-line configuration Σ_{γ∈window}m_γe^{−iuγ} = (2π)⁻¹(E_ν ∗ ŵ_W)(u) — the factor (2π)⁻¹ is missing. (b) E_ν is a distribution (for off-line points not even tempered: cosh(yu) growth summed over infinitely many orbits) and ŵ_W decays like 1/|u|; the convolution is not defined in general, so "an exact identity of distributions" is not available. (c) For an off-line point x ± iy the windowed term 1_W(x)e^{−iux}·2cosh(uy) is not a convolution in u of E_ν with ŵ_W: (2π)⁻¹∫ŵ(v)e^{ivγ}dv = w(γ) needs w entire. (d) "for L ≥ ℓ it is a tail term … decay (W(L − ℓ))^{−3} per unit of out-of-band mass" is not supported: E_ν's out-of-band mass is infinite (for ζ it equals K_A − π off the band, with the 2cosh(u/2) growth cancelled only on average by the comb). **Exact replacement `[derivation, reader]`:** take a BAND-LIMITED taper, w ∈ L¹ with ŵ ∈ C_c^∞(−ε, ε) (w is entire of exponential type ε), w_T(τ) := w(τ − T), and ĉ_{T,w}(u) := Σ_γ m_γw(γ − T)e^{−iuγ}. Then ĉ_{T,w} = (2π)⁻¹E_ν ∗ ŵ_T holds exactly for on- and off-line points alike (Fourier inversion of w at complex γ, |Im γ| ≤ ½), and ĉ_{T,w}(u) depends only on E_ν on (u − ε, u + ε). **On the class 𝒦_L(π), every soft-windowed transform at |u| ≤ L − ε is therefore a functional of F_π alone — R ≡ 0 exactly — and every two-moment row built from such transforms at |u_k| ≤ L − ε (the Frobenius row at L ≥ ℓ + ε included) is the datum's.** This is stronger than the writer's "up to leakage" and gives the brief's requested derivation ("a functional of F_π alone, say so and derive it") without a leakage term; the configuration's freedom is visible only to hard-window rows and to rows at |u| ≥ L − ε. The consequences (i)–(ii) the writer draws stand in this form.

**Amendments (row 1)** — each OLD occurs once in FORMULATION.md (checked by script):

**A1-1** (FORMULATION.md) OLD:
```text
Now ĉ_{T,W} = E_ν ∗ ŵ_W with w_W the window's indicator (or a C² taper of it) and ŵ_W(u) = e^{−iu(T+W/2)}·2sin(uW/2)/u — an exact identity of distributions, because multiplying ν by the window is convolving its transform by the window's transform.
```
NEW:
```text
Now, for an on-line configuration and formally, ĉ_{T,W} = (2π)⁻¹E_ν ∗ ŵ_W with w_W the window's indicator and ŵ_W(u) = e^{−iu(T+W/2)}·2sin(uW/2)/u. [CORRECTION, Opus reader, read-O.md §1: with a hard window this is not an exact identity — the convolution of the distribution E_ν with the slowly decaying ŵ_W is not defined in general, and an off-line point's windowed term 1_W(x)e^{−iux}·2cosh(uy) is not a convolution in u. The exact form uses a band-limited taper: w ∈ L¹ with ŵ ∈ C_c^∞(−ε, ε) (w entire of exponential type ε), w_T(τ) := w(τ − T), ĉ_{T,w}(u) := Σ_γ m_γw(γ − T)e^{−iuγ}; then ĉ_{T,w} = (2π)⁻¹E_ν ∗ ŵ_T exactly, for on- and off-line points alike, and ĉ_{T,w}(u) depends only on E_ν on (u − ε, u + ε).]
```

**A1-2** (FORMULATION.md) OLD:
```text
R is the sinc-tail contribution of the configuration's transform OUTSIDE the band; it is the ONLY channel through which the configuration's freedom enters any two-moment row, and for L ≥ ℓ it is a tail term (the window kernel at distance ≥ L − ℓ from the band edge; with a C² taper, decay (W(L − ℓ))^{−3} per unit of out-of-band mass).
```
NEW:
```text
R is the configuration's out-of-band content seen through the hard window's kernel; with a hard window (0.5) is a formal display (`I infer`), and no decay rate for R is proved (E_ν carries infinite out-of-band mass; the rate "(W(L − ℓ))^{−3} per unit of out-of-band mass" is withdrawn). [CORRECTION, Opus reader: with the band-limited taper above, R ≡ 0 EXACTLY at every |u| ≤ L − ε — on the class every soft-windowed two-moment row at |u_k| ≤ L − ε, the Frobenius row at L ≥ ℓ + ε included, is a functional of F_π alone, and the configuration's freedom enters only through hard-window rows or rows at |u| ≥ L − ε.]
```

---

## §2 Row 2 — Theorem F1(a), re-derived independently (landed Fri Sep 25 22:19:04 IST 2026)

**The reader's proof.** Let ν be finite, total mass M = Σm_γ, and g even C² with supp g ⊂ [−1, 1], g(0) = 1. For ε < L the dilate g_ε is admissible. Zero side: ĝ_ε(z) = εĝ(εz) and |ĝ(z)| ≤ e^{|Im z|}‖g‖₁ for supp g ⊂ [−1, 1], so |W_ν(g_ε)| ≤ εe^{ε/2}‖g‖₁M → 0. Prime side: for ε < log 2 the interval (−ε, ε) contains no ±log n with n ≥ 2, so ∫g_ε dπ = 0 (or the constant 2Λ_π(1) if a datum admitted an atom at log 1 = 0 — immaterial). Archimedean side: by (R) and the dilation computation of §1(v), A(g_ε) = log(1/ε) + a(g) + O(ε) → +∞. So (0.1) fails for all sufficiently small ε — how small depends on M and g, not only on L. The "more generally" clause is (0.1) read on g_ε. **Agreement with the writer: complete, except that the writer's statement says "for every ε < min(L, log 2, 1)", which is false as written for configurations of large mass (for g = (1 − u²)³ at ε = ½, A(g_{1/2}) = log 2 − 0.6936 ≈ −0.0004, which a configuration's W_ν(g_{1/2}) can match); the proof in §1.2 is right and says "for all small ε".** The reader's kernel differs in shape from the writer's ((R) subtracts g(0)e^{−u}, not g(0)) and agrees after the 2 log 2 identity.

**A2-1** (FORMULATION.md) OLD:
```text
the system (0.1) fails on the dilated even bumps g_ε (§0.2) for every ε < min(L, log 2, 1), quantitatively
```
NEW:
```text
the system (0.1) fails on the dilated even bumps g_ε (§0.2) for every sufficiently small ε — ε < min(L, log 2) and so small that g(0)log(1/ε) + a(g) + O(ε) exceeds εe^{ε/2}‖g‖₁ν(S), a threshold depending on ν(S) and g [precision, Opus reader] — quantitatively
```

---

## §3 Row 3 — Theorem F1(b), (b′), (c), re-derived by a different route (landed Fri Sep 25 22:19:04 IST 2026)

**The reader's proof of (b).** μ := ν − ν₀ is finite, signed, integer-atomic and symmetric under γ ↦ −γ (both ν and ν₀ are). Subtracting the two systems: for every even g ∈ C²_c(−L, L), ∫g(u)p(u)du = Σ_{log n<L} c_n·2g(log n), with p(u) := Σ_{γ∈supp μ}μ({γ})cos(γu) = Σ_{[γ]}n_{[γ]}cos(γu) (sum over sign classes [γ] = {γ, −γ}, n_{[γ]} := μ({γ}) + μ({−γ}) = 2μ({γ}) for γ ≠ 0), and c_n := (Λ_{π₀}(n) − Λ_π(n))n^{−1/2}. *Step 1 (atoms vanish; even tests only).* Fix n with 0 < log n < L and φ ∈ C_c^∞(−1, 1) even, φ(0) = 1; for k large the even test g_k(u) := φ(k(u − log n)) + φ(k(u + log n)) is supported in (−L, L) away from the other atoms, ∫g_k p = O(1/k) (p is bounded near ±log n), and the right side is Σ_m c_m[g_k(log m) + g_k(−log m)] = 2c_n(φ(0) + φ(2k log n)) = 2c_n for k large. So c_n = 0; n = 1 likewise with g_k(u) = φ(ku). *Step 2.* Then ∫gp = 0 for all even g ∈ C²_c(−L, L); p is even and continuous, so p ≡ 0 on (−L, L). *Step 3 (Vandermonde, not analytic continuation).* p^{(2j)}(0) = (−1)^jΣ_{[γ]}n_{[γ]}γ^{2j} = 0 for every j ≥ 0. The numbers γ² over distinct sign classes are distinct (γ² = γ′² ⟺ γ′ = ±γ, for complex γ too), so the finitely many unknowns n_{[γ]} satisfy a Vandermonde system in the distinct nodes γ² with infinitely many rows: all n_{[γ]} = 0, hence μ = 0 by the symmetry. ∎ **Comparison.** The writer's route (density of U = (−L, L) ∖ atoms, continuity, entire-ness, linear independence of exponentials) and the reader's (scaling tests at each atom, Vandermonde in γ²) reach the same statement with the same hypotheses; neither uses positivity of π, the strip, or RvM. One precision in the writer's text: "the exponents {±γ : γ ∈ Γ} are pairwise distinct complex numbers" fails for γ = 0 (a point at ρ = ½, where +0 = −0); the argument survives (cos(0·u) = 1 is one more independent function), and the Vandermonde route has no such case. No amendment is required. **(b′)** CONFIRMED: E_μ(u)cos(Tu) is a real even entire function; Step 1 kills c_n cos(T log n); Step 2 gives E_μ·cos(T·) = 0 on (−L, L), hence E_μ = 0 off the isolated zeros of cos(Tu), hence on (−L, L) by continuity; Step 3 as above. **(c)** cited correctly (rider B, BARRIER-ZOO.md line 422, its READ block line 423). **Corollary F1-C** follows: a program with finitely many position/mark variables is either finite (F1(a)) or a finite modification of a fixed global configuration (F1(b)); the feasible set is empty or the single point. CONFIRMED.

---

## §4 Row 4 — the companion numerics (§1.4), re-run from the reader's own script (landed Fri Sep 25 22:22:16 IST 2026)

**Design check of the writer's final version.** The envelope S(u) = Σ_k e^{−i(γ_k − T)u} is band-limited to |ξ| ≤ W/2 only while every position stays in the window; the writer's bounds [γ₁ − 1, γ₄₀ + 1] keep |τ − T| ≤ 20.6, so the Nyquist spacing is π/20.6 = 0.152 against the 0.02 grid — SOUND; the off-grid check on a 0.005 grid including the excluded windows is the right guard. The exclusion |u − log n| < 0.1/n is immaterial for this object (the windowed envelope has no prime atoms): the reader's variant without it gives the same picture (row values below). The aliasing trap the writer records is real — the reader fell into it independently: an unbounded Levenberg–Marquardt first run (`verify-O/window_residual_O_run_v1_unbounded_LM.log`) returned the SAME grid residuals as the bounded run but off-grid max |E| = 4.0–4.8 at L = 2–3.5, because a point displaced by 2π/h = 157.08 is invisible on a grid of spacing h = 0.04; bounding the positions removed it (off-grid 8.6·10⁻⁴ … 1.1 in the final run).

**Reader's design** (`verify-O/window_residual_O.py`): zeros recomputed with `mpmath.zetazero` (identical to the writer's JSON, max difference 0); grid 0.04 with no atom exclusion; bounded trust-region fits with CONTINUATION in L (ascending and descending sweeps warm-started from neighboring L's, plus 12 fresh merge-starts by the reader's own merge rule); the Jacobian's singular values at ζ's positions; controls from σ = 0.15 and σ = 0.5. 108 s.

**Results.** (a) *Jacobian spectrum* (new): #singular values above 10⁻⁶ of the largest = 15, 23, 29, 35, 40, 40 at L = 0.5, 1, 1.5, 2, 2.5, 3 (counts LW/π = 6.2, 12.5, 18.7, 24.9, 31.2, 37.4); smallest relative singular value 5·10⁻¹⁷, 2·10⁻¹⁷, 5·10⁻¹⁷, 3.2·10⁻¹¹, 2.0·10⁻⁶, 1.8·10⁻² — the prolate-type plunge, computed. (b) *26s + 7d best-found relative residual* (reader / writer): L = 0.5: 1.5·10⁻¹² / 1.2·10⁻¹⁰; 1: 2.1·10⁻¹² / 2.1·10⁻⁹; 1.5: 1.0·10⁻⁹ / 1.3·10⁻⁸; 2: 2.9·10⁻⁵ / 5.7·10⁻⁶; 2.5: 1.0·10⁻² / 9.0·10⁻³; 3: 6.1·10⁻² / 5.0·10⁻²; 3.5: 8.1·10⁻² / 7.2·10⁻²; 4: 0.149 / 0.130; 5: 0.204 / 0.175; ℓ: 0.350 / 0.325; 8: 0.556 / 0.526; 12: 0.595 / 0.573. 28s + 6d: the same pattern (8.0·10⁻¹³ … 0.555 against the writer's 8.4·10⁻¹¹ … 0.528). The writer's-grid variant (0.02 + exclusion, warm-started) gives 2.2·10⁻⁵, 4.6·10⁻², 0.320 at L = 2, 3, ℓ. **Reading: the shape is reproduced (tiny below count ≈ 25–31, 1 %–60 % above); every entry is an UPPER bound on the infimum; below the count the writer's numbers are optimizer-limited (the reader's go 100–1000× lower); above it the writer's are the better bounds by 5–20 %. "The floor" is the wrong word.** (c) *Control* (V.4): from σ = 0.15, 40 simples: L = 1, 2 other positions (max deviation 0.25, 0.053; RMS 6.6·10⁻⁹, 1.7·10⁻¹⁰); L = 2.5 recovered to 4.2·10⁻¹⁰; L ≥ 3 recovered BITWISE (residual exactly 0.0 after 7–8 evaluations: Gauss–Newton converges quadratically and the last step rounds onto the floating-point zeros — the writer's "0.0" is genuine, not a bug). From σ = 0.5: recovered at L = 2.5, 3, 3.5; at L = 5, ℓ, 12 the fit stops in local minima with RMS 0.64, 0.64, 3.1 (deviation 1.3, 0.76, 1.0). **The control is REAL and LOCAL** — it tests local identifiability, which the Jacobian spectrum places between count 25 and 31. The writer's reading (ii) ("pinning by count at α = ½") is consistent with all of this; its reading (iv) is now computed in its local form.

**A4-1** (FORMULATION.md) OLD:
```text
*Result — the floor tracks the Slepian count.*
```
NEW:
```text
*Result — the best-found residual tracks the Slepian count.* [precision, Opus reader, read-O.md §4: each entry is the best of 12 starts, an UPPER bound on the infimum over positions, not a floor; below the count it is optimizer-limited — the reader's bounded continuation fits reach 1.5·10⁻¹² / 2.1·10⁻¹² relative at L = 0.5 / 1 (26s + 7d) and 8.0·10⁻¹³ / 1.3·10⁻¹² (28s + 6d), `verify-O/window_residual_O_run.log` — and above the count the values below are the better bounds by 5–20 % over the reader's.]
```

**A4-2** (FORMULATION.md) OLD:
```text
the ζ positions are recovered EXACTLY (residual 0.0, deviation 0.0): the instrument fires where it should and is silent where it should.
```
NEW:
```text
the ζ positions are recovered EXACTLY (residual 0.0, deviation 0.0 — bitwise: the Gauss–Newton steps converge quadratically onto the floating-point zeros in 7–8 evaluations; reproduced by the Opus reader) from starts within σ = 0.15 of ζ's zeros: the instrument fires where it should and is silent where it should. [precision, Opus reader: this is a LOCAL identifiability test — from σ = 0.5 starts the fit stops in nonzero-residual local minima at L = 5, ℓ, 12 (RMS 0.64, 0.64, 3.1); the reader's Jacobian spectrum at ζ's positions puts the onset of local identifiability between count 25 and count 31 (smallest relative singular value 3.2·10⁻¹¹ at L = 2, 2.0·10⁻⁶ at L = 2.5, 1.8·10⁻² at L = 3), and the σ = 0.15 control already recovers the zeros to 4·10⁻¹⁰ at L = 2.5 (count 31 < 40).]
```

**A4-3** (FORMULATION.md) OLD:
```text
(`I infer` the identification; the eigenvalues were not computed)
```
NEW:
```text
(the identification was `I infer` here; the Opus reader computed its local form — the singular values of the fit's Jacobian at ζ's 40 positions fall to 10⁻¹¹–10⁻¹⁷ relative past the count, 15 / 23 / 29 / 35 of them above 10⁻⁶ at L = 0.5 / 1 / 1.5 / 2 against counts 6 / 12 / 19 / 25, i.e. the plunge region of width ≈ 10 around the count, `verify-O/window_residual_O_run.log` (4))
```

**A4-4** (FORMULATION.md) OLD:
```text
(i) The theorem's "not zero" is 10⁻⁹–10⁻⁵ relative below the count
```
NEW:
```text
(i) The theorem's "not zero" is below 10⁻⁵ relative under the count (writer's fits 10⁻¹⁰–10⁻⁵; the reader's 10⁻¹²–10⁻⁵ — optimizer-limited, so the true infimum there is not measured)
```


---

## §5 Row 5 — §2, the gap theorem and H2 (landed Fri Sep 25 22:22:16 IST 2026)

**Poltoratski at the page** (arXiv:0908.2079v2, the writer's PDF, hash verified; pages of the arXiv version): (2.1) p. 5, G_X for "finite Borel complex measures" with μ̂ = 0 on [0, a] (a ONE-sided gap of length a; the class's (−L, L) is length 2L — immaterial here); short/long sequences (5.2) and a SHORT PARTITION I_n = (a_n, a_{n+1}] with a₀ = 0 and |I_n| → ∞ (p. 8); the main definition (5.3)–(5.5); Remarks 2–6; Example 1 (p. 10: "for separated sequences Λ the energy condition disappears and G_Λ = d_i(Λ)" — printed without 2π, as the writer notes); Theorem 2 (p. 10) "G_X = 2πC_X"; §7 p. 32 d_BM and Lemma 1; Lemma 2 (p. 32–33). **Every quotation in §2.1 is CONFIRMED verbatim.**

**The density required vs the density used — the refutation of H2(i) is RIGHT.** The theorem's C_X is a supremum over subsequences of a Beurling–Malliavin interior density on short partitions going to infinity, with an energy condition, for supports of FINITE complex measures (P2); the brief's H2(i) inserted a local density at one height (≤ ℓ/π per unit τ) into it. That is a category error, and P2 alone (the class's μ is infinite, integer-weighted, with positivity constraints on ν₁, ν₂; nothing in the paper speaks to it) suffices to refute "H2(i) follows from the gap theorem".

**P1's derivation has a gap, and its conclusion holds for ζ's zero set by a printed fact.** P1 builds a subsequence separated with spacing in [1/(2a), 1/a] "because the mean gap 2π/log R → 0 … the count in I_n is (|I_n|/2π)log R_n(1 + o(1)) ≫ a|I_n|". A large count in I_n does not give a separated subsequence of density a: the points may cluster (all of them inside one sub-interval of length 10⁻⁹, say), and then a separated subsequence has density ≤ 1/(cluster spacing), while a non-separated one can fail the energy condition (5.4) when within-cluster distances shrink fast enough with height (the reader's estimate: distances e^{−x} at height x make the energy sum diverge logarithmically on the |I_n| = √x partition). What is needed is that the MAXIMAL gap tends to 0: then one point from every other cell of length 1/(4a) gives a subsequence separated by ≥ 1/(4a) with ≥ 2a|I| − 2 points in I, and the writer's partition (|I_n| = √dist) plus Example 1 give C_X ≥ a. **For ζ's zero set the maximal gap does tend to 0, and this is printed where the writer already looked: Bombieri 2000 p. 225 (vol. pagination), "As pointed out by J. Bourgain, the existence of linear relations over intervals of arbitrary length also follows from the fact that the gap between consecutive γ's tends to 0 as γ → ∞"** `[read at the page, reader]` — which is the same conclusion (G = ∞ for ζ's zeros, in the language of linear relations of x^{−ρ}) with the same mechanism. Since G_X is monotone in X by (2.1), G_X = ∞ for every closed X ⊇ ζ's zeros, in particular for X = supp ν_ζ ∪ supp ν, the case M5-U needs. For a GENERAL element ν of 𝒦_L(π) the reader derives only: the band identity on modulated tests h(u)cos(xu) (ĥ = |φ̂|² ≥ 0, supp h ⊂ (−L, L)) has a bounded prime side (∫|h|dπ_L < ∞) and an archimedean side ≍ ĥ-weighted log x, so every interval of a fixed length D(L) at height x carries ≍ log x points — C_X ≥ 1/(2D(L)), finite — and nothing at smaller scales. **The refutation of H2(i) survives; P1's universal claim must be restricted.** (The writer's statement that the local density is ≍ log|x| "by F1(a)" is also not right as a derivation — F1(a) reads a global smoothed count; the band identity on modulated tests is what gives it; amendment A5-5.)

**The height stratification.** α(T) = L/log(T/2π) ≥ 1 ⟺ T ≤ 2πe^{L}, α ≥ ½ ⟺ T ≤ 2πe^{2L} — CONFIRMED. "Free above 2πe^{2L}" follows from the COUNT alone (clause R3 labels it so, correctly); it is not a consequence of anything cited, and §7.1, §7.2 and the Instruments row must carry "by count" (A10-2; A11-1/2 carry the Poltoratski restriction). **The Slepian constant.** A real signal on a window of length W with transform supported in (−L, L) has 2L·W/2π = LW/π real degrees of freedom; with W = 2πN/ℓ this is 2αN, and the evenness of E_ν (only the cosine transform on (0, L) is data) does not change it (the even extension lives on two windows of total length 2W with the symmetry halving the count). The threshold 2αN = N is α = ½ — CONFIRMED, constant right. The reader's Jacobian spectrum (row 4) shows the numerical onset of local identifiability at counts 25–31 for 40 positions — the plunge region, consistent with the count as a count.

**A5-1** (FORMULATION.md) OLD:
```text
and for supports whose local density grows like log τ that characteristic is infinite.
```
NEW:
```text
and for every closed set containing ζ's zeros that characteristic is infinite (the maximal gap of ζ's zeros tends to 0 — Bombieri 2000 p. 225 — which yields separated subsequences of every density; for a general element of the class only a local density at scale D(L) ≍ 1 is known, and C_X = ∞ is not proved there — correction by the Opus reader, read-O.md §5).
```

**A5-2** (FORMULATION.md) OLD:
```text
Let X be the support of any configuration whose counting function satisfies N_X(R) ≥ (1 − o(1))(R/2π)log R (ζ's zeros, or any element of the class).
```
NEW:
```text
Let X be any closed set containing ζ's zero set — for instance X = supp ν_ζ ∪ supp ν for any ν ∈ 𝒦_L(Λ), the case M5-U needs; G_X is monotone in X by (2.1). [CORRECTION, Opus reader: the draft took X = the support of any configuration whose counting function satisfies N_X(R) ≥ (1 − o(1))(R/2π)log R; a counting-function (mean-gap) hypothesis does not give the separated subsequence used below — the points of I_n may cluster.]
```

**A5-3** (FORMULATION.md) OLD:
```text
choose a subsequence Λ_a ⊂ X that is separated with spacing in [1/(2a), 1/a] beyond some height R_a (possible because the mean gap 2π/log R → 0, with the finitely many exceptional stretches absorbed by taking |I_n| → ∞ — the count in I_n is (|I_n|/2π)log R_n(1 + o(1)) ≫ a|I_n|)
```
NEW:
```text
choose a subsequence Λ_a ⊂ X that is separated with spacing ≥ 1/(4a) and with at least one point in every other cell of length 1/(4a) beyond some height R_a (so #(Λ_a ∩ I) ≥ 2a|I| − 2 ≥ a|I| on intervals of length ≥ 2/a) — possible because the MAXIMAL gap between consecutive ordinates of ζ's zeros tends to 0 (Bombieri 2000 p. 225, `[read at the page, Opus reader]`: "the gap between consecutive γ's tends to 0 as γ → ∞", with Bourgain's consequence "the existence of linear relations over intervals of arbitrary length")
```

**A5-4** (FORMULATION.md) OLD:
```text
**G_X = ∞: the support of every element of the class carries finite complex measures with arbitrarily long spectral gaps.**
```
NEW:
```text
**G_X = ∞: every closed set containing ζ's zeros carries finite complex measures with arbitrarily long spectral gaps** (for a general element of the class the reader's derivation gives only C_X ≥ 1/(2D(L)): the band identity with modulated tests h(u)cos(xu), ĥ ≥ 0, forces ≍ log x points in every interval of a fixed length D(L) at height x, and nothing at smaller scales).
```

**A5-5** (FORMULATION.md) OLD:
```text
and for configurations carrying the archimedean density (every element of the class, by F1(a)) the local density is ≍ (1/2π)log|x| → ∞.
```
NEW:
```text
and for every element of the class the local density at a fixed scale D(L) is ≍ log|x| → ∞ (not by F1(a), which reads only a global smoothed count, but by the band identity on modulated tests h(u)cos(xu) with ĥ ≥ 0 and the bounded prime side ∫|h|dπ_L — Opus reader's derivation).
```

---

## §6 Row 6 — §3, rung 1 and H3 (landed Fri Sep 25 22:23:03 IST 2026)

**Reader's independent computation** (`verify-O/rung1_O.py`, 1.8 s): own F_{7ⁿ} arithmetic (irreducible moduli found by search), own counts #C(F_{7ⁿ}) = 7ⁿ + 1 + Σ_x χ(f(x)) for odd-degree f (one point at infinity), own Newton identities in exact Fractions, own functional equation, own power-sum prediction for n ≤ 4, own root moduli, own Toeplitz ranks with every sign pattern of c₁…c_m. **Reproduced exactly:** g = 1: N = 5, 55, 380, 2475, P = 1 − 3t + 7t²; g = 2 (y² = x⁵ + 3x + 1, gcd(f, f′) = 1 mod 7): N = 11, 55, 371, 2419, P = 1 + 3t + 7t² + 21t³ + 49t⁴, four distinct roots; g = 3 (y² = x⁷ + x + 1, gcd(f, f′) = 1): N = 8, 92, 344, 2108, s = 0, −42, 0, 294, **P = (7t² + 1)³ — CONFIRMED, two distinct Frobenius points ±i√7 of mark 3**; every |α_i|² = 7; predicted s_{g+1}…s₄ match the brute-force counts on all three curves. The brief's y² = x⁵ + x + 1 is indeed singular mod 7: x⁵ + x + 1 ≡ (x − 2)(x + 3)²(x² + 3x − 2). **Exact minima below g:** g = 2, m = 1: N_d = 1 would need s₁ = ±4√7 ≠ −3; N_d = 2 by (1 − bt + 7t²)² with b = −3/2 — minimum 2 = rank T₁, CONFIRMED; g = 3, m = 1: minimum 2, attained by (1 − 7t²)³ and (1 + 7t²)³ (and, among N_d = 2 patterns, only these: a conjugate pair of mark 3 needs cos θ = 0; R₊ᵃR₋ᵇ needs a = b = 3; off-circle orbits have 4 points or break s₁ = 0); g = 3, m = 2: only (1 + 7t²)³ (s₂ = −42 excludes (1 − 7t²)³, s₂ = +42) — CONFIRMED; T₂ has eigenvalues 12, 6, 0 (rank 2 < 3: the Carathéodory uniqueness case, as the writer says). **The relaxation clause is vacuous:** the reader's sign-flip ranks are identical on every instance ({(±1): 2} for T₁ on g = 2 and g = 3; all four sign patterns rank 2 for T₂ on g = 3), because rank T₁ depends on |c₁| alone and at g = 3, m = 2 c₁ = 0. So "the |c_k|²-relaxation is TIGHT … the brief refuted" is not supported; the brief's clause is untested. Rung-1 clause (a) (g counts pin P(t), marks included) and the genus-3 triple stand. Rungs 0, 2, 3: citations CONFIRMED (PRICING §2 and §1.2(b); zoo I.1 line 49; `results/c3-m0-epstein/n1_epstein_witness.{py,json}` present).

**A6-1** (FORMULATION.md) OLD:
```text
and the two-moment-type relaxation is TIGHT there, not "NOT tight" as the brief inferred)
```
NEW:
```text
and the two-moment-type relaxation coincides with it there — for a structural reason: on these instances rank T_m depends on the moduli |c_k| alone — so the brief's "NOT tight" is UNTESTED, not refuted [correction, Opus reader])
```

**A6-2** (FORMULATION.md) OLD:
```text
**the brief's "below that the two-moment relaxation is NOT tight" is refuted on these instances** (it may hold on others; none was found among the three)
```
NEW:
```text
**the brief's "below that the two-moment relaxation is NOT tight" is UNTESTED by these instances, not refuted** [CORRECTION, Opus reader, read-O.md §6]: at m = 1, rank T₁ depends on |c₁| only; at g = 3, m = 2, c₁ = 0 and rank T₂ depends on |c₂| only (the reader's sign-flip ranks are identical on every instance, `verify-O/rung1_O_run.log`), so the |c_k|²-relaxation cannot differ from the exact problem there. A test needs m ≥ 2 with c₁c₂ ≠ 0, where det T₂ = c₀³ − 2c₀c₁² + 2c₁²c₂ − c₀c₂² changes with the sign of c₂
```

**A6-3** (FORMULATION.md) OLD:
```text
below g the exact min N_d = the Toeplitz rank bound on all three instances and the \|c_k\|²-relaxation is tight;
```
NEW:
```text
below g the exact min N_d = the Toeplitz rank bound on all three instances, and the \|c_k\|²-relaxation coincides with it only because rank T_m depends on \|c_k\| alone there (the brief's "NOT tight" untested — Opus reader);
```

**A6-4** (FORMULATION.md) OLD:
```text
the brief's "the two-moment relaxation is NOT tight below g" → (i) refuted on three instances (§3.1), no zoo line;
```
NEW:
```text
the brief's "the two-moment relaxation is NOT tight below g" → (ii) untested on three instances whose Toeplitz ranks depend on |c_k| only (§3.1 as corrected by the Opus reader), re-queued with the missing input named (a rung-1 instance with m ≥ 2 and c₁c₂ ≠ 0), no zoo line;
```


---

## §7 Row 7 — §4, Krein and H4; the prior art at the page (landed Fri Sep 25 22:23:03 IST 2026)

**Krein–Langer at the page.** IEOT 2014 (`fetched-r2/r-02a`): p. 1–2, the definition of P_a (kernel f(t − s), |s|, |t| < a, on (−2a, 2a)) and "M. G. Krein solved this problem completely in 1940, see [20]"; [20] = "Sur le problème du prolongement des fonctions hermitiennes positives et continues", C. R. (Doklady) 26, 17–22 (1940); §4.1 Bochner; **Theorem 4.4 on p. 24 (volume pagination; PDF page 24)** — every quoted sentence CONFIRMED. Math. Nachr. 1977 (`t-56a`): pages 189 and 190 rendered by the reader at 110 dpi and read as images — item 3 (the problem P_a(𝔓_κ), 𝔓_{κ;a}, the kernel H_f of (0.4) with exactly κ negative squares on [−a, a]) on p. 189; "Wie in [10] gezeigt wurde, ist diese Aufgabe stets lösbar", "Das Problem P_a(𝔓₀) wurde bekanntlich zuerst von M. G. Krein [11, 12] (siehe auch [13]) vollständig gelöst. In [14] verband er dieses Problem mit einer Saite." on p. 190 — CONFIRMED verbatim (p. 190 item 6 is the Hamburger problem P(H_κ), the literal source of the "truncated-Hamburger" vocabulary). JFA 1978 (`r-01b`): the text mentions neither ζ nor an explicit formula; the writer's "not printed there separately" is consistent with the reader's search.

**The change of variables (4.1)** — re-derived: with 2a = L, ∫∫F(t − s)φ(s)conj φ(t) ds dt = ∫F(x)ψ(x)dx, ψ(x) = ∫φ(s)conj φ(s + x)ds = (φ ⋆ φ̃)(−x), and for even F the sign of x is immaterial; supp φ ⊂ (−L/2, L/2) ⟹ supp φ ⋆ φ̃ ⊂ (−L, L). So "F positive-definite on (−L, L)" ⟺ "Weil positivity on tests g = φ ⋆ φ̃ with supp φ ⊂ (−L/2, L/2)" (Yoshida's t = (log 2)/2 is the φ-support; the g-support is (−log 2, log 2) — the writer's reading of Bombieri p. 184 is consistent) — CONFIRMED. **The distributional gap** is named correctly: Theorem 4.4 needs f continuous with f(0) = σ(ℝ) < ∞, F_π has a −½·fp(1/|u|) singularity (σ must be unbounded, as the class's elements are) and atoms; the Krein-type theorem for positive-definite distributions is recalled, not read. The sentence "Then Krein–Langer Theorem 4.4 + Bochner give … ⟺ the on-line, real-weighted relaxation of 𝒦_L(π) is nonempty" is stated for F generically but is only proved for continuous F — A7-2 says so in place. **Attribution:** "truncated-Hamburger existence set" is PRICING §5 line 143's phrase (it glosses C2's M1 items, line 43); C2 line 43 itself does not contain it (the brief carried the same slip) — A7-1.

**Bombieri 2000 at the page** (bdim PDF, hash verified): abstract ("prove again Yoshida's theorem that it is positive definite if t is sufficiently small"), p. 184 (Yoshida "verifies this positivity for t = (log 2)/2"), Theorem 1 p. 191, Theorem 2 p. 193 (the functional T[f] transcribed in (0.2) — CONFIRMED, and the reader's own (R) agrees with it), Theorems 3, 4, 8 at the stated places — CONFIRMED. **literature.md line 29 "(1/p, p)": LOCATED.** The OCR renders "1/p" as "1=p", which is why the writer's search missed it: p. 224, "An Example", two Dirichlet L-functions of one modulus and parity, p₀ the first prime with χ(p₀) ≠ χ′(p₀): "if we evaluate the Explicit Formula for a function f(x) with compact support in (1/p₀, p₀) … we obtain the relation Σ_ρ f̃(ρ) − Σ_ρ′ f̃(ρ′) = 0" — a LINEAR RELATION, not a negativity; and Connes–Consani 2021 p. 2: "provide a conceptual reason for Weil's negativity for functions f fulfilling the support condition Support(f) ⊂ (p⁻¹, p)". The record line conflates the two. Bombieri's example matters beyond the record line: it is a printed instance of **two distinct infinite zero configurations with identical band data on (−log p₀, log p₀) and the same archimedean functional** — the NO-type phenomenon of M5-U, for complex (non-positive, non-reflection-symmetric) data. The reader infers (`I infer`, not checked) that the same construction with two non-isomorphic number fields of equal degree, signature and discriminant and the same splitting below p₀ would give an exact positive-datum (Λ_K ≥ 0) ghost pair on a degree ≥ 3 rung — a candidate first rung for §7.3's second Untried line, outside ζ's own class (degree 1, conductor 1).

**Connes–Consani 2021** (`fetched/y-03`): Theorem 1 — CONFIRMED, but on p. 3, not p. 2 (A7-6); the sentence after (5), Corollary 2, Corollary 3.8 (u = 1.10246) and Remark 3.9 (1.15077; "not negative on [2⁻¹, 2]") — CONFIRMED. The reading "their band is |u| ≤ (log 2)/2 for g, i.e. F on (−log 2, log 2)" — CONFIRMED (support [2^{−1/2}, 2^{1/2}] for g, (1/2, 2) for f = g ⋆ g*).

**Lagarias–Rodgers 2020** (`fetched/w-09`): Conjecture 2.2 (p. 2), Theorem 2.4 (p. 3, the band-limited class K_n), §3's "Our purpose in this note…" (p. 4), Theorem 4.7 (the AH point process, p. 9) — CONFIRMED. **The consequence the writer draws is wrong as argued:** "Its configurations live on a translate of ½ℤ, whose transform is a lattice comb — by F1(c)/rider B such a configuration satisfies no first-order row". The process's configurations are SUBSETS of ω + ½ℤ (Theorem 4.7: "points in all configurations separated by integer multiples of 1/2"), whose transform is 4π-periodic, not a comb; they are not N-periodic, so rider B (a theorem about N-periodic configurations, PRICING §1.2(b)) does not apply; and they are unfolded (density 1), not configurations of RvM density. The data-class answer to the brief's question — T-averaged n-level CORRELATION data, not first-order band data at a height — is right and is what should stand (A7-3, A7-4, A7-7; rider 3, Z-5).

**A7-1** (FORMULATION.md) OLD:
```text
Hence C2 line 43's "truncated-Hamburger existence set"
```
NEW:
```text
Hence PRICING §5's "truncated-Hamburger existence set" (`results/c2-m5/PRICING.md` line 143, glossing C2's M1 items, C2 line 43 — attribution corrected by the Opus reader)
```

**A7-2** (FORMULATION.md) OLD:
```text
Then Krein–Langer Theorem 4.4 + Bochner give: F PD on (−L, L) ⟺
```
NEW:
```text
Then, for CONTINUOUS F (not F_π itself — see the next paragraph), Krein–Langer Theorem 4.4 + Bochner give: F PD on (−L, L) ⟺
```

**A7-3** (FORMULATION.md) OLD:
```text
Its configurations live on a translate of ½ℤ, whose transform is a lattice comb — by F1(c)/rider B such a configuration satisfies no first-order row, so I.3's world and the honest class are disjoint at the level of first-order data;
```
NEW:
```text
[CORRECTION, Opus reader, read-O.md §7] Its configurations are SUBSETS of a random translate of ½ℤ in unfolded coordinates (a stationary process of density 1, Theorem 4.7 p. 9): their transform is periodic (period 4π in the unfolded frequency), not a lattice comb, and they are not N-periodic, so rider B does not apply as stated; nor are they configurations of Riemann–von Mangoldt density. Whether an AH-type configuration at the true density (gaps at half-integer multiples of the LOCAL mean spacing) can belong to 𝒦_L(Λ) is not decided here — by the count of §2.3 it cannot be excluded at α < ½. What is at the page is the data-class statement: L–R match T-averaged n-level correlations, not first-order band data at a height;
```

**A7-4** (FORMULATION.md) OLD:
```text
so I.3's world is disjoint from the honest class at the level of first-order data.**
```
NEW:
```text
so I.3's DATA CLASS (T-averaged correlations) is not the honest class's (first-order band data at a height); disjointness of the configuration sets is NOT proved (Opus reader).**
```

**A7-5** (FORMULATION.md) OLD:
```text
the record line is unverified as to its source and is not used here.
```
NEW:
```text
the record line is unverified as to its source and is not used here. [LOCATED, Opus reader, read-O.md §7: the OCR renders "1/p" as "1=p"; Bombieri 2000 p. 224, "An Example", prints the support condition (1/p₀, p₀) for a LINEAR RELATION Σ_ρ f̃(ρ) − Σ_ρ′ f̃(ρ′) = 0 between two Dirichlet L-functions of the same modulus and parity (p₀ the first prime with χ(p₀) ≠ χ′(p₀)) — not a negativity; and Connes–Consani 2021 p. 2 prints "a conceptual reason for Weil's negativity for functions f fulfilling the support condition Support(f) ⊂ (p⁻¹, p)". The record line conflates the two; it is to be re-sourced, not struck. Bombieri's example is also the nearest printed neighbor of §5.1's M5-U: two distinct infinite zero configurations with identical explicit-formula data on (−log p₀, log p₀), for complex (non-positive) data.]
```

**A7-6** (FORMULATION.md) OLD:
```text
Theorem 1 (p. 2)
```
NEW:
```text
Theorem 1 (p. 3)
```

**A7-7** (FORMULATION.md) OLD:
```text
and satisfies no first-order row (F1(c));
```
NEW:
```text
and is not shown to satisfy or to violate a first-order row (its configurations are lattice subsets, not periodic — rider B does not apply as stated; §4.3 as corrected by the Opus reader);
```


---

## §8 Row 8 — §5, the contract theorem (landed Fri Sep 25 22:23:03 IST 2026)

M5-U and M5-D are well posed on the class as defined in §0.3; M5-U ⇒ M5-D where ζ's zeros in the window are simple — CONFIRMED. The YES shape (an uncertainty principle for positive integer-atomic measures of logarithmic density with a spectral gap, localized to a window) and the NO shape (an exact ghost) — CONFIRMED as shapes; the comb Σ_k(δ_{ks} − δ_{ks+s/2}) has transform (4π/s)Σ_{j odd}δ_{2πj/s}, so its gap is (−2π/s, 2π/s) — CONFIRMED by the reader's computation (Poisson summation: Σ_k e^{−iuks}(1 − e^{−ius/2}) is supported where us ∈ 2πℤ and vanishes at even j). §5.2's M2 reading: h_f(r) = (r − t)B̂(L(r − t)) is the separation note's (0.1) at line 16 — CONFIRMED; the two-simples-versus-double difference is ≤ 2ε², uniformly in L (A8-3 corrects "below the resolution ε ≲ 1/L", which misplaces the mechanism: it is h_f(t) = 0, not the bandwidth). The depth confinement "δ < 25/L" drops M2's second term and the (R*) height condition (C2 Instruments line 102, the M2 row) — A8-1. The nearest printed neighbor of M5-U is Bombieri p. 224 (§7 above) — A8-2; A8-4 carries row 5's restriction.

**A8-1** (FORMULATION.md) OLD:
```text
**the class's strip freedom at bandwidth L is confined to depths δ < 25/L, II.4's depth family**
```
NEW:
```text
**the class's strip freedom at bandwidth L is confined to the depths δ with L < L*(t, δ) = max(25/δ, 4δ⁻¹(log log(3 + t) + 2 log(1/δ) + log(17.4C₁))) (C2 Instruments line 102), or to heights where (R*) fails — a set containing, and larger than, δ < 25/L — II.4's depth family** [precision, Opus reader]
```

**A8-2** (FORMULATION.md) OLD:
```text
Inputs it would need, none on the record:
```
NEW:
```text
Nearest printed neighbor (Opus reader): Bombieri 2000 p. 224 — two Dirichlet L-functions of the same modulus and parity have identical explicit-formula data for tests supported in (1/p₀, p₀), so their zero sets differ by an integer-atomic measure with a spectral gap (−log p₀, log p₀): the NO-type phenomenon, printed, for complex (non-positive) data. Inputs it would need, none on the record:
```

**A8-3** (FORMULATION.md) OLD:
```text
the difference is O(ε²) and vanishes below the resolution ε ≲ 1/L of a bandwidth-L test (the uncertainty bound, one line: |B̂(η)| ≤ 1 and the ε² prefactor)
```
NEW:
```text
the difference is at most 2ε² uniformly in L (|B̂(η)| ≤ 1 and the ε² prefactor, which comes from h_f(t) = 0), so it vanishes as ε → 0 at every bandwidth, and for ε ≳ 1/L the factor B̂(Lε)² makes it smaller still [precision, Opus reader]
```

**A8-4** (FORMULATION.md) OLD:
```text
measures and gives G_X = ∞ on these supports (§2.2 P1–P2)
```
NEW:
```text
measures and gives G_X = ∞ on every closed set containing ζ's zeros (§2.2 P1–P2 as corrected)
```

---

## §9 Row 9 — §6, the zoo protocol and the three proposed riders (landed Fri Sep 25 22:23:57 IST 2026)

**Protocol items read against the zoo** (BARRIER-ZOO.md headings at lines 58 I.2, 66 I.3, 99 I.7, 107 I.8, 119 II.1, 149 II.4, 164 II.5, 176 III.1, 185 III.2, 340 III.20, 362 IV.1, 413 IV.7, 433 IV.9, 508 IV.18, 535 IV.17, 544 IV.19, 561 V.2, 579 V.4, 587 V.5): each item's cited content is where the note says; the I.2 evasion (FE with ζ's A fails in DMV worlds) and I.2 test (b) (F1 is axiom-free, hence infrastructure only) are right; IV.1's expression succeeding with multiplier 1 and the withdrawal of "the phases are the new coordinate" as a data claim are right and are strengthened by the exact band-limited-taper form of row 1. Two corrections carry over: item 2's I.3 clause (A7-7) and the rider-B application. **Record defect found in passing, for the orchestrator (not an amendment to this note):** zoo III.2's STATEMENT (line 187) carries the same attribution as literature.md line 29 — "genuine negativity appears once support reaches (1/p, p) (Bombieri, Lincei 2000 …)"; at the page the negativity sentence is Connes–Consani 2021 p. 2 and Bombieri's (1/p₀, p₀) is the p. 224 linear-relation example (row 7). A dated correction line on III.2 is owed at the next zoo stream.

**Does any existing entry already state the riders?** grep over BARRIER-ZOO.md for "finite configuration", "windowed", "finite exponential", "entire", "Lagarias", "Rodgers", "uncertainty principle", "Poltoratski", "spectral gap": no entry states F1's (a)–(b) (the only first-order-host statement is rider B / the II.1 pointer, about PERIODIC configurations); Lagarias–Rodgers appears only as a V.2 casualty (line 563); nothing on spectral gaps or uncertainty principles. **All three riders are new statements to the zoo.** Format: the house BLOCK shape ("- **[RIDER <date>, Session N — source; label.]** **bold statement.** …; executable test; logged numbers") is followed, anchors named (FORMULATION.md sections, the three scripts and logs). Two insertion notes for the orchestrator: IV.7's riders sit as indented sub-bullets (" - **[RIDER B …"), and the house dates are ISO ("2026-09-10", "2026-09-24 18:27 IST"), whereas the proposals carry the `date` string — convert on insertion.

**Rider 1 (IV.7, Theorem F1)** — CLOSES: its (a)–(c) are exactly F1 as re-derived (rows 2–3); its "for NO datum π and NO L > 0" is right (the F1(a) threshold precision concerns ε, not L); the executable test is sound; the logged numbers need only the "best-found" word (Z-1). **Rider 2 (II.1)** — FIX-FIRST: its (0.5) sentence must become the exact band-limited-taper statement (Z-2), its Poltoratski clause the ζ-zero-set statement (Z-3), and "on which nothing is printed" is false as a statement about neighbors (Z-4). **Rider 3 (I.3 pointer)** — FIX-FIRST: the rider-B argument is wrong (Z-5); the data-class distinction, read at the page, stands.

**Z-1** (zoo-entries-proposed.md) OLD:
```text
best relative residual
```
NEW:
```text
best-found relative residual (upper bounds on the infimum; below the count optimizer-limited — the Opus reader's fits reach 1.5·10⁻¹² and 2.1·10⁻¹² at L = 0.5 and 1)
```

**Z-2** (zoo-entries-proposed.md) OLD:
```text
the windowed transform on [T, T + W] is ĉ_{T,W} = (F_π·1_{(−L,L)}) ∗ ŵ_W + R_{T,W}, R the out-of-band leakage (the configuration's transform outside (−L, L) seen through the window kernel's tails): at L ≥ ℓ = log(T/2π) every two-moment row of this ceiling's template — |c_k|² at |u_k| ≤ ℓ, the Frobenius row m₂(1) = 4/3 included — is a functional of F_π plus R, so the class at α = L/ℓ ≥ 1 sits inside this ceiling's constraint set up to leakage and the two-moment LP is its relaxation; the modulus AND the phase of the band transform are the datum's, so "the phases" are not a coordinate of the configuration, and the class's only freedom is R.
```
NEW:
```text
every transform of the configuration windowed at height T by a band-limited taper w (ŵ ∈ C_c^∞(−ε, ε), w_T(τ) = w(τ − T)) is, at |u| ≤ L − ε, EXACTLY (2π)⁻¹F_π ∗ ŵ_T — on- and off-line points alike: at L ≥ ℓ + ε, ℓ = log(T/2π), every soft-windowed two-moment row of this ceiling's template — |c_k|² at |u_k| ≤ ℓ, the Frobenius row m₂(1) = 4/3 included — is a functional of F_π alone, so the class at α > 1 satisfies the soft-windowed form of this ceiling's rows with the datum's values and the two-moment LP is its relaxation; the modulus AND the phase of every such transform are the datum's, so "the phases" are not a coordinate of the configuration; the class's freedom is visible only to hard-window rows and to rows at |u| ≥ L − ε.
```

**Z-3** (zoo-entries-proposed.md) OLD:
```text
C_X = ∞ for supports of RvM density.
```
NEW:
```text
C_X = ∞ on every closed set containing ζ's zeros (their maximal gap tends to 0, Bombieri 2000 p. 225).
```

**Z-4** (zoo-entries-proposed.md) OLD:
```text
on which nothing is printed.
```
NEW:
```text
whose nearest printed neighbors are Bombieri 2000 p. 224 (two Dirichlet L-functions of the same modulus and parity: their zero sets have identical explicit-formula data for tests supported in (1/p₀, p₀) — a spectral-gap difference of two infinite zero configurations, for complex, non-positive data) and p. 225 (Bourgain: linear relations over intervals of arbitrary length, from gaps → 0); for positive integer-atomic measures nothing is printed in the sources opened.
```

**Z-5** (zoo-entries-proposed.md) OLD:
```text
A configuration on a translate of ½ℤ has a lattice comb as its transform and by IV.7 rider B (and its extension above) satisfies no first-order equality row: this world and the honest first-order class are disjoint at the level of first-order data.
```
NEW:
```text
Its configurations are subsets of a random translate of ½ℤ in unfolded coordinates (stationary, density 1; their Theorem 4.7, p. 9): they are neither N-periodic (so IV.7 rider B does not apply to them as stated) nor of Riemann–von Mangoldt density, and whether an AH-type configuration at the true density can satisfy first-order equality rows at bandwidth L is not decided (by count it cannot be excluded at α < ½). The pointer records the data-class distinction only.
```


---

## §10 Row 10 — §7, the DECISION (landed Fri Sep 25 22:23:57 IST 2026)

**Is NO-GO for an implementation slot the right reading? Yes — CLOSES.** The load-bearing fact is F1 alone (rows 2–3, re-derived by a different route): a program with finitely many position/mark variables hosting explicit-formula EQUALITY rows with a free datum is infeasible (finite configurations, F1(a)) or has the single feasible point ν₀ (finite modifications, F1(b)) or is degenerate (periodic, rider B); so the digest's stop line (iii) — "the bilinear program's optimum is not certifiable (no dual certificate)" — cannot even be posed, and the D1(b) route as priced ("formulation → bilinear program → Opus audit") has no second slot to fund. Neither the gap finding (row 5) nor the count (row 4) is needed for the NO-GO; they price what remains (M5-U as a theorem question). Three checks on the text: (1) "the one finite decidable instance is rung 1 … run in this slot" — correct (row 6), with the relaxation clause amended; (2) the GO paragraph states the unavailable object honestly; (3) the Poltoratski clause of the NO-GO sentence must be restricted as in row 5 (A10-1), and §7.1's H2 row must label the stratification "by count" (A10-2). The reader's one addition to the price: an exact-ghost construction for the NO is not hopeless in principle — Bombieri p. 224's L-function pairs show exact spectral-gap differences of infinite zero sets exist for non-positive data (row 7) — which supports keeping §7.3's second Untried line, now with a named first rung outside ζ's class. Grade of the DECISION as written in §7.2 ("theorem (F1, elementary, single-check)") becomes "theorem (F1, elementary, dual-model check 2026-09-25)".

**A10-1** (FORMULATION.md) OLD:
```text
(Poltoratski's density is infinite on Riemann–von Mangoldt supports; his theorem concerns finite complex measures)
```
NEW:
```text
(Poltoratski's density is infinite on every closed set containing ζ's zeros; his theorem concerns finite complex measures)
```

**A10-2** (FORMULATION.md) OLD:
```text
on RvM-density supports C_X = ∞ (Theorem 2 ⇒ G_X = ∞): no pinning at any α; the regimes are a height stratification at fixed L (free above 2πe^{2L});
```
NEW:
```text
on every closed set containing ζ's zeros C_X = ∞ (maximal gap → 0, Bombieri 2000 p. 225; Theorem 2 ⇒ G_X = ∞): no pinning at any α; the regimes are a height stratification at fixed L BY COUNT (free by count above 2πe^{2L});
```

**A10-3** (FORMULATION.md) OLD:
```text
the record sentence "genuine negativity once support reaches (1/p, p)" (`results/literature.md` line 29) → (iii) unexplained: one re-read of Bombieri 2000 for that claim is owed before it may be kept or struck.
```
NEW:
```text
the record sentence "genuine negativity once support reaches (1/p, p)" (`results/literature.md` line 29) → LOCATED by the Opus reader (read-O.md §7): Connes–Consani 2021 p. 2 (the negativity) and Bombieri 2000 p. 224 (the (1/p₀, p₀) linear-relation example); the line conflates them and is to be re-sourced, not struck.
```


---

## §11 Row 11 — the Untried lines (§7.3) and Instruments rows (§7.4, §2.3) (landed Fri Sep 25 22:23:57 IST 2026)

**Units and format.** Opened C2's Instruments table (line 94 on: four columns Quantity | Current best value | Result file | Dated) and Untried (line 135 on: "- **title (entered <date>, Session, from <file> — reason).** S1–S5 fit: … First rung: … Leaves only into …"). Both proposed Instruments rows have the four columns in the table's order; both are dated; row 1 records a qualitative regime rather than a number — admissible (the table "records, never ranks"), but its value column must carry row 5's restriction (A11-1 in §2.3's copy, A11-2 in §7.4's copy). Row 2 records numbers and must call them best-found upper bounds (A11-3). The three Untried lines follow the house shape (title with entry stamp and source, S1–S5 fit, first rung, exit). **Restatement check:** the existing Instruments rows (lines 97–133) concern the cone layer, M2's constants, R₀, (R*), the sign channel, Lean labels and residues — none records the honest class or a window-residual measurement; the existing Untried lines (137 general α for M2; 138 the Siegel-zero world) — none overlaps. No proposed line restates an existing one. Amendments: the Poltoratski clause in Untried 1 (A11-4, and its twin in §5.1, A8-4) and the integer-marks precision in Untried 2 (A11-5). Reader's note for Untried 2 (not an amendment): a positive-datum exact ghost pair is plausibly available on a degree ≥ 3 Dedekind rung (row 7, `I infer`), which would make "the NO has an exact form somewhere on the ladder" a ½-slot literature-plus-compute check.

**A11-1** (FORMULATION.md) OLD:
```text
C_X = ∞ for RvM-density supports (finite complex measures with arbitrarily long gaps exist on them)
```
NEW:
```text
C_X = ∞ on every closed set containing ζ's zeros (maximal gap → 0, Bombieri 2000 p. 225; finite complex measures with arbitrarily long gaps exist on them)
```

**A11-2** (FORMULATION.md) OLD:
```text
C_X = ∞ for RvM-density supports; no theorem
```
NEW:
```text
C_X = ∞ on every closed set containing ζ's zeros (maximal gap → 0, Bombieri 2000 p. 225); no theorem
```

**A11-3** (FORMULATION.md) OLD:
```text
| Band-data residual floor of a marks-{1, 2}
```
NEW:
```text
| Band-data best-found residual (an upper bound on the infimum; below the count optimizer-limited — the Opus reader's fits reach 1.5·10⁻¹² / 2.1·10⁻¹² at L = 0.5 / 1, `verify-O/window_residual_O_run.log`) of a marks-{1, 2}
```

**A11-4** (FORMULATION.md) OLD:
```text
G_X = 2πC_X) gives G_X = ∞ on these supports
```
NEW:
```text
G_X = 2πC_X) gives G_X = ∞ on every closed set containing ζ's zeros
```

**A11-5** (FORMULATION.md) OLD:
```text
(a second on-circle configuration with the same s₁…s_m exists whenever rank T_m = m + 1;
```
NEW:
```text
(a second on-circle representing measure with the same s₁…s_m exists whenever rank T_m = m + 1 — with real weights; with integer marks and mass 2g it must be exhibited, e.g. g = 2, m = 1: (1 − b₁t + 7t²)(1 − b₂t + 7t²) with b₁ + b₂ = −3, |b_i| ≤ 2√7;
```


---

## §12 Row 12 — the `[novelty: single-check]` labels (standing order 7) (landed Fri Sep 25 22:23:57 IST 2026)

| Where | Claim | Reader's check | Outcome |
|---|---|---|---|
| §1.3 (Corollary F1-C; rider 1's packaging) | no finite, windowed or periodic host for explicit-formula equality rows; the consequence for PRICING §1.1(v)'s bilinear program | F1 re-derived by a different route (rows 2–3); zoo grep: no entry states it; sources opened state nothing about finite hosts (Bombieri p. 224–225 concern INFINITE zero sets, the opposite side) | **`[novelty: dual-model check 2026-09-25]`** for the packaging and its consequence (the mathematics remains, as the writer says, elementary and not claimed new) |
| §4.3 (the Krein-continuation reading (4.1) ⟺ "a positive on-line measure with the datum's band transform exists") | no printed source opened states it | checked the three Krein–Langer PDFs (no ζ, no explicit formula in r-01b / r-02a text), Bombieri 2000 (no "Krein"), Connes–Consani 2021 (no "Krein", no "Bochner") — consistent with the writer | **stays `[novelty: single-check]`, open**: the nearest neighbors the writer names (Yoshida 1992; Suzuki's screw-function papers; Krein–Langer screw functions) are not on disk; the reading is a two-line consequence of Bochner + Krein and its novelty is not worth asserting until Yoshida 1992 and Suzuki are opened (a Round-9 fetch row) |
| §4.3 ("the printed prior art on the band-limited Weil criterion sits exactly at the first prime") | Yoshida via Bombieri, and Connes–Consani, both on (−log 2, log 2) | every quotation re-read at the page; CC's Corollary 3.8 / Remark 3.9 bands (u = 1.10246 → 1.15077, not negative on [2⁻¹, 2]) confirm | **`[novelty: dual-model check 2026-09-25]`** for the placement (a prior-art statement, not a novelty claim) |
| rider 1 | = §1.3 | as above | **`[novelty: dual-model check 2026-09-25]`**, with Z-1 |
| rider 2 | the honest class relative to II.1; M5 as an uncertainty principle "on which nothing is printed" | the (0.5) claim corrected (exact with band-limited tapers); the "nothing is printed" clause is FALSE as to neighbors (Bombieri p. 224–225) | **stays `[novelty: single-check]`** until Z-2–Z-4 are applied; after them the statement "for POSITIVE integer-atomic measures nothing is printed in the sources opened" is dual-checked as far as the opened sources go (V.5: absence is not evidence) |
| rider 3 | the AH data class | the data-class reading is `[printed]` (Lagarias–Rodgers pp. 3, 4, 9, read by both models); the disjointness argument is wrong | **`[printed: Lagarias–Rodgers 2020, Theorem 2.4 p. 3, §3 p. 4, Theorem 4.7 p. 9]`** for the data class, after Z-5; no novelty claim remains |
---

## §13 Summary for the orchestrator, honesty note, lint (landed Fri Sep 25 22:24:18 IST 2026)

**Verdicts.** DECISION (NO-GO for an implementation slot): **CLOSES.** Sections: §0 FIX-FIRST (A1-1, A1-2); F1(a) CLOSES with one precision (A2-1); F1(b)/(b′)/(c) CLOSES; §1.4 FIX-FIRST in wording (A4-1–A4-4); §2 FIX-FIRST (A5-1–A5-5); §3 FIX-FIRST in one clause (A6-1–A6-4); §4 FIX-FIRST in attributions and one argument (A7-1–A7-7); §5 FIX-FIRST in one clause (A8-1–A8-4); §6/riders FIX-FIRST for riders 2–3 (Z-1–Z-5), rider 1 CLOSES; §7 texts FIX-FIRST in wording (A10-1–A10-3, A11-1–A11-5). No FATAL. **40 amendments: 35 to FORMULATION.md, 5 to zoo-entries-proposed.md**; every OLD string was checked by script to occur exactly once in its file, and the whole set applies sequentially without collision (insertion-style: each NEW keeps the OLD's content or marks what it replaces). None of them touches the NO-GO.

**The three substantive corrections, in one line each.** (1) Eq. (0.5) is exact only with a band-limited taper — and then the leakage R vanishes identically, which strengthens the writer's reading. (2) P1's "C_X = ∞ for every element of the class" rests on "mean gap → 0", which does not give separated subsequences; the conclusion holds for every closed set containing ζ's zeros because their maximal gap tends to 0 (printed: Bombieri 2000 p. 225) — the refutation of H2(i) stands. (3) The AH "disjoint by rider B" argument is wrong (lattice subsets are not periodic); the data-class reading stands. Two record findings: literature.md line 29 / zoo III.2 line 187 misattribute Connes–Consani's negativity sentence to Bombieri, whose (1/p₀, p₀) is a linear-relation example (p. 224) — and that example is the nearest printed neighbor of M5-U.

**Honesty note.** Read at the page this session by the reader: Poltoratski arXiv:0908.2079v2 (§2 (2.1), §5 pp. 8–10 incl. Remarks 2–6, Examples 1–2, Theorem 2, §7 Lemmas 1–2); Bombieri 2000 (abstract; pp. 184, 186, 191, 193; pp. 224–225 "An Example" and the Bourgain remark); Krein–Langer IEOT 2014 (pp. 1–2, §4.1, Theorem 4.4 p. 24, ref. [20]); Krein–Langer Math. Nachr. 1977 pp. 189–190 (rendered by the reader and read as images); Krein–Langer JFA 1978 (text searched); Connes–Consani 2021 (pp. 2–3, 17, 21–22); Lagarias–Rodgers 2020 (pp. 2–4, 7, 9, 12); C2 lines 14, 16, 43, 62, 80, 94–138; PRICING §1–§2, §5 (lines 1–50, 83–97, 139–150); digest lines 173–187, 308–327; zoo I.2, I.3, II.1 (with its pointer and READ block), III.2, IV.7 (riders, READ block), and the headings of every entry the protocol names; the M2 note's (0.1) (line 16). Computed by the reader: three scripts under `verify-O/` (logs named in the header). Recalled, never load-bearing: nothing new beyond the writer's list; the reader's Dedekind-pair ghost is `I infer`. Not done: Yoshida 1992, Suzuki, Koosis/Havin–Jöricke, Landau–Pollak–Slepian not fetched (as for the writer); no Lean; no commit; no edit outside `results/c2-m5b/read-O.md`, `results/c2-m5b/verify-O/` and the SHARED block.

**Lint.** A case-insensitive grep of this file for the four phrases KICKSTART 10(g) forbids: 0 hits (run before hashing; the phrases are not reproduced here). U.S. English. Machine-clock stamps only.

Closed Fri Sep 25 22:24:18 IST 2026.
