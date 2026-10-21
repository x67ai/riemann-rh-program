# Cubic augmentation — revised version 2

The main result is exact finite N=64 atom-only absorption with an algebraically defined three-column witness. It does not prove global absorption over pair-containing or pinned classes. Read CHANGES.md for the mathematical scope and certificate corrections.

Reproduce:

1. Use Python 3 with python-flint 0.6.0 (`python3 -m pip install -r anc/requirements.txt` in an appropriate environment).
2. Run `python3 anc/certificate.py` and `python3 anc/check_cyclotomic.py`.
3. Build by running `pdflatex main.tex` twice. The default TeX Live binary directory is ~/texlive/2026/bin/universal-darwin; override TEXLIVE_BIN if needed.

The exact input in anc/witness-data.json contains integer mark vectors and exact decimal-rational parameters. The certificate uses no rounded floating-point rows and no feasibility grace. The three equalities defining the weights are algebraic identities; Arb checks only the strict inequalities and inertia signs. Counts at 2,3,4 plus monotonicity prove the all-threshold ladder. certificate-result.json records its strict bucket margins and exact objective fractions. check_cyclotomic.py uses only standard-library integer arithmetic and proves that two selected Frobenius rows are irrational in the cyclotomic field.

main.tex is the full manuscript source. Table 1 specifies the same input mark vectors as the JSON. Stored outputs and logs are under anc/. The new witness is computer-assisted, not a new Lean formalization. Historical v1 records and code remain at the original record and public tag paper-2026-08-28.

Companion archive: cubic-augmentation-v2-source-and-checks.zip. Zenodo concept DOI: 10.5281/zenodo.22171688; old version DOI: 10.5281/zenodo.22171689; existing Hexagon record: 2610.00252. The corrected local PDF is in upload/.
