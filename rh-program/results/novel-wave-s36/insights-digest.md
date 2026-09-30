# Insights digest — Session-36 novel-approach wave (KICKSTART 10(a))

Consolidation agent (Opus 5.5), 2026-09-30. Sources: `WAVE-CHARTER.md`; per seed `read-F.md` (binding where it differs from the NOTE), `NOTE.md`, `SHARED.md`;
`results/haglund-cert-s37/BRIEF.md` and `producer-A/CERT.md`; `results/novel-wave-s37/WAVE-CHARTER.md` §0.
Nothing here is new mathematics: every statement is quoted or pointed to; status labels are copied from the source.
Seed folders are abbreviated `ly/` (N1 `ly-infinity`), `st/` (N2 `staircase`), `fp/` (N3 `fingerprint`), `tn/` (N4 `tournament`),
all under `results/novel-wave-s36/`.

## §A Per seed

### A.1 N1 `ly-infinity` — Lee–Yang functions of the primes. Close (K), UPHELD (`ly/read-F.md` header: "AGREES … No FIX-FIRST item").

Three most useful findings.
1. Theorem 1 (counting along inner channels), `ly/NOTE.md` §2: "|N_F(t_1, t_2) − (1/2π)·Σ_j d_j·|Δ_{[t_1,t_2]} arg v_j(½ + it)|| < |d|"; the reader adds that
   the monotonicity of arg v_j holds for EVERY inner function of Re s > ½ (`ly/read-F.md` §1, step 4).
2. Nakamura's f(s, χ) = 7^s·L(s, χ) + G(χ)·L(s, χ̄) (χ cubic mod 7) is an RH-false control with EXACTLY Riemann's functional equation (residual 10⁻³⁰; 31
   off-line zeros with 0 < t < 45): the integer-lattice support in the Hamburger acceptance test is sharp (`ly/NOTE.md` §6 (2),
   `ly/verify/f_hamburger_checks.log`).
3. Proposition 3, `ly/NOTE.md` §2: outside the prime basis (the Alon–Cohen–Vinzant class) the Hurwitz route is equivalent to RH — "Under RH, Ξ is a locally
   uniform limit of zero-free multiples of real-rooted Dirichlet polynomials. Conversely (Hurwitz), such a limit is real-rooted." The reader: "the ACV class
   is tautological" (`ly/read-F.md` §1).

Most useful failure. Inverse design (task d): a fitted unitary coupling U tracks ζ's zeros out of sample no better than the prime-free baseline and worse than
the parameter-free aligned product in 2 of 3 configurations; "the fit is parameter counting plus the density match … not arithmetic" (`ly/NOTE.md` §4). The
coupling search (k ≤ 6 slow archimedean channels) found no evasion of the gap; the optimum always decouples the prime channel (§4, "Status: **open**").

Borrow. (i) The inner-channel counting device (Theorem 1): zero density = total winding of the inner channels, error < |d|.
(ii) The S-part detector as an RH-false test: DH's S-truncations carry an off-line zero converging to DH's own (distance 0.193 at X = 7, 0.0081 at X = 10⁴;
`ly/NOTE.md` §5). (iii) Nakamura's f(s, χ) as a control for any test that consumes only the functional equation.

Close (K), carried by Theorem K (`ly/NOTE.md` §2): "*Setting.* U := {|Re t| < 14.2, |Im t| < ½}. f_k(t) := P_k(v(½ + it)), where P_k is Lee–Yang in the prime
channels p^{1/2−s} (p ∈ S_k finite), optionally with one extra archimedean channel Θ_k(s) of degree ≤ 1 (any meromorphic inner function). h_k is holomorphic
and zero-free on U. *Claim.* h_k·f_k does not converge uniformly on compact subsets of U to Ξ." Re-derived and re-run by an independent method (40 Haar-random
U, `ly/verify-F/rerun_theoremK.log`: "**CONFIRMED**"). Status (`ly/read-F.md` §4): Theorem 1, Corollary 2, Theorem K, Propositions 3–4, Lemma F "dual-model
(Opus writer + this read)"; novelty of the application to Ξ "single-check (Opus) … not for external use without the second check". Open edge: several coupled
slow archimedean channels (`ly/NOTE.md` §8), priority "LOW unless a rung-1 model appears" (`ly/read-F.md` §3(b)).

### A.2 N2 `staircase` — real-rootedness chains from Riemann's incomplete-gamma series. Close (K), UPHELD (`st/read-F.md`: "AGREES-WITH-CORRECTIONS"; F1–F5 applied in `st/NOTE.md`, pre-read copy `st/NOTE.pre-reader.md`).

Three most useful findings.
1. Theorem A, `st/NOTE.md` §2: "Let w ≢ 0, and either (i) 0 ≤ w_n ≤ 1 with some w_m < 1 (covers C1 for every N, C2 for every finite S, every smooth cutoff
   with 0 ≤ φ ≤ 1), or (ii) w finitely supported with arbitrary real values. Then ξ_w has only finitely many zeros on Re s = ½ and infinitely many zeros off
   it." With Theorem B ("If every zero of ξ_w lies on Re s = ½, then w ≡ 1").
2. Haglund's Conjecture 1 (arXiv:0910.5228, open since 2009, implies RH) is FALSE at N = 27: off-line zero 0.8152587993782148453823 + 3143.220682421536585287
   i below real zeros t = 3144.8946…, 3145.5998… (`st/NOTE.md` §4 item 1); its C1 analogue fails at N = 24 (0.8159896243… + 2508.2839748… i). Both at heights
   where RH holds, so "monotonic zeros" is "not implied by RH: it fires on the RH-TRUE control". Certification status: §D below.
