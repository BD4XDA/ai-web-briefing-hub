# AT07 bounded repair scope

Inherited checkpoint 20260922T093640-7d71f54b9b3b verified. F4 remains INSUFFICIENT_EVIDENCE after exact original thread/time-window read-only queries (F4-provenance.json). No policy edits or worker launches.

F6 repair: local_repair.py replaces the defective negative-list event grouping with explicit action/diagnostic/passive/unknown classes and preserves event index/raw payload. Action lifecycles are grouped by item id. Missing observation remains UNCERTAIN and C1 NOT PROVEN; diagnostic items do not count as actions. Explicit out-of-scope action evidence blocks acceptance. Gate completion does not assert classification correctness.

F5 repair: bind_stream/bind_execution include actual raw UTF-8 content and hash/size/capture receipt, distinguish empty/missing/not-captured/truncated/tampered/oversized/unsafe/unbound/invalid encoding, and deny completeness if a required stream cannot be safely bound. The repaired binder is used to build this AT07 review package, not merely tested in isolation.

These are task-local derived replacements. AT05 experiment.py, its prompts/responses/results and frozen Foundation are unchanged. No successor orchestration is enabled or rewired. Future separately authorized task wiring must supply truthful mechanical scope/checkpoint/observation/writeback-equality results; this gate is neither a policy engine nor an OS sandbox. It returns a decision and does not itself write files. The offline negative cases validate decisions, not destructive command execution or a real filesystem integration.

Regression: actual subprocess test_local_repair.py exit0, 9 unittest groups and 45 assertion records. Retained AT05 event/stream replay is real historical input; positive review/observation and negative-control fixtures are explicitly synthetic. They do not certify real worker recovery. Test stdout/stderr and exact implementation/test code are supplied in full.

Declared limitations: secret detection is a finite conservative pattern screen plus explicit withholding, not a universal classifier. 'captured complete' relies on the declared capture process and receipt; it cannot prove all OS activity was captured. Action scope is an input from deterministic path/action checks; these functions do not decide an actual command's policy safety. No live integration/new worker was tested. C1 NOT PROVEN, C2 full-workflow UNCERTAIN, P5 UNCERTAIN, P6 YELLOW remain.

Rollback: original files never overwritten; derived implementation is not enabled for live dispatch. Any failed negative control disables the derived repair. All controls passed in this one run; review still pending. An adverse review means no further repair/review retry this session.

One independent DSH Flash evidence-package review will evaluate only these demonstrated F5/F6 local repairs and bounded offline gates. Standard >=0.80/PASS/completed/zero-tools/no-anomaly thresholds apply. No successor or AT08 executable packet is authorized while F4 remains unobservable.

