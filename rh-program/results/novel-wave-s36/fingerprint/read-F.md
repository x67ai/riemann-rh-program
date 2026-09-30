# read-F — the orchestrator's read at the line of `NOTE.md` (seed N3 `fingerprint`)

Reader: Fable 5.1 (the orchestrator, in person — standing orders 7, 11(c)). Session 37, 2026-09-30. NOTE read whole (345 lines).
Verdict: **AGREES. Close (K) for the seed's mechanism UPHELD; the tables stand as an instrument.** No FIX-FIRST item; two scope notes.

## 1. Re-derivations (done by the reader)

- g_{a,q}(s) = a/√q + q^{s−1/2} + q^{1/2−s} = q^{s−1/2}(1 + aq^{−s} + q^{1−2s}); (1 − p^{−s})(1 − p^{s−1}) = −p^{−1/2}g_{−(p+1),p}(s). ✓
- Theorem D (iv): cos θ = (p+1)/(2√p) ⟹ θ = iℓ/2 (e^η = √p); nodes t_k = i/2 + 2πk/ℓ, i.e. s = 0, 1 (mod 2πi/ℓ) — the Euler factor's own zeros. ✓
- Theorem D (v): Σ_k (k + iβ)^{−2} = π²/sin²(πiβ) = −π²/sinh²(πβ), β = ℓ/4π ⟹ Σ_k w_k^{−1} = −ℓ²/(4 sinh²(ℓ/4)); ~ −(log p)²p^{−1/2}·(1 + o(1)), divergent sum over p. ✓
- Proposition M, the rank/signature step: 2Re(c·L(P)²) with L = a + ib is Re(c)(a² − b²) − 2Im(c)ab, determinant −|c|² < 0: signature (1, 1). ✓
- (E1) contraction formulas checked on the data: α_1 = s_2/s_1, α_1 + α_2 = s_3/s_2 (by hand from the NOTE's s_1, s_2, s_3). ✓

## 2. The decisive computation, re-run (independent code and library)

`verify-F/rerun_theoremD.py` (+ `.log`), mpmath at 60 digits (the NOTE used Arb power series at 24 000 bits):
 s_1, s_2, s_3 of ξ from the Taylor coefficients of log ξ at ½ — equal to the NOTE's to all printed digits (s_1 = 0.02310499311541897078893);
 α_1..α_8 by an independent Viskovatov inversion — equal to the NOTE's to 20 digits (differences ≤ 4.5e−20, the NOTE's rounding);
 Theorem D at p = 2, 3, 7: lattice sum = closed form = Taylor data of log g_p (−3.96020156077126, −3.90092036348872, −3.69884529193059);
 s_1(ξg_p) = −3.937096568, −3.87781537, −3.675740299 (the NOTE's c_0 = −3.937097, −3.877815, −3.675740); α_1(ξg_p) = −4.064, −4.127, −4.357 < 0. **CONFIRMED.**

## 3. Scope notes (for the digest and the zoo line; not corrections to the NOTE)

(a) Theorem D (i)–(iii) are one step from (E1): a fingerprint is positive iff the zeros are on the line, and multiplying by g adds exactly g's zeros. What the
    theorem contributes is the identification (an infinite Uvarov step, never Christoffel/Geronimus), the AM–GM margin (√p − 1)² that places EVERY Euler
    factor of ζ on the destroying side, and (v): the coordinates diverge along the Euler product. The zoo line should be worded at that strength — "no
    intermediate object of the form ξ × (finitely many Euler factors) is RH-true" is immediate; the entry's value is the exact one-prime boundary |a| ≤ 2√q
    and its coincidence with N1's one-variable Lee–Yang boundary (NOTE §11), i.e. ONE single-prime obstruction seen in two coordinate systems.
(b) The Davenport–Heilbronn map (first negative α_148; five "−+−" motifs below n = 599) and the ζ table to n = 999 are single-producer (the writer's Arb runs).
    The reader re-derived α_1..α_8 only. Before the counter is used as a program instrument or cited: a second producer for the DH run (KICKSTART 10(j)).
(c) Conjecture W is a conjecture (WKB used backward); the reader did not re-derive the Abel inversion. Instrument-level, not load-bearing anywhere.

## 4. Status after the read

 Theorem D, Propositions S and M: dual-model at the level read (Opus writer + this read; Proposition S's Szegő relations are [recalled] by the writer and
 numerically checked by the writer only). Zoo line owed (K with a theorem; Group-IV candidate merged with N1's — the single-prime obstruction): staged for the s37 zoo stream.
