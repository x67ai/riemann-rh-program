# M2a barrier-certificate contract — the producer/checker specification for the formal Λ ≤ 0.2 instance

**Status:** v1.0, 2026-09-02 (Session 14, D1 M2a contract agent; workflow `d1-audit-m2a-s14`).
**This file is the contract.** The Lean stream building `Zeta23/DBN/BarrierCert.lean` and
`Zeta23/DBN/Instance02.lean` reads THIS file as the normative specification of the transcript data,
the checker's integer checks, the displayed hypotheses and the theorem shapes; the two untrusted
producers (Arb/FLINT leg, mpmath-ball leg) write files conforming to `barrier-schema.json` (this
directory). It is the M2a analogue of `results/d1-m1/FORMAT.md` (the M1 v1 W1 contract), reuses that
contract's row vocabulary verbatim wherever a barrier transcript IS a W1 exclusion transcript, and
changes nothing in it. Any change to a check or a hypothesis here is a version bump of this file and
of the schema, recorded here.

**Mandate.** `results/d1-m0/m2a-m2b-design.md` (the D-R2 repair note) §1.3 statement skeleton, §1.6
work-breakdown items (b)–(e), §4 enclosure conventions, §7 the `Defs.lean` deviation record;
`results/d1-m1/AUDIT.md` §4 (D-1 … D-4) and §6; `results/d1-m1/RUN-REPORT.md` §5–§6 (what M2a must
add, in order). Constraints (1)–(8) of the M1 v1 audit verdict are carried forward and discharged or
recorded below (§13.1).

**Trust language (binding; D-R3/D-R8; FORMAT.md §8.2 addendum of 2026-09-02).** Every public sentence
about an accepted M2a transcript reads *"kernel-checked modulo the displayed hypotheses"* — with the
hypotheses named (§6) — never "fully machine-checked". Producers are UNTRUSTED by design; their output
enters the trusted statement only through the displayed enclosure hypotheses. The Λ bracket of record
is **0 ≤ Λ ≤ 0.2** (Rodgers–Tao; Platt–Trudgian Corollary 2); the strict "Λ < 0.2" is never written
(`results/corpus-routing.md` caveat 9). Nothing about the Gomila claim is a record (§11).

**Sources, at exact locations (standing order 5 — nothing load-bearing from memory).** All page
numbers below are PDF pages of the on-disk files, which for the arXiv Polymath15 file coincide with
its printed page numbers (checked: the running head "64 D.H.J. POLYMATH" opens PDF page 64). Text
was extracted with `pdftotext -layout`; every quotation was read from that extraction this session.

* **P15** = `fetched/p3-22a4-polymath15-2019-upper-bound-debruijn-newman.pdf` — D.H.J. Polymath,
  *Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for
  the de Bruijn–Newman constant*, arXiv:1904.12438v2. The ONLY on-disk Polymath15 text (see the
  corpus finding below). Locations used: Theorem 1.2 p2; the simplified barrier region p3; the region
  (5) p3; eqs. (6)–(11) (M₀, α, M_t, B_t) p4; Theorem 1.3 with (13)–(24) p6 and the holomorphy/jump
  remark p6; Corollary 1.4 p7; Theorem 1.5 p9–10; Theorem 3.2 (de Bruijn) p14; Proposition 3.3 p15;
  eqs. (69)–(74) and Proposition 6.6 p30–31, the "(24) from 6.6(vi)" remark p31; §8.2 regions and
  Proposition 8.1 p38–39, its proof (82)–(87) p39–42; §8.3 (claim (c): the tail) with Lemma 8.2 and
  Remark 8.3 p42–44; §8.4 (claim (a): the barrier algorithm, eq. (91)) p44–45, Lemma 8.4 p46, mesh
  counts p49; §8.5 (claim (b)) with Lemma 8.5 p50–56; Proposition 9.1 p56; §10 with Table 1 p62–67.
* **PT** = `fetched/p3-22a1-platt-trudgian-2020-rh-true-up-to-3e12.pdf` — D. Platt, T. Trudgian,
  *The Riemann hypothesis is true up to 3·10¹²*, arXiv:2004.09765v1 (Bull. LMS 53 (2021)). Theorem 1
  p2; §3.4 (the Table-1 pairing, Corollary 2, the "H > 2.51·10¹²" and "higher than 10¹³ … Λ < 0.19"
  sentences) p5.
