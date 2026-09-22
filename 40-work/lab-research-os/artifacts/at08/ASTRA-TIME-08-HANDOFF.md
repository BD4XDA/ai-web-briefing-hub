# ASTRA TIME 08 — 裁定与设计交接

最新 committed checkpoint：**20260922T100447-a65b69dbf2c6**。
**下一门槛：NOT READY。建议：C — EVIDENCE-ONLY IMPROVEMENT JUSTIFIED。**
C1 NOT PROVEN、C2 UNCERTAIN、P5 UNCERTAIN、P6 YELLOW 保持；Foundation 未改。

Canonical root：C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os。下一 owner 读 AGENTS.md、PROJECT.md，再运行 `python tools/foundation.py show`；若有更新有效提交，以其为准。checkpoint是项目内部提交，不是Git发布。

## AT07结果不改判

9组／45断言通过不等于修复接收。原review报告PASS、confidence0.72、异常列表非空；原自动接收FAIL正确，F5/F6继续DISABLED_NOT_ACCEPTED。
AT08没有清空原异常、重算分数、复测、修补、采用代码、再次审阅或启动successor。

## 逐项裁定

分类：A=实质接收阻断；B=重要但不阻断所述离线范围的局限；C=预期范围限制；D=重复／派生。每项完整原文、受影响claim、原证据、缺口、false-acceptance风险、采用YES/NO/UNCERTAIN及最小下一检查，均在[逐项机器记录](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at08/ANOMALY-ADJUDICATION.json)。原文直接从原review解析提取，未人工改写。

| ID | reviewer主题 | 类别与裁定 |
|---|---|---|
| A1 | unknown只产生UNCERTAIN而非FAIL，因此不阻止 | C。其“不阻止”子句与代码矛盾：UNCERTAIN时writeback_allowed=false，原负控也记录false。未来类型覆盖有限属于范围限制。 |
| A2 | 超大流无内容／hash绑定，不能完整验证 | C。OVERSIZED保持complete=false；它拒绝范围外输入，不会伪称完整。无需无界流支持。 |
| A3 | 正则秘密筛选有限 | A，针对未来采用前的证据缺口。边界／非法编码输入已拒绝，但未列出的秘密格式确不能普遍识别。未证明本包泄密；需限定数据来源、可发送类别与安全保留路径，否则可能把字节完整误当可安全发送。是否安全采用仍UNCERTAIN。 |
| A4 | 文档未写无异常门槛，代码更严格 | D。原scope末段明确包含no-anomaly；审阅摘录省略该词。未发现所述不一致。原门槛照常保持。 |
| A5 | 空流可能其实是被抑制流 | B。绑定器区分EMPTY/NOT_CAPTURED；hash不能证明采集诚实。历史已知collector和receipt支持其有界声明；未来真实采集过程仍需绑定，不能只填True。 |
| L1 | synthetic没有证明真实恢复／live集成 | C。正确的范围限制；没有把fixture晋升为C1/P5证据。 |
| L2 | F4未解决 | A。阻断successor，不等于局部分类／绑定代码有缺陷。 |
| L3 | 只做离线fixtures，没对live模型输出检查 | D。与L1重复；此外review_once确已将真实AT07响应送入同一gate并拒绝。但不证明全部live分支或successor集成。 |
| L4 | 包内hash／receipt不能排除恶意producer | D。与A5的信任边界重复；没有恶意造假证据，不新增认证架构。未来producer绑定仍是前提。 |
| L5 | reviewer没有独立重算每条断言 | C。review的职责是审阅已提供执行证据，不是独立执行；不能反向宣称它证明测试器本身正确。 |
| L6 | scope_by_action来自输入，不是policy决策 | B。符合局部gate范围，但未来调用方必须将值绑定到实际动作／路径／策略证据，不能以随手填True替代。 |

**真正仍阻断下一步的条件**：原接收门槛未满足；F4决策路径不可观测；未来输入安全范围、采集生命周期和scope来源未建立。后几项可能导致错误接收，不能仅当“泛化不足”放过；目前优先补有界证据，尚无依据要求普遍秘密检测或重写policy引擎。

## F4历史可恢复性

**HISTORICAL_F4_PROVENANCE = NOT CURRENTLY RECOVERABLE**，限定于已检查的授权来源。
AT05 raw stderr只保留拒绝文本；stdout没有规范化请求／规则决策。AT06与AT07精确thread/time-window查询为空；ephemeral启动是线索，不是所有日志永久消失的证明。没有出现具体的新归档／审计来源，所以AT08不重复查询同一源，不查无关会话或凭据，也不以当前config补写历史。

不使用全局永久UNRECOVERABLE。仅在找到具体新来源后重开有界历史取证。

## 未来观测与下一证据包

[最小F4观测设计](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at08/F4-OBSERVABILITY-DESIGN.md)规定：在实际策略评估边界记录原请求→规范化请求、有效策略来源／版本／非秘密hash、命中规则或决策路径ID、结果与解释、UTC／序列、session／process／request关联，再绑定执行或拒绝及原始流。拒绝前未创建子进程就记录null，不伪造恢复轨迹。

必要字段无法取得即F4 UNCERTAIN；不猜默认策略、不放行、不重构旧事件。配置只取必要非秘密字段；秘密或被保留的字段明确不完整，不能用删改版本冒充精确原输入。当前harness是否支持这些观察点尚未建立，本文件不声称已有hook/API。

[下一接收包设计](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at08/NEXT-ACCEPTANCE-DESIGN.md)要求：
- 复用既有绑定的回归与负控，不为安心重跑；
- 补齐实际producer、输入安全范围、capture状态与scope值的来源；
- 所需原流正文、字节数、hash、编码、EOF／截断／安全保留及投影引用齐全；
- 对新观测职责只做必要的缺字段／错身份／错hash／未知安全／拒绝等负控；
- 未满足前提不安排review；之后仍须单独授权，阈值0.80、completed、零工具、异常阻断规则均不变。

建议C并不是修复已接收，也不是保证下次分数更高。如果新的直接证据证明错误采集／范围映射／秘密外发，再提出最小局部代码修订；AT08不预先改实现。

## 下一授权与停止线

**Successor = NOT READY**。没有可执行successor packet，没有安排模型复审。
精确下一动作：另行有界授权一次**只读的producer-side观测能力核查**，确认实际harness能否在决策时提供上述非秘密字段；同时明确输入／采集／scope证据契约。若不能，先给最小只记录不改策略的方案，仍不启动successor。

AT08仅新增裁定、设计、交接与checkpoint；原代码、policy、Foundation、历史证据保持不变。P3/P4与HELD pilots不动。到此停止。

