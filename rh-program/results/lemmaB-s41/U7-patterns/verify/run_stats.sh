#!/bin/bash
cd /private/tmp/rh-s41-lemmaB-U7-patterns
P16=$(python3 -c "import math; print(repr(1+0.5*16/math.pi))"); P32=$(python3 -c "import math; print(repr(1+0.5*32/math.pi))")
/usr/bin/time -l ./stats b16_1e10 5.0929581789406511 0.19634954084936207 0.5 $P16 1e10 400 > b16_1e10.stats 2> b16_1e10.stats.err
/usr/bin/time -l ./stats b32_1e10 10.185916357881302 0.098174770424681035 0.5 $P32 1e10 400 > b32_1e10.stats 2> b32_1e10.stats.err
echo done > run_stats.done