* **Defs** = `Zeta23/DBN/Defs.lean` (working tree `~/rh-lean-work/zeta-23-lean-main`, identical to
  `rh-program/lean/Zeta23/DBN/Defs.lean`): `Phi` line 82, `Ht` line 89, `ZeroVerification` line 98,
  `Polymath15Bridge` line 109.
* **W1** = `Zeta23/W1/{Format,Checker,Soundness,ArgPrincipleBridge}.lean` and
  `results/d1-m1/FORMAT.md` v1.0 with its 2026-09-02 errata; `results/d1-m1/w1-schema.json`.
* **Gomila** = the audit repository `judegomila/dbn-lambda-01787854-candidate-audit`, branch
  `lean/certificate-and-argument-principle`, commit `ea09b2f6aa7afe60706b67c87b202126f3149e8c`, as
  cloned this session by the Lean-branch verify agent into `~/rh-lean-work/gomila-ap/repo/`
  (`results/d1-m1/gomila-lean-branch-verify.md` §1). Files read: `BARRIER_CERTIFICATE.md`,
  `CANDIDATE_PARAMETERS.md`, `DERIVATIVE_BOX_LEMMA.md`, `ERROR_CONSTANT_WELD.md`, `NATIVE_BINDING.md`,
  `TAIL_LEMMA.md` (§1), `WINDOW_FREEZE_THEOREM.md`, `barrier/certificates/barrier_target_closed.log`,
  `barrier/src/TloopSinglemat_closed_cert.c` (its `printf` lines only), the finite shards
  `certificates/p*.log.gz` (first lines), `verifiers/verify_finite_and_binding.py` (row regex).

**Corpus finding (recorded, not repaired here — the fix is a rename plus a routing note).** The file
`fetched/p3-22a5-polymath15-2019-upper-bound-published-forum-pi.pdf`, listed program-wide as "the
published Polymath15 (Forum Math. Pi)", is NOT Polymath15: its first page reads *"Forum of Mathematics,
Pi (2020), Vol. 8, e6, 62 pages … THE DE BRUIJN–NEWMAN CONSTANT IS NON-NEGATIVE, BRAD RODGERS and
TERENCE TAO"* — it is the published Rodgers–Tao paper, a second copy of `p3-22a3` (which is the arXiv
v5 of the same paper; its first page carries the "Forum of Mathematics, Pi (2021), vol. ???" stub).
Polymath15 was published in *Research in the Mathematical Sciences* 6 (2019), art. 31 (PT's citation
[24] and their "page 65 of [24]" refer to that version; the arXiv v2 has Table 1 on page 64). No
published Polymath15 text is on disk; this contract cites the arXiv v2 only, and the brief's
instruction to cite "p3-22a4/p3-22a5" pages is discharged with p3-22a4 alone. Affected records:
`results/corpus-routing.md` line 101 ("Polymath15 Λ ≤ 0.22 (arXiv + published)"),
`FETCH-LIST-RESPONSE.md` line 324, and the M1/M2a briefs. The mislabel is load-bearing for nothing
(every Polymath15 quotation in the program was taken from p3-22a4).

---

## 1. What the certificate certifies

### 1.1 The target theorem (ray form, design note §1.2; the shape is fixed by `Defs.lean`)

    ∀ t : ℝ, 1/5 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0

"every H_t with t ≥ 0.2 has only real zeros" — the assertion Λ ≤ 0.2 without the word Λ — modulo the
displayed hypotheses of §6, with `Ht` the Bochner-integral definition of `Defs.lean` line 89
(H_t(z) = ∫₀^∞ e^{tu²} Φ(u) cos(zu) du, Φ from P15 eq. (2)).

### 1.2 The analytic input the certificate feeds (P15 Theorem 1.2, p2, quoted)

