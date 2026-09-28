# Decision 0009 · GPT-6 cost routing and runtime portability

Status: approved by direct Human PI instruction, 2026-09-27.

## Decision

Adopt `config/model-routing.json` as the single current project source for GPT model assignment and reasoning effort. Default routing is Luna/low for bounded repeatable work, Sol/medium for judgment-bearing everyday research/coding, Sol/high for independent consequential scientific or visual review, and Astra/medium for broad ambiguous architecture. Astra/high is reserved for consequential architecture and exacting integration. `xhigh` requires evaluation evidence or explicit Human PI authorization; it is not a standing default.

Use the Responses API for GPT reasoning with tools. Use dynamic effort updates when available. Hold a task when required capability is unavailable rather than silently changing model generation, role or provider.

DeepSeek Flash/Pro roles and external DSH/provider configuration are unchanged. This decision does not upgrade DSH, call a model, or qualify an external runtime.

## Rationale

Official OpenAI guidance places Luna on efficient repeatable work, Sol on demanding work needing judgment, and Astra on the most complex broad-context work. Current published token prices make Luna materially cheaper than Sol and Sol materially cheaper than Astra, while higher effort consumes more reasoning work. Therefore the best default is the lightest route and effort that meets a predeclared quality gate, with escalation triggered by task properties and evidence rather than prestige.

## DSH and model-update seam

The installed DSH `0.1.1-rc.2` statically supports project instruction discovery and workspace-scoped filesystem/command tools, so Lab Research OS is structurally portable to DSH. Upstream is newer and remains a developer preview; no in-place upgrade or live end-to-end qualification is implied. Future GPT updates change the central manifest, pass schema/semantic validation and representative evaluations, then receive a superseding decision/checkpoint. Historical identifiers remain unchanged.

## Public-release boundary

The system can be curated into a standalone public repository, but the current repository is not release-ready: it lacks a license/security/contribution package and contains machine-specific absolute paths and historical execution captures. Publish a sanitized core plus synthetic examples, not a raw copy of the current history. License selection and publication require a separate Human PI decision.
