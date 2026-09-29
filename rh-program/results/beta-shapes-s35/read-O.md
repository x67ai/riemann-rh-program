# β-SHAPES — READER (Opus 5) — `read-O.md` (Session 35; started Tue Sep 29 16:05 IST 2026, machine clock)

Read: `BRIEF.md` in full (the READER section binding); `NOTE.md` §0–§6 (SHA-256 17717f151638618ab6f026d896cc632c955ce6c0c1db6cf4c60ff2a25eb0aff5, identical to `NOTE.pre-reader.md`); `SHARED.md` Blocks 1–5; `verify/numbers-check.log`. Sources at the page: SPEC A5, A7, A8, A9, A11, A13 (f7553e52…); E3 NOTE §0, §3 (Theorems 3.3–3.4, "On Z (H5)"), §4, §5, §6 (d71fb8a0…); Borger 0906.3146 pp. 5, 7–8, 24–28 (§1.2, §2.1, §7.2–7.8, §7.7 WHOLE, Cor. 7.6 p. 27); Borger 1006.0092 Prop. 16.5 (d) with proof (`results/zoo-s27/prior-art/S27-1006.0092.txt`); Milne 1509.00797 pp. 9–11; Durov 0704.2030 p. 43; Connes–Consani 1805.10501 pp. 17–18 and 1603.03191 p. 1; the Deninger extractions x-04, x-17, x-18, x-20, x-21, x-03, z-19 at every page the note cites; zoo (8e66cdc0…) I.1, III.20 (STATEMENT and riders), III.21, IV.10, IV.11–IV.16, V.1, V.5 and the Group-IV header and count paragraphs; digest s28 line 266 and s32 line 302. Everything numerical re-derived in `verify-O/` (Python 3.x, mpmath 1.3.0 at 30 digits, sympy 1.14.0). U.S. English. No file of the writer's edited; nothing committed.

## 1 Verdict table