> Theorem 1.2 (Upper bound criterion). Suppose that t₀, X > 0 and 0 < y₀ ≤ 1 obey the following
> hypotheses:
> (i) (Numerical verification of RH at initial time 0) There are no zeroes ζ(σ + iT) = 0 with
> (1+y₀)/2 ≤ σ ≤ 1 and 0 ≤ T ≤ X/2.
> (ii) (Asymptotic zero-free region at final time t₀) There are no zeroes H_{t₀}(x + iy) = 0 with
> x ≥ X + √(1 − y₀²) and y₀ ≤ y ≤ √(1 − 2t₀).
> (iii) (Barrier at intermediate times) There are no zeroes H_t(x + iy) = 0 with X ≤ x ≤ X + √(1 − y₀²),
> √(y₀² + 2(t₀ − t)) ≤ y ≤ √(1 − 2t), and 0 ≤ t ≤ t₀.
> Then Λ ≤ t₀ + ½y₀².

and, p3: *"In practice, we have found it convenient numerically to replace the barrier region in
Theorem 1.2 with the larger and simpler region X ≤ x ≤ X + 1; y₀ ≤ y ≤ 1; 0 ≤ t ≤ t₀."* The proof
(p14–16) is Proposition 3.3 (p15: under (i)–(iii), "there are no zeroes H_{t₀}(x + iy) = 0 with x ∈ ℝ
and y ≥ y₀") followed by de Bruijn's Theorem 3.2 (p14: no zeros of H_{t₀} with y > y₀ ⟹ Λ ≤ t₀ + ½y₀²).
Hypothesis (ii) is a statement at the FINAL time t₀ only; hypothesis (iii) is the only one that
quantifies over intermediate times. This asymmetry is load-bearing for §3.2.

### 1.3 The two certified statements (the "lanes")

For the instance parameters (t₀, X, y₀) of §9 the certificate consists of two lanes, each with its own
transcript documents, checker and displayed hypotheses:

* **Lane B — the barrier** (hypothesis (iii), in its simplified box form). Certified statement:

      (B)  ∀ t ∈ [0, t₀], ∀ z ∈ R := [X, X+1] × [y₀, 1] (closed),  H_t(z) ≠ 0.

  Mechanism (§4): a finite list of consecutive time prisms [τ_j, τ_{j+1}] covering [0, t₀]; at each
  seam τ_j a W1-style exclusion transcript (winding number 0 around ∂R, boundary nonvanishing, a
  modulus floor) for the producer's holomorphic approximant f of g_{τ_j} := H_{τ_j}/B_{τ_j}, plus two
  integers per prism — the approximation defect E (|g_{τ_j} − f| ≤ E/K on ∂R) and the time
  displacement D (|g_t − g_{τ_j}| ≤ D/K on ∂R for t in the prism) — with the single integer gate
  (E + D)/K < floor. Soundness is a Rouché-type argument reduced to the argument principle already
  in the repository plus one new elementary lemma (§4.6).

* **Lane A — the asymptotic region at the final time** (hypothesis (ii)). Certified statement:

      (A)  ∀ x ≥ X + 1, ∀ y ∈ [y₀, yA],  H_{t₀}(x + iy) ≠ 0,     yA rational with yA² ≥ 1 − 2t₀.

  Mechanism (§5): consecutive Riemann–Siegel window rows [N₋, N₊] from N_start to N_end, each a
  pointwise modulus floor (Corollary 1.4 applied uniformly on the window), kernel-checked as E < T;
  and beyond N_end the derived tail lemma (Lemma T, §5.4) whose finite numeric antecedent is a
  kernel-checked row and whose analytic reduction is a displayed hypothesis (H-TAIL).

(B) with y-range [y₀, 1] and (A) with x ≥ X+1 together imply the paper's (ii) and (iii): the strip
X + √(1−y₀²) ≤ x ≤ X + 1 at time t₀ is inside (B) (§3.2, derivation D-H3). This is why the amended
bridge hypothesis of §3.2 is stated with the all-rational boundaries X, X+1, y₀, 1 and y² ≤ 1 − 2t₀,
and why no square root ever appears in a transcript.

### 1.4 What "nonvanishing on every prism" means, precisely

For prism j = [τ_j, τ_{j+1}] (τ_J := t₀): for EVERY real t with τ_j ≤ t ≤ τ_{j+1} and EVERY z in the
closed rectangle R, H_t(z) ≠ 0. The kernel does not see t: the per-prism data are the seam
transcript (an assertion at the single time τ_j) and the two integers E, D; the "for every t in the
prism" is delivered by the soundness theorem from the displacement hypothesis (§4.5), not by
enclosures indexed by t. §4.7 records why the alternative — rows uniform in t — was rejected.

---

## 2. The Polymath15 inputs, quoted at exact page (what the producers implement, what the hypotheses mean)

All of the following are P15 (arXiv v2) text; nothing here is re-derived except where marked
"derivation".

**2.1 The normalizer (p4).** *"we first introduce the function M₀ : ℂ∖(−∞,1] → ℂ∖{0} defined by the
formula (6) M₀(s) := (1/8)·(s(s−1)/2)·π^{−s/2}·√(2π)·exp((s/2 − 1/2)Log(s/2) − s/2), where Log denotes
the standard branch of the complex logarithm, with branch cut at the negative axis and imaginary part
in (−π, π]."* — *"(9) α(s) = 1/s + 1/(s−1) − ½ log π + ½ Log(s/2) − 1/(2s) = 1/(2s) + 1/(s−1) +
½ Log(s/(2π))."* — *"(10) M_t(s) := exp((t/4)α(s)²) M₀(s) for any t ≥ 0."* — *"(11) B_t(x + iy) :=
M_t((1 + y − ix)/2). For fixed t ≥ 0 and y > 0, B_t(x + iy) is non-vanishing".* With z = x + iy one
has (1 + y − ix)/2 = (1 − iz)/2 (derivation: iz = ix − y). The Lean transcription is §3.4.

**2.2 The region (5) (p3):** *"0 < t ≤ 1/2; 0 ≤ y ≤ 1; x ≥ 200"* — every Theorem-1.3 estimate is
stated on this region. The barrier box and the asymptotic half-strip of the instance lie in it
(X ≈ 5·10¹², y ∈ [y₀, 1], t ∈ (0, t₀]); the endpoint t = 0 is outside (5) and is handled in §4.4.

**2.3 The effective approximation (p6, Theorem 1.3).** *"Let t, x, y lie in the region (5). Then we
have (13) H_t(x+iy)/B_t(x+iy) = f_t(x+iy) + O_≤(e_A + e_B + e_{C,0}) where (14) f_t(x+iy) :=
Σ_{n=1}^{N} b_n^t/n^{s*} + γ Σ_{n=1}^{N} n^y b_n^t/n^{s*+κ}, (15) b_n^t := exp((t/4) log² n),
(16) γ = γ(x+iy) := M_t((1−y+ix)/2)/M_t((1+y−ix)/2), (17) s* = s*(x+iy) := (1+y−ix)/2 +
(t/2)α((1+y−ix)/2), (18) κ = κ(x+iy) := (t/2)(α((1−y+ix)/2) − α((1+y+ix)/2)), (19) N :=
⌊√(x/(4π) + t/16)⌋, and e_A, e_B, e_{C,0} are certain explicitly computable positive quantities
depending on t and x + iy [footnote: See (71)–(74) for the precise definition of these quantities].
Furthermore, we have the following bounds: (20) |γ| ≤ e^{0.02y}(x/4π)^{−y/2}; (21) Re s* ≥ (1+y)/2 +
(t/4) log(x/4π) − (t/(2x²))(1 − 3y + 4y(1+y)/x²)_+; (22) |κ| ≤ ty/(2(x−6)); (23) e_A + e_B ≤
Σ_{n=1}^{N} (1 + |γ|N^{|κ|} … ) [the displayed (23) — producers take e_A, e_B from (71)–(72) and
Proposition 6.6(iv)–(v) directly, §10]; (24) e_{C,0} ≤ (x/4π)^{−(1+y)/4} exp(−(t/16)log²(x/4π) +
(3|log(x/4π) + iπ/2| + 10.44)/(x−12))·(1 + 1.24(3^y + 3^{−y})/(N − 0.125))."* And p6: *"We remark
that f_t(x+iy) is a holomorphic function of x+iy in the region (5) as long as N is constant, but has
jump discontinuities when N is incremented."*

**2.4 The exact error quantities (p30–31).** *"(70) H_t(x+iy)/B_t(x+iy) = f_t(x+iy) + O_≤(e_A + e_B +
e_{C,0}) where (71) e_A := |γ| Σ_{n=1}^{N} n^y b_n^t/n^{Re s* + Re κ} ε_{t,n}(s_−), (72) e_B :=
Σ_{n=1}^{N} b_n^t/n^{Re s*} ε_{t,n}(s_+), (73) e_C := exp(tπ²/64)|M₀′(iT′)|/|M_t(s_+)| ·
(ε̃(s_−) + ε̃(s_+)), (74) e_{C,0} := exp(tπ²/64)|M₀′(iT′)|/|M_t(s_+)| · (1 + ε̃(s_−) + ε̃(s_+))"*;
Proposition 6.6 (p31) gives the explicit majorants (i)–(vi) — in particular *(vi) e_{C,0} ≤
(x/4π)^{−(1+y)/4} exp(−(t/16)log²(x/4π) + (3|log(x/4π)+iπ/2| + 3.58)/(x − 8.52))·(1 +
1.24(3^y+3^{−y})/(N − 0.125) + 6.92/(x − 12))* — followed by (p31): *"Note that to obtain the bound
(24) from Proposition 6.6(vi) we may simply use the inequality 1 + u ≤ exp(u) for any u ∈ ℝ, and
then bound 1/(x−8.52) ≤ 1/(x−12)."* **Derivation D-2.4 (the displayed constant 10.44 does not follow;
10.50 does).** From 6.6(vi) with a := 1.24(3^y+3^{−y})/(N−0.125) ≥ 0, b := 6.92/(x−12) ≥ 0: (1 + a + b)
≤ (1 + a)(1 + b) ≤ (1 + a)e^{b} (the first since ab ≥ 0, the second since 1 + b ≤ e^{b}); and
1/(x − 8.52) ≤ 1/(x − 12) for x > 12 (the paper's "bound", read as an inequality between the two
positive reciprocals, is true in this direction). Hence e_{C,0} ≤ (x/4π)^{−(1+y)/4}
exp(−(t/16)log²(x/4π) + (3|log(x/4π)+iπ/2| + 3.58 + 6.92)/(x−12))·(1 + a), and 3.58 + 6.92 = 10.50.
The displayed 10.44 is therefore not a consequence of 6.6(vi) as written; **producers MUST use the
10.50 form (or 6.6(vi) itself), never the displayed 10.44** — the same weld Gomila records in
`ERROR_CONSTANT_WELD.md` ("3.58 + 6.92 = 21/2 = 10.50"). At x ≈ 5·10¹² the numerical difference is
≈ 10⁻¹², immaterial for margins; the discipline matters.

