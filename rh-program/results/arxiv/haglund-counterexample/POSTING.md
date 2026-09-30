# Posting instructions for the sponsor — "A counterexample to Haglund's monotonic-zeros conjecture for the Riemann Ξ approximants"

Written 2026-10-01 (Session 38). Everything below is the sponsor's act; nothing here has been posted by the program. The package is frozen once the git tag named at the bottom exists; any later change is a public revision (a new Zenodo version), never a silent edit.

## What the paper is, in one paragraph (for the record description and for anyone who asks)
Haglund (2009) conjectured that the partial sums Ξ_N of Riemann's series for the Ξ-function have "monotonic zeros" in the first quadrant, and proved that this would imply the Riemann hypothesis. The paper shows the conjecture is false at N = 27: Ξ₂₇ has a non-real zero whose real part is smaller than that of a real zero. The fact is proved twice, by two independently written interval-arithmetic certificates (Arb ball arithmetic; outward-rounded intervals with proved truncation bounds), and the mechanism is explained (the approximants sit below Ξ on the critical line, so their real zeros live in the positive lobes of Ξ; near the height 4(N+1)² a shallow lobe followed by a deeper one leaves a non-real zero below real ones). Two statements in Haglund's paper are corrected. **The result refutes a sufficient condition for the Riemann hypothesis and says nothing about the Riemann hypothesis itself.** Posts and descriptions must say so in the first sentence.

## Files (all in this folder)
- `main.pdf` — the paper (16 pages). This is what goes on x67.ai and Zenodo.
- `main.tex` — the source; this alone is what arXiv takes (no figures, no .bib).
- `abstract.txt` — line 1 the title, the rest the abstract (paste into metadata forms).
- `haglund-counterexample-certificate.zip` — the reproducibility archive (both certificates, the re-runs, the third evaluation, README with the exact commands and expected outputs). Its SHA-256 is printed in the paper and stored in `haglund-counterexample-certificate.zip.sha256`; upload it as a second file on Zenodo so the printed hash resolves to a public object.

## Where, in the order used for the two earlier papers
1. **x67.ai** — upload `main.pdf` as `https://x67.ai/haglund-counterexample.pdf` (same pattern as `cubic-augmentation-no-go.pdf` and `tate-products-no-go.pdf`).
2. **Zenodo** (new record, not a new version of an earlier one): upload `main.pdf` and the certificate zip; Title = line 1 of `abstract.txt`; Authors = Kunal Tyagi; Description = the abstract; Resource type = Publication / Preprint; License = CC BY 4.0 (as before); Keywords: Riemann hypothesis, Riemann Xi function, Haglund conjecture, incomplete gamma function, interval arithmetic, computer-assisted proof, counterexample; Related identifiers: `https://github.com/x67ai/riemann-rh-program` (is supplemented by) and the git tag URL below. Publish, then send me the concept DOI and the version DOI; I record them in `results/arxiv/README.md` and the paper is frozen.
3. **arXiv** (math.NT primary; cross-list math.CA or math.NA optional) — only once you hold an endorsement (CIRCULATION-PREP item 4, still open). Upload `main.tex` alone; Comments: "16 pages. Two independent interval-arithmetic certificates; reproducibility archive: Zenodo DOI <fill in>. Code and data: https://github.com/x67ai/riemann-rh-program". MSC 2020 suggestions (yours to confirm): 11M26 (zeros of ζ and L-functions), 11Y35 (analytic computations), 33B20 (incomplete gamma functions), 30C15 (zeros of entire functions).

## Do not
- Do not describe it as progress on the Riemann hypothesis. It is not; the paper's Scope section says exactly what it is.
- Do not edit `main.tex` after tagging without a new version number and a stated change.
- Do not post the internal folders (`results/haglund-cert-s37/`, `results/novel-wave-s36/staircase/`) separately; they are public in the repository and cited from the paper by path.

## The tag
The git tag `haglund-cert-2026-10` marks the exact repository state the paper was prepared against; it is printed in the paper's data-availability statement. Created in Session 38 on the commit that holds the referee-revised package (LOG.md, 2026-10-01); `git tag -l 'haglund-*'` shows it. **Before posting, decide the history question in LOG.md's Session-38 sponsor note (third-party literature untracked at this commit but still present in earlier commits).**
