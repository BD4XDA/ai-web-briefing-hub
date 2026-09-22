# P2 provenance clarification

**Claim**：现有 P2 证据混合了 AT01 与 AT02 时间线；确定性测试证据属于 AT02，DeepSeek review 记录属于 AT01，不能把后者当作 AT02 review 完成证据。

**Evidence**：

- `checkpoints/20260921T181551-5e0214f704e7.json` 的 committed state 写明：AT02 entry 时 “P2 contracts and test source exist; P2 run and DeepSeek review were absent”，且当前 worker 正在补齐这些证据。
- `evidence/p2-test-run.json` 的 `started_at`/`finished_at` 是 AT02 checkpoint 附近的归档字段；其 stdout 是从工具回显整理出的格式化文本，不是独立保存的原始终端文件。`0.5284s` 是外层工具 wall time，stdout 内 `0.132s` 是 unittest 自报运行时间，两者量测层级不同。
- `evidence/p2-deepseek-review-raw.json` 的 `started_at=2026-09-21T13:16:34+08:00`，早于 AT02 的 `18:15:51+08:00` checkpoint，因此只能归为 AT01 尝试。当前 workspace 没有保存该 shell session 的原始 stdout/exit/status 文件；该 JSON 是当时可见 warning 与观察结果的清理记录，不能还原完整原始响应。
- `outputs/evidence/claude-flash-smoke-v2.json` 是另一项早先的 smoke：记录 `exit_code=0`、`stop_reason=end_turn`、`modelUsage.deepseek-flash[1m]`，但 prompt 是 `CLAUDE_FLASH_OK`，不是 P2 review。`outputs/lab-os/run-20260921/flash-extract-execution.json` 也是独立科研 run，不能充当 P2 review。

**Verification Method**：只读比对 committed AT02 checkpoint、现有 P2 文件时间/内容及两份历史 Claude 运行 artifact；未重跑测试或模型调用。对 Claude 过程，仅能确认 13:16:34 左右存在一个此前启动的 CLI 进程、stderr 出现 `[claude-code:unrecognized_model] ... query_source=generate_session_title`，随后在等待窗口后不再可见；没有可靠的 exit code、终止信号或响应正文记录。

**Result**：AT02 deterministic test provenance = `PASS_WITH_FORMATTED_OUTPUT`；AT02 DeepSeek review provenance = `MISSING`。AT01 CLI warning 是观察到的旁带信息，不能被解释为推理失败原因，也不能据此判定实际 inference model。

**Confidence**：AT02/AT01 时间线归属 `0.95`；原始 stdout/终止状态缺失结论 `0.95`；任何关于 warning 因果或模型真实性的结论 `0.0`。

**Anomaly/Conflict**：现有 `p2-verification.md` 将 AT01 的 `p2-deepseek-review-raw.json` 描述为唯一 Flash 调用，但它不能代表 AT02 review；该描述应由 owner 视为过期/需修订的 provenance。未静默重构 raw test output，也未把历史 smoke 结果冒充 P2 review。
