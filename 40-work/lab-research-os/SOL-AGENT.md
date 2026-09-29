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

Checkpoint ID: 20260929T120741-8786a6aaca0b
Priority: P3 · Status: in_progress
Canonical committed pointer: `checkpoints/LATEST.json`. This generated mirror is required for Sol resume, but `tools/foundation.py show` remains authoritative if IDs differ.

### Current Verified State

- The canonical repository root remains D:/20_代码项目/赛博课题组 and the Lab Research OS root remains its 40-work/lab-research-os directory; D:/项目仓库/赛博课题组 is not a valid working root.
- Current GPT routing remains centralized in config/model-routing.json: Luna low, Sol medium and Astra medium by default, with bounded high/xhigh escalation; DeepSeek remains unchanged and externally managed.
- The existing Daily Paper conversation and its single 08:00 Asia/Shanghai heartbeat remain active; no duplicate automation exists.
- The live heartbeat and private Skill now require same-paper source visuals, source-traceable method/research workflows and portable published paths for every new note.
- The private validator compiles with opt-in --require-visuals and --require-portable-paths gates; historical issues are not failed by default.
- The real Event-triggered note-073 pilot completed and verified bounded resume, source matching, rendered visual QA, local recovery, a ten-section Daily Research Brief and zero-default-Astra behavior.
- Two over-budget supervisor paths in issue 021 were shortened without changing document content; both final paths open directly in Word and render cleanly, and the complete issue passes the portable-path gate.
- A read-only scan found 34 other historical supervisor DOCX paths above the new budget; they remain a separate Event migration backlog.
- The future visual and portable-path contracts remain IMPLEMENTED BUT UNVERIFIED by a complete post-contract new issue.
- The unrelated public-release scaffold remains an uncommitted PARTIAL task and AT09 remains untouched.

### Completed

- Closed the note-073 Event pilot from its preserved continuation point instead of restarting it.
- Independently compared the inserted source figure and eight-node workflow with the paper's source pages and inspected every rendered page.
- Repaired the published-path defect for two issue-021 supervisor DOCX files and verified direct Word open plus clean rendering from their final locations.
- Added a short-filename contract, a 140-character filename budget, a 240-character full-path budget and the --require-portable-paths validator gate for new issues.
- Updated the existing heartbeat rather than creating another automation, and added Research Readiness Integration Report v3 plus Decision 0013.

### Decisions

- Complete English article titles remain inside notes and the master index rather than supervisor filenames.
- New generated human-deliverable filenames must be at most 140 characters and complete absolute paths at most 240 characters.
- A final DOCX must be opened or rendered from its published path; a staged-copy render alone is insufficient.
- The note-073 Event pilot qualifies only its bounded resume, evidence, visual-QA, recovery, budget and Daily Brief observations; it does not qualify the next scheduled new issue.
- Historical over-budget paths form an Event backlog and are not silently bulk-renamed or retroactively invalidated.

### Open Questions

- A complete future Daily Paper issue must pass --require-visuals and --require-portable-paths plus source/flowchart scientific review before the standing contract is live-qualified.
- Thirty-four historical supervisor paths remain above the new budget and require Human PI approval for a bounded bulk migration.
- Six historical notes still lack complete lawful full text and remain blocked for evidence-bearing source-image insertion.
- Human PI approval is still required before deploying weekly synthesis or additional automation, executing AT11, qualifying a DSH upgrade or selecting a public-release license.

### Known Risks

- Section labels, drawing counts and path-length checks do not prove scientific correctness; source inspection and visual QA remain required.
- Scheduled heartbeat model pinning and a complete post-contract new issue remain unverified.
- Historical path migration can stale working manifests unless it uses a reversible rename map and updates active references.
- Private research paths, full texts, images and personal profile remain local and must not enter the public repository.
- The local repository remains ahead of origin because earlier GitHub pushes encountered a TLS handshake failure; remote publication is not assumed.

### In Progress

- Daily Paper production/shadow pilot remains active at the system level; the next live qualification event is a complete scheduled new issue under both validator gates.
- Historical image/flowchart repair remains PARTIAL with note 072 as the next content unit and 34 path-only historical migrations held for separate authorization.

### Next Actions

- Observe the next genuinely new Daily Paper issue and run both validator gates plus source/flowchart scientific review before claiming live qualification.
- Resume note 072 only from preserved evidence when the historical Event workload is explicitly continued.
- Keep the six source-incomplete notes blocked rather than manufacturing visuals.
- Do not bulk-rename the 34 historical paths, create new schedules, execute AT11, upgrade DSH or continue the public-release scaffold without the relevant Human PI decision.
- Retry GitHub push without changing credentials or remote configuration when connectivity permits.

### Evidence References

- ../../50-decisions/2026-09-29-daily-paper-portable-paths.md
- decisions/0013-daily-paper-portable-paths-and-pilot-observation.md
- protocols/RESEARCH-AUTOMATION.md
- artifacts/daily-paper/PILOT-073-VERIFICATION.md
- artifacts/daily-paper/RESEARCH-READINESS-INTEGRATION-REPORT-v3.md
- artifacts/daily-paper/CURRENT-STATE.md
- artifacts/daily-paper/WORKLOAD-CLASSIFICATION.md
- artifacts/daily-paper/VALIDATION.md
- SOL-AGENT.md

<!-- FOUNDATION-SOL-CHECKPOINT:END -->
