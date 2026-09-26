# AT10 A — Responsibility matrix

Date: 2026-09-22. Auditor: Astra, governance/architecture capacity. This is an audit, not role deployment or an independent certification of Astra. B–D contain findings and proposals; none changes operating rules.

## Resolved authority and evidence boundary

Canonical project: `D:/项目仓库/赛博课题组/40-work/lab-research-os`. The app project registry identifies its parent repository as the saved “课题组构建” project; `.lab-project.json` confirms `project_id=lab-research-os`. Direct `python tools/foundation.py show` succeeded with **20260922T155833-7fcdcab38f00**, EXIT / complete. LATEST, CHECKPOINT and generated SOL mirror agree. Git HEAD at entry: `5c9c75f`; initial status: only `?? artifacts/at09/`. The current task is the Human PI's AT10 attachment, overriding historical next-action suggestions.

Discovery discrepancy: the former dated C-drive root was absent. A C-drive hub copy at `C:/Users/ASUS/Documents/Codex/ai-web-briefing-hub/40-work/lab-research-os` had AT08 LATEST and `foundation.py show` failed with `Checkpoint integrity conflict`. The saved-project registry then located the D-drive root above. No C-drive files were changed, no cause of its byte mismatch was inferred, and no extra digest investigation was needed. This stale copy is not current engineering truth. Historical absolute paths remain historical locators, not permission to execute old packets at the wrong root.

Digest use is limited to Foundation's mandatory immutable-checkpoint read/write contract: it detects mismatch between the snapshot bytes and committed pointer. No evidence-package or accepted test hashes were recalculated. Byte identity does not establish semantic truth. Direct file inspection and retained execution receipts underpin this audit; no old tests or model review were rerun.

## Source key (relative to this root)

| Key | Source and precise use |
|---|---|
| R | `AGENTS.md`, `PROJECT.md`: roles, authorization, writes, exclusions, escalation |
| V | `protocols/VERIFICATION.md`, `decisions/0002-evidence-gates.md`: independent review, gates, L0–L3 |
| H | `protocols/HANDOFF.md`: per-packet owner, verifier, write set, review and checkpoint |
| M | `protocols/MEMORY.md`, `decisions/0001-canonical-memory.md`: persistent state ownership and promotion |
| S | `SOL-AGENT.md` stable sections: scientific/visual QA and consequential acceptance review |
| C | `checkpoints/20260922T155833-7fcdcab38f00.json`, Decisions 0004/0005, `tools/foundation.py`: current authority, mirror, evidence proportionality |
| E3 | `packets/at03-loop-01.json`, `artifacts/at04/P5-ACCEPTANCE.md`: assigned worker/checkpoint ownership; later qualification of the worker's PROVEN claim |
| E5 | `artifacts/at05/EXCEPTION-JUDGMENT.md`: blocked attempt, package omission, event-classification defect, withheld writeback and C2 qualification |
| E7 | `artifacts/at07/REPAIR-SCOPE.md`, `regression-execution.json`, `review-execution.json`, `review-acceptance.json`, `FINAL-REPAIR-STATUS.json`: actual retained test/review receipts, local scope and disabled adoption |
| E8 | `artifacts/at08/ANOMALY-ADJUDICATION.json`, `NEXT-ACCEPTANCE-DESIGN.md`: coordinator dispositions distinct from independent review; successor gate unchanged |

These are source locators, not claims that all historical assertions were independently reacquired. E7 reports one DSH execution and a model evidence-package review; it does not authenticate the underlying model or independently observe machine state. Historical execution is not current liveness.

## Current role inventory

