# SHARED — seed M1a `beurling-fe` (NOVEL-APPROACH WAVE 2, Session 37)

Agent: Opus 5.5 (seed agent). Charter: `results/novel-wave-s37/WAVE-CHARTER.md` §"Seed M1a".
Deliverables: `NOTE.md` (the unit), `verify/` (scripts + logs), `sources/` (texts quoted, with line numbers).

## 2026-09-30 block 1 — setup, inputs read

- Read: charter §0, §M1a, rules; the four `novel-wave-s36/*/read-F.md`; zoo I.2, I.7, I.8.
- Extracted to `sources/` (pdftotext -layout): p3-22c1 (Hilberdink–Lapidus 2006), p3-22c2 (Hilberdink 2012),
  w-18a (Hilberdink 2005), p1-02 (DMV 2006), t-50 (Diamond–Zhang book 2016).
- First gate findings:
  * Hilberdink–Lapidus 2006 p. 2 (sources/p3-22c1…txt lines 126–128): "We do not give a complete answer to the latter
    difficult question [when ζ_P can be completed to satisfy a generalised FE], but indicate several approaches and give
    a criterion". Their Theorem 3.2 (lines 1036–1057) is an EQUIVALENCE (FE ⟺ modular identity with a finite residual
    H(x)); addendum: Bochner 1951 (Ann. Math. 53, 332–363) Theorems 2, 3 had "a very similar result". No rigidity theorem.
  * Hilberdink 2012 Theorem A (lines 97–103): N(x) − cx PERIODIC + N in class T (finitely many discontinuities per
    bounded interval) + g-prime system ⟹ N is the counting function of the usual primes minus finitely many primes.
    Proposition 3.2 (lines 536–556) is the pigeonhole "irrational α" argument — the same device this unit needs.

## 2026-09-30 block 2 — the Fejér argument (found), gate sources gathered

- FOUND (NOTE §1 draft): with φ(x) = (1−|x|)₊, self-duality of μ = ρδ₀ + Σ(δ_{n_k}+δ_{−n_k}) and the Beurling gap
  (no generalized integer in (0,1)) give Σ_k sin²(πn_k)/n_k² = 0 ⟹ all n_k ∈ Z ⟹ μ 1-periodic ⟹ 𝒩_P = N. Uses only
  dN ≥ 0, supp ⊂ [1,∞), exact FE. To be attacked (NOTE §4) and gated.
- Fetched: Kahane–Mandelbrojt 1958 (Numdam, sources/kahane-mandelbrojt-1958-asens75.{pdf,txt}); Olofsson 2010 preprint
  (sources/olofsson-2010-…{pdf,txt}); Lagarias 1999 abstract (sources/lagarias-1999-delone-abstract.md, Firecrawl).
  Copied from N1: Nakamura 2008.02570, Burnol 1106.4749, Lev–Olevskii u-30b, Olevskii–Ulanovskii p2-19b, Kurasov–Sarnak,
  Favorov u-34b, y-33, y-34, Gonçalves u-28b, Meyer u-25a.
- arXiv export API timed out all session (HTML search used instead; queries saved in sources/arxiv-queries/).
- Gate reading so far: KM58 Thms 1–2 = FE ⟺ Poisson formula (the reformulation is in print); KM58 Prop. 7/Thm 4/Thm 5 =
  density/gap theorems for complex coefficients (equality case = Dirac combs); Diamond–Zhang 2016 p. 1 (t-50 lines 356–360)
  states RH "will require more than just the multiplicative structure"; Olofsson Prop. 3.1 + Conj. 1.2 (Beurling's
  problem: |N(x) − [x]| small ⟹ primes); Lagarias 1999: Delone systems inside Z classified; the non-integer Delone case
  is Lagarias's open question (Olofsson lines 656–669). None states FE-rigidity for Beurling systems (so far).

## 2026-09-30 block 3 — NOTE §2 (gate), §3 (Prop. R + Lemma G), §4 (Theorem T + T1–T3) written

