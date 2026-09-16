#!/bin/bash
# checkpoint.sh -- append a dated checkpoint block (controls, stop conditions, derived bandwidths, SHA-256s) for the heights
# named on the command line to results/c2-m2/SHARED.md.   usage: ./checkpoint.sh t1e4 t1e5 [t1e6]   (run from anywhere)
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE" || exit 1
SH="../SHARED.md"
H() { shasum -a 256 "$1" | cut -c1-64; }
{
  echo
  echo "## $(date '+%Y-%m-%d %H:%M %Z') — CAMPAIGN checkpoint (builder \`checkpoint.sh\`): heights $*"
  echo
  for tag in "$@"; do
    L="logs/height_$tag.log"
    if [ ! -f "summary_$tag.json" ]; then echo "* **$tag**: no summary_$tag.json yet (process still running or died; see $L)"; continue; fi
    echo "* **$tag** — $(grep 'zeros done' "$L" | tail -1 | sed 's/^ *//')"
    echo "  * $(grep 'POSITIVE control (zeta' "$L" | tail -1 | sed 's/^ *//')"
    echo "  * $(grep -- '-> NEGATIVE control' "$L" | tail -1 | sed 's/^ *//')"
    grep '^   delta = 0\.[0-9]*: L_sign' "$L" | tail -3 | sed 's/^ *//; s/^/  * at t: /'
    grep 'over [0-9]* centers' "$L" | tail -3 | sed 's/^ *//; s/^/  * ensemble: /'
    echo "  * stop conditions: $(grep '^   (ii) ' "$L" | tail -1 | sed 's/.*-> //'); (iv) $(grep '^   (iv) ' "$L" | tail -1 | sed 's/.*-> //'); $(grep 'any stop condition fires' "$L" | tail -1 | sed 's/.*(summary/(summary/')"
    for f in "zeros_$tag.json" "rows_$tag.csv" "rows_$tag.json" "summary_$tag.json" "logs/height_$tag.log"; do
      echo "  * \`campaign/$f\`  $(H "$f")"
    done
  done
  [ -f CAMPAIGN.md ] && echo "* \`campaign/CAMPAIGN.md\` ($(head -1 CAMPAIGN.md | sed 's/.*-- //'))  $(H CAMPAIGN.md)"
  [ -f dh_offline_scan.json ] && echo "* \`campaign/dh_offline_scan.json\`  $(H dh_offline_scan.json)  — $(grep 'verdict' logs/dh_offline_scan.log | tail -1 | sed 's/.*verdict: //')"
} >> "$SH"
tail -n +1 "$SH" | tail -25
