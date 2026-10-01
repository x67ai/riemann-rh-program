#!/bin/bash
# read-O (U1-lookahead), target (d): does the block-edge bug change any number of free-greedy-s40/theory/NOTE.md §3.1?
# Runs the ORIGINAL s40 script and a copy patched ONLY in the cofactor search (widened by 1e-12 relative, as U1's fix;
# the membership test v in [B, Bh) on the computed product is unchanged), same seeds. Copies live in $BIN (scratch).
# Usage: bash s8w_bugcheck.sh "X W SEED" ...
set -u
S40="$(cd "$(dirname "$0")/../../../free-greedy-s40/theory/verify" && pwd)"
BIN=/private/tmp/rh-s41-read-lemmaB-s41U1-lookahead; mkdir -p "$BIN"
cp "$S40/s8w_block.py" "$BIN/s8w_orig.py"
sed -e "s|lo = np.searchsorted(G, B / q, side='left'); hi = np.searchsorted(G, Bh / q, side='left')|lo = np.searchsorted(G, B / q * (1 - 1e-12), side='left'); hi = np.searchsorted(G, Bh / q * (1 + 1e-12), side='left')|" \
    "$S40/s8w_block.py" > "$BIN/s8w_fixed.py"
diff "$BIN/s8w_orig.py" "$BIN/s8w_fixed.py" > /dev/null && { echo "PATCH DID NOT APPLY"; exit 1; }
for cfg in "$@"; do set -- $cfg
  echo "== X=$1 w=$2 seed=$3"
  echo -n "orig : "; python3 "$BIN/s8w_orig.py" "3.141592653589793/16" "$1" "$2" "$3"
  echo -n "fixed: "; python3 "$BIN/s8w_fixed.py" "3.141592653589793/16" "$1" "$2" "$3"
done
