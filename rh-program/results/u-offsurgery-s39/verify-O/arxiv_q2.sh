#!/bin/bash
# arxiv_q.sh -- prior-art queries for read-O (one at a time, >= 6 s apart, 60 s backoff on rate limit, up to 20 tries)
cd "$(dirname "$0")/sources"
i=0
while IFS='|' read -r tag q; do
  i=$((i+1)); out="arxiv-$tag.xml"
  for try in $(seq 1 20); do
    curl -s -L -m 60 -o "$out" "https://export.arxiv.org/api/query?search_query=$q&start=0&max_results=40" 
    if [ -s "$out" ] && ! grep -q -i "rate exceeded" "$out" && grep -q "<feed" "$out"; then echo "$(date '+%H:%M') $tag ok $(grep -c '<entry>' "$out") entries"; break; fi
    echo "$(date '+%H:%M') $tag try $try failed; sleeping 60"; sleep 60
  done
  sleep 7
done <<'QL'
lagarias-delone|au:Lagarias+AND+all:Delone
lagarias-beurling|au:Lagarias+AND+all:Beurling
zhang2|au:Zhang+AND+ti:Beurling
maamori|au:Maamori
olofsson|au:Olofsson+AND+all:Beurling
gint-integers|all:%22generalized+integers%22+AND+all:%22natural+numbers%22
beurl-intvalued|ti:Beurling+AND+abs:%22integer+valued%22
beurl-multiplicity|ti:Beurling+AND+abs:multiplicities+AND+abs:integers
beurl-recent|cat:math.NT+AND+abs:Beurling
QL
