# D-R8 pricing — the f_DH-in-Lean statement (Session 20, queue item 2a)

**Written 2026-09-10 by pricing agent 2a (Claude Fable 5.1).** Brief: `results/d1-m2a/dr8/BRIEF.md` §2a. This file is a PRICING, not an implementation: nothing in `lean/` is edited, no build is run. Authorities read: `directions/D1-certified-refutation-arm.md` (D-R8 at line 143; "Current frontier"), `results/d1-m1/FORMAT.md` §2, §7.1, §9.2, `results/d1-m1/acceptance-report.md`, `lean/README.md`, `lean/Zeta23/W1/{Format,Checker,Soundness,ArgPrincipleBridge,Instances}.lean`, Mathlib at commit `51e6992efd06126df61a496bebf8f49482a4e129` (2026-08-03, the commit pinned by `~/rh-lean-work/zeta-23-lean-main/.lake/packages/mathlib`), files `Mathlib/NumberTheory/LSeries/HurwitzZeta.lean`, `HurwitzZetaEven.lean`, `HurwitzZetaOdd.lean`. Paths below are relative to `rh-program/` unless absolute.

Status line (kept current as sections land): §1 object+Mathlib coverage — DONE; §2 soundness twin — DONE; §3 statement+label — DONE; §4 price/risk/GO-NO-GO — DONE; §5 refutation-shaped close — DONE; appendices A–B (probes verbatim) — DONE.

## 0. One-paragraph answer

The DH live fire can be turned into a Lean theorem about f_DH — a twin of `cert_of_checkW1_ap` with `fDH` in place of `riemannZeta`, modulo a displayed `W1EnclOK fDH d` only — at low cost, because the two things that could have been expensive are already done or already in Mathlib: (i) the rectangle argument principle is proved for EVERY `f : ℂ → ℂ` (`rectArgPrinciple_of_local`, v1.1), and (ii) Mathlib `51e6992e` ships `HurwitzZeta.hurwitzZeta` with `differentiable_hurwitzZeta_sub_hurwitzZeta`, from which the entirety of f_DH is a 12-line proof (probed this session against the pinned Mathlib: elaborates in 2 s, axioms `[propext, Classical.choice, Quot.sound]` — Appendix A). The only ζ-specific content in the 1,262-line `Soundness.lean` is one 25-line continuity lemma and one 6-line `hdiff` block; both are instances of a generic lemma that also probed clean (Appendix B). Price: 2 agent-sessions (one builder, one independent Opus checker), about 60 changed lines plus about 150 new lines of Lean, one 7-minute full-tree rebuild, no producer computation. Recommendation (§4.4): GO as a bounded, low-priority, instrument-hardening item that must not displace anything with signal and does NOT trigger the 10(d) reallocation rule.

## 1. The object, and what Mathlib `51e6992e` covers

### 1.1 The object, quoted from the contract (never from memory)

FORMAT.md §9.2 (lines 515–520), quoting `rh-program/results/ccm-dh-test/dh.py` lines 5–8:

```
f_DH(s) = 5^{-s} [ zeta(s,1/5) + kap*zeta(s,2/5) - kap*zeta(s,3/5) - zeta(s,4/5) ]
kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)
```

"(Hurwitz zetas; kap = tan θ with ε_χ = e^{2iθ} = τ(χ)/(i√5), χ mod 5, χ(2) = i — same file.) f_DH is ENTIRE (no pole anywhere …)". Re-read from `dh.py` itself this session: identical text. Numerically κ = 0.28407904… (√5 = 2.2360680, 10 − 2√5 = 5.5278640, √ = 2.3511410, −2 = 0.3511410, ÷ 1.2360680); the builder must reproduce this figure from the Lean definition's real value by an mpmath one-liner before anything else — it is the cheapest possible guard against a transcription slip in `kappaDH` (risk R2).

The live-fire rectangle, from the on-disk literals (`Instances.lean` `mpDH`/`arbDH`): R = [4/5, 41/50] × [8569/100, 8571/100], m = 1, containing ρ_DH = 0.808517182456637 + 85.699348485377592i in its interior. Both legs accepted (acceptance-report §3), both kernel-accepted as checker instances (`mpDH_check`, `arbDH_check : checkW1Floor … = true := by decide +kernel`).

### 1.2 Mathlib declarations checked (source read at the pinned commit; docs site not needed)

Commit: `51e6992efd06126df61a496bebf8f49482a4e129` (Mon Aug 3 2026), from `git log -1` inside `~/rh-lean-work/zeta-23-lean-main/.lake/packages/mathlib`. Oleans for `Mathlib/NumberTheory/LSeries/HurwitzZeta*` are already built in that tree (no Mathlib compile is needed).

