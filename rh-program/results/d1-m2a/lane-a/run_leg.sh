#!/bin/bash
# run_leg.sh -- detached Lane A producer driver (one leg): rows (resumable, per-row checkpoints) -> tail row (--direct)
# -> assemble the transcript.  STATUS.json / STATUS-<leg>.json in OUT are the polling files (BRIEF.md).
# usage: nohup ./run_leg.sh mp|arb [OUT=.] > producers-<leg>.log 2>&1 &
# Re-run the same command after a kill: rows already on disk are skipped (--resume); the tail and assembly re-run (seconds).
set -u
LEG="${1:?leg: mp or arb}"; OUT="${2:-.}"
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE" || exit 1
PLAN="rows-plan.json"
case "$LEG" in
  mp)  PROD="p9_mp.py";  NAME="asym-mp.json" ;;
  arb) PROD="p9_arb.py"; NAME="asym-arb.json" ;;
  *) echo "leg must be mp or arb"; exit 2 ;;
esac
echo "== $LEG start $(date) pid $$ host $(hostname) plan $PLAN out $OUT"
python3 "$PROD" rows --plan "$PLAN" --out "$OUT" --resume || { echo "== $LEG rows FAILED $(date)"; exit 3; }
python3 "$PROD" tail --plan "$PLAN" --out "$OUT" --direct   || { echo "== $LEG tail FAILED $(date)"; exit 4; }
python3 "$PROD" assemble --plan "$PLAN" --out "$OUT" --name "$NAME" || { echo "== $LEG assemble FAILED $(date)"; exit 5; }
echo "== $LEG done $(date)"
