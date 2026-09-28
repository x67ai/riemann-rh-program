#!/usr/bin/env bash
# linux-comparator-check.sh — the program's independent kernel run on a LINUX host, with a REAL landrun sandbox.
#
# Written Session 30 (2026-09-29) for the sponsor's Linux machine. Every Mac run of leanprover/comparator so far used the
# comparator's own fake-landrun.sh (macOS has no Landlock), so the sandbox guarantee — that an untrusted Solution build cannot
# tamper with the trusted Challenge build — was never exercised. This script reproduces the Session-30 runs (D5 = topics
# WeilContainment and WeilContainmentOne; IV.17 = topic IntegralityGap) from a fresh clone, on a different OS and CPU, with
# landrun real, and writes every log to ~/rh-lean-linux/logs/. Nothing is installed with sudo; nothing is posted anywhere.
#
# Usage (three commands, from any directory on the Linux machine):
#   git clone https://github.com/x67ai/riemann-rh-program ~/riemann-rh-program     # your private repo; GitHub login needed once
#   bash ~/riemann-rh-program/rh-program/scripts/linux-comparator-check.sh
#   ls ~/rh-lean-linux/logs                                                       # send this folder back, or commit it
#
# Needs on the machine: git, curl, tar, a C compiler and make (Debian/Ubuntu: `sudo apt install build-essential git curl` once),
# about 12 GB of free disk, 8 GB of RAM, a Linux kernel with Landlock (5.13 or newer; every mainstream distro since 2021).
# Everything else (elan + the pinned Lean, Rust, Go, Mathlib's prebuilt cache, the four tools) is fetched by this script into
# $HOME with retry loops. First run: roughly 30–60 minutes, most of it downloads and the one-time compile of the Zeta23 library.

set -u
ROOT="$HOME/rh-lean-linux"; LOGS="$ROOT/logs"; TOOLS="$ROOT/tools"
PROG="${1:-$HOME/riemann-rh-program/rh-program}"   # the rh-program directory of your clone
mkdir -p "$LOGS" "$TOOLS"
MAIN="$LOGS/00-main.log"; exec > >(tee -a "$MAIN") 2>&1
echo "=== linux-comparator-check start $(date '+%Y-%m-%d %H:%M:%S %Z') ==="
uname -a; echo "host: $(hostname); cores: $(nproc); mem: $(free -g 2>/dev/null | awk '/Mem/{print $2" GB"}'); disk free: $(df -h "$HOME" | awk 'NR==2{print $4}')"
[ -d "$PROG/lean/comparator" ] || { echo "ERROR: rh-program not found at $PROG (pass its path as the first argument)"; exit 2; }
echo "program checkout: $PROG @ $(git -C "$PROG" rev-parse --short HEAD 2>/dev/null)"

retry() { local n=$1; shift; local i; for i in $(seq 1 "$n"); do "$@" && return 0; echo "  (attempt $i failed: $*) — waiting 60 s"; sleep 60; done; return 1; }
STATUS=()
mark() { STATUS+=("$1: $2"); echo "### $1: $2"; }

# ---------- 1. toolchains: elan, Rust, Go (user-level, no sudo) ----------
export PATH="$HOME/.elan/bin:$HOME/.cargo/bin:$HOME/go-sdk/go/bin:$PATH"
if ! command -v elan >/dev/null; then retry 10 bash -c 'curl -sSf https://elan.lean-lang.org/elan-init.sh | sh -s -- -y --default-toolchain none' || mark elan FAIL; fi
command -v elan >/dev/null && mark elan "ok ($(elan --version))"
if ! command -v cargo >/dev/null; then retry 10 bash -c 'curl -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal' || mark rust FAIL; fi
command -v cargo >/dev/null && mark rust "ok ($(cargo --version))"
if ! command -v go >/dev/null; then
  GOV=$(curl -sSL 'https://go.dev/VERSION?m=text' | head -1); ARCH=$(uname -m); case "$ARCH" in x86_64) GA=amd64;; aarch64|arm64) GA=arm64;; *) GA=amd64;; esac
  mkdir -p "$HOME/go-sdk" && retry 10 bash -c "curl -sSL https://go.dev/dl/${GOV}.linux-${GA}.tar.gz | tar -xz -C '$HOME/go-sdk'" || mark go FAIL
fi
command -v go >/dev/null && mark go "ok ($(go version))"

# ---------- 2. the Lean tree: zeta-23-lean at v1.0 + the program's overlay (lean/README.md "Building") ----------
TREE="$ROOT/zeta-23-lean"
if [ ! -d "$TREE/.git" ]; then retry 30 git clone -q https://github.com/anthropics/zeta-23-lean "$TREE" || { mark clone FAIL; exit 3; }; fi
git -C "$TREE" checkout -q 3635e74826a4c1fcece7d1cd2b6fa75e43a00510 && mark clone "ok (v1.0 = $(git -C "$TREE" rev-parse --short HEAD))"
cp -R "$PROG/lean/Zeta23/." "$TREE/Zeta23/" && cp -R "$PROG/lean/comparator/." "$TREE/comparator/" && cp "$PROG/lean/Zeta23.lean" "$TREE/Zeta23.lean" && mark overlay ok
cd "$TREE" || exit 3
echo "toolchain: $(cat lean-toolchain)"; retry 10 lake --version >/dev/null || mark lake FAIL   # elan installs the pinned Lean here
echo "lean: $(lean --version)"
retry 10 lake exe cache get > "$LOGS/01-cache-get.log" 2>&1 && mark cache "ok (mathlib $(git -C .lake/packages/mathlib rev-parse --short HEAD))" || mark cache FAIL
# Zeta23 itself is not in Mathlib's cache: build it once (the parent's own record: ~9100 jobs, a few minutes)
lake build Zeta23 > "$LOGS/02-build-zeta23.log" 2>&1 && mark "build Zeta23" "ok ($(grep -c . "$LOGS/02-build-zeta23.log") log lines)" || mark "build Zeta23" FAIL
# quick check (no extra tooling): #print axioms for the three Session-30 topics
for T in WeilContainment WeilContainmentOne IntegralityGap; do
  lake build "Solution.$T" > "$LOGS/03-build-solution-$T.log" 2>&1 && lake env lean "comparator/PrintAxioms/$T.lean" > "$LOGS/04-print-axioms-$T.log" 2>&1 \
    && mark "print-axioms $T" "$(grep -c 'depends on axioms: \[propext, Classical.choice, Quot.sound\]' "$LOGS/04-print-axioms-$T.log") names on the three standard axioms; sorryAx: $(grep -c sorryAx "$LOGS/04-print-axioms-$T.log")" \
    || mark "print-axioms $T" FAIL
