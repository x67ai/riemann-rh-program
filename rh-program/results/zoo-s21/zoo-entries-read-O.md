# Zoo stream, Session 21 — READER report (Opus 5, independent second model)

**Written 2026-09-10. Brief:** `results/zoo-s21/BRIEF.md`, "Writer deliverables" paragraph.
**Writer's deliverable checked:** `results/zoo-s21/zoo-entries-proposed.md` (SHA-256 `07449e8fd03b51070149250821f6f7f53b012806fe6e1a2c4db46e2ea7274911`, re-computed this session and matching the writer's SHARED.md line), 13 blocks, inserted by `scripts/zoo-insert-s21.py` into `BARRIER-ZOO.md` and `results/corpus-routing.md`.

**Method.** Every inserted sentence was read against the record it cites, opened at the page named. Nothing below rests on the brief's paraphrase, on the writer's "Findings at the page" list, or on recall. Where a quoted phrase is load-bearing it was matched against the record's own text. The insertion itself was verified mechanically: all 13 blocks are present in the two target files verbatim (a line-by-line containment check), and `git` shows the writer's commit as 28 insertions / 0 deletions in `BARRIER-ZOO.md` and 2 / 0 in `results/corpus-routing.md` — a pure addition, as the brief requires.

**Repairs applied.** Five dated notes, additions only, appended inside the entry or rider they concern: II.1 (pointer), IV.7 (rider B), IV.11 (riders), IV.17 (STATUS), and one after the cross-reference table. `BARRIER-ZOO.md` 553 → 559 lines by this reader's edit; 6 insertions, 0 deletions; entry count unchanged at 54. (A bookkeeping note, nothing depending on it: the writer's SHARED.md records the post-insertion file as 554 lines and the pre-insertion file as 526. `wc -l` gives 553 and 525 — the file is newline-terminated, so a `split('\n')` count returns one extra empty element. The 28-line insertion is consistent either way: 525 + 28 = 553.) `results/corpus-routing.md` needed no repair and was not edited. Nothing was committed.

---

## §0. Verdict per item

| # | Item | Verdict |
|---|---|---|
| 1 | **IV.17** — the fractional-mark integrality barrier (A4), new numbered Group-IV entry | **REPAIRED** |
| 2 | **V.4** — the negative-control rule for falsification tests (B2), new numbered Group-V entry | **CONFIRMED** |
| 3 | **II.1** — one-line pointer to IV.7 rider B | **CONFIRMED** (its "until the Opus reader's check" clause discharged) |
| 4 | **IV.3** — rider: the A1 salvage-(b) price tag, with the scope guard | **CONFIRMED** |
| 5 | **IV.7** — pointer "the integrality half of the corner is IV.17" | **CONFIRMED** |
| 6 | **IV.7 rider B** — the periodic-template degeneracy, from `results/c2-m5/PRICING.md` §5 | **CONFIRMED and relabeled** `[novelty: dual-model check 2026-09-10]` |
| 7 | **IV.11 rider (i)** — DQ-M = NO, Road 2 closed | **REPAIRED** (credit line) |
| 8 | **IV.11 rider (ii)** — Route 1 DEAD | **CONFIRMED** |
| 9 | **IV.14** — KILLS rider, the ÁLKL trace formula never applies to an S4′ + clause-(0) object | **CONFIRMED** |
| 10 | **IV.16** — the four s20 §F riders (items 4, 6, 8, 9) | **CONFIRMED** |
| 11 | **Entry-count paragraph** (54) | **CONFIRMED** (recounted independently — §2) |
| 12 | **Three cross-reference rows** | **CONFIRMED** (one label update noted after the table) |
| 13 | **Formalization-queue item 10** | **CONFIRMED** |
| 14 | **`corpus-routing.md` caveat-22 addendum** (s20 §F 13–15) | **CONFIRMED** |
| 15 | **`corpus-routing.md` caveat 23** (the Platt–Trudgian exact height) | **CONFIRMED** |

Nothing is REMOVED-FROM-CLAIM. No inserted item was found to miss its grade.

### 1 — IV.17: **REPAIRED** (two scope repairs; the mathematics confirmed at every record)

