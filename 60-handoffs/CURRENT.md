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

<!-- CANONICAL-ROOT-CONTEXT-ROLLOVER-20260929 -->
The canonical repository has returned to `D:/项目仓库/赛博课题组`; the former `D:/20_代码项目/赛博课题组` location is a compatibility junction to the same files, not a second repository. Lab Research OS now uses proactive conversation rollover under [Decision 0016](../40-work/lab-research-os/decisions/0016-canonical-root-return-and-context-rollover.md): compare marginal context value with cached-context cost and reliability risk, checkpoint all material state first, verify a file-only successor resume, repoint the existing schedule and archive rather than delete the predecessor. The current Daily Paper conversation meets the trigger because the issue-022 trial reported 20,867,481 total tokens and three compactions; its successor must resume from the latest checkpoint without repeating the two acquired SCI papers.
<!-- /CANONICAL-ROOT-CONTEXT-ROLLOVER-20260929 -->

<!-- ROLLOVER-PREP-AND-HEARTBEAT-CONFLICT-20260929 -->
At Foundation checkpoint `20260929T203829-b113799fa300`, the Daily Paper successor bootstrap is written and file-only resume references are verified, but **the 08:00 heartbeat could not be found**: the running lab-research profile has no `storages/schedule.json`, the legacy `task-board` ledger is empty, no matching Windows scheduled task exists, and no DSH session log ever recorded a `schedule_create` call or the heartbeat title. No session file changed between 2026-09-28T20:00 and 2026-09-29T12:26 local, so the 08:00 delivery did not occur. Bootstrap and exact continuation point: [SUCCESSOR-BOOTSTRAP-2026-09-30.md](../40-work/lab-research-os/artifacts/daily-paper/SUCCESSOR-BOOTSTRAP-2026-09-30.md). The recurring prompt's stale junction path was corrected after a dated backup. Human PI must locate the task in the running GUI to decide repoint versus recreate; no second automation was created.
<!-- /ROLLOVER-PREP-AND-HEARTBEAT-CONFLICT-20260929 -->

<!-- GPT61-SOL-ROLLOVER-CLOSURE-20260930 -->
Human PI authorized GPT-6.1 Sol adoption and continuation of the interrupted work. Active Sol routing now targets `gpt-6.1-sol`: low for focused work, medium for everyday judgment and high for consequential independent review; xhigh/max are evaluation/PI gated, while Astra is reserved for highest-stakes cross-system or L3 exceptions. DeepSeek remains unchanged. The Codex app directly showed the existing active `automation-2`, so the earlier DSH/Windows search was too narrow to prove global absence. The verified fresh `每日论文` successor now owns that single heartbeat; the predecessor is archived, not deleted. Decision: [0017](../40-work/lab-research-os/decisions/0017-gpt61-sol-and-daily-paper-rollover.md). Evidence: [GPT61 migration](../40-work/lab-research-os/artifacts/GPT61-SOL-MIGRATION-2026-09-30.md). Read scoped LATEST through Foundation for the current checkpoint.
<!-- /GPT61-SOL-ROLLOVER-CLOSURE-20260930 -->


## 2026-10-02 · 每日论文笔记交付
Human PI直接要求的第022期两篇SCI读书笔记已完成；整期仍PARTIAL。当前最小续接与状态以40-work/lab-research-os/CHECKPOINT.md及artifacts/daily-paper/CURRENT-STATE.md为准；不维护第二套科研档案。


## 2026-10-02 · 每日论文第022期完成
Human PI已要求补齐中文论文并形成读书笔记。第022期三篇论文的个人DOCX/PDF、导师DOCX和个人Daily Research Brief DOCX/PDF现已完成；新视觉与便携路径门禁通过。详细目录、论文列表和证据记录位于D盘总索引及2026-10-02运行日志。Lab OS状态见`40-work/lab-research-os/artifacts/daily-paper/CURRENT-STATE.md`与最新Foundation checkpoint。历史73篇修复仍PARTIAL/PAUSED，须待Human PI直接续接。

第022期完成后，原执行对话出现1198万cached-input token的高成本，已按context lifecycle完成第二次rollover。现有`automation-2`原位指向新successor `01a0fc40-dd4c-7652-a971-5475aca1f4cc`；高成本对话`01a0ecd4-1374-7df2-ad32-672e28bddac6`已归档，未删除、未新建第二个automation。

## 2026-10-06 · DSH Desktop 启动画面

Human PI 指定的 `lxj5820/dsh-boot-animation` 已按上游 `v0.2.0` 安装至 DSH Desktop `desktop` profile。当前 Desktop `0.2.0-rc.2` 与插件合同匹配；插件模块、设置逻辑和本地视频清单路由已验证，三段素材均已启用且为 fast-start。安装前 profile patch 备份与卸载路径均已保留。该项目是可选外观扩展，不纳入科研 capability registry，不改变 DSH core、模型路由或科研流程。证据与回滚说明见 [安装记录](../40-work/lab-research-os/artifacts/DSH-BOOT-ANIMATION-INSTALL-2026-10-06.md) 和 [决策](../50-decisions/2026-10-06-dsh-boot-animation.md)。

## 2026-10-06 · 每日论文第023期完成

第023期已从保存的合法开放全文续接并完成：1篇中文核心、2篇SCI，个人版DOCX/PDF、导师版DOCX、原文PDF、总索引和Human PI Daily Research Brief均已交付。最终视觉与便携路径门禁为0 error / 0 warning；Chemical Geology裁图和化学式缺字已修复后重新验证。实际目标路由经会话证据确认为`gpt-6-luna/low`，未使用Astra、子代理或高推理模型。

该目标回合最终报告17,514,298 token，其中17,113,216为cached input。科研产物有效，但上下文效费比不合格；下一期必须从项目状态在新短上下文中恢复，不得把已完成的第023期长对话作为默认历史。详细状态见[Daily Paper current state](../40-work/lab-research-os/artifacts/daily-paper/CURRENT-STATE.md)与最新Foundation checkpoint。历史73篇修复仍为PARTIAL/PAUSED。

2026-10-07已完成主动rollover：新会话`01a114e8-2997-7f50-b227-3d9cb3fa3778`仅凭项目文件准确恢复，现有`automation-2`仍为ACTIVE并原位改指向新会话；旧高成本会话`01a0fc40-dd4c-7652-a971-5475aca1f4cc`已归档而未删除。第024期尚未开始，不得重复第023期。

## 2026-10-07 · 每日论文机构全文通道

Human PI确认学校图书馆、校园网/机构VPN或代理、出版社订阅、学校合作知识库、文献传递及已有本地原文均可用于私有科研工作流。每日论文不再以OA为入选前提，优先最快的完整原文通道；自动任务与私有Skill已同步更新。账号凭据与会话材料不得记录或输出，受订阅许可约束的原文不得提交到公开GitHub，摘要仍不能代替全文精读，三次失败上限与效费比规则不变。决策见[2026-10-07-institutional-fulltext-access](../50-decisions/2026-10-07-institutional-fulltext-access.md)。

发现层已进一步扩展到Crossref、OpenAlex、Unpaywall、CORE、PubMed/PMC、Europe PMC、Semantic Scholar、Google Scholar、机构/作者/学科仓储及学校授权中文知识库，避免反复死磕官网。Sci-Hub与未授权影子镜像不进入自动下载路径。候选的正式发表身份、DOI和期刊质量须独立核验；作者接受稿或预印本必须标记版本并绑定正式DOI。决策见[2026-10-07-broad-literature-discovery-and-version-verification](../50-decisions/2026-10-07-broad-literature-discovery-and-version-verification.md)。
