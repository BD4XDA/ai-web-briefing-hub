# AT02 Pilot A

Task ID: AT02-pilot-A. Objective, allowed paths, owner, baseline and budget: at02-pilot-A.json. This Markdown and that JSON together are the task packet.

Inputs: canonical AGENTS/PROJECT, latest committed checkpoint, decisions/0003-foundation-v0.1.md, protocols/AT02-PILOTS.md, the named allowed sources. Load only necessary context; records from filenames alone are not facts about content.

Permissions: read bounded approved sources; create only artifacts/at02/pilot-A/. No source edit, shell-wide environment change, credentials, deletion, migration, publishing, model calls or checkpoint mutation. One owner for this write set.

Scope: existing DSH router plugin, web package manifest, CLI package manifest and agent-team metadata; installed Claude/Codex version commands may be used. Sample at most 30 files; depth <=2. Do not infer running agents from stored team state.

Procedure: load canonical context; inspect only the named manifests and safe agent-team projections (names, models, permissions, MCP names, team state/task counts). Capture projection by code; never paste full agent_team or global settings/auth. Record installed CLI versions only if already resolvable; no install. Inspect at most two existing router source files for declared routes/tool boundaries. Existing reports may guide selection but cannot replace fresh observations. Existing source may mention skills/MCP; label configuration and unknown liveness. Produce agent-harness plus any instruction-memory/conflict records justified by evidence. No live API calls or service restarts.

Stop: cannot safely project a source, source changed during capture, scope would exceed limits, sensitive content found. Escalate only meaningful conflicting source-of-truth or unsafe capability routing; ordinary missing asset becomes unknown.

Evidence required: original machine-captured observations and streams, source/capture hashes, UTC time, selection and omission policy; code-created projection retains field origins. Preserve original files; no hand transcription of primary evidence.

Output schema: schemas/agent-harness.schema.json, workspace.schema.json, project.schema.json, instruction-memory.schema.json, conflict.schema.json as applicable; every supporting evidence uses evidence.schema.json, worker report uses verification.schema.json. Output files and their meanings are defined in protocols/AT02-PILOTS.md.

Acceptance: original evidence exists; each record matches its actual schema; facts and unknowns are distinct; approved bounds respected; deterministic checks captured; independent DeepSeek verification follows in a separate step. Collection alone is not integration.

Write-back location: artifacts/at02/pilot-A/. If validation fails, keep partial files and create exception.json per exception schema, identifying failure class and minimal next action. Do not widen scope or silently replace failures.

