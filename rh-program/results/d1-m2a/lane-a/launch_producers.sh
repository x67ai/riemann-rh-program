#!/bin/bash
# launch_producers.sh -- detached launch of the FULL Lane A run, exactly PLAN.md §3.5's two command lines
# (one process per leg, resumable, per-row checkpoints under batches/, STATUS.json in this directory).
# Session 19 builder, 2026-09-09.  macOS has no setsid: nohup + & + disown, stdin from /dev/null.
# Thermal cap (BRIEF.md): refuses to start when more than 2 heavy jobs (processes above 50% CPU) already run (two legs + 2 = cap 4).
# Resume after a kill: run this script again (rows on disk with ok = true are skipped; tail + assemble re-run, seconds/minutes).
# NOTE: the PLAN's lines use ">" so a re-run OVERWRITES producers-mp.log / producers-arb.log -- copy them aside first if they matter.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"; cd "$HERE" || exit 1
LOG="producers.log"
heavy=$(ps -axo pcpu=,command= | awk '$1 > 50.0 && $0 !~ /awk|ps -axo/' | wc -l | tr -d ' ')  # 21:44 IST: heavy = processes above 50% CPU (name patterns were noisy: the legs run as '/Library/.../Python p9_*.py', the status line spawns short-lived pythons, 'lake' matches other names)
{
  echo "== launch_producers.sh $(date)  host $(hostname)  cwd $HERE  heavy-jobs-before=$heavy  caffeinate-pid=$(pgrep -x caffeinate | head -1)"
  ps -axo pcpu=,command= | awk '$1 > 50.0 && $0 !~ /awk|ps -axo/' | sed "s/^/==   heavy: /"
  if [ "$heavy" -gt 2 ]; then echo "== REFUSED: $heavy heavy jobs already running (cap 4; the two legs need 2)"; exit 9; fi
  echo "== mp : nohup ./run_leg.sh mp  . > producers-mp.log  2>&1 &"
  nohup ./run_leg.sh mp  . > producers-mp.log  2>&1 < /dev/null &
  MP=$!; disown "$MP"; echo "$MP" > producers-mp.pid
  echo "== mp  pid $MP  (stdout/stderr: producers-mp.log)"
  echo "== arb: nohup ./run_leg.sh arb . > producers-arb.log 2>&1 &"
  nohup ./run_leg.sh arb . > producers-arb.log 2>&1 < /dev/null &
  ARB=$!; disown "$ARB"; echo "$ARB" > producers-arb.pid
  echo "== arb pid $ARB  (stdout/stderr: producers-arb.log)"
  echo "== poll: STATUS.json (top-level roll-up + per-leg dicts), STATUS-mp.json, STATUS-arb.json, batches/<leg>-row_000k.json, batches/<leg>-tail.json, asym-<leg>.json"
} >> "$LOG" 2>&1
cat "$LOG"