Everything mathematical in IV.17 reproduces. Read and matched: `paper.md` §2.4 with revision record R1-m7 (mark-4/3 atoms on the grid of Theorem 3.9, F1 = (4/3)N budget-tight, N_d = (3/4)N < (5/6)N — against the (MI) demand 3N − (3/2)N = (3/2)N; the arithmetic (3/4)N·(16/9) = (4/3)N checks); `paper.md` line 413's Reading verbatim, including "the fractional relaxation of the marked-configuration program has a strictly smaller optimum than the integer program, so a bound proved for the relaxation is simply not a bound for the problem" and "invisible to every convexified or soft-positivity analysis"; Prop. 4.5 = `pair-channel.md` Prop. 3.1 word for word, including the vacancy lattice on grid sites g₁…g₆₄, the REAL mark μ, F1 − S2 = 2μ²ā(2d)² − 4μ(ā(d)² − 1), the numeric anchor −3.520·10⁻² at (d, μ) = (0.25, 0.05) (independently reproduced by referee-1 as −0.0352002534 by two routes), and the integer-mark safety via (T3)'s ā(d)² ≤ (1 + ā(2d))/2; the two integrality devices quoted verbatim from `pair-channel.md` §3 Reading; Lemma 2.2(a) with equality iff m ∈ {1, 2}; Thms 4.6–4.9 with the 34% margin, w ≤ 0.82 unconditional, sup Sgen2 ≤ 0.98465 on (0, 0.156]², the certified sliver failure Sgen2(0.159, 0.159) ≥ 1.01405, min F1 − T ≥ +17.46, N_d ≥ (4/9)(3M − F1), 20/27 − (16/27)ε and 5/54 ≈ 0.0926; the 0.9775 grid artifact and its withdrawal per `o1-n128-report.md` §1 and §5; referee-1 "FATAL: none", referee-2 "Findings — FATAL: None", `referee-revision.md` "PASS-WITH-REPAIRS — zero fatals; 3 distinct majors + 8 minors, ALL EXECUTED same-day"; the Zenodo concept DOI 10.5281/zenodo.22171688 with v1 record DOI …689 in `results/arxiv/README.md`.

Two repairs, both to scope in the STATUS line, both applied as a dated note:

* **The frozen public record is the PRE-revision text.** `results/arxiv/README.md` records the Zenodo v1 record at 41 pp, record date **2026-08-26**, while the on-disk `paper.md` is the 44-pp text carrying the 2026-08-27 revision and the citation pass — and the same file states that any later change is "a **public revision** … never a silent edit". So the public DOI freezes the wording that still carried the withdrawn 0.9775 full-family ratio; the 0.98465 / sliver-failure re-scoping and its two referees exist on disk only. The grade survives on the four referees, all on disk; "frozen public record" is a separate and weaker fact and must not be read as freezing the revision.
* **The "first / second integrality level" cross-reference is inverted and conflates two claims.** `theorems.md` Lemma 2.2 is titled "the two integrality levels" and its Remark states that (a), the per-zero slack (m − 1)(m − 2) ≥ 0, **is the second integrality level** — the opposite of the entry's "IV.17 is the FIRST level". And IV.8(a) is not a different level: it reads "the (m−1)(m−2) spectral level is destroyed by interactions even under RH+GUE", the same expression. The two records are compatible, but the distinction is of setting: IV.8(a) kills (m−1)(m−2) as a per-pair QUADRATIC SPECTRAL pricing under interactions, while A4 consumes it as a per-atom COUNTING inequality on the ψ₁-zero grid, where grid Parseval decouples the cross-terms into F1 = Σ m² and the pair channel is closed separately by Thms 4.6–4.9.

### 2 — V.4: **CONFIRMED**

`directions/B2-refutation-program.md` line 71 prints the experiment's own falsifier verbatim — "curves for δ = 10^{-1} and 10^{-6} should coincide — the depth-blindness signature; if they do not, the theorem's uniformity claim is in trouble, a genuine falsification channel" — and the Phase-4 block prints both critics' inversions independently, "No conflict — no adjudication needed. Consensus: survives-with-repairs, ~6.75", with mandatory repair (2) as quoted. `results/verdicts.json` supplies both lens texts word for word, including the referee's "logically inverted and would produce a false 'falsification' of a correct theorem; its cost estimate is also wrong by ~5x" and the killer's "the designated 'genuine falsification channel' would fire on a true theorem", together with the mechanism the entry states: "Depth-blindness is a property of the certificate's PRICING (Sylvester inertia charges any off-line pair n_+(Q) <= 1 regardless of depth), NOT of the measured functionals", the e^(2L·delta) self-term, and the numbers e^{2Lδ} = 4.60 at δ = 10⁻¹ against 1.0000 at δ = 10⁻⁶. The repair's "separate the moment-visible regime from an exact-arithmetic inertia/signature computation (which IS depth-uniform for every delta > 0)" is verbatim in the referee lens's repairs. The A1 companion exhibit checks too: `results/adjudication-A1.json` prints "the refutation channel is miscalibrated in the unsafe direction (would pass while the route is dead)" and "the toy numerics and the entire M0 program live where the divergent term is invisible, so the designed kill-switch cannot fire".

