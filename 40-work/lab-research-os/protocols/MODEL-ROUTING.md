# Model routing and reasoning-effort protocol

Current machine source: `config/model-routing.json`. Validate it with `python tools/model_routing.py validate` before adopting a model-policy change.

## Cost-performance ladder

| Route | Default effort | Use it for | Raise effort when |
|---|---:|---|---|
| Luna | low | bounded extraction, triage, formatting, metadata and clear-brief edits | medium only for coordinated work; `none` only for deterministic transforms with an independent validator |
| Sol | medium | everyday research, coding, writing and judgment-bearing workflows | high for independent scientific/visual review, deep verification or consequential acceptance |
| Astra | medium | ambiguous architecture, cross-system integration and exceptions | high for consequential failure analysis or exacting integration |

`xhigh` is not a default. Use it only after representative evaluations show a clear quality gain worth the extra latency/cost, or with explicit Human PI authorization. Do not use `max` by default. Prefer promotion to the next model over spending extreme effort on a model whose role no longer fits.

## Runtime rules

- Use the Responses API for GPT reasoning with tools.
- Start at the route's declared default effort; use `configuration_update` where the runtime supports changing effort without discarding the conversation prefix.
- Record requested model, requested effort, actual runtime identity and observed capability separately.
- Missing required capability produces `HELD` or `UNCERTAIN`; never silently fall back to GPT 5.6 or another role.
- DeepSeek Flash/Pro routing and external DSH/provider configuration are outside this manifest and remain unchanged.

## Updating models later

1. Review official capability, migration, reasoning and pricing documents.
2. Change the model ID and effort policy in the central manifest, not scattered historical artifacts.
3. Validate the manifest and run representative task evaluations for quality, latency and cost.
4. Record a superseding decision and a Foundation checkpoint.
5. Update current role/task documents; preserve historical evidence with the identifier actually observed.
