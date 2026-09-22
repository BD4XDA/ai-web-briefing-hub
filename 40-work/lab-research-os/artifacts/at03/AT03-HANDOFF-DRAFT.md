# AT03 handoff draft（P3/P4 → P5/P6）

## 当前结论

P3 已完成评估闭环，但三个 pilot candidate 均为 `HELD`，没有任何 inventory candidate 被集成。Collection 完成、deterministic input validation、DeepSeek evidence review 和最终 bundle gate 是分开的状态。P5 fresh-owner reversible loop 尚未完成，P6 scale decision 仍待定；本文不推断二者结果。

P3 closure：[P3-PILOT-CLOSURE.md](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at03/P3-PILOT-CLOSURE.md)。最终 gate：[AT02 acceptance.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at02/verification/acceptance.json)。初次独立 review：[review-parsed.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at02/verification/review-parsed.json)。

## 三个 pilot 的实际状态

| Pilot | 已观察事实 | 独立 review / gate | 当前处理 |
|---|---|---|---|
| Vela / A | 5 records、5 evidence；缺失 `evidence` 键后仅用既有 evidence 做过一次组装修正；`schema_version` 仍是额外顶层键。A 还保留 stale checkpoint claim 与 CLI lookup failure。 | DeepSeek `FAIL`, confidence `0.62`；最终 `HELD`，`Unknown or missing bundle fields`。 | 保留 initial/correction/raw evidence；不再 recollect 或 repair。本轮 worker queue 仅记录 exact shape/checkpoint discrimination，未证明可集成。 |
| Janus / B | 5 records、17 evidence；selection policy 文本写 18 files，实际 `files` 数为 17；repo metadata 与直接 git root 不一致。worker 带有既有对话上下文。 | DeepSeek `UNCERTAIN`, confidence `0.60`；最终 `HELD`，`Integration held: unresolved verification`。 | 不接受 fresh-owner resume claim；不再 repair/recollect。错误 path/count 不得指导写入。 |
| Seshat / C | `00_总索引` bounded metadata capture：1 个 index 文件、2 records、2 evidence；项目关联为 unknown，未读 paper bodies/PDF。 | 初次 `UNCERTAIN 0.65`；stage clarification `PASS 0.78`、无 anomaly；最终仍 `HELD`（gate 要求至少 0.80）。 | 保留 provenance 与 bounded limitation；不降低阈值、不再 retry。 |

C clarification 的实际文件：[acceptance.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at02/verification-C-clarification/acceptance.json)、[review-parsed.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at02/verification-C-clarification/review-parsed.json)、[dispatch capture](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at02/verifier-dispatch-clarify-C-execution.json)。直接 discrimination receipt：[discriminating-receipt.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at02/verification/discriminating-receipt.json)。

A 的 preserved files：[candidate-bundle.initial.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at02/pilot-A/candidate-bundle.initial.json)、[candidate-bundle-correction.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at02/pilot-A/candidate-bundle-correction.json)。B 的 collection：[collection.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at02/pilot-B/collection.json)。C 的 primary capture：[raw-capture.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at02/pilot-C/raw-capture.json) 与 [index-snapshot.md](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at02/pilot-C/index-snapshot.md)。

## P4 学习与边界

[P4-FAILURE-LEARNING.md](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at03/P4-FAILURE-LEARNING.md) 与 [FAILURE-TAXONOMY.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at03/FAILURE-TAXONOMY.json) 记录了实际观察：A delivery shape 为 F7；B repo/count contradictions 为 F1/F5；A CLI lookup 为 F4；C stage/review context 与 verifier precheck omission 为 F2/F6；早期 manual transcription 为继承的已解决证据教训。F8 concurrency corruption、F9 capability mismatch、F10 frozen Foundation defect 均未被证明。

Agent-harness 的 `model_id` applicability、instruction-memory richness、report ownership、parallel checkpoint behavior 和相关 schema 设计仍是 hypotheses/candidates，不能在本 handoff 中升级为 redesign 或事实。Janus 的旧对话上下文是 test-design limitation；不能写成 fresh-owner success。

## 已知基础设施状态

[INFRASTRUCTURE-MAP.md](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/INFRASTRUCTURE-MAP.md) 明确区分 configured、tested 与 current live。DSH web/router 在最近观察时 3080 为 `NO_LISTENER`、web offline；既有 recovery overlay 只允许一次受限恢复检查，不能宣称持久在线。既有 scientific Sol review 为失败/`CHECKPOINTED_FAILURE`，保持 untouched；不能把历史 smoke 或模板配置当作本轮科研审阅通过。Exa 恢复记录是临时证据，持久 startup ordering 尚未修复。

Foundation v0.1 仍冻结；本阶段没有 Foundation contract/schema 基线改动。发生的范围仅包括 task-specific verifier 的最小 precheck/stage clarification、pilot derived evidence 与本文档。生产 census、完整语料、通用 router/compiler、Outdex、resume/CV、War Thunder 与新的 permanent agent 均不在范围。

## P5/P6 状态（待填）

- **P5 fresh-owner loop：`PENDING`。** 允许的范围是基于已接受 frozen Foundation manifest 的一个小型、可逆、一次性 loop；held A/B/C records 不得 promotion。需要由 fresh-context owner 产生 primary capture、独立 review、原 gate 与一次 writeback/checkpoint。结果可能是 completed、failed 或 unknown；本 draft 不预判。
- **P6 scale decision：`PENDING`。** 在 P5 receipt 与 checkpoint 之前不作 GREEN/YELLOW/RED 或 scale-up 判断。未证明一般 autonomous research、drive-wide census 或可靠 broader census。

## 回滚与连续性

回滚采用非破坏方式：保留 A 的 initial/corrected copies、原始 captures、review responses 与 held bundles；任何后续状态通过新 checkpoint / 新 artifact 表达。不得删除、覆盖、清空 legacy、source data、credentials、lock 或旧 evidence。若 P5 失败，保留失败和最小 next check，不以重复 retry 制造 green。

Failure record：[FAILURE-TAXONOMY.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at03/FAILURE-TAXONOMY.json)。P3/P4 的完整 evidence references 也见 [packets/at03-p3-closed.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/packets/at03-p3-closed.json) 与 [packets/at03-p4-closed.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/packets/at03-p4-closed.json)。
