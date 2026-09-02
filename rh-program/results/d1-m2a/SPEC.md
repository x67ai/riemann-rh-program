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

---

## 3. The Lean-facing statement: `Defs.lean` as elaborated, one defect, and the amended bridge

### 3.1 The elaborated shapes (Defs, lines 82–117; `#print`-verified per the design note §7)

    def Phi (u : ℝ) : ℝ := ∑' n : ℕ+, (2 * π ^ 2 * (n : ℝ) ^ 4 * exp (9 * u) - 3 * π * (n : ℝ) ^ 2 * exp (5 * u)) * exp (-π * (n : ℝ) ^ 2 * exp (4 * u))
    def Ht (t : ℝ) (z : ℂ) : ℂ := ∫ u in Set.Ioi (0 : ℝ), Complex.exp (t * u ^ 2) * (Phi u : ℂ) * Complex.cos (z * u)
    def ZeroVerification (σ₀ T₀ : ℝ) : Prop := ∀ s : ℂ, riemannZeta s = 0 → σ₀ ≤ s.re → s.re ≤ 1 → 0 ≤ s.im → s.im ≤ T₀ → False
    def Polymath15Bridge : Prop :=
      ∀ t₀ X y₀ : ℝ, 0 < t₀ → 0 < X → 0 < y₀ → y₀ ≤ 1 →
        ZeroVerification ((1 + y₀) / 2) (X / 2) →
        (∀ x y : ℝ, X ≤ x → y₀ ≤ y → y ≤ 1 → ∀ t : ℝ, 0 ≤ t → t ≤ t₀ → Ht t (x + y * Complex.I) ≠ 0) →
        ∀ t : ℝ, t₀ + y₀ ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0

The contract fits `Phi`, `Ht`, `ZeroVerification` as they stand. It does NOT fit `Polymath15Bridge`
as it stands, for the reason in §3.2.

### 3.2 DEFECT (blocking for Instance02): the merged "canopy" hypothesis of `Polymath15Bridge` is not dischargeable by any finite certificate

The second hypothesis of `Polymath15Bridge` demands H_t(x + iy) ≠ 0 for ALL x ≥ X, y ∈ [y₀, 1] and
ALL t ∈ [0, t₀] — in particular at t = 0 for every x ≥ X. **Derivation D-3.2.** By P15 eq. (1) (p1),
H₀(z) = ⅛·ξ(½ + iz/2); with z = x + iy, ½ + iz/2 = (1 − y)/2 + ix/2. So H₀(x + iy) = 0 iff ξ(s) = 0 at
s = (1 − y)/2 + ix/2, i.e. iff ζ has a zero with Re s = (1 − y)/2 and Im s = x/2 — equivalently (by
ξ(s) = ξ(1 − s)) a zero with Re s = (1 + y)/2 at height x/2. Hence the t = 0 slice of the canopy
hypothesis for x ≥ X says: ζ has no zeros with (1 + y₀)/2 ≤ Re s ≤ 1 at ANY height ≥ X/2. For the
instance (X/2 ≈ 2.5·10¹²) that is the Riemann hypothesis in the strip Re s ≥ 0.583665 at all
heights above PT's 3 000 175 332 800 — unproved, and not the object of any finite computation
(at t = 0 the effective approximation does not stabilize: Theorem 1.5's solidification region
x ≥ exp(C/t) escapes to infinity as t → 0, P15 p9–11). ∎

The Prop is TRUE as a mathematical statement (its hypotheses are stronger than Theorem 1.2's, so
it is a weaker implication than the theorem), which is why it type-checked and why the design
note's §7 check ("the merged form elaborates as written") could not catch this: elaboration does
not test instantiability. The design note's own §1.3 point 1 intended (ii) "on the finite rectangle
plus one analytic tail row … at final time t₀"; the merge over "0 ≤ t ≤ t₀" over-strengthened it.
With the Prop as written, `lambda_le_point2` cannot be proved from any transcript plus H1 — the
instance theorem of design §1.3 is unprovable. The repair is one definition:

### 3.3 The amended bridge (type-checked, `lean-shapes-scratch.lean` §A; to replace `Polymath15Bridge` in `Defs.lean` v1.1 with a dated deviation record in the file header and in the design note §7)

    /-- (H3) Polymath15 Theorem 1.2 with hypothesis (ii) at the FINAL time only and the simplified
    barrier box for (iii) — the instantiable form (SPEC §3.2). -/
    def Polymath15Bridge' : Prop :=
      ∀ t₀ X y₀ : ℝ, 0 < t₀ → 0 < X → 0 < y₀ → y₀ ≤ 1 →
        ZeroVerification ((1 + y₀) / 2) (X / 2) →
        (∀ x y : ℝ, X + 1 ≤ x → y₀ ≤ y → y ^ 2 ≤ 1 - 2 * t₀ →
            Ht t₀ (x + y * I) ≠ 0) →                                            -- (ii′)
        (∀ x y : ℝ, X ≤ x → x ≤ X + 1 → y₀ ≤ y → y ≤ 1 → ∀ t : ℝ, 0 ≤ t → t ≤ t₀ →
            Ht t (x + y * I) ≠ 0) →                                             -- (iii′)
        ∀ t : ℝ, t₀ + y₀ ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0

**Derivation D-H3 (`Polymath15Bridge'` is implied by Theorem 1.2, hence is a legitimate displayed
form of it).** Fix parameters with 0 < t₀, 0 < X, 0 < y₀ ≤ 1 and assume (i), (ii′), (iii′). Theorem
1.2's (ii): take x ≥ X + √(1 − y₀²) and y₀ ≤ y ≤ √(1 − 2t₀) (so y² ≤ 1 − 2t₀). If x ≥ X + 1, (ii′)
gives H_{t₀}(x + iy) ≠ 0. Otherwise X ≤ X + √(1 − y₀²) ≤ x ≤ X + 1 (as 0 ≤ √(1 − y₀²) ≤ 1), and
y ≤ √(1 − 2t₀) ≤ 1, so (iii′) at t = t₀ gives it. Theorem 1.2's (iii): its region has X ≤ x ≤
X + √(1 − y₀²) ≤ X + 1, y ≥ √(y₀² + 2(t₀ − t)) ≥ y₀ and y ≤ √(1 − 2t) ≤ 1, 0 ≤ t ≤ t₀ — inside
(iii′)'s box. So Theorem 1.2 applies and gives the conclusion. ∎ (When 1 − 2t₀ < y₀², (ii′) is
vacuous; Theorem 1.2 still applies with its (ii) region empty, exactly as in the paper.)

The name: the amended Prop REPLACES the merged one (do not keep both — a Prop that cannot be
instantiated must not remain in the trusted layer under the name "Theorem 1.2"). Everywhere below,
"H3" means `Polymath15Bridge'` in conjunction with `HtEntire` (§3.5).

### 3.4 The normalizer B_t in the trusted layer (Defs.lean v1.1; type-checked, scratch §A)

