#!/bin/bash
# Route 2 for alpha (S5, rho = 0.8): arg-principle data on vertical lines and horizontal segments, X = 3e7.
cd "$(dirname "$0")"
BIG="/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math/a1ca2244-cf17-4f92-9355-9db717d0d6ae/scratchpad/big"
X=3e7
for sg in 0.60 0.65 0.70 0.75 0.80 0.90 1.10; do
  ./zscan "$BIG/a_r0.8.u16" $X 0.8 300 v $sg 0.1 60 0.05 > logs/zeros/r0.8_v${sg}_X$X.txt
done
for t in 0.1 60; do ./zscan "$BIG/a_r0.8.u16" $X 0.8 300 h $t 0.6 1.1 0.002 > logs/zeros/r0.8_h${t}_X$X.txt; done
echo done > logs/zeros/r0.8_X$X.done
