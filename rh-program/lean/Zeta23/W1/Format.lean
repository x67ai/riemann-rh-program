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
Zeta23/W1/Format.lean — the TRANSCRIPT DATA TYPES of the M1 v1 W1 rectangle-transcript checker
(D1 first deliverable, component 1, under the D-R3 two-displayed-hypotheses rescope).

Binding format contract: rh-program/results/d1-m1/FORMAT.md, v1.0 (2026-08-26), §7.1 — this file
realizes that section's Lean data structures verbatim.  The JSON shape contract is w1-schema.json
(same directory); the JSON→Lean literal translation is producer-side and UNTRUSTED — the kernel
re-checks everything that matters from the literals (Checker.lean), and the analytic meaning of
the fields enters only through the displayed hypotheses (Soundness.lean).

FIELD SEMANTICS (normative statement in FORMAT.md; recalled here for the reader):
  * (p1, q1), (p2, q2), (a1, b1), (a2, b2) — the rectangle R = [σ₁, σ₂] × [T₁, T₂] as exact
    rationals σ₁ = p1/q1, σ₂ = p2/q2, T₁ = a1/b1, T₂ = a2/b2; denominators are checked ≥ 1 by
    the checker (C1), not typed positive — literals stay flat ℤ, per FORMAT.md §7.1.
  * K, A — the value and argument scales (§1): a row asserts reLo ≤ K·Re f ≤ reHi and
    imLo ≤ K·Im f ≤ imHi on the whole closed segment, and argLo ≤ A·(Δ/2π) ≤ argHi with Δ the
    argument increment along the segment (TURN units — π never appears in the transcript).
  * m — the claimed winding number; the JSON `mode` field is intentionally ABSENT here
    (FORMAT.md §12.5): the soundness theorem splits on 1 ≤ m (refutation) vs m = 0 (exclusion).
  * bottom, right, top, left — the boundary mesh (§4): each edge stores its VARYING coordinate
    only, as rational breakpoints (n, d), in the counterclockwise traversal order
    bottom (Re: σ₁ → σ₂ increasing), right (Im: T₁ → T₂ increasing),
    top (Re: σ₂ → σ₁ DEcreasing), left (Im: T₂ → T₁ DEcreasing), endpoints included.
  * rows — one `W1Row` per boundary segment, in the global traversal order (bottom segments,
    then right, top, left); the checker verifies the count (C4).
  * `W1Floor` — the OPTIONAL modulus-floor claim |f| ≥ Fn/Fd on ∂R (§5.2), kept as a separate
    structure per §7.1's note; its check (C11) and soundness are not load-bearing for the W1
    conclusion.

Trust model: this file contains DEFINITIONS ONLY (no proofs, no analysis, no Mathlib imports
beyond the ℤ notation) — it is part of the ~100-line trusted audit surface together with the
hypothesis definitions and the theorem statement in Soundness.lean.
-/
import Mathlib.Data.Int.Notation

namespace Zeta23
namespace W1

/-- Per-segment transcript row (FORMAT.md §2, §7.1): the value box at scale K
(`reLo ≤ K·Re f ≤ reHi`, `imLo ≤ K·Im f ≤ imHi`, for ALL points of the closed segment) and the
argument-increment enclosure at scale A in turn units (`argLo ≤ A·(Δ/2π) ≤ argHi`). -/
structure W1Row where
  reLo : ℤ
  reHi : ℤ
  imLo : ℤ
  imHi : ℤ
  argLo : ℤ
  argHi : ℤ

/-- The W1 rectangle transcript (FORMAT.md §7.1).  All numbers are flat ℤ literals; every
constraint on them (C1–C10) is the checker's, and every analytic assertion about them is a
displayed hypothesis. -/
structure W1Data where
  /-- σ₁ = p1/q1 (left abscissa). -/
  p1 : ℤ
  q1 : ℤ
  /-- σ₂ = p2/q2 (right abscissa). -/
  p2 : ℤ
  q2 : ℤ
  /-- T₁ = a1/b1 (bottom ordinate). -/
  a1 : ℤ
  b1 : ℤ
  /-- T₂ = a2/b2 (top ordinate). -/
  a2 : ℤ
  b2 : ℤ
  /-- value scale K ≥ 1. -/
  K : ℤ
  /-- argument scale A ≥ 1 (turn units). -/
  A : ℤ
  /-- claimed winding number m ≥ 0; the refutation/exclusion mode split is at the theorem level. -/
  m : ℤ
  /-- bottom-edge breakpoints: Re values, σ₁ → σ₂ strictly increasing. -/
  bottom : List (ℤ × ℤ)
  /-- right-edge breakpoints: Im values, T₁ → T₂ strictly increasing. -/
  right : List (ℤ × ℤ)
  /-- top-edge breakpoints: Re values, σ₂ → σ₁ strictly DEcreasing. -/
  top : List (ℤ × ℤ)
  /-- left-edge breakpoints: Im values, T₂ → T₁ strictly DEcreasing. -/
  left : List (ℤ × ℤ)
  /-- per-segment rows, global traversal order (bottom, right, top, left segments). -/
  rows : List W1Row

/-- The OPTIONAL modulus-floor claim (FORMAT.md §5.2): |f| ≥ Fn/Fd on all of ∂R.  Kept as a
separate structure (FORMAT.md §7.1): a transcript with a floor is a `W1Data` plus a `W1Floor`,
checked by `checkW1Floor`; the floor is a certified by-product for other components (M2a's
`BarrierCert` t-interpolation, screen sensitivity), never load-bearing for the W1 conclusion. -/
structure W1Floor where
  Fn : ℤ
  Fd : ℤ

end W1
end Zeta23
