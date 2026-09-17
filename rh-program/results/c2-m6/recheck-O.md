# recheck-O.md — the INDEPENDENT RE-CHECK of the M6 rung-1 fix pass (Opus 5)

**Written 2026-09-17 (Session 23, the re-checker, Opus 5; machine clock via `date`). Contract: re-check the CHANGED items only of the author's fix pass (`results/c2-m6/FIX-BRIEF.md`, ledger `m6-rung1-note.md` §13) against `check-O.md` §10 items 1–7 and §9 amendments 1–6. Read at the page: the note's §13 ledger and every changed passage; `zoo-IV19-proposed.md` in full; `SHARED.md`; `hashes.txt`; Turán 1960 p. 313 as a page image; Weber 2009 pp. 2, 9, 12; Farmer pp. 44, 54, 63–66; Steuding printed p. 17. Every number below is printed by my OWN code in the session scratchpad (`recheck/exact_lam.py`, `recheck/sieveS.c`, `recheck/refine36.py`, `recheck/wzp.py`, `recheck/wzp_Lstar.py`, `recheck/pow2_closed.py`), written from the definitions, not from `verify/`. Nothing in the repository was edited except this file. Standing order 4: nothing here is a statement about RH.**

---

## §0 Headline verdict

**The fix pass CLOSES on substance, with ONE FIX-FIRST: a mis-transcribed exponent in the Turán citation.** Every one of check-O.md §10's seven items is discharged, and the two items that carried real mathematics — the label split on (E) and the DH coefficient counts — are discharged *better* than the check asked: the author replaced the check's inference about the L = 20 count with a structural theorem and an exact computation, and I have re-derived that theorem from `dh.py`'s definition and reproduced both counts from scratch by two independent routes. No number the rung computed moved: every pre-existing file under `verify/` is byte-identical to its pre-fix hash.

The single defect: the note prints Turán's window as **e^{17ωN² log N}** in five places. Turán (2.1), printed p. 313, reads **e^{17ωN log² N}** (page image read), and Weber p. 2 quotes it the same way. The exponent is a citation digit; it moves no conclusion (both forms are astronomically beyond any height the channel visits) — but the note claims the page was read, so the page must be what it says.

**Verdict for the fix pass as a whole: FIX-FIRST (one line, below). Insertable for zoo IV.19: YES** — the zoo draft carries no exponent, all six amendments are applied verbatim, and nothing in it depends on the defect.

**The exact edit, for the orchestrator to apply without another author pass:**

```
In results/c2-m6/m6-rung1-note.md, replace all five occurrences of  e^{17ωN² log N}
with  e^{17ωN log² N}  (lines 133, 181 twice, 208, 278) — Turán (2.1), printed p. 313;
Weber, arXiv:0806.3990v1, p. 2, quotes the same form.
```

Per item: **§1 (E)'s attribution — CLOSES except that one exponent (FIX-FIRST) · §2 DH counts — CLOSES · §3 §8's hypothesis and o(1) — CLOSES · §4 the Lindelöf-lock anchor — CLOSES · §5 §5.3's ranges, the cancellation identity, L* — CLOSES · §6 citation hygiene — CLOSES · §7 the Step-5 measure remark and §7's normalization — CLOSES · §8 zoo IV.19 — CLOSES, insertable · §9 hashes — CLOSES.**

---

## §1 Item 1 — the attribution and label of (E) (check-O §4.3 (a)–(e)): **CLOSES, with one FIX-FIRST**

**(a) The §6 theorem header.** Present and correct in substance: "(Bohr 1913, through the 'Bohr's reduction argument' of Weber §3; **Turán 1960**, *Acta Sci. Math. Szeged* 21, 311–318, Lemma p. 313, for the frequencies {log p}, with the effective window …; **Weber**, *Unif. Distrib. Theory* 4 (2009) 97–116 = arXiv:0806.3990, Theorem 1 and (3.17)–(3.18), in general and effective — Turán and Weber read at the page, §11; the proof below is reproduced for this coefficient system, and the published form is effective where this one is not)". That is §4.3(a) discharged.

**(b) The 10(n) paragraph.** Rewritten end to end. The nearest published object is now Weber 2009 Theorem 1 / (3.17)–(3.18) with Turán 1960 Lemma p. 313; the exact difference is reduced to the coefficient system, the prime-power grouping, the instance numbers and the impossibility reading; the sentence "that understated the distance by sixty-six years" is carried. §4.3(b) discharged.