3. Proposition F (approximation staircases are height filtrations), `st/NOTE.md` §2: "**Consequence:** in any induction 'members real-rooted up to T_N ⟹ up to
   T_{N+1}', the only content is RH on the new window T_N < |Im s| ≤ T_{N+1}; … The step's missing lemma is literally 'no zero of ξ off the line with T_N < γ
   ≤ T_{N+1}'." Proposition E(b) needed the reader's paragraph F3 (`st/read-F.md` §3) to exclude zeros with Re s ≥ 2 for large N.

Most useful failure. The orchestrator's prime chain C2 never brings the Euler product to the zeros: "in the tracking window a C2 member equals Ξ + P with P >
0 of size e^{−πm²}, m the least excluded integer — the same as the C1 member N = m − 1; the Euler factor (1 − 2^{−s})^{−1} appears only in the Γ-dominated
region" (`st/NOTE.md` §10 item 4; S = {2} agrees with C1 N = 2 to 1.2e−10, §3).

Borrow. (i) The one-sided approximants (Theorems D, D′): ξ_N from above and Haglund's Ξ_N from below on the line, "two super-exponentially accurate one-sided
approximants built from finitely many incomplete gamma functions" (§2, D′(3)).
(ii) The visibility law: an off-line zero of the limit at height γ₀ enters the member only when "departure height ≈ 4(N+1)² + 8 … exceeds γ₀" (§9). (iii) The
complete-census discipline: argument-principle total, count = (Z_tot − Z_line)/2, every zero re-solved by a second formula at a second precision and
circle-counted (§3).

