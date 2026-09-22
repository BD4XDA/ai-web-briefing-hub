# AT06 — 分开诊断 F4、F5、F6（只读）

授权依据为本轮后发的“Blocked-Event Diagnosis → Minimum Repair Proposal”。它取代了本轮先发的允许修复／一次再验证草案。本轮不执行修复、回归、模型复审或新的恢复 worker。

入口 checkpoint 仍为 20260922T091418-c3831eb34892，无需回退历史 anchor。
C1 NOT PROVEN 表示恢复尚未实际受测，不表示 continuity FAILED。
C2 UNCERTAIN；P5 UNCERTAIN；P6 YELLOW 保持不变。

## F4：策略拒绝

**唯一分类：INSUFFICIENT_EVIDENCE。原始拒绝是否正确或属于缺陷：UNKNOWN。**

| 链条 | 能确认的事实／缺口 |
|---|---|
| worker 意图 | launch-input.json 明确要求运行一次 observe；worker.stdout 表达同一意图。 |
| 请求表示 | worker.stderr 的 exec_command 错误显示 pwsh.exe -Command 包装的 python “…/artifacts/at05/experiment.py” observe .。未保存原始工具参数对象及送入策略的规范化结构。日志中的转义不能当成真实 argv 损坏证据。 |
| CLI 配置 | worker-execution.json 记录 --ignore-user-config、--ephemeral、--sandbox read-only；未显式设置审批选项。CLI help 描述这些标志，但不还原历史有效策略。 |
| 策略评估 | 没有命中规则 ID、规则源码、输入分类、审批理由或有效配置快照。不能据默认值推断历史实际规则。 |
| 决策 | stderr 在 2026-09-22T01:10:57.567051Z 记录 codex_core::tools::router 的 CreateProcess Rejected / blocked by policy。它是拒绝结果的直接证据，但不证明由独立自动审批模型作出了语义判断。 |
| 执行 | 没有成功 command_execution、观察 payload 或 canonical 恢复结果。CLI 自身 exit0 仅表示会话结束，不是命令成功。 |
| 后果 | 任务脚本随后给出 FAIL 并阻止正式摘要写回；这一步发生在拒绝之后。 |

只读补查：当前 .codex/logs_2.sqlite 中精确 thread_id，以及 worker 的29秒窗口内 policy/approval/sandbox/router 元数据查询都未返回匹配记录。查询及边界保存在 diagnostic-evidence.json。没有扫描其他会话正文。常见用户／项目 rules 位置未发现可用规则；这不证明没有其他管理策略。当前用户配置含 danger-full-access／Windows elevated，但 AT05 显式忽略用户配置；不能据当前值补写历史有效设置。CLI help 不提供这次拒绝的规则溯源。

### 命令实际语义的静态检查

AT05 experiment.py 当前字节与启动前绑定一致。observe 分支从实际记录的子目录向上查找 marker，读取固定路径，并调用 foundation.current 校验 checkpoint；不调用 run、process、save、写回或 checkpoint 分支。foundation.py 在导入及 current 路径只读。父级 AGENTS.md 与 CURRENT.md 虽在 scoped root 外，但被 packet 单独列入允许读取范围。没有删除、移动、网络请求或读取凭据的显式操作。

不过，“完整进程必然纯只读”不能仅由脚本证明：原始工具参数、策略规范化输入、shell profile 实际加载、python 的 PATH 解析／环境均未完整保存。PYTHONDONTWRITEBYTECODE=1 是启动记录中的明确设置，但没有独立的子进程环境观测。代码没有请求秘密材料，也不能代替对所有 ambient runtime 行为的审计。checkpoint 在 controller 启动前检查过；被拒绝的 observer 没有再次观察它。

**边界判断**：拒绝可见于 Codex CLI exec_command/进程启动策略路径，发生在 Foundation 恢复逻辑执行前；可见组件不属于冻结 Foundation。具体产生拒绝的规则／集成组件仍未知。因此不提出策略修复、命令白名单或审批例外。

## F6：error 被计作额外工具动作

