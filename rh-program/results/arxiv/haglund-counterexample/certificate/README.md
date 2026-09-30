# Certificate archive

Reproducibility archive for the paper *A counterexample to Haglund's monotonic-zeros conjecture
for the Riemann Ξ approximants* (Kunal Tyagi, October 1, 2026). Code and data:
https://github.com/x67ai/riemann-rh-program, directory `rh-program/results/haglund-cert-s37/`.

## What is certified

The objects are J. Haglund's, arXiv:0910.5228 pp. 1-3: `Ξ_N(z) = Σ_{n≤N} Φ_n(z)` with
`Φ_n(z) = 2π²n⁴ G(z/2; n²π, 9/4) − 3πn² G(z/2; n²π, 5/4)` and
`G(z; a, b) = Γ(b+iz, a)/a^{b+iz} + Γ(b−iz, a)/a^{b−iz}` (his (10), (13), (14)).

- **H1.** Ξ₂₇ changes sign on (3144.8946, 3144.8947): a real zero x₁.
- **H2.** Ξ₂₇ has winding number 1 along the boundary of the square of half-width r about
  c = 3143.2206824215 + 0.3152587994 i, for r from 10⁻³ down to 4·10⁻¹¹ (A) and 3.7·10⁻¹¹ (B);
  B also encloses the zero in a square of half-width 10⁻⁴⁸ about an explicit center
  (`producer-B/CERT.md` §0, H2*).
- **H3 (consequence).** The zero z₀ in that square is non-real, lies in the closed first quadrant,
  and has real part below x₁: Haglund's Conjecture 1 (p. 3) and its weak form (Remark 1, p. 4)
  are false for N = 27.
- **H4.** A second real zero in (3145.5998, 3145.5999).
- **H5.** The companion truncation ξ₂₄(s) = ½ + ½s(s−1)Σ_{n≤24} g_n(s) = Ξ₂₄ + c₂₄, where
  g_n(s) = X^{−s/2}Γ(s/2, X) + X^{−(1−s)/2}Γ((1−s)/2, X) and X = πn², has a zero off the critical
  line near s = 0.8159896243 + 2508.2839748053 i (winding number 1) below zeros on the line at
  t ∈ (2510.2026, 2510.2027) and (2510.7086, 2510.7087).

Each certificate first runs a ladder of known cases: the largest real zeros of Ξ₁ and Ξ₂ from
Haglund's table (p. 4), the first non-real zero of Ξ₁ from his appendix (p. 16), and zero-free
control squares.

## Contents

| Path | What it is |
|---|---|
| `producer-A/` | Certificate A: Arb ball arithmetic through python-flint 0.6.0 (FLINT 3.0.1). `hag_core.py` (both evaluation routes, the tail bound, the winding-number walk), `ladder.py`, `h1.py` (H1, H4), `h2.py` (H2), `xcheck.py` (route cross-check), `h5.py` (H5), their logs `*.log`, `CERT.md` (statement, method, proofs of the analytic lemmas, tables, SHA-256 of every script and log), `SHARED.md` (the working log). |
| `producer-B/` | Certificate B: outward-rounded interval arithmetic of mpmath 1.3.0, no Arb. `ivc.py` (interval complex arithmetic), `specfun.py` (Γ, ζ, h with proved remainders), `xin.py` (Φ_n, Ξ_N, tail bound), `winding.py` (Taylor model and boundary walk), scripts `selftest.py`, `ladder.py`, `cert27.py` (H1-H4, H2*), `crosscheck.py` (X1-X3), `cert_h5.py` (H5), `logs/`, `lit/` (the DLMF pages whose remainder bounds are used, saved 2026-09-30), `CERT.md`, `SHARED.md`. |
| `rerun-F/` | Independent re-runs: certificate A's `h1.py` (`A-h1-rerun.log`, and `A-h1-diff.txt`, the diff against `producer-A/h1.log`: timings only) and certificate B's `ladder.py` (`B-ladder-rerun.log`). |
| `verify-F/` | A third, separately written evaluation of the literal sum (13)-(14) in Arb at 4800 bits (`haglund_direct_arb.py`, `rerun_N27.py`, log `rerun_N27.log`), with the ladder check of Haglund's two table zeros. |
| `NOVELTY-F.md` | The literature search on the refutation (working note). |
| `SHA256SUMS` | SHA-256 of every file in this archive except itself. |

The `CERT.md`, `SHARED.md` and `NOVELTY-F.md` files are the working records, copied verbatim.

## Requirements

