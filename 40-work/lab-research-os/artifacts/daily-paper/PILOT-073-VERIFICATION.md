# Daily Paper Event pilot 073 · independent verification

Observed 2026-09-29 after the real historical-repair workload completed.

## Claim 1 · note 073 visual augmentation

- **Evidence:** the published personal DOCX/PDF, published supervisor DOCX, the same-paper source PDF, the preserved recipe and run record in the private corpus.
- **Verification method:** direct structural inspection; source pages 2–4 compared with the inserted Fig. 1 and eight-node workflow; Word export plus Poppler rasterization; every rendered page inspected.
- **Result:** PASS after the path repair described below.
- **Confidence:** 0.97.
- **Finding:** both note versions contain a legible same-paper figure and a method workflow supported by the source methods. The interpretation records the different pH axes, COD/NH4-N boundary, low-salinity bottle scope and absence of performed precipitation recovery.
- **Uncertainty:** this is a historical repair using legacy section labels. It is not a complete new issue and does not exercise the future `--require-visuals` gate.

## Claim 2 · published-path usability

- **Evidence:** direct Word open attempts at the published path and the rendered final output.
- **Verification method:** the original 309-character supervisor path failed direct Word automation; the same unchanged DOCX opened from a short path. The published filename was shortened, reducing its full path to 110 characters. A second issue-021 supervisor path exposed by the regression gate was also shortened. Both repaired final paths opened directly and rendered 6 and 4 clean pages respectively.
- **Result:** PASS after L0 repair.
- **Confidence:** 0.99.
- **Anomaly:** the previous workflow could validate a staged copy without proving that the published path itself was usable.
- **Adoption effect:** new issues must pass `--require-portable-paths`; final-path direct open is part of document QA. Existing historical notes are not retroactively failed.

## Claim 3 · resource and recovery behavior

- **Evidence:** the actual Event-run report and observed tool route.
- **Verification method:** inspected the real run rather than constructing a synthetic issue.
- **Result:** PASS for this bounded Event workload.
- **Confidence:** 0.95.
- **Finding:** the run resumed note 073 instead of restarting, used local document/PDF tooling, made no Astra call, used no subagent and produced the ten-section Daily Research Brief. A filename error was recovered locally without reopening the whole workload.
- **Uncertainty:** scheduled heartbeat routing and a complete new issue remain unverified.

## Historical backlog observation

A read-only scan found 34 remaining historical supervisor DOCX files above the new portable-path budget after the two issue-021 repairs. This is a bounded Event backlog, not a Daily workload. Bulk migration requires its own rename map, reference update and direct-open verification; it is not silently performed by this pilot.

No new digest was calculated. The claims concern semantic content, rendered behavior and direct-open usability rather than byte identity.