**The writer's correction of the brief is upheld.** The brief called V.4 a rule "extracted from a Phase-4 kill"; the record's B2 verdict is survives-with-repairs on both lenses, so "extracted from a Phase-4 FINDING (B2; not a kill)" is the right label and the writer was right to change it at the page. The rule itself is unaffected, and it is stated in the vocabulary of V.1–V.3 as a process barrier, which is what the brief asked for.

### 3–5 — II.1 pointer, IV.3 rider, IV.7 pointer: **CONFIRMED**

*IV.3.* `results/adjudication-A1.json` is `final_verdict: refuted`, `final_score: 2`, and its salvage option (b) reads verbatim "restate the direction as an explicit conditional reduction 'certificate value 2/3 + delta requires averaged-HL at window T^{c*delta}', converting the route into a sharp price tag on the M5 frontier rather than an unconditional claim"; `directions/A1-break-bandwidth.md` line 71 carries the same with "a sharp frontier marker on M5". The constant c is indeed unspecified in the record. The rider's scope guard checks against II.1's own dated block: the bandwidth-one class reaches **0.672500703679** unconditionally and is ceilinged at **0.6818287** (dual-model check 2026-09-05). The guard is the right addition — the brief's phrasing would have licensed the reading "every value above 2/3 needs averaged HL", which II.1 falsifies.

*IV.7 pointer.* IV.7's own per-zero identity is printed there as "cubic = 3F − 2 + (m−1)(m−2)" for atoms, so the pointer's parenthetical ("the (m − 1)(m − 2) ≥ 0 slack this entry's per-zero identity reads") is accurate.

*II.1 pointer.* Accurate, and correctly scoped — it says this ceiling's own content is unchanged, which is right: the two-moment rows read |c_k|² and are blind to support, and PRICING §1.2(b) says so in the same words.

### 6 — IV.7 rider B: **CONFIRMED and relabeled**. Full record in §1 below.

### 7 — IV.11 rider (i): **REPAIRED** (credit line)

The mathematics is confirmed: ledger §13's dated addendum of 2026-09-02 and `results/c3-r/s14/dqm-adjudication.md` give the non-degeneracy-free mapping-torus trace ℓ Σ_k L(h^k) δ_{kℓ}, the continuum's contribution ℓ·ind(return map, B)·δ_{kℓ} "an integer, never a Haar mass", the explicit models with weights 0, 2, 2−2g against Haar's 1, the transitive-translation-symmetry index 0, the type II transverse-measure trace with its four disqualifiers (finite packet mass, bounded mass per unit interval, evenness, blindness to null orbits), the unstatability on X₀ at rows W6/W12, three derivations (dqm-F, dqm-O, the adjudicator's), and the 2026-09-02 Session-14 date. Kim arXiv:1712.04181 Thms 2.1, 2.2, 3.2 is the C5(a) credit, with the PDF on disk.

**The Fuller citation is the wrong paper, and here the writer's correction of the brief is itself the error.** The writer's "Findings at the page" item 3 asserts that Fuller's paper is *Amer. J. Math.* 89 (**1967**), "not on disk (adjudication D6, locate-only)", and that the C3 work log's "1966" is "a date slip … not repeated". The record says otherwise. `results/c3-r/s14/novelty/adjudication.md` §(b) credits **F. B. Fuller, *The treatment of periodic orbits by the methods of fixed point theory*, Bull. AMS 72 (1966) 838–840**, quotes p. 838 verbatim ("To the set of all periodic orbits of degree d we can assign the Lefschetz number Λ(T^d), or total index of the fixed points of T^d") and p. 839's THEOREM, states "Project Euclid PDF obtained this session via WebFetch; pdftotext; saved beside this file", and its repair R4 reads "item 4: Fuller 1966 p. 838". The PDF is on disk at `results/c3-r/s14/novelty/fuller-1966-treatment-of-periodic-orbits-BAMS-72-838-ADJ-FETCH.pdf`. The "Amer. J. Math. 89 (1967), not on disk" sentence is `dqm-adjudication.md` **D6**, and D6 is a *locate-only open question about a different Fuller paper* — whether the Fuller index of a compact family of closed orbits of a flow equals ι_k of the leafwise return map on a suspension. It is not the credit line. Citing it as such would send a reader to a paper the program has never opened, and would drop the one Fuller text it did open and quote. Repaired by a dated note on IV.11.

### 8 — IV.11 rider (ii): **CONFIRMED**

