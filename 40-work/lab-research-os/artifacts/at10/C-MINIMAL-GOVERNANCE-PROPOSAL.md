# AT10 C — Minimal governance proposal (NOT ADOPTED)

Basis: [A](A-RESPONSIBILITY-MATRIX.md), [B](B-GAP-CLASSIFICATION.md). This document does not amend AGENTS, protocols, schemas, Foundation, role names or authorization.

**What is the smallest change that solves the demonstrated problem?**

Clarify the existing task-owner/verifier contract: every bounded packet names its executor, independent reviewer, acceptance/state owner and, only when code changes, QC finding owner. Add one disposition-and-stop sentence to the existing review procedure. Reuse the current packet/report/checkpoint locations. No new ledger, permanent agent, daemon or department is needed.

## Proposed responsibility clarification

1. **Verification:** assigned verifier owns the independent report and a concise disposition recommendation; task owner owns canonical verification state and acceptance under the declared gate. They need not be Astra. The worker cannot be the only accepter of its own result. When Astra authored/coordinated the work, ordinary result review should be assigned to an existing qualified reviewer; Astra handles only consequential exceptions. “Independent” means distinct execution/review responsibility with suitable evidence and capability, not merely a renamed model alias. If a suitable reviewer cannot run, hold the relevant result; do not silently call coordinator inspection independent review.
2. **Code QC:** for each authorized code-changing task, designate an existing worker as bounded maintainer and a distinct verifier as QC report owner. The task owner retains a short finding/disposition entry in existing artifacts/checkpoint until acceptance, explicit limitation or rejection. Include affected code/claim, evidence, classification, consequence, authorization bound and disposition. No standing code repair authority is created. Sol may review high-rigor/scientific/visual aspects when assigned; this is not a default Sol or Argus maintenance appointment.
3. **Continuity:** existing task owner remains the single checkpoint writer. Reviewer writes report; worker writes artifacts; task owner integrates only permitted outcomes. A report can be preserved as FAIL/UNCERTAIN without being adopted. Carry unresolved consequential status forward by reference. Checkpoint commitment records state, not proof that every recorded result passed.
4. **Uncertainty budget:** routine owner decides whether an issue affects the authorized claim and is inside the remaining packet bounds. Astra decides consequential architecture/authority ambiguities; PI decides L3 or phase/scope changes. A reviewer identifies consequence and evidence, not an unbounded new work queue.

Themis and Argus are deliberately not assigned: their current project-owned meanings are not established. If the PI later supplies an existing definition, reconcile it before proposing any appointment. Candidate A/B do not justify new permanent roles on present evidence.

## Proposed recursive-review breaker

| Outcome | Required disposition | Who decides / stop condition |
|---|---|---|
| ACCEPTED RESULT within its original scope | Continue only the authorized next action; no reassurance rereview | Task owner retains accepted evidence; reopen only on changed relevant inputs or a concrete consequential contradiction |
| PROVEN LOCAL DEFECT | State exact failing claim and smallest local repair; L0/L1 execution only inside existing authorization/write set/budget | Existing worker/maintainer repairs if authorized; otherwise proposal only. One bounded return and the packet's permitted re-review, never an open-ended green-seeking loop |
| BLOCKING + CONSEQUENTIAL UNCERTAINTY | Hold affected acceptance; bounded Exception Package | Task owner supplies Problem/Evidence/Conflicting Evidence/Attempts/Confidence/Possible Explanations/Consequence/Recommended Next Check; Astra adjudicates, PI only L3 |
| NON-BLOCKING UNCERTAINTY | Record Known Limitation or non-executing backlog item | Task owner states affected claim and why current action is safe without resolving it; no task/review automatically created |
| ARCHITECTURE / POLICY / FOUNDATION CHANGE | Proposal and appropriate authority decision before implementation | Astra judges architecture; PI where direction/risk/authorization demands; old contracts remain until authorized change |
| NEW IDEA / POSSIBLE IMPROVEMENT | IDEA only | No implementation or review round solely because it sounds useful |

UNCERTAIN ≠ automatic next task. Observation ≠ defect. Defect ≠ architecture redesign. Started ≠ must finish.

The breaker does not erase a report's anomaly field, lower confidence thresholds or retroactively accept AT07. An anomaly can block its own gate while remaining nonblocking for a different authorized supervised workflow. Reviewers must identify that scope explicitly.

## Adoption and scope

These are proposed ownership/protocol clarifications for PI consideration, **not implemented**. Before a future supervised task, ordinary packet scoping already requires owner, verifier, writes and acceptance conditions (HANDOFF step 7); assigning those fields is sufficient to avoid waiting for a new governance subsystem. No additional Foundation work is a prerequisite on current evidence.

No new automatic retry allowance is granted here. If a packet permits no retry, none occurs. Re-review of a specifically authorized correction is not recursive global assurance; it checks the changed claim and stops at its declared gate. Exhausted retries do not automatically become PI work or justify a new task.
