# History purge of 2026-10-01 (Session 41) — record

Written 17:58 IST 2026-10-01 by the orchestrator (Fable 5.1). The sponsor delegated the decision ("purge the history, whatever you want there, your call").

## What was decided
One rule everywhere: other people's published work (PDFs, full-text extractions, OCR, page images, page dumps) and a third party's private email are kept on the sponsor's machine and are not in the public repository — neither in the current files nor in its history. Openly licensed or public-domain material that the program builds on stays: arXiv API abstract listings (metadata), LMFDB pages and a data extract, Odlyzko's table of zeros, the Lean files ported from an MIT-licensed repository (attributed), the Apache-2.0 root import file, and the program's own papers and certificate archive.

## What was done, in order
1. Read-only inventory by an Opus agent: every path that ever existed (8,865) classified (`resolved.tsv`; `PATHS-THIRD-PARTY.txt`, `PATHS-KEEP.md`, `PATHS-OWNER-DECIDES.md`, `GITIGNORE-PROPOSED.txt`, `stats.txt`, `tp-at-head.txt`).
2. Both watchdogs stopped. `.gitignore` extended (the proposed block A plus one line for quoted private replies; the earlier file is `gitignore.before-s41`). 837 tracked files untracked with `git rm --cached` (835 from the inventory, the private-email file, one arXiv search page); the files stay on disk. The program's own two PDFs under `c3-r/s14` tracked again. Commit 13f1e0ea (old history).
3. Backup: `~/riemann-backup-before-purge-2026-10-01.bundle` (755,957,364 bytes; "is okay", "records a complete history").
4. Fresh clone outside iCloud; `git-filter-repo 2.47.0 --invert-paths --paths-from-file` with 468 path entries (`PURGE-PATHS-FINAL.txt`: the inventory's 466 lines, the private-email file, the search page): 1,286 commits parsed, 1,278 remain (8 became empty).
5. Verified before pushing: the final tree is identical to the working tree's (a125ac0a…); no path on the list remains in any commit; the three tags exist; the 13 PDFs left in history are all the program's own; no page image remains; the 8 paths left under `anthropic/zeta-23-lean-main/` are the program's own Lean files; the one remaining "diamond-zhang" path is an arXiv metadata listing.
6. Force-pushed `main` (8fdec35c → efad5a8d) and the tags `paper-2026-08-28`, `haglund-cert-2026-10`, `haglund-paper-2026-10-01` to GitHub.
7. Working repository moved to the rewritten history with `git reset --soft` (same tree, no file touched); tags refreshed; watchdogs restarted at 17:57 IST. Agents were writing throughout; none of their files was affected.

## Numbers
Third-party paths removed from history: 1,533 (835 were still tracked at HEAD; 166 MB of blobs in history). Repository size after the rewrite: 617 MB (from 738 MB).

## What this does not do
- GitHub may keep the old commits reachable by their IDs for some time (cached views); complete removal there needs a request to GitHub Support. Clones or forks made by others before today keep the old history.
- The earlier backup bundles in the home folder (2026-09-09, 2026-09-25, 2026-10-01) contain the purged files by design; they are local.
- The published certificate archive (Zenodo, and `results/arxiv/haglund-counterexample/haglund-counterexample-certificate.zip`) contains ten saved pages of the NIST Digital Library of Mathematical Functions (five sections, as HTML and text, under `certificate/producer-B/lit/`). It was left as published; removing them would be a new Zenodo version with a new archive hash — the sponsor's decision.
- Every commit ID changed. No paper cites one; the Zenodo record cites the repository URL and the archive hash.
