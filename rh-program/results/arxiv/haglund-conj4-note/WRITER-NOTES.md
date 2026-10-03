# WRITER-NOTES — "On Haglund's Conjecture 4 for the Riemann Ξ approximants"

## Plan (first pass, before reading the sources)

1. Read WRITER-BRIEF.md to the end; then the dual-read working note NOTE.md and every file the brief names.
2. Read the template (haglund-counterexample/v2/main.tex) for front matter, AI-disclosure footnote, bibliography style.
3. Draft main.tex section by section, appending one section per tool call, re-typing statements, proofs and numbers from the sources (no re-derivation, no hand computation).
4. Label every item by kind: proved / proved under a stated hypothesis / numerical (floating point) / heuristic.
5. Frozen-level statement: presented as known in substance, with its two citations.
6. Census table: rows final in A-track/NOTE.md and B-track/NOTE.md only, with the producing program named; re-read both just before the last build.
7. abstract.txt; build with pdflatex twice; target 6-9 pages.
8. Run the checker on this folder only; fix; record wording choices and gaps below.
9. Append a dated block to haglund-conj4/SHARED.md after each batch.

## Wording choices and gaps (filled as the work proceeds)
- W1 (front matter): AI-disclosure footnote copied verbatim from the v2 template (including "in this paper" and "the verification suite"); date line "October 3, 2026"; no acknowledgment section (the template's thanks concern the earlier paper; whether to thank J. Haglund for the question is the sponsor's call).
- W2 (§1.1): the journal wording "Conjecture 5.1 ... in the same words" and "p. 310" are from L-lit/PRIOR-ART.md §3 item 12, confirmed against the journal text on disk (novel-wave-s36/staircase/lit/haglund-CEJM-2011-degruyter-fulltext.md l. 78: the conjecture's words are identical; only the lead-in's word order "for k high enough" differs, not mentioned in the paper).
- W3 (§1.1): the sentence "a pair that leaves the axis violates (R), and also (D) just after t_0" is the NOTE's Remark 2.2 / B-track M2 ("a witness against (R), and against (D) just after"), worded by the writer.
- W4 (§1.2): "Neither (D) nor (R) is proved here for any k; Baccaro treats k = 1" — the NOTE §0 says "for any k >= 2 (k = 1 is claimed in Baccaro 2026)"; the writer chose the form that is true for every k and avoids calling Baccaro's result "proved" or "claimed" (the paper quotes his abstract instead, §7).
