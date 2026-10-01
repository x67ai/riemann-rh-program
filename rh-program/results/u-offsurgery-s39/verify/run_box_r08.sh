#!/bin/bash
# Winding number of zeta_P (S5, rho = 0.8) around the zero near 0.76587 + 30.32606i, X = 1e9 (all computed data).
cd "$(dirname "$0")"
BIG="/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math/a1ca2244-cf17-4f92-9355-9db717d0d6ae/scratchpad/big"
A="$BIG/a_r0.8.u16"; X=1e9
./zscan "$A" $X 0.8 0 h 30.306 0.7459 0.7859 0.001 > logs/zeros/box30_bottom.txt
./zscan "$A" $X 0.8 0 v 0.7859 30.306 30.346 0.001 > logs/zeros/box30_right.txt
./zscan "$A" $X 0.8 0 h 30.346 0.7459 0.7859 0.001 > logs/zeros/box30_top.txt
./zscan "$A" $X 0.8 0 v 0.7459 30.306 30.346 0.001 > logs/zeros/box30_left.txt
echo done > logs/zeros/box30.done
