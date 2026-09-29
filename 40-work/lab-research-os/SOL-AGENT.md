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

Checkpoint ID: 20260929T203829-b113799fa300
Priority: P3 · Status: in_progress
Canonical committed pointer: `checkpoints/LATEST.json`. This generated mirror is required for Sol resume, but `tools/foundation.py show` remains authoritative if IDs differ.

### Current Verified State

- The single canonical repository is D:/项目仓库/赛博课题组 and Lab Research OS is D:/项目仓库/赛博课题组/40-work/lab-research-os.
- D:/20_代码项目/赛博课题组 is a <JUNCTION> to the canonical repository for compatibility; it is not a duplicate Source of Truth, and the junction still resolves correctly.
- The repository remains on main at commit 7ecf070b0ae7e5a0f9d624a6c3a1dd86099a30ac; the migration, DSH and incident writebacks remain uncommitted and the untracked artifacts/at09 work is preserved.
- DSH core is 0.1.7-rc.2. The running Web host is PID 11724, started 2026-09-29T20:15:40+08:00 with `--profile lab-research --host 127.0.0.1 --port 3080 --no-open`; the legacy `web` profile is not running.
- DSH Web session creation failed twice in one episode and both causes are repaired: a drive-root Workspace registration raised EPERM on mkdir, and the laboratory Workspace failed to attach because its registration named the compatibility junction. The Human PI confirmed on 2026-09-29 that new-session creation in the Web UI now works, so the repair is verified end to end.
- Workspace attach compares the fs.realpath of a Session's cwd against the unresolved registered path string for exact equality, so any Workspace registered through a junction or symlink can never attach and its Sessions are also filtered out of the listing.
- The laboratory Workspace e4c2f3c7 is now registered as the canonical D:/项目仓库/赛博课题组; the three pre-existing Sessions, whose headers still carry the junction path, all resolve to that value and are attachable and visible again.
- Every remaining registered Workspace passes the same realpath equality check and none has a resolution mismatch; five stale registrations simply point at directories that no longer exist.
- No DSH vendor code, credential, session, attachment or research file was modified; the only DSH state changes are two Workspace registry edits, each made after a dated backup with the web server stopped.
- Daily Paper issue 022 remains PARTIAL with two completed SCI acquisitions and one download-blocked Chinese candidate; its minimal next action is to replace that candidate under Luna low and the three-attempt cap.
- The existing Daily Paper conversation still meets the early-rollover trigger and the recurring workflow remains singular; a successor must resolve this checkpoint before the schedule is repointed and the predecessor archived.
- Global bounded retries, passive cost telemetry and silent SOL-AGENT checkpoint mirroring remain active.
- The Claude Code PATH override was removed from C:/Users/ASUS/.claude/settings.json after a dated backup; a diff against the backup shows only the PATH entry and its preceding comma changed, every other env key and every other top-level key is byte-identical, and the file still parses as strict JSON.
- The override was redundant as well as harmful: the real user PATH already carries nodejs, Git cmd, Python, dotnet and the npm global directory, and the machine PATH carries %SystemRoot%\system32, so removing the override strictly widens the shell PATH instead of narrowing it.
- Direct evidence found no stored 08:00 heartbeat: the running lab-research profile has no `storages/schedule.json` (the Schedule domain is rejected as absent/empty when the file is missing), the legacy `task-board/ledger-v2.json` holds an empty `tasks` array with scheduler.ledgerId d973865a and lastTickAt 1789043938913, Windows Task Scheduler has no matching non-Microsoft task, and no DSH session log ever contains a `schedule_create` call or the literal title 每日沉积物磷论文整理.
- No DSH session file was modified between 2026-09-28T20:00 and 2026-09-29T12:26 local time, so the 08:00 heartbeat did not deliver on either 2026-09-29 or 2026-09-30; the earliest 2026-09-29 session write is 12:26:04.
- The Daily Paper data root shows no file modified on 2026-09-30; its newest write is the 2026-09-29 18:44 run record, consistent with an afternoon manual run rather than a scheduled morning delivery.
- The junction path still appears in one live configuration: the Daily Paper recurring prompt at D:/10_学业科研/论文_沉积物磷/90_智能体工作区/04_Lab_Research_OS/contracts/2026-09-29_每日论文_recurring_prompt.md told the agent to read Lab Research OS through D:/20_代码项目/...; it was corrected to the canonical D:/项目仓库/... path after a dated backup.

### Completed

