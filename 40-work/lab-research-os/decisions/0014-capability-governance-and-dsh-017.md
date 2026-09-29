# Decision 0014 — Need-driven capability governance and DSH 0.1.7

Date: 2026-09-29. Owner: Human PI. Implementer: Sol/Codex maintenance turn.

The laboratory will manage only capabilities tied to actual research or continuity workloads. `config/capability-registry.json` is adopted as the machine-readable register; `protocols/CAPABILITY-GOVERNANCE.md` governs admission, qualification, fallback and updates. Installation or runtime visibility alone is not integration.

A weekly update check is authorized for official release metadata and credential-free health signals. It reports meaningful changes but does not automatically install, remove, enable, grant access or alter scientific workflow. Material updates remain evidence-driven and reversible.

The local DSH core is upgraded to npm `latest` `0.1.7-rc.2`. Clean `lab-research` and `lab-headless` profiles are the qualified routes. The legacy Web profile and custom Sol/Luna router are retained but held outside clean production use until their plugin APIs and obsolete model routes are migrated. This does not change the externally managed DeepSeek model policy in `config/model-routing.json`.
