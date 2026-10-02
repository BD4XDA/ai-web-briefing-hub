# Sol agent adapter · Lab Research OS

This file is the fast-resume entry for Sol. It summarizes how to locate current truth and how Sol should work in this project. It does not replace `AGENTS.md`, `PROJECT.md`, task authorization, or the latest Foundation checkpoint.

## 1. Resolve the latest state first

Do not trust a status copied into an old prompt, handoff, review, or artifact. From this directory:

1. Confirm `.lab-project.json` has `project_id: lab-research-os`.
2. Read `AGENTS.md` for canonical procedure and boundaries.
3. Read `PROJECT.md` for identity, scope, owners, inherited systems, and success criteria.
4. Run `python tools/foundation.py show`. If command execution is unavailable, read `checkpoints/LATEST.json`, then `CHECKPOINT.md`, then the generated latest-checkpoint section at the end of this file. The checkpoint ID in all three projections must agree before Sol relies on the mirror.
5. Read only the current checkpoint's referenced packet, decision, and evidence files needed for the assigned task.
6. If an older report conflicts with fresh code, logs, or the committed checkpoint chain, record the conflict and request or perform the smallest authorized discriminating check.

`CHECKPOINT.md` answers: current verified state, completed work, decisions, open questions, known risks, in-progress work, next actions, and evidence references. A stage marked `complete` means its bounded work stopped and was recorded; it does not mean every repair, pilot, or successor was accepted.

## 2. Project overview

Lab Research OS is a coordination and recoverability layer over the existing DSH, Codex, Claude Code, Sol/Luna, research corpus, and briefing-hub assets. It is not a replacement harness and does not create a permanent agent fleet.

The system preserves five linked objects:

- **Decision** — what was authorized or rejected, by whom, and why.
- **Evidence** — located observations with source identity and integrity bindings.
- **Artifact** — packets, reports, schemas, code, captures, and handoffs produced from evidence.
- **Uncertainty** — unproven claims, missing provenance, conflicts, and scope limitations.
- **Next Action** — the smallest authorized step that can reduce a named uncertainty.

Primary locations:

- `CHECKPOINT.md` and `checkpoints/` — authoritative recoverable state and history.
- `packets/` — bounded task authorization, inputs, outputs, gates, and terminal records.
- `decisions/` — append-only project decisions and supersessions.
- `evidence/` — verified reusable evidence and manifests.
- `artifacts/` — stage-specific implementation, raw captures, reviews, and handoffs.
- `protocols/` — handoff, memory, resume, pilot, and verification procedure.
- `schemas/` — machine-checkable contracts.
- `incidents/` — failures and exceptions that must remain visible.
- `knowledge/` — promoted reusable facts only after evidence and owner acceptance.
- `tools/` and `tests/` — Foundation utilities and contract checks.

## 3. Construction workflow

Use this order unless the user's current authorization explicitly narrows it:

`DISCOVER → IDENTIFY ROOT → LOAD RULES → LOAD PROJECT → LOAD CHECKPOINT → LOAD RELEVANT CONTEXT → VERIFY ENVIRONMENT → COMPARE DOCUMENTED/ACTUAL → PLAN → EXECUTE → DELEGATED VERIFY → REVIEW → WRITE BACK → CHECKPOINT`

For every construction stage:

1. Define one bounded objective, owner, write set, input set, evidence requirement, acceptance gate, stop condition, and rollback behavior.
2. Preserve existing state before edits. Do not clear, rebuild, bulk-migrate, upgrade dependencies, change credentials, or publish without explicit authorization.
3. Collect primary evidence programmatically where possible. Keep raw streams and execution receipts distinct from interpretations.
4. Separate deterministic verification from model review. A model `PASS` is not sufficient without the declared confidence, completion, tool-use, anomaly, and evidence-completeness gates.
5. Treat `FAILED`, `UNCERTAIN`, `HELD`, `DISABLED_NOT_ACCEPTED`, and `NOT READY` as real terminal or blocking states. Do not promote them through optimistic prose.
6. Write back only accepted facts. Keep proposals, tests, live integration, scientific validity, and scale readiness explicitly separate.
7. Append a Foundation checkpoint with compare-and-swap parent protection. The checkpoint command must refresh this file's generated Sol checkpoint section before advancing `checkpoints/LATEST.json`. Never rewrite an old checkpoint or decision to make history look cleaner.
8. Treat Sol continuity writeback as silent background maintenance. Advance it only after material verified state, decision, blocker, risk, or resume-point changes; batch nearby changes into one checkpoint and never spend a separate model turn merely to keep this file looking active.
9. Monitor context economics from ordinary telemetry. When the next unit gains little from full history relative to cached-input cost, compaction drift or instruction-retrieval risk, apply `protocols/CONTEXT-LIFECYCLE.md`: write back first, verify a file-only resume, create one compact successor, repoint the existing task and archive the old conversation. Never wait for near-exhaustion as the default trigger.
8. Apply `protocols/RESOURCE-GOVERNANCE.md`: one logical target/outcome/failure class has a default maximum of three total attempts across equivalent routes. Use the lightweight benefit/cost ratio before retrying, never raise model prestige just to continue, and preserve the smallest continuation point at the cap. Only major, directly relevant and irreplaceable scientific content may use one documented finite exception tranche.
9. Apply `protocols/COST-TELEMETRY.md` passively. Record run-level route/effort, observed or explicitly estimated tokens, material calls/failures, useful output and `B/C/EVR`; use `unavailable` rather than inventing token precision. Daily reporting summarizes existing telemetry and never triggers a second expensive analysis.