| declaration | file:line | statement (condensed) | relevance |
|---|---|---|---|
| `HurwitzZeta.hurwitzZeta (a : UnitAddCircle) (s : ℂ) : ℂ` | `HurwitzZeta.lean:52` | `:= hurwitzZetaEven a s + hurwitzZetaOdd a s` | the object; domain ALL of ℂ (junk value at s = 1, see below) |
| `HurwitzZeta.hurwitzZetaEven (a : UnitAddCircle) : ℂ → ℂ` | `HurwitzZetaEven.lean:583` | `Function.update (fun s ↦ completedHurwitzZetaEven a s / Gammaℝ s) 0 (if a = 0 then -1/2 else 0)` | Mellin-transform construction; meromorphic with the pole at s = 1 |
| `HurwitzZeta.hurwitzZetaOdd (a : UnitAddCircle) (s : ℂ) : ℂ` | `HurwitzZetaOdd.lean:458` | `:= completedHurwitzZetaOdd a s / Gammaℝ (s + 1)` | entire |
| `differentiableAt_hurwitzZeta (a) {s} (hs : s ≠ 1) : DifferentiableAt ℂ (hurwitzZeta a) s` | `HurwitzZeta.lean:66` | analytic away from s = 1 | the per-term fact; NOT enough alone (pole at 1) |
| `differentiable_hurwitzZeta_sub_hurwitzZeta (a b : UnitAddCircle) : Differentiable ℂ (fun s ↦ hurwitzZeta a s - hurwitzZeta b s)` | `HurwitzZeta.lean:103` | the difference is entire | **the pole cancellation, off the shelf** — exactly the lemma f_DH needs, since f_DH = 5^{−s}[(ζ(·,1/5) − ζ(·,4/5)) + κ(ζ(·,2/5) − ζ(·,3/5))] |
| `differentiable_hurwitzZetaEven_sub_hurwitzZetaEven`, `differentiable_hurwitzZetaOdd` | `HurwitzZetaEven.lean:652`, `HurwitzZetaOdd.lean:466` | the two halves of the previous line | not consumed directly |
| `hurwitzZeta_residue_one (a) : Tendsto (fun s ↦ (s - 1) * hurwitzZeta a s) (𝓝[≠] 1) (𝓝 1)` | `HurwitzZeta.lean:82` | residue 1 for every a | why the four-term combination with coefficients 1 + κ − κ − 1 = 0 is entire; not consumed (the difference lemma already encodes it) |
| `hasSum_hurwitzZeta_of_one_lt_re {a : ℝ} (ha : a ∈ Icc 0 1) {s} (hs : 1 < re s) : HasSum (fun n : ℕ ↦ 1 / (n + a : ℂ) ^ s) (hurwitzZeta a s)` | `HurwitzZeta.lean:72` | the Dirichlet series on Re s > 1 | **the convention anchor** (§1.3) |
| `tendsto_hurwitzZeta_sub_one_div_nhds_one` | `HurwitzZeta.lean:96` | `hurwitzZeta a 1` is the limit of `hurwitzZeta a s − 1/((s−1)·Gammaℝ s)` | says what the junk value at s = 1 is; it is the value that makes differences continuous there, so `fDH 1` in Lean is the true entire value (irrelevant to any transcript anyway: C2c keeps σ₂ < 1) |
| `UnitAddCircle := AddCircle (1 : ℝ)` | `Topology/Instances/AddCircle/Real.lean:48` | ℝ/ℤ | the parameter type; the cast `((1/5 : ℝ) : UnitAddCircle)` is the form to use (risk R3) |

What is MISSING in Mathlib: nothing that this theorem needs. There is no `fDH`, no κ, no Davenport–Heilbronn anything — those are the program's ~15 lines of definitions. There is no statement that f_DH has an off-line zero (there never will be one in Mathlib; that is what the transcript certifies, modulo H-ENCL). The differentiability of `fun s ↦ (5 : ℂ) ^ (-s)` is `Differentiable.const_cpow` with `Or.inl (by norm_num : (5 : ℂ) ≠ 0)` — probed.

### 1.3 The convention check (standing order 5: the silent-error class)

Three conventions must agree: Mathlib's `hurwitzZeta`, mpmath's `mp.zeta(s, a)`, and Arb's `acb_hurwitz_zeta` as called by the two producers. They do, at the API level, on the half-plane where all three are defined by a series; uniqueness of analytic continuation carries the identity everywhere else.

* **Mathlib:** `hasSum_hurwitzZeta_of_one_lt_re`: for a ∈ [0, 1] (as a real, cast to ℝ/ℤ) and Re s > 1, `hurwitzZeta a s = Σ_{n ≥ 0} 1/(n + a)^s`. Parameter normalized to a ∈ [0, 1]; the function is 1-periodic in a. For a = j/5, j = 1..4, this is Σ_{n≥0} (n + j/5)^{−s}, the classical Hurwitz series (probed with a = 1/5: Appendix A, the `example`).
* **mpmath leg:** `hurwitz_encl.py` line 19 defines the object it encloses as "zeta(s, a) := sum_{n=0}^{infty} (n+a)^{-s}" continued by Euler–Maclaurin (Z′) on {σ > −2m, s ≠ 1}, with the validation reference `mp.zeta(s, a)` (lines 38–39, 63–67, "mpmath's mp.zeta(s, a) implements this same continuation"); `producer_mp.py` lines 128–144 build f_DH from `hurwitz_ball(s, Fraction(j, 5))`, j = 1..4, with κ as a directed-rounded surd interval and 5^{−s} as an interval power. mpmath's documented convention for `zeta(s, a)` is Σ_{n≥0} (n + a)^{−s}. Same series, same a-normalization (a = j/5 ∈ (0, 1]).
* **Arb leg:** `producer_arb.py` lines 242–246: `s.zeta(acb(rat_ball(Fraction(j, 5))))` — python-flint's `acb.zeta(a)` is `acb_hurwitz_zeta(s, a)`, documented as Σ_{n≥0} (n + a)^{−s} (Arb: "the Hurwitz zeta function ζ(s, a) = Σ_{k=0}^∞ 1/(k+a)^s"). Same series, same a.

