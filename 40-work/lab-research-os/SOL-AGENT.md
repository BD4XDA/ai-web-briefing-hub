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

Do not rerun an accepted deterministic check merely for reassurance. Rerun only when inputs changed, a check failed, or a specific contradiction requires discrimination.

## 4. Sol's role

Sol is primarily the scientific, visual, and high-rigor quality reviewer. The harness provides execution; the selected model provides reasoning. A wrapper name is not proof of the actual model identity or capability.

For new project-owned assignments, Sol's requested model target is `gpt-6-sol`. Sol's default reasoning effort is `medium` for everyday research, coding and synthesis; use `low` for focused editing/fact checks, and `high` for independent scientific or visual review, deep verification or consequential acceptance. `xhigh` is exceptional and requires representative evaluation evidence or explicit Human PI authorization. The machine-readable source is `config/model-routing.json`; validate it with `python tools/model_routing.py validate`. Do not route new Sol work to GPT 5.6 or silently fall back when GPT-6 Sol is unavailable. Record requested model/effort and actual runtime identity separately; missing required capability holds the task. Historical artifacts may still mention GPT-5.6 Sol because they preserve earlier observed configuration.

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

Checkpoint ID: 20260929T174406-62590a5094c2
Priority: P3 · Status: in_progress
Canonical committed pointer: `checkpoints/LATEST.json`. This generated mirror is required for Sol resume, but `tools/foundation.py show` remains authoritative if IDs differ.

### Current Verified State

- The canonical repository root is D:/20_代码项目/赛博课题组 and Lab Research OS is its 40-work/lab-research-os directory.
- Need-driven capability governance is active through config/capability-registry.json and protocols/CAPABILITY-GOVERNANCE.md; installation or runtime visibility is not integration.
- The registry currently manages 13 capabilities: seven core, four on-demand and two watch-only; legacy dsh-sol-luna-router and Exa MCP are blocked rather than treated as production routes.
- Global @deepseek-ai/dsh is 0.1.7-rc.2. Clean lab-research Web and lab-headless profiles are live and qualified for bounded Web/text use.
- The legacy DSH web profile is preserved but is not the qualified route because its Codex adapter and patch target older DSH APIs; the custom router also retains obsolete GPT-5.6 and retired DeepSeek identifiers.
- During qualification the DSH Web UI listened on 127.0.0.1:3080, recognized the D:/20_代码项目/赛博课题组 workspace and used workspace-write for new work; a clean headless DeepSeek call from the canonical project returned DSH_OK. Current daemon liveness is not assumed after the managed test session ends.
- The Daily Paper conversation and its single daily heartbeat remain active. Its future source-visual and portable-path contract is still pending qualification by a complete new issue.
- Weekly automation automation-3 performs a read-only capability update check; it cannot automatically install, remove, enable or reconfigure capabilities.
- The unrelated public-release scaffold remains uncommitted/partial and AT09 remains untouched.

### Completed

- Created and validated capability-registry schema, manifest, validator, tests and governance protocol.
- Admitted only capabilities tied to active or credible near-term research workloads instead of treating every installed Skill/MCP as a service.
- Backed up DSH configuration and upgraded the global Harness from 0.1.1-rc.2 to npm latest 0.1.7-rc.2 without copying or modifying sessions and attachments.
- Created clean lab-research and lab-headless profiles, removed expired model overrides from the clean Web profile, set workspace-write and disabled only the rebuildable Windows-incompatible projection cache.
- Verified DSH version, Web activation, Lab workspace visibility and one bounded live DeepSeek text call.
- Changed the local dsh-web launcher to the qualified lab-research profile while retaining the legacy profile and rollback data.
- Created active weekly capability update heartbeat automation-3.

### Decisions

- Capabilities are managed by need, trigger, evidence and fallback; installed does not imply integrated or qualified.
- Weekly checks are read-only and signal-driven. They never auto-upgrade developer-preview harnesses, plugins, MCPs or scientific workflows.
- DSH 0.1.7-rc.2 npm latest is adopted; the 0.2.0 next channel is not adopted.
- Clean DSH profiles are the qualified route. Legacy optional plugins and the Sol/Luna router remain isolated until migrated against current APIs and GPT-6/valid DeepSeek identifiers.
- DeepSeek model policy remains externally managed; this maintenance changed the harness and qualified profiles, not config/model-routing.json's GPT routing boundary.

### Open Questions

- Whether and when to migrate the legacy Sol/Luna router to DSH 0.1.7 APIs and GPT-6 routes depends on a real workload requiring mixed-provider failover.
- Exa MCP remains unnecessary for current production because the existing web research path is available; requalification should wait for a workload need.
- R, SPSS, Google Drive and explanatory-visual capabilities remain on-demand/unverified until their first representative research task.
- The next complete Daily Paper issue remains the live qualification event for the visual and portable-path contract.

### Known Risks

- DeepSeek Harness is a developer preview and future releases may break profiles or plugins.
- The legacy Web plugin set includes incompatible and deprecated packages; it must not replace the clean qualified route without evidence.
- Disabling the projection cache can slow historical session listing but does not remove authoritative session logs.
- Runtime-managed Skills/MCPs may change independently; weekly checks detect meaningful drift but do not prove every connector's authentication or scientific suitability.
- Private credentials, research papers and annotations remain outside the repository and must not be included in update reports.

### In Progress

- Daily Paper production/shadow pilot remains active; its next complete new issue supplies the outstanding live qualification evidence.
- Capability registry entries will be promoted from installed/unverified only when a real triggered workload supplies representative evidence.
- DSH Web is available through the updated dsh-web launcher and clean lab-research profile; it is started on demand rather than claimed as a permanent service.

### Next Actions

- Use the clean DSH profiles for bounded work and keep the legacy profile/router isolated.
- Review the weekly capability update result only when it reports a meaningful version, deprecation, compatibility or core health change.
- Qualify R/SPSS/cloud/visual capabilities only at their declared data, event or on-demand trigger; do not run synthetic integration campaigns.
- Observe the next genuinely new Daily Paper issue under both validator gates before promoting its standing visual contract.
- Do not bulk-update third-party DSH plugins, enable Exa, migrate the legacy router or alter credentials without a scoped maintenance decision.

### Evidence References

- decisions/0014-capability-governance-and-dsh-017.md
- config/capability-registry.json
- schemas/capability-registry.schema.json
- protocols/CAPABILITY-GOVERNANCE.md
- artifacts/DSH-017-UPGRADE-REPORT.md
- tools/capability_registry.py
- tests/test_capability_registry.py
- artifacts/daily-paper/CURRENT-STATE.md
- artifacts/daily-paper/VALIDATION.md
- CHECKPOINT.md
- SOL-AGENT.md

<!-- FOUNDATION-SOL-CHECKPOINT:END -->
