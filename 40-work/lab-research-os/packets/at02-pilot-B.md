# AT02 Pilot B

Task ID: AT02-pilot-B. Objective, allowed paths, owner, baseline and budget: at02-pilot-B.json. This Markdown and that JSON together are the task packet.

Inputs: canonical AGENTS/PROJECT, latest committed checkpoint, decisions/0003-foundation-v0.1.md, protocols/AT02-PILOTS.md, the named allowed sources. Load only necessary context; records from filenames alone are not facts about content.

Permissions: read bounded approved sources; create only artifacts/at02/pilot-B/. No source edit, shell-wide environment change, credentials, deletion, migration, publishing, model calls or checkpoint mutation. One owner for this write set.

Scope: this actual canonical project within shared hub. At most 30 files; do not scan unrelated repository areas.

Procedure: discover root via marker from a child directory; load AGENTS, PROJECT, committed checkpoint through foundation.current, relevant AT02 brief/decision and packet. Record plan-baseline/current differences. Use immutable checkpoint snapshot as evidence; do not hash mutable pointer/projection as lasting evidence. Collect bounded project and instruction-memory records. Verify frozen manifest hashes using code; do not rerun accepted 8/10 tests. Exercise real schemas once: candidate record schema validation, valid bundle acceptance with a temporary honest worker verification report; negative unknown-kind/duplicate-ID/reference errors if needed to verify actual new schema path. Label temporary verification report as fixture, never an independent model review. Capture all raw output and assertions automatically. No changes to tools/schemas/protocols.

Stop: committed integrity failure, frozen file drift, ambiguous root, stale write attempt or unmet scope. Record F1/F2/F5/F8 candidate with minimal check rather than repairing implementation.

Evidence required: original machine-captured observations and streams, source/capture hashes, UTC time, selection and omission policy; code-created projection retains field origins. Preserve original files; no hand transcription of primary evidence.

Output schema: schemas/agent-harness.schema.json, workspace.schema.json, project.schema.json, instruction-memory.schema.json, conflict.schema.json as applicable; every supporting evidence uses evidence.schema.json, worker report uses verification.schema.json. Output files and their meanings are defined in protocols/AT02-PILOTS.md.

Acceptance: original evidence exists; each record matches its actual schema; facts and unknowns are distinct; approved bounds respected; deterministic checks captured; independent DeepSeek verification follows in a separate step. Collection alone is not integration.

Write-back location: artifacts/at02/pilot-B/. If validation fails, keep partial files and create exception.json per exception schema, identifying failure class and minimal next action. Do not widen scope or silently replace failures.

