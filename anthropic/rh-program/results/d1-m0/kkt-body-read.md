# KKT body read (D-R4): arXiv:2408.03938 in full, with arXiv:2410.17158 alongside

**Date:** 2026-08-26 (Session 7 orchestration; D1 arm, repair D-R4).
**Reader discipline:** both PDFs fetched this session from the GCS arXiv mirror (direct arxiv.org unreachable; D-R10 record below), full text extracted with pdftotext and read end to end. Every quote below was copied from the extracted text and checked against the layout; page references are the papers' own printed page numbers.

## Sources on disk

| file | identity (from the PDF itself) | bytes | pages |
|---|---|---|---|
| `fetched-r3/r3s-09-kkt-2408.03938.pdf` | "Zeros of L-functions and large partial sums of Dirichlet coefficients," Bryce Kerr, Oleksiy Klurman, Jesse Thorner, arXiv:2408.03938v1 [math.NT] 7 Aug 2024 | 324,260 | 23 |
| `fetched-r3/r3s-10-2410.17158.pdf` | "Zeros of L-functions in families near the critical line," Valentin Blomer, Jesse Thorner, arXiv:2410.17158v1 [math.NT] 22 Oct 2024 | 348,144 | 21 |

Fetch record (D-R10): GCS mirror v1 fetched clean for both; `2408.03938v2` and `v3` returned 404 on the mirror (v1 is the version read — if a later revision exists it was not reachable this session). Direct arxiv.org remained unreachable.

## What the paper actually proves (structure, for the record)

Class: S(m) = entire L-functions L(s,π) = Σ λπ(n) n^{−s} with degree-m Euler product, functional equation (1.7), a weak Ramanujan hypothesis |α_{j,π}(p)| ≤ p^{θπ} with θπ ≤ 1 − 1/m (1.6), and the *averaged* coefficient bound (1.10): Σ_{x<n≤ex} |aπ(n)|²Λ(n)/n ≤ κ² + A₀/log(ex). Footnote 2 (p. 3): "In this paper, L(s, π) has no poles. We could easily modify the proofs to allow for a pole at s = 1." — so ζ itself is outside the stated class (and see "scope" below: it could never be a W2 target anyway).

**Theorem 1.3 (p. 4), verbatim in the essentials:** "Let δ ∈ (0, 1/2]. … There exist constants c13, c14, c15, c16, c17, c18 > 0 (depending on δ, κ, m, and A0) such that the following is true. Let C ≥ c13, x ∈ [exp((log C)^{1−1/(50m)}), √C], N ∈ [1, (log x)^{1/(100m)}], and L ∈ [c14 N^{2/ℓκ} (log C/log x)^{1−2δ}, c15 log x]. If |S(x, π)| = x(log x)^{κ−1}/N, then there exists φ ∈ R such that |φ| ≤ c16 N and

  #{ρ : L(ρ, π) = 0, |1 + iφ − ρ| < (L/log x)(log C/log x)^δ} ≥ c17 L.

If aπ(n) ∈ R for all n ≥ 1, then one may take φ = 0 when L ≥ c18 N^{6/κ}."

Tuned form (Remark, p. 4): with L = (ε^{1+δ}/4) log C and x = C^ε, "a positive proportion (≫_{δ,κ,m,A0} ε^{1+δ}) of the O(log C) nontrivial zeros β + iγ of L(s, χ) with 0 < β < 1 and |γ − φ| ≤ 1/4 must satisfy β ≥ 3/4." Corollary 1.1 (p. 1) is the Dirichlet-character case (primitive χ mod q of order k ≥ 2, x ∈ [exp((log q)^{49/50}), √q]); Corollary 1.2 (p. 3) the SL₂(Z) holomorphic Hecke-eigenform case; the p. 4 Remark extends to cuspidal automorphic π on GL_m(A_Q) with unitary central character under GRC, and to Rankin–Selberg L(s, π1 × π2) with one GRC factor. Proof route: Halász/GHS mean-value theory extended to the averaged class C_w(κ) (§2), a large-partial-sum ⟹ large |L(1−λ+iξ)/L(1+λ+iξ)| bridge (Prop. 3.3, p. 13), and a new "hybrid Euler–Hadamard product" favoring zeros near Re(s) = 1 without GRH (Prop. 4.1, §4); zero count extracted in §5 via a sign argument in which the u-integral (5.12) is ≤ 0, so the ratio in (3.8) is large only if ≫ λy₀ zeros sit in the K/log X disc — conclusion (5.15), p. 22.

---

## Gate (i) — explicit vs unspecified constants: **EFFECTIVE, NOWHERE EXPLICIT**

The paper's own statement (p. 5, end of §1, verbatim): "Throughout this paper, all implied constants in our O(·), ≪, and ≫ notation depend on at most the numbers κ, A0, m, and δ in Theorem 1.3. All implied constants are effectively computable. Each constant in the sequence c1, c2, c3, . . . is effectively computable."

