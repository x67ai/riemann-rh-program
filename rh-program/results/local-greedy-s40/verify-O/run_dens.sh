#!/bin/bash
# run_dens.sh -- read-O: the other densities of NOTE Table 2.1 at 10^9 (no dump), rho = 3/2 at 10^8, and 10^8 dumps for the
# route-2 spot checks at rho = 0.75, 0.8, 1.1. Scratch in /private/tmp/rh-s41-read-localgreedy (dumps 200 MB each).
T=/private/tmp/rh-s41-read-localgreedy; L="$(cd "$(dirname "$0")" && pwd)/logs"
for nd in "3 4" "4 5" "9 10" "11 10" "5 4"; do set -- $nd; "$T/gen7o" $1 $2 0 1000000000 - > "$L/gen7o_r$1-$2_cap0_X1e9.log"; done
"$T/gen7o" 3 2 0 100000000 - > "$L/gen7o_r3-2_cap0_X1e8.log"
for nd in "3 4" "4 5" "11 10"; do set -- $nd; "$T/gen7o" $1 $2 0 100000000 "$T/g_r$1-$2_1e8.u16" > /dev/null; done
echo finished > "$T/dens.done"
