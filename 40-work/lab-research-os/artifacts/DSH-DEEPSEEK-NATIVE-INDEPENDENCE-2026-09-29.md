# DSH DeepSeek-native independence verification — 2026-09-29

Trigger: EVENT (bounded DSH recovery/consolidation task). Scope: DSH itself and its minimal interface
to Lab Research OS. No Foundation, memory, evidence or routing architecture was modified.

## Question

Can a normal DSH worker execution complete without any usable GPT/OpenAI quota, and does DeepSeek
provider/model selection silently fall back to GPT? Answer: **yes, and no.**

## Method

Configuration inspection (`dsh --dump-config`) plus two bounded live DeepSeek headless calls from the
canonical workspace root. The second call is a direct falsification test: the OpenAI environment is
poisoned so that any latent OpenAI dependency would fail closed instead of silently succeeding.

## A. DeepSeek-native headless smoke — PASS

Command (run from `D:/项目仓库/赛博课题组/40-work/lab-research-os`):

    DSH_PERMISSION_MODE=read-only dsh --profile lab-headless --json "<prompt>"

| Item | Observed |
|---|---|
| Requested provider / model | `deepseek-official` / `deepseek-flash` (`agent-default-model`, inherited from `dsh-base`) |
| Actual serving identity | `source.kind = "model"`, `provider = "deepseek-official"`, `model = "deepseek-flash"`, `replayState.response.kind = "deepseek-messages"` |
| Profile | `lab-headless` |
| Workspace (recorded cwd) | `D:\项目仓库\赛博课题组\40-work\lab-research-os` |
| Exit state | 0; `turn_end` reason `completed` |
| Output | `DSH_DEEPSEEK_NATIVE_OK` (exact match, no extra text) |
| Usage | 7,851 input (384 cache-read) / 10 output / 8,245 total |
| Session | `session-a7c34294-2528-4537-a3de-804505ed4e29` |

The serving identity is read from the session log's own `assistant/message` record, not from a model
alias. Label: **authenticated provenance**, not alias inference.

## B. GPT-unavailable independence — SUPPORTED (live, not merely inspected)

An equivalent call was executed with the OpenAI environment deliberately poisoned:

    OPENAI_API_KEY=sk-INVALID-SENTINEL-FOR-INDEPENDENCE-TEST
    OPENAI_BASE_URL=http://127.0.0.1:9/dead
    CODEX_API_KEY=sk-INVALID-SENTINEL
    OPENAI_ORG_ID=deadbeef

Result: exit 0, exact output `DSH_GPT_INDEPENDENT_OK`, `turn_end` reason `completed`, and the same
authenticated provenance `provider = "deepseek-official"`, `model = "deepseek-flash"`.
Usage: 2,727 input / 5,504 cache-read / 11 output / 8,242 total. Session `session-c554564b-2c6d-43ca-adb8-b9de6dd6ac85`.

Supporting facts from the same environment:

- `OPENAI_API_KEY` is absent; there are **no** OpenAI/Codex/GPT/Azure environment variables at all.
- `$DSH_HOME/.credentials.yaml` holds exactly two references: `DEEPSEEK_API_KEY` and `OLLAMA_API_KEY`.
- No quota was consumed and no credential was broken; the sentinels are inert strings.

Because GPT-unavailable was simulated by hostile environment rather than by exhausting a real quota,
this is recorded as **SUPPORTED by direct live execution**, which is stronger than inspection-only and
weaker than a true quota-exhaustion rehearsal (which the task prohibited).

## C. Workspace safety — PASS, one note

- `D:/20_代码项目/赛博课题组` resolves to `D:/项目仓库/赛博课题组`; `git rev-parse --show-toplevel`
  returns `D:/项目仓库/赛博课题组`. Single repository, single Source of Truth, no second checkout.
- Both live calls recorded the canonical path as their cwd.
- **Note (not a defect):** the DSH workspace registry (`storages/workspace.json`, id
  `e4c2f3c7-0d47-4fbb-86d2-2e1ac0fae9d1`) still lists the workspace as
  `D:\20_代码项目\赛博课题组` — the compatibility junction, i.e. the *former* path. Because the
  junction resolves to the canonical directory, this creates no state divergence, but it is exactly
  the "new configuration must use the canonical path" risk already recorded in `CHECKPOINT.md`. There
  is no duplicate registry entry at the canonical path, so no second workspace exists.

## D. Clean-profile Web path — PASS

`lab-research` booted on `127.0.0.1:3081`: unauthenticated probe `401`, token flow `303 → 200`,
served `<title>DeepSeek Harness</title>` with the `id="root"` app mount (34,128 bytes). The test
server was stopped afterwards; port 3081 is closed and no `cloudflared` process exists. The Web model
turn was **not** re-executed — `dsh-base` supplies the same `agent-default-model` row, the headless
path already proves the model route, and the DSH-017 report already covers a live Web turn.

## Dependency inspection (configuration evidence)

From `dsh --dump-config` on both clean profiles:

- `lab-headless` composes `agent-default-model` = `deepseek-official` / `deepseek-flash` and **no**
  provider row other than DeepSeek; `llm-pi-ai` is present with no config, i.e. dormant (zero routes).
- `lab-research` adds only `llm-pi-ai` → `local-ollama` (`http://localhost:11434/v1`, model
  `qwen3-vl:latest`). Its `api: openai-completions` is the **wire-protocol name** for an
  OpenAI-compatible local endpoint; it is not the OpenAI service and carries no OpenAI credential.
