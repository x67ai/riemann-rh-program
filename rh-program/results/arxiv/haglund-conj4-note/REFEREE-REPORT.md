# Referee report (second model) — "On Haglund's Conjecture 4 for the Riemann Xi approximants"

VERDICT: PENDING (to be set at the end of the review)

## Plan (at most 20 lines)
1. Read REFEREE-BRIEF.md to the end; then WRITER-NOTES.md, main.tex (and pdftotext of main.pdf), the working note haglund-conj4/NOTE.md, and the two census units' files.
2. Section A — statements and proofs: for each numbered statement, compare with NOTE.md; re-derive every proof step by step as printed; log each try as ATTEMPT k (or "ATTEMPT k — breaks at: ...").
3. Section B — census: every number in the census section against the census units' files and NOTE.md; recompute cheap ones (mpmath / python-flint).
4. Section C — every quotation and citation checked at the page (source PDFs / pages available on disk or fetched).
5. Section D — labels and tone: nothing in print presented as new; no sentence on whether anything bears on RH; no internal paths, session labels or process narration.
6. Section E — the writer's recorded wording choices in WRITER-NOTES.md, each accepted or contested.
7. Findings: FIX-FIRST list with OLD/NEW pairs; minor list with OLD/NEW pairs.
8. What could not be checked.
Deliverable built incrementally; a dated block appended to haglund-conj4/SHARED.md after each batch.

## Reading as an outside reader (18:16 IST 2026-10-03, pdftotext of main.pdf, 9 pp.)
The note reads cleanly: conjecture quoted, two statements (D)/(R) defined, each result labeled by kind (proved / proved under a hypothesis / numerical / heuristic). Points that stopped me on a first read, each examined below: the abstract's "frozen at a constant" (no "that decreases"); Lemma 2.3's equivalence "(D) is the statement that ..."; the Table-1 reading sentence "1122 branches in the rows other than k = 9 and k = 50"; the far-field "to three digits".

## Section A — statements and proofs (main.tex §§2–4, Lemma 6.1) against NOTE.md §§1–5

