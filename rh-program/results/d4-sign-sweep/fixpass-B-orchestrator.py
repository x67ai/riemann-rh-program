# D4 Job 2 B/C fix pass (orchestrator, Session 26). Applies CHECK-O-B.md's FIX-FIRST items and the cheap MINORs
# to d4-sweep-note.md as tagged corrections, and inserts the three Instruments rows + work-log lines.
# Dry run by default; `--apply` writes. Every replacement asserts a unique match (the s25 lesson: lookups, not indices).
import sys, re, datetime
APPLY = '--apply' in sys.argv
ROOT = "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program"
TAG = "[corrected 2026-09-25, Session 26, CHECK-O-B §C.{s}]"
def rep(text, old, new, n=1):
    c = text.count(old)
    assert c == n, (c, old[:80])
    return text.replace(old, new)
note_p = f"{ROOT}/results/d4-sign-sweep/d4-sweep-note.md"
t = open(note_p, encoding='utf-8').read()
# --- §C.2 numbers
t = rep(t, "| ≤ 2.12·10⁻⁹ at the top of the ladder (k = 120)", f"| ≤ 2.13·10⁻⁹ at the top of the ladder (k = 120) {TAG.format(s=2)}: the record's maximum is 2.124·10⁻⁹, so \"≤ 2.12·10⁻⁹\" was rounded down")
t = rep(t, "(largest line 2.12·10⁻⁹ at k = 120, 9.49·10¹⁹)", "(largest line 2.124·10⁻⁹ at k = 120, 9.49·10¹⁹)")
t = rep(t, "all 121 tier-1 heights (largest 2.12·10⁻⁹)", "all 121 tier-1 heights (largest 2.124·10⁻⁹)")
t = rep(t, "phase-line dominated above ≈ 10¹⁶: 2.1·10⁻⁹ at the top, 1.4·10⁻¹³ at PT's height", f"phase-line dominated above ≈ 10¹⁶: 2.124·10⁻⁹ at the top, 1.4·10⁻¹³ at PT's height ({TAG.format(s=2)}: as bounds, ≤ 2.13·10⁻⁹ and, with the weight-rounding line 4u·ℓ¹ = 9.7·10⁻¹⁵ the table omits, a minimum of 1.5·10⁻¹³; tier 2: ≤ 9.30·10⁻⁹ and 9.6·10⁻¹³ with 6.5·10⁻¹⁴; the Neumaier summation line ≤ 6.3·10⁻¹⁸ / 2.1·10⁻¹⁸ sits under the 10⁻¹⁴ floor; `checker-O/out/budget_check.json`)")
t = rep(t, "value, budget (≤ 2.1·10⁻⁹ at L = 22, ≤ 9.3·10⁻⁹ at L = 28.35)", "value, budget (≤ 2.13·10⁻⁹ at L = 22, ≤ 9.3·10⁻⁹ at L = 28.35)")
t = rep(t, "| 1.3·10⁻¹³ | 8.7·10⁻¹³ | `A_interp_check` |", f"| 1.3·10⁻¹³ | 8.5·10⁻¹³ {TAG.format(s=2)}: the record is 8.479·10⁻¹³, not 8.7·10⁻¹³ | `A_interp_check` |")
t = rep(t, "| ≤ 10⁻¹⁶ | ≤ 10⁻¹⁶ | `conv_h`, `conv_H` |", f"| ≤ 5.6·10⁻¹⁶ {TAG.format(s=2)}: the tier-1 maximum is 5.55·10⁻¹⁶ (k = 36), not ≤ 10⁻¹⁶ | ≤ 10⁻¹⁶ (record ≤ 6.9·10⁻¹⁷) | `conv_h`, `conv_H` |")
t = rep(t, "| ≤ 2.6·10⁻²⁰ (r = 85.7 … 10²⁰) | same |", f"| ≤ 2.8·10⁻²⁰ (worst 2.73·10⁻²⁰ at t = 533 515 002 082 491, k = 36, L = 22; {TAG.format(s=2)}: \"≤ 2.6·10⁻²⁰\" held at the rehearsal points, not over the sweep) | ≤ 2.7·10⁻²⁰ (worst 2.616·10⁻²⁰) |")
t = rep(t, "(6) not fired (two paths agree to ≤ 2.6·10⁻²⁰ up to r = 10²⁰)", f"(6) not fired (two paths agree to ≤ 2.8·10⁻²⁰ over the sweep {TAG.format(s=2)}, ≤ 2.6·10⁻²⁰ at the rehearsal points up to r = 10²⁰)")
t = rep(t, "(6) not fired (two-path bracket ≤ 2.6·10⁻²⁰ up to r ≈ 6·10¹⁹ at the sweep's points and r = 10²⁰ in the rehearsal)", f"(6) not fired (two-path bracket ≤ 2.8·10⁻²⁰ at the sweep's points {TAG.format(s=2)} and ≤ 2.6·10⁻²⁰ up to r = 10²⁰ in the rehearsal)")
t = rep(t, "| ≤ 10^{−555 280} at 10¹², smaller above | ≤ 10^{−661 116} |", "| ≤ 10^{−555 280} at 10¹², smaller above (sweep worst 10^{−1 008 780} at k = 0) | ≤ 10^{−661 116} (sweep worst 10^{−1 145 152} at the PT edge) |")
# --- §C.3 coverage measure
t = rep(t, "Total measure 2.75·10⁹ in t — **a fraction 2.7·10⁻¹¹ of the range**", f"Total measure (union) 2.72·10⁹ in t — **a fraction 2.7·10⁻¹¹ of the range** ({TAG.format(s=3)}: the plain sum 2.75·10⁹, which is what `sweep_plan.json` v2 stores as `covered_measure_in_t`, counts the five Odlyzko 1992 sets that overlap Gourdon's windows twice; the JSON is left as landed and its key means the sum of window lengths; `checker-O/out/coverage_check_B.json`)")
# --- §C.4 visibility sentences + MINORs
t = rep(t, "δ = ¼ is visible at every point of both tiers; δ = 0.1 is visible at L = 28.35 only up to ≈ 3·10¹² (δ_vis = 0.1013 at the PT edge and rises to 0.1276 at the ceiling) and at no point of tier 1",
        f"δ = ¼ is visible at every point of both tiers (at the law's central value; within the factor-1.5 band at L = 28.35 only); δ = 0.1 is visible at no sweep point: δ_vis(t, 28.35) = 0.1 at t ≈ 1.5·10¹², below PT's height (δ_vis = 0.1013 at the PT edge, rising to 0.1276 at the ceiling; 0.0993 at the (10¹², 28.35) rehearsal point, inside PT's range) {TAG.format(s=4)}; δ_vis is the campaign's law (measured over 10³ ≤ t ≤ 10⁶, IV.9 rider 2026-09-24) extrapolated to 3·10¹²–9.5·10¹⁹ `[inferred: extrapolation, 6.5–14 decades; the factor-1.5 band is the in-range tolerance]` {TAG.format(s=5)}")
