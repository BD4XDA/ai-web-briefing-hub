# Capability governance

`config/capability-registry.json` is the current need-driven register for Skills, MCPs, harnesses, profiles and scientific toolchains. Installation alone is not integration.

## Admission

A capability enters management only when it serves an identified research or control-plane workload. Record its tier, trigger, availability, qualification, evidence, fallback and update policy. Do not enumerate every installed package as a standing laboratory service.

- `core`: required by an active production/shadow workload or Lab Research OS continuity.
- `on-demand`: useful after a declared EVENT, MILESTONE, STATE or explicit request.
- `watch-only`: known asset that is blocked, legacy or not currently depended upon.
- `excluded`: intentionally outside laboratory use.

Installed, configured, live and qualified remain separate. A runtime-visible Skill/MCP is not qualified until a representative bounded task supplies evidence.

## Updates

Run a lightweight weekly update check and a focused check before first use after a material version change. The weekly check may inspect official release metadata, installed versions, deprecations and credential-free health signals. It must not automatically install, remove, enable or grant access.

Update only when the change is relevant. Preserve configuration first; use an isolated profile or environment for breaking/pre-release changes; run configuration composition and one bounded representative task; then update the registry and checkpoint. Report only meaningful changes, security/reliability risk, a blocked core capability or a Human PI decision.

No recursive verification: one deterministic check and one representative run are sufficient unless a concrete failure requires a smaller discriminating test.

## Scientific boundaries

Generated diagrams may explain a method or architecture but never replace an evidence-bearing source figure. Cloud connectors may not receive private papers, annotations or research data without explicit scope. Statistical Skills activate only when the relevant dataset/state trigger exists and must preserve code, parameters, environment and output provenance.

Validate with `python tools/capability_registry.py validate`; summarize with `python tools/capability_registry.py show`.
