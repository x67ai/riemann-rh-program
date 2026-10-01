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

VERDICT LINE: AGREES-WITH-CORRECTIONS on the close "G, stated as a theorem, with RIGIDITY extended; no construction". Every
theorem, proposition, lemma and corollary was re-derived at the line — Lemma M, G1 (Steps 0–4, including the new Fourier-side
Step 3, attacked with an explicit positive self-dual gapped comb with an irrational frequency, which G1 correctly excludes at Step 1),
G1′, Lemma A, L‴ in both forms (the Landau step is PROVED by QC Lemma L's own proof; nothing recalled is needed), Prop. S (Wiener's
lemma re-proved), the route-(iii) repair, P1, the §5 reduction and the 𝒯 reduction — and no load-bearing rigidity statement is false.
The decisive computations reproduce by independent routes: rung 1 exactly (W1 for d ≤ 60, the W3 certificate, now with a proof for
all d), the Pisot self-duality test and orbit values, and the 𝒯 probe at M = 2, 3 digit for digit. Six FIX-FIRST items: (F1) credit —
Lemma M/M1 and the unconditional Theorem D were proved first in QC's dual read (qcond-s38/read-O §2) and are in QC-now; (F2) missed
prior art on disk — Hilberdink 2012 (Acta Arith. 152): Prop. 3.4 excludes every finite positive rational multiplier with a
non-integer atom WITHOUT the FE (every probe design), Thm 4.4 contains W3, Thm 4.3 is the printed finite-S core of L′/L‴, Thm C
classifies the squarefree-period case; (F3) the M = 4 probe value is ≥ −0.293651, not −0.31 (M = 5: ≥ −0.218541); (F4) Cor. M1 is
false as written (μ = δ₀, μ̂ = Lebesgue) — add "μ̂ purely atomic"; (F5) zeta-zero repairs fail hypothesis (i) of Prop. S/L‴(general)
and are covered instead by the direct splitting + §4; (F6) §5.2's mechanism (b) is a heuristic labeled (P), so "k cannot be smooth"
and §0.4(3)'s "every finite-dimensional family … is excluded" are unproved — smooth even self-dual k vanishing on Z_j exist (KNS
Lemma 6, §7 A3). Ten minor pairs. No Q-side twin: no member of 𝒯 with Π_F ≥ 0 was found; every finite design is excluded (L′;
Hilberdink Prop. 3.4), and at each window optimum about half the atoms of Π_F are negative.

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

## §3. Prior art at the page

