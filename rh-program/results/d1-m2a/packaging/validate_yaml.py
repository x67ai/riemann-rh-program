#!/usr/bin/env python3
"""validate_yaml.py -- a minimal JSON-Schema (draft-07 subset: type, properties, required, items, enum, additionalProperties)
validator for formalization.yaml against schema/v0.4.schema.json, used because neither PyYAML nor jsonschema is installed on
this machine and no package may be fetched in this job (the YAML is parsed by macOS's Ruby/Psych into JSON first).
usage: validate_yaml.py <formalization.json> <v0.4.schema.json>"""
import json, sys
doc = json.load(open(sys.argv[1])); schema = json.load(open(sys.argv[2]))
errs = []
def check(v, s, path):
    t = s.get("type")
    if t:
        ts = t if isinstance(t, list) else [t]
        ok = any((tt == "object" and isinstance(v, dict)) or (tt == "array" and isinstance(v, list)) or (tt == "string" and isinstance(v, str))
                 or (tt == "integer" and isinstance(v, int) and not isinstance(v, bool)) or (tt == "number" and isinstance(v, (int, float)))
                 or (tt == "boolean" and isinstance(v, bool)) or (tt == "null" and v is None) for tt in ts)
        if not ok: errs.append(f"{path}: expected type {t}, got {type(v).__name__}")
    if "enum" in s and v not in s["enum"]: errs.append(f"{path}: {v!r} not in enum {s['enum']}")
    if isinstance(v, dict):
        for r in s.get("required", []):
            if r not in v: errs.append(f"{path}: missing required '{r}'")
        props = s.get("properties", {})
        for k, vv in v.items():
            if k in props: check(vv, props[k], f"{path}.{k}")
            elif s.get("additionalProperties") is False: errs.append(f"{path}: additional property '{k}' not allowed")
    if isinstance(v, list) and isinstance(s.get("items"), dict):
        for i, vv in enumerate(v): check(vv, s["items"], f"{path}[{i}]")
check(doc, schema, "$")
print(f"schema '{schema.get('title')}': required {schema.get('required')}; top-level keys in document: {list(doc.keys())}")
unknown = [k for k in doc if k not in schema.get("properties", {})]
print("keys not in the schema's properties:", unknown or "none")
print("main_results:", len(doc["status"]["main_results"]), "; alignment.statements:", len(doc["alignment"]["statements"]),
      "; sources:", len(doc["sources"]), "; fidelity.divergences:", len(doc["fidelity"]["divergences"]), "chars")
print("validation errors:", len(errs))
for e in errs: print("  ", e)
sys.exit(1 if errs else 0)
