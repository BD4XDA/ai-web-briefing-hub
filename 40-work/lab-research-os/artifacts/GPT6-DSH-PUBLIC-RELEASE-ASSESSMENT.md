# GPT-6 routing, DSH compatibility and public-release assessment

Assessment date: 2026-09-27. No model was called and no external configuration was changed.

## Outcome

- **GPT routing:** implemented as a validated central manifest. Luna/low handles bounded volume work; Sol/medium is the general research/coding route; Sol/high handles consequential independent scientific/visual QA; Astra/medium or high owns ambiguous architecture and exceptions. `xhigh` is evaluation- or PI-gated.
- **DeepSeek:** unchanged. The manifest deliberately records DeepSeek as externally managed and does not remap Flash or Pro.
- **DSH:** structurally compatible, not newly live-qualified. Installed version is `0.1.1-rc.2`; npm `latest` is `0.1.5-rc.3`, while the upstream prerelease line reaches `0.1.7-rc.2`. Installed source confirms project-chain `AGENTS.md`/`CLAUDE.md` loading plus workspace filesystem and command tools. That is sufficient to consume this file-based OS from the project root. It is not evidence that an upgraded DSH profile, provider, web UI or paid model path works end to end.
- **Future models:** explicitly supported through `config/model-routing.json`, its schema, validator, tests and an update contract. Changes require official-doc review, representative evaluation, a decision and a Foundation checkpoint.
- **Public release:** feasible as a curated standalone distribution, but the current repository snapshot is not release-ready.

## DSH update risk

DSH upstream describes itself as a developer preview with breaking changes expected. Recent releases add model/provider discovery, editable account models, dynamic tools, new headless continuation/JSON event features, MCP resources and expanded workspace tooling; they also contain plugin/persona/API changes. The local router and plugins were built around `0.1.1-rc.2`, so an in-place upgrade would mix migration and qualification risk.

Recommended path: create an isolated DSH profile pinned to `0.1.5-rc.3` first, validate plugin peer ranges and the Sol/Luna router, then run no-model instruction/tool smoke tests and one separately authorized bounded model task. Evaluate `0.1.7-rc.2` only after the stable-candidate path passes. Do not upgrade the working profile in place.

## Public-release audit

The GitHub repository is already publicly visible, but its root README still describes it as private. Static tracked-file inspection found no high-confidence token/private-key signature and no tracked secret-like filename. That is useful negative evidence, not a complete security review.

Blocking release gaps:

1. No repository license, SECURITY policy or CONTRIBUTING guide.
2. At least 69 project files contain machine-specific absolute paths; many historical artifacts embed old workspace locations and raw execution context.
3. Historical evidence includes large prompts, stdout/stderr and environment-specific captures that are valuable internally but unsuitable as the default public product surface.
4. README/onboarding assumes the current owner's directory layout and inherited local tools.
5. No clean-room install test on a second machine or CI matrix exists.

Recommended public package:

- Keep: core `AGENTS.md`, generic `PROJECT.md` template, checkpoint/packet protocols, schemas, Foundation tools, model-routing seam and synthetic tests/examples.
- Exclude or sanitize: `artifacts/at02` through `at11`, raw prompts/streams, personal drive paths, local provider/profile references and research-corpus bindings.
- Add: chosen license, SECURITY, CONTRIBUTING, CODE_OF_CONDUCT, install/quickstart, release manifest, synthetic demo project and CI on supported Python/OS versions.
- Publish from a clean export or new repository so the public history never contains removed private material. Do not rely on deleting files in a later commit.

## What to borrow

| Source | Borrow directly | Do not copy wholesale |
|---|---|---|
| OpenAI Agents SDK | manager vs handoff semantics, tool guardrails, tracing vocabulary | provider-specific runtime as the project's only execution layer |
| LangGraph | durable checkpoints, interrupts, pending-write resume semantics | graph runtime before an executable workflow need exists |
| CrewAI Flows | persisted flow state and explicit human-feedback outcomes | role-play abstractions as governance truth |
| AutoGen | portable agent/team state serialization ideas | new runtime dependency while the project is in maintenance mode |
| PaperQA2 | scientific retrieval, evidence ranking, citations, metadata/retraction checks, fast/high-quality presets | replacing Human-PI acceptance or project evidence contracts |
| STORM | multi-perspective question generation and cited report assembly | automatic report acceptance |
| AI Scientist v2 | experiment-tree and manager concepts as research references | autonomous hypothesis-to-publication execution in the present phase |

## Sources

- OpenAI GPT-6 guidance: https://developers.openai.com/api/docs/guides/latest-model
- OpenAI model selection: https://developers.openai.com/api/docs/guides/model-selection
- OpenAI reasoning guide: https://developers.openai.com/api/docs/guides/reasoning
- OpenAI pricing: https://developers.openai.com/api/docs/pricing
- OpenAI changelog: https://developers.openai.com/api/docs/changelog
- DSH repository/releases: https://github.com/deepseek-ai/deepseek-harness and https://github.com/deepseek-ai/deepseek-harness/releases
- Comparable projects: https://openai.github.io/openai-agents-python/ ; https://github.com/langchain-ai/langgraph ; https://github.com/crewAIInc/crewAI ; https://github.com/microsoft/autogen ; https://github.com/Future-House/paper-qa ; https://github.com/stanford-oval/storm ; https://github.com/SakanaAI/AI-Scientist-v2