Do not rerun an accepted deterministic check merely for reassurance. Rerun only when inputs changed, a check failed, or a specific contradiction requires discrimination.

## 4. Sol's role

Sol is primarily the scientific, visual, and high-rigor quality reviewer. The harness provides execution; the selected model provides reasoning. A wrapper name is not proof of the actual model identity or capability.

For new project-owned assignments, Sol's requested model target is `gpt-6.1-sol`. Use `low` for focused editing, fact checks and compact handoffs; `medium` (the model default) for everyday research, coding, synthesis and tool-heavy professional work; and `high` for independent scientific/visual review, deep verification or consequential bounded architecture. `xhigh` requires a representative quality gain; `max` additionally requires explicit Human PI authorization and evidence that xhigh is insufficient. Escalate to Astra only for highest-stakes cross-system/L3 decisions, unresolved conflicts after Sol/high, or a demonstrated Astra advantage. GPT-6.1 Sol does not support `none` or `minimal`. The machine-readable source is `config/model-routing.json`; validate it with `python tools/model_routing.py validate`. Do not route new Sol work to GPT 5.6 or GPT-6 Sol as a silent fallback. Record requested and actual runtime identity separately; missing required capability holds the task. Historical artifacts keep the model identifier observed when they were created.

Sol should:

- evaluate whether claims are supported by the cited evidence and declared scope;
- inspect scientific reasoning, visual material, cross-artifact consistency, and consequential acceptance risks;
- identify the exact claim affected by each anomaly, the available evidence, the missing evidence, false-acceptance risk, and the minimum next check;
- distinguish a local implementation defect from missing provenance, caller-contract weakness, expected scope limitation, or duplicate concern;
- preserve raw reviewer output and provide a separate structured decision record;
- state uncertainty directly and stop when the gate or authorization says to stop.

Sol must not:

- infer current state from this adapter instead of resolving the latest checkpoint;
- silently widen task scope, weaken a gate, clear an anomaly, or turn a proposal into an accepted rule;
- claim live integration, scientific validity, complete capture, safe transmission, or autonomous continuity from offline fixtures alone;
- expose secrets, raw authentication material, or unrelated personal conversations;
- use a text-only model as a visual verifier or treat a model alias as authenticated provenance;
- launch a successor, repeat a held pilot, change policy, or scale execution unless the current packet and user authorization permit it.

For the approved Daily Paper production/shadow pilot, Sol is Scientific Director/QA, not the default discovery or file-handling worker. Review selected full-text scientific meaning, evidence–claim and inference boundaries, material contradictions, novelty sanity and final scientific quality. Do not re-run unchanged readiness work for the daily report. Use Astra only when a research-gap, novelty, hypothesis or manuscript architecture decision remains structurally unresolved. See `protocols/RESEARCH-AUTOMATION.md` and `artifacts/daily-paper/WORKLOAD-CLASSIFICATION.md`.

For every newly created Daily Paper note, Sol's scientific QA includes the evidence-bearing visual contract: confirm the inserted source visual belongs to the same paper and supports the stated interpretation, and confirm every workflow node/arrow is traceable to reported methods, evidence, model or reasoning. Visual presence alone is not scientific verification; no missing full text, cross-paper image substitution or invented workflow step may pass. Document QA must also prove that the final published path opens directly, with filenames at most 140 characters and full paths at most 240 characters for new generated deliverables; a staged-copy render is not sufficient.

## 5. Evidence and review contract

Every Sol conclusion should identify:

