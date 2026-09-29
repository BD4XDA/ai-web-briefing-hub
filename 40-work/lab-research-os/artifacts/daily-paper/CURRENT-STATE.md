# Daily Paper integration · recovered state

Observed 2026-09-29.

## Existing workflow

- The existing Work conversation is titled `每日论文` and is already attached to the same saved project as Lab Research OS.
- One active heartbeat (`每日沉积物磷论文整理`) targets that conversation at 08:00 Asia/Shanghai. No second automation is required.
- The private Skill and archive implement one Chinese core plus two SCI full-text papers, optional supervisor-paper add-on, personal/supervisor notes, legal-access rules, deduplication, rendering QA and index maintenance.
- The current master index reaches issue 021 dated 2026-09-26. This establishes archive existence, not scientific validation of every historical note.

## Interrupted work

The latest explicit Daily Paper task paused new daily selection and requested historical repair: normalize 73 personal notes, add appropriate original-paper figures to personal and supervisor versions, and add non-invented process/reasoning diagrams. The parent and three bounded child ranges failed because the account usage window was exhausted. Existing artifacts remain under the 2026-09-28 image/flowchart verification workspace. Six notes were reported as lacking complete full text. This repair is independent of the automation upgrade and remains resumable from those artifacts; it must not restart or be silently treated as completed.

## Status table

| Capability | Status | Basis |
|---|---|---|
| Existing archive and issue workflow | IMPLEMENTED & OBSERVED | Master index and issue 021 folders |
| Existing heartbeat schedule | IMPLEMENTED & LIVE configuration | Active automation record; last scheduled turn failed on quota |
| Private Skill after root migration | IMPLEMENTED & VERIFIED locally | New target exists and system Skill junction is readable after repair |
| Daily Paper → Lab OS prompt binding | IMPLEMENTED BUT UNVERIFIED | Automation prompt updated; no post-update heartbeat observed yet |
| Cost-aware delegation | CONFIGURED, LIVE UNKNOWN | Contract now forbids inherited high effort; next run must provide evidence |
| Evidence-ready daily records | PARTIAL | Existing notes/index exist; new statement labels and run observations await a live run |
| Human PI Daily Research Brief | IMPLEMENTED BUT UNVERIFIED | Template and recurring prompt exist; first live brief pending |
| Weekly/event/milestone/state readiness | PROPOSED, NOT DEPLOYED | Workload classification only |
| Historical 73-note repair | PARTIAL / PAUSED | Quota-failed parent/children; preserved continuation artifacts |
| Persistent automation-level model pinning | UNKNOWN | Heartbeat configuration exposes schedule/thread/prompt; no model/effort field was observed |
| Future-note source visuals and workflow diagrams | IMPLEMENTED BUT UNVERIFIED live | Private Skill, output contract, recurring prompt and opt-in validator updated; no complete new issue has yet passed the visual contract |

## Minimum continuation points

1. Next heartbeat: restore the latest user instruction and incomplete repair state before deciding whether a new issue may start; always generate the brief from actual work only.
2. First upgraded run: observe requested/actual routes, source/evidence pointers, Daily Brief output and quota behavior. Do not synthesize a test run merely for validation.
3. Historical repair: resume the three preserved ranges only when explicitly continued in the Daily Paper conversation; finish one bounded range before opening another review loop.
