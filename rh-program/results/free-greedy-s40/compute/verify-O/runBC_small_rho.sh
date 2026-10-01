#!/bin/bash
# Runs B, C: S8(pi/16), S8(pi/32) to X = 1e10 with real moments at the real zero (J = 30, lambda = 0.05)
D="$(cd "$(dirname "$0")" && pwd)"
export S8O_J=30
S8O_CENTERS="0.7948:0:0.05" S8O_MOM="$D/logs/o_pi16_1e10.mom" /usr/bin/time -l "$D/run_o.sh" pi16 1e10 > "$D/logs/o_pi16_1e10.log" 2> "$D/logs/o_pi16_1e10.err"
S8O_CENTERS="0.8951:0:0.05" S8O_MOM="$D/logs/o_pi32_1e10.mom" /usr/bin/time -l "$D/run_o.sh" pi32 1e10 > "$D/logs/o_pi32_1e10.log" 2> "$D/logs/o_pi32_1e10.err"