| Row | Verdict | Ground (details in §2) |
|---|---|---|
| §1 exhaustiveness | **AGREE WITH ONE FIX (F10–F11)** | The two-predicate split is a partition of TRIPLES by the excluded middle; the one triple in no cell is one whose diagonal row is not real-valued — A11 as printed names no value group, and §1.3's proof silently assumes "real-valued". Such a triple fails A9 by type, so nothing is lost, but the Claim must say it. No triple is in two cells except (D2) ⊂ (D1), as stated. One β may carry triples in several cells; harmless because (D1)–(D3) are empty. |
| Lemma F (§2.0) | **AGREE — PROVED** | (a)–(c) re-derived; the only input is the finiteness of the real number κ(Δ·D) (A9 with real A11 values) and Λ ≥ log 2 on prime powers. |
| T1 (§2.1) | **AGREE — PROVED** | Lemma F(b) + three sub-cases; subterminal ⟺ diagonal iso; Durov p. 43 quoted exactly. Rung 1 untouched (Fr_q of infinite order). |
| T2 (§2.2) | **AGREE — PROVED** | (a) 16.5(d) read at the page; (b) the J-lemma, the clipping map and the [1, N] index count re-derived and recomputed (index(L_N) = N! by exhaustive enumeration N ≤ 8, the Legendre product N ≤ 40); the zero-divisor survives localization at every prime of Γ_n; (c) by T1. Proposition 2.2.1(i) needs the parametrization c|Γ_n = (id, φ_n) as a stated part of A7 (M8, not load-bearing). |
| T3 / Theorem R (§2.3) | **AGREE — PROVED from A5 + A9 (real-valued, one fixed κ) + H3.3; does NOT kill rung 1** | Re-derived line by line (§2.5). Uses A9's real-valued finiteness (through Lemma F(a)), never a Z-valued form; both are stated in H3.2. A7 is idle in Theorem R. The fixed κ is essential (with κ_D depending on D the theorem fails). Converse proved by the reader: dim_Q G ≤ |char(B)|, so dim_Q G < ∞ ⟺ char(B) finite (M1). Corollaries 3.1–3.2 PROVED. Routes (a), (b) PROVED in the stated sub-cases; (b)(i) can be sharpened (M10). |
| E4 | **AGREE (re-derived)** | Hodge index on a finite-rank Num gives inequalities (Milne p. 9 (5), p. 9–10 (6)); the Lefschetz form is a tautology for Weil's σ (Milne p. 11) and its content — multiplicativity on a finite-dimensional space — needs composition through C × C × C (Milne pp. 10–11), and A13 item 4 over Z supplies the tower only (SPEC A13 "OVER Z: items 1 and 4 present as data on X (Λ(n))"). Precision M9. |
| §3 clauses A8′ / A11′ / A13′ | **AGREE WITH ONE FIX (F9)** | A8′: (Γ_f)² = −(2g − 2) deg f re-derived from Milne Ex. 1.7 (with f = π: q(2 − 2g), [O8]). A11′ in §3.2 states "G infinite-dimensional" unconditionally, which is FALSE on rung 1 and contradicts its own "rung-1 specialization" line; the §5 SPEC version is correctly conditional. A13′: item 3′'s Selberg ground matches III.20's STATEMENT; items 2′/4′ read on rung 1 through their stated specializations. |
| §3 nearest objects | **AGREE; three additions (M2, M7)** | Every Deninger, Connes–Consani, Durov quotation found at the page named (`verify-O/quote-check.log`), with two slips: x-04 2.7 prints "canononical" (the note silently corrected it — F13) and x-17's "Finally we expect …" begins on p. 4 (F14). Missing and relevant: Borger §7.7 p. 27 "Of course this makes essential use of equal characteristic" (the printed remark at Theorem R's exact coordinate); x-18 p. 4 "the N γ are not all powers of the same number" (Corollary 3.2's twin); CC 1603.03191 p. 1 "real valued dimensions". IV.11–IV.16 STATEMENTS matched by first words. Stop line (iii) correctly not fired. |
| §3 ladder (§3.5) | **AGREE IN SUBSTANCE, FIX-FIRST ON ONE PHRASE (F1)** | "(2) … infinitely many residue characteristics" is right; "(4) … a base with at least two residue characteristics (so that Theorem R bites)" is wrong — over a base with finitely many residue characteristics dim_Q G ≤ |char(B)| < ∞ and Theorem R is silent. The same slip recurs six more times (F3–F8). |
| §3.7 candidate object | **AGREE (NO), GROUND CORRECTED (F2–F4, F6, M12)** | The s28 definition's own gloss says "the SPEC supplies the axioms and the rung-1 model, and no candidate for the target over Z is on the record": a candidate is a PROPOSED target over Z. (D4) is a shape, not a proposal. The writer's ground "no rung-1 model" is imprecise: the primed axioms keep the curve pair as rung-1 model in (D3) form; what no lower rung can test is their (D4) content. |
| §5 close | **AGREE WITH FIXES (F4–F6, F12)** | Close and verdicts stand; the candidate sentence (F4), the Untried item (a) (F5), the Instruments row (F6) and one KILLS overclaim in the staged IV.20 (F12: "Deligne-style rationality" killed only with integer traces; (D4-fin) open by the note's own §3.4). |
| staged lines | **Option A (IV.20) — YES, with M4–M7 and F12**; C3 lines with F6, F7, M12; SPEC lines AGREE (A11′ in §5 already conditional; row-P1 precision verified: N!·Z^N ⊆ L_N at the line) | See §4. Under Option A the IV.10 rider of Option B (the Z-form of E3 Theorem 4.1(b)) should still be inserted as a rider: it is a scope change on IV.10 that IV.20 does not carry. |

**Overall: AGREES-WITH-CORRECTIONS.** No theorem is wrong and none kills rung 1. 29 OLD/NEW pairs (14 FIX-FIRST, 15 recommended), all verified by script to occur exactly the stated number of times in NOTE.md and to apply cleanly (`verify-O/apply_check.py` → `apply-check.log`: ALL OK; residual "at least two / ≥ 2 residue characteristics" after application: none).

## 2 The checks

### 2.1 Exhaustiveness (brief item 1)
Attempted counterexamples. (i) A triple satisfying A6–A8, A11 whose pairing takes values in a group that is not a subgroup of R (a p-adic or formal value group): P₂ is undefined, so it lies in no cell — the only "β in none" I can build. It fails A9 by type (the left side of A9 is a real number, κ > 0 real), so it is outside the question, but §1.3's proof says "A8 and A11 supply the real-valued pairing", and A11 as printed (SPEC line 52) does not say "real". FIX F10–F11. (ii) A β carrying two triples in different cells (e.g. one with φ_p = id, one non-degenerate): the shapes are properties of triples, the note's Claim is correctly about triples, but §0 and the theorem statements say "no β of shape (Di)". Harmless — every triple over every β lies in exactly one cell and (D1)–(D3) are empty — and recorded inside F10. (iii) "In two": only (D2) ⊂ (D1), as the note says. (iv) P₁ is well defined for every A7 family (finite order is a property of each φ_p). Verdict: a partition of the triples with real diagonal row; exhaustive by the excluded middle; stop line (ii) correctly not fired.

### 2.2 Lemma F (§2.0)
(a) #F_D · log 2 ≤ Σ_{F_D} log p = L(D) = κ(Δ·D) ∈ R, so F_D is finite ([O1]; [11] of the writer). (b) the induction φ_p^{a+jm} = φ_p^a re-derived; D := c(Γ_{p^a}) (p^a ≥ 2, so A9 applies) has an infinite fiber — contradiction. (c) re-derived. Rung 1: Fr_q has infinite order (x ↦ x^{q^k}, 0906.3146 p. 25 at the page) and fibers are the finitely many effective divisors of a degree (p. 25). PROVED.

### 2.3 T1 (§2.1)
Re-derived; θ(10⁴) = 9895.99137916 and 30031 = 59 · 509 recomputed [O1]. Durov p. 43 quotation exact (0.6.13–0.6.14, page 43 of the extraction). Separating hypothesis H1.2 correct. PROVED.

### 2.4 T2 (§2.2)
(a) 1006.0092 Prop. 16.5 (d) at the page (extraction line 1817/1844: "The ghost map w_{⩽n}: W_n(A) → A^{[0,n]} is integral and surjective on spectra; so the Krull dimension of W_n(A) agrees with that of A^{[0,n]}, which is d"). (b) Independently recomputed [O7]: index(L_N) found by enumerating the finite quotient for N = 1..8 equals the product of the moduli equals N!; v_d ∈ L_N and det(v_d) = N!; N!·e_n ∈ L_N for N ≤ 40; the product of moduli equals N! for N ≤ 40 (Legendre). The zero-divisor argument is local as it must be: for s outside a prime of Γ_n, s_n ≠ 0 and s · N!e_n = s_n N! e_n ≠ 0, so the witness survives localization. Box levels [O7b]: J = Π p^{1+b_p} works; the smaller Π p^{b_p} also works (the note's J is safe, not sharp; no amendment). (c) by T1. Proposition 2.2.1(i): the equivariance computation is right given c|Γ_n = (id, φ_n) under Γ_n ≅ B; A7 fixes the image, not the parametrization; M8 states it. PROVED.

### 2.5 Theorem R and T3 (§2.3) — attacked hardest (brief item 2)
*Line by line.* W := κG is the Q-span of {log N_D}; this uses Lemma F(a) at every D = c(Γ_n), n ≥ 2 — i.e. A9 with a REAL right side and ONE κ. V := ⊕_ℓ Q log ℓ is direct by unique factorization (re-derived: Σ c_ℓ log ℓ = 0 with c_ℓ ∈ Q, clear denominators, Π ℓ^{m_ℓ} = 1 with m_ℓ ∈ Z, so all m_ℓ = 0). If dim W = r < ∞, W is spanned by r of the log N_{D_i}, so every element of W has support in the finite set S = ∪ supp(log N_{D_i}). For every prime ℓ, Λ(ℓ) = log ℓ > 0 puts ℓ in the fiber of c(Γ_ℓ), so ℓ | N_{c(Γ_ℓ)} and ℓ ∈ S. Contradiction with the infinitude of primes. Correct.
*What it uses.* A5 (Λ on prime powers), A9 with real values and one fixed κ > 0, Euclid, unique factorization. It does NOT use a Z-valued form (Corollary 3.1 does, and says so), Hodge index, adjunction, Lefschetz, rationality, Hadamard or Littlewood. A7 is idle in Theorem R (the fibers of c on components suffice); the hypotheses are stated in H3.2, but the one-κ dependence deserves a sentence: if A9 allowed κ_D to depend on D, the target could set every value to 1 and G = Q — so Theorem R is exactly as strong as A9's one normalization (M1). SPEC A9 prints one κ ("κ the normalization of the arithmetic degree … over Z … κ = 1"), so the hypothesis is the SPEC's, not an addition.
*Converse (reader).* supp(log N_D) ⊆ char(B) for every D (Λ_B is supported on log N(𝔪), N(𝔪) a power of the residue characteristic), so dim_Q G ≤ |char(B)|. Hence dim_Q G < ∞ ⟺ char(B) finite: (D4) is empty over any base with finitely many residue characteristics. This is what makes the note's "at least two residue characteristics" (7 places) wrong (F1, F3–F8), and it turns E6's sentence into a theorem (M1).
*Rung 1.* char(S) = {ℓ}; fiber products q^{N_N} recomputed from scratch on y² = x³ + x + 1 over F₇ [O8]: #E(F₇) = 5, trace 3, N_k = 5, 55, 380, 2475, closed points 5, 25, 125, 605 — E3's numbers. G = Q, dim 1 ≤ |char| = 1. Theorem R is silent; T3 does not kill rung 1. Stop line (i) not fired.
*Corollary 3.1* re-derived (N_p^{m_q} = N_q^{m_p} ⇒ proportional exponent vectors ⇒ equal support ∋ every prime). The brute-force count: the writer's 18 233 counts pairs N ≤ M; the reader's 18 472 counts ordered pairs — 17 994 diagonal cases + 2 × 239 off-diagonal = 18 472, and 17 994 + 239 = 18 233: consistent; 0 mismatches either way [O6].
*Routes.* (a) the Vandermonde/base-1 argument re-derived; the coefficient at λ = 1 is 1 − log p/κ + [d_p = 1] − #{χ_i(p) = 1}, so log p/κ ∈ Z_{≤2}; first failure p = 11 at κ = 1, p = 5 at κ = log 2 [O2]. (b) (i) n = pq: d + 1 ≤ 2g√d ⟺ d ≤ C_g, recomputed [O4]; the note's "at most ONE prime has d_p > C_g" is true but weak — since d_q ≥ 1 for the second prime, NO prime has d_p > C_g, and g = 0 dies at once (M10). (ii) the sufficient bound k > 2 log((2g + 1) + log p/κ)/log d verified against the exact first violating k for 27 cases [O3]. (iii) first failing primes 59, 409, 162779 (κ = 1; g = 1, 2, 5) and 17, 67, 4099 (κ = log 2) [O2]. General fibers: heuristic, as the note says; Littlewood correctly non-load-bearing.
*DH / negative control.* Correct: T3 is RH-blind; Λ_DH(12) = −0.7628774719884, Λ_DH(3) = −0.3120927285, Λ_DH(4) = −1.442231965 recomputed from the a_n (mod 5) recursion [O13] — the SPEC's digits.
**Verdict: Theorem R and T3 PROVED; the hypotheses are exactly A5 + A9 (real values, one κ) + H3.3; no extra hypothesis hides; rung 1 is not killed.**

### 2.6 E4 (brief item 3) — AGREE, by re-derivation
Milne p. 9: Hodge index ⇒ index 1 on N(V) (Cor. 1.3); p. 9 (5) Castelnuovo–Severi; p. 9–10 (6) the defect inequality; p. 10 Ex. 1.7 (7). Nothing there produces a trace with finitely many eigenvalues. On p. 11 Weil's σ(D) = d₁ + d₂ − (D·Δ) makes the "identity" a definition; the content — σ(D ∘ D′) as the trace of a product on a finite-dimensional space — rests on composition D₁ ∘ D₂ = p₁₃*(p₁₂*D₁ · p₂₃*D₂) (p. 10 bottom), which needs C × C × C, and on the ring R(C) (p. 11). A13 item 4 over Z is "present as data on X (Λ(n))" (SPEC A13 OVER Z), not rationality. So (H-Lef) is an extra hypothesis. The note's E4 cites "Milne p. 10" for the composition; the formula straddles pp. 10–11 (inside M9).

### 2.7 Quotations (brief item 4) — `verify-O/quote_check.py` → `quote-check.log`
Found at the page named: Borger p. 5 (caveat), p. 7 (§1.2), p. 8 (§2.1), p. 25 (§7.3, both sentences), p. 27 (§7.7); Milne p. 9 (form, Cor. 1.3), p. 10 (Ex. 1.7, "(∆ · Γπ) = number of points …"); Durov p. 43; CC 1805.10501 p. 17 (13), p. 18 (14) and the "key missing step" sentence; x-20 pp. 8, 9, 22, 24; x-21 pp. 3, 12, 14; x-18 pp. 1, 4, 5, 6 (the explicit formula (2) at p. 5 checked character-level against the extraction); x-17 pp. 1, 10; x-04 pp. 2, 5 (Thm. 2.13), 6; x-03 p. 5 = z-19 p. 5. **Slips:** x-04 p. 3, 2.7 prints "There is a canononical anti-linear automorphism" — the note corrected the typo inside quotation marks (F13, [sic]); x-17 "Finally we expect a C-antilinear Hodge ∗-isomorphism …" begins on p. 4 and ends on p. 5 (F14). **Borger §7.7 read whole** (p. 27): the note lists it as read but quotes none of it; it is the printed free slot the brief names and contains the sentence "Of course this makes essential use of equal characteristic" — the printed remark at Theorem R's coordinate (M2, M7).

### 2.8 Zoo citations by first words — `verify-O/zoo_check.py` → `zoo-check.log`
All 26 cited strings found inside the named entries (three "MISS" lines in the log are markdown only: IV.13 "**B1** (dual-check)…", IV.12 "**Theorem T** (Opus 5 adjudicator…", IV.14 "`f1-check-O.md` §4.4" — the STATEMENT first words match). III.20 "Deligne's squeeze additionally needs RATIONALITY …", "Selberg has (B)-shape without (A)'s tower", "NEVER acts on the zeta's own explicit formula"; IV.13 "is Z-linearly independent (unique factorization)"; IV.10 R-b′ and the E3 rider's scope sentence; III.21; I.1 THE CCM CASE STUDY; V.1; V.5 — all exact. The zoo holds IV.1–IV.19 (count paragraph of Session 34: Group IV 19), so IV.20 is the next free number.

### 2.9 Novelty (standing order 7) — the reader's independent search
`verify-O/arxiv_O.sh` (15 queries) and `arxiv_O2.sh` (5 queries), https, one request at a time, 3 s apart, once-a-minute retry loop; raw responses `arxiv-O.xml`, `arxiv-O-2.xml`; parsed `arxiv-O-parsed.txt` (16:13:09–16:14:35 IST). Positive controls PASS: abs:"lambda-rings" AND abs:"field with one element" → 3 (0906.3146 first); abs:"arithmetic site" → 15 (1405.4527, 1502.05580, 1507.05818, …, 2606.06604). Non-control hits: 1603.03191 ("scaling site" + "Riemann-Roch"), 1502.05580 ("Frobenius correspondences" + RH), 1204.3129 ("Weil proof" + "Spec Z") — all on disk and on the record; grep of the three texts for index / rank / genus / independent / Hodge / Castelnuovo finds no statement of Theorem R, Lemma F, Proposition 2.2.1, Corollaries 3.1–3.2 or T2 (b) over Z. The other 16 queries returned 0 (queries listed in `arxiv-O-parsed.txt`). **Flip: every `[novelty: single-check]` label of the note (Lemma F; T1's general form; Proposition 2.2.1; T2 (b) over Z; Theorem R with Corollaries 3.1–3.2; the staged IV.20 and riders) → `[novelty: dual-model check 2026-09-29]`** (M2–M5, M11), scoped as the note scopes it: the arithmetic core (Q-independence of {log p}) is classical and is not claimed; V.5 governs what a null search licenses.

### 2.10 Numbers — `verify-O/numbers_O.py` → `numbers-O.log` (independent code; 10 s)
Every number in NOTE §4 recomputed and agreeing to the digits printed: Λ(2..30); ψ, θ, π at 10, 10², 10³, 10⁴; 30031 = 59·509; the route-(a)/(b) first primes; the first violating k (27 cases) and the sufficiency of the note's k-bound; C_g for g = 1, 2, 3, 5, 10 with the floor checks; the κZ-hit lists (0 / 16 / 6 / 4) and dist(e^m, Z) for m ≤ 12; the proportionality count (reconciled in §2.5); index(L_N) = N! (enumeration N ≤ 8) and the Legendre product (N ≤ 40); five boxes; rung-1 counts from scratch; 29 zeros below T = 100 (mpmath.nzeros) with the first five ordinates; ψ(x) − x at 10²…10⁶; the DH witnesses (not recomputed by the writer; recomputed here). Randomized illustration of Theorem R [O12]: the Q-rank of {log N_D} equals the rank of the exponent matrix and grows with the number of finite fibers. Lint of NOTE.md: no "clearly / obviously / easy to see / well known" outside §6.3's own list; "towards" occurs only inside a paper title (Lorscheid) — a quotation, kept.

## 3 OLD/NEW amendments (exact; machine-applicable from `verify-O/amendments.py`; checked by `verify-O/apply_check.py`)

Apply each OLD → NEW once (M5: both occurrences). FIX-FIRST = F1–F14 (apply before any staged line is inserted); recommended = M1–M12. The orchestrator re-derives each FIX-FIRST at the line before applying (brief, "On completion").

**F1 (FIX-FIRST).**
OLD:
```
What a (D4) rung would have to be: a base with at least two residue characteristics (so that Theorem R bites) and a target
```
NEW:
```
What a (D4) rung would have to be: a base with infinitely many residue characteristics (Theorem R with its converse, §2.3: over a base with finitely many, dim_Q G ≤ |char(B)| < ∞, so (D4) is empty there — two residue characteristics do not make Theorem R bite) and a target
```

**F2 (FIX-FIRST).**
OLD:
```
It does NOT have (b) a rung-1 model: rung 1 is (D3)-shaped by Theorem R's arithmetic (one residue characteristic), no infinite-genus pair is on the record on any rung (§3.5), and the only base on which (D4) can be tested is the arithmetic case itself.
```
NEW:
```
Its axioms keep the SPEC's rung-1 model only in (D3) form: the curve pair satisfies A8′, A11′, A13′ in their rung-1 specializations (δ_S = 2g − 2; G = Q · log q; h = 2g), but it is (D3)-shaped by Theorem R's arithmetic (one residue characteristic), so it tests the reduction of the primed clauses to A8, A11, A13 and never their (D4) content; no infinite-genus pair is on the record on any rung (§3.5), and by Theorem R with its converse (§2.3) the only bases on which (D4)'s content can be tested have infinitely many residue characteristics — the arithmetic case itself. And the thing the s28 definition asks to be PROPOSED is absent: its own gloss reads "the SPEC supplies the axioms and the rung-1 model, and no candidate for the target over Z is on the record" (`results/program-digest-s28.md` line 266) — a candidate object is a proposed target (β, Y, c) over Z, and (D4) is a shape such a proposal must have, not a proposal (§0; V.1).
```

**F3 (FIX-FIRST).**
OLD:
```
**a base B with at least two residue characteristics for which a target (β, Y, c) satisfying A6, A7, A9, A11′ and A8′/A13′ is KNOWN**
```
NEW:
```
**a PROPOSED target (β, Y, c) of shape (D4) over a base B with infinitely many residue characteristics (Spec Z or a number ring) satisfying A6, A7, A9, A11′ and A8′/A13′ — with no rung below the arithmetic case on which its (D4) content could first be checked**
```

**F4 (FIX-FIRST).**
OLD:
```
The candidate-object question is NO: (D4) has axioms and a written DH failure (A5, unchanged) and no rung-1 model, and it can have none — rung 1 is finite-rank by the arithmetic of one residue characteristic; the missing piece is a base with at least two residue characteristics on which a (D4) target is KNOWN, and no page prints one.
```
NEW:
```
The candidate-object question is NO: the s28 candidate is a PROPOSED target over Z ("the SPEC supplies the axioms and the rung-1 model, and no candidate for the target over Z is on the record", `results/program-digest-s28.md` line 266), and (D4) is a shape, not a proposal; the amended axioms keep the curve pair as their rung-1 model only in its (D3)-shaped specialization, because by Theorem R and its converse (D4)'s content lives exactly over bases with infinitely many residue characteristics — the arithmetic case — so no lower rung can test it; no page prints a (D4) target.
```

**F5 (FIX-FIRST).**
OLD:
```
(a) a (D4) rung — a base with ≥ 2 residue characteristics carrying a KNOWN target (§3.5)
```
NEW:
```
(a) a (D4) rung — a base with infinitely many residue characteristics carrying a KNOWN target (§3.5)
```

**F6 (FIX-FIRST).**
OLD:
```
candidate object NO (no rung; the rung would be a base with ≥ 2 residue characteristics)
```
NEW:
```
candidate object NO (no proposed target over Z; (D4)'s content is testable only over bases with infinitely many residue characteristics — the arithmetic case)
```

**F7 (FIX-FIRST).**
OLD:
```
(a) a (D4) rung — a base with at least two residue characteristics carrying a KNOWN target
```
NEW:
```
(a) a (D4) rung — a base with infinitely many residue characteristics carrying a KNOWN target
```

**F8 (FIX-FIRST).**
OLD:
```
the rung for (D4) is a base with ≥ 2 residue characteristics
```
NEW:
```
the rung for (D4) is a base with infinitely many residue characteristics
```

**F9 (FIX-FIRST).**
OLD:
```
NEW (A11′): the same, plus: the pairing is real-valued; its diagonal-row span G is infinite-dimensional over Q; and for every prime p
```
NEW:
```
NEW (A11′): the same, plus: the pairing is real-valued; over a base with infinitely many residue characteristics its diagonal-row span G is infinite-dimensional over Q (over a base with finitely many, dim_Q G ≤ |char(B)| and this part of the clause is void — which is what lets the rung-1 specialization below hold); and for every prime p
```

**F10 (FIX-FIRST).**
OLD:
```
**Claim.** Every triple (β, Y, c) satisfying A6, A7, A8 and A11 lies in exactly one of (D1), (D3), (D4); (D2) is a named sub-shape of (D1).
```
NEW:
```
**Claim.** Every triple (β, Y, c) satisfying A6, A7, A8 and A11 whose diagonal-row intersection numbers (Δ · c(Γ_n))_Y, n ≥ 2, are real numbers lies in exactly one of (D1), (D3), (D4); (D2) is a named sub-shape of (D1). (A11 as printed does not name the value group; A9's equation with a real κ > 0 forces real diagonal-row values, so a triple whose diagonal row is not real-valued fails A9 by type and needs no theorem — it is the only triple outside the four cells, and it is outside the question. The shapes are properties of TRIPLES: one β may carry triples in several cells, which is harmless because (D1)–(D3) are empty.)
```

**F11 (FIX-FIRST).**
OLD:
```
A8 and A11 supply the real-valued pairing on Y's divisor classes
```
NEW:
```
A8 and A11 supply the pairing on Y's divisor classes, and the Claim's hypothesis makes its diagonal row real
```

**F12 (FIX-FIRST).**
OLD:
```
any brief presenting Deligne-style rationality (finitely many eigenvalues of fixed weight) as available on a square of Spec Z;
```
NEW:
```
any brief presenting Deligne-style rationality (finitely many eigenvalues whose traces are integers — a characteristic polynomial over Z, (H-Lef_Z)) as available on a square of Spec Z (finitely many transcendental eigencharacters with non-injective c — the sub-shape (D4-fin) of NOTE §3.4 — is NOT killed);
```

**F13 (FIX-FIRST).**
OLD:
```
p. 3, 2.7: "There is a canonical anti-linear automorphism
```
NEW:
```
p. 3, 2.7: "There is a canononical [sic] anti-linear automorphism
```

**F14 (FIX-FIRST).**
OLD:
```
p. 5: "Finally we expect a C-antilinear Hodge
```
NEW:
```
pp. 4–5: "Finally we expect a C-antilinear Hodge
```

**M1 (recommended).**
OLD:
```
*Proof of T3.*
```
NEW:
```
**Converse, and the hypotheses the proof actually uses (reader, 2026-09-29).** Under H3.1–H3.2 every N_D has its prime support inside char(B) (Λ_B is supported on the log N(𝔪), and N(𝔪) is a power of a residue characteristic), so dim_Q G ≤ |char(B)|; with Theorem R, dim_Q G < ∞ exactly when char(B) is finite — (D3) is the finite-characteristic case and (D4) is non-empty only over bases with infinitely many residue characteristics. The proof reads only the fibers of c on components: A7's graph structure is not used (it enters Lemma F(b)–(c), not Theorem R). The ONE fixed κ of A9 is used: with a normalization κ_D allowed to depend on D, every value could be 1 and the theorem fails; H3.2 states the fixed κ, as SPEC A9 prints it. *Proof of T3.*
```

**M2 (recommended).**
OLD:
```
`[novelty: single-check]` — arXiv searches recorded in SHARED.md; nothing found by title words (§6.1).
```
NEW:
```
(5) Borger 0906.3146 §7.7 p. 27 (read at the page by the reader): "So, objects of F^S_1 are generalized—but not weakened—versions of separated reduced algebraic spaces over the point Spec k. Of course this makes essential use of equal characteristic. The corresponding interpretation of Λ-spaces in the usual sense, over Z, would be that while it is possible to say what it means to descend an algebraic space to F1—that is, to give it a Λ-action—we do not know if there is a uniformity property, which is what we would need to create a true arithmetic analogue of the base point Spec k." — the printed free slot, and the printed remark that rung 1 uses equal characteristic; exact difference: Borger's remark is about descent (a uniformity PROPERTY), Theorem R is a theorem on the pair's PAIRING at the same coordinate (one residue characteristic versus infinitely many). (6) x-18 p. 4: "So the foliation setting allows for a product formula where the N γ are not all powers of the same number." — Corollary 3.2's dynamical twin (on rung 1 every fiber product is a power of q). (7) Connes–Consani 1603.03191 abstract, p. 1: "prove the Riemann-Roch formula which involves real valued dimensions, as in the type II index theory" — a printed real-valued invariant on the per-prime orbit C_p = R*_+/p^Z, not a pairing on a square. `[novelty: dual-model check 2026-09-29]` — writer's 22 arXiv queries (SHARED.md, §6.1) and the reader's 20 (`verify-O/arxiv-O-parsed.txt`, positive controls passing); nothing prints Theorem R, Lemma F or Proposition 2.2.1; the arithmetic core (Q-linear independence of {log p}) is classical and is not claimed.
```

**M3a (recommended).**
OLD:
```
`[novelty: single-check]` for Lemma F as a statement
```
NEW:
```
`[novelty: dual-model check 2026-09-29]` for Lemma F as a statement
```

**M3b (recommended).**
OLD:
```
carries no fiber sum. `[novelty: single-check]`.
```
NEW:
```
carries no fiber sum. `[novelty: dual-model check 2026-09-29]`.
```

**M3c (recommended).**
OLD:
```
`[novelty: single-check]` for (i)–(iii) as a statement
```
NEW:
```
`[novelty: dual-model check 2026-09-29]` for (i)–(iii) as a statement
```

**M3d (recommended).**
OLD:
```
neither printed over Z. `[novelty: single-check]`.
```
NEW:
```
neither printed over Z. `[novelty: dual-model check 2026-09-29]`.
```

**M4 (recommended).**
OLD:
```
`[novelty: single-check → the reader flips]`
```
NEW:
```
`[novelty: dual-model check 2026-09-29]` (writer 22 arXiv queries, reader 20, positive controls passing; `results/beta-shapes-s35/read-O.md` §2.9)
```

**M5 (recommended, replace both occurrences).**
OLD:
```
`[novelty: single-check → reader]`
```
NEW:
```
`[novelty: dual-model check 2026-09-29]`
```

**M6 (recommended).**
OLD:
```
**Theorem R:** if the Q-linear span G of the diagonal row {(Δ · c(Γ_n))_Y : n ≥ 2} is finite-dimensional, then B has finitely many residue characteristics.
```
NEW:
```
**Theorem R:** if the Q-linear span G of the diagonal row {(Δ · c(Γ_n))_Y : n ≥ 2} is finite-dimensional, then B has finitely many residue characteristics; conversely dim_Q G ≤ |char(B)| always, so dim_Q G < ∞ exactly when char(B) is finite (A9's one fixed κ is used; A7 only names the fibers of c).
```

**M7 (recommended).**
OLD:
```
Durov 0704.2030 p. 43 (the F₁-square is the diagonal).
```
NEW:
```
Durov 0704.2030 p. 43 (the F₁-square is the diagonal); Borger 0906.3146 §7.7 p. 27 ("Of course this makes essential use of equal characteristic" — the printed remark at Theorem R's coordinate, on descent, not on a pairing); Deninger x-18 p. 4 ("the N γ are not all powers of the same number" — Corollary 3.2's dynamical twin).
```

**M8 (recommended).**
OLD:
```
evaluating on Γ_n ≅ B: for b ∈ B, c(Γ_n) ∋ (b, φ_n(b))
```
NEW:
```
evaluating on Γ_n ≅ B, with c restricted to Γ_n written as b ↦ (b, φ_n(b)) — the rung-1 form (pr, Fr^n_T) of p. 25, taken here as part of A7(T2b)'s graph identification (A7 fixes the image of Γ_n, not its parametrization; with c|Γ_n = (σ_n, φ_n ∘ σ_n) for β-automorphisms σ_n of B the computation below changes) — for b ∈ B, c(Γ_n) ∋ (b, φ_n(b))
```

**M9 (recommended).**
OLD:
```
Hodge index gives an inequality on the square, and A13 item 4 over Z gives the tower Λ(n) and no rationality.
```
NEW:
```
Hodge index gives an inequality on the square, and A13 item 4 over Z gives the tower Λ(n) and no rationality. (Reader's precision: on a finite-rank Num(Y) the identity (Δ · Γ) = 1 + d(Γ) − σ(Γ), with Weil's σ(D) := d₁(D) + d₂(D) − (D · Δ) (Milne p. 11), is a DEFINITION of σ and holds tautologically; the content of (H-Lef) is that n ↦ σ(Γ_{φ_n}) is the trace of a MULTIPLICATIVE family on a finite-dimensional space, which needs the composition of correspondences through the triple product (Milne pp. 10–11, D₁ ∘ D₂ = p₁₃*(p₁₂*D₁ · p₂₃*D₂) and (8)) — structure beyond the square and beyond A6–A13.)
```

**M10 (recommended).**
OLD:
```
hence at most ONE prime has d_p > C_g (two such primes would give d_p d_q > C_g² ≥ C_g)
```
NEW:
```
hence NO prime has d_p > C_g (for any second prime q, d_q ≥ 1 gives d_p d_q > C_g), and g = 0 is excluded at the first composite (d + 1 ≤ 0)
```

**M11 (recommended).**
OLD:
```
and nothing more; the Opus reader's independent search is the second check.
```
NEW:
```
and nothing more; the Opus reader's independent search is the second check. **Reader's check (2026-09-29, `verify-O/arxiv_O.sh`, `arxiv_O2.sh` → `arxiv-O.xml`, `arxiv-O-2.xml`, parsed in `arxiv-O-parsed.txt`; 20 queries, https, one at a time, 3 s apart, positive controls "lambda-rings" + "field with one element" (3, incl. 0906.3146) and "arithmetic site" (15) PASS):** the non-control hits (1603.03191, 1502.05580, 1204.3129) are on disk and on the record and do not state Theorem R, Lemma F, Proposition 2.2.1, Corollaries 3.1–3.2 or T2 (b) over Z; the labels are flipped to `[novelty: dual-model check 2026-09-29]`; V.5 governs what the null search licenses.
```

**M12 (recommended).**
OLD:
```
no candidate object, and the missing piece is now the rung, not the axioms.
```
NEW:
```
no candidate object: the missing piece is a proposed (D4) target over Z, and no rung below the arithmetic case can test one.
```

## 4 Group-IV decision (brief item 4) — **YES: Option A (IV.20), with F12 and M4–M7 applied to the staged text**

The test: is Theorem R (with T3) a program-discovered barrier of the form "proof class X cannot decide RH because Z", with a proof the record does not already carry?
- **X** — every route that transfers Weil's intersection-theoretic proof to Spec Z (or a number ring) through a target of the SPEC's pair whose diagonal-row intersection numbers span a finite-dimensional Q-space: a surface over a field, a Z- or Q-valued form, a finite-rank Néron–Severi group, a finite-h Lefschetz identity with integer traces. Borger prints exactly this program as a proposal (0906.3146 p. 5: "translation of Weil's proof of the Riemann hypothesis for S from algebraic geometry over k to that over F^S_1 … it is hard to imagine this succeeding without further ideas").
- **Z** — A9 makes each κ(Δ · c(Γ_n)) the logarithm of an integer; every prime divides one of them; {log p} is Q-linearly independent; there are infinitely many primes. Conversely dim_Q G ≤ |char(B)| (the reader's converse, M1): the obstruction is exactly the count of residue characteristics.
- **Does the record carry it?** III.20's "Deligne's squeeze additionally needs RATIONALITY (finitely many eigenvalues of fixed weight) — the exact coordinate with no archimedean analog, where the transfer dies" is on the (A) side (the determinantal realization), is an anatomy observation with no proof, and would be answered over Z by the infinitude of the zeros; Theorem R is on the (B) side — the SQUARE's own pairing — and is proved from the prime side alone (no zeros, no Hadamard). IV.13's "{log p} is Z-linearly independent (unique factorization)" is the same arithmetic input on a different object (the period group of a flow on a closed 3-manifold, bounded by rank H₁(M ∖ N)); IV.13 is itself a Group-IV entry built on that input, which is the precedent: the same lemma on a new object with a new kill is an entry, not a rider. Borger §7.7's "Of course this makes essential use of equal characteristic" names the coordinate and proves nothing. Deninger's x-18 p. 4 dictionary line is an analogy; x-20 p. 24 Remark 3 is about flows. None states or proves Theorem R, and the reader's 20 queries plus the writer's 22 find no print (§2.9).
- **Guard.** The entry is RH-blind (NOTE §2.3 DH CHECK) — a shape barrier on constructions, not an S1 filter; its KILLS must not reach (D4-fin) (F12), and its STATUS must carry the one-κ dependence (M6). With those, **YES — a 10(d) trigger**: the next digest's follow-ups are the ones the note prices (§5 "REMAINS" (d): a Lean statement of Theorem R's arithmetic core — elementary; and the (D4) candidate-object question, which by §5 below is a question about PROPOSING a target over Z, not about finding a lower rung).
- **Count impact.** Group IV 19 → 20, total 58 → 59 (Session-34 count paragraph). Insert the Option-B IV.10 rider as well (it carries the Z-form of E3 Theorem 4.1(b), a scope change IV.20 does not state), with its label flipped (M5); do not insert the Option-B III.20 rider (its content is IV.20's).

## 5 Candidate-object decision (brief item 6; the note's §3.7) — **AGREE: NO; ground corrected**

The definition, quoted at the line (`results/program-digest-s28.md` line 266): "standing order 6's free rein begins when a candidate object (axioms together with a rung-1 model and a written DH failure at the axiom level) is proposed — the SPEC supplies the axioms and the rung-1 model, and no candidate for the target over Z is on the record". The definition's own second clause makes the candidate a PROPOSED TARGET over Z; the axioms, the rung-1 model and the DH failure are the SPEC's and already exist. (D4) is a description of the shape any such proposal must have — "Described, not refuted", in the note's words — and the note proposes no (β, Y, c) (§0, V.1). So the answer is NO on the definition's first requirement (nothing is proposed), not on "no rung-1 model": the primed clauses A8′, A11′ (as conditioned by F9), A13′ keep the curve pair as their rung-1 model, in (D3) form. What IS true, and is the note's real finding, is sharper than "no rung": by Theorem R and its converse, the (D4) content of any proposal lives exactly over bases with infinitely many residue characteristics, so 10(b)'s ladder can check only the reduction of the primed clauses to A8, A11, A13 on rung 1 — never their (D4) content below the arithmetic case. F2–F4, F6 and M12 state this; the NO and the V.5 sentence ("a fact about the record's rungs, not a verdict on the branch") stand.

## 6 Honesty, lint, cost

*Read at the page:* the list in the header. *Re-derived at the line:* the §1.3 partition; Lemma F; T1; T2 (a)–(c) and Proposition 2.2.1; Theorem R, its converse, Corollaries 3.1–3.2; routes (a), (b); E4 from Milne pp. 9–11; A8′ from Ex. 1.7. *Computed:* `verify-O/numbers_O.py` [O1]–[O13]. *Searched:* 20 arXiv queries (§2.9). *Recalled, unverified, not used:* none added by the reader. *Not opened:* Hadamard/Littlewood sources (not on disk; non-load-bearing, as the note says — agreed). Lint of this file: none of "clearly / obviously / easy to see / well known"; U.S. English. Files written by the reader: `read-O.md`, `verify-O/` (numbers_O.py, numbers-O.log, quote_check.py, quote-check.log, zoo_check.py, zoo-check.log, arxiv_O.sh, arxiv_O2.sh, arxiv-O.xml, arxiv-O-2.xml, arxiv-O-parsed.txt, amendments.py, apply_check.py, apply-check.log), a dated block in `SHARED.md`. NOTE.md not edited; nothing committed. Cost (reader's estimate): ≈ 190k tokens of context, ≈ 20 min wall clock (16:05 → 16:25 IST), no agents spawned.
