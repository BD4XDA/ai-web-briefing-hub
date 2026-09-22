# AT05 exception judgment — no gate override or retry

Automatic execution checkpoint: 20260922T091207-ca38de8b3e1a.
Raw automatic result remains FAIL; writeback remains WITHHELD.
Coordinator accepts C1 NOT PROVEN; C2 is UNCERTAIN, superseding only the automatic script's meta-claim C2 PROVEN. This does not turn a failed gate into PASS or change predeclared criteria.

## Observations and evidence

- One CLI invocation launched with --ephemeral, --ignore-user-config and read-only mode; no resume/fork/prior transcript. See launch-input.json, worker-execution.json and worker.stdout. A distinct thread id is captured, but a new id alone is not recovery proof.
- Worker returned a blocked response instead of a receipt. No observation payload or successful command execution exists. worker.stderr contains the actual exec_command CreateProcess rejection: blocked by policy. The command was not successfully executed. No fresh recovery of canonical documents was demonstrated.
- worker.stdout contains an item of type error about exceeded skills context budget. This is not proof of another tool action. The adapter places all unrecognized completed item types in other_tools and uses that to force FAIL. It therefore implements the predeclared missing-trace/extra-action distinction incorrectly in this observed case.
- automatic-acceptance.json records G0 PASS, G1/G2 FAIL, G3 FAIL and G4 WITHHELD. recovery-receipt.json was not created. The failure path prevented promotion without a coordinator-supplied PASS.
- Separate DSH review completed with zero tools: result FAIL, confidence0.86, anomaly list nonempty. It reviewed supplied execution evidence, not independent machine state.
- The review package includes structured command/thread projections but omits raw worker.stderr. Consequently its statement that policy denial lacks captured support is limited by the supplied subset. The actual stderr supplies that support. Its suggestion that auto-rejection contradicts disabled approvals is not accepted: those observations are compatible. No second review was requested.
- CLI stderr also records an internal sampling retry and startup/network warnings. Exactly one worker process invocation is established; the packet's model-call budget cannot be certified from this partial network telemetry. No application-level retry or second worker was launched.

## Classification, consequence, minimum proposal

F4: policy-denied execution, confirmed by stderr. Consequence: recovery experiment could not reach observation. Minimum next check, only in a future explicitly authorized diagnostic, is inspect the applicable CLI policy decision/configuration with read-only tools; do not disable safeguards or simply relaunch.

F6: observed task-adapter event classification defect, not Foundation. Missing successful observation plus an error item was mapped as extra tool activity. Consequence: the rejection was safe, but FAIL versus UNCERTAIN semantics and the C2 PROVEN meta-claim are unsupported. Minimum proposed repair is explicit handling of error items distinct from command/tool actions and a truth table matching the existing predeclared criteria. Do not apply that repair or rerun in AT05.

F5: review package omission of existing raw denial stderr. Consequence: reviewer could not establish the execution cause and added an unsupported contradiction. Minimum proposed repair is byte-bound inclusion of the relevant captured stdout/stderr in future evidence packages. No reconstruction of unavailable evidence.

Limitation: C1 freshness remains untested beyond the invocation boundary because actual canonical recovery never ran. Large default skill context and hidden harness defaults are not themselves proof of prior conversation leakage. No Foundation architecture defect or reason for v0.2 is demonstrated.

## Terminal acceptance

C1 Fresh Successor Recovery: NOT PROVEN for this failed attempt; this is not a claim that Foundation can never recover.
C2 Automatic Acceptance: UNCERTAIN. Safe automatic withholding is observed, but correct terminal classification against predeclared criteria is not proven.
P5: UNCERTAIN.
P6: YELLOW, unchanged.
Foundation: unchanged.
Do not retry, repair, replace a model, modify thresholds or start broader work. Preserve all raw evidence and the earlier automatic checkpoint. Commit this narrow qualification with expected-current protection and stop.