**2.5 Corollary 1.4 (p7):** *"Let t, x, y lie in the region (5), and let f_t, e_A, e_B, e_{C,0} be as
in Theorem 1.3. If one has the inequality (25) |f_t(x+iy)| > e_A + e_B + e_{C,0} then H_t(x+iy) ≠ 0."*
This is Lane A's row semantics (§5.2) and the boundary-nonvanishing half of Lane B.

**2.6 The barrier algorithm (§8.4, p44–45; quoted because Lane B is its certificate form).** *"As
N = N₀ is constant in this region, the function f_t(x+iy) is holomorphic, so by Rouché's theorem, it
suffices to show that for each time 0 ≤ t ≤ 0.2, as x+iy traverses the boundary ∂R of the rectangle
R := {x+iy : X₀ − 0.5 ≤ x ≤ X₀ + 0.5; 0.2 ≤ y ≤ 1}, the function f_t(x+iy) stays outside of the ball
B := {z : |z| ≤ 1.25 × 10⁻³}, and furthermore has a winding number of zero around the origin."* …
*"If one has a derivative bound |∂f_t/∂z| ≤ D_z on the boundary of the rectangle, the polygonal path
and the true trajectory f_t(∂R) differ by a distance of at most D_z/(2n), and the latter will have
the same winding number around the origin (and stay outside of the ball B) as long as
|f_t(x_j+iy_j)| > 1.25 × 10⁻³ + D_z/(2n). Furthermore, the same is true for nearby times
t ≤ t′ ≤ 0.2 to t, as long as one has the stronger bound (91) |f_t(x_j+iy_j)| > 1.25 × 10⁻³ +
D_z/(2n) + D_t|t′ − t| and a bound of the form |∂f_t̃/∂t| ≤ D_t for t ≤ t̃ ≤ 0.2 and z ∈ ∂R."* Lemma 8.4
(p46) supplies the pointwise majorants for |∂f_t/∂z| and |∂f_t/∂t| (the two displays on p46, in
terms of b_n^t, Re s*, |γ|, N, |κ|, x, y, t). Mesh record (p49): *"The number of rectangle mesh points
varies with t ranging from 11076 at t = 0 to 56 at t = 0.195"*, for X₀ = 6 × 10¹⁰ + 83952.