The barrier rows enclose the NORMALIZED function g_t := H_t/B_t (P15 p4: "renormalise the function
H_t(x+iy) by dividing it by a nowhere vanishing explicit function B_t(x+iy)"; |H_t| itself is
e^{−(π/8 + o(1))x} ≈ 10^{−10¹²} at the instance's X and cannot be scaled into integers). The
contract fixes B_t CONCRETELY in the trusted layer rather than existentially ("∃ B nonvanishing
holomorphic with rows enclosing H_t/B") — so that a reader of the ~40 trusted lines sees which
function the rows are about — transcribed from P15 (6), (9), (10), (11) (p4):

    def alpha (s : ℂ) : ℂ := 1 / (2 * s) + 1 / (s - 1) + (1 / 2 : ℂ) * Complex.log (s / (2 * π))
    def M0 (s : ℂ) : ℂ :=
      (1 / 8 : ℂ) * (s * (s - 1) / 2) * (π : ℂ) ^ (-s / 2) * (Real.sqrt (2 * π) : ℂ)
        * Complex.exp ((s / 2 - 1 / 2) * Complex.log (s / 2) - s / 2)
    def Mt (t : ℝ) (s : ℂ) : ℂ := Complex.exp ((t : ℂ) / 4 * alpha s ^ 2) * M0 s
    def Bt (t : ℝ) (z : ℂ) : ℂ := Mt t ((1 - I * z) / 2)

Transcription notes (audit surface): Mathlib's `Complex.log` is the principal branch with argument
in (−π, π] — P15's "Log"; `(π : ℂ) ^ (-s / 2)` is `Complex.cpow` with a positive real base, i.e.
exp((−s/2)·log π) with real log π — P15's π^{−s/2}; (1 − iz)/2 = (1 + y − ix)/2 for z = x + iy.
Two facts about `Bt` are PROVED in `BarrierCert.lean` (Lean obligation L-B3, §8.3), not displayed:
for t ∈ ℝ and z with Im z ≠ 0 … more precisely on an open neighborhood of any rectangle with y₁ > 0
and x₁ > 1: `Bt t` is differentiable and nonvanishing (s = (1 − iz)/2 has Im s = −x/2 ≠ 0, so s ∉
(−∞, 1], both logs are off the cut, exp ≠ 0, cpow of a positive base ≠ 0, s ≠ 0, s − 1 ≠ 0). If
that proof turned out costly it may be displayed instead (fallback recorded in §13.2); the
statement shapes do not change.

### 3.5 The entirety of H_t (Defs.lean v1.1; type-checked)

    def HtEntire : Prop := ∀ t : ℝ, Differentiable ℂ (Ht t)

The argument principle needs g_t holomorphic on a neighborhood of R; `Ht` is a Bochner integral
whose holomorphy (differentiation under the integral against the super-exponentially decaying Φ) is
M2b-class analysis (design note §2 item 1). It is therefore DISPLAYED, as the second component of
the analytic package H3 := `Polymath15Bridge' ∧ HtEntire`. It is not folded into H2: H2 is where
producers enter; H3 is where Polymath15's analysis enters.

### 3.6 H1 for the instance — exact, no rounding (correcting design note §1.3 point 4)

Theorem 1.2(i) at row 2 needs `ZeroVerification ((1 + y₀)/2) (X/2)` with y₀ = 16733/100000 and
X = 5 000 000 194 858: (1 + y₀)/2 = 116733/200000 = 0.583665 exactly and X/2 = 2 500 000 097 429
exactly (X is even). The design note wrote σ₀ = 58367/100000 and called it a round-DOWN; but
58367/100000 = 0.58367 > 0.583665 — it is a round-UP, and `ZeroVerification` is monotone the wrong
way for that (a larger σ₀ is a WEAKER hypothesis, which does not imply the one the bridge consumes).
The instance therefore states H1 exactly:

    hH1 : ZeroVerification (116733 / 200000) 2500000097429

discharged in prose by PT Theorem 1 (p2: RH true up to height 3 000 175 332 800), with margin
3 000 175 332 800 − 2 500 000 097 429 = 500 175 235 371 (exact, `row2_arith.log`). PT's own pairing
sentence uses the rounded "H > 2.51·10¹²" (p5); 2.51·10¹² − X/2 = 9 999 902 571 > 0, consistent.

### 3.7 The honest label (final wording for M2a)

> kernel-checked modulo the displayed hypotheses: (H1) a producer-certified zero verification —
> `ZeroVerification (116733/200000) 2500000097429`, discharged by Platt–Trudgian Theorem 1; (H2)
> producer-certified enclosures — the barrier prisms (H2-B), the final-time window rows (H2-A) and the
> tail (H-TAIL), from two independent producers; (H3) the Polymath15 analytic package — Theorem 1.2
> in the form `Polymath15Bridge'` and the entirety of H_t — as hypotheses.

Never "fully machine-checked". The count is three named hypotheses with H2 a conjunction of three
enclosure-type Props; publications may say "three displayed hypotheses" only with that gloss.

---

## 4. Lane B — the barrier: mechanism and soundness

### 4.1 Overview

Fix R = [x₁, x₂] × [y₁, y₂] (instance: [X, X+1] × [y₀, 1]) and 0 = τ₀ < τ₁ < … < τ_{J−1} < τ_J := t₀.
Prism j is R × [τ_j, τ_{j+1}]. For each prism the transcript carries:

1. the **seam transcript** at time τ_j: a W1 exclusion transcript (FORMAT.md §§2–6, verbatim) for the
   producer's holomorphic approximant f = f_{τ_j} of g_{τ_j} = H_{τ_j}/B_{τ_j} — mesh of ∂R, per-segment
   value boxes at scale K, per-segment argument rows at scale A (turn units), claimed winding 0;
2. the **floor** (Fn, Fd): |f| ≥ Fn/Fd on ∂R (FORMAT.md §5.2 integer-squares scheme, check C11);
3. the **approximation defect** E ∈ ℕ: |g_{τ_j}(z) − f(z)| ≤ E/K for all z ∈ ∂R;
4. the **displacement** D ∈ ℕ: |g_t(z) − g_{τ_j}(z)| ≤ D/K for all z ∈ ∂R and τ_j ≤ t ≤ τ_{j+1}.

The checker verifies W1's C1, C3–C9 (with m = 0), C11, the general-rectangle C2′, and the one new
gate **C-B12: (E + D)·Fd < Fn·K** (i.e. E/K + D/K < Fn/Fd), plus the seam chain C-B13. Items 1–2 are
the M1 v1 checker with m = 0, exactly as the design note §1.3 point 1 prescribes; items 3–4 are the
two integers that carry Theorem 1.3 and the time step.

### 4.2 The seam rows: what f is, and what H-ENCL says about it

f is P15's f_t of eq. (14) at t = τ_j with N = N₀ constant on R (P15 p6: "f_t(x + iy) is a
holomorphic function of x + iy in the region (5) as long as N is constant"). For the instance,
N = 630783 on all of [X, X+1] × [0, t₀] (`row2_arith.log`: √(x/4π + t/16) ∈ [630783.1427963,
630783.1427965] at the four corners; the producer re-verifies with directed rounding, requirement
P-4). The rows assert, for every segment k (FORMAT.md §8.1(a),(b) with f in place of ζ):
reLo_k ≤ K·Re f ≤ reHi_k, imLo_k ≤ K·Im f ≤ imHi_k on the whole closed segment, and
argLo_k ≤ A·(Δ_k/2π) ≤ argHi_k for the log-derivative increment Δ_k of f. In Lean this is
`W1.RowEnclOK f p.K p.A` row-by-row against `W1.segs (toW1 r p)` — the M1 definitions, unchanged.
f is NOT defined in Lean (defining it would move (14)–(19) into the trusted layer); H2-B says
"there exists f, holomorphic on an open U ⊇ R, such that …" (§8.1), and the producers' f_t is the
intended witness. M2b, which defines f_t to prove Theorem 1.3, replaces the existential by it.

### 4.3 The winding: a W1 exclusion certificate for f

C8/C9 with m = 0 pin the winding number of f around ∂R to 0 (FORMAT.md D4); C6 gives f ≠ 0 on ∂R
(D1); the general-rectangle argument principle (`RectArgPrincipleGen`, §8.3 L-B0 — the proof of
`rectArgPrinciple_of_local` already discards the strip bounds, which appear as `_hhalf _hs2` in its
`intro`) then gives f ≠ 0 on R° and hence on R. The strip constraints of W1's C2 (½ < σ₁ ≤ σ₂ < 1)
are ζ-specific (they keep the pole out) and are REPLACED by C2′: x₁ < x₂, y₁ < y₂ (nondegenerate)
and y₁ > 0 (Theorem 1.2 needs y₀ > 0; B_t nonvanishing uses Im s ≠ 0).

### 4.4 The approximation defect E (Theorem 1.3 enters here, and only here)

E/K must bound e_A + e_B + e_{C,0} at t = τ_j uniformly on ∂R, from (71)–(72) + Proposition
6.6(iv)–(v) for e_A + e_B and the 10.50 form (D-2.4) for e_{C,0}; every factor bounded in its
conservative direction over the box (x ∈ [x₁, x₂], y ∈ [y₁, y₂]) — requirement P-6. The paper's own
budget for X₀ ≈ 6·10¹⁰ is 1.25·10⁻³ (Proposition 8.1, p39–42); the instance's indicative values
(`row2_errbudget_indicative.log`, heuristic floats, NOT a certificate): e_{C,0} ≤ 4.12·10⁻⁴ at
(X, y₀, t = 0) — the worst corner (smallest y, t = 0) — falling to 1.0·10⁻⁷ at t = t₀; e_A + e_B ≲
3·10⁻¹⁰. **The t = 0 endpoint.** Theorem 1.3 is stated on region (5), which has t > 0. The seam
τ₀ = 0 needs it at t = 0. Gomila's `BARRIER_CERTIFICATE.md` argues it by a limit t_j ↓ 0 (dominated
convergence for H_t, continuity of B_t, f_t and of the majorant on the compact box). This contract
does NOT rely on that argument in the checker; it is part of what H2-B asserts at the first seam,
and the producers must either (a) record the limit argument as their discharge of E at τ₀ = 0, or
(b) place the first seam at a small positive τ₀ > 0 and cover [0, τ₀] by … no: (b) is impossible,
the prism chain must start at 0 (C-B13) because Theorem 1.2(iii) starts at t = 0. Option (a) it is;
the SPEC records the limit argument as a producer obligation (P-7) and flags it for M2b (§13.3).

### 4.5 The displacement D (the time step)

D/K must bound sup{|g_t(z) − g_{τ_j}(z)| : z ∈ ∂R, τ_j ≤ t ≤ τ_{j+1}}. The producers obtain it as
D_t·(τ_{j+1} − τ_j) + (defect terms) from P15's (91) reasoning with Lemma 8.4's |∂f_t/∂t| majorant
(p46), UNIFORMIZED over the prism (pointwise Lemma 8.4 values at one corner are not box bounds —
Gomila's `DERIVATIVE_BOX_LEMMA.md` documents exactly this pitfall and its repair; requirement P-8),
and with the two defects E(τ_j) and E(t) added when the displacement is routed through f: |g_t −
g_{τ_j}| ≤ |g_t − f_t| + |f_t − f_{τ_j}| + |f_{τ_j} − g_{τ_j}| ≤ E_t + D_t·Δt + E_{τ_j}. (A producer
may instead bound |∂_t g_t| directly if it has an evaluator for it; the contract does not care how
D was obtained — only that the displayed clause holds.) **Why a displacement, not a Lipschitz
constant:** a row "sup |∂_t g_t| ≤ L" would make the trusted statement assert t-differentiability of
H_t/B_t (differentiation of the Bochner integral in t — M2b-class); the displacement clause is a
plain inequality between values of `Ht`, checkable by the producers' own arithmetic and stated with
no derivative. The design note's "slice-spacing × that bound < floor" is the same check with the
multiplication moved to the producer (recorded deviation, §4.7(i)).

### 4.6 Soundness of Lane B (the derivation the Lean theorem `cert_of_checkBarrier` formalizes)

Notation: G : ℝ → ℂ → ℂ the normalized family (instance: G t z = Ht t z / Bt t z), g_t := G t; U
an open set containing R on which the seam's f is holomorphic (H2-B); U_t an open set containing R
on which g_t is holomorphic (`hHol`, from H3's `HtEntire` + L-B3 for the instance). Fix prism
[τ, τ′] and t ∈ [τ, τ′].

* **D-B1 (seam exclusion for f).** C-B0..C-B9 (m = 0) with the row enclosures give: f ≠ 0 on ∂R
  (FORMAT D1); the four-edge increment sum of f is 2π·Z_f with Z_f ∈ ℕ (argument principle for f on
  U) and A·Z_f ∈ [S_lo, S_hi] ∋ A·0 with width < A/2 (FORMAT D4), so Z_f = 0; the Z = 0 clause of the
  argument principle gives f ≠ 0 on R°. Hence f ≠ 0 on R.
* **D-B2 (floor).** C-B11 + rows ⟹ |f| ≥ Fn/Fd on ∂R (FORMAT D6; Lean `floor_of_checkW1Floor`,
  already generic in f).
* **D-B3 (boundary perturbation).** For z ∈ ∂R: |g_t(z) − f(z)| ≤ |g_t(z) − g_τ(z)| + |g_τ(z) − f(z)|
  ≤ (D + E)/K < Fn/Fd ≤ |f(z)| by the two H2-B clauses and C-B12 ((E + D)·Fd < Fn·K, cross-
  multiplied with K, Fd ≥ 1). So g_t(z) ≠ 0, and h(z) := g_t(z)/f(z) satisfies |h(z) − 1| < 1,
  hence Re h(z) > 0 — h(∂R) lies in the open right half-plane.
* **D-B4 (holomorphy of h near R).** V := U ∩ U_t ∩ {z ∈ U : f z ≠ 0} is open (f continuous on U),
  contains R (D-B1), and h = g_t/f is holomorphic on V.
* **D-B5 (log-derivative additivity).** On each mesh segment γ ⊂ ∂R, f and h are holomorphic and
  nonvanishing near γ and g_t = h·f, so g_t′/g_t = h′/h + f′/f there, and (linearity of the interval
  integral, integrability from continuity on the compact segment) argIncrement(g_t, γ) =
  argIncrement(h, γ) + argIncrement(f, γ).
* **D-B6 (the half-plane lemma — the one new analytic lemma).** If h is holomorphic near the segment
  γ : [0,1] → ℂ from z to w and Re h > 0 on γ, then ∫₀¹ (h′/h)(γ(s))·γ′(s) ds = Log h(w) − Log h(z)
  for the principal Log: Log ∘ h ∘ γ is differentiable on [0,1] with derivative (h′/h)(γ)·γ′ (chain
  rule; `Complex.log` has derivative 1/w on the slit plane, and the right half-plane lies in it), so
  the fundamental theorem of calculus for the interval integral of a derivative applies. Taking
  imaginary parts: argIncrement(h, γ) = Arg h(w) − Arg h(z), Arg = `Complex.arg`.
* **D-B7 (telescoping).** Summing D-B6 over the segments of the closed counterclockwise traversal
  (FORMAT §4: each segment's end is the next segment's start, and the last segment ends at the first
  segment's start): Σ_γ argIncrement(h, γ) = 0 exactly.
* **D-B8 (conclusion).** Apply the argument principle to g_t on V (D-B3: g_t ≠ 0 on ∂R; D-B4):
  ∃ Z ∈ ℕ, 2πZ = Σ_edges argIncrement(g_t) = Σ_γ argIncrement(g_t, γ) (W1 L1 sub-segment
  additivity) = Σ_γ argIncrement(h, γ) + Σ_γ argIncrement(f, γ) (D-B5) = 0 + 2π·Z_f = 0 (D-B7,
  D-B1). So Z = 0 and g_t ≠ 0 on R°; with D-B3, g_t ≠ 0 on R. ∎
* **D-B9 (coverage in t).** C-B13 (0 = τ₀ < … < τ_{J−1} < t₀) with W1's `cover_chain` lemma: every
  t ∈ [0, t₀] lies in some [τ_j, τ_{j+1}].

For the instance, G t z = Ht t z / Bt t z, and `Bt t z ≠ 0` on R (L-B3) turns g_t ≠ 0 into Ht t z ≠ 0.
No Rouché theorem, no homotopy invariance and no zero-continuity in t is used: D-B6/D-B7 reduce the
time step to the same fixed-t argument principle W1 already has, applied twice (to f and to g_t),
plus one FTC-on-a-segment lemma.

### 4.7 Deviations from the design note, and the road not taken

1. **Displacement row D instead of a Lipschitz row.** Reason in §4.5. The checker's gate is the
   design note's inequality with the product formed producer-side.
2. **The rows enclose f, with Theorem 1.3's defect as a separate integer E.** Reason: the argument
   principle needs a holomorphic function whose winding the rows pin, and the two trusts — the
   producers' arithmetic (rows) and Polymath15's Theorem 1.3 (E) — are kept visibly apart.
3. **The road not taken — rows uniform in t (prism-uniform boxes and argument rows, no D).** It
   would remove the time step from the soundness theorem entirely (argument principle at every
   fixed t against t-uniform rows). It fails quantitatively: C8 needs the SUM of the argument-row
   widths below ½ turn; a t-uniform endpoint box has half-width ≈ D_t·Δt, which on Gomila's first
   prism is 1.89 against a modulus of 4.28 (`barrier_target_closed.log`, prism 1: time = 1.8885,
   min_mesh = 4.2784) — ≈ ±0.07 turn of argument uncertainty per segment; with ≈ 3.8·10⁴ segments
   per seam the sum width would be ≈ 5·10³ turns. Shrinking Δt by 10⁴ restores C8 at the price of
   ≈ 10⁷ prisms × 10⁴ rows = 10¹¹ rows. The seam-plus-displacement design keeps the argument rows
   sharp (endpoint enclosures at the exact seam) and pays one integer per prism for the time step —
   P15's (91) with the mesh term absorbed into the whole-segment hull boxes.
4. **B_t concrete** (§3.4) rather than "∃ B". 5. **`HtEntire` in H3**, not H2 (§3.5).
6. **General-rectangle C2′** replaces W1's strip C2 (§4.3); W1's own files are not modified.

---

## 5. Lane A — the asymptotic region at the final time: decision, rows, coverage, the tail

### 5.1 DECISION (task item (c)): a second CHECKED lane, with the analytic tail reduction displayed

Lane A is a checked lane — window rows of a finite computation plus a tail row — NOT a bare
displayed hypothesis "(ii) holds". Reasons, in order of weight:

1. **The paper's record for Table-1 row 2's hypothesis (ii) is an expectation, not a per-window
   run** (§2.8: "expect to be able to verify … for any choice of parameters … as above", p66).
   PT's Corollary 2 rests on that row. The finite computation therefore has to be DONE for the
   instance in any case; a bare hypothesis would hide that fact rather than record it.
2. The EnclOK discipline: a computation the program performs enters the trusted statement as
   integer data plus a displayed enclosure claim, never as prose. The kernel's work per row is
   small (E < T), but the coverage facts — consecutive windows from N_start, the tail row anchored
   at N_end + 1, the y-range reaching √(1 − 2t₀) — are integer facts worth checking, and the rows
   are what the two-producer cross-check compares.
3. Gomila's finite lane (3 149 013 per-N rows with a stored floor and a global error bound) converts
   into this row format directly (§11), so M2a′ inherits the lane.

What is and is not kernel-checked in Lane A, stated plainly: the kernel checks the integer
inequalities C-A1..C-A6 (row floors exceed error ceilings; windows consecutive; the tail row's sum
below 2K; yA² ≥ 1 − 2t₀). The kernel does NOT check that the row floors are true floors of |f_{t₀}|
(H2-A, producer-certified via a mollified triangle inequality), nor that the tail row's five numbers
bound the five quantities of Lemma T, nor Lemma T's reduction "if that sum < 2 then nonvanishing for
all N ≥ N₁" (H-TAIL, displayed; Lemma T is DERIVED in §5.4 — it is checkable mathematics, but not
Lean mathematics until f_t is defined in Lean, i.e. M2b). The Lean hypothesis `TailOK` is stated in
CONCLUSION form (§8.1); the tail row and its kernel-checked inequality are the recorded computational
component of its prose discharge, and the theorem does not consume the row. That is the honest
shape: the row is evidence, the reduction is displayed.

### 5.2 Window rows

A row (N₋, N₊, T, E), with N₋ ≤ N₊ integers and T, E ∈ ℕ at the lane's scale K, asserts (H2-A):

    for all real x with N(x) := ⌊√(x/(4π) + t₀/16)⌋ ∈ [N₋, N₊] and all y ∈ [y₀, yA]:
        |f_{t₀}(x + iy)| ≥ T/K   and   e_A + e_B + e_{C,0} ≤ E/K   at (x, y, t₀),
    hence (Corollary 1.4)  |g_{t₀}(x + iy)| ≥ (T − E)/K.

In Lean only the consequence is stated (`AsymEnclOK`, §8.1: (T − E)/K ≤ ‖g_{t₀}(x + iy)‖ on the
window), since f_{t₀} is not a Lean object; the producers record T and E separately for the
cross-check. Note the window is defined through N(x) with π and a square root — the Lean hypothesis
uses `windowIdx t x := ⌊Real.sqrt (x / (4π) + t/16)⌋₊` (P15 (19)); no transcript field is
irrational. **How a producer obtains T** (informative; P-9): a mollified triangle-inequality floor
uniform in N ∈ [N₋, N₊] and y ∈ [y₀, yA] — P15's Lemma 10.1 (p65, Euler-2 mollifier: the Table-1
column "|f_t(x+iy)| lower bound" is this at N = N₀) or the E_{t,5}-mollified naive bound (98) (p54)
with σ ≥ σ_{N₋} and |γ|n^y bounded as on p53 (the y = 0.2 constants there must be re-derived at
y₀ = 0.16733), or Gomila's "Native Triangle lemma" (`NATIVE_BINDING.md`: L_N > 0 ⟹ |f_t| ≥ L_N on
the window). A pointwise evaluation cannot give a window floor (f_{t₀} oscillates on a window of
x-length 4π(2N + 1) ≈ 1.6·10⁷ at N₀). **How a producer obtains E** (P-6): the 10.50 form of D-2.4
and 6.6(iv)–(v), each factor at its worst corner of the window × y-range (all factors are monotone
in x for x ≥ 200: (x/4π)^{−(1+y)/4}, exp(−(t/16)log²(x/4π)), exp(c/(x − 12)) all decrease; the
N-factor decreases in N; 3^y + 3^{−y} increases in y ≥ 0 — worst at yA; (x/4π)^{−(1+y)/4} worst at
y₀). Indicative magnitude at row 2 (`row2_errbudget_indicative.log`): e_{C,0}(x_{N₀}, y₀, t₀) ≈
1.03·10⁻⁷, e_A + e_B ≈ 10⁻¹², against P15's floor 0.0376 at N₀ — margin ≈ 3.6·10⁵.

### 5.3 Coverage

Rows are consecutive (C-A4: next N₋ = previous N₊ + 1) from N_start := first N₋ to N_end := last
N₊, and the tail row has N₁ = N_end + 1 (C-A5). The Lean instance proves (obligation L-A1) that
N(x) ≥ N_start for every x ≥ X + 1 — for the instance N_start = N₀ = 630783 and the fact needed is
(X + 1)/(4π) + t₀/16 ≥ 630783², i.e. X + 1 ≥ 4π·630783² − πt₀/4, which holds with margin ≈ 2.26·10⁶
(`row2_arith.log`: x_{N₀} ∈ [4999997931063.31, 4999997931063.47] against X = 5000000194858); a
rational upper bound π < 3.141593 (`Real.pi_lt_d6`) suffices (4·630783²·10⁻⁶ ≈ 1.6·10⁶ < 2.26·10⁶,
tight — a producer may choose N_start = N₀ − 1 to leave slack, at the cost of one more window).
`windowIdx` is monotone in x (L-A2: floor and sqrt are monotone), so every x ≥ X + 1 has N(x) in some
row or N(x) ≥ N₁. The y-range: yA rational with yA² ≥ 1 − 2t₀ (C-A1, cross-multiplied); the bridge's
(ii′) quantifies y with y² ≤ 1 − 2t₀, so y ≤ yA (both ≥ 0). Instance: 1 − 2t₀ = 157/250,
yA = 3962323/5000000 = 0.7924646 works (bracket in `row2_arith.log`; yA² − 157/250 > 0 by integer
squares).

### 5.4 Lemma T — the tail, derived (this is the analytic content of H-TAIL, parametrized; nothing here is quoted from P15 except the cited inequalities)

**Setting.** t := t₀ ∈ (0, ½]; 0 < y₀ ≤ yA ≤ 1; an integer N₁ ≥ 5; y ∈ [y₀, yA]; x real with
N := N(x) ≥ N₁ — hence x ≥ x_N := 4π(N² − t/16) ≥ x_{N₁} ≥ 200 (P15 (80), p38: x_N ≤ x < x_{N+1}),
and (x, y, t) is in region (5). Put b_n := exp((t/4)log² n), σ := Re s*(x + iy), and
N′ := √(N² − t/16), N₁′ := √(N₁² − t/16), u := log N, u₁ := log N₁.

**Step 1 (triangle inequality).** From (14): |f_t(x + iy)| ≥ 1 − Σ_{n=2}^{N} b_n n^{−σ} −
|γ| Σ_{n=1}^{N} n^{y} b_n n^{−σ + |κ|}, since |n^{−s*}| = n^{−σ} and |n^{−s*−κ}| = n^{−σ − Re κ} ≤
n^{−σ + |κ|}. Writing A(N, σ) := Σ_{n=1}^{N} b_n n^{−σ} (its n = 1 term is 1) and
B := |γ| Σ_{n=1}^{N} n^{y} b_n n^{−σ+|κ|}:  |f_t| ≥ 2 − A(N, σ) − B.

**Step 2 (the window bounds, from (20)–(22)).** (a) Since x ≥ x_N: log(x/4π) ≥ log(N² − t/16) =
2u + log(1 − t/(16N²)). (b) For y ∈ [0, 1] and x ≥ 200: 1 − 3y + 4y(1 + y)/x² ≤ 1 (as
4y(1 + y)/x² ≤ 3y ⟸ x² ≥ 4(1 + y)/3), so the positive part is ≤ 1 and (21) gives
σ ≥ σ_N(y) := (1 + y)/2 + (t/2)u − ε_N,  ε_N := −(t/4)log(1 − t/(16N²)) + t/(2x_N²) > 0,
with ε_N decreasing in N and σ_N(y) increasing in both N and y. (c) From (20) and x/4π ≥ N′²:
|γ| n^{y} ≤ e^{0.02y}(n/N′)^{y} = e^{0.02y}(n/N)^{y}(N/N′)^{y} ≤ e^{0.02}·(n/N)^{y₀}·ρ₁ for
1 ≤ n ≤ N, where (n/N)^{y} ≤ (n/N)^{y₀} because n/N ≤ 1 and y ≥ y₀, and (N/N′)^{y} ≤ N/N′ ≤
ρ₁ := (1 − t/(16N₁²))^{−1/2} because N/N′ ≥ 1, y ≤ 1, N ≥ N₁. Put c_γ := e^{0.02}ρ₁. (d) From (22):
|κ| ≤ t y/(2(x − 6)) ≤ t·yA/(2(x_{N₁} − 6)) =: k₁.

**Step 3 (the A-sum, all N ≥ N₁).** A(N, σ) ≤ A(N, σ_N(y)) ≤ A(N, σ_N) with σ_N := σ_N(y₀) (each
summand decreases in σ; σ_N(y) ≥ σ_N(y₀)). Lemma 8.2 (p42) with N₀ := N₁ applies since N ≥ N₁ and
σ_N − (t/2)u = (1 + y₀)/2 − ε_N > 0 (side condition **(S1)**: ε_{N₁} < (1 + y₀)/2; ε_N ≤ ε_{N₁}):
A(N, σ_N) ≤ Σ_{n≤N₁} b_n n^{−σ_N} + max(N₁^{1−σ_N} b_{N₁}, N^{1−σ_N} b_N)·log(N/N₁). The head:
σ_N ≥ σ_{N₁} gives Σ_{n≤N₁} b_n n^{−σ_N} ≤ Σ_{n≤N₁} b_n n^{−σ_{N₁}} =: **Q₁** (finite; σ_{N₁} =
σ_{N₁}(y₀)). The max term, with a := (1 − y₀)/2 + ε_{N₁} and ψ(v) := a·v − (t/4)v²:
  N^{1−σ_N} b_N = exp((1 − σ_N)u + (t/4)u²) ≤ exp((1 − (1+y₀)/2 + ε_N)u − (t/2)u² + (t/4)u²) ≤ exp(ψ(u));
  N₁^{1−σ_N} b_{N₁} = exp((1 − σ_N)u₁ + (t/4)u₁²) ≤ exp(a·u₁ + (t/4)u₁² − (t/2)u·u₁) = exp(ψ(u₁))·exp(−(t/2)u₁(u − u₁)).
Under **(S2)**: u₁ ≥ 2a/t, ψ is decreasing on [u₁, ∞) (concave quadratic with vertex 2a/t), so
exp(ψ(u))·(u − u₁) = exp(ψ(u₁))·exp(ψ(u₁ + v) − ψ(u₁))·v with v := u − u₁ ≥ 0, and ψ(u₁ + v) − ψ(u₁)
= (a − (t/2)u₁)v − (t/4)v² ≤ −(t/4)v², whence exp(ψ(u))·(u − u₁) ≤ exp(ψ(u₁))·sup_{v≥0} v e^{−(t/4)v²}
= exp(ψ(u₁))·√(2/t)·e^{−1/2} (the supremum is at v = √(2/t)); and exp(ψ(u₁))·e^{−c v}·v with
c := (t/2)u₁ is ≤ exp(ψ(u₁))/(e·c). Therefore max(…)·log(N/N₁) ≤ exp(ψ(u₁))·κ_T,
κ_T := max(√(2/(e·t)), 2/(e·t·u₁)), for every N ≥ N₁. Put **Q₃** := exp(ψ(u₁))·κ_T. So
A(N, σ) ≤ Q₁ + Q₃ for all N ≥ N₁.

**Step 4 (the B-sum).** By Step 2(c),(d): B ≤ c_γ N^{−y₀} Σ_{n≤N} b_n n^{y₀ − σ + k₁} ≤
c_γ N₁^{−y₀} Σ_{n≤N} b_n n^{−σ″_N}, σ″_N := σ_N − y₀ − k₁ = (1 − y₀)/2 + (t/2)u − ε_N − k₁
(N^{−y₀} ≤ N₁^{−y₀}). Lemma 8.2 applies to the exponent σ″_N under **(S3)**: (1 − y₀)/2 > ε_{N₁} + k₁
(so σ″_N > (t/2)u); with a″ := (1 + y₀)/2 + ε_{N₁} + k₁ (since 1 − σ″_N ≤ a″ − (t/2)u) and
ψ″(v) := a″v − (t/4)v², the same computation under **(S4)**: u₁ ≥ 2a″/t gives
Σ_{n≤N} b_n n^{−σ″_N} ≤ Σ_{n≤N₁} b_n n^{−σ″_{N₁}} + exp(ψ″(u₁))·κ_T. Put **Q₂** := c_γ N₁^{−y₀}
Σ_{n≤N₁} b_n n^{−σ″_{N₁}} and **Q₄** := c_γ N₁^{−y₀} exp(ψ″(u₁))·κ_T. So B ≤ Q₂ + Q₄.

**Step 5 (the defect).** Let **E₁** ≥ sup{e_A + e_B + e_{C,0} at (x, y, t₀) : x ≥ x_{N₁},
y ∈ [y₀, yA]} — obtained from the 10.50 form and 6.6(iv)–(v) with every factor at its worst corner
(as in §5.2; the P15 chain (82)–(87), p39–42, is the template for e_A + e_B, with its "x ≥ X₀ − 0.5"
replaced by x ≥ x_{N₁} and its 0.5999 by the instance's σ lower bound).

**Conclusion (Lemma T).** Under (S1)–(S4), for every x with N(x) ≥ N₁ and every y ∈ [y₀, yA]:
|g_{t₀}(x + iy)| ≥ |f_{t₀}(x + iy)| − (e_A + e_B + e_{C,0}) ≥ 2 − Q₁ − Q₂ − Q₃ − Q₄ − E₁.
Hence **if Q₁ + Q₂ + Q₃ + Q₄ + E₁ < 2 then H_{t₀}(x + iy) ≠ 0 on the whole tail region.** ∎

**The tail row** carries integer upper bounds Q₁, Q₂, Q₃, Q₄, E₁ (at scale K) of the five quantities
and N₁; the checker verifies Q₁ + Q₂ + Q₃ + Q₄ + E₁ < 2K (C-A6) and N₁ = N_end + 1 (C-A5). The
producers verify (S1)–(S4) as directed-rounded inequalities and record them, with σ_{N₁}, σ″_{N₁},
ε_{N₁}, k₁, ρ₁, a, a″, κ_T, in the transcript's `producer` block; the enclosure of Q₁…Q₄, E₁ and the
side conditions are the producer-side part of H-TAIL's discharge, Lemma T is its analytic part.
**Indicative instance values** (`row2_tail_indicative.log`, float64, NOT a certificate): with the
crude Step-1 inequality the sums at y = y₀ give 2 − A − B ≈ −0.31 at N = 1.5·10⁶ (P15's N₁ for
their (t, y₀) = (0.2, 0.2)), ≈ −0.09 at 3·10⁶ and ≈ +0.076 at 6·10⁶; the side conditions are
comfortable (2a/t ≈ 4.5 and 2a″/t ≈ 6.3 against u₁ = log(6·10⁶) ≈ 15.6). So the crude tail at row 2
needs N₁ ≈ 6–8·10⁶ — four to five times P15's 1.5·10⁶, because y₀ = 0.16733 < 0.2 and t₀ = 0.186 <
0.2 both weaken the decay; the producer fixes N₁ rigorously (a mollified tail in the style of
Gomila's `TAIL_LEMMA.md` would lower N₁ but is a different lemma and is out of this contract's
scope). The finite lane then spans N ∈ [630783, N₁ − 1]; the number of rows is the producer's choice
(P15 covered 1.4·10⁶ windows with four intervals, p56; Gomila used singletons).

### 5.5 Finding recorded: the evidential status of hypothesis (ii) at Table-1 row 2

P15 established (ii) for the Λ ≤ 0.22 result by a full run (§8.5 with the four intervals of p56).
For the Table-1 rows, including row 2, the text records the barrier runs and, for (ii), the N₀
lower bound together with "expect to be able to verify" (p66). Lane A is the computation that
turns that expectation into a checked record for row 2; until it is run, the program's own
description of PT's Corollary 2 should say "Polymath15 Table 1 row 2 (barrier verified numerically;
asymptotic hypothesis argued from the N₀ lower bound and the §8.3/§8.5 method)". This is not a
doubt about the bound — the method is explicit and the margins are large (§5.2) — it is the honest
description of what is on the record.

### 5.6 Soundness of Lane A

Trivial by design: for x ≥ X + 1 and y ∈ [y₀, yA], either N(x) ∈ [N₋, N₊] for some row (then
`AsymEnclOK` gives ‖g_{t₀}(x + iy)‖ ≥ (T − E)/K > 0 by C-A3 and K ≥ 1) or N(x) ≥ N₁ (then `TailOK`);
`Bt t₀ ≠ 0` (L-B3) turns g ≠ 0 into `Ht t₀ (x + iy) ≠ 0`. Formalized as `cert_of_checkAsym` (§8.3).

---

## 6. What is displayed and what the kernel checks

| item | statement | discharge | kernel-checked? |
|---|---|---|---|
| **H1** | `ZeroVerification (116733/200000) 2500000097429` | PT Theorem 1 (prose; §3.6) | no |
| **H2-B** | `BarrierEnclOK G row2.barrier`: per prism ∃ holomorphic f on U ⊇ R with the seam rows enclosing f (`W1.RowEnclOK`), \|g_τ − f\| ≤ E/K on ∂R, \|g_t − g_τ\| ≤ D/K on ∂R for t in the prism | the two producers (rows, E, D) — Theorem 1.3 with the 10.50 weld for E, Lemma 8.4 uniformized for D | no (the rows' integer relations are; the enclosure claims are not) |
| **H2-A** | `AsymEnclOK (G t₀) row2.asym`: each window row's floor (T − E)/K ≤ ‖g_{t₀}‖ | the two producers (mollified triangle floor T, Theorem 1.3 defect E) | no (E < T and coverage are) |
| **H-TAIL** | `TailOK (G t₀) row2.asym`: g_{t₀} ≠ 0 for N(x) ≥ N₁, y ∈ [y₀, yA] | Lemma T (§5.4, derived here) + the producers' Q₁…Q₄, E₁ and (S1)–(S4) | the row inequality is; the enclosure and the reduction are not |
| **H3** | `Polymath15Bridge' ∧ HtEntire` | P15 Theorem 1.2 via D-H3; H_t entire (M2b) | no |
| checker facts | `checkBarrierChain`, `checkPrism` for every prism, `checkAsym` | `decide +kernel` on the literals | **yes** |
| soundness | `cert_of_checkBarrier`, `cert_of_checkAsym`, L-B3 (B_t ≠ 0, holomorphic near R), L-A1/L-A2, the glue arithmetic | Lean proofs (§8.3) | **yes** (theorems) |

Lean-proved obligations, named (all in `BarrierCert.lean` / `Instance02.lean`, none displayed):
**L-B0** `RectArgPrincipleGen` (the strip-free restatement of `RectArgPrinciple`, same proof) and the
W1 lemma refactor (`ChecksOK` minus its C2 strip clauses; `bdry_cover`, `boundary_nonvanishing`
restated for it); **L-B1** the half-plane lemma D-B6; **L-B2** log-derivative additivity D-B5;
**L-B3** `Bt` differentiable and nonvanishing on an open neighborhood of the instance rectangle;
**L-B4** t-coverage D-B9 from `cover_chain`; **L-A1** N(X + 1) ≥ N_start from a rational bound on
π; **L-A2** monotonicity of `windowIdx` in x; **L-G** the exact-rational glue (already type-checked:
t₀ + y₀²/2 ≤ 1/5, (1 + y₀)/2 = 116733/200000, X/2 = 2500000097429, X/2 ≤ 3000175332800).

---

## 7. The transcript format (`barrier-schema.json`) and the checker, normatively

### 7.1 Documents and fields — barrier lane

Three document kinds share `format: "M2a-barrier-transcript"`, `version: "1.0"`, and a `kind`.

**`manifest`** (one per barrier certificate):

| field | type | meaning |
|---|---|---|
| `lane` | const `"barrier"` | |
| `trust_label` | fixed string (§3.7, short form in the schema) | the honest label, verbatim |
| `rect` | `{x1, x2, y1, y2}`, rationals | R = [x₁, x₂] × [y₁, y₂] in the z = x + iy plane |
| `t0` | rational | the final time; the last prism is [last seam, t₀] |
| `prisms` | array of `{index, file, seam}` | the prism files in time order; each file's own `seam` must equal the entry's (consistency check of the reference checker; the Lean data has one copy) |
| `producer`, `comment` | optional | untrusted |

**`prism`** (one file per prism; the bulk data):

| field | type | meaning |
|---|---|---|
| `index` | nat string | position in the manifest |
| `seam` | rational τ_j ≥ 0 | the seam time (left endpoint of the prism) |
| `scales` | `{K, A}` | this prism's value scale (rows, floor, E, D) and argument scale (turn units; A even, ≥ 2 — producer requirement, FORMAT.md §1) |
| `mesh` | `{bottom, right, top, left}` | the boundary mesh of R, FORMAT.md §4 conventions verbatim |
| `segments` | array of rows `{reLo, reHi, imLo, imHi, argLo, argHi}` | FORMAT.md §§5–6 rows for the seam approximant f, global traversal order |
| `modulus_floor` | `{Fn, Fd}` | \|f\| ≥ Fn/Fd on ∂R |
| `approx_defect` | nat string E | \|g_{τ_j} − f\| ≤ E/K on ∂R |
| `displacement` | nat string D | \|g_t − g_{τ_j}\| ≤ D/K on ∂R for τ_j ≤ t ≤ τ_{j+1} |
| `producer` | optional object | untrusted per-prism diagnostics for the cross-check: the f boxes and argument rows BEFORE any inflation, the E derivation's inputs (N, the corner values of each factor), D_t and Δt, mesh policy, timings |

### 7.2 Documents and fields — asymptotic lane (`asymptotic`, one file)

| field | type | meaning |
|---|---|---|
| `lane` | const `"asymptotic"`; `trust_label` as above | |
| `scales` | `{K}` | the lane's value scale |
| `t0`, `y0`, `yA` | rationals | t₀ > 0; the y-range [y₀, yA]; C-A1: yA² ≥ 1 − 2t₀ |
| `rows` | array of `{Nlo, Nhi, T, E}` | window rows in increasing N, consecutive (§5.2–5.3) |
| `tail` | `{N1, Q1, Q2, Q3, Q4, E1}` | the Lemma-T row (§5.4) |
| `producer` | optional | untrusted: per-row mollifier data and σ bounds; the tail's constants and the side conditions (S1)–(S4) |

### 7.3 The barrier checker, normatively (per prism unless stated; all comparisons on integers)

* **C-B0** scales and denominators: K ≥ 1, A ≥ 1, every rational's d ≥ 1 (rectangle, t₀, seam,
  mesh), Fd ≥ 1, Fn ≥ 0, E ≥ 0, D ≥ 0, seam numerator ≥ 0.
* **C-B2′** rectangle (global): x₁ < x₂ and y₁ < y₂ by cross-multiplication; y₁ > 0; t₀ > 0.
* **C-B3** mesh walk on R: `bottom[0] = x₁`, `bottom[last] = x₂`, strictly increasing; `right`
  y₁ → y₂ increasing; `top` x₂ → x₁ decreasing; `left` y₂ → y₁ decreasing (FORMAT.md §4 = W1 C3).
* **C-B4** \|segments\| = Σ_edges(breakpoints − 1) (W1 C4).
* **C-B5** reLo ≤ reHi ∧ imLo ≤ imHi per row (W1 C5).
* **C-B6** reLo > 0 ∨ reHi < 0 ∨ imLo > 0 ∨ imHi < 0 per row (W1 C6 — the 0-exclusion scheme).
* **C-B7** argLo ≤ argHi ∧ −A ≤ 2·argLo ∧ 2·argHi ≤ A per row (W1 C7).
* **C-B8** 2·(S_hi − S_lo) < A, S_lo = Σ argLo, S_hi = Σ argHi (W1 C8).
* **C-B9** S_lo ≤ 0 ≤ S_hi (W1 C9 with m = 0).
* **C-B11** (mre² + mim²)·Fd² ≥ Fn²·K² per row, mre/mim as in FORMAT.md §5.2 (W1 C11).
* **C-B12** (E + D)·Fd < Fn·K — the prism gate.
* **C-B13** (global) the seam chain: first seam = 0; seams strictly increasing; last seam < t₀.

There is no C-B10 (no mode field; m = 0 is built in). C-B0..C-B9 and C-B11 are the M1 v1 checks with
C2 replaced; their Lean text is W1's helper functions (`densPos`, `edgeOK`, `rowsOK`, `sumArgLo/Hi`,
`floorRowsOK`) called on `toW1 rect prism` (§8.2) — no change to `W1/Checker.lean`.

