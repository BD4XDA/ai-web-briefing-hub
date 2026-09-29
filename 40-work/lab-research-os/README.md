# Lab Research OS

This directory is the canonical, recoverable coordination layer for the Lab Research OS project.

## Resume from chat mode

Read these files in order:

1. [`AGENTS.md`](AGENTS.md) — stable operating rules and safety boundaries.
2. [`PROJECT.md`](PROJECT.md) — project identity, scope, owners, and success criteria.
3. [`CHECKPOINT.md`](CHECKPOINT.md) — current authoritative state, risks, and next actions.

When the assigned model is Sol, continue with [`SOL-AGENT.md`](SOL-AGENT.md) for the Sol-specific project map, construction workflow, evidence gates, reporting contract, and the required generated mirror of the latest Foundation checkpoint.

Current GPT task division and reasoning-effort defaults are centralized in [`config/model-routing.json`](config/model-routing.json); validate changes with `python tools/model_routing.py validate`. DeepSeek routing remains external and unchanged.

The first approved production/shadow workload is the existing Daily Paper conversation and its single heartbeat. Its trigger, resource, evidence and reporting contract is [`protocols/RESEARCH-AUTOMATION.md`](protocols/RESEARCH-AUTOMATION.md); current adoption state and proposed non-daily workloads are under [`artifacts/daily-paper/`](artifacts/daily-paper/). Configured behavior is not considered live-qualified until a real run supplies evidence.

Do not infer current status from an older artifact or handoff. `CHECKPOINT.md` is rendered from the committed Foundation checkpoint, and `checkpoints/LATEST.json` identifies that checkpoint. When local tools are available, `python tools/foundation.py show` is the authoritative resume command.

Historical evidence and handoffs are retained under `artifacts/`; task packets are under `packets/`. A completed packet means that bounded stage stopped and was recorded—it does not automatically mean its proposed repair, pilot, or successor was accepted.

The repository must not contain credentials, raw authentication files, private research papers/profiles, or unrelated personal conversations. If GitHub access is unavailable in chat mode, ask the user to connect the repository or provide `AGENTS.md`, `PROJECT.md`, and `CHECKPOINT.md` directly.