Status by statement:
- **Corollary 1.1:** constants c4–c8 (plus c3 from GS for the φ = 0 order-k clause) — named, effective, **no numerical value anywhere**.
- **Corollary 1.2:** c9–c12 — same status.
- **Theorem 1.3:** c13–c18 — same status; the conclusion's count is "≥ c17 L" and the raw form of the proof gives only "≫ λy0" (5.15).
- Interior constants c19–c29 (Halász machinery, Prop. 3.3's c21–c22, §5's c26–c28) — same status. No section computes any of them; the chain runs through GHS Compositio 155 (2019) Halász theory, Soundararajan's weak-subconvexity lemmas (Ann. of Math. 172, 2010), and [8, Lemma 2.3], all themselves inexplicit.

Consequence for a witness: **applicability is not even checkable** for a concrete (q, χ, x, N): the hypotheses require q ≥ c4 (resp. C ≥ c13) and L inside a window whose endpoints carry c5/c6 (c14/c15) — with the constants unspecified, no finite transcript can verify that the theorem's hypotheses hold, before one even reaches the conclusion. This is asymptotic-in-conductor mathematics with an effectivity certificate, not an explicit inequality.

## Gate (ii) — existence companion needed? **NO — the theorem is itself a zero-EXISTENCE statement** (the D-R4 worry dissolves in the body)

The worry was that "repulsion away from the critical line" might only assert a zero-free neighborhood of the line — which is GRH-compatible (GRH tolerates zero-sparse stretches). The body says otherwise: the conclusion of Theorem 1.3 is a **lower bound on a zero count in a disc centered at 1 + iφ**: #{ρ : |1 + iφ − ρ| < r} ≥ c17 L ≥ 1. In the tuned corollaries r = 1/4, so every counted zero has β ≥ 3/4 and |γ − φ| ≤ 1/4 — each one singly violates GRH. The paper says so in words (p. 2): if S(q^ε, χ) is large "then a much larger positive proportion (≫δ ε^{1+δ}) of the O(log q) nontrivial zeros β + iγ of L(s, χ) with 0 < β < 1 and |γ − φ| ≤ 1/4 satisfy β ≥ 3/4," and (p. 4 Remark) "large partial sums of λπ(n) strongly repel the nontrivial zeros away from the critical line" — where "repel" means *the zeros that must exist are pushed to β ≥ 3/4*, not that a neighborhood is emptied. Sharpness check the paper itself supplies (p. 2): Linnik's unconditional upper bound #{ρ : |ρ − (1 + it)| ≤ r} ≪ r log(q(|t|+3)) matches (1.2) up to (1/ε)^{1+δ} — the lower bound is real zero mass, not vacuous.

**One format-level proviso (radius pinning):** in the general Theorem 1.3 window L may run up to c15 log x, making the disc radius (L/log x)(log C/log x)^δ exceed 1/2, in which case the counted zeros could sit on the critical line and nothing violates GRH. Any witness format must pin its parameters so the disc radius is < 1/2 (the tuned corollary choices give 1/4). With that pinning, **no unconditional low-lying-zero-existence companion is needed**: existence is the theorem's own conclusion.