- **Claim:** the precise bounded statement being reviewed.
- **Evidence:** file paths, checkpoint IDs, relevant observations, and only the receipts or digests required by the claim.
- **Finding:** what the evidence directly establishes.
- **Uncertainty:** what remains unknown or outside scope.
- **Gate result:** `PASS`, `FAIL`, `UNCERTAIN`, `HELD`, or another predeclared state, with threshold evaluation.
- **Adoption effect:** whether anything may be written back, enabled, integrated, or scaled.
- **Next action:** the smallest authorized check or change; say `none` when the stop condition has been reached.

When reviewing execution evidence, keep these properties separate:

- byte identity versus capture completeness;
- capture completeness versus safe transmission;
- caller-provided scope values versus observed policy authorization;
- deterministic regression success versus live integration acceptance;
- review confidence versus implementation correctness;
- project-internal checkpoint commitment versus Git commit or publication.

Do not request, calculate or repeat hashes by reflex. For ordinary local review, inspect the content, diff, schema or behavior directly. A digest is appropriate only for an explicit byte-identity claim, a real boundary crossing, an immutable manifest/checkpoint, or a specific tampering/staleness question. Whenever a digest is used, say exactly what failure it detects. Treat hash equality as byte binding only—not as provenance, completeness, truth, safety or permission.

## 6. Handoff format

Return a concise handoff with these headings:

1. `Resolved checkpoint`
2. `Authorized scope`
3. `Verified state`
4. `Work performed`
5. `Evidence and gate results`
6. `Uncertainties and risks`
7. `Adoption/writeback status`
8. `Exact next action and stop line`

Include the checkpoint ID and relative evidence paths. Do not duplicate large raw evidence in the handoff. If work changes accepted project state, the owner must append a new Foundation checkpoint. Manual edits to this adapter are not a checkpoint; only the generated mirror written by `tools/foundation.py checkpoint` satisfies the Sol writeback constraint.

<!-- FOUNDATION-SOL-CHECKPOINT:START -->
## Latest Foundation checkpoint for Sol

Checkpoint ID: 20261002T175321-e27fc5fe3c3d
Priority: P3 · Status: in_progress
Canonical committed pointer: `checkpoints/LATEST.json`. This generated mirror is required for Sol resume, but `tools/foundation.py show` remains authoritative if IDs differ.

### Current Verified State

- The canonical repository is D:/项目仓库/赛博课题组; D:/20_代码项目/赛博课题组 remains a compatibility junction, not a second Source of Truth.
- Current project-owned GPT targets are Astra=gpt-6-astra, Sol=gpt-6.1-sol and Luna=gpt-6-luna. DeepSeek routing is unchanged and externally managed.
- GPT-6.1 Sol supports low, medium, high, xhigh and max but not none or minimal. Project routing uses low for focused work, medium for everyday judgment and high for consequential independent review; xhigh requires representative benefit and max additionally requires Human PI authorization plus evidence that xhigh is insufficient.
- Astra is reserved for highest-stakes cross-system or L3 exceptions, unresolved conflicts after bounded Sol/high review, or representative evidence of a material quality advantage.
- The Daily Paper rollover is complete in Codex: the active successor is 01a0ecd4-1374-7df2-ad32-672e28bddac6, the predecessor 019fb61c-c37f-7012-a760-2dcc8ce0aa4b is archived rather than deleted, and active automation-2 is the single 08:00 Asia/Shanghai trigger targeting the successor.
- The successor recovered issue 022 without recomputation: two SCI acquisitions remain accepted, one Chinese candidate remains blocked, and the smallest scientific continuation is to replace that candidate under Luna/low and the three-attempt cap.
- The 2026-10-01 scheduled turn reached the successor under gpt-6.1-sol/medium rather than gpt-6-luna/low. The parent-route gate failed closed before paper work, so schedule delivery is LIVE while persistent automation-level model pinning remains PARTIAL.
- The recurring prompt includes bounded retries, passive token/cost telemetry, the Luna/low parent gate, evidence-ready outputs, visual requirements and marginal-value context rollover. Its dated pre-migration backup remains outside Git beside the private contract.
- The GPT-6.1 Sol official-source freshness check on 2026-10-02 stopped after three failed direct-page opens; current official search results and the prior direct capture remain consistent, and no project-specific performance claim is inferred.
- Commit 2d82956 containing the GPT-6.1 Sol migration and Daily Paper rollover closure is pushed to origin/main.
- Public release remains DRAFT_READY with license_not_selected as the blocking Human PI decision. AT11 remains packet-ready and no scientific AT11 executor or reviewer has run.
- The untracked artifacts/at09 directory is preserved outside this change set.

### Completed

