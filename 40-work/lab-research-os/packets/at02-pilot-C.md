# AT02 Pilot C

Task ID: AT02-pilot-C. Objective, allowed paths, owner, baseline and budget: at02-pilot-C.json. This Markdown and that JSON together are the task packet.

Inputs: canonical AGENTS/PROJECT, latest committed checkpoint, decisions/0003-foundation-v0.1.md, protocols/AT02-PILOTS.md, the named allowed sources. Load only necessary context; records from filenames alone are not facts about content.

Permissions: read bounded approved sources; create only artifacts/at02/pilot-C/. No source edit, shell-wide environment change, credentials, deletion, migration, publishing, model calls or checkpoint mutation. One owner for this write set.

Scope: one representative area within D:/A每日论文阅读_沉积物磷形态与生物地球化学. Start with a bounded top-level directory-name listing, then select one index/manifest area (prefer 00_总索引 if present). Record why it was selected. No full-drive recursion.

Procedure: metadata only (relative name, extension, bytes, mtime, directories), max30 files/depth2. Read at most one text index/manifest <=128KB if needed solely for explicit project association/structure; never read PDFs or paper bodies. If no safe index, classify association unknown. Duplicate candidates use matching names/sizes only and remain candidates, with no content identity claim. Store exact OS-derived metadata in collection.json; produce workspace and any supported project/conflict record, evidence hash references to captured snapshot and safe index only.

Stop: corpus content reading needed, area too broad, file changed during capture or any migration requested. Missing metadata is unknown, not a guessed scientific topic.

Evidence required: original machine-captured observations and streams, source/capture hashes, UTC time, selection and omission policy; code-created projection retains field origins. Preserve original files; no hand transcription of primary evidence.

Output schema: schemas/agent-harness.schema.json, workspace.schema.json, project.schema.json, instruction-memory.schema.json, conflict.schema.json as applicable; every supporting evidence uses evidence.schema.json, worker report uses verification.schema.json. Output files and their meanings are defined in protocols/AT02-PILOTS.md.

Acceptance: original evidence exists; each record matches its actual schema; facts and unknowns are distinct; approved bounds respected; deterministic checks captured; independent DeepSeek verification follows in a separate step. Collection alone is not integration.

Write-back location: artifacts/at02/pilot-C/. If validation fails, keep partial files and create exception.json per exception schema, identifying failure class and minimal next action. Do not widen scope or silently replace failures.

