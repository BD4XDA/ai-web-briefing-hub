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

<!-- GPT6-MIGRATION -->
Current project-owned GPT targets are generation 6 at Foundation checkpoint `20260927T222534-4ceb3f3a3a79` under [Decision 0008](../40-work/lab-research-os/decisions/0008-gpt6-model-generation.md): Astra/former Terra responsibility=`gpt-6-astra`, Sol=`gpt-6-sol`, Luna=`gpt-6-luna`. No GPT 5.6 fallback is permitted for new tasks. Remaining 5.6 strings are preserved AT02 historical evidence, not current routing. External DSH/user/provider configuration was not changed or qualified.
<!-- /GPT6-MIGRATION -->

<!-- GPT6-COST-DSH-PUBLIC-20260928 -->
GPT-6 cost routing, DSH portability and public-release assessment completed at Foundation checkpoint `20260928T132433-391786e56d73`. The canonical repository is now `D:/20_代码项目/赛博课题组`; the Lab Research OS root is `40-work/lab-research-os/`. Current GPT defaults are Luna/low, Sol/medium and Astra/medium, with Sol/high or Astra/high only for declared risk/complexity and `xhigh` evaluation- or PI-gated. DeepSeek and external DSH/provider configuration were not changed. Installed DSH `0.1.1-rc.2` is statically compatible with project instructions/workspace tools but not newly end-to-end qualified; upstream npm latest is `0.1.5-rc.3` and next is `0.1.7-rc.2`. Public packaging is feasible but held for a clean sanitized export, license/security/contribution files, synthetic examples and clean-room CI. Assessment: [GPT6-DSH-PUBLIC-RELEASE-ASSESSMENT.md](../40-work/lab-research-os/artifacts/GPT6-DSH-PUBLIC-RELEASE-ASSESSMENT.md). Routing source: [model-routing.json](../40-work/lab-research-os/config/model-routing.json). AT11 remains PACKET_READY and unexecuted.
<!-- /GPT6-COST-DSH-PUBLIC-20260928 -->

<!-- DAILY-PAPER-PILOT-20260929 -->
At Foundation checkpoint `20260929T000830-e6268772584d`, the existing `每日论文` conversation and its single 08:00 heartbeat are the approved first Lab Research OS production/shadow workload under [Decision 0011](../40-work/lab-research-os/decisions/0011-daily-paper-production-shadow-pilot.md). The private Skill path migration was repaired. Daily work is limited to Literature Radar, the existing paper workflow and the Human PI Daily Research Brief; readiness work follows declared weekly/event/milestone/state triggers and is not newly scheduled. The historical 73-note image/flowchart repair remains PARTIAL/PAUSED after quota failures and must resume from preserved artifacts, not restart. Public-release scaffold files remain unrelated and uncommitted.
<!-- /DAILY-PAPER-PILOT-20260929 -->

<!-- DAILY-PAPER-VISUAL-CONTRACT-20260929 -->
At Foundation checkpoint `20260929T112730-2f53d2723c4d`, [Decision 0012](../40-work/lab-research-os/decisions/0012-daily-note-visual-contract.md) makes evidence-bearing source visuals and method/research workflow diagrams a standing requirement for every future personal and supervisor Daily Paper note. The private Skill, output contract, heartbeat prompt and opt-in validator are updated. Historical validation remains backward-compatible; a completed new issue has not yet live-qualified the contract. The real Event pilot is currently resuming note 073 only from preserved evidence.
<!-- /DAILY-PAPER-VISUAL-CONTRACT-20260929 -->

<!-- DAILY-PAPER-READINESS-V3-20260929 -->
At Foundation checkpoint `20260929T120741-8786a6aaca0b`, the real note-073 Event pilot is complete and boundedly verified. Independent QA exposed a published-path defect: a staged DOCX could render while the overlong final path could not open directly in Word. Two issue-021 supervisor filenames were shortened and now open/render from their final locations. [Decision 0013](../40-work/lab-research-os/decisions/0013-daily-paper-portable-paths-and-pilot-observation.md) adds the `--require-portable-paths` gate for new issues: filename <=140 characters and absolute path <=240 characters; complete English titles remain inside the note and index. Thirty-four historical supervisor paths remain an explicit Event backlog and were not bulk-renamed. A complete post-contract new issue is still required before the visual/path contract is live-qualified. See [v3 report](../40-work/lab-research-os/artifacts/daily-paper/RESEARCH-READINESS-INTEGRATION-REPORT-v3.md).
<!-- /DAILY-PAPER-READINESS-V3-20260929 -->