- Moved the complete repository into the empty Human PI-designated project store without merging content or losing the untracked AT09 directory.
- Created a compatibility junction at the former repository path so stale local tools fail safe into the same canonical files rather than a second copy.
- Updated current project locators, infrastructure map and active Daily Paper and AT11 task packet paths while preserving historical checkpoints and decisions unchanged.
- Added the context lifecycle protocol and stable instructions for checkpoint-first, value-based conversation rollover.
- Verified post-migration DSH state from live evidence and proved DeepSeek-native independence by direct falsification, recorded in artifacts/DSH-DEEPSEEK-NATIVE-INDEPENDENCE-2026-09-29.md.
- Diagnosed and repaired the first DSH Web session-creation failure: the drive-root Workspace registration was removed using the workspace controller's own delete semantics, with a dated backup and the server stopped.
- Diagnosed and repaired the second failure in the same episode: the laboratory Workspace path was repointed from the compatibility junction to the canonical repository path, derived from fs.realpathSync rather than hardcoded.
- Verified that newly created Sessions and all three pre-existing Sessions now resolve to the registered workspace path, and that no remaining Workspace has a realpath mismatch.
- Recorded both causes, their source evidence and the repairs in incidents/2026-09-29-dsh-drive-root-workspace-session-failure.md and corrected the capability registry accordingly.
- Confirmed the legacy web profile, the Codex adapter, the Sol/Luna router and the Exa route remain isolated and are not loaded by either clean profile.
- Re-ran the deterministic project regressions: 36 unit tests, model routing validation and capability registry validation all pass.
- Received Human PI confirmation that new-session creation in the DSH Web UI works, closing the only repair step that could not be exercised locally.
- Diagnosed and removed the Claude Code PATH override that replaced the process PATH with a literal unexpanded %PATH% token, which had been hiding System32 and the npm global directory from every Claude Code shell.
- Wrote the Daily Paper successor bootstrap at artifacts/daily-paper/SUCCESSOR-BOOTSTRAP-2026-09-30.md: a compact, copy-paste prompt that names the canonical root, the exact read set, the Luna/low ceiling, the no-browsing bootstrap rule and the four required resume lines.
- Corrected the Daily Paper recurring prompt to read Lab Research OS through the canonical root, preserving the prior revision as a dated .bak file.
- Re-ran all 36 project unit tests after these writes; they still pass.
- Empirically decoded the DSH session store for this investigation: session logs are concatenated zstd frames, and read-only probes now exist at C:/Users/ASUS/.dsh/probe-zstd3.cjs, probe-find2.cjs, probe-find3.cjs and probe-survey.cjs for future session-history questions.

### Decisions

- The Human PI-designated D:/项目仓库/赛博课题组 path is the canonical repository; the former path is compatibility-only, and DSH registrations must now name the canonical path rather than the junction.
- Conversation history is an execution cache, not project memory. Project-owned checkpoint, decisions and evidence references are the durable resume surface.
- DeepSeek-native independence is an acceptance property of the harness, while GPT/OpenAI integration stays optional and separately governed; no GPT model-routing policy change was authorized or made.
- A Workspace registration that can never be created in is a defect to remove, not a cosmetic tidy-up: the drive-root registration was deleted while retaining files and Sessions.
- A Workspace registered through a junction or symlink is a defect to repoint, because DSH compares a canonicalised cwd against the unresolved registered string.
- Stale Workspace registrations that still hold historical Sessions are left registered; removing them would discard usable history and is not required to fix the reported failures.
- DSH vendor code is not patched locally even when it is the robustness gap, because local patches are lost on update; such gaps are reported for upstream instead.
- The Claude Code settings.json literal %PATH% defect was repaired on 2026-09-29, superseding the earlier decision to leave it reported rather than fixed; closure still requires one restarted-session confirmation.
- The 08:00 heartbeat must not be treated as live merely because a prior checkpoint asserted it: the claim is contradicted by fresh direct evidence, so the schedule is treated as absent until the Human PI locates it or it is recreated once for the successor.
- Recreating the heartbeat is a single repoint-or-recreate action inside the existing Daily Paper workflow, never a second parallel automation; the recurring prompt stays versioned in the research data root rather than duplicated into the repository.

### Open Questions

- The exact blocked Chinese issue-022 candidate may be retained only if Human PI later supplies its PDF; otherwise the successor replaces it automatically under the bounded acquisition rule.
- Public release remains DRAFT_READY and still requires Human PI license selection before a final licensed build.
- Google Drive remains unauthenticated and R/SPSS runtimes remain unverified until a real trigger requires them.
- Whether the retired settings.yaml keys describe-image and llm-deepseek vision models should be restored under the clean profiles; no current visual workload requires them.
- Whether the five stale Workspace registrations should be retired or relocated to their new Desktop ministry paths.
- Where the 08:00 Daily Paper heartbeat was actually authored and stored, and which Session it targets: no DSH Schedule task, legacy ledger entry, Windows task or session-log record of one was found, so only the Human PI can identify it in the running GUI.
- Whether the Daily Paper predecessor conversation still exists in the running GUI at all; no DSH session in the store carries its project root or its content, so its identity cannot be confirmed from files alone.

