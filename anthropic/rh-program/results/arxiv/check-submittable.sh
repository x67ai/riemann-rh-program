#!/usr/bin/env bash
# arXiv submission-readiness checker for the four converted papers.
# Usage:  bash results/arxiv/check-submittable.sh [dir ...]      (run from the program root)
# With no arguments it checks every subdirectory of results/arxiv that holds a main.tex.
export PATH="$HOME/texlive/2026/bin/universal-darwin:$PATH"

fail=0
note()  { printf '    %-34s %s\n' "$1" "$2"; }
bad()   { printf '    %-34s \033[31mFAIL\033[0m  %s\n' "$1" "$2"; fail=1; }
ok()    { printf '    %-34s ok    %s\n' "$1" "$2"; }

dirs=("$@")
if [ ${#dirs[@]} -eq 0 ]; then
  dirs=()
  for d in results/arxiv/*/; do
    [ -f "$d/main.tex" ] && dirs+=("${d%/}")
  done
fi

for d in "${dirs[@]}"; do
  echo "=== $d"
  tex="$d/main.tex"; pdf="$d/main.pdf"; log="$d/main.log"
  [ -f "$tex" ] || { bad "main.tex" "missing"; continue; }

  # 1. it must compile from a clean state, twice, with no errors
  ( cd "$d" && rm -f main.aux main.out main.toc main.log \
      && pdflatex -interaction=nonstopmode main.tex >/dev/null 2>&1 \
      && pdflatex -interaction=nonstopmode main.tex >/dev/null 2>&1 )
  if [ -f "$pdf" ]; then ok "compiles from clean" "$(pdfinfo "$pdf" | awk '/^Pages/{print $2" pp"}')"
  else bad "compiles from clean" "no PDF produced"; continue; fi

  errs=$(grep -c '^!' "$log" 2>/dev/null | head -1); errs=${errs:-0}
  [ "$errs" -eq 0 ] && ok "no TeX errors" "" || bad "no TeX errors" "$errs error line(s)"

  # 2. no undefined references or citations (arXiv rejects nothing for this, referees notice)
  und=$(grep -c 'LaTeX Warning: \(Reference\|Citation\).*undefined' "$log" 2>/dev/null | head -1); und=${und:-0}
  [ "$und" -eq 0 ] && ok "no undefined refs/cites" "" || bad "no undefined refs/cites" "$und"
  qq=$(pdftotext "$pdf" - 2>/dev/null | grep -c '??' | head -1); qq=${qq:-0}
  [ "${qq:-0}" -eq 0 ] && ok "no '??' in output" "" || bad "no '??' in output" "$qq occurrence(s)"

  # 3. overfull boxes that would actually show as text in the margin
  ovf=$(grep -o 'Overfull \\hbox ([0-9.]*pt' "$log" 2>/dev/null | sed 's/[^0-9.]//g' | awk '$1>20' | wc -l | tr -d ' ')
  [ "${ovf:-0}" -eq 0 ] && ok "no overfull box > 20pt" "" || bad "no overfull box > 20pt" "$ovf"

  # 4. arXiv AutoTeX constraints
  grep -q '\\write18\|\\immediate\\write18\|shell-escape' "$tex" \
    && bad "no shell-escape" "\\write18 present" || ok "no shell-escape" ""
  grep -q '\\input{[^}]*}\|\\include{' "$tex" \
    && note "external \\input/\\include" "check those files ship too" || ok "self-contained (no \\input)" ""
  if grep -q '\\includegraphics' "$tex"; then
    note "figures" "$(grep -c '\\includegraphics' "$tex") - confirm the image files ship"
  else ok "no external figures" ""; fi
  # arXiv wants no .aux/.log in the tarball, and a PDF-producing main
  ok "engine" "pdflatex (AutoTeX default)"

  # 5. a title, an author and an abstract must exist
  for m in '\\title' '\\author' 'begin{abstract}'; do
    grep -q -- "$m" "$tex" && ok "has ${m//\\\\/}" "" || bad "has ${m//\\\\/}" "missing"
  done

  # 6. U.S. English (identifiers and quoted titles excepted - eyeball any hit)
  brit=$(grep -n -iE '\b(colour|behaviour|favour|neighbour|centre|fibre|modelling|labelled|travelled|cancelled|maths|grey|towards|programme|defence|offence|licence|analyse|organise|recognise|normalise|characterise)\b' "$tex" | wc -l | tr -d ' ')
  [ "$brit" -eq 0 ] && ok "U.S. English" "" || bad "U.S. English" "$brit hit(s) - inspect"

  # 7. non-ASCII bytes: fine for UTF-8 LaTeX, but arXiv is happier with escapes; report only
  na=$(LC_ALL=C grep -c '[^ -~]' "$tex" | head -1); na=${na:-0}
  [ "${na:-0}" -eq 0 ] && ok "pure ASCII source" "" || note "non-ASCII lines" "${na} (UTF-8 is accepted; verify they render)"

  # 8. the stray build products that should not be in the submission tarball
  extra=$(ls "$d" | grep -vE '^(main\.(tex|pdf|bbl)|refs\.bib|README.*)$' | tr '\n' ' ')
  [ -z "$extra" ] && ok "no stray files" "" || note "not for the tarball" "$extra"
done

echo
[ $fail -eq 0 ] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED (see FAIL lines above)"
exit $fail
