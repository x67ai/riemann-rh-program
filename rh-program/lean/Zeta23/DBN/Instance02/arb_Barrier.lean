/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it.
-/
/-
Zeta23/DBN/Instance02/arb_Barrier.lean — the Arb/FLINT leg (transcripts/row2-arb) Instance02 barrier certificate assembled:
`row2BarrierARB : BarrierData` (72 prisms, 10771 rows, t₀ = 93/500), the chain fact
`row2BarrierARB_chain : checkBarrierChain row2BarrierARB = true` (C-B0 global, C-B2′, C-B13; `decide +kernel`), the split
per-prism fact `row2BarrierARB_prisms : ∀ p ∈ row2BarrierARB.prisms, checkPrism row2BarrierARB.rect p = true` assembled from the
per-prism modules (SPEC.md §7.6), and the monolithic `row2BarrierARB_check : checkBarrier row2BarrierARB = true`.
UNTRUSTED producer data, emitted by results/d1-m2a/emit_lean_m2a.py; the theorems are integer facts.  The
analytic conclusion is `cert_of_checkBarrier` applied to these facts MODULO H2-B and hHol — see Instance02.lean.
-/
import Zeta23.DBN.Instance02.arb_0000
import Zeta23.DBN.Instance02.arb_0001
import Zeta23.DBN.Instance02.arb_0002
import Zeta23.DBN.Instance02.arb_0003
import Zeta23.DBN.Instance02.arb_0004
import Zeta23.DBN.Instance02.arb_0005
import Zeta23.DBN.Instance02.arb_0006
import Zeta23.DBN.Instance02.arb_0007
import Zeta23.DBN.Instance02.arb_0008
import Zeta23.DBN.Instance02.arb_0009
import Zeta23.DBN.Instance02.arb_0010
import Zeta23.DBN.Instance02.arb_0011
import Zeta23.DBN.Instance02.arb_0012
import Zeta23.DBN.Instance02.arb_0013
import Zeta23.DBN.Instance02.arb_0014
import Zeta23.DBN.Instance02.arb_0015
import Zeta23.DBN.Instance02.arb_0016
import Zeta23.DBN.Instance02.arb_0017
import Zeta23.DBN.Instance02.arb_0018
import Zeta23.DBN.Instance02.arb_0019
import Zeta23.DBN.Instance02.arb_0020
import Zeta23.DBN.Instance02.arb_0021
import Zeta23.DBN.Instance02.arb_0022
import Zeta23.DBN.Instance02.arb_0023
import Zeta23.DBN.Instance02.arb_0024
import Zeta23.DBN.Instance02.arb_0025
import Zeta23.DBN.Instance02.arb_0026
import Zeta23.DBN.Instance02.arb_0027
import Zeta23.DBN.Instance02.arb_0028
import Zeta23.DBN.Instance02.arb_0029
import Zeta23.DBN.Instance02.arb_0030
import Zeta23.DBN.Instance02.arb_0031
import Zeta23.DBN.Instance02.arb_0032
import Zeta23.DBN.Instance02.arb_0033
import Zeta23.DBN.Instance02.arb_0034
import Zeta23.DBN.Instance02.arb_0035
import Zeta23.DBN.Instance02.arb_0036
import Zeta23.DBN.Instance02.arb_0037
import Zeta23.DBN.Instance02.arb_0038
import Zeta23.DBN.Instance02.arb_0039
import Zeta23.DBN.Instance02.arb_0040
import Zeta23.DBN.Instance02.arb_0041
import Zeta23.DBN.Instance02.arb_0042
import Zeta23.DBN.Instance02.arb_0043
import Zeta23.DBN.Instance02.arb_0044
import Zeta23.DBN.Instance02.arb_0045
import Zeta23.DBN.Instance02.arb_0046
import Zeta23.DBN.Instance02.arb_0047
import Zeta23.DBN.Instance02.arb_0048
import Zeta23.DBN.Instance02.arb_0049
import Zeta23.DBN.Instance02.arb_0050
import Zeta23.DBN.Instance02.arb_0051
import Zeta23.DBN.Instance02.arb_0052
import Zeta23.DBN.Instance02.arb_0053
import Zeta23.DBN.Instance02.arb_0054
import Zeta23.DBN.Instance02.arb_0055
import Zeta23.DBN.Instance02.arb_0056
import Zeta23.DBN.Instance02.arb_0057
import Zeta23.DBN.Instance02.arb_0058
import Zeta23.DBN.Instance02.arb_0059
import Zeta23.DBN.Instance02.arb_0060
import Zeta23.DBN.Instance02.arb_0061
import Zeta23.DBN.Instance02.arb_0062
import Zeta23.DBN.Instance02.arb_0063
import Zeta23.DBN.Instance02.arb_0064
import Zeta23.DBN.Instance02.arb_0065
import Zeta23.DBN.Instance02.arb_0066
import Zeta23.DBN.Instance02.arb_0067
import Zeta23.DBN.Instance02.arb_0068
import Zeta23.DBN.Instance02.arb_0069
import Zeta23.DBN.Instance02.arb_0070
import Zeta23.DBN.Instance02.arb_0071

