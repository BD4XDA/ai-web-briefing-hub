# AT08 F4 recoverability and minimum future observability — DESIGN ONLY

## Historical finding
**HISTORICAL_F4_PROVENANCE = NOT CURRENTLY RECOVERABLE.**
Scope: the original AT05 thread 01a0c6aa-340f-7703-8fe8-4256283b700d and recorded execution window 2026-09-22T01:10:38–01:11:07Z, within the already inspected authorized local surfaces.

Evidence: AT05 worker.stderr preserves only a shell-wrapped exec_command rejection; worker.stdout has no normalized policy request/decision event. AT06 diagnostic-evidence.json and AT07 F4-provenance.json preserve exact, empty read-only thread/time-window policy queries. AT05 launch-input.json declares --ephemeral, but that is not proof that every possible log has vanished. The original matched rule, effective policy source, normalization and explanation are absent from these artifacts. No newly identified archive/export points to them.

Therefore no repeated query of the same sources is warranted. We do not claim permanent global UNRECOVERABLE, search unrelated sessions, read credentials, or substitute current config. Reopen historical retrieval only if a concrete new authorized source or original-process audit export appears.

## Minimal future record at the actual execution boundary
Required instrumentation is a producer-side observation of the existing decision path, not another classifier and not a policy override. Hook/API availability in this installed harness is NOT established. The following is a contract/design, not an implemented or supported feature claim.

1. **Request capture before evaluation**: event_id/request_id, actual normalized tool name and arguments, resolved executable and argv, cwd and authorized root references, actual sandbox/approval mode and requested overrides, plus normalization version/source identifier. Preserve original→normalized mapping for the same request. Do not infer normalized arguments from a human-readable exception or reconstruct them afterward.
2. **Effective policy provenance**: source class (built-in/managed/user/project), ordered precedence of applicable policy layers, effective non-secret decision inputs, policy/ruleset version and SHA-256 of the exact relevant non-secret policy bytes. Opaque host-provided policy digests may be recorded as such. A current config snapshot is not a substitute for the evaluator's effective policy snapshot.
3. **Decision**: rule_id or stable evaluation-path id, allow/deny/approval-required/unknown result, matched condition, evaluator reason code/explanation and evaluator version. If the evaluator exposes no rule id, record that absence; do not invent an id from the command string.
4. **Time and identity**: capture UTC timestamps at request/decision/launch-or-denial/exit; monotonic ordering where available; parent invocation/session id, process id and process-start identity; same request_id throughout. A denied launch has child_pid=null with explicit denied-before-start, not a fabricated child process or recovery observation.
5. **Actual execution/capture linkage**: bind terminal streams to request/session/process; record pipe-open, EOF or truncation/timeout, exact byte counts, full-stream hashes and outcome. An empty stream requires captured=true and actual zero bytes; no file or no EOF is UNKNOWN/INCOMPLETE, not empty-success. Reference projections by stream hash and source offsets/index.
6. **Integrity**: append records as emitted; close a manifest binding request, effective policy, decision, launch/non-launch, raw streams and derived verdict by relative path/size/hash. Atomic exclusive artifact creation and normal CAS checkpoint protect continuity; hashes establish byte identity, not source honesty or scientific truth.
7. **Secrets**: whitelist fields of the telemetry record, not commands or actions. No global config dump, auth file, secret environment value or unrelated session. Record necessary non-secret argv and policy fields exactly. If required decision semantics contain sensitive data, withhold that field/body with reason and a safe opaque reference provided by the source; mark the package incomplete for the affected claim. Do not publish individual secret-value hashes or pretend redacted content is the full original. Secret-safe capture must not change policy evaluation.

## Failure semantics
Any missing request normalization, applicable source, rule/path, explanation or session/time binding produces **F4 OBSERVABILITY UNCERTAIN**. Inconsistent ids/hashes are integrity failures. Both prevent successor authorization. Policy allow is not task acceptance; policy deny is not proof of broken continuity. No defaults to allow, no command whitelist and no relaxation of sandbox or approval.

Before any new authorized experiment, a separately approved capability inspection must establish whether this exact decision boundary can emit the required non-secret records. If not, STOP at the design gap and propose the smallest recorder-only change to the responsible harness component; do not launch a successor to discover after the fact that the trace is missing.

This design does not authorize implementation, policy tests, a model call or a new worker. It specifies what direct evidence must exist before the next gate can be evaluated.

