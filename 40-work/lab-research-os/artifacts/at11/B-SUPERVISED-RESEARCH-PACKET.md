# AT11 B — Future supervised evidence card packet

State: PACKET_READY / NOT AUTHORIZED TO EXECUTE. This document and the [machine packet](../../packets/at11-first-supervised-research.json) describe one future task only. [A](A-FIRST-RESEARCH-SCOPE.md) records scope; [D](D-SOURCE-BINDING.md) records the exact approved original.

## Task-level ownership
Executor: existing Research/Evidence role, one separately assigned local worker. Independent reviewer: existing Sol scientific QA role using the project target `gpt-6-sol` at reasoning effort `high`, a distinct assignment/session with access to the same approved original and demonstrated text-evidence review capability. Role naming or requested model/effort is not current availability, authenticated runtime identity or qualification evidence; these must be checked at future authorization/start. Neither is invoked by AT11. A renamed executor alias cannot supply independent review, and GPT 5.6 is not an allowed silent fallback.
Acceptance owner: Human PI, explicitly accepting or declining the bounded draft for internal use.
Canonical state and single checkpoint owner: Astra, recording only that PI disposition.
QC finding owner: not applicable; no code changes. No permanent role is created.

## Deliverables and ownership of write set
All paths relative to the canonical project:
- Executor alone: `artifacts/at11-research-run/EVIDENCE-CARD.md` — four rows / 600 Chinese words maximum, source and precise page/section locator for each row, observation versus interpretation distinguished.
- Reviewer alone: `artifacts/at11-research-run/REVIEW.md` — claim-scoped report specified in C.
- Astra alone: `artifacts/at11-research-run/DISPOSITION.md` — PI outcome, evidence links, limitations, no automatic promotion.

These are proposed future writes; AT11 creates none of them. No future checkpoint write is included in the machine write set; an authorized state owner must obtain an explicit checkpoint write scope when the run is authorized. No source changes, source copying or publication.

## Budget and start conditions
One original paper; maximum seven unique input/output files (three scope documents, one approved original, three outputs), depth 4 relative to each explicitly approved read root, two task model calls total (one executor and one independent reviewer), no retries, no correction/re-review round, no browsing, no download, no visual/numeric extraction. A figure-only support claim is omitted and flagged; if indispensable, stop for a suitably authorized visual review route.

The source read root is the one exact PDF bound in D; the index is no longer a scientific-evidence input. Separate PI execution authorization must approve starting the ready packet, confirm its roles and bind expected_checkpoint to the then-current Foundation state. Neither source-binding approval nor packet readiness starts a run.

## Stop and rollback
Stop immediately on source mismatch/unreadability, unavailable independent capability, private-content transmission requirement, exhausted budget or material unsupported claim. No substitute source/model, expanded search, automatic repair or successor. Preserve incomplete outputs with HELD or REJECTED and exact affected claims; never silently overwrite accepted output. Rollback means retain failed drafts as non-adopted and do not integrate into knowledge/manuscript or use for conclusions. PI may decline the whole candidate. Only local draft preparation can later be accepted; no general scientific validity is implied.
