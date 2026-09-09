#!/usr/bin/env python3
"""Validate lean/formalization.yaml with PyYAML + jsonschema against the upstream dispatcher schema
(formalization.schema.json -> v0.4.schema.json), both resolved from local copies in results/d1-m2a/packaging/.
usage: validate_yaml_jsonschema.py <formalization.yaml> <packaging-dir>"""
import sys, json, yaml, jsonschema, hashlib
from referencing import Registry, Resource
doc = yaml.safe_load(open(sys.argv[1]))
pk = sys.argv[2]
disp = json.load(open(f"{pk}/formalization.schema.dispatcher.json")); v04 = json.load(open(f"{pk}/v0.4.schema.json"))
base = "https://raw.githubusercontent.com/mathlib-initiative/formalization.yaml/main/schema/"
reg = Registry().with_resources([(base + "formalization.schema.json", Resource.from_contents(disp)),
                                 (base + "v0.4.schema.json", Resource.from_contents(v04))])
V = jsonschema.Draft7Validator(disp, registry=reg)
errs = sorted(V.iter_errors(doc), key=lambda e: list(e.path))
for f in ("formalization.schema.dispatcher.json", "v0.4.schema.json"):
    print(f, "sha256", hashlib.sha256(open(f"{pk}/{f}", "rb").read()).hexdigest())
print("document version:", doc.get("version"), "; review.status:", doc["review"]["status"], "; review.notes chars:", len(doc["review"]["notes"]))
print("jsonschema", jsonschema.__version__, "errors:", len(errs))
for e in errs: print("  ", list(e.path), e.message[:200])
sys.exit(1 if errs else 0)