**2.7 The tail (§8.3, p42–44).** *"By Proposition 8.1, it suffices to establish the bound |f_t(x+iy)| >
1.25 × 10⁻³. In fact we will establish the stronger estimate (88) f_t(x+iy) = 1 + O_≤(0.955)."* … *"it
thus suffices to show that (89) Σ_{n=1}^{N} b_n^{0.2}/n^σ + |γ| Σ_{n=1}^{N} n^y b_n^{0.2}/n^{σ−|κ|} <
1.955. Our main tool here will be Lemma 8.2. Let N ≥ N₀ ≥ 1 be natural numbers, and let σ, t > 0 be
such that σ > (t/2) log N. Then Σ_{n=1}^{N} b_n^t/n^σ ≤ Σ_{n=1}^{N₀} b_n^t/n^σ + max(N₀^{1−σ} b_{N₀}^t,
N^{1−σ} b_N^t) log(N/N₀)."* (Proof p43: the summands decrease for 1 ≤ n ≤ N by the identity
b_n^t/n^σ = exp((t/4)(log N − log n)² − (t/4)log² N)/n^{σ − (t/2)log N}; integral test; convexity of
(1−σ)u + (t/4)u².) Their instantiation at t = 0.2, y ∈ [0.2, 1], N₁ = 1.5 × 10⁶ gives A ≤ 1.88 and
B ≤ 0.075 (p44); footnote 6 (p44) leaves the monotonicity of B in N "to the interested reader".
Lemma T of §5.4 is this argument re-derived with every step explicit and parametrized.

