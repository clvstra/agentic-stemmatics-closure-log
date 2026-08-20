# Bitcoin anchors

Each line records a hash from this log committed to the Bitcoin blockchain in an `OP_RETURN`
output. Anchoring proves the hash existed no later than the block that contains it.

| log entry | hash anchored | payload | txid | block | time (UTC) |
|---|---|---|---|---|---|
| `seq` 1 | `328ceb0c29fad9a17a9df9b1bf816ee8a52af4e069d7405e2a55ba4c80304d46` | `CPRLOG1:328ceb0c…04d46` | [`542748138c9889e745c99fbccd268ec16cafc3e53ebb6fe30b1ee44cdd0145e0`](https://mempool.space/tx/542748138c9889e745c99fbccd268ec16cafc3e53ebb6fe30b1ee44cdd0145e0) | 963282 | 2026-08-20 09:23:01 |

## How to check one

1. Open the txid on any block explorer, or query a node directly.
2. Find the `OP_RETURN` output and decode its data as ASCII.
3. It reads `CPRLOG1:` followed by a SHA-256 hash.
4. Compare that hash against the corresponding entry's `entry_hash` in `PAPER-CLOSURE-LOG.jsonl`.

If they match, that entry existed in this exact form no later than the block's timestamp.

## What is not anchored

Only the entries listed above. At the time of writing that is `seq` 1 alone — entries 2 through 4
are **not** anchored, and neither is the chain tip. An unanchored entry can still be verified
against the chain (`verify_chain.py`), but the chain alone carries no timestamp: it proves internal
consistency, not when anything was written.
