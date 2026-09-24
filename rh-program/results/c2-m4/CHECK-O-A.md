# C2 — M4 residue, Unit A (`Separation6b`): b₁ proved in symbolic form, the clause-7 fold, `rstar_of_21L` — independent check (Session 24 item 3, Job 2, Opus 5, clean clone)

Task: `results/c2-m4/BRIEF-A.md` "Job 2 — INDEPENDENT CHECKER"; contract `results/c2-m4/PRICING-RESIDUE.md` §1 Pieces 2, 3
(3-sym), 6 and §2 row A; the builder's own checklist `results/c2-m4/BUILD-NOTES-A.md` §5. Object checked: the builder's
work (Job 1, Fable 5.1, 2026-09-24, 19:20–19:55 IST) as recorded in `BUILD-NOTES-A.md`, `SHARED.md` (the Unit A blocks)
and `hashes-A.txt`. Method precedent: `results/c2-m4/CHECK-O-iii.md` (layout repeated), `CHECK-O.md`.

Nothing in the repository, the mirror or the builder's working tree was modified by this job, and nothing was committed
by it. Everything in §§2–12 was produced in a FRESH clone made for this check, `~/rh-lean-check-s24/clone` (cloned from
`https://github.com/anthropics/zeta-23-lean.git` at 19:58 IST, checked out at tag v1.0), overlaid with the current
`rh-program/lean/` mirror; never in `~/rh-lean-work/zeta-23-lean-main`. Scripts and logs: `results/c2-m4/verify-A-O/`.

---

## §0 Headline verdict

(PENDING — written last; see the verdict table at the end.)

---

## §1 Clone provenance and the overlay — **CLEAN**

A new clone, not a reset of an earlier one:

```
git clone https://github.com/anthropics/zeta-23-lean.git clone ; git checkout v1.0
HEAD:          3635e74826a4c1fcece7d1cd2b6fa75e43a00510
v1.0^{commit}: 3635e74826a4c1fcece7d1cd2b6fa75e43a00510
git status --porcelain -> (empty)
lean-toolchain  leanprover/lean4:v4.33.0-rc2
lakefile.toml   rev = "51e6992efd06126df61a496bebf8f49482a4e129"   (Mathlib)
```

This is the commit `lean/README.md` "Building" names and the toolchain/Mathlib pair of every record in this program.

**Overlay measured before copying.** A file-by-file `cmp` of all **177** mirror files (`rh-program/lean/**`) against the
pristine v1.0 tree: **175 NEW, 2 CHANGED** (`README.md`, `Zeta23.lean`), 0 identical. The `Zeta23.lean` difference is
exactly **23 added `import` lines and nothing else** (the M4 (iii) record's 21 plus `import Zeta23.Separation.B1Sym`,
`import Zeta23.Separation.Assembly2`), so BUILD-NOTES-A's "the ONE edit to an existing Lean file is the two additive
imports in `Zeta23.lean`" is confirmed against upstream, not merely against the previous commit. Overlay applied by the
README recipe (`Zeta23/`, `comparator/`, `Zeta23.lean`, plus `formalization.yaml` and `README.md`); post-overlay
`git status --porcelain` in the clone lists 43 entries, all of them the program's own files.

**Cold.** The clone has no `.lake/build` at all: the Mathlib package directory (`.lake/packages`, 7.8 GB) was copied by an
APFS clone from the earlier checker's clone (`cp -Rc`), and `lake exe cache get` then reported `No files to download;
Already decompressed 8681 file(s)` (`verify-A-O/cache-get.log`). The whole `Zeta23` library, the program's additions
included, therefore compiled from source.

Load discipline: one `lake` process at a time throughout; no `-j`; `caffeinate` running; nothing else heavy in parallel.

