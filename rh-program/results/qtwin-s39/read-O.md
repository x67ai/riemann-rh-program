# read-O — OPUS READER on unit `qtwin-s39` (NOTE.md: the last corner of Q_cond — weighted, clustering Beurling systems with Riemann's exact FE at q > 1)

Reader: Opus 5.5 (second model of the dual-model check; standing orders 5, 7, 11(c); Session 40 brief `novel-wave-s39/READ-BRIEF-O.md`).
Started 11:08 IST 2026-10-01. NOTE read whole at SHA-256 cebe0a9671de2c63fec6cfe3553bd1dd0f45bb74cbffb0cbe9d43bb640ebd1dc (407 lines).
Also read: BRIEF.md; SHARED.md; verify/ logs; sources/ (KNS 2306.14013 txt+pdf, Córdoba landing page, arXiv query files); the parent
`qcond-s38/` ("QC"): NOTE.pre-reader.md (SHA-256 445cfe96… = the version the NOTE cites, 446 lines), the CURRENT NOTE.md (SHA-256
579f22e3…, 471 lines, edited 05:24 after the parent's dual reads), and read-O.md §2 (Meyer ruling); Meyer LNM 117 p. 25 as a page
image (`fetched-r9/…pisot-salem.pdf`, p. 25) and OCR lines 670–716. NOT opened: read-F.md, verify-F/ (independence).
Independent re-run: `verify-O/` (own code from the NOTE's definitions; nothing imported from or copied out of `verify/`).
Conventions: ✓ = re-derived at the line; GAP = what is missing, with the fix; FALSE = counterexample or failing line.
"QC-pre" = NOTE.pre-reader.md line numbers (what the NOTE cites); "QC-now" = current NOTE.md.

VERDICT LINE: (provisional — filled at the end of the read)

## §1. Re-derivations at the line

(a) §1.1 Meyer at the page ✓. The page image (p. 25) prints exactly the NOTE's quote; the formula the OCR garbles is printed
    "dμ_n = n^{−1}Ψ(n^{−1}x)dμ(x)" and "μ̂_n(t) = Σ_{λ∈Λ}φ(nt − nλ)" — the NOTE's repaired normalization (line 86) is the printed one ✓.
    The only input not on disk is inside Meyer's proof: Rosenthal, Mem. AMS 63 (1966), Th. 1.6 p. 22 (m3).
(b) Lemma M ✓ (re-derived). (1) ‖n^{−1}ψ(x/n)μ‖ ≤ ‖μ‖_TB·Σ_k n^{−1}sup_{[k/n,(k+1)/n]}|ψ| ≤ C(ψ)‖μ‖_TB ✓; FT(n^{−1}ψ(·/n)) = φ(n·) so
    μ̂_n = φ(n·)∗μ̂ ✓; pointwise limit μ̂({t}) by dominated convergence (|φ(n(t−λ))| ≤ ‖φ‖_∞1_{[t−R,t+R]}, |μ̂|-integrable) ✓.
    (2) bounded set in M(bR) = C(bR)*, weak-* cluster point, ν̂(t) = lim μ̂_n(t) since characters are in C(bR) ✓. (3) B(R_d) is an
    algebra, P_v(0) = 0 makes P_v(a) vanish off supp a, P_v(a) = 1_{Λ_v} ✓ (the constant term would be harmless too: 1 = δ̂₀).
    (4) Λ_v locally finite (|μ̂|(K) ≥ min|w|·#(Λ_v ∩ K)) ✓, so Meyer's last sentence (Rosenthal) applies to Λ_v ✓.
    The same argument is in the PARENT's read-O §2 (05:20 IST, "THE FINITE-VALUES FORM … PROVED", items (i)–(iv)), finished before
    this NOTE's §1 was final (06:04) and now in QC-now §1.3(ii) — see F1 (credit), not a mathematical defect.
(c) Cor. M1 — GAP (minor, m1). The proof writes μ̂ = C + e, which presumes μ̂ PURELY ATOMIC; under the stated hypotheses (Lemma M +
    "μ purely atomic") μ̂ may carry a continuous part μ̂_c, whose inverse transform is not controlled, and the step "the a.c. density
    vanishes" fails. Fix: add "and μ̂ purely atomic" (both are pure point in every application, since μ̂_q = μ_q) — the parent's
    read-O §2(iv) states it this way ("crystalline"). With that hypothesis ✓; the π_a sanity check ✓ (1 + 1/a − 1 − 1/a = 0).
(d) §1.4 Theorem D unconditional ✓ — by either route: Lemma M + M1 (masses in {1, ρ_q} by QC-pre Cor. E3, lines 183–188), or Meyer's
    printed unit-mass statement applied verbatim to μ′ = μ_q − (ρ_q − 1)·Lebesgue (parent read-O §2; QC-now Theorem D step (1)). Then
    QC-pre §2.7 steps (2)–(6) (lines 324–333) with constant weights, Lemma Q not needed ✓. Record: the unconditional status was
    established by the parent's dual read and applied to QC at 05:24 (QC-now); the NOTE's "now UNCONDITIONAL" (lines 52, 77, 119,
    126, 312, 383, 403) should credit that (F1).
(e) THEOREM G1 ✓ (re-derived line by line). Step 0: exp*(tΠ)({z}) = Σ_k t^kΠ^{*k}({z})/k! is > 0 iff some Π^{*k}({z}) > 0,
    independent of t > 0; dN∗dN ≥ c(x)c(y)δ_{xy} ⟹ 𝒩 a monoid ✓; Π finite on (1, x] so the series converge ✓; 𝒩 ≠ {1} (F ≢ 1).
    Step 1: x(a − a′) ∈ √qα_jZ∖0, a − a′ ∈ √qα_iZ∖0 ⟹ x ∈ (α_j/α_i)Q ✓; finite cancellative monoid ⟹ group ✓. Step 2: weight on
    y_j + αZ is g_j(y_j + αn)·N_j^{−1}Σ_{r mod N_j}e^{2πirn/N_j}, a trig polynomial in n ✓; two cosets of incommensurable lattices meet
    in ≤ 1 point ✓; a non-rational coset meets each β_γQ/√q at most once (≤ |Γ| points, the NOTE's 2|Γ| + 1 is a safe overcount) ✓;
    a trig polynomial on Z vanishing off a finite set is 0 (Bohr mean) ✓. Step 3: FT(Σ_ne^{2πiθn}δ_{y+αn}) = α^{−1}Σ_m
    e^{−2πiy(θ+m)/α}δ_{(θ+m)/α} ✓ (atoms of modulus 1/α on (θ + Z)/α); (θ + Z)/α meets βQ at most once for θ ∉ Q ✓; ω̂_I = μ̂_q − ω̂_R
    is a pure point measure whose atoms lie in (finite union of irrational cosets) ∩ (finite union of Q-lines) = finite E ✓; ω_I is
    then a.c. and pure point, so 0, and per coset the irrational coefficients vanish (Bohr mean again) ✓. Step 4: rational cosets of
    class γ are mutually commensurable, so no exceptional points inside a class; a_γ periodic ✓; QC-pre §2.7 steps (4)–(6) use
    periodicity only (S–W Thm 1 is linear algebra on periodic coefficients; S–W′; ρ_q ≥ 1 by QC E1 for the pole; L′ for real
    frequencies; BFE T) — no integrality ✓. "Integrality of masses: nowhere" ✓.
    ATTEMPT TO BREAK (verify-O/o2): positive, self-dual finite combs WITH irrational frequencies exist — μ_c = Σ_n(c + 2cos2πθn)δ_n
    + δ_{θ+Z} + δ_{−θ+Z} (c ≥ 2, θ ∉ Q, frac θ ∈ [r, 1 − r], q ≥ 4) is positive, even, μ̂_c = μ_c (Poisson pairs Σe^{2πiθn}δ_n ↔ δ_{θ+Z}),
    lies in 𝓜_r, and has infinitely many mass values. It is not Beurling: its support is not inside finitely many Q-lines (θ + Z
    meets each Q-line once), which is exactly what Step 1 forbids; Step 3 is therefore not vacuous and is used where it must be.
    No counterexample to G1 found; the theorem is correct as stated given QC's S–W′ (single-check extension of a printed proof).
(f) Cor. G1′ ✓ (μ_q ≥ 0, μ̂_q = μ_q ⟹ TB; values finite; Lemma M + M1 with μ̂ = μ pure point; G1 with constant weights).
(g) §3 rung 1 ✓ (re-run exactly, §2(a)). (W1) for d ≤ 60 ✓; the NOTE's "exactly" (all d) needs a tail bound the NOTE does not
    give — supplied in §7 A1 (m2). (W2) ✓, (W3) ✓ (the four-line certificate is right: s₁, s₂, s₄ ≤ 1 confine t to
    [−√11, −√(10 − √51)], where s₃ − 1 = t³ − 15t − 1 > 0), (W4) ✓. Dictionary (i)–(iii) ✓ as readings (no load).
(h) Lemma A ✓. ‖m − δ₁‖_σ = ∫_{(1,Q]}b^{−σ}d|m| → 0 ✓; m = m_a∗(δ₁ + κ), κ = m_a^{*−1}∗m_c continuous ((ν∗κ)({x}) = ∫κ({x/y})dν(y) = 0) ✓;
    atomic and continuous measures are closed bands under ‖·‖_σ-limits ✓; (Π_F)_atomic = Π_ζ + log*(m_a) ≥ 0 ✓. FE: D(1 − s) =
    q^{s−½}D(s) ⟺ b^{−1}dm(b) = q^{−½}d(J_*m)(b) (Mellin uniqueness on Re s = 0), i.e. m_{q/b} = √q·m_b/b on atoms ✓; J preserves
    atoms, so D_a has the FE ✓. Side fact: J-invariance forces supp m ⊂ [1, Q] ∩ [q/Q, q], so q ≥ 1 and supp m ⊂ [1, q].
    Notation (m4): "Λ_F = q^{s/2}ξ(s)D(s)" uses ξ for π^{−s/2}Γ(s/2)ζ(s) (poles at 0, 1), not Riemann's entire ξ; harmless.
(i) THEOREM L‴ (bounded range) ✓. (1) p^k = γ·s (γ ∈ ⟨B⟩, s ∈ ⟨S⟩) ⟹ γ = p^k/s ∈ Γ ∩ Q_{>0} ⟹ p ∈ S ✓. (2) ✓. (3) The Landau step is
    PROVED, not only recalled: QC-pre Lemma L's proof (lines 191–195: Taylor at c = σ_a + 1, all terms ≥ 0, Tonelli) never uses local
    finiteness and applies verbatim to ∫e^{−su}dα(u), α(u) = Π_{F_a}|_G({log g ≤ u}) nondecreasing and finite (Π_{F_a} is Radon on
    (1, ∞) with no atom at 1) — replace "[recalled, standard]" (lines 222, 370) by this (m5). Branch argument: h(σ) = exp(Σ ≥ 0) ≥ 1
    for real σ > max(σ_a, σ*); h analytic on Re s > σ* (Π_{p∈S}(1 − p^{−s})^{−1} converges absolutely and is zero-free for σ > σ_S) ✓.
    (4) σ* < 1 − σ* ⟺ σ* < ½ ✓; |D_a(s)| ≤ ‖m_a‖max(1, Q^{−σ}) ⟹ order ≤ 1 ✓; Hadamard ⟹ e^{α+βs} ⟹ m_a = e^αδ_{e^{−β}} (uniqueness) ⟹
    m_a = δ₁ ⟹ q^{s−½} ≡ 1 ⟹ q = 1 ✓; BFE T ✓. EXACTLY WHERE σ_S = ½ STOPS IT: at σ* = ½ the half-planes Re s > ½ and Re s < ½ leave
    the line Re s = ½, and D_a may vanish there (e.g. 1 + √q q^{−s} has all its zeros on Re s = ½) ✓ — the NOTE's statement is sharp
    for the method. Note: at σ_S = ½ the method still FORCES all zeros of D_a onto Re s = ½ (single-check, §7 A2).
(j) Proposition S ✓. On Re s = ½: ∫x^{−½}d|m| < ∞ since σ₀ < ½ ✓; D = F/ζ on Re s > σ₀ by continuation, and the FE of D holds on
    the strip as an identity of absolutely convergent transforms ✓. E(t) is uniformly a.p. ✓; right side = ν̂(t) for a finite
    CONTINUOUS ν ✓; Wiener's lemma re-proved at the line: (2T)^{−1}∫_{−T}^{T}|ν̂|² = ∬sinc(2πT(x − y))dν(x)dν̄(y) → (ν × ν̄)(diagonal)
    = Σ|ν({x})|² = 0 ✓; Bohr–Parseval ⟹ E ≡ 0 ✓; identity theorem on the strip ✓; D_a(s) := q^{½−s}D_a(1 − s) on Re s < 1 − σ₀
    continues D_a to C with |D_a| ≤ C·max(1, q^{½−σ}) ✓; log* splitting needs only ‖m − δ₁‖_σ → 0 for large σ ✓.
(k) L‴ (general) ✓ (Prop. S + (i) verbatim; D_a order ≤ 1; uniqueness of the transform on Re s > σ₀).
(l) §6 route (iii) ✓ with one mis-attribution (m6). The zeta-zero repair: G(1 − s) = q^{s−½}G(s) ✓; poles of G at ρ, 1 − ρ are
    cancelled by ζ ✓; m_c = Σc_ρ[x^{ρ−1}1_{[1,∞)} − q^{ρ−½}x^{−ρ}1_{[q,∞)}]dx ✓ (Mellin of each term re-computed); G_c satisfies the
    FE alone ✓ (re-computed term by term); (Π_F)_atomic = Π_ζ + log*(δ₁ + √qδ_q) has mass ≤ 1 − q^k/(2k) at q^{2k} ✓ (q = √2: 8 ✓).
    BUT these repairs do NOT satisfy Prop. S / L‴(general) hypothesis (i): for zeros on the line |x^{ρ−1}| = x^{−½}, so
    ∫x^{−σ₀}d|m| = ∞ for every σ₀ ≤ ½. The NOTE's own text says "split directly" (lines 55, 297–299, 314), but line 301 ("COVERAGE OF
    L‴ (general) … every zeta-zero repair whose atomic part is thin") and line 299 ("More atoms in m_a lead back to L‴") attribute
    them to L‴(general). Correct route: the direct splitting (G_c has the FE alone) + log* splitting (needs only large σ) + §4's
    bounded-range L‴ applied to F_a. The conclusion stands; the attribution must change.
(m) §5.1 the exact reduction ✓. Minkowski lattice {(x/c, x^σ/c)} has covolume √5/c² = 1 ✓; its dual is {(z/c, −z^σ/c)} (for w = zx ∈ O_K,
    (w − w^σ)/√5 ∈ Z) ✓; Poisson for g ⊗ k gives μ̂_k = μ_{k̂(−·)} = μ_{k̂} for even k ✓; k ↦ μ_k injective (the x^σ/c are dense) ✓, so
    "self-dual iff k̂ = k" ✓. Gap ⟺ k = 0 on Z_j: the atom "1" at φ^{−j}/c = r gives q = √5φ^{2j} ✓, n = xφ^j, weight k(n^σφ^j/c) ✓;
    density 2/(cφ^j) ✓ (window width 2, covolume √5, scale φ^j/c). P1 ✓ (one line).
(n) P2 — GAP (minor, m7). KNS Thm 1(ii) is quoted correctly (sources/ txt lines 101–139: subcritical pairs are non-uniqueness
    pairs for S; Z_j u.d. ⟹ |λ_j|^{p−1}(λ_{j+1} − λ_j) → ∞ ✓). But it yields f ≠ 0 with f|_Z = f̂|_Z = 0, not an EVEN SELF-DUAL k: the
    space V of such f is Fourier-invariant (Z_j = −Z_j), yet its eigenvalue-1 part is not shown non-zero, so "the zero conditions
    alone do not force k = 0" (line 253) is not yet proved for k̂ = k. Fix (§7 A3, single-check): KNS Lemma 6 (§7.3, lines 2000–2016)
    interpolates freely on Λ′_L ⊋ Λ with infinitely many extra nodes; prescribing data at N symmetric extra nodes and imposing the
    K finitely many conditions on Z_j ∩ [−L, L] leaves a ≥ (2N − K)-dimensional family, and for N > K some member has a non-zero
    eigenvalue-1 projection P₁f = (f + f̂ + f(−·) + f̂(−·))/4, which is even, self-dual, vanishes on Z_j; Re or Im of it is real.
(o) §5.2 ✓ (re-derived): unit orbit divisor-closed in O_K (a unit factors only into units) ✓; Π(φ²) ≥ 0 ⟺ e^{πφ^{2j−2}/√5} ≤ 2 ✓
    (algebra: log 2 ≥ (π/√5)φ^{2j−4}(φ² − 1)² = (π/√5)φ^{2j−2}); values reproduced (§2(c)). k = e^{−2π|t|} + 1/(π(1 + t²)) is
    positive, self-dual (FT e^{−2π|t|} = 1/(π(1 + ξ²))) ✓.
(p) §7.2 the class 𝒯 ✓ as a reduction: for m ∈ 𝒯, dN = Σ_nΣ_b m_bδ_{nb} ≥ 0 carried by [1, ∞) (gap) ✓, FE by J-symmetry ✓, μ_q ∈ 𝒦_r ✓,
    so Q_cond on 𝒯 ⟺ Π_ζ + log*(m) ≥ 0 ✓; L′ excludes finite truncations ✓; thin atomic m excluded by §4 ✓; continuous parts
    reduce to atomic by Lemma A ✓. A member of 𝒯 satisfying the condition WOULD be a Q-side twin (q > 1, not ζ). Numbers: §2(d).
(q) THEOREM G (§0.4) as a whole ✓ as a summary of (1)–(3), with three record corrections: (1)'s "Theorem D, now UNCONDITIONAL" is
    the parent's dual-read result (F1); (1)'s coverage parenthesis "the zeta-zero repairs … split directly" is right, but §6's
    coverage line contradicts it (m6); the 𝒯 probe numbers in (THE SMALLEST OPEN SUB-CLASS) change at M = 4 (F3).

## §2. Independent re-run (`verify-O/`; own code from the NOTE's definitions; the unit's scripts were not opened, only its logs)

(a) Rung 1, exact (`o1_rung1_exact.{py,log}`; sympy exact rationals, isolating intervals + exact sign tests — a different route
    from the unit's arb balls). d·b_d(t) ∈ Z[t] built from N_e = 1 + 5^e − s_e (s_e = ts_{e−1} − 5s_{e−2}); for every d ≤ 60 no
    negative value and no odd-order root strictly inside (−5, 6); P₁(6) = P₂(−5) = 0, all P_d(6) = 0; P₂ = −(t − 6)(t + 5) ⟹ W1 on
    d ≤ 60 AGREES exactly. W3: s₁, s₂, s₄ ≤ 1 ⟺ t ∈ [−√11, −√(10 − √51)] = [−3.316625, −1.690731]; s₃ − 1 has no root in
    [−3.32, −1.69] and s₃(−2) − 1 = 21 ⟹ EMPTY — AGREES; the roots −3.8392, −0.0667, 3.9059 and ±1.6907, ±4.1402 match the NOTE to 4
    digits. W2, W4 AGREE.
(b) G1 control (`o2_irrational_comb.{py,log}`, mpmath 60 digits): μ_c = Σ(2 + 2cos2πθn)δ_n + δ_{θ+Z} + δ_{−θ+Z}, θ = √2 − 1: theta
    pairings equal at y = 0.37, 1, 2.2, 5.1 (|diff| ≤ 1.2e−60); masses ≥ 0; gap for q ≥ 5.83. Positive self-dual finite comb with an
    irrational frequency — excluded from Beurling by G1 Step 1 (support meets each Q-line once), as G1 requires.
(c) Route (ii) (`o3_pisot.{py,log}`, mpmath 50 digits, own lattice sum |a|, |b| ≤ 45): theta pairing of μ_k (Gaussian k) equal to
    2.7e−51 (y = 0.37), 0 (y = 1), 1.1e−50 (y = 2.2) — AGREES with the NOTE's 2.7e−51; Z_0 first points 1.0820, 1.7508, 2.8328;
    Z_1: 1.7508, 2.8328, 4.5836 — AGREE; unit orbit Π(φ²) = 0.481 (j = 0), −24.013 (j = 1), −7.01e4 (j = 2), −1.709e13 (j = 3) —
    AGREE (criterion e^{πφ^{2j−2}/√5} = 1.71, 4.08, 39.6, 1.5e4 against 2).
(d) THE 𝒯 PROBE at q = 4 (`tprobe_core.py`, `o4a_selftest`, `o4b_optimize`, `o4c_gradopt`, `o4d_polish_M4`, `o4e_driver` + logs).
    Method (independent of the unit's): atom positions exact (Fractions); log*(m) on the monoid G ≤ 64 from D′ = D·L′, i.e. the
    unit-lower-triangular sparse system u(x) + Σ_a m_a u(x/a) = m_x log x, u = log*(m)·log x; Π_F = u/log x + Π_ζ; global search by
    differential evolution (3 seeds, popsize 25) then SLSQP on the epigraph with ANALYTIC gradients (checked against central
    differences: 3.0e−10). Self-tests: Π(2) = 1 + t, Π(16/3) = −4wt/3, Π(3/2) = w, Π(8/3) = 4w/3 exact; control D = 1 + 2·4^{−s}:
    Π(4^k) = 2.5, −1.75, 2.8333, −3.875 = 1/(2k) + (−1)^{k+1}2^k/k exactly.
    Design as in the NOTE (lower atoms n/d ∈ (1, 2), d ≤ M; J-partners; m₂ = t; m₄ = 2):
      M = 2 (3/2): max-min = −0.680076 at (t, w) = (2.04143, 0.24985), binding 16/3 — AGREES digit for digit (DE global).
      M = 3 (4/3, 3/2, 5/3): −0.400711 at t = 0.74486, w = (0.48669, 0.48669, 0.68611) — AGREES digit for digit with the unit's
        local value; DE from 3 seeds finds nothing better.
      M = 4 (+5/4, 7/4): −0.293651 at t = 0.318472, w = (0.386373, 0.386373, 0.355084, 0.301804, 0.665016) — BETTER than the NOTE's
        −0.310622 (its "local search" value). Seven constraints are active (x = 16/3, 20/7, 64/21, 64/7, 128/21, 320/7, 4608/175)
        = number of unknowns (6 weights + τ). Exact re-evaluation with rational weights by a SECOND algorithm (convolution-power
        series in Fractions): min Π_F = −0.293650523 at 64/7 ✓. So the NOTE's M = 4 entry (lines 69, 331, 334, 384) is not the best
        attainable; the trend reading (−0.68 → −0.40 → −0.29) is unchanged in direction (F3).