### 7.4 The asymptotic checker, normatively

* **C-A1** K ≥ 1, denominators ≥ 1, t₀ > 0, y₀ > 0, yA ≥ 0, and yA² ≥ 1 − 2t₀, i.e.
  (t0d − 2·t0n)·yAd² ≤ yAn²·t0d.
* **C-A2** at least one row.
* **C-A3** per row: Nlo ≤ Nhi and 0 ≤ E < T.
* **C-A4** consecutive rows: next.Nlo = Nhi + 1.
* **C-A5** tail.N1 = last row's Nhi + 1.
* **C-A6** Q₁ + Q₂ + Q₃ + Q₄ + E₁ < 2·K, all five ≥ 0.

### 7.5 Number encoding

Exactly FORMAT.md §1: integers as decimal strings (`^-?(0|[1-9][0-9]*)$`), rationals as `{n, d}`
with d syntactically positive and re-verified ≥ 1 by the checker, no floats, no division, no
transcendental constants in checked data; argument rows in turn units. Scales are per prism / per
lane. The instance's X ≈ 5·10¹² makes mesh numerators ≈ 10¹²·10^k; production K is 10¹²–10³⁰-class.

### 7.6 Bulk-data packaging — the D-1 decision (settled here, before `BarrierCert.lean`)