Close (K), carried by Theorems A and B (Z₁) with Proposition F (Z₂), the computed counterexamples (Z₃) and the axiom-level control (Z₄: "the chain's one
positivity generator (Pólya's criterion, Theorem D) holds verbatim for the RH-false positive Euler product F_{2.9,2}", `st/NOTE.md` §0). Status
(`st/read-F.md` §4): "Theorems D, D′, A, B, Proposition F: dual-model (Opus writer + this read). Proposition E: (a), (c) as corrected; (b) with the reader's
paragraph F3." The decisive computation was re-run in Arb ball arithmetic at 4800 bits from Haglund's own (10), (13), (14): "**CONFIRMED**" (`st/read-F.md`
§2).

### A.3 N3 `fingerprint` — Jacobi / Schur / Verblunsky parameters of ζ. Close (K) for the seed's mechanism (task (d)), UPHELD; "the tables stand as an instrument" (`fp/read-F.md` header).

Three most useful findings.
1. Theorem D, `fp/NOTE.md` §6, for g_{a,q}(s) = a/√q + q^{s−1/2} + q^{1/2−s}: "(ii) If |a| < 2√q (θ real), every node 1/w_k is real positive with positive
   mass: multiplication by g preserves the positivity of every fingerprint, for every Λ … (iii) If |a| > 2√q … its fingerprint fails at a finite index for
   EVERY Λ … (iv) (Euler factors) a = −(p + 1): |a| − 2√p = (√p − 1)² > 0 for every p > 1 … Multiplying or dividing ξ by one Euler factor never preserves
   positivity; the fingerprint has no prime-by-prime positivity induction." Scope (`fp/read-F.md` §3(a)): (i)–(iii) are "one step from (E1)"; the value is the
   exact one-prime boundary |a| ≤ 2√q.
2. Proposition M (Hermite–Krein count), `fp/NOTE.md` §5: the Hankel form has exactly J negative squares when J off-line pairs are resolved, "so generically
   (non-adjacent flips) **#{n: b_n² < 0} = 2J**"; on Davenport–Heilbronn the "−+−" motifs sit one per off-line zero with t ≤ 241 ("The fingerprint is a
   spectral MAP of the off-line zeros"). DH map single-producer (`fp/read-F.md` §3(b)).
3. Visibility without early warning, `fp/NOTE.md` §5: n_fail ≈ n_WKB(T) + lag, lag logarithmic in 1/δ, at ≈ 6 digits per index; "Below its resolution index an
   off-line pair is indistinguishable from an on-line pair split by ±δ … There is no early warning: the IV.9 'deceptive' regime, measured." Li's λ_n need n ~
   T²/δ (≈ 3×10⁵ for DH's first zero; DH's λ_1..λ_601 all positive).

Most useful failure. The mining task found no arithmetic: the fingerprint carries the explicit formula's prime lines (log 2, 3, 4, 5) through a low-pass
transfer plus a combination tone at log(3/2); "No prime structure appears that is not already in the zeros; the fingerprint is not an arithmetic coordinate
system" (`fp/NOTE.md` §7). PSLQ at 300 digits: "no relation" (§8); the leading term of the asymptotic law "carries no arithmetic beyond the density
(conductor)" (§4).

Borrow. (i) The fingerprint as the wave's common certified diagnostic for RH-true approximation schemes: "a member with a motif is a certified counterexample
to that scheme's conjecture, with its height read off from t_n" (`fp/NOTE.md` §11). (ii) Uvarov bookkeeping: s_m(Λg) = s_m(Λ) + Σ_k w_k^{−m} (Theorem D(i))
prices any finite multiplier exactly. (iii) The injection method (ζ plus one off-line quadruple, exact in the moments) for measuring any detector's visibility
threshold (§5).

Close (K), carried by Theorem D ("Z (the proved statement): Theorem D", `fp/NOTE.md` §0). Re-run with independent code and library (mpmath at 60 digits
against the writer's Arb at 24 000 bits): "**CONFIRMED**" (`fp/read-F.md` §2). Status (`fp/read-F.md` §4): "Theorem D, Propositions S and M: dual-model at the
level read (Opus writer + this read; Proposition S's Szegő relations are [recalled] by the writer and numerically checked by the writer only)." Conjecture W
is "Instrument-level, not load-bearing anywhere" (`fp/read-F.md` §3(c)). Disguise audit: the fingerprint positivity "IS Weil positivity with multiplier 1 … It
is a re-dress, not a generator (S4 fails)" (`fp/NOTE.md` §0).

### A.4 N4 `tournament` — 35 mechanisms run to a brief-time verdict. Close (N), UPHELD: "nothing survives, correctly" (`tn/read-F.md` header).

Three most useful findings.
1. DD1, `tn/NOTE.md` §2.1: pointwise Λ ≥ 0 separates all three computed RH-false controls — Epstein x² + 5y² first fails at n = 36 (Λ(36) = −2 log 36), DH at
   n = 3, every F_{a,q} at q², by the derived identity "Λ_F(q²)/log q = 1 − (α² + β²) = 1 − a² + 2q < 1 − 2q < 0"; Euler-product controls give no negative
   value to 2·10⁵. Re-run: "**CONFIRMED**" (`tn/read-F.md` §2).
2. The rung-1 twin, `tn/NOTE.md` §2.1: the virtual curve Z(u) = (1 − 5u + 5u²)/((1 − u)(1 − 5u)) over F₅ "is an Euler product with Λ ≥ 0, rational, with FE;
   its zeros sit at σ = 0.79899 and 0.20101"; so "the function-field analog of 𝒫 therefore does NOT imply RH". The reader's rule: "a mechanism the virtual
   curve passes cannot be the generator" (`tn/read-F.md` §3).
3. The synthesis, `tn/NOTE.md` §4: "Four ways to die" — (a) local objects own zeros or own none, (b) finiteness hypotheses fail exactly on the line, (c)
   hypotheses satisfied by an RH-false world, (d) wrong output type — and "Every EQUIV row, stripped of its failed generator, is Weil/Li/Lagarias positivity
   with multiplier 1." Carried into §B and §F below.

Most useful failure. DD2, the Krein–Langer Pick kernel on a disk in Re s > 1 (`tn/NOTE.md` §2.2): it decides RH exactly in principle and flags DH with exactly
one negative square, but "the negative square, global in principle, is exponentially local in practice: ≈ 6 digits per unit of height offset … no gain over
Turing-method verification". Lesson carried as survivor property (3): the transport from Re s > 1 inward "must be a theorem, not a computation" (§4).

Borrow. (i) Λ ≥ 0 as a one-line axiom screen: any mechanism whose inputs DH, F_{a,q} and Epstein all satisfy is I.1-blind.
(ii) The rung-1 twin test (virtual curve (q, a) = (5, 5)) as a mandatory control, now adopted in `results/novel-wave-s37/WAVE-CHARTER.md` §0 (e). (iii) The
labeling rule for the table (§C.3 below): rows resting on `[recalled, unverified]` statements are "screened at brief time" only.

Close (N), carried by the table (`tn/NOTE.md` §3: "35 rows: 26 DEAD, 9 EQUIV, 0 OPEN") and the three deep dives. The one self-contained new proof in the table
is the T6 lemma, re-derived by the reader: "an infinitely divisible law with all exponential moments has an n-th convolution root with the same property for
every n, so φ = φ_n^n with φ_n entire; the order of any zero of φ is divisible by every n, hence there is none. ✓ So the tilted Riemann kernel Φ(u)e^{εu} is
never infinitely divisible, whatever the truth of RH" (`tn/read-F.md` §1). "The zoo gains exactly two things from this seed: the control 'virtual curve over
F₅' … and the T6 lemma" (`tn/read-F.md` §3). Deep-dive probability estimates, as the writer gave them: DD1 "< 0.5%", DD2 "< 0.5%", DD3 "< 0.3%".

## §B Cross-seed structure — what the four closes have in common (propositions with pointers; each is the sources' statement)

B1 (the density is archimedean). ξ's zero density "is purely archimedean: (1/2π)·log(t/2π)", while inner prime channels "add zero density ⟨d, log p⟩/2π ≥
   |d|·log 2/2π at every height, with error at most |d|" (`ly/NOTE.md` §0; Theorem 1, Corollary 2); a prime part of weight W "can only 'switch on' above
   height 2π·e^W" (Proposition 4). The reader's sharpening (`ly/read-F.md` §3(a)): "the primes must enter with ZERO net winding — as a phase arg ζ(½+it) =
   πS(t) that is a boundary value of log of an OUTER function on Re s > ½ … 'Primes in the outer part' is therefore not a design choice but a restatement of
   RH; the design problem is to find a positivity generator that FORCES outerness." Same fact from N4: "ξ's zeros are collective: archimedean density plus a
   bounded prime correction; no prime owns one" (`tn/NOTE.md` §4(a)); from N2: the C2 Euler factor acts "only in the Γ-dominated region Re s ≳ σ_c(t), where
   the zeros are already off the line" (`st/NOTE.md` §10 item 4).
B2 (one single-prime obstruction, two coordinate systems). Lee–Yang coordinates: the local factor "1 + (a/√q)z + z², Lee–Yang exactly when a ≤ 2√q"
   (`ly/NOTE.md` §5), the conductor-q² family "crossing the RH boundary at b = 2√q" (§6 (2)). Fingerprint coordinates: positivity preserved for every input
   iff |a| ≤ 2√q, destroyed for every input when |a| > 2√q (`fp/NOTE.md` §6, Theorem D(ii)–(iii)); ζ's factor "misses the Lee–Yang class by the AM–GM gap (√p
   − 1)². This is the precise single-prime obstruction for seed N1" (`fp/NOTE.md` §11). The reader: "ONE single-prime obstruction seen in two coordinate
   systems" (`fp/read-F.md` §3(a)). Both sides of the boundary are dead: "Anything built prime by prime either carries zeros periodically at every height (T2,
   T5, T16; N1 Theorem K …) or carries them at Re s ∈ {0, 1} (T3; N3 Theorem D)" (`tn/NOTE.md` §4(a)).
B3 (approximation staircases are height filtrations). N2 Proposition F: the induction step's "missing lemma is literally 'no zero of ξ off the line with T_N <
   γ ≤ T_{N+1}'" (`st/NOTE.md` §2). The same shape elsewhere: N1's receding threshold 2π·e^W (Proposition 4); N3's index–height dictionary t_n ≈ 2n/W(qn/2π),
   failure at n_WKB(T) + lag (`fp/NOTE.md` §4, §5); N4 T29 "DEAD — filtration; axiom-blind" (`tn/NOTE.md` §3).
B4 (no early warning). "There is no early warning: the IV.9 'deceptive' regime, measured" (`fp/NOTE.md` §5); the staircase controls break "exactly when the
   member's window first covers the limit's off-line zero (visibility), and nothing earlier" (`st/NOTE.md` §5); the Krein–Langer kernel sees an off-line zero
   "only within ≈ 10 units of height at 60–90 digits" (`tn/NOTE.md` §2.2); the exact squeeze only at "X ≳ |ρ|^{1/δ}" (§2.3).
B5 (approximants of an RH-true function are not RH-true). ξ₂₄ and Haglund's Ξ₂₇ have in-strip off-line zeros "at heights where the limit has none … false
   positives of the same shape as the controls' true off-line zeros" (`st/NOTE.md` §9); N1's analytic archimedean models A(s) + χ(s)A(1−s) acquire off-line
   zeros "exactly when min_I φ′ < 0" (`ly/NOTE.md` §3).
B6 (what survives the controls is a re-dress). The fingerprint is "Weil positivity with multiplier 1" (`fp/NOTE.md` §0); "Every EQUIV row, stripped of its
   failed generator, is Weil/Li/Lagarias positivity with multiplier 1" (`tn/NOTE.md` §4); the Taylor–Lagarias chain's HB invariant "IS the zero-free region"
   (`st/NOTE.md` §9); the Hamburger acceptance test "collapses to Hilbert–Pólya plus a converse theorem" (`ly/NOTE.md` §6 (4)).
B7 (the Euler product enters as an axiom filter, never as a generator). N1 passes zoo I.1 "at the axiom level" but is "blind to ζ's zeros" (`ly/NOTE.md` §5);
   N2's generator "holds verbatim for the RH-false positive Euler product F_{2.9,2}" (`st/NOTE.md` §0 Z₄); N3: "S1: no Euler-product input is consumed"
   (`fp/NOTE.md` §9); N4: Λ ≥ 0 separates the three controls over Q, but the virtual curve has "Euler product, Λ ≥ 0, FE and rationality and violates RH"
   (`tn/NOTE.md` §4 (4)).

## §C Controls gained or corrected

C1 F_{a,q}(s) = ζ(s)(1 + a q^{−s} + q^{1−2s}), corrected range **2√q < a < q + 1**. "With a = q + 1 the factor splits as (1 + q^{−s}) (1 + q^{1−s}) and the
   off-line zeros sit exactly on Re s = 0, 1 … a must lie strictly between 2√q and q + 1 for zeros inside the strip; used here: a = 2.9, q = 2, zeros at Re s
   = 0.8238766801660445817, t = (2j+1)·4.5323601418271938096" (`st/NOTE.md` §10 item 2). Certified by: FE exact to ≤ 1.2e−30 and the zero table ((3,2): σ = 1
   and 0; (5,5): 0.79899; (2.9,2): 0.82388; (4.5,5): 0.56932) in `tn/verify/faq_control.log` (`tn/SHARED.md` block 2); the axiom it breaks, "Λ_F(q²)/log q = 1
   − a² + 2q < 1 − 2q < 0", re-derived in `tn/read-F.md` §1 and re-run in `tn/verify-F/rerun_dd1.log`; Ramanujan at q (`ly/NOTE.md` §5). Labeling note: the
   runs at (a, q) = (3, 2) — `fp/NOTE.md` §5–§6 (F_{3,2}), `ly/NOTE.md` §5, `tn/read-F.md` §2 — sit at the boundary a = q + 1 (zeros on Re s = 0, 1, not
   inside the strip); they remain RH-false, but the in-strip instance is F_{2.9,2}.
C2 The virtual curve over F₅ (the rung-1 twin): Z(u) = (1 − 5u + 5u²)/((1 − u)(1 − 5u)), (q, a) = (5, 5), "the exact twin of the control F_{5,5}"
   (`tn/NOTE.md` §2.1). Certified by: `tn/verify/dd1_rung1_virtual.log` (exact integers, d ≤ 40) and the reader's re-run `tn/verify-F/rerun_dd1.log` ("N_n ≥ 1
   and b_d ≥ 0, integers, for all d ≤ 60 … functional equation residual 3e−16; zeros at σ = 0.79899, 0.20101"); hand derivation `tn/read-F.md` §1 (DD1). Rule:
   "a mechanism the virtual curve passes cannot be the generator" (`tn/read-F.md` §3). Consistency: the fingerprint (an instrument, not a generator) fails on
   N3's "fake curves" (Hasse broken, c1 = 5, 6, 9 over F₅) at α_1 (`fp/NOTE.md` §6).
C3 The labeling rule of `tn/read-F.md` §3: "The 35 verdicts are BRIEF-TIME verdicts (zoo §0 protocol), not zoo entries. Rows whose kill or equivalence rests
   on a statement the writer labeled `[recalled, unverified]` — T4 (Schoenberg), T10 and T12 (the Euler-product-convergence equivalence), T13, T17, T19, T23,
   T26, T28, T29, T30, T32, T33 — may be cited as 'screened at brief time' only; re-proposing one of them requires reading its recalled source first (standing
   order 5). Rows with proofs on the page or resting on program theorems: T1, T2, T3, T5, T6, T15, T16, T18, T21, T34, T35."
C4 Further controls on disk. Nakamura's f(s, χ), χ cubic mod 7: Riemann's FE to 1.0·10⁻³⁰ and 31 off-line zeros with 0 < t < 45 — the RH-false control for any
   test that consumes only the FE and a lattice support (`ly/NOTE.md` §6 (2), `ly/verify/f_hamburger_checks.log`). Epstein x² + 5y²: Λ(36) = −2 log 36, re-run
   (`tn/verify-F/rerun_dd1.log`). DH's S-truncations converge to its off-line zero (distance 0.0081 at X = 10⁴; `ly/verify/e_controls.log`). The DH staircase
   breaks at N = 9, when its window (≈ 96.8) first covers 85.7 (`st/verify/violation_DH_N9_84.json`).

## §D Instruments gained — rows ready to append (column shape of every `directions/*.md` "Instruments" table; files not edited)

Paths are relative to `results/`. Status words are the sources'. Target file named above each block.

→ `directions/D1-certified-refutation-arm.md`

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| Haglund's Conjecture 1 (arXiv:0910.5228 p. 3; implies RH) at N = 27 — interval certificate | FALSE. Producer A (Arb balls): (H1) real zero x₁ ∈ (3144.8946, 3144.8947); (H2) winding number k = 1 of Ξ₂₇ on the square c + [−r, r]², c = 3143.2206824215 + 0.3152587994 i, smallest r = 4·10⁻¹¹; (H3) Conjecture 1 and the weak form (Remark 1) false; (H4) second real zero in (3145.5998, 3145.5999). Trust base: FLINT/Arb, Lemmas B, Γ, T and the half-plane lemma proved in CERT §3, identity (12) read on disk. SINGLE-PRODUCER: Producer B (no Arb) owed by BRIEF §3; novelty single-check until the reader's own search is recorded (`novel-wave-s36/staircase/read-F.md` §4) | `haglund-cert-s37/producer-A/CERT.md` §1–§6 (SHA-256 b1ecfe0a… in `producer-A/SHARED.md`); `novel-wave-s36/staircase/NOTE.md` §4 item 1; `staircase/verify-F/rerun_N27.log` | 2026-09-30 |
| Ordering invariant for the seed chain ξ₂₄ (C1 analogue of Conjecture 1) | FAILS: zero with Re ρ ≥ 0.8159896242 > ½, Im ρ ≤ 2508.2839748054 (winding k = 1 at r = 1e−10) below on-line zeros in (2510.2026, 2510.2027) and (2510.7086, 2510.7087). Route T "rests on Riemann's identity" (Jacobi's theta relation not re-proved in the CERT); single-producer | `haglund-cert-s37/producer-A/CERT.md` §8 (H5); `novel-wave-s36/staircase/NOTE.md` §4 | 2026-09-30 |
| Certified ζ fingerprint tables | s_1..s_1000, S-fraction α_1..α_999 of Σ_{γ>0} 1/(γ² − w) "ALL certified positive (Arb, ≥ 1192 certified digits at n = 999)"; det(s_{i+j+1})_{n×n} > 0 for n ≤ 500; λ_1..λ_1001 certified; Verblunsky α_0..α_999 verified, all \|α_n\| < 1; zeros route (30 001 Arb zeros + tail) agrees to 1e−11..1e−34. SINGLE-PRODUCER beyond α_1..α_8 (re-derived by the reader) | `novel-wave-s36/fingerprint/tables/zeta_real_P24000_S1000.json`, `zeta_circle_P24000_S1000.json`; NOTE §3; `fingerprint/read-F.md` §2, §3(b) | 2026-09-30 |
| Off-line-pair counter (Proposition M: #{n: b_n² < 0} = 2J generically; "−+−" S-motifs) on Davenport–Heilbronn | negative S-indices {148,150, 217,219, 351,353, 372,374, 539,541} up to 599 = five off-line zeros with t ≤ 241, each motif where t_n first exceeds the zero's height (lag ≤ 6). SINGLE-PRODUCER: "Before the counter is used as a program instrument or cited: a second producer for the DH run (KICKSTART 10(j))" | `novel-wave-s36/fingerprint/tables/dh_real_P16000_S600.json`; `fingerprint/verify/u5b_dh_offline.py`; NOTE §5; `fingerprint/read-F.md` §3(b) | 2026-09-30 |
| Visibility price of the fingerprint (ζ + one injected off-line quadruple) | n_fail ≈ n_WKB(T) + lag; lag 7–28 at δ = 0.3, growing logarithmically in 1/δ; ≈ 6 digits per index (1430 digits at n = 519); Li's λ_n need n ~ (T²/δ)log(T²/δ). Single-producer | `novel-wave-s36/fingerprint/verify/u5d_inject_table.json`; NOTE §5 | 2026-09-30 |
| Interval certificates for the first staircase member ξ₁ | (R1) ξ₁(½ + it) ≥ 2.9e−7 > 0 for every t ≥ 30; (R4) exactly one zero in the square of half-width 1e−8 centred at 5.165902026924569091939 + 22.91546577056082331413 i. The two cited remainder bounds (Euler–Maclaurin, Stirling) are "the only unread ingredients"; (R2)/(R3) not run | `novel-wave-s36/staircase/verify/rigor_xi1.py`, `rigor_xi1_*.json`; NOTE §6 | 2026-09-30 |

→ `directions/B3-arithmetic-debranges.md`

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| Counting along inner channels (N1 Theorem 1; Kronecker case = Alon–Vinzant Thm 1.9) | \|N_F(t₁, t₂) − (1/2π)Σ_j d_j\|Δ arg v_j\|\| < \|d\|; a prime-variable restriction has a zero in every interval longer than 2π/log 2 = 9.06472; worst \|N − WL/2π\|/\|d\| = 0.785 over 40 Haar-random couplings (reader's re-run). Dual-model | `novel-wave-s36/ly-infinity/NOTE.md` §2; `ly-infinity/verify/k1_gap_theorem.log`; `ly-infinity/verify-F/rerun_theoremK.log` | 2026-09-30 |
| Ξ's zero-free central box (the one numerical input of Theorem K) | argument principle for ξ on [−0.5, 1.5] × [−14.1, 14.1]: −1.5·10⁻³⁰; nzeros(14.1) = 0, nzeros(14.2) = 1, nzeros(21.0) = 1, nzeros(21.1) = 2 | `novel-wave-s36/ly-infinity/verify/k1_xi_lowzeros.log` | 2026-09-30 |
| Natural Hermite–Biehler split ξ = A + A♯, A(s) = ¼ + ½s(s−1)Σ_n X^{−s/2}Γ(s/2, X) | min \|A\|/\|A♯\| − 1 = −0.955 (grid ½ < Re s ≤ 3); A has 49 zeros in Re s > ½ below 200, lowest 2.80769690200782731 + 5.87093395263593058 i; negative at every level N = 1, 2, 3, 5 and in the limit. Writer's run, not re-run by the reader | `novel-wave-s36/staircase/verify/natural_split.json`; `staircase/NOTE.md` §4 item 3 | 2026-09-30 |
| Taylor–Lagarias chain F_h = ξ(s + h) + ξ(s − h), window [80.3, 91.7] | ζ: real-rooted for every h ∈ {0, 0.02, …, 1}, grid HB margin ≈ 0.156·h; DH: real-rootedness threshold h* ∈ (0.28, 0.30] against the zero-free-region threshold δ = 0.3085 ("a re-dress", NOTE §9). Writer's run | `novel-wave-s36/staircase/verify/taylor_chain.json`; `staircase/NOTE.md` §4 item 5 | 2026-09-30 |

→ `directions/C2-rigidity-conservation.md`

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| Λ-sign screen of the RH-false controls (DD1) | first Λ_F(n) < 0: Epstein x² + 5y² at n = 36 (Λ(36) = −2 log 36; 2604 negatives ≤ 2·10⁵; h = 3, 4 forms fail too); DH at n = 3; F_{a,q} at q² (Λ_F(q²)/log q = 1 − a² + 2q); Euler-product controls: none to 2·10⁵. Re-run "CONFIRMED" | `novel-wave-s36/tournament/verify/dd1_lambda_sign.log`; `tournament/verify-F/rerun_dd1.log`; `tournament/NOTE.md` §2.1 | 2026-09-30 |

→ `directions/B2-refutation-program.md` (visibility prices of three detectors; writer's runs, not re-run by the readers)

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| Krein–Langer Pick kernel on a disk in Re s > 1 (DD2) | DH at its zero's height: exactly one negative eigenvalue (−0.051, −0.102, −0.153 for n = 12, 24, 36); ζ: none below −10⁻⁵⁵·max; log₁₀(−min/max) = −2.9, −4.7, −10.6, −24.4, −40.5, −58.3 at height offset D = 0, 1, 2.5, 5, 7.5, 10 (r = 0.3): ≈ 6 digits per unit of height | `novel-wave-s36/tournament/verify/dd2_pick_kernel.log`, `dd2_visibility.log`; NOTE §2.2 | 2026-09-30 |
| Exact squeeze D₁ = ∫(ψ − x)²x^{−s−1}dx to X = 10⁷ (DD3) | F_{2.9,2}: abscissa 2Θ_F = 1.648 legible from X = 10⁴; DH: off-line term visible only for X ≳ \|ρ\|^{1/δ} ≈ 10^{6.3} | `novel-wave-s36/tournament/verify/dd3_landau_squeeze.log`; NOTE §2.3 | 2026-09-30 |
| Staircase departure law (C1, ζ normalization) | departure height ≈ 4(N+1)² + 6…10 (first failing lobe, N = 1…7); an off-line zero of the limit at γ₀ enters the member only above it (DH chain: N = 9 for 85.7) | `novel-wave-s36/staircase/NOTE.md` §3, §9; `staircase/verify/lobes_T320.log` | 2026-09-30 |

Owed before any row above is cited outside the program: the second producer named in its row (KICKSTART 10(j)); a producer-B `CERT.md` for `haglund-cert-s37`
appeared on disk at 23:07 during this consolidation and was NOT read here (not an input).

## §E Errata of the orchestrator's Session-36 seeds established by the wave (one line each; the source holds the argument)

Charter, rule 2 (the F_{a,q} control): "a > 2√q" must be 2√q < a < q + 1 for in-strip zeros; a = q + 1 puts them on Re s = 0, 1 (`st/NOTE.md` §10 item 2; §C1).
N1-E1: for product type the Lee–Yang lift adds nothing — "a product of one-variable Hermite–Biehler factors is Hermite–Biehler" (`ly/NOTE.md` §1).
N1-E2: the seed's A = Π(1 − p^{−1/2−it}) is anti-aligned with ζ (worse than no primes); the aligned choice is Π(1 + p^{−s}) — "the orchestrator's error stands recorded" (`ly/read-F.md` §1).
N1-E3: "the product form is exactly where the Euler product enters" is half right: it needs Euler product plus Ramanujan and is blind to the values log p and to ζ's zeros (`ly/NOTE.md` §1).
N1-E4: the change of variables is legitimate but the torus line carries the wrong density law, constant ⟨d, ℓ⟩/2π instead of (1/2π)log(t/2π) (`ly/NOTE.md` §1).
N1-E5: "the zeros of ζ (if on the line) form a Fourier quasicrystal" is false as stated (Kurasov–Sarnak p. 1 on Guinand); the archimedean-phase variant is Gonek's non-analytic ζ_X (`ly/NOTE.md` §1 E5).
N1-E6/E7: the convergence statement is true but empty (Theorem K) or tautological (Proposition 3); the operative obstruction is the coefficient-independent density, not "the divergence of Σ p^{−1}" (`ly/NOTE.md` §1).
N2-1: Haglund proved only "Conjecture 1 implies RH" and conjectured MONOTONIC ZEROS, not real-rootedness; nothing is proved for N = 1; his Ξ_N = ξ_N − c_N is not the seed's truncation (`st/NOTE.md` §10 item 1).
N2-3: "Chains exist whose first step is a THEOREM" — for the incomplete-gamma chains no member is real-rooted (Theorem A), so there is no first step (`st/NOTE.md` §10 item 3).
N2-4: the prime chain C2's multiplicative index set "does not act where the zeros are" (`st/NOTE.md` §10 item 4); the S-smooth incomplete-gamma series is in print for L(s, χ) and modular L-functions; the literal ζ-form not found [novelty: single-check] (§7).
N3-E-1/E-2: the Stieltjes identity holds for γ > 0 only (twice that over all γ); the Hankel determinants must start at s_1, since s_0 = ∞ (`fp/NOTE.md` §1).
N3-E-3: the measure Σ_ρ δ_{1−1/ρ} is infinite; the Carathéodory function is 2ξ′/ξ(1/(1 − z)), with Herglotz measure σ = Σ_ρ |ρ|^{−2}δ_{z_ρ} (`fp/NOTE.md` §1).
N3-E-4: "RH ⟺ all |γ_n| ≤ 1" must be strict, |α_n| < 1 (|α_n| = 1 means finite support) (`fp/NOTE.md` §1).
N3-E-5: a genus-g curve over F_q does NOT have a terminating J-fraction in the seed's variable (299 positive coefficients computed); what terminates is the Frobenius-variable measure (`fp/NOTE.md` §1).
N3-E-6/E-7: the Jacobi and Schur families are one object (Proposition S); "no closed form" holds only in the non-trivial sense — each α_n is rational in s_1..s_{n+1} (`fp/NOTE.md` §1).
N3 task (d): the hoped-for "Christoffel/Geronimus-type" Euler-factor step is an infinite Uvarov step on the destroying side of the Hasse bound — the kill itself (`fp/NOTE.md` §6).
N4 seed (Deligne's squeeze on the Proposition-B regrading): "DEAD — regraded 'RH' free; Theorem S" (`tn/NOTE.md` §3 row T21).
Beyond the seeds (Session-37 briefs): the tail sketch of `haglund-cert-s37/BRIEF.md` §2 holds only for β ≥ 1 (CERT §3.2, §7(a)); the orchestrator's first Arb script had the `gamma_upper` argument order backwards (BRIEF §3).
Against the prior art (Haglund, arXiv:0910.5228): the 1/x² coefficient is negative for every N (not "positive for k ≥ 3", p. 10); the N = 4 table entry is 31, not 32; Conjecture 1 is false at N = 27 (`st/NOTE.md` §7).

## §F The filter for the next wave

Survivor properties, as adopted (`tn/NOTE.md` §4, "What a survivor must have", with `tn/read-F.md` §4 and `ly/read-F.md` §3(a)):
(1) "It consumes pointwise Λ ≥ 0 *jointly* with the FE". (2) "It is global: primes move zeros without owning them" — sharpened by `ly/read-F.md` §3(a): the
primes enter with zero net winding, and the task is "a positivity generator that FORCES outerness". (3) "It survives divergent prime mass on the line with a
renormalization that is not Weil's — or it works where the mass is finite (Re s > 1) and transports the result inward … the transport itself must be a
theorem, not a computation". (4) "It fails at rung 1 on a single curve", split by the reader: "(4a) On rung 1 the input the virtual curve lacks is GEOMETRIC
(a surface with an index theorem; a family with monodromy) … (4b) Over Z, Hamburger's rigidity … supplies uniqueness, not an extra object."
Already funded from this filter (Session 37, `results/novel-wave-s37/WAVE-CHARTER.md`): M1a `beurling-fe`, M1b `beurling-frontier`, M2 `proof-mine` — not
Untried. Not to be re-proposed: the staircase Conjecture S_κ ("a height filtration of RH — it carries no mechanism", `st/NOTE.md` §8), the ACV class
(Proposition 3), the fingerprint as a route (`fp/NOTE.md` §0).

Untried entries the wave suggests (format of the direction files' "Untried" lists; the fit reasons are this digest's reading of the cited lines, not new
claims):
- **Extremal characterization of ξ** (`tn/read-F.md` §4 (4b), "Recorded for the funding decision, not claimed"): a variational problem with an FE-type
  constraint whose unique extremal is ξ (uniqueness by a Hamburger-type argument) and whose second variation there is a form in the zeros. Fit: S4 (the second
  variation is the generator); S1 through FE rigidity on the integer lattice (Nakamura's f(s, χ) is the control that the lattice condition excludes,
  `ly/NOTE.md` §6 (2)). First rung: the function-field analog over F₅ — the virtual curve (5, 5) must fail it and a genuine curve with |a| ≤ 2√5 must pass
  (§C2). Target: `directions/C2-rigidity-conservation.md`.
- **A generator that forces outerness of ζ(s)(s − 1) on Re s > ½** (`ly/read-F.md` §3(a)). Fit: S2 (one off-line zero is one inner factor, so outerness fails
  at a single zero); S4 required by construction; S1 open (must fail on DH and on F_{2.9,2}). First rung: curves over F_q, where the input that forces RH is
  geometric (`tn/read-F.md` §4 (4a)). Pointer: "Connes–Consani, Quasi-inner functions and local factors — not on the record; read before any return to
  inner-function models". Target: `directions/B3-arithmetic-debranges.md`.
- **The coupling frontier of N1** (`ly/NOTE.md` §8): prove N_F(I) ≥ (W_prime(I) − Σ_j W_{a_j}(I))/2π − 1 for det(I − V(s)U), or construct an evading U with k
  ≥ 4 slow archimedean channels. Fit: S1 at the axiom level only (Euler product plus Ramanujan, `ly/NOTE.md` §5); a no-go extension, not a mechanism. Priority
  "LOW unless a rung-1 model appears" (`ly/read-F.md` §3(b)). First rung: "function fields, where Lemma F is exact" (`ly/NOTE.md` §8). Same Connes–Consani
  pointer. Target: B3.
- **Krein–Langer transport as a theorem (lemma L2)** (`tn/NOTE.md` §2.2): K = K_arch + K_prime on a disk in Re s > 1 with K_arch − (negative part of K_prime)
  PSD. Fit: S2, S3 (negative squares count off-line pairs); S1 via Λ ≥ 0; S4 if L2 holds. First rung: the virtual curve's kernel, which "has a negative
  square, and its prime part satisfies Λ ≥ 0" — name the extra input first. Target: C2.
- **The fingerprint as the wave's common certified diagnostic** (`fp/NOTE.md` §11). Fit: S2, S3 yes, S4 no (`fp/NOTE.md` §9): an instrument entry. First rung:
  a second producer for the DH map (`fp/read-F.md` §3(b)); then the censused members ξ_N, N = 1–5, whose off-line zeros are known completely (`st/NOTE.md`
  §3), as known answers. Target: `directions/D1-certified-refutation-arm.md`.
- **Conjecture W and the low-pass transfer as theorems** (`fp/NOTE.md` §11, "Secondary (mathematics, not RH)"). Fit: none of S1–S5 (instrument theory). First
  rung: the exactly solvable toys (sin, Bessel) where α_n is known in closed form (`fp/NOTE.md` §4).

## §G What was spent for nothing, by cause (KICKSTART 10(o), labels of 10(m); from the four `SHARED.md` files)

Spent on the wrong thing. (a) The seed's task N2(d) asked for a computer-assisted proof of real-rootedness of members that are not real-rooted (Theorem A;
`st/NOTE.md` §6, "asks for something false"), replaced by certificates about ξ₁ — cause: seed erratum N2-3. (b) The first N4 agent "died emitting > 128k
output in one response"; the replacement rebuilt from SHARED (`tn/SHARED.md` block 3) — cause (ii) tool: the ≤ 6 kB per-write rule was the missing input (now
in the Session-37 briefs).
(ii) Budget/tool/time — re-queued or recorded, missing input named. N1: 4th alignment height (T* ≈ 3.2·10⁶) and 4th inverse-design configuration stopped by
the 10-minute rule (`ly/SHARED.md` units 3, 6). N2: DH N = 9 whole-box quadtree stalled and was stopped (the zero was found directly; unit 17); fixed queues
killed for `runner.sh` (unit 8); F_{2.9,2} runs restarted after the near-line locator band (unit 17); unrun at close: dense Haglund scan N = 31–39, Haglund
census N = 1–3, 5, 6, DH N = 8, 11, rigor R2 (`st/verify/jobs.txt`, unit 22). N3: primes run 1 INVALID (Gauss–Laguerre tail to t ≈ T·e^230, Lanczos underflow;
unit 5f); DH circle at 24 000 bits non-finite, re-run at 16 000; bugs fixed in-run (15-digit zero parse, a missing Jacobian e^v, 53-bit constants; unit 3);
the plain discretized Stieltjes procedure (O(1) errors by n = 50) replaced by Lanczos with reorthogonalization.
(iii) Unexplained or recall errors. N3: a recalled DH zero (0.646008 + 240.935500i) "did not reproduce" (`fp/NOTE.md` §5). N1: the Cayley-factor bound 2
arcsin corrected to 2 arctan (first unstable S₂ is {2, 3, 7}; `ly/SHARED.md` unit 3); a page citation corrected.
Record-keeping. Estimated SHARED timestamps later corrected in N2 (units 1–4) and N3 (three blocks) — and in this digest's own log.
Found nothing, correctly (not waste): N4's 35 rows and DD1–DD3; N1's inverse design (parameter counting, `ly/NOTE.md` §4); N3's PSLQ null (§8); N2's natural
HB split and Taylor–Lagarias chain (§4).
Candidate LOG line: "Spent for nothing: N2 task (d) (false target, seed erratum), the first N4 agent run (> 128k output), N3 primes run 1 (tail underflow), N2
DH N = 9 quadtree (stall), N1's two 10-minute-rule stops, because (ii) tool/budget except N2(d) (wrong thing)."

