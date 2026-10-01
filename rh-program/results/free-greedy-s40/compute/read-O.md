# READ at the line — `free-greedy-s40/compute` NOTE — Opus reader (second model of the dual check)

**Reader:** Opus 5.5 agent (Session 41, dual read, brief `results/novel-wave-s41/READ-BRIEF-O.md`). **Opened 14:45 IST 2026-10-01** (machine clock).
**NOTE read:** `results/free-greedy-s40/compute/NOTE.md`, SHA-256 `b7d6c8d0c3f9293d20d13f5e6043b082aeeab0f3a7cbe22d8ed3b6087bf3021f`, 124 lines (matches the brief's b7d6c8d0c3f9293d…). All line numbers below refer to this hash.
**Also read:** `CHARTER.md` (definition §1), `compute/BRIEF.md`, `SHARED.md` (blocks 11:24–14:02), the unit's logs under `compute/verify/logs/` for the numbers compared; the unit's generator sources only AFTER my own generator had produced its numbers (for target (f)). Not opened: `compute/read-F.md`, `compute/verify-F/`, `theory/read-F.md`.
**Independent re-run:** `compute/verify-O/` (my own code, written from CHARTER §1 only; logs in `verify-O/logs/`; scratch over 50 MB in `/private/tmp/rh-s41-read-compute/`).

(Sections are appended as the read lands; the VERDICT LINE is written last, at the top of §0.)

## §2 Independent re-run (`verify-O/`)

**Instrument (my own, written from CHARTER §1 before opening any of the unit's sources).** `verify-O/s8o.cpp`: the g-prime placed when k g-integers are below it sits at L_k = 1 + (k − ½)/ρ; the next g-integer is min(next composite, L_k). Positions are 128-bit unsigned fixed point with 92 fractional bits, t = 1/ρ rounded to 2⁻⁹² from 80-digit mpmath (`verify-O/params_o.py`), each position carrying a rigorous error bound in ulps. Composites are enumerated as m = n·p with p = P(m) the largest g-prime factor and n a "prefix" (every g-integer with n·P(n) ≤ X), each prefix walking the g-prime list from P(n) on — one uniform rule, no √X split, no heap; windows [a, b) with b ≤ a(1 + 0.9(q₀ − 1)) so all factors are known; window composites `std::sort`-ed and merged with the lattice. **Every composite-versus-lattice decision is certified**: |c − L| > err(c) + err(L) with err(c) the window's largest composite bound, plus a check of each g-prime placed after the window's last composite against the window end. A pass with flags = 0 is therefore a proof (modulo the correctness of ~200 lines of C++) that the computed sequence is S8(ρ). Zeta side: `verify-O/zt.c` (direct sum of n^{−s} over a dump of the g-integers, Neumaier-compensated, Newton with the analytic F′, bisection on the real axis); moments Σ n^{−s₀}(λ log n)^j/j! accumulated inside the generator for a Taylor evaluation on boxes (`S8O_CENTERS`).

**(a) Counts, sup E, ψ_P − x — S8(π/4) [computed, `verify-O/logs/o_pi4_1e9.log`, 53 s, 0.57 GB].** Every decimal agrees with the unit's `verify/logs/pi4_1e9.log` S-rows:

| x | N(x) mine = unit | π_P(x) mine = unit | sup E mine / unit | ψ_P − x mine / unit |
|---|---|---|---|---|
| 10³ | 793 | 156 | 8.2174410257 / 8.217441 | −74.819823 / −74.820 |
| 10⁶ | 785,400 | 78,134 | 39.5303075943 / 39.530308 | −5213.645129 / −5213.645 |
| 10⁷ | 7,853,983 | 650,561 | 47.8635398026 / 47.863540 | −225573.710663 / −225573.711 |
| 10⁸ | 78,539,828 | 5,851,473 | 95.8616048208 / 95.861605 | 1662595.074496 / 1662595.074 |
| 10⁹ | 785,398,166 | 50,857,391 | 95.8616048208 / 95.861605 | 162744.004440 / 162744.004 |

The record sup E = 95.8616048208 sits at x = 4.84991215·10⁷ (NOTE l. 59, 105: 4.85·10⁷). Certification: 785,398,157 decisions, **0 flags**, smallest |composite − lattice point| = 3.06·10⁻⁸ absolute (3.76·10⁻¹⁷ relative) against a largest error bound of 1.75·10⁻¹⁸ — margin factor ≥ 2.1·10¹⁰. This reproduces independently the unit's statement that double precision would no longer compute S8 past ~10⁸ (SHARED 11:46: "within 3.8·10⁻⁸ (relative 3.8·10⁻¹⁷) of the threshold by 10⁹") — my smallest margin is the same 3.8·10⁻¹⁷ relative. N(10⁷) = 7,853,983 confirms the NOTE's correction of the charter's 7,853,984 (NOTE l. 56).

**(b) Zeros of F_X for π/4 by direct sum [computed, `verify-O/logs/zt_pi4_1e6_rho1.txt`, `zt_pi4_1e8_zeros.txt`].** At X = 10⁶ (785,400 terms): ρ₁ = 0.896204948081 + 14.549948455069i, |F′| = 4.388447 — the NOTE's 12 digits (l. 108) exactly. At X = 10⁸ (78,539,828 terms, E(10⁸) = 11.4456533355), Newton on the direct sum:

| zero (mine, X = 10⁸, direct sum) | \|F′\| | unit's value at 10⁸ (`verify/logs/zeros_pi4_X1.000000e+08.txt`, block moments) |
|---|---|---|
| 0.896212310637 + 14.549935706583i | 4.388893 | 0.896212310637 + 14.549935706583i |
| 0.716282731356 + 28.358982356773i | 2.518147 | identical, 12 digits |
| 0.712606628787 + 67.294747467075i | 3.239037 | identical |
| 0.666747674994 + 53.915335244569i | 3.803308 | identical |
| 0.661887778990 + 185.211534604613i | 3.877779 | identical |
| 0.652461852903 + 198.611674213405i | 3.472666 | identical |
| 0.641362641766 + 40.646992802774i | 4.815135 | …765 (last digit) |

Seven of the 44 (target (e) asked for five) reproduce to 12 digits by a different evaluation (direct compensated sum, no binning, no FFT).