**Scale to package.** Row 2's barrier will have ≈ 10³ prisms (indicative: D_t ≈ 5·10⁴ against
floors of order 1–4 forces Δt ≲ 10⁻⁴; P15 stepped adaptively, Gomila used 883 prisms at X ≈ 6·10¹²)
with ≈ 10⁴ segments per seam early on (P15: 11076 mesh points per rectangle at t = 0 for X ≈ 6·10¹⁰,
p49; Gomila: 38396 at t = 0), decreasing with t — in all ≈ 10⁶–10⁷ rows of six integers. Lane A is
≈ 10³–10⁴ rows unless a producer emits per-N singletons (Gomila: 3.1·10⁶).

**Decision.**
1. **JSON:** one file per prism (`prism` kind) plus a manifest; files may be gzip-compressed; the
   manifest is the unit the checkers and the cross-check consume. Lane A is one file.
2. **Lean:** one MODULE per prism, `Zeta23/DBN/Instance02/Prism_NNNN.lean`, containing (a)
   `set_option maxRecDepth 100000`, (b) the prism's rows as list literals of at most 1 000 rows
   each (`def prism_NNNN_rows_k : List W1.W1Row`), (c) `def prism_NNNN : PrismData` with
   `rows := prism_NNNN_rows_0 ++ … ++ prism_NNNN_rows_m`, and (d) the kernel fact
   `theorem prism_NNNN_check : checkPrism row2Rect prism_NNNN = true := by decide +kernel`. The
   rectangle `row2Rect : RectData` lives in its own small module so that prism modules do not
   import the prism list (this is why `checkPrism` takes a `RectData`, §8.2). The top module
   `Instance02.lean` imports the prism modules, defines `row2Barrier` with
   `prisms := [prism_0000, …]`, proves `checkBarrierChain row2Barrier = true` by `decide +kernel`
   (cheap: J rationals) and `∀ p ∈ row2Barrier.prisms, checkPrism row2Rect p = true` by unfolding
   the list and citing the per-prism theorems (the assembly pattern is demonstrated on the
   micro-example in `lean-shapes-scratch.lean`, `exBarrier_check'`). The soundness theorem takes
   the checker facts in exactly this split form (`hchain`, `hprisms`; §8.3), so the kernel work is
   per module and lake parallelizes it — under the thermal cap (`lake build -j2`, at most two
   heavy processes for this stream).
