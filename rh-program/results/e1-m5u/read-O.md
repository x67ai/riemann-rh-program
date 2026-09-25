# E1 (M5-U formulation slot) — the Opus read (reader, Opus 5; standing orders 5 and 7)

Started Sat Sep 26 02:05:57 IST 2026 (machine clock, `date`). Inputs recomputed at start:
BRIEF.md SHA-256 52dc54209dcc15fbb8b494956d7e4c20857957c90873588367cff8b3651dcc4e (matches the launch line);
FORMULATION.md SHA-256 7d7d00726e20c6876a44d5540d055614159e0041a4320056f2a559b245e40343 (matches);
SHARED.md at start 5d5b2d79d2364a9de212fa1305d09fbbfa204c142075743f40bc865e622d076c.

## §P — the reader's own prior-art pass (written BEFORE opening FORMULATION.md §1; stamped Sat Sep 26 02:08 IST 2026)

Queries run (web search, Sep 26 2026): "positive measure spectral gap uncertainty principle integer point masses";
"uniqueness positive measure determined by Fourier transform on an interval Krein extension indeterminate";
"Poltoratski gap problem … Mitkovski … Beurling–Malliavin"; "integer-valued measure spectral gap … integer masses";
"Kurasov Sarnak crystalline measures positive integer masses Lev Olevskii"; "Weil explicit formula zeros uniquely
determined by primes below X … non-uniqueness"; "spectral gap … integer weights point masses uniqueness".
Opened and saved under `sources-O/` (PDF + pdftotext; SHA-256 in `verify-O/hashes-O.txt`):