| source (opened) | at the line | verdict on the NOTE's use |
|---|---|---|
| Meyer 1970, LNM 117, §4.2 p. 25 (`fetched-r9/…pisot-salem.pdf` p. 25 as an image; OCR 677–713) | unit masses; dμ_n = n^{−1}Ψ(n^{−1}x)dμ; Rosenthal [7] th. 1.6 p. 22; p. 26 "On retrouve donc la formule de Poisson habituelle" | quoted exactly ✓; Rosenthal (inside Meyer's proof) not on disk — label it (m3) |
| QC `read-O.md` §2 (05:20 IST) and QC-now (579f22e3…) §1.3(ii), Theorem D step (1) | finite-values form proved via Meyer's Bohr passage + Lagrange idempotents; D unconditional via μ_q − (ρ_q − 1)·Lebesgue | SAME results as the NOTE's Lemma M, M1, §1.4, earlier on the record — credit missing (F1) |
| Hilberdink 2012, Acta Arith. 152, 217–241 (BFE `sources/p3-22c2-…txt`) | Thm 4.3 (812–905): Q(s) = Σ_{d∣P}q(d)d^{−s}, t(n) ≥ 0 off prime powers ⟹ t(n) = 0 there, by a several-variable Landau argument on Q̃(p₁^{β}, x₂, …, x_r); Thm 4.4 (1028–1066): τ_n = Σμ_r^n ≤ 1 ∀n ⟹ |μ₁| ≤ 1 (k = 1), |μ_r| < 1 (k > 1) | NOT CITED by the NOTE (flagged on disk by QC read-O F2 at 05:20). Thm 4.4 with k = 2, μ = α, β, |αβ| = 5 gives (W3)'s emptiness for every real t at once; Thm 4.3 is the printed finite-S, integer-frequency core of the L′/L‴ mechanism and the printed precedent for UT-QT1's "several-variable Landau" (F2) |
| Kurasov–Sarnak 2020 (BFE u-20b) | 43–44 Meyer as quoted (finite values, |μ̂| TB); 47–49 "any such classification is probably very difficult [5]"; 56–58 positive non-comb question; 792–796 (A) answered | quoted correctly ✓ |
| Baake–Spindeler–Strungaru 2023 (QC 2104.06812) | §8 Outlook 1235–1241: "the characterisation of all doubly sparse measures, an important open problem … is equivalent to the characterisation of all doubly sparse eigenmeasures"; Thm 7.5 (1160–1172): doubly sparse eigenmeasures with LARGE GAPS around 0 (signed) | quoted correctly ✓; Thm 7.5 is worth a line: gapped self-dual measures abound once signs are allowed (consistent with BFE read-O R1) (m8) |
| Kulikov–Nazarov–Sodin 2023 (sources/ 2306.14013) | Def. 2 101–118; Thm 1 137–139; Thm 1-NUP 1871; Lemma 6 2000–2016 (free interpolation on Λ′_L, M′_L) | Thm 1(ii) quoted correctly ✓; P2 needs Lemma 6 to reach even self-dual k (m7, §7 A3) |
| Lev–Olevskii 2015 (BFE 1312.6884) | 63–68 "finitely many different values … [17, p. 25], [6], [11] … Helson-Cohen"; Thm 1 103–105 | quoted correctly ✓; LO's "[17, p. 25]" over-attributes (p. 25 is unit masses) — the NOTE's §1.1 says so; its §8 row should too (m9) |
| Widder, The Laplace Transform, Thm II.5b (NOTE lines 222, 370, "[recalled, standard]") | not opened | not needed: QC Lemma L's proof covers it (m5) |
| Wiener's lemma (Prop. S) | not opened | re-proved at the line in §1(j) |
| arXiv, reader's queries q7–q9 (`verify-O/sources/`) | see §8 for status | — |

## §4. FIX-FIRST pairs (OLD quoted exactly at NOTE SHA-256 cebe0a96…, with line numbers; not applied — the orchestrator applies)

F1 — credit: Lemma M, Cor. M1 and the unconditional Theorem D were proved first in QC's dual read (read-O §2, 05:20 IST) and
entered QC-now (579f22e3…) at 05:24; the NOTE (final 06:04) cites QC at 445cfe96 and claims them as its own.
OLD (91–92): "So the primary proves the unit-mass case, with a finite exceptional set; QC's secondary quote Q4 (Kurasov–Sarnak: "If aλ take values in a finite set … then µ is a generalized Dirac comb") is the finitely-valued extension. It is proved here (Lemma M, M1)."
NEW: "So the primary proves the unit-mass case, with a finite exceptional set; QC's secondary quote Q4 (Kurasov–Sarnak: "If aλ take values in a finite set … then µ is a generalized Dirac comb") is the finitely-valued extension. It was proved in QC's dual read (qcond-s38/read-O.md §2, items (i)–(iv), now QC §1.3(ii) at 579f22e3…); Lemma M, M1 below re-derive it independently (two independent derivations)."
OLD (107–108): " UPSTREAM (10(n)): Meyer 1970 p. 25 (unit masses, purely atomic μ̂); the Lagrange step is the standard reduction of finitely valued Fourier–Stieltjes transforms to idempotents; Kurasov–Sarnak's quote (u-20b 43–44) states the result. `[single-check]`"
NEW: " UPSTREAM (10(n)): Meyer 1970 p. 25 (unit masses, purely atomic μ̂; its last step is Rosenthal, Mem. AMS 63 (1966) Th. 1.6 p. 22, not on disk); the Lagrange step is the standard reduction of finitely valued Fourier–Stieltjes transforms to idempotents; Kurasov–Sarnak's quote (u-20b 43–44) states the result; the same proof is qcond-s38/read-O.md §2. `[dual-checked: this NOTE and QC read-O §2, independently]`"
OLD (126): " STATUS. QC §2.6(b)'s conditional clause and QC §5's "T given one printed theorem on disk only second-hand" are discharged."
NEW: " STATUS. QC §2.6(b)'s conditional clause and QC §5's "T given one printed theorem on disk only second-hand" are discharged — as already recorded by QC's dual read (read-O §2 RULING; QC-now Theorem D step (1), via Meyer's printed statement applied to μ_q − (ρ_q − 1)·Lebesgue); this section is an independent second route (Lemma M + M1)."
OLD (355): "self-dual (doubly sparse) measures" (BSS §8; KS line 49). Novelty labels: Lemma M = Meyer + a standard reduction `[single-check]`;"
NEW: "self-dual (doubly sparse) measures" (BSS §8; KS line 49). Novelty labels: Lemma M = Meyer + a standard reduction, also proved in QC read-O §2 `[dual-checked]`; Theorem D unconditional: QC's dual-read result, re-derived here;"

F2 — missed prior art on disk (changes novelty labels): Hilberdink 2012, Acta Arith. 152, 217–241 (`novel-wave-s37/beurling-fe/
sources/p3-22c2-…txt`; already flagged by QC read-O F2), Thm 4.3 (lines 812–905) and Thm 4.4 (lines 1028–1066).
OLD (175–176): "s₃ ≤ 1 ⟺ t ∈ (−∞, −3.8392] ∪ [−0.0667, 3.9059]; s₄ ≤ 1 ⟺ |t| ∈ [1.6907, 4.1402]. The intersection is EMPTY: Theorem L′'s obstruction holds at rung 1 for every real t, weights allowed — a four-line exact certificate."
NEW: "s₃ ≤ 1 ⟺ t ∈ (−∞, −3.8392] ∪ [−0.0667, 3.9059]; s₄ ≤ 1 ⟺ |t| ∈ [1.6907, 4.1402]. The intersection is EMPTY: Theorem L′'s obstruction holds at rung 1 for every real t, weights allowed — a four-line exact certificate. The conclusion (for all n) is in print: Hilberdink 2012, Acta Arith. 152, Thm 4.4 (BFE sources/p3-22c2 lines 1028–1066: τ_n = Σμ_r^n ≤ 1 ∀n forces |μ_r| < 1 when k > 1; here k = 2, |αβ| = 5); what is new is only that n ≤ 4 suffices."
OLD (221–222): "meets Q_{>0} only in S-units for a finite (or thin) prime set S — is excluded at every conductor. `[novelty: single-check]` UPSTREAM: Landau 1905 / Widder, The Laplace Transform, Thm II.5b `[recalled, standard]`; QC Theorem L′."
NEW: "meets Q_{>0} only in S-units for a finite (or thin) prime set S — is excluded at every conductor. `[novelty: new in its infinite-atom / real-frequency / continuous-part statement; the finite-S mechanism is printed for integer divisor-supported multipliers in Hilberdink 2012, Acta Arith. 152, Thm 4.3 (BFE sources/p3-22c2 lines 812–905, a several-variable Landau argument); single-check]` UPSTREAM: QC Lemma L (its proof needs no local finiteness, so it covers Laplace–Stieltjes transforms of positive measures); QC Theorem L′; Hilberdink 2012 Thm 4.3."
OLD (390): "  Laurent) Landau theorem — the one-variable version is L‴ and stops at σ_S = ½ — or a construction with atoms (p + 1)/p. Fit: S1"
NEW: "  Laurent) Landau theorem — the one-variable version is L‴ and stops at σ_S = ½; the printed several-variable precedent is Hilberdink 2012, Acta Arith. 152, Thm 4.3 (finitely many primes, polynomial weights) — or a construction with atoms (p + 1)/p. Fit: S1"
OLD (328, first clause): "Every finite truncation of 𝒯 has finite S and is excluded by L′; the probe measures how far the violation can be pushed."
NEW: "Every finite truncation of 𝒯 has finite S and is excluded by L′; a truncation with rational atoms one of which is not an integer is excluded already WITHOUT the FE by Hilberdink 2012, Acta Arith. 152, Prop. 3.4 (BFE sources/p3-22c2 lines 632–660: if N ∈ T, N(x) − cx periodic and Π increasing — an "outer g-prime system", Def. 1.2, line 317, = the program's weighted Beurling system — then every discontinuity of N is an integer; here N(x) = Σ_b m_b⌊x/b⌋ jumps at every atom b, and step functions lie in T, line 269). All the probe's designs are of this kind; the probe measures how far the violation can be pushed."
Also add a §8 table row after line 352: "| Hilberdink 2012, Acta Arith. 152 ([BFE] p3-22c2: Prop. 3.4 632–660, Prop. 4.2 741–760, Thm 4.3 812–905, Thm 4.4 1028–1066, Thm C 1138–1150) | for OUTER g-prime systems (Π increasing, Def. 1.2) with N ∈ T and N(x) − cx periodic: discontinuities at integers, period P ∈ N, N̂ = Q·ζ with Q on the divisors of P; several-variable Landau (Thm 4.3); power sums τ_n ≤ 1 ∀n ⟹ |μ_r| < 1 (Thm 4.4); squarefree P: exactly ζ·Π_{p∣P}(1 + q(p)p^{−s}), |q(p)| ≤ 1 (Thm C) | printed core of L′/L‴ for rational finite multipliers (no FE needed when an atom is a non-integer rational); contains (W3); limit-periodic N − cx (infinitely many rational atoms, i.e. 𝒯 proper) is outside it |".

F3 — a number that does not reproduce as "best attainable" (the reader's global optimizer, §2(d)): at q = 4, M = 4 the max-min
on [1, 64] is ≥ −0.293651 (achieved; exact-rational re-check −0.293650523), not −0.31; M = 5 reaches −0.218541.
OLD (68–69): "Π_ζ + log*(m) ≥ 0. Every finite truncation fails (L′); the probe raises the best attainable min Π_F on [1, 64] from −0.68 (one atom pair, global) to −0.31 (five pairs, local) at q = 4 as primes are added — evidence only."
NEW: "Π_ζ + log*(m) ≥ 0. Every finite truncation fails (L′); at q = 4 the max-min of Π_F on [1, 64] rises from −0.680 (one atom pair, global) through −0.401 (three pairs) and ≥ −0.294 (five pairs) to ≥ −0.219 (nine pairs) as atoms are added (read-O §2(d)), while about half the atoms stay negative at every optimum and the total negative mass grows — evidence of nothing about 𝒯."
OLD (331): " M = 3, 4 (local search, values are achieved, hence lower bounds for the max-min): −0.4007, −0.3106 (binding x = 16/5, 384/7)."
NEW: " M = 3, 4 (local search, values are achieved, hence lower bounds for the max-min): −0.4007, −0.3106 (binding x = 16/5, 384/7). Reader's global search (read-O §2(d)): M = 3 −0.400711 (same); M = 4 −0.293651 (seven active constraints); M = 5 −0.218541."
OLD (384, the cell): "−0.680 (one pair 3/2 ↔ 8/3, global grid + polish); −0.401, −0.311 (M = 3, 4 pairs, local search, achieved values)"
NEW: "−0.680 (one pair 3/2 ↔ 8/3, global grid + polish); −0.401 (M = 3); ≥ −0.2937 (M = 4) and ≥ −0.2185 (M = 5), reader's DE + SLSQP (`verify-O/o4b`, `o4e` logs); about half the atoms negative at each optimum"

F4 — a false statement: Cor. M1 as written (Lemma M's hypotheses + "μ purely atomic"). Counterexample: μ = δ₀ is purely atomic and
TB, μ̂ = Lebesgue is a Radon measure with no atoms (a ≡ 0 ∈ V ∪ {0}), yet μ̂ is not a finite combination of progression combs. The
proof's "μ̂ = C + e" silently assumes μ̂ purely atomic. Every use (μ̂_q = μ_q) is unaffected.
OLD (111): "If in addition μ is purely atomic, then μ̂ = Σ_{j≤J} κ_j δ_{β_j+α_jZ} exactly (finite, κ_j ∈ C): no finite correction survives."
NEW: "If in addition μ and μ̂ are both purely atomic (e.g. μ̂ = μ pure point), then μ̂ = Σ_{j≤J} κ_j δ_{β_j+α_jZ} exactly (finite, κ_j ∈ C): no finite correction survives. (Without "μ̂ purely atomic" it fails: μ = δ₀, μ̂ = Lebesgue.)"

F5 — a false coverage statement: zeta-zero repairs do NOT satisfy hypothesis (i) of Prop. S / L‴(general) — for zeros on the line
|x^{ρ−1}| = |x^{−ρ}| = x^{−½}, so ∫x^{−σ₀}d|m| = ∞ for every σ₀ ≤ ½. They are covered by the direct splitting (G_c has the FE alone,
§6(b)), the log* splitting (which needs only large σ) and the bounded-range L‴ of §4 applied to F_a.
OLD (299, last two sentences): "More atoms in m_a lead back to L‴. So route (iii) produces no exact solution outside the residue of §4."
NEW: "For repairs built term by term on a bounded-range atomic m_a (so that the continuous part satisfies the FE by itself), the same direct splitting makes F_a = ζ·D_a a Beurling solution and §4's bounded-range L‴ applies when the atoms' rational part is thin; Prop. S does not apply to repairs (their densities are ≍ x^{−½}). So route (iii) produces no exact solution of this kind outside the residue of §4."
OLD (300–301): "COVERAGE OF L‴ (general). All of route (i) with thin rational part, continuous parts included; every zeta-zero repair whose atomic part is thin; every solution whose quotient F/ζ converges absolutely to the left of ½ with thin atoms."
NEW: "COVERAGE OF L‴ (general). All of route (i) with thin rational part, continuous parts included; every solution whose quotient F/ζ converges absolutely to the left of ½ with thin atoms. (Zeta-zero repairs with zeros on the line are NOT in its scope — hypothesis (i) fails — and are handled by the direct splitting of §6(b) + §4.)"

F6 — a heuristic labeled (P), and two claims resting on it. §5.2 MECHANISM (b) is not a proof: Π(n) is the full alternating series
Σ_j(−1)^{j+1}(dN − δ₁)^{*j}({n})/j, and when c(xy) ≪ c(x)c(y) the higher-order terms are LARGER, not smaller (c(a)c(b)c(n₂) ≫ c(ab)c(n₂)
when n₁ = ab), so the sign of the second-order term decides nothing. Hence "k cannot be smooth" is unproved; and smooth, even,
self-dual k ≢ 0 vanishing on Z_j DO exist (KNS 2023 Lemma 6 + §7 A3), spanning finite-dimensional families with the exact FE and the
gap that no certificate of §7.1 excludes (positivity — double zeros on Z_j — and the Euler condition are open there). So §0.4(3)'s
first sentence overclaims.
OLD (61–62, first sentence): "(3) THE OBSTRUCTION TO CONSTRUCTION (P). Every finite-dimensional family on which the exact FE can be imposed is excluded (§7.1 table: G1, G1′, D, L′, L‴, U_q, P1, W3)."
NEW: "(3) THE OBSTRUCTION TO CONSTRUCTION (P for the listed families). Every finite-dimensional family in the §7.1 table is excluded (G1, G1′, D, L′, L‴, U_q, P1, W3); finite-dimensional families of model-set measures with smooth self-dual weights vanishing on Z_j (which exist, KNS 2023 Lemma 6) are not excluded by any theorem here."
OLD (63): "thick rational part; (R2) model-set (cut-and-project) measures whose self-dual weight is non-smooth and vanishes on a"
NEW: "thick rational part; (R2) model-set (cut-and-project) measures whose self-dual weight (smooth or not) vanishes on a"
OLD (263, from "(b)"): "(b) For n = n₁n₂ with c(n) tiny and c(n₁)c(n₂) not, Π(n) < 0 at first order; a"
NEW: "(b) HEURISTIC (not a proof — the higher-order terms of log* are not controlled): for n = n₁n₂ with c(n) tiny and c(n₁)c(n₂) not, the second-order term of Π(n) is negative; a"
OLD (265): "most polynomially along the multiplicative structure — hence (k̂ = k) k cannot be smooth — AND vanish on Z_j, AND rise gradually"
NEW: "most polynomially along the multiplicative structure (heuristic; for the Gaussian the probe confirms failure) — so smooth k are suspect but not excluded — AND vanish on Z_j, AND rise gradually"
OLD (270): "only in an infinite-dimensional, non-smooth class — named in §0.4 as part of the residue."
NEW: "in self-dual weights vanishing on Z_j (smooth ones exist by KNS Lemma 6; whether a non-negative one with the Euler property exists is open) — named in §0.4 as part of the residue."

Total FIX-FIRST pairs: 6 items (F1–F6).

## §5. Minor pairs (precision; no change to what is true)

m1 — (W1) is computed for d ≤ 60; "exactly" (all d) needs a tail bound, now supplied (§7 A1).
OLD (171): " (W1) weighted Beurling over F₅ ⟺ t ∈ [−5, 6] exactly (the lower end is b₂(−5) = 0; t = 6 is the empty system Z ≡ 1). Weights add"
NEW: " (W1) weighted Beurling over F₅ ⟺ t ∈ [−5, 6] exactly (computed for d ≤ 60; all d by read-O §7 A1: on (2√5, 6], N_e = (α^e − 1)(β^e − 1) and N_d/N_e ≥ 5^{d−e}; on [−5, 2√5], |α|, |β| ≤ (5 + √5)/2; the lower end is b₂(−5) = 0; t = 6 is the empty system Z ≡ 1). Weights add"
m2 — P2 proves non-uniqueness for (f, f̂), not for an even self-dual k; the fix is short (§7 A3).
OLD (252–253): "is a NON-uniqueness pair for S. Z_j is uniformly discrete, so (Z_j, Z_j) is subcritical for every p > 1: there are f ∈ S∖{0} with f|_{Z_j} = f̂|_{Z_j} = 0. The zero conditions alone therefore do not force k = 0; positivity (k ≥ 0, double zeros) and the Euler"
NEW: "is a NON-uniqueness pair for S. Z_j is uniformly discrete, so (Z_j, Z_j) is subcritical for every p > 1: there are f ∈ S∖{0} with f|_{Z_j} = f̂|_{Z_j} = 0; by KNS Lemma 6 (free interpolation on a symmetric Λ′ ⊋ Z_j with infinitely many extra nodes, their Claim 7) one may also make the eigenvalue-1 projection (f + f̂ + f(−·) + f̂(−·))/4 non-zero at an extra node, which gives a real, even k ≢ 0 with k̂ = k and k|_{Z_j} = 0 (read-O §7 A3). The zero conditions alone therefore do not force k = 0; positivity (k ≥ 0, double zeros) and the Euler"
m3 — Rosenthal is the one input of Lemma M taken on trust from Meyer's proof.
OLD (89, from "([7]"): "([7] = Rosenthal, Thèse, Memoirs AMS; OCR"
NEW: "([7] = Rosenthal, Thèse, Memoirs AMS = H. P. Rosenthal, Mem. AMS 63 (1966), Th. 1.6 p. 22 — not on disk; OCR"
m4 — notation.
OLD (203, phrase): "dividing Λ_F = q^{s/2}ξ(s)D(s) by ξ(s) = ξ(1 − s)"
NEW: "dividing Λ_F = q^{s/2}ξ(s)D(s), ξ(s) := π^{−s/2}Γ(s/2)ζ(s) (poles at 0 and 1), by ξ(s) = ξ(1 − s)"
m5 — the Landau step is proved on disk; drop the recalled label.
OLD (212–213, phrase): "(3) Landau–Widder (a Laplace–Stieltjes transform of a positive measure is singular at the real point of its abscissa σ_a; no local finiteness is needed):"
NEW: "(3) Landau's theorem for Laplace–Stieltjes transforms of positive measures (QC Lemma L, whose proof — Taylor at σ_a + 1 with nonnegative terms, then Tonelli — never uses local finiteness):"
OLD (370, first sentence): "(e) L‴. Landau–Widder for Laplace–Stieltjes transforms of positive measures needs no local finiteness `[recalled, standard]`."
NEW: "(e) L‴. Landau's theorem for Laplace–Stieltjes transforms of positive measures needs no local finiteness (QC Lemma L's proof applies verbatim; re-derived in read-O §1(i))."
m6 — BSS row: their Thm 7.5 (gapped eigenmeasures) is relevant context.
OLD (347, middle cell): "classification of doubly sparse measures OPEN"
NEW: "classification of doubly sparse measures OPEN (§8 Outlook, line 1236); Thm 7.5 (1160–1172) builds doubly sparse eigenmeasures with large gaps around 0 — signed, so outside Q_cond"
m7 — LO row: flag the over-attribution, as §1.1 already does.
OLD (344, phrase): "finitely many values [17 p. 25], [6], [11], via Helson–Cohen idempotents"
NEW: "finitely many values [17 p. 25], [6], [11], via Helson–Cohen idempotents (LO's "[17 p. 25]" is broader than the page, which treats unit masses — §1.1)"
m8 — the probe's READING over-interprets: at every optimum about half the atoms in [1, 64] are negative, the total negative mass grows
(4.51, 27.30, 62.82, 61.30 for M = 2, 3, 4, 5) and min/mean|Π_F| worsens (2.25, 2.60, 5.53, 10.10); the M = 4 optimum falls to −0.58
at x = 120 and −1.13 at x = 225. The rising max-min is dilution over more monoid points, not approach to positivity.
OLD (334–335): "READING. Adding atoms with new primes raises the best attainable minimum (q = 4: −0.68 → −0.40 → −0.31), as the Landau picture predicts (more Euler factors visible on the multiplier's monoid); the probe cannot reach the thick limit and decides nothing about 𝒯."
NEW: "READING. Adding atoms with new primes raises the best attainable minimum (q = 4: −0.68 → −0.40 → ≥ −0.29 → ≥ −0.22), but about half the atoms stay negative at every optimum, the total negative mass grows and min/mean|Π_F| worsens (2.3 → 10.1, read-O §2(d)): the rise is dilution over more monoid points, not evidence for the Landau picture; the probe cannot reach the thick limit and decides nothing about 𝒯."
m9 — citation drift: the NOTE's QC line numbers refer to 445cfe96…, which is now `qcond-s38/NOTE.pre-reader.md`; the live QC NOTE is
579f22e3… (471 lines) and its line numbers differ.
OLD (5, phrase): "Conventions (as in `qcond-s38/NOTE.md`, cited "QC","
NEW: "Conventions (as in `qcond-s38/NOTE.md` at SHA-256 445cfe96… — now saved as `qcond-s38/NOTE.pre-reader.md`; QC line numbers below refer to that file; the live QC NOTE is 579f22e3… — cited "QC","
m10 — the STOP-LINE sentence inherits F6's overclaim.
OLD (73, after the quote): "— met in the form of §7.1: every parametrizable family is excluded by a theorem or an exact finite computation."
NEW: "— met in the form of §7.1 for every family listed there (each excluded by a theorem or an exact finite computation); not for model-set families with smooth self-dual weights vanishing on Z_j (F6)."

Total minor pairs: 10 (m1–m10). TOTAL PAIRS: 16 (F1–F6, m1–m10).

## §6. Novelty per result

| result | verdict | page |
|---|---|---|
| Lemma M (finitely many values, via Meyer's Bohr passage + Lagrange) | NOT NEW: same proof in QC read-O §2 (earlier, same session); the finitely-valued case is attributed in print to Córdoba 1989 [LO's 6] and Kolountzakis–Lagarias, Duke [LO's 11] (LO 2015 lines 63–68, refs 785, 795) — bodies not on disk, so the attribution is unverified at the page | Meyer p. 25; LO 63–68 |
| Cor. M1 | NOT NEW (QC read-O §2(iv)); correct only with "μ̂ purely atomic" (F4) | — |
| Theorem D unconditional | NOT NEW to the program: QC read-O §2 RULING (05:20), QC-now Theorem D | QC-now step (1) |
| THEOREM G1 (finite generalized Dirac combs, any weights) | NEW as a statement (not found in print; Beurling + FE literature: Hilberdink–Lapidus "difficult", BSS §8 open); the new step (Step 3, Poisson for modulated combs vs finitely many Q-lines) uses standard tools; Steps 1, 2, 4 are QC's. Re-derived here ✓ → dual-checked | — |
| Cor. G1′ | NEW as a statement on printed + QC cores (Lemma M is old; G1 is the new input) | — |
| Lemma A, Proposition S | NEW as statements (single-check → re-derived ✓); tools standard (Banach-algebra log, Wiener's lemma, Bohr–Parseval) | — |
| THEOREM L‴ (both forms) | NEW in its infinite-atom / real-frequency / continuous-part statement; the finite-S mechanism is in print for integer divisor-supported multipliers (Hilberdink 2012 Thm 4.3, F2) and in QC L′ for finite real-frequency multipliers | Hilberdink 812–905 |
| (W1) weighted rung 1 = convex hull [−5, 6] | NEW (small computation + §7 A1 tail proof) | — |
| (W3) Q-side positivity empty at rung 1 | IN PRINT as a conclusion (Hilberdink 2012 Thm 4.4, k = 2); new only in that n ≤ 4 suffices | Hilberdink 1028–1066 |
| P1 | trivial (one line), new as applied | — |
| P2 | IN PRINT as applied (KNS 2023 Thm 1(ii)), plus a short eigen-projection step needed for k̂ = k (§7 A3) | KNS 137–139, 2000–2016 |
| Route (iii) zeta-zero repair (exact FE family; G_c has the FE alone) | NEW as an observation (single-check → re-derived ✓) | — |
| class 𝒯 and its one-condition reduction | NEW as a named class (a definition plus a reduction, ✓) | — |

## §7. Additions (single-check unless stated)

A1 — (W1) for ALL d (closes m1). L = (1 − αu)(1 − βu), αβ = 5, N_e = 1 + 5^e − α^e − β^e = (1 − α^e)(1 − β^e), d·b_d = Σ_{e∣d}μ(d/e)N_e ≥
N_d − Σ_{e∣d, e<d}|N_e|. (i) t ∈ (2√5, 6]: α ∈ (√5, 5], β = 5/α ∈ [1, √5), so N_e = (α^e − 1)(β^e − 1) ≥ 0, and (x^d − 1)/(x^e − 1) ≥ x^{d−e}
for x ≥ 1 gives N_d/N_e ≥ (αβ)^{d−e} = 5^{d−e} ≥ 5^{d/2} for e ≤ d/2; hence d·b_d ≥ N_d(1 − τ(d)5^{−d/2}) ≥ 0 for every d ≥ 2 (τ(d) <
5^{d/2}), with no computation. (ii) t ∈ [−5, 2√5]: max(|α|, |β|) ≤ R := (5 + √5)/2 = 3.618…, so d·b_d ≥ 5^d + 1 − 2R^d −
Σ_{e≤d/2}(1 + 5^e + 2R^e) > 0 for all d ≥ 61 (already 5^61(1 − 2·0.7236^61) ≫ (5/4)5^{30.5} + 31 + 3R^{31.5}); d ≤ 60 is the exact
computation (§2(a)). So weighted admissibility over F₅ is EXACTLY t ∈ [−5, 6].
A2 — what the Landau step still gives at σ_S ≥ ½ (sharpening §4's "stops at σ_S = ½"). For F = ζ·D_m Beurling with (A) at q (m ≥ 0
bounded-range or as in Prop. S), §4 steps (2)–(3) give D_a ≠ 0 on Re s > σ*, and the FE gives D_a ≠ 0 on Re s < 1 − σ*. So: if σ_S = ½
EXACTLY, every zero of D_a lies on Re s = ½; if σ_S ∈ (½, 1], the zeros lie in 1 − σ_S ≤ Re s ≤ σ_S. In addition, when F is Beurling
the Mertens inequality F(σ)³|F(σ + it)|⁴|F(σ + 2it)| ≥ 1 (σ > 1; from Π_F ≥ 0 and 3 + 4cosθ + cos2θ ≥ 0) forces D(1 + it) ≠ 0 for
t ≠ 0 (a zero would make the left side O((σ − 1)^{−3}·(σ − 1)^4) → 0). So a member of 𝒯 satisfying Π ≥ 0 has D zero-free on
Re s ≥ 1 and Re s ≤ 0, all zeros strictly inside the critical strip, and on the line if σ_S = ½ — a necessary condition a construction
must meet (D is entire of exponential type log q with ~(log q/2π)T zeros up to height T).
A3 — P2 for even self-dual k (closes m2). KNS Claim 7 (lines 1915–1930) gives a p-smooth Γ′ ⊃ Γ with |Γ′∖Γ| = ∞ on each half-line;
take p = q = 2, Λ′ = M′ symmetric with Λ′ ⊋ Z_j. KNS Lemma 6 (lines 2003–2016): for every fast-decaying (α, β) on (Λ′_L, M′_L) there is
f ∈ S(2, 2) with f = α on Λ′_L, f̂ = β on M′_L. Prescribe 0 on Z_j ∖ [−L, L] and free values at N symmetric extra nodes ±e_i; the K
finitely many conditions f = f̂ = 0 on Z_j ∩ [−L, L] leave a family of dimension ≥ 2N − K; the map to (P₁f(e_i))_i, P₁ := (I + F + F² + F³)/4,
has a kernel of dimension ≥ 2N − K − N, so for N > K some member has P₁f ≠ 0. P₁f is even, P₁f^ = P₁f, vanishes on Z_j (Z_j = −Z_j);
Re P₁f or Im P₁f is a real such k. Hence route (ii)'s zero conditions alone never force k = 0, also for k̂ = k.
A4 — Hilberdink 2012 Prop. 3.4 as a certificate (F2). Any F = ζ·D with D = Σ_{b∈B}m_b b^{−s}, B ⊂ Q ∩ [1, ∞) FINITE, m ≥ 0, m₁ = 1
and some b ∉ N is not a weighted Beurling system — no FE, no J-symmetry needed: N(x) = Σm_b⌊x/b⌋ ∈ T, N(x) − D(1)x has period
lcm(numerators of B), and Prop. 3.4 forces every jump (in particular at each b) to be an integer. So every design in the NOTE's
probe (and in mine) is excluded by print for a structural reason, and only infinitely many rational atoms (limit-periodic
N − D(1)x, outside Hilberdink's argument, whose Props. 3.2–3.4 use the finiteness of the jump set mod P) can escape it. Suggested
UT line: "a limit-periodic Hilberdink Prop. 3.4" would close the rational part of 𝒯.
A5 — the probe, completed (`verify-O/o4b–o4f`). q = 4, window [1, 64], the NOTE's design:
      M:          2          3          4           5           (6: see §8)
      max-min:  −0.680076  −0.400711  ≥ −0.293651  ≥ −0.218541
      |G≤64|:     51        408        2547        6196
      negative atoms at the optimum: 23, 204, 1277, 3072 (≈ half); total negative mass 4.51, 27.30, 62.82, 61.30;
      min/mean|Π_F|: 2.25, 2.60, 5.53, 10.10.
    The M = 4 optimum evaluated beyond its window: min Π_F = −0.579 on [1, 128] (x = 120), −1.129 on [1, 256] (x = 225). NO design
    reached min Π_F ≥ 0 even on [1, 64]; and none could be a member of 𝒯 (finite, hence excluded by L′ and, being rational with a
    non-integer atom, by Hilberdink Prop. 3.4 — A4). No Q-side twin: nothing to report under the brief's stop line (i).
A6 — G1 control (`verify-O/o2`): an explicit positive, self-dual, gapped (q ≥ 5.83) finite generalized Dirac comb with an irrational
    frequency and infinitely many mass values, μ_c = Σ(2 + 2cos2πθn)δ_n + δ_{θ+Z} + δ_{−θ+Z}, θ = √2 − 1 (self-dual to 1e−60). It lies in
    𝓜_r and is not Beurling exactly because its support is in no finite union of Q-lines (G1 Step 1). So G1's Step 3 is not vacuous,
    and the class G1 excludes is strictly larger than the constant-weight combs of Theorem D.

## §8. What I could not check, and why

- Rosenthal, Mem. AMS 63 (1966), Th. 1.6 p. 22 — the one input of Lemma M (and of Meyer p. 25) not on disk; not fetched (pre-arXiv
  memoir). Lemma M, M1, G1′ and Theorem D (via either route) rest on it through Meyer's printed proof.
- Saias–Weingartner's Thm 1/Thm 4 and QC's Lemma S–W′ (an extension of a printed proof, single-check in QC) were not re-derived here;
  G1 Step 4 and Theorem D use them exactly as QC §2.7 does. BFE Theorem T (dual-checked in its own unit) was not re-derived.
- Córdoba 1989 (body paywalled; landing page only) and Kolountzakis–Lagarias (Duke; not on arXiv by my query q10) — the printed
  finitely-valued case LO attributes to them is unverified at the page; Lemma M's novelty verdict does not depend on it (QC read-O §2).
- Hilberdink 2012 Props. 3.2–3.4 and Thm C: statements and hypotheses read at the page (outer systems, N ∈ T, periodic N − cx);
  proofs read but not re-derived line by line — A4 and the F2 row are (Q) at the page.
- Global optimality of the probe values for M ≥ 3: differential evolution + SLSQP is a heuristic global search (M = 2 is a 2-D problem
  where it agrees with the unit's 201² grid). The values are ACHIEVED (lower bounds for the max-min), certified at M = 4 by exact
  rational re-evaluation.
- arXiv: queries q7–q11 (`verify-O/sources/`) found no theorem closing the weighted corner (hits: Burnol 1106.4749, extensions of
  Hamburger for ordinary Dirichlet series; Nakamura 2008.02570, the f(s, χ) already in digest B5; Alfes–Kiefer–Mazáč 2405.15620,
  spherical eigenmeasures; BSS 2104.06812). An early batch was lost to an http → https redirect (empty files), then re-run.
