#!/bin/sh
# Opus reader's runs of s8dd (independent generator). Binary is built into the scratch dir; logs land here.
# Usage: sh run_s8dd.sh <name> <X> <sigma_lo> <sigma_hi> [sigma ...]
# t = 1/rho as a double-double, from mpmath at 60 digits (pairs below; |error| <= 3.4e-33 relative).
BIN="${S8DD_BIN:-/private/tmp/claude-501/s8dd-read-O}"
HERE="$(cd "$(dirname "$0")" && pwd)"
case "$1" in
  pi4)    TH=1.2732395447351628;  TL=-7.871470670072994e-17 ;;
  pi6)    TH=1.909859317102744;   TL=-7.049757588579267e-18 ;;
  pi8)    TH=2.5464790894703255;  TL=-1.5742941340145989e-16 ;;
  pi16)   TH=5.092958178940651;   TL=-3.1485882680291977e-16 ;;
  pi32)   TH=10.185916357881302;  TL=-6.297176536058395e-16 ;;
  pi64)   TH=20.371832715762604;  TL=-1.259435307211679e-15 ;;
  095pi3) TH=1.0051891142646021;  TL=7.976159423117822e-18 ;;
  r08)    TH=1.25;                TL=0 ;;
  *) echo "unknown rho name $1"; exit 1 ;;
esac
NAME="$1"; X="$2"; shift 2
LOG="$HERE/s8dd_${NAME}_${X}.log"
WD="$(mktemp -d /private/tmp/claude-501/s8dd-run.XXXXXX)"
cd "$WD" || exit 1
{ echo "# $(date '+%H:%M IST %Y-%m-%d')  s8dd $NAME X=$X args: $*"; /usr/bin/time -l "$BIN" "$TH" "$TL" "$X" 100 "$@" 2>&1; } > "$LOG" 2>&1
grep -c NEARTIE s8dd_ties.tmp > /dev/null 2>&1; cp s8dd_ties.tmp "$HERE/s8dd_${NAME}_${X}.close.txt" 2>/dev/null
cd / && rm -rf "$WD"
grep -E "^(FINAL|AUDIT|F |ROOT)" "$LOG"
