# Verify: the Gomila `lean/certificate-and-argument-principle` branch — does it build, and on what axioms?

**Date:** 2026-09-02 (Session 14, D1 Lean verification agent). **Input:** `results/d1-m1/gomila-lean-branch-scout.md` (read in full first). **Scope:** build the two Lake projects `lean/aristotle/argument_principle/` and `lean/aristotle/ec0_certificate/` at branch head `ea09b2f` against their own pinned toolchain, run `#print axioms` on every theorem and lemma, grep for escape hatches. Nothing else: no evaluation of the mathematics, no port, no D1 files touched. **Standing order 5:** every block below is pasted from the commands as run today; where a log line was cut for width it says so. **Machine:** the sponsor's Mac (arm64, Darwin 25.6.0), shared, under a thermal cap; one `lake` process at a time; `pmset -g therm` checked before each heavy step (it printed "No CPU power status has been recorded", i.e. no `CPU_Speed_Limit` line, at every check — no throttling recorded). **Working directory:** `~/rh-lean-work/gomila-ap/` (space-free scratch, created today); `~/rh-lean-work/zeta-23-lean-main/` was not touched. Scripts and full logs are kept there (`cache-get.sh`, `confirm-and-build.sh`, `build.sh`, `make-report.sh`, `*.log`).

**Verdict line:** **BUILDS-CLEAN** — both projects build (exit 0) on the pinned `leanprover/lean4:v4.28.0` + Mathlib `8f9d9cff`; all 61 theorems/lemmas and all 12 definitions depend on `[propext, Classical.choice, Quot.sound]` only.

**Interruption record.** The session that started this run was cut by the usage limit at about 08:10 IST, after the Mathlib cache download had completed (08:08:35) and before `lake build` started. Work resumed at 12:45 IST from the logs on disk; nothing was lost.

---

## 1. Clone (step 1)

Command (retry loop, up to 30 attempts one minute apart; succeeded on attempt 1):

    mkdir -p ~/rh-lean-work/gomila-ap && cd ~/rh-lean-work/gomila-ap && date && for i in $(seq 1 30); do if git clone --depth 1 --branch lean/certificate-and-argument-principle https://github.com/judegomila/dbn-lambda-01787854-candidate-audit ~/rh-lean-work/gomila-ap/repo 2>&1; then echo "CLONE OK on attempt $i"; break; else echo "clone attempt $i failed; sleeping 60"; rm -rf ~/rh-lean-work/gomila-ap/repo; sleep 60; fi; done; date; cd ~/rh-lean-work/gomila-ap/repo && git rev-parse HEAD && git log -1 --format='%H %ad %s' --date=iso

Output, verbatim:

    Wed Sep  2 08:03:26 IST 2026
    Cloning into '/Users/jaytyagi/rh-lean-work/gomila-ap/repo'...
    CLONE OK on attempt 1
    Wed Sep  2 08:03:35 IST 2026
    ea09b2f6aa7afe60706b67c87b202126f3149e8c
    ea09b2f6aa7afe60706b67c87b202126f3149e8c 2026-08-27 16:13:46 -0700 Reseal for the two new lean/aristotle projects

HEAD matches the scout's `ea09b2f6aa7afe60706b67c87b202126f3149e8c`.

### 1.1 Tree of `lean/aristotle/` as cloned (sizes in bytes)

