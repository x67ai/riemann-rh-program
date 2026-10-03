#!/bin/zsh
cd "$(dirname "$0")"
while [ ! -f ../data/queue1.done ]; do sleep 30; done
python3 q2_zeros.py 3128 3160 100 > ../data/q2-zeros.log 2>&1
python3 q2_axis.py 26 3128 3160 > ../data/q2-axis-k26.log 2>&1
python3 q2_axis.py 27 3128 3160 > ../data/q2-axis-k27.log 2>&1
python3 q2_starts.py 27 3128 3160 > ../data/q2-starts-k27.log 2>&1
python3 track.py 27 0.1 ../data/q2-starts-k27.json ../data/q2-track-k27.json 30 > ../data/q2-track-k27.log 2>&1
python3 q2_starts.py 26 3132 3156 > ../data/q2-starts-k26.log 2>&1
python3 track.py 26 0.1 ../data/q2-starts-k26.json ../data/q2-track-k26.json 30 > ../data/q2-track-k26.log 2>&1
echo Q2-DONE > ../data/q2.done
