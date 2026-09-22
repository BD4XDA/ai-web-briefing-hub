# Instruction adapter audit

Scope was bounded to the shared hub instruction files, Codex `config.toml` project-document keys, installed DSH instruction-loader source/README, local Claude help, and a path/count-only Claude memory inventory. No model was started and no source/config file was changed.

## Findings

- `AGENTS.md` is the canonical hub contract. It requires `60-handoffs/CURRENT.md`, the relevant `10-briefs/` file, and related `50-decisions/` files in that order ([AGENTS.md](C:/Users/ASUS/Documents/Codex/2026-09-05/gu/ai-web-briefing-hub/AGENTS.md:3), hash `C913EF212073BA4DD1AD0A216294A11FFC5C7FBC6C503639CDD38AB259AB21CF`). The earlier `CURRENT.md` reading that reported a newly initialized repository with no active task is a pre-change baseline (lines 1-9, hash `EC592A55DB67BC20FA35DCB5E48F9B23AFD1BCA1DBC69D5E63CD16D590E22982`), preserved at `canonical/evidence/legacy/hub-CURRENT-before-20260921.md`. The current file has hash `A3927C7EAE4214F3916F36D4A13F6AC2D3C36F5E6E59A75782C6257139C4A2FC` and appends the `LAB-OS-CANONICAL-20260921` pointer at lines 11-16.
- The hub's `CLAUDE.md` and `DEEPSEEK.md` are thin pointers to `AGENTS.md` (both verified by line-numbered reads and SHA-256). `DEEPSEEK.md` does not prove that DSH auto-loads that filename.
- The inspected Codex config contains project tables including the hub path but no `project_doc`, `project-document`, or document-limit key. This is an absence claim for the inspected file/version only; config hash is `5FBD306F3DF69818329751040FAE4A6B54C211649514F47C7B91998DDFB59A23`.
- Installed `@deepseek-ai/dsh-agent-instructions` defaults to `AGENTS.md`, `CLAUDE.md`, `AGENTS.local.md`, and `CLAUDE.local.md`; it walks upward to the first configured root marker (default `.git`), then loads candidates from root through cwd. Same-directory trimmed-content duplicates collapse to the earliest candidate. Source: `lib/index.js` lines 466-480, 488-498, 524-572; README lines 5-13 and 57-72. `DEEPSEEK.md` is not a default candidate.
- Local Claude Code `2.1.258` help explicitly mentions `CLAUDE.md` auto-discovery and `--add-dir (CLAUDE.md dirs)`. Local help did not document `@import`; mark that behavior unverified rather than assuming it.
- Claude auto-memory inventory found 20 `~/.claude/projects/*/memory` directories and 79 immediate files total. Only paths/counts were inspected; contents were not read.

## Minimal discovery and priority boundary

For this hub, the minimal project-root discovery set is `.git` root plus `60-handoffs/CURRENT.md`, `AGENTS.md`, `CLAUDE.md`, and `DEEPSEEK.md`. The adapter boundary is: Codex `AGENTS.md` remains canonical; Claude `CLAUDE.md` points to it; DSH uses its actual `dsh-agent-instructions` candidate/root traversal and must not infer automatic `DEEPSEEK.md` loading.

## Recommended thin adapters

Codex: preserve `AGENTS.md` as the single canonical contract and its explicit handoff/brief/decision order.

Claude: keep `CLAUDE.md` as a pointer to `AGENTS.md`; use verified auto-discovery; leave `@import` unclaimed until official local documentation is found.

DSH: use the installed loader's configured candidate lists and root-marker walk. Add or configure candidates explicitly if a non-default name is required.