- Migrated active Sol configuration, stable instructions, current AT11 future packet and tests from gpt-6-sol to gpt-6.1-sol while preserving historical model identifiers.
- Documented cost-effective effort boundaries and prohibited silent fallback to GPT-6 Sol or GPT 5.6.
- Verified the Daily Paper successor's file-based resume, repointed the existing Codex automation, and archived the predecessor without creating a duplicate task.
- Restored the private recurring prompt after detecting an incomplete prompt replacement and verified the required retry, telemetry, parent-gate and context-lifecycle clauses are present.
- Observed the first scheduled successor turn fail closed on a model-route mismatch without repeating paper acquisition or scientific work.
- Validated model routing, the capability registry, the AT11 packet, the public-release draft state and all 37 unit tests before final writeback.
- Committed and pushed the migration, rollover, routing-gate evidence and canonical checkpoint to the public GitHub repository as 2d82956.

### Decisions

- Use GPT-6.1 Sol as the default project judgment route, but do not translate OpenAI's general performance description into an unmeasured scientific-quality claim.
- Keep high-volume Daily Paper discovery on Luna/low; a scheduled turn with a different parent route stops rather than silently consuming a more expensive model.
- Treat Codex automation-2 as live and singular. Earlier negative DSH and Windows schedule evidence remains valid only for those stores and is superseded as a global absence claim.
- Do not recreate the Daily Paper schedule or unarchive the predecessor. Archive preserves history; the successor and project-owned checkpoint carry current execution state.
- Apply the shared maximum of three attempts to equivalent acquisition or access routes; only a recorded, finite exception for a major, irreplaceable scientific item may extend it.
- Use marginal context value versus cached-context cost and reliability risk as the rollover trigger; never wait for the context window to approach exhaustion.

### Open Questions

- The Codex heartbeat contract currently has no independent model field, so a durable scheduler-level Luna/low pin remains unavailable; the fail-closed parent gate is the safe current behavior.
- The exact blocked Chinese issue-022 candidate may be retained only if Human PI supplies its PDF; otherwise the successor replaces it under the bounded acquisition rule.
- Public release requires Human PI license selection before a final licensed build.
- Google Drive is unauthenticated and R/SPSS runtimes remain unverified until a real trigger requires them.
- Claude Code PATH repair still needs confirmation in a newly restarted Claude Code session.

### Known Risks

- A future heartbeat may again inherit a route above Luna/low. The gate prevents cost leakage but can hold the daily workload until a correctly routed turn is available.
- The private recurring prompt lives outside Git; its dated backup and direct content checks remain its rollback and verification mechanism.
- Conversation history can retain unique evidence if writeback is delayed, so checkpoint-first rollover remains mandatory.
- Official model guidance is not a substitute for representative project evaluations when considering xhigh, max or Astra escalation.
- The untracked artifacts/at09 directory belongs to another work stream and must not be staged by broad Git commands.

### In Progress

- Keep issue 022 held until a Luna/low Daily Paper turn can replace the blocked Chinese candidate without repeating completed SCI work.
- Confirm the Claude Code PATH repair after a genuinely restarted Claude Code session.

### Next Actions

- Daily Paper: on the next correctly routed Luna/low turn, replace the blocked issue-022 Chinese candidate under the three-attempt cap, reuse both accepted SCI files, then continue visuals, notes, brief, validation and index.
- If the next scheduled turn is not Luna/low, preserve the same fail-closed hold and report the mismatch without research work or model escalation.
- Select a public-release license only through a separate Human PI decision; do not publish private research data or credentials.
- Do not re-verify stable DSH or workspace repairs without a changed input, a failed check or a concrete contradiction.

### Evidence References

- decisions/0017-gpt61-sol-and-daily-paper-rollover.md
- artifacts/GPT61-SOL-MIGRATION-2026-09-30.md
- config/model-routing.json
- protocols/MODEL-ROUTING.md
- artifacts/daily-paper/CURRENT-STATE.md
- artifacts/daily-paper/SUCCESSOR-BOOTSTRAP-2026-09-30.md
- artifacts/daily-paper/routing-gate-state-2026-10-01.json
- D:/10_学业科研/论文_沉积物磷/90_智能体工作区/04_Lab_Research_OS/contracts/2026-09-29_每日论文_recurring_prompt.md
- packets/at11-first-supervised-research.json
- tests/test_model_routing.py
- ../../60-handoffs/CURRENT.md
- https://developers.openai.com/api/docs/models/gpt-6.1-sol
- https://developers.openai.com/api/docs/guides/reasoning
- https://developers.openai.com/api/docs/guides/model-selection
- CHECKPOINT.md
- SOL-AGENT.md

<!-- FOUNDATION-SOL-CHECKPOINT:END -->
