# AT02 bounded census pilot dispatch

Operational need: AT01 bundle code recognizes five inventory kinds but their production schemas did not exist; tests explicitly mocked project shape. Five local pilot schemas now complete the requested six record types when combined with Evidence Record. Frozen P1 contract code and existing schemas remain unchanged.

Each pilot has a machine task packet and a Markdown procedure; read both. Its expected_checkpoint is the planning baseline. Workers must load the latest committed snapshot and record any difference. The P2 dispatch checkpoint adds these packets, not a source-data change. Workers have no checkpoint write permission during collection; the coordinator serializes stage commits.

Worker output in its assigned artifacts/at02/pilot-X directory:
- collection.json: original program-captured observations, selection/omission reasons, timestamps, no manually reconstructed stdout.
- candidate-bundle.json: task_id, schema-valid records, evidence records, reports (empty until independent verification). Evidence paths are absolute and hash actual file bytes. Historical observations use immutable snapshot/capture files, not volatile LATEST/CHECKPOINT as lasting hash anchors.
- execution.json: exact command/exit/stdout/stderr/timing, collector source hash. A collector may capture OS/file observations directly in collection.json; identify that method honestly.
- observations.json: loaded/necessary/missing/excess context, context failure; actual requested model and harness (unknown allowed), task type, capability required, routing outcome/mismatch. No invented model identity.
- worker-report.json: claim, evidence IDs, method, result/confidence/anomaly, reviewer/model_reported/harness/observed_at per verification schema.

No model calls during collection. A separate DSH Flash invocation reviews machine-assembled original collection/evidence/records and deterministic validation output, without manual transcription. That reviewer inspects evidence; it does not claim to run the collector. Reports with missing evidence, low confidence or unresolved relevant anomalies remain unaccepted. Keep limitations separate from contradictions.

Unknown is valid. A configured template is not a live agent. Same filename/size only suggests a duplicate candidate. No content/topic inference from filenames. A bounded sample is never a drive-wide inventory.

Safety: skip symlinks/junctions and secret/auth/token/config contents unless a packet explicitly permits a safe field projection. No file writes outside assigned paths; no writes to source data. At most 30 sampled files, depth 2; stop on a larger needed scope and report the omitted portion. Sensitive file names may be listed as 'excluded sensitive item' without values/content.

On failure, retain raw output and an exception with F1..F10 candidate, minimal next check and consequence. No unauthorized cleanup/reinstall/migration. These tasks exercise existing contracts; they do not build a generic census engine.
