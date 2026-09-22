# Decision 0005 · Evidence proportionality

Decision: hashing is no longer a default verification step for agents in this project.

Use direct inspection, Git status/diff, schema validation and targeted tests for ordinary local work. A digest is justified only when exact byte identity is part of the claim, evidence crosses a meaningful boundary, an immutable manifest/checkpoint requires it, or a concrete tampering/staleness question needs it. Repeating an accepted digest without changed inputs or a named contradiction is prohibited reassurance work.

Rationale: indiscriminate hashing adds latency and evidence noise while encouraging false confidence. Hash equality binds bytes; it does not prove provenance, capture completeness, semantic correctness, safety or authorization.

Existing historical packets and checkpoint formats retain their declared hashes. This decision changes the default for new work and does not rewrite prior evidence contracts.