### Known Risks

- External tools may retain the former path; the compatibility junction prevents immediate breakage, but new configuration must use the canonical path.
- Any tool that registers a DSH Workspace through a junction or symlink will reproduce the attach failure, because the registered string is compared unresolved against a canonicalised cwd.
- Archiving the old Daily Paper conversation before successor recovery or schedule repointing would risk losing the active execution route, so archival is last.
- Conversation rollover can lose scientific meaning if judgments or evidence remain only in chat; the pre-rollover writeback gate is mandatory.
- Selecting a stale Workspace registration silently recreates an empty directory at a path the Human PI has since reorganized away, which can leave stray folders behind.
- A verification that exercises only boot and serve can declare a path qualified while a later, unexercised operation still fails; qualification claims must name the operations actually exercised.
- The Claude Code PATH override has been removed in configuration, but it takes effect only after a Claude Code restart; a success claim is not valid until one shell in a restarted session resolves System32 and the npm bin directory.
- lab-headless inherits the session projection cache enabled while lab-research disables it; no headless failure was observed, so this is reserved rather than fixed.
- If the 08:00 heartbeat was attached to the legacy web profile, it can no longer deliver while only lab-research runs on port 3080, and a silent schedule loss would look exactly like a healthy quiet day.
- A checkpoint that asserts a live automation without naming its storage location cannot be audited later; the corrected state must therefore name the negative evidence, not just the missing task.
- The corrected Daily Paper recurring prompt lives outside the repository, so it is not covered by repository review or rollback; it needs its own dated backup discipline.

### In Progress

- Create one fresh Daily Paper successor conversation in the laboratory Workspace with Luna low, using artifacts/daily-paper/SUCCESSOR-BOOTSTRAP-2026-09-30.md as its first message.
- Verify the successor resolves the checkpoint and reports the exact issue-022 continuation without rerunning research.
- Repoint the existing Daily Paper recurring task to the successor, or recreate that single task once if the Human PI confirms it no longer exists, then archive the predecessor as historical reference.
- Confirm in a restarted Claude Code session that the shell PATH now resolves System32 and the npm global directory.

### Next Actions

- Ask the Human PI to locate the 08:00 Daily Paper task in the running GUI and report whether it still exists and which conversation it targets; that answer decides repoint versus recreate.
- Create the Daily Paper successor from artifacts/daily-paper/SUCCESSOR-BOOTSTRAP-2026-09-30.md with no browsing, acquisition or scientific recomputation during bootstrap.
- Accept the successor only when it reports RESOLVED_CHECKPOINT, ISSUE_022_STATE=PARTIAL and a NEXT_ACTION that names the replacement of the blocked Chinese candidate or the validation of a Human PI-supplied PDF.
- Update or recreate the single 08:00 target only after readiness succeeds; never create a second recurring task.
- Archive the predecessor after successful repointing, then run tests, advance the final checkpoint if rollover state changed, commit and push.
- Do not re-verify the DeepSeek-native path or the repaired Workspace registry without a changed input, a failed check or a specific contradiction.
- After the next Claude Code restart, verify the shell PATH contains System32 and %APPDATA%\npm, and that a bare dsh invocation resolves; only then consider the PATH defect closed.
- Decide separately whether to align the lab-headless projection cache with lab-research and whether to retire the stale Workspace registrations.

### Evidence References

- artifacts/daily-paper/SUCCESSOR-BOOTSTRAP-2026-09-30.md
- D:/10_学业科研/论文_沉积物磷/90_智能体工作区/04_Lab_Research_OS/contracts/2026-09-29_每日论文_recurring_prompt.md
- D:/10_学业科研/论文_沉积物磷/90_智能体工作区/04_Lab_Research_OS/运行记录/2026/2026-09/2026-09-29.md
- artifacts/daily-paper/CURRENT-STATE.md
- incidents/2026-09-29-dsh-drive-root-workspace-session-failure.md
- artifacts/DSH-DEEPSEEK-NATIVE-INDEPENDENCE-2026-09-29.md
- artifacts/DSH-017-UPGRADE-REPORT.md
- artifacts/REPRESENTATIVE-VERIFICATION-2026-09-29.md
- config/capability-registry.json
- artifacts/telemetry/run-cost.jsonl
- decisions/0016-canonical-root-return-and-context-rollover.md
- protocols/CONTEXT-LIFECYCLE.md
- protocols/COST-TELEMETRY.md
- protocols/RESOURCE-GOVERNANCE.md
- packets/canonical-root-context-rollover-state.json
- PROJECT.md
- AGENTS.md
- SOL-AGENT.md
- CHECKPOINT.md

<!-- FOUNDATION-SOL-CHECKPOINT:END -->
