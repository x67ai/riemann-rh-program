"""recon_compare_transcripts.py -- RECONCILIATION (2026-09-02): compare two W1 transcripts on
their NUMERIC CONTENT (everything except the untrusted `producer` and `comment` metadata).
Used to show that repairs R1 (outward ulp inflation) and R2 (A even) leave the acceptance
transcripts byte-identical in every checked field.
Usage: python3 recon_compare_transcripts.py A.json B.json [...pairs]"""
import json, sys

def content(path):
    with open(path) as fh:
        d = json.load(fh)
    d.pop("producer", None)
    d.pop("comment", None)
    return d

def main(argv):
    bad = 0
    for a, b in zip(argv[0::2], argv[1::2]):
        same = content(a) == content(b)
        print("%-9s %s  vs  %s" % ("IDENTICAL" if same else "DIFFERENT", a, b))
        bad += not same
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
