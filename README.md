# Agentic Stemmatics — review closure log

This repository is the external copy of the append-only review log kept for the paper *Agentic
Stemmatics: Collation, Provenance, and Conservation for an Emerging Machine Textual Tradition*
(CounterProof Research). The paper is at <https://research.counterproof.io/>.

It exists because the paper commits to one, and because a log held only by its author is not
evidence to anybody else.

## What is in here

| File | What it is |
|---|---|
| `PAPER-CLOSURE-LOG.jsonl` | The log. One JSON object per line, hash-chained. |
| `verify_chain.py` | Standalone verifier. No dependencies. `python3 verify_chain.py` |
| `ANCHORS.md` | Which log hashes have been committed to the Bitcoin blockchain, and how to check them. |

Each entry records a review round: which revision of the paper, which reviewing model lineage,
whether the round was sent or returned, the verdict where there was one, and the SHA-256 of the
artifact filed for that round.

## What this establishes

- **Internal consistency.** `verify_chain.py` recomputes every hash. If it passes, no entry has
  been altered relative to the others since it was written.
- **Existence at a time, for anchored entries only.** An entry whose hash is in `ANCHORS.md`
  provably existed no later than the Bitcoin block containing it.
- **Public availability.** Anyone can clone this and check the above without asking us for
  anything.

## What this does not establish

This section is longer than the one above on purpose.

- **It does not prove the entries are true.** The log records that a round happened and hashes the
  artifact filed for it. It cannot prove the artifact is what the round actually produced, or that
  a round was not run and quietly omitted.
- **It does not prove completeness.** Rounds are only in here if they were written down. The log
  began at revision v1.1; every round before that — including the paper's original four-seat
  review — is not covered and never will be.
- **Some entries were written retroactively.** Entries `seq` 2 through 4 were appended on 20 August
  2026, reconstructed from filed artifacts, days after the rounds they describe. They are marked
  as such in the log itself. A retroactively written entry is weaker evidence than a contemporaneous
  one: the artifact hash is real, the timing of the record is not.
- **The log was not kept current.** It sat at one entry for eleven revisions of the paper before
  being brought up to date. That is a failure of practice, recorded here rather than smoothed over.
- **Most entries are not anchored.** See `ANCHORS.md`. Without an anchor the chain proves ordering
  and integrity but carries no timestamp of its own.
- **The custodians are not independent of the practice.** This repository is held by the paper's
  author's own GitHub account, and a second copy is held by the other principal of the same
  practice. That is better than a single private copy, and it is not an independent third party.
  A reader weighing this should weigh it as what it is.

## Verifying

```
git clone https://github.com/clvstra/agentic-stemmatics-closure-log
cd agentic-stemmatics-closure-log
python3 verify_chain.py
```

Then pick any row in `ANCHORS.md`, open the transaction on a block explorer, decode the
`OP_RETURN` output, and confirm the hash matches the entry it claims to.

## Why the history matters

This repository has force-pushing disabled, so its commit history cannot be rewritten. If you are
checking whether the log has been edited after the fact, the git history is the record to read —
not just the current file.