**What 2410.17158 is and is not:** Blomer–Thorner is a family zero-DENSITY paper — averaged UPPER bounds: Theorem 1.1 (p. 2): "(1/V(q)) Σ_{π∈F(q)} Nπ(σ,T)/L(1,π,Ad) ≪_B T^m q^{−B(σ−1/2)} F(q)(log q)^5," with RF(q) ≪ exp(C1 log q/log log q) for "an effectively computable constant C1" (p. 2). It is the opposite direction (almost-all-π non-existence), also asymptotic with unspecified ≪_B constants. It is **not** an existence companion and closes no gate; its D1 relevance is contextual — it quantifies how thin the haystack of possible GRH-violators in a family is (and Theorem 1.5's average central-zero bound recovers the GRH-conditional prediction on average), i.e. it prices the search, it never certifies a hit.

## Gate (iii) — is the honest machine-checkable threshold an explicit GRH-conditional partial-sum bound, with KKT as pointer? **YES — confirmed, with one honest caveat**

Because of gate (i), KKT's own threshold ("|S| = x(log x)^{κ−1}/N with N ≤ (log x)^{1/(100m)}, parameters in the c-windows") cannot back a checkable certificate today. The sound certificate shape is the classical one: an inequality "GRH for L(s,χ) ⟹ |S(x,χ)| ≤ f(x,q)" with **explicit** f, so that a certified evaluation |S(x,χ)| > f(x,q) is a one-implication disproof of GRH for that χ. KKT is then pointer-grade: it says *what a violation would look like* (a positive proportion ≫ ε^{1+δ} of the low-lying zeros pushed to β ≥ 3/4, at φ = 0 for real coefficients / order-2 characters) and it *directs the detector* (anomalously large certified sums below threshold flag candidate χ) — exactly the role the direction file's detector row already assigns it.

**Caveat (verified against the paper's own account of the conditional literature, p. 1):** the GRH-conditional bound in the relevant window is Granville–Soundararajan's S(x,χ) = o_ε(x) for (log x)/log log q → ∞ [7], and its cusp-form analogue Lamzouri [11] — both **asymptotic**, not explicit. The Montgomery–Vaughan-type explicit conditional bounds (√q log log q class) live at x ≳ √q and are weaker than trivial in KKT's window x ∈ [exp((log q)^{49/50}), √q]. I could not verify (network-limited; and I believe it does not exist) any off-the-shelf explicit-constant version of the GS conditional bound in the medium range. So even the gate-(iii) route requires a derivation: an explicit-constant "GRH ⟹ |S(x,χ)| ≤ ε(x,q)·x" in the medium range (standard conditional explicit-formula work, same genre as explicit RH-conditional ψ(x) bounds — real but bounded work, and of certificate grade once done).

## Zoo III.9 adjudication

Entry III.9's Session-6 caution says the abstract supports only "large partial sums repel low-lying zeros away from the line," yielding a witness "only with an existence companion or explicit constants." **Adjudication against the body:** the scout-recalled stronger gloss "certified large partial sums ⇒ off-line low-lying zero" is **mathematically CORRECT as stated in the body** — Theorem 1.3's conclusion is zero existence off the line (gate ii), with the radius-pinning proviso — so the "existence companion" fork of the caution is resolved and should be dropped. The "explicit constants" fork is the one that bites: the gloss's word "certified" fails (gate i), so III.9's surviving-refutation-direction line stays pointer-grade ("a B2 instrument"), which is what the entry already says. Net: III.9's caution should be superseded by a dated note "body read 2026-08-26: existence internal to Thm 1.3 (companion fork resolved); constants effective-not-explicit (certified fork stands); see results/d1-m0/kkt-body-read.md." (Orchestrator propagates; nothing edited here.)

## W2 verdict: **DEMOTED — pointer-only, per gate (iii)**, with a contingent re-based format W2′

W2 as commissioned ("KKT certified large partial sum" as a machine-checkable GRH-disproof witness) cannot be specified: the checkable-threshold half fails gate (i). Two named upgrade paths, either of which un-demotes it:

- **(a) KKT constant extraction:** compute c4–c8 (Dirichlet case suffices) through GHS-Halász + Prop. 3.3 + §5. Research-grade (the chain passes through three inexplicit papers), months, not bookkeeping. Payoff: the unconditional, family-wide format.
- **(b) Explicit conditional threshold (cheaper, recommended):** derive an explicit-constant GRH-conditional medium-range bound |S(x,χ)| ≤ f(x,q) and base the witness on it. KKT stays pointer/amplifier.

**W2′ sketch (contingent on (b); one paragraph because the format is genuinely small):** transcript = (q, χ as index or defining data, x, S_exact, threshold check). Soundness statement (Lean, comparator style): "GRH_χ ⟹ |S(x,χ)| ≤ f(x,q)" as the displayed analytic hypothesis (discharged when (b) lands, exactly the EnclOK pattern), plus the kernel-checked arithmetic: S_exact = Σ_{n≤x} χ(n) computed in **exact cyclotomic integer arithmetic Z[ζ_k]** (character values are roots of unity — this is the unique witness format in the D1 line whose evaluation needs NO interval arithmetic at all), and the certified comparison |S_exact|² > f(x,q)² in exact rational arithmetic. Compute cost is trivial: the window x ≤ √q means ≤ 10⁶ terms even at q ~ 10¹²; the checker is NumericCert-pattern `decide +kernel`. Detector use unchanged: sub-threshold large sums rank candidate χ for the conductor-Fuchs/W1 pipeline.

**Scope limit to record in the direction file (orchestrator):** W2/W2′ is strictly a GRH-family witness — ζ is outside S(m) (pole, footnote 2) and outside the asymptotic regime (fixed C < c13), and a GRH violation for some L(s,χ) does not disprove RH for ζ. W2 therefore never feeds the Λ > 0 channel or M5's conversion loop; it is a complementary product, exactly as the "complementary to Λ>0" clause in the direction file already hints, now with the reason on the record.

## D-R10 network record

- GCS mirror (storage.googleapis.com): WORKED — both v1 PDFs fetched and read in full (this document's basis).
- arxiv.org direct: unreachable this session (not retried past the mandate since the mirror sufficed).
- 2408.03938 v2/v3: 404 on the mirror; read is of v1. Journal/revision status unverified this session.