Consequently the producers' f_DH and Lean's `fDH` are the same entire function; the identification is a META-level fact (not in Lean), of exactly the same standing as "mpmath's `zeta(s)` / Arb's `acb_zeta` is Mathlib's `riemannZeta`" on the ζ leg. It is where H-ENCL_DH's meaning lives, and it must be written in the theorem's docstring and in the fidelity ledger, not assumed. One genuine subtlety, harmless here: Mathlib assigns `hurwitzZeta a 1` a junk value and `hurwitzZetaEven a 0` a special value; neither point can lie on or inside a W1 rectangle (½ < σ₁, σ₂ < 1, C2), so no transcript row can touch them.

## 2. The soundness twin: what is ζ-specific, what is generic

### 2.1 The split, by file (mirror `lean/Zeta23/W1/`, read in full this session)

| file | lines | ζ-specific content | generic in f |
|---|---|---|---|
| `Format.lean` | ~110 | none. `W1Data` has NO `function` field: the JSON `function` tag (like `mode`, FORMAT §12.5) is dropped at the JSON→Lean boundary; the function enters ONLY through the hypothesis `W1EnclOK f d` | everything |
| `Checker.lean` | ~170 | none (FORMAT §9.2: "C1–C11 mention no function") | everything |
| `Soundness.lean` | 1262 | (a) `continuousOn_zeta_logDeriv_seg` (lines 879–901, 25 lines): continuity of the edge integrand, proved from `differentiableAt_riemannZeta` on U = {Re s < 1}; consumed four times inside `cert_of_checkW1` (lines ~1003–1058, the `hcontB/R/T/L` blocks, whose first argument `hre` proves the segment lies in {Re < 1} from `hs2lt1`); (b) the `hdiff : DifferentiableOn ℂ riemannZeta {s | s.re < 1}` block (lines 1114–1119, 6 lines) passed to H-AP; (c) the statement and docstring of `cert_of_checkW1` (lines 922–932), which name `riemannZeta` | §1–§8 and §10–§11 entirely: the real/complex reading of the data, `RowEnclOK`/`W1EnclOK f`/`RectArgPrinciple f` (all already parameterized by `f`), cross-multiplication soundness, checker unpacking, mesh covering, L1 additivity (`edge_sum_eq` takes the continuity fact as an argument), `pin_m`, `floor_of_checkW1Floor {f}` (already generic) |
| `ArgPrincipleBridge.lean` | 459 | `rectArgPrinciple_riemannZeta` (2 lines, an instantiation) and `cert_of_checkW1_ap` (statement names `riemannZeta`, 1-line proof) | `rectArgPrinciple_of_local : ∀ f, RectArgPrinciple f` and every lemma above it — the header says it: "No ζ-specific fact is consumed anywhere in this file" |
| `Instances.lean` | 3265 | none; `mpDH`, `arbDH` are `W1Data` literals with `mpDH_check`, `arbDH_check : checkW1Floor … = true := by decide +kernel` | consumable UNCHANGED: `(checkW1Floor_spec mpDH_check).1 : checkW1 mpDH = true` (probed, Appendix B) |

So the soundness proof is generic in `f` in all but ~31 lines, and those 31 lines are the two instances of one generic lemma:

```lean
lemma continuousOn_logDeriv_seg_of_diffOn {f : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hf : DifferentiableOn ℂ f U) {z w : ℂ}
    (hin : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → segPt z w t ∈ U)
    (hnz : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → f (segPt z w t) ≠ 0) :
    ContinuousOn (fun t : ℝ => (deriv f (segPt z w t) / f (segPt z w t)) * (w - z)) (Set.Icc 0 1)
```

which probed clean against the built `ArgPrincipleBridge` olean (Appendix B, 2 s, standard axioms), together with the check that the ζ lemma is its instance at U = {Re < 1}.

### 2.2 The two implementation routes, and the recommended one

**Route G (generalize in place; RECOMMENDED).** In `Soundness.lean`: add the generic lemma above (or replace §9 by it); restate `cert_of_checkW1` as

```lean
theorem cert_of_checkW1_of_diffOn (f : ℂ → ℂ) (hf : DifferentiableOn ℂ f {s : ℂ | s.re < 1})
    (d : W1Data) (hc : checkW1 d = true) (hEncl : W1EnclOK f d) (hAP : RectArgPrinciple f) : …
```

