# Verification v1

Report is not evidence. Every report contains Claim, Evidence IDs, Verification Method, Result (PASS/FAIL/UNCERTAIN), Confidence (0–1), Anomaly/Conflict and reviewer identity. Evidence records contain a source locator, collection time, scope and enough directly inspectable content or references to support the claim. Add SHA256 only when the declared claim requires exact byte identity across an immutable or trust boundary. Absolute source paths remain local and must be allowed by the task packet.

The deterministic validator confirms structure, reference resolution, any explicitly declared byte bindings, and gate conditions. It does not establish scientific truth, model authenticity, complete capture, absence of secrets, or authorization to publish. PASS applies only to the written claim and method. A model reviewing a test log must say 'reviewed test evidence', not 'ran the tests'. Source observations and their age remain visible.

## Evidence proportionality

Default to no new digest. Use direct content inspection for a currently readable file, Git status/diff for working-tree change, schema validation for shape, and targeted tests for behavior. Do not hash merely because a file exists, because another artifact already contains a digest, or because a previous stage used hashes.

A new or repeated digest needs one explicit reason:

- the claim is exact byte equality or immutable snapshot identity;
- the data crosses a process, machine, harness, storage or network boundary where substitution/truncation is in scope;
- a committed manifest/checkpoint contract requires a digest;
- a concrete tampering, stale-writer or cache-key question cannot be answered more directly.

If none applies, omit the digest. If one applies, record the protected object, boundary, expected value/source and failure detected. Reuse an already accepted binding when its object and boundary are unchanged; do not rehash for reassurance. A matching digest does not prove who produced the bytes, whether capture was complete, whether the contents are true or safe, or whether an action is authorized.

Workflow: worker execution → deterministic checks → DeepSeek verification → owner review → integration. Flash suits metadata and test-output consistency; Pro suits complex textual consistency. Visual review requires a qualified visual route. Tool/model failures become UNCERTAIN, not inferred PASS. No automatic substitution with the same model under a different alias.

L0: deterministic safe repair within packet. L1: return to original worker with specific failing evidence. L2: bounded heterogeneous review or queue an exception; exhausted retries alone stay L2. Astra reviews architectural contradiction, important insufficient evidence, suspected fabricated evidence, source-of-truth conflict or unexplained repeated failure. Only L3 consequences (research direction, core interpretation, data integrity, ethics/authorship/authenticity, major experiments/budget or irreversible action) require Human PI.

Exception package fields: Problem, Evidence, Conflicting Evidence, Attempts, Confidence, Possible Explanations, Consequence, Recommended Next Check. Do the smallest discriminating check. A policy does not imply an autonomous Review Board has been deployed.

For the historical foundation pilot, require all reports PASS, confidence >=0.8, no unresolved anomalies, the packet's predeclared byte bindings, and one explicitly identified DeepSeek review. This does not create a universal hash requirement for later work. Record actual reported model separately from configured alias; missing runtime identity is a limitation, not a guessed model. The validator enforces declared evidence gates; the owner checks reviewer suitability.
