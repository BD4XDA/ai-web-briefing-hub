# Foundation P1 机械验证

**Claim**：foundation checkpoint 写入、完整性和恢复保护行为通过验证；测试使用临时目录，未修改 `tools/foundation.py`、真实 checkpoint 或运行模型。

**Evidence**：`evidence/foundation-test-run.json`（测试文件 SHA256 `0D5E8C23D85830EAAFDAB7C04719A1E375B71181E55217B8CEA902F40959F108`，原始 stdout、exit code=0、8 tests）；`evidence/inherited-evidence-index.json` 记录 7 个既有证据的绝对路径、大小和 SHA256；P0 文件已复制为 `evidence/p0-health-worker.json`（SHA256 `852754D6BA34F6C05F9B13BDCCD741713E8B40AA07B21333AD9E7F06B506A6BD`）及 `evidence/p0-health-worker.md`（SHA256 `8841C8B01339D0F6177FED23E8920731C82313FFE2DD871FC0C000F1D027FBD2`）。

**Verification Method**：运行 `python -m unittest discover -s tests -v`；每个测试创建独立临时 root，使用 `.lab-project.json` marker。覆盖必填字段/evidence、正常写入读取与 hash、stale expected 保旧状态、已有 writer.lock 保留、snapshot 篡改拒绝、模拟 CHECKPOINT `os.replace` 失败时 LATEST 不前进且旧 checkpoint 可读、子目录 root 识别，以及实际 hub CURRENT 备份作为前缀。

**Result**：PASS，8/8，exit code 0，运行时间 2026-09-21T13:06:42+08:00。

**Confidence**：高；断言直接作用于临时文件系统和实际只读交接文件。实现未改动。

**Anomaly/Conflict**：未发现测试失败。`foundation.py` 在模拟 CHECKPOINT 替换失败后会留下未提交的新 snapshot 文件，但 LATEST 保持旧指针；测试只要求旧状态可读，未把孤立 snapshot 视为已提交状态。
