#!/bin/bash
# Independent nanoda evidence (outside comparator): export the same targets comparator exports from the solution module with
# lean4export to a FILE (so the export size is measurable), then feed that file to nanoda_bin with print_success_message=true so
# nanoda reports how many declarations it checked. Same permitted axioms, nat/string extensions, hard error on unpermitted axioms.
# usage: nanoda-evidence.sh <solution-module> <outdir> <theorem...>
export PATH="$HOME/.cargo/bin:$HOME/go-sdk/go/bin:$HOME/.elan/bin:$PATH"
MOD="$1"; OUT="$2"; shift 2
LEAN4EXPORT="$HOME/rh-lean-work/tools/lean4export/.lake/build/bin/lean4export"
NANODA="$HOME/rh-lean-work/tools/nanoda_lib/target/release/nanoda_bin"
mkdir -p "$OUT"; cd "$HOME/rh-lean-work/zeta-23-lean-main" || exit 99
# the comparator's export target list (Main.lean compareIt): builtinTargets (nanoda on) ++ theorem_names ++ permitted axioms ++ primitiveTargets
BUILTIN="Nat String String.mk Char Quot Quot.mk Quot.lift Quot.ind"
AXIOMS="propext Quot.sound Classical.choice"
PRIM="Nat.add Nat.sub Nat.mul Nat.pow Nat.gcd Nat.div Nat.mod Nat.beq Nat.ble Nat.land Nat.lor Nat.xor Nat.shiftLeft Nat.shiftRight String.ofList Char.ofNat List eagerReduce"
echo "=== nanoda evidence for $MOD start $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "targets: $BUILTIN $* $AXIOMS $PRIM"
/usr/bin/time -l lake env "$LEAN4EXPORT" "$MOD" -- $BUILTIN "$@" $AXIOMS $PRIM > "$OUT/solution.export" 2> "$OUT/lean4export.stderr"
echo "lean4export exit=$? ; export bytes: $(wc -c < "$OUT/solution.export") ; lines: $(wc -l < "$OUT/solution.export")"
head -c 400 "$OUT/solution.export"; echo
echo "declaration lines by kind (first token): "; awk '{print $1}' "$OUT/solution.export" | sort | uniq -c | sort -rn | head -12
cat > "$OUT/nanoda-config.json" <<JSON
{"export_file_path": "$OUT/solution.export", "permitted_axioms": ["propext","Quot.sound","Classical.choice"],
 "unpermitted_axiom_hard_error": true, "nat_extension": true, "string_extension": true, "print_success_message": true}
JSON
cat "$OUT/nanoda-config.json"
/usr/bin/time -l "$NANODA" "$OUT/nanoda-config.json"
echo "nanoda exit=$?"
echo "=== end $(date '+%Y-%m-%d %H:%M:%S %Z')"
