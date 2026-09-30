# Insights digest — Session-36 novel-approach wave (KICKSTART 10(a))

Consolidation agent (Opus 5.5), 2026-09-30. Sources: `WAVE-CHARTER.md`; per seed `read-F.md` (binding where it differs from
the NOTE), `NOTE.md`, `SHARED.md`; `results/haglund-cert-s37/BRIEF.md` and `producer-A/CERT.md`; `results/novel-wave-s37/WAVE-CHARTER.md` §0.
Nothing here is new mathematics: every statement is quoted or pointed to; status labels are copied from the source.
Seed folders are abbreviated `ly/` (N1 `ly-infinity`), `st/` (N2 `staircase`), `fp/` (N3 `fingerprint`), `tn/` (N4 `tournament`),
all under `results/novel-wave-s36/`.

## §A Per seed

### A.1 N1 `ly-infinity` — Lee–Yang functions of the primes. Close (K), UPHELD (`ly/read-F.md` header: "AGREES … No FIX-FIRST item").

Three most useful findings.
1. Theorem 1 (counting along inner channels), `ly/NOTE.md` §2: "|N_F(t_1, t_2) − (1/2π)·Σ_j d_j·|Δ_{[t_1,t_2]} arg v_j(½ + it)|| < |d|";
   the reader adds that the monotonicity of arg v_j holds for EVERY inner function of Re s > ½ (`ly/read-F.md` §1, step 4).
2. Nakamura's f(s, χ) = 7^s·L(s, χ) + G(χ)·L(s, χ̄) (χ cubic mod 7) is an RH-false control with EXACTLY Riemann's functional
   equation (residual 10⁻³⁰; 31 off-line zeros with 0 < t < 45): the integer-lattice support in the Hamburger acceptance test is
   sharp (`ly/NOTE.md` §6 (2), `ly/verify/f_hamburger_checks.log`).
3. Proposition 3, `ly/NOTE.md` §2: outside the prime basis (the Alon–Cohen–Vinzant class) the Hurwitz route is equivalent to RH —
   "Under RH, Ξ is a locally uniform limit of zero-free multiples of real-rooted Dirichlet polynomials. Conversely (Hurwitz), such a
   limit is real-rooted." The reader: "the ACV class is tautological" (`ly/read-F.md` §1).

Most useful failure. Inverse design (task d): a fitted unitary coupling U tracks ζ's zeros out of sample no better than the
prime-free baseline and worse than the parameter-free aligned product in 2 of 3 configurations; "the fit is parameter counting
plus the density match … not arithmetic" (`ly/NOTE.md` §4). The coupling search (k ≤ 6 slow archimedean channels) found no
evasion of the gap; the optimum always decouples the prime channel (§4, "Status: **open**").

Borrow. (i) The inner-channel counting device (Theorem 1): zero density = total winding of the inner channels, error < |d|.
(ii) The S-part detector as an RH-false test: DH's S-truncations carry an off-line zero converging to DH's own
(distance 0.193 at X = 7, 0.0081 at X = 10⁴; `ly/NOTE.md` §5). (iii) Nakamura's f(s, χ) as a control for any test that
consumes only the functional equation.

Close (K), carried by Theorem K (`ly/NOTE.md` §2): "*Setting.* U := {|Re t| < 14.2, |Im t| < ½}. f_k(t) := P_k(v(½ + it)), where
P_k is Lee–Yang in the prime channels p^{1/2−s} (p ∈ S_k finite), optionally with one extra archimedean channel Θ_k(s) of
degree ≤ 1 (any meromorphic inner function). h_k is holomorphic and zero-free on U. *Claim.* h_k·f_k does not converge uniformly
on compact subsets of U to Ξ." Re-derived and re-run by an independent method (40 Haar-random U, `ly/verify-F/rerun_theoremK.log`:
"**CONFIRMED**"). Status (`ly/read-F.md` §4): Theorem 1, Corollary 2, Theorem K, Propositions 3–4, Lemma F "dual-model (Opus
writer + this read)"; novelty of the application to Ξ "single-check (Opus) … not for external use without the second check".
Open edge: several coupled slow archimedean channels (`ly/NOTE.md` §8), priority "LOW unless a rung-1 model appears" (`ly/read-F.md` §3(b)).

### A.2 N2 `staircase` — real-rootedness chains from Riemann's incomplete-gamma series. Close (K), UPHELD (`st/read-F.md`: "AGREES-WITH-CORRECTIONS"; F1–F5 applied in `st/NOTE.md`, pre-read copy `st/NOTE.pre-reader.md`).

Three most useful findings.
1. Theorem A, `st/NOTE.md` §2: "Let w ≢ 0, and either (i) 0 ≤ w_n ≤ 1 with some w_m < 1 (covers C1 for every N, C2 for every finite
   S, every smooth cutoff with 0 ≤ φ ≤ 1), or (ii) w finitely supported with arbitrary real values. Then ξ_w has only finitely many
   zeros on Re s = ½ and infinitely many zeros off it." With Theorem B ("If every zero of ξ_w lies on Re s = ½, then w ≡ 1").
