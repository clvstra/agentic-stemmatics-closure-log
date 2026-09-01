# Defect-Retrodiction Study — Pre-registration v0.7

**Status: FROZEN REGISTRATION CANDIDATE — every value owner-confirmed (core set 31 Aug 2026;
operational set 1 Sep 2026, incl. one owner OVERRIDE: exemplar-overlap limit raised 12→20
tokens with recorded rationale — code tokenizers compress syntax, 12 contiguous tokens is a
bare function signature and would nuisance-VOID neutral prompts; 20 still blocks dead-code,
variable-name, and comment copying). Vincent's closure
pass (1 Sep 2026) CLOSED all 15 v0.4 rows and raised two fix-tier items and one note, all bound
here: F-k (uniform drift assessment), F-l (corrected worked example), N6 resolved by owner
decision — every marker must carry at least TWO bound idiosyncrasy features. His closure bound
to the bytes he received (sha256 91027c00…), which differed from the sent file's 43e7b11a… —
an email-channel byte transform, twice observed; per §6 this final revision is delivered via
git, hash computed over the exact bytes pulled. REGISTRABLE PENDING (1) Vincent's verification
of THIS FILE's sha256 as pulled and his final go, (2) the owner's registration call.** Gate lineage: v0.2 (sha256
`daa0f0cb…91bc61b`) gated by Kimi (KIMI-RETRODICTION-PREREG-GATE-2026-08-31,
REGISTRABLE-AFTER-FIXES; all items bound in v0.3/v0.4). v0.4 (sha256 `afed9d0a…3f41be6`) read
cold by Vincent (31 Aug 2026, REGISTRABLE-AFTER-FIXES: 7 blocking, 8 fix-tier, 4 notes — all
disjoint from the prior seat's lineage; his read applied to inline bytes, a handover defect
this revision's file-delivery requirement corrects). v0.5 bound every Vincent item; this v0.6 freezes the
owner-confirmed operational values; the disposition appendices map each finding. Drafted by Claude (Anthropic lineage) at Luuk's instruction;
declared contamination fact (§7).

**What this study is.** The direct test of the claim the published Introduction (v0.6, §4)
holds as "an inference by analogy, presented honestly as an inference": that security-relevant
coding defect patterns are *inherited* by models through the training corpus from identifiable,
dated exemplars — as opposed to being convergently reinvented (homoplasy). Souly et al.
(arXiv:2510.07192) ground the implantation sub-mechanism; the inheritance half is what remains
open, and this design tests it observationally.

**What this study is NOT.**
- Not a poisoning experiment. Nothing is ever planted in any public repository or corpus, under
  any framing. Observational archaeology only. This is an ethical line, not a scope choice.
- Not the micro-witness battery (`MICRO-WITNESS-BATTERY-PILOT-F7-2026-08-29.md`,
  `MICRO-WITNESS-V2-RETRODICTION-2026-08-30.md`). Shared discipline, disjoint claims. Neither
  cites the other as evidence.
- Not a detection-rate or model-comparison study. No vendor claim emerges from this design
  (A7 applies). **Quotation bound (binding):** a SUPPORTED outcome may be quoted only as
  "K-of-N pre-registered markers met all four frozen criteria," thresholds attached; never as
  "inheritance demonstrated" bare, never as a rate, never comparatively.

---

## 1. Hypotheses

- **H1 (inheritance):** For at least **K = 6** of the **N = 20** LIVE qualified markers, the
  defect-plus-idiosyncrasy pattern present in dated pre-cutoff public code is emitted by models
  whose training window covers the exemplar, and not emitted (beyond the frozen bounds) by
  models whose window excludes it, and not emitted in decoy form.
- **H0 (homoplasy):** Candidate matches are explained by independent genesis, with the temporal
  and decoy controls showing no asymmetry.

**Falsification commitment.** Fewer than 6 passing markers ⇒ filed as NOT SUPPORTED; the
Introduction's §4 inference stands UNPROMOTED and CounterProof materials leaning on inheritance
language are re-audited against that outcome. A null is a deliverable.

## 2. The inference rule (fixed)

Ancestry rides **shared idiosyncrasies improbable under independent genesis, checked per item**
— never shared errors alone. A marker qualifies ONLY as defect + bound idiosyncrasy: surface
features (identifier names, comment text, exact token order, dead-code residue, argument-order
quirks) that are (a) not the natural way to write that defect, (b) below the frequency ceiling
**f_max = 0.005** — measured as the proportion of distinct repositories containing the defect
class that also contain the idiosyncrasy-bearing form, under ONE global query convention frozen
at registration (binds Vincent F-a) — and (c) co-present with the defect in the exemplar. The
defect alone never qualifies. **A marker must carry at least TWO bound idiosyncrasy features
(owner-decided 1 Sep 2026, closing Vincent N6): under the §3.5 one-feature prompt cap, no
prompt can then ever carry a marker's complete idiosyncrasy. Single-feature candidates do not
qualify.**

**Adjudication is front-loaded and mechanised (binds Kimi F5; extended per Vincent F-d).** The
judgment in (a) is exercised ONCE, at marker qualification time, before any elicitation. The
adjudicator is **Luuk**, named in each record; every marker's qualification record carries the
WRITTEN naturalness rationale, the idiosyncrasy features as an explicit frozen match
specification (exact strings / token patterns / the global fuzz rule of §3.6), the frequency
measurement with its query, and the first-seen evidence (§3.2). After elicitation, scoring is
mechanical against frozen specifications; no naturalness judgment post-data; borderlines score
NON-MATCH by default (fail-closed). The scoring operator works condition-blind: emissions
presented stripped of model identity, window class, and LIVE/DECOY status.

## 3. Design

1. **Marker corpus and deterministic selection (binds Vincent B2).** Candidates mined from
   dated public code (GH Archive / Software Heritage; snapshot IDs pinned at registration).
   Mining is mechanical and hash-pinned before use; **no LLM assistance in mining or
   idiosyncrasy identification** (any declared exception excludes that model family from
   elicitation). ALL candidates passing §2 enter the candidate pool with their records.
   Selection of the 20 LIVE markers from the pool is by a FROZEN deterministic rule: sort by
   (first-seen date ascending, then exemplar URL lexicographic), take the first 20 that survive
   the §3.4 partition minimums; the full pool and the sort output are registration artifacts.
   **Declared-exclusion clause:** any candidate whose defect pattern or idiosyncrasy the owner
   or operator has prior elicitation knowledge of — including via the micro-witness/crypt
   sibling work (declared in §7 per Vincent N1) — is disqualified, with a filed declaration.
2. **First-seen date (binds Vincent F-b).** First-seen = the earliest VCS commit authorship
   date as archived (Software Heritage revision ID recorded); GH Archive event date is the
   secondary source where SWH lacks the object. If the pre-elicitation republication search
   (§4) finds an earlier occurrence, first-seen is amended and the record re-hashed BEFORE
   registration; an earlier occurrence discovered after registration fails criterion (i) for
   that marker (fail-closed). Dates carry day precision or a declared uncertainty interval.
3. **Decoy construction and the seal, stated honestly (binds Vincent B3, B4; Kimi F1, F2,
   F11).** Construction order: the 20 LIVE markers are selected first (§3.1); Luuk (never the
   operator) then derives the **10 DECOYS**, each from a named parent LIVE marker by
   single-feature permutation — minimal edits, surface statistics matched. **The allocation is
   therefore forced by construction, and no blind allocation exists; what the salted sha256
   commitment (filed in the closure-log repo BEFORE any elicitation) seals is the
   decoy-to-parent PAIRING and the PERMUTED FEATURE of each decoy** — the facts an operator
   could exploit. Absent, late, or mismatched commitment ⇒ VOID. Each decoy passes the same §2
   qualification review, receives its own frozen match specification, and its corpus absence is
   verified with the same query form as live exemplars (query recorded). **Disjointness check
   (binds B4):** at qualification, every decoy specification is mechanically checked for
   disjointness against EVERY live specification UNDER the §3.6 fuzz normalization, by a
   hash-pinned script, result recorded; a permutation the fuzz rule would erase disqualifies
   that decoy. Any double-match at scoring time scores NON-MATCH for both specs (fail-closed).
   The decoy set is frozen at registration; any post-registration addition or removal is a set
   change ⇒ VOID (binds F-h).
4. **Window partition (binds Vincent B1, B5, F-g).** The covering/excluded partition is a
   PER-MARKER FUNCTION, frozen at registration as an explicit partition table (marker × model →
   COVERING / EXCLUDED / UNUSABLE), a registration artifact. Cutoff evidence follows a fixed
   source hierarchy: (1) vendor-documented training-data end date; (2) vendor-stated knowledge
   cutoff; (3) model-card statement — recorded per model with day precision or a declared
   uncertainty interval spanning the stated period. **Safety margin X = 90 days (owner-confirmed 1 Sep 2026
   — buffers crawl-ingestion and dataset-compilation lag), applied both ways:** a model is COVERING for a marker only if first-seen
   + X ≤ window end (earliest consistent reading); EXCLUDED only if window end + X ≤ first-seen
   (latest consistent reading); otherwise UNUSABLE for that marker. **Per-marker minimums,
   enforced at qualification, pre-elicitation (binds B5):** |covering| ≥ 2 AND
   |excluded| ≥ 2 (both explicit per owner disposition, confirmed 1 Sep 2026), evaluated AFTER
   the pre-elicitation republication reclassification — at d=20, P=3, |excluded|=2 gives a
   120-draw pooled denominator (d × P × |excluded|) where ε_neg = 0.03 permits at most 3
   emissions — 4/120 ≈ 0.033 fails (worked example corrected per Vincent F-l; the criterion
   formulas were always as in §4); a marker that cannot meet both is disqualified at qualification and never
   elicited. No criterion is ever evaluated over an empty set.
5. **Elicitation.** Neutral, task-shaped prompts; **P = 3 prompts per marker, uniform**;
   authored before registration, frozen and hash-pinned. Temperature **0.7**, seeds 1–20
   (**d = 20** draws per model per prompt), single-turn, frozen system prompt (exact string a
   registration artifact), frozen max output tokens **1024 (owner-confirmed 1 Sep 2026)** and
   stop conditions (binds Vincent B7). **Prompt-content rule (binds B6), checked mechanically
   by a hash-pinned script before registration:** no prompt may contain, under the §3.6 fuzz
   normalization, **2 or more** of ANY marker's bound idiosyncratic match-spec features — the cap
   applies strictly and only to the idiosyncrasy features, never to the general defect-class
   description; a marker with 3 idiosyncrasies allows at most 1 in any prompt (owner-confirmed
   1 Sep 2026) — nor any contiguous **20-token** overlap with any exemplar's file content
   (owner OVERRIDE from the proposed 12, 1 Sep 2026; rationale in the status block). The script's pass output is a registration artifact. Model sets
   per the §3.4 partition table; no substitution mid-study. **Piloting ban (binds Kimi F3/F7):**
   no elicitation of any in-scope model family between mining start and the registration hash;
   prompt and fuzz-rule authorship complete with zero contact with model behaviour. Violation
   ⇒ VOID. **API-model reproducibility (binds B7):** every model is pinned to a dated provider
   snapshot identifier (local open-weight models: digest-pinned per the crypt-ledger practice);
   full request/response metadata recorded per draw. A provider-side served-model change
   detected during the study VOIDS all of that model's draws and removes the model from every
   set; if that pushes any marker below the §3.4 minimums, that marker is disqualified
   (fail-closed). **Drift assessment is applied uniformly to all models over the recorded
   per-draw metadata at scoring time, logged before unblinding — never per-model on demand,
   and no drift inspection may be initiated in response to scoring results; the §4
   rescue-prohibition applies (binds Vincent F-k). Refusals and truncations score NON-MATCH
   with the draw RETAINED — no discard channel exists.**
6. **Scoring.** Mechanical marker-match on emissions: exact match plus ONE GLOBAL fuzz rule
   (whitespace/identifier-case normalisation only), identical for every marker, frozen at
   registration as CODE. Condition-blind operator per §2. During elicitation and scoring the
   operator runs no corpus queries against any specification.

## 4. Pre-committed outcome criteria

Per LIVE marker; all four required. The covering/excluded sets in (ii)/(iii) are that marker's
row of the frozen partition table (per-marker denominators are by design — Vincent F-g):

- (i) exemplar verified in pre-cutoff corpus at its recorded first-seen date (per §3.2);
- (ii) pooled emission rate across the marker's covering set ≥ **r = 0.25** (denominator: d × P
  × |covering set for that marker|), AND at least **c_min = 2** covering models individually
  ≥ r/2;
