# WRITER BRIEF — manuscript "A counterexample to Haglund's monotonic-zeros conjecture for the Riemann Ξ approximants" (package `results/arxiv/haglund-counterexample/`)

Written 00:10 IST 2026-10-01 (Session 37, orchestrator Fable 5.1) on the SPONSOR'S DECISION to publish the result. One WRITER (Opus, default effort);
a blind REFEREE agent and the orchestrator's read at the line follow in Session 38; posting is the sponsor's act (Zenodo + x67.ai as for the earlier
papers; arXiv needs an endorsement — `CIRCULATION-PREP.md` item 4). Follow the conventions of the earlier packages: read `results/arxiv/README.md`
(authorship: Kunal Tyagi, hello.jay.tyagi@gmail.com; the exact AI-disclosure footnote wording; the "Data and code availability" statement; no internal
vocabulary, no session references — dates or neutral phrasing only; U.S. English; `check-submittable.sh` must pass) and `results/arxiv/a4-no-go/main.tex`
as the template for structure, front matter, footnotes and bibliography style.

## What the paper proves (all on disk; every number and every theorem must be quoted from these files, not recomputed by hand)
1. **Theorem H** (the counterexample), from `results/haglund-cert-s37/NOTE.md` and the two certificates `producer-A/CERT.md` (Arb via python-flint) and
   `producer-B/CERT.md` (mpmath interval arithmetic with proved remainders): Ξ₂₇ has a real zero in (3144.8946, 3144.8947) and a non-real zero
   z₀ = 3143.220682421536585287… + 0.315258799378214845382… i in the closed first quadrant; hence Haglund's Conjecture 1 (arXiv:0910.5228; Cent. Eur. J.
   Math. 9 (2011) 302–318, Conjecture 1 p. 3 and the weak form of Remark 1 p. 4) is false for N = 27. State the two independent certifications, their
   trust bases, the ladder (Haglund's own table zeros at N = 1, 2; his appendix zero of Ξ₁), the cross-checks, and the hashes.
2. **The mechanism** (why the conjecture must fail, and where), from `results/novel-wave-s36/staircase/NOTE.md` §1–§4 as corrected by its `read-F.md`:
   Riemann's identity; Theorem D (Pólya positivity: ξ_N decreases to Ξ on the line) and Theorem D′ (the sandwich Ξ_N^{Hag} < Ξ < ξ_N; Haglund's real zeros
   lie in the positive lobes of Ξ deeper than the level Q_N, an even number per lobe plus an odd number in the central lobe — so his real-zero counts are
   odd, and his table's N = 4 entry 32 is inconsistent, the census gives 31); the 1/t² tail coefficient is negative for every N (his p. 10 says otherwise for
   k ≥ 3 — an erratum, with the numbers); the departure height ≈ 4(N+1)² and the lobe-scan picture (a shallow positive lobe below a deeper one at the
   departure height leaves an off-line pair below real zeros); Theorem A (no member of the chain other than ξ is real-rooted) and Theorem B (real-rootedness
   with polynomially bounded weights forces the weights of ξ, via Hamburger's theorem) as the structural context; Proposition F (windowed real-rootedness
   is a height filtration of RH) in one paragraph. Every proof you print must be the NOTE's proof as corrected (read-F F1–F5 applied), re-typed with care.
3. **The sibling chain** ξ₂₄ = Ξ₂₄ + c₂₄ (H5 in both certificates): the same violation at N = 24 (state it as a second instance, with its numbers).
4. Scope, stated plainly in the abstract and the introduction: the result refutes a sufficient condition for RH and says nothing about RH; the off-line
   zero belongs to the approximant, at a height where the approximant has departed from Ξ; RH is verified far above this height (cite Platt–Trudgian 2021
   for the verification height — arXiv:2004.09765; read its abstract at the page and quote the height it proves).
5. Prior art paragraph from `results/novel-wave-s36/staircase/lit/PRIOR-ART.md` and `results/haglund-cert-s37/NOVELTY-F.md`: Haglund 2009/2011 (weak form
   checked to N ≤ 10); Ahn's 2012 Penn thesis (component functions); the 2026 result on Haglund's Conjecture 4 (the pencil, k = 1) — cite it only if you
   can read its Zenodo record at the page and quote its title, author and DOI; otherwise omit it. Cite Alzergani, Liu–Matiyasevich–Oesterlé–Zaharescu,
   Lagarias–Suzuki, Ki only where the NOTE cites them and only with the statements the NOTE quotes at the page.

## Deliverables
- `main.tex` (target 8–12 pages, amsart or the a4-no-go class; theorem environments; a "Certificate" section with the exact enclosures as tables;
  a "Data and code availability" statement pointing at the public repository path `results/haglund-cert-s37/` and at the archive below), `abstract.txt`,
  `references.bib` or inline bibliography as the template does, and `main.pdf` built locally. TeX is NOT on this machine's PATH: install a user-level TeX
  (TinyTeX: `curl -sL https://yihui.org/tinytex/install-bin-unix.sh | sh`, then `~/Library/TinyTeX/bin/*/tlmgr install` the packages you need; or
  `brew install tectonic` if Homebrew works without sudo) — standing order 9: install, never skip; network calls in a retry loop.
- `certificate/` — a self-contained reproducibility archive: copies of `producer-A/` and `producer-B/` (scripts, logs, CERT.md, SHARED.md), the
  orchestrator's `verify-F/` and `rerun-F/` scripts, `NOVELTY-F.md`, a `README.md` with exact run commands and expected outputs, and `SHA256SUMS`.
  Also a `.zip` of it with its hash (Zenodo takes the zip).
- `REFEREE-BRIEF.md` (≤ 40 lines): what a blind referee must check (every theorem's proof against the NOTE; every number against the CERTs; the two
  errata against Haglund's text on disk; the citations at the page), for Session 38.
- `SHARED.md` with dated blocks. Do not touch anything outside this folder. Do not run git.

Stop and report when: a statement you must print is NOT on disk in the named files (never fill it from memory — say what is missing); the build cannot be
made to work after installing TeX (say exactly what failed).

HARD OUTPUT RULE: never write more than about 6 kB of text in a single response or tool call. Build every deliverable incrementally on disk — create the
file, then append one section (or five table rows) at a time — and append a dated block to SHARED.md after each batch. Keep reasoning between tool calls
short; think in the files, not in long messages. Your final report is under 60 lines.
