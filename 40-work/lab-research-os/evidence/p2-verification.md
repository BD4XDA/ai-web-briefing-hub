# P2 contracts 验证

**Claim**：contracts 的确定性验证通过；DeepSeek Flash 复核未形成可用模型报告，因此模型复核状态为 UNCERTAIN，不能推断 PASS 或模型真实性。

**Evidence**：`evidence/p2-test-run.json`：`python -m unittest tests.test_contracts -v`，10/10，exit code 0；测试文件 SHA256 `B4688D42939C83AC3E590D89F556E596BBD1BF69896C653C1145BE4D06641A67`；实现文件 SHA256 `B4517C1AC37062377B8899ED1F84EA535C88B90ED25CC73AEEA82F769FCF93D1`。`evidence/p2-deepseek-review-raw.json` 保存唯一一次 Flash CLI 调用的已清理失败证据。

**Verification Method**：在临时目录构造合法与非法 task-packet、evidence、bundle、report；真实校验 packet/evidence/verification schema，因 `schemas/project.schema.json` 尚未提供，仅对 bundle inventory 的 `project` record 使用临时 `schema_check` mock。覆盖 root mismatch、write escape、resolved traversal、hash mismatch、malformed report、missing evidence、FAIL/UNCERTAIN/低置信度/未解决 anomaly、evidence 数量超 `max_files`、record evidence 未被 report 覆盖。随后按协议发起一次 `claude -p --safe-mode --tools \"\" --effort low --output-format json`，提示 reviewer 读取测试证据而非执行测试。

**Result**：确定性测试 `PASS`。DeepSeek 复核 `UNCERTAIN`：CLI 报告 `unrecognized_model` 警告，限定等待内没有返回模型报告；未重试。

**Confidence**：测试结果 `1.0`；模型复核 `0.0`（无可评阅响应）。实际模型身份未得到可靠字段，不能将配置别名视为真实性证明。

**Anomaly/Conflict**：模型复核失败/超时是未完成的异构复核，不否定确定性测试；inventory schema 仍是 P3 限制，生产 inventory 语义尚未测试。应由 owner 决定是否以确定性证据独立接受 P2，或在后续容量可用时补一次复核。
