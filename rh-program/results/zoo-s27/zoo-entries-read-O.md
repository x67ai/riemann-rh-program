# Zoo stream `zoo-s27`, Session 27 — READER report (Opus 5, independent second model, standing order 7)

**Opened Fri Sep 25 20:49:47 IST 2026 (machine clock, `date`).** IN PROGRESS — sections land one at a time; the verdict table is written last.
**Brief:** `results/zoo-s27/BRIEF.md` (`cf239a80…`, recomputed, matches), section "The reader (Opus 5)". FORMAT precedent `results/zoo-s25/zoo-entries-read-O.md`.
**Writer's deliverables checked:** `results/zoo-s27/zoo-entries-proposed.md` `38986446…` (recomputed, matches); `scripts/zoo-insert-s27.py`; `results/zoo-s27/SHARED.md`; `results/zoo-s27/dryrun-BARRIER-ZOO.md`; the writer's `prior-art/` folder and finding 7 were NOT opened until §4 (my own search) was on disk.

---

## §1 Computations (my own scripts, `results/zoo-s27/verify-O/`)

- **`zeros200_O.py` → `zeros200_O_run.log`** (mpmath 1.3.0, dps 30; written without opening `results/zoo-s26/verify/*`): at the first 200 zeros, c_k = Re[1/(ρ_kζ′(ρ_k))] is **positive at 96 and negative at 104**, **108 sign changes in 199 steps**; the residue of 1/ξ, 1/ξ′(ρ) with ξ′(ρ) = ½ρ(ρ−1)π^{−ρ/2}Γ(ρ/2)ζ′(ρ), has max | |arg| − π/2 | = **5.96·10⁻²⁹** and Im alternates at **199 of 199** consecutive pairs (Im < 0 at k = 1); arg(1/ζ′(ρ))/π ∈ **[−0.506529, +0.506296]**, Re(1/ζ′(ρ)) < 0 at **k = 127, 136, 196**. Every number the blocks `i5`/`iv4` and note §3.2 quote is reproduced to the printed digit.
- **`witt_diag_O.py` → `witt_diag_O_run.log`** (see §3 for the derivation it checks): Part A, the Z-basis v_d = (d·[d | n])_n of the truncated ghost lattice, 0 congruence violations at N = 120; Part A2, gcd{d : d | n, d > 1} = e^{Λ(n)} at every 2 ≤ n ≤ 20 000 (0 mismatches); Part B, 4 000 random big-Witt vectors in Witt coordinates, ghost map from the definition w_n = Σ_{d|n} d·x_d^{n/d}: (1.10) holds for all 4 000, and gcd(w₁ − w_n) over the samples equals e^{Λ(n)} at every n = 2 … 40 (11 → 11, 13 → 13).

