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
Zeta23/DBN/Instance02/Rect.lean — the common rectangle and final time of the Instance02 barrier certificate
(Polymath15 Table 1 row 2, SPEC.md §9): R = [X, X+1] × [y₀, 1] with X = 5 000 000 194 858, y₀ = 16733/100000,
t₀ = 93/500.  Its own small module so that the per-prism modules (SPEC.md §7.6) import it and not the prism list.
Mechanically emitted by results/d1-m2a/emit_lean_m2a.py (UNTRUSTED); verified by verify_lean_m2a.py.
-/
import Zeta23.DBN.BarrierCert

namespace Zeta23
namespace DBN
namespace Instance02

/-- R = [5000000194858/1, 5000000194859/1] × [16733/100000, 1/1] (SPEC.md §9). -/
def row2Rect : RectData :=
  ⟨5000000194858, 1, 5000000194859, 1, 16733, 100000, 1, 1⟩

/-- t₀ = 93/500 as the pair (t0n, t0d). -/
def row2T0n : ℤ := 93
def row2T0d : ℤ := 500

end Instance02
end DBN
end Zeta23
