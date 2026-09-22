# AT03 P3 — bounded pilot closure

Decision: evaluation closed; **no pilot candidate integrated**. Collection completion is not acceptance. Source state restored from committed 20260921T183240-2a5430059765, newer than planning baseline 183037. Later progress checkpoint 20260922T000722-8a87d4b9f624 preserves held results.

| Pilot | Actual collection/delivery state | Independent result | Coordinator disposition |
|---|---|---|---|
| Vela / A | Collection captured; delivery INVALID / REQUIRES_MINIMUM_REPAIR. 5 records, 5 evidence entries. Original missing evidence key repaired once without recollection; extra schema_version remains. | FAIL, 0.62; gate HELD. | Not accepted. Also stale 'latest checkpoint' claim and CLI lookup failure. Preserve raw/initial/corrected files. |
| Janus / B | Collection captured; delivery INVALID / REQUIRES_MINIMUM_REPAIR. 5 records, 17 evidence entries. | UNCERTAIN, 0.60; gate HELD. | Not accepted: 18-vs17 text/count and incorrect repository path. Prior worker context means fresh-owner resume is not proven. |
| Seshat / C | COMPLETED_COLLECTION: one index file in 00_总索引, bounded metadata/index only; 2 records, 2 evidence entries. | Initial UNCERTAIN0.65; one stage clarification PASS0.78, no anomalies, gate still HELD (<0.80). | Not accepted; no lowering threshold or further retry. Unknown project association and bounded coverage remain valid limitations. |

Machine observation, deterministic input validation and model evidence-package review are separate. DeepSeek reviewed supplied execution evidence; it did not independently acquire machine state. The C empty reports array was the expected pre-review state, not evidence of failed collection. Clarification corrected that interpretation without recollecting.

Minimal discriminating evidence confirmed repository root as C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub; A still includes schema_version; B policy says 18 while actual file list has 17. No Foundation file was changed. Task-specific verifier was preserved and corrected to reject unknown candidate keys before a paid call and support this single C clarification.

Primary evidence:
- ../at02/pilot-A/execution.json; candidate-bundle.initial.json; candidate-bundle-correction.json; exception.json
- ../at02/pilot-B/execution.json; observations.json; collection.json
- ../at02/pilot-C/execution.json; raw-capture.json; index-snapshot.md
- ../at02/verification/acceptance.json; review-response.json; review-parsed.json; discriminating-receipt.json
- ../at02/verification-C-clarification/acceptance.json; review-response.json; review-parsed.json

Next: classify observed failures, not hypothetical defects. One low-risk loop may use the already accepted frozen Foundation manifest; it must not promote these held pilot records. No broader census or repeat-until-green sequence is authorized.