2. Haglund's Conjecture 1 (arXiv:0910.5228, open since 2009, implies RH) is FALSE at N = 27: off-line zero
   0.8152587993782148453823 + 3143.220682421536585287 i below real zeros t = 3144.8946…, 3145.5998… (`st/NOTE.md` §4 item 1);
   its C1 analogue fails at N = 24 (0.8159896243… + 2508.2839748… i). Both at heights where RH holds, so "monotonic zeros" is
   "not implied by RH: it fires on the RH-TRUE control". Certification status: §D below.
3. Proposition F (approximation staircases are height filtrations), `st/NOTE.md` §2: "**Consequence:** in any induction 'members
   real-rooted up to T_N ⟹ up to T_{N+1}', the only content is RH on the new window T_N < |Im s| ≤ T_{N+1}; … The step's missing
   lemma is literally 'no zero of ξ off the line with T_N < γ ≤ T_{N+1}'." Proposition E(b) needed the reader's paragraph F3
   (`st/read-F.md` §3) to exclude zeros with Re s ≥ 2 for large N.

Most useful failure. The orchestrator's prime chain C2 never brings the Euler product to the zeros: "in the tracking window a C2
member equals Ξ + P with P > 0 of size e^{−πm²}, m the least excluded integer — the same as the C1 member N = m − 1; the Euler
factor (1 − 2^{−s})^{−1} appears only in the Γ-dominated region" (`st/NOTE.md` §10 item 4; S = {2} agrees with C1 N = 2 to 1.2e−10, §3).

Borrow. (i) The one-sided approximants (Theorems D, D′): ξ_N from above and Haglund's Ξ_N from below on the line, "two
super-exponentially accurate one-sided approximants built from finitely many incomplete gamma functions" (§2, D′(3)).
(ii) The visibility law: an off-line zero of the limit at height γ₀ enters the member only when "departure height ≈ 4(N+1)² + 8
… exceeds γ₀" (§9). (iii) The complete-census discipline: argument-principle total, count = (Z_tot − Z_line)/2, every zero
re-solved by a second formula at a second precision and circle-counted (§3).

