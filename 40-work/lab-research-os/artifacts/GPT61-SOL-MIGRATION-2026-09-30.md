# GPT-6.1 Sol migration evidence · 2026-09-30

## Official observations

- OpenAI identifies GPT-6.1 Sol as the balanced complex-work route with near-Astra performance at lower cost.
- Supported efforts are low, medium (default), high, xhigh and max; none and minimal are unsupported.
- The model has a 1,050,000-token context window, 128,000 maximum output and supports text plus image input.
- Standard model-page pricing is $2 per million input tokens, $0.10 cached input and $10 output; prompts above 272K input are subject to long-context multipliers. This reinforces early conversation rollover based on marginal context value rather than window exhaustion.
- Responses API is required for tool calling.

Sources: [GPT-6.1 Sol model](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [GPT-6 guide](https://developers.openai.com/api/docs/guides/latest-model), [model selection](https://developers.openai.com/api/docs/guides/model-selection).

## Project interpretation

The official pages do not publish a project-specific scientific benchmark. “Near-Astra” is therefore not treated as universal equivalence. The project uses GPT-6.1 Sol as the default judgment-bearing route and keeps Astra as an evidence-gated exception for the highest-stakes architecture and L3 decisions.

The app's current model catalogue exposes `gpt-6.1-sol`, so the target is available to new Codex work. This proves route availability, not scientific qualification for every workload. Actual model identity, effort and useful output remain recorded per run.

## Freshness check · 2026-10-02

Current official OpenAI search results still expose the same GPT-6.1 Sol model page, supported-effort contract and Responses API guidance. Direct page opening then failed on three equivalent network attempts, so the bounded-retry rule fired and no fourth fetch was made. The routing decision remains supported by the prior direct official-page capture plus the current official index; this is not treated as a new workload-specific benchmark.

## Applied policy

| Work class | Route |
|---|---|
| High-volume discovery, metadata, formatting | Luna/low or deterministic tools |
| Focused editing, fact checks, compact handoff | GPT-6.1 Sol/low |
| Everyday research, coding, synthesis, tool workflows | GPT-6.1 Sol/medium |
| Consequential scientific/visual review or bounded architecture | GPT-6.1 Sol/high |
| Deep exceptional analysis | GPT-6.1 Sol/xhigh only after representative gain |
| Maximal reasoning | GPT-6.1 Sol/max only with Human PI authorization and evidence xhigh is insufficient |
| Highest-stakes cross-system/L3 exception | Astra after lower route is insufficient or an eval shows material gain |