with the proof body unchanged except `riemannZeta` → `f` (mechanical, ~40 occurrences), the four `hcont*` blocks calling the generic lemma with `hin` := the existing `hre` proof composed with membership, and the `hdiff` block deleted (it IS `hf`). Then `cert_of_checkW1` (ζ, both hypotheses) is a 3-line instance with the SAME name and SAME statement as today — no downstream statement changes; `cert_of_checkW1_ap` in the bridge is untouched. Diff ≈ 60 lines. Cost: `Soundness.lean` is imported by `ArgPrincipleBridge` → `DBN/BarrierCert` → the 116 DBN modules → `Solution.DBN`, so ONE full `lake build Zeta23` (397 s on record, README line 304) plus `lake build Solution.DBN` (54 s) and the PrintAxioms rerun; no DBN SOURCE changes, so the packaged comparator's hashes and fidelity ledger are unaffected (the checker re-run is a 1-minute confirmation, not a re-package). The v1 audit (`AUDIT.md`) covered `Soundness.lean` line by line; an Opus re-read of the ~60-line diff is part of the price below.

**Route N (new file, no edit to `Soundness.lean`).** Copy the 230-line body of `cert_of_checkW1` into a new generic theorem in a new file. Rejected: duplicates an audited proof, doubles the audit surface, and the copy drifts.

Either route then adds ONE new file (proposed name `Zeta23/W1/DavenportHeilbronn.lean`, importing `ArgPrincipleBridge` and `Instances`): `kappaDH`, `fDH`, `differentiable_fDH` (Appendix A, 12 lines), `cert_of_checkW1_fDH` (§3, from `cert_of_checkW1_of_diffOn fDH differentiable_fDH.differentiableOn d hc hEncl (rectArgPrinciple_of_local fDH)`), and two instance corollaries `mpDH_zero`, `arbDH_zero` (each: the existential conclusion for the literal, with `hEncl : W1EnclOK fDH mpDH` displayed). ≈ 150 lines including the program header, the trust-vocabulary docstring, and the convention paragraph of §1.3 verbatim.

### 2.3 What `Instances.lean` and the JSON side need

* `Instances.lean`: nothing. The two literals and their `_check` theorems are consumed as they stand (Appendix B). Not a single row is re-emitted.
* Producers, checkers, on-disk transcripts: no computation. ONE text-level change is forced by honesty, not by Lean: FORMAT §9.2 fixes the f_DH `trust_label` string ("checker-level only (D-R8): format-checked modulo H-ENCL for f_DH; no Lean-backed conclusion") and calls it schema-enforced; once the theorem exists that string is false. Price: a dated amendment to FORMAT §9.2 (the "Scope, per D-R8" paragraph), the `trust_label` constant in `w1-schema.json`, `TRUST_LABELS["f_DH"]` in `producer_mp.py`/`producer_arb.py`, the banner strings in `checker_ref.py`/`reference_checker.py`, and the two on-disk DH JSONs' label fields (the label is outside the checked arithmetic and outside `W1Data`, so the Lean literals do not change; re-run both Python checkers and `recon_instances_verify.py` afterward — minutes). New string, proposed: `kernel-checked modulo displayed hypothesis H-ENCL for f_DH (producers untrusted); no conclusion about zeta`. Leaving two labels for one object (old in the JSON, new in Lean) is precisely the silent inconsistency standing order 5 exists for, so the text change is in the price, not optional.

## 3. The theorem, verbatim (proposed), and its honest label

### 3.1 Proposed statement (10 lines of Lean; names provisional, shape binding)

```lean
/-- f_DH := 5^{-s}[ζ(s,1/5) + κ ζ(s,2/5) − κ ζ(s,3/5) − ζ(s,4/5)], FORMAT.md §9.2; entire. -/
def fDH (s : ℂ) : ℂ := (5 : ℂ) ^ (-s) *
  (hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) s + (kappaDH : ℂ) * hurwitzZeta ((2/5 : ℝ) : UnitAddCircle) s
    - (kappaDH : ℂ) * hurwitzZeta ((3/5 : ℝ) : UnitAddCircle) s - hurwitzZeta ((4/5 : ℝ) : UnitAddCircle) s)

theorem cert_of_checkW1_fDH (d : W1Data) (hc : checkW1 d = true) (hEncl : W1EnclOK fDH d) :
    (1 ≤ d.m → ∃ ρ : ℂ, fDH ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ T1 d < ρ.im ∧ ρ.im < T2 d)
    ∧ (d.m = 0 → ∀ s ∈ W1Rect d, fDH s ≠ 0)
```

with `kappaDH : ℝ := (Real.sqrt (10 - 2 * Real.sqrt 5) - 2) / (Real.sqrt 5 - 1)` (§9.2 verbatim; both radicands positive and the denominator nonzero, so no `Real.sqrt`/division junk enters). The instance corollary for the live fire:

```lean
theorem mpDH_zero (hEncl : W1EnclOK fDH mpDH) :
    ∃ ρ : ℂ, fDH ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1 ∧ (8569/100 : ℝ) < ρ.im ∧ ρ.im < 8571/100 :=
  (cert_of_checkW1_fDH mpDH (checkW1Floor_spec mpDH_check).1 hEncl).1 (by decide)
```

(and `arbDH_zero` likewise; `T1 mpDH` unfolds to `(8569 : ℝ)/100` — the builder may keep `T1 mpDH` in the statement to stay literal). Expected `#print axioms`: `[propext, Classical.choice, Quot.sound]` for all three (the probes of both halves report exactly these).

### 3.2 The honest label (binding wording, to be used everywhere it is printed)

**[SUPERSEDED 04:18 IST 2026-09-10, Session 20 — after the Opus check (`CHECK-fDH-O.md` §12 item 1).]** The sentence below overclaimed the box: the theorem as shipped concludes `1/2 < Re ρ < 1 ∧ T1 d < Im ρ < T2 d`, not Re ρ ∈ [σ₁, σ₂]. The binding label is now the one in `BUILD-NOTES-fDH.md` §7 / `Zeta23/W1/FDH.lean`'s module doc: "f_DH has at least one zero ρ with 1/2 < Re ρ < 1 and 85.69 < Im ρ < 85.71 (the live-fire window; the transcript's rectangle is R = [4/5, 41/50] × [85.69, 85.71]) — kernel-checked modulo the displayed hypothesis H-ENCL_DH (producers untrusted)." The box-form conclusion is OWED as a σ-strong sibling `cert_of_checkW1_of_diffOn'` (fidelity item (m)). Text below kept as written.


**"f_DH has at least one zero in R = [4/5, 41/50] × [85.69, 85.71] with Re s > 1/2 — kernel-checked modulo the displayed hypothesis H-ENCL_DH (the two producers' enclosures of f_DH on ∂R are true; producers untrusted)."**

What it says: the W1 checker's acceptance of the DH transcript is now a Lean-backed implication for f_DH, of the same shape and the same trust boundary as the ζ theorem `cert_of_checkW1_ap`. The DH rung of the ladder (KICKSTART 10(b): "Davenport–Heilbronn (RH false)") carries the same theorem as the ζ rung; the "checker-level only" caveat of D-R8 is discharged.

What it does NOT say — and must never be read as:
* nothing about ζ: no zero of ζ, nothing about RH, no change to any ζ transcript's label;
* nothing about Λ: the de Bruijn–Newman chain (direction file line 33) runs from a zero of ζ (or of H_t), never from f_DH; f_DH is not in the Λ family;
* not "RH-for-DH machine-checked disproof": "RH for DH" is the (false) statement that ALL zeros of f_DH in the strip lie on Re s = ½; the theorem exhibits ONE off-line zero modulo H-ENCL_DH, which is the witness direction only, and the witness's truth is still the producers' (H-ENCL_DH is displayed, not proved);
* not "fully machine-checked": H-ENCL_DH is where mpmath/Arb enter, exactly as H-ENCL does for ζ;
* not a Mathlib fact about Davenport–Heilbronn: `fDH`, `kappaDH`, and the identification with the producers' function (§1.3) are the program's, and the identification is a documented meta-level convention match, not a Lean theorem.

## 4. Price, risks, GO/NO-GO

### 4.1 Price

| item | agent-sessions | Lean | wall | thermal |
|---|---|---|---|---|
| Builder (plan + build, Route G): generic lemma, `cert_of_checkW1_of_diffOn`, ζ re-instantiated under its old name, new `DavenportHeilbronn.lean`, `#print axioms`, README + FORMAT §9.2 amendment + label strings + JSON label fields + Python checker re-runs + back-parse re-run | 1 (Fable-class; the analytic content is already probed, so this is mechanical editing plus one rebuild) | ≈ 60 lines changed in `Soundness.lean`; ≈ 150 new lines | 2–4 h including one full `lake build Zeta23` (≈ 7 min on record) and `lake build Solution.DBN` + PrintAxioms (≈ 1 min) | one lake process; the full-tree build is one "heavy job" for ≈ 7 min (lake fans out over cores internally; counts as 1 of the 4 allowed) |
| Independent checker (Opus, standing order 5 / 10(f)): clean-clone rebuild, `#print axioms` on the three new theorems and the re-instantiated ζ theorem, line-read of the ~60-line diff against the audited v1, statement read against FORMAT §9.2, κ numeric reproduction, convention paragraph check (§1.3), label-string sweep | 1 (short) | 0 | ≈ 1 h + one clean-clone build (397 s) | one lake process |
| Packaging per 10(j) (challenge/solution pair, `formalization.yaml` entry, fidelity row "producers' f_DH = Lean `fDH` is a documented convention match") | 0 now: W1 itself (the ζ theorem) is NOT yet packaged as a comparator topic — only DBN is (Session 20). The f_DH twin joins the W1 packaging item as +3 statements; pricing that item is not this brief's | — | — | — |
| Producer compute | 0 (no new transcript; `mpDH`/`arbDH` consumed as they stand) | — | — | — |
| **Total** | **2 agent-sessions** (≈ 1.5 in effort) | **≈ 60 changed + ≈ 150 new** | **about half a working day, sequential** | **2 short single-lake-process builds** |