`find . -type f | sort` with `stat -f %z`, taken before any build (the listing below excludes the `.lake/` build directories and the two `PrintAxioms.lean` scratch files this run added). The directory holds **nine** Aristotle projects, not two — the seven from the repository's 2026-08-20 record (`derivative_box`, `error_weld`, `ht_continuity`, `native_binding`, `tail_lemma`, `theorem12_weld`, `window_freeze`) plus the two in scope. Only `argument_principle` and `ec0_certificate` were built.

        2964  ./argument_principle/ARISTOTLE_SUMMARY.md
        3109  ./argument_principle/lake-manifest.json
         234  ./argument_principle/lakefile.toml
          25  ./argument_principle/lean-toolchain
       23422  ./argument_principle/RequestProject/ArgumentPrinciple.lean
       10838  ./argument_principle/RequestProject/ArgumentPrincipleGeneral.lean
         563  ./argument_principle/RequestProject/Main.lean
        3331  ./derivative_box/ARISTOTLE_SUMMARY.md
        3109  ./derivative_box/lake-manifest.json
         234  ./derivative_box/lakefile.toml
          25  ./derivative_box/lean-toolchain
       34065  ./derivative_box/RequestProject/DerivativeBox.lean
         563  ./derivative_box/RequestProject/Main.lean
        2579  ./ec0_certificate/ARISTOTLE_SUMMARY.md
        3109  ./ec0_certificate/lake-manifest.json
         234  ./ec0_certificate/lakefile.toml
          25  ./ec0_certificate/lean-toolchain
       14630  ./ec0_certificate/RequestProject/EC0Certificate.lean
         563  ./ec0_certificate/RequestProject/Main.lean
        1452  ./error_weld/ARISTOTLE_SUMMARY.md
        3109  ./error_weld/lake-manifest.json
         234  ./error_weld/lakefile.toml
          25  ./error_weld/lean-toolchain
        5028  ./error_weld/RequestProject/ErrorWeld.lean
         563  ./error_weld/RequestProject/Main.lean
        2135  ./ht_continuity/ARISTOTLE_SUMMARY.md
        3109  ./ht_continuity/lake-manifest.json
         234  ./ht_continuity/lakefile.toml
          25  ./ht_continuity/lean-toolchain
       15091  ./ht_continuity/RequestProject/HTContinuity.lean
         563  ./ht_continuity/RequestProject/Main.lean
        2674  ./native_binding/ARISTOTLE_SUMMARY.md
        3109  ./native_binding/lake-manifest.json
         234  ./native_binding/lakefile.toml
          25  ./native_binding/lean-toolchain
         563  ./native_binding/RequestProject/Main.lean
       27386  ./native_binding/RequestProject/NativeBinding.lean
        7436  ./README.md
        2786  ./tail_lemma/ARISTOTLE_SUMMARY.md
        3109  ./tail_lemma/lake-manifest.json
         234  ./tail_lemma/lakefile.toml
          25  ./tail_lemma/lean-toolchain
        5476  ./tail_lemma/RequestProject/Basic.lean
        7406  ./tail_lemma/RequestProject/Cap.lean
        9170  ./tail_lemma/RequestProject/Contraction.lean
        6640  ./tail_lemma/RequestProject/Convolution.lean
        7080  ./tail_lemma/RequestProject/Errors.lean
         772  ./tail_lemma/RequestProject/Main.lean
       18758  ./tail_lemma/RequestProject/Monotone.lean
       11752  ./tail_lemma/RequestProject/Tail.lean
        2680  ./theorem12_weld/ARISTOTLE_SUMMARY.md
        3109  ./theorem12_weld/lake-manifest.json
         234  ./theorem12_weld/lakefile.toml
          25  ./theorem12_weld/lean-toolchain
         563  ./theorem12_weld/RequestProject/Main.lean
       14136  ./theorem12_weld/RequestProject/Weld.lean
        2697  ./window_freeze/ARISTOTLE_SUMMARY.md
        3109  ./window_freeze/lake-manifest.json
         234  ./window_freeze/lakefile.toml
          25  ./window_freeze/lean-toolchain
         632  ./window_freeze/RequestProject/Main.lean
        5591  ./window_freeze/RequestProject/SiteBracket.lean
       10471  ./window_freeze/RequestProject/WindowFreeze.lean

### 1.2 SHA-256 of every `.lean` file in the two projects in scope (`shasum -a 256`)

    b1162a0cc3b46c3559e928d04cf1a3c37b4fad6ca1323b65a41ea9948fbe605b  ./argument_principle/RequestProject/ArgumentPrinciple.lean
    ee3822428e40b210d14c47b044bbbde011d0b72a4cfa2bad0fb2811a04113e82  ./argument_principle/RequestProject/ArgumentPrincipleGeneral.lean
    929b0bddef0b781f3fb42c7a99f252dc0bda7331f698104f7075e12ff637c52d  ./argument_principle/RequestProject/Main.lean
    bbf8c87db066583a2f9cabd0438607b70dc44d8465c53a90b9fae3d0a4a00d6b  ./ec0_certificate/RequestProject/EC0Certificate.lean
    929b0bddef0b781f3fb42c7a99f252dc0bda7331f698104f7075e12ff637c52d  ./ec0_certificate/RequestProject/Main.lean

