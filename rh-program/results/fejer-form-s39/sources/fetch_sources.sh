#!/bin/bash
# Fetch prior-art PDFs from arXiv with a retry loop (network is patchy). Run from sources/.
for id in 1202.6308 1409.2357 1207.6230; do
  f="arxiv-${id}.pdf"
  for i in $(seq 1 30); do
    curl -sfL -A "Mozilla/5.0" -o "$f" "https://arxiv.org/pdf/${id}" && [ -s "$f" ] && head -c 4 "$f" | grep -q "%PDF" && break
    sleep 20
  done
  printf "%s %s %s\n" "$id" "$(ls -l "$f" 2>/dev/null | awk '{print $5}')" "$(shasum -a 256 "$f" 2>/dev/null | cut -c1-16)"
done
for id in 1202.6308 1409.2357 1207.6230; do
  for i in $(seq 1 20); do
    curl -sfL -A "Mozilla/5.0" -o "abs-${id}.html" "https://arxiv.org/abs/${id}" && break; sleep 20
  done
  grep -o '<meta name="citation_title" content="[^"]*"' "abs-${id}.html" | head -1
  grep -o '<meta name="citation_author" content="[^"]*"' "abs-${id}.html" | head -4
done
