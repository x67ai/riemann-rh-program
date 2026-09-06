# VERIFICATION 2 of `alkl23-note.tex` — the repair pass after rechecks F and O

**Date:** 2026-09-06 (Session 16, direction C3-r). **Verifier:** O (Opus 5), independent of the repairer
(Fable 5.1) and of both rerecheckers. Scope as instructed: **only the changes the repairer made**, plus the
consequences those changes have for lines they touch.

**What I opened, with what tool.** The current `alkl23-note.tex` and the git diff against `HEAD`
(`git diff HEAD -- results/c3-r/s14/alkl23-note.tex`; the working tree was not yet committed, so the diff is
the full repair). `alkl23-note-REVISION2.md`, `alkl23-note-recheck-F.md`, `alkl23-note-recheck-O.md`,
`w3-adjudication.md` §§3.4 and 3.8. Sources: the published PDF
(`novelty/ALKL-2024-topology-conormal-distributions-PUBLISHED-JPDOA-15-47.pdf`, text layer split on form
feeds, plus 170–500 dpi `pdftoppm` renders of pp. 18, 19, 22, 23, 39, 47, 56, 57, 59 where symbols matter,
**and a per-glyph font extraction of p. 56 via `pdftohtml -xml`**); arXiv v1 (`fetched-r3/r3s-18`), **v2
(`fetched-r3/r3s-37`) and v3 (`fetched-r3/r3s-38`)** as downloaded by the repairer this session; memoir v1
(`r3s-17`) and **v2 (`r3s-39`)**, plus a font extraction of v3 p. 45. Live re-checks run by me today:
`arxiv.org/abs/2304.00798`, `arxiv.org/abs/2402.06671`, `api.crossref.org`, `api.semanticscholar.org`,
`api.zbmath.org`. Rebuild: TeX Live 2026 (`/Users/jaytyagi/texlive/2026`), `pdflatex` twice, in a scratch copy.

---

## 0. VERDICT

### **FIX-FIRST — one fix, one line, then send.**

Every other change the repairer made is **true against the source and correct**: I re-verified E1 by my own
word-level diff of §§3–4 across v1/v2/v3 and by extracting each cited statement; I re-derived witness (d)
end to end under the new hypothesis and both displays are unchanged and correct; the semi-Montel sentence
agrees with the binding record; the density clause, the Prop. 7.26 rewrite, the memoir pages, the §5 facts
(all four re-checked live by me today) and the bibliography all check out; the build is 3 pages, zero
overfull, zero underfull, no warnings, and its text is identical to the shipped PDF. No repair was declined
without a valid reason.

**The one defect — introduced by the repair (item E7).**

Witness (e), `alkl23-note.tex` line 58 / PDF p. 2:

    Since $J^m(M,L)$ is given by (7.27) with $\Diff(M,L)$ and $\boldsymbol x^mL^\infty(\boldsymbol M)$,
    $\boldsymbol M$ the manifold with boundary obtained by cutting $M$ along $L$ and $\boldsymbol x$
    extending $|x|$ (p.~56), …

**(7.27) does not have a bold *M*.** It reads `Diff(M, L) u ⊂ 𝒙^m L^∞(M)` — **bold x, ordinary M**. The
repair fixed the `x` correctly (that half of F7 was right) and over-corrected the `M`, so the note now
misquotes the equation in the other direction, in the very sentence whose purpose is to quote it exactly.