3. **Measured basis and projection.** The M1 audit measured the definition compiler at ≈ 5 ms/row
   (≈ 2 900 rows of `Instances.lean` in 13.9 s, `recon_lean_instances.log`) and `decide +kernel` at ≈ 1.5 ms/row on
   imported data (1 294 rows in ≈ 2 s). Projection for 5·10⁶ rows: ≈ 7 h compile + ≈ 2 h kernel
   single-threaded, ≈ 4.5 h at −j2 — batchable, not iterable. Therefore:
4. **The D-1 experiment (days; runs before item (b) of the Lean stream, on the micro-example's
   checkers extended to ≈ 10⁴ random rows per module):** measure per-row compile and kernel time
   for (a) the list-literal chunks above and (b) a compact encoding — one `Nat` literal per
   ≤ 1 000-row chunk (six 64-bit fields per row packed big-endian; kernel `Nat.div`/`Nat.mod` on
   literals are GMP-accelerated), decoded by a Lean function `decodeRows : ℕ → ℕ → List W1Row`
   evaluated inside `decide +kernel`. Decision rule: adopt (b) only if it cuts compile time by
   ≥ 3× at ≤ 1.5× the kernel time; otherwise (a). Either way the JSON format and the hypotheses
   are unchanged — the encoding is the emitter's business (`emit_lean.py`'s successor), and the
   decoded `PrismData` is what H2-B is stated about; the emitter's fidelity is checked by a
   back-parse (FORMAT.md §10), as for W1.
5. **Not viable, recorded:** a single `def` with all rows (fails at ≈ 10³ rows without
   `maxRecDepth`; unusable at 10⁶), and a monolithic `decide +kernel` over `d.prisms.all` for the
   whole certificate (serial hours, and one failure loses everything).

---

## 8. The Lean contract (type-checked shapes; `lean-shapes-scratch.lean`, log `lean-shapes-typecheck.log`)

The following elaborates against the working tree (Lean v4.33.0-rc2, the built `Zeta23.DBN.Defs`
and `Zeta23.W1.Soundness`); the names below are the ones `BarrierCert.lean` and `Instance02.lean`
must use, in `namespace Zeta23.DBN`.

