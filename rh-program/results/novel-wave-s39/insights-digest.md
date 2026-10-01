# Insights digest — wave 3 (Sessions 38–40, eleven units; KICKSTART 10(a)): rigidity, the line α = 2β, and integer-greedy systems

Consolidation agent (Opus 5.5), 2026-10-01, Session 41. Brief: `DIGEST-BRIEF.md` (this folder). Inputs in the brief's order: the wave-2
digest and staged zoo lines (`results/novel-wave-s37/`, the baseline: its §B B1–B10, §F ranking, UT-1 … UT-13); per unit `NOTE.md` (as
corrected by its dual read), `read-F.md` (Fable 5.1, the orchestrator), `read-O.md` (Opus 5.5); `results/lemmaB-s41/CHARTER.md` (its unit
folders not read — in flight); `directions/README.md` and the Instruments tables of B2 and C2; `digest-APPLIED.md` (what is already
applied for the five Session-39 units); `BARRIER-ZOO.md` (788 lines; the Session-40 count paragraph, I.2, I.9, I.10, I.11 only).
SHA-256 prefixes of every input: `SHARED.md` block 11. Nothing here is new mathematics unless marked `[consolidator's reading]`.

Unit folders (all under `results/`): qcond = `qcond-s38/`, conjO = `conj-O-s38/`, uoff = `u-offsurgery-s39/`, lemG = `lemmaG-s39/`,
dzh = `dz-half-s39/`, qtw = `qtwin-s39/`, fej = `fejer-form-s39/`, fgT = `free-greedy-s40/theory/`, fgC = `free-greedy-s40/compute/`,
s5m = `s5-multiplicity-s40/`, lg = `local-greedy-s40/`. "NOTE:n" = line n of that unit's NOTE.md as on disk at 16:57 IST (post-read);
"rF:n", "rO:n" = lines of its read-F.md, read-O.md.
Status labels (as the reads leave them): **THEOREM (dual-read)** = proved in the NOTE and re-derived at the line by both reads;
**(dual-read, repaired)** = the same after a FIX-FIRST repair now applied; **CONDITIONAL THEOREM** (hypothesis named); **NUMERICAL (k
producers)**; **WITHDRAWN**; **single-check** = one model only. Where read-F and read-O differ, the entry says so and names the read that
re-derives the point at the line.

## §A Per unit

### A.1 qcond — Q_cond: a Beurling system with Riemann's exact FE at conductor q > 1? Close T (stated classes, every conductor) + G
Verdicts: read-F AGREES with ONE UPGRADE (rF:5); read-O AGREES-WITH-CORRECTIONS, F1–F3 (rO:9–24). Both found the upgrade of Theorem D
independently at Meyer 1970 LNM 117 p. 25 (NOTE:3).
Three most useful findings.
1. **Theorem D** (NOTE:351–358, the complete copy; close NOTE:451–452): every DISCRETE Beurling system with Riemann's exact FE at any
   conductor q > 0 is the rational primes, q = 1. THEOREM (dual-read, upgraded to unconditional): rF:18, rO:13–15 (F1, rO:230–243).
   Remaining off-disk input: Rosenthal, Mem. AMS 63 Th. 1.6, cited inside Meyer's printed proof (NOTE:470; rO:350–352).
2. **Theorem U_q** (NOTE:228; close NOTE:440–441): the uniformly discrete class is rigid at every conductor. THEOREM (dual-read; rF:11,
   rO:10). Novelty split by read-O F2 (rO:16–19, 23–24): "new reduction … on a printed core (Hilberdink 2012 §4)", whose Thm C already
   excludes every squarefree conductor in the u.d. family.
3. **Theorem L′** (NOTE:199; close NOTE:442–444) — no ζ·(finite generalized Dirichlet polynomial) has Riemann's FE at any conductor — and
   **Corollary E2** (NOTE:178; close NOTE:445–446) — no purely continuous system does. THEOREM (dual-read; rF:9–10; rO:10). L′ "new in its
   real-frequency statement, method printed for integer divisor-supported multipliers" (rO:23–24).
Most useful failure. The finite Euler-side LP (§2.5) "could never see Π ≥ 0": the sieved identity (E) holds for every finite SIGNED sieve
(rO:344–345, R4), and on F₅ the linear Q-side constraints admit the RH-false t = ±5 (NOTE:463–465). Linear constraints are blind to positivity.
Borrow. (a) The subtraction μ′ = μ_q − (ρ_q − 1)·Lebesgue turns a self-dual measure with unit masses off 0 into Meyer's unit-mass comb
(NOTE:353–354; by-product ρ_q ∈ Z for any discrete candidate, rO:338–339). read-F subtracts ρ_q·Lebesgue and gets the comb on Λ∖{0}
(rF:18); both normalizations are valid [consolidator's check: 𝔉(cλ) = cδ₀]; the NOTE uses read-O's. (b) The Landau (Pringsheim)
obstruction on the finitely generated "q-part" of the frequencies, where ζ's pole is invisible (NOTE:447–450) — the rung-1 F2 condition
with the pole term removed (NOTE:463–465).
Statuses. U_q, L′, E1–E3, Prop. E/E′, §1.4 Cor. 1–3, §1.6, Lemma Q, Theorem D: THEOREM (dual-read; D upgraded). Lemma S–W′: read-F
`[single-check]` pending (rF:12); read-O re-derived it against S–W §4 at the page (rO:10–11) — dual-read. Novelty: E2, D, §1.6 "not found
in print (dual-checked)" (rO:24). Open residue G: weighted/mixed systems with clustering integers and infinitely many distinct masses
(NOTE:458–459, 466–469) — inherited by qtw.
