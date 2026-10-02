# Daily Paper integration · recovered state

Observed through 2026-09-30.

## CORRECTION 2026-09-30 — Codex heartbeat is live and rollover is complete

The 2026-09-29 investigation searched DSH Schedule storage, the legacy task-board ledger and Windows Task Scheduler and found no task there. That result was accurate for those subsystems but was incorrectly generalized to the Codex app. Fresh direct Codex evidence resolves the conflict:

- Codex automation `automation-2` is ACTIVE at 08:00 Asia/Shanghai and is the single `每日沉积物磷论文整理` heartbeat;
- its prompt uses the canonical `D:\项目仓库\赛博课题组` root and includes bounded retries, passive cost telemetry and context-lifecycle rules;
- the fresh `每日论文` successor resolved checkpoint `20260929T190136-77fa33d54c35`, accurately reported issue 022 as PARTIAL and named replacement of the blocked Chinese candidate without rerunning research;
- the existing automation now targets that successor, and the predecessor conversation is archived rather than deleted.

Consequence: no manual DSH task creation is needed and no second automation may be created. Codex `automation-2` is the current trigger; DSH's empty schedule is not evidence against it.

## OBSERVATION 2026-10-01 — trigger delivery works; persistent model pinning remains partial

The first observed scheduled turn reached the successor, but its effective parent route was `gpt-6.1-sol/medium` rather than the required `gpt-6-luna/low`. The recurring prompt's parent-route gate failed closed before literature discovery, download, extraction or scientific recomputation. Issue 022 and its two accepted SCI files therefore remain unchanged.

This separates two claims that must not be conflated:

- schedule delivery and successor targeting are **LIVE**;
- automation-level persistent Luna/low pinning is **PARTIAL**, because the current Codex heartbeat contract exposes no independent model field.

Until the scheduler can guarantee the requested route, a mismatched turn must stop and report the hold; it must not silently spend Sol/Astra capacity or create a replacement automation. The smallest scientific continuation remains replacement of the blocked Chinese candidate under Luna/low and the shared three-attempt cap.

## Existing workflow

- The active Codex conversation is titled `每日论文` and is attached to the same saved project as Lab Research OS; the predecessor is archived as historical reference.
- One active Codex heartbeat (`每日沉积物磷论文整理`) targets that conversation at 08:00 Asia/Shanghai. No second automation is required.
- The private Skill and archive implement one Chinese core plus two SCI full-text papers, optional supervisor-paper add-on, personal/supervisor notes, legal-access rules, deduplication, rendering QA and index maintenance.
- The current master index reaches issue 021 dated 2026-09-26. This establishes archive existence, not scientific validation of every historical note.
- A directly authorized 2026-09-29 production trial opened issue 022 but stopped at `PARTIAL`: two lawful SCI PDFs were retained, the Chinese-core full text was readable online, and the original Chinese PDF remained blocked by connection closure, HTTP 429 and a publisher safety challenge. No formal note or index entry was fabricated.

## Interrupted work

The latest explicit Daily Paper task paused new daily selection and requested historical repair: normalize 73 personal notes, add appropriate original-paper figures to personal and supervisor versions, and add non-invented process/reasoning diagrams. The parent and three bounded child ranges initially failed because the account usage window was exhausted. The real Event pilot later resumed note 073 from the preserved workspace and completed it. Independent verification found and repaired an overlong published supervisor path; the same regression gate found one more issue-021 supervisor path and repaired it. Six notes still lack complete full text. Note 072 is the next content-repair unit; the repair must not restart or be silently treated as complete.

## Status table