Close (K), carried by Theorems A and B (Z₁) with Proposition F (Z₂), the computed counterexamples (Z₃) and the axiom-level control
(Z₄: "the chain's one positivity generator (Pólya's criterion, Theorem D) holds verbatim for the RH-false positive Euler product
F_{2.9,2}", `st/NOTE.md` §0). Status (`st/read-F.md` §4): "Theorems D, D′, A, B, Proposition F: dual-model (Opus writer + this
read). Proposition E: (a), (c) as corrected; (b) with the reader's paragraph F3." The decisive computation was re-run in Arb ball
arithmetic at 4800 bits from Haglund's own (10), (13), (14): "**CONFIRMED**" (`st/read-F.md` §2).

### A.3 N3 `fingerprint` — Jacobi / Schur / Verblunsky parameters of ζ. Close (K) for the seed's mechanism (task (d)), UPHELD; "the tables stand as an instrument" (`fp/read-F.md` header).

Three most useful findings.
1. Theorem D, `fp/NOTE.md` §6, for g_{a,q}(s) = a/√q + q^{s−1/2} + q^{1/2−s}: "(ii) If |a| < 2√q (θ real), every node 1/w_k is real
   positive with positive mass: multiplication by g preserves the positivity of every fingerprint, for every Λ … (iii) If |a| > 2√q
   … its fingerprint fails at a finite index for EVERY Λ … (iv) (Euler factors) a = −(p + 1): |a| − 2√p = (√p − 1)² > 0 for every
   p > 1 … Multiplying or dividing ξ by one Euler factor never preserves positivity; the fingerprint has no prime-by-prime positivity
   induction." Scope (`fp/read-F.md` §3(a)): (i)–(iii) are "one step from (E1)"; the value is the exact one-prime boundary |a| ≤ 2√q.
2. Proposition M (Hermite–Krein count), `fp/NOTE.md` §5: the Hankel form has exactly J negative squares when J off-line pairs are
   resolved, "so generically (non-adjacent flips) **#{n: b_n² < 0} = 2J**"; on Davenport–Heilbronn the "−+−" motifs sit one per
   off-line zero with t ≤ 241 ("The fingerprint is a spectral MAP of the off-line zeros"). DH map single-producer (`fp/read-F.md` §3(b)).
3. Visibility without early warning, `fp/NOTE.md` §5: n_fail ≈ n_WKB(T) + lag, lag logarithmic in 1/δ, at ≈ 6 digits per index;
   "Below its resolution index an off-line pair is indistinguishable from an on-line pair split by ±δ … There is no early warning:
   the IV.9 'deceptive' regime, measured." Li's λ_n need n ~ T²/δ (≈ 3×10⁵ for DH's first zero; DH's λ_1..λ_601 all positive).

Most useful failure. The mining task found no arithmetic: the fingerprint carries the explicit formula's prime lines (log 2, 3, 4, 5)
through a low-pass transfer plus a combination tone at log(3/2); "No prime structure appears that is not already in the zeros;
the fingerprint is not an arithmetic coordinate system" (`fp/NOTE.md` §7). PSLQ at 300 digits: "no relation" (§8); the leading
term of the asymptotic law "carries no arithmetic beyond the density (conductor)" (§4).

Borrow. (i) The fingerprint as the wave's common certified diagnostic for RH-true approximation schemes: "a member with a motif is
a certified counterexample to that scheme's conjecture, with its height read off from t_n" (`fp/NOTE.md` §11). (ii) Uvarov
bookkeeping: s_m(Λg) = s_m(Λ) + Σ_k w_k^{−m} (Theorem D(i)) prices any finite multiplier exactly. (iii) The injection method (ζ
plus one off-line quadruple, exact in the moments) for measuring any detector's visibility threshold (§5).

Close (K), carried by Theorem D ("Z (the proved statement): Theorem D", `fp/NOTE.md` §0). Re-run with independent code and library
(mpmath at 60 digits against the writer's Arb at 24 000 bits): "**CONFIRMED**" (`fp/read-F.md` §2). Status (`fp/read-F.md` §4):
"Theorem D, Propositions S and M: dual-model at the level read (Opus writer + this read; Proposition S's Szegő relations are
[recalled] by the writer and numerically checked by the writer only)." Conjecture W is "Instrument-level, not load-bearing
anywhere" (`fp/read-F.md` §3(c)). Disguise audit: the fingerprint positivity "IS Weil positivity with multiplier 1 … It is a
re-dress, not a generator (S4 fails)" (`fp/NOTE.md` §0).

### A.4 N4 `tournament` — 35 mechanisms run to a brief-time verdict. Close (N), UPHELD: "nothing survives, correctly" (`tn/read-F.md` header).

Three most useful findings.
1. DD1, `tn/NOTE.md` §2.1: pointwise Λ ≥ 0 separates all three computed RH-false controls — Epstein x² + 5y² first fails at n = 36
   (Λ(36) = −2 log 36), DH at n = 3, every F_{a,q} at q², by the derived identity "Λ_F(q²)/log q = 1 − (α² + β²) = 1 − a² + 2q
   < 1 − 2q < 0"; Euler-product controls give no negative value to 2·10⁵. Re-run: "**CONFIRMED**" (`tn/read-F.md` §2).
2. The rung-1 twin, `tn/NOTE.md` §2.1: the virtual curve Z(u) = (1 − 5u + 5u²)/((1 − u)(1 − 5u)) over F₅ "is an Euler product with
   Λ ≥ 0, rational, with FE; its zeros sit at σ = 0.79899 and 0.20101"; so "the function-field analog of 𝒫 therefore does NOT
   imply RH". The reader's rule: "a mechanism the virtual curve passes cannot be the generator" (`tn/read-F.md` §3).
3. The synthesis, `tn/NOTE.md` §4: "Four ways to die" — (a) local objects own zeros or own none, (b) finiteness hypotheses fail
   exactly on the line, (c) hypotheses satisfied by an RH-false world, (d) wrong output type — and "Every EQUIV row, stripped of its
   failed generator, is Weil/Li/Lagarias positivity with multiplier 1." Carried into §B and §F below.

Most useful failure. DD2, the Krein–Langer Pick kernel on a disk in Re s > 1 (`tn/NOTE.md` §2.2): it decides RH exactly in
principle and flags DH with exactly one negative square, but "the negative square, global in principle, is exponentially local in
practice: ≈ 6 digits per unit of height offset … no gain over Turing-method verification". Lesson carried as survivor property (3):
the transport from Re s > 1 inward "must be a theorem, not a computation" (§4).

Borrow. (i) Λ ≥ 0 as a one-line axiom screen: any mechanism whose inputs DH, F_{a,q} and Epstein all satisfy is I.1-blind.
(ii) The rung-1 twin test (virtual curve (q, a) = (5, 5)) as a mandatory control, now adopted in `results/novel-wave-s37/WAVE-CHARTER.md`
§0 (e). (iii) The labeling rule for the table (§C.3 below): rows resting on `[recalled, unverified]` statements are "screened at
brief time" only.

Close (N), carried by the table (`tn/NOTE.md` §3: "35 rows: 26 DEAD, 9 EQUIV, 0 OPEN") and the three deep dives. The one
self-contained new proof in the table is the T6 lemma, re-derived by the reader: "an infinitely divisible law with all exponential
moments has an n-th convolution root with the same property for every n, so φ = φ_n^n with φ_n entire; the order of any zero of φ
is divisible by every n, hence there is none. ✓ So the tilted Riemann kernel Φ(u)e^{εu} is never infinitely divisible, whatever
the truth of RH" (`tn/read-F.md` §1). "The zoo gains exactly two things from this seed: the control 'virtual curve over F₅' … and
the T6 lemma" (`tn/read-F.md` §3). Deep-dive probability estimates, as the writer gave them: DD1 "< 0.5%", DD2 "< 0.5%", DD3 "< 0.3%".
