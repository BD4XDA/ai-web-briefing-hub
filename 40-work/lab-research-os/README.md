# Lab Research OS

This directory is the canonical, recoverable coordination layer for the Lab Research OS project.

## Resume from chat mode

Read these files in order:

1. [`AGENTS.md`](AGENTS.md) — stable operating rules and safety boundaries.
2. [`PROJECT.md`](PROJECT.md) — project identity, scope, owners, and success criteria.
3. [`CHECKPOINT.md`](CHECKPOINT.md) — current authoritative state, risks, and next actions.

When the assigned model is Sol, continue with [`SOL-AGENT.md`](SOL-AGENT.md) for the Sol-specific project map, construction workflow, evidence gates, reporting contract, and the required generated mirror of the latest Foundation checkpoint.

Current GPT task division and reasoning-effort defaults are centralized in [`config/model-routing.json`](config/model-routing.json); validate changes with `python tools/model_routing.py validate`. DeepSeek routing remains external and unchanged.

Managed Skills, MCPs, harnesses and scientific toolchains are listed in [`config/capability-registry.json`](config/capability-registry.json). Follow [`protocols/CAPABILITY-GOVERNANCE.md`](protocols/CAPABILITY-GOVERNANCE.md); validate with `python tools/capability_registry.py validate`. Installed does not mean integrated, and updates are reviewed rather than automatically applied.

The first approved production/shadow workload is the existing Daily Paper conversation and its single heartbeat. Its trigger, resource, evidence and reporting contract is [`protocols/RESEARCH-AUTOMATION.md`](protocols/RESEARCH-AUTOMATION.md); current adoption state and proposed non-daily workloads are under [`artifacts/daily-paper/`](artifacts/daily-paper/). Configured behavior is not considered live-qualified until a real run supplies evidence.

Do not infer current status from an older artifact or handoff. `CHECKPOINT.md` is rendered from the committed Foundation checkpoint, and `checkpoints/LATEST.json` identifies that checkpoint. When local tools are available, `python tools/foundation.py show` is the authoritative resume command.

Historical evidence and handoffs are retained under `artifacts/`; task packets are under `packets/`. A completed packet means that bounded stage stopped and was recorded—it does not automatically mean its proposed repair, pilot, or successor was accepted.

The repository must not contain credentials, raw authentication files, private research papers/profiles, or unrelated personal conversations. If GitHub access is unavailable in chat mode, ask the user to connect the repository or provide `AGENTS.md`, `PROJECT.md`, and `CHECKPOINT.md` directly.

Resource use is governed by `protocols/RESOURCE-GOVERNANCE.md` and `protocols/COST-TELEMETRY.md`. A logical target receives at most three total retrieval attempts by default, while run-level model route, effort, reported/estimated token use, retries, useful output and benefit/cost ratio are appended silently to the ignored local ledger. The Human PI Daily Research Brief reads a deterministic daily aggregate with `python tools/cost_telemetry.py show --date YYYY-MM-DD`; it does not launch extra model work merely to calculate cost.
