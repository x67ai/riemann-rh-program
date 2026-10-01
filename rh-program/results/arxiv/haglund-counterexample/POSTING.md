# Posting instructions for the sponsor — "A counterexample to Haglund's monotonic-zeros conjecture for the Riemann Ξ approximants"

Written 2026-10-01 (Session 38); updated 04:40 IST 2026-10-01 (Session 39) after the sponsor asked the program to post the paper (a Zenodo draft prepared in his browser session; x67.ai remains his push). The package is frozen once the git tag named at the bottom exists; any later change is a public revision (a new Zenodo version), never a silent edit.

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

## The tag
The git tag `haglund-cert-2026-10` marks the referee-revised package of Session 38 (history). The posted package is the repository state of Session 39, 2026-10-01 (the paper de-internalized and its RH-verdict sentences removed on the sponsor's instructions; the certificate archive rebuilt without its working logs, SHA-256 4dfb1360042c3123b815e571a1916720081beca51fe9be8d6ed4760f41b1091c, printed in the paper; 15 pp.); tag it `haglund-paper-2026-10-01` at the commit that carries the final `main.pdf`. The history question (third-party literature in earlier commits) is still the sponsor's decision and does not block posting.

## Zenodo (done as a DRAFT in Session 39)
Draft record https://zenodo.org/uploads/23071931 in the sponsor's account: both files, title, author (Tyagi, Kunal), date 2026-10-01, Publication / Preprint, CC BY 4.0, seven keywords, description = the abstract. **Not published.** The sponsor opens it, checks the file list shows the 15-page `main.pdf` and the zip, and clicks Publish; then records the concept DOI and the version DOI in `results/arxiv/README.md`.

## x67.ai (the sponsor's commands)
The served copy is deployed from `public/` by the Cloudflare Worker on every push to `main`. From the repository root:

    cp rh-program/results/arxiv/haglund-counterexample/main.pdf public/haglund-counterexample.pdf && git add public && git commit -m "serve haglund-counterexample.pdf" && git push origin main

The URL will be https://x67.ai/haglund-counterexample.pdf within a minute or two (add the same `cp` line to `public/sync.sh` for later rebuilds).

## Zenodo — PUBLISHED (recorded 17:21 IST 2026-10-01, Session 41)
Published by the sponsor. Concept DOI 10.5281/zenodo.23071930 (cite this); version DOI 10.5281/zenodo.23071931; record https://zenodo.org/records/23071931. Both files on the record equal this folder's `main.pdf` and certificate zip byte for byte (checked through the public record API). Recorded in `results/arxiv/README.md`. Still open: the x67.ai copy (the command block above).
