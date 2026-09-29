# DeepSeek Harness 0.1.7-rc.2 upgrade report

Date: 2026-09-29. Scope: local Harness maintenance and bounded qualification; no research conclusion or private corpus transmission.

## Outcome

- Global `@deepseek-ai/dsh` upgraded from `0.1.1-rc.2` to npm `latest` `0.1.7-rc.2`. The `next` channel `0.2.0-rc.1` was not installed.
- A pre-upgrade configuration backup was created at `C:/Users/ASUS/.dsh/backups/dsh-core-upgrade-20260929-121654`; sessions and attachments were not copied or modified.
- The legacy `web` profile is retained. It is not the qualified route because `@softspark/dsh-codex@1.0.0` is rejected by the new exact peer guard, its latest release still targets older DSH packages, and its patch then references a missing `llm-codex` entry.
- New clean profiles `lab-research` and `lab-headless` were created from the shipped 0.1.7 templates. `lab-research` uses `deepseek-flash`, `workspace-write`, and disables only the rebuildable projection cache that fails on historical `agent-team:<id>` filenames on Windows. The source session logs remain authoritative and untouched.
- The DSH launcher now uses `lab-research`; the legacy profile remains available for later plugin migration.

## Verification

- `dsh --version` returned `0.1.7-rc.2`.
- The clean Web profile listened on `127.0.0.1:3080` and rendered the DeepSeek Harness interface.
- The UI listed and selected the `D:/20_代码项目/赛博课题组` workspace with `workspace-write` access.
- A bounded headless call from the canonical Lab Research OS root returned exactly `DSH_OK` through one model step. Reported usage was 7,693 input and 4 output tokens.

Status: DSH core and the two clean laboratory profiles are **LIVE & QUALIFIED for bounded text/headless and Web use**. The legacy Sol/Luna router, Codex adapter and Exa route are not thereby qualified.

## Known limitations

- The custom Sol/Luna router still contains GPT-5.6 and retired DeepSeek model identifiers and old DSH peer ranges. It is excluded from the clean profiles until migrated and tested.
- Historical Web plugins remain in the legacy profile; one UI package is deprecated. They are not bulk-updated.
- Disabling the projection cache may make historical session listing slower; it does not remove the session logs.
- DSH remains a developer preview. Updates require manual review and representative qualification rather than automatic installation.

## Rollback

Reinstall `@deepseek-ai/dsh@0.1.1-rc.2` and restore selected configuration from the named backup only if the clean qualified profiles fail. Do not restore or delete sessions merely to satisfy a cache.
