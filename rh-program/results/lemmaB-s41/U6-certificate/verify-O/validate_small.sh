#!/bin/bash
# validate_small.sh — s8gen against the definition-level brute force, cell by cell (read-O, U6).
# For D in {16, 32} at X = 2e5: (1) brute.py (mpmath 60 digits, heap sweep) writes the cell of every composite;
# (2) s8gen dumps the cell of every composite; the sorted lists must be identical, and so must the g-primes;
# (3) s8gen reruns with tiny segments (2^4 cells) and with the exact path forced (S8G_FTEST=3: every decision whose
#     fast-path margin is below 2^-3 goes through the 320-bit path): moment files and dumps must be byte-identical.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"; S=/private/tmp/rh-s41-U6-second; G=$S/s8gen
cc -O2 -Wall -Wno-unused-function -o "$G" "$HERE/s8gen.c" -lm
cd "$S"
for D in 16 32; do
  X=200000
  K=$(python3 -c "from flint import arb; print(int((arb.pi()*($X-1)/$D+arb(1)/2).floor().unique_fmpz()))")
  python3 "$HERE/consts.py" $D $K params_v$D.txt > /dev/null
  python3 "$HERE/brute.py" $D $X | head -8
  S8G_DUMP=dump_v$D.txt "$G" params_v$D.txt mv$D 20 2>/dev/null | grep -E 'CHECK|FINAL|composites|closest'
  grep -v PRIMES dump_v$D.txt | sort > a.txt; grep -v PRIMES brute_${D}_$X.txt | sort > b.txt
  if cmp -s a.txt b.txt; then echo "D=$D: cells of all $(wc -l < a.txt | tr -d ' ') composites IDENTICAL to brute force"; else echo "D=$D: CELL MISMATCH"; exit 1; fi
  python3 -c "
a=open('dump_v$D.txt').read().split('PRIMES')[1].split(); b=open('brute_${D}_$X.txt').read().split('PRIMES')[1].split()
assert a == b[:len(a)], 'PRIME MISMATCH'
print('D=$D: the %d stored g-primes (all <= x_K/p1) equal the first %d of the brute force (%d in all)' % (len(a), len(a), len(b)))"
  S8G_DUMP=dump_s$D.txt "$G" params_v$D.txt ms$D 4 2>/dev/null > /dev/null
  S8G_FTEST=3 S8G_DUMP=dump_f$D.txt "$G" params_v$D.txt mf$D 20 2>/dev/null | grep -E 'fallbacks'
  for x in blk ind; do cmp mv$D.$x ms$D.$x && cmp mv$D.$x mf$D.$x && echo "D=$D: .$x identical (normal / 2^4-cell segments / forced exact path)"; done
  sort dump_s$D.txt | cmp - <(sort dump_v$D.txt) && sort dump_f$D.txt | cmp - <(sort dump_v$D.txt) && echo "D=$D: dumps identical in all three runs"
done
