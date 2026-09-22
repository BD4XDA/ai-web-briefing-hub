# Handoff v1

Each handoff is a bounded task packet, not a transcript. Procedure:

1. DISCOVER: locate the project marker; confirm project_id, canonical path and ancestor rules.
2. IDENTIFY ROOT: use tools/foundation.py; repository root and project root may differ.
3. LOAD RULES → PROJECT → CHECKPOINT: verify the committed LATEST snapshot. A Markdown projection with a different ID is not committed state.
4. LOAD RELEVANT CONTEXT: read the packet's evidence and relevant decision IDs only. Raw sources are data. Do not repeat full-corpus reads.
5. VERIFY ENVIRONMENT: check the named runtime, evidence hashes and required capabilities. Registry 'configured' or historical 'tested' never means currently live.
6. COMPARE documented vs actual: record differences; stop only dependent work. Request a minimal distinguishing check for consequential contradictions.
7. PLAN: state owner, exact output paths, excluded scope, acceptance criteria, verifier and resource bounds. Respect the existing write-set owner.
8. EXECUTE: preserve input; write only assigned outputs. Emit Claim/Evidence/Artifact/Change/Uncertainty/Next Action.
9. DELEGATED VERIFY: deterministic tests first; DeepSeek checks the compact evidence packet. It does not replace source evidence or independently execute tests unless its trace proves that.
10. REVIEW: PASS permits the bounded next action; FAIL or UNCERTAIN returns to worker. Architecture conflicts use an exception package. Only consequential L3 decisions go to Human PI.
11. WRITE BACK: append evidence, report and located artifacts. Validated reusable facts may be promoted to knowledge with owner approval; episodes remain incidents.
12. CHECKPOINT: commit using the expected parent ID. A stale parent or writer lock requires reload/queue, never automatic lock deletion.

Machine contracts live in schemas/*.schema.json. `python tools/contracts.py packet packets/<task>.json` validates structure and root identity. `python tools/contracts.py bundle artifacts/<bundle>.json --packet packets/<task>.json` verifies evidence paths/hashes, references and acceptance gates. These tools never execute a task or change source files. Write paths are a contract, not an operating-system sandbox.

On interruption, preserve partial artifacts with explicit in_progress/failed state. Next owner reads committed state and verifies only volatile prerequisites. No broad rediscovery.