All four hashes the scout recorded (`ArgumentPrinciple.lean` b1162a0c…, `ArgumentPrincipleGeneral.lean` ee382242…, `Main.lean` 929b0bdd…, `EC0Certificate.lean` bbf8c87d…) match the clone byte for byte. Line counts (`wc -l`): 444 / 215 / 24 (argument_principle), 321 / 24 (ec0_certificate). Declarations by `grep -c '^theorem '` / `'^lemma '`: ArgumentPrinciple.lean 4 / 26, ArgumentPrincipleGeneral.lean 3 / 8, EC0Certificate.lean 2 / 18 — total 61, matching the commit's "61 theorems".

### 1.3 Pins (both projects)

`lean-toolchain` (both): `leanprover/lean4:v4.28.0`. `lakefile.toml` (both, identical): as quoted in the scout §1.2 (mathlib `rev = "v4.28.0"`, lib `RequestProject`, globs `RequestProject.+`). `diff argument_principle/lake-manifest.json ec0_certificate/lake-manifest.json` printed nothing (`IDENTICAL`); mathlib rev `8f9d9cff6bd728b17a24e163c9402775d9e6a365` (inputRev `v4.28.0`) in both. So step 4 needed no second Mathlib revision.

---

## 2. Toolchain (step 2)

Command: `elan toolchain install leanprover/lean4:v4.28.0` in a 30-attempt retry loop. The default toolchain was left as it was (`elan show`: "no active toolchain" — this machine's elan has no default; lake reads the project's `lean-toolchain`). Output, verbatim (`~/rh-lean-work/gomila-ap/verify.log`):

    2026-09-02 08:03:52 toolchain install leanprover/lean4:v4.28.0 begin
    info: downloading https://releases.lean-lang.org/lean4/v4.28.0/lean-4.28.0-darwin_aarch64.tar.zst
    info: installing /Users/jaytyagi/.elan/toolchains/leanprover--lean4---v4.28.0
    
    leanprover/lean4:v4.28.0 installed - Lean (version 4.28.0, arm64-apple-darwin24.6.0, commit 7e01a1bf5c70fc6167d49c345d3bf80596e9a79b, Release)
    
    2026-09-02 08:05:19 TOOLCHAIN OK on attempt 1

`elan toolchain list` afterwards: `leanprover/lean4:v4.28.0`, `leanprover/lean4:v4.33.0-rc2`. Disk: `~/.elan/toolchains/leanprover--lean4---v4.28.0` = 2.4G. Wall time 08:03:52 → 08:05:19 (87 s).

---

## 3. `argument_principle/` (step 3)

### 3.1 Mathlib cache — `lake exe cache get`

