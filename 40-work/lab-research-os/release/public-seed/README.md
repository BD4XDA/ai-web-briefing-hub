# Lab Research OS Core

Lab Research OS Core is a provider-neutral starter for recoverable research-agent work. It contains schemas, task and evidence contracts, checkpoint tooling, model-routing policy and deterministic tests. It does not include private research corpora, credentials, historical execution logs or a bundled agent fleet.

## Quick start

1. Create an isolated Python environment.
2. Install `requirements.txt`.
3. Review `AGENTS.md` and `PROJECT.md`.
4. Adapt `packets/bootstrap.json` to the local project and create the initial checkpoint state.
5. Run `python -m unittest discover -s tests -v`.

This draft intentionally has no final publication license until the maintainer selects one. Do not redistribute a final release without an explicit license.
