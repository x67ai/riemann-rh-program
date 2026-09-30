# SHARED.md — writer's log for `results/arxiv/haglund-counterexample/`

Dated blocks, newest last. Writer: Opus 5.5 (default effort), on `WRITER-BRIEF.md`.

## 2026-10-01 00:09 IST — start

- Read `WRITER-BRIEF.md`, `results/arxiv/README.md`, `check-submittable.sh`.
- TeX: the brief says TeX is not on PATH. It is not on PATH, but a user-level TeX Live 2026 is
  already installed at `~/texlive/2026/bin/universal-darwin` (pdfTeX 1.40.29), exactly as
  `results/arxiv/README.md` "Building" records, and `check-submittable.sh` prepends that directory
  itself. Verified: amsart, amsthm, hyperref, booktabs, mathtools, microtype, lmodern present.
  No install needed; build with `export PATH="$HOME/texlive/2026/bin/universal-darwin:$PATH"`.
- Next: read the template, then the source files named in the brief.
