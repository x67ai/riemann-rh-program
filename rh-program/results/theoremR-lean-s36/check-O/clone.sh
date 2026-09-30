#!/bin/bash
# CHECK-O clean clone (checker-written, Session 36): anthropics/zeta-23-lean at tag v1.0 into a NEW directory; retry loop for the network.
export PATH="$HOME/.elan/bin:$HOME/.cargo/bin:$HOME/go-sdk/go/bin:$PATH"
C="$HOME/rh-lean-work/checker-clone-s36-residue"
date
[ -e "$C" ] && { echo "REFUSING: $C exists"; exit 98; }
for i in $(seq 1 60); do
  git clone https://github.com/anthropics/zeta-23-lean "$C" && break
  rm -rf "$C"; echo "clone attempt $i failed; retry in 60 s"; sleep 60
done
cd "$C" || exit 99
git checkout -q v1.0 && git log -1 --format='HEAD is now at %h %s'
git rev-parse HEAD
cat lean-toolchain
grep -n -A3 '"name": "mathlib"' lake-manifest.json
grep -n '"rev"' lake-manifest.json | head -3
grep -n '"inputRev"' lake-manifest.json | head -3
git status --short | head
date
