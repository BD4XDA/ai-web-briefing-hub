# ASTRA TIME 基础设施地图

更新：2026-09-21。本文是已有证据的压缩地图，不是新的诊断结果；没有启动模型、重跑服务或重测路由。

## 证据边界

主 checkpoint：[ASTRA-TIME-01-P0-CHECKPOINT.md](C:/Users/ASUS/Documents/Codex/2026-09-21/referenced-chatgpt-conversation-this-is-an/outputs/ASTRA-TIME-01-P0-CHECKPOINT.md)，SHA-256 `58C4E6878F3D9A91075380D1E8EFE96B07AF6BA8F61B1B85E28A6B1E4E8BA763`。P0 worker：[p0-health-worker.md](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/evidence/p0-health-worker.md)，SHA-256 `8841C8B01339D0F6177FED23E8920731C82313FFE2DD871FC0C000F1D027FBD2`；对应 JSON SHA-256 `852754D6BA34F6C05F9B13BDCCD741713E8B40AA07B21333AD9E7F06B506A6BD`。继承索引：[inherited-evidence-index.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/evidence/inherited-evidence-index.json)，SHA-256 `882B9BA2D2478330C00E0244875E9A6A01B3FA8995D289F816BAD86281A8FCE8`。原始盘点：[inventory.json](C:/Users/ASUS/Documents/Codex/2026-09-21/referenced-chatgpt-conversation-this-is-an/outputs/evidence/inventory.json)，SHA-256 `B5936A593F50A2A7B2715F01F41956E761097D37985E746AC05E8CE5AAAFFADC`。指令入口审计：[instruction-adapter-audit.md](C:/Users/ASUS/Documents/Codex/2026-09-21/referenced-chatgpt-conversation-this-is-an/outputs/evidence/instruction-adapter-audit.md)，SHA-256 `6D80279ABA58A6168282A6FDDEF296DCCF48C75FF0DBB77064C3245E199B076F`。

## 当前模板、角色与状态

盘点中的 agent 模板是两个 Sol 角色：

| 模板/角色 | 配置目的 | 证据状态 |
|---|---|---|
| Sol 科研审阅员 | GPT-5.6 Sol，高推理，只读；方法、证据链、统计假设、可复现性审阅 | 已配置；不能据此宣称本轮研究审阅完成 |
| Sol 联网科研员 | GPT-5.6 Sol，高推理，只读；通过 Exa 做一手来源核查 | 已配置，绑定 Exa；历史上启动时曾因 Exa 权限报错，后有一次恢复记录 |

盘点中的团队状态是：`Sol 兼容性测试团队` 为 `active`，1 名成员、0 task、0 lease；`Sol 联网科研测试团队` 为 `error`，1 名成员、0 task、0 lease，错误摘要为无法访问 Exa。它们是已有资产，不是新建实验室实现。来源为 `inventory.json` lines 3–76，文件哈希见上。

## Model × Harness 能力矩阵

“已配置”来自模板/依赖盘点；“已测试”只表示已有证据文件；“当前 live”是 checkpoint 时的瞬时状态。三列不能互相替代。

| Model / Harness | 已配置 | 已测试的证据 | 当前 live / 限制 |
|---|---|---|---|
| DeepSeek Flash（DSH） | DSH `0.1.1-rc.2`；普通文本、工具、子代理、重启恢复路径已存在 | `dsh-smoke.json` SHA-256 `E2D4F2FC1DDF040BAB52DF9100EC247D594464949B80F06964388A0DEA34CFEB`；`dsh-restart-resume.json` SHA-256 `49C3FDE38D65D3284D6C50D5B3A1441CA5EF7CBE730D6EAB271D9C6B15B946E6`，均记录 passed | 文本与恢复证据可继承；不能把历史 smoke 当作当前 web 服务在线 |
| DeepSeek Pro（DSH） | Pro 文本通道存在 | checkpoint 明确有文本调用证据 | 只按 text-only 能力使用；不要把 legacy `sol-auto` 的图像宣传当作可用视觉 QA |
| Codex Sol | Sol 模板已配置 | `codex-sol-smoke.json` 被 checkpoint 列为既有证据 | 本轮科研 run 在 Sol review 处为 `CHECKPOINTED_FAILURE`；不能声称 legacy 的整条 Sol/Luna 链已通过 |
| Claude Flash | Claude Code `2.1.258` | safe-mode Flash 文本调用通过 | 当前可用依据是 Flash 文本；Fable/Opus/Sonnet/Haiku 别名实际映射到 Flash，不能当作异构模型 |
| DSH web/router | 现有 `dsh-sol-luna-router` 与 web profile | router 既有测试为 `70/72` 通过，doctor `17/17`；证据索引含 `router-existing-tests.json` | 不能据 70/72 或 doctor 17/17 宣称端到端通过；3080 当前 `NO_LISTENER` |
| Exa MCP | Sol 联网模板声明依赖 Exa | MCP catalog/团队恢复文件记录曾恢复可用 | Exa retry 只能视为临时恢复；持久启动顺序修复尚未部署 |