### 8.1 The displayed hypotheses

    def PrismEnclOK (G : ℝ → ℂ → ℂ) (d : BarrierData) (p : PrismData) (τ' : ℝ) : Prop :=
      ∃ (U : Set ℂ) (f : ℂ → ℂ), IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ f U ∧
        List.Forall₂ (W1.RowEnclOK f p.K p.A) p.rows (W1.segs (toW1 d.rect p)) ∧
        (∀ z ∈ BarrierBdry d, ‖G (seamTime p) z - f z‖ ≤ (p.E : ℝ) / p.K) ∧
        (∀ t : ℝ, seamTime p ≤ t → t ≤ τ' →
          ∀ z ∈ BarrierBdry d, ‖G t z - G (seamTime p) z‖ ≤ (p.D : ℝ) / p.K)

    def BarrierEnclOK (G : ℝ → ℂ → ℂ) (d : BarrierData) : Prop :=
      List.Forall₂ (PrismEnclOK G d) d.prisms (nextSeams d)        -- nextSeams = later seams ++ [t₀]

    def AsymEnclOK (g : ℂ → ℂ) (d : AsymData) : Prop :=
      ∀ r ∈ d.rows, ∀ x y : ℝ, (r.Nlo : ℝ) ≤ windowIdx (At0 d) x → (windowIdx (At0 d) x : ℝ) ≤ r.Nhi →
        Ay0 d ≤ y → y ≤ AyA d → ((r.T : ℝ) - r.E) / d.K ≤ ‖g (x + y * I)‖

    def TailOK (g : ℂ → ℂ) (d : AsymData) : Prop :=
      ∀ x y : ℝ, (d.tail.N1 : ℝ) ≤ windowIdx (At0 d) x → Ay0 d ≤ y → y ≤ AyA d → g (x + y * I) ≠ 0

    def M2aEnclOK (c : Row2Cert) : Prop :=          -- H2 for the instance, G t z := Ht t z / Bt t z
      BarrierEnclOK G c.barrier ∧ AsymEnclOK (G (At0 c.asym)) c.asym ∧ TailOK (G (At0 c.asym)) c.asym

with `windowIdx (t x : ℝ) : ℕ := ⌊Real.sqrt (x / (4 * π) + t / 16)⌋₊`, `seamTime p = p.tn / p.td`,
`BarrierRect`/`BarrierBdry` the W1 `rectClosed`/`rectBdry` of the rectangle's rationals, and
`W1.RowEnclOK`, `W1.segs` the M1 definitions unchanged. H3 = `Polymath15Bridge' ∧ HtEntire` (§3.3,
§3.5); H1 as in §3.6.

### 8.2 Data and checkers

    structure PrismData where          -- §7.1 `prism`
      tn td K A : ℤ
      bottom right top left : List (ℤ × ℤ)
      rows : List W1.W1Row
      Fn Fd E D : ℤ
    structure RectData where xn1 xd1 xn2 xd2 yn1 yd1 yn2 yd2 : ℤ
    structure BarrierData where rect : RectData; t0n t0d : ℤ; prisms : List PrismData
    def toW1 (r : RectData) (p : PrismData) : W1.W1Data := { p1 := r.xn1, q1 := r.xd1, p2 := r.xn2,
      q2 := r.xd2, a1 := r.yn1, b1 := r.yd1, a2 := r.yn2, b2 := r.yd2, K := p.K, A := p.A, m := 0,
      bottom := p.bottom, right := p.right, top := p.top, left := p.left, rows := p.rows }
    def checkPrismW1 (w : W1.W1Data) : Bool := …      -- W1 C1, C3–C9 (m = 0) with C2′; §7.3
    def checkPrism (r : RectData) (p : PrismData) : Bool :=
      checkPrismW1 (toW1 r p) && decide (1 ≤ p.td) && decide (0 ≤ p.tn)
        && decide (0 ≤ p.Fn) && decide (1 ≤ p.Fd) && W1.floorRowsOK p.K p.Fn p.Fd p.rows
        && decide (0 ≤ p.E) && decide (0 ≤ p.D) && decide ((p.E + p.D) * p.Fd < p.Fn * p.K)
    def checkBarrierChain (d : BarrierData) : Bool := …  -- C-B0 (global), C-B2′, C-B13
    def checkBarrier (d : BarrierData) : Bool := checkBarrierChain d && d.prisms.all (checkPrism d.rect)

    structure AsymRow where Nlo Nhi T E : ℤ
    structure TailRow where N1 Q1 Q2 Q3 Q4 E1 : ℤ
    structure AsymData where K t0n t0d y0n y0d yAn yAd : ℤ; rows : List AsymRow; tail : TailRow
    def checkAsym (d : AsymData) : Bool := …           -- C-A1..C-A6, §7.4

(Full text in `lean-shapes-scratch.lean` §§B–C; the structure fields are written one per line there.)
Every check is +, ·, ^2, comparisons on ℤ and ℕ lengths — `decide +kernel`-expressible, no
`native_decide`, the NumericCert discipline.

### 8.3 The soundness theorems and the instance shape

    theorem cert_of_checkBarrier (G : ℝ → ℂ → ℂ) (d : BarrierData)
        (hchain : checkBarrierChain d = true)
        (hprisms : ∀ p ∈ d.prisms, checkPrism d.rect p = true)
        (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 d →
          ∃ U : Set ℂ, IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ (G t) U)
        (hEncl : BarrierEnclOK G d) :
        ∀ t : ℝ, 0 ≤ t → t ≤ t0 d → ∀ z ∈ BarrierRect d, G t z ≠ 0

    theorem cert_of_checkAsym (g : ℂ → ℂ) (d : AsymData) (hc : checkAsym d = true)
        (hEncl : AsymEnclOK g d) (hTail : TailOK g d) :
        ∀ x y : ℝ, ∀ r ∈ d.rows, (r.Nlo : ℝ) ≤ windowIdx (At0 d) x →
          Ay0 d ≤ y → y ≤ AyA d → g (x + y * I) ≠ 0

    theorem lambda_le_point2 (c : Row2Cert)                 -- Instance02.lean, with c := row2
        (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
        (hH2 : M2aEnclOK c)
        (hH3 : Polymath15Bridge' ∧ HtEntire) :
        ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0

(The instance theorem is stated for a `Row2Cert` argument in the scratch; `Instance02.lean` states
it for the literal `row2` and discharges the checker facts by the per-prism theorems.) The proof
plan of `cert_of_checkBarrier` is §4.6 D-B1…D-B9; of `cert_of_checkAsym`, §5.6; of
`lambda_le_point2`: from `hH2.1`, `hH3.2` and L-B3 obtain (iii′) via `cert_of_checkBarrier` at
G = Ht/Bt and `Ht = G · Bt`; from `hH2.2`, `hH2.3`, L-A1/L-A2 and `cert_of_checkAsym` obtain (ii′);
feed `hH3.1` with t₀ = 186/1000, X = 5000000194858, y₀ = 16733/100000 (its parameter side conditions
by `norm_num`), `hH1` (exact match), (ii′), (iii′); finish with t₀ + y₀²/2 ≤ 1/5 ≤ t (L-G).

### 8.4 Reuse map to the M1 v1 Lean layer (nothing in `W1/` is modified)

| W1 item | reused as | change |
|---|---|---|
| `W1Row`, `W1Data`, `segs`, `segPt`, `argIncrement`, `RowEnclOK`, `rectClosed/Open/Bdry`, `cover_chain` | verbatim, through `toW1` | none |
| `densPos`, `edgeOK`, `rowsOK`, `sumArgLo/Hi`, `floorRowsOK`, `mdist` | the body of `checkPrismW1`/`checkPrism` | none |
| `checkW1` | NOT reused (its C2 hard-wires the strip) | `checkPrismW1` restates C1, C3–C9 with C2′ |
| `ChecksOK`, `bdry_cover`, `boundary_nonvanishing`, `sum_arg_encl`, `edge_sum_eq`, `pin_m`, `row_box_excludes_zero`, `floor_of_checkW1Floor` | the D-B1/D-B2 chain | L-B0: `ChecksOK` split into a strip-free core (its hC2a/hC2c are used only at Soundness.lean lines 935–950, 1022, 1050, 1112, 1119, 1152 — the ζ-specific integrability and the AP call) |
| `RectArgPrinciple`, `rectArgPrinciple_of_local` | `RectArgPrincipleGen` | L-B0: drop the two strip hypotheses; the proof already ignores them (`_hhalf _hs2`) |
| `cert_of_checkW1` | the template for `cert_of_checkBarrier` | generic in G; the ζ-specific `continuousOn_zeta_logDeriv_seg` replaced by continuity from `DifferentiableOn` |

### 8.5 Type-check record

`lake env lean lean-shapes-scratch.lean` in `~/rh-lean-work/zeta-23-lean-main` (2026-09-02, Lean
v4.33.0-rc2): zero errors; exactly three `declaration uses 'sorry'` warnings — the two soundness
STATEMENTS and the instance-shape statement, whose proofs are the Lean stream's work items (b) and
(e); the four `norm_num` glue examples, the six `decide +kernel` micro-example facts (including the
two negative controls) and the assembled `exBarrier_check'` pass (`lean-shapes-typecheck.log`). The
scratch is not a program file and carries `sorry`; nothing from it enters `lean/Zeta23/` until the
Lean stream writes `BarrierCert.lean` without `sorry`.

---

## 9. The instance: Polymath15 Table 1 row 2, exact (task item 2; `row2_arith.py` / `row2_arith.log`)

| parameter | exact value | decimal | source / check |
|---|---|---|---|
| X | 5 000 000 194 858 | | P15 Table 1 row 2, p64 |
| t₀ | 186/1000 = 93/500 | 0.186 | same |
| y₀ | 16733/100000 | 0.16733 | same |
| t₀ + y₀²/2 | 3999993289/20000000000 | 0.19999966445 | recomputed exactly; ≤ 1/5 with slack 6711/20000000000 = 3.3555·10⁻⁷ |
| (1 + y₀)/2 = σ₀ of H1 | 116733/200000 | 0.583665 | exact; §3.6 (58367/100000 is a round-UP — not used) |
| X/2 = T₀ of H1 | 2 500 000 097 429 | | X even, exact |
| PT height | 3 000 175 332 800 | | PT Theorem 1 p2 |
| PT height − X/2 | 500 175 235 371 | | > 0: H1 is discharged by PT with this margin |
| PT's "2.51·10¹²" − X/2 | 9 999 902 571 | | > 0: PT's rounded pairing sentence (p5) is consistent |
| 1 − 2t₀ | 157/250 | 0.628 | (ii′)'s y² bound |
| 1 − y₀² | 9720006711/10¹⁰ | 0.9720006711 | |
| y₀² + 2t₀ | 3999993289/10¹⁰ | 0.3999993289 | < 1: Theorem 1.2's regions nonempty |
| √(1 − 2t₀) bracket | (1584929/2000000, 3962323/5000000] | (0.7924645, 0.7924646] | integer squares; yA := 3962323/5000000 satisfies C-A1 |
| √(1 − y₀²) bracket | (9859009/10⁷, 985901/10⁶] | | not needed by the certificate (D-H3 uses X + 1) |
| N₀ | 630 783 | | ⌊√(x/4π + t/16)⌋ ∈ [630783.14279635, 630783.14279643] at all four corners (x ∈ {X, X+1}, t ∈ {0, t₀}), mpmath interval arithmetic; matches Table 1 |
| x_{N₀}, x_{N₀+1} at t = 0 | ≈ 4 999 997 931 063.46, ≈ 5 000 013 784 381.94 | | [X, X+1] strictly inside the window; margin to x_{N₀} ≈ 2.26·10⁶ (L-A1 slack) |

**The pairing, redone (design note §0, task item 2).** Row 2 consumes RH to ζ-height X/2 =
2 500 000 097 429 (P15 eq. (1): x = 2T); PT Theorem 1 verifies it to 3 000 175 332 800; the row's
bound is t₀ + y₀²/2 = 0.19999966445 ≤ 0.2; so PT Corollary 2, Λ ≤ 0.2, is exactly this row paired
with PT's height, as PT say (p5: "The second row in Table 1 … provided one has shown H > 2.51·10¹²").
Row 3 (X = 2·10¹³ + 131252, Λ ≤ 0.19) would need X/2 ≈ 10¹³ — "higher than 10¹³", not available.
Row 2 is the unique Table-1 row that PT's height licenses. ✓

**The instance certificate.** `row2 : Row2Cert` with `barrier.rect = ⟨5000000194858, 1,
5000000194859, 1, 16733, 100000, 1, 1⟩`, `t0 = 93/500`, the prisms as produced;
`asym.t0 = 93/500`, `y0 = 16733/100000`, `yA = 3962323/5000000`, rows from N_start ∈ {630782, 630783}
to N_end = N₁ − 1, the tail at N₁ (indicatively 6–8·10⁶, §5.4).

**Expected scales (indicative, `row2_errbudget_indicative.log`; heuristic floats — the rigorous
values are the producers' to certify).** Barrier: e_{C,0} ≤ 4.1·10⁻⁴ at (X, y₀, t = 0), the worst
corner; 1.6·10⁻⁶ at y = 1; 1.0·10⁻⁷ at t = t₀; e_A + e_B ≤ 3·10⁻¹⁰. P15's Proposition 8.1 allowance
1.25·10⁻³ (p39) would also cover row 2's box, but the E row should carry the certified value (a
tighter E means larger admissible prisms through C-B12). The seam floors Fn/Fd are unknown until
the producers run; P15's X-selection heuristic (§8.1, p37–38: Euler-product fractional parts near 0
for p ≤ 11) was applied to row 2's X by the paper's authors, so floors of order 1 at t = 0 are
expected as for X₀ (P15 p45: "we expect |f_t(x+iy)| to stay well above 1"); a producer verifies
this cheaply before meshing (P-3). Asymptotic lane: P15's floor 0.0376 at N₀ (p64) against
e_{C,0} ≈ 10⁻⁷.

---

## 10. Producer requirements (informative — outside the trust boundary; both legs, D-R3)

* **P-1 Two legs.** Arb/FLINT (python-flint 0.6.0 `acb`) and mpmath 1.3.0 interval/ball; every
  transcript produced by both; disagreement beyond stated radii is stop-the-line (design note §4).
  The mp leg's transcendental endpoints go through `ball.iv_exp/iv_log/iv_atan/iv_pi/iv_cos/iv_sin`
  (never raw `iv.exp` etc.), under the stated weak platform assumption (each endpoint within 2⁻²⁷²
  relative of the truth at prec 288 — tested, cross-checked, not proved; `ball.py::_inflate`).
* **P-2 The evaluator.** f_t from (14)–(19) at N = N₀ (barrier) / N = N(x) (asymptotic), with α, M_t
  from (6)–(10); complex logs on the principal branch with the argument verified off the cut; no
  Taylor-expansion shortcut (P15 §7) unless its remainder is derived and added — the M1 rule
  "a DERIVED remainder for every truncation, quoted from p3-22a4 at exact page" applies to every
  sum truncation, Stirling-type step and series in the evaluator.
* **P-3 Before meshing:** verify N(x) = N₀ on the closed box (directed rounding) — otherwise f is not
  holomorphic on U and H2-B is false; sanity-check the floor scale at t = 0.
* **P-4 Rows:** whole-segment hull boxes (interval x over the segment) for C-B6/C-B11; endpoint
  enclosures for the argument rows via FORMAT.md §10's derivative-free recipe (D1–D3, branch
  formulas in `ball.py`), clamped to [−A/2, A/2] with A even; outward integer rounding at K and A;
  subdivide until C-B6 holds and until the argument-row sum width is comfortably < A/2.
* **P-5 Floor:** Fn/Fd from the hull boxes' coordinate distances (the C-B11 scheme), the largest
  rational the rows support (or any smaller one).
* **P-6 E:** e_A + e_B from (71)–(72) with Proposition 6.6(iv)–(v), e_{C,0} from the 10.50 form
  (D-2.4), every factor at its worst corner of the box × y-range (§5.2 monotonicities; for e_A + e_B
  the (82)–(86) chain of p39–41 re-instantiated with x ≥ X, t ≤ t₀, y ∈ [y₀, 1]); recorded with
  its inputs in `producer`.
* **P-7 The seam at t = 0:** Theorem 1.3 at t = 0 by the limit argument (§4.4); the argument is
  recorded in the transcript's `producer.comment` of prism 0 and is part of H2-B's discharge.
* **P-8 D:** from Lemma 8.4's |∂f_t/∂t| (p46) UNIFORMIZED over ∂R × [τ_j, τ_{j+1}] (evaluate each
  factor in its conservative direction on the box — the `DERIVATIVE_BOX_LEMMA.md` repair; never a
  corner value), times Δt, plus E(τ_j) + E(t) if routed through f (§4.5); D_t and Δt recorded.
