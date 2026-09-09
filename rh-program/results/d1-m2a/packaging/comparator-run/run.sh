#!/bin/bash
# Job 3 runner: run leanprover/comparator on one config from the Lean repository root.
# usage: run.sh <config-relative-to-repo-root> <label>   (stdout+stderr are the caller's redirection)
export PATH="$HOME/.cargo/bin:$HOME/go-sdk/go/bin:$HOME/.elan/bin:$HOME/rh-lean-work/tools/nanoda_lib/target/release:$PATH"
export COMPARATOR_LANDRUN="$HOME/rh-lean-work/tools/comparator/scripts/fake-landrun.sh"
export COMPARATOR_LEAN4EXPORT="$HOME/rh-lean-work/tools/lean4export/.lake/build/bin/lean4export"
export COMPARATOR_NANODA="$HOME/rh-lean-work/tools/nanoda_lib/target/release/nanoda_bin"
COMPARATOR="$HOME/rh-lean-work/tools/comparator/.lake/build/bin/comparator"
cd "$HOME/rh-lean-work/zeta-23-lean-main" || exit 99
echo "=== [$2] start $(date '+%Y-%m-%d %H:%M:%S %Z') ==="
echo "cwd=$(pwd)"; echo "config=$1"; cat "$1"
echo "toolchain=$(cat lean-toolchain)"; echo "lean=$(which lean) $(lean --version)"; echo "lake=$(which lake)"
env | grep '^COMPARATOR_' ; echo "nanoda on PATH: $(which nanoda_bin)"
echo "heavy procs (>50% cpu) before start:"; ps -Ao pcpu,comm | awk '$1>50'
echo "--- comparator output follows ---"
/usr/bin/time -l lake env "$COMPARATOR" "$1"
rc=$?
echo "--- comparator exit code: $rc ---"
echo "=== [$2] end $(date '+%Y-%m-%d %H:%M:%S %Z') ==="
exit $rc