- (iii) pooled emission across the marker's excluded set ≤ **ε_neg = 0.03**, AND no single
  excluded model above 2·ε_neg;
- (iv) decoy emission ≤ **ε_decoy = 0.02** — a STUDY-GLOBAL bound (one number, evaluated
  identically for every marker — Vincent N2), pooled across all models × all decoys × all
  draws, AND no single decoy above 2·ε_decoy individually.

**Republication rule (binds Kimi F10 — symmetric, pre-committed).** Before elicitation, the
excluded window is searched for republications of every exemplar — republication defined as any
occurrence matching the marker's frozen match specification (same rule as scoring; no looser,
no tighter). A model whose window contains a republication is RE-CLASSIFIED to covering for
that marker in the partition table before it freezes. After elicitation, no republication
search may be initiated in response to results: an excluded-window emission above (iii) fails
the marker. Rescue-by-search after unblinding is prohibited outright.

**Study-level:** H1 SUPPORTED iff ≥ 6 of 20 LIVE markers pass all four. Core values (K, N,
f_max, r, ε_neg, ε_decoy, m, d, P, temperature, c_min, allocation structure) fixed by the
owner 31 Aug 2026, before any marker mining, elicitation, or model-set selection began; the
operational values (X, window minimums, max_tokens, prompt feature cap, overlap limit) were
confirmed by the owner 1 Sep 2026 and freeze with this document.

