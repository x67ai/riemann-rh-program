#!/usr/bin/env python3
"""gen_prove2me_solutions.py -- emit the Prove2Me-layout SOLUTION files of the WeilContainment topics (Session 30, D5 unit).
usage: gen_prove2me_solutions.py <rh-program/lean/comparator> <prove2me_workspace>
For every challenge theorem `weilContainment_<suffix>` of Challenge/WeilContainment{,One}.lean it writes
  Solutions/Sol_WeilContainment_<suffix>.lean   — imports Definitions.Def_WeilContainment (+ Mathlib), NEVER its own
                                                  Theorems.Thm_ stub (platform rule 2) and no other Thm_ stub either (so the
                                                  local `#print axioms solution` is sorry-free and each file is self-contained);
                                                  the helper lemmas it needs are pasted as `private theorem`s (file-scoped, no
                                                  clash between files); then a top-level `theorem solution` whose statement is
                                                  VERBATIM the challenge statement (platform rule 1) and whose proof is the
                                                  proof of comparator/Solution/WeilContainment{,One}.lean for that theorem.
Nothing is uploaded; nothing here talks to the network."""
import os, re, sys

comp, ws = sys.argv[1], sys.argv[2]

HELPERS = {
"tilt_even": """private theorem tilt_even (a u : ℝ) : tilt a (-u) = tilt a u := by
  simp [tilt, abs_neg]
""",
"tilt_pos": """private theorem tilt_pos (a u : ℝ) : 0 < tilt a u := Real.exp_pos _
""",
"tilt_of_nonneg": """private theorem tilt_of_nonneg (a u : ℝ) (hu : 0 ≤ u) : tilt a u = Real.exp (-(a - 1 / 2) * u) := by
  simp [tilt, abs_of_nonneg hu]
""",
"tilt_mul_tilt": """private theorem tilt_mul_tilt (a u : ℝ) : tilt a u * tilt (1 - a) u = 1 := by
  unfold tilt
  rw [← Real.exp_add]
  have h : -(a - 1 / 2) * |u| + -(1 - a - 1 / 2) * |u| = 0 := by ring
  rw [h, Real.exp_zero]
""",
"summand_eq": """private theorem summand_eq (a : ℝ) (g : ℝ → ℂ) (hg : ∀ u, g (-u) = g u) (n : ℕ) :
    ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) * g (Real.log n)
      = ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ)
          * (weilTestOf a g (Real.log n) + weilTestOf a g (-Real.log n)) := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp
  · have hn' : (0 : ℝ) < n := by exact_mod_cast hn
    have hlog : 0 ≤ Real.log n := Real.log_nonneg (by exact_mod_cast hn)
    have h1 : weilTestOf a g (Real.log n) + weilTestOf a g (-Real.log n)
        = g (Real.log n) * (tilt a (Real.log n) : ℂ) := by
      simp only [weilTestOf, hg, tilt_even]; ring
    have h2 : tilt a (Real.log n) = (n : ℝ) ^ (1 / 2 - a) := by
      rw [tilt_of_nonneg _ _ hlog, Real.rpow_def_of_pos hn']; congr 1; ring
    have h3 : ArithmeticFunction.vonMangoldt n / Real.sqrt n * (n : ℝ) ^ (1 / 2 - a)
        = ArithmeticFunction.vonMangoldt n * (n : ℝ) ^ (-a) := by
      rw [Real.sqrt_eq_rpow, div_eq_mul_inv, ← Real.rpow_neg hn'.le, mul_assoc, ← Real.rpow_add hn']
      congr 2; ring
    have h3' : ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) * (((n : ℝ) ^ (1 / 2 - a) : ℝ) : ℂ)
        = ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) := by
      rw [← Complex.ofReal_mul, h3, Complex.ofReal_mul]
    rw [h1, h2, ← h3']; ring
""",
"identity": """private theorem identity (a : ℝ) (g : ℝ → ℂ) (hg : ∀ u, g (-u) = g u) :
    tiltedPrimeSide a g = primeSide (weilTestOf a g) := by
  unfold tiltedPrimeSide primeSide
  exact tsum_congr (fun n => summand_eq a g hg n)
""",
"support_weilTestOf": """private theorem support_weilTestOf (a : ℝ) (g : ℝ → ℂ) :
    Function.support (weilTestOf a g) = Function.support g := by
  ext u
  simp [weilTestOf, Function.mem_support, (tilt_pos a u).ne']
""",
"tsupport_weilTestOf": """private theorem tsupport_weilTestOf (a : ℝ) (g : ℝ → ℂ) : tsupport (weilTestOf a g) = tsupport g := by
  simp only [tsupport, support_weilTestOf]
""",
"weilTestOf_even": """private theorem weilTestOf_even (a : ℝ) (g : ℝ → ℂ) (hg : ∀ u, g (-u) = g u) (u : ℝ) :
    weilTestOf a g (-u) = weilTestOf a g u := by
  simp only [weilTestOf, hg, tilt_even]
""",
"exact": """private theorem exact (a L : ℝ) (k : ℝ → ℂ) (hk : ∀ u, k (-u) = k u) (hks : tsupport k ⊆ Set.Icc (-L) L) :
    ∃ g : ℝ → ℂ, (∀ u, g (-u) = g u) ∧ tsupport g ⊆ Set.Icc (-L) L ∧ primeSide k = tiltedPrimeSide a g := by
  set g : ℝ → ℂ := fun u => 2 * k u * (tilt (1 - a) u : ℂ) with hgdef
  have hgeven : ∀ u, g (-u) = g u := by
    intro u; simp only [hgdef, hk, tilt_even]
  have hsupp : Function.support g = Function.support k := by
    ext u; simp [hgdef, Function.mem_support, (tilt_pos (1 - a) u).ne']
  refine ⟨g, hgeven, ?_, ?_⟩
  · calc tsupport g = tsupport k := by simp only [tsupport, hsupp]
      _ ⊆ Set.Icc (-L) L := hks
  · rw [identity a g hgeven]
    congr 1
    funext u
    have hc : (tilt a u : ℂ) * (tilt (1 - a) u : ℂ) = 1 := by
      rw [← Complex.ofReal_mul, tilt_mul_tilt, Complex.ofReal_one]
    simp only [weilTestOf, hgdef]
    linear_combination (-(k u)) * hc
""",
}
ORDER = ["tilt_even", "tilt_pos", "tilt_of_nonneg", "tilt_mul_tilt", "summand_eq", "identity", "support_weilTestOf",
         "tsupport_weilTestOf", "weilTestOf_even", "exact"]

