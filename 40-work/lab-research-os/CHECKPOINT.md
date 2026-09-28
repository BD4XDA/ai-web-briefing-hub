# Lab Research OS · CHECKPOINT
Checkpoint ID: 20260928T132433-391786e56d73
Priority: P3 · Status: complete
Canonical committed pointer: checkpoints/LATEST.json. If IDs differ, use tools/foundation.py show; do not guess.

## Current Verified State

- Canonical repository root migrated to D:/20_代码项目/赛博课题组 and project root to D:/20_代码项目/赛博课题组/40-work/lab-research-os; active paths were updated while historical records were preserved.
- Current GPT routing is centralized in config/model-routing.json: Luna low, Sol medium and Astra medium by default, with bounded high/xhigh escalation rules.
- DeepSeek routing and external DSH/provider configuration remain unchanged.
- Installed DSH 0.1.1-rc.2 is structurally compatible with the project through AGENTS/CLAUDE instruction discovery plus workspace filesystem and command tools; no upgraded or paid-model end-to-end qualification was performed.
- The public GitHub repository is visible, but a standalone public release is held pending licensing, security/contribution documents, path sanitization, historical-artifact curation and clean-room installation tests.
- AT11 remains PACKET_READY and unexecuted; its future gpt-6-sol scientific review now requests reasoning effort high.

## Completed

- Adopted the D-drive path migration through Decision 0010 and rebound current AT11 project/source locators without running the science task.
- Reviewed official OpenAI GPT-6 model, reasoning, pricing and changelog guidance and recorded primary-source references.
- Added the model-routing manifest, JSON Schema, validator, four new tests and routing protocol; all 24 project unit tests pass.
- Inspected installed and upstream DSH versions without mutation and documented structural compatibility plus upgrade risks.
- Completed a static public-release audit and comparable-project analysis; corrected the root README public/private mismatch.

## Decisions

- Use the migrated repository and corpus roots for current work; preserve old paths only as historical observations.
- Use the lightest route and reasoning effort that meets a predeclared quality gate; do not default to xhigh or max.
- Keep DeepSeek unchanged and outside the GPT routing manifest.
- Do not upgrade the working DSH profile in place; qualify a pinned isolated profile before adoption.
- A public release must be a sanitized clean export or standalone repository, not a raw publication of internal history.

## Open Questions

- Human PI must choose a license and authorize a standalone public-release construction/publish task.
- A future separately authorized DSH qualification should decide whether to target npm latest 0.1.5-rc.3 or the 0.1.7 prerelease line after plugin compatibility review.
- Representative quality/cost evaluations are still required before changing default efforts or adopting a future GPT model generation.

## Known Risks

- Static DSH compatibility does not prove provider authentication, model identity, web UI health or live end-to-end execution.
- The already-public repository contains machine-specific paths and historical execution context even though the high-confidence static scan found no token/private-key signature.
- Official product capabilities, pricing and release status can change; the routing policy records its review date and must be re-evaluated before a future migration.

## In Progress


## Next Actions

- Use config/model-routing.json for new GPT assignments and validate any change with python tools/model_routing.py validate.
- If the Human PI authorizes public packaging, build a clean sanitized distribution with license/security/contribution files, synthetic examples and CI; do not copy raw artifact history.
- If the Human PI authorizes DSH upgrade qualification, use an isolated pinned profile and preserve the current working profile. No automatic AT11 science, AT09 work or successor is authorized.

## Evidence References

- ../../00-inbox/2026-09-27-gpt6-routing-dsh-public-release.md
- ../../10-briefs/2026-09-27-gpt6-routing-dsh-public-release.md
- ../../20-research/2026-09-27-gpt6-dsh-comparables.md
- ../../50-decisions/2026-09-27-gpt6-cost-routing.md
- decisions/0009-gpt6-cost-routing-and-portability.md
- config/model-routing.json
- schemas/model-routing.schema.json
- tools/model_routing.py
- tests/test_model_routing.py
- protocols/MODEL-ROUTING.md
- artifacts/GPT6-DSH-PUBLIC-RELEASE-ASSESSMENT.md
- decisions/0010-canonical-root-migration.md
- packets/at11-first-supervised-research.json
- SOL-AGENT.md
