#!/bin/bash
# usage: q.sh <query> <max> <name>
for i in $(seq 1 5); do curl -s -m 60 "http://export.arxiv.org/api/query?search_query=$1&max_results=$2" -o "$3.xml" && [ -s "$3.xml" ] && break; sleep 20; done
grep -E "<title>|<id>" "$3.xml" | sed 's/<[^>]*>//g' | paste - - | cut -c1-170
