#!/bin/sh
# Opus reader (Session 41): every run behind read-O.md section 2, in order. Total about 15 s on this Mac.
cd "$(dirname "$0")" || exit 1
clang -O2 -ffp-contract=off -Wall -o /private/tmp/claude-501/s8dd-read-O s8dd.c -lm || exit 1
# the seven densities of NOTE section 1.8 at X = 10^6 (sigma list: 0.89 for pi/32's certificate)
for r in pi64:0.94:0.96 pi32:0.88:0.90 pi16:0.78:0.80 pi8:0.6:0.7 pi6:0.5:0.6 pi4:0.5:0.6 095pi3:0.3:0.5; do
  n=${r%%:*}; rest=${r#*:}; lo=${rest%%:*}; hi=${rest#*:}
  sh run_s8dd.sh "$n" 1e6 "$lo" "$hi" 0.89 > /dev/null
done
sh run_s8dd.sh pi16 1e7 0.79 0.80 0.78 0.79 0.80 0.81 > /dev/null     # Theorem 4.1 certificate
sh run_s8dd.sh pi4  1e7 0.50 0.60 0.50 0.52 0.55 > /dev/null          # Theorem 4.2 certificate
sh run_s8dd.sh pi16 5e7 0.79 0.80 0.79 0.80 > /dev/null               # sigma* at 5e7, sup E at 10^7.5
sh run_s8dd.sh pi32 1e8 0.89 0.90 0.89 > /dev/null                    # NOTE 3.0 pi/32 to 1e8
sh close_paths.sh                                                     # factorizations of decisions < 1e-12
python3 mp_recheck.py > mp_recheck.log                                # 60-digit recheck of those decisions
python3 tau_check.py > tau_check.log                                  # tail factors and K thresholds
