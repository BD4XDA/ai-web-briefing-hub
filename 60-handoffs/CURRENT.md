# 当前交接

状态：仓库刚初始化，尚无进行中的任务。

下一次网页端提出需求时：

1. 在 `00-inbox/` 记录原始需求。
2. 整理为 `10-briefs/YYYY-MM-DD-主题.md`。
3. 在此文件写明负责人、当前状态、下一步及相关文件。

<!-- LAB-OS-CANONICAL-20260921 -->
## 2026-09-21 · 当前课题组基础设施工作
已有 DSH / Sol-Luna / Claude Code / Codex 工程的基础规范现位于 `40-work/lab-research-os/`。
处理此项目时，读取该目录的 `AGENTS.md`、`PROJECT.md`、`CHECKPOINT.md`；本页仅作入口，不维护第二份状态。
此前“仓库刚初始化”的记录保留为历史。Outdex、简历与战雷项目仍后置。
<!-- /LAB-OS-CANONICAL-20260921 -->

<!-- EVIDENCE-PROPORTIONALITY-20260922 -->
Evidence proportionality is now canonical for Lab Research OS: agents must not calculate or repeat hashes by default. Use direct inspection, Git diff/status, schema checks or targeted tests unless an explicit byte-identity, boundary-integrity, immutable-checkpoint or tampering/staleness claim requires a digest. Read scoped `CHECKPOINT.md` through `foundation.py show`; Decision 0005 records the rule.
<!-- /EVIDENCE-PROPORTIONALITY-20260922 -->

<!-- AT04-CLOSURE -->
AT04 closure: P5 UNCERTAIN; P6 YELLOW. Canonical handoff: [AT04](../40-work/lab-research-os/artifacts/at04/ASTRA-TIME-04-HANDOFF.md). Read scoped checkpoints/LATEST.json through foundation.py; this index does not duplicate state.

<!-- AT05-CLOSURE -->
AT05 handoff: [AT05](../40-work/lab-research-os/artifacts/at05/ASTRA-TIME-05-HANDOFF.md). Read scoped LATEST through foundation.py for current authoritative state.

<!-- AT06-CLOSURE -->
AT06 diagnostic handoff: [AT06](../40-work/lab-research-os/artifacts/at06/ASTRA-TIME-06-HANDOFF.md). Scoped LATEST remains authoritative.

<!-- AT07-CLOSURE -->
AT07 repair-verification handoff: [AT07](../40-work/lab-research-os/artifacts/at07/ASTRA-TIME-07-HANDOFF.md). Scoped LATEST remains authoritative.

<!-- AT08-CLOSURE -->
AT08 adjudication/design handoff: [AT08](../40-work/lab-research-os/artifacts/at08/ASTRA-TIME-08-HANDOFF.md). Scoped LATEST remains authoritative.

<!-- SOL-CHECKPOINT-MIRROR-CONSTRAINT -->
Human PI hard constraint: every Foundation checkpoint must update the generated latest-checkpoint section in [SOL-AGENT.md](../40-work/lab-research-os/SOL-AGENT.md) before `checkpoints/LATEST.json` advances. Decision: [0004](../40-work/lab-research-os/decisions/0004-sol-agent-checkpoint-mirror.md). Scoped LATEST remains authoritative.

<!-- AT10-CLOSURE -->
AT10 responsibility audit and supervised Phase-0 exit decision preparation: [handoff](../40-work/lab-research-os/artifacts/at10/AT10-HANDOFF.md). Canonical registered root is `D:/项目仓库/赛博课题组/40-work/lab-research-os`; read its current LATEST through Foundation. Four audit artifacts and governance proposals are preserved; proposals are not adopted and the PI phase decision is pending. AT08 gates remain unchanged, AT09 remains preliminary. Stop: no automatic AT11, successor or research pilot.
<!-- /AT10-CLOSURE -->

<!-- AT11-CLOSURE -->
AT11 source binding is **PACKET_READY** at Foundation checkpoint `20260927T221637-5ab599164add`: [Decision 0007](../40-work/lab-research-os/decisions/0007-at11-s1-source-binding.md), [binding](../40-work/lab-research-os/artifacts/at11/D-SOURCE-BINDING.md), [future packet](../40-work/lab-research-os/packets/at11-first-supervised-research.json). Human PI approved bounded read-only location of the DOI `10.5194/bg-18-1451-2021` original; the canonical archived PDF was directly identified and bound. No scientific task or future executor/reviewer ran. Separate Human PI run authorization remains required; no automatic AT12, AT09 promotion, successor/F5/F6 or infrastructure work.
<!-- /AT11-CLOSURE -->
