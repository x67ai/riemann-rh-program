#!/bin/bash
# launch_heights.sh -- the production heights of the zero-side campaign (PRICING 2(e); BRIEF rule 3).
# Batches: (1e4 || 1e5) then (1e6); at most 2 heavy processes at any time (heavy := ps -Ao pcpu,comm | awk '$1>50');
# one process per height, nohup, PID files logs/height_<tag>.pid, per-height logs logs/height_<tag>.log (+ .stdout),
# outputs zeros_<tag>.json + rows_<tag>.{csv,json} + summary_<tag>.json at completion.  This supervisor itself runs
# under nohup (launch it as:  nohup ./launch_heights.sh > logs/launch.stdout 2>&1 &) and exits when 1e6 has finished.
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE" || exit 1
mkdir -p logs
LOG="logs/launch.log"
say() { echo "[$(date '+%Y-%m-%d %H:%M:%S %Z')] $*" | tee -a "$LOG"; }
heavy() { ps -Ao pcpu,comm | awk '$1>50' | wc -l | tr -d ' '; }
wait_for_slot() {   # wait until fewer than $1 heavy processes are running
  while [ "$(heavy)" -ge "$1" ]; do sleep 30; done
}
launch() {
  local tag="$1" t="$2"
  nohup python3 run_height.py --t "$t" --tag "$tag" > "logs/height_$tag.stdout" 2>&1 &
  echo $! > "logs/height_$tag.pid"
  say "launched $tag (t = $t) pid $(cat "logs/height_$tag.pid")"
}
wait_pid() { while kill -0 "$1" 2>/dev/null; do sleep 30; done; }

say "launch_heights.sh START (supervisor pid $$; heavy now: $(heavy))"
echo $$ > logs/launch_heights.pid
# batch 1: 1e4 || 1e5
wait_for_slot 2; launch t1e4 1e4
sleep 5
wait_for_slot 2; launch t1e5 1e5
wait_pid "$(cat logs/height_t1e4.pid)"; say "t1e4 finished (exit status in logs/height_t1e4.log; summary_t1e4.json present: $([ -f summary_t1e4.json ] && echo yes || echo NO))"
wait_pid "$(cat logs/height_t1e5.pid)"; say "t1e5 finished (summary_t1e5.json present: $([ -f summary_t1e5.json ] && echo yes || echo NO))"
# batch 2: 1e6
wait_for_slot 2; launch t1e6 1e6
wait_pid "$(cat logs/height_t1e6.pid)"; say "t1e6 finished (summary_t1e6.json present: $([ -f summary_t1e6.json ] && echo yes || echo NO))"
# harvest: aggregate whatever row files exist into CAMPAIGN.md (v1 if all four heights are present)
python3 aggregate.py >> "$LOG" 2>&1 && say "aggregate.py run; CAMPAIGN.md rebuilt"
say "launch_heights.sh DONE"
