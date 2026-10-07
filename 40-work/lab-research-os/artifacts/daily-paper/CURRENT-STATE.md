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
| Daily Paper → Lab OS prompt binding | IMPLEMENTED & VERIFIED FOR TWO ISSUES | Issues 022 and 023 completed from project-owned state with evidence boundaries, daily briefs and required validators; this does not prove universal repeatability |
| Cost-aware delegation | PARTIAL; CONTEXT-COST DEFECT OBSERVED | Issue 023 used Luna/low and no Astra/subagent/high reasoning, but the completed target turn still reached 17.51M reported tokens, 17.11M cached input; the next cycle requires a fresh short context |
| Evidence-ready daily records | IMPLEMENTED & VERIFIED FOR ISSUES 022–023 | Legal originals, DOI/source metadata, labeled inference boundaries, notes, briefs, index entries and run logs are present and validated |
| Human PI Daily Research Brief | IMPLEMENTED & VERIFIED FOR COMPLETE TIME RUNS | Issues 022 and 023 each produced the ten-section personal DOCX/PDF brief from actual work without daily recomputation |
| Weekly/event/milestone/state readiness | PROPOSED, NOT DEPLOYED | Workload classification only |
| Historical 73-note repair | PARTIAL | Note 073 complete; note 072 is next; six notes remain full-text blocked |
| Persistent automation-level model pinning | PARTIAL | A Luna/low turn was applied and the heartbeat now fails closed on a non-Luna/low parent; heartbeat metadata still has no independent model field |
| Future-note source visuals, workflows and portable paths | IMPLEMENTED & VERIFIED FOR ISSUES 022–023 | Both completed post-contract issues passed `--require-visuals --require-portable-paths`; Issue 023 passed after final crop and glyph repairs |

## Minimum continuation points

1. Next heartbeat: treat Issues 022 and 023 as closed and begin Issue 024 only from the master index, current project state and the latest run log. Use Luna/low, a fresh short context and the shared three-attempt cap.
2. Do not carry the completed Issue-023 conversation forward as default context. Its final target-turn report was 17,514,298 tokens, including 17,113,216 cached input; marginal context value is now below its cost.
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

## VERIFIED UPDATE 2026-10-06 — issue 023 completed; fresh-context gate required

Issue 023 resumed from preserved open-access full texts and completed under the directly verified target route `gpt-6-luna/low`; no Astra, subagent or high-reasoning scientific model was used. The issue contains one Chinese core paper and two SCI papers, three lawful source PDFs, three personal DOCX/PDF pairs, three supervisor DOCX notes and one Human PI Daily Research Brief DOCX/PDF. The master index and append-only run log were updated. A clipped Chemical Geology source crop and missing chemical-formula glyphs in agent-drawn material were repaired, all affected files were re-exported, and `validate_issue.py --require-visuals --require-portable-paths` passed with zero errors and zero warnings.

Scientific boundaries remain explicit: the Haiyang Xuebao paper reports total P2O5 rather than operational P fractions; the Chemical Geology study is an early-Proterozoic model rather than a modern coastal observation; the Frontiers study represents one spring cruise. These outputs remain Discovery/Extraction/Evidence and were not promoted automatically to validated long-term knowledge.

The final target-turn usage report was 17,514,298 tokens: 17,437,859 input, 17,113,216 cached input, 76,439 output and 27,151 reasoning output. This is an unacceptable context-efficiency profile despite correct low-cost model routing. Before Issue 024, continue from project-owned state in a fresh short context; do not replay the completed conversation. The historical 73-note repair remains `PARTIAL/PAUSED`.

## VERIFIED ROLLOVER 2026-10-07

Fresh successor `01a114e8-2997-7f50-b227-3d9cb3fa3778` (`每日论文｜Issue 024 起点`) completed a file-only recovery under `gpt-6-luna/low`. Without research or file changes it correctly identified checkpoint `20261007T134817-28a68e940a67`, Issues 022–023 as complete, Issue 024 as not started, the historical 73-note repair as `PARTIAL/PAUSED`, and no need to repeat Issue 023. Existing heartbeat `automation-2` remains ACTIVE at 08:00 Asia/Shanghai and was repointed in place to this successor. The high-cost predecessor `01a0fc40-dd4c-7652-a971-5475aca1f4cc` was archived, not deleted. No duplicate automation was created.