For calibration: v1.1 (the H-AP discharge) was priced at "½–1 session + 1–3 sessions" (RUN-REPORT §3) and landed in one session with a port, a discharge, and an audit agent (direction file, 2026-09-02). This item is smaller than v1.1's discharge alone: the argument principle it needs is v1.1's own output, and the entirety proof is 12 lines.

### 4.2 Risk list

* **R1 — convention mismatch (the silent-error class; standing order 5).** Checked at the API level in §1.3: all three (`hasSum_hurwitzZeta_of_one_lt_re`, `hurwitz_encl.py` line 19 / `mp.zeta`, `acb.zeta(a)`) are Σ_{n≥0}(n+a)^{−s} with a = j/5 ∈ (0, 1). Residual risk: none found; the checker re-derives it independently (that is the audit's second item). Mitigation in the artifact: the convention paragraph goes in the Lean docstring and the fidelity row, so the identification is visible, not assumed.
* **R2 — a slip in `kappaDH`.** One transcription; caught by the mpmath one-liner (κ = 0.28407904…) that the builder runs first and the checker repeats. If κ were wrong the theorem would be a true theorem about a different entire function while the transcript enclosed the real f_DH — H-ENCL_DH would then be false and nothing would detect it in Lean. Hence the numeric reproduction is mandatory, not advisory.
* **R3 — the `UnitAddCircle` cast.** `((1/5 : ℝ) : UnitAddCircle)` is the probed form; `(1/5 : UnitAddCircle)` does not mean the same thing (there is no division on ℝ/ℤ). The builder copies the probe verbatim.
* **R4 — the function tag lives only in the hypothesis.** `W1Data` has no `function` field, so Lean would equally accept the STATEMENT `cert_of_checkW1_ap mpDH … (hEncl : W1EnclOK riemannZeta mpDH)` — a theorem with a false hypothesis about a DH transcript. Nothing new: this is the v1 design (the tag is enforced by producers and Python checkers, FORMAT §12.5), but the DH twin makes the confusion easier to write. Mitigation: the instance corollaries name `fDH` in their statements, and the fidelity row records that the JSON `function` tag is not represented in `W1Data`.
* **R5 — rebuild cascade.** Route G re-elaborates `Soundness` → `ArgPrincipleBridge` → `BarrierCert` → 116 DBN modules → `Solution.DBN`. Sources under DBN and the comparator do not change; their recorded SHA-256s stay valid; the comparator run is re-executed as a 1-minute confirmation. If the orchestrator wants zero risk to the packaged topic, Route N avoids the cascade at the cost of a duplicated proof; not recommended.
* **R6 — Mathlib drift.** The theorem pins `51e6992e`; `differentiable_hurwitzZeta_sub_hurwitzZeta` has been in Mathlib since 2024 and is stable. No risk at the pinned commit (probed).
* **R7 — the label sweep is missed.** If the FORMAT/schema/producer/checker strings are not updated in the same unit, the repository carries two contradictory labels for one object. The builder's checklist ends with a `grep -rn "checker-level only"` over `results/d1-m1/` and `lean/`.
* **R8 — scope creep toward H_t.** FORMAT §9.2's last sentence ("Future function tags (e.g. H_t slices for M2a) enter only by a version bump") will tempt a builder to generalize the JSON `function` enum now. Out of scope: this item adds one theorem and one label string; no contract version bump, no new function tag.

### 4.3 What it is, honestly

An instrument-hardening item. It closes a standing "unpriced work" note (D-R8, direction file line 143; FORMAT §9.2 lines 528–530), and it makes the W1 soundness theorem generic in `f` — which any future function tag (H_t slices, or Gomila's M2a′ row if it ever needs W1 form) would require anyway. It carries no mathematical signal about ζ or Λ: Davenport–Heilbronn has been known to have off-line zeros since 1936, and the theorem re-proves one instance of that modulo producers' enclosures. It is a "Lean-checked statement" in the letter of 10(d), but not in its spirit: 10(d) reallocates budget to results that change what the program believes; this changes only how well an already-accepted test is certified.

### 4.4 GO/NO-GO against KICKSTART 10(d)

**GO — bounded, low priority, instrument-hardening; does NOT trigger 10(d).** Two agent-sessions, no producer compute, two short builds, and the analytic content already probed to standard axioms (Appendices A–B) — this is about the cheapest Lean unit the program has priced. It pulls nothing from anything with signal: it is sequenced into a slot when no signal-bearing lane is waiting on the agent budget (after the M3 ledger decision and the Gomila M2a′ decision are taken, whichever of those the orchestrator runs), and it blocks nothing. It must NOT be treated as a 10(d) trigger when it lands: no lane pauses for its follow-ups, because it has none beyond the label sweep and the (separate, unpriced here) W1 packaging item. If the orchestrator prefers to defer, the named trigger for GO-later is: "before the W1 instrument is packaged or circulated (10(j)), so that the DH rung and the ζ rung of the ladder ship with the same theorem shape and no `checker-level only` caveat has to be explained to a referee." NO-GO is not recommended: leaving D-R8 open costs a standing caveat in every W1 write-up for a saving of about one agent-day.

## 5. Refutation-shaped close (KICKSTART 10(c))

1. **Mathlib coverage holds.** At `51e6992e`, `HurwitzZeta.hurwitzZeta` is defined on all of ℂ, `differentiableAt_hurwitzZeta` gives analyticity off s = 1, and `differentiable_hurwitzZeta_sub_hurwitzZeta` gives the pole cancellation; `Differentiable ℂ fDH` is a 12-line theorem with axioms `[propext, Classical.choice, Quot.sound]` (Appendix A). Nothing is missing.
2. **The convention match holds at the API level.** Mathlib (`hasSum_hurwitzZeta_of_one_lt_re`), mpmath (`hurwitz_encl.py` line 19, `mp.zeta`), and Arb (`acb.zeta(a)`) all realize Σ_{n≥0}(n+a)^{−s}, a = j/5 ∈ (0, 1), on Re s > 1; uniqueness of continuation identifies the three entire f_DH's. The identification is a documented meta-level fact of the same standing as the ζ leg's, never a Lean theorem.
3. **The soundness chain is generic in f except for 31 lines**, all of which are instances of `continuousOn_logDeriv_seg_of_diffOn` (Appendix B). `W1Data` carries no function tag; `mpDH`/`arbDH` and their kernel checks are consumed unchanged. The twin is an instantiation, not a re-proof.
4. **The twin cannot yield any statement about ζ**, because `fDH` and `riemannZeta` share no hypothesis and no conclusion: `W1EnclOK fDH d` and `W1EnclOK riemannZeta d` are different propositions about the same integers, and only the former is asserted by the DH producers.
5. **The twin cannot yield any statement about Λ**, because the de Bruijn–Newman chain (direction file line 33) starts from a zero of ζ or of H_t, and f_DH is neither.
6. **The twin cannot yield "RH-for-DH disproved, machine-checked"**, because H-ENCL_DH is displayed and unproved: the zero's existence is the producers' assertion, kernel-checked only in its consequences. The licensed sentence is §3.2's, no shorter.
7. **The item cannot trigger 10(d)**, because it changes no belief of the program: it certifies, to a better standard, a test whose outcome (a checker-level true positive) was already accepted on 2026-08-27 and kernel-accepted on 2026-09-02. Reallocation is for results with signal; this has none.
8. **The price holds**: 2 agent-sessions, ≈ 60 changed + ≈ 150 new Lean lines, two single-process builds (≈ 7 min + ≈ 7 min clean-clone), zero producer compute — and the only silent-error channels (κ transcription, a-normalization, the label sweep) each have a named, mechanical check in §4.2.
9. **GO holds**, bounded and low priority, sequenced behind whatever the orchestrator decides on the M3 ledger and the Gomila M2a′ decision; GO-later's named trigger is the W1 packaging/circulation step (10(j)).

## Appendix A — probe 1: `fDH` and its entirety against Mathlib `51e6992e` (verbatim; scratchpad, not committed)

Run: `lake env lean probe_fdh.lean` from `~/rh-lean-work/zeta-23-lean-main`, single lake process, no build; wall 2.06 s. Output, in full:

```
'differentiable_fDH' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Source:

```lean
import Mathlib.NumberTheory.LSeries.HurwitzZeta

open HurwitzZeta Complex

noncomputable section

/-- κ = (√(10 − 2√5) − 2)/(√5 − 1), FORMAT.md §9.2 verbatim. -/
def kappaDH : ℝ := (Real.sqrt (10 - 2 * Real.sqrt 5) - 2) / (Real.sqrt 5 - 1)

/-- f_DH(s) = 5^{−s} [ζ(s,1/5) + κ ζ(s,2/5) − κ ζ(s,3/5) − ζ(s,4/5)] (FORMAT.md §9.2). -/
def fDH (s : ℂ) : ℂ :=
  (5 : ℂ) ^ (-s) *
    (hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) s + (kappaDH : ℂ) * hurwitzZeta ((2/5 : ℝ) : UnitAddCircle) s
      - (kappaDH : ℂ) * hurwitzZeta ((3/5 : ℝ) : UnitAddCircle) s - hurwitzZeta ((4/5 : ℝ) : UnitAddCircle) s)

/-- f_DH is entire: the poles at s = 1 cancel pairwise (Mathlib
`differentiable_hurwitzZeta_sub_hurwitzZeta`). -/
theorem differentiable_fDH : Differentiable ℂ fDH := by
  have h14 := differentiable_hurwitzZeta_sub_hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) ((4/5 : ℝ) : UnitAddCircle)
  have h23 := differentiable_hurwitzZeta_sub_hurwitzZeta ((2/5 : ℝ) : UnitAddCircle) ((3/5 : ℝ) : UnitAddCircle)
  have hpow : Differentiable ℂ (fun s : ℂ => (5 : ℂ) ^ (-s)) :=
    Differentiable.const_cpow differentiable_neg (Or.inl (by norm_num))
  have hcomb : Differentiable ℂ (fun s : ℂ =>
      (hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) s - hurwitzZeta ((4/5 : ℝ) : UnitAddCircle) s)
        + (kappaDH : ℂ) * (hurwitzZeta ((2/5 : ℝ) : UnitAddCircle) s - hurwitzZeta ((3/5 : ℝ) : UnitAddCircle) s)) :=
    h14.add (h23.const_mul _)
  have : fDH = fun s => (5 : ℂ) ^ (-s) *
      ((hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) s - hurwitzZeta ((4/5 : ℝ) : UnitAddCircle) s)
        + (kappaDH : ℂ) * (hurwitzZeta ((2/5 : ℝ) : UnitAddCircle) s - hurwitzZeta ((3/5 : ℝ) : UnitAddCircle) s)) := by
    funext s; simp only [fDH]; ring
  rw [this]
  exact hpow.mul hcomb

