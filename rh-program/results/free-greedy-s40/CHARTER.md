# S8 — the free greedy system: charter for the stream `free-greedy-s40`

**Written 11:35 IST 2026-10-01 (Session 40, orchestrator Fable 5.1). The construction is the orchestrator's own, proposed this session during the read at the line of `results/u-offsurgery-s39/NOTE.md`; `[novelty: single-check]` until the prior-art gate is passed by two models.** Two units work on it side by side and share `results/free-greedy-s40/SHARED.md` (append dated blocks; read it at start and before every close): `compute/` (the system at scale, its integer error, its zeros) and `theory/` (the identities, the mechanism, the proof problem).

## 0. Why this object
Conjecture U (the program's, `results/novel-wave-s37/beurling-frontier/NOTE.md` §7.2): every DISCRETE Beurling [α, β]-system has α ≤ max{½, 2β} (α = exponent of ψ_P(x) − x, equivalently the supremum of real parts of zeros of ζ_P when zero-driven; β = exponent of N_P(x) − ρx). It implies RH (ℕ has β = 0). Diamond–Montgomery–Vorhauer (Math. Ann. 334 (2006), p. 4) left open whether integer regularity below the square root forces RH-type prime regularity for discrete systems. Session 39's candidate S5(ρ) (integers as g-primes, chosen greedily so that N tracks ρx) crosses U's line numerically at 10⁹, but the orchestrator's read found that its integer error is driven by MULTIPLICITY: S5 is supported on ℕ, a refused rational prime enters through many composite g-primes ("carriers"), integers acquire many factorizations (a_n = 276 at n = 902538000), sup E equals the largest multiplicity, and that multiplicity is a factorization-counting function whose exponent keeps rising (0.27 at 10⁹; rigorous lower bounds 0.30 at 10¹⁴, 0.33 at 10³⁰). So S5's "β ≈ 0.30" is a transient. S8 removes the cause: real positions, no coincidences.

## 1. Definition (S8(ρ), threshold ½)
Fix ρ ∈ (0, 1]. Target T(x) = ρ(x − 1) + 1. Sweep x upward from 1 with N(x) = #{g-integers ≤ x} (the empty product 1 included), deficit D(x) = T(x) − N(x). Between g-integers D increases at slope ρ; at a g-integer it drops by 1. **Rule: whenever D reaches ½, a new g-prime is placed at that x** (then D = −½). Composites are all products of two or more g-primes (with repetition), each multiset counted once; a composite arriving exactly at a deficit time is counted first. So g-primes lie on the lattice 1 + (k − ½)/ρ, k ∈ ℤ.
Facts that follow at once (to be written as lemmas by the theory unit): (a) E(x) := N(x) − T(x) ≥ −½ for all x; (b) consecutive g-primes are at least 1/ρ apart; (c) if 1/ρ is transcendental, distinct multisets of g-primes have distinct products (the products are distinct polynomials in t = 1/ρ with rational coefficients — unique factorization in ℚ[t]), so the g-integers are a FREE monoid of distinct reals — no multiplicities; (d) with V(x) := ρ(x − 1) − C(x) (C = number of composites ≤ x), π_P(x) = max(0, ⌊sup_{y≤x} V(y) + ½⌋) and E(x) = π_P(x) − V(x): **the integer error is the drawdown of V below its running maximum** (a discrete Skorokhod reflection); E is large only after a stretch in which composites alone arrive faster than ρ.

## 2. What the prototype shows (`proto/s8_proto.py`, Python, event-driven: a heap holding the next composite of every g-prime, one cursor per g-prime into the sorted list of g-integers; logs in `proto/`)
ρ = π/4, X = 10⁷ (7,853,984 g-integers, 650,561 g-primes; first g-primes 1.6366, 4.1831, 6.7296, 10.5493, 15.6423, 16.9155, …):

| x | sup E | sup\|ψ_P − x\| | max # g-integers in a unit window |
|---|---|---|---|
| 10³ | 8.22 | 108.6 | 5 |
| 10⁴ | 13.33 | 758.6 | 6 |
| 10⁵ | 26.63 | 4792.7 | 7 |
| 10⁶ | 39.53 | 29823.2 | 8 |
| 10⁷ | 47.86 | 260184.9 | 9 |

sup E / log²x = 0.172, 0.157, 0.201, 0.207, 0.184 — consistent with E ≍ 0.18·log²x (the stationary tail of a queue with Poisson-like arrivals at rate ρ − 1/log x served at rate ρ predicts (ρ/2)·log²x up to a constant); a power law x^{0.19} fits the same five points and the two separate only beyond 10⁹. sup|ψ_P − x| has local exponents 0.6–1.0 (0.87 over [10⁵, 10⁷]): the primes are very irregular while the integers are almost as regular as they can be. Other densities at 10⁶: ρ = 0.8 (rational; lattice (10k + 3)/8): sup E 41.2; ρ = e/π: 37.3; ρ = 0.95·π/3: 82.4.
**If β(S8) = 0 (or any β < ¼) and ζ_P has a zero with real part > ½, Conjecture U is false in the strongest way, and DMV's question is answered: discreteness, unique factorization and near-perfect integer regularity do not confine the zeros.** RH itself is not touched (U implies RH, not conversely) — what it would show is that the ADDITIVE structure of ℕ, which S8 lacks, is the indispensable input.

## 3. The rung-1 analog is on the record
`results/u-offsurgery-s39/NOTE.md` §3.1 and `results/novel-wave-s37/beurling-frontier/NOTE.md` §5.4: the virtual curve V over F₅ (Z = (1 − 5u + 5u²)/((1 − u)(1 − 5u)), A_n = (5ⁿ − 1)/4 exactly, zeros at Re s = 0.79899) is built the same way (closed-point counts b_d ≥ 0 fitted to prescribed A_n) — perfect integer regularity, RH false. S8 is its ℚ-side analog with a continuum of norms.

## 4. Rules for both units
Repo root: the `riemann` folder; paths contain spaces — quote them. U.S. English. Machine-clock stamps (`date`). No git. Write only inside your own sub-folder (`compute/` or `theory/`) and append to `results/free-greedy-s40/SHARED.md`. Labels on every statement: **[proved here]**, **[computed]** (script + log on disk), **[quoted]** (source at page/line, on disk), **[recalled, unverified]** (never load-bearing), **[novelty: single-check]**. Standing order 5: no decisive claim rests on a recalled fact. KICKSTART 10(g): no "clearly / obviously / it is easy to see / well known". Compute: at most one heavy process of your own at a time; before starting one run `ps -Ao pcpu,comm | awk '$1>50' | wc -l` and wait if it prints 4 or more; at most 4 GB RAM; no run over 30 minutes without a checkpoint; scratch files over 50 MB go under `/private/tmp/rh-s40-free-greedy/`, never into the repo.
