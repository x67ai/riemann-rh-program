#!/bin/bash
# CHECK-O clean-clone build script (Opus 5 checker, Session 32). Written by the checker.
RP="/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program"
C="$HOME/rh-lean-work/checker-clone-s32-i1"
export PATH="$HOME/.elan/bin:$PATH"
echo "=== start $(date) ==="
for i in $(seq 1 60); do git clone https://github.com/anthropics/zeta-23-lean "$C" && break; rm -rf "$C"; sleep 60; done
cd "$C" || exit 99
git checkout v1.0 || exit 98
echo "HEAD=$(git rev-parse HEAD)"
cp -R "$RP/lean/Zeta23/." Zeta23/
cp -R "$RP/lean/comparator/." comparator/
cp "$RP/lean/Zeta23.lean" Zeta23.lean
echo "toolchain=$(cat lean-toolchain)"
for i in $(seq 1 30); do lake exe cache get && break; sleep 60; done
echo "mathlib=$(git -C .lake/packages/mathlib rev-parse HEAD)"
echo "=== build EpsteinWitnessSix $(date) ==="
/usr/bin/time -p lake build Solution.EpsteinWitnessSix; echo "rc=$?"
echo "=== build I1Witness $(date) ==="
/usr/bin/time -p lake build Solution.I1Witness; echo "rc=$?"
echo "=== end $(date) ==="
