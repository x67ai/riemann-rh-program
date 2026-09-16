#!/bin/sh
cd "$(dirname "$0")" || exit 1
run() { s="$1"; base="${s%.py}"; echo "=== $s  $(date)"; ( time python3 -u "$s" "${base}_out.json" ) > "${base}_run.log" 2>&1; echo "exit=$?" >> "${base}_run.log"; tail -3 "${base}_run.log"; }
run lemma_G_constants.py
run dh_negative_control.py
echo "REST DONE $(date)"
