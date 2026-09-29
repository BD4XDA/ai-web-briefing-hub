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

Checkpoint ID: 20260929T000830-e6268772584d
Priority: P3 · Status: complete
Canonical committed pointer: `checkpoints/LATEST.json`. This generated mirror is required for Sol resume, but `tools/foundation.py show` remains authoritative if IDs differ.

### Current Verified State

- The canonical repository root remains D:/20_代码项目/赛博课题组 and the Lab Research OS root remains its 40-work/lab-research-os directory.
- Current GPT routing remains centralized in config/model-routing.json: Luna low, Sol medium and Astra medium by default, with bounded high/xhigh escalation; DeepSeek remains unchanged and externally managed.
- Installed DSH 0.1.1-rc.2 remains structurally compatible but not live end-to-end qualified, and AT11 remains PACKET_READY and unexecuted.
- The existing Daily Paper Work conversation and its single 08:00 Asia/Shanghai heartbeat are preserved; no duplicate automation was created.
- The archive master index reaches issue 021 dated 2026-09-26; this verifies archive presence, not the scientific validity of every historical note.
- The private Daily Paper Skill survived the D-drive migration, but its Codex junction and authoritative path profile were stale; both are now repaired and the Skill entry is readable.
- The heartbeat prompt now binds resume-first behavior, explicit cost routing, evidence labels, natural infrastructure observations and the ten-section Human PI Daily Research Brief to the existing workflow. This configuration has not yet been qualified by a post-update live run.
- The 73-note historical layout/image/flowchart repair remains PARTIAL and PAUSED at preserved quota-failed continuation artifacts; six notes were reported without complete full text.
- Weekly, event, milestone and state-triggered Research Readiness workloads are classified but not deployed.
- The unrelated public-release scaffold remains an uncommitted PARTIAL task; its four discovered tests currently have two passes and two missing-seed errors and were not repaired in this work.

### Completed

- Recovered the latest Daily Paper conversation turns, the existing automation, the private Skill contract, the current archive/index and the Lab Research OS canonical checkpoint.
- Separated the interrupted historical document repair from the daily schedule and recorded its minimum continuation point without restarting it.
- Repaired current local Skill and archive locators after the D-drive migration while preserving the old junction as a recoverable stale entry.
- Updated the existing automation only; retained the 08:00 heartbeat and target conversation.
- Added the research automation trigger/evidence/resource contract, workload classification, Daily Brief template, recovered state and upgrade report.
- Kept the unrelated public-release scaffold and AT11 work untouched.

### Decisions

- Use the existing Daily Paper conversation as the first production/shadow workload; do not build a second daily system.
- Keep Literature Radar and reporting daily; require weekly, event, milestone or state triggers for other readiness work.
- Use local/cheap workers for mechanical work, Luna for discovery, Sol for scientific interpretation/QA and Astra only for architecture or unresolved structural conflicts.
- Require explicit model class and reasoning effort for every delegate; never inherit the parent highest effort.
- Treat discovery records and reports as evidence candidates, not automatically validated knowledge.

### Open Questions

- A real post-update heartbeat must establish whether routing, evidence-ready output, Daily Brief compression and quota behavior work as configured.
- Human PI approval is required before deploying the proposed weekly evidence/novelty synthesis or any additional automation.
- The six historical notes without complete full text need either lawful source recovery or an explicit decision to leave source-image insertion unavailable.
- Human PI must still choose a license before a standalone public release; any DSH upgrade qualification remains a separate authorization.

### Known Risks

- The heartbeat automation record exposes prompt, schedule and target thread but no persistent model/effort pin; actual parent-route control remains unknown.
- The existing three-full-paper workflow is intrinsically substantial; prompt routing should reduce waste but cannot be claimed effective until observed in a real run.
- The Daily Paper conversation retains a historical working-directory label from the pre-migration root; all active prompt and Skill locators therefore use explicit current roots.
- Private research paths, papers and personal profile must remain outside the public repository.
- Static DSH compatibility does not prove provider authentication, model identity, UI health or live execution, and the current public repository still contains machine-specific historical context.

### In Progress


### Next Actions

- Observe the next naturally scheduled heartbeat; record actual routes, output pointers, quota behavior and the first upgraded Daily Brief without creating a synthetic run.
- Resume the historical 73-note repair only after a new direct Human PI continuation request; continue from existing range artifacts and close one bounded unit at a time.
- Do not deploy weekly/event/milestone/state schedules until Human PI approves a specific proposal.
- Keep the public-release scaffold as a separate paused task and exclude it from this integration commit.
- Continue using config/model-routing.json for new GPT assignments; do not automatically execute AT11, upgrade DSH or publish a release.

### Evidence References

- ../../00-inbox/2026-09-29-daily-paper-research-readiness.md
- ../../10-briefs/2026-09-29-daily-paper-research-readiness.md
- ../../50-decisions/2026-09-29-daily-paper-integration.md
- decisions/0011-daily-paper-production-shadow-pilot.md
- protocols/RESEARCH-AUTOMATION.md
- templates/HUMAN-PI-DAILY-RESEARCH-BRIEF.md
- artifacts/daily-paper/CURRENT-STATE.md
- artifacts/daily-paper/WORKLOAD-CLASSIFICATION.md
- artifacts/daily-paper/RESEARCH-AUTOMATION-UPGRADE-REPORT.md
- artifacts/daily-paper/VALIDATION.md
- SOL-AGENT.md

<!-- FOUNDATION-SOL-CHECKPOINT:END -->