Ledger §8 prints verbatim: "Hits OBSTRUCTED rows R1, R2, R4, R5, R6, R7, R8, R9, R15 (and R11–R13 independently). Every analytic ingredient of ALKL (H6–H9) lacks a counterpart, the archimedean datum is absent, and the orbit count is wrong by an uncountable factor. No repair short of replacing the space itself addresses R4/R5/R6." Ledger §6's three term-shape mismatches match the rider item for item, including the Deninger quote "in the first case it is ±1 whereas in the second it is Np^k" at [Den05] p. 27, the leafwise return Jacobian ≡ 1 versus e^{ℓ(γ)} = Np and the "symmetrizing moves the asymmetry, never removes it" clause, W_L even against W_∞ with the [Lei13] §4.4 orbifold/double-cover mechanism, and the pole term's Θ = 1 / α = 1 with [x-06] p. 8's "the class of smooth compact manifolds is too restrictive". `directions/C3-geometric-substrate.md` carries the Session-7 "Route 1 exhausted".

### 9 — IV.14 rider: **CONFIRMED**

`results/c3-r/s19/insights-digest.md` §H8 states the rider almost word for word, with the memoir's §4.1.2 p. 100 "Then M⁰ is a finite union of compact leaves because every fixed point of φ̄ is isolated", Theorem A(C1) as the forbidding mechanism, the consequence "no trace formula in print covers this object", the chain of records (adjudication §2 A-IV(α) row A11; refute-adjudication §3.3 (α); ledger §16-bis S16-5 (α)), and the dual-model attestation. Kopei's printed confirmation is `results/fetch-r4/a03-kopei.md` item 8, Remark 2.44 p. 156: "They are known only in the transverse case." The writer's reason for placing it on IV.14 rather than IV.15 (the killing mechanism is Theorem A(C1), and IV.15's EXECUTABLE TEST already checks "no justification cites the ALKL trace formula") is sound and is what the brief asked for.

### 10 — IV.16 riders: **CONFIRMED**

All four read back at the Round-5 reports, not only at the digest. §F 4: `results/fetch-r5/a02.md` prints "the word 'end' does not occur in §5 'Leaves at infinite level' (pp. 198–199)" and that every end-theorem, (6.0)–(6.4) and the p. 186 Example, carries "totally proper" or polynomial-growth domination. §F 6: `a01.md` §3.4 item 4 prints "(D5) gives only K ⊆ L̄ … It does not supply L ⊂ K" and that Theorem 1 does not reach a leaf outside X. §F 8: `a03.md` §3.1 transcribes CMH 73 Theorem 9.1 p. 329 verbatim with every hypothesis, prints "the general case remains open", and establishes on pp. 307–308 that "generic" there is Baire-residual and never measure ("In this paper, we take 'generic' in the topological sense"); the rider correctly flags its last clause as a03's inference. §F 9: `a03.md` §3.2 transcribes Dippolito's Theorem 3 (Annals 107, printed pp. 417–418) with its hypotheses — 𝒞^r, r ≥ 0, smooth leaves, a fixed transverse 𝒞^∞ one-dimensional foliation, no C², no orientability — and §3.2(c) establishes that "border leaf" is Candel–Conlon's vocabulary, not Dippolito's, while §3.2(d) closes with exactly the rider's negative: nothing there relates a boundary leaf of the completion to its endset, to C², to minimal sets, or to levels.

### 11–13 — count, cross-reference rows, queue item 10: **CONFIRMED**

The count is recounted in §2. The three cross-reference rows state their verdicts as their records do (A4: closed on the R5 family, dual-refereed both texts; C2 M5: NO-GO per PRICING §5; B2 Experiment 1: INVERTED, consensus survives-with-repairs ~6.75). Queue item 10's arithmetic was recomputed exactly: 48 atoms of mark 4/3 give M = 64, Σ m² = 48·16/9 = 256/3 = 85.33…, N_d = 48, 3M − 2N_d = 96 > 256/3 — so the configuration is a valid kernel-checkable negation of (MI) over rational marks. `mark_one_count_ge` does exist in `lean/Zeta23/PairCeiling/GridCorner.lean` as the entry claims (the file is present and the name is recorded in this suite's own IV.7 Session-8 block and in `LOG.md`). The one label update after the table is recorded in a dated note there.

### 14–15 — `results/corpus-routing.md`: **CONFIRMED**

