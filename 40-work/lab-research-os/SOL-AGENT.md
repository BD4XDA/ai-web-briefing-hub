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

Checkpoint ID: 20260928T132433-391786e56d73
Priority: P3 · Status: complete
Canonical committed pointer: `checkpoints/LATEST.json`. This generated mirror is required for Sol resume, but `tools/foundation.py show` remains authoritative if IDs differ.

### Current Verified State

- Canonical repository root migrated to D:/20_代码项目/赛博课题组 and project root to D:/20_代码项目/赛博课题组/40-work/lab-research-os; active paths were updated while historical records were preserved.
- Current GPT routing is centralized in config/model-routing.json: Luna low, Sol medium and Astra medium by default, with bounded high/xhigh escalation rules.
- DeepSeek routing and external DSH/provider configuration remain unchanged.
- Installed DSH 0.1.1-rc.2 is structurally compatible with the project through AGENTS/CLAUDE instruction discovery plus workspace filesystem and command tools; no upgraded or paid-model end-to-end qualification was performed.
- The public GitHub repository is visible, but a standalone public release is held pending licensing, security/contribution documents, path sanitization, historical-artifact curation and clean-room installation tests.
- AT11 remains PACKET_READY and unexecuted; its future gpt-6-sol scientific review now requests reasoning effort high.

### Completed

- Adopted the D-drive path migration through Decision 0010 and rebound current AT11 project/source locators without running the science task.
- Reviewed official OpenAI GPT-6 model, reasoning, pricing and changelog guidance and recorded primary-source references.
- Added the model-routing manifest, JSON Schema, validator, four new tests and routing protocol; all 24 project unit tests pass.
- Inspected installed and upstream DSH versions without mutation and documented structural compatibility plus upgrade risks.
- Completed a static public-release audit and comparable-project analysis; corrected the root README public/private mismatch.

### Decisions

- Use the migrated repository and corpus roots for current work; preserve old paths only as historical observations.
- Use the lightest route and reasoning effort that meets a predeclared quality gate; do not default to xhigh or max.
- Keep DeepSeek unchanged and outside the GPT routing manifest.
- Do not upgrade the working DSH profile in place; qualify a pinned isolated profile before adoption.
- A public release must be a sanitized clean export or standalone repository, not a raw publication of internal history.

### Open Questions

- Human PI must choose a license and authorize a standalone public-release construction/publish task.
- A future separately authorized DSH qualification should decide whether to target npm latest 0.1.5-rc.3 or the 0.1.7 prerelease line after plugin compatibility review.
- Representative quality/cost evaluations are still required before changing default efforts or adopting a future GPT model generation.

### Known Risks

- Static DSH compatibility does not prove provider authentication, model identity, web UI health or live end-to-end execution.
- The already-public repository contains machine-specific paths and historical execution context even though the high-confidence static scan found no token/private-key signature.
- Official product capabilities, pricing and release status can change; the routing policy records its review date and must be re-evaluated before a future migration.

### In Progress


### Next Actions

- Use config/model-routing.json for new GPT assignments and validate any change with python tools/model_routing.py validate.
- If the Human PI authorizes public packaging, build a clean sanitized distribution with license/security/contribution files, synthetic examples and CI; do not copy raw artifact history.
- If the Human PI authorizes DSH upgrade qualification, use an isolated pinned profile and preserve the current working profile. No automatic AT11 science, AT09 work or successor is authorized.

### Evidence References

- ../../00-inbox/2026-09-27-gpt6-routing-dsh-public-release.md
- ../../10-briefs/2026-09-27-gpt6-routing-dsh-public-release.md
- ../../20-research/2026-09-27-gpt6-dsh-comparables.md
- ../../50-decisions/2026-09-27-gpt6-cost-routing.md
- decisions/0009-gpt6-cost-routing-and-portability.md
- config/model-routing.json
- schemas/model-routing.schema.json
- tools/model_routing.py
- tests/test_model_routing.py
- protocols/MODEL-ROUTING.md
- artifacts/GPT6-DSH-PUBLIC-RELEASE-ASSESSMENT.md
- decisions/0010-canonical-root-migration.md
- packets/at11-first-supervised-research.json
- SOL-AGENT.md

<!-- FOUNDATION-SOL-CHECKPOINT:END -->
