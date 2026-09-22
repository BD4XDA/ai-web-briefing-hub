# ASTRA TIME 05 — 最终交接

**C1 = NOT PROVEN；C2 = UNCERTAIN；P5 = UNCERTAIN；P6 = YELLOW。**
最新 committed checkpoint：**20260922T091418-c3831eb34892**。
这是项目自身的 checkpoint 提交，不是 Git commit 或发布。AT05 已结束。

Canonical root：C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os
恢复时读取 AGENTS.md、PROJECT.md，再运行 `python tools/foundation.py show`；若已有更新的有效 checkpoint，以其为准。

## 实验与结果

AT05 启动了恰好一个新的 Codex CLI worker，使用 ephemeral、ignore-user-config、read-only，未使用 resume/fork，也未传入旧聊天。初始输入仅包含项目入口、任务包和一次观察命令。模型沿用用户当前配置 gpt-6-astra；它是单独的 CLI invocation，不是旧 P5 worker。

新任务只是从 canonical 输入生成包含项目身份、release、冻结文件数量和观测 checkpoint 的小摘要；没有重跑 AT03 索引任务。任务包、代码及初始输入的内容和哈希在启动前保存。

worker 的观察命令被策略拒绝，未产生成功的命令执行或恢复观察结果。CLI 返回了 blocked 描述，而非任务摘要。一个独立 DSH / DeepSeek Flash 会话审阅了证据包，返回 FAIL、置信度0.86、completed、零工具调用。自动门槛给出 FAIL，并阻止正式摘要写回。

| 主张 | 最终状态 | 精确边界 |
|---|---|---|
| C1 Fresh Successor Recovery | NOT PROVEN | 新 invocation 有记录，但恢复命令没有成功执行；未证明从项目记忆恢复。不是断言 Foundation 永远不能恢复。 |
| C2 Automatic Acceptance | UNCERTAIN | 自动阻止写回已发生，但任务脚本把 error 事件误归类为额外工具动作，不能据此证明 FAIL／UNCERTAIN 分类正确。 |
| P5 Autonomous Work Loop | UNCERTAIN | 不晋升为 PROVEN；旧 AT03 证据也未被追溯修补。 |
| P6 Scale Gate | YELLOW | 未形成扩大普查的充分证据，也未证明阻断工作的 Foundation 缺陷。 |

自动脚本先提交了 **20260922T091207-ca38de8b3e1a**，其中 C2 自报 PROVEN。协调者检查实际代码与审阅异常后，以最新 checkpoint 将该元主张降为 UNCERTAIN。原自动判定 FAIL、所有原始文件和原 checkpoint 均保留；没有修改门槛、重跑实验或把 FAIL 变成 PASS。

## 可核查证据

- [预声明任务包](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/packets/at05-recovery-01.md) 与 [机器任务包](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/packets/at05-recovery-01.json)。
- [启动前内容／哈希绑定](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/prelaunch-binding.json)、[原始启动输入](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/launch-input.json)、[进程身份／时间／退出记录](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/worker-execution.json)。
- [原始 CLI stdout](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/worker.stdout)、[原始 stderr：含 blocked by policy](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/worker.stderr)。
- [机械验证结果](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/deterministic-validation.json)、[独立模型响应](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/review-response.json)、[模型执行记录](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/review-execution.json)。
- [自动门槛结果](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/automatic-acceptance.json)、[自动提交结果](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/terminal.json)、[协调者例外判断](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/EXCEPTION-JUDGMENT.md)。

DeepSeek 审阅的是提供的执行证据，不是独立获取机器状态或执行 worker。请求的模型名称不等于独立认证模型身份。

## 实际发现与 UNKNOWN

1. **F4 执行阻断**：stderr 直接记录观察命令被策略拒绝。具体适用策略的来源与配置原因尚未定位；未绕过拒绝。
2. **F6 任务适配脚本缺陷**：技能上下文预算警告是 error 事件，却被算作额外工具动作。安全阻止写回可见，但分类语义不可靠。没有修改该脚本。
3. **F5 证据包缺口**：模型审阅包没有包含原始 worker.stderr，因此审阅者无法看到策略拒绝的直接证据。其“禁用审批与自动拒绝相矛盾”的推论不被接收；两者可以同时成立。未追加模型审阅。
4. worker 实际加载的完整上下文、模型服务内部状态、所有 OS 读取以及精确底层请求次数仍不可独立确认。CLI stderr 显示一次内部采样重试；只能确认一次 worker invocation，不能认证 packet 中的模型调用预算完全满足。
5. 完整恢复流程、成功写回分支及其他门槛分支均未在本轮证明。新线程名字本身不构成恢复证明。

这些是执行限制、观测／证据缺口和任务脚本缺陷。没有据此认定 Foundation 架构缺陷。

## 保护现状与下一步

Foundation v0.1 实现、协议与 schema 未改；仅新增 AT05 task packet、观察／门槛脚本、证据、交接和 checkpoint。旧证据未覆盖。P3/P4 保持有效关闭，Vela／Janus／Seshat 继续 HELD（Seshat0.78仍低于0.80）。无普查扩大、材料移动、重装、凭据修改或科学流程启动。

**下一项授权范围：仅准备一个最小诊断／修复提案**，针对适用 CLI 策略的只读定位、error 与 tool-action 的明确区分、原始 stdout/stderr 的证据绑定。不得以此自动授权修复或新一次 worker；新的执行需要单独有界授权。AT05 不再继续。

下轮不得重复 AT05、AT03-loop-01、三个 pilots、P0–P2、已接受测试或本次模型审阅；不得降低阈值、修改原证据或重试到绿。

自动审批审核拒绝了 worker 的只读观察命令；原始原因是“blocked by policy”。拒绝与证据缺口已经保留，未绕过。

