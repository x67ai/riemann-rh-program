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
