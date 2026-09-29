#!/bin/bash
# Reader (Opus 5) independent novelty searches, standing order 7. One request at a time, 3 s apart, retry loop.
OUT="arxiv-O-2.xml"; : > "$OUT"
qs=(
'abs:"arithmetic site"'
'all:"Riemann hypothesis" AND all:"Witt vectors"'
'abs:"Weil" AND abs:"Spec Z" AND abs:"square"'
'abs:"one residue characteristic" OR abs:"infinitely many residue characteristics"'
'abs:"intersection pairing" AND abs:"Spec Z" AND abs:"Frobenius"'
)
for q in "${qs[@]}"; do
  enc=$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$q")
  url="https://export.arxiv.org/api/query?search_query=${enc}&start=0&max_results=25"
  for i in $(seq 1 60); do
    body=$(curl -sL --max-time 60 "$url") && echo "$body" | grep -q '<feed' && break
    sleep 60
  done
  { echo "<!-- QUERY: $q | $(date) -->"; echo "$body"; } >> "$OUT"
  sleep 3
done
echo done
