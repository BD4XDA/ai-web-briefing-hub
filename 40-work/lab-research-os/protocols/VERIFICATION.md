# Verification v1

Report is not evidence. Every report contains Claim, Evidence IDs, Verification Method, Result (PASS/FAIL/UNCERTAIN), Confidence (0–1), Anomaly/Conflict and reviewer identity. Evidence records contain file path, SHA256, collection time, locator and scope. Absolute source paths remain local and must be allowed by the task packet.

The deterministic validator confirms structure, reference resolution, source-byte hashes and gate conditions. It does not establish scientific truth, model authenticity, absence of secrets, or authorization to publish. PASS applies only to the written claim and method. A model reviewing a test log must say 'reviewed test evidence', not 'ran the tests'. Source observations and their age remain visible.

Workflow: worker execution → deterministic checks → DeepSeek verification → owner review → integration. Flash suits metadata and test-output consistency; Pro suits complex textual consistency. Visual review requires a qualified visual route. Tool/model failures become UNCERTAIN, not inferred PASS. No automatic substitution with the same model under a different alias.

L0: deterministic safe repair within packet. L1: return to original worker with specific failing evidence. L2: bounded heterogeneous review or queue an exception; exhausted retries alone stay L2. Astra reviews architectural contradiction, important insufficient evidence, suspected fabricated evidence, source-of-truth conflict or unexplained repeated failure. Only L3 consequences (research direction, core interpretation, data integrity, ethics/authorship/authenticity, major experiments/budget or irreversible action) require Human PI.

Exception package fields: Problem, Evidence, Conflicting Evidence, Attempts, Confidence, Possible Explanations, Consequence, Recommended Next Check. Do the smallest discriminating check. A policy does not imply an autonomous Review Board has been deployed.

For the foundation pilot, require all reports PASS, confidence >=0.8, no unresolved anomalies, valid evidence hashes, and one explicitly identified DeepSeek review. Record actual reported model separately from configured alias; missing runtime identity is a limitation, not a guessed model. The validator enforces evidence gates; the owner checks reviewer suitability.