**2.8 Table 1 and its evidential status (§10, p63–67).** Table 1 (p64), row 2: *"5 × 10¹² + 194858 |
0.186 | 0.16733 | 0.20 | 0 | 630783 | 0.0376"* (columns: X, t₀, y₀, Λ, Winding Number, N₀,
|f_t(x+iy)| lower bound). On how the rows were established (p66): *"we thus (in view of the
conservative safety margin in our lower bounds for |f_{t₀}(x + iy₀)|) expect to be able to verify the
hypothesis in Theorem 1.2(iii) for any choice of parameters t₀, y₀, N₀ as above. The main remaining
difficulty is then to verify the barrier hypothesis (Theorem 1.2(ii)). This is by far the most
numerically intensive step, and we proceed as in Section 8.4"* [the labels (ii)/(iii) are swapped in
this sentence relative to the theorem statement: "barrier" is (iii)], and (p66–67): *"All barrier
runs generated a winding number of zero for each rectangle and the scripts completed successfully
without any errors. For all barrier locations, the computations of the mesh points where calculated at
20 digits accuracy except for the highest two where 10 digits where used."* **Reading, recorded as a
finding for §5.5:** for the Table-1 rows the BARRIER hypothesis was computed and recorded (winding
0 per rectangle); the ASYMPTOTIC hypothesis (ii) is stated as expected-verifiable from the N₀ lower
bound (0.0376 for row 2, target ≥ 0.03) plus the §8.3/§8.5 method — not as a recorded per-window
run. PT's Corollary 2 (p5) rests on this row.

**2.9 PT Theorem 1 and §3.4 (p2, p5).** *"Theorem 1. The Riemann hypothesis is true up to height
3 000 175 332 800. That is, the lowest 12 363 153 437 138 non-trivial zeroes ρ have ℜρ = 1/2."*
§3.4: *"The second row in Table 1 on page 65 of [24] shows that one may take Λ ≤ 0.2 provided one has
shown H > 2.51 · 10¹². This leads to the following. Corollary 2. We have Λ ≤ 0.2. The next entry in
Table 1 of [24] is conditional on taking H a little higher than 10¹³, which of course, is not
achieved by Theorem 1. This would enable one to prove Λ < 0.19."*
