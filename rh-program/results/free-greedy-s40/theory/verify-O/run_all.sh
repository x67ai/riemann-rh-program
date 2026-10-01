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
# F1 data: Legendre remainder S(u, 2u] (env S8DD_SIEVE) for pi/16 to 5e7 and pi/4 to 1e7
S8DD_SIEVE="1e3,1e4,1e5,1e6,5e6,2.5e7" TAG=.sieve sh run_s8dd.sh pi16 5e7 0 0 > /dev/null
S8DD_SIEVE="1e4,1e5,1e6,5e6" TAG=.sieve sh run_s8dd.sh pi4 1e7 0 0 > /dev/null
python3 legendre_check.py > legendre_check.log                        # Legendre identity exactly; M_lat, M(z) log z
python3 break_thm16.py > break_thm16.log                              # Theorem 1.6 hypothesis (A) on arithmetic systems
python3 r08_exact.py 1000000 > r08_exact_1e6.log                      # rho = 4/5 in exact integers
sh -c 'for r in "pi64 0.950912703473" "pi32 0.901825229590" "pi16 0.803650459" "pi8 0.607300918"; do set -- $r; TAG=.lin sh run_s8dd.sh $1 1e6 0 0 $2 | grep "^F sigma" | awk -v n=$1 -v s=$2 "{split(\$3,a,\"=\"); rho=1-s; printf \"%s 1-rho=%s F(1-rho)=%s first-order sigma*=%.6f\n\", n, s, a[2], s+rho*a[2]}"; done' > lin_check.log
