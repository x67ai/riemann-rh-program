#!/bin/bash
# CHECK-O cold builds (checker-written, Session 36): one lake process at a time, strictly sequential, in the clean clone.
# usage: build.sh <target> <logfile>
export PATH="$HOME/.elan/bin:$HOME/.cargo/bin:$HOME/go-sdk/go/bin:$PATH"
cd "$HOME/rh-lean-work/checker-clone-s36-residue" || exit 99
{
  echo "=== $(date) lake build $1 (clean clone $(pwd))"
  echo "other lake processes before start: $(pgrep -x lake | wc -l | tr -d ' ')"
  /usr/bin/time -l lake build "$1"
  echo "rc=$?"
  echo "=== $(date) end"
} > "$2" 2>&1
