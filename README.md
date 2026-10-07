# Papers, certificates and code — analytic number theory

This repository holds three papers in analytic number theory, the computer-checked
certificates and Lean files that support them, and the code and data needed to reproduce the
computations.

**Author:** Kunal Tyagi &lt;hello.jay.tyagi@gmail.com&gt;

**Use of AI.** The mathematics in this repository — the derivations, the computations, the
verification suites, the Lean formalization, and the text of the papers — was produced by
**Claude (Anthropic)** working under the author's direction. The author set the objectives, made
the technical and editorial decisions, and is responsible for the content. Claude is a tool and
is not an author. The same statement appears in a footnote on page 1 of every paper.

---

## The papers

| Paper | PDF | DOI |
|---|---|---|
| A counterexample to Haglund's monotonic-zeros conjecture for the Riemann Ξ approximants | [x67.ai/haglund-counterexample.pdf](https://x67.ai/haglund-counterexample.pdf) | [10.5281/zenodo.23071930](https://doi.org/10.5281/zenodo.23071930) |
| The two-moment certificate is robust under Rudnick–Sarnak-range cubic augmentation with capacity control | [x67.ai/cubic-augmentation-no-go.pdf](https://x67.ai/cubic-augmentation-no-go.pdf) | [10.5281/zenodo.22171688](https://doi.org/10.5281/zenodo.22171688) |
| Products of the per-prime Tate curves of absolute geometry carry no correspondence calculus for the Weil explicit formula | [x67.ai/tate-products-no-go.pdf](https://x67.ai/tate-products-no-go.pdf) | [10.5281/zenodo.22171136](https://doi.org/10.5281/zenodo.22171136) |

## Where the files are

Paths are relative to `rh-program/`.

| Paper | Source and PDF | Code, data and records the paper cites |
|---|---|---|
| Haglund counterexample | `results/arxiv/haglund-counterexample/` (`main.tex`, `main.pdf`) | In the same folder: `certificate/` and `haglund-counterexample-certificate.zip` (the two interval-arithmetic certificates; the hash of the archive is printed in the paper); `computations/` (the floating-point computations of Sections 3 and 5) |
| Cubic augmentation | `results/arxiv/a4-no-go/` | `results/a4-m2-gate/` (specification, run report, independent check, follow-up report, raw data, code); `results/a4-no-go/` (proof note, pair-channel note, data digest, formalization record, and the verification suite `verify/`); `results/adjudication-A4.json`; `directions/A4-lindelof-lock.md`; `lean/` |
| Tate products | `results/arxiv/seed-no-go/` | `results/c3-r/` (the numerical checks, their independent re-implementation, and the prior-art record); `results/arxiv/m1-noncirc/` (the companion note); `results/arxiv/citation-verification/` (the source checks) |

The cubic-augmentation and Tate-products papers cite the tag `paper-2026-08-28`; the files they
list are at that tag.

## Checking the work

* **Interval-arithmetic certificates.** The counterexample paper rests on two independently
  written certificates (Arb ball arithmetic; outward-rounded intervals with proved truncation
  bounds). `rh-program/results/arxiv/haglund-counterexample/certificate/README.md` gives the
  exact commands and the expected outputs (Python 3 with python-flint and mpmath).
* **Floating-point computations of the counterexample paper.**
  `rh-program/results/arxiv/haglund-counterexample/computations/README.md` lists each
  computation with its command and its stored output (Python 3 with mpmath).
* **Lean.** Twelve theorems of the cubic-augmentation paper are machine-checked in Lean 4
  against a pinned Mathlib (`rh-program/lean/`; see its `README.md` for the build, which uses
  the Zeta23 library, <https://github.com/anthropics/zeta-23-lean>). `#print axioms` on all
  twelve returns `[propext, Classical.choice, Quot.sound]`.
* **Verification suite of the cubic-augmentation paper.** In
  `rh-program/results/a4-no-go/verify/`, each `verify_t<n>.py` checks the results of one
  section and writes `verify_t<n>_out.json`; `pairchan_verify_all.py` runs the pair-channel
  suite (Python 3 with numpy, scipy and mpmath; run from that folder).
* **Numerical checks of the Tate-products paper.** In `rh-program/results/c3-r/`:
  `python3 seed-no-go-checks.py` (checks A–E of the paper) and
  `python3 referee_seed_checks.py` (the independent re-implementation); Python 3 with mpmath.

## License

**Apache License 2.0** for everything in this repository (see [`LICENSE`](LICENSE) and
[`NOTICE`](NOTICE)), Copyright 2026 Kunal Tyagi. The prose — the papers and notes — is
additionally offered under **CC BY 4.0**.