ATTEMPT 1 — Lemma 2.1 (main.tex l. 151–163; NOTE Lemma 1.1). Statement identical.
- Step 1: integration by parts, boundary terms vanish (phi_n(v) sin(xv) -> 0 super-exponentially; sin 0 = 0): ∫phi cos(xv) = x^{-1}∫(-phi') sin(xv). Checked.
- Step 2: -phi' > 0 and strictly decreasing: strict convexity makes phi' strictly increasing, and phi'(v) -> 0, so phi' < 0 everywhere. Checked (the text cites the kernel facts of §1.1, fine).
- Step 3: alternating half-period pieces, decreasing sizes, first positive: sum > 0 for x > 0. For x < 0 the first piece is negative and x^{-1} < 0; the product is still positive (or use evenness). Printed "For x ≠ 0 ... the first positive" is literally true only for x > 0. Cosmetic (minor m1).
- Verdict: proof complete.

ATTEMPT 2 — Lemma 2.2 (l. 165–178; NOTE Lemma 1.2). Statement identical.
- F_t = Ξ - Q_k + tPhi_{k+1} = Ξ - Phi_{k+1} - Q_{k+1} + tPhi_{k+1} = Ξ - (uPhi_{k+1} + Q_{k+1}). Checked.
- L_t = 2∫kappa_t cos(zv): termwise interchange is legitimate (sum of phi_n(v)cosh(|Im z|v) converges in L^1, double-exponential decay); not said, standard, as in the NOTE.
- kappa_t positive, strictly decreasing, strictly convex for 0 ≤ u ≤ 1 (also u = 0: the tail sum alone); the derivative series converge uniformly on [0, ∞). Checked.
- "the argument of Lemma 2.1 applies to kappa_t" (W5's added clause) is exactly what the step needs. Checked.
- Verdict: proof complete.

ATTEMPT 3 — Lemma 2.3 (l. 180–194; NOTE Lemma 1.3). Statement identical (NOTE's bracket became "together with ...").
- F_t = Ξ_{k+1} - uPhi_{k+1}: checked. F_t = 0 <=> S_k = u off the zeros of Phi_{k+1}: checked.
- At a zero, ∂_zF_t = Phi_{k+1}S_k' (since S_k = u), so a simple zero with Phi_{k+1} ≠ 0 has S_k' ≠ 0; dz/dt = -Phi_{k+1}/∂_zF_t = -1/S_k'. Checked.
- Im(-1/w) = Im(-w̄)/|w|^2 = Im w/|w|^2. Checked.
- "(D) for k is the statement Im S_k' ≤ 0 at every z, Im z > 0, S_k(z) ∈ (0,1), together with the behavior at multiple zeros": every such z is a zero of F_t at t = 1 - S_k(z) ∈ (0,1); simple ones carry the sign condition; endpoints t = 0, 1 do not affect monotonicity. Checked, with the hedge as printed.
- Verdict: proof complete.

ATTEMPT 4 — Theorem 2.4 (l. 196–262; NOTE Theorem 2.1). Statement: the corrected form — (e) reads "every critical point of x -> S_k(x) with value in (0,1] is a non-degenerate local maximum (S_k'' < 0)", and the three weaker conditions are "necessary", "sufficient when no ... multiplicity at least 3". (d)'s first sentence is merged with the NOTE's parenthesis (the NOTE's "odd number of real zeros near x_0 ... counted with multiplicity" is dropped; it is implied by "exactly one of them real"). No hypothesis dropped.
- (a) from Lemma 2.2: checked.
- (b) step 1: Ξ ≤ 0 => F_t = Ξ - L_t < 0; so F_t(γ_j) < 0. Checked.
- (b) step 2: F_t - Ξ_1 = Σ_{2≤n≤k}Phi_n + tPhi_{k+1} ≥ 0 on R (Lemma 2.1). Checked.
- (b) step 3: Ξ_1(0) = Ξ(0) - Q_1(0) ≥ 0.4971 - c_1 > 0. Recomputed (mpmath, 30 digits): Ξ(0) = 0.4971207782; Q_1(0) = Σ_{n≥2}Phi_n(0) = 1.71740e-4 (Phi_n(0) = 2X^{-1/4}[2Γ(9/4,X) - 3Γ(5/4,X)]); c_1 = 1.71806e-4; so Q_1(0) ≤ c_1 and Ξ(0) - c_1 = 0.49695 > 0. Checked (citation to be verified in Section C).
- (b) step 4: two integrations by parts: L_t(x) = -(2/x^2)kappa'(0) - (2/x^2)∫kappa'' cos(xv), Riemann–Lebesgue => x^2 L_t -> -2kappa_t'(0) > 0; x^2 Ξ(x) -> 0. So x^2F_t -> 2kappa_t'(0) < 0. Checked.
- (b) step 5: zeros in [0, ∞) bounded, finitely many (F_t analytic, ≢ 0). Parity: F_t < 0 at both ends of a positive lobe (even), F_t(0) > 0 > F_t(γ_1) (odd); no zeros in negative lobes. Checked. (Real zeros cannot escape: F_t(γ_j) < 0 traps them in their lobe — useful for (e), not stated, not needed for (b).)
- (c): checked (P_t open, boundary point has F_s = 0 < F_t).
- (d): F_t = F_{t0} + (t - t0)Phi_{k+1}; c real (F real on R); Weierstrass gives m zeros; Puiseux leading term (-(t - t0)Phi(x0)/c)^{1/m}. Odd m: exactly one real m-th root; the zero near the real direction is its own conjugate's only candidate, hence real; others non-real. Even m ≥ 4: two real roots iff -(t - t0)Phi(x0)/c > 0 iff F_t(x0) = (t - t0)Phi(x0) has sign opposite to c. m = 2, c < 0: two real zeros iff t > t0 (landing); c > 0: iff t < t0 (lift-off). All checked.
- (e): simple real zeros move on R (IFT, F real); a multiple real zero at t0 < 1 keeps (R) iff m = 2 and c < 0 (odd m ≥ 3 loses m - 1 real zeros; even m ≥ 4 loses ≥ m - 2 ≥ 2; m = 2, c > 0 is a lift-off). On R, F_t = Phi_{k+1}(S_k - u) with Phi_{k+1} > 0, so the multiplicity of the zero equals that of S_k - u, and t ∈ [0,1) <=> u ∈ (0,1]. Hence the S_k form. Weaker conditions: "even multiplicity, locally ≥ 0" <=> local minimum of S_k with value u ∈ (0,1] (S_k analytic, non-constant: extrema are strict, of even order) <=> a merge of two components of {S_k > u} as u decreases through that value (value 1 included: merge just after t = 0; value 0 excluded). Necessary: such a zero loses its real zeros after t0 (m = 2: lift-off; even m ≥ 4, c > 0: m non-real after t0). Sufficient without m ≥ 3: then every multiple zero is double, and a double zero not of lift-off type is a landing. Checked.
- Verdict: proof complete; the corrected form is printed.

ATTEMPT 5 — Proposition 2.5 (l. 265–293; NOTE Proposition 2.3). Statement identical; label "conditional on the zeros of Ξ being real" matches the NOTE's.
- Step 1: lift-off = m = 2, c > 0: F = F' = 0, F'' > 0 at x0, so Ξ = L > 0, Ξ' = L', Ξ'' ≥ L''. Checked.
- Step 2: (log Ξ)'' = Ξ''/Ξ - (Ξ'/Ξ)^2 ≥ L''/L - (L'/L)^2 = (log L)''. Checked.
- Step 3: Hadamard for the even order-1 function with only real zeros: Ξ(z) = Ξ(0)∏(1 - z^2/γ^2) (the factors e^{±z/γ} cancel in pairs; evenness kills e^{Az}; Ξ(0) ≠ 0). (log Ξ)'' = -Σ[(x - γ)^{-2} + (x + γ)^{-2}]. Checked.
- Following paragraph: "(R) follows from the strict inequality ... at the real points where Ξ = L_t": correct, and also covers zeros of multiplicity ≥ 3 (there Ξ'' = L'', so equality holds, which the strict inequality excludes); the text does not say this, nor does the NOTE — acceptable as printed (the claim is true).
- "at least 2Σγ^{-2} = 0.0462... in the central lobe": f(x) = Σ[(x-γ)^{-2} + (x+γ)^{-2}] is increasing on (0, γ_1) (f' = 2Σ[|x-γ|^{-3} - (x+γ)^{-3}] > 0), so its minimum is f(0) = 2Σγ^{-2} = 0.046210 (Σ_{γ>0}γ^{-2} = 0.0231050 under the hypothesis). Checked.
- "at least 8(γ_{j+1} - γ_j)^{-2} in the lobe (two endpoint terms, smallest at the midpoint)": checked.
- "heuristically ... about 1/(2π^2(k+1)^4)": labeled heuristic; second moment of a kernel of width 1/(2X) in v, X = π(k+1)^2: <v^2> ≈ 1/(2X^2). Consistent.
- Verdict: proof complete.

ATTEMPT 6 — Lemma 3.1 (l. 305–320; NOTE Lemma 3.1). Statement identical; label "Titchmarsh [§8.52, p. 266]" (attribution checked in Section C).
- f'/f = m/z - 2az + b + Σ[1/(z - a_j) + 1/a_j]; the series converges (terms z/(a_j(z - a_j)), Σa_j^{-2} < ∞). Checked.
- Im(m/z) ≤ 0, Im(-2az) ≤ 0 (a ≥ 0), Im 1/(z - a_j) = -Im z/|z - a_j|^2 < 0; strict for at least one by "at least one zero or a > 0". Checked.
- dz/dc = 1/f' = (1/c)(f/f'); Im(f/f') = -Im(f'/f)/|f'/f|^2 > 0; so Im(dz/dc) has the sign of c and d(Im z)/d|c| > 0 for either sign of c. Checked.
- Verdict: complete.
- The sentence after it (l. 322–326): for Ξ, Ξ'/Ξ = Σ_ρ 1/(z - ρ) (paired), each term has negative imaginary part when Im z > Im ρ, and all zeros have |Im ρ| < 1/2: so "Im Ξ'/Ξ < 0 for Im z > 1/2 with no hypothesis" is true. Attribution to CS (2.5) checked in Section C.

ATTEMPT 7 — Proposition 3.2 (l. 328–382; NOTE Proposition 3.2). Statement identical, hypotheses kept (real AND simple); label "in substance [CS]". Both steps added by the earlier read are present: F2a (boundary values of the argument, l. 364–367) and F2b (the bound for arg ξ(σ + ix), l. 372–377).
- (i) Ξ'/Ξ = Σ_{γ>0}[1/(z - γ) + 1/(z + γ)], Im 1/(z - γ) = -y/((x - γ)^2 + y^2): the printed inequality holds; ∫_0^∞ Σ_γ y/((x - γ)^2 + y^2) dx ≥ Σ π/2 = ∞. Ξ(iy) = Σ_n 2∫phi_n cosh(yv) > 0 (every phi_n > 0, since y = πn^2e^{2v} > 3/2). IFT with ∂_x arg < 0. Set equality: Ξ > 0 iff arg ∈ 2πZ, and arg < 0 for x > 0. Checked.
- (ii) step 1: Ξ' ≠ 0 off R (Lemma 3.1 under the hypothesis, Ξ ≠ 0 there): Ξ real with non-zero derivative along C_m, so strictly monotone; Lemma 3.1 on the branch Ξ = c through a point of C_m (the branch keeps arg = -2πm): increasing in y. Checked.
- (ii) step 2: near a non-critical non-zero real point, and near a simple zero, Ξ is injective with real preimage of real values: C_m cannot approach there; near a point with Ξ < 0 it cannot either (Ξ > 0 on C_m). Checked.
- (ii) step 3 (F2a): with the product, arg Ξ(x + iy) = Σ_γ[arg(1 - z/γ) + arg(1 + z/γ)] -> -π·#{γ < x} as y -> 0, locally uniformly off the zeros: -2πm on the m-th positive lobe (γ_{2m}, γ_{2m+1}), -2πm ± π on the neighbors. Checked.
- (ii) step 4: (Ξ'/Ξ)' < 0, Ξ'/Ξ runs from +∞ to -∞ on each lobe (simple zeros): one critical point; there Ξ'/Ξ = 0, so Ξ'' = Ξ(Ξ'/Ξ)' < 0. Checked.
- (ii) compression: the NOTE's "so for small y the point x_m(y) lies within ε of [γ_{2m}, γ_{2m+1}]" and its closing "Hence C_m tends to it" are not printed. The first gives boundedness of x_m(y) as y -> 0 (so limit points exist); the second is the conclusion of (ii). Both are one-line consequences, but the printed proof of (ii) ends without reaching its own claim. Minor m2 (pair below).
- (iii) step 1: Ξ(x + iy) = ξ(1/2 - y + ix) = ξ(σ - ix) (functional equation) = conj ξ(σ + ix) (ξ real on R). Checked.
- (iii) step 2 (F2b), term by term from x = 0 (all arguments 0 there): arg π^{-s/2} = -(x/2)log π; arg Γ(s/2) = (1/2)∫_0^x Re ψ((σ + iτ)/2)dτ ≥ (x/2)(log(σ/2) - 2/σ) [Re ψ(a + ib) - ψ(a) = Σ b^2/((n+a)((n+a)^2 + b^2)) ≥ 0; ψ(a) ≥ log a - 1/a]; arg s(s - 1) ≥ 0; arg ζ(s) > -π/2 (Re ζ ≥ 2 - π^2/6 > 0 for σ ≥ 2). Sum ≥ (x/2)[log(σ/2π) - 2/σ] - π/2 ≥ (x/2)log(σ/(2πe)) - π/2 since σ ≥ 2. Checked.
- (iii) step 3: at x = x_m(y), -2πm = -arg ξ ≤ -(x/2)log(σ/(2πe)) + π/2, and σ > 2πe^2 gives log(σ/(2πe)) > 1: x_m(y) ≤ 4πm + π. Checked.
- (iii) step 4: |ξ| -> ∞ uniformly on that segment; with (ii), Ξ maps C_m increasingly onto (M_m, ∞); a lobe with M_m > c has exactly two solutions of Ξ = c (single critical point). Bijection: first-quadrant solutions of Ξ = c > 0 lie on the union of the C_m, one on C_m iff c > M_m. Checked.
- Verdict: complete, apart from the compression m2 in (ii).

ATTEMPT 8 — the two paragraphs after Proposition 3.2 (l. 384–402).
- "What this says about the pencil": the frozen model gives (D) and (R) via 3.2(iii) (second quadrant by Ξ(-z̄) = conj Ξ(z)). Checked. The added "This is how Haglund's Conjecture 1 ... fails at N = 27 [Tya]" is not in the NOTE's §3 (which says "which is the failure of Conjecture 1"); the N = 27 support is the numerical site paragraph of §5. The description of Conjecture 1 is checked in Section C.
- "The exact criterion": ∂_tL_t = -Phi_{k+1}, dz/dt = -Phi_{k+1}/(Ξ' - L_t') = -(Phi/L)/(Ξ'/Ξ - L'/L) using Ξ = L_t ≠ 0; Im dz/dt = -Im(ρ/Λ). Checked.

ATTEMPT 9 — Lemma 4.1 and its Consequences (l. 407–436; NOTE Lemma 4.1). Statement identical.
- |cos(zv) - 1| ≤ cosh(Rv) - 1 (termwise) ≤ (1/2)R^2v^2e^{Rv} (2/(2j)! ≤ 1/(2j-2)!). Checked.
- y = Xe^{2v}: phi_n dv = (2y - 3)(y/X)^{1/4}e^{-y}dy; denominator ≥ ∫_X^∞(2y - 3)e^{-y} = (2X - 1)e^{-X}. Checked.
- Numerator: v^2 = (1/4)log^2(y/X) ≤ w^2/(4X^2); e^{Rv} = (y/X)^{R/2}; (y/X)^{1/4 + R/2} ≤ e^{w/2} iff X ≥ 1/2 + R; 2y - 3 ≤ 2X + 2w; ∫w^2e^{-w/2} = 16, ∫w^3e^{-w/2} = 96: (R^2/8X^2)(32X + 192)e^{-X}. Checked.
- Quotient (32X + 192)/(8(2X - 1)) is decreasing in X and equals 3.0774 at X = 4π: ≤ 3.1. Checked (n ≥ 2 gives X ≥ 4π).
- Consequences: |L_t| ≤ Σ_{n>k}|Phi_n| (L_t = uPhi_{k+1} + Σ_{n>k+1}Phi_n); upper bound of (1/2)Phi_n(0): e^{-X}[2X/(1-ε) + 2/(1-ε)^2] = e^{-X}(2X + 2.592) at X = 4π, ≤ (2X + 3)e^{-X}. Ratios -> 0; Cauchy for L_t'. Checked.
- Verdict: complete.

ATTEMPT 10 — Proposition 4.2 (l. 438–466; NOTE Proposition 4.2). Statement identical; no hypothesis dropped (simple, Im β > 0, Im Ξ'(β) ≠ 0).
- D, δ, Rouché (|L_t| < δ ≤ |Ξ| on ∂D): one zero, simple. IFT: dz/dt = -Phi_{k+1}/(Ξ' - L_t'). Checked.
- Uniform limits: z_k -> β (Rouché on smaller discs), L_t' -> 0 on a smaller disc, Phi_{k+1}(z_k)/Phi_{k+1}(0) -> 1. Checked.
- Phi_{k+1}(0)^{-1}dz/dt -> -1/Ξ'(β) uniformly; Im(-1/w) = Im w/|w|^2; Phi_{k+1}(0) > 0, so the sign of d(Im z)/dt is that of Im Ξ'(β) for k ≥ k_0, all t. Checked.
- Verdict: complete.

ATTEMPT 11 — Remark 4.3 (l. 468–489; NOTE Remarks (1)–(4)).
- (1) Ξ + L_t = Phi_1 + ... + Phi_k + (2 - t)Phi_{k+1} + 2Σ_{n>k+1}Phi_n: weights checked; dz/dt = +Phi_{k+1}/(Ξ' + L_t'), opposite limiting sign. Checked ((53) checked in Section C).
- (2) labeled "a sketch, not a proof": m-th roots of L_t(β)/c; for m ≥ 3 equally spaced directions, at most floor(m/2) + 1 < m lie in a closed half-plane, so one points downward; m = 2 with L > 0: both directions real iff c > 0. Consistent.
- (3) "Read in the other direction, (D) for all large k excludes the simple zeros of Ξ off the real axis with Im Ξ'(β) > 0": literally wrong for a zero in the LOWER half-plane — its conjugate β in the upper half-plane has Im Ξ'(β) of the opposite sign (Ξ'(β̄) = conj Ξ'(β)), so a lower zero with Im Ξ' > 0 belongs to an upper zero with Im Ξ' < 0, which is not excluded. The NOTE's Reading says "above the real axis". Minor m3 (pair below).
- (4) Ξ(w) = conj Ξ(-w̄) gives Ξ'(-β̄) = -conj Ξ'(β), same sign of Im. Checked.

ATTEMPT 12 — Lemma 6.1 (l. 653–666; NOTE §5 (III), the sentence marked PROVED). Promoting it to a lemma is backed by the NOTE (its §0 lists it under PROVED).
- c(t) = lim x^2F_t = 0 - (-2kappa_t'(0)) = 2kappa_t'(0) (Theorem 2.4(b) step 4). Checked.
- kappa_t'(0) = u·phi'_{k+1}(0) + Σ_{n>k+1}phi_n'(0). Recomputed phi_n'(v) = (-8y^3 + 30y^2 - 15y)e^{v/2 - y} (y' = 2y), so phi_n'(0) = -(8X^3 - 30X^2 + 15X)e^{-X}; positive alpha_n for X > 3.16, so for every n ≥ 2. Checked.
- |c(t)| = 2[u alpha_{k+1} + Σ alpha_n], strictly decreasing in t since alpha_{k+1} > 0. Checked.
- Verdict: complete.

ATTEMPT 13 — the labeled heuristics of §6 (l. 612–677): spot checks only (they are not claimed as proved).
- (I) 4(k+2)^2/(2π(k+1)^2) = 0.9947 at k = 3 ("0.5%"), 0.9167 at k = 4 ("8%"), limit 2/π: checked. |Ξ(x)| ~ x^{7/4}e^{-πx/4} (Stirling), Phi_{k+1}(0) ≈ 4a e^{-a}: consistent.
- (II) Ξ(z) = ξ(1/2 - iz) = A(1/2 - iz)ζ(1/2 - iz); ζ(2.5) - 1 = 0.3415, ζ(3) - 1 = 0.2021 ("34%", "20%"): checked. Λ ≈ -π/4 - (i/2)log(x/2π) from (1/2)ψ(s/2) - (1/2)log π at s ≈ -ix; descent iff tan(phase ρ) < 2log(x/2π)/π: checked; arctan(...) = 1.05 at x = 100, 1.18 at x = 300, 1.27 at x = 1000, so "≈ 1.2" is a mid-range value (acceptable in a heuristic).
- (III) δz ≈ (δc/c)(T/T'): |c| decreasing gives δc/c < 0, so Im δz < 0 when Im(T/T') > 0: sign checked.