**(c) The label split.** Exactly as required: the statement `[classical: cited at the page]`; the instance numbers, the twelve-point table and the reading `[novelty: dual-model check 2026-09-17]`; and "that reading is an interpretation of the theorem, not a theorem". The same split is in §0.3. §4.3(c) discharged.

**(d) §11's shelf.** "Recalled, labeled, none load-bearing" now reads "Bohr 1913 itself (not on disk; cited through Weber §3's 'Bohr's reduction argument' — the statement of (E) is carried by Turán 1960 and Weber 2009 at the page, §6)". §4.3(d) discharged.

**(e) The zoo.** §8 below.

### Verification at the page

**Turán 1960, Lemma p. 313.** The OCR layer is garbled at the displays, so I rendered PDF page 3 (printed 313) at 250 dpi and read the image. The Lemma is verbatim what the note reports: *"If 2 = p₁ < p₂ < ⋯ < p_N stand for the first N primes, d, β₁, β₂, …, β_N for arbitrary real numbers and ω is an integer ≥ 4, then there is a t₀ with (2.1) … such that for ν = 1, 2, …, N the inequalities (2.2) |t₀ log p_ν − β_ν − e_ν| ≤ 1/ω (e_ν integers) hold, if only N > c₆ (> e³¹), N > ω."* The note's report of the hypotheses (ω ≥ 4; N > c₆ > e³¹; N > ω), of the inhomogeneous shape, and of the Fejér-kernel proof at (2.3)–(2.7) ("Since after FEJÉR's formula we have …") is accurate.

**The one defect.** (2.1) as printed reads **d ≤ t₀ ≤ d + e^{17ωN log² N}** — seventeen-omega-N-log-squared-N. The note prints e^{17ωN² log N} at §6's header, twice in the 10(n) paragraph, in §8 and in the §13 ledger (five places). Weber's own quotation, arXiv p. 2 (image read), is "T = e^{17ωN log² N} if N is large enough, and 4 ≤ ω ≤ N" — so neither source supports the note's form. `check-O.md` §4.3 carries the same slip twice; it is inherited, not invented in the fix pass, but the note is the file a successor will quote. **FIX-FIRST, one line (§0).**

**Weber 2009, at the page.** Theorem 1 with (1.6)–(1.7) is on arXiv p. 2; the Turán citation ("Turán ([Tu], Lemma p.313)") is on p. 2; (3.17) and (3.18) are on p. 9; the References are on p. 12 — all as §11 says. The three sentences the note quotes are verbatim: *"the supremum of the Dirichlet polynomials D_L over large intervals (of length greater than T(N, ω)) is comparable to the supremum over the real line"*; *"Further estimate (3.18) is uniform over d"*; and the label *"Bohr's reduction argument"* on the display sup_ℝ D_L = sup_{𝕋^N}. (3.18) is 0 ≤ sup_ℝ|D_L| − sup_{2πd ≤ t ≤ 2π(d+T)}|D_L| ≤ (2π/ω)Σ|α_n|Ω(n), as the note states; (3.19) is Dirichlet's theorem "corresponding to the particular case β₁ = … = β_N = d = 0 in Theorem 1", which is the §11(i) correction the note claims. Weber's Theorem 1 is effective (explicit T through Ξ, with Ξ bounded below on the next lines), so "in general and effective" is right.

**Farmer §13.2 / Principle 13.2.** Verified in `fetched/p2-12-farmer-no-reasons-to-doubt-rh-arxiv-v4.pdf` (printed page = PDF page throughout). The subsection "13.2 Reason 5: The Deuring-Heilbronn phenomenon" opens on **p. 63**; Principle 13.1 and the DH function's construction are on **p. 64**; the sentence the note quotes — *"but that is not any extra information because Dirichlet series are almost periodic functions (of t) in σ > 1: so once there is one zero in that region, there must be ≫ T zeros in that region"* — and **Principle 13.2** are on **p. 65**. The note's "§13.2, pp. 64–65 … Principle 13.2 on p. 65" is correct, and the author's §13 remark on the check's "§13 p. 64" is the right correction.

**Steuding.** Lemma 1.8(i) **and** the sentence "The unique prime factorization of integers implies the linear independence of the logarithms of the prime numbers over the field of rational numbers" are both on the page whose running head is "1.3 Voronin's Universality Theorem 17", i.e. **printed p. 17** — so the note's §12 row (both on p. 17) is right and `check-O.md` §4.3's "the following page" was the slip.

---

## §2 Item 2 — the DH coefficient counts and the structural theorem: **CLOSES**

### §2.1 The factorization, re-derived from the definition

