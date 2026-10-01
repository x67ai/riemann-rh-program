#!/bin/sh
# U4-sparse: finite-rho test of Prop. 3.3 (pathwise alternating brackets). Levels 0..3 (level 0 = lattice monoid, mode 1;
# level j>0 = mode 2 with generators = idle set of level j-1), then S8 (mode 0) compared step by step with e^(1) and e^(2).
S=/private/tmp/rh-s41-lemmaB-U4-sparse; V="$(cd "$(dirname "$0")" && pwd)"; cd "$S" || exit 1
for D in 128 64 32; do X=1e9
  while [ "$(ps -Ao pcpu,comm | awk '$1>50' | wc -l)" -ge 4 ]; do sleep 30; done
  ./s8sp $D $X 1 br${D}_L0.tsv br${D}_e0.u16 - br${D}_i0.u8 2> br${D}_L0.err
  ./s8sp $D $X 2 br${D}_L1.tsv br${D}_e1.u16 - br${D}_i1.u8 br${D}_i0.u8 2> br${D}_L1.err
  ./s8sp $D $X 2 br${D}_L2.tsv br${D}_e2.u16 - br${D}_i2.u8 br${D}_i1.u8 2> br${D}_L2.err
  ./s8sp $D $X 2 br${D}_L3.tsv br${D}_e3.u16 - br${D}_i3.u8 br${D}_i2.u8 2> br${D}_L3.err
  ./s8sp $D $X 0 br${D}_S8vs2.tsv br${D}_eS.u16 br${D}_e2.u16 br${D}_iS.u8 2> br${D}_S8.err
  ./s8sp $D $X 0 br${D}_S8vs1.tsv - br${D}_e1.u16 2>> br${D}_S8.err
  python3 "$V/check_brackets.py" $D >> "$V/logs/brackets_finite.log" 2>&1
  cp br${D}_L*.tsv br${D}_S8vs*.tsv "$V/logs/"
  rm -f br${D}_*.u16 br${D}_*.u8
done
echo ALLDONE > "$V/logs/brackets_finite.done"
