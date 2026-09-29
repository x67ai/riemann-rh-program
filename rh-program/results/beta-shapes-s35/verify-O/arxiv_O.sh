#!/bin/bash
# Reader (Opus 5) independent novelty searches, standing order 7. One request at a time, 3 s apart, retry loop.
OUT="arxiv-O.xml"; : > "$OUT"
qs=(
'abs:"Witt vectors" AND abs:"intersection" AND abs:"Riemann hypothesis"'
'abs:"field with one element" AND abs:"Hodge index"'
'abs:"Spec Z" AND abs:"Hodge index"'
'abs:"arithmetic site" AND abs:"intersection"'
'abs:"scaling site" AND abs:"Riemann-Roch"'
'abs:"Frobenius correspondences" AND abs:"Riemann hypothesis"'
'abs:"logarithms of primes" AND abs:"linearly independent"'
'abs:"lambda-rings" AND abs:"Riemann hypothesis"'
'abs:"infinite genus" AND abs:"Riemann hypothesis"'
'abs:"ghost map" AND abs:"Cartier"'
'abs:"von Mangoldt" AND abs:"intersection number"'
'abs:"residue characteristics" AND abs:"field with one element"'
'abs:"Weil proof" AND abs:"Spec Z"'
'abs:"arithmetic surface" AND abs:"Riemann hypothesis" AND abs:"Hodge index"'
'abs:"lambda-rings" AND abs:"field with one element"'
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
