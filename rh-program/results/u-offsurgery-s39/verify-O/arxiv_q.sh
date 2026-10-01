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
greedy|all:Beurling+AND+all:greedy
prescribed|all:Beurling+AND+all:integers+AND+all:prescribed
inverse|all:Beurling+AND+all:inverse+AND+all:primes
gprimes-constr|all:%22generalized+primes%22+AND+all:construction+AND+all:integers
gprimes-regular|all:%22g-primes%22+AND+all:integers
dmv|au:Vorhauer
zhang|au:Zhang_Wen-Bin+AND+all:Beurling
bdv|au:Broucke+AND+au:Vindas
almaamori|au:Al-Maamori
neamah|au:Neamah
hilberdink|au:Hilberdink
feedback|all:Beurling+AND+all:algorithm+AND+all:primes
subsemigroup|all:Beurling+AND+all:%22natural+numbers%22+AND+all:%22generalized+integers%22
QL
