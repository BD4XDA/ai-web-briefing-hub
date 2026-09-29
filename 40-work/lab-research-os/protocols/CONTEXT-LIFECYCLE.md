# Context lifecycle and conversation rollover

## Decision rule

Conversation continuity is an execution cache, not project memory. Resume from project-owned state, not conversational history. Sol must initiate rollover when the expected marginal value of retaining the full conversation is lower than its marginal context cost or reliability risk. Do not wait for the context window to approach exhaustion.

Use signals already exposed by normal work; do not launch a separate model call to measure context. Rollover is justified by one strong signal or a persistent combination:

- repeated high cached-input cost that is disproportionate to the useful output;
- two or more compactions during the current work unit, or compaction that removes needed distinctions;
- most carried context is historical and the active task uses only a small verified subset;
- a focused continuation repeatedly pays for unrelated history;
- instruction collision, retrieval difficulty, latency or semantic drift is increasing because of conversation size;
- the same project state can now be restored more cheaply and reliably from checkpoint, decisions and evidence pointers.

Token count alone is not the rule. A long conversation with high current information value may remain active; a shorter conversation with low marginal value and high repeated cost should roll over earlier.

## Pre-rollover writeback gate

Before creating the successor conversation, the current owner must:

1. finish or safely pause the smallest active unit;
2. write verified state, incomplete work, consequential decisions, evidence references, blockers, uncertainties, continuation point and one exact next action into the canonical project state;
3. append a Foundation checkpoint and confirm `CHECKPOINT.md`, `checkpoints/LATEST.json` and the generated section of `SOL-AGENT.md` agree;
4. verify that a new conversation can resume by reading only `AGENTS.md`, `PROJECT.md`, the checkpoint and its bounded references;
5. preserve any old conversation that remains a unique evidence source.

No scientific judgment, evidence, incomplete work or Human PI decision may exist only in the old conversation when rollover occurs.

## Successor and retirement

Create one successor conversation with a compact bootstrap prompt containing the canonical root, checkpoint ID, workload identity, exact next action, model/effort ceiling and explicit instruction to avoid replaying completed work. Repoint an existing recurring task only after the successor can resolve the checkpoint. Do not create a duplicate schedule.

After successful handoff, mark the old conversation archived/historical; never delete it by default. Retrieve it only when the canonical evidence pointers are insufficient. Record the rollover as one workload event in passive cost telemetry, but do not count archival itself as scientific output.

If the writeback gate or successor verification fails, keep the old conversation active and checkpoint the rollover blocker. Rollover must reduce expected future cost without weakening scientific traceability.