- **观察**：worker.stdout 的 item.completed / item.type=error，内容是 skills context budget exceeded。
- **表示**：同一 item 原样出现在 review-prompt.txt 的 package.other_tools；没有先规范化成真正的工具调用。
- **逻辑**：experiment.py:63 用“不是 command_execution/reasoning/agent_message/plan 的所有 item”定义 other_tools；error 不在排除集合。
- **影响**：第75行 no_other_tool=false；第86行非空 other_tools 令机械结果 FAIL；G1/G2 因此失败。第117行又仅依据门槛输出及未写回自报 C2 PROVEN，不能证明分类正确。
- **根因状态**：已定位的本地适配脚本缺陷。error 是诊断事件，不是额外 action 的证据。它没有导致先前 F4 的进程拒绝。
- **Foundation component? NO**：artifacts/at05/experiment.py 不在冻结 manifest 中；Foundation 的规则／checkpoint／schema 未显示该缺陷。
- **最小提议**：区分明确 action、diagnostic、unknown；只有有动作证据的类型才能计作额外 action。diagnostic 不自动升级为安全或 PASS，仍保留原消息。缺观察／未知类型保持 UNCERTAIN 并禁止写回；真实越界动作 FAIL 并禁止写回。执行被拒绝应保留 BLOCKED 的执行状态，不能翻译为 continuity failure。C2 不能仅凭“未写回”自行认证分类正确。
- **回归风险**：简单把 error 全部忽略会漏掉失败；类型白名单不完整会把新事件错误当安全。提议必须保留 unknown、错误状态和审计，不采用“除此之外都安全”。
- **回滚方法**：未来修改前绑定原字节，在单独派生文件中实现；必要时停用新派生版本，保留原文件／结果，不删除历史。
- **必要测试（未执行）**：真实原 error 不计工具动作但观察缺失仍阻止写回；合法成功观察；工具拒绝／进程失败；未知／畸形事件；额外越界／破坏性动作；混合 warning+action；没有独立审阅／低置信度均不得写回。

## F5：stderr 有哈希却没有内容

- **观察**：worker.stdout、worker.stderr 在 process 返回前写入；worker-execution.json 同时记录两者的 SHA-256。实际哈希与文件一致。worker 结束01:11:06.361625Z，模型审阅开始01:11:06.371514Z。
- **构造路径**：experiment.py:37–40 保存原始流；第88行 package 只放 execution receipt、thread_events、commands、other_tools 等投影，未放 stderr／完整 stdout 内容。receipt 的 hash 存在，review package 中原始 stderr 不存在。
- **根因状态**：已定位的证据包组装遗漏。没有 schema 限制要求省略；任务契约要求保留执行证据。代码选择了有限字段，作者主观上有意／无意不可由文件判定，不作心理推断。
- **可访问性**：DSH reviewer 工具被禁用且实际 tool_calls=0。它无法从哈希恢复原文，也不能自行读取本机 stderr，所以无法看到直接拒绝证据。
- **Foundation component? NO**：问题位于同一本地 experiment.py 的 package 构造，不属于冻结 Foundation 或 verification schema。
- **后果**：审阅者报告拒绝原因缺少直接证据，并提出不成立的“禁用审批与自动拒绝矛盾”；原始 stderr 支持拒绝，但仍没有策略根因。保留原审阅，不重写历史。
- **最小提议**：未来包直接绑定原始 stdout/stderr 的路径、字节数、哈希、编码与内容；保留派生事件并标明关联。完整性检查在送审前运行。超限、缺失、哈希不符、不可安全发送时明确停止／UNCERTAIN；不得静默截断。若发现秘密内容，先保留本地原件，另出有明确删改映射的安全审阅包，不能声称它是完整原流。
- **回归风险**：原始流可能含秘密、过长或编码异常。字节绑定和发送内容要区分；不能一味全量外发。
- **回滚方法**：未来独立派生组装文件、原始版本哈希与新版本并存；停用派生版本即可，不覆盖旧证据。
- **必要测试（未执行）**：确有内容的 stderr、合法空 stderr、stdout 多事件、缺文件、篡改、非法编码、超限／截断标记、含秘密的合成负例；缺证据一律不得包装成完整证据。

## 证据与责任范围

[diagnostic-evidence.json](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/40-work/lab-research-os/artifacts/at06/diagnostic-evidence.json) 保存命名文件哈希、启动前代码匹配、原始事件与 package 投影、代码行、流的哈希比较、时间先后、只读日志查询及 CLI help。
这是一份当前生成的诊断记录，不冒充 AT05 原始采集时间，也不执行 AT05 脚本。

结论：F5/F6 是已证明的任务脚本缺陷；F4 根因及拒绝正确性 UNKNOWN。没有已证明的冻结 Foundation 缺陷。本轮没有修复、回归／负控执行、独立模型复审或 successor 再验证。