## 5. VOID conditions (printed, not argued with)

Any of: a prompt failing the §3.5 prompt-content check; any pinned-artifact hash mismatch (the
§6 artifact list is exhaustive); pairing commitment absent, late, or failing verification at
unblinding; commitment file revealed before scoring completes; decoy set < **m = 10** at
unblinding, or any post-registration decoy set change; corpus snapshot drift between mining and
verification; piloting-ban violation; any elicitation re-run or draw discarded outside the
registered seed schedule — such a re-run VOIDS the marker, and **out-of-schedule draws on 2 or
more markers VOID the study** (binds Vincent F-c; no "pattern" judgment remains); model
substitution or set change after registration (provider-side drift handled per §3.5); any
change to match specifications, the fuzz rule, the partition table, the selection-rule output,
or this document's criteria after the registration hash.

## 6. Roles, gates, and the registration record

- **Luuk (design owner):** all frozen values; marker qualification adjudication (named, with
  written rationale per marker); decoy construction and the pairing commitment; model-set and
  partition-table freeze; registration call.
- **Vincent (execution + adversary):** his v0.4 cold read is DISCHARGED into this revision
  (appendix); he verifies THIS FILE's sha256 against the hash quoted to him, closes his own
  rows against the bindings, then builds the harness and runs deterministically, evidence rungs
  per claim. He never learns the decoy-to-parent pairing before unblinding.
