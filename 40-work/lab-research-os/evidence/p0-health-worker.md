# ASTRA TIME P0 最小健康确认

**Claim**：P0 核心证据仍在；DSH smoke、restart/resume、API probe 与 team recovery 文件可读且哈希稳定。当前实验 run 已 checkpoint，但最后的 Sol review 因连接断开/usage limit 失败；已有 draft、packet 和恢复所需上下文。

**Evidence**：

- `outputs/evidence/dsh-smoke.json` SHA256 `E2D4F2FC1DDF040BAB52DF9100EC247D594464949B80F06964388A0DEA34CFEB`，`passed=true`。
- `outputs/evidence/dsh-restart-resume.json` SHA256 `49C3FDE38D65D3284D6C50D5B3A1441CA5EF7CBE730D6EAB271D9C6B15B946E6`，`passed=true`。
- `outputs/evidence/api-probe.json` SHA256 `D27F9E6C9A6C4C5990D92D1E55BFA2E48D8293CF6C7698DFE92F6C2C92760086`；`team-recovery.json` SHA256 `EB3996A3EA8CC2E02C68D00C310A90D5095D303DD0194ACB06C3CC7A0D77278B`，记录 `ok=true`、team `active`。
- `outputs/lab-os/run-20260921/checkpoint.json` SHA256 `6D3D08C9289EBDFEC167D3D013A9E61D504A11422EA148B7F0BA8A3D264D3541`，状态 `CHECKPOINTED_FAILURE`。

**Verification Method**：只读读取 JSON/markdown、计算 SHA256，并执行 `Get-NetTCPConnection -LocalPort 3080`；观察时间 `2026-09-21 13:00:46 +08:00`。未启动/终止进程，未改凭据/全局配置，未重跑付费模型流水线。

**Result**：`P0 PASS_WITH_BLOCKED_REVIEW`。当前 `127.0.0.1:3080` 为 `NO_LISTENER`，因此 web 服务此刻未运行；历史证据显示恢复路径已验证，实验产物可从 checkpoint 继续。

**Confidence**：高；端口结论是当前瞬时状态，API/team 结论基于既有证据文件而非新探测。

**Anomaly/Conflict**：Sol review 记录 `exit_code=1`，原因包含 stream disconnect 和 usage limit；checkpoint 已明确下一步为基于 packet/锚定不确定性恢复。无监听时无法提供当前 PID 归属，不能据此推断旧 PID 状态。

**最小恢复动作**：需要 web 访问时，沿用已记录的 recovery patch，仅禁用 `web-ui-task-board` 后启动一次，再复核 3080；实验 run 仅在 review 容量可用后从 checkpoint/task packet 恢复，不重跑全面普查或完整原始语料。
