# Decision 0008 · GPT generation-6 project targets

Status: approved by direct Human PI instruction, 2026-09-27.

## Current project mapping

All new project-owned GPT task packets, role assignments and model selections use:

| Former 5.6 target | Current target | Project responsibility |
|---|---|---|
| `gpt-5.6-sol` | `gpt-6-sol` | scientific, visual and high-rigor review |
| `gpt-5.6-luna` | `gpt-6-luna` | fast bounded routine work when a GPT model is appropriate |
| `gpt-5.6-terra` | `gpt-6-astra` | architecture, complex planning and consequential exceptions |

There is no project-approved `gpt-6-terra` target. The responsibility moves to Astra rather than inventing an unavailable alias.

## Evidence and runtime boundary

This decision changes current project intent and future packet routing. It does not prove that an external harness is configured, authenticated, live or actually served the requested model. Each future task records the requested model and available runtime identity; inability to obtain the required GPT-6 capability yields `HELD` or `UNCERTAIN`, not silent fallback to GPT 5.6.

AT02 capture files retain their historical `gpt-5.6-sol` observations. They are evidence of past configuration, not current routing, and must not be rewritten to manufacture a migration history. External DSH, user-level configuration and provider accounts remain unchanged by this project-internal decision.

The current AT11 future scientific reviewer target is `gpt-6-sol`. Packet readiness remains separate from scientific execution authorization and reviewer qualification.