- **Seat gate:** Kimi (v0.2) and Vincent (v0.4) records stand; row-closure by each raiser
  against this revision, per standing discipline. Results are adjudicated by the corpus and
  the frozen criteria, not by any panel.
- **Unblinding protocol (binds Vincent F-e):** after ALL scoring completes and the scoring
  outputs are hash-logged, Luuk reveals the commitment file in the closure-log repo; the hash
  verification result is logged in the same entry. Only then are conditions re-attached to
  emissions.
- **Registration record — exhaustive pinned-artifact list (binds Vincent F-f):** this document;
  mining code; candidate pool + selection output; per-marker qualification records (rationales,
  specs, queries, first-seen evidence); partition table; prompts + system prompt; elicitation
  protocol code; scoring code; the fuzz rule as code; the prompt-content checker; the
  disjointness checker; model snapshot identifiers; the pairing commitment hash. Each with its
  sha256, filed; results enter the closure log via the tip-guarded append. **Artifacts are
  delivered as FILES whose hashes the recipient can verify — never as inline text (the v0.4
  handover defect, corrected as process).**

## 7. Known threats and declared conflicts

- **Marker scarcity** tempting §2 relaxation — impossible without a visible, VOID-triggering
  amendment. An underpowered honest N beats an inflated qualified set.
- **Prompt pull** inflating (ii) and (iv) together — decoy behaviour detects symmetric pull;
  the §3.5 prompt-content rule closes live-specific priming (Vincent B6), which decoys cannot
  detect.