- **P1. Mitkovski–Poltoratski, "Determinacy for measures"** (`sources-O/mitkovski-poltoratski-determinacy.pdf`, author
  copy, 6 pp. as served; Proc. AMS 2013 per the authors' page `[recalled, unverified]` for the journal line). Printed p. 1:
  definition — a positive FINITE measure µ is *a-determinate* if no other positive finite ν has ν̂ = µ̂ on [−a, a];
  "this definition does not depend on the interval [−a, a], but only on its length". **Theorem 1.2** (p. 1, "in essence,
  goes back to M. Riesz"): µ is a-determinate iff ∫ log m^µ_{a/2}(x)/(1+x²) dx = ∞, m the point-evaluation extremal over
  span{e^{ixt}: |t| ≤ a/2} in L²(µ). **Corollary 1.3** (p. 2): a signed measure whose POSITIVE part lives on a set with long
  complement has no spectral gap — "we don't require anything about the support of the negative part". p. 2: "Clearly,
  every a-indeterminate measure is a positive part of a signed measure σ with a spectral gap (−a, a) … Conversely, every
  non-zero measure σ with a spectral gap (−a, a) gives a rise to two a-indeterminate measures σ₊ and σ₋." **Theorem 1.5**
  (p. 2): Det(X) = G(X) for every closed X. **Theorem 1.6** (p. 3): for disjoint closed A, B, the largest gap of a finite
  signed σ with supp σ₊ ⊂ A, supp σ₋ ⊂ B equals π·sup{d : a d-uniform sequence alternates between A and B}.
  For M5-U: this is EXACTLY the real-weighted positive relaxation of M5-U ("is ν_ζ determined among positive measures by its
  transform on (−L, L)?") — but for FINITE measures; ν_ζ is infinite (log density). The p. 2 sentence is the printed form of
  the orchestrator's H1 corollary ("both parts of a gap measure are nonzero" is implicit in "gives rise to two
  a-indeterminate measures"). Integer weights: absent.
- **P2. Poltoratski, "Spectral gaps for sets and measures"**, arXiv:0908.2079v2 (`sources-O/poltoratski-0908.2079.pdf`,
  Acta Math. 208 (2012) 151–209 per Lev–Reti's bibliography). p. 3 (2.1): G_X over FINITE complex measures on X, gap
  [0, a] (any position — modulation invariance); **Proposition 1** (p. 3): G_µ = G_{supp µ}; **Theorem 2** (arXiv p. 10):
  G_X = 2πC_X. Positivity and integrality play no role; the gap is not required to contain 0.
- **P3. Lev–Reti, "Crystalline temperate distributions with uniformly discrete support and spectrum"**, arXiv:2101.04092
  (`sources-O/crystalline-temperate-2101.04092.pdf`). §3 p. 3: "There is a well-known principle stating that if a set Γ ⊂ R
  supports a nonzero measure, or a distribution, with a spectral gap, then Γ cannot be 'too sparse'", citing
  Kahane–Mandelbrojt 1958 Prop. 7 (Ann. ENS 75, 57–80 — "Sur l'équation fonctionnelle de Riemann et la formule sommatoire de
  Poisson": NOT opened), Mitkovski–Poltoratski, Poltoratski, Lev–Olevskii 2015 §4. **Theorem 3.1** (p. 4): a nonzero
  γ = Σ c_p(λ)δ_λ^{(p)} with Σ|c_p(λ)| < ∞ and a gap of length a has D(Γ) ≥ a/(k+1), D the logarithmic-averaged density.
  For ζ's ordinate set D = ∞: no constraint. p. 11 §6.2: positivity forces lattice structure in the CRYSTALLINE
  (discrete-spectrum) problem [LO15] — a spectrum statement, not a gap statement.
- **P4. Limani, "The uncertainty principle in harmonic analysis" (lecture notes), arXiv:2604.24900**
  (`sources-O/uncertainty-lecture-notes-2604.24900.pdf`): scanned by grep only (circle/lacunary setting; F. and M. Riesz,
  Zygmund, Pollard); no statement on positive or integer-atomic measures with a gap on R. Skimmed, not load-bearing.
- **Not opened (search hits only)**: Kurasov–Sarnak 2020 (positive crystalline measures from stable polynomials — discrete
  spectrum, not gaps); Olevskii–Ulanovskii "Fourier quasicrystals with unit masses" (C. R. Math. 2020: integer-mass
  Fourier quasicrystals ↔ zero sets of exponential polynomials with real zeros — again a discrete-SPECTRUM hypothesis);
  Eremenko–Novikov PNAS 2004 (sign changes of functions with a spectral gap); arXiv:2209.00318 (Krein's uniqueness criteria
  for positive symmetric operators); Kulikov–Nazarov–Sodin arXiv:2306.14013 (Fourier uniqueness pairs). All
  `[search hit, not opened]`, none load-bearing.

**Elementary facts re-derived here (not citations).** (i) *A positive tempered measure µ ≠ 0 has no spectral gap
containing 0.* With ψ ∈ C_c^∞(−L/2, L/2), ψ ≠ 0, and φ = ψ ⋆ ψ̃, ⟨µ̂, φ⟩ = ∫|ψ̂|² dµ; modulating ψ by e^{iγ₀u} keeps its
support and translates ψ̂, so ∫|ψ̂(γ − γ₀)|² dµ(γ) = 0 for every γ₀ forces µ(U + γ₀) = 0 for the open set U = {ψ̂ ≠ 0}, hence
µ = 0. (Bochner's positive-definiteness; the gap must CONTAIN 0 — P2's gaps [0, a] need not.) (ii) *In the real-weighted
positive relaxation, determinacy fails whenever the support set X of ν carries a finite real measure with gap (−L, L) and
ν's atoms are bounded below*: if m is such a measure, ν + t·m ≥ 0 for |t| ≤ (inf atom of ν)/sup|m({x})|, and ν + t·m has
ν's transform on (−L, L). This is P1's "σ₊, σ₋ are indeterminate" run in reverse, and it needs G_X > 2L only (P2's
Theorem 2 via C_X), not finiteness of ν.

**§P verdict.** (a) *Found in print:* the real-weighted determinacy problem for positive FINITE measures (P1 Thm 1.2, 1.5,
1.6) and the gap characteristic of sets (P2); the "positive measures have no gap at 0 / both parts of a gap measure are
nonzero" principle is printed only implicitly (P1 p. 2). (b) *Not found:* any uniqueness or non-uniqueness theorem for
positive INTEGER-atomic (or integer-weighted) measures with a spectral gap, finite or infinite; any gap theorem that uses
integrality. The integer-mass literature found (Kurasov–Sarnak, Olevskii–Ulanovskii, Lev–Olevskii, Lev–Reti) is about
discrete SPECTRA (crystalline measures), not gaps. (c) Consequence for the slot: stop line (i) does NOT fire from this
search; the real-weighted relaxation is expected to be indeterminate for ζ (fact (ii) with G_X = ∞), so any YES for M5-U
must use integrality — the reader will check whether FORMULATION reaches the same conclusion and cites P1/P2 or an
equivalent. Novelty of "an uncertainty principle for positive integer-atomic measures of logarithmic density" is
supported by this search at the level of a short pass (seven queries, four papers opened; not exhaustive; Koosis and Havin–Jöricke not on disk).

---

## Verdict table (FORMULATION.md 7d7d0072…; rows as the launch line orders them)

| Row | Object | Verdict | Amendments |
|---|---|---|---|
| 1 | §1 sources at the page | **FIX-FIRST** (every page citation the launch line names confirmed at the page, with five transcription/record errors and one missing source) | A1–A7 |
| 2a | §2.1 clause 1, identity (2.2), strip positivity | **CLOSES** (re-derived; re-run independently, `verify-O/h1_strip_reader_run.log`) | A8 (label only) |
| 2b | §2.2 clause 2, balance (2.3) | **FIX-FIRST** (one hypothesis missing: ε ≤ 1) | A9 |
| 2c | §2.3(b) Krein indeterminacy at every bandwidth (the load-bearing theorem) | **CLOSES** — the theorem holds exactly (not refuted); its mechanism is printed for finite measures | A10 (source + label) |
| 2d | §2.4 soft-windowed datum indeterminate at all but countably many heights | **CLOSES** | — |
| 2e | §2.5–§2.6 clauses 5–7, dependency chain, H2 | **CLOSES with two precisions** | A11, A12 |
| 3a | §3.1 rung-1 exact pair (rehearsal) | **CLOSES** (re-run and independently re-counted, `verify-O/rung1_pair_check_run.log`) | — |
| 3b | §3.3(a) datum equality via Yoshida (1.6) | **CLOSES** (at the page) | — |
| 3c | §3.3(b)–(d) the LMFDB pair, p₀ = 19, free-stratum precision | **FIX-FIRST** on the LMFDB transcription (class number of .1; the row "23, 29, 31, 37 … differ"); the mathematics CLOSES (p₀ = 19 confirmed three ways; 0.0233 / 0.0087 recomputed) | A13, A14, A15 |
| 3d | §3.4–§3.5 ζ has no partner; what the control says | **CLOSES** | A16 (Bombieri's own framing) |
| 4 | §4 the positivity step and the DECISION | **CLOSES — STOP at (iii) stands.** One candidate was OMITTED (not dismissed): the Mitkovski–Poltoratski determinacy/oscillation theory; it fails at its first obstacle too | A17 |
| 5 | §5 E7 and the proposed §4.2 correction | **CLOSES** — §5.1 step (2) re-derived (mean-zero tests ⟺ Krein–Langer's kernel definition), step (3) at the page; the §5.2 paragraph is exact at its records | — |
| 6 | §6 zoo protocol and the II.1 rider | **FIX-FIRST** (four word-level corrections in the rider) | A19–A22 |
| 7 | §7 close (verdict table, three shapes, 10(m), 10(o)) | **CLOSES with the consequential edit to §7.3's record corrections** | A23 |
| 8 | §8 C2 lines | **FIX-FIRST** (orbit-sum factor in the Instruments row; MP reference in the first Untried line) | A24, A25 |
| 9 | labels (§9 and the four `[novelty: single-check]` tags) | **FIX-FIRST** row by row, below | A26–A28 |

No row is FATAL. Amendments: **27 (numbered A1–A28; A18 unused), of which 3 change mathematics** (A9: clause 2's range of ε; A12: the comb's sign wording; A17: a seventh candidate added to §4), **7 correct a transcription at the page** (A1, A2, A3, A5, A13, A14, A23), **4 add or re-route a source** (A4, A6, A7, A10), and the rest are precision/label edits. None changes the DECISION.

---

## Per-row checks

### Row 1 — §1, every page the launch line names, opened by the reader (Read tool, page images)

- **Yoshida 1992** (`fetched/p3-23-…`; PDF p. n = printed p. 280 + n — confirmed). **p. 284 (PDF 4):** eq. (1.6) exactly as the writer transcribes it: "= ∫F(x)(e^{x/2} + e^{−x/2})dx + (log A_k)F(0) − Σ_𝔭Σ_m (log N(𝔭))/N(𝔭)^{m/2}(F(m log N(𝔭)) + F(−m log N(𝔭))) + r₁V₁(F) + 2r₂V₂(F)", A_k = π^{−r₁}(2π)^{−2r₂}|D_k|; (1.4)–(1.5) V₁, V₂ as quoted. **p. 285 (PDF 5):** Proposition 1 (1)–(2) verbatim. **p. 310 (PDF 30), rendered:** Theorem 1 reads "Let a = log 2/2. We have ⟨φ, φ⟩ = T_ℚ(φ ∗ φ̃) ≥ 0 for every φ ∈ K(a), where equality holds if and only if φ = 0" — **the "displayed lower bound" is 0** (A1). **pp. 321–322 (PDF 41–42):** Theorem 2 and its proof; p. 322 lines 1–7: "This shows that Φ(s) is an entire function of order ≤ 1, exponential type a (cf. Boas [1], p. 8). Let n(r) be the number of zeros of Φ(s) in the disk |s| ≤ r counted with multiplicity. Then we have n(r) = O(r) if Φ ≠ 0 … Let N(r) be the number of distinct zeros of ζ_k(s) in |s| ≤ r. It is known that N(r) ≠ O(r) (cf. Siegel [6], Satz 2). This is a contradiction if Φ ≠ 0." — CONFIRMED; it is an argument inside a proof, not a numbered statement (the writer's "printed" is fair; the label `[read at the page: Yoshida 1992 p. 322]` is right). **Proposition 7, pp. 322–324 (PDF 42–44):** statement, (8.3), the continuity of V₁ ∗ φ off ±a via (8.4), (8.5), the forced relation (8.6) e₁log p₁ − e₂log p₂ = 2a and (8.7), the case analysis a ≤ (log 5)/2, and the iteration giving φ ∈ C(a) then V₀ = {0} via Proposition 2 — CONFIRMED as summarized. The writer's reading "a unique-continuation statement for the datum side … atomic prime side against a continuous archimedean side" is accurate.
- **Suzuki JLMS 2023 = arXiv:2206.03682v4** (`fetched/w-01-…`; arXiv pages). **p. 1:** (1.1), "Formula (1.1) shows that Ψ(t) is real-valued and continuous on [0, ∞) and that Ψ(0) = 0", Theorem 1.1 (1)–(2). **p. 2:** G_a, kernel (1.4)–(1.5), the Krein–Langer Satz 5.9 sentence, (1.8) g := −Ψ. **p. 10:** (3.3) W(φ) := Σ_γφ̂(γ); **Proposition 3.1: "⟨Dψ₁, Dψ₂⟩_{G_g,a} = W(ψ₁ ∗ ψ̃₂) for every ψ₁, ψ₂ ∈ C(a)"**, C(a) = {φ ∈ C_c^∞ : supp ⊂ [−a, a]} (3.6), D, I₀^{(a)} inverse bijections (3.7). **p. 11, §3.5:** "−g″(t) = Ψ″(t) = Σ_γe^{iγt} = W(t) as a distribution … the Weil distribution W(t) can be regarded as an 'accelerant' of the screw function g(t)" — CONFIRMED verbatim. (Suzuki 2026 `y-09` pp. 3–5 and Suzuki 2022 `y-10` p. 1: spot-checked in the text layer — the Krein–Langer §5 sentence, Theorem 1.4, and the even screw representation are as quoted.)
- **Krein–Langer IEOT 78 (2014)** (`fetched-r2/r-02a-…`; PDF = printed). **p. 29:** Lemma 4.6 and the end of the proof of Theorem 4.4 ("if A is self-adjoint it has a unique u-resolvent and hence by Lemma 4.6 a unique continuation … If A has defect numbers n₊ = n₋ = 1 then there are infinitely many …") — CONFIRMED. **p. 30:** (4.16)–(4.17), orthogonal continuations, "If f ∈ P_a has more than one continuation in P_∞ then the support of the spectral measure of an orthogonal continuation is a discrete sequence of real points", Remark 4.8 (1)–(3) — CONFIRMED. **p. 33:** the example f_a = 1 − |t| (infinitely many continuations for 0 < a < 1, exactly one at a = 1); §5.1 G_a with kernel (5.1) g(t − s) − g(t) − conj g(s) + g(0) — CONFIRMED. **p. 34:** Theorem 5.1 (5.2)–(5.3), Corollary 5.2 — CONFIRMED verbatim. **p. 40:** §6.1 and **Theorem 6.1 — with the boundary point defined as a_f := ∫₀^∞ √(det H_f(ξ)) dξ** (the writer drops the square root, A2); case (2) carries the proviso "∫₀^ℓ √(det H_f(ξ))dξ < a_f for each ℓ < ∞" (the writer's paraphrase merges (2) and (3); harmless). **p. 41:** Krein's log-integral sentence verbatim; §6.2 "analogous statements to Theorem 6.1 remain true" for g ∈ G_∞ — CONFIRMED. Also noticed at p. 30: **Proposition 4.9** (in the non-unique case every continuation's spectral measure meets every gap between adjacent support points of an orthogonal one) — not used by the writer; recorded for any later integrality unit (it is the only printed statement in the paper about where the atoms of continuations can sit).
- **Bombieri 2000** (`fetched-r2/u-23a-…`; PDF p. n = printed p. 180 + n — confirmed). **p. 221 (PDF 41):** Theorem 10, statement as the writer quotes — CONFIRMED (the record's "p. 228" is wrong: p. 228 carries only numerical discussion and a plot). **p. 224 (PDF 44):** the Corollary after Theorem 11 — **but the writer's quotation inverts its last clause**: the page prints "at least half of its ℓ²-mass is supported on the set of zeros ρ with ℜ(ρ) ≠ ½", not "= ½" (A3). The sentence immediately before "An Example" reads **"One may ask if linear dependence relations occur at all. The following example shows that they may occur for Dedekind zeta functions."** — the writer does not quote it (A16). The Example text is as quoted. **p. 225 (PDF 45):** the dilation relation and **Bourgain's sentence verbatim**: "As pointed out by J. Bourgain, the existence of linear relations over intervals of arbitrary length also follows from the fact that the gap between consecutive γ's tends to 0 as γ → ∞." — CONFIRMED. **Record correction, refined (A5, A23):** the trichotomy that D1(b) §4.3 quotes — "(iii) a linear combination Σ_ρ c_ρ x^{−ρ}/(ρ(1 − ρ)) + A + Bx^{−1} with Σ|c_ρ|² = 1 vanishing identically for 1 ≤ x ≤ M₀" — is printed in the **Introduction, p. 185 (PDF 5)**, as "the following corollary of one of our theorems", followed by "More precise results of this type are contained in §10, Theorem 10 and §11, Theorem 11"; the Corollary at p. 224 is a different (E-interval, ℓ²) form. So the writer is right that "p. 228" is wrong, and not quite right that "the trichotomy is the Corollary at p. 224".
- **Poltoratski arXiv:0908.2079v2** — fetched by the reader (`sources-O/poltoratski-0908.2079.pdf`, 43 pp., SHA-256 378856e9…). p. 3 (2.1): G_X over finite Borel complex measures, gap [0, a]; Proposition 1 (p. 3); **Theorem 2 "G_X = 2πC_X" at arXiv p. 10** (text layer; the next page header is 11) — CONFIRMED; the finite-measure hypothesis is in (2.1). The writer's §1 item 8 "NOT re-fetched" is now superseded (A4).
- **Lapidus arXiv:1505.01548, printed p. 5 = PDF p. 5** (rendered): the sentence "… cannot have an infinite vertical arithmetic progression of zeros. (See [Lap-vFr3, Chapter 11] …) Unknown at the time to the authors of [Lap-vFr1] …, this latter result about the zeros in arithmetic progression, in the special case of ζ, was already obtained by Putnam in [Put1–2] by a completely different method" — CONFIRMED (SHA-256 of the writer's copy recomputed: 85e2e128… matches).
- **Kaczorowski–Perelli 1999** — the file is `fetched-r2/u-26a-…`, not `fetched/u-26a-…` (A6); PDF p. 4 (= p. 210) carries "restricts the functions F ∈ S₁ to either the Riemann zeta function or shifted Dirichlet L-functions" — CONFIRMED in the text layer.
- **Missing source (A7).** The writer's §1 has no entry for the one printed theory of exactly the real-weighted relaxation — Mitkovski–Poltoratski "Determinacy for measures" (§P, P1): a-determinacy of positive finite measures, the Riesz-type criterion (Theorem 1.2), Det(X) = G(X) (Theorem 1.5), and p. 2's "every non-zero measure σ with a spectral gap (−a, a) gives a rise to two a-indeterminate measures σ₊ and σ₋". It is the printed form of clause 3(b)'s mechanism for finite measures, and it bears on stop line (i) (see Row 2c).

### Row 2a — clause 1 and (2.2), re-derived

(2.2): ∫e^{iux}e^{±yu}sech(u/2)du = 2π·sech(π(x ∓ iy)) by analytic continuation of ∫e^{iuz}sech(u/2)du = 2π sech(πz) (|Im z| < ½), so ∫e^{iux}h_y = 2π·Re sech(π(x − iy)) and Re[1/cosh(πx − iπy)] = cosh(πx)cos(πy)/|cosh(π(x − iy))|² — the writer's P_y, positive for |y| < ½. The orbit sum of an even real g at {±x ± iy} is 4·Re ĝ(x + iy) = 4∫g(u)cos(xu)cosh(yu)du (ĝ(z̄) = conj ĝ(z), ĝ(−z) = ĝ(z)). With g = k·sech(u/2), Re ĝ(x + iy) = ∫k·h_y·cos(xu) = (2π)^{−1}(k̂ ∗ P_y)(x), k̂ = |ψ̂|² ≥ 0: strictly positive for |y| < ½; = |ψ̂(x)|² at |y| = ½. This is Schur's product theorem for positive-definite functions (k and h_y both PD), which is also the cleanest statement of the clause (A8). Strictness via dilates: CONFIRMED (for x ≠ 0 the entire ψ̂ would vanish on a segment). **Numerics, reader's own script** (`verify-O/h1_strip_reader.py`, 1.4 s): (2.2) agrees with quadrature to ≤ 2.4·10⁻¹⁰ at six points including y = 0.45 and x < 0; the sech family's minimum of Re ĝ over x ∈ [0, 40] is positive at y = 0, 0.25, 0.45, 0.49, 0.5 (smallest +9.5·10⁻¹⁴, at the |ψ̂|² tail at y = ½), while the plain family ψ⋆ψ is negative off the line (−1.0·10⁻⁴ at y = 0.25; −6.2·10⁻⁴ at y = ½, x = 6.60) — matching the writer's −6.0·10⁻⁴ at x = 6.5 to grid precision; the convolution form (2π)^{−1}(|ψ̂|² ∗ P_y) matches the direct integral to 8 digits at (3.0, 0.25) and (6.5, 0.45). CLOSES.

### Row 2b — clause 2 and the balance (2.3)

The proof is right line by line (the scaling ĝ_ε(z) = εĝ_ψ(εz); the near/far split; Σ_{|γ|>R}m_γγ^{−2} ≤ 2C_ζ(1 + log R)/R; the division by ε; "μ₋ finite ⟹ μ₊ finite ⟹ μ finite ⟹ μ = 0", where the last step is also elementary: a finite integer-atomic μ has finitely many atoms, so E_μ is real-analytic and cannot vanish on an interval unless μ = 0). **One hypothesis is missing:** the positivity of every left-hand term uses clause 1 at the point εγ, i.e. |Im εγ| ≤ ½, which the proof secures by "ε/2 ≤ ½" — so ε ≤ 1 is needed, while the statement allows every ε ∈ (0, L); for L > 1 and a ghost with off-line orbits in μ₊ the left side is not signed for ε ∈ (1, L). The consequences (d) use ε → 0 only and are unaffected. **A9.**

### Row 2c — §2.3(b), the load-bearing theorem: attempted refutation

I tried to break it at five places. (1) *G_X = ∞ for X = ζ's ordinates under RH:* record (dual-model) through Bombieri p. 225's printed sentence, now also confirmed at the page by me; an independent sketch: gaps → 0 lets one pick, for any d and all |n| ≥ n₀, points λ_n ∈ X within 1/(8d) of n/d; changing finitely many points keeps a sine-type-like generating function of type πd, and Lagrange-interpolation measures on such sequences with two points removed are finite with gap of length ≈ 2πd — `[recalled, unverified]` as to a page (Poltoratski's Theorem 2 is the printed route). Not refuted. (2) *Convention of the gap:* Poltoratski's transform is ∫e^{−izt}dµ with gap [0, a]; in the note's e^{+iux} convention the gap is [−a, 0], and the recentering modulation must be e^{−i(L+1)x} rather than e^{+i(L+1)x} — immaterial (reflect m₀ or flip the sign), no amendment. (3) *Real part, symmetrization, odd case:* (conj m)^(u) = conj m̂(−u) keeps a symmetric gap; the even part keeps it; in the odd case sin(δx)·m₂ is even, finite, nonzero for δ avoiding a countable set, with m̂(u) = (2i)^{−1}[m̂₂(u + δ) − m̂₂(u − δ)] = 0 for |u| ≤ L when δ ≤ 1 — CONFIRMED (an alternative: take m₀ supported on X ∩ (0, ∞), then m + m(−·) is nonzero automatically). (4) *Positivity:* each atom of ν_ζ is ≥ 1 and |m|({γ}) ≤ ‖m‖, so |t| ≤ 1/‖m‖ suffices — CONFIRMED. (5) *"Krein-indeterminate" exactly:* by §5.1 the relaxation ℛ_L(Λ) is the set of continuations of the screw function g = −Ψ from (−L, L) (b = L/2 in Krein–Langer's (−2b, 2b)); the double primitive of t·m̂ vanishes on (−L, L) because it is affine there, even, and 0 at 0. Two distinct continuations ⇒ non-unique ⇒ by Theorem 6.1/§6.2 (p. 40–41) the boundary point is +∞ (case (1) excluded, and cases (2)–(3) with a_g < ∞ give uniqueness for b > a_g). **The theorem holds exactly; the conclusion "F_Λ is Krein-indeterminate at every bandwidth (under RH)" follows.** *What it is:* a two-line corollary of printed facts — Bombieri p. 225 (gaps → 0), Poltoratski Theorem 2 (G_X = 2πC_X), and Mitkovski–Poltoratski p. 2 (a gap measure produces indeterminacy of a positive measure) — plus the elementary positivity margin of integer marks. My search (§P) did not find it printed FOR ζ's zero measure. So stop line (i) fires in the writer's sense ("non-uniqueness for positive tempered measures" as citation + derivation), with MP p. 2 as the citation it lacks. **A10.**

### Row 2d — §2.4

f_T = (2π)^{−1}(F_Λ ∗ ŵ_T) only reads F_Λ on (u − ε, u + ε) ⊂ (−L, L) for |u| ≤ L − ε (supp ŵ open in (−ε, ε)) — continuous, PD, of Krein–Langer class P_{(L−ε)/2}; the perturbation w_T(ν_ζ + t m) keeps it; w_T m ≠ 0 off a countable set of T. CONFIRMED. The rider's "at every height" must say "at all but countably many heights" (A21).

### Row 2e — clauses 5–7, dependency chain, H2

Dependency chain re-traced: clause 1 ← (2.2) + §0.1 bound; clause 2 ← 1 + F1(b) + RvM; 3(a) ← §5 (KL 5.1 + Suzuki 3.1, p. 11) + Yoshida Theorem 1; 3(b) ← G_X = ∞ + RH; 4 ← 3(b) + (0.5)-corrected + KL 4.4; 5 ← M2. No cycle; no hidden input beyond the RH hypothesis already declared for 3(b)–4. Two precisions: **A11** (Bombieri's relations are ℓ²-weighted, not finite measures, so "exactly such measures" is too strong); **A12** (the comb's sign: with μ = Σ_k(δ_{ks} − δ_{ks+s/2}) the NEGATIVE part {ks + s/2} is the one that must lie on ζ's zeros; the writer writes "positive atoms").

### Row 3a — rung 1

Writer's script re-run (1.17 s): output identical to `verify/rung1_ghost_pair_run.log` modulo timing. Independent re-count (`verify-O/rung1_pair_check.py`, direct point counts over F₇ and F₄₉ = F₇[i]; my first run counted y over F₄₉ for N₁ — a reader bug, fixed and logged): both quintics squarefree over F₇; N₁ = 1, 1; N₂ = 49, 51; P(t) = 1 − 7t + 24t² − 49t³ + 49t⁴ and 1 − 7t + 25t² − 49t³ + 49t⁴. The factorization (1 − 2t + 7t²)(1 − 5t + 7t²) and the irreducibility of the second (no integer b, b′ with b + b′ = −7 and bb′ = 11, nor with the other constant-term splittings of 49) re-checked by hand. CLOSES.

### Row 3b — §3.3(a), datum equality (the point the brief marked most likely to be wrong)

At Yoshida p. 284 the archimedean side of (1.6) is ∫F(x)(e^{x/2} + e^{−x/2})dx + (log A_k)F(0) + r₁V₁(F) + 2r₂V₂(F), A_k = π^{−r₁}(2π)^{−2r₂}|D_k| — a function of (r₁, r₂, |D_k|) only; the prime side is a sum over prime ideals with atoms at ±m log N𝔭, weight log N𝔭·N𝔭^{−m/2}, i.e. Λ_K(n)n^{−1/2} at n = N𝔭^m. For the pair: (r₁, r₂) = (3, 0), |D| = 7063225849 for both (LMFDB, opened by me); every prime ideal power of norm < 19 has the same data in both fields (all p < 19 inert, so the only norms < 19 are 8 = 2³ with log N𝔭 = 3 log 2, and none else below 19: 3³ = 27 > 19); the ramified primes 229, 367 lie above 19; the atoms at ±log 19 lie on the boundary of the OPEN band (−log 19, log 19). The pole term is the same (ζ | ζ_K). The class-level conclusion 𝒦_L(π_{K₁}) = 𝒦_L(π_{K₂}) for L ≤ log 19 follows, and both zero measures belong to it by (1.6). The distinctness argument (Hadamard: the ratio of completed functions is entire, zero-free, order ≤ 1, FE-symmetric, → 1) is right. **CLOSES.** One observation for the record: both ν_{K_i} contain ν_ζ (ζ_K = ζ·L(χ)·L(χ̄)), so μ = ν_{L(χ₂)} + ν_{L(χ̄₂)} − ν_{L(χ₁)} − ν_{L(χ̄₁)} — the ghost pair is a Dirichlet-L pair of Bombieri's kind, made positive by adding ζ and the conjugate character.

### Row 3c — §3.3(b)–(d), the LMFDB pair

Opened by me (`sources-O/lmfdb-nf-3.3.7063225849.{1,2}.html`, fetched 02:12 IST, SHA-256 in `verify-O/hashes-O.txt`): both degree 3, signature (3, 0), discriminant 7063225849 = 229²·367², conductor 84043 = 229·367, ramified primes 229, 367, Galois group C₃ (3T1), polynomials x³ − x² − 28014x + 703471 (.1) and x³ − x² − 28014x + 1711987 (.2). **Class numbers: 3 (.1, class group [3]) and 12 (.2, class group [2, 6]) — not "12 and 12"** (A13; the writer's own saved page for .1 carries the same data). Frobenius rows (p ≤ 59): identical (inert) at 2, 3, 5, 7, 11, 13, 17; **first difference at 19** (.1 split, .2 inert) — CONFIRMED; after that, 23, 31, 37, 41 differ and **29, 43, 47, 53, 59 agree** (both inert) — the writer's "the next primes 23, 29, 31, 37, … differ" is wrong at 29 (A14). Independent confirmation (`verify-O/rung3_check.py`): root counts of the two LMFDB polynomials mod p give the same table (p = 37 shows 2 roots for .2 because 37 divides that polynomial's index — the polynomial discriminant is d·37² — so the root count is not a splitting test there; LMFDB's 1³ stands); the character rule "same type ⟺ p is a cube mod 229 or mod 367" reproduces every row p < 60; the independent search over the 666 pairs q₁ < q₂ ≤ 400 gives the same top p₀ = 19 at (229, 367), then 13, 13, 11, … ; T(α ≥ ½) = 2π(19²/d)^{1/3} = 0.02332 and T(α ≥ 1) = 0.00874 — CONFIRMED. The writer's script re-run: identical output. The free-stratum precision is right as stated, including its hedge (a zero of L(s, χ_i) with |γ| < 0.023 is not excluded). **A15**: "by the count none of this construction can" overstates a heuristic (the size of the least prime that is a non-cube modulo both q₁ and q₂ is bounded by a power of f unconditionally, and by (log f)² under GRH `[recalled, unverified]`) — it should say "is expected to".

### Row 3d — §3.4–§3.5

KP p. 210 confirmed; the degree/conductor/pole argument that no other Selberg-class element has a configuration in 𝒦_L(Λ) is right (on (−log 2, log 2) the class sees only the archimedean kernel, whose fp-singularity fixes the degree, whose 2cosh(u/2) term fixes the pole at s = 1, and whose δ₀-coefficient fixes the conductor; degree 1 then leaves ζ(s + iθ), excluded by symmetry). **A16**: Bombieri himself frames his Example as showing linear relations "may occur for Dedekind zeta functions" (p. 224); the note should quote it, so that the rung-3 pair is recorded as the concrete positive-datum instance of Bombieri's own remark, not as a new construction.

### Row 4 — §4, the dismissals, adversarially; the DECISION

(a) REFUTED — agreed (Row 2c). (b) Hard-window Toeplitz — the first obstacle (the hard-window transform is not a functional of the band datum; the out-of-window part is an infinite integer-atomic measure of full order) is the right one; not dismissed too fast. (c) REFUTED as a determinacy route, RETAINED as the localized statement — agreed; the localized statement is correct as an implication. (d) Clause 7 — wrong object; agreed. (e) Crystalline measures — my §P confirms the characterization at the level of Lev–Reti §6.2 p. 11 (positivity forces lattice structure in the DISCRETE-SPECTRUM problem [LO15]) and search hits for Kurasov–Sarnak and Olevskii–Ulanovskii: the hypotheses are a discrete spectrum, not a gap; agreed. (f) The arithmetic shape — the first obstacle ("the ghost has ζ's prime side by definition, so the prime relations cancel") is exact; agreed. **Omitted, not dismissed — (g) the Mitkovski–Poltoratski determinacy/oscillation theory** (§P P1: Theorems 1.2, 1.5–1.7). *Mechanism:* the tapered difference w_T·μ is a FINITE signed measure with gap (−L + ε, L − ε) whose negative part lies on ζ's zeros; Theorem 1.6 then says its sign pattern must alternate along an (L − ε)/π-uniform sequence, the odd terms in B = ζ's ordinates — density (L − ε)/(2π) for the B-half, which ζ's ordinates can supply locally exactly where (1/2π)log(T/2π) ≥ (L − ε)/(2π), i.e. at α(T) ≤ 1 (up to ε): a gap-theoretic threshold that coincides with the count's α = 1 line. *First obstacle:* d-uniformity is a large-scale (Beurling–Malliavin-type) property and w_T has only discrete zeros, so supp(w_T μ) = supp μ and the alternation can be realized at heights far from T where the zeros are dense; the theorem gives no window statement, and no integrality enters. **Rejected at its first obstacle**; recorded because it is the only printed theory of the relaxation's exact question and because a LOCAL version of Theorem 1.6 would be precisely clause 6's input (III). **A17.** No other strategy is visible to me that survives its first obstacle. **The STOP at stop line (iii) stands**, and it stands on refutations and named obstacles, not on a null search (V.5).

### Row 5 — §5 E7 and the §4.2 correction

Step (1): Suzuki p. 11 at the page. Step (2), re-derived: for φ ∈ C_c^∞(−a, a), ψ := φ′ has mean 0 and (φ⋆φ̃)″ = −ψ⋆ψ̃, so ⟨−g″, φ⋆φ̃⟩ = ⟨g, ψ⋆ψ̃⟩ = ∫∫[g(t − s) − g(t) − g(−s) + g(0)]ψ(s)conj ψ(t) (the added terms integrate to 0); conversely every mean-zero ψ ∈ C_c^∞(−a, a) is φ′ with φ ∈ C_c^∞(−a, a). For point masses ρ = Σξ_iδ_{t_i} (|t_i| < a), ∫∫G_g dρ dρ̄ = ∫∫g(t − s)dρ₀(s)dρ̄₀(t) with ρ₀ = ρ − ρ(ℝ)δ₀ — expanded and checked term by term — and ρ₀ ∗ η_n (η_n a mollifier of small support) are smooth, mean-zero, supported in (−a, a), and converge in the pairing because g is continuous; the converse direction (point masses ⟹ continuous densities) is by Riemann sums. So (i) ⟺ g ∈ G_a exactly (Krein–Langer (5.1) p. 33; Suzuki (1.5) p. 2). Step (3): Theorem 5.1 at the page; −g″ = τ̂ follows by pairing (5.2) with φ″ (∫φ″ = ∫tφ″ = 0 kill the subtracted terms). **CLOSES.** The §5.2 correction paragraph is exact at its records: the D1(b) sentence it supersedes — "the theorem for distributions is `[recalled, unverified]` (I recall it as known and do not know the page)" — occurs verbatim at `results/c2-m5b/FORMULATION.md` line 253 (84e34569… recomputed), and (4.1) is D1(b) line 249. No amendment to §5.2 (its "boundary point a_g … is +∞" carries no formula, so A2 does not reach it).

### Row 6 — §6 zoo protocol and the rider

Items 1–7: agreed; IV.1's self-disclosure (clause 3(a) IS Weil positivity) is right; V.4's finding (clause 6's YES-shape fires on the controls unless it uses ζ's arithmetic) is right. The rider is exact at its records except: (1) the "orbit sums" are 4·(2π)⁻¹(|ψ̂|² ∗ P_y) for a four-point orbit — the displayed quantity is the real part per point (A19); (2) the indeterminacy theorem should cite its printed mechanism, Mitkovski–Poltoratski p. 2 (A20); (3) "every height" → "all but countably many heights" (A21); (4) Bombieri's Example is his own remark that relations "may occur for Dedekind zeta functions" (A22). With A19–A22 the rider earns `[dual-model check 2026-09-26]`.

### Row 7 — §7

H1–H5 verdicts: all five agreed (H1 CONFIRMED on the strip; H2 CONFIRMED as restated with (i)–(iii) decided; H3 CONFIRMED (a)–(d) — with A13–A16; H4 STOP; H5 CONFIRMED at the page). The three 10(c) shapes are correctly written. §7.3's record-correction sentence needs A23 (Bombieri p. 185). The 10(o) line is honest.

### Row 8 — §8 C2 lines

Instruments row 1: exact (with "for all but countably many T" already in it). Row 2: the orbit-sum factor (A24). Row 3: exact (class numbers are not in it). Untried line 1: add the MP pointer to the "real-weighted relaxation" clause (A25). Untried lines 2–3, work-log line, frontier sentence: exact.

---

## Amendments (EXACT OLD → NEW; FORMULATION.md unless stated; apply with the pre-reader copy kept)

**A1** (§1 item 1, Yoshida Theorem 1). OLD: `"Let a = log 2/2. We have (φ, φ) ≥ [a displayed lower bound] for every φ ∈ K(a), where equality holds if and only if φ = 0" (for k = ℚ; the displayed bound is garbled in the text layer and was not transcribed — the reader is asked to render p. 310)` → NEW: `"Let a = log 2/2. We have ⟨φ, φ⟩ = T_ℚ(φ ∗ φ̃) ≥ 0 for every φ ∈ K(a), where equality holds if and only if φ = 0" (for k = ℚ; the bound is 0 — rendered at p. 310 by the Opus reader)`. And in §9 OLD: `(no page images were rendered this session; Theorem 1's displayed bound is not transcribed)` → NEW: `(no page images were rendered by the writer; Theorem 1's bound is 0, rendered by the Opus reader)`.

**A2** (§1 item 5 and §2.3(c)(i), Krein–Langer's boundary point). OLD: `boundary point a_f := ∫₀^∞det H_f(ξ)dξ` → NEW: `boundary point a_f := ∫₀^∞√(det H_f(ξ))dξ (p. 40)`. OLD: `a_g := ∫₀^∞det H_g(ξ)dξ` → NEW: `a_g := ∫₀^∞√(det H_g(ξ))dξ`.

**A3** (§1 item 6, Bombieri's Corollary). OLD: `such that at least half of its ℓ²-mass is supported on the set of zeros ρ with Re(ρ) = ½"` → NEW: `such that at least half of its ℓ²-mass is supported on the set of zeros ρ with ℜ(ρ) ≠ ½"`.

**A4** (§1 item 8, Poltoratski). OLD: `NOT re-fetched.` → NEW: `NOT re-fetched by the writer; fetched by the Opus reader (`results/e1-m5u/sources-O/poltoratski-0908.2079.pdf`, SHA-256 378856e9…): (2.1) p. 3 and Theorem 2 at arXiv p. 10 confirmed at the page.` And in §9 OLD: `**Not done:** Poltoratski's PDF was not re-fetched (used from the record, dual-model);` → NEW: `**Not done by the writer:** Poltoratski's PDF was not re-fetched (used from the record, dual-model; the Opus reader fetched and confirmed it);`.

**A5** (§1 item 6, the record correction). OLD: `The **trichotomy is the Corollary at p. 224 (PDF p. 44)**` → NEW: `The trichotomy D1(b) §4.3 quotes (with "A + Bx⁻¹ … vanishing identically for 1 ≤ x ≤ M₀") is printed in the **Introduction, p. 185 (PDF p. 5)**, as "the following corollary of one of our theorems", referred there to "§10, Theorem 10 and §11, Theorem 11"; its §11 form is **the Corollary at p. 224 (PDF p. 44)**`.

**A6** (§1 item 9). OLD: `(\`fetched/u-26a-…\`` → NEW: `(\`fetched-r2/u-26a-…\``.

**A7** (§1, a new item after item 10). NEW paragraph: `**11. Mitkovski–Poltoratski, "Determinacy for measures"** (author copy, fetched by the Opus reader: \`results/e1-m5u/sources-O/mitkovski-poltoratski-determinacy.pdf\`, SHA-256 a38da25c…). p. 1: a positive FINITE measure µ is a-determinate if no other positive finite measure has the same Fourier transform on [−a, a]; Theorem 1.2 (p. 1; "in essence, goes back to M. Riesz"): µ is a-determinate iff ∫log m^µ_{a/2}(x)/(1 + x²)dx = ∞; p. 2: "every non-zero measure σ with a spectral gap (−a, a) gives a rise to two a-indeterminate measures σ₊ and σ₋"; Theorem 1.5 (p. 2): Det(X) = G(X); Theorems 1.6–1.7 (pp. 2–3): a finite signed measure with gap (−a, a) alternates in sign along an a/π-uniform sequence \`[read at the page: Opus reader]\`. This is the printed theory of exactly the real-weighted relaxation (§2.3), for finite measures; integer weights do not occur in it.`

**A8** (§2.1 Remark (b), label). OLD: `\`[novelty: single-check]\` for the family (0.1) as such` → NEW: `(the family (0.1) is Schur's product theorem applied to the positive-definite functions ψ⋆ψ̃ and cosh(yu)/cosh(u/2); no novelty is claimed for it)`.

**A9** (§2.2 clause 2(c)). OLD: `Then for every ε ∈ (0, L) and every c′ ≥ 2ε` → NEW: `Then for every ε ∈ (0, min(L, 1)] and every c′ ≥ 2ε`.

**A10** (§2.3(b)–(c), source and label). After `σ_t ≠ ν_ζ for t ≠ 0. ∎` insert: `*Source of the mechanism.* For finite positive measures this is printed: Mitkovski–Poltoratski p. 2 ("every non-zero measure σ with a spectral gap (−a, a) gives a rise to two a-indeterminate measures σ₊ and σ₋", §1 item 11); the theorem above is its transfer to ζ's infinite zero measure via the unit lower bound of the marks. Not found printed for ζ (Opus reader's search, read-O §P).` And OLD: `\`[derivation from (b) + the page]\` \`[novelty: single-check]\`` → NEW: `\`[derivation from (b) + the page]\` \`[novelty: dual-model check 2026-09-26]\` (as to ζ's zero measure; the mechanism is printed, §1 item 11)`.

**A11** (§2.6 (iii)). OLD: `and they are not integer-coefficient statements and not claimed to be` → NEW: `(with ℓ²-coefficients, i.e. not necessarily finite measures — the finite ones come from Poltoratski's theorem), and they are not integer-coefficient statements and not claimed to be`.

**A12** (§2.6, the comb). OLD: `because its positive atoms {ks + s/2} would have to be zeros of ζ` → NEW: `because the atoms {ks + s/2} of its negative part (of its positive part, for −μ) would have to be zeros of ζ`.

**A13** (§3.3(b)). OLD: `class numbers 12 and 12` → NEW: `class numbers 3 (class group [3], label .1) and 12 (class group [2, 6], label .2)`.

**A14** (§3.3(b)). OLD: `the next primes 23, 29, 31, 37, … differ between the two rows (extract file)` → NEW: `after 19 the rows differ at 23, 31, 37, 41 and agree (both inert) at 29, 43, 47, 53, 59 — exactly the primes that are cubes modulo 229 or 367 (extract file; reader's check \`verify-O/rung3_check_run.log\`)`.

**A15** (§3.3(d)). OLD: `and by the count none of this construction can:` → NEW: `and by the count none of this construction is expected to:`.

**A16** (§1 item 6, before the Example). OLD: `**"An Example", p. 224:** two Dirichlet` → NEW: `**"An Example", p. 224**, introduced by "One may ask if linear dependence relations occur at all. The following example shows that they may occur for Dedekind zeta functions.": two Dirichlet`.

**A17** (§4, after candidate (f), before §4.1). NEW paragraph: `**(g) A seventh candidate (added by the Opus reader): the Mitkovski–Poltoratski determinacy/oscillation theory (§1 item 11).** *Mechanism:* the tapered difference w_T·μ is a FINITE signed measure with spectral gap (−L + ε, L − ε) and negative part on ζ's ordinates; by Theorem 1.6 its sign pattern alternates along an (L − ε)/π-uniform sequence whose odd terms lie in ζ's ordinate set — a B-half of density (L − ε)/(2π), which ζ's ordinates supply locally exactly where α(T) ≤ 1 (up to ε), a threshold that coincides with the count's α = 1 line. *First obstacle:* uniformity is a large-scale (Beurling–Malliavin-type) property and supp(w_T·μ) = supp μ (w_T has only discrete zeros), so the alternation can be carried by heights where the zeros are dense; the theorem gives no statement on the window, and integrality does not enter. **REJECTED at its first obstacle**; a LOCAL form of Theorem 1.6 would be exactly clause 6's input (III).` And in §4.1 OLD: `(b), (d), (e) are rejected at their first obstacle, and the sixth shape (f) has no object to act on.` → NEW: `(b), (d), (e), (g) are rejected at their first obstacle, and the sixth shape (f) has no object to act on.`

**A19** (§6 rider (1)). OLD: `orbit sums (2π)⁻¹(|ψ̂|² ∗ P_y)(x) ≥ 0 on the strip` → NEW: `real parts Re ĝ(x + iy) = (2π)⁻¹(|ψ̂|² ∗ P_y)(x) ≥ 0 on the strip (a four-point orbit contributes four times this)`.

**A20** (§6 rider (2)). OLD: `(from G_X = ∞, Poltoratski Thm 2 + Bombieri 2000 p. 225)` → NEW: `(from G_X = ∞, Poltoratski Thm 2 + Bombieri 2000 p. 225; the mechanism is Mitkovski–Poltoratski's for finite measures, "every non-zero measure σ with a spectral gap (−a, a) gives a rise to two a-indeterminate measures")`.

**A21** (§6 rider (2)). OLD: `and so is the soft-windowed datum at every height (E1 §2.4)` → NEW: `and so is the soft-windowed datum at all but countably many heights (E1 §2.4)`.

**A22** (§6 rider (3)). OLD: `Bombieri 2000 p. 224's Example is its complex-datum form.` → NEW: `Bombieri 2000 p. 224's Example — introduced as showing that linear relations "may occur for Dedekind zeta functions" — is its complex-datum form.`

**A23** (§7.3 record corrections). OLD: `the trichotomy is the Corollary at p. 224 (PDF p. 44) — the brief's and D1(b) §4.3's "Theorem 10 (p. 228)" is wrong as to page and as to which statement carries the trichotomy;` → NEW: `the trichotomy D1(b) §4.3 quotes (with A + Bx⁻¹ on 1 ≤ x ≤ M₀) is printed in the Introduction at p. 185 (PDF p. 5) as "the following corollary of one of our theorems", with its precise forms Theorem 10 (p. 221) and the Corollary after Theorem 11 (p. 224) — the brief's and D1(b) §4.3's "Theorem 10 (p. 228)" is wrong as to page (p. 228 carries no theorem);`.

**A24** (§8 Instruments row 2). OLD: `have orbit sums (2π)⁻¹(|ψ̂|² ∗ P_y)(x) ≥ 0 on the closed strip` → NEW: `have Re ĝ(x + iy) = (2π)⁻¹(|ψ̂|² ∗ P_y)(x) ≥ 0 on the closed strip (orbit sums are 4× this)`.

**A25** (§8 Untried line 1). OLD: `What E1 settled: the real-weighted relaxation is a continuum at every L (Krein indeterminate, under RH), so integrality is the whole content;` → NEW: `What E1 settled: the real-weighted relaxation is a continuum at every L (Krein indeterminate, under RH; the mechanism is Mitkovski–Poltoratski's for finite measures), so integrality is the whole content;`.

**A26–A28** (labels): see the next section. (A18 is unused: the §5.2 paragraph needs no change.)

---

## Labels, row by row (standing order 7)

| Where | Writer's label | Reader's label | Basis |
|---|---|---|---|
| §1 item 1 (vi-b), Yoshida Prop. 7 as "nearest printed neighbor of F1(b)" | `[read at the page]` `[novelty: single-check]` | **A26:** `[read at the page]` (twice-opened) + `I infer` for the pairing; drop the novelty tag (a characterization, not a result). OLD: `\`[read at the page]\` \`[novelty: single-check]\` for the pairing with F1(b)` → NEW: `\`[read at the page: Yoshida 1992 pp. 322–324, dual-model 2026-09-26]\`; the pairing with F1(b) is \`I infer\`` | pp. 322–324 rendered by the reader |
| §2.1 Remark (b), the family (0.1) | `[novelty: single-check]` | no novelty (A8) | Schur's product theorem |
| §2.3(c)(i), a_g = +∞ / indeterminacy for ζ | `[novelty: single-check]` | `[novelty: dual-model check 2026-09-26]` as to ζ's zero measure, mechanism printed (A10) | §P search + Row 2c re-derivation |
| §4.1, the localized question "never asked" | `[novelty: single-check]` | **A27:** `[novelty: dual-model check 2026-09-26]` (two targeted searches, Sep 26 2026 before 02:21 IST: "Krein continuation problem indeterminate … integer atoms", "truncated trigonometric moment problem integer weights" — no hit; re-derivation: the implication is correct). OLD: `(\`[novelty: single-check]\`; the reader's prior-art pass on "integer-atomic continuations / integral spectral measures in the indeterminate case" is the check)` → NEW: `(\`[novelty: dual-model check 2026-09-26]\`: the Opus reader's searches for integer-atomic continuations and integrality in truncated moment problems found nothing; short search, not exhaustive)` | read-O §P + this row |
| §1 items 1–7, 9: `[read at the page]` | — | **dual-model** for every page the launch line named (Yoshida pp. 284, 285, 310, 321–324; Suzuki pp. 1–2, 10–11; Krein–Langer pp. 29–30, 33–34, 40–41; Bombieri pp. 221, 224–225, and p. 185; Lapidus p. 5; LMFDB .1/.2), with A1–A3, A5, A13–A14 applied | reader's renders |
| §1 item 5 other pages (pp. 1–3, 22–24, 32, 37–39), Yoshida pp. 287–289, 320; Suzuki Thms 4.1–4.2, 6.1; y-09, y-10 | `[read at the page]` | stay single-model `[read at the page]` (text-layer spot checks only for y-09 pp. 3–5, y-10 p. 1, KP p. 210) | not rendered by the reader |
| §3.3(c) "stop line (ii) fires … in print (LMFDB)" | `[read at the page]` | **A28:** `[read at the page: LMFDB, dual-model 2026-09-26]` for the field data; the ghost-pair statement itself is `[derivation]` from those data and Yoshida (1.6). OLD: `So the pair is an EXACT free-stratum ghost — the object D1(b) §2.3 R3 and its Untried line 2 declared "OWED" and "not constructed exactly": on rung 3, with a positive datum, it is in print (LMFDB) \`[read at the page]\`.` → NEW: `So the pair is an EXACT free-stratum ghost — the object D1(b) §2.3 R3 and its Untried line 2 declared "OWED" and "not constructed exactly": on rung 3, with a positive datum, its data are in print (LMFDB \`[read at the page]\`, dual-model 2026-09-26) and the ghost property is \`[derivation]\` from them and Yoshida (1.6); Bombieri p. 224 anticipates it in words ("may occur for Dedekind zeta functions").` | reader's LMFDB fetch + Row 3b |
| `[recalled, unverified]` items of §9 | — | unchanged; none load-bearing (checked: clause 3(b) uses Littlewood only through Bombieri's printed sentence) | — |
| The rider | `[dual-model check]` after the reader | `[dual-model check 2026-09-26]` with A19–A22 | Row 6 |

---

## Group-IV decision

**None.** No exact ghost for ζ's own datum is exhibited or implied (the rung-1 and rung-3 pairs are controls outside ζ's class, and both sit where the count already says "free"); the slot yields a contract (clauses 1–5 proved or cited, 6–7 stated), controls, the E7 correction, and a rider on II.1 — the brief's default.

## DECISION (stop line (iii))

**CLOSES as STOP-shape, after the FIX-FIRST amendments A1–A28 (27; none touches the decision).** The load-bearing theorem (§2.3(b), Krein indeterminacy of F_Λ at every bandwidth under RH) holds exactly and I could not refute it; it is a short corollary of printed facts (Bombieri p. 225, Poltoratski Theorem 2, Mitkovski–Poltoratski p. 2), not found printed for ζ. The rung-3 pair is right in every mathematical respect (p₀ = 19 confirmed by LMFDB, by polynomial root counts, and by the character rule; datum equality exact at Yoshida p. 284; free stratum only), with two LMFDB transcription errors to fix. The §4 dismissals hold; the one omitted candidate (Mitkovski–Poltoratski) fails at its first obstacle and is added. The II.1 rider (§6) and the §4.2 correction (§5.2) are exact at their records with A19–A22 on the rider and no change to §5.2. **Nothing for the orchestrator to decide beyond applying the amendments**; one optional item: whether to file Mitkovski–Poltoratski (`sources-O/`) into the corpus (`fetched/`) at harvest — it is now a cited source of the rider.