* **P-9 Window rows:** T by a mollified triangle inequality uniform on the window × y-range
  (§5.2 options), E as in P-6 at the window's worst corner; both recorded.
* **P-10 Tail row:** Q₁…Q₄, E₁ as upper bounds (directed rounding), (S1)–(S4) verified and recorded
  with σ_{N₁}, σ″_{N₁}, ε_{N₁}, k₁, ρ₁, κ_T.
* **P-11 Cross-check cells (design note §3(b) step 4, mandatory for every transcript):** for the
  barrier, per prism: seam rows cell-wise on the common mesh refinement (as `crosscheck.py`), and the
  three scalars Fn/Fd, E, D compared as intervals (each leg's value must lie within the other's
  stated radius, or the larger of the two is used by both — recorded); for lane A: per row T and E;
  for the tail: the five quantities. Because the checker cannot see K, A, or the row↔segment
  alignment (FORMAT.md §8.1, carried forward), the cross-check is the only detector of a mis-scaled
  or rotated transcript.
* **P-12 Emission:** the JSON→Lean emitter (successor of `emit_lean.py`) writes the per-prism modules
  of §7.6; fidelity by back-parse.

---

## 11. Compatibility map to the Gomila artifact format (task item (e)) — M2a′ as a conversion

Read at commit `ea09b2f` (§0). The claim's row: X = 6 000 000 185 827, t₀ = 129/800, y₀² =
87677/2500000, barrier rectangle [X, X+1] × [1809/10000, 1], 883 prisms from t = 0, allowance
0.00125 per prism, finite lane N = 690988…3840000 (3 149 013 rows), tail from N★ = 3 840 000
(`CANDIDATE_PARAMETERS.md`, `BARRIER_CERTIFICATE.md`).

| Gomila object | this contract | conversion | status |
|---|---|---|---|
| rectangle [X, X+1] × [0.1809, 1] (y-floor below their irrational y₀) | `RectData` = ⟨X,1, X+1,1, 1809,10000, 1,1⟩ | direct | fits (C-B2′; the instance glue for M2a′ needs y₁ = 1809/10000 ≤ y₀, checked by squares: (1809/10⁴)² < 87677/2500000 — their own margin 234599/10⁸) |
| 883 closed time prisms, seams dyadic-stepped from 0, last enclosing 129/800 | the seam chain, C-B13 | seams are exact rationals in their code (dyadic) — direct; the last prism's right end must be exactly t₀ (C-B13 makes the last prism [τ_{J−1}, t₀]) | fits |
| per-prism gate M_i > D_z/(2(num−1)) + D_t·Δt + 0.00125 (`BARRIER_CERTIFICATE.md` eq. (1)) | C-B12 (E + D)/K < Fn/Fd with Fn/Fd ≤ M_i − D_z·h/2 (the hull-box floor), E = ⌈K·0.00125⌉ or their certified 3.5653·10⁻⁴, D = ⌈K·D_t·Δt⌉ | same inequality, the mesh term moved into the hull boxes | fits arithmetically |
| per-prism winding "strictly inside (−1/4, 1/4)" from mesh-point arguments; endpoint enclosures excluding zero; each argument increment inside (−π, π) | C-B6, C-B7, C-B8, C-B9 on per-segment rows | needs per-mesh-point value enclosures to build hull boxes and argument rows | **NOT convertible from the sealed logs**: `barrier_target_closed.log` (896 lines) holds ONE summary line per prism — `Prism(k) t=[…] winding=… min_mesh=… Dz=… Dt=… spatial=… time=… eps=… margin=… mesh=38396 PASS` — no per-point data (the C source prints only these summaries: `TloopSinglemat_closed_cert.c` lines 1446–1466). Conversion = re-running their producer with a per-point emitter added (their C source and stored-sum matrix are in the repo), or running D1's own legs on their prisms — the latter is what step 4 of the screen requires anyway. |
| stored 62×62 coefficient matrix at 20 digits + Taylor-tail bound 1.95·10⁻²² | producer-internal (P-2) | not a transcript object | n/a; D1's legs evaluate f_t directly (P-2), no stored sum |
| finite lane rows `N <n> L12 <12-decimal floor> GT089 <0/1>` (`verify_finite_and_binding.py` regex), per-N singletons; global E_max = 2.33494905212337849·10⁻⁷ (`CANDIDATE_PARAMETERS.md`) | `AsymRow` ⟨N, N, T = floor·10¹², E = ⌈E_max·10¹²⌉⟩ at K = 10¹² | direct (their P11/P7/P5/P23 shards concatenate to consecutive N; the y-range [y₀, y_max] with y_max² ≥ 1 − 2t₀ = 271/400 — C-A1 with yA = 8231039/10⁷ from their bracket) | fits; 3.1·10⁶ rows (packaging §7.6 applies; or coarsen by taking the minimum floor over N-ranges) |
| tail: their P1113 contraction theorem at N★ = 3 840 000 (`TAIL_LEMMA.md`, "an all-N contraction … not merely a description of the numerical output") | Lemma T's tail row | **not convertible**: a different lemma with different finite quantities; either D1 recomputes Lemma T at their parameters (N₁ then ≈ 7–9·10⁶ by the crude method — so their finite lane would have to be extended by D1's producers from 3 840 001 upward), or `TailOK` for M2a′ is discharged by their lemma as prose (flagged unrefereed; `gomila-screen.md` §5) | decision deferred to M2a′; both paths keep the Lean shape |
| E: `verify_uniform_error_01787854.c`, 10.50 weld, e_A + e_B + e_{C,0} < 3.56523011600040·10⁻⁴ on the whole box incl. t = 0 by their limit argument | E row (§4.4), P-7 | direct (one number) | fits |
| D_t, D_z per prism from `DERIVATIVE_BOX_LEMMA.md` (box-uniformized Lemma 8.4) | D row = D_t·Δt (+ E terms if routed through f), P-8 | direct from the log's `Dt` and the prism's Δt | fits |
| trust: their fail-closed C/Python verifiers, sealed logs | untrusted producers + `decide +kernel` on the rows | n/a | their verifiers are producer-side by our vocabulary |

Bottom line for the screen: steps 3–4 remain D1-side. The finite lane converts by a script; the
barrier needs regenerated per-point data (their code or ours); the tail needs a decision. Nothing
about the claim is a record (bracket of record 0 ≤ Λ ≤ 0.2); their Lean branch is cited here only
through `gomila-lean-branch-verify.md`, whose `#print axioms` output is on disk.

---

## 12. Worked micro-example (ARTIFICIAL data; all integers; files in this directory)

**Honesty label:** the numbers are invented to exercise every check with small integers; no
producer certified H2 for them; "accept" means exactly and only that C-B0..C-B13 / C-A1..C-A6 pass.
Files: `m2a-example-barrier-manifest.json`, `m2a-example-barrier-prism-{0,1}.json`,
`m2a-example-asym.json`. Verified twice: by the untrusted reference checker
(`barrier_ref_checker.py`, run record `ref-checker-run.txt`, with fifteen negative controls) and by
the Lean kernel on the same numbers (`lean-shapes-scratch.lean` §E: `exBarrier_check`,
`exPrism{0,1}_check`, `exBarrier_chain`, `exAsym_check` by `decide +kernel`, plus `exPrism0_bad` and
`exAsym_bad` for two mutations, and the assembled `exBarrier_check'`).

