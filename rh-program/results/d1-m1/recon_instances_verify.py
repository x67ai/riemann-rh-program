"""recon_instances_verify.py -- RECONCILIATION (2026-09-02): independent back-parse of the
program file lean/Zeta23/W1/Instances.lean (emitted by emit_lean.py, UNTRUSTED) against the
acceptance transcripts, field by field and row by row.  Reuses auditor O's reader
(audit_O_leancases_verify.py: an independent regex/tokenizer parser sharing no code with the
emitter) pointed at Instances.lean with the 12 clean instances.  A single mismatch would make
every kernel verdict in Instances.lean evidence about nothing."""
import sys
import audit_O_leancases_verify as V

V.LEAN = "/Users/jaytyagi/rh-lean-work/zeta-23-lean-main/Zeta23/W1/Instances.lean"
V.INSTANCES = [
    ("mpNullT100",     "w1-mp-null-t100.json",       "clean"),
    ("arbNullT100",    "w1-arb-null-t100.json",      "clean"),
    ("mpNullT1000",    "w1-mp-null-t1000.json",      "clean"),
    ("arbNullT1000",   "w1-arb-null-t1000.json",     "clean"),
    ("mpNullT10000",   "w1-mp-null-t10000.json",     "clean"),
    ("arbNullT10000",  "w1-arb-null-t10000.json",    "clean"),
    ("mpNullDeepT100", "w1-mp-null-deep-t100.json",  "clean"),
    ("arbNullDeepT100","w1-arb-null-deep-t100.json", "clean"),
    ("mpDH",           "w1-mp-dh-livefire.json",     "clean"),
    ("arbDH",          "w1-arb-dh-livefire.json",    "clean"),
    ("posMP_rej",      "w1-poscontrol-mp.json",      "clean"),
    ("posARB_rej",     "w1-poscontrol-arb.json",     "clean"),
]

if __name__ == "__main__":
    print("RECONCILER -- Instances.lean literals vs acceptance/*.json (independent back-parse, O's reader)")
    sys.exit(1 if V.main() else 0)