/-- the series convention on Re s > 1 (for the producer-convention check, §1). -/
example {s : ℂ} (hs : 1 < s.re) :
    HasSum (fun n : ℕ ↦ 1 / (n + (1/5 : ℝ) : ℂ) ^ s) (hurwitzZeta ((1/5 : ℝ) : UnitAddCircle) s) :=
  hasSum_hurwitzZeta_of_one_lt_re (by norm_num) hs

#print axioms differentiable_fDH
end
```

## Appendix B — probe 2: the generic edge-continuity lemma and unchanged consumption of the DH instances (verbatim)

Run: `lake env lean probe_generic.lean` against the built `Zeta23.W1.ArgPrincipleBridge` and `Zeta23.W1.Instances` oleans; single lake process; wall 2.04 s. Output, in full:

```
'Zeta23.W1.continuousOn_logDeriv_seg_of_diffOn' depends on axioms: [propext, Classical.choice, Quot.sound]
```

(The three `example`s — the ζ lemma as an instance at U = {Re < 1}, and `checkW1 mpDH = true`, `checkW1 arbDH = true` from the existing `_check` theorems — elaborate silently, i.e. succeed.) Source:

```lean
import Zeta23.W1.ArgPrincipleBridge
import Zeta23.W1.Instances

open Set Complex MeasureTheory

