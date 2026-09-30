# SHARED — producer A (Arb / python-flint 0.6.0), unit haglund-cert-s37

## 2026-09-30 22:42 — stage 0: setup
- Read BRIEF.md (all), staircase NOTE.md §4 and §7, Haglund arXiv:0910.5228 text pp. 1–4 (defs (1), (6), (10), (12)–(14),
  Conjecture 1, Prop. 1, Remark 1, table p. 4) and the Appendix p. 15 (zeros of Ξ₁; smallest-modulus non-real zero in Q is
  20.62534600592171760132974 + 2.697151842339519632505712 i).
- Environment: /usr/bin/python3 3.9.6, python-flint 0.6.0 (Arb). caffeinate and the Session-37 watchdogs are running.
- Did NOT read producer-B/. No git commands.
- Plan: hag_core.py (routes L and T, tail bound, winding code) -> ladder.py (R1–R3) -> h1.py -> h2.py -> xcheck.py -> CERT.md.

## 2026-09-30 22:47 — stage 1: ladder R1–R3 PASSED (`ladder.py` -> `ladder.log`, 11.9 s, 256 bits)
- Code: `hag_core.py` = route L (literal (13)–(14)), route T (Xi from acb zeta/gamma minus Phi_{N+1..N+4}, tail n > N+4
  by the proved bound 2U_{M+1}), and the winding code (bisecting cover of ∂S; every piece box's enclosure certified
  in an open half-plane Re>0/Re<0/Im>0/Im<0; increments Arg(F_{k+1}/F_k) with |.| < π checked; sum/2π).
- C0: `acb(x).gamma_upper(s)` = Γ(s, x) confirmed (Γ(1,2) = e^-2, Γ(3,2) = 10e^-2, overlapping balls).
- R1: certified sign changes, BOTH routes: Ξ₁(14.04543957) ∈ +1.347060456e-11 ± 5e-75 (L) / ± 7e-47 (T),
  Ξ₁(14.04543959) ∈ −1.704102125e-11; Ξ₂(39.5324810797) ∈ +3.605517254e-21, Ξ₂(39.5324810799) ∈ −4.593418771e-21.
- R2: Ξ₁, square centre 20.62534600592171760132974 + 2.697151842339519632505712 i (Haglund App. p. 15), r = 1e-10:
  1516 pieces, total ΔArg = 6.28318530717959 ± 3.5e-15, winding = 1 (certified).
- R3: zero-free controls, same code: (a) centre shifted +0.5, r = 0.1 -> winding 0; (b) centre shifted +3e-10, r = 1e-10
  (zero 2e-10 outside) -> winding 0.

## 2026-09-30 22:48 — stage 2: H1 CERTIFIED by both routes (+ H4) (`h1.py` -> `h1.log`, 10.4 s)
- Ξ₂₇(3144.8946) ∈ −1.76019463127752e-1070 ± 5.0e-1138 (T, 256 bits) ± 3.2e-1435 (L, 4800 bits) ± 6.0e-1915 (L, 6400 bits);
  Ξ₂₇(3144.8947) ∈ +1.06871649226171e-1070 (same radii). Certified sign change -> real zero in (3144.8946, 3144.8947).
- H4: Ξ₂₇(3145.5998) ∈ +1.12975694291664e-1070, Ξ₂₇(3145.5999) ∈ −1.14913915362778e-1070 -> real zero in (3145.5998, 3145.5999).
- L/T overlap at all four endpoints, |L − T| ≤ 5.1e-1138. Values agree with the orchestrator's reference (BRIEF §2).

