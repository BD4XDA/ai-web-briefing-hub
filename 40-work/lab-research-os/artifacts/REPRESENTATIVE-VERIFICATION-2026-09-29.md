# Representative infrastructure verification — 2026-09-29

## Outcome

One real Daily Paper production trial and one bounded pass over currently managed infrastructure were executed under Decision 0015. Core control-plane and routing checks pass; DeepSeek headless is live; the public release is draft-ready; the Daily Paper run is scientifically honest but cost-inefficient and incomplete. State-gated scientific workloads were not fabricated merely to claim integration.

## Results

| Path | Result | Direct evidence |
|---|---|---|
| Foundation/checkpoint contracts | PASS | `python -m unittest discover -s tests -v`: all 36 tests pass |
| GPT-6 model routing | PASS | `python tools/model_routing.py validate`: 3 routes, policy 2026-09-27 |
| Capability registry | PASS | `python tools/capability_registry.py validate` |
| Current task packet | PASS | `daily-paper-readiness-v3.json` passes packet/root validation; an earlier attempt mistakenly sent a checkpoint-state file to the packet validator and was not repeated |
| Codex App coordination | PASS, bounded | Existing Daily Paper thread was messaged, waited, read and its two existing automations updated; no duplicate thread or automation was created |
| Daily Paper issue 022 | PARTIAL | Two lawful SCI PDFs retained; Chinese full text read online but original PDF blocked; no formal issue, notes or index entry published |
| Daily document/visual pipeline | NOT REACHED | Upstream Chinese original-PDF gate failed; no synthetic note was manufactured to force document PASS |
| Web/literature access | PARTIAL | Primary/public sources worked for two PDFs; one publisher path hit close/429/safety challenge and stopped after three equivalent attempts |
| DSH core and lab-headless profile | PASS | `dsh --version` = 0.1.7-rc.2; one live headless step returned exactly `DSH_COST_SMOKE_OK` |
| DSH usage | OBSERVED | 2,483 uncached + 5,504 cache-read input tokens, 10 output tokens; total 7,997 |
| Public-release draft | DRAFT_READY | 33 allowlisted files; five release tests pass; final build correctly held by `license_not_selected` |
| Google Drive connector | HELD | Read-only profile health check returned `USER_NOT_LOGGED_IN`; no file was listed or read and no retry was justified |
| R runtime | NOT READY | R analytics Skill is installed; `Rscript` is not available on PATH |
| SPSS runtime | NOT READY | SPSS Skills are installed; no SPSS runtime/command was found |
| Exa and legacy DSH router | BLOCKED, NOT RUN | Existing registry block retained; verification authorization did not justify enabling obsolete/blocked routes |
| Figure/manuscript/data workloads | STATE-GATED | No `DATA_READY`, `QAQC_PASS`, figure or manuscript milestone; synthetic scientific execution remained prohibited |

## Cost finding

The issue-022 Daily Paper turn ran as `gpt-6-luna/medium` and reported 20,790,654 input tokens (19,896,832 cached), 76,827 output tokens and 20,867,481 total, with 134 model steps, 130 tool calls and three context compactions. It produced two usable SCI PDFs, one fully readable but download-blocked Chinese candidate, and an exact continuation point; B=5, C=5, EVR=1.0. This is a resource anomaly even though Astra and subagents were not used.

The repair is operational rather than rhetorical: the existing heartbeat and private Skill now use the global three-attempt budget, passive cost telemetry, a Luna/low parent gate and a compact Daily Brief cost section. A subsequent settings turn directly observed `gpt-6-luna/low`. A non-low future heartbeat must fail closed before a long search.

The shared local cost ledger records six workloads. Known token use totals 20,875,478; four other local/connector records correctly use `unavailable` rather than invented precision. There was one stop-rule event, zero high-reasoning calls, and no Astra use. Mean recorded EVR is 1.889; this aggregate is a routing aid, not a scientific-quality score.

## Remaining decisions and continuation

- Daily Paper: either place a valid publisher PDF for the current Chinese candidate at the recorded issue-022 continuation path, or allow the next Luna/low run to replace it. Do not repeat the three failed access paths.
- Public release: Human PI still needs to choose a license before a final public package can be built or published.
- Google Drive: connect the account only when explicit cloud collaboration is desired; local canonical state remains the fallback.
- R/SPSS: install or bind a runtime only after a real data/analysis trigger and an analysis plan exist. Installed Skills alone are not execution capability.