Tested with the system Python 3.9.6 of macOS 27.0.1 on an Apple M4, single core, one process at a
time. Certificate A and `verify-F/` need python-flint 0.6.0 (it bundles FLINT 3.0.1 with Arb);
certificate B needs mpmath 1.3.0 and nothing else (pure-Python backend, no gmpy):

    python3 -m pip install --user python-flint==0.6.0 mpmath==1.3.0

Other versions of python-flint may print balls with different radii; the certified signs and
winding numbers should not change, but only the versions above were run.

## Running certificate A (about 72 s in total)

The scripts print to standard output; write to new files and compare with the archived logs.

    cd producer-A
    for f in ladder h1 h2 xcheck h5; do python3 $f.py > $f.new; diff $f.log $f.new; done

Expected: the only differences are the timing figures, such as `(3.8s)`. Run times on the machine
above: ladder 11.9 s, h1 10.4 s, h2 36.2 s, xcheck 10.4 s, h5 3.2 s. Key lines to look for:

    H1 route L prec 4800: certified sign change on [3144.8946, 3144.8947]: True
    H4 route L prec 4800: certified sign change on [3145.5998, 3145.5999]: True
    H2[r=4e-11,prec=256] total Arg increment = [6.28318530717959 +/- 3.53e-15] ; winding = [1.00000000000000 +/- 3e-20] ; ...
    CTL27a[c+2.5e-3,r=1e-3] total Arg increment = [+/- 6.85e-66] ; winding = [+/- 1.09e-66] ; ...
    XCHECK VERDICT: all 14 points overlap (L vs T at 256 and 1024 bits): True ; ...
    R1 all certified: True
    R2[N=1,r=1e-10] winding number certified = 1
    H5b[r=1e-10] winding number certified = 1

`h1.log` prints the four routes (T at 256 and 1024 bits, L at 4800 and 6400 bits) for each of the
four endpoints; `h2.log` prints every boundary piece's enclosure and argument increment.

## Running the third evaluation (about 7 s)

    cd verify-F
    python3 rerun_N27.py > rerun_N27.new; diff rerun_N27.log rerun_N27.new

Expected: timings only. It prints, among others,
`Xi_27(3144.8946)  Re: [-1.76019463128e-1070 +/- 2.49e-1082]` and
`Xi_27(3144.8947)  Re: [1.06871649226e-1070 +/- 1.71e-1082]`.

## Running certificate B (about 15 minutes in total)

Each script writes its own log into `producer-B/logs/`, overwriting the archived one. Work on a copy
and compare the copy's logs with the archived ones:

    cp -R producer-B /tmp/producer-B-run && cd /tmp/producer-B-run
    python3 selftest.py && python3 ladder.py && python3 cert27.py && python3 cert_h5.py \
      && python3 crosscheck.py X1 X2 && python3 crosscheck.py X3
    for f in logs/*.log; do diff "$OLDPWD/producer-B/$f" "$f"; done

(`$OLDPWD` is the archive directory you started from.) Expected: the only differences are timing
figures. Run times on the machine above: selftest 2 s, ladder 118 s, cert27 56 s, cert_h5 17 s,
crosscheck X1 X2 16 s, crosscheck X3 664 s (the 4400-bit literal sum). Key lines to look for:

    SUMMARY: R1 certified;  R2 winding numbers {'1e-3': 1, '1e-8': 1} (expected 1);  R3 winding number {'0.25': 0} (expected 0); ...
    H2: r = 3.7e-11 -> winding number k = 1
    H2: r = 3.5e-11 -> winding number k = 0
    H2*: square z* + [-r, r]^2, r = 1e-48 -> winding number k = 1
    SUMMARY: H1 True; H4 True; H2 k(r=1e-3) = 1, smallest r = 3.7e-11; control k = 0; H3 HOLDS; ...
    SUMMARY H5: real zeros certified True; winding at r = 1e-3: 1; control 0; ...

`logs/crosscheck-X3.log` prints, for each of the four real-axis points, the literal sum and the tail
route with their intervals and "overlap True ; same strict sign". `logs/crosscheck-run1-X2invalid.log`
is kept for the record only: its X2 part ran at 1400 bits, where one method's boxes are useless, and
is void (see `producer-B/SHARED.md`); its X3 values equal the valid run's.

**About `producer-B/logs/ladder.log`.** `ladder.py` rewrites this file on every run. The file in the
archive is the output of the independent re-run of 2026-09-30 23:48 (it equals
`rerun-F/B-ladder-rerun.log` except for a final "exit 0" line added by the re-run harness), so its
SHA-256 differs from the one recorded for `logs/ladder.log` in `producer-B/SHARED.md` (final block).
Every value in it equals the values in `producer-B/CERT.md` §C. All other hashes recorded by both
certificates match the files here.