- Gate verdict (NOTE §2): not settled in print in anything read. Closest printed results: Hamburger's second theorem as stated by
  Burnol 1106.4749 line 160 (f ORDINARY, dual frequencies ≥ 1 ⟹ f = cζ) and Burnol Thm 2 (f, g general: only an equivalence);
  Hilberdink–Lapidus 2006 lines 125–128 call the Beurling-FE question "difficult" and leave it open. Web searches (2026-09-30):
  "Beurling … functional equation must be Riemann zeta", "Lagarias Delone", "Bochner Chandrasekharan On Riemann's functional
  equation", "generalized primes Hamburger", "positive measure equal to its Fourier transform … Dirac comb" — no statement found.
  Also fetched: Perelli 1605.02354 (converse-theorem survey; Hecke groups G(λ), λ > 2 ⟹ infinite-dimensional solution spaces).
- THEOREM T (positive Hamburger): dN ≥ 0 on [1,∞), Riemann FE with poles only at 0,1, growth (G') ⟹ dN = ρΣδ_n.
  Corollaries: Beurling discrete ⟹ rational primes; no continuous Beurling system has the FE; general Dirichlet series with
  a_k ≥ 0, λ_k ≥ 1 ⟹ multiple of ζ. Proof = Fejér kernel (1−|x|)₊ + periodicity; Lemma G proves Gaussians determine even
  tempered distributions (no Hermite-density citation needed).
- NEXT: verify/ scripts (theta relation, Fejér identity, conductor identity, controls, least-squares experiment); §5 attack log;
  §6 second proof in the u.d. case (Lev–Olevskii + Hilberdink pigeonhole + Hamburger); relaxations; controls; close.

## 2026-09-30 block 4 — verify v1, v2, v2b run; NOTE §5 (attack log), §6 (u.d. second proof), §7 (non-u.d. + experiment)

- v1 (`verify/v1_theta_fejer_conductor.log`): theta relation for Z exact at 60 digits; Fejér sums: Z 7e−29, near-misses 2e−3..9e−2;
  conductor identity ρ_q(1 − q^{−1/2}) = 2q^{−1/2}Σc_k sinc²(n_k/q) confirmed on ζ(s)(1+q^{1/2−s}), q = 2, 4, 9, and F_{5,5} (8.8 = 8.8,
  up to the truncation tail 1e−4), each also satisfying its conductor-q theta relation to 1e−60.
- v2/v2b: least squares on the theta relation at double precision "finds" {2, 3, arbitrary} near-solutions (RMS 1e−16); at 60 digits
  they fail by 1e−4..0.5 and have Fejér sums 2e−3..9e−3. Lesson recorded in NOTE §7.
- §6: Prop. U = independent proof in the u.d. case via Lev–Olevskii Thm 1 + Hilberdink's pigeonhole + Hamburger (dual-route check).
- NEXT: §8 relaxations — (a) continuous (orchestrator's sketch: verify prime density ≥ 0), (b) conductor: Theorem C (q ≥ 1, = iff ζ)
  and the open q > 1 question, (c) finite Euler factor, (d) extra poles (Fejér identity with residual), (e) no positivity; §9 controls.

## 2026-09-30 block 5 — v3 run; NOTE §8 (relaxations) written

- v3 (`verify/v3_continuous_sketch_and_controls.log`): orchestrator's continuous sketch CONFIRMED (G symmetric 1e−27; Mellin 1e−19;
  prime density f ≥ 0 iff a ≥ β on the grid; −0.077 at a = 0.7 < β = 0.8). Virtual curve: b_d ≥ 1 to d = 60, zeros Re s = 0.79899;
  genus-1 scan over F₅ (L = 1 − tu + 5u²): b_d ≥ 0 to d = 60 exactly for t ∈ {−5,…,6}; RH-false admissible t = −5, 5 (6 = empty system).
  F_{5,5}: Λ(5^k)/log 5 = 6, −14, 51, −174, 626, −2249; zeros at σ = 0.79899, 0.20101 (the SAME as the virtual curve: its factor
  1 + 5u + 5u² is the t = −5 curve's L-polynomial).
- §8 verdicts: (a) sketch correct; entire completed function impossible (T2). (b) THEOREM C: conductor q ≥ 1, q = 1 iff ζ; identity (C_q);
  q > 1 OPEN = question Q_cond (Beurling + FE at conductor q > 1), all known positive-coefficient solutions fail Λ ≥ 0 (every q > 1 for
  ζ(1+q^{1/2−s})). (c) finite Euler factor: reduces to T, RH-equivalent. (d) extra poles: identity (F_R), continuous RH-false systems
  live there; discrete open. (e) positivity dropped: open. (f) double pole: not pursued.
- One error caught and fixed in §8(b) (q irrational: q = √2 has q² = 2 prime; replaced by the q^{2k} argument, Λ(8)/log 8 = −0.138).

## 2026-09-30 block 6 — CLOSE T; NOTE complete (§0–§11); final checks

- NOTE re-read whole; fixes applied: status line; T2 restated precisely (dΠ = Σ_p Σ_k k^{−1}δ_{p^k}); Theorem C's q > 1 step simplified
  (atom at 1 ∉ qN); recalled labels added (Kaczorowski–Perelli analogy); §9 wording (positivity over F_q ≈ |α_i| < q, not Hasse);
  Lemma TB (translation-boundedness from μ ≥ 0, μ̂ ≥ 0) proved in §7 as the charter asked; finite-order justification for (H2) in §6.
- CLOSE: T. Theorem T (positive Hamburger) + T1 (discrete Beurling ⟹ rational primes) + T2 (no continuous system) + T3 (positive
  general Dirichlet series with frequencies ≥ 1 ⟹ cζ); Prop. U (independent u.d. proof); Theorem C (conductor q ≥ 1, = iff ζ; (C_q)).
  Verdicts on relaxations: (a) orchestrator's continuous sketch correct, entire completion impossible; (b) q > 1 OPEN (Q_cond);
  (c) finite Euler factor → T, RH-equivalent; (d) extra poles: identity (F_R), continuous RH-false systems live there; (e) signed: open.
- Controls printed (v3): virtual curve and genus-1 F₅ scan (RH-false admissible t = ±5); F_{5,5} = ζ × (t = −5 L-polynomial), Λ(25) < 0.
- Files: NOTE.md, SHARED.md; verify/ v1, v2, v2b, v3 (.py + .log); sources/ (gate texts, arXiv/Firecrawl captures, queries).
- Successor (ranked): Q_cond (Beurling + FE at conductor q > 1; §8(b), §11); discrete + extra poles; signed Hamburger with gap.

## 2026-10-01 OPUS READER (read-O.md) block 1 — §1 re-derivations landed

- Reader: Opus 5.5, independent of the orchestrator's read (verify-F/ not opened). Deliverable `read-O.md`, scripts `verify-O/`.
- §1: Prop. R, Lemma G, Theorem T Steps 0–2, T1, T3, Prop. U, Lemma TB, Theorem C (incl. (C_q) by hand: exact on ζ(1+q^{1/2−s})
  and F_{5,5}), §8(a)(b)(d), §9 — all re-derived ✓. No error found that affects T. Prose/hypothesis gaps: positivity also enters
  through Prop. R's linear growth (NOTE line 126 says "only"); T2 needs polynomial growth, which Diamond–Zhang's definition
  (t-50 lines 592–593) does not supply. §8(e)'s verdict "open" is wrong: an explicit signed counterexample is in hand (§6 of read-O).
- Next: §2 independent numerics, §3 prior-art gate.

## 2026-10-01 OPUS READER block 2 — §2 independent numerics landed (verify-O/ o1–o5)

- o1: Fejér sums of the v2 near-solutions in CLOSED FORM (Poisson + Euler-factor convolution, no truncation): 1.654343e−3, 5.358231e−3,
  2.612375e−3, 3.075454e−3 (K=6, new), 8.744635e−3; Z exactly 0. Writer's v2b values confirmed (they sit 2e−7..1.4e−6 low = tail).
- o2: theta defects via jtheta confirm v2b (ρ = 1, [1/8, 8]) to 3 digits; with the true residue: 0.18–1.6 on [2^−6, 2^6].
- o3/o4: a SIGNED self-dual measure with gap (−1,1)∖{0} that is not δ_Z (χ₅-comb + two dilated comb pairs): exact Riemann FE, simple
  poles at 0, 1, all frequencies ≥ √5/2 > 1 — and RH-FALSE (zero at 1.32691 + 33.26351i). NOTE §8(e)'s "open" is answered.
- o5: (C_q) exact on ζ(1+5^{1/2−s}) + L(s,χ₅), q = 5.
- Next: §3 prior-art gate.