Caveat 22's addendum: `results/fetch-r5/a04.md` prints Inaba at printed pp. 95–100 as a six-page note with one finiteness theorem and the branched-staircase construction, "names four exceptional minimal sets (its own 𝓜_S; Sacksteder's, Hirsch's and Raymond's)" and states the endset of none; Schweitzer Problem 28.1 p. 250 is transcribed verbatim with the printed C¹ caveat and with 28.2, and a04 records that the 1978 list has nothing on ends; the r5-09 theorems all carry nonexponential growth, p. 334's trichotomy prints that the finite-level leaves in the closure of an infinite-level nonexponential leaf are totally proper, and Cass's Definition 0.3 plus Example 4.1 p. 208 are as quoted. The addendum's closing "NOT BANKABLE, do not cite" clause reproduces digest §F 16–17 and correctly leaves a04's Markov inference and a02 §4's growth inference outside the claim — the writer did not carry a04's flagged "no exceptional LMS in the closure" inference either, which was the right call.

Caveat 23: `results/d1-m2a/dr8/DECISION-gomila-m2a-prime.md` §2.2 and §5 item 8 carry every figure, and I recomputed all of them exactly: 3 000 175 332 800 − 6 000 000 185 827/2 = 350 479 773/2 = 175 239 886.5; the relative surplus is 5.84·10⁻⁵; 3·10¹² − X/2 = −185 827/2 = −92 913.5; and 500 175 235 371 / 175 239 886.5 ≈ 2 854, which is the decision's "2 900× thinner".

---

## §1. Rider B's dual check

### (a) The five-line degeneracy theorem, re-derived independently

Setting, from `results/c2-m5/PRICING.md` §1.2: Σ_L = {h ≥ 0, ĥ ≥ 0, supp h ⊂ [−L, L]}; ℓ = log(T/2π); Δ = ℓ/N; u_k = kΔ; P(h) := 4Σ_n Λ(n)h(log n)/(n + 1); the periodic-model Fourier row (1.3) E_T(h) = (ℓ/N)Σ_{k≥1} Re[c_k^{on} + c_k^{pr}cosh(u_k y)]·h(u_k)/cosh(u_k/2); the row (1.2) E_T(h) ≤ P(h) + 2ĥ(T). Write hat^{(d)}_v(u) = max(0, 1 − |u − v|/d) and h_{k,d} = hat^{(d)}_0 + ½(hat^{(d)}_{u_k} + hat^{(d)}_{−u_k}).

1. **h_{k,d} ≥ 0** as a sum of nonnegative triangles.
2. **ĥ_{k,d} ≥ 0.** ∫_{−d}^{d}(1 − |u|/d)e^{−iuξ}du = d·sinc²(dξ/2) (value d at ξ = 0, matching ∫hat = d), so the shifted pair contributes d·sinc²(dξ/2)·½(e^{−iu_kξ} + e^{iu_kξ}) and ĥ_{k,d}(ξ) = d·sinc²(ξd/2)(1 + cos(u_kξ)) ≥ 0 — printed exactly so in §1.2(b). Hence **h_{k,d} ∈ Σ_L**.
3. **Zero side.** For d ≤ Δ the central tooth catches no lattice point with k′ ≥ 1 (|u_{k′}|/d = k′Δ/d ≥ 1), the −u_k tooth catches none either (u_{k′} + u_k ≥ 2Δ > d), and the +u_k tooth catches only k′ = k (|k′ − k|Δ ≥ Δ ≥ d otherwise). So h_{k,d}(u_{k′}) = ½·δ_{k′,k}, and (1.3) collapses to **E_T(h_{k,d}) = ½(ℓ/N)Re(c_k e^{iφ})/cosh(u_k/2)**, φ the rotation, c_k the combined on-line-plus-pair mode.
4. **Prime side.** Λ(n) ≠ 0 forces log n ≥ log 2, so for d < log 2 the central and the −u_k teeth catch no integer: **P(h_{k,d}) = ½·P(tooth_k^{(d)})**, with P(tooth) the same functional applied to the bare unit tooth at u_k.
5. **The row, and the limit.** Substituting into (1.2) and taking the rotation that aligns the phase: ½(ℓ/N)|c_k|/cosh(u_k/2) ≤ ½P(tooth) + 2ĥ_{k,d}(T), i.e. **|c_k| ≤ (N/ℓ)cosh(u_k/2)[P(tooth_k^{(d)}) + 4ĥ_{k,d}(T)]** — equation (1.4) exactly, factor for factor. As d → 0 the tooth's support shrinks to the single point u_k; Λ(n)/(n + 1) is bounded and the log n are isolated, so P(tooth) → 0 unless some log n equals u_k exactly (the "coincidence" clause), while ĥ_{k,d}(T) ≤ 2d → 0. Hence **c_k = 0** for every admissible k.

**Verdict: the theorem holds as printed.** Two remarks of my own.