namespace Zeta23
namespace W1

/-- the generic twin of `continuousOn_zeta_logDeriv_seg`: for any f differentiable on the
open set U ⊇ segment, the edge integrand is continuous on [0,1] given boundary nonvanishing. -/
lemma continuousOn_logDeriv_seg_of_diffOn {f : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hf : DifferentiableOn ℂ f U) {z w : ℂ}
    (hin : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → segPt z w t ∈ U)
    (hnz : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → f (segPt z w t) ≠ 0) :
    ContinuousOn (fun t : ℝ => (deriv f (segPt z w t) / f (segPt z w t)) * (w - z)) (Set.Icc 0 1) := by
  have hA : AnalyticOnNhd ℂ f U := hf.analyticOnNhd hU
  have hdC : ContinuousOn (deriv f) U := hA.deriv.continuousOn
  have hzC : ContinuousOn f U := hA.continuousOn
  have hseg : Continuous fun t : ℝ => segPt z w t := by
    unfold segPt
    exact continuous_const.add (Complex.continuous_ofReal.mul continuous_const)
  have hmaps : Set.MapsTo (fun t : ℝ => segPt z w t) (Set.Icc 0 1) U :=
    fun t ht => hin t ht.1 ht.2
  exact ((hdC.comp hseg.continuousOn hmaps).div (hzC.comp hseg.continuousOn hmaps)
    fun t ht => hnz t ht.1 ht.2).mul continuousOn_const

/-- the ζ lemma is the instance U = {re < 1} (sanity: the generic twin subsumes the original). -/
example {z w : ℂ}
    (hre : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → (segPt z w t).re < 1)
    (hnz : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → riemannZeta (segPt z w t) ≠ 0) :
    ContinuousOn
      (fun t : ℝ => (deriv riemannZeta (segPt z w t) / riemannZeta (segPt z w t)) * (w - z))
      (Set.Icc 0 1) :=
  continuousOn_logDeriv_seg_of_diffOn (isOpen_lt Complex.continuous_re continuous_const)
    (fun s hs => (differentiableAt_riemannZeta (by rintro rfl; simp at hs)).differentiableWithinAt)
    hre hnz

/-- the DH instances can be consumed unchanged: `checkW1 mpDH = true` from the floor theorem. -/
example : checkW1 mpDH = true := (checkW1Floor_spec mpDH_check).1
example : checkW1 arbDH = true := (checkW1Floor_spec arbDH_check).1

#print axioms continuousOn_logDeriv_seg_of_diffOn
end W1
end Zeta23
```

*End of pricing. Nothing outside this file was edited; no build was run; two `lake env lean` probes only.*
