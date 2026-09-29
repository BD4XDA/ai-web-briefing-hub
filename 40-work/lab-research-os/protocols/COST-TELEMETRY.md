# Lightweight cost and value telemetry

## Goal

Track enough operational cost to improve routing without creating another monitoring workload. Collection is passive and run-scoped; it must not trigger an extra model call, token audit or daily recomputation.

## One record per executed workload

Append a compact record to the workload's existing run log. For project-owned execution, use `python tools/cost_telemetry.py record ...`; it writes the ignored local ledger `artifacts/telemetry/run-cost.jsonl` without storing prompts or research content. Private Daily Paper work also keeps the same summary in its existing corpus run log. Record:

- workload, trigger and outcome;
- model class and reasoning effort actually used when observable;
- approximate input/output/total tokens when the provider or harness reports them;
- otherwise a clearly labelled estimate and its method, or `unavailable` when no defensible estimate exists;
- tool/model call count at the useful aggregate level, failed-attempt count and whether the three-attempt stop rule fired;
- high-reasoning/Astra calls and whether each was justified;
- useful deliverables or decisions produced;
- lightweight benefit `B`, cost `C`, `EVR = B/C`, and the next cheaper qualified route if one exists.

Never claim estimated tokens as provider-reported usage. Do not infer hidden chain-of-thought tokens. Do not retain prompts, private paper text, credentials or unrelated personal content in telemetry.

## Daily report projection

Section 9, `💰 Compute / Agent Budget`, of the Human PI Daily Research Brief summarizes the last reporting period:

- approximate token range and whether it is reported, estimated or unavailable;
- model/agent classes and reasoning levels used;
- material tool/retry counts and stop-rule events;
- `B/C/EVR` at run level and whether a cheaper route is recommended;
- any unnecessary high-reasoning use.

Keep this to a few lines on normal days. Zero model usage or unavailable token telemetry are valid results. The private ledger remains in the existing local run record; the daily brief carries only the compressed summary.

Before composing the brief, `python tools/cost_telemetry.py show --date YYYY-MM-DD` may summarize the shared local ledger. Reading the ledger is deterministic and must not trigger a model call.
