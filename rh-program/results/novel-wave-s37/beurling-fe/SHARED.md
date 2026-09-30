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
