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