| Role/function | Documented meaning | Observed exercise / limit |
|---|---|---|
| Human PI | Research direction, major decisions, L3 and irreversible consequences (R) | Direct AT10 authorization; Decision 0004 records PI's mirror requirement. Final phase exit remains PI's decision. |
| Astra | Architecture and exceptions (R) | E3/E5/E8 contain coordinator acceptance qualifications and anomaly adjudication. Not an independent reviewer of its own adjudication. |
| Sol | Scientific, visual, high-rigor claim/evidence QA (S) | Current adapter and mandatory mirror exist; no scientific/visual pilot qualification is demonstrated by the engineering records inspected. |
| Workers | Bounded execution and assigned artifacts (R/H) | E3 names fresh-loop-worker and its write set. E7 demonstrates code/test work, but its receipt alone does not prove a separate maintainer's identity. |
| Verifiers / DeepSeek verification function | Independent report ownership; Flash for metadata/test consistency, Pro for complex text; qualified multimodal route for visuals (R/V) | E7 DSH review ran separately, completed with zero tools and PASS at 0.72; acceptance remained FAIL. This is an exercised function, not a deployed department or current process claim. |
| Scout/Luna, Research/Evidence, Pro, Flash | Research collection/evidence, text writing, routine execution roles (PROJECT) | Defined capability allocations; this audit does not test their current availability or scientific quality. Pro is text-only. |
| Themis | **No current project-owned definition found** | Bounded text search of scoped project documents/JSON and hub briefs/specs/decisions/handoffs found no role definition. The AT10 candidate name is not appointment or deployment evidence. External conversational intent remains unknown. |
| Argus | **No current project-owned definition found** | Same search boundary. Existing meaning outside these sources remains unknown; not renamed, repurposed or assigned QC. |

No additional currently defined standing code-health custodian was located within those sources. This is a bounded documentation finding, not proof that no such role exists anywhere.

## Function / ownership matrix

“Gap” means the bounded finding in B, not automatic authorization for work.

| Function | Current owner | Documented source | Observed workflow evidence | State ownership | Gap? | Consequence | Escalation destination |
|---|---|---|---|---|---|---|---|
| Architecture / planning | Astra under PI direction | R/M | E3 packet, E8 design | Architecture owner: decisions; task owner: packet | Covered | Planning is not implementation authority | PI for L3/direction |
| Task authorization | PI scope; task owner bounds delegated work | R/H | E3 assigned owner, bounds and stop; direct AT10 brief | Decision owner and packet owner | Covered; historical packets cannot be blindly replayed | Wrong-root or stale scope possible | Astra; PI if scope changes |
| Execution | Assigned worker | R/H | E3 execution evidence; E5 blocked attempt; E7 local work | Worker artifacts, collector evidence | Covered | A blocked attempt is not successful execution | L1 worker; L2 exception |
| Deterministic verification | Assigned verifier/worker runs bounded checks; validator applies declared contract | R/V/H | E7 test receipt exit 0, nine groups / 45 records retained | Assigned report owner; task owner records disposition | No independent tester guaranteed by a test receipt | Self-tests cannot certify their own correctness | Verifier; Astra if consequential |
| Model review | Independent verifier via suitable model/harness | R/V | E7 DSH receipt and rejected review gate; E3 scoped evidence review | Verifier report; task owner disposition | Independent review covered; availability not current-tested | Review ≠ execution or machine acquisition | Task owner; qualified alternate only within authorization |
| Work-result acceptance | Task/subject owner; Astra handles architectural exceptions | V/H/M | E3 PROVEN qualified in AT04; E5 C2 qualified; E7 withheld | Owner decision + checkpoint | May coincide with planning/execution coordination | Self-review concentration, not absence of a gate | Astra exceptions; PI L3 |
| Verification-state maintenance | Verifier owns report; **current task owner** owns checkpoint; subject owner + verifier own promoted knowledge | R/M | E7 terminal, E8 preserved FAIL, current C | Clear per-artifact owners; no separate continuing custodian named | Candidate A: independent end-to-end custody not demonstrated | Astra may repeatedly reconcile reports itself | Task owner; consequential disagreement to Astra/PI |
| Code QC | Workers for tests, verifiers for independent reports; Sol high-rigor QA when assigned | R/V/S | E7 regression + model review, E3 gate omissions identified later | Packet reports / incidents | Candidate B: continuing code-health responsibility not assigned | Episodic QC exists; findings may depend on coordinator memory | Packet owner; architecture issue to Astra |
| Defect classification | Worker/verifier findings; Astra consequential adjudication | V/S | E5 F5/F6 vs F4; E8 limits vs defects | Task/service incident owner; separate adjudication artifact | Covered; no universal taxonomy engine implied | Reviewer's suspicion can be overpromoted | L1/L2; Astra disputed consequential finding |
| Bounded code repair | L0 safe repair within packet; L1 original worker | R/V | E7 additive local module; failed adoption retained | Assigned worker's write set; task owner adoption | Mechanism covered; durable QC owner gap remains | Repair execution does not authorize integration | Task owner; Astra/PI for contract/policy change |
| Architecture-level repair proposal | Astra; others may submit located findings | R/M | E8 proposes evidence first, no redesign | Decision owner, proposed artifact | Covered | Observation alone must not redesign Foundation | PI where consequential |
| Anomaly handling | Verifier records; owner dispositions; Sol/Astra for assigned high-rigor/consequential issues | V/S/H | E8 exact anomaly dispositions; original gate not cleared | Raw report verifier; disposition task owner | Stop rule partly ambiguous | Review of review may generate unbounded work | Astra only consequential exception |
| Exception routing | Task/service owner creates package; Astra adjudicates; PI L3 | V/M | E5 exception judgment, E8 stop | Incident/package owner; decision owner | Protocol covered; end-to-end PI escalation not live-tested here | Exhausted retries must not become PI work dump | L2 queue; PI only L3 |
| Checkpoint / handoff | Current task owner, exclusive writer; tool owns generated projections | M/H/C | Current successful recovery; mandatory Sol mirror agreement | LATEST + immutable snapshot; two mirrors | Covered at current root; stale-copy limitation | Wrong copy can mislead fresh discovery | Stop dependent writes, resolve root / stale owner |
| Scientific / visual QA | Sol / qualified multimodal reviewer; PI final scientific decisions | R/PROJECT/S | Role documented; engineering pilot does not prove science | Assigned reviewer report; subject owner + verifier knowledge | Qualification for a future task not established | Unreviewed scientific assertions must remain drafts | Sol, then PI consequential science |
| PI decision escalation | Astra forwards consequential decision; PI decides | R/V | AT10 requested decision preparation; Decision 0004 explicit PI instruction | Decision owner | Covered protocol; no blanket autonomous authority | Recommendations must not become authorization | Human PI |

