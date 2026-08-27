# REFEREE REPORT — `results/c3-r/seed-no-go-note.md` (barrier-zoo IV.10, publishable form)

**Date:** 2026-08-26 (Session 6, independent referee — none of the inputs are the referee's own work; everything load-bearing re-derived from scratch per standing order 5).
**Object:** the no-go note "Products of the per-prime Tate curves of absolute geometry carry no correspondence calculus for the Weil explicit formula," pre-external-circulation pass.
**Instruments:** full line-by-line re-derivation of Theorems 1–6 and all remarks; on-disk verification of every quotation and file pointer; bit-for-bit rerun of `seed-no-go-checks.py`; an independent check suite written from scratch (`referee_seed_checks.py` / `.json`, this directory) with a *rigorous* interval-arithmetic continued-fraction method, instrument-independent constants (exact-rational atanh series; hand-rolled integer Chudnovsky), exact integer-determinant intersection theory, and PSLQ replication at different precision/coefficient bounds; WolframAlpha as a third digit instrument on two targets.

---

## VERDICT: **FAIL AS-WRITTEN — one fatal-class defect (§7's transcendence-status claims are false), repairable, and the repair STRENGTHENS the note.** All six theorems and both sharpenings verify completely. Nine mechanical repairs applied directly (list in §5). The note must not circulate until the §7 repair (drafted in full in §2 below) is executed.

The irony of the fatal is that it is an *underclaim*: the note labels as "open, no proven theorem excludes it" a coincidence — (T2), the CM case `(log p)² ∈ 4π²Q` — that is excluded by the Gelfond–Schneider theorem, classical since 1934. A transcendence-literate reader would catch this instantly, and in a note whose entire posture is verification discipline, a false bolded claim about the state of transcendence theory is fatal to circulation even though every headline theorem stands and the correction only makes the result stronger.

---

## 1. Line-by-line re-derivation (task 1) — ALL VERIFIED

### Lemma 0 (lattice presentation)
Re-derived: `exp₂(w + τ_p) = e^{2πiw}·e^{2πi·(i y_p)} = e^{2πiw}·e^{−log p}` ✓ (the exponent is `−2π y_p = −log p`); `p^Z = (p^{−1})^Z` ✓; kernel `Z` ✓. The pinpoint source citation is exact: the lattice statement `Λ_p = Z ⊕ Zτ, τ = i·log p/(2π)`, `q = 1/p`, rectangular, defined over **R** sits at **line 1526** of the on-disk extraction, verbatim as quoted. Consistency with the Tate parameter checked independently: `q = e^{2πiτ} = e^{−log p} = 1/p` ✓.

### Theorem 1 (iff isogeny criterion) — both directions, Hom refinement, degree
- *Forward.* `λ·1 ∈ Λ_q ⟹ λ = a + i b y_q`; `λ·τ_p = −b y_p y_q + i a y_p`; membership forces `−b y_p y_q = c ∈ Z` and `a y_p = d y_q`. Case `a ≠ 0`: `y_p/y_q = d/a ∈ Q ⟹ p^a = q^d` (after clearing signs, both exponents positive) — kills by unique factorization ✓. Case `a = 0`: `d = 0`, `λ = i b y_q`, `b ≠ 0`, `b·y_p y_q ∈ Z ⟹ y_p y_q ∈ Q` ✓.
- *Hom refinement.* `Hom = {i b y_q : b y_p y_q ∈ Z}`; with `y_p y_q = u/v` lowest terms, `v | bu ⟺ v | b` (gcd(u,v)=1) ⟹ `Hom = Z·(i v y_q)`, rank 1 ✓.
- *Converse.* `λ₀·1 = vτ_q ∈ Λ_q`, `λ₀·τ_p = −v y_p y_q = −u ∈ Z` ✓ — genuinely produces the map, so the criterion is iff ✓.
- *Degree.* `covol(Λ_p) = y_p`; `[Λ_q : λ₀Λ_p] = |λ₀|² y_p / y_q = v² y_q y_p = uv` ✓. **Independently re-verified by exact integer arithmetic** (referee check R4): in the bases `(1, τ_p)`, `(1, τ_q)` the map λ₀ has integer matrix `[[0, −u], [v, 0]]`, `|det| = uv` — checked for `(u,v) ∈ {(3,7),(1,1),(2,5),(10,9),(1,4)}`, all pass. Degree = kernel size = index ✓.
- *Remark 1 (4π²Q vs π²Q).* `4π²Q = π²Q` as subsets of **R** since `4 ∈ Q^×` — trivially correct; the normalization-free invariant `y_p y_q ∈ Q` is the right display; the account matches `results/adjudication-C3.json` computation (a) verbatim (read this session: "the killers' 'π²Q' vs '4π²Q' bookkeeping is the same rationality condition") ✓.
- *Remark 2 (symmetry).* `y_p y_q` symmetric ✓; consistent with dual isogeny ✓.

### Theorem 2 (two-partner rigidity) — unconditional ✓
`y_p y_q, y_p y_{q′} ∈ Q^×` (nonzero since the `y`'s are positive) ⟹ `y_q/y_{q′} ∈ Q ⟹ log q/log q′ ∈ Q ⟹ q^m = q′^n` — unique factorization kill ✓. Consumes no transcendence input ✓. Partial-matching corollary follows with Remark 2's symmetry ✓.

### Theorem 3 ({2,3,5} kill, strengthened form) ✓
Any two of `{2,3},{2,5},{3,5}` share a prime, so two simultaneously nonzero groups contradict Theorem 2 — hence at most ONE of the three surfaces carries a nonzero group ("no two," a fortiori not all three) ✓; the direct derivation (`y_3/y_5 = r₁/r₂ ∈ Q ⟹ 3^m = 5^n`) also checks ✓. The closing family-level sentence is licensed because R1's multiplicativity needs cross-prime classes for all pairs ✓.

### Theorem 4 (NS collapse) — checked against the note's own reproof; BL citation is properly hedged
The self-contained proof is correct at every step; I re-derived each:
- *Step 1:* the normalization `L̃` has `L̃_x = L_x ⊗ L₀^{−1} ∈ Pic⁰` (degree constancy in a connected flat family ✓), `L̃₀` and `L̃|_{E×{0}}` trivial ✓; universal property of `(Ê′, P)` with the `pr₁`-ambiguity killed on `E×{0}` ✓; `φ_L(0) = 0` + rigidity ⟹ homomorphism ✓.
- *Step 2:* additivity via Poincaré biadditivity ✓; `Pic⁰(E×E′) = pr₁^*Pic⁰(E) ⊗ pr₂^*Pic⁰(E′)` (dual of product = product of duals) annihilated by the normalization ✓; converse via seesaw ✓; kernel = `Zξ₁ ⊕ Zξ₂`, freeness read off by intersection numbers ✓.
- *Step 3:* `L^ψ = (ψ×id)^*P` is already normalized, `φ_{L^ψ} = ψ` by uniqueness — splits the sequence ✓.
- *Step 4:* Abel–Jacobi principal polarization `E′ ≅ Ê′` ✓. (Bonus check the note does not make explicit but which I verified because Theorem 5(2) needs it: under `φ_{O(Δ)}`, `L_x = O([x])`, `L̃_x = O([x] − [0])` — so the class of Δ maps to exactly the Abel–Jacobi isomorphism, i.e. Δ's Hom-component is the *generator* `id`. `NS(E_p×E_p) = Zξ₁ ⊕ Zξ₂ ⊕ Z[Δ]` is therefore correct as stated.)
- *(a)* rank 2, `ξ₁² = ξ₂² = 0`, `ξ₁·ξ₂ = 1` ✓ (also exactly reproduced by referee check R7's integer determinants).
- *(b)* Künneth argument: `pr₁^*β` acts via `β ∪ α ∈ H³(E) = 0`; `pr₂^*β` via projection formula + fiber integration dropping `H¹` below degree 0 ✓; `ξ₁ = pr₁^*[pt]`, `ξ₂ = pr₂^*[pt]` ✓. (Nit N1 below on the transpose parenthetical.)
- *(c)* rigidity ⟹ only constant maps; graphs of constants ≡ ξ₂ ✓. **The numerical-profile kill re-derived:** `D·ξ₁ = b = 1`, `D·ξ₂ = a = 1 ⟹ D = ξ₁+ξ₂ ⟹ D² = 2 ≠ 0` ✓, against the true diagonal profile `(1,1,0)` (Δ² = 0 by adjunction, K = 0 — and confirmed exactly by R7: computed Δ-profile `(1,1,0)`, `(ξ₁+ξ₂)² = 2`). I additionally checked the exceptional-pair version: on a matched pair with `Hom = Zλ₀` of degree `uv`, a class with profile `(1,1,0)` exists iff `uv = 1`, i.e. iff the curves are isomorphic — so the note's restriction of (c) to the `Hom = 0` case is exactly right, neither over- nor under-scoped.
- *(d)* primitive part `⟨ξ₁,ξ₂⟩^⊥ = 0` ✓; `D² = 2d₁d₂` = CS with equality everywhere ✓; negative-semidefiniteness-on-primitive-part formulation of CS is the correct equivalent ✓.
- *Remark 5 (the care point, task 2):* present and correct. `ξ₁+ξ₂` ample by Nakai (a curve with `C·ξ₁ = C·ξ₂ = 0` would map to a point in both factors — impossible) ✓; general members of `|3(ξ₁+ξ₂)|` irreducible (Lefschetz very-ampleness of the third power + irreducibility of general very-ample divisors on an irreducible surface) and dominating both factors ✓. The note nowhere says "every curve is a fiber union" — it says *numerically* a fiber combination, and Remark 5 explicitly warns against the stronger misreading ✓.
- *BL:* Birkenhake–Lange is not on disk; the note cites it at chapter level only and re-proves every consumed fact, with the hedge stated in the references — acceptable under standing order 5. Nothing load-bearing rests on a recalled page number ✓.

### Theorem 5 (diagonal residue) ✓
(1) `λ = a + i b y_p`; `λτ_p = −b y_p² + i a y_p`; `b ≠ 0 ⟹ y_p² ∈ Q ⟹ τ_p² ∈ Q` imaginary quadratic ⟹ CM order ✓ (but see FATAL F1: the exception is in fact *impossible*, not merely unexpected).
(2) `Γ_m·ξ₁ = 1`, `Γ_m·ξ₂ = m²` (`#ker[k] = k²` ✓), `(Γ_m·Γ_n) = #ker[m−n] = (m−n)²` with transversality from independent tangents `(1,m), (1,n)` ✓; `Δ² = 0` ✓; Lefschetz number `1 − 2m + m² = (m−1)²` ✓. **Independently re-verified exactly** (R7): intersection numbers of the integral subtori of `T⁴ = R⁴/Z⁴` as 4×4 integer determinants of direction vectors reproduce the entire profile `(1, m², (m−n)²)` for `m, n ∈ [−3, 5]`, plus the Δ-profile and `(ξ₁+ξ₂)² = 2`, all signs consistent.
(3) `p`-independence: the `Γ_m, ξᵢ` are the same integral subtori under the basis identification for every `p`; cup products of integral classes are topological ✓. The claim that the complex structure enters the calculus only through `Hom`/`End` is correct given Theorem 4 ✓.

### Theorem 6 (no-go assembly) ✓
- **O1** ✓ — multiplicativity `Ψ_p ∘ Ψ_q = Ψ_pq` needs nonzero cross-prime `Corr` for essentially all pairs; Theorems 2–4 cap the supply at a partial matching, and `{2,3,5}` already fails. Unconditional; the parenthetical correctly notes only the *existence* question (T1) is open, not the kill.
- **O2** ✓ — correctly scoped to off-matching surfaces; no diagonal class even numerically (4c), zero action on `H¹` (4b), vacuous CS (4d).
- **O3** ✓ — `(Ψ_f·Δ) = Σ c_m(p)(m−1)² + a + b` re-derived (ξᵢ·Δ = 1 each ✓); integer-coefficient functional, so any `p`-dependence must be hand-inserted into `c_m(p)` = barrier IV.1 re-entry ✓. The commission's Z2 clause is quoted accurately ("C3's prime contact is the correspondence calculus itself or nothing," `directions/C3-geometric-substrate.md`, verified this session) ✓. The `X̃_∞` `p`-independence is the source paper's own Theorem 5 / §4.3, "totally independent of p," verified verbatim on the extraction (line 1580) ✓. Pole terms: no candidate home — correct ✓.
- Logical independence of O1–O3 ✓. The escape-route rider ✓: `λe^{iθ} ↦ λ^{log q/log p}e^{iθ}` does conjugate the flows (`p ↦ q` ✓), is real-analytic and not holomorphic ✓, and the price statement (smooth/char-one correspondences forfeit `(1,1)`-positivity) is right.

### Remark 3 (composite moduli / one-generator towers) — verified with one precision repair
`log m/log n ∈ Q ⟺ m, n` multiplicatively dependent `⟺ m = k^a, n = k^b` ✓; commensurable subgroups `k^{aZ}, k^{bZ}` give genuine isogenies within a tower ✓ (spot-checked: `λ = 2` maps `Λ_{E_2} → Λ_{E_4}`); two partners of a fixed modulus forced into a single tower ✓. But the original flat "nothing across towers" contradicted the note's own Theorem-2 structure: a cross-tower isogeny is *conjecturally* excluded (same open rational-product coincidence as T1), not unconditionally. Repaired (applied edit 6) to "at most the same conjecturally-empty exceptional structure … now a partial matching of towers." The Lemma-B-fork echo sentence is a fair structural observation ✓.

### Explicit formula display (§1.3) ✓
The displayed normalization (`f̂(s) = ∫ f(x)e^{(s−1/2)x}dx`; `f̂(0) + f̂(1) − Σ Λ(n)n^{−1/2}(f(log n)+f(−log n)) − W_∞(f)`) is a standard shape, explicitly hedged as schematic; only (W-i)–(W-iii) are consumed, and each is correct ✓.

---

## 2. FATAL F1 (substantive — NOT applied; repair drafted): §7's transcendence-status claims are false. (T2) is a refuted question, not an open one; (T1) is settled by the four-exponentials conjecture, not only by Schanuel.

### F1(a): (T2) is excluded UNCONDITIONALLY by the Gelfond–Schneider theorem (1934). No `E_p` has CM; `End(E_p) = Z` for every prime, full stop.

Proof (re-derived, two independent routes):
1. *Power form.* Suppose `(log p)² = 4π²r`, `r ∈ Q`. Both sides positive ⟹ `r > 0` and `log p = 2π√r`, i.e. `p = e^{2π√r}`. Now `e^{2π√r} = (−1)^{−2i√r}` (branch `log(−1) = iπ`): base `−1` algebraic ≠ 0, 1; exponent `β = −2i√r` algebraic (i and √r are) and **not rational** (purely imaginary, nonzero). Gelfond–Schneider ⟹ `(−1)^β` is transcendental. But `p` is an integer. Contradiction. ∎ (This is the classical family "e^{π√d} is transcendental" — the Ramanujan-constant circle — specialized to `d = 4r`; it covers `r` a perfect rational square too, since `β` stays imaginary.)
2. *Linear-forms form — using the very Baker statement the note itself quotes.* (T2) ⟺ `log p = 2√r·π = (−2i√r)·(iπ)`, a **Q̄-linear relation between `log p` and `log(−1) = iπ`**, two Q-linearly independent logarithms of algebraic numbers (one real, one imaginary). Baker (homogeneous case = Gelfond–Schneider) forbids exactly this. ∎

So the note's §7 sentence "*(T1)/(T2) are quadratic relations among log p, log q, π, outside the reach of any proven linear-forms result*" is **false for (T2)**: the quadratic `(log p)² = 4π²r` *factors* into a linear relation with an algebraic (imaginary quadratic-irrational) coefficient — precisely linear-forms territory. And the bolded "**No proven theorem currently excludes either coincidence**" is false — a proven theorem excludes (T2), and has since 1934.

### F1(b): (T1) is settled by the FOUR-EXPONENTIALS CONJECTURE — a standard conjecture far short of Schanuel — contradicting "to our knowledge no standard conjecture short of Schanuel-type algebraic independence settles them."

Proof (re-derived): suppose `log p·log q = 4π²·u/v`. Take `x₁ = 2πi, x₂ = log p` (Q-linearly independent: real vs imaginary parts) and `y₁ = 1, y₂ = log q/(2πi)` (Q-linearly independent: `y₂` is purely imaginary, nonzero, hence not rational). The four exponentials:
`e^{x₁y₁} = e^{2πi} = 1`, `e^{x₁y₂} = e^{log q} = q`, `e^{x₂y₁} = p`, and `e^{x₂y₂} = e^{log p·log q/(2πi)} = e^{−2πi·u/v}` — a root of unity. **All four are algebraic**, contradicting the four-exponentials conjecture. So 4EC ⟹ ¬(T1). ∎
(T1) does remain open *unconditionally*, and — a point worth adding to the note — the **proven** six-exponentials theorem does not obviously reach it: a third row `x₃` with both `e^{x₃y_j}` algebraic would itself require a second rational-product coincidence, which the note's own Theorem 2 forbids. The note's Schanuel derivation (verified line-by-line: Q-linear independence of `log p, log q, iπ` ✓, trdeg ≥ 3 ⟹ algebraic independence ✓ ⟹ both non-coincidences) remains correct as the stronger conditional statement.

### Impact — the repair STRENGTHENS the note everywhere it touches:
- **Theorem 5(1):** the CM exception clause is vacuous. Replace "(No prime is known — or expected — to satisfy the exception; see §7.)" with "(No prime satisfies the exception — Gelfond–Schneider, §7; so `End(E_p) = Z` unconditionally.)" The theorem as printed stays literally true; the parenthetical as printed is true-but-misleading.
- **§0 item 5:** "barring `(log p)² ∈ 4π²·Q`" can be deleted or replaced by "unconditionally (the CM exception is impossible, §7)".
- **§0 closing line and §10 ledger row:** "(T1), (T2) … OPEN" must become "(T1) OPEN (settled under the four-exponentials conjecture; Schanuel gives algebraic independence); (T2) REFUTED unconditionally (Gelfond–Schneider)".
- **§7 in full:** re-title the section (only ONE open rider remains); state the (T2) theorem with the one-paragraph proof above; restate (T1)'s status as "open unconditionally; an instance of the four-exponentials conjecture; Schanuel-conditional proof retained; six-exponentials does not obviously apply (via Theorem 2)". Numerics rows 4–5 (`(log2)²`, `(log3)²`) become *confirmations of a theorem* rather than evidence on an open question — keep them as detector controls.
- **§9 transcendence-background paragraph:** "the four-exponentials circle for the open status of quadratic relations" must be corrected ((T1) is an *instance-consequence* of 4EC; (T2) is Gelfond–Schneider — cite it); "stated here as open" now applies to (T1) only. The sentence "(T1)/(T2) appear to be unrecorded in the literature in this form" should be softened for (T2): the *question* may be unrecorded, but its resolution is a two-line specialization of a classical theorem.
- **Remark 4, Theorems 1–4, 6:** untouched — (T1) is the only coincidence relevant to cross-prime pairs, and it remains open. Nothing in the no-go weakens; O3 loses its "barring" hedge and becomes cleaner.
- **Downstream (parent's files, outside this note):** `BARRIER-ZOO.md` IV.10 ("End(E_p) = Z barring (log p)² ∈ 4π²Q"; "the two transcendence non-relations are unproven") and the adjudication echo carry the same understatement and should be updated when the note is.

Why this is fatal rather than major: the note is headed for *external* circulation with a bolded, false claim about what transcendence theory proves, in its "honesty" section of all places, and with its own quoted Baker statement contradicting the very next sentence. Any competent reader in the CCM/transcendence audience catches it. Repair cost: one section rewrite plus five one-line echoes; drafted above; content only gets stronger.

---

## 3. Scope, citations, riders (tasks 2–3) — VERIFIED (with the F1 caveat)

**Scope (§8).** Kills exactly M2b, N2, thesis asset 3 — each verified against `directions/C3-geometric-substrate.md` (adjudication header: "STRUCK: M2b, N2, thesis asset 3…" ✓; asset 3's original wording at line 31 ✓; the seed text at line 49 ✓, including "the positivity is free fiber-by-fiber" that Theorem 4(d) answers, and the Z5/R2 "bandwidth data in geometric dress" fear at lines 118/130 that Theorem 6 shows was too optimistic). Routes A (char-one square, [CC7] watch ≥ Nov 2026) and C (Deninger/M2c) explicitly untouched ✓; M3 untouched ✓; the curves themselves and pair-indexed analytic data (Kurokawa) explicitly not diminished ✓ — nothing beyond the three targets is claimed killed. The bracket framing (char-one square: correspondences without positivity calculus; complex surfaces: positivity calculus without correspondences) is accurate and effective. N2 bullet repaired for conditionality precision (applied edit 7). Riders labeled open and unneeded ✓ as to the *kill's* logic — but the labels themselves are wrong per F1.

**The seven citation-and-distinguish obligations vs `prior-art-r7a.md` §6.** All seven gate obligations are discharged; note that the note's §9 enumerates a slightly different seven (it promotes the Scholze/FF adjacency — gate §4's "one sentence" duty — to item 7 and discharges the gate's item 7, the transcendence background, in the trailing paragraph). Mapping and accuracy:
1. **CCM math/0703392** — cited by its correct title "The Weil Proof and the Geometry of the Adeles Class Space" ✓ (the gate's bookkeeping correction propagated); §7.1 scaling correspondences and §10.2 `T_p ≅ R⁺^×/p^Z` vanishing-cycles germ characterized exactly as the gate found ✓; "Fun with F₁" 0806.2401 correctly separated ✓.
2. **CC16 + CE15 §4.3.2** ✓ — stall quote verified verbatim on disk this session (t-20b extraction line 1429; the note's silent capitalization of the source's mid-sentence "what" repaired to "[W]hat", applied edit 2).
3. **2501.06560 → 2606.06604 lineage** ✓ — the u-18b first-appearance quote verified verbatim on disk this session ("each C_p … becomes an analogue of an elliptic curve within the framework of characteristic one", extraction line 423–425); Jan 2025 → June 2026 = seventeen months ✓; "never raises products/isogenies" consistent with the gate's grep record ✓.
4. **Banaszak–Uetake trilogy** ✓ — arXiv numbers, venues, INT1–INT3, existence ⟺ RH (+ semi-simplicity), and the opposite-poles distinction all match the gate ✓.
5. **Kurokawa line** ✓ — 1992 proposal, Koyama–Kurokawa, Akatsuka CNTP 3 (2009) 619–653, Kurokawa–Wakayama, Tanaka 2008.07752; zeros at sums `ρ₁+ρ₂`; the localization sharpening (analytic pair-data exists, geometric host empty) is exactly the gate's §3 ✓; the Akatsuka paywall flag honestly carried into §10 ✓.
6. **Haran** ✓ — postulated intersection numbers, hoped-for 2D RR; distinction accurate ✓. [**Dated correction 2026-08-27:** this line, following the prior-art gate, cited arXiv:1507.06480 and the paraphrase "degenerates to the diagonal." arXiv:1507.06480 is **Koen Thas's** survey, not Haran's paper; the primary source is S. Haran, *Index theory, potential theory, and the Riemann hypothesis*, LMS Lecture Note Ser. 153, CUP 1991, pp. 257–270, p. 259, whose own wording is that the surface **reduces** to the diagonal (an isomorphism). The referee's substantive verdict — that the distinction is accurate — was re-checked verbatim against Haran p. 259 as quoted by Thas and stands unchanged.]
7. **Scholze/FF adjacency** ✓ — single-`p` legs/families, no published no-go, the `X̃_∞` bridge correctly attributed to [CC26] itself ✓.
Gate item 7 (transcendence rider citations + open status + unneededness) — present in §7 and the §9 trailing paragraph ✓ structurally, but its content requires the F1 correction.

**References block:** all identifiers cross-checked against the gate report and on-disk corpus (u-15b/u-18b/t-20b/t-43b/t-30b/t-58a) ✓. The [BL] chapter-level hedge is explicit ✓. [We52] properly limited to the hedged display ✓.

---

## 4. Numerics (task 4) — REPRODUCED AND INDEPENDENTLY CONFIRMED

1. **Rerun of `seed-no-go-checks.py`:** completes, `all_pass: true`, and the regenerated JSON is **bit-for-bit identical** to the committed one. Every number in the note's §7 table (five values to 37 digits, PSLQ nulls at `10³⁰`, CF terms 201/201/179/160/191, max partial quotients 4591/1598/284/226/1521, `q_N > 10¹⁰⁰`) matches the JSON exactly ✓. Checks A/B tolerances match the note's "55 digits" claim ✓. Control E finds `log 8 = 3·log 2` ✓.
2. **Independent instrument, rigorous method** (`referee_seed_checks.py`, written from scratch): constants recomputed by exact-rational atanh series (`log 2 = 2 atanh(1/3)` etc.) and a hand-rolled integer binary-splitting Chudnovsky π with certified error bounds; the five targets bracketed in rational intervals; **interval continued fractions** (only the common CF prefix of the two endpoints is kept — every reported term is *proven*, no floating-point heuristic). Result: identical term counts and max partial quotients to the note's table, and a **rigorous proof that any rational value of any of the five targets has denominator > 10¹⁰⁰** ✓. First 36 digits of each target match the note's table ✓.
3. **Third instrument:** WolframAlpha, 40 digits, on `log2·log3/(4π²)` (= 0.01928902059982156790073460399965086597553) and `(log3)²/(4π²)` (= 0.03057237432635508825361790081727330614887) — both match the table ✓.
4. **PSLQ replication at different parameters:** dps 300, maxcoeff `10²⁵`, all five targets null ✓; **plus a stronger affine 3-term PSLQ** `[log p·log q, π², 1]` at maxcoeff `10¹⁵` — also null for all five (the note only claims the 2-term form); control `log 9 = 2 log 3` found instantly ✓.
5. **Lattice-arithmetic spots:** exact-integer isogeny-degree check (R4, above); a brute-force demonstration for `(p,q) = (2,3)` that no lattice map exists with coefficients ≤ 300 — minimum residual of the imaginary-part condition is 3.3·10⁻⁴ (at `(a,d) = (−84,−53)`) and of the integrality condition 3.0·10⁻³, versus the 10⁻³⁰ tolerance a true map would meet (R5) ✓; and the full intersection profile by exact integer determinants (R7) ✓.
6. **Defect found in the script (minor M3 below):** check D is tautological as coded — its inner loop is `count += 1` unconditionally, so it verifies `k·k = k²` and nothing else (no distinctness of the representatives mod Λ, no membership). The referee suite's R6 performs the genuine check (all `k ≤ 7`: representatives pairwise distinct mod Λ and honest kernel points; passes). The note's "check D confirms the count" wording was softened accordingly (applied edit 8).

---

## 5. Findings register and applied repairs (task 5 included)

**FATAL (left as finding; repair drafted in §2):**
- **F1.** §7's status claims: "**No proven theorem currently excludes either coincidence**" (false — Gelfond–Schneider excludes (T2)); "outside the reach of any proven linear-forms result" (false for (T2), which factors into a Q̄-linear relation between `log p` and `iπ`); "no standard conjecture short of Schanuel-type algebraic independence settles them" (false — 4EC settles (T1)). Echoes in §0 (two places), Theorem 5(1)'s parenthetical, §9's transcendence paragraph, §10's ledger row. Repair strengthens the note; exact replacement content in §2.

**MINOR — applied directly (9 repairs, 8 Edit operations — items 2 and 3 shared one edit):**
1. §1.1 "The only mechanism that has ever proved a Riemann hypothesis" → "The classical template for proving a Riemann hypothesis". (Overclaim: Hasse's genus-1 proof, the Stepanov–Bombieri auxiliary-function method, and Deligne's weight/monodromy argument are Riemann-hypothesis proofs outside the CS-positivity mechanism.)
2. §1.1 CE15 quote: "What is missing…" → "[W]hat is missing…" (source reads "At this point, what is missing is…" — t-20b extraction line 1429; silent capitalization inside quotation marks removed).
3. §1.1 "eight years on" → "a decade on" (the note anchors the stall to [CC16] = Adv. Math. 2016; 2026 − 2016 = 10. The commission's "8-year stall" is anchored to the 2018 RR-strategy paper, which the note does not cite).
4. §9 item 2 "intersection theory/RR missing for eight years" → "missing a decade on" (same arithmetic).
5. §1.2 "Theorem 5 in §4.1.2 of the HTML full text" → "…in §4.3…" (the extraction places Theorem 5 under the §4.3 heading, line 1588; §4.1.2 is the Tate-curve subsection; intro Theorem 4 pointer verified correct, line 269).
6. Remark 3: "nothing across towers" → "at most the same conjecturally-empty exceptional structure as in Theorem 2, now a partial matching of towers …" (the flat claim contradicted the note's own Theorem-2 caveat structure; cross-tower isogenies are conjecturally, not unconditionally, excluded).
7. §8 N2 bullet reordered so the unconditional kill (Theorem 3) leads and the graph/diagonal emptiness is correctly scoped "off the conjecturally empty exceptional matching," with the unconditional "at least two of the three" statement added.
8. Theorem 5 proof: "check D confirms the count for `k ≤ 7`" → "check D tabulates them for `k ≤ 7`" (per the script defect; genuine verification now in `referee_seed_checks.json` R6).
9. Theorem 6 O3: "([CC26] Thm 5: …)" → "([CC26] Thm 5 and §4.3: …)" (the verbatim phrase "totally independent of p" sits in the §4.3 body, line 1580; Thm 5's own statement says "p-independent").

**MINOR — noted, not applied (judgment calls for the author):**
- **N1.** Theorem 4(b), "The transpose direction is identical using `Hom(E_q, E_p) = 0` (Remark 2)": the Künneth argument on the same surface needs no such input (just exchange `pr₁`, `pr₂`); the citation is needed only if the transpose is modeled on the swapped product `E_q×E_p`. Harmless, but stating the cheaper route would be cleaner.
- **N2.** §9's "seven obligations" enumeration differs from the gate's seven as described in §3 above; all obligations are discharged, so no action is required — but if the author wants a 1:1 correspondence with `prior-art-r7a.md` §6, the transcendence paragraph should be numbered 7 and Scholze footnoted (the gate itself asked only for one sentence there).
- **N3.** `seed-no-go-checks.py` check D should be upgraded to a genuine distinctness/membership verification (five lines; model in `referee_seed_checks.py` R6) so the JSON's `pass: true` for D certifies something.
- **N4.** "analogue" (six occurrences) retained deliberately: two are inside verbatim quotations, and the source papers' own terminology ("real analogue of the Fargues–Fontaine curve") plus standard U.S. mathematical usage justify the rest. No other British spellings found (full scan: -ise/-yse/-our/-re/-ll-/licence/towards/grey/maths — clean).

**U.S. English:** clean apart from the deliberate "analogue" (N4).

**Overclaim hunt, negative results (things I checked for and did NOT find):** no claim that the surfaces are curve-poor (Remark 5 explicitly guards it); no unconditional claim of Hom-vanishing for any specific pair (always "conjecturally empty matching"); O2/O3 correctly scoped to off-matching/diagonal surfaces respectively; Theorem 6 does not claim more than (R1)–(R3) for this family; §8 does not leak the kill onto routes A/C/M3 or onto [CC26] itself; the numerics are labeled evidence-not-proof; the Schanuel derivation is labeled conditional. The one genuine overclaim (§1.1 "only mechanism") is repaired.

---

## 6. Referee's summary for the record

The mathematics of the kill is correct, complete, and honestly scoped: Theorem 1 (both directions, the rank-1 Hom, degree `uv`), Theorems 2–3 (genuinely unconditional — nothing but unique factorization and Q-linear algebra), Theorem 4 (the decomposition reproved soundly; collapse, inertness, profile kill, vacuous CS all verified, including the sharpening that a diagonal-profile class on an exceptional pair would require an isomorphism), Theorem 5 (profile re-derived by exact topology), Theorem 6 (three independently fatal obstructions, each airtight given the preceding theorems). The numerics reproduce bit-for-bit and survive an independent, more rigorous re-implementation plus a third instrument. The prior-art obligations are discharged accurately against the gate report, with the correct math/0703392 title and the correct CC25→CC26 lineage.

The single blocking defect is §7: the note is *too modest*, and falsely so — (T2)/CM is killed by Gelfond–Schneider unconditionally, (T1) by the four-exponentials conjecture conditionally, and the note's bolded claim to the contrary would not survive first contact with a transcendence-literate reader. Execute the §2 repair (and its five echo lines, plus the zoo/adjudication echoes outside the note), and this becomes a pass: the no-go gains a theorem (`End(E_p) = Z` always — the diagonal residue statement no longer needs its hedge) at the cost of one honest rider instead of two.

**Files:** note (repaired in place) `results/c3-r/seed-no-go-note.md`; this report `results/c3-r/referee-seed-no-go.md`; referee checks `results/c3-r/referee_seed_checks.py` + `results/c3-r/referee_seed_checks.json`; note's own checks rerun-verified `results/c3-r/seed-no-go-checks.{py,json}`.
