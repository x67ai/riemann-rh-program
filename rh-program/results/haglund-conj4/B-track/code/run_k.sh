#!/bin/zsh
# one heavy process at a time: zeros -> real axis -> tracking, sequentially
k=$1; Y0=$2; dt=${3:-0.1}
cd "$(dirname "$0")"
python3 census_zeros.py $k $Y0 > ../data/k$k-zeros.log 2>&1
python3 realaxis.py $k $(python3 -c "import math;print(2*math.pi*($k+2)**2+42)") > ../data/q3-k$k.log 2>&1
python3 track.py $k $dt ../data/k$k-starts.json ../data/k$k-track.json 30 > ../data/k$k-track.log 2>&1
echo DONE >> ../data/k$k-track.log
