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

Checkpoint ID: 20261010T075702-ea5655d7b238
Priority: P3 · Status: in_progress
Canonical committed pointer: `checkpoints/LATEST.json`. This generated mirror is required for Sol resume, but `tools/foundation.py show` remains authoritative if IDs differ.

### Current Verified State

- Daily Paper Issues 022 and 023 remain VERIFIED COMPLETE; Issue 024 has not started, and the broad discovery/full-text/version-verification rules remain active.
- DSH Desktop 0.2.0-rc.2 now starts normally; no host crash log newer than the repaired 2026-10-08 failures was present on 2026-10-10.
- The desktop profile pins @linxin666/dsh-remote-web-ui 0.4.5, which targets DSH >=0.2.0-rc.2 and uses webServer + typertGateway + connection rather than the removed legacy apiProxy service.
- The remote host listens on 0.0.0.0:19387; its LAN posture probe reports 10.190.28.65:19387 not exposed, an unpaired /remote API request returns 403, and direct LAN /api access returns 401.
- The plugin reports LAN available and preserves four existing paired-device records with zero devices online at verification time; no device records were revoked automatically.

### Completed

- Disabled the incompatible voice plugin entry that caused the first Desktop startup crash while preserving dated profile backups.
- Replaced remote-web-ui 0.2.9 and the obsolete direct dsh-host-apiproxy dependency with remote-web-ui 0.4.5.
- Installed the declared cloudflared 0.7.3 optional tunnel binary, kept autoTunnel disabled, and configured the plugin-managed LAN bind block with the Web compression defaults.
- Verified live Desktop startup, listener state, pairing status route, LAN posture, unpaired-channel denial and direct-API denial without computing unnecessary hashes.
- Recorded the repair decision, rollback path, bounded firewall failure and run-level cost telemetry.

### Decisions

- Do not mix the removed legacy apiProxy service into Desktop 0.2.0-rc.2; use a remote-control plugin release whose declared cohort matches the installed Desktop.
- Default to paired LAN access on 0.0.0.0:19387 without trusting LAN hosts for direct /api access; keep the public tunnel off until explicitly needed.
- If a firewall rule is added, scope it to TCP 19387 on Private/Domain profiles rather than opening the port on all Public networks.
- Treat phone scan/control as unverified until a real phone completes the pairing round trip; Configured and host-live are not end-to-end qualification.

### Open Questions

- Human PI must accept an administrator firewall change if the phone cannot reach 10.190.28.65:19387 on the same private Wi-Fi.
- A real phone scan and control round trip is still required to promote the remote-control capability to end-to-end VERIFIED.

### Known Risks

- Windows Defender Firewall currently has no remote-web-ui (auto) inbound rule; the status endpoint reports firewall ok false even though the local LAN-address probe reaches the listener from the same machine.
- The three-attempt limit for the firewall permission failure class was reached; further automated retries are stopped until administrator authorization changes.
- The optional public tunnel passes traffic through third-party infrastructure and therefore remains installed but disabled by default.
- Existing paired-device records are full-control credentials after pairing; Human PI should revoke unfamiliar devices in the plugin panel.

### In Progress

- Daily Paper Issue 024 awaits the existing daily trigger or a direct Human PI request.
- DSH phone control awaits only the administrator firewall rule if required and one Human PI phone scan/control test.

### Next Actions

- If the phone cannot connect on the same private Wi-Fi, run the exact Private/Domain TCP 19387 netsh rule from the repair artifact in an elevated terminal.
- Open the phone icon beside DSH Desktop settings, refresh the QR code, scan it on the phone and verify one chat/control round trip; then record E2E PASS or the smallest observed defect.
- Do not enable autoTunnel merely to fill a test; enable it only when off-LAN access is actually needed and recheck the exposure posture afterward.
- For Daily Paper Issue 024, resume from the existing project state and broad-discovery contracts without repeating Issues 022 or 023.

### Evidence References

- artifacts/DSH-DESKTOP-REMOTE-CONTROL-REPAIR-2026-10-10.md
- ../../50-decisions/2026-10-10-dsh-desktop-remote-control-repair.md
- ../../60-handoffs/CURRENT.md
- artifacts/telemetry/run-cost.jsonl
- C:/Users/ASUS/.dsh/profiles/desktop/package.json
- C:/Users/ASUS/.dsh/profiles/desktop/cordis.patch.yml
- C:/Users/ASUS/AppData/Roaming/@deepseek-ai/dsh-desktop/logs

<!-- FOUNDATION-SOL-CHECKPOINT:END -->
