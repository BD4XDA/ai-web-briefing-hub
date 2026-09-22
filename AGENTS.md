# Shared agent rules

Read these files in order before starting work:

1. `60-handoffs/CURRENT.md`
2. The relevant brief in `10-briefs/`
3. Related decisions in `50-decisions/`

Keep source material intact. Put new deliverables in `40-work/`, and update `60-handoffs/CURRENT.md` when pausing or completing a task. Record non-obvious choices in `50-decisions/`.

Do not commit secrets or upload private data without explicit approval.

Use evidence proportionally. Do not calculate or recheck hashes by default. Prefer direct content inspection, Git status/diff, schema validation, targeted tests, and source provenance. Use a digest only when exact byte identity is part of the claim, data crosses a process/machine/network boundary, an immutable manifest or checkpoint requires it, or a concrete tampering/staleness question cannot be answered more directly. When using a digest, state the failure it can detect; never treat it as proof of semantic correctness, complete capture, authenticity, safety, or authorization.
