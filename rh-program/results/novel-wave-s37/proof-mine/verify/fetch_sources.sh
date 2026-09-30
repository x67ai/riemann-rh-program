#!/bin/bash
# Fetch free source texts for seed M2 proof-mine. Retries each URL (network is patchy). Log: fetch_sources.log
D="/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/novel-wave-s37/proof-mine/sources"
LOG="/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/novel-wave-s37/proof-mine/verify/fetch_sources.log"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
get() { # name url
  local name="$1" url="$2" out="$D/$1"
  for i in 1 2 3 4 5 6; do
    if curl -sSL -A "$UA" --max-time 120 -o "$out" "$url"; then
      if head -c 5 "$out" | grep -q "%PDF"; then echo "$(date '+%F %T') OK   $name <- $url ($(wc -c < "$out") bytes)" >> "$LOG"; return 0; fi
      echo "$(date '+%F %T') NOPDF $name <- $url (try $i; $(head -c 60 "$out" | tr -d '\n'))" >> "$LOG"; rm -f "$out"; return 1
    fi
    echo "$(date '+%F %T') RETRY $name (try $i)" >> "$LOG"; sleep 30
  done
  echo "$(date '+%F %T') FAIL $name <- $url" >> "$LOG"; return 1
}
get bombieri-1973-bourbaki430-stepanov.pdf "http://www.numdam.org/item/SB_1972-1973__15__234_0.pdf" || \
get bombieri-1973-bourbaki430-stepanov.pdf "http://www.numdam.org/article/SB_1972-1973__15__234_0.pdf"
get deligne-1974-weil-I-pmihes43.pdf "http://www.numdam.org/item/PMIHES_1974__43__273_0.pdf" || \
get deligne-1974-weil-I-pmihes43.pdf "http://www.numdam.org/article/PMIHES_1974__43__273_0.pdf"
get laumon-1987-fourier-weil-pmihes65.pdf "http://www.numdam.org/item/PMIHES_1987__65__131_0.pdf" || \
get laumon-1987-fourier-weil-pmihes65.pdf "http://www.numdam.org/article/PMIHES_1987__65__131_0.pdf"
get weil-1949-numbers-of-solutions-bams55.pdf "https://www.ams.org/journals/bull/1949-55-05/S0002-9904-1949-09219-4/S0002-9904-1949-09219-4.pdf"
get kedlaya-2006-fourier-p-adic-weil-II-math0210149.pdf "https://arxiv.org/pdf/math/0210149"
get hrushovski-frobenius-elementary-theory-math0406514.pdf "https://arxiv.org/pdf/math/0406514"
get sutherland-18783-hasse-lecture.pdf "https://math.mit.edu/classes/18.783/2019/LectureNotes7.pdf" || \
get sutherland-18783-hasse-lecture.pdf "https://math.mit.edu/classes/18.783/2017/LectureNotes7.pdf"
get kowalski-exp-sums-elementary.pdf "https://people.math.ethz.ch/~kowalski/exp-sums.pdf"
echo "$(date '+%F %T') DONE" >> "$LOG"
