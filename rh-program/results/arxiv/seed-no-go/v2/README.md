# Tate curves — revised version 2

The paper proves a classical cross-fiber matching obstruction. It withdraws the universal no-assignment conclusion of version 1. Read CHANGES.md for the precise correction.

Files:

- main.tex: complete self-contained LaTeX source.
- abstract.txt: revised title and plain-text abstract.
- anc/check_exact.py: standard-library exact finite diagnostics for lattice indices and intersection determinants; it does not decide a transcendence conjecture.
- anc/check-result.json and anc/check.log: stored successful check.
- BUILD.txt: portable two-pass pdfLaTeX instructions.
- LICENSE.txt and Apache-2.0.txt: prose and code licenses.

Reproduce: `python3 anc/check_exact.py`, then run `pdflatex main.tex` twice.

The companion archive is tate-products-v2-source-and-checks.zip. Zenodo concept DOI: 10.5281/zenodo.22171136. The old version remains available at version DOI 10.5281/zenodo.22171137. The corrected local PDF is in upload/.
