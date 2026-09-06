# repair3-log.md — Session 17 repair of `alkl23-note.tex` and creation of the sendable companion `alkl23-derivations.tex`

Repairer: Session 17 repair agent (Fable 5.1). Started: Sun Sep  6 14:49:04 IST 2026.
Inputs: `adjudication.md` (§Recommendation items 1–11, companion list C1–C9, §A/§B/§C reasons), `alkl23-note.tex`, `alkl23-note-derivations.md`, the twelve referee reports, `novelty/ALKL-2024-published.txt`.
Rule applied: every fact changed is checked against the published text or a live web query before the edit is made; no report quotation is trusted unopened.

## Task 1 — read adjudication.md in full and the note in full
- 2026-09-06 14:49 IST: Read adjudication.md in full (all sections: verdict table rows 1–22, §A N1–N6, §B N7–N12, §C C1–C10, §D D1–D7, §E O1–O9, §Recommendation items 1–11 and the companion list, §Summary). Read alkl23-note.tex in full (80 lines; §§1–5, bibliography). Read alkl23-note-derivations.md in full (222 lines, §§0–13).

## Verification of every fact touched by items 1–11 (done before editing; 2026-09-06 14:50–15:05 IST)
Published text (`novelty/ALKL-2024-published.txt`, page markers "Page k of 68"; pp. 39 and 56 also rendered from the PDF at 200 dpi):
- p. 18: "Remark 3.7 Another proof of Corollary 3.5 could be given like in Proposition 6.10." — item 9 confirmed.
- p. 22: "I^m(M,L), which becomes a Fréchet space [25, Sections 6.2 and 6.10]" — item 6 confirmed.
- p. 23: "Corollary 4.7 has extensions for ⋃_m I^m(M,L) and I_{·/c}(M,L), except acyclicity in the case of I(M,L)." — item 4 confirmed. Proof of Cor. 4.7: "I(M,L) is semi-Montel because C^∞(M\L) and S^∞(N*L_j; ΩN*L_j) are Montel spaces (Corollary 3.6)", with L_j = L ∩ U_j (p. 22) — item 9's second clause confirmed.
- p. 37: "there is a continuous inclusion x^m L^∞(M) ⊂ C^{−∞}(M)" — item 6 confirmed.
- p. 38: A^m(M) with "the projective topology given by the maps P: A^m(M) → x^m L^∞(M) (P ∈ Diff_b(M))"; "Let {P_j | j ∈ N_0} be a countable C^∞(M)-spanning set of Diff_b(M). The topology of A^m(M) can be described by the semi-norms ‖·‖_{k,m} (k ∈ N_0) given by (6.41)" — item 6 (countable family) confirmed.
- p. 40: (6.47) "Ȧ^m(M) = I^m_M(M̆,∂M) ⊂ I^m(M̆,∂M) (m ∈ R), which are closed subspaces"; §6.13 "K^m(M) = Ȧ^m_{∂M}(M)" — item 8 confirmed. p. 41: "closed subspaces of Ȧ^{(s)}(M), Ȧ^m(M) and Ȧ(M), respectively"; p. 58: "K^m(M,L) = I^m_L(M,L) ... closed subspaces" — item 8's chain K^m(M) = Ȧ^m_{∂M}(M) = I^m_{∂M}(M̆,∂M) = K^m(M̆,∂M) with subspace topologies confirmed.
- p. 46: "Corollary 6.38 A^m(M) ≡ x^m H_b^∞(M) ≡ x^{m+1/2} H^∞(M̊) (m ∈ R)"; p. 47: "Remark 6.41 Corollary 6.39 and the first identities of Corollaries 6.38 and 6.40 are independent of g. So they hold true without the assumptions (A) and (B)." — item 6 confirmed.
- p. 50: "Let 𝑴 be the smooth manifold with boundary defined by 'cutting' M along L" — item 3's "(pp. 50, 56)" confirmed. p. 56: (7.26) π_*: A(𝑴) → J(M,L); "Extend |x| to a function 𝒙 on M that is positive and smooth on M\L. Its lift π^*𝒙 is a boundary defining function of 𝑴"; (7.27) J^m(M,L) = {u ∈ C^{−∞}(M,L) | Diff(M,L)u ⊂ 𝒙^m L^∞(M)} — item 3's inserted clause confirmed.
Live record (all re-run by this agent on 2026-09-06, ~14:50–15:05 IST; raw responses kept in the session scratchpad `live/`):
- arXiv API for 2304.00798: latest v3 (2024-06-01); abs page lists v1, v2, v3; https://arxiv.org/abs/2304.00798v4 → HTTP 404. "v1 to v3 only" confirmed.
- Crossref works/10.1007/s11868-024-00617-y: update-to None, relation {}, is-referenced-by-count 0; reverse filter `updates:` → total-results 0. "carries no correction" and "Crossref ... no citing work" confirmed.
- Crossmark dialog (crossmark.crossref.org/dialog/?doi=...): the page contains "Document is current" (the JSON endpoint returns an empty body; the dialog HTML was used). Confirmed.
- zbMATH API document/7901419: identifier 1564.46031; editorial_contributions = one entry of type "summary" (text unavailable for license reasons), no review, no corrigendum; document_type journal article. "zbMATH 7901419 (Zbl 1564.46031) carries no review or corrigendum" confirmed.
- OpenAlex W4399476425: cited_by_count 0. Semantic Scholar DOI record: citationCount 0, citations []. "DOI-based citation indexes ... list no citing work" confirmed.
- Google Scholar (curl, no captcha): result "Topology of the space of conormal distributions" shows "Cited by 3"; the cites page lists exactly three: (i) "A trace formula for foliated flows", Álvarez López–Kordyukov–Leichtnam (ecommons.udayton.edu copy); (ii) "Analytic Tools", same authors, in *A Trace Formula for Foliated Flows*, 2026, Springer; (iii) T. E. Gilsdorf, *Locally Convex Spaces: Banach Space Theory, Mathematical Physics, and Distribution Theory Applications*, 2026 (book). None is a correction. "Google Scholar lists three, among them Chapter 2 of [ALKL24m]" confirmed.
- Crossref works/10.1007/978-3-032-15413-2: type book, "A Trace Formula for Foliated Flows", container Lecture Notes in Mathematics, publisher Springer Nature Switzerland, location Cham, issued 2026, created 2026-05-03, ISBN 9783032154125 / 9783032154132; chapter _2 "Analytic Tools" pp. 13–99 (its reference 2_CR11 is the paper); chapter _5 "Conormal Leafwise Reduced Cohomology" pp. 159–176. Crossref carries no series volume number.
- Springer book page (WebFetch through the idp.springer.com cookie bounce; curl is blocked by a Cloudflare challenge): "Lecture Notes in Mathematics (LNM, volume 2387)", Springer Cham, © 2026, eBook 03 May 2026, softcover 05 May 2026, ISBN 978-3-032-15413-2 (eBook) / 978-3-032-15412-5 (softcover), XI + 228 pp.; Analytic Tools pp. 13–99; Conormal Leafwise Reduced Cohomology pp. 159–176. "vol. 2387, Springer, Cham (2026)" confirmed.
- arXiv API for 2402.06671: v2 (2024-02-13), abs page lists v1, v2; no journal-ref field. Confirmed.
- Memoir pagination (pdftotext of the repo copies of v1 and v2, `fetched-r3/r3s-17-…v1` and `r3s-39-…v2`, plus a fresh download of v2 whose text is byte-identical to the repo copy): the note's memoir page numbers are the PRINTED arXiv page numbers (front matter shifts the PDF index by 6). §2.1.8 with the Cor. 3.4–3.6 restatement on printed p. 15; "2.5.10. Filtration of A(M) by bounds" and "the topologies of A(M) and C^∞(M̊) coincide on every A^m(M)" on printed p. 38; §2.6.7 header on printed p. 52 and "the topologies of J(M,L) and C^∞(M\L) coincide on every J^m(M,L)" on printed p. 53; "5.2.1. Injectivity ... compactly retractive (Section 2.2.2)" on printed p. 119; "5.5.3 ... J(F) is compactly retractive (Section 2.6.7)" and "5.5.4 ... Since I(F) is compactly retractive" on printed p. 122. Identical in v1 and v2. "the same in v1 and v2" confirmed; the "arXiv p." relabeling is correct as printed page numbers.
- Dates: today is 2026-09-06; the \date line and §5's "As of September 6, 2026" already carry today's date, so neither is changed.

### Task 2 — edits applied to alkl23-note.tex (each old string asserted present exactly once, grep -cF and str.count, before the edit)
- E1 (item 1, companion attached): line 29; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E2 (item 2): line 47; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E3a (item 3, pages): line 58; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E3b (item 3, J-membership clause): line 58; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E3c (item 11, memoir pages in (e)): line 58; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E4 (item 4): line 60; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E4b (item 11, memoir page in (f)): line 60; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E5a (item 5, constants): line 67; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E5b (item 5, epsilon-delta step): line 67; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E6 (item 6, Frechet fill): line 67; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E7 (item 7, Claim 6.46 clause): line 69; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E8 (item 8, Cor. 6.27 via (6.47)): line 69; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E9a (item 9, Remark 3.7): line 69; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E9b (item 9, Montel clause of Cor. 4.7): line 67; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E9c (item 11, memoir pages in section 4): line 69; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E10 (item 10 + item 11 clause, section 5): line 72; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E11 (item 11, bibliography): line 77; grep -cF of the old string = 1 (exactly once) before the edit; applied.
