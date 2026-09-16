#!/bin/sh
# runs the six verify scripts SEQUENTIALLY (one process at a time), logging each; run from results/c2-m2/verify
cd "$(dirname "$0")" || exit 1
run() { s="$1"; base="${s%.py}"; echo "=== $s  $(date)"; ( time python3 "$s" "${base}_out.json" ) > "${base}_run.log" 2>&1; echo "exit=$?" >> "${base}_run.log"; tail -3 "${base}_run.log"; }
run gevrey_edge_law_rerun.py
diff <(grep -v '^done in' gevrey_edge_law_rerun_run.log | grep -v '^real\|^user\|^sys\|^exit' ) <(grep -v '^done in' ../../c2-m5/verify-next/gevrey_edge_law_run.log | grep -v '^exit') > gevrey_edge_law_rerun_DIFF.txt 2>&1; echo "diff lines vs pricing log: $(wc -l < gevrey_edge_law_rerun_DIFF.txt)"
run b1_constant.py
run edge_law_two_sided.py
run lemma_G_constants.py
run four_point_accounting.py
run dh_negative_control.py
echo "ALL DONE $(date)"