done

# ---------- 3. the four tools at the recorded revisions (results/d1-m2a/packaging/COMPARATOR-RUN.md §1) ----------
cd "$TOOLS"
[ -d lean4export ] || retry 30 git clone -q https://github.com/leanprover/lean4export
(cd lean4export && git checkout -q 9fb131bb100eb32ccf6836f14e4f8328d13b6792 && lake build > "$LOGS/05-build-lean4export.log" 2>&1) && mark lean4export ok || mark lean4export FAIL
[ -d comparator ] || retry 30 git clone -q https://github.com/leanprover/comparator
(cd comparator && git checkout -q 3927ad383f208ae977c340a91c48ac9b497d2097 && lake build > "$LOGS/06-build-comparator.log" 2>&1) && mark comparator ok || mark comparator FAIL
[ -d nanoda_lib ] || retry 30 git clone -q https://github.com/ammkrn/nanoda_lib
(cd nanoda_lib && git checkout -q 4c544ed4099c8227f07d5de77ad1e69fb0740a27 && cargo build --release > "$LOGS/07-build-nanoda.log" 2>&1) && mark nanoda ok || mark nanoda FAIL
[ -d landrun ] || retry 30 git clone -q https://github.com/Zouuup/landrun
(cd landrun && git checkout -q 811cfff51ceaf3d9843708aa6d22e9b84ccac8b4 && go build -o landrun ./cmd/landrun > "$LOGS/08-build-landrun.log" 2>&1) && mark landrun "built" || mark landrun FAIL
export COMPARATOR_LANDRUN="$TOOLS/landrun/landrun"
export COMPARATOR_LEAN4EXPORT="$TOOLS/lean4export/.lake/build/bin/lean4export"
export COMPARATOR_NANODA="$TOOLS/nanoda_lib/target/release/nanoda_bin"
COMPARATOR="$TOOLS/comparator/.lake/build/bin/comparator"
export PATH="$TOOLS/landrun:$TOOLS/nanoda_lib/target/release:$PATH"
# landrun sanity: REAL sandbox available? (this is the whole point of the Linux run)
if "$COMPARATOR_LANDRUN" --rox / -- /bin/true > "$LOGS/09-landrun-test.log" 2>&1; then mark "landrun sandbox" "REAL (Landlock works on this kernel)"; else mark "landrun sandbox" "FAIL — see 09-landrun-test.log (kernel without Landlock?)"; fi
echo "tool hashes:"; sha256sum "$COMPARATOR" "$COMPARATOR_LEAN4EXPORT" "$COMPARATOR_NANODA" "$COMPARATOR_LANDRUN" | tee "$LOGS/10-tool-hashes.txt"

# ---------- 4. the comparator runs (from the repository root; comparator builds Challenge/Solution itself) ----------
cd "$TREE"
# comparator README assumption 2: do not rely on pre-built Challenge/Solution — remove the quick check's artifacts first
rm -rf .lake/build/lib/lean/Challenge .lake/build/lib/lean/ChallengeDeps .lake/build/lib/lean/Solution .lake/build/ir/Challenge .lake/build/ir/ChallengeDeps .lake/build/ir/Solution 2>/dev/null
for CFG in config-weil-containment-one.json config-weil-containment.json config-integrality-gap.json; do
  L="$LOGS/11-comparator-${CFG%.json}.log"
  { echo "=== $CFG start $(date '+%Y-%m-%d %H:%M:%S %Z') ==="; cat "comparator/$CFG"; echo "lean: $(lean --version)"; echo "mathlib: $(git -C .lake/packages/mathlib rev-parse HEAD)"; env | grep '^COMPARATOR_';
    /usr/bin/time -v lake env "$COMPARATOR" "comparator/$CFG"; rc=$?; echo "--- comparator exit code: $rc ---"; echo "=== end $(date '+%Y-%m-%d %H:%M:%S %Z') ==="; exit $rc; } > "$L" 2>&1
  rc=$?; if [ $rc -eq 0 ] && grep -q 'Your solution is okay!' "$L"; then mark "comparator $CFG" "PASS (exit 0; nanoda: $(grep -c 'Nanoda kernel accepts' "$L"); fake-landrun warnings: $(grep -c 'NOT REAL LANDRUN' "$L"))"; else mark "comparator $CFG" "FAIL (exit $rc) — see $(basename "$L")"; fi
done

# ---------- 5. summary ----------
echo; echo "=== SUMMARY $(date '+%Y-%m-%d %H:%M:%S %Z') ==="; printf '%s\n' "${STATUS[@]}" | tee "$LOGS/99-summary.txt"
echo "Logs: $LOGS  (send this folder back, or copy it into rh-program/results/linux-check-s30/ and commit)"
