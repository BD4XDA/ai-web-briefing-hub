# Decision 0017 — GPT-6.1 Sol routing and Daily Paper rollover closure

Status: accepted by Human PI on 2026-09-30.

OpenAI's current model page describes `gpt-6.1-sol` as near-Astra performance at lower cost for complex coding, computer use and professional work. It supports `low`, `medium` (default), `high`, `xhigh` and `max`; it does not support `none` or `minimal`. Tool calling uses the Responses API. The project therefore replaces active `gpt-6-sol` targets with `gpt-6.1-sol` while preserving historical observations.

Cost-performance routing is Luna/low for routine volume; GPT-6.1 Sol/low for focused work, medium for everyday judgment and high for consequential independent review. `xhigh` needs representative evidence of gain. `max` additionally needs Human PI authorization and evidence that xhigh is insufficient. Astra is reserved for highest-stakes cross-system/L3 decisions, unresolved conflicts after bounded Sol/high review or a demonstrated Astra quality advantage. DeepSeek remains unchanged.

The Daily Paper rollover is complete in Codex. The successor resolved the canonical checkpoint and exact issue-022 continuation without recomputation. Existing automation-2 was repointed to it and remains the only daily heartbeat. The predecessor was archived, not deleted. Earlier evidence that DSH and Windows scheduling stores lacked this task was scoped correctly but did not describe Codex's automation store; the broader absence claim is superseded.

Official evidence:

- https://developers.openai.com/api/docs/models/gpt-6.1-sol
- https://developers.openai.com/api/docs/guides/latest-model
- https://developers.openai.com/api/docs/guides/model-selection
