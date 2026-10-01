#!/bin/bash
# concavity of F_X on [sigma_1, 1) at x_K ~ 1e10 for the four systems (NOTE §6, Lemma 6.3)
D="$(cd "$(dirname "$0")" && pwd)"; cd "$D"
while read f den sa; do
  { echo "# $(date '+%H:%M IST %Y-%m-%d') concavity.py data/$f.mom $den $sa"; python3 concavity.py "data/$f.mom" "$den" "$sa"; } > "logs/concavity_$f.log" 2>&1
done <<'LIST'
pi16_K1963495408 16 794755370097/1000000000000
pi32_K981747704 32 895076517592/1000000000000
pi64_K490873852 64 947634190223/1000000000000
pi128_K245436926 128 974264562328/1000000000000
LIST
