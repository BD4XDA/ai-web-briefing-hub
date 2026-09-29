# Local cost telemetry

`run-cost.jsonl` is a local, ignored operational ledger. One compact record is appended per executed workload with `python tools/cost_telemetry.py record ...`. It contains route, token provenance, material calls/failures, useful output and the lightweight `B/C/EVR`; it must not contain prompts, paper text, credentials or personal data.

Use `python tools/cost_telemetry.py show --date YYYY-MM-DD` to produce the aggregate consumed by a Human PI Daily Research Brief. `unavailable` token telemetry is preserved rather than guessed.
