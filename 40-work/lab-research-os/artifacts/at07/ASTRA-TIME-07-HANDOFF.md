# ASTRA TIME 07 — 最终交接

最新 committed checkpoint：**20260922T095401-23b9cefe804f**。
**F4 INSUFFICIENT_EVIDENCE；F5/F6 修复均未通过接收门槛；C1 NOT PROVEN，C2 UNCERTAIN，P5 UNCERTAIN，P6 YELLOW。**
AT07 已按停止条件结束，未启动 successor。

Canonical root：C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os。恢复时读 AGENTS.md、PROJECT.md，运行 `python tools/foundation.py show`；更新的有效 checkpoint 优先。这里的commit是项目checkpoint，不是Git提交。

## 本轮结果

| 项目 | 结果及边界 |
|---|---|
| F4 | 原AT05 thread/time window的受限只读查询仍未取得历史策略规则／评估解释；拒绝正确性UNKNOWN。没有更改配置或以当前策略替代历史证据。 |
| F6局部修复 | 新派生local_repair.py明确区分action、diagnostic、unknown；保留事件顺序与原始信息。缺观察仍禁止接收，gate完成不自证分类正确。 |
| F5局部修复 | 新派生binder绑定真实stdout/stderr正文、字节数、hash、编码及capture receipt；区分空、未采集、缺失、截断、篡改、超限、编码异常与安全保留。已实际用于构建AT07审阅包。 |
| 离线回归 | 一次执行，**9组测试、45条断言记录通过**。包含真实历史事件／流的离线重放及明确标记的synthetic正负例。 |
| 负控 | 枚举范围内通过：未知／畸形事件、越界动作、执行拒绝／超时、缺失／损坏流、不合格review、陈旧checkpoint、字节不等均不允许接收。 |
| 证据完整性 | 本次所列包检查PASS；原始拒绝stderr正文、测试stdout/stderr、receipts、代码、差异及hash均提供。不是所有机器行为的完整性证明。 |
| 独立审阅 | 一次DSH Flash evidence review：报告总结果及F5/F6分项PASS，**confidence=0.72**；completed，tool_calls=0；异常列表非空。 |
| 自动接收 | **FAIL**：低于0.80且异常未清空。F5 REPAIR=FAILED，F6 REPAIR=FAILED，指未通过接收，不是声称离线测试失败。 |
| 采用／回滚 | **DISABLED_NOT_ACCEPTED**。派生模块未接入live dispatch，原AT05文件未覆盖；无需撤销线上改动。代码与失败接收证据完整保留，不采用、不重试。 |

审阅者检查的是提供的执行证据，没有亲自运行测试。它提出的异常／局限保留在原响应中，包括unknown分类、超限流完整性、有限secret screen、capture可信度等。本轮没有补充解释寻求改判、二次review或事后修补。正常接收阈值未变化。

## 证据入口

- [F4定向取证](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/F4-provenance.json)
- [修复范围与局限](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/REPAIR-SCOPE.md) · [局部派生代码](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/local_repair.py) · [责任范围前后对比](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/repair.diff)
- [测试代码](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/test_local_repair.py) · [执行receipt](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/regression-execution.json) · [断言stdout](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/regression.stdout) · [unittest stderr](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/regression.stderr)
- [完整性检查](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/completeness.json) · [实际送审包](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/review-package.json)
- [独立review原响应](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/review-response.json) · [review执行记录](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/review-execution.json) · [自动接收记录](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/review-acceptance.json)
- [最终修复状态](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at07/FINAL-REPAIR-STATUS.json)

## 保留边界与UNKNOWN

冻结Foundation、schema、policy、sandbox、approval、global config均未修改。AT05原程序、prompt、review与结果保持不变。P3/P4和三个HELD pilots保持原状。

派生gate只消费机械观测与scope判定并返回决策，不是policy engine或OS sandbox，也未验证真实文件系统接入。synthetic通过不认证真实恢复。有限秘密模式筛选不是通用秘密检测器。历史F4的有效策略来源仍缺失。

C1未实际恢复受测，NOT PROVEN不能改写为continuity FAILED。C2仅增加了本轮离线分类测试证据，但修复未接收，保持UNCERTAIN。P5不因局部测试通过而晋升。P6保持YELLOW。

## 下一步与停止线

**AT08 successor revalidation 目前不能授权；未准备可执行packet。**
仍需的最小可观测诊断是：取得原拒绝的有效policy来源、原始规范化工具输入、命中规则／决策路径及解释；若历史记录不可恢复，应先另行批准能保存这些证据的诊断设计，而非直接重试命令。

下一项动作必须在单独有界授权下处理已记录的低置信度／异常或缺失F4溯源；不得自动追加review、反复修补到绿。任何后续successor仍须F4路径足够可观测、F5/F6被接收、回归负控与独立验证通过，并预先声明scope/gates/budget。

本轮不再修改、测试或调用模型；不重复AT05、旧闭环、pilots或已接受Foundation测试，不扩大普查、不迁移、不启动科学流程。

