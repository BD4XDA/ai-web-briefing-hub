# Decision 0001 · Additive canonical memory
Status: approved implementation within the user's Phase 0 authorization, 2026-09-21.
Owner: Astra. Human PI's requested scope is authoritative.

Keep the existing hub and harness assets. Add a scoped canonical project at 40-work/lab-research-os. Parent AGENTS.md and existing shared directories remain. No legacy memory is deleted or migrated.

Canonical meanings:
- AGENTS.md: stable operating procedure; changed only after a verified recurrent need.
- PROJECT.md: identity, scope, owners and objectives.
- CHECKPOINT.md: current summary derived from append-only checkpoint JSON snapshots.
- decisions/: durable rationale, superseding links and explicit authorization where needed.
- knowledge/: reusable validated facts, each with scope, evidence, verifier and review date.
- evidence/: located observations, content hashes, commands/results and timestamps.
- incidents/: episodes, failures and hypotheses including refuted ones.
- artifacts/: outputs with draft/reviewed/integrated status.
- IDEA-INBOX.md: capture before evaluation; no execution authorization.
- packets/ and queues/: bounded delegation inputs and pending work.

Precedence is dimension-specific. User authorization controls intent, project rules control procedure, direct observations control factual state. No single file can authorize destruction or turn an unverified report into fact. Conflicts become evidence-backed exception packages, not silent merges.

Update procedure: evidence → verification → owner decision → scoped promotion; preserve prior revisions. Only one writer can advance a checkpoint from its named parent. Harness session memory may be used as an index, never as an independent source of canonical truth.

Rollback: remove neither legacy state nor original files. To stop using this layer, remove only the new pointer appended to the hub handoff after preserving it; archive the additive directory on explicit user approval. No git push is authorized.
