# Model routing and reasoning-effort protocol

Current machine source: `config/model-routing.json`. Validate it with `python tools/model_routing.py validate` before adopting a model-policy change.

## Cost-performance ladder

| Route | Default effort | Use it for | Raise effort when |
|---|---:|---|---|
| Luna | low | bounded extraction, triage, formatting, metadata and clear-brief edits | medium only for coordinated work; `none` only for deterministic transforms with an independent validator |
| GPT-6.1 Sol | medium | everyday research, coding, writing, computer use and judgment-bearing workflows | low for focused work; high for independent scientific/visual review, deep verification or consequential bounded architecture |
| Astra | medium | highest-stakes ambiguous architecture, cross-system L3 integration and exceptions after lower routes are insufficient | high only for consequential failure analysis or exacting integration with evidence that Astra is the right capability |

GPT-6.1 Sol does not support `none` or `minimal`. `xhigh` is not a default and requires a representative quality gain. `max` additionally requires explicit Human PI authorization and evidence that xhigh is insufficient. Because GPT-6.1 Sol is the near-Astra lower-cost route, try a bounded Sol/high review before Astra when capability fit is otherwise equal; route to Astra directly only when the task itself is an L3 architecture/exception decision.

## Runtime rules

- Use the Responses API for GPT reasoning with tools.
- Start at the route's declared default effort; use `configuration_update` where the runtime supports changing effort without discarding the conversation prefix.
- Record requested model, requested effort, actual runtime identity and observed capability separately.
- Missing required capability produces `HELD` or `UNCERTAIN`; never silently fall back to GPT 5.6, GPT-6 Sol or another role.
- DeepSeek Flash/Pro routing and external DSH/provider configuration are outside this manifest and remain unchanged.

## Updating models later

1. Review official capability, migration, reasoning and pricing documents.
2. Change the model ID and effort policy in the central manifest, not scattered historical artifacts.
3. Validate the manifest and run representative task evaluations for quality, latency and cost.
4. Record a superseding decision and a Foundation checkpoint.
5. Update current role/task documents; preserve historical evidence with the identifier actually observed.