- `web.searchProvider` is `deepseek-official` with `apiKeyEnv: DEEPSEEK_API_KEY`; the DeepSeek search
  route also consumes no OpenAI quota.
- Cross-vendor delegation rows `tool-subagent-codex` and `tool-subagent-claude-code` are composed but
  `disabled: true` in both profiles. They are dormant, so a Codex/Claude CLI outage cannot break a
  DeepSeek worker.
- No `openai` provider row, no `codex` route, and no tunnel/`remote-web-ui` row exists in either clean
  profile. GPT/OpenAI integration remains optional and separately governed, as required.

## Defects actually found

**None in DSH.** The DeepSeek-native path was intact before this task; no DSH repair was required and
none was performed. Two adjacent findings are recorded rather than repaired:

1. **Claude Code PATH defect (outside DSH scope, not repaired).** `C:/Users/ASUS/.claude/settings.json`
   sets `env.PATH` ending in a literal, unexpanded `%PATH%`. Because Claude Code injects that value
   verbatim, the shell PATH is *replaced* rather than extended. Consequences inside Claude Code Bash
   sessions: `C:\Windows\System32` is missing (no `cmd.exe`, `reg.exe`, `netstat.exe`,
   `powershell.exe`) and `%APPDATA%\npm` is missing, so a bare `dsh` returns exit 127. This does **not**
   affect DSH execution: `dsh-web.cmd` invokes `%APPDATA%\npm\dsh.cmd` by absolute path, and this
   verification used the absolute path successfully. No project-owned script invokes a bare `dsh`
   (only prose references "dsh headless text runner" appear in evidence files). Deliberately not
   repaired — it is the Claude Code harness configuration, not DSH, and changing it affects every
   project on this machine. Suggested minimal fix for Human PI approval: drop the trailing `;%PATH%`
   token, or remove the `PATH` override so the real system PATH is inherited.

2. **Clean-profile hardening asymmetry (documented, not repaired).** `lab-research` disables
   `session-projection-cache` (the DSH-017 report records a Windows failure on historical
   `agent-team:<id>` filenames); `lab-headless` inherits it **enabled** from `dsh-base`. No failure was
   observed: both headless runs wrote valid, well-formed cache records
   (`storages/session_projcache/sessions/session-a7c34294-….json`, `session-c554564b-….json`). The
   headless bundle mounts no Host/HTTP/Web layer and never enumerates a session listing, so the known
   trigger is not on its path. With no direct evidence of failure, disabling it would be a speculative
   change and was not made. Recorded as a reserved item should a real headless failure appear.

## Legacy components intentionally left isolated

| Component | State | Basis |
|---|---|---|
| Legacy `web` profile | LEGACY, not qualified | Retained on disk; not in either clean profile's bundle list |
| `@softspark/dsh-codex` adapter | INCOMPATIBLE, isolated | Present only under `profiles/web/node_modules`; rejected by the 0.1.7 exact peer guard (DSH-017) |
| `dsh-sol-luna-router` | BLOCKED, isolated | Registry marks it watch-only/blocked; contains legacy GPT-5.6 and retired DeepSeek ids; excluded from clean profiles |
| `exa` MCP route | BLOCKED, isolated | Legacy web-profile row only |
| Legacy web UI plugins (task-board, pet, voice, model-switch, …) | LEGACY, isolated | Confined to the legacy `web` profile; their failure classes do not reach the clean routes |

Triage result: the clean qualified routes already cover the current bounded workloads, so none of
these was repaired. Repairing them would add compatibility and regression cost without addressing a
current failure.

## Regression and safety

| Check | Result |
|---|---|
| `python -m unittest discover -s tests` | 36 tests, OK |
| `python tools/model_routing.py validate` | PASS — policy `2026-09-27`, 3 routes |
| `python tools/capability_registry.py validate` | PASS — registry `1.0.0` |
| GPT-routing policy | Unchanged; `config/model-routing.json` not touched |
| Credentials | Unchanged; no credential read, written or rotated |
| Sessions / attachments / research data | Not copied, moved, cleared or deleted |

## Rollback surface

- `C:/Users/ASUS/.dsh/backups/dsh-core-upgrade-20260929-121654/` — pre-upgrade snapshot including
  `settings.yaml`, `.credentials.yaml` (a credential snapshot — handle as sensitive), `agent_team.json`,
  `dsh-web.cmd`, the `web` profile and `dsh-sol-luna-router`, with `upgrade-manifest.json` recording
  `prior_dsh_version 0.1.1-rc.2` and the rollback command
  `npm install -g @deepseek-ai/dsh@0.1.1-rc.2`.
- No write was made to any DSH configuration, profile, credential or session store by this task.

## Remaining UNKNOWN / BLOCKED

- **UNKNOWN:** whether the retired `settings.yaml` keys `describe-image` (DeepSeek vision endpoint) and
  `llm-deepseek.models` (custom vision-capable model list) are wanted under the clean profiles. They
  were not migrated by DSH-017, which is consistent with the clean profiles' declared text/headless/Web
  scope, and the retired default id `deepseek-v4.1-flash-expires-on-0910` had already expired on
  09-10. No visual workload currently requires them. This is a Human PI scope question, not a defect.
- **NOT PROVEN:** true quota-exhaustion behaviour. Independence was proven by hostile environment
  rather than by consuming or exhausting any quota, which the task prohibited.
- **RESERVED:** the `lab-headless` projection-cache asymmetry above, pending any real headless failure.

## Gate result

The DeepSeek-native execution path is independently live, carries no live GPT/OpenAI dependency, does
not silently fall back to GPT, and is recoverable from a named backup. No DSH repair was needed.
