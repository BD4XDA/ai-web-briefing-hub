# AT05-recovery-01 — predeclared experiment

Exactly one new ephemeral Codex CLI successor, no resume/fork/prior transcript. Use installed CLI with --ignore-user-config, --json, --sandbox read-only. The prompt contains only project entry, packet and observation command. No previous outcome is supplied as conversation. Global/platform defaults and model internals cannot be independently audited; the claim is scoped to captured invocation/context at the harness boundary.

The worker must execute the observation command ONCE and use its returned canonical documents to determine the task. The observer is task-local instrumentation, not a new memory/compiler subsystem: from the declared child cwd it checks parent markers, then reads actual project instructions/packet, obtains current state through unchanged foundation.current, and reads the accepted manifest. It prints paths, exact content, hashes and actual read timestamps. The model itself receives no precompiled historical summary. It may use one command tool and then its final message (two reasoning calls budget); one independent review follows. Any extra tool use or repeated observation makes this experiment FAIL/UNCERTAIN as below.

Task: return ONLY JSON with exact fields project_id (marker), release (accepted manifest), frozen_file_count (len of manifest files), observed_checkpoint (actual current). Do not reproduce the old index, hash frozen source files, repair anything, or write files. Harness/controller captures candidate and, only after gates, writes canonical artifacts/at05/recovery-receipt.json.

Predeclared gates, evaluated by artifacts/at05/experiment.py:
- G0 prelaunch packet/program/prompt binding intact; packet validates against unchanged schema; expected checkpoint still current. Conflicting current state stops the attempt.
- G1 one CLI invocation (no resume/fork), thread.started identity captured, completed command trace contains exactly one successful observation command, observer's discovery/reads/current state present, no other completed tool action, worker exit0 and turn.completed. Missing trace = UNCERTAIN; known extra access/action = FAIL.
- G2 candidate exact fields/values from captured inputs; schema/path/root/hash checks. Contradiction = FAIL; absent output = UNCERTAIN.
- G3 independent response parses required Claim/Evidence/Verification Method/Result/Confidence/Anomaly/Limitation fields with valid types; reason completed, tools0, exit0. FAIL result/anomaly = FAIL; missing/malformed/incomplete/low confidence/UNCERTAIN = UNCERTAIN. PASS requires >=0.80 and <=1.
- G4 immutable candidate copied exclusively to approved target only after G0–G3 PASS, then exact-byte equality and hashes. Failed writeback = FAIL.
- C1 = PROVEN only if G0–G3 PASS; FAIL on contradicted recovery/output -> NOT PROVEN; otherwise UNCERTAIN. Scoped to this invocation boundary, not opaque provider internals.
- C2 = PROVEN when the pre-bound gate automatically records a terminal PASS/FAIL/UNCERTAIN and enforces the corresponding writeback policy. This proves only the exercised branch, not correctness of every branch. Gate execution exception or evidence binding mismatch -> UNCERTAIN.
- Overall = FAIL if any definite failed gate, else UNCERTAIN if any unknown, else PASS. No human override.
- P5 stays UNCERTAIN unless C1/C2 PROVEN, overall PASS, exact writeback and normal CAS checkpoint succeed. If those all succeed, scope promotion only to this new receipt workflow, without retroactively repairing AT03 evidence.
- P6 remains YELLOW: held pilots and unexercised rejection paths still prevent a broader census claim. No scale execution.
- Checkpoint immediately via unchanged foundation.py with expected-current protection. CAS conflict -> preserve, stop/reload/reconcile, never force.
- One launch, one independent review, no timeout/low-confidence/parse retries. Worker180s, reviewer120s. Missing evidence is never reconstructed.

Scope excludes all other files except standard runtime/auth internal reads of existing harnesses. Project task access is limited by the observer allowlist and checked tool trace; the read-only sandbox is not proof of no hidden provider context. No credentials copied, printed or modified. Trace covers model tools and observer file reads, not every OS read.

Independent reviewer examines the actual launch/observation/command/candidate/check package and code. It reviews execution evidence; it does not execute the worker. Requested model labels are not authenticity proof.

Observation versus validation versus review versus automatic gate remain separate. All criteria above exist before execution.

