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
Zeta23/DBN/Instance02/mp_Barrier.lean — the mpmath-ball leg (transcripts/row2) Instance02 barrier certificate assembled:
`row2BarrierMP : BarrierData` (39 prisms, 7176 rows, t₀ = 93/500), the chain fact
`row2BarrierMP_chain : checkBarrierChain row2BarrierMP = true` (C-B0 global, C-B2′, C-B13; `decide +kernel`), the split
per-prism fact `row2BarrierMP_prisms : ∀ p ∈ row2BarrierMP.prisms, checkPrism row2BarrierMP.rect p = true` assembled from the
per-prism modules (SPEC.md §7.6), and the monolithic `row2BarrierMP_check : checkBarrier row2BarrierMP = true`.
UNTRUSTED producer data, emitted by results/d1-m2a/emit_lean_m2a.py; the theorems are integer facts.  The
analytic conclusion is `cert_of_checkBarrier` applied to these facts MODULO H2-B and hHol — see Instance02.lean.
-/
import Zeta23.DBN.Instance02.mp_0000
import Zeta23.DBN.Instance02.mp_0001
import Zeta23.DBN.Instance02.mp_0002
import Zeta23.DBN.Instance02.mp_0003
import Zeta23.DBN.Instance02.mp_0004
import Zeta23.DBN.Instance02.mp_0005
import Zeta23.DBN.Instance02.mp_0006
import Zeta23.DBN.Instance02.mp_0007
import Zeta23.DBN.Instance02.mp_0008
import Zeta23.DBN.Instance02.mp_0009
import Zeta23.DBN.Instance02.mp_0010
import Zeta23.DBN.Instance02.mp_0011
import Zeta23.DBN.Instance02.mp_0012
import Zeta23.DBN.Instance02.mp_0013
import Zeta23.DBN.Instance02.mp_0014
import Zeta23.DBN.Instance02.mp_0015
import Zeta23.DBN.Instance02.mp_0016
import Zeta23.DBN.Instance02.mp_0017
import Zeta23.DBN.Instance02.mp_0018
import Zeta23.DBN.Instance02.mp_0019
import Zeta23.DBN.Instance02.mp_0020
import Zeta23.DBN.Instance02.mp_0021
import Zeta23.DBN.Instance02.mp_0022
import Zeta23.DBN.Instance02.mp_0023
import Zeta23.DBN.Instance02.mp_0024
import Zeta23.DBN.Instance02.mp_0025
import Zeta23.DBN.Instance02.mp_0026
import Zeta23.DBN.Instance02.mp_0027
import Zeta23.DBN.Instance02.mp_0028
import Zeta23.DBN.Instance02.mp_0029
import Zeta23.DBN.Instance02.mp_0030
import Zeta23.DBN.Instance02.mp_0031
import Zeta23.DBN.Instance02.mp_0032
import Zeta23.DBN.Instance02.mp_0033
import Zeta23.DBN.Instance02.mp_0034
import Zeta23.DBN.Instance02.mp_0035
import Zeta23.DBN.Instance02.mp_0036
import Zeta23.DBN.Instance02.mp_0037
import Zeta23.DBN.Instance02.mp_0038

namespace Zeta23
namespace DBN
namespace Instance02

set_option maxRecDepth 100000

/-- the mpmath-ball leg (transcripts/row2) barrier certificate for row 2. -/
def row2BarrierMP : BarrierData where
  rect := row2Rect
  t0n := 93
  t0d := 500
  prisms := [mp0000, mp0001, mp0002, mp0003, mp0004, mp0005, mp0006, mp0007, mp0008, mp0009, mp0010, mp0011, mp0012, mp0013, mp0014, mp0015, mp0016, mp0017, mp0018, mp0019, mp0020, mp0021, mp0022, mp0023, mp0024, mp0025, mp0026, mp0027, mp0028, mp0029, mp0030, mp0031, mp0032, mp0033, mp0034, mp0035, mp0036, mp0037, mp0038]

/-- C-B0 (global), C-B2′, C-B13 for the 39-seam chain: first seam 0, strictly increasing, last seam < t₀. -/
theorem row2BarrierMP_chain : checkBarrierChain row2BarrierMP = true := by decide +kernel

/-- the split per-prism facts, assembled from the per-prism kernel theorems. -/
theorem row2BarrierMP_prisms : ∀ p ∈ row2BarrierMP.prisms, checkPrism row2BarrierMP.rect p = true := by
  intro p hp
  simp only [row2BarrierMP, List.mem_cons, List.not_mem_nil, or_false] at hp
  rcases hp with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  exacts [mp0000_check, mp0001_check, mp0002_check, mp0003_check, mp0004_check, mp0005_check, mp0006_check, mp0007_check, mp0008_check, mp0009_check, mp0010_check, mp0011_check, mp0012_check, mp0013_check, mp0014_check, mp0015_check, mp0016_check, mp0017_check, mp0018_check, mp0019_check, mp0020_check, mp0021_check, mp0022_check, mp0023_check, mp0024_check, mp0025_check, mp0026_check, mp0027_check, mp0028_check, mp0029_check, mp0030_check, mp0031_check, mp0032_check, mp0033_check, mp0034_check, mp0035_check, mp0036_check, mp0037_check, mp0038_check]

/-- the monolithic checker fact, from the chain fact and the per-prism facts (no second kernel evaluation of
the rows: `List.all_eq_true` turns `prisms.all` into the split fact `row2BarrierMP_prisms`). -/
theorem row2BarrierMP_check : checkBarrier row2BarrierMP = true := by
  unfold checkBarrier
  rw [row2BarrierMP_chain, Bool.true_and, List.all_eq_true]
  exact row2BarrierMP_prisms

end Instance02
end DBN
end Zeta23