| Capability | Status | Basis |
|---|---|---|
| Existing archive and issue workflow | IMPLEMENTED & OBSERVED | Master index and issue 021 folders |
| Existing heartbeat schedule | IMPLEMENTED & LIVE configuration | Codex automation-2 is ACTIVE, points to the verified successor and uses the current canonical root |
| Private Skill after root migration | IMPLEMENTED & VERIFIED locally | New target exists and system Skill junction is readable after repair |
| Daily Paper → Lab OS prompt binding | PARTIAL LIVE EVIDENCE | Event pilot and issue-022 TIME trial followed resume/evidence boundaries; a complete upgraded issue remains unverified |
| Cost-aware delegation | DEFECT OBSERVED, POLICY REPAIRED | Issue 022 used no Astra/subagent but consumed 20.87M reported tokens in Luna/medium; three-attempt stop, passive telemetry and Luna/low parent gate are now live rules |
| Evidence-ready daily records | PARTIAL LIVE | Issue 022 preserved DOI/source/status/claim labels and an exact continuation point; formal issue evidence remains incomplete |
| Human PI Daily Research Brief | VERIFIED FOR EVENT AND PARTIAL TIME RUNS | Ten-section briefs reflect actual work; complete new-issue behavior remains unverified |
| Weekly/event/milestone/state readiness | PROPOSED, NOT DEPLOYED | Workload classification only |
| Historical 73-note repair | PARTIAL | Note 073 complete; note 072 is next; six notes remain full-text blocked |
| Persistent automation-level model pinning | PARTIAL | A Luna/low turn was applied and the heartbeat now fails closed on a non-Luna/low parent; heartbeat metadata still has no independent model field |
| Future-note source visuals, workflows and portable paths | IMPLEMENTED BUT UNVERIFIED live | Private Skill, output contract, recurring prompt and opt-in validators updated; no complete new issue has yet passed both gates |

## Minimum continuation points

1. Next heartbeat: restore the latest user instruction and incomplete repair state before deciding whether a new issue may start; always generate the brief from actual work only.
2. Next upgraded run: start from the issue-022 continuation point or replace the blocked Chinese candidate; keep Luna/low, a fresh short context and the three-attempt cap. Do not repeat the two SCI downloads or the failed Chinese access paths.
3. Historical repair: resume note 072 from preserved evidence only when explicitly continued; finish one bounded unit before opening another review loop.
4. Historical path portability: 34 supervisor files remain over the new budget after the two issue-021 repairs. Treat bulk migration as a separately approved Event with a reversible rename map and reference update.


## 2026-10-02 · Human PI直接要求两篇已有SCI读书笔记
两篇原文复用；个人DOCX/PDF与导师DOCX完成，各7页，28渲染页已检查；笔记图文/路径检查PASS。022仍PARTIAL，缺中文核心和期次简报。最小续接仅中文合法全文及其笔记、简报和整期验证；不得重复已有两篇QC。73篇历史修复继续PARTIAL/PAUSED。详见私有当日运行记录及canonical checkpoint。


## VERIFIED UPDATE 2026-10-02 — issue 022 completed under Luna/low

The existing issue-022 TIME workflow resumed after the first route gate had stopped. The effective continuation route was verified as `gpt-6-luna/low`. The blocked Chinese candidate was replaced without revisiting the two accepted SCI papers. Issue 022 now contains three legal full texts, three personal DOCX/PDF pairs, three supervisor DOCX files, and a ten-section personal Human PI Daily Research Brief DOCX/PDF. The Chinese-core selection is a declared freshwater method-value exception; results are explicitly bounded to Erhai Lake and not treated as marine evidence. `validate_issue.py --require-visuals --require-portable-paths` passed with 3/3/3 note counts, one brief pair, no errors or warnings. New note and brief pages were visually reviewed against the original paper and their renderings. The detailed evidence and limitations are in the private 2026-10-02 corpus run log and master index.

This is one verified complete post-contract issue for visual/path acceptance; it is not evidence for universal repeatability or for unrelated workflow readiness. The historical 73-note repair remains `PARTIAL/PAUSED`. The private evidence record remains Discovery/Extraction/Evidence and was not promoted to validated knowledge. The primary run telemetry plus one token-free correction entry are in the shared local ledger.

Next daily turn: resume from the master index and latest run log, reuse issue 022 as closed, and run only the current Literature Radar / daily workflow under Luna/low. Do not resume the historical repair without a new direct Human PI request.

## VERIFIED ROLLOVER 2026-10-02

The issue-022 continuation consumed 12,533,537 turn tokens, including 11,982,336 cached input tokens; the conversation cumulative total reached 19,668,737. That direct evidence triggered proactive rollover under the marginal-context-value rule. Compact successor `01a0fc40-dd4c-7652-a971-5475aca1f4cc` resolved checkpoint `20261002T185443-bebb0c725d03`, reported issue 022 CLOSED and performed no research. One initial readiness attempt ended in a transport disconnect; the second succeeded within the shared three-attempt budget. Existing `automation-2` now targets the compact successor, and long conversation `01a0ecd4-1374-7df2-ad32-672e28bddac6` is archived rather than deleted. No duplicate automation was created.