* **A strengthening the record does not display.** At L ≥ ℓ the conclusion covers 1 ≤ k ≤ N − 1. Those c_k are the power sums p_k = Σ_z m_z z_z^k of the N points-counted-with-multiplicity on the circle (z_z = e^{−2πiθ_z/N}). With p_1 = ⋯ = p_{N−1} = 0, Newton's identities in characteristic zero give e_1 = ⋯ = e_{N−1} = 0, so the multiset is the root multiset of z^N = const: **N distinct points, uniformly spaced, each of mark 1**. PRICING's "the uniform lattice of N simple zeros" is therefore not an added reading but a consequence, with the marks forced rather than assumed. This makes the degeneracy stronger than the rider states, not weaker.
* **One precision caveat, harmless.** supp h_{k,d} ⊆ [−u_k − d, u_k + d] can exceed [−L, L] by up to d at the top index k = NL/ℓ, so strictly the row is licensed for k with u_k + d ≤ L. Since d → 0 is taken and the Newton argument needs only k ≤ N − 1, no conclusion in the rider or in PRICING depends on the boundary index.

Also checked and correct: the writer's decision to render §1.2(b)'s "disjoint from {log n} except by coincidence" as "meets the primes' frequencies {± log n} only by coincidence (none occurs at the tested heights)" rather than "disjoint" outright. §1.2(b) itself writes "which never happens for the lattice"; the weaker, exactly-supported phrasing is the right one for a zoo rider and the writer chose it.

### (b) The two verify scripts re-run

Run this session with `python3` (mpmath 1.3.0, numpy) from `results/c2-m5/verify/`.

* `two_tooth_exact.py` — **reproduces `two_tooth_exact.log` with a zero-line diff** (72 cells, all three heights, both tooth widths, all four bandwidths, three configuration families).
* `zeta_periodized_check.py` — **reproduces `zeta_periodized_run.log` identically** apart from the logged file's trailing `exit=0` line, which my redirection does not write. (Both runs emit the same three numpy `RuntimeWarning`s at line 63, which are the expected overflow in the unused deep-crystal branch and do not touch the reported cells.) Elapsed 88.0 s, of which 77.3 s is `mpmath.zetazero`.

The four numbers the rider quotes, as re-measured:

| Rider's figure | Re-run |
|---|---|
| T = 10⁶, ℓ = 11.98, period-6 crystal, k = 32, u = 1.996, \|c₃₂\| = 64 | `T=1e6 crystal d/D=1.0 L=ell/6 … worst k=32 u=1.996 \|c\|=64.00` |
| bound 4.631 at d = Δ | `bound=4.631` |
| bound 0.000 at d = Δ/10 | `d/D=0.1 … bound=0.000` |
| 198 zeros n = 3000–3197; T = 3630.911; ℓ = 6.3594; mean gap 0.98787 vs RvM 0.98802 | `zeros 3000..3197: T=3630.911 ell=6.3594 mean gap=0.98787 (RvM 2pi/ell=0.98802)` |
| L = log 2⁻: all 20 of 20 prime-free teeth violated, max \|c_k\| 2.599 | `L=log2- K=21 prime-free teeth=20 two-tooth violations=20 max\|c_k\| at prime-free k=2.599` |
| L = ℓ: 88 violations on 80 prime-free teeth, max 5.782 | `L=ell K=198 prime-free teeth=80 two-tooth violations=88 max\|c_k\| at prime-free k=5.782` |

**Every figure matches to the printed digit.** One scope note that strengthens rather than weakens the rider: PRICING §1.4(b) records that `cone_rows_check.py`'s LP optima fail an a-posteriori positive-definiteness check between grid points and are therefore "DISCRETIZED-cone indications, not certified cone elements". That caveat does not touch rider B — the two scripts re-run here use exact two-tooth cone elements whose transforms are the closed form of step (2) above, and those are exactly the evidence the rider cites. The `computationally-verified` grade is carried by the right artifacts.

### (c) The novelty claim against PRICING §4's sources on disk

PRICING §4 finding (2) reads: "No source found states the periodic-template incompatibility of §1.2(b) `[novelty: single-check]`; its ingredients (Boas–Kac cone elements as combs; Poisson summation on a periodic configuration; Fourier support of the counting measure on {± log n}) are all classical". The rider carries this faithfully, including the "bounded, single-check" framing and the ingredient list.

