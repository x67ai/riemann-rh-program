#!/bin/bash
# run_cert.sh NAME XMAX  -- builds s8cert into the scratch dir and runs S8(NAME) to XMAX; moments -> data/, log -> logs/
D="$(cd "$(dirname "$0")" && pwd)"
S=/private/tmp/rh-s41-lemmaB-U6-certificate
mkdir -p "$S" "$D/data" "$D/logs"
cc -O2 -Wall -ffp-contract=off -o "$S/s8cert" "$D/s8cert.c" -I/opt/homebrew/include -L/opt/homebrew/lib -lgmp -lm || exit 1
{ echo "# $(date '+%H:%M IST %Y-%m-%d') s8cert $1 $2"; /usr/bin/time -l "$S/s8cert" "$D/params.txt" "$1" "$2" "$D/data/$1"; } > "$D/logs/s8cert_$1_$2.log" 2>&1
echo "# done $(date '+%H:%M IST %Y-%m-%d')" >> "$D/logs/s8cert_$1_$2.log"