## 2026-09-30 22:49 — stage 3: H2 CERTIFIED, k = 1 (`h2.py` -> `h2.log`, 36 s, route T on ball inputs, M = 31)
- S = c + [−r, r]², c = 3143.2206824215 + 0.3152587994 i. Winding number of Ξ₂₇ along ∂S = 1 for
  r = 1e-3 (512 pieces; at 256 AND 512 bits), r = 1e-6 (512), r = 1e-10 (663), r = 4e-11 (807 pieces) — smallest r reached
  4e-11 (the NOTE's 50-digit zero sits at c + 3.66e-11 − 2.18e-11 i, so r < 3.66e-11 cannot contain it with this centre).
  Total ΔArg = 6.28318530717959 ± 4e-15 each time; every piece enclosure in an open half-plane.
- N = 27 controls (same code): square c + 2.5e-3, r = 1e-3 -> 0; square c + 1.5e-10, r = 1e-10 (zero 1.3e-11 outside) -> 0.
- Arb comparison semantics checked: x > 0 is True only if certain ([−1,1] > 0 False; [1 ± 1.5] > 0 False).

## 2026-09-30 22:51 — stage 4: cross-check L vs T PASSED (`xcheck.py` -> `xcheck.log`, 10.4 s)
- 14 exact points: centre c, the NOTE's zero z0*, the 4 corners and 4 side midpoints of the r = 1e-3 square, the 4 corners
  of the r = 4e-11 square. Route L at 4800 bits vs route T at 256 and 1024 bits: ALL balls overlap;
  |L − T| ≤ 6.4e-1137 (T at 256 bits) and ≤ 1.2e-1288 (T at 1024 bits), against values ~1e-1076 … 1e-1068.
  E.g. Ξ₂₇(c) ∈ 1.6557370640183e-1076 + 2.0178675679148e-1076 i (L rad 4.9e-1435; T rad 2.3e-1137 / 8.3e-1289).
- Next: CERT.md (proofs of Lemma B, Lemma Γ, Lemma T, half-plane lemma), hashes.

## 2026-09-30 22:56 — stage 5: optional H5 (seed chain ξ₂₄) CERTIFIED (`h5.py` -> `h5.log`, 3.2 s)
- ξ₂₄(s) = ½ + ½s(s−1)Σ_{n≤24} g_n(s) (NOTE §1). On-line sign changes, both routes (T 256 bits, L 4800 bits):
  ξ₂₄(½ + 2510.2026 i) ∈ +2.81317536164e-854, ξ₂₄(½ + 2510.2027 i) ∈ −1.65267129215e-854;
  ξ₂₄(½ + 2510.7086 i) ∈ −3.23281139505e-854, ξ₂₄(½ + 2510.7087 i) ∈ +6.14184061542e-855.
- Winding of ξ₂₄ (route T) around the s-square centred 0.8159896243 + 2508.2839748053 i: k = 1 at r = 1e-3 (151 pieces)
  and r = 1e-10 (174 pieces); control square shifted +2.5e-3 i: k = 0. L/T overlap at the NOTE zero and at the centre.
- So ξ₂₄ has a zero with Re s ≥ 0.8159896242 > ½ at height ≤ 2508.2839748054 below on-line zeros at t ∈ (2510.2026,
  2510.2027) and (2510.7086, 2510.7087): the ordering invariant fails for the seed chain at N = 24.
- Tail for route T: Lemma G (|g_n(s)| ≤ 2e^{−X}/X for −1 ≤ Re s ≤ 2), proof in CERT §8.

## 2026-09-30 22:58 — stage 6: CERT.md final (194 lines); hashes; producer A DONE
- Verdict: Theorem H certified. H1 (both routes), H2 (k = 1 at r = 1e-3 … 4e-11, route T), H3 follows; optional H4, H5 done.
  No clause contradicted; no piece failed to exclude 0 (max bisection depth 7 of 16).
- SHA-256:
    b1ecfe0a604c8b05e3439ad9ecae1c2a86c2fcdda55930cecbd1defea499513f  CERT.md
    d88efc8879dc7b22b9fac0bb01c5f47baf983c92778f14c208765053848d473a  ladder.log
    e9ac0878ea67ef58e57dfcb23838436b2b3fdd92185ace6286f7d6faa21d7c56  h1.log
    90a00e963b1f7891c092e4d65127568aea99f06b45789e54db96ce91e70d7f90  h2.log
    e05c73a7d4ce1e7c0fc8fbd0a9b5be0c595b9a4ec10d22a9752ccc160e4d799e  xcheck.log
    48455c3a41864bdf1208557f491085351991d5d968a97b46c772a09c6277ae05  h5.log
  (script hashes in CERT.md §9). Re-run check (22:59): h1.py and xcheck.py reproduce their logs identically up to timings.
