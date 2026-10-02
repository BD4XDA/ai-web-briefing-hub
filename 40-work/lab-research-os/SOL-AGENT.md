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

Checkpoint ID: 20261002T185908-a2d7c56e64c8
Priority: P3 · Status: in_progress
Canonical committed pointer: `checkpoints/LATEST.json`. This generated mirror is required for Sol resume, but `tools/foundation.py show` remains authoritative if IDs differ.

### Current Verified State

- The canonical repository is D:/项目仓库/赛博课题组; D:/20_代码项目/赛博课题组 remains a compatibility junction, not a second Source of Truth.
- Current project-owned GPT targets are Astra=gpt-6-astra, Sol=gpt-6.1-sol and Luna=gpt-6-luna. DeepSeek routing is unchanged and externally managed.
- The existing Codex automation-2 remains the single 08:00 Asia/Shanghai Daily Paper trigger and now targets compact successor 01a0fc40-dd4c-7652-a971-5475aca1f4cc. Both earlier Daily Paper conversations 019fb61c-c37f-7012-a760-2dcc8ce0aa4b and 01a0ecd4-1374-7df2-ad32-672e28bddac6 are archived rather than deleted.
- Daily Paper issue 022 is VERIFIED COMPLETE: three lawful full-text originals, three personal DOCX/PDF pairs, three supervisor DOCX notes and one Human PI Daily Research Brief DOCX/PDF are present. The deterministic visual and portable-path validator passed with zero errors and zero warnings.
- The replacement Chinese paper is Chen Ting et al. (2022), DOI 10.15928/j.1674-3075.202109070312, obtained from the journal site. It is a declared freshwater method-value exception, not marine evidence; salinity, sulfate/sulfide, ionic strength, hydrodynamics and benthos limit transfer.
- The 2026-10-02 TIME continuation ran under directly observed gpt-6-luna/low. No subagent, Astra, Sol/high, xhigh or max route was used. The first preflight stopped because the worker could not see its own route; local session turn_context then directly confirmed Luna/low and the same workload resumed from the exact continuation point.
- The completed continuation reported 12,533,537 turn tokens, including 11,982,336 cached input tokens, 52,568 output tokens and 16,122 reasoning-output tokens. The thread cumulative total reached 19,668,737 tokens. This is decisive evidence that marginal context cost now exceeds the value of retaining the full Daily Paper conversation history.
- Proactive rollover is complete: the compact successor resolved checkpoint 20261002T185443-bebb0c725d03 on its second readiness attempt after one transport disconnect, accurately reported issue 022 CLOSED and performed no research; automation-2 was repointed and the long conversation archived.
- The historical 73-note visual repair remains PARTIAL/PAUSED and was not resumed. Issue 022 evidence remains Discovery/Extraction/Evidence and was not promoted to validated knowledge.
- Public release remains DRAFT_READY with license_not_selected as the blocking Human PI decision. AT11 remains packet-ready and no scientific AT11 executor or reviewer has run.
- The untracked artifacts/at09 directory remains outside this work set and must not be staged.

### Completed

- Preserved and reused the two accepted issue-022 SCI originals and completed notes without reacquisition, rewrite, rerender or repeat QC.
- Replaced the blocked Chinese candidate under Luna/low with a deduplicated journal-hosted full text after marine alternatives were duplicates or outside criteria.
- Created the Chinese personal and supervisor notes with same-paper original figure interpretation, an original-text-based methods workflow and explicit freshwater-to-marine inference boundaries.
- Completed the issue-022 Human PI Daily Research Brief, evidence-ready private run record, corpus index update and shared run-level cost telemetry.
- Inspected the new Chinese note and brief renderings, repaired one workflow-label line break without changing scientific content, and passed the final visual/portable-path validator with zero errors and warnings.
- Corrected the first route-gate diagnosis using direct session turn_context evidence and preserved the superseded record as historical evidence rather than deleting it.
- Completed a checkpoint-first file-only conversation rollover, preserved the single automation, and archived the 19.67M-token predecessor after the new successor passed readiness.

### Decisions

- Issue 022 is closed as the first verified complete post-contract Daily Paper issue; this verifies the visual/path contract once but does not prove repeated-cycle reliability.
- The Erhai wetland paper is admitted only as a freshwater method-value exception. Its reported phosphorus patterns cannot be represented as marine, estuarine or tidal-flat evidence.
- Direct Codex turn_context is sufficient runtime evidence for model and effort when a worker cannot introspect them; requested route alone is not treated as actual-runtime proof.
- Conversation rollover is triggered by marginal context value versus cost and reliability, not by window exhaustion. The 11.98M cached-input continuation makes another Daily Paper rollover mandatory before the next cycle.
- Rollover must preserve project-owned state, verify a compact successor, repoint the existing automation and archive rather than delete the current conversation; this contract was exercised successfully for issue 022 closure.

### Open Questions

- Codex heartbeat metadata still has no independent model field, so future scheduled turns retain the fail-closed Luna/low gate and must use direct turn_context evidence when available.
- Public release requires Human PI license selection before a final licensed build.
- Google Drive is unauthenticated and R/SPSS runtimes remain unverified until a real trigger requires them.
- Claude Code PATH repair still needs confirmation in a newly restarted Claude Code session.

### Known Risks

- Reactivating archived Daily Paper conversation 01a0ecd4-1374-7df2-ad32-672e28bddac6 as the default execution surface would repeat multi-million-token cached-context costs and increase instruction-retrieval risk.
- A successor that imports full conversation history instead of the bounded checkpoint would reproduce the same cost defect.
- Freshwater operational phosphorus fractions, correlations and RDA are not mineral identification, process causality or sediment-water flux evidence.
- The private paper corpus and recurring prompt live outside Git; repository commits must contain state pointers and contracts only, never private full texts or notes.
- The untracked artifacts/at09 directory belongs to another work stream and must not be included by broad Git staging.

### In Progress

- Confirm the Claude Code PATH repair after a genuinely restarted Claude Code session.

### Next Actions

- Next Daily Paper TIME run in successor 01a0fc40-dd4c-7652-a971-5475aca1f4cc starts a new deduplicated daily issue under Luna/low from the master index. Do not reopen issue 022 or the historical 73-note EVENT without a changed input or direct Human PI request.
- Do not rerun stable issue-022 validation without a changed artifact or concrete defect signal.

### Evidence References

- artifacts/daily-paper/CURRENT-STATE.md
- artifacts/daily-paper/WORKLOAD-CLASSIFICATION.md
- D:/10_学业科研/论文_沉积物磷/90_智能体工作区/04_Lab_Research_OS/运行记录/2026/2026-10/2026-10-02.md
- D:/10_学业科研/论文_沉积物磷/00_总索引/总索引.md
- D:/10_学业科研/论文_沉积物磷/01_我的阅读资料/2026/2026-09/2026-09-29_第022期
- D:/10_学业科研/论文_沉积物磷/02_导师版读书笔记/2026/2026-09/2026-09-29_第022期
- C:/Users/ASUS/.codex/sessions/2026/09/29/rollout-2026-09-29T19-01-56-01a0ecd4-1374-7df2-ad32-672e28bddac6.jsonl
- protocols/CONTEXT-LIFECYCLE.md
- protocols/RESOURCE-GOVERNANCE.md
- protocols/COST-TELEMETRY.md
- ../../60-handoffs/CURRENT.md
- CHECKPOINT.md
- SOL-AGENT.md

<!-- FOUNDATION-SOL-CHECKPOINT:END -->
