#!/bin/bash
# run_o.sh NAME X [dumpX dumpfile] -- runs the independent generator s8o
D="$(cd "$(dirname "$0")" && pwd)"
read TFX T R < <(python3 "$D/params_o.py" "$1")
/private/tmp/rh-s41-read-compute/s8o "$TFX" "$T" "$R" "$2" 16000000 "${@:3}"
