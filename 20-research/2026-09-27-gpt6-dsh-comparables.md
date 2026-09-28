# Research note · GPT-6, DSH and comparable systems

Reviewed 2026-09-27. Links are primary vendor/project sources. This note records current external evidence; it is not a claim that any provider or runtime is available in the local account.

## OpenAI GPT-6 evidence

- GPT-6 family guidance: https://developers.openai.com/api/docs/guides/latest-model
- Model/effort selection: https://developers.openai.com/api/docs/guides/model-selection
- Reasoning effort and mid-conversation `configuration_update`: https://developers.openai.com/api/docs/guides/reasoning
- Current API pricing: https://developers.openai.com/api/docs/pricing
- Release and fix chronology: https://developers.openai.com/api/docs/changelog

Observed guidance: Astra is the highest-capability option; Sol is the demanding-work reasoning default; Luna is intended for efficient repeatable work. Official model-selection guidance maps Luna Low/Medium to scoped and coordinated work, Sol Medium to everyday coding/research requiring judgment, Sol Extra-high to deep verification, Astra Medium to broad ambitious work and Astra Extra-high to exacting complex deliverables. The reasoning guide says `xhigh` should be used only when evaluations justify its added latency and cost. Tool-using reasoning should use the Responses API. Astra does not accept `none`; Sol and Luna do.

## DSH evidence

- Repository and developer-preview status: https://github.com/deepseek-ai/deepseek-harness
- Releases: https://github.com/deepseek-ai/deepseek-harness/releases
- CLI profiles/plugins: https://github.com/deepseek-ai/deepseek-harness/blob/master/apps/cli/README.md

Local static inspection found DSH `0.1.1-rc.2`; npm `latest` is `0.1.5-rc.3` and `next` is `0.1.7-rc.2`. The installed instruction plugin loads `AGENTS.md` and `CLAUDE.md` from the project chain; the standard preset contains instruction, filesystem and command tools whose working directory derives from the session workspace. This establishes structural compatibility with Lab Research OS. No paid model call or upgraded-version end-to-end qualification was performed.

## Comparable projects and directly reusable patterns

- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/ — handoffs, guardrails, persistent sessions and tracing. Reuse its manager-versus-handoff distinction and guarded tool boundaries; do not replace the project's evidence/checkpoint contracts wholesale.
- LangGraph: https://github.com/langchain-ai/langgraph and https://langchain-ai.github.io/langgraph/reference/checkpoints/ — durable checkpoints, pending writes, interrupts and resume. Reuse the checkpoint/interrupt semantics if Lab Research OS later gains an executable workflow engine.
- CrewAI Flows: https://github.com/crewAIInc/crewAI/blob/main/docs/v1.14.7/en/concepts/flows.mdx — persisted flow state and human-feedback gates. Reuse the explicit pause/outcome routing pattern, not the role-play layer by default.
- AutoGen: https://microsoft.github.io/autogen/dev/user-guide/agentchat-user-guide/tutorial/state.html — portable agent/team state save/load. Useful as a state-serialization reference, but the main repository is now in maintenance mode, so it is not the preferred new runtime dependency.
- PaperQA2: https://github.com/Future-House/paper-qa — scientific-paper retrieval, evidence gathering, citations, metadata/retraction checks and cheap/high-quality presets. This is the strongest candidate for a bounded literature-evidence component.
- STORM: https://github.com/stanford-oval/storm — multi-perspective research and cited report generation. Borrow question decomposition and source-grounded report assembly.
- AI Scientist v2: https://github.com/SakanaAI/AI-Scientist-v2 — end-to-end hypothesis/experiment/manuscript automation. Treat as an architecture reference only; its autonomy and ML-experiment scope exceed current Human-PI gates.

Conclusion: the project is not a duplicate of these runtimes. It is a harness-neutral governance, evidence and recoverability layer. Directly borrow narrow components and contracts; do not import an entire orchestration framework until an actual executable-runtime need is demonstrated.