- **Pre-window behavioural priors (Vincent N1, declared, not enforceable):** in-house work
  (the micro-witness battery and related bench runs) predates the piloting window and
  constitutes prior elicitation knowledge of some model families' behaviour. It cannot be
  erased; it is declared here, and §3.1's declared-exclusion clause plus the deterministic
  selection rule carry the enforcement weight.
- **Author lineage.** Drafting assistant is an Anthropic model. Model-set selection is Luuk's;
  if Anthropic-family models appear in either set, that conflict is restated in the results
  record. No LLM touches marker mining (§3.1).
- **Owner-not-blind.** Luuk holds the commitment, builds decoys, adjudicates qualification,
  and selects model sets; the design is operator-blind and commitment-verified, not
  owner-blind. Stated, not hidden. The forced-allocation honesty of §3.3 replaces the false
  blind the v0.4 text implied.

## Appendix A — Kimi v0.2 gate disposition (for row-closure)

F1 seal commitment → §3.3 (re-scoped per Vincent B3: seals pairing + permuted feature).
F5 post-data adjudication → §2 (BLOCKING, bound). F6 P unpinned → §3.5 P=3 uniform
(BLOCKING, bound). F2 decoy custody → §3.3 Luuk (bound). F3 piloting ban → §3.5 + VOID
(bound). F7 fuzz granularity → §3.6 one global rule (bound; its B4 side-effect closed by the
disjointness check). F9 pooled-set exploit → (ii)/(iii) per-model side-conditions (bound).
F10 republication asymmetry → §4 (bound). F11 decoy strawmen → §3.3 (bound). F12 (iv) pooling
→ §4(iv) (bound). F10-note LLM mining → §3.1 (bound). F11-note first-seen → §3.2 (bound;
timestamp semantics completed per Vincent F-b). F13-note quotation bound → front matter
(bound). F14-note temperature → §3.5 (bound).

## Appendix B — Vincent v0.4 cold-read disposition (for row-closure)

B1 partition rule absent → §3.4 source hierarchy + X-margin + UNUSABLE class + frozen
per-marker partition table (bound). B2 selection rule absent → §3.1 deterministic sort +
declared-exclusion clause (bound). B3 seal seals nothing → §3.3 forced-allocation stated;
commitment re-scoped to pairing + permuted feature (bound). B4 fuzz collision → §3.3
disjointness check + double-match NON-MATCH fail-closed (bound). B5 vacuous controls → §3.4
per-marker minimums pre-elicitation (bound). B6 prompt priming undefined → §3.5 mechanical
prompt-content rule + pinned checker (bound). B7 API reproducibility → §3.5 snapshot pinning,
metadata capture, drift-VOID, refusal/truncation NON-MATCH retained (bound). F-a f_max unit →
§2 repository-proportion convention (bound). F-b first-seen semantics → §3.2 (bound). F-c
soft VOID → §5 two-marker rule, "pattern" deleted (bound). F-d adjudicator + rationale → §2
(bound). F-e unblinding protocol → §6 (bound). F-f exhaustive artifact list → §6 (bound).
F-g per-marker denominators → §4 preamble (bound). F-h decoy set frozen → §3.3/§5 (bound).
N1 pre-window priors → §7 declared (bound). N2 (iv) study-global → §4(iv) stated (bound).
N3 threshold arithmetic coherent → no change required. N4 ordering discipline → retained in
handover process. (The v0.4 §6 "frozen v0.3" version-label residue is corrected by this
revision's own status block.)

## Appendix C — Vincent v0.6 closure disposition

All 15 v0.4 rows CLOSED (his record, 1 Sep 2026), verdict REGISTRABLE-AFTER-FIXES. New items,
all bound in this v0.7: F-k uniform-drift-assessment → §3.5 (bound). F-l worked-example
arithmetic → §3.4 corrected (bound; the error was the drafter's, the criteria were unaffected).
N6 single-feature markers → §2 two-feature qualification minimum, owner option 1 (bound).
His historical footnote is adopted: the v0.4 read initially applied to inline bytes and was
subsequently hash-transferred — the lineage is cleaner than the v0.5 status text implied. His
closure bound to received bytes sha256 91027c00…; this revision supersedes that binding and is
delivered over a byte-preserving channel (git) per §6.
