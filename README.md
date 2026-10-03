# Papers, certificates and code — analytic number theory

This repository holds three papers in analytic number theory, the computer-checked
certificates and Lean files that support them, and the code needed to reproduce the
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

Sources are under `rh-program/results/arxiv/` (`haglund-counterexample/`, `a4-no-go/`,
`seed-no-go/`).

## Checking the work

* **Interval-arithmetic certificates.** The counterexample paper rests on two independently
  written certificates (Arb ball arithmetic; outward-rounded intervals with proved truncation
  bounds). The archive, with the exact commands and expected outputs, is
  `rh-program/results/arxiv/haglund-counterexample/certificate/`; its hash is printed in the
  paper.
* **Lean.** Twelve theorems of the cubic-augmentation paper are machine-checked in Lean 4
  against a pinned Mathlib (`rh-program/lean/`; see its `README.md` for the build). `#print
  axioms` on all twelve returns `[propext, Classical.choice, Quot.sound]`.

## Not in the repository

* Third-party literature. Every external claim in the papers is cited to its published source.
* The **Zeta23** Lean formalization (Apache-2.0, Copyright 2026 Anthropic, PBC), whose home is
  <https://github.com/anthropics/zeta-23-lean>, and Alpoge and Furman's *More than two thirds
  of the zeros of the Riemann zeta function lie on the critical line* (arXiv:2608.13637). The
  Lean files in `rh-program/lean/` are additions to that library.

## License

**Apache License 2.0** for everything in this repository (see [`LICENSE`](LICENSE) and
[`NOTICE`](NOTICE)), Copyright 2026 Kunal Tyagi. The prose — the papers and notes — is
additionally offered under **CC BY 4.0**.
