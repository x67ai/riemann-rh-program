# REFEREE BRIEF — `main.pdf` / `main.tex`, "A counterexample to Haglund's monotonic-zeros conjecture for the Riemann Ξ approximants"

Written 2026-10-01 by the writer. Read `main.pdf` first as an outside reader would; then check it against the files below. Report every
finding with its place (section, line of `main.tex`) and a proposed fix; fix nothing silently. Paths are relative to `rh-program/`.

## What to check
1. **Theorem 1.1 and Section 6** against `results/haglund-cert-s37/producer-A/CERT.md`, `producer-B/CERT.md` and that folder's `NOTE.md`:
   every number in Tables 1-3 and in §6.1-§6.2 (bit sizes, M, the tail bounds, E, M_R, ρ, m, K), the digits of z*, the half-widths
   4·10⁻¹¹ (A) and 3.7·10⁻¹¹ (B), the inequalities in the proof of Theorem 1.1(c), and z* − c = 3.66e−11 − 2.18e−11 i (A's CERT §5).
2. **Theorem 7.1** (N = 24) against A's CERT §8 and B's CERT section "H5".
3. **Sections 2-4** against `results/novel-wave-s36/staircase/NOTE.md` §1-§2 as corrected by `read-F.md` F1-F5. Map: Lemma 2.1 ↔
   `lit/PRIOR-ART.md` §0 (the relation Φ_n = ½s(s−1)g_n + (4πn²−1)e^{−πn²}; the proof printed is the writer's re-typing of the
   recurrence argument named there — check it line by line); Thm 3.1 ↔ D; Cor 3.2 ↔ D1; Thm 3.3 ↔ D′ (F1); Prop 3.4 ↔ D′(2);
   Cor 3.5 ↔ D′(1) (F5); Thm 4.1 ↔ A (F2); Thm 4.2 ↔ B; Prop 4.3 ↔ F, with F3 for hypothesis (ii). Note for Thm 4.1: the paper writes
   Φ_w = Σ w_n φ̃_n with φ̃_n = 2 × the NOTE's φ_n (so Φ_w = 2Σ w_n φ_n, as F2 requires), hence its u → −∞ coefficient
   −2π(2k+3)(−π)^k/k!·Σ w_n n^{2k+2} is twice the NOTE's; confirm.
4. **Section 5** (floating-point, not part of the proof) against NOTE §3 (departure lobes N = 1-7, lobe count to height 320) and §4.1
   (scan windows, tally, the N = 21 and N = 20 near misses, the N = 27 and N = 24 lobes and ratios).
5. **The two errata** against Haglund's text on disk, `results/novel-wave-s36/staircase/lit/haglund-0910.5228.txt`: the p. 4 table
   (text lines 199-209), (52) and the p. 10 sentence (lines 541-547). The census count 31 for N = 4 is from NOTE §7 errata (2).
   Writer's own remark, not on disk as a claim: Haglund's (51) applies (50) at x instead of x/2, so his (52) values are one quarter of
   the true coefficients (N = 1: 0.078997 / 0.01974938206 = 4.000). The paper says so after Prop 3.4. Confirm or strike.
6. **Every quotation at the page:** Haglund pp. 3-4 and 10 (text lines 143-151, 153, 190-197, 546-547); Platt-Trudgian abstract
   (`results/arxiv/haglund-counterexample/lit/platt-trudgian-2004.09765-abs.html`); Baccaro's Zenodo record (same `lit/`,
   `zenodo-22059236.md` and `.html`); Ahn pp. 10-11 (`results/haglund-cert-s37/novelty-F/ahn-thesis-penn.txt` lines 505-514);
   Lagarias-Montague p. 24 (text lines 1349-1352); Ki p. 198; LMOZ Theorem 1.7; Nakamura p. 4 Theorem D; Burnol pp. 2-3.
7. **Scope:** the abstract and §1.3 must say plainly that the paper refutes a sufficient condition for RH and says nothing about RH.
8. **Bibliography:** each entry against its source (texts on disk, Crossref for Platt-Trudgian and Arb, the Zenodo record). The
   Riemann 1859 page range is taken from reference lists of papers on disk, not from a primary source; check it.

## Points the writer could not settle alone (decide or confirm)
- AI footnote: the README wording is used verbatim, as the brief requires; the two posted papers carry the later wording.
- Length: 16 pages against the brief's target of 8-12; the full proofs of D, D′, A, B and the certificate lemmas account for it.
- Data availability cites real directory names that contain internal labels; there is no git tag pin (the writer may not run git),
  but the certificate zip is pinned by its SHA-256, printed in the paper.
- `certificate/producer-B/logs/ladder.log` is the orchestrator's re-run output (the script rewrites its own log), so its SHA-256
  differs from the one in B's `SHARED.md`; the values are identical. The certificate README says so.
- Producer A's CERT cites Haglund's appendix as p. 15; the text on disk puts it on p. 16, which the paper uses.
- The writer re-ran both certificates and the third evaluation on 2026-10-01; results in `SHARED.md`.