From `results/ccm-dh-test/dh.py` / `weilform.py`: a(n) is periodic mod 5 with values (1, κ, −κ, −1, 0) at residues (1, 2, 3, 4, 0), and Λ_DH is defined by a(n)log n = Σ_{d|n}Λ_DH(d)a(n/d). Let χ be the character mod 5 with χ(2) = i (2 generates (ℤ/5)^×, so χ(2, 4, 3, 1) = (i, −1, −i, 1)). Then a = Re χ + κ Im χ — check the four residues: 1 ↦ 1, 2 ↦ κ, 3 ↦ −κ, 4 ↦ −1 ✔ — equivalently a = αχ + ᾱχ̄ with α = (1 − iκ)/2.

For n coprime to 5 write n = n₁n₂, n₁ built from primes ≡ ±1 (mod 5) and n₂ from primes ≡ ±2 (mod 5). χ(n₁) ∈ {±1} is real, so χ(n) = χ(n₁)χ(n₂) gives a(n) = χ(n₁)a(n₂). Summing over the unique factorization n ↦ (n₁, n₂),

  **f_DH(s) = L₁(s)·F₂(s),  L₁(s) = Σ_{n₁}χ(n₁)n₁^{−s} = Π_{p≡±1 (5)}(1 − χ(p)p^{−s})^{−1},  F₂(s) = Σ_{n₂}a(n₂)n₂^{−s}.**

Hence −f′/f = −L₁′/L₁ − F₂′/F₂, the first supported on {p^k : p ≡ ±1 (5)} with value χ(p)^k log p ≠ 0, the second on T = {n ≥ 2 : every prime factor ≡ ±2 (5)}. **The author's §1 theorem is correct as stated, and I re-derived it independently.** The support claim S = {p^k : p ≡ ±1 (5)} ∪ T follows; the only thing the factorization does *not* settle is whether Λ_{F₂} can vanish somewhere inside T (the "mixed exponents" cancellation the brief asked about).

### §2.2 The exact count at L = 10, two ways

`recheck/exact_lam.py` runs the recursion **exactly in ℤ[κ]** (basis 1, κ, κ², κ³; κ⁴ = −2κ³ + 6κ² + 2κ − 1, the minimal polynomial κ⁴ + 2κ³ − 6κ² − 2κ + 1 = 0 verified to 10⁻⁵⁰ at the surd value), carrying Λ_DH(n) as a map {prime ↦ ℤ[κ]-coefficient of log p}. Results on [2, 22 026]:

| quantity | **mine** | note §1/§2.2 |
|---|---|---|
| nonzero Λ_DH(n) | **8 562** | 8 562 |
| support equals S | **True** (0 in S with Λ = 0; 0 outside S with Λ ≠ 0) | claimed |
| split |{p^k, p ≡ ±1}| + |T| | **1 239 + 7 323** | 1 239 + 7 323 |
| Λ_DH(n) = 0, n coprime to 5 | **9 058** (first: 22, 33, 38, 44, 57, 58, 62, 66, 76, 77, 82, 87) | 9 058, same list |

**No cancellation inside S.** Evaluating my exact ℤ[κ]-vectors at **120 digits**, all 8 562 are above 10⁻⁸⁰; the smallest is **5.4392·10⁻⁸ at n = 8 192 = 2¹³**, which is the note's "min nonzero 5.4·10⁻⁸ at 2¹³". So the count is right for the right reason, and it is right independently of Baker's theorem (the exact vectors are nonzero *and* their evaluations are).

A second, coefficient-free route: `recheck/sieveS.c` (C, bitset) counts |S ∩ [2, N]| by sieving out multiples of 5 and of every prime ≡ ±1 (mod 5) and adding the prime powers of primes ≡ ±1. At N = 22 026 it returns **1 239 + 7 323 = 8 562** — the same number with no recursion at all.

### §2.3 The count at L = 20, by an independent sieve

Same C program at N = ⌊e²⁰⌋ = 485 165 195:

```
primes <= N            : 25614562
primes = +-1 mod 5     : 12806386
{p^k : p = +-1 mod 5}  : 12807696
T (all factors +-2)    : 108146181
|S cap [2,N]|          : 120953877
```

**12 807 696 + 108 146 181 = 120 953 877** — the note's figure, digit for digit, from a sieve that knows nothing about Λ_DH. (The 25 614 562 primes also reproduce §2.1's ζ term split.) What the sieve cannot certify is the step from |S| to "nonzero coefficients" at L = 20, i.e. that Λ_{F₂} vanishes nowhere on T ∩ [2, e²⁰]; the note does not claim a proof there — it certifies the 2 235 borderline elements exactly and rests the remainder on a five-order f64 margin over 2.67·10⁸ proven zeros, and §11 labels exactly that as the fix pass's one inference. That is the honest statement and I endorse it.