**Barrier lane.** R = [10, 11] × [1/5, 1] (a toy X; the instance's is 5·10¹²), t₀ = 1/10, two
prisms with seams 0 and 1/20. Prism 0: K = 100, A = 1000, mesh two segments per edge (bottom
[10, 21/2, 11], right [1/5, 3/5, 1], top [11, 21/2, 10], left [1, 3/5, 1/5]), M = 8 rows, all with
reLo ≥ 300 (C-B6 by reLo > 0) and imLo < 0 < imHi; argument rows straddling 0:
S_lo = −12−10−11−13−14−12−15−9 = **−96**, S_hi = 15+14+13+12+11+16+10+17 = **108**;
C-B8: 2·(108 − (−96)) = 408 < 1000 ✓; C-B9: −96 ≤ 0 ≤ 108 ✓. Floor 5/2: every row has mre = reLo ≥ 300,
mim = 0, so (mre² + mim²)·Fd² ≥ 90000·4 = 360000 ≥ Fn²·K² = 25·10000 = 250000 ✓ (C-B11).
E = 20 (0.20), D = 100 (1.00): C-B12: (20 + 100)·2 = 240 < 5·100 = 500 ✓ — i.e. 0.2 + 1.0 < 2.5.
Prism 1: mesh three/one/two/one segments (M = 7), all rows with reHi ≤ −10 (C-B6 by reHi < 0) and
imLo ≥ 250; S_lo = **−55**, S_hi = **57**, 2·112 = 224 < 1000 ✓, −55 ≤ 0 ≤ 57 ✓; floor 12/5: the
weakest row is row 0 with mre = 40, mim = 250: (1600 + 62500)·25 = 1 602 500 ≥ 144·10⁴ = 1 440 000 ✓;
E = 20, D = 150: (20 + 150)·5 = 850 < 12·100 = 1200 ✓. Chain (C-B13): seams 0 < 1/20 < t₀ = 1/10 by
cross-multiplication (1·10 < 1·20 … i.e. 1/20 < 1/10 ⟺ 1·10 < 1·20) ✓; C-B2′: 10 < 11, 1/5 < 1,
1/5 > 0 ✓. **Verdict: ACCEPT** (both checkers). Modulo H2-B (false here — artificial) and the
holomorphy input, the transcript would certify: G_t ≠ 0 on [10, 11] × [1/5, 1] for all t ∈ [0, 1/10].

**Asymptotic lane.** K = 1000, t₀ = 1/10, y₀ = 1/5, yA = 9/10: C-A1: (10 − 2·1)·10² = 800 ≤ 9²·10 =
810 ✓ (yA² = 0.81 ≥ 0.8 = 1 − 2t₀). Rows (5,5,400,30), (6,9,350,25), (10,20,300,20): E < T ✓,
consecutive 5→6, 9→10 ✓ (C-A3, C-A4). Tail N₁ = 21 = 20 + 1 ✓ (C-A5); Q₁ + Q₂ + Q₃ + Q₄ + E₁ =
1500 + 100 + 50 + 20 + 5 = 1675 < 2000 = 2K ✓ (C-A6). **Verdict: ACCEPT.**

**Negative controls** (`ref-checker-run.txt`): box containing 0 → C-B6; over-wide argument rows →
C-B8; argument sum excluding 0 → C-B9; floor 4/1 → C-B11; D = 400 → C-B12 ((20+400)·2 = 840 ≥ 500;
also kernel-rejected: `exPrism0_bad`); bottom[last] ≠ x₂ → C-B3; a row removed → C-B4; a prism's
manifest seam moved → the manifest/prism consistency check; t₀ = 1/40 below the last seam → C-B13;
x₂ = x₁ → C-B2′; E = T → C-A3; a gap in the windows → C-A4; tail N₁ ≠ N_end + 1 → C-A5; Q₁ = 1900 →
C-A6; yA = 8/10 → C-A1 (also kernel-rejected: `exAsym_bad`). Each rejects at exactly the named check.

---

## 13. Constraints discharged, open items, verification ledger, files

### 13.1 The M1 v1 audit constraints (1)–(8), status

1. **Bulk-data packaging settled before `BarrierCert.lean`:** §7.6 (per-prism JSON files and per-prism
   Lean modules with ≤ 1000-row chunk defs; the D-1 experiment with a decision rule; the Lean
   contract already split so that per-prism kernel facts assemble — `checkPrism` takes `RectData`).
2. **mp-leg platform assumption and the ball discipline:** P-1, P-2; every truncation with a derived
   remainder; the E and D derivations cite (71)–(74), 6.6, Lemma 8.4 at pages p31, p46.
3. **A even:** P-4; checker unchanged (C-B7 is sound for any A ≥ 1, as W1's C7).
4. **Trust wording:** §0, §3.7, §6; existential conclusion of W1 unchanged; f_DH untouched; never
   "fully machine-checked". Note: since 2026-09-02 W1's own label is "modulo H-ENCL" (H-AP proved).
5. **The checker cannot see K, A, alignment:** P-11 makes the cell-wise cross-check mandatory per
   prism and per row; the same blindness applies to E, D, T, Q_i (scalars).
6. **Gomila steps 3–4 blocked D1-side; nothing is a record; PT's exact height cited:** §11, §9.
7. **Gomila Lean branch cited only with axioms on disk:** §11 last paragraph.
8. **`Instances.lean` vs `AuditOCases.lean` identifiers:** `BarrierCert.lean` imports `Zeta23.W1.Soundness`
   (and, for L-B0, `Zeta23.W1.ArgPrincipleBridge`), never the audit scratch modules.

### 13.2 Open items and fallbacks (for the Lean stream and the producers)

* **The `Polymath15Bridge` replacement (§3.2–3.3) is blocking** for `Instance02.lean`: it changes
  the trusted layer and needs a dated deviation record (Defs header + design note §7 addendum).
* L-B3 (B_t holomorphic and nonvanishing near R): expected ≤ 100 lines; fallback = display it as
  part of H2 (existential normalizer) — shapes unchanged, label amended.
* L-B1 (half-plane FTC lemma): the one new analytic lemma; Mathlib has `Complex.hasStrictDerivAt_log`
  (`Analysis/SpecialFunctions/Complex/LogDeriv.lean`, on `slitPlane`) and
  `intervalIntegral.integral_eq_sub_of_hasDerivAt` (`FundThmCalculus.lean`); `Real.pi_lt_d6` and
  `Real.pi_lt_d20` exist for L-A1 (`Analysis/Real/Pi/Bounds.lean`) — all four names verified in the
  pinned Mathlib this session.
* The D-1 packaging experiment (§7.6 item 4) before item (b).
* N₁ for the crude tail (indicatively 6–8·10⁶) makes lane A's finite range ≈ 5–7·10⁶ windows;
  a mollified tail lemma (out of scope) would shrink it.
* Theorem 1.3 at t = 0 (P-7) is a producer-recorded limit argument inside H2-B; M2b should prove it.
* Corpus: rename `p3-22a5` (§0) and fix `corpus-routing.md` line 101 / `FETCH-LIST-RESPONSE.md`
  line 324; fetch the published Polymath15 (Res. Math. Sci. 6 (2019) 31) if page-exact citations to
  the published version are ever needed.

### 13.3 What this contract does not settle

The proofs of `cert_of_checkBarrier`, `cert_of_checkAsym`, `lambda_le_point2` (Lean stream items
(b), (e)); the producers' f_t evaluators (items (c), (d)); the rigorous E, D, T, Q_i, E₁ values for
row 2 (every number in §9's "expected scales" is heuristic and labeled so); the comparator packaging
(item (f)); the choice between Lemma T and a mollified tail for M2a′.

### 13.4 Verification ledger (standing order 5)

Read from disk this session (pdftotext, page-verified): P15 Theorem 1.2 + simplified region (p2–3),
region (5) (p3), (6)–(11) (p4), Theorem 1.3 with (13)–(24) and the holomorphy remark (p6),
Corollary 1.4 (p7), Theorem 1.5 (p9–10), Theorem 3.2 (p14), Proposition 3.3 with proof (p15–16),
(69)–(74) and Proposition 6.6 with the 10.44 remark (p30–31), §8.1–8.2 (p37–39), Proposition 8.1
with proof (p39–42), §8.3 incl. Lemma 8.2 and its proof (p42–44), §8.4 incl. (91) and Lemma 8.4
(p44–48), mesh counts (p49), §8.5 (p50–56), Proposition 9.1 (p56), §10 with Table 1 (p62–67); PT
Theorem 1 (p2) and §3.4 (p5); `Defs.lean` in full; `W1/{Format,Checker}.lean` in full,
`W1/Soundness.lean` lines 1–240, 455–490, 925–950, 1162–1262 and its declaration index,
`W1/ArgPrincipleBridge.lean` lines 360–459; the Gomila files listed in §0. Recomputed exactly
(Python `fractions`, `row2_arith.log`): every entry of the §9 table; the σ₀ finding. Recomputed by
mpmath interval arithmetic: N₀ and the x_{N₀} bracket. Indicative only (floats): the error budget,
the tail sums. Derived here: D-2.4, D-3.2, D-H3, D-B1…D-B9, Lemma T (§5.4), the §4.7(3) count.
Type-checked: every Lean shape in §3 and §8 (`lean-shapes-typecheck.log`). Run: the reference
checker on the examples and fifteen mutations; the kernel on the examples and two mutations.
Not verified: the Gomila numbers beyond what their files state (unaudited, as in the screen); the
published Polymath15 page numbers (not on disk).

### 13.5 File inventory (this directory)

| file | role | trust |
|---|---|---|
| `SPEC.md` | this contract | normative |
| `barrier-schema.json` | JSON Schema 2020-12 shape contract (manifest / prism / asymptotic) | normative (shape only) |
| `m2a-example-barrier-manifest.json`, `m2a-example-barrier-prism-{0,1}.json`, `m2a-example-asym.json` | §12 micro-example | artificial data |
| `barrier_ref_checker.py` | reference implementation of C-B0..C-B13, C-A1..C-A6 | UNTRUSTED (the trusted checker is the Lean one) |
| `ref-checker-run.txt` | run record: both examples ACCEPT; fifteen negative controls reject at the named check | evidence, rerunnable |
| `lean-shapes-scratch.lean`, `lean-shapes-typecheck.log` | the Lean shapes of §3/§8 type-checked against the working tree; the micro-example kernel-checked | scratch (contains `sorry` in three statements; not a program file) |
| `row2_arith.py`, `row2_arith.log` | exact row-2 arithmetic (§9) | exact (Fractions) + mpmath intervals for N₀ |
| `row2_errbudget_indicative.py/.log`, `row2_tail_indicative.py/.log` | indicative magnitudes (§4.4, §5.4, §9) | heuristic floats — NOT certificates |


---

## 14. Errata and audit notes (final audit, 2026-09-03; `results/d1-m2a/AUDIT.md`) — append-only; v1.0 text above unchanged

1. **§2.3, the quotation of (14).** The PDF carries an overline on s_* in the second sum — `n^y b_n^t / n^{\overline{s_*} + κ}`
   (page image of PDF p6 re-read by both producer agents and by the auditor); `pdftotext` drops it, so the quotation
   above reads `n^{s*+κ}`. The overline reading is the only one consistent with (69)–(70) and (92) (`ft_mp.py` D-F1,
   `producer_arb.py` D-A1), and it is what both producers implement and what the auditor's independent direct evaluator
   (`audit/audit_direct.py`) uses. Wording only; no check or hypothesis changes.
2. **§2.3, (21) versus Proposition 6.6(ii).** The paper's (21) has `4y(1+y)/x²` inside the positive part where Prop. 6.6(ii)
   (p31) has `8y(1−y)/x²`. Neither producer uses either display (both enclose Re s_* from (17) directly); the
   difference is ≈ 10⁻²⁵ at the instance. Recorded for the corpus, immaterial for the certificate.
3. **§2.4 / P-6, the exponent of 6.6(iv)–(v).** It is `log²(x/(4πn²))` (p31). `ft_mp.py`'s docstring had `x/(4πn)`;
   corrected 2026-09-03 with a dated note (AUDIT.md F-1). Both legs majorize it by δ₁ of (84), valid for n ≤ N, N² ≤ x/(4π).
4. **§7.1, `trust_label`.** The schema's constant is the label of the FULL certificate (H1, H2 = H2-B ∧ H2-A ∧ H-TAIL, H3).
   A barrier-lane transcript on its own is "kernel-checked modulo H2-B and `hHol`" (`lean-notes.md` §1); the manifest
   string is not wrong (it names what the transcript is a component of) but a v1.1 of this contract should carry a
   per-lane label. Wording only.
5. **§7.6 item 3, the cost projection.** The projection was for 5·10⁶ rows; the actual row-2 transcripts are 7 176 and
   10 771 rows (mp, Arb), the per-prism modules build in 3–4 s each (import-dominated), and the monolithic
   `decide +kernel` on both full literals takes 28 s (`kernel-time.log`). The per-prism packaging stands as the program's
   choice; the "serial hours" concern does not arise at this scale.
