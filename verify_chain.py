#!/usr/bin/env python3
"""
Verify the hash chain in PAPER-CLOSURE-LOG.jsonl.

No dependencies. Run:  python3 verify_chain.py [path-to-log]

Each entry's hash is:
    sha256( prev_hash + json.dumps(entry_without_entry_hash, sort_keys=True, ensure_ascii=False) )

The first entry's prev_hash is the genesis constant below. A chain that verifies proves the
entries have not been altered *relative to each other* since they were written. It does NOT
prove the entries are true, complete, or contemporaneous -- see README.md.
"""
import io, sys, json, hashlib

GENESIS = "GENESIS-e2f1b7a4-agentic-stemmatics-closure-log"
path = sys.argv[1] if len(sys.argv) > 1 else "PAPER-CLOSURE-LOG.jsonl"

prev, n, ok = GENESIS, 0, True
with io.open(path, encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        obj = json.loads(line)
        chk = dict(obj)
        claimed = chk.pop("entry_hash")
        canon = json.dumps(chk, sort_keys=True, ensure_ascii=False)
        recomputed = hashlib.sha256((obj["prev_hash"] + canon).encode("utf-8")).hexdigest()
        if obj["prev_hash"] != prev:
            print("BROKEN seq=%s: prev_hash does not match previous entry" % obj.get("seq"))
            ok = False
        if recomputed != claimed:
            print("BROKEN seq=%s: entry_hash does not match content" % obj.get("seq"))
            ok = False
        prev, n = claimed, n + 1

print("entries: %d" % n)
print("chain: %s" % ("VALID" if ok else "BROKEN"))
print("tip: %s" % prev)
sys.exit(0 if ok else 1)