**The powers-of-2 closed form.** The 2-part of F₂ is Σ_k a(2^k)y^k = (1 + κy)/(1 + y²), y = 2^{−s} (a(2^k) cycles κ, −1, −κ, 1). Then y(d/dy)log H gives Λ_DH(2^k)/log 2 = (−1)^{k−1}κ^k for odd k and 2(−1)^{k/2} − κ^k for even k. `recheck/pow2_closed.py` confirms both against my exact recursion for k = 1…30: Λ_DH(4) = −(2 + κ²)log 2 = −1.44223196461 ✔, Λ_DH(2¹³) = 5.4392·10⁻⁸ ✔, **Λ_DH(2²⁷) = 1.21251·10⁻¹⁵** ✔ (the note's 1.2·10⁻¹⁵, the smallest element of S at L = 20).

### §2.4 The summed counts, and that no cost number moved

`verify/out/dh_t85p7_L10.json` still carries `n_terms: 15346` and `verify/out/dh_t85p7_L20.json` `n_terms: 340796040`, so the f64-summed counts the note preserves are exactly what the Rust binary sums. Stronger: the pre-fix/post-fix hash diff shows that **the only files the fix pass changed are `m6-rung1-note.md`, `zoo-IV19-proposed.md` and `SHARED.md`**; every pre-existing script, log and JSON under `verify/` — including `cost_line.py`, `out/cost_line.json`, `out/controls_table.json` and the eleven twisted-sum JSONs — is byte-identical. No computed number could have moved. §5.1's arithmetic for the surplus terms checks out too: 7.9·10⁻¹² × 2√X × 2a₀ = 1.4·10⁻⁹ at L = 20, the note's "a priori ≤ 2·10⁻⁹".

---

## §3 Item 3 — §8's restored hypothesis and the o(1) re-normalization: **CLOSES**

**§6a.** §8 now reads: "by (E), no bound on |P_X(g_t)| whose constant is uniform in the height certifies it — the constant would have to exceed the torus supremum sup_𝕋|Φ| (1.42 at L = 10, 12.5 at L = 20), and a bound with a T-dependent constant is an evaluation by another name. The hypothesis is the uniformity of the constant in the height, not the window length (check-O.md §6a): a bound on a window of length ≍ 1/L, the form in which `results/full-map.md` line 203 states the Lindelöf lock, is closed by (E) only through the T-uniformity of its constant". That is check-O §6a's required wording, including the `full-map.md` line 203 point.

**§6b.** Both places carry the new normalization. The narrative: "a proportion o(1) of the ZEROS in [T, 2T] lie at depth ≥ δ, and the datum at a height sampled from the zeros sits within the kernel's reach ≈ 5/L of a deep orbit with probability o(1)". The italic restatement: "a proportion o(1) of the zeros in [T, 2T] lie at depth ≥ δ, so the bandwidth-L datum at a height sampled from the zeros misses a deep orbit with probability o(1)", with PRICING's wording identified as the same statement once the proportion is taken over the zeros.

**The arithmetic is stated correctly.** Backlund's form gives ≤ T·o_δ(log T) off-line zeros in [T, 2T]; each captures a height set of measure ≈ 10/L; the Lebesgue proportion of [T, 2T] is then (10/L)·o(log T), which is unbounded as T → ∞ at fixed L. That is exactly what the note prints, and it is the correct reason the Lebesgue normalization fails.

---

## §4 Item 4 — the Lindelöf-lock anchor: **CLOSES**

The full anchor — "(`directions/A4-lindelof-lock.md`; named at zoo IV.6 and in the §0 protocol item 5(b); the Schatten-3 route to it decided at IV.7's Session-6 closure; the prime-side form is `results/full-map.md` line 203)" — appears at every place the ledger lists: note §8 twice (the narrative and the italic restatement), §9 protocol item (5), §10's Lands sentence, and §11's read list; and in the zoo draft's STATEMENT and SOURCE.

A grep for "IV.7" over the note and the zoo draft returns only: the corrected anchor (five hits), §9's "IV.7 — no cubic row (the Lindelöf lock named in §8 as the SHARED wall is IV.6's and A4's object, not IV.7's …)", the §11/§12 read-lists, the zoo's SOURCE line "IV.7 (the Session-6 closure that decided the Schatten-3 route to it)", and the §13 ledger quoting the superseded text. **No residual "of zoo IV.7" anchor survives as a live claim.** The note also hands the orchestrator the two PRICING §3(a) sentences (lines 135 and 144) that still carry the mis-anchor, which is the right division of labor.