## DSH web 故障与精确恢复边界

默认 web 启动失败的已知触发点是 task-board ledger lock 指向 PID `15680`，而该 PID 当前已被 `svchost.exe` 重用。已记录的 `outputs/dsh-recovery.patch.yml` 是 additive overlay，只禁用可选插件 `web-ui-task-board`；原始 lock/config 保留。该 overlay 的作用是让 web 启动/目录查询路径恢复一次，不能修复持久的启动排序问题，也不能证明 3080 会持续在线。

P0 worker 在 `2026-09-21 13:00:46 +08:00` 只读检查 `Get-NetTCPConnection -LocalPort 3080` 得到 `NO_LISTENER`。因此 DSH3080 当前 offline；没有 listener 时不能归因旧 PID，也不能声称旧服务仍在运行。需要 web 访问时，限制在“沿用已记录 overlay 启动一次，再复核 3080”；不要借此重跑完整普查或付费模型流水线。来源为 `p0-health-worker.md` lines 12–20 与 `p0-health-worker.json` lines 39–50。

## 方向变化

- 从“重新诊断/重启整套链路”改为继承 checkpoint：先读 P0 worker 与当前 checkpoint，再按 P0→P1→P2 顺序推进。
- 从覆盖旧配置改为 additive recovery overlay；保留原始配置、凭据、lock、source data 与 Outdex。
- 从把工具状态当作持久服务改为瞬时状态声明：每次新 turn 后，旧的 tool-hosted web server 都必须重新确认。
- 从把 Exa 一次恢复当成稳定能力改为“临时 retry 已见证，持久顺序修复未部署”。
- 从把模型别名当成不同模型改为按实测底层 Flash 记录 Claude Fable 等别名。
- 科研 run 保留 packet/draft/checkpoint，从 Sol review 的 `CHECKPOINTED_FAILURE` 恢复；不重读完整原始语料。

## P0 / P1 / P2 残余项

| 阶段 | 已有结果 | 残余项 |
|---|---|---|
| P0 | 核心 smoke、restart/resume、API/team 历史证据可继承；worker 结果 `PASS_WITH_BLOCKED_REVIEW` | 3080 offline；Sol review 因 stream disconnect/usage limit 阻断；web 与 API 状态仍需分开陈述 |
| P1 | 指令入口已审计：Codex `AGENTS.md` canonical；Claude `CLAUDE.md` auto-discovery 已由本地 help 验证；DSH 以实际 `dsh-agent-instructions` 源码发现 `AGENTS.md`/`CLAUDE.md`，不假定 `DEEPSEEK.md` 自动加载 | `@import` 未由本地官方 help/doc 验证；DSH 持久 startup ordering 未修复；router 尚有 2 个 Windows path 测试失败 |
| P2 | 本地图与证据索引可作为后续工作入口 | 需要在不清空 legacy 的前提下完成 handoff/evidence contract、bounded census pilot 与科研 review 恢复；不把未测的整链能力写成已通过 |

## 项目边界

Outdex 保持 untouched；简历、resume project、War Thunder 后置。本文只描述已在证据中出现的角色、模型、服务与限制。没有证据的“当前在线”“整条 Sol/Luna 链通过”“Fable 为独立底层模型”等说法均不成立。

## 证据缺口

尚缺一个持久启动排序修复的验证记录、3080 当前重启后的新鲜 listener 证据、router 两个 Windows path 测试的修复证据，以及 Sol review 从 checkpoint 恢复后的新鲜审阅结果。本文没有补做这些验证。
