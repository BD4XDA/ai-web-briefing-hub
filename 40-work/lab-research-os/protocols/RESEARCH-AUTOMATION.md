# Research automation · production/shadow workload contract

## Operating rule

Run because something changed, not because computation is available. Reporting frequency does not determine workload frequency. `Human PI Daily Research Brief` is daily; expensive scientific recomputation is not.

## Trigger classes

- **TIME** — only when the external world changes often enough to justify cadence. Current approved examples: Daily Literature Radar and a proposed Weekly Literature Synthesis.
- **EVENT** — new paper, decision, dataset, experiment batch, analysis output, figure or checkpoint.
- **MILESTONE** — research question/design frozen, sampling/experiment/data/analysis/figure milestones, or manuscript drafting start.
- **STATE** — a declared gate such as `DATA_READY`, `QAQC_PASS`, `EVIDENCE_SUFFICIENT`, `FIGURE_READY` or `MANUSCRIPT_READY`.

Every workload records its trigger and observed input change. Absence of a trigger means no run. A daily report may read the latest verified state without recomputing it.

## Resource routing

1. Deterministic metadata, deduplication, file handling, formatting and batch extraction use local tools or the cheapest qualified worker.
2. Discovery, frontier scouting, screening and relevance ranking use Luna/low by default; medium is allowed only for coordinated multi-source work.
3. Sol/medium handles scientific meaning, full-text interpretation, evidence–claim and inference boundaries, contradictions and final scientific QA. Sol/high is reserved for consequential independent review.
4. Astra is not a literature worker. It is reserved for cross-paper architecture, research gap, novelty/hypothesis/manuscript architecture and unresolved structural conflicts.
5. A delegated task must set model class and effort explicitly. Never inherit a parent's highest effort. Escalate a decision, not unfinished mechanical work.

## Evidence boundary

Daily discovery writes evidence-ready records but does not promote knowledge. Keep these labels distinct:

`Observation | Author claim | Agent interpretation | Hypothesis | Candidate claim | Supported claim | Contradicted claim | Unknown`

Minimum record: source identifier/URL, full-text access status, exact artifact pointer, statement label, verification state, observed trigger, requested/actual model class when available, and unresolved uncertainty. A report points to evidence; it is not evidence itself.

Promotion remains:

`Discovery → Extraction → Evidence → Verification → Candidate Knowledge → Validated Knowledge`

## Resume and failure

Before starting a scheduled run, inspect the conversation's latest user instruction and last failed/incomplete turn. Reuse completed artifacts and continue from the smallest unfinished unit. Never start a duplicate issue or overwrite a partial repair. On quota, access or tool failure, preserve the partial state and report the exact continuation point.

## Production/shadow observations

Collect only observations naturally produced by real research: route chosen, handoff loss, source traceability, verification performed, checkpoint/resume success, promotion boundary, local recovery, expensive-model anomalies, Human PI attention load, scientific quality and repeated-QC drift. Do not build synthetic work merely to create a PASS.

One verification pass is normal. Further review requires a named anomaly or changed input. `QC → QC the QC` is prohibited.
