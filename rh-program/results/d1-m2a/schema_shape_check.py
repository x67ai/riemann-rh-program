"""schema_shape_check.py -- minimal JSON-Schema (2020-12 subset) shape validator for barrier-schema.json,
used because the `jsonschema` package is not installed on this machine.  Supports exactly the keywords
the schema uses: type, required, additionalProperties, properties, $ref (local #/$defs/...), const,
enum, pattern, minItems, items, oneOf, description/title/$schema/$id (ignored).  Untrusted tooling;
U.S. English.

usage: python3 schema_shape_check.py barrier-schema.json file.json [file.json ...]
       (a manifest's prism files are validated too, resolved relative to the manifest)
"""
import json
import os
import re
import sys


class Bad(Exception):
    pass


def resolve(schema, ref):
    assert ref.startswith("#/"), ref
    node = schema
    for part in ref[2:].split("/"):
        node = node[part]
    return node


def validate(schema, node, doc, path="$"):
    if "$ref" in node:
        validate(schema, resolve(schema, node["$ref"]), doc, path)
    if "const" in node and doc != node["const"]:
        raise Bad("%s: expected const %r, got %r" % (path, node["const"], doc))
    if "enum" in node and doc not in node["enum"]:
        raise Bad("%s: %r not in enum %r" % (path, doc, node["enum"]))
    t = node.get("type")
    if t == "object":
        if not isinstance(doc, dict):
            raise Bad("%s: expected object" % path)
        props = node.get("properties", {})
        for r in node.get("required", []):
            if r not in doc:
                raise Bad("%s: missing required key %r" % (path, r))
        if node.get("additionalProperties") is False:
            extra = set(doc) - set(props)
            if extra:
                raise Bad("%s: additional properties %r" % (path, sorted(extra)))
        for k, sub in props.items():
            if k in doc:
                validate(schema, sub, doc[k], path + "." + k)
    elif t == "array":
        if not isinstance(doc, list):
            raise Bad("%s: expected array" % path)
        if len(doc) < node.get("minItems", 0):
            raise Bad("%s: fewer than minItems=%d" % (path, node["minItems"]))
        if "items" in node:
            for i, el in enumerate(doc):
                validate(schema, node["items"], el, "%s[%d]" % (path, i))
    elif t == "string":
        if not isinstance(doc, str):
            raise Bad("%s: expected string (JSON numbers are forbidden for checked data), got %r" % (path, type(doc).__name__))
        if "pattern" in node and not re.match(node["pattern"], doc):
            raise Bad("%s: %r does not match %s" % (path, doc[:40], node["pattern"]))
    if "oneOf" in node:
        ok = 0
        errs = []
        for alt in node["oneOf"]:
            try:
                validate(schema, alt, doc, path)
                ok += 1
            except Bad as e:
                errs.append(str(e))
        if ok != 1:
            raise Bad("%s: oneOf matched %d alternatives; errors: %s" % (path, ok, " | ".join(errs)[:600]))


def main(argv):
    with open(argv[0]) as fh:
        schema = json.load(fh)
    files = list(argv[1:])
    n_ok = 0
    while files:
        f = files.pop(0)
        with open(f) as fh:
            doc = json.load(fh)
        try:
            validate(schema, schema, doc)
        except Bad as e:
            print("SHAPE FAIL %s: %s" % (f, e))
            return 1
        n_ok += 1
        print("shape OK  %s (kind=%s%s)" % (f, doc.get("kind"),
                                             ", %d prisms" % len(doc["prisms"]) if doc.get("kind") == "manifest" else
                                             ", %d rows" % len(doc["segments"]) if doc.get("kind") == "prism" else ""))
        if doc.get("kind") == "manifest":
            base = os.path.dirname(f)
            files = [os.path.join(base, p["file"]) for p in doc["prisms"]] + files
    print("all %d files shape-valid against %s" % (n_ok, argv[0]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
