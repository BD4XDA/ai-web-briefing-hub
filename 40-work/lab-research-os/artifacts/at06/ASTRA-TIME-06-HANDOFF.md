# ASTRA TIME 06 — 诊断交接

最新 committed checkpoint：**20260922T093640-7d71f54b9b3b**。
状态保持：**C1 NOT PROVEN；C2 UNCERTAIN；P5 UNCERTAIN；P6 YELLOW**。
本轮按后发的“诊断与提案”授权结束；没有实施先发草案中的修复或再验证。

Canonical root：C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os。恢复时读取 AGENTS.md、PROJECT.md，执行 `python tools/foundation.py show`；更新的有效提交优先。checkpoint 是项目内部提交，不是 Git commit。

| 问题 | 诊断 | 缺陷边界与证据 |
|---|---|---|
| F4 策略拒绝 | **INSUFFICIENT_EVIDENCE**；拒绝正确或错误仍UNKNOWN | 原始 stderr 确认 Codex CLI exec_command 创建进程前返回 blocked by policy。缺失匹配规则、评估输入及历史有效策略；当前配置和help不能代替。只读日志定向查询没有取得进一步规则记录。 |
| F5 证据包绑定 | **已证明局部组装遗漏** | stderr在review前已存在，hash正确；package仅包含execution hash及事件投影，没有stderr正文。reviewer工具禁用，不能凭hash取得拒绝证据。 |
| F6 事件语义 | **已证明局部适配缺陷** | item.type=error的技能预算警告被否定式类型筛选归入other_tools，使no_other_tool=false并影响FAIL；该事件没有证明额外工具动作。 |

F4发生在执行前；F6是其后的结果分类，二者不能混称一个“策略问题”。F5使reviewer看不到已有直接证据，又与二者不同。冻结 Foundation 未证明有缺陷；F5/F6都位于 artifacts/at05/experiment.py，未作修改。F4的可见CLI层不属于Foundation，具体根因仍未定位。

C1未被实际恢复执行所区分，**NOT PROVEN不等于continuity FAILED**。自动写回阻止仍是有用证据；但不能仅凭“没写文件”认证C2分类正确。P3/P4与三个HELD pilots保持原状。

## 原始证据与诊断

- [诊断详情：链条、语义、责任、风险](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at06/DIAGNOSIS.md)
- [诊断记录与原文件hash／代码行／受限日志查询](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at06/diagnostic-evidence.json)
- [AT05原始stderr](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/worker.stderr) · [原始stdout](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/worker.stdout)
- [原执行记录](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/worker-execution.json) · [原证据包](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/review-prompt.txt) · [原适配代码](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at05/experiment.py)

静态代码显示observe分支固定读取项目文件及两个明确授权的父级文件，不执行写回／迁移。完整shell/profile/python环境与策略输入并未保存，因此不能把静态只读意图升级为整个进程安全性的完整证明；也不能仅因看起来安全就称拒绝错误。

本轮仅增加诊断、提案、交接和checkpoint；未覆盖历史AT05证据。一次只读诊断委派因额度限制未执行，后续由协调者处理该例外，没有再启其他worker或新successor。

## 最小提案与下一授权

[唯一修复／验证提案](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at06/MINIMUM-REPAIR-PROPOSAL.md) 已列出逐项责任、最小语义改动、证据包绑定、回归风险、回滚、负控和单次新验证设计。

下一步需要**另行明确授权这个有界流程**：
先定向取得F4历史决策溯源；仅修复已证明的F5/F6局部逻辑；做限定离线回归与负控、证据完整性检查、独立证据审阅。只有F4正确策略路径有依据且修复验证被接收后，才单独有条件授权恰好一次新successor。缺原始历史证据时保留UNKNOWN，另拟可观测诊断，不直接重试。

回归须覆盖：原error与缺观察、合法成功、真实拒绝、未知／畸形事件、越界／破坏性负例、原始流缺失／篡改／超限／编码／秘密、低置信度／不完整review、陈旧checkpoint与写回字节不等。所有负控必须保持禁止错误接收，不能用synthetic fixture认证真实任务PASS。

**修复、回归、负控、模型审阅、single revalidation：本轮均NOT_EXECUTED。**
没有策略白名单、权限弱化、阈值降低、Foundation修改、材料迁移或普查扩大。不得重跑AT05、AT03闭环、三个pilots、P0–P2、接受过的测试或AT05review。

AT06到此停止。