The three corpus items §4 leans on are on disk and were opened: `fetched/w-08-chirre-goncalves-delaat-2020-pair-correlation-via-SDP.pdf`, `fetched/w-14-carneiro-chandee-chirre-milinovich-2022-tale-of-three-integrals-crelle786.pdf`, `fetched/w-15-carneiro-chandee-littmann-milinovich-2017-hilbert-spaces-pair-correlation-crelle725.pdf`. A text-layer sweep of all three finds no periodic-configuration statement: w-15 contains no occurrence of "periodic", "periodization", "lattice" or "Poisson summation" at all; w-14's three "periodic" hits are periodizations of a TEST FUNCTION (a continuous 1-periodic P_g in the extremal problem, and the 2π-periodic Dirichlet/Fejér kernel D_n), never of a zero configuration; w-08's two "lattice" hits are E8 and Leech in its sphere-packing preamble. Nothing there states, or is one step from stating, "a periodic configuration's Fourier support is a prime-free lattice, so first-order rules cannot bind on it". The arXiv items §4 fetched (2310.01913, 1410.3926, 2212.06867, 2502.05106, 2211.14918) are, as §4 describes them, second-order Fourier-optimization or zero-free-region work with no configuration-support content.

**Honest scope of this leg.** This is a second model re-reading the SAME on-disk sources under standing order 7 — the check the brief specified — not a fresh network sweep. PRICING §4's own bounded-search caveat stands, and so does its finding (3): the ZFR regime of the cone is Heath-Brown / Kadiri / Mossinghoff–Trudgian(–Yang) territory, and only the strip-positive cone and the μ_y calculus as objects are unfound there.

### Label decision

All three legs pass. **Rider B is relabeled `[novelty: dual-model check 2026-09-10]`.** The relabel is recorded as a dated note inside the rider, with companion notes on the II.1 pointer and after the cross-reference table; the three `[novelty: single-check]` tokens already written into those places are left as written under file discipline and are superseded by the notes.

---

## §2. The count

Recounted independently of the writer and of the insertion script, by `grep -c '^### '` over `BARRIER-ZOO.md` and by an `awk` pass attributing each `###` heading to the `## GROUP` heading above it. Every `###` heading in the file is a numbered entry; there are no non-entry sub-headings at that level, so the grep count and the entry count coincide.

| Group | Headings | Range |
|---|---|---|
| I — model-world barriers | 7 | I.1 … I.7 |
| II — formalized ceilings | 5 | II.1 … II.5 |
| III — structural no-gos | 21 | III.1 … III.21 |
| IV — program-discovered barriers | 17 | IV.1 … IV.17 |
| V — process barriers | 4 | V.1 … V.4 |
| **Total** | **54** | |

**54 — I: 7, II: 5, III: 21, IV: 17, V: 4.** This agrees with the writer's count paragraph and with the writer's independent recount, and the count is unchanged by this reader's five repair notes (verified after the edit). The riders entered this session (II.1, IV.3, IV.7, IV.11, IV.14, IV.16) are not entries and move no count, as the paragraph says.

**The Session-19 slip is real and the writer's diagnosis of it is right.** The Session-16/19 paragraph reads "makes **52** — I: 7, II: 5, III: 21, IV: 15, V: 3"; those figures sum to 51. IV.16 was the sixteenth Group-IV entry, so 7 + 5 + 21 + 16 + 3 = 52 and the stated total was correct while "IV: 15" was the slip. Leaving it unedited and recording it in the new paragraph is the correct handling under file discipline.

---

## §3. What the brief required and the writer did not do

**Nothing.** Every binding item of the brief's list is on the page: A (IV.17, both paragraphs, with the IV.7 pointer and the cross-reference row), B (V.4), C1–C4 and C5b (the IV.16, IV.14, IV.11, IV.3 and IV.7-plus-II.1 riders), C5 (`corpus-routing.md`: the caveat-22 addendum for s20 §F 13–15 and caveat 23 for the Platt–Trudgian height), D (the count paragraph after the Session-16/19 one, three cross-reference rows, formalization-queue item 10). The two "writer decides at the page; say why" choices were both made and both justified: rider 3(i) placed on IV.11 because both exhaustions concern the target X₀ itself, which is IV.11's object; the ÁLKL rider placed on IV.14 because the killing mechanism is Theorem A(C1), IV.14's own theorem. The brief's out-of-scope list (§E 7–11, 14–17, 19) was respected — none of those items appears in the inserted text.

The writer's deliverables are also complete: the proposed text was written to disk before insertion and its SHA-256 matches; `scripts/zoo-insert-s21.py` exists, refuses a second run, and its output is a pure addition (0 deletions in both targets, all 13 blocks present verbatim); the SHARED.md dated block carries the hash, the entry ids and the count.

**On the writer's four corrections of the brief.** Three are upheld and one is itself wrong.

