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
- W5 (§2, Lemma 2.2 proof): added the clause "then the argument of Lemma 2.1 applies to kappa_t" — the NOTE's proof cites "Lemma 1.1" for this step; no new mathematics.
- W6 (§2, Thm 2.4(b) proof): c_1 = sum_{n>=2}(4 pi n^2 - 1)e^{-pi n^2} >= Q_1(0) is taken from the earlier paper (v2/main.tex l. 317 definition of c_N, l. 493-494 "Q_N = c_N - P_N <= c_N <= c_1"); the NOTE writes only "c_1 (the paper, Corollary odd)". 0.4971 from NOTE §2 / v2 l. 493.
- W7 (§3): "proof kept short" — the NOTE's proof of Prop. 3.2 is re-typed with light compression; every step of the NOTE (incl. F2a boundary values, F2b argument bound) is kept. The attribution of "no horizontal tangent" to CS (3.3)-(3.4) and of the direction to Lemma 3.1 follows PRIOR-ART §4(b) ("this unit's one-line reading ... not a sentence of theirs").
- W8 (§3): Conjecture 1 is described in one parenthesis (Haglund p. 3, as quoted in the earlier paper) because the NOTE refers to it without definition.
- W9 (§4): the NOTE's last sentence of "Reading" ("Conjecture 1, by contrast, fails for a reason unrelated to the zeros of Xi") is omitted; the mechanism is already stated in §3.