Script `~/rh-lean-work/gomila-ap/cache-get.sh` (thermal gate, then `lake exe cache get` in a 30-attempt retry loop, one minute apart). Log `cache-get-argument_principle.log`, complete except that lines over 200 characters (the curl progress meter and the single carriage-return-separated "Downloaded: …" progress line) are cut:

    2026-09-02 08:06:11  === cache get begin in /Users/jaytyagi/rh-lean-work/gomila-ap/repo/lean/aristotle/argument_principle ===
    2026-09-02 08:06:12  toolchain: leanprover/lean4:v4.28.0; lake: Lake version 5.0.0-src+7e01a1b (Lean version 4.28.0)
    2026-09-02 08:06:12  therm ok (CPU_Speed_Limit='none recorded')
    2026-09-02 08:06:12  --- attempt 1 ---
    info: mathlib: cloning https://github.com/leanprover-community/mathlib4.git
    info: mathlib: checking out revision '8f9d9cff6bd728b17a24e163c9402775d9e6a365'
    info: plausible: cloning https://github.com/leanprover-community/plausible
    info: plausible: checking out revision '55c8532eb21ec9f6d565d51d96b8ca50bd1fbef3'
    info: LeanSearchClient: cloning https://github.com/leanprover-community/LeanSearchClient
    info: LeanSearchClient: checking out revision 'c5d5b8fe6e5158def25cd28eb94e4141ad97c843'
    info: importGraph: cloning https://github.com/leanprover-community/import-graph
    info: importGraph: checking out revision '85b59af46828c029a9168f2f9c35119bd0721e6e'
    info: proofwidgets: cloning https://github.com/leanprover-community/ProofWidgets4
    info: proofwidgets: checking out revision 'be3b2e63b1bbf496c478cef98b86972a37c1417d'
    info: aesop: cloning https://github.com/leanprover-community/aesop
    info: aesop: checking out revision 'f642a64c76df8ba9cb53dba3b919425a0c2aeaf1'
    info: Qq: cloning https://github.com/leanprover-community/quote4
    info: Qq: checking out revision 'b8f98e9087e02c8553945a2c5abf07cec8e798c3'
    info: batteries: cloning https://github.com/leanprover-community/batteries
    info: batteries: checking out revision '495c008c3e3f4fb4256ff5582ddb3abf3198026f'
    info: Cli: cloning https://github.com/leanprover/lean4-cli
    info: Cli: checking out revision '4f10f47646cb7d5748d6f423f4a07f98f7bbcc9e'
    ✔ [2/22] Built Cache.Lean (205ms)
    ✔ [3/22] Built Cache.Init (174ms)
    ✔ [4/22] Built Cache.IO (472ms)
    ✔ [5/22] Built Cache.Hashing (277ms)
    ✔ [8/22] Built Batteries.Data.String.Basic (186ms)
    ✔ [9/22] Built Batteries.Data.Array.Match (324ms)
    ✔ [10/22] Built Batteries.Data.String.Matcher (163ms)
    ✔ [11/22] Built Batteries.Data.String.Basic:c.o (336ms)
    ✔ [12/22] Built Cache.Init:c.o (2.2s)
    ✔ [13/22] Built Batteries.Data.Array.Match:c.o (254ms)
    ✔ [14/22] Built Batteries.Data.String.Matcher:c.o (99ms)
    ✔ [15/22] Built Cache.Lean:c.o (2.2s)
    ✔ [16/22] Built Cache.Hashing:c.o (1.6s)
    ✔ [17/22] Built Cache.Requests (586ms)
    ✔ [18/22] Built Cache.IO:c.o (2.3s)
    ✔ [19/22] Built Cache.Main (333ms)
    ✔ [20/22] Built Cache.Main:c.o (241ms)
    ✔ [21/22] Built Cache.Requests:c.o (603ms)
    ✔ [22/22] Built cache:exe (801ms)
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
      3  884k    3 32958    0     0  23835      0  0:00:37  0:00:01  0:00:36 23835100  884k  100  884k    0     0   608k      0  0:00:01  0:00:01 --:--:-- 11.8M
    
    installing leantar 0.1.16
    Fetching ProofWidgets cloud release... done!
    Current branch: HEAD
    Using cache (Azure) from origin: leanprover-community/mathlib4
    Attempting to download 8010 file(s) from leanprover-community/mathlib4 cache
    Downloaded: 1 file(s) [attempted 1/8010 = 0%, 12 KB/s]Downloaded: 15 file(s) [attempted 15/8010 = 0%, 4 KB/s]Downloaded: 20 file(s) [attempted 20/8010 = 0%, 4 KB/s]Downloaded: 29 file(s) [attempte…[cut at 200 chars]
    Decompressing 8007 file(s) (3 already decompressed)
    Decompressed in 4864 ms
    Completed successfully!
    2026-09-02 08:08:35  CACHE GET OK on attempt 1 after 143 s
    CACHE_GET_RESULT=OK attempt=1 secs=143
    6.9G	.lake
    134M	.lake/packages/aesop
    162M	.lake/packages/batteries
    456K	.lake/packages/Cli
    6.4M	.lake/packages/importGraph
    5.0M	.lake/packages/LeanSearchClient
    6.5G	.lake/packages/mathlib
     11M	.lake/packages/plausible
     45M	.lake/packages/proofwidgets
     23M	.lake/packages/Qq

**Read-off:** the Mathlib cache for rev `8f9d9cff` exists on the community cache server ("Using cache (Azure) from origin: leanprover-community/mathlib4"; 8010 files attempted, 8007 decompressed + 3 already present); it completed on attempt 1 in 143 s wall (08:06:12 → 08:08:35), so the STOP condition (no cache → compile Mathlib from source) did not arise. Disk after the step: `.lake` 6.9G, of which `packages/mathlib` 6.5G.

Confirmation after the resume (`confirm-and-build.sh`, `lake exe cache get` again, retry-wrapped) — log `confirm-cache-argument_principle.log`, verbatim:

    2026-09-02 12:46:12  === confirm: lake exe cache get in /Users/jaytyagi/rh-lean-work/gomila-ap/repo/lean/aristotle/argument_principle ===
    2026-09-02 12:46:12  --- confirm attempt 1 ---
    Current branch: HEAD
    Using cache (Azure) from origin: leanprover-community/mathlib4
    No files to download
    Already decompressed 8010 file(s)
    2026-09-02 12:46:20  CONFIRM_RESULT=OK attempt=1 secs=8

### 3.2 `lake build`

Script `build.sh` (thermal gate, `lake build`, then `lake env lean PrintAxioms.lean`). Log `build-argument_principle.log`:

    2026-09-02 12:46:21  === lake build begin in /Users/jaytyagi/rh-lean-work/gomila-ap/repo/lean/aristotle/argument_principle ===
    2026-09-02 12:46:22  lean: Lean (version 4.28.0, arm64-apple-darwin24.6.0, commit 7e01a1bf5c70fc6167d49c345d3bf80596e9a79b, Release)
    2026-09-02 12:46:22  therm ok (CPU_Speed_Limit='none recorded')
    ✔ [8026/8029] Built RequestProject.Main (23s)
    ⚠ [8027/8029] Built RequestProject.ArgumentPrinciple (25s)
    warning: RequestProject/ArgumentPrinciple.lean:398:40: unused variable `hre`
    
    Note: This linter can be disabled with `set_option linter.unusedVariables false`
    warning: RequestProject/ArgumentPrinciple.lean:398:60: unused variable `him`
    
    Note: This linter can be disabled with `set_option linter.unusedVariables false`
    warning: RequestProject/ArgumentPrinciple.lean:400:45: unused variable `hm`
    
    Note: This linter can be disabled with `set_option linter.unusedVariables false`
    warning: RequestProject/ArgumentPrinciple.lean:417:44: unused variable `hre`
    
    Note: This linter can be disabled with `set_option linter.unusedVariables false`
    warning: RequestProject/ArgumentPrinciple.lean:417:64: unused variable `him`
    
    Note: This linter can be disabled with `set_option linter.unusedVariables false`
    warning: RequestProject/ArgumentPrinciple.lean:420:45: unused variable `hm`
    
    Note: This linter can be disabled with `set_option linter.unusedVariables false`
    ✔ [8028/8029] Built RequestProject.ArgumentPrincipleGeneral (2.9s)
    Build completed successfully (8029 jobs).
    2026-09-02 12:46:52  lake build exit=0 after 30 s
    BUILD_RESULT=0 secs=30
    2026-09-02 12:46:52  === lake env lean PrintAxioms.lean ===
    2026-09-02 12:47:16  print axioms exit=0 after 24 s;       45 lines in /Users/jaytyagi/rh-lean-work/gomila-ap/print-axioms-argument_principle.log
    AXIOMS_RESULT=0 secs=24
    6.9G	.lake

Warnings/errors in the build log (`grep -n -i -E 'warning|error|sorry'`):

    6:warning: RequestProject/ArgumentPrinciple.lean:398:40: unused variable `hre`
    9:warning: RequestProject/ArgumentPrinciple.lean:398:60: unused variable `him`
    12:warning: RequestProject/ArgumentPrinciple.lean:400:45: unused variable `hm`
    15:warning: RequestProject/ArgumentPrinciple.lean:417:44: unused variable `hre`
    18:warning: RequestProject/ArgumentPrinciple.lean:417:64: unused variable `him`
    21:warning: RequestProject/ArgumentPrinciple.lean:420:45: unused variable `hm`

### 3.3 `#print axioms` — every theorem and lemma (41) and the four definitions

Scratch file `argument_principle/PrintAxioms.lean` (not part of the Lake target; imports `RequestProject.ArgumentPrinciple` and `RequestProject.ArgumentPrincipleGeneral`; 45 `#print axioms` lines: the eight main results the scout names first, then the remaining 33 lemmas, then the four `def`s). Run as `lake env lean PrintAxioms.lean`. Output `print-axioms-argument_principle.log`, verbatim and complete:

    'ArgumentPrinciple.windingRect_eq_sum_analyticOrder' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.rectIntegral_inv_sub' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.windingRect_prod_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.windingRect_factored' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.windingRect_factored_div' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.windingRect_eq_finsum_analyticOrder' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.windingRect_id_eq_one' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.rectIntegral_eq_zero_of_differentiableOn' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.mem_Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.RectFrontier_subset_Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.mem_RectFrontier_bot' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.mem_RectFrontier_top' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.mem_RectFrontier_right' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.mem_RectFrontier_left' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.continuousOn_edge_bot' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.continuousOn_edge_top' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.continuousOn_edge_right' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.continuousOn_edge_left' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.rectIntegral_congr' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.rectIntegral_add' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.rectIntegral_sub' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.rectIntegral_const_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.rectIntegral_sum' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.arctan_add_arctan_inv_of_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.arctan_add_arctan_inv_of_neg' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.ofReal_add_const_mul_I_ne_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.hasDerivAt_edge_antiderivative' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.integral_inv_ofReal_add_const_mul_I' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.integral_inv_const_add_ofReal_mul_I' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.arctan_rect_sum' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.continuousOn_logDeriv' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.rectIntegral_logDeriv_eq_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.sub_ne_zero_of_mem_RectFrontier' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.analyticOrderAt_ne_top' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.exists_factor_pow_sub' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.exists_factor_prod' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.isCompact_Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.finite_zeros_of_isCompact' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.finite_zeros_Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.mem_RectFrontier_left_corner' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.mem_Ioo_of_zero_mem_Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.rectIntegral' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.windingRect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'ArgumentPrinciple.RectFrontier' depends on axioms: [propext, Classical.choice, Quot.sound]

### 3.4 Escape-hatch grep on the sources

    cd ~/rh-lean-work/gomila-ap/repo/lean/aristotle && grep -n -E "sorry|admit|native_decide|axiom |unsafe|opaque|implemented_by|extern" argument_principle/RequestProject/*.lean ec0_certificate/RequestProject/*.lean; echo "exit=$?"

Output: no lines; `exit=1` (grep found nothing) — run on the clone before the build and identical after it (the build does not modify sources; `git status` in the clone shows only the two untracked `PrintAxioms.lean` files and the `.lake/` directories). A broader grep for `\bdecide\b|set_option|\bpartial\b|\bmacro\b|\belab\b|\bsyntax\b|initialize|@[simp]|\bomega\b` matched only `set_option` lines: the fourteen in each `Main.lean` (as the scout lists) and, in `EC0Certificate.lean` lines 38–39, `set_option exponentiation.threshold 40000` and `set_option maxRecDepth 20000`. Imports: every file `import Mathlib`; `ArgumentPrincipleGeneral.lean` also `import RequestProject.ArgumentPrinciple`.

---

## 4. `ec0_certificate/` (step 4)

Same toolchain and byte-identical `lake-manifest.json` (§1.3), so the same package set applies. To avoid a second multi-gigabyte clone and download on the sponsor's link, the package directory was cloned with APFS `cp -Rc` (clonefile, no extra disk) from `argument_principle/.lake/packages` to `ec0_certificate/.lake/packages`, after the first project's lake process had exited; `lake exe cache get` was then run in `ec0_certificate/` to let lake verify the manifest against the copied packages (it re-fetches anything that does not match), followed by `lake build` and the `#print axioms` file, all via the same scripts.

### 4.1 Package clone and cache confirmation

    Command (after confirming no lake process was running and `pmset -g therm` printed no CPU_Speed_Limit line):
    
        mkdir -p ec0_certificate/.lake && cp -Rc argument_principle/.lake/packages ec0_certificate/.lake/packages
    
    Output:
    
        Wed Sep  2 12:50:12 IST 2026
        cp -Rc packages done in 13 s
        6.9G	/Users/jaytyagi/rh-lean-work/gomila-ap/repo/lean/aristotle/ec0_certificate/.lake/packages
        Wed Sep  2 12:50:26 IST 2026
        launched ec0 pid 5777

Log `confirm-cache-ec0_certificate.log`, verbatim:

    2026-09-02 12:50:26  === confirm: lake exe cache get in /Users/jaytyagi/rh-lean-work/gomila-ap/repo/lean/aristotle/ec0_certificate ===
    2026-09-02 12:50:26  --- confirm attempt 1 ---
    Current branch: HEAD
    Using cache (Azure) from origin: leanprover-community/mathlib4
    No files to download
    Already decompressed 8010 file(s)
    2026-09-02 12:50:34  CONFIRM_RESULT=OK attempt=1 secs=8

### 4.2 `lake build` — log `build-ec0_certificate.log`

    2026-09-02 12:50:34  === lake build begin in /Users/jaytyagi/rh-lean-work/gomila-ap/repo/lean/aristotle/ec0_certificate ===
    2026-09-02 12:50:34  lean: Lean (version 4.28.0, arm64-apple-darwin24.6.0, commit 7e01a1bf5c70fc6167d49c345d3bf80596e9a79b, Release)
    2026-09-02 12:50:34  therm ok (CPU_Speed_Limit='none recorded')
    ✔ [8026/8028] Built RequestProject.Main (21s)
    ✔ [8027/8028] Built RequestProject.EC0Certificate (25s)
    Build completed successfully (8028 jobs).
    2026-09-02 12:51:02  lake build exit=0 after 28 s
    BUILD_RESULT=0 secs=28
    2026-09-02 12:51:02  === lake env lean PrintAxioms.lean ===
    2026-09-02 12:51:12  print axioms exit=0 after 10 s;       28 lines in /Users/jaytyagi/rh-lean-work/gomila-ap/print-axioms-ec0_certificate.log
    AXIOMS_RESULT=0 secs=10
    6.9G	.lake

Warnings/errors in the build log (`grep -n -i -E 'warning|error|sorry'`):


### 4.3 `#print axioms` — both theorems, all 18 lemmas, the eight definitions

Scratch file `ec0_certificate/PrintAxioms.lean` (28 `#print axioms` lines), run as `lake env lean PrintAxioms.lean`. Output `print-axioms-ec0_certificate.log`, verbatim and complete:

    'EC0.eC0_le_sharp' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.eC0_le_weak' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.box_nonempty' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.Lf_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.log_lower_of_pow' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.log_A_lower' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.log_T_lower' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.M_lower' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.M_upper' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.Lf_lower' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.Lf_upper' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.y0_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.y0_lower' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.y0_upper' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.ymax_le_one' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.three_rpow_sub_le' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.three_rpow_y0_le' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.three_rpow_neg_y0_le' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.tail_le' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.exponent_le' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.N0' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.t0' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.t1' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.y0' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.ymax' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.xf' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.Lf' depends on axioms: [propext, Classical.choice, Quot.sound]
    'EC0.eC0' depends on axioms: [propext, Classical.choice, Quot.sound]

---

## 5. Wall times and disk

    Step                                                   Wall time              Result
    git clone --depth 1 (branch head ea09b2f)              08:03:26 → 08:03:35  ( 9 s)   OK, attempt 1
    elan toolchain install leanprover/lean4:v4.28.0        08:03:52 → 08:05:19  (87 s)   OK, attempt 1
    argument_principle: lake exe cache get (deps + oleans) 08:06:12 → 08:08:35  (143 s)  OK, attempt 1; 8010 files
      [usage-limit cut ~08:10; resumed 12:45]
    argument_principle: lake exe cache get (confirm)       12:46:12 → 12:46:20  ( 8 s)   "No files to download / Already decompressed 8010 file(s)"
    argument_principle: lake build                         12:46:22 → 12:46:52  (30 s)   exit 0, 8029 jobs, 6 linter warnings, 0 errors
    argument_principle: lake env lean PrintAxioms.lean     12:46:52 → 12:47:16  (24 s)   exit 0, 45 lines
    ec0_certificate: cp -Rc of .lake/packages (clonefile)  12:50:12 → 12:50:26  (13 s)   6.9G logical, shared blocks
    ec0_certificate: lake exe cache get (confirm)          12:50:26 → 12:50:34  ( 8 s)   "No files to download / Already decompressed 8010 file(s)"
    ec0_certificate: lake build                            12:50:34 → 12:51:02  (28 s)   exit 0, 8028 jobs, 0 warnings, 0 errors
    ec0_certificate: lake env lean PrintAxioms.lean        12:51:02 → 12:51:12  (10 s)   exit 0, 28 lines
    
    Heavy-CPU time in total: about 2 minutes (the two builds and two axiom runs). Thermal: `pmset -g therm`
    printed no CPU_Speed_Limit line at every check (before clone, before cache get, before each build).
    
    Disk (du -sh, logical):
      ~/rh-lean-work/gomila-ap                                        14G   (the two .lake trees are APFS clones of the same blocks;
      …/argument_principle/.lake                                     6.9G    real footprint of the scratch dir is about 7 GB)
      …/ec0_certificate/.lake                                        6.9G
      ~/.elan/toolchains/leanprover--lean4---v4.28.0                 2.4G   (second toolchain, left installed; default unchanged)
      ~/.cache/mathlib                                               842M   (the cache tool's downloaded archives)
    Machine free space before: 313 GiB.

---

## 6. Deviations from the brief, and what was not done

* The `#print axioms` file covers **every** theorem and lemma (61) plus the twelve `def`s, not only the "main" ones — so the commit's "all 61 theorems on the three standard axioms" claim is checked in full rather than sampled.
* `ec0_certificate` reused the package directory by APFS clone (§4) instead of a second network fetch; lake's own manifest check and `lake exe cache get` ran on the copy, and the output is above.
* The first session's log monitor died on a zsh-only substitution after the build had already finished; it cost nothing but is mentioned so the log timestamps make sense.
* Not done, by design: no mathematics evaluated, no definition-faithfulness audit against FORMAT.md §8.2, no port to the program's toolchain (v4.33.0-rc2 / Mathlib 51e6992), no D1 file touched. The scout's G1–G6 gap list stands as written.

---

## 7. Verdict

**BUILDS-CLEAN** — both projects build (exit 0) on the pinned `leanprover/lean4:v4.28.0` + Mathlib `8f9d9cff`; all 61 theorems/lemmas and all 12 definitions depend on `[propext, Classical.choice, Quot.sound]` only.

Both Lake projects at branch head `ea09b2f6aa7afe60706b67c87b202126f3149e8c` build from a fresh clone against their own pins (`leanprover/lean4:v4.28.0`, Mathlib `8f9d9cff6bd728b17a24e163c9402775d9e6a365`, oleans from the community cache, nothing compiled from Mathlib source): `lake build` exit 0 in `argument_principle/` (8029 jobs, 30 s) and in `ec0_certificate/` (8028 jobs, 28 s), no errors. `#print axioms` on all 61 theorems and lemmas — the eight the scout names (`windingRect_eq_sum_analyticOrder`, `rectIntegral_inv_sub`, `windingRect_prod_mul`, `windingRect_factored`, `windingRect_factored_div`, `windingRect_eq_finsum_analyticOrder`, `windingRect_id_eq_one`, `rectIntegral_eq_zero_of_differentiableOn`), the other 33 lemmas of `argument_principle`, and all 20 of `ec0_certificate` (`eC0_le_sharp`, `eC0_le_weak`, `box_nonempty`, 17 lemmas) — plus the twelve definitions reports exactly `[propext, Classical.choice, Quot.sound]` on every one of the 73 lines; no other axiom, no `sorryAx`. The source grep for `sorry|admit|native_decide|axiom |unsafe|opaque|implemented_by|extern` finds nothing. The only build-output findings are six `linter.unusedVariables` warnings in `ArgumentPrinciple.lean`: the hypotheses `hre`, `him` (lines 398 and 417) and `hm` (lines 400 and 420) of `windingRect_factored` and `windingRect_factored_div` are not used by their proofs — recorded as observed, not interpreted here. So the branch's claim ("lake build green on v4.28.0; no sorry/axiom/native_decide; all 61 theorems on the three standard axioms") is reproduced on this machine. What this does NOT establish: that the statements are faithful to the intended mathematics (the scout's G1–G6 stand — the theorem is for entire `H`, not for ζ on an open set, and it is stated in a different winding-number vocabulary from D1's `RectArgPrinciple`), or that the files compile on the program's toolchain (v4.33.0-rc2 / Mathlib 51e6992), which was not attempted.