# (helpers needed, proof text after `:=`) per challenge theorem suffix
PROOFS = {
"identity_one": (["tilt_even", "tilt_of_nonneg", "summand_eq", "identity"],
    "\n  fun g hg => identity 1 g hg\n"),
"identity": (["tilt_even", "tilt_of_nonneg", "summand_eq", "identity"],
    "\n  fun a g hg => identity a g hg\n"),
"cutoff": ([], """ by
  intro a L g hg
  unfold tiltedPrimeSide
  apply tsum_eq_sum
  intro n hn
  have hn' : ⌊Real.exp L⌋₊ < n := by
    rw [Finset.mem_range, not_lt] at hn; omega
  have hlt : Real.exp L < n := Nat.lt_of_floor_lt hn'
  have hL : L < Real.log n := (Real.lt_log_iff_exp_lt (lt_trans (Real.exp_pos L) hlt)).mpr hlt
  have hg0 : g (Real.log n) = 0 := by
    apply image_eq_zero_of_notMem_tsupport
    intro hmem
    exact absurd (hg hmem).2 (not_le.mpr hL)
  rw [hg0, mul_zero]
"""),
"tilt_bounds": ([], """ by
  intro a L u hu
  unfold tilt
  have h0 : abs (-(a - 1 / 2) * |u|) ≤ |a - 1 / 2| * L := by
    rw [abs_mul, abs_neg, abs_abs]
    exact mul_le_mul_of_nonneg_left hu (abs_nonneg _)
  rw [abs_le] at h0
  exact ⟨Real.exp_le_exp.mpr h0.1, Real.exp_le_exp.mpr h0.2⟩
"""),
"tilt_pos": (["tilt_pos"], "\n  fun a u => tilt_pos a u\n"),
"tilt_inv": (["tilt_mul_tilt"], "\n  fun a u => tilt_mul_tilt a u\n"),
"even": (["tilt_even", "weilTestOf_even"], "\n  fun a g hg u => weilTestOf_even a g hg u\n"),
"tsupport": (["tilt_pos", "support_weilTestOf", "tsupport_weilTestOf"], "\n  fun a g => (tsupport_weilTestOf a g).le\n"),
"tsupport_eq": (["tilt_pos", "support_weilTestOf", "tsupport_weilTestOf"], "\n  fun a g => tsupport_weilTestOf a g\n"),
"continuous": ([], """ by
  intro a g hg
  have ht : Continuous (tilt a) := Real.continuous_exp.comp (continuous_const.mul continuous_abs)
  exact (continuous_const.mul hg).mul (Complex.continuous_ofReal.comp ht)
"""),
"exact": (["tilt_even", "tilt_pos", "tilt_of_nonneg", "tilt_mul_tilt", "summand_eq", "identity", "exact"],
    "\n  fun a L k hk hks => exact a L k hk hks\n"),
"range_eq": (["tilt_even", "tilt_pos", "tilt_of_nonneg", "tilt_mul_tilt", "summand_eq", "identity", "support_weilTestOf",
              "tsupport_weilTestOf", "weilTestOf_even", "exact"], """ by
  intro a L
  ext x
  constructor
  · rintro ⟨g, hg, hgs, rfl⟩
    exact ⟨weilTestOf a g, weilTestOf_even a g hg, (tsupport_weilTestOf a g).le.trans hgs, identity a g hg⟩
  · rintro ⟨k, hk, hks, rfl⟩
    obtain ⟨g, hg, hgs, hgk⟩ := exact a L k hk hks
    exact ⟨g, hg, hgs, hgk⟩
"""),
"not_contDiff": ([], """ by
  intro h
  have hfun : weilTestOf 1 (fun _ => (1 : ℂ)) =
      fun u => ((1 / 2 * Real.exp (-(1 / 2) * |u|) : ℝ) : ℂ) := by
    funext u
    simp only [weilTestOf, tilt]
    push_cast
    ring_nf
  have hd : DifferentiableAt ℝ (weilTestOf 1 (fun _ => (1 : ℂ))) 0 :=
    (h.differentiable (by norm_num)).differentiableAt
  have hre : DifferentiableAt ℝ (Complex.reCLM ∘ weilTestOf 1 (fun _ => (1 : ℂ))) 0 :=
    Complex.reCLM.differentiableAt.comp 0 hd
  have hre' : DifferentiableAt ℝ (fun u : ℝ => 1 / 2 * Real.exp (-(1 / 2) * |u|)) 0 := by
    have : (Complex.reCLM ∘ weilTestOf 1 (fun _ => (1 : ℂ))) =
        fun u : ℝ => 1 / 2 * Real.exp (-(1 / 2) * |u|) := by
      rw [hfun]; funext u; simp only [Function.comp, Complex.reCLM_apply, Complex.ofReal_re]
    rwa [this] at hre
  have hlog : DifferentiableAt ℝ
      (fun u : ℝ => -2 * Real.log (2 * (1 / 2 * Real.exp (-(1 / 2) * |u|)))) 0 := by
    apply DifferentiableAt.const_mul
    apply DifferentiableAt.log
    · exact hre'.const_mul 2
    · have := Real.exp_pos (-(1 / 2) * |(0 : ℝ)|)
      positivity
  have habs : (fun u : ℝ => -2 * Real.log (2 * (1 / 2 * Real.exp (-(1 / 2) * |u|)))) =
      fun u : ℝ => |u| := by
    funext u
    rw [show 2 * (1 / 2 * Real.exp (-(1 / 2) * |u|)) = Real.exp (-(1 / 2) * |u|) by ring, Real.log_exp]
    ring
  rw [habs] at hlog
  exact not_differentiableAt_abs_zero hlog
"""),
}