t = rep(t, "δ = ¼ visible everywhere in both tiers, δ = 0.1 visible only at L = 28.35 up to ≈ 3·10¹²", f"δ = ¼ visible everywhere in both tiers at the law's central value (within the factor-1.5 band at L = 28.35 only), δ = 0.1 visible at no sweep point (at L = 28.35 only below t ≈ 1.5·10¹², inside PT's range) {TAG.format(s=4)}; δ_vis is the campaign's law extrapolated 6.5–14 decades beyond its measured range 10³ ≤ t ≤ 10⁶ `[inferred: extrapolation]` {TAG.format(s=5)}")
t = rep(t, "(02:18–02:48 IST)", "(02:18–02:48 IST, then Job 2's PT-edge replay 02:49–03:19 IST)")
t = rep(t, "a few units of 1/L·log", "a few times 1/L (1/L = 0.045 at L = 22) `[inferred: the reach is not measured here]`")
t = rep(t, "(≈ 1267, C2 line 103)", "(≈ 1267 at (δ, t) = (0.1, 10⁶), C2 line 103; larger at the sweep's heights)")
# --- §C.5 labels
t = rep(t, "**Inferred:** none load-bearing after the fix pass", f"**Inferred:** δ_vis(t, L) above t = 10⁶ — the campaign's law extrapolated 6.5–14 decades (§7), load-bearing for S2 and for the \"shallower than δ_vis\" reach of the silence sentences {TAG.format(s=5)}; otherwise none load-bearing after the fix pass")
t = rep(t, "The silence is not evidence (zoo IV.9)", "The silence is not evidence for RH (zoo IV.9); it is a floating-point record of no sign flip at 129 heights, for orbits of depth ≥ δ_vis within the kernel's reach of each height")
t = rep(t, "none containing a sweep height", "none containing a non-control sweep height")
t = rep(t, "the threshold is computed per point (δ_vis, §6)", "the threshold is computed per point from the campaign's law, extrapolated beyond its measured range (δ_vis, §6, §7)")
t = rep(t, "Job 2's own part-B launches (Job 1 ran Job 2's evaluator at every point as Control 1; part B confirms)", "Job 2's own part-B launches (Job 1 ran Job 2's evaluator at every point as Control 1; part B confirms) — superseded: Job 2 launched 20 of its own (14 at L = 22, all 6 at L = 28.35), all PASS, bit-identical to Job 1's replays (`CHECK-O-B.md` §B)")
t = rep(t, "Rigorous coverage above PT's height: none", "Rigorous coverage above PT's height: none `[prior-art gate: dual-checked at the sources opened at the page — Job 1 §5, CHECK-O-A (c), CHECK-O-B C.3; not an exhaustive literature search]`")
# --- §C.6 the three Instruments rows in §11 replaced by the corrected rows
cb = open(f"{ROOT}/results/d4-sign-sweep/CHECK-O-B.md", encoding='utf-8').read()
def row_from_check(prefix):
    m = [l for l in cb.split('\n') if l.startswith(prefix)]
    assert len(m) == 1, (prefix, len(m)); return m[0]
