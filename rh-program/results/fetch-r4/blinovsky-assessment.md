# Assessment — V. Blinovsky, "Proof of Riemann hypothesis", arXiv:1703.03827v16 [math.GM], 10 Aug 2026 (12 pp.)

**Session 18, 2026-09-09. Read in full by vision (all 12 pages) at the sponsor's request. Verdict: NOT a proof. The argument's decisive term is produced by a differentiation error; corrected, the term the paper relies on vanishes and nothing in the paper decides the sign that is left.** Not requested by the program; recorded here so nobody re-reads it. No program verdict is affected.

## What the paper does (structure is coherent up to p. 4)

1. Uses the Dirichlet-eta integral ζ(z) = (1−2^{1−z})^{−1} Γ(z)^{−1} ∫₀^∞ x^{z−1}/(eˣ+1) dx (valid for Re z > 0) and sets K(σ,T) = |∫₀^∞ x^{z−1}/(eˣ+1) dx|², which has the same zeros as ζ in the open strip. Correct.
2. Uses Platt–Trudgian (RH verified to T = 3·10¹²) and an explicit zero-free region σ > 1 − 1/(6 ln T) (ref. [3], a 2023 Res. Number Theory paper) to restrict to T > 3·10¹² and σ ∈ D = [1/(6 ln T), 1 − 1/(6 ln T)]. Correct as used.
3. **Key claim (4):** ∂²_σ K(σ,T) ≥ 0 on D for every T > 3·10¹². Since K ≥ 0 and the zeros at height T come in pairs σ, 1−σ, convexity in σ forces at most one zero per horizontal line, hence σ = ½. The logic is valid. **But (4) is at least as strong as RH itself** (an off-line zero pair σ₀, 1−σ₀ with K ≥ 0 between them would already break convexity), so everything rests on the proof of (4).
4. pp. 2–3: two changes of variable and cos x = 2cos²(x/2) − 1 turn (4) into an inequality (5) of the form ∫₀¹ f(h,T) cos²(πh/2) dh ≥ ½∫₀¹ f(h,T) dh, where f(h,T) = Σ_{i≥0} [G(2i+h) + G(2i+2−h)] folds the x-integral onto h ∈ [0,1]. I checked the substitutions; they are right (the x-range after the second substitution is all of ℝ, folded by the x → −x symmetry).
5. p. 3–4: by Chebyshev's integral inequality (the paper calls it FKG), (5) follows IF f(·,T) is non-increasing on [0,1]. Correct — but only a SUFFICIENT condition, with no reason offered why it should hold.
6. pp. 4–12: Euler–Maclaurin applied to ∂_h f, an expansion of the y-integral in powers of π/T, and crude absolute-value bounds, ending in (17): Φ ≤ −(1−h)·10^{−9}(π/T)² < 0.

## Where it fails

**A. The leading term of (13) is an artifact of a factor-of-2 error (fatal).** In (12) the paper differentiates δ(πh/(2T)) with respect to h, where δ(u) = c Σ_k a_{2k} u^{2k}/(2k)!. The correct derivative carries the factor π/(2T), i.e. (π/T)^{2k}·k·(h/2)^{2k−1}; the paper's (13), second line, writes (π/T)^{2k}·2k·(h/2)^{2k−1} (twice too large), and the second-derivative term is written with 1/3 where (1/12)·4·¼ = 1/12 is right (four times too large). With the correct factors the k = 1 (order (π/T)²) contributions are a₂/2!·[(1−h) − (1−h) + 0] = **0**: the order-(π/T)² term cancels identically. I re-derived this independently: with F(h) = Σ_i Φ(εi + εh/2), Euler–Maclaurin gives F′(h) = −½Φ(δ) + (ε/4)Φ′(δ) − (ε²/24)Φ″(δ) + …, and in f′(h) = F′(h) − F′(2−h) the two O(ε²) pieces −¼|Φ″(0)|ε²(1−h) and +¼|Φ″(0)|ε²(1−h) cancel exactly. The paper's own printed formula for b_{2k}(h) (p. 8, below (13)) ALSO gives b₂(h) = a₂[(h/2) + (1−h/2) − 1] = 0, contradicting the sentence that follows it, "From above equation it follows that b₂(h) = −a₂". The entire final bound (17) is the term −(1−h)½a₂(π/T)² with a₂ > 4·10^{−9}; that term does not exist.

**B. What is left cannot be signed by the paper's method.** After the cancellation the sign of f′ is decided by the k ≥ 2 terms and the B₃-remainder, which the paper only bounds in ABSOLUTE value (|b_{2k}|/(2k)! ≤ 2^{16k}ση(2σ), (14); |Δ₄(T)| ≤ 6·10^{−6}π⁴(1−h)/T³, (16)). Absolute bounds cannot establish a sign for a quantity whose leading term is zero.

**C. Further errors, each independently damaging.**
- Eq. (11), p. 5: ∫₀^∞ y^{2σ−1}(ln y)² e^{−cy} dy is written as ¼(Γ(2σ))″_σ · c^{−2σ}; the σ-derivative must also act on c^{−2σ} (terms in ln c and (ln c)² are dropped). All later coefficients a_{2k} inherit this.
- The double series Σ_{m,n≥1} (−1)^{m+n}(me^x + ne^{−x})^{−2σ} (p. 5) is only conditionally convergent for σ ≤ 1; it is differentiated term-by-term in x at x = 0 to any order and re-summed over set partitions with no justification.
- p. 6: "|B_{2(q−1)}| < |B_{2q}|, q > 1" is false for q = 2, 3 (|B₂| = 1/6 > |B₄| = 1/30 > |B₆| = 1/42).
- Numerous "≤ universal constant" steps (p. 8: Γ(2σ) ≤ 1/δ, inf|ψ| < 1/δ + 2; p. 11: Σ Γ(2σ+i)(ψ² + ψ′) ≤ 45·10³σ) are asserted without proof and some are wrong at the endpoints of D.
- Presentation: v16 of a 2017 preprint in math.GM (general mathematics, the arXiv category for unrefereed claims of this kind); references include two Wikipedia URLs; "Then" / "We have" chains with no lemma structure.

## Bottom line for the sponsor
The paper has one good idea in it — reduce RH above 3·10¹² to convexity of |Γ(z)ζ(z)(1−2^{1−z})|² in σ, then to monotonicity of a folded integral via Chebyshev's inequality — but that reduction only replaces RH by a statement at least as strong, and the attempt to prove the strong statement rests on a term that a correct differentiation makes vanish. It does not make sense as a proof and nothing in it is usable by the program. Filed under `fetched-r4/not-on-list/`, not routed.
