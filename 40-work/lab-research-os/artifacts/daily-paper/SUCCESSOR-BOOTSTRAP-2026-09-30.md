# Daily Paper 继任会话 bootstrap（context rollover）

状态：READY_FOR_HUMAN_PI_CREATION · 生成于 2026-09-30（承接 Foundation checkpoint `20260929T201634-0d642f05e654` 之后的滚动工作）

## 使用方式

在 DSH Web GUI 的实验室 Workspace（规范根 `D:/项目仓库/赛博课题组`）新建一个会话，模型固定为 `Luna / low`，把下面“Bootstrap 提示词”整段作为第一条消息粘贴。不要沿用旧的长会话。

## Bootstrap 提示词（整段复制）

```text
你在承接“每日沉积物磷论文整理”这一既有 heartbeat 工作流，本次只做继任会话的就绪确认，不要开始新的检索或下载。

硬约束（必须遵守）
1. 规范工作根：D:\项目仓库\赛博课题组；Lab Research OS：D:\项目仓库\赛博课题组\40-work\lab-research-os。
   D:\20_代码项目\赛博课题组 只是兼容 junction，不是第二个仓库；不要使用它。
2. 论文数据根：D:\10_学业科研\论文_沉积物磷（保持不变）。
3. 模型与预算：本次与后续每日运行使用 Luna/low；不启用子代理；不调用 Astra；不升级模型。
   单个候选的等价公开访问路径累计失败 3 次即止损换候选。
4. 本次只读文件、只做就绪确认：不浏览、不下载、不渲染、不重跑任何科学判断、不写正式笔记、不改总索引。

请按顺序只读以下文件后回答
- D:\项目仓库\赛博课题组\40-work\lab-research-os\CHECKPOINT.md
- D:\项目仓库\赛博课题组\40-work\lab-research-os\artifacts\daily-paper\CURRENT-STATE.md
- D:\项目仓库\赛博课题组\40-work\lab-research-os\artifacts\daily-paper\WORKLOAD-CLASSIFICATION.md
- D:\10_学业科研\论文_沉积物磷\90_智能体工作区\04_Lab_Research_OS\contracts\2026-09-29_每日论文_recurring_prompt.md
- D:\10_学业科研\论文_沉积物磷\90_智能体工作区\04_Lab_Research_OS\运行记录\2026\2026-09\2026-09-29.md
- D:\10_学业科研\论文_沉积物磷\90_智能体工作区\02_临时文件\2026-09-29_第022期\原文候选\ 目录清单

然后只输出下面四行，不要输出别的内容
第1行：RESOLVED_CHECKPOINT=<你读到的 checkpoint ID>
第2行：ISSUE_022_STATE=<PARTIAL 或 COMPLETE>
第3行：NEXT_ACTION=<你在中文核心候选上将要执行的最小下一步，一句话，含具体路径>
第4行：WILL_NOT_REPEAT=<你确认不会重做的已完成工作，逗号分隔>
```

## 继任会话在就绪确认之后的最小续点（供你判断其输出是否正确）

- 第022期仍为 PARTIAL：两篇 SCI 原文已合法取得并保存在
  `D:\10_学业科研\论文_沉积物磷\90_智能体工作区\02_临时文件\2026-09-29_第022期\原文候选\`
  （`nature-lucapcycle.pdf` 约 3.36 MB / 16 页；`gca-vivianite.pdf` 约 1.07 MB / 15 页），**不得重新下载**。
- 中文核心候选（刘忠航等 2023，双齿围沙蚕，DOI `10.19663/j.issn2095-9869.20220111003`）的出版社原始 PDF 未取得：
  `cn-polychaete.pdf` 当前仅 59 bytes、`cn-fep-review.pdf` 为 0 bytes，均**不是有效 PDF，不得当原文使用**。
- 因此正确的 `NEXT_ACTION` 是二选一，且必须含具体路径：
  (a) 若 Human PI 已人工下载有效 PDF 放入上述 `cn-polychaete.pdf`，先校验 PDF 文件头/页数，通过后继续该候选的笔记生产；
  (b) 否则按三次封顶规则直接更换中文核心候选，并把新候选的合法全文落到同一目录。
- `WILL_NOT_REPEAT` 应包含：两篇 SCI 的检索与下载、中文候选的网页全文阅读、第022期已完成的去重与元数据核对。

## 未决事项（继任会话不要自行处理）

- 08:00 heartbeat 的宿主任务需要重指到本继任会话；在 Human PI 确认之前，不要新建第二套定时任务。
- 历史 73 篇笔记配图/流程图修复仍为 PARTIAL/PAUSED，只有 Human PI 明确要求才续接。