## Independence, repair authority and work creation

| Actor | Can independently check preceding actor? | Can create/execute repair work? | Bound and persistent responsibility |
|---|---|---|---|
| Worker | May self-check; not independent acceptance of its own work | Only assigned scope and authorized L0/L1 | Own artifacts; cannot expand scope or clear held review |
| Deterministic validator | Checks declared inputs/contracts, not itself or all runtime facts | No intrinsic task-authorizing authority | Results owned by named report/task owner |
| Independent model verifier | Yes for supplied evidence and suitable capabilities; not independently acquired facts | Can report/propose; no implicit code-write or new-task authority | Own immutable report, not sole adoption authority |
| Sol | Independent of worker when separately assigned; not independent of Sol's own execution | Can propose located remediation; execution requires packet authority | Own review; no implicit standing code maintenance |
| Task owner | Accepts gate-bound results; may also be coordinator, so independence is conditional | Routes authorized L0/L1; queues L2 | Own checkpoint and disposition; must not treat every unknown as work |
| Astra | Adjudicates exceptions; not independent certification of own adjudication | Authorized architectural decisions/proposals; no scope expansion by inference | Architecture/exception decisions; PI when L3 |
| Human PI | Final decision authority, not routine verification labor | Can authorize new direction/scope | Own decisions, not execution queue |

Today V/H route FAIL/UNCERTAIN back to worker; AGENTS prohibits reassurance reruns and proposals becoming rules. They do not explicitly answer every “nonblocking uncertainty versus additional engineering” case. E5→E8 shows repeated, separately authorized attention to one failure chain; it does **not** establish unauthorized autonomous recursion. B/C propose the smallest explicit stop distinction.