rx = re.compile(r"^theorem\s+weilContainment_([A-Za-z0-9_']+)\s*(.*?):=\s*by\s*\n\s*sorry", re.S | re.M)
os.makedirs(os.path.join(ws, "Solutions"), exist_ok=True)
count = 0
for chal in ("WeilContainmentOne.lean", "WeilContainment.lean"):
    src = open(os.path.join(comp, "Challenge", chal), encoding="utf-8").read()
    for m in rx.finditer(src):
        suffix, stmt = m.group(1), m.group(2)
        helpers, proof = PROOFS[suffix]
        helpers = [h for h in ORDER if h in helpers]
        body = "".join(HELPERS[h] + "\n" for h in helpers)
        out = ("-- Sol_WeilContainment_%s: the Prove2Me-layout solution of Thm_WeilContainment_%s (theorem\n"
               "-- `WeilContainment.%s` = the comparator challenge theorem `weilContainment_%s` of\n"
               "-- rh-program/lean/comparator/Challenge/%s). Statement VERBATIM; proof = comparator/Solution/%s.\n"
               "-- Self-contained: imports the Definitions bundle only (never its own Thm_ stub, and no other stub), helper lemmas\n"
               "-- pasted as private theorems. Generated by results/d5-lean-s30/tools/gen_prove2me_solutions.py; NOT uploaded.\n"
               "import Definitions.Def_WeilContainment\nimport Mathlib\n\nnoncomputable section\n\nopen WeilContainment\n\n"
               "%stheorem solution %s:=%s") % (suffix, suffix, suffix, suffix, chal, chal, body, stmt, proof)
        with open(os.path.join(ws, "Solutions", "Sol_WeilContainment_%s.lean" % suffix), "w", encoding="utf-8") as f:
            f.write(out)
        count += 1
        print("wrote Solutions/Sol_WeilContainment_%s.lean (helpers: %s)" % (suffix, ", ".join(helpers) or "none"))
print("solution files written:", count)
