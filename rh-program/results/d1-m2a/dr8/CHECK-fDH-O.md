# D-R8 independent check — `cert_of_checkW1_fDH` + the M3 seed ledger (Session 20, Job 2, Opus 5)

**Checker:** Claude Opus 5 (1M), 2026-09-10, KICKSTART 10(f) second model. Brief of record:
`results/d1-m2a/dr8/BUILD-BRIEF-fDH.md` (Job 2 paragraph + the 02:47 addendum). Pricing of record:
`PRICING-fDH.md` (§1.1 the object, §1.3 the convention, §3.1 the BINDING statement shape, §3.2 the
only label) and `PRICING-M3-ledger.md` (§1–§2). Everything below is RE-DERIVED with my own scripts
and my own clean-clone build; Job 1's scripts are read only to know what was claimed, never run in
place of my own. Scripts and raw logs: `results/d1-m2a/dr8/check-o/`. Written as the work lands
(RULE ONE).

**Status line:** IN PROGRESS — §0 setup.

## 0. Setup, provenance of the tree I checked

**Tree checked.** Clean clone `~/rh-lean-work/checker-clone-s20/` (upstream tag v1.0 + the mirror at
`a4a14f6f`, built during the packaging check), overlaid with the CURRENT mirror `rh-program/lean/`
at git commit **`5fe6aa279ba68de83dfa737530810da1d26d62f3`** (`5fe6aa2`, "D-R8 Job 1 harvested; Job 2
launching"). Toolchain `leanprover/lean4:v4.33.0-rc2`, Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`
(verified by `git -C .lake/packages/mathlib rev-parse HEAD` in the clone itself).

**What the overlay actually changed** (my own file-by-file `cmp` of all 143 mirror files against the
clone BEFORE copying — `check-o/overlay-plan.txt`): exactly **six** paths, and no others.

```
NEW      formalization.yaml
NEW      Zeta23/W1/FDH.lean
NEW      Zeta23/W1/Ledger.lean
CHANGED  README.md
CHANGED  Zeta23.lean
CHANGED  Zeta23/W1/Soundness.lean
```

Every other mirror file — all of `Zeta23/DBN/**`, all of `comparator/**`, `Instances.lean`,
`ArgPrincipleBridge.lean`, `Format.lean`, `Checker.lean`, `Examples.lean` — was **already
byte-identical** in a clone that predates this work. That is an independent confirmation of Job 1's
"untouched" claim that does not go through any hash file. Post-overlay SHA-256 of the five Lean/YAML
files equals `hashes-fdh.txt` line for line.

**The pre-change baseline is mine.** Before the overlay I ran, on the clean clone,
`#check @Zeta23.W1.cert_of_checkW1_ap` and `#print axioms` (`check-o/before_ap.lean`,
`check-o/no-regression-before.out`, 10.4 s). That is my own "before", not Job 1's `no-regression.log`.

Load discipline: `ps -Ao pcpu,comm | awk '$1>50'` empty before every build; one `lake` process
throughout. `caffeinate` and both watchdogs running.

## 1. Cold build of the overlaid clone — PASS

`lake build Zeta23` from the changed modules: **Build completed successfully (9144 jobs)**,
**79 s** wall (300.6 s user, 616 % CPU), started 03:50:50, ended 03:52:09
(`check-o/build-zeta23.log`, 878 lines).

* **Errors: 0.** The two lines matching `error` are the module name
  `Zeta23.XiPrime.ExplicitFormula.EntryError` and its file path — not diagnostics.
* **Warnings from any program module (`Zeta23/W1/**`, `Zeta23/DBN/**`, `comparator/**`): 0.**
  All 247 warnings are upstream Zeta23 deprecations (`Set.mem_setOf_eq`, `ENat.toNat_coe`,
  unreferenced binder names) in `Statement.lean`, `Assembly.lean`, `ZeroSide/**`,
  `FromPNTPlus/**`, `RvM/**`, `WeilEF/**`, `ThmE/**`, `XiPrime/**`.
* The four W1 modules built (not replayed) in order — `Soundness` 5.2 s, `ArgPrincipleBridge` 1.6 s,
  `Ledger` 1.6 s, `FDH` 1.7 s — and the whole DBN cascade (`BarrierCert` and the 116
  `Instance02.*` modules) rebuilt behind them and succeeded. So the generalization of
  `Soundness.lean` does not break a single downstream DBN module.

## 2. `#print axioms` — my own probe over every top-level declaration — PASS

Not Job 1's list: I stripped the (nested) block and line comments from `FDH.lean`, `Ledger.lean`
and `Soundness.lean` with my own parser and took **every** `theorem`/`lemma`/`def`/`abbrev`
declaration it found — 11 + 8 + 79 = 98 names — then added `cert_of_checkW1_ap`,
`rectArgPrinciple_riemannZeta`, the ten `_check` literals and `mpDH`/`arbDH`: **112 declarations**,
all probed in one file (`check-o/axioms_probe.lean`; full log
`results/d1-m2a/dr8/CHECK-fDH-O-axioms.log`, 2.1 s, exit 0).

| axiom set | count |
|---|---|
| `[propext, Classical.choice, Quot.sound]` | 87 |
| `[propext, Quot.sound]` | 2 |
| `[propext]` | 19 |
| "does not depend on any axioms" | 4 (`consecPairs`, `consecPairs_map`, `mpDH`, `arbDH`) |

112 = 87 + 2 + 19 + 4, so nothing was silently skipped. **Every set is a subset of the three
standard axioms.** No `sorryAx`, no `Lean.ofReduceBool` (i.e. no `native_decide` anywhere in the
dependency cone), no `Classical.em` as a separate axiom, no program-declared `axiom`. In particular

* `cert_of_checkW1_fDH`, `mpDH_zero`, `arbDH_zero`, `differentiable_fDH`,
  `hasSum_hurwitzZeta_one_fifth`, `cert_of_checkW1_of_diffOn`,
  `continuousOn_logDeriv_seg_of_diffOn`, `cert_of_checkW1`, `cert_of_checkW1_ap` and all eight
  `_exclusion` corollaries: `[propext, Classical.choice, Quot.sound]`;
* the ten `by decide +kernel` literals (`mpDH_check`, `arbDH_check`, the eight `*Null*_check`):
  `[propext]` — kernel reduction, not `native_decide`.

## 3. κ — four independent routes, 80 digits — PASS

My own script (`check-o/kappa_o.py`, log `check-o/kappa-o.log`); Job 1's `kappa_check.py` was
neither imported nor run. mpmath at `mp.dps = 80`.

| route | how | κ (60 digits) |
|---|---|---|
| A contract | the line `kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)` located by regex in **both** `results/d1-m1/FORMAT.md` and `results/ccm-dh-test/dh.py` (found verbatim in both), evaluated | 0.284079043840412296028291832393126169091088088445737582759163 |
| B Lean | `def kappaDH : ℝ := …` re-read by regex from `lean/Zeta23/W1/FDH.lean`; identifiers restricted to `Real.sqrt` (nothing else appears); Lean juxtaposition rewritten to Python calls by my own mini-parser | identical |
| C Gauss sum | χ mod 5 built from χ(2) = i on the primitive root 2 (χ(1)=1, χ(2)=i, χ(3)=−i, χ(4)=−1); τ(χ) = Σ χ(a)e^{2πia/5} = −1.17557… + 1.90211…i, \|τ\| = √5 exactly; ε = τ/(i√5), \|ε\| = 1; κ = tan(arg ε / 2) | identical |
| D dh.py | the body of `dh.py`'s `kappa()` re-read by regex and `exec`'d in an empty namespace (not imported) | identical |

Pairwise: A = B = D to the last bit (difference exactly 0); the Gauss-sum route agrees with all
three to **2.6·10⁻⁸¹**. The demand was ≥ 30 digits; this is > 50 by construction and ~80 in fact.
Guards: radicand 10 − 2√5 = 5.52786… > 0, denominator √5 − 1 = 1.23607… ≠ 0, so no `Real.sqrt`
junk value and no division by zero enters `kappaDH`. Leading digits 0.28407904…, as PRICING §1.1.
**This equals Job 1's figure to all 60 digits it printed.**

## 4. The Hurwitz convention — PARTLY A LEAN THEOREM, and I say which part

The brief asks whether the Mathlib-vs-mpmath-vs-Arb identification is a proof or a meta-level
identification. The honest answer has two halves, and Job 1's file states it correctly.

**(a) Proved in Lean.** Mathlib `51e6992e`, `Mathlib/NumberTheory/LSeries/HurwitzZeta.lean:72`
(read at the source in the clone's own `.lake/packages/mathlib`):

```lean
lemma hasSum_hurwitzZeta_of_one_lt_re {a : ℝ} (ha : a ∈ Icc 0 1) {s : ℂ} (hs : 1 < re s) :
    HasSum (fun n : ℕ ↦ 1 / (n + a : ℂ) ^ s) (hurwitzZeta a s)
```

`FDH.lean` instantiates it at a = 1/5 as `hasSum_hurwitzZeta_one_fifth`. I re-elaborated the same
instantiation **at all four shifts a = 1/5, 2/5, 3/5, 4/5** on the built tree, plus
`((1/5 : ℝ) : UnitAddCircle) ≠ ((2/5 : ℝ) : UnitAddCircle)`, plus `kappaDH = …` and
`∀ s, fDH s = …` by `rfl` against the FORMAT §9.2 combination
(`check-o/convention_probe.lean`, `check-o/convention-probe.out`, exit 0, no errors). So **pricing
risk R3 is closed by proof, not by inspection**: the four `UnitAddCircle` casts really are the
reals 1/5, 2/5, 3/5, 4/5 (confirmed again by `#print` under `pp.numericTypes`, which shows
`hurwitzZeta (↑(1 / 5 : ℝ)) s` and so on), and Lean's `fDH` really is
Σ-series-based on Re s > 1 with the shifts in the contract's order and signs.

**(b) META-level, and it cannot be otherwise.** That the two producers' *library calls* compute
that same series is not a Lean statement. I checked it at the source and numerically:

* `results/d1-m1/hurwitz_encl.py` STEP 3′ (lines 20–21): "`zeta(s, a) := sum_{n=0}^{infty}
  (n+a)^{-s}` for sigma > 1, continued elsewhere", continued by Euler–Maclaurin on
  {σ > −2m, s ≠ 1}, with "mpmath's `mp.zeta(s, a)` implements this same continuation" as the
  cross-check target (STEP 4′) — same series, same a-normalization.
* `producer_mp.py` `f_dh_ball` (lines 133–141): `h1 + h2.scale_iv(k) - h3.scale_iv(k) - h4` times
  `pow_int_neg(5, s)`, with `h_j = hurwitz_ball(s, Fraction(j, 5))` — the contract's shifts, order
  and signs exactly. `producer_arb.py` `eval_fdh` (lines 241–247): `s.zeta(acb(rat_ball(j/5)))`,
  same combination, `acb(5) ** (-s)` factor.
* **Numeric re-derivation** (`check-o/convention_o.py`, log `check-o/convention-o.log`, exit 0):
  at s ∈ {2, 3+i, 1.5+10i, 4−2.5i} and a ∈ {1/5, 2/5, 3/5, 4/5} I built Σ_{n≥0}(n+a)^{−s} myself
  as an exact head plus an Euler–Maclaurin tail (`mp.sumem` — a different mpmath entry point from
  `mp.zeta`, so agreement is evidence about the convention rather than about one implementation
  agreeing with itself) and compared with `mp.zeta(s, a)` and with python-flint
  `acb(s).zeta(acb(a))` (= Arb `acb_hurwitz_zeta`). All 16 cells agree; `mp.zeta` vs Arb agree to
  10⁻³⁸–10⁻⁴⁰, my EM route to 10⁻⁴⁹ except at s = 1.5 + 10i where `mp.sumem`'s own floor is
  1.3·10⁻²⁹ (identical for all four a, and it does not move with the truncation point — an
  accuracy floor, not a convention gap). A wrong convention (n ≥ 1 instead of n ≥ 0, a ↦ 1 − a, an
  unnormalized shift) moves the first digits, not the twentieth. The four assembled f_DH values
  agree to 10⁻⁵¹.

**Verdict on the convention: correct, and correctly labeled.** `FDH.lean`'s header calls the
identification "META-level, not a Lean theorem" and `formalization.yaml`'s divergence (l) repeats
it. That is the honest description: half (a) is a Mathlib theorem the file consumes, half (b) is a
documented convention match of exactly the same standing as "mpmath's `zeta(s)` is Mathlib's
`riemannZeta`" on the ζ leg — which is where H-ENCL_DH's meaning lives.

