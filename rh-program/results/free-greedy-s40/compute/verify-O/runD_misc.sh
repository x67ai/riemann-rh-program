#!/bin/bash
# Run D (after A, B, C): time-weighted E statistics for pi/4 to 1e9; the rational control rho = 4/5 to 1e8;
# the argument-principle count at X = 1e6; Newton at 1e8 for three high zeros. One process at a time.
D="$(cd "$(dirname "$0")" && pwd)"; B=/private/tmp/rh-s41-read-compute
read TFX T R < <(python3 "$D/params_o.py" pi4)
S8O_STATS="$D/logs/o_pi4_1e9.Estats" "$B/s8o_stats" $TFX $T $R 1e9 16000000 > "$D/logs/o_pi4_1e9_stats.log" 2>/dev/null
read TFX T R < <(python3 "$D/params_o.py" r08)
"$B/s8o_stats" $TFX $T $R 1e8 16000000 > "$D/logs/o_r08_1e8.log" 2>/dev/null
"$B/zcount_o" "$B/gint_pi4_1e8.f64" 1e6 0.78539816339744830962 0.5 1.05 0.01 200 10 0.02 > "$D/logs/zcount_o_pi4_1e6.txt"
"$B/zt" "$B/gint_pi4_1e8.f64" 1e8 0.78539816339744830962 newton 0.7536 307.455 0.7071 396.447 0.7009 766.131 > "$D/logs/zt_pi4_1e8_high.txt"
