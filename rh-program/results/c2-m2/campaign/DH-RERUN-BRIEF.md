# C2 — Session 23 item 0(c): re-run of the three DH zero-side scripts with the gamma-normalized root refinement (the record correction of 2026-09-17) — brief

**Written 2026-09-17 (Session 23, orchestrator). One agent (Fable 5.1). CONTRACT: `results/c2-m6/m6-rung1-note.md` §5.3 (the correction) and `results/c2-m6/check-O.md` §3 (independent confirmation, the list of touched record files, the cancellation identity W_Z − W_{Z′} = W(orbit), and the one caveat it settles). Paths contain spaces — quote them. U.S. English. Do not commit (watchdogs). At most 2 heavy local processes.**

## The defect and the fix (read §5.3 and §3 at the page first)
The three record scripts locate DH's on-line zeros by sign changes of Z_DH(u) = Re Ξ_DH(½ + iu) and refine with `mp.findroot(Zline, (u, u2), solver='illinois')` at `mp.dps = 15`. |Ξ_DH(½ + iu)| ≈ |Γ(¾ + iu/2)| ≈ e^{−πu/4} ≈ 10⁻²⁰…10⁻³³ on these windows, so the absolute stopping test is met after one secant step and the returned points are displaced by 1.2·10⁻⁶ to 1.1·10⁻³ (±30 around 85.7). The fix, as shipped in `results/c2-m6/verify/zero_side_dh.py` (lines ≈ 37–54): refine on S(u) = Z_DH(u)/[(5/π)^{3/4}|Γ(¾ + iu/2)|] — O(1), same zeros — at 40 digits; verify max |f_DH(½ + iγ)| over the refined points is ≤ 10⁻³⁰.

## The three scripts and what to produce
1. `results/c2-m2/verify/dh_negative_control.py` (lines 22–29) → new run `dh_negative_control_rerun.py` (copy of the original with ONLY the refinement changed: rescaled S(u), 40-digit refinement, a printed max |f_DH| line; nothing else altered), outputs `dh_negative_control_rerun_run.log`, `dh_negative_control_rerun_out.json`. Print the nine L-rows side by side: W_{Z′} recorded / re-run / relative; W_Z recorded / re-run; W_Z − W_{Z′} both (must agree to machine precision — the cancellation identity); the ×6.24 ratio at L* (expect 6.2375; the check's 6.23731 is a truncation of L*).
2. `results/c2-m2/campaign/dh_offline_scan.py` (`online_count`, line ≈ 75) → `dh_offline_scan_rerun.py`; DO NOT redo the orbit search (the 26 orbits are located on f_DH itself and stand — read them from `dh_offline_scan.json`); re-run ONLY the on-line-zero location for the `control_rows` / `online_window` fields and reprint those; output `dh_offline_scan_rerun.json` + log.
3. `results/c2-m2/campaign/dh_control_new_heights.py` (`online_count`, line ≈ 35) → `dh_control_new_heights_rerun.py`, same discipline, the control tables at t = 114.163343, 166.479306, 176.702461; output json + log; the separation / ratio / fires columns must be identical to the record's, the W_{Z′} columns reprinted with their relative change.
Keep the original scripts and their outputs untouched (the record is immutable; the re-run sits beside it). Re-hash: append the new files' SHA-256 to `results/c2-m2/verify/hashes-rerun.txt` (new file) and the campaign's to `results/c2-m2/campaign/hashes-rerun.txt`.

## The two dated lines to append (append only — never edit earlier text)
* `results/c2-m2/separation-note.md`: a dated block at the very end, "**Re-run 2026-09-17 (Session 23; after `results/c2-m6/m6-rung1-note.md` §5.3 and `check-O.md` §3)**", stating: the on-line-zero recipe of §8 rung 2's control mislocated the 36 on-line points by 1.2·10⁻⁶ to 1.1·10⁻³; the re-run's W_{Z′} at (85.7, 10) / (85.7, 20) / L* with relative changes; W_Z − W_{Z′} identical (the identity); the ×6.24 ratio and every "fires" line STAND; the "3·10⁻¹⁰ in-window on-line noise" figure → its re-run value; and the settled caveat: the argument-principle count of `results/c2-m6/verify/zero_side_dh.py` (79 = 75 + 2·2 on [−1, 2] × [t − 60, t + 60]) shows the step-0.05 scan misses nothing in ±60, so the "40.1 against 36 + 2" of §8 rung 2 is S(T) fluctuation, not a missed pair. One paragraph; file paths of the re-run outputs.
* `results/c2-m2/campaign/CAMPAIGN.md`: a dated block at the end of §1 (or at the file's end if §1 has no natural tail — append, do not interleave), same content for the three campaign heights; the DH negative controls at four heights STAND.
* Also append one dated line to `results/c2-m2/SHARED.md` under checkpoint (5): the criterion "max |Z_DH(γ)| at 25 digits" is scale-blind; the replacement criterion is max |f_DH(½ + iγ)| or max |S(γ)|.

## Stop and report when (10(m))
* Any separation / ratio / fires column moves by more than 10⁻⁸ relative (the identity says it cannot; if it does, stop — something else is wrong).
* Any W_{Z′} changes by more than 2 % relative at L ≤ 20 (the expected change is ≈ 2·10⁻⁴).
* The 40-digit refinement fails to bring max |f_DH| below 10⁻²⁵ at any point.

## Final report (chat, ≤ 20 lines)
Per script: rows changed, max relative change of W_{Z′}, identity check residual, wall time; the SHA-256 of the two appended files; any stop condition fired.
