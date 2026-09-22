# Exact worker resume procedure

1. Open this canonical directory, not an unrelated current shell folder. Read AGENTS.md and PROJECT.md.
2. Run `python tools/foundation.py show`. It reads LATEST and checks snapshot integrity. A missing marker, bad hash or writer conflict requires evidence-led repair, not deletion.
3. Read only the indicated task packet and decision/evidence references. Check actual volatile prerequisites (a port/process/model) only if your next task needs them.
4. Check `python -c "import jsonschema; print('validator available')"` before contract work. The existing environment has jsonschema 4.26.0; no install or upgrade is authorized by this document.
5. Validate the packet with `python tools/contracts.py packet packets/<task>.json`. Compare its expected_checkpoint to current state before execution; historical packet validation intentionally does not reject newer project checkpoints.
6. Execute only its bounded write set, have a separate verifier inspect located evidence, and validate the bundle if it is an inventory task. Do not interpret the write-set contract as an operating-system sandbox.
7. Fill all continuity fields in a NEW state input. Commit `python tools/foundation.py checkpoint --input packets/<new-state>.json --expected <current-id>`. A stale parent means reload and reconcile, not force overwrite.

No task is authorized merely because it is listed in IDEA-INBOX. Broader census requires an explicit allowlist packet and its resource limits. Never start a full drive scan from this resume procedure.