---

## §5 Item 5 — §5.3's ranges, the cancellation identity, and L*: **CLOSES**

**My own machinery, from the definitions.** `recheck/wzp.py` builds B(v) = Z⁻¹exp(−1/(1 − 4v²)), Z computed by quadrature as **0.22199690808403972** (the record's 0.2219969080840397), and ĝ(r) = (r − t)²B̂(L(r − t))². Summed over the record's own 36 on-line points it returns **0.0048010831907523** at L = 10 and **4.4642881736258·10⁻⁵** at L = 20 — the record's `W_Zprime` values 0.004801083190752414 and 4.464288173625844·10⁻⁵ to fourteen digits. So my transform is the record's transform.

**The 36 points, refined at 40 digits on S(u) = Z_DH(u)/[(5/π)^{3/4}|Γ(¾ + iu/2)|]** (`recheck/refine36.py`, f_DH from the four Hurwitz zetas, κ from the surd). The three spot checks the brief named:

| | recorded u | my refined u (40 digits) | displacement | |f_DH| recorded | |f_DH| refined |
|---|---|---|---|---|---|
| note example 1 | 87.64752783514871 | **87.647476332559739** | −5.1503·10⁻⁵ | 2.5629·10⁻⁴ | 3.54·10⁻³⁹ |
| best in ±30 | 100.59899262113166 | **100.598993807792285** | +1.1867·10⁻⁶ | 4.8487·10⁻⁶ | 1.29·10⁻⁴⁰ |
| worst in ±30 | 102.82034971047517 | **102.819209827108413** | −1.1399·10⁻³ | 3.6994·10⁻³ | 2.53·10⁻³⁹ |

All three agree with `check-O.md` §3's table to every printed digit. Over **all 36**: displacement range **1.187·10⁻⁶ to 1.140·10⁻³**, |f_DH| at the recorded points **4.849·10⁻⁶ to 3.699·10⁻³**, max |f_DH| at the refined points 3.54·10⁻³⁹, and exactly **one** of the 36 below 2·10⁻⁵. The note's "1.19·10⁻⁶–1.14·10⁻³", "4.85·10⁻⁶–3.70·10⁻³", "all but one larger than 2·10⁻⁵" are all confirmed, and the note's rounded restatement "1.2·10⁻⁶ to 1.1·10⁻³" / "4.9·10⁻⁶ to 3.7·10⁻³" is the check's.

**W_{Z′} at the record's exact L*** (`recheck/wzp_Lstar.py`; L* = 86.90744354035114 read from `results/c2-m2/verify/dh_negative_control_out.json`):

| L | recorded positions | refined positions | relative |
|---|---|---|---|
| **L* = 86.90744354035114** | **3.432164·10⁻¹⁰** (record log: 3.43216397640519·10⁻¹⁰) | **3.4083861·10⁻¹⁰** | **−6.93·10⁻³** |
| L* truncated to 86.907 | 3.428215·10⁻¹⁰ | 3.4044547·10⁻¹⁰ | −6.93·10⁻³ |
| 10 | 0.0048010832 | 0.0048001176 | −2.01·10⁻⁴ |
| 20 | 4.4642882·10⁻⁵ | 4.4652466·10⁻⁵ | +2.15·10⁻⁴ |

**The author's digit string is the right one and the author's note on the difference is correct.** At the exact L* the pair is 3.4322 → 3.4084·10⁻¹⁰ (the note); at L* truncated to 86.907 it is 3.4282 → 3.4045·10⁻¹⁰ (the check). Both give the same relative change 6.9·10⁻³ and the same verdict, "good to two digits". The author printing both, with the truncation named, is the correct resolution.

**The cancellation identity.** §5.3 now says: every record script forms W_Z = W(orbit ∪ on-line) and W_{Z′} = W(on-line), so W_Z − W_{Z′} = W(orbit) identically and the separation, ratio and "fires" columns of every DH control table are independent of the on-line positions. That is an identity, not an estimate, and it replaces "the main term dominates" as check-O §3 required. Correct as stated.

---

## §6 Item 6 — citation hygiene: **CLOSES**

A grep for "text lines" and "pdftotext" over `m6-rung1-note.md` and `zoo-IV19-proposed.md` finds **no live anchor**: the four hits are all inside the §13 ledger, three of them quoting the superseded text in an "old → new" line and the fourth flagging the surviving anchor in PRICING line 144 for the orchestrator. Farmer is now cited as §9.3 p. 44 (Conjecture 9.7, (9.1)–(9.3), Theorem 9.8, (9.4)–(9.5)), §12.1 p. 54, §13.2 pp. 64–65, §14.3 p. 66 — I verified each page in the PDF: Conjecture 9.7, Theorem 9.8 and the "negligible proportion of the zeros" sentence on p. 44; the heading "12.1 Reason 1: Lehmer's phenomenon" on p. 54; "Maybe the zeros in σ > ½, if they exist, all lie on σ = ¾?" on p. 66; Principle 13.2 on p. 65. Steuding is cited as Lemma 1.8(i), p. 17, which is where both the lemma and the independence sentence are printed. §12's Farmer/Steuding row and the new Turán/Weber row carry section and page only.

---

## §7 Item 7 — the §6 Step 5 measure remark and §7's "normalized at X₀": **CLOSES**

**The measure remark is correct as stated.** Step 5 already has (1/H)∫_T^{T+H}Q(θ(t))dt ≥ c₀/4 for H ≥ H₀. Since Q ≤ χ ≤ 1, ∫_T^{T+H}Q ≤ ∫_{{Q>0}}Q ≤ meas{Q > 0}, so meas{t ∈ [T, T + H] : Q(θ(t)) > 0} ≥ (c₀/4)H; and Q(θ(t)) > 0 forces P_X(g_t) > S − ε/2 by Step 4. So the near-maximizers have **lower density ≥ c₀/4 > 0 in every window of length ≥ H₀**, which is exactly what the note prints. The note also prints the two honest riders: c₀ = (ρ₀/2π)^N, so the density is positive and not effective; and Steuding's Lemma 1.8(i) gives the exact density (ρ₀/π)^N of the box over (0, T) with no window uniformity — the box side in unit-cube coordinates is 2ρ₀/2π = ρ₀/π, so that constant is right too.

**It earns the zoo's clause.** The zoo's EXECUTABLE TEST now says "false on a set of heights of lower density ≥ c₀/4 > 0 in every window of length ≥ H₀ (Theorem (E), Step 5, the measure remark)" — a claim the note now proves, and no longer the unsupported "positive lower density in every long window" that check-O §4.1 flagged.

**§7.** "the model reproduces the 8-thread measurement at X₀ exactly (1.144 s)" is gone; the note now reads "the model is normalized at X₀ (S is the ratio of the measured single-thread and 8-thread times there, so the 8-thread time 1.144 s is reproduced by construction, not as a validation)". That is item 7 discharged.

---

## §8 The zoo draft `zoo-IV19-proposed.md`: **all six amendments applied; insertable**

I recovered the pre-fix draft from git (`4c99262`, SHA-256 `2cdf79fa…`, matching `hashes-pre-fix.txt`) and diffed it word by word against the current file. Every change belongs to one of the six amendments; there is no unlisted edit.

1. **THEOREM (E)'s attribution** — replaced verbatim with check-O §9's wording (Bohr 1913; Turán 1960 Lemma p. 313 with an effective window; Weber 2009 Theorem 1 and (3.17)–(3.18), in general and effective; proof reproduced for this coefficient system, non-effective). The zoo does **not** print the Turán exponent, so the §0 FIX-FIRST does not touch it. ✔
2. **The counts** — "15 346 coefficients" → "8 562 nonzero coefficients"; "3.4·10⁸ coefficients" → "1.21·10⁸ nonzero coefficients; the exact counts are `m6-rung1-note.md` §1–§2, the f64 program summed 15 346 and 3.4·10⁸ terms". Recomputed, not merely labeled — better than the amendment asked. ✔
3. **The IV.7 anchor** — the full anchor in the STATEMENT and in the SOURCE. ✔
4. **The density clause** — "lower density ≥ c₀/4 > 0 in every window of length ≥ H₀ (Theorem (E), Step 5, the measure remark)", backed by §7 above; and the PNT shortcut now prints its measured accuracy, "1.4 % high at L = 10 — 1.4778 against the exact 1.4569 — and 0.02 % high at L = 20 — 12.5425 against 12.5397". ✔ (both figures as check-O §9 required)
5. **STATUS** — "**program-adjudicated (dual-model)**, `results/c2-m6/check-O.md` 2026-09-17", with the three-way split exactly as specified: theorem `[classical: cited at the page]`; instance + both controls + cost line `computationally-verified` (dual-model, independent implementation); the reading `[novelty: dual-model check 2026-09-17]` — an interpretation, not a theorem. The sentence "the mechanism is Bohr's/Weyl's; the statement for this coefficient system over every long window … are the program's" is **deleted**, replaced by "only the coefficient system and that reading are the program's". ✔
6. **SOURCE** — Turán and Weber added with their page anchors; Farmer §13.2 pp. 64–65 added next to the DH control with its content named; all Farmer references by section and page. ✔

**Extra, beyond the six:** the o(1) clause in the STATEMENT is re-normalized over the zeros, consistent with note §8. Correct, and the author flags it as an addition.

**Lint.** One `### ` heading and it is `### IV.19`. A case-insensitive grep for KICKSTART 10(g)'s four banned hedges over the note, the zoo draft and `SHARED.md`: no hits. A grep for twenty-one British spellings (the -our, -re, -ise/-yse and -lled families, plus the usual singletons): no hits. The header line still says "NOT inserted … pending the Opus re-check of the fix pass", which is now this file.

**Insertable: yes.** With the one-line note fix of §0 applied (which the zoo does not depend on), I endorse insertion.

---

## §9 Hashes

`hashes.txt` was recomputed against the disk: **85 entries, 85 match, 0 mismatches, 0 missing, and no file under `results/c2-m6/` is absent from the table** (excluding the two hash files themselves, as the header says). Spot values, recomputed:

| file | SHA-256 | in `SHARED.md` |
|---|---|---|
| `m6-rung1-note.md` | `515f544924936df53a1e6af0e1b90035c18b0a86ca78fe2c69f5e6d9535d1074` | ✔ |
| `zoo-IV19-proposed.md` | `580e9093c5c32a3bd54b885cdb55370224e38671b24fa7ce51718dc2a2711995` | ✔ |
| `SHARED.md` | `a7252dc7b60582fc9e5b83be5443cbe05daa54ae95a4322b20c6839d7843518c` | (self) |
| `verify/dh_true_count.py` | `33346c76935e364cc1a2190d9d76809086e0cfb0516e7bd01eb789add458dccc` | ✔ |
| `verify/dh_count_L20.rs` | `9c3eb4b9bdf738bdfe803148c831b1f36399ee4c0ed5c37ee6f8207ac0285828` | ✔ |
| `verify/dh_exact_eval.py` | `45c680e4029507d84f56cb6c79d9e9d62686862421630343403ff7a0dca44377` | ✔ |
| `verify/dh_online_shift_all36.py` | `6c5b04e51105d8bae93322a2cffc130a99999c7ad391513dc0f1fadfb55f4bce` | ✔ |

**The pre-fix/post-fix diff.** `hashes-pre-fix.txt` vs `hashes.txt`: exactly three files changed (the note, the zoo draft, `SHARED.md`); eleven files were added (the four scripts, their four logs, their outputs, and `check-O.md`/`FIX-BRIEF.md`, which were not in the pre-fix table); nothing was removed; **every other entry is identical**. The pre-fix note and zoo draft recovered from git commit `4c99262` hash to `6aae7081…` and `2cdf79fa…`, matching `hashes-pre-fix.txt` — so the preserved pre-fix state is genuine and the §13 ledger is auditable. I diffed both files against it: **every changed region of the note corresponds to a §13 ledger bullet, and no change is unlisted.**

---

## §10 What I checked and did not check (standing order 5)

* **Read at the page, this job:** `check-O.md` §1–§12; `FIX-BRIEF.md`; `m6-rung1-note.md` §0, §1, §2, §5.1, §5.3, §6 (setting, header, proof Steps 1–5, remarks, instance tables, the 10(n) paragraph), §7 (the normalization sentence), §8 (both paragraphs), §9, §10, §11, §12 (the new and rewritten rows), §13 in full; `zoo-IV19-proposed.md` in full; `SHARED.md` (the fix-pass block); `hashes.txt` and `hashes-pre-fix.txt`; `results/ccm-dh-test/dh.py` and `weilform.py` (`dh_coeffs`, `lambda_dh`); `results/c2-m2/verify/dh_negative_control_out.json`; the pre-fix note and zoo draft from git `4c99262`; Turán 1960 printed p. 313 **as a page image** (the OCR layer is garbled at the displays) plus the surrounding OCR for (2.3)–(2.7) and footnote 2; Weber arXiv:0806.3990v1 pp. 2 (image) and 9, 12 (text); Farmer arXiv:2211.11671v4 pp. 44, 54, 63, 64, 65, 66 from my own `pdftotext`; Steuding LNM 1877 printed p. 17.
* **Computed independently (session scratchpad, ≈ 6 minutes of wall time):** the ℤ[κ] minimal polynomial of κ; the exact Λ_DH recursion in ℤ[κ] over [2, 22 026] with per-prime coefficient vectors, its support, its 8 562 / 9 058 counts and the 120-digit evaluation of all 8 562; a coefficient-free C sieve of |S ∩ [2, N]| at N = 22 026 and N = 485 165 195; the closed form Λ_DH(2^k) for k = 1…30 against the exact recursion; my own B̂ / ĝ transform and W_{Z′} over the record's 36 points at L = 10, 20, 86.907 and L* = 86.90744354035114; the 40-digit refinement of all 36 recorded on-line points on the gamma-normalized S(u), their displacements and |f_DH| both ways; the full hash audit of `hashes.txt`; the word-level diffs of the note and the zoo draft against their pre-fix versions.
* **Not done:** I did not re-run the rung's Rust pipeline or re-measure the cost line (item 2 required only that no cost number moved, which the hash identity of every `verify/` output settles); I did not re-run `verify/dh_count_L20.rs` or `dh_exact_eval.py` (I counted S independently instead, and the step from |S| to the nonzero count at L = 20 is the author's labeled inference, which I did not attempt to prove); I did not re-derive (E)'s proof line by line (check-O.md §4.1 did, and the proof is unchanged apart from the added measure remark, which I did verify); I did not re-check the ζ positive control, the archimedean integrals or the §7 cost line (unchanged by the fix pass); no Lean was read or built; no commit (watchdogs commit).
* **Labeled inferences of mine:** none load-bearing. The only judgement call is the FIX-FIRST classification of the Turán exponent: it is a citation-fidelity defect, not a mathematical one, and no number or conclusion in the note depends on which of the two forms is right.