namespace Zeta23
namespace DBN
namespace Instance02

set_option maxRecDepth 100000

/-- the Arb/FLINT leg (transcripts/row2-arb) barrier certificate for row 2. -/
def row2BarrierARB : BarrierData where
  rect := row2Rect
  t0n := 93
  t0d := 500
  prisms := [arb0000, arb0001, arb0002, arb0003, arb0004, arb0005, arb0006, arb0007, arb0008, arb0009, arb0010, arb0011, arb0012, arb0013, arb0014, arb0015, arb0016, arb0017, arb0018, arb0019, arb0020, arb0021, arb0022, arb0023, arb0024, arb0025, arb0026, arb0027, arb0028, arb0029, arb0030, arb0031, arb0032, arb0033, arb0034, arb0035, arb0036, arb0037, arb0038, arb0039, arb0040, arb0041, arb0042, arb0043, arb0044, arb0045, arb0046, arb0047, arb0048, arb0049, arb0050, arb0051, arb0052, arb0053, arb0054, arb0055, arb0056, arb0057, arb0058, arb0059, arb0060, arb0061, arb0062, arb0063, arb0064, arb0065, arb0066, arb0067, arb0068, arb0069, arb0070, arb0071]

/-- C-B0 (global), C-B2′, C-B13 for the 72-seam chain: first seam 0, strictly increasing, last seam < t₀. -/
theorem row2BarrierARB_chain : checkBarrierChain row2BarrierARB = true := by decide +kernel

/-- the split per-prism facts, assembled from the per-prism kernel theorems. -/
theorem row2BarrierARB_prisms : ∀ p ∈ row2BarrierARB.prisms, checkPrism row2BarrierARB.rect p = true := by
  intro p hp
  simp only [row2BarrierARB, List.mem_cons, List.not_mem_nil, or_false] at hp
  rcases hp with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  exacts [arb0000_check, arb0001_check, arb0002_check, arb0003_check, arb0004_check, arb0005_check, arb0006_check, arb0007_check, arb0008_check, arb0009_check, arb0010_check, arb0011_check, arb0012_check, arb0013_check, arb0014_check, arb0015_check, arb0016_check, arb0017_check, arb0018_check, arb0019_check, arb0020_check, arb0021_check, arb0022_check, arb0023_check, arb0024_check, arb0025_check, arb0026_check, arb0027_check, arb0028_check, arb0029_check, arb0030_check, arb0031_check, arb0032_check, arb0033_check, arb0034_check, arb0035_check, arb0036_check, arb0037_check, arb0038_check, arb0039_check, arb0040_check, arb0041_check, arb0042_check, arb0043_check, arb0044_check, arb0045_check, arb0046_check, arb0047_check, arb0048_check, arb0049_check, arb0050_check, arb0051_check, arb0052_check, arb0053_check, arb0054_check, arb0055_check, arb0056_check, arb0057_check, arb0058_check, arb0059_check, arb0060_check, arb0061_check, arb0062_check, arb0063_check, arb0064_check, arb0065_check, arb0066_check, arb0067_check, arb0068_check, arb0069_check, arb0070_check, arb0071_check]

/-- the monolithic checker fact, from the chain fact and the per-prism facts (no second kernel evaluation of
the rows: `List.all_eq_true` turns `prisms.all` into the split fact `row2BarrierARB_prisms`). -/
theorem row2BarrierARB_check : checkBarrier row2BarrierARB = true := by
  unfold checkBarrier
  rw [row2BarrierARB_chain, Bool.true_and, List.all_eq_true]
  exact row2BarrierARB_prisms

end Instance02
end DBN
end Zeta23