1. **V.4's label** ("Phase-4 FINDING", not "kill") — **UPHELD.** The record's B2 verdict is survives-with-repairs on both lenses.
2. **Rider 3(i)'s date and Fuller's year** — **HALF UPHELD, HALF OVERTURNED.** The date correction is right: the DQ-M adjudication is 2026-09-02 (Session 14) and the 2026-09-03 work-log line is the novelty sweep. The Fuller correction is wrong: the credit line is Bull. AMS 72 (**1966**) 838–840, opened, quoted and saved on disk; the "Amer. J. Math. 89 (1967), not on disk" is D6's separate locate-only question about a different paper. Repaired on IV.11.
3. **Rider 4's scope** (the tag prices A1's mechanism, not every value above 2/3) — **UPHELD**, and it is a real improvement on the brief: II.1's dual-model check puts 0.672500703679 above 2/3 unconditionally, so the unguarded phrasing would have been false.
4. **Rider 5b's "except by coincidence"** — **UPHELD.** PRICING §1.2(b)'s own mechanism sentence uses that qualifier, and the tested heights are where the non-coincidence was checked.

One further item the writer flagged and did not act on — the Session-19 count-line slip — was the right call (record it, do not edit it), and it is confirmed in §2.

---

## Closing honesty note

What this report rests on, and what it does not.

* **Read at the page, in this session:** `results/a4-no-go/{paper,theorems,pair-channel,o1-n128-report,referee-1,referee-2,referee-revision}.md` at every theorem, lemma, remark, quote and constant IV.17 cites; `results/arxiv/README.md`'s frozen-records table; `directions/B2-refutation-program.md` (Phase-4 block, Experiment 1, mandatory repairs) and the B2 slots of `results/verdicts.json`; `directions/A1-break-bandwidth.md` salvage block and `results/adjudication-A1.json`; `results/c2-m5/PRICING.md` §§1.1–1.4, 4, 5, 6 in full; `results/c3-r/m2c-feasibility-ledger.md` §6, §8, §13; `results/c3-r/s14/dqm-adjudication.md` (§13 addendum, D6) and `results/c3-r/s14/novelty/adjudication.md` (C5, §(b), R4, the fetch log); `results/c3-r/s19/insights-digest.md` §H8 and its Kopei line; `results/fetch-r4/a03-kopei.md` item 8; `results/c3-r/s20/insights-digest.md` §F in full; `results/fetch-r5/a01.md` §3.4, `a02.md` §3.4 and its answer block, `a03.md` §3.1–§3.2, `a04.md` §3; `results/d1-m2a/dr8/DECISION-gomila-m2a-prime.md` §2.2 and §5; `BARRIER-ZOO.md` II.1, IV.7, IV.8, the header, the cross-reference table and the queue.
* **Computed by me:** the five-line theorem re-derivation of §1(a), including the triangle transform, the tooth-catching arithmetic, the (1.4) constant, and the Newton-identity strengthening; both verify-script re-runs and their diffs against the logged outputs; the mark-4/3 arithmetic of queue item 10 (M = 64, Σ m² = 256/3, 3M − 2N_d = 96); the Platt–Trudgian margins of caveat 23 (350 479 773/2 = 175 239 886.5, relative 5.84·10⁻⁵, −185 827/2 = −92 913.5, ratio ≈ 2 854); the entry recount; the block-containment and pure-addition checks on both target files; the text-layer sweep of the three corpus PDFs.
* **Not done, and therefore not claimed.** I did not re-run A4's `verify/` scripts (the pair-channel interval certificates, the N = 128 rerun, the sliver attacks) — IV.17's numbers were checked against the on-disk report, the referees' independent re-derivations and the paper, not re-measured. I did not open the Zenodo records over the network; the pre-revision finding rests on `results/arxiv/README.md`'s own record date and page count. I did not open the ÁLKL memoir, the Kim, Fuller, Dippolito, Cantwell–Conlon, Inaba, Schweitzer or Cass PDFs; the C3 and Round-5 riders were checked against the program's own transcription reports, which quote those pages verbatim, and the reports' own "I infer" flags were respected — where a report flagged an inference, I checked that the rider did not launder it into a fact, and in every case it did not. My novelty leg for rider B is a re-reading of PRICING §4's on-disk sources by a second model, not an independent literature sweep; the `[novelty: dual-model check 2026-09-10]` label carries exactly that meaning and no more.
* **One judgment call.** The three `[novelty: single-check]` tokens now superseded by the relabel sit in the rider header, the II.1 pointer and a cross-reference-table cell. Under the never-delete rule I left all three as written and added dated notes that supersede them, including one placed after the cross-reference table because a table cell has no interior in which to append. A future reader who meets the token before the note will be one line from the correction in every case.