---

## §11 Traceability

| number | script |
|---|---|
| κ = 0.28407904384041229602829183239312616909…, κ⁴ + 2κ³ − 6κ² − 2κ + 1 = 1.6·10⁻⁵⁰ at 50 digits | inline mpmath, `recheck/` |
| **8 562 exact nonzeros; support = S; 1 239 + 7 323; 9 058 zeros coprime to 5; first zeros 22, 33, 38, 44, 57, 58, 62, 66, 76, 77, 82, 87; all 8 562 above 10⁻⁸⁰ at 120 digits; min 5.4392·10⁻⁸ at 2¹³** | `recheck/exact_lam.py`, `recheck/exact_lam_out.json` |
| **|S ∩ [2, 22 026]| = 8 562 = 1 239 + 7 323; |S ∩ [2, 485 165 195]| = 120 953 877 = 12 807 696 + 108 146 181; 25 614 562 primes ≤ e²⁰** | `recheck/sieveS.c` (clang -O3), `recheck/sieveS_L20.txt` |
| **Λ_DH(2^k) closed form for k = 1…30; Λ_DH(4) = −1.44223196461; Λ_DH(2¹³) = 5.4392·10⁻⁸; Λ_DH(2²⁷) = 1.21251·10⁻¹⁵** | `recheck/pow2_closed.py` |
| **Z = 0.22199690808403972; Σ ĝ over the 36 recorded points = 0.0048010831907523 (L = 10), 4.4642881736258·10⁻⁵ (L = 20)** | `recheck/wzp.py` |
| **the 36 refinements at 40 digits; displacements 1.187·10⁻⁶–1.140·10⁻³; |f_DH| recorded 4.849·10⁻⁶–3.699·10⁻³; max |f_DH| refined 3.54·10⁻³⁹; one point below 2·10⁻⁵** | `recheck/refine36.py`, `recheck/refine36.json`, `recheck/spot3.json` |
| **W_{Z′} at L* exact: 3.432164 → 3.4083861·10⁻¹⁰ (rel −6.93·10⁻³); at 86.907: 3.428215 → 3.4044547·10⁻¹⁰; L = 10: 0.0048010832 → 0.0048001176; L = 20: 4.4642882 → 4.4652466·10⁻⁵** | `recheck/wzp_Lstar.py` |
| the hash audit (85/85), the pre-fix/post-fix diff, the ledger completeness diff | inline Python over `hashes.txt`, `hashes-pre-fix.txt`, and git `4c99262` (`recheck/note_prefix.md`, `recheck/zoo_prefix.md`) |
| Turán (2.1) as printed; Weber p. 2 quotation | `recheck/turan313-3.png`, `recheck/turan_21.png`, `recheck/weber2-02.png`, `recheck/weber2_turan.png` (pdftoppm at 250 / 200 dpi) |
| Farmer pp. 44, 54, 63–66; Steuding p. 17 | `recheck/farmer_all.txt`, `recheck/farmer60_72.txt`, inline `pdftotext` page scan |

*End of re-check. The SHA-256 of this file is in the final report.*
