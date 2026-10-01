#!/bin/bash
# Run A: S8(pi/4) to X = 1e10 with zeta moments at rho1 (complex) and at 0.515 (real), J = 30, lambda = 0.05
D="$(cd "$(dirname "$0")" && pwd)"
export S8O_XCP="2.5e9,5e9" S8O_J=30 S8O_CENTERS="0.8962124913:14.5499355887:0.05,0.515:0:0.05" S8O_MOM="$D/logs/o_pi4_1e10.mom"
/usr/bin/time -l "$D/run_o.sh" pi4 1e10 > "$D/logs/o_pi4_1e10.log" 2> "$D/logs/o_pi4_1e10.err"