b2_new = row_from_check("| ↳ [EXTENSION 2026-09-25, Session 26 — D4]")
d1_new = row_from_check("| Sign-channel sweep: the (D-c) search range and its ceiling |")
c2_new = row_from_check("| Prime-side sign channel: the phase ceiling of the double-double pipeline")
b2_old = [l for l in t.split('\n') if l.startswith("| ↳ The sign channel SWEPT above the verified height (D4, Session 26 item 1)")]
d1_old = [l for l in t.split('\n') if l.startswith("| Sign-channel sweep: the (D-c) search range and its ceiling (the certified-refutation arm's")]
c2_old = [l for l in t.split('\n') if l.startswith("| Prime-side sign channel: the phase ceiling of the double-double pipeline")]
assert len(b2_old)==1 and len(d1_old)==1 and len(c2_old)==1, (len(b2_old),len(d1_old),len(c2_old))
t = rep(t, b2_old[0], b2_new + f" ← {TAG.format(s=6)} (file column, labels; the row as first written stands in the git history)")
t = rep(t, d1_old[0], d1_new + f" ← {TAG.format(s=6)}")
t = rep(t, c2_old[0], c2_new + f" ← {TAG.format(s=6)}")
t = rep(t, "at visible depths δ_vis = 0.10–0.19", "at visible depths δ_vis = 0.10–0.19 `[inferred: the campaign's law, measured over 10³ ≤ t ≤ 10⁶, extrapolated to the sweep's heights]`")
t = rep(t, "covered measure 2.75·10⁹ (fraction 2.7·10⁻¹¹)", "covered measure 2.75·10⁹ as a plain sum, 2.72·10⁹ as the union [corrected 2026-09-25, Session 26, CHECK-O-B §C.3] (fraction 2.7·10⁻¹¹)")
print("note: all replacements matched")
# --- direction files
b2p = f"{ROOT}/directions/B2-refutation-program.md"; d1p = f"{ROOT}/directions/D1-certified-refutation-arm.md"; c2p = f"{ROOT}/directions/C2-rigidity-conservation.md"
b2 = open(b2p, encoding='utf-8').read(); d1 = open(d1p, encoding='utf-8').read(); c2 = open(c2p, encoding='utf-8').read()
def insert_after_row(text, row_prefix, new_row):
    lines = text.split('\n'); idx = [i for i,l in enumerate(lines) if l.startswith(row_prefix)]
    assert len(idx)==1, (row_prefix, len(idx)); lines.insert(idx[0]+1, new_row); return '\n'.join(lines)
b2 = insert_after_row(b2, "| The first-order SIGN channel as an unconditional refutation channel (shared with C2 M6): prime-side cost on this machine |", b2_new)
d1 = insert_after_row(d1, "| Gomila Λ ≤ 0.1787854 claim", d1_new)
c2 = insert_after_row(c2, "| Prime-side sign channel: measured cost curve on this machine", c2_new)
WL = "- 2026-09-25 (Session 26): **D4, the certified sign-channel sweep above the verified height, CLOSED SILENT** — 129 heights in [3 000 175 332 800, 9.49·10¹⁹] at L = 22 and 28.35, all W > 0, two implementations ≤ 6.8·10⁻¹⁴ apart, both IV.19 controls at every point, Job 2's own replays at 20 points bit-identical; the pipeline's proven phase ceiling 6.63·10¹⁹ at L = 28.35; a datum claiming nothing about RH (IV.9), \"found nothing, correctly\"; certification of a firing priced, not run. `results/d4-sign-sweep/d4-sweep-note.md`, `CHECK-O-A.md`, `CHECK-O-B.md`; the Instruments row above."
def insert_worklog(text, heading="## Work log (append-only)"):
    lines = text.split('\n'); idx=[i for i,l in enumerate(lines) if l.startswith(heading)]; assert len(idx)==1
    # find the end of the work-log block: the next '## ' heading
    j = idx[0]+1
    while j < len(lines) and not lines[j].startswith('## '): j += 1
    k = j
    while k-1 > idx[0] and lines[k-1].strip()=='' : k -= 1
    lines.insert(k, WL); return '\n'.join(lines)
b2 = insert_worklog(b2); d1 = insert_worklog(d1); c2 = insert_worklog(c2)
print("directions: all insertions matched")
if APPLY:
    open(note_p,'w',encoding='utf-8').write(t); open(b2p,'w',encoding='utf-8').write(b2); open(d1p,'w',encoding='utf-8').write(d1); open(c2p,'w',encoding='utf-8').write(c2)
    print("APPLIED")
else:
    print("dry run only")