*Evidence (decisive, not a judgement of glyph weight).* Per-glyph font extraction of published p. 56
(`pdftohtml -xml`): on the `J^m` line of (7.27) the token `x` is set in `SKYXXQ+Times` — the bold-italic
subset, used on that page only for the six bold `M`s and three bold `x`s (e.g. "boundary defining function
of **𝑴**, also denoted by **𝒙**") — while the token `M` inside `L^∞(M)` is `QGWBFT+Times`, the same regular
subset as the `M` in `Diff(M, L)` on the same line. arXiv v3 p. 45 says the same thing in Computer Modern:
`x` in **CMMIB10** (bold math italic), `M` in **CMMI10** (regular). A 500-dpi render of the line agrees.
(So `alkl23-note-recheck-F.md` F7's "bold x and bold M" is half wrong, and REVISION2's E7 note "(7.27) reads
… with BOLD x and BOLD M" repeats the error. The mathematics is untouched: 𝒙 is a function on `M`, and
`L^∞(M)` is exactly what the paper writes.)

**Exact fix** (keeps `\boldsymbol M` introduced, since §4 still uses it in "`$J^m(M,L)\cong A^m(\boldsymbol
M)$ by (7.26)`"):

    OLD: with $\Diff(M,L)$ and $\boldsymbol x^mL^\infty(\boldsymbol M)$, $\boldsymbol M$ the manifold with
         boundary obtained by cutting $M$ along $L$ and $\boldsymbol x$ extending $|x|$ (p.~56),
    NEW: with $\Diff(M,L)$ and $\boldsymbol x^mL^\infty(M)$, $\boldsymbol x$ the extension of $|x|$ to $M$
         whose lift is a boundary defining function of the manifold with boundary $\boldsymbol M$ obtained
         by cutting $M$ along $L$ (p.~56),

(Any wording works provided `L^\infty(M)` is unbolded and `\boldsymbol M` is still defined for §4. If a
shorter line is wanted, write `$\boldsymbol x^mL^\infty(M)$, $\boldsymbol x$ extending $|x|$ (p.~56)` and
restore the §4 clause "`, where $\boldsymbol M$ is the manifold with boundary obtained by cutting $M$ along
$L$`" that E7 removed.)

**Two optional nits (not blocking, my judgement: leave them).**
1. (d) now uses `N` for the neighborhood while `N_0 ∈ ℕ_0`, `2N_0 ≥ \bar m''`, `Δ^{N_0}` sit two lines below;
   an italic `N` and an italic `N_0` next to each other read ambiguously for a moment. `V` or `N_1` would
   remove it. Nothing is wrong as written.
2. The margins were cut to `hmargin=0.6in, vmargin=0.5in` to hold three pages. The measure is now ~7.3 in
   (about 100 characters), dense for 11 pt. It is legible and the page budget was a requirement, so I would
   ship it; if the three-page cap is soft, 0.7 in reads better.

---

## 1. Line-by-line table — every changed line

"Changed" = every hunk in `git diff HEAD -- results/c3-r/s14/alkl23-note.tex`. Verdicts: **TRUE** = the new
statement checks out against the source I opened; **OK** = correct/harmless (layout, notation, index range);
**FIX** = must change before sending.

| # | Item | Changed text (new) | What I checked, and where | Verdict |
|---|---|---|---|---|
| 1 | preamble | `hmargin=0.75in,vmargin=0.65in` → `0.6in/0.5in` | Layout only; rebuild holds 3 pp. with no content cut. | OK (nit 2) |
| 2 | `\date` | September 5 → **September 6, 2026** | Not earlier than §5's date; consistent. | OK |
| 3 | after `\maketitle` | `\vspace{-2.5em}` → `-2em` | Renders: date line and "1. Purpose." now separated. | OK |
| 4 | §1, E1 | "arXiv:2304.00798**v2 and v3** carry the same numbering, and every **proposition, corollary, remark and equation** cited here from §§3–4 has the same number and wording in all three arXiv versions" | (i) *v2 = v3 in §§3–4*: I extracted §§3–4 (heading "3. Symbols" → "5. Dual-conormal distributions") from both text layers, normalized, diffed: **0 differences**. (ii) *v2/v3 carry the published numbering*: the statement lists of v2 and v3 are identical and match the published (Props. 6.10, 6.12, 6.29, 7.26, 8.8; Cors. 6.14, 6.15, 6.16, 6.21, 6.22, 6.27, 6.28, 6.39, 7.13, 7.14, 7.15, 7.17, 7.22, 7.23, 7.31; Claim 6.46; Remarks 6.17, 6.41), whereas v1 has Prop. 6.10 = seminorms, Cors. 6.12/6.19/6.25/7.11/7.20; and published (6.29), (6.33), (6.38)–(6.43), (6.45), (6.47), (6.49), (7.26), (7.27) all carry the same content in v3. (iii) *every cited §§3–4 item identical in v1/v2/v3*: with running heads stripped I compared, character for character, **Prop. 3.2 + proof, Prop. 3.3 + proof, Cor. 3.4 + proof, Cor. 3.5 + proof, Cor. 3.6 + proof, Remark 3.8 (through the p. 18 bundle paragraph), Cor. 4.5 + proof, Cor. 4.7 + proof, (3.1), (3.4), (3.5), (4.8), (4.9), (4.10)** — all identical in v1, v2, v3 (and the bundle sentence identical in the published text too). (iv) *my own v1↔v2 §§3–4 word diff*: 43 non-equal opcodes, all in the `U = R^0` sentence, Remark 3.7 ("Proposition 6.8"→"6.10"), §4.2.2 (Fréchet→LCHS), Sect. 4.3.3 wording, §§4.6–4.8 with (4.21)–(4.24)→(4.20)–(4.22), and running-head noise — i.e. **none** in a cited numbered item. The narrowing to numbered items is *necessary*: Sect. 4.3.3, which (f) cites, was reworded at v2. | **TRUE** |
| 5 | §2, E3a | "…Cor. 3.6 (p. 18) for every non-compact `U` **and every `l ≥ 1`**" | Published p. 15: "The canonical coordinates of `R^n × R^l` (`n, l ∈ N_0`)", and (3.1) has weight `(1+|ξ|)^{m-|β|}`. For `l = 0` only `β = 0` occurs and the weight is 1, so `S^m(U×R^0) = C^∞(U)` for every `m`: the spectrum is constant, hence acyclic and Montel, and Cor. 3.6 is **true**. The restriction is required, and (f)'s witness `χ_j(x)(1+|ξ|²)^{j/2}` degenerates at `l = 0`. | **TRUE** |
| 6 | §2, E3b | bundle clause split: "extends Prop. 3.2 and Cor. 3.4 to symbols on a vector bundle, **and its extension of Cor. 3.6 when the base manifold is non-compact** (… and the extension of Cor. 3.6 over a compact base is true, §4)" | Published p. 18 sentence read in full ("Propositions 3.2 and 3.3 and Corollaries 3.4 to 3.6 can be directly extended to this setting"); the sentence is word-identical in v1/v2/v3/published. Witness (a) is local in one trivializing chart and constant in the base, so the Prop. 3.2 / Cor. 3.4 extensions fail over **any** base; (f)'s supports must escape every compact set, so the Cor. 3.6 extension fails only over a non-compact base; the note's own §4 proves the compact-base case. The split is exactly right and removes a real overclaim. | **TRUE** |
| 7 | §2, E3c | "Cor. 4.5 (p. 23), for every compact `(M,L)` with **`L ≠ ∅`** and `codim L ≥ 1`" | Witness (d) needs a chart meeting `L`; for `L = ∅`, `I(M,∅) = C^∞(M)` and Cor. 4.5 is vacuous. Cor. 4.5 is on published p. 23 (checked). | **TRUE** |
| 8 | §2, E3d | "The witnesses **(a)–(e)** below are constant in the base variable up to a fixed cut-off, …; **(f) is inherently non-local.**" | (a)–(c) are literally `x`-constant; (d), (e) carry a fixed bump `g`; (f)'s `χ_j` moves with `j` by construction. | **TRUE** |
| 9 | (b), E10 | `\sum_{i\le j}` → `\sum_{1\le i\le j}` | Makes the lower limit visible; `c_i = (1+iR)^{m+1}` and the disjointness argument are unaffected. | OK |
| 10 | (d), E2 — setup | "`L ≠ ∅` … Take a chart `(U_1, x=(x',x''))` adapted to `L` **and meeting `L`**, `x: U_1 → U'×U''` (p. 19), **`g ∈ C_c^∞(U'')`**, `g ≢ 0`, and the partition of unity `{h,f_i}` of (4.10) with `f_1 = 1` and `h = f_i = 0` (`i ≥ 2`) **on a neighborhood `N` of the compact set `x^{-1}({0}×supp g) ⊂ L`** (… `ρ = 1` **on `N`**…)" | Chart convention verified on published p. 19 (`x = (x',x''): U → U'×U''`, `L_0 = L∩U = {x'=0}`); (4.10) and `{h,f_j}` subordinate to `{M\L, U_j}` verified on p. 22. "Meeting `L`" gives `0 ∈ U'`, so `{0}×supp g ⊂ U'×U''` and `x^{-1}({0}×supp g)` is a compact subset of `L∩U_1`; a relatively compact open `N` around it inside `U_1` exists, and `ρ ∈ C_c^∞(U_1)` with `ρ = 1` on `N` exists. The replacement family sums to 1 (`(1-ρ)(h+Σf_i) + ρ = 1`) and stays subordinate to the same cover (`supp(ρ+(1-ρ)f_1) ⊂ U_1`), and equals `{0,1,0,…}` on `N`. `p_0` is gone; nothing else in the witness refers to it. This is precisely the gap both rereaders found, and it is closed. | **TRUE** |
| 11 | (d), E2 — display | `u_j = j^{n'+\bar m'} g(x'')ψ_*(jx')` (the "` ∈ C^∞(M) ⊂ I^m(M,L)`" moved out of the display) | Cosmetic relocation; see next row for the claim itself. | OK |
| 12 | (d), E2 — support sentence | "For `j` large, `supp u_j ⊂ x^{-1}({|x'| ≤ 1/j} × supp g) ⊂ N`, so `u_j ∈ C_c^∞(U_1) ⊂ C^∞(M) ⊂ I^m(M,L)`, `hu_j = 0` and `f_i u_j = 0` (`i ≥ 2`), and by (4.8) the symbol of `f_1u_j = u_j` is …" | Re-derived. `supp ψ_* ⊆ supp ψ ⊂ {|x'|<1}` (the Laplacian does not enlarge support), so `supp u_j ⊂ x^{-1}({|x'|≤1/j}×supp g)` — the note's `⊂` is right, `=` would not be. These compacta decrease in `j` with intersection `x^{-1}({0}×supp g)`, so a decreasing family of compacta inside the open `N` is eventually inside `N`: "for `j` large" is exactly what is needed and is enough. Hence `u_j ∈ C_c^∞(U_1)`, extends by zero, and `hu_j = f_iu_j = 0` (`i ≥ 2`) because those vanish on `N` — so the (4.10)-image is `(0,(a_j,0,…))` and the two-term computation below is legitimate. `C^∞(M) ⊂ I^m(M,L)` for every `m` (smooth ⇒ symbol in `S^{-∞}`, cf. (4.12)). **The witness now goes through; before the repair it did not.** | **TRUE** |
| 13 | (d) — both displays | unchanged text; re-derived under the new hypothesis | (4.8) gives `a_j(x'',ξ) = j^{n'+\bar m'} g(x'') · j^{-n'} \hatψ_*(ξ/j) = j^{\bar m'} g(x'')\hatψ_*(ξ/j)`; `∂_{x''}^α∂_ξ^β a_j = j^{\bar m'-|β|}∂^αg·(∂^β\hatψ_*)(ξ/j)`; with `ξ = jη`, `(1+|ξ|)^{|β|-\bar m_1} = j^{|β|-\bar m_1}(1/j+|η|)^{|β|-\bar m_1}`, and the two suprema factor — giving **exactly** the printed identity `‖a_j‖_{K,α,β,\bar m_1} = j^{\bar m'-\bar m_1}\sup_K|∂^αg|·Φ_{β,\bar m_1}(j)`. Upper bound for `\bar m_1 ≤ 2N_0`: `|β| ≥ \bar m_1` ⇒ weight `≤ (1+|η|)^{|β|-\bar m_1}`, Schwartz decay; `|β| < \bar m_1` ⇒ weight `≤ |η|^{|β|-\bar m_1}` and `|∂^β\hatψ_*| ≤ C|η|^{2N_0-|β|}` near 0 ⇒ product `≤ C|η|^{2N_0-\bar m_1} ≤ C` on `|η| ≤ 1`, `≤ C` for `|η| ≥ 1`. With `\bar m_1 = \bar m''`: `‖a_j‖ ≤ Cj^{\bar m'-\bar m''} → 0` (`\bar m' < \bar m''` since `m̄ = m + n/4 - n'/2` is increasing in `m`), so `u_j → 0` in `I^{m''}`. Lower bound: `Φ_{0,\bar m'}(j) ≥ |\hatψ_*(η_0)|(1/j+|η_0|)^{-\bar m'} ≥ c > 0`, and `‖a_j‖_{K,0,0,\bar m'} = \sup_K|g|·Φ_{0,\bar m'}(j) ≥ c\sup_K|g| > 0`, so `u_j ↛ 0` in `I^{m'}`. **Both displays unchanged and correct.** | **TRUE** |
| 14 | (d), E2/E8 | "for any `η_0 ≠ 0` with `\hatψ_*(η_0) ≠ 0`" | Necessary: `min{(1+|η_0|)^{-\bar m'}, |η_0|^{-\bar m'}}` is undefined/zero at `η_0 = 0`, and `N_0 = 0` is admissible whenever `\bar m'' ≤ 0`, where `\hatψ_*(0) = ∫ψ` may be non-zero. Such an `η_0` exists: `\hatψ_* = (-|η|²)^{N_0}\hatψ` with `\hatψ` a non-zero real-analytic function. | **TRUE** |
| 15 | (e), E8 | `m' < m` → **`m' ∈ R`** | Removes a flat self-contradiction: nothing in the computation needs `m' < m` (`sup x^{-m'}|u_j| ≥ 1` for every real `m'`), and the paragraph legitimately uses `m' = m` (Prop. 6.12, published p. 39: one order) and `m' < m` (Cor. 6.14, p. 39: two orders). Both statements re-read on p. 39. | **TRUE** |
| 16 | (e), E10 | `{x < 1/2j}` → `{x < 1/(2j)}` | `supp u_j ⊂ {1/(2j) < x < 2/j}`, so the (6.43) seminorms vanish for every `j`. | OK |
| 17 | (e), E10 | `\inf_i` → `\inf_{i\ge1}` | `e^i i^{-k}` needs `i ≥ 1` to be defined and the infimum positive; matches (c)'s `\inf_{j\ge1}`. | OK |
| 18 | (e), E7 | "(7.27) with `Diff(M,L)` and **`𝒙^m L^∞(𝑴)`**, `𝑴` the manifold … and `𝒙` extending `|x|` (p. 56)" | (7.27) has **bold x and ORDINARY M** — established by per-glyph font extraction of published p. 56 (`x` in the bold-italic subset `SKYXXQ+Times`; `M` in the regular `QGWBFT+Times`, identical to the `M` of `Diff(M,L)` on the same line) and of arXiv v3 p. 45 (`x` CMMIB10, `M` CMMI10), plus a 500-dpi render. The `𝒙` half of the repair is right; the `𝑴` half misquotes. "`𝑴` the manifold with boundary obtained by cutting `M` along `L`" (published p. 50) and "`𝒙` extending `|x|`" (p. 56, "Extend `|x|` to a function `𝒙` on `M`…") are both accurate. | **FIX** (see §0) |
| 19 | (e), E5 | "(`[2]` restates these second assertions at §2.5.10, p. 38, and §2.6.7, p. 53.)" | Memoir **v1 and v2** both: §2.5.10 "Filtration of `A(M)` by bounds", pdf p. 44, running head "38 2. ANALYTIC TOOLS" — "[ÁLKL23, Corollaries 6.14–6.16 and 6.39 and Remark 6.41]: the topologies of `A(M)` and `C^∞(M̊)` coincide on every `A^m(M)`" = the second assertion of Cor. 6.14. §2.6.7 "The space `J(M,L)`", the sentence on pdf p. 59, running head "2.6. CONORMAL SEQUENCE 53" — "the topologies of `J(M,L)` and `C^∞(M\L)` coincide on every `J^m(M,L)`" = the second assertion of Cor. 7.13. Both are refuted by (e)'s `v_j`. Printed pages 38 and 53 confirmed from the running heads in both versions. | **TRUE** |
| 20 | (f), E9 | "`n ≥ 1`, **and let `l ≥ 1`**" | Same evidence as row 5. | **TRUE** |
| 21 | §4, E2 | `f_j → f_i`, `λ_j → λ_i` (two places) | Notation only; `grep` finds no stray `f_j`/`λ_j`. Matches (d)'s `f_i`. | OK |
| 22 | §4, E7 | "`J^m(M,L) ≅ A^m(𝑴)` by (7.26)" — the definition of `𝑴` deleted here | Correct only while (e) still introduces `𝑴`; the §0 fix keeps that. (7.26) verified on published p. 56 and in v3. | OK *(depends on the §0 fix)* |
| 23 | §4, E10 | "to finite products **of spectra each satisfying it**" (was "with constant spectra") | True: given `k`, take `k' = max_i k'_i`; coincidence of the `X_{k'_i}`- and `X_{k''}`-topologies for all `k'' ≥ k'_i` forces coincidence of the `X_{k'}`- and `X_{k''}`-topologies on the same set, and the product of the `0`-neighborhoods is a `0`-neighborhood of the product. The old wording was ambiguous (the (4.10) product has one constant factor and non-constant symbol factors). | **TRUE** |
| 24 | §4, E4a | "**Several** printed arguments use a coincidence statement for more than the word 'acyclic'. The semi-Montel step of the printed proof of Cor. 3.6 (p. 18) applies Cor. 3.4 to a bounded subset `B` of some `S^m`; what it needs is the bounded-set statement, which is true: for `m' > m`, `S^{m'}`- and `C^∞`-convergence agree on bounded subsets of `S^m(U×R^l)`, so, with `m' > m` in place of `m` and bounded retractivity in hand, the step goes through." | Printed step read on published p. 18: "Since `S^∞(U×R^l)` is boundedly retractive, `B` is contained and bounded in some `S^m(U×R^l)`, and the topologies of `S^∞` and `S^m` coincide on `B`. By Corollary 3.4, it follows that `B` is a complete bounded subspace of `C^∞(U×R^l)`" — so the note's description of the step is exact. The bounded-set statement is **TRUE** and is exactly what `w3-adjudication.md` §3.8 records as binding (O Lemma 6.5.2, CONFIRMED): for `a` in a bounded `B ⊂ S^m`, `‖a‖_{K,α,β,m'} ≤ max(C_{α,β}R^{m-m'}, (1+R)^{|β|-m'}‖a‖_{K×B̄_R,C^{|α|+|β|}})`, whose first term → 0 as `R → ∞` precisely because `m' > m`; the converse direction is automatic. The note's sentence **does not contradict the binding record** and states it in the record's own form. The repair is sound. | **TRUE** |
| 25 | §4, E4b | "The density Cors. 6.15 and 7.14, whose printed proofs are modeled on Cor. 3.5's, follow instead from Prop. 6.10 and its `J`-analogue, or from Cors. 6.39 and 7.17 (Remarks 6.17 and 6.41 and their analogues on p. 57)." | All numbers and pages verified in the published PDF: Cor. 6.15 p. 39, preceded by "The proofs of the following results are similar to the proofs of Propositions 3.2 and 3.3, Corollaries 3.4 to 3.6, using (6.33)" (so "modeled on Cor. 3.5's" is right); Remark 6.17 p. 39 "Proposition 6.10 provides an alternative direct proof of Corollary 6.15. Actually, it will be shown that `C_c^∞(M̊)` is dense in every `A^m(M)` with its own topology (Corollary 6.39 and Remark 6.41)"; Prop. 6.10 p. 37 (direct proof, no coincidence statement); Cor. 6.39 p. 47; Remark 6.41 p. 47 ("Corollary 6.39 is stronger than Corollary 6.15"); Cor. 7.14 p. 56; Cor. 7.17 p. 57; and **both** analogues on p. 57 ("The analog of Remark 6.17 makes sense for `J(M,L)`", "The analog of Remark 6.41 makes sense for `J(M,L)`"). | **TRUE** |
| 26 | §4, E10 | `\chi(\xi/R)` → `\rho(\xi/R)` "with the `ρ` of (f)" | `χ` was undefined in §4 and collided with (e)'s `χ ∈ C_c^∞((½,2))`, which is *zero* near 0; (f)'s `ρ ∈ C_c^∞`, `ρ = 1` near 0, is the right cut-off for `‖a - ρ(ξ/R)a‖_{K,α,β,m'} ≤ CR^{m-m'}`. | OK |
| 27 | §4, E10 | "by Prop. 7.26 every element of **`K(M,L)`** is a finite sum of Dirac layers `∂_x^kδ_L ⊗ v_k`, whose local symbols are polynomials in `ξ` **with the `v_k` as coefficients, so it lies in `K^m(M,L)` iff `v_k = 0` for `k > \bar m`**" | Published p. 59: (7.36) `⊕_{m≥0} C^1_m → K(M,L)`, `C^1_m = C^∞(L;Ω^{-1}NL)`, and Prop. 7.26 "The map (7.36) is a TVS-isomorphism, which induces TVS-isomorphisms (7.37)" — so the finite-sum statement is about `K(M,L)`, not `K^m(M,L)`; the old text attributed the degree bound to Prop. 7.26, which it does not state. The new "iff" is the note's own (correct) symbol computation: the symbol of `∂_x^kδ_L⊗v_k` is `c_k v_k(x'')ξ^k`, homogeneous of degree `k`, terms of different degrees cannot cancel, and a degree-`k` polynomial symbol lies in `S^{\bar m}` iff `k ≤ \bar m`. | **TRUE** |
| 28 | §5, E10 | "As of **September 6, 2026** … arXiv lists versions v1 to v3 only, the Crossref record of the DOI carries no correction, zbMATH 7901419 carries no review or corrigendum, and Semantic Scholar lists no citing work (**all four re-checked on that date**); Unpaywall listed no correction DOI on September 3, 2026." | **Re-run live by me today.** arXiv `abs/2304.00798`: v1 3 Apr 2023, v2 29 Jul 2023, v3 1 Jun 2024, no v4. Crossref `10.1007/s11868-024-00617-y`: `relation {}`, no `update-to`, no `updated-by`, `is-referenced-by-count 0`. Semantic Scholar (by DOI): `citationCount 0`. zbMATH API document 7901419 (= Zbl 1564.46031): `document_type` journal article, `review` null, the single editorial contribution is a `summary` with `reviewer.name` null and its text withheld under zbMATH's license, `links` only the DOI and arXiv — no corrigendum. The split of the Unpaywall claim onto its own date is honest and correct. | **TRUE** |
| 29 | bib [2], E6 | "arXiv:2402.06671 (**v2, 13 February 2024**; the pages cited are the same in v1)" | arXiv live today: v1 Wed 7 Feb 2024, v2 Tue 13 Feb 2024. Memoir v1 and v2 compared: §2.1.8 "Symbols. For any open `U ⊂ R^n` and `l ∈ N_0`…" on pdf p. 21, running head "…15"; §5.2.1 "because `I(F)` is compactly retractive (Section 2.2.2)" pdf p. 125, head "…119"; §§5.5.3–5.5.4 pdf p. 128, head "122 5. CONORMAL LEAFWISE REDUCED COHOMOLOGY"; the same three uses of compact retractivity and no others. So the parenthetical "the pages cited are the same in v1" is true. | **TRUE** |
| 30 | bib layout | `\vspace{-0.5em}` → `-1em`; `\small` → `\footnotesize` | Layout only; bibliography still sets on p. 3 with slack. | OK |

### Declines — were any of E1–E10 dropped without a valid reason? **No.**

* **E1 — applied in narrower wording.** Valid, and in fact *required*: the orchestrator's draft ("every
  statement … unchanged") would have been false, because Sect. 4.3.3 — which witness (f) cites by name — was
  reworded between v1 and v2 ("Corollary 4.7 can be extended with" → "has extensions for"), and §§4.6–4.8
  were rewritten with (4.21)–(4.24) → (4.20)–(4.22). Restricting the claim to numbered propositions,
  corollaries, remarks and equations makes it exactly true (row 4).
* **E4 — the "copies" clause not written.** Valid as far as it goes. I read the printed proof of Cor. 4.7
  (published p. 23): it obtains semi-Montel from the *closed* TVS-embedding (4.13) into a product of Montel
  spaces, "and this property is inherited by closed subspaces and products" — **not** from the bounded-set
  step; Cors. 6.22, 6.28 and 7.23 follow that route. *One correction to the repairer's rationale, which does
  not change the outcome:* Cors. **6.16** and **7.15** *are* copies of Cor. 3.6's step (p. 39: "The proofs of
  the following results are similar to the proofs of Propositions 3.2 and 3.3, Corollaries 3.4 to 3.6, using
  (6.33)"; p. 56: "the following analogs of Proposition 6.6 and Corollaries 6.7 and 6.14 to 6.16 hold true").
  The note is still accurate — it says "Several", not "these and no others", and its first §4 paragraph
  already re-proves all six Montel clauses by its own route ("…and then of their Montel clauses"). No change
  needed; recorded so the point is not rediscovered.
* Every other item (E2, E3, E5–E10) was applied in full; I found each edit present in the source and true.

### Build

Scratch copy, TeX Live 2026, `pdflatex` twice: **3 pages**, `Pages: 3`, letter; the log contains **no**
`Overfull`, `Underfull`, `LaTeX Warning`, or `!` line at all. `pdftotext -layout` of my rebuild versus the
shipped `alkl23-note.pdf`: **byte-identical text**. 110-dpi renders of all three pages read: no broken
symbols (`\mathring M`, `\breve M`, `\boldsymbol M`, `\boldsymbol x`, `\varrho`, the `‖·‖'` primes, `\ind`,
`\Diff_b`, `\Delta^{N_0}`, `\hat\psi_*`, accented `Álvarez López`), display (1) numbered and referenced, the
footnote and the three-item bibliography set on p. 3 with slack, no orphaned heading, nothing off the measure.

---

## 2. What I did **not** re-verify

1. **Unpaywall** — not re-fetched (its API requires an e-mail parameter). The note's sentence is dated
   September 3, 2026 and attributed separately, which is the honest form; nothing to fix.
2. The **zbMATH review text** is withheld by the API under a license notice; "no review" rests on
   `review: null` and `reviewer.name: null`. Unchanged from the previous version of the note apart from the
   date.
3. Lines the repairer did **not** touch were outside my brief; I re-derived only what the changed lines
   depend on (witness (d) in full, the (e) transfer to Cor. 7.13, the semi-Montel step, the Prop. 7.26
   sentence). The unchanged material was verified by both fresh rereaders in the same session.
4. **`\boldsymbol M` in the memoir / bundle-valued spaces** — as recheck O noted, the "covered by the above"
   sentence for `I(F)`, `J(F)` assumes the scalar argument localizes to bundle coefficients; unchanged text,
   not in my scope.

---

## 3. For the program record (not the note)

`alkl23-note-recheck-F.md` F1's evidence line — "(7.27) reads `Diff(M,L) u ⊂ 𝒙^m L^∞(𝑴)` with bold x and
bold M (p. 56, rendered)" — and `alkl23-note-REVISION2.md` E7's confirmation of it are **wrong about the M**.
Per-glyph font extraction of published p. 56 and of arXiv v3 p. 45 shows bold `x`, ordinary `M`. If those two
files are kept as the audit trail, they should carry a dated correction, and the fix in §0 applied to the
note.
